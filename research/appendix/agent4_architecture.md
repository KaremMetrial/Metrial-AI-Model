# Agent 4: Technical Architecture for a Multi-Tenant "Business Model + Monitoring + Auto-Investigation" SaaS

Date: 2026-11-19. Convention: **[V]** = verified from a cited source during this research; **[K]** = from my prior knowledge, not re-verified this session (check before committing); **[R]** = my recommendation/judgment. Several web sources were vendor blogs or aggregators; I flag that where it matters. Search tooling here was limited (some queries returned thin results), so items marked [K] deserve a quick check.

---

## 0. Executive recommendation (the decisive version)

1. **One Postgres (managed) as the system of record AND the first analytical store**, with a per-tenant *schema* for synced raw/staging data and RLS on shared control-plane tables. Add **DuckDB** (embedded, reading Parquet in object storage) as the analytical/"scratch" engine for heavy scans and for sandboxed LLM-generated queries. Defer ClickHouse until a single tenant's metric tables exceed roughly 100M-1B rows or dashboards need sub-second at scale. [R]
2. **Do not build a knowledge graph or adopt a graph DB.** Model entities, relationships and metric dependencies as typed relational tables (`entity`, `entity_link(type, valid_from, valid_to, confidence, source)`, `metric_dependency`). Use recursive CTEs for impact propagation. [R]
3. **Semantic layer: write your own thin YAML metric spec modeled on / convertible to OSI/MetricFlow**, compile to SQL yourself for the 5-10 metric shapes you need. Adopt MetricFlow (now Apache 2.0) only if you want its query compiler for free. Do not run Cube or a full BI semantic server in v1. [R]
4. **Ingestion: buy/borrow, don't build connectors.** dlt (code-first, Apache 2.0) + a few hand-written connectors for the top 3-5 systems; Nango for OAuth/credential plumbing and long-tail API access; Airbyte OSS only if you need breadth fast and accept ops burden. Fivetran is too expensive per-connection for SMB-margin products at small scale and now sits inside a dbt competitor-adjacent company (see 3). [R + V]
5. **Detection: statistical, deterministic, boring.** Robust seasonal decomposition (STL/MSTL) + residual z-score/MAD, plus statsforecast baselines (ETS/Theta/MSTL), CUSUM/EWMA for drift, ruptures/PELT only for post-hoc changepoint localization. Foundation models (Chronos-2) are an optional upgrade for series with short history, not a launch dependency. [R]
6. **Investigation = a deterministic analysis engine (dimension decomposition, bridge/waterfall, lagged correlation, event-window comparison) driven by an LLM planner that picks from a fixed tool menu.** The LLM never computes numbers; it chooses tools, reads results, writes narrative and hypotheses. Single agent loop on a durable workflow engine (Temporal or Inngest/plain Postgres-backed queue), not a multi-agent swarm. [R]
7. **"The AI learns the company" = a versioned, human-reviewed company model + memory tables + feedback labels fed into retrieval and thresholds. Not fine-tuning.** [R]
8. **Multi-tenancy: Postgres schema-per-tenant (or database-per-tenant for the first regulated customers) + RLS as defense in depth + per-tenant envelope encryption of credentials via a KMS.** Credentials in a vault service, never in the app DB. [R]
9. **"3-day onboarding" is credible only as: 3 days to first connected data + first draft model + first dashboards for 1-3 well-known systems; NOT 3 days to a validated company model.** Plan for ~2-4 weeks to a trusted, human-validated model. [R, with evidence in section 11]

---

## 1. Storage: warehouse vs ClickHouse vs DuckDB vs Postgres

**What the data actually looks like.** SMB/mid-market tenants: orders, invoices, GL entries, customers, products, tickets. Typically 10^5 to 10^8 rows per tenant. That is Postgres/DuckDB scale, not ClickHouse scale. [R]

| Option | Strengths | Weaknesses | Verdict |
|---|---|---|---|
| Postgres (managed: RDS/Aurora/Neon/Supabase) | One system for app + analytics; RLS; pgvector; transactional upserts for incremental syncs; ops familiarity | Row store: wide scans on 100M+ rows get slow; vacuum bloat on heavy upsert | **Default.** Use materialized/rollup tables for metric time series. |
| DuckDB (+ Parquet in S3/R2) | Embedded, no server, fast columnar scans, great for ad-hoc agent queries and sandboxing (read-only attach, memory/time limits, no network) | Single-writer; not a multi-user server; you manage files | **Add early** as the analytical engine for investigation queries and heavy aggregations; one file/prefix per tenant gives physical isolation for free. |
| ClickHouse (self-host/Cloud) | Best-in-class for large event data, real-time dashboards | Ops complexity, mutation/upsert awkwardness, cost floor on cloud | **Defer.** Adopt at ~100+ tenants or when one tenant has event-scale data (clickstream, telemetry). |
| Snowflake/BigQuery/Databricks | Zero ops at scale, native semantic features | Per-query cost, minimums, tenant-isolation modeling is on you, hurts unit economics for SMB | **Do not use as your core.** Instead *integrate* with the customer's if they already have one (read-only connector). |

[R] Rationale: a startup's biggest risk is not query speed; it is data correctness and onboarding speed. Postgres+DuckDB keeps the stack small enough for 2-4 engineers. The bronze/silver/gold split can live as schemas (`raw`, `clean`, `model`) inside the tenant schema.

**Not needed:** a lakehouse (Iceberg/Delta) in v1, Spark, a streaming bus (Kafka), a separate OLAP cluster, a feature store. Hourly/daily batch sync is enough for "continuous monitoring" of business metrics; real-time webhooks (Shopify, Stripe) can be an optimization for freshness. [R]

---

## 2. Semantic layer and OSI

**Verified state (2025-2026):**
- OSI (Open Semantic Interchange) was launched 2025-09-23, led by Snowflake with Salesforce, dbt Labs, BlackRock, RelationalAI and others; it is a vendor-neutral format for metrics, dimensions, datasets, relationships and context. [V] https://www.snowflake.com/en/blog/osi-initiative-expands-partners/ ; spec updates at https://www.getdbt.com/blog/the-osi-spec-updates
- dbt Labs open-sourced MetricFlow under Apache 2.0 (Oct 2025) as a reference implementation. [V] https://www.getdbt.com/blog/dbt-labs-affirms-commitment-to-open-semantic-interchange-by-open-sourcing-metricflow ; https://thenewstack.io/dbt-labs-open-sources-metricflow-an-independent-schema-for-data-interoperability/
- A dbt Summit session title refers to "Apache Ossie" for the portability effort; I could not confirm whether OSI was renamed or moved to Apache. [V that the string exists; unresolved] https://www.getdbt.com/dbt-summit/agenda/apache-ossie-realizing-semantic-layer-portability
- Fivetran and dbt Labs announced a merger in Oct 2025; secondary sources say it closed 2026-06-01. [V, secondary] https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement

**Others [K]:** Cube (open core, Apache/commercial, strong API/caching/multi-tenant security context), Malloy (Google-backed language, expressive but small ecosystem), Boring Semantic Layer (lightweight Python library on Ibis, YAML/Python; handy for agents). Wren AI's open-source "semantic engine" (MDL) is explicitly aimed at text-to-SQL context.

**Recommendation [R]:**
- Your product's semantic layer is **a core IP asset, not a plumbing choice**: it holds the validated company model (metric definitions, grain, filters, entity keys, caveats, owner, confidence). Keep it in your own tables + a YAML export in an OSI-compatible shape so customers' existing dbt/Snowflake definitions can be *imported* and yours can be *exported*. Importing existing definitions from a customer's dbt/Looker/PowerBI is a strong onboarding shortcut.
- Compile metric specs to SQL with a small in-house compiler (sum/count/ratio/derived/cumulative with time grain and dimensions; the "MetricFlow subset"). If compiler scope grows, embed MetricFlow (Apache 2.0) rather than writing a general engine.
- **Not needed:** Cube/semantic server as a runtime dependency, a GraphQL/REST semantic API for third-party BI, MDX compatibility.

---

## 3. Data ingestion

| Tool | License / model | Pricing notes | Fit |
|---|---|---|---|
| **Fivetran** | Proprietary SaaS | Per-connection billing since Mar 2025; $5 min per connection added Jan 2026; deletes/history rows count as billable [V, secondary: https://dataopsleadership.substack.com/p/fivetran-vs-airbyte-in-2026-complete ; https://nexla.com/?p=26553 (competitor, discount)] | Best connector quality (NetSuite, QuickBooks, Shopify) and has dbt packages. But *you* would pay per customer-connection and resell: margin risk. Option: let customers who already have Fivetran/Airbyte point you at their warehouse. |
| **Airbyte** | OSS (ELv2 core connectors mostly MIT/ELv2 [K]); Cloud capacity pricing | Self-host free but ops-heavy; Cloud capacity-based [V secondary] | Broadest long-tail; connector quality uneven; use for breadth when a customer needs an obscure source. |
| **dlt** (dlthub) | Apache 2.0 Python library [K] | Free; paid platform optional [K; no 2026 source found] | **Recommended core.** Code-first, schema inference + evolution built in, runs in your own workers, easy per-tenant destination/schema. You write ~1-2 days per connector for REST APIs. |
| **Meltano/Singer** | MIT [K] | Free | Singer tap quality is patchy and community maintenance has waned [K]. Skip. |
| **Nango** | Source-available (Elastic License v2, not OSI; cannot resell as managed service) [V secondary: https://www.getknit.dev/blog/nango-review-evaluation-integration-platform ; competitor pricing page https://www.merge.dev/blog/nango-pricing] | Usage-based; Free tier + paid plans [V secondary, figures unverified] | **Recommended for OAuth flows, token refresh, credential storage, and long-tail API passthrough/syncs.** Cuts a month of auth plumbing. Check ELv2 terms if self-hosting. |
| **Merge / Unified.to** | Proprietary | Merge ~ $650/mo for 10 linked accounts then ~$65/account; Unified.to usage-based, from ~$750/mo [V secondary: https://truto.one/blog/top-5-open-source-and-low-cost-alternatives-to-mergedev-2026/ ; https://unified.to/blog/unified_apis_usage_based_vs_per_connection_pricing_for_integrations; competitor-authored] | Normalized models are lossy (you want raw ERP detail, not a lowest-common-denominator "Invoice"). Merge's accounting category is useful for QuickBooks/Xero/NetSuite-class *speed*, but per-account fees hit SMB unit economics. Consider for accounting only, as a stopgap. |

**Recommendation [R]:** Phase 1: Nango (auth) + dlt (extraction) for 4-6 sources: Shopify, QuickBooks Online, Xero, Stripe, HubSpot, Postgres/MySQL, CSV/Sheets/S3 uploads. Phase 2: Airbyte OSS or Merge-style unified API for long tail on demand. Always land **raw, unmodified** data first (append + `_loaded_at`), then transform; this preserves auditability for evidence trails.

**Not needed:** your own connector framework, CDC/Debezium (except for customers with big transactional DBs, later), reverse ETL.

---

## 4. Schema discovery and entity resolution

**Schema discovery / mapping [R, K]:**
1. Deterministic profiling first: column types, cardinality, null rates, PK/FK candidates (inclusion dependencies), date/currency/amount heuristics, distribution stats. This is cheap and reliable.
2. Known-source "templates": for Shopify/QuickBooks/Xero/NetSuite/Stripe, ship pre-built mappings (like Fivetran's dbt packages, which standardize those schemas). 80% of SMB value comes from ~10 sources whose schemas are public and stable. See section 11.
3. LLM-assisted mapping only for the residual: propose "this column is `order_total_net_of_tax`" with sample values + neighboring columns + confidence, **always shown for human confirmation**, with deterministic checks (does SUM(line items) = header total? do invoices tie to GL?). LLM is a proposer, reconciliation tests are the judge.
4. Reconciliation tests as the validation primitive: totals tie to source reports (e.g. P&L revenue vs sum of invoices), row counts vs API counts, no orphan FKs, period continuity. These are what make a "validated" company model defensible.

**Entity resolution (customers, products, vendors across systems):**
- **Splink** (Ministry of Justice, MIT, Fellegi-Sunter probabilistic linkage, runs on DuckDB/Spark): recommended. Unsupervised EM training, explainable match weights (great for evidence trails). [K]
- **Zingg** (Spark/ML-based, active-learning): heavier, Spark dependency; skip. [K]
- **dedupe** (Python, active learning, in-memory): fine for small data, less maintained; skip. [K]
- LLM role: adjudicate the *ambiguous band* of pairs (match probability 0.3-0.8) and propose canonical names; never the first pass. Persist decisions as `entity_link` rows with `source=human|model`, so human overrides survive re-runs. [R]
- Most SMB resolution is deterministic: email, tax ID/VAT, domain, SKU, GL account codes. Do deterministic first, probabilistic second.

**Not needed:** a master-data-management platform; embeddings-based ER as the primary method.

---

## 5. Time-series anomaly detection with seasonality

**Verified foundation-model state:**
- Chronos-2 (Amazon, Oct 2025) reports 79.8% win rate / 46.6 skill score on GIFT-Eval vs 70.0%/42.4 for TimesFM-2.5 and 56.0% for Moirai-2.0, as reported by the authors. [V] https://arxiv.org/pdf/2510.15821
- Moirai 2.0 (Salesforce) paper: https://arxiv.org/html/2511.11698v3 [V]. A 2026 blog claims licensing differences (TimesFM 3.0 weights non-commercial; Moirai weights non-commercial); I could not verify against primary sources, so **check licenses before any commercial use**. https://www.beri.net/article/timesfm-vs-chronos-vs-moirai-time-series-foundation-model-licence-bigquery-sagemaker-cost-2026 [V that claim exists; unverified]
- These are *forecasting* benchmarks; none of the sources I found validated them for *anomaly detection* on business metrics. [V gap]

**Recommended layered approach [R]:**
- **Layer 1 (day-one):** For each metric x slice: MSTL/STL decomposition (weekly + yearly/monthly seasonality, holiday/calendar regressors, payday effects), robust residual scoring (median/MAD) with a **prediction interval**; require *persistence* (k of n points) and *materiality* (absolute and relative impact in business units, e.g. revenue at stake) before alerting. Materiality gating is what reduces alert fatigue far more than a fancier model.
- **Layer 2:** statsforecast (Nixtla, Apache 2.0, fast ETS/Theta/MSTL/AutoARIMA) for forecast-based intervals and backtests. Prophet works but is slower, and its maintenance has slowed [K]; statsforecast is the better default.
- **Layer 3:** CUSUM/EWMA for small persistent shifts (conversion rate drifts). `ruptures` (PELT/BinSeg) to localize *when* a level/trend shift started, which is essential for the investigation step (which window to compare).
- **Context-aware / adaptive:** (a) calendar/event regressors (promotions, holidays, price changes pulled from the company model); (b) per-metric learned sensitivity from user feedback ("not an anomaly" lowers score weight for that slice); (c) hierarchical reconciliation: alert at the level where signal-to-noise is best and drill down.
- **Optional Layer 4:** Chronos-2 zero-shot forecasts for series with <1 year of history or many covariates; evaluate by backtest on tenant data before use. ADTK and Merlion are reasonable libraries but unmaintained or heavy [K]; skip.

**Not needed:** deep-learning anomaly detectors (autoencoders, TranAD), GPU inference, an LLM looking at raw time series. Do not let an LLM decide "is this an anomaly."

---

## 6. Causal/RCA methods

**What actually works in practice [R, K]:**
1. **Dimension decomposition ("drivers analysis")**: when metric M changes between window A (baseline) and B, attribute the delta to dimension values (region, channel, product, customer segment). Adtributor (Bhagwan et al., NSDI 2014) uses surprise (JS divergence) + explanatory power across one dimension at a time; commercial tools (Sisu-style) generalize to multi-dimension combos. For ratio metrics, decompose via mix/rate effects (Simpson's-paradox-safe). This is deterministic SQL + math, and it is the highest-ROI feature in the whole product.
2. **Metric tree/bridge decomposition**: revenue = orders x AOV; orders = sessions x conversion. Walk the tree via `metric_dependency` to find which child moved. Also deterministic.
3. **Event/change correlation**: join the changepoint window against an events table (deploys, price changes, promotions, stockouts, integration outages). Temporal proximity gives *candidate* explanations.
4. **Quasi-experimental causal estimates, used sparingly:** CausalImpact (Bayesian structural time series, synthetic control from unaffected control series) or DoWhy/EconML for estimating the effect of a *known intervention* (e.g. promo, price change) when good control series exist. These need assumptions (no confounder, stable pre-period relation) that are rarely verifiable in SMB data. Present as "estimated effect, conditional on assumptions: [list]."
5. **Granger causality**: only predictive precedence, not causation; confounded by shared seasonality and common drivers. Use at most as a *hypothesis ranking feature* and label it as such. Do not present Granger results as "X caused Y."

**Confidence separation [R]:** store two scores: (a) *observation confidence* (data freshness, completeness, reconciliation status, statistical significance of the anomaly) and (b) *explanation confidence* (explanatory power of the decomposition, whether a mechanism was tested, whether alternative hypotheses were ruled out, evidence type: observed-decomposition vs correlational vs causal-estimate). Mark every explanation with an **evidence grade**: `arithmetic identity` > `decomposition attribution` > `temporal coincidence with event` > `correlation` > `LLM-suggested/unverified`. UI shows the grade, not a single false-precision percentage.

**Not needed:** full structural causal model discovery (PC/GES algorithms), causal graph learning from observational data. Hand-authored metric trees plus decomposition cover most value.

---

## 7. Knowledge graph vs relational (decisive)

**Decision: relational tables with typed relationships. No graph DB.** [R]

Why:
- Your graph is small (thousands to low millions of nodes/tenant), shallow (impact propagates 2-4 hops: product -> order -> customer -> revenue metric), and mostly **typed and known in advance**. Postgres handles this with recursive CTEs trivially.
- Impact propagation is mainly: (a) metric dependency DAG (tree math), (b) entity-to-metric attribution (SQL group-bys), (c) entity-entity links with weights (supplier -> SKU -> order lines). All are relational joins/aggregations that must be consistent with the same warehouse numbers anyway. A graph DB would duplicate data and add a consistency problem.
- Graph DB brings ops cost, a second query language, a second tenant-isolation model.
- "Knowledge graph" as a marketing concept can be a *view*: expose `entity` and `entity_link` as a graph in the UI. Revisit only if you need variable-depth path queries over >10^8 edges (unlikely) or customers demand Neo4j export.

Suggested core tables [R]: `entity_type`, `entity`, `entity_link(type, from, to, valid_from, valid_to, confidence, provenance)`, `metric`, `metric_dependency`, `metric_slice`, `event`, `anomaly`, `investigation`, `hypothesis`, `evidence`, `decision`, `outcome`, `feedback`.

---

## 8. Vector search and RAG

- **pgvector** (or pgvectorscale) in the same Postgres is sufficient for ≤ millions of chunks/tenant. Per-tenant isolation via the same schema/RLS as everything else. No Pinecone/Weaviate/Qdrant needed. [R]
- **Where RAG matters:** unstructured context: contracts, SOPs, Slack/email threads, past investigation write-ups, user notes, metric definitions' descriptions, runbooks. It matters for **explanations ("a supplier contract changed pricing on Oct 1")** and for retrieving relevant *past investigations/decisions* (institutional memory).
- **Where RAG does not matter:** numeric analysis. Never retrieve numbers by embedding similarity; compute them with SQL. Embedding-search over column names/metric descriptions is useful for *schema linking* (picking relevant tables for a question); keep catalog small enough that a metric-menu in the prompt (hundreds of metrics) is better than retrieval.
- Hybrid retrieval (BM25 via Postgres FTS + vectors, simple rerank) is enough. [R]

**Not needed in v1:** document ingestion pipelines for arbitrary files (do a few: PDF/Docs/Notion/Drive later), GraphRAG, rerank services.

---

## 9. LLM roles and where deterministic computation must be used

**Text-to-SQL realities (verified):**
- Spider 2.0 (ICLR 2025): on enterprise-style workflows, an o1-preview code agent solved **21.3%** vs 91.2% on Spider 1.0 and 73.0% on BIRD. [V] https://github.com/xlang-ai/Spider2 ; review summary https://www.themoonlight.io/review/spider-20-evaluating-language-models-on-real-world-enterprise-text-to-sql-workflows
- By mid-2026, leaderboard entries reportedly reach ~70%+ with heavy agent scaffolding (aggregator figures; subsets/metrics unclear; the repo also notes an eval-suite fix in Aug 2026). [V, low confidence] https://benchmarklist.com/benchmarks/spider_2_0/ ; https://github.com/xlang-ai/Spider2
- Snowflake: 90%+ accuracy on its *internal* 150-question benchmark with a curated semantic model; on public BIRD, 57% without semantic model vs 78% with. [V, vendor] https://www.snowflake.com/en/blog/engineering/cortex-analyst-text-to-sql-accuracy-bi/ ; Databricks reports 75.68% on BIRD private test in its research paper https://arxiv.org/html/2509.21459v1 [V, as reported by search summary]
- Takeaway [R]: accuracy is high *when a curated semantic layer constrains the question space* and poor on raw messy schemas. This is exactly the argument for the semantic layer in section 2.

**Division of labor [R]:**

| Task | LLM? | Deterministic? |
|---|---|---|
| Detect anomaly, score, materiality | No | Yes (stats) |
| Compute decomposition, bridges, deltas, correlations | No | Yes (SQL/Python tools) |
| Choose which analyses to run, in which order | Yes (planner over fixed tool menu) | Tool execution |
| Generate ad-hoc SQL for exploratory questions | Yes, constrained (read-only, against semantic views/model schema, with row/time limits, result validation) | Execution + validation |
| Metric/schema mapping proposals | Yes (proposer) | Reconciliation tests (judge) |
| Hypothesis generation (non-obvious: "supplier delay", "pricing change") | Yes | Testing each hypothesis with data tools |
| Narrative, summaries, next-step suggestions | Yes | Numbers injected from tool outputs, never typed by model (templated number slots / structured outputs, post-check that every number in text appears in evidence) |
| Causal claims | Only from graded evidence | Estimator outputs with assumptions |

Rule: **every number in a user-facing explanation must carry a pointer (query ID + result hash) to an executed computation.** Enforce with a post-generation validator.

**Agent orchestration [R]:**
- Single-agent tool-use loop (Anthropic/OpenAI function calling) with a bounded step/budget limit and fixed tool menu is sufficient. Multi-agent (planner/critic/specialist) is **not justified** now: it multiplies cost, latency and failure modes; a "critic" pass can be a second call in the same workflow (check evidence-grade rules) rather than an autonomous agent.
- Durable execution: **Temporal** (robust; heavier ops, Temporal Cloud paid) vs **Inngest** (serverless, simpler, step functions) vs **Dagster** (best for asset-based data pipelines, sync/transform) vs **LangGraph** (graph abstraction for agent state; adds framework lock-in; not needed for a linear investigate loop) [K]. Recommendation: **Dagster or plain cron+queue for data pipelines; Inngest or Postgres-backed queue (e.g. pg-boss/Procrastinate/River) for investigations** with idempotent steps and persisted state. Move to Temporal at ~100 tenants if workflows get long/complex. Avoid LangChain-style abstractions; use the provider SDK directly with your own tool registry.
- Model choice: use a frontier model for planning/hypotheses and a cheaper model for classification/summarization/mapping proposals; cache aggressively; keep cost per investigation tracked as a first-class metric.

---

## 10. Eval systems

[R] unless noted.
1. **Golden incidents:** curate 30-100 historical cases per vertical (real, anonymized, with a known root cause established by the customer). Score: did the system find the true driver in top-k hypotheses? Was the evidence grade correct? Did it avoid claiming causation unsupported?
2. **Synthetic fault injection (highest leverage early, since you have little real labeled data):** take real/clean tenant data (or generated demo data), inject known faults: revenue drop in one region, price-change-driven AOV shift, duplicate-order bug, missing data feed, currency conversion error, stockout, seasonality shift. You know ground truth by construction. Measure recall@k of the true cause, false-alert rate on un-injected periods, numeric faithfulness.
3. **Component evals separate from end-to-end:** detector precision/recall at a fixed materiality threshold; decomposition correctness (unit tests against closed-form); mapping accuracy vs hand-labeled mappings; text-to-SQL execution accuracy on a tenant-specific question set; narrative faithfulness (every number traceable).
4. **LLM-as-judge pitfalls:** self-preference bias, verbosity bias, position bias, poor calibration on numeric correctness, judge sees the answer key leaking, agreement with humans must be measured on a labeled subset. Use judges only for style/clarity/"does the explanation address the question"; use programmatic checks for correctness. Use pairwise comparison with swapped order, and re-validate judge vs human labels quarterly.
5. **Tooling:** Langfuse (open-source MIT core, self-hostable; tracing + datasets + evals), Braintrust (hosted; strong eval UX), Inspect (UK AISI; open-source eval framework, good for agentic evals with sandboxing) [K for all three; verify current pricing/licenses]. A pragmatic pick: **Langfuse for tracing + your own pytest-style eval harness over golden/synthetic sets in CI**; add Inspect if you want a reusable agent-eval framework.
6. **Production feedback loop:** thumbs-up/down + "was this the real cause?" at investigation close + outcome tracking (section 7 tables) are your long-run eval data; this is the moat.

---

## 11. "3-day onboarding": feasibility

**Evidence (verified or semi-verified):**
- Standardized connectors + prebuilt models for popular sources exist: Fivetran/dbt packages for Shopify, QuickBooks, NetSuite etc. produce standard tables quickly; this is the basis of "days not months" for *known* sources. [K; Fivetran docs/dbt hub; not re-fetched here]
- Auto-modeling/semantic-model generation tools exist (Snowflake semantic-model generator, Databricks Genie spaces, Wren, Cube). Their reported high accuracy comes *with curation*: Snowflake's 90%+ is an internal benchmark with curated models and an "agentic semantic model improvement" loop; on public BIRD, auto/no-semantic-model gets 57% vs 78% with it. [V, vendor] https://www.snowflake.com/en/blog/engineering/agentic-semantic-model-text-to-sql/ ; https://www.snowflake.com/en/blog/engineering/cortex-analyst-text-to-sql-accuracy-bi/
- Enterprise text-to-SQL on uncurated schemas is still weak (Spider 2.0 figures above). [V]

**What can be automated in 3 days [R]:**
| Step | Automatable? | Human needed |
|---|---|---|
| OAuth/connect, initial backfill | Yes (hours; API rate limits can stretch backfill to a day+) | Customer admin grants access (often the real delay: IT approval, ERP admin) |
| Schema profiling, PK/FK, type inference | Yes | None |
| Mapping of standard sources to canonical model (revenue, orders, customers, COGS, AR/AP) | Mostly (templates for known systems) | 30-60 min confirm |
| Metric catalog draft (revenue, GM, AOV, churn, DSO, inventory turns) | Yes from templates + LLM naming | Finance/ops lead confirms *definitions* (net vs gross, tax, refunds, fiscal calendar): the main judgment-heavy step |
| Entity resolution | Deterministic yes; fuzzy needs review queue | Review ambiguous pairs (hours of work, not minutes) |
| Reconciliation to the customer's own reports | Automated checks, but breaks reveal real data-quality or definition issues | Humans resolve; often reveals custom fields, manual journal entries, multi-currency, multi-entity |
| Anomaly baselines | Need history (ideally ≥1 year weekly/daily seasonality); backfill gives it if source has history | Context on known events |
| Custom ERPs, heavy customization, spreadsheets-as-system-of-record | No | Weeks |

**Honest claim:** "Connected, first metrics and anomalies on standard systems in 3 days; validated model in 2-4 weeks; long-tail/custom in 4-8 weeks." Define "onboarded" by a measurable gate (reconciliation within x% of customer's P&L, metric definitions signed off by a named owner). I'd recommend offering a human "solutions engineer" onboarding layer early; it is cheaper than perfect automation and generates labeled training data for the automation. [R]

---

## 12. What "the AI learns the company" means technically [R]

Concretely, a persistent, queryable, versioned context consumed at inference time:
1. **Company model** (entities, metric definitions with owner/rationale, calendars, fiscal rules, known events, seasonality notes, thresholds per metric). Versioned; changes require review; every definition change is audit-logged.
2. **Memory of investigations and decisions:** past anomalies, accepted root causes, rejected hypotheses, decisions taken, outcomes. Retrieved (hybrid search + structured filters) into the investigator's context: "last 3 times conversion dropped in region X it was a payment-gateway outage".
3. **Feedback-calibrated parameters:** per-metric/slice alert thresholds, hypothesis priors (which causes were historically true in this tenant), suppression rules. This is classical statistics/Bayesian updating, not model training.
4. **User glossary/instructions:** "when we say 'active customer' we mean ...", stored as structured definitions + retrieved text.

**Fine-tuning verdict:** No, not in v1 or v2. Reasons: tiny per-tenant data, cost, drift with model upgrades, data-governance headaches, and prompt+retrieval+tools capture nearly all of the value. Consider fine-tuning (or distillation) only later, on *cross-tenant, de-identified, consented* tasks like schema-mapping classification or hypothesis ranking, to cut cost on a small model. [R]

---

## 13. Tenant isolation and security

**Isolation options [R, K]:**
| Model | Pros | Cons | When |
|---|---|---|---|
| Shared tables + Postgres RLS (`tenant_id`) | Cheapest, simplest migrations | One bug/missing policy = cross-tenant leak; noisy neighbors; backup/delete per tenant harder | Control-plane tables (users, settings, model metadata) only |
| **Schema-per-tenant** | Strong logical isolation, easy per-tenant export/delete, per-tenant roles, still one cluster | Migration fan-out; catalog bloat past a few thousand schemas | **Default for tenant data up to ~hundreds of tenants** |
| DB-per-tenant (or cluster/VPC-per-tenant) | Strongest isolation, per-tenant KMS/residency/restore | Costly, ops overhead | Regulated/enterprise tier, residency requirements, "private cloud" |

- Use RLS *plus* schema separation (defense in depth), per-tenant DB roles, and `SET ROLE` per request; automated cross-tenant leakage tests in CI (try every API with another tenant's token).
- DuckDB/Parquet: separate object prefix/bucket per tenant with scoped IAM; encrypt with per-tenant KMS key (envelope encryption; AWS KMS per-tenant keys cost ~$1/key/month [K]).
- **Vector namespaces:** same schema as the tenant's data (pgvector table in tenant schema) so isolation is inherited; if using an external store, per-tenant collection/namespace plus a server-enforced filter, not a client-side one.
- **Credentials:** never store customer tokens in app tables in plaintext. Options: Nango (stores/refreshes OAuth tokens), AWS Secrets Manager/GCP Secret Manager (simple, per-secret pricing ~$0.40/secret/month [K]), HashiCorp Vault/OpenBao (more ops; use only if multi-cloud/on-prem). Prefer **read-only scopes** at source and ask customers for dedicated read-only DB users.

**LLM-app security [R]:**
- **Prompt injection from data content** is the main novel risk: a product name, invoice memo, support-ticket text or file contents can contain instructions. Controls: treat all tenant data as untrusted; wrap in delimited data blocks; no tool that can write, send, or exfiltrate; the model's tools are read-only and parameterized; **no outbound network** from the analysis sandbox; render outputs without auto-loading remote images/links (markdown-image exfiltration); structured outputs validated against schema; separate the "reader of untrusted text" step from the "planner with tools" step where possible (dual-LLM/quarantine pattern).
- **Least-privilege execution:** per-tenant read-only DB role scoped to semantic views; statement timeout, row cap, memory limit; SQL parsed (e.g. sqlglot [K]) and allow-listed to SELECT on approved relations; DuckDB in a container with no network and a read-only mount.
- **Audit logs:** immutable log of every tool call, query text, rows returned count, prompt/response hashes, who/what triggered; customer-visible. Doubles as the evidence trail.
- **Data residency:** pin tenant region at creation (EU/US), use region-pinned model endpoints (Bedrock/Vertex/Azure regions), keep embeddings and logs in region.
- **Model-provider terms:** Anthropic API zero-data-retention is available by request per organization, covers the commercial API, with exceptions (e.g. features like prompt caching/Batch/Files may override, and some models require 30-day retention and are not ZDR-eligible unless authorized) [V] https://platform.claude.com/docs/en/build-with-claude/zero-data-retention ; https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to . For OpenAI/Google/Azure/Bedrock: I did not verify current terms this session; [K] Bedrock and Vertex/Azure offer in-tenant-cloud processing with no training on customer data and region selection, and Azure OpenAI abuse-monitoring logging can be opted out by approval. **Verify each in contract before promising a customer.** Recommendation: route via your own cloud account (Bedrock/Vertex) for the strictest customers; keep a provider abstraction so a tenant can pin a provider/region.
- **SOC 2 pathway [R + V on costs]:** Vanta/Drata/Secureframe automate evidence collection. Reported platform cost roughly $10k-$30k/yr; audit $8k-$25k+; all-in first-year ~$20k-$60k; figures are mostly third-party/vendor-affiliated estimates. [V, low confidence] https://tracelayer.it.com/blog/soc2-compliance-cost-2026 ; https://underdefense.com/blog/compliance-automation-pricing/ ; https://costbench.com/compare/drata-vs-vanta/ . Path: start controls on day one (SSO, MFA, least privilege, logging, encrypted at rest, vendor review, change management) -> SOC 2 Type I at ~month 4-6 (useful as a sales unlock) -> Type II after a 3-6 month observation window (~month 9-12). Get a pen test. Do this when the first enterprise/mid-market procurement asks, not before first design partners; but build the controls now since retrofitting is costly.
- **Private cloud/on-prem:** Offer only when a signed customer pays for it (>~$100-150k ACV) [R]. Prepare for it cheaply by making the stack containerized, with no dependency on proprietary managed services you can't replicate, and a single-tenant deployment mode (DB-per-tenant + customer-managed keys + bring-your-own-model endpoint). Don't build an on-prem installer before demand exists.

---

## 14. Recommended early-stage architecture

```
                 +--------------------------- Control plane (Postgres, RLS) ---------------------------+
                 | tenants, users/SSO, connections, company model (entities/metrics/defs/versions),    |
                 | anomalies, investigations, hypotheses, evidence, decisions, outcomes, feedback,     |
                 | audit log, job state                                                                |
                 +-------------------------------------^------------------------------+----------------+
                                                       |                              |
 Customer systems                                      |                              v
 (ERP, accounting, e-com,   +----------+  raw    +-----+------+   metrics    +------------------+
  CRM, DBs, files)  ------> | Nango    |  ----> | Tenant PG  | -----------> | Detection jobs   |
        OAuth/keys          | (auth,   |        | schema:    |  (scheduled) | STL/MSTL/stats-  |
        (read-only)         |  tokens) |        | raw|clean| |              | forecast, CUSUM  |
                            +----+-----+        | model|mart |              +--------+---------+
                                 |  dlt workers +-----+------+                       | significant anomaly
                                 +------------------->|  ^                            v
                                                      |  | Semantic/metric compiler   +--------------------+
   Profiling + mapping + ER (Splink)  <---------------+  | (YAML spec, OSI-shaped)    | Investigation      |
   + reconciliation tests  --> human review UI           |                            | workflow (durable) |
                                                         |   read-only role / DuckDB  |  - LLM planner     |
                                                         +<-------------------------+  - analysis tools: |
                                                         |   sandbox, no network      |    decomposition,  |
                      pgvector (tenant schema): docs,    |                            |    bridges, event  |
                      past investigations, glossary <----+                            |    window, lagged  |
                                                                                      |    corr, CausalImp.|
                                                                                      |  - evidence grader |
                                                                                      +---------+----------+
                                                                                                v
        Web app / API / Slack-email alerts <--- narrative (numbers from evidence only) + confidence(obs, expl)
                       ^                                                                        |
                       +------ feedback, decisions, outcomes -----------------------------------+
        Cross-cutting: KMS envelope keys, secrets vault, audit log, LLM gateway (provider/region pin,
        ZDR, cost tracking, Langfuse tracing), eval harness (golden + synthetic faults) in CI
```

Team footprint [R]: 3-5 engineers can run this on one cloud account with managed Postgres, one container service (ECS/Fly/Cloud Run), object storage, a queue.

---

## 15. Evolution path

| Stage | Data/compute | Orchestration | Isolation | Notable changes |
|---|---|---|---|---|
| **~20 tenants** | 1 managed Postgres cluster, schema-per-tenant, DuckDB workers on demand | Postgres-backed queue or Inngest; dlt cron | Schema + RLS control plane; per-tenant KMS key for creds | Hand-hold onboarding; golden incidents grow; SOC 2 Type I |
| **~100 tenants** | Read replicas; split ingestion workers; move large tenants' facts to Parquet/DuckDB or ClickHouse; connection pooling (PgBouncer) | Temporal or Dagster for pipelines; autoscaling workers; per-tenant rate limiting for LLM spend | Shard tenants across Postgres clusters; DB-per-tenant tier for regulated; regional deploys | Template library of source mappings reduces onboarding to hours; SOC 2 Type II; evaluation CI gating |
| **~500 tenants** | Multiple Postgres shards (tenant->shard map), ClickHouse for big/event tenants, tiered storage | Temporal in production; dedicated data-platform team | Optional single-tenant/VPC deployments; per-tenant BYO key (CMK) | Cross-tenant (de-identified, consented) benchmarks and priors; maybe distilled small models for mapping/hypothesis ranking; consider Iceberg only if customers want data sharing |

Schema-per-tenant migration fan-out is the first scaling pain (hundreds of schemas x migrations); automate migration runner with parallelism and per-tenant version tracking from day one. [R]

---

## 16. Build vs buy

| Capability | Build | Buy/Use OSS | Recommendation |
|---|---|---|---|
| Auth/OAuth token handling | | Nango / cloud secrets | Buy/OSS |
| Connector extraction | Top 3-5 sources | dlt, Airbyte for long tail, Merge for accounting stopgap | Hybrid; own the connectors that drive your wedge |
| Warehouse | | Managed Postgres + DuckDB | Buy |
| Semantic layer spec | Own spec + compiler subset | MetricFlow (Apache 2.0) as fallback | **Build** (core IP), OSI-compatible import/export |
| Schema profiling + mapping templates | Yes | | **Build** (core to onboarding speed) |
| Entity resolution engine | | Splink | Use OSS, build review UI |
| Anomaly detection | Orchestration + materiality + context | statsforecast, statsmodels STL, ruptures | OSS libs, own the logic |
| Root-cause/driver analysis | Yes | | **Build** (core differentiator) |
| Causal estimators | | CausalImpact (python ports), DoWhy | OSS, used sparingly |
| Impact propagation | Yes (SQL/recursive CTE) | | Build |
| LLM access | | Anthropic/OpenAI/Bedrock/Vertex via thin gateway | Buy |
| Agent framework | Thin own loop | LangGraph (optional) | Build thin |
| Durable workflows | | Inngest / Temporal / Dagster | Buy/OSS |
| Vector search | | pgvector | OSS |
| Eval/tracing | Eval harness + datasets | Langfuse/Braintrust/Inspect | Hybrid |
| Compliance | Controls | Vanta/Drata + auditor | Buy |
| Secrets/KMS | | Cloud KMS + Secrets Manager | Buy |
| BI front end | Minimal UI for alerts/investigations | Embedded charting libs | Build thin; do not build a BI tool |

---

## 17. Hardest unsolved technical risks (honest list)

1. **Semantic correctness at scale of customization.** Metric definitions ("revenue", "active customer") are political and idiosyncratic; ERPs are heavily customized. Auto-modeling gets you a draft, not truth. Wrong-but-confident metrics destroy trust faster than missing metrics. Reconciliation catches only what has an external anchor.
2. **Causal attribution from observational SMB data.** Decomposition tells *where*, not *why*. Real causes (competitor action, weather, an unrecorded promo, a supplier problem) are often not in the data. Honest UX must say "unexplained," and the system must be rewarded for abstaining. Risk: LLM fluent narratives that overstate evidence.
3. **Alert quality vs. history.** Short histories, regime changes (COVID-like), promotions and one-off events yield false positives; users churn from noisy alerts. Materiality + feedback helps but needs real-world tuning data you won't have initially.
4. **Evaluation without ground truth.** Few labeled root causes; synthetic faults may not resemble real failures (Goodhart risk). LLM-judge unreliability for numeric claims.
5. **Prompt injection and data exfiltration** via ingested content, in a product that deliberately reads untrusted business data with tools. No complete defense exists; only containment (read-only, no egress, human in loop for actions).
6. **Entity resolution across systems** (customers/SKUs without shared keys, M&A, multi-entity, multi-currency) remains error-prone; errors silently corrupt attribution and impact propagation.
7. **Impact propagation fidelity.** Propagating effects across entities needs quantitative models (elasticities, lead times) that don't exist until you build them; naive propagation = double counting. This is also the prerequisite for credible what-if simulation (stage 6): simulating on unvalidated causal structure will yield authoritative-looking nonsense. Treat simulation as a separate, later product with explicit model validation.
8. **Unit economics of LLM investigations** (tokens x frequency x tenants) with frontier models; needs caching, triage (only investigate material anomalies) and budgets.
9. **Connector maintenance burden and API rate limits/changes** (long-tail ERPs, on-prem systems behind firewalls). Backfill of years of history can take days.
10. **Vendor/licence volatility:** Fivetran-dbt consolidation, ELv2/non-OSI licenses (Nango), non-commercial foundation-model weights, OSI spec still moving. Keep abstractions thin.
11. **Trust/liability for decision tracking:** attributing outcomes to decisions is itself a causal inference problem; early versions should log and display, not claim credit.

---

## 18. What is NOT needed (consolidated)

Graph DB / GraphRAG; ClickHouse or lakehouse at launch; Kafka/streaming; Spark; Kubernetes (until ~100 tenants); multi-agent frameworks; fine-tuned models; separate vector DB; feature store; full BI/dashboard builder; Cube server; deep-learning anomaly detectors; causal discovery algorithms; on-prem installer; in-house MDM; real-time (sub-hour) monitoring for most business metrics.

---

## Source list (all URLs referenced)
- Spider 2.0 repo/leaderboard: https://github.com/xlang-ai/Spider2 ; summary https://www.themoonlight.io/review/spider-20-evaluating-language-models-on-real-world-enterprise-text-to-sql-workflows ; aggregator https://benchmarklist.com/benchmarks/spider_2_0/
- Snowflake Cortex Analyst accuracy: https://www.snowflake.com/en/blog/engineering/cortex-analyst-text-to-sql-accuracy-bi/ ; https://www.snowflake.com/en/blog/engineering/agentic-semantic-model-text-to-sql/
- Databricks BIRD paper: https://arxiv.org/html/2509.21459v1
- OSI: https://www.snowflake.com/en/blog/osi-initiative-expands-partners/ ; https://www.getdbt.com/blog/the-osi-spec-updates ; https://www.getdbt.com/blog/dbt-labs-affirms-commitment-to-open-semantic-interchange-by-open-sourcing-metricflow ; https://thenewstack.io/dbt-labs-open-sources-metricflow-an-independent-schema-for-data-interoperability/ ; https://www.getdbt.com/dbt-summit/agenda/apache-ossie-realizing-semantic-layer-portability
- Fivetran/dbt merger and pricing: https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement ; https://dataopsleadership.substack.com/p/fivetran-vs-airbyte-in-2026-complete ; https://nexla.com/?p=26553
- Nango/Merge/Unified.to: https://www.getknit.dev/blog/nango-review-evaluation-integration-platform ; https://www.merge.dev/blog/nango-pricing ; https://truto.one/blog/top-5-open-source-and-low-cost-alternatives-to-mergedev-2026/ ; https://unified.to/blog/unified_apis_usage_based_vs_per_connection_pricing_for_integrations
- Time-series foundation models: https://arxiv.org/pdf/2510.15821 ; https://arxiv.org/html/2511.11698v3 ; https://www.beri.net/article/timesfm-vs-chronos-vs-moirai-time-series-foundation-model-licence-bigquery-sagemaker-cost-2026
- Anthropic ZDR: https://platform.claude.com/docs/en/build-with-claude/zero-data-retention ; https://privacy.claude.com/en/articles/8956058-i-have-a-zero-data-retention-agreement-with-anthropic-what-products-does-it-apply-to
- SOC 2 costs: https://tracelayer.it.com/blog/soc2-compliance-cost-2026 ; https://underdefense.com/blog/compliance-automation-pricing/ ; https://costbench.com/compare/drata-vs-vanta/

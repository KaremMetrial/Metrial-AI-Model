# Strategic Research: AI Company Intelligence Platform
**Date:** 2026-11-19 · **Phase:** research, strategy, validation only (no code, no repo, no UI design)
**Method:** 7 parallel research streams (competitors ×2, customer/market, architecture, UX, economics, devil's advocate). Full evidence lives in `research/appendix/` — this report synthesizes it.

---

## 0. Read this first: evidence quality and limits

Be careful how much weight you put on any single number here.

- **WebFetch was blocked for most vendor and news hosts.** Nearly every competitor claim comes from *search-result summaries*, not from reading primary documentation. Few capabilities reach "VERIFIED". Most are ADVERTISED. Nothing was hands-on tested.
- **No Reddit threads were retrieved** from the subreddits you named. Practitioner voices are from r/excel mirrors, Shopify Community, and Hacker News (anecdote, labelled).
- **Pricing is mostly third-party aggregators** with conflicting figures. Anthropic prices were not verified against Anthropic's own page.
- **Vertical scores are my judgment**, informed by sourced facts, not measured.
- **Customer demand is unproven.** I found strong evidence that the *supply* of SMB-grade "investigate why" products is thin. I found no evidence that SMBs will pay for it. That gap is the whole game.
- Labels used: **VERIFIED / ADVERTISED / INFERRED / UNKNOWN** for capabilities; **SOURCED / ASSUMPTION** for numbers; **[J]** = judgment.

A follow-up pass with unrestricted network access (primary docs, G2/Gartner Peer Insights full reads, demos/trials, Reddit by hand) is listed in §16.

---

## Deliverable 1 — Executive Verdict

### Verdict: **PIVOT to a narrow wedge. Conditional GO on the wedge. NO-GO on the platform as originally described.**

| Question | Honest answer |
|---|---|
| Worth pursuing? | **The general "living digital model of your company" — no.** A narrow, vertical, evidence-first "why did my margin move" product, sold through trusted advisors — **yes, conditionally**, and only after a ~4-week concierge test that costs almost nothing. |
| Is the market attractive? | Pain is real and widely documented, but mostly by vendors. The BI market is large ($32–39B, enterprise-skewed — useless as a TAM). SMB-specific willingness to pay for *causal explanations* is **unproven**. |
| Is the current concept differentiated? | **No.** Continuous monitoring, anomaly detection, NL Q&A, agents, semantic layers/ontologies and "proactive" insights are all shipped by incumbents (Qlik, Tableau, ThoughtSpot, Databricks, Microsoft) and by systems of record (Intuit, Xero, Shopify). A funded startup (WisdomAI, $50M Series A) ships proactive RCA with anomaly memory. |
| Biggest risk | **The gap versus free-and-already-there:** Intuit/Xero/Shopify agents inside the tools SMBs already pay for, plus Claude for Small Business (launched 2026-05-13, QuickBooks/PayPal/HubSpot connectors, scheduled tasks, approval gates) at $20–200/month. A thin "chat over connectors" layer has a price ceiling near zero. Second risk: **onboarding is really data cleaning**, which makes this a services business at first. |
| Strongest opportunity | **Cross-system causality that no single system of record sees**, delivered with an honest evidence trail (observation confidence ≠ explanation confidence, counter-evidence, "what we couldn't check"), in a niche where the dollars are measurable (margin and price-cost leakage). No vendor I found documents calibrated confidence or correlation-vs-causation framing. That is either the opening or a sign nobody pays for it. |
| Would I invest my time with limited capital? | **Yes — but only the 4-week concierge test first, not the product.** I would not spend months building a platform before ≥10 owners have paid or committed for the memo. |

**Why PIVOT rather than GO:** the four attacks on the full vision are independent and mutually reinforcing: (1) systems of record are shipping first-order "what's wrong" for free; (2) foundation-model vendors sell the horizontal version; (3) data platforms own the "ontology of the business" story; (4) every precedent that tried automated "why did the metric move" (Sisu → Snowflake 2023, standalone discontinued; Peak → UiPath 2025; Chartio/Periscope absorbed) ended as a feature inside a bigger platform, not as an independent category winner. None of this means the problem is fake. It means the *shape* has to change.

---

## Deliverable 2 — Market and Competitive Map

| Category | Representative players | What it already solves | Overlap with your idea | Who it fails |
|---|---|---|---|---|
| **Systems of record with built-in AI** | Intuit (QuickBooks "Intuit Intelligence": anomaly detection, reconciliations, next-step chat), Xero (JAX agent), Shopify (Sidekick Pulse), NetSuite/SAP/Oracle (not verified) | First-order "what's wrong" *inside their own data boundary*, free/bundled, with distribution and trust | **Highest overlap for SMB** | Cross-system causality (they see only their half) |
| **Foundation-model assistants** | Claude for Small Business (+ Cowork scheduled tasks), ChatGPT/Gemini with connectors | Scheduled briefings, reconciliation, forecasts, "why did revenue dip" on covered connectors | Substitutes anything chat-shaped | Persistent state, audit trail, entity resolution, uncovered sources |
| **BI incumbents with proactive AI** | Qlik Discovery Agent (GA Feb 2026), Tableau Pulse/Next, ThoughtSpot Monitor, Databricks Genie, Power BI anomaly + Activator, Looker Conversational Analytics | Metric monitoring, anomaly alerts, driver/contributor analysis | Monitoring is **commoditized** here | Anyone without a modeled semantic layer + admin — i.e. SMB |
| **Enterprise AI / search** | Glean (~$300M ARR, vendor-claimed), Microsoft Copilot ($21/user Business), Dust, Sana (→Workday ~$1.1B), Onyx, Hyperspell, PromptQL | Knowledge retrieval, agent builders, connectors/MCP | Low — they model *documents*, not *metrics/causes* | Quantitative investigation |
| **Decision intelligence** | Palantir, Aera (Decision Ledger/Policy Studio, Oct 2026, ADVERTISED), Tellius (autonomous RCA), Quantexa, FICO, SAS, IBM, Pega, o9, Peak (→UiPath), Cloverpop | Enterprise decisioning; Aera = closest on decision log + approvals; Tellius = closest on RCA | **Closest functionally** | All enterprise, sales-led, $100K+, data-team prerequisites |
| **Data/AI observability & process intelligence** | Monte Carlo, Metaplane (→Datadog), Celonis, Signavio | Data-health monitoring; process mining | Adjacent (data health ≠ business causality) | SMB; commercial metrics |
| **AI-native BI/analyst startups** | **WisdomAI** ($50M A, Nov 2025: proactive agents, RCA, anomaly memory), **Gravity/Orion** (~$10M, autonomous investigation, ADVERTISED), Zenlytic (ecommerce semantic AI), Julius, Hex, Omni ($1.5B), Sigma (~$3B), Fabi, Basedash | AI Q&A, semantic-layer BI; a few proactive | **WisdomAI and Gravity are the closest startups** | SMB zero-setup; decision/outcome loop; calibrated confidence |
| **SMB "AI CFO" / vertical monitors** | CentSight, Finley, Nume, Fathom, Shopify apps ($79–$199/mo with "AI RCA"), TrueProfit/Triple Whale/Polar, Cogsy/Prediko | Cheap narrow monitors and reporting | Compete on price at the low end | Cross-functional "why", decisions |

**Consolidation is the pattern:** Sisu→Snowflake (2023), Metaplane→Datadog (2025), Causal→LucaNet (2024), Peak→UiPath (2025; ~$38M reported by one source, unverified), Sana→Workday (closed 2025-11-04), Pyramid→ServiceNow (closed 2026-03-10), Snowflake–Observe (agreed Jan 2026). Exits happen; independent category-defining outcomes in this space have been rare.

Detail and source URLs: `appendix/agent1a_competitors.md`, `appendix/agent1b_competitors.md`.

---

## Deliverable 3 — Competitor Capability Matrix

Cell key: **V** verified (primary/reputable source seen) · **A** advertised only · **P** partial/narrow · **U** unknown / not found in public sources · **—** not offered/not found. "U" does **not** prove absence. Because most primaries could not be fetched, V is used sparingly.

| Competitor | Monitoring | Anomaly det. | Root-cause | Proactive investigation | Evidence trail | Calibrated confidence / causal framing | Impact propagation | Decision/outcome loop | Simulation | SMB zero-setup onboarding | Pricing (public?) | Impl. complexity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Intuit Intelligence (QBO) | A/P | V (Jan 2026 update) | P | A | U | — | — | P (user confirms actions) | P (finance agent scenarios) | **V (in-product)** | Bundled | Low |
| Xero JAX | A | A | U | A ("proactively highlights") | U | — | — | — | — | **V (in-product)** | Bundled | Low |
| Shopify Sidekick Pulse | A | U | U | A | U | — | — | — | — | **V (in-product)** | Bundled | Low |
| Claude for Small Business | P (scheduled tasks) | P | P (prompted) | — (re-derives, no state) | P | — | — | — (approval gates only) | — | P | $20–200/mo + tools | Low |
| Qlik Discovery Agent | **V** (GA Feb 2026) | **V** | U | V (unprompted alerts) | U | — | — | — | — | — (needs Qlik model) | No | Med-High |
| Tableau Pulse / Next | **V** | V | P (descriptive; "Explain Data" for why) | A | P | — | — | — | — | — | Opaque | Med-High |
| ThoughtSpot Monitor | P | P | P ("drivers") | A | P | — | — | — | — | — | No | High |
| Databricks Genie | A | A | A | A | P | — | — | — | — | — (needs lakehouse) | No | High |
| Power BI/Fabric | P (Activator thresholds) | V (line charts) | P (explain-increase, statistical) | — | P | — | — | — | — | — | $14–$24/user + Fabric | Med-High |
| Looker | U | U | U | U | P | — | — | — | — | — | No | High |
| Tellius | A | P | **P (independent: narratives need analyst validation)** | A | P | **U (none documented)** | — | — | U | — | No ("expensive", G2) | Med-High |
| Aera | A | A | P | A | A | — | — | **A (Decision Ledger, Oct 2026)** | U | — | No | High |
| Palantir | V | P (build) | P (build) | P | V (action logging) | — | P | P (build) | V (scenarios) | — | est. $0.1–2.5M/yr | Very high |
| WisdomAI | A | A | A | A | A | U | U | — | — | — | No | U |
| Gravity/Orion | A | A | A | A | A | U | A | A ("recommendations") | — | U | U | U |
| Zenlytic | U | U | U | U | U | U | — | — | — | P (ecommerce) | No | U |
| Glean / Dust / Onyx | P (Glean "proactive") | U | U | U | — | — | — | — | — | P (Dust/Onyx) | $20–75/user | Low-Med |
| Cloverpop | — | — | — | — | — | — | — | A (manual decision logging) | — | P | No | Low |
| Shopify vertical monitors | V/A | A | A (shallow "AI RCA") | — | U | — | — | — | — | **V (app install)** | $79–$199/mo | Very low |

**Key reading:** no row has a verified cell in *calibrated confidence*, *impact propagation*, or *decision→outcome loop for SMB*. Three possible explanations — an opening, an unproven need, or hard-to-do — and the evidence cannot distinguish them. The concierge test will.

---

## Deliverable 4 — Unsolved Customer Problems (ranked)

Ranking logic [J]: dollars at stake, recurrence, data accessible without a data team, a "why" existing tools cannot answer, one-quarter route to a pilot. Dollar figures are vendor-sourced hypotheses unless noted.

| # | Problem | Customer | Current workaround | Impact (evidence quality) | Why current tools fail |
|---|---|---|---|---|---|
| 1 | **Margin erosion explained** by price / cost / mix / freight / discount / returns, across systems | Owner/CFO/controller at 10–200-person distributor, specialty CPG or Shopify brand | Month-end Excel bridge from ERP/Shopify/accounting exports | Distributors: COGS +10% expected by 62% (NAW, trade association — better source); ~half confident of margin-impact visibility (vendor survey). 0.5 pt of margin on $20M revenue = $100K/yr (arithmetic) | BI shows margin; doesn't decompose it with evidence; each system sees half the chain |
| 2 | **Supplier-cost pass-through / price leakage** ("cost rose, sell price didn't") | Distributor pricing/sales-ops lead | Manual price lists, rep overrides | Supplier reconciliation cycles of 3–6 months (consultancy survey, abstract only) | ERP pricing modules rarely used; BI doesn't alert on this event. **Sharper than #1 because it's a detectable event** |
| 3 | **Stockout/overstock root cause** | Shopify-brand or distributor ops head | Excel reorder sheets | IHL $1.73T global (vendor-sponsored); distributors overbuy (vendor) | Planners forecast but don't explain *why* it happened; competition real (not surveyed) |
| 4 | **Shopify true profit + ad efficiency anomalies** | DTC founders, $1–20M GMV | Month-end spreadsheet (Shopify Community, anecdote) | Unknown per brand | 5+ funded apps at $49–$750/mo — pain real, price ceiling low |
| 5 | **Carrier/3PL invoice & service-failure recovery** | Shippers / 3PLs | Ignore, or pay auditors 25–50% contingency | 1–5% of freight spend recoverable (vendor) | Services, not software; mature incumbents |
| 6 | **Cash-flow risk from late receivables** | Services/B2B firms on Xero/QBO | AR aging review, spreadsheet 13-week forecast | Xero platform data: ~29 days to get paid, ~9 days late (stronger source) | Crowded; Intuit/Xero moving in fast — weak wedge |
| 7 | **SaaS churn / failed-payment leakage** | B2B SaaS founders | Stripe + Baremetrics/ChartMogul | ~9% of MRR touched by failed payments (vendor) | Well served; lowest defensibility |
| 8 | **Month-end variance explanation** | Controllers/fractional CFOs | Manual commentary; 4+ days to close (vendor) | Time saved, not money found | Works as a *feature inside #1*, not a standalone wedge |
| **Cross-cutting** | **Verification cost of AI outputs** | Finance leaders already using AI | Re-check everything | 96% of AI-using finance execs spend ≥10% of time verifying AI (Datarails, vendor n=270); only ~14% fully trust AI for accounting data (Journal of Accountancy summary) | Nobody ships a standard evidence format for AI-generated analysis |

---

## Deliverable 5 — Differentiation Blueprint

**Do not force a USP.** The research supports a *narrow, testable* one and rejects most of the original list.

| | |
|---|---|
| **Proposed category** | **Margin investigation** (working phrase) — or "exception review with evidence". Avoid "decision intelligence" (Aera/Cloverpop/Gartner own it, enterprise-priced) and "digital twin" (noise: 1STLabs, Viven, Twin1 all use it for unrelated things). |
| **Primary customer** | Owner/CFO/controller of a **specialty product brand or distributor (≈$3–75M revenue)** running Shopify and/or an ERP plus QuickBooks/Xero, reached via **accountants, fractional CFOs and ERP resellers** [J]. |
| **Core problem** | "My margin moved and nobody can tell me why, with evidence, across the systems." Starting event: supplier cost rose but price did not; discount/mix/freight shifted. |
| **Core promise** | Each week, the 1–3 margin movements that matter, each with a case file: dollar range, what we're sure of, what we think explains it, counter-evidence, what we couldn't check, one recommended action, and a follow-up date. Quiet when nothing matters. |
| **Unique workflow** | Case file → decision → scheduled outcome check ("followed by", not "caused by"). The pairing of *separate* observation vs explanation confidence with *equal-weight counter-evidence* is the part no competitor documents. |
| **Most defensible capabilities** | (1) Vertical metric tree + hypothesis library for margin (price/cost/mix/freight/discount/returns) with deterministic decomposition; (2) evidence-grading and abstention ("unexplained" is a first-class answer); (3) labeled investigation+outcome history per tenant and, later, de-identified cross-tenant priors; (4) advisor-channel relationships and reliable connectors for one stack. |
| **Easy to copy** | Chat UI, anomaly alerts, LLM narratives, "AI recommends", connectors, MCP, agents, semantic layers. Intuit/Xero/Shopify/Anthropic can ship any of these in a quarter. |
| **Hard to copy** | Calibrated, abstaining RCA tuned on a vertical's *labeled* incidents; cross-system entity resolution for a specific stack; trusted-advisor distribution; years of outcome-labeled decisions. (Hard ≠ impossible: a platform vendor could build it if the market proves out.) |
| **Why customers would choose you** | Because after the owner's QuickBooks/Shopify agent says "margin is down", yours says *why*, across both systems, shows what it could *not* verify, and follows up. **Only true if a blind comparison confirms it** (§Validation). |

**What does NOT differentiate** (rejected): AI agents, knowledge graph, memory, proactive alerts, root-cause *claims*, predictions, simulations, recommendations, decision tracking in the abstract, NL queries. Decision-journal tracking in particular has weak evidence of sustained use (Cloverpop: ~$17.5M raised over a decade, no public adoption data) — treat as an unproven retention hypothesis, not a moat.

---

## Deliverable 6 — Three Alternative Product Strategies

| | **Strategy A: Margin Investigator** (vertical, owner-facing) | **Strategy B: Advisor Investigation Copilot** (accountant is the customer) | **Strategy C: Evidence Layer for AI analysis** (horizontal trust layer) |
|---|---|---|---|
| **Target customer** | Specialty product brands / distributors, $3–75M, Shopify + QBO/Xero (+ one ERP later) | Accounting firms, fractional CFOs, ERP resellers serving 5–50 SMB clients | Finance/ops teams already using Claude/Copilot/Intuit AI |
| **Problem** | Margin/price-cost leakage with no cross-system explanation | Advisors want forward-looking, scalable client insight; can't hand-investigate 30 clients | Verifying AI outputs consumes ≥10% of finance time |
| **Product** | Weekly margin case-file brief + case page + decision log + follow-up | Multi-client queue of cases across their portfolio, white-label-ish briefs | Citation/evidence-grading and audit trail wrapped around other tools' outputs |
| **Differentiation** | Vertical hypothesis library, abstaining RCA, cross-system | Trust holder + human-in-the-loop solves onboarding/churn; one relationship → many clients | Complements rather than competes with Claude/Intuit/Xero |
| **Competition** | Shopify profit apps ($49–750/mo); in-product agents; Zenlytic (DTC); Tellius upmarket | Fathom (accountant-led reporting), Intuit/Xero courting accountants | Every vendor will build native citations |
| **Pricing** | $349–$999/mo + $1.5–3.5k setup; later savings-share (§Fin) | Per-client-seat to advisor, e.g. $75–$250/client/mo, advisor resells at margin [A] | Likely low per-seat; value unclear |
| **Technical complexity** | Medium (2–3 connectors, margin tree) | Medium-High (multi-tenant portfolio UX + same engine) | Medium; integration surface unclear |
| **Capital needed** | ~$250–450k runway to 20 customers at full salaries; far less if founders draw $4–5k [A] | Similar; slower start, better scaling | Low to start, uncertain demand |
| **Time to first customer** | 4–8 weeks (concierge) | 6–12 weeks (needs advisor trust first) | 8–12 weeks |
| **Main risks** | Free in-product agents; data messiness; Shopify/Intuit absorb it | Advisors may not resell; Intuit/Xero courting same channel | Incumbents/vendors ship citations; no budget line |
| **Expansion** | More margin drivers → cash → inventory → whole-company model | Portfolio benchmarks across clients (consent-based) | Becomes a standard; unclear monetization |

**Ranking:** **1. A, validated through B as its distribution channel**; 2. B as a stand-alone product if advisors respond more strongly than owners; 3. C only as a feature of A (the evidence format), not a company.
**My choice:** A, with the pilot deliberately sourced through 3–5 accountants/fractional CFOs so the test also measures B.

---

## Deliverable 7 — Product Blueprint

**Name directions** (limited conflict checks, **not** trademark clearance): Casefile (generic, hard to own), Margin Note, Ledgerlight, Quorum, Overlook, Nightwatch. *Avoid:* Watchtower (verified crowded), Lookout, Hindsight, The Rundown. Prefer a coined/compound name; run USPTO/EUIPO + domain checks; test two finalists with five owners ("what do you think this does?"). Category phrases to test: "margin investigation", "continuous business review", "exception intelligence", "AI chief of staff for operations".

**Positioning (testable):** *"Your margin moved. Here is why, how sure we are, what we couldn't check — and whether last month's fix worked."*

**Pillars:** (1) **Quiet by default** — surface ≤3 things; "nothing needs you" is a valid output. (2) **Evidence, not assertion** — observation vs explanation confidence, equal-weight counter-evidence, abstention. (3) **Closed loop** — every case ends in a decision and a scheduled follow-up. (4) **No data team** — plain-language company-model confirmation, never database terms.

**Information architecture** (from `appendix/agent5_ux.md`, Part C): `Brief | Cases | Decisions | Business Model | Ask` + Settings. Default landing = Brief. No dashboard, no chart gallery.
- **Brief** — the *front door for executives*: weekly (twice-weekly optional) email/Slack/Teams message, ≤3 items, summary in email, detail behind login (avoids leaking financial data in email).
- **Cases** — the Investigation Queue, demoted from front door to *ops back office* (filters: Mine / Needs decision / Waiting on data / Snoozed / Resolved).
- **Decisions** — auto-built from cases; "Of 14 actions in Q4, 9 improved the metric" is the proof-of-value artifact.
- **Business Model** — what the product believes about the company; reviewable/editable; every confirmed definition is a dated, user-confirmed fact.

**Verdict on your Investigation Queue concept:** right object model, wrong front door for executives. Closest analogs (Aera inbox, AI-SRE tools like Datadog Bits/Resolve/Cleric) show the pattern works: ranked hypotheses, evidence, confidence, a human feedback step, a persistent record. But BI tools reach only ~25–29% of employees, clinical alert override rates run ~53–90%, and no AI-SRE accuracy claim has been independently benchmarked.

**Case-file anatomy** (top→bottom): headline · bottom line box (dollar range, urgency, recommended action) · *what we're sure of* (observation) · *what we think explains it* (≤3 ranked hypotheses: best-supported / possible / ruled out) · evidence with source+date · counter-evidence directly under each hypothesis · what we couldn't check / what would change our mind · affected entities · recommended actions incl. explicit "do nothing" with its cost · decision panel (Act / Investigate / Dismiss-with-reason / Snooze) · follow-up date · scoped Ask box.

**Confidence display:** do not show a bare percentage. Studies show confidence numbers and hedging raise acceptance without improving discrimination between right and wrong answers; explanations can increase overreliance. Use three labelled levels *with reasons* ("Observation: confirmed — matches your invoices. Explanation: moderate — one of three checks supports it"), and test with **seeded wrong explanations** to see whether owners catch them. Cognitive-forcing prompts only above a dollar threshold (they reduce overreliance but users dislike them).

**Notification policy:** ≤1 push/day; three tiers (Interrupt — rare, <1/month, observation must be "confirmed"; Brief — default; Archive); never push on explanation confidence alone ("something changed, cause unknown, here's the question we need answered"); dedupe into one case per issue; after 3 ignored/dismissed items of one type, ask once to stop flagging; track open/action/dismissal/"not useful" rates from day one; if action rate falls below a floor, **cut volume, don't add features**.

**First-time experience:** connect *one* source → "What I understand about your business" card (Right / Not quite / Not sure) → ≤5 ranked confirmation questions in business language ("Is Acme Co the same customer as ACME Corporation?") → a "first look, low history" baseline brief in the same session → "Expect about one message a week."

**Roles:** Owner/CEO/CFO (Brief; decide/assign/snooze); Ops/finance manager (Cases; investigate/close/tune); Advisor (portfolio view — Strategy B); Admin (connections, model sign-off).

---

## Deliverable 8 — Build vs Buy vs Do Not Build

| Capability | Verdict | Reasoning |
|---|---|---|
| Margin metric tree + deterministic decomposition (price/cost/mix/freight/discount/returns) | **Build (core IP)** | This is the product. Decomposition says *where*; the LLM never computes numbers |
| Investigation engine (hypothesis list → deterministic tools → evidence grading) | **Build** | Core differentiator; single agent loop with fixed tool menu |
| Evidence & confidence engine (observation vs explanation; abstention) | **Build** | Only plausible gap in the matrix; must be *rewarded for abstaining* |
| Business-specific materiality / prioritization | **Build** | Precision is the product; ranking = $ impact × urgency × confidence |
| Decision + outcome log, follow-up scheduler | **Build (thin)** | Log and display; do **not** claim causal credit |
| Company-model confirmation UX ("Is this right?") | **Build** | Onboarding quality = retention |
| Source-to-canonical mapping templates (Shopify, QBO/Xero) | **Build** | Drives onboarding speed; reusable across tenants |
| Semantic/metric layer | **Build thin YAML spec**, OSI/MetricFlow-compatible; MetricFlow (Apache 2.0) as fallback | Skip Cube server; it's a full BI runtime |
| Connectors | **Hybrid**: dlt (Apache 2.0) for your 2–3 wedge sources; Nango for OAuth/token plumbing; Airbyte OSS for long tail only | Fivetran per-connection pricing hurts SMB margin; Merge normalizes away ERP detail |
| Entity resolution | **Reuse OSS (Splink)**, build the review UI | |
| Anomaly detection | **Reuse OSS** (statsmodels STL/MSTL, statsforecast, ruptures); own the materiality logic | Boring statistics beat fancy models here; foundation TS models optional |
| Causal estimators | **Reuse OSS sparingly** (CausalImpact ports, DoWhy); Granger only as a ranking feature | Observational SMB data rarely supports causal claims |
| LLMs | **Buy** via thin gateway (Anthropic/Bedrock/Vertex/OpenAI), provider/region pin, ZDR | Verified only for Anthropic ZDR terms |
| Durable workflows | **Buy/OSS**: Postgres queue or Inngest first; Temporal/Dagster at ~100 tenants | |
| Vector search | **OSS: pgvector** in tenant schema | For past-investigation/glossary retrieval only |
| Eval/tracing | **Hybrid**: own golden-incident + synthetic-fault harness; Langfuse/Braintrust/Inspect (licences unverified) | |
| Auth/SSO, secrets/KMS, compliance automation | **Buy** (cloud KMS/Secrets Manager, Vanta/Drata + auditor) | SOC 2 ≈ $20–60k first year (low confidence) |
| Impact propagation | **Postpone** beyond the margin tree; recursive CTEs when needed | Naive propagation double-counts; needs elasticities/lead times |
| What-if simulation | **Postpone** (separate later product) | Simulating on unvalidated causal structure yields "authoritative-looking nonsense" |
| Knowledge graph / graph DB | **Never build** (until a measured problem demands it) | Typed relational tables + recursive CTEs cover it |
| Custom/fine-tuned foundation model | **Never build** | Retrieval + tools capture the value; consider distillation much later on consented cross-tenant tasks |
| Generic chatbot / agent builder / dashboard builder | **Never build** | Commoditized; "Ask" is scoped to a case, not a product |
| Multi-agent swarm | **Never build** (v1) | Single loop on durable queue is sufficient |
| ClickHouse/lakehouse/Kafka/Spark/Kubernetes | **Postpone** | One Postgres + DuckDB; K8s ≈ 100 tenants |
| Autonomous financial transactions / write-back | **Never build** (v1) | Approval-gated suggestions only |
| Huge integration catalog; warehouse replacement; on-prem | **Never build / postpone** | On-prem only when a signed customer pays (>~$100–150k ACV) |

---

## Deliverable 9 — Technical Architecture

*(Source: `appendix/agent4_architecture.md`. Tags: [V] verified, [K] prior knowledge not re-verified, [R] recommendation.)*

**Principles.** (1) The LLM plans, hypothesizes, and narrates; **every number traces to an executed deterministic query**. (2) One boring data store. (3) "Learning the company" = a versioned, human-reviewed context, **not** fine-tuning. (4) Treat all tenant data as untrusted input. (5) Abstain rather than guess.

```
 Customer systems         Control plane (Postgres, RLS): tenants, users/SSO, connections,
 (Shopify, QBO/Xero,      company model (entities/metrics/defs/versions), anomalies,
  ERP, files)             investigations, hypotheses, evidence, decisions, outcomes,
      │ read-only OAuth   feedback, audit log, job state
      ▼                                  ▲
  Nango (auth) ─► dlt workers ─► Tenant Postgres schema [raw|clean|model|mart]
                                   │                 │
        profiling + mapping + ER   │      metric compiler (YAML spec, OSI-shaped)
        (Splink) + reconciliation ─┘                 │ scheduled
        ─► human review UI                           ▼
                                      Detection jobs (STL/MSTL residuals, statsforecast,
                                      CUSUM; materiality gate)
                                                     │ significant change
                                                     ▼
                       Investigation workflow (durable) — LLM planner picks from fixed tools:
                       dimension decomposition · bridge/waterfall · event-window compare ·
                       lagged correlation · CausalImpact (sparingly) → evidence grader
                       (read-only role / DuckDB sandbox, no network)
                                                     │
                       narrative (numbers from evidence only) + confidence(obs, expl)
                                                     ▼
                  Brief (email/Slack) · Case page · Decision log ──► feedback/outcomes ─┐
                       ▲──────────────────────────────────────────────────────────────┘
 Cross-cutting: KMS envelope keys · secrets vault · immutable audit log (doubles as evidence trail) ·
 LLM gateway (provider/region pin, ZDR, cost tracking, tracing) · eval harness in CI
```

**Company context model.** Entities, metric definitions (owner + rationale), fiscal calendar, known events/promotions, seasonality notes, per-metric thresholds — all versioned and audit-logged. Relationship table `entity_link(type, valid_from, valid_to, confidence, source)` with a status per link: **user-confirmed / data-supported / historical-pattern / inferred / hypothetical** — directly implementing your "not every relationship is causal" requirement. Known/unknown/outdated/inconsistent flags come from profiling + reconciliation checks.

**What "the AI learns" means** (ordered by value): metric definitions and glossary → investigation/decision memory retrieved at inference → feedback-calibrated thresholds and hypothesis priors (Bayesian updating, not training) → user instructions. **RAG** only for documents/past cases. **Fine-tuning: no** in v1/v2 (tiny per-tenant data, drift on model upgrades, governance cost).

**Investigation architecture.** Detect → *validate the data* (freshness, completeness, reconciliation) → decompose (which dimension/segment moved) → test candidate hypotheses with deterministic tools → grade evidence for/against → compute impact range → state what couldn't be checked → recommend → LLM writes narrative from graded evidence only. Observation confidence and explanation confidence are stored separately. Evidence grades map to your categories: Verified / Strongly supported / Probable / Hypothesis / Unknown.

**Why deterministic matters (evidence):** Spider 2.0 (real enterprise text-to-SQL): o1-preview ~5.7%–21.3% depending on split/agent vs 73% BIRD and 91% Spider 1.0 [V, original paper; aggregator leaderboards low-confidence]; Snowflake reports 57%→78% on BIRD with a semantic model [V, vendor]; Vals Finance Agent: top models ~65%, ~34% on financial modeling [V]. Direction improving; still short of "trust without verification."

**Tenant isolation.** Schema-per-tenant for tenant data (default to ~hundreds of tenants) + RLS on control-plane tables + per-tenant DB roles; per-tenant object-storage prefix and KMS key for Parquet; pgvector tables live *inside* the tenant schema so isolation is inherited; credentials in Nango/Secrets Manager, never in app tables; **read-only scopes** at the source; automated cross-tenant leak tests in CI; DB-per-tenant tier for regulated/enterprise.

**LLM security.** Prompt injection from data content is the main novel risk (product names, invoice memos, ticket text). Controls: read-only parameterized tools only; SQL parsed and allow-listed to SELECT on approved views; statement timeout/row/memory caps; **no outbound network** in the analysis sandbox; no auto-loading remote images/links in rendered output; schema-validated structured outputs; separate "reader of untrusted text" from "planner with tools" where possible; human approval for any action. No complete defense exists — only containment.

**Other security.** Immutable customer-visible audit log; region pinning at tenant creation; Anthropic zero-data-retention terms verified [V] (Bedrock/Vertex/Azure/OpenAI terms **not verified** — check contracts); SOC 2: controls from day one, Type I ~month 4–6 when procurement asks, Type II after 3–6-month window; pen test; private cloud only for a paying customer.

**Evaluation system.** Golden incidents (owner-confirmed historical movements with known causes), synthetic fault injection (Goodhart risk acknowledged), abstention rate, calibration plots (stated 80% should be right ~80%), LLM-judge only for prose, never for numeric claims. **Release gate:** top explanation correct ≥~70% on ≥30 confirmed incidents and calibrated, before you scale.

**Infrastructure (early stage):** one cloud account; managed Postgres; one container service (Cloud Run/Fly/ECS); object storage; a queue. **3–5 engineers** can run it. **Evolution:** ~20 tenants (above, hand-held onboarding, SOC 2 Type I) → ~100 (read replicas, template library cuts onboarding to hours, Temporal/Dagster, shard Postgres, regional deploys) → ~500 (shard map, ClickHouse for big tenants, optional single-tenant/BYO-key deployments, consented cross-tenant priors). First scaling pain: schema-migration fan-out — automate per-tenant migration tracking from day one.

**"3-day onboarding" — honest verdict.** Credible only as *3 days to connected data + first draft model + first metrics on 1–3 standard systems*. A **validated** model takes **2–4 weeks**; custom ERPs/spreadsheets-as-system-of-record take **4–8 weeks**. Define "onboarded" by a measurable gate (reconciliation within x% of the customer's own P&L; metric definitions signed off by a named owner). Offer a human solutions-engineer layer early: cheaper than perfect automation and it generates the labeled data to automate later.

**Hardest unsolved risks:** semantic correctness under customization; causal attribution from observational SMB data (real causes often aren't in the data); alert quality with short history; evaluation without ground truth; prompt injection/exfiltration; cross-system entity resolution; impact-propagation fidelity (prerequisite for any credible what-if); connector maintenance; vendor/licence volatility; outcome attribution being itself a causal inference problem.

---

## Deliverable 10 — MVP Specification

**Guiding rule:** *do not build until the concierge test (Deliverable 11, Phase 1) passes.* The MVP below is what you build **after** it passes, scoped to the wedge, not the "30-feature" platform.

### Scope: "The Margin Loop"
Connect → understand → monitor margin → investigate → decide → follow up. One metric family, two or three connectors.

**In scope (what must be included)**
1. **Connectors:** Shopify, QuickBooks Online *or* Xero (pick the one the pilot cohort uses), plus structured CSV/Google-Sheet import for COGS/supplier price lists (SMB reality). NetSuite/Odoo/ERP **postponed**.
2. **Company Blueprint (thin):** auto-profiled canonical model (orders, products/SKUs, customers, costs, suppliers, AR/AP) + ≤5 plain-language confirmation questions + reconciliation to the customer's own P&L.
3. **Margin monitoring:** gross margin and contribution margin by product/channel/customer; seasonal baselines (STL/MSTL residuals) with a materiality gate.
4. **Margin investigation engine:** decomposition into price / cost / mix / freight / discount / returns; supplier-cost vs sell-price check; hypotheses ≤3; evidence for and against; impact range; "what we couldn't check".
5. **Brief + Case page:** weekly email brief (≤3 items) and the case-file page.
6. **Decision log + follow-up:** Act / Investigate / Dismiss-with-reason / Snooze; owner; scheduled outcome check reported as improved / no change / worse / cannot tell.
7. **Audit/evidence log** (customer-visible) and basic tenant isolation.

**Postponed:** impact propagation graph beyond the margin tree; what-if simulation; cash-flow, inventory and churn monitors; Slack/Teams bots (email first); advisor portfolio view (Strategy B); NetSuite/Odoo; SSO/SOC 2 Type II.
**Removed:** generic chat, dashboards/BI builder, agent builder, knowledge graph, write-back/autonomous actions.

### User stories (abbreviated)
- *As an owner*, I get a weekly brief that says "Nothing needs you" or up to three items with dollar effect, so I don't read dashboards.
- *As an owner*, I open a case and see what is confirmed, what is hypothesized, and what contradicts it, so I can decide whether to trust it.
- *As an owner*, I Dismiss with a reason so the system stops flagging known issues.
- *As a controller*, I confirm or correct the company model in business terms so findings reflect our definitions.
- *As an owner*, I'm reminded on the follow-up date and told whether the metric improved, so I know if the decision worked.
- *As an advisor (later)*, I see cases across my clients.

### Core entities
Tenant · User · Connection · Source record · Canonical entity (Customer, Product/SKU, Supplier, Order, Invoice, Cost) · Entity link (typed, status, confidence, source) · Metric definition (versioned) · Baseline · Anomaly · Investigation/Case · Hypothesis · Evidence item (supports/contradicts, source, date) · Limitation (missing data) · Recommendation · Decision · Outcome check · Feedback · Audit event.

### Functional requirements (selected)
- FR1 Every number in a narrative must trace to an executed query stored with the case.
- FR2 Observation confidence and explanation confidence are stored and shown separately, with reasons.
- FR3 The system can return **"cause not determined"**; abstention rate is tracked.
- FR4 Relationship status ∈ {user-confirmed, data-supported, historical-pattern, inferred, hypothetical}.
- FR5 Data-validation step runs before any investigation (freshness, completeness, reconciliation).
- FR6 ≤3 items per brief; hard cap on pushes; dedupe to one case per issue.
- FR7 Outcomes are labelled "followed by", never "caused by", unless a causal basis is recorded.

### Non-functional requirements
Read-only source access; tenant isolation tested in CI; encryption in transit/at rest; per-tenant credentials in a vault; immutable audit log; LLM calls via gateway with ZDR where available and cost budget per tenant; investigation p95 under ~10 minutes (batch is fine); no outbound network in the analysis sandbox; per-tenant export and deletion.

### Acceptance criteria (gates)
- Reconciliation within an agreed tolerance of the customer's P&L, with metric definitions signed off by a named owner.
- On ≥30 owner-confirmed historical margin movements: top explanation correct ≥70%; stated confidence calibrated within an agreed band; correct abstention on an injected "no-cause-in-data" set.
- Median human onboarding time **≤8 hours** by customer #10 (contribution math breaks above ~4 CS+validation hours per customer-month at $900).
- ≥60% of surfaced cases rated "useful/material" by the owner; weekly brief open rate >50% after week 6.

### Out of scope
Everything under "Postponed/Removed" above, plus fine-tuning, on-prem, and any write-back.

### 8–12 week delivery plan (small team: 2–3 engineers + 1 domain/sales founder)
| Weeks | Milestone |
|---|---|
| **Pre-0 → 4** | **Concierge validation (no product build)** — see Deliverable 11 Phase 1; collect real exports; time cleaning hours; hand-produce memos |
| 1–2 | Ingestion + canonical model for Shopify and QBO/Xero via dlt/Nango; profiling; reconciliation checks |
| 3–4 | Metric compiler (YAML) + margin tree; seasonal baselines; materiality gate |
| 5–7 | Investigation engine (decomposition, supplier-vs-price check, event-window compare, evidence grader); eval harness with golden incidents from the concierge phase |
| 8–9 | Case page + weekly email brief; confirmation-question onboarding flow |
| 10–11 | Decision log + follow-up scheduler; audit log; tenant-isolation tests |
| 12 | Hardening, pilot onboarding of first 5–10 paid customers, SOC 2 controls plan |

**Technically too ambitious for 8–12 weeks:** calibrated RCA across arbitrary ERPs, simulation, graph propagation, auto-onboarding of custom systems, SOC 2 Type II.

---

## Deliverable 11 — Validation Plan

**The smallest test that could disprove the idea (from the devil's advocate):** a ~3–4-week concierge "investigation memo" test, near-zero engineering.

### Phase 1 — Concierge (weeks 0–4, cost ≈ time only)
1. **Recruit 10–15 businesses in one niche and one stack** (e.g., specialty product brands on Shopify + QBO/Xero). **Not only cold outreach**: pitch 3–5 accountants/fractional CFOs and 1–2 ERP resellers on a *free "margin leak audit" for their clients*; post in Shopify Community / DTC Slack and Discord groups as "what's actually broken in your margin reporting?"; offer a trade-association benchmark swap (NAW-type members seek benchmarks); use the Xero/Shopify app-store listing only as a later channel.
2. **Get read-only access or exports. Time every hour spent cleaning data** (tests the #2 failure reason directly).
3. **Each week, produce a human-assisted memo** with off-the-shelf Claude + connectors (the $20–200 competitor itself): 1–3 investigated margin movements, each as a case file.
4. **Blind-rank against the incumbent:** give each customer their own Intuit/Xero/Shopify/Claude-for-Small-Business output on the same question; owners rank the two without labels.
5. **Charge $200–500/month from week 3** (a free pilot proves nothing).
6. **Seed wrong explanations** in a few memos to see whether owners catch them (tests the confidence UX and trust).

### Phase 2 — Demo prototype + landing page (weeks 3–6, parallel)
Fake-door landing page describing the Brief ("Your margin moved. Here's why — with evidence.") with a "request a margin audit" CTA; measure conversion from advisor posts and communities. A clickable case-file demo built from real Phase-1 memos for sales conversations. (Design the UI only as far as needed; no full UI program yet.)

### Phase 3 — Paid pilot (weeks 5–12)
5–10 paying customers on the productized service with a setup fee ($1.5k–$3.5k) and $349–$999/month; track CS+validation hours per customer-month from day one.

### Willingness-to-pay test
Price the Starter at $349/mo + $1.5k setup and Growth at $999/mo + $3.5k setup [A]; separately probe the savings-share variant ($500 platform + 10–15% of verified savings, capped) **only** after 3–5 documented wins. Anchor: self-serve comps $50–$750/mo; mid-market FP&A $25–$80k/yr; light fractional-CFO retainer $1.4–3k/mo (your Growth tier should sit below it with a distinct deliverable).

### Success criteria (all should hold by ~week 12)
- ≥30–40% of qualified prospects pay the setup fee or sign a paid pilot.
- Blind comparison: owners prefer the case file over the incumbent output in a clear majority.
- Top explanation correct ≥~70% against owner-confirmed causes on ≥30 movements; confidence reasonably calibrated.
- Median onboarding ≤8 human hours; entity resolution ≥80% without manual fix.
- ≥60% of cases rated useful; ≥1/3 of cases lead to a logged action within 7 days; ≥3 customers can name a dollar outcome.
- 6-month logo retention trending >85% in the first cohort, or an advisor channel delivering customers at near-zero CAC.
- ≥8 of 10 prospects grant read access without a heavy security review.

### Kill criteria (any one should force a stop or re-pick)
- **<30% of qualified prospects pay**, or owners rate the memo no better than the incumbent/Claude output.
- **Data-cleaning/validation hours per customer exceed what a $200–$500 price (or $900) can bear** (>~4 CS+validation hours per customer-month at $900).
- **Top-explanation accuracy < ~60%** on owner-confirmed causes.
- Surfaced-case "useful" rate below ~50% after 6 weeks, or the brief is muted/ignored.
- Advisors and owners both decline to pay for decision tracking and follow-up (drop it from the pitch, don't force it).
- After two more quarters, Intuit/Xero/Shopify/Anthropic ship persistent cross-source margin investigation and customers confirm they no longer hit a wall.

---

## Deliverable 12 — Financial Model (preliminary, conservative, mostly ASSUMPTION)

*(Source: `appendix/agent6_economics.md`; calc script: `appendix/model.py`. Every price in the cost model is a third-party-aggregator figure — re-check Anthropic/OpenAI/Google pricing pages before relying on it.)*

**Headline findings**
1. **LLM cost is not the problem.** A grounded investigation ≈ $0.09–$0.26 in tokens (Haiku triage + Sonnet investigation with cache reads + verification pass); inflated ×1.6 for retries/loops → ~$0.30. At 50–80 investigations/customer/month that's **$5–36/month, 1–4% of price.** Do not price per token.
2. **Humans are the cost.** Onboarding (14–40 hours; use ~24), validation, and customer success are **70–85% of COGS**. Price and CS load dominate sensitivity; LLM cost barely moves it.
3. **Price floor ≈ $600/month blended**, below which human review drives gross margin negative.

**Packaging [ASSUMPTION]** — metric = monitored entities × connected sources × investigation allowance; unlimited seats.

| | Starter | Growth | Scale/Enterprise |
|---|---|---|---|
| Target | $2–10M revenue, 1 business line | $10–75M, 2–5 entities | $75–200M, finance team exists |
| Price/mo | **$349** | **$999** | $2,500–6,000 |
| Sources / entities | 3 / 1 | 10 / 5 | unlimited / custom |
| Investigations/mo | 20 | 100 | 400+ |
| Human analyst notes | quarterly | monthly | bi-weekly + named analyst |
| Setup fee | $1.5k | $3.5k | $7.5–15k |
| Overage | $8/investigation | $5 | negotiated |

**Value-based option:** $500/mo + 10–15% of verified savings, capped at 2× annual platform fee — only after 3–5 documented wins; attribution disputes and baseline gaming are real risks.

**Unit economics (base, $900/mo):** variable COGS ≈ $409/mo (LLM $18, infra $45, ingestion $30, validation $66, CS $250) → contribution ≈ $491/mo; with CAC $4,000, payback ≈ 8 months (contribution) [A].

**P&L by scenario** (opex = heads × $12k loaded + tools; excludes setup-fee income and CAC program spend):

| Customers | Conservative ($450, GM −44%) | Base ($900, GM ~55%) | Optimistic ($1,500, GM ~82%) |
|---|---|---|---|
| 5 | −$26.5k/mo | −$23.0k/mo | −$19.3k/mo |
| 20 | −$42.4k | −$28.7k | −$13.8k |
| 100 | −$123.6k | −$54.9k | **+$19.3k** |
| 500 | −$464k | −$120.5k | **+$250k** |

Headcount ladder: 2 → 3 → 8 → 28 at 5 / 20 / 100 / 500 customers. Base case breaks even only at ~212 customers on that ladder because hiring was front-loaded; a leaner ladder (~$15–20k MRR per head) could break even around 100–150. Optimistic breaks even at ~32.

**Fixed costs [ASSUMPTION unless noted]:** SOC 2 ≈ $15–60k first year (vendor-biased, 2–3× spread; ~$25k used); cloud/observability/CRM/legal $1.5k/mo at 5 customers → $30k/mo at 500; fully loaded person ≈ $12k/mo.

**Runway:** at 5 and 20 customers **every scenario loses $13–43k/month at full salaries** → roughly **$250–450k runway or founder-subsidized cash** to reach ~20 customers; ~half that if founders draw $4–5k.

**Break-even rule of thumb:** a 2–3 person team needs **~30 customers at ~$1,000–1,300/month or ~50–60 at $900** (≈$360–470k ARR at 30).

**Operating cost at 5 / 20 / 100 / 500 customers (base case, monthly COGS):** $2.0k / $8.2k / $40.9k / $204.5k (LLM $90 / $360 / $1.8k / $9k — i.e. immaterial).

**Funding reality (SOURCED, noisy):** AI seed medians ~$15–19M pre-money; Series A bar ≈ $2–4M ARR (= ~190–370 customers at $900). Realistic milestone: **raise a seed on 20–40 paying customers**, or bootstrap on the productized-service model. AI-native gross margins average ~50–60% vs 75–90% classic SaaS (secondary summaries; contested).

**Self-serve vs high-touch:** the first 20 customers should be **high-touch, "SaaS-enabled service"** — fixed scope per tier, hour caps, no custom dashboards, every manual step ticketed for automation. Self-serve comps ($49–$400/mo) cannot fund 14–40 hours of onboarding. This is consulting-in-disguise unless the *advisor* becomes the customer (Strategy B) or automation is earned step by step.

---

## Deliverable 13 — Competitive Moat Roadmap

**Be realistic about what a moat is.** Most accumulated data is *not* a moat. Only four assets create real defensibility: (a) **labeled outcomes** that improve accuracy, (b) **switching costs** from decision history and confirmed company model, (c) **trusted distribution**, (d) **reliability/depth** on a specific stack.

| | Year 1 | Year 3 | Year 5 |
|---|---|---|---|
| **Assets that accumulate** | 20–40 customers' *confirmed* models; hundreds of owner-labeled investigations (right/wrong/"what was actually going on"); first golden-incident set; 3–5 documented dollar wins; 3–10 advisor relationships | Vertical hypothesis library + calibrated per-vertical priors (de-identified, consented cross-tenant); thousands of outcome-labeled decisions; templated source mappings (onboarding in hours); benchmark data | Outcome-labeled decision corpus large enough to answer "what usually works when X"; multi-stack coverage; advisor network; possibly a recognized "evidence format" |
| **Advantages created** | Learning speed and a credible case study — **not a moat yet** | Better precision at lower cost; lower CS load per customer; switching cost from decision history | Compounding accuracy + distribution; defensible niche leader |
| **What incumbents can replicate** | Everything visible: UI, alerts, narratives, connectors, agents | Generic RCA, semantic layers, decision logs (Aera already ships one) | A well-resourced platform with the same data could catch up on accuracy if it commits |
| **What is hard to replicate** | Founder-level proximity to a niche's data quirks | Calibrated, abstaining RCA tuned on *labeled incidents* in one vertical; advisor trust | Cross-tenant priors and outcome history (needs customers + time + consent) |
| **Risks of imitation** | Intuit/Xero/Shopify/Anthropic ship persistent cross-source margin investigation | Platform vendors move down-market; consolidation acquirer absorbs you | Category consolidates; independent outcome is an acquisition |

**Honest bottom line:** the moat, if it exists, is *calibrated vertical accuracy + trusted advisor distribution + outcome history* — all of which only materialize with customers. This points to an **acquisition-plausible** business as much as a category-defining one (Sisu, Peak, Metaplane precedents). That can still be a good outcome for a capital-light founder; just don't plan around becoming Palantir.

---

## Deliverable 14 — Final Founder Decision

1. **What exactly should we build?** A **weekly "margin investigation" brief + case-file product** (Margin Loop, Deliverable 10) for one stack — *not* a company-wide digital twin, chatbot, or dashboard. First deliver it as a **concierge service** using off-the-shelf tools; build the engine only after the test passes.
2. **Who is the first customer?** A **specialty product brand or small distributor ($3–75M)** on Shopify and/or an ERP plus QuickBooks/Xero, **introduced by an accountant, fractional CFO or ERP reseller**. (Run Shopify-specialty-brand and distributor niches side by side and see which converts.)
3. **What specific problem first?** **"Supplier cost rose but price didn't / margin moved and nobody can say why"** — price-cost pass-through and margin erosion. It is a detectable event, measurable in dollars, and cross-system.
4. **What should we call the category?** **Margin investigation** (or "continuous business review"/"exception intelligence" — test with owners). Avoid "digital twin" and "decision intelligence."
5. **Most compelling differentiation?** **Cross-system explanation with an honest evidence trail**: separate confidence in the observation vs the explanation, equal-weight counter-evidence, explicit "couldn't check," abstention, and a follow-up on whether the decision worked. *Only claim it after the blind comparison proves owners prefer it.*
6. **What should we not build?** Generic chat, dashboards/BI builder, agent builder, custom/fine-tuned model, knowledge graph/graph DB, multi-agent swarm, simulation, autonomous write-back, big integration catalog, ClickHouse/Kafka/K8s, on-prem, decision-tracking as a headline feature.
7. **First 90 days:**
   - **Days 1–10:** pick niche + stack; line up 3–5 advisors; write the "margin leak audit" offer; recruit 10–15 businesses; sign data-access terms; set up time-tracking of cleaning hours; start Reddit/HN pass.
   - **Days 10–40:** run weekly concierge memos (Claude + connectors); blind-rank against incumbent output; charge $200–500/month from week 3; log every hour; seed wrong explanations; build the golden-incident set.
   - **Days 40–50:** go/no-go against the kill criteria.
   - **Days 50–90 (if go):** build the thin engine on the stack (ingestion → margin tree → investigation → brief/case → decision log); convert pilots to $349–$999 plans + setup fee; track CS hours; ask 3 customers for documented dollar wins.
8. **What should I do this week?** (a) Pick the niche and stack; (b) write a one-page "margin leak audit" offer and 10 target names *including 3 accountants/fractional CFOs*; (c) do the 2-hour direct Reddit/HN pass (queries in `appendix/agent2_market.md` §7); (d) run **one** audit by hand on a friendly business with Claude + their exports, timing the data cleaning; (e) read Anthropic's Claude for Small Business page and Intuit/Xero/Shopify docs *directly* so you know exactly what you're up against.
9. **Assumptions to prove before development:** SMB owners **pay** for causal explanations (not just alerts); data access works without heavy implementation; onboarding is ≤8 human hours; top explanation is ≥70% right and calibrated; the case-file output is preferred to the incumbent's in a blind test; advisors will refer/resell; owners grant read-only access to an unknown vendor.
10. **What would make me abandon it?** Any kill criterion in Deliverable 11 — especially **(i)** owners rate your memo no better than their in-product/Claude output; **(ii)** data-cleaning hours make $900/month uneconomic; **(iii)** explanation accuracy <60%; **(iv)** nobody pays the setup fee. If (i) fails, try Strategy B (advisor as customer) once before stopping; if both fail, stop.

---

## 15. Answers to the ten differentiation questions (§6 of your brief)

1. **Commoditized:** connectors/RAG, NL Q&A, no-code agent builders, MCP, KPI alerts, semantic-layer-as-AI-context, basic anomaly detection.
2. **Becoming commoditized:** proactive monitoring agents (Qlik, Tableau Next, Genie, Sidekick Pulse, JAX), "ontology/context layers" (Fabric IQ, Palantir, ServiceNow+Pyramid), in-product next-step recommendations (Intuit).
3. **Hard for incumbents:** cross-system causality (none sees the others' data), abstaining/calibrated RCA, vertical hypothesis libraries, small-customer onboarding economics.
4. **Poorly solved:** price-cost leakage explanation, cross-system margin "why", verification of AI-generated analysis.
5. **Expensive enough to pay:** margin leakage (0.5 pt on $20M = $100K/yr), recoverable freight/billing errors, stockout/overstock — hypotheses, to be tested.
6. **Unnecessarily complex:** semantic-layer prerequisites, warehouse + data-team dependency, free-form chat that returns plausible wrong SQL.
7. **Underserved segments:** $3–75M specialty product brands and distributors without data teams.
8. **Frustrations:** trust in AI answers (consistent across vendor sources), learning curve, spreadsheets running in parallel, "dashboards show what, not why".
9. **Still manual:** month-end bridges, KPI pulls from 3–5 exports, supplier price reconciliation, reorder spreadsheets, checking AI outputs.
10. **Not a smaller Palantir/Aera/Glean/Copilot:** a *narrow, evidence-first investigator for one problem in one stack, sold through advisors* — the opposite of a platform.

---

## 16. What remains unverified — do this before you rely on the report

- **Primary-source checks:** Anthropic's Claude for Small Business page and Cowork scheduled-task limits; Microsoft Fabric IQ GA status; Snowflake Intelligence/"CoWork" status; SAP Joule/Business Data Cloud, Oracle, NetSuite, Salesforce 2026 launches; Intuit/Xero/Shopify AI docs.
- **Competitor detail:** read G2/Gartner Peer Insights/TrustRadius in full; trial Tellius, WisdomAI, Zenlytic, Qlik Discovery Agent; Anodot ownership; Sisu post-mortem (none found — consider interviewing former Sisu/Chartio staff); Cloverpop current ownership; Peak exit price (single source).
- **Demand evidence:** Reddit/HN threads by hand; QuickBooks/NetSuite/Odoo user counts from filings; Techaisle and MIT NANDA primary PDFs; independent measurement of metric-RCA precision at SMB data volumes.
- **Economics:** Anthropic/OpenAI/Google API prices from vendor pages; SMB churn for <$100/mo ACV; ACV benchmarks for AI analytics (none found).
- **Architecture:** Bedrock/Azure/OpenAI retention terms; eval-tooling licences; OSI naming status; TimesFM/Moirai licensing.
- **Do not cite** as fact: MIT NANDA "95%" (disputed methodology), "60–70% of dashboards unused (Gartner)" (unsupported), Traversal "90%" AI-SRE accuracy (unattributed).

---

## Appendix map

| File | Contents |
|---|---|
| `appendix/agent1a_competitors.md` | Enterprise AI + decision-intelligence profiles and matrix |
| `appendix/agent1b_competitors.md` | BI incumbents, process intelligence, AI-native startup funding table |
| `appendix/agent2_market.md` | Customer pain evidence, vertical scoring (12 criteria), top-8 problems, pilot channels |
| `appendix/agent4_architecture.md` | Full architecture, build-vs-buy, security, risks |
| `appendix/agent5_ux.md` | UX evidence, critique of the Investigation Queue, IA, notification policy, naming |
| `appendix/agent6_economics.md` + `model.py` | Pricing evidence, cost model, P&L scenarios, sensitivity |
| `appendix/agent7_devils_advocate.md` | Graveyard, pre-mortem (10 failure reasons + falsifiers), cheapest kill test, surviving variants |

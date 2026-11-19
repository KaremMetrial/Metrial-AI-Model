# Agent 1B: Competitive Intelligence (as of 2026-11-19)

## 0. Method, source quality, and honest caveats

- Research was done with WebSearch only. WebFetch failed on every host tried (pulse2.com, techcrunch.com, techzine.eu, tableau.com all returned DNS/ENOTFOUND, i.e. blocked by the session's network allowlist). I therefore could NOT read primary vendor pages for most claims. Nearly everything below comes from search-result summaries of press, aggregator, or vendor-marketing pages.
- Label legend: VERIFIED = stated in a source that looks primary or reputable trade press and I saw it in results (still not read in full); ADVERTISED = vendor/marketing claim, no independent evidence of how well it works; PARTIAL = exists but narrow; INFERRED = my reasoning; UNKNOWN = not found.
- Treat all funding figures from aggregators (neuronfeed, pulse.bot, startupim, raising.fi, tamradar, etc.) as "reported", not confirmed. Where sources conflict I say so.
- Nothing here is a hands-on test. Capability labels reflect documentation/marketing, not observed accuracy. No independent accuracy benchmark for any autonomous RCA product was found.

## 1. Headline conclusions (brutal version)

1. "Proactive monitoring + anomaly detection + AI-written explanation" is commoditized at the incumbent tier. Qlik (Discovery Agent, GA Feb 2026), Tableau (Pulse, Tableau Next Autonomous Insights), ThoughtSpot (Monitor/Spotter), Databricks (Genie agent mode, proactive/background), Power BI (line-chart anomaly detection, Activator alerts), Looker (Conversational Analytics GA) all ship some version of it. A founder cannot differentiate on "watches your metrics and tells you something changed."
2. The incumbents' weakness is not the feature, it is the prerequisite: a modeled semantic layer, a warehouse, and an admin to curate metrics. Their proactive agents run on top of curated metrics, not a messy raw SaaS estate. Zero-data-team onboarding for SMB is genuinely unserved by them. But see point 5.
3. Funded AI-native startups are converging on the exact thesis. WisdomAI (Series A $50M, Nov 2025) explicitly ships "proactive agents" that flag metric shifts, do RCA, and remember prior anomaly causes. Gravity/Orion (~$10M, Apr 2026) markets continuous monitoring + multi-agent root-cause investigation. Both target enterprise/upper-mid-market, not SMB. They are the closest direct competitors and are 12-24 months ahead on funding.
4. At the SMB end, narrow vertical monitors already exist cheaply (Shopify apps such as CheckoutGuard at $79-$199/mo with "AI root-cause analysis", Metrixon, Shoptest $99/mo, Monitrees, RevCure). Horizontal "business observability for SMB" is thin, but vertical slices are being filled by $79-$199 tools and indie hackers, which caps willingness to pay for a generic product.
5. Real gaps (not claimed by anyone I found with evidence): (a) explicit correlation-vs-causation framing with calibrated confidence and an evidence trail; (b) decision tracking with outcome learning tied back to monitored metrics; (c) cross-system "living model" of the company (entities, drivers, dependencies) built without a data team; (d) impact propagation across metrics. "Decision intelligence" funded players (Aily Labs $80M, Pluvo, Omniscient) exist but target enterprise finance/planning or external risk, not SMB closed-loop decision/outcome logging.
6. Platform risk is severe: Snowflake, Databricks, Google, Microsoft, Salesforce all ship agents plus MCP servers, and observability vendors are consolidating (Datadog bought Metaplane Apr 2025; Snowflake agreed to buy Observe Jan 2026; Snowflake absorbed Sisu Oct 2023 and discontinued it standalone). Sisu, the closest historical precedent for "automated driver analysis," did NOT survive as an independent product.

## 2. Incumbent BI profiles (proactive monitoring / RCA focus)

### Microsoft Power BI / Fabric
- Built-in line-chart anomaly detection and "Analyze / explain the increase" (contribution by field) exist and are NOT Copilot features (reported via third-party blogs; community.fabric.microsoft.com threads, ecosire.com). Label: VERIFIED-ish (long-standing documented features), PARTIAL for RCA (statistical contribution analysis, not causal).
- Copilot in Power BI routes questions across semantic models, reports, and Fabric data agents (Microsoft Fabric blog: blog.fabric.microsoft.com/en/blog/extracting-deeper-insights-with-fabric-data-agents-in-copilot-in-power-bi). VERIFIED.
- Fabric Activator monitors data thresholds and triggers actions: reported by third-party posts. Threshold-based, not model-based. PARTIAL.
- A Collab365 item (spaces.collab365.com) claims the Copilot/data-agent integration retires 26 Aug 2026; I could not verify. UNKNOWN. An EPC Group post claims "operations agents" GA at Build 2026; no primary confirmation. ADVERTISED.
- Limits: requires Fabric capacity/Power BI licensing, a curated semantic model; Copilot needs paid capacity. Target: Microsoft shops with an analyst. Not SMB zero-setup.

### Tableau (Salesforce): Pulse, Agent, Tableau Next
- Pulse: automatically detects drivers, trends, contributors, outliers for metrics users follow (help.tableau.com pulse intro / insights platform insight types). VERIFIED. Independent analysis (thedataschool.co.uk, "Tableau Pulse, Explained: Key Considerations") frames it as descriptive: what happened and when, not causal why. A competitor blog (infinisynapse) says Pulse "explains movement, doesn't always investigate why" (biased source). Causal "why" is left to Explain Data/analysts. PARTIAL.
- Tableau Next blog (tableau.com/blog/how-to-set-up-proactive-intelligence-tableau-next, dated 2 Nov 2026): always-on agent surfaces risks; requires enabling Autonomous Insights and selecting an agent (none by default). ADVERTISED/VERIFIED existence, effectiveness unknown. "Pace to Threshold" forecast-vs-threshold insight in release notes. PARTIAL.
- Premium AI (Agent, premium Pulse) is gated behind Tableau+ per third-party posts. Pricing opaque. Needs Tableau Cloud / Salesforce stack. Not SMB zero-setup.

### Looker (Google)
- Conversational Analytics GA 13 Nov 2025 (cloud.google.com/blog/products/business-intelligence/looker-conversational-analytics-now-ga). VERIFIED. Next '26 (Apr 2026): embedded conversational agents GA; upgraded core agent and new Looker UI in Preview (cloud.google.com/blog/.../looker-updates-for-agentic-bi-at-next26). Conversational Analytics API GA for BigQuery and Looker by Sept 2026 release notes. Gemini Enterprise publishing: Preview.
- Proactive monitoring/anomaly alerting: I found no evidence of an autonomous monitoring/RCA agent in Looker. UNKNOWN. Positioning is Q&A over the LookML semantic layer. Requires LookML modeling, i.e. a data team.

### ThoughtSpot (Spotter, SpotIQ, Monitor)
- Spotter agent launched Nov 2024; Spotter 3 / agents for modeling, visualization, code slated early 2026 (TechTarget; IT Brief Dec 2025). SpotIQ automated insights are older. Monitor helps track KPIs and find "main drivers of change" (thoughtspot.com product page). PARTIAL.
- Docs for 10.15 describe proactive suggestions as "Limited" and metadata-based (docs.thoughtspot.com). The "autonomous monitoring that can take actions" is blog-level vision (thoughtspot.com/blog/insights-to-actions-with-agentic-analytics). ADVERTISED. No evidence of confidence/causal framing. Enterprise pricing, sales-led.

### Qlik (Answers, Insight Advisor, Discovery Agent)
- Discovery Agent GA Feb 2026: continuously monitors key measures, detects anomalies, alerts on material changes, works without prompting; Qlik reports >100,000 "discoveries" surfaced since GA (BusinessWire 14 Apr 2026, qlik.com press room). VERIFIED (vendor-reported counts). April 2026 also added Automate/Analytics/Predict agents and an MCP server; TechTarget analyst notes Qlik does not provide an agent-building framework. This is the most literal incumbent match to "monitor for material changes." RCA depth: UNKNOWN. Requires Qlik Cloud app/data model.

### Databricks (Genie, AI/BI)
- Genie Agent Mode (blog 17 Apr 2026, databricks.com/blog/introducing-genie-agent-mode): iterative plan/explore/reason over data; reportedly default in spaces later in 2026 (release notes, docs.databricks.com/.../ai-bi/release-notes/2026). VERIFIED. Techzine/SD Times describe Genie as autonomous, proactive, "always on", running background compute; source is ambiguous on which Genie variant (Genie One / Zero Ops). ADVERTISED. Requires Unity Catalog/lakehouse and curated Genie spaces. Not SMB.

### Snowflake (Cortex Analyst, Snowflake Intelligence)
- A secondary source (brillio.com) says Snowflake Intelligence was renamed "CoWork" and Cortex Code "CoCo", with bots performing recurring tasks autonomously. Low-confidence; ADVERTISED. Sisu acquired Oct 2023, standalone product discontinued (yespress.io/sisu-data, basedash.com blog). Requires Snowflake data.

### Sigma, Omni, Domo, Zoho, Metabase (BI challengers)
- Sigma: $80M Series E, ~$3B valuation, >$200M ARR Apr 2026 (reported May 2026; aiweekly.co, pulse.bot). Omni: $120M Series C at $1.5B led by ICONIQ, Apr 2026, ARR ~4x YoY, reported profitable (pulse2.com, pulse.bot, beri.net). Both are warehouse-centric BI with AI query layers; no evidence of autonomous RCA. These are headcount-light BI winners, proof the market pays for semantic-layer-plus-AI, not for monitoring.
- Domo: TechTarget analyst says Domo enables users to build agents; no 2026 specifics found. UNKNOWN. Zoho Analytics, Metabase AI: not found in 2026 results. UNKNOWN.

## 3. Process intelligence and automation

- Celonis: Gartner MQ Leader (process intelligence, 2026 per company release), claims >$10B customer value; AgentC/Orchestration Engine, MCP server for process intelligence, AI Task Discovery in private preview, Microsoft Agent 365 launch partner, Oracle OCI collaboration (Apr 2026) (celonis.com/news/press, businesswire 4 Feb 2026 and 10 Apr 2026). VERIFIED (vendor). Enterprise-only, event-log/ERP centric (SAP, Oracle). Models processes, not the P&L/commercial business. No SMB motion found.
- SAP Signavio, UiPath (+Peak), Skan: searches returned nothing; UNKNOWN for 2026 status. Do not rely on me for these. INFERRED: all enterprise, ERP/process-event-log oriented, adjacent rather than competing for SMB "living model."
- Relevance: process mining gives a different "living model" (control-flow of operations). It is a partner/integration or later-stage expansion, not a head-on competitor for an SMB metrics-and-decisions product.

## 4. AI-native BI / analyst / monitoring startups

| Company | Stage / funding (reported) | Product and target | Monitoring / RCA / decision features | Evidence label | Notes, risks |
|---|---|---|---|---|---|
| WisdomAI | Seed $23M (Coatue, ~mid-2025); Series A $50M led by Kleiner Perkins with NVentures, Nov 2025 (wisdom.ai/blog/announcing-our-series-a-funding; kleinerperkins.com; techcrunch 2025-11-12) | AI data analyst; "conversational and proactive agents"; enterprise (Cisco, Rubrik, ConocoPhillips per Descope case study) | Proactive agents flag meaningful metric shifts, run RCA, remember past anomaly causes (Sept 2025 launch) | Existence VERIFIED; RCA quality ADVERTISED; customer list self-reported | Closest funded analog to the monitoring+RCA+memory thesis. Enterprise motion, no public pricing found. |
| Gravity (Orion) | ~$10M total, announced Apr 2026 (pulse2.com; raising.fi); sources conflict on rounds (also $3.2M seed Village Global; $7M per Endeavor Colorado) | "Autonomous AI analyst" / multi-agent decision intelligence "built to replace dashboards"; has a Claude connector listing (claude.com/connectors/orion) | Continuous monitoring, anomaly detection, root-cause tracing by agents, recommendations | ADVERTISED | Names collide with ORION Security ($32M DLP), do not confuse. Smaller and earlier than Wisdom. SMB focus UNKNOWN. |
| Hex | ~$100M raise reported 2026, possibly Series D, ~$1.2B valuation (dealroom; fourweekmba, unconfirmed by second source) | Collaborative notebook/analytics; rebuilt "agent-first" | Agents for analysis; no autonomous monitoring found | Funding UNVERIFIED; features ADVERTISED | Data-team tool. |
| Julius AI | $10M seed led by Bessemer, Jul 2025 (techcrunch 2025-07-28); no 2026 raise found | Chat-with-your-data for individuals/small teams; freemium, Plus ~$20/mo (dupple.com) | No proactive monitoring found | VERIFIED seed | Cheap, self-serve; reactive only. |
| Zenlytic | Series A $9M led by M13, Sep 2024; ~$15.4M total per CB Insights; no 2026 round found | Semantic-layer AI analyst ("Zoë") for ecommerce/DTC and mid-market | Zoë advertised as proactive/autonomous in the past; current 2026 specifics UNKNOWN | UNKNOWN | Pricing not public (G2). Ecommerce vertical, a direct competitor for DTC SMB. |
| Fabi.ai | Funding UNKNOWN | AI analyst + SQL/Python; ~$39/seat/mo per one aggregator (conflicts with free-tier claim) | None found | ADVERTISED | |
| Basedash | Funding UNKNOWN | Chat BI; credit-based pricing, 30-day trial | None found | ADVERTISED | Third-party cites $250/mo; conflicting. |
| Wren AI | Open-source GenBI, founded 2024; funding UNKNOWN | Text-to-SQL with semantic layer | None found | UNKNOWN | |
| Omni | $120M Series C @ $1.5B, Apr 2026 | Semantic-layer BI with AI | No autonomous RCA found | VERIFIED funding | By ex-Looker founders; data-team-assisted. |
| Sigma | $80M Series E @ ~$3B, 2026 | Spreadsheet-style BI on warehouse + AI apps | None | VERIFIED-ish | |
| Monte Carlo | $135M round at $1.6B (dates conflict 2024 vs Oct 2025 across aggregators); launched Observability Agents (Apr 2025), Agent Observability (Mar 2026), "Bayes" AI teammate (reported late Oct 2026) | Data/AI observability for data teams | Monitors data quality/pipelines, not business KPIs | VERIFIED category | Adjacent: monitors data health, not business causality. Could expand toward business metrics. |
| Metaplane | Acquired by Datadog, Apr 2025 | Data observability | Data-quality ML monitors | VERIFIED | Consolidation precedent. |
| Anodot (Amazon-hosted marketplace listing; reportedly acquired by Glassbox Nov 2025, per startupim aggregator, UNVERIFIED) | 20% layoffs May 2023 (aggregator) | Autonomous business metric anomaly detection/correlation for ecommerce, telco, adtech | Long-standing anomaly correlation and alert grouping | ADVERTISED; ownership UNVERIFIED | The original "business metrics monitoring" product; stagnated/changed hands. Cautionary tale. An ideaproof.io page lists it under "Failed 2024". |
| Sisu | Acquired by Snowflake Oct 2023; standalone discontinued | Automated driver/diagnostic analysis ("decision intelligence") | Key driver analysis | VERIFIED | Precedent: automated drivers analysis was absorbed, not a standalone win. |
| Causal | Acquired by LucaNet, Oct 2024 | Modeling/FP&A | n/a | VERIFIED | Finance modeling consolidates into CFO suites. |
| Lightup, Narrative BI, Pecan, Akkio, Mosaic, Pigment | UNKNOWN (searches returned nothing usable) | | | UNKNOWN | Do not assume alive or dead. |

### Decision intelligence / "AI CFO" / SMB-adjacent (funded 2025-2026)

| Company | Funding (reported) | Focus | Relevance |
|---|---|---|---|
| Aily Labs | $80M Series B (Nov 2025, reported Jan 2026; folio3, pulse2) | Enterprise decision intelligence | Large-enterprise, different buyer. |
| Pluvo | $5M seed | "AI decision intelligence" for finance teams | FP&A-focused. |
| Omniscient | $4.1M pre-seed, Apr 2026 (siliconangle) | External risk/reputation decision intelligence for insurers etc. | Not an internal business model. |
| Una Software | $13M total | AI-native FP&A | Finance only. |
| Finley | $1.3M seed, Aug 2026 (startupwired) | AI CFO for mid-market | Closest to "AI CFO"; tiny. |
| CentSight | $1.5M pre-seed, Jun 2026 (fintech.global) | SMB financial Q&A over accounting/bank data; "identifies issues early" | SMB AI-CFO chat plus dashboards; monitoring depth ADVERTISED. |
| Nume (Scaleup Finance) | GBP 3M, Oct 2025 (tech.eu) | AI CFO for startups/SMEs | |
| Affiniti | $17M Series A | Vertical AI CFO agents/SMB finance | Payments/banking angle. |
| Numos, Stacks, OpenCFO | $4.25M, $23M Series A (Feb 2026), $2M seed | Enterprise/mid finance ops | Not SMB monitoring. |
| 1STLabs | $49M seed reported (secondary blog; verify) | "Digital twin of the enterprise" for IT request resolution | Uses "digital twin" for ITSM, not business metrics. |
| Twin1 AI, Viven | $20M seed (Aug 2026), $35M seed (Oct 2025) | Per-person digital twins | Name collision only; different concept. |

Observation: funding clusters at $1-5M for SMB "AI CFO" and $50-250M for enterprise analytics/BI. Capital for the SMB horizontal monitoring thesis is thin, which is either an open lane or a signal that the SMB market does not pay.

### SMB vertical monitors (already in market, cheap)
- CheckoutGuard (Shopify): order-rate vs 7-day baseline; Growth $79/mo includes AI RCA on alerts, top tier $199/mo with payment-failure checks every 60s (apps.shopify.com/checkoutguard-3). ADVERTISED.
- Metrixon (free tier), Shoptest from $99/mo, Monitrees (Stripe/PayPal/Shopify/ads), RevCure (launched 20 May 2026), a "Datadog for business metrics" Indie Hackers post. All ADVERTISED; adoption and accuracy UNKNOWN. A practitioner playbook (warpdriven.ai) states a "revenue down" alert triggers RCA, and causal claims should stay provisional until human-validated.

## 5. Capability matrix

Legend: V = VERIFIED (exists per reputable/primary-looking source), A = ADVERTISED (claimed, effectiveness unproven), P = PARTIAL/narrow, U = UNKNOWN, - = not offered/not found.

| Capability | Power BI/Fabric | Tableau | Looker | ThoughtSpot | Qlik | Databricks | Snowflake | WisdomAI | Gravity Orion | Zenlytic | Celonis | SMB Shopify monitors | CentSight/Finley (AI CFO) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NL Q&A over data | V | V | V | V | V | V | V | V | A | V | P | - | A |
| Continuous metric monitoring | P (Activator thresholds) | V (Pulse) | U | P (Monitor) | V (Discovery Agent) | A | A | A | A | U | P (process KPIs) | V/A | A |
| Anomaly detection | V (line charts) | V | U | P | V | A | U | A | A | U | P | A | A |
| Autonomous multi-step cause investigation | P (explain-increase) | P (Explain Data) | U | P | U | A (agent mode) | A | A | A | U | P (process root cause) | A (shallow) | U |
| Evidence trail shown | P | P | P | P | U | P | U | A | A | U | V | U | U |
| Calibrated confidence / correlation vs causation | - | - | - | - | - | - | - | U | U | U | - | - | - |
| Impact propagation across metrics | - | - | - | - | - | - | - | U | A | U | P | - | - |
| Persistent memory of past anomalies/causes | - | - | - | - | - | U | U | A | U | U | - | - | - |
| Decision tracking and outcome learning | - | - | - | - | - | - | - | - | A ("recommendations") | - | P (action tracking) | - | - |
| Persistent entity/company "living model" | P (semantic model) | P | V (LookML) | P | P | P (UC/Genie spaces) | P | U | U | V (semantic layer) | V (process model, enterprise) | - | - |
| Zero-data-team SMB onboarding | - | - | - | - | - | - | - | - | U | P (ecommerce) | - | V (app install) | P |
| Public self-serve pricing | P | P | - | - | - | P | P | - | U | - | - | V | U |

Reading the matrix: no one has a VERIFIED cell for calibrated confidence, causal-vs-correlational framing, impact propagation, or decision-outcome learning. That is either the gap or the part users do not value enough to buy. I found no customer-demand evidence either way.

## 6. Who is closest to the idea, and what they do not do

1. WisdomAI (closest on thesis). Does: proactive agents, RCA, memory of earlier anomalies; enterprise customers; well-funded. Does not (as far as evidence shows): SMB zero-setup; decision tracking/outcome learning; explicit confidence and causality labeling; a persistent company model beyond a semantic layer. Not found: public pricing, independent accuracy data.
2. Gravity / Orion. Does: monitoring plus multi-agent investigation plus recommendations, "replace dashboards." Does not (known): decision/outcome loop; SMB motion unknown. Early, funding reports inconsistent.
3. Qlik Discovery Agent / Tableau Pulse / ThoughtSpot Monitor. Do: proactive, anomaly-driven alerts at scale with incumbents' distribution. Do not: investigate causally across systems, remember decisions, work without a modeled BI estate, or serve SMB at low cost.
4. Zenlytic. Does: semantic-layer AI analyst for ecommerce/mid-market. Do not know: current proactive/RCA depth. Direct competitor in DTC SMB.
5. Anodot/Sisu lineage. Showed technical feasibility of automated anomaly correlation and driver analysis; both ended acquired/absorbed or stagnant. Why they stalled is INFERRED (hard to monetize stand-alone, needs integrations and trust), not verified.
6. SMB AI-CFO and Shopify monitors. Do: cheap, narrow, finance- or store-specific alerts. Do not: cross-functional modeling, impact propagation, decisions.
7. Process intelligence (Celonis): strongest "living model + action tracking" at enterprise; not SMB, not commercial metrics.

## 7. Implications for a capital-constrained founder (INFERRED, not sourced)

- Do not pitch "AI monitors your metrics" as the wedge; it is table stakes. The defensible claims, if any, are trustworthy RCA (evidence, calibrated confidence, honest "we cannot tell causation") and a decision-to-outcome loop. Neither is proven demanded; test with design partners before building a "living model."
- The strongest wedge candidates: an SMB vertical (ecommerce/SaaS billing) where connectors are few and standard (Stripe, Shopify, QuickBooks/Xero, ads, CRM), because a horizontal model across arbitrary SMB data needs per-customer semantic work that incumbents solve with data teams. Cheap vertical monitors already sit at $79-$199/mo, so ARPA expectations are low unless the product delivers clear decisions/outcomes.
- Platform vendors now expose MCP servers (Qlik, Celonis, Snowflake, Databricks, Looker API). A new entrant can ride these as connectors, but so can general-purpose assistants (Claude/ChatGPT with connectors), a serious substitute for chat-style analyst products, though not for always-on monitoring.
- Consolidation pattern (Sisu, Metaplane, Causal, Observe) implies exit via acquisition is plausible but standalone category-building is hard.

## 8. Not covered or unverified, to be re-checked

- Hex round label/valuation; Gravity round structure; Anodot ownership; Monte Carlo round date; 1STLabs seed; Qlik discovery counts; Fabi/Basedash/Wren funding and pricing; Domo, Zoho, Metabase AI 2026 status; SAP Signavio, UiPath/Peak, Skan; Lightup, Narrative BI, Pecan, Akkio, Mosaic, Pigment; Power BI Copilot data-agent retirement date; Snowflake renaming; any customer complaints or G2/Reddit reviews (I did not retrieve user-complaint data, so complaints per product are UNKNOWN).
- Blocked hosts for WebFetch (would need allowlisting to verify primaries): pulse2.com, techcrunch.com, www.techzine.eu, www.tableau.com.

## 9. Source URLs (as returned by search)

- WisdomAI Series A: https://www.wisdom.ai/blog/announcing-our-series-a-funding ; https://www.kleinerperkins.com/perspectives/wisdomai-series-a/ ; https://techcrunch.com/2025/11/12/ai-data-startup-wisdomai-has-raised-another-50m-led-by-kleiner-nvidia ; https://www.descope.com/customers/wisdomai
- Gravity Orion: https://pulse2.com/gravity-10-million-raised-to-build-orion-an-autonomous-ai-analyst-platform/ ; https://raising.fi/news/gravity-undisclosed-april-2026 ; https://techedgeai.com/gravity-launches-orion-an-agentic-ai-platform-built-to-replace-dashboards/ ; https://claude.com/connectors/orion
- Hex: https://app.dealroom.co/news/note/hex-deletes-its-code-raises-100m-to-go-agent-first ; https://fourweekmba.com/ai-hex-rewrote-its-data-platform-for-ai-agents-and-raised-100m/
- Julius: https://www.techcrunch.com/2025/07/28/ai-data-analyst-startup-julius-nabs-10m-seed-round/ ; https://sacra.com/c/julius
- Omni / Sigma / Zenlytic: https://pulse2.com/omni-120-million-series-c-raised-at-1-5-billion-valuation-for-ai-analytics-platform/amp/ ; https://aiweekly.co/alerts/sigma-computing-hits-3b-valuation-with-80m-series-e ; https://www.vcaonline.com/news/2024092608/zenlytic-secures-9-million-in-series-a-funding-led-by-m13-to-scale-ai-data-analyst/
- Monte Carlo / Metaplane / Observe: https://siliconangle.com/2025/04/17/monte-carlo-puts-ai-agents-work-data-reliability/ ; https://www.datadoghq.com/blog/datadog-acquires-metaplane ; https://www.privsource.com/acquisitions/deal/snowflake-to-acquire-observe-to-deliver-ai-powered-observability-at-enterprise-scale-5ZSe4N
- Sisu / Anodot: https://yespress.io/sisu-data ; https://www.basedash.com/blog/sisu-data-discontinued-alternatives ; https://startupim.com/company/anodot ; https://ideaproof.io/failure/anodot-ai
- Causal/LucaNet: https://app.mergerlinks.com/transactions/2024-10-31-causal
- Qlik: https://www.businesswire.com/news/home/20260414204323/en/Qlik-Extends-Analytics-from-Answers-to-Agentic-Action ; https://www.techtarget.com/searchbusinessanalytics/news/366623785/Qlik-unveils-agentic-AI-capabilities-launches-lakehouse
- Tableau: https://www.tableau.com/blog/how-to-set-up-proactive-intelligence-tableau-next ; https://help.tableau.com/release-preview/online/en-us/pulse_intro.htm ; https://thedataschool.co.uk/stephanie-pichardo/tableau-pulse-explained-what-it-is-who-its-for-and-where-it-falls-short/
- ThoughtSpot: https://www.techtarget.com/data-technologies/news/366636078/ThoughtSpot-automates-full-platform-with-new-Spotter-agents ; https://www.thoughtspot.com/blog/insights-to-actions-with-agentic-analytics ; https://docs.thoughtspot.com/cloud/10.15.0.cl/spotter-getting-started
- Power BI/Fabric: https://blog.fabric.microsoft.com/en/blog/extracting-deeper-insights-with-fabric-data-agents-in-copilot-in-power-bi ; https://learn.microsoft.com/en-my/fabric/fundamentals/copilot-ai-feature-state ; https://spaces.collab365.com/posts/fabric-ends-copilot-data-agent-integration-on-26-a-qy2LTE
- Looker: https://cloud.google.com/blog/products/business-intelligence/looker-conversational-analytics-now-ga ; https://cloud.google.com/blog/products/business-intelligence/looker-updates-for-agentic-bi-at-next26 ; https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/release-notes
- Databricks: https://databricks.com/blog/introducing-genie-agent-mode ; https://docs.databricks.com/gcp/en/ai-bi/release-notes/2026 ; https://www.techzine.eu/news/data-management/145764/databricks-genie-gets-a-makeover-autonomous-proactive-and-always-on/
- Celonis: https://www.businesswire.com/news/home/20260204723950/en/ ; https://www.celonis.com/blog/finally-enterprise-ai-gets-the-context-it-needs-to-succeed-celonis-next-2026
- AI CFO: https://fintech.global/2026/06/26/centsight-launches-with-1-5m-pre-seed-backing/ ; https://startupwired.com/2026/08/17/finley-raises-1-3m-to-build-an-ai-cfo-for-businesses/ ; https://tech.eu/2025/10/22/scaleup-finance-raises-ps3m-to-launch-nume-an-ai-cfo-for-startups-and-smes/ ; https://siliconangle.com/2026/02/19/agentic-finance-automation-startup-stacks-raises-23m-funding/
- Decision intelligence: https://siliconangle.com/2026/04/02/omniscient-raises-4-1m-ai-driven-decision-intelligence-platform/ ; https://pulse2.com/aily-labs-80-million-raised-to-advance-ai-decision-intelligence-adoption-across-global-enterprises
- SMB monitors: https://apps.shopify.com/checkoutguard-3 ; https://apps.shopify.com/metrixon-ai-analytics ; https://apps.shopify.com/shoptest ; https://www.indiehackers.com/post/show-ih-i-built-datadog-for-business-metrics-after-missing-a-revenue-dip-across-12-sites-4c35a77c6d
- Digital twin noise: https://siliconangle.com/2025/10/15/ai-startup-viven-raises-35m-create-digital-twins-fill-absent-team-members/ ; https://siliconangle.com/2026/08/20/twin1-ai-raises-20m-to-put-an-ai-twin-behind-every-knowledge-worker/

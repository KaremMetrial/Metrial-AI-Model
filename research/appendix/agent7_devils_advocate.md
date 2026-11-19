# Agent 7: Devil's Advocate on the "Living Digital Model of Your Company" Idea
Date: 2026-11-19. Method: ~14 web searches (snippets and aggregator summaries, not primary-document deep reads). Evidence quality is flagged per claim. Anything I could not verify is marked UNVERIFIED. Where I cite my own inference rather than a source, I say so.

## 0. Verdict up front

The idea as pitched (a general, autonomous "company model" with monitoring, RCA, propagation, what-if simulation, and decision tracking, sold to SMB/mid-market with 3-day zero-data-team onboarding, built by a tiny team) is attacked from four sides at once:

1. The systems of record (Intuit, Xero, Shopify) are shipping the "tell me what's wrong" layer for free inside the product the SMB already pays for.
2. Foundation-model vendors now sell the horizontal version for a Claude/ChatGPT subscription. Anthropic launched a packaged SMB version in May 2026.
3. The data platforms (Microsoft, Databricks, Snowflake) own the "semantic model/ontology of the business" story for mid-market and up.
4. The previous generation of startups that did exactly this (Sisu, Anodot-style, Peak, Chartio, Periscope) ended in acqui-hires or acquisitions, not large independent outcomes.

The survivable core is narrow: a vertical, system-of-record-adjacent investigation product for a segment where the owner's own systems of record do not cover cross-system causality, sold with a human-in-the-loop service wrapper. The full-vision product is a poor bet for a capital-constrained founder.

## 1. What is genuinely strong (conceding fairly)

- Pain is real and persistent. CFO surveys show 96% of finance executives already using AI spend at least 10% of work time checking or fixing outputs (Datarails survey, vendor-sponsored, n=270): https://www.cpapracticeadvisor.com/2026/10/07/fact-checking-ai-is-taking-up-more-of-cfos-and-finance-teams-time/191230 . An evidence-and-confidence layer that reduces verification cost is a real wedge, not a gimmick.
- Spend intent exists: 53% of finance leaders plan to expand AI licences in the next 12 months, only 7% plan to cut (same Datarails source, same caveat).
- "Evidence + confidence + approval gate" matches what buyers say they need. 97% of mid-market US CFOs say human oversight remains critical (https://cfotech.news/story/us-cfos-back-ai-for-finance-but-insist-on-oversight). A product that is built around oversight, not around autonomy, fits the stated preference.
- Cross-system causality is a genuine gap in every incumbent. QuickBooks sees books and payments; Shopify sees the store; HubSpot sees pipeline. Nobody is incentivized to explain "margin fell because a supplier price change in the ops sheet hit the SKU mix that Shopify promotions shifted." That is a real structural opening, but see section 4: incumbents and model vendors are both moving at it.
- External-partnership/vendor-built AI succeeds more often than internal builds (MIT NANDA's buried finding, about 67% vs 33%, per critique summaries): https://www.govinfosecurity.com/most-ai-pilots-never-take-flight-a-29361 and critic summaries linked in section 3. That favors a buy-not-build product, if the product actually works.

## 2. The graveyard (evidence)

Verified items first, then gaps.

| Company | Concept | Outcome | Evidence and confidence |
|---|---|---|---|
| Sisu Data | "Decision intelligence engine": automated key-driver / "why did the metric change" analysis, from Stanford research. Raised $62M Series C. | Joined Snowflake October 2023. One secondary source says the standalone product was discontinued. | Funding: https://www.dbta.com/Editorial/News-Flashes/Sisu-Data-Secures-62-Million-in-Latest-Funding-Round-Introduces-New-Capabilities-to-Close-the-Decision-Gap-149257.aspx . Fate: https://yespress.io/sisu-data (single secondary source; treat as likely, not certain). Product description: https://bigdatawire.com/2020/05/18/sisu-seeks-to-answer-why . I found no founder post-mortem. |
| Peak AI | Decision intelligence for retail/manufacturing. About $115-118M raised (sources conflict). | Acquired by UiPath, March 2025. Price not disclosed in what I found. | https://itwire.com/it-industry-news/deals/uipath-acquires-peak-to-%E2%80%98launch-vertically-specialised-agents%E2%80%99-within-its-agentic-automation-platform ; funding: https://www.cbinsights.com/company/peak-1/financials . Note: Peak survived by going vertical (pricing/inventory), then got absorbed. Price unknown, so "cheap" is not proven. |
| Cloverpop | Decision journals/tracking for enterprises. | Raised a Series A; CB Insights total about $17.5M. Still small after more than a decade. I found no customer counts or adoption metrics. | https://www.newswire.com/news/cloverpop-decision-intelligence-platform-raises-series-a-financing-to-21901676 ; https://www.cbinsights.com/company/cloverpop . The absence of public adoption data is itself weak evidence. |
| Chartio | Self-serve BI for SMB. | Atlassian acquired it Feb 2021; standalone service ended March 2022. No price in sources. | https://devclass.com/2021/03/01/atlassian-buys-analytics-and-virtualisation-outfit-chartio . (One aggregator claims a 2026 end date; contradicts the better sources.) |
| Periscope Data | Cloud-data-team BI. | Acquired by Sisense, 2019. | https://www.trustradius.com/compare-products/atlassian-chartio-vs-sisense-for-cloud-data-teams-periscope-data |
| Anodot, Outlier.ai, Mode, Narrative Science, Tellius | Anomaly detection / auto-insight / BI narratives. | My searches returned nothing usable on prices or outcomes. UNVERIFIED in this research pass; I am not asserting outcomes. I recall (from training, not verified today) that Outlier.ai was acquired by Ancestry-adjacent/Looker-adjacent players and that Narrative Science was bought by Salesforce/Tableau; do not cite these without checking. |

Pattern I draw (inference, flagged): the product category "automatically tell me why the metric moved" has repeatedly been well-funded, technically credible (Sisu came out of a top Stanford lab), and still ended as a feature inside a bigger platform (Snowflake, UiPath, Atlassian, Sisense). The exits are not shown to be disasters, but none of the examples I could verify became an independent category-defining company. A tiny-team founder with limited capital does not have the cushion that a $62M Sisu had.

Hard-to-verify claim to retire: I could not find a single credible founder post-mortem for any of these. Absence of public lessons means the founder cannot learn cheaply from predecessors and must treat their failure reasons as unknown.

## 3. Why proactive-insight / auto-RCA products disappoint

Evidence quality here is weaker; most of what exists is vendor content in the observability and data-quality domain.

- Alert fatigue and false positives are the documented failure of static thresholds and of poorly designed monitors. Monte Carlo (data observability vendor) states that one of the biggest sources of alert fatigue is monitors based on incorrect assumptions and recommends routing by domain owner: https://www.montecarlodata.com/blog-alert-fatigue-monitoring-strategy . Anomalo advises sequencing checks to avoid false alarms from incomplete data: https://www.anomalo.com/blog/chapter-6-high-quality-notifications-bring-the-right-information-to-the-right-people-at-the-right-time/ . Resolve.io says false positives are a hidden risk requiring regular tuning reviews: https://resolve.io/blog/false-positive-alerts-a-hidden-risk-in-observability .
- Caveat on those sources: all are vendors selling the fix, and I found no independent measured false-positive rates for business-metric alerting. Claims like "cut noise 70%" are unsourced marketing.
- Business metrics are harder than infrastructure metrics: lower volume, high seasonality, few labeled incidents, and small samples. SMBs have a few hundred to a few thousand transactions a week, so statistical power for subpopulation attribution is thin. Key-driver analysis on small n produces spurious drivers. This is my inference from basic statistics, not a cited study; the way to prove it wrong is the cheap test in section 9.
- The "no action path" failure: an explanation without a lever produces a read-only dashboard. Sisu's own marketing framed the problem as "close the decision gap," which acknowledges insight alone was not sufficient (see DBTA link above).
- Gap: I found no practitioner post or study specifically on metric-level RCA false-positive rates. That is a research hole; do not treat this section as settled.

## 4. AI agents on enterprise data: failure modes

- Text-to-SQL on realistic schemas: the Spider 2.0 paper (real enterprise workflows) reported o1-preview at 5.7% on the full benchmark versus 73.0% on BIRD and 91.2% on Spider 1.0: https://www.arxiv.org/pdf/2411.07763 (summary via https://www.themoonlight.io/review/spider-20-evaluating-language-models-on-real-world-enterprise-text-to-sql-workflows ). That is a late-2024 baseline. Later aggregator snapshots (May 2026) show top Spider 2.0 entries in the 30s-50s depending on split, with metric definitions unclear: https://benchlm.ai/benchmarks/spider2Lite and https://benchmarklist.com/benchmarks/spider_2_0/ . Fair reading: huge improvement, still far below "trust without verification" on messy multi-table schemas, and these are benchmarks on warehouse data, not on SMB spreadsheets.
- Financial research tasks: Vals AI Finance Agent benchmark. Original 2025 paper: best model o3 at 46.8% (https://alphaxiv.org/abs/2508.00828). Current: v1.1 top about 64.4% (Claude Opus 4.7), and v2 top about 65.4% with Financial Modeling tasks topping out around 34.5% (https://vals.ai/benchmarks/finance_agent , https://www.vals.ai/benchmarks/finance-agent). FBBench (June 2026): best final-answer accuracy 44.3% (https://www.emergentmind.com/topics/fbbench). Caveat: these are SEC-filing research tasks, not "explain my company's data," and versions are not comparable. Direction is improvement; absolute level is still short of CFO-grade reliability for modeling and multi-step derivation, which is what "root cause with confidence" requires.
- MIT NANDA "GenAI Divide": headline of 95% of organizations getting zero return. Critiques are substantive: unclear methodology and sample (one critic says 52 organizations, another summary says 150 interviews plus a 350-employee survey plus 300 deployments; I could not reconcile), the 95% is about "no measurable P&L impact," not failure, and authors' affiliations. Sources: https://arnon.dk/mits-95-ai-failure-rate-is-wrong/ , https://www.bigdatawire.com/?p=89626 , https://www.govinfosecurity.com/most-ai-pilots-never-take-flight-a-29361 . My use of it: do not cite 95% as fact in a pitch; it will be attacked. What survives is the weaker claim that pilots stall before workflow integration.
- Gartner: more than 40% of agentic AI projects will be cancelled by end of 2027 due to cost, unclear value, and risk controls; also "agent washing," with only about 130 of thousands of vendors judged real. Based on a 3,412-person webinar poll (not a representative sample): https://www.thestar.com.my/tech/tech-news/2025/06/25/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says and https://w.media/over-40-percent-of-agentic-ai-projects-could-face-the-axe-by-end-of-2027-gartner/ . It is a forecast, with no follow-up verification found. It does support one real risk: buyers are being burned by "agent" claims and will discount a new entrant that uses the same words.
- Intuit's own admission: its finance-agent story is titled "Trust lost in buckets, earned back in spoonfuls": https://finanzen.net/nachricht/aktien/intuit-learned-to-build-ai-agents-for-finance-the-hard-way-trust-lost-in-buckets-earned-back-in-spoonfuls-15132490 . This is the best qualitative evidence that even the best-positioned incumbent, with perfect access to the data, found trust the binding constraint.

## 5. Incumbent threat (verified items, with confidence)

Question: is the SMB "tell me what's wrong with my business" feature being absorbed by systems of record? Answer: yes, partially, and fast, within each system's own data boundary.

- Intuit (QuickBooks): "Intuit Intelligence" with Accounting, Payments, Customer, Payroll, Sales Tax agents and a Business Tax agent in beta; Finance Agent for mid-market with KPI analysis and scenario planning/forecasting; Jan 2026 update added expanded anomaly detection and AI reconciliations; Aug 2026 added Intuit Intelligence Chat to Enterprise Suite and QBO Advanced, recommending next steps and acting only after user confirmation. Also a multi-year Anthropic partnership. Sources: https://quickbooks.intuit.com/r/product-update/intuit-intelligence-ai-business-tax-2026/ , https://www.cpapracticeadvisor.com/2026/08/27/intuit-introduces-new-capabilities-across-enterprise-suite-qbo-advanced/189236/ , https://www.accountingtoday.com/news/intuit-debuts-ai-agents-for-quickbooks . Several items are beta/coming soon; scale claims (60 models, 100+ skill agents) are company claims.
- Xero: JAX "financial superagent" (launched Sept 2025) says it proactively identifies and highlights issues in financial data; July 2026 added cash-flow/collections features and XeroForce, a no-code agent builder; claims "JAX Assure" reduces hallucinations (vendor claim). Reported Xero-Anthropic partnership and Microsoft 365 embedding are from secondary sources only (UNVERIFIED). Sources: https://www.xero.com/us/media-releases/xeros-ai-financial-superagent-jax-launches-powerful-new-features/ , https://cfotech.news/story/xero-expands-jax-ai-agent-to-boost-automation-for-small-firms .
- Shopify: Sidekick Pulse "monitors your store" and surfaces recommendations (blog claims up to 5 at a time); Spring '26 puts it at the center of Admin home as next best actions. Primary: https://www.shopify.com/news/winter-26-edition-merchant and https://www.shopify.com/news/spring-26-edition-merchant ; details from third-party guides, unverified against Shopify docs.
- Microsoft: Fabric IQ with an Ontology item (entities, relationships, rules, actions) announced at Ignite 2025 in preview; requires data in OneLake; Data Agent queries entities not raw schemas. A secondary blog claims GA at Build 2026 (UNVERIFIED). Sources: https://blog.fabric.microsoft.com/en-US/blog/from-data-platform-to-intelligence-platform-introducing-microsoft-fabric-iq/ , https://kanerika.com/blogs/microsoft-fabric-iq/ . This is the closest thing to an "enterprise digital twin of the business" from a mega-vendor, and it is aimed at exactly the "business ontology" part of the pitch, though at customers who already have a Fabric footprint.
- Databricks: Genie evolved into proactive, autonomous, "always on" and "Genie One" (AI coworker): https://www.techzine.eu/news/data-management/145764/databricks-genie-gets-a-makeover-autonomous-proactive-and-always-on/ and https://itdaily.com/news/cloud/databricks-genie-one/ . Snowflake: Snowflake Intelligence reportedly renamed CoWork (secondary, UNVERIFIED): https://siliconangle.com/2026/05/30/personal-agents-light-fuse-snowflake-databricks-move-ai-stack/ . These target customers already on a lakehouse; not zero-data-team SMBs, but they squeeze the mid-market upper edge and make "company model" a platform checkbox.
- SAP (Joule / Business Data Cloud), Oracle, NetSuite, Salesforce: my searches returned nothing verifiable this pass. UNVERIFIED; do not assert. A follow-up check is needed before any claim about the mid-market ERP layer.

Net: for an SMB on QuickBooks, Xero, or Shopify, a free in-product agent already answers a first-order version of "what is wrong," with the system-of-record's native data access, auth, billing relationship, and distribution. A startup's differentiation can only be the cross-system and cross-source causality that no single record system sees.

## 6. Foundation-model threat

Verified (Anthropic's own announcement plus coverage): Claude for Small Business launched 2026-05-13 as a Cowork toggle, bundling about 15 pre-built workflows and connectors (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365; coverage differs on Slack/Stripe/Square). Workflows include reconciling QuickBooks cash against PayPal settlements, 30-day forecasts, ranking overdue items, and queuing reminders for approval; the user approves before anything sends or pays. No extra charge beyond Claude licences and existing partner tools. Sources: https://www.anthropic.com/news/claude-for-small-business , https://qz.com/anthropic-claude-small-business-quickbooks-paypal-051326 , https://the-decoder.com/anthropic-launches-claude-for-small-business-to-embed-ai-into-the-tools-you-forgot-you-pay-for/ . Scheduled tasks: Anthropic support documents recurring and on-demand tasks that work with connectors and saved files: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork . Third-party posts claim cloud-run schedules and Stripe revenue reports as common tasks, and a Cowork/chat merge in Sept 2026 (single-source, UNVERIFIED).

Can a customer approximate the idea for $20-200 a month? Mostly yes for: monitoring-by-schedule, morning briefings, anomaly summaries, "why did revenue dip," cash forecasts, and reconciliation across the covered connectors. Gaps that remain (my assessment, not a cited finding): persistent entity-resolved cross-system model, continuous event detection with state (a scheduled prompt re-derives rather than remembers), audit trail of investigations, calibrated confidence, and sources without connectors (spreadsheets scattered on drives, bespoke ops tools). Those gaps are exactly where the foundation vendors are least likely to build first, and exactly the hardest to productize. Also note Intuit and Xero both partner with Anthropic, so the incumbent and the foundation-model layers are converging on the same customer.

Implication: a thin "chat over connectors with scheduling" layer has no moat and an effective price ceiling near zero. Any defensible value must come from persistent state, entity resolution, verification, and vertical ontology that the horizontal subscription does not supply.

## 7. SMB sales and implementation reality

- Churn: sources disagree widely, which is itself the signal. Under-$10K ACV SMB logo churn is reported at 30-50% annually (3-5% monthly) in some aggregator content, 10-14% median annual in a ChartMogul-based figure for $1-10K ACV, and 40.3% in an Optifai sample of 939 (N and methods unaudited). Sources: https://crv.com/content/saas-churn-rate , https://userjot.com/blog/saas-churn-rate-benchmarks , https://visionary-marketing.co.uk/blog/saas-churn-benchmarks-2026 . All are secondary/vendor; none broke out sub-$100/month ACV cleanly.
- Data messiness is where "3-day zero-data-team onboarding" breaks. SMB data lives in spreadsheets, inconsistent product names, hand-keyed ops, and personal tools. The text-to-SQL and finance-agent evidence above is on cleaner data than that. Every "automatic model" claim has to survive entity resolution across QuickBooks customer names, Shopify SKUs, and a manager's spreadsheet. This is the classic move where the "SaaS" becomes data-cleaning labor. That is an inference from the evidence (no cited study of SMB onboarding hours); the test in section 9 measures it directly.
- Consulting-in-disguise risk: high. Sisu and Peak both ended up with heavy enterprise motion; Peak is vertical (retail/manufacturing). The pattern that survived (Peak) was narrow and decision-specific (pricing, inventory), not "model of your company."
- Unit economics: a tiny team can afford only self-serve or low-touch sales. Low-touch SMB plus 30%+ churn plus a free in-product competitor plus $20-200 model subscriptions implies a ceiling on price. At that ARPA, even a modest support burden destroys margins.

## 8. Trust, liability, and decision-tracking evidence

- Trust: only about 14% of finance leaders completely trust AI to deliver accurate accounting data, 41% mostly (Journal of Accountancy summary): https://www.journalofaccountancy.com/news/2026/feb/agentic-ai-is-handling-more-finance-work-but-can-cfos-trust-it/ . Datarails: 5% trust AI for board-ready reports unreviewed, 4% for month-end close. 77% of CFOs cite security/privacy as the biggest AI trust gap (CFO Pulse summary, vendor-adjacent): https://www.pulse.bot/cfo-pulse/news/77-of-global-cfos-cite-security-and-privacy-risks-as-the-biggest-ai-trust-gap-806ec694-db95-4f35-a98e-fbda5b3b45d4/ . Caveat: small samples (60-270) and vendor sponsors.
- Implication: an owner will read an explanation but will not act on it without checking. That makes the product a "who investigates for me" labor-saver, and its measurable value is hours saved, not decisions improved. That is harder to price than decisions improved, but easier to prove.
- Liability: I found no case law or insurer guidance specific to AI-generated root-cause explanations. UNVERIFIED. The practical risk is reputational: one confidently wrong explanation that causes a bad pricing or hiring decision. Intuit's "trust lost in buckets" suggests this plays out in practice.
- Data-sharing resistance: connecting payroll, bank, and CRM data to a tiny unknown vendor means a SOC 2 / security review burden that Intuit, Xero, and Anthropic already have. This is a cost the founder must pay before first sales and which the incumbents amortize.
- Decision tracking/outcome learning: Cloverpop is the main specialist and, after a decade-plus, has about $17.5M total raised and no public adoption metrics that I could find (https://www.cbinsights.com/company/cloverpop). I found no study showing sustained use of decision journals by SMBs. My assessment: decision logging is a feature people agree with and do not do, because it adds work at the moment of decision. Treat the "Investigation Queue as decision tracker" as an unproven retention hypothesis, not a moat.

## 9. Pre-mortem: ten most likely failure reasons, ranked

Rank by probability times severity (my estimates, not measured). Each has a falsifier.

1. **No defensible gap vs. free in-product agents and the $20-200 subscription (very high probability, fatal).** Falsifier: 10 target SMBs, each already using QuickBooks/Xero/Shopify AI plus Claude, still pay for and use the product weekly for 8 weeks, and say they would be unhappy to lose it; the product's findings are not reproducible by their existing tools in a blind comparison.
2. **Onboarding is really data cleaning; margin collapses (very high, severe).** Falsifier: median onboarding under 2 human-hours across 15 real customers with messy data, with at least 80% of entities correctly resolved without manual fix.
3. **Spurious/unfounded root causes erode trust (high, severe).** Falsifier: on 30 historical metric movements with known causes (owner-confirmed), the system's top explanation is correct at least about 70% of the time, and confidence scores are calibrated (stated 80% is right around 80%).
4. **Alert fatigue: users mute it within a month (high, severe).** Falsifier: at least 60% of surfaced investigations are marked "useful" and weekly open rate stays above 50% after week 6.
5. **Insight without an action path, so no budget attaches (high, medium-severe).** Falsifier: at least a third of investigations lead to a logged action within 7 days; at least 3 customers can name a dollar outcome.
6. **SMB churn plus low ACV makes CAC payback impossible for a tiny team (high, severe).** Falsifier: 6-month logo retention above 85% in the first cohort at an ACV that covers support; or a channel (accountants, bookkeepers) delivering customers at near-zero CAC.
7. **Incumbents or Anthropic ship the cross-system layer directly (medium-high, fatal).** Intuit has Anthropic as a partner and an Aug 2026 chat that suggests next steps; Fabric IQ is a business-ontology product; Claude for Small Business already reconciles QuickBooks and PayPal. Falsifier: after another two quarters, none of them offers persistent cross-source investigation across the customer's non-native sources, and customers confirm they hit that wall.
8. **Security/trust barrier to connecting sensitive data to an unknown vendor (medium-high, moderate-severe).** Falsifier: at least 8 of 10 prospects grant read access to payroll/banking/accounting data with no more than a lightweight review.
9. **"What-if simulation" and "propagation" are unreliable or unused (medium-high, moderate).** A causal model for a company is under-identified at SMB data volumes; users run it once. Falsifier: simulations are rerun by at least half of active users monthly, and forecasts beat a naive baseline in backtests.
10. **Decision-tracking never gets used (medium-high, low-moderate).** Falsifier: at least 40% of investigations get an outcome recorded without being nagged; if not, drop the feature from the core pitch.

Honorable mention: the founder's capital runway. A model-cost and integration-maintenance burden (connector APIs change; per-customer LLM inference cost) hits a tiny team before product-market fit signals arrive.

### Smallest, cheapest test that could disprove the whole idea

A concierge "investigation memo" test, about 3-4 weeks, near-zero engineering:

1. Recruit 10-15 target SMBs (pick one vertical, one stack, e.g., Shopify + QuickBooks + one ads platform).
2. Get read-only exports or connector access. Time every hour spent cleaning data (this measures reason 2 directly).
3. Each week, produce a human-assisted memo using off-the-shelf Claude with connectors (the $20-200 competitor itself): 1-3 investigated anomalies, each with evidence and confidence.
4. In parallel, give each customer their own Claude-for-Small-Business or in-product Intuit/Xero/Shopify output on the same questions, and ask the owner to blind-rank the two.
5. Charge $200-500/month from week 3.

Disproof criteria: fewer than 30% pay; or owners rate the memo no better than the incumbent/Claude output; or data-cleaning hours per customer exceed what a $200-500 price can bear; or top-explanation accuracy against owner-confirmed causes is under about 60%. Any single failure kills the "automatic, 3-day, zero-data-team" thesis, and the memo output doubles as a dataset for steps that survive.

## 10. Narrower variants that survive the attacks

Ranked by my confidence, all flagged as judgment, not evidence:

A. **Vertical, cross-system margin/cash "why" for one niche stack** (e.g., DTC e-commerce brands on Shopify + QuickBooks/Xero + ads, or restaurant groups). Why it survives: Shopify and Intuit each see only half the causal chain; vertical ontology (SKU margin, discounting, returns, ad spend) is something horizontal agents lack; Peak survived longest by going vertical (retail/manufacturing). Risk: Shopify Pulse and the Anthropic SMB pack both move toward it.

B. **Sold through accountants/bookkeepers/fractional CFOs as an "investigation copilot" (channel, not direct SMB).** Why: the accountant is the trust holder and the human-in-the-loop, solving trust, onboarding labor, and churn (one relationship carries many SMB clients). Intuit and Xero both court accountants, so competition is real, but the accountant channel is multi-system and tool-agnostic. This is the variant that most directly answers "consulting in disguise": make the consultant the customer.

C. **Investigation audit trail / evidence layer for outputs from other AI tools** (verification-cost reduction). Why: 96% of finance leaders already spend 10%+ of time fact-checking AI (Datarails). Narrower and complementary to Claude, Intuit, and Xero rather than competing. Risk: those vendors will build their own citations and evidence views.

D. **Monitor-and-explain for one metric family with a pre-wired action** (e.g., collections/cash-in or promo-margin leak), with the action executed under approval. Why: matches Intuit's and Anthropic's approval-gated pattern, gives an outcome you can price, and avoids the open-ended "company model."

What does not survive: the general-purpose autonomous company twin for SMBs sold direct at self-serve prices, with decision-tracking as the retention story.

## 11. Evidence gaps to close before committing

- Primary-source checks needed: Anthropic's Claude for Small Business page and current Cowork scheduled-task limits; Microsoft Fabric IQ GA status; Snowflake Intelligence/CoWork status; SAP Joule/Business Data Cloud, Oracle, NetSuite, Salesforce 2026 launches.
- Outcomes and prices for Anodot, Outlier, Mode, Tellius, Narrative Science (not retrieved).
- Any founder post-mortem of Sisu (none found); consider interviewing former Sisu/Chartio staff.
- An independent measurement of metric-RCA precision at SMB data volumes (none found); the section 9 test is how to get it.
- SMB churn for products under $100/month ACV (sources conflict and none isolate it).

## Source index (main)

- Sisu: https://www.dbta.com/Editorial/News-Flashes/Sisu-Data-Secures-62-Million-in-Latest-Funding-Round-Introduces-New-Capabilities-to-Close-the-Decision-Gap-149257.aspx ; https://yespress.io/sisu-data ; https://bigdatawire.com/2020/05/18/sisu-seeks-to-answer-why
- Peak/UiPath: https://itwire.com/it-industry-news/deals/uipath-acquires-peak-to-%E2%80%98launch-vertically-specialised-agents%E2%80%99-within-its-agentic-automation-platform
- Cloverpop: https://www.cbinsights.com/company/cloverpop
- Chartio: https://devclass.com/2021/03/01/atlassian-buys-analytics-and-virtualisation-outfit-chartio
- Alert fatigue: https://www.montecarlodata.com/blog-alert-fatigue-monitoring-strategy ; https://resolve.io/blog/false-positive-alerts-a-hidden-risk-in-observability
- Spider 2.0: https://www.arxiv.org/pdf/2411.07763
- Finance Agent benchmark: https://vals.ai/benchmarks/finance_agent ; https://alphaxiv.org/abs/2508.00828 ; https://www.emergentmind.com/topics/fbbench
- MIT NANDA critiques: https://arnon.dk/mits-95-ai-failure-rate-is-wrong/ ; https://www.govinfosecurity.com/most-ai-pilots-never-take-flight-a-29361
- Gartner: https://www.thestar.com.my/tech/tech-news/2025/06/25/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says
- Intuit: https://quickbooks.intuit.com/r/product-update/intuit-intelligence-ai-business-tax-2026/ ; https://www.cpapracticeadvisor.com/2026/08/27/intuit-introduces-new-capabilities-across-enterprise-suite-qbo-advanced/189236/ ; https://finanzen.net/nachricht/aktien/intuit-learned-to-build-ai-agents-for-finance-the-hard-way-trust-lost-in-buckets-earned-back-in-spoonfuls-15132490
- Xero: https://www.xero.com/us/media-releases/xeros-ai-financial-superagent-jax-launches-powerful-new-features/
- Shopify: https://www.shopify.com/news/spring-26-edition-merchant
- Microsoft Fabric IQ: https://blog.fabric.microsoft.com/en-US/blog/from-data-platform-to-intelligence-platform-introducing-microsoft-fabric-iq/
- Databricks Genie: https://www.techzine.eu/news/data-management/145764/databricks-genie-gets-a-makeover-autonomous-proactive-and-always-on/
- Claude for Small Business: https://www.anthropic.com/news/claude-for-small-business ; https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
- CFO trust: https://www.cpapracticeadvisor.com/2026/10/07/fact-checking-ai-is-taking-up-more-of-cfos-and-finance-teams-time/191230 ; https://www.journalofaccountancy.com/news/2026/feb/agentic-ai-is-handling-more-finance-work-but-can-cfos-trust-it/
- SMB churn: https://crv.com/content/saas-churn-rate ; https://userjot.com/blog/saas-churn-rate-benchmarks

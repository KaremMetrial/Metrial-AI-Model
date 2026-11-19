# Agent 1A: Competitive Intelligence (Enterprise AI + Decision Intelligence)

Date of research: 2026-11-19. Method caveat: WebSearch only. WebFetch was blocked for most hosts (DNS failure for glean.com, forrester.com, itbrief.co.uk), so I could NOT read primary vendor docs. Search results are summaries. Therefore very few claims below reach VERIFIED; most are ADVERTISED (vendor press/marketing) or secondary-source. Where sources conflict, I say so. Prices are almost all third-party estimates.

Label key: VERIFIED = official docs/independent review seen in results; ADVERTISED = vendor marketing/press only; INFERRED = my deduction; UNKNOWN = not found.

---

## 0. Bottom line (read this first)

1. Nobody I found sells the full thing you described (continuous company model + material-change monitoring + autonomous causal investigation with confidence + impact propagation + decision/outcome tracking) to SMB with zero data-team onboarding. The closest are enterprise decision-intelligence vendors (Aera, Tellius, Palantir) which are sales-led, expensive and implementation-heavy, and enterprise-AI search vendors (Glean, Dust, Onyx) which are knowledge/agent platforms, not metric-monitoring systems.
2. Individual pieces ARE commoditized or being commoditized by big platforms: NL-to-data Q&A, connectors/RAG over SaaS, agent builders, MCP connectivity, semantic-layer-as-AI-context (Microsoft Fabric IQ, ServiceNow-Pyramid), anomaly alerts/KPI monitoring (Tableau Pulse, Tellius, etc.).
3. The category is consolidating fast: Peak to UiPath (Mar 2025), Sana to Workday (closed 2025-11-04), Pyramid Analytics to ServiceNow (closed 2026-03-10). Independents in the "context layer" niche are tiny (Hyperspell) or developer-tool shaped (PromptQL, Onyx).
4. The strongest competitor threat to an SMB entrant is not a startup; it is Microsoft (Copilot Business at ~$21/user + Fabric IQ) and, to a lesser degree, Glean moving down-market.

---

## 1. Profiles: Enterprise AI

### Glean
- Positioning: "Work AI platform": enterprise search + Assistant + Agents over an enterprise graph. Target: large enterprise (hundreds to tens of thousands of seats).
- Status: ~$300M ARR claimed by Glean (press release, ~May 2026) [glean.com/press/glean-surpasses-300m-arr...]. $150M Series F at $7.2B (Jun 2025) per secondary coverage; a claim of a $12B round (Apr 2026) is uncorroborated (callsphere.ai post) - treat as UNKNOWN. ADVERTISED/secondary.
- Integrations: 100+ connectors (ADVERTISED; count not re-verified here).
- AI capabilities: Assistant, Agents (launched Feb 2025; no-code builder; reported "250M+ actions", secondary source), Feb 17 2026 next-gen "proactive coworker" Assistant (ADVERTISED; coverage at theaieconomy.substack.com and briefglance.com). Glean blogs describe "proactive AI" that "continuously observes business signals" and dashboards refreshing on a schedule (ADVERTISED; glean.com/blog/intelligent-secure-proactive-ai, undated in my results).
- Context/memory: Enterprise Graph of people/content/activity (ADVERTISED). This is a graph of work artifacts and permissions, NOT of business metrics/causal structure (INFERRED).
- Monitoring/RCA/simulation/outcome tracking: no evidence of metric anomaly detection, causal RCA, simulation, or decision-outcome tracking. UNKNOWN/not found.
- Security: permission-aware retrieval is core (ADVERTISED; widely stated).
- Pricing: not public; glean.com/pricing redirects to sales. Third-party: ~$35-50/user/mo, ~100-seat minimums; 500-person company $250-350K/yr all-in (secondary; unverified).
- Implementation: 60-90 days to 3-6 months (secondary review sites; vendor-adjacent, e.g. slite.com, workativ.com).
- Complaints (G2 4.7/5, ~162 reviews per G2 snippet; g2.com/products/glean-technologies-glean/reviews): search can be broad/hard to pinpoint, filtering, slow on old docs; Capterra value-for-money 3.0 on 2 reviews. Quality depends on source data hygiene. No Reddit threads surfaced.
- What customers still do manually (INFERRED): everything quantitative. Glean tells you where information lives and drafts/acts on documents; it does not tell you why revenue fell.

### Microsoft (M365 Copilot, Power BI Copilot, Fabric Data Agents, Fabric IQ)
- Positioning: horizontal assistant + data platform. Target: everyone, incl. SMB.
- Pricing (best-sourced item in this report): Copilot Business $21/user/mo from the 2026-07-01 pricing update per Microsoft Tech Community post (techcommunity.microsoft.com ...ba-p/4502628), requires eligible M365 Business plan, ~300 user cap; promo $18 disputed (alphabold, softwareone, collab365 posts). M365 Copilot enterprise $30/user. Power BI Copilot needs paid Fabric capacity (F2+, older doc said F64+/P1+) AND Pro/PPU licenses; an M365 Copilot license does not enable it (learn.microsoft.com/power-bi/create-reports/copilot-enable-power-bi; conflicting older Q&A). VERIFIED-ish (Microsoft pages surfaced in results, details via secondary summaries).
- Fabric IQ: "business-context layer over OneLake" combining ontologies, Power BI semantic models, a graph, and data/operations agents; semantic model GA, ontology reported still in preview; MCP access (read-only DAX against semantic models) (atlan.com/know/microsoft-fabric/what-is-fabric-iq/, futurumgroup.com, kanerika.com, letsdatascience.com; Forrester blog "Microsoft FabCon 2026: Enterprise AI Needs A Governed Context Layer" exists but I could not read it). Sources disagree on GA vs preview: label PARTIAL/ADVERTISED.
- Monitoring/alerts: Fabric Real-Time Intelligence/Activator exist (INFERRED from my knowledge; not confirmed this session). Autonomous causal RCA: UNKNOWN/not found. Power BI "key influencers"/"explain the increase" are older features (my prior knowledge; not re-verified).
- Complaints: Gartner 2025 survey: ROI "quite challenging"; nearly half of piloters said "some value, shows promise"; barriers content sprawl/oversharing/governance (techpartner.news Gartner summary). 30M paid seats reported FY26 Q4 but ~3% of M365 base (single blog citing Microsoft; unverified). Gartner 2026 report "Assessing Impact and Value in 2026" (2026-06-09) exists, content not read.
- Implementation for SMB: Copilot is quick; the Fabric/semantic-model path needs someone to build and govern semantic models (INFERRED from "start from existing Power BI model" claims). A no-data-team SMB cannot easily do this.
- Strategic risk: Microsoft is explicitly building the "governed context layer / ontology" idea you are describing, bundled with the tool SMBs already pay for.

### Dust
- Positioning: no-code platform to build custom AI agents/assistants over company data, multiplayer. Paris. Target: tech-forward SMB/mid-market (scale-ups), also enterprise.
- Funding: "$40M Series B co-led by Sequoia, May 2026" reported by one review site (subscribed.fyi/aggregators) - UNVERIFIED.
- Integrations: 20+ connectors (Slack, Notion, GitHub, Drive...) per Dust pricing page as of Jul 2026, plus any tool via MCP (as relayed by search summary); other aggregators say 5 or 61+ (conflict).
- Capabilities: agents in Slack, Chrome extension, cross-source query (G2 reviewer). Scheduled/triggered automation: PARTIAL (aggregators mention event notifications; ADVERTISED). Metric monitoring/RCA/simulation: not found.
- Pricing: ~$29-30/user/mo Pro; Max ~$150/user/mo with 40,000 credits; programmatic usage ~$0.01/credit; Enterprise custom (costbench.com, usagepricing.com, withorb.com: aggregators; free tier disputed). Credit-metered seats introduced Jun 2026 (usagepricing.com).
- Complaints: missing connectors for some sources; complex source setup sometimes needs technical help (G2 snippet). 
- Manual leftover: someone must design agents, choose data, write prompts. It is a toolkit, not a modeled company.

### Sana (Workday)
- Acquired by Workday for ~$1.1B; announced 2025-09-16, completed 2025-11-04 (newsroom.workday.com/2025-11-04-Workday-Completes-Acquisition-of-Sana). VERIFIED (official release).
- Now being folded into Workday as the "front door for work" (new interface expected 2026 per Reuters-sourced brief). Sana Agents (no-code agents) and Sana Learn continue (ADVERTISED). Not independently available as a neutral SMB product going forward (INFERRED). Implication: one fewer independent; but also demonstrates exit values for "AI knowledge layer" companies.

### Onyx (formerly Danswer)
- Open-source (MIT core) enterprise search/chat/agents; Business $20/user/mo annual; Enterprise contact-sales (SSO, RBAC, permission sync gated) (onyx.app/pricing per search summary; aggregators vary $16-25). $10M raise reported Mar 2025 (secondary). YC W24 per aggregators (unconfirmed primary).
- 40+ connectors (ADVERTISED). No metric monitoring/RCA found. Strength: self-host, cost. Weakness: governance features paywalled; self-host TCO real (gosearch.ai post, competitor-authored).

### Hyperspell
- YC F25; "memory & context layer for AI agents"; connects Slack/Gmail/Notion/Drive; SDK for developers (ycombinator.com/companies/hyperspell). Funding unclear ($0.5M-$5.7M across trackers, conflicting). 3-9 staff.
- Developer infrastructure, not a business application. Relevance: shows the "context/memory" primitive is becoming a component (ADVERTISED). No evidence of business-model/causal reasoning. Tiny; acquisition or irrelevance risk.

### PromptQL (Hasura)
- "Agentic semantic layer"/data agent: builds a semantic graph across sources (Snowflake, MongoDB, Salesforce...); LLM plans, PromptQL runtime executes; MCP server (hasura.io/pricing/promptql; promptql.hasura.io/docs). ADVERTISED/documented.
- Pricing: usage-based, token costs billed separately; third-party says "no seat pricing"; billing terms last updated 2025-03-13 (hasura.io/promptql-billing-terms). Reviews are mostly eesel.ai/makerstack (vendor-adjacent).
- Target: technical teams with data engineers (INFERRED: requires configuring data connectors/semantic model). No proactive monitoring/RCA claims found.

---

## 2. Profiles: Decision Intelligence / Decisioning

### Gartner context
Gartner published its first Magic Quadrant for Decision Intelligence Platforms on 2026-01-26. Leaders per vendor press releases: IBM, FICO, Quantexa, SAS, Aera (fintechnews.ch; vendor press). Pega reportedly Challenger; Sapiens and Faculty Visionaries (briefglance.com; relational.ai page). Full report paywalled; I did not verify placements for Tellius, Peak, Palantir, o9, Pyramid. Note the MQ's definition of DI is heavily "decisioning engines + agents", i.e. enterprise ops (credit, fraud, supply chain).

### Palantir (Foundry / AIP)
- Positioning: ontology-based operational platform with AI agents that read/write back to systems. Target: large enterprise and government; has bootcamp-led sales.
- Capabilities: Ontology (objects/actions/links), Automate, AIP Logic, monitoring on functions/actions via Data Health, alerts to Foundry/PagerDuty/Slack (palantir.com/docs/foundry/announcements/2025-10/) VERIFIED (official docs). Logging of every action by humans or agents; human-in-the-loop and branching/scenario staging described in Palantir architecture docs (palantir.com/docs/foundry/architecture-center/aip-architecture) VERIFIED (docs surfaced via search). Simulation: scenarios staged before write-back VERIFIED (docs per search). Approval for Automate runs: not confirmed.
- Pricing: not public. Estimates: low-mid six figures/yr for one use case (bdemerson.com); $800K-$2.5M/yr mid-market (redresscompliance.com) - consultancies; unverified. Bootcamp: ~5 days onsite proof-of-value (Rackspace description via search).
- Implementation: needs forward-deployed engineers or in-house builders; production timeline not found. Ontology must be built and maintained ("whether the ontology still holds months later" btw.media).
- Complaints: cost, lock-in/exit cost (beri.net), engineering heavy. No G2 data pulled.
- Not an SMB product (INFERRED from price). Autonomous causal RCA of "why did metric X move": not a packaged feature found; you would build it.

### Aera Technology (Decision Cloud)
- Positioning: "agentic decision intelligence" for supply chain/enterprise decisions; Gartner MQ Leader (Jan 2026). Customers: Kerry Group, large CPG/manufacturing (ADVERTISED).
- Capabilities: May 2026 agentic reasoning; Oct 2026 (AeraHUB 26 NYC) six announcements: Skill Building, Decision Ledger, Policy Studio, Agent Interoperability (Copilot Studio, A2A, MCP), Dynamic UX, Command Center (itbrief.co.uk/story/aera-unveils-six-tools-to-automate-enterprise-decisions; techintelpro.com). Decision Ledger records decisions, policies evaluated, outcomes (ADVERTISED). Policy Studio: rules drafted from policy docs, human-approved, observer mode first, can block/require approval/warn; example: $62K air freight expedite waits for director approval (ADVERTISED, CTO interview via letsdatascience.com).
- Why it matters: this is the closest existing feature set to your "track decisions and outcomes" + human approval. But it is bounded to ERP/supply-chain-style operational decisions with integrated enterprise systems.
- Pricing: not found. Implementation: Gartner Peer Insights ~4.5-4.6 (32-40 ratings); reviewer says success needs data quality, process alignment, change management; ease-of-use "overwhelming to new users" (gartner.com/reviews/product/aera-decision-cloud; Dec 2025 review). Cost complaints not found.
- Not an SMB product (INFERRED: enterprise sales, integration needs).

### Tellius
- Positioning: agentic analytics / "AI analyst" (Kaiya; Deep Insights; Agent Mode) with automated driver/root-cause analysis on warehouse data; sells to mid-large enterprises, CPG/pharma/finance (tellius.com).
- Claims: RCA "days to seconds"; PepsiCo 12x faster RCA (vendor); Dresner #1 agentic report Nov 2025 (vendor-reported); Gartner Visionary (vendor-reported, not verified) - ADVERTISED. Independent review: surfaces drivers/anomalies but narratives need analyst validation; noisy-metric tuning takes iteration (rfp.wiki review) PARTIAL-VERIFIED (independent but thin).
- Semantic: business views (BV) layer, SmartSelect (release 5.3 notes). Credits/usage limits enforced (patch 6.3.0.1) - consumption-metered.
- Pricing: not public. G2 (22-26 reviews, 4.3-4.4): "expensive", "medium or large scale organization", costly training, integration/support issues; roadmap perceived behind ThoughtSpot. Aggregator price figures ($25/user, $495/mo) conflict - disregard.
- Needs: cloud warehouse + modeled data. Requires data team to set up (INFERRED from product shape).
- This is the most direct functional competitor on "autonomous investigation". Gap versus your idea: it analyzes ONE company's warehouse data in a BI frame; no company-wide model of decisions/people/ops across tools, and no SMB zero-data-team onboarding (INFERRED).

### Quantexa
- Entity resolution + knowledge graph + decisioning; Gartner Leader; banks (ABN AMRO, Standard Chartered, Morgan Stanley), financial crime/KYC/AML (quantexa.com). Platform scale claim 60bn+ records (vendor). Pricing/implementation: not found; enterprise by nature. Irrelevant for SMB; relevant only as proof that "graph + entity resolution" is a defensible enterprise category.

### FICO, SAS, IBM, Pega
- Rules/ML decisioning engines (credit, risk, fraud, customer decisioning). FICO, SAS, IBM named Leaders in 2026 MQ (vendor releases: marketplace.fico.com, sas.com press release Feb 2026, ibm.com). Pega reportedly Challenger. Not researched deeper: they require model/rule authoring by specialists, regulated-industry focus (INFERRED). Capability on SMB, monitoring-of-business-metrics, causal RCA: not found.

### Peak (UiPath)
- Acquired by UiPath; announced 2025-03-12 (uipath.com/newsroom/uipath-acquires-peak...; techcrunch.com 2025-03-13). Reported $38.1M consideration per UiPath filing (single secondary source; unverified). Products: Agentic Inventory Management, Agentic Merchandising, Agentic Commercial Pricing (Peak Dec 2025 review); "Negotiation Agent" still "coming soon". Vertical (retail/manufacturing). Peak is no longer independent. Cautionary data point: a well-funded UK DI startup ($75M raised 2021) exited for roughly $38M (INFERRED comparison; flag as unverified).

### o9 Solutions
- Supply-chain/enterprise planning with "Enterprise Knowledge Graph" "digital twin"; agents GA Jun 2025. Estimated $200K-$1M+/yr; not for mid-market (softabase.com, erpresearch.com; estimates). Strong example of a knowledge-graph/digital-twin model for planning at large enterprise.

### Pyramid Analytics (ServiceNow)
- ServiceNow announced acquisition 2026-02-12, closed 2026-03-10 (servicenow.com/blogs/2026/pyramid-analytics-expanding-data-driven-ai) VERIFIED. Plan: analytics + semantic layer for ServiceNow Workflow Data Fabric. Pricing conflicting ($36K/yr start vs free tier; both aggregators). Standalone product path uncertain.

### Cloverpop
- Decision-logging/"decision intelligence" workflow platform (human-first, decision templates, outcome tracking) (cloverpop.com). No public pricing (G2 says none provided). Ownership status confusing: PitchBook lists 2021 deal; CB Insights stage "acquired" unreliable. I could not confirm current status: UNKNOWN. Most relevant to your "decisions and outcomes" pillar; appears to be a manual/workflow tool rather than data-driven (INFERRED; ADVERTISED).

---

## 3. Capability matrix

Cell values: VERIFIED / ADVERTISED / PARTIAL / UNKNOWN. "NO*" = no evidence found; treat as UNKNOWN unless stated. Few cells are VERIFIED because primary docs could not be fetched.

| Competitor | Business context | Data connectivity | Semantic model | Knowledge graph | Monitoring | Anomaly detection | RCA | Proactive investigations | Decision intelligence | Simulation | Outcome learning | Agents | Automation | Onboarding ease | Target market | Pricing | Implementation complexity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Glean | ADVERTISED (work graph) | ADVERTISED (100+) | PARTIAL | ADVERTISED (enterprise graph, docs) | PARTIAL (proactive, ADVERTISED) | UNKNOWN | UNKNOWN | ADVERTISED (proactive AI) | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | ADVERTISED | Moderate (60-90d, secondary) | Enterprise | Not public ($35-50/user est.) | Medium |
| Microsoft Copilot + Fabric/Power BI | PARTIAL (Fabric IQ) | VERIFIED (M365/Fabric) | VERIFIED (Power BI semantic models) | PARTIAL (ontology preview) | PARTIAL | PARTIAL (INFERRED from RTI) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | VERIFIED (data agents) | PARTIAL | Easy for M365, hard for Fabric model | All sizes | VERIFIED ($21-30/user; + F2 capacity) | Low (Copilot) to High (Fabric) |
| Dust | PARTIAL | ADVERTISED (20+, MCP) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | PARTIAL | Easy-moderate | SMB/mid/ent | ~$29-30/user (aggregators) | Low-Med |
| Sana (Workday) | ADVERTISED | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | PARTIAL | Folded into Workday | Enterprise | UNKNOWN | Medium |
| Onyx | PARTIAL | ADVERTISED (40+) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | PARTIAL | Easy (cloud) / dev (self-host) | SMB-ent, dev-led | VERIFIED-ish ($20/user) | Low-Med |
| Hyperspell | ADVERTISED (memory) | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PARTIAL (memory) | Infra for agents | UNKNOWN | Dev SDK | Developers | UNKNOWN | Low (dev) |
| PromptQL | PARTIAL | ADVERTISED | ADVERTISED (agentic semantic layer) | ADVERTISED (semantic graph) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | PARTIAL | Dev-led | Data/eng teams | Usage-based (unclear) | Medium |
| Palantir AIP/Foundry | VERIFIED (Ontology) | VERIFIED | VERIFIED (Ontology) | VERIFIED-ish (ontology as graph) | VERIFIED (monitoring/alerts) | PARTIAL (build) | PARTIAL (build) | PARTIAL (Automate, unverified) | VERIFIED (platform) | VERIFIED (scenarios) | PARTIAL (build) | VERIFIED | VERIFIED (logged, human-in-loop) | Hard (bootcamp+FDE) | Large ent/gov | Not public ($0.1-2.5M/yr est.) | Very high |
| Aera | ADVERTISED | ADVERTISED (ERP etc.) | ADVERTISED | UNKNOWN | ADVERTISED | ADVERTISED | PARTIAL | ADVERTISED | ADVERTISED (MQ Leader) | UNKNOWN | ADVERTISED (Decision Ledger) | ADVERTISED | ADVERTISED (approval policies) | Hard | Large ent (supply chain) | UNKNOWN | High |
| Tellius | PARTIAL | ADVERTISED (warehouses) | ADVERTISED (business views) | UNKNOWN | ADVERTISED | PARTIAL (independent) | PARTIAL (independent, ADVERTISED depth) | ADVERTISED (agent mode) | PARTIAL | UNKNOWN | UNKNOWN | ADVERTISED | PARTIAL | Moderate-hard | Mid-large ent | Not public ("expensive" G2) | Medium-High |
| Quantexa | ADVERTISED | ADVERTISED | ADVERTISED | ADVERTISED (patented KG) | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | Hard | Banks/large FS | UNKNOWN | Very high |
| FICO/SAS/IBM/Pega | PARTIAL | ADVERTISED | PARTIAL | UNKNOWN | PARTIAL | PARTIAL | UNKNOWN | UNKNOWN | ADVERTISED (MQ) | PARTIAL | PARTIAL | ADVERTISED | ADVERTISED | Hard | Large regulated | UNKNOWN | Very high |
| Peak (UiPath) | PARTIAL (retail/mfg) | ADVERTISED | UNKNOWN | UNKNOWN | PARTIAL | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | UNKNOWN | PARTIAL (customer case) | ADVERTISED | ADVERTISED | Moderate | Retail/mfg mid-large | UNKNOWN | Medium-High |
| o9 | ADVERTISED (EKG) | ADVERTISED | ADVERTISED | ADVERTISED (EKG) | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | ADVERTISED (planning) | UNKNOWN | ADVERTISED | ADVERTISED | Hard | Large ent | $200K-$1M+ est. | Very high |
| Pyramid (ServiceNow) | PARTIAL | ADVERTISED | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED | UNKNOWN | UNKNOWN | UNKNOWN | PARTIAL | Moderate | Mid-large, now ServiceNow | Conflicting | Medium |
| Cloverpop | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | ADVERTISED (decision logging) | UNKNOWN | ADVERTISED (outcome tracking) | PARTIAL | UNKNOWN | Easy (workflow) | Mid-large | Not public | Low-Med |

Honest note: the matrix reflects what I could find, not exhaustive proof of absence. "UNKNOWN" in RCA for Glean/Dust etc. means I found no mention; it does not prove the feature is missing.

---

## 4. Gaps and what is commoditized

### Commoditized or near-commoditized (do not build a company on these)
- Connectors and RAG over SaaS (Glean, Dust, Onyx, Hyperspell, Copilot, Sana). Open-source and $20/user options exist (Onyx).
- NL question-answering over structured data (Power BI Copilot, PromptQL, Tellius, every BI vendor).
- No-code agent builders (Glean Agents, Dust, Sana Agents, Copilot Studio, Aera Skill Building).
- MCP/A2A interoperability (Aera, Fabric IQ MCP server, PromptQL, Palantir MCP).
- Semantic layer / ontology as AI grounding: Microsoft Fabric IQ, Palantir Ontology, ServiceNow+Pyramid, PromptQL. Big platforms treat this as a feature of their stack.
- Anomaly alerts and KPI watch (Tableau Pulse, Tellius, Palantir monitoring).
- Decision logs with policy-based approvals at the enterprise end (Aera Decision Ledger/Policy Studio, Palantir action logging).

### Where gaps appear real (hypotheses, with evidence strength)
1. SMB/mid-market with no data team: every vendor with real RCA/decision features (Palantir, Aera, Tellius, o9, Quantexa) is enterprise, sales-led, expensive, implementation-heavy. The SMB-friendly vendors (Dust, Onyx, Copilot Business) do not do metric monitoring or causal investigation. A web search for SMB "monitor and investigate" products returned only light BI tools and a GitHub prototype (STRONG negative evidence for supply; no proof of demand).
2. Cross-tool operational model (CRM + finance + product + support) rather than a single warehouse: Tellius needs a modeled warehouse; Glean models documents; Palantir models anything but requires heavy build. Zero-config "learn the company's structure from its tools" is not offered by anyone I found. INFERRED gap; could also be hard for technical reasons.
3. Causal honesty (evidence, confidence, correlation vs causation): vendors claim RCA speed (Tellius "seconds"), but I found no vendor documenting calibrated confidence or causal-vs-correlational labeling. Independent review says narratives need analyst validation (rfp.wiki). Weak evidence of gap; a trust differentiator if executable. Also LLM text-to-SQL hallucination risk is documented (promethium.ai guide).
4. Closed-loop decision/outcome learning for non-structured business decisions: Aera does it for supply-chain decisions; Cloverpop does manual logging. Nobody found linking an auto-detected change, an investigation, a human decision, and a measured outcome for SMB. INFERRED.
5. Impact propagation / simulation outside planning suites (o9, Palantir scenarios): not found for SMB.

### Honest threats and risks
- Microsoft: $21/user Copilot Business + Fabric IQ ontology + Power BI semantic models + data agents is directly aimed at "governed context layer". Its SMB weakness is the setup burden of Fabric and the Gartner-documented ROI doubts; that is a window, not a moat.
- Consolidation: acquirers (Workday, ServiceNow, UiPath) are absorbing the independents; this both validates demand and shrinks the independent field. Peak's reported ~$38M exit versus $75M raised (unverified) shows poor outcomes are possible.
- Glean at $300M ARR (vendor claim) with proactive agents could move down-market; its data model is work-artifact-centric rather than metric-centric (INFERRED), so it would need new capability to compete on RCA.
- LLM labs/agent platforms: a founder-level thesis risk (outside my scope) is that horizontal agents plus MCP connectors can replicate a lot of "investigation" on demand.

### What customers still do manually (INFERRED unless cited)
Weekly KPI reviews, deciding which anomaly matters, tracing causes across tools, remembering why a decision was made, checking whether the outcome matched the expectation, and maintaining metric definitions. Reviewers of Aera cite data quality and change management as success factors; Glean/Copilot reviews cite data hygiene and oversharing.

### Evidence quality warning
Most pricing is from aggregators or consultancies (costbench, usagepricing, redresscompliance, bdemerson, eesel) with conflicts. Review-site excerpts are small samples (G2 Tellius ~26 reviews; Capterra Glean value score on 2 reviews). No Reddit or TrustRadius data surfaced. Recommend a follow-up pass with network access to vendor docs (glean.com, palantir.com/docs, learn.microsoft.com), G2/Gartner Peer Insights full reads, and a few demos/trials.

---

## 5. Source list (selected)
- Glean ARR: https://glean.com/press/glean-surpasses-300m-arr-unrivaled-enterprise-context-fuels-ai-adoption ; G2: https://g2.com/products/glean-technologies-glean/reviews ; Proactive: https://www.glean.com/blog/intelligent-secure-proactive-ai
- Microsoft price: https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/act-now-lock-in-current-pricing-on-microsoft-365-copilot/ba-p/4502628 ; Power BI Copilot: https://learn.microsoft.com/power-bi/create-reports/copilot-enable-power-bi ; Fabric IQ: https://atlan.com/know/microsoft-fabric/what-is-fabric-iq/ , https://www.forrester.com/blogs/microsoft-fabcon-2026-enterprise-ai-needs-a-governed-context-layer-not-just-data/ ; Gartner Copilot: https://www.techpartner.news/news/gartner-microsoft-copilot-hype-offset-by-roi-and-readiness-realities-618118
- Workday-Sana close: https://newsroom.workday.com/2025-11-04-Workday-Completes-Acquisition-of-Sana
- UiPath-Peak: https://www.uipath.com/newsroom/uipath-acquires-peak-to-launch-vertically-specialized-agents ; https://techcrunch.com/2025/03/13/uipath-is-looking-for-a-path-to-growth-in-agentic-ai-with-its-peak-ai-acquisition
- ServiceNow-Pyramid: https://www.servicenow.com/blogs/2026/pyramid-analytics-expanding-data-driven-ai
- Aera: https://itbrief.co.uk/story/aera-unveils-six-tools-to-automate-enterprise-decisions ; Gartner reviews: https://www.gartner.com/reviews/product/aera-decision-cloud
- Gartner DI MQ: https://www.gartner.com/en/documents/7363830 ; https://fintechnews.ch/aifintech/top-decision-intelligence-platforms-of-2026-according-to-gartner/82427/
- Palantir docs: https://palantir.com/docs/foundry/announcements/2025-10/ ; https://palantir.com/docs/foundry/architecture-center/aip-architecture ; pricing estimates: https://www.bdemerson.com/article/palantir-cost , https://redresscompliance.com/palantir-aip-foundry-guide.html
- Tellius: https://www.tellius.com/resources/blog/ai-powered-root-cause-analysis-from-what-happened-to-why-in-60-seconds ; G2: https://www.g2.com/products/tellius/reviews ; rfp.wiki: https://www.rfp.wiki/artificial-intelligence/analytics-business-intelligence-platforms/agentic-analytics/tellius
- Dust pricing: https://costbench.com/software/ai-search-enterprise/dust-tt/ ; Onyx: https://onyx.app/pricing ; PromptQL: https://hasura.io/pricing/promptql ; Hyperspell: https://ycombinator.com/companies/hyperspell
- Quantexa: https://www.quantexa.com/platform/ ; o9: https://o9solutions.com/ai-info , https://softabase.com/software/supply-chain-management/o9-solutions ; Cloverpop: https://www.g2.com/products/cloverpop/pricing

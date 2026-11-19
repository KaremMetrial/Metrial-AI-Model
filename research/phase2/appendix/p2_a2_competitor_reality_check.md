# P2-A2: Competitor Reality Check for "Margin Investigator"

Date: 2026-11-19. Agent: Phase-2 Research Agent 2. Status of recommendation: NOT approved; this file tests differentiation.

## 0. Method and honesty limits

- WebFetch failed with DNS/ENOTFOUND on every host I tried (list in section 6). I could NOT read any primary page directly. All evidence is WebSearch result summaries, some of which quote primary vendor/docs text.
- Label meaning in this file:
  - VERIFIED* = concrete primary-source text (vendor docs, help center, app listing, press release) appeared inside a search summary. The asterisk means I did not fetch the page myself and saw no independent test.
  - ADVERTISED = vendor marketing or partner/consultant blog only.
  - INFERRED = my reasoning from product shape.
  - UNKNOWN = not found. UNKNOWN never means "missing".
- Nothing here is a hands-on test. No independent accuracy benchmark for any margin-RCA product was found.
- Prices are mostly aggregator or vendor-affiliated and conflict; each is cited with its source.

## 1. Headline findings (read this first)

1. **PVM and margin bridges already exist, but not as an automatic SMB product.** Found: Vendavo Margin Bridge Analyzer (enterprise PVM with cost effect, ADVERTISED); Coefficient's free QuickBooks price-volume-mix template (user-run spreadsheet, waterfall chart, scheduled refresh, VERIFIED* mechanics); Zebra BI and Inforiver PVM visuals for Power BI (ADVERTISED); an Umbrex SKU-level template with price/volume/mix/cost terms. I found NO SMB product that runs PVM or a margin bridge automatically, continuously and unprompted on Shopify/ERP data (UNKNOWN, not proven absent; a Shopify-app search for "price volume mix / margin bridge / margin waterfall" returned none).
2. **"Cost increase not passed through to price" detection exists in narrow slices.** MarginEdge (restaurants, invoice-driven price alerts, ~$330-350/location/month, ADVERTISED), CostSentry and Margin Sentinel (Shopify, supplier-cost-change alerts and margin floors, ADVERTISED), price-list monitoring tools, SPARXiQ on Epicor (override and contract-drift analytics, ADVERTISED). None found that joins supplier cost change, price lag, mix and volume into one explained case with evidence.
3. **The cheap end of the market already does "margin exception queue".** Profit Pulse AI ($19/month, Shopify) flags negative-margin orders, low-margin products, missing COGS, discount leakage and shipping drag (VERIFIED* listing text; zero reviews, so adoption UNKNOWN). Part of the wedge ("what is leaking, ranked") is therefore a $19 commodity on Shopify.
4. **ERP-native "why did margin drop" now exists for NetSuite.** Ask Oracle can be asked "why did margins drop this month" (Withum, Crowe; ADVERTISED/partner). NetSuite Analytics Warehouse was renamed NetSuite Data Intelligence at SuiteWorld 2026, with a Data Intelligence Agent and "Deep Insights"; 2026.2 adds pricing analytics comparing realized margin with expectations. Accuracy is untested; AI is metered via "AI Units" (Crowe). This corrects Agent 7, which listed NetSuite as UNVERIFIED.
5. **The claimed differentiators are not documented anywhere I could see.** Separate confidence for observation vs explanation, explicit counterevidence, and outcome follow-up: no product found documents them for margin work. Closest partials: Aera Decision Ledger (enterprise supply chain, prior files), Lifetimely Profit Agent (proposes and executes on approval; outcome tracking UNKNOWN), Polar's own marketing saying an AI looking at Shopify alone can misattribute a swing. Absence of documentation is weak evidence of absence, and these features are cheap to copy once someone cares.
6. **Verdict: PARTIAL** (section 4). The wedge is real only as a combination (distributor/multi-system, evidence-linked, honest uncertainty, follow-up) for companies whose ERP has no AI margin explainer. Each single element has a substitute.

## 2. Comparison matrix

Columns: OOB = ready out-of-box margin analytics; Config = who must configure; RCA = root-cause/driver analysis (PVM, price/cost/mix/volume/FX/freight decomposition counts); Multi = multi-system; Trace = traceability to underlying records; CE/Unc = counterevidence/uncertainty; Rec = recommends actions; Track = outcome tracking. Price, Segment and Complaints follow.

### 2a. ERP-native

| Vendor | OOB | Config | RCA | Multi | Trace | CE/Unc | Rec | Track | Price | Segment | Top complaints |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NetSuite (SuiteAnalytics, NAW now "Data Intelligence", Ask Oracle, Next) | ADVERTISED: item/customer margin reports; AI Q&A "why did margins drop" | Admin or partner; AI Units metered | ADVERTISED (Ask Oracle explanation, 2026.2 pricing analytics); method UNKNOWN | Own ERP + warehouse; external LLM connector (ADVERTISED) | UNKNOWN | UNKNOWN | ADVERTISED ("Deep Insights" recommendations) | UNKNOWN | ~$129-199/full user/mo + ~$999-5,000/mo base (erpresearch, hyperbots, Vendr; est.); $50-150K/yr mid-market (est.) | Mid-market, 50+ users | Partner blogs say standard P&L shows that margin fell but not why (AlphaBOLD, ACL); AI cost metering (Crowe) |
| Acumatica 2026 R1/R2 | VERIFIED*: Amazon profitability dashboards (fees, refunds, product margin); margin on quotes | Partner/IT; AI Studio is user-built | UNKNOWN | Marketplaces in-suite | UNKNOWN | UNKNOWN | ADVERTISED (AI Assistant early access) | UNKNOWN | Not public | Mid-market | Not found |
| Odoo (19) | VERIFIED*: margin = price minus cost per product/SO; sales analysis report with Sales Margin measure | User; margin depends on cost field accuracy | NO PVM in docs found; UNKNOWN for AI | Own suite | Drill-down in reports (INFERRED) | UNKNOWN | UNKNOWN | UNKNOWN | Per-user; not researched | SMB-mid | Margins rely on cost/price fields entered; some add-ons incompatible with Odoo Online (Cybrosys/Idealis, community) |
| Microsoft Dynamics 365 Business Central | VERIFIED*: Sales analytics, Power BI Sales app, Copilot over analysis views; gross profit by item | Partner for Power BI apps | PARTIAL: Copilot Q&A; native PVM not found | Via Power BI/Fabric | Drill via BC | UNKNOWN | UNKNOWN | UNKNOWN | Per-user + Copilot capacity | SMB-mid | No independent reviews of margin AI found |
| Epicor Prophet 21 / Eclipse (+SPARXiQ) | ADVERTISED: Epicor Data Analytics, FP&A; SPARXiQ pricing-leak analytics | Epicor/partner; AI features need cloud (Software Reviews) | ADVERTISED: leak sources (overrides, contract drift); PVM bridge UNKNOWN | Epicor data only | UNKNOWN | UNKNOWN | ADVERTISED (customer-level price recs) | UNKNOWN | Not public; SPARXiQ claims 200-400 bps (vendor) | Distributors (mid-market) | Not found |
| Sage Intacct / Sage X3 | ADVERTISED: Copilot flags budget variances; X3 anomaly detection | Sage/partner | UNKNOWN | Within Sage | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Not researched | Mid-market | Not found |
| Brightpearl (Sage) | ADVERTISED: Retail Analytics via Conjura, daily sync, SKU margin | Light | PARTIAL (see Conjura) | Via Conjura | SKU level | UNKNOWN | ADVERTISED | UNKNOWN | Not public | Multichannel retail/wholesale | Cin7 marketing says Cin7 reporting is weak (biased) |
| Cin7 Core / Omni | VERIFIED*-ish: gross-profit reports from static COGS | User | NO AI margin feature found (UNKNOWN) | Own | Report drill | UNKNOWN | UNKNOWN | UNKNOWN | Not researched | SMB inventory | Reporting limits, steep learning curve (G2 comparison) |
| Fishbowl, Katana, Linnworks | UNKNOWN for margin analytics | User | UNKNOWN | Own | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Not researched | SMB | Fishbowl: limited reporting (G2 comparison); Katana: wants richer reporting (SelectHub) |

### 2b. Shopify profit and analytics apps

| Vendor | OOB | Config | RCA | Multi | Trace | CE/Unc | Rec | Track | Price | Segment | Top complaints |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Shopify native reports / Sidekick Pulse | VERIFIED*: gross profit = net sales minus static per-item COGS; excludes fees, shipping, returns, ads | Merchant enters costs | NO decomposition found for profit; Pulse margin advice UNKNOWN | Shopify only | Order-level | UNKNOWN | ADVERTISED: Pulse "up to 5 recommendations" (secondary) | UNKNOWN | Included in plan | All merchants | Cost field static in time; gross not net profit |
| TrueProfit | VERIFIED*-ish: P&L, ad spend, COGS sync | Merchant | NO PVM/driver found; UNKNOWN | Shopify, ads | Order/product | UNKNOWN | UNKNOWN | UNKNOWN | $35/$60/$100/$200 by orders; $0.30/order overage cap $300 (listing via search) | SMB DTC, 4.9 stars, ~780-1,100 reviews (counts conflict) | Price, overage in busy months, occasional COGS/P&L sync lag (reviews) |
| BeProfit | ADVERTISED: profit dashboard, multichannel | Merchant | UNKNOWN | Shopify, Amazon, Woo | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | $25-249 (sources conflict) | SMB | One-star reviews about billing (one source) |
| Lifetimely (Amp) | ADVERTISED: daily P&L, contribution margin, LTV, cohorts | Merchant | UNKNOWN | Shopify, ads, Amazon add-on | UNKNOWN | UNKNOWN | ADVERTISED: Profit Agent 24/7 monitors and executes on approval | UNKNOWN | Free <50 orders; paid from $49; M $149 (3,000 orders) per Amp pages (vendor) | DTC SMB, ~4.8 stars | Narrower than full analytics suites (review) |
| Polar Analytics | ADVERTISED: semantic layer, contribution margin, "AI Data Analyst", "revenue autopsy" use case | Setup by Polar/merchant | ADVERTISED: traces swing to channel/margin shift using ads+finance | Shopify, ads, finance | UNKNOWN | ADVERTISED: states Shopify-only AI can misattribute | UNKNOWN | UNKNOWN | Not retrieved | Mid-size DTC | Not found |
| Triple Whale (Moby) | ADVERTISED: net profit, cost inputs, cohorts; Moby agent | Merchant | Critics: weak margin view (competitor blogs); UNKNOWN | Shopify, ads, email | UNKNOWN | UNKNOWN | ADVERTISED: acts in ad/email accounts | UNKNOWN | ~$219/mo Foundation by GMV; Automate from $749 (competitor pages; unconfirmed) | DTC | Data inaccuracy, ROAS mix-ups, price, slow support (G2, Shopify reviews, small samples) |
| Conjura (Wayflyer, acquired 2026-06-19) | VERIFIED*: SKU-level contribution profit incl. ads, shipping, refunds, fees; ERP/OMS/marketplace inputs | Light | ADVERTISED: top/bottom SKU breakdown and pricing recs; PVM UNKNOWN | Store, ads, ERP, marketplaces | SKU | UNKNOWN | ADVERTISED pricing recs | UNKNOWN | Free plan or custom; ">$20M GMV custom" (listings conflict) | DTC/wholesale brands, ~2,000 merchants | Acquisition may redirect roadmap to Wayflyer financing (analyst view, INFERRED) |
| Setpilot (Digismoothie) | VERIFIED*: CM1-CM4 profit waterfall (a cost-stack, not a period bridge) | Merchant costs | NO period-over-period decomposition found | Shopify, ads | Product | UNKNOWN | ADVERTISED "AI" | UNKNOWN | Free plan; $29.99 start (third-party) | Small Shopify | Vendor says new, limited track record |
| Profit Pulse AI (Das Group) | VERIFIED*: exception queue (negative margin, missing COGS, discount leakage, shipping drag) | Merchant | NO; rule-based flags (INFERRED) | Shopify | Order | UNKNOWN | Queue items | UNKNOWN | $19/mo | Tiny Shopify | 0 reviews |
| Hypersonix Profit Max AI | ADVERTISED: weekly ranked margin/inventory/promo recommendations to variant level; WoW/YoY | Install | PARTIAL/UNKNOWN | Shopify, competitor listings | Variant | UNKNOWN | ADVERTISED | UNKNOWN | App page shows Free; vendor claims 8-28% profit lift (conflicting) | SMB to mid | 0 reviews |
| Margin Sentinel, CostSentry | ADVERTISED: missing cost, negative margin, supplier-cost-change alerts, margin floors | Merchant CSV | NO | Shopify (+CSV) | Variant | UNKNOWN | Alerts | UNKNOWN | Free 100 variants; paid tiers | Micro | Vendor pages only |

### 2c. QuickBooks / Xero ecosystem

| Vendor | OOB | Config | RCA | Multi | Trace | CE/Unc | Rec | Track | Price | Segment | Top complaints |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QuickBooks (AI report insights, Intuit Intelligence) | VERIFIED*: AI flags trends/anomalies in P&L and Balance Sheet (Plus, Advanced, Enterprise Suite); Oct 2026 Intuit Intelligence is beta | None | PARTIAL: P&L-level anomaly; product-level margin UNKNOWN | QuickBooks data (+ Anthropic partnership, secondary) | UNKNOWN | UNKNOWN | ADVERTISED: next steps with confirmation | UNKNOWN | In subscription | Micro to mid | Beta limitations (walkthrough); no independent product-margin test found |
| Xero (Analytics, JAX) | ADVERTISED: gross-margin overview with AI insights (AU/NZ), JAX Q&A | None | UNKNOWN | Xero data | UNKNOWN | UNKNOWN | ADVERTISED | UNKNOWN | In subscription | Micro to SMB | Not found |
| Fathom | ADVERTISED: management reporting, consolidation, KPI | Accountant | NO PVM found; UNKNOWN | Accounting only | Drill to ledger (INFERRED) | UNKNOWN | UNKNOWN | UNKNOWN | G2 "contact"; $50 start (third-party, conflicting) | Accountants/advisors | Steep learning curve, report-locking, date flexibility gaps (Xero App Store reviews) |
| Syft, Spotlight | ADVERTISED: reporting, forecasting; Syft free tier | Accountant | UNKNOWN | Accounting | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Syft $0 basic; Spotlight $35-250 (conflicting) | Accountants | One source: Spotlight lacks anomaly detection (low-authority) |
| Puzzle, Digits | ADVERTISED: AI close incl. variance explanations; anomaly checks | None | PARTIAL: variance text, human-in-loop (vendor) | Accounting | UNKNOWN | ADVERTISED human review | UNKNOWN | UNKNOWN | Not researched | Startups/SMB | Puzzle acquisition by Accrual (Sept 2026) is claimed only on a Digits competitor page: UNVERIFIED |
| A2X, Link My Books | ADVERTISED: payout-level sync; SKU COGS journals depend on Shopify cost field | Bookkeeper | NO | Shopify to QBO/Xero | Payout summaries | n/a | n/a | n/a | Not retrieved | Ecommerce bookkeepers | Payout aggregation hides transaction detail; bundle COGS breaks (Webgility, competitor) |
| LivePlan, Jirav, Zeni, Pilot | UNKNOWN (no usable results) | | | | | | | | | | |

### 2d. Inventory, cost and pricing analytics

| Vendor | OOB | Config | RCA | Multi | Trace | CE/Unc | Rec | Track | Price | Segment | Top complaints |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cogsy, Prediko, Inventory Planner, Netstock | ADVERTISED: forecasting, replenishment, scenarios; margin analytics UNKNOWN | Merchant | NO margin RCA found | Shopify/ERP | n/a | UNKNOWN | Reorder recs | UNKNOWN | Prediko from $49; Cogsy ~$199 (range $69-199); Netstock $900/mo or $15-50K/yr (estimates) | DTC, SMB ERP | Not retrieved |
| Stocky (Shopify) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Shut down 2026-08-31 (craftybase, others): no longer a competitor |
| Lokad, GMDH, Slimstock | UNKNOWN (not researched deeply; supply-planning, INFERRED not margin) | | | | | | | | | | |
| Vendavo (Margin Bridge Analyzer) | ADVERTISED: PVM with cost decomposition, tariff early warning, freight methodology example | Vendor/customer config ("configuration not code") | ADVERTISED: price, volume, mix, cost effects | Enterprise ERP feeds | UNKNOWN | UNKNOWN | ADVERTISED (diagnostics) | UNKNOWN | ~$75K/yr floor (single comparison site, Jan 2026) | $20M-$250M+ B2B | No independent reviews found; 4.3 G2 (aggregator) |
| Zilliant (Price IQ, Pricing Plus) | ADVERTISED: governed price waterfall, AI pricing analytics, MCP server (Oct 2025) | Vendor; Pricing Plus pitched for no pricing staff | PARTIAL: waterfall per transaction, not period bridge (INFERRED) | ERP feeds | UNKNOWN | UNKNOWN | ADVERTISED | UNKNOWN | Not public; G2 4.4 (61 reviews) | Distributors/manufacturers | Not found. Vendor survey: 23% use AI pricing |
| Pricefx, PROS | ADVERTISED | Vendor, months | UNKNOWN | ERP | UNKNOWN | UNKNOWN | ADVERTISED | UNKNOWN | Pricefx ~$50K/yr floor (comparison site); not public | Mid to enterprise | Timelines 4-12 months (conflicting) |

### 2e. BI and AI-native analytics

| Vendor | OOB | Config | RCA | Multi | Trace | CE/Unc | Rec | Track | Price | Segment | Top complaints |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Power BI | Key Influencers, Decomposition Tree native visuals; PVM via third-party visuals/templates | Analyst builds model and measures | PARTIAL: statistical contribution, not causal; PVM = DIY | Many | Drill-through | Key Influencers is correlation (INFERRED) | NO | NO | Pro $14/user/mo (Querio roundup) | All | Needs model builder |
| Tableau (Pulse) / Looker / ThoughtSpot / Qlik / Sigma / Metabase / Domo / Zoho | See Agent 1B; no PVM or margin-specific feature found this pass | Data team | PARTIAL at best | Many | Drill | UNKNOWN | Varies | NO | ThoughtSpot $25-50/user (conflicting) | Mid to enterprise | Domo/Zoho/Metabase AI: UNKNOWN |
| Phocas | ADVERTISED: margin analysis, rebates, drill to negative-margin SKUs; AI summaries | Phocas/partner | PARTIAL: drill-down, narrative; no PVM documented | ERP + others | Drill to SKU | UNKNOWN | ADVERTISED anecdote (value story vs discount) | UNKNOWN | No list price; $150/mo listing-site figure | Distributors | Not found |
| Tellius | ADVERTISED: automated driver analysis, agentic monitoring; CPG page says PVM needs custom Excel models | Data team, warehouse | ADVERTISED; PVM engine UNKNOWN | Warehouse | UNKNOWN | Independent: narratives need analyst validation (prior file) | ADVERTISED | UNKNOWN | Not public; "expensive" (G2, prior) | Mid-large | Cost, integration |
| WisdomAI | ADVERTISED: proactive agents, RCA with evidence (charts, SQL, summary) | Context onboarding and connectors | ADVERTISED | Warehouse | SQL shown | UNKNOWN | UNKNOWN | UNKNOWN | No public price; ~40 enterprise customers (CEO, Nov 2025) | Enterprise | Not for small teams (directory) |
| Zenlytic | ADVERTISED | Customer builds ecommerce margin models (competitor Saras claim) | UNKNOWN | Warehouse | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | Not public; G2 4.1 (17 reviews, via competitor) | Mid-market | Biased source |
| Julius, Hex, Basedash, Narrative BI, Gravity | Reactive Q&A or notebooks; Narrative BI not found; Gravity not re-researched | Analyst | NO automatic PVM found | Files/warehouse | Code/SQL shown | UNKNOWN | NO | NO | Julius ~$20/mo (Agent 1B) | Individuals/teams | "Shared metric layer: No" (competitor-sponsored review) |
| Claude for Small Business | ADVERTISED: 15 workflows; QuickBooks cash/forecast/overdue; no margin workflow found | User/prompts | On demand | QuickBooks, PayPal, HubSpot, etc. | Per connector | User-dependent | Queues for approval | UNKNOWN | No extra charge beyond Claude licenses | Small business | Not found |

### 2f. Decision/process intelligence (irrelevance check)

| Vendor | Verdict |
|---|---|
| Aera, Celonis, Peak (UiPath), Palantir | Enterprise, sales-led, implementation-heavy (Agent 1A/1B). Aera Decision Ledger is the only outcome-tracking analog found. INFERRED irrelevant for SMB. No new evidence this pass. |

## 3. Per-competitor evidence notes (closest to the wedge first)

**Vendavo Margin Bridge Analyzer (enterprise, ADVERTISED).** Vendavo describes comprehensive PVM across business dimensions, breaking gross-profit change into price, volume and mix effects, with cost-effect decomposition and "early warnings of margin erosion due to tariffs". Models are built by configuration, not code. It cites a freight methodology case, so freight is at least representable. Its own 2022 release calls it the only enterprise-ready solution. Pricing not public; one comparison site gives ~$75K/yr floor. The wedge is not "PVM exists"; it is "PVM without a pricing team or six-month deployment, and with evidence trail". Whether Vendavo gives record-level traceability, uncertainty or outcome tracking: UNKNOWN.

**Coefficient QuickBooks PVM template (VERIFIED* mechanics).** Free spreadsheet template: price effect = (current price - prior price) x current volume; volume effect = prior price x volume change; mix effect = (current mix % - prior mix %) x total current revenue. Includes a waterfall chart and a scheduled refresh. This is revenue PVM; I did not see a COGS or cost term in the results, so gross-margin bridge capability is UNKNOWN. It needs a human to run and read it. It kills the claim that "no one provides PVM for QuickBooks users"; it does not kill "automatic, explained, evidence-linked."

**Zebra BI / Inforiver PVM (ADVERTISED).** Third-party Power BI visuals and templates for PVM and variance. DIY for an analyst. Gartner also lists a PVM template (title only). Reinforces that PVM is a known commodity technique (FTI notes that revenue PVM plus COGS PVM gives a gross-margin bridge; also that traditional PVM needs consistent units and mishandles returns and discontinued SKUs, which is a real SMB data problem).

**NetSuite (Ask Oracle / Data Intelligence / Next).** The closest ERP-native threat. Partner write-ups say finance can ask Ask Oracle to explain a gross-margin decline; ACL Digital claims anomaly recognition can flag margin compression and unexpected cost spikes; 2026.2 adds pricing analytics comparing realized margin with expectations. NetSuite Next is available in the US/Canada as of 2026-07-30 (Oracle statement via search). No primary doc or independent test seen. AlphaBOLD (a NetSuite partner) frames the gap as: a standard P&L shows that margin fell but not why, and it is usually many small changes; they argue AI should trace it to SKUs. Implication: for NetSuite distributors the "explain" function is on the vendor roadmap and partly shipped; the opening is smaller, and it is limited to NetSuite data plus a connector.

**Hypersonix Profit Max AI and Profit Pulse AI (Shopify, ADVERTISED/VERIFIED* listing).** Profit Max AI produces weekly ranked recommendations on margin, inventory and promotions to variant level. Profit Pulse AI is a $19/month exception queue. Neither shows evidence, counterevidence, confidence or outcome tracking in what I saw. Both have zero reviews: adoption UNKNOWN. They show the "ranked leak list" is cheap.

**Polar Analytics.** Its "Shopify revenue autopsy" use case traces a revenue swing to Meta spend and new-customer revenue and argues that Shopify-only AI can misattribute. That is vendor acknowledgment of the counterevidence problem, but ADVERTISED and aimed at revenue, not distributor gross margin. Polar's semantic layer defines contribution margin once. Pricing not retrieved.

**Lifetimely / Amp Profit Agent.** Monitors the store 24/7, proposes and executes actions on approval; covers P&L, margin, LTV, CAC, cohorts, product analysis (vendor comparison pages). Paid plans only (M tier $149 for 3,000 orders). Closest "monitor, recommend, act with approval" analog at SMB price. Root-cause decomposition, counterevidence and outcome follow-up: UNKNOWN.

**Conjura (Wayflyer).** SKU-level contribution profit with ad, shipping, refund and fee deductions; pulls ERP/OMS; Brightpearl resells it. Acquired by Wayflyer 2026-06-19 (Business Wire press release); Wayflyer plans AI for small-business customers. Agent 1B listed Conjura only in passing and missed the acquisition. Strategic implication (INFERRED): the independent Shopify-margin-analytics field is consolidating into lenders and ERP-adjacent vendors.

**Epicor + SPARXiQ (distributors).** SPARXiQ's pitch at Epicor Insights 2026 is finding "pricing leaks" in Prophet 21/Eclipse data; named causes are overrides, contract drift and inconsistent execution; claims 200-400 bps. Mechanism: customer data exported to SPARXiQ, recommendations returned. No margin bridge found (the search found none). A distributor-specific source (Distribution Strategy Group, Cavallo) lists cost pass-through timing, rounding to 0s and 5s, and long SPA reconciliation cycles as margin leaks; those are exactly the kinds of causes a product would have to encode.

**Phocas.** Distribution-focused BI. A 2026 blog describes drill-down from territory to negative-margin SKUs and an AI summary advising a value story over a price concession for an account at 6% margin (anecdotal, ADVERTISED). Margin analysis and rebates analytics are features. No PVM or evidence-with-uncertainty documented. Likely the most direct distributor-BI substitute for the "where is margin going" question; the "why" step is still the user's.

**Tellius and WisdomAI.** Both do or claim automated driver analysis and proactive RCA on warehouse data with enterprise pricing and onboarding. Tellius' own CPG page admits PVM otherwise needs custom Excel models per request, i.e. they sell automation of exactly that. Neither is SMB or no-data-team (warehouse and modeling prerequisites, INFERRED from directory descriptions).

**QuickBooks / Xero native.** QuickBooks AI report insights flag trends and anomalies on P&L and Balance Sheet (Plus, Advanced, Enterprise Suite); Intuit Intelligence is beta; product-level margin and inventory costing were not shown. Xero Analytics (AU/NZ) shows gross margin with AI-written insights. Neither does Shopify-to-ledger-to-supplier cross-system causality (INFERRED from their data boundaries). Per Agent 7, Anthropic partners with both.

**Fathom, Syft, Spotlight, A2X, Link My Books.** Reporting and sync layers. A2X's SKU COGS journals depend on the Shopify cost field and work from payouts; Webgility (competitor) notes bundle SKUs break COGS. This is a data-quality precondition that any margin investigator inherits, and supports Agent 7's point that onboarding is data cleaning.

**Inventory tools (Cogsy, Prediko, Inventory Planner, Netstock).** Forecasting and replenishment; margin RCA not found. Stocky is gone (Aug 31, 2026).

**Power BI.** Native Key Influencers and Decomposition Tree plus PVM via third-party visuals. A model builder is required. Sources warn that automated attribution can mislead when a key dimension is missing from the model.

**Claude for Small Business.** QuickBooks workflows reported: cash reconciliation with PayPal, 30-day forecast, overdue ranking with queued reminders. I found no margin workflow. Nothing prevents a user from prompting margin questions (INFERRED); it is the main generalist substitute.

## 4. Differentiation verdict

**Verdict: PARTIAL.** Margin Investigator is differentiated as a combination for a specific buyer, not on any single feature.

Claim-by-claim:

| Claimed differentiator | Status | Reasoning |
|---|---|---|
| Automatic margin driver analysis (price/cost/mix/volume) | NOT SUPPORTED as unique | Exists enterprise (Vendavo), DIY (Coefficient, Zebra BI, Inforiver, Power BI visuals), ADVERTISED ERP-native (NetSuite Ask Oracle), ADVERTISED AI-BI (Tellius, WisdomAI). |
| Works for SMB/distributors without data team or pricing team | PARTIAL / INSUFFICIENT | I found no SMB product doing automatic PVM on Shopify/ERP data, and no zero-config distributor product. Absence in search is weak evidence; Hypersonix, Polar and Conjura could be doing more than their public pages show. |
| Multi-system (Shopify + ERP + QuickBooks/Xero + supplier costs) | PARTIAL | Polar, Conjura, Brightpearl combine store, ads, ERP, but not ledger plus supplier invoice evidence for distributors. Each ERP covers only itself. |
| Evidence trail to underlying records | INSUFFICIENT | Order/SKU-level drill exists in many tools; a case file that cites specific invoices and POs was not seen anywhere. UNKNOWN for Vendavo, NetSuite AI. |
| Separate confidence for observation vs explanation; counterevidence | INSUFFICIENT but unclaimed by anyone | No vendor documents it for margin. Polar and AI-BI sources acknowledge misattribution risk in prose. Gap is plausible; not shown to matter to buyers (Agent 7 trust surveys suggest it may). |
| Recommended action | NOT SUPPORTED as unique | Hypersonix, Lifetimely, Conjura, SPARXiQ, Zilliant, Phocas already recommend. |
| Outcome tracking | PARTIAL | Aera (enterprise) has Decision Ledger; no SMB product found with margin-action outcome follow-up. Agent 7 doubts it will be used (decision journals are rarely maintained). |
| Cost increase vs price pass-through detection | PARTIAL | MarginEdge (restaurants), CostSentry, Margin Sentinel, price-list monitors catch cost changes; joining that to mix/volume and explaining is not seen. |

Contradictory evidence to weigh:
- Against differentiation: the $19 exception queue; Coefficient's free PVM; NetSuite's "why did margins drop" prompt; Phocas margin drill for distributors; QuickBooks and Xero embedding AI insights; Claude for Small Business as a prompt-based substitute; consolidation (Conjura to Wayflyer, Puzzle claimed acquired).
- For differentiation: even enterprise tools (Tellius page, FTI) concede PVM is manual or fragile (unit consistency, returns, discontinued SKUs); partner blogs say standard ERP reports show what, not why; cheap Shopify apps show rule-based flags without decomposition; no one documents calibrated or counterevidence-based explanation.
- Unresolved: whether NetSuite Ask Oracle, Hypersonix and Polar's agents actually produce evidence-linked decompositions. A 1-hour trial of each would resolve it; I could not do that.

What would move this to SUPPORTED: (1) a blind test where owners prefer Margin Investigator case files over NetSuite Ask Oracle, Polar's agent or a Claude/QuickBooks prompt on the same data; (2) a distributor segment (QuickBooks, Xero, Odoo, Acumatica, Business Central, Cin7) where no vendor AI explainer exists; (3) evidence that buyers pay for uncertainty and outcome tracking, not just the explanation.

## 5. Closest to the wedge, and what they do not (do not know)

1. **Vendavo Margin Bridge Analyzer**: closest functionally (PVM + cost + early warning). Not SMB, long implementation, price UNKNOWN. Evidence/uncertainty/outcomes: UNKNOWN.
2. **NetSuite Ask Oracle / Data Intelligence**: closest ERP-native, for NetSuite customers only. Method and accuracy UNKNOWN; AI Units cost.
3. **Hypersonix Profit Max AI / Polar Analytics / Lifetimely / Conjura**: closest SMB Shopify, with recommendations and (Lifetimely) approval-based action. No documented counterevidence, confidence or outcome tracking; non-Shopify ERP/ledger depth UNKNOWN.
4. **Phocas + SPARXiQ on Epicor**: closest distributor stack. No documented bridge; human-led.
5. **Tellius / WisdomAI**: closest AI-native RCA, but warehouse-centric, enterprise.
6. **MarginEdge, CostSentry**: closest on supplier-cost change alerts, narrow verticals.

## 6. Blocked hosts and untested hosts

WebFetch failed (getaddrinfo ENOTFOUND, i.e. outside the session network allowlist): help.shopify.com, apps.shopify.com, www.netsuite.com, www.polaranalytics.com, www.vendavo.com, docs.oracle.com, www.odoo.com, learn.microsoft.com, www.g2.com. The tool instructed me to stop trying other hosts after repeated failures, so apps.xero.com, quickbooks.intuit.com, acumatica.com, and the hosts of other vendors were NOT individually tested; I assume blocked (INFERRED). Everything is therefore based on WebSearch summaries. Recommend allowlisting help.shopify.com, apps.shopify.com, apps.xero.com, vendavo.com, netsuite.com/docs.oracle.com, polaranalytics.com, useamp.com and g2.com for a follow-up, plus 30-60 minute trials of NetSuite Ask Oracle, Polar, Lifetimely, Hypersonix.

Corrections to prior agents:
- Agent 1B: Conjura is no longer independent (acquired by Wayflyer, 2026-06-19). Zenlytic as "direct DTC competitor": the only 2026 source (Saras, a rival) calls it general-purpose, so DTC fit is UNKNOWN.
- Agent 7: NetSuite "UNVERIFIED" is now partly covered (Ask Oracle, Data Intelligence). Odoo and Acumatica have no AI margin-RCA that I could find.
- Agents 1A/1B/7 on Peak: funding and price conflict ($38.1M consideration vs ~$115-118M raised); not re-checked.
- Agent 1B's "no Shopify-ready margin PVM" is consistent with this pass but still not proof.

## 7. SOURCE REGISTER

All sources were seen only as search-result summaries (WebFetch blocked) unless stated. Dates are those shown or inferred from the result; "n/d" = not displayed.

| ID | URL | Source date | Source type | Claims supported | Reliability note |
|---|---|---|---|---|---|
| A2-01 | https://help.shopify.com/manual/reports-and-analytics/shopify-reports/report-types/profit-reports | n/d | Vendor help center (via search) | Shopify profit report is gross profit from static per-item cost; excludes fees/shipping/ads | Primary; plan gating conflicts across secondary sources |
| A2-02 | https://www.vendavo.com/?p=35939 | n/d | Vendor product page | Margin Bridge Analyzer: PVM, cost, tariff warnings, configuration | Marketing; no price or reviews |
| A2-03 | https://www.vendavo.com/?p=5065 | n/d | Vendor press | Profitability diagnostics added to Margin Bridge Analyzer | Marketing |
| A2-04 | https://coefficient.io/dashboard-examples/quickbooks-price-volume-mix-analysis | n/d | Vendor template page | QuickBooks PVM formulas, waterfall, refresh | Vendor-described; no independent test |
| A2-05 | https://zebrabi.com/template/price-volume-mix-analysis-power-bi-template/ ; https://inforiver.com/blog/inforiver-analytics-plus/price-volume-mix-analysis-power-bi/ | n/d | Vendor templates | PVM visuals for Power BI | Marketing |
| A2-06 | https://www.fticonsulting.com/insights/white-papers/quantifiable-approach-price-volume-mix-analysis | n/d | Consultancy white paper | Revenue PVM + COGS PVM = margin bridge; unit consistency caveats | Good methodology source |
| A2-07 | https://umbrex.com/resources/company-analysis/product-management/gross-margin-by-product/ | n/d | Template site | Price/volume/mix/cost effect formulas | Template, not product |
| A2-08 | https://apps.shopify.com/trueprofit | 2026 | App listing (via search) | TrueProfit plans, rating, overage fees | Review counts conflict across pages |
| A2-09 | https://ecommercefastlane.com/trueprofit-shopify/ | 2026 | Trade blog | TrueProfit cost and fit | Secondary |
| A2-10 | https://attribuly.com/blogs/triple-whale-pricing-review/ ; https://venon.io/blog/triple-whale-pricing | 2026 | Competitor blogs | Triple Whale pricing, margin-view critique | Biased, unconfirmed |
| A2-11 | https://www.g2.com/products/triple-whale/reviews | 2026 | Review site (via search) | Triple Whale complaints: inaccuracy, price, support | Small samples |
| A2-12 | https://useamp.com/pricing ; https://useamp.com/pricing.md | 2026 | Vendor pricing | Lifetimely tiers, Profit Agent gated to paid plans | Vendor; other Amp pages conflict on free tier |
| A2-13 | https://useamp.com/blog/agentic-ai-ecommerce/ | 2026 | Vendor blog | Profit Agent monitors, executes on approval | Marketing |
| A2-14 | https://www.polaranalytics.com/use-cases/shopify-revenue-autopsy | 2026 | Vendor use case | Swing tracing; Shopify-only AI can misattribute | Marketing |
| A2-15 | https://businesswire.com/news/home/20260619044302/en/Wayflyer-Acquires-Conjura-to-Accelerate-Its-AI-Product-Offering-for-Small-Businesses | 2026-06-19 | Press release | Wayflyer acquired Conjura; terms undisclosed | Primary; most coverage derivative |
| A2-16 | https://apps.shopify.com/profit-pulse-ai | 2026 | App listing | Exception queue, $19/mo, 0 reviews | Primary listing; no usage data |
| A2-17 | https://apps.shopify.com/profitgpt ; https://hypersonix.ai/blogs/silent-margin-killers-identifying-hidden-pricing-inefficiencies-with-ai | 2026 | App listing; vendor blog | Profit Max AI weekly ranked recommendations | Marketing; 0 reviews |
| A2-18 | https://help.digismoothie.com/en/articles/14686494-understanding-the-cm1-cm4-profit-waterfall | 2026 | Vendor help center | Setpilot CM1-CM4 waterfall | Tier labels inconsistent across vendor pages |
| A2-19 | https://apps.shopify.com/margin-sentinel ; https://pickyourapp.com/products/costsentry | 2026 | App listings/directory | Missing-cost, negative-margin, supplier-cost-change alerts | Micro vendors |
| A2-20 | https://www.shopify.com/enterprise/blog/sidekick-ai-questions | 2026 | Vendor blog | Sidekick recommendations by impact | No margin-specific Pulse feature found |
| A2-21 | https://www.ringly.io/blog/beprofit-alternatives | 2026 | Competitor blog | BeProfit tiers | Conflicts with GetApp |
| A2-22 | https://www.netsuite.com/portal/resource/articles/business-intelligence/netsuite-2026-2-turning-business-data-into-action-with-ai.shtml ; https://www.crowe.com/insights/netsuite-blog/netsuite-next-is-here-are-businesses-ready ; https://www.withum.com/resources/netsuite-ai-features-netsuite-next-readiness/ ; https://www.netsuite.alphabold.com/netsuite-ai-gross-margin-analysis/ | 2026 | Vendor/partner | Ask Oracle margin questions, Data Intelligence rename, AI Units | Partner marketing; no accuracy tests |
| A2-23 | https://erpresearch.com/en-us/netsuite-pricing ; https://www.vendr.com/buyer-guides/netsuite | 2026 | Aggregator | NetSuite per-user and base fees | Estimates, not Oracle list |
| A2-24 | https://www.acumatica.com/corporate-newsroom/press-releases/2026-r1-for-manufacturers-distributors-and-retailers/ | 2026-03 | Vendor press | Amazon profitability dashboards, quote margin, AI Studio | Primary |
| A2-25 | https://learn.microsoft.com/en-gb/dynamics365/business-central/sales-analytics-overview ; https://cavallo.com/profit-analytics | n/d | Vendor docs; ISV | BC sales analytics, Power BI app, Copilot | Docs primary; no reviews |
| A2-26 | https://www.odoo.com/documentation/19.0/applications/sales/sales/sales_quotations/margin.html ; https://www.cybrosys.com/blog/how-to-perform-margin-analysis-in-odoo-19 | n/d | Vendor docs; partner | Odoo margin = price minus cost; add-on limits | Docs primary |
| A2-27 | https://epicor.swoogo.com/insights2026/session/3995663/profiting-from-ai-in-3-easy-steps-how-epicor-eclipse-prophet-21-distributors-can-unlock-hidden-margin-accelerate-growth-and-win-in-ecommerce-with-sparxiq ; https://www.softwarereviews.com/vendor-technology-notes/at-insights-2026-epicor-reframes-erp-from-record-keeper-to-action-taker | 2026-05 | Conference listing; analyst note | SPARXiQ pricing leaks; cloud prerequisite | Vendor claims |
| A2-28 | https://www.g2.com/compare/cin7-core-vs-katana-cloud-inventory-vs-fishbowl-inventory ; https://www.brightpearl.com/integrations/listing/retail-analytics-conjura | 2026 | Review site; vendor | Cin7/Fishbowl/Katana reporting complaints; Brightpearl-Conjura | Aggregated ratings |
| A2-29 | https://www.sage.com/en-us/news/press-releases/2026/06/sage-helps-manufacturers-and-distributors-make-faster-more-informed-decisions-with-ai/ | 2026-06 | Vendor press | Sage X3 anomaly detection, Copilot | Marketing |
| A2-30 | https://quickbooks.intuit.com/learn-support/en-us/help-article/business-reports/ai-powered-report-insights/L2jZq6tfM_US_en_US ; https://quickbooks.intuit.com/ca/resources/product-update/intuit-intelligence-october-2026/ | 2026 | Vendor help; product update | AI P&L insights tiers; beta status | Primary |
| A2-31 | https://itbrief.news/story/xero-unveils-ai-business-health-scorecards-for-users | 2026 | Trade press | Xero analytics gross margin with AI insights | Secondary |
| A2-32 | https://apps.xero.com/us/app/fathom//reviews ; https://www.g2.com/products/spotlight-reporting/pricing | 2026 | Review/pricing pages | Fathom reviews; Spotlight pricing | Pricing conflicts |
| A2-33 | https://puzzle.io/blog/puzzle-launches-ai-suite ; https://digits.com/blog/digits-vs-puzzle/ | 2026 | Vendor | AI close, variance explanations; Puzzle acquisition claim | Acquisition claim UNVERIFIED (competitor page) |
| A2-34 | https://www.webgility.com/blog/shopify-product-bundle-quickbooks-fixes ; https://linkmybooks.com/blog/a2x-quickbooks | 2025-2026 | Competitor blogs | A2X/LMB COGS dependence, bundles, payouts | Biased |
| A2-35 | https://dupple.com/learn/best-ai-inventory-forecasting-tools ; https://www.capterra.com/p/152724/NETSTOCK/ | 2026 | Directory/blog | Prediko, Cogsy, Netstock, Inventory Planner pricing | Conflicting prices |
| A2-36 | https://craftybase.com/blog/shopify-stocky-discontinued | 2026 | Competitor blog | Stocky shutdown 2026-08-31 | Consistent across several sources |
| A2-37 | https://www.businesswire.com/news/home/20251103039929/en/Zilliant-Launches-Pricing-Plus-to-Help-Companies-Move-Beyond-Spreadsheets-and-Prevent-Margin-Leakage ; https://zilliant.com/press-releases/zilliant-survey-executives-are-adjusting-prices-more-than-ever-but-losing-control-of-the-outcomes ; https://datatoolindex.pages.dev/compare/pricefx-vs-vendavo/ | 2025-11; 2026-04 | Press; aggregator | Pricing Plus, MCP server, survey, vendor price floors | Vendor-commissioned survey; aggregator low quality |
| A2-38 | https://www.capterra.com/p/141678/Phocas-Software/pricing/ ; https://www.shashi.co/2026/05/phocas-at-epicor-insights-2026-when.html | 2026 | Directory; analyst blog | Phocas pricing, SKU drill-down, AI summary anecdote | Anecdotal |
| A2-39 | https://www.tellius.com/cpg/brand-performance | 2026 | Vendor page | PVM needs manual Excel models; agentic monitoring | Marketing |
| A2-40 | https://www.rfp.wiki/vendors/wisdomai ; https://siliconangle.com/2025/09/03/wisdom-ai-debuts-agentic-data-analysts-deliver-continuous-stream-business-insights/ | 2025-09; 2026-11 | Directory; trade press | WisdomAI proactive agents, no public pricing, ~40 customers | Directory low-medium |
| A2-41 | https://www.sarasanalytics.com/blog/saras-iq-vs-zenlytic | 2026 | Competitor blog | Zenlytic general-purpose, margin models built by customer | Biased |
| A2-42 | https://zebrabi.com/?p=33167 ; https://querio.ai/blogs/ai-business-intelligence-tools ; https://www.gooddata.ai/docs/cloud/ai/use-ai_assistant/key-driver-analysis/ | 2026 | Vendor docs/blogs | Power BI native visuals, key-driver caveats, pricing | Vendor-authored |
| A2-43 | https://www.anthropic.com/news/claude-for-small-business | 2026-05-13 | Vendor announcement (fragments) | QuickBooks workflows, no extra charge | Primary; no margin workflow found |
| A2-44 | https://distributionstrategy.com/report/the-state-of-distributor-profitability/ ; https://pagecrawl.io/blog/supplier-distributor-price-list-monitoring ; https://www.profitoptics.com/insights/turning-cost-increases-into-margin-protection-a-practical-guide-for-distributors | 2026 | Industry/vendor | Distributor leak causes; price-list monitoring | Vendor marketing; two-week lag figure illustrative |
| A2-45 | https://www.marginedge.com/price-alerts | 2026 | Vendor page | Invoice-based price alerts; ~$330-350/location | Pricing inconsistent |
| A2-46 | https://www.capterra.com/p/214079/BeProfit/ | 2026 | Review site | BeProfit ratings conflict | Tiny sample |

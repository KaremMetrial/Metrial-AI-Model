# 01 — Evidence-Backed Competitor Comparison (Margin Investigator reality check)

**Source:** `appendix/p2_a2_competitor_reality_check.md` (46 sources, register IDs A2-xx) plus Phase 1 files. **Evidence limit:** WebFetch was blocked for help.shopify.com, apps.shopify.com, netsuite.com, docs.oracle.com, odoo.com, vendavo.com, polaranalytics.com, learn.microsoft.com and g2.com. Everything below comes from search-result summaries; nothing was hands-on tested. "VERIFIED*" means primary text appeared inside a summary.
**Labels:** VERIFIED* / ADVERTISED / INFERRED / UNKNOWN. UNKNOWN means *not found*, never *absent*.

## 1. Verdict: differentiation is PARTIAL

Margin Investigator is differentiated only as a **combination for a specific buyer**, not on any single feature.

| Claimed differentiator | Status | Reason |
|---|---|---|
| Automatic margin driver analysis (price/cost/mix/volume) | **Not unique** | Vendavo Margin Bridge Analyzer (enterprise, ~$75K/yr floor, one comparison site); Coefficient free QuickBooks PVM template; Zebra BI/Inforiver PVM visuals in Power BI; NetSuite Ask Oracle "why did margins drop" (partner blogs); Tellius/WisdomAI (enterprise, warehouse-centric) |
| Works for SMB/distributors with no data or pricing team | **Partial / insufficient** | No SMB product found running PVM automatically on Shopify/ERP data (UNKNOWN, not proven absent) |
| Multi-system (Shopify + ERP + ledger + supplier costs) | **Partial** | Polar, Conjura, Brightpearl join store/ads/ERP; none found joining ledger + supplier-invoice evidence for distributors |
| Record-level evidence trail | **Insufficient** | SKU/order drill-down is common; a case file citing specific invoices/POs not seen. Vendavo/NetSuite AI: UNKNOWN |
| Separate confidence for observation vs explanation; counterevidence | **Unclaimed, unproven demand** | No vendor documents it for margin work; Polar's own marketing says Shopify-only AI can misattribute a swing |
| Recommended action | **Not unique** | Hypersonix, Lifetimely, Conjura, SPARXiQ, Zilliant, Phocas all recommend |
| Outcome tracking | **Partial** | Aera Decision Ledger (enterprise, Oct 2026, ADVERTISED); no SMB margin product found; decision journals are rarely maintained (Phase 1) |
| Supplier cost vs price pass-through detection | **Partial** | MarginEdge (restaurants, ~$330–350/location/month), CostSentry, Margin Sentinel (Shopify), SPARXiQ on Epicor; none joins cost + price lag + mix + volume into one explained case |

## 2. Comparison matrix (condensed; full per-vendor tables in appendix §2a–2f)

Columns: **OOB** out-of-box margin analytics · **RCA** root-cause/driver analysis · **Multi** multiple business systems · **Trace** evidence/traceability · **CE/Unc** counterevidence/uncertainty · **Rec** recommends actions · **Track** tracks outcomes.

| Competitor (segment) | OOB | RCA | Multi | Trace | CE/Unc | Rec | Track | Price (public?) | Notable complaints/limits |
|---|---|---|---|---|---|---|---|---|---|
| **NetSuite** SuiteAnalytics / Data Intelligence / Ask Oracle (mid-market) | ADV | ADV ("why did margins drop"; method UNKNOWN) | Own ERP + warehouse | UNK | UNK | ADV | UNK | ~$129–199/user/mo + base fee (estimates); AI metered ("AI Units") | Partner blogs: standard P&L shows margin fell, not why; AI cost metering |
| **Acumatica** | V* Amazon profitability dashboards | UNK | In-suite | UNK | UNK | ADV | UNK | Not public | Not found |
| **Odoo 19** | V* margin = price − cost; Sales Margin report | No PVM found | Own suite | Drill (INF) | UNK | UNK | UNK | Per user | Margins depend on manually entered cost fields |
| **Business Central** | V* sales analytics, Copilot over views | Partial (Q&A; no native PVM found) | Via Power BI | Drill | UNK | UNK | UNK | Per user + Copilot capacity | No independent margin-AI reviews |
| **Epicor P21/Eclipse + SPARXiQ** (distributors) | ADV leak analytics | ADV (bridge UNK) | Epicor only | UNK | UNK | ADV | UNK | Not public; vendor claims 200–400 bps | Not found |
| **Shopify native / Sidekick Pulse** | V* gross profit = sales − static per-item COGS (excludes fees/shipping/ads) | No decomposition found | Shopify only | Order-level | UNK | ADV (≤5 recs) | UNK | Included | Cost static in time; gross not net |
| **TrueProfit** | V* P&L, ads, COGS sync | No PVM found | Shopify + ads | Order/product | UNK | UNK | UNK | $35–$200 by orders (listing, via search) | Overage in busy months; occasional sync lag |
| **Lifetimely (Amp)** | ADV daily P&L, contribution margin | UNK | Shopify, ads, Amazon | UNK | UNK | ADV (Profit Agent; acts on approval) | UNK | Free <50 orders; from $49 | Narrower than suites |
| **Polar Analytics** | ADV contribution margin, "revenue autopsy" | ADV | Shopify, ads, finance | UNK | ADV (says Shopify-only AI can misattribute) | UNK | UNK | Not retrieved | Not found |
| **Triple Whale** | ADV net profit | Critics: weak margin view (competitor blogs) | Shopify, ads | UNK | UNK | ADV | UNK | ~$219/mo+ (competitor pages) | Data accuracy, price, support (small samples) |
| **Conjura** (Wayflyer, acquired 2026-06-19) | V* SKU contribution profit | PVM UNK | Store, ads, ERP, marketplaces | SKU | UNK | ADV | UNK | Free / custom | Roadmap may shift to financing (INF) |
| **Profit Pulse AI** | V* exception queue (negative margin, missing COGS, discount leakage) | No (rule-based, INF) | Shopify | Order | UNK | Queue | UNK | **$19/mo** | 0 reviews |
| **Hypersonix Profit Max AI** | ADV weekly ranked recs | Partial/UNK | Shopify | Variant | UNK | ADV | UNK | Free listing; vendor lift claims conflict | 0 reviews |
| **CostSentry / Margin Sentinel** | ADV supplier-cost-change alerts, margin floors | No | Shopify + CSV | Variant | UNK | Alerts | UNK | Free tier; paid tiers | Vendor pages only |
| **QuickBooks (AI report insights, Intuit Intelligence)** | V* anomalies on P&L/Balance Sheet (Plus/Advanced) | Partial (P&L-level; product margin UNK) | QuickBooks | UNK | UNK | ADV (next steps with confirmation) | UNK | In subscription | Beta limits; no independent product-margin test |
| **Xero (Analytics, JAX)** | ADV gross-margin overview with AI insights | UNK | Xero | UNK | UNK | ADV | UNK | In subscription | Not found |
| **Fathom / Syft / Spotlight** | ADV management reporting | No PVM found | Accounting only | Ledger drill (INF) | UNK | UNK | UNK | Fathom ≈ $50+ (conflicting); ≈ $18/client at 25-client tier | Steep learning curve, report locking (Xero App Store reviews) |
| **Puzzle / Digits** | ADV AI close, variance text | Partial (vendor) | Accounting | UNK | ADV human review | UNK | UNK | Not researched | Puzzle acquisition claim unverified |
| **Phocas** (distributor BI) | ADV margin analysis, rebates, drill to negative-margin SKUs | Partial (drill + narrative; no PVM documented) | ERP + others | SKU drill | UNK | ADV | UNK | Not public ($150/mo listing-site figure) | Not found |
| **Vendavo** (Margin Bridge Analyzer) | ADV PVM + cost effect, tariff early warning | ADV | Enterprise ERP feeds | UNK | UNK | ADV | UNK | ~$75K/yr floor (single site) | No independent reviews |
| **Zilliant / Pricefx / PROS** | ADV price waterfall, pricing analytics | Partial/UNK | ERP | UNK | UNK | ADV | UNK | Not public; Pricefx ≈ $50K/yr floor (comparison site) | Deployment 4–12 months (conflicting) |
| **Cogsy / Prediko / Inventory Planner / Netstock** | ADV forecasting | No margin RCA found | Shopify/ERP | n/a | UNK | Reorder recs | UNK | $49–$199 DTC; Netstock ≈ $900/mo | Not retrieved |
| **Power BI / Tableau / Looker / ThoughtSpot** | Key Influencers, Decomposition Tree; PVM DIY | Partial (statistical, not causal) | Many | Drill | UNK | No | No | Pro $14/user/mo | Needs a model builder |
| **Tellius / WisdomAI** (AI-native) | ADV driver analysis / RCA | ADV | Warehouse | SQL shown (Wisdom) | Independent: narratives need analyst validation (Tellius) | ADV | UNK | Not public; "expensive" (G2) | Enterprise, warehouse prerequisite |
| **Claude for Small Business** | ADV 15 workflows; no margin workflow found | On demand | QuickBooks, PayPal, HubSpot… | Per connector | User-dependent | Queues for approval | UNK | Claude licence only | Not found |
| **Aera / Celonis / Peak / Palantir** | Enterprise | — | — | — | — | — | Aera Decision Ledger only analog | Not public | Irrelevant for SMB (INF) |

## 3. Closest to the wedge, and what they do not (or are not known to) do
1. **Vendavo** — closest functionally (PVM + cost + early warning). Not SMB; long deployment; evidence/uncertainty/outcomes UNKNOWN.
2. **NetSuite Ask Oracle / Data Intelligence** — closest ERP-native, NetSuite customers only; accuracy UNKNOWN. A one-hour trial would resolve whether it produces evidence-linked decompositions.
3. **Hypersonix, Polar, Lifetimely, Conjura** — closest SMB Shopify; recommendations yes, documented counterevidence/confidence/outcome tracking no; non-Shopify ERP/ledger depth UNKNOWN.
4. **Phocas + SPARXiQ on Epicor** — closest distributor stack; human-led, no documented bridge.
5. **Tellius / WisdomAI** — closest AI-native RCA; warehouse-centric, enterprise.

## 4. Contradictory evidence the founder must weigh
- **Against:** $19 exception queue; free PVM template; NetSuite "why did margins drop"; QuickBooks/Xero embedded AI; prompt-based substitutes; consolidation (Conjura → Wayflyer).
- **For:** even enterprise vendors concede PVM is manual or fragile (unit consistency, returns, discontinued SKUs); partner blogs say standard ERP reports show *what*, not *why*; cheap Shopify apps flag but do not decompose; nobody documents calibrated/counterevidence-based explanation.
- **Unresolved:** whether NetSuite Ask Oracle, Hypersonix and Polar agents actually produce evidence-linked decompositions.

## 5. What would upgrade the verdict to SUPPORTED
1. A blind test where owners prefer a Margin Investigator case file over NetSuite Ask Oracle, Polar's agent, or a Claude/QuickBooks prompt on the same data.
2. A segment where **no** vendor AI explainer exists (QuickBooks, Xero, Odoo, Acumatica, Business Central, Cin7 distributors).
3. Evidence that buyers pay for uncertainty and outcome tracking, not just the explanation.

## 6. Corrections to Phase 1 agents
Conjura acquired (2026-06-19); Stocky shut down (2026-08-31); Zenlytic's DTC fit UNKNOWN (only a rival's blog); NetSuite now partly covered (Ask Oracle); Puzzle "acquired by Accrual" unverified; Peak price ($38.1M vs ~$115M raised) unresolved.

## 7. Follow-up access needed
Allowlist help.shopify.com, apps.shopify.com, apps.xero.com, vendavo.com, docs.oracle.com/netsuite, polaranalytics.com, useamp.com, g2.com; run 30–60-minute trials of NetSuite Ask Oracle, Polar, Lifetimely, Hypersonix.

# Phase 2 — Executive Decision Report

**Date:** 2026-11-19 · **Status:** research and decision only. No code, no integrations, no customer interviews have been run. Nothing here claims customer validation.
**Supersedes nothing:** Phase 1 (`research/00_founder_research_report.md`) is untouched. Where Phase 2 contradicts Phase 1, this report says so.

---

## 1. The decision

**Outcome C (as refined below): do not build any of the researched opportunities yet. Run a 30-day paid diagnostic experiment first, and let its pre-registered results choose between Margin Investigator, a cash/AR module, or stopping.**

This is not "more research". It is a specific, cheap, falsifiable investment decision:

| | |
|---|---|
| **What you commit now** | ~120–150 founder-hours over 30 days and under ~$500 cash [ASSUMPTION]. Zero production code. |
| **What you do not commit** | Engineering months, an integration build, an app-store listing, SOC 2, a platform architecture. |
| **What the test sells** | A paid, human-assisted "Profit & Cash Leak Audit" for Shopify + QuickBooks/Xero businesses (one-time fee, charged up front). It reads the same data connection for three candidate modules (margin bridge, late-AR/cash, payout reconciliation) and records which one buyers value and pay for. |
| **What it decides** | A: Margin Investigator is confirmed. B: a different first module (most likely cash/AR) wins. Or stop. Thresholds are in `07_30_day_validation_plan.md` and `08_risks_assumptions_kill_criteria.md`. |

**Margin Investigator is demoted from "recommendation" to "lead hypothesis".** After this research it is not the strongest-evidenced opportunity; it is one of three plausible ones and none has the evidence a build decision needs.

## 2. Why this outcome (and why not A or B right now)

### The one finding that drives everything
**Nobody in any of the researched categories has been shown to pay for an *explanation* product.** Every priced comparable sells one of three things: *visibility* ($19–$300/month Shopify profit apps), *sync/automation* (A2X, Link My Books, Chaser), or *recovery* on contingency (parcel audit 25–50%, deductions, FBA reimbursement 10–25%, AP audit 13.5–25%). The middle product — "tell me why, with evidence, and follow up" at $349–$999/month — has no named paying small-company customer in anything found (`appendix/p2_a1`, `p2_a3a`, `p2_a3b`).

### Why not A (proceed with Margin Investigator)
1. **Willingness to pay is rated INSUFFICIENT** for a separate $349–$999 product; overall problem-supports-product rating is **WEAK** (Agent 1). The problem is real and documented (NAW/MDM, Distribution Strategy Group), but mostly by trade bodies and consultancies who sell services.
2. **The differentiation verdict is PARTIAL** (Agent 2). Every individual element has a substitute: a $19 Shopify "margin exception queue" (Profit Pulse AI), free PVM spreadsheets (Coefficient, Zebra BI), NetSuite "Ask Oracle" pitched for "why did margins drop", enterprise Vendavo Margin Bridge, Phocas margin drill-down for distributors, QuickBooks/Xero AI insights, Claude for Small Business. Only the *combination* (cross-system, record-level evidence, honest uncertainty, follow-up) is undocumented — and undocumented is not the same as demanded.
3. **The behavior contradicts the premise.** 91% of distributors raise prices when costs rise; 45% say they pass through all increases and 45% most (Baird-NAW 2Q26; DSG Q4 2026 — trade surveys seen only as summaries). The product's trigger ("cost rose, price didn't") may be rarer than Phase 1 assumed, or may be exactly what they don't know — the sources cannot say which.
4. **ICP and price point pull in opposite directions** (Agent 4): the segment easiest to reach by inbound (Shopify-first brands) has the lowest price ceiling ($49–750/month); the segment that could pay $900+ (distributors) is the hardest to reach inbound and needs interviews and referrals.
5. **Data feasibility is only AMBER-GREEN** (Agent 5): the revenue-side bridge is easy; *true* margin needs cost data that Shopify stores as optional, current-value-only `unitCost` and that QuickBooks/Xero rarely hold at SKU level.

### Why not B (select a different product now)
No alternative has better evidence for *the thing that matters*.
- **Cash flow + AR prioritization** scores highest in my weighted framework (77/100) because data access is the easiest (GREEN), onboarding is hours not days, accuracy tolerance is good, and usage is weekly. But it is crowded (Float, Fathom, Chaser ~$259/month, Upflow) and is exactly what Intuit and Xero are bundling into plans. Its high score reflects *ease*, not a business case. It is the strongest challenger, not a proven winner.
- **Churn/revenue risk** (72) is a billing-first, probabilistic problem with good accuracy tolerance, but the SaaS segment builds in-house and is the most crowded (Baremetrics, ChartMogul, Churnkey ~$250).
- **Reconciliation** (65) has the best proof of payment (A2X/Link My Books) but demands cent-level accuracy and is crowded and edge-case-heavy.
- **Recovery products** (freight audit, deductions, FBA reimbursement) have the strongest proof of payment of all — and are saturated, contingency-priced, and decaying (a company that built its own audit agent with off-the-shelf AI saw recoveries fall below $40K from $400K).
- The ranking is **not stable**. Doubling the weight on willingness-to-pay promotes recovery categories; ignoring it promotes Margin to a near tie with Cash/AR (73.5 vs 73.9). That instability is the finding: desk research cannot pick a winner.

### Why C, positively
- The unresolved question (does anyone pay for an explanation?) is **cheap to test with money, not engineering**. A paid manual audit costs founder time; a build costs months.
- The same Shopify + QuickBooks/Xero data connection serves the top three candidates on data feasibility (C2 cash/AR GREEN, C1 margin AMBER-GREEN, C3 reconciliation AMBER). One audit can test pull across all three.
- It is a true first step toward Company Intelligence: the audit produces the labeled cases, entity maps and outcome records that any later module needs.

## 3. Answers to the ten Margin Investigator revalidation questions (short form; evidence in `appendix/p2_a1`)

1. **Frequency:** supplier cost shocks were severe in 2025–26 (NAW/MDM: 62% expected COGS up 10%+; one-third faced 25%+ hikes); Baird-NAW 2Q26 says 91% raise prices. Margin pressure is frequent; *unexplained* erosion frequency is **unknown**. [TRADE; summaries only]
2. **How discovered/investigated:** month-end close, spreadsheets (Vendavo/Copperberg: 85% of manufacturers and distributors rely on them), consultants. [VENDOR]
3. **Tools:** ERP reports, Excel, Phocas (distribution BI), Shopify profit apps, QuickBooks/Xero.
4. **Done well:** visibility and drill-down to customer/SKU; contribution-margin P&L; supplier-cost-change alerts in narrow slices.
5. **Still hard:** joining cost change + price lag + mix + volume across systems into one explained, traceable case; requires clean cost data and often a pricing/finance analyst.
6. **Who feels it:** owner/CFO/controller; sales-ops/pricing lead for distributors.
7. **Who owns budget:** owner or CFO signs below ~$30M; pricing is often sales-owned while finance holds the budget. No budget-owner survey exists for small firms. [GAP]
8. **Impact:** consultancy/trade estimates of 100–300 bps (DSG), 3–5% revenue leak (DSG/Cavallo); 0.5 pt of margin on $20M = $100K (arithmetic). All sponsor-biased.
9. **Urgency:** tariffs and supplier hikes (strongest; may fade — unverified), lender covenants/PE/ERP migration (no evidence retrieved).
10. **Evidence of paying for a separate product:** cheap end ($35–$300 Shopify apps) and enterprise end ($75K–$200K pricing suites) only. **None at $349–$999 for $5–50M firms.**

## 4. What changed versus Phase 1

| Phase 1 claim | Phase 2 finding |
|---|---|
| Specialty distributors / DTC-plus-wholesale brands are the ICP | **Not validated.** No segment is both easy to reach inbound and able to pay the required price (Agent 4). |
| Margin Investigator is the wedge | Differentiation **PARTIAL**; willingness to pay **INSUFFICIENT**; demoted to lead hypothesis. |
| NetSuite status unverified | Ask Oracle ("why did margins drop") and NetSuite Data Intelligence now exist (partner blogs; accuracy untested). |
| Advisor channel (Strategy B) is promising | Reach is real (94% of US accounting firms offer advisory) but price evidence is weak (Fathom ≈ $18/client/month at scale) and bookkeepers want fewer tools. |
| Cross-tenant priors as a moat | **Xero's developer terms reportedly prohibit training AI/ML on API data** (single search summary; verify) — a gating risk if Xero is the first stack. |
| Conjura / Stocky as competitors | Conjura acquired by Wayflyer (2026-06-19); Stocky shut down (2026-08-31). |
| Inbound can supply early users | Marketplace listings are conversion surfaces, not lead sources; SEO demand for the problem is **unmeasured**; first accountants and any distributor test require direct outreach. |

## 5. Evidence that supports the recommendation / evidence that is missing

**Supports:** the WTP gap is consistent across three independent agents (1, 3A, 3B); competitor matrix finds no documented calibrated-confidence/outcome-tracking for margin work (an *unclaimed* gap); data feasibility shows one connection serves three modules; paid-memo test is the cheapest instrument that could disprove the idea.

**Missing (do not pretend otherwise):**
- **No customer interviews, no customer quotes, no primary Reddit/HN threads** were obtained. Every research agent was blocked from most primary pages and Reddit; all evidence is from search-result summaries. The "voice of customer" gap from Phase 1 is **not closed**.
- Census/SUSB firm counts by NAICS and size, Shopify merchant counts by revenue band, keyword demand volumes, the full Baird-NAW/MDM survey, primary API terms (Shopify, Xero, Intuit), and hands-on trials of NetSuite Ask Oracle, Polar, Lifetimely, Hypersonix.
- Whether anyone grants read-only access to an unknown vendor.

## 6. Main risks and what could invalidate this recommendation

- **The test itself is biased.** A free-tool/inbound funnel skews to Shopify brands (lowest price ceiling); distributors need parallel interview-led tests. n=15 can falsify but not prove.
- **Concierge ≠ product.** If buyers pay for a human analyst's judgment, the business is consulting; scaling it requires the automation to match that judgment (tested via blind comparison and accuracy on confirmed cases).
- **Platform absorption:** Intuit, Xero, Shopify, NetSuite and Anthropic are all shipping "what's wrong" features; the window may close in two quarters.
- **Invalidators of C itself:** if 5+ of the first 10 conversations show owners already satisfied with free in-product tools, stop early; if ≥4 of 15 qualified prospects *pay* for margin findings, the recommendation upgrades to A without further delay.

## 7. Next documents
`01` competitors · `02` opportunities · `03` ICP/buyer · `04` data feasibility · `05` product/MVP · `06` pricing · `07` 30-day plan · `08` risks/kill criteria · `09` final recommendation · `10` source register · `appendix/` raw agent reports.

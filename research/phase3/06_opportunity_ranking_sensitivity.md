# 06 — Opportunity Ranking and Sensitivity

**Code:** `appendix/p3_ranking_lenses.py` (and the skeptic's `appendix/p3_a5_rank_stability.py`). **All scores are judgment informed by sourced facts; the Phase 3 adjustments are listed below and are also judgment.** Rankings are an organising device, not a measurement. Where sources are search snippets the score inherits that weakness.

## 1. What changed from Phase 2's scores

| Opportunity | Criterion | Phase 2 | Phase 3 | Reason |
|---|---|---|---|---|
| Cash flow | Openness | 2 | **1** | Claude SMB cash forecast + invoice chaser (primary), Intuit/Xero forecasting bundled |
| Cash flow | WTP | 3.5 | **3** | A free bundled substitute lowers the price ceiling |
| Late AR | Openness | 2 | **1** | Claude `invoice-chase`, Intuit Payments agent, Chaser, Upflow |
| Reconciliation | Openness | 2 | **1.5** | Claude `close-month` reconciles ledger vs Shopify/Stripe/PayPal |
| Margin | Openness | 3 | **2.5** | Analyzer named; QuickBooks AI insights; Polar marketing |
| Margin | Data | 4 | **3.5** | Cost data is the blocker; "current-only `unitCost`" is a testable assumption |
| Margin | Expansion | 5 | **4** | Breadth asserted, never demonstrated |
| Churn | Expansion | 5 | **4** | Same |
Added rows: **Late AR / collections prioritisation** as its own row (Phase 2 had merged it with cash flow); **Operational bottlenecks**; **Distributor price-cost leakage (ERP, interview-led)** to separate the Shopify margin product from the distributor version.

## 2. The ten criteria and the eight weighting "lenses"
Criteria: willingness-to-pay evidence, dollar impact/measurability, pain severity, competitive openness, data accessibility/integration ease, time-to-value, accuracy tolerance, recurring usage, expansion into Company Intelligence, inbound reachability.

| Lens | Purpose | Heaviest weights |
|---|---|---|
| L0 Phase-2 weights | Baseline | WTP 20, $ 12, open 12, data 12 |
| L1 **Best business** | Value and defensibility | WTP 25, open 20, $ 15, expansion 10 |
| L2 **Easiest to build** | Tiny backend team | data 40, TTV 25, accuracy 25 |
| L3 **Easiest to validate** | Weeks, not months | data 25, TTV 25, inbound 15 |
| L4 **Most recurring** | Retention | recurring 30, WTP 20 |
| L5 **Entry to Company Intelligence** | Platform path | expansion 35, $ 10, open 10 |
| L6 WTP ignored, openness doubled | Phase 2's near-tie case | open 24 |
| L7 WTP doubled | WTP emphasis | WTP 40 |

## 3. Results (top four per lens; Phase-3 adjusted scores)

| Lens | #1 | #2 | #3 | #4 |
|---|---|---|---|---|
| L0 Phase-2 weights | Late AR 78.0 | Cash flow 72.8 | Churn 70.4 | **Margin 64.4** |
| L1 Best business | Late AR 70.4 | **Distributor price-cost 68.9** | Churn 68.4 | Procurement 64.8 |
| L2 Easiest to build | Late AR 93.0 | Cash flow 93.0 | Churn 72.0 | Margin 69.0 |
| L3 Easiest to validate | Late AR 90.0 | Cash flow 87.5 | Churn 75.0 | Margin 68.5 |
| L4 Most recurring | Late AR 82.0 | Cash flow 77.0 | Reconciliation 74.0 | Churn 73.0 |
| L5 Entry to Company Intelligence | Late AR 79.0 | Cash flow 77.0 | **Distributor price-cost 76.0** | Churn 74.0 |
| L6 WTP ignored | Late AR 70.0 | Churn 68.7 | Cash flow 68.7 | Margin 67.8 |
| L7 WTP ×2 | Late AR 78.3 | Cash flow 70.7 | Churn 68.7 | Reconciliation 66.3 |

**Stability (5,000 flat-Dirichlet weight vectors, adjusted scores): P(top-1) / P(top-3)**

| Opportunity | Top-1 | Top-3 |
|---|---|---|
| Late AR / collections prioritisation | **0.86** | 0.96 |
| Cash flow investigation | 0.00 | 0.89 |
| Churn / revenue risk (billing-first) | 0.09 | 0.88 |
| Distributor price-cost leakage | 0.04 | 0.12 |
| Procurement / supplier price-creep | 0.01 | 0.04 |
| **Margin / price-cost (Shopify + ledger)** | **0.00** | **0.05** |
| Reconciliation | 0.00 | 0.05 |
(The unadjusted Phase-2 scores give margin P(top-1) 0.02, P(top-3) 0.22; the Claude-related adjustments lower it further.) Removing the ease criteria (data, time-to-value, accuracy tolerance) from the baseline weights leaves Late AR 71.9, Churn 70.3, **Distributor price-cost 68.6**, Reconciliation 68.1, Procurement 65.4, Cash flow 64.9: the ordering among the top five becomes close.

## 4. What the ranking says — and does not say

1. **The ranking is not unstable. It is stable and mis-targeted.** Late-AR/cash leads in nearly every weighting, but its lead is built mostly on *ease* (data GREEN, onboarding in hours, forgiving accuracy, weekly use). Phase 2's headline claim that the ranking could not pick a winner was wrong.
2. **Easiest to build and validate ≠ best business.** Late-AR/cash is the easiest module to build and test and the one most directly covered by free tools: Claude's invoice chaser and cash forecast, Intuit's Payments agent and forecasting, Xero Analytics Plus, Upflow, Chaser. Its high score overstates its business quality. The documented gap (explaining *why* past cash or DSO changed) is narrow and platform-closable.
3. **Margin is a distant third on these scores** and falls further once Claude's margin analyzer, QuickBooks insights and Polar's explanation feature are counted. It stays interesting for two reasons that are *not* in the scores: (a) a margin bridge draws on price, cost, supplier, discount, freight and returns data, so it is the broadest on-ramp to a Company Intelligence model; (b) at larger ACV in distribution, it is less obviously covered by free SMB tools.
4. **The best-business question is genuinely open.** Under lens L1, Late-AR, Distributor price-cost leakage and Churn sit within 2.5 points of each other: a three-way tie that desk evidence cannot break. The distributor version scores well on dollar impact and openness but badly on data access, onboarding time and inbound reach, and its demand evidence is the weakest in the file (sponsor-authored, mismatched population, pass-through surveys that cut both ways).
5. **Recurring revenue:** Late-AR/cash and reconciliation have the most natural weekly/monthly cadence; margin and churn recur only if the Brief is valued.
6. **Best entry to the platform:** a margin/price-cost model touches the most entities (SKU, supplier, customer, channel, price list, shipment); cash/AR touches customers, invoices, payments and bills. A margin entry builds more reusable structure; a cash/AR entry is faster and more crowded. See `07`.

## 5. Ranked views the founder asked for

| Question | Answer (with confidence) |
|---|---|
| **Best business opportunity** | **Undetermined** — a three-way tie (Late AR, distributor price-cost leakage, churn) with no willingness-to-pay evidence for any. Low confidence |
| **Easiest to validate** | **Late-AR / cash** (data GREEN, hours to onboard, weekly use). High confidence |
| **Easiest to build** | **Late-AR / cash**, then reconciliation-light and churn-bridge versions. High confidence |
| **Most likely recurring revenue** | **Late-AR / cash**, **reconciliation**. Medium confidence — and the same categories most bundled for free |
| **Best long-term entry into Company Intelligence** | **Margin / price-cost family** (breadth), with cash/AR as the second module. Medium confidence; breadth is asserted, not demonstrated |

## 6. Specific opportunities the committee was asked to reassess

| Opportunity | Phase 3 assessment |
|---|---|
| **Margin Investigator** | Third on most lenses; weakest WTP evidence; most differentiated *if* an evidence layer is valued; risk of repackaging per `02`. Keep as the platform-aligned hypothesis, not the front-runner |
| **Cash-flow investigation** | Easiest; now largely covered by free tools; documented gap = explaining *past* cash change; weak differentiation |
| **Late accounts receivable** | Top on ease/recurring; Claude's invoice-chase explicitly lacks DSO analysis; Chaser/Upflow own the workflow; WTP exists for chasing, not for explanation |
| **Inventory anomalies** | Valuable, but the movement ledger sits in ERP/WMS behind admin gates; Claude's inventory planner needs unit cost; low scores on data and TTV; Stocky shutdown leaves a native-tool gap (unverified need) |
| **Procurement and supplier investigation** | High openness and expansion; data are the problem (SKU-level line items rarely in SMB ledgers; PDFs); no paying-customer evidence |
| **Revenue leakage** | Lowest total: the "should-have-billed" ground truth is bespoke; services-heavy; no named buyer |
| **Operational bottlenecks** | Weak: hard 3PL data, weak WTP, WMS bundled dashboards |
| **Any stronger opportunity** | **None supported by evidence.** Two *hypotheses* surfaced (below) |

## 7. Two hypotheses that came out of the review (untested, no market evidence)
- **H-1: the investigation engine as a connector/plugin inside the AI tools owners already use.** The Claude Small Business plugin documents its own gaps (no past-cash causation, no DSO analysis, no margin in the pulse, margin/COGS left to the owner). A deterministic evidence layer (price/cost/mix bridges, aging, coverage, row lineage, abstention) delivered as an MCP server or skill could be sold *into* that distribution channel, which is the inbound channel this team wants. Risks: platform dependency, thin moat, easy for the platform to copy, unknown marketplace economics. **Gate 0 Arm 3 tests the technical half of this.**
- **H-2: distributor price-cost leakage via ERP resellers.** Higher ACV, less covered by free SMB tools, but the evidence base is sponsor-authored and mismatched to the target size, and reach requires introductions.

## 8. Sensitivity of this review itself
The adjustments in §1 are my judgment. Using the *unadjusted* Phase-2 scores gives the same top three and the same conclusion (Late AR first in 86% of draws). Using the skeptic's alternative adjustments (margin WTP → 1; expansion 5 → 3) widens the gap further. No defensible adjustment I tried makes margin the top-ranked opportunity on these ten criteria.

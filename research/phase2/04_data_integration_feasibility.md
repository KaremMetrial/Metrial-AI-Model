# 04 — Data and Integration Feasibility

**Source:** `appendix/p2_a5_data_feasibility.md` (25-row register, A5-xx). **Evidence limit:** direct fetches of shopify.dev, developer.xero.com, developer.intuit.com failed; everything is search-summary tagged SS-P (summary of a primary vendor host), SS-S (secondary, often competitor-authored) or PK (prior knowledge). Not found: Shopify rate limits, QBO/Xero rate limits and history depth, Stripe read-only scopes, Business Central/Acumatica details, carrier invoice APIs, bank-feed vendors, unified-API data-depth limits. **Hour estimates are assumptions.**

## 1. Ranking for a tiny strong-backend team (data feasibility only)

| Rank | Candidate | Rating | Reason |
|---|---|---|---|
| 1 | Cash flow / late AR | **GREEN** | QBO/Xero invoice, bill, payment objects are native, documented, read-only; aging/DSO is arithmetic |
| 2 | Margin erosion (revenue-side bridge first) | **AMBER-GREEN** | Shopify orders/discounts/refunds/fees accessible; deterministic bridge; **cost completeness and 60-day history are the gates** |
| 3 | Payout reconciliation (single-platform wedge) | AMBER | Payout-to-order links exist; heavy edge-case depth; high accuracy bar |
| 4 | Churn / revenue risk (NRR-bridge version) | AMBER | Stripe easy; prediction needs volume and labels |
| 5 | Inventory anomalies | AMBER-RED | Movement ledger lives in ERP/WMS, admin- and plan-gated (Odoo external API not on Free/Standard) |
| 6 | Freight / 3PL leakage | AMBER-RED | Invoice line items and rate cards are off-API |
| 7 | Revenue leakage / billing | AMBER-RED | "Should-have-billed" ground truth is bespoke |
| 8 | Supplier pass-through | RED-AMBER | SKU-level line items missing in SMB ledgers; PDF-heavy |

## 2. Per-system access facts (tagged; verify against primaries)

- **Shopify (Admin GraphQL):** orders default to **60 days** unless Shopify approves `read_all_orders`; order data is protected customer data; `unitCost` is optional and **current-value only** (no cost-at-sale on line items); payouts/balance transactions available for Shopify Payments merchants; legacy custom-app creation closed 2026-01-01; public-app review 2 weeks to 4+ months in 2026 forum reports. [SS-P/SS-S]
- **QuickBooks Online:** production keys need an app-assessment questionnaire; partner tiers priced as above; overage rates conflict between sources; inventory valuation only if the inventory module is used. [SS-P/SS-S]
- **Xero:** 2026-03-02 connection tiers (Starter 5, Core 50, Plus 1,000, Advanced 10,000), egress metering, granular `.read` scopes; prices/limits conflict between sources; terms reportedly bar AI/ML training on API data. [SS-P/SS-S]
- **Amazon SP-API:** settlement reports go back ~90 days. **Odoo:** external API not on Free/Standard; API keys max 3-month lifetime. **Stripe:** payout reconciliation and balance transactions available; read-only key scopes not found.
- **Unified APIs:** useful only for the accounting leg. Merge ≈ $650/mo for 10 linked accounts; Apideck ≈ $599/mo for 25 consumers; Unified.to from ≈ $750/mo; Codat and Rutter quote-only with high commercial minimums (≈ $18K/yr median for Rutter, via Vendr as cited by a competitor). All pricing from competitor-authored sources. **Data-depth limits per vendor were not found; sandbox-test before choosing.** Normalized models flatten exactly the detail margin/reconciliation need (unit cost, payout detail).
- **Recommended plumbing (consistent with Phase 1):** Nango + dlt for Shopify, Stripe and one accounting system; unified API only as a stopgap for the accounting leg.

## 3. Strongest three, in detail

### C2 — Cash flow / late AR (GREEN)
- **Data:** invoices (open/paid/due), payments, credit notes, bills, bank balances. Read-only; no data team needed.
- **Deterministic:** aging buckets, DSO, collection effectiveness, per-customer payment-behavior stats, forecast roll-forward.
- **History:** 12 months for behavior baselines; event alerts need less.
- **Where data lies:** invoices marked paid by journal or bank-rec timing; credit notes/prepayments/overpayments; customers with several legal entities; billing outside the ledger (spreadsheets).
- **Onboarding:** ~1–2 days to trusted first insight (assumption).

### C1 — Margin (AMBER-GREEN)
- **Data:** orders, line items, discounts, refunds, fees (Shopify Payments only), product cost, shipping cost, ad spend, returns.
- **Deterministic core:** price-volume-mix and margin bridge, discount/refund/fee leakage. No LLM computes numbers.
- **The gate:** reliable cost. Show **"margin confidence = % of revenue with known cost"** — turn the data gap into a feature.
- **History:** 12–24 months for seasonality; 3–6 months enough for a two-period bridge if costs exist. 60-day Shopify default forces a custom-app or `read_all_orders` path for history.
- **Onboarding:** ~3–5 days elapsed; 10–28 human hours (assumption), 2× for the first 3–5 design customers.
- **Validation step before any build:** measure cost-per-item completeness on a 10-merchant sample.

### C3 — Reconciliation (AMBER)
- Payout-to-order links exist (Shopify Payments, Stripe); matching is deterministic; AI only suggests rules and explains unmatched items. Edge cases: gift cards, partial refunds, holdbacks, FX, bundles, manual journals netting fees. **Finance users will not tolerate false matches** — accuracy bar is the cost. Narrow to one platform.

## 4. Deterministic vs AI

**Must be deterministic code, never LLM-computed:** PVM and margin bridges, matching/tolerance logic, aging/DSO, variance, FX, unit-cost lookup, any displayed number.
**AI appropriate for:** proposing hypotheses from decomposition results, ranking which dimension to inspect, drafting narrative, suggesting mapping rules (confirmed by checks), plain-language explanations of unmatched items, low-stakes classification with confidence labels.

**Where AI would mislead on this data:**
- treating missing COGS as zero, or applying today's `unitCost` to historical sales, and narrating a "margin collapse" that is a data artifact;
- explaining a cash dip as "customers paying later" when invoices were booked after payment, a manual journal exists, or a sync window failed;
- presenting temporal coincidence (promo started, margin fell) as cause, confounded by mix, seasonality and shipping rates;
- hallucinated SKU/customer equivalences across systems;
- silent truncation (Shopify 60-day, Amazon 90-day) producing confident analysis over partial history;
- averaging across currencies or accounting policies; smoothing over unreconciled residuals ("other").

**Evidence the interface must show:** (1) per-number lineage with source system, object IDs, sync timestamp and a **coverage badge** ("cost known for 62% of revenue", "history from 2026-03-01"); (2) reconciliation of derived totals to the system's own report within tolerance; (3) evidence grade per explanation — arithmetic identity > decomposition attribution > temporal coincidence > correlation > LLM-suggested; (4) the unexplained residual, never hidden; (5) one-click "show me the rows"; (6) assumptions list (e.g., current cost applied to historical sales).

## 5. Onboarding hours and maintenance

| Candidate | Connect + first sync | Mapping/validation | Customer cleanup | Time to trusted first insight |
|---|---|---|---|---|
| Cash/AR (QBO or Xero) | 1–2 h | 2–4 h | 2–6 h | ~1–2 days |
| Margin (Shopify + QBO/Xero) | 2–4 h | 4–8 h | 4–16 h | ~3–5 days |
| Reconciliation (one platform) | 3–6 h | 8–16 h | 8–24 h | ~1–2 weeks |
| Churn (Stripe, bridge) | 1–2 h | 4–8 h | 4–12 h | ~2–4 days |
| Inventory | 4–8 h | 8–16 h | 8–24 h | ~1–3 weeks |

All ASSUMPTION; first 3–5 design customers ≈ 2×. Anchor: Phase 1 recommends planning 2–4 weeks to a human-validated model.

**Maintenance:** API changes observed in ~12 months across these searches — Shopify legacy-app end (2026-01-01) and quarterly API versions; Xero tiering (2026-03-02) and scope migration (deadline ~Sept 2027); Intuit partner tiers/credits; Amazon report deprecations; Odoo key lifetimes. Estimate **~1 engineer-week per source per quarter** [ASSUMPTION]. Plan a freshness/coverage monitor as part of the product, reconnect UX for token expiry, and per-tenant metering for Xero egress/Intuit credits.

## 6. Cheap validation steps before committing
1. 10-merchant sample: Shopify cost-per-item completeness and shipping-cost availability.
2. Sandbox-test the QBO InventoryValuation report and Xero journal access at Starter tier.
3. Confirm the Shopify `read_all_orders` approval path with a pilot.
4. Submit a real Intuit production-key assessment to learn the lead time.
5. One unified-API trial (Apideck or Merge) to measure data depth.

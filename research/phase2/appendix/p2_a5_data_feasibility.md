# Phase 2 / Agent 5: Data and Integration Feasibility for the Eight Candidate First Modules

Date: 2026-11-19. Scope: what data each candidate needs, what is realistically accessible to a tiny backend-strong team with no data/finance domain staff, and what it costs in onboarding and upkeep. This file does not repeat the Phase 1 architecture (`research/appendix/agent4_architecture.md`). It is consistent with it: Postgres + DuckDB, Nango for auth plumbing, dlt for extraction, raw-first landing, deterministic analysis engine with an LLM planner/narrator, evidence grades, and "3 days to connected data, 2-4 weeks to a trusted model".

## 0. Evidence-quality disclosure (read first)

- **Direct WebFetch of primary documentation was blocked.** `shopify.dev`, `developer.xero.com`, `developer.intuit.com` and `truto.one` all failed DNS resolution in this session (not on the network allowlist). I did not attempt the remaining hosts (docs.oracle.com, developers.stripe.com, odoo.com, shipstation, shippo, easypost, amazon SP-API) by direct fetch after the first hosts failed in the same way, per the tool's instruction. **No claim in this file is tagged VERIFIED-PRIMARY-FETCH.**
- All facts below come from WebSearch result summaries. I tag them:
  - **[SS-P]** = search summary quoting/derived from a primary vendor host (shopify.dev, developer.xero.com, docs.stripe.com, docs.oracle.com, odoo.com/documentation, docs.shipstation.com, developer-docs.amazon.com). Higher confidence, still not read in full.
  - **[SS-S]** = search summary of a secondary source (vendor blogs, aggregators, forums, competitors of the vendor discussed). Treat as leads; many are authored by unified-API competitors with a commercial interest.
  - **[PK]** = my prior knowledge, not checked in this session.
  - **[ASSUMPTION]** / **[SOURCED]** mark hour estimates (all hour figures are ASSUMPTION unless stated).
- Action: before any commitment, re-check the exact figures flagged "conflicting" (Xero prices, daily limits, Intuit overage rates, Nango plans) against the vendor pages once the hosts are allowlisted.

## 1. Per-system access fact sheet

### 1.1 Shopify (Admin GraphQL API)

| Topic | Finding | Tag |
|---|---|---|
| Order history depth | Default access is the last 60 days of orders; older requires the `read_all_orders` scope, requested via Partner Dashboard and approved by Shopify; it must be declared alongside `read_orders`/`write_orders`. Missing scope fails silently (older orders just do not appear). | SS-P (shopify.dev changelog + access-scopes), SS-S (forum) |
| Protected customer data | Order data is "protected customer data". Outside development stores, protected fields are redacted until the app is configured and approved. | SS-P |
| Read-only possible | Yes; `read_*` scopes exist per resource (orders, products, inventory). | SS-P/PK |
| Cost of goods | `InventoryItem.unitCost` (GraphQL; `cost` in REST/input) holds the merchant-entered "Cost per item". Only the *current* value is exposed; there is no cost-at-time-of-sale on order line items (community reports). Merchant cost entry is optional. | SS-S (forum), SS-P (changelog on `cost` property) |
| Payout/fee data | `shopifyPaymentsAccount` exposes `payouts` and `balanceTransactions` (type, amount, fee, net, `sourceOrderTransactionId`, `associatedOrder`, `associatedPayout`). Only for Shopify Payments merchants. Scope name could not be confirmed (REST docs cite `shopify_payments_payouts`). Field sets differ between API versions; pin versions. | SS-P |
| Legacy custom apps | Since 2026-01-01 new legacy custom apps cannot be created. New apps go through the Dev Dashboard (client-credentials grant). Client credentials only work when the app's organization owns the store; otherwise `shop_not_permitted`. Merchant-created-app-in-own-dashboard or a distributed app are the workarounds. Forum claims 24-hour expiring tokens for that grant (unconfirmed). | SS-S (forum, Acumatica community) |
| App review | Public app listing: review times reported by developers from ~2 weeks to 2-4+ months in 2026 forum threads (anecdotal; Shopify staff cite high submission volume). Shopify also reported tightening submission requirements (unconfirmed date 2026-11-10). | SS-S |
| Rate limits, bulk ops | Not retrieved (fetch blocked). Prior knowledge: GraphQL cost-based leaky bucket (points/sec scale with plan), Bulk Operations API for large exports, webhooks available (orders, refunds, inventory, payouts). | PK, unverified this session |

Implication: Shopify access is easy for a *design partner* (merchant creates an app and shares credentials, or you install a distributed app in unlisted/"custom distribution" mode [PK]) but a **public-listing path is a multi-month, unpredictable gate**. History beyond 60 days needs a separate approval that is typically justified by a concrete use case (analytics qualifies, but approval is not guaranteed).

### 1.2 QuickBooks Online (Intuit)

| Topic | Finding | Tag |
|---|---|---|
| Production access | Production keys require a self-assessment (app assessment) questionnaire for both private/unlisted and App Store apps; failing requirements blocks production keys. Dev and production keys are separate; sandbox only for dev. | SS-S (Apideck, Codat, Railz docs) + SS-P (developer.intuit.com publishing requirements page exists) |
| Review timeline | Third-party page (July 2026) estimates ~10 business days technical, up to 30 days security, ~5 days marketing review; "estimates not SLAs". | SS-S, low confidence |
| Annual security review | Applies to listed apps or those connected to >500 QuickBooks companies. | SS-S |
| API pricing | Intuit App Partner Program tiers: Builder (free; unlimited "Core" API calls; 500,000 CorePlus credits/month), Silver ($300/mo; 1M credits), Gold ($1,700/mo; 10M), Platinum ($4,500/mo; 75M). Overage rates conflict across sources (~$3.50 per 1,000 credits at Silver cited). Gold/Platinum gated on connection volume/Marketplace listing. CorePlus (read-heavy endpoints such as reports) is what meters; Core (create/update) is free. Applies to QBO only, not Desktop. | SS-S (Truto, Apideck), partly Intuit blog |
| Reports | Run Reports API lists InventoryValuationSummary/Detail, P&L, Balance Sheet, AR/AP Aging, General Ledger, etc. A connector vendor claims there is no inventory valuation report via API; Intuit docs list one, so test in sandbox. Valuation method (FIFO/avg) not confirmed. | SS-P / SS-S conflict |
| Read-only | `com.intuit.quickbooks.accounting` scope is the single accounting scope; it is read/write-capable at the scope level [PK]. Read-only is enforced by what the app calls, not by the scope. This matters for security reviews and customer trust. | PK |
| Rate limits | Not retrieved this session. Prior knowledge: ~500 requests/min per realm, 10 concurrent, batch up to 30 operations, Change Data Capture (CDC) endpoint for incremental sync with a limited lookback (~30 days) [PK]. | PK |

Design consequence: The *metering of report-type reads as CorePlus credits* means a monitoring product that polls reports for many tenants has a real but modest variable cost. Builder (free, 500k credits) likely covers the first dozens of tenants [ASSUMPTION: reports consume more credits than entity reads].

### 1.3 Xero

| Topic | Finding | Tag |
|---|---|---|
| Tiering | Since 2026-03-02: tiers Starter (5 connections), Core (50), Plus (1,000), Advanced (10,000), Enterprise (unlimited). Monthly egress allowances: Core 10 GB, Plus 50 GB, Advanced 250 GB; overage AUD 2.40/GB. Aggregator prices: Starter 0, Core AUD 35, Plus AUD 245, Advanced AUD 1,445 per month (not confirmed on Xero's page). | SS-P (developer.xero.com FAQ for tiers/limits/egress/date), SS-S (prices) |
| Daily limits | Sources conflict: Starter 1,000 calls/org/day, others 5,000/org/day (one version), minute limits per app per tenant. | SS-S, conflicting |
| Restricted endpoints | One guide states Journals GET, Practice Manager API and bulk connections need Advanced or above. Another says manual journals remain at all tiers. | SS-S, conflicting |
| Scopes | Apps created on/after 2026-03-02 get granular scopes only; each has a `.read` variant (true read-only is possible). `accounting.reports.read` is split into per-report scopes (P&L, bank summary, etc.). Legacy apps migrate by ~Sept 2027 (sources differ on exact date). | SS-S (Apideck, Databuzz, Chift) |
| Partner billing | Xero retiring app-store billing; partners to bill customers themselves, deadline cited 30 June or 1 July 2026. | SS-S |
| History | Reports/journal lookback numbers (12 months, etc.) not found; treat as unknown. | gap |

Design consequence: a Starter-tier app (5 connections) is free for pilots; at ~50 tenants you need Core. Cost is small in absolute terms (<AUD 250/month to 1,000 orgs) but the **egress meter and the possible gating of Journals** matter, because journals are the main route to account-level detail for margin work.

### 1.4 Stripe

| Topic | Finding | Tag |
|---|---|---|
| Payout reconciliation | Reporting API supports payout reconciliation reports (`payout_reconciliation.by_id.summary.1`, `payout_reconciliation.itemized.7`); reports are created as runs, polled, then downloaded as CSV. Payout-reconciliation is stated as available to platform accounts (check eligibility for a connected-account read use case). Balance Transactions endpoint with `payout` parameter lists all items in an automatic payout. Reports via API can cover partial days. | SS-P (docs.stripe.com) |
| Auth for read-only | Not retrieved. Prior knowledge: restricted API keys (customer-supplied, read-only scopes) or Stripe Connect OAuth/Stripe Apps; Connect OAuth for a data product needs Stripe platform review [PK]. | PK |

### 1.5 Amazon SP-API

| Topic | Finding | Tag |
|---|---|---|
| Settlement reports | V2 flat-file settlement report (`GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2`) is the supported one; older flat-file/XML types are marked deprecated. Only the last ~90 days can be listed/requested; default report retention is 90 days. A vendor says one older payment-statement flat file was removed on 2026-11-11 (unverified). | SS-P (developer-docs.amazon.com), SS-S |
| Throttling | `createReport` throttled to ~1 request/minute (burst 15). Finances API limits not retrieved. | SS-S |
| Registration | Developer registration, role-based access, and for restricted data (buyer PII) additional vetting [PK]; the settlement/finance roles are not PII-heavy. | PK |

Consequence: **history must be accumulated from the day of connection**; backfill beyond ~90 days requires the seller exporting files manually or the Finances API event listing [PK].

### 1.6 NetSuite

| Topic | Finding | Tag |
|---|---|---|
| Concurrency | REST web services and RESTlet requests share an account-level concurrency limit, enforced per integration record; exceeding returns an error (429 reported). Default figures vary by source: 5 (no SuiteCloud Plus) to 15 base, +10 per SuiteCloud Plus license. `governanceLimits` REST operation reports the account's actual limit. 15-minute request timeout. | SS-P (docs.oracle.com) + SS-S |
| SuiteQL | Third-party says ~100,000-row cap per query set/pagination; unverified. | SS-S |
| Admin burden | Requires the customer's NetSuite admin to create an integration record, role with permissions and OAuth 2.0 / token-based credentials [PK]. Concurrency must be allocated across all integrations (Celigo docs). | SS-S, PK |

### 1.7 Odoo, Business Central, Acumatica

- **Odoo**: External JSON-2 API (`/json/2/<model>/<method>`) with bearer API keys; **external API access is not available on One App Free or Standard plans (Custom plans only)**; keys cannot last more than three months so rotation is required; access follows the key-owner user's permissions. [SS-P, odoo.com docs 19.x/20.0]
- **Business Central, Acumatica**: nothing retrieved; prior knowledge: BC has OData/API v2.0 with Entra OAuth and an admin-consent step; Acumatica has contract-based REST and OData. [PK, unverified]

### 1.8 ShipStation and carriers

- ShipStation API v2: default 200 requests/minute, 429 with `Retry-After`; V1 reportedly 40 requests/minute. [SS-P, docs.shipstation.com]
- Carrier-billed invoice line data (the thing needed for freight leakage) was not found in ShipStation/Shippo/EasyPost docs. Prior knowledge: label APIs return quoted rates, not carrier invoice adjustments (dimensional-weight corrections, residential surcharges, fuel); actual invoices come as carrier EDI/CSV/PDF or via carrier APIs (UPS/FedEx billing) that require customer account credentials. [PK, high-risk gap]

### 1.9 Bank feeds

Not researched this session (no Plaid/Yodlee/Open Banking source fetched). Prior knowledge: Plaid/TrueLayer/GoCardless provide transactions with ~24 months history typically and per-connection pricing; coverage and history vary by country/bank. [PK; unverified]

## 2. Data-quality problems and what the accounting systems cannot tell you

1. **Unit-level cost history is not in the ledger.** QBO and Xero hold COGS as an account balance or, with inventory tracking, average-cost movements; neither exposes a reliable *per-unit, per-lot landed-cost history* equivalent to ERP costing. QBO's inventory valuation report availability via API is disputed (test needed). Xero tracked inventory cost is moving-average [PK]. Expect margin by SKU from the ledger to be approximate or unavailable.
2. **Shopify cost per item is optional and current-value-only.** Historical margin computed with today's `unitCost` is wrong whenever costs changed; deleted variants lose cost; bundles/kits and multi-warehouse cost differences are not represented. No source gave a completeness percentage; my planning assumption is that a substantial minority of SMB merchants have partial or no cost data [ASSUMPTION; run a 10-merchant sample to measure].
3. **Shipping cost per order is generally absent** from the order object (only shipping *charged*). Actual cost needs ShipStation/carrier data, and billed-vs-quoted needs carrier invoices.
4. **Fees live in payout/settlement data**, not in orders: Shopify balance transactions (fee, net), Stripe balance transactions, PayPal reports, Amazon settlement lines. Ledgers often book net deposits or monthly summary journals, which breaks one-to-one matching.
5. **Timing differences**: order date vs capture vs payout vs bank posting vs ledger posting; refunds/chargebacks lag; payout batching (Stripe/Shopify batch by day; Amazon by settlement period).
6. **Identity mismatches**: SKU vs ledger item vs ERP item; Amazon ASIN/SKU; customer duplicates between Stripe, billing and CRM.
7. **Multi-currency**: presentment vs settlement currency and FX at payout; ledger revalued at month-end.
8. **Manual journals and spreadsheets as system of record** (allocations, accruals, supplier price lists). Expected frequent in the target SMB segment; the product needs a CSV/Sheets upload path from day one.
9. **API-surface limits that silently truncate**: Shopify 60 days, Amazon 90 days, Intuit CDC lookback [PK], NetSuite row caps [SS-S].

## 3. Per-candidate feasibility

Scoring: GREEN = achievable by 2-3 engineers in roughly 8-12 weeks with read-only data from 1-3 systems and little domain staff; AMBER = achievable but with a named blocking dependency; RED = key data not reliably accessible or domain depth too high.

### C1. Margin / profit erosion investigation (product businesses)
- **Required data**: orders + line items + discounts + refunds (Shopify/WooCommerce/Amazon), product cost (Shopify unitCost, ERP item cost, or supplier invoice/COGS from ledger), shipping cost, payment fees, ad spend (Meta/Google), returns.
- **Accessible**: orders, refunds, fees (Shopify Payments only), ad spend (via separate platform OAuth with its own review) yes. Reliable cost is the blocker.
- **Deterministic core**: price-volume-mix and margin bridge, discount/refund/fee leakage attribution. All arithmetic; no AI needed for numbers.
- **History**: 12-24 months for seasonality/baselines; 3-6 months enough for a bridge between two periods if costs are available.
- **Read-only without data team**: yes for revenue-side bridge; cost side requires the merchant to supply or confirm cost (human-in-the-loop CSV).
- **Rating: AMBER-GREEN.** The revenue/discount/refund/fee part is green. The "true margin" claim is amber because of cost completeness and shipping cost. A product that explicitly shows "margin confidence = % of revenue with known cost" turns the problem into a feature. Shopify's 60-day default makes a design-partner custom-app path or `read_all_orders` approval necessary for history.

### C2. Cash-flow / working-capital and late-AR investigation
- **Required data**: invoices (open/paid, due dates, customers), payments, credit notes, bills (AP), bank balances/transactions.
- **Accessible**: QBO and Xero invoices/bills/payments are first-class, well documented entities; AR/AP aging reports exist via API. Standard shapes across the big two make this the best-covered accounting use case.
- **Deterministic**: aging buckets, DSO, collection-effectiveness, payment-behavior stats per customer, forecast roll-forward. Straightforward.
- **Where data lies**: invoices marked paid by journal or bank-rec timing; credit notes/prepayments/overpayments; customers with multiple legal entities; invoices outside the accounting system (spreadsheet billing).
- **History**: 12 months of invoices gives payment-behavior baselines; event-based alerts need less.
- **Read-only, no data team**: yes (Xero `.read` granular scopes; QBO reads only).
- **Rating: GREEN** on data feasibility. Crowded market (not this agent's remit) but data access is the easiest of the eight.

### C3. Reconciliation of ecommerce payouts vs bank vs ledger
- **Required data**: Shopify/Stripe/PayPal/Amazon transaction-level payout data, bank transactions, ledger deposits/journals.
- **Accessible**: Shopify Payments balance transactions (payout-to-order link available), Stripe payout reconciliation/balance transactions, Amazon settlement (90-day window). Bank feeds need an aggregator or CSV. Ledger side: QBO/Xero bank transactions and deposits.
- **Deterministic**: yes entirely; matching rules, tolerance, grouping (one payout = many orders + fees + refunds + adjustments), FX. AI only for suggesting rules and explaining unmatched items.
- **Hard parts**: three-way grouping logic per platform, manual journals that net fees, multi-currency, partial refunds, reserve/holdbacks, PayPal (not researched), Amazon V2 report quirks. Also correctness bar is high: finance users will not tolerate false matches.
- **History**: event-based; works from connection day forward with 1-3 months of back data; Amazon backfill limited.
- **Rating: AMBER.** Data is mostly accessible and deterministic, but domain-specific matching depth is large and per-platform; a no-finance-domain team will under-estimate edge cases. Existing tools in this space (not researched here) set a high feature bar.

### C4. Inventory / stock anomaly investigation
- **Required data**: inventory levels and movements (Shopify inventory levels/adjustments, ERP stock ledger, WMS), POs/receipts, sales velocity, returns.
- **Accessible**: Shopify gives levels, and inventory adjustment history via webhooks/events [PK]; no reliable movement ledger across channels. ERPs (NetSuite, Odoo, Business Central, Acumatica) hold true stock moves but access is admin-heavy and plan-gated (Odoo external API not on Free/Standard). QBO/Xero inventory is shallow.
- **Deterministic**: stock-out/overstock detection, velocity vs cover, shrink variance. Good.
- **Issues**: SKU/location mapping, bundles/kits, in-transit stock, count adjustments with no reason codes.
- **History**: 12+ months for seasonality; snapshots must be accumulated from connection because Shopify does not expose historical snapshots [PK].
- **Rating: AMBER-RED.** Valuable data lives in ERP/WMS systems with heavy integration burden; Shopify-only slice is shallow.

### C5. Supplier cost / price pass-through and procurement performance
- **Required data**: supplier invoices/bills with line items and unit prices, POs, receipts, item master, contract/price lists.
- **Accessible**: QBO/Xero bills have line items but item-level unit costs only if bills are coded to items; many SMBs code to expense accounts (no SKU). ERPs have it. Much real data is in PDFs/email/spreadsheets (needs document extraction, which is a different product).
- **Deterministic**: price-change detection per item/supplier, PPV, pass-through lag vs selling price. Fine once clean line items exist.
- **Rating: RED to AMBER.** Data completeness is the problem (line-item detail missing or unstructured), SKU matching across supplier naming is hard, and no-domain team lacks procurement context.

### C6. Revenue leakage / billing errors
- **Required data**: contracts/price books/usage (source of truth), billing system (Stripe Billing, Chargebee, Zuora), invoices, CRM.
- **Accessible**: Stripe Billing is accessible; but leakage detection needs *what should have been billed* (contracts, usage, entitlements), which is usually unstructured or in a custom system. For ecommerce, "leakage" collapses into discounts/refunds/fee analysis (C1).
- **Rating: AMBER-RED.** Ground truth for "expected" is the missing input; each customer's logic is bespoke, so it is services-heavy.

### C7. Freight / 3PL invoice leakage
- **Required data**: carrier/3PL invoices (line-level: weight, zone, surcharges), shipment records (ShipStation/WMS), contracted rate cards, order data.
- **Accessible**: shipment and quoted-rate data via ShipStation (200 req/min v2) is accessible; invoice line items are not exposed by label APIs (PK/gap); typically requires carrier portal exports/EDI/PDF. Rate cards are PDFs/contracts needing structured entry.
- **Deterministic**: yes (rate-card recomputation, duplicate and late-delivery refund claims) but requires correct rate-card modeling per carrier, which is domain-heavy.
- **Rating: AMBER-RED.** Value is concrete and measurable, but the key input (invoices and contracts) is outside APIs and parsing-heavy. A file-upload-based wedge (CSV invoice + rate card) is feasible but is not "integration-light".

### C8. Churn / revenue risk
- **Required data**: subscriptions/invoices (Stripe, Chargebee), product usage events, support tickets, CRM.
- **Accessible**: billing side easy (Stripe); usage and support need per-customer instrumentation or integrations (Zendesk/Intercom/product DB). Without usage data, only payment-based signals (failed payments, downgrades) are available.
- **Deterministic vs AI**: cohort retention/NRR bridges deterministic; risk *scores* need modeling and labeled history (needs 12-24 months and enough churn events; many SMB tenants lack volume).
- **Rating: AMBER.** Easy data entry (Stripe), but predictive value requires volume and domain labels; "investigation" (why did NRR move) via bridge is feasible and green.

### Summary matrix

| # | Candidate | Core data availability | Deterministic fit | Domain depth needed | Rating |
|---|---|---|---|---|---|
| C2 | Cash-flow / late AR | High (QBO/Xero native) | Very high | Low-moderate | GREEN |
| C1 | Margin erosion | Medium (cost gaps) | Very high | Moderate | AMBER-GREEN |
| C8 | Churn / revenue risk (bridge version) | Medium-high (Stripe) | High | Moderate | AMBER |
| C3 | Payout reconciliation | Medium-high | Very high | High (matching edge cases) | AMBER |
| C4 | Inventory anomalies | Low-medium (ERP-gated) | High | Moderate-high | AMBER-RED |
| C5 | Supplier pass-through | Low (line items) | High | High | RED-AMBER |
| C6 | Revenue leakage / billing | Low (expected values missing) | Medium | High | AMBER-RED |
| C7 | Freight/3PL leakage | Low (invoice data off-API) | High | High | AMBER-RED |

## 4. Top 3 on pure data feasibility

1. **C2 Cash-flow / late-AR**: entities are standard in QBO/Xero, read-only scopes exist, aging/DSO are arithmetic, and value shows within the first sync. Risk: easy for incumbents and spreadsheet-savvy owners; this is a market question, not a data question.
2. **C1 Margin erosion (revenue-side first)**: Shopify orders/discounts/refunds/fees are accessible, the margin bridge is deterministic, and the cost gap can be handled by surfacing "cost coverage %" and a merchant cost-upload step. Needs the 60-day history decision.
3. **C3 Reconciliation (single-platform wedge, e.g. Shopify Payments or Stripe to QBO/Xero)**: data exists with explicit payout-to-transaction links and matching is deterministic; narrow the scope to one platform to contain edge cases. Alternative third place: C8 in bridge form on Stripe.

## 5. Deterministic vs AI, and where AI misleads

**Must be deterministic code (never LLM-computed):** price-volume-mix and margin bridges; payout/bank/ledger matching and tolerance logic; aging buckets and DSO; variance (budget/prior period, PPV); FX conversion; unit-cost lookups; rate-card recomputation; any figure shown as a number.

**AI is appropriate for:** proposing hypotheses from decomposition results, ranking which dimension to inspect next, drafting narrative, suggesting mapping rules (confirmed by checks), explaining unmatched items in plain language, classifying messy descriptions (low-stakes, confidence-labelled).

**Where AI can mislead (specific to these data sets):**
- Treating incomplete COGS as zero or as the current `unitCost` and narrating a "margin collapse" that is a data artifact.
- Explaining a cash dip with "customers paying later" when the cause is invoices booked after payment, a manual journal, or a missing sync window (freshness failure).
- Presenting temporal coincidence (promo started, margin fell) as cause; confounded by mix shift, seasonality, shipping-rate changes.
- Hallucinated SKU or customer equivalences across systems.
- Silent truncation: Shopify 60-day and Amazon 90-day windows produce confident analysis over partial history.
- Averaging across currencies or periods with different accounting policies.
- Narrative smoothing over unreconciled residuals ("other").

**Evidence the UI must show (verified fact vs hypothesis):**
1. Data lineage per number: source system, object ids, sync timestamp, and a *coverage* badge (e.g. "cost known for 62% of revenue", "history from 2026-03-01").
2. Reconciliation status: does the derived total tie to the system's own report (e.g. P&L revenue) within tolerance.
3. Evidence grade per explanation (consistent with Phase 1): arithmetic identity > decomposition attribution > temporal coincidence > correlation > LLM-suggested.
4. Explicit unexplained residual after decomposition, never hidden.
5. A one-click "show me the rows" link to underlying transactions.
6. Assumptions list for any estimate (current cost applied to historical sales, etc.).

## 6. Onboarding complexity (human hours per customer, first value) [ASSUMPTION unless stated]

| Candidate | Connect + first sync (cust + us) | Mapping/validation | Customer-specific cleanup | Total to trusted first insight |
|---|---|---|---|---|
| C2 late-AR (QBO or Xero) | 1-2 h | 2-4 h | 2-6 h | ~1-2 days |
| C1 margin (Shopify + QBO/Xero) | 2-4 h (custom-app setup by merchant) | 4-8 h (cost coverage, SKU map) | 4-16 h (cost upload, shipping) | ~3-5 days |
| C3 reconciliation (one platform) | 3-6 h (platform + bank/ledger) | 8-16 h (matching rules, deposits) | 8-24 h | ~1-2 weeks |
| C4 inventory | 4-8 h (ERP admin involved) | 8-16 h | 8-24 h | ~1-3 weeks |
| C5 supplier | 4-8 h | 16-40 h (item/line coding) | 16+ h | 2-4 weeks |
| C6 leakage/billing | 4-8 h | 24-60 h (contract logic) | high, bespoke | 3-6 weeks |
| C7 freight | 4-8 h | 16-40 h (rate cards, invoice parsing) | 8-24 h | 2-4 weeks |
| C8 churn (Stripe) | 1-2 h | 4-8 h | 4-12 h | ~2-4 days (bridge), longer for scoring |

These are my estimates for a mature product; the first 3-5 design customers will take roughly 2x. SOURCED anchor: Phase 1 recommends planning "2-4 weeks to a trusted, human-validated model" (agent4 section 0).

**One-off platform lead times (SOURCED where tagged):** Shopify public-app review: 2 weeks to 4+ months per 2026 forum reports [SS-S]; Intuit production questionnaire plus review: reported estimates of 1-6 weeks [SS-S]; Xero: Starter tier is self-serve (5 connections), certification path not researched. Start unlisted/private-credential pilots first.

## 7. Ongoing maintenance burden

- **API change cadence observed in just these searches (all within ~12 months):** Shopify legacy custom-app creation ended 2026-01-01 and token model shifted; Shopify quarterly API versions with field differences (2024-10 vs 2025-01 vs 2026-01) [SS-P]; Xero tiering/pricing (2026-03-02), granular scope migration with deadline ~Sept 2027 [SS-P/SS-S]; Intuit App Partner Program tiers and credit metering; Amazon settlement report deprecations; Odoo API key 3-month max lifetime [SS-P]. This is strong evidence that **connector maintenance is a standing cost, roughly one engineer-week per source per quarter [ASSUMPTION]**.
- Token/credential lifecycle: Odoo key rotation, Shopify short-lived tokens (unconfirmed), QBO refresh-token expiry [PK], Xero refresh tokens [PK]. Needs monitoring and a "reconnect" UX.
- Silent-failure class: lost scope approvals, throttling, deleted records, plan downgrades. A freshness/coverage monitor is part of the product, not an add-on.
- Pricing drift risk: Xero egress overage and Intuit CorePlus credits create per-tenant variable cost; plan on metering per tenant from day one.

## 8. Unified-API / pipeline vendor comparison (all pricing from secondary sources unless noted)

| Vendor | Model | Pricing evidence | Fit for this team | Caveat |
|---|---|---|---|---|
| Merge | Unified accounting/etc., per linked account | Third-party: 3 free production accounts, then ~$650/mo for up to 10 linked accounts, +$65 per additional [SS-S] | Quick for accounting; per-account fee hurts SMB unit economics | Normalized models lose ERP detail; written by competitors |
| Apideck | Per consumer, unlimited calls | ~$599/mo for 25 consumers, 1 category [SS-S] | Candidate stopgap for QBO/Xero | Competitor-authored comparisons; depth for reports/journals unclear |
| Codat | Accounting + commerce, quote-only | Estimates $30-50 per connected company/month, platform fee $12-24k/yr [SS-S, benchmarks not quotes]; pricing page reported 404 | Strong accounting depth reputation [PK] | Cost likely too high for pre-revenue |
| Rutter | Commerce + accounting, quote-only | One-year term; median ~USD 18k/yr per Vendr as cited by Unified.to [SS-S] | Directly targets Shopify/Amazon + accounting (aligned with C1/C3) | Commercial minimum is high for a tiny team |
| Unified.to | Usage-based | From ~$750/mo [SS-S] | Broad | Normalization loss |
| Nango | Auth + sync/proxy framework (source-available, ELv2) | Sources conflict: Pay-as-you-go $50/mo or Starter $50 / Growth $500; metered on egress; check nango.dev/pricing [SS-S] | Best fit with Phase 1 (own the data model; get auth, token refresh, retries) | You still write mappings and handle each API's quirks |
| Fivetran/Airbyte/dlt | ETL | See Phase 1 | Fivetran per-connection economics poor for resale | Not re-researched here |

**Judgment [R]:** For a tiny team, a unified API is a shortcut only for the *accounting* leg (QBO/Xero invoices, bills, payments, accounts). It is **not** a shortcut for the hard parts of C1/C3/C4/C7: unit costs, payout-level detail, stock movements and carrier invoices are exactly what normalized "Invoice/Item" models flatten. Also, unified vendors do not remove the Intuit/Xero/Shopify review obligations on their side; some use their own (already approved) app, which is the real time saving. Recommendation consistent with Phase 1: Nango + dlt for Shopify, Stripe and one accounting system; consider Apideck/Merge for the accounting leg only if Intuit/Xero onboarding blocks a pilot. Defer Codat/Rutter until revenue justifies a five-figure annual commitment. **Data-depth limits per vendor (historical sync window, report endpoints, journal access) were not found and must be tested in sandboxes before choosing.**

## 9. Final feasibility ranking (tiny strong-backend team)

| Rank | Candidate | Colour | Reason in one line |
|---|---|---|---|
| 1 | C2 Cash-flow / late-AR | GREEN | Native QBO/Xero objects, read-only scopes, pure arithmetic, fast onboarding |
| 2 | C1 Margin erosion (revenue-side bridge first, cost coverage explicit) | AMBER-GREEN | Rich Shopify data and deterministic bridge; cost completeness and 60-day history are the gates |
| 3 | C3 Payout reconciliation (one-platform wedge) | AMBER | Explicit payout-to-order links; heavy edge-case depth |
| 4 | C8 Churn/revenue risk (NRR bridge; scoring deferred) | AMBER | Stripe data easy; predictive part needs volume/labels |
| 5 | C4 Inventory anomalies | AMBER-RED | Real data in ERP/WMS with admin and plan gating |
| 6 | C7 Freight/3PL leakage | AMBER-RED | Invoice and contract inputs off-API |
| 7 | C6 Revenue leakage/billing | AMBER-RED | "Should-have-billed" ground truth is bespoke |
| 8 | C5 Supplier pass-through | RED-AMBER | Line-item/SKU detail absent in SMB ledgers; PDF-heavy |

**Top 3 by pure data feasibility: C2, C1, C3.** Note the ranking is data-feasibility only; it says nothing about willingness to pay or competition.

**Cheap validation steps before committing:** (1) 10-merchant sample to measure Shopify cost-per-item completeness and shipping cost availability; (2) sandbox-test QBO InventoryValuation report and Xero journals access at Starter tier; (3) confirm Shopify `read_all_orders` approval path with a pilot; (4) confirm Intuit production-key lead time with a real submission; (5) get one unified-API (Apideck/Merge) trial to measure data depth.

## SOURCE REGISTER

All access via WebSearch result summaries on 2026-11-19; direct fetches of shopify.dev, developer.xero.com, developer.intuit.com, truto.one failed (host not allowlisted).

| ID | URL | Source date | Source type | Claims supported | Reliability note |
|---|---|---|---|---|---|
| A5-01 | https://shopify.dev/changelog/apps-now-need-shopify-approval-to-read-orders-older-than-60-days | 2018 (changelog; age noted) | Vendor primary (summary only) | 60-day default; read_all_orders approval | Old; 60-day rule still reflected in current docs per other results |
| A5-02 | https://shopify.dev/docs/api/usage/access-scopes | undated (current) | Vendor primary (summary only) | Protected customer data redaction for non-dev stores | Not read in full |
| A5-03 | https://help.zuzana.ai/article/how-to-request-shopifys-read-all-orders-scope.html | ~2026-06 | Third-party vendor help | read_all_orders request procedure | Secondary |
| A5-04 | https://community.shopify.dev/t/orders-are-not-returning-when-queried/35297 | 2026 | Forum | Silent failure without scope | Anecdotal |
| A5-05 | https://shopify.dev/docs/api/admin-graphql/latest/objects/shopifypaymentsaccount (and 2026-01 BalanceTransaction page) | current | Vendor primary (summary only) | Payouts/balanceTransactions fields, order linkage | Scope name unconfirmed |
| A5-06 | https://shopify.dev/changelog/the-inventoryitem-resource-now-includes-a-cost-property | undated | Vendor primary (summary only) | InventoryItem cost property | |
| A5-07 | https://community.shopify.dev/t/assymetry-of-cost-and-unitcost-on-inventoryitem/13399 ; https://community.shopify.com/t/cost-on-orders-api/1610 | 2021-2024 | Forum | Current-only cost, no cost-at-sale on line items | Anecdotal but consistent |
| A5-08 | https://community.shopify.dev/t/starting-january-1-2026-you-will-not-be-able-to-create-new-legacy-custom-apps-this-will-not-impact-any-existing-apps/26798 ; https://community.shopify.dev/t/legacy-custom-apps-workaround/32032 | 2025-2026 | Forum (incl. staff replies) | Legacy custom app end, Dev Dashboard client credentials, org restriction | Verify against docs |
| A5-09 | https://community.shopify.dev/t/longer-app-store-review-times-what-you-need-to-know/31728 ; https://community.shopify.dev/t/shopify-where-is-the-bridge-shpat-deprecated-jan-1-app-store-reviews-are-4-months-new-merchants-are-stranded/34558 | 2026 | Forum | App review delays (2 weeks to 4+ months) | Anecdotal |
| A5-10 | https://developer.xero.com/faq/pricing-and-policy-updates | 2026 | Vendor primary (summary only) | Tiers, connection caps, egress, 2026-03-02 effective date | Prices not confirmed here |
| A5-11 | https://truto.one/blog/xero-api-pricing-changes-2026-costs-tiers-and-how-to-minimize-egress/ ; https://www.apideck.com/blog/xero-api-pricing-and-the-app-partner-program | 2026 | Competitor vendor blogs | Monthly prices, daily limits, Advanced-gated endpoints | Conflicting; commercial bias |
| A5-12 | https://www.apideck.com/blog/xero-scopes ; https://www.chift.eu/blog/xero-march-2026-changes-guide-for-third-party-developers ; https://docs.codat.io/updates/260116-xero-pricing | 2026 | Vendor blogs/docs | Granular `.read` scopes, report scope split, partner billing deadline | Dates differ between sources |
| A5-13 | https://truto.one/blog/how-much-does-the-quickbooks-api-cost-2026-pricing-rate-limits/ ; https://www.apideck.com/blog/quickbooks-api-pricing-and-the-intuit-app-partner-program | 2025-2026 | Competitor vendor blogs | Intuit App Partner Program tiers, credits, prices | Overage rates conflict; Intuit rate card not seen |
| A5-14 | https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/platform-requirements ; https://developers.apideck.com/connectors/quickbooks/docs/application_owner+app_compliance ; https://docs-integration.codat.io/integrations/accounting/quickbooksonline/qbo-app-assessment-questionnaire | 2025-2026 | Vendor primary (titles only) + vendor docs | Production-key questionnaire requirement | Intuit page not read |
| A5-15 | https://vorplabs.com/agent-tools/quickbooks-online-api | 2026-07 | Third-party | Review time estimates | Low reliability |
| A5-16 | https://developer.intuit.com/app/developer/qbo/docs/workflows/run-reports | undated | Vendor primary (summary only) | Report endpoints incl. InventoryValuation | Valuation method not confirmed |
| A5-17 | https://docs.stripe.com/reports/payout-reconciliation ; https://docs.stripe.com/plan-integration/get-started/reporting-reconciliation | current | Vendor primary (summary only) | Payout reconciliation reports, balance transactions by payout, partial-day API reports | Auth/key scopes not retrieved |
| A5-18 | https://developer-docs.amazon.com/sp-api/docs/report-type-values ; https://developer-docs.amazon.com/sp-api/docs/report-type-values-settlement | current | Vendor primary (summary only) | 90-day default retention, settlement report types and deprecation | |
| A5-19 | https://improvado.io/product-updates/connectors/amazon-seller-central-settlement-report-sunset ; https://help.sarasanalytics.com/en_US/amazon-selling-partner/faq-%E2%80%93-flatfilev2settlementreport- | 2026 | Third-party data vendors | V2 90-day request limit, 2026-11-11 removal claim | Date unverified |
| A5-20 | https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/subsect_1559222360.html ; https://www.houseblend.io/articles/en/netsuite-api-rate-limits-concurrency ; https://docs.celigo.com/hc/en-us/articles/360034522472 | 2025-2026 | Vendor primary (summary) + third-party | Concurrency model, governanceLimits, per-integration allocation | Default values conflict |
| A5-21 | https://www.odoo.com/documentation/20.0/developer/reference/external_api.html | current | Vendor primary (summary) | JSON-2 API, plan gating, 3-month key max | Good |
| A5-22 | https://docs.shipstation.com/apis/shipengine/docs/guides/rate-limits | current | Vendor primary (summary) | 200 req/min v2, 429/Retry-After | V1 limit differs |
| A5-23 | https://unified.to/blog/unified_apis_usage_based_vs_per_connection_pricing_for_integrations ; https://radar.apideck.com/blog/best-unified-api-platforms-for-developers-and-saas-teams ; https://truto.one/blog/what-is-the-cheapest-unified-api-platform-2026-pricing-breakdown/ | 2026 | Competitor vendor blogs | Merge, Apideck, Codat, Rutter, Unified.to pricing models | Biased; Codat/Rutter figures are estimates |
| A5-24 | https://nango.dev/pricing ; https://toolradar.com/tools/nango/pricing ; https://www.getknit.dev/blog/nango-review-evaluation-integration-platform | 2026-11 | Vendor + aggregator | Nango egress-based pricing | Plan details conflict |
| A5-25 | /home/user/Metrial-AI-Model/research/appendix/agent4_architecture.md | 2026-11-19 | Internal Phase 1 | Architecture assumptions, 2-4 week onboarding estimate | Internal |

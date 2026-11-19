# Phase 2, Agent 3B: Operations-Side Opportunity Comparison
Date: 2026-11-19. Scope: eight operations-side candidates for the first module of a Company Intelligence platform, plus two additions. Prior hypothesis "Margin Investigator" is not re-argued; Phase-1 report and `appendix/agent2_market.md` were read first and are not repeated.

## 0. Evidence limits (read first)

- **WebFetch failed on every host I tried.** `lateshipment.com`, `spscommerce.com`, `community.shopify.com`, `fastcompany.com`, `apexanalytix.com`, `distributionstrategy.com` and `supplypike.com` all returned DNS failure (outside the session's allowed network domains); `reddit.com` was refused by the tool. These hosts have to be allowed in the session's network settings before a primary-page pass is possible. **Every claim below therefore comes from WebSearch result summaries, not from reading the pages.** Where a summary quoted a page, I reproduce that quoted text and cite the URL; I could not confirm it against the live page.
- **No Reddit or Hacker News thread was retrieved.** Searches aimed at r/ecommerce, r/logistics, r/FulfillmentByAmazon and HN returned Shopify Community, Amazon Seller Forums, r/shopify mirrors and vendor blogs. Independent practitioner evidence is thin and labelled `[ANEC]`.
- Source tags: `[IND]` independent or association/government; `[TRADE]` trade press; `[VENDOR]` vendor-authored or vendor-sponsored; `[ANEC]` forum anecdote; `[AGG]` listing or aggregator with conflicting figures. Almost all dollar-impact figures here are `[VENDOR]`. Treat them as hypotheses.
- Scores in section 12 are tagged `[EVIDENCE-BASED]` only where a sourced fact supports the score directly; otherwise `[JUDGMENT]`.
- Common pattern found across categories 3, 4 and 6: the *recovery* half is already sold as contingency-fee services or software; the *investigation* half (why it happened, which supplier/carrier/customer) is usually a by-product, not the product. That matters for a "Company Intelligence" first module.

---

## 1. Inventory and stock anomaly investigation

**Severity.** Moderate to high at the SKU level (stockout on an ad-funded SKU, oversell, dead stock). A Shopify Community thread frames stockout cost this way via a blog summary: for merchants spending on ads, losing a customer to an unavailable product "can be significantly more expensive than the missed order itself" (paraphrase in search summary of vendor blogs; `[VENDOR]`). No independent severity measure found.

**Frequency.** Continuous. Oversell and sync-failure threads recur in Shopify Community, e.g. "Inventory oversold with settings set up correctly" (https://community.shopify.com/t/inventory-oversold-with-settings-set-up-correctly/379787) and "Bundle sold but components didn't decrement — how are you catching oversells?" (https://community.shopify.com/t/bundle-sold-but-components-didnt-decrement-how-are-you-catching-oversells/658245) `[ANEC]`. I saw titles and snippets only.

**Financial impact (sourced).**
- Shrink: NRF 2023 survey, 1.6% of sales for fiscal 2022; NRF has since paused the survey (via search summary; `[IND]`-ish trade association, retail-specific, not distributors).
- Cross-industry inventory record accuracy median 95% (APQC, via a vendor blog summary at https://apprissretail.com/resources/the-other-side-of-shrink-managing-poor-inventory-record-accuracy-percentages/ `[VENDOR]`).
- IHL $1.73T global distortion is vendor-sponsored (Phase 1 report).
- Marketplace example: an agency estimates "1-3% of annual FBA revenue is lost to reimbursable errors" (summary of https://amzadvisers.com/fba-mistakes/ `[VENDOR]`).
- I found **no current authoritative distributor shrink survey**; sources say definitions differ and dollar value depends on costing method.

**Alternatives and prices.**
- Shopify inventory/forecasting apps: Prediko from $49/month (revenue-tiered), Cogsy flat ~$199/month (one source says $69-$199, unresolved), Inventory Planner $119.99 Essentials / $249.99+ Standard, quote-based at scale (`[AGG]` via https://www.prediko.io/blog/stocky-app-alternatives and https://eightx.co/blog/compare/how-much-does-cogsy-cost; vendor and consultancy estimates).
- Shopify Stocky was removed from the App Store in February 2026 and reportedly stopped working 31 August 2026 (same summary), which created a live replacement market; a Shopify Community thread titled "What are you actually paying for inventory forecasting after Stocky? ($19 to $199 spread)" (https://community.shopify.com/t/what-are-you-actually-paying-for-inventory-forecasting-after-stocky-19-to-199-spread/675887) indicates a price ceiling of roughly $200/month for SMB Shopify.
- Sync/threshold apps (HotWax, Linnworks) target oversell.
- ERPs (NetSuite, Odoo, Acumatica) include cycle count and demand planning modules; not researched in depth.

**Competitive intensity.** High for planning/forecasting; low for *explaining a variance* (why ledger and physical differ, which movement is unexplained). I found no product marketed as stock-variance investigation for SMB. Absence in search results, not proof.

**Data accessibility.** Shopify Admin API (inventory levels, adjustments with reason codes), ERP/WMS exports (NetSuite, Odoo, Extensiv/3PL portals), Amazon FBA reports. Adjustment history is the key table; for 3PL-held inventory the brand often sees only the 3PL's feed.

**Integration complexity.** Medium. Shopify easy; multi-warehouse, bundles, lot/serial and 3PL feeds are not. A sync-failure case: if an app integration "fails or disconnects, synchronization may stop without immediate notification" (vendor-blog summary, https://www.linnworks.com/blog/shopify-inventory-tracking-multichannel/ `[VENDOR]`).

**Implementation time.** 8-12 weeks for a Shopify+3PL anomaly feed; ERP variants longer.

**Accuracy requirement.** Moderate-high. A false "shrink" claim against a 3PL or warehouse team is politically costly; needs reconciled movement ledgers, not forecasts. Count-based variance is deterministic, which helps.

**Buyer / budget owner.** Ops head or founder at brand; controller at distributor. Budget line is typically "inventory software" ($50-$500/month for brands).

**Willingness-to-pay evidence.** Weak for investigation specifically. Forecasting apps show payment at $49-$250/month. I found no named customer paying for *variance investigation*. Dollar results are mostly in category 9 (reimbursement), where contingency is 10-25% (section 9).

**Recurring usage.** High (daily feed), but alerts risk fatigue.

**Expansion.** Strong: stock movements link to supplier receipts (cat. 2), fulfilment (cat. 3), returns (cat. 5), working capital.

**Dollar measurability.** Medium. Shrink at cost is measurable post-count; prevented stockouts are counterfactual.

**Contradictory evidence.** Well served at the forecasting layer by $49-$250 apps; owners' stated pain is oversell and counts, which sync tools address; an independent distributor shrink benchmark is missing, so impact is unproven.

---

## 2. Procurement and supplier performance investigation

**Severity.** High for distributors and manufacturers in a cost-inflation period; low-medium for DTC brands with 1-3 suppliers.

**Frequency.** Continuous (each PO and invoice) but detectable events are lumpy (a supplier price update).

**Financial impact.**
- NAM (trade association, `[IND]`-like): in Q2 2025 "89.0%" of respondents said cost of doing business increased due to tariffs, average stated cost increase 7.7%; 87% of small and medium manufacturers "may need to raise prices" (https://nam.org/?p=36966 and https://documents.nam.org/COMM/Tariff_One_Pager_2025.pdf, via summary).
- Pass-through is partial: Boston Fed (Morning Consult small-business survey, 2025) found importers expected to pass through "about two-thirds" of anticipated cost increases within a year and non-importers about one-third rising to about 50% by August (https://www.bostonfed.org/publications/current-policy-perspectives/2025/who-pays-for-tariffs, via summary; `[IND]`). This is the strongest independent evidence that supplier cost increases leak into margin.
- Distribution Strategy Group: execution gaps translate to "3-5% of revenue annually" (84 respondents; via summary of https://distributionstrategy.com/report/closing-the-execution-gap/; `[TRADE]`/consultancy).
- Phase 1 already cites supplier reconciliation cycles of 3-6 months; not repeated.

**Alternatives and prices.** SRM/supplier scorecard tools mostly "contact the vendor" pricing (FitGap listings); one vendor-management tool "from $199" `[AGG]`; Coupa-class suites quote "mid-to-high five figures annually" (https://us.fitgap.com/search/supplier-relationship-management-srm-software/small-business `[AGG]`). I found no NetSuite/Odoo scorecard documentation or any late-delivery rate survey. Walmart-type OTIF programs push supplier scorecards from the retailer side (cat. 6).

**Competitive intensity.** Mixed. Enterprise SRM crowded; SMB "supplier cost change vs sell price" detection is not a named product category in anything I found. Overlaps the Phase-1 margin hypothesis; I treat the *procurement* framing here (supplier OTIF, quality, price creep) as distinct.

**Data accessibility.** POs, receipts and vendor bills in ERP/accounting (NetSuite, QuickBooks, Xero bills lack PO linkage unless a purchasing module is used). SMBs without POs have only bills: price creep is detectable from bill line items, delivery lateness is not.

**Integration complexity.** Medium-high. Requires PO-receipt-bill linkage (three-way match), item/supplier master cleanup.

**Implementation time.** 10-16 weeks per ERP; faster if bill line items from QuickBooks/Xero suffice for price-creep only.

**Accuracy requirement.** High when used in supplier negotiations; the buyer will confront a supplier with the number. Item-matching errors are the main risk.

**Buyer / budget owner.** Purchasing manager, COO, or owner. Budget line is weak: procurement savings are often justified by savings reports, not tool budgets.

**Willingness-to-pay evidence.** No named SMB customer or case study found for supplier-performance analytics. Contingency recovery on overcharges is established (20-30%, Texas contracts 14-22.5%; https://www.apexanalytix.com/resources/blog/recovery-audit-cost/ and https://fmx.cpa.texas.gov/fm/audit/recovery/rpt2021/Recovery_Audit_2021.pdf, via summary; `[VENDOR]`/government contract) but that is AP recovery for large payers.

**Recurring usage.** Medium: monthly supplier review plus event alerts.

**Expansion.** Strong: supplier cost feeds margin, inventory, cash planning.

**Dollar measurability.** Medium-high for price creep vs contract/last price; low for "late delivery cost".

**Contradictory evidence.** Several surveys show most manufacturers *do* pass cost on (ISM Dec 2025: 86% plan to pass on at least some; Manufacturers Alliance June 2025: 77% chose price increases; via https://www.manufacturingdive.com/news/manufacturers-plan-price-hikes-over-reshoring-to-combat-tariff-effects-ism/808157/ summary), so the leak is a *lag/partial* problem, not absent pricing. No evidence SMBs buy scorecard software.

---

## 3. Order fulfilment and operational bottlenecks

**Severity.** High when SLA penalties exist (retail compliance, marketplaces); otherwise customer-experience cost that is hard to dollarize.

**Frequency.** Daily.

**Financial impact.**
- Retail OTIF fines: multiple sources agree Walmart fines "3% of cost of goods sold" on non-compliant cases (https://www.8thandwalton.com/blog/walmart-otif; Retail Dive reports a spokesperson confirming the 3% fine, https://www.retaildive.com/news/walmart-on-time-in-full-87-suppliers/550102; `[TRADE]`).
- A SupplyPike case study describes a grocery supplier with monthly losses of "$158,000" from prepaid on-time fines (https://www.supplypike.com/customer-stories/grocery-supplier, via summary; `[VENDOR]`, anonymous).
- For DTC brands, no sourced dollar figure for late shipments. 3PL on-time-ship benchmarks (97-99.9%) are 3PL-authored and definitions vary; backorders and held orders are sometimes excluded (https://www.spscommerce.com/community/articles/3pl-performance-benchmarks-how-to-verify-your-3pls-numbers, via summary).

**Alternatives and prices.** 3PL dashboards (ShipBob etc.), OMS/WMS reporting, tracking/post-purchase apps (AfterShip), SupplyPike/SPS for OTIF fines (quote-based). No sourced SMB-priced "bottleneck investigation" product.

**Competitive intensity.** Medium: operational dashboards are bundled into WMS/3PL; investigation across order, warehouse and carrier timestamps is not sold standalone as far as I found.

**Data accessibility.** Order timestamps (Shopify), WMS/3PL events (often API-poor, CSV/EDI/portal), carrier tracking APIs. 3PL data is the bottleneck: a "3PL performance" check depends on the 3PL's own numbers.

**Integration complexity.** High (3PL heterogeneity).

**Implementation time.** 12-20 weeks for first 3PL-agnostic version.

**Accuracy requirement.** High where fines/credits are disputed; medium for internal ops.

**Buyer / budget owner.** Ops/fulfilment lead; CFO only when fines are involved.

**Willingness-to-pay evidence.** Strong only in the fine-recovery sub-case (cat. 6). Otherwise none.

**Recurring usage.** High, but ops staff already live in WMS screens.

**Expansion.** Strong into the broader operating model.

**Dollar measurability.** Low unless tied to fines, refunds, or expedite spend.

**Contradictory evidence.** Benchmarks show warehouse on-time shipping is typically reported above 97% by 3PLs themselves, i.e., buyers may not perceive a problem; value rests on verifying 3PL claims, which is a 3PL-contract issue.

---

## 4. Freight, 3PL and carrier invoice auditing; shipping-cost leakage

**Severity.** Moderate; real money, low drama.

**Frequency.** Every invoice cycle (weekly).

**Financial impact (with source quality).**
- "Typically returning 1% to 5% of parcel spend" and "6 to 20%" (LateShipment's own research) conflict; both vendor claims (https://www.lateshipment.com/platform/oneaudit/ and https://www.shipscience.com/parcel-audit-guide/, via summary; `[VENDOR]`). Another LateShipment page estimates "between 2% and 8%" of carrier invoice value is refund-eligible per billing cycle (`[VENDOR]`).
- Trax Technologies is quoted for 15-25% of freight invoices containing mistakes (via search summary; `[VENDOR]`, original not seen).
- Refund windows: 15 days for late-delivery claims, 180 days for billing errors (vendor guides). UPS Ground and Ground Saver "no longer offer money-back guarantees", so late-delivery refunds mostly matter on express services (https://www.shipscience.com/?p=80582 via summary; `[VENDOR]`).
- Surcharge pressure is rising: carriers' general rate increase is reported at 5.9% for 2026, with surcharges "now the primary drivers of total shipping cost" per one summary (https://shipperhq.com/blog/carrier-rate-increases-2026; https://www.digitalcommerce360.com/2026/03/26/analysis-shipping-surcharges-surge-carriers-ecommerce-economics/amp/; `[TRADE]`/vendor). No independent measure of surcharge share of spend found.
- **Named customer evidence:** Rebel Cheese (Austin). Fortune (1 May 2026, https://fortune.com/2026/05/01/rebel-cheese-mark-cuban-ai-shipping/) reports the AI agent saved $400,000 in one year; the CEO estimated about $250,000 overcharged after a holiday rush; savings have fallen below $40,000 in recent months because "carriers now knowing the tool catches overcharges" (my paraphrase of the summary). Fast Company (https://www.fastcompany.com/91537200/texas-rebel-cheese-ai-shipping) says the system was built with Claude and Manus and its lead reports only "thousands" recovered; the two sources disagree on size. Company-reported, a founder-led build, not a purchase of software.
- Plant Addicts recovered $36,968 in carrier claims (https://www.lateshipment.com/resources/case-studies/plant-addicts/; vendor-hosted).

**Alternatives and prices.** LateShipment.com OneAudit: 35% of recovered credits, no monthly/setup fee (one listing also shows 25%); AuditShipment standard tier 50% for spend up to $500K; Refund Retriever charges "only" on refunds received; Lojistic, ShipScience, ShipRx, Intelligent Audit (Catalyst for SMB), Shipium (carrier-selection platform), plus managed audits generally 25-50% (all `[VENDOR]`/`[AGG]`, via summaries of https://www.lateshipment.com/platform/oneaudit/, https://www.easypost.com/blog/parcel-audit-software/). Phase 1 already noted 25-50% contingency.

**Competitive intensity.** High and mature. Contingency means zero upfront cost to shippers, which makes a subscription analytics product a hard sell.

**Data accessibility.** Carrier invoices (CSV/EDI via carrier portals), shipping software (ShipStation, EasyPost, Shopify Shipping), contract rate tables (often PDFs). A brand on a 3PL's carrier account cannot see invoices at all (Phase 1).

**Integration complexity.** Medium; invoice parsing plus contract-rate encoding is the real work.

**Implementation time.** 6-10 weeks for a parcel-only auditor; the rebuild is feasible for a strong backend team but the market is served.

**Accuracy requirement.** High (claims go to carriers; false claims damage relationships), though deterministic rules (contract vs invoice) are verifiable.

**Buyer / budget owner.** Ops/finance lead; budget is the shipping line itself (contingency).

**Willingness-to-pay evidence.** Strongest of the eight: real contingency prices and named results. But the buyer is paying a percentage, not a SaaS fee.

**Recurring usage.** High, but value decays: Rebel Cheese's own recoveries fell, implying carriers respond to scrutiny.

**Expansion.** Medium: shipping cost data joins margin, fulfilment and returns analysis.

**Dollar measurability.** Highest in the set: each refund is a ledger credit.

**Contradictory evidence.** Services-only/contingency incumbents dominate; a CEO built her own agent with off-the-shelf Claude/Manus; recoveries decline over time; independent leakage % is absent.

---

## 5. Returns and refunds root-cause investigation

**Severity.** High for apparel/fit/electronics; direct margin and inventory impact.

**Frequency.** Continuous.

**Financial impact.** NRF/Happy Returns 2025: $849.9B returns, 15.8% return rate; 19.3% of online sales returned; 9% of returns fraudulent per the report's estimate, with analysts cautioning that fraud figures are not comparable across studies (https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025, 15 Oct 2025; `[IND]`-ish, sponsored by a returns vendor). Merchant-level dollars per SKU are not sourced.

**Independent practitioner evidence (anecdote).** A Shopify Community thread titled "Has anyone actually traced a return spike back to a specific supplier shipment?" (https://community.shopify.com/t/has-anyone-actually-traced-a-return-spike-back-to-a-specific-supplier-shipment/622026) is quoted in a search summary as saying "Most stores track returns at the SKU level and stop there, but the batch/shipment layer is where the actual root cause lives." I could not read the thread to establish whether the author is a merchant or a vendor. `[ANEC]`.

**Alternatives and prices.** Loop Returns (Essential from about $155/month, Advanced from about $340/month; overages unpublished), AfterShip Returns ($16-$19 Essentials, $99-$119 Premium; overage $0.55-$1.19/return; promotion reported), Happy Returns Plus $500/month (UPS), Returnly now under Affirm (all `[AGG]`/vendor, via https://www.aftership.com/blog/returns-platform-pricing-guide and https://www.ringly.io/blog/shopify-returns-app). Returns apps provide reason codes; one vendor argues "Return Reason Codes Lie" (https://www.cahoot.ai/return-reason-codes/, `[VENDOR]`). Shopify native product-level return report exists (summary).

**Competitive intensity.** High on returns *management*; medium on root-cause analytics. Returns app vendors have the data and a natural upsell.

**Data accessibility.** Shopify returns/refunds API, returns app data, supplier/lot (only if captured: "SKUs, tags, barcodes, and custom metadata don't always sync from supplier to retailer", search summary), 3PL receiving notes.

**Integration complexity.** Low-medium for Shopify; high to link returns to supplier lots.

**Implementation time.** 6-10 weeks for SKU/channel/reason analysis; supplier-batch linkage depends on customer data.

**Accuracy requirement.** Medium; findings like "defect cluster after restock date" are statistical and negotiable with suppliers.

**Buyer / budget owner.** Ecommerce/ops lead, CX lead; budget limited to returns-app tier ($100-$500/month).

**Willingness-to-pay evidence.** No named customers paying for return root-cause. Price anchors are the returns apps above.

**Recurring usage.** Medium: monthly review plus spike alerts.

**Expansion.** Good: ties product quality, supplier, margin, CX.

**Dollar measurability.** Medium: return cost per SKU computable; causal attribution to supplier is uncertain.

**Contradictory evidence.** Returns platforms already bundle analytics; the signal for root cause (supplier lot) often is not in the data; the one community thread I found stresses the problem but has no answer visible.

---

## 6. B2B price and discount leakage; rebates, chargebacks, retailer deductions

I treat two sub-cases separately because their evidence differs.

### 6a. Retailer deductions and chargebacks (CPG/wholesale selling into retail)

**Severity.** High for brands selling to Walmart, Kroger, Amazon Vendor and natural distributors (KeHE, UNFI). Dispute windows are short ("11 days" in one summary), which creates urgency.

**Frequency.** Continuous monthly volume.

**Financial impact.** Vendor ranges only: "1% to 7%" of gross revenue; SPS Commerce "5-7%"; Endless Commerce "2-5%"; Inmar "5 to 15%"; SPS "up to 17%" for health and wellness (summary of https://www.spscommerce.com/deduction-management/ and https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands). Invalid share 15-25% (Inmar) to 30-60% (Confido); "70%" of invalid dollars ultimately recovered per a 2012 Credit Research Foundation survey (https://www.minneapolisfed.org/~/media/files/about/what we do/remittance coalition/2012-crf-deduction-code-study-vcf-fall-conference-butler.pdf, via summary; the only independent-style source, 14 years old). Manual handling estimated at "$200 to $300 per deduction" by one vendor.

**Alternatives and prices.** SupplyPike (SPS Commerce), Vividly, Glimpse ($10M raise, success-based low monthly fee plus percentage of recovery), PACMAN (commission-only, rate declines with scale per G2), HighRadius (enterprise), Confido, Doss, iNymbus, Promomash (free pilot, custom pricing), Chargeback Gurus (not verified) (`[VENDOR]`/`[AGG]`: https://us.fitgap.com/search/deduction-management-software/small-business, https://www.foodbevy.com/?p=38999).

**Competitive intensity.** High and recently funded; commission models are the norm.

**Willingness-to-pay evidence.** The best in this report. Named: Bissell via SupplyPike ("recovered over $1 million in lost revenue", "increased their win rate by 20%"), E.T. Browne ("recovered over $1M from Walmart"), Health-Ade via Vividly (headline "Recovered $700K"), immi via Glimpse (no number), Glimpse claims "four to five times" average ROI (https://www.supplypike.com/customer-stories, https://govividly.com/our-customers, https://foodindustryexecutive.com/?p=26377, via summaries; `[VENDOR]` self-reported, not verified).

**Data accessibility / integration.** Retailer portals (Walmart Retail Link, Amazon Vendor Central), remittance/EDI 820/812, ERP AR. Portal scraping and EDI are heavy; this is the integration burden that deduction vendors have already paid for.

**Implementation time.** 12-24 weeks to cover 2-3 retailers properly.

**Accuracy requirement.** High; disputes require evidence packets (proof of delivery, BOLs, ASNs).

**Buyer.** AR/credit manager or CFO in CPG; budget from recoveries.

**Contradictory evidence.** Saturated with funded, success-fee vendors; the dispute work is workflow-heavy (document assembly), not investigation-heavy; most figures anonymous and vendor-reported. **Why OTIF (Walmart 3% fine) matters:** it is the cleanest detectable-event dollar case in operations (see cat. 3), but vendors already own it.

### 6b. Rep overrides, customer-specific pricing drift, rebates

**Severity/frequency.** Described as common in distribution: "most mid-cap distributors leak 100 to 300 basis points of margin a year" (summary of https://distributionstrategy.com/2026/06/the-mid-cap-distributors-pricing-quandary/ `[TRADE]`, abstract not read). A vendor, Intuilize, cites a $45M distributor that documented "$250,000" annual losses from delayed cost updates on 7% of its catalogue (vendor; marketing).

**Named case studies (enterprise).** Metalwork Industrial Distributing Company (PROS): "$3.8M above target revenue" and "anticipated $18M annual gross profit lift" (the $18M is expected, not realized); global wholesale electronics distributor $41M annual leakage (anonymous, $1-5B revenue); Fortune 150 distributor $50M (ProfitOptics, anonymous) (https://pros.com/learn/distribution/industrial-distributor-optimizes-pricing-for-millions-in-profit, https://conga.com/customer-stories/distributor-improves-pricing-and-sales, https://www.profitoptics.com/case-studies/fortune-150-distributor, via summaries; `[VENDOR]`). All enterprise-scale; no mid-market named result found.

**Alternatives.** PROS (Conga), ProfitOptics, Zilliant, Vendavo (not verified in my results), ERP price books. Prices not public; enterprise quote-based.

**Competitive intensity.** Enterprise crowded; mid-market open but also thinly evidenced.

**Data accessibility.** Quote/order/invoice lines and price books in ERP (NetSuite, Epicor, Acumatica); rebate agreements in contracts/spreadsheets. **Integration:** high, rebate terms are unstructured.

**Time to value.** 12-20 weeks; first value is a one-time price-waterfall analysis.

**Accuracy.** Medium-high; sales teams will contest findings, so evidence trails matter.

**WTP.** Enterprise pricing projects are priced at six to seven figures (not sourced); mid-market WTP unproven.

**Contradictory evidence.** Phase-1 treats this as the margin thesis and it is already ruled "not approved"; I note that rep-override and rebate leakage depends on ERP data that mid-market firms keep inconsistently.

---

## 7. Marketing and ad-spend efficiency anomalies (ecommerce)

**Severity.** Moderate; ad spend is often the largest variable cost.

**Frequency.** Daily.

**Financial impact.** No independent leakage figure found.

**Alternatives and prices.** Triple Whale ($99-$219 floor depending on source; GMV-tiered), Northbeam (reported floor $1,500/month; "core infrastructure at roughly $50K+/month in paid media"), Polar (entry $720/month, tracker dated 2026-07-31), plus Lifetimely and others (https://attribuly.com/blogs/triple-whale-pricing-review/, https://thecmo.com/tools/northbeam-review/, https://www.ringly.io/blog/triple-whale-alternatives; `[AGG]`/affiliate-driven reviews).

**Competitive intensity.** Very high: 5+ funded vendors, platform-native analytics (Meta, Google, Shopify).

**Data/integration.** Meta/Google/TikTok ad APIs plus Shopify orders and COGS: easy, standardized, but attribution is contested.

**Attribution caveat.** One review says Triple Whale's attribution is "decision-support rather than audited revenue", and a G2 reviewer "strongly advised against it, citing data accuracy and support concerns" (via search summary of https://www.g2.com/products/triple-whale/pricing and https://attribuly.com/blogs/triple-whale-pricing-review/; single review, affiliate-adjacent). This makes causal claims about campaign contribution margin inherently weak.

**Implementation time.** 6-8 weeks (replicates existing apps).

**Accuracy requirement.** Low tolerance for wrong "kill this campaign" advice; users will compare to the ad platform's numbers.

**Buyer.** Founder or growth lead; budget line = marketing tools ($100-$1,500/month).

**WTP.** Proven but price-capped, and incumbents hold the money.

**Recurring usage.** Very high (daily).

**Expansion.** Medium; moves toward customer/channel profitability.

**Dollar measurability.** Medium; attribution contested.

**Contradictory evidence.** Most crowded category in the list; pricing is anchored by competitors; claims depend on attribution that independent reviewers question.

---

## 8. Manufacturing cost and yield variance (scrap, labor efficiency, BOM cost drift)

**Severity.** High per customer in discrete manufacturing; evidence here is weak.

**Frequency.** Per work order or batch.

**Financial impact.** No independent figure found. Phase 1 cites vendor claims on Excel reliance (e.g., Galorath: 96% of manufacturers rely on Excel for cost estimation). I did not find scrap-rate or yield-variance benchmarks for small manufacturers.

**Alternatives and prices.** Small-maker MRP: MRPeasy $49-$149 per user/month, Katana Core $299/month monthly (older PDF: $359 Standard, $799 Professional; another source says custom annual contracts), Odoo/NetSuite/Fishbowl in the middle (`[AGG]`: https://www.mrpeasy.com/mrpeasy-vs-katana, https://www.capterra.com/p/172888/Katana-MRP/pricing/). I could not confirm whether they expose standard-vs-actual variance reports; search summaries said they do not document it. ERP vendors with cost accounting (NetSuite, Epicor, Plex) include variance reporting; heavy to configure.

**Competitive intensity.** Low for SMB "explain the variance", but because buyers use ERP-native reports or consultants.

**Data accessibility.** Work orders, routings, BOM versions, labor time, material issues and receipts: in ERP, often incomplete or entered in batches; shop-floor capture is spotty.

**Integration complexity.** High. Each ERP's costing model differs (standard vs actual vs average).

**Implementation time.** 16-30 weeks; consulting-heavy.

**Accuracy requirement.** Very high; cost accounting disputes involve the controller.

**Buyer.** Plant manager/controller; budget through ERP partner.

**WTP.** No named customers found.

**Recurring usage.** Monthly close + weekly production review.

**Expansion.** Strong but deep.

**Dollar measurability.** High once data is clean; extremely dependent on data quality.

**Contradictory evidence.** Evidence of demand is the thinnest of the eight; implementation drags like an ERP project; the founder's small team lacks manufacturing domain knowledge (inference).

---

## 9. Additional opportunity A: marketplace reimbursement and claims recovery (Amazon FBA lost/damaged inventory, fee overcharges)

Included because it is the closest analogue of a *ledger-vs-physical variance investigation* with a paid, named market.

- **Pain evidence (anecdote).** Amazon Seller Forum posts: "Only around 50 of the items were checked in" of a pallet of "a few hundred" (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4b65fb9e-971c-4eb1-a363-6c56d5fc5287, `[ANEC]`); another seller reports about 800 units removed under "Inventory Ownership Correction" with repeated denials (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/5ee8861a-bad5-471b-9ae9-0ab314c0ffb5, `[ANEC]`). Quotes are from a search summary.
- **$ impact.** "1-3% of annual FBA revenue" reimbursable (agency estimate, `[VENDOR]`).
- **Alternatives and prices.** Helium 10 Refund Genie (DIY, tied to subscription $99-$129/month), Helium 10 Managed Refund Service (success-fee; included in Platinum/Diamond), Getida 25%, Seller Investigators (Carbon6) 10% with first $1,000 free (sources conflict on which fee applies to which service; https://www.helium10.com/tools/operations/managed-refund-service/, https://jarvio.io/best-amazon-reimbursement-tools; `[AGG]`/affiliate).
- **Competitive intensity.** Very high and commoditized; fees compress toward 10%.
- **Data access.** Amazon SP-API reports (inventory ledger, reimbursements): good. **Integration:** low-medium. **Time:** 6-8 weeks.
- **Accuracy:** claims are reviewed by Amazon; a deterministic ledger check works.
- **Buyer:** FBA seller owner; budget is contingency.
- **Expansion:** weak outside Amazon sellers (not B2B SaaS with mid-market upside).
- **Verdict:** proves contingency pricing works for ledger-vs-physical discrepancies but the market is saturated and low-ARPA.

## 10. Additional opportunity B: vendor invoice/contract price-compliance and rebate-collection audit (AP side)

A bridge between categories 2 and 6b: compare vendor bills to PO/contract/last-price and unclaimed rebates.

- **Evidence.** Recovery audits (duplicate payments, contract overpayments, unclaimed rebates) are an established contingency category at 20-30% (apexanalytix and others, `[VENDOR]`; Texas state contracts 14-22.5%, `[government contract]`). One vendor says "92 percent of all duplicate payments that auditors uncovered could be traced to coding errors" (via summary; `[VENDOR]`). The search returned nothing specific to PO-vs-invoice price variance for small distributors.
- **Competition:** recovery auditors (services), AP automation suites (Tipalti, Stampli, not researched in depth).
- **Data:** AP ledger, POs, contracts (unstructured). **Integration:** medium (accounting) to high (contracts).
- **Verdict:** buyer budget is contingency; weak signal for SaaS pricing; I rank it below the eight because I found no SMB customer evidence.

I did not find a better opportunity than the ten above. The most interesting *structural* finding is that the highest-evidence markets (parcel audit, deductions, FBA reimbursement) are all "find money owed by a counterparty" with deterministic rules, priced on success fees.

---

## 11. Cross-cutting observations

1. **Counterparty-recovery vs internal-leak.** Parcel audit, deductions, FBA reimbursements and AP recovery have a third party who owes money, a deadline, and contingency pricing. Internal leaks (inventory, procurement price creep, ad efficiency, manufacturing variance) have no counterparty, weaker price evidence, and are bundled into ERPs/apps.
2. **Contingency pricing compresses SaaS pricing.** Buyers anchor at 10-50% of recovered dollars with no upfront cost. A subscription must beat that.
3. **DIY with general AI is a real substitute** in the recovery category (Rebel Cheese), and recoveries decay as counterparties adapt (savings under $40,000 recently vs $400,000 for the year, per Fortune).
4. **Independent evidence is scarce.** Nearly every dollar figure is vendor-authored. The best independent items are NAM/Boston Fed/ISM (supplier cost pass-through), NRF (returns), the CRF 2012 deductions study, and Fortune's Rebel Cheese report (company-reported).
5. **A company-intelligence module fits where several systems must be joined** (inventory + supplier + returns + shipping + margin) rather than any single recovery workflow; this argues for a *cross-ops variance investigator* with one recovery-friendly entry, not a single-category tool. This is judgment.

---

## 12. Scoring table

Scale 1-5. Competition openness: 5 = open. Accuracy tolerance: 5 = forgiving. Time-to-value: 5 = fast. Integration ease: 5 = easy. Tag: **E** = [EVIDENCE-BASED], **J** = [JUDGMENT].

| # | Opportunity | Pain severity | Frequency | $ impact | Data access | Integration ease | WTP evidence | Competition openness | Time-to-value | Accuracy tolerance | Recurring usage | Expansion | Total /55 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Inventory/stock anomaly | 3 J | 5 E | 3 J | 4 J | 3 J | 2 E | 3 E | 3 J | 2 J | 4 J | 5 J | 37 |
| 2 | Procurement/supplier | 4 E | 4 J | 4 E | 3 J | 2 J | 2 E | 4 E | 2 J | 2 J | 3 J | 5 J | 35 |
| 3 | Fulfilment bottlenecks | 3 J | 5 J | 2 J | 2 J | 2 J | 2 E | 3 J | 2 J | 3 J | 4 J | 4 J | 32 |
| 4 | Freight/parcel audit | 3 J | 5 E | 3 E | 4 J | 3 J | 5 E | 1 E | 4 J | 2 J | 4 E | 3 J | 37 |
| 5 | Returns root cause | 4 J | 5 E | 3 E | 4 J | 3 J | 2 E | 3 E | 3 J | 3 J | 3 J | 4 J | 37 |
| 6a | Deductions/chargebacks | 4 E | 5 E | 4 E | 2 J | 1 J | 5 E | 1 E | 2 J | 2 J | 4 J | 3 J | 33 |
| 6b | Rep override/rebate leakage | 4 J | 4 J | 4 E | 3 J | 2 J | 3 E | 3 E | 2 J | 3 J | 3 J | 5 J | 36 |
| 7 | Ad-spend efficiency | 3 J | 5 J | 3 J | 5 J | 5 J | 3 E | 1 E | 4 J | 2 E | 5 J | 3 J | 39 |
| 8 | Manufacturing variance | 4 J | 3 J | 3 J | 2 J | 1 J | 1 E | 4 J | 1 J | 1 J | 3 J | 4 J | 27 |
| 9 | FBA/marketplace reimbursement | 3 E | 5 E | 3 E | 4 E | 4 J | 4 E | 1 E | 4 J | 3 J | 4 J | 2 J | 37 |
| 10 | AP/contract price compliance | 3 J | 4 J | 3 E | 3 J | 3 J | 3 E | 3 J | 3 J | 2 J | 3 J | 4 J | 34 |

One-line justifications (criterion order as in the table; unsourced scores are judgment):

1. **Inventory.** Severity: SKU-level, no independent measure. Frequency: oversell threads recur (Shopify Community titles). $: NRF 1.6% retail shrink but no distributor benchmark. Data: Shopify API plus 3PL feeds. Integration: bundles, multi-warehouse. WTP: apps cap at ~$199-$250/month; no investigation buyers seen. Competition: forecasting crowded, variance explanation open. Time: 8-12 weeks. Accuracy: false shrink claims hurt. Recurring: daily feed. Expansion: links to every ops module.
2. **Procurement.** Severity/$: NAM and Boston Fed show real but partial pass-through. Data: PO-receipt-bill linkage rare in SMBs. Integration: item master cleanup. WTP: no scorecard buyers found. Competition: SMB price-creep detection unnamed. Time: 10-16 weeks. Accuracy: used in negotiation. Expansion: feeds margin, inventory, cash.
3. **Fulfilment.** Severity/$: only OTIF fines quantified (3% COGS; one $158K/month anonymous case). Data/integration: 3PL data is hard. WTP: only in fine-recovery. Competition: WMS/3PL dashboards bundled. Accuracy: disputed credits. Recurring: daily but staff already in WMS.
4. **Parcel audit.** Frequency: every invoice. $: 1-5% vs 6-20% vendor claims conflict; Rebel Cheese $250-400K company-reported. Data: invoices plus contract rates. WTP: 25-50% contingency, named recoveries. Competition: mature vendors, zero-upfront pricing. Time: 6-10 weeks. Recurring: weekly, but recoveries decay (savings <$40K recently). Expansion: moderate.
5. **Returns.** Frequency/$: NRF 15.8% returns, 19.3% online. Data: Shopify easy, supplier lots hard. WTP: returns apps $16-$500/month, no root-cause buyers seen. Competition: apps own the data. Accuracy: supplier negotiation is statistical. Expansion: ties quality, supplier, margin.
6a. **Deductions.** Severity: 1-17% revenue vendor range, 2012 CRF 70% recovery. WTP: named results (Bissell, E.T. Browne, Health-Ade) vendor-reported, commission models. Data/integration: retailer portals, EDI. Competition: funded vendors. Time: 12-24 weeks. Accuracy: evidence packets.
6b. **Override/rebate.** $: 100-300 bps (trade source, abstract unread); named cases enterprise-scale only. Data: ERP price books, rebate terms unstructured. Competition: enterprise crowded, mid-market open. WTP: enterprise only evidenced.
7. **Ad spend.** Data/integration: standardized ad APIs. WTP: proven, $99-$1,500/month. Competition: 5+ funded vendors. Accuracy: attribution contested by independent reviewer. Recurring: daily.
8. **Manufacturing.** Integration: costing models differ per ERP. WTP: none found. Time: 16-30 weeks. Accuracy: controller-level. Competition: open because ERP-native/consulting-driven. Expansion: deep but slow.
9. **Reimbursement.** Frequency: FBA inbound/removal errors. $: 1-3% FBA revenue (agency). Data: SP-API good. WTP: 10-25% fees, named competitors. Competition: commoditized. Expansion: weak beyond Amazon.
10. **AP/contract compliance.** $: 20-30% recovery contingency norm. Data: contracts unstructured. WTP: no SMB customers found. Expansion: bridges to procurement and margin.

**Reading the table (judgment).** Highest total is ad spend (39) but with the weakest competition openness and attribution-dependent accuracy. Parcel audit, FBA reimbursement and returns tie at 37 with inventory. Evidence of payment is strongest in categories 4, 6a and 9, and all three are saturated and success-fee priced. Evidence of openness is strongest for 2, 6b and 8, and all three lack paying-customer evidence and carry heavy integration. No category scores high on both. Phase 3 should test the cross-ops variance framing (section 11 item 5) against one counterparty-recovery wedge rather than pick a single category on these totals.

---

## SOURCE REGISTER

All accessed via WebSearch result summaries on 2026-11-19; WebFetch was blocked for every host tried. "Source date" is as shown in the search summary or URL; "n/d" means not shown.

| ID | URL | Source date | Source type | Claims supported | Reliability note |
|---|---|---|---|---|---|
| A3B-01 | https://www.lateshipment.com/platform/oneaudit/ | n/d | Vendor product page | OneAudit 35% of recovered credits, no monthly/setup fee; 25% on another bundle | Vendor; rate inconsistency across pages |
| A3B-02 | https://www.shipscience.com/parcel-audit-guide/ ; https://www.fulfill.com/blog-posts/parcel-audit-guide | n/d | Vendor guides | 25-50% managed audit contingency; 1-5% of spend; 180-day billing window | Vendor; figures conflict with A3B-01 |
| A3B-03 | https://www.shipscience.com/?p=80582 ; https://www.lojistic.com/blog/guaranteed-service-refund-gsr-waivers-and-how-parcel-auditing-can-help-you | n/d | Vendor blogs | UPS Ground no longer money-back guarantee; 15-day late-claim window; GSR waivers | Vendor; needs carrier-terms check |
| A3B-04 | https://fortune.com/2026/05/01/rebel-cheese-mark-cuban-ai-shipping/ | 2026-05-01 | Business press | Rebel Cheese $400K saved in one year, ~$250K overcharge estimate, recent savings <$40K | Company-reported via press; summary only |
| A3B-05 | https://www.fastcompany.com/91537200/texas-rebel-cheese-ai-shipping | 2026 (n/d) | Business press | Built with Claude and Manus; "thousands" recovered | Conflicts with A3B-04 on size |
| A3B-06 | https://www.lateshipment.com/resources/case-studies/plant-addicts/ | n/d | Vendor case study | Plant Addicts $36,968 recovered | Vendor-hosted |
| A3B-07 | https://www.spscommerce.com/deduction-management/ ; https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands ; https://www.inmar.com/blog/insights/martech/hidden-cost-cpg-chargebacks-what-manufacturers-overlook | n/d | Vendor pages | Deductions 1-17% of revenue (varying); invalid share 15-60%; $200-$300 per deduction | Vendor; ranges disagree |
| A3B-08 | https://www.minneapolisfed.org/~/media/files/about/what we do/remittance coalition/2012-crf-deduction-code-study-vcf-fall-conference-butler.pdf | 2012 | Industry survey (Credit Research Foundation) | 70% of invalid deduction dollars recovered (median) | Only independent-style source; 14 years old; summary only |
| A3B-09 | https://www.supplypike.com/customer-stories ; https://supplypike.com/customer-stories/bissell | n/d | Vendor case studies | Bissell >$1M recovered, 20% win-rate gain; E.T. Browne >$1M from Walmart; anonymous $3M disputed | Vendor self-reported |
| A3B-10 | https://govividly.com/our-customers ; https://foodindustryexecutive.com/?p=26377 | n/d | Vendor page; trade press | Health-Ade headline $700K; Glimpse $10M raise, immi, 4-5x ROI claim | Headline only for Health-Ade; vendor claims |
| A3B-11 | https://us.fitgap.com/search/deduction-management-software/small-business ; https://www.foodbevy.com/?p=38999 | 2026 (n/d) | Aggregator/blog | Commission-based pricing models (Glimpse, PACMAN, Promomash) | Aggregator; no prices |
| A3B-12 | https://www.8thandwalton.com/blog/walmart-otif ; https://www.retaildive.com/news/walmart-on-time-in-full-87-suppliers/550102 | n/d | Consultancy; trade press | Walmart 3% of COGS OTIF fine | Trade press corroborates |
| A3B-13 | https://www.supplypike.com/customer-stories/grocery-supplier | n/d | Vendor case study | $158,000/month prepaid-on-time fines (anonymous) | Vendor; anonymous |
| A3B-14 | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 | 2025-10-15 | Trade association release | $849.9B returns, 15.8% rate, 19.3% online, 9% fraud est. | Sponsored by returns vendor; fraud caveat |
| A3B-15 | https://community.shopify.com/t/has-anyone-actually-traced-a-return-spike-back-to-a-specific-supplier-shipment/622026 | 2026 (n/d) | Forum | Batch/shipment layer quote on returns root cause | Anecdote; author type unknown; summary only |
| A3B-16 | https://www.aftership.com/blog/returns-platform-pricing-guide ; https://www.ringly.io/blog/shopify-returns-app ; https://www.cahoot.ai/return-reason-codes/ | 2026 (n/d) | Vendor comparison blogs | Loop, AfterShip, Happy Returns prices; reason-code criticism | Vendor/competitor authored; conflicting prices |
| A3B-17 | https://www.prediko.io/blog/stocky-app-alternatives ; https://eightx.co/blog/compare/how-much-does-cogsy-cost ; https://community.shopify.com/t/what-are-you-actually-paying-for-inventory-forecasting-after-stocky-19-to-199-spread/675887 | 2026 | Vendor blog; consultancy; forum | Prediko/Cogsy/Inventory Planner prices; Stocky shutdown 31 Aug 2026 | Self-serving comparisons; directional |
| A3B-18 | https://www.apprissretail.com/resources/the-other-side-of-shrink-managing-poor-inventory-record-accuracy-percentages/ ; https://www.phocassoftware.com/resources/blog/inventory-shrinkage-leakage | n/d | Vendor blogs | APQC 95% record accuracy; NRF 1.6% shrink; definitions vary | Secondhand; no distributor benchmark |
| A3B-19 | https://distributionstrategy.com/2026/06/the-mid-cap-distributors-pricing-quandary/ ; https://distributionstrategy.com/report/closing-the-execution-gap/ | 2026-06; n/d | Trade consultancy | 100-300 bps margin leakage; 3-5% of revenue execution gap (84 respondents) | Abstract-level; not opened |
| A3B-20 | https://pros.com/learn/distribution/industrial-distributor-optimizes-pricing-for-millions-in-profit ; https://conga.com/customer-stories/distributor-improves-pricing-and-sales ; https://www.profitoptics.com/case-studies/fortune-150-distributor | n/d | Vendor case studies | Metalwork $3.8M/$18M anticipated; $41M and $50M anonymous leakage cases | Vendor; enterprise; anonymized |
| A3B-21 | https://attribuly.com/blogs/triple-whale-pricing-review/ ; https://thecmo.com/tools/northbeam-review/ ; https://www.ringly.io/blog/triple-whale-alternatives ; https://www.g2.com/products/triple-whale/pricing | 2026 | Affiliate/review sites | Triple Whale, Northbeam, Polar pricing; attribution "decision-support" caveat; G2 single negative review | Affiliate-driven; prices conflict |
| A3B-22 | https://www.mrpeasy.com/mrpeasy-vs-katana ; https://www.capterra.com/p/172888/Katana-MRP/pricing/ | 2026 | Vendor; aggregator | MRPeasy $49-$149/user/month; Katana $299+/month, conflicting | Aggregator conflicts; no variance-feature confirmation |
| A3B-23 | https://www.helium10.com/tools/operations/managed-refund-service/ ; https://jarvio.io/best-amazon-reimbursement-tools | 2026 | Vendor; affiliate roundup | Refund Genie, Managed Refund Service, Getida 25%, Seller Investigators 10% | Fee attributions conflict |
| A3B-24 | https://www.apexanalytix.com/resources/blog/recovery-audit-cost/ ; https://fmx.cpa.texas.gov/fm/audit/recovery/rpt2021/Recovery_Audit_2021.pdf | n/d; 2021 | Vendor; state report | 20-30% recovery-audit contingency; Texas 14%/22.5%; 92% duplicates from coding errors | Vendor; government figure is public-sector contracts |
| A3B-25 | https://nam.org/?p=36966 ; https://documents.nam.org/COMM/Tariff_One_Pager_2025.pdf ; https://www.bostonfed.org/publications/current-policy-perspectives/2025/who-pays-for-tariffs ; https://www.manufacturingdive.com/news/manufacturers-plan-price-hikes-over-reshoring-to-combat-tariff-effects-ism/808157/ | 2025 | Trade association; Fed research; trade press | Cost increase 7.7%, 87% may raise prices; partial pass-through (Boston Fed); ISM 86% pass some | Best independent set here; summaries only |
| A3B-26 | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/4b65fb9e-971c-4eb1-a363-6c56d5fc5287 ; https://sellercentral-europe.amazon.com/seller-forums/discussions/t/5ee8861a-bad5-471b-9ae9-0ab314c0ffb5 ; https://amzadvisers.com/fba-mistakes/ | 2025-2026 (n/d) | Forum; agency blog | FBA inbound shortfalls, denied reimbursements; 1-3% FBA revenue claim | Anecdote; agency estimate |
| A3B-27 | https://www.spscommerce.com/community/articles/3pl-performance-benchmarks-how-to-verify-your-3pls-numbers ; https://redstagfulfillment.com/how-to-manage-3pl-performance/ | 2025-2026 | Vendor/3PL blogs | 3PL on-time benchmarks 97-99.9%, definition drift | 3PL-authored |
| A3B-28 | https://shipperhq.com/blog/carrier-rate-increases-2026 ; https://www.digitalcommerce360.com/2026/03/26/analysis-shipping-surcharges-surge-carriers-ecommerce-economics/amp/ | 2026-03 | Vendor blog; trade press | 5.9% GRI; surcharges as primary cost driver | No independent surcharge-share figure |
| A3B-29 | https://community.shopify.com/t/inventory-oversold-with-settings-set-up-correctly/379787 ; https://community.shopify.com/t/bundle-sold-but-components-didnt-decrement-how-are-you-catching-oversells/658245 ; https://www.linnworks.com/blog/shopify-inventory-tracking-multichannel/ | 2025-2026 | Forum; vendor | Oversell and sync-failure pain; silent sync stoppage | Titles/snippets only |
| A3B-30 | https://us.fitgap.com/search/supplier-relationship-management-srm-software/small-business | 2026 | Aggregator | SRM pricing largely undisclosed; one tool from $199; Coupa mid-high five figures | Aggregator; thin |
| A3B-31 | https://www.indiehackers.com/post/52994bba83 | n/d | Indie forum | Indie inventory-sync tool suggests showing mismatches to build trust | Anecdote; not evidence of demand |
| A3B-32 | https://www.parcelperform.com/insights/stop-carrier-overcharges-automated-auditing | n/d | Vendor | Freight bills with errors (Trax 15-25%; "up to 10%") | Vendor; secondhand |
| A3B-33 | https://reddit.birdcat.cafe/r/shopify/comments/1ki23z5/4200_chargeback_yikes | 2025-05-08 | Reddit mirror | $4,200 chargeback reversed after three weeks of evidence | Anecdote; payment chargebacks, adjacent to scope |
| A3B-34 | /home/user/Metrial-AI-Model/research/appendix/agent2_market.md | 2026-11-19 | Internal Phase 1 | Baseline price anchors and vendor figures not repeated here | Mostly vendor-sourced |

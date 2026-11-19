# Phase 2, Agent 1: Margin Investigator re-validation

Date: 2026-11-19. Scope: try to disprove, as well as support, the Phase-1 hypothesis that "margin erosion investigation" is a problem a small team can sell as a separate paid product to small/mid distributors, wholesalers, specialty ecommerce brands and small manufacturers.

## 0. Method and limits (read first)

- **WebFetch was blocked for every host I tried** (DNS failed in this session's network policy): distributionstrategy.com, mdm.com, zilliant.com, g2.com, community.shopify.com, news.ycombinator.com, simon-kucher.com, mckinsey.com. I fetched zero primary pages. Reddit is also blocked for WebSearch domain filters.
- Everything below therefore comes from **WebSearch result summaries only** (a model-written digest of search hits, not raw page text). Statistics are as reported in those digests and should be re-checked against the primary page before anyone cites them externally. Where a digest itself quoted a phrase, I reproduce it and mark it "quoted in search digest".
- **I did not retrieve a single actual Reddit or Hacker News thread.** The only forum-like material I saw is Shopify Community threads and one r/FPandA thread, both only as search-digest paraphrases. No customer-interview-grade quotes exist in this file. The Phase-1 gap ("no direct customer discussion") is **not closed**.
- Evidence tags: [PRIMARY] first-party data or filing; [VENDOR] vendor-run survey/case study/marketing; [ANALYST] consultancy, trade association or industry-media research; [INDEPENDENT-REVIEW] third-party review sites; [COMMUNITY-ANECDOTE] forum/social posts; [ASSUMPTION] my inference. I found no [PRIMARY] evidence and no peer-reviewed academic work on small-distributor margin leakage in this pass; the McKinsey/HBR items are consultancy-published [ANALYST].
- Source IDs refer to the SOURCE REGISTER at the end.

## 1. How frequently do target companies experience gross-margin erosion?

**Pressure is near-universal and recent; "erosion" frequency is not measured as an incidence rate anywhere I found.**

- Tariff/cost shock, distributors: NAW/MDM 2025 survey: about 62% expected COGS to rise by 10% or more in 2025, and NAW's CEO said about a third faced supplier hikes of 25%+. [ANALYST] (A1-01, A1-02)
- Response: 2Q26 Baird-NAW survey (about 300 respondents, mostly distributors): 91% raise prices in response to rising COGS, but 33% absorb at least part of the increase. [ANALYST] (A1-03)
- Ecommerce brands, tariffs (several surveys, different samples, not comparable): Portless (Feb 2026) 92% raised prices and 79% absorbed some margin loss; Clearco (May 2025, 97 founders) 80% raised prices by typically 5-15%; Omnisend (Dec 2025, 170 SMB owners) only 39% raised prices while 54% made significant changes. [VENDOR] (A1-04 to A1-07). The spread (39% to 92%) shows the sample/definition noise; direction (tariffs hit margin) is consistent.
- Distributor "execution gap": Distribution Strategy Group (DSG)/Cavallo report (84 participants per the digest) estimates distributors lose 3-5% of revenue (about 150-200 bps of margin opportunity) to incomplete supplier pass-through, manual pricing errors, small-order losses and unauthorized discounts. [ANALYST, consultancy-sponsored] (A1-08)
- DSG June 2026: "most mid-cap distributors leak 100 to 300 basis points of margin a year" (digest wording), for firms of roughly $100M-$1B revenue. [ANALYST; the 100-300 bps figure is asserted in an article, methodology not seen] (A1-09)
- Older, smaller-scale numbers: Intuilize-sourced MDM slide: manual cost-increase-to-price-increase lag can erode 1-3 margin points; a secondary source cites 1.6% from delayed cost updates (Intuilize, 2021). [VENDOR] (A1-10)

**Assessment:** The *problem* (margin leakage, cost-price lag) is well-evidenced across trade media. What is absent is evidence on how often a *typical $5-50M company* experiences an episode large enough to trigger investigation. The 1-5% figures all come from parties who sell pricing software or consulting. Note that DSG/Cavallo's sponsor sells pricing consulting; Zilliant's "up to 28.47% of revenue" is an upper-bound claim the digest itself called aggressive (A1-11). I discount all of these. [ASSUMPTION: a realistic recoverable leak for a small distributor is likely under the 100-300 bps range; no source tests this.]

Sizing note: even taking 100 bps at face value, a $20M distributor's leak is $200K/year gross, of which a standalone tool realistically captures a fraction. This is the same arithmetic Phase 1 used ($100K for 50 bps); it does not become better evidence by repetition.

## 2. How do they discover and investigate it today?

- **Spreadsheets dominate.** Vendavo/Copperberg 2025: 85% of manufacturers and distributors still rely on spreadsheets for pricing decisions (including more than half of those claiming automation); only 14% report fully scalable modern pricing systems; 46% partially automated; 29% evaluating. Senior pricing/commercial/finance respondents, North America and Europe. [VENDOR; Vendavo sells pricing software, Copperberg is a consultancy] (A1-12). Zilliant has a similar survey (84% manual), also [VENDOR]. (A1-12 digest)
- **Cost-plus and gut feel.** Simon-Kucher 2026 (239 senior leaders, NA and Europe, August): 52% primarily set prices by markup on cost (this 52% was attributed in digests ambiguously; treat as unconfirmed). [ANALYST] (A1-13)
- **Waterfall visibility missing.** Revify (via DSG June 2026): more than half of mid-market firms Revify diagnosed had never built a complete waterfall from list price to pocket margin; only about 10% ranked high on foundational pricing-engine inputs; a related Revify survey of 250+ commercial leaders: about one in ten mid-market companies consistently uses analytics to drive pricing. [VENDOR/consultancy, secondary relay] (A1-09, A1-14)
- **Customer profitability is measured but not used.** DSG/Cavallo: 69% of respondents say they track customer profitability, but only 34% give sales teams real-time access. The report's thesis is "execution, not data." [ANALYST] (A1-08)
- **Month-end variance in Excel.** One r/FPandA thread (Mar 2024) about building gross-margin variance (price/volume/mix, channel, client) in Excel: the poster said individual mix effects did not sum to the total mix impact. Seen only as a digest paraphrase. [COMMUNITY-ANECDOTE, one thread, unverified] (A1-15). FTI Consulting and Zebra BI publish PVM methods/templates, which shows the technique is commodity knowledge. [VENDOR/ANALYST] (A1-16)
- **Shopify merchants:** per search digests of Shopify Community threads, native reports show margin only if COGS is entered, store one cost per variant (historical margins get recalculated at today's cost), and omit ad spend, fees and shipping labels; commenters suggest snapshotting cost at sale and cost tables with effective dates, or a scheduled Shopify Flow to flag low-margin items. [COMMUNITY-ANECDOTE, some posters are app vendors] (A1-17)

**Assessment:** Spreadsheets and ad hoc analysis are the current method; this supports "manual". It also shows that the first-order fix in many cases is *data hygiene and a pricing process* (cost snapshots, waterfall, discount rules), which is what DSG/Revify say must come "before buying technology" (A1-09). That is a risk for an analytics-first product: the customer's blocker may be inputs, not investigation.

## 3. What tools do they use?

- ERP/accounting reports (NetSuite, Epicor, Acumatica, Sage, QuickBooks/Xero) plus Excel. [ANALYST/VENDOR]
- Distributor BI/analytics: Phocas (margin drill-down by rep/branch/product/customer, 200+ connectors; no published price list; one unverified third-party estimate of $150/month minimum). [VENDOR] (A1-18)
- Distributor price-cost automation: Intuilize (CEO article on gross-margin variance analysis, vendor pitch) (A1-19).
- Enterprise pricing: Zilliant, PROS, Pricefx, Vendavo (custom quote; a single third-party guide, Feb 2026, says Vendavo typically $75K-$200K/yr and 4-18 month implementations by vendor, unverified; guide recommends Pricefx for $50M-$250M B2B firms; editorial) (A1-20).
- Shopify profit apps: TrueProfit (about $35/month per a competitor roundup), BeProfit (about $49/month), Lifetimely (free to roughly $49-$149), Triple Whale (about $129-$259+ by GMV), Polar Analytics (from about $300-$720/month). Prices are from third-party blogs and conflict; verify on vendor pages. [VENDOR/third-party blogs] (A1-21, A1-22)
- Inventory/ERP-lite: Cin7 (actual costing recalculates COGS on tariff changes, per vendor), Katana; Phocas integrates with Cin7. [VENDOR] (A1-23)

## 4. What do existing tools do well?

- Product/channel/customer margin drill-down is solved in Phocas-type BI and in Shopify profit apps (once COGS and ad spend are connected). Vendor testimonials: Robert Welch Designs "margin analysis in a few clicks," Abcoe "barrier to entry is very small" (vendor-hosted, digest). [VENDOR] (A1-18)
- Rule-based pricing execution at scale: enterprise pricing vendors claim 50-144 bps margin lift: Zilliant building-products 120 bps and foodservice 50 bps and 134 bps/20x ROI; Pricefx automotive distributor 144 bps and +13.1% gross margin at 3 months; PROS Fortune-500 distributor 120 bps; Infor +1.3% gross margin. [VENDOR; best-case, self-selected, large customers] (A1-24)
- Shopify profit app reviews are mostly positive for TrueProfit (4.9 across 900+ per one tracker) with BeProfit lower (about 4.1-4.2, billing/cancellation and ad-cost accuracy complaints). [INDEPENDENT-REVIEW, aggregator-relayed; I found no churn data] (A1-25)

**Key implication:** the "show me margin by SKU/customer" job is already served cheaply. A margin product must win on the *explanation* layer (why), not the *visibility* layer.

## 5. What remains difficult, expensive, slow or manual?

- Cross-system causal decomposition (price vs cost vs mix vs freight vs discount vs returns) beyond what a single BI tool is configured to show: evidenced indirectly (manual Excel PVM that does not reconcile; Intuilize and DSG describing manual variance work). [mixed, weak] (A1-15, A1-19)
- Pass-through lag: supplier reconciliation cycles of 3-6 months (DSG, abstract only per Phase 1); manual cost-to-price updates. [ANALYST] (A1-10)
- Execution: getting profitability data to people who quote and price (34% real-time access). [ANALYST] (A1-08)
- Enterprise pricing projects are slow and heavy: 4-18 months, at least 0.5 FTE, dedicated pricing ops (single unverified guide). [VENDOR/third-party] (A1-20)
- Shopify cost accuracy: landed cost, per-variant COGS, refunds counted as issued, matched-vs-total ad spend. [COMMUNITY-ANECDOTE + vendor blogs] (A1-17, A1-25)

Observation: most listed difficulties are *data input and process* problems. An AI "investigator" does not remove the need for clean cost data; it consumes it.

## 6. Who feels the pain most directly?

- The **owner/GM** of a small firm (sees margin % fall at month end and cannot explain it). [ASSUMPTION; no survey asked this]
- **Controller / finance lead** who is asked to explain the gross-margin variance at close (r/FPandA example above). [COMMUNITY-ANECDOTE, single thread]
- **Sales/pricing roles** who set quotes without margin visibility (DSG 34% stat; MDM "front-line teams making the pricing decisions" recommendation seen in digest). [ANALYST]
- For ecommerce brands: the founder/operator doing it in a spreadsheet; Shopify Community posts. [COMMUNITY-ANECDOTE]

## 7. Who owns budget and can approve a purchase?

No survey I found answers this for small firms. Evidence is circumstantial:

- DSG-quoted former Graybar pricing VP: ownership varies; some have a pricing VP, some an analytics team, some marketing, some sales executives. [ANALYST, one quote] (A1-26)
- Simon-Kucher: 55% of firms with $500M+ revenue have invested in pricing tools/analytics/dashboards vs 27% of smaller companies; discount discipline was identical in both groups. [ANALYST] (A1-13). Small firms invest less, and the invested-in category includes cheap dashboards.
- DSG 2026 (128 distributors): most have a pricing approach, far fewer a pricing system; split between pricing-as-strategy and pricing-as-back-office. [ANALYST] (A1-26)

**Assessment [ASSUMPTION]:** In a $5-50M company the buyer is the owner or a finance lead, with sales leadership as a veto. Distributor pricing is a sales-owned function in many firms, meaning the person with budget (finance) may not own the behavior to be fixed (sales). This is a go-to-market risk for a finance-facing investigation tool.

## 8. Realistic financial impact (by source type)

| Source type | Figure | Caveat |
|---|---|---|
| Consultancy (McKinsey, 2003 and later) | 1% price rise, volume constant, yields about 8% (or 8.7% per McKinsey web page) operating-profit increase; managing pocket-price waterfall often finds 1% or more in realized price [ANALYST] (A1-27) | Large-company S&P 1500 base; 8.7% vs Marn/Rosiello 11.1% attributions conflicted in digest; operating leverage claim is arithmetic, not a measure of what a tool delivers |
| Trade association (NAW/MDM) | 62% expect COGS +10%; 33% of respondents absorb part of cost increases [ANALYST] (A1-01, A1-03) | Measures pressure, not recoverable dollars |
| Consultancy/trade (DSG/Cavallo, DSG/Revify) | 3-5% of revenue or 100-300 bps leak [ANALYST] (A1-08, A1-09) | Sponsor sells services; method not seen |
| Vendor (Zilliant/PROS/Pricefx/Infor) | 50-144 bps lift [VENDOR] (A1-24) | Large distributors; no sub-$100M case found |
| Vendor (Revify) | Lag costs 8-11% of recoverable profit [VENDOR] (A1-14) | Self-interested, secondary |
| Rebate/chargeback auditors (ProfitOptics, PRGX) | Single cases of $1.9M and $11.3M recovered; "$1M per $1B" (about 0.1%) [VENDOR] (A1-28) | Different problem (claims/rebates), large firms; no fee % disclosed |
| Academic/independent | None found | Gap |

**Reading:** the impact is real in principle but the per-customer recoverable dollars for a firm under $50M are unmeasured. The only vendor results come from firms with $100M+ revenue and dedicated pricing teams. The 8.7% operating-profit leverage argument is not evidence that an *investigation* product gets a customer a price increase; the customer still has to change prices, and the DSG "execution gap" thesis says that is the hard part.

## 9. Urgency: what triggers action?

- **Supplier price increases and tariffs** (strongest, repeatedly documented 2025-2026): NAW/MDM, Baird-NAW, ecommerce surveys above. [ANALYST/VENDOR] Counterpoint: the tariff regime itself changed (a trade-press title refers to a Supreme Court ruling striking down tariffs; I did not verify the details), so a tariff-triggered wave may be time-limited. [ASSUMPTION on durability]
- **Month-end close variances** (recurring, weak urgency unless large). [ASSUMPTION]
- **Lenders/covenants:** I found only indirect material (ABL covenant case studies; an ABI article converting margin to sales shortfall, e.g. at 25% margin a $400K variance equals $1.6M sales shortfall). No source ties a gross-margin covenant to purchase of a margin tool. [ANALYST, indirect] (A1-29)
- **PE ownership / ERP migration:** no evidence retrieved in this pass; Phase 1 asserted them. [ASSUMPTION]
- **Pattern in the survey data:** the dominant response to cost pressure is a single blunt action (raise prices; 91%) rather than investigation, per the MDM column title "Your Costs Changed in 3 Places During 2Q26. Your Pricing Changed Once." (title and intro only seen; body not retrieved) (A1-03).

## 10. Evidence that companies PAY for a separate product

What I found, ranked from most to least relevant to a $349-$999/month investigator:

1. **Shopify profit apps exist at $35-$720/month with hundreds to 900+ reviews** (TrueProfit, BeProfit, Lifetimely, Polar, Triple Whale). This is real WTP for *profit visibility* at a low price point, in a crowded category. [INDEPENDENT-REVIEW/VENDOR] (A1-21, A1-22, A1-25). It supports "merchants pay about $35-$300", not "$349-$999".
2. **Enterprise pricing software is bought by large distributors** at roughly $75K-$200K/yr (one unverified source). Evidence of WTP at the top of the market only. (A1-20, A1-24)
3. **Distributor analytics (Phocas, Intuilize)** have named case studies, but these are vendor-hosted and contain no disclosed prices. (A1-18, A1-19)
4. **Contingency/outcome audits exist** (ProfitOptics rebate audit at "no upfront cost"; PRGX paid only on recovery), but fee percentages are undisclosed. (A1-28)
5. **Consultant rates**: a vendor blog puts distribution consultants at $150-$600/hour, $5-20K/month, $20-80K projects (unverified, generic). [VENDOR blog] (A1-30). This is a ceiling-anchor for a human-assisted service, not proof of purchase.
6. **Survey interest**: MDM/Baird: 27% of distributors ranked pricing/margin optimization their #1 AI investment area; 74% have pricing AI on the roadmap; but only 13% deployed AI in pricing workflows (Vendavo report, secondary). [ANALYST/VENDOR] (A1-12, A1-31). Roadmap interest is a weak WTP signal.

**What I did NOT find:** a named small-company customer of a standalone margin-explanation product with a stated dollar result and price paid; any G2/Capterra review set for a margin-investigation product at SMB price points (G2/Capterra data found was for enterprise pricing tools: Pricefx 4.4 from 112 reviews, Zilliant 4.4 from 61, Enterprise-weighted); any willingness-to-pay interviews.

## Contradictory evidence

1. **The market's response to margin pressure is mostly "raise prices", not "investigate".** 91% raise prices (Baird-NAW). Investigation tools compete with a blunt but free action. (A1-03)
2. **The binding problem is often execution and foundations, not insight.** DSG says "the problem is execution, not data" and recommends building the price waterfall before buying technology; Revify says only about 10% of mid-market firms have the foundations a pricing engine needs. A product that outputs a clever explanation to a firm without cost snapshots or discount discipline may produce shelfware. (A1-08, A1-09)
3. **Visibility already exists at low cost.** Phocas-type BI drills margin to customer/SKU "in a few clicks"; Shopify profit apps cost $35-$300; vendor testimonials say entry barriers are small. The unmet part is "explanation," which a competent controller can do in Excel PVM (commodity technique; FTI, Zebra BI). (A1-16, A1-18, A1-21)
4. **Small firms invest less in pricing tooling** (27% vs 55% at larger firms), which cuts against the small-company target. (A1-13)
5. **No sub-$100M proof from the paid pricing market.** Every quantified vendor win I saw is a large distributor. (A1-24)
6. **Crowded low-price anchors in ecommerce.** Four to five funded profit apps; BeProfit's reviews cite billing/cancellation friction and ad-cost accuracy issues, so even the incumbent set has trust problems. No churn data found either way. (A1-22, A1-25)
7. **Tariff urgency may fade.** A trade-press title referencing a Supreme Court ruling against tariffs and merchants "not lowering prices" (Feb 2026) suggests the shock is not monotonic; I did not verify details. (A1-32) [ASSUMPTION]
8. **Dead or struggling products in adjacent space:** Phase 1 already covered Sisu/Chartio/Peak outcomes. In this pass I found no *margin-specific* analytics startup shutdown (search digest said none clearly matched); Prayas Analytics (retail analytics) shut down "due to lack of customer growth" per its founder (digest), and Neta (commerce, not analytics) cited "Product Margin" as its "Achilles heel". Both are adjacent only and do not demonstrate that margin tools fail. (A1-33) Absence of a found failure is not evidence of success.
9. **Accuracy is the product, and I found no precedent for explanation-accuracy at SMB data quality.** Reviews of profit apps stress COGS, refund and ad-spend input errors (A1-25), so an "investigation" layer inherits those errors.

## What is still unknown and the cheapest way to learn it

| Unknown | Cheapest test | Pass/fail signal |
|---|---|---|
| Will anyone pay for *explanation*, vs visibility? | Offer 10-15 businesses a paid ($500-$1,500) one-time "why did margin move" memo done by hand from exports. Charge up front; do not give it free. | At least 4 of 15 pay before seeing results; at least 2 say they would pay monthly |
| Who signs? | In the first 10 discovery calls ask "who would approve $500/month for this?" and "who sets sell prices?" | Buyer consistent (owner or finance) and not blocked by sales |
| Recoverable dollars at $5-50M | In each paid memo, log identified leak $ and whether the customer acted | Median identified leak above 10x annual price |
| Is data foundation the blocker? | Time the data cleaning per customer; count how many lack cost-at-sale history | Under 6 hours per customer; at least 60% have usable cost history |
| Real customer voice | Obtain Reddit/HN/Shopify Community/IH threads by a human or an allowed-network session (this session could not) and 10 interviews via accountants/fractional CFOs | Unprompted description of the pain with a dollar figure |
| Do cheap tools already satisfy them? | Ask each prospect what they use now (Phocas/Excel/TrueProfit) and why it is insufficient | At least half name a specific unmet gap |
| Primary-source verification | Re-run the key stats (DSG, NAW, Simon-Kucher, Vendavo/Copperberg) from primary pages in a session with network access | Numbers match digests |

## Verdict: does this support a separate paid product?

**WEAK-TO-MODERATE for the problem; INSUFFICIENT for willingness to pay a separate $349-$999/month product.** Overall rating: **WEAK** pending the paid-memo test above.

Why not higher:
- The evidence base is almost entirely vendor, consultancy and trade-media sourced, seen only through search summaries; zero primary documents were opened and zero actual Reddit/HN threads retrieved.
- Evidence of payment exists at two ends: cheap Shopify profit apps ($35-$300/month) and enterprise pricing suites ($75K+/year, large firms). The middle (a $349-$999/month tool for $5-50M companies) has no named paying customer in anything I found.
- The dominant behavior under margin pressure is to raise prices; the dominant stated barrier is execution/foundation, which a diagnostic product does not by itself fix.
- Where visibility is the gap, existing low-price tools serve it. The "why" claim is plausible but untested, and requires clean cost data the target companies often lack.

Why not lower:
- The problem is consistently documented across independent-ish trade bodies (NAW/MDM, DSG), not just vendors; supplier cost shocks in 2025-26 were severe; manual spreadsheet investigation is the norm; ecommerce merchants do pay for profit visibility.
- Contingency audits and human-delivered services demonstrate that outcome-linked margin recovery is sellable in adjacent forms.

**Practical reading for the founder:** the evidence supports testing a *paid, human-assisted diagnostic* (priced near consulting anchors, sold through accountants/fractional CFOs) before building any product; it does not support committing engineering to a standalone subscription yet. If fewer than about 4 of 15 prospects pay for the manual memo, treat the hypothesis as disproved for this segment.

---

## SOURCE REGISTER

All entries were seen only as WebSearch result titles/summaries unless noted; no page was opened (WebFetch blocked). Dates are as shown in the search results or the cited title where visible; "n/d" means no date seen.

| ID | URL | source date | source type | claims supported | reliability note |
|---|---|---|---|---|---|
| A1-01 | https://www.mhlnews.com/transportation-distribution/news/55287944/tariffs-driving-cost-for-wholesale-distribution-industry | 2025 | trade media reporting NAW/MDM survey | 62% expect COGS +10% | Secondary; NAW primary page not opened |
| A1-02 | https://www.supplychain247.com/article/tariffs-increase-distributors-naw-mdm-survey/freight_rates | 2025 | trade media | one-third face supplier hikes of 25%+; 37% >20% China inventory | Secondary |
| A1-03 | https://www.mdm.com/article/featured/featured-main/research-your-costs-changed-in-3-places-during-2q26-your-pricing-changed-once/ | 2026 (2Q26) | trade association/industry media column on Baird-NAW survey | 91% raise prices; 33% absorb part; sub-$100M single blunt response | Title and intro only; body not seen |
| A1-04 | https://chainstoreage.com/survey-wide-majority-e-commerce-brands-raised-prices-response-tariffs | 2026 | trade media on Portless survey | 92% raised prices, 79% absorbed margin loss | Vendor survey (logistics startup) |
| A1-05 | https://clear.co/blog/ecommerce-price-increase-trade-war | 2025 | vendor blog (Clearco survey, 97 founders) | 80% raised prices 5-15% | Small sample, vendor |
| A1-06 | https://www.omnisend.com/latest-news/54-of-online-retailers-impacted-by-tariffs-39-hiked-prices-with-plans-for-more/ | Dec 2025 | vendor survey (170 SMB owners) | 39% raised prices; 54% significant changes | Small sample, vendor |
| A1-07 | https://www.signifyd.com/?p=59206 | 2025 | vendor survey (500 retail pros) | 75% raised prices due to tariffs | Vendor; not Shopify-specific |
| A1-08 | https://distributionstrategy.com/report/closing-the-execution-gap/ (and https://www.cavallo.com/blog/how-to-close-the-execution-gap-thats-costing-distributors-millions/) | n/d | consultancy/analyst report | 3-5% revenue leak; 69% vs 34% profitability stat; 150-200 bps in 12-18 months | Sponsor sells consulting; 84-participant sample per digest; not opened |
| A1-09 | https://distributionstrategy.com/2026/06/the-mid-cap-distributors-pricing-quandary/ | Jun 2026 | analyst article (Revify-linked) | 100-300 bps leak; waterfall not built; build waterfall before tech; 10% foundation | Methodology unseen |
| A1-10 | https://www.mdm.com/wp-content/uploads/2021/12/Webinar-Dec-2-Final-v2.pdf (and https://archive.distributionstrategy.com/?p=4786) | 2021 | vendor presentation (Intuilize) via trade media | 1-3 pt margin erosion from manual lag; 1.6% from delay | Old, vendor |
| A1-11 | https://zilliant.com/reports/distribution-edition-2024-global-b2b-distribution-benchmark | 2024 | vendor report | "up to 28.47%" revenue loss claim; 11% margin whitepaper | Aggressive upper bound; not opened |
| A1-12 | https://www.vendavo.com/pricing/pricing-strategy-holding-you-back/ (and https://www.copperberg.com/?p=16774) | 2025 | vendor + consultancy survey | 85% spreadsheets; 14% modern systems; 13% AI in pricing | Vendor-sponsored; report not seen |
| A1-13 | https://www.simon-kucher.com/en/insights/2026-wholesale-and-distribution-industry-report | Aug-2026 survey | consultancy report | 239 leaders; 55% vs 27% pricing tool investment; discount discipline equal | Digest only; 52% markup stat attribution unclear |
| A1-14 | https://www.mdm.com/article/technology/ai/the-hidden-majority-your-ai-is-writing-emails-your-competitors-ai-is-finding-margin/ | 2025-26 | industry media | 27% rank pricing AI #1; 74% on roadmap; Revify 8-11% lag cost | Mixed-source stats; secondary |
| A1-15 | https://axebps-redlib.hf.space/r/FPandA/comments/1bivmoq/variance_analysis | Mar 2024 | forum mirror (r/FPandA) | Manual Excel mix analysis does not reconcile | Digest paraphrase only; single thread |
| A1-16 | https://www.fticonsulting.com/insights/white-papers/quantifiable-approach-price-volume-mix-analysis ; https://zebrabi.com/?p=45893 | n/d | consultancy/vendor | PVM is documented commodity method | Methodology, not demand evidence |
| A1-17 | https://community.shopify.com/t/profit-ad-spend-tracking-on-shopify-whats-actually-broken-for-you/646399 ; https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805 | 2025-26 | forum | Shopify cost-per-item limits; missing ad spend/fees | Digest only; some posters are app vendors |
| A1-18 | https://www.phocassoftware.com/industries/wholesale-distribution/pricing-strategy ; https://www.erpresearch.com/erp-add-ons/embedded-bi/phocas-analytics/pricing | n/d | vendor | Margin drill-down; no published price; testimonials | Vendor-hosted; price estimate unverified |
| A1-19 | https://www.inddist.com/technology-software/blog/22936818/unlocking-hidden-profits-how-wholesale-distributors-can-combat-margin-compression-with-advanced-variance-analysis | n/d | vendor article (Intuilize CEO) | Gross-margin variance analysis offering | Product pitch |
| A1-20 | https://datatoolindex.pages.dev/use-cases/best-pricing-analytics-software-b2b-industrial/ | Feb 2026 | third-party guide (low-authority aggregator) | Vendavo $75-200K/yr; 4-18 month implementations | Unverified; aggregator |
| A1-21 | https://trueprofit.io/blog/beprofit-alternatives ; https://www.ringly.io/blog/trueprofit-alternatives | 2026 | vendor/competitor blogs | TrueProfit about $35/mo; BeProfit about $49/mo | Biased comparison pages |
| A1-22 | https://attribuly.com/blogs/triple-whale-pricing-review/ ; https://useamp.com/alternatives/lifetimely-vs-polar-analytics | 2026 | third-party blogs | Lifetimely, Triple Whale, Polar price ranges | Conflicting figures |
| A1-23 | https://www.phocassoftware.com/integrations/cin7 | n/d | vendor | Cin7 actual costing; Phocas+Cin7 | Vendor claims |
| A1-24 | https://zilliant.com/case-studies/foodservice-distributor-lifts-margin-rate-50-basis-points-year-over-year-with-zilliant ; https://www.pricefx.com/resources/customer-story/automotive-distributor ; https://pros.com/learn/blog/how-pros-helped-fortune-500-distributor-optimize-pricing-seven-billion-revenue ; https://www.infor.com/en-sg/blog/ai-pricing-for-distributors | various | vendor case studies | 50-144 bps lifts | Anonymous/large customers; best-case |
| A1-25 | https://appnavigator.io/app/trueprofit/reviews/?page=2 ; https://apps.shopify.com/reviews/2181628 | 2026 | review aggregator/app store | TrueProfit about 4.9; BeProfit about 4.1-4.2 with billing and ad-cost complaints | Aggregator-relayed; no churn data |
| A1-26 | https://distributionstrategy.com/report/the-state-of-distributor-pricing-and-costing/ ; https://distributionstrategy.com/2024/02/distributors-want-better-pricing-focus-on-the-right-people-processes-and-technology/ | Mar 2026; Feb 2024 | analyst report/article | 128 distributors; ownership of pricing varies | Role breakdown not seen |
| A1-27 | https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/bringing-discipline-to-pricing ; https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/using-big-data-to-make-better-pricing-decisions | 2003; later | consultancy | 1% price about 8-8.7% operating profit; pocket-price leakage 1%+ | Large-company base; attribution of 8.7% vs 11.1% unclear |
| A1-28 | https://www.profitoptics.com/rebate-audit ; https://www.prgx.com/resources/blog/how-prgx-grows-net-profit/ | n/d | vendor | Contingency/no-upfront audits; $1.9M and $11.3M cases | Fee % undisclosed; different problem |
| A1-29 | https://www.abfjournal.com/?p=38657 ; https://jsheld.com/case-studies/reducing-inventory-allows-for-refinancing-for-agriculture-distributor | n/d | trade/advisory | Margin-to-sales-shortfall math; ABL covenant cases | Indirect only |
| A1-30 | https://syncgtm.com/blog/how-much-does-an-leadership-sales-distribution-digital-marketing-staff-development-consultant-cost | May 2026 | vendor blog | Consultant rates $150-600/hr; $20-80K projects | Generic, unverified |
| A1-31 | https://www.descartes.com/sites/default/files/media/documents/2026-05/MDM-NAW-Research-Paper-In-Pursuit-of-Value-Where-400-Distributors-are-Investing-in-AI-Today-April-2026.pdf | Apr 2026 | trade association research | AI investment interest by distributors | Listed in results; contents not retrieved |
| A1-32 | https://www.modernretail.co/operations/marketplace-briefing-online-merchants-arent-lowering-prices-despite-supreme-court-ruling/ | Feb 2026 | trade media | Tariff regime change; merchants not lowering prices | Title only; details unverified |
| A1-33 | https://technical.ly/startups/prayas-analytics-shutdown-pranshu-maheshwari.md ; https://nicolasabad.substack.com/p/startup-post-mortem-neta?open=false | n/d | founder post-mortems | Adjacent failures (retail analytics; commerce margin) | Adjacent, not margin-analytics failures |

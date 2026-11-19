# 03 — ICP and Buyer Analysis

**Source:** `appendix/p2_a4_icp_buyer_inbound.md` (40 sources, A4-xx). **Evidence limit:** WebFetch failed for api.census.gov, shopify.dev, developer.xero.com, mdm.com, smb-gr.com; segment counts are partly missing or conflicting; keyword demand is unmeasured; no interviews exist.

## 1. The honest finding
**No segment is both easy to reach through inbound *and* able to pay the price a services-heavy product needs ($600+ blended).** For 30-day inbound feasibility: Shopify-first brands > accountant-led firms > distributors. For willingness to pay at $600+: distributors > accountant-led > Shopify-first. Desk research cannot resolve this; a two-track test can.

## 2. Segment comparison

| Segment | Typical stack | Who does finance | Budget behavior | Trigger events | Inbound reachability | Verdict |
|---|---|---|---|---|---|---|
| **Shopify-first brands with a wholesale channel** | Shopify + QBO/Xero + ads + 3PL | Founder + part-time bookkeeper; often fractional CFO | App-store billing norm; analytics apps $49–750/mo (aggregator prices) | Tariff/landed-cost change; margin fall after wholesale launch; inventory loan; year-end | **High** (Shopify App Store, Community, r/ecommerce) but ~17,591 apps and free in-product AI | Easiest to reach, lowest price ceiling |
| **Specialty distributors / wholesalers ($10–75M)** | NetSuite, Acumatica, Epicor, QB Enterprise, Odoo + Excel price lists | Controller/CFO at $20M+; owner + bookkeeper below | ERP-reseller and CFO decisions; no self-serve evidence | Tariff supplier hikes (NAW May 2025: one-third faced 25%+); PE/ERP migration (unsourced) | **Low** (resellers, trade events, peers) | Best pain, worst inbound; pass-through contradiction (§4) |
| **Accountants / fractional CFOs serving product SMBs** | QBO/Xero + Fathom-type tools | The firm itself | Per-client pricing; 94% of US firms offer advisory | Clients asking "why did margin drop"; month-end commentary | Medium (partner programs need earned relationships) | Real reach; weak price anchor |
| Amazon/marketplace sellers ($1M+) | Seller Central + QBO/Xero | Owner + bookkeeper | Heavy incumbent tooling (not surveyed) | Fee changes, returns | High | "Check next" |
| Small manufacturers | ERP + Excel costing (96% Excel for cost estimating, vendor n=180) | Controller/owner | Long cycles, ERP-partner-mediated | Material cost, tariffs | Low-medium | Data messiest; not first |
| Logistics / 3PL | WMS/TMS + QBO | Owner/finance lead | Freight audit = 25–50% contingency | Rate changes, disputes | Medium | Mature audit competitors |
| B2B SaaS | Stripe, HubSpot, QBO/Xero | Founder → finance hire | Self-serve | Churn, failed payments | **Highest** | Most crowded; builds in-house |
| Professional services/agencies | QBO/Xero + PSA | Owner + bookkeeper | Accountant-led | Utilization drop | Medium-high | Different product (utilization, not product margin) |
| Retail (SMB), restaurants, healthcare, construction | Vertical POS/EHR/PM | Varies | Vertical incumbents | Shrink, denials, job-cost fade | Low | Skip for first ICP |

Counts: NAW says ~30,000 distributors; one aggregator says 277,932 — two orders of magnitude apart. Pull Census SUSB by NAICS 423/424/454/54 before sizing. Shopify "millions of merchants" (10-K); live-store estimates 2.8M–6.9M by tool; ~47K Plus stores. QuickBooks/NetSuite/Odoo counts: not found.

## 3. Three candidate ICPs

**ICP-1 — Shopify-first product brand with a wholesale channel (the inbound sensor).** Physical-product brands (food/beverage, health/beauty, home, apparel), ~$2–20M revenue, 5–40 employees [J], US/QBO first (Xero only after checking its terms). Stack Shopify + QBO + ads + 3PL. Maturity: founder + bookkeeper ± fractional CFO. Buyer: founder signs; accountant influences. Triggers: tariff/landed-cost change, supplier price increase, margin fall after wholesale launch, inventory loan. *For:* only segment where inbound surfaces exist and the product is mostly API-first. *Against:* price ceiling ~$49–750/mo; crowded; in-product AI; $349+ unjustified without a documented dollar win.

**ICP-2 — Specialty distributor/wholesaler $10–75M on a mid-market ERP (the interview-led track).** US first; NetSuite/Acumatica/Epicor/Odoo/QB Enterprise; price lists in Excel; controller or CFO signs; pricing/sales-ops and the ERP reseller influence. Triggers: tariff-driven supplier price lists; PE acquisition, covenants, ERP migration (unsourced). *For:* highest dollar pain per customer; fits $900+/mo. *Against:* weakest inbound evidence; pass-through contradiction; CSV/ERP export path required; multi-week cycles. **Interviews and referrals unavoidable.**

**ICP-3 — Fractional-CFO / accounting-advisory firms serving 10–50 product-company clients (the channel test).** Customer is the firm. Reach: 94% of US firms offer advisory (Wolters Kluwer, n=2,768, fielded Apr–May 2025, survey vendor); Intuit–Fathom ProAdvisor partnership proves resale model. *Against:* Fathom ≈ $450/mo for 25 companies (~$18/client); 9 in 10 of 261 bookkeeping firms want ≤4 tools; no evidence accountant recommendations drive *non-accounting* software choices.

**Chosen design:** run ICP-1 as the inbound sensor, ICP-3 as the channel test, ICP-2 as interview-led — pick the ICP from where real files are uploaded and who says yes, not from desk scores.

## 4. Contradictory evidence
1. Distributors say they already pass costs through (DSG Q4 2026: 45% all, 45% most; Baird-NAW 2Q26: 91% raise prices). The MDM headline "Your Costs Changed in 3 Places During 2Q26. Your Pricing Changed Once." suggests the belief may not match the data — but the article body was not readable. **The single most important unresolved fact for ICP-2.**
2. Intuit is moving up-market (Enterprise Suite, Intuit Intelligence Chat; Feb 2026 Intuit–Anthropic partnership) and routes via accountants.
3. 45% of small businesses employ no accountant or bookkeeper (Clutch, n=302, vendor) — below ~$2–3M revenue, "who reads the case file?" is unanswered.
4. Small firms invest less in pricing tools (27% vs 55% at $500M+).

## 5. Buyer and budget analysis

| Role | Signs? | Influences? | Evidence (reliability) |
|---|---|---|---|
| Owner/CEO | Yes below ~$20M | Yes | SMB Group (n=751): CFO 28%, owner/president 27% of roles in financial-software decisions; Belkins 2026: CEO in 33.8% of SMB buying processes (marketing studies) |
| CFO/VP Finance | Yes where present | Yes | same |
| Controller | Rarely | Strong (operates tool) | inference |
| Fractional CFO / accountant | Seldom signs | **Very strong in sub-$20M firms**; 57% found their accountant by peer referral (TaxDome, about accountants not software) | Unproven for non-accounting software |
| Ops / pricing / sales-ops | No | Strong for margin tools | judgment |
| ERP reseller / consultant | No | Strong at mid-market ERP sites | directory pages |

Budget (all [J], only Techaisle is a sourced anchor: <1/3 of small businesses have deployed analytics; ~80% ad hoc/descriptive): sub-$5M no analytics budget line; $5–30M finance/ops head approves a few hundred dollars/month, security implications escalate to owner; $30–75M CFO/controller budget, reseller influence, security questionnaire. **No survey data exists on the dollar threshold SMBs approve without procurement.** $349+/month is *probably* owner-approvable; the $1.5–3.5K setup fee is the likeliest trigger for "let me ask my accountant." Testable.

## 6. Purchase triggers
Sourced: tariff and supplier cost shocks (NAW, Baird-NAW, DSG). Plausible but **unsourced**: PE acquisition, lender covenants, ERP migration, post-wholesale-launch margin drop, inventory financing, year-end close. A trigger that fades (tariffs; one trade-press title refers to a Supreme Court ruling against tariffs — unverified) weakens urgency, so the test should ask prospects what changed in the last 90 days.

## 7. Platform terms that gate the first stack
- **Xero:** developer terms reportedly prohibit using API data to train AI/ML (single summary — read the primary terms); revenue-share retired; connection-tier fees from 2026-03-02.
- **Intuit:** production keys require an app assessment; security review mandatory even for private apps; partner tiers Builder free / Silver $300 / Gold $1,700 / Platinum $4,500 per month (reported).
- **Shopify:** order history limited to 60 days without `read_all_orders` approval; public-app review took 2 weeks to 4+ months in forum reports; 0% revenue share on the first $1M lifetime, 15% after, one-time $19 fee.
Implication: for the 30-day test, **use exports and invited read-only users, not marketplace apps**; choose QBO first unless the Xero clause is confirmed harmless.

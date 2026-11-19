# 10 — Source Register (Phase 3)

**Total register entries from these four agents: 159 (126 table rows + 33 listed URLs).**

**Scope.** This register reproduces the source registers written by the four Phase 3 research agents that gathered external evidence (the skeptic review used only Phase 2 files and its own scripts). Phase 1 and Phase 2 registers remain in `research/appendix/` and `research/phase2/10_source_register.md` (218 rows). Each row: ID, URL, date, source type, claim supported, how verified (full page vs search snippet), as the agent recorded it.

**Verification caveat (applies to every row).** Only www.anthropic.com, claude.com and github.com returned page content to WebFetch. Everything else was a **search-result summary** (a model-written paraphrase of a page), so quoted figures may be right while context (sample, base, period) is missing. Reddit could not be read. Treat every row marked snippet/S-sum as *seen, not read*. No interviews were conducted.

**How the claims are used.** `01_phase2_evidence_audit.md` and `02_competitive_claims_verification.md` cite these IDs; `03`–`08` cite them for reachability, pricing and platform facts.


## P3A1 — Competitive claims verification (primary pages where reachable) (`appendix/p3_a1_competitive_verification.md`; 52 rows)

| ID | URL | Date seen | Type | Claim supported | How verified |
|---|---|---|---|---|---|
| P3A1-01 | https://www.anthropic.com/news/claude-for-small-business | 2026-11-19 | Vendor (primary) | Workflows named; margin analyzer name only; QuickBooks/PayPal cash workflow; approval wording; Cowork install | full page |
| P3A1-02 | https://claude.com/solutions/small-business | 2026-11-19 | Vendor (primary) | Shopify/Stripe/QuickBooks close; scheduling; no margin terms; Pro/Team | full page |
| P3A1-03 | https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business | 2026-11-19 | Open-source repo (primary) | 44 skills; no margin-analyzer skill listed | full page |
| P3A1-04 | https://github.com/anthropics/knowledge-work-plugins/blob/main/small-business/.mcp.json | 2026-11-19 | Repo (primary) | 35 connectors incl. QuickBooks, Xero, Shopify | full page |
| P3A1-05 | https://github.com/anthropics/knowledge-work-plugins/blob/main/small-business/README.md | 2026-11-19 | Repo (primary) | Approval rules; CSV fallback; no margin skill | full page |
| P3A1-06 | .../small-business/skills/report-builder/SKILL.md | 2026-11-19 | Repo (primary) | Ledger + Shopify pull; margin needs spec | full page |
| P3A1-07 | .../skills/close-month/SKILL.md | 2026-11-19 | Repo (primary) | Reconcile; hard sign-off gate; margin vs prior month | full page |
| P3A1-08 | .../skills/cash-flow-snapshot/SKILL.md | 2026-11-19 | Repo (primary) | Forward forecast; no historical attribution | full page |
| P3A1-09 | .../skills/invoice-chase/SKILL.md | 2026-11-19 | Repo (primary) | AR reminders; approval; no DSO analysis | full page |
| P3A1-10 | .../skills/business-pulse/SKILL.md | 2026-11-19 | Repo (primary) | Pulse; schedule presets; no margin calc | full page |
| P3A1-11 | .../skills/inventory-planner/SKILL.md | 2026-11-19 | Repo (primary) | Shopify reorder; no margin | full page |
| P3A1-12 | https://claude.com/marketplace/connectors/quickbooks | 2026-11-19 | Vendor (primary) | QuickBooks connector tools; confirmation before sending | full page |
| P3A1-13 | https://claude.com/marketplace/connectors/shopify | 2026-11-19 | Vendor (primary) | Shopify connector tools; no ShopifyQL/cost mention | full page |
| P3A1-14 | https://claude.com/marketplace/connectors/xero | 2026-11-19 | Vendor (primary) | Xero connector read-only, 20 tools | full page |
| P3A1-15 | https://quickbooks.intuit.com/learn-support/en-us/help-article/business-reports/ai-powered-report-insights/L2jZq6tfM_US_en_US | 2026-11-19 | Vendor help | AI report insights, root cause, 15 months | snippet |
| P3A1-16 | https://quickbooks.intuit.com/learn-support/en-us/help-article/intuit-ai/understand-business-trends-anomalies-intuit-intelligence/L6RpHl0M4_US_en_US | 2026-11-19 | Vendor help | Chat names drivers (customers, vendors, products) | snippet |
| P3A1-17 | https://quickbooks.intuit.com/r/news/intuit-advances-mid-market-platform/ | 2026-11-19 | Vendor newsroom | Chat beta, 25 prompts per month | snippet |
| P3A1-18 | https://quickbooks.intuit.com/learn-support/en-us/help-article/tasks/forecast-financial-performance-intuit-intelligence/L7o5sk5t2_US_en_US | 2026-11-19 | Vendor help | Forecast needs 2 years' history | snippet |
| P3A1-19 | https://quickbooks.intuit.com/payments-agent/ | 2026-11-19 | Vendor marketing | Payments agent; 5-days-faster claim | snippet |
| P3A1-20 | https://investors.intuit.com/news-events/press-releases/detail/1305/intuit-and-anthropic-partner-to-bring-trusted-financial-intelligence-and-custom-ai-agents-to-consumers-and-businesses | 2026-11-19 | Press release | Intuit-Anthropic partnership | snippet |
| P3A1-21 | https://quickbooks.intuit.com/learn-support/en-us/help-article/accounting-bookkeeping/use-quickbooks-connector-claude/L3YBlo6Ht_US_en_US | 2026-11-19 | Vendor help | Connector US-only | snippet |
| P3A1-22 | https://www.xero.com/us/media-releases/xeros-ai-financial-superagent-jax-launches-powerful-new-features/ | 2026-11-19 | Press release | JAX launch 2025-09-03; AU first | snippet |
| P3A1-23 | https://www.xero.com/us/accounting-software/analytics/ | 2026-11-19 | Vendor marketing | Analytics gross margin, DSO | snippet |
| P3A1-24 | https://www.xero.com/us/accounting-software/analytics/cash-flow/ | 2026-11-19 | Vendor marketing | Forecasts incl. invoice and bill payment predictions | snippet |
| P3A1-25 | https://www.xero.com/us/media-releases/xero-and-anthropic-collaborate/ | 2026-11-19 | Press release | Xero-Anthropic partnership; read-only Claude connector | snippet |
| P3A1-26 | https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports | 2026-11-19 | Vendor help | Native profit reports; cost needed; net-sales margin | snippet |
| P3A1-27 | https://changelog.shopify.com/posts/product-cost-and-profit-reporting-is-here | 2026-11-19 | Vendor changelog | Profit reports "Shopify Plan or higher" (old) | snippet |
| P3A1-28 | https://changelog.shopify.com/posts/turn-business-questions-into-analytics-reports-with-natural-language-queries | 2026-11-19 | Vendor changelog | Sidekick to ShopifyQL | snippet |
| P3A1-29 | https://help.shopify.com/en/manual/ai-powered-tools/sidekick/pulse | 2026-11-19 | Vendor help | Pulse eligibility, up to 5 suggestions | snippet |
| P3A1-30 | https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/shopify-connector-for-claude | 2026-11-19 | Vendor help | Shopify connector for Claude, analytics read-only | snippet |
| P3A1-31 | https://help.shopify.com/en/manual/products/inventory/transitioning-from-stocky | 2026-11-19 | Vendor help | Stocky ended 2026-08-31; 90-day read-only | snippet |
| P3A1-32 | https://www.netsuite.com/artificial-intelligence.shtml | 2026-11-19 | Vendor marketing | Ask Oracle "how and why" | snippet |
| P3A1-33 | https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_8144753226.html | 2026-11-19 | Vendor docs | AI Units, 10-50 units example | snippet |
| P3A1-34 | https://www.netsuite.com/portal/collateral/public/ds-ns-data-intelligence.pdf | 2026-11-19 | Vendor datasheet | Data Intelligence | snippet |
| P3A1-35 | https://www.fathomhq.com/pricing | 2026-11-19 | Vendor pricing | $450 / 25 companies; AI commentary | snippet |
| P3A1-36 | https://www.float.com/pricing | 2026-11-19 | Vendor pricing | Float is capacity planning; $7/$12 per person | snippet |
| P3A1-37 | https://chaser.io/ | 2026-11-19 | Vendor marketing | AI debtor insights; 60% DSO claim | snippet |
| P3A1-38 | https://upflow.io/pricing ; https://upflow.io/features/analytics | 2026-11-19 | Vendor | Pricing tiers; DSO root cause via Ask Upflow | snippet |
| P3A1-39 | https://cashflowfrog.com/pricing/ | 2026-11-19 | Vendor | Tiers $69-$249; drill-down | snippet |
| P3A1-40 | https://www.jirav.com/pricing | 2026-11-19 | Vendor | Wholesale pricing for firms | snippet |
| P3A1-41 | https://apps.shopify.com/trueprofit | 2026-11-19 | App listing | TrueProfit tiers | snippet |
| P3A1-42 | https://useamp.com/pricing/ | 2026-11-19 | Vendor | Lifetimely Profit Agent; pricing conflicts | snippet |
| P3A1-43 | https://www.polaranalytics.com/ | 2026-11-19 | Vendor marketing | "Why did contribution margin fall"; Data Debug Sheet | snippet |
| P3A1-44 | https://www.triplewhale.com/pricing ; kb.triplewhale.com | 2026-11-19 | Vendor | Net profit definition; gross margin not default | snippet |
| P3A1-45 | https://www.conjura.com/ ; https://wayflyer.com/press-releases/wayflyer-acquires-conjura-to-accelerate-its-ai-product-offering-for-small-businesses | 2026-11-19 | Vendor / press | Contribution profit; Owly AI; acquisition 2026-06-19 | snippet |
| P3A1-46 | https://apps.shopify.com/beprofit-profit-tracker | 2026-11-19 | App listing | BeProfit features, credits | snippet |
| P3A1-47 | https://apps.shopify.com/profit-pulse-ai | 2026-11-19 | App listing | $19/month exception queue; 0 reviews | snippet |
| P3A1-48 | https://apps.shopify.com/profitgpt | 2026-11-19 | App listing | Hypersonix Profit Max AI daily lists | snippet |
| P3A1-49 | https://apps.shopify.com/marjn | 2026-11-19 | App listing | Low-margin alerts, $19 tier | snippet |
| P3A1-50 | https://www.vendavo.com/our-products/margin-bridge-analyzer/ | 2026-11-19 | Vendor marketing | PVM + rebate bridge, period-over-period | snippet |
| P3A1-51 | https://www.a2xaccounting.com/integrations/shopify/quickbooks | 2026-11-19 | Vendor | Shopify payout to QuickBooks; SKU COGS | snippet |
| P3A1-52 | skills.sh/anthropics/knowledge-work-plugins/margin-analyzer (host blocked); easytool-me.pages.dev; spicyadvisory.pages.dev | 2026-11-19 | Third-party | Description of margin analyzer (PayPal + QuickBooks; GM table) | search-result title/summary only; UNVERIFIED |


## P3A2 — Reachability, trust and pricing (`appendix/p3_a2_reachability_trust_pricing.md`; 30 rows)

All rows: verified by WebSearch result summary only (snippet) unless stated; I did not read any external full page. Dates are the dates the snippets or titles show, else "undated".

| ID | URL | date | type | claim supported | how verified |
|---|---|---|---|---|---|
| P3A2-01 | https://belkins.io/blog/cold-email-response-rates | 2026 study (2025 data) | VENDOR | 0.45% average reply on 7.5M emails; founders/owners 0.57%, C-level 0.42%, VP 0.32% | snippet; fetch blocked (ENOTFOUND) |
| P3A2-02 | https://belkins.io/blog/linkedin-outreach-study.md | 2026 | VENDOR | LinkedIn founders/owners 6.4%; finance/marketing hardest, below 6% | snippet |
| P3A2-03 | https://thedigitalbloom.com/learn/cold-outbound-reply-rate-benchmarks/ ; https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach | 2025-2026 | VENDOR | 3-6% "healthy" cold reply rates; ~3.2% median; denominators differ | snippet (aggregated summary) |
| P3A2-04 | https://leadhaste.com/blog/cold-email-template-for-accounting ; https://moderninbound.com/blog/cold-email-for-accounting-firms | undated | VENDOR | 2-4% reply, 1-1.5% meeting on accounting partner lists; 22% single-case top angle; timing advice | snippet |
| P3A2-05 | https://www.indiehackers.com/post/i-sent-43-cold-emails-with-my-own-tool-17-replied-1-paid-here-s-the-unofficial-launch-329774e623 | undated | COMMUNITY-ANECDOTE | 43 emails, 17 replies, 1 paid at $230/mo | snippet |
| P3A2-06 | https://www.indiehackers.com/post/the-exact-cold-email-script-that-gets-agencies-to-reply-and-the-3-versions-that-got-ignored-18b57cef84 | undated | COMMUNITY-ANECDOTE | 150+ personalized agency emails, most ignored | snippet |
| P3A2-07 | https://www.demandsage.com/shopify-statistics/ ; https://explodingtopics.com/blog/shopify-stats ; https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm | 2025-2026 | ANALYST/PRIMARY | conflicting BuiltWith-derived counts (200+, 1,148, 2,860+) of $1M+ merchants; no official revenue-band count seen | snippet; 10-K excerpt not read in full |
| P3A2-08 | https://www.richpanel.com/learn/shopify-plus-cx-software-install-base-2026 ; https://www.launchtip.com/blog/shopify-plus-adoption-stats-2026-upgrading-and-why | 2026 | VENDOR | StoreLeads Plus counts 74,777 (May 2026) and 77,514 (Sept 2026); only Plus reliably detectable | snippet |
| P3A2-09 | https://storeleads.app/reports/shopify/app/wholesale ; https://syncgtm.com/blog/store-leads-review-2026 | 2026 | VENDOR | 146 stores with one wholesale app; revenue-estimate filter claimed but unconfirmed | snippet |
| P3A2-10 | https://www.faire.com/blog/trends/faire-market-by-the-numbers-july-2025 ; https://www.faire.com/news/2025-11-17-a-milestone-for-faire | 2025-2026 | VENDOR | 30K-32K brands receiving orders per market; 100K+ brands total | snippet |
| P3A2-11 | https://www.cpapracticeadvisor.com/2017/01/04/celebrating-20-years-200000-global-members/25643 ; https://intuit.com/company/press-room/press-releases/2017/intuit-helps-small-businesses-find-their-perfect-match-with-new-quickbooks-accounting-professionals-marketplace | 2008-2017 | TRADE/PRIMARY | ProAdvisor program size (100K in 2014; "200,000" headline 2017); free certified listing in Find-a-ProAdvisor; no current count | snippet |
| P3A2-12 | https://a2xaccounting.com/ecommerce-accountant-directory ; https://taxomate.com/accountant-directory | undated | VENDOR | ecommerce accountant directories with partner tiers; no totals | snippet |
| P3A2-13 | https://help.shopify.com/en/manual/partner-directory ; https://stackinfluence.com/blog/guide-to-the-shopify-partner-directory | undated | PRIMARY/third-party | no accounting category in Shopify Partner Directory; conflicting expert counts | snippet |
| P3A2-14 | https://community.shopify.com/guidelines ; https://community.shopify.com/t/code-of-conduct/366910/1 | current; code ~2 years old | PRIMARY | promotion barred outside Ask and Offer; promotional PMs barred; own-service disclosure guidance | snippet |
| P3A2-15 | https://thehiveindex.com/communities/r-shopify/ ; https://www.letstalkshop.com/blog/reddit-communities-for-shopify-store-owners-guide | undated | COMMUNITY/third-party | r/shopify bans self-promotion/PM service offers (conflicting on review posts) | snippet; official rules not retrieved |
| P3A2-16 | https://reddit.birdcat.cafe/r/ecommerce/comments/1j3crv8/welcome_to_recommerce_please_read_before_posting | 2025-03-04 | COMMUNITY mirror | r/ecommerce account age/karma and no-solicitation rule | snippet of a mirror |
| P3A2-17 | https://www.xero.com/data/for-small-businesses/2021-survey/ | 2021 | VENDOR | SMBs unsure how providers use data; 39% understood third-party access | snippet |
| P3A2-18 | https://www.pymnts.com/?p=759113 ; https://www.codat.io/blog/what-makes-smbs-willing-to-share-data-with-financial-providers/ ; https://newsroom.paypal-corp.com/2023-06-13-Entrepreneurs-Willingness-to-Share-Data-Offers-a-Path-to-Narrowing-Credit-Gaps | 2020-2023 | TRADE/VENDOR | 15% of UK small firms share bank data electronically; 67% of potential borrowers would share with lenders; 58% in a US survey | snippet |
| P3A2-19 | https://quickbooks.intuit.com/learn-support/en-au/manage-your-account/can-i-give-my-external-accountant-read-only-access-3f/00/1482928 ; https://www.webgility.com/blog/how-to-add-accountant-to-quickbooks-online ; https://quickbooks.intuit.com/learn-support/en-us/manage-your-account/invite-or-remove-an-accountant/00/263125 | undated | COMMUNITY/VENDOR/PRIMARY | read-only accountant access reportedly unavailable in QBO vs vendor blog saying it is; admin needed to invite | snippet; conflicting |
| P3A2-20 | https://warrenaverett.com/insights/soc-2-catch-22/ ; https://www.brightdefense.com/resources/soc-2-for-startups ; https://secureframe.com/customers/my-askai.md | undated | VENDOR | SOC 2 mainly demanded by larger buyers; Type I $5-20K, Type II $15-50K | snippet |
| P3A2-21 | https://eightx.co/blog/ecommerce-profitability-audit-framework ; https://eightx.co/services ; https://eightx.co/blog/fractional-cfo-for-ecommerce-brands | 2026 | VENDOR | audit scope; audit from $5,000; retainers $3K-$15K/mo; productized tiers $995-$3,500/mo; pages conflict | snippet; fetch blocked |
| P3A2-22 | https://www.upwork.com/services/product/consulting-hr-a-1-page-cfo-assessment-of-your-books-margins-and-reporting-gaps-2058915694245648455 ; https://acuity.co/cfo/ | undated | VENDOR | fixed-fee 1-page CFO assessment; $250/hr; health check without published price | snippet |
| P3A2-23 | https://www.webgility.com/pricing?unifyPlan=desktop ; https://salaccounting.ca/pricing-for-ecommerce-bookkeeping/ ; https://www.meruaccounting.com/cost-of-hiring-an-ecommerce-accountant/ | undated | VENDOR | cleanup from $249; Canadian catch-up $3,000-$9,000 CAD; setup/cleanup $500-$5,000+ | snippet |
| P3A2-24 | https://ecombalance.com/pricing-new/ ; https://client.ecombalance.com/estimate | undated | VENDOR | one-time cleanup fee plus monthly; monthly from $250 per a comparison page | snippet; fetch blocked |
| P3A2-25 | https://www.blackbeltcommerce.com/shopify-conversion-audit/ ; https://www.firstpier.com/service/ecommerce-audit-strategy ; https://website-1hy.pages.dev/growth-audit ; https://fillthelobby.pages.dev/audit | 2026 | VENDOR | agency one-time audits $997 (title only; detail unconfirmed), $1,950 (10 days), $1,500 (7 days); free audits as lead magnets | snippet; fetch blocked |
| P3A2-26 | https://www.lateshipment.com/platform/oneaudit/ ; https://www.shipscience.com/parcel-audit-guide/ ; https://refundretriever.com/?p=30 ; https://dash.fi/shipping/audit | undated | VENDOR | parcel audit contingency 25-50%, 35% typical, Dash 0% success fee | snippet |
| P3A2-27 | https://eva.guru/answers/how-to-outsource-amazon-fba-reimbursements/ ; https://revenuegeeks.com/?p=28080 ; https://www.amplisell.com/blog-post/best-amazon-reimbursement-services-for-fba-brands | 2025-2026 | VENDOR | FBA reimbursement fees 10-30%, no recovery no fee | snippet |
| P3A2-28 | https://sakasandcompany.com/paid-discovery/ ; https://www.consultingsuccess.com/productization-playbook ; https://www.agencymavericks.com/?p=54882 | undated | VENDOR | paid discovery framing, audits $500-$3,000 (citing Productize), credit-toward-program and keep-output terms | snippet |
| P3A2-29 | https://insites.com/blog/why-your-free-audits-arent-turning-into-paid-work/ ; https://seomator.com/blog/expert-roundup-free-vs-paid-seo-audits-1311.html | undated | VENDOR | free audits give volume, paid audits filter intent; no controlled close-rate comparison | snippet |
| P3A2-30 | /home/user/Metrial-AI-Model/research/phase2/07_30_day_validation_plan.md ; 03_icp_and_buyer_analysis.md ; 06_pricing_and_unit_economics.md ; appendix/p2_a4_icp_buyer_inbound.md | 2026 | internal | plan, thresholds (all judgment), price anchors, 10-28h onboarding, A4-38 lead-tool benchmarks | full read (first three); keyword read (appendix) |


## P3A3 — Evidence audit of Phase 2 claims (`appendix/p3_a3_evidence_audit.md`; 44 rows)

All "how verified" entries are **WebSearch result summary (snippet only)**, because the cited host was blocked for WebFetch. Dates are those visible in the results.

| ID | URL | Date | Type | Claim(s) tested | How verified |
|---|---|---|---|---|---|
| P3A3-01 | https://www.mhlnews.com/transportation-distribution/news/55287944/tariffs-driving-cost-for-wholesale-distribution-industry ; https://www.mdm.com/news/research/economic-trends/new-naw-mdm-research-shows-tariffs-growing-impact-on-supply-chain/ | 2025 | Trade press on NAW/MDM survey | 62% COGS +10% (A01) | Snippet; fetch blocked |
| P3A3-02 | https://www.naw.org/new-naw-research-shows-tariffs-growing-impact-on-supply-chain/ ; https://www.supplychain247.com/article/tariffs-increase-distributors-naw-mdm-survey/freight_rates | 2025-05 | Trade association | One-third 25%+ (A02) | Snippet; fetch blocked |
| P3A3-03 | https://www.mdm.com/article/featured/featured-main/research-your-costs-changed-in-3-places-during-2q26-your-pricing-changed-once/ ; https://www.naw.org/product/naw-2q26-marketpulse-report/ | 2026-Q2 | Trade press / paywalled report | 91%, 33% absorb (A03, A04) | Snippet; fetch blocked |
| P3A3-04 | https://distributionstrategy.com/2026/10/distributors-see-steady-q4-demand-as-ecommerce-competition-intensifies/ | 2026-10 | Trade research firm | 45%/45% (A05) | Snippet; fetch blocked |
| P3A3-05 | https://distributionstrategy.com/2026/06/the-mid-cap-distributors-pricing-quandary/ | 2026-06 | Analyst article | 100-300 bps, $100M-$1B (A06) | Snippet; fetch blocked |
| P3A3-06 | https://distributionstrategy.com/report/closing-the-execution-gap/ ; https://www.cavallo.com/blog/how-to-close-the-execution-gap-thats-costing-distributors-millions/ | 2026-03-10 | Consultancy report (gated) | 3-5%, 150-200 bps, $750K-$1M (A07) | Snippet; fetch blocked |
| P3A3-07 | https://www.vendavo.com/pricing/pricing-strategy-holding-you-back/ ; https://www.copperberg.com/?p=16774 | 2025 | Vendor + consultancy survey | 85% spreadsheets; 13% AI; 14% not found (A08, A09, A11) | Snippet; fetch blocked |
| P3A3-08 | https://www.mdm.com/article/technology/ai/the-hidden-majority-your-ai-is-writing-emails-your-competitors-ai-is-finding-margin/ | 2026-05 | Industry media column | 27% rank pricing AI #1; 74% roadmap (A10) | Snippet; fetch not attempted separately (same host blocked) |
| P3A3-09 | https://www.simon-kucher.com/en/insights/2026-wholesale-and-distribution-industry-report | 2026 | Consultancy report | 55% vs 27% (A12): not found | Snippet only |
| P3A3-10 | https://shopify.dev/changelog/apps-now-need-shopify-approval-to-read-orders-older-than-60-days | 2018 | Vendor changelog | 60-day default (A14) | Snippet; fetch blocked |
| P3A3-11 | https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem ; https://community.shopify.dev/t/assymetry-of-cost-and-unitcost-on-inventoryitem/13399 ; https://community.shopify.com/t/cost-on-orders-api/1610/1 | 2021-2026 | Vendor docs + forum | unitCost optional/current (A15) | Snippet; no official current-only statement |
| P3A3-12 | https://shopify.dev/changelog/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026.md ; https://changelog.shopify.com/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026 | 2025-10-30 | Vendor changelog | Legacy apps (A17) | Snippet |
| P3A3-13 | https://shopify.dev/docs/apps/launch/distribution/revenue-share | 2025-26 | Vendor docs | 0%/15%/$19; 2.9% fee (A19) | Snippet |
| P3A3-14 | https://community.shopify.dev/t/longer-app-store-review-times-what-you-need-to-know/31728 | 2026 | Forum (staff post) | Review times (A18) | Snippet |
| P3A3-15 | https://shopify.dev/docs/apps/launch/protected-customer-data | 2025-26 | Vendor docs | Protected data (A16) | Snippet |
| P3A3-16 | https://uxify.com/blog/ai-agents-shopify-apps ; https://craftberry-silk.vercel.app/articles/shopify-app-store-statistics | 2026-04 | Aggregator blogs | 17,591 apps (A20) | Snippet |
| P3A3-17 | https://developer.xero.com/pricing ; https://www.accountingtoday.com/news/xero-shifts-to-tiered-pricing-model-for-developers ; https://truto.one/blog/xero-api-pricing-changes-2026-costs-tiers-and-how-to-minimize-egress/ | 2025-12 to 2026-03 | Vendor page + trade press | Tiers (A21) | Snippet |
| P3A3-18 | https://developer.xero.com/faq/pricing-and-policy-updates ; https://www.theregister.com/2025/12/04/xero_api_fees_change/ ; https://accounts-os.com/blog/xero-api-ban-ai-accounting-future | 2025-12 | Vendor FAQ + press | AI/ML training ban (A22) | Snippet |
| P3A3-19 | https://cfotech.com.au/story/xero-to-retire-app-store-billing-shift-to-api-tiers ; https://www.accountantsdaily.com.au/technology/21986-all-you-can-eat-xero-data-buffet-comes-to-abrupt-end | 2025-12/2026-02 | Trade press | Revenue share retired (A23) | Snippet |
| P3A3-20 | https://www.fool.com.au/2026/05/14/why-xero-shares-are-falling-despite-a-big-jump-in-revenue/ ; https://kalkine.com.au/news/technology/xero-asx-xro-fy26-revenue-up-31-melio-fuels-us-push | 2026-05-14 | Financial press | 4.92M vs 4.9M (A24) | Snippet |
| P3A3-21 | https://developers.intuit.com/app/developer/qbo/docs/get-started/partner-faq ; https://investors.intuit.com/_assets/_08ee5483ec4c057568cc8774f3fd6aad/intuit/news/2025-07-28_Intuit_Launches_New_App_Partner_Program_to_Drive_1261.pdf ; https://www.apideck.com/blog/quickbooks-api-pricing-and-the-intuit-app-partner-program | 2025-07-28 | Vendor FAQ/release + integrator | Tiers (A25) | Snippet |
| P3A3-22 | https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/platform-requirements ; https://developers.apideck.com/connectors/quickbooks/docs/application_owner+app_compliance ; https://docs.codat.io/integrations/accounting/quickbooksonline/qbo-app-assessment-questionnaire | 2025-26 | Vendor + integrator docs | Production keys (A26) | Snippet |
| P3A3-23 | https://blog.insightfulaccountant.com/new-and-enhanced-ai-agents-across-the-intuit-platform ; https://fortune.com/article/intuit-intelligence/ ; https://cpapracticeadvisor.com/2026/11/06/overview-of-intuit-ai-in-quickbooks-online-2026/193399 | 2025-11 to 2026-11 | Trade press | Intuit Intelligence features/tiers (A27) | Snippet |
| P3A3-24 | https://quickbooks.intuit.com/r/news/intuit-advances-intelligence-platform/ ; https://www.constellationr.com/insights/news/intuit-expands-industry-roster-intuit-enterprise-suite-steps-midmarket-game ; https://www.cpapracticeadvisor.com/2026/08/27/intuit-introduces-new-capabilities-across-enterprise-suite-qbo-advanced/189236/ | 2026-02 to 2026-10 | Vendor blog + analyst | Industry editions (A28) | Snippet |
| P3A3-25 | https://www.wolterskluwer.com/en/know/future-ready-accountant ; https://www.cpapracticeadvisor.com/2025/10/09/accounting-firms-are-choosing-transformation-over-tactics-wolters-kluwer-report-says/170677/ | 2025-10 | Vendor survey | 94%, n=2,768 (A34) | Snippet; fetch blocked |
| P3A3-26 | https://fathomhq.com/pricing | 2026 | Vendor pricing | $450/25, $17 extra (A35) | Snippet |
| P3A3-27 | https://chaserhq.com/pricing ; https://www.capterra.com/p/157101/CHASER/pricing/ | 2026 | Vendor + review site | $259 (A36) | Snippet |
| P3A3-28 | https://apps.shopify.com/profit-pulse-ai | 2026 | App listing | $19/mo (A37) | Snippet |
| P3A3-29 | https://techaisle.com/blog/253-analytics-and-big-data-in-the-us-smb-market | undated | Analyst blog | Under one-third (A38) | Snippet; no date visible |
| P3A3-30 | https://www.cfodive.com/news/ai-verification-eats-26percent-finance-teams-workweek-datarails/832210/ ; https://cpapracticeadvisor.com/2026/10/07/fact-checking-ai-is-taking-up-more-of-cfos-and-finance-teams-time/191230 | 2026-10-06/07 | Vendor survey via press | 96% (A39) | Snippet; fetch blocked |
| P3A3-31 | https://www.journalofaccountancy.com/news/2026/feb/agentic-ai-is-handling-more-finance-work-but-can-cfos-trust-it/ ; https://www.cfodive.com/news/massive-trust-gap-hinders-cfo-ai-ambitions-study-finds/810786/ | 2026-02 | Trade press | 14% (A40) | Snippet; fetch blocked |
| P3A3-32 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | 2025-06-25 | Analyst press release | 40% (A41) | Snippet; fetch blocked |
| P3A3-33 | https://www.arxiv.org/pdf/2411.07763 ; https://spider2-sql.github.io/ ; https://www.themoonlight.io/review/spider-20-evaluating-language-models-on-real-world-enterprise-text-to-sql-workflows | 2024-25 | Paper + summaries | 21.3% / 17% / 5.7% (A42) | Snippet; fetch blocked |
| P3A3-34 | https://vals.ai/benchmarks/finance_agent ; https://www.benchlm.ai/benchmarks/financeAgentV2 | 2026-06 | Benchmark vendor | 64.4% (A43) | Snippet; fetch blocked |
| P3A3-35 | https://developer-docs.amazon.com/sp-api/docs/report-type-values-settlement ; https://developer-docs.amazon.com/sp-api/lang-it_IT/changelog/update-removal-of-xml-settlement-report-and-flat-file-settlement-report-date-changed-to-november-11-2026 | 2026 | Vendor docs/changelog | 90 days; 2026-11-11 (A30) | Snippet |
| P3A3-36 | https://www.odoo.com/documentation/latest/developer/reference/external_api.html | current | Vendor docs | Plan gating (A29) | Snippet |
| P3A3-37 | https://www.merge.dev/pricing ; https://help.merge.dev/en/articles/6641605-self-serve-with-merge-launch-plans-faq | 2025-05-28 and 2026 | Vendor pricing/FAQ | $650/$65 (A31) | Snippet |
| P3A3-38 | https://unified.to/blog/unified_apis_usage_based_vs_per_connection_pricing_for_integrations ; https://radar.apideck.com/blog/best-unified-api-platforms-for-developers-and-saas-teams | 2026 | Competitor blogs | Apideck, Unified.to, Rutter, Codat (A32, A33) | Snippet |
| P3A3-39 | https://fortune.com/2026/05/01/rebel-cheese-mark-cuban-ai-shipping/ ; https://finance.yahoo.com/sectors/technology/articles/mark-cuban-backed-vegan-cheese-172818866.html ; https://www.fastcompany.com/91537200/texas-rebel-cheese-ai-shipping | 2026-05-01 | Business press + aggregators | $400K; $250K; <$40K (A44) | Snippet; "<$40K" only in aggregators |
| P3A3-40 | https://wayflyer.com/press-releases/wayflyer-acquires-conjura-to-accelerate-its-ai-product-offering-for-small-businesses ; https://www.businesswire.com/news/home/20260619044302/en/ | 2026-06-19 | Press release | Conjura (A45) | Snippet |
| P3A3-41 | https://craftybase.com/blog/shopify-stocky-discontinued ; https://community.shopify.com/t/stocky-app-going-away-after-august-31-2026/587292 ; https://www.sku.io/stocky-alternative/ | 2026 | Vendor + forum | Stocky (A46) | Snippet; fetch blocked |
| P3A3-42 | https://techcrunch.com/2025/03/13/uipath-is-looking-for-a-path-to-growth-in-agentic-ai-with-its-peak-ai-acquisition ; https://yespress.io/peak ; https://www.cbinsights.com/company/peakai/financials | 2025-03 | Press + trackers | Peak price/funding (A48) | Snippet |
| P3A3-43 | https://www.sisudata.com ; https://yespress.io/sisu-data ; https://www.cbinsights.com/company/sisu-data/ | 2023-10 | Company site + trackers | Sisu discontinued (A48) | Snippet |
| P3A3-44 | https://www.netsuite.alphabold.com/netsuite-ai-gross-margin-analysis/ ; https://www.withum.com/resources/netsuite-ai-features-netsuite-next-readiness/ ; https://www.crowe.com/insights/netsuite-blog/netsuite-next-is-here-are-businesses-ready | 2026 | Partner marketing | Ask Oracle (A47) | Snippet; no Oracle doc found |

---

## 8. Limits of this audit

- No full page was read. Every status is bounded by the quality of a search summary, which can drop caveats (sample, base, period) or, rarely, mis-state them. I tried to flag where a summary itself said it could not confirm a figure.
- WebSearch results are US-only and ranked by an unknown algorithm; absence of a figure (A09, A12, A32) means "not found in summaries", not "false".
- I audited 48 claims; about 170 register rows were not individually tested. The untested rows are mostly lower-impact (competitor features, reviews, forum anecdotes).
- No customer evidence was audited here (see p3_a4).
- Next step to convert statuses to VERIFIED-FULL-PAGE: allowlist mdm.com, naw.org, distributionstrategy.com, vendavo.com, shopify.dev, developer.xero.com, developer.intuit.com, fortune.com, wolterskluwer.com, and read A03/A05/A06/A07/A12/A15/A22/A44 first; those eight carry most of the decision weight.


## P3A4 — Independent customer-evidence search (`appendix/p3_a4_customer_evidence.md`; 33 URLs listed as a bullet list; the full 22-item evidence log with permalinks and quotes is in section 2 of that appendix file)

All sources below were seen only as **search-result entries or search-tool summaries**, never as fetched pages. Access date for all: 2026-11-19.

**Customer or community platforms**
- https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805
- https://community.shopify.com/t/profit-ad-spend-tracking-on-shopify-whats-actually-broken-for-you/646399
- https://community.shopify.com/t/how-can-i-accurately-calculate-the-net-profit-per-order/631719
- https://community.shopify.com/t/replace-my-spreadsheet-track-cost-revenue-and-margin-in-shopify/567219
- https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628
- https://community.shopify.com/t/how-do-you-pack-shopify-numbers-for-your-accountant-each-month/669948
- https://community.shopify.com/t/stuck-in-sheets-for-sales-reports-how-are-you-handling-this/673334
- https://community.shopify.com/t/true-profit-ask/401391 (seen in results; no content reported)
- https://news.ycombinator.com/item?id=46901206
- https://news.ycombinator.com/item?id=47180585
- https://news.ycombinator.com/item?id=48130950
- https://news.ycombinator.com/item?id=45110330
- https://news.ycombinator.com/item?id=7515318
- https://quickbooks.intuit.com/community/account-management-7/how-can-i-turn-off-ai-in-quickbooks-76453
- https://quickbooks.intuit.com/community/other-questions-9/how-do-i-permanently-opt-out-of-the-ai-assistant-idiocy-4698
- https://quickbooks.intuit.com/community/do-more-with-quickbooks-6/qbo-s-ai-implementation-284062
- https://quickbooks.intuit.com/community/account-management-65/why-does-this-whole-app-suck-now-162741
- https://quickbooks.intuit.com/learn-support/en-us/other-questions/ai-is-sending-out-payment-reminders-it-sounds-like-i-m/00/1555976
- https://community.xero.com/business/discussion/38473387
- https://www.capterra.com/p/157101/CHASER/reviews/?page=2
- https://www.g2.com/discussions/what-are-the-best-tools-for-tracking-overdue-payments
- https://unofficialquickbooksaccountantspodcast.transistor.fm/104/transcript

**Vendor, trade or consultancy (NOT customer voice)**
- https://quickbooks.intuit.com/learn-support/en-us/accounting/allowing-third-party-access-to-your-company-file/00/609618 (Intuit help)
- https://www.sage.com/en-us/blog/security-and-information-sharing-what-you-should-know-about-quickbooks/
- https://liveflow.io/post/security-and-integrating-third-party-apps-with-quickbooks-online
- https://enterprisedna.co/resources/insights/accounting-third-party-ai-connectors-expand-risk
- https://eightx.co/blog/fractional-cfo-for-ecommerce-brands (and related eightx.co pages)
- https://www.chaserhq.com/blog/ (several Chaser pages)
- https://distributionstrategy.com/report/the-state-of-distributor-profitability/
- https://www.mdm.com/article/research/economic-trends/distributors-pay-the-price-when-supply-chains-crack-whats-your-response/
- https://zilliant.com/blog/how-distributors-lose-margin-in-plain-sight-the-pricing-agreement-problem
- https://trueprofit.io/blog/why-keeping-track-of-cogs-is-painful-shopify-dropshipping-business (vendor blog)
- https://ecommercefastlane.com/shopify-reports-guide-real-profit/ (agency content)

Honesty note: titles quoted above are as indexed in result lists. All other quoted fragments are second-hand search-summary text, flagged "S-sum". None should be cited in an investment memo as a verbatim customer quote until verified against the source page.

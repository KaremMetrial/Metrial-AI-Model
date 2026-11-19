# P3-A1 — Independent competitive-claims verification (Margin Investigator)

**Date of verification:** 2026-11-19. **Method:** WebFetch on every primary host the session allowed; WebSearch with `allowed_domains` on vendor hosts that WebFetch could not resolve. Read-only; nothing was signed up for, bought, or contacted.

**Evidence grades used in every table**
- **full page** = the page was fetched and read through WebFetch. WebFetch itself runs a small summarising model over the page, so even "full page" is a machine summary of the page, not my own reading of raw HTML. Quotes marked "quote" came back verbatim in the tool output.
- **snippet** = I saw only a search-result summary of a vendor-hosted page. The vendor URL is real and was returned by the search, but I did not read the page.
- **third-party** = a non-vendor page. Never used as the sole basis for an EXISTS verdict.

**Status labels:** EXISTS (documented as available) · NEEDS-CONFIG (available once the user defines or supplies something) · NEEDS-SERVICES (vendor or partner services required) · MISSING-with-evidence (a documented limitation or an explicit "does not") · UNVERIFIED (not seen, or seen only in a form too thin to rely on). UNVERIFIED never means "absent".

---

## 0. Headline findings

1. **Phase 2's "no margin workflow found" for Claude for Small Business was wrong, but what exists is thinner than the launch copy implies.** Anthropic's launch page names a "margin analyzer" and gives no detail (full page). The only descriptions of what it does come from third-party sites; I could not read a primary specification. See section 1.
2. **The Claude Small Business plugin ships connectors for QuickBooks, Xero, Shopify, PayPal, Stripe and 29 other tools**, and its documented skills pull Shopify orders and ledger data into the same run, with hard approval gates (full page, GitHub). Phase 2 listed only "QuickBooks, PayPal, HubSpot".
3. **Intuit already ships root-cause explanation inside QuickBooks** (AI report insights; Intuit Intelligence chat that names the customers, vendors or products behind a change). This was seen only as search snippets of intuit.com pages, since intuit.com was not reachable.
4. **Polar Analytics markets the exact question "Why did contribution margin fall this week?"** and says each answer carries a "Data Debug Sheet" (snippet). That is a documented evidence-trail feature in a direct Shopify competitor.
5. **Two Phase 2 claims need correcting:** the "Profit Pulse AI $19/month" listing is confirmed, but there are at least three other, differently-priced apps with near-identical names; and the Conjura acquisition date is confirmed with a one-line caveat on dating.
6. **I found no product whose public pages document all of:** a cross-system (Shopify + ledger) investigation, separate confidence for observation versus explanation, a counterevidence section, and outcome follow-up. That is an absence in what I could reach, not proof of absence.

---

## 1. Claude for Small Business and the Claude connectors

### 1a. What the primary pages say

| Capability | Status | Primary URL | Date seen | How verified |
|---|---|---|---|---|
| Product exists; launched 2026-05-13; installs as a toggle in Claude Cowork | EXISTS | https://www.anthropic.com/news/claude-for-small-business | 2026-11-19 | full page |
| Named workflows incl. "margin analyzer", "invoice chaser", "month-end prepper", "business pulse" | EXISTS (names only) | same | 2026-11-19 | full page: the page "only gives the name" of the margin analyzer |
| Margin analyzer: what it computes | UNVERIFIED | same; claude.com/solutions/small-business (margin, gross margin, COGS, profit: "None of these terms appear on the page") | 2026-11-19 | full page x2 |
| Cash planning: settles QuickBooks cash against PayPal settlements, 30-day forecast, ranks overdue items, queues reminders for approval | EXISTS | anthropic.com news page | 2026-11-19 | full page |
| Monthly close: reconciles books against settlements, flags mismatches, plain-English P&L, close packet | EXISTS | same | 2026-11-19 | full page |
| Business pulse on a schedule | EXISTS | same | 2026-11-19 | full page |
| Approval gate | EXISTS | same: quote "you approve before anything sends, posts, or pays" | 2026-11-19 | full page |
| Shopify + Stripe + QuickBooks used together in "close the books" | EXISTS | https://claude.com/solutions/small-business: quote "Claude can check your books against Stripe and Shopify, flag anything odd, and explain the month in plain English" | 2026-11-19 | full page |
| Scheduled runs (every Monday / month-end / new lead) | EXISTS | same | 2026-11-19 | full page |
| Pricing of the SMB product | UNVERIFIED | claude.com/solutions/small-business: "Pro for one person, Team for a business with more than one" (plan names only; no prices on the page) | 2026-11-19 | full page |

Note on the two Anthropic pages: the news page's fetch summary said "It does not mention Shopify or Xero" among connectors; the claude.com page names Shopify. The plugin's own `.mcp.json` (below) lists both. The conflict is about which page lists what; it does not affect the conclusion that the connectors exist.

### 1b. The open-source plugin (primary, GitHub `anthropics/knowledge-work-plugins`, `small-business/`)

| Capability | Status | URL | Date seen | How verified |
|---|---|---|---|---|
| 35 HTTP connectors defined, incl. `intuit-quickbooks`, `xero`, `shopify`, `paypal`, `stripe`, `myob`, `zoho-books` | EXISTS | https://github.com/anthropics/knowledge-work-plugins/blob/main/small-business/.mcp.json | 2026-11-19 | full page |
| 44 skills listed in `skills/`; **no skill named `margin-analyzer`, `margin` or `price-check`** in that listing | MISSING-with-evidence (in this repo path as of the date seen) | https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business/skills | 2026-11-19 | full page (fetch tool warned the listing "may not be the complete directory listing"; README also showed no such skill) |
| Third-party sites describe a published `margin-analyzer` skill (PayPal + QuickBooks, revenue/COGS/GM table) | UNVERIFIED (third-party only) | skills.sh/anthropics/knowledge-work-plugins/margin-analyzer (host blocked; seen as search-result title only) | 2026-11-19 | snippet |
| `report-builder`: saves a recurring report spec; pulls ledger + Shopify (orders, SKU-level revenue) + payment processors in one run; warns "a Shopify order and its Stripe settlement are one sale" | EXISTS | .../skills/report-builder/SKILL.md | 2026-11-19 | full page |
| `report-builder` margin / COGS | NEEDS-CONFIG | same: owner "would need to define those metrics in their spec" (fetch-summary wording); cost source not specified | 2026-11-19 | full page |
| `close-month`: ledger required; Shopify/Stripe/PayPal optional; reconciles; hard gate: quote "Do not start the forecast until the owner has signed off on the close" | EXISTS | .../skills/close-month/SKILL.md | 2026-11-19 | full page |
| `close-month` margin: reports "revenue and margin compared with the prior month"; triggers on questions about why revenue or margin moved; no dedicated variance module described | EXISTS (summary level) / UNVERIFIED (depth of "why") | same | 2026-11-19 | full page |
| `cash-flow-snapshot`: 30/60/90-day forecast, confidence bands, up to five named risks | EXISTS | .../skills/cash-flow-snapshot/SKILL.md | 2026-11-19 | full page |
| `cash-flow-snapshot` explaining why PAST cash changed | MISSING-with-evidence | same: fetch summary says it "does not reconcile last month's cash movement or attribute historical changes to causes"; past transactions are shown "for reference" only | 2026-11-19 | full page |
| `invoice-chase`: overdue AR from ledger, cross-checks PayPal/Stripe payments, scores `good-payer`/`occasionally-late`/`repeat-late`, drafts reminders; quote "Never send or queue a draft without explicit owner approval" | EXISTS | .../skills/invoice-chase/SKILL.md | 2026-11-19 | full page |
| `invoice-chase` explaining why DSO / late payments changed | MISSING-with-evidence | same: "has no DSO metric or trend analysis of its own" | 2026-11-19 | full page |
| `business-pulse` (Monday / Friday presets, delta, risks naming a record and next step) | EXISTS | .../skills/business-pulse/SKILL.md | 2026-11-19 | full page |
| `business-pulse` computes margin | MISSING-with-evidence | same: "doesn't compute margin directly" | 2026-11-19 | full page |
| `inventory-planner`: Shopify velocity, stockouts, reorder POs; unit cost required | EXISTS | .../skills/inventory-planner/SKILL.md | 2026-11-19 | full page |
| `inventory-planner` margin | MISSING-with-evidence | same: "no margin calculation, no gross-margin ranking" | 2026-11-19 | full page |
| Plugin-wide: every skill pauses before acting; nothing sent, posted, paid or written without explicit yes; "Figures that can't be read are reported as unreadable, not estimated" | EXISTS | https://github.com/anthropics/knowledge-work-plugins/blob/main/small-business/README.md | 2026-11-19 | full page |

**Interpretation, and what I cannot establish.** The skills are prompt files. Whether Claude, given a Shopify plus QuickBooks connection and a request like "why did gross margin fall in October", would produce a price/cost/mix bridge depends on the model, the data returned by connectors, and the user's request. No primary page documents that behaviour either way. "Margin analyzer" is therefore best labelled NEEDS-CONFIG at most and UNVERIFIED for depth. The skill library has no documented evidence ledger, no counterevidence step, no separate confidence for observation versus explanation, and no outcome follow-up. I treat those as "not documented in these skills", not as "Claude cannot do them when asked".

### 1c. The individual connectors (claude.com marketplace pages)

| Capability | Status | URL | Date seen | How verified |
|---|---|---|---|---|
| Intuit QuickBooks connector: P&L, cash-flow, balance sheet, A/R aging, sales by customer and by product, product/service list, industry benchmarking, invoice create/update/delete, transaction import; 74 tools, 25 listed | EXISTS | https://claude.com/marketplace/connectors/quickbooks | 2026-11-19 | full page |
| QuickBooks connector COGS / cost-by-item report | UNVERIFIED ("doesn't mention COGS by name"; only 25 of 74 tools shown) | same | 2026-11-19 | full page |
| QuickBooks connector write access with confirmation: "a clear preview and your confirmation before anything is sent" | EXISTS | same | 2026-11-19 | full page |
| QuickBooks connector regional limit: "currently available to US customers only" | EXISTS as stated by Intuit; **marketplace page lists no region limits** | Intuit help article, intuit.com host not reachable | 2026-11-19 | snippet |
| Xero connector: read-only; get_profit_and_loss, get_aged_receivables, get_invoices, get_top_customers_by_revenue, get_bank_account_transactions, etc. (20 tools) | EXISTS | https://claude.com/marketplace/connectors/xero | 2026-11-19 | full page |
| Xero connector: quote "Claude connects with read-only access" | EXISTS (limits write actions) | same | 2026-11-19 | full page |
| Xero connector: inventory/COGS-by-product report | UNVERIFIED (no such tool among the 20 named) | same | 2026-11-19 | full page |
| Shopify connector: `run-analytics-query`, `list-orders`, `get-order`, inventory, product and discount writes, GraphQL tools | EXISTS | https://claude.com/marketplace/connectors/shopify | 2026-11-19 | full page |
| Shopify connector: ShopifyQL, cost/profit data | UNVERIFIED (page says neither is mentioned) | same | 2026-11-19 | full page |
| Shopify connector: profitability questions may omit ad spend, fulfilment cost, returns | Third-party opinion only | community.shopify.com thread (seen in search results) | 2026-11-19 | snippet |

### 1d. Can Claude combine Shopify and QuickBooks/Xero data?

**EXISTS at the connector and skill level.** Both connectors are published, the plugin's `report-builder`, `close-month` and `business-pulse` skills read from a ledger and Shopify in the same run, and the claude.com page says Claude checks "your books against Stripe and Shopify". What is **not documented** is a margin-specific cross-system investigation with record-level evidence, a counterevidence step, or outcome follow-up.

---

## 2. Intuit / QuickBooks

intuit.com, quickbooks.intuit.com and developer.intuit.com all failed to resolve in this session (ENOTFOUND). Everything below is a **snippet** of a vendor-hosted page returned by WebSearch restricted to Intuit domains. I did not read any of these pages in full.

| Capability | Status | Primary URL (snippet) | Date seen | How verified |
|---|---|---|---|---|
| AI report insights on Profit & Loss and Balance Sheet: "hero number", headline, chart and root-cause analysis; up to 15 months of data | EXISTS | https://quickbooks.intuit.com/learn-support/en-us/help-article/business-reports/ai-powered-report-insights/L2jZq6tfM_US_en_US | 2026-11-19 | snippet |
| Plan for report insights: Plus, Advanced and Intuit Enterprise Suite per one passage, Plus and Advanced per its FAQ | UNVERIFIED (Intuit's own text conflicts) | same | 2026-11-19 | snippet |
| Intuit Intelligence chat: ask why a metric moved; answer names customers, vendors or products behind the change; Intuit example is a revenue decline driven by two customers | EXISTS | https://quickbooks.intuit.com/learn-support/en-us/help-article/intuit-ai/understand-business-trends-anomalies-intuit-intelligence/L6RpHl0M4_US_en_US | 2026-11-19 | snippet |
| Intuit Intelligence chat is beta with a monthly prompt cap (25 prompts per eligible plan per month) | EXISTS as a limitation | https://quickbooks.intuit.com/r/news/intuit-advances-mid-market-platform/ | 2026-11-19 | snippet |
| Anomaly detection in P&L and Balance Sheet | EXISTS | report-insights article above | 2026-11-19 | snippet |
| Product-level margin | UNVERIFIED. KPI scorecards track "revenue, margin, and cash"; product/service revenue reporting "tiered by plan"; whether product-level GM exists as a report is not shown | https://quickbooks.intuit.com/r/product-update/quickbooks-advanced-most-powerful/ | 2026-11-19 | snippet |
| Cash-flow forecasting inside QBO | EXISTS, needs history: "at least 2 years of transaction history", not available in Intuit Accountant Suite | https://quickbooks.intuit.com/learn-support/en-us/help-article/tasks/forecast-financial-performance-intuit-intelligence/L7o5sk5t2_US_en_US | 2026-11-19 | snippet |
| Finance AI in QBO Advanced / Intuit Enterprise Suite: P&L, cash flow, balance sheet, budget comparison; flags significant changes | EXISTS | https://quickbooks.intuit.com/learn-support/en-us/help-article/intuit-assist/get-started-finance-agent/L0g3aJO6W_US_en_US | 2026-11-19 | snippet |
| Accounting AI: finds AR/AP aging issues, duplicates, miscategorisations; root-cause summary and PDF | EXISTS | https://quickbooks.intuit.com/learn-support/en-us/help-article/bank-transactions/accounting-agent-features/L6pl9rv94_US_en_US | 2026-11-19 | snippet |
| AI Payments Agent: drafts reminders, suggests late fees, "paid up to 5 days faster on average" (vendor claim) | EXISTS (benefit claim unverified) | https://quickbooks.intuit.com/payments-agent/ | 2026-11-19 | snippet |
| Intuit-Anthropic partnership; QuickBooks connector in Claude; "currently available to US customers only" | EXISTS | https://investors.intuit.com/news-events/press-releases/detail/1305/... and https://quickbooks.intuit.com/learn-support/en-us/help-article/accounting-bookkeeping/use-quickbooks-connector-claude/L3YBlo6Ht_US_en_US | 2026-11-19 | snippet |
| Joins QuickBooks data with Shopify data inside QuickBooks AI | UNVERIFIED (not seen; QBO's AI works on the ledger) | n/a | 2026-11-19 | n/a |
| Separate confidence / counterevidence / outcome follow-up in report insights | UNVERIFIED (none seen in snippets) | n/a | 2026-11-19 | n/a |

**Reading.** The chat and insights can name which customers, vendors or products drove a change in the ledger. That is the "why" step at ledger level. It cannot, from what I saw, see Shopify order-level discounts, shipping or returns that never reach the ledger as separate lines, but I saw no document either confirming or refuting that.

---

## 3. Xero

xero.com, central.xero.com and developer.xero.com all failed to resolve. All Xero facts are **snippets** from WebSearch restricted to Xero domains, except the Claude connector page (full page, on claude.com).

| Capability | Status | Primary URL | Date seen | How verified |
|---|---|---|---|---|
| JAX (Just Ask Xero) AI assistant; natural-language questions with charts and tables; staged rollout starting in Australia | EXISTS (availability varies by region) | https://www.xero.com/us/media-releases/xeros-ai-financial-superagent-jax-launches-powerful-new-features/ (dated 2025-09-03) | 2026-11-19 | snippet |
| Gross-profit trend as a JAX example question; "dive deep into profitability" drill-down on mobile | EXISTS (drill-down); dedicated margin-bridge UNVERIFIED | https://www.xero.com/us/ai-in-accounting/jax/ | 2026-11-19 | snippet |
| Analytics tracks gross profit margin, net profit, DSO, cash runway | EXISTS | https://www.xero.com/us/accounting-software/analytics/ | 2026-11-19 | snippet |
| Analytics Plus: extended cash-flow forecast up to 90 days, scenarios; on the Established plan or as add-on | EXISTS | same | 2026-11-19 | snippet |
| Short-term forecast includes predictions for regular invoice and bill payments (2023 release) | EXISTS | https://www.xero.com/us/accounting-software/analytics/cash-flow/ | 2026-11-19 | snippet |
| Per-customer late-payment risk score | UNVERIFIED (search found none; "may exist but isn't covered") | n/a | 2026-11-19 | snippet |
| Forecast horizons by plan in AU (60/90/180 day) and a US 30-day lowest tier | EXISTS, regional | https://www.xero.com/au/... pricing pages | 2026-11-19 | snippet |
| Xero-Anthropic multi-year partnership (2026-03-27); Claude integration live (2026-05-12); read-only; free to add | EXISTS | https://www.xero.com/us/media-releases/xero-and-anthropic-collaborate/ ; https://www.xero.com/us/ai-in-accounting/claude/ | 2026-11-19 | snippet; connector page itself full-page |
| Ultra tier (Australia, medium business): Syft advanced reporting, scenario modelling, AI insights | EXISTS, AU only | https://www.xero.com/us/media-releases/xero-targets-medium-businesses-with-ultra/ | 2026-11-19 | snippet |
| Evidence trail / counterevidence / outcome follow-up | UNVERIFIED | n/a | 2026-11-19 | n/a |

---

## 4. Shopify

help.shopify.com, www.shopify.com, shopify.dev and apps.shopify.com all failed to resolve in WebFetch. All facts below are **snippets** from searches limited to Shopify domains.

| Capability | Status | Primary URL | Date seen | How verified |
|---|---|---|---|---|
| Native profit reports: gross profit by product, by variant, by POS location, profit margin by order, average margin by market | EXISTS, NEEDS-CONFIG (cost per item must be entered; profit only reported for items with a cost at time of sale) | https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports | 2026-11-19 | snippet |
| Gross margin in profit reports uses net sales after discounts and refunds | EXISTS | same | 2026-11-19 | snippet |
| Native profit excludes ad spend, payment fees, shipping | Third-party (community posts) only | community.shopify.com threads | 2026-11-19 | snippet; **UNVERIFIED as official** |
| Plan requirement for profit reports | UNVERIFIED (only an old changelog post: "Shopify Plan or higher") | https://changelog.shopify.com/posts/product-cost-and-profit-reporting-is-here | 2026-11-19 | snippet |
| Sidekick turns plain-language questions into ShopifyQL and explains the report | EXISTS | https://changelog.shopify.com/posts/turn-business-questions-into-analytics-reports-with-natural-language-queries | 2026-11-19 | snippet |
| Sidekick can give profit numbers only if per-product cost is entered | EXISTS, NEEDS-CONFIG | profit-reports help page | 2026-11-19 | snippet |
| Sidekick Pulse / "Sidekick suggestions": up to five proactive suggestion cards on Home, with citations; only some stores with recent sales; Shopify Network Intelligence must be on | EXISTS, restricted eligibility | https://help.shopify.com/en/manual/ai-powered-tools/sidekick/pulse ; https://changelog.shopify.com/posts/proactive-business-recommendations-from-sidekick | 2026-11-19 | snippet |
| Sidekick can use data from apps with supported Sidekick app extensions | EXISTS | https://changelog.shopify.com/posts/get-sidekick-recommendations-using-supported-app-data | 2026-11-19 | snippet |
| Shopify's own connector for Claude (not on App Store; read-only for analytics; runs ShopifyQL) | EXISTS | https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/shopify-connector-for-claude | 2026-11-19 | snippet |
| "Shopify Magic" | UNVERIFIED (not found in this pass) | n/a | 2026-11-19 | n/a |
| Margin decomposition between periods (price/cost/mix/discount/shipping/returns) in native Shopify | UNVERIFIED (no such report found; absence in search is not evidence) | n/a | 2026-11-19 | n/a |
| Accounting-ledger data (supplier invoices, landed cost not in Shopify) inside Shopify AI | UNVERIFIED | n/a | 2026-11-19 | n/a |

**Stocky.** Phase 2 said "shut down 2026-08-31". The snippet of Shopify's own help page says the app stopped being usable on August 31, 2026, with at least 90 days of read-only export; it was delisted on 2026-02-02. **CONFIRMED.** At today's date the 90-day window ends about 2026-11-29. Community posts claim native replenishment/min-max features are not planned for 2026; that is user-reported only.

---

## 5. NetSuite

netsuite.com and docs.oracle.com failed in WebFetch. Evidence is **snippets** from searches limited to Oracle/NetSuite domains.

| Capability | Status | Primary URL | Date seen | How verified |
|---|---|---|---|---|
| Ask Oracle conversational assistant; "reasoning that explains the 'how' and 'why' behind every response" | EXISTS (marketing language) | https://www.netsuite.com/artificial-intelligence.shtml | 2026-11-19 | snippet |
| "Why did margins drop" as a documented Ask Oracle use case | UNVERIFIED (exact phrase not found on any Oracle/NetSuite page) | n/a | 2026-11-19 | snippet |
| AI Units metering; Ask Oracle usage counts; a simple example question "could consume between 10-50 AI Units"; cost varies with complexity | EXISTS (metered) | https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_8144753226.html ; .../article_2163848930.html | 2026-11-19 | snippet |
| NetSuite Data Intelligence: AI-powered cloud data warehouse; "Deep Data Research Agent" for next steps and why | EXISTS (marketing) | https://www.netsuite.com/portal/collateral/public/ds-ns-data-intelligence.pdf | 2026-11-19 | snippet |
| Reads Shopify data | UNVERIFIED (NetSuite-native only seen) | n/a | 2026-11-19 | n/a |
| Evidence / counterevidence / outcome follow-up | UNVERIFIED | n/a | 2026-11-19 | n/a |

Phase 2's price estimate of "$129-199/user/month" was not re-checked; it is not a primary figure and I did not confirm it.

---

## 6. Cash-flow and AR tools

| Product / capability | Status | Primary URL | Date seen | How verified |
|---|---|---|---|---|
| **Fathom**: Xero and QuickBooks sync every 24h; Gold at $450/month incl. 25 companies, +$17 per extra company; AI "Commentary Writer"; AI variance/dashboard build-out per Fathom blog; MCP server announced with a webinar on 2026-12-02 | EXISTS; pricing from vendor page | https://www.fathomhq.com/pricing | 2026-11-19 | snippet |
| Fathom explains why margin changed at transaction level | UNVERIFIED | n/a | 2026-11-19 | n/a |
| **Float** (the capacity-planning product at float.com): scope is resource/capacity planning, staffing and project profitability; no QuickBooks integration since Feb 2024; Starter $7, Pro $12 per scheduled person | Not a cash-flow tool; **Phase 2/lead's "Float" framing should be disambiguated**. A separate cash-flow product also named Float (withfloat.com) was unreachable | https://www.float.com/pricing | 2026-11-19 | snippet |
| **Chaser**: AR automation; AI debtor risk insights; payment prediction; forecasting; automated letters; claims "60% DSO reduction" (vendor marketing); pricing not shown | EXISTS (vendor claims) | https://chaser.io/ | 2026-11-19 | snippet |
| **Upflow**: AR agents; DSO via Countback; root-cause analysis via "Ask Upflow"; Starter up to $10M invoiced revenue lists at $333, Grow up to $25M at $833 (billing period not stated); free Discover tier; autonomous agent sends only when confident, otherwise drafts | EXISTS | https://upflow.io/pricing ; https://upflow.io/features/analytics | 2026-11-19 | snippet |
| **Cash Flow Frog**: planned-vs-actual snapshots, drill-down by customer or vendor; ecommerce page describes transaction-level drill-down; $69/month up to $1M revenue to $249/month above $20M (pages disagree on early-bird price) | EXISTS (drill-down); "explains WHY cash changed" UNVERIFIED | https://cashflowfrog.com/pricing/ | 2026-11-19 | snippet |
| **Jirav**: budget vs actual, integrated projections; pricing shown is wholesale for accounting firms ($50 / $150 starting points) | EXISTS; pricing not comparable | https://www.jirav.com/pricing | 2026-11-19 | snippet |
| **Planful, Pulse (cash app)**: not found by search | UNVERIFIED | n/a | 2026-11-19 | n/a |
| Any of the above combines Shopify order-level data with ledger data to explain DSO or cash change with an evidence trail | UNVERIFIED (not seen; Cash Flow Frog's ecommerce page mentions ad-platform bills as drivers) | n/a | 2026-11-19 | snippet |

---

## 7. Shopify profit apps

All **snippets** (apps.shopify.com and vendor sites were not fetchable).

| Product | What the official page claims | Margin-change decomposition / "why margin moved" | Pricing seen | Primary URL |
|---|---|---|---|---|
| **TrueProfit** | Live profit per order after COGS, shipping, payment fees, taxes, refunds, ad spend; product-level and ad-level profit; P&L report on Advanced | UNVERIFIED (none seen) | $35 / $60 / $100 / $200 per month by order volume, $0.30 overage on Basic. Vendor's own pages disagree on a tier limit (3,000 vs 3,500) | https://apps.shopify.com/trueprofit |
| **Lifetimely (Amp)** | Real-time profit, P&L, LTV; "Profit Agent" that "runs the full cycle: monitor, diagnose, plan, execute on your approval" | EXISTS as marketing ("diagnose"); depth and method UNVERIFIED | Free to 50 orders; paid ladders conflict ($49/$79/$149 entry on different pages; $149-$999 in help docs); 5,000 credits/month | https://useamp.com/pricing/ |
| **Polar Analytics** | Governed metrics; "Ask Polar" and Polar MCP; homepage example "Why did contribution margin fall this week?"; each answer has a "Data Debug Sheet"; margin waterfall via custom metrics | EXISTS as marketing for an explanation question; automatic price/cost/mix bridge UNVERIFIED; no worked example seen | Not retrieved | https://www.polaranalytics.com/ |
| **Triple Whale** | Net profit = sales - ad spend - COGS, shipping, handling, fees, taxes, custom; **gross profit/margin "not provided by default"** (build in Custom Metric Builder); Moby AI; Automate tier adds automations and governed actions | Triple Whale's own knowledge base says gross margin must be custom-built (MISSING by default, per vendor text); decomposition UNVERIFIED | Foundation $219/month, Automate $749/month per Shopify listing; official page says price depends on GMV | https://kb.triplewhale.com (summary dashboard metrics library) |
| **Conjura** | SKU-level contribution profit incl. ad spend, refunds, fees; Owly AI pricing recommendations and plain-English questions; ERP links (Brightpearl, Linnworks, Cin7, NetSuite) | Decomposition UNVERIFIED | Third-party lists from $299 (currency unresolved) | https://www.conjura.com/ |
| **BeProfit** | Profit per order and product; POAS; Gross P&L; "Ask Claude or ChatGPT" via MCP; AI credits | UNVERIFIED | Newer listing: Free; $29 (200 credits), $99 (400), $149 (600), Enterprise from $249; older listing $49 | https://apps.shopify.com/beprofit-profit-tracker |
| **Hypersonix Profit Max AI** | Shopify listing: daily; vendor blog: weekly; ranked by profit impact; reprice, discount or reorder lists to variant level; accept/reject price | Recommendations, not decomposition (UNVERIFIED depth) | Not retrieved | https://apps.shopify.com/profitgpt |
| **Marjn / ProfitGuard Pro / AI Profit Analytics** | Marjn: landed cost and ad spend, low-margin alerts at $19 Pro; ProfitGuard Pro: $19, alerts and action centre; AI Profit Analytics: $19 tier | Alerts only as described | $19 tiers | https://apps.shopify.com/marjn |

**Question: does any decompose margin change between periods automatically?** I found marketing language implying explanation (Polar, Lifetimely "diagnose") and a statement from Triple Whale that gross margin is not even built in. I found **no official page that documents an automatic price / cost / mix / discount / shipping / returns bridge** in this set. That is UNVERIFIED, not MISSING: Polar's "Data Debug Sheet" and margin waterfall suggest partial capability, and I could not open any of these pages.

### 7b. Phase 2 spot-checks

- **Profit Pulse AI $19/month:** a search returned the Shopify listing apps.shopify.com/profit-pulse-ai: "Das Group", $19/month, 0 reviews, "turns Shopify order profit into a margin exception queue" (snippet, Shopify host). **CONFIRMED.** Correction: at least three other apps use near-identical names (Profit Pulse: P&L & Net Profit from $14; Profit Pulse: AI Net Profit from $35; Profit Pulse by Argora at $29.99), plus Hypersonix uses "Profit Pulse" as a product name. Any committee reference to "Profit Pulse" must name the developer.
- **Conjura / Wayflyer:** Business Wire, Wayflyer and Conjura pages returned in search; dateline 2026-06-19, terms undisclosed, all employees expected to join Wayflyer, Conjura "pivot toward a natural language interface". The Conjura blog is dated June 17. **CONFIRMED with a dating note.**

---

## 8. Products combining Shopify and QuickBooks/Xero to explain margin or cash with an evidence trail

| Candidate | What it joins | Explains margin or cash change? | Evidence trail | Status |
|---|---|---|---|---|
| Claude + Shopify + QuickBooks/Xero connectors with SMB plugin | Shopify orders and SKU revenue, ledger, payment processors | Depends on prompt; `close-month` reports margin vs prior month; `cash-flow-snapshot` does not explain history (documented) | Detail sheets; raw-data tab; "n/a" rule | NEEDS-CONFIG; depth UNVERIFIED |
| A2X, Link My Books | Shopify payouts to QuickBooks/Xero, with SKU COGS option | No; bookkeeping accuracy tools | Payout-level journals | EXISTS as plumbing; explanation not claimed (snippet) |
| Polar Analytics + A2X integration page | Shopify store/ads/finance data in a warehouse | "Why did contribution margin fall" marketed | "Data Debug Sheet" | UNVERIFIED depth |
| Conjura | Shopify, ads, ERPs (Brightpearl, Linnworks, Cin7, NetSuite) | SKU contribution; PVM UNVERIFIED | SKU-level | UNVERIFIED |
| QuickBooks AI insights | Ledger only | Root cause by customer/vendor/product | Chart with 12-month history | EXISTS for ledger only |
| NetSuite Ask Oracle | NetSuite only | "How/why" reasoning marketed | UNVERIFIED | UNVERIFIED |

No product seen documents **Shopify + ledger + supplier-cost evidence, with a counterevidence section and outcome follow-up**.

---

## 9. Phase 2 claims

| Phase 2 claim | Verdict | Basis |
|---|---|---|
| Claude for Small Business: "no margin workflow found" | **REFUTED** (a "margin analyzer" is named) but **depth STILL UNVERIFIED** | Anthropic news page (full page): name only. No primary spec found; no skill with that name in plugin skill list |
| Claude for Small Business connects QuickBooks, PayPal, HubSpot | **CORRECTED**: the plugin defines 35 connectors, including Shopify, Xero, Stripe | `.mcp.json` full page |
| Claude for Small Business queues actions for approval | **CONFIRMED**, and stronger than Phase 2: README says nothing sent, posted, paid or written without explicit yes | README full page |
| Profit Pulse AI $19/month | **CONFIRMED**, with name-collision correction | Shopify listing snippet |
| Conjura acquired by Wayflyer 2026-06-19 | **CONFIRMED** (one-line dating note) | Business Wire / Wayflyer / Conjura snippets |
| Stocky shutdown 2026-08-31 | **CONFIRMED** | Shopify help page snippet |
| QuickBooks "Intuit Intelligence Chat" on Advanced/Enterprise Suite | **CONFIRMED with correction**: marked beta, 25 prompts/month, available to "all eligible" QBO, Advanced and Enterprise Suite | Intuit snippets |
| QuickBooks product margin "UNKNOWN" | **STILL UNVERIFIED** | Margin on scorecards; product-level GM report not confirmed |
| Xero JAX gross-margin overview "AU/NZ" | **STILL UNVERIFIED**; JAX gross-profit trend questions and Analytics gross margin are documented; region split unclear | Xero snippets |
| Xero JAX features | **CORRECTED**: add Claude integration (live 2026-05-12, read-only); late-payment scoring not found | Xero snippets |
| NetSuite Ask Oracle "why did margins drop" | **STILL UNVERIFIED** as a documented use case (partner-blog phrasing); Oracle documents "how/why" reasoning generally and AI Unit metering | Oracle snippets |
| Triple Whale "weak margin view (competitor blogs)" | **CONFIRMED by the vendor's own knowledge base**: gross profit/margin not provided by default | Triple Whale KB snippet |
| Polar says Shopify-only AI misattributes | **STILL UNVERIFIED** (not re-seen); but Polar markets a margin question and a "Data Debug Sheet" | Polar snippet |
| Lifetimely "Profit Agent acts on approval" | **CONFIRMED** (vendor wording) | Amp pricing snippet |
| TrueProfit $35-$200 by orders | **CONFIRMED** (listing snippet; vendor pages inconsistent on one limit) | Shopify listing snippet |
| Hypersonix "weekly ranked recs" | **CORRECTED**: Shopify listing says daily; vendor blog says weekly | Hypersonix/Shopify snippets |
| Fathom "approx $50+" | **CORRECTED**: pricing page lists Gold $450/month for 25 companies (about $18 per company) | Fathom pricing snippet |

---

## 10. Host reachability

| Host | Result |
|---|---|
| www.anthropic.com | WORKS (full page) |
| claude.com (solutions page, marketplace connector pages) | WORKS |
| support.claude.com | Resolved but returned 404 for the guessed article path; no help-centre article found |
| github.com, raw.githubusercontent.com | github.com WORKS; raw.githubusercontent.com resolved but the guessed skill path returned 404 |
| academy.claude.com | BLOCKED (ENOTFOUND) |
| www.intuit.com, quickbooks.intuit.com, developer.intuit.com | BLOCKED |
| www.xero.com, central.xero.com, developer.xero.com | BLOCKED |
| www.shopify.com, help.shopify.com, shopify.dev, apps.shopify.com | BLOCKED |
| www.netsuite.com, docs.oracle.com | BLOCKED |
| fathomhq.com, www.chaser.io, withfloat.com, upflow.io, trueprofit.io, www.useamp.com, www.polaranalytics.com, www.hypersonix.ai, www.marginedge.com, www.businesswire.com, www.skills.sh | BLOCKED |
| Not retried after repeated failures: vendavo.com, phocas, coefficient.io, jirav, planful, g2 | Seen only as search-result snippets |

I also tried the GitHub API through the shell; the session's permission layer refused it, and I did not work around it.

---

## 11. Verdict: real unmet need, or repackaging?

**Mostly repackaging at the level of any single step; the residual gap is narrower than Phase 2 implied and is not yet proven to be a paid need.**

1. **Detection.** Shopify Pulse/suggestions, Hypersonix, Profit Pulse AI and QuickBooks anomaly insights already flag things. EXISTS.
2. **Explanation inside one system.** QuickBooks' "why did this change" names the customers, vendors or products behind a movement (snippets), Xero JAX answers gross-profit questions, Ask Oracle markets reasoning, and Polar markets "Why did contribution margin fall?" with a debug sheet. A reasonable owner on QuickBooks, Xero or Polar already has an explanation button. EXISTS, quality UNVERIFIED.
3. **Cross-system (Shopify + ledger) by an AI that an owner can already rent.** The Claude SMB plugin and the three connectors exist today, are documented, and include approval gates, a saved-report mechanism and scheduling. The package is the same shape as the proposed product's front end. What the skills do not document is a margin-bridge method, a cost source for margin, or any explanation of past cash or DSO movement. Two skills state that limitation themselves (cash-flow-snapshot, invoice-chase). That is the strongest positive evidence of a gap I found, but it describes prompt files, and an owner who asks Claude directly could get more than the skill promises.
4. **Case file with separate confidence for observation versus explanation, counterevidence, outcome follow-up.** I found no vendor documenting these. Absence in what I could read, from vendors whose primary pages were mostly blocked, is weak evidence. The plugin's rules ("Do not invent a number", unreadable figures reported as unreadable) show Anthropic's own skills are moving toward evidence discipline, so this is a feature a platform vendor could add with a prompt change.

**Answer to the committee.** Today the honest description is: **packaging existing functionality into a new interface for the detection, single-system explanation and cross-system data access steps; a possible unmet need only in the last mile** (a persistent, auditable case file that separates "what changed" from "why", records counterevidence, and checks the outcome). Whether owners will pay for that last mile is untested by anything I found. The risk is not that the capability is missing; it is that Anthropic, Intuit or Polar can close it quickly, and that a prompted Claude session may already deliver 70-80% of it for the price of a licence. That last percentage is a judgement, not a measurement.

**What would change this verdict.**
- A hands-on run of the Claude SMB plugin, with Shopify and QuickBooks connected, on a real margin-erosion case (a trial, which this session was not allowed to do).
- A read of the margin analyzer's actual specification (not found in the 44-skill listing).
- A hands-on run of Polar's Ask Polar and QuickBooks Intuit Intelligence on the same data.
- Evidence of willingness to pay for outcome tracking, which none of these pages can supply.

---

## SOURCE REGISTER

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

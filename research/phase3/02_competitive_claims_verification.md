# 02 — Competitive Claims Verification

**Basis:** `appendix/p3_a1_competitive_verification.md` (52-row source register). **Reachability:** full-page reads only for www.anthropic.com, claude.com (solutions page, marketplace connector pages) and github.com (Anthropic's `knowledge-work-plugins` repository). Intuit, Xero, Shopify, NetSuite/Oracle and every other vendor were **blocked** (`getaddrinfo ENOTFOUND`); their rows are **search snippets of vendor-hosted pages**. WebFetch itself summarises pages with a small model, so even "full page" rows are machine summaries, not raw HTML.

**Status labels:** **EXISTS** (documented) · **NEEDS-CONFIG** (works once the user defines or supplies something) · **NEEDS-SERVICES** (vendor/partner services required) · **MISSING-with-evidence** (an explicit documented limitation) · **UNVERIFIED** (not seen or seen too thinly). UNVERIFIED never means absent.

## 1. The workflow we proposed, step by step, versus what exists

Proposed: **(1)** detect a margin/cash change → **(2)** investigate it across Shopify and ledger data → **(3)** write an evidence-linked case file with counterevidence and separate confidence for "what changed" vs "why" → **(4)** recommend an action → **(5)** follow up on the outcome.

| Step | Where it already exists | Status | Evidence |
|---|---|---|---|
| 1. Detect | Shopify Sidekick suggestions (up to five cards, limited eligibility); Profit Pulse AI ($19); Hypersonix; Intuit AI report insights and anomaly detection; Xero Analytics; Claude "business pulse" | **EXISTS** | Vendor pages (snippets) and Anthropic page (full) |
| 2a. Explain *inside one system* | QuickBooks AI insights and Intuit Intelligence chat name the customers, vendors or products behind a change (beta, 25 prompts/month); Xero JAX answers gross-profit questions; Polar markets "Why did contribution margin fall this week?" | **EXISTS** (quality **UNVERIFIED**) | Snippets of vendor pages |
| 2b. Explain *across* Shopify + ledger | Claude Small Business plugin: Shopify, QuickBooks/Xero, Stripe, PayPal connectors; `report-builder`, `close-month`, `business-pulse` skills combine ledger and Shopify data in one run | **EXISTS at connector/skill level; NEEDS-CONFIG for margin** | **Full pages** (GitHub, claude.com). Margin and COGS definition left to the owner; margin-analyzer depth **UNVERIFIED** |
| 3a. Evidence trail | Polar "Data Debug Sheet" (snippet); plugin "detail sheets / raw-data tab" and "unreadable figures are reported as unreadable, not estimated" (full page) | **EXISTS (partial)** | |
| 3b. Counterevidence section; separate confidence for observation vs explanation | None documented by any product reached | **UNVERIFIED** (not seen; not proven absent) | Phase 2 and Phase 3 agree |
| 4. Recommend actions | Hypersonix, Lifetimely ("Profit Agent… executes on your approval"), Conjura, Claude invoice-chaser drafts, Intuit Payments agent | **EXISTS** | |
| 5. Follow up on outcomes | Aera Decision Ledger (enterprise); none for SMB found | **UNVERIFIED** at SMB | |

## 2. What the Claude Small Business plugin documents about itself (primary, full page)

| Capability | Status |
|---|---|
| 35 connectors defined, including `intuit-quickbooks`, `xero`, `shopify`, `paypal`, `stripe`, `myob`, `zoho-books` | **EXISTS** |
| Named workflows: margin analyzer, invoice chaser, month-end prepper, business pulse; 15 workflows total (launched 2026-05-13) | **EXISTS (names)** |
| "Margin analyzer": what it computes | **UNVERIFIED** (the launch page gives only the name; the claude.com page does not mention margin, COGS or profit; the plugin's 44 listed skills include no skill with that name — "may not be the complete directory listing"; third-party sites describe one) |
| `cash-flow-snapshot`: 30/60/90-day forecast with confidence bands and up to five named risks | **EXISTS**; "does not reconcile last month's cash movement or attribute historical changes to causes" → **MISSING-with-evidence** for *explaining past cash change* |
| `invoice-chase`: ranks overdue AR, scores payers good/occasionally-late/repeat-late, drafts reminders; "never send or queue a draft without explicit owner approval" | **EXISTS**; "has no DSO metric or trend analysis of its own" → **MISSING-with-evidence** for DSO explanation |
| `business-pulse`: scheduled Monday/Friday digest with risks naming a record and a next step | **EXISTS**; "doesn't compute margin directly" |
| `close-month`: reconciles ledger against Shopify/Stripe/PayPal, reports revenue and margin versus prior month, triggers on questions about why margin moved | **EXISTS (summary level)**; depth of "why" **UNVERIFIED** |
| `report-builder`: saved recurring report; pulls ledger + Shopify orders/SKU revenue + processors; margin/COGS "would need to define those metrics" | **NEEDS-CONFIG** |
| QuickBooks connector: P&L, cash flow, A/R aging, sales by customer/product; 74 tools (25 listed); COGS by item **UNVERIFIED**; US customers only per Intuit (snippet) | **EXISTS** |
| Xero connector: read-only; P&L, aged receivables, invoices, top customers; 20 tools; inventory/COGS **UNVERIFIED** | **EXISTS** |
| Shopify connector: analytics queries, orders, inventory, GraphQL; ShopifyQL and cost/profit data **UNVERIFIED** | **EXISTS** |
| Approval gates: nothing sent, posted, paid or written without explicit yes | **EXISTS** |
| Pricing of the SMB product | **UNVERIFIED** ("Pro for one person, Team for more than one"; no prices) |

**Interpretation limit:** these skills are prompt files. Whether Claude with Shopify and QuickBooks connected would produce a price/cost/mix bridge when asked "why did gross margin fall in October" depends on the model, connector data and the request. No primary page documents that behaviour either way. That is exactly what Gate 0 (`04`) tests.

## 3. Product-by-product status

| Product | What exists | Needs configuration | Needs services | Documented limit / missing | Unverified |
|---|---|---|---|---|---|
| **Claude SMB** | Cross-system data access; cash forecast; AR chasing; close; scheduled pulse; approval gates | Margin and COGS definitions; saved report specs | — | Past-cash causation; DSO analysis; margin in pulse | Margin analyzer depth; price |
| **QuickBooks / Intuit** (snippets) | AI report insights with root-cause on P&L/BS (up to 15 months); Intuit Intelligence chat naming drivers; anomaly detection; AR/AP aging issues; Payments agent; forecasting with ≥2 years history | Plan tier (conflicting texts); beta limits (25 prompts/month) | — | Cannot see Shopify order-level discounts/shipping/returns (inference, no source) | Product-level margin report; confidence/counterevidence/outcome tracking |
| **Xero** (snippets) | JAX; Analytics with gross margin, DSO, runway; 90-day forecast (Analytics Plus); Claude integration read-only (2026-05-12) | Region and plan (AU-first rollouts) | — | — | Late-payment risk score; margin bridge; evidence trail |
| **Shopify native** (snippets) | Profit reports by product/variant/order; Sidekick → ShopifyQL; Sidekick suggestions; Shopify connector for Claude | **Cost per item must be entered** | — | Ads, fees, shipping excluded per community posts (not official) | Period-over-period margin bridge |
| **NetSuite** (snippets) | Ask Oracle ("how/why" reasoning, metered "AI Units"); Data Intelligence | Admin/partner | Partner services common | NetSuite data only | "Why did margins drop" as a documented use case; reads Shopify |
| **Polar** (snippet) | "Why did contribution margin fall this week?"; Data Debug Sheet; margin waterfall via custom metrics | Metric setup | Onboarding by vendor | — | Automatic price/cost/mix bridge; price |
| **Lifetimely/Amp** (snippet) | Profit P&L; "Profit Agent: monitor, diagnose, plan, execute on your approval" | — | — | — | Depth of "diagnose" |
| **Triple Whale** (vendor KB, snippet) | Net profit; Moby AI | **Gross profit/margin "not provided by default"** (custom metric) | — | Confirmed by the vendor's own knowledge base | Decomposition |
| **TrueProfit, BeProfit, Conjura, Hypersonix, Profit Pulse AI** (snippets) | Per-order/SKU profit; alerts; ranked recommendations | Cost inputs | — | — | Any automatic period decomposition |
| **Fathom** (snippet) | Reporting for QuickBooks/Xero; AI commentary; $450/mo for 25 companies; MCP server announced (webinar 2026-12-02) | Accountant setup | — | — | Transaction-level "why margin changed" |
| **Upflow, Chaser** (snippets) | AR automation; DSO; root-cause "Ask Upflow" (Upflow); AI debtor risk (Chaser) | — | — | — | Shopify order data joined to ledger |
| **Cash Flow Frog** (snippet) | Planned-vs-actual with customer/vendor drill-down | — | — | — | "Explains why cash changed" |
| **Float** | Float.com is capacity/resource planning, not cash flow; a separate cash-flow product also named Float was unreachable. Phase 2's "Float" framing was ambiguous | | | | |

**Cash/AR specifically:** Claude's invoice chaser and cash forecast, Intuit's Payments agent and forecasting, Xero's Analytics Plus forecast, Upflow and Chaser together cover detection, prioritisation and reminders. The one documented *gap* is explaining *why* past cash or DSO changed (Claude's own skill files say they do not do it). Nobody was shown to join Shopify order-level data to the ledger to explain DSO or cash change with an evidence trail.

## 4. Corrections to Phase 2 competitive claims
| Claim | Phase 3 result |
|---|---|
| Claude SMB: "no margin workflow found" | **Refuted** (name exists; depth unverified) |
| Claude SMB connects QuickBooks, PayPal, HubSpot | **Corrected** (35 connectors incl. Shopify, Xero, Stripe) |
| Claude SMB queues actions for approval | **Confirmed** and stronger (nothing written without explicit yes) |
| Profit Pulse AI $19/month | **Confirmed**; ≥3 other apps share the name (name the developer: Das Group); feature description ("exception queue") unconfirmed |
| Conjura acquired by Wayflyer 2026-06-19 | **Confirmed** (one source gives 06-22; Wayflyer was incubated inside Conjura) |
| Stocky shut down 2026-08-31 | **Confirmed** (delisted 2026-02-02) |
| Intuit Intelligence chat on Advanced/Enterprise Suite | **Confirmed with correction:** beta, 25 prompts/month, broader eligibility |
| Triple Whale weak margin view | **Confirmed by the vendor's own KB** |
| Hypersonix "weekly ranked recs" | **Corrected:** Shopify listing says daily; vendor blog says weekly |
| Fathom "~$50+" | **Corrected:** $450/month Gold tier for 25 companies (≈ $18 each) |
| NetSuite Ask Oracle "why did margins drop" | **Still unverified** as a documented use case; Oracle documents "how/why" reasoning generally and AI Unit metering |
| Polar "says Shopify-only AI misattributes" | **Not re-seen** |

## 5. Answer to the committee's question

**Is there a real unmet customer need, or are we packaging existing functionality into a new interface?**

- **Today, mostly packaging.** Detection, single-system explanation, cross-system data access, approval-gated actions, saved reports and scheduling all exist in rentable form (a Claude licence plus free connectors; Intuit and Xero bundled; Polar and Lifetimely for Shopify). A prompted Claude session may already deliver a large share of the proposed front end; the share is a judgment, not a measurement.
- **A narrow last mile may be unmet:** a persistent, auditable case file that separates "what changed" from "why", records counterevidence and what could not be checked, and checks the outcome later. The plugin's own limits (no explanation of past cash movement, no DSO analysis, no margin in the pulse, margin/COGS left to the owner) are the strongest positive evidence of this gap. No vendor reached documents it.
- **Whether anyone pays for that last mile is untested.** Anthropic, Intuit or Polar could add it quickly. The product, if it exists, is probably an **evidence-and-investigation layer** (deterministic bridges, row-level lineage, abstention, outcome log), not another assistant.

## 6. What would change this verdict
A hands-on run of the Claude plugin with Shopify and QuickBooks connected on a seeded margin case; the margin analyzer's actual specification; hands-on runs of Polar's "Ask Polar" and Intuit Intelligence on the same data; any evidence that owners pay for outcome tracking. **Blocked hosts to allow for a primary-page rerun:** intuit.com, quickbooks.intuit.com, developer.intuit.com, xero.com, central.xero.com, developer.xero.com, shopify.com, help.shopify.com, shopify.dev, apps.shopify.com, netsuite.com, docs.oracle.com, polaranalytics.com, useamp.com, fathomhq.com, chaser.io, upflow.io, g2.com.

# Phase 3, Agent 4: Independent Customer-Evidence Mining

**Date:** 2026-11-19. **Status:** read-only research. No one contacted, nothing signed up for, nothing paid for.
**Thesis under test:** "Owners will pay for an explanation of why margin or cash moved."

## 0. Bottom line (read this first)

**I obtained no verbatim customer text that I read on a page myself.** Every page-level fetch failed. The only evidence channel that worked was WebSearch, which returns a model-written summary of the results, not the raw page text. Some of those summaries embed short fragments in quotation marks or parentheses. I record those fragments below, but they are **second-hand: I did not see them on the source page, and I cannot confirm that they are exact or in context.** Treat them as leads to verify, not as verbatim customer voice.

Counts:

| Measure | Count |
|---|---|
| Distinct host classes where WebFetch was attempted | 17 |
| Hosts where WebFetch returned page content | **0** |
| Search queries that returned usable result lists | 11 |
| Search queries blocked outright (reddit.com is "not accessible to our user agent") | 3 |
| Relevant customer-forum threads whose existence is confirmed by a URL in search results | 22 |
| Threads whose body I actually read | **0** |
| Items where a poster says they would pay, or did pay, for a profit or margin explanation | **0** |
| Items that contradict the thesis (direct statement that nobody pays, or that existing tools suffice) | **0** direct; 2 weak indirect (E-12, E-13) |
| Items that support the thesis, weakly (the problem is described by owners) | 8 |

The headline result for the committee: **this session did not fill the customer-voice hole.** It closed no part of the willingness-to-pay question. It adds modest, second-hand corroboration that the *pain* is discussed publicly. It adds nothing on the *purchase*.

---

## 1. Hosts reachable vs blocked

WebFetch was tested directly. Failures were either "Claude Code is unable to fetch from <host>" (a policy block) or `getaddrinfo ENOTFOUND` (the host is not on the session's allowed network).

| Host | WebFetch | Notes |
|---|---|---|
| www.reddit.com | BLOCKED (policy) | Same as earlier sessions |
| old.reddit.com | BLOCKED (policy) | |
| reddit.com via WebSearch `allowed_domains` | BLOCKED | API error 400: "not accessible to our user agent". Reddit cannot be searched at all, so no Reddit snippets either |
| hn.algolia.com | ENOTFOUND | |
| news.ycombinator.com | ENOTFOUND | HN pages do appear as *search results*, but cannot be fetched |
| community.shopify.com | ENOTFOUND | Appears in search results only |
| apps.shopify.com | ENOTFOUND | Review pages unreadable |
| www.trustpilot.com | ENOTFOUND | |
| www.capterra.com | ENOTFOUND | |
| quickbooks.intuit.com | ENOTFOUND | Appears in search results only |
| community.xero.com | ENOTFOUND | Appears in search results only |
| www.indiehackers.com | ENOTFOUND | |
| dev.to | ENOTFOUND | |
| ecommercefastlane.com | ENOTFOUND | |
| g2.com, softwareadvice.com, producthunt.com, medium.com, substack.com, apps.xero.com, community.intuit.com, redlib mirrors, YouTube transcripts | NOT TRIED | The first ENOTFOUND message instructed stopping the host sweep; the pattern (every non-Anthropic host fails) made further attempts low-value. A different session with a wider allowlist should try these. |

**WebSearch (non-Reddit domains)** works. The result list shows real URLs on news.ycombinator.com, community.shopify.com, quickbooks.intuit.com and community.xero.com. The prose answer is machine-summarised and sometimes explicitly says "I did not find a thread" for what I asked. This matters: **the search tool's own summaries repeatedly stated that results were vendor blogs, promotional posts or AI-generated summaries.**

To obtain real verbatim voice, the session's network allowlist would need to add at least: `news.ycombinator.com`, `hn.algolia.com`, `community.shopify.com`, `apps.shopify.com`, `quickbooks.intuit.com`, `community.xero.com`, `www.trustpilot.com`, `www.capterra.com`, and Reddit would still need a policy exception that may not exist.

---

## 2. Evidence log

**Verification key**
- **S-url:** the URL was returned in a search result list (so it exists as indexed), but I did not read the page.
- **S-sum:** the quoted text appears inside the search tool's summary, in quotation marks or parentheses. **It is NOT confirmed verbatim against the source.**
- **S-para:** the content is the search tool's paraphrase, not a quote. I give no quotation.

Dates: the search results gave no reliable posting dates except one relative one (E-07, "about 287 days ago" as of the search, which puts it roughly February 2026). Where I do not know the date I say "unknown". I did not infer dates from thread numbers.

Classification: S = supports, C = contradicts, N = neutral, relative to "owners will pay for an explanation of why margin or cash moved". "Supports" here means only that the pain is described. Nothing here evidences payment.

| ID | URL | Date | Platform | Poster role | Text (marked S-sum or S-para) | Theme | Class | Verification |
|---|---|---|---|---|---|---|---|---|
| E-01 | https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805 | unknown | Shopify Community | unclear; search tool said several such threads are vendor-written | S-sum: "Shopify does not track historical landed costs (production + shipping + duties). It only keeps the current cost you set for a product. When costs change, old orders will adjust to the new cost." | 1, 2 (stale COGS) | S (pain), but poster may be a vendor | S-url + S-sum |
| E-02 | https://community.shopify.com/t/profit-ad-spend-tracking-on-shopify-whats-actually-broken-for-you/646399 | unknown | Shopify Community | unknown, title reads like a vendor discovery post | Title only: "Profit/ad-spend tracking on Shopify — what's actually broken for you?" No body seen. | 1 | N | S-url only |
| E-03 | https://community.shopify.com/t/how-can-i-accurately-calculate-the-net-profit-per-order/631719 | unknown | Shopify Community | merchant (inferred from title) | Title only: "How can I accurately calculate the net profit per order?" | 1 | S (a merchant is asking) | S-url only |
| E-04 | https://community.shopify.com/t/replace-my-spreadsheet-track-cost-revenue-and-margin-in-shopify/567219 | unknown | Shopify Community | unknown | Title only: "Replace my spreadsheet: track cost, revenue, and margin in Shopify" | 1 (spreadsheet use) | S (spreadsheet is the incumbent) | S-url only |
| E-05 | https://community.shopify.com/t/anyone-using-clearprofit-for-profit-tracking-thinking-of-switching-from-spreadsheets/588628 | unknown | Shopify Community | merchant asking; search tool says a founder also pitches a competing tool in it | Title only: "Anyone using ClearProfit for profit tracking? Thinking of switching from spreadsheets" | 1, 2 | S (spreadsheet incumbent, tool shopping) | S-url only; vendor presence reported by search tool |
| E-06 | https://community.shopify.com/t/how-do-you-pack-shopify-numbers-for-your-accountant-each-month/669948 and https://community.shopify.com/t/stuck-in-sheets-for-sales-reports-how-are-you-handling-this/673334 | unknown | Shopify Community | merchants (inferred from titles) | Titles only: "How do you pack Shopify numbers for your accountant each month?" / "Stuck in Sheets for sales reports" | 1 | S | S-url only |
| E-07 | https://news.ycombinator.com/item?id=46901206 | about Feb 2026 (search-tool relative date, "about 287 days ago") | Hacker News (Show HN) | founder with finance background | S-para: built an accounting system as an MCP server, 17 tools, local SQLite, "Claude as the UI layer". Comments were not returned. | 3 (DIY with Claude) | N (a builder, not a buyer; shows DIY demand among technical users) | S-url + S-para |
| E-08 | https://news.ycombinator.com/item?id=47180585 | unknown | Hacker News (Show HN) | developer | S-para: qbo-cli, a QuickBooks CLI for AI agents; the author criticised the official QBO MCP server for "parameter inconsistencies and results that fill up the context window" (this phrase was in the summary, not marked as a direct quote) | 3 | N | S-url + S-para |
| E-09 | https://news.ycombinator.com/item?id=48130950 | unknown (the "Claude for Small Business" thread) | Hacker News | commenters, mixed | S-sum (summary of several commenters, not individual quotes): one commenter "cancelled QuickBooks after using AI to do their LLC's bookkeeping" and "their CPA said the books look great"; another would "never give Claude or any AI agent direct write access to financial operations like payouts or settlements"; another called the official QuickBooks Online MCP server "a mess"; another noted some QBO MCP connections "don't do RBAC at all". I cannot attribute these to individual comment IDs. | 3, 7 | Mixed: S for DIY-with-Claude appetite, N for trust (write-access fear), and a weak C for "QuickBooks is replaceable by an LLM", which undercuts QuickBooks-dependent positioning | S-url + S-sum |
| E-10 | https://news.ycombinator.com/item?id=45110330 | unknown | Hacker News | founder of an AI bookkeeping app | S-sum: the founder says the team avoids letting the LLM invent numbers and uses the model as the interface, with figures "pulled from a structured database"; another commenter warned an error "could create serious liability" | 3, 7 | N | S-url + S-sum |
| E-11 | https://news.ycombinator.com/item?id=7515318 (older thread, "Ask HN: What accounting software do you use?") | around 2014 (I infer this from the old item number; unverified) | Hacker News | small-business commenters | S-sum: "most accounting software does little to predict cash flow, and small-business CFOs often rely on rough spreadsheets for scenario modeling" (this is the tool's wording of a commenter's point) | 4 | S (cash forecasting is spreadsheet-based), but very old | S-url + S-sum |
| E-12 | https://quickbooks.intuit.com/community/account-management-7/how-can-i-turn-off-ai-in-quickbooks-76453 | unknown | Intuit community | QuickBooks users | S-para: users ask for an off switch; one says turning off AI "is not an option" and was angry (not a marked quote) | 3 (Intuit Assist) | Weak C: shows AI-in-QuickBooks is unwelcome in some user bases, which could either hurt or help an outside product | S-url + S-para |
| E-13 | https://quickbooks.intuit.com/community/other-questions-9/how-do-i-permanently-opt-out-of-the-ai-assistant-idiocy-4698 | unknown | Intuit community | QuickBooks user (title wording is the poster's) | S-sum for related threads: "constantly gets things wrong so I don't trust anything it does"; "make enough mistakes and leave enough fields blank that they have to go over every bill manually". The search tool did not say which thread each came from. | 3, 7 (trust) | Weak C for any "AI explains your numbers" product: distrust of AI accuracy is stated by users of the incumbent's AI. Also supports the need for evidence-backed outputs. | S-url + S-sum |
| E-14 | https://quickbooks.intuit.com/learn-support/en-us/other-questions/ai-is-sending-out-payment-reminders-it-sounds-like-i-m/00/1555976 | unknown | Intuit support forum | small business owner | Title (a user's own words, as indexed): "AI is sending out payment reminders. It sounds like I'm reprimanding my customers. This is very embarrassing and there's no real help - Quickbooks keeps taking my money". Body not seen. | 4 (AR reminders) | N: shows built-in AR reminders exist and are disliked; does not show willingness to pay a third party | S-url (title is read from the result list) |
| E-15 | https://quickbooks.intuit.com/community/do-more-with-quickbooks-6/qbo-s-ai-implementation-284062 | unknown | Intuit community | unknown | Title only: "QBO's AI implementation". Search tool summary, not attributed to this thread: AI miscodes transactions, marks unpaid invoices paid, and one poster says they now spend "at least a day a month" verifying payments post to the correct client. | 3 | N | S-url; the summary was not tied to a specific thread |
| E-16 | https://quickbooks.intuit.com/community/account-management-65/why-does-this-whole-app-suck-now-162741 | unknown | Intuit community | QuickBooks user | Title only: "Why does this whole app suck now" | 3 | N | S-url only |
| E-17 | https://quickbooks.intuit.com/learn-support/en-us/accounting/allowing-third-party-access-to-your-company-file/00/609618 | unknown | Intuit support | Intuit-hosted help | S-para: Intuit's help page says third-party apps can reach sensitive company-file data (SSNs, employee data, bank account numbers) and suggests informing affected people before connecting an app. This is vendor documentation, not customer voice. | 7 | S for the trust barrier (as a stated friction), but not customer voice | S-url + S-para |
| E-18 | https://unofficialquickbooksaccountantspodcast.transistor.fm/104/transcript ("Insecurity about Security") | unknown | Podcast transcript, QuickBooks accountants | accountants | Title only. Not read. A real bookkeeper-voice source worth a follow-up. | 7 | N | S-url only |
| E-19 | https://community.xero.com/business/discussion/38473387 ("Reports overhaul for...") | unknown | Xero Community | bookkeeper or accountant | S-sum: "the new reports add nothing for bookkeepers" (summary-quoted; the same summary said Xero community threads in results were 10 to 13 years old, so this may be old) | 1 (Xero reports) | N | S-url + S-sum |
| E-20 | https://www.capterra.com/p/157101/CHASER/reviews/?page=2 (Chaser) | unknown | Capterra | Chaser customer | S-sum: "clients email me to respond and the email address is the chaser one which confuses them" (the only complaint a reviewer listed, per the summary) | 4 | S (an AR automation tool has paying users with minor complaints) | S-url + S-sum |
| E-21 | https://www.g2.com/discussions/what-are-the-best-tools-for-tracking-overdue-payments | unknown | G2 discussions | unknown | Title only. Not read. | 4 | N | S-url only |
| E-22 | https://www.distributionstrategy.com/report/the-state-of-distributor-profitability/ and https://www.mdm.com/article/research/economic-trends/distributors-pay-the-price-when-supply-chains-crack-whats-your-response/ | unknown | Trade publications | consultancies and trade press, **not customers** | S-sum: "91% of survey respondents said they fully pass supplier increases through to customers and add their margin on top"; Distribution Strategy names "override habits, cost pass-through timing, rounding effects, and SPA reconciliation cycles" as leak sources. Same claim Phase 2 already cited. | 5 | N (not customer voice; also not independent of consultancies who sell services) | S-url + S-sum |

Pricing items (vendor-published, not owner-reported). I list them so they are not mistaken for customer willingness to pay:

| ID | URL | Content | Class |
|---|---|---|---|
| P-01 | https://eightx.co/blog/fractional-cfo-for-ecommerce-brands (and siblings) | Eightx (a vendor selling these services) publishes $995 to $3,500/month for productized bookkeeping-led tiers and $3,000 to $15,000/month for operator-CFO work; one-off cleanup $5,000 to $25,000 fixed fee, typically 30 to 60 days; a free 30-minute "profit audit" call leads into a paid 14-day audit with no price shown. Eightx says only three of nine firms in its records publish a rate card. | N: shows a market exists for services; says nothing about owner demand for a software explanation |
| P-02 | Practical Ecommerce article, attributed to UpCounting's co-founder | $2,000 to $3,000/month bookkeeping, $5,000 to $8,000/month with fractional CFO. I only saw this as a search-tool summary. | N |

---

## 3. Thematic synthesis, by the eight requested themes

For each theme I state what the evidence is and how weak it is. I do not draw conclusions the data cannot carry.

### Theme 1. How owners discover and investigate margin drops

**What I have:** Titles of six or so Shopify Community threads (E-01 to E-06) that show merchants asking how to compute net profit per order and describing spreadsheets as the working tool. The search tool summarised the community conversation as a consistent pattern: Shopify's native "Profit by product" report covers only revenue and product cost, and merchants assemble payment fees, shipping labels, refunds, apps and ad spend in a spreadsheet or an app. It also said refund payment fees are not returned, and that historical margins are distorted when current costs are applied to old orders.

**What this suggests, with low confidence:** the investigation workflow is manual and spreadsheet-based, and the reasons given for margin discrepancies are structural data gaps (stale cost, missing fees, refund treatment), not a missing "AI". That is consistent with the Phase 2 data-feasibility finding that true margin needs cost data Shopify holds only as a current-value field.

**Caveat that matters:** the search tool itself warned that several of these threads were written by app vendors or contain AI-generated text, and that a founder was pitching a competing tool inside one. Some of the "merchant" voice here may be marketing seeded into the community. I cannot tell which from titles.

**What the evidence does not say:** no merchant, in anything I saw, says "I could not find why my margin fell". Titles show people asking how to *calculate* margin, which is a visibility problem, the problem existing $19 to $300/month apps address. This is not evidence of demand for an *explanation* layer on top.

### Theme 2. Complaints about profit apps (TrueProfit, Lifetimely, Triple Whale, Polar, BeProfit)

**What I have: almost nothing.** The Shopify App Store, Trustpilot and Capterra were all unreachable. One search returned vendor and affiliate comparison articles. The only independent-looking note was a third-party comparison listing TrueProfit's top plan at about $200/month, and a remark that Lifetimely is positioned around lifetime value rather than COGS audit. Both come from the search summary of vendor-adjacent pages. I do not count them as customer evidence.

**Status:** the review-theme analysis (COGS accuracy, shipping, refunds, ad spend, billing) requested in the brief **could not be performed.** It remains missing.

### Theme 3. Opinions on AI in the incumbent tools, and DIY with Claude or ChatGPT

This is the best-populated theme, but mostly from developers on Hacker News, not from owners or bookkeepers.

- **QuickBooks and Intuit Assist (E-12, E-13, E-15, E-16):** Intuit community thread titles and summaries show recurring requests to turn the AI off, and distrust of its accuracy. If the summary is accurate, users of the incumbent's AI say they must re-check its output. The implication runs two ways. It weakens any claim that "Intuit's AI will make a separate explainer unnecessary", because the incumbent's AI is distrusted. It also raises the bar for a third-party explainer: if users already assume AI output is wrong, an unsupported narrative will be dismissed. This points to the evidence-first design Phase 2 proposed, but it is my inference, not a customer statement.
- **Xero JAX:** I found no independent bookkeeper or accountant opinion of JAX. The search tool said results were Xero's own training pages and decade-old community posts. **Zero data on JAX sentiment.**
- **Shopify Sidekick:** my one query returned only Shopify Community results about profit tracking. No Sidekick opinions were retrieved. **Zero data.**
- **DIY with Claude or ChatGPT (E-07 to E-10):** Hacker News shows technical users building MCP servers and CLIs to put QuickBooks or their own ledgers behind Claude. The Claude for Small Business thread (E-09), per the summary, had one commenter who says they dropped QuickBooks after an AI-assisted setup passed a CPA's review, others who refuse to give an AI write access to payouts, and complaints that the official QuickBooks Online MCP server is "a mess". Two readings are both fair: (a) DIY substitution is real among technical owners, which is a *threat* to a paid explainer, since a capable owner can ask Claude directly; (b) the objections concentrate on write access and reliability, not on read-only analysis. I saw no post describing a DIY attempt at margin or cash *explanation* specifically, with results or limits. That is the most relevant missing item.

### Theme 4. Cash flow and late AR

**What I have:** Chaser's own blog content (vendor), a G2 discussion title (E-21, unread), one Capterra snippet with a mild complaint (E-20), and a QuickBooks forum title in which a small-business owner dislikes the tone of built-in AI payment reminders (E-14). The one old Hacker News snippet (E-11) says cash forecasting is spreadsheet-based. Vendor statistics, such as Chaser's claim that 87% of businesses were paid late and a Xero and PayPal figure that 48% of invoices are paid late, are published by interested parties and describe the pain, not purchasing.

**Interpretation:** existing paid AR tools have real users (supports the category being purchasable) but nothing here shows what they pay, what they cannot do, or whether they want an *explanation* of cash movement. Float, Fathom and Upflow returned no user-voice results. Phase 2 already rated this category crowded; nothing here changes that.

### Theme 5. Distributors and wholesalers

**Nothing from ERP or QuickBooks or NetSuite communities.** The search tool explicitly said it found no QuickBooks or NetSuite forum threads on cost pass-through. What came back were consultancies and trade press (Distribution Strategy Group, MDM, Zilliant, Vendavo, HVACR Trends, McKinsey), all of whom sell pricing services or software. The recurring claim is that margin leaks come from stale pricing agreements, rebates, overrides and handoffs between purchasing, pricing, sales and finance, and that pass-through lags. This is the same material Phase 2 used. No distributor owner or controller is heard in this session.

### Theme 6. Willingness to pay

**Zero owner or bookkeeper statements.** What I found are vendor rate cards (P-01, P-02): fractional CFO engagements of $995 to $15,000 a month and cleanups of $5,000 to $25,000. These establish that firms sell such services and that at least some are priced high, but vendors' listed prices are not evidence that anyone bought. Eightx's own note that only three of nine firms publish a rate card, and that prices online should be treated sceptically, is a caution I repeat. The "free 30-minute profit audit leading to a paid 14-day audit" is a funnel structure that resembles the Phase 2 proposed experiment; it is a vendor design and tells us nothing about conversion.

The pricing of the incumbent tools ($19 to about $200 or $300/month for profit apps) was already in Phase 2. I add nothing independent on it.

### Theme 7. Trust and data-sharing concerns

**Indirect only.** Intuit's own help page, Sage, Bitdefender and LiveFlow (a vendor) all describe third-party app access as a risk. The HN thread (E-09) shows commenters unwilling to give AI agents write access, and a commenter noting that some QBO MCP connections lack role-based access control. A QuickBooks accountants' podcast titled "Insecurity about Security" (E-18) exists and would be a good bookkeeper-voice source if the transcript can be read. No bookkeeper or owner said "I would not connect X to a startup". So trust is confirmed as a *discussed* risk, not quantified as a *deal-breaker*.

### Theme 8. Disconfirming evidence

I looked for posts saying existing tools suffice or nobody pays. **I found none directly.** The nearest items are indirect:
- Developers can wire Claude to QuickBooks themselves (E-07 to E-09), a substitution threat for technical owners.
- Intuit's AI is distrusted (E-12, E-13), which cuts against the idea that incumbents have solved the problem, but also against how easy it is to earn trust for any AI explainer.
- The recurring advice in Shopify threads is "build a spreadsheet", suggesting that for many owners the spreadsheet is judged good enough. This is my reading of titles and a summary, not a stated opinion.

The absence of disconfirming posts is **not** evidence that disconfirmation does not exist. I could not search the places such posts would be (Reddit especially).

---

## 4. How much real customer voice was obtainable, and what is missing

**Obtained:** roughly 22 confirmed thread or page URLs across Shopify Community, Intuit community, Hacker News, Xero Community, Capterra and G2, with, at best, summary-level text for about 8 of them. **Verbatim text I read on a page: none.**

**Why:** the sandbox resolves only a small allowlist of hosts. Reddit is blocked by policy and by the search tool. Every other community host failed to resolve. WebSearch summaries are generated, can blend threads, and (in this session) twice stated that they could not find what I asked for. I have not "quoted" any phrase beyond what the tool put in quotation marks, and every such phrase is marked S-sum above.

**Still missing, in order of importance for the investment decision:**
1. Any owner or bookkeeper stating they paid, or would pay, for a diagnosis or audit, with a price. Evidence count: 0.
2. Any account of DIY analysis of margin or cash with Claude or ChatGPT on exports: what worked and what failed. Count: 0 (only developers building plumbing).
3. App Store, Trustpilot, Capterra and G2 reviews of the profit apps and AR tools: themes and counts. Count: 0.
4. Any distributor-side voice from ERP communities, controllers, or pricing managers. Count: 0.
5. Reddit (r/shopify, r/ecommerce, r/Bookkeeping, r/QuickBooks, r/Accounting, r/smallbusiness). Entirely unreachable.
6. Bookkeeper voice on connecting a startup to client QuickBooks files. Podcast transcript E-18 is the best lead.

**Recommendation for the committee (about evidence, not about the product):** do not treat this appendix as customer validation. It leaves the Phase 2 position unchanged: the pain is plausibly public, willingness to pay for an explanation product is unobserved. Two paths close the gap. Either (a) widen the sandbox allowlist and rerun the mining against the hosts in section 1, plus a human-read pass on Reddit, or (b) rely on the Phase 2 paid-diagnostic experiment, which produces first-party payment data instead of second-hand forum text. Option (b) is the stronger evidence per hour spent.

---

## 5. Source register

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

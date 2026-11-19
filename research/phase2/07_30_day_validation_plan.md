# 07 — 30-Day Validation Plan

**Purpose:** decide between Margin Investigator (A), a different first module (B — most likely cash/AR), or stop — using money and behavior, not opinion. **No interviews have occurred. Nothing in this plan has been done. All thresholds are my judgment; no benchmark supports them.** Sample sizes are small: this plan can *falsify* a hypothesis; it cannot prove one.

## 1. Constraints this plan respects
Very limited capital; small team with strong backend engineering and no sales/finance-domain experience; no customers; preference for scalable B2B SaaS; preference for inbound. **Honest reality:** inbound alone cannot supply the first accountants, any distributor test, or willingness to pay $349+/month (Agent 4). Direct conversations are unavoidable and are scheduled below — the plan uses inbound where it works (problem-language resonance, file uploads, segment skew, accountant interest) and outreach where it must.

## 2. The offer: "Profit & Cash Leak Audit"
A paid, one-time, human-assisted audit for Shopify + QuickBooks (US) businesses with a wholesale channel (ICP-1), delivered from CSV exports or an invited read-only user — **no app, no integration build, no production code**.
- **Price test:** $500 / $1,000 / $1,500 tiers offered to different prospects; **payment taken before results are seen** (a free pilot proves nothing).
- **Deliverable:** one case-file report (`05` template) covering up to three finding types, using the same data: **(1)** margin bridge and supplier-cost-vs-price lag, **(2)** late-AR/cash-floor findings, **(3)** payout-to-ledger reconciliation breaks. The buyer chooses which finding to read first and which to act on — that choice is the data.
- **Method:** analysis by hand and throwaway spreadsheets/scripts; narrative drafted with off-the-shelf Claude from verified numbers; every number traced to rows; a "could not check" section in every report.
- **Stack choice:** QuickBooks first. Xero only after reading its developer terms (reported ban on AI/ML training with API data).

## 3. Who and where (find 15 qualified prospects)

| Track | Target | How to find them | Inbound or outreach |
|---|---|---|---|
| **T1 — Shopify brands with wholesale (10 conversations)** | $2–20M revenue, 5–40 staff, Shopify + QBO + wholesale channel | Free "file-in / leak-list-out" checker + landing page; helpful posts in Shopify Community, r/ecommerce, DTC operator Slack/Discord groups; accountants' referrals | Inbound for discovery; outreach for follow-up calls |
| **T2 — Accountants / fractional CFOs (10 approached, 3–5 pilots)** | Firms serving 10–50 product SMBs | ProAdvisor/Xero partner directories, LinkedIn communities, ecommerce-accountant niche groups; offer: "I will run the audit free for one of your clients" | **Outreach (unavoidable)** |
| **T3 — Distributors (5–8 interviews)** | $10–75M, mid-market ERP | NAW contacts, ERP-reseller introductions (NetSuite, Acumatica, Epicor, Odoo partners), trade-association events | **Outreach/referral (unavoidable)** |

Cash budget: domain, landing page, spreadsheet/analysis tooling, one Claude subscription ≈ **under $500** [ASSUMPTION]. Founder time ≈ **120–150 hours** [ASSUMPTION].

## 4. Week by week

**Week 1 — desk tasks and assets (do these first; they cost almost nothing).**
1. Pull Census SUSB size-class counts for NAICS 423/424/454/54; check keyword volumes for ~30 phrases across three intents (problem: "why did gross margin drop shopify"; method: "price volume mix analysis excel"; tool: "margin leakage software") with any keyword planner account.
2. Read the primary data-use clauses of Xero, Intuit and Shopify developer terms; read the full MDM/Baird-NAW 2Q26 article and DSG Q4 2026 survey (pass-through question).
3. Hand-run Reddit/HN searches (queries in `appendix/p2_a1` and Phase 1 `agent2_market.md` §7); capture permalinks and verbatim text for 15–20 threads. **Quote only what you read.**
4. Hands-on 1-hour trials of NetSuite Ask Oracle (if a sandbox is available), Polar, Lifetimely, Hypersonix, and a Claude/QuickBooks prompt on the same sample data.
5. Build the landing page and the free checker spec; write the audit report template; set up the tracking sheet (§5).

**Week 2 — recruit.** Launch the checker and community posts; send direct outreach to ~10 accountants/fractional CFOs and request 5–8 distributor conversations via ERP resellers/NAW; book the first audits. Target by end of week: ≥15 qualified conversations booked or completed.

**Week 3 — deliver and charge.** Run audits for paying customers; time every hour; collect exports; deliver reports; run a **blind comparison** with each customer: show the case file next to the output of their own in-product AI (Intuit Assist, Shopify Sidekick, or a Claude/QBO prompt) without labels.

**Week 4 — measure and decide.** Follow up on actions taken; ask for outcome; ask whether they'd pay monthly and at what price; apply the decision rules (§7). Write a one-page result memo, including everything that went wrong.

## 5. Evidence to collect (one row per prospect — do not infer, record)
Source (inbound/outreach/referral) · stack · revenue band · role of the person speaking · who would approve $500 / $400 per month · what they use now and why it fails · access granted (yes/no, what, how long) · data-cleaning hours · cost-coverage % · finding types delivered · dollars identified · which finding they valued first · which they acted on · action taken within 7 days · paid? (amount/date) · would pay monthly (price) · blind-comparison preference · owner-confirmed cause correct (yes/partial/no) · objections (verbatim).

## 6. Metrics

| Metric | Definition |
|---|---|
| Conversion to paid | paying customers ÷ qualified prospects (qualified = right stack, revenue band, decision-maker on call) |
| Price signal | accepted tier; refusals and stated reasons |
| Data access | share granting access without heavy review |
| Onboarding hours | median human hours per audit |
| Explanation accuracy | owner-confirmed top explanation correct, across all findings |
| Blind preference | share preferring the case file over their in-product AI |
| Finding pull | which finding type each buyer opens first, values most, acts on |
| Action rate | audits followed by a logged action within 7 days |
| Inbound signal | file uploads, landing-page conversion, accountant replies |

## 7. Success, failure and decision rules (pre-registered — write them down before starting)

**Success for the experiment (justifies building an MVP):** all of
1. ≥ **4 of 15** qualified prospects pay ≥ $500 before seeing results (Agent 1 criterion), **and** ≥ 2 say they would pay monthly at ≥ $199;
2. median **onboarding ≤ 8 hours** by the 5th audit (≤ 6 hours of cleaning per customer is Agent 1's bar), and ≥ 60% of customers have usable cost history for margin work;
3. top explanation correct ≥ ~70% on owner-confirmed cases (small n; also report abstentions);
4. blind comparison: a clear majority prefer the case file over their in-product AI;
5. ≥ 1 customer can name a dollar outcome or action taken.

**Decision rules**
- **→ A (Margin Investigator):** conditions 1–3 met **and** margin findings are the most-valued/most-acted-on in ≥ half of paying customers.
- **→ B (different first module):** conditions 1–3 met **but** pull concentrates elsewhere (e.g., ≥ 60% of payers act first on cash/AR or reconciliation) — then run the same design for that module with price at ≥ $199 and lower onboarding.
- **→ Distributor track:** if T1 stalls on price but ≥ 3 of 5–8 distributor conversations show unprompted dollar pain **and** a clear budget owner, pivot ICP and repeat as an interview-led paid diagnostic.
- **→ Stop or re-pick (C stays):** see failure.

**Failure (any one):**
- **fewer than 2 of 15** qualified prospects pay;
- owners rate the case file no better than their in-product/Claude output;
- median onboarding > ~12 hours or cost coverage < ~40% for most customers (the product is a data-cleaning service);
- explanation accuracy < ~60%;
- nobody grants read access/exports without a heavy security review;
- 5 of the first 10 conversations say free in-product tools are sufficient (stop early).

**Inconclusive zone:** 2–3 of 15 pay → extend 2 weeks with a different channel (accountant referrals) before deciding; do not lower price to manufacture a pass.

## 8. What this plan will not tell you
- Whether SEO or marketplace listing will work as a channel (months, not days).
- Retention or churn; renewals; true monthly willingness to pay beyond stated intent.
- Whether a product can match the analyst's judgment (blind-comparison and accuracy tests are proxies).
- Distributor demand from an inbound funnel (structurally biased to ICP-1).
- Accountant resale economics (needs a billing cycle).

## 9. Ethical and practical guardrails
Do not claim interviews or results that have not happened; do not scrape or spam communities; disclose that the audit is a paid pilot; handle customer data under a written data-handling note; delete data on request; no production credentials stored outside a vault; no action taken on a customer's behalf.

## 10. What justifies building the MVP
Success conditions 1–5 plus a named ICP and first stack; then start the 8–12-week plan in `05`/Phase 1 Deliverable 10 for the winning module only. If success is partial, the next step is a second 30-day cycle on the revised hypothesis, not a build.

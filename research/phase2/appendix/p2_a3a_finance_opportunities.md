# Phase 2, Agent 3A: Finance-Side Opportunity Comparison

**Date:** 2026-11-19. **Scope:** six assigned finance opportunities plus three discovered ones (F7 to F9). Not repeating the Phase 1 report or `agent2_market.md`.

## 0. Evidence quality, read first

- **WebFetch failed on every host tried** (`www.apexanalytix.com`, `www.withorb.com`, `help.linkmybooks.com`: ENOTFOUND, not on the session allowlist). Everything below comes from **WebSearch result summaries**. No primary page was read in full. Figures are "as summarized by search", and the register marks that.
- **No Reddit or Hacker News thread was retrieved.** Searches with `site:reddit.com` and `site:news.ycombinator.com` returned vendor help pages, Intuit Community, Indie Hackers, YC and DEV posts. I could not quote r/accounting, r/bookkeeping, r/FPandA or r/Netsuite. **I quote no practitioner text as verbatim**, except short fragments printed inside search summaries, which I flag "snippet, unverified verbatim". Customer evidence is therefore thin and mostly vendor-authored. Treat the whole file as desk research that still needs the Reddit/HN pass by hand.
- Tags: **[EVIDENCE-BASED]** means a sourced fact supports the score. **[JUDGMENT]** means my inference. Source IDs (A3A-xx) point to the register at the end.
- Pricing figures conflict between aggregators. Quote them as ranges, not as list prices.

## 1. Cross-cutting findings

1. **Almost every finance pain here already has a priced product**, so "open" competition is rare. The open space is **cross-system explanation and evidence**, not detection or syncing.
2. **System-of-record vendors are moving in.** Intuit says its Accounting AI can "help identify possible reconciliation issues and explain potential resolutions" on QuickBooks Online Plus and Advanced (A3A-29, Nov 2026 trade summary). Xero put Syft-powered analytics into every plan at no extra cost by Jan 2026 and launched auto bank reconciliation in beta Nov 2025 (A3A-31). First-order "what's wrong inside one ledger" is being given away.
3. **Dollar-denominated outcomes have contingency precedent.** Recovery audits (13.5% to 25% quoted), chargeback recovery (25%), failed-payment recovery (about 10% to 30%, anecdotal). This is the strongest willingness-to-pay pattern found, and it lets a no-brand founder charge only when value is shown.
4. **Contradiction:** a founder post titled "3 months building Stripe fee auditor, 0 revenue, 5 clicks, 2 real users" appears in search (A3A-38; title only, body not read). Detection of small leaks may be easy to build and hard to sell. Indie Hackers also holds many founder posts offering free Stripe audits; these double as lead-gen (A3A-37).
5. **Accuracy asymmetry:** reconciliation and AP must be cent-accurate. Churn, collections prioritization and variance commentary tolerate being directionally right if evidence is shown.

---

## 2. Profiles

### F1. Cash-flow and working-capital investigation (late AR, DSO drift, payables timing, 13-week variance)

- **Severity:** High (cash kills firms). **Frequency:** continuous; weekly review for tight firms.
- **Financial impact:** Xero platform data (from Phase 1): about 29.3 days to get paid, about 9 days late. Gateway's lender-sponsored survey (n=503): 64% have invoices 90+ days overdue, averaging 11% of annual revenue (A3A-33, secondary, sponsor bias). Intuit 2026 report via business.com: 59% of small businesses have invoices 30+ days overdue, average $17,700 outstanding (A3A-32, secondary).
- **Alternatives and prices:** Float (13-week specialist; sources give about $50 to £79/month, A3A-23), Pulse ($29), Fathom (about $59 to $860/month by tier), Jirav ($50 to $150), Agicap (quote only). All via aggregators, conflicting.
- **Competitive intensity:** High and cheap. QuickBooks has a 90-day cash dashboard. Xero's JAX answers cash-position questions (demo, A3A-31).
- **Data accessibility:** Accounting API (QBO/Xero), bank feeds (Plaid/open banking), AR/AP ledgers. Good.
- **Integration complexity:** Low-medium. **Time to build:** 6 to 10 weeks for a read-only MVP [JUDGMENT].
- **Accuracy requirement:** Forecast accuracy is inherently soft. Trust breaks if a flagged "payment will be late" proves wrong repeatedly [JUDGMENT]. I found **no independent forecast-accuracy data** for any tool.
- **Buyer:** Owner or fractional CFO. Budget is tiny ($30 to $300/month).
- **Willingness to pay:** Real but price-capped by the tools above. Only vendor-authored sources.
- **Recurring usage:** Weekly. **Expansion:** Strong (the cash layer connects to every other module).
- **Dollar-measurable:** Partly (days saved, late fees avoided), not attributable to the tool.
- **Verdict:** Easy to enter, hard to charge above $100/month for a forecast alone.

### F2. Revenue leakage detection (unbilled usage, missed invoices, credit leakage, contract-vs-billed, failed payments, billing errors)

- **Severity:** High where it exists. **Frequency:** every billing run, but incidence varies widely.
- **Financial impact (all vendor or secondary):** MGI Research, cited by Lago: 1% to 5% of revenue (A3A-02). Fintel Analytics, cited by Orb: 4% to 9% for usage-based versus 2% to 4% flat-rate (A3A-01). Chargebee's own blog: average 9% (A3A-03). Chargebee labels its 9.7% MRR and 13% unbilled-usage numbers a directional model. **The spread, 1% to 9%, shows no solid primary number.**
- **Alternatives:** Billing platforms with built-in leakage reports (Chargebee, Maxio, Zenskar, Orb, Lago). JustPaid (YC) checks vendor bills against contract pricing (A3A-39). Stripe Smart Retries for payment failures (F5).
- **Competitive intensity:** Medium to high on detection, **low on contract-vs-invoice-vs-usage auditing across systems**, which billing vendors cannot do for their own data.
- **Data accessibility:** Needs billing system plus usage plus CRM/contracts. Contracts are usually PDFs, which is hard.
- **Integration complexity:** High for contract-vs-billed; low for Stripe-only checks. **Time to build:** 3 months for contract extraction with human review [JUDGMENT].
- **Accuracy requirement:** Low tolerance. A false "you under-billed Acme by $4,000" that is wrong destroys trust fast [JUDGMENT]. Show source rows and contract clause.
- **Buyer:** CFO or RevOps at a $3M to $50M ARR SaaS. Budget: RevOps or finance tooling.
- **Willingness to pay:** No named customer found. Contingency is plausible (cf. F4, F5), unproven for this category.
- **Recurring usage:** Every billing cycle. **Expansion:** High (contract and pricing data feed margin and churn modules).
- **Dollar-measurable:** Yes, directly, and this is the best feature of the category.
- **Contradictory evidence:** Indie Hackers founder-audit posts report most bugs are webhook handling, a one-time fix rather than a subscription (A3A-37, snippet).

### F3. Reconciliation and unexplained discrepancies (Shopify/Stripe/PayPal vs bank vs ledger; marketplaces; intercompany)

- **Severity:** High for bookkeepers, medium for owners. **Frequency:** daily to monthly. Highest frequency of all candidates.
- **Impact:** Mostly time and misstated margin. Eightx guidance, as summarized, says a naive QuickBooks setup books the payout lump as revenue "and your margins lie to you" (A3A-35, snippet). Velosio vendor survey (Phase 1): 68% of 151 mid-market ERP users lose 11+ hours per week to manual reconciliation.
- **Alternatives and prices:** A2X from $29/month per channel (Multi plans about $89 for 1,000 orders and $169 for 5,000, A3A-06, A3A-07). Link My Books about $17 to $21 entry, $60 for 5,000 orders, $136 for 15,000, with a price change effective 2026-07-01 (A3A-04, A3A-05, A3A-08). Synder, Webgility, Quipli, SaasAnt, Amaka also appear (A3A-34).
- **Competitive intensity:** Very high and mature for Shopify/Amazon sync. A2X has an accuracy case study (ecombalance, A3A-35). A CFO review says A2X pays off above roughly $500K GMV (A3A-35, secondary).
- **Gaps:** A Link My Books post (vendor, Aug 2026) describes a TikTok Shop case where A2X via Shopify missed fees and misrecorded platform-funded discounts (A3A-36). The same summary says gift cards and partial refunds need accountant support. Residual **unexplained differences** remain a manual accountant task.
- **Data accessibility:** Payments/marketplace APIs and accounting APIs are good. **Integration:** medium (many edge cases). **Time:** 3 to 4 months to cover Shopify+Stripe+PayPal+QBO/Xero well [JUDGMENT].
- **Accuracy requirement:** The strictest. Ledger entries must tie to the cent. Investigation-only (no posting) lowers the bar.
- **Buyer:** Bookkeeper or accounting firm (reachable through communities), then owner. Budget $30 to $200/month per client.
- **Willingness to pay:** **Strongest observable** (priced, adopted, many reviews), but for sync. Willingness to pay for "explain this $312 difference" is unproven.
- **Recurring:** Daily. **Expansion:** Medium (feeds margin and cash).
- **Dollar-measurable:** Mostly hours, not dollars.

### F4. Accounts-payable errors (duplicates, invoice vs PO mismatch, price variance, recovery audit)

- **Severity:** Medium. **Frequency:** every payment run, but rare per run.
- **Impact:** APQC 2024 as cited by Corpay: top performers about 0.8% of annual disbursements go out as duplicate or erroneous payments, median 1.5%, worst 2.0% (A3A-12). SAP Concur via Klippa: 1.29% average (A3A-13). Definitions mix duplicates and errors. Apex Analytix publishes a 2026 overpayment report; I could not open it (A3A-11).
- **Alternatives:** Recovery-audit firms (PRGX, Apex Analytix, Auditec, Purchase Control) on **contingency**. A 2006 Virginia state report shows bid fees from 13.5% (A3A-10, old). A vendor illustration assumes 25% (A3A-09). AP automation platforms (Medius, Tipalti, Bill, Ramp) likely include duplicate checks; I did not verify.
- **Competitive intensity:** Entrenched at enterprise. Corpay notes ERP duplicate detection is exact-match on vendor+invoice number+amount, so one changed character slips through (A3A-12). Fuzzy matching is a real technical gap.
- **Data accessibility:** Needs AP ledger, POs, receipts, vendor master. In SMBs, POs often do not exist. **Integration:** medium-high. **Time:** 3 to 4 months [JUDGMENT].
- **Accuracy requirement:** High. Asking a vendor for a refund on a false positive burns relationships.
- **Buyer:** Controller or AP manager at $50M+ spend firms; budget is contingency-funded.
- **Willingness to pay:** Strong precedent for contingency (13.5% to 25%), only for firms with enough AP volume.
- **Recurring:** Weak. Recovery audits are periodic, and the prize decays after the first sweep. **Expansion:** Medium (vendor price data supports procurement and margin).
- **Dollar-measurable:** Yes, cleanly. **Fit with the founder:** poor for tiny SMBs (low volume), better for mid-market, which conflicts with the "inbound, no capital" preference.

### F5. Customer churn and revenue-risk investigation (B2B SaaS, subscription ecommerce)

- **Severity:** Very high (valuation and growth driver). **Frequency:** continuous.
- **Impact:** SaaS Capital survey (>1,000 private B2B firms): median gross revenue retention 91%, about 90% to 91% for ACV up to $250K, 95% above (A3A-28). Recurly 2025 report via a search summary: median annual B2B churn 3.5%, of which involuntary 0.8%. Involuntary is commonly quoted as 20% to 40% of churn, with Baremetrics' 2026 figure of about 9% of MRR lost to failed payments (vendor, secondhand, Phase 1 and A3A-18).
- **Alternatives and prices:** ChartMogul (free under $10K MRR, about $119 to $179/month at $50K to $200K MRR, conflicting, A3A-24). Baremetrics ($75 to $255/month; Recover add-on $69+; Cancellation Insights $129). ProfitWell Metrics free. Churnkey from about $250/month. Paddle Retain: flat from $500/month for smaller firms, or performance-based (competitor lists 10% to 15%, unconfirmed, A3A-19). Stripe Smart Retries: Stripe says average 55% of failed payments recovered, "$9 per $1" on Billing (snippet via A3A-17); VEED case: $1.8M recovered in a year (A3A-16, primary customer story). FlyCode argues gross recovery rates mostly measure what Stripe would recover anyway (A3A-15, competitor).
- **Competitive intensity:** Very high on involuntary churn and cancel flows. **Open:** causal investigation of voluntary B2B churn (which accounts, why, what changed, what evidence). CS platforms (Vitally, Planhat, Gainsight) target larger teams; I found no pricing.
- **Data accessibility:** Billing (Stripe/Chargebee), CRM, product usage, support tickets. Usage and support data vary by company.
- **Integration:** medium. **Time:** 2 to 3 months for billing-only; 4+ with product usage [JUDGMENT].
- **Accuracy requirement:** Tolerant (risk scores are probabilistic) if the evidence behind each flag is shown.
- **Buyer:** Founder, CS lead or RevOps at $1M to $30M ARR SaaS. Budget $100 to $1,000/month.
- **Willingness to pay:** Strong for the payment-recovery slice (named prices, a $600K Retool and $1.8M VEED recovery claim). Weak for "insights only" (ChartMogul and ProfitWell are cheap or free).
- **Recurring:** Weekly and monthly. **Expansion:** Very high (churn ties to product, support, pricing, margin).
- **Dollar-measurable:** Yes (MRR saved), with attribution disputes.

### F6. Month-end variance and close explanation (budget vs actual commentary)

- **Severity:** Medium (time, not loss). **Frequency:** monthly, universal.
- **Impact:** Time only. Search-summarized vendor content puts the commentary step at "1 to 3 days" depending on the month (A3A-40, vendor). No credible dollar figure.
- **Alternatives:** Numeric (entry about $30/user/month per one aggregator; mid-market about $8K to $35K/year per a pro-Numeric blog, A3A-25), FloQast (quote only), Aleph, ChatFin, Pigment, Excel Copilot, ChatGPT with a spreadsheet. Numeric and FloQast both advertise drafted flux explanations.
- **Competitive intensity:** High and funded.
- **Data accessibility:** GL and budget from QBO/NetSuite/Excel. Budget data is frequently an Excel file with no API. **Integration:** medium. **Time:** 6 to 8 weeks for a draft-commentary product [JUDGMENT].
- **Accuracy requirement:** High on numbers (computed deterministically), medium on prose. Sources warn the risk is "an explanation no one can trace back to the ledger" (summary wording, A3A-40, snippet).
- **Buyer:** Controller or FP&A lead. Budget: finance tooling, mid-market $8K+/year.
- **Willingness to pay:** Real in mid-market. Weak at the SMB owner level, where nobody writes commentary.
- **Recurring:** Monthly. **Expansion:** High (it is the natural home of "why did X move").
- **Dollar-measurable:** Hours only. Phase 1 already noted it works better as a feature than a wedge; evidence here agrees.

### F7 (new). AR collections prioritization and payment-behaviour prediction

- **Severity:** High. **Frequency:** weekly.
- **Impact:** same AR data as F1. Chaser argues forecasts built on due dates mislead because customers rarely pay on the due date; forecast from each customer's actual payment history (A3A-32, vendor).
- **Alternatives:** Chaser (Capterra lists Compact at $259/month flat; another source £199, A3A-21), BILL AR ($49 to $89/user/month), Upflow (no published price, A3A-22), Tesorio (quote-based, mid-market), HighRadius (enterprise), QuickBooks/Xero reminders (Xero added payment follow-ups, A3A-31).
- **Competitive intensity:** High. **Data:** invoice/payment history, easy. **Integration:** low. **Time:** 4 to 6 weeks [JUDGMENT].
- **Accuracy:** Moderate; a ranked list is useful even if imperfect.
- **Buyer:** Owner or AR clerk. $50 to $300/month.
- **Willingness to pay:** Demonstrated by Chaser and Upflow existing at $259+/month.
- **Recurring:** Weekly. **Expansion:** Good (feeds F1 forecasting and F5 churn risk).
- **Dollar-measurable:** Yes (days to collect, cash accelerated).

### F8 (new). SaaS and vendor spend leakage

- **Severity:** Medium. **Frequency:** monthly/renewal driven.
- **Impact:** Zylo 2025 Index: average $21M annual unused-license waste, up 14.2% year over year (A3A-26); Zylo's 2026 data via search: 46% unused licenses and about $19.8M waste (vendor, enterprise-skewed). Vendr: average savings of 14.2% in proactive renewal reviews, unverified (A3A-26). Applicability to small firms is unproven.
- **Alternatives:** Zylo, Vendr, Tropic (enterprise, quote-only; fee percentages not found), card-spend tools. **Open:** sub-$10M firms. **Data:** card/bank feeds, SSO logs, hard. **Accuracy:** tolerant. **Buyer:** finance or IT. **WTP:** enterprise only evidenced. **Expansion:** low. **Dollar-measurable:** yes.

### F9 (new). Sales-tax nexus and anomaly detection

- **Severity:** High exposure (liability) but I found **no penalty or incidence data**; severity is inferred.
- **Alternatives:** Stripe Tax (0.5% of transactions where registered, or $0.50 per API transaction; does not file in most places, A3A-41), TaxJar from $19/month, Anrok (SaaS, startup tier), Avalara ($5K to $70K+/year, per one comparison), Zamp, TaxCloud. Saturated.
- **Data:** easy. **Accuracy:** very low tolerance, a legal liability. **Buyer:** owner or accountant. **WTP:** proven but for compliance, not investigation. **Expansion:** low. **Verdict:** do not enter; regulated accuracy and saturated.
- **Payroll/overtime anomalies:** not researched in this pass; no evidence collected.

---

## 3. Scoring matrix (1 to 5; 5 = best for the founder; competition 5 = open; accuracy 5 = forgiving)

| Opportunity | Sev | Freq | $ | Data | Integ | WTP | Open | TTV | Acc | Recur | Expand | Total /55 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 Cash/working capital | 4 | 5 | 3 | 4 | 4 | 3 | 2 | 3 | 3 | 4 | 4 | 39 |
| F2 Revenue leakage | 4 | 3 | 4 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 4 | 34 |
| F3 Reconciliation | 4 | 5 | 3 | 4 | 3 | 4 | 2 | 4 | 1 | 5 | 3 | 38 |
| F4 AP errors | 3 | 3 | 4 | 2 | 2 | 4 | 2 | 3 | 2 | 2 | 3 | 30 |
| F5 Churn/revenue risk | 5 | 5 | 4 | 3 | 3 | 3 | 2 | 3 | 4 | 4 | 5 | 41 |
| F6 Close variance | 3 | 5 | 2 | 4 | 3 | 3 | 2 | 4 | 2 | 5 | 4 | 37 |
| F7 AR collections priority | 4 | 5 | 4 | 4 | 4 | 4 | 2 | 4 | 4 | 5 | 4 | 44 |
| F8 SaaS spend leakage | 3 | 4 | 3 | 3 | 3 | 3 | 2 | 3 | 4 | 3 | 2 | 33 |
| F9 Sales tax | 4 | 2 | 3 | 4 | 4 | 4 | 1 | 3 | 1 | 3 | 2 | 31 |

Totals are unweighted. They rank ease and fit, not a business case; a high-total, saturated category (F7) is not necessarily a good wedge.

### Justifications (EB = [EVIDENCE-BASED], J = [JUDGMENT])

**F1 Cash.** Sev 4: cash failure fatal, late-payment data A3A-33 [EB]. Freq 5: weekly review [J]. $ 3: delays are measured, savings not attributable [J]. Data 4: QBO/Xero/bank APIs [J]. Integ 4: read-only [J]. WTP 3: tools priced $29 to $860 but price-capped [EB]. Open 2: Float, Fathom, Pulse, native dashboards [EB]. TTV 3: needs 2+ months of history to trust a forecast [J]. Acc 3: forecast soft, no accuracy benchmark found [J]. Recur 4: weekly [J]. Expand 4: cash layer links everything [J].

**F2 Leakage.** Sev 4 [J]. Freq 3: per billing run, incidence uneven [J]. $ 4: 1% to 9% of revenue claimed, all vendor [EB, weak]. Data 3: contracts are PDFs [J]. Integ 2 [J]. WTP 3: no named buyer; contingency plausible [J]. Open 3: billing vendors cover own data only [EB]. TTV 3 [J]. Acc 2: false under-billing claims hurt trust [J]. Recur 3 [J]. Expand 4: contract data supports margin/churn [J].

**F3 Reconciliation.** Sev 4 [J]. Freq 5: daily [EB]. $ 3: time and misstated margin [J]. Data 4: APIs good [EB]. Integ 3: many edge cases (gift cards, partial refunds) [EB]. WTP 4: A2X/LMB priced and adopted [EB]. Open 2: A2X, LMB, Synder, Webgility [EB]. TTV 4: value visible on first import [J]. Acc 1: must tie to the cent [J]. Recur 5 [J]. Expand 3 [J].

**F4 AP.** Sev 3 [J]. Freq 3 [J]. $ 4: 0.8% to 2.0% of disbursements, APQC via Corpay [EB]. Data 2: PO/receipt data rare in SMB [J]. Integ 2 [J]. WTP 4: contingency 13.5% to 25% [EB]. Open 2: PRGX/Apex entrenched [EB]. TTV 3 [J]. Acc 2: wrong refund requests hurt vendor ties [J]. Recur 2: audits are periodic [J]. Expand 3 [J].

**F5 Churn.** Sev 5: retention drives SaaS value [J]. Freq 5 [J]. $ 4: GRR 91% median, 9% MRR lost to failed payments claimed [EB]. Data 3: billing easy, usage varies [J]. Integ 3 [J]. WTP 3: recovery tools priced $250+/month, insights tools cheap [EB]. Open 2: payment recovery crowded; causal voluntary-churn explanation open [EB/J]. TTV 3 [J]. Acc 4: probabilistic flags acceptable with evidence [J]. Recur 4 [J]. Expand 5 [J].

**F6 Close.** Sev 3 [J]. Freq 5: monthly, universal [J]. $ 2: hours only [EB]. Data 4 [J]. Integ 3: budgets in Excel [J]. WTP 3: Numeric/FloQast mid-market only [EB]. Open 2 [EB]. TTV 4: first month shows output [J]. Acc 2: numbers must trace to GL [EB, vendor commentary]. Recur 5 [J]. Expand 4 [J].

**F7 AR priority.** Sev 4 [J]. Freq 5 [J]. $ 4: cash accelerated, measurable [J]. Data 4: invoice history [J]. Integ 4 [J]. WTP 4: Chaser $259/month flat per Capterra [EB]. Open 2: Chaser, Upflow, BILL, QBO/Xero reminders [EB]. TTV 4 [J]. Acc 4: ranking tolerates error [J]. Recur 5 [J]. Expand 4 [J].

**F8 SaaS spend.** Sev 3 [J]. Freq 4 [J]. $ 3: Zylo waste figures enterprise-only [EB]. Data 3 [J]. Integ 3 [J]. WTP 3: enterprise evidence only [EB]. Open 2: Zylo/Vendr/Tropic [EB]. TTV 3 [J]. Acc 4 [J]. Recur 3 [J]. Expand 2 [J].

**F9 Sales tax.** Sev 4: legal liability, no incidence data [J]. Freq 2 [J]. $ 3 [J]. Data 4 [J]. Integ 4 [J]. WTP 4: TaxJar $19/month, Stripe Tax 0.5% [EB]. Open 1: saturated [EB]. TTV 3 [J]. Acc 1 [J]. Recur 3 [J]. Expand 2 [J].

## 4. Reading across the finance side

- **Best fit for the founder's constraints [JUDGMENT]:** F5 (revenue-risk and churn investigation, billing-first) and F7 (AR prioritization) score highest on recurrence, accuracy tolerance and expansion. F2 (leakage) has the best dollar measurability but the weakest integration ease. F3 is the most validated willingness to pay, but the accuracy bar and crowded field cut against a lean team.
- **Unproven everywhere:** willingness to pay for *explanation* (versus detection, syncing or recovery). Every priced comparable sells a **detect-and-act** or **sync** product.
- **Measurability test:** F2, F4, F5 (payment recovery) and F7 give dollar outcomes that can anchor contingency pricing. F3 and F6 deliver hours.
- **Before any build:** run the Reddit/HN pass that this session could not do, and open the vendor primary pages (Apex, Orb, Link My Books, Chaser, Paddle) after the allowlist is widened.

---

## SOURCE REGISTER

Dates are the date shown in search results or inferred from the URL; "n/d" means not shown. All were seen via WebSearch summaries, not fetched.

| ID | URL | Source date | Source type | Claims supported | Reliability note |
|---|---|---|---|---|---|
| A3A-01 | https://www.withorb.com/blog/revenue-leakage-statistics | n/d | Vendor blog (billing) | Fintel Analytics 4% to 9% vs 2% to 4% leakage | Vendor, original report not opened |
| A3A-02 | https://getlago.com/blog/revenue-leakage-saas-billing | n/d | Vendor blog | MGI Research 1% to 5% | Vendor, secondary |
| A3A-03 | https://chargebee.com/blog/revenue-leakage/ | n/d | Vendor blog | 9% average leakage; 9.7%/13% directional model | Vendor incentive to inflate |
| A3A-04 | https://linkmybooks.com/blog/a2x-pricing | 2025-12-24 | Competitor blog | A2X vs Link My Books pricing | Competitor marketing |
| A3A-05 | https://www.capterra.com/p/184768/Link-My-Books/pricing/ | 2026 | Review site | LMB $21/$60/$136 plans | Aggregator, conflicts with $17 elsewhere |
| A3A-06 | https://taxomate.com/a2x-vs-link-my-books-vs-taxomate | n/d | Competitor comparison | A2X Multi $89/$169 | Competitor |
| A3A-07 | https://saasrat.com/products/a2x-for-amazon-accounting | n/d | Aggregator | A2X from $29 per channel | Aggregator |
| A3A-08 | https://help.linkmybooks.com/en/articles/11093698-2026-price-changes | 2026 | Vendor help | LMB price change effective 2026-07-01 | Vendor, page not fetched |
| A3A-09 | https://www.apexanalytix.com/resources/blog/recovery-audit-cost/ | n/d | Vendor blog | Contingency model, 25% worked example | Vendor illustration |
| A3A-10 | https://rga.lis.virginia.gov/Published/2006/RD385/PDF | 2006 | Government report | Contingency bids from 13.5% | Primary but 20 years old |
| A3A-11 | https://www.apexanalytix.com/resources/blog/apexanalytix-2026-global-overpayment-report/ | 2026 | Vendor report | Existence of 2026 overpayment report | Not opened, no figures used |
| A3A-12 | https://www.corpay.com/en-NZ/resources/blog/duplicate-payment | n/d | Vendor blog | APQC 2024 0.8%/1.5%/2.0%; exact-match detection weakness | Vendor, APQC original not seen |
| A3A-13 | https://www.klippa.com/en/blog/information/duplicate-payment-prevention/ | n/d | Vendor blog | SAP Concur 1.29% duplication rate | Vendor, secondary |
| A3A-15 | https://www.flycode.com/blog/stripe-failed-payment-recovery-benchmark | n/d | Competitor benchmark | Gross recovery vs counterfactual critique | Competitor |
| A3A-16 | https://stripe.com/en-lu/customers/veed | n/d | Vendor case study | VEED recovered $1.8M in a year via Smart Retries | Primary vendor claim |
| A3A-17 | https://www.reduxpayments.com/blog/stripe-smart-retries-explained | n/d | Competitor blog | Stripe 55% average recovery; "$9 per $1" | Competitor relays Stripe claims |
| A3A-18 | https://churnkey.co/guides/reduce-involuntary-churn | n/d | Vendor guide | Churnkey pricing/claims; involuntary 20% to 40% | Vendor |
| A3A-19 | https://paddle.com/help/profitwell-metrics/retain/get-started/how-much-does-retain-cost | n/d | Vendor help | Retain performance-based or flat from $500/month | Vendor; 10% to 15% not confirmed |
| A3A-20 | https://redo.com/resources/articles/comparisons/chargeflow-pricing | n/d | Third-party review | Chargeflow 25% of recovered chargebacks | Third party |
| A3A-21 | https://www.capterra.com/p/157101/CHASER/pricing/ | 2026 | Review site | Chaser Compact $259/month | Aggregator, conflicts with £199 |
| A3A-22 | https://www.vendr.com/marketplace/upflow | n/d | Marketplace | Upflow no list price | Aggregator |
| A3A-23 | https://www.floatapp.com/blog/cash-flow-forecasting-software-cost | n/d | Vendor blog | Float/Fathom/Pulse/Jirav price ranges | Vendor and affiliate mix |
| A3A-24 | https://toolradar.com/tools/chartmogul/pricing | 2026 | Aggregator | ChartMogul, Baremetrics tiers | Conflicting aggregators |
| A3A-25 | https://kynledger.pages.dev/tools/ai-month-end-close-tools-cpa-2026 | 2026 | Blog | Numeric $8K to $35K/yr estimate | Single pro-Numeric source |
| A3A-26 | https://zylo.com/news/2025-saas-management-index | 2025-01-16 | Vendor report | $21M unused-license waste; Vendr 14.2% savings (unverified) | Vendor, enterprise |
| A3A-28 | https://www.saas-capital.com/research/saas-retention-benchmarks-for-private-b2b-companies/ | 2025 | Investor survey | Median GRR 91%, by ACV | Most methodical retention source here |
| A3A-29 | https://cpapracticeadvisor.com/2026/11/06/overview-of-intuit-ai-in-quickbooks-online-2026/193399 | 2026-11-06 | Trade press | QBO Accounting AI reconciliation help | Trade summary, tier details vary |
| A3A-30 | https://www.businesswire.com/news/home/20251028595899/en/ | 2025-10-28 | Press release | Intuit Intelligence announcement | Primary, promotional |
| A3A-31 | https://www.cpapracticeadvisor.com/2025/10/07/xero-adds-new-features-to-ai-financial-superagent-jax/170382/ | 2025-10-07 | Trade press | JAX, Syft analytics included, auto-reconciliation beta | Trade press; demo claims unverified |
| A3A-32 | https://www.business.com/articles/payment-terms-collection-cycle/ | 2026 | Media | Intuit 2026: 59% overdue, $17,700 avg; Chaser forecasting claim via search | Secondary |
| A3A-33 | https://www.actionnewsjax.com/news/real-cost-late/PSLENA6EKMYNXN2WIUNCA7KDW4/ | 2025 | News (sponsored survey) | Gateway n=503, 64% have 90+ day invoices | Lender-sponsored |
| A3A-34 | https://quickbooks.intuit.com/learn-support/en-us/banking/stripe-payouts-reconciliation/01/836529 | n/d | Intuit Community | Fee difference on payout reconciliation | User thread; read via snippet only |
| A3A-35 | https://eightx.co/blog/compare/reviews/a2x-for-ecommerce-review | n/d | Consultant review | A2X payoff threshold; lump-payout framing | Consultant, may sell services |
| A3A-36 | https://linkmybooks.com/blog/tiktok-shop-payout-doesnt-match-xero-a2x-switch | 2026-08-20 | Competitor blog | A2X missed fees in TikTok Shop case | Competitor marketing |
| A3A-37 | https://www.indiehackers.com/post/i-ran-20-free-stripe-audits-this-month-here-is-every-number-and-what-i-found-f756ba95ea | 2026 | Founder post | 13 of 20 accounts had webhook issues | Self-reported, lead-gen |
| A3A-38 | https://www.indiehackers.com/post/3-months-building-stripe-fee-auditor-0-revenue-5-clicks-2-real-users-heres-what-i-learned-9750b274bb | n/d | Founder post | Contradiction: stripe-fee auditor with 0 revenue | Title only seen |
| A3A-39 | https://www.ycombinator.com/launches/I43-justpaid-io-loopfour-spend-confidently-with-smart-financial-tools | n/d | YC launch page | JustPaid checks vendor bills against contract pricing | Vendor/YC promotion |
| A3A-40 | https://www.getaleph.com/answers/automate-month-end-close-commentary-ai | 2026 | Vendor blog | Commentary takes 1 to 3 days; traceability risk | Vendor |
| A3A-41 | https://dodopayments.com/blogs/stripe-tax-explained | 2026 | Vendor blog | Stripe Tax 0.5%, filing limits | Competitor |
| A3A-42 | research/appendix/agent2_market.md (repo file) | 2026-11-19 | Internal | Baseline price anchors, Baremetrics 9% MRR, Xero/Gateway data | Internal synthesis |

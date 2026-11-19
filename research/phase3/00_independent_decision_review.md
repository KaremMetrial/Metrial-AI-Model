# 00 — Independent Decision Review (Phase 3)

**Date:** 2026-11-19. **Role:** investment committee reviewing its own Phase 2 recommendation ("Outcome C: do not build yet; run a 30-day paid Profit & Cash Leak Audit; Margin Investigator is the lead hypothesis").
**Method:** five independent reviewers (competitive verification, reachability/pricing, evidence audit, customer-evidence search, hostile statistical/logic review) plus my own re-scoring and expected-value model. Raw reports: `appendix/`. Nothing was purchased, no one was contacted, no code was written, and nothing was published on your behalf.

---

> **Update (see `11_founder_inputs_addendum.md`):** after the founder's answers (no contacts, very limited cash, 120+ hours), the approval is narrowed to Gate 0 plus a non-selling Gate A access test (≈ 40 hours); Stage 1 is not approved until both pass. Updated prior ≈ 5–8%.

## 1. Verdict

**Decision: B — approve a REDESIGNED validation experiment. Do not approve the Phase 2 experiment as designed.**

| Question | Answer |
|---|---|
| Does "don't build yet" survive review? | **Yes.** It is strengthened. |
| Does "run the 30-day paid audit as designed" survive? | **No.** It is under-powered, conjunctive, pools three different cohorts, asks strangers to prepay, tests a human service, and starts in the worst month of the year for ecommerce owners. |
| Is Margin Investigator still the lead hypothesis? | **Demoted.** It is third on Phase 2's own scores in most weightings. It stays on the shortlist for strategic reasons (breadth, expansion), not evidence. |
| Is there a real unmet need? | **Not proven.** Most of the proposed workflow already exists in rentable form. A narrow *last mile* may be unmet, and nobody has shown it is paid for. |
| Should we stop (D)? | **Not yet, but it is close.** Stopping is nearly as good as the redesigned test unless your honest prior is below roughly 6–8% or you cannot cap the effort at about 120 hours. |

## 2. What changed my mind about Phase 2 (the six findings that matter)

1. **A primary source refutes a Phase 2 claim.** Phase 2 wrote "no margin workflow found" for Claude for Small Business. Anthropic's own launch page (fetched in full, 2026-11-19) names a "margin analyzer", a QuickBooks-plus-PayPal 30-day cash forecast, an "invoice chaser" that ranks overdue invoices and queues reminders for approval, a monthly close that reconciles books against settlements, and a scheduled "business pulse". Anthropic's plugin repository defines 35 connectors, including QuickBooks, Xero, Shopify, PayPal and Stripe, and its documented skills combine Shopify and ledger data in one run with explicit approval gates. The cash and reconciliation modules Phase 2 hoped to fall back on are the ones now covered.
2. **But the same primary sources document limits.** The plugin's own skill files say the cash-flow skill "does not reconcile last month's cash movement or attribute historical changes to causes", the invoice-chase skill "has no DSO metric or trend analysis of its own", the business-pulse skill "doesn't compute margin directly", and the margin and COGS definition is left to the owner. The skills show no evidence ledger, no counterevidence step, no separate confidence for observation versus explanation, and no outcome follow-up. This is the best positive evidence of a gap found in either phase — and it describes prompt files, which a platform vendor can change in a day.
3. **My "ranking is unstable" claim was wrong.** Over 5,000 random weightings, Late-AR/cash is first in 86% of draws and margin is first in about 0–2%. Phase 2's own table said Cash/AR was first under every weighting, then its headline said the opposite. The real instability is in *what the scores mean*, not in the order.
4. **The experiment's statistics are poor.** With 15 qualified prospects and a pass line of 4 payers, a product with a true 30% conversion fails to pass 30% of the time. With the five-condition pass rule Phase 2 actually wrote, a good product fails at least 60% of the time. A bad product (10%) passes 5.6% of the time; a 20% product passes 35%. (Reproduced from the reviewer's script.)
5. **Reaching the customer is the binding constraint, not price.** There is no reliable count of Shopify + QuickBooks + wholesale businesses at $2–20M. Cold-email reply rates in the only dataset found are about 0.45–3%. Shopify Community bans promotion, and r/shopify and r/ecommerce rules reportedly do likewise (seen through third-party summaries). Qualifying 15 businesses probably takes hundreds of manual touches; four prepaying strangers is a low-likelihood outcome; a result of 0–2 would be uninterpretable (distrust? no demand? timing?).
6. **Several Phase 2 "facts" were stronger than their sources** (full audit in `01`). The most consequential: "behavior contradicts the premise" (the pass-through surveys do not measure realised pass-through, and 45% not passing through everything is consistent with a leakage premise), "100–300 bps / 3–5% leakage" (sponsor estimates for $100M–$1B distributors, not the $10–75M target; the 3–5% figure does not reconcile with its own example), and "recoveries decay" (one aggregator-relayed number with no period).

## 3. What did NOT change

- **No one has shown that small businesses pay for an explanation product.** Phase 3 could not close this. The customer-evidence reviewer read **zero** thread bodies, found **zero** statements from owners or bookkeepers about paying for margin or cash explanation, and could not search Reddit at all. The voice-of-customer hole is exactly as large as before. The honest status is "no evidence either way", not "evidence of no demand".
- **Every primary host except Anthropic, claude.com and GitHub was blocked** (Intuit, Xero, Shopify, NetSuite, Oracle, G2, trade bodies, news). Nearly everything about those products is a search-snippet reading. This limit applies to this review too.
- **Xero's ban on using API data to train AI/ML is now confirmed** by a snippet of Xero's own developer FAQ plus two trade-press reports. Phase 2 called it "reported, verify". It blocks cross-tenant learning from Xero data and should be treated as confirmed for planning.

## 4. Why B and not the alternatives

| Option | Verdict | Reason |
|---|---|---|
| **A. Approve the 30-day experiment as designed** | **Reject** | Dominated by stopping when the prior is below ~20–28% and by building when it is above ~23–25% (reviewer's model, all inputs assumptions). Wrong cohort mix, wrong statistics, wrong month, and it ignores the Claude findings. |
| **B. Approve a redesigned experiment** | **Choose** | Keep the one cheap falsification step but front-load a kill gate, split cohorts, replace the pass rule with a sequential payers-only rule, lower the trust barrier with a capped free scripted scan, and start customer-facing work after the holidays. Cost ≈ 120 hours and < $400 at most. |
| **C. Reject and investigate another opportunity** | **Reject** | No alternative has demand evidence either; Cash/AR is the easiest but now the most directly covered by free tools. A different topic restarts the same evidence gap. |
| **D. Stop** | **Live alternative** | Reasonable if your honest prior is below about 6–8%, if you cannot commit ~120 hours, or if Gate 0 shows an existing tool already produces an acceptable explanation. |

## 5. The redesigned experiment in one screen

1. **Gate 0 (≤ 25 hours, $0, no customers):** run Claude for Small Business, Intuit's AI, Shopify's Sidekick and a plain prompt on a seeded Shopify + QuickBooks sandbox with known causes. If an existing tool already writes an acceptable case file, **stop**. If not, test whether "Claude + deterministic evidence tables" beats "Claude alone" — that tells you whether the product is an *evidence layer* rather than an *analyst*.
2. **Stage 1 (≤ 95 hours including scan scripts and target list; customer-facing from January):** a two-step ladder per prospect: a capped, scripted free **scan** (observations only, no causes, ≤ 90 minutes) followed by a fixed-scope, fixed-price **paid investigation** ($750 Shopify cohort; $2,000 distributor cohort via introductions only). Cohorts are never pooled.
3. **Decision rule:** a sequential test on paid conversion among qualified scan recipients (H0 10% vs H1 30%), with a futility stop at 0 payers in 9 qualified recipients, a cap at 25 recipients or 95 hours of Stage 1, and a "not run" verdict if fewer than 10 qualify in six weeks.
4. **Tripwires for "consulting, not software":** hours per investigation must fall ≥ 40% from first to fourth; ≥ 60% of deliverable numbers must come from a re-runnable script; at least two payers must commit to a recurring plan.

Full design: `04`. Measurement definitions: `05`. Decision details, budget, expected value, and conditions to build or abandon: `08`.

## 6. How this review is organised
`01` evidence audit · `02` competitive claims verification · `03` customer and pricing reassessment · `04` experiment redesign · `05` measurement and success criteria · `06` opportunity ranking sensitivity · `07` long-term platform alignment · `08` final investment decision · `09` Arabic executive summary · `10` source register.

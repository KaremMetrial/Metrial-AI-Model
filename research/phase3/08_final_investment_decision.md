# 08 — Final Investment Decision

> **Update (see `11_founder_inputs_addendum.md`).** After the founder reported no contacts in the field, very limited cash and 120+ available hours, the committee narrowed this decision: **approve only Gate 0 (≤ 25 h) and a new non-selling Gate A access test (≤ 15 h) — about 40 hours.** Stage 1 below is **not approved** until both gates pass and a warm path to qualified prospects exists. My updated prior is ≈ 5–8% (was 8–15%), at or just below the ≈ 6.5% break-even, so stopping after either gate is an acceptable, likely outcome. Everything below that conflicts with this note is superseded by it.

## Decision: **B — Approve a redesigned validation experiment**
(Not A: the Phase 2 design is rejected. Not C: no better opportunity has evidence. Not D yet: stopping is a close second and becomes the right answer under the conditions in §7.)

Every number in this document is an **assumption** unless a source is named. I have not contacted anyone, spent money, or run any experiment.

## 1. What exactly is approved
A two-stage, **time-boxed and cash-capped** experiment (details in `04`, measures in `05`):
- **Gate 0** — a ≤ 25-hour, $0, customer-free bake-off of existing tools on seeded Shopify + QuickBooks data. Can end the project.
- **Stage 1** (≤ 95 hours: scan scripts, target list, discovery conversations, scans, ≈3 paid investigations) — a capped free scripted *scan* followed by a fixed-scope $750 *investigation* (distributor cohort: $2,000, introductions only), judged by a sequential test, with customer-facing work starting in January.
- A weekly Brief at $299/month is **offered at delivery** to measure recurring intent.

## 2. Maximum investment
| Resource | Cap | Basis |
|---|---|---|
| **Time** | **120 founder-hours total**: Gate 0 ≤ 25; scripts, target list and discovery ≤ 35; scans ≤ 20; paid investigations and follow-ups ≤ 35; decision memo ≤ 5 — and **≤ 10 calendar weeks** from Gate 0 start to the decision memo. **Hard stop when the hours are spent**, even if the sequential test has not concluded (record "capped by hours") | Phase 2's design was 127–207 bottom-up hours; this plan is cheaper because the scan is scripted, cohorts are split and only ≈3 investigations are budgeted |
| **Cash** | **≤ $400** (tool subscriptions you already need, a domain, a template pack) | Phase 2: < $500; no ads, no data purchases |
| **Opportunity cost** | ≈ $9,000 at an assumed $75/hour (120 h) | Assumption |
**If any cap is hit before the decision rules fire, the experiment ends and the default is D (stop), not "extend".**

## 3. Expected value (all inputs assumptions; code: `appendix/p3_ev_redesigned.py`, derived from the skeptic's model)
Inputs: $75/hour; build cost $60,000 (4.5 months of a $13.5K/month lean team); value of a "good" world $250,000 present value (small SaaS incl. exit option), 10% delay haircut; Gate 0 (25 h) passes in 90% of good worlds and 50% of bad worlds (i.e., it catches half the bad ones); Stage 1 (95 h + $300) accepts H1 in 80% of good worlds and 7% of bad worlds; the Phase 2 column uses 135 h, $500 and its conjunctive pass rule (35% / 2%).

| P(a viable paid product exists) | Stop | Build now | Phase 2 design (135 h, conjunctive) | **Redesigned (120 h)** |
|---|---|---|---|---|
| 5% | 0 | −$47.5K | −$8.9K | **−$1.8K** |
| 10% | 0 | −$35.0K | −$5.9K | **+$4.1K** |
| 15% | 0 | −$22.5K | −$3.0K | **+$10.0K** |
| 20% | 0 | −$10.0K | −$0.0K | **+$15.9K** |
| 30% | 0 | +$15.0K | +$5.9K | **+$27.7K** |
| 50% | 0 | +$65.0K | +$17.7K | **+$51.3K** |

**Break-even prior for the redesigned plan: ≈ 6.5%** (4.6% if Gate 0 catches only 30% of bad worlds; 7.7% if Stage 1 takes 130 hours instead of 95; **≈ 21% if a good world is worth $125,000 instead of $250,000**). The Phase 2 design needed ≈ 20–28%.

**Reading, honestly:**
- The redesigned experiment is worth doing if you believe there is more than roughly **6–21%** chance that a viable paid product exists here. My own judgment of that prior, given **zero demonstrated willingness to pay, a primary-source confirmation of free competing tools, and no customer conversation yet**, is about **8–15%**. That puts the experiment at **marginal-to-positive**, not compelling.
- The value of the experiment is mostly **avoiding a wasted build** (≈ $60K and 4–6 months), not the value of a pass. If you would not otherwise build for months at full cost, the avoided loss is smaller and the case weakens.
- The model is crude: it treats build as irreversible, ignores audit revenue, and is very sensitive to the value of a good world and to Gate 0's catch rate. Treat it as a way to see which inputs matter.
- **Why approve despite a marginal EV:** the downside is capped (≈ 120 hours, < $400), Gate 0 is a cheap early exit, and the experiment produces reusable assets whatever the outcome (scripts, case-file template, labelled scenarios, a documented answer on free-tool coverage).

## 4. Required evidence BEFORE starting Stage 1 (Gate 0 completes first)
1. **Gate 0 result** recorded against the pre-registered "acceptable" definition (`04` §3), with tool versions and dates.
2. **Primary reading** of the developer/data-use terms of Xero (AI/ML clause scope), Intuit, and Shopify, plus Anthropic's connector terms — and a decision on which stack to use (QuickBooks first unless Xero terms are harmless).
3. **QuickBooks access path verified**: exports and customer-run reports suffice for the three data sets; do not promise "read-only login".
4. **Target list**: ≥ 60 named, reachable Shopify + wholesale businesses and ≥ 10 named accountants/fractional CFOs; ≥ 8 non-selling discovery conversations completed (accountants and a few owners), with written notes. Only what actually happened is recorded.
5. **Scan scripts** running on the seeded sandbox data and on one friendly real dataset, with hours logged.
6. **One-page data-handling note and engagement terms** prepared; refund/liability exposure reviewed against local requirements (this document is not legal advice).
7. **Pre-registration** written and dated: thresholds, caps, stopping rules, definition of "qualified", loss-reason codes.
8. **Your cash floor, founder draw, and honest prior** written down.

## 5. Success criteria (all required; details in `05`)
- **Primary:** the sequential test on cohort S crosses the success boundary (e.g., 2 payers and 0 non-payers; 3 with ≤ 4 non-payers; 4 with ≤ 8; 5 with ≤ 13), with payment by the full fee.
- **Recurring:** at least two payers commit to the weekly Brief ($149–$399/month) with card or signed order form and a start date within 30 days.
- **Software tripwires:** ≥ 40% fall in hours per investigation (first to fourth); ≥ 60% of numbers from a re-runnable script; median onboarding ≤ 8 hours by the fourth; cost coverage usable for ≥ 60% of scans.
- **Quality:** 8 of 8 evidence-completeness items on every case; no *refuted* explanation delivered with high confidence; at least one confirmed explanation per payer; blind-comparison results favour the case file on ≥ 3 of 4 rubric items for at least half of compared cases (directional).
- **Value:** at least half of payers "very disappointed" to lose it.

## 6. Failure criteria (any one ends the experiment)
- **Gate 0:** Claude SMB, Intuit AI or Sidekick is acceptable on ≥ 2 of 3 seeded scenarios.
- **Futility:** 0 payers among the first 9 qualified cohort-S recipients, or the H0 boundary crossed (1 in 14; 2 in 18; 3 in 22).
- **Not run:** < 10 qualified recipients after six weeks → report "not run"; decide whether reach, not demand, is the problem; **do not extend by default**.
- **Economics:** median onboarding > 12 hours after four investigations or scripted share < 40%.
- **Trust:** most prospects refuse exports without a heavy security review.
- **Recurring:** no payer will commit to any recurring plan in $149–$399.
- **Quality:** a high-confidence explanation is refuted by records and cannot be fixed by a rule within two weeks.
- **Caps:** 120 hours, $400, or 10 weeks reached first.
- **Early stop:** 5 of the first 10 conversations say a free in-product tool already answers their question.

## 7. Conditions that justify building an MVP
**All of:** Gate 0 passed; Stage 1 success criteria met; at least two recurring commitments; tripwires met; a named ICP and stack; the primary-term review shows no blocking clause; your cash floor allows ≥ 8–12 weeks of build.
**What gets built:** only a **6-week thin version for the paying cohort** (two connectors or exports, reconciliation/coverage, the bridge and lag detector for the winning module, the case file, the weekly Brief, the decision log) — not the platform. Re-run the economics with measured hours before committing further (Phase 2's corrected base case: margin at $399/month needs ≈ 68 customers to cover a $13.5K/month team; cash/AR at $199/month ≈ 96; both ignore churn and ramp).

## 8. Conditions that justify abandoning the opportunity
- **Any failure criterion in §6.**
- **Your prior is below ~6–8%** after Gate 0, or you cannot commit ~120 hours (→ D).
- **A platform vendor ships the explanation** (persistent cross-source investigation with evidence and outcome tracking) and prospects confirm they no longer have the gap.
- **The primary-term review blocks the design** (e.g., a data-use clause that prohibits the intended processing).
- **Payers are friends or favours**, not repeatable strangers.
- **Willingness to pay appears only for a human analyst's judgment and cannot be scripted** (a services business, a different company).
- **Two consecutive cycles** (this one and one revised cycle, with a changed hypothesis) fail the pre-registered criteria.

## 9. What to do in the next ten days
1. Write your prior, cash floor, draw and the caps above in a dated note. If the prior is below ~6–8% or you cannot commit ~120 hours, **choose D now.**
2. Create the Shopify development store and QuickBooks sandbox; seed the three scenarios (§ `04` 3); write the "acceptable" definition *before* running anything.
3. Run Gate 0 arms 1–4; log hours; stop at 25.
4. In parallel, read the primary terms (Xero, Intuit, Shopify) and the Anthropic connector terms; note which hosts you need to open for a primary-page rerun of this review.
5. Start the target list and schedule the first discovery conversations (non-selling; accountants and a few owners) for December.
6. **Decision at the end of Gate 0:** stop (D), continue to Stage 1, or revise the hypothesis; record it in a dated memo.

## 10. Committee statement
This committee does not approve building a product. It approves spending at most ~120 hours and < $400 to learn whether an evidence-first investigation layer is already commoditised and, if not, whether strangers will pay for it. The probability of a viable outcome is low by my judgment (≈ 8–15%); the cost of learning is small and capped; stopping is a respectable outcome. If the result is "no", that is a successful use of the experiment.

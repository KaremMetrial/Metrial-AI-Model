# Phase 3 / Agent 5: Skeptic Review of Phase 2

**Date:** 2026-11-19. **Scope:** Phase 2 files 00-09 plus `p2_scoring_model.py` and `p2_econ_model.py`. Phase 1 skimmed. **Method:** Phase 2 was read as written. Arithmetic was rechecked and the scoring and the experiment were simulated (`p3_a5_rank_stability.py`, `p3_a5_experiment_math.py`, same folder). Every number labelled ASSUMPTION is my input, not a fact.

**New fact used throughout:** Claude for Small Business (anthropic.com, 2026-05-13) lists 15 workflows, including a QuickBooks+PayPal 30-day cash forecast, an "invoice chaser" that ranks overdue invoices and queues reminders for approval, a monthly close that reconciles books against settlements and writes a P&L, a named "margin analyzer" (no details), and a scheduled "business pulse". Phase 2 recorded "no margin workflow found" (`01`, row for Claude for Small Business).

---

## 0. Bottom line

**Recommendation: B, approve a redesigned experiment, with a cheaper kill gate in front of it.** Do not approve the 30-day audit as designed (A). The reasoning:

- Phase 2's honest core finding is "no evidence of willingness to pay for explanation as a software product". That justifies a cheap falsification step. It does not justify this particular step.
- The experiment as written has four defects:
  - It is under-powered, and its pass line is much harder to reach than a viable business requires.
  - It lets one test feed three hypotheses, so the result cannot attribute demand to any of them.
  - It samples from the segment Phase 2 itself said cannot pay.
  - It measures willingness to pay for a human service, which is a consulting signal.
- The new Claude for Small Business facts hit the very modules Phase 2 hoped to fall back on (cash/AR, reconciliation) and name a margin workflow. That makes a 1-week, near-zero-cost bake-off against Claude a better first gate than a 30-day audit.
- Under my assumed inputs (section 6), the experiment is worth doing only if the founder's prior that "a viable paid product exists here" is roughly 12-35%. The evidence Phase 2 itself collected (zero named payers, platform absorption) pushes honest priors toward the bottom of that window. D (stop) is therefore a live alternative, not a straw man.

---

## 1. Does "Outcome C: run a 30-day paid audit" follow from the evidence?

**Partly.** The inference "evidence is insufficient to build, so test before building" is sound. The inference "so test with this 30-day, three-module, pay-first audit" is not derived from anything in the evidence. It is a design choice presented as a conclusion.

### 1a. Is it a cop-out?

It is not an evasion, because it is falsifiable and has kill criteria. But it has the structure of one in three ways:

1. **Every path is rescued by the test.** Phase 2 demoted margin, said no module has evidence, and ranks nothing above "lead hypothesis". Then it assigns the unresolved choice to the experiment (A, B, or stop). It never states a probability that anything works, so no one can tell what outcome C is betting on. See section 6: without a prior there is no way to say whether the experiment is worth its cost.
2. **"Run an experiment" is the default for every ambiguous idea.** The report never prices the alternative "stop now". For a founder with limited capital, 135-200 hours is the scarcest input, and the report never compares it to the next-best use. D is dismissed implicitly: "No alternative has better evidence" is an argument for *no alternative*, not for the experiment.
3. **The evidence stated against WTP is mis-stated in the headline.** `00` §2 says nobody has been shown to pay for an explanation product. But `06` §1 lists fractional CFOs at $1.4-12K/month, distribution consultants at $5-20K/month, and Fathom commentary, all of which are paid explanation. What is unproven is *explanation as low-priced software*. That is a narrower and different claim, and the experiment (a human-delivered service) is the form for which evidence of payment already exists. A pass would therefore be weak evidence for the software thesis (section 5).

### 1b. Is the "three independent agents" claim sound?

`00` §6 says WTP absence is "consistent across three independent agents (1, 3A, 3B)". They were all blocked from primary pages and Reddit and relied on search-result summaries (`00` §5). Their silence on WTP is correlated: they share the same blind spot. Absence of evidence under that constraint is weak evidence of absence, and the report treats it as strong. This cuts both ways: it weakens the reason to demote margin and equally weakens the reason to believe no one pays.

### 1c. Is the right verdict actually something else?

The Phase 2 verdict is the right *family* (do not build) but wrongly *shaped*:
- Without a cheap prior step, the 30-day audit costs 135-200 hours for a 9-25% chance (conjunctive rule, section 3) of a decision-grade pass.
- A better sequence is: (i) 3-5 days testing whether Claude for Small Business already produces the "explanation" for margin and cash on sample QuickBooks data (kill gate); (ii) only then, a smaller, single-hypothesis pre-sale. See section 8.

---

## 2. Internal consistency

### 2a. Scores: arithmetic and stability

**Arithmetic is correct.** I recomputed all 15 totals from `p2_scoring_model.py`; they match table `02` §2 exactly, and the two printed sensitivities match (`02` §3). No numeric error in scoring.

**The claim "the ranking is not stable" is wrong as stated.** `00` §2 says the ranking is "not stable ... desk research cannot pick a winner" and `02` §3 says "the framework cannot separate the top three". Yet `02` §3 itself says Cash/AR is first under every weighting. My simulation (`p3_a5_rank_stability.py`, 5,000 weight vectors per scheme, scores unchanged):

| Weight scheme | Cash/AR P(top-1) | Churn P(top-1) | Margin P(top-1) | Margin P(top-3) | P(Cash/AR > Margin) |
|---|---|---|---|---|---|
| Flat Dirichlet (total ignorance) | 0.75 | 0.21 | 0.03 | 0.76 | 0.92 |
| Dirichlet around P2 weights, concentration 10 | 0.77 | 0.14 | 0.03 | 0.58 | 0.93 |
| Dirichlet around P2 weights, concentration 30 | 0.95 | 0.05 | 0.00 | 0.70 | 0.99 |
| P2 weights x uniform(0.5, 1.5) | 1.00 | 0.00 | 0.00 | ~1.00 (3rd) | 1.00 |

What is true: the top three {Cash/AR, Churn, Margin} are the top three in most draws (Cash/AR and Churn are in the top 3 in 94-100% of flat-Dirichlet draws, Margin in 76%). Margin is the *third* choice in most draws and wins only when WTP is ignored (73.5 vs 73.9, a near-tie, driven by setting WTP to 0 and doubling openness). What is false: that the framework cannot choose. By its own scores, **Cash/AR is the winner in 75-100% of weightings and Margin is a distant third**. Phase 2 reports this and then says the opposite in its headline.

**Consequence:** the experiment is organized around margin ("lead hypothesis", ICP-1, "Margin Investigator") although Phase 2's own scoring says margin is not the front-runner. Either the scoring is not what drives the decision (then why publish it), or the experiment is mis-targeted. The honest reading is that the real driver is "margin is the founder's thesis".

**Are the weights biased toward the conclusion?** Not toward margin: WTP is the heaviest weight (20) and margin scores 2 on it, which hurts margin. Two weights embed the founder's preferences (inbound reachability 8, expansion 8). Removing both (`inb=0, exp=0`) gives Cash/AR 76.7, Churn 68.6, Margin 66.2: same order. So the weights are not rigging the answer; they just don't matter much. What matters is the *score entries*.

**Defensible alternative scores (all computed in the script):**

| Change | Cash/AR | Churn | Margin | Notes |
|---|---|---|---|---|
| Published | 77.2 | 72.0 | 68.4 | |
| Claude-for-SB adjustment: openness Cash/AR 2→1, Margin 3→2, Reconciliation 2→1 | 74.8 | 72.0 | 66.0 | Invoice chaser, forecast, close, margin analyzer are named workflows |
| Same, plus Cash/AR WTP 3.5→3 (free bundled substitute lowers price ceiling) | 72.8 | 72.0 | 66.0 | Cash/AR lead shrinks to 0.8 points |
| Margin WTP 2→1 (no evidence at all at $349+) | 77.2 | 72.0 | 64.4 | |
| Expansion 5→3 for Margin and Churn (never demonstrated) | 77.2 | 68.8 | 65.2 | |
| Margin data 4→3 (A5's AMBER-GREEN is for the revenue-side bridge only; true margin needs cost data) | 77.2 | 72.0 | 66.0 | |
| Data+TTV weights raised (tiny team) | 81.0 | 71.2 | 70.3 | |

Defensible conclusion: **Cash/AR and Churn are at or near the top, margin is third at 64-70, and the gap between #1 and #3 is 6-11 points on a 100 scale that rewards ease**. Two scoring entries are questionable: Cash/AR "Open = 2" (after the Claude facts it should be 1) and Margin "Expansion = 5" (asserted, never tested). Neither changes order.

### 2b. Unit economics (06, `p2_econ_model.py`)

Recomputed: all contribution, gross margin, payback and break-even figures match the script and the table in `06`. Specific problems:

1. **Payback ignores the setup fee in the margin case.** The table shows "Net of setup fee: +$620" for the base case, but payback (9.1 months) is computed as CAC ÷ contribution only. Netting the setup surplus gives (1,800 - 620) / 197.5 = **6.0 months**. The model is internally inconsistent in the conservative direction for margin and not for cash/AR (setup 0), which makes margin look worse relative to cash than it is.
2. **Labour is double counted.** Team cost of $13.5K/month already contains the two people. Variable cost then charges CS/validation hours at $55/hour for the same people. Break-even customers (68 / 96) therefore overstate need, while "GM 49.5%" understates. It is also inconsistent: onboarding hours (16 h x $55) are used in payback but not in break-even.
3. **"Break-even" language.** `06` §4.2 says margin "needs price ≥ ~$400/mo or onboarding ≤ ~16 h to break even". That is *positive contribution*, not break-even; break-even is 68 customers. Misleading in a document a founder reads.
4. **No churn, no CAC in break-even, no ramp.** 68 customers x $399 with zero churn is a steady-state number with nothing to say about how many months of acquisition it takes.
5. **Pass thresholds do not match base economics.** Success needs median onboarding ≤ 8 h (`07` §7); the base-case economics use 16 h and only the *optimistic* case uses 8 h. The pass criterion equals the optimistic case. If the test passes at exactly 8 h, the base-case economics don't apply; if reality is 16 h, the test fails a business the base model calls viable. Kill criterion (> 12 h) sits between them. These three numbers should be one number.
6. **Audit revenue vs cost.** At $500-$1,000 pricing and 16-28 onboarding hours at $55/hour ($880-$1,540), each audit loses money before founder time. `06` §4.4 calls it revenue ($2-6K) that "offsets cost"; it does not at the lower tiers. It is fine as a test cost; do not call it an offset.

### 2c. Thresholds and plan consistency

- **"4 of 15" = 26.7%.** `06` §4.4 calls it a "27% conversion". That is the implied *success* conversion for a cold, pre-paid, $500-$1,500 B2B purchase from an unknown vendor, which is high (section 3).
- **"15 qualified prospects" vs the plan's counts.** T1: 10 conversations. T2: 10 accountants approached, 3-5 pilots. T3: 5-8 interviews. These sum to ~18-23 *contacts* of three different types; which 15 count as "qualified prospects" in the denominator is undefined. Accountant "pilots" are free ("I will run the audit free for one of your clients", `07` §3), contradicting "payment before results". Distributor "interviews" are not audits. Only T1 is a paid audit. So the 4/15 denominator is a mixture and the binomial does not apply (heterogeneous p, clustered referrals).
- **"≥ 2 say they'd pay monthly at ≥ $199"** is stated intent from people who just paid $500+; weak and non-comparable to the $349-$999 price in `00`.
- **"≥ 60% have usable cost history"** is measured only on those who paid (≈4), where selection already favours clean data.
- **Hours.** Plan says 120-150 hours. My bottom-up estimate (`p3_a5_experiment_math.py` §3): desk week ~30 h, outreach ~25 h, 15 calls ~20 h, 4 audits at 8-28 h (32-112 h), blind comparison, follow-up and memo ~20 h = **127-207 h**. The base-case audit (16 h) puts it near 170. The plan understates by 20-40% at the realistic end.
- **Accuracy ≥ ~70% on owner-confirmed cases with ≤ 4-8 audits.** With n=6 confirmed cases the rule needs 5/6; a system with true accuracy 70% passes 42% of the time, one at 50% passes 11% (section 3). The threshold is noise, and no ground truth exists for the "owner-confirmed" answers except owner recollection.

### 2d. Other contradictions

- `00` §2 says Cash/AR ranks first "because of ease"; `00` §1 and `09` then say margin is the lead hypothesis. The ICP section (`03`) says the easiest segment (Shopify) has the lowest price ceiling ($49-750/month), and the experiment's T1 track is Shopify brands.
- `00` §6 says "n=15 can falsify but not prove". With 70% power at true 30% and 35% pass chance at true 20%, it cannot reliably falsify a viable product either (section 3).
- `01` lists Claude for Small Business with "no margin workflow found" while the page names a margin analyzer. Phase 2 cannot claim a differentiation verdict (PARTIAL) with that line unverified; if the analyzer does anything useful, the cross-system claim narrows further.

---

## 3. Statistical logic of the experiment

All from `p3_a5_experiment_math.py`. Rule as written: pass ≥ 4 of 15 pay; 2-3 inconclusive (extend 2 weeks); 0-1 fail.

### 3a. Outcome probabilities, n = 15

| True conversion | P(pass, ≥4) | P(inconclusive, 2-3) | P(fail, 0-1) |
|---|---|---|---|
| 5% | 0.005 | 0.165 | 0.829 |
| 10% | 0.056 | 0.395 | 0.549 |
| 20% | 0.352 | 0.481 | 0.167 |
| 30% | 0.703 | 0.262 | 0.035 |
| 40% | 0.909 | 0.085 | 0.005 |

- A "good" product (30%) misses the pass line **29.7%** of the time (3.5% outright fail, 26.2% inconclusive).
- A "bad" product (10%) passes **5.6%** of the time. At 20%, **35%**.
- A product at 10% (which could still be a business) lands in "inconclusive" or "pass" 45% of the time and drives a 2-week extension nearly 40% of the time.
- Fixed-n for 80% power at 30% vs ≤10% false-pass needs **n = 18 with threshold ≥ 4** (power 0.835, false pass 0.098). 15 is just below.
- Alternative thresholds at n=15: ≥3 gives power 0.87 but false-pass 0.18 (0.40 at p=15%); ≥5 gives power 0.49 and false-pass 0.013.

### 3b. The real pass rule is conjunctive

Success requires five conditions (`07` §7). With my ASSUMED conditional probabilities (good world: 0.75, 0.60, 0.60, 0.65, 0.80; bad world: 0.30, 0.40, 0.45, 0.40, 0.40), independent: P(full pass | good) ≈ **0.10**, P(full pass | bad) ≈ 0.0005. Real conditions are positively correlated, so a fair figure for the good world is 0.2-0.4. I use 0.35 in the EV model. Under any plausible correlation, a *good* product fails the full rule at least 60% of the time. The decision rules for A/B require conditions 1-3 plus margin pull in half of payers: with 4 payers, "half" is 2, which is a coin toss between any two modules.

### 3c. The 70% accuracy rule

At n=6 confirmed cases: need 5/6. True accuracy 85% passes 78%; 70% passes 42%; 50% passes 11%. At n=15: 94% / 52% / 6%. The test cannot distinguish 70% from 85% at any feasible n.

### 3d. Blind preference

"Clear majority" with 4 payers means ≥ 3/4. A coin-flip preference passes 31%; true 70% preference passes 65%.

### 3e. Is 15 qualified prospects achievable?

ASSUMED funnel (outreach plus inbound checker; no audience exists today): pessimistic 300 contacts x 3% reply x 35% qualified = **3**; base 400 x 6% x 45% = **11**; optimistic 400 x 10% x 60% = **24**. A zero-audience founder with a three-week recruiting window should expect 5-12 qualified conversations, not 15, and fewer who will wire $500-$1,500 to an unknown vendor before seeing anything. "≥ 15 qualified conversations booked or completed by end of week 2" is a stretch target presented as a plan. If the base case holds, the test ends with n ≈ 11 and the threshold 4/15 is 36% of the sample, a much higher bar.

### 3f. Better stopping rules

1. **SPRT, H0 = 10%, H1 = 30%, α = β = 10%.** Each payer adds +1.10, each non-payer -0.25 to log-LR; stop for H1 at +2.20 and for H0 at -2.20. Simulated: true 30% accepts H1 88% of the time (E[n] = 14.0); true 10% accepts H1 7% (E[n] = 16.6); true 5% accepts H1 1% (E[n] = 12.4); true 20% is a coin flip (49%, E[n] = 19.6). This is better than the fixed rule at roughly the same sample, and stops as soon as the evidence is conclusive.
2. **Bayesian with a Beta(1,1) prior** and decision rules on the posterior. After k payers of n: 0/15 → P(p ≥ 20%) = 0.03; 1/15 → 0.14; 2/15 → 0.35; 3/15 → 0.60; **4/15 → 0.80**; 6/15 → 0.97; 0/8 → 0.13; 3/8 → 0.91. Pre-register: continue until n = 20-25 or P(p ≥ 20%) is outside [0.15, 0.85]. 4/15 is then only an 80% posterior for "better than 20%".
3. **Early futility stop:** 0 payers in 8 qualified: P = 0.058 if true 30%, 0.43 if 10%. 0 in 10: 0.028 if 30%. Stop for futility at 0/10 and save the rest of the hours.
4. **Define the unit and the target.** The decision-relevant parameter is not "conversion" but *paid audits at a price*, split by segment. Pool nothing across segments.

---

## 4. "Pay before results" for unknown sellers

**Where the logic can be wrong:**

1. **It tests trust-in-an-unknown-vendor, not demand.** A conversion of 5% at "pay $1,000 before seeing anything" may reflect brand-less trust friction. Passing it signals demand strongly (a good point for the design), but a *failure* is ambiguous: no demand, or no trust. The test is asymmetric: it can confirm, but its failure is interpretable only if the same outreach is also run with a free or refundable arm to isolate trust.
2. **The seller is the product.** Buyers buy the founder-analyst's judgment. That is a consulting sale; it says nothing about whether software can replace the judgment, and the monthly-intent question ("would pay $199/month") is hypothetical.
3. **Pre-paid vs refund.** US mid-market buyers often refuse pre-payment and sign an SOW with 50% on delivery. A required up-front charge biases toward micro-buyers who can expense $500 on a card, which is the Shopify segment Phase 2 said can't pay $349+/month.
4. **Self-selection on data readiness.** Only those with clean QuickBooks and willing to share an export will pay; the 60% "usable cost history" metric is therefore inflated.
5. **The price test is confounded.** Three price tiers assigned to ~11 prospects gives 3-4 per cell. No price signal can be read.
6. **Three findings for one fee.** The buyer "chooses which finding to read first". Order of reading follows report layout and what the founder emphasizes in the call. It does not reveal preference. One fee for three modules also prevents attributing WTP to any module.

**Designs that might give cleaner evidence:**

| Design | What it isolates | Cost | Weakness |
|---|---|---|---|
| **Single-module paid pilot** (margin only, one segment, $750 fixed, 50% up front / 50% on delivery) | WTP for *one* explanation product at one price | 60-90 h | Needs the segment to be right |
| **Pre-sale of a monthly plan with a refund guarantee** ($299/month, start in 3 weeks) | Recurring WTP directly | 40-60 h | Needs a landing page, a credible vendor |
| **Fake-door / smoke test** (landing page with price and "request audit", measure paid deposits) | Demand at scale without delivering | 20-30 h | Needs traffic; unknown vendor trust again |
| **Distributor-only paid diagnostic via ERP resellers** (10 warm intros, $2,500) | The segment that can pay | 60-100 h | Reach; slow cycles; the pass-through objection |
| **Free first, then paid second** (offer one free finding on their own data, then charge for the next) | Separates trust from value | 50 h | Free pilots don't measure WTP (Phase 2's own point), but a free-then-paid ladder does |
| **Wizard-of-Oz bake-off vs Claude for Small Business** | Whether the "explanation" is distinguishable | 20-30 h | Does not test WTP, but is a cheap kill gate |
| **Letter-of-intent with price from accountants** (3-5 firms agree to resell at $X per client) | Channel economics | 20 h | LOIs are cheap |

My preference: bake-off first, then a single-module paid pilot against warm distributor/ERP-reseller introductions and Shopify-wholesale accounts in separate cohorts.

---

## 5. Long-term vision: product or consultancy?

Phase 2 says the audit "builds raw material" for Company Intelligence. That holds *only if*:
- the audit is templated enough to be automated step by step (data pull, cost-coverage check, bridge, lag detector, case file), and
- the founders track hours per audit as a falling curve.

Danger signs already in the documents:
- Base onboarding is 16 h and 10-28 h per customer (Agent 5). A 16-hour "onboarding" for a $399/month product is a services business with software attached.
- The deliverable is judgment (which cause to rank first, what to abstain on). Phase 2's own test says the product needs to "match the analyst's judgment" and only offers blind-comparison and accuracy as proxies, with the sample sizes in section 3.
- Consulting benchmark pricing in `06`: $150-$600/hour. A founder-delivered audit at $500-$1,500 is below consulting prices. If buyers pay, they pay the consultant price for a below-market consultant. That's a legitimate cash-generating business, but it isn't the SaaS the founder prefers.
- Free in-product AI is converging on the surface (Claude for Small Business with named cash, close and margin workflows). The scalable moat claimed (cross-system evidence, calibration, outcome log) is the part needing human labour and 12-24 months of labelled outcomes.

**Verdict:** the first product can evolve into software *if* three tripwires are added to the experiment: (1) hours per audit must fall by at least 40% from audit 1 to audit 4 with scripts; (2) at least 60% of the deliverable's numbers must come from a re-runnable script; (3) the buyer must pay for something recurring (a monthly Brief), not only a diagnostic. Without them, a pass is evidence for a services business. That is not necessarily bad, but it should be a named decision, not an accident.

---

## 6. Expected value of the experiment

All inputs are **ASSUMPTIONS** (the script is `p3_a5_experiment_math.py`, section 5). Parameters:

| Input | Value | Label |
|---|---|---|
| Founder opportunity cost | $75/hour | ASSUMPTION (freelance backend ~$100-150/h, discounted) |
| Experiment hours | 135 (plan midpoint) or 200 (realistic) | ASSUMPTION (see 3e/2c) |
| Cash | $500 | Phase 2 |
| **Experiment cost** | **$10.6K (135 h) or $15.5K (200 h)** | Computed |
| MVP build cost if built | $60,000 (4.5 months x $13.5K/month team) | ASSUMPTION, from `06` |
| Value of a *good* world after build | $250,000 NPV | ASSUMPTION (small SaaS, discounted, includes exit option) |
| Delay haircut on value from 30 days | 10% | ASSUMPTION |
| P(pass \| good) / P(pass \| bad), payers-only rule | 0.70 / 0.056 | Computed (binomial, 30% vs 10%) |
| P(pass \| good) / P(pass \| bad), conjunctive rule | 0.35 / 0.02 | ASSUMPTION (correlated conditions) |
| Audit revenue (4 x $750 = $3,000 on a pass) | Ignored | Conservative |
| "Good" | a viable paid product exists: true conversion ~30% **and** a retained business follows | ASSUMPTION |

**Decision tree.** Three options: **stop** (0), **build now** (EV = P(good) x $250K - $60K), **test, then build only on a pass** (EV = -cost + P(pass) x [posterior x $250K x 0.9 - $60K]).

**Results, payers-only rule (the best-case reading of the experiment):**

| P(good) | Stop | Build now | Test→build (135 h) | Test→build (200 h) | Best |
|---|---|---|---|---|---|
| 5% | 0 | -$47.5K | -$8.0K | -$12.9K | **stop** |
| 10% | 0 | -$35.0K | -$2.0K | -$6.9K | **stop** |
| 20% | 0 | -$10.0K | +$9.9K | +$5.0K | **test** |
| 30% | 0 | +$15.0K | +$21.8K | +$17.0K | **test** |
| 50% | 0 | +$65.0K | +$45.7K | +$40.8K | **build now** |

**Results, conjunctive rule as written (pass is rarer):**

| P(good) | Test→build (135 h) | Test→build (200 h) | Best |
|---|---|---|---|
| 5% | -$8.9K | -$13.8K | stop |
| 10% | -$5.9K | -$10.8K | stop |
| 20% | -$0.0K | -$4.9K | stop |
| 30% | +$5.9K | +$1.0K | build now (+$15K) |
| 50% | +$17.7K | +$12.8K | build now |

**Break-even priors** (the experiment beats stopping when P(good) exceeds):
- Payers-only rule: **11.7%** (135 h), **15.8%** (200 h). Build-now beats the test above ~32-35%.
- Conjunctive rule as written: **20.1%** (135 h), **28.4%** (200 h). Build-now beats the test above ~23-25%. The design as written has **almost no window** in which it is the best option: it is dominated by stopping below ~20-28% and by building above ~23-25%.
- Cheaper design (~70 h, $200, payers-only sensitivity): positive at P(good) ≥ 10% (+$3.2K) and +$15.1K at 20%.

**What this says.**
1. The experiment is worth doing only if the founder believes there is at least ~12-16% chance (best-case design) or ~20-28% (design as written) that a viable product exists. Given zero evidence of WTP, ongoing platform absorption, and no customer conversations, a calibrated prior is plausibly 5-15%. Honest EV is near zero or slightly negative for the design as written.
2. Cutting experiment cost (by half) and making the pass rule payers-only lowers break-even to ~10% and widens the window. **Redesign makes the experiment worth more than it costs; the original design barely does.**
3. The model is crude: it treats "build" as irreversible (real MVPs can be stopped early at lower cost, which would favor build-now) and ignores audit revenue (favors the test). It is also very sensitive to V_good: halving V to $125K moves the break-even prior to ~30%+ for the design as written. Treat it as a way to see which inputs matter, not as an answer.
4. **The value of the experiment is mostly "avoid a wasted $60K build"**, not the value of a pass. If the founder was not going to build for 4.5 months at full cost anyway (founders drawing little, building lean MVP over 8-12 weeks, as `09` suggests), the avoided loss is lower and the test is worth less.

---

## 7. The 10 weakest points of Phase 2, ranked

| # | Weakness | Severity | What would fix it |
|---|---|---|---|
| 1 | **The experiment is under-powered and its pass rule is conjunctive.** 30% of good products miss 4/15; five conditions together fail a good product at least 60% of the time; the 70% accuracy and "clear majority" rules are noise at n ≈ 4-6. | Critical | Replace with a payers-only primary rule, SPRT or Bayesian stopping, secondary metrics reported but not gating. |
| 2 | **No prior and no EV: the experiment is never shown to be worth its cost, and "stop" is never priced.** | Critical | State P(good), cost in hours, and the break-even prior (section 6). If the founder's prior is below ~12%, choose D. |
| 3 | **Experiment targets margin while the scoring puts Cash/AR first in 75-100% of weightings; the report says the ranking is "unstable".** The framing misstates its own evidence. | High | Say plainly: Cash/AR is first on ease, margin is third on thesis; test the one the founder actually wants to run and why, or test cash/AR head to head. |
| 4 | **The paid-audit test measures WTP for a human service, then infers software demand.** A pass is consistent with a consultancy. | High | Add recurring-purchase and hours-per-audit tripwires (section 5); pre-sell a monthly plan. |
| 5 | **The denominator and cohort are undefined and mixed.** Accountants get a free audit, distributors get interviews, only T1 pays. Qualified prospects are heterogeneous, non-independent. | High | Run separate cohorts; define "qualified" and "paid" before outreach; no free arm counts toward the pass. |
| 6 | **Claude for Small Business is not handled.** Phase 2 says "no margin workflow found" while the page names a margin analyzer and lists the cash, close and chaser workflows that Cash/AR and reconciliation (the fallbacks) rest on. | High | Day-1 gate: run Claude for SB (and Intuit/Shopify AI) on sample data; if it explains a seeded margin change adequately, stop. |
| 7 | **"Nobody has been shown to pay" rests on blocked-source search summaries (non-independent), and the headline contradicts `06`'s own consulting/fractional-CFO prices.** | Medium-High | Re-state as "no evidence for low-priced software explanation"; do the primary-source and Reddit pass in week 1; accept the finding is weak either way. |
| 8 | **Sample sources are the segment Phase 2 said cannot pay.** T1 (Shopify) is the inbound path but has the lowest ceiling; the $900+ segment (distributors) gets 5-8 *interviews*. | Medium-High | Make distributors/ERP-reseller introductions the primary arm of the paid pilot; treat Shopify as the cheap secondary arm. |
| 9 | **Hours and economics are internally inconsistent.** 120-150 h plan vs ~127-207 h bottom-up; 8 h pass vs 16 h base vs 12 h kill; payback omits setup offset; labour double-counted in break-even. | Medium | One hours estimate; one onboarding threshold tied to the base model; fix payback and break-even definitions; cap total hours and cash a priori. |
| 10 | **Feasibility of 15 qualified prospects is asserted, not shown, and "willingness to grant access to an unknown vendor" (assumption 5) is untested.** | Medium | Show a funnel with conversion assumptions; set a minimum n at which the test is declared "not run" rather than failed; do the access question in week 1 interviews. |

---

## 8. Recommendation

### Verdict: **B, approve a redesigned experiment, with a front-loaded kill gate.** Reject A. D is the right call if the founder's honest prior is below ~12%.

**Why not A (approve as designed):** under my assumed inputs it is the worst of the three variants. It is dominated by stopping below ~20-28% prior and by building above ~23-25%; it has under 70% power at the pass line; the pass rule is conjunctive; the denominator is not a binomial sample; and it ignores the new Claude facts. I would not spend 135-200 hours on it.

**Why not C (reject and investigate a different opportunity):** Phase 2's scoring does not give a better candidate with demand evidence. Cash/AR is first on ease and now the most directly covered by Claude's named workflows. Different opportunities have the same WTP evidence gap. No one has shown a reason to restart.

**Why not D (stop) outright:** the founder has one cheap, falsifiable test and Phase 2's evidence is limited by blocked sources, not by contrary findings. If the redesigned test costs ~70 h and the prior is ≥ 10-12%, the EV is positive. D becomes right if the founder cannot articulate any reason to believe in a paying cohort better than the research found.

### Redesign (what B means concretely)

1. **Gate 0 (3-5 days, ≤ 25 h, $0):** run Claude for Small Business, Intuit Assist and Shopify AI on a seeded QuickBooks/Shopify sample with a known cost shock and a known late-payment pattern. If the margin analyzer or a plain prompt identifies the cause and writes an acceptable case file, **stop** (D). Otherwise continue. Pre-write what "acceptable" means.
2. **One hypothesis, one price.** Margin (or the founder's chosen module) only, one fee ($750-$1,000, 50% up front or full up front, stated in advance), no free arm in the count.
3. **Two cohorts reported separately:** (a) Shopify+wholesale brands ($2-20M) via outreach/checker; (b) distributors/ERP-reseller introductions ($10-75M) at a higher price ($2,000-$2,500). Do not pool.
4. **Primary decision on payers, via sequential rule:** SPRT with H0 = 10%, H1 = 30%, or posterior P(p ≥ 20%) with stop at ≤ 0.15 or ≥ 0.85; futility stop at 0 payers in 10 qualified conversations. Cap the test at 25 qualified conversations or 70 hours, whichever comes first. If fewer than 10 qualified conversations are reached in 3 weeks, report "not run", not "fail".
5. **Secondary metrics (reported, not gating):** hours per audit (target a 40% fall from audit 1 to 4), scripted share of the deliverable, accuracy on confirmed cases with exact counts, blind preference with exact counts, monthly-plan pre-sale (offer a real $299/month commitment at delivery).
6. **Set cash floor and founder draw before starting;** budget 70-100 hours, not 135-200.
7. **A pass means "build a 6-week thin version for the paying cohort", not "build the product".**

### What would change my mind
- Gate 0 shows Claude cannot do the cross-system explanation and a prospect group commits money: move toward A-like confidence.
- The founder's prior is below ~12% or they cannot afford 70-100 hours: D.
- Primary-source reading in week 1 shows a hard platform barrier (Xero AI-training clause, Shopify cost-data limits): D or re-pick.

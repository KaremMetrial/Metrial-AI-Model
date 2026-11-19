# 05 — Measurement and Success Criteria

Phase 2's "70% accuracy" was ambiguous: accuracy of what, against what truth, over how many cases. This document defines nine separate measures. **Rule 0: a language model's confidence score is never ground truth.** Ground truth comes only from (a) arithmetic identities, (b) source records (invoices, bills, payouts, contracts, bank rows), (c) independent confirmation by a person who did not see the model's answer first, or (d) a seeded case where the cause was planted. Small samples are reported with exact counts and intervals, never as bare percentages.

**Unit conventions.** A *case* = one investigated finding. A *prospect* = a qualified scan recipient (right stack, decision-maker, exports supplied, named pain). A *payer* = a prospect who paid the investigation fee in full (or the required first instalment) before delivery.

## 1. The nine measures

### M1. Problem-detection accuracy
- **Definition:** of the movements the method flags as material, how many are real and material; of the material movements that truly occurred, how many were flagged.
- **Materiality:** pre-registered per business: ≥ 25 basis points of gross margin or ≥ $1,000/month of cash effect or ≥ 5 days of DSO drift, whichever the owner agrees is "worth a conversation" (record the owner's own threshold before the scan).
- **Ground truth:** (i) **precision** — each flagged item is reconciled to source rows; an item is a *true positive* if the arithmetic reproduces from records and exceeds materiality; (ii) **recall** — before the scan, ask the owner to list the 3 most important changes they already know about (written down first); recall = how many of those the scan detects; plus seeded events in Gate 0.
- **Report:** counts (true positives / flagged; known events detected / known events), per cohort. Do not report a single percentage below n = 10.

### M2. Root-cause explanation accuracy
- **Definition:** for each case where the method *offers* a cause, was the top-ranked explanation correct?
- **Grading (pre-registered, by evidence, not opinion):** *Confirmed* (a record or counterparty confirms the cause, e.g. supplier invoice shows a price rise on the named SKUs); *Partially confirmed* (a material share of the effect explained, residual stated); *Refuted* (records contradict); *Undetermined* (cannot be checked). The owner's recollection counts only when corroborated by at least one record or a second person.
- **Independence:** the grader sees the evidence package, not the model confidence; a second grader (bookkeeper or accountant if available) grades a random 30% of cases; report agreement.
- **Report:** among *answered* cases: confirmed / partial / refuted counts; **abstention rate** separately; never merge abstentions into accuracy. A correct "undetermined" on a planted no-cause case counts as correct abstention.
- **Calibration:** only after ≥ 30 graded cases overall; before that, report nothing about calibration.

### M3. Financial-impact estimation accuracy
- **Definition:** for each case with a stated dollar range, did the later or reconciled figure fall inside it, and how far off was the midpoint?
- **Truth:** the reconciled figure from records (bridge components sum exactly to the observed change; any residual is shown), or the realised figure from the 30-day follow-up where an action was taken.
- **Report:** share of cases whose actual falls inside the stated range; median absolute percentage error of the midpoint (only n ≥ 10); arithmetic-identity check pass/fail for every bridge (must be 100%).

### M4. Evidence completeness
- **Definition:** share of case-file elements present, scored by a fixed checklist: every displayed number traced to rows (Y/N); coverage badge present (cost coverage %, history window) (Y/N); reconciliation to the system's own total within tolerance (Y/N); counterevidence section present and non-empty (Y/N); "could not check" present (Y/N); assumptions listed (Y/N); unexplained residual shown (Y/N); evidence grade per explanation (Y/N).
- **Pass:** 8 of 8 on every delivered case. **Scored by someone other than the author** (the second founder or a template-driven checker).

### M5. Recommendation usefulness
- **Definition:** whether the recommended actions were taken and mattered.
- **Measures:** owner rating 1–5 at delivery; **action taken within 14 days** (Y/N, verified by the owner showing the change or a message); dollar effect reported at day 30 (with "cannot tell" allowed). Report "followed by", not "caused by".
- **Warning:** adoption is not proof of value; a bad action can be taken. Record reasons for non-action (not material / not feasible / already known / do not trust).

### M6. Customer-perceived value
- **Definition:** whether the customer would miss the output and prefers it to what they have.
- **Measures:** (a) "How disappointed would you be if you could not get this again?" (very / somewhat / not) — report counts; (b) **blind comparison** (below); (c) what they say they would use instead.

### M7. Time required to deliver an investigation
- **Definition:** founder hours per scan and per investigation, logged by task (access, cleaning, analysis, writing, review, follow-up), split into **scripted** vs **manual** share.
- **Trend:** first-to-fourth investigation (target −40%); share of numbers produced by a re-runnable script (target ≥ 60% by the fourth). Median reported, not mean.

### M8. Willingness to pay
- **Definition:** money moved, not stated intent.
- **Measures:** payers ÷ qualified prospects, per cohort and per price; time from scan to payment; refusal reasons coded (no urgency / not the right problem / would not prepay / price / would not share more data / already has a tool / wants it free). **Stated intent is recorded but never counts.**
- **Sequential rule:** in `04` §7.

### M9. Repeat purchase or subscription interest
- **Definition:** an actual commitment to continue.
- **Strong signal (counts):** a card on file (or signed order form) for a weekly Brief at a stated price ($299/month) with a start date within 30 days; or a second paid investigation.
- **Weak signal (does not count):** "would you pay?" answers; letters of intent without a price and date.
- **Target:** at least two payers make a strong-signal commitment.

## 2. Blind comparison methodology
Purpose: test whether the case file is better than what the customer can already get.
1. **Same question, same data, same period.** Pick one finding per customer (a margin movement or a cash/DSO movement).
2. **Produce the alternatives faithfully.** Generate the competing output by running the customer's own available tool on the same data: Claude (with the Small Business plugin and connectors), Intuit's AI insights/chat, Shopify Sidekick, and a Polar-style tool only if the customer already uses it. Use the tool's documented prompt and default settings; save prompts and versions; do not tune against it.
3. **Anonymise.** Strip names, logos and formatting; render both as plain documents labelled X and Y in random order.
4. **Rate.** The owner (and the bookkeeper or accountant if available) rates each on a fixed rubric (correct driver named; evidence they could check; honest about limits; would act on it) and states a preference with a one-line reason. Raters do not know which is ours.
5. **Report exact counts** (e.g., "3 of 4 preferred X") with the reasons verbatim; with n ≈ 4–6 this is **directional evidence only**, not a statistic. Never write "clear majority" unless the count is ≥ 4 of 5 or ≥ 5 of 6.
6. **Pre-register** "preferred" to mean preferred on at least 3 of the 4 rubric items.
7. **Repeat** the comparison on Gate 0 seeded data with ground truth, where correctness is measurable.

## 3. Success criteria (all pre-registered; write them down before the first scan)

**Gate 0 passes** if: no existing tool (Claude SMB, Intuit AI, Sidekick) is acceptable on ≥ 2 of 3 seeded scenarios under the pre-registered "acceptable" definition (`04` §3), and Arm 4 (our manual method) is acceptable on all three.

**Stage 1 succeeds** only if all of the following hold:
1. **Willingness to pay (M8):** the sequential test crosses the success boundary in cohort S (e.g., 2 payers and 0 non-payers; 3 with ≤ 4 non-payers; 4 with ≤ 8; 5 with ≤ 13) — **primary decision metric.**
2. **Recurring signal (M9):** at least **two payers** make a strong-signal commitment to a recurring plan.
3. **Software tripwires (M7):** hours per investigation fall ≥ 40% from the first to the fourth; ≥ 60% of the delivered numbers come from a re-runnable script.
4. **Evidence completeness (M4):** 8 of 8 on every delivered case.
5. **Explanation (M2):** report confirmed/partial/refuted/abstained counts; **no refuted explanation delivered with high stated confidence**; at least one confirmed explanation per payer. *No percentage gate below n = 10 graded answers.*
6. **Customer value (M6):** at least half of payers answer "very disappointed" to losing it, and blind-comparison results favour the case file on ≥ 3 of 4 rubric items for at least half of compared cases (directional).
7. **Access and effort:** median human onboarding ≤ 8 hours by the fourth investigation; cost coverage usable (≥ 70% of revenue with known cost, or a customer upload that gets it there) for ≥ 60% of scans.

## 4. Failure criteria (any one)
- **Gate 0:** an existing tool is acceptable on ≥ 2 of 3 seeded scenarios.
- **M8:** 0 payers among the first 9 qualified recipients in cohort S, or the sequential boundary for H0 is crossed (1 in 14; 2 in 18; 3 in 22).
- **Not run:** < 10 qualified recipients in six weeks (report "not run" and diagnose reach).
- **M7:** median onboarding > 12 hours after four investigations, or scripted share < 40%.
- **M2:** any delivered explanation is *refuted* by records after being stated with high confidence, and the method cannot be fixed by a rule within two weeks.
- **M9:** no payer will commit to a recurring plan at any price in $149–$399.
- **Access:** most prospects refuse to supply exports without a heavy security review.
- **Cost:** hours or cash exceed the caps in `08`.

## 5. What these criteria cannot prove
Small samples cannot establish an accuracy percentage or a true conversion rate; they can reject poor products and give directional evidence on good ones. Blind comparison with n ≈ 4–6 is directional. Willingness to pay for a human service is not willingness to pay for software; the tripwires exist to detect that difference. Nothing here measures retention beyond 30 days.

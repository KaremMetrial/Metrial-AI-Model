# Amendments to the frozen pre-registration

`PRE_REGISTRATION.md` was frozen on 2026-11-19 and is not edited. Changes are recorded here with date and reason.

## A1 — 2026-11-21 — Arm 3 data dictionary line (clarification only; no change to criteria, tolerances or decision rule)
**Reason:** the frozen text defines Arm 3 as "Claude + `arm3_evidence` tables" but the data dictionary in `prompts.md` does not say what those extra files are. Without a neutral description the model may be confused about them, which would measure the prompt and not the evidence layer.
**Addition for Arm 3 runs only** (append after the standard data dictionary, before the question):
> The numbered files from `arm3_evidence` are additional summary tables computed from the exports above (coverage and history, monthly summary, reconciliation to the P&L, a September-to-October margin bridge, SKU and channel breakdowns, supplier unit costs, discount rates, carrier cost per order, receivables aging, and days-to-pay by customer and quarter). They are provided as extra files; use them or the raw exports as you judge best.
**Not changed:** the questions (P1, P1e, P2, P2e), the definition of "acceptable", the ±35% tolerance, the scoring procedure, the decision rule, or the rule that no answer key is opened before scoring.
**Made before any Arm 3 run:** yes (Arm 1 runs were already completed and are unscored; this clarification does not affect them).

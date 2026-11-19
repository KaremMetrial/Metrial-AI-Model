# Gate 0 — Pre-Registration (freeze before running anything)

**Status:** DRAFT proposed by the assistant. **The founder must review, edit if needed, then commit this file with the date. After that, no changes.** Frozen on: ____-__-__ by: __________.

## 1. Question
Does a tool the owner can already rent (Claude for Small Business / Claude with files; Intuit AI and Shopify Sidekick if tested) produce an **acceptable** explanation of (a) a margin decline and (b) a cash/receivables problem on synthetic data with planted causes — and does it correctly **abstain** when no cause exists?

## 2. Scenarios (ground truth in `answer_key/`; do not open until all runs are scored)
- **S1 — Margin (dataset A):** gross margin fell from September to October 2026. Several causes were planted (supplier cost, promotion/mix, freight).
- **S2 — Cash (dataset A):** receivables/days-to-pay deteriorated. A specific cause was planted.
- **S3 — Control (dataset C):** gross margin is lower in October by a normal amount of noise. **No cause was planted.**

## 3. Arms
1 = Claude for Small Business or Claude with uploaded files (plain prompts and evidence-style prompts); 2 = Intuit AI / Shopify Sidekick (only if live sandboxes exist; else "not tested"); 3 = Claude + `arm3_evidence` tables; 4 = founder's manual analysis (no LLM).

## 4. Definition of "acceptable" (per scenario, all required)
**S1 (margin):**
1. Names **at least 2 of the 3** planted drivers as material, with the correct direction, and attributes each to the correct entity (cost: the SKUs whose supplier cost rose; promotion/mix: the bundle SKU; freight: DTC carrier cost per order).
2. For each named driver, the magnitude (in basis points of gross margin or in dollars) is within **±35%** of the key's value or, if a different decomposition method is used, the output states its method and the components **sum to the observed change**.
3. Cites **at least 3 checkable records** (bill IDs, order IDs, months/SKUs) that exist in the data and support the claim.
4. States **at least one limitation** that is true of the data (for example, Shopify unit cost is blank for some SKUs; cost for those SKUs came from bills).
5. Does **not** assert as fact a cause that the data cannot support (for example "tariffs", "competitor pricing", "seasonality" without evidence) — such statements must be labelled hypotheses.

**S2 (cash):**
1. Identifies the **specific customers** whose payment behaviour changed (not merely "customers are paying later").
2. States the change in days-to-pay for them (before vs after) within **±10 days** of the key, and their share of past-due receivables within **±20 percentage points**.
3. Cites at least 3 invoice IDs/dates.
4. States at least one true limitation (as-of date, small number of invoices per customer, no payment-terms data beyond due dates).
5. Does not invent customers, causes or amounts.

**S3 (control):** acceptable only if it **abstains or flags low confidence**: says that no specific cause can be identified from the data and/or that the change is within normal monthly variation, **and** does not present an invented single cause as the explanation (candidate hypotheses are allowed if explicitly labelled unverified).

An arm is **acceptable on a scenario** only if every numbered condition for that scenario is met. An arm is **acceptable overall** if it is acceptable on at least 2 of the 3 scenarios.

## 5. Scoring procedure
- Run each prompt **once per arm** (record the date, product and version; do not cherry-pick re-runs; if a re-run is needed because the tool failed to load files, say so and keep both).
- Strip arm labels and shuffle outputs before scoring; if a second person is available, they score independently and disagreements are listed.
- Score each condition 0/1 in `scoring_sheet.csv`; record hours spent per arm.
- **A model's own confidence statement is not evidence of correctness.** Only the answer key and the records decide.

## 6. Decision rule (frozen)
| Result | Decision |
|---|---|
| Arm 1 **or** Arm 2 (if tested) is acceptable overall (≥ 2 of 3 scenarios) | **Stop the software path (D).** Explanation is already available. Record versions/dates; consider only a services niche. |
| Arms 1 (and 2 if tested) are **not** acceptable overall, **and** Arm 3 is acceptable overall | **Continue** to Gate A; note the **evidence-layer** hypothesis (deterministic tables + lineage + abstention) |
| Arms 1–3 all fail overall | Do **not** go to customers. Improve the method until Arm 4 passes, or stop. A failing Arm 4 means the problem or the data model is harder than assumed |
| Arm 2 not tested | Record "not tested"; do not treat as passed; decide on Arms 1/3/4 and flag the gap in the memo |

## 7. Pre-committed caveats
Synthetic, clean, small-scale data; planted causes are simpler than real ones; tools update quickly (results age); one scorer introduces bias; no customer demand is measured; Arm 4 is the founder's skill, not a product.

## 8. Budget
≤ 25 hours and ≈ $0 beyond existing subscriptions. If 25 hours are reached before all arms finish, stop, score what exists, and decide on that evidence.

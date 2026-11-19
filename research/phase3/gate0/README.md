# Gate 0 — Run Sheet and Test Packet

**What this is:** a ready-to-run test of whether tools you can already rent explain a margin change and a cash problem acceptably, using **synthetic** data with planted, known causes. It is the first of the two gates approved in `../11_founder_inputs_addendum.md`. Budget: **≤ 25 hours, ≈ $0 beyond subscriptions you already have.**

**What I (the assistant) did:** built the synthetic datasets, the answer key, the deterministic evidence tables (Arm 3 inputs), the pre-registration template, the prompts and the scoring sheet. **I did not run any tool arm.** Claude for Small Business, Intuit's AI and Shopify Sidekick run in accounts you control; I cannot sign in to them, I will not create accounts or spend money for you, and I could not reach those vendors' sites from this environment. Running them is your step below. **Nothing was contacted or published.**

## Files
| Path | What it is |
|---|---|
| `PRE_REGISTRATION.md` | Definition of "acceptable", scoring rubric and decision rule. **Freeze it (commit with a date) before running any arm.** |
| `prompts.md` | The exact prompts for every arm (plain and evidence-style variants). |
| `scoring_sheet.csv` | One row per run; fill in as you go. |
| `data/A/` | **Dataset A (planted causes):** Shopify-style order lines, products, shipping costs, supplier bills, wholesale invoices, QuickBooks-style monthly P&L. Fictional specialty-food brand, 24 months to 2026-10. |
| `data/C/` | **Dataset C (control):** same shape, **no planted cause**; October margin is lower than September by a normal amount of noise. |
| `arm3_evidence/A,C/` | Deterministic evidence tables built only from the exported files: coverage, monthly summary, reconciliation to the P&L (difference 0), a Sep→Oct margin bridge that sums exactly (residual 0), SKU cost changes, discount and freight tables, AR aging, days-to-pay by customer. |
| `answer_key/` | Ground truth. **Do not open until every run is finished.** |
| `make_seed_data.py`, `build_evidence_tables.py` | Test-fixture scripts that produced the files (not product code). Re-run to regenerate. |

## Arms
| Arm | What | Needs | Status |
|---|---|---|---|
| **1** | Claude for Small Business (plugin skills) or plain Claude on the **uploaded CSVs** (the plugin's README reportedly supports a CSV fallback — confirm in your install) | Your Claude account | **To run** |
| **2** | Intuit's AI report insights/chat and Shopify Sidekick on the same data | A QuickBooks sandbox company and a Shopify development store loaded with equivalent data. The CSVs here cannot be imported as history into those products; loading a live store/ledger needs importers or scripts (not provided) | **Optional / later.** Without it, record "not tested" for Arm 2, not "passed" |
| **3** | Claude + the `arm3_evidence` tables added to the same files | Your Claude account | **To run** |
| **4** | Your own manual analysis, no LLM, using the CSVs and Arm 3 tables | You | **To run** (quality ceiling and time measurement) |

## Order of work (suggested hours)
1. **Freeze the pre-registration** (1 h): read `PRE_REGISTRATION.md`, adjust anything you disagree with, **commit it with the date**, then do not change it.
2. **Do not open `answer_key/`.** Shuffle/rename outputs when scoring so the scorer does not know which arm produced which (a second person scoring is better).
3. **Arm 1 on A** (≈ 3 h): run P1 (plain) and P1e (evidence-style), then P2 (cash) and P2e. Save full outputs and note the tool version and date.
4. **Arm 1 on C** (≈ 1 h): P1 and P1e on the control.
5. **Arm 3 on A and C** (≈ 3 h): same prompts with the evidence tables attached.
6. **Arm 4** (≈ 6 h): do it yourself, time it, write the case file in the template from `../04` §4.2.
7. **Arm 2** only if you can set up live sandboxes within the remaining hours (≈ 8 h).
8. **Score** (≈ 3 h) with the rubric and `scoring_sheet.csv`, then open `answer_key/`.
9. **Decide** using the rule in `PRE_REGISTRATION.md` and write a dated memo (≈ 1 h).

## What a result does and does not mean
- If an existing tool is acceptable on **≥ 2 of 3** scenarios → stop the software path (decision D).
- If Arms 1 (and 2, if run) fail but Arm 3 passes → the value may lie in the **evidence layer** (deterministic tables + lineage + abstention), not in a new analyst.
- Caveats: the data are clean and small (≈ $0.5M/yr illustrative scale; judge percentages and ratios, not dollars); real businesses are messier; tools change quickly (record versions and dates); a pass on synthetic data is not demand; Arm 4 is you, not a product.

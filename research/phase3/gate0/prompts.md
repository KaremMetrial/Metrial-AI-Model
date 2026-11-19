# Gate 0 — Prompts

Use these exactly. Attach the files named for each arm. Start a **fresh conversation** for every run. Do not add hints. Do not paste anything from `answer_key/`.

**Files — Arms 1 and 2:** `data/A/*.csv` (or `data/C/*.csv` for the control).
**Files — Arm 3:** the same CSVs **plus** `arm3_evidence/A/*.csv` (or `arm3_evidence/C/*.csv`).
Data dictionary to include once with each run (copy as-is):
> These are exports for a fictional specialty-food brand selling on Shopify (DTC) and to wholesale customers. `shopify_order_lines.csv` has one row per order line (qty, list price, discount rate, net unit price, refund_rate 1.0 = refunded). `shipping_costs.csv` has shipping charged and carrier cost per order. `supplier_bills.csv` has supplier bills with unit cost by SKU and date. `wholesale_invoices.csv` has wholesale invoices with due and paid dates (blank-free; paid dates after 2026-10-31 mean unpaid at the as-of date). `shopify_products.csv` has Shopify's recorded unit cost (blank where not entered). `quickbooks_pnl_monthly.csv` has the monthly P&L. Today is 2026-11-01.

## P1 — Margin, plain (dataset A and dataset C)
> Gross margin fell in October 2026 compared with September 2026. Why? Use the files.

## P1e — Margin, evidence-style (dataset A and dataset C)
> Gross margin fell in October 2026 compared with September 2026. Explain why using only the files. For each reason: show the numbers and the records (order, bill or invoice IDs) that support it, say how large the effect is, and say what evidence argues against it. List what you could not check. Give your confidence in the observation and, separately, in the explanation, with reasons. If the data does not support a cause, say so.

## P2 — Cash, plain (dataset A)
> Cash feels tight. Why? Look at the receivables.

## P2e — Cash, evidence-style (dataset A)
> Cash feels tight. Using only the files, explain what changed in how customers pay. Name specific customers if relevant, show the days-to-pay before and after with invoice IDs, estimate the amount past due as of 2026-11-01, say what evidence argues against your explanation, and list what you could not check. Give your confidence in the observation and, separately, in the explanation, with reasons.

## Arm 4 (manual, no LLM)
Use the CSVs and the Arm 3 tables. Produce one case file per scenario in the template from `../04_validation_experiment_redesign.md` §4.2 (headline; what we are sure of; what we think explains it; evidence; counterevidence; what we could not check; dollar range; recommended actions; follow-up). Time every task.

## Recording
For each run save: arm, scenario, prompt ID, date, product and version, the complete output, and the hours spent. Do not edit outputs.

# 04 — Validation Experiment Redesign

Every hour, price, probability and timeline below is an **assumption** unless a source is named. No one has been contacted; nothing here has been run. Nothing in this plan requires production code: the scan uses throwaway scripts and spreadsheets.

## 1. Design comparison

| | **A. Paid diagnostic before results** (Phase 2 design) | **B. Free/low-cost initial diagnostic → paid investigation** | **C. Paid, manually assisted pilot with a clear deliverable and measurable outcome** |
|---|---|---|---|
| **Acquisition difficulty** | Very high: strangers must prepay | High but lower: the first step asks for exports, not money | High: needs warm introductions to land a $750–$2,000 commitment |
| **Trust required** | Highest (data + money + unknown seller + no output seen) | Medium (exports only; bounded free output; money asked after seeing observation-level value) | Medium-high (money up front, or 50/50) |
| **Time to first customer** | 3–6 weeks (cold); likely 0 in Q4 | First scans 2–3 weeks after launch; first paid 4–6 weeks | 4–8 weeks (warm intros) |
| **Founder hours** | 130–200 (bottom-up 127–207) | 95–120 (scripts and target list ≈ 30–35 h once; scan ≤ 1.5 h each; investigation 8–16 h each, ≈ 3 maximum within the cap) | 120–200 (16–30 h per pilot) |
| **Data access** | Exports or QBO login + Shopify | Three exports (Shopify orders/products with cost; QuickBooks P&L by month + A/R aging + sales by product; supplier cost list optional) | Same exports + 30-day follow-up data |
| **Delivery cost** | 8–28 h per audit ($440–$1,540 at $55/h) | Scan ≈ $80; investigation 8–16 h | 16–30 h per pilot |
| **Revenue potential** | $500–$1,500 per audit; ≈ $2–6K total | $750–$2,000 per paid investigation; plus recurring-plan commitments | $1,500–$5,000 or setup + $299/mo |
| **What we learn** | Willingness to pay *at maximum trust friction*; ambiguous on failure | **Separates trust from value:** data willingness (cost coverage), scan→paid conversion, which finding they pay to investigate, whether detection alone is enough | Value, retention intent, outcome; but small n and relies on warm intros |
| **Main failure modes** | 0–2 payers uninterpretable; consulting signal only; pools cohorts; Q4 | Free-riders (take the scan, do not pay); scan may duplicate free Shopify apps; scripts take longer than planned; scan quality reads as "just detection" | Selection (friends); consulting not software; too few pilots to decide |

## 2. Recommendation: **Design B, structured so its second step is a C-style fixed-scope paid pilot**

Why B: it is the only design that lets a *failure* be interpreted (did they refuse to share data, to pay, or did the scan alone satisfy them?), it keeps the free work scripted and bounded so it cannot become unpaid consulting, it generates the re-runnable scripts that a software product needs, and it fits a team with strong backend skills and no brand. A is rejected (see `00`). C is the right *second* phase if B produces payers.

## 3. Gate 0 — before any customer contact (≤ 25 hours, $0 beyond tools you already use)

**Purpose:** find out whether an existing tool already delivers an acceptable explanation, and whether the value is an *evidence layer* rather than an *analyst*.

**Setup:** a Shopify development store and a QuickBooks sandbox company (no cost; confirm sandbox AI features exist — QuickBooks AI may not run on sandbox data) seeded with synthetic data and **three scenarios with known ground truth**:
1. **Margin:** a supplier cost increase on two SKUs for six weeks with prices flat, a mix shift toward discounted bundles, and a freight cost rise.
2. **Cash:** two large customers drifting from 30 to 58 days to pay, plus one overdue cluster.
3. **Control:** a margin change with **no cause present in the data** (to test abstention).

**Arms (same question, same data):**
- Arm 1 — **Claude for Small Business** (Shopify + QuickBooks connectors, the plugin skills) asked "why did gross margin fall in October?" and "why did cash get tight?".
- Arm 2 — **Intuit's AI report insights/chat** and **Shopify Sidekick** on the same data (to the extent sandboxes allow).
- Arm 3 — **Claude + hand-prepared deterministic evidence tables** (a price/cost/mix/discount/freight bridge, aging tables, coverage %, with row IDs), simulating what our product would supply.
- Arm 4 — **our manual method** (you, no LLM), as the quality ceiling.

**Pre-register "acceptable"** (write before running): names the seeded primary driver; magnitude within ±20% of truth; cites rows or invoices that can be checked; states at least one thing it could not check; abstains or flags low confidence on the control.

**Decision:**
- If Arm 1 or 2 is acceptable on ≥ 2 of 3 scenarios → **stop the software path (D)**, or at most consider a services niche; explanation is already commoditised.
- If Arm 1/2 fail but Arm 3 is acceptable → the product is an **evidence layer for LLM tools** (deterministic bridges, lineage, abstention). Continue to Stage 1 *and* note the MCP/plugin distribution option (`06`, `07`).
- If Arms 1–3 all fail on ≥ 2 of 3 → either the data/problem is harder than assumed or the method needs work; do not proceed to customers until Arm 4 passes.
**Caveats:** synthetic data is cleaner than real data; the test measures the tools, not demand; results age quickly as tools update — record dates and versions.

## 4. Stage 1 — the free-scan → paid-investigation ladder (customer-facing; start after the holidays)

### 4.1 What the prospect receives, free (the **Scan**)
Capped at **≤ 90 minutes of founder time per prospect, mostly scripted**; one scan per business.
Content (observation-level only):
1. **Data readiness:** months of history; **cost coverage %** (share of revenue with a known unit cost); SKU/customer matching problems; reconciliation of Shopify revenue to the ledger within tolerance.
2. **Facts:** a two-period gross-margin bridge at the granularity the data supports (price / mix / discount / freight / refunds, with an explicit unexplained residual); AR aging with late-payer list; top three anomalies with dollars and the rows behind them.
3. **Open questions:** what the scan *could not* determine.
**It never contains:** root-cause conclusions, recommendations, or a ranked hypothesis list. Those are the paid product.
**Why this is not free consulting:** it is largely produced by a re-runnable script; it is bounded in time; it stops at observations that Shopify apps and QuickBooks reports already provide in part, so the hook is *detection plus honesty about gaps*, and the paid step is *explanation*. If the scan alone satisfies buyers, that is itself the finding (detection is enough, explanation is not paid for).

### 4.2 What the customer receives, paid (the **Investigation**)
**Price:** **$750** for the Shopify-with-wholesale cohort; **$2,000** for the distributor cohort via introductions only. One price per cohort; no tiers.
**Terms:** 100% up front at $750 (card); 50% up front / 50% on delivery at $2,000. **Refund only for non-delivery** (if the deliverable specified below is not delivered within 15 business days of complete data) — not for dissatisfaction, to keep the signal clean. **Keep the output.** If they subscribe within 30 days, **credit the fee toward month one**.
**Deliverable:**
- up to **two investigated findings** as case files: headline; what we are sure of; what we think explains it (≤3 hypotheses, ranked as best-supported / possible / ruled out); evidence with source and date; **counterevidence directly under each hypothesis**; what we could not check; dollar range; recommended actions including "do nothing" with its cost;
- an **evidence appendix** tracing every number to rows or invoices;
- a 30-minute walkthrough;
- a **30-day follow-up check** by email: did the proposed action happen, did the metric move (improved / no change / worse / cannot tell), labelled "followed by", not "caused by".
**Timeline:** delivered within 10 business days of receiving complete exports.

### 4.3 Data we require
Shopify: orders (12–24 months if available), products with cost per item, refunds, payouts. QuickBooks: P&L by month (class/location if used), A/R aging, sales by product/service, bills by vendor, inventory valuation if used. Optional: supplier price list. **Exports or customer-run reports only; no logins; no stored credentials.** Data stays in an encrypted folder; deleted within 30 days of delivery or on request; never used to train models; a one-page written note says so.

### 4.4 What we will NOT promise
Dollar savings; certainty of cause (we state evidence grade and abstain when the data cannot support a cause); tax, legal or accounting advice; implementation of changes; pricing or purchasing decisions made for them; ongoing monitoring (unless they subscribe); any outcome attributable to our work ("followed by", not "caused by").

### 4.5 How the customer evaluates the result
A pre-agreed one-page rubric given **before** payment: (1) every number traceable to a row; (2) coverage and limits stated; (3) counterevidence shown; (4) at least one finding they did not already know; (5) at least one action they can take in 14 days. At delivery, the customer scores 1–5 on each and answers two questions: "How disappointed would you be if you could not get this again?" and "Would you commit to a weekly Brief at $299/month starting within 30 days?" **Blind comparison** (see `05`): the same finding compared with what their own tools produce, anonymised.

## 5. Cohorts (never pooled)
| Cohort | Who | How found | Price | Role in the decision |
|---|---|---|---|---|
| **S — Shopify + wholesale, $2–20M** | Founders/ops leads | Hand-built list; owner outreach; accountant introductions; credibility content (no community pitching) | $750 | Primary cohort for the sequential test |
| **D — Distributors, $10–75M** | CFO/controller; pricing lead | Introductions via ERP resellers, trade-association contacts, accountants | $2,000 | Run only with warm introductions; **5–8 paid investigations or 8–10 interviews; not pooled with S** |
| **A — Accountants/fractional CFOs** | The firm | Direct outreach (unavoidable) | none | **Qualitative only** — their willingness to refer, resell, and what they would pay per client; never counted toward the payer rule |

## 6. Timeline (proposed dates)
| Dates | Activity | Hours |
|---|---|---|
| Nov 20 – Dec 5 | **Gate 0** and primary-term reading (Xero, Intuit, Shopify); allow blocked hosts for reruns | ≤ 25 |
| Dec 5 – Dec 8 | Go/no-go on Gate 0; commit prior, cash floor and draw in writing | 2 |
| Dec 8 – Dec 22 | Non-selling discovery conversations (8–10: accountants, bookkeepers, two or three owners), build the target list (≥ 60 named businesses) and the scan scripts | ≤ 35 |
| Jan 5 – Feb 6 | Scans (up to ≈ 14 qualified recipients at ≤ 1.5 h each; more only if hours remain) | ≤ 20 |
| Jan 12 – Feb 20 | Paid investigations and 30-day follow-ups (≈ 3 at 8–12 h; **stop accepting new investigations when this budget is spent**) | ≤ 35 |
| By Mar 2 | Decision memo; apply `08` rules | ≤ 5 |
**Total ≤ 120 hours (Gate 0 25 + Stage 1 95); ≤ $400 cash; ≤ 10 weeks.** If the hours budget limits the number of paid investigations before the sequential test can conclude, record the verdict as "capped by hours" — not as success or failure.

## 7. Stopping rules
- **Futility:** 0 payers among the first 9 qualified recipients (cohort S).
- **Success (sequential):** payers/non-payers cross the +2.20 boundary (e.g., 2 payers and 0 non-payers; 3 payers with ≤ 4 non-payers; 4 with ≤ 8; 5 with ≤ 13), then require the tripwires in `05`.
- **Cap:** 25 qualified recipients or 95 hours of Stage 1, whichever comes first.
- **"Not run":** fewer than 10 qualified recipients after six weeks of effort → report "not run", not "failed", and decide whether reach (not demand) is the problem.
- **Early evidence stop:** if 5 of the first 10 conversations say a free in-product tool already answers their question, stop.

## 8. Failure modes of the redesign and mitigations
| Failure mode | Mitigation |
|---|---|
| Scan satisfies them; nobody pays | Treat as a finding (detection is enough); try the $149–$299 "data review" arm in a later cycle |
| Scripts take > 30 hours | Cap; scan by hand on the first five and script only what repeats |
| Free-riders collect scans | One scan per business; no causes or actions in the scan; require exports; log every non-payer's reason |
| Few qualified recipients | "Not run" verdict; add accountant introductions; defer the distributor cohort |
| Sandbox AI differs from real data | Re-run Gate 0 arms on the first real (consented) data and compare |
| Signal contamination | Pre-register rules; do not discount to reach a threshold; do not count friends unless they would have been qualified strangers |
| Legal/ethics | Written terms; no tax/legal/accounting advice; delete data on request; do not store credentials; check local requirements for engagement terms |

# 06 — Preliminary Pricing and Unit Economics

**Separation of facts and assumptions.** *Verified/sourced market prices* (all from search summaries or aggregators; conflicts noted) are in §1. *Every number in §2–§4 is an ASSUMPTION.* Calculations come from a small script (`appendix/p2_econ_model.py` in this folder's appendix) and are reproduced below. Phase 1's cost model (`research/appendix/agent6_economics.md`) is the base; Phase 2 adjusts onboarding hours using Agent 5 and prices using Agents 1, 3A, 3B and 4.

## 1. Market price anchors (sourced; reliability varies)

| Category | Price evidence | Reliability |
|---|---|---|
| Shopify profit/analytics apps | TrueProfit $35–$200/mo by orders; Lifetimely free <50 orders, from $49; Setpilot $29.99; Profit Pulse AI $19; BeProfit $25–249 (conflicting); Triple Whale ≈ $219+ (competitor pages); Polar ≈ $300–720 (Phase 1, conflicting) | Listings via search; aggregator conflicts |
| Cash/AR tools | Chaser ≈ $259/mo (Capterra); Float/Fathom $29–$860 (range across tiers); A2X $29–$169 | Aggregators |
| Accountant-led reporting | Fathom ≈ $50+ (conflicting), ≈ $450/mo for 25 companies (≈ $18/client) | Provisional pricing page via search |
| Distributor margin/pricing | Vendavo ≈ $75K/yr floor (one comparison site); Pricefx ≈ $50K/yr floor; Phocas listing $150/mo (unreliable) | Single-source estimates |
| ERP AI | NetSuite ≈ $129–199/user/mo + base fee; AI metered by "AI Units" | Estimates |
| Recovery products | Parcel audit 25–50% contingency; deductions ≈ 25%; FBA reimbursement 10–25%; AP recovery 13.5–25% | Vendor-quoted |
| Consulting | Distribution consultants $150–$600/hr, $5–20K/mo (generic vendor blog) | Weak |
| Fractional CFO | $3–12K/mo typical; light retainers $1.4–3K/mo | Sellers of these services |

**No SMB willingness-to-pay data exists for a $349–$999 margin/cash *explanation* product.** The anchors say: owners swipe a card at $50–$760/mo; mid-market FP&A buys at $25–$80K/yr; services price on outcomes.

## 2. Pricing hypotheses by model

| Model | Fit | Evidence | Verdict for first 30–90 days |
|---|---|---|---|
| **Paid pilot / paid diagnostic (one-time $500–$1,500)** | Tests willingness to pay directly; funds human time | Pass/fail signal recommended in Agent 1: ≥4 of 15 pay before seeing results | **Use first** |
| Setup fee ($750–$2,500) + monthly | Offsets 8–28 onboarding hours | Phase 1; onboarding hours from Agent 5 | Use once audits convert |
| Monthly subscription | Recurring revenue | $49–$760 clusters for SaaS analytics; $349+ unproven | Test $199–$399 first, $799 only after documented dollar wins |
| Service-assisted onboarding | Needed for margin (data cleanup) | A5: 10–28 h | Required, price it |
| Usage-based (per investigation) | Aligns with cost | LLM cost is 1–4% of price; metering adds friction | Avoid as the headline metric; cap allowance instead |
| Outcome-based (platform fee + 10–15% of verified savings, capped) | Matches recovery-market norms | Contingency norm 10–50% in recovery categories; attribution disputes | Offer only after 3–5 documented wins |

## 3. Cost to serve (assumptions, with inputs)

Inputs: analyst/support time $55/hour loaded; LLM cost per grounded investigation $0.15 / $0.30 / $0.45 (optimistic / base / conservative) from Phase 1's token model (Sonnet-class prices from aggregators; verify against vendor pages); infra/warehouse per tenant $10–$60/mo; per-tenant connector variable cost (Xero egress, Intuit credits, unified API) $5–$20/mo; connector maintenance ≈ 1 engineer-week per source per quarter (fixed, in team cost); security/SOC 2 deferred (Phase 1: $15–$60K first year when required). Team cost for break-even: **$13.5K/month** (2 people × $6K loaded + $1.5K tools) — a lean, founder-subsidized team.

### Margin investigation (service-assisted)

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Monthly price | $199 | $399 | $799 |
| Setup fee | $750 | $1,500 | $2,500 |
| Investigations/mo × cost | 40 × $0.45 = $18 | 30 × $0.30 = $9 | 20 × $0.15 = $3 |
| Infra + connectors | $80 | $55 | $40 |
| CS + validation hours/mo | 4 h = $220 | 2.5 h = $138 | 1.5 h = $82 |
| **Variable cost** | $318 | $202 | $126 |
| **Contribution/mo** | **−$119** | **$198 (49.5% GM)** | **$674 (84.3% GM)** |
| Onboarding hours | 28 h ($1,540) | 16 h ($880) | 8 h ($440) |
| Net of setup fee | −$790 | +$620 | +$2,060 |
| CAC (concierge/relationship) | $3,000 | $1,800 | $900 |
| Contribution payback | never | 9.1 months | 1.3 months |
| **Customers to cover $13.5K/mo team** | never | **~68** | **~20** |

### Cash/AR investigation (near self-serve)

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Monthly price | $99 | $199 | $349 |
| Setup fee | $0 | $0 | $0 |
| Investigations/mo × cost | 20 × $0.45 = $9 | 20 × $0.30 = $6 | 15 × $0.15 = $2 |
| Infra + connectors | $40 | $25 | $15 |
| CS hours/mo | 1 h = $55 | 0.5 h = $28 | 0.25 h = $14 |
| **Variable cost** | $104 | $59 | $31 |
| **Contribution/mo** | **−$5** | **$141 (70.6% GM)** | **$318 (91.1% GM)** |
| Onboarding hours | 3 h | 1.5 h | 0.5 h |
| CAC (inbound/partner) | $1,500 | $800 | $400 |
| Payback | never | 6.3 months | 1.3 months |
| **Customers to cover $13.5K/mo** | never | **~96** | **~42** |

## 4. What the numbers say
1. **LLM inference is irrelevant to the decision** ($2–$18 per customer per month); humans and price decide viability — same conclusion as Phase 1.
2. **Margin needs price ≥ ~$400/mo or onboarding ≤ ~16 h** to break even; at $199 it loses money. Evidence supports $35–$300 for self-serve apps and **nothing yet at $349+**. The product therefore depends on the single least-validated assumption in the research.
3. **Cash/AR can be profitable at $199** because onboarding is hours — but 96 customers at base is a distribution problem against crowded, bundled incumbents; CAC of $800 inbound is an assumption with no evidence.
4. **The concierge audit is itself revenue**: $500–$1,500 × 15 prospects at a 27% conversion (4 buyers) is ~$2–6K — it will not fund the team but offsets cost and, more importantly, measures price.
5. **Runway:** at 5–20 customers any scenario loses money at full salaries (Phase 1: roughly $250–$450K to reach ~20 customers; ~half if founders draw $4–5K). Choose the founders' draw before the test so the kill criteria include a cash trigger.
6. **Sensitivity (unit contribution):** price ±$200 ≈ ±$200; CS load per customer halves/doubles contribution; onboarding hours matter via setup-fee offset; LLM cost ×3 ≈ −$36.

## 5. Sourced vs assumed — quick map
- **Sourced (weak):** market prices in §1; LLM prices (aggregators); Xero/Intuit/Shopify fees as reported.
- **Assumed:** every price proposed for our product, setup fees, onboarding/CS hours, CAC, churn, team cost, infra and connector costs, all contribution and break-even figures.

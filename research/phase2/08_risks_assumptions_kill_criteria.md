# 08 — Risks, Assumptions and Kill Criteria

## 1. Assumptions that must be proven (ranked by how much of the decision rests on them)

| # | Assumption | Current evidence | Cheapest test | Pass signal |
|---|---|---|---|---|
| 1 | Small and mid-sized product businesses will **pay** for an explanation (not just visibility, sync or recovery) | None at $349–$999; $35–$300 for visibility; contingency for recovery | Paid audit, payment before results | ≥ 4/15 pay ≥ $500 |
| 2 | The case file is **better than the in-product AI** they already have (Intuit, Shopify, NetSuite, Claude) | Differentiation PARTIAL; nobody documents confidence/counterevidence; no blind test | Blind comparison in every audit | Clear majority prefer |
| 3 | Onboarding is cheap enough: ≤ 8 human hours; cost-coverage usable | Agent 5: 10–28 h margin; Shopify `unitCost` optional/current-only | Time every audit; measure coverage on 10 merchants | Median ≤ 8 h; ≥ 60% usable |
| 4 | Explanations are **right** ≥ 70% and abstention works | No SMB-volume RCA precision evidence exists | Owner-confirmed labels | ≥ 70% on confirmed cases |
| 5 | Owners/controllers grant read access to an unknown vendor | No evidence | Count grants vs refusals | ≥ 8/10 grant with light review |
| 6 | Buyer and approver are identifiable and not blocked by sales | No budget-owner survey | Ask "who approves $500/$400 per month?" | Consistent answer |
| 7 | A trigger exists now (cost shock, wholesale launch, lender request) | Tariffs documented; durability unverified | Ask "what changed in the last 90 days?" | Specific events, not generalities |
| 8 | Accountants/fractional CFOs will introduce clients or resell | 94% offer advisory; tool-consolidation intent; price anchor $18/client | 10 approaches, 3–5 pilots | ≥ 3 pilots |
| 9 | Distributors truly fail to pass through costs (ICP-2) | Surveys say they pass through | 5–8 interviews; read full surveys | Unprompted dollar examples |
| 10 | Platform terms allow the planned data use | Xero AI-training clause reported; Shopify 60-day default; Intuit review | Read primaries | No blocking clause |

## 2. Risk register

| Risk | Likelihood / severity [J] | Evidence | Mitigation |
|---|---|---|---|
| **No WTP for explanation** | High / fatal | Agents 1, 3A, 3B all find none | Paid test first; kill rule |
| **Free in-product AI absorbs the use case** (Intuit Intelligence, Xero JAX, Shopify Sidekick Pulse, NetSuite Ask Oracle, Claude for Small Business) | High / fatal | Phase 1 + Agents 2, 3A | Blind comparison; cross-system focus; verticalize; move fast |
| Onboarding = data cleaning; margin collapses into services | High / severe | Agent 5; Phase 1 | Cap hours; coverage badge; price setup fee; automate only repeated steps |
| Spurious/confident wrong explanations erode trust | Medium-high / severe | Phase 1 devil's advocate; A5 AI-misleads list | Deterministic numbers; abstention; seeded-error tests; evidence grades |
| Cost data missing (Shopify `unitCost`, SKU-level QBO/Xero) | High / moderate | Agent 5 | Cost-coverage metric; customer cost-upload step; revenue-side bridge first |
| Distributor premise weak (they already pass through) | Medium / moderate | DSG, Baird-NAW | Interviews; focus on *not knowing whether* they did |
| Inbound cannot reach the paying segment | High / moderate | Agent 4 | Two-track design; accountant channel |
| Platform-terms and API-change churn | Medium / moderate | Xero tiers, Shopify app changes | Read primaries; unlisted pilots; monitor + reconnect UX; ~1 eng-week/source/quarter |
| Tariff urgency fades | Medium / moderate | One unverified trade-press title | Ask for recent trigger events; keep trigger-agnostic framing |
| Security/trust barrier for unknown vendor | Medium / moderate | Phase 1 | Read-only; exports first; data-handling note; SOC 2 only when procurement asks |
| Consolidation/acquirers make independence hard | Medium / low-moderate | Conjura, Peak, Sisu | Treat acquisition as plausible exit; avoid over-investment |
| Founder runway exhausted before signal | Medium / severe | Phase 1 model: loses money at 5–20 customers | Set a draw and a cash floor now; tie to kill criteria |
| Research bias (confirmation) | Medium / moderate | This research began with a hypothesis | Pre-registered thresholds; document contradictions; blind tests |

## 3. Kill criteria (any one triggers stop or a re-pick; decide before starting)

**Market:** fewer than 2 of 15 qualified prospects pay; owners rate the case file no better than in-product/Claude output; 5 of the first 10 conversations say free tools suffice.
**Economics:** median onboarding > ~12 hours; cost coverage < ~40% for most customers; at the accepted price the contribution turns negative at 4 CS+validation hours per customer-month.
**Quality:** owner-confirmed explanation accuracy < ~60%; abstention fails (confident wrong answers on injected "no-cause" cases).
**Access:** most prospects refuse exports/read-only access without a heavy security review.
**Platform:** primary terms forbid the planned processing (e.g., Xero AI clause matters for the chosen design) or in-product vendors ship persistent cross-source margin/cash investigation that customers confirm removes their gap.
**Cash:** founders hit the pre-agreed cash floor before conditions are met.

## 4. What would change this recommendation
- **Upgrade to A:** ≥ 4/15 pay for margin findings and margin is the most-valued type.
- **Upgrade to B (cash/AR or reconciliation):** payers act first on those findings.
- **Re-pick the market:** T1 fails on price but ≥ 3 distributors show clear dollar pain and a budget owner.
- **Downgrade to stop:** any kill criterion above.

## 5. Contradictory evidence kept in view
- Distributors say they pass costs through; small firms buy fewer pricing tools (27% vs 55%).
- Cheap tools already cover visibility; an exception queue exists at $19.
- Where WTP is proven (recovery, reconciliation), the fields are saturated; one brand built its own audit agent with off-the-shelf AI and recoveries decayed.
- Absence of documented confidence/outcome features is not proof customers value them.
- Cash/AR has the best data and onboarding but is the likeliest to be bundled for free.

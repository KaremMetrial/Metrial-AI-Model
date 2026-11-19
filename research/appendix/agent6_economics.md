# Agent 6: Business Model and Economics (as of 2026-11-19)

**Labels:** [S] = sourced (URL given; note most are third-party aggregators, because vendor pages were mostly unreachable from this environment, and docs.anthropic.com did not resolve). [A] = my assumption. Where sources conflict I say so. The model script is at `/tmp/claude-0/-home-user-Metrial-AI-Model/828ffc9c-3701-528d-931a-29cfd311c092/scratchpad/model.py`.

## 0. Bottom line

1. **LLM cost is not the problem.** A computation-grounded investigation costs about $0.10-0.26 in tokens [A, built on S prices]. At 50-80 investigations per customer per month that is $5-20, or 1-4% of a ~$900 plan. Do not price per token.
2. **Humans are the cost.** Onboarding, data-source wrangling, validating findings, and customer success are 70-85% of COGS in my model. This is a services-heavy business at first. Price accordingly (setup fee plus a plan large enough to fund human review).
3. **Price floor:** below roughly $600/month blended, gross margin goes negative once human review is included. Base case ($900) gives about 55% gross margin; optimistic ($1,500 with automation) about 82%.
4. **A 2-3 person team needs about 55-80 customers at $900/month** (base) or about 22-31 at $1,500. In the conservative case ($450) it never breaks even. See section 6.
5. **For the first 20 customers: high-touch, "SaaS-enabled service."** Sell a productized recurring service, charge a setup fee, and automate only what you have done by hand 10 times.

---

## 1. Comparable pricing evidence

| Category / vendor | Price | Label / source |
|---|---|---|
| ThoughtSpot Essentials | $25/user/mo, 5-user minimum, 25M row cap | S, conflicting third-party: [Toucan](https://www.toucantoco.com/en/blog/thoughtspot-pricing), [Querio](https://querio.ai/articles/thoughtspot-pricing-explained) |
| ThoughtSpot Pro | $50/user/mo (embedded flat) or $0.10/credit consumption; Spotter AI capped at 25 queries/user/mo; CostBench estimates $150-250/user, which conflicts | S: [Knowi](https://www.knowi.com/blog/thoughtspot-pricing/), [CostBench](https://www.costbench.com/software/business-intelligence/thoughtspot/) |
| Power BI Pro / PPU | $14 / $24 per user/mo (raised from $10 in Apr 2025) | S: [Knowi](https://www.knowi.com/blog/power-bi-pricing-2026/), [Perceptive](https://www.perceptive-analytics.com/?p=13057) |
| Tableau Cloud Standard | Creator $75, Explorer $42, Viewer $15 per user/mo; Enterprise $115/$70/$35 | S: [Coefficient](https://coefficient.io/tableau-pricing) |
| Fathom (financial reporting) | $53 (1 co.) to $720 (50 cos.) per month; one aggregator says Pro $450/mo flat | S, conflicting: [G2](https://www.g2.com/products/fathom/pricing), [Toolradar](https://toolradar.com/tools/fathom-ai/pricing.md) |
| Jirav | About $10k-15k/yr (Eightx est.); Toolradar's $50/mo conflicts, so unverified | S: [Eightx](https://eightx.co/blog/fathom-vs-jirav-vs-liveflow-reporting) |
| Syft | About $35/org/mo, unclear attribution | S, weak: [G2](https://www.g2.com/products/syft-analytics-syft/pricing) |
| Inventory Planner (Sage) | Quote-based; third-party about $250/mo base plus $80/warehouse, $15 per 1,000 SKUs over 1,000 | S, conflicting: [Prediko comparison](https://prediko.io/inventory-planner-vs-cogsy-vs-prediko) |
| Cogsy | $199/mo flat (a $49 tier not selectable per one review) | S: [Eightx](https://eightx.co/blog/compare/how-much-does-cogsy-cost) |
| Prediko | From $49/mo (<$100k GMV), tiers about $119/$199/$349 by GMV | S: [Capterra](https://www.capterra.com/p/10025153/Prediko) |
| Glean | About $50-75/user/mo, about 100-seat minimum (about $60k/yr), possible +$15 AI add-on | S, buyer-reported: [eesel](https://www.eesel.ai/blog/glean-pricing), [GoSearch](https://www.gosearch.ai/blog/glean-pricing-explained) |
| Zenlytic | Quote-based, no public price | S: [Toolradar](https://toolradar.com/tools/zenlytic/pricing) |
| Narrative BI, Dust, Anodot | **No reliable public pricing found** | Not found; treat as quote-based |
| Datadog | Infra Pro $15/host/mo (annual), APM $31/host, logs $0.10/GB ingest plus indexing | S: [SigNoz](https://signoz.io/blog/datadog-pricing/), [OpenObserve](https://openobserve.ai/blog/datadog-pricing/) |
| Fractional CFO | $3k-12k/mo typical ($5k-10k common); light/early-stage $1.4k-3k/mo; $175-500/hr | S: [Pilot](https://pilot.com/blog/fractional-cfo-hourly-rates), [JRG](https://jrgpartners.com/what-fractional-cfo-costs-use-cases-when-hire-one), [Eightx](https://eightx.co/blog/fractional-cfo-cost-pricing-guide) (sellers of these services) |

**What this tells us**
- **Per-seat BI is cheap** ($14-75/seat) because it sells tooling, not outcomes. A 10-person management team costs about $150-750/mo on Power BI/Tableau. Our product must not be priced as "another dashboard seat."
- **Vertical single-purpose SMB tools cluster at $50-400/mo** (Prediko, Cogsy, Fathom, Syft). That is the price anchor for a self-serve buyer, and it caps self-serve ARPA near $2-5k/yr.
- **Higher willingness to pay exists where the product replaces human judgment:** Jirav ($10-15k/yr), fractional CFO ($36-120k/yr), Glean (>$60k/yr). A product that credibly delivers a slice of a part-time analyst/CFO can land at **$6-18k/yr**, roughly 10-25% of a fractional CFO retainer. [A]
- Light-retainer fractional CFO at $1.4-3k/mo is the realistic substitute at the low end. Our Growth tier should sit below it and promise a distinct deliverable (continuous monitoring, not monthly meetings).

---

## 2. Proposed packaging (not per token, not per seat)

Pricing metric: **"monitored entities x connected sources" with an investigation allowance**, because those are what drive onboarding labor and compute. Seats are unlimited. [A, all prices]

| | **Starter** | **Growth** | **Scale / Enterprise** |
|---|---|---|---|
| Target | $2-10M revenue, one business line | $10-75M revenue, 2-5 entities/locations | $75-200M, multi-entity, finance team exists |
| Monthly price | **$349** | **$999** | **$2,500-6,000** (custom) |
| Annual prepay | $3,490 (2 months free) | $9,990 | $30k-72k |
| Connected sources | 3 | 10 | Unlimited (fair use) |
| Entities | 1 | 5 | Custom |
| Investigations/mo (auto, grounded) | 20 | 100 | 400+ |
| Human-reviewed "analyst notes" | Quarterly | Monthly (30 min) | Bi-weekly plus named analyst |
| Decision and outcome tracking | Basic log | Full, with outcome follow-up | Full plus API/export |
| Security | Standard | Standard | SOC 2 report, SSO, DPA, VPC option |
| One-time setup | $1,500 | $3,500 | $7,500-15,000 |
| Overage | $8 per extra investigation | $5 | negotiated |

**Why the setup fee:** onboarding takes 8-40 hours (section 3). A setup fee turns what would be a cash-flow hole into services revenue. It also screens out unserious buyers. [A]

**Value-based option (for Growth and Scale):**
`Fee = Platform fee ($500/mo) + 10-15% of Verified Savings, capped at 2x the annual platform fee`
- "Verified Savings" = measured, customer-confirmed outcomes tied to tracked decisions (e.g., an overdue-vendor-price correction, a stockout avoided, margin leak fixed), with a baseline agreed up front and a 90-day attribution window.
- Risks: attribution disputes, long cash collection, and customers gaming baselines. Outcomes-based pricing compresses margins when costs scale with outcomes ([SoftwareSeni](https://softwareseni.com/outcomes-based-pricing-and-ai-first-saas-gross-margin-economics-explained), S but secondary). Offer only after 3-5 customers have documented savings; then use the data as the sales proof.
- Expected value [A]: if a mid-market customer has 0.5-1% of revenue recoverable (on $20M that is $100-200k/yr), 10-15% share is $10-30k/yr, comparable to the Growth subscription plus upside.

---

## 3. Cost model

### 3.1 LLM prices used

| Model | Input/Output per M tokens | Label |
|---|---|---|
| Sonnet 5 / 5.5 | $2 / $10 | S (one source says Sonnet 5 intro pricing through Aug 2026; verify): [Benchlm](https://benchlm.ai/anthropic/api-pricing), [Activepieces](https://www.activepieces.com/blog/anthropic-api-pricing-2026-cost-per-million-tokens.md) |
| Sonnet 4.6 (conservative) | $3 / $15 | S: [Finout](https://www.finout.io/blog/claude-pricing-in-2026-for-individuals-organizations-and-developers), [DEV](https://dev.to/toshanthistack/what-does-the-claude-api-actually-cost-june-2026-9mh) |
| Haiku 4.5 | $1 / $5 | S: same sources |
| Cache read | 0.1x base input; 5-min write 1.25x; 1-hour write 2x | S: [cut-the-saas](https://cut-the-saas.com/the-cut/claude-api-pricing) |
| Batch API | -50% | S: same |

I could not verify against Anthropic's own page (host blocked), and a few aggregators mix columns. **Re-check at platform.claude.com/docs/en/about-claude/pricing before relying on these.** OpenAI/Google prices were not collected; at similar mid-tier levels the conclusion (LLM is a minor cost) does not change.

### 3.2 Cost per investigation [A token counts, S prices]

Pipeline: (1) Haiku triage/summarize the detected change: 20k in, 2k out. (2) Sonnet investigation: 60k tokens context (70% cache-read), 6k out, with deterministic SQL/pandas computed outside the LLM. (3) Verification pass: 15k in, 2k out.

```
triage  = 20k*P_in_H + 2k*P_out_H
invest  = 60k*(0.3*P_in_S + 0.7*0.1*P_in_S) + 6k*P_out_S
verify  = 15k*P_in_S + 2k*P_out_S
```

| Scenario | Prices | $/investigation (calculated) |
|---|---|---|
| Conservative | Sonnet 4.6 $3/$15 | $0.26 |
| Base | Sonnet 5.5 $2/$10 | $0.18 |
| Optimistic | Batch, -50% | $0.09 |

For the customer model I **inflate base by about 1.6x to $0.30** (retries, exploration, multi-step agent loops [A]), conservative to $0.45, optimistic $0.15. Even at 5x this is under $90/customer/month.

**Evidence of margin compression, and why it does not apply as much here:** AI-native margins average about 50-60% vs 75-90% for classic SaaS; inference is often cited at about 20-23% of revenue ([CloudZero](https://www.cloudzero.com/blog/ai-gross-margin), [Monetizely](https://www.getmonetizely.com/articles/the-economics-of-ai-first-b2b-saas-in-2026-margins-pricing-models-and-profitability), [Aleph](https://www.getaleph.com/blog/2026-saas-benchmarks-takeaways)), but those are chat/agent products with heavy open-ended usage. A scheduled, bounded, computation-grounded product with an investigation cap sits far below that. Benchmarkit reportedly shows median software margin still above 80% (same Monetizely/aggregator trail; secondary). My model's low margin comes from **people**, not tokens.

### 3.3 Other per-tenant COGS (monthly) [A unless noted]

| Item | Cons | Base | Opt | Basis |
|---|---|---|---|---|
| Warehouse/DB compute and storage (Postgres/DuckDB/ClickHouse, small tenant) | $60 | $45 | $35 | Multi-tenant shared cluster; small tenants are GBs |
| Ingestion (Airbyte/Fivetran/dlt) | $40 | $30 | $25 | Fivetran has a 500k MAR free tier and about $5 minimum per connector ([Hevo](https://hevodata.com/learn/fivetran-pricing/), S, competitor source); Airbyte Cloud cheaper at low volume (S, same family); self-hosted dlt/Airbyte OSS reduces to compute |
| Observability/monitoring jobs | in infra | in infra | in infra | Allocated to fixed tools in 3.5 |
| Human validation | 0.5 hr x4 = 2 hr | 1.2 hr | 0.6 hr | $55/hr loaded analyst time, per customer per month |
| Customer success / support | 1 CSM per 25 | 1 per 40 | 1 per 60 | $10k/mo loaded per CSM |
| LLM (50-80 inv x $/inv) | $36 | $18 | $7.5 | 3.2 |

**Per-customer variable COGS (base) = 18 (LLM) + 45 + 30 + 66 (validation, 0.3 x 220) + 250 (CS) = about $409/mo.** Unit contribution before CAC = $900 - $409 = **$491/mo**.

### 3.4 Onboarding labor (realistic) [A]

| Task | Hours |
|---|---|
| Source connection, credentials, permissions | 2-6 |
| Data mapping/cleaning, entity and metric definitions (the hard part) | 6-20 |
| Threshold tuning and baseline validation with customer | 3-8 |
| First 2-3 investigations human-verified, review call | 3-6 |
| **Total** | **14-40 hrs; use 24 hrs** |

At $55/hr that is about $1,320 of labor per customer, in line with the $1,500-3,500 setup fee, so setup should about break even. In the first 20 customers the founder does it (opportunity cost, not cash).

### 3.5 Fixed costs [A unless noted]

- **SOC 2:** compliance platform about $7.5-15k/yr for a startup tier; Type 1 audit $7.5-25k; Type 2 $12-45k; total first-year about $15-60k ([Drata](https://drata.com/blog/soc-2-audit-cost), [Agency](https://blog.getagency.com/articles/how-much-does-soc-2-compliance-cost-2026), [Probo](https://www.probo.com/blog/2025-03-04-what-is-soc2-cost); S, vendor-biased, 2-3x spread). Use about $25k year one, spread as about $2k/mo. Defer Type 2 until the first Scale deal requires it; use a trust page, pen-test summary and a questionnaire pack for the first 20.
- Cloud base, observability (Datadog-class or open-source stack), error tracking, CRM, email, legal: $1.5k/mo at 5 customers, rising to $30k/mo at 500.
- Headcount, **$12k/month fully loaded average** [A] (founders can draw less early):

| Customers | Heads | Roles |
|---|---|---|
| 5 | 2 | 2 founders (eng/product + domain/sales) |
| 20 | 3 | + 1 eng/data-analyst-CS hybrid |
| 100 | 8 | 3 eng, 2 CS/analyst, 1 sales, 1 PM/ops, 1 founder-ops |
| 500 | 28 | 9 eng, 8 CS/analysts, 5 sales/marketing, 3 ops/security/finance, 3 mgmt/other |

### 3.6 CAC and sales cycle [A, benchmark-informed]

Benchmarks (all S, agency blogs, directional): SMB CAC payback 12-15 months median, top quartile 7-10 months; sales-assisted 12-19 months vs self-serve/PLG 6-11; $5-25k ACV is the "hybrid" band with acceptable CAC of $2-8k; sales cycles 30-45 days under $10k ACV, 60-120 for $10-50k; median B2B SaaS cycle 84 days ([Stealth Agents](https://stealthagents.com/research/startup-cac-payback-period-benchmarks-2026), [SaaS Hero](https://www.saashero.net/strategy/saas-cac-benchmarks-2026/), [GrowthSpree](https://www.growthspreeofficial.com/blogs/b2b-saas-cac-payback-period-benchmarks-2026-by-stage-vertical-gtm-motion.md)).

| Channel | CAC | Cycle | Notes [A] |
|---|---|---|---|
| Founder-led outbound/network | $3-6k (mostly time) | 45-90 days | First 10-20 customers |
| Partners: fractional CFOs, accountants, e-commerce/ERP consultants | $1-3k plus 15-20% rev share yr 1 | 30-60 days | Best expected channel; they already sell the pain |
| Content/SEO/community | $1.5-3k blended | 30-60 days | Slow to start (6-9 months) |
| Paid | $4-8k | 30-60 days | Poor fit at this ACV without self-serve |

Base CAC $4,000 vs base unit contribution $491/mo gives **8.1-month contribution payback** (cons: undefined, since contribution is negative; opt: $2,500 / $1,233 = 2 months).

---

## 4. Financial model: monthly P&L at 5/20/100/500 customers

Scenario inputs [A]: price $450/$900/$1,500; investigations per customer 80/60/50; monthly churn 2.5%/1.5%/1.0%. Opex = heads x $12k + fixed tools. **Excludes CAC/S&M program spend and setup-fee income** (sales headcount is included in heads; setup fees would add about $1.3-3.5k per new customer, one-time). Calculated by `model.py`.

### Conservative ($450/mo, cost-heavy)
| Customers | Revenue | COGS | Gross margin | Opex | Operating result |
|---|---|---|---|---|---|
| 5 | $2,250 | $3,230 | -44% | $25,500 | -$26.5k |
| 20 | $9,000 | $12,920 | -44% | $38,500 | -$42.4k |
| 100 | $45,000 | $64,600 | -44% | $104,000 | -$123.6k |
| 500 | $225,000 | $323,000 | -44% | $366,000 | -$464k |

The conservative case is deliberately **unviable**: it shows that $450 with 1 CSM per 25 customers cannot work. It is the failure mode if you underprice a human-heavy product.

### Base ($900/mo)
| Customers | Revenue | COGS (LLM / infra+ingest / validation / CS) | Gross margin | Opex | Operating result |
|---|---|---|---|---|---|
| 5 | $4,500 | $2,045 ($90 / $375 / $330 / $1,250) | 54.6% | $25,500 | -$23.0k |
| 20 | $18,000 | $8,180 ($360 / $1,500 / $1,320 / $5,000) | 54.6% | $38,500 | -$28.7k |
| 100 | $90,000 | $40,900 ($1,800 / $7,500 / $6,600 / $25,000) | 54.6% | $104,000 | -$54.9k |
| 500 | $450,000 | $204,500 ($9k / $37.5k / $33k / $125k) | 54.6% | $366,000 | -$120.5k |

Break-even at the stated headcount ladder: **about 212 customers (about $190k MRR)**. Base never looks good at 100 because I hired 8 people; hiring should lag revenue, and the 28-person team at 500 is oversized for $450k MRR (about $5.4M ARR). A leaner ladder (revenue per head about $15-20k MRR) would be profitable around 100-150 customers.

### Optimistic ($1,500/mo, automated validation)
| Customers | Revenue | COGS | Gross margin | Opex | Operating result |
|---|---|---|---|---|---|
| 5 | $7,500 | $1,336 | 82.2% | $25,500 | -$19.3k |
| 20 | $30,000 | $5,343 | 82.2% | $38,500 | -$13.8k |
| 100 | $150,000 | $26,717 | 82.2% | $104,000 | +$19.3k |
| 500 | $750,000 | $133,583 | 82.2% | $366,000 | +$250k |

Break-even about **32 customers** (at the 3-person team).

**Reading the tables:** At 5 and 20 customers every scenario loses $13-43k/month on a full-salary basis. That means roughly **$250-450k of runway or founder-subsidized cash** to get to 20 customers if founders pay themselves $12k loaded each. Founders drawing $4-5k lowers burn by half.

---

## 5. Self-serve vs high-touch for the first 20 customers

**Verdict: high-touch, productized-service ("consulting disguised as SaaS") for the first 20, with self-serve as a later Starter-tier goal.**

Evidence:
1. **Onboarding is 14-40 hours** (3.4); metric definitions and messy data are the cost, not connector setup. Self-serve ingestion tools do not solve semantics.
2. **Trust:** a product that says "your margin dropped, here is why" is judged on correctness. Early errors kill retention. Human validation (about 1-2 hours/customer/month) is the quality control and is also your labeled eval data.
3. **Price anchors:** self-serve comps live at $49-400/mo (Prediko, Cogsy, Fathom), which cannot fund the labor above. Buyers who pay $6-18k/yr (Jirav, fractional CFO, Glean) are sales-assisted or quote-based.
4. **Funnel benchmarks:** $5-25k ACV is a "hybrid" band; payback for self-serve (6-11 months) is better but only if onboarding is automated (S, GrowthSpree/Stealth Agents above).
5. **Learning value:** 20 hands-on customers gives you the investigation taxonomy, the thresholds, and the outcome data that justify value-based pricing and later automation.

Rules to keep it "SaaS" and not agency: fixed scope in the plan, hour caps per tier, every manual step logged and ticketed for automation, no custom dashboards, annual prepay where possible.

---

## 6. Benchmarks, funding environment, sensitivity

### 6.1 Startup benchmarks (S unless marked)
- **Gross margin:** AI-native about 50-60% (Bessemer figure as quoted), ICONIQ-reported average about 52% in 2026 (up from about 41% in 2024) vs 75-85% classic SaaS; margin projections 45% (2025), 53% (2026), 59% (2027) ([Monetizely](https://www.getmonetizely.com/articles/the-economics-of-ai-first-b2b-saas-in-2026-margins-pricing-models-and-profitability), [Enterprise DNA](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-31-ai-native-saas-gross-margins-are-still-running-20-40-points), [SaaS CFO](https://www.thesaascfo.com/?p=308177)). Mostly secondary summaries of one survey; primary reports not opened.
- **Compression:** some public SaaS firms attribute 6-9 points of margin compression to AI features ([Pulse](https://www.pulse.bot/saas/news/the-ai-cogs-problem-why-saas-gross-margins-are-compressing-in-2026-and-what-the-best-operators-are-d-ea0eea40-7f2a-498a-8625-3391df3faf7b/)); counter-evidence says median is stable above 80%. Contested.
- **ACV and cycles:** see 3.6. I found no ACV benchmark specific to AI analytics for SMB; my $6-18k ACV is an assumption anchored on Jirav/fractional CFO comps.
- **Funding:** AI seed medians about $15-19M pre-money (Q1-Q2 2026), roughly 40% above non-AI at one source; Series A bar about $2-4M ARR for AI; 10-25x ARR multiples at seed ([Eqvista](https://eqvista.com/ai-startup-fundraising-trends/), [Causo](https://hub.causo.ai/guides/h1-2026-ai-startup-funding-report), [Crunchbase](https://news.crunchbase.com/seed/data-bigger-deals-longer-seriesa-2026/), [Carta Q1 2026](https://carta.com/data/state-of-private-markets-q1-2026-full-report/)). Figures are noisy, skewed by mega-rounds in foundation models, and not specific to AI analytics. Implication: capital is available but concentrates in foundation/agent platforms; a vertical SMB analytics startup is best positioned for a small seed after about $15-30k MRR, or bootstrapped via the service-heavy model. A $2-4M ARR Series A bar equals about 190-370 customers at $900 (base), which means **raising a seed on traction of 20-40 customers is the realistic milestone.** [A]

### 6.2 Sensitivity (base unit contribution = $491/mo; calculated)

| Change | Effect on unit contribution | Rank |
|---|---|---|
| Price +/- $200/mo | +/- $200 (about 41%) | **1** |
| CS load: 1 per 40 to 1 per 20 customers | -$250 (halves contribution) | **2** |
| CS load: 1 per 40 to 1 per 80 | +$125 | |
| Validation hours doubled (0.3 to 0.6 x $220) | -$66 | 3 |
| Infra + ingestion +50% | -$38 | 4 |
| LLM cost 3x ($18 to $54) | -$36 | 5 (negligible) |
| Monthly churn 1.5% to 2.5% | LTV (unit contrib / churn) falls from $32.7k to $19.6k | Major for LTV |
| Loaded cost per head $12k to $8k | Break-even customers drop about 30% | Major for runway |

Takeaway: **price and human load per customer dominate; LLM and compute barely matter.** Invest in reducing CSM time per customer and in raising price/mix, not in model optimization.

### 6.3 Customers needed to sustain a small team (monthly gross profit must cover people + tools)

Formula: `N = (heads x loaded_cost + tools) / unit_contribution`, ignoring CAC and setup-fee income (both partly offset each other).

| Team | Monthly cost | Base ($491/cust) | Optimistic ($1,233/cust) | Price needed for 30 customers |
|---|---|---|---|---|
| 2 people at $8k loaded + $1.5k tools = $17.5k | $17.5k | 36 | 14 | $491 -> need unit contrib $583, i.e. about $992 price |
| 3 people at $8k + $3k = $27k | $27k | 55 | 22 | $900 -> unit contrib $900, i.e. about $1,310 price |
| 3 people at $12k + $2.5k = $38.5k | $38.5k | 78 | 31 | about $1,690 price (base cost structure) |

Rough rule: **about 30 customers at about $1,000-1,300/month, or 50-60 at $900,** funds a 2-3 person team. That is roughly $360-470k ARR for 30 customers, consistent with a seed-stage "default alive" threshold. [A]

---

## 7. Key risks and what to validate first

1. **Willingness to pay $900-1,000/month** for a data-less SMB. The comps are mixed; test with 10 priced pilots (setup fee included) before building. A free pilot proves nothing.
2. **Human load per customer.** Track hours per customer per month from day 1; the contribution model fails above about 4 hours (CS+validation) per customer-month at $900.
3. **Churn:** monitoring tools without clear weekly value churn quickly. Tie the product to decision tracking and a monthly "decisions made / outcomes" report, which supports the value-based price.
4. **SOC 2 timing:** defer until a deal needs it, but budget $15-60k.
5. **Data gaps in my evidence:** vendor pricing pages were not reachable (third-party aggregators with conflicting numbers); Anodot, Dust and Narrative BI prices not found; OpenAI/Google API prices not checked; no AI-analytics-specific funding or ACV data found. Treat all [A] numbers as hypotheses to be replaced by pilot data.

# 07 — Long-Term Platform Alignment (Company Intelligence)

**Question:** does the proposed first product create a credible path toward a Company Intelligence platform — and not a small consulting business that cannot become software? Architecture facts come from Phase 1 (`research/appendix/agent4_architecture.md`) and Phase 2 (`research/phase2/04`); the consulting-versus-software tripwires come from the Phase 3 skeptic review. Everything about future value is a hypothesis.

## 1. Honest answer
**Credible only if three conditions are enforced from the first customer; otherwise a pass means a services business.** The first product (a margin/cash investigation delivered as a scan plus a fixed-scope investigation) builds *reusable raw material*, but the judgment in the deliverable is currently human. Whether that judgment can be turned into software is exactly what the tripwires measure.

**Three tripwires (carried into `05`):**
1. Hours per investigation fall ≥ 40% from the first to the fourth.
2. ≥ 60% of the delivered numbers come from a re-runnable script.
3. At least two payers commit to something recurring (a weekly Brief at a stated price).

## 2. What becomes a reusable platform capability

| Capability | Built for the first use case | Reused by later modules | Notes |
|---|---|---|---|
| **Source ingestion + credential handling** (Shopify, QuickBooks/Xero, Stripe; CSV/export import) | Yes | Every module needs the same sources | Plumbing: Nango + dlt per Phase 1; connectors are a standing maintenance cost (~1 engineer-week per source per quarter, assumption) |
| **Canonical business model** (customers, products/SKUs, suppliers, orders, invoices, payments, costs, channels, price lists) | Yes | Core of Company Intelligence | Typed relational tables with relationship status (user-confirmed / data-supported / historical pattern / inferred / hypothetical) — no graph database needed |
| **Validation layer** (freshness, completeness, reconciliation to the system's own totals, **coverage badges** such as cost coverage %) | Yes | Universal; the most valuable trust asset | Turns missing data into a visible feature |
| **Metric/semantic compiler** (thin YAML spec for revenue, gross margin, DSO, aging, etc.) | Yes | All modules | Phase 1 recommends a thin in-house spec, OSI-compatible |
| **Deterministic analysis library** (price/volume/mix bridges, aging, payout matching, variance, event-window comparison) | Yes | Reused across margin, cash, reconciliation, churn bridges | Numbers never computed by an LLM |
| **Investigation engine** (hypothesis list → fixed tool menu → evidence grading → abstention) | Yes | All investigations | Single agent loop; no multi-agent swarm |
| **Case-file and evidence-ledger format** (observation vs explanation confidence, counterevidence, could-not-check, lineage) | Yes | Every module and any delivery channel (email Brief, web page, MCP tool) | The most plausible differentiator, and the easiest for a platform to copy if it proves valuable |
| **Decision and outcome log** (decision, owner, expected effect, follow-up date, result labelled "followed by") | Yes | Company Intelligence's learning loop | Adoption evidence is weak; build thin |
| **Brief / notification policy** (quiet by default, ≤3 items, hard push cap) | Yes | All modules | Phase 1 UX research |
| **Evaluation harness** (golden incidents, seeded faults, abstention checks, blind comparison records) | Yes | Quality gate for every module | Needs real labelled incidents from customers |
| **Tenant isolation, audit log, data-handling controls** | Partly | All modules | SOC 2 only when procurement asks |

## 3. What is specific to the first use case (will not transfer)
- The **margin tree** (price, cost, mix, discount, freight, fees, returns) and the supplier-cost-versus-price-lag detector.
- **Shopify and QuickBooks quirks:** cost-per-item handling, payout grouping, bundles, history limits.
- The **hypothesis library** for margin movements and its observed frequencies.
- **Finding templates** and thresholds tuned to Shopify-with-wholesale businesses.
- **Cohort-specific language** (customers, SKUs, payouts) in the Brief.

## 4. Data model and investigation capabilities that would carry forward
- **Entities and links:** SKU ↔ supplier ↔ cost history; SKU ↔ price list ↔ customer; order ↔ line ↔ discount ↔ refund ↔ payout ↔ bank row ↔ ledger entry; invoice ↔ customer ↔ payment. These links are the substrate for impact propagation later (supplier delay → stockout → late orders → churn), but propagation needs quantitative models (lead times, elasticities) that do not exist yet; Phase 1 warns naive propagation double-counts.
- **Evidence grades:** arithmetic identity > decomposition attribution > temporal coincidence > correlation > LLM-suggested; the same grading serves every module.
- **Abstention as a first-class output.**
- **Outcome labels:** every recommendation, action and follow-up result becomes labelled data. This is the only data asset that compounds — and only after many months and many customers.

## 5. What would create real switching costs (and what would not)

| Asset | Switching cost? | Honest assessment |
|---|---|---|
| Customer-confirmed company model (definitions, entity mappings, cost corrections) | **Moderate** | Real work the customer would have to redo; but it can be re-exported, and a rival can rebuild it from the same sources |
| Decision and outcome history | **Moderate, grows over time** | Valuable only if people actually log decisions; evidence of sustained use is weak |
| A weekly Brief embedded in the owner's routine | **Moderate** | Habit and trust; but any free tool can send a Monday email |
| Labelled incident history that tunes thresholds and hypothesis priors per tenant | **Low-moderate** | Improves quality; transferable only if exported |
| Accountant/advisor relationships | **Potentially high, unproven** | Referral loops could be the only durable distribution moat |
| Cross-tenant priors | **Blocked on Xero data** | Xero's developer terms bar AI/ML training on API data; for Intuit/Shopify, terms must be read |
| Connectors | **Low** | Commoditised; maintenance burden favours platforms |
| The case-file format | **Low** | Platform vendors can copy it with a prompt change |
**Realistic moat:** calibrated, abstaining investigations tuned on labelled outcomes in one vertical, plus trusted-advisor distribution. Both need customers and time; neither exists on day one.

## 6. What should stay outside the initial scope
Generic chat; a dashboard or BI builder; an agent builder; a knowledge graph or graph database; multi-agent orchestration; what-if simulation; impact-propagation models beyond the margin tree; write-back or autonomous actions (including repricing and payments); ERP connectors (NetSuite, Odoo, Acumatica); advisor portfolio views; SOC 2 Type II; fine-tuning; a free tier. Each either dilutes the first test or depends on evidence that does not exist.

## 7. Does the experiment itself build toward the platform?
Yes, if run as designed: the scan scripts are the first version of the validation layer and bridge library; the case files are the first version of the evidence ledger; the labelled incidents are the first golden set; the timing log shows what to automate next. No, if the founders write each deliverable by hand and track nothing: that outcome is a consulting practice.

## 8. A product-form question the review surfaced
If Gate 0 shows that an LLM *with deterministic evidence tables* is acceptable where an LLM *alone* is not, the product may be best expressed as an **evidence-and-investigation layer delivered through existing assistants** (an MCP server or plugin), not a standalone interface. That aligns with the inbound preference, reuses nearly every component above, and lowers the cost of a web UI — and it concentrates platform risk. Treat it as a hypothesis (`06` H-1) to test, not a plan.

## 9. Path to the vision if the first test passes
1. **Module 1:** the winning investigation (margin or cash/AR) with the Brief and decision log.
2. **Module 2:** the adjacent module on the same connection (cash/AR if margin won; margin bridge if cash won; payout reconciliation third).
3. **Then:** supplier/procurement and inventory investigation as data allow; a company model that spans them; outcome-labelled priors; only then impact propagation and simulation, each requiring validated quantitative models.
**Do not commit to the broad platform until one module has paying customers and the tripwires are met.**

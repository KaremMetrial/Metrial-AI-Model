# 05 — Product Experience and MVP Specification (conditional)

**Status:** this specification is **conditional**. Nothing here is to be built until the 30-day test (`07`) passes its thresholds. Until then, the "product" is a manually delivered audit. It is written now so the test produces the artifacts (case files, labels, timings) that the MVP will need. Not a UI design; wireframe-level text only.

**Design rules carried from Phase 1 UX research (`research/appendix/agent5_ux.md`):** quiet by default; ≤3 items per brief; confidence shown as labelled levels with reasons, never a bare percentage; counterevidence given equal weight; a "could not check" section; outcomes labelled "followed by", not "caused by"; no dashboard gallery, no generic chatbot. Evidence caveat: confidence-display and hypothesis-ranking patterns come from HCI studies and AI-SRE products whose accuracy claims are self-reported; test them with seeded wrong explanations.

---

## A. Opportunity 1 (lead hypothesis): Margin Investigator for Shopify-first brands with a wholesale channel

### Customer journey
1. **Discovers.** A founder searching "why did my gross margin drop" or reading an accountant's note lands on a page that offers a **free file-in/leak-list-out check** (upload Shopify orders export + supplier cost/invoice file). *Evidence status: search demand unmeasured; channel unproven (Agent 4).*
2. **Connects.** Concierge stage: exports or an invited read-only QBO user and a Shopify staff account with read permissions; no marketplace app. Productized stage: Shopify custom-app/read-only token + QBO read scope. Ask only for the sources the first finding needs.
3. **Imports and validates.** Freshness, completeness and reconciliation checks run first: do Shopify revenue and QBO sales tie within tolerance; what % of revenue has a known unit cost; how many months of history exist. *Display a coverage badge before any finding.*
4. **Understands entities/metrics.** A "What I understand about your business" card — channels, top products, cost categories, fiscal calendar — with Right / Not quite / Not sure on each line; ≤5 confirmation questions in business language ("Is *Acme Co* the same customer as *ACME Corporation*?"). Each answer is stored as a dated, user-confirmed fact.
5. **Identifies a meaningful problem.** The monitor compares two periods and gates on materiality (dollars × persistence), not a fixed threshold. Typical first findings: gross-margin points lost to price vs cost vs mix vs discounts vs freight/fees vs returns; SKUs where supplier cost rose but price did not.
6. **Investigates.** Deterministic decomposition produces the bridge and the leading dimension; a bounded set of hypotheses is tested with fixed tools (supplier-cost vs sell-price check, event-window comparison for promotions, mix-shift test). The LLM plans and narrates; it computes nothing.
7. **Presents evidence and uncertainty.** Case file: headline → bottom-line box (dollar range, urgency, recommended action) → *what we are sure of* → *what we think explains it* (≤3 hypotheses: best-supported / possible / ruled out) → evidence with source and date → counterevidence directly under each hypothesis → *what we could not check* → affected SKUs/suppliers/customers → actions including "do nothing" with its cost.
8. **Customer decides.** Act / Investigate further / Dismiss (reason required) / Snooze; owner and due date assigned; reply by email or button without a login for simple acknowledgments.
9. **Tracks outcome.** The system proposes a measurable check ("blended margin on SKU group A back above 41% by 3 Dec") and reports improved / no change / worse / cannot tell, labelled "followed by". *Weak adoption evidence: decision journals are rarely maintained; measure completion without nagging.*

### First screen
**The Brief**, not a dashboard: "This week: 2 things need you" or "Nothing needs you." Each item shows headline, dollar range, one-line reason, one-line confidence-with-reason, one recommended action, and four buttons (Open case / Assign / Snooze / Not an issue). Footer: "Last week's decisions: 1 followed up, 1 pending." Executives live here (email first; summary in email, detail behind login).

### Primary workflow
Brief → Case file → Decision → Follow-up. The **Cases** queue is the ops back office (filters Mine / Needs decision / Waiting on data / Snoozed / Resolved). **Business Model** is the review-and-correct page. **Ask** is a chat box scoped to a case, not a product.

### Core features (MVP, if the test passes)
1. Two connectors (Shopify; QBO *or* Xero) plus CSV import for supplier costs/price lists.
2. Reconciliation and coverage checks with visible lineage.
3. Two-period margin bridge (price / cost / mix / volume / discount / fees / returns) with an explicit unexplained residual.
4. Supplier-cost vs sell-price lag detector.
5. Case file with evidence/counterevidence/could-not-check and separate observation vs explanation confidence.
6. Weekly Brief email (≤3 items, hard push cap).
7. Decision log and scheduled follow-up.
8. Customer-visible audit log; read-only access; tenant isolation.

### Explicitly NOT in the MVP
Generic chatbot; dashboard or chart gallery; BI/report builder; agent builder; knowledge graph; multi-agent orchestration; what-if simulation; impact-propagation graph beyond the margin tree; autonomous actions or write-back (including repricing); cash/inventory/churn monitors; Slack/Teams bots (email first); NetSuite/Odoo/Acumatica connectors; advisor portfolio view; SOC 2 Type II; fine-tuning; free tier.

### Acceptance gates
Reconciliation within tolerance with metric definitions signed off by a named owner; on ≥30 owner-confirmed historical movements, top explanation correct ≥70% and calibrated, correct abstention on injected "no-cause-in-data" cases; median human onboarding ≤8 hours by customer #10; ≥60% of cases rated useful.

---

## B. Opportunity 2 (strongest challenger): Cash and AR Investigator for QuickBooks/Xero businesses

### Customer journey
1. **Discovers.** Via an accountant/bookkeeper recommendation, QBO/Xero ecosystem content, or a free "DSO and late-payer check" (upload an AR aging export). *Competition: Float, Fathom, Chaser (~$259/month), Upflow, native reminders and AI.*
2. **Connects.** One read-only accounting connection (QBO or Xero); no second system needed for first value.
3. **Imports and validates.** Detect invoices paid by journal, unapplied credits/prepayments, multi-entity customers, stale sync; show data freshness.
4. **Understands entities.** Customer entity resolution (parents/subsidiaries, duplicates) and payment terms confirmed with 3–5 questions.
5. **Identifies a problem.** DSO drift by customer segment, a specific large customer's behavior change, a payables cluster that breaks the cash floor in N weeks.
6. **Investigates.** Deterministic aging and payment-behavior statistics; hypotheses ("terms changed", "dispute", "one-off delay") tested against invoice history, credit notes and payments.
7. **Presents evidence and uncertainty.** Same case-file anatomy; forecasts shown as ranges with the assumptions list.
8. **Customer decides.** Prioritized collection list with owner; proposed message drafts for approval (nothing sent automatically).
9. **Tracks outcome.** Cash collected vs proposed; DSO delta; "cannot tell" when confounded.

**First screen:** "Cash this week": the 1–3 customers/payables that change the 13-week cash floor, plus "nothing needs you." **Not in MVP:** payments, reminders sending, loans/financing, forecasting beyond 13 weeks, accounting write-back, other systems.

**Why it is the challenger, not the lead:** easiest data (GREEN) and fastest onboarding (~1–2 days), but crowded and bundled by Intuit/Xero; willingness to pay for *explanation* is unproven (`02`).

---

## C. What the audit must produce now (so a build is cheap later)
- A **case-file template** per finding type (margin, cash/AR, reconciliation).
- A **labeled incident log**: finding, evidence, owner-confirmed cause (yes/no/partial), dollars, action taken, outcome.
- A **data-timing log**: hours to access, clean and validate per customer; cost-coverage %.
- A **hypothesis library** per finding type with observed frequency.
- A **blind-comparison record** against the customer's in-product AI output (Intuit Assist, Shopify Sidekick, Claude/QBO prompt).

These double as the golden set for evaluating any later automation.

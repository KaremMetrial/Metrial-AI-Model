# Agent 5: UX and Product Experience for an "Investigation Queue" product

Date: 2026-11-19. Method: web search of vendor docs, blogs, and research summaries. Several fetches were blocked by the session network (for example docs.incident.io), so many claims rest on search-result summaries of vendor pages. Where a number is vendor-reported I say so. Part A is evidence. Part B is critique. Part C is recommendation.

---

## PART A. EVIDENCE

### A1. How existing products deliver proactive insight

**Tableau Pulse (digest model).**
- Users pick Slack or email and a cadence under Preferences. The email carries a generated summary of which metrics changed most, with per-metric thumbnails and links. Source: [O'Reilly, Learning AI Tools ch.4](https://www.oreilly.com/library/view/learning-ai-tools/9781098175771/ch04.html).
- Each insight has thumbs up/down. Feedback is described as reaching the summarizing LLM rather than changing detection immediately (same source).
- Admins track adoption (metrics created, followers, data sources) via Admin Insights and are advised to roll out to specific groups first. Source: [Tableau Pulse admin guide](https://www.tableau.com/learn/get-started/pulse-admin).
- A 2024 analyst note cited about 3,000 customer firms and 9,000+ monthly active users shortly after GA. It is dated and I found no current numbers. Source: [Constellation Research](https://www.constellationr.com/blog-news/tableau-and-salesforce-eye-next-wave-analytics-and-bi).
- Pattern: the user must first define or follow metrics, so the product starts from a metric list, not from "what is wrong with my business". There is no decision or outcome object.

**ThoughtSpot Monitor / Spotter.**
- KPI alerts come in three kinds: threshold, scheduled, and anomaly. Anomaly alerts fire when a KPI leaves a predicted range. The docs mark anomaly alerts Early Access and off by default, and say a transient breach that has recovered by the next check produces no alert. Channels are email or webhook/custom. Source: [ThoughtSpot docs](https://docs.thoughtspot.com/cloud/26.6.0.cl/monitor-alert-anomaly).
- Marketing says Spotter shares insights in Slack/Teams ([ThoughtSpot Liveboard page](https://www.thoughtspot.com/product/data-visualization-tools)). I could not find documentation of proactive Spotter alerts or any adoption data.

**Power BI / Fabric.**
- Copilot-generated summaries in email subscriptions are in preview, and the community already has a request to make them optional. Sources: [Microsoft Learn](https://learn.microsoft.com/en-au/power-bi/create-reports/copilot-summaries-in-subscriptions), [Fabric Ideas](https://community.fabric.microsoft.com/t5/Fabric-Ideas/Make-Copilot-summaries-in-Power-BI-subscription-emails-optional/idi-p/5131648).
- Activator (formerly Data Activator) provides threshold-triggered notifications and actions. I found no adoption data.

**Anodot (business-metric anomaly detection).**
- The main product claim is correlation: grouping related anomalies into one incident with contributing factors, to avoid "alert storms". Vendor-reported results are 90% less alert noise and 80% faster detection. These are self-reported and unverified. Sources: [Anodot incident detection](https://anodot.com/incident-detection), [Fintech brochure](https://www.anodot.com/wp-content/uploads/Anodot-for-Fintech-web-1.pdf). Anodot is now owned by Glassbox.
- Lesson: even the incumbent in business-metric anomaly detection sells the "fewer, grouped alerts" angle, so noise is the known failure mode of the category.

**AI SRE (closest analog for autonomous investigation).**
- Datadog Bits AI SRE:
  - It proposes hypotheses, queries telemetry to confirm or reject each, drops unsupported ones, and pursues promising ones. It posts progress in a Slack thread and a final summary with root cause, evidence, and next steps, and saves the investigation to the incident record. Sources: [Datadog Bits docs](https://docs.datadoghq.com/bits_ai/bits_ai_sre/investigate_issues.md), [Datadog blog](https://www.datadoghq.com/blog/bits-ai-sre.md).
  - The alert-investigation docs describe a feedback step where you tell Bits whether the conclusion was correct and supply the real cause if it was wrong. This is a decision/outcome loop in miniature.
  - Reported numbers: about $4 and about 2 minutes per investigation, and a "44% higher investigation quality score" versus its own March 2026 release on an internal benchmark. Source: [Datadog cost/speed/accuracy post](https://www.datadoghq.com/blog/bits-investigations-cost-speed-accuracy/). The benchmark is Datadog's own and not independently verified.
  - Newer capabilities such as investigating without a triggering monitor are still preview. Source: [InfoQ on Scout](https://infoq.com/news/2026/10/datadog-scout-sre-model).
- Resolve AI: runs multiple hypotheses in parallel and surfaces root cause with a confidence score and evidence trail. It claims a more than 2x accuracy gain on internal eval sets versus earlier versions. Sources: [Resolve AI](https://resolve.ai/lp/automated-rca), [Mezmo market map](https://www.mezmo.com/learn/the-2026-ai-sre-market-map-agents-harnesses-and-the-data-layer).
- Cleric: tests hypotheses and delivers diagnoses with confidence scores in Slack, in read-only mode (per a third-party comparison). Source: [Better Stack](https://betterstack.com/community/comparisons/cleric-alternatives/).
- Traversal: I found no primary-source accuracy claim. The "90%+" figure on guide sites is unattributed. Treat it as unverified.
- incident.io has a "measuring accuracy" docs page, which suggests accuracy measurement is an expected product surface. I could not fetch it ([URL](https://docs.incident.io/investigations/measuring-accuracy)).
- Overall: no independent benchmark exists. The UX convention that has emerged is a chat-native thread, hypotheses tested against evidence, a confidence level, a human feedback step, and a record that persists. Accuracy numbers are marketing, not evidence of reliability.

**Aera Technology "Inbox".**
- Prioritized, personalized recommendations pushed to each user, sortable by importance, financial impact, and urgency. Users accept, modify, or reject, and every response is logged in a Decision Data Model that feeds learning. It is also reachable by chat and voice. Sources: [Aera Inbox](https://www.aeratechnology.com/aera-inbox), [Aera platform](https://www.aeratechnology.com/platform).
- One article says Aera is moving beyond the inbox toward role-specific workspaces. I could not date it, so verify before relying on it.
- This is the closest existing analog to the proposed queue, and it is aimed at large enterprises with deep integration, which leaves the SMB/mid-market gap open.

**Cloverpop.**
- A "Decision Bank" records rationale, data sources, and outcomes, with a free Slack app and follow-up reminders. Sources: [Cloverpop features](https://cloverpop.com/cloverpop-decision-making-product-features), [Slack listing](https://slack.com/marketplace/AKHMRPUCT-cloverpop). Its claims of "75% better decisions" are vendor research and I could not verify them.
- It relies on humans manually logging decisions, with no automated detection.

**Linear Triage and Superhuman-style inbox.**
- Linear Triage: a per-team inbox where each item is accepted, declined (with a required comment), marked duplicate (merge), or snoozed, and it can stay pending while awaiting information. Sources: [Linear docs](https://linear.app/docs/triage), [Linear snooze/merge changelog](https://linear.app/changelog/2021-06-17-inbox-snooze-and-easier-issue-merge).
- I did not research Superhuman directly. The pattern here (keyboard-first, process each item to zero) is well known but I have no source for it in this report.
- Transferable idea: a small closed set of dispositions, a required reason on decline, and snooze with a return date.

**Statsig.**
- Experiment Summary: a persistent record of results, discussion, and action items that becomes the default tab once a decision is made. Decision Frameworks recommend Ship / Discuss / Don't ship and can require a reviewer if the human decision departs from the recommendation. Sources: [Experiment summaries](https://statsig.com/updates/update/interactive-experiment-summaries), [Decision framework](https://statsig.com/updates/update/ship-decision-framework), [Experiment reviews](https://statsig.com/perspectives/experiment-reviews-learning-tests).
- Transferable idea: a recommendation that the human can override, with the override recorded.

**Slack/Teams-delivered "AI chief of staff" tools.**
- Slack launched a "Today" daily briefing view in 2026, and there are many small founder-focused tools (OpenPulse, GAIA, readywhen). Source: [Slack Today blog](https://join.slack.com/blog/news/today-daily-briefing). These are mostly marketing pages, and I found no outcome evidence.
- They focus on email, calendar, and task triage, not on the financial and operational health of the business.
- Related: Mastercard announced a virtual-CFO product for small business in March 2026. I saw only a secondary news summary, so the details are unconfirmed. Source: [Fintech News](https://fintech-news.pages.dev/news/2026/03/mastercard-offers-small-businesses-insights-from-virtual-cfo).

### A2. Adoption and fatigue evidence

- BI adoption is low. IBM cites Gartner at about 29% of employees using analytics/BI tools, with little growth over seven years. A survey of 214 data leaders (BARC/Eckerson) is reported at about 25% active use. Source: [IBM](https://www.ibm.com/think/insights/business-intelligence-adoption).
  - Caution: the widely repeated "60-70% of dashboards unused (Gartner)" does not trace to a Gartner publication, so do not cite it.
- Alert override in clinical settings is the best-studied analog. Reported override rates run from about 53% of inpatient alerts to about 90% for drug-interaction alerts, and in one study 40% of overrides were inappropriate. Sources: [Fierce Healthcare](https://www.fiercehealthcare.com/ehr/alert-fatigue-overrides-remain-a-safety-threat), [HealthExec](https://healthexec.com/topics/healthcare-management/healthcare-economics/75-medication-alert-overrides-pose-harm-patients).
  - Hospital arrhythmia alarms: 88.8% false positives. Source: [UNC Nursing](https://nursing.unc.edu/news/modern-monitoring-systems-contribute-to-alarm-fatigue-in-hospitals).
- IT operations: the Splunk-reported share of teams that had an outage from an ignored or suppressed alert is a vendor survey. Source: [ITPro](https://www.itpro.com/software/it-teams-are-battling-a-surge-in-outages-over-missed-critical-alerts).
- Executives: a vendor blog (Flock) reports 61% of C-level execs do not respond to all notifications. This is weak evidence. Source: [Flock](https://blog.flock.com/communication-overload-hits-executives-hardest).

Interpretation: the base rate for "proactive alerts get ignored" is high across domains. The thing that changes it is precision and consequence, not volume or polish.

### A3. Trust, explanations, uncertainty

- Google PAIR Guidebook: the goal is calibrated trust (trust in some situations, double-check in others). Confidence display is a decision input, "don't say what without why" in high-stakes cases, and admitting a prediction might be wrong can lower trust in that prediction, which can be the right outcome. Source: [PAIR Explainability + Trust](https://pair.withgoogle.com/chapter/explainability-trust/).
- Buçinca et al. (CSCW 2021, N=199): plain explanations did not reduce overreliance on AI and may increase it. "Cognitive forcing" (for example, having the person commit to their own view first, or a time-out) reduced overreliance, but people liked those designs least and benefits varied by individual. Source: [arXiv 2102.09692](https://arxiv.org/pdf/2102.09692).
- Showing confidence scores: users accept high-confidence outputs more often, but decision quality did not necessarily improve when human and AI strengths were not complementary. Hedging language reduced acceptance without improving the ability to tell right from wrong. Sources: [Kim et al., "I'm Not Sure, But..." (Microsoft Research)](https://www.microsoft.com/en-us/research/?p=1030965), [Hide or Highlight](https://arxiv.org/html/2508.07095v1). More detailed uncertainty did not necessarily produce more cautious use ([Not All Uncertainty Is Equal](https://www.alphaxiv.org/abs/2605.28571.md)).
- Longer explanations raised user confidence without raising accuracy (same cluster of studies).
- I did not find a primary Nielsen Norman Group study on AI uncertainty. A UXmatters article cites NN/g statistics without linking them, so I excluded those.
- Practical reading: a single "87% confident" number or hedging prose is not shown to help non-experts. What is supported is giving reasons, making evidence checkable, and structurally prompting a check before a high-stakes action.

### A4. Delivery channels

- Dated but direct: the Quartz executive survey (2014/2016) found email newsletters were a top-three morning source for 60% of executives, 59% consumed news mainly on mobile, and executives skewed to morning reading. The publisher's Daily Brief open rate of 40-50% is self-reported. Sources: [Nieman Lab](https://niemanlab.org/2016/12/business-execs-are-still-getting-a-ton-of-news-via-email-says-quartz-survey), [Martech](https://martech.org/business-executives-still-turn-email-newsletters-first-news).
- General workplace surveys: email remains the formal default. A vendor-run (Slack-commissioned) study found 51% of workers prefer real-time messaging, and an independent survey put consumer messaging apps (WhatsApp, Messenger) at 18% and 14% of one professional sample. Sources: [Tech.co](https://tech.co/news/slack-teams-replacing-business-emails), [ITPro](https://www.itpro.com/collaboration/33262/80-of-businesses-still-use-email-as-a-primary-collaboration-tool).
- Gap: I found no solid study of SMB owner/CFO channel preference, nor of dashboard versus email usage. Channel choice for this product must be tested with customers, not assumed.

### A5. Onboarding and company-model validation

- Userpilot reports median time-to-value of about 1.5 days across SaaS, with top-quartile products delivering first value in under 5 minutes, and says integrations or setup do not themselves count as first value. The sample size is inconsistently reported across sources. Sources: [Userpilot benchmarks](https://userpilot.com/blog/saas-onboarding-benchmarks/), [TTV report](https://userpilot.com/blog/time-to-value-benchmark-report-2024). I found no benchmark for "connect data to first insight".
- Accounting-connector onboarding practice (Shopify to QuickBooks/Xero): mapping (chart of accounts, fees, refunds, taxes, clearing accounts) is the make-or-break step. Products offer an assisted/auto-map path plus a custom path, pre-fill a mapping page the user can edit, and offer limited historical backfill (about 90 days is mentioned). Sources: [A2X](https://www.a2xaccounting.com/blog/how-to-integrate-shopify-with-quickbooks/), [Bookkeep automap](https://www.bookkeep.com/docs/account-setup/connecting-an-accounting-platform/chart-of-accounts-automap-for-quickbooks-xero-and-zoho), [Intuit](https://quickbooks.intuit.com/learn-support/global/manage-integrations/shopify-and-quickbooks-online-integration-guide/00/964955). These are vendor sources with no usability data.
- Finance teams reportedly spend substantial time verifying AI outputs (IDC-Sage report via [CFO.com](https://www.cfo.com/news/finance-teams-spend-13-hours-a-week-verifying-ai-outputs-aaron-harris-michael-friedman-trial-balance/824390/)). Verification cost is a real adoption tax.

### A6. Naming landscape (preliminary, not a trademark clearance)

- "Watchtower" is crowded: a pending WATCHTOWER AI application (access control), a live WATCHTOWER application by Decagon AI for monitoring chatbots, plus Watchtower Labs and Watchtower AI. Source: [Justia trademarks](https://trademarks.justia.com/990/29/watchtower-99029580.html).
- Existing AI "business monitoring" tools include InfiniteWatch, Gowatch, and RivalSense. Sources: [InfiniteWatch](https://infinitewatch.ai/product/ai-insights), [YC Gowatch](https://www.ycombinator.com/launches/P0q-gowatch-ai-monitoring-platform-for-businesses).
- AI startups are now litigating name collisions ([Domain Name Wire, Jul 2026](https://domainnamewire.com/2026/07/16/two-ai-startups-chose-the-same-brand-name-now-theyre-headed-to-court/)). My searches for the other candidates below returned nothing conclusive, which is not the same as clear.

---

## PART B. CRITIQUE OF THE INVESTIGATION QUEUE VERSUS ALTERNATIVES

The Queue as specified has 12 fields per item. Strengths and weaknesses:

- Strength: it is a work object with state (owner, status, follow-up), unlike a dashboard tile. Aera, Linear, and Datadog all converge on persistent, dispositionable items.
- Weakness 1: a queue is only as good as precision. Item #1 that is wrong costs more trust than ten right items earn (alert-override evidence in A2). A visible queue also makes "zero items this week" feel like the product is broken, which pressures the system to emit filler.
- Weakness 2: for a CEO or owner, a queue is another inbox to maintain. It is a pull surface. Evidence that BI tools reach about 25-29% of employees suggests pull surfaces decay.
- Weakness 3: 12 fields on first view overwhelms a non-technical reader. Confidence in "observation" versus "explanation" is conceptually right but is not proven to help non-experts (A3).
- Weakness 4: it presumes a trusted company model. Wrong entity resolution or wrong metric definitions produce confident, wrong items.

Alternatives, scored for this user (non-technical owner/COO/CFO, SMB/mid-market, fears dashboard graveyard and fatigue). Scores are my judgment, not measured.

| Option | Push or pull | Trust build | Decision loop | Fatigue risk | Notes |
|---|---|---|---|---|---|
| Weekly briefing memo by email | Push | Medium; one artifact to judge | Weak unless it carries items forward | Low (once a week) | Matches exec email habit (A4, dated). Cadence may be too slow for urgent issues. |
| Slack-native AI chief of staff | Push plus chat | Medium | Medium | Medium-high | Many entrants already, and Slack itself ships a briefing. SMB owners may not live in Slack. |
| "Monday morning CFO memo" | Push | High if finance-literate | Weak | Low | Narrower to finance. Strong frame ("CFO you cannot afford") but bounded. |
| Exception-based reporting | Push on trigger | Depends on precision | Weak | High if thresholds are static | This is what ThoughtSpot/Anodot do. Known noise problem. |
| "Ask-the-owner" questions triage | Push, short | High; it validates the model | Medium | Low if rare | Very strong for onboarding and for model repair. Not a standalone product. |
| Decision journal | Pull | Low | Strong | Low | Cloverpop shows manual logging has low pull. Valuable as a by-product, not the hook. |
| Case file (legal/clinical analog) | Pull on demand | Highest for a given issue | Strong | Not applicable | Best page anatomy. Weak as an entry surface. |
| Conversational first | Pull | Variable; hallucination risk | Weak | Low | Good for follow-up questions on a case. A poor hook, since users must know what to ask. |
| Investigation Queue | Pull-ish | Depends on precision | Strong | Medium | Right object model, wrong front door for execs. |

**Verdict.** No single option wins on all axes. The strongest design is a composite:
1. The front door is a short, push-delivered brief (email first, with Slack/Teams as an option) that contains at most three items. This answers "do I need to look at anything".
2. Each item opens into a case file (the investigation page). This is where evidence, counterevidence, and uncertainty live.
3. The queue is the back-office view (mostly for the ops/finance owner, not the CEO), and is where status, owner, and follow-up live.
4. Ask-the-owner questions are the onboarding and model-repair mechanism, and they also feed confidence.
5. The decision journal and outcome follow-up are generated automatically from dispositions on cases, not manually written.
6. Chat is attached to a case and to the brief, not offered as the main surface.

Reasoning: it uses push where executives already are, keeps the persistent object model that Aera/Datadog/Linear validate, and contains fatigue by capping volume. Its riskiest assumption is precision, which no UX fixes.

---

## PART C. RECOMMENDATIONS

Everything here is a hypothesis to test, not a finding.

### C1. Information architecture

Three nouns and one verb, plus settings:
- **Brief**: the periodic push message (and its web twin, at most 3 items).
- **Cases**: all investigations (open, snoozed, resolved), the queue view.
- **Decisions**: the log of what was decided and what happened next (auto-built from cases).
- **Business Model**: what the product believes about the company (entities, definitions, thresholds), editable and always reviewable.
- Verb: **Ask** (chat), available in the Brief and in any Case, plus a global box.
- Settings: channels, quiet hours, who is the owner per area, thresholds.

Wireframe-level nav: `Brief | Cases | Decisions | Business Model | Ask`. Default landing is the Brief. Cases has filter chips: Mine, Needs decision, Waiting on data, Snoozed, Resolved. There is no dashboard and no chart gallery.

### C2. First-time experience

Goal: first useful artifact in one sitting, and first trusted insight within about a week. The benchmark evidence says top performers deliver first value in minutes, while the median SaaS takes about a day and a half (A5). Connecting data does not count as value.

Flow:
1. Connect one source (accounting or commerce, whichever the user has). Do not ask for all sources up front.
2. While syncing (minutes), show a plain-language "What I understand about your business" card: revenue streams, top customers, main cost categories, fiscal calendar. Each line has Right / Not quite / Not sure.
3. Ask at most 5 confirmation questions, ranked by how much a wrong answer would distort findings. Examples: "Is Acme Co the same customer as ACME Corporation?", "Is the $48k payment on 3 Oct a one-time project or recurring?", "We read your year starting in January; is that right?" Use suggest-then-confirm with prefilled answers, as the accounting-connector evidence shows.
4. Produce a first "Baseline brief" within the session: 3 facts it learned and 1 to 3 open observations, labeled "first look, low history". Be honest that detection needs history.
5. Set expectations: "I will stay quiet until I find something that matters. Expect about 1 message per week."
6. Offer backfill depth as a choice (for example 90 days now, more later), not as a required step.

Validation pattern: confirm the model through business concepts (customers, products, months), never through database terms. Record each answer as a dated user-confirmed fact, and show a "confirmed by you" tag in later evidence.

### C3. Daily experience

- Default is quiet. Most days produce nothing, and the product says so only inside the periodic brief, as "Nothing needed your attention. N things checked, X stayed within normal."
- The Brief (email, optionally mirrored in Slack/Teams) has this shape:
  - Line 1: "This week: 2 things need you" (or "Nothing needs you").
  - Each item: headline in plain words, dollar effect, one-sentence reason, one-line confidence statement, one recommended action, and buttons: Open case / Assign / Snooze to date / Not an issue.
  - Footer: "Last week's decisions: 1 followed up, 1 pending". This sustains the loop.
- Ops variant lives in Cases and has a filtered working view with keyboard dispositions (Linear-style: accept, decline with reason, snooze, merge as duplicate).

### C4. Investigation page ("case file") anatomy

Top to bottom, text wireframe:
1. **Headline**: "Refunds on Product X doubled; likely linked to supplier batch 14." Status chip and owner.
2. **Bottom line box**: effect (dollars, range), urgency (by when it matters), recommended action. Max 3 lines.
3. **What we are sure of** (the observation): the numbers, period, comparison baseline, and how it was measured. Uses plain labels: "Confirmed in your data".
4. **What we think explains it** (the explanation): ranked hypotheses (max 3), each with a label such as "Best-supported", "Possible", "Ruled out", with the evidence for and against. This follows the AI SRE hypothesis pattern (A1).
5. **Evidence**: each item has source, date, and a link to the underlying records. Counterevidence has equal visual weight and sits directly under each hypothesis, not in a footnote.
6. **What would change our mind / what we could not check**: missing data, unconfirmed definitions, and which question to the owner would resolve it. This turns uncertainty into an action.
7. **Affected entities**: customers, products, accounts, suppliers, each linking to its own context.
8. **Recommended action(s)**: concrete, with the owner and a due date. Include "Do nothing" as an explicit option, with its estimated cost.
9. **Decision panel**: Act / Investigate further / Dismiss / Snooze, plus a required one-line reason on Dismiss (Linear's required-comment-on-decline).
10. **Follow-up**: a scheduled check ("We will look again on 3 Dec and tell you whether refunds fell"), and a history log.
11. **Ask**: a chat box scoped to this case.

Confidence display recommendation: do not show a bare percentage. Use three labeled levels per claim, with the reason. For example: "Observation: confirmed (matches your invoices)". "Explanation: moderate, because only one of three checks supports it". The reasons are what people can evaluate. Because the studies (A3) show numbers and hedges shift acceptance without improving discrimination, test any scheme with real owners.

Cognitive-forcing option: for high-dollar recommendations, ask the owner "What would you expect to see if this explanation were wrong?" or have them pick their own hypothesis before seeing the ranking. Buçinca et al. found these reduce overreliance but are disliked, so use them only above a dollar threshold.

### C5. Decision workflow

States: New, Seen, Assigned, Investigating, Decided (Act / Dismiss), Monitoring, Resolved (confirmed / not confirmed / inconclusive), Snoozed.
- Every state change records who, when, and the reason.
- "Dismiss" asks for a reason from a short list (known issue, expected, wrong data, wrong explanation, not material) plus an optional free-text note. Reasons feed detection tuning and show up in a "why we stopped flagging this" explanation.
- Overrides: if the user declines the top recommendation, store it as a decision, in the manner of Statsig recording human departures from the recommended action.
- Delegation: Assign to a teammate through the channel they are already in (email reply, Slack button), with no login required for simple acknowledgments.

### C6. Follow-up loop

- When a decision is made, the system proposes a measurable check and date ("refund rate back under 3% by 3 Dec").
- On that date it reports one of: improved, no change, worse, cannot tell (and why). It asks "Was this useful?" and, if the diagnosis was wrong, "What was actually going on?" (the Datadog feedback pattern).
- Outcomes accumulate in Decisions: "Of 14 recommendations you acted on in Q4, 9 improved the metric." This is the proof-of-value artifact, and the only credible answer to "is this worth paying for?".
- Caution: attribution is hard. Label outcomes "followed by" and not "caused by" unless there is a basis for causality.

### C7. Executive versus ops variants

| | Executive (CEO/COO/CFO) | Ops/finance manager |
|---|---|---|
| Surface | Brief by email/mobile, tap into a case | Cases queue, filters, keyboard |
| Volume | At most 3 items per brief; zero is fine | All open cases for their area |
| Detail default | Bottom line box and one-line evidence | Full case file |
| Actions | Decide, assign, snooze | Investigate, close, tune thresholds |
| Language | Dollars, customers, deadlines | Adds metric definitions and source records |
| Model editing | Rare, via "Is this right?" prompts | Owns the Business Model page |

### C8. Notification policy (quiet by default)

Hypotheses to test:
1. Hard cap: at most 1 push per day and at most 3 items per brief. If more qualify, rank by dollar impact times urgency times confidence, and show the rest as "N more in Cases".
2. Three tiers only:
   - **Interrupt** (rare, same-day): large dollar effect plus time sensitivity (for example, payment processing failing, cash will not cover payroll). Target under 1 per month per company. Needs observation confidence "confirmed".
   - **Brief** (default): included in the weekly (or twice-weekly) summary.
   - **Archive**: logged in Cases, never pushed.
3. Nothing is pushed on explanation confidence alone. If the observation is solid but the cause is unclear, push as "something changed, cause unknown, here is the question we need answered".
4. Dedupe and group: one case per underlying issue (Anodot-style correlation), and update the case instead of sending a new message.
5. Self-tightening: if the user dismisses or ignores three items of one type, ask once "Should I stop flagging this?" and then lower its tier.
6. Quiet hours, owner-based routing, and a visible "Notification budget" setting in plain language ("urgent only / weekly / weekly plus urgent").
7. Instrument the fatigue metrics from day one: open rate, action rate, dismissal rate, "not useful" rate, time to disposition, and the share of weeks with zero items. If the action rate falls below an agreed floor, cut volume rather than add features.
8. Precision target: choose a floor (for example, most surfaced items judged "material" by the owner) and report it internally. The evidence in A2 says this matters more than design.

### C9. Product-name and category directions

Category phrasing options (check how buyers search before committing): "business watchdog", "AI chief of staff for operations", "exception intelligence", "continuous business review", "decision intelligence for SMB" (Aera, Cloverpop already use "decision intelligence", so this is crowded).

Name directions. Conflict notes are from limited web search and are not trademark clearance.

1. **Casefile**: reflects the case-file anatomy and the "investigation" value. Generic English word, so likely hard to own. Many legal/case-management products use similar terms.
2. **Nightwatch**: suggests quiet watching. Likely crowded in monitoring and entertainment.
3. **Overlook**: double meaning (oversight, and things overlooked). Possible negative connotation and brand confusion. No conflict found in my search, but not verified.
4. **Margin Note**: a note in the margin of the business. Soft, non-technical. Unchecked.
5. **Ledgerlight**: finance-flavored, shines light on the ledger. I did not find a conflict, but this is not verified.
6. **The Rundown / Rundown**: familiar briefing language. Heavily used by newsletters, so likely conflicts.
7. **Hindsight (follow-up loop)**: stresses outcomes. Heavily used already (several software products).
8. **Quorum**: decisions and sign-off. Used by several software firms (unverified count).
9. **Lookout**: plain, protective. Common in security products (Lookout Mobile Security), so probably a conflict.
10. **Watchtower**: strongest "monitoring" metaphor, but verified crowded (A6). Avoid.

Recommendation on naming: prefer a coined or compound name over a common word, since AI-category naming disputes are active (A6). Pick two finalists, run USPTO/EUIPO and domain checks, and test the name with five owners for "what do you think this does".

### C10. Risks and open questions

- Precision is the product. Define and measure "material" with design partners before investing in polish.
- The evidence base for channel preference among SMB owners is thin and dated. Run a two-week test of email versus Slack versus WhatsApp-link delivery with actual customers.
- Hypothesis display and confidence wording are untested with non-technical users. The academic evidence says explanations and numbers can raise acceptance without improving correctness, so test with seeded wrong explanations and measure whether users catch them.
- Outcome attribution: avoid overclaiming causal impact in the follow-up loop.
- Access and permissions: a brief that carries financial data by email creates leakage risk. Consider "summary in email, detail behind login" as the default.
- Vendor accuracy claims (Datadog, Resolve, Cleric, Anodot, Cloverpop) are all self-reported. Do not use them as benchmarks in investor material without caveats.

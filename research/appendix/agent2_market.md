# Agent 2: Customer Pain and Market Validation
Date: 2026-11-19. Scope: B2B SaaS that monitors company data, detects material problems, investigates root cause, estimates impact, tracks decisions and outcomes, aimed at SMB and mid-market firms without data teams.

## 0. Method and limits (read first)
- All evidence came from web search result summaries. WebFetch could not reach several hosts (velosio.com, erp.intuit.com were blocked by the session network). I could not open primary PDFs (MIT NANDA, Gartner bodies, McKinsey). Every figure below is therefore "as reported by the cited page." Verify against primaries before putting numbers in a deck.
- I could NOT retrieve actual r/BusinessIntelligence, r/dataengineering, r/NetSuite, r/supplychain or r/manufacturing threads. Search returned only mirrors of r/excel, r/datascience, r/analytics threads and community forums. Where I quote practitioner voices, I label them anecdote and name the actual source. No Reddit quote is invented. Gap: the founder should do 2-3 hours of direct Reddit/HN reading (suggested queries in section 7).
- Reliability tags used: [IND] independent/government/regulatory filing; [ANALYST] analyst or academic with unclear sponsor; [VENDOR] vendor-run survey or blog (biased toward selling a fix); [ANEC] anecdote.
- Scores in section 5 are marked S (sourced in part) or J (my judgment).

## 1. Customer frustration with BI, AI analytics and enterprise AI

### 1.1 Verified-ish data on AI pilot failure
| Claim | Source | Reliability |
|---|---|---|
| MIT NANDA "GenAI Divide: State of AI in Business 2025" says ~95% of enterprise GenAI pilots show no measurable P&L return; based on 300+ public deployments, 350 employee surveys, 150 leader interviews. Cause named: a "learning gap" (tools do not retain feedback, adapt to context, or integrate into workflows). | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ ; https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html ; https://www.thinkdigital.travel/research-directory/the-genai-divide-state-of-ai-in-business-2025 | [ANALYST], preliminary, small sample, authors promote their own NANDA agentic infrastructure project; headline widely disputed. Treat as directional. |
| Same report (via secondary coverage): purchased vendor tools succeed ~2x as often as internal builds (often quoted 67% vs 33%); back-office automation showed clearer ROI than sales/marketing pilots. | https://www.legal.io/blog/5719519/MIT-Report-Finds-95-of-AI-Pilots-Fail ; https://nationalcioreview.com/articles-insights/extra-bytes/mit-finds-genai-projects-fail-roi-in-95-of-companies/ | Secondary only; one outlet gives a different split. Useful framing for a founder: buy-not-build favors a vendor, and back-office is where ROI shows. |
| Gartner (June 2025): over 40% of agentic AI projects will be canceled by end of 2027 due to cost, unclear value, weak risk controls; only ~130 of thousands of "agentic" vendors are real. | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | [ANALYST] prediction, not measurement. Gartner sells advisory. |
| McKinsey State of AI 2025 (1,993 respondents, fielded June-July 2025): 88% use AI in at least one function; 62% at least experimenting with agents; only ~39% report any enterprise EBIT impact, most under 5%; ~6% are "high performers." | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025 ; secondary figures via https://itbrief.co.uk/story/mckinsey-report-shows-ai-interest-but-slow-scaling | [ANALYST] self-reported survey, skewed to larger firms. |

Read-across for this founder: enterprise-class evidence says value fails at integration, context and trust, not at model quality. An SMB product that arrives pre-integrated for one narrow job fits that diagnosis. None of this data covers SMBs well.

### 1.2 Chat-with-your-data / text-to-SQL trust problem
- Practitioners and vendors report that benchmark accuracy does not carry to a company's own schema; silent wrong-but-plausible numbers are the worst failure; same question can yield different SQL on different runs. Example claims: "85% benchmark vs roughly half of answers wrong in an internal review"; 38% of GPT-4o failures from wrong join paths and 24% from missing tables. https://tianpan.co/blog/2026-04-19-text-to-sql-at-scale-production ; https://omni.co/blog/why-text-to-sql-fails ; https://www.getcollate.io/blog/your-text-to-sql-problem-is-not-the-llm . Reliability: [VENDOR]/blog, each selling a semantic layer or catalog. Direction is consistent across many unrelated sellers, which raises confidence, but specific percentages are unverified.
- Salesforce reportedly got from ~50% to ~80% efficacy only by generating 10 candidate queries and scoring consistency (reported in the same tianpan piece). [VENDOR]/secondhand.
- Hacker News, Vanna.ai "chat with your SQL database" thread (Jan 2024, 547 points): one commenter said wrong numbers from an AI would be as bad as dashboards that "lie." https://news.ycombinator.com/item?id=38992601 . [ANEC], single comment, 2024.
- Power BI Copilot: Microsoft documentation warns generated DAX, narratives and summaries can be incorrect; consultants say errors trace to weak semantic models and undefined KPIs; business users trust AI answers only when they match certified reports. https://blog.bismart.com/en/power-bi-copilot-errors-wrong-answers ; https://www.metricinsights.com/blog/why-enterprises-stumble-on-ai-for-bi/ ; https://spaces.collab365.com/posts/microsoft-says-copilot-answers-in-excel-and-power--deHRzB . [VENDOR]/consultant.
- Implication: "answers with evidence and confidence" (the founder's thesis) targets a real trust gap. But the same sources say the root fix is metric definitions, so the product must ship with a curated, vertical-specific metric layer rather than free-form Q&A.

### 1.3 Dashboard and BI fatigue
- Stakeholders keep Excel next to BI. Example from r/excel mirror: a manager had to rebuild a Power BI dashboard in Excel to justify differences from stakeholder figures (annualized vs trailing-12-month; fee classified as COGS); commenter described running two parallel systems. https://redlib.hackliberty.org/r/excel/comments/1enw6vy/little_excel_saved_the_day/lhap6an/?context=3 . [ANEC], r/excel not r/BusinessIntelligence.
- Finance "bought a BI tool and went back to Excel" because they need to drill from a total to the transaction behind it. https://www.velixo.com/why-finance-bought-a-bi-tool-and-went-back-to-excel/ . [VENDOR] (Excel add-in seller).
- "Why" questions are the unmet part: dashboards show what happened; ad hoc analysis is mainly "why." https://hex.tech/blog/from-dashboards-to-decisions/ . [VENDOR].
- Claims that 60-70% of dashboards go unused and analysts spend 40-60% of time on ad hoc requests appear in a vendor blog with no primary study: https://sds.apps.streamdata.com/blog/the-dashboard-delusion . [VENDOR], do NOT cite as fact.
- G2/Capterra review themes (review counts, not satisfaction): "learning curve" is a top con for Power BI (75 G2 reviews) and Tableau (275, plus 240 on "learning difficulty"); Power BI slow performance (65); small-company reviewers call Tableau licenses expensive. https://www.g2.com/compare/microsoft-microsoft-power-bi-vs-the-ikigai-platform-vs-tableau ; https://www.softwareadvice.com/marketing/tableau-profile/reviews/ ; https://www.capterra.com/p/176586/Power-BI/reviews/ . [IND-ish] review aggregator counts; I did not read the full review pages.

### 1.4 Shopify merchants: profit blindness
- Shopify Community threads: Shopify shows revenue and gross margin only if COGS is entered; it does not natively deduct shipping, transaction fees or ad spend; "you don't know which orders/products/channels are actually profitable until you sit down with a spreadsheet at month-end." https://community.shopify.com/t/understanding-profit-tracking-for-shopify-stores/657805 ; https://community.shopify.com/t/profit-ad-spend-tracking-on-shopify-whats-actually-broken-for-you/646399 . [ANEC], merchant forum posts (and some seller-run threads). 
- Several profit-tracking apps already exist (TrueProfit, Triple Whale, Polar, Lifetimely, Bloom), so this specific pain is real but crowded. Pricing in 3.4 below.

## 2. What SMB and mid-market operators still do manually after buying tools
| Manual task | Evidence | Reliability |
|---|---|---|
| Manual data entry and reconciliation: ~25 hours/week at US firms with 10-99 employees (Intuit survey, Aug 2024, n=630) | https://quickbooks.intuit.com/r/enterprise/business-solutions-survey-2024 (could not open; figure via search summary) | [VENDOR] (Intuit sells QuickBooks Enterprise) |
| 68% of 151 US mid-market ERP decision-makers lose 11+ hours/week to manual reconciliation; 91% take 4+ days to close the books | https://www.velosio.com/research/the-real-cost-of-delayed-erp-modernization/ (not opened; via summary) | [VENDOR] (Velosio is a Microsoft ERP partner) |
| Nearly 50% of small businesses still use spreadsheets for core financial functions (SMB Group, as cited by a blog) | https://resourcefulfinancepro.com/news/finance-automation-spreadsheets | [ANALYST] via blog; date and sample unknown |
| Spreadsheets remain part of operations in ~90% of organizations even after ERP (AutoRek) | https://techradar.com/pro/almost-all-firms-are-still-reliant-on-spreadsheets-is-it-time-for-change | [VENDOR]; mostly larger firms |
| 96% of manufacturers still rely on Excel for cost estimation (Galorath 2025, 180 cost professionals) | https://galorath.com/?p=1728 | [VENDOR], not small-manufacturer specific |
| 2025 survey of 300 manufacturing and distribution execs: 99% changed prices amid volatility, only ~half had strong confidence in margin-impact visibility | https://www.aktion.com/how-manufacturers-can-tackle-rising-costs-and-margin-pressure-in-2025/ (cited via search) | [VENDOR] |
| 64% of 70 MRPeasy customer case studies relied on spreadsheets before ERP | https://www.themanufacturer.com/articles/erp-statistics-insights-from-70-manufacturing-case-studies/ | [VENDOR] sample, self-selected |
| Distributors: margin leaks through override habits, cost pass-through timing, supplier reconciliation cycles of 3-6 months (survey of 200+ executives) | https://distributionstrategy.com/report/the-state-of-distributor-profitability/ | [ANALYST]/consultancy; abstract only |
| Shopify brands: month-end spreadsheet to learn true profit by product and channel | see 1.4 | [ANEC] |

Recurring manual jobs (synthesis, J): weekly KPI review pulled from 3-5 exports; month-end "why is gross margin down" variance explanation; vendor cost change pass-through to price lists; inventory reorder list built in Excel; AR aging chase; carrier invoice checks. Common thread: the number is visible, the cause is not, and the owner must ask a person.

## 3. Market size and demand evidence

### 3.1 Market estimates (all vendor/market-research firms; wide disagreement)
| Estimate | Source | Bias note |
|---|---|---|
| BI market ~$38.2B in 2025 to $56.3B by 2030 (8.2% CAGR); another Mordor listing gives $70B by 2030 at 13.2% | https://www.marketresearch.com/Mordor-Intelligence-LLP-v4018/Business-Intelligence-BI-Share-Trends-36226918 | Paid research-report publishers; the same firm gives two numbers |
| $32.3B (2025) to $56.9B (2032), 7.2% | https://www.meticulousresearch.com/pressrelease/640/business-intelligence-market | same |
| $33.5B (2025) to $57.3B (2031), 9.4% | https://www.techsciresearch.com/report/business-intelligence-market/24175.html | same |
| BI and analytics platforms +$20.7B 2024-2029, 8.4% | https://www.technavio.com/report/business-intelligence-and-analytics-platforms-market-industry-analysis | same |
| "Enterprise analytics software" $226B (2025) to $416B (2030) | https://www.knowledge-sourcing.com/resources/press-releases/enterprise-analytics-software-market | Far broader scope; not comparable |
Consensus (J): BI is roughly $32-39B growing 7-9%. This is mostly enterprise seats; the SMB slice is unquantified in my sources. Do not use TAM figures for the pitch; build a bottom-up count of reachable firms x ARPA (section 3.3).
- Decision intelligence: Gartner published its first Magic Quadrant for Decision Intelligence Platforms in January 2026 (leaders: FICO, SAS, Aera Technology, IBM, ACTICO). https://sdtimes.com/ai/gartner-acknowledges-growth-of-decision-intelligence-platforms-with-inaugural-magic-quadrant/ . The category is now named and enterprise-priced; trade press notes adoption is hindered by leaders' reluctance to track decisions (https://briefglance.com/articles/dawn-of-decision-intelligence-gartners-new-magic-quadrant-arrives), which supports the "decision and outcome tracking" feature as both valuable and hard to sell. I found no credible market-size number for it.

### 3.2 SMB data capability (the founder's premise)
- Techaisle: fewer than one-third of small businesses (1-99 employees) have deployed analytics vs 77% of midmarket (100-999); ~80% of small businesses describe analytics use as ad hoc or descriptive; only 6% of small and 27% of midmarket firms are "highly data-driven." https://www.techaisle.com/blog/361-ww-smb-and-midmarket-analytics-adoption-acceleration-needs-external-services . [ANALYST], SMB-specialist research firm; date not confirmed in my snippet. Best available support for "SMBs lack analytics."
- Census Bureau BTOS: fewer than 20% of firms with 4 or fewer employees reported using AI (Dec 2025-May 2026 data window, per search summary). [IND], government; I did not open it.
- B2B companies have the lowest data-role ratio, ~2.4% of workforce, among ~100 scaleups studied (https://www.synq.io/blog/data-team-size-at-100-scaleups); a data analyst costs $80-120K before benefits (https://www.fabi.ai/blog/data-team-no-budget). [VENDOR]. A firm with 50 employees therefore has roughly 1 data person at most, usually none.
- Only 27% of SMBs have BI budgets above $10K/year (Mewayz, uses its own user base): https://mewayz.com/ug/blog/the-business-intelligence-report-2025-how-smbs-make-data-driven-decisions . [VENDOR], low confidence.

### 3.3 Stack adoption (reachability)
- Xero: 4.92M subscribers at FY26 (31 March 2026), +11% YoY; revenue up 31%; acquired Melio (US payments). https://www.fool.com.au/2026/05/14/xero-fy26-result-revenue-surges-31-but-profit-dips-due-to-melio-acquisition-costs/ ; ASX filing https://announcements.asx.com.au/asxpdf/20260514/pdf/06zkqzlkq0xnph.pdf . [IND], company results.
- Shopify: FY2025 10-K says "millions of merchants" in 175+ countries https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm [IND]; third-party live-store counts range from ~2.8M (StoreLeads) to 6.9M (BuiltWith), ~47K Plus stores (https://colorlib.com/wp/shopify-statistics/) [ANALYST/aggregator; definitions differ].
- QuickBooks, NetSuite, Odoo user counts: searches returned nothing reliable. GAP. (Founder can pull from Intuit 10-K, Oracle filings, Odoo press.)
- Implication (J): the integration surfaces with the largest SMB reach are Shopify, QuickBooks Online and Xero, all with app marketplaces and open APIs. NetSuite and Odoo are narrower but richer for operations data.

### 3.4 Willingness-to-pay anchors (what comparable tools cost)
| Tool | Reported price | Source | Reliability |
|---|---|---|---|
| Power BI Pro | ~$10/user/month; Tableau Creator ~$70 | https://aglowiditsolutions.com/blog/power-bi-vs-tableau/ | blog; verify |
| Fathom (accountant-led reporting) | ~$50-53/mo single company; ~$260-380/mo tiers | https://www.capterra.com/p/136476/Fathom/pricing/ ; https://www.getapp.com/business-intelligence-analytics-software/a/fathom/ | third-party listing |
| Jirav | conflicting: $50-150/mo vs ~$10K/yr | https://eightx.co/blog/compare/how-much-does-jirav-cost | unresolved |
| Cube / Mosaic | ~$25-80K/yr; ~$30-60K/yr, quote-based | https://beancount.io/blog/2026/10/31/cube-vs-jirav-vs-datarails-fpa-software-compared-guide | third-party estimates |
| Shopify analytics: Lifetimely ~$49-149/mo; Triple Whale ~$179-749/mo at low GMV (other source $549-1,349); Polar ~$300-720/mo | https://www.ringly.io/blog/triple-whale-alternatives ; https://www.conjura.com/blog/polar-analytics-pricing-in-2025-costs-features-and-best-alternatives | conflicting, vendor-adjacent |
| Fractional CFO engagements | $3,000-10,000/mo | https://www.eaglerockcfo.com/blog/research/client-advisory-services-market-report | firm's own report |
| Freight audit services | 25-50% of recovered dollars (contingency) | https://www.fulfill.com/blog-posts/parcel-audit-guide | vendor |
Read-across (J): self-serve SMB analytics clusters at $50-$750/month; mid-market finance/ops tools at $25-80K/year; services (CFO, audit) are priced on outcomes. A founder can credibly price $200-$1,500/month if the product names a dollar problem; below $100/month it competes with commodity dashboards and cannot fund sales. Contingency pricing on recovered or saved dollars is an established norm in audit categories.

## 4. Vendor-sourced cost-of-problem figures by theme (use as hypotheses only)
- Inventory distortion: IHL Group puts global cost of out-of-stocks plus overstocks at ~$1.73T/year (~6.5% of retail sales), research sponsored by Board (a planning vendor). https://www.ihlservices.com/news/analyst-corner/2025/09/retail-inventory-crisis-persists-despite-172-billion-in-improvements ; https://www.board.com/resources/the-1-73-trillion-wake-up-call . [VENDOR-sponsored]; internal sources disagree on exact share. Distributors: many hold 2-3 months of stock; ~49% overbuy because stockout pressure exceeds excess pressure (Phocas survey, 100+ distributors) https://www.phocassoftware.com/l/distribution-industry-trends-report [VENDOR]; NAW/MDM: 62% expect COGS up 10%+ in 2025 https://www.mhlnews.com/transportation-distribution/news/55287944/tariffs-driving-cost-for-wholesale-distribution-industry [trade association, better].
- Construction: profit fade averages ~5% of project margin, one third typically 7%+ (Dodge, JLC survey via blog) https://archdesk.com/blog/construction-project-margin-fade ; https://www.jlconline.com/?p=40496 [mixed; blog-relayed].
- Healthcare: initial denial rate ~11.6% in 2025 across ~2,300 hospitals (Kodiak); leakage 3-5% of net revenue (vendor); McKinsey-cited rise from 9% (2016) to 15% (2023). https://www.physicianspractice.com/view/denial-rates-are-rising-here-s-how-to-fight-back ; https://www.adsc.com/2026-rcm-revenue-leakage-checklist . Hospital-scale data, vendor leakage estimates; small practices are different and heavily served by billing companies.
- SaaS: ~9% of MRR lost to failed payments on average across 119 B2B SaaS companies (Baremetrics, May 2026 sample); involuntary churn ~20-40% of total churn; smart retries recover ~68% of failures. https://www.withorb.com/blog/dunning-failed-payment-recovery-statistics ; https://chargehive.com/blog/involuntary-vs-voluntary-churn-saas [VENDOR]. Stripe-native tools (Baremetrics, ChartMogul, dunning apps) already address this.
- Freight/3PL: recoverable billing errors 1-5% of freight spend (up to 3-10% per Tompkins via vendors); disputes typically within ~180 days. https://www.fulfill.com/blog-posts/parcel-audit-guide ; https://www.traxtech.com/blog/a-primer-on-freight-audit-recovery [VENDOR]. Mature audit-and-recovery vendors exist.
- Cash flow / late payment: US owners (Gateway, 2025, n=503): 64% have invoices 90+ days overdue, average 11% of annual revenue delayed. Xero Q2 2026 small-business data: average 29.3 days to get paid, ~9 days late. https://www.actionnewsjax.com/news/real-cost-late/PSLENA6EKMYNXN2WIUNCA7KDW4/ ; Intuit UK 2025 report https://quickbooks.intuit.com/uk/blog/small-business-late-payments-report-2025/ . The Xero figure is from platform data (stronger); Gateway is lender-sponsored.

## 5. Vertical scoring (1 = poor for this founder, 5 = excellent; higher is better in every column, including Competition where 5 = little competition and Sales cycle where 5 = short)
Criteria: P pain severity, F financial impact, Q frequency, D data availability, I integration ease, W willingness to pay, S sales cycle, C competition (5 = open), A pilot access, R measurable ROI, K capital-light start, E expansion. All scores are J (my judgment) informed by the sourced facts noted in the last column; "S" in the note means a sourced fact informs it, not that the score itself is measured.

| Vertical | P | F | Q | D | I | W | S | C | A | R | K | E | Total /60 | Evidence-based justification (flag) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E-commerce/DTC (Shopify) | 4 | 4 | 5 | 5 | 5 | 3 | 5 | 2 | 5 | 4 | 5 | 3 | 50 | Open API, daily data, thin margins, forum-documented profit blindness (S: Shopify Community); but profit apps priced $49-750/mo are crowded and churn-prone (S: pricing sources). Judgment on scores. |
| Wholesale distribution | 4 | 5 | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 5 | 4 | 4 | 46 | Margin leakage via overrides and cost pass-through, overstock buffers (S: Distribution Strategy, Phocas, NAW); data sits in NetSuite/Epicor/Acumatica or Excel, uneven. Judgment on scores. |
| Manufacturing (SMB) | 5 | 5 | 4 | 2 | 2 | 4 | 2 | 4 | 3 | 4 | 3 | 4 | 42 | Costing visibility gaps and Excel reliance (S, vendor sources); messy ERP/shop-floor data and long integrations. Judgment. |
| Logistics/3PL | 4 | 4 | 5 | 3 | 3 | 4 | 3 | 2 | 3 | 5 | 3 | 3 | 42 | Invoice errors are recoverable and measurable (S: 1-5% of freight spend, vendor); mature audit competitors and TMS/WMS fragmentation. Judgment. |
| B2B SaaS companies | 3 | 3 | 5 | 5 | 5 | 4 | 4 | 1 | 4 | 4 | 5 | 3 | 46 | Easiest data (Stripe, HubSpot, product) and ~9% MRR failed payments (S: Baremetrics via vendor); but ChartMogul, Baremetrics, ProfitWell-type tools plus founders who build in-house make it the most crowded. Judgment. |
| Professional services/agencies | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 3 | 5 | 3 | 5 | 3 | 44 | Utilization and project margin visible in time-tracking plus accounting; founders reachable via communities; modest dollar leaks; competitors are PSA suites. Judgment. |
| Retail (SMB, brick-and-mortar) | 4 | 4 | 5 | 3 | 3 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 41 | Inventory distortion is large at scale (S: IHL, vendor-sponsored), but POS fragmentation and thin IT. Judgment. |
| Healthcare practices | 4 | 4 | 4 | 2 | 1 | 3 | 1 | 3 | 2 | 4 | 1 | 3 | 32 | Denials/leakage real (S: Kodiak, McKinsey-cited) but HIPAA, EHR integration and incumbent RCM firms make it capital-heavy. Judgment. |
| Construction | 4 | 5 | 3 | 2 | 2 | 3 | 3 | 3 | 3 | 4 | 3 | 3 | 38 | Profit fade ~5% of margin (S: Dodge/JLC via blog), but data is job-cost in Sage/Procore/Excel and field-driven. Judgment. |
| Others identified: Specialty food/CPG brands (Shopify + wholesale) | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 | 4 | 46 | Blend of DTC and distributor margin and inventory problems; reachable via Shopify and accounting stacks. Judgment, no direct source. |
| Others: Multi-location services (restaurants, clinics, home services) | 3 | 3 | 5 | 3 | 3 | 3 | 4 | 2 | 3 | 3 | 4 | 3 | 39 | Frequent but crowded with vertical POS dashboards. Judgment. |

Reading the table (J): the top candidates by this scoring are DTC/Shopify (50) then wholesale distribution, B2B SaaS and specialty CPG (all 46). Ranking by total hides the real tradeoff: DTC and SaaS are easy to reach and hardest to defend; distribution and manufacturing pay most per customer but need heavier integration. The scores are not statistically derived and should be tested via the pilot interviews in section 7.

## 6. Top 8 candidate narrow problems (ranked)
Ranking logic (J): weigh dollars at stake, recurrence, data accessibility without a data team, a clear "why" the existing tool cannot answer, and a one-quarter route to a pilot.

### Rank 1: Margin erosion explained by product/customer/channel (cost, price, mix, freight, discount drivers)
- Customer: owner/CFO/controller at a 10-200-person distributor, specialty CPG or Shopify brand with gross margin pressure.
- Workaround: month-end Excel bridge from ERP/Shopify/accounting exports; ad hoc "why did GM drop 2 points."
- Impact: distributors face COGS +10% and 25% supplier hikes (S: NAW 2025, https://www.mhlnews.com/transportation-distribution/news/55287944/tariffs-driving-cost-for-wholesale-distribution-industry); only ~half confident of margin-impact visibility (vendor survey, https://www.aktion.com/how-manufacturers-can-tackle-rising-costs-and-margin-pressure-in-2025/); margin leaks through overrides and pass-through timing (https://distributionstrategy.com/report/the-state-of-distributor-profitability/). Dollar value per customer is a hypothesis: even 0.5 point of margin on $20M revenue is $100K/year (J, arithmetic).
- Why tools fail: BI shows the margin; it does not decompose it into price vs cost vs mix vs freight with evidence; ERPs report standard cost vs actual only when someone builds the report.

### Rank 2: Supplier cost change pass-through / price leakage (distributors)
- Customer: distributor sales ops or pricing lead.
- Workaround: spreadsheet price lists updated manually; reps override.
- Impact: same sources; supplier reconciliation cycles 3-6 months (Distribution Strategy, abstract only).
- Why tools fail: ERP pricing modules exist but few SMBs use them; BI does not alert on "cost rose, price did not."
- Note: overlaps Rank 1 and may be the sharper entry wedge because it is a detectable event (a supplier invoice price versus sell price).

### Rank 3: Inventory stockout/overstock early warning with root cause (SKU level)
- Customer: ops head at Shopify brand or distributor.
- Workaround: Excel reorder sheets, tribal knowledge.
- Impact: IHL $1.73T global (vendor-sponsored; not a per-firm number); distributors holding 2-3 months of stock and overbuying (Phocas, vendor).
- Why tools fail: inventory planners (Cogsy, Inventory Planner, etc.) forecast but do not explain "why did we stock out" (supplier delay vs demand spike vs bad lead-time assumption). Competition is real; I did not survey them (GAP).

### Rank 4: Shopify true-profit and ad-efficiency anomaly detection
- Customer: DTC founder/ops lead, $1-20M GMV.
- Workaround: spreadsheet at month-end (Shopify Community, anecdote).
- Impact: unknown per brand; thin margins make a few points material (J).
- Why tools fail: profit dashboards report; few alert on contribution-margin drops with causes. But 5+ funded apps and $49-750/mo anchors cap price.

### Rank 5: Carrier/3PL invoice and service-failure recovery
- Customer: shipper or 3PL finance lead.
- Workaround: ignore, or pay an auditor 25-50% of recoveries.
- Impact: 1-5% of freight spend recoverable (vendor); 180-day dispute window creates urgency.
- Why tools fail: audit vendors are contingency-fee services, not software; SMB shippers on a 3PL's carrier account cannot see invoices at all (https://www.fulfill.com/blog-posts/parcel-audit-guide).
- Strong ROI measurability, but a services-like business and incumbents exist.

### Rank 6: Cash-flow risk from late receivables and upcoming payables
- Customer: owner/bookkeeper of a services or B2B firm on Xero/QuickBooks.
- Workaround: weekly AR aging review, spreadsheet 13-week forecast.
- Impact: Xero platform data: 29.3 days to get paid, ~9 days late (https://www.actionnewsjax.com/news/real-cost-late/PSLENA6EKMYNXN2WIUNCA7KDW4/ is the Gateway report; Xero figures cited in same search summary); Gateway: 11% of annual revenue delayed (lender-sponsored).
- Why tools fail: strong crowded field (Fathom, Float, Pulse, Xero/Intuit native forecasting). Pain real, wedge weak, platforms moving into it.

### Rank 7: SaaS revenue leakage and churn diagnosis (failed payments, plan mismatch, expansion drop)
- Customer: B2B SaaS founder, $1-10M ARR.
- Workaround: Stripe dashboard, Baremetrics/ChartMogul, spreadsheets.
- Impact: ~9% of MRR touched by failed payments, 68% recoverable via retries (vendor).
- Why tools fail: mostly they do not; the category is well served and founders build their own. Lowest defensibility.

### Rank 8: Month-end variance explanation (budget vs actual, with evidence)
- Customer: controller or fractional CFO at a 20-200 person firm.
- Workaround: 4+ days to close at 91% of mid-market firms (vendor); manual variance commentary.
- Impact: time cost (11+ hours/week reconciliation, vendor); no direct dollar leak.
- Why tools fail: FP&A tools (Cube, Mosaic, Datarails; $25-80K/year) are enterprise-priced; Fathom covers cheap reporting without root cause. A gap exists, but it is a time-saver, not a money-finder, so willingness to pay is weaker. It works well as a feature inside Rank 1, not as a standalone wedge.

Also considered, not ranked: supplier delay prediction (needs PO/EDI data many SMBs lack; I found no SMB-specific evidence), fulfillment delays (carrier-side data is accessible but ROI hard to measure), AP duplicate-payment detection (not researched).

## 7. How an unfunded founder gets real pilots beyond cold outreach
Evidence quality here is the weakest section; most evidence shows channels exist, not that they convert for a first-time founder.

| Channel | What the evidence shows | Source | Reliability |
|---|---|---|---|
| Accounting platform marketplaces (Xero App Store, Intuit App Center, Shopify App Store) | Xero App Store offers subscription billing APIs and a 15% referral share on new-customer subscriptions; developers can still sell elsewhere; 4.92M Xero subscribers is the reachable base | https://www.xero.com/my/media-releases/introducing-the-xero-app-store ; https://itwire.com/business-it-news/business-software/xero-opens-its-app-store,-adds-subscription-api ; FY26 numbers in 3.3 | launch-era press; terms may have changed; no conversion data found. One commentator says small developers face barriers (https://www.accountingweb.co.uk/ opinion, ANEC). |
| Fractional CFOs and advisory-led accounting firms | Firms are shifting toward advisory; fractional CFO engagements $3-10K/month; partner programs pay referral fees of $50-300 per referral (Relay); accountants want forward-looking tooling | https://njbiz.com/fractional-cfo-services-small-business-demand/ ; https://relayfi.com/blog/fractional-cfo-services-for-accountants/ ; https://www.planguru.com/?p=43 | vendor/marketing; plausible but unproven for a new product. One fractional CFO can bring 5-20 clients, which is the practical pilot multiplier (J). |
| Fathom-style accountant-led distribution | Fathom is priced per company with multi-company tiers sold through accounting practices (as shown in pricing listings) | https://www.capterra.com/p/136476/Fathom/pricing/ | listing only; suggests accountant channel works commercially (J inference) |
| ERP partners/resellers (NetSuite, Acumatica, Odoo, MRPeasy-type) | Resellers publish content on spreadsheet reliance (Velosio, Aktion, Phocas) because it sells ERP; they own post-implementation relationships and see the "manual after go-live" problem | https://www.velosio.com/research/the-real-cost-of-delayed-erp-modernization/ ; https://www.aktion.com/how-manufacturers-can-tackle-rising-costs-and-margin-pressure-in-2025/ | indicates incentive alignment, not proven pilot flow |
| Trade associations (NAW for distributors, Distribution Strategy Group) | Publish member surveys on margin and inventory; members actively seek benchmarks | https://www.mhlnews.com/transportation-distribution/news/55287944/tariffs-driving-cost-for-wholesale-distribution-industry ; https://distributionstrategy.com/report/the-state-of-distributor-profitability/ | evidence of demand for benchmarks, not of pilot acceptance |
| Shopify/ecommerce communities (Shopify Community, r/ecommerce, DTC Slack/Discords) | Merchants openly describe profit-tracking pain; a founder asking "what's actually broken" gets responses (note: one such thread was itself posed by a vendor) | https://community.shopify.com/t/profit-ad-spend-tracking-on-shopify-whats-actually-broken-for-you/646399 | [ANEC] |

Practical pilot design (J, not sourced): offer a free, one-time "margin leak audit" delivered as a report from read-only data exports, pitched through 3-5 fractional CFOs/accountants and 1-2 ERP resellers; convert to monthly monitoring with contingency or outcome-linked pricing. This gets real data and fastest learning without integration engineering. Run it in two verticals at once (e.g., Shopify brands and a distributor niche) to compare which converts.

Direct research to close the evidence gaps (about two hours):
1. Reddit: search `site:reddit.com r/NetSuite "reporting"`, `r/supplychain "stockout" excel`, `r/ecommerce "real profit"`, `r/Bookkeeping "fractional CFO"`, `r/smallbusiness "cash flow forecast"`. Capture 15-20 verbatim posts with permalinks.
2. Hacker News: "Show HN" threads for AI analytics, text-to-SQL, and "why did revenue drop" tools; read top comments.
3. Pull QuickBooks, NetSuite, Odoo counts from filings (Intuit 10-K, Oracle 10-K, Odoo press).
4. Read the MIT NANDA PDF directly and Techaisle's source report to confirm date and sample.

## 8. Summary of conclusions
1. Pain: verified at the level of "BI and AI tools show numbers but not causes, and users do not trust AI answers without evidence" (many consistent but largely vendor-authored sources; enterprise studies from MIT, Gartner, McKinsey agree on poor realized value). Evidence for SMB specifically is thinner and mostly vendor-run.
2. Manual work after tool purchase is well documented (spreadsheet reconciliation hours, month-end closes), mostly by vendors with an incentive; treat hours as indicative.
3. Market size figures are unreliable and enterprise-skewed; the decision to proceed should rest on bottom-up pilot economics, not $38B TAM.
4. Price anchors: $50-750/month self-serve; $25-80K/year mid-market FP&A; contingency models in audit. Pricing of $200-1,500/month tied to named dollars is plausible (J).
5. Best-scoring wedge areas (J): margin erosion/price-cost leakage for distributors and specialty brands, with Shopify DTC as the easiest integration and fastest pilot but weakest defensibility.
6. Biggest unknowns: whether SMB owners will pay for causal explanations versus alerts; whether data access (ERP exports) can be obtained without implementation work; whether accountants/fractional CFOs will actually resell. Test these first.

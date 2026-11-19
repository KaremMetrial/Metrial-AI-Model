W = dict(wtp=20, dollar=12, pain=8, open=12, data=12, ttv=8, acc=6, rec=6, exp=8, inb=8)
# order: wtp, dollar, pain, open, data, ttv, acc, rec, exp, inb
S = {
 "Margin / price-cost investigation (cross-system)":      (2,4,4,3,4,4,3,4,5,3),
 "Cash flow + AR collections prioritisation":             (3.5,3.5,4,2,5,5,4,5,4,4),
 "Payout / bank / ledger reconciliation":                 (4,3,4,2,3,3,1,5,3,4),
 "Churn & revenue-risk investigation (billing-first)":    (3,4,5,2,3,4,4,4,5,4),
 "Revenue leakage / billing errors":                      (2,4,4,3,2,1,2,3,4,2),
 "Inventory / stock anomaly investigation":               (2,3,3,3,2,3,2,4,5,3),
 "Procurement / supplier price-creep & pass-through":     (2,4,4,4,1,2,2,3,5,2),
 "Freight / parcel invoice audit":                        (5,3,3,1,2,2,2,4,3,3),
 "Returns & refunds root cause":                          (2,3,4,3,3,3,3,3,4,3),
 "B2B price / rep-override / rebate leakage":             (2,4,4,3,2,2,3,3,5,1),
 "Ad-spend / campaign contribution-margin anomalies":     (3,3,3,1,4,4,2,5,3,4),
 "Retailer deductions / chargebacks recovery":            (5,4,4,1,1,2,2,4,3,2),
 "Marketplace (FBA) reimbursement recovery":              (4,3,3,1,4,4,3,4,2,4),
 "AP errors / vendor contract price compliance":          (3.5,3.5,3,2.5,2,3,2,2,3.5,2),
 "Month-end variance explanation":                        (3,2,3,2,3,4,2,5,4,3),
}
rows=[]
for k,v in S.items():
    tot=sum(w*s for w,s in zip(W.values(),v))/5
    rows.append((tot,k,v))
rows.sort(reverse=True)
for t,k,v in rows: print(f"{t:5.1f} | {k} | {v}")
# sensitivity: WTP weight doubled (40) renormalised
W2=dict(W); W2['wtp']=40
tot2=sum(W2.values())
print("\nSensitivity: WTP weight 40 (renormalised to 100)")
r2=[]
for k,v in S.items():
    t=sum(w*s for w,s in zip(W2.values(),v))/5*100/tot2
    r2.append((t,k))
for t,k in sorted(r2,reverse=True): print(f"{t:5.1f} | {k}")
W3=dict(W); W3['wtp']=0; W3['open']=24
tot3=sum(W3.values())
print("\nSensitivity: ignore WTP, openness 24")
r3=[]
for k,v in S.items():
    t=sum(w*s for w,s in zip(W3.values(),v))/5*100/tot3
    r3.append((t,k))
for t,k in sorted(r3,reverse=True): print(f"{t:5.1f} | {k}")

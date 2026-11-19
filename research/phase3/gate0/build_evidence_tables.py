"""Gate 0, Arm 3 inputs (NOT product code): deterministic evidence tables built ONLY from the exported CSVs
(no access to the answer key or the generator flags). This simulates what an evidence layer would hand an LLM.
Usage: python3 build_evidence_tables.py A   |   python3 build_evidence_tables.py C"""
import sys, os, pandas as pd, numpy as np, datetime as dt
HERE=os.path.dirname(os.path.abspath(__file__)); ds=sys.argv[1] if len(sys.argv)>1 else "A"
D=f"{HERE}/data/{ds}"; O=f"{HERE}/arm3_evidence/{ds}"; os.makedirs(O,exist_ok=True)
L=pd.read_csv(f"{D}/shopify_order_lines.csv",parse_dates=["date"]); S=pd.read_csv(f"{D}/shipping_costs.csv",parse_dates=["date"])
B=pd.read_csv(f"{D}/supplier_bills.csv",parse_dates=["bill_date"]); I=pd.read_csv(f"{D}/wholesale_invoices.csv",parse_dates=["invoice_date","due_date","paid_date"])
P=pd.read_csv(f"{D}/shopify_products.csv"); Q=pd.read_csv(f"{D}/quickbooks_pnl_monthly.csv")
# unit cost effective at order date = latest bill on/before the date
B=B.sort_values("bill_date"); L=L.sort_values("date")
L=pd.merge_asof(L,B[["sku","bill_date","unit_cost"]].sort_values("bill_date"),left_on="date",right_on="bill_date",by="sku",direction="backward")
first_cost=B.sort_values("bill_date").groupby("sku")["unit_cost"].first()
L["unit_cost"]=L["unit_cost"].fillna(L["sku"].map(first_cost))   # orders before the first bill use the first bill cost
L["qe"]=L["qty"]*(1-L["refund_rate"]); L["rev"]=L["qe"]*L["net_unit_price"]; L["cogs"]=L["qe"]*L["unit_cost"]
L["month"]=L["date"].dt.to_period("M").astype(str); S["month"]=S["date"].dt.to_period("M").astype(str)
# 1. coverage and history
rev_by_sku=L.groupby("sku")["rev"].sum(); known=P.dropna(subset=["shopify_unit_cost"])["sku"]
pd.DataFrame([{"months_of_history":L["month"].nunique(),"first_month":L["month"].min(),"last_month":L["month"].max(),
  "share_of_revenue_with_shopify_unit_cost":round(rev_by_sku[rev_by_sku.index.isin(known)].sum()/rev_by_sku.sum(),3),
  "skus_without_shopify_unit_cost":", ".join(sorted(set(P["sku"])-set(known))),
  "note":"Cost for the SKUs above was taken from supplier bills; Shopify unit cost is blank for them."}]).to_csv(f"{O}/01_coverage.csv",index=False)
# 2. monthly summary + reconciliation to QuickBooks P&L
g=L.groupby("month").agg(revenue=("rev","sum"),cogs=("cogs","sum")); sh=S.groupby("month").agg(shipping_charged=("shipping_charged","sum"),carrier_cost=("carrier_cost","sum"))
g=g.join(sh); g["gross_profit"]=g.revenue-g.cogs+g.shipping_charged-g.carrier_cost; g["gm_pct"]=g.gross_profit/(g.revenue+g.shipping_charged)
g.round(4).reset_index().to_csv(f"{O}/02_monthly_summary.csv",index=False)
q=Q.set_index("month"); rec=pd.DataFrame({"derived_gross_profit":g["gross_profit"],"quickbooks_gross_profit":q["gross_profit"]}); rec["difference"]=rec.derived_gross_profit-rec.quickbooks_gross_profit
rec.round(2).reset_index().to_csv(f"{O}/03_reconciliation_to_quickbooks.csv",index=False)
# 4. margin bridge Sep -> Oct (price/list unchanged; discount; mix; volume; cost; shipping) with identity check
m0,m1="2026-09","2026-10"
def agg(m):
    x=L[L.month==m].groupby(["sku","channel"]).agg(Q=("qe","sum"),rev=("rev","sum"),cogs=("cogs","sum"),listrev=("list_price",lambda s:0)).reset_index()
    x["lp"]=L[L.month==m].assign(lw=lambda d:d.qe*d.list_price).groupby(["sku","channel"])["lw"].sum().values/x["Q"]
    x["P"]=x.rev/x.Q; x["C"]=x.cogs/x.Q; x["D"]=x.lp-x.P; return x.set_index(["sku","channel"])
a0,a1=agg(m0),agg(m1); keys=sorted(set(a0.index)|set(a1.index)); rows=[]
Q0=a0.Q.sum(); gp0_merch=(a0.rev-a0.cogs).sum(); avgm0=gp0_merch/Q0
for k in keys:
    q0=a0.Q.get(k,0.0); q1=a1.Q.get(k,0.0)
    p0=a0.P.get(k,np.nan); c0=a0.C.get(k,np.nan); l0=a0.lp.get(k,np.nan)
    p1=a1.P.get(k,np.nan); c1=a1.C.get(k,np.nan); l1=a1.lp.get(k,np.nan)
    if q0==0: p0,c0,l0=p1,c1,l1
    if q1==0: p1,c1,l1=p0,c0,l0
    m0_=p0-c0
    rows.append(dict(sku=k[0],channel=k[1],q0=q0,q1=q1,d_qty_x_m0=(q1-q0)*m0_,list_price_effect=q1*(l1-l0),discount_effect=-q1*((l1-p1)-(l0-p0)),cost_effect=-q1*(c1-c0)))
Bd=pd.DataFrame(rows)
tot_dq_m0=Bd.d_qty_x_m0.sum(); vol=(a1.Q.sum()-Q0)*avgm0; mix=tot_dq_m0-vol
N0=(S.month==m0).sum(); N1=(S.month==m1).sum(); s0=(S[S.month==m0].shipping_charged-S[S.month==m0].carrier_cost).sum()/N0; s1=(S[S.month==m1].shipping_charged-S[S.month==m1].carrier_cost).sum()/N1
ship_orders=(N1-N0)*s0; ship_perorder=N1*(s1-s0)
dgp=g.loc[m1,"gross_profit"]-g.loc[m0,"gross_profit"]
parts={"volume (orders/units at prior-month margin)":vol,"mix (shift between SKUs/channels)":mix,"list price":Bd.list_price_effect.sum(),
       "discounts (average discount per unit)":Bd.discount_effect.sum(),"supplier unit cost":Bd.cost_effect.sum(),
       "shipping: order count":ship_orders,"shipping: net cost per order":ship_perorder}
res=sum(parts.values())-dgp
out=pd.DataFrame([{"driver":k,"gross_profit_effect_usd":round(v,2)} for k,v in parts.items()]+
                 [{"driver":"TOTAL of drivers","gross_profit_effect_usd":round(sum(parts.values()),2)},
                  {"driver":"ACTUAL change in gross profit (Oct minus Sep)","gross_profit_effect_usd":round(dgp,2)},
                  {"driver":"UNEXPLAINED RESIDUAL (must be ~0 for an identity bridge)","gross_profit_effect_usd":round(-res,2)}])
out.to_csv(f"{O}/04_margin_bridge_Sep_to_Oct.csv",index=False)
Bd["abs_total"]=Bd[["d_qty_x_m0","discount_effect","cost_effect"]].abs().sum(axis=1)
Bd.sort_values("abs_total",ascending=False).drop(columns="abs_total").round(2).to_csv(f"{O}/05_bridge_by_sku_channel.csv",index=False)
# 6. supplier unit cost by SKU: last bill before 2026-09-01 vs last bill in Oct
def last_cost(d_from,d_to):
    x=B[(B.bill_date>=d_from)&(B.bill_date<=d_to)].sort_values("bill_date").groupby("sku").tail(1).set_index("sku")["unit_cost"]; return x
c_aug=last_cost("2026-08-01","2026-08-31"); c_oct=last_cost("2026-10-01","2026-10-31")
cc=pd.DataFrame({"unit_cost_aug":c_aug,"unit_cost_oct":c_oct}); cc["change_pct"]=(cc.unit_cost_oct/cc.unit_cost_aug-1)*100
cc.round(3).reset_index().to_csv(f"{O}/06_supplier_unit_cost_aug_vs_oct.csv",index=False)
# 7. discount rate and freight
dd=L.assign(w=L.qe*L.discount_rate).groupby(["month","channel"]).agg(w=("w","sum"),q=("qe","sum")); dd["avg_discount_rate"]=dd.w/dd.q
dd[["avg_discount_rate"]].round(4).reset_index().to_csv(f"{O}/07_avg_discount_rate_by_month_channel.csv",index=False)
s12=L[L.sku=="S12"].groupby(["month"]).agg(units=("qe","sum"),avg_net_price=("net_unit_price","mean")); s12["share_of_all_units"]=s12.units/L.groupby("month")["qe"].sum()
s12.round(4).reset_index().to_csv(f"{O}/08_bundle_S12_units_and_share.csv",index=False)
fr=S.assign(ch=S.order_id.str[0]).groupby(["month","ch"]).agg(orders=("order_id","count"),avg_carrier_cost=("carrier_cost","mean")); fr.round(3).reset_index().to_csv(f"{O}/09_carrier_cost_per_order.csv",index=False)
# 10. AR aging as of 2026-10-31 and days-to-pay by customer by quarter
asof=pd.Timestamp("2026-10-31"); openI=I[I.paid_date>asof].copy(); openI["days_past_due"]=(asof-openI.due_date).dt.days
bins=[-9999,0,30,60,9999]; labels=["not yet due","1-30 past due","31-60 past due","60+ past due"]
openI["bucket"]=pd.cut(openI.days_past_due,bins=bins,labels=labels)
openI.groupby(["customer_id","bucket"],observed=True)["amount"].sum().round(0).reset_index().to_csv(f"{O}/10_ar_aging_by_customer.csv",index=False)
P2=I[I.paid_date<=asof].copy(); P2["days_to_pay"]=(P2.paid_date-P2.invoice_date).dt.days; P2["q"]=P2.invoice_date.dt.to_period("Q").astype(str)
dtp=P2.groupby(["customer_id","q"])["days_to_pay"].agg(["count","mean"]).round(1).reset_index()
dtp.to_csv(f"{O}/11_days_to_pay_by_customer_quarter.csv",index=False)
print("bridge:\n",out.to_string(index=False)); print("\nAR buckets:\n",openI.groupby("bucket",observed=True)["amount"].sum().round(0))
print("\nunit cost change top:\n",cc.sort_values("change_pct",ascending=False).head(3).round(2))
print("\nrec max abs diff:",rec.difference.abs().max().round(4))

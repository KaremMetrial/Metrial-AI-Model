"""Gate 0 test-fixture generator (NOT product code). Builds SYNTHETIC data for a fictional specialty-food brand
('Northwind Pantry') with planted causes, plus a control dataset with no planted cause.
Deterministic: all random draws are made BEFORE any flag is applied, so flag-off counterfactuals share the same draws.
Usage: python3 make_seed_data.py   (writes ./data/A, ./data/C and ./answer_key/*.json)"""
import numpy as np, pandas as pd, json, os, datetime as dt
HERE=os.path.dirname(os.path.abspath(__file__))
MONTHS=pd.period_range("2024-11","2026-10",freq="M")
SKUS=[f"S{i:02d}" for i in range(1,13)]
BASE_COST={s:c for s,c in zip(SKUS,[4.1,5.2,6.0,3.4,7.8,4.9,8.4,2.9,5.5,6.6,3.8,9.5])}  # S12 = bundle
LIST_PRICE={s:round(BASE_COST[s]/0.46,2) for s in SKUS}
LIST_PRICE["S12"]=round(BASE_COST["S12"]/0.52,2)   # bundle carries a thinner margin by design
WHOLESALE_FACTOR=0.62
CUSTOMERS=[f"W{i:02d}" for i in range(1,31)]
CUST_POOL=CUSTOMERS+["W12"]*5+["W27"]*5   # W12/W27 are heavier buyers
SLOW=["W12","W27"]
FLAGS_ALL=dict(cost_up=True,promo=True,freight=True,slow_pay=True)
FLAGS_OFF=dict(cost_up=False,promo=False,freight=False,slow_pay=False)

def draws(seed):
    r=np.random.default_rng(seed); D={}
    D["orders"]=[]
    for m in MONTHS:
        season=1.35 if m.month in (11,12) else (0.9 if m.month in (1,2) else 1.0)
        growth=1+0.012*(m-MONTHS[0]).n
        n_dtc=int(round(420*season*growth*r.uniform(0.95,1.05)))
        n_ws=int(r.integers(15,22))
        D["orders"].append((m,n_dtc,n_ws))
    D["u"]=r.random((200000,12))      # pre-drawn uniform pool, consumed in order
    D["pos"]=0
    D["rng"]=r
    return D

def nxt(D,k=1):
    a=D["u"][D["pos"]]; D["pos"]+=1     # one row of 12 independent uniforms per call
    return a

def build(seed,flags):
    D=draws(seed); r=D["rng"]
    lines=[];orders=[];ship=[];bills=[];inv=[]
    oid=1;iid=1
    # cost per SKU over time (bills use cost effective on bill date)
    def unit_cost(s,date):
        c=BASE_COST[s]*(1+0.002*max(0,(date.year-2024)*12+date.month-11))   # slow drift ~0.2%/month
        if flags["cost_up"] and s in("S03","S07") and date>=dt.date(2026,9,15): c*=1.12
        return round(c,3)
    for (m,n_dtc,n_ws) in D["orders"]:
        days=m.days_in_month
        # DTC orders
        for _ in range(n_dtc):
            u=nxt(D)
            day=int(u[0]*days)+1; date=dt.date(m.year,m.month,day)
            nlines=1+int(u[1]*2.99)
            skus=[SKUS[int(u[2+j]*11.99)] for j in range(nlines)]     # S12 chosen at the base 1/12 rate
            disc_rate=0.08 if u[5]<0.25 else 0.0
            promo_extra = (flags["promo"] and m==pd.Period("2026-10") and u[6]<0.50)
            if promo_extra: skus.append("S12")
            for s in skus:
                q=1+int(u[7]*2.99)
                d=disc_rate
                if s=="S12" and flags["promo"] and m==pd.Period("2026-10"): d=0.25
                price=LIST_PRICE[s]
                lines.append(dict(order_id=f"D{oid:06d}",date=date,channel="DTC",customer_id=f"C{oid%900:04d}",sku=s,qty=q,list_price=price,discount_rate=d,
                                  net_unit_price=round(price*(1-d),3),refund_rate=1.0 if u[8]<0.03 else 0.0))
            items=sum(l["qty"] for l in lines[-len(skus):])
            carrier=7.2+0.9*items
            if flags["freight"] and date>=dt.date(2026,10,1): carrier*=1.09
            carrier*= (0.98+0.04*u[9])
            ship.append(dict(order_id=f"D{oid:06d}",date=date,shipping_charged=6.0,carrier_cost=round(carrier,2)))
            orders.append(dict(order_id=f"D{oid:06d}",date=date,channel="DTC"))
            oid+=1
        # wholesale orders + invoices
        for _ in range(n_ws):
            u=nxt(D)
            day=int(u[0]*days)+1; date=dt.date(m.year,m.month,day)
            cust=CUST_POOL[int(u[1]*(len(CUST_POOL)-0.01))]
            nlines=3+int(u[2]*4.99)
            total=0
            for j in range(nlines):
                s=SKUS[int(nxt(D)[0]*11.99)]
                q=12+int(nxt(D)[1]*36)
                price=round(LIST_PRICE[s]*WHOLESALE_FACTOR,3)
                lines.append(dict(order_id=f"W{oid:06d}",date=date,channel="Wholesale",customer_id=cust,sku=s,qty=q,list_price=LIST_PRICE[s],discount_rate=round(1-WHOLESALE_FACTOR,3),
                                  net_unit_price=price,refund_rate=0.0))
                total+=price*q
            items=sum(l["qty"] for l in lines[-nlines:])
            ship.append(dict(order_id=f"W{oid:06d}",date=date,shipping_charged=0.0,carrier_cost=round(38+0.35*items,2)))
            orders.append(dict(order_id=f"W{oid:06d}",date=date,channel="Wholesale"))
            lag_mu,lag_sd=31,5
            if flags["slow_pay"] and cust in SLOW and date>=dt.date(2026,7,15): lag_mu,lag_sd=62,6
            z=(u[7]+u[8]+u[9]+u[10]-2.0)/0.577          # approx N(0,1)
            lag=max(10,int(round(lag_mu+lag_sd*z)))
            inv.append(dict(invoice_id=f"INV{iid:05d}",customer_id=cust,invoice_date=date,due_date=date+dt.timedelta(days=30),amount=round(total,2),
                            paid_date=date+dt.timedelta(days=lag)))
            iid+=1
            oid+=1
        # supplier bills: one bill per SKU per month, qty ~ monthly usage
    L=pd.DataFrame(lines)
    L["month"]=pd.to_datetime(L["date"]).dt.to_period("M")
    use=L.groupby(["month","sku"])["qty"].sum().reset_index()
    for _,row in use.iterrows():
        d=dt.date(row["month"].year,row["month"].month,min(10,row["month"].days_in_month))
        bills.append(dict(bill_id=f"B{len(bills)+1:05d}",bill_date=d,supplier=f"Supplier-{(int(row['sku'][1:])%4)+1}",sku=row["sku"],qty=int(row["qty"]*1.02),unit_cost=unit_cost(row["sku"],d)))
        # a second mid-month bill carries the Sep-15 cost step
        d2=dt.date(row["month"].year,row["month"].month,min(20,row["month"].days_in_month))
        bills.append(dict(bill_id=f"B{len(bills)+1:05d}",bill_date=d2,supplier=f"Supplier-{(int(row['sku'][1:])%4)+1}",sku=row["sku"],qty=int(row["qty"]*0.01)+1,unit_cost=unit_cost(row["sku"],d2)))
    B=pd.DataFrame(bills)
    return L.drop(columns="month"),pd.DataFrame(ship),B,pd.DataFrame(inv),pd.DataFrame(orders)

def cogs_lookup(B):
    """cost effective at order date = most recent bill unit_cost on/before date (per SKU)"""
    B=B.sort_values("bill_date"); return {s:g[["bill_date","unit_cost"]].values.tolist() for s,g in B.groupby("sku")}
def cost_at(look,s,d):
    c=None
    for bd,uc in look[s]:
        if bd<=d: c=uc
        else: break
    return c if c is not None else look[s][0][1]

def monthly_gm(L,S,B):
    look=cogs_lookup(B)
    L=L.copy(); L["unit_cost"]=[cost_at(look,s,d) for s,d in zip(L["sku"],L["date"])]
    L["rev"]=L["qty"]*L["net_unit_price"]*(1-L["refund_rate"]); L["cogs"]=L["qty"]*L["unit_cost"]*(1-L["refund_rate"])
    L["month"]=pd.to_datetime(L["date"]).dt.to_period("M")
    S=S.copy(); S["month"]=pd.to_datetime(S["date"]).dt.to_period("M")
    g=L.groupby("month").agg(revenue=("rev","sum"),cogs=("cogs","sum"))
    sh=S.groupby("month").agg(shipping_charged=("shipping_charged","sum"),carrier_cost=("carrier_cost","sum"))
    g=g.join(sh); g["gross_profit"]=g.revenue-g.cogs+g.shipping_charged-g.carrier_cost; g["gm_pct"]=g.gross_profit/(g.revenue+g.shipping_charged)
    return g

def dso_summary(inv,asof=dt.date(2026,10,31)):
    I=inv.copy(); I["paid_by_asof"]=I["paid_date"]<=asof
    openI=I[~I["paid_by_asof"]]
    openI=openI.assign(days_past_due=[(asof-d).days for d in openI["due_date"]])
    return openI

if __name__=="__main__":
    out={}
    # --- Dataset A: planted causes ---
    seedA=11
    A=build(seedA,FLAGS_ALL)
    gmA=monthly_gm(A[0],A[1],A[2])
    truth={"dataset":"A","seed":seedA,"period_of_interest":"2026-10 vs 2026-09",
           "planted":{"cost_up":"supplier cost +12% on S03 and S07 for bills dated on/after 2026-09-15 (prices unchanged)",
                      "promo":"October 2026 bundle promo: S12 discount 25% (was ~8% on 25% of orders) and an extra S12 line on ~50% of DTC orders (mix shift to the thin-margin bundle)",
                      "freight":"carrier cost +9% on DTC orders from 2026-10-01",
                      "slow_pay":"wholesale customers W12 and W27 pay in ~62 days (was ~31) for invoices dated on/after 2026-07-15"}}
    base=gmA.loc[pd.Period("2026-10"),"gross_profit"]; base_pct=gmA.loc[pd.Period("2026-10"),"gm_pct"]
    effects={}
    for f in ("cost_up","promo","freight"):
        fl=dict(FLAGS_ALL); fl[f]=False
        Ax=build(seedA,fl); g=monthly_gm(Ax[0],Ax[1],Ax[2])
        effects[f]={"oct_gross_profit_effect_usd":round(float(base-g.loc[pd.Period("2026-10"),"gross_profit"]),0),
                    "oct_gm_pct_effect_bps":round(float((base_pct-g.loc[pd.Period("2026-10"),"gm_pct"])*1e4),1)}
    fl0=dict(FLAGS_OFF); A0=build(seedA,fl0); g0=monthly_gm(A0[0],A0[1],A0[2])
    truth["effects_vs_no_event_counterfactual_Oct2026"]=effects
    truth["actual_gm_pct"]={"2026-09":round(float(gmA.loc[pd.Period('2026-09'),'gm_pct']),4),"2026-10":round(float(base_pct),4)}
    truth["actual_gm_change_bps_oct_vs_sep"]=round(float((base_pct-gmA.loc[pd.Period('2026-09'),'gm_pct'])*1e4),1)
    truth["counterfactual_all_off_gm_pct_oct"]=round(float(g0.loc[pd.Period('2026-10'),'gm_pct']),4)
    openA=dso_summary(A[3])
    inv=A[3].copy(); inv["lag"]=[(p-d).days for p,d in zip(inv["paid_date"],inv["invoice_date"])]
    inv["q"]=pd.to_datetime(inv["invoice_date"]).dt.to_period("Q")
    slow=inv[inv["customer_id"].isin(SLOW)]; rest=inv[~inv["customer_id"].isin(SLOW)]
    truth["avg_days_to_pay"]={"W12_W27_invoices_before_2026-07-15":round(float(slow[slow["invoice_date"]<dt.date(2026,7,15)]["lag"].mean()),1),
                              "W12_W27_invoices_on_or_after_2026-07-15":round(float(slow[slow["invoice_date"]>=dt.date(2026,7,15)]["lag"].mean()),1),
                              "all_other_customers_on_or_after_2026-07-15":round(float(rest[rest["invoice_date"]>=dt.date(2026,7,15)]["lag"].mean()),1)}
    pd_any=openA[openA["days_past_due"]>=1].groupby("customer_id")["amount"].sum().sort_values(ascending=False)
    truth["ar_open_total_asof_2026-10-31"]=round(float(openA["amount"].sum()),0)
    truth["ar_past_due_any_by_customer_top5"]={k:round(float(v),0) for k,v in pd_any.head(5).items()}
    truth["slow_pay_customers_share_of_past_due"]=round(float(pd_any.reindex(SLOW).fillna(0).sum()/max(1,pd_any.sum())),3)
    # Shopify-style cost coverage gap: unit_cost blank for S10 and S11
    prods=pd.DataFrame({"sku":SKUS,"title":[f"Northwind {s}" for s in SKUS],"shopify_unit_cost":[BASE_COST[s] if s not in("S10","S11") else None for s in SKUS],"list_price":[LIST_PRICE[s] for s in SKUS]})
    revA=(A[0]["qty"]*A[0]["net_unit_price"]).groupby(A[0]["sku"]).sum(); cov=1-revA[["S10","S11"]].sum()/revA.sum()
    truth["cost_coverage_shopify_unitCost_share_of_revenue"]=round(float(cov),3)
    os.makedirs(f"{HERE}/data/A",exist_ok=True); os.makedirs(f"{HERE}/answer_key",exist_ok=True)
    A[0].to_csv(f"{HERE}/data/A/shopify_order_lines.csv",index=False); A[1].to_csv(f"{HERE}/data/A/shipping_costs.csv",index=False)
    A[2].to_csv(f"{HERE}/data/A/supplier_bills.csv",index=False); A[3].to_csv(f"{HERE}/data/A/wholesale_invoices.csv",index=False)
    prods.to_csv(f"{HERE}/data/A/shopify_products.csv",index=False)
    gm_out=gmA.reset_index(); gm_out["month"]=gm_out["month"].astype(str); gm_out.round(4).to_csv(f"{HERE}/data/A/quickbooks_pnl_monthly.csv",index=False)
    json.dump(truth,open(f"{HERE}/answer_key/A_truth.json","w"),indent=2)
    # --- Dataset C: control, no planted cause; pick a seed whose Oct-vs-Sep fall is 35-80 bps ---
    chosen=None
    for sd in range(100,400):
        C=build(sd,FLAGS_OFF); g=monthly_gm(C[0],C[1],C[2])
        d=(g.loc[pd.Period("2026-10"),"gm_pct"]-g.loc[pd.Period("2026-09"),"gm_pct"])*1e4
        if -80<=d<=-35: chosen=(sd,C,g,d); break
    sd,C,g,d=chosen
    hist=(g["gm_pct"].diff().dropna()*1e4)
    truthC={"dataset":"C (control)","seed":sd,"planted":"NONE. All flags off.","period_of_interest":"2026-10 vs 2026-09",
            "actual_gm_change_bps_oct_vs_sep":round(float(d),1),"historical_monthly_change_bps_std":round(float(hist.std()),1),
            "correct_behavior":"Say that no specific cause can be identified from the data; the change is within normal monthly variation; list what was checked and what could not be checked."}
    os.makedirs(f"{HERE}/data/C",exist_ok=True)
    C[0].to_csv(f"{HERE}/data/C/shopify_order_lines.csv",index=False); C[1].to_csv(f"{HERE}/data/C/shipping_costs.csv",index=False)
    C[2].to_csv(f"{HERE}/data/C/supplier_bills.csv",index=False); C[3].to_csv(f"{HERE}/data/C/wholesale_invoices.csv",index=False)
    prods.to_csv(f"{HERE}/data/C/shopify_products.csv",index=False)
    gm_out=g.reset_index(); gm_out["month"]=gm_out["month"].astype(str); gm_out.round(4).to_csv(f"{HERE}/data/C/quickbooks_pnl_monthly.csv",index=False)
    json.dump(truthC,open(f"{HERE}/answer_key/C_truth.json","w"),indent=2)
    print(json.dumps(truth,indent=1)); print(json.dumps(truthC,indent=1))

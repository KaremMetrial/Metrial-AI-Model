"""Phase 3 re-ranking under multiple lenses. Scores start from Phase 2 (p2_scoring_model.py) and are
adjusted for Phase 3 findings; every adjustment is listed in ADJ and is JUDGMENT, not measurement.
Criteria order: wtp, dollar, pain, open, data, ttv, acc, rec, exp, inb"""
import random, statistics
CRIT=["wtp","dollar","pain","open","data","ttv","acc","rec","exp","inb"]
P2={
 "Margin / price-cost investigation (Shopify+ledger)":(2,4,4,3,4,4,3,4,5,3),
 "Cash flow investigation":(3.5,3.5,4,2,5,5,4,5,4,4),
 "Late AR / collections prioritisation":(4,4,4,2,5,5,4,5,4,4),
 "Churn / revenue-risk (billing-first)":(3,4,5,2,3,4,4,4,5,4),
 "Payout / bank / ledger reconciliation":(4,3,4,2,3,3,1,5,3,4),
 "Inventory / stock anomalies":(2,3,3,3,2,3,2,4,5,3),
 "Procurement / supplier price-creep":(2,4,4,4,1,2,2,3,5,2),
 "Revenue leakage / billing errors":(2,4,4,3,2,1,2,3,4,2),
 "Operational bottlenecks (fulfilment)":(2,2,3,3,2,2,3,4,4,2),
 "Distributor price-cost leakage (ERP, interview-led)":(2.5,4.5,4,3.5,2,2,3,4,5,1.5),
}
# Phase 3 adjustments (criterion -> new value), with reason
ADJ={
 "Cash flow investigation":{"open":1,"wtp":3},      # Claude SMB cash forecast+invoice chaser, Intuit/Xero forecasting bundled
 "Late AR / collections prioritisation":{"open":1}, # Claude invoice-chase, Intuit payments agent, Chaser/Upflow
 "Payout / bank / ledger reconciliation":{"open":1.5}, # Claude close-month reconciles vs Shopify/Stripe/PayPal
 "Margin / price-cost investigation (Shopify+ledger)":{"open":2.5,"data":3.5,"exp":4}, # analyzer named; QBO insights; cost data gap; expansion untested
 "Churn / revenue-risk (billing-first)":{"exp":4},
}
S={k:list(v) for k,v in P2.items()}
for k,ch in ADJ.items():
    for c,v in ch.items(): S[k][CRIT.index(c)]=v
LENS={
 "L0 Phase-2 weights":dict(wtp=20,dollar=12,pain=8,open=12,data=12,ttv=8,acc=6,rec=6,exp=8,inb=8),
 "L1 Best BUSINESS (value+defensibility)":dict(wtp=25,dollar=15,pain=10,open=20,data=3,ttv=2,acc=3,rec=7,exp=10,inb=5),
 "L2 Easiest to BUILD (tiny backend team)":dict(wtp=0,dollar=0,pain=0,open=0,data=40,ttv=25,acc=25,rec=0,exp=0,inb=10),
 "L3 Easiest to VALIDATE in weeks":dict(wtp=10,dollar=5,pain=10,open=0,data=25,ttv=25,acc=10,rec=0,exp=0,inb=15),
 "L4 Most RECURRING revenue":dict(wtp=20,dollar=10,pain=10,open=10,data=5,ttv=5,acc=5,rec=30,exp=0,inb=5),
 "L5 Entry to COMPANY INTELLIGENCE":dict(wtp=5,dollar=10,pain=5,open=10,data=10,ttv=5,acc=5,rec=10,exp=35,inb=5),
 "L6 WTP ignored, openness doubled":dict(wtp=0,dollar=12,pain=8,open=24,data=12,ttv=8,acc=6,rec=6,exp=8,inb=8),
 "L7 WTP x2":dict(wtp=40,dollar=12,pain=8,open=12,data=12,ttv=8,acc=6,rec=6,exp=8,inb=8),
}
def score(s,w):
    t=sum(w.values()); return sum(w[c]*s[i] for i,c in enumerate(CRIT))/5*100/t
def table(Sd,title):
    print("\n=== ",title)
    names=list(Sd)
    for L,w in LENS.items():
        r=sorted(((score(Sd[n],w),n) for n in names),reverse=True)
        print(f"{L}: "+" | ".join(f"{n.split(' (')[0][:26]} {v:.1f}" for v,n in r[:4]))
table(P2,"Phase-2 scores (unadjusted)")
table(S,"Phase-3 adjusted scores")
# stability: random weights (flat Dirichlet) on adjusted and unadjusted
random.seed(7)
def dirichlet(k):
    x=[random.gammavariate(1,1) for _ in range(k)]; s=sum(x); return [v/s*100 for v in x]
def stab(Sd,N=5000):
    names=list(Sd); top1={n:0 for n in names}; top3={n:0 for n in names}
    for _ in range(N):
        w=dict(zip(CRIT,dirichlet(10)))
        r=sorted(names,key=lambda n:-score(Sd[n],w))
        top1[r[0]]+=1
        for n in r[:3]: top3[n]+=1
    return top1,top3
for nm,Sd in (("unadjusted",P2),("adjusted",S)):
    t1,t3=stab(Sd)
    print(f"\n=== flat-Dirichlet stability, {nm}, 5000 draws (P top-1 / P top-3)")
    for n in sorted(t1,key=lambda n:-t3[n]): print(f"{n[:55]:55s} {t1[n]/5000:.2f} / {t3[n]/5000:.2f}")
# gap check: is cash/AR lead from ease? Remove data+ttv+acc (ease criteria) and rescore
W_NOEASE=dict(wtp=20,dollar=12,pain=8,open=12,data=0,ttv=0,acc=0,rec=6,exp=8,inb=8)
print("\n=== Ease criteria (data,ttv,acc) removed, Phase-3 adjusted")
for v,n in sorted(((score(S[n],W_NOEASE),n) for n in S),reverse=True)[:6]: print(f"{v:5.1f} {n}")

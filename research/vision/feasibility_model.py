"""Feasibility model (36 months). ALL INPUTS ARE ASSUMPTIONS unless noted in the study. Analysis script, not product code.
Stage-gated path: months 1-2 Gates (Gate 0 + Gate A), 3-5 Stage-1 pilot, 6-8 thin MVP build (only if gates pass), selling from month 9."""
import json
SC={
 "متشائم": dict(price=199,setup=750, new_per_month=1.0, churn=0.040, var_cost=318, onboard_cost=1540, cac=3000),
 "أساسي":  dict(price=399,setup=1500,new_per_month=3.0, churn=0.025, var_cost=202, onboard_cost=880,  cac=1800),
 "متفائل": dict(price=799,setup=2500,new_per_month=6.0, churn=0.015, var_cost=126, onboard_cost=440,  cac=900),
}
COSTCASE={"مؤسسان بسحب أدنى 1,500$ لكل واحد":3000,"فريق بتكلفة كاملة 6,000$ لكل واحد":12000}
def run(sc,team_cost,months=36,start_sell=9,ramp=6):
    cust=0.0; cash=0.0; min_cash=0.0; mrr_hist=[]; be=None; cum_rev=0
    for m in range(1,months+1):
        # fixed costs
        fixed=500 if m<start_sell else 1000
        team=team_cost
        if m<start_sell:   # pre-launch: gates, pilot, build (no revenue); build months 6-8 cost tools only (founders' time already in team cost)
            rev=0;var=0;acq=0;onb=0;setup_rev=0
            new=0
        else:
            r=min(1.0,(m-start_sell+1)/ramp); new=sc["new_per_month"]*r
            churned=cust*sc["churn"]; cust=cust+new-churned
            rev=cust*sc["price"]; var=cust*sc["var_cost"]; acq=new*sc["cac"]; onb=new*sc["onboard_cost"]; setup_rev=new*sc["setup"]
        legal=3000/12 if m<=12 else 0
        soc2=25000/12 if (18<=m<=29 and sc["price"]>=399) else 0     # SOC 2 only when procurement asks (assumption: month 18+)
        # hire first employee when MRR >= 15000
        hire=6000 if (cust*sc["price"]>=15000) else 0
        op=rev+setup_rev-var-acq-onb-fixed-team-legal-soc2-hire
        cash+=op; min_cash=min(min_cash,cash); cum_rev+=rev+setup_rev
        mrr_hist.append(rev)
        if be is None and m>=start_sell and op>=0: be=m
    return dict(customers_36=round(cust,1),mrr_36=round(mrr_hist[-1]),arr_36=round(mrr_hist[-1]*12),cash_36=round(cash),peak_funding_need=round(-min_cash),first_cash_positive_month=be)
out={}
for cn,tc in COSTCASE.items():
    out[cn]={sn:run(sc,tc) for sn,sc in SC.items()}
print(json.dumps(out,ensure_ascii=False,indent=1))
# Stage-gated expected value (all probabilities are assumptions, anchored to prior 5-8% viable product)
H=75
cost_gate0=25*H+50; cost_gateA=15*H; cost_stage1=95*H+300
p_stop_g0,p_stop_gA,p_fail_s1,p_mvp=0.35,0.25,0.32,0.08
split={"متشائم":0.50,"أساسي":0.40,"متفائل":0.10}
def expected(tc):
    cost_gates=cost_gate0+ (1-p_stop_g0)*cost_gateA + (1-p_stop_g0)*(1-p_stop_gA)*cost_stage1
    ev_mvp=sum(split[s]*out[tc][s]["cash_36"] for s in split)
    # founders' living cost during the 36 months is already inside cash_36 via team cost; only compare relative magnitudes
    return cost_gates, ev_mvp
for tc in COSTCASE:
    g,e=expected(tc)
    print(f"\n{tc}: expected cost of the gates before any build = ${g:,.0f}; expected 36-month cash result if MVP is reached (weighted by scenario split) = ${e:,.0f}")
print("\nStop probabilities: Gate0",p_stop_g0,"GateA",p_stop_gA,"Stage1 fail",p_fail_s1,"reach MVP",p_mvp)

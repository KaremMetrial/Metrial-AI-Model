H=55  # loaded $/hr analyst time [ASSUMPTION]
TEAM=13500  # 2 people x $6k loaded + $1.5k tools /mo [ASSUMPTION]
def run(name, sc):
    print("\n##",name)
    for label,d in sc.items():
        llm=d['inv']*d['cpi']
        var=llm+d['infra']+d['conn']+d['cs_h']*H
        contrib=d['price']-var
        onboard=d['onb_h']*H
        net_setup=d['setup']-onboard
        cac=d['cac']
        payback = (cac+max(0,-net_setup))/contrib if contrib>0 else float('inf')
        be = TEAM/contrib if contrib>0 else float('inf')
        gm=contrib/d['price']*100
        print(f"{label:12s} price ${d['price']:>5} setup ${d['setup']:>5} | LLM ${llm:5.1f} infra ${d['infra']} conn ${d['conn']} CS ${d['cs_h']*H:5.0f} => var ${var:6.1f} | contrib ${contrib:6.1f} GM {gm:5.1f}% | onboard cost ${onboard:5.0f} net setup {net_setup:+6.0f} | CAC ${cac} payback {payback:5.1f} mo | customers to cover ${TEAM}: {be:5.0f}")
margin={
 'Conservative':dict(price=199,setup=750,inv=40,cpi=0.45,infra=60,conn=20,cs_h=4,onb_h=28,cac=3000),
 'Base':dict(price=399,setup=1500,inv=30,cpi=0.30,infra=40,conn=15,cs_h=2.5,onb_h=16,cac=1800),
 'Optimistic':dict(price=799,setup=2500,inv=20,cpi=0.15,infra=30,conn=10,cs_h=1.5,onb_h=8,cac=900),
}
cash={
 'Conservative':dict(price=99,setup=0,inv=20,cpi=0.45,infra=25,conn=15,cs_h=1.0,onb_h=3,cac=1500),
 'Base':dict(price=199,setup=0,inv=20,cpi=0.30,infra=15,conn=10,cs_h=0.5,onb_h=1.5,cac=800),
 'Optimistic':dict(price=349,setup=0,inv=15,cpi=0.15,infra=10,conn=5,cs_h=0.25,onb_h=0.5,cac=400),
}
run("Margin investigation (service-assisted)",margin)
run("Cash/AR investigation (near self-serve)",cash)

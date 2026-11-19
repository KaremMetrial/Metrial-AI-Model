"""Phase-3 A5: statistics and expected value of the Phase-2 30-day paid audit.
Every EV input is an ASSUMPTION unless stated. Analysis only."""
import math
import numpy as np
from math import comb, log
from fractions import Fraction

def pmf(k, n, p): return comb(n, k) * p**k * (1-p)**(n-k)
def cdf(k, n, p): return sum(pmf(i, n, p) for i in range(0, k+1))
def sf(k, n, p):  return 1 - cdf(k-1, n, p)   # P(X>=k)

print("=== 1. Binomial, n=15; pass >=4, inconclusive 2-3, fail 0-1 ===")
print(f"{'true p':>7} {'P(>=4)pass':>11} {'P(2-3)':>8} {'P(0-1)fail':>11} {'P(>=5)':>8}")
for p in (0.05, .10, .20, .30, .40):
    print(f"{p:7.2f} {sf(4,15,p):11.3f} {cdf(3,15,p)-cdf(1,15,p):8.3f} {cdf(1,15,p):11.3f} {sf(5,15,p):8.3f}")
print("Good product (p=.30) fails/inconclusive (<4):", round(cdf(3,15,.3),3), " fails outright (<2):", round(cdf(1,15,.3),3))
print("Bad product (p=.10) passes (>=4):", round(sf(4,15,.10),3), "; p=.20 passes:", round(sf(4,15,.2),3))
# threshold alternatives
print("\nAlternative thresholds at n=15 (power at .30 / false-pass at .10 / at .15):")
for t in (3,4,5,6):
    print(f" >= {t}: power {sf(t,15,.3):.3f}  FP@.10 {sf(t,15,.10):.3f}  FP@.15 {sf(t,15,.15):.3f}")
print("\nn needed for 80% power/10% FP, H1=.30 vs H0=.10 (fixed-n):")
for n in range(10, 60):
    for t in range(1, n+1):
        if sf(t, n, .10) <= .10 and sf(t, n, .30) >= .80:
            print(f" n={n}, threshold >= {t}: power {sf(t,n,.3):.3f}, FP {sf(t,n,.1):.3f}"); break
    else: continue
    break

print("\n=== 2. Conjunctive pass rule (5 conditions) ===")
# ASSUMPTION: conditional prob. each non-payment condition is met, given enough payers. Good vs Bad world.
cond = {"good": dict(monthly2=.75, onboard=.60, accuracy=.60, blind=.65, dollar=.80),
        "bad":  dict(monthly2=.30, onboard=.40, accuracy=.45, blind=.40, dollar=.40)}
for world, p in (("good", .30), ("bad", .10)):
    c = np.prod(list(cond[world].values()))
    print(f" {world}: P(>=4 pay)={sf(4,15,p):.3f} x P(other 4 conditions | ...)={c:.3f} => P(full pass)={sf(4,15,p)*c:.3f}")
# 70% accuracy on tiny n
print("\nAccuracy >=70% observed with n owner-confirmed cases:")
for n in (5, 6, 8, 10, 15):
    k = math.ceil(0.7*n - 1e-9)
    print(f" n={n}: need >= {k}; P(pass | true acc 50%) {sf(k,n,.5):.2f}; 70% {sf(k,n,.7):.2f}; 85% {sf(k,n,.85):.2f}")
print("Blind preference 'clear majority' with 4 payers (need >=3/4): true 50% ->", round(sf(3,4,.5),2), "; true 70% ->", round(sf(3,4,.7),2))

print("\n=== 3. Feasibility of 15 qualified prospects (ASSUMPTION funnel) ===")
for label, reach, reply, qual in (("pessimistic", 300, .03, .35), ("base", 400, .06, .45), ("optimistic", 400, .10, .6)):
    print(f" {label}: {reach} outreach x {reply:.0%} reply x {qual:.0%} qualified = {reach*reply*qual:.1f} qualified (before inbound)")
print(" Hours: desk wk1 ~30h + outreach/booking ~25h + 15 calls ~20h + 4 audits x 8-28h (=32-112h) + blind/follow-up/memo ~20h => ",
      30+25+20+32+20, "to", 30+25+20+112+20, "h vs plan 120-150h")

print("\n=== 4. Sequential / Bayesian alternatives ===")
# SPRT H0 p=.10 vs H1 p=.30, alpha=.10, beta=.10 (Wald)
p0, p1, a, b = .10, .30, .10, .10
A = log((1-b)/a); B = log(b/(1-a))
s = log(p1/p0); f = log((1-p1)/(1-p0))
print(f" SPRT: accept H1 when log-LR >= {A:.2f}; accept H0 when <= {B:.2f}")
print(" Per-prospect LR step: payer +%.2f, non-payer %.2f" % (s, f))
def sprt(true_p, rng, nmax=40):
    llr = 0
    for i in range(1, nmax+1):
        llr += s if rng.random() < true_p else f
        if llr >= A: return "H1", i
        if llr <= B: return "H0", i
    return "undecided", nmax
rng = np.random.default_rng(1)
for tp in (.05, .10, .20, .30, .40):
    res = [sprt(tp, rng) for _ in range(20000)]
    pH1 = np.mean([r[0]=="H1" for r in res]); und = np.mean([r[0]=="undecided" for r in res]); en = np.mean([r[1] for r in res])
    print(f"  true {tp:.2f}: P(accept H1)={pH1:.2f} P(undecided by 40)={und:.2f} E[n]={en:.1f}")
# Bayesian: Beta(1,1)... posterior P(p>=.20) after k of n
from math import lgamma, exp
def beta_sf(x, a, b, N=20000):
    xs = np.linspace(x, 1, N); 
    from math import lgamma
    logB = lgamma(a)+lgamma(b)-lgamma(a+b)
    d = np.exp((a-1)*np.log(xs+1e-12) + (b-1)*np.log(1-xs+1e-12) - logB)
    tot = np.trapezoid(np.exp((a-1)*np.log(np.linspace(1e-9,1-1e-9,N)) + (b-1)*np.log(1-np.linspace(1e-9,1-1e-9,N)) - logB), np.linspace(1e-9,1-1e-9,N))
    return np.trapezoid(d, xs)/tot
print(" Posterior P(p>=0.20) under Beta(1,1) prior after k payers in n:")
for n, k in ((15,0),(15,1),(15,2),(15,3),(15,4),(15,6),(8,0),(8,3),(25,3),(25,8)):
    print(f"  {k}/{n}: {beta_sf(.20, 1+k, 1+n-k):.2f}   P(p>=.10)= {beta_sf(.10,1+k,1+n-k):.2f}")
print(" Early stop: P(0 of 8 | p=.30) =", round(pmf(0,8,.3),3), "; | p=.10 =", round(pmf(0,8,.1),3), "; P(0 of 10|.30)=", round(pmf(0,10,.3),3))

print("\n=== 5. Expected value of the experiment (ALL INPUTS ASSUMPTIONS) ===")
H_RATE = 75          # ASSUMPTION $/founder hour opportunity cost (founder could freelance backend at ~$100-150/h; discounted)
HOURS = {"plan": 135, "realistic": 200}
CASH = 500           # ASSUMPTION (Phase 2)
REV = 4 * 750 * 0.0  # revenue from audits ignored (conservative); see below
BUILD = 60000        # ASSUMPTION 4.5 months x $13.5k/mo team (Phase-2 06 team cost)
V_GOOD = 250000      # ASSUMPTION NPV of 'good' world after build (small SaaS, ~$150-250k ARR yr3, heavy discount, includes exit)
Q = 1.0              # absorb viability inside P_GOOD
DELAY = 0.10         # ASSUMPTION fraction of V_GOOD lost to 30-day delay/ platform window
SENS = {"design-as-written (conjunctive)": (0.35, 0.02), "payers-only >=4/15": (sf(4,15,.3), sf(4,15,.1))}
def ev(p_good, hours, sens, spec, price_rev=0):
    T = hours*H_RATE + CASH - price_rev
    build_now = p_good*V_GOOD - BUILD
    pass_g, pass_b = sens, spec
    p_pass = p_good*pass_g + (1-p_good)*pass_b
    post = p_good*pass_g/p_pass if p_pass else 0
    test_then_build = -T + p_pass*(post*V_GOOD*(1-DELAY) - BUILD)
    return T, build_now, test_then_build, p_pass, post
print(f" Inputs: ${H_RATE}/h founder time; build ${BUILD:,}; V_good ${V_GOOD:,}; delay haircut {DELAY:.0%}; cash ${CASH}")
for lab, (g, bad) in SENS.items():
    # 'good world' = true conversion 30% & business viable; 'bad world' = true 10%.  Sens/spec for the pass rule:
    pg = g if lab.startswith("design") else sf(4,15,.3)
    pb = bad if lab.startswith("design") else sf(4,15,.1)
    print(f"\n Rule: {lab}: P(pass|good)={pg:.2f}, P(pass|bad)={pb:.3f}")
    for hrs_lab, hrs in HOURS.items():
        print(f"  founder hours {hrs} ({hrs_lab})")
        for prior in (0.05, 0.10, 0.20, 0.30, 0.50):
            T, bn, tb, pp, post = ev(prior, hrs, pg, pb)
            best = max((0,'stop'), (bn,'build now'), (tb,'test->build'))
            print(f"   P(good)={prior:.2f}: test cost ${T:,.0f} | stop 0 | build-now {bn:+,.0f} | test->build {tb:+,.0f} (P(pass)={pp:.2f}, posterior {post:.2f}) => best: {best[1]}")
# break-even prior: lowest prior at which test->build > stop
for lab, (g, bad) in SENS.items():
    pg = g if lab.startswith("design") else sf(4,15,.3); pb = bad if lab.startswith("design") else sf(4,15,.1)
    for hrs in (135, 200):
        lo = next((x/1000 for x in range(1,1000) if ev(x/1000,hrs,pg,pb)[2] > 0), None)
        hi = next((x/1000 for x in range(1,1000) if ev(x/1000,hrs,pg,pb)[1] > ev(x/1000,hrs,pg,pb)[2]), None)
        print(f" {lab}, {hrs}h: test beats stop for P(good) > {lo}; build-now beats test for P(good) > {hi}")
# Revenue offset: 4 payers x $750
print(" Audit revenue offset in a pass: 4 x $750 = $3,000 (ignored above)")
# Cheaper alternative: 12 conversations (founders sell) + 5 paid, cost half
print("\n Cheaper alt design (~70h, $200), same sens/spec as payers-only:")
for prior in (0.05,0.10,0.20):
    T = 70*H_RATE+200; _,bn,_,pp,post = ev(prior,70,sf(4,15,.3),sf(4,15,.1))
    tb = -T + pp*(post*V_GOOD*(1-DELAY)-BUILD)
    print(f"   P(good)={prior}: test->build {tb:+,.0f}")

"""Expected value of the REDESIGNED (staged) experiment vs stop / build-now / Phase-2 design.
Structure copied from the skeptic's p3_a5_experiment_math.py (section 5). EVERY INPUT IS AN ASSUMPTION.
Gate 0 = 3-5 day bake-off vs Claude SMB / Intuit / Shopify AI. Stage 1 = scan->paid ladder with SPRT."""
H=75; BUILD=60000; V=250000; HAIRCUT=0.9
def ev_test(pg, cost, p_pass_good, p_pass_bad, build=BUILD, v=V):
    p_pass = pg*p_pass_good + (1-pg)*p_pass_bad
    post = pg*p_pass_good/p_pass if p_pass>0 else 0
    return -cost + p_pass*(post*v*HAIRCUT - build)
def staged(pg, hours0, hours1, g_good, g_bad, s_good, s_bad):
    """Gate0 passes w.p. g_*; only then Stage1 (cost hours1). Stop after fail. Approx: expected cost of stage1 weighted by P(gate pass)."""
    cost0 = hours0*H
    pgate = pg*g_good + (1-pg)*g_bad
    post_after_gate = pg*g_good/pgate
    cost1 = hours1*H + 300  # + cash
    # stage1 EV conditional on passing gate
    ev1 = ev_test(post_after_gate, cost1, s_good, s_bad)
    return -cost0 - 300*0 + pgate*ev1 , pgate, post_after_gate
print("P(good) | stop | build-now | Phase2 design 135h conj. | redesign: gate0 25h + stage1 95h (120h total)")
for pg in (0.05,0.10,0.15,0.20,0.30,0.50):
    b=pg*V-BUILD
    p2=ev_test(pg,135*H+500,0.35,0.02)
    # gate0: good passes 0.90, bad passes 0.50 (half of bad worlds caught: Claude/Intuit already explain)
    # stage1 (SPRT ladder): accept-H1 0.80 if good (0.88 minus undecided), 0.07 if bad
    rd,pgate,post=staged(pg,25,95,0.90,0.50,0.80,0.07)
    print(f"{pg:5.2f}   | 0 | {b:9.0f} | {p2:9.0f} | {rd:9.0f}   (P(gate pass)={pgate:.2f}, posterior after gate={post:.2f})")
# break-even priors
def solve(f,lo=0.0,hi=0.6):
    for _ in range(60):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2
be=solve(lambda pg: staged(pg,25,95,0.90,0.50,0.80,0.07)[0])
print(f"\nBreak-even prior for redesigned staged plan (120h total): {be:.3f}")
be2=solve(lambda pg: staged(pg,25,95,0.90,0.30,0.80,0.07)[0])
print(f"  if Gate 0 catches only 30% of bad worlds: {be2:.3f}")
be3=solve(lambda pg: staged(pg,25,130,0.90,0.50,0.80,0.07)[0])
print(f"  if stage 1 takes 130h not 95h (155h total): {be3:.3f}")
be4=solve(lambda pg: ev_test(pg,100*H,0.80,0.07))
print(f"  no gate, ladder only, 100h: {be4:.3f}")
# value sensitivity: halve V
import copy
V2=125000
def staged_v(pg,v):
    cost0=25*H; pgate=pg*0.9+(1-pg)*0.5; post=pg*0.9/pgate
    ev1=ev_test(post,95*H+300,0.8,0.07,v=v)
    return -cost0+pgate*ev1
bev=solve(lambda pg: staged_v(pg,V2))
print(f"  if value of a good world is $125k (not $250k): {bev:.3f}")

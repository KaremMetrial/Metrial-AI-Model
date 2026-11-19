"""Phase-3 A5: rank stability of Phase-2 opportunity scores under random weights.
Scores copied from research/phase2/appendix/p2_scoring_model.py. Analysis only."""
import numpy as np
W0 = dict(wtp=20, dollar=12, pain=8, open=12, data=12, ttv=8, acc=6, rec=6, exp=8, inb=8)
KEYS = list(W0)
S = {
 "Margin": (2,4,4,3,4,4,3,4,5,3),
 "Cash/AR": (3.5,3.5,4,2,5,5,4,5,4,4),
 "Reconciliation": (4,3,4,2,3,3,1,5,3,4),
 "Churn": (3,4,5,2,3,4,4,4,5,4),
 "Rev leakage": (2,4,4,3,2,1,2,3,4,2),
 "Inventory": (2,3,3,3,2,3,2,4,5,3),
 "Procurement": (2,4,4,4,1,2,2,3,5,2),
 "Freight audit": (5,3,3,1,2,2,2,4,3,3),
 "Returns": (2,3,4,3,3,3,3,3,4,3),
 "B2B price leakage": (2,4,4,3,2,2,3,3,5,1),
 "Ad-spend": (3,3,3,1,4,4,2,5,3,4),
 "Deductions": (5,4,4,1,1,2,2,4,3,2),
 "FBA reimb": (4,3,3,1,4,4,3,4,2,4),
 "AP compliance": (3.5,3.5,3,2.5,2,3,2,2,3.5,2),
 "Month-end variance": (3,2,3,2,3,4,2,5,4,3),
}
names = list(S); M = np.array([S[n] for n in names], float)
w0 = np.array([W0[k] for k in KEYS], float); w0 /= w0.sum()
rng = np.random.default_rng(42)

def stats(W, label):
    tot = W @ M.T                      # N x 15 (score on 1-5 scale)
    rk = (-tot).argsort(1).argsort(1) + 1
    print(f"\n== {label} (N={len(W)}) ==")
    print(f"{'opportunity':20s} P(top1) P(top3) P(top5) medRank  [5%-95%]")
    out = []
    for i, n in enumerate(names):
        r = rk[:, i]
        out.append((-(r == 1).mean(), n, (r == 1).mean(), (r <= 3).mean(), (r <= 5).mean(), np.median(r), np.percentile(r, 5), np.percentile(r, 95)))
    for _, n, a, b, c, m, lo, hi in sorted(out)[:8]:
        print(f"{n:20s} {a:6.2f} {b:7.2f} {c:7.2f} {m:7.1f}  [{lo:.0f}-{hi:.0f}]")
    # head-to-head
    mi, ci = names.index("Margin"), names.index("Cash/AR")
    print(f"P(Cash/AR > Margin) = {(tot[:,ci]>tot[:,mi]).mean():.2f}")

# 1. flat Dirichlet (maximal ignorance on weights)
stats(rng.dirichlet(np.ones(10), 5000), "Flat Dirichlet(1)")
# 2. Dirichlet centred on Phase-2 weights, concentration 30 (moderate) and 10 (loose)
for c in (30, 10):
    stats(rng.dirichlet(w0 * c, 5000), f"Dirichlet centred on P2 weights, conc={c}")
# 3. +-50% multiplicative perturbation
P = w0 * rng.uniform(0.5, 1.5, (5000, 10)); P /= P.sum(1, keepdims=True)
stats(P, "P2 weights x U(0.5,1.5)")

# 4. Alternative defensible scorings (Phase-3 adjustments after Claude for Small Business)
def rescored(changes, label, W=w0):
    S2 = {k: list(v) for k, v in S.items()}
    for (n, crit), val in changes.items(): S2[n][KEYS.index(crit)] = val
    M2 = np.array([S2[n] for n in names], float)
    tot = (M2 @ W) / 1 * 20  # to /100
    order = sorted(zip(tot, names), reverse=True)
    print(f"\n-- {label}: " + "; ".join(f"{n} {t:.1f}" for t, n in order[:6]))
rescored({}, "Phase-2 as published")
rescored({("Cash/AR","open"):1, ("Margin","open"):2, ("Reconciliation","open"):1}, "Claude-for-SB adj: open Cash/AR 2->1, Margin 3->2, Recon 2->1")
rescored({("Cash/AR","open"):1, ("Margin","open"):2, ("Reconciliation","open"):1, ("Cash/AR","wtp"):3}, "...plus Cash/AR WTP 3.5->3")
rescored({("Margin","wtp"):1}, "Margin WTP 2->1 (no evidence at all at $349+)")
rescored({("Margin","exp"):3,("Churn","exp"):3}, "Expansion 5->3 for Margin/Churn (not demonstrated)")
rescored({("Margin","data"):3}, "Margin data 4->3 (cost data missing; A5 'AMBER-GREEN' is revenue side only)")
# 5. Weight sets that are defensibly different
alt = {"WTP-heavy (40)": dict(wtp=40), "No inbound/exp (founder prefs removed)": dict(inb=0, exp=0), "Data+TTV heavy (tiny team)": dict(data=25, ttv=15)}
for lab, ch in alt.items():
    W = dict(W0); W.update(ch); w = np.array([W[k] for k in KEYS], float); w /= w.sum()
    tot = (M @ w) * 20
    print(f"\n-- {lab}: " + "; ".join(f"{n} {t:.1f}" for t, n in sorted(zip(tot, names), reverse=True)[:6]))
# sum check of published totals
print("\nPublished-total check (Margin):", round(M[0] @ (np.array([W0[k] for k in KEYS])) / 5, 1))

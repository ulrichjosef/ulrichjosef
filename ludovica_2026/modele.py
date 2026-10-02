"""Prix Ludovica 2026 (R1C4 Vincennes, 02/10/2026) - score composite + Plackett-Luce."""
import numpy as np

# Notes 0-10 par dimension (expertes, à partir des données fournies)
# F=forme, GP=aptitude Grande Piste/2700, V=vitesse, R=régularité allures,
# Fer=déferrage, T=adéquation tactique au scénario (train soutenu), E=entourage
H = {
 1: ("JADE DE NAVARY",     64, dict(F=2, GP=4, V=6, R=4, Fer=5, T=7, E=6)),
 2: ("JUNIOR STEED",       34, dict(F=5, GP=2, V=5, R=7, Fer=8, T=5, E=5)),
 3: ("JYTRACE DE HOUELLE", 16, dict(F=4, GP=6, V=6, R=4, Fer=8, T=3, E=5)),
 4: ("JAIFA DE L'ITON",     5.4, dict(F=6, GP=9, V=7, R=6, Fer=8, T=5, E=7)),
 5: ("JOHORE",             15, dict(F=3, GP=7, V=6, R=2, Fer=8, T=5, E=7)),
 6: ("JAZZ D'OURVILLE",     6.2, dict(F=8, GP=7, V=9, R=6, Fer=8, T=8, E=8)),
 7: ("JOB DES LOUANGES",   23, dict(F=5, GP=3, V=8, R=5, Fer=2, T=4, E=6)),
 8: ("JACKSON D'ARC",      43, dict(F=6, GP=6, V=6, R=7, Fer=2, T=7, E=4)),
 9: ("JOG JELOCA",         8.5, dict(F=8, GP=6, V=2, R=9, Fer=4, T=7, E=3)),
10: ("JUDOPOCK",           23, dict(F=7, GP=3, V=4, R=8, Fer=6, T=5, E=5)),
11: ("JEWEL DE BANVILLE",  6.7, dict(F=2, GP=5, V=3, R=3, Fer=6, T=5, E=7)),
12: ("JOEY DU NOYER",      17, dict(F=5, GP=5, V=5, R=7, Fer=8, T=3, E=8)),
13: ("JOHNNY MIX",         6.6, dict(F=10, GP=2, V=7, R=8, Fer=5, T=5, E=5)),
14: ("JERICHO",            14, dict(F=5, GP=4, V=6, R=6, Fer=8, T=5, E=7)),
}
W = dict(F=0.22, GP=0.20, V=0.15, R=0.13, Fer=0.10, T=0.12, E=0.08)
TAU = 1.5    # température élevée : arrivées serrées / course volatile historiquement
W_MODEL = 0.5  # fusion log-linéaire modèle/marché (rétrécissement vers le marché)

nums = list(H)
sgc = np.array([sum(W[k] * H[n][2][k] for k in W) for n in nums])
p_raw = np.exp(sgc / TAU); p_raw /= p_raw.sum()

# Marché : cote x/1 -> décimale x+1, dévigage multiplicatif
dec = np.array([H[n][1] + 1.0 for n in nums])
imp = 1 / dec; overround = imp.sum(); p_mkt = imp / overround

# Fusion : log p = w log p_modèle + (1-w) log p_marché
p_win = np.exp(W_MODEL*np.log(p_raw) + (1-W_MODEL)*np.log(p_mkt)); p_win /= p_win.sum()

# Monte-Carlo Plackett-Luce (Gumbel trick)
rng = np.random.default_rng(20261002)
N = 200_000
g = rng.gumbel(size=(N, len(nums))) + np.log(p_win)
order = np.argsort(-g, axis=1)
top3 = np.zeros(len(nums)); top5 = np.zeros(len(nums))
for k in range(5):
    c = np.bincount(order[:, k], minlength=len(nums))
    top5 += c
    if k < 3: top3 += c
top3 /= N; top5 /= N

print(f"overround={overround:.3f}")
print(f"{'N°':>2} {'Cheval':20} {'SGC':>5} {'Praw':>6} {'Pwin':>6} {'Pmkt':>6} {'edge':>6} {'P3':>5} {'P5':>5}")
idx = np.argsort(-p_win)
for i in idx:
    n = nums[i]
    print(f"{n:>2} {H[n][0]:20} {sgc[i]:5.2f} {p_raw[i]:6.3f} {p_win[i]:6.3f} {p_mkt[i]:6.3f} "
          f"{p_win[i]-p_mkt[i]:+6.3f} {top3[i]:5.2f} {top5[i]:5.2f}")

# Kelly 1/4 simple gagnant (cote PMU approx.)
# Les cotes fournies sommant à <1 (incohérent pour un pari mutuel), on recalcule
# un rapport réaliste : prélèvement PMU ~16 % appliqué à la proba marché dévigée.
dec_eff = 0.84 / p_mkt
print("\nKelly 1/4 sur rapport réaliste (plafond 2 %):")
for i in idx:
    b = dec_eff[i] - 1; p = p_win[i]
    f = (b * p - (1 - p)) / b
    if f > 0:
        print(f"  {nums[i]:>2} {H[nums[i]][0]:20} rapport~{dec_eff[i]:.1f} f*={f:.3f} -> mise {min(f/4, 0.02)*100:.2f} %")

# Probabilité que le top5 soit contenu dans une sélection
def p_contains(sel):
    s = set(nums.index(n) for n in sel)
    return np.mean([set(r[:5]) <= s for r in order[:50000]])
for sel in ([6,4,13,9,8,14,12,10], [6,4,13,9,8,14,12], [6,4,13,9,8,14], [6,4,13,9,8]):
    print(f"P(top5 ⊂ {sel}) = {p_contains(sel):.3f}")

# Probabilités de base
i6, i4 = nums.index(6), nums.index(4)
print(f"P(6 dans top5)={top5[i6]:.3f}  P(4 dans top5)={top5[i4]:.3f}  "
      f"P(6 et 4 dans top5)={np.mean([(i6 in r[:5]) and (i4 in r[:5]) for r in order[:50000]]):.3f}")

# Tickets Quinté+ (désordre) : base(s) + associés
def p_ticket(bases, assoc):
    b = [nums.index(n) for n in bases]; a = set(nums.index(n) for n in bases + assoc)
    return np.mean([all(x in r[:5] for x in b) and set(r[:5]) <= a for r in order[:100000]])
from math import comb
for bases, assoc in (([6,4], [13,9,14,12,8,11]), ([6,4], [13,9,14,12,8,10]), ([6,4], [13,9,14,12,5,11]), ([6], [4,13,9,14,12,8,11])):
    n = comb(len(assoc), 5-len(bases))
    print(f"Bases {bases} + {assoc}: {n} combis x 2 EUR = {2*n} EUR, P(désordre)={p_ticket(bases, assoc):.3f}")

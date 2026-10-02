"""Scénarios alternatifs du Prix Ludovica 2026 : on ne change que l'adéquation
tactique T (et son poids) ; le reste du modèle (modele.py) est identique."""
import numpy as np
from math import comb
src = open('modele.py').read().split("nums = list(H)")[0]
exec(src)
SCEN = {
 "B - Train contrôlé, la tête tient": {1:3,2:5,3:7,4:9,5:5,6:8,7:5,8:4,9:7,10:5,11:4,12:7,13:6,14:5},
 "C - Train d'enfer, les finisseurs": {1:9,2:6,3:2,4:3,5:5,6:7,7:2,8:9,9:8,10:7,11:6,12:2,13:5,14:6},
}
WT = 0.25
TICKETS = {
 "B - Train contrôlé, la tête tient": [([4,6],[12,3,9,13,14,5])],
 "C - Train d'enfer, les finisseurs": [([6,9],[8,1,10,13,14,4]), ([6],[9,8,1,10,13,14,2])],
}
nums = list(H)
dec = np.array([H[n][1] + 1.0 for n in nums]); p_mkt = (1/dec)/(1/dec).sum()
rng = np.random.default_rng(7)
for name, T in SCEN.items():
    w = {k: v*(1-WT)/(1-W["T"]) for k, v in W.items()}; w["T"] = WT
    sgc = np.array([sum(w[k]*(T[n] if k=="T" else H[n][2][k]) for k in w) for n in nums])
    p_raw = np.exp(sgc/TAU); p_raw /= p_raw.sum()
    p = np.exp(W_MODEL*np.log(p_raw)+(1-W_MODEL)*np.log(p_mkt)); p /= p.sum()
    order = np.argsort(-(rng.gumbel(size=(100000, len(nums))) + np.log(p)), axis=1)
    top5 = np.array([np.mean((order[:, :5] == i).any(1)) for i in range(len(nums))])
    print(f"\n=== {name} ===")
    for i in np.argsort(-p)[:9]:
        print(f"{nums[i]:>2} {H[nums[i]][0]:20} Pwin={p[i]:.3f} Pmkt={p_mkt[i]:.3f} edge={p[i]-p_mkt[i]:+.3f} P5={top5[i]:.2f}")
    for bases, assoc in TICKETS[name]:
        b = [nums.index(x) for x in bases]; a = set(nums.index(x) for x in bases+assoc)
        hit = np.mean([all(x in r[:5] for x in b) and set(r[:5]) <= a for r in order[:60000]])
        print(f"Ticket bases {bases} + {assoc}: {2*comb(len(assoc),5-len(bases))} EUR, P(désordre)={hit:.3f}")

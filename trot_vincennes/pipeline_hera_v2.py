"""Prix Héra v2 — modèle de forme à partir de data/Prix_Hera_R1C4_09-10-2026.docx.

Composantes (z-scores) : vitesse (RK comparables Vincennes GP / Enghien volté,
corrigée du recul), forme pondérée par la classe, aptitude GP, forme écurie /
driver 30 j, ferrure du jour. Le risque de faute est simulé à part (un cheval
fautif est classé dernier). Température calée sur la dispersion du marché,
puis pooling logarithmique modèle/marché.
"""
import json
import numpy as np

RNG = np.random.default_rng(20261009)
N_SIM = 200_000
W_MODEL = 0.6  # poids du modèle dans le pooling (données partiellement contradictoires)
HAIRCUT = 0.90  # tassement prudent des cotes de 13h24 jusqu'au départ

PTS = {1: 10, 2: 7, 3: 5.5, 4: 4.5, 5: 3.5, 6: 2.5, 7: 2, 8: 1.5, 9: 1}
REC = [1, .85, .72, .6, .5]

# n: nom, échelon, 5 dernières (place|'D'|'A', facteur de classe), RK comparable (s/km),
#    RK imputé ?, taux de faute, (places+victoires GP, sorties GP), %victoire écurie 30 j,
#    score ferrure du jour, cote 13h24
H = {
    1: ("Igloo de Beaulieu", 0, [("D", .45), (0, .45), ("D", .45), ("D", .4), (9, .45)], 75.5, True, .45, (0, 6), 5.0, -1, 88.1),
    2: ("Heaven d'Ecajeul", 0, [(2, .8), (4, 1), (0, .65), (5, 1), (3, 1)], 72.65, False, .10, (7, 18), 13.4, .5, 13.6),
    3: ("Horacio de Cerisy", 0, [(5, 1), (0, .65), (5, .5), (0, .6), (0, 1)], 74.2, True, .12, (3, 12), 8.0, 1, 58.1),
    4: ("History Majyc", 0, [(7, 1), (10, 1), (5, .65), (2, .65), (8, .6)], 73.65, False, .08, (5, 22), 5.6, .5, 74.9),
    5: ("Jytrace de Houelle", 0, [("D", 1), (4, 1), (11, 1), ("D", 1), (0, 1.15)], 73.25, False, .30, (5, 14), 16.3, 1, 8.4),
    6: ("Jannig d'Erevan", 0, [(2, .6), (1, .5), (2, .4), (6, .5), (4, .35)], 73.6, True, .12, (0, 1), 14.7, .5, 8.9),
    7: ("Izijal", 0, [(9, .65), (12, 1), (0, .6), (0, .6), (7, 1)], 73.55, False, .07, (5, 15), 13.7, 0, 19.8),
    8: ("Horizon du Thay", 0, [(5, .65), (1, .5), (2, .4), (4, .35), (8, .45)], 73.8, True, .06, (0, 0), 9.5, 1, 30.3),
    9: ("Inédit du Pavillon", 0, [(6, .8), (7, 1), ("D", .65), (9, 1), (8, .45)], 73.55, False, .15, (2, 11), 9.0, 0, 33.4),
    10: ("Irish Nice Elgé", 1, [(1, 1), (3, 1), ("D", 1), (8, 1), (2, .65)], 72.5, False, .22, (5, 10), 14.0, 1, 4.5),
    11: ("Hove Pont Vautier", 1, [(12, .8), (11, 1), (10, .7), (6, 1.15), (8, 1.15)], 73.8, False, .08, (9, 28), 4.0, -1, 91.1),
    12: ("Inherit", 1, [(6, .8), (3, 1), (3, .7), ("A", 1), (7, .65)], 72.9, False, .12, (6, 16), 8.5, .5, 15.3),
    13: ("I Still Loving You", 1, [(3, .8), ("D", 1), (1, 1), (3, 1), (1, 1)], 72.7, False, .25, (10, 19), 19.0, .5, 5.9),
    14: ("Indien de Fontaine", 1, [(1, .8), (4, 1), (8, 1), (5, 1), (9, 1)], 72.9, False, .08, (6, 15), 18.6, .5, 6.9),
    15: ("Ileo Pierji", 1, [(2, .6), (5, 1), (6, 1), (4, 1), (5, 1)], 72.95, False, .12, (10, 25), 12.6, 1, 10.3),
}
WEIGHTS = {"vitesse": .35, "forme": .25, "ecurie": .15, "aptitude_gp": .10, "ferrure": .10}
RECUL_S_PER_KM = 0.64  # 25 m sur ~2 850 m à ~1'13 de réduction ≈ +0,64 s/km


def form_score(runs):
    num = den = 0.0
    for w, (pl, cls) in zip(REC, runs):
        if pl in ("D", "A"):
            continue  # la faute est traitée par le risque de faute, pas ici
        num += w * PTS.get(pl, 0.5) * cls
        den += w
    return num / den if den else 0.0


def z(x):
    x = np.asarray(x, float)
    return (x - x.mean()) / x.std()


def devig_power(odds):
    q = 1.0 / np.asarray(odds, float)
    lo, hi = 1.0, 3.0
    for _ in range(100):
        k = (lo + hi) / 2
        lo, hi = (k, hi) if (q ** k).sum() > 1 else (lo, k)
    p = q ** k
    return p / p.sum()


def simulate(s, pfault, n_sim=N_SIM):
    g = RNG.gumbel(size=(n_sim, len(s)))
    key = s + g
    key[RNG.random((n_sim, len(s))) < pfault] -= 1e3  # fautif → classé dernier
    order = np.argsort(-key, axis=1)
    rank = np.empty_like(order)
    rank[np.arange(n_sim)[:, None], order] = np.arange(len(s))
    return rank


def main():
    nums = sorted(H)
    D = [H[n] for n in nums]
    rk_eff = np.array([d[3] + RECUL_S_PER_KM * d[1] for d in D])
    comps = {
        "vitesse": z(-rk_eff),
        "forme": z([form_score(d[2]) for d in D]),
        "ecurie": z([d[7] for d in D]),
        "aptitude_gp": z([(d[6][0] + 3 * .28) / (d[6][1] + 3) for d in D]),
        "ferrure": z([d[8] for d in D]),
    }
    comp = sum(WEIGHTS[k] * v for k, v in comps.items())
    pfault = np.array([d[5] for d in D])
    odds = np.array([d[9] for d in D])
    p_mkt = devig_power(odds)

    # Température : la dispersion du marché fixe β (on garde le classement du modèle)
    def win_probs(beta, n=40_000):
        r = simulate(beta * comp, pfault, n)
        return (r == 0).mean(0)
    target = np.sort(p_mkt)[::-1][:5].sum()
    beta = min(np.linspace(.5, 4, 36), key=lambda b: abs(np.sort(win_probs(b))[::-1][:5].sum() - target))
    p_form = win_probs(beta, N_SIM)

    # Pooling logarithmique modèle / marché
    p_pool = p_form ** W_MODEL * p_mkt ** (1 - W_MODEL)
    p_pool /= p_pool.sum()
    # Force PL équivalente pour les places (point fixe sur p(1er) avec fautes)
    s = np.log(p_pool)
    for _ in range(30):
        pw = (simulate(s, pfault, 40_000) == 0).mean(0)
        s += 0.8 * (np.log(p_pool) - np.log(np.maximum(pw, 1e-5)))
    rank = simulate(s, pfault)
    p1, p3, p5 = [(rank < k).mean(0) for k in (1, 3, 5)]

    rows = []
    for i, n in enumerate(nums):
        o = odds[i] * HAIRCUT
        kelly = max(0.0, (p1[i] * o - 1) / (o - 1))
        rows.append(dict(n=n, cheval=D[i][0], cote_13h24=odds[i], rk_eff=round(rk_eff[i], 2),
                         composite=round(comp[i], 3), p_faute=pfault[i],
                         p_forme=round(p_form[i], 4), p_mkt=round(p_mkt[i], 4),
                         p_gagnant=round(p1[i], 4), p_top3=round(p3[i], 4), p_top5=round(p5[i], 4),
                         edge=round(p1[i] - p_mkt[i], 4), kelly_quart=round(kelly / 4, 4),
                         **{f"z_{k}": round(v[i], 2) for k, v in comps.items()}))
    rows.sort(key=lambda r: -r["p_gagnant"])
    idx = {n: i for i, n in enumerate(nums)}

    def both_top(k, *ns):
        return round(float(np.all([rank[:, idx[n]] < k for n in ns], axis=0).mean()), 4)
    extra = {
        "beta": round(float(beta), 2),
        "couple_gagnant_10_13": both_top(2, 10, 13), "couple_gagnant_10_14": both_top(2, 10, 14),
        "couple_gagnant_13_14": both_top(2, 13, 14), "2sur4_10_14": both_top(4, 10, 14),
        "2sur4_13_14": both_top(4, 13, 14), "2sur4_10_13": both_top(4, 10, 13),
    }
    # Couverture du Quinté+ désordre en champ réduit : base 10 + 6 associés (15 combinaisons)
    top5 = np.argsort(rank, axis=1)[:, :5]
    for label, assoc in {"base10_13-14-2-15-5-6": [13, 14, 2, 15, 5, 6],
                         "base10_13-14-2-15-12-6": [13, 14, 2, 15, 12, 6]}.items():
        ok = np.isin(top5, [idx[n] for n in [10] + assoc]).all(axis=1) & (rank[:, idx[10]] < 5)
        extra["quinte_" + label] = round(float(ok.mean()), 4)
    json.dump(dict(rows=rows, extra=extra), open("output/resultats_hera_v2.json", "w"), ensure_ascii=False, indent=1)
    print(f"beta={beta:.2f}")
    print(f"{'n':>2} {'cheval':20} {'cote':>5} {'RKeff':>6} {'comp':>6} {'pFrm':>6} {'pMkt':>6} {'pWin':>6} {'top3':>5} {'top5':>5} {'edge':>6} {'K/4':>6}")
    for r in rows:
        print(f"{r['n']:>2} {r['cheval']:20} {r['cote_13h24']:>5} {r['rk_eff']:6.2f} {r['composite']:+6.2f} {r['p_forme']:6.3f} "
              f"{r['p_mkt']:6.3f} {r['p_gagnant']:6.3f} {r['p_top3']:5.2f} {r['p_top5']:5.2f} {r['edge']:+6.3f} {r['kelly_quart']:6.4f}")
    print(extra)


if __name__ == "__main__":
    main()

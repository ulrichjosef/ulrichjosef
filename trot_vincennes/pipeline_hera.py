"""Prix Héra — Vincennes R1C4 09/10/2026 (trot attelé, volté, GP 2850/2875 m).

Mode « marché + ajustements » : aucune musique / aucun chrono / aucune réduction
kilométrique n'a été fournie, donc le prior est la probabilité PMU dévigée
(méthode power) et seuls des ajustements contextuels modestes sont appliqués.
"""
import json
import numpy as np

RNG = np.random.default_rng(20261009)
N_SIM = 200_000

# n, nom, sexe/âge, échelon (0 = 2850, 1 = 2875), ferrure, driver, gains, cote PMU (rapport brut)
PARTANTS = [
    (1, "Igloo de Beaulieu", "H8", 0, "P4", "J. Condette", 97250, 99),
    (2, "Heaven d'Ecajeul", "H9", 0, "Pa", "G. Gelormini", 155190, 16),
    (3, "Horacio de Cerisy", "H9", 0, "D4", "A. Gendrot", 155390, 30),
    (4, "History Majyc", "F9", 0, "Pa/Dp", "F. Tabesse", 156955, 60),
    (5, "Jytrace de Houelle", "H7", 0, "D4", "M. Mottier", 162960, 8.7),
    (6, "Jannig d'Erevan", "M7", 0, "Pa/Dp", "D. Bonne", 163500, 10),
    (7, "Izijal", "H8", 0, "Pa/Dp", "D. Thomain", 166505, 45),
    (8, "Horizon du Thay", "H9", 0, "D4", "N.-R. Brossard", 168605, 28),
    (9, "Inédit du Pavillon", "H8", 0, "DP", "F. Lagadeuc", 168605, 50),
    (10, "Irish Nice Elgé", "H8", 1, "D4", "M. Abrivard", 277570, 3.3),
    (11, "Hove Pont Vautier", "H9", 1, "Pa", "A. Mériel", 283290, 80),
    (12, "Inherit", "H8", 1, "Pa/Dp", "P.-Y. Verva", 286325, 18),
    (13, "I Still Loving You", "M8", 1, "DP", "A. Abrivard", 294350, 5.1),
    (14, "Indien de Fontaine", "H8", 1, "Pa/Dp", "E. Raffin", 296000, 7.8),
    (15, "Ileo Pierji", "H8", 1, "D4", "A. Barrier", 298265, 12),
]

# Ajustements en unités de log-force (ESTIMÉS, volontairement faibles :
# le marché intègre déjà la plupart de ces informations).
ADJ_FERRURE = {"D4": 0.06, "DP": 0.03, "Pa/Dp": 0.02, "Pa": 0.0, "P4": -0.04}
ADJ_AGE = {7: 0.05, 8: 0.0, 9: -0.04}  # 7 ans encore en progression, 9 ans en plateau
TOP_DRIVERS = {"M. Abrivard", "A. Abrivard", "E. Raffin", "D. Thomain",
               "G. Gelormini", "A. Barrier", "F. Lagadeuc"}
ADJ_DRIVER = 0.03
ADJ_VOLTE_RECUL = -0.03  # second échelon : risque de faute au départ volté en remontant le lot


def devig_power(odds):
    q = 1.0 / np.asarray(odds, float)
    lo, hi = 1.0, 3.0
    for _ in range(100):
        k = (lo + hi) / 2
        if (q ** k).sum() > 1:
            lo = k
        else:
            hi = k
    p = q ** k
    return p / p.sum(), k


def main():
    odds = np.array([p[7] for p in PARTANTS], float)
    overround = (1 / odds).sum()
    p_mkt, k = devig_power(odds)

    adj = np.zeros(len(PARTANTS))
    for i, (n, nom, sa, ech, fer, drv, gains, cote) in enumerate(PARTANTS):
        adj[i] += ADJ_FERRURE[fer] + ADJ_AGE[int(sa[1:])]
        adj[i] += ADJ_DRIVER if drv in TOP_DRIVERS else 0.0
        adj[i] += ADJ_VOLTE_RECUL if ech == 1 else 0.0
    adj -= adj.mean()  # neutre en moyenne
    s = np.log(p_mkt) + adj
    p_mod = np.exp(s) / np.exp(s).sum()

    # Monte-Carlo Plackett-Luce (perturbation Gumbel)
    g = RNG.gumbel(size=(N_SIM, len(PARTANTS)))
    order = np.argsort(-(s + g), axis=1)
    rank = np.empty_like(order)
    rank[np.arange(N_SIM)[:, None], order] = np.arange(len(PARTANTS))
    p_top3 = (rank < 3).mean(0)
    p_top5 = (rank < 5).mean(0)

    rows = []
    for i, part in enumerate(PARTANTS):
        edge = p_mod[i] - p_mkt[i]
        b = odds[i] * 0.85 - 1  # rapport réel estimé ≈ cote affichée tassée de 15 % au départ
        kelly = max(0.0, (p_mod[i] * (b + 1) - 1) / b) if b > 0 else 0.0
        rows.append(dict(n=part[0], cheval=part[1], cote=part[7], adj=round(adj[i], 3),
                         p_mkt=round(p_mkt[i], 4), p_mod=round(p_mod[i], 4),
                         p_top3=round(p_top3[i], 4), p_top5=round(p_top5[i], 4),
                         edge=round(edge, 4), kelly_quart=round(kelly / 4, 4)))
    rows.sort(key=lambda r: -r["p_mod"])

    top5_order = [r["n"] for r in rows[:5]]
    combos = {}
    for key, idx in {"couple_10_13": (9, 12), "couple_10_14": (9, 13), "couple_10_5": (9, 4)}.items():
        combos[key] = round(((rank[:, idx[0]] < 2) & (rank[:, idx[1]] < 2)).mean(), 4)
    out = dict(overround=round(overround, 4), k_power=round(k, 4), partants=rows,
               ordre_modele=top5_order, couples=combos)
    json.dump(out, open("output/resultats_hera.json", "w"), ensure_ascii=False, indent=1)
    print(f"overround={overround:.3f}  k={k:.3f}")
    print(f"{'n':>2} {'cheval':22} {'cote':>5} {'pMkt':>6} {'pMod':>6} {'top3':>6} {'top5':>6} {'edge':>7} {'K/4':>6}")
    for r in rows:
        print(f"{r['n']:>2} {r['cheval']:22} {r['cote']:>5} {r['p_mkt']:6.3f} {r['p_mod']:6.3f} "
              f"{r['p_top3']:6.3f} {r['p_top5']:6.3f} {r['edge']:+7.4f} {r['kelly_quart']:6.4f}")
    print(combos)


if __name__ == "__main__":
    main()

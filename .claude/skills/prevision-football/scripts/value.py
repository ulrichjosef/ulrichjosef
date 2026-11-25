#!/usr/bin/env python3
"""Dévigage, edge, mise Kelly fractionnée et CLV (Python standard).

Exemples :
  # Marché 1X2 avec probas modèle -> tableau value + mises
  python value.py --odds 1=2.10 X=3.40 2=3.70 --model 1=0.52 X=0.26 2=0.22 \
      --bankroll 1000 --kelly 0.25 --cap 0.02 --min-edge 0.05 --method shin

  # CLV d'un pari pris à 2.10 contre les cotes de clôture
  python value.py clv --taken 2.10 --selection 1 --closing 1=1.95 X=3.50 2=4.10

Méthodes de dévigage :
  multiplicative : p_i = (1/c_i) / somme(1/c_j)          (celle de la plateforme)
  power          : p_i = (1/c_i)^k, k tel que somme = 1   (corrige le biais favori/outsider)
  shin           : modèle de Shin (initiés)               (recommandé sur marchés à outsiders)

Seuil de value : edge relatif EV = p_modele * cote - 1. La plateforme
sports-forecasting-platform ne transmet un pick que si EV >= 5 % (par défaut).
"""

from __future__ import annotations

import argparse
import json
import math


def parse_kv(items: list[str]) -> dict[str, float]:
    out = {}
    for it in items:
        k, v = it.split("=", 1)
        out[k.strip()] = float(v)
    return out


def devig(odds: dict[str, float], method: str = "multiplicative") -> dict[str, float]:
    for k, v in odds.items():
        if v <= 1.0:
            raise SystemExit(f"Cote invalide pour {k}: {v} (doit être > 1)")
    imp = {k: 1 / v for k, v in odds.items()}
    if method == "multiplicative":
        s = sum(imp.values())
        return {k: p / s for k, p in imp.items()}
    if method == "power":
        lo, hi = 0.5, 5.0
        for _ in range(200):
            k_ = (lo + hi) / 2
            s = sum(p**k_ for p in imp.values())
            lo, hi = (k_, hi) if s > 1 else (lo, k_)
        return {k: p**k_ for k, p in imp.items()}
    if method == "shin":
        s = sum(imp.values())
        n = len(imp)
        lo, hi = 0.0, 0.4
        def probs(z: float) -> dict[str, float]:
            return {k: (math.sqrt(z * z + 4 * (1 - z) * p * p / s) - z) / (2 * (1 - z))
                    for k, p in imp.items()}
        for _ in range(200):
            z = (lo + hi) / 2
            t = sum(probs(z).values())
            lo, hi = (z, hi) if t > 1 else (lo, z)
        pr = probs(z)
        t = sum(pr.values())
        return {k: v / t for k, v in pr.items()} if n else pr
    raise SystemExit(f"Méthode inconnue : {method}")


def kelly_fraction(p: float, odd: float) -> float:
    b = odd - 1
    return max((b * p - (1 - p)) / b, 0.0)


def clv_pct(taken: float, closing: dict[str, float], selection: str, method: str) -> float:
    fair_p = devig(closing, method)[selection]
    return (taken * fair_p - 1) * 100


def main() -> None:
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "clv":
        ap = argparse.ArgumentParser(prog="value.py clv")
        ap.add_argument("clv")
        ap.add_argument("--taken", type=float, required=True)
        ap.add_argument("--selection", required=True)
        ap.add_argument("--closing", nargs="+", required=True)
        ap.add_argument("--method", default="multiplicative")
        a = ap.parse_args()
        c = clv_pct(a.taken, parse_kv(a.closing), a.selection, a.method)
        print(json.dumps({"clv_pct": round(c, 2),
                          "lecture": "positif = cote prise meilleure que la clôture juste "
                                     "(meilleur indicateur précoce d'un vrai edge)"},
                         ensure_ascii=False, indent=2))
        return

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--odds", nargs="+", required=True, help="issue=cote ...")
    ap.add_argument("--model", nargs="+", help="issue=proba ... (même clés)")
    ap.add_argument("--method", default="shin", choices=["multiplicative", "power", "shin"])
    ap.add_argument("--bankroll", type=float, default=100.0)
    ap.add_argument("--kelly", type=float, default=0.25, help="fraction de Kelly (0.25 = quart)")
    ap.add_argument("--cap", type=float, default=0.02, help="mise max en part de bankroll")
    ap.add_argument("--min-edge", type=float, default=0.05, help="EV minimum (0.05 = 5 %%)")
    a = ap.parse_args()

    odds = parse_kv(a.odds)
    overround = sum(1 / v for v in odds.values()) - 1
    fair = devig(odds, a.method)
    rows = []
    model = parse_kv(a.model) if a.model else {}
    if model and abs(sum(model.values()) - 1) > 0.02 and len(model) == len(odds):
        print(f"# avertissement : probas modèle somment à {sum(model.values()):.3f}", file=sys.stderr)
    for k, c in odds.items():
        r = {"issue": k, "cote": c, "p_marche_devig": round(fair[k], 4),
             "cote_juste_marche": round(1 / fair[k], 3)}
        if k in model:
            p = model[k]
            ev = p * c - 1
            f = min(kelly_fraction(p, c) * a.kelly, a.cap)
            value = ev >= a.min_edge
            r.update({"p_modele": p, "edge_pp": round(p - fair[k], 4), "ev": round(ev, 4),
                      "value": value,
                      "mise_pct_bankroll": round(f * 100, 2) if value else 0.0,
                      "mise": round(f * a.bankroll, 2) if value else 0.0})
        rows.append(r)
    print(json.dumps({"marge_bookmaker_pct": round(overround * 100, 2), "methode": a.method,
                      "regles": {"kelly": a.kelly, "plafond": a.cap, "ev_min": a.min_edge},
                      "selections": rows}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

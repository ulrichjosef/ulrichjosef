#!/usr/bin/env python3
"""Modèle de buts football (Python standard, sans dépendance).

Deux modes :

1. Depuis des espérances de buts connues :
       python match_model.py grid --lambda-home 1.55 --lambda-away 1.05 [--rho -0.08]
2. En ajustant des forces attaque/défense sur un historique CSV
   (colonnes : date,home,away,home_goals,away_goals ; date AAAA-MM-JJ) :
       python match_model.py fit --csv resultats.csv --home "PSG" --away "Lyon" \
           [--half-life-days 180] [--as-of 2026-11-25] [--neutral]

Méthodes reprises de sports-forecasting-platform (MIT, K. Beltrán) :
- Dixon-Coles (1997) : correction tau des scores faibles (0-0, 1-0, 0-1, 1-1).
- Pondération temporelle exponentielle (demi-vie) : seuls les matchs
  ANTÉRIEURS à --as-of sont utilisés (aucune fuite de données).
- Bivariate Poisson diagonal-inflaté (DIBP) optionnel via --pi-diag/--theta-diag
  pour les compétitions à forte proportion de nuls.

Sortie JSON : lambdas, 1X2, double chance, DNB, BTTS, over/under 0.5..4.5,
handicaps -1/+1, top 10 scores exacts.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from datetime import date

MAX_GOALS = 10


def poisson_pmf(k: int, lam: float) -> float:
    return math.exp(-lam) * lam**k / math.factorial(k)


def dc_tau(x: int, y: int, lh: float, la: float, rho: float) -> float:
    if x == 0 and y == 0:
        return 1 - lh * la * rho
    if x == 0 and y == 1:
        return 1 + lh * rho
    if x == 1 and y == 0:
        return 1 + la * rho
    if x == 1 and y == 1:
        return 1 - rho
    return 1.0


def score_grid(lh: float, la: float, rho: float = 0.0,
               pi_diag: float = 0.0, theta_diag: float = 0.3) -> list[list[float]]:
    lh, la = max(lh, 1e-6), max(la, 1e-6)
    ph = [poisson_pmf(i, lh) for i in range(MAX_GOALS + 1)]
    pa = [poisson_pmf(j, la) for j in range(MAX_GOALS + 1)]
    g = [[max(ph[i] * pa[j] * dc_tau(i, j, lh, la, rho), 0.0)
          for j in range(MAX_GOALS + 1)] for i in range(MAX_GOALS + 1)]
    if pi_diag > 0:
        g = [[(1 - pi_diag) * v for v in row] for row in g]
        for k in range(MAX_GOALS + 1):
            g[k][k] += pi_diag * (1 - theta_diag) * theta_diag**k
    tot = sum(map(sum, g))
    return [[v / tot for v in row] for row in g]


def markets(g: list[list[float]]) -> dict:
    n = len(g)
    cells = [(i, j, g[i][j]) for i in range(n) for j in range(n)]
    p = lambda f: sum(v for i, j, v in cells if f(i, j))  # noqa: E731
    h, d, a = p(lambda i, j: i > j), p(lambda i, j: i == j), p(lambda i, j: i < j)
    out = {
        "1X2": {"1": h, "X": d, "2": a},
        "double_chance": {"1X": h + d, "12": h + a, "X2": d + a},
        "draw_no_bet": {"1": h / (h + a), "2": a / (h + a)},
        "btts": {"oui": p(lambda i, j: i >= 1 and j >= 1)},
        "over_under": {},
        "handicap": {
            "dom_-1 (gagne par 2+)": p(lambda i, j: i - j >= 2),
            "ext_+1 (ne perd pas de 2+)": p(lambda i, j: i - j <= 1),
            "ext_-1 (gagne par 2+)": p(lambda i, j: j - i >= 2),
        },
        "esperance_buts": {
            "dom": sum(i * v for i, j, v in cells),
            "ext": sum(j * v for i, j, v in cells),
        },
    }
    out["btts"]["non"] = 1 - out["btts"]["oui"]
    for line in (0.5, 1.5, 2.5, 3.5, 4.5):
        over = p(lambda i, j, L=line: i + j > L)
        out["over_under"][f"over_{line}"] = over
        out["over_under"][f"under_{line}"] = 1 - over
    top = sorted(cells, key=lambda c: -c[2])[:10]
    out["scores_exacts_top10"] = [{"score": f"{i}-{j}", "p": v} for i, j, v in top]
    return out


# ---------------------------------------------------------------- ajustement

def load_matches(path: str, as_of: date, half_life: float) -> list[tuple]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            d = date.fromisoformat(r["date"][:10])
            if d >= as_of:  # strictement antérieur : pas de fuite
                continue
            w = 0.5 ** ((as_of - d).days / half_life)
            neutral = str(r.get("neutral", "")).strip().lower() in ("1", "true", "oui")
            rows.append((r["home"].strip(), r["away"].strip(),
                         int(r["home_goals"]), int(r["away_goals"]), w, neutral))
    if not rows:
        raise SystemExit("Aucun match antérieur à --as-of dans le CSV.")
    return rows


def fit_strengths(rows: list[tuple], iters: int = 200) -> tuple[dict, dict, float, float]:
    """Ajustement Maher pondéré (point fixe du MLE de Poisson indépendant)."""
    teams = sorted({r[0] for r in rows} | {r[1] for r in rows})
    att = {t: 1.0 for t in teams}
    dfn = {t: 1.0 for t in teams}
    home_adv = 1.25
    for _ in range(iters):
        for t in teams:
            num = sum(w * hg for h, a, hg, ag, w, n in rows if h == t) + \
                  sum(w * ag for h, a, hg, ag, w, n in rows if a == t)
            den = sum(w * dfn[a] * (1 if n else home_adv) for h, a, hg, ag, w, n in rows if h == t) + \
                  sum(w * dfn[h] for h, a, hg, ag, w, n in rows if a == t)
            att[t] = num / den if den > 0 else 1.0
        for t in teams:
            num = sum(w * ag for h, a, hg, ag, w, n in rows if h == t) + \
                  sum(w * hg for h, a, hg, ag, w, n in rows if a == t)
            den = sum(w * att[a] for h, a, hg, ag, w, n in rows if h == t) + \
                  sum(w * att[h] * (1 if n else home_adv) for h, a, hg, ag, w, n in rows if a == t)
            dfn[t] = num / den if den > 0 else 1.0
        m = sum(att.values()) / len(att)
        att = {t: v / m for t, v in att.items()}
        dfn = {t: v * m for t, v in dfn.items()}
        num = sum(w * hg for h, a, hg, ag, w, n in rows if not n)
        den = sum(w * att[h] * dfn[a] for h, a, hg, ag, w, n in rows if not n)
        home_adv = num / den if den > 0 else 1.0
    # rho Dixon-Coles par recherche en grille sur la vraisemblance pondérée
    best_rho, best_ll = 0.0, -math.inf
    for k in range(-30, 11):
        rho = k / 100
        ll = 0.0
        for h, a, hg, ag, w, n in rows:
            lh = att[h] * dfn[a] * (1 if n else home_adv)
            la = att[a] * dfn[h]
            tau = dc_tau(hg, ag, lh, la, rho)
            if tau <= 0:
                ll = -math.inf
                break
            ll += w * math.log(tau)
        if ll > best_ll:
            best_rho, best_ll = rho, ll
    return att, dfn, home_adv, best_rho


def rnd(o, nd: int = 4):
    if isinstance(o, float):
        return round(o, nd)
    if isinstance(o, dict):
        return {k: rnd(v, nd) for k, v in o.items()}
    if isinstance(o, list):
        return [rnd(v, nd) for v in o]
    return o


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("grid")
    g.add_argument("--lambda-home", type=float, required=True)
    g.add_argument("--lambda-away", type=float, required=True)
    g.add_argument("--rho", type=float, default=-0.08)
    f = sub.add_parser("fit")
    f.add_argument("--csv", required=True)
    f.add_argument("--home", required=True)
    f.add_argument("--away", required=True)
    f.add_argument("--as-of", default=date.today().isoformat())
    f.add_argument("--half-life-days", type=float, default=180.0)
    f.add_argument("--neutral", action="store_true")
    for p in (g, f):
        p.add_argument("--pi-diag", type=float, default=0.0, help="inflation diagonale DIBP (0 = off)")
        p.add_argument("--theta-diag", type=float, default=0.3)
    args = ap.parse_args()

    meta: dict = {}
    if args.cmd == "grid":
        lh, la, rho = args.lambda_home, args.lambda_away, args.rho
    else:
        rows = load_matches(args.csv, date.fromisoformat(args.as_of), args.half_life_days)
        att, dfn, hadv, rho = fit_strengths(rows)
        for t in (args.home, args.away):
            if t not in att:
                raise SystemExit(f"Équipe inconnue dans l'historique : {t!r}")
        lh = att[args.home] * dfn[args.away] * (1 if args.neutral else hadv)
        la = att[args.away] * dfn[args.home]
        n_home = sum(1 for r in rows if args.home in r[:2])
        n_away = sum(1 for r in rows if args.away in r[:2])
        meta = {"avantage_domicile": hadv, "matchs_utilises": len(rows),
                "matchs_equipe": {args.home: n_home, args.away: n_away},
                "attaque": {args.home: att[args.home], args.away: att[args.away]},
                "defense": {args.home: dfn[args.home], args.away: dfn[args.away]},
                "avertissement": "échantillon faible (<15 matchs/équipe) : élargir l'incertitude"
                if min(n_home, n_away) < 15 else None}
    grid = score_grid(lh, la, rho, args.pi_diag, args.theta_diag)
    out = {"lambda_dom": lh, "lambda_ext": la, "rho": rho, **meta, "marches": markets(grid)}
    print(json.dumps(rnd(out), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Rapport de calibration d'un journal de pronostics (JSONL, Python standard).

Une ligne JSON par sélection, champs utilisés :
  p_modele (0-1) *, resultat ("gagne"|"perdu"|null) *, discipline, marche,
  mise, gain_net, cote, cote_cloture, clv_pct, date_evenement

Calcule (méthodes de sports-forecasting-platform) :
- Brier + intervalle de confiance bootstrap 95 %,
- log-loss,
- ECE (10 bins) + test de remplissage des bins (>= 80 % sinon ECE non fiable),
- courbe de fiabilité par bin,
- ROI réalisé,
- CLV moyen glissant sur les 50 derniers paris : alerte si < +1 %
  (règle « pause & audit » de la plateforme).

Usage :
  python calibration_report.py --journal journal.jsonl [--discipline football] \
      [--marche 1X2] [--bins 10] [--json]
"""

from __future__ import annotations

import argparse
import json
import math
import random


def load(path: str) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"Ligne {n} illisible : {e}")
    return rows


def brier(ps, ys):
    return sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps)


def logloss(ps, ys):
    eps = 1e-12
    return -sum(y * math.log(max(p, eps)) + (1 - y) * math.log(max(1 - p, eps))
                for p, y in zip(ps, ys)) / len(ps)


def bootstrap_ci(ps, ys, n=2000, seed=42):
    rnd = random.Random(seed)
    idx = range(len(ps))
    vals = []
    for _ in range(n):
        s = [rnd.choice(idx) for _ in idx]
        vals.append(brier([ps[i] for i in s], [ys[i] for i in s]))
    vals.sort()
    return vals[int(0.025 * n)], vals[int(0.975 * n) - 1]


def reliability(ps, ys, bins):
    out = []
    for b in range(bins):
        lo, hi = b / bins, (b + 1) / bins
        sel = [(p, y) for p, y in zip(ps, ys) if lo <= p < hi or (b == bins - 1 and p == 1.0)]
        if sel:
            mp = sum(p for p, _ in sel) / len(sel)
            fy = sum(y for _, y in sel) / len(sel)
            out.append({"bin": f"{lo:.2f}-{hi:.2f}", "n": len(sel), "p_moy": round(mp, 4),
                        "freq_obs": round(fy, 4), "ecart": round(fy - mp, 4)})
    return out


def report(rows: list[dict], bins: int) -> dict:
    res = [r for r in rows if r.get("resultat") in ("gagne", "perdu") and r.get("p_modele") is not None]
    out: dict = {"total": len(rows), "resolus": len(res), "en_attente": len(rows) - len(res)}
    if not res:
        return out
    ps = [float(r["p_modele"]) for r in res]
    ys = [1 if r["resultat"] == "gagne" else 0 for r in res]
    rel = reliability(ps, ys, bins)
    ece = sum(b["n"] * abs(b["ecart"]) for b in rel) / len(ps)
    lo, hi = bootstrap_ci(ps, ys)
    filled = len(rel) / bins
    out.update({
        "brier": round(brier(ps, ys), 4), "brier_ic95": [round(lo, 4), round(hi, 4)],
        "log_loss": round(logloss(ps, ys), 4),
        "ece": round(ece, 4), "bins_remplis_pct": round(filled * 100, 1),
        "ece_fiable": filled >= 0.8,
        "taux_reussite": round(sum(ys) / len(ys), 4), "p_moyenne": round(sum(ps) / len(ps), 4),
        "courbe_fiabilite": rel,
    })
    if len(res) < 50:
        out["avertissement"] = "moins de 50 pronostics résolus : aucune correction de poids justifiable"
    staked = [r for r in res if r.get("mise") and r.get("gain_net") is not None]
    if staked:
        m = sum(float(r["mise"]) for r in staked)
        g = sum(float(r["gain_net"]) for r in staked)
        out["roi_pct"] = round(100 * g / m, 2) if m else None
        out["mises_total"], out["gain_net_total"] = round(m, 2), round(g, 2)
    clv = [float(r["clv_pct"]) for r in sorted(res, key=lambda r: r.get("date_evenement", ""))
           if r.get("clv_pct") is not None]
    if not clv:
        clv = [(float(r["cote"]) / float(r["cote_cloture"]) - 1) * 100
               for r in res if r.get("cote") and r.get("cote_cloture")]
    if clv:
        w = clv[-50:]
        avg = sum(w) / len(w)
        out["clv_moyen_50_derniers_pct"] = round(avg, 2)
        out["clv_alerte"] = (avg < 1.0 and len(w) >= 50)
        out["clv_lecture"] = ("ALERTE : CLV glissant < +1 % sur 50 paris → pause et audit"
                              if out["clv_alerte"] else
                              "CLV sur moins de 50 paris : indicatif" if len(w) < 50 else "CLV sain")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--journal", required=True)
    ap.add_argument("--discipline")
    ap.add_argument("--marche")
    ap.add_argument("--bins", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = load(a.journal)
    if a.discipline:
        rows = [r for r in rows if r.get("discipline") == a.discipline]
    if a.marche:
        rows = [r for r in rows if r.get("marche") == a.marche]
    full = {"global": report(rows, a.bins), "par_discipline": {}, "par_marche": {}}
    for key, dest in (("discipline", "par_discipline"), ("marche", "par_marche")):
        for v in sorted({r.get(key) for r in rows if r.get(key)}):
            sub = report([r for r in rows if r.get(key) == v], a.bins)
            sub.pop("courbe_fiabilite", None)
            full[dest][v] = sub
    if a.json:
        print(json.dumps(full, ensure_ascii=False, indent=2))
        return
    g = full["global"]
    print(f"Pronostics : {g['total']} (résolus {g['resolus']}, en attente {g['en_attente']})")
    if g["resolus"]:
        print(f"Brier {g['brier']} (IC95 {g['brier_ic95'][0]}–{g['brier_ic95'][1]}) | "
              f"log-loss {g['log_loss']} | ECE {g['ece']} "
              f"({'fiable' if g['ece_fiable'] else 'NON fiable : bins remplis ' + str(g['bins_remplis_pct']) + ' %'})")
        print(f"Réussite {g['taux_reussite']:.1%} vs proba moyenne {g['p_moyenne']:.1%}")
        if "roi_pct" in g:
            print(f"ROI {g['roi_pct']} % sur {g['mises_total']} misés")
        if "clv_moyen_50_derniers_pct" in g:
            print(f"CLV moyen (50 derniers) {g['clv_moyen_50_derniers_pct']} % — {g['clv_lecture']}")
        print("\nbin        n    p_moy  freq_obs  écart")
        for b in g["courbe_fiabilite"]:
            print(f"{b['bin']:<10}{b['n']:>4}  {b['p_moy']:.3f}  {b['freq_obs']:.3f}   {b['ecart']:+.3f}")
        if g.get("avertissement"):
            print("\n⚠ " + g["avertissement"])
    for title, key in (("Par discipline", "par_discipline"), ("Par marché", "par_marche")):
        if full[key]:
            print(f"\n{title} :")
            for k, s in full[key].items():
                if s["resolus"]:
                    print(f"  {k}: n={s['resolus']} Brier={s['brier']} ECE={s['ece']}"
                          + (f" ROI={s['roi_pct']}%" if s.get("roi_pct") is not None else ""))


if __name__ == "__main__":
    main()

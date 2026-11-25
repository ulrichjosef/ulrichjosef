#!/usr/bin/env python3
"""Client minimal (stdlib) pour l'API publique Open PMU.

Exemples :
  pmu.py --date 2026-10-31
  pmu.py --date 31/10/2026          (JJ/MM/AAAA par défaut)
  pmu.py --date 10/31/2026 --us     (MM/JJ/AAAA)
  pmu.py --hippo Chantilly --limit 20
  pmu.py --prix "PRIX DU PAYS DE BRAY" --json
  pmu.py --from 2026-10-01 --to 2026-10-07 --summary
"""
import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta

BASE = "https://open-pmu-api.vercel.app/api/arrivees"


def parse_date(s: str, us: bool = False) -> date:
    s = s.strip()
    if "-" in s:
        return datetime.strptime(s, "%Y-%m-%d").date()
    return datetime.strptime(s, "%m/%d/%Y" if us else "%d/%m/%Y").date()


def fetch(**params) -> dict:
    url = BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    req = urllib.request.Request(url, headers={"User-Agent": "open-pmu-skill/1.0", "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == 2:
                raise
        except urllib.error.URLError:
            if attempt == 2:
                raise
        time.sleep(2 ** attempt)
    return {}


def races(resp: dict) -> list:
    msg = resp.get("message")
    return msg if isinstance(msg, list) else []


def fmt_race(c: dict) -> str:
    st = c.get("statistiques") or {}
    g, f = st.get("gagnant") or {}, st.get("favori") or {}
    head = (f"{c.get('date')} {c.get('r/c', '?')} {c.get('lieu', '?')} {str(c.get('heure_depart') or '')[:5]} | "
            f"{c.get('prix', '?')} | {c.get('type', '?')} {c.get('distance', '?')}m | "
            f"{c.get('partants', '?')} partants | {c.get('montant', '?')} EUR")
    lines = [head, f"  Arrivée : {'-'.join(map(str, c.get('arrivee') or []))}"]
    if c.get("non_partants"):
        lines.append(f"  Non-partants : {c['non_partants']}")
    if g:
        lines.append(f"  Gagnant : n°{g.get('numero')} {g.get('nom_cheval')} (cote {g.get('cote')})")
    if f:
        lines.append(f"  Favori  : n°{f.get('numero')} {f.get('nom_cheval')} (cote {f.get('cote')}, arrivé {f.get('position') or 'non placé'})")
    det = c.get("arrivee_details") or {}
    for num in (c.get("arrivee") or [])[:5]:
        h = det.get(str(num))
        if h:
            lines.append(f"    {h.get('position', '?')}. n°{num} {h.get('nom_cheval')} - {h.get('nom_jockey') or '?'} / "
                         f"{h.get('nom_entraineur') or '?'}" + (f" - musique {h['musique']}" if h.get("musique") else ""))
    return "\n".join(lines)


def summary(all_races: list) -> str:
    n = len(all_races)
    if not n:
        return "Aucune course."
    fav_win = sum(1 for c in all_races if (c.get("statistiques") or {}).get("taux_favori_gagnant") == 100)
    fav_place = sum(1 for c in all_races if (c.get("statistiques") or {}).get("taux_favori_place") == 100)
    cotes = [g["cote"] for c in all_races if (g := (c.get("statistiques") or {}).get("gagnant")) and g.get("cote")]
    out = [f"Courses : {n}",
           f"Favori gagnant : {fav_win} ({100 * fav_win / n:.1f} %)",
           f"Favori placé (top 3) : {fav_place} ({100 * fav_place / n:.1f} %)"]
    if cotes:
        cotes.sort()
        out.append(f"Cote du gagnant : moyenne {sum(cotes) / len(cotes):.2f}, médiane {cotes[len(cotes) // 2]:.2f}")
    by_type = {}
    for c in all_races:
        by_type[c.get("type", "?")] = by_type.get(c.get("type", "?"), 0) + 1
    out.append("Par discipline : " + ", ".join(f"{k} {v}" for k, v in sorted(by_type.items(), key=lambda x: -x[1])))
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(description="Arrivées PMU via open-pmu-api.vercel.app")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="AAAA-MM-JJ ou JJ/MM/AAAA (MM/JJ/AAAA avec --us)")
    g.add_argument("--hippo", help="Nom de l'hippodrome")
    g.add_argument("--prix", help="Nom du prix")
    g.add_argument("--from", dest="start", help="Début de plage (avec --to)")
    p.add_argument("--to", dest="end", help="Fin de plage incluse")
    p.add_argument("--us", action="store_true", help="Dates saisies en MM/JJ/AAAA")
    p.add_argument("--json", action="store_true", help="Sortie JSON brute")
    p.add_argument("--summary", action="store_true", help="Statistiques agrégées")
    p.add_argument("--limit", type=int, default=0, help="Nombre max de courses affichées")
    p.add_argument("--sleep", type=float, default=0.5, help="Pause entre jours en mode plage")
    a = p.parse_args()

    try:
        if a.start:
            if not a.end:
                p.error("--from exige --to")
            d, end = parse_date(a.start, a.us), parse_date(a.end, a.us)
            all_races = []
            while d <= end:
                all_races += races(fetch(date=d.strftime("%m/%d/%Y")))
                d += timedelta(days=1)
                if d <= end:
                    time.sleep(a.sleep)
            resp = {"error": False, "total": len(all_races), "message": all_races}
        elif a.date:
            resp = fetch(date=parse_date(a.date, a.us).strftime("%m/%d/%Y"))
        elif a.hippo:
            resp = fetch(hippo=a.hippo)
        else:
            resp = fetch(prix=a.prix)
    except urllib.error.HTTPError as e:
        print(f"Erreur HTTP {e.code} : {e.reason}", file=sys.stderr)
        return 1
    except (urllib.error.URLError, OSError) as e:
        print(f"Erreur réseau : {e} (l'hôte open-pmu-api.vercel.app est-il autorisé ?)", file=sys.stderr)
        return 1

    lst = races(resp)
    if a.limit:
        lst = lst[: a.limit]
    if a.json:
        print(json.dumps({**resp, "message": lst if races(resp) else resp.get("message")}, ensure_ascii=False, indent=2))
        return 0
    if resp.get("error") or not lst:
        print(f"Aucun résultat : {resp.get('message')}")
        return 0
    print(f"{resp.get('total', len(lst))} course(s)\n")
    if not a.summary or not a.start:
        print("\n\n".join(fmt_race(c) for c in lst))
    if a.summary:
        print("\n" + summary(races(resp)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

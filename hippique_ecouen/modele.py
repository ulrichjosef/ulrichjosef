"""Modèle pré-enregistré — Prix du Prince d'Écouen (haies, handicap, Auteuil 3 900 m).

Écrit AVANT consultation de toute édition autre que 2015 et AVANT tout résultat.
Le classement est entièrement mécanique : aucune note discrétionnaire cheval par cheval.

Usage : python3 modele.py <fichier_annee_expurge.txt> <annee> <dossier_sortie>
"""
import re, sys, json, math, hashlib, datetime, os

POIDS_CRITERES = {  # pondération initiale du cahier des charges (/100)
    'forme': 25, 'aptitude': 20, 'valeur': 15, 'poids': 15,
    'fiabilite': 10, 'jockey': 10, 'cote': 5,
}
# Jockeys d'obstacle — réputation générale en France 2015-2025 (pas d'info course-spécifique).
JOCKEYS_A = ['nabet', 'reveley', 'beaurain', 'lestrade', 'de giles', 'charron', 'gallagher',
             'philipperon', 'plouganou', 'de chitray', 'lefebvre', 'gueguen']
JOCKEYS_B = ['duchêne', 'duchene', 'cottin', 'lecordier', 'carberry', 'regairaz', 'gelhay',
             'mescam', 'beaunez', 'masure', 'dehez', 'lemagnen', 'deniel', 'zuliani', 'lucas',
             'bourez', 'carroux', 'gagnon', 'meunier', 'merienne', 'chevillard', 'delage',
             'cheminaud', 'quinton', 'jouin', 'seguy', 'betron', 'nattiez', 'mosse']
NEUTRE = 0.5          # critère non documenté -> note neutre (jamais pénalisante)
TEMP = 8.0            # température softmax score -> probabilité de victoire
POS_NOTE = {1: 10, 2: 8, 3: 7, 4: 6, 5: 5, 6: 3, 7: 3, 8: 3, 9: 3, 0: 1}
DISC_POIDS = {'h': 1.0, 's': 0.8, 'p': 0.5, 'c': 0.5}


def num(x):
    x = x.replace('≈', '').replace(',', '.').strip()
    if re.fullmatch(r'[\d.]+\s*[–-]\s*[\d.]+', x):  # fourchette de cote -> milieu
        a, b = re.split(r'\s*[–-]\s*', x)
        return (float(a) + float(b)) / 2
    try:
        return float(x)
    except ValueError:
        return None


def parse_musique(m):
    """Musique française : la plus récente à gauche. Renvoie [(pos|lettre, disc, année)]."""
    if not m or m.strip() in ('–', '-', ''):
        return None
    m = m.replace(' ', '')
    out, annee = [], None
    for tok in re.finditer(r'\((\d{2})\)|([0-9]|[ATJDR])([hspc])', m):
        if tok.group(1):
            annee = tok.group(1); continue
        p, d = tok.group(2), tok.group(3)
        out.append((int(p) if p.isdigit() else p, d, annee))
    return out or None


def note_course(p):
    return POS_NOTE.get(p, 0) if isinstance(p, int) else 0


def lire(path):
    lignes = open(path).read().splitlines()
    hdr, rows, cond = None, [], {}
    for l in lignes:
        if l.startswith('N° |'):
            hdr = [c.strip() for c in l.split('|')]
        elif hdr and re.match(r'^\d+ \|', l):
            rows.append(dict(zip(hdr, [c.strip() for c in l.split('|')])))
        elif l.startswith('Année:'):
            cond = dict(kv.split(': ', 1) for kv in l.split(' | '))
    return rows, cond


def scorer(rows, cond):
    terrain = cond.get('Terrain (pénétromètre)', '').lower()
    lourd = any(k in terrain for k in ('lourd', 'très souple', 'collant'))
    k_poids = 0.6 if lourd else 0.4
    poids = [num(r.get('Poids (kg)', '')) for r in rows]
    pv = [p for p in poids if p is not None]
    pmin, pmax = min(pv), max(pv)
    cotes = [num(r.get('Cote PMU finale') or r.get('Cote PMU') or '') for r in rows]
    probs = [1 / c if c else None for c in cotes]
    s = sum(p for p in probs if p)
    probs = [p / s if p else None for p in probs]
    pmaxm = max(p for p in probs if p)
    vals = [num(r.get('Valeur', '') or '') for r in rows]
    vv = [v for v in vals if v is not None]
    out = []
    for i, r in enumerate(rows):
        doc = {}
        c = {}
        mus = parse_musique(r.get('Musique', ''))
        # Forme récente (5 dernières, pondération récence et discipline)
        if mus:
            last = mus[:5]
            w = [(0.8 ** j) * DISC_POIDS.get(d, 0.5) for j, (_, d, _) in enumerate(last)]
            c['forme'] = sum(wi * note_course(p) for wi, (p, _, _) in zip(w, last)) / sum(w) / 10
            doc['forme'] = 'documenté'
            hs = [note_course(p) for p, d, _ in mus[:8] if d == 'h']
            part_h = sum(1 for _, d, _ in mus[:8] if d == 'h') / len(mus[:8])
            c['aptitude'] = 0.5 * part_h + 0.5 * ((sum(hs) / len(hs) / 10) if hs else NEUTRE)
            doc['aptitude'] = 'partiel (haies oui ; Auteuil/distance/terrain non)'
            inc = sum(1 if p == 'T' else 0.7 if p in ('A', 'D', 'R') else 0.4 if p == 'J' else 0
                      for p, _, _ in mus[:8])
            c['fiabilite'] = max(0.0, 1 - inc / len(mus[:8]) * 2)
            doc['fiabilite'] = 'documenté'
        else:
            c['forme'] = c['aptitude'] = c['fiabilite'] = NEUTRE
            doc['forme'] = doc['aptitude'] = doc['fiabilite'] = 'inconnu'
        p = poids[i]
        x = (p - pmin) / (pmax - pmin) if (p is not None and pmax > pmin) else 0.5
        if vals[i] is not None and len(vv) > 1 and max(vv) > min(vv):
            c['valeur'] = (vals[i] - min(vv)) / (max(vv) - min(vv)); doc['valeur'] = 'documenté (valeur officielle)'
        else:
            c['valeur'] = x; doc['valeur'] = 'partiel (proxy : poids de handicap)'
        c['poids'] = 1 - k_poids * x; doc['poids'] = 'documenté'
        jk = r.get('Jockey', '').lower()
        c['jockey'] = 1.0 if any(n in jk for n in JOCKEYS_A) else 0.7 if any(n in jk for n in JOCKEYS_B) else NEUTRE
        doc['jockey'] = 'partiel (jockey seul, entraîneur ' + ('connu' if r.get('Entraîneur') else 'masqué/inconnu') + ')'
        if probs[i]:
            c['cote'] = probs[i] / pmaxm; doc['cote'] = 'documenté'
        else:
            c['cote'] = NEUTRE; doc['cote'] = 'inconnu'
        sc = {k: round(POIDS_CRITERES[k] * v, 2) for k, v in c.items()}
        A = round(sum(sc.values()), 2)
        mkt = 100 * c['cote']
        B = 0.7 * A + 0.3 * mkt - (5 * (1 - c['fiabilite']) if doc['fiabilite'] == 'documenté' else 0)
        out.append(dict(num=int(r['N°']), cheval=r['Cheval'], jockey=r.get('Jockey', ''),
                        poids=p, valeur=vals[i], cote=cotes[i], prob_marche=probs[i],
                        musique=r.get('Musique', ''), scores=sc, documentation=doc,
                        score_A=A, score_B=round(B, 2)))
    z = [math.exp(o['score_B'] / TEMP) for o in out]
    for o, zi in zip(out, z):
        o['prob_victoire'] = round(zi / sum(z), 4)
    for key, rk in (('score_A', 'rang_A'), ('score_B', 'rang_prevu')):
        for j, o in enumerate(sorted(out, key=lambda o: -o[key])):
            o[rk] = j + 1
    # Références simples
    for key, rk, rev in (('prob_marche', 'rang_ref_cote', True), ('poids', 'rang_ref_valeur', True)):
        srt = sorted(out, key=lambda o: (-(o[key] or 0)) if rev else (o[key] or 0))
        for j, o in enumerate(srt): o[rk] = j + 1
    fo = sorted(out, key=lambda o: -(o['scores']['forme'] + (0 if o['documentation']['forme'] != 'inconnu' else -100)))
    for j, o in enumerate(fo): o['rang_ref_forme'] = j + 1 if o['documentation']['forme'] != 'inconnu' else None
    n_doc = sum(1 for v in out[0]['documentation'].values() if v == 'documenté')
    for o in out:
        ecart = sorted([x['score_B'] for x in out], reverse=True)
        top_gap = ecart[0] - ecart[min(4, len(ecart) - 1)]
        nd = sum(1 for v in o['documentation'].values() if v.startswith('documenté'))
        o['confiance'] = 'moyenne' if (nd >= 5 and o['rang_prevu'] <= 3 and top_gap > 8) else 'faible' if nd < 4 else 'moyenne-faible'
        fort = max(o['scores'], key=lambda k: o['scores'][k] / POIDS_CRITERES[k])
        faible = min(o['scores'], key=lambda k: o['scores'][k] / POIDS_CRITERES[k])
        o['justification'] = (f"Point fort : {fort} ; point faible : {faible} ; cote {o['cote']} ; "
                              f"{o['poids']} kg ; critères inconnus : "
                              + (', '.join(k for k, v in o['documentation'].items() if v == 'inconnu') or 'aucun'))
    return out


if __name__ == '__main__':
    path, annee, dossier = sys.argv[1], sys.argv[2], sys.argv[3]
    rows, cond = lire(path)
    res = scorer(rows, cond)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    blob = dict(course=f'ECOUEN-{annee}', annee=annee, conditions=cond, horodatage=now,
                source_sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(),
                modele_sha256=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
                partants=sorted(res, key=lambda o: o['rang_prevu']))
    os.makedirs(dossier, exist_ok=True)
    f = os.path.join(dossier, f'prediction_{annee}.json')
    if os.path.exists(f):
        sys.exit(f'REFUS : {f} existe déjà (prédiction verrouillée, non modifiable).')
    json.dump(blob, open(f, 'w'), ensure_ascii=False, indent=1)
    os.chmod(f, 0o444)
    for o in blob['partants']:
        print(o['rang_prevu'], o['num'], o['cheval'], o['score_A'], o['score_B'], o['prob_victoire'])

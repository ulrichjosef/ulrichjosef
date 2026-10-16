"""Étape C — évaluation des prédictions verrouillées contre les arrivées officielles.
Ne modifie jamais les fichiers de predictions_verrouillees/ (lecture seule)."""
import json, csv, math, glob, os, statistics as st

R = {k: v for k, v in json.load(open('resultats/arrivees_officielles.json')).items() if not k.startswith('_')}
PERIODE = {**{y: 'entrainement' for y in ('2015', '2016', '2017', '2018')},
           **{y: 'validation' for y in ('2019', '2020', '2021', '2022')},
           **{y: 'test' for y in ('2023', '2024', '2025')}}
# Années à données propres (pas de fuite par sélection/données manquantes ; musiques fiables ou neutralisées)
PROPRES = {'2015', '2016', '2017', '2021', '2025'}
FUITES = {'2018': 'liste incomplète contenant les 5 placés (sélection liée au résultat)',
          '2019': 'chevaux sans cote/poids tous non placés',
          '2020': 'chevaux sans cote/poids tous non placés (8/15 sans cote)',
          '2022': 'chevaux sans cote/poids tous non placés',
          '2023': 'datation des musiques incertaine (variante sans musique fournie)',
          '2024': 'musiques contenant des courses postérieures (variante sans musique = référence)'}

preds = {}
for f in sorted(glob.glob('predictions_verrouillees/prediction_*.json')):
    b = json.load(open(f)); preds[b['annee']] = b
PREDS_EVAL = {a: b for a, b in preds.items() if a.split('_')[0] in R}  # 2026 : pas encore de résultat

def rangs(b, methode):
    P = b['partants']
    if methode == 'combine_B': key = lambda p: p['rang_prevu']
    elif methode == 'performance_A': key = lambda p: p['rang_A']
    elif methode == 'ref_favori_cote': key = lambda p: p['rang_ref_cote']
    elif methode == 'ref_valeur_poids': key = lambda p: p['rang_ref_valeur']
    elif methode == 'ref_forme':
        if any(p['rang_ref_forme'] is None for p in P): return None
        key = lambda p: p['rang_ref_forme']
    elif methode.startswith('melange_'):
        lam = float(methode.split('_')[1])
        sc = {p['num']: (1 - lam) * p['score_A'] + lam * 100 * (p['scores']['cote'] / 5) for p in P}
        o = sorted(P, key=lambda p: -sc[p['num']]); return {p['num']: i + 1 for i, p in enumerate(o)}
    return {p['num']: key(p) for p in P}

def metriques(rk, arr, n, probs=None):
    w = arr[0]; top5 = arr[:5]
    pred = sorted(rk, key=rk.get)
    m = dict(gagnant_1er=int(rk.get(w) == 1), gagnant_top3=int(rk.get(w, 99) <= 3),
             gagnant_top5=int(rk.get(w, 99) <= 5),
             top3_reel_dans_top3=len(set(arr[:3]) & set(pred[:3])) / 3,
             top5_reel_dans_top5=len(set(top5) & set(pred[:5])) / 5,
             top5_reel_dans_top8=len(set(top5) & set(pred[:8])) / 5,
             rang_moyen_norm_top5=st.mean((rk[x] - 1) / (n - 1) for x in top5 if x in rk))
    if probs:
        pw = max(probs.get(w, 0), 1e-4)
        m['logloss_gagnant'] = -math.log(pw)
        m['brier'] = sum((probs.get(k, 0) - (k == w)) ** 2 for k in rk)
    return m

# ---- Fichier 1 : predictions_aveugles.csv
with open('predictions_aveugles.csv', 'w', newline='') as fh:
    W = csv.writer(fh)
    W.writerow(['id_course', 'variante', 'date', 'num', 'cheval', 'jockey', 'poids_kg', 'valeur', 'cote_pre_course',
                'musique', 'sc_forme', 'sc_aptitude', 'sc_valeur', 'sc_poids', 'sc_fiabilite', 'sc_jockey',
                'sc_cote', 'score_A', 'score_total_B', 'rang_A', 'rang_prevu', 'prob_victoire', 'confiance',
                'criteres_documentation', 'justification', 'horodatage_enregistrement'])
    for a, b in preds.items():
        an = a.split('_')[0]; var = 'sans_musique' if 'sans' in a else 'complete'
        for p in b['partants']:
            s = p['scores']
            W.writerow([f'ECOUEN-{an}', var, b['conditions'].get('Date', ''), p['num'], p['cheval'], p['jockey'], p['poids'],
                        p['valeur'], p['cote'], p['musique'], s['forme'], s['aptitude'], s['valeur'], s['poids'],
                        s['fiabilite'], s['jockey'], s['cote'], p['score_A'], p['score_B'], p['rang_A'],
                        p['rang_prevu'], p['prob_victoire'], p['confiance'],
                        '; '.join(f'{k}={v}' for k, v in p['documentation'].items()), p['justification'],
                        b['horodatage']])

# ---- Fichier 2 : evaluation_predictions.csv
with open('evaluation_predictions.csv', 'w', newline='') as fh:
    W = csv.writer(fh)
    W.writerow(['id_course', 'variante', 'periode', 'qualite_donnees', 'num', 'cheval', 'rang_prevu_initial',
                'rang_reel_officiel', 'gagnant_reel', 'statut_officiel', 'ecart_rang', 'dans_top5_prevu',
                'place_reel_top5', 'prob_victoire', 'outsider_identifie', 'favori_fragile_identifie'])
    for a, b in PREDS_EVAL.items():
        an = a.split('_')[0]; arr = R[an]['arrivee']; inc = R[an]['incidents']
        var = 'sans_musique' if 'sans' in a else 'complete'
        for p in b['partants']:
            reel = arr.index(p['num']) + 1 if p['num'] in arr else None
            statut = inc.get(str(p['num']), 'Classé' if reel else f'Non classé dans les {len(arr)} premiers (rang exact inconnu)')
            outsider = p['rang_prevu'] <= 5 and p['rang_ref_cote'] > 5
            fragile = p['rang_ref_cote'] == 1 and p['rang_prevu'] > 3
            W.writerow([f'ECOUEN-{an}', var, PERIODE[an], 'propre' if an in PROPRES else 'fuite: ' + FUITES[an],
                        p['num'], p['cheval'], p['rang_prevu'], reel or '', int(reel == 1), statut,
                        (p['rang_prevu'] - reel) if reel else '', int(p['rang_prevu'] <= 5),
                        int(bool(reel and reel <= 5)), p['prob_victoire'], int(outsider), int(fragile)])

# ---- Fichier 3 : synthese_modeles.csv
METHODES = ['combine_B', 'performance_A', 'ref_favori_cote', 'ref_valeur_poids', 'ref_forme',
            'melange_0.0', 'melange_0.3', 'melange_0.5', 'melange_0.7', 'melange_1.0']
def jeu(a):  # variante retenue par année : sans musique pour 2024 (musiques contaminées)
    return a + '_sans_musique' if a == '2024' else a
lignes = []
for perim_nom, annees in (('toutes_annees', sorted(R)), ('annees_propres', sorted(PROPRES)),
                          ('entrainement', [a for a in sorted(R) if PERIODE[a] == 'entrainement']),
                          ('validation', [a for a in sorted(R) if PERIODE[a] == 'validation']),
                          ('test', [a for a in sorted(R) if PERIODE[a] == 'test']),
                          ('test_sans_musique', None)):
    for meth in METHODES:
        ms = []
        for a in (annees or ['2023', '2024', '2025']):
            b = preds[a + '_sans_musique'] if annees is None else preds[jeu(a)]
            rk = rangs(b, meth)
            if rk is None: continue
            probs = None
            if meth == 'combine_B': probs = {p['num']: p['prob_victoire'] for p in b['partants']}
            if meth == 'ref_favori_cote': probs = {p['num']: p['prob_marche'] or 0 for p in b['partants']}
            ms.append(metriques(rk, R[a]['arrivee'], len(b['partants']), probs))
        if not ms: continue
        agg = {k: round(st.mean(m[k] for m in ms), 3) for k in ms[0]}
        lignes.append(dict(perimetre=perim_nom, methode=meth, n_courses=len(ms), **agg))
# v2 rétrospective (post-hoc, mêmes données : résultat fragile, non verrouillé avant les arrivées)
preds2 = {}
for f in sorted(glob.glob('predictions_retrospectives_v2/prediction_*.json')):
    b = json.load(open(f)); preds2[b['annee'].replace('_v2', '').replace('_sans_musique', '')] = b
for perim_nom, annees in (('toutes_annees', sorted(R)), ('annees_propres', sorted(PROPRES)),
                          ('test', [a for a in sorted(R) if PERIODE[a] == 'test'])):
    ms = [metriques(rangs(preds2[a], 'combine_B'), R[a]['arrivee'], len(preds2[a]['partants']),
                    {p['num']: p['prob_victoire'] for p in preds2[a]['partants']}) for a in annees]
    agg = {k: round(st.mean(m[k] for m in ms), 3) for k in ms[0]}
    lignes.append(dict(perimetre=perim_nom, methode='combine_B_v2_retrospectif', n_courses=len(ms), **agg))
# Référence hasard (espérance analytique)
for perim_nom, annees in (('toutes_annees', sorted(R)), ('annees_propres', sorted(PROPRES))):
    ns = [len(preds[jeu(a)]['partants']) for a in annees]
    lignes.append(dict(perimetre=perim_nom, methode='ref_hasard (espérance)', n_courses=len(ns),
                       gagnant_1er=round(st.mean(1 / n for n in ns), 3), gagnant_top3=round(st.mean(3 / n for n in ns), 3),
                       gagnant_top5=round(st.mean(5 / n for n in ns), 3), top3_reel_dans_top3=round(st.mean(3 / n for n in ns), 3),
                       top5_reel_dans_top5=round(st.mean(5 / n for n in ns), 3), top5_reel_dans_top8=round(st.mean(8 / n for n in ns), 3),
                       rang_moyen_norm_top5=0.5, logloss_gagnant=round(st.mean(math.log(n) for n in ns), 3)))
cols = ['perimetre', 'methode', 'n_courses', 'gagnant_1er', 'gagnant_top3', 'gagnant_top5', 'top3_reel_dans_top3',
        'top5_reel_dans_top5', 'top5_reel_dans_top8', 'rang_moyen_norm_top5', 'logloss_gagnant', 'brier']
with open('synthese_modeles.csv', 'w', newline='') as fh:
    W = csv.DictWriter(fh, fieldnames=cols + ['ponderations']); W.writeheader()
    pond = {'combine_B': 'B = 0,7·A + 0,3·100·p/pmax − 5·(1−fiab) ; A = forme25 apt20 val15 poids15 fiab10 jockey10 cote5',
            'performance_A': 'A seul (pondération initiale)', 'ref_favori_cote': 'cote PMU seule',
            'ref_valeur_poids': 'poids/valeur décroissants',
            'combine_B_v2_retrospectif': 'B v2 : cote manquante = part de la masse restante (livre 118 %), T=12 — POST-HOC', 'ref_forme': 'score forme musique seul (2023-2025)'}
    for l in lignes:
        l['ponderations'] = pond.get(l['methode'], 'mélange (1−λ)·A + λ·marché' if 'melange' in l['methode'] else 'aucune')
        W.writerow({k: l.get(k, '') for k in cols + ['ponderations']})

# Détail par course pour le rapport
det = {}
for a in sorted(R):
    b = preds[jeu(a)]; arr = R[a]['arrivee']
    det[a] = {m: metriques(rangs(b, m), arr, len(b['partants'])) for m in ('combine_B', 'ref_favori_cote')}
    det[a]['rang_prevu_gagnant'] = rangs(b, 'combine_B').get(arr[0])
    det[a]['rang_cote_gagnant'] = rangs(b, 'ref_favori_cote').get(arr[0])
    det[a]['cote_gagnant'] = next((p['cote'] for p in b['partants'] if p['num'] == arr[0]), None)
    det[a]['top5_prevu'] = [p['num'] for p in sorted(b['partants'], key=lambda p: p['rang_prevu'])[:5]]
    det[a]['arrivee'] = arr[:5]
    det[a]['outsiders'] = [(p['num'], arr.index(p['num']) + 1 if p['num'] in arr else None) for p in b['partants'] if p['rang_prevu'] <= 5 and p['rang_ref_cote'] > 5]
    det[a]['fragiles'] = [(p['num'], arr.index(p['num']) + 1 if p['num'] in arr else None) for p in b['partants'] if p['rang_ref_cote'] == 1 and p['rang_prevu'] > 3]
json.dump(det, open('resultats/detail_par_course.json', 'w'), indent=1, default=str)
for l in lignes:
    if l['perimetre'] in ('toutes_annees', 'annees_propres', 'test', 'test_sans_musique'):
        print({k: l.get(k) for k in cols})

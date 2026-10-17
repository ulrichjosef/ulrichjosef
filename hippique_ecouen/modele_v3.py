"""v3 — raisonnement corrigé après comparaison avec l'arrivée officielle (fichier « Après course »).
Pour l'année Y, l'historique de la course n'utilise QUE les éditions < Y (pas de fuite)."""
import json, re
A = json.load(open('resultats/arrivees_completes.json'))
# Palmarès (fichier après course) : gagnant -> (jockey, entraîneur)
GAGNANTS = {'2015': ('Schmidlin', 'Cottin'), '2016': ('Beaunez', 'Butel'), '2017': ('Bureller', 'Rudolf'),
            '2018': ('de Giles', 'Carberry'), '2019': ('Mescam', 'Cottin'), '2020': ('Regairaz', 'Bertran de Balanda'),
            '2021': ('Philipperon', 'Collet'), '2022': ('Lefebvre', 'Collet'), '2023': ('Lefebvre', 'Collet'),
            '2024': ('Meunier', 'Fouin'), '2025': ('Lefebvre', 'Delaunay')}
def nom(c): return re.sub(r'\s*\(.*?\)', '', c).strip().lower()
def score(p, y, poids_min, poids_max):
    s = 0.0
    c = p['cote']
    s += 100 * (1 / c if c else 1 / 30)                       # 1. marché = base (cote inconnue ~ 30/1)
    if c and c > 23: s -= 15                                   # 2. au-delà de 23/1 : jamais gagné, 40 % non classés
    x = (p['poids'] - poids_min) / (poids_max - poids_min) if p['poids'] and poids_max > poids_min else 0.5
    s += 4 * (1 - x)                                           # 3. poids : léger légèrement favorisé (plus de double comptage)
    passe = [a for a in A if a < y]                            # 4. historique de la course (éditions antérieures seulement)
    for a in passe:
        for r in A[a]['lignes']:
            if nom(r['cheval']) == nom(p['cheval']) and r['rang'].isdigit() and int(r['rang']) <= 5:
                s += 4
    entourage = (p['jockey'] + ' ' + str(p.get('entraineur', ''))).lower()
    if any(j.lower() in entourage or t.lower() in entourage for a in passe for j, t in [GAGNANTS[a]]):
        s += 3                                                 # 5. jockey/entraîneur déjà gagnant de la course
    if p['documentation']['fiabilite'] == 'documenté':
        s -= 8 * (1 - p['scores']['fiabilite'] / 10)          # 6. chutes/arrêts récents
    return s
def classer(y, partants, entraineurs=None):
    pv = [p['poids'] for p in partants if p['poids']]
    for p in partants:
        p['entraineur'] = (entraineurs or {}).get(p['num'], '')
        p['score_v3'] = score(p, y, min(pv), max(pv))
    return sorted(partants, key=lambda p: -p['score_v3'])

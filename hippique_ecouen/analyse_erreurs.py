"""Analyse post-course : pourquoi les prédictions verrouillées diffèrent des arrivées complètes."""
import json, statistics as st, math
A = json.load(open('resultats/arrivees_completes.json'))
def pred(y):
    v = y + '_sans_musique' if y == '2024' else y
    return json.load(open(f'predictions_verrouillees/prediction_{v}.json'))
def num(x):
    x = x.replace('≈', '').replace(',', '.').strip()
    if '–' in x and x != '–':
        a, b = x.split('–'); return (float(a) + float(b)) / 2
    try: return float(x)
    except: return None
def spearman(a, b):
    n = len(a)
    ra = {v: i for i, v in enumerate(sorted(range(n), key=lambda i: a[i]))}
    rb = {v: i for i, v in enumerate(sorted(range(n), key=lambda i: b[i]))}
    return 1 - 6 * sum((ra[i] - rb[i]) ** 2 for i in range(n)) / (n * (n * n - 1))
rows = []
for y in sorted(A):
    P = {p['num']: p for p in pred(y)['partants']}
    for r in A[y]['lignes']:
        p = P.get(r['num'])
        if not p: continue
        rows.append(dict(y=y, n=len(P), num=r['num'], cheval=r['cheval'], rang=r['rang'],
                         fini=r['rang'].isdigit(), rr=int(r['rang']) if r['rang'].isdigit() else None,
                         rp=p['rang_prevu'], ra=p['rang_A'], rc=p['rang_ref_cote'],
                         poids=num(r['poids']) or p['poids'], cote_post=num(r['cote']), cote_pre=p['cote'],
                         sc=p['scores'], jk=p['jockey']))
print('=== 1. Corrélation de rang (Spearman) sur chevaux classés, par course')
for y in sorted(A):
    R = [r for r in rows if r['y'] == y and r['fini']]
    if len(R) < 5: continue
    s_b = spearman([r['rp'] for r in R], [r['rr'] for r in R])
    s_c = spearman([r['rc'] for r in R], [r['rr'] for r in R])
    s_w = spearman([-(r['poids'] or 0) for r in R], [r['rr'] for r in R])
    print(y, f'n_classés={len(R):2d}  modèle={s_b:+.2f}  cote={s_c:+.2f}  poids lourd->devant={s_w:+.2f}')
print('\n=== 2. Non-classés (AR/T) : où le modèle les plaçait')
nc = [r for r in rows if not r['fini']]
print('non-classés:', len(nc), '/', len(rows), f'({len(nc)/len(rows):.0%})')
print('dont dans le Top 5 prévu :', sum(r['rp'] <= 5 for r in nc), ' | dans le Top 5 de la cote :', sum(r['rc'] <= 5 for r in nc))
for r in nc:
    if r['rp'] <= 5: print('   ', r['y'], r['num'], r['cheval'], 'prévu', r['rp'], 'cote rang', r['rc'], r['rang'])
print('\n=== 3. Taux Top 5 réel par tranche de poids (dans la course)')
def tranche(r):
    P = sorted([x['poids'] for x in rows if x['y'] == r['y'] and x['poids']], reverse=True)
    if not r['poids']: return None
    q = P.index(r['poids']) / len(P)
    return 'haut (1er tiers)' if q < 1/3 else 'milieu' if q < 2/3 else 'bas (dernier tiers)'
from collections import defaultdict
T = defaultdict(lambda: [0, 0, 0, 0])
for r in rows:
    t = tranche(r)
    if not t: continue
    T[t][0] += 1; T[t][1] += bool(r['rr'] and r['rr'] <= 5); T[t][2] += r['rp'] <= 5; T[t][3] += r['rr'] == 1
for t, (n, top5, pt5, w) in T.items():
    print(f'  {t:20s} partants={n:3d}  Top5 réel={top5/n:.0%}  gagnants={w}  | part mise par le modèle dans son Top5={pt5/n:.0%}')
print('\n=== 4. Taux par rang de cote (cote pré-course)')
B = defaultdict(lambda: [0, 0, 0, 0])
for r in rows:
    k = '1 (favori)' if r['rc'] == 1 else '2-3' if r['rc'] <= 3 else '4-6' if r['rc'] <= 6 else '7-10' if r['rc'] <= 10 else '11+'
    B[k][0] += 1; B[k][1] += r['rr'] == 1; B[k][2] += bool(r['rr'] and r['rr'] <= 5); B[k][3] += not r['fini']
for k in ['1 (favori)', '2-3', '4-6', '7-10', '11+']:
    n, w, t5, ncl = B[k]; print(f'  {k:11s} n={n:3d}  victoire={w/n:.0%}  Top5={t5/n:.0%}  non-classé={ncl/n:.0%}')
print('\n=== 5. Gagnants : rang prévu, et critère qui les a le plus pénalisés vs la moyenne du champ')
for y in sorted(A):
    R = [r for r in rows if r['y'] == y]
    w = next(r for r in R if r['rr'] == 1)
    moy = {k: st.mean(x['sc'][k] for x in R) for k in w['sc']}
    d = {k: round(w['sc'][k] - moy[k], 1) for k in w['sc']}
    pire = min(d, key=d.get)
    print(f"  {y} {w['cheval'][:20]:20s} prévu {w['rp']:2d}/{w['n']}  cote rang {w['rc']:2d}  {w['poids']} kg  écart critères vs champ: {d}  -> plus pénalisant: {pire}")
print('\n=== 6. Top 5 prévus : ce qu\'ils sont devenus')
F = defaultdict(int)
for r in rows:
    if r['rp'] <= 5:
        F['gagnant' if r['rr'] == 1 else 'placé 2-5' if r['rr'] and r['rr'] <= 5 else '6e et +' if r['rr'] else 'non classé (AR/T)'] += 1
print(' ', dict(F))
print('\n=== 7. Écart cote pré-course (fichier avant) vs cote finale (fichier après)')
for r in rows:
    if r['cote_pre'] and r['cote_post'] and abs(r['cote_pre'] - r['cote_post']) / r['cote_post'] > 0.25:
        print('  ', r['y'], r['num'], r['cheval'], 'avant', r['cote_pre'], 'après', r['cote_post'], '| rang réel', r['rang'])

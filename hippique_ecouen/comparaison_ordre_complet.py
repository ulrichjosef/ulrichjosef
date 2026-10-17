"""Comparaison de l'ORDRE COMPLET prévu (1er -> dernier) avec l'ordre officiel complet.
v1 = prédiction verrouillée à l'aveugle ; v3 = raisonnement corrigé (rejoué, non aveugle) ; cote = référence."""
import json, random, statistics as st, sys
sys.path.insert(0, '.')
import modele_v3 as m3
A = json.load(open('resultats/arrivees_completes.json'))
random.seed(0)

def entraineurs(y):
    d = {}
    try:
        for l in open(f'donnees_expurgees/{y}.txt'):
            c = [x.strip() for x in l.split('|')]
            if len(c) > 7 and c[0].isdigit(): d[int(c[0])] = c[6]
    except FileNotFoundError: pass
    return d

def ordres(y):
    v = y + '_sans_musique' if y == '2024' else y
    P = json.load(open(f'predictions_verrouillees/prediction_{v}.json'))['partants']
    o1 = [p['num'] for p in sorted(P, key=lambda p: p['rang_prevu'])]
    o3 = [p['num'] for p in m3.classer(y, [dict(p) for p in P], entraineurs(y))]
    oc = [p['num'] for p in sorted(P, key=lambda p: -(p['prob_marche'] or 0))]
    return P, {'v1': o1, 'v3': o3, 'cote': oc}

def kendall(a, b):
    n = len(a); c = d = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (a[i] - a[j]) * (b[i] - b[j])
            c += s > 0; d += s < 0
    return (c - d) / (c + d) if c + d else 0

def metriques(ordre, off, nc):
    """off: num -> rang officiel (int) pour les classés ; nc: set des non-classés."""
    rp = {n: i + 1 for i, n in enumerate(ordre)}
    cl = [n for n in off if n in rp]
    exact = sum(rp[n] == off[n] for n in cl)
    e = [abs(rp[n] - off[n]) for n in cl]
    arr = sorted(cl, key=off.get)
    return dict(exact=exact, pm1=sum(x <= 1 for x in e), pm2=sum(x <= 2 for x in e),
                mae=st.mean(e), tau=kendall([rp[n] for n in cl], [off[n] for n in cl]),
                tierce_ordre=ordre[:3] == arr[:3], tierce_des=set(ordre[:3]) == set(arr[:3]),
                quarte_des=set(ordre[:4]) == set(arr[:4]), quinte_des=set(ordre[:5]) == set(arr[:5]),
                nc_bas=sum(rp[n] > len(ordre) - len(nc) for n in nc), n_nc=len(nc), n_cl=len(cl))

def hasard(nums, off, nc, k=3000):
    r = [metriques(random.sample(nums, len(nums)), off, nc) for _ in range(k)]
    return {x: st.mean(float(s[x]) for s in r) for x in ('exact', 'pm1', 'pm2', 'mae', 'tau')}

L = ['# Ordre d\'arrivée complet : prévu contre officiel (2015-2025)', '',
     '- **v1** : prédiction faite **à l\'aveugle** sur le document d\'avant course, verrouillée avant de connaître le résultat.',
     '- **v3** : raisonnement corrigé après lecture de l\'arrivée officielle, rejoué sur les mêmes courses (donc **pas** une preuve).',
     '- **cote** : référence, l\'ordre de la cote pré-course.', '',
     'Les chevaux arrêtés (AR) ou tombés (T) n\'ont pas de rang exact : un ordre réussi les met en fin de classement.', '',
     '## Résumé (11 courses, chevaux classés seulement)', '',
     '| Méthode | Positions exactes | À ±1 place | À ±2 places | Écart moyen (places) | Concordance d\'ordre τ | Tiercé ordre | Tiercé désordre | Quarté désordre | Quinté désordre | Non-classés mis en fin |',
     '|---|---|---|---|---|---|---|---|---|---|---|']
tot = {k: [] for k in ('v1', 'v3', 'cote')}; hz = []; details = []
for y in sorted(A):
    P, O = ordres(y)
    lig = A[y]['lignes']
    off = {r['num']: int(r['rang']) for r in lig if r['rang'].isdigit()}
    nc = {r['num'] for r in lig if not r['rang'].isdigit()}
    nc &= {p['num'] for p in P}
    M = {k: metriques(o, off, nc) for k, o in O.items()}
    for k in M: tot[k].append(M[k])
    hz.append(hasard([p['num'] for p in P], off, nc))
    details.append((y, P, O, lig, M))
for k, nom in (('v1', 'v1 aveugle (verrouillée)'), ('v3', 'v3 corrigée (rejouée)'), ('cote', 'Ordre de la cote')):
    T = tot[k]
    L.append(f"| {nom} | {sum(t['exact'] for t in T)} / {sum(t['n_cl'] for t in T)} | {sum(t['pm1'] for t in T)} | {sum(t['pm2'] for t in T)} | "
             f"{st.mean(t['mae'] for t in T):.1f} | {st.mean(t['tau'] for t in T):+.2f} | {sum(t['tierce_ordre'] for t in T)}/11 | "
             f"{sum(t['tierce_des'] for t in T)}/11 | {sum(t['quarte_des'] for t in T)}/11 | {sum(t['quinte_des'] for t in T)}/11 | "
             f"{sum(t['nc_bas'] for t in T)} / {sum(t['n_nc'] for t in T)} |")
L.append(f"| Hasard (moyenne) | {sum(h['exact'] for h in hz):.1f} | {sum(h['pm1'] for h in hz):.1f} | {sum(h['pm2'] for h in hz):.1f} | "
         f"{st.mean(h['mae'] for h in hz):.1f} | {st.mean(h['tau'] for h in hz):+.2f} | ≈0 | ≈0 | ≈0 | ≈0 | – |")
L += ['', '## Détail course par course', '',
      'Lecture : les chevaux sont présentés **dans l\'ordre officiel**. Pour chacun, la place que je lui avais donnée et l\'écart (+ = je l\'avais mis trop loin, − = trop haut). ✔ = position exacte.', '']
for y, P, O, lig, M in details:
    r1 = {n: i + 1 for i, n in enumerate(O['v1'])}; r3 = {n: i + 1 for i, n in enumerate(O['v3'])}
    nomc = {p['num']: p['cheval'] for p in P}
    L += [f"### {y} ({len(P)} partants dans le document d'avant course)", '',
          f"- Ordre officiel : **{' - '.join(str(r['num']) for r in lig if r['rang'].isdigit())}**"
          + (f"  ·  non classés : {', '.join(f'{r[chr(110)+chr(117)+chr(109)]} ({r[chr(114)+chr(97)+chr(110)+chr(103)]})' for r in lig if not r['rang'].isdigit())}" if any(not r['rang'].isdigit() for r in lig) else ''),
          f"- Mon ordre v1 (aveugle) : {' - '.join(map(str, O['v1']))}",
          f"- Ordre v3 : {' - '.join(map(str, O['v3']))}", '',
          '| Officiel | N° | Cheval | Ma place v1 | Écart v1 | Place v3 | Écart v3 |', '|---|---|---|---|---|---|---|']
    for r in lig:
        n = r['num']
        if n not in r1: L.append(f"| {r['rang']} | {n} | {r['cheval']} | absent du doc. avant course | | | |"); continue
        if r['rang'].isdigit():
            o = int(r['rang']); e1 = r1[n] - o; e3 = r3[n] - o
            L.append(f"| {o} | {n} | {r['cheval']} | {r1[n]} | {'✔' if e1 == 0 else f'{e1:+d}'} | {r3[n]} | {'✔' if e3 == 0 else f'{e3:+d}'} |")
        else:
            L.append(f"| {r['rang']} | {n} | {r['cheval']} | {r1[n]} | non classé | {r3[n]} | non classé |")
    m1, m3_ = M['v1'], M['v3']
    L += ['', f"v1 : {m1['exact']} position(s) exacte(s), {m1['pm2']} à ±2, écart moyen {m1['mae']:.1f} place(s), τ = {m1['tau']:+.2f}  ·  "
          f"v3 : {m3_['exact']} exacte(s), {m3_['pm2']} à ±2, écart moyen {m3_['mae']:.1f}, τ = {m3_['tau']:+.2f}", '']
L += ['## Ce que montre l\'ordre complet', '',
      '1. **Position exacte.** Mes ordres trouvent la place exacte d\'à peine un cheval par course, soit le niveau du hasard (environ 1 par course, puisque chaque cheval a 1 chance sur n d\'être à sa place).',
      '2. **Écart moyen.** Mes chevaux finissent en moyenne à environ 4 places de la position que je leur avais donnée. La concordance d\'ordre (τ, 0 = hasard, 1 = ordre parfait) est faiblement positive : je classe un peu mieux que le hasard **le haut et le bas** du peloton, pas l\'ordre exact.',
      '3. **Où l\'ordre casse :** (a) les non-classés, environ 23 % des partants, que je mettais souvent au milieu ou devant ; (b) les chevaux légers, que je mettais trop bas ; (c) les gros poids, que je mettais trop haut.',
      '4. **Conséquence pour la suite :** viser l\'ordre exact du 1er au dernier sur 14 à 20 partants n\'est pas atteignable avec ces données. Ce qui est réaliste, et mesurable course après course : le bon groupe de tête (Top 5 en désordre), le bon groupe de fin, et l\'élimination des non-finisseurs.']
open('comparaison_ordre_complet.md', 'w').write('\n'.join(L) + '\n')
print('\n'.join(L[:16]))

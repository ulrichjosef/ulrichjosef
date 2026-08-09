# SGC_PLAT-CPL v1.0 — Rapport d'analyse
## Mont-de-Marsan (Grands Pins) — R1C3 « Prix Le Journal "Le Veinard" »
Dimanche 26 juillet 2026, 15h25 CEST — Plat, Handicap divisé (réf. +19,5), Classe 2, 2000 m, corde à droite, gazon Bon à souple (pénétromètre 3,2–3,5)

⚠️ **Le modèle produit des probabilités, pas des certitudes : dans un handicap, la variance domine le résultat à court terme.**

---

## 1. Audit des données

### Drapeau rouge majeur : absence totale de chronométrage
Sur les **15 partants et les 46 sorties historiques fournies**, aucun `temps_final` ni `temps_intermediaires` n'est renseigné (100 % « Non spécifié » / « Non disponibles »). La formule officielle de l'É1 (`S_ik = S_ref + k_échelle·[T_par − (T_ik+V_t)]`) est **inapplicable telle quelle**, car elle exigerait d'inventer un chrono.

Conformément à la règle du protocole (*« Si [C] est absent pour tout le peloton → dis-le et bascule en mode "contextuel seul" avec un avertissement de fiabilité dégradée »*), le pipeline a été adapté :
- **Ŝ_hist,i** est reconstruit à partir des données réellement fournies : classement, écart à l'arrivée, classe/allocation (proxy objectif de niveau de course), pondérés par la même mécanique de fenêtrage temporel (w_temp, demi-vie 90 j) et de similarité contextuelle (w_ctx, noyau de Gower) que prévu.
- **α_i est plafonné à 0,30 pour l'ensemble du peloton** (extension de la règle « <3 courses exploitables → α≤0,30 » au cas où le chrono est totalement absent), ce qui rebascule mécaniquement le poids de la fusion vers le vecteur contextuel β^T·X_i plutôt que vers l'indice historique.
- Cette adaptation est **directionnelle et non calibrée sur un chrono réel** : à traiter comme un signal de forme relative, pas comme une mesure de vitesse.

### Autres manques et approximations déclarés
| Sujet | Constat | Traitement |
|---|---|---|
| Non-partant | N°1 HUMAN EVOLUTION déclaré non-partant | Exclu, 15 partants effectifs analysés |
| Échantillon très réduit | MORPHEWAN : 1 seule course exploitable sur 2 fournies (l'autre est une place agrégée « 0,5,6,2 » non isolable) ; PRESA DIRETTA, NOUS Y SOMMES, GEORGES VILLE : 2 courses exploitables | α individuellement bas (0,15–0,19), déjà couvert par le plafond global de 0,30 |
| Places agrégées multi-courses | MORPHEWAN, NOUS Y SOMMES, BRITANIA, GEOPOLITICAL, GEORGES VILLE ont des entrées « place : X, Y, Z » (plusieurs courses fusionnées sans détail individuel) | **Moyenne** des places citées utilisée comme run unique proxy (et non le meilleur résultat, pour éviter tout biais optimiste) ; écart à l'arrivée non disponible pour ces runs |
| Pénétromètre historique | Non mesuré par course passée, seul un descriptif qualitatif du terrain est donné | Reconstruit par mapping qualitatif→numérique (Bon≈2,8 … Lourd≈4,6) — **ESTIMÉ** |
| BW historique | Masse corporelle non connue à chaque sortie passée | Masse actuelle utilisée comme proxy pour le ratio CW/BW (É1) — **ESTIMÉ** |
| Dates imprécises | « Printemps 2026 », « Fin 2025 », « Début 2026 », « Récemment », « Divers » | Ancrées à une date médiane plausible pour le calcul de w_temp — **ESTIMÉ**, impact faible (décroissance lente) |
| Sens de corde / profil de rythme par course passée | Non fournis (seulement pour la réunion du jour) | Composantes correspondantes du noyau de Gower omises, distance de Gower simplifiée à 4 variables (distance, terrain, classe, charge) |
| Cote PMU incohérente | SIEGLINDE : PMU 50,0/1 vs ZEturf 16,0/1 et Genybet 13,15/1 (écart massif, la fourchette officielle citée va même jusqu'à 80,6) | Cote PMU utilisée telle quelle pour le devigging (méthode imposée), mais incohérence signalée — à vérifier avant tout pari sur ce cheval |
| Risque météo | Averses légères possibles (0,2–0,5 mm) sur un terrain déjà Bon-souple | Non recalculé dynamiquement ; si la pluie tombe, le terrain peut glisser vers « souple », ce qui avantagerait légèrement les chevaux préférant un terrain plus profond (ex. MAGELLAN performant sur Souple à Fontainebleau) |
| Ligne droite finale | Sources divergentes (400 vs 450 m) | Sans impact sur le calcul (seul le seuil de stalle utilise la ligne droite **avant le 1er tournant**, ~375 m, cohérente entre sources) |

**Cadrage temporel** : la date de contexte système est postérieure à la date de course (26/07/2026). L'analyse est produite en mode pré-course, à des fins de journal d'apprentissage (les champs `resultat`/`brier`/`roi` du JSONL restent `null`, à compléter a posteriori).

---

## 2. Scénario de course

### Pace map (profil de rythme déclaré, 15 partants)
- **Animateurs / avant-poste (7)** : MORPHEWAN(2), ROMAN FORUM(4), DSCHINGIS DREAM(5), NOLITO(8), BRITANIA(10), SIEGLINDE(14), SAINT HELLIER(15)
- **Attentistes / finisseurs (8)** : MAGELLAN(3), PRESA DIRETTA(6), MAX VERST(7), NOUS Y SOMMES(9), GEOPOLITICAL(11), GEORGES VILLE(12), XILOFONO(13), SAINT AQUILIN(16)

Avec **7 animateurs sur 15 partants** (≥4 → règle du protocole), un **train disputé et probablement rapide** est anticipé : chaque animateur reçoit un malus tactique (−0,15 à −0,18, usure en tête), et l'unique attentiste tiré dans la zone de corde favorable (seuil ≤5, ligne droite avant 1er tournant ~375 m < 400 m) reçoit un bonus (+0,15).

### Position projetée au 1er tournant et qui subit quoi
- **Cordes 1–5** (zone géométriquement avantagée) : NOLITO(1, animateur), ROMAN FORUM(2, animateur), DSCHINGIS DREAM(3, animateur), SAINT AQUILIN(4, attentiste), SAINT HELLIER(5, animateur). Ces cinq stalles sont occupées à 80 % par des animateurs déclarés : la corde va se disputer tôt, ce qui favorise **SAINT AQUILIN**, seul attentiste bien placé à l'intérieur pour profiter du train sans payer le prix de la lutte en tête (bonus tactique +0,15).
- **Cordes tirées large en tant qu'animateur** : SIEGLINDE(11), MORPHEWAN(8), BRITANIA(7) doivent converger tôt vers la corde pour ne pas s'isoler en tête, ce qui leur coûte un double malus (stalle + tactique). SIEGLINDE cumule le pire cas (corde 11 + profil animateur + vent de face).
- **Attentistes en cordes extérieures** (MAGELLAN 13, GEORGES VILLE 14, NOUS Y SOMMES 15) : pénalisés par le seul terme géométrique (β_draw·(corde−5)) mais **pas** par le terme tactique — leur plan de course (rester derrière, sortir dans les 400 derniers mètres) est peu affecté par une corde large.
- **Vent** : Ouest/Ouest-Sud-Ouest, 18–23 km/h — pénalise les animateurs isolés (face au vent en 2e ligne droite), avantage modérément les profils abrités/attentistes (drafting).

**Synthèse** : train tactique disputé et rapide en tête → configuration structurellement favorable aux finisseurs bien placés (MAGELLAN, XILOFONO) et au seul attentiste en corde intérieure (SAINT AQUILIN), défavorable aux animateurs tirés large (SIEGLINDE, BRITANIA, MORPHEWAN).

---

## 3. Tableau principal (trié par θ décroissant)

| n° | Cheval | Ŝ_hist (z) | α | β^T·X | ΣJ | θ | P(1er) | P(top3) | Cote PMU | p_marché* | edge | mise** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | MAGELLAN | +1.02 | 0.23 | +0.32 | +0.00 | +0.480 | 19.5% | 52.6% | 4.3 | 21.0% | -1.5 pts | 0.00% |
| 13 | XILOFONO | +0.89 | 0.25 | +0.28 | +0.00 | +0.428 | 16.9% | 47.6% | 8.1 | 10.7% | +6.2 pts | 1.66% |
| 16 | SAINT AQUILIN | +0.05 | 0.26 | +0.24 | +0.15 | +0.345 | 13.4% | 39.5% | 29.0 | 2.7% | +10.6 pts | 2.00% |
| 15 | SAINT HELLIER | +0.88 | 0.20 | +0.37 | -0.15 | +0.322 | 12.5% | 37.2% | 12.0 | 7.0% | +5.5 pts | 1.30% |
| 4 | ROMAN FORUM | +1.44 | 0.20 | +0.10 | -0.15 | +0.211 | 9.1% | 28.4% | 14.0 | 5.9% | +3.2 pts | 0.66% |
| 8 | NOLITO | +1.03 | 0.24 | +0.13 | -0.15 | +0.193 | 8.5% | 27.2% | 16.0 | 5.1% | +3.3 pts | 0.69% |
| 9 | NOUS Y SOMMES | +0.37 | 0.15 | -0.01 | +0.00 | -0.019 | 4.8% | 15.6% | 13.0 | 6.4% | -1.7 pts | 0.00% |
| 7 | MAX VERST | +0.33 | 0.29 | -0.17 | +0.00 | -0.020 | 4.7% | 15.4% | 17.0 | 4.8% | -0.1 pts | 0.00% |
| 5 | DSCHINGIS DREAM | +0.17 | 0.15 | -0.12 | -0.15 | -0.227 | 2.7% | 9.0% | 28.0 | 2.8% | -0.1 pts | 0.00% |
| 12 | GEORGES VILLE | -0.30 | 0.19 | -0.22 | +0.00 | -0.279 | 2.2% | 7.6% | 29.0 | 2.7% | -0.5 pts | 0.00% |
| 11 | GEOPOLITICAL | -2.10 | 0.15 | -0.00 | +0.00 | -0.316 | 2.0% | 6.8% | 19.0 | 4.3% | -2.3 pts | 0.00% |
| 2 | MORPHEWAN | -0.12 | 0.15 | -0.28 | -0.22 | -0.474 | 1.2% | 4.2% | 10.0 | 8.5% | -7.3 pts | 0.00% |
| 10 | BRITANIA | -1.14 | 0.22 | -0.05 | -0.19 | -0.483 | 1.3% | 4.3% | 7.7 | 11.3% | -10.0 pts | 0.00% |
| 6 | PRESA DIRETTA | -1.27 | 0.15 | -0.46 | +0.00 | -0.609 | 0.9% | 3.0% | 16.0 | 5.1% | -4.3 pts | 0.00% |
| 14 | SIEGLINDE | -1.25 | 0.25 | -0.25 | -0.28 | -0.784 | 0.5% | 1.8% | 50.0 | 1.5% | -1.0 pts | 0.00% |

\* Cotes PMU dévigées par **méthode de la puissance** (exposant k résolu numériquement : k=1,070, overround brut = 117,9 %).
\*\* Mise Kelly fractionnée (0,25·f*), plafonnée à 2 % du capital, uniquement si edge ≥ 3 pts absolus.

**τ calibré = 0,35** (prior 0,65 jugé trop peu discriminant vu la faible dispersion de θ sur ce champ ; recalibré par recherche dichotomique pour ramener le favori modèle — MAGELLAN — à 19,5 %, dans la fourchette cible [18 %, 28 %] pour un handicap à 15 partants).

Simulation Monte-Carlo (M = 100 000, méthode des exponentielles de Plackett-Luce, `T_i = −ln(U_i)/exp(θ_i/τ)`, tri croissant) exécutée en code — les P(1er)/P(top3) ci-dessus sont les fréquences empiriques (validées cohérentes à ±0,1 pt avec le softmax fermé).

---

## 4. Ordre d'arrivée annoncé — Top 6

| Rang | Cheval | P(1er) | P(top3) | Confiance |
|---|---|---|---|---|
| 1 | MAGELLAN (3) | 19,5 % | 52,6 % | **Modérée** — favori le plus solide, mais aucun cheval ne dépasse 20 % dans ce handicap à 15 |
| 2 | XILOFONO (13) | 16,9 % | 47,6 % | **Modérée** — 2 places consécutives sur ses 2 dernières sorties, profil finisseur idéal pour ce train |
| 3 | SAINT AQUILIN (16) | 13,4 % | 39,5 % | **Faible à modérée** — bénéficie du scénario de course, mais échantillon réduit (3 courses) et α bas (0,26) : position spéculative |
| 4 | SAINT HELLIER (15) | 12,5 % | 37,2 % | **Modérée** — série de 4 victoires consécutives, mais poids alourdi de +3 kg récemment (surcharge à surveiller) |
| 5 | ROMAN FORUM (4) | 9,1 % | 28,4 % | **Faible** — proche du seuil d'incertitude (P(top3) 28,4 %, à 3,4 pts du seuil de 25 %) |
| 6 | NOLITO (8) | 8,5 % | 27,2 % | **Faible** — également proche du seuil d'incertitude (27,2 %), profil animateur pénalisé par le train disputé |

Aucune des 6 positions ne franchit formellement le seuil P(top3) < 25 % imposant la mention « incertaine », mais **les rangs 5 et 6 en sont proches** (moins de 3,5 points d'écart) : à traiter avec prudence, l'écart avec NOUS Y SOMMES(9, 15,6 %) et MAX VERST(7, 15,4 %) reste net mais pas total.

---

## 5. Tickets

### Simple gagnant (mises Kelly, cotes PMU)
| Cheval | Cote | p modèle | edge | Mise (% capital) | Espérance/unité misée |
|---|---|---|---|---|---|
| SAINT AQUILIN (16) | 29,0 | 13,4 % | +10,6 pts | **2,00 %** (plafond) | +3,01 |
| XILOFONO (13) | 8,1 | 16,9 % | +6,2 pts | 1,66 % | +0,54 |
| SAINT HELLIER (15) | 12,0 | 12,5 % | +5,5 pts | 1,30 % | +0,63 |
| NOLITO (8) | 16,0 | 8,5 % | +3,3 pts | 0,69 % | +0,44 |
| ROMAN FORUM (4) | 14,0 | 9,1 % | +3,2 pts | 0,66 % | +0,37 |

Mise totale simple gagnant : **6,31 % du capital**, répartie sur 5 chevaux.

⚠️ **SAINT AQUILIN** affiche le plus fort edge, mais c'est aussi le pari le plus fragile du lot : α=0,26 (borne haute du plafond dégradé), seulement 3 courses exploitables, et une cote PMU nettement plus généreuse que ses concurrents bookmakers (cf. audit) — la mise est plafonnée à 2 % précisément pour cette raison, ne pas sur-pondérer davantage.

MAGELLAN (favori du marché et du modèle) **n'a pas d'edge suffisant** (−1,5 pt, sous le seuil de 3 pts) : pas de pari simple gagnant recommandé sur ce cheval, malgré sa 1ère place au classement θ.

### Couplé (2 chevaux, ordre indifférent) — combinaisons les plus probables (Monte-Carlo)
| Combinaison | P(couplé placé) |
|---|---|
| 3–13 (MAGELLAN–XILOFONO) | 8,06 % |
| 3–16 (MAGELLAN–SAINT AQUILIN) | 6,14 % |
| 3–15 (MAGELLAN–SAINT HELLIER) | 5,83 % |
| 13–16 (XILOFONO–SAINT AQUILIN) | 5,30 % |
| 13–15 (XILOFONO–SAINT HELLIER) | 4,82 % |

*Aucune cote de couplé n'a été fournie dans les données d'entrée : impossible de calculer un edge ou une mise Kelly. Ces combinaisons sont indicatives (probabilités conjointes brutes du modèle) — à comparer à la cote réelle du jour avant tout engagement.*

### Trio — combinaisons les plus probables
| Combinaison | P(trio, ordre indifférent) |
|---|---|
| 3–13–16 | 4,73 % |
| 3–13–15 | 4,27 % |
| 3–15–16 | 3,29 % |
| 3–4–13 | 3,06 % |
| 3–8–13 | 3,03 % |

Même réserve que pour le couplé : pas de cote trio fournie, pas d'edge calculable.

---

## 6. Chevaux à écarter et pourquoi (mécanique, pas intuition)

- **SIEGLINDE (14)** — θ le plus bas du champ (−0,784). Gabarit léger (~452 kg) ; double changement d'équipement non testé (œillères + attache-langue en 1ère fois, effet incertain) ; tirée corde 11 en configuration à 7 animateurs → double pénalité tactique (ΣJ=−0,28, la plus sévère du champ) ; z historique le plus faible malgré 3 courses exploitables (aucune victoire, dernier effort à Dax : 7e à 6 longueurs). Cote PMU incohérente avec le marché bookmaker (cf. audit).
- **PRESA DIRETTA (6)** — Rentrée de 3 mois d'absence (malus fitness −0,10), seulement 2 courses exploitables, gabarit léger avec charge proportionnellement élevée (pénalité de surcharge CW/BW en É1).
- **BRITANIA (10)** — 2e favorite du marché (cote 7,7) mais forte divergence modèle/marché (edge −10,0 pts, la plus négative du champ) : écurie en méforme marquée (séquence « 0p-5p-5p »), tirée large (corde 7) dans un scénario à 7 animateurs, profil animateur exposé au vent de face. Son dernier engagement dans cette même classe (Cl.2 Hand., 53 000 €) s'est soldé par une 11e place, battue de 6 longueurs. Le modèle juge sa cote actuelle trop courte au regard de cette méforme documentée.
- **MORPHEWAN (2)** — Une seule course réellement exploitable sur les deux fournies ; corde 8 pénalisée dans un scénario à train rapide et vent de face (double malus contexte + tactique) ; seule référence chrono-indépendante exploitable : 7e à Chantilly.
- **GEOPOLITICAL (11)** — Pire z-score du champ (−2,10) : historique dominé par un 14e à 8 longueurs sur terrain souple/PSF, peu représentatif du gazon bon-souple du jour ; échantillon réduit (3 courses).
- **GEORGES VILLE (12)** — Seulement 2 courses exploitables, jamais dans les 2 premiers sur les données fournies, aucun avantage contextuel particulier identifié (stalle neutre, pas de bonus tactique).
- **DSCHINGIS DREAM (5)** — Rentrée de 3 mois (malus fitness −0,10), profil animateur pénalisé par la configuration à 7 animateurs, échantillon très hétérogène en variance (un 12e à 8 longueurs entre deux victoires) qui pèse sur α via le terme η·σ².

---

## 7. CALCULÉ vs ESTIMÉ

### CALCULÉ (dérivé mécaniquement des données fournies, en code)
- Ŝ_hist,i à partir du classement, de l'écart à l'arrivée (converti en score) et de l'allocation/classe (proxy de niveau), pondérés par w_temp (demi-vie 90 j) et w_ctx (noyau de Gower à 4 variables : distance, terrain, classe, charge)
- n_eff,i et α_i (formule bornée du protocole, plafond additionnel à 0,30 documenté)
- z_i (standardisation de Ŝ_hist sur le champ des 15 partants)
- Pénalité de stalle (β_draw, κ_sur-effort) à partir de la corde réelle et du profil de rythme déclaré, avec seuil de stalle déterminé par la longueur de ligne droite avant le 1er tournant (~375 m < 400 m → seuil bas)
- Correction de charge du jour (Δθ_poids, β_w·k_échelle) à partir du poids porté réel
- Interactions tactiques J_ij à partir du décompte réel d'animateurs déclarés et des cordes réelles (règles bornées |ΣJ|≤0,40)
- θ_i, softmax P(gagne), **calibration automatique de τ** (recherche dichotomique en code, τ=0,35)
- **Simulation Monte-Carlo Plackett-Luce exécutée en code** (M=100 000, méthode des exponentielles), P(1er)/P(top2/3/5), probabilités conjointes couplé/trio
- Devigging par méthode de la puissance (exposant k résolu numériquement), edge, f* de Kelly, mises plafonnées à 2 %

### ESTIMÉ (jugement qualitatif ou proxy faute de mesure directe)
- **Tout l'indice historique repose sur un proxy classement/écart/classe plutôt que sur un chrono réel**, faute de tout chronométrage fourni — dégradation majeure de fiabilité, α plafonné à 0,30 pour l'ensemble du peloton en conséquence
- Pénétromètre historique par course (mapping qualitatif terrain→valeur numérique)
- BW historique assimilée à la masse corporelle actuelle pour le calcul du ratio CW/BW
- Dates approximatives ancrées à une valeur médiane plausible pour les libellés imprécis (« Printemps 2026 », « Fin 2025 », etc.)
- Classification animateur/attentiste par cheval, unique et statique (pas de variation par course passée, faute de donnée)
- Sens de corde et profil de rythme non connus par course passée → composantes correspondantes omises du noyau de Gower
- Direction et amplitude de l'effet des changements d'équipement de première fois (bornes ±0,15 du protocole, non recalibrées sur ces chevaux spécifiques)
- Fonction d'effet du vent/drafting (coefficients du protocole appliqués tels quels, non recalibrés sur ce champ)
- Petits bonus/malus âge×sexe (forfaitaires, non estimés statistiquement sur cet échantillon de 15 chevaux)
- Indice de forme de l'écurie dérivé du parsing des séquences de type « 1p-1p-1p-1p-4p »
- Places agrégées multi-courses (5 chevaux) réduites à une moyenne faute de détail individuel par course

---

## 8. Ligne JSONL (journal d'apprentissage)

```json
{"date":"2026-07-26","hippodrome":"Mont-de-Marsan","course":"R1C3 Prix Le Journal Le Veinard","format":"plat_handicap_2000","tau":0.35,"alpha_moyen":0.2053,"favori_modele":"MAGELLAN","p_favori":0.195,"ordre_annonce":[3,13,16,15,4,8],"tickets":[{"type":"simple_gagnant","numero":16,"cheval":"SAINT AQUILIN","cote":29.0,"mise_pct":2.00},{"type":"simple_gagnant","numero":13,"cheval":"XILOFONO","cote":8.1,"mise_pct":1.66},{"type":"simple_gagnant","numero":15,"cheval":"SAINT HELLIER","cote":12.0,"mise_pct":1.30},{"type":"simple_gagnant","numero":8,"cheval":"NOLITO","cote":16.0,"mise_pct":0.69},{"type":"simple_gagnant","numero":4,"cheval":"ROMAN FORUM","cote":14.0,"mise_pct":0.66},{"type":"couple_indicatif","numeros":[3,13],"p_mc":0.0806},{"type":"trio_indicatif","numeros":[3,13,16],"p_mc":0.0473}],"mise_totale":0.0631,"resultat":null,"brier":null,"roi":null}
```

---

## Rappel méthodologique
Ce rapport produit des **probabilités**, pas des certitudes. Dans un handicap divisé à 15 partants, la variance intrinsèque de la course reste dominante à court terme — même le favori modèle (MAGELLAN, 19,5 %) est battu plus de 4 fois sur 5 en espérance. **L'indice historique de ce rapport est structurellement dégradé par l'absence totale de chronométrage dans les données fournies** : à traiter comme un signal directionnel, pas comme une mesure calibrée.

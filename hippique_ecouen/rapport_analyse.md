# Prix du Prince d'Écouen : analyse à l'aveugle 2015-2025 et pronostic 2026

*Rapport produit le 16/10/2026, la veille de la course cible (Auteuil R1C3, 17/10/2026, 15 h 15).*

---

## 1. Ce qu'il faut retenir

1. **La méthode n'apporte pas de gain mesurable sur le marché.** Sur 11 éditions, le modèle combiné trouve le gagnant en 1re position une fois (9 %), soit autant que le favori PMU. Il place le gagnant dans son Top 3 trois fois (27 %), soit autant que la cote. Il retrouve 46 % des chevaux du Top 5 réel dans son Top 5, contre 51 % pour la cote seule. Ses probabilités sont moins bien calibrées que celles du marché (log-loss 2,97 contre 2,42 ; hasard 2,73).
2. **La course est très ouverte.** Le favori n'a gagné qu'**1 fois sur 11** (2016). Le gagnant était en général entre le 2e et le 10e de la cote (rang médian 5, cote médiane 10,7/1). Le hasard pur mettrait le gagnant dans son Top 3 environ 20 % du temps ; le modèle et la cote y arrivent environ 27 % du temps. C'est un écart faible, et l'échantillon est trop petit pour qu'il soit significatif.
3. **Le fichier source contenait trois fuites indirectes**, détectées puis neutralisées ou signalées (§ 3). Six éditions sur onze ne sont donc pas totalement « propres ».
4. **2026 : classement provisoire, confiance faible.** La distance passe à 4 300 m, 20 partants sont annoncés, et ni les musiques, ni le terrain, ni les cotes complètes n'étaient accessibles (§ 8).

---

## 2. Méthode et garanties d'aveugle

| Étape | Ce qui a été fait | Preuve |
|---|---|---|
| A. Préparation | Lecture de la *structure* du .docx seulement (titres, en-têtes, mots-clés comptés sans affichage), puis expurgation par script : entraîneur supprimé pour 2015-2022 et table « Habitués » exclue. | `donnees_expurgees/`, outil de masquage |
| Pré-enregistrement | Le modèle complet (pondérations, liste de jockeys, lecture des musiques) a été écrit **après avoir vu 2015 seulement**. Le classement est **100 % mécanique** : aucune note n'est donnée à la main cheval par cheval. | `modele.py`, commit `b6b02b6` |
| B. Prédiction | Les années ont été ouvertes **dans l'ordre chronologique**. Chaque prédiction est écrite en JSON horodaté, en lecture seule, avec l'empreinte SHA-256 de la source et du modèle. Le script refuse d'écraser un fichier existant. Il y a eu un commit git par année, puis un push vers GitHub avant toute recherche de résultat. | `predictions_verrouillees/`, commits `b6b02b6` → `2025` |
| C. Vérification | Les arrivées officielles ont été recherchées **après** le push des 11 prédictions. | `resultats/arrivees_officielles.json` |

**Limite à déclarer honnêtement.** En tant que modèle de langage, j'ai pu voir certains de ces résultats pendant mon entraînement, et je ne peux pas l'exclure. C'est justement pour cela que le classement est entièrement calculé par le script : ma mémoire ne peut pas intervenir dans les rangs. Les justifications sont générées à partir des scores.

**Modifications du modèle en cours de route** (toutes tracées dans git) :
- **Avant 2023 :** lecture des fourchettes de cote (« ≈ 5,5–7 » donne le milieu). Aucune fourchette n'existait en 2015-2022, donc les années déjà verrouillées ne sont pas touchées.
- **2023 et 2024 :** ajout d'une variante « sans musique » (§ 3).
- **2026 :** ajout d'une **v2**, décidée après l'évaluation et avant la course (§ 7).

### Notation (pondération initiale du cahier des charges, /100)

| Critère | Poids | Mesure utilisée | Documentation |
|---|---|---|---|
| Forme récente | 25 | 5 dernières courses de la musique, pondérées par la récence (×0,8 par course) et par la discipline (haies 1, steeple 0,8, plat 0,5) | 2023-2025 seulement |
| Aptitude | 20 | part des haies dans la musique et niveau moyen en haies | partielle : Auteuil, distance et terrain non disponibles |
| Valeur sportive | 15 | valeur officielle ; à défaut, poids du handicap | valeur en 2023-2025, poids avant |
| Poids / handicap | 15 | pénalité linéaire du poids, plus forte sur terrain lourd (0,6) que sinon (0,4) | partout |
| Fiabilité | 10 | taux de chutes, arrêts et non-classements sur 8 courses | 2023-2025 |
| Jockey | 10 | 3 niveaux selon la réputation générale en obstacle (A = 10, B = 7, autres = 5) | partout ; entraîneur masqué |
| Cote | 5 | probabilité implicite rapportée au favori | partout sauf trous |

Un critère inconnu reçoit une **note neutre (0,5)** et n'est jamais pénalisé. Le **Classement A** est la somme des critères. Le **Classement B** (ordre d'arrivée prévu) vaut 0,7·A + 0,3·(marché), moins une pénalité de fiabilité. La probabilité de victoire est un softmax de B, avec T = 8 en v1.

---

## 3. Limites des données et fuites détectées

| Problème | Années | Nature | Traitement |
|---|---|---|---|
| Entraîneur indiqué « pour les 5 premiers » | 2015-2022 | **Fuite directe** : la présence de l'entraîneur désigne les placés (vérifié par un test booléen sans lecture). | Entraîneur **supprimé par script** avant toute lecture. |
| Liste incomplète (11/17) contenant les 5 placés | 2018 | Fuite par sélection : la liste a été bâtie à partir de l'arrivée. | Année exclue du périmètre « propre ». |
| Chevaux sans cote ni poids **tous non placés** | 2019, 2020 (8/15 sans cote), 2022 | Fuite par sélection : les données manquent pour les chevaux non placés. | Exclues du périmètre « propre ». |
| Musiques 2024 contenant des courses **postérieures** (ex. « Jh (24) 1s… ») | 2024 | Fuite post-course probable. | Variante **sans musique** retenue pour l'évaluation. |
| Datation des musiques incertaine (Chichi de la Vega a le même préfixe en 2023 et en 2024) | 2023 | Doute. | Variante sans musique verrouillée aussi ; année hors périmètre propre. |
| Musiques, valeurs et terrain détaillé absents | 2015-2022 | Données manquantes. | Critères neutres ; confiance « faible ». |
| Arrivées au-delà de la 5e place rarement disponibles | toutes | L'évaluation ne porte que sur le Top 5. | Les métriques se limitent au Top 5. |

**Périmètre « propre » : 2015, 2016, 2017, 2021, 2025 (5 courses).**

---

## 4. Résultats du test à l'aveugle

### 4.1 Synthèse (extrait de `synthese_modeles.csv`)

| Périmètre | Méthode | n | Gagnant 1er | Gagnant Top 3 | Gagnant Top 5 | Top 3 réel / Top 3 prévu | Top 5 réel / Top 5 prévu | Top 5 réel / Top 8 prévu | Rang normalisé moyen du Top 5 (0 = parfait) | Log-loss gagnant |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 années | **Combiné B (v1)** | 11 | 9 % | 27 % | 55 % | 42 % | 46 % | 64 % | 0,415 | 2,97 |
| 11 années | Favori / cote seule | 11 | 9 % | 27 % | 55 % | 42 % | **51 %** | **73 %** | **0,356** | **2,42** |
| 11 années | Performance A seule | 11 | **18 %** | 18 % | 36 % | 24 % | 42 % | 58 % | 0,459 | – |
| 11 années | Valeur / poids seul | 11 | 18 % | 18 % | 18 % | 24 % | 27 % | 44 % | 0,518 | – |
| 11 années | Combiné B v2 (*post-hoc*) | 11 | 9 % | 27 % | 55 % | 42 % | 51 % | 65 % | 0,385 | 2,67 |
| 11 années | Hasard (espérance) | 11 | 7 % | 20 % | 33 % | 20 % | 33 % | 52 % | 0,500 | 2,73 |
| Années propres | **Combiné B (v1)** | 5 | 20 % | 20 % | 60 % | 40 % | 52 % | 68 % | 0,339 | 2,50 |
| Années propres | Cote seule | 5 | 20 % | 20 % | **80 %** | 40 % | 52 % | **76 %** | **0,329** | **2,32** |
| Test 2023-25 | Combiné B (v1) | 3 | 0 % | 0 % | 67 % | 22 % | 47 % | 73 % | 0,431 | 2,99 |
| Test 2023-25 | Cote seule | 3 | 0 % | 0 % | 33 % | 22 % | 40 % | 73 % | 0,427 | 2,46 |
| Test 2023-25 | Forme seule (musique) | 1 | – | – | – | – | 20 % | 40 % | 0,492 | – |

Lecture :
- Le modèle combiné **suit la cote** mais fait légèrement moins bien qu'elle. Le seul critère autonome qui dépasse le hasard est la cote.
- La **forme seule** n'est évaluable que sur 2025 (la seule année où les musiques sont fiables) : n = 1, donc aucune conclusion.
- Le **mélange A / marché** (λ de 0 à 1) a été balayé. Le meilleur λ dépend de la période : 0,7-1,0 sur les années propres, 0-0,3 sur le test. **Aucun réglage stable.** Avec 4 courses d'entraînement, tout réglage serait du sur-ajustement, donc aucune pondération « optimisée » n'est retenue.

### 4.2 Détail par course (variante retenue)

| Année | Arrivée (Top 5) | Top 5 prévu | Rang prévu du gagnant | Rang à la cote du gagnant (cote) | Qualité des données |
|---|---|---|---|---|---|
| 2015 | 17-1-14-10-12 | 14-2-10-11-8 | 8 | 5 (10,7) | propre |
| 2016 | 1-5-3-15-11 | **1**-8-11-7-**5** | **1** | 1 (5,1) | propre |
| 2017 | 10-3-1-12-11 | 3-1-16-8-13 | 6 | 5 (10,2) | propre |
| 2018 | 16-13-7-18-2 | 7-16-17-9-2 | 2 | 3 (9,1) | fuite (liste) |
| 2019 | 7-12-6-8-15 | 4-8-2-10-11 | 12 | 10 (18,9) | fuite (manquants) |
| 2020 | 16-10-14-15-9 | 4-16-10-6-8 | 2 | 2 (6,5) | fuite (manquants) |
| 2021 | 15-12-13-3-14 | 13-5-12-9-15 | 5 | 6 (11,0) | propre |
| 2022 | 12-11-14-16-3 | 1-11-14-13-6 | 14 | 9 (22,3) | fuite (manquants) |
| 2023 | 16-10-1-13-14 | 6-1-8-7-10 | 8 | 7 (11,8) | doute (musiques) |
| 2024 | 1-6-15-7-9 | 6-11-14-1-13 (sans musique) | 4 | 6 (12,0) | fuite (musiques) |
| 2025 | 7-1-13-3-14 | 4-2-3-7-1 | 4 | 4 (7,1) | propre |

### 4.3 Outsiders et favoris fragiles identifiés

Règles mécaniques : un **outsider** est un cheval du Top 5 prévu classé au-delà du 5e rang à la cote. Un **favori fragile** est le favori de la cote classé au-delà du 3e rang par le modèle.

- **Outsiders** : 11 signalés. Trois ont terminé dans les 5 premiers : 2016 n° 5 Rouge et Sage (**2e**), 2021 n° 15 Foreign Flower (**1er**, cote 11), 2024 n° 1 Mamix's Passion (**1er**, cote 12). Six des huit autres étaient des chevaux **sans cote**, remontés artificiellement par la note neutre (défaut corrigé en v2).
- **Favoris fragiles** : aucun signalé sur 11 courses. Le modèle ne contredit jamais le marché sur le favori, alors que celui-ci a perdu 10 fois sur 11. C'est une faiblesse.

### 4.4 Calibration

Les probabilités v1 (softmax T = 8) sont **trop confiantes** : log-loss 2,97, pire que le hasard (2,73). La v2 (T = 12, imputation de marché) descend à 2,67 *a posteriori*. Le marché seul reste le mieux calibré (2,42).

---

## 5. Erreurs récurrentes

1. **Les favoris sur-évalués.** Le favori a gagné 1 fois sur 11, mais il s'est classé dans les 5 premiers 7 fois sur 11. Dans ce handicap, il s'agit plutôt d'un cheval à jouer **placé**.
2. **La note neutre attribuée aux données manquantes**, en particulier à la cote, fait remonter des chevaux sans information au-dessus de chevaux connus et cotés longtemps (2019, 2020, 2022, 2026 v1).
3. **La mauvaise forme récente est pénalisée à tort.** En 2023, le gagnant Chichi de la Vega avait la musique la plus faible du lot (8h 8h 0h 0h 0h Jh), avec le poids le plus bas (66,5 kg). Un cheval qui recule au handicap après une série médiocre peut redevenir compétitif. Le critère « forme » de 25 points ne capte pas ce mécanisme. C'est une hypothèse explicative, sur un seul cas.
4. **Le poids n'a pas de sens univoque.** Le top weight a gagné 2 fois (2016, 2024), un cheval du bas de l'échelle 3 fois (2015, 2021, 2023). Aucun effet net n'est démontré.

## 6. Critères réellement utiles (avec prudence, n ≤ 11)

- **Cote pré-course** : seul critère au-dessus du hasard de façon cohérente, surtout pour le Top 8 (73 % contre 52 %).
- **Jockey** : non isolable, car il est confondu avec la cote.
- **Forme, aptitude, fiabilité** : **non testables** faute de musiques fiables (une seule année propre).
- **Poids et valeur seuls** : pas mieux que le hasard pour l'ordre (27 % du Top 5 contre 33 % pour le hasard).

## 7. Améliorations proposées

| Proposition | Statut |
|---|---|
| Imputer une cote manquante à partir de la masse de probabilité restante (livre ≈ 118 %) plutôt que par une note neutre | **appliquée en v2** pour 2026 ; testée seulement *post-hoc* |
| Rendre le softmax moins confiant (T = 12), ou utiliser directement les probabilités du marché | appliquée en v2 |
| Obtenir des musiques **horodatées avant course** pour 2015-2022 (Geny, archives Paris-Turf), afin de rendre la forme réellement testable | à faire ; c'est la condition pour juger les critères sportifs |
| Ajouter l'évolution de la valeur handicap (montée ou descente depuis la dernière course), un candidat sérieux après le cas Chichi de la Vega | à tester |
| Utiliser le nombre de sélections de la presse comme référence supplémentaire | à tester |
| Étendre l'échantillon à d'autres grands handicaps de haies d'Auteuil (11 courses, c'est trop peu) | indispensable pour toute conclusion |

**Conditions dans lesquelles le modèle fonctionne moins bien** : un champ avec beaucoup de données manquantes, une course sans favori net (cote du favori au-dessus de 6), un vainqueur venant du bas du handicap après une série médiocre, et un écart de distance par rapport à l'historique (cas de 2026).

---

## 8. Application finale : Prix Prince d'Écouen, Grand Handicap d'Automne, 17/10/2026

### 8.1 Caractéristiques vérifiées, et ce qui ne l'a pas été

| Élément | Information trouvée | Fiabilité |
|---|---|---|
| Course | Auteuil, R1C3, 15 h 15, haies, handicap divisé Listed, 120 000 € | concordante (Equidia, Canalturf, iTurf) |
| Distance | **4 300 m** (Equidia, Canalturf) ; une source dit 3 600 m | quasi certaine, mais **différente de l'historique (3 900 m)** |
| Partants | 20 annoncés ; le n° 16 (L'Aziza des Places) n'est cité que par une source | **à vérifier** |
| Non-partants | non trouvés | **inconnu** |
| Terrain | non trouvé (souple à lourd 9 fois sur 11 dans l'historique) | **inconnu** |
| Poids | 16 sur 20 lus ; les n° 14, 16, 19 et 20 sont *inférés* par l'ordre des numéros | partiel |
| Valeurs, musiques, entraîneurs | quasi absents | **inconnu** |
| Cotes | cotes de référence Geny pour 7 chevaux (non finales) | partiel, **instable** |

Toutes ces données viennent de **résumés de recherche web**. L'accès direct aux sites (Geny, PMU, Equidia…) est bloqué par la politique réseau de cet environnement. **Je n'ai pas vérifié la liste officielle.**

### 8.2 Classement complet : ordre d'arrivée prévisionnel (Classement B, v2 verrouillée)

Fichier `predictions_verrouillees/prediction_2026_v2.json`, commit `d0db99d`, poussé **avant la course**.

| Rang prévu | N° | Cheval | Score B /100 | Score A (perf. théorique) | P(victoire) | Confiance | Justification synthétique |
|---|---|---|---|---|---|---|---|
| 1 | 4 | Gardons le Sourire | 73,3 | 61,8 (3e) | 35 %* | faible | Favori de la cote de référence (4,3), 70,5 kg ; aucune forme accessible |
| 2 | 5 | Kel Story | 56,0 | 60,0 (4e) | 8 % | faible | 9,2 ; L. Philipperon ; 68 kg |
| 3 | 6 | Grey Fighter | 54,8 | 59,4 (5e) | 8 % | faible | 9,8 ; J. Reveley ; 67,5 kg ; favori de la presse |
| 4 | 2 | Loquas | 52,7 | 62,2 (2e) | 6 % | faible | 14 ; K. Nabet ; 71,5 kg ; base de plusieurs pronostiqueurs |
| 5 | 1 | Goliath d'Aunou | 48,6 | 62,3 (1er) | 5 % | faible | Top weight 72,5 kg ; F. de Giles ; 26 |
| 6 | 11 | Robin Hill | 44,2 | 55,5 | 3 % | faible | T. Beaurain ; 64,5 kg ; cote inconnue |
| 7 | 12 | Interdit de Jeu | 43,3 | 50,9 | 3 % | faible | 16,8 ; 64,5 kg ; 2e de la course de référence selon la presse |
| 8 | 9 | Never Risk | 43,0 | 53,8 | 3 % | faible | G. Meunier ; 66 kg ; cote inconnue |
| 9 | 10 | Lemnos | 43,0 | 53,8 | 3 % | faible | A. Zuliani ; 66 kg ; cote inconnue |
| 10 | 3 | Kirikou des Mers | 42,6 | 55,8 | 3 % | faible | 37 ; 71 kg ; rentrée correcte en Groupe III (presse) |
| 11 | 7 | Rock and Roll | 42,2 | 52,7 | 3 % | faible | 5e en 2023 et 4e en 2025 de cette course ; 67 kg (contre 71 kg en 2025) |
| 12 | 8 | Aleric | 41,9 | 52,3 | 3 % | faible | 66,5 kg ; données minimales |
| 13 | 14 | Loreley des Places | 41,8 | 52,1 | 3 % | faible | poids inféré ; données minimales |
| 14 | 15 | Mohican | 41,5 | 51,7 | 3 % | faible | B. Gelhay ; 63,5 kg |
| 15 | 13 | Karafon | 40,7 | 50,5 | 2 % | faible | 64,5 kg ; données minimales |
| 16 | 16 | L'Aziza des Places | 39,7 | 49,0 | 2 % | faible | **participation non confirmée** |
| 17 | 17 | The Must | 39,2 | 48,4 | 2 % | faible | 62 kg ; « fantasque » selon la presse |
| 18 | 18 | Lilette | 39,2 | 48,4 | 2 % | faible | 62 kg (valeur 56) ; manque de marge selon la presse |
| 19 | 19 | Chant de Garde | 39,2 | 48,4 | 2 % | faible | Petit poids ; vainqueur récent ; très cité par la presse ; cote inconnue |
| 20 | 20 | Parfum d'Une Reine | 39,2 | 48,4 | 2 % | faible | données minimales |

\* Les 35 % de Gardons le Sourire reflètent surtout une seule cote de référence partielle. Historiquement, ce type de probabilité est sur-confiant. Une probabilité réaliste pour un favori de cette course serait plutôt de 15 à 20 %.

**Classement A et classement B divergent.** A (niveau théorique : poids, jockey) met les chevaux de tête du handicap devant (Goliath d'Aunou, Loquas, Gardons le Sourire). B les recale vers ce que dit le marché. Les rangs 6 à 20 sont presque à égalité (écart inférieur à 5 points) : **leur ordre n'est pas informatif.**

La v1 pré-enregistrée (`prediction_2026.json`) reste disponible pour comparaison. Elle classe Interdit de Jeu 19e à cause du défaut d'imputation corrigé en v2.

### 8.3 Synthèse demandée

- **Top 3 le plus plausible (modèle) :** 4 Gardons le Sourire, 5 Kel Story, 6 Grey Fighter.
- **Top 5 le plus plausible (modèle) :** 4, 5, 6, 2 Loquas, 1 Goliath d'Aunou.
- **Plus fiables pour les places :** 6 Grey Fighter et 2 Loquas. Ce sont les seuls chevaux cités de façon cohérente à la fois par la cote et par la presse (8 et 7 sélections sur 8). Historiquement, le favori finit dans les 5 premiers 7 fois sur 11.
- **Outsiders avec un argument sportif sérieux :**
  - 7 **Rock and Roll** : 5e en 2023 et 4e en 2025 de ce même handicap, il descend de 71 à 67 kg. C'est l'argument le plus concret dont je dispose, mais il a 8 ans et passe à 4 300 m.
  - 12 **Interdit de Jeu** : 2e de la course de référence selon la presse, 64,5 kg.
  - 19 **Chant de Garde** : petit poids et victoire récente.
  - 11 **Robin Hill** : T. Beaurain, 64,5 kg.
- **Favoris fragiles :**
  - 4 **Gardons le Sourire** : 1er du modèle uniquement grâce à une cote de référence isolée (4,3), alors que la presse lui préfère Grey Fighter. Aucune forme n'est accessible. Le favori n'a gagné qu'1 fois sur 11.
  - 1 **Goliath d'Aunou** : 72,5 kg sur 4 300 m, probablement en terrain souple.
- **Données insuffisantes :** les n° 8, 13, 14, 16, 17, 18 et 20 (ni cote, ni musique, poids parfois inféré). Le n° 16 n'est pas confirmé comme partant.
- **Confiance globale : FAIBLE.** Le classement est **provisoire**.

### 8.4 Scénarios plausibles (hypothèses, non modélisées)

Ces probabilités sont des estimations subjectives, à défaut de données sur le style de course des chevaux.

| Scénario | Probabilité estimée | Profils favorisés | Profils exposés |
|---|---|---|---|
| S1. Terrain souple à lourd, course très sélective sur 4 300 m | ≈ 50 % (le terrain a été souple à lourd 9 fois sur 11) | Chevaux d'endurance éprouvés, poids moyens à légers (64-68 kg) | Top weights (1, 2, 3), chevaux sans tenue prouvée au-delà de 3 900 m |
| S2. Train modéré, peloton groupé, emballage final | ≈ 30 % | Bons finisseurs bien montés (Reveley, Nabet, Philipperon) | Chevaux de tête sans pointe de vitesse |
| S3. Course à incidents (20 partants, chutes ou gênes) | ≈ 20 % | Aucun profil identifiable : le hasard domine | Tous, y compris les favoris |

### 8.5 Incertitude et limites

- **La méthode n'a pas battu le marché sur 11 courses.** Ce classement n'apporte donc pas d'avantage démontré sur la cote.
- La distance de **4 300 m est hors de l'historique**, et il y a 20 partants (contre 14 à 18).
- Il manque **le terrain, les non-partants, les musiques et les cotes finales**. À refaire avec le fichier officiel des partants le jour J : même format que le .docx historique, puis `python3 modele.py <fichier> 2026J predictions_verrouillees --v2`.
- **Aucun résultat 2026 n'a été consulté.** La course n'avait pas eu lieu au moment du verrouillage.

---

## 9. Fichiers

| Fichier | Contenu |
|---|---|
| `predictions_aveugles.csv` | Une ligne par cheval, par course et par variante : données pré-course, scores par critère, rangs, confiance, justification, horodatage. |
| `evaluation_predictions.csv` | Rang prévu, rang réel (Top 5 à 7), gagnant, statut, écart, outsiders et favoris fragiles, qualité des données. |
| `synthese_modeles.csv` | Comparaison des méthodes et des pondérations par période (entraînement 2015-18, validation 2019-22, test 2023-25, années propres). |
| `predictions_verrouillees/` | JSON en lecture seule et horodatés (historique gardé dans git). |
| `predictions_retrospectives_v2/` | v2 rejouée *a posteriori* : **non aveugle par rapport au choix de méthode**, à interpréter comme telle. |
| `resultats/` | Arrivées officielles (saisies après verrouillage) et détail par course. |
| `modele.py`, `evaluation.py` | Code reproductible. |

Sources des arrivées : agrégateurs consultés via la recherche web (Geny, Canalturf, Zeturf, Zone-Turf, Turfomania, Equidia, Turf-FR). Pour 2017, les 4e et 5e places diffèrent selon les sources ; c'est l'ordre de Zeturf, Canalturf et Turf-FR qui a été retenu.

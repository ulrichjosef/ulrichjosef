# PIPELINE D'ANALYSE ET DE SCÉNARISATION DES COURSES

*Version 0.1 : modèle provisoire tiré de 16 éditions exploitables du Prix de l'Arc de Triomphe (2008–2025, sans 2011 ni 2022).*

---

## 0. Statut, portée et limites

| Point | État |
|---|---|
| Base empirique | 16 courses, toutes du même type : Groupe 1, 2 400 m, Longchamp ou Chantilly, poids pour l'âge |
| Validation hors échantillon | **Aucune.** Aucune règle n'a encore été testée sur une course inédite. |
| Contamination | Je connaissais les résultats, et les documents pré-course contenaient des informations d'après-course. Les « succès » du modèle sont surestimés. |
| Qualité des données | Les deux documents se contredisent sur les stalles, les jockeys et les pelotons (voir l'audit, section 0) |
| Conséquence | Les règles ci-dessous sont des **a priori à tester**, pas des lois. Leur niveau de confiance est volontairement prudent. |

**Domaine d'application**
- **Direct** : grandes courses de plat de classe internationale sur 2 000 à 2 400 m, à poids pour l'âge.
- **Avec prudence** : autres Groupes 1 et 2 de plat.
- **Non couvert** : handicaps, trot, obstacle, sprint. La structure du pipeline reste utilisable, mais les règles chiffrées ne s'y transfèrent pas.

**Principe directeur.** Le modèle ne prédit pas un ordre unique. Il produit des **classements conditionnels par scénario**, puis une synthèse pondérée. L'erreur la plus fréquente de l'audit était de **ne pas faire remonter dans le classement les chevaux favorisés par un scénario que j'avais moi-même jugé plausible** (2010, 2019, 2020, 2021). Le pipeline est conçu pour l'empêcher.

---

## 1. Variables classées selon leur comportement historique

**Fréquences de référence** (16 courses) :
- favori gagnant : 5 sur 16 ;
- vainqueur dans les 3 premiers du marché : 9 sur 16 ;
- au moins un cheval à 20/1 ou plus dans les 3 premiers : 9 sur 16 ;
- mâles de 4 ans et plus gagnants : 3 sur 16.

### 1.1 Variables fortement utiles
| Variable | Pourquoi |
|---|---|
| **Pénétromètre (état du terrain)** | Il modifie la hiérarchie de façon reconnaissable. Sous 4,2 : 0 victoire de mâle d'âge sur 12. À 4,2 et au-dessus : 3 sur 4, avec les deux seuls gagnants à plus de 20/1 (Solemia 40/1, Torquator Tasso 80/1). |
| **Statut poids pour l'âge (3 ans, femelle)** | 13 vainqueurs sur 16 ont un avantage de poids. L'effet est mécanique (décharge de 1,5 à 5 kg), cohérent et stable sur 18 ans. |
| **Classe démontrée face aux chevaux d'âge** | Les chevaux qui ont déjà battu des chevaux d'âge en Groupe 1 (Bluestocking, Golden Horn, Enable, Sea The Stars, Workforce au Derby) résistent mieux que les « invaincus » qui ne les ont jamais affrontés (Behkabad, Sosie 2024, Minnie Hauk). |
| **Aptitude au terrain du jour, prouvée en course** | Les chevaux sous-cotés mais adaptés au terrain ont surperformé (Nakayama Festa, Solemia, Torquator Tasso, In Swoop). Ce signal est à distinguer du pedigree, qui n'est qu'une présomption. |

### 1.2 Variables potentiellement utiles
| Variable | Pourquoi |
|---|---|
| Historique dans l'épreuve même (top 5 l'année précédente) | 9 sur 22 sont revenus dans les 3 premiers, ce qui est élevé pour des pelotons de 15 à 20 chevaux. Mais beaucoup de chevaux de valeur s'effondrent l'année suivante (Aventure 2025, Los Angeles 2025). |
| Écart entre le rating et la cote | Onesto (124 de rating à 50/1, 3e), It's Gino, Nakayama Festa. Peu de cas, et les ratings du document étaient parfois reconstruits. |
| Âge du champion qui défend son titre | Les champions de 5 ans ou plus favoris ont été battus 3 fois sur 3. Le mécanisme est plausible (déclin, poids plein), mais l'échantillon est minuscule. |
| Régularité dans les places | Found, Flintshire, Youmzain, Orfevre : utile pour les places, pas pour la victoire. |

### 1.3 Variables contextuelles (utiles seulement dans certaines conditions)
| Variable | Condition d'activation |
|---|---|
| Stalle et corde | Peloton nombreux, terrain souple, open stretch (2025 : les trois premiers partaient des stalles 1 à 3). **Données à vérifier.** |
| Style de course (devant ou derrière) | Dépend du rythme : les leaders se placent quand le rythme est lent (Persian King 3e en 2020, Los Angeles 3e en 2024) et s'effondrent quand il est rapide. |
| Pedigree de tenue ou de terrain lourd | Pertinent seulement à partir d'un pénétromètre d'environ 3,8. Il départage, il ne classe pas. |
| Fatigue liée au calendrier (St Leger, double effort) | Ectot 2014, Capri 2017 et Hurricane Lane 2021 ont déçu. Signal faible mais logique. |

### 1.4 Variables faibles
| Variable | Pourquoi |
|---|---|
| Équipements (œillères, bonnet, attache-langue) | Aucun effet observable sur 18 courses |
| Météo hors terrain (vent, température) | Aucun effet observable |
| Statistiques jockey ou entraîneur sur 30 jours | Bruitées, non discriminantes à ce niveau (tous les jockeys sont d'élite) |

### 1.5 Variables trompeuses
| Variable | Pourquoi |
|---|---|
| **Victoire dans la course préparatoire sur le parcours (Prix Niel)** | 0 victoire sur 13 dans l'Arc. Elle reflète un niveau inférieur obtenu sur un rythme lent ; je l'avais surpondérée. |
| **Série de victoires du favori** | Postponed, Behkabad, Treve 2015, Sosie 2024 : la série masque souvent un plafond de valeur ou de la fatigue. |
| **Rythme projeté par les fiches de presse** | Faux en 2010, 2020 et 2021. À traiter comme une hypothèse, jamais comme une donnée. |
| **Indices « synthétiques » et conclusions des dossiers** | Contaminés ou circulaires (ils réutilisent la cote). À exclure de l'analyse. |
| Favori unanime à cote très basse | Il a gagné 5 fois sur 16 seulement. La cote mesure le consensus, pas la probabilité réelle. |

### 1.6 Variables insuffisamment documentées
Temps intermédiaires (sectionnels), nombre de jours de repos, nombre de courses dans la saison, rôles d'écurie (lièvres, chevaux d'équipe), poids réel du cheval, comportement aux stalles, vétérinaire, effet d'écurie (O'Brien 1-2-3 en 2016), origine japonaise (0 victoire sur 18 ans, mais très peu de partants).

---

## 2. Interactions retenues

Une interaction n'est retenue comme « règle » que si elle apparaît au moins 4 fois avec un mécanisme plausible.

| Interaction | Observation | Occurrences | Statut |
|---|---|---|---|
| **Poids × terrain** | L'avantage des 3 ans et des femelles domine sous 4,2 ; il s'efface au-dessus (mâles d'âge 3 sur 4) | 16 | **Retenue** |
| **Rythme × tenue** | Un rythme lent protège les chevaux limites en distance (Persian King 2020) ; un rythme rapide en lourd les élimine (Ghaiyyath 2019, Adayar 2021) | 5 | **Retenue** |
| **Rythme × style** | Un leader non contesté sur faux rythme garde une place ; les leaders sur rythme rapide ne se placent jamais | 8 | **Retenue** |
| **Terrain × style** | En terrain à 4,2 ou plus avec un rythme soutenu, les attentistes qui tiennent battent les chevaux placés qui ont attaqué tôt (Waldgeist 2019, Torquator Tasso 2021) | 3 | Prometteuse |
| Corde × peloton compact × open stretch | Les chevaux à la corde passent dans la ligne droite (Bluestocking 2024, Daryz 2025, Solemia 2012) | ~8 | Prometteuse (stalles douteuses) |
| Classe × confrontation avec les chevaux d'âge | Un 3 ans invaincu mais jamais confronté aux chevaux d'âge est surestimé (Behkabad, Sosie 2024, Minnie Hauk battue d'une tête) | 4 | Prometteuse |
| Forme × calendrier | Un gros effort 3 semaines avant (St Leger, rentrée violente) conduit à une déception | 3 | Faible |
| Cheval × épreuve (historique) | Un cheval déjà placé dans l'Arc revient placé | 9 sur 22 | Prometteuse |

---

## 3. Règles et conditions de validité

| # | Règle | Fonctionne quand | Peut échouer quand | Contre-exemples | Confiance |
|---|---|---|---|---|---|
| R1 | Favoriser les chevaux avantagés au poids (3 ans, femelles) | Terrain < 4,2, valeur proche de celle des meilleurs | Terrain ≥ 4,2 ; 3 ans jamais confronté aux chevaux d'âge | 2019, 2020, 2021 ; Sosie 2024 | **Haute** |
| R2 | À partir de 4,2, monter d'un cran l'aptitude au lourd prouvée et la tenue, baisser d'un cran la classe pure | Terrain lourd ou collant, train soutenu | Train lent (2020 : la position en course a primé) | 2025 à 4,1 | Moyenne |
| R3 | Ne jamais classer 1er un cheval qui n'a pour référence majeure qu'une victoire dans le Niel (ou une préparatoire équivalente) | Toujours vérifier | Si le cheval a déjà battu des chevaux d'âge en Groupe 1 | Aucun gagnant sur 13 | Moyenne-haute |
| R4 | Rythme : construire au moins deux hypothèses (rapide ou lent) et ne jamais se fier à la projection de presse | Toujours | — | 3 erreurs sur environ 16 | Haute (règle de méthode) |
| R5 | Un leader non contesté sur faux rythme mérite un statut de « placé possible » malgré ses doutes de tenue | Un seul leader naturel, pas de lièvre | Rythme rapide imposé par un autre | 2008, 2014, 2015, 2019, 2025 (leaders battus en rythme rapide) | Moyenne |
| R6 | Champion de 5 ans ou plus qui défend son titre comme favori : baisser d'un cran | Cote très basse, poids plein | Supériorité écrasante maintenue dans la saison | 0 victoire sur 3 | Basse |
| R7 | Un cheval sous-coté (cote ≥ 20/1) mais avec une aptitude **prouvée** au terrain du jour doit figurer dans les ordres d'arrivée possibles | Toujours, et surtout à partir de 3,8 | Aptitude seulement présumée par le pedigree | Al Riffa 2024 (11e) | Moyenne |
| R8 | La stalle doit être cohérente avec le scénario : si la course se joue à la corde, pénaliser les stalles au-delà de 10 | Peloton de 15 ou plus, open stretch, terrain souple | Jockey qui contourne (Golden Horn 2015) ; finisseurs en lourd | Aventure 2025 (erreur de cohérence) | Basse à moyenne (données à vérifier) |
| R9 | Un cheval déjà dans les 5 premiers de l'épreuve l'année précédente : +1 cran pour les places | Même parcours, âge ≤ 5 ans | Changement de forme ou de terrain | 13 échecs sur 22 | Moyenne-basse |
| R10 | Le favori n'est qu'un candidat parmi 3 ou 4 : la probabilité de victoire du meilleur profil dépasse rarement 35 à 40 % | Toujours | Champion hors normes (Sea The Stars, Enable 2017) | — | Haute (fréquence de base) |

---

## 4. Modèle de scénarios

Chaque course reçoit une **probabilité estimée pour chaque scénario** (somme = 100 %). On ne garde que 3 ou 4 scénarios utiles.

### S1 : Train soutenu sur terrain bon à souple (< 3,8)
- **Conditions** : au moins un lièvre ou deux leaders naturels, terrain rapide.
- **Déroulement** : peloton étiré, accélération décisive à partir de 400 m, les meilleurs chevaux s'expriment.
- **Favorisés** : classe + poids (3 ans, femelles), chevaux bien placés dans le premier tiers, accélérateurs qui tiennent.
- **Défavorisés** : leaders, chevaux à la tenue limite, chevaux bloqués en 3e épaisseur.
- **Variables critiques** : valeur, poids, placement.
- **Indicateurs** : pénétromètre ≤ 3,5, lièvres déclarés. Exemples : 2008, 2009, 2015, 2017, 2018, 2023.

### S2 : Faux rythme / course tactique
- **Conditions** : pas de lièvre (forfait ou absence), un seul leader naturel.
- **Déroulement** : peloton groupé, sprint à partir de 500 m.
- **Favorisés** : chevaux placés devant, leader non contesté, chevaux de vitesse limite en distance.
- **Défavorisés** : stayers purs, attentistes extrêmes.
- **Variables critiques** : position à 600 m, capacité d'accélération.
- **Indicateurs** : liste des leaders vide ou réduite à un seul, forfaits tardifs. Exemples : 2010, 2020, en partie 2024.

### S3 : Course d'usure en terrain lourd (≥ 4,2)
- **Conditions** : pénétromètre ≥ 4,2, rythme soutenu.
- **Déroulement** : les leaders et les chevaux qui attaquent tôt faiblissent dans les 150 derniers mètres ; les finisseurs qui tiennent remontent, souvent par l'extérieur.
- **Favorisés** : aptitude au lourd prouvée, tenue (pedigree allemand ou Montjeu à titre d'indice), mâles d'âge robustes.
- **Défavorisés** : chevaux de vitesse, chevaux japonais, favoris qui attaquent tôt, chevaux légers sans tenue.
- **Variables critiques** : aptitude au terrain, tenue, moment de l'effort.
- **Indicateurs** : pluie de plus de 20 mm sur 48 à 72 h, pénétromètre ≥ 4,2. Exemples : 2012, 2019, 2021.

### S4 : Course de corde, peloton compact
- **Conditions** : terrain souple, rythme moyen, open stretch, peloton nombreux.
- **Déroulement** : les chevaux à la corde économisent du terrain et trouvent l'ouverture ; les chevaux en dehors parcourent plus de distance.
- **Favorisés** : petites stalles, chevaux maniables, jockeys patients.
- **Défavorisés** : stalles au-delà de 10, finisseurs en 3e épaisseur.
- **Variables critiques** : stalle, maniabilité.
- **Indicateurs** : open stretch actif, rythme pas trop rapide. Exemples : 2024, 2025.

### S5 : Incident ou chaos
- **Conditions** : toujours possible (environ 15 à 25 %).
- **Déroulement** : départ manqué, enfermement, cheval qui penche, favori qui ne se montre pas.
- **Favorisés** : chevaux réguliers bien placés, et l'outsider adapté au terrain.
- **Indicateurs** : antécédents de comportement (Orfevre, Zarkava aux stalles), peloton de plus de 18 chevaux.

**Pondération par défaut des scénarios** (à ajuster) :

| Situation | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|
| Terrain < 3,8, lièvre présent | 50 | 10 | 0 | 20 | 20 |
| Terrain < 3,8, sans lièvre | 15 | 45 | 0 | 20 | 20 |
| Terrain de 3,8 à 4,1 | 30 | 15 | 20 | 20 | 15 |
| Terrain ≥ 4,2 | 10 | 20 | 50 | 5 | 15 |

---

## 5. Le pipeline

### ÉTAPE 1 : Compréhension de la course
- **Entrées** : catégorie, distance, hippodrome, piste, corde, sens, nombre de partants, échelle de poids, lice ou open stretch, terrain et pénétromètre, météo des 72 dernières heures, place dans la réunion.
- **Sorties** :
  - une fiche contexte ;
  - la **classe de terrain** : T1 < 3,5 ; T2 de 3,5 à 3,8 ; T3 de 3,8 à 4,1 ; T4 ≥ 4,2 ;
  - le **niveau d'avantage de poids** (écart réel en kg entre les catégories).
- **Contrôle** : l'échelle de poids est-elle cohérente avec le règlement (ex. 2025 : 58 kg annoncés pour les 3 ans, une erreur) ?

### ÉTAPE 2 : Normalisation des données
1. **Vérifier l'identité de chaque partant** : stalle, jockey et poids, croisés avec une source officielle. Toute contradiction est signalée et fait baisser la confiance de l'analyse.
2. **Purger le document** : exclure les conclusions, les « déroulements prédictifs », les indices synthétiques opaques et tout fait postérieur à la course (temps du gagnant, palmarès incluant l'année en cours, allocations révélatrices).
3. **Convertir** : cotes en probabilités sans marge ; ratings sur une même échelle ; forme en notes ordinales (voir l'étape 3).
4. **Séparer** les données de **marché** (cotes, mouvements) des données **sportives**. Le marché ne sert qu'à l'étape 9.

### ÉTAPE 3 : Analyse individuelle (fiche par cheval)
Notes ordinales de 0 à 3 :

| Code | Dimension | Critère d'un 3 |
|---|---|---|
| V | Valeur démontrée | Groupe 1 gagné **contre des chevaux d'âge** au niveau de l'épreuve |
| Vp | Plafond potentiel | Une performance isolée de très haut niveau (ex. Workforce au Derby), même si la forme récente est mauvaise avec des excuses documentées |
| F | Forme / fraîcheur | Dernière course bonne, 3 à 6 semaines de repos, pas d'effort extrême récent |
| D | Distance | A gagné ou s'est placé en Groupe 1 sur la distance |
| T | Terrain du jour | A gagné ou s'est placé en Groupe sur un terrain équivalent (**prouvé**, pas présumé) |
| H | Historique dans l'épreuve ou sur le parcours | Placé dans l'épreuve elle-même (le Niel ne compte pas comme preuve de niveau) |
| St | Style | Leader / placé / milieu / attentiste |
| R | Risques | Comportement, distance inconnue, calendrier, changement de jockey forcé |

Signaux à appliquer d'office :
- **Drapeau « Niel »** : la seule référence majeure est une préparatoire, donc V est plafonnée à 2.
- **Drapeau « jamais face aux chevaux d'âge »** pour un 3 ans : V est plafonnée à 2.
- **Drapeau « champion de 5 ans ou plus qui défend son titre »** : risque +1.

### ÉTAPE 4 : Compatibilité cheval × conditions
Indice de compatibilité de base, **IC = V + Vp/2 + F + D + T + bonus de poids**.

| Bonus de poids | T1–T2 | T3 | T4 |
|---|---|---|---|
| Pouliche de 3 ans | +2 | +1 | 0 |
| Mâle de 3 ans ou femelle d'âge | +1 | +0,5 | 0 |
| Mâle d'âge | 0 | 0 | 0 (en T4, T est doublé à la place) |

**En T4, T compte double.** Les coefficients sont des **a priori grossiers** : ils servent à ordonner, pas à calculer une probabilité.

### ÉTAPE 5 : Analyse tactique
- Classer chaque cheval : leader désigné, leader naturel, placé, milieu, attentiste.
- Croiser avec la stalle **uniquement si elle est vérifiée** : stalles 1 à 6 (corde), 7 à 12, 13 et au-delà.
- Repérer les **rôles d'écurie** : lièvres, chevaux d'équipe, plusieurs partants de la même écurie.
- Repérer les **risques de parcours** : finisseur à la corde (enfermement), stalle extérieure + leader (effort précoce).

### ÉTAPE 6 : Construction du rythme probable
- Compter les leaders réels, c'est-à-dire ceux qui ont mené lors de leurs 3 dernières courses. Ignorer la projection de presse.
  - 0 ou 1 leader : rythme lent probable (S2).
  - 2 leaders ou plus, ou un lièvre déclaré : rythme soutenu (S1 ou S3).
- Noter **toujours** l'hypothèse inverse et sa probabilité (au moins 20 %). C'est la leçon de 2010, 2020 et 2021.

### ÉTAPE 7 : Génération des scénarios
- Choisir 3 ou 4 scénarios parmi S1 à S5 dans le tableau de pondération (section 4).
- Ajuster les probabilités selon le nombre de leaders, les forfaits, la pluie annoncée et les antécédents de comportement des favoris.
- **Écrire pour chaque scénario les 2 ou 3 chevaux qu'il favorise.** Ces chevaux devront apparaître dans la synthèse (étape 10).

### ÉTAPE 8 : Évaluation des chevaux dans chaque scénario
**Score par scénario = IC + ajustement de scénario (de −2 à +2)**, selon la grille :

| Scénario | +2 | +1 | −1 | −2 |
|---|---|---|---|---|
| S1 | V = 3 et placé | Accélérateur qui tient la distance | Leader | Distance douteuse |
| S2 | Leader non contesté | Placé, vitesse | Stayer pur | Attentiste extrême |
| S3 | T = 3 et tenue | Mâle d'âge robuste | Cheval de vitesse, attaque précoce | T présumé seulement |
| S4 | Stalle 1 à 4, maniable | Stalle 5 à 8 | Stalle 11 à 14 | Stalle 15 et au-delà, finisseur |
| S5 | Régulier, bien placé | — | Comportement à risque | — |

On obtient un classement par scénario.

### ÉTAPE 9 : Analyse des risques
- **Risques individuels** : comportement, distance, calendrier, jockey.
- **Confrontation avec le marché.** Pour chaque cheval, comparer le rang du modèle au rang du marché :
  - si le modèle est **beaucoup plus optimiste** que le marché, chercher une information manquante (vétérinaire, travail du matin) ;
  - si le modèle est **beaucoup plus pessimiste**, vérifier qu'on ne surpondère pas une variable « trompeuse » (Niel, série en cours).
- **Fiabilité des données** : chaque contradiction de l'étape 2 fait baisser d'un cran la confiance globale.

### ÉTAPE 10 : Synthèse des scénarios
- **Rang attendu** = somme, sur les scénarios, de (probabilité du scénario × rang du cheval dans ce scénario).
- **Robustesse** = nombre de scénarios où le cheval est dans les 3 premiers.
- **Contrôle de cohérence (obligatoire)** : chaque cheval favorisé par un scénario ≥ 20 % doit figurer dans les 6 premiers du rang attendu. Sinon, le corriger ou justifier par écrit. C'est la leçon d'Aventure 2025, d'Enable 2019 et de Persian King 2020.

### ÉTAPE 11 : Classements conditionnels
Produire les classements suivants :
- un **classement synthétique** (rang attendu) ;
- un **classement par scénario** pour les 2 scénarios principaux ;
- quatre groupes :
  - **G1, solides** : dans les 3 premiers dans au moins 3 scénarios ;
  - **G2, favorables** : dans les 3 premiers dans 2 scénarios ;
  - **G3, dépendants du scénario** : dans les 3 premiers dans 1 seul scénario ;
  - **G4, à risque** : aucun.

### ÉTAPE 12 : Ordres d'arrivée possibles
Produire **trois ordres** :
1. **Ordre de base** : rang attendu, top 5.
2. **Ordre alternatif** : le scénario n° 2 réalisé.
3. **Ordre outsider** : au moins un cheval coté ≥ 20/1 avec un signal de la règle R7 ou R5 dans les 5 premiers (9 courses sur 16 ont eu un tel cheval dans les 3 premiers).

Donner aussi une **probabilité indicative de victoire** pour les 4 premiers, plafonnée à 40 % pour le meilleur (règle R10).

**Registre de sortie** : reprendre le format du registre pré-course (ordre, solides, dangereux, dépendants, sous-évalués, hypothèses, risques, variables clés, variables incertaines), **en ajoutant la probabilité de chaque scénario** pour pouvoir l'auditer ensuite.

---

## 6. Règle anti-surapprentissage

### 6.1 Tests appliqués à chaque pattern
1. **Fréquence** : au moins 5 occurrences pour être « robuste », de 3 à 4 pour être « prometteur ».
2. **Contre-exemples** : comptés explicitement ; plus de 30 % de contre-exemples ramènent à « faible ».
3. **Mécanisme** : explication physique ou tactique plausible indépendante du résultat.
4. **Contamination** : un pattern soutenu surtout par des courses où le document contenait des fuites (2012, 2014, 2015, 2021) est rétrogradé d'un niveau.
5. **Hors échantillon** : aucun pattern n'est « confirmé » tant qu'il n'a pas fonctionné sur au moins 5 courses inédites.

### 6.2 Classification actuelle

| Niveau | Patterns |
|---|---|
| **ROBUSTE** | Avantage de poids sous 4,2 (13 sur 16, mécanisme clair) · le terrain modifie la hiérarchie au-delà de 4,2 · le favori n'est pas fiable (5 sur 16) · le rythme projeté par la presse est peu fiable |
| **PROMETTEUR** | Le gagnant du Niel ne gagne pas (0 sur 13, mais le niveau de l'Arc l'explique en partie) · leader non contesté sur faux rythme placé · les déjà placés dans l'épreuve reviennent placés · un cheval sous-coté mais adapté au terrain surperforme · un 3 ans jamais confronté aux chevaux d'âge est surestimé |
| **FAIBLE** | Avantage de la corde / des petites stalles (données contradictoires) · champion de 5 ans ou plus battu (3 cas) · fatigue après le St Leger (3 cas) · pedigree allemand en lourd |
| **ANECDOTIQUE** | Effet d'écurie O'Brien (2016) · aucun Japonais vainqueur (aucun mécanisme isolé, peu de partants) · « croire l'entourage sur la santé » (Treve 2014, contaminé) · un lièvre placé (Penglai Pavilion 2013) |

### 6.3 Signes de surapprentissage à surveiller
- Une règle formulée avec un seuil très précis qui ne sépare qu'une ou deux courses (ex. « pénétromètre 4,1 contre 4,2 »). Les seuils sont des **zones**, pas des frontières.
- Une règle inventée pour « sauver » une erreur précise (ex. « les fils de Sea The Stars gagnent en souple » : 1 seul cas, 2025).
- Une amélioration du score rétrospectif sans nouvelle course testée.
- Toute pondération chiffrée ajustée pour reproduire les 16 arrivées passées.

---

## 7. Fiche opératoire (à copier pour chaque nouvelle course)

```
COURSE : …  DATE : …  CLASSE TERRAIN : T1/T2/T3/T4  PARTANTS : …
DONNÉES VÉRIFIÉES : oui/non (contradictions : …)   CONFIANCE : haute/moyenne/basse
LEADERS RÉELS : …  → RYTHME : lent/soutenu (hypothèse inverse : …%)
SCÉNARIOS : S_ …% | S_ …% | S_ …% | S5 …%
FICHES : cheval | V | Vp | F | D | T | H | style | stalle | drapeaux | IC
CLASSEMENT PAR SCÉNARIO : S_ : … / S_ : …
RANG ATTENDU : 1… 2… 3… 4… 5…
CONTRÔLE DE COHÉRENCE : chevaux favorisés par un scénario ≥ 20 % absents du top 6 → …
GROUPES : G1 … G2 … G3 … G4 …
ORDRES : base … | alternatif … | outsider …
PROBABILITÉS DE VICTOIRE (top 4) : …
CONFRONTATION AVEC LE MARCHÉ : écarts > 3 rangs → explication
À OBSERVER APRÈS LA COURSE : scénario réalisé, rythme réel, position à 600 m, trajectoires
```

---

## 8. Données supplémentaires les plus utiles (par ordre de priorité)

1. **Courses inédites, analysées réellement à l'aveugle** (après la date de coupure de mes connaissances), avec des documents pré-course sans conclusion ni scénario rédigés. C'est indispensable pour toute validation.
2. **Données officielles vérifiées** : stalles, jockeys, poids et partants (France Galop, PMU). C'est indispensable pour juger la variable stalle.
3. **Temps intermédiaires (sectionnels)** : ceux de la course (rythme réel) et ceux des courses de préparation (qualité réelle de la forme, notamment pour les gagnants du Niel).
4. **Positions en course** à 1 000 m, 600 m et 400 m. Elles permettent de mesurer l'effet du style et de la corde.
5. **Calendrier** : jours depuis la dernière course, nombre de courses dans la saison, distance de la dernière course.
6. **Rôles d'écurie** déclarés (lièvres, chevaux d'équipe).
7. **Élargir l'échantillon** à d'autres Groupes 1 de 2 000 à 2 400 m (King George, Grand Prix de Saint-Cloud, Prix du Jockey Club, Irish Champion), pour tester les règles hors de l'Arc et augmenter le nombre de cas.
8. **Ratings officiels non reconstruits** (Official Rating avant la course) et cotes horodatées.
9. **Informations vétérinaires et comportementales** (incidents aux stalles, retraits, rapports de commissaires).

**Prochaine étape recommandée.** Appliquer ce pipeline tel quel, sans modifier les pondérations, à 5 à 10 courses non encore courues. Les auditer avec le même protocole, puis seulement réviser les règles.

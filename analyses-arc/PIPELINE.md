# PIPELINE D'ANALYSE ET DE SCÉNARISATION DES COURSES

*Version 0.3 : modèle tiré de 16 éditions exploitables du Prix de l'Arc de Triomphe (2008–2025, sans 2011 ni 2022), recalé sur les **arrivées vérifiées** (Wikipedia, Racing Post, France Galop). Pour une explication pas à pas avec un exemple complet, voir [GUIDE.md](GUIDE.md).*

**Changements de la v0.3 (génération dynamique des scénarios)**
1. Nouveau module **4 bis : Moteur de génération dynamique des scénarios**. Le nombre de scénarios n'est plus fixé : il découle des axes d'incertitude ouverts, des interactions et d'un test de distinction (fusion des scénarios équivalents).
2. Les scénarios S1 à S5 de la section 4 deviennent une **bibliothèque de configurations de référence**. Ils restent valides et servent de repères, mais ne sont plus une liste à remplir.
3. Les étapes 7, 10, 11 et 12 sont **complétées** sans supprimer leurs règles : génération dynamique, synthèse croisée, groupes relatifs au nombre de scénarios, un ordre par scénario retenu.
4. Ajout d'un **niveau de soutien** pour chaque affirmation : D (donnée), E (extrapolation d'un pattern), H (hypothèse).
5. Ajout d'**emplacements pour le trot** (autostart ou volté, recul, numéro derrière l'autostart, driver, déferrage, risque de disqualification). **Aucune règle trot n'est encore établie** : notre base historique ne contient que des courses de plat.

**Changements de la v0.2**
1. Les arrivées vérifiées remplacent le document de résultats précédent. Corrections : 2010 (Behkabad 4e), 2018 (Cloth of Stars 3e, Waldgeist 4e, Capri 5e), jockeys de 2008, 2010, 2018 et 2021.
2. Ajout d'une **hiérarchie des sources** (étape 2).
3. Suppression d'un **double comptage** : la distance non prouvée était pénalisée deux fois (note D + ajustement −2 dans S1). Voir l'étape 8.
4. Mise à jour des chiffres de la règle R9 (historique dans l'épreuve).

---

## 0. Statut, portée et limites

| Point | État |
|---|---|
| Base empirique | 16 courses, toutes du même type : Groupe 1, 2 400 m, Longchamp ou Chantilly, poids pour l'âge |
| Validation hors échantillon | **Aucune.** Aucune règle n'a encore été testée sur une course inédite. |
| Contamination | Je connaissais les résultats, et les documents pré-course contenaient des informations d'après-course. Les « succès » du modèle sont surestimés. |
| Qualité des données | Arrivées : **vérifiées** (top 4 ou 5 chaque année, top 10 en 2018, top 8 en 2025). Jockeys : en grande partie confirmés. **Stalles : toujours non vérifiées**, car aucune source fiable ne les fournit encore. |
| Conséquence | Les règles ci-dessous sont des **a priori à tester**, pas des lois. Leur niveau de confiance est volontairement prudent. |

**Domaine d'application**
- **Direct** : grandes courses de plat de classe internationale sur 2 000 à 2 400 m, à poids pour l'âge.
- **Avec prudence** : autres Groupes 1 et 2 de plat.
- **Non couvert par des règles apprises** : handicaps, trot, obstacle, sprint. La structure du pipeline, y compris le moteur de scénarios (4 bis), est utilisable. Les axes propres au trot y sont prévus, mais **leurs effets restent à apprendre** à partir de courses de trot auditées. Je n'ai encore analysé aucune course de trot.

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
| Historique dans l'épreuve même (top 5 l'année précédente) | Selon les arrivées vérifiées, **11 sur 29** sont revenus dans les 3 premiers (38 %), ce qui est élevé pour des pelotons de 15 à 20 chevaux. Exemples : Cloth of Stars (2e en 2017, 3e en 2018), Youmzain, Flintshire, Orfevre. Mais certains déçoivent l'année suivante (Aventure et Los Angeles en 2025). |
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
| R9 | Un cheval déjà dans les 5 premiers de l'épreuve l'année précédente : +1 cran pour les places | Même parcours, âge ≤ 5 ans | Changement de forme ou de terrain | 18 échecs sur 29 (11 retours dans le top 3) | Moyenne |
| R10 | Le favori n'est qu'un candidat parmi 3 ou 4 : la probabilité de victoire du meilleur profil dépasse rarement 35 à 40 % | Toujours | Champion hors normes (Sea The Stars, Enable 2017) | — | Haute (fréquence de base) |

---

## 4. Modèle de scénarios

**Statut depuis la v0.3** : les scénarios S1 à S5 sont une **bibliothèque de configurations de référence** issue de l'historique. Ils servent :
- à nommer et à reconnaître une configuration quand elle correspond à un cas connu ;
- à fournir des ajustements déjà calibrés (grille de l'étape 8) ;
- à vérifier qu'un scénario généré dynamiquement n'en double pas un autre.

Le nombre et le contenu des scénarios d'une course sont désormais produits par le **moteur 4 bis**. Une course peut donner 2 scénarios ou 6, et un scénario peut ne correspondre à aucune entrée de la bibliothèque.

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

**Pondération de départ des familles de référence** (point de départ du moteur 4 bis ; à ajuster) :

| Situation | S1 | S2 | S3 | S4 | S5 |
|---|---|---|---|---|---|
| Terrain < 3,8, lièvre présent | 50 | 10 | 0 | 20 | 20 |
| Terrain < 3,8, sans lièvre | 15 | 45 | 0 | 20 | 20 |
| Terrain de 3,8 à 4,1 | 30 | 15 | 20 | 20 | 15 |
| Terrain ≥ 4,2 | 10 | 20 | 50 | 5 | 15 |

---

## 4 bis. Moteur de génération dynamique des scénarios (v0.3)

### 4b.1 Principe
```
DONNÉES DE LA COURSE + HISTORIQUE → PATTERNS (sections 1, 2, 3) → INTERACTIONS (4b.3)
→ AXES D'INCERTITUDE OUVERTS (4b.2) → CONFIGURATIONS CANDIDATES → TEST DE DISTINCTION ET FUSION
→ SCÉNARIOS DISTINCTS → HIÉRARCHIES CONDITIONNELLES → SYNTHÈSE CROISÉE (4b.7)
```
Un scénario est une **configuration de course** : un déroulement, défini par l'état de quelques facteurs. Ce n'est pas une liste de chevaux. Le nombre de scénarios est une **conséquence** de l'analyse :
- aucun minimum artificiel, sauf la règle R4 : si le rythme est incertain, ses deux versions doivent être examinées ;
- aucun maximum, mais chaque scénario doit passer le test de distinction (4b.4).

### 4b.2 Les axes de configuration
Un **axe** est un facteur dont l'état n'est pas connu avant la course et qui peut changer la hiérarchie. Il est **ouvert** s'il remplit deux conditions :
1. son état est réellement incertain d'après les données ;
2. le changement d'état modifie le groupe de tête (test d'impact : au moins un cheval entre ou sort du top 4 provisoire).

Sinon il est **fermé** : son état le plus probable est fixé, et il ne génère pas de scénario.

| Axe | États possibles | Données qui déterminent l'état | Base historique |
|---|---|---|---|
| **A1. Rythme** | lent / modéré / soutenu | nombre de leaders réels, lièvres, forfaits | **Plat : forte** (R4, R5 ; 2010, 2020, 2021) |
| **A2. Terrain effectif** | stable / s'alourdit / sèche pendant la réunion | pénétromètre du matin, pluie annoncée, position de la course dans la réunion | **Plat : forte** (classes T1 à T4, R1, R2) |
| **A3. Trajectoire / corde** | la corde paie / l'extérieur paie / neutre | taille du peloton, open stretch, état de la corde, stalles **vérifiées** | Plat : prometteuse (2024, 2025), stalles à vérifier |
| **A4. Tenue du ou des favoris** | reproduisent leur niveau / défaillent | drapeaux (jamais face aux chevaux d'âge, Niel, champion de 5 ans ou plus, calendrier), dépendance au terrain | Plat : favori gagnant 5 fois sur 16 seulement (R10) |
| **A5. Moment décisif de l'effort** | long effort depuis 600 m / sprint court après 300 m | rythme, profil de la ligne droite, styles en présence | Plat : prometteuse (Waldgeist 2019, Torquator Tasso 2021 contre 2020) |
| **A6. Rôles d'écurie / tactique collective** | lièvre efficace / lièvre ignoré / écurie qui verrouille | partants d'une même écurie, lièvres déclarés | Plat : anecdotique (2016) |
| **A7. Incident** | aucun / départ manqué, enfermement, cheval qui penche | antécédents comportementaux, taille du peloton | Plat : faible mais récurrent (Zarkava 2008, Orfevre 2012) |
| *T1. Type de départ (trot)* | autostart / volté | conditions de la course | **Aucune** : à apprendre |
| *T2. Recul / handicap de distance (trot)* | effet neutre / pénalisant / compensé par le rythme | mètres de recul, capacité à produire un long effort | **Aucune** : à apprendre |
| *T3. Numéro derrière l'autostart (trot)* | placement facile / chevaux enfermés en 2e ligne | numéro, vitesse au départ | **Aucune** : à apprendre |
| *T4. Allures / disqualification (trot)* | course propre / fautes | historique de fautes, ferrure (déferré des 4 ou non), terrain | **Aucune** : à apprendre |
| *T5. Driver × configuration (trot)* | driver offensif / attentiste | statistiques du driver selon le scénario | **Aucune** : à apprendre |

Les axes T1 à T5 sont des **emplacements prévus**. Tant qu'aucune course de trot n'a été auditée, leurs effets sont des hypothèses (niveau H). Ils ne doivent pas être présentés comme des patterns.

### 4b.3 Interactions : c'est d'elles que naissent les scénarios distincts
Un axe isolé déplace peu la hiérarchie. Les scénarios **réellement distincts** naissent des interactions, c'est-à-dire des combinaisons d'axes qui avantagent des profils différents.

| Interaction | Effet attendu | Statut (plat) |
|---|---|---|
| Rythme × tenue | Faux rythme : les chevaux limites en distance tiennent. Rythme rapide en lourd : ils s'effondrent. | **Retenue** |
| Rythme × style | Leader seul et rythme lent : il se place. Leaders multiples : ils s'effondrent. | **Retenue** |
| Terrain × poids | L'avantage de poids s'efface à partir de T4 | **Retenue** |
| Terrain × style × moment de l'effort | T4 + rythme soutenu + long effort : les attentistes qui tiennent battent les chevaux qui attaquent tôt | Prometteuse |
| Stalle × rythme × open stretch | Rythme moyen + peloton compact : la corde paie | Prometteuse (stalles à vérifier) |
| Forme × niveau de compétition | Série gagnée sous le niveau de l'épreuve (Niel, invaincu sans chevaux d'âge) : surestimation | Prometteuse |
| Aptitude au parcours × rythme | La spécialité du tracé aide surtout quand le rythme est régulier | Faible |
| Équipement × comportement historique | Œillères pour la première fois sur un cheval tendu | **Non observée** (aucun effet en 18 ans) |
| *Recul × distance ; handicap × effort prolongé (trot)* | Le recul pèse moins sur longue distance et rythme soutenu | **H** (à apprendre) |
| *Numéro derrière l'autostart × style (trot)* | Petit numéro + cheval rapide : position de tête. Grand numéro + attentiste : dépend du rythme. | **H** (à apprendre) |
| *Driver × configuration (trot)* | Un driver offensif valorise le scénario rythme soutenu | **H** (à apprendre) |

### 4b.4 Procédure de génération
1. **Lister les axes ouverts** (4b.2, test d'impact). En pratique, 1 à 4 axes sont ouverts.
2. **Combiner leurs états** pour former des configurations candidates.
3. **Éliminer** les combinaisons incohérentes, comme une course d'usure avec un sprint court, et les combinaisons jugées très improbables (soutien H uniquement et contraires à un pattern robuste).
4. **Construire la hiérarchie de chaque candidate**. On applique les étapes 4 et 8 : l'indice de compatibilité IC plus les ajustements dictés par les facteurs de la configuration, sur l'échelle de −2 à +2 (déjà calibrée dans la bibliothèque quand la configuration y ressemble).
5. **Test de distinction et fusion.** Deux candidates sont **fusionnées** si elles produisent :
   - le même déroulement décrit ;
   - **ou** le même groupe de tête, c'est-à-dire au moins 3 chevaux communs sur 4 avec le même cheval en tête.

   Une candidate n'est **retenue** que si elle apporte **au moins une** différence réelle :
   - un déroulement différent ;
   - un autre cheval en tête ;
   - un cheval qui entre dans le top 4 ou en sort.
   *Précision v0.3.1 (première application à l'aveugle, Arc 2026)* :
   - deux chevaux séparés de ≤ 0,5 point sont **co-têtes** ;
   - « même tête » signifie que les ensembles de co-têtes se recoupent ;
   - le critère de fusion **prévaut** : la « différence réelle » s'apprécie après fusion.
6. **Arrêter** quand plus aucune candidate ne passe le test. Le nombre de scénarios obtenu est le résultat.
7. **Vérifier la couverture.** Au moins un scénario doit couvrir l'hypothèse « le ou les favoris ne reproduisent pas leur niveau » si un drapeau existe (axe A4). Rappel : favori gagnant 5 fois sur 16.

### 4b.5 Fiche de chaque scénario retenu (12 rubriques)
Chaque affirmation porte un niveau de soutien : **[D]** donnée de la course, **[E]** extrapolation d'un pattern (avec son niveau : robuste, prometteur, faible), **[H]** hypothèse incertaine.

1. **Nom du scénario** (descriptif, ex. « Course de position à la corde sur rythme moyen »)
2. **Déroulement probable** : départ, placement, rythme, moment décisif
3. **Conditions d'apparition** : états des axes qui doivent se réaliser
4. **Facteurs historiques qui le soutiennent** : patterns et règles (R1 à R10), avec leur niveau
5. **Chevaux particulièrement favorisés**
6. **Chevaux particulièrement vulnérables**
7. **Chevaux susceptibles de progresser** par rapport à l'analyse principale (rang attendu)
8. **Chevaux susceptibles de régresser**
9. **Profils outsiders compatibles** (règles R5 et R7, cote ≥ 20/1)
10. **Impact sur les chevaux déjà identifiés** par l'analyse principale
11. **Ordre ou groupes plausibles** dans cette configuration
12. **Arguments précis du pipeline** : variables, interactions et règles mobilisées

### 4b.6 Hiérarchie des scénarios (sans score arbitraire)
Les scénarios sont présentés en trois niveaux de cohérence avec les données :

| Niveau | Critère |
|---|---|
| **Forte concordance** | Ses conditions sont annoncées par des données de la course [D], **et** il s'appuie sur au moins un pattern robuste ou une règle de confiance haute |
| **Concordance partielle** | Données de la course compatibles mais non décisives ; il s'appuie sur des patterns prometteurs |
| **Hypothèse** | Il repose surtout sur [H] ou sur des patterns faibles, mais il passe le test de distinction et reste plausible |

Pour chaque scénario, expliquer en une ou deux phrases **pourquoi** il est à ce niveau : combien d'éléments indépendants concordent et ce qui le contredit.

*Pour le calcul du rang attendu (étape 10), et seulement là, chaque niveau reçoit un poids indicatif :*
- *forte concordance : 25 à 45 % ;*
- *concordance partielle : 10 à 25 % ;*
- *hypothèse : 5 à 10 %.*

*On normalise ensuite à 100 %. Ces poids servent à combiner les classements, pas à présenter les scénarios.*

### 4b.7 Synthèse croisée
Après la génération, produire :

| Rubrique | Définition opératoire |
|---|---|
| Chevaux présents dans plusieurs scénarios | Top 4 dans au moins la moitié des scénarios retenus |
| Chevaux « de configuration » | Top 4 dans un seul scénario |
| Dépendance au déroulement | **Amplitude** = écart entre le meilleur et le pire rang selon les scénarios (≥ 4 : très dépendant) |
| Bénéficiaires d'une défaillance du favori | Les chevaux qui montent le plus dans le scénario « favori défaillant » |
| Outsiders récurrents | Cote ≥ 20/1 et top 5 dans au moins 2 scénarios |
| Soutien par arguments indépendants | Nombre de **familles d'arguments** distinctes qui soutiennent le cheval : valeur, terrain prouvé, tactique ou position, historique dans l'épreuve, écart cote/valeur. Au moins 3 familles : soutien solide. |
| Convergences | Ce qui reste vrai dans tous les scénarios (chevaux toujours dans le top 4, chevaux jamais placés) |
| Divergences | Les axes qui renversent la hiérarchie, et les chevaux concernés |

### 4b.8 Illustration rétrospective (2025)
*Illustration seulement : je connais l'arrivée, donc cet exemple ne prouve rien. Il montre la mécanique.*
- **Axes ouverts.**
  - A1, le rythme : 3 leaders, donc un rythme soutenu probable, mais un rythme modéré reste possible [D].
  - A3, la corde : open stretch et 17 partants [D]. L'axe change le top 4 (Minnie Hauk, Daryz et Sosie en stalles 1 à 3 contre Aventure en stalle 12).
  - A4, le favori : Minnie Hauk n'a jamais affronté de chevaux d'âge [D], ce qui correspond au pattern prometteur « 3 ans invaincu surestimé ».
- **Axe fermé.** A2, le terrain : 4,1 et stable [D]. Il ne génère pas de scénario.
- **Candidates.** 2 × 2 × 2 = 8. Le calcul, fait avec l'IC + les ajustements de l'étape 8 (détail dans [GUIDE.md](GUIDE.md)), donne ceci :
  - « rythme modéré » : groupe de tête Minnie Hauk, Aventure, Sosie, Kalpana ;
  - « la corde paie » : Minnie Hauk, Sosie, Aventure, puis Daryz à égalité avec Kalpana.

  Même cheval en tête et 3 chevaux communs sur 4 : ces deux candidates sont **fusionnées** en un seul scénario, *Course de position à la corde*. En combinant leurs ajustements : Minnie Hauk 16,5, Sosie 16, Aventure 13, Daryz 12,5.
- La candidate « favori défaillant » donne Aventure, Sosie, Kalpana, Byzantine Dream. La candidate « rythme soutenu, trajectoire neutre » donne Aventure, Sosie, Minnie Hauk, Kalpana. Même cheval en tête et 3 chevaux communs : elles sont **fusionnées** elles aussi. La couverture « favori défaillant » (étape 7 de la procédure) est assurée par ce scénario fusionné.
- **Résultat : 2 scénarios seulement.** Les autres combinaisons ne changeaient pas le groupe de tête. Ce nombre est une conséquence du calcul, pas un choix.
  1. *Sélection par la valeur (rythme soutenu, corde neutre ; inclut la variante « favori défaillant »)* : Aventure, Sosie, Minnie Hauk ou Kalpana. Concordance partielle.
  2. *Course de position à la corde* : Minnie Hauk, Sosie, Aventure, Daryz. Concordance partielle.
- **Synthèse croisée.**
  - Sosie est 2e dans les deux scénarios : c'est la **convergence**.
  - Minnie Hauk dépend de l'axe A3, la corde (1re ou 3e).
  - Daryz est un **cheval de configuration** : il n'entre dans le top 4 que dans le scénario 2.
  - Aventure est en tête dans le scénario 1 et seulement 3e dans le scénario 2.
- **Confrontation avec l'arrivée** (Daryz, Minnie Hauk, Sosie). C'est le scénario 2 qui s'est réalisé. Les trois premiers figuraient dans son top 4, mais Daryz y était 4e et non 1er. Le moteur dynamique rend Daryz **visible** comme cheval de configuration (la v0.2 le classait 6e), sans le désigner gagnant.

**Son efficacité réelle reste à mesurer sur des courses inédites.**

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
   **Hiérarchie des sources** (de la plus fiable à la moins fiable) :
   1. France Galop, PMU, Racing Post (officielles) ;
   2. Wikipedia et presse spécialisée contemporaine ;
   3. dossier pré-course compilé ;
   4. synthèses générées après coup.

   En 2008–2025, les erreurs venaient surtout des synthèses générées après coup (arrivées 2010 et 2018, plusieurs jockeys).
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
**Depuis la v0.3 : appliquer le moteur 4 bis** (axes ouverts, puis interactions, candidates, test de distinction et fusion, et enfin fiche en 12 rubriques pour chaque scénario retenu). La bibliothèque S1 à S5 et le tableau de pondération servent de point de départ et de repère. Les règles ci-dessous restent valables :
- Partir des familles S1 à S5 les plus proches de la course (section 4) pour amorcer la génération, sans s'y limiter.
- Ajuster les probabilités selon le nombre de leaders, les forfaits, la pluie annoncée et les antécédents de comportement des favoris.
- **Écrire pour chaque scénario les 2 ou 3 chevaux qu'il favorise.** Ces chevaux devront apparaître dans la synthèse (étape 10).

### ÉTAPE 8 : Évaluation des chevaux dans chaque scénario
**Score par scénario = IC + ajustement de scénario (de −2 à +2)**, selon la grille :

| Scénario | +2 | +1 | −1 | −2 |
|---|---|---|---|---|
| S1 | V = 3 et placé | Accélérateur qui tient la distance | Leader | Tenue **contredite** par une course (a déjà calé sur la distance) |
| S2 | Leader non contesté | Placé, vitesse | Stayer pur | Attentiste extrême |
| S3 | T = 3 et tenue | Mâle d'âge robuste | Cheval de vitesse, attaque précoce | T présumé seulement |
| S4 | Stalle 1 à 4, maniable | Stalle 5 à 8 | Stalle 11 à 14 | Stalle 15 et au-delà, finisseur |
| S5 | Régulier, bien placé | — | Comportement à risque | — |

On obtient un classement par scénario.

**Scénarios hors bibliothèque (v0.3).** Pour un scénario généré qui ne correspond à aucune famille S1 à S5, les ajustements de −2 à +2 sont déduits de ses **facteurs déterminants** (rubrique 3 de sa fiche), sur la même échelle. Chaque ajustement est justifié par une interaction du tableau 4b.3 et porte un niveau [D], [E] ou [H]. Un ajustement [H] ne peut pas dépasser ±1.

**Règle de non-double-comptage (ajoutée en v0.2).** Une même information n'intervient qu'à un seul endroit du calcul. La distance non prouvée est déjà dans la note D : elle ne doit pas être pénalisée une seconde fois dans un scénario. Seule une tenue **contredite** par une course (le cheval a déjà calé sur la distance) justifie l'ajustement −2. Ce défaut a été trouvé en rejouant 2025 (Daryz). Il aurait aussi pénalisé à tort Ace Impact (2023), qui découvrait lui aussi les 2 400 m. Il est corrigé parce que c'est une **erreur de logique**, pas pour coller à un résultat.

### ÉTAPE 9 : Analyse des risques
- **Risques individuels** : comportement, distance, calendrier, jockey.
- **Confrontation avec le marché.** Pour chaque cheval, comparer le rang du modèle au rang du marché :
  - si le modèle est **beaucoup plus optimiste** que le marché, chercher une information manquante (vétérinaire, travail du matin) ;
  - si le modèle est **beaucoup plus pessimiste**, vérifier qu'on ne surpondère pas une variable « trompeuse » (Niel, série en cours).
- **Fiabilité des données** : chaque contradiction de l'étape 2 fait baisser d'un cran la confiance globale.

### ÉTAPE 10 : Synthèse des scénarios
- **Rang attendu** = somme, sur les scénarios, de (probabilité du scénario × rang du cheval dans ce scénario).
- **Robustesse** = nombre de scénarios où le cheval est dans les 3 premiers.
- **Contrôle de cohérence (obligatoire)** : chaque cheval favorisé par un scénario ≥ 20 % doit figurer dans les 6 premiers du rang attendu. Sinon, le corriger ou justifier par écrit. C'est la leçon d'Aventure 2025, d'Enable 2019 et de Persian King 2020. *(v0.3 : les « 20 % » s'entendent comme tout scénario au moins en concordance partielle.)*
- **Synthèse croisée (v0.3)** : produire le tableau 4b.7, avec les convergences, les divergences, l'amplitude par cheval et les familles d'arguments indépendantes.

### ÉTAPE 11 : Classements conditionnels
Produire les classements suivants :
- un **classement synthétique** (rang attendu) ;
- quatre groupes :
  - **G1, solides** : dans les 3 premiers dans au moins la moitié des scénarios retenus, et soutenus par au moins 3 familles d'arguments ;
  - **G2, favorables** : dans les 3 premiers dans au moins 2 scénarios ;
  - **G3, dépendants du scénario** : dans les 3 premiers dans 1 seul scénario (préciser lequel) ;
  - **G4, à risque** : aucun.

  *(v0.3 : ces seuils sont relatifs au nombre de scénarios retenus. La v0.2 utilisait « 3 scénarios » quand il y en avait 4 ou 5.)*
- un **classement par scénario pour chaque scénario retenu**, et plus seulement pour les 2 principaux.

### ÉTAPE 12 : Ordres d'arrivée possibles
**Depuis la v0.3, le nombre d'ordres suit le nombre de scénarios retenus** :
1. **Ordre synthétique** : rang attendu, top 5.
2. **Un ordre par scénario retenu** : top 5, avec le nom du scénario et son niveau de concordance.
3. **Ordre outsider**, seulement s'il existe un signal R5 ou R7. Il doit compter au moins un cheval coté ≥ 20/1 dans les 5 premiers (9 courses sur 16 ont eu un tel cheval dans les 3 premiers). S'il coïncide avec l'ordre d'un scénario, on ne le duplique pas.

Donner aussi une **probabilité indicative de victoire** pour les 4 premiers, plafonnée à 40 % pour le meilleur (règle R10).

**Registre de sortie** : reprendre le format du registre pré-course (ordre, solides, dangereux, dépendants, sous-évalués, hypothèses, risques, variables clés, variables incertaines), **en ajoutant la liste des scénarios retenus, leur niveau de concordance, les axes ouverts et les candidates fusionnées**. L'audit post-course pourra ainsi vérifier quel scénario s'est réalisé, et si un scénario manquait.

---

## 5 bis. Résultat d'un premier test rétrospectif (2025)

Le pipeline a été appliqué tel quel au dossier pré-course 2025 (détail dans [GUIDE.md](GUIDE.md)) :
- **ordre proposé** : Minnie Hauk, Aventure, Sosie, Kalpana, Byzantine Dream, Daryz ;
- **ordre réel** : Daryz, Minnie Hauk, Sosie… Aventure 11e.

Ce que le test montre :
- 2 des 3 premiers sont trouvés ;
- le vainqueur est classé 6e ;
- le scénario « corde » (S4), pourtant réalisé, ne pesait que 20 % ;
- Daryz, sans victoire de Groupe 1, avait une note de valeur faible.

**Je ne modifie pas les pondérations pour faire gagner Daryz après coup** : ce serait du surapprentissage. Ces deux points deviennent des **ajustements candidats**, à tester sur de nouvelles courses :
- (a) dans un terrain T3 ou T4 avec open stretch et 15 partants ou plus, monter S4 à 30 % ;
- (b) pour un 3 ans dont la seule faiblesse est la distance non prouvée, utiliser le plafond Vp plutôt que V.

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
AXES OUVERTS : A_ (états …) | A_ (…) | … AXES FERMÉS : …
INTERACTIONS ACTIVES : …
CANDIDATES : n = … → FUSIONS : … → SCÉNARIOS RETENUS : n = …
SCÉNARIO k : nom | niveau (forte/partielle/hypothèse) | conditions | favorisés | vulnérables | ordre top 5 | [D]/[E]/[H]
FICHES : cheval | V | Vp | F | D | T | H | style | stalle | drapeaux | IC
SYNTHÈSE CROISÉE : multi-scénarios … | de configuration … | amplitude ≥ 4 … | bénéficiaires d'une défaillance … | outsiders récurrents … | convergences … | divergences …
RANG ATTENDU : 1… 2… 3… 4… 5…
CONTRÔLE DE COHÉRENCE : chevaux favorisés par un scénario ≥ 20 % absents du top 6 → …
GROUPES : G1 … G2 … G3 … G4 …
ORDRES : synthétique … | par scénario (k = 1…n) … | outsider (si signal R5/R7) …
PROBABILITÉS DE VICTOIRE (top 4) : …
CONFRONTATION AVEC LE MARCHÉ : écarts > 3 rangs → explication
À OBSERVER APRÈS LA COURSE : scénario réalisé (parmi les n), scénario manquant ?, fusion abusive ?, rythme réel, position à 600 m, trajectoires
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
10. **Pour activer les axes trot (T1 à T5)** : des courses de trot auditées avec le même protocole, en précisant pour chacune :
    - type de départ, recul et numéro derrière l'autostart ;
    - driver, ferrure (déferré ou non) et fautes ou disqualifications passées ;
    - réductions kilométriques et positions en course.

    Il faut au moins 10 à 15 courses par type de départ avant de qualifier un pattern de « prometteur ».

**Prochaine étape recommandée.** Appliquer ce pipeline tel quel, sans modifier les pondérations, à 5 à 10 courses non encore courues. Les auditer avec le même protocole, puis seulement réviser les règles.

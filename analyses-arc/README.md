# Prix de l'Arc de Triomphe 2008–2025 : analyses pré-course (phase « aveugle »)

Source : `Données Pré-Course 1.docx`, avec 18 éditions de 2008 à 2025.
Méthode : protocole en 9 sections (course, partants, interactions, déroulement, 3 scénarios, groupes, traçabilité, variables, registre). Un fichier par édition.

**Audit post-course : voir [AUDIT.md](AUDIT.md).**

**Modèle opératoire : voir [PIPELINE.md](PIPELINE.md).**

## ⚠️ Limites de validité, à lire avant toute exploitation

1. **Aveugle impossible.** Les résultats de ces 18 courses sont dans mes données d'entraînement (y compris 2025). Je me suis limité aux données du document, sans pouvoir garantir que cette connaissance ne m'a pas influencé.
2. **Le document lui-même contient des informations d'après-course.** Il a probablement été généré par une IA qui connaissait les arrivées.

| Année | Fuite ou biais repéré | Gravité |
|---|---|---|
| 2008 | Temps du gagnant (2'28"80). Allocation identique pour les 3e et 4e, ce qui trahit un dead-heat. It's Gino noté OR 124 alors qu'il est coté 150/1. | Forte |
| 2009 | La section 20 raconte la victoire de Sea The Stars | Moyenne |
| 2010 | — | Faible |
| 2011 | **Arrivée complète, écarts et temps record** en section 20. Ratings apparemment reconstruits. | **Rédhibitoire** |
| 2012 | La section 20 décrit le récit réel (Orfevre penche, Solemia passe à la corde) | Forte |
| 2013 | La section 20 raconte la victoire de Treve | Moyenne |
| 2014 | « Head-Maarek : 3 victoires (1979, 2013, **2014**) ». RPR de 128 pour Treve malgré sa saison. | Forte |
| 2015 | La section 20 décrit le scénario réel. « Fabre : 8 Arcs », anachronisme. | Forte |
| 2016 | — | Faible |
| 2017 | Léger biais dans le schéma tactique | Faible |
| 2018 | La section 20 décrit le scénario réel (Sea Of Class en trombe) | Moyenne |
| 2019 | Conclusion orientée vers Waldgeist | Moyenne |
| 2020 | Conclusion orientée vers Sottsass et In Swoop | Moyenne |
| 2021 | Conclusion orientée vers Torquator Tasso (« surprise d'envergure ») | Moyenne |
| 2022 | **Arrivée officielle complète** + « Demuro vainqueur avec Ace Impact » (2023) | **Rédhibitoire** |
| 2023 | « Demuro vainqueur de l'Arc 2023 » | Forte |
| 2024 | « Départ effectif à 16h27 ». La section 20 décrit le scénario réel. | Moyenne |
| 2025 | Indice global orienté vers Daryz malgré un rating inférieur. Échelle de poids des 3 ans erronée. | Moyenne |

Recommandation : **exclure 2011 et 2022** de toute mesure. Considérer les sections 17 à 20 de chaque document (« conclusion », « déroulement prédictif », « indices calculés ») comme contaminées. Pour un vrai test, il faut des courses postérieures à juin 2026 ou des documents générés sans accès aux résultats.

## Registre consolidé (ordre théorique, 3 premiers)

| # | Course | 1 | 2 | 3 | Sous-évalué(s) signalé(s) |
|---|---|---|---|---|---|
| 1 | [2008](#2008) | Zarkava | Youmzain | Soldier of Fortune | Youmzain, It's Gino |
| 2 | [2009](2009.md) | Sea The Stars | Fame and Glory | Conduit | Dar Re Mi, Youmzain |
| 3 | [2010](2010.md) | Behkabad | Fame And Glory | Workforce | Nakayama Festa, Workforce |
| 4 | [2011](2011.md) ⛔ | Galikova | Danedream | Sarafina | Danedream, Shareta |
| 5 | [2012](2012.md) | Orfevre | Great Heavens | Masterstroke | Solemia, Masterstroke |
| 6 | [2013](2013.md) | Treve | Orfevre | Kizuna | Treve |
| 7 | [2014](2014.md) | Taghrooda | Flintshire | Treve | Flintshire, Treve |
| 8 | [2015](2015.md) | Treve | Golden Horn | New Bay | Golden Horn, Flintshire |
| 9 | [2016](2016.md) | Postponed | Found | Harzand | Highland Reel, Silverwave |
| 10 | [2017](2017.md) | Enable | Ulysses | Cloth of Stars | Cloth of Stars |
| 11 | [2018](2018.md) | Enable | Sea Of Class | Waldgeist | Cloth Of Stars |
| 12 | [2019](2019.md) | Enable | Waldgeist | Sottsass | Waldgeist, Magical |
| 13 | [2020](2020.md) | Sottsass | Enable | In Swoop | Sottsass, In Swoop |
| 14 | [2021](2021.md) | Hurricane Lane | Tarnawa | Snowfall | Torquator Tasso, Alenquer |
| 15 | [2022](2022.md) ⛔ | Alpinista | Torquator Tasso | Vadeni | Westover |
| 16 | [2023](2023.md) | Ace Impact | Westover | Hukum | Onesto, Westover |
| 17 | [2024](2024.md) | Sosie | Bluestocking | Aventure | Aventure, Al Riffa |
| 18 | [2025](2025.md) | Minnie Hauk | Aventure | Daryz | Daryz |

## Hypothèses récurrentes (à vérifier, pas encore des règles)

- La décharge de poids des pouliches de 3 ans semble décisive à valeur égale.
- L'aptitude au terrain (pénétromètre au-dessus de 4) pourrait primer sur la classe pure.
- Les stalles extérieures (au-delà de 13–14) pénalisent, mais les grands favoris les surmontent parfois.
- Un lièvre garantit un train sélectif, ce qui favorise la tenue.
- La forme sur le parcours (Niel, Vermeille, Foy) est un bon indicateur.
- La forme étrangère (Allemagne, Japon) est difficile à étalonner : c'est la principale source d'incertitude.

<a id="2008"></a>
## Course 1 : Arc 2008 (rappel du registre)
- **Ordre** : 1 Zarkava, 2 Youmzain, 3 Soldier of Fortune, 4 Vision d'Etat, 5 Duke of Marmalade, 6 Getaway, 7 It's Gino, 8 Papal Bull.
- **Très solides** : Zarkava, Youmzain.
- **Dangereux** : Soldier of Fortune, Vision d'Etat.
- **Dépendants du scénario** : Duke of Marmalade, Getaway, It's Gino.
- **Potentiellement sous-évalués** : Youmzain (12/1), It's Gino (si son rating est exact).
- **Principales hypothèses** : train fort, terrain neutre, décharge de poids décisive.
- **Principaux risques d'erreur** : le départ de Zarkava, un train lent, les enfermements à la corde.

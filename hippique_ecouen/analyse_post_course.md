# Analyse post-course : pourquoi les prédictions ont différé des arrivées

Source : fichier « Après course » fourni le 17/10/2026, avec les arrivées complètes, les non-classés et les cotes. Les Top 5 utilisés pour l'évaluation (récupérés sur le web) sont **identiques** à ce fichier pour les 11 éditions. Les prédictions verrouillées n'ont pas été modifiées. Les chiffres se reproduisent avec `analyse_erreurs.py` ; la sortie est dans `resultats/analyse_erreurs_sortie.txt`.

## 1. Erreur de conception n° 1 : le critère « valeur » favorisait les gros poids

Faute de valeur officielle en 2015-2022, la « valeur sportive » (15 pts) reposait sur le poids porté. La pénalité de poids (15 pts × 0,4 à 0,6) ne compensait qu'en partie. **Au total, plus un cheval portait lourd, plus il marquait de points.** Le handicapeur a pourtant déjà égalisé les chances par le poids : c'était un double comptage.

| Tiers de poids dans la course | Part du Top 5 réel | Gagnants | Part placée par le modèle dans son Top 5 |
|---|---|---|---|
| Haut | 24 % | 2 | **37 %** |
| Milieu | 40 % | 5 | 33 % |
| Bas | **47 %** | 4 | **18 %** |

« Valeur » est le critère qui a le plus pénalisé **8 gagnants sur 11** : Mister Emily, Kami Kaze, Célèbre d'Allen, Zarisk, Bonaparte Sizing, Foreign Flower, Kapteen et Chichi de la Vega.
Correctif testé *a posteriori* (supprimer ce critère) : le gagnant entre dans le Top 3 4 fois sur 11 au lieu de 3, et le Top 5 retrouvé passe de 45 % à 47 %. C'est mieux, mais **toujours sous la cote seule (53 %)**.

## 2. Erreur n° 2 : les non-classés étaient ignorés

39 partants sur 170 n'ont pas fini (23 %). **12 des 55 chevaux du Top 5 prévu n'ont pas été classés** (AR/T), contre 7 pour le Top 5 de la cote.
- Six d'entre eux étaient des chevaux **sans cote** (Pagomix, Rasique, December, Emirat, St Romain du Derby, Pharaon). La note neutre les avait remontés.
- Les autres : favoris ou chevaux bien cotés arrêtés ou tombés (Calayan 2019, Happyday 2022, Realm Keeper 2018, Rêve de Prince 2024…). Le modèle n'avait pas les musiques pour mesurer leur fiabilité.
- Sur le marché, les chevaux cotés au-delà du 10e rang ne finissent pas dans **40 %** des cas.

## 3. Erreur n° 3 : copier la cote revient à copier ses faiblesses

| Rang à la cote | Victoire | Top 5 | Non classé |
|---|---|---|---|
| Favori | 9 % | 64 % | 9 % |
| 2e-3e | 9 % | 50 % | 14 % |
| 4e-6e | **15 %** | 45 % | 18 % |
| 7e-10e | 7 % | 30 % | 11 % |
| 11e et + | **0 %** | 15 % | 40 % |

Le classement B reprend 30 % de la cote et ne contredit jamais le favori. Or, dans cette course, le favori est un bon cheval **à placer**, pas un gagnant. Les gagnants viennent surtout des rangs 4 à 6 de la cote, et jamais au-delà de la cote 23.

## 4. Données qui manquaient (et qui étaient connaissables avant la course)

- **L'historique de la course.** Les habitués ne sont pas pris en compte. Un cheval déjà dans les 3 premiers revient dans les 5 premiers 5 fois sur 10 (Silver Axe, Chichi de la Vega, Folly Foot, Rock and Roll…).
- **L'entraîneur**, masqué en 2015-2022 à cause de la fuite. Rob. Collet a gagné en 2021, 2022 et 2023 ; C. Lefebvre en 2022, 2023 et 2025. Pour 2022, 2023 et 2025, ces victoires antérieures étaient connues avant le départ. C'est une hypothèse à tester, sans conclusion possible sur si peu de cas.
- **Les musiques fiables**, présentes seulement pour 2025. En 2025, la forme a bien classé Jackson Ville (+8 pts sur le champ), mais le favori Undeniable Alibi a fini 10e.

## 5. Ce qui relève du hasard de la course

- Même la cote ne fait qu'une corrélation de rang moyenne d'environ +0,3 avec l'arrivée (de −0,15 en 2019 à +0,56 en 2020).
- 2022 a été une course d'élimination : 8 classés sur 16.
- Le Quinté+ ordre a dépassé 190 000 € quatre fois, signe que l'ordre réel était très improbable même pour l'ensemble des parieurs.
- Une part de l'écart n'est donc réductible par **aucun** modèle.

## 6. Corrections proposées pour une v3, à valider sur d'autres courses

1. Supprimer le bonus implicite de poids. En handicap, le poids doit rester neutre, voire légèrement favorable aux chevaux légers sur terrain lourd.
2. Ajouter un risque de non-classement : cote longue, chutes ou arrêts dans la musique, 20 partants, terrain lourd.
3. Utiliser la cote comme filtre (exclure les chevaux au-delà de la cote 23) plutôt que comme score.
4. Ajouter l'historique de la course et celui de l'entourage, calculés **uniquement** sur les éditions antérieures.
5. Valider sur d'autres handicaps de haies d'Auteuil. Tout réglage fait sur ces 11 courses serait du sur-ajustement.

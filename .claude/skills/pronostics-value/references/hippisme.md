# Référence — Analyse Hippique (PMU / Quinté+)

Spécifications pour l'analyse des courses hippiques. Lire ce fichier avant de
modéliser, puis appliquer le pipeline unifié de `SKILL.md`.

## Table des matières
1. Identifier le format (impacte les variables clés)
2. Données à rassembler (Bloc 0)
3. Variables par ordre d'importance & sélection
4. Modèle probabiliste (Plackett-Luce / softmax)
5. Devigging du marché PMU & value
6. Construction du ticket Quinté+ / couverture
7. Format de sortie hippique

---

## 1. Identifier le format

Le format conditionne quelles variables dominent. Repérer :

- **Plat handicap (galop)** — ex. Saint-Cloud, Longchamp, Chantilly, Bordeaux.
  Variables fortes : valeur handicap/poids porté, corde (draw) selon la piste,
  distance, terrain (going), forme, jockey, entraînement.
- **Trot attelé avec échelons de handicap** — ex. Lyon-Parilly, Angers,
  Le Croisé-Laroche, Caen, Vire. Variables fortes : recul/échelon (25 m, 50 m…),
  aptitude à la distance, régularité (fautes/disqualifications), driver, ferrure,
  déferrage.
- **Trot autostart** (départ derrière l'autostart) — pas de recul ; la place au
  départ et la vitesse de base priment.
- **Grande Piste de Vincennes** (ex. 2700 m autostart) — spécificités de tracé et
  d'endurance ; l'aptitude à la piste et à la distance est déterminante.
- **Obstacle (haies / steeple)** — ex. Auteuil. Variables fortes : sauteur fiable,
  expérience de l'obstacle, terrain souple, poids, endurance.

Noter aussi : discipline monté vs attelé (trot), catégorie/classe de l'épreuve,
nombre de partants (impacte la dispersion des probabilités).

## 2. Données à rassembler (Bloc 0)

Rassembler pour **chaque partant**, sans présélection :

- **Identité** : numéro, corde/échelon, âge, sexe.
- **Forme récente** : 5 à 6 dernières performances (place, écart, conditions),
  régularité, progression/régression.
- **Aptitudes** : distance, terrain/going, piste/hippodrome, corde, main
  (droite/gauche), autostart vs volté.
- **Conditions du jour** : état du terrain, météo, distance exacte, corde de la
  réunion.
- **Poids / handicap** : poids porté (plat) ou recul/échelon (trot), valeur
  handicap, évolution récente de la valeur.
- **Équipe** : jockey/driver (statistiques, association avec l'entraîneur),
  entraîneur (forme d'écurie), propriétaire si pertinent.
- **Matériel** : ferrure/déferrage (trot — signal fort), œillères (plat).
- **Marché** : cote PMU (rapport probable), évolution de la cote, éventuels
  mouvements.
- **Comportement** : notes sur le tempérament au départ, aptitude à se placer,
  finish, incidents récents (fautes, arrêts).

Signaler explicitement toute donnée absente : elle élargit l'incertitude, elle ne
se remplace pas par une hypothèse.

## 3. Variables par ordre d'importance & sélection

Objectif : garder le signal, éliminer le bruit.

1. Classer les variables par pouvoir prédictif via pondération de type SHAP sur un
   modèle de référence (gradient boosting sur historique), ou à défaut par gain
   d'information / corrélation avec l'arrivée.
2. Construire un **score composite pondéré** par partant. Convention réutilisable :
   - **SGC** = Score Global Composite (agrégat pondéré de toutes les dimensions).
   - **SGP** = composante « Performance/forme ».
   - **SGV** = composante « Value/marché » (proximité forme vs cote).
3. Contrôler la **multicolinéarité (VIF)** : poids et valeur handicap, forme et
   régularité, etc. peuvent être redondants — fusionner ou écarter.
4. Conserver le sous-ensemble parcimonieux le plus explicatif. Documenter les
   variables écartées et la raison.

Signaux souvent décisifs selon le format : recul/échelon et déferrage (trot),
corde et poids (plat handicap), fiabilité au saut et terrain souple (obstacle),
aptitude distance + autostart (Grande Piste).

## 4. Modèle probabiliste

- Convertir les scores composites en **probabilités de victoire** via
  **Plackett-Luce** (modèle de classement) ou **softmax** sur les scores.
- En déduire des **probabilités de place** cohérentes (top 3 / top 5 selon le
  nombre de partants et le type de pari).
- Vérifier que les probabilités somment à 1 sur le champ et restent cohérentes
  entre victoire et place.

## 5. Devigging du marché PMU & value

- Convertir les rapports probables PMU en probabilités implicites, puis **retirer la
  marge** (méthode multiplicative ; envisager Shin/power sur gros champ) pour
  obtenir la proba de marché « juste ».
- `edge = p_modèle − p_marché_dévigée`. Repérer :
  - **Favoris solides** : p_modèle élevée ET confirmée par plusieurs dimensions →
    candidats « base ».
  - **Value / tocards** : p_modèle nettement supérieure à p_marché sur un partant
    peu coté → candidats à intégrer pour le rapport.
- Ne retenir que les edges robustes (survivant à la validation walk-forward).

## 6. Construction du ticket Quinté+ / couverture

Structurer autour de trois rôles :

- **Base(s)** : 1 à 2 partants à forte probabilité et edge — présents sur tous les
  tickets.
- **Associés** : partants probables complétant la combinaison.
- **Value / outsiders** : 1 à 2 tocards à edge positif, pour viser le rapport.

Adapter la **largeur de couverture** au budget et à la dispersion des probabilités
(champ ouvert → couverture plus large ; course « pointue » → resserrer). Rappeler
que chaque cheval ajouté augmente le coût et dilue le rendement : chercher le
meilleur compromis couverture/valeur, pas la couverture maximale.

Proposer, selon le budget : Quinté+ en ordre/désordre, champ réduit, et
éventuellement des paris annexes (Tiercé/Quarté, couplé, 2sur4) cohérents avec
l'analyse.

## 7. Format de sortie hippique

Suivre le gabarit de `SKILL.md`, en précisant :

- Tableau des partants : n° | proba victoire modèle | proba place | cote PMU |
  proba marché dévigée | edge | rôle (base/associé/value).
- Ticket(s) Quinté+ proposé(s) avec base/associés/value et budget.
- Paris annexes éventuels.
- **Confiance & réserves** : calibration, incertitudes (terrain incertain, partant
  fragile, données manquantes) et rappel que l'aléa de course (incident, faute,
  disqualification) reste hors modèle. Une base « solide » n'est pas une garantie.

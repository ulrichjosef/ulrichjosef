# Référence — Analyse Tennis

Spécifications pour l'analyse de matchs de tennis. Lire ce fichier avant de
modéliser, puis appliquer le pipeline unifié de `SKILL.md`.

## Table des matières
1. Données à rassembler (Bloc 0)
2. Variables & sélection (l'effet surface domine)
3. Modèle de probabilité de match (Elo surface / logistique)
4. Cadre « Gazon-Value » et déclinaisons par surface
5. Demandes « sûr à 90 % » : traitement honnête
6. Devigging, value & paris
7. Format de sortie tennis

---

## 1. Données à rassembler (Bloc 0)

Pour **chaque joueur/joueuse** :

- **Niveau par surface** : Elo spécifique à la surface (terre, gazon, dur, indoor).
  La surface est le facteur le plus discriminant du tennis — un joueur peut être
  excellent sur terre et médiocre sur gazon.
- **Statistiques de service/retour** : % de points gagnés sur 1re/2e balle, points
  de retour gagnés, % de jeux de service tenus, balles de break sauvées/converties.
- **Forme récente** : résultats et niveau de jeu récents, idéalement pondérés par la
  qualité des adversaires et la surface.
- **H2H** : confrontations directes, à pondérer selon la surface et la récence
  (échantillon souvent réduit).
- **Fatigue & calendrier** : nombre et durée des matchs récents, temps de
  récupération, enchaînement de tournois, fuseaux/voyage.
- **Conditions** : indoor/outdoor, altitude, vitesse de la surface, balles, météo.
- **Contexte** : blessure/gêne physique signalée, retour de blessure, motivation
  (importance du tournoi/tour).
- **Marché** : cotes bookmaker (vainqueur, handicap jeux/sets, over/under).

Signaler les données manquantes (stats de service indisponibles, forme sur la
surface faible en échantillon).

## 2. Variables & sélection (l'effet surface domine)

- Prioriser l'**Elo par surface** et les **stats service/retour ajustées à la
  surface** comme socle.
- Pondérer la forme par récence et par surface (une forme sur dur informe peu un
  match sur gazon).
- Contrôler la redondance (VIF) : Elo surface et % de jeux tenus se recoupent
  partiellement.
- H2H : signal faible, ne pas surpondérer (surtout hors surface concernée).

## 3. Modèle de probabilité de match

Deux approches complémentaires :

- **Approche Elo-surface** : différentiel d'Elo sur la surface → probabilité de
  victoire via la fonction logistique.
- **Approche par points de service** : estimer la probabilité de gagner un point au
  service pour chaque joueur, puis dériver analytiquement (ou par simulation) la
  probabilité de gagner jeu → set → match. Utile pour les marchés handicap
  jeux/sets et over/under.

Combiner les deux (ensemble/pondération) pour robustesse. Valider en walk-forward et
vérifier la calibration.

## 4. Cadre « Gazon-Value » et déclinaisons par surface

Décliner le modèle selon la surface, car les dynamiques changent :

- **Gazon (Wimbledon)** — « Modèle Gazon-Value » : surface rapide, service
  prépondérant, matchs à faible taux de break → surpondérer la qualité de service et
  la tenue d'engagement ; les tie-breaks pèsent lourd. Les gros serveurs sont
  sous-estimés sur la proba de tenir leurs jeux.
- **Terre battue (Roland-Garros)** : échanges longs, retour et endurance
  déterminants, plus de breaks → surpondérer le jeu de fond de court, la régularité
  et la condition physique.
- **Dur (Open d'Australie / US Open)** : profil intermédiaire, équilibre
  service/retour ; l'ajustement dépend de la vitesse spécifique du court.

Toujours indiquer quelle déclinaison est appliquée et pourquoi.

## 5. Demandes « sûr à 90 % » : traitement honnête

L'utilisateur demande souvent une sélection « à ~90 % de passer, peu importe la
cote ». Traiter ainsi :

- Identifier les **favoris nets** que le modèle soutient réellement à haute proba
  (grand écart d'Elo surface, avantage de service marqué, adversaire fatigué/blessé).
- Être explicite : **90 % n'est pas une garantie** (~1 échec sur 10), et ces favoris
  sont cotés très bas (souvent 1.05–1.15). « Peu importe la cote » implique un gain
  unitaire faible et un risque réel si on empile les mises.
- Marchés parfois plus « sûrs » qu'un vainqueur pur : handicap jeux favorable, « le
  favori gagne au moins un set », total de jeux — à condition que le modèle les
  soutienne. Ne jamais afficher « 90 % » sans que la proba calibrée le justifie.
- Rappeler que c'est la calibration et le volume qui paient, pas un ticket isolé.

## 6. Devigging, value & paris

- Retirer la marge du bookmaker (marché à 2 issues : devig simple et fiable) pour la
  proba implicite « juste ».
- `edge = p_modèle − p_marché_dévigée` → value si edge positif robuste. Le tennis
  offre souvent de la value sur les marchés annexes (handicap jeux, over/under)
  moins efficients que le vainqueur.
- **Combinés** : dans un même match, vainqueur + handicap + over sont corrélés — ne
  pas les multiplier comme indépendants. Chaque jambe réduit la proba globale.
- Dimensionner via Kelly fractionné, plafonné par pari.

## 7. Format de sortie tennis

Suivre le gabarit de `SKILL.md` :

- Par match : surface + déclinaison appliquée, proba de victoire, probas des marchés
  annexes retenus.
- Tableau value : marché | proba modèle | cote | proba marché dévigée | edge.
- Sélections « haute confiance » avec proba calibrée honnête.
- Paris/combinés proposés avec note de corrélation et mise (% bankroll).
- **Confiance & réserves** : calibration, incertitudes (blessure en cours de match,
  météo, forme sur surface en faible échantillon) et rappel que proba ≠ certitude
  (abandon, cadre du filet, coup de chaud restent hors modèle).

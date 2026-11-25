# Référence — Analyse Football

Spécifications pour l'analyse de matchs de football. Lire ce fichier avant de
modéliser, puis appliquer le pipeline unifié de `SKILL.md`.

## Table des matières
1. Données à rassembler (Bloc 0)
2. Variables & sélection
3. Modèle de buts (Poisson / Dixon-Coles + xG)
4. Dérivation des marchés (1X2, BTTS, over/under, score exact)
5. Ajustements motivationnels & contextuels
6. Demandes « sûr à 90 % » : traitement honnête
7. Devigging, value & combinés
8. Format de sortie football

---

## 1. Données à rassembler (Bloc 0)

Pour **chaque équipe** :

- **xG / xGA** : buts attendus créés et concédés (moyennes récentes + tendance),
  idéalement pondérés par la qualité de l'adversaire.
- **Forme** : résultats récents, mais surtout performances sous-jacentes (xG) plutôt
  que les seuls scores (qui contiennent du bruit).
- **Domicile / extérieur** : avantage du terrain, splits domicile vs extérieur.
- **Confrontations directes (H2H)** : à pondérer faiblement (échantillon réduit,
  effectifs changeants) — indicatif, pas déterminant.
- **Effectif** : blessures, suspensions, rotations probables, retours de sélection.
- **Repos & calendrier** : jours de récupération, déplacement, match européen en
  semaine.
- **Enjeu / motivation** : position au classement, objectif (titre, Europe,
  maintien), matchs « à enjeu asymétrique » (une équipe joue tout, l'autre rien).
- **Style/tactique** : compatibilité des styles (bloc bas vs équipe de possession,
  intensité du pressing) pouvant influencer le nombre de buts.
- **Marché** : cotes bookmaker 1X2 et marchés annexes.

Signaler les données manquantes (compos non confirmées, xG indisponible) : elles
élargissent l'incertitude.

## 2. Variables & sélection

- Prioriser les **xG** comme socle prédictif (meilleur signal que les scores bruts).
- Pondérer par qualité d'adversaire et récence (les matchs récents pèsent plus).
- Contrôler la redondance (VIF) : forme et xG récents se recoupent — éviter le
  double comptage.
- Traiter H2H et « série en cours » comme signaux faibles, à ne pas surpondérer.

## 3. Modèle de buts (Poisson / Dixon-Coles + xG)

1. Estimer des **forces d'attaque et de défense** par équipe à partir des xG
   (informées par la ligue, l'adversaire, le lieu).
2. En déduire les **espérances de buts** λ_domicile et λ_extérieur pour le match.
3. Modéliser le nombre de buts par une loi de **Poisson**, avec correction
   **Dixon-Coles** pour les scores faibles corrélés (0-0, 1-0, 0-1, 1-1) que le
   Poisson simple sous-estime.
4. En sortie : matrice des probabilités de scores exacts, d'où se dérivent tous les
   marchés.
5. Ajustement sur historique : pondération temporelle exponentielle (demi-vie
   ~180 jours en club), avantage du terrain estimé (désactivé en terrain neutre),
   et **uniquement les matchs antérieurs à la date du pronostic**.
6. Option nuls fréquents (phases de poules, matchs fermés) : Poisson bivarié à
   inflation diagonale — mais n'en garder l'usage que si un backtest le justifie
   (pas de gain significatif constaté sur les grands tournois).
7. Données minces : mélanger la proba du modèle avec celle du marché dévigé
   plutôt que de faire confiance au modèle seul.

Outil : `prevision-football/scripts/match_model.py` (fit sur CSV ou grille
depuis λ) renvoie directement tous les marchés ci-dessous.

Valider en walk-forward chronologique (pas de fuite de données) et vérifier la
calibration (les 1X2 donnés à p % arrivent-ils ~p % du temps ?).

## 4. Dérivation des marchés

Depuis la matrice de scores :

- **1X2** : sommer les probabilités des scores correspondants.
- **Double chance** (1X, 12, X2) : sommes agrégées — marché à forte probabilité,
  utile pour les jambes « sécurisées ».
- **Draw No Bet (DNB)** : retirer le nul et renormaliser.
- **BTTS** (les deux marquent) : P(dom ≥ 1 et ext ≥ 1).
- **Over/Under** (0.5, 1.5, 2.5, 3.5) : sommer les scores au-dessus/au-dessous du
  seuil.
- **Score exact** : lecture directe de la matrice.

## 5. Ajustements motivationnels & contextuels

Appliquer des ajustements explicites et justifiés (jamais opaques) :

- Enjeu asymétrique (équipe déjà qualifiée/reléguée) → ajuster λ à la baisse pour
  l'équipe démotivée.
- Absences majeures (buteur, défenseur clé) → ajuster la force concernée.
- Fatigue / rotation probable → ajuster l'intensité attendue.

Documenter chaque ajustement et son ampleur.

## 6. Demandes « sûr à 90 % » : traitement honnête

L'utilisateur demande souvent des sélections « à ~90 % de chance de passer, peu
importe la cote ». Traiter ainsi, sans tromper :

- Identifier les **jambes à haute probabilité** que le modèle soutient réellement :
  double chance sur un fort favori, over 0.5, DNB sur un favori net, etc.
- Être explicite : **90 % n'est pas une garantie** — c'est ~1 échec sur 10. Et le
  marché cote ces événements très bas (souvent 1.08–1.15), donc « peu importe la
  cote » implique un gain unitaire faible et un risque de ruine si on empile les
  mises.
- Ne jamais étiqueter « 90 % » une sélection que le modèle ne soutient pas à ce
  niveau. La confiance affichée doit correspondre à la proba calibrée.
- Rappeler que sur ce type de paris, ce sont la **calibration** et le **volume** qui
  paient, pas un ticket isolé « sûr ».

## 7. Devigging, value & combinés

- Retirer la marge du bookmaker des cotes 1X2 (et annexes) pour la proba implicite
  « juste » (Shin par défaut ; la cote de référence idéale est Pinnacle).
- `edge = p_modèle − p_marché_dévigée` → value bet si edge positif robuste.
- **Combinés** : attention à la corrélation entre jambes (un même match : victoire +
  over sont corrélés). Les probabilités d'événements corrélés **ne se multiplient
  pas** comme des indépendants — calculer la proba conjointe directement dans la
  matrice de scores (ex. « 1 + over 2.5 » = somme des cases dom > ext et total ≥ 3). Chaque jambe
  ajoutée réduit fortement la probabilité globale : viser le meilleur compromis
  proba/rapport, pas le combiné le plus long.
- Value seulement si EV ≥ 5 % ; dimensionner via Kelly fractionné (¼), plafonné
  (ex. 2 % de bankroll par pari).
- Après le match : enregistrer la cote de clôture et calculer le CLV.

## 8. Format de sortie football

Suivre le gabarit de `SKILL.md` :

- Par match : λ dom/ext, top scores exacts, probas des marchés clés.
- Tableau value : marché | proba modèle | cote | proba marché dévigée | edge.
- Sélections « haute confiance » avec proba calibrée honnête (pas d'étiquette
  « 90 % » gratuite).
- Combinés proposés avec note de corrélation et mise (% bankroll).
- **Confiance & réserves** : calibration, incertitudes (compos, motivation) et rappel
  que proba ≠ certitude (carton, penalty, contre du hasard restent hors modèle).

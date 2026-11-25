# Diagnostic & corrections

## 1. Grille de lecture du rapport

| Signal | Seuil de sérieux | Lecture |
|---|---|---|
| Résolus < 50 (par discipline/marché) | — | Aucune correction. Continuer à journaliser. |
| ECE marqué « NON fiable » | < 80 % des bins remplis | Réduire `--bins` (ex. 5) ou attendre. Ne pas conclure. |
| Écart d'un bin de calibration | |écart| > 2 × √(p(1−p)/n) et même signe sur 2 revues | Biais probable sur cette zone de probas. |
| Réussite ≠ proba moyenne | écart > 2 × √(p̄(1−p̄)/N) | Sur- ou sous-confiance globale. |
| Brier nouvelle version vs ancienne | hors de l'IC95 bootstrap de l'ancienne | Amélioration réelle ; sinon équivalent. |
| CLV glissant 50 paris | < +1 % | Pause et audit : le marché ne valide plus l'edge. |
| ROI | n'importe quel signe sur < 300 paris | Surtout du bruit ; ne pas piloter dessus. |

## 2. Formes de biais et corrections

- **Sur-confiance** (favoris trop hauts, outsiders trop bas ; courbe sous la diagonale
  aux extrêmes) → recalibration par température : p' = σ(logit(p) / T), T > 1.
  Ajuster T sur la moitié ancienne, valider sur la moitié récente.
- **Sous-confiance** → même formule, T < 1.
- **Biais localisé** (une zone de probas) → Platt (sigmoïde a·logit(p)+b) si n ≤ 500,
  isotonique si n > 500.
- **Biais sur une issue précise** (ex. nul sous-estimé en foot) → vérifier l'ECE par
  classe ; corriger le ρ de Dixon-Coles ou ajouter une inflation diagonale, puis valider.
- **Dévigage inadapté** (edges systématiques sur outsiders qui perdent) → passer de la
  méthode multiplicative à Shin ou power.
- **Variable surpondérée** (erreurs corrélées à une variable) → réduire son poids d'un
  cran, une variable à la fois.

## 3. Biais fréquents par discipline

- **Hippisme** : biais favori/outsider des cotes PMU (outsiders surjoués) ; surpondération
  de la dernière course ; terrain et corde mal pris en compte ; non-partants tardifs.
- **Football** : nuls sous-estimés par Poisson simple ; avantage du terrain surestimé
  (il a baissé depuis 2020) ; matchs de fin de saison à enjeu asymétrique.
- **Tennis** : Elo non spécifique à la surface ; fatigue (enchaînement de tournois) ;
  abandons/forfaits.

## 4. Résultats négatifs à connaître (sports-forecasting-platform)

Sur des backtests de tournois internationaux, ces raffinements n'ont **pas** apporté
d'amélioration significative : inflation diagonale des nuls, calibration bêta,
pondération par enjeu du match, mutualisation bayésienne hiérarchique, valeur
marchande des effectifs. Les traiter comme des hypothèses à tester, pas des leviers acquis.

## 5. Changelog type

```
## 1.1.0 — 2026-12-10
Biais : sur-confiance sur les favoris > 70 % (écart −0.09 sur 64 pronostics, 2 revues).
Changement : température T = 1.15 appliquée aux probas finales (references/football.md).
Validation hold-out (40 pronostics récents) : Brier 0.231 → 0.219 (IC95 ancien 0.222–0.241).
Décision : appliqué. Rollback : retirer la ligne T.
```

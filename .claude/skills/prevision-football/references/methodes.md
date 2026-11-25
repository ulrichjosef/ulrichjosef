# Méthodes — détail et leçons de sports-forecasting-platform

## λ depuis les xG (sans historique de résultats)
1. Moyennes ligue : xG_moy_dom, xG_moy_ext (par match).
2. Force d'attaque A_t = xG créés / match ÷ moyenne ligue ; défense D_t = xG concédés / match ÷ moyenne ligue.
   Pondérer les matchs récents (demi-vie ~ 10–15 matchs) et ajuster par la force de l'adversaire.
3. λ_dom = A_dom × D_ext × xG_moy_dom ; λ_ext = A_ext × D_dom × xG_moy_ext.
4. Mélange prudent avec le marché si les données sont minces : la plateforme combine
   modèle et marché (« blender ») plutôt que de faire confiance au modèle seul.

## Dixon-Coles
Correction τ des cases 0-0, 1-0, 0-1, 1-1. ρ typiquement entre −0.15 et 0 en club.
ρ < 0 augmente 0-0 et 1-1 (sous-estimés par Poisson simple).

## Poisson bivarié diagonal-inflaté (DIBP)
grid = (1−π)·BP + π·J(k;θ) sur la diagonale, J(k;θ) = (1−θ)θ^k.
Utile pour sur-représenter les nuls. **Résultat de la plateforme : pas de gain
significatif** sur Coupe du monde / Euro / Copa — garder π = 0 sauf preuve par backtest.

## Calibration (règles de la plateforme)
- n ≤ 500 échantillons → Platt (sigmoïde) ; n > 500 → isotonique (l'isotonique sur-apprend en dessous).
- Mesurer l'ECE **par classe** (1, X, 2 séparément) : un modèle bon sur 1 et 2 mais
  faux de 5 points sur le nul peut afficher un bon ECE global et perdre de l'argent avec Kelly.
- ECE non fiable si < 80 % des bins sont remplis : réduire le nombre de bins ou attendre plus de données.
- Rapporter le Brier **avec intervalle de confiance bootstrap** : deux modèles dont les IC se
  chevauchent ne sont pas significativement différents.

## Validation
- Walk-forward : chaque date d'entraînement strictement antérieure à chaque date de test.
- Empilement (stacking) en out-of-fold imbriqué : le méta-modèle ne voit jamais de match futur.
- Pré-enregistrer les objectifs (ex. Brier 1X2 ≤ 0.21, ECE ≤ 0.05) et publier le résultat
  même s'il échoue (« below-gate ») — c'est ce qui rend l'évaluation honnête.
- Résultats négatifs documentés par la plateforme : inflation diagonale, calibration bêta,
  pondération par enjeu, mutualisation bayésienne hiérarchique et valeur marchande des effectifs
  n'ont apporté **aucune amélioration significative**. Ne pas les présenter comme des leviers sûrs.

## CLV
CLV % = (cote_prise / cote_juste_clôture − 1) × 100, cote juste = clôture dévigée (Pinnacle idéalement).
Comparer à la cote brute de clôture gonfle artificiellement le CLV (erreur n°1).
Moyenne glissante sur 50 paris < +1 % → pause et audit.

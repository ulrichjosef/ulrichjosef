---
name: prevision-football
description: >-
  Prévision probabiliste de matchs de football avec outils exécutables :
  modèle de buts Dixon-Coles / Poisson bivarié (avec option d'inflation des nuls),
  ajusté sur un historique avec pondération temporelle et sans fuite de données ;
  dérivation de tous les marchés (1X2, double chance, DNB, BTTS, over/under,
  handicaps, scores exacts) ; dévigage des cotes (multiplicatif, power, Shin) ;
  détection de value avec seuil d'EV ; mise Kelly fractionnée plafonnée ; CLV
  (closing line value) ; gel SHA-256 des pronostics avant le match ; rapport de
  calibration (Brier + IC bootstrap, ECE avec contrôle de remplissage des bins,
  ROI, alerte CLV). À utiliser dès qu'il faut CALCULER des probabilités de match
  de foot, des cotes justes, un edge ou une mise, figer un pronostic, ou évaluer un
  journal de pronostics football. Complète `pronostics-value` (méthode générale)
  et `pronostics-apprentissage` (boucle d'amélioration).
---

# Prévision Football — calculs exécutables

Méthodes reprises du projet open source **sports-forecasting-platform**
(K. Beltrán, licence MIT, installé dans `sports-forecasting-platform/` de ce dépôt),
réécrites en scripts Python **standard, sans dépendance**, pour être lancées
n'importe où. Les scripts sont dans `scripts/` de ce skill ; appelle-les avec
`python3 <chemin-du-skill>/scripts/<script>.py`.

## Règle de base : honnêteté probabiliste

- Toute sortie est une **probabilité**, jamais une certitude. Un 80 % perd 1 fois sur 5.
- La plateforme d'origine a publié ses propres résultats : Brier 1X2 ≈ 0.21–0.22 sur
  135 matchs internationaux, **sous ses propres objectifs** de calibration. C'est le
  niveau réaliste d'un bon modèle : à rappeler quand l'utilisateur attend du « sûr ».
- Le meilleur indicateur précoce d'un vrai edge est le **CLV**, pas le taux de réussite.

## Pipeline

### 1. Espérances de buts (λ)
- **Avec un historique** (CSV `date,home,away,home_goals,away_goals[,neutral]`) :
  ```bash
  python3 scripts/match_model.py fit --csv resultats.csv --home "Lens" --away "Nice" \
      --as-of 2026-11-29 --half-life-days 180
  ```
  Ajuste attaque/défense/avantage du terrain par MLE Poisson pondéré
  (demi-vie exponentielle), puis le ρ de Dixon-Coles. **Seuls les matchs
  antérieurs à `--as-of` sont utilisés** (pas de fuite). `--neutral` pour terrain
  neutre (tournois). Moins de 15 matchs par équipe → avertissement, élargir l'incertitude.
- **Sans historique exploitable** : estimer λ à partir des xG/xGA récents
  (pondérés adversaire et récence, cf. `references/methodes.md`), puis :
  ```bash
  python3 scripts/match_model.py grid --lambda-home 1.55 --lambda-away 1.05 --rho -0.08
  ```
- Compétition à forte proportion de nuls (phases de poules, matchs fermés) :
  ajouter `--pi-diag 0.05 --theta-diag 0.3` (Poisson bivarié diagonal-inflaté).
  Note : sur les tests de la plateforme, ce raffinement n'a **pas** amélioré
  significativement le Brier — à n'utiliser que si un backtest le justifie.
- Ajustements contextuels (absences, motivation, rotation) : modifier λ
  **explicitement** et documenter l'ampleur, jamais en silence.

### 2. Marchés
La sortie JSON contient 1X2, double chance, DNB, BTTS, over/under 0.5–4.5,
handicaps ±1 et le top 10 des scores exacts, tous dérivés de la même matrice
(donc cohérents entre eux).

### 3. Value et mise
```bash
python3 scripts/value.py --odds 1=2.10 X=3.40 2=3.70 --model 1=0.52 X=0.26 2=0.22 \
    --bankroll 1000 --kelly 0.25 --cap 0.02 --min-edge 0.05 --method shin
```
- Dévigage **Shin** par défaut (corrige le biais favori/outsider) ; `power` ou
  `multiplicative` disponibles. Résultats vérifiés identiques à `penaltyblog`.
- Value seulement si **EV = p × cote − 1 ≥ 5 %** (seuil par défaut de la plateforme).
- Mise = Kelly × fraction (¼ par défaut), **plafonnée** (2 % de bankroll par défaut).
- Combinés : les jambes d'un même match sont corrélées — calculer la probabilité
  conjointe dans la matrice de scores (ex. « 1 + over 2.5 » = somme des cases
  i>j et i+j>2), jamais par multiplication.

### 4. Gel avant le match
```bash
python3 scripts/lock.py create --input pronostics.json --out lock_2026-11-29.json
python3 scripts/lock.py verify --lock lock_2026-11-29.json
```
Empreinte SHA-256 horodatée : prouve que les probabilités n'ont pas été retouchées
après coup. Faire un lock pour tout pronostic qui sera évalué.

### 5. Après le match : CLV et calibration
```bash
python3 scripts/value.py clv --taken 2.10 --selection 1 --closing 1=1.95 X=3.50 2=4.10
python3 scripts/calibration_report.py --journal journal.jsonl --discipline football
```
- CLV = cote prise × proba juste de clôture − 1. Positif = on a battu le marché.
- Rapport : Brier + IC95 bootstrap, log-loss, ECE (marqué **non fiable** si < 80 %
  des bins sont remplis), courbe de fiabilité, ROI, CLV glissant sur 50 paris
  avec **alerte « pause & audit » si < +1 %**.
- Le journal suit le schéma de `pronostics-apprentissage` (ajouter `cote_cloture`
  ou `clv_pct` pour le suivi CLV).

## Format de sortie

```
# [Match] — Prévision
λ dom / ext, ρ, source (historique n matchs / xG) et ajustements appliqués
Tableau : marché | p modèle | cote | p marché dévigée (Shin) | EV | value | mise
Top 5 scores exacts
Lock : sha256 (si pronostic gelé)
Confiance & réserves : taille d'échantillon, données manquantes, aléa résiduel
```

## Utiliser la plateforme complète

Pour l'entraînement des ensembles XGBoost/CatBoost/LightGBM, le walk-forward
complet et les alertes Telegram, voir `references/plateforme.md` (nécessite des
clés API, non fournies).

## Jeu responsable

Analyse et recherche, pas conseil financier. Ne miser que ce dont la perte est sans
conséquence ; ne jamais augmenter les mises pour « se refaire ».

---
name: horse-racing-rf-betting
description: Modèle random forest de prédiction hippique (gagnant / placé top 3) avec sélection de variables et backtest d'une stratégie de mise à mise fixe (gain net, ROI). À utiliser pour entraîner ou évaluer un modèle de pronostic sur un historique de courses (CSV une ligne par cheval par course), comparer stratégie « classifieur » et stratégie « value bet », ou reprendre la méthode du projet HKJC Horse-Racing-Prediction.
---

# Horse racing — Random Forest + stratégie de mise

Skill tiré du projet « Horse-Racing-Prediction---Optimized-Gambling-Strategy »
(données Hong Kong Jockey Club, ~10 000 lignes, 98 variables brutes). Le README d'origine et les
deux notebooks sont dans `references/`.

## Méthode d'origine (résumé)

1. **Scraping** HKJC : liste des chevaux → page de chaque cheval → historique de courses
   (`references/web-scrap-and-eda.ipynb`).
2. **Prétraitement** : suppression des variables connues seulement après la course
   (position en course, LBW, temps), `Gear` → nombre d'équipements, one-hot sur
   `G`, `RaceClass`, `RC`, `Track`, `Course`, `Country of Origin` ; drop `Trainer`, `Jockey`.
3. **Cibles** : `top1` (gagnant) et `top3` (placé).
4. **Modèles** (`references/feature-selection-and-model-comparison.ipynb`) :
   RF naïf (64 variables) → variables d'importance par permutation > 0,01 →
   ajout progressif des variables par importance, on garde le meilleur nombre →
   grid search (`n_estimators`, `max_features`, `min_samples_split`). Un MLP a aussi été testé.
5. **Gain** : mise 10 $ sur chaque cheval prédit 1 ; net = (cote − 1) × 10 si juste, −10 sinon.

Résultats annoncés : top3 ≈ 76 % d'accuracy, +41 084 HKD sur 2 936 lignes de test ;
top1 ≈ 0 de gain (accuracy 90 % ≈ taux de base, le modèle ne fait presque rien).

## ⚠️ Limites à rappeler systématiquement

- **Fuite de données** reconnue par les auteurs : `Season Stakes*` est la valeur de la saison
  *en cours*, qui inclut déjà les gains de la course prédite. C'est la 2ᵉ variable la plus
  importante → le profit annoncé est très probablement surestimé.
- **Split aléatoire par ligne** : des chevaux d'une même course se retrouvent en train et en test,
  et le futur sert à prédire le passé.
- **Accuracy trompeuse** : sur `top1` le taux de base est ~92 % de 0.
- Aucun résultat de ce projet ne garantit un gain réel ; toujours présenter les sorties comme
  un backtest, avec la mise totale et le ROI, pas seulement le net.

## Utilisation du script

`scripts/rf_betting.py` reprend la méthode en corrigeant ces points : split **chronologique
par course**, exclusion explicite des colonnes fuyantes, sélection de variables sur un jeu de
validation séparé, AUC + taux de base, et deux stratégies.

```bash
pip install scikit-learn pandas
python scripts/rf_betting.py --csv courses.csv \
  --race-col N_RaceIndex --date-col Date \
  --target top3 --odds-col top3Winodd \
  --exclude "Season Stakes*" "Pla." "Finish Time" horse top1 \
  --select forward --strategy value --margin 0.05 --one-per-race \
  --out bets.csv
```

Options clés :
- `--strategy classifier --threshold 0.5` : stratégie d'origine (miser si prédit 1).
- `--strategy value --margin m` : miser si `proba × cote > 1 + m` (value bet).
- `--one-per-race` : une seule mise par course (meilleur edge).
- `--select importance|forward` : sélection par importance de permutation (seuil
  `--importance-min`) ou ajout progressif jusqu'au meilleur AUC de validation.
- `--exclude` : **toujours** y mettre les colonnes post-course et les autres cibles.

Sortie : JSON (`bets`, `wins`, `hit_rate`, `staked`, `net`, `roi`, `auc`, `base_rate`,
variables retenues) et, avec `--out`, le CSV du test avec `proba` et `bet`.

## Démarche conseillée

1. Vérifier que chaque variable est connue **avant** le départ ; sinon `--exclude`.
2. Lancer d'abord sans sélection pour avoir une référence, puis `--select forward`.
3. Comparer `classifier` et `value`, avec et sans `--one-per-race`.
4. Lire le ROI et le nombre de mises, pas l'accuracy. Un ROI positif sur peu de mises
   ou une seule période n'est pas significatif : refaire sur plusieurs fenêtres.
5. Ce skill peut se combiner avec les skills de pronostics existants
   (`pronostics-value`, `analyse-pronostics`) pour l'étape de sélection des paris.

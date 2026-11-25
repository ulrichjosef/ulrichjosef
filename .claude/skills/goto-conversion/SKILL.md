---
name: goto-conversion
description: Convert bookmaker odds (decimal or American) into true implied probabilities by removing the bookmaker margin with the goto_conversion method (favourite-longshot bias aware) or the efficient Shin method. Use for sports betting / pronostics, value-bet detection, fair odds, or Kaggle-style outcome prediction from odds.
---

# goto_conversion – cotes → probabilités

Méthode de Kaito Goto (MIT, v4.0.3) : réduit toutes les probabilités inverses (1/cote)
du même nombre d'erreurs-types, ce qui corrige le biais favori/outsider mieux qu'une
normalisation multiplicative. Inclut aussi `efficient_shin_conversion` (Shin analytique)
et `zero_sum` (variante marchés boursiers).

## Utilisation rapide (CLI, aucune dépendance)

```bash
python3 ~/.claude/skills/goto-conversion/scripts/goto_conversion.py 1.85 3.60 4.20
```
Options : `--american` (cotes US), `--shin`, `--total 1.0`, `--multiplicative-fallback`
(si la marge est nulle/négative, sinon erreur).

Le chemin du script est `scripts/goto_conversion.py` dans le dossier de ce skill
(`.claude/skills/goto-conversion/` dans le projet, ou `~/.claude/skills/goto-conversion/`).

## En Python

```python
import sys; sys.path.insert(0, "<dossier du skill>/scripts")
from goto_conversion import goto_conversion, efficient_shin_conversion, zero_sum
goto_conversion([1.85, 3.60, 4.20])          # liste ou np.array de cotes décimales
goto_conversion([-150, 130], isAmericanOdds=True)
```

## Règles
- Toutes les cotes décimales doivent être > 1.0 et au moins 2 issues (marché complet).
- Passer toutes les issues d'un même marché (1X2 = 3 cotes) chez le même bookmaker.
- Value bet : comparer la proba goto (cote juste = 1/proba) à la meilleure cote disponible ;
  edge = proba × cote − 1.
- Si erreur « imprudent odds » (marge ≤ 0, ex. cotes de plusieurs bookmakers), utiliser
  `--multiplicative-fallback`.

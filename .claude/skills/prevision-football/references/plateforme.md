# Utiliser la plateforme complète (sports-forecasting-platform)

Installée dans `sports-forecasting-platform/` à la racine de ce dépôt (Python 3.12, uv).

```bash
cd sports-forecasting-platform
uv sync --extra dev                      # dépendances
uv run pytest -m "not requires_data" -q  # tests hors-ligne
uv run python -m bip.pipeline --dry-run  # pipeline complet avec dépendances simulées
cp env.example .env                       # puis renseigner ses propres clés
```

Clés nécessaires pour un usage réel (voir `env.example`) : API-Football, The Odds API,
(Sportmonks optionnel), Supabase/PostgreSQL, bot Telegram, et Anthropic pour la revue LLM
optionnelle. Ne jamais committer `.env`.

Modules utiles :
- `src/bip/clv/odds_math.py` — dévigage proportionnel ; `clv/recorder.py` — CLV.
- `src/bip/train/` — walk-forward, stacking, calibration Platt/isotonique, CLI `python -m bip.train fit`.
- `src/bip/evaluation/tournaments/` — Elo, Poisson, Dixon-Coles, DIBP, locks Coupe du monde 2026.
- `src/bip/evaluation/tournaments/backtest/calibration_metrics.py` — ECE par classe + contrôle de remplissage.

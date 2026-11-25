---
name: horse-racing-analytics
description: Leakage-safe horse-racing research lab (Horse Race Formula Lab) — build prior-only features, score runners (glass-box rule scorer + LightGBM LambdaRank), de-vig odds (multiplicative/power/Shin), compute edge/EV/fractional Kelly, backtest chronologically against a market-favourite baseline, and explain races in plain language. Use when the user wants to model, backtest or explain horse races, evaluate betting strategies, compute fair odds / value, or run the formula-lab pipeline on synthetic or Kaggle HK racing data.
---

# Horse Racing Analytics (Formula Lab)

The full project lives in `formula-lab/` next to this file. All commands run
from that folder.

## Setup (once per session)

```bash
cd <this skill dir>/formula-lab
pip install -r requirements.txt        # lightgbm optional: falls back to sklearn
```

## Core workflows

1. **Run the pipeline** (synthetic data if `data/raw/` is empty):
   ```bash
   python scripts/run_pipeline.py --config config/config.yaml
   python scripts/run_pipeline.py --objective classification --devig shin --edge 0.07
   python scripts/run_pipeline.py --n-races 1500 --report artifacts/report.md --save-model artifacts/model.joblib
   ```
   Flags: `--raw-dir`, `--objective ranking|classification`, `--include-market`,
   `--devig multiplicative|power|shin`, `--edge`, `--train-frac`, `--n-races`.

2. **Real data**: put Kaggle `gdaley/hkracing` `races.csv` + `runs.csv` in
   `data/raw/` (or `python scripts/download_kaggle.py` with a Kaggle token).
   The loader picks them up automatically and reports `Data source: kaggle`.

3. **Use from Python** (for custom races / explanations):
   ```python
   from src.pipeline import run_pipeline
   from src.llm.explain import summarize_race, compare_horses, explain_prediction
   from src.probability import probability as prob   # devig, EV, Kelly, price_race
   res = run_pipeline(synthetic_kwargs={"n_races": 800})
   print(res.summary()); res.priced_test.head()
   ```
   `price_race(df, devig_method=...)` prices any race frame that has
   `win_odds` and `model_prob` columns. `src/llm/assistant.py` + `rag.py` give a
   retrieval-based race assistant (TF-IDF offline; Claude if `ANTHROPIC_API_KEY`
   is set).

4. **Tests**: `python -m pytest tests -q` (leakage + probability maths).

## Reference docs (read as needed)

`formula-lab/docs/`: `DATA_STRUCTURE.md`, `MODEL_DESIGN.md`,
`PROBABILITY_LOGIC.md`, `BACKTESTING.md`, `LLM_FEATURES.md`,
`ASSUMPTIONS_LIMITATIONS.md`.

## Rules when answering

- Never let post-race columns (result, finish time, dividends) into features;
  respect `src/data/schema.py` `LEAKAGE_COLS`.
- Always compare strategies against the `market_favourite` baseline and report
  out-of-sample numbers only. Results on synthetic data demonstrate the code,
  not profitability — say so.
- Takeout is ~17–22%; present EV/Kelly outputs as research, not betting advice.

## Install notes (changes vs. the uploaded zip)

- `src/models/scoring.py` and `src/models/ranker.py` were **missing** from the
  zip (upstream `.gitignore` had `models/`, which swallowed `src/models/`).
  They were rebuilt from `docs/MODEL_DESIGN.md`; `.gitignore` now uses
  `/models/` so they are kept.
- `load_dataset(cache_synthetic=...)` now defaults to `False`: before, synthetic
  data was written into `data/raw/` and later runs mislabelled it as "kaggle"
  and ignored `--n-races`.

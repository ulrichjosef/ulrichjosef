---
name: horse
description: Work on the horse-racing probabilities project in horse/ (UK & Irish racing data ingestion, feature store, LightGBM win model, forecast correction, Matchbook 11:00 paper-betting record, workbench UI). Use for any task about this horse racing model, its features, CLV/ROI research, the paper record or the workbench.
---

# Horse racing probabilities (`horse/`)

The project lives in `horse/` at the repository root. Before any change:

1. Read `horse/README.md` (operating guide), `horse/CLAUDE.md` (hard rules) and
   `horse/CONTINUATION.md` (current handoff).
2. Before proposing a new feature or data source, read `horse/docs/ALREADY_TRIED.md`.
3. Module map: `horse/docs/PROJECT_INVENTORY.md`.

Run commands from `horse/` (the project root), not the repository root.

## Hard rules (summary — full text in `horse/CLAUDE.md`)

- No leakage: past-form features must exclude the current race; use
  `groupby(...).transform(lambda x: x.cummax().shift(1))`, never a global `.shift(1)`.
- Bet thresholds, each-way band and settlement PnL live only in `src/bet_settlement.py`.
- Horse/track/off-time joins use the keys in `src/utils.py`.
- Any module that can change a feature value is registered in `_FE_SOURCE_FILES`
  (`src/featured_dataset.py`) or exempted in `FE_SIGNATURE_EXEMPT`.
- Check the instrument before trusting a number: `scripts/project_status.py`.
- Walk-forward evaluation uses `src/wf_eval.py`; read CLV via `src.clv.summarise_clv`
  (median / geometric), never the plain mean of `taken_odds / bsp`.
- LightGBM is the only model framework.
- Nothing places real bets; don't touch `src/matchbook`, `src/correction` or the
  store on a racing morning (07:50 until the last race).

## Environment

- Built for Windows: Python 3.14 in `.venv`, from `uv.lock` via
  `scripts/tooling.ps1 venv` (`[tool.uv] environments` is restricted to win32).
- `data/` and `models/` are local and gitignored, so the live pipeline, store and
  models are not in this repository; only code, docs and tests are.

## Key commands (Windows, from `horse/`)

| Stage | Command |
|---|---|
| Status check | `.venv\Scripts\python.exe scripts/project_status.py` |
| Sync sources | `python -m src.ingestion --sync 14 --results-only` |
| Win model | `python -m src.modelling --help` |
| Correction | `python -m src.correction status` |
| Paper record | `python -m src.matchbook day --refresh` / `python -m src.matchbook summary` |
| Workbench | `python scripts/workbench.py` then http://127.0.0.1:8765 |
| Tests | `scripts/tooling.ps1 test` (quick), `scripts/tooling.ps1 test -TestPath tests` (full) |

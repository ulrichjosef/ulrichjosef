---
name: football-predictions
description: Fetch daily football (soccer) match predictions and odds from API-Football (1X2, Over/Under 2.5, GG/NG, short tips like 1 / X2 / 12, value bets where probability x odds > 1), grade past predictions against final scores, and render the neon VIP dashboard. Use when the user asks for today's football predictions, pronostics foot, value bets, results tracking or accuracy history.
---

# Football Predictions (API-Football)

Self-contained pipeline: Python fetchers write JSON into `data/`, and a static
dashboard (`index.html`, `script.js`, `style.css`, `assets/`) reads it.

## Requirements
- Env var `API_FOOTBALL_KEY` (key from api-football.com / api-sports.io).
  Never hardcode it. In a cloud session, ask for it as a network credential for
  host `v3.football.api-sports.io` (header `x-apisports-key`).
- `pip install requests` (the other entries in `requirements.txt` are optional).

## Commands (run from this skill's directory)
- Today's predictions (up to 5 matches, ~15 API calls max) →
  `data/predictions_today.json` + `data/predictions.json`:
  `python scripts/fetch_predictions.py`
- Grade pending matches and update accuracy log `data/history.json`
  (keeps last 100, tracks `total_1x2` / `correct_1x2`):
  `python scripts/fetch_results.py`
- View the dashboard: serve the folder (`python -m http.server 8000`) and open
  `index.html`, or publish it as an artifact.

## Data shape (each match in `matches`)
`fixture_id, date, league, home_team, away_team, short_tip, percent_home/draw/away,
prediction_1x2, prediction_gg, prediction_ou, advice, odds{home,draw,away},
status (Pending|In Play|Finished), home_goals, away_goals, correct_1x2`.

## How to answer the user
1. Run the fetcher (or read the existing JSON if no key / offline, and say the data date).
2. Present a table: match, league, short tip, probabilities, odds, GG/NG, O/U.
3. Flag value bets: implied edge = probability(%) / 100 x odds > 1.0; highlight the
   highest-EV pick as "bet of the day".
4. Report historical accuracy from `history.json` (correct_1x2 / total_1x2).
5. Always add: predictions are informational, not financial advice; bet responsibly.

## Automation
`workflows/` holds the original GitHub Actions (06:17 UTC predictions, 23:22 UTC
results). To use them, copy into a repo's `.github/workflows/` and add the
`API_FOOTBALL_KEY` repository secret.

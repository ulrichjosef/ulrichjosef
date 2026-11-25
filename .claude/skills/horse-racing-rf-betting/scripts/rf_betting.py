#!/usr/bin/env python3
"""Random-forest horse-racing model + flat-stake betting backtest.

Adapted from the "Horse-Racing-Prediction---Optimized-Gambling-Strategy" project
(HKJC data, RF on top1/top3 flags, net = (odds-1)*stake if right, -stake if wrong).

Improvements over the original notebooks:
  * chronological split by race (no random row split -> no same-race leakage)
  * --exclude to drop leaky columns (e.g. current-season stakes)
  * optional forward feature selection on permutation importance
  * two strategies: "classifier" (bet when predicted 1, original) and
    "value" (bet when p * odds > 1 + margin)

Input: one row per horse per race. Needs a race id column, a target column
(0/1), an odds column and numeric/categorical feature columns.

Example:
  python rf_betting.py --csv data.csv --race-col N_RaceIndex --date-col Date \
      --target top3 --odds-col top3Winodd --exclude "Season Stakes*" Pla. "Finish Time" \
      --select forward --strategy value --margin 0.05
"""
import argparse
import json
import sys

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score, roc_auc_score


def chrono_split(df, race_col, date_col, test_size):
    order = df[[race_col] + ([date_col] if date_col else [])].drop_duplicates(race_col)
    if date_col:
        order = order.assign(_d=pd.to_datetime(order[date_col], errors="coerce", dayfirst=True)).sort_values("_d")
    races = order[race_col].tolist()
    cut = int(len(races) * (1 - test_size))
    train_races = set(races[:cut])
    m = df[race_col].isin(train_races)
    return df[m], df[~m]


def make_rf(args):
    return RandomForestClassifier(n_estimators=args.n_estimators, min_samples_leaf=args.min_samples_leaf,
                                  max_features="sqrt", n_jobs=-1, random_state=args.seed,
                                  class_weight="balanced_subsample" if args.balanced else None)


def backtest(test, proba, args):
    odds = test[args.odds_col].astype(float).values
    y = test[args.target].astype(int).values
    if args.strategy == "classifier":
        bet = proba >= args.threshold
    else:
        bet = proba * odds > 1 + args.margin
    if args.one_per_race:  # keep only the best-edge horse per race
        edge = pd.Series(np.where(bet, proba * odds, -np.inf), index=test.index)
        best = edge.groupby(test[args.race_col]).transform("max")
        bet = bet & (edge.values == best.values)
    net = np.where(bet, np.where(y == 1, (odds - 1) * args.stake, -args.stake), 0.0)
    n_bets = int(bet.sum())
    staked = n_bets * args.stake
    return {
        "races_test": int(test[args.race_col].nunique()),
        "bets": n_bets,
        "wins": int((bet & (y == 1)).sum()),
        "hit_rate": round(float((bet & (y == 1)).sum() / n_bets), 4) if n_bets else None,
        "staked": staked,
        "net": round(float(net.sum()), 2),
        "roi": round(float(net.sum() / staked), 4) if staked else None,
    }, bet


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--csv", required=True)
    p.add_argument("--race-col", required=True)
    p.add_argument("--date-col")
    p.add_argument("--target", required=True, help="0/1 column, e.g. top1 or top3")
    p.add_argument("--odds-col", required=True, help="decimal odds paid for the target bet")
    p.add_argument("--features", nargs="*", help="feature columns (default: all other columns)")
    p.add_argument("--exclude", nargs="*", default=[], help="columns to drop (leaky/post-race)")
    p.add_argument("--select", choices=["none", "importance", "forward"], default="none")
    p.add_argument("--importance-min", type=float, default=0.01)
    p.add_argument("--max-features", type=int, default=30)
    p.add_argument("--strategy", choices=["classifier", "value"], default="value")
    p.add_argument("--threshold", type=float, default=0.5)
    p.add_argument("--margin", type=float, default=0.0)
    p.add_argument("--one-per-race", action="store_true")
    p.add_argument("--stake", type=float, default=10.0)
    p.add_argument("--test-size", type=float, default=0.2)
    p.add_argument("--n-estimators", type=int, default=500)
    p.add_argument("--min-samples-leaf", type=int, default=5)
    p.add_argument("--balanced", action="store_true")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--out", help="write test-set predictions/bets to this CSV")
    args = p.parse_args()

    df = pd.read_csv(args.csv)
    reserved = {args.race_col, args.target, args.odds_col} | ({args.date_col} if args.date_col else set())
    feats = args.features or [c for c in df.columns if c not in reserved | set(args.exclude)]
    X_all = pd.get_dummies(df[feats], dummy_na=False).apply(pd.to_numeric, errors="coerce").fillna(-1)
    df = df.join(X_all.add_prefix("__f_"))
    fcols = [c for c in df.columns if c.startswith("__f_")]

    train, test = chrono_split(df, args.race_col, args.date_col, args.test_size)
    if args.select != "none":
        # validation = last 20% of the training races, chronologically
        tr, va = chrono_split(train, args.race_col, args.date_col, 0.2)
        rf = make_rf(args).fit(tr[fcols], tr[args.target])
        imp = permutation_importance(rf, va[fcols], va[args.target], n_repeats=5,
                                     random_state=args.seed, scoring="roc_auc", n_jobs=-1)
        ranked = [fcols[i] for i in np.argsort(-imp.importances_mean)]
        if args.select == "importance":
            fcols = [c for c, v in zip(fcols, imp.importances_mean) if v > args.importance_min] or ranked[:5]
        else:
            best, best_auc, chosen = [], -1, []
            for c in ranked[: args.max_features]:
                chosen.append(c)
                m = make_rf(args).fit(tr[chosen], tr[args.target])
                auc = roc_auc_score(va[args.target], m.predict_proba(va[chosen])[:, 1])
                if auc > best_auc:
                    best_auc, best = auc, list(chosen)
            fcols = best
    model = make_rf(args).fit(train[fcols], train[args.target])
    proba = model.predict_proba(test[fcols])[:, 1]
    res, bet = backtest(test, proba, args)
    res.update({
        "features": [c[4:] for c in fcols],
        "accuracy@0.5": round(float(accuracy_score(test[args.target], proba >= 0.5)), 4),
        "auc": round(float(roc_auc_score(test[args.target], proba)), 4),
        "base_rate": round(float(test[args.target].mean()), 4),
    })
    print(json.dumps(res, indent=2, ensure_ascii=False))
    if args.out:
        o = test.drop(columns=[c for c in test.columns if c.startswith("__f_")]).copy()
        o["proba"], o["bet"] = proba, bet
        o.to_csv(args.out, index=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())

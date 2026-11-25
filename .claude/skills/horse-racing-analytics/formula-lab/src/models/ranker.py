"""
Learned ranker -- the main model, behind one ``RaceRanker`` interface.

* ``objective="ranking"`` (default): LightGBM LambdaRank, grouped by race, with
  relevance ``clip(field_size - result, 0, 31)`` so the winner ranks highest.
* ``objective="classification"``: LightGBM binary classifier on ``won``.

Raw outputs become within-race win probabilities that sum to 1 (softmax for the
ranker, renormalised ``predict_proba`` for the classifier). Without LightGBM it
falls back to sklearn's ``HistGradientBoostingClassifier`` on category codes.

Note: this module was reconstructed from docs/MODEL_DESIGN.md because the
upstream repository's ``.gitignore`` (``models/``) excluded ``src/models/``.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

try:  # optional dependency
    import lightgbm as lgb  # type: ignore
    _HAS_LGB = True
except Exception:  # pragma: no cover
    _HAS_LGB = False


@dataclass
class RankerConfig:
    objective: str = "ranking"  # "ranking" | "classification"
    n_estimators: int = 400
    learning_rate: float = 0.05
    num_leaves: int = 31
    min_child_samples: int = 20
    random_state: int = 7
    extra_params: dict = field(default_factory=dict)


def _group_softmax(scores: np.ndarray, groups: np.ndarray) -> np.ndarray:
    s = pd.Series(scores)
    g = pd.Series(groups)
    s = s - s.groupby(g).transform("max")
    e = np.exp(s)
    return (e / e.groupby(g).transform("sum")).to_numpy()


def _group_normalise(p: np.ndarray, groups: np.ndarray) -> np.ndarray:
    s = pd.Series(np.clip(p, 1e-12, None))
    return (s / s.groupby(pd.Series(groups)).transform("sum")).to_numpy()


class RaceRanker:
    def __init__(self, config: RankerConfig | None = None):
        self.config = config or RankerConfig()
        if self.config.objective not in ("ranking", "classification"):
            raise ValueError(f"unknown objective: {self.config.objective}")
        self.model = None
        self.feature_cols: list[str] = []
        self.categorical_cols: list[str] = []
        self._categories: dict[str, pd.Index] = {}
        self.backend = "unfitted"

    # ------------------------------------------------------------------ #
    def _prep(self, X: pd.DataFrame, codes: bool) -> pd.DataFrame:
        X = X[self.feature_cols].copy()
        for c in self.categorical_cols:
            X[c] = pd.Categorical(X[c].astype(object), categories=self._categories[c])
            if codes:
                X[c] = X[c].cat.codes
        return X

    def fit(self, bundle, train_idx) -> "RaceRanker":
        cfg = self.config
        self.feature_cols = list(bundle.feature_cols)
        self.categorical_cols = list(bundle.categorical_cols)
        Xall = bundle.X
        self._categories = {
            c: pd.Index(Xall[c].astype(object).dropna().unique()) for c in self.categorical_cols
        }
        idx = np.asarray(train_idx)
        # LambdaRank needs rows of a group to be contiguous.
        order = np.lexsort((bundle.groups.iloc[idx].to_numpy(), bundle.date.iloc[idx].to_numpy()))
        idx = idx[order]
        y_won = bundle.y.iloc[idx].to_numpy()

        if _HAS_LGB:
            X = self._prep(Xall.iloc[idx], codes=False)
            common = dict(
                n_estimators=cfg.n_estimators,
                learning_rate=cfg.learning_rate,
                num_leaves=cfg.num_leaves,
                min_child_samples=cfg.min_child_samples,
                random_state=cfg.random_state,
                verbose=-1,
                **cfg.extra_params,
            )
            if cfg.objective == "ranking":
                frame = bundle.frame.iloc[idx]
                field_size = frame["field_size"] if "field_size" in frame else frame.groupby(
                    bundle.groups.iloc[idx]
                )["horse_id"].transform("count")
                rel = np.clip(
                    (field_size - bundle.result.iloc[idx]).fillna(0).to_numpy(), 0, 31
                ).astype(int)
                grp = bundle.groups.iloc[idx]
                sizes = grp.groupby(grp, sort=False).size().to_numpy()
                self.model = lgb.LGBMRanker(objective="lambdarank", **common)
                self.model.fit(X, rel, group=sizes)
                self.backend = "lightgbm-lambdarank"
            else:
                self.model = lgb.LGBMClassifier(objective="binary", **common)
                self.model.fit(X, y_won)
                self.backend = "lightgbm-classifier"
        else:
            from sklearn.ensemble import HistGradientBoostingClassifier

            X = self._prep(Xall.iloc[idx], codes=True)
            self.model = HistGradientBoostingClassifier(
                max_iter=cfg.n_estimators,
                learning_rate=cfg.learning_rate,
                random_state=cfg.random_state,
            )
            self.model.fit(X, y_won)
            self.backend = "sklearn-hgb"
        return self

    def predict_proba(self, bundle, idx) -> pd.Series:
        if self.model is None:
            raise RuntimeError("RaceRanker is not fitted")
        idx = np.asarray(idx)
        groups = bundle.groups.iloc[idx].to_numpy()
        if self.backend == "lightgbm-lambdarank":
            raw = self.model.predict(self._prep(bundle.X.iloc[idx], codes=False))
            p = _group_softmax(np.asarray(raw, float), groups)
        elif self.backend == "lightgbm-classifier":
            raw = self.model.predict_proba(self._prep(bundle.X.iloc[idx], codes=False))[:, 1]
            p = _group_normalise(raw, groups)
        else:
            raw = self.model.predict_proba(self._prep(bundle.X.iloc[idx], codes=True))[:, 1]
            p = _group_normalise(raw, groups)
        return pd.Series(p, index=bundle.X.index[idx], name="model_prob")

    def feature_importance(self) -> pd.DataFrame:
        if self.model is None:
            raise RuntimeError("RaceRanker is not fitted")
        imp = getattr(self.model, "feature_importances_", None)
        if imp is None:  # sklearn HGB has no native importances
            imp = np.zeros(len(self.feature_cols))
        return (
            pd.DataFrame({"feature": self.feature_cols, "importance": imp})
            .sort_values("importance", ascending=False)
            .reset_index(drop=True)
        )

    def save(self, path: str) -> None:
        import joblib

        joblib.dump(self, path)

    @staticmethod
    def load(path: str) -> "RaceRanker":
        import joblib

        return joblib.load(path)

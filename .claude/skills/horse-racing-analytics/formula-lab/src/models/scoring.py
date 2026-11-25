"""
Glass-box rule scorer -- a transparent, training-free baseline.

For each race it z-scores every signal *within the race* (horses are only
compared with today's rivals), flips "lower-is-better" signals, takes a weighted
sum into ``rule_raw``, then emits a 0-100 ``rule_score`` (within-race percentile)
and a ``rule_prob`` (softmax over the field, sums to 1 per race).

Per-signal contributions are kept as ``contrib_<signal>`` columns so the
explanation layer can narrate *why* a horse scored as it did
(:func:`top_signals_for_runner`).

Note: this module was reconstructed from docs/MODEL_DESIGN.md because the
upstream repository's ``.gitignore`` (``models/``) excluded ``src/models/``.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from ..data import schema

# Positive weight = more is better. "Lower-is-better" signals are listed in
# LOWER_IS_BETTER and are sign-flipped after z-scoring, so weights stay positive.
DEFAULT_WEIGHTS: dict[str, float] = {
    "horse_win_rate": 1.0,
    "horse_place_rate": 0.8,
    "horse_form_win_3": 0.8,
    "horse_form_pos_3": 0.9,
    "rating_vs_field": 1.2,
    "jockey_win_rate": 0.7,
    "jockey_form_win_20": 0.4,
    "trainer_win_rate": 0.5,
    "weight_vs_field": 0.3,
    "draw_norm": 0.3,
    "horse_days_since": 0.2,
}

LOWER_IS_BETTER = {"horse_form_pos_3", "weight_vs_field", "draw_norm", "horse_days_since"}


@dataclass
class ScoringConfig:
    weights: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_WEIGHTS))
    temperature: float = 1.0  # softmax temperature for rule_prob


def _within_race_z(s: pd.Series, groups: pd.Series) -> pd.Series:
    g = s.groupby(groups)
    mu = g.transform("mean")
    sd = g.transform("std").replace(0, np.nan)
    return ((s - mu) / sd).fillna(0.0)


def _softmax_by_group(x: pd.Series, groups: pd.Series, temp: float) -> pd.Series:
    z = x / max(temp, 1e-9)
    z = z - z.groupby(groups).transform("max")
    e = np.exp(z)
    return e / e.groupby(groups).transform("sum")


def score_runners(frame: pd.DataFrame, config: ScoringConfig | None = None) -> pd.DataFrame:
    """Score every runner in ``frame`` (runner grain, must contain race_id).

    Returns a frame aligned to ``frame.index`` with ``rule_raw``,
    ``rule_score``, ``rule_prob`` and ``contrib_<signal>`` columns.
    """
    cfg = config or ScoringConfig()
    groups = frame[schema.RACE_KEY]
    out = pd.DataFrame(index=frame.index)
    raw = pd.Series(0.0, index=frame.index)
    for sig, w in cfg.weights.items():
        if sig not in frame.columns:
            continue
        vals = pd.to_numeric(frame[sig], errors="coerce").fillna(0.0)
        if sig == "horse_days_since":
            # 9999 marks a debut; cap so it does not dominate the z-score.
            vals = vals.clip(upper=365)
        z = _within_race_z(vals, groups)
        if sig in LOWER_IS_BETTER:
            z = -z
        contrib = w * z
        out[f"contrib_{sig}"] = contrib
        raw = raw + contrib
    out["rule_raw"] = raw
    out["rule_score"] = raw.groupby(groups).rank(pct=True) * 100.0
    out["rule_prob"] = _softmax_by_group(raw, groups, cfg.temperature)
    return out


def top_signals_for_runner(row: pd.Series, k: int = 3) -> list[tuple[str, float]]:
    """The ``k`` signals that moved this runner's rule score the most."""
    items = [
        (str(c)[len("contrib_"):], float(v))
        for c, v in row.items()
        if str(c).startswith("contrib_") and pd.notna(v)
    ]
    items.sort(key=lambda t: abs(t[1]), reverse=True)
    return items[:k]

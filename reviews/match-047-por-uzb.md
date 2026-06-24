# Match 047 Review: Portugal vs Uzbekistan

[Reviews index](README.md) | [简体中文](match-047-por-uzb.zh-CN.md) | [Prediction](../predictions/match-047-por-uzb.md)

## Result

- Final result: Portugal 5-0 Uzbekistan in Match 047.
- Predicted winner: POR.
- Actual winner: POR.
- Predicted scoreline: Portugal vs Uzbekistan 2-0.
- Review rating: partial.

## What Held Up

- Portugal's winner and clean-sheet direction were right.
- The model correctly treated Portugal's response pressure as the base match script.

## What Failed

- The favorite-margin tail was too low; 3+ and 4+ Portugal scorelines needed more weight.
- Heat and first-match caution were over-applied against a talent gap that widened after the first goal.

## Model Adjustment Notes

- When an elite favorite faces a lower-ranked opponent after a draw, raise the multi-goal win tail if the underdog must eventually chase.
- Calibration tag: `favorite_margin_underweighted`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021503
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/portugal-uzbekistan-highlights-match-report
- Verified at: 2026-06-24T22:20:00+08:00

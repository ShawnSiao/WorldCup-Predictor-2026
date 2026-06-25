# Match 050 Review: Morocco vs Haiti

[Reviews index](README.md) | [简体中文](match-050-mar-hai.zh-CN.md) | [Prediction](../predictions/match-050-mar-hai.md)

## Result

- Final result: Morocco 4-2 Haiti in Match 050.
- Predicted winner: Morocco.
- Actual winner: Morocco.
- Predicted scoreline: Morocco vs Haiti 3-0.
- Review rating: partial.

## What Held Up

- Morocco's winner and multi-goal favorite path were correct.
- The prediction captured Morocco's control and attacking volume.

## What Failed

- The clean-sheet assumption failed badly because Haiti converted two scoring moments.
- The model underweighted underdog transition and set-piece scoring resilience.

## Model Adjustment Notes

- Keep the favorite-margin tail, but separate 'favorite controls' from 'favorite keeps a clean sheet'.
- Calibration tags: `clean_sheet_overstated`, `underdog_resilience_underweighted`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021452
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/matchday-14-round-up-review-highlights
- Verified at: 2026-06-25T13:51:27+08:00

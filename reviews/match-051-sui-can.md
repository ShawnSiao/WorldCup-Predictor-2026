# Match 051 Review: Switzerland vs Canada

[Reviews index](README.md) | [简体中文](match-051-sui-can.zh-CN.md) | [Prediction](../predictions/match-051-sui-can.md)

## Result

- Final result: Switzerland 2-1 Canada in Match 051.
- Predicted winner: Draw.
- Actual winner: Switzerland.
- Predicted scoreline: Switzerland vs Canada 1-1.
- Review rating: wrong.

## What Held Up

- The one-goal, balanced-match script was accurate.
- Canada's scoring response was correctly kept live.

## What Failed

- The draw was overweighted and Switzerland's winner route was underweighted.
- The model overread shared-point incentive in a match Switzerland could still decide.

## Model Adjustment Notes

- For balanced group-position games, do not let mutual caution erase a stronger side's late winner path.
- Calibration tags: `draw_overweighted`, `favorite_margin_understated`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021451
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/matchday-14-round-up-review-highlights
- Verified at: 2026-06-25T13:51:27+08:00

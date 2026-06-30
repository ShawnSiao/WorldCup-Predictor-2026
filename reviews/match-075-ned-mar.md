# Match 075 Review: Netherlands vs Morocco

[Reviews index](README.md) | [简体中文](match-075-ned-mar.zh-CN.md) | [Prediction](../predictions/match-075-ned-mar.md)

## Result

- Final result: Netherlands 1-1 Morocco; Morocco won 3-2 on penalties in Match 075.
- Predicted winner: Netherlands.
- Actual winner: Morocco.
- Predicted scoreline: Netherlands vs Morocco 2-1.
- Review rating: partial.

## What Held Up

- The conservative draw path was 1-1, matching the regulation-time score.
- Morocco's compact block and transition discipline were correctly flagged as the route that could keep the match level.

## What Failed

- The Netherlands winner and advancement lean were wrong.
- The model still gave the Netherlands too much late attacking-depth credit and did not weight Morocco's penalty resilience enough.

## Model Adjustment Notes

- `draw_underweighted`, `underdog_resilience_underweighted`, `data_gap_overconfidence`; when the primary and conservative scenarios are close, advancement probabilities should reflect penalty variance more strongly.

## Source Snapshot

- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures
- https://www.fifa.com/en/match-centre/match/17/285023/289287/400021520
- https://www.aljazeera.com/sports/liveblog/2026/6/29/netherlands-vs-morocco-live-world-cup-2026-last-32-match-updates
- https://www.espn.com/soccer/report/_/gameId/760495
- https://www.foxsports.com/soccer/fifa-world-cup/scores
- Verified at: 2026-06-30T23:55:00+08:00

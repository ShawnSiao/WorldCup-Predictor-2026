# Match 017 Review: France vs Senegal

[Reviews index](README.md) | [简体中文](match-017-fra-sen.zh-CN.md) | [Prediction](../predictions/match-017-fra-sen.md)

## Result

- Final result: France 3-1 Senegal in Match 017.
- Predicted winner: France.
- Actual winner: France.
- Predicted scoreline: France 2-1 Senegal.
- Review rating: correct.

## What Held Up

- France's deeper attacking options and stronger ranking baseline translated into a real edge.
- Senegal did score, which matched the prediction's transition and set-piece risk framing.
- The model was right to avoid a clean-sheet call after the prior review pass.

## What Failed

- The margin was still understated: France created more separation than the 2-1 headline expected.
- Senegal's compactness did not hold the match close enough to make the 1-1 draw path the main threat.

## Model Adjustment Notes

- Keep the African-underdog transition adjustment, but do not let it erase a clear favorite's chance-volume edge.
- When a favorite has both ranking separation and attacking depth, maintain an upside scoreline with a larger margin.
- Calibration tags: `favorite_margin_understated`, `underdog_resilience_overweighted_after_correction`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021490
- https://www.aljazeera.com/sports/2026/6/16/france-overcome-senegal-test-in-world-cup-opener
- https://www.espn.com/soccer/report/_/gameId/760430
- Verified at: 2026-06-17T14:38:30+08:00

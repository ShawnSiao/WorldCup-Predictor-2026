# Match 016 Review: Belgium vs Egypt

[Dashboard](../README.md) | [简体中文](match-016-bel-egy.zh-CN.md) | [Prediction](../predictions/match-016-bel-egy.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Belgium | Draw |
| Scoreline | Belgium 2-1 Egypt | Belgium 1-1 Egypt |
| Rating | partial | partial |

## Match Data And Conditions

- Final result: Belgium 1-1 Egypt in Match 016.
- Prediction rating: `partial`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- Egypt's scoring threat through high-quality attacking players was correctly identified.
- Belgium's bench impact mattered, with the equalizer coming after a substitute changed the box dynamics.

## What Failed

- The Belgium win lean was too strong.
- The model did not price Egypt's first-half control and Belgium's slow attacking rhythm enough.
- Heat and cooling-break context should have raised the draw path.

## Potential Factors To Carry Forward

- For aging or transition-phase favorites, attacking rhythm must be verified before projecting a win.
- Heat and hydration-break conditions can reduce tempo and help organized underdogs.
- Substitute impact should be a scenario variable, not only a generic late risk.

## Model Adjustment Notes

- Calibration tags: `draw_underweighted`, `underdog_resilience_underweighted`, `data_gap_overconfidence`.
- Increase draw probability when a favorite has name value but uncertain current attacking cohesion.

## Source Snapshot

- FIFA match centre: https://www.fifa.com/en/match-centre/match/17/285023/289273/400021478
- Guardian live report: https://www.theguardian.com/football/live/2026/jun/15/belgium-v-egypt-world-cup-2026-live
- Guardian match report: https://www.theguardian.com/football/2026/jun/15/belgium-egypt-world-cup-2026-group-g-match-report
- Verified at: 2026-06-16T16:13:02+08:00

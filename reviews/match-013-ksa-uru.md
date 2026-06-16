# Match 013 Review: Saudi Arabia vs Uruguay

[Dashboard](../README.md) | [简体中文](match-013-ksa-uru.zh-CN.md) | [Prediction](../predictions/match-013-ksa-uru.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Uruguay | Draw |
| Scoreline | Saudi Arabia 0-2 Uruguay | Saudi Arabia 1-1 Uruguay |
| Rating | wrong | wrong |

## Match Data And Conditions

- Final result: Saudi Arabia 1-1 Uruguay in Match 013.
- Prediction rating: `wrong`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- Uruguay's second-half pressure and ability to recover a result were real.
- Saudi Arabia's set-piece and defensive-resilience routes were identified as risks, but not given enough probability.

## What Failed

- The clean-sheet and two-goal Uruguay margin were overstated.
- The model underweighted Saudi Arabia's tournament resilience and set-piece route.
- It did not sufficiently account for travel and matchday disruption around Uruguay.

## Potential Factors To Carry Forward

- Saudi-style compactness and set pieces should carry more weight in group openers.
- Travel, traffic, and late arrival disruptions can reduce favorite sharpness.
- A low-scoring Uruguay attack should not be paired with a comfortable win unless chance volume is verified.

## Model Adjustment Notes

- Calibration tags: `draw_underweighted`, `clean_sheet_overstated`, `set_piece_risk_underweighted`, `data_gap_overconfidence`.
- For favorites with known attacking inconsistency, keep draw probability higher even when squad quality is superior.

## Source Snapshot

- FIFA match centre: https://www.fifa.com/en/match-centre/match/17/285023/289273/400021486
- Guardian live report: https://www.theguardian.com/football/live/2026/jun/15/saudi-arabia-v-uruguay-world-cup-2026-live
- NBC Miami report: https://www.nbcmiami.com/world-cup/world-cup-comes-to-miami-saudi-arabia-takes-on-uruguay-today/3820657/
- Verified at: 2026-06-16T16:13:02+08:00

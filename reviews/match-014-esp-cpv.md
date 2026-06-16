# Match 014 Review: Spain vs Cabo Verde

[Dashboard](../README.md) | [简体中文](match-014-esp-cpv.zh-CN.md) | [Prediction](../predictions/match-014-esp-cpv.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Spain | Draw |
| Scoreline | Spain 3-0 Cabo Verde | Spain 0-0 Cabo Verde |
| Rating | wrong | wrong |

## Match Data And Conditions

- Final result: Spain 0-0 Cabo Verde in Match 014.
- Prediction rating: `wrong`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- Spain's territorial and shot-volume dominance was real.
- Cabo Verde's defensive commitment was identified as a low-probability risk, but not priced remotely high enough.

## What Failed

- The model overstated Spain's conversion and clean-margin expectation.
- It underweighted debutant emotion, goalkeeper performance, emergency defending, and finishing variance.
- It treated the ranking gap as too deterministic.

## Potential Factors To Carry Forward

- Heavy favorites against compact debutants need a 0-0 or 1-0 scenario when chance conversion is not verified.
- Goalkeeper ceiling and blocked-shot volume must be explicit variables.
- A shot-volume edge is not enough; the model needs chance quality and final-third spacing.

## Model Adjustment Notes

- Calibration tags: `draw_underweighted`, `favorite_margin_overstated`, `data_gap_overconfidence`.
- For elite favorites, cap clean-margin confidence unless lineup, chance quality, and opponent fatigue are all verified.

## Source Snapshot

- FIFA match centre: https://www.fifa.com/en/match-centre/match/17/285023/289273/400021482
- Guardian match report: https://www.theguardian.com/football/2026/jun/15/spain-cape-verde-world-cup-2026-group-h-match-report
- Al Jazeera live report: https://www.aljazeera.com/sports/liveblog/2026/6/15/spain-vs-cape-verde-live-world-cup-2026
- Verified at: 2026-06-16T16:13:02+08:00

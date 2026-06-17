# Match 018 Review: Iraq vs Norway

[Reviews index](README.md) | [简体中文](match-018-irq-nor.zh-CN.md) | [Prediction](../predictions/match-018-irq-nor.md)

## Result

- Final result: Iraq 1-4 Norway in Match 018.
- Predicted winner: Norway.
- Actual winner: Norway.
- Predicted scoreline: Iraq 0-2 Norway.
- Review rating: correct.

## What Held Up

- Norway's attacking-ceiling edge was real and decisive.
- Iraq did not generate enough sustained control to turn the match into the 1-1 conservative path.
- The favorite lean was directionally right.

## What Failed

- The model understated Norway's finishing upside and overstated the probability of a narrow low-block game.
- The clean-sheet assumption failed: Iraq still found a scoring route.

## Model Adjustment Notes

- For elite-forward profiles, keep a wider-margin upside case even when the opponent projects as compact.
- Separate "low block reduces volume" from "low block eliminates finishing bursts"; the latter was too strong here.
- Calibration tags: `favorite_margin_understated`, `clean_sheet_overstated`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021491
- https://www.theguardian.com/football/2026/jun/16/norway-iraq-world-cup-2026-group-i-match-report
- https://www.foxsports.com/stories/soccer/world-cup-norway-iraq-france-senegal
- Verified at: 2026-06-17T14:38:30+08:00

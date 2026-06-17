# Match 019 Review: Argentina vs Algeria

[Reviews index](README.md) | [简体中文](match-019-arg-alg.zh-CN.md) | [Prediction](../predictions/match-019-arg-alg.md)

## Result

- Final result: Argentina 3-0 Algeria in Match 019.
- Predicted winner: Argentina.
- Actual winner: Argentina.
- Predicted scoreline: Argentina 2-0 Algeria.
- Review rating: correct.

## What Held Up

- Argentina's ranking and squad-quality edge controlled the base case.
- The model correctly treated Algeria's transition risk as real but not enough to flip the match.
- The favorite clean-sheet path held in this specific matchup.

## What Failed

- Argentina's margin and finishing control were understated by one goal.
- The post-review caution around clean sheets was appropriate globally, but slightly too conservative for this matchup.

## Model Adjustment Notes

- Keep the underdog-transition correction, but allow high-control favorites to retain clean-sheet upside when the opposition cannot sustain pressure.
- For top-tier favorites, model a wider primary/upside spread instead of compressing all risk into 2-0.
- Calibration tags: `favorite_margin_understated`, `clean_sheet_caution_overweighted`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021497
- https://www.reuters.com/sports/soccer/argentina-beat-algeria-3-0-world-cup-opener-2026-06-17/
- https://www.espn.com/soccer/report/_/gameId/760435
- Verified at: 2026-06-17T14:38:30+08:00

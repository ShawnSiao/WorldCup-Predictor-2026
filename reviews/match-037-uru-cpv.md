# Match 037 Review: Uruguay vs Cape Verde

[Reviews index](README.md) | [简体中文](match-037-uru-cpv.zh-CN.md) | [Prediction](../predictions/match-037-uru-cpv.md)

## Result

- Final result: Uruguay 2-2 Cape Verde in Match 037.
- Predicted winner: Uruguay.
- Actual winner: Draw.
- Predicted scoreline: Uruguay vs Cape Verde 1-0.
- Review rating: wrong.

## What Held Up

- The forecast correctly identified Cape Verde's low block and draw route as the main danger.
- The match stayed tight enough for one moment, restart, or goalkeeping error to swing the result.

## What Failed

- Uruguay's control was overstated; the model did not give enough weight to Cape Verde scoring twice.
- The 0-0 conservative path captured underdog resistance but underweighted a scoring draw.

## Model Adjustment Notes

- Low-block underdogs with a proven goalkeeper and set-piece route need a larger scoring-draw tail.
- Calibration tags: `draw_underweighted`, `underdog_resilience_underweighted`, `set_piece_risk_underweighted`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021487
- https://www.foxsports.com/soccer/fifa-world-cup-men-uruguay-vs-cape-verde-jun-21-2026-game-boxscore-647654
- Verified at: 2026-06-22T15:01:00+08:00

# Match 021 Review: Ghana vs Panama

[Reviews index](README.md) | [简体中文](match-021-gha-pan.zh-CN.md) | [Prediction](../predictions/match-021-gha-pan.md)

## Result

- Final result: Ghana 1-0 Panama in Match 021.
- Predicted winner: Ghana.
- Actual winner: Ghana.
- Predicted scoreline: Ghana 1-0 Panama.
- Review rating: correct.

## What Held Up

- The 1-0 headline scoreline landed exactly.
- The low-event, physical-duel read was the right base case.
- Keeping Panama close rather than dismissing them kept the confidence at the right level.

## What Failed

- The ranking gap still overstated Panama relative to the match script.
- The upset route was present but correctly stayed secondary.

## Model Adjustment Notes

- Keep full 1-0 routes when tempo and chance volume are constrained.
- Do not flatten lower-ranked physical teams solely because ranking says otherwise.
- Calibration tags: `low_margin_correct`, `set_piece_transition_risk_retained`.

## Source Snapshot

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021510
- https://www.espn.com/soccer/match/_/gameId/760436/ghana-panama
- https://www.sportingnews.com/us/soccer/news/ghana-panama-live-score-result-world-cup/4773447545378ec79f6b9b6c
- Verified at: 2026-06-18T17:05:25+08:00

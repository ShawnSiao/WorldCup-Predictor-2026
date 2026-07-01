# Match 078 Review: Cote d'Ivoire vs Norway

[Reviews index](README.md) | [简体中文](match-078-civ-nor.zh-CN.md) | [Prediction](../predictions/match-078-civ-nor.md)

## Result

- Final result: Cote d'Ivoire 1-2 Norway in Match 078.
- Predicted winner: Norway.
- Actual winner: Norway.
- Predicted scoreline: Cote d'Ivoire vs Norway 1-2.
- Review rating: correct.

## What Held Up

- Norway winner, one-goal margin, and exact scoreline were correct.
- The Brazil-path caveat was useful: Norway still had to win efficiently before a harder next opponent.

## What Failed

- Cote d'Ivoire's physical pressure was correctly present but did not push the match into the draw route.
- The model can keep this pattern but should not overreact to every duel-heavy underdog as an extra-time favourite.

## Model Adjustment Notes

- `exact_score_hit`, `transition_risk_calibrated`; keep Norway-style elite finishing as a major single-action edge.

## Source Snapshot

- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures
- https://www.fifa.com/en/match-centre/match/17/285023/289287/400021522
- https://www.si.com/soccer/norway-player-ratings-vs-ivory-coast-haaland-world-cup
- https://www.foxsports.com/soccer/fifa-world-cup/scores
- Verified at: 2026-07-01T20:51:00+08:00

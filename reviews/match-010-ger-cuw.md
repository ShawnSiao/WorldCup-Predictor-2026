# Match 010 Review: Germany vs Curacao

[Dashboard](../README.md) | [简体中文](match-010-ger-cuw.zh-CN.md) | [Prediction](../predictions/match-010-ger-cuw.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Germany | Germany |
| Scoreline | Germany 3-0 Curacao | Germany 7-1 Curacao |
| Rating | correct | correct |

## Match Data And Conditions

- Final result: Germany 7-1 Curacao in Match 010.
- Prediction rating: `correct`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- The Germany win lean was correct.
- The model correctly identified the large quality gap and low-block patience risk.

## What Failed

- The model understated the margin once Curacao's defensive structure broke.
- The clean-sheet call failed; even heavy favorites remain exposed to one transition or concentration lapse.

## Potential Factors To Carry Forward

- Debutant or low-ranked teams can collapse after the first or second goal if the favorite keeps pressure high.
- Heavy favorite forecasts need both a conservative path and a blowout path, not just a controlled 2-0 or 3-0.

## Model Adjustment Notes

- Calibration tags: `favorite_margin_understated`, `clean_sheet_overstated`.
- Keep favorite caps, but widen scoreline scenarios when a favorite has verified depth and the opponent has limited escape routes.

## Source Snapshot

- FIFA schedule/results page: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- Al Jazeera match report: https://www.aljazeera.com/sports/2026/6/14/germany-hit-curacao-for-seven-to-open-their-world-cup
- ESPN match report: https://www.espn.com/soccer/report/_/gameId/760422
- Verified at: 2026-06-16T16:13:02+08:00

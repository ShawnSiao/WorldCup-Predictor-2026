# Match 009 Review: Cote d'Ivoire vs Ecuador

[Dashboard](../README.md) | [简体中文](match-009-civ-ecu.zh-CN.md) | [Prediction](../predictions/match-009-civ-ecu.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Ecuador | Cote d'Ivoire |
| Scoreline | Cote d'Ivoire 0-1 Ecuador | Cote d'Ivoire 1-0 Ecuador |
| Rating | wrong | wrong |

## Match Data And Conditions

- Final result: Cote d'Ivoire 1-0 Ecuador in Match 009.
- Prediction rating: `wrong`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- The low-scoring expectation was directionally correct.
- The prediction correctly treated the match as a small-margin contest.

## What Failed

- The model put the one decisive goal on the wrong side.
- It overweighted Ecuador's midfield-control case and underweighted Cote d'Ivoire's direct, late-game attacking route.
- It did not price late substitute impact and transition execution strongly enough.

## Potential Factors To Carry Forward

- In evenly matched cross-confederation games, physical duels, late legs, and direct wide attacks deserve a higher weight than raw control.
- A one-goal favorite call should stay close to a draw unless there is verified chance-creation or finishing support.

## Model Adjustment Notes

- Calibration tags: `transition_risk_underweighted`, `underdog_resilience_underweighted`, `data_gap_overconfidence`.
- When the preferred team is only a narrow favorite, keep the opposite 1-0 path explicit rather than treating it as a tail event.

## Source Snapshot

- FIFA schedule/results page: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- ESPN match report: https://www.espn.com/soccer/story/_/id/49064087/ivory-coast-ecuador-live-world-cup-2026-latest-updates-commentary-score-result
- FOX Sports highlights: https://www.foxsports.com/watch/fmc-43wd33qm20poy8zk
- Verified at: 2026-06-16T16:13:02+08:00

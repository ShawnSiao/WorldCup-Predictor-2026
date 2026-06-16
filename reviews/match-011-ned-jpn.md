# Match 011 Review: Netherlands vs Japan

[Dashboard](../README.md) | [简体中文](match-011-ned-jpn.zh-CN.md) | [Prediction](../predictions/match-011-ned-jpn.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Netherlands | Draw |
| Scoreline | Netherlands 2-1 Japan | Netherlands 2-2 Japan |
| Rating | partial | partial |

## Match Data And Conditions

- Final result: Netherlands 2-2 Japan in Match 011.
- Prediction rating: `partial`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- The match was correctly projected as high-quality and close.
- Japan's pressing and transition threat were correctly identified as the main risk to the Netherlands lean.

## What Failed

- The draw risk was still underweighted.
- The model did not give enough weight to Japan's ability to answer after falling behind.
- Late-game concentration and second-half rhythm swings were stronger than the pre-match forecast allowed.

## Potential Factors To Carry Forward

- Japan's press should be treated as a result-changing feature, not just a stylistic nuisance.
- When two strong teams both have transition routes, draw probability should sit closer to the top of the draw-floor band.

## Model Adjustment Notes

- Calibration tags: `draw_underweighted`, `transition_risk_underweighted`, `underdog_resilience_underweighted`.
- For upcoming favorites against high-press teams, keep the one-goal favorite call but raise the 1-1 or 2-2 scenario.

## Source Snapshot

- FIFA match report: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/netherlands-japan-highlights-match-report
- FOX Sports live blog: https://www.foxsports.com/live-blog/soccer/netherlands-vs-japan-live-updates-score-top-plays-from-group-showdown
- Verified at: 2026-06-16T16:13:02+08:00

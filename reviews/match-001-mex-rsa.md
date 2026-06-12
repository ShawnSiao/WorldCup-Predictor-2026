# Match 001 Review: Mexico vs South Africa

[Dashboard](../README.md) | [简体中文](match-001-mex-rsa.zh-CN.md) | [Prediction](../predictions/match-001-mex-rsa.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Mexico | Mexico |
| Scoreline | Mexico 2-0 South Africa | Mexico 2-0 South Africa |
| Rating | correct | correct |

## What Held Up

- Mexico's home setting, altitude familiarity, and stronger baseline translated into territorial control and a clean-sheet win.
- The pre-match call that South Africa needed a low-event game proved right; once the match became chaotic, Mexico handled the decisive moments better.
- The 2-0 scoreline matched the expected script of Mexico scoring through pressure and then adding control after South Africa opened up.

## What Failed

- The preview treated South Africa set pieces and counters as the main risk, but the larger swing factor was discipline: South Africa finished with nine players, and Mexico also had a late red card.
- The model underweighted how much a tournament opener can become card-driven rather than chance-quality-driven.

## Model Adjustment Notes

- Add discipline volatility as a specific opening-match feature, not just a generic "early event" risk.
- Separate clean-sheet confidence from winner confidence more explicitly when a match has high pressure and possible card risk.
- Track official red-card and suspension consequences immediately because they affect the next Group A predictions.

## Source Snapshot

- FIFA schedule/results page: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- Guardian live report: https://www.theguardian.com/football/live/2026/jun/11/mexico-v-south-africa-world-cup-2026-opening-match-live
- Verified at: 2026-06-12T08:08:19+08:00

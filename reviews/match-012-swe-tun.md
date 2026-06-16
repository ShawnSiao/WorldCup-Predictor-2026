# Match 012 Review: Sweden vs Tunisia

[Dashboard](../README.md) | [简体中文](match-012-swe-tun.zh-CN.md) | [Prediction](../predictions/match-012-swe-tun.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Sweden | Sweden |
| Scoreline | Sweden 1-0 Tunisia | Sweden 5-1 Tunisia |
| Rating | partial | partial |

## Match Data And Conditions

- Final result: Sweden 5-1 Tunisia in Match 012.
- Prediction rating: `partial`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- The Sweden win lean was correct.
- Tunisia's defensive fragility was a valid risk, but the predicted scoreline did not reflect how severe it could become.

## What Failed

- The model badly understated Sweden's attacking ceiling.
- It treated Tunisia's defensive record as more stable than the late tactical and managerial context justified.
- The scoreline scenarios lacked a true rout path.

## Potential Factors To Carry Forward

- Recent coach or formation disruption can invalidate older defensive priors.
- If a favorite has multiple high-quality forwards and the opponent's setup is unstable, include a high-margin scenario even when the headline lean is cautious.

## Model Adjustment Notes

- Calibration tags: `favorite_margin_understated`, `data_gap_overconfidence`.
- Add a late-tactical-change penalty for teams with new managers, unfamiliar shapes, or disrupted preparation.

## Source Snapshot

- FIFA match centre: https://www.fifa.com/en/match-centre/match/17/285023/289273/400021474
- Al Jazeera match report: https://www.aljazeera.com/sports/2026/6/15/sweden-beat-tunisia-5-1-in-strong-start-to-world-cup
- NY Post Tunisia manager report: https://nypost.com/2026/06/15/sports/tunisia-firing-manager-sabri-lamouchi-after-one-world-cup-game/
- Verified at: 2026-06-16T16:13:02+08:00

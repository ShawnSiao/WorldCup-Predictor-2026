# Match 006 Review: Australia vs Turkiye

[Dashboard](../README.md) | [简体中文](match-006-aus-tur.zh-CN.md) | [Prediction](../predictions/match-006-aus-tur.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | Turkiye | Australia |
| Scoreline | Australia 1-2 Turkiye | Australia 2-0 Turkiye |
| Rating | wrong | wrong |

## Match Data And Conditions

- Final result: Australia 2-0 Turkiye in Match 006.
- Prediction rating: `wrong`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- The prediction correctly treated Turkiye as a side with more ball-dominant talent, but that did not translate into decisive chance conversion.
- Australia's ability to keep the game narrow was a valid risk, but the model did not price it strongly enough.

## What Failed

- Australia were not just a resistance case; they won the match through counterattacking execution and goalkeeper performance.
- The model overweighted Turkiye's possession and European-club talent signal.
- It underweighted selection volatility: Australia's goalkeeper and midfield calls changed the match script.

## Potential Factors To Carry Forward

- Treat underdog counterattack plans as live upset routes when the favorite's finishing profile is not verified.
- Add goalkeeper form and surprise selection risk to the evidence pass before backing a technical favorite.
- Do not assume territory becomes goals against disciplined low-block or mid-block opponents.

## Model Adjustment Notes

- Calibration tags: `transition_risk_underweighted`, `underdog_resilience_underweighted`, `data_gap_overconfidence`.
- For the next predictions, reduce favorite win probability when the favorite depends on possession without clear chance-quality data.

## Source Snapshot

- FIFA schedule/results page: https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- Al Jazeera match report: https://www.aljazeera.com/sports/2026/6/14/2026-world-cup-australia-stun-turkiye-2-0-in-counterattacking-masterclass
- Verified at: 2026-06-16T16:13:02+08:00

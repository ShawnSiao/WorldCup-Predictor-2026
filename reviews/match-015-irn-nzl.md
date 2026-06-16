# Match 015 Review: IR Iran vs New Zealand

[Dashboard](../README.md) | [简体中文](match-015-irn-nzl.zh-CN.md) | [Prediction](../predictions/match-015-irn-nzl.md)

## Result

| Item | Prediction | Actual |
| --- | --- | --- |
| Winner | IR Iran | Draw |
| Scoreline | IR Iran 2-0 New Zealand | IR Iran 2-2 New Zealand |
| Rating | wrong | wrong |

## Match Data And Conditions

- Final result: IR Iran 2-2 New Zealand in Match 015.
- Prediction rating: `wrong`.
- Review basis: verified result, pre-match prediction file, and post-match source snapshot.

## What Held Up

- Iran's ability to respond and score twice was real.
- The match was affected by off-field and logistical context, which had been noted but not weighted enough.

## What Failed

- The clean-sheet assumption failed badly.
- New Zealand's attacking efficiency and Chris Wood-linked chance creation were underweighted.
- The model did not sufficiently price Iran's disrupted preparation, political pressure, and forced travel logistics.

## Potential Factors To Carry Forward

- Political and travel disruption should reduce confidence and raise both concession and draw probabilities.
- OFC or lower-ranked teams with a clear target-forward / runner structure can outperform ranking priors.
- A favorite's ability to equalize is not the same as ability to control the match.

## Model Adjustment Notes

- Calibration tags: `draw_underweighted`, `clean_sheet_overstated`, `transition_risk_underweighted`, `data_gap_overconfidence`.
- Add a logistics-pressure variable for teams with visa, relocation, security, or travel uncertainty.

## Source Snapshot

- FIFA match centre: https://www.fifa.com/en/match-centre/match/17/285023/289273/400021476
- Guardian live report: https://www.theguardian.com/football/live/2026/jun/16/fifa-world-cup-2026-live-iran-v-new-zealand-updates-irn-vs-nzl-group-f-match-score-latest
- Al Jazeera match report: https://www.aljazeera.com/sports/2026/6/16/iran-draw-2-2-with-new-zealand-in-politically-charged-world-cup-match
- Verified at: 2026-06-16T16:13:02+08:00

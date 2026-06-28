# Prediction and Review Methodology

[English](../README.md) | [简体中文](methodology.zh-CN.md) | [Changelog](../CHANGELOG.md)

## Reasoning Model

All prediction reasoning is specified to use the ChatGPT 5.5 ultra-high reasoning model.

The repository publishes concise reasoning summaries. It does not store hidden chain-of-thought or private reasoning traces.

## Prediction Inputs

Each pre-match prediction must complete a pre-result coverage pass before publishing the outcome. The pass covers:

- tactics and expected tactical matchup
- players, squad strength, and likely lineup quality
- injuries, suspensions, and player availability
- schedule, rest days, travel load, kickoff time, and venue context
- head-to-head record, tournament history, and relevant historical patterns
- public sentiment, media narrative, and crowd expectation
- weather, climate, pitch, altitude, and venue conditions
- psychology, pressure, motivation, and group/knockout incentives
- bracket path incentives, including whether winning, drawing, or losing changes next-round opponent strength, rest/travel burden, draw quadrant, or qualification route
- reputable public forecast signals and movement, clearly labeled as context
- expert views from reputable analysts or official broadcast/editorial sources

If an input is unavailable, stale, or unverified, the prediction must label the gap, explain how it affects confidence, and avoid using the missing item as confirmed evidence.

Data gaps should be closed through the source tiers in [Prediction Calibration](prediction-calibration.md). In short: schedule/results/rankings are refreshed from official structured sources; weather, odds movement, and expert views require timestamped snapshots; injuries, suspensions, and likely lineups require official or reputable late team-news verification before confidence can be raised.

Every prediction must include a bracket path incentive read. This applies to all matches, not only final group matches. The forecast should compare the current live table or bracket against plausible next-round paths, then explain whether a team has reason to protect a draw, chase top spot, manage minutes, avoid a stronger opponent, or accept a lower-risk route. If the path is not yet fixed, the forecast must say so and keep the strategy effect as a confidence limiter rather than confirmed intent.

## Prediction Output

Group-stage predictions include:

- home win probability
- draw probability
- away win probability
- predicted scoreline
- three scoreline scenarios for Match 017 onward: primary, conservative/draw path, and upside/alternate path
- confidence level
- share image
- factual basis
- prediction coverage checklist
- prediction logic
- reasoning summary
- risk factors
- platform share copy
- investment advice disclaimer

The prediction copy must describe the strategy read clearly enough for readers to see how bracket path incentives affected the published probabilities, scoreline scenarios, rotation risk, and confidence level.

Knockout predictions should add advancement probability and separate regulation-time outcome from extra-time or penalty scenarios.

Scoreline scenario probabilities are single-score estimates and do not need to sum to 100%. The three scenarios must include the main non-primary route so readers can see how a draw, narrow result, or underdog path could happen.

## Publishing Copy

Each prediction should include share-ready copy for Douyin, Xiaohongshu, Weibo, and WeChat.

Platform copy should be concise, fact-based, and clearly labeled as a match prediction. It must include a disclaimer that the content does not constitute investment advice. Standing account-introduction copy for each platform is maintained in [Platform Publishing Copy](platform-copy.md).

Each prediction and daily report should embed a `$imagegen` generated raster share image from `assets/cards/`. Use this instruction pattern:

```text
$imagegen: Generate a social-platform match prediction image, 16:9 landscape, real raster image for Douyin, Xiaohongshu, Weibo, and WeChat sharing. For Simplified Chinese documents, make the primary match information Simplified Chinese and keep any English team or event text only as secondary text in an appropriate location; do not generate SVG, HTML, code art, wireframes, chart-only graphics, official FIFA logos, or watermarks.
```

Daily automation should read the current connected Gmail profile email address, then email the validated daily summary and generated image assets to that Google mailbox. Git config email addresses and GitHub account emails must not be used as recipients.

## Review Method

Post-match reviews compare the prediction to the official final result.

Each review should record:

- actual score and winner
- key events and turning points
- whether the predicted winner was correct
- whether the scoreline was close
- which assumptions held up
- which assumptions failed
- model adjustment notes for later matches

Review ratings:

- `correct`: core outcome correct and match script close.
- `partial`: useful read, but material misses.
- `wrong`: core outcome missed.

Reviews should add structured error tags when they reveal calibration issues, such as `draw_underweighted`, `favorite_margin_overstated`, `clean_sheet_overstated`, `underdog_resilience_underweighted`, or `data_gap_overconfidence`.

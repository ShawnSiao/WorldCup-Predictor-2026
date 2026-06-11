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
- reputable public forecast signals and movement, clearly labeled as context
- expert views from reputable analysts or official broadcast/editorial sources

If an input is unavailable, stale, or unverified, the prediction must label the gap, explain how it affects confidence, and avoid using the missing item as confirmed evidence.

## Prediction Output

Group-stage predictions include:

- home win probability
- draw probability
- away win probability
- predicted scoreline
- confidence level
- share image
- factual basis
- prediction coverage checklist
- prediction logic
- reasoning summary
- risk factors
- platform share copy
- investment advice disclaimer

Knockout predictions should add advancement probability and separate regulation-time outcome from extra-time or penalty scenarios.

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

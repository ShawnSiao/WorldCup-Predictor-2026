---
name: worldcup-match-predictor
description: Use when predicting FIFA World Cup match outcomes, preparing pre-match probability briefs, creating social share copy or images, or reviewing completed predictions against official results.
---

# World Cup Match Predictor

## Purpose

Use this skill to produce evidence-based FIFA World Cup match predictions. Treat predictions as editorial analysis, not betting, financial, or investment advice. Publish concise reasoning summaries only; do not reveal or store hidden chain-of-thought.

## Portability Rules

- Do not assume any fixed project folders, filenames, schemas, scripts, or validation commands exist.
- First inspect the user's request and current workspace, then reuse whatever conventions are already present.
- If no local convention exists, produce a self-contained prediction brief in the response or in the user-requested output location.
- If the user asks for files but gives no structure, choose simple human-readable Markdown plus optional structured JSON only when useful.
- Use exact dates and source timestamps for time-sensitive facts.

## Evidence Inputs

Verify current facts from official or reputable sources before making or refreshing a prediction. Prefer:

- official match schedule, kickoff time, venue, host city, and stage
- FIFA ranking snapshots and ranking movement
- official squad lists, injuries, suspensions, and player availability
- recent competitive form and opponent strength
- tactical matchup, likely lineups, rest days, travel, altitude, climate, and home/host context
- group table or knockout incentive context
- reputable market odds only when clearly labeled and not treated as certainty

When facts are unavailable, say so and lower confidence instead of inventing details.

## Prediction Method

1. Define the match context: teams, stage, kickoff, venue, and competitive incentives.
2. Build a source snapshot with URLs or citations and a verification timestamp.
3. Compare baseline team strength, squad quality, availability, form, tactics, and venue/travel factors.
4. Estimate probabilities. For group-stage matches, include Team A win, draw, and Team B win. For knockout matches, separate regulation-time probabilities from advancement probabilities.
5. Pick a predicted scoreline that matches the probability distribution and expected match script.
6. Assign confidence as low, medium-low, medium, medium-high, or high.
7. List risk factors that could change the result.
8. Create platform copy or image prompts only after the factual prediction is coherent.

Probabilities should sum to 100% or 1.00. Avoid false precision when the input data is thin.

## Prediction Brief Template

Use this structure unless the target project already has a stricter format:

```markdown
# <Team A> vs <Team B> Prediction

## Match Context

- Match: <Team A> vs <Team B>
- Stage: <stage>
- Kickoff: <date and time with timezone>
- Venue: <stadium, city>
- Source snapshot: <timestamp>

## Prediction

| Outcome | Probability |
| --- | ---: |
| <Team A> win | <percent> |
| Draw | <percent> |
| <Team B> win | <percent> |

- Predicted result: <winner or draw>
- Predicted scoreline: <score>
- Confidence: <level>

## Factual Basis

- <verified fact>
- <verified fact>
- <known data gap, if any>

## Prediction Logic

1. <concise reasoning summary>
2. <concise reasoning summary>
3. <concise reasoning summary>

## Risk Factors

- <risk>
- <risk>

## Source Snapshot

- <source name>: <URL or citation>
- Verified at: <timestamp>

## Disclaimer

This is a football match prediction only. It does not constitute betting advice, investment advice, financial advice, or any guarantee of outcome.
```

## Social Sharing

When preparing share copy, include concise versions for the platforms the user requests. For Chinese platforms, useful labels are:

- Douyin / 抖音
- Xiaohongshu / 小红书
- Weibo / 微博
- WeChat / 微信

Every share-ready block should clearly say it is a sports prediction and include a disclaimer equivalent to:

```text
This is a match prediction only and does not constitute investment advice.
仅为足球赛事预测，不构成任何投资建议。
```

## Share Image Guidance

If generating a social card image, use a real raster image format such as PNG, JPG, JPEG, or WebP. Do not create SVG, HTML, code art, wireframes, chart-only graphics, official FIFA logos, or watermarks.

Prompt shape:

```text
Generate a social-platform FIFA World Cup match prediction image, 16:9 landscape, <teams and match context>, real raster image for social sharing; do not use official FIFA logos or watermarks.
```

For Chinese output:

```text
生成【社交平台世界杯赛事预测配图】，16:9 横版，<球队与比赛背景>，真实位图图片，用于社交平台分享；不要生成 SVG，不要生成 HTML，不要生成代码图，不要生成线框图，不要使用官方 FIFA 标志或水印。
```

## Completed Match Review

When reviewing a finished match, compare:

- predicted winner vs actual winner
- predicted scoreline vs final score
- assumptions that held up
- assumptions that failed
- model adjustment notes for future matches

Use `correct`, `partial`, or `wrong` only if the target project needs a rating.

## Self-Check

Before finalizing:

- current facts were verified from official or reputable sources
- source snapshot and exact dates are present
- probabilities sum correctly
- confidence reflects data quality
- unavailable facts are labeled as gaps
- no hidden chain-of-thought is included
- disclaimers are present
- generated images, if any, are raster assets without official logos or watermarks
- any existing local validation commands were run, or the absence of such commands is stated

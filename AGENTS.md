# WorldCup-Predictor-2026 Agent Index

This file is the working entry point for AI agents maintaining this repository.

## Repository Purpose

WorldCup-Predictor-2026 tracks the 2026 FIFA World Cup schedule, publishes pre-match predictions, records official results, and creates post-match reviews for every completed match.

## Durable Local Context

- Local-only working spec: `docs/local/repository-display-and-update-spec.zh-CN.md`
- `docs/local/` is ignored through `.git/info/exclude` and must not be committed.
- Public documentation starts from `README.md` and `docs/README.zh-CN.md`.

## Required Daily Workflow

1. Verify current facts from official or reputable sources.
2. Update structured data under `data/`.
3. Create or refresh predictions for upcoming matches.
4. Generate or refresh two raster share images for every published prediction with `$imagegen`.
5. Create reviews for completed matches.
6. Update the daily report in `reports/daily/`, including a daily overview card when the report covers multiple predicted matches on the same China-time date.
7. Refresh README dashboard counters and links when visible state changes.
8. Run validation.
9. Commit and push only repository artifacts, never local specs.

## Prediction Requirements

Every prediction file in `predictions/` must include:

- `## Prediction`
- `## Share Image`
- `## Factual Basis`
- `## Scoreline Scenarios` for Match 017 onward and future refreshed predictions
- `## Prediction Logic`
- `## Risk Factors`
- `## Platform Share Copy`
- `## Disclaimer`
- `## Source Snapshot`

Prediction reasoning must be based on current facts such as official schedule, venue, team strength, rankings, squad availability, recent form, group table state, knockout bracket path, and verified source updates.

Before publishing any predicted result, the model must complete a documented coverage pass across all of these dimensions: tactics, players, injuries/suspensions, schedule/rest/travel, head-to-head and tournament history, public sentiment/media narrative, weather and venue conditions, psychology/pressure/motivation, bracket path incentives, odds movement, and expert views. If a dimension is unavailable or not yet verified, the prediction must say so explicitly, explain the impact on confidence, and avoid treating that dimension as confirmed evidence.

Every prediction must explicitly evaluate bracket path incentives, including whether winning, drawing, or losing changes the next-round opponent quality, rest/travel burden, draw quadrant, or qualification route. This applies to every match, not only final group matches. When the next-round path is not yet fixed, the prediction must state the current uncertainty, compare the live table or bracket possibilities with reputable source data, and explain how this uncertainty affects probabilities, scoreline scenarios, rotation risk, risk appetite, and confidence. Do not assume deliberate underperformance; treat any "Tian Ji horse racing" style strategy as a hypothesis that requires table/bracket incentives, coach incentives, and squad-rotation evidence.

Use `data/source-coverage.json` and `docs/prediction-calibration.md` as the standing data-gap closure plan. Schedule/results/rankings should be refreshed from official structured sources. Weather, bracket path incentives, odds movement, expert views, injuries, suspensions, and likely lineups need timestamped snapshots or official/reputable late team-news verification before confidence is raised.

For Match 017 onward, every new or refreshed prediction must include three scoreline scenarios in addition to the three-way win/draw/loss probabilities:

- `primary`: the headline scoreline aligned with the published lean.
- `conservative_draw_path`: the lower-margin or draw route that best reflects unresolved gaps.
- `upside_alternate`: the higher-margin or underdog route that captures the main volatility risk.

Scenario probabilities are single-score estimates and do not need to sum to 100%.

All prediction reasoning is specified to use the ChatGPT 5.5 ultra-high reasoning model. Publish concise reasoning summaries only. Do not store hidden chain-of-thought or private reasoning traces.

Each prediction record in `data/predictions.json` must include two image values:

- `lead_image_file`: the first share image. It must introduce the fixture only and must not output scoreline, predicted winner, win/draw/loss wording, probabilities, or result language.
- `image_file`: the second share image. It keeps the existing prediction-card convention and may include the predicted result, scoreline, confidence, and key risk framing.

Both images must exist under `assets/cards/`. The prediction file plus the corresponding daily report must embed both images in that order: `lead_image_file` first, `image_file` second.

Generate the first prediction image with this instruction pattern:

```text
$imagegen: 生成【社交平台赛事预测首图】，16:9 横版，真实位图图片，只展示赛事对阵、比赛阶段、城市/场馆氛围和球队色彩；中文文档配图的主要比赛信息必须使用简体中文，可在画面合适位置保留英文队名/赛事信息作为辅助文字；不输出比分，不输出预测胜负，不输出概率，不使用胜/平/负、晋级、爆冷等结果暗示词；不要生成 SVG，不要生成 HTML，不要生成代码图，不要生成线框图，不要使用官方 FIFA 标志或水印。
```

Generate the second prediction image with this instruction pattern:

```text
$imagegen: 生成【社交平台赛事预测配图】，16:9 横版，真实位图图片，用于抖音、小红书、微博和微信分享；中文文档配图的主要比赛信息必须使用简体中文，可在画面合适位置保留英文队名/赛事信息作为辅助文字；不要生成 SVG，不要生成 HTML，不要生成代码图，不要生成线框图，不要使用官方 FIFA 标志或水印。
```

Images must be raster files such as PNG, JPG, JPEG, or WebP. Do not create SVG, HTML, canvas, Mermaid, chart-only, or script-generated image substitutes for prediction share images.

Generated public artifacts must be bilingual. For every generated English prediction or daily report, maintain a Simplified Chinese counterpart, link the language pair from both files, and embed the same two share images in both versions.

## Daily Overview Requirements

When a daily report covers two or more predicted matches on the same China-time date, create a daily prediction overview card in `assets/cards/`, named with the pattern `daily-YYYY-MM-DD-summary.<png|jpg|jpeg|webp>`.

The daily overview card is a supplement and must not replace per-match `lead_image_file` or `image_file` assets. It must be generated with `$imagegen` as a real raster image. Do not use SVG, HTML, Mermaid, canvas, chart-only images, or script-generated substitutes.

The overview card must summarize each match with:

- China-time kickoff.
- Matchup.
- Win/draw/loss probability summary.
- Three scoreline scenarios: `primary`, `conservative_draw_path`, and `upside_alternate`.
- The public `rationale` for each scenario, tied directly to that scoreline rather than written as a generic match reason.

If one image would become too crowded, split the same date into multiple overview cards. A four-match date should normally fit one 16:9 landscape card.

The daily report must embed the overview card before per-match images and include:

- `## Summary Card Notes` / `## 总览图说明`: a short paragraph explaining how to read the card, what evidence was used, what late variables can change the forecast, and the investment-advice disclaimer.
- `## Scoreline Scenario Overview` / `## 比分情景总览`: a table that lists every match and the rationale attached to each scoreline scenario.

## Platform Copy Requirements

Prediction files should include share-ready copy suitable for Douyin, Xiaohongshu, Weibo, and WeChat. The copy should be concise, factual, and clear that the content is a sports prediction. Maintain standing platform announcement copy in `docs/platform-copy.md` and `docs/platform-copy.zh-CN.md` explaining that the account will use ChatGPT's highest reasoning model during the World Cup to predict match outcomes, scorelines, and key risks.

Daily automation runs that publish or refresh predictions must prepare share-ready text and image assets. After validation, use the connected Gmail tool to read the current Gmail profile email address and send the daily result summary plus generated images to that Google mailbox. Do not use Git config email addresses, GitHub account emails, or repository metadata as the recipient.

Every share-ready copy block must include a disclaimer equivalent to:

```text
This is a match prediction only and does not constitute investment advice.
```

Chinese copy should include:

```text
仅为足球赛事预测，不构成任何投资建议。
```

## Review Requirements

Each completed match should receive a post-match review in `reviews/` before the match status becomes `reviewed`.

Reviews must compare:

- predicted winner vs actual winner
- predicted scoreline vs final score
- assumptions that held up
- assumptions that failed
- future model adjustment notes

When useful, reviews should add calibration error tags such as `draw_underweighted`, `favorite_margin_overstated`, `clean_sheet_overstated`, `underdog_resilience_underweighted`, `transition_risk_underweighted`, `set_piece_risk_underweighted`, or `data_gap_overconfidence`.

## Validation

Run:

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

The validation script must fail when required prediction sections or referenced artifacts are missing.

## Commit Rules

- Do not commit `docs/local/`.
- Do not commit local credentials, secrets, or generated junk.
- Keep source URLs and verification timestamps with data updates.
- Use focused commit messages, for example `data: update world cup snapshot 2026-06-11`.

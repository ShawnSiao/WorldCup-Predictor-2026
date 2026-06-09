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
4. Create reviews for completed matches.
5. Update the daily report in `reports/daily/`.
6. Refresh README dashboard counters and links when visible state changes.
7. Run validation.
8. Commit and push only repository artifacts, never local specs.

## Prediction Requirements

Every prediction file in `predictions/` must include:

- `## Prediction`
- `## Factual Basis`
- `## Prediction Logic`
- `## Risk Factors`
- `## Platform Share Copy`
- `## Disclaimer`
- `## Source Snapshot`

Prediction reasoning must be based on current facts such as official schedule, venue, team strength, rankings, squad availability, recent form, and verified source updates.

All prediction reasoning is specified to use the ChatGPT 5.5 ultra-high reasoning model. Publish concise reasoning summaries only. Do not store hidden chain-of-thought or private reasoning traces.

## Platform Copy Requirements

Prediction files should include share-ready copy suitable for Douyin, Xiaohongshu, Weibo, and WeChat. The copy should be concise, factual, and clear that the content is a sports prediction.

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

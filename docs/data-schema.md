# Data Schema

[English](data-schema.md) | [简体中文](data-schema.zh-CN.md) | [Changelog](../CHANGELOG.md)

## Match Status

Matches move through:

```text
scheduled -> predicted -> live -> final -> reviewed
```

Allowed values:

- `scheduled`
- `predicted`
- `live`
- `final`
- `reviewed`

## Files

| File | Purpose |
| --- | --- |
| `AGENTS.md` | AI working index and repository maintenance rules. |
| `assets/cards/` | `$imagegen` generated raster prediction-card images used by prediction pages, daily reports, and email delivery. |
| `data/matches.json` | Canonical schedule and match lifecycle state. |
| `data/teams.json` | Team metadata and group assignments. |
| `data/venues.json` | Venue metadata. |
| `data/players.json` | Player-level squad data. |
| `data/rankings.json` | FIFA ranking snapshots. |
| `data/source-coverage.json` | Source coverage checklist for closing prediction data gaps. |
| `data/predictions.json` | Index of prediction files and prediction summaries. Generated predictions should maintain both English and Simplified Chinese files. |
| `data/results.json` | Official final result records. |
| `data/review-index.json` | Index of post-match review files. |

## Prediction Images

Each record in `data/predictions.json` must include:

- `lead_image_file`: first share image under `assets/cards/`; introduces the fixture only and omits scoreline, predicted winner, win/draw/loss wording, probabilities, and result language.
- `image_file`: second share image under `assets/cards/`; keeps the existing prediction-card convention and may include the predicted result and scoreline.

Prediction files and their corresponding daily reports embed both images in that order.

## Prediction Scoreline Scenarios

For Match 017 onward, each prediction record must include `scoreline_scenarios` with exactly three entries:

- `label`: `primary`, `conservative_draw_path`, or `upside_alternate`.
- `scoreline`: a scoreline string such as `2-1`.
- `probability`: a single-score estimate between 0 and 1.
- `rationale`: concise public explanation for that path.

Scenario probabilities are not exhaustive and do not need to sum to 1.00.

## Validation

Run:

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

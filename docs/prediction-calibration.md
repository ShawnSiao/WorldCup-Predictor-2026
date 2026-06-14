# Prediction Calibration

[English](prediction-calibration.md) | [简体中文](prediction-calibration.zh-CN.md) | [Methodology](methodology.md)

This document defines the calibration layer used after the evidence pass and before publishing probabilities, scorelines, confidence, and share copy.

## Data Gap Closure

Data gaps are closed in three tiers:

| Tier | Gap type | Action |
| --- | --- | --- |
| Automatic | schedule, venue, result, ranking, squad-publication status | Refresh structured data from FIFA, official federation hubs, and reputable fixture/result cross-checks. |
| Semi-automatic | weather, pitch/roof context, public market movement, expert previews | Pull or manually snapshot reputable sources at T-72h, T-24h, and T-6h; label stale or unavailable values. |
| Manual verification | injuries, suspensions, likely lineups, late player availability | Check official press conferences, federation updates, official lineups, and reputable team-news reports before raising confidence. |

`data/source-coverage.json` is the working checklist for these tiers. A prediction may still publish with gaps, but each unresolved gap must reduce confidence and must not be treated as evidence.

## Calibration Rules

- Group-stage draw floor: if the favorite is below 60%, keep draw probability near 28%-32% unless verified evidence strongly argues otherwise.
- Favorite cap: avoid pushing a team above 60% without strong ranking, squad, tactical, availability, and market support.
- Clean-sheet caution: avoid 2-0 or 3-0 as the only scoreline path when the opponent has verified transition, set-piece, or crowd/host-context routes.
- Data-gap penalty: missing injuries/lineups/weather/market movement keeps confidence at `medium` or lower; two or more major gaps should usually cap confidence at `medium-low`.
- Dissenting case: every prediction must explicitly state the most plausible route to the non-primary outcome.

## Scoreline Scenarios

For Match 017 onward, every new or refreshed prediction must provide three scoreline scenarios:

| Scenario | Meaning |
| --- | --- |
| Primary | The headline scoreline aligned with the published outcome lean. |
| Conservative / draw path | The lower-margin or draw route most consistent with the evidence gaps. |
| Upside / alternate | A higher-margin or underdog route that captures the main volatility risk. |

Scenario probabilities are top-scoreline estimates, not a complete probability distribution. They do not need to sum to 100%, because other scorelines remain possible.

## Daily Overview Cards

For daily reports with two or more predicted matches on the same China-time date, add one daily overview card after the snapshot and before the per-match images.

The overview card should show each match as one row or compact block:

- kickoff in China time
- matchup
- win/draw/loss probabilities
- primary scoreline with its scenario rationale
- conservative / draw scoreline with its scenario rationale
- upside / alternate scoreline with its scenario rationale

The rationale must come from the matching scoreline scenario. Do not use one generic reason for the whole match when the image displays multiple scoreline paths.

Each daily report must include a short `Summary Card Notes` section explaining how to read the card, which evidence families were used, which late variables can change the forecast, and that the content does not constitute investment advice.

## Review Feedback Tags

Post-match reviews should add one or more structured error tags when useful:

- `draw_underweighted`
- `favorite_margin_overstated`
- `favorite_margin_understated`
- `clean_sheet_overstated`
- `underdog_resilience_underweighted`
- `transition_risk_underweighted`
- `set_piece_risk_underweighted`
- `data_gap_overconfidence`

These tags guide the next daily run's calibration but do not rewrite already-published pre-kickoff predictions.

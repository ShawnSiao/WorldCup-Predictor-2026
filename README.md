# WorldCup-Predictor-2026

[English](README.md) | [简体中文](docs/README.zh-CN.md) | [Changelog](CHANGELOG.md)

![Project status](https://img.shields.io/badge/status-active%20tracking-1f883d)
![World Cup](https://img.shields.io/badge/world%20cup-2026-1f883d)
![Reasoning](https://img.shields.io/badge/reasoning-ChatGPT%205.5-blue)
![Docs](https://img.shields.io/badge/docs-EN%20%2F%20ZH--CN-0969da)

Track the 2026 FIFA World Cup schedule, publish match-by-match predictions, and review every prediction after the final whistle.

## Dashboard

| Item | Status |
| --- | --- |
| Data snapshot | 2026-06-17 |
| Tournament window | 2026-06-11 to 2026-07-19 |
| Official match count | 104 |
| Tracked matches in repository | 24 |
| Predictions published | 24 |
| Final results tracked | 20 |
| Post-match reviews published | 20 |

## Next Matches

| Match | Stage | Kickoff | Venue | Prediction |
| --- | --- | --- | --- | --- |
| Portugal vs Congo DR | Group K | 2026-06-17 17:00 UTC | Houston Stadium | [Portugal win, 3-1](predictions/match-023-por-cod.md) / [简体中文](predictions/match-023-por-cod.zh-CN.md) |
| England vs Croatia | Group L | 2026-06-17 20:00 UTC | Dallas Stadium | [England win, 2-1](predictions/match-022-eng-cro.md) / [简体中文](predictions/match-022-eng-cro.zh-CN.md) |
| Ghana vs Panama | Group L | 2026-06-17 23:00 UTC | Toronto Stadium | [Ghana win, 1-0](predictions/match-021-gha-pan.md) / [简体中文](predictions/match-021-gha-pan.zh-CN.md) |
| Uzbekistan vs Colombia | Group M | 2026-06-18 02:00 UTC | Mexico City Stadium | [Colombia win, 2-1](predictions/match-024-uzb-col.md) / [简体中文](predictions/match-024-uzb-col.zh-CN.md) |

## Daily Overview Card

[![China-time 2026-06-18 prediction overview card](assets/cards/daily-2026-06-18-summary.png)](reports/daily/2026-06-18.md)

The overview card groups the same China-time date into one share image and links each scoreline scenario to its own rationale.

## Featured Prediction Image Sets

[![Mexico vs South Africa lead prediction image](assets/cards/match-001-mex-rsa-lead.png)](predictions/match-001-mex-rsa.md)
[![Korea Republic vs Czechia lead prediction image](assets/cards/match-002-kor-cze-lead.png)](predictions/match-002-kor-cze.md)
[![Canada vs Bosnia and Herzegovina lead prediction image](assets/cards/match-003-can-bih-lead.png)](predictions/match-003-can-bih.md)
[![USA vs Paraguay lead prediction image](assets/cards/match-004-usa-par-lead.png)](predictions/match-004-usa-par.md)
[![Haiti vs Scotland lead prediction image](assets/cards/match-005-hai-sco-lead.png)](predictions/match-005-hai-sco.md)
[![Australia vs Türkiye lead prediction image](assets/cards/match-006-aus-tur-lead.png)](predictions/match-006-aus-tur.md)
[![Brazil vs Morocco lead prediction image](assets/cards/match-007-bra-mar-lead.png)](predictions/match-007-bra-mar.md)
[![Qatar vs Switzerland lead prediction image](assets/cards/match-008-qat-sui-lead.png)](predictions/match-008-qat-sui.md)
[![Côte d'Ivoire vs Ecuador lead prediction image](assets/cards/match-009-civ-ecu-lead.png)](predictions/match-009-civ-ecu.md)
[![Germany vs Curaçao lead prediction image](assets/cards/match-010-ger-cuw-lead.png)](predictions/match-010-ger-cuw.md)
[![Netherlands vs Japan lead prediction image](assets/cards/match-011-ned-jpn-lead.png)](predictions/match-011-ned-jpn.md)
[![Sweden vs Tunisia lead prediction image](assets/cards/match-012-swe-tun-lead.png)](predictions/match-012-swe-tun.md)
[![Saudi Arabia vs Uruguay lead prediction image](assets/cards/match-013-ksa-uru-lead.png)](predictions/match-013-ksa-uru.md)
[![Spain vs Cabo Verde lead prediction image](assets/cards/match-014-esp-cpv-lead.png)](predictions/match-014-esp-cpv.md)
[![IR Iran vs New Zealand lead prediction image](assets/cards/match-015-irn-nzl-lead.png)](predictions/match-015-irn-nzl.md)
[![Belgium vs Egypt lead prediction image](assets/cards/match-016-bel-egy-lead.png)](predictions/match-016-bel-egy.md)
[![France vs Senegal lead prediction image](assets/cards/match-017-fra-sen-lead.png)](predictions/match-017-fra-sen.md)
[![Iraq vs Norway lead prediction image](assets/cards/match-018-irq-nor-lead.png)](predictions/match-018-irq-nor.md)
[![Argentina vs Algeria lead prediction image](assets/cards/match-019-arg-alg-lead.png)](predictions/match-019-arg-alg.md)
[![Austria vs Jordan lead prediction image](assets/cards/match-020-aut-jor-lead.png)](predictions/match-020-aut-jor.md)
[![Ghana vs Panama lead prediction image](assets/cards/match-021-gha-pan-lead.png)](predictions/match-021-gha-pan.md)
[![England vs Croatia lead prediction image](assets/cards/match-022-eng-cro-lead.png)](predictions/match-022-eng-cro.md)
[![Portugal vs Congo DR lead prediction image](assets/cards/match-023-por-cod-lead.png)](predictions/match-023-por-cod.md)
[![Uzbekistan vs Colombia lead prediction image](assets/cards/match-024-uzb-col-lead.png)](predictions/match-024-uzb-col.md)

Share images live under [`assets/cards/`](assets/cards/). Each prediction embeds a fixture-only lead image first and the result prediction card second.

## Today

Reviews are now complete for all verified finals through Match 020. The next China-time matchday window covers Portugal vs Congo DR, England vs Croatia, Ghana vs Panama, and Uzbekistan vs Colombia, with calibration updated for favorite margin, clean-sheet risk, set pieces, and transition paths.

## Reasoning Model

All prediction reasoning is specified to use the ChatGPT 5.5 ultra-high reasoning model.

The repository publishes concise reasoning summaries only. It does not store hidden chain-of-thought or private reasoning traces.

## Platform Announcement Copy

During the World Cup, social-platform posts will explain that the account uses ChatGPT's highest reasoning model for match-by-match football predictions, including outcome lean, projected scoreline, confidence, and key risks. Ready-to-publish English and Simplified Chinese copy is maintained in [Platform Publishing Copy](docs/platform-copy.md).

## How The Repository Works

- `data/` stores structured schedule, team, venue, ranking, prediction, result, and review indexes.
- `predictions/` stores immutable pre-match prediction files.
- `reviews/` stores post-match reviews after official results are confirmed.
- `reports/daily/` stores daily tracking reports.
- `docs/` stores methodology, sources, and data schema documentation.

Each match moves through this lifecycle:

```text
scheduled -> predicted -> live -> final -> reviewed
```

## Current Artifacts

- Latest prediction: [Match 024: Uzbekistan vs Colombia](predictions/match-024-uzb-col.md)
- Latest review: [Match 020: Austria vs Jordan](reviews/match-020-aut-jor.md)
- Latest daily report: [2026-06-18](reports/daily/2026-06-18.md)
- Methodology: [Prediction and review methodology](docs/methodology.md) / [简体中文](docs/methodology.zh-CN.md)
- Calibration: [Prediction calibration](docs/prediction-calibration.md) / [简体中文](docs/prediction-calibration.zh-CN.md)
- Data schema: [Repository data schema](docs/data-schema.md) / [简体中文](docs/data-schema.zh-CN.md)
- Sources: [Source policy and current source list](docs/sources.md) / [简体中文](docs/sources.zh-CN.md)

## Roadmap

- [x] Create the repository and bilingual documentation.
- [x] Document the prediction reasoning model.
- [x] Add data, prediction, review, and report structure.
- [x] Publish the first pre-match prediction.
- [ ] Expand `data/matches.json` to the full 104-match official schedule.
- [ ] Add full squad snapshots for all 48 teams.
- [ ] Create daily updates during the tournament.
- [ ] Publish post-match reviews after each final result.

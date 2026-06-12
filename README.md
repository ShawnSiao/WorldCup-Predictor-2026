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
| Data snapshot | 2026-06-12 |
| Tournament window | 2026-06-11 to 2026-07-19 |
| Official match count | 104 |
| Tracked matches in repository | 11 |
| Predictions published | 11 |
| Final results tracked | 2 |
| Post-match reviews published | 2 |

## Next Matches

| Match | Stage | Kickoff | Venue | Prediction |
| --- | --- | --- | --- | --- |
| Canada vs Bosnia and Herzegovina | Group B | 2026-06-12 19:00 UTC | Toronto Stadium | [Canada win, 2-1](predictions/match-003-can-bih.md) / [简体中文](predictions/match-003-can-bih.zh-CN.md) |
| USA vs Paraguay | Group D | 2026-06-13 01:00 UTC | Los Angeles Stadium | [USA win, 2-1](predictions/match-004-usa-par.md) / [简体中文](predictions/match-004-usa-par.zh-CN.md) |
| Qatar vs Switzerland | Group B | 2026-06-13 19:00 UTC | San Francisco Bay Area Stadium | [Switzerland win, 2-0](predictions/match-008-qat-sui.md) / [简体中文](predictions/match-008-qat-sui.zh-CN.md) |
| Brazil vs Morocco | Group C | 2026-06-13 22:00 UTC | New York New Jersey Stadium | [Brazil win, 2-1](predictions/match-007-bra-mar.md) / [简体中文](predictions/match-007-bra-mar.zh-CN.md) |
| Haiti vs Scotland | Group C | 2026-06-14 01:00 UTC | Boston Stadium | [Scotland win, 2-1](predictions/match-005-hai-sco.md) / [简体中文](predictions/match-005-hai-sco.zh-CN.md) |
| Australia vs Türkiye | Group D | 2026-06-14 04:00 UTC | BC Place Vancouver | [Türkiye win, 2-1](predictions/match-006-aus-tur.md) / [简体中文](predictions/match-006-aus-tur.zh-CN.md) |
| Germany vs Curaçao | Group E | 2026-06-14 17:00 UTC | Houston Stadium | [Germany win, 3-0](predictions/match-010-ger-cuw.md) / [简体中文](predictions/match-010-ger-cuw.zh-CN.md) |
| Netherlands vs Japan | Group F | 2026-06-14 20:00 UTC | Dallas Stadium | [Netherlands win, 2-1](predictions/match-011-ned-jpn.md) / [简体中文](predictions/match-011-ned-jpn.zh-CN.md) |
| Côte d'Ivoire vs Ecuador | Group E | 2026-06-14 23:00 UTC | Philadelphia Stadium | [Draw, 1-1](predictions/match-009-civ-ecu.md) / [简体中文](predictions/match-009-civ-ecu.zh-CN.md) |

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

Share images live under [`assets/cards/`](assets/cards/). Each prediction embeds a fixture-only lead image first and the result prediction card second.

## Today

Mexico opened the tournament with a 2-0 win over South Africa, and Korea Republic followed with a 2-1 comeback win over Czechia. The current 72-hour prediction window runs through Côte d'Ivoire vs Ecuador on 2026-06-14 23:00 UTC.

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

- Latest prediction: [Match 011: Netherlands vs Japan](predictions/match-011-ned-jpn.md)
- Latest review: [Match 002: Korea Republic vs Czechia](reviews/match-002-kor-cze.md)
- Latest daily report: [2026-06-12](reports/daily/2026-06-12.md)
- Methodology: [Prediction and review methodology](docs/methodology.md) / [简体中文](docs/methodology.zh-CN.md)
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

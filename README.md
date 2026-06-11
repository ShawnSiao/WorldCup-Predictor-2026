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
| Data snapshot | 2026-06-11 |
| Tournament window | 2026-06-11 to 2026-07-19 |
| Official match count | 104 |
| Tracked matches in repository | 8 |
| Predictions published | 8 |
| Final results tracked | 0 |
| Post-match reviews published | 0 |

## Next Matches

| Match | Stage | Kickoff | Venue | Prediction |
| --- | --- | --- | --- | --- |
| Mexico vs South Africa | Group A | 2026-06-11 19:00 UTC | Mexico City Stadium | [Mexico win, 2-0](predictions/match-001-mex-rsa.md) / [简体中文](predictions/match-001-mex-rsa.zh-CN.md) |
| Korea Republic vs Czechia | Group A | 2026-06-12 02:00 UTC | Estadio Guadalajara | [Draw, 1-1](predictions/match-002-kor-cze.md) / [简体中文](predictions/match-002-kor-cze.zh-CN.md) |
| Canada vs Bosnia and Herzegovina | Group B | 2026-06-12 19:00 UTC | Toronto Stadium | [Canada win, 2-1](predictions/match-003-can-bih.md) / [简体中文](predictions/match-003-can-bih.zh-CN.md) |
| USA vs Paraguay | Group D | 2026-06-13 01:00 UTC | Los Angeles Stadium | [USA win, 2-1](predictions/match-004-usa-par.md) / [简体中文](predictions/match-004-usa-par.zh-CN.md) |
| Qatar vs Switzerland | Group B | 2026-06-13 19:00 UTC | San Francisco Bay Area Stadium | [Switzerland win, 2-0](predictions/match-008-qat-sui.md) / [简体中文](predictions/match-008-qat-sui.zh-CN.md) |
| Brazil vs Morocco | Group C | 2026-06-13 22:00 UTC | New York New Jersey Stadium | [Brazil win, 2-1](predictions/match-007-bra-mar.md) / [简体中文](predictions/match-007-bra-mar.zh-CN.md) |
| Haiti vs Scotland | Group C | 2026-06-14 01:00 UTC | Boston Stadium | [Scotland win, 2-1](predictions/match-005-hai-sco.md) / [简体中文](predictions/match-005-hai-sco.zh-CN.md) |
| Australia vs Türkiye | Group D | 2026-06-14 04:00 UTC | BC Place Vancouver | [Türkiye win, 2-1](predictions/match-006-aus-tur.md) / [简体中文](predictions/match-006-aus-tur.zh-CN.md) |

## Featured Prediction Cards

[![Mexico vs South Africa prediction card](assets/cards/match-001-mex-rsa.png)](predictions/match-001-mex-rsa.md)
[![Korea Republic vs Czechia prediction card](assets/cards/match-002-kor-cze.png)](predictions/match-002-kor-cze.md)
[![Canada vs Bosnia and Herzegovina prediction card](assets/cards/match-003-can-bih.png)](predictions/match-003-can-bih.md)
[![USA vs Paraguay prediction card](assets/cards/match-004-usa-par.png)](predictions/match-004-usa-par.md)
[![Haiti vs Scotland prediction card](assets/cards/match-005-hai-sco.png)](predictions/match-005-hai-sco.md)
[![Australia vs Türkiye prediction card](assets/cards/match-006-aus-tur.png)](predictions/match-006-aus-tur.md)
[![Brazil vs Morocco prediction card](assets/cards/match-007-bra-mar.png)](predictions/match-007-bra-mar.md)
[![Qatar vs Switzerland prediction card](assets/cards/match-008-qat-sui.png)](predictions/match-008-qat-sui.md)

Share images live under [`assets/cards/`](assets/cards/).

## Today

Opening day is scheduled for 2026-06-11. Mexico vs South Africa kicks off at 19:00 UTC, and Korea Republic vs Czechia follows at 02:00 UTC on 2026-06-12.

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

- Latest prediction: [Match 008: Qatar vs Switzerland](predictions/match-008-qat-sui.md)
- Latest daily report: [2026-06-11](reports/daily/2026-06-11.md)
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

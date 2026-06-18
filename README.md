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
| Data snapshot | 2026-06-18 |
| Tournament window | 2026-06-11 to 2026-07-19 |
| Official match count | 104 |
| Tracked matches in repository | 28 |
| Predictions published | 28 |
| Final results tracked | 24 |
| Post-match reviews published | 24 |

## Next Matches

| Match | Stage | Kickoff | Venue | Prediction |
| --- | --- | --- | --- | --- |
| Czechia vs South Africa | Group A | 2026-06-18 16:00 UTC / 2026-06-19 00:00 China time | Atlanta Stadium | [Czechia win, 2-0](predictions/match-025-cze-rsa.md) / [简体中文](predictions/match-025-cze-rsa.zh-CN.md) |
| Switzerland vs Bosnia and Herzegovina | Group B | 2026-06-18 19:00 UTC / 2026-06-19 03:00 China time | Los Angeles Stadium | [Switzerland win, 1-0](predictions/match-026-sui-bih.md) / [简体中文](predictions/match-026-sui-bih.zh-CN.md) |
| Canada vs Qatar | Group B | 2026-06-18 22:00 UTC / 2026-06-19 06:00 China time | BC Place Vancouver | [Canada win, 2-1](predictions/match-027-can-qat.md) / [简体中文](predictions/match-027-can-qat.zh-CN.md) |
| Mexico vs Korea Republic | Group A | 2026-06-19 01:00 UTC / 2026-06-19 09:00 China time | Estadio Guadalajara | [Mexico win, 2-1](predictions/match-028-mex-kor.md) / [简体中文](predictions/match-028-mex-kor.zh-CN.md) |

## Daily Overview Card

[![China-time 2026-06-19 prediction overview card](assets/cards/daily-2026-06-19-summary.png)](reports/daily/2026-06-19.md)

The overview card groups the same China-time date into one share image and links each scoreline scenario to its own rationale.

## Featured Prediction Image Sets

[![Mexico vs South Africa lead prediction image](assets/cards/match-001-mex-rsa-lead.png)](predictions/match-001-mex-rsa.md)
[![Korea Republic vs Czechia lead prediction image](assets/cards/match-002-kor-cze-lead.png)](predictions/match-002-kor-cze.md)
[![Canada vs Bosnia and Herzegovina lead prediction image](assets/cards/match-003-can-bih-lead.png)](predictions/match-003-can-bih.md)
[![USA vs PAR lead prediction image](assets/cards/match-004-usa-par-lead.png)](predictions/match-004-usa-par.md)
[![HAI vs SCO lead prediction image](assets/cards/match-005-hai-sco-lead.png)](predictions/match-005-hai-sco.md)
[![AUS vs TUR lead prediction image](assets/cards/match-006-aus-tur-lead.png)](predictions/match-006-aus-tur.md)
[![BRA vs MAR lead prediction image](assets/cards/match-007-bra-mar-lead.png)](predictions/match-007-bra-mar.md)
[![Qatar vs Switzerland lead prediction image](assets/cards/match-008-qat-sui-lead.png)](predictions/match-008-qat-sui.md)
[![CIV vs ECU lead prediction image](assets/cards/match-009-civ-ecu-lead.png)](predictions/match-009-civ-ecu.md)
[![GER vs CUW lead prediction image](assets/cards/match-010-ger-cuw-lead.png)](predictions/match-010-ger-cuw.md)
[![NED vs JPN lead prediction image](assets/cards/match-011-ned-jpn-lead.png)](predictions/match-011-ned-jpn.md)
[![SWE vs TUN lead prediction image](assets/cards/match-012-swe-tun-lead.png)](predictions/match-012-swe-tun.md)
[![KSA vs URU lead prediction image](assets/cards/match-013-ksa-uru-lead.png)](predictions/match-013-ksa-uru.md)
[![ESP vs CPV lead prediction image](assets/cards/match-014-esp-cpv-lead.png)](predictions/match-014-esp-cpv.md)
[![IRN vs NZL lead prediction image](assets/cards/match-015-irn-nzl-lead.png)](predictions/match-015-irn-nzl.md)
[![BEL vs EGY lead prediction image](assets/cards/match-016-bel-egy-lead.png)](predictions/match-016-bel-egy.md)
[![FRA vs SEN lead prediction image](assets/cards/match-017-fra-sen-lead.png)](predictions/match-017-fra-sen.md)
[![IRQ vs NOR lead prediction image](assets/cards/match-018-irq-nor-lead.png)](predictions/match-018-irq-nor.md)
[![ARG vs ALG lead prediction image](assets/cards/match-019-arg-alg-lead.png)](predictions/match-019-arg-alg.md)
[![AUT vs JOR lead prediction image](assets/cards/match-020-aut-jor-lead.png)](predictions/match-020-aut-jor.md)
[![Ghana vs Panama lead prediction image](assets/cards/match-021-gha-pan-lead.png)](predictions/match-021-gha-pan.md)
[![England vs Croatia lead prediction image](assets/cards/match-022-eng-cro-lead.png)](predictions/match-022-eng-cro.md)
[![Portugal vs Congo DR lead prediction image](assets/cards/match-023-por-cod-lead.png)](predictions/match-023-por-cod.md)
[![Uzbekistan vs Colombia lead prediction image](assets/cards/match-024-uzb-col-lead.png)](predictions/match-024-uzb-col.md)
[![Czechia vs South Africa lead prediction image](assets/cards/match-025-cze-rsa-lead.png)](predictions/match-025-cze-rsa.md)
[![Switzerland vs Bosnia and Herzegovina lead prediction image](assets/cards/match-026-sui-bih-lead.png)](predictions/match-026-sui-bih.md)
[![Canada vs Qatar lead prediction image](assets/cards/match-027-can-qat-lead.png)](predictions/match-027-can-qat.md)
[![Mexico vs Korea Republic lead prediction image](assets/cards/match-028-mex-kor-lead.png)](predictions/match-028-mex-kor.md)

Share images live under [`assets/cards/`](assets/cards/). Each prediction embeds a fixture-only lead image first and the result prediction card second.

## Today

Reviews are now complete for all verified finals through Match 024. The next China-time matchday window covers Czechia vs South Africa, Switzerland vs Bosnia and Herzegovina, Canada vs Qatar, and Mexico vs Korea Republic. Calibration now raises draw paths for favorites with unresolved late variables and separates favorite-margin upside from clean-sheet probability.

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

- Latest prediction: [Match 028: Mexico vs Korea Republic](predictions/match-028-mex-kor.md)
- Latest review: [Match 024: Uzbekistan vs Colombia](reviews/match-024-uzb-col.md)
- Latest daily report: [2026-06-19](reports/daily/2026-06-19.md)
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

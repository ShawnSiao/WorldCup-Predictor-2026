# WorldCup-Predictor-2026

[English](README.md) | [简体中文](docs/README.zh-CN.md) | [Changelog](CHANGELOG.md)

![Project status](https://img.shields.io/badge/status-planning-blue)
![World Cup](https://img.shields.io/badge/world%20cup-2026-1f883d)
![Languages](https://img.shields.io/badge/docs-EN%20%2F%20ZH--CN-0969da)

Track the 2026 FIFA World Cup schedule, record match-by-match predictions, and compare those predictions with final results.

This repository is in the initial setup phase. The schedule data, prediction workflow, and result-tracking tools will be added in later commits.

## What This Project Tracks

- Tournament schedule by group, round, venue, and kickoff time.
- Match predictions including winner, scoreline, confidence, and notes.
- Final results including score, winner, penalties when applicable, and prediction score.
- Historical prediction records for later analysis.

## Planned Data Model

| Entity | Purpose |
| --- | --- |
| `teams` | Qualified national teams and group assignments. |
| `matches` | Kickoff time, venue, group or knockout round, teams, and score. |
| `predictions` | Predicted winner, predicted scoreline, confidence, and notes. |
| `results` | Final score, winner, penalties when applicable, and points awarded. |

## Roadmap

- [x] Create the repository and initial documentation.
- [ ] Add structured schedule data.
- [ ] Add prediction records for each match.
- [ ] Add result comparison logic.
- [ ] Add summary views for prediction accuracy.

## Repository Status

Current status: project scaffold.

The repository does not yet contain the full 2026 FIFA World Cup schedule or prediction tooling.

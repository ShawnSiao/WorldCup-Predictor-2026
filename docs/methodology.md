# Prediction and Review Methodology

[English](../README.md) | [简体中文](methodology.zh-CN.md) | [Changelog](../CHANGELOG.md)

## Reasoning Model

All prediction reasoning is specified to use the ChatGPT 5.5 ultra-high reasoning model.

The repository publishes concise reasoning summaries. It does not store hidden chain-of-thought or private reasoning traces.

## Prediction Inputs

Each pre-match prediction should consider:

- official schedule, kickoff time, venue, and travel context
- FIFA ranking and ranking movement
- squad strength and player availability
- expected lineup and tactical matchup
- recent international form
- climate, rest days, and travel load
- group-state or knockout incentive context
- market odds only when the source is reputable and clearly labeled

## Prediction Output

Group-stage predictions include:

- home win probability
- draw probability
- away win probability
- predicted scoreline
- confidence level
- reasoning summary
- risk factors

Knockout predictions should add advancement probability and separate regulation-time outcome from extra-time or penalty scenarios.

## Review Method

Post-match reviews compare the prediction to the official final result.

Each review should record:

- actual score and winner
- key events and turning points
- whether the predicted winner was correct
- whether the scoreline was close
- which assumptions held up
- which assumptions failed
- model adjustment notes for later matches

Review ratings:

- `correct`: core outcome correct and match script close.
- `partial`: useful read, but material misses.
- `wrong`: core outcome missed.

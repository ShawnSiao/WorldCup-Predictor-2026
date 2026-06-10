# WorldCup-Predictor-2026

[English](../README.md) | [简体中文](README.zh-CN.md) | [更新日志](../CHANGELOG.md)

![项目状态](https://img.shields.io/badge/status-active%20tracking-1f883d)
![世界杯](https://img.shields.io/badge/world%20cup-2026-1f883d)
![推理模型](https://img.shields.io/badge/reasoning-ChatGPT%205.5-blue)
![文档语言](https://img.shields.io/badge/docs-EN%20%2F%20ZH--CN-0969da)

本仓库用于追踪 2026 年 FIFA 世界杯赛程，发布每场比赛的赛前预测，并在比赛结束后复盘预测表现。

## 仪表盘

| 项目 | 状态 |
| --- | --- |
| 数据快照 | 2026-06-10 |
| 赛事周期 | 2026-06-11 至 2026-07-19 |
| 官方比赛总数 | 104 |
| 仓库已追踪比赛 | 4 |
| 已发布预测 | 4 |
| 已追踪赛果 | 0 |
| 已发布复盘 | 0 |

## 近期比赛

| 比赛 | 阶段 | 开球时间 | 场地 | 预测 |
| --- | --- | --- | --- | --- |
| Mexico vs South Africa | Group A | 2026-06-11 19:00 UTC | Mexico City Stadium | [Mexico 胜，2-0](../predictions/match-001-mex-rsa.md) |
| Korea Republic vs Czechia | Group A | 2026-06-12 02:00 UTC | Estadio Guadalajara | [平局，1-1](../predictions/match-002-kor-cze.md) |
| Canada vs Bosnia and Herzegovina | Group B | 2026-06-12 19:00 UTC | Toronto Stadium | [Canada 胜，2-1](../predictions/match-003-can-bih.md) |
| USA vs Paraguay | Group D | 2026-06-13 01:00 UTC | Los Angeles Stadium | [USA 胜，2-1](../predictions/match-004-usa-par.md) |

## 预测配图

[![Mexico vs South Africa prediction card](../assets/cards/match-001-mex-rsa.png)](../predictions/match-001-mex-rsa.md)

[![Korea Republic vs Czechia prediction card](../assets/cards/match-002-kor-cze.png)](../predictions/match-002-kor-cze.md)

[![Canada vs Bosnia and Herzegovina prediction card](../assets/cards/match-003-can-bih.png)](../predictions/match-003-can-bih.md)

[![USA vs Paraguay prediction card](../assets/cards/match-004-usa-par.png)](../predictions/match-004-usa-par.md)

| 墨西哥 vs 南非 | A 组 | 2026-06-11 19:00 UTC | 墨西哥城体育场 | [墨西哥胜，2-0](../predictions/match-001-mex-rsa.zh-CN.md) / [English](../predictions/match-001-mex-rsa.md) |

## 重点预测配图

[![墨西哥 vs 南非预测配图](../assets/cards/match-001-mex-rsa.png)](../predictions/match-001-mex-rsa.zh-CN.md)

分享图片：[`assets/cards/match-001-mex-rsa.png`](../assets/cards/match-001-mex-rsa.png)

| 墨西哥 vs 南非 | A 组 | 2026-06-11 19:00 UTC | 墨西哥城体育场 | [墨西哥胜，2-0](../predictions/match-001-mex-rsa.zh-CN.md) / [English](../predictions/match-001-mex-rsa.md) |
| 韩国 vs 捷克 | A 组 | 2026-06-12 02:00 UTC | Estadio Guadalajara | [平局，1-1](../predictions/match-002-kor-cze.zh-CN.md) / [English](../predictions/match-002-kor-cze.md) |
| 加拿大 vs 波黑 | B 组 | 2026-06-12 19:00 UTC | Toronto Stadium | [加拿大胜，2-1](../predictions/match-003-can-bih.zh-CN.md) / [English](../predictions/match-003-can-bih.md) |
| 美国 vs 巴拉圭 | D 组 | 2026-06-13 01:00 UTC | Los Angeles Stadium | [美国胜，2-1](../predictions/match-004-usa-par.zh-CN.md) / [English](../predictions/match-004-usa-par.md) |

## 预测配图

[![墨西哥 vs 南非预测配图](../assets/cards/match-001-mex-rsa.png)](../predictions/match-001-mex-rsa.zh-CN.md)
[![韩国 vs 捷克预测配图](../assets/cards/match-002-kor-cze.png)](../predictions/match-002-kor-cze.zh-CN.md)
[![加拿大 vs 波黑预测配图](../assets/cards/match-003-can-bih.png)](../predictions/match-003-can-bih.zh-CN.md)
[![美国 vs 巴拉圭预测配图](../assets/cards/match-004-usa-par.png)](../predictions/match-004-usa-par.zh-CN.md)

分享图片目录：[`assets/cards/`](../assets/cards/)


## 今日赛程

2026-06-10 没有 FIFA World Cup 2026 比赛。

## 推理模型

所有预测推理均指定使用 ChatGPT 5.5 超高推理模型。

仓库只公开简明推理摘要，不保存隐藏推理链或私有推理过程。

## 平台说明文案

世界杯期间，社交平台发布内容会说明账号使用 ChatGPT 最高推理模型逐场预测比赛，包括胜平负倾向、预测比分、信心等级和关键风险。可直接发布的简体中文和英文文案维护在[平台发布文案](platform-copy.zh-CN.md)。

## 仓库结构

- `data/`：结构化赛程、球队、场地、排名、预测、赛果和复盘索引。
- `predictions/`：赛前预测文件。开球后不改写预测内容。
- `reviews/`：官方赛果确认后的赛后复盘。
- `reports/daily/`：每日追踪报告。
- `docs/`：预测方法、数据来源和数据结构说明。

每场比赛按以下状态推进：

```text
scheduled -> predicted -> live -> final -> reviewed
```

## 当前产物

- 最新预测：[Match 004: USA vs Paraguay](../predictions/match-004-usa-par.md)
- 最新日报：[2026-06-10](../reports/daily/2026-06-10.md)
- 最新预测：[第 001 场：墨西哥 vs 南非](../predictions/match-001-mex-rsa.zh-CN.md) / [English](../predictions/match-001-mex-rsa.md)
- 最新日报：[2026-06-09](../reports/daily/2026-06-09.zh-CN.md) / [English](../reports/daily/2026-06-09.md)
- 最新预测：[第 001 场：墨西哥 vs 南非](../predictions/match-001-mex-rsa.zh-CN.md) / [English](../predictions/match-001-mex-rsa.md)
- 最新日报：[2026-06-09](../reports/daily/2026-06-09.zh-CN.md) / [English](../reports/daily/2026-06-09.md)
- 最新预测：[第 001 场：墨西哥 vs 南非](../predictions/match-001-mex-rsa.zh-CN.md) / [English](../predictions/match-001-mex-rsa.md)
- 最新日报：[2026-06-09](../reports/daily/2026-06-09.zh-CN.md) / [English](../reports/daily/2026-06-09.md)
- 最新预测：[第 001 场：墨西哥 vs 南非](../predictions/match-001-mex-rsa.zh-CN.md) / [English](../predictions/match-001-mex-rsa.md)
- 最新日报：[2026-06-09](../reports/daily/2026-06-09.zh-CN.md) / [English](../reports/daily/2026-06-09.md)
- 方法说明：[预测与复盘方法](methodology.zh-CN.md)
- 最新预测：[第 004 场：美国 vs 巴拉圭](../predictions/match-004-usa-par.zh-CN.md) / [English](../predictions/match-004-usa-par.md)
- 最新日报：[2026-06-10](../reports/daily/2026-06-10.zh-CN.md) / [English](../reports/daily/2026-06-10.md)
- 方法说明：[预测与复盘方法](methodology.zh-CN.md) / [English](methodology.md)
- 最新预测：[第 004 场：美国 vs 巴拉圭](../predictions/match-004-usa-par.zh-CN.md) / [English](../predictions/match-004-usa-par.md)
- 最新日报：[2026-06-10](../reports/daily/2026-06-10.zh-CN.md) / [English](../reports/daily/2026-06-10.md)
- 方法说明：[预测与复盘方法](methodology.zh-CN.md) / [English](methodology.md)
- 数据结构：[数据结构](data-schema.zh-CN.md) / [English](data-schema.md)
- 来源说明：[来源政策与当前来源列表](sources.zh-CN.md) / [English](sources.md)

## 路线图

- [x] 创建仓库和双语文档。
- [x] 说明预测推理模型。
- [x] 添加数据、预测、复盘和日报结构。
- [x] 发布第一场赛前预测。
- [ ] 将 `data/matches.json` 扩展为官方 104 场完整赛程。
- [ ] 添加 48 支球队的完整球员名单快照。
- [ ] 在赛事期间创建每日更新。
- [ ] 每场比赛完赛后发布赛后复盘。

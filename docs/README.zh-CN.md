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
| 数据快照 | 2026-06-09 |
| 赛事周期 | 2026-06-11 至 2026-07-19 |
| 官方比赛总数 | 104 |
| 仓库已追踪比赛 | 1 |
| 已发布预测 | 1 |
| 已追踪赛果 | 0 |
| 已发布复盘 | 0 |

## 下一场比赛

| 比赛 | 阶段 | 开球时间 | 场地 | 预测 |
| --- | --- | --- | --- | --- |
| Mexico vs South Africa | Group A | 2026-06-11 19:00 UTC | Mexico City Stadium | [Mexico 胜，2-0](../predictions/match-001-mex-rsa.md) |

## 今日赛程

2026-06-09 没有 FIFA World Cup 2026 比赛。

## 推理模型

所有预测推理均指定使用 ChatGPT 5.5 超高推理模型。

仓库只公开简明推理摘要，不保存隐藏推理链或私有推理过程。

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

- 最新预测：[Match 001: Mexico vs South Africa](../predictions/match-001-mex-rsa.md)
- 最新日报：[2026-06-09](../reports/daily/2026-06-09.md)
- 方法说明：[预测与复盘方法](methodology.zh-CN.md)
- 数据结构：[Repository data schema](data-schema.md)
- 来源说明：[Source policy and current source list](sources.md)

## 路线图

- [x] 创建仓库和双语文档。
- [x] 说明预测推理模型。
- [x] 添加数据、预测、复盘和日报结构。
- [x] 发布第一场赛前预测。
- [ ] 将 `data/matches.json` 扩展为官方 104 场完整赛程。
- [ ] 添加 48 支球队的完整球员名单快照。
- [ ] 在赛事期间创建每日更新。
- [ ] 每场比赛完赛后发布赛后复盘。

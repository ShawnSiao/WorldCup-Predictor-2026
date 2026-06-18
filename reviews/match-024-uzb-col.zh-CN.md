# 第 024 场复盘：乌兹别克斯坦 vs 哥伦比亚

[复盘索引](README.zh-CN.md) | [English](match-024-uzb-col.md) | [预测](../predictions/match-024-uzb-col.zh-CN.md)

## 赛果

- 最终赛果：第 024 场 乌兹别克斯坦 1-3 哥伦比亚。
- 预测胜者：哥伦比亚。
- 实际胜者：哥伦比亚。
- 预测比分：乌兹别克斯坦 1-2 哥伦比亚。
- 复盘评级：正确。

## 判断成立部分

- 哥伦比亚胜负判断正确。
- 预测正确保留了乌兹别克斯坦进球路径。
- 哥伦比亚机会质量更强、乌兹别克斯坦依靠重启球和转换威胁的脚本成立。

## 判断失效部分

- 哥伦比亚分差低估一球。
- 大比分替代情景应包含 1-3，而不只是 0-2 零封拉开。

## 模型调整记录

- 热门队同时具备边路创造和转换强度时，大比分替代情景应允许 0-2 与 1-3 两条路径。
- 即使热门队分差上升，也要保留下风方进球风险。
- 校准标签：`favorite_margin_understated`, `set_piece_risk_retained`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021504
- https://www.theguardian.com/football/2026/jun/18/uzbekistan-colombia-world-cup-2026-match-report
- https://www.sportingnews.com/us/soccer/news/uzbekistan-colombia-live-score-result-world-cup/bc642d4e6f08b7ad7b7ebf6d
- 核验时间：2026-06-18T17:05:25+08:00

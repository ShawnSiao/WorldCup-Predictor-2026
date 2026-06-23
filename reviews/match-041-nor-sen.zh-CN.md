# 第 041 场复盘：挪威 vs 塞内加尔

[复盘索引](README.zh-CN.md) | [English](match-041-nor-sen.md) | [预测](../predictions/match-041-nor-sen.zh-CN.md)

## 赛果

- 最终赛果：第 041 场 挪威 3-2 塞内加尔。
- 预测胜者：平局。
- 实际胜者：NOR。
- 预测比分：挪威 vs 塞内加尔 2-2。
- 复盘评级：wrong。

## 命中的判断

- 高比分和双方都有进球的比赛脚本判断正确。
- 挪威直接进攻路线和塞内加尔回应能力都进入比赛，符合赛前开放局面风险。

## 失效的判断

- 平局倾向过于谨慎：挪威终结优势和后段控制把比赛带到 3-2，而不是 2-2。
- 塞内加尔第二球保留了胶着程度，但模型低估了挪威最终拉开一球的路径。

## 模型校准备注

- 当热门一方有清晰的顶级前锋路线，且双方已经制造转换机会时，主胜尾部需要高于单纯保平读法。
- 校准标签：`favorite_margin_underweighted`、`transition_risk_underweighted`。

## 来源快照

- https://www.foxsports.com/soccer/fifa-world-cup-men-norway-vs-senegal-jun-22-2026-game-boxscore-647656
- 核验时间：2026-06-23T21:48:00+08:00

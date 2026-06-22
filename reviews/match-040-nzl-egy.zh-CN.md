# 第 040 场复盘：新西兰 vs 埃及

[复盘索引](README.zh-CN.md) | [English](match-040-nzl-egy.md) | [预测](../predictions/match-040-nzl-egy.zh-CN.md)

## 结果

- 最终赛果：第 040 场 新西兰 1-3 埃及。
- 预测胜方：埃及。
- 实际胜方：埃及。
- 预测比分：新西兰 vs 埃及 1-2。
- 复盘评级：partial。

## 成立的判断

- 埃及胜和双方进球方向成立。
- 预测正确把 Salah / Marmoush 质量作为核心，同时保留新西兰 Wood 路线。

## 失效的判断

- 埃及后段拉开比分的概率被低估：实际为 1-3，而不是 1-2。
- 埃及控制比赛后，热门队扩大分差路线比主比分更接近。

## 模型校准记录

- 拥有更强转换攻击手的热门队，在弱势方被迫追赶时，需要更大的后段扩大分差尾部。
- 校准标签：`favorite_margin_underweighted`、`transition_risk_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021480
- https://www.foxsports.com/soccer/fifa-world-cup-men-new-zealand-vs-egypt-jun-21-2026-game-boxscore-647655
- 核验时间：2026-06-22T15:01:00+08:00

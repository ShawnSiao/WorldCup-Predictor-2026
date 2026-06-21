# 第 036 场复盘：突尼斯 vs 日本

[复盘索引](README.zh-CN.md) | [English](match-036-tun-jpn.md) | [预测](../predictions/match-036-tun-jpn.zh-CN.md)

## 赛果

- 最终赛果：突尼斯 0-4 日本。
- 预测胜方：日本。
- 实际胜方：日本。
- 预测比分：突尼斯 0-2 日本。
- 复盘评级：partial。

## 判断成立部分

- 日本胜负方向和零封方向正确。
- 预测正确依赖日本结构、技术稳定性，以及突尼斯首战后的动荡。
- 0-3 上限路线预见了日本早段进球后比分可能拉开。

## 判断偏差

- 比分差距仍被低估：日本最终 4-0，而非 0-2。
- 突尼斯换帅后的防守失序需要更高权重。
- 日本后段继续追加进球的能力建模不足。

## 模型调整记录

- 当一支球队同时面临战术错配和教练动荡时，下行尾部应更大。
- 校准标签：`favorite_margin_underweighted`、`opponent_disorganization_underweighted`、`clean_sheet_correct`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021475
- https://www.theguardian.com/football/2026/jun/21/japan-tunisia-world-cup-group-f-match-report
- https://www.theguardian.com/football/live/2026/jun/21/fifa-world-cup-2026-live-tunisia-v-japan-updates-tun-vs-jpn-group-f-match-score-latest
- https://www.espn.com/soccer/report/_/gameId/760449
- https://www.foxsports.com/soccer/fifa-world-cup-men-tunisia-vs-japan-jun-21-2026-game-boxscore-647651
- 核验时间：2026-06-21T16:30:00+08:00

# 第 075 场复盘：荷兰 vs 摩洛哥

[复盘索引](README.zh-CN.md) | [English](match-075-ned-mar.md) | [预测](../predictions/match-075-ned-mar.zh-CN.md)

## 结果

- 最终结果：第 075 场 荷兰 1-1 摩洛哥；摩洛哥点球 3-2 胜出。
- 预测胜者：荷兰。
- 实际胜者：摩洛哥。
- 预测比分：荷兰 vs 摩洛哥 2-1。
- 复盘评级：partial。

## 命中的判断

- 保守 / 平局路径为 1-1，命中常规时间比分。
- 预测正确指出摩洛哥紧凑防守和转换纪律是把比赛拖平的路线。

## 失效的判断

- 荷兰胜和晋级倾向错误。
- 模型仍给了荷兰过高的末段进攻深度权重，且低估摩洛哥点球韧性。

## 模型校准备注

- `draw_underweighted`、`underdog_resilience_underweighted`、`data_gap_overconfidence`；主情景和平局情景接近时，晋级概率要更重视点球方差。

## 来源快照

- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures
- https://www.fifa.com/en/match-centre/match/17/285023/289287/400021520
- https://www.aljazeera.com/sports/liveblog/2026/6/29/netherlands-vs-morocco-live-world-cup-2026-last-32-match-updates
- https://www.espn.com/soccer/report/_/gameId/760495
- https://www.foxsports.com/soccer/fifa-world-cup/scores
- 核验时间：2026-06-30T23:55:00+08:00

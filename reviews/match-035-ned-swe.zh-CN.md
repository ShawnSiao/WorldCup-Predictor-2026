# 第 035 场复盘：荷兰 vs 瑞典

[复盘索引](README.zh-CN.md) | [English](match-035-ned-swe.md) | [预测](../predictions/match-035-ned-swe.zh-CN.md)

## 赛果

- 最终赛果：荷兰 5-1 瑞典。
- 预测胜方：平局。
- 实际胜方：荷兰。
- 预测比分：荷兰 2-2 瑞典。
- 复盘评级：wrong。

## 判断成立部分

- 预测正确预期比赛会开放，边路和机会量都具备波动性。
- 瑞典确实制造了足够射门，说明比赛并非所有阶段都一边倒。

## 判断偏差

- 平局判断错误：荷兰把边路和中路压力转化为 5-1 大胜。
- Brian Brobbey 与 Cody Gakpo 的终结效率被严重低估。
- 瑞典在连续禁区压力下的防线崩盘，没有出现在上限情景里。

## 模型调整记录

- 当双方都有机会量时，终结能力更强的一方应获得更高的大比分情景权重。
- 校准标签：`favorite_margin_underweighted`、`defensive_fragility_underweighted`、`wide_area_risk_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021472
- https://www.theguardian.com/football/live/2026/jun/20/netherlands-v-sweden-world-cup-2026-live
- https://www.espn.com/soccer/match/_/gameId/760447
- 核验时间：2026-06-21T16:30:00+08:00

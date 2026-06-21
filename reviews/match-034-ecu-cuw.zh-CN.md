# 第 034 场复盘：厄瓜多尔 vs 库拉索

[复盘索引](README.zh-CN.md) | [English](match-034-ecu-cuw.md) | [预测](../predictions/match-034-ecu-cuw.zh-CN.md)

## 赛果

- 最终赛果：厄瓜多尔 0-0 库拉索。
- 预测胜方：厄瓜多尔。
- 实际胜方：平局。
- 预测比分：厄瓜多尔 2-0 库拉索。
- 复盘评级：wrong。

## 判断成立部分

- 厄瓜多尔场面控制判断方向正确，确实形成大量射门。
- 预测识别了库拉索低位防守和门将变量是主要风险。

## 判断偏差

- 胜负方向错误：厄瓜多尔 28 次射门最终变成 0-0。
- Eloy Room 的扑救表现和库拉索零封韧性被明显低估。
- 零封路径被更多分配给厄瓜多尔，而不是弱队守住比分的路径。

## 模型调整记录

- 当弱队门将状态和紧凑防守已被验证时，热门球队射门量不能自动等同于进球期望。
- 校准标签：`draw_underweighted`、`underdog_resilience_underweighted`、`data_gap_overconfidence`、`clean_sheet_overstated`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021465
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/ecuador-curacao-match-report-highlights
- https://www.theguardian.com/football/2026/jun/21/curacao-ecuador-world-cup-group-e-match-report
- https://www.skysports.com/football/news/29910/13553789/world-cup-2026-ecuador-0-0-curacao-eloy-room-makes-history-with-incredible-15-saves-to-earn-blue-wave-first-ever-point
- 核验时间：2026-06-21T16:30:00+08:00

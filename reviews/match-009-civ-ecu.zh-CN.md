# 第 009 场复盘：科特迪瓦 vs 厄瓜多尔

[首页](../docs/README.zh-CN.md) | [English](match-009-civ-ecu.md) | [预测](../predictions/match-009-civ-ecu.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 厄瓜多尔 | 科特迪瓦 |
| 比分 | 科特迪瓦 0-1 厄瓜多尔 | 科特迪瓦 1-0 厄瓜多尔 |
| 评级 | wrong | wrong |

## 比赛数据与条件

- 最终赛果：第 009 场科特迪瓦 1-0 厄瓜多尔。
- 预测评级：`wrong`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 小比分判断方向正确。
- 预测把比赛视为一球差拉扯，这一点成立。

## 失效的判断

- 决定性进球被放在了错误一方。
- 模型高估了厄瓜多尔中场控制的稳定性，低估了科特迪瓦直接进攻和后段冲击。
- 替补影响、转换执行和后段体能优势的权重不够。

## 后续可继承因素

- 势均力敌的跨洲对位里，身体对抗、后段冲刺和边路直接进攻不能低估。
- 一球差热门判断应继续贴近平局，除非有明确机会创造或终结证据。

## 模型调整记录

- 校准标签：`transition_risk_underweighted`、`underdog_resilience_underweighted`、`data_gap_overconfidence`。
- 当热门方优势很窄时，需要明确保留反向 1-0 路径，而不是把它当作极低概率尾部。

## 来源快照

- FIFA 赛程/赛果页：https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- ESPN 赛后报道：https://www.espn.com/soccer/story/_/id/49064087/ivory-coast-ecuador-live-world-cup-2026-latest-updates-commentary-score-result
- FOX Sports 集锦：https://www.foxsports.com/watch/fmc-43wd33qm20poy8zk
- 核验时间：2026-06-16T16:13:02+08:00

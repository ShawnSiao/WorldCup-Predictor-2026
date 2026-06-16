# 第 015 场复盘：伊朗 vs 新西兰

[首页](../docs/README.zh-CN.md) | [English](match-015-irn-nzl.md) | [预测](../predictions/match-015-irn-nzl.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 伊朗 | 平局 |
| 比分 | 伊朗 2-0 新西兰 | 伊朗 2-2 新西兰 |
| 评级 | wrong | wrong |

## 比赛数据与条件

- 最终赛果：第 015 场伊朗 2-2 新西兰。
- 预测评级：`wrong`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 伊朗两次回应并取得进球的能力真实存在。
- 场外和物流背景会影响比赛，这一点被提到过，但权重不够。

## 失效的判断

- 零封假设严重失败。
- 新西兰的进攻效率以及围绕 Chris Wood 的连接和跑动被低估。
- 模型没有充分计入伊朗备战受扰、政治压力和强制旅行安排。

## 后续可继承因素

- 政治和旅行扰动应同时降低信心、提高丢球概率和平局概率。
- 排名较低但有明确支点 + 跑动结构的球队，可以明显跑赢排名预期。
- 热门方能追平，不等于能控制比赛。

## 模型调整记录

- 校准标签：`draw_underweighted`、`clean_sheet_overstated`、`transition_risk_underweighted`、`data_gap_overconfidence`。
- 对存在签证、基地迁移、安保或旅行不确定性的球队，增加物流压力变量。

## 来源快照

- FIFA 比赛中心：https://www.fifa.com/en/match-centre/match/17/285023/289273/400021476
- Guardian 文字直播：https://www.theguardian.com/football/live/2026/jun/16/fifa-world-cup-2026-live-iran-v-new-zealand-updates-irn-vs-nzl-group-f-match-score-latest
- Al Jazeera 赛后报道：https://www.aljazeera.com/sports/2026/6/16/iran-draw-2-2-with-new-zealand-in-politically-charged-world-cup-match
- 核验时间：2026-06-16T16:13:02+08:00

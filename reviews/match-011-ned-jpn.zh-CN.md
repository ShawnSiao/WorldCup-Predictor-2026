# 第 011 场复盘：荷兰 vs 日本

[首页](../docs/README.zh-CN.md) | [English](match-011-ned-jpn.md) | [预测](../predictions/match-011-ned-jpn.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 荷兰 | 平局 |
| 比分 | 荷兰 2-1 日本 | 荷兰 2-2 日本 |
| 评级 | partial | partial |

## 比赛数据与条件

- 最终赛果：第 011 场荷兰 2-2 日本。
- 预测评级：`partial`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 比赛质量高、比分接近的判断成立。
- 日本压迫和转换威胁被正确识别为荷兰取胜倾向的主要风险。

## 失效的判断

- 平局风险仍然被低估。
- 模型没有充分计入日本落后后再次回应的能力。
- 后段注意力和下半场节奏变化比预测中更强。

## 后续可继承因素

- 日本式高压应被当作能改变赛果的变量，而不是单纯风格扰动。
- 两支强队都有转换路径时，平局概率应靠近小组赛平局地板的上沿。

## 模型调整记录

- 校准标签：`draw_underweighted`、`transition_risk_underweighted`、`underdog_resilience_underweighted`。
- 后续强队遇到高压球队时，可以保留一球小胜主情景，但必须抬高 1-1 或 2-2 情景。

## 来源快照

- FIFA 赛后报道：https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/netherlands-japan-highlights-match-report
- FOX Sports 文字直播：https://www.foxsports.com/live-blog/soccer/netherlands-vs-japan-live-updates-score-top-plays-from-group-showdown
- 核验时间：2026-06-16T16:13:02+08:00

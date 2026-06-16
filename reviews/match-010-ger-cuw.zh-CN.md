# 第 010 场复盘：德国 vs 库拉索

[首页](../docs/README.zh-CN.md) | [English](match-010-ger-cuw.md) | [预测](../predictions/match-010-ger-cuw.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 德国 | 德国 |
| 比分 | 德国 3-0 库拉索 | 德国 7-1 库拉索 |
| 评级 | correct | correct |

## 比赛数据与条件

- 最终赛果：第 010 场德国 7-1 库拉索。
- 预测评级：`correct`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 德国取胜方向正确。
- 模型正确识别了双方质量差距和德国对低位防守的持续施压能力。

## 失效的判断

- 一旦库拉索防线被连续打穿，模型低估了比分扩大的速度。
- 零封判断失败；即使强热门也可能被一次转换或注意力下降惩罚。

## 后续可继承因素

- 新军或低排名球队在先丢球后可能出现结构性崩盘。
- 强热门预测需要同时保留保守路径和大胜路径，不能只给受控 2-0 / 3-0。

## 模型调整记录

- 校准标签：`favorite_margin_understated`、`clean_sheet_overstated`。
- 继续控制热门方概率上限，但当强队深度和对手出球缺口都明确时，要扩大比分情景。

## 来源快照

- FIFA 赛程/赛果页：https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- Al Jazeera 赛后报道：https://www.aljazeera.com/sports/2026/6/14/germany-hit-curacao-for-seven-to-open-their-world-cup
- ESPN 赛后报道：https://www.espn.com/soccer/report/_/gameId/760422
- 核验时间：2026-06-16T16:13:02+08:00

# 第 051 场复盘：瑞士 vs 加拿大

[复盘索引](README.zh-CN.md) | [English](match-051-sui-can.md) | [预测](../predictions/match-051-sui-can.zh-CN.md)

## 赛果

- 最终赛果：第 051 场 瑞士 2-1 加拿大。
- 预测胜者：平局。
- 实际胜者：瑞士。
- 预测比分：瑞士 vs 加拿大 1-1。
- 复盘评级：wrong。

## 判断成立之处

- 一球差、均衡比赛脚本是准确的。
- 加拿大得分回应路径也被保留。

## 判断失效之处

- 平局权重过高，瑞士赢球路径被低估。
- 模型过度解读了双方都可接受平局的动机，忽略瑞士仍能终结比赛。

## 模型调整备注

- 均势小组形势不应让谨慎心态完全压过较强一方的后段制胜路径。
- 校准标签：`draw_overweighted`、`favorite_margin_understated`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021451
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/matchday-14-round-up-review-highlights
- 核验时间：2026-06-25T13:51:27+08:00

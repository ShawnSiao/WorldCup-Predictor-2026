# 第 022 场复盘：英格兰 vs 克罗地亚

[复盘索引](README.zh-CN.md) | [English](match-022-eng-cro.md) | [预测](../predictions/match-022-eng-cro.zh-CN.md)

## 赛果

- 最终赛果：第 022 场 英格兰 4-2 克罗地亚。
- 预测胜者：英格兰。
- 实际胜者：英格兰。
- 预测比分：英格兰 2-1 克罗地亚。
- 复盘评级：正确。

## 判断成立部分

- 胜负判断正确：英格兰前场上限更高。
- 预测保留了克罗地亚进球风险。
- 大体脚本抓住了英格兰优势和克罗地亚回应。

## 判断失效部分

- 英格兰分差和总进球上限被低估。
- 克罗地亚追分后，模型对后段拉开比分的权重不足。

## 模型调整记录

- 前场深度占优的热门队面对有进球质量的对手时，应保留 3-1 或 4-2 高事件替代情景。
- 零封概率和赢球分差概率要分开处理。
- 校准标签：`favorite_margin_understated`, `opponent_scoring_risk_retained`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021509
- https://www.englandfootball.com/england/mens-senior-team/fixtures-results/2025-26/World-Cup/england-v-croatia-fifa-world-cup-wednesday-17-june-2026-match-centre
- https://www.sportingnews.com/us/soccer/news/england-croatia-live-score-result-world-cup/6ef1296f64286e9dcf2d5710
- 核验时间：2026-06-18T17:05:25+08:00

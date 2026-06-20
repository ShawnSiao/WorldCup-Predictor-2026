# 第 032 场复盘：美国 vs 澳大利亚

[复盘索引](README.zh-CN.md) | [English](match-032-usa-aus.md) | [预测](../predictions/match-032-usa-aus.zh-CN.md)

## 赛果

- 最终赛果：第 032 场 美国 2-0 澳大利亚。
- 预测胜者：美国。
- 实际胜者：美国。
- 预测比分：美国 2-1 澳大利亚。
- 复盘评级：正确。

## 判断成立部分

- 美国胜负判断正确。
- 即使普利西奇缺席，主场压迫和进攻深度仍足以决定比赛。
- 澳大利亚下半场反扑存在，但不足以改变结果。

## 判断失效部分

- 澳大利亚进球路径被高估。
- 普利西奇缺席带来的进攻风险被放大。
- 美国领先后防守态势改善，零封路径应提高权重。

## 模型调整记录

- 东道主阵容深度可以比单一球星风险框架更好地吸收缺席。
- 热门队早进球后，如果比赛状态利于收缩，对手进攻风险会下降。
- 校准标签：`clean_sheet_underweighted`, `star_absence_overweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021462
- https://www.ussoccer.com/competitions/fifa-world-cup-26/matches/united-states-australia-tickets-live-score-match-hub-lineups-highlights
- https://www.cbssports.com/soccer/news/usmnt-vs-australia-live-updates-world-cup-2026-score-result/live/
- 核验时间：2026-06-20T14:45:00+08:00

# 第 026 场复盘：瑞士 vs 波黑

[复盘索引](README.zh-CN.md) | [English](match-026-sui-bih.md) | [预测](../predictions/match-026-sui-bih.zh-CN.md)

## 赛果

- 最终赛果：第 026 场 瑞士 4-1 波黑。
- 预测胜者：瑞士。
- 实际胜者：瑞士。
- 预测比分：瑞士 1-0 波黑。
- 复盘评级：部分正确。

## 判断成立部分

- 瑞士胜负判断正确。
- 预测正确识别了瑞士定位球和场面控制路径。
- 波黑进球路径仍然存在，虽然卡片偏向零封。

## 判断失效部分

- 分差被明显低估。
- 预测没有覆盖红牌和替补对后段比赛的放大效应。
- 零封概率偏高。

## 模型调整记录

- 后段比赛状态变化会把可控热门变成大分差。
- 热门分差上限和零封概率不能混在一起。
- 校准标签：`favorite_margin_understated`, `clean_sheet_overstated`, `red_card_swing_underweighted`。

## 来源快照

- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/switzerland-bosnia-herzegovina-match-report-highlights
- https://www.aljazeera.com/sports/2026/6/18/switzerland-beat-bosnia-and-herzegovina-4-1-top-group-b-in-world-cup
- https://www.theguardian.com/football/live/2026/jun/18/switzerland-v-bosnia-and-herzegovina-world-cup-2026-live
- 核验时间：2026-06-20T14:45:00+08:00

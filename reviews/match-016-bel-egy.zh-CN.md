# 第 016 场复盘：比利时 vs 埃及

[首页](../docs/README.zh-CN.md) | [English](match-016-bel-egy.md) | [预测](../predictions/match-016-bel-egy.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 比利时 | 平局 |
| 比分 | 比利时 2-1 埃及 | 比利时 1-1 埃及 |
| 评级 | partial | partial |

## 比赛数据与条件

- 最终赛果：第 016 场比利时 1-1 埃及。
- 预测评级：`partial`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 埃及通过高质量攻击手制造进球威胁的判断成立。
- 比利时替补影响确实重要，扳平球来自替补改变禁区动态。

## 失效的判断

- 比利时取胜倾向给得过强。
- 模型没有充分计入埃及上半场压制和比利时进攻节奏偏慢。
- 高温和补水暂停背景本应进一步提高平局路径。

## 后续可继承因素

- 对老化或换代中的热门方，必须先核验当前进攻节奏，再给胜利倾向。
- 高温和补水暂停会降低节奏，帮助组织性强的下风方。
- 替补影响应成为比分情景变量，而不只是泛化的后段风险。

## 模型调整记录

- 校准标签：`draw_underweighted`、`underdog_resilience_underweighted`、`data_gap_overconfidence`。
- 当热门方名气高但当前进攻磨合不确定时，提高平局概率。

## 来源快照

- FIFA 比赛中心：https://www.fifa.com/en/match-centre/match/17/285023/289273/400021478
- Guardian 文字直播：https://www.theguardian.com/football/live/2026/jun/15/belgium-v-egypt-world-cup-2026-live
- Guardian 赛后报道：https://www.theguardian.com/football/2026/jun/15/belgium-egypt-world-cup-2026-group-g-match-report
- 核验时间：2026-06-16T16:13:02+08:00

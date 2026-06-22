# 第 039 场复盘：比利时 vs 伊朗

[复盘索引](README.zh-CN.md) | [English](match-039-bel-irn.md) | [预测](../predictions/match-039-bel-irn.zh-CN.md)

## 结果

- 最终赛果：第 039 场 比利时 0-0 伊朗。
- 预测胜方：比利时。
- 实际胜方：平局。
- 预测比分：比利时 vs 伊朗 2-1。
- 复盘评级：wrong。

## 成立的判断

- 预测确实把 Doku 缺阵和伊朗低节奏防守列为主要风险。
- 比分情景中保留了平局路径。

## 失效的判断

- 比利时进攻产出被高估，比赛落在 0-0，而不是比利时小胜。
- 模型没有给伊朗完全压低节奏和机会质量足够空间。

## 模型校准记录

- 面对紧凑弱势方时，确认缺少创造点应更明显地下调热门队进球期望。
- 校准标签：`draw_underweighted`、`favorite_attack_overstated`、`clean_sheet_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021477
- https://www.foxsports.com/soccer/fifa-world-cup-men-belgium-vs-iran-jun-21-2026-game-boxscore-647653
- 核验时间：2026-06-22T15:01:00+08:00

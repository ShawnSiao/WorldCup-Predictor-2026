# 第 018 场复盘：伊拉克 vs 挪威

[复盘索引](README.zh-CN.md) | [English](match-018-irq-nor.md) | [赛前预测](../predictions/match-018-irq-nor.zh-CN.md)

## 赛果

- 最终赛果：第 018 场，伊拉克 1-4 挪威。
- 预测胜者：挪威。
- 实际胜者：挪威。
- 预测比分：伊拉克 0-2 挪威。
- 复盘评级：correct。

## 成立的判断

- 挪威的进攻上限优势真实且决定比赛。
- 伊拉克没有形成足够持续的控场能力，未能把比赛拖向 1-1 保守路径。
- 热门方方向判断正确。

## 失效的判断

- 模型低估了挪威的终结上限，并高估了低位防守把比分压窄的能力。
- 零封假设失败：伊拉克仍找到了一条进球路径。

## 后续模型调整

- 面对顶级前锋画像时，即便对手预计低位防守，也要保留更大分差上限。
- 区分「低位减少机会量」和「低位消除连续终结爆发」，后者在本场被估得过强。
- 校准标签：`favorite_margin_understated`，`clean_sheet_overstated`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021491
- https://www.theguardian.com/football/2026/jun/16/norway-iraq-world-cup-2026-group-i-match-report
- https://www.foxsports.com/stories/soccer/world-cup-norway-iraq-france-senegal
- 核验时间：2026-06-17T14:38:30+08:00

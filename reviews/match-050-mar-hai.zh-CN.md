# 第 050 场复盘：摩洛哥 vs 海地

[复盘索引](README.zh-CN.md) | [English](match-050-mar-hai.md) | [预测](../predictions/match-050-mar-hai.zh-CN.md)

## 赛果

- 最终赛果：第 050 场 摩洛哥 4-2 海地。
- 预测胜者：摩洛哥。
- 实际胜者：摩洛哥。
- 预测比分：摩洛哥 vs 海地 3-0。
- 复盘评级：partial。

## 判断成立之处

- 摩洛哥胜者和多球热门路径判断正确。
- 预测捕捉到了摩洛哥控制力和进攻量。

## 判断失效之处

- 零封假设明显失败，海地把两次得分机会转化为进球。
- 模型低估了弱势方转换和定位球得分韧性。

## 模型调整备注

- 保留热门多球胜尾部，但要区分“热门控制比赛”和“热门零封”。
- 校准标签：`clean_sheet_overstated`、`underdog_resilience_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021452
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/matchday-14-round-up-review-highlights
- 核验时间：2026-06-25T13:51:27+08:00

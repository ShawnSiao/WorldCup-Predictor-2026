# 第 053 场复盘：捷克 vs 墨西哥

[复盘索引](README.zh-CN.md) | [English](match-053-cze-mex.md) | [预测](../predictions/match-053-cze-mex.zh-CN.md)

## 赛果

- 最终赛果：第 053 场 捷克 0-3 墨西哥。
- 预测胜者：墨西哥。
- 实际胜者：墨西哥。
- 预测比分：捷克 vs 墨西哥 1-2。
- 复盘评级：partial。

## 判断成立之处

- 墨西哥胜者和主场 / 战术优势判断正确。
- 模型捕捉到捷克追分可能打开转换空间。

## 判断失效之处

- 墨西哥零封与多球分差被低估。
- 捷克定位球得分路线权重过高。

## 模型调整备注

- 主场热门若拥有首球杠杆，0-2 或 0-3 零封分支需要上调。
- 校准标签：`favorite_margin_underweighted`、`clean_sheet_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021444
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/matchday-14-round-up-review-highlights
- 核验时间：2026-06-25T13:51:27+08:00

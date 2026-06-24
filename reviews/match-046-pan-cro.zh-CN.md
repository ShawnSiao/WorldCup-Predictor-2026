# 第 046 场复盘：巴拿马 vs 克罗地亚

[复盘索引](README.zh-CN.md) | [English](match-046-pan-cro.md) | [预测](../predictions/match-046-pan-cro.zh-CN.md)

## 赛果

- 最终赛果：第 046 场 巴拿马 0-1 克罗地亚。
- 预测胜者：克罗地亚。
- 实际胜者：克罗地亚。
- 预测比分：巴拿马 vs 克罗地亚 1-2。
- 复盘评级：correct。

## 判断成立之处

- 克罗地亚中场优势和一球小胜脚本权重正确。
- 巴拿马直接进攻 / 定位球路线被保留为风险，而不是主路径。

## 判断失误之处

- 巴拿马进球路线仍偏高；克罗地亚零封控制权重高于预测。

## 模型调整记录

- 面对克罗地亚这种控节奏球队，保留小胜判断的同时，应给 0-1 和 0-2 更多概率。
- 校准标签：`clean_sheet_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021511
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/panama-croatia-highlights-match-report
- 核验时间：2026-06-24T22:20:00+08:00

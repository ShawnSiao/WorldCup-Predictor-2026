# 第 033 场复盘：德国 vs 科特迪瓦

[复盘索引](README.zh-CN.md) | [English](match-033-ger-civ.md) | [预测](../predictions/match-033-ger-civ.zh-CN.md)

## 赛果

- 最终赛果：德国 2-1 科特迪瓦。
- 预测胜方：德国。
- 实际胜方：德国。
- 预测比分：德国 2-1 科特迪瓦。
- 复盘评级：correct。

## 判断成立部分

- 德国胜负方向和 2-1 比分都命中。
- 预测正确保留了科特迪瓦通过转换和定位球得分的路线。
- 德国后段阵容深度产生决定性作用，Deniz Undav 替补改变比赛。

## 判断偏差

- 赛前文件没有充分强调德国可能需要替补介入，而不是早早掌控比赛。
- 科特迪瓦先取得领先的路径应获得更高情景权重。

## 模型调整记录

- 热门球队阵容深度明显时，替补影响应纳入主情景，而非只作为补救路径。
- 校准标签：`exact_score_hit`、`bench_impact_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021469
- https://www.wral.com/news/ap/ef8fa-undav-scores-twice-saves-germany-with-2-1-world-cup-win-over-ivory-coast/
- https://www.espn.com/soccer/story/_/id/49129600/germany-ivory-coast-2026-fifa-world-cup-deniz-undav
- 核验时间：2026-06-21T16:30:00+08:00

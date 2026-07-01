# 第 077 场复盘：法国 vs 瑞典

[复盘索引](README.zh-CN.md) | [English](match-077-fra-swe.md) | [预测](../predictions/match-077-fra-swe.zh-CN.md)

## 结果

- 最终结果：第 077 场 法国 3-0 瑞典。
- 预测胜者：法国。
- 实际胜者：法国。
- 预测比分：法国 vs 瑞典 2-1。
- 复盘评级：correct。

## 命中的判断

- 法国胜和技术优势判断正确。
- 预测正确把瑞典路线定位为定位球依赖，而不是持续运动战优势。

## 失效的判断

- 2-1 比分低估了法国零封和扩大比分路径。
- 法国控制首个进球阶段后，模型对瑞典进攻威胁权重过高。

## 模型校准备注

- `clean_sheet_underweighted`、`favorite_margin_understated`；当热门能压制弱势方定位球数量时，应提高零封概率。

## 来源快照

- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures
- https://www.fifa.com/en/match-centre/match/17/285023/289287/400021523
- https://www.si.com/soccer/france-player-ratings-vs-sweden-history-maker-kylian-mbappe-world-cup
- https://www.foxsports.com/soccer/fifa-world-cup/scores
- 核验时间：2026-07-01T20:51:00+08:00

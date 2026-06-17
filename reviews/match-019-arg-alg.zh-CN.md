# 第 019 场复盘：阿根廷 vs 阿尔及利亚

[复盘索引](README.zh-CN.md) | [English](match-019-arg-alg.md) | [赛前预测](../predictions/match-019-arg-alg.zh-CN.md)

## 赛果

- 最终赛果：第 019 场，阿根廷 3-0 阿尔及利亚。
- 预测胜者：阿根廷。
- 实际胜者：阿根廷。
- 预测比分：阿根廷 2-0 阿尔及利亚。
- 复盘评级：correct。

## 成立的判断

- 阿根廷的排名和阵容质量优势支撑了基础判断。
- 模型正确把阿尔及利亚转换风险视为真实变量，但没有夸大到足以改变胜负。
- 在这组对位中，热门零封路径成立。

## 失效的判断

- 阿根廷的分差和终结控制力被低估了一球。
- 复盘后对零封的谨慎在总体上合理，但对本场略偏保守。

## 后续模型调整

- 保留下风方转换修正，但当强队能持续控场且对手无法稳定施压时，应保留零封上限。
- 对顶级热门方，不应把所有风险压缩到 2-0，需要让主情景和上限情景有更宽间距。
- 校准标签：`favorite_margin_understated`，`clean_sheet_caution_overweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021497
- https://www.reuters.com/sports/soccer/argentina-beat-algeria-3-0-world-cup-opener-2026-06-17/
- https://www.espn.com/soccer/report/_/gameId/760435
- 核验时间：2026-06-17T14:38:30+08:00

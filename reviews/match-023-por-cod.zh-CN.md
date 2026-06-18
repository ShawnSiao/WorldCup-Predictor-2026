# 第 023 场复盘：葡萄牙 vs 民主刚果

[复盘索引](README.zh-CN.md) | [English](match-023-por-cod.md) | [预测](../predictions/match-023-por-cod.zh-CN.md)

## 赛果

- 最终赛果：第 023 场 葡萄牙 1-1 民主刚果。
- 预测胜者：葡萄牙。
- 实际胜者：平局。
- 预测比分：葡萄牙 3-1 民主刚果。
- 复盘评级：部分正确。

## 判断成立部分

- 保守平局路径明确列出 1-1，最终正是该比分。
- 民主刚果的转换和空中对抗风险被正确识别。
- 葡萄牙仍有足够场面优势，因此赛前倾向热门有依据。

## 判断失效部分

- 平局路径 7% 明显偏低。
- 3-1 主预测高估了葡萄牙转化率和持续压迫能力。
- 公开热门强度压过了临场首发、天气和市场等未闭合变量。

## 模型调整记录

- 强热门若对手有直接进攻出口且临场变量不完整，就要给 1-1 更高权重。
- 赔率、专家、天气和首发信息不完整时，开赛前信心必须下调。
- 校准标签：`draw_underweighted`, `favorite_margin_overstated`, `underdog_resilience_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021501
- https://www.reuters.com/sports/soccer/portugal-held-by-congo-dr-1-1-world-cup-opener-2026-06-17/
- https://www.espn.com/soccer/report/_/gameId/760435
- 核验时间：2026-06-18T17:05:25+08:00

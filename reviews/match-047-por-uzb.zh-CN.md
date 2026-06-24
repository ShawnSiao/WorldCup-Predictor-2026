# 第 047 场复盘：葡萄牙 vs 乌兹别克斯坦

[复盘索引](README.zh-CN.md) | [English](match-047-por-uzb.md) | [预测](../predictions/match-047-por-uzb.zh-CN.md)

## 赛果

- 最终赛果：第 047 场 葡萄牙 5-0 乌兹别克斯坦。
- 预测胜者：葡萄牙。
- 实际胜者：葡萄牙。
- 预测比分：葡萄牙 vs 乌兹别克斯坦 2-0。
- 复盘评级：partial。

## 判断成立之处

- 葡萄牙胜出和零封方向正确。
- 模型把葡萄牙反弹压力作为基础比赛脚本是合理的。

## 判断失误之处

- 热门大比分尾部权重偏低；葡萄牙 3 球及以上路径应更高。
- 高温和首战谨慎被过度套用，首球后双方能力差距进一步放大。

## 模型调整记录

- 顶级热门首战平局后面对排名较低对手，如果下风方迟早要前压，应上调多球胜尾部。
- 校准标签：`favorite_margin_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021503
- https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/portugal-uzbekistan-highlights-match-report
- 核验时间：2026-06-24T22:20:00+08:00

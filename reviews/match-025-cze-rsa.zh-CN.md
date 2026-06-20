# 第 025 场复盘：捷克 vs 南非

[复盘索引](README.zh-CN.md) | [English](match-025-cze-rsa.md) | [预测](../predictions/match-025-cze-rsa.zh-CN.md)

## 赛果

- 最终赛果：第 025 场 捷克 1-1 南非。
- 预测胜者：捷克。
- 实际胜者：平局。
- 预测比分：捷克 2-0 南非。
- 复盘评级：部分正确。

## 判断成立部分

- 已发布比分情景中包含 1-1 平局路径。
- 南非反击和重启球路线作为主要风险被正确标注。
- 比赛分差确实低于简单热门队脚本。

## 判断失效部分

- 主预测胜负方向错过平局。
- 捷克定位球和场面优势没有转化为分差。
- 相对热门倾向，南非韧性仍被低估。

## 模型调整记录

- 热门队进攻效率未闭合时，必须保留 1-1 路径。
- 下风方重启球韧性不应只是象征性尾部风险。
- 校准标签：`draw_underweighted`, `favorite_margin_overstated`, `underdog_resilience_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021440
- https://www.aljazeera.com/sports/liveblog/2026/6/18/czechia-vs-south-africa-live-world-cup-2026
- https://www.espn.com/soccer/report/_/gameId/760438
- 核验时间：2026-06-20T14:45:00+08:00

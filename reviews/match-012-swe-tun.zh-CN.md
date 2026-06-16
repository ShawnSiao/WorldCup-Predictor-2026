# 第 012 场复盘：瑞典 vs 突尼斯

[首页](../docs/README.zh-CN.md) | [English](match-012-swe-tun.md) | [预测](../predictions/match-012-swe-tun.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 瑞典 | 瑞典 |
| 比分 | 瑞典 1-0 突尼斯 | 瑞典 5-1 突尼斯 |
| 评级 | partial | partial |

## 比赛数据与条件

- 最终赛果：第 012 场瑞典 5-1 突尼斯。
- 预测评级：`partial`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 瑞典取胜方向正确。
- 突尼斯防线存在不稳定风险，但预测比分没有体现这种风险可能放大到什么程度。

## 失效的判断

- 模型明显低估了瑞典进攻上限。
- 模型把突尼斯此前防守记录看得过稳，没有充分计入临场战术和教练背景变化。
- 比分情景缺少真正的大胜路径。

## 后续可继承因素

- 近期换帅或阵型大改会削弱旧防守数据的参考价值。
- 如果热门方有多个高质量前锋，而对手体系不稳，即使主判断谨慎，也要保留大比分情景。

## 模型调整记录

- 校准标签：`favorite_margin_understated`、`data_gap_overconfidence`。
- 对新帅、陌生阵型和备战被打乱的球队增加临场战术变化惩罚。

## 来源快照

- FIFA 比赛中心：https://www.fifa.com/en/match-centre/match/17/285023/289273/400021474
- Al Jazeera 赛后报道：https://www.aljazeera.com/sports/2026/6/15/sweden-beat-tunisia-5-1-in-strong-start-to-world-cup
- NY Post 突尼斯换帅报道：https://nypost.com/2026/06/15/sports/tunisia-firing-manager-sabri-lamouchi-after-one-world-cup-game/
- 核验时间：2026-06-16T16:13:02+08:00

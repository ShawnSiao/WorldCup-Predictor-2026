# 第 013 场复盘：沙特阿拉伯 vs 乌拉圭

[首页](../docs/README.zh-CN.md) | [English](match-013-ksa-uru.md) | [预测](../predictions/match-013-ksa-uru.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 乌拉圭 | 平局 |
| 比分 | 沙特阿拉伯 0-2 乌拉圭 | 沙特阿拉伯 1-1 乌拉圭 |
| 评级 | wrong | wrong |

## 比赛数据与条件

- 最终赛果：第 013 场沙特阿拉伯 1-1 乌拉圭。
- 预测评级：`wrong`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 乌拉圭下半场施压和追回比赛的能力存在。
- 沙特的定位球和防守韧性被列为风险，但概率给得不够。

## 失效的判断

- 乌拉圭零封和两球优势都被高估。
- 模型低估了沙特在大赛首战中的韧性和定位球得分路径。
- 乌拉圭临场旅行 / 抵达扰动没有被充分计入。

## 后续可继承因素

- 沙特式紧凑防守和定位球在小组首战中需要提高权重。
- 交通、旅行和迟到等临场扰动会降低热门方锐度。
- 如果热门方进攻稳定性存疑，不应轻易给舒适胜。

## 模型调整记录

- 校准标签：`draw_underweighted`、`clean_sheet_overstated`、`set_piece_risk_underweighted`、`data_gap_overconfidence`。
- 对进攻不够稳定的热门方，即便阵容质量更好，也要提高平局概率。

## 来源快照

- FIFA 比赛中心：https://www.fifa.com/en/match-centre/match/17/285023/289273/400021486
- Guardian 文字直播：https://www.theguardian.com/football/live/2026/jun/15/saudi-arabia-v-uruguay-world-cup-2026-live
- NBC Miami 报道：https://www.nbcmiami.com/world-cup/world-cup-comes-to-miami-saudi-arabia-takes-on-uruguay-today/3820657/
- 核验时间：2026-06-16T16:13:02+08:00

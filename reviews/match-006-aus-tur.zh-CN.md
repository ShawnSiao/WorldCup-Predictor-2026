# 第 006 场复盘：澳大利亚 vs 土耳其

[首页](../docs/README.zh-CN.md) | [English](match-006-aus-tur.md) | [预测](../predictions/match-006-aus-tur.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 土耳其 | 澳大利亚 |
| 比分 | 澳大利亚 1-2 土耳其 | 澳大利亚 2-0 土耳其 |
| 评级 | wrong | wrong |

## 比赛数据与条件

- 最终赛果：第 006 场澳大利亚 2-0 土耳其。
- 预测评级：`wrong`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 预测把土耳其视为更有控球和技术天赋的一方，这个方向有基础，但没有转化成进球。
- 澳大利亚能把比赛压窄这一风险被提到过，但权重明显不够。

## 失效的判断

- 澳大利亚不只是“抗压方”，而是通过反击执行和门将发挥直接赢下比赛。
- 模型过度依赖土耳其控球和欧洲俱乐部人才信号。
- 模型低估了临场选择变化：澳大利亚门将和中场首发调整改变了比赛脚本。

## 后续可继承因素

- 热门方缺少明确机会质量数据时，下风方反击计划必须被视为真实爆冷路径。
- 门将状态和意外首发应进入预测证据检查。
- 面对纪律性强的低位或中位防守，不能默认场面优势会自动转化为进球。

## 模型调整记录

- 校准标签：`transition_risk_underweighted`、`underdog_resilience_underweighted`、`data_gap_overconfidence`。
- 后续预测中，如果热门方主要依赖控球但缺少机会质量证明，需要压低热门胜率。

## 来源快照

- FIFA 赛程/赛果页：https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums
- Al Jazeera 赛后报道：https://www.aljazeera.com/sports/2026/6/14/2026-world-cup-australia-stun-turkiye-2-0-in-counterattacking-masterclass
- 核验时间：2026-06-16T16:13:02+08:00

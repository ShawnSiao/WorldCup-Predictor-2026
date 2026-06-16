# 第 014 场复盘：西班牙 vs 佛得角

[首页](../docs/README.zh-CN.md) | [English](match-014-esp-cpv.md) | [预测](../predictions/match-014-esp-cpv.zh-CN.md)

## 赛果

| 项目 | 预测 | 实际 |
| --- | --- | --- |
| 胜者 | 西班牙 | 平局 |
| 比分 | 西班牙 3-0 佛得角 | 西班牙 0-0 佛得角 |
| 评级 | wrong | wrong |

## 比赛数据与条件

- 最终赛果：第 014 场西班牙 0-0 佛得角。
- 预测评级：`wrong`。
- 复盘依据：已核验赛果、赛前预测文件和赛后来源快照。

## 成立的判断

- 西班牙的场面和射门数量优势真实存在。
- 佛得角顽强防守是低概率风险，但模型给得远远不够。

## 失效的判断

- 模型高估了西班牙终结效率和净胜球空间。
- 模型低估了新军情绪、门将上限、禁区封堵和终结波动。
- 排名差距被当成过强的决定性信号。

## 后续可继承因素

- 强热门面对紧凑新军时，若机会质量未核验，必须保留 0-0 或 1-0 情景。
- 门将爆发和封堵数量要成为显式变量。
- 射门数量不等于进球确定性，还需要机会质量和前场空间证据。

## 模型调整记录

- 校准标签：`draw_underweighted`、`favorite_margin_overstated`、`data_gap_overconfidence`。
- 对顶级强队也要控制零封大胜信心，除非首发、机会质量和对手体能缺口都已核验。

## 来源快照

- FIFA 比赛中心：https://www.fifa.com/en/match-centre/match/17/285023/289273/400021482
- Guardian 赛后报道：https://www.theguardian.com/football/2026/jun/15/spain-cape-verde-world-cup-2026-group-h-match-report
- Al Jazeera 文字直播：https://www.aljazeera.com/sports/liveblog/2026/6/15/spain-vs-cape-verde-live-world-cup-2026
- 核验时间：2026-06-16T16:13:02+08:00

# 第 037 场复盘：乌拉圭 vs 佛得角

[复盘索引](README.zh-CN.md) | [English](match-037-uru-cpv.md) | [预测](../predictions/match-037-uru-cpv.zh-CN.md)

## 结果

- 最终赛果：第 037 场 乌拉圭 2-2 佛得角。
- 预测胜方：乌拉圭。
- 实际胜方：平局。
- 预测比分：乌拉圭 vs 佛得角 1-0。
- 复盘评级：wrong。

## 成立的判断

- 预测正确识别了佛得角低位防守和平局路径是主要风险。
- 比赛确实足够胶着，一次定位球、转换或门将失误就能改变结果。

## 失效的判断

- 乌拉圭控制力被高估，模型没有给佛得角打入两球的路径足够权重。
- 0-0 保守路径抓住了弱势方韧性，但低估了有进球平局。

## 模型校准记录

- 拥有门将状态和定位球路径的低位弱势方，需要更大的有进球平局尾部。
- 校准标签：`draw_underweighted`、`underdog_resilience_underweighted`、`set_piece_risk_underweighted`。

## 来源快照

- https://www.fifa.com/en/match-centre/match/17/285023/289273/400021487
- https://www.foxsports.com/soccer/fifa-world-cup-men-uruguay-vs-cape-verde-jun-21-2026-game-boxscore-647654
- 核验时间：2026-06-22T15:01:00+08:00

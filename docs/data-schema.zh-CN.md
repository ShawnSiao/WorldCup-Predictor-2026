# 数据结构

[English](data-schema.md) | [简体中文](data-schema.zh-CN.md) | [更新日志](../CHANGELOG.md)

## 比赛状态

比赛按以下状态推进：

```text
scheduled -> predicted -> live -> final -> reviewed
```

允许值：

- `scheduled`
- `predicted`
- `live`
- `final`
- `reviewed`

## 文件

| 文件 | 用途 |
| --- | --- |
| `AGENTS.md` | AI 工作索引与仓库维护规则。 |
| `assets/cards/` | 由 `$imagegen` 生成的预测分享位图，用于预测页、日报和邮件发送。 |
| `data/matches.json` | 标准赛程和比赛生命周期状态。 |
| `data/teams.json` | 球队元数据和小组分配。 |
| `data/venues.json` | 场地元数据。 |
| `data/players.json` | 球员级名单数据。 |
| `data/rankings.json` | FIFA 排名快照。 |
| `data/predictions.json` | 预测文件和预测摘要索引；生成的预测应同时维护英文和简体中文文件。 |
| `data/results.json` | 官方最终赛果记录。 |
| `data/review-index.json` | 赛后复盘文件索引。 |

## 验证

运行：

```powershell
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

# Prediction Cards

[English](README.md) | [简体中文](README.zh-CN.md)


This directory stores `$imagegen` generated share images for match predictions and daily reports.

Images in this directory must be real raster files, such as PNG, JPG, JPEG, or WebP. Do not use SVG, HTML, canvas, Mermaid, chart-only, or script-generated image substitutes.

Each prediction has two images:

- `*-lead.png`: first share image. It introduces the fixture only and must not include a scoreline, predicted winner, win/draw/loss wording, probabilities, or result language.
- `*.png`: second share image. It keeps the existing prediction-card convention and may include the predicted result, scoreline, confidence, and key risk framing.

Use this instruction pattern for the first image:

```text
$imagegen: 生成【社交平台赛事预测首图】，16:9 横版，真实位图图片，只展示赛事对阵、比赛阶段、城市/场馆氛围和球队色彩；中文文档配图的主要比赛信息必须使用简体中文，可在画面合适位置保留英文队名/赛事信息作为辅助文字；不输出比分，不输出预测胜负，不输出概率，不使用胜/平/负、晋级、爆冷等结果暗示词；不要生成 SVG，不要生成 HTML，不要生成代码图，不要生成线框图，不要使用官方 FIFA 标志或水印。
```

Use this instruction pattern for the second image:

```text
$imagegen: 生成【社交平台赛事预测配图】，16:9 横版，真实位图图片，用于抖音、小红书、微博和微信分享；中文文档配图的主要比赛信息必须使用简体中文，可在画面合适位置保留英文队名/赛事信息作为辅助文字；不要生成 SVG，不要生成 HTML，不要生成代码图，不要生成线框图，不要使用官方 FIFA 标志或水印。
```

Each prediction record in `data/predictions.json` must include `lead_image_file` and `image_file` paths under this directory. Prediction pages and daily reports should embed both images in that order so GitHub readers and social-platform editors can reuse them directly.

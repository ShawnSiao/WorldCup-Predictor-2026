# Prediction Cards

[English](README.md) | [简体中文](README.zh-CN.md)


This directory stores `$imagegen` generated share images for match predictions and daily reports.

Images in this directory must be real raster files, such as PNG, JPG, JPEG, or WebP. Do not use SVG, HTML, canvas, Mermaid, chart-only, or script-generated image substitutes.

Use this instruction pattern:

```text
$imagegen: 生成【社交平台赛事预测配图】，16:9 横版，真实位图图片，用于抖音、小红书、微博和微信分享；中文文档配图的主要比赛信息必须使用简体中文，可在画面合适位置保留英文队名/赛事信息作为辅助文字；不要生成 SVG，不要生成 HTML，不要生成代码图，不要生成线框图，不要使用官方 FIFA 标志或水印。
```

Each prediction record in `data/predictions.json` must include an `image_file` path under this directory. Prediction pages and daily reports should embed the same image so GitHub readers and social-platform editors can reuse it directly.

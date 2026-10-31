# Volcan

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Moonship-Lab/Volcan?style=social)](https://github.com/Moonship-Lab/Volcan)
[![Docs Check](https://github.com/Moonship-Lab/Volcan/actions/workflows/docs-check.yml/badge.svg?branch=main)](https://github.com/Moonship-Lab/Volcan/actions/workflows/docs-check.yml)
[![Docs](https://img.shields.io/badge/docs-outline-brightgreen?style=flat-square)](docs/zh/outline-timeline.md)

整理制造业简史：让 AI 研究者看见技术的来路，让制造从业者看见经验的价值。
Volcan — a brief history of manufacturing, written for AI researchers and manufacturing practitioners alike.

本站为双语（中文 / English）。文档按语言分目录：`docs/zh/`、`docs/en/`，同一内容两侧保持同一 slug 便于互链。
This repository is bilingual. Content lives under `docs/zh/` and `docs/en/`, and paired pages share the same slug.

## 为什么做这件事 / Why

**给 AI 研究者**：制造业的许多词在论文里只是一个 token——OEE、Cpk、节拍、柔性制造、换型时间。一旦脱离它们诞生的现场，数据假设和目标函数就容易被建错。Volcan 把这些概念放回原地：它当初为了解决什么问题、付出过什么代价、哪些约束到今天仍然存在。

**给制造从业者**：产线上的判断很大一部分长在人身上，难以写进公式，也难以被检索。Volcan 提供一个可被机器读取、可被复用的位置，把 tacit knowledge 变成 explicit knowledge——让经验不随人退休而消失。

一句话：**让技术落地，让经验发光。**

## 内容地图 / Where things live

| 内容 | 中文 | English |
| --- | --- | --- |
| 通史时间线大纲 | [`docs/zh/outline-timeline.md`](docs/zh/outline-timeline.md) | [`docs/en/outline-timeline.md`](docs/en/outline-timeline.md) |
| 词条正文 `entries/` | 尚未开始 | not started |
| 术语对照表 `glossary/` | 尚未开始 | not started |
| 案例与从业者口述 `cases/` | 尚未开始 | not started |
| AI × 制造专题 `ai/` | 尚未开始 | not started |

> 大纲里每个词条都标了状态：**待认领 → 撰写中 → 待校对 → 待翻译 → 完成**。认领前先看 `outline-timeline.md`，写前先看 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

## 第一批写什么 / What comes first

通史时间线：从手工工场到智能制造，共十一章。每章由若干独立词条构成，词条是本项目的最小写作单元——因为它们既适合人读，也适合被检索、被嵌入、被喂给模型。

先接通史，是因为词条需要一个坐标系。散落的名词没有重力，挂在时间线上，它们之间才有因果。

## 路线图 / Roadmap

- [x] 大纲与贡献规范
- [ ] 时间线第一批词条（每章 1–2 篇）
- [ ] 中英术语对照表（统一译名，避免同一个概念三种写法）
- [ ] 案例与从业者口述
- [ ] AI × 制造专题
- [ ] 静态站点与全文检索

## 参与 / Contributing

欢迎 AI 研究者、制造工程师、工艺/质量/供应链从业者、以及译者。

参与方式见 [`CONTRIBUTING.md`](CONTRIBUTING.md)：认领词条、补一条时间线、提交勘误或补充译名，都从那里开始。

在 Issue 里认领，比闷头写完再提 PR 更省时间。

## 许可证 / License

[Apache License 2.0](LICENSE)。提交到此仓库的贡献默认以同一许可证授权。

# 贡献指南 · Contributing to Volcan

本项目用中英双语写作。每种语言自成一篇文档，`docs/zh/` 与 `docs/en/` 使用同一 slug 互相对应。
Volcan is written bilingually. Each entry exists once per language under `docs/zh/` and `docs/en/`, sharing the same slug.

> 目录：[中文规范](#中文规范) · [English guidelines](#english-guidelines)

---

# 中文规范

## 一、两条底线

1. **事实与解读分开。** 「1913 年福特在 Highland Park 引入移动装配线」是事实；「这是现代制造的起点」是解读。解读可以大胆，但必须让读者看得出这是解读。
2. **不确定的内容要标注。** 查不到可靠出处的数据、年份、传说（例如某些广泛流传的行业神话），宁可写成「此说流传甚广，但缺少一手证据」，也不要写成断言。**查证不清的段落请勿写入正文**，可在 PR 描述里说明并请求协助核实。

## 二、可以怎么贡献

| 类型 | 说明 | 起点 |
| --- | --- | --- |
| 写词条 | 最小写作单元，4 000 字以内即可 | 在 `docs/zh/outline-timeline.md` 认领 |
| 补时间线 | 为大纲补一个缺失节点或勘误现有年份 | 直接提 Issue |
| 译名与术语 | 统一中英对照，避免同一概念多种写法 | 提 Issue，标注现有分歧 |
| 案例与口述 | 一线经验、失败复盘 | 提 Issue 说明边界（可否公开、是否脱敏） |
| 审稿 | 事实核查、可读性 | 在 PR 里 review |

## 三、写作规范

### 文件与命名

```
docs/zh/entries/03-interchangeable-parts.md
docs/en/entries/03-interchangeable-parts.md   ← 同一 slug
```

文件名用小写字母与短横线，全部为 ASCII（中文标题放在 frontmatter 里，不放文件名）。

### Frontmatter

```yaml
---
title: 互换零件
title_en: Interchangeable Parts
slug: 03-interchangeable-parts
era: 1850-1900
tags: [公差, 装配, 军械工坊]
status: reviewing        # draft | reviewing | needs-translation | done
author: your-github-id
date: 2026-03-15
related: [03-gauges-and-limits, 02-machine-tools]
---
```

### 正文结构（六段，固定）

```markdown
## 一句话定义
一段话说清「它是什么」，并给出英文对照（如：节拍时间（Takt Time））。

## 它出现之前
那个年代的真实约束是什么——贵在哪、慢在哪、为什么没人解决。

## 关键转折
发生了什么，谁做的，在什么约束下做的。

## 今天留下了什么
今天哪些做法、指标、名词是从这里继承而来的。

## 常见误解
至少一条。制造业史料里传说极多，这一节是本项目的核心价值之一。

## 参考
按人文写作惯例列出书名/文章/档案，附出版信息与页码（如可获取）。
```

顺序固定不变；没有内容的段落写「待补充」，不要删掉标题。

### 术语写法

- 首次出现给原文对照：`数字孪生（Digital Twin）`、`自働化（Jidoka）`。
- 「自働化」保留人字旁，它是有意的用字差异，请改正笔误，勿"纠错"。
- 缩写首次出现时展开一次：`制造执行系统（MES, Manufacturing Execution System）`。
- 译名以 `docs/zh/glossary/` 为准（术语表尚在建设；遇分歧请提 Issue，勿自行造词）。

### 引用

- 每个关键论断尽力给出出处，尤其是数字、年份、人名。
- 数字要带单位与口径：`约 12.5 小时/台（1914 年，高地公园，含辅助工序）`。
- 二手来源（尤其是综述性文章）请标注为二手；能找到一手档案时优先一手。

## 四、关于 AI 辅助写作

允许使用 AI 辅助润色、翻译与整理。**但：**

- AI 生成的内容**不得充当事实来源**——所有事实必须回到可查证的出处。
- 作者最终对全文负责，包括 AI 参与的部分。
- 在 PR 描述中说明是否使用了 AI 辅助，以及用在哪一部分。

## 五、PR 流程

1. 在 Issue 认领（避免重复劳动），并在 `docs/zh/outline-timeline.md` 把状态改为「撰写中 @你的ID」。
2. 分支名建议：`entry/03-interchangeable-parts`。
3. PR 标题加前缀：`[zh]`、`[en]`、`[zh+en]`、`[needs-translation]`。
4. 自查清单（请在 PR 描述里勾选）：
   - [ ] 关键事实有出处，不确定之处已显式标注
   - [ ] 六段结构完整，空段落标了「待补充」
   - [ ] 术语首次出现给了原文对照
   - [ ] 六段结构、slug 与另一语种版本一致（或已标记 `needs-translation`）
   - [ ] 无营销倾向、无未脱敏的客户信息

## 六、双语同步

- 任一语种都可以先提交，不必等待另一语种。**结论与数据必须一致**，文字不必逐句镜像。
- 单语提交时 frontmatter 写 `status: needs-translation`，PR 标题加 `[needs-translation]`。
- 已双语的条目，一侧修改时请在 PR 里提醒同步另一侧。

## 七、许可证

本项目采用 Apache License 2.0。提交贡献即表示你同意该贡献按同一许可证授权，并确认你有权提交此内容。

---

# English Guidelines

## 1. Two hard rules

1. **Separate fact from interpretation.** "Ford introduced the moving assembly line at Highland Park in 1913" is a fact. "This is where modern manufacturing begins" is an interpretation. Interpretations may be bold, but they must be recognisable as interpretations.
2. **Mark what you cannot verify.** For uncertain dates, numbers, or widely repeated industry legends, write "this account is widely repeated but lacks primary evidence" rather than stating it flatly. **Do not put unverifiable passages in the body** — flag them in the PR description and ask for help checking.

## 2. Ways to contribute

| Type | Description | Start here |
| --- | --- | --- |
| Entry | The smallest unit of writing; under ~2,500 words is fine | Claim in `docs/en/outline-timeline.md` |
| Timeline fix | A missing node or a wrong year | Open an Issue |
| Glossary | Unify zh↔en term pairs, resolve naming conflicts | Open an Issue describing the split |
| Cases / oral history | Shopfloor experience, failure post-mortems | Open an Issue, state what can be published and what must be anonymised |
| Review | Fact-checking and readability | Review open PRs |

## 3. Writing rules

### Files and naming

```
docs/en/entries/03-interchangeable-parts.md
docs/zh/entries/03-interchangeable-parts.md   ← same slug
```

Filenames are lowercase, ASCII-only, dash-separated. Non-English titles live in the frontmatter, not the filename.

### Frontmatter

```yaml
---
title: Interchangeable Parts
title_zh: 互换零件
slug: 03-interchangeable-parts
era: 1850-1900
tags: [tolerance, assembly, armory]
status: reviewing        # draft | reviewing | needs-translation | done
author: your-github-id
date: 2026-03-15
related: [03-gauges-and-limits, 02-machine-tools]
---
```

### Body structure (six fixed sections)

```markdown
## One-line definition
What it is, plus the original-language term (e.g. takt time（タクトタイム）).

## What came before
The real constraints of the era — what was expensive, slow, and why nobody had fixed it.

## The turning point
What happened, who did it, under which constraints.

## What survives today
Which practices, metrics and terms descend from it.

## Common misconceptions
At least one. Manufacturing history is full of legends; debunking them is core value here.

## References
Books, articles, archives with publication details and page numbers where available.
```

Keep the order fixed. Write "To be added" under empty sections; do not delete headings.

### Terminology

- Give the original term on first use: `digital twin（Digital Twin）`, `jidoka（自働化）`.
- Keep the human radical in `自働化` when quoting the Japanese — it is deliberate, not a typo.
- Spell acronyms out once on first use: `Manufacturing Execution System (MES)`.
- Translations follow `docs/en/glossary/` (still being built). When terms conflict, open an Issue rather than inventing new ones.

### Citations

- Attach a source to every key claim, especially numbers, years and names.
- Numbers carry units and scope: "≈12.5 hours per car (Highland Park, 1914, including auxiliary operations)".
- Label secondary sources as secondary; prefer primary archives when reachable.

## 4. On using AI while writing

AI assistance for polishing, translation and structuring is allowed. **However:**

- AI-generated content **must not serve as the source of facts** — every claim traces back to a checkable source.
- The author is responsible for the whole entry, including AI-assisted parts.
- State in the PR description whether AI was used, and where.

## 5. PR process

1. Claim the entry in an Issue, then flip its status in `docs/en/outline-timeline.md` to "Drafting @yourid".
2. Suggested branch name: `entry/03-interchangeable-parts`.
3. Prefix PR titles: `[zh]`, `[en]`, `[zh+en]`, `[needs-translation]`.
4. Self-check before requesting review (tick them in the PR body):
   - [ ] Key facts cited; uncertain points explicitly flagged
   - [ ] All six sections present, empty ones marked "To be added"
   - [ ] Original-language term given on first use
   - [ ] Slug and section structure match the other language version (or marked `needs-translation`)
   - [ ] No promotional content, no un-anonymised client information

## 6. Keeping both languages in sync

- Either language may land first; neither waits for the other. **Conclusions and data must match**; wording need not mirror sentence by sentence.
- Single-language submissions use `status: needs-translation` and a `[needs-translation]` PR title.
- When editing an existing bilingual entry, note in the PR that the other language needs to follow.

## 7. License

This project is licensed under Apache License 2.0. By contributing, you agree that your contribution is licensed under the same terms and that you have the right to submit it.

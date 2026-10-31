#!/usr/bin/env python3
"""Volcan documentation sanity checks.

Three independent checks, all using the standard library only:

1. slug alignment  - docs/zh/outline-timeline.md and docs/en/outline-timeline.md must list the same slugs
2. entry structure - files under docs/{lang}/entries/ must carry valid frontmatter and the six fixed sections
3. internal links  - relative Markdown links must point at files that exist

Exit status is 0 when no error is found. Warnings never fail the build by default;
pass --strict to promote them to errors (useful once the outline is fully bilingual).

Reference-style links ([text][ref]) are not parsed - use inline links in this repo.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

OUTLINE = {
    "zh": ROOT / "docs" / "zh" / "outline-timeline.md",
    "en": ROOT / "docs" / "en" / "outline-timeline.md",
}

SECTIONS = {
    "zh": [
        "一句话定义",
        "它出现之前",
        "关键转折",
        "今天留下了什么",
        "常见误解",
        "参考",
    ],
    "en": [
        "One-line definition",
        "What came before",
        "The turning point",
        "What survives today",
        "Common misconceptions",
        "References",
    ],
}

REQUIRED_FRONTMATTER = ["title", "slug", "status"]

OUTLINE_ITEM = re.compile(r"^-\s*\[[ xX]\]\s*`([A-Za-z0-9][A-Za-z0-9-]*)`", re.MULTILINE)
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(([^()\s]+)(?:\s+\"[^\"]*\")?\)")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.MULTILINE)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)
        print(f"[ERROR] {message}")

    def warn(self, message: str) -> None:
        self.warnings.append(message)
        print(f"[WARN ] {message}")

    def ok(self, message: str) -> None:
        print(f"[OK   ] {message}")


def parse_slugs(path: Path) -> list[str]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8-sig")
    return OUTLINE_ITEM.findall(text)


def check_slug_alignment(report: Report) -> None:
    print("\n== 1. outline slug alignment ==")
    missing_side = False
    for lang, path in OUTLINE.items():
        if not path.is_file():
            report.error(f"missing outline file: {path.relative_to(ROOT)}")
            missing_side = True
    if missing_side:
        return

    zh_slugs = parse_slugs(OUTLINE["zh"])
    en_slugs = parse_slugs(OUTLINE["en"])
    report.ok(f"zh outline: {len(zh_slugs)} entries | en outline: {len(en_slugs)} entries")

    for slug in zh_slugs:
        if slug not in en_slugs:
            report.warn(f"`{slug}` has no counterpart in docs/en/outline-timeline.md")
    for slug in en_slugs:
        if slug not in zh_slugs:
            report.warn(f"`{slug}` has no counterpart in docs/zh/outline-timeline.md")

    if zh_slugs == en_slugs:
        report.ok("both outlines are aligned")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_entries(report: Report) -> None:
    print("\n== 2. entry file structure ==")
    found = False
    for lang, sections in SECTIONS.items():
        entries_dir = ROOT / "docs" / lang / "entries"
        if not entries_dir.is_dir():
            continue
        for path in sorted(entries_dir.glob("*.md")):
            found = True
            rel = path.relative_to(ROOT)
            text = path.read_text(encoding="utf-8-sig")
            fields = parse_frontmatter(text)
            if not fields:
                report.error(f"{rel}: no YAML frontmatter block found")
            else:
                for key in REQUIRED_FRONTMATTER:
                    if not fields.get(key):
                        report.error(f"{rel}: frontmatter field `{key}` is missing or empty")
            headings = [h.strip() for h in HEADING.findall(text)]
            for section in sections:
                if section not in headings:
                    report.error(f"{rel}: missing required section heading `## {section}`")
    if not found:
        report.ok("no entry files yet - nothing to validate")


def check_links(report: Report) -> None:
    print("\n== 3. internal markdown links ==")
    checked = 0
    broken = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for target in INLINE_LINK.findall(text):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "<")):
                continue
            target_path, _, _fragment = target.partition("#")
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            checked += 1
            if not resolved.exists():
                broken += 1
                report.error(
                    f"{path.relative_to(ROOT)}: broken link -> {target}"
                )
    report.ok(f"{checked} internal links checked, {broken} broken")


def write_step_summary(report: Report) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = [
        "## Volcan docs check",
        "",
        f"- errors: **{len(report.errors)}**",
        f"- warnings: **{len(report.warnings)}**",
        "",
    ]
    if report.errors:
        lines += ["### Errors", ""] + [f"- {m}" for m in report.errors] + [""]
    if report.warnings:
        lines += ["### Warnings", ""] + [f"- {m}" for m in report.warnings] + [""]
    Path(summary_path).write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    if os.environ.get("VOLCAN_STRICT", "").strip() in {"1", "true", "yes"}:
        strict = True

    report = Report()
    print(f"Volcan docs check (root: {ROOT}, strict: {strict})")

    check_slug_alignment(report)
    check_entries(report)
    check_links(report)

    failures = len(report.errors) + (len(report.warnings) if strict else 0)
    print(
        f"\nresult: {len(report.errors)} error(s), {len(report.warnings)} warning(s)"
        + (" (strict mode: warnings count as failures)" if strict else "")
    )
    write_step_summary(report)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Audit the repository for ManimCE debt and ManimGX migration hazards."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re


SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "media", "__pycache__"}


@dataclass(frozen=True)
class Rule:
    code: str
    pattern: re.Pattern[str]
    severity: str
    message: str


RULES = (
    Rule(
        "CE_IMPORT",
        re.compile(r"^\s*from\s+manim(?:\.|\s+)|^\s*import\s+manim(?:\s|$)", re.M),
        "error",
        "ManimCE import remains; ManimGX does not reproduce CE module paths",
    ),
    Rule(
        "FRAME_WIDTH_SET",
        re.compile(r"\b(?:(?:[A-Za-z_]\w*)\.)?config(?:\[[\"']frame_width[\"']\]|\.frame_width)\s*="),
        "error",
        "ManimGX frame_width is derived/read-only",
    ),
    Rule(
        "TEX_TEMPLATE",
        re.compile(r"\b(?:TexTemplate|TexTemplateLibrary|tex_template)\b"),
        "warn",
        "CE TeX template usage requires a ManimGX mitex/Typst redesign",
    ),
    Rule(
        "LATEX_PACKAGE",
        re.compile(r"\\(?:usepackage|newcommand|def)\b"),
        "warn",
        "Custom LaTeX package/macros require mitex/Typst review",
    ),
    Rule(
        "DEPRECATED_GX_ALIAS",
        re.compile(r"\b(?:MovingCameraScene|ApplyMethod|ScaleInPlace|FadeToColor|arrange_submobjects|rotate_about_origin|get_edge_center|PGroup|add_foreground_mobject)\b"),
        "warn",
        "ManimGX compatibility/deprecated alias remains; use the preferred native API",
    ),
    Rule(
        "RENDERER_SPECIFIC",
        re.compile(r"\b(?:CairoRenderer|OpenGLRenderer|OpenGLMobject|renderer=|(?:[A-Za-z_]\w*\.)?config\.renderer)\b"),
        "warn",
        "Renderer-specific ManimCE API needs redesign for the wgpu runtime",
    ),
    Rule(
        "CE_CLI",
        re.compile(r"(?<![\w-])(?:python\s+-m\s+)?manim\s+(?:-[A-Za-z]|render\b|preview\b)"),
        "warn",
        "ManimCE CLI reference remains; migrate to manimgx inspect/preview/render",
    ),
    Rule(
        "CE_MEDIA_INTERNAL",
        re.compile(r"\b(?:partial_movie_files|media_dir|write_to_movie|disable_caching|tempconfig)\b"),
        "warn",
        "ManimCE media/config internal remains",
    ),
)


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in {".py", ".md", ".sh", ".yml", ".yaml", ".toml"}:
            yield path


def audit(root: Path) -> list[tuple[Path, Rule, int, str]]:
    findings: list[tuple[Path, Rule, int, str]] = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lines = text.splitlines()
        for rule in RULES:
            for match in rule.pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                excerpt = lines[line_no - 1].strip() if lines else ""
                # Historical/reference Markdown is migration evidence, not executable code.
                effective = rule
                if path.suffix.lower() == ".md" and rule.severity == "error":
                    effective = Rule(rule.code, rule.pattern, "warn", rule.message)
                findings.append((path, effective, line_no, excerpt))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    args = parser.parse_args()

    findings = audit(args.root)
    for path, rule, line_no, excerpt in findings:
        print(f"{rule.severity.upper():5} {rule.code:20} {path}:{line_no}: {excerpt}")

    errors = sum(rule.severity == "error" for _, rule, _, _ in findings)
    warnings = len(findings) - errors
    print(f"\nManimGX audit: {errors} error(s), {warnings} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())

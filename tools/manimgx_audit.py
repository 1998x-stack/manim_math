#!/usr/bin/env python3
"""Audit the repository for ManimCE debt and ManimGX migration hazards.

The audit deliberately distinguishes executable blockers from migration debt:
- blockers are patterns that are invalid or semantically unsafe under ManimGX;
- warnings are compatibility aliases or portability debt that still need cleanup.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "media", "__pycache__"}
TEXT_SUFFIXES = {".py", ".md", ".sh", ".yml", ".yaml", ".toml"}


@dataclass(frozen=True)
class Finding:
    path: Path
    severity: str
    code: str
    line_no: int
    excerpt: str
    message: str


@dataclass(frozen=True)
class TextRule:
    code: str
    pattern: re.Pattern[str]
    severity: str
    message: str
    python_blocker: bool = False


TEXT_RULES = (
    TextRule(
        "CE_IMPORT",
        re.compile(r"^\s*from\s+manim(?:\.|\s+)|^\s*import\s+manim(?:\s|$)", re.M),
        "error",
        "ManimCE import remains; ManimGX does not reproduce CE module paths",
        python_blocker=True,
    ),
    TextRule(
        "TEX_TEMPLATE",
        re.compile(r"\b(?:TexTemplate|TexTemplateLibrary|tex_template)\b"),
        "warn",
        "CE TeX template usage requires a ManimGX mitex/Typst redesign",
        python_blocker=True,
    ),
    TextRule(
        "LATEX_PACKAGE",
        re.compile(r"\\(?:usepackage|newcommand|def)\b"),
        "warn",
        "Custom LaTeX package/macros are not translated by ManimGX mitex",
        python_blocker=True,
    ),
    TextRule(
        "DEPRECATED_GX_ALIAS",
        re.compile(
            r"\b(?:MovingCameraScene|ApplyMethod|ScaleInPlace|FadeToColor|"
            r"arrange_submobjects|rotate_about_origin|get_edge_center|PGroup|"
            r"add_foreground_mobject)\b"
        ),
        "warn",
        "ManimGX deprecated compatibility alias remains; use the preferred native API",
    ),
    TextRule(
        "RENDERER_SPECIFIC",
        re.compile(
            r"\b(?:CairoRenderer|OpenGLRenderer|OpenGLMobject|renderer=|"
            r"(?:[A-Za-z_]\w*\.)?config\.renderer)\b"
        ),
        "warn",
        "Renderer-specific ManimCE API needs redesign for the wgpu runtime",
        python_blocker=True,
    ),
    TextRule(
        "CE_CLI",
        re.compile(r"(?<![\w-])(?:python\s+-m\s+)?manim\s+(?:-[A-Za-z]|render\b|preview\b)"),
        "warn",
        "ManimCE CLI reference remains; migrate to manimgx inspect/preview/render",
    ),
    TextRule(
        "CE_MEDIA_INTERNAL",
        re.compile(r"\b(?:partial_movie_files|media_dir|write_to_movie|disable_caching|tempconfig)\b"),
        "warn",
        "ManimCE media/config internal remains",
        python_blocker=True,
    ),
    TextRule(
        "SYSTEM_FONT",
        re.compile(
            r'''(?ix)
            ["']
            (?:PingFang\ SC|Microsoft\ YaHei|SimHei|SimSun|Heiti\ SC|Songti\ SC)
            ["']
            '''
        ),
        "warn",
        "System-specific CJK font remains; prefer repository CJK_FONT or a bundled/generic font",
    ),
)

DYNAMIC_SEMANTIC_NAMES = {
    "ValueTracker",
    "always_redraw",
    "Succession",
    "AnimationGroup",
    "LaggedStart",
}


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def line_excerpt(text: str, line_no: int) -> str:
    lines = text.splitlines()
    if not lines or not (1 <= line_no <= len(lines)):
        return ""
    return lines[line_no - 1].strip()


def add_finding(
    findings: list[Finding],
    *,
    path: Path,
    severity: str,
    code: str,
    line_no: int,
    text: str,
    message: str,
) -> None:
    findings.append(
        Finding(
            path=path,
            severity=severity,
            code=code,
            line_no=line_no,
            excerpt=line_excerpt(text, line_no),
            message=message,
        )
    )


def config_attr(node: ast.AST) -> str | None:
    """Return config attribute for `config.x` or `<alias>.config.x`."""
    if not isinstance(node, ast.Attribute):
        return None
    owner = node.value
    if isinstance(owner, ast.Name) and owner.id == "config":
        return node.attr
    if (
        isinstance(owner, ast.Attribute)
        and owner.attr == "config"
        and isinstance(owner.value, ast.Name)
    ):
        return node.attr
    return None


def iter_assignment_targets(node: ast.AST) -> Iterable[ast.AST]:
    """Flatten tuple/list assignment targets so tuple config writes are not missed."""
    if isinstance(node, (ast.Tuple, ast.List)):
        for element in node.elts:
            yield from iter_assignment_targets(element)
        return
    yield node


def called_name(node: ast.Call) -> str | None:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def audit_python(path: Path, text: str, findings: list[Finding]) -> None:
    try:
        tree = ast.parse(text)
    except SyntaxError as exc:
        add_finding(
            findings,
            path=path,
            severity="error",
            code="PYTHON_SYNTAX",
            line_no=exc.lineno or 1,
            text=text,
            message=exc.msg,
        )
        return

    is_runtime_module = path.as_posix().endswith("manim_math_gx/runtime.py")
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets.append(node.target)
        elif isinstance(node, ast.AugAssign):
            targets.append(node.target)

        for target in targets:
            for leaf in iter_assignment_targets(target):
                attribute = config_attr(leaf)
                if attribute == "frame_width":
                    add_finding(
                        findings,
                        path=path,
                        severity="error",
                        code="READONLY_FRAME_WIDTH",
                        line_no=getattr(leaf, "lineno", 1),
                        text=text,
                        message=(
                            "ManimGX config.frame_width is derived/read-only; "
                            "set pixel_width/pixel_height/frame_height instead"
                        ),
                    )
                elif (
                    attribute
                    in {
                        "pixel_width",
                        "pixel_height",
                        "frame_height",
                        "frame_rate",
                        "background_color",
                    }
                    and not is_runtime_module
                ):
                    add_finding(
                        findings,
                        path=path,
                        severity="warn",
                        code="INLINE_RENDER_CONFIG",
                        line_no=getattr(leaf, "lineno", 1),
                        text=text,
                        message=(
                            "Scene-local render config remains; prefer "
                            "manim_math_gx.configure_render for repository-wide consistency"
                        ),
                    )

        if isinstance(node, ast.Call):
            name = called_name(node)
            if name in DYNAMIC_SEMANTIC_NAMES:
                add_finding(
                    findings,
                    path=path,
                    severity="warn",
                    code="TIMELINE_SEMANTICS_REVIEW",
                    line_no=getattr(node, "lineno", 1),
                    text=text,
                    message=(
                        f"{name} requires explicit ManimGX timeline review "
                        "(exact dt, start state, composition, and checkpoints)"
                    ),
                )
            if name == "add_updater":
                add_finding(
                    findings,
                    path=path,
                    severity="warn",
                    code="UPDATER_SEMANTICS_REVIEW",
                    line_no=getattr(node, "lineno", 1),
                    text=text,
                    message=(
                        "Updater must be checked against ManimGX exact-time dt semantics "
                        "and while its mobject is animated"
                    ),
                )


def audit(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for rule in TEXT_RULES:
            for match in rule.pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                severity = rule.severity
                if path.suffix.lower() == ".py" and rule.python_blocker:
                    severity = "error"
                elif path.suffix.lower() == ".md" and severity == "error":
                    severity = "warn"
                add_finding(
                    findings,
                    path=path,
                    severity=severity,
                    code=rule.code,
                    line_no=line_no,
                    text=text,
                    message=rule.message,
                )

        if path.suffix.lower() == ".py":
            audit_python(path, text, findings)

    unique: dict[tuple[str, str, int, str], Finding] = {}
    for finding in findings:
        key = (
            finding.path.as_posix(),
            finding.code,
            finding.line_no,
            finding.severity,
        )
        unique[key] = finding
    return sorted(
        unique.values(),
        key=lambda f: (f.path.as_posix(), f.line_no, f.code, f.severity),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on warnings as well as errors",
    )
    args = parser.parse_args()

    findings = audit(args.root)
    for finding in findings:
        print(
            f"{finding.severity.upper():5} {finding.code:24} "
            f"{finding.path}:{finding.line_no}: {finding.excerpt}"
        )

    errors = sum(f.severity == "error" for f in findings)
    warnings = len(findings) - errors
    by_code: dict[str, int] = {}
    for finding in findings:
        by_code[finding.code] = by_code.get(finding.code, 0) + 1

    print(f"\nManimGX audit: {errors} error(s), {warnings} warning(s)")
    if by_code:
        print("Debt by code:")
        for code, count in sorted(by_code.items(), key=lambda item: (-item[1], item[0])):
            print(f"  {code:24} {count}")

    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())

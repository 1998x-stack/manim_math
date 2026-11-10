#!/usr/bin/env python3
"""Read-only inventory of primary-school Python sources (stdlib only).

Includes standalone lessons, alternate Scene entries, compatibility wrappers,
math helpers, verifier scripts and tests. This is NOT a render or math proof.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import sys

GRADE_NAMES = ("一年级", "二年级", "三年级", "四年级", "五年级", "六年级")
SCENE_BASES = {
    "Scene", "MovingCameraScene", "ThreeDScene", "ZoomedScene",
    "LinearTransformationScene", "VectorScene", "GraphScene",
}


def scene_names(tree: ast.Module) -> list[str]:
    """Find direct Manim Scene subclasses; avoid guessing indirect inheritance."""
    named_bases = set(SCENE_BASES)
    manim_modules = {"manim"}
    for node in tree.body:
        if isinstance(node, ast.Import):
            for name in node.names:
                if name.name == "manim":
                    manim_modules.add(name.asname or name.name)
        elif isinstance(node, ast.ImportFrom) and node.module == "manim":
            for name in node.names:
                if name.name in SCENE_BASES:
                    named_bases.add(name.asname or name.name)

    result = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if any(
            (isinstance(base, ast.Name) and base.id in named_bases)
            or (
                isinstance(base, ast.Attribute)
                and isinstance(base.value, ast.Name)
                and base.value.id in manim_modules
                and base.attr in SCENE_BASES
            )
            for base in node.bases
        ):
            result.append(node.name)
    return result


def inspect_source(path: Path, root: Path) -> dict:
    relative = path.relative_to(root).as_posix()
    parts = path.relative_to(root).parts
    filename = path.name
    role = "unresolved"
    if filename.startswith("test_"):
        role = "test"
    elif filename.startswith("verify_"):
        role = "verifier"

    record = {
        "path": relative,
        "grade": parts[1],
        "term": parts[2] if parts[1] in GRADE_NAMES and len(parts) > 2 else None,
        "topic_directory": path.parent.relative_to(root).as_posix(),
        "bytes": path.stat().st_size,
        "role": role,
        "scenes": [],
        "error": None,
    }
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=relative)
    except (OSError, UnicodeError, SyntaxError) as exc:
        record["error"] = f"{type(exc).__name__}: {exc}"
        return record

    record["scenes"] = scene_names(tree)
    if record["role"] not in {"test", "verifier"}:
        if record["scenes"]:
            record["role"] = "direct-scene"
        elif any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "run_path"
            for node in ast.walk(tree)
        ):
            record["role"] = "compatibility-wrapper"
        else:
            record["role"] = "helper-or-indirect-scene"
    return record


def audit(root: Path) -> dict:
    """Return deterministic source and topic inventories without importing scenes."""
    root = root.resolve()
    course = root / "小学"
    if not course.is_dir():
        raise FileNotFoundError(f"Missing primary-school directory: {course}")

    files = [inspect_source(path, root) for path in sorted(course.rglob("*.py"))]
    groups: dict[str, list[dict]] = {}
    for item in files:
        groups.setdefault(item["topic_directory"], []).append(item)

    topics = []
    for directory, members in sorted(groups.items()):
        folder = root / directory
        grade = members[0]["grade"]
        has_companions = grade in GRADE_NAMES
        companions = {
            name: (folder / name).is_file()
            for name in ("description.json", "prompt.md", "storyboard.md")
        } if has_companions else None
        topics.append({
            "path": directory,
            "python_files": [item["path"] for item in members],
            "direct_scenes": [
                {"file": item["path"], "classes": item["scenes"]}
                for item in members if item["scenes"]
            ],
            "companions": companions,
            "needs_scene_review": has_companions and not any(item["scenes"] for item in members),
        })

    return {
        "schema_version": 1,
        "scope": "小学",
        "summary": {
            "python_files": len(files),
            "source_directories": len(topics),
            "by_grade": dict(sorted(Counter(item["grade"] for item in files).items())),
            "by_role": dict(sorted(Counter(item["role"] for item in files).items())),
            "parse_errors": sum(item["error"] is not None for item in files),
            "multiple_python_directories": sum(len(topic["python_files"]) > 1 for topic in topics),
            "missing_storyboards": sum(
                topic["companions"] is not None and not topic["companions"]["storyboard.md"]
                for topic in topics
            ),
        },
        "topics": topics,
        "files": files,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Write JSON only to this explicit path")
    parser.add_argument("--fail-on", choices=("syntax", "none"), default="syntax")
    args = parser.parse_args(argv)
    try:
        result = audit(args.root)
        data = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.output is None:
            sys.stdout.write(data)
        else:
            args.output.write_text(data, encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot audit primary-school sources: {exc}\n")
    return int(args.fail_on == "syntax" and result["summary"]["parse_errors"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())

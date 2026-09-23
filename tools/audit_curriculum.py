#!/usr/bin/env python3
"""Read-only curriculum inventory. No Manim import, render, media read or mutation."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

LEVELS = ("小学", "初中", "高中")
FILES = ("description.json", "prompt.md", "storyboard.md")
LIST_FIELDS = ("数学公式", "相关知识点", "manim动画涉及元素")
SCENE_BASES = {"Scene", "MovingCameraScene", "ThreeDScene", "ZoomedScene", "VectorScene", "GraphScene"}
PROBLEM = re.compile(r"<problem>\s*(.*?)\s*</problem>", re.DOTALL | re.IGNORECASE)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def problem_from_prompt(text: str) -> tuple[object | None, str | None]:
    match = PROBLEM.search(text)
    if match is None:
        return None, None
    try:
        return json.loads(match.group(1)), None
    except json.JSONDecodeError as exc:
        return None, f"problem block is not JSON: {exc.msg}"


def scene_candidates(path: Path) -> tuple[list[str], str | None]:
    """Direct Manim subclasses only; unresolved alias/inheritance needs human review."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (UnicodeError, OSError, SyntaxError) as exc:
        return [], f"python parse failed: {type(exc).__name__}"
    names = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        bases = [base.id if isinstance(base, ast.Name) else base.attr if isinstance(base, ast.Attribute) else None for base in node.bases]
        if any(name in SCENE_BASES for name in bases):
            names.append(node.name)
    return sorted(names), None


def audit(root: Path) -> dict:
    root = root.resolve()
    records: list[dict] = []
    template_groups: dict[str, list[str]] = defaultdict(list)
    for level in LEVELS:
        parent = root / level
        if not parent.is_dir():
            continue
        # Only directories that contain knowledge-point metadata count as topics;
        # standalone Python files and chapter helpers are not silently reclassified.
        directories = sorted({p.parent for name in FILES for p in parent.rglob(name)}, key=lambda p: p.as_posix())
        for folder in directories:
            relative = folder.relative_to(root).as_posix()
            parts = folder.relative_to(parent).parts
            found = {name: (folder / name).is_file() for name in FILES}
            issues: list[dict] = []

            def issue(severity: str, code: str, detail: str = "") -> None:
                issues.append({"severity": severity, "code": code, "detail": detail})

            for name, exists in found.items():
                if not exists:
                    issue("warning", "missing_file", name)
            description = None
            if found["description.json"]:
                try:
                    description = json.loads((folder / "description.json").read_text(encoding="utf-8"))
                    if not isinstance(description, dict):
                        issue("error", "invalid_description", "expected JSON object")
                        description = None
                except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                    issue("error", "invalid_description", type(exc).__name__)
            if description is not None:
                for field in LIST_FIELDS:
                    if field in description and not isinstance(description[field], list):
                        issue("error", "invalid_field_type", field)
                for field, index in (("年级", 0), ("学期", 1)):
                    if len(parts) > index and field in description and description[field] != parts[index]:
                        issue("warning", "path_description_mismatch", field)
            prompt_data = None
            prompt_hash = None
            if found["prompt.md"]:
                try:
                    raw = (folder / "prompt.md").read_bytes()
                    text = raw.decode("utf-8")
                    prompt_hash = digest(raw)
                    prompt_data, failure = problem_from_prompt(text)
                    if failure:
                        issue("warning", "invalid_problem_block", failure)
                    if isinstance(prompt_data, dict) and description is not None:
                        for field in ("年级", "学期", "章节", "知识点"):
                            if field in prompt_data and field in description and prompt_data[field] != description[field]:
                                issue("warning", "prompt_description_mismatch", field)
                    if prompt_data is not None and not isinstance(prompt_data, dict):
                        issue("warning", "invalid_problem_type", "expected JSON object")
                    normalized = PROBLEM.sub("<problem>__KNOWLEDGE_POINT__</problem>", text, count=1)
                    template_groups[digest(normalized.encode("utf-8"))].append(relative)
                except (OSError, UnicodeError) as exc:
                    issue("error", "unreadable_prompt", type(exc).__name__)
            py_files = sorted((p for p in folder.glob("*.py") if not p.name.startswith(("test_", "verify_", "__"))), key=lambda p: p.name)
            scenes = {}
            for path in py_files:
                candidates, failure = scene_candidates(path)
                scenes[path.name] = candidates
                if failure:
                    issue("warning", "unreadable_python", f"{path.name}: {failure}")
            if not py_files:
                issue("warning", "missing_scene_source")
            elif not any(scenes.values()):
                issue("warning", "scene_needs_review", "no direct Scene subclass found")
            elif sum(map(len, scenes.values())) > 1:
                issue("warning", "multiple_scene_candidates")
            videos = sorted(p.name for p in folder.glob("*.mp4"))  # filenames only
            if len([name for name in videos if name.endswith("_finish.mp4")]) > 1:
                issue("warning", "multiple_final_videos")
            records.append({"path": relative, "files": found, "prompt_sha256": prompt_hash,
                            "python_scene_candidates": scenes, "video_names": videos,
                            "issues": sorted(issues, key=lambda row: (row["severity"], row["code"], row["detail"]))})
    groups = [{"template_sha256": fingerprint, "count": len(paths), "paths": sorted(paths)}
              for fingerprint, paths in template_groups.items() if len(paths) > 1]
    groups.sort(key=lambda group: (-group["count"], group["template_sha256"]))
    issue_counts: dict[str, int] = defaultdict(int)
    for record in records:
        for issue in record["issues"]:
            issue_counts[issue["code"]] += 1
    return {"format": "manim-math-curriculum-audit-v1", "topic_directory_count": len(records),
            "issue_counts": dict(sorted(issue_counts.items())), "shared_prompt_templates": groups,
            "records": records}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path, help="write JSON report only to this explicit path")
    parser.add_argument("--fail-on", choices=("none", "error", "warning"), default="error")
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error("--root must be an existing directory")
    result = audit(args.root)
    data = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(data, encoding="utf-8")
        except OSError as exc:
            print(f"cannot write audit report: {exc}", file=sys.stderr)
            return 2
    else:
        sys.stdout.write(data)
    severities = {issue["severity"] for record in result["records"] for issue in record["issues"]}
    return int(args.fail_on == "warning" and bool(severities) or args.fail_on == "error" and "error" in severities)


if __name__ == "__main__":
    raise SystemExit(main())

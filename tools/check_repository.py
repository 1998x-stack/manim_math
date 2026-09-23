#!/usr/bin/env python3
"""Lightweight structural QA for documentation, categories, and skills (no Manim)."""
from __future__ import annotations

import ast
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ("README.md", "AGENTS.md", "docs/README.md", "docs/architecture/audit.md", "docs/architecture/architecture.md", "docs/architecture/categories.md", "docs/architecture/migration.md", "docs/engineering/scene-workflow.md", "docs/engineering/quality-gates.md", "skills/README.md", "catalog/README.md")
AGENTS = (".codex", ".opencode", ".claude")


def validate() -> list[str]:
    errors: list[str] = []
    for name in DOCS:
        if not (ROOT / name).is_file():
            errors.append(f"missing document: {name}")
    sources = sorted((ROOT / "skills/source").glob("*/SKILL.md"))
    if not sources:
        errors.append("missing canonical SKILL.md files")
    for path in sources:
        raw = path.read_text(encoding="utf-8")
        head = re.match(r"\A---\n(.*?)\n---\n", raw, re.S)
        if not head or not re.search(r"(?m)^name:\s*\S+", head.group(1)) or not re.search(r"(?m)^description:\s*\S+", head.group(1)):
            errors.append(f"bad skill frontmatter: {path.relative_to(ROOT)}")
        for agent in AGENTS:
            mirror = ROOT / agent / "skills" / path.parent.name / "SKILL.md"
            if not mirror.is_file() or mirror.read_bytes() != path.read_bytes():
                errors.append(f"missing or drifted mirror: {mirror.relative_to(ROOT)}")
    for name in ("assets/build_catalog.py", "tools/sync_skills.py", "tools/check_repository.py", "tools/audit_catalog.py"):
        path = ROOT / name
        if path.exists():
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=name)
            except SyntaxError as exc:
                errors.append(f"syntax: {name}: {exc}")
    try:
        registry = json.loads((ROOT / "catalog/categories.json").read_text(encoding="utf-8"))
        example = json.loads((ROOT / "catalog/topic.example.json").read_text(encoding="utf-8"))
        moves = json.loads((ROOT / "catalog/documentation-moves.json").read_text(encoding="utf-8"))
        if registry["schemaVersion"] != 1 or example["schemaVersion"] != 1 or moves["schemaVersion"] != 1:
            errors.append("catalog schemaVersion mismatch")
        for dimension, spec in registry["dimensions"].items():
            if spec["cardinality"] not in ("one", "many") or not spec["values"]:
                errors.append(f"invalid classification: {dimension}")
            if dimension in example:
                values = example[dimension] if spec["cardinality"] == "many" else [example[dimension]]
                if not all(v in spec["values"] for v in values):
                    errors.append(f"unknown example classification: {dimension}")
        old_paths, new_paths = set(), set()
        for move in moves["moves"]:
            source, dest = move["from"], move["to"]
            if source in old_paths or dest in new_paths or source == dest:
                errors.append(f"duplicate or noop migration: {source} -> {dest}")
            old_paths.add(source)
            new_paths.add(dest)
            src, dst = ROOT / source, ROOT / dest
            if not src.is_file() or not dst.is_file():
                errors.append(f"missing migrated document or legacy stub: {source} -> {dest}")
            elif f"({os.path.relpath(dst, start=src.parent)})" not in src.read_text(encoding="utf-8"):
                errors.append(f"legacy stub does not link to destination: {source}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"catalog registry/migrations error: {exc}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("Repository structural checks passed (not a rendering or math proof check)")

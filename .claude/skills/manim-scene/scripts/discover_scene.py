#!/usr/bin/env python3
"""Discover statically visible Manim Scene classes without importing target code."""
import argparse
import ast
import json
import sys
from pathlib import Path

BASES = {"Scene", "MovingCameraScene", "ThreeDScene", "ZoomedScene", "VectorScene", "LinearTransformationScene"}


def discover(source: str) -> dict:
    tree = ast.parse(source)
    imported = set()
    modules = set()
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module and (node.module == "manim" or node.module.startswith("manim.")):
            for alias in node.names:
                if alias.name in BASES:
                    imported.add(alias.asname or alias.name)
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "manim":
                    modules.add(alias.asname or "manim")
    derived = set(imported)
    candidates, uncertain = [], []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        is_scene = False
        for base in node.bases:
            if isinstance(base, ast.Name):
                is_scene |= base.id in derived
            elif isinstance(base, ast.Attribute) and isinstance(base.value, ast.Name) and base.value.id in modules and base.attr in BASES:
                is_scene = True
            else:
                uncertain.append(node.name)
        if is_scene:
            derived.add(node.name)
            candidates.append(node.name)
    return {"candidates": candidates, "uncertain_classes": sorted(set(uncertain)), "status": "needs_review" if len(candidates) != 1 or uncertain else "static_candidate_only"}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args(argv)
    try:
        result = discover(args.source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, SyntaxError) as exc:
        print(f"discover_scene: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"source": str(args.source), **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

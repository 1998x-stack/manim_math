#!/usr/bin/env python3
"""Testing control plane for suite and representative render selection."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "tests" / "test_manifest.json"
COURSE_ROOTS = {"小学", "初中", "高中"}
VALID_TIERS = {"pr", "main", "nightly"}


def load_manifest(path: Path = DEFAULT_MANIFEST) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("unsupported test manifest schema")
    return data


def validate_manifest(data: dict, root: Path = ROOT, check_sources: bool = True) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    for section in ("suites", "renders"):
        if not isinstance(data.get(section), list):
            errors.append(f"{section} must be a list")
            continue
        for item in data[section]:
            item_id = item.get("id")
            if not item_id:
                errors.append(f"{section} entry missing id")
            elif item_id in ids:
                errors.append(f"duplicate id: {item_id}")
            else:
                ids.add(item_id)

    domains: set[str] = set()
    for item in data.get("renders", []):
        source, scene = item.get("source", ""), item.get("scene")
        domain = item.get("domain")
        if not source or not scene:
            errors.append(f"render {item.get('id')} needs source and scene")
            continue
        if check_sources and not (root / source).is_file():
            errors.append(f"render source missing: {source}")
        if item.get("tier") not in VALID_TIERS:
            errors.append(f"render {item.get('id')} has invalid tier")
        if not domain:
            errors.append(f"render {item.get('id')} needs domain")
        else:
            domains.add(domain)
        for key in ("width", "height"):
            if not isinstance(item.get(key), int) or item[key] <= 0:
                errors.append(f"render {item.get('id')} needs positive {key}")

    required = set(data.get("required_render_domains", []))
    missing = sorted(required - domains)
    if missing:
        errors.append("missing required render domains: " + ", ".join(missing))
    return errors


def lesson_dir(path: str) -> str | None:
    p = Path(path)
    parts = p.parts
    if not parts or parts[0] not in COURSE_ROOTS:
        return None
    if p.suffix.lower() not in {".py", ".json", ".md"}:
        return None
    return str(p.parent)


def changed_lessons(paths: list[str]) -> list[str]:
    return sorted({lesson for path in paths if (lesson := lesson_dir(path))})


def selected_renders(data: dict, tier: str) -> list[dict]:
    order = {"pr": 0, "main": 1, "nightly": 2}
    return [item for item in data["renders"] if order[item["tier"]] <= order[tier]]


def renders_for_changes(data: dict, paths: list[str]) -> list[dict]:
    lessons = set(changed_lessons(paths))
    return [item for item in data["renders"] if str(Path(item["source"]).parent) in lessons]


def matrix_from_items(items: list[dict]) -> dict:
    return {
        "include": [
            {
                "id": item["id"],
                "source": item["source"],
                "scene": item["scene"],
                "width": item["width"],
                "height": item["height"],
                "resolution": f"{item['width']},{item['height']}",
                "lesson": str(Path(item["source"]).parent),
            }
            for item in items
        ]
    }


def render_matrix(data: dict, tier: str) -> dict:
    return matrix_from_items(selected_renders(data, tier))


def changed_render_matrix(data: dict, paths: list[str]) -> dict:
    return matrix_from_items(renders_for_changes(data, paths))


def read_paths(path: Path | None, positional: list[str]) -> list[str]:
    if path is None:
        return positional
    return [line for line in path.read_text(encoding="utf-8").splitlines() if line]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("--skip-source-check", action="store_true")
    sub.add_parser("sources")

    changed = sub.add_parser("changed-lessons")
    changed.add_argument("paths", nargs="*")
    changed.add_argument("--paths-file", type=Path)

    for name in ("renders", "matrix"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--tier", choices=("pr", "main", "nightly"), required=True)

    changed_matrix = sub.add_parser("changed-matrix")
    changed_matrix.add_argument("paths", nargs="*")
    changed_matrix.add_argument("--paths-file", type=Path)

    args = parser.parse_args()
    data = load_manifest(args.manifest)

    if args.command == "validate":
        errors = validate_manifest(data, check_sources=not args.skip_source_check)
        if errors:
            print("\n".join(errors))
            return 1
        print(f"manifest ok: {len(data['suites'])} suites, {len(data['renders'])} renders")
        return 0

    if args.command == "sources":
        for item in data.get("renders", []):
            print(item["source"])
        return 0

    if args.command == "changed-lessons":
        for lesson in changed_lessons(read_paths(args.paths_file, args.paths)):
            print(lesson)
        return 0

    if args.command == "changed-matrix":
        matrix = changed_render_matrix(data, read_paths(args.paths_file, args.paths))
        print(json.dumps(matrix, ensure_ascii=False, separators=(",", ":")))
        return 0

    if args.command == "matrix":
        print(json.dumps(render_matrix(data, args.tier), ensure_ascii=False, separators=(",", ":")))
        return 0

    for item in selected_renders(data, args.tier):
        print(json.dumps(item, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

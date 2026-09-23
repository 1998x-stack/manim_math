#!/usr/bin/env python3
"""Freeze and compare the *legacy* Gallery contract without rewriting its source.

This tool does not allocate new topic IDs, discover Scenes or verify media files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = ("id", "number", "name", "docstring", "pyFile", "videoFile", "hasVideo")


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def snapshot(raw_catalog: bytes) -> dict:
    catalog = json.loads(raw_catalog)
    if not isinstance(catalog.get("levels"), list):
        raise ValueError("legacy catalog must contain levels array")
    records: list[dict] = []
    seen: set[str] = set()
    for level in catalog["levels"]:
        for grade in level.get("grades", []):
            for semester in grade.get("semesters", []):
                for chapter in semester.get("chapters", []):
                    for topic in chapter.get("topics", []):
                        legacy_id = topic.get("id")
                        if not isinstance(legacy_id, str) or not legacy_id:
                            raise ValueError("missing legacy topic id")
                        if legacy_id in seen:
                            raise ValueError(f"duplicate legacy id: {legacy_id}")
                        seen.add(legacy_id)
                        missing = set(KEYS) - topic.keys()
                        if missing:
                            raise ValueError(f"{legacy_id}: missing legacy fields: {sorted(missing)}")
                        if not isinstance(topic["pyFile"], str) or not topic["pyFile"]:
                            raise ValueError(f"{legacy_id}: missing pyFile")
                        if not isinstance(topic["hasVideo"], bool) or topic["hasVideo"] != (topic["videoFile"] is not None):
                            raise ValueError(f"{legacy_id}: inconsistent video flags")
                        records.append({
                            "legacy_id": legacy_id,
                            "level_id": level.get("id"),
                            "grade": grade.get("name"),
                            "semester": semester.get("name"),
                            "chapter": chapter.get("name"),
                            **{key: topic[key] for key in KEYS},
                        })
    records.sort(key=lambda record: record["legacy_id"])
    return {
        "format": "manim-math-legacy-contract-v1",
        "source_sha256": sha256(raw_catalog),
        "count": len(records),
        "records": records,
    }


def compare(current: dict, previous: dict) -> dict:
    old = {r["legacy_id"]: r for r in previous["records"]}
    new = {r["legacy_id"]: r for r in current["records"]}
    return {
        "added": sorted(new.keys() - old.keys()),
        "removed": sorted(old.keys() - new.keys()),
        "changed": {key: {
            field: {"before": old[key].get(field), "after": new[key].get(field)}
            for field in sorted(old[key].keys() | new[key].keys())
            if old[key].get(field) != new[key].get(field)
        } for key in sorted(old.keys() & new.keys()) if old[key] != new[key]},
        "source_sha256_changed": current["source_sha256"] != previous["source_sha256"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "assets/catalog.json")
    parser.add_argument("--write-snapshot", type=Path, help="explicitly write baseline; never overwrites")
    parser.add_argument("--compare", type=Path, help="compare with a previously frozen snapshot")
    parser.add_argument("--expect-count", type=int)
    args = parser.parse_args(argv)
    if args.write_snapshot and args.compare:
        parser.error("--compare and --write-snapshot are mutually exclusive")
    try:
        current = snapshot(args.catalog.read_bytes())
        if args.expect_count is not None and args.expect_count != current["count"]:
            raise ValueError(f"expected {args.expect_count} legacy entries, got {current['count']}")
        if args.write_snapshot:
            args.write_snapshot.parent.mkdir(parents=True, exist_ok=True)
            with args.write_snapshot.open("xb") as handle:
                handle.write(canonical_bytes(current))
            print(f"Wrote baseline: {args.write_snapshot} ({current['count']} entries)")
        elif args.compare:
            previous = json.loads(args.compare.read_text(encoding="utf-8"))
            if previous.get("format") != current["format"]:
                raise ValueError("incompatible baseline format")
            delta = compare(current, previous)
            print(json.dumps(delta, ensure_ascii=False, indent=2, sort_keys=True))
            return 1 if (delta["added"] or delta["removed"] or delta["changed"] or delta["source_sha256_changed"]) else 0
        else:
            print(json.dumps({"count": current["count"], "source_sha256": current["source_sha256"], "format": current["format"]}, ensure_ascii=False, sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"legacy contract error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

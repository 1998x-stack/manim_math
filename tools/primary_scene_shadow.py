#!/usr/bin/env python3
"""Read-only primary Scene shadow mapping: never rewrites Gallery or media.

Run from repository root:
    python -m tools.primary_scene_shadow --output /tmp/primary-scene-shadow.json
    python -m tools.primary_scene_shadow --require-complete

A source-reviewed choice identifies a Python file and Scene class only.
It is not evidence that an existing MP4 was rendered from that Scene.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import sys

from tools.audit_primary_sources import GRADE_NAMES, audit as audit_sources

DEFAULT_MANIFEST = Path("catalog/primary-scene-overrides.json")
DEFAULT_GALLERY = Path("assets/catalog.json")


class ManifestError(ValueError):
    """Invalid or stale explicit Scene association."""


def load_gallery(path: Path) -> dict[str, list[dict]]:
    """Read existing Gallery associations, not source-name heuristics."""
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    found: dict[str, list[dict]] = {}
    for level in data.get("levels", []):
        if level.get("id") != "xiaoxue":
            continue
        for grade in level.get("grades", []):
            for semester in grade.get("semesters", []):
                for chapter in semester.get("chapters", []):
                    for topic in chapter.get("topics", []):
                        source = topic.get("pyFile")
                        if not isinstance(source, str) or not source.startswith("小学/"):
                            continue
                        directory = PurePosixPath(source).parent.as_posix()
                        found.setdefault(directory, []).append({
                            "legacy_id": topic.get("id"),
                            "pyFile": source,
                            "videoFile": topic.get("videoFile"),
                        })
    return found


def safe_topic(value: str) -> bool:
    """Reject paths that could escape the checked-out curriculum."""
    if not isinstance(value, str) or "\\" in value:
        return False
    path = PurePosixPath(value)
    return (
        not path.is_absolute()
        and len(path.parts) >= 5
        and path.parts[0] == "小学"
        and path.parts[1] in GRADE_NAMES
        and all(part not in {"", ".", ".."} for part in path.parts)
        and path.as_posix() == value
    )


def read_manifest(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("mode") != "shadow":
        raise ManifestError("requires schema_version=1 and mode=shadow")
    topics = data.get("topics")
    if not isinstance(topics, list):
        raise ManifestError("manifest topics must be a list")
    return topics


def build_shadow(root: Path, manifest: Path | None = None) -> dict:
    root = root.resolve()
    manifest_path = manifest or root / DEFAULT_MANIFEST
    entries = read_manifest(manifest_path)
    audit = audit_sources(root)
    complete = audit["summary"]["complete_checkout"]
    candidates = {
        topic["path"]: topic
        for topic in audit["topics"]
        if topic["path"].split("/")[1] in GRADE_NAMES
        and len(topic["python_files"]) > 1
    }
    by_file = {entry["path"]: entry for entry in audit["files"]}
    gallery = load_gallery(root / DEFAULT_GALLERY)
    validations: list[str] = []
    mapped: dict[str, dict] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            validations.append("manifest entry must be an object")
            continue
        topic = entry.get("topic")
        if not safe_topic(topic):
            validations.append(f"invalid topic path: {topic!r}")
            continue
        if topic in mapped:
            validations.append(f"duplicate topic: {topic}")
            continue
        mapped[topic] = entry
        status = entry.get("status")
        if status not in {"source-reviewed", "needs-review"}:
            validations.append(f"{topic}: invalid status {status!r}")
            continue
        if status == "needs-review":
            if not isinstance(entry.get("reason"), str) or not entry["reason"].strip():
                validations.append(f"{topic}: needs-review requires reason")
            if "source" in entry or "scene_class" in entry:
                validations.append(f"{topic}: unresolved selection cannot specify source or scene_class")
        else:
            source = entry.get("source")
            scene_class = entry.get("scene_class")
            evidence = entry.get("evidence")
            if (not isinstance(source, str) or not source.startswith(topic + "/")
                    or PurePosixPath(source).parent.as_posix() != topic
                    or not source.endswith(".py")):
                validations.append(f"{topic}: source must be a Python file directly inside topic")
                continue
            if not isinstance(scene_class, str) or not scene_class.isidentifier():
                validations.append(f"{topic}: invalid scene_class")
                continue
            if not isinstance(evidence, str) or not evidence.strip():
                validations.append(f"{topic}: source-reviewed requires evidence")
            if topic in candidates:
                file = by_file.get(source)
                if file is None:
                    validations.append(f"{topic}: selected source does not exist: {source}")
                elif scene_class not in file["scenes"]:
                    validations.append(f"{topic}: {scene_class} is not a direct Scene in {source}")
                elif file["role"] != "direct-scene":
                    validations.append(f"{topic}: selected source is not a directly declared Scene")

    # Compare against the actual scanned tree only when a complete tracked
    # checkout is available, or in a non-Git isolated fixture (complete=None).
    if complete is not False:
        for topic in sorted(candidates.keys() - mapped.keys()):
            validations.append(f"missing manifest topic: {topic}")
        for topic in sorted(mapped.keys() - candidates.keys()):
            validations.append(f"manifest topic no longer has multiple Python files: {topic}")

    rows = []
    for topic, inventory in sorted(candidates.items()):
        record = mapped.get(topic)
        status = record.get("status") if record else "unmapped"
        legacy = gallery.get(topic, [])
        choice = (
            {"source": record["source"], "scene_class": record["scene_class"]}
            if status == "source-reviewed" else None
        )
        changed = bool(
            choice is not None and len(legacy) == 1
            and choice["source"] != legacy[0]["pyFile"]
        )
        rows.append({
            "topic": topic,
            "status": status,
            "selected": choice,
            "reason_or_evidence": (
                record.get("evidence", "") if choice else record.get("reason", "") if record else ""
            ),
            "sources": [
                {"path": name, "role": by_file[name]["role"], "scenes": by_file[name]["scenes"]}
                for name in inventory["python_files"]
            ],
            "legacy_gallery": legacy,
            "shadow_differs_from_gallery_source": changed,
            "requires_gallery_media_review": changed and any(item.get("videoFile") for item in legacy),
        })
    return {
        "schema_version": 1,
        "mode": "shadow",
        "scope": "小学-多源码知识点",
        "summary": {
            "multi_python_topics_scanned": len(rows),
            "manifest_topics": len(mapped),
            "source_reviewed": sum(r["status"] == "source-reviewed" for r in rows),
            "needs_review": sum(r["status"] == "needs-review" for r in rows),
            "shadow_gallery_source_diffs": sum(r["shadow_differs_from_gallery_source"] for r in rows),
            "requires_media_review": sum(r["requires_gallery_media_review"] for r in rows),
            "complete_checkout": complete,
            "not_checked_out": audit["summary"]["not_checked_out"],
            "gallery_missing_topics": sum(not r["legacy_gallery"] for r in rows),
            "validation_errors": len(validations),
        },
        "validation_errors": validations,
        "records": rows,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--manifest", type=Path, help="Custom manifest, e.g. a fixture")
    parser.add_argument("--output", type=Path, help="Write report to explicit path, default stdout")
    parser.add_argument("--require-complete", action="store_true",
                        help="Fail if sparse checkout omits tracked primary Python files")
    args = parser.parse_args(argv)
    try:
        report = build_shadow(args.root, args.manifest)
        rendered = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
    except (OSError, UnicodeError, json.JSONDecodeError, ManifestError) as exc:
        parser.exit(2, f"Cannot generate Scene shadow report: {exc}\n")
    bad_checkout = args.require_complete and report["summary"]["complete_checkout"] is not True
    return int(bool(report["validation_errors"]) or bad_checkout)


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read-only report of legacy gallery catalog IDs, source and media references."""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def collect_topics(catalog: dict):
    for level in catalog.get("levels", []):
        for grade in level.get("grades", []):
            for sem in grade.get("semesters", []):
                for chapter in sem.get("chapters", []):
                    for topic in chapter.get("topics", []):
                        yield level.get("id"), topic


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "assets/catalog.json")
    parser.add_argument("--strict", action="store_true", help="fail on duplicate IDs or missing local files")
    parser.add_argument("--skip-file-check", action="store_true", help="inventory only (for sparse CI checkouts without videos/scenes)")
    args = parser.parse_args()
    try:
        payload = json.loads(args.catalog.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"cannot load catalog: {exc}", file=sys.stderr)
        return 2
    topics = list(collect_topics(payload))
    ids = collections.Counter(t.get("id") for _, t in topics)
    source_paths = collections.Counter(t.get("pyFile") for _, t in topics)
    video_paths = collections.Counter(t.get("videoFile") for _, t in topics if t.get("videoFile"))
    missing_sources = []
    missing_videos = []
    if not args.skip_file_check:
        missing_sources = sorted({str(p) for _, t in topics if not (p := t.get("pyFile")) or not (ROOT / p).is_file()})
        missing_videos = sorted({str(p) for _, t in topics if (p := t.get("videoFile")) and not (ROOT / p).is_file()})
    stats = {
        "catalog": str(args.catalog), "topicCount": len(topics),
        "byLevel": dict(collections.Counter(level for level, _ in topics)),
        "duplicateIds": sorted(str(k) for k, v in ids.items() if v > 1),
        "sharedScenePaths": {str(k): v for k, v in source_paths.items() if v > 1},
        "sharedVideoPaths": {str(k): v for k, v in video_paths.items() if v > 1},
        "fileCheckPerformed": not args.skip_file_check,
        "missingSceneFiles": missing_sources,
        "missingVideoFiles": missing_videos,
        "note": "Presence checks require a full local checkout; absent ignored media does not by itself mean a published URL is broken."
    }
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    return 1 if args.strict and (stats["duplicateIds"] or missing_sources or missing_videos) else 0


if __name__ == "__main__":
    raise SystemExit(main())

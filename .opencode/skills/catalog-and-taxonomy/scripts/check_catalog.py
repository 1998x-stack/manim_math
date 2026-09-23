#!/usr/bin/env python3
"""Read-only legacy gallery JSON structure check; no filesystem/video probes."""
import argparse
import json
import sys
from pathlib import Path


def validate(catalog):
    if not isinstance(catalog, dict) or not isinstance(catalog.get("levels"), list):
        return ["levels must be a list"], 0
    issues, seen, count = [], set(), 0
    for level in catalog["levels"]:
        for grade in level.get("grades", []):
            for sem in grade.get("semesters", []):
                for chap in sem.get("chapters", []):
                    for topic in chap.get("topics", []):
                        count += 1
                        tid = topic.get("id")
                        if not isinstance(tid, str) or not tid:
                            issues.append(f"entry {count}: missing id")
                        elif tid in seen:
                            issues.append(f"duplicate id: {tid}")
                        else:
                            seen.add(tid)
                        for key in ("number", "name", "docstring", "pyFile", "videoFile", "hasVideo"):
                            if key not in topic:
                                issues.append(f"{tid}: missing {key}")
                        if not isinstance(topic.get("pyFile"), str) or not topic["pyFile"]:
                            issues.append(f"{tid}: invalid pyFile")
                        video = topic.get("videoFile")
                        if video is not None and (not isinstance(video, str) or not video):
                            issues.append(f"{tid}: invalid videoFile")
                        if not isinstance(topic.get("hasVideo"), bool) or topic["hasVideo"] != (video is not None):
                            issues.append(f"{tid}: invalid hasVideo/videoFile")
    return issues, count


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    args = parser.parse_args(argv)
    try:
        issues, count = validate(json.loads(args.catalog.read_text(encoding="utf-8")))
    except (OSError, UnicodeError, ValueError, TypeError, AttributeError) as exc:
        print(f"check_catalog: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"entries": count, "errors": issues, "scope": "structure only"}, ensure_ascii=False, indent=2))
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())

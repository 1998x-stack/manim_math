#!/usr/bin/env python3
"""Read-only media manifest sanity checks; no FFmpeg/Manim dependencies."""
import argparse
import json
import sys
from pathlib import Path


def validate(data, root: Path, require_files=False):
    if not isinstance(data, dict):
        return ["manifest must be an object"]
    issues = []
    for field in ("scene_id", "source_video", "final_video", "license_status", "render_status", "visual_status"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            issues.append(f"{field} must be nonblank string")
    source, final = data.get("source_video"), data.get("final_video")
    if source == final and source not in (None, "unknown"):
        issues.append("source and final video must differ (no implicit overwrite)")
    if require_files:
        for field in ("source_video", "final_video"):
            value = data.get(field)
            if isinstance(value, str) and value not in ("unknown", ""):
                candidate = (root / value).resolve()
                if not candidate.is_relative_to(root.resolve()) or not candidate.is_file():
                    issues.append(f"{field}: absent or outside root")
    return issues


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--require-files", action="store_true")
    args = parser.parse_args(argv)
    try:
        errors = validate(json.loads(args.manifest.read_text(encoding="utf-8")), args.root, args.require_files)
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(f"check_manifest: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"errors": errors, "scope": "manifest only; not media or license verification"}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

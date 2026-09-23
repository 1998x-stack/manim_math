#!/usr/bin/env python3
"""Read-only migration-plan validation: relative paths, duplicates and overwrite risks."""
import argparse
import json
import sys
from pathlib import Path, PurePosixPath


def safe_path(value):
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and all(x not in ("", ".", "..") for x in value.split("/")) and ":" not in value.split("/")[0]


def validate(data, root):
    if not isinstance(data, dict) or not isinstance(data.get("moves"), list):
        return ["moves must be a list"]
    errors, origins, destinations = [], set(), set()
    for number, move in enumerate(data["moves"], 1):
        if not isinstance(move, dict):
            errors.append(f"move {number}: not an object")
            continue
        origin, dest = move.get("from"), move.get("to")
        if not safe_path(origin) or not safe_path(dest):
            errors.append(f"move {number}: unsafe path")
            continue
        if origin == dest or origin in origins or dest in destinations:
            errors.append(f"move {number}: noop or repeated source/destination")
        origins.add(origin)
        destinations.add(dest)
        if not (root / origin).is_file():
            errors.append(f"move {number}: missing source")
        if (root / dest).exists() and dest not in origins:
            errors.append(f"move {number}: destination already exists")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        errors = validate(json.loads(args.plan.read_text(encoding="utf-8")), args.root)
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(f"check_moves: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"errors": errors, "scope": "read-only path validation"}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

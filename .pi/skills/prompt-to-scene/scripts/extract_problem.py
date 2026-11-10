#!/usr/bin/env python3
"""Extract exactly one <problem> JSON block from a historical prompt, without executing it."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def extract(text: str) -> object:
    blocks = re.findall(r"<problem>\s*(.*?)\s*</problem>", text, flags=re.S | re.I)
    if len(blocks) != 1:
        raise ValueError(f"expected exactly one complete <problem> block, found {len(blocks)}")
    block = blocks[0].strip()
    if block.startswith("```"):
        match = re.fullmatch(r"```(?:json)?\s*\n(.*?)\n```", block, flags=re.S | re.I)
        if not match:
            raise ValueError("malformed fenced JSON block")
        block = match.group(1)
    value = json.loads(block)
    if not isinstance(value, (dict, list)):
        raise ValueError("problem must be a JSON object or list")
    return value


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--output", type=Path, help="new JSON path; refuses to overwrite")
    args = parser.parse_args(argv)
    try:
        raw = args.prompt.read_bytes()
        value = extract(raw.decode("utf-8"))
        result = {"source": str(args.prompt), "sha256": hashlib.sha256(raw).hexdigest(), "problem": value, "status": "candidate_needs_review"}
        content = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as dest:
                dest.write(content)
        else:
            sys.stdout.write(content)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"extract_problem: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

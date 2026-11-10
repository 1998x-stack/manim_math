#!/usr/bin/env python3
"""Validate mathematical-specification JSON structure; never claim proof validity."""
import argparse
import json
import sys
from pathlib import Path

STATUSES = {"needs_review", "illustration_only", "verified_by_proof", "verified_by_source"}


def validate(data: object) -> list[str]:
    if not isinstance(data, dict):
        return ["specification must be an object"]
    errors = []
    for field in ("claim", "domain"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"{field} requires nonblank text")
    for field in ("givens", "derivation", "counterexamples", "tests", "evidence"):
        if not isinstance(data.get(field), list):
            errors.append(f"{field} must be a list")
    if data.get("proof_status") not in STATUSES:
        errors.append("invalid proof_status")
    if data.get("proof_status") in ("verified_by_proof", "verified_by_source") and not data.get("evidence"):
        errors.append("verified status requires evidence")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    args = parser.parse_args(argv)
    try:
        errors = validate(json.loads(args.spec.read_text(encoding="utf-8")))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"spec parse failed: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Specification structure OK; mathematical proof NOT checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

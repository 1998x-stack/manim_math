#!/usr/bin/env python3
"""Report literal CJK text in MathTex/Tex constructor arguments; static heuristic only."""
import argparse
import ast
import json
import re
import sys
from pathlib import Path

CJK = re.compile(r"[\u3400-\u9fff]")


def scan(source: str) -> list[dict]:
    tree = ast.parse(source)
    findings = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        name = func.id if isinstance(func, ast.Name) else func.attr if isinstance(func, ast.Attribute) else ""
        if name not in {"MathTex", "Tex"}:
            continue
        for arg in node.args:
            for child in ast.walk(arg):
                if isinstance(child, ast.Constant) and isinstance(child.value, str) and CJK.search(child.value):
                    findings.append({"line": child.lineno, "constructor": name, "reason": "CJK in formula literal"})
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args(argv)
    try:
        findings = scan(args.source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, SyntaxError) as exc:
        print(f"scan_mathtex: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"source": str(args.source), "findings": findings, "scope": "literal-only; no LaTeX or font verification"}, ensure_ascii=False, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

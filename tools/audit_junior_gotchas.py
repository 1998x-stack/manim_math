"""Scan junior-high Manim Python files for documented historical gotchas.

No Manim dependency; findings are candidates, not a substitute for rendering or
checking the mathematical truth of a scene.

Usage:
  python tools/audit_junior_gotchas.py --json
  python tools/audit_junior_gotchas.py --root /path/to/repo --strict
"""

import argparse
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRADES = ("六年级", "七年级", "八年级", "九年级")
LATEX_UNICODE = set("°÷×∠≤≥")


def _name(expr):
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, ast.Attribute):
        return expr.attr
    return ""


def _literal_parts(expr):
    if isinstance(expr, ast.Constant) and isinstance(expr.value, str):
        yield expr.value
    elif isinstance(expr, ast.JoinedStr):
        for part in expr.values:
            if isinstance(part, ast.Constant) and isinstance(part.value, str):
                yield part.value


def _contains_chinese(value):
    return any("\u4e00" <= char <= "\u9fff" for char in value)


def _constant_zero_interval(expr):
    if not isinstance(expr, (ast.List, ast.Tuple)) or len(expr.elts) < 2:
        return False
    try:
        left, right = (ast.literal_eval(expr.elts[i]) for i in (0, 1))
    except (ValueError, TypeError, MemoryError, RecursionError):
        return False
    return (isinstance(left, (int, float)) and not isinstance(left, bool)
            and isinstance(right, (int, float)) and not isinstance(right, bool)
            and left == right)


def _empty_list_branch(expr):
    return isinstance(expr, ast.IfExp) and any(
        isinstance(branch, ast.List) and not branch.elts
        for branch in (expr.body, expr.orelse)
    )


def audit_source(source, path):
    """Return line-addressable findings for a single file, without executing it."""
    findings = []

    def add(code, severity, line, message):
        findings.append({"code": code, "severity": severity, "path": str(path),
                         "line": line, "message": message})

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        add("PY_SYNTAX", "error", exc.lineno or 0, exc.msg)
        return findings

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = _name(node.func)
        keywords = {kw.arg: kw.value for kw in node.keywords if kw.arg is not None}

        if name == "Rectangle" and "corner_radius" in keywords:
            add("RECTANGLE_CORNER_RADIUS", "error", node.lineno,
                "Rectangle does not accept corner_radius; review RoundedRectangle")
        if name == "Sector":
            for keyword in ("inner_radius", "outer_radius"):
                if keyword in keywords:
                    add("SECTOR_RADIUS_KEYWORD", "error", node.lineno,
                        "Sector does not accept " + keyword + "; review AnnularSector")
        if name == "scale" and "scale_tips" in keywords:
            add("LEGACY_SCALE_TIPS", "warning", node.lineno,
                "scale_tips keyword may be incompatible with the target Manim API")
        if name in ("MathTex", "Tex"):
            texts = [part for arg in node.args for part in _literal_parts(arg)]
            # Keep findings distinct: a single literal can contain Chinese and °.
            if any(_contains_chinese(text) for text in texts):
                add("CHINESE_IN_TEX", "warning", node.lineno,
                    "Chinese in Tex/MathTex: prefer Text + MathTex; review custom templates")
            if any(LATEX_UNICODE.intersection(text) for text in texts):
                add("UNICODE_IN_TEX", "warning", node.lineno,
                    "Unicode math symbol in Tex/MathTex; use supported LaTeX commands")
        if name == "plot" and "x_range" in keywords and _constant_zero_interval(keywords["x_range"]):
            add("ZERO_WIDTH_PLOT", "error", node.lineno,
                "Axes.plot has a literal zero-width x_range")
        if name == "play" and any(_empty_list_branch(arg) for arg in node.args):
            add("PLAY_EMPTY_ANIMATION", "warning", node.lineno,
                "self.play may receive [] instead of an Animation; build an animation list")
        if name == "seed" and isinstance(node.func, ast.Attribute):
            owner = node.func.value
            if isinstance(owner, ast.Attribute) and _name(owner) == "random" and _name(owner.value) in ("np", "numpy"):
                add("GLOBAL_NUMPY_SEED", "warning", node.lineno,
                    "np.random.seed mutates global RNG; consider a local Generator")
    return sorted(findings, key=lambda item: (item["line"], item["code"]))


def audit(root=ROOT, grades=GRADES):
    root = Path(root)
    findings = []
    counts = {}
    for grade_name in grades:
        grade = root / "初中" / grade_name
        paths = sorted(grade.rglob("*.py")) if grade.is_dir() else []
        counts[grade_name] = len(paths)
        if not grade.is_dir():
            findings.append({"code": "GRADE_MISSING", "severity": "error",
                             "path": (Path("初中") / grade_name).as_posix(), "line": 0,
                             "message": "grade directory is missing"})
        for path in paths:
            relative = path.relative_to(root).as_posix()
            try:
                source = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                findings.append({"code": "READ_ERROR", "severity": "error",
                                 "path": relative, "line": 0, "message": str(exc)})
                continue
            findings.extend(audit_source(source, relative))
    findings.sort(key=lambda item: (item["path"], item["line"], item["code"]))
    return {"grades": counts, "files": sum(counts.values()),
            "errors": sum(x["severity"] == "error" for x in findings),
            "warnings": sum(x["severity"] == "warning" for x in findings),
            "findings": findings}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--grades", nargs="+", choices=GRADES, default=GRADES)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true",
                        help="fail if any finding exists; use after triaging legacy warnings")
    args = parser.parse_args(argv)
    result = audit(args.root, args.grades)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Junior Manim: {result['files']} files, {result['errors']} errors, "
              f"{result['warnings']} warnings")
        for issue in result["findings"]:
            print(f"{issue['path']}:{issue['line']} [{issue['severity']}] "
                  f"{issue['code']}: {issue['message']}")
    return int(bool(result["errors"] or (args.strict and result["warnings"])))


if __name__ == "__main__":
    raise SystemExit(main())

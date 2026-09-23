#!/usr/bin/env python3
"""Mine commit provenance and generate a reviewable, resumable TODO.json.

history: git log --all --no-merges, retaining filenames and actual commit links.
scan: AST-only candidate detection; no source files are automatically modified.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE_DIRS = ("小学", "初中", "高中", "external")
CJK = re.compile(r"[\u3400-\u9fff]")
FIX = re.compile(r"\b(fix|bug|repair|gotcha|error|regression|hotfix)\b|修复|纠错|错误", re.I)
RULES = {
    "SYNTAX_ERROR": ("P0", "Python source cannot be parsed"),
    "CHINESE_IN_TEX": ("P2", "Chinese text in Tex/MathTex; custom CJK template may be valid"),
    "UNICODE_IN_TEX": ("P2", "Unicode degree sign in Tex/MathTex"),
    "SECTOR_RADIUS_KEYWORD": ("P1", "Sector received AnnularSector-specific keyword"),
    "RECTANGLE_CORNER_RADIUS": ("P1", "Rectangle received RoundedRectangle-specific keyword"),
    "LEGACY_SCALE_TIPS": ("P2", "scale(scale_tips=...) may be incompatible"),
    "GLOBAL_NUMPY_SEED": ("P2", "Global numpy random seed may leak between scenes"),
    "NESTED_PLAY": ("P1", "self.play called inside another self.play"),
    "PLAY_EMPTY_ANIMATION": ("P2", "self.play receives a list or a conditional empty-list animation"),
}
EVIDENCE = {
    "CHINESE_IN_TEX": "H01/H06", "UNICODE_IN_TEX": "H02",
    "SECTOR_RADIUS_KEYWORD": "H03", "LEGACY_SCALE_TIPS": "H05",
    "RECTANGLE_CORNER_RADIUS": "H07", "GLOBAL_NUMPY_SEED": "H11",
    "PLAY_EMPTY_ANIMATION": "H09", "NESTED_PLAY": "commit bc81f46c1ffbcb27ea54287716750fe379c28edf",
}


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True,
                          text=True, encoding="utf-8", capture_output=True).stdout


def mine_history(max_commits: int = 0) -> dict:
    shallow = git("rev-parse", "--is-shallow-repository").strip() == "true"
    shas = [line for line in git("log", "--all", "--no-merges", "--format=%H").splitlines() if line]
    if max_commits:
        shas = shas[:max_commits]
    commits = []
    touched = {}
    for sha in shas:
        subject = git("show", "-s", "--format=%s", sha).strip()
        # -z protects Chinese and filenames containing unusual whitespace.
        raw = subprocess.run(["git", "-C", str(ROOT), "diff-tree", "--root", "--no-commit-id",
                              "--name-only", "-r", "-z", sha], check=True, capture_output=True).stdout
        paths = [name.decode("utf-8", "surrogateescape") for name in raw.split(b"\x00") if name]
        for path in paths:
            touched[path] = touched.get(path, 0) + 1
        if FIX.search(subject):
            commits.append({"sha": sha, "subject": subject,
                            "url": f"https://github.com/1998x-stack/manim_math/commit/{sha}",
                            "changed_files": paths})
    return {"schema_version": 1, "scanned_commits": len(shas),
            "history_complete": not shallow and max_commits == 0,
            "caveat": "Commit subjects indicate intent, not verified root cause; inspect each linked diff.",
            "fix_related_commits": commits,
            "touched_files": dict(sorted(touched.items(), key=lambda kv: (-kv[1], kv[0])))}


def func_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{func_name(node.value)}.{node.attr}"
    return ""


def literal_strings(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, ast.JoinedStr):
        return [part.value for part in node.values
                if isinstance(part, ast.Constant) and isinstance(part.value, str)]
    return []


def inspect_source(path: Path, root: Path = ROOT) -> list[dict]:
    source = path.read_bytes()
    rel = path.relative_to(root).as_posix()
    digest = hashlib.sha256(source).hexdigest()
    problems = []

    def record(rule: str, line: int, detail: str = "") -> None:
        key = f"{rel}:{line}:{rule}"
        problems.append({"id": hashlib.sha1(key.encode("utf-8")).hexdigest()[:16],
                         "path": rel, "line": line, "rule": rule,
                         "priority": RULES[rule][0], "description": RULES[rule][1],
                         "detail": detail[:160], "source_sha256": digest,
                         "history_ref": EVIDENCE.get(rule), "status": "needs_review",
                         "checks": {"static": "pending", "math": "pending",
                                    "render": "pending", "visual": "pending"}})
    try:
        tree = ast.parse(source, filename=rel)
    except (SyntaxError, UnicodeError) as exc:
        record("SYNTAX_ERROR", getattr(exc, "lineno", 1) or 1, str(exc))
        return problems
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = func_name(node.func)
        short = name.rsplit(".", 1)[-1]
        if short in ("Tex", "MathTex"):
            text = " ".join(s for arg in node.args for s in literal_strings(arg))
            if CJK.search(text):
                record("CHINESE_IN_TEX", node.lineno, text)
            if "°" in text:
                record("UNICODE_IN_TEX", node.lineno, text)
        keywords = {kw.arg for kw in node.keywords}
        if short == "Sector" and keywords.intersection({"inner_radius", "outer_radius"}):
            record("SECTOR_RADIUS_KEYWORD", node.lineno)
        if short == "Rectangle" and "corner_radius" in keywords:
            record("RECTANGLE_CORNER_RADIUS", node.lineno)
        if short == "scale" and "scale_tips" in keywords:
            record("LEGACY_SCALE_TIPS", node.lineno)
        if name in ("np.random.seed", "numpy.random.seed"):
            record("GLOBAL_NUMPY_SEED", node.lineno)
        if name == "self.play":
            if any(isinstance(inner, ast.Call) and func_name(inner.func) == "self.play"
                   for arg in node.args for inner in ast.walk(arg)):
                record("NESTED_PLAY", node.lineno)
            if any(isinstance(arg, (ast.List, ast.ListComp)) or
                   (isinstance(arg, ast.IfExp) and
                    any(isinstance(branch, ast.List) for branch in (arg.body, arg.orelse)))
                   for arg in node.args):
                record("PLAY_EMPTY_ANIMATION", node.lineno)
    return problems


def files_to_scan(root: Path = ROOT) -> list[Path]:
    return sorted((path for folder in COURSE_DIRS if (root / folder).is_dir()
                   for path in (root / folder).rglob("*.py")
                   if path.is_file() and not path.is_symlink()),
                  key=lambda p: p.relative_to(root).as_posix())


def scan(root: Path = ROOT, *, batch: int | None = None, batch_size: int = 100,
         previous: dict | None = None) -> dict:
    if batch_size < 1 or (batch is not None and batch < 0):
        raise ValueError("batch must be >= 0; batch-size must be >= 1")
    paths = files_to_scan(root)
    total_batches = (len(paths) + batch_size - 1) // batch_size
    if batch is not None and batch >= max(1, total_batches):
        raise ValueError(f"Batch {batch} outside 0..{max(0, total_batches - 1)}")
    chosen = paths if batch is None else paths[batch * batch_size:(batch + 1) * batch_size]
    previously = previous or {}
    selected_names = {path.relative_to(root).as_posix() for path in chosen}
    old_items = {item["id"]: item for item in previously.get("items", [])}
    findings = [item for item in previously.get("items", []) if item["path"] not in selected_names] if batch is not None else []
    for path in chosen:
        for item in inspect_source(path, root):
            old = old_items.get(item["id"])
            if old and old.get("source_sha256") == item["source_sha256"]:
                item["status"] = old.get("status", "needs_review")
                item["checks"] = old.get("checks", item["checks"])
            findings.append(item)
    scanned_files = dict(previously.get("scanned_files", {})) if batch is not None else {}
    for path in chosen:
        scanned_files[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    outstanding = sum(item["status"] not in ("verified", "false_positive") for item in findings)
    return {"schema_version": 1, "generated_at": datetime.now(timezone.utc).isoformat(),
            "scope": list(COURSE_DIRS), "total_python_files": len(paths),
            "batch_size": batch_size, "total_batches": total_batches,
            "last_scanned_batch": batch, "scanned_files": dict(sorted(scanned_files.items())),
            "scanned_file_count": len(scanned_files), "outstanding": outstanding,
            "notice": "AST hits are candidates, not proof of a rendering or mathematical error.",
            "items": sorted(findings, key=lambda entry: (entry["path"], entry["line"], entry["rule"]))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    history = sub.add_parser("history", help="Inventory non-merge commits and files they changed")
    history.add_argument("--max-commits", type=int, default=0, help="0 means all visible commits")
    history.add_argument("--output", type=Path, default=Path("docs/engineering/commit-gotchas.generated.json"))
    audit = sub.add_parser("scan", help="Scan all course Python sources or one numbered batch")
    audit.add_argument("--batch", type=int, help="Zero-based batch; omit to scan all")
    audit.add_argument("--batch-size", type=int, default=100)
    audit.add_argument("--output", type=Path, default=Path("TODO.json"))
    args = parser.parse_args(argv)
    try:
        if args.command == "history":
            data = mine_history(args.max_commits)
        else:
            previous = json.loads(args.output.read_text(encoding="utf-8")) if args.output.is_file() else None
            data = scan(batch=args.batch, batch_size=args.batch_size, previous=previous)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Audit failed: {exc}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} (items={len(data.get('items', []))}, commits={data.get('scanned_commits', 0)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

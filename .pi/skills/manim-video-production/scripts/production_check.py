#!/usr/bin/env python3
"""Opt-in static, render and media gate; outputs into a new directory.

  python scripts/production_check.py /abs/lesson.py ActualScene --math-test /abs/test_math.py --render --preview

This gate never deletes or replaces old media, and cannot certify visual quality.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid

import audit_scene


def run_command(command, log, *, cwd=None, env=None):
    try:
        completed = subprocess.run(command, cwd=cwd, env=env, capture_output=True,
                                   encoding="utf-8", errors="replace", check=False)
        log.write_text(completed.stdout + "\n" + completed.stderr, encoding="utf-8")
        return {"status": "pass" if completed.returncode == 0 else "fail",
                "exit_code": completed.returncode, "command": command, "log": str(log)}
    except OSError as exc:
        log.write_text(str(exc), encoding="utf-8")
        return {"status": "blocked", "command": command, "log": str(log), "reason": str(exc)}


def probe_video(path, log, width, height):
    result = run_command(["ffprobe", "-v", "error", "-show_entries",
                          "stream=codec_type,width,height,r_frame_rate", "-show_entries",
                          "format=duration", "-of", "json", str(path)], log)
    if result["status"] != "pass":
        return result
    try:
        data = json.loads(log.read_text(encoding="utf-8"))
        streams = data.get("streams", [])
        videos = [s for s in streams if s.get("codec_type") == "video"]
        duration = float(data.get("format", {}).get("duration", 0))
        if len(videos) != 1 or not 0 < duration < float("inf"):
            raise ValueError("requires one video stream and positive finite duration")
        if (videos[0].get("width"), videos[0].get("height")) != (width, height):
            raise ValueError(f"actual dimensions: {videos[0].get('width')}x{videos[0].get('height')}, expected {width}x{height}")
        result.update({"video": str(path), "duration_s": duration,
                       "resolution": [width, height], "frame_rate": videos[0].get("r_frame_rate"),
                       "audio_streams": sum(s.get("codec_type") == "audio" for s in streams)})
    except (OSError, ValueError, TypeError, KeyError) as exc:
        result.update({"status": "fail", "reason": str(exc)})
    return result


def inspect_checkpoints(path):
    if not path.is_file() or not path.stat().st_size:
        return {"status": "not_run", "reason": "Scene emitted no runtime checkpoint"}
    try:
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
        if not rows or any(not isinstance(row, dict) or row.get("status") != "pass" or row.get("findings") for row in rows):
            raise ValueError("checkpoint log contains failed or malformed results")
        return {"status": "pass", "count": len(rows), "evidence": str(path),
                "scope": "explicit checkpoints only; not an every-frame review"}
    except (OSError, ValueError, TypeError) as exc:
        return {"status": "fail", "reason": str(exc), "evidence": str(path)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson", type=Path)
    parser.add_argument("scene_class")
    parser.add_argument("--math-test", type=Path)
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--out-dir", type=Path, default=Path("skill-runs"))
    args = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z_]\w*", args.scene_class, flags=re.ASCII) or args.preview and not args.render:
        parser.error("valid class name required; --preview requires --render")
    lesson = args.lesson.expanduser().resolve()
    math_test = args.math_test.expanduser().resolve() if args.math_test else None
    if not lesson.is_file() or math_test and not math_test.is_file():
        parser.error("lesson and optional math test must be existing files")
    out = args.out_dir.expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    run_dir = out / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex)
    run_dir.mkdir(exist_ok=False)
    report = {"scene": str(lesson), "scene_class": args.scene_class,
              "output_directory": str(run_dir), "checks": {}}
    checks = report["checks"]

    def finish():
        failed = [k for k, v in checks.items() if v["status"] in {"fail", "blocked"}]
        pending = [k for k, v in checks.items() if v["status"] == "not_run"]
        report.update({"status": "fail" if failed else ("partial" if pending else "pass"),
                       "failed_or_blocked": failed, "not_run": pending})
        target = run_dir / "report.json"
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"report": str(target), "status": report["status"]}, ensure_ascii=False))
        return 2 if failed else 0

    checks["syntax"] = run_command([sys.executable, "-m", "py_compile", str(lesson)], run_dir / "syntax.log")
    if checks["syntax"]["status"] != "pass":
        return finish()
    try:
        source = lesson.read_text(encoding="utf-8")
        tree = ast.parse(source)
        if not any(isinstance(n, ast.ClassDef) and n.name == args.scene_class for n in ast.walk(tree)):
            raise ValueError(f"Scene class not found: {args.scene_class}")
        findings = audit_scene.audit_source(source)
        errors = [f for f in findings if f["level"] == "ERROR"]
        evidence = run_dir / "ast.json"
        evidence.write_text(json.dumps(findings, ensure_ascii=False, indent=2), encoding="utf-8")
        checks["ast"] = {"status": "fail" if errors else "pass", "errors": len(errors),
                         "warnings": len(findings) - len(errors), "evidence": str(evidence)}
    except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
        checks["ast"] = {"status": "fail", "reason": str(exc)}
    if checks["ast"]["status"] != "pass":
        return finish()
    checks["math_test"] = (run_command([sys.executable, str(math_test)], run_dir / "math.log", cwd=lesson.parent)
                           if math_test else {"status": "not_run", "reason": "no course math test supplied"})
    if checks["math_test"]["status"] in {"fail", "blocked"}:
        return finish()
    if not args.render:
        checks["manim_render"] = {"status": "not_run", "reason": "--render not requested"}
        checks["runtime_checkpoints"] = {"status": "not_run", "reason": "requires a real Scene"}
        checks["frame_review"] = {"status": "not_run", "reason": "human review required"}
        checks["audio_review"] = {"status": "not_run", "reason": "human review required"}
        return finish()
    if importlib.util.find_spec("manim") is None or shutil.which("ffprobe") is None:
        checks["manim_render"] = {"status": "blocked", "reason": "manim or ffprobe unavailable in current environment"}
        return finish()
    media = run_dir / "media"
    media.mkdir()
    checkpoint_file = run_dir / "scene_checkpoints.jsonl"
    env = dict(os.environ, MANIM_PROBE_REPORT=str(checkpoint_file))
    env["PYTHONPATH"] = str(Path(__file__).resolve().parent) + os.pathsep + env.get("PYTHONPATH", "")
    stages = ([("preview", 270, 480, 15)] if args.preview else []) + [("final", 1080, 1920, 30)]
    for stage, width, height, fps in stages:
        output_name = f"skill_{stage}_{uuid.uuid4().hex}"
        command = [sys.executable, "-m", "manim", "render", "-r", f"{width},{height}",
                   "--fps", str(fps), "--media_dir", str(media), "-o", output_name,
                   str(lesson), args.scene_class]
        checks[f"{stage}_render"] = run_command(command, run_dir / f"{stage}_render.log", env=env)
        if checks[f"{stage}_render"]["status"] != "pass":
            return finish()
        videos = list(media.rglob(output_name + ".mp4"))
        if len(videos) != 1:
            checks[f"{stage}_ffprobe"] = {"status": "fail", "reason": "expected exactly one newly named MP4"}
            return finish()
        checks[f"{stage}_ffprobe"] = probe_video(videos[0], run_dir / f"{stage}_ffprobe.log", width, height)
        if checks[f"{stage}_ffprobe"]["status"] != "pass":
            return finish()
    checks["manim_render"] = {"status": "pass", "video": checks["final_ffprobe"]["video"]}
    checks["runtime_checkpoints"] = inspect_checkpoints(checkpoint_file)
    checks["frame_review"] = {"status": "not_run", "reason": "visually inspect initial, middle, extremal and ending frames"}
    checks["audio_review"] = {"status": "not_run", "reason": "listen to original narration and any mixed audio"}
    return finish()


if __name__ == "__main__":
    sys.exit(main())

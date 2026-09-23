#!/usr/bin/env python3
"""Opt-in Manim production gate. Never overwrites existing videos or deletes files.

From the skill directory:
  python scripts/production_check.py /abs/lesson.py Lesson --math-test /abs/test_math.py
  python scripts/production_check.py /abs/lesson.py Lesson --render --preview

Rendering is opt-in and requires installed Manim/ffprobe. All artifacts go into
an exclusive new run directory. This tool cannot judge proof or visual quality.
"""
from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import uuid

import audit_scene


SCENE_NAME = re.compile(r"^[A-Za-z_][A-Za-z_0-9]*$")


def run_command(argv: list[str], log: Path, *, cwd: Path | None = None, env=None) -> dict:
    try:
        process = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True,
                                 encoding="utf-8", errors="replace", check=False)
        output = process.stdout + "\n" + process.stderr
        log.write_text(output, encoding="utf-8")
        return {"status": "pass" if process.returncode == 0 else "fail",
                "returncode": process.returncode, "command": argv, "log": str(log)}
    except OSError as exc:
        log.write_text(f"{type(exc).__name__}: {exc}\n", encoding="utf-8")
        return {"status": "blocked", "command": argv, "log": str(log), "reason": str(exc)}


def probe_video(video: Path, log: Path, *, width: int, height: int) -> dict:
    command = ["ffprobe", "-v", "error", "-show_entries",
               "stream=codec_type,width,height,r_frame_rate", "-show_entries",
               "format=duration", "-of", "json", str(video)]
    result = run_command(command, log)
    if result["status"] != "pass":
        return result
    try:
        payload = json.loads(log.read_text(encoding="utf-8"))
        videos = [s for s in payload.get("streams", []) if s.get("codec_type") == "video"]
        duration = float(payload.get("format", {}).get("duration", 0))
        if len(videos) != 1 or duration <= 0 or not all(
            (isinstance(s.get("width"), int) and isinstance(s.get("height"), int))
            for s in videos
        ):
            raise ValueError("expected exactly one valid video stream and positive duration")
        stream = videos[0]
        if stream["width"] != width or stream["height"] != height:
            raise ValueError(f"video is {stream['width']}x{stream['height']}, expected {width}x{height}")
        result.update({"duration_s": duration, "resolution": [width, height],
                       "audio_streams": sum(s.get("codec_type") == "audio" for s in payload.get("streams", [])),
                       "video": str(video)})
    except (OSError, ValueError, TypeError, KeyError) as exc:
        result.update({"status": "fail", "reason": str(exc)})
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lesson", type=Path)
    parser.add_argument("scene_class")
    parser.add_argument("--math-test", type=Path, help="independent lesson-specific Python test file")
    parser.add_argument("--render", action="store_true", help="actually render, then inspect the MP4")
    parser.add_argument("--preview", action="store_true", help="preview before final render (requires --render)")
    parser.add_argument("--out-dir", type=Path, default=Path("skill-runs"))
    args = parser.parse_args(argv)
    if not SCENE_NAME.fullmatch(args.scene_class) or (args.preview and not args.render):
        parser.error("valid Scene class required; --preview requires --render")
    lesson = args.lesson.expanduser().resolve()
    if not lesson.is_file():
        parser.error(f"lesson not found: {lesson}")
    if args.math_test and not args.math_test.expanduser().resolve().is_file():
        parser.error("--math-test must reference an existing file")
    root = args.out_dir.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    run_dir = root / (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-") + uuid.uuid4().hex[:10])
    run_dir.mkdir(exist_ok=False)
    report = {"scene": str(lesson), "scene_class": args.scene_class,
              "output_directory": str(run_dir), "checks": {}}
    checks = report["checks"]

    def finish() -> int:
        failed = [name for name, item in checks.items() if item["status"] in {"fail", "blocked"}]
        report["status"] = "fail" if failed else "pass"
        report["failed_or_blocked"] = failed
        (run_dir / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"report": str(run_dir / 'report.json'), "status": report["status"],
                          "checks": checks}, ensure_ascii=False, indent=2))
        return 2 if failed else 0

    checks["syntax"] = run_command([sys.executable, "-m", "py_compile", str(lesson)], run_dir / "syntax.log")
    if checks["syntax"]["status"] != "pass":
        return finish()
    try:
        src = lesson.read_text(encoding="utf-8")
        tree = ast.parse(src)
        actual = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)
                  and node.name == args.scene_class]
        if not actual:
            raise ValueError(f"Scene class {args.scene_class} not found in lesson")
        findings = audit_scene.audit_source(src)
        errors = [item for item in findings if item["level"] == "ERROR"]
        (run_dir / "ast.json").write_text(json.dumps(findings, ensure_ascii=False, indent=2), encoding="utf-8")
        checks["ast"] = {"status": "fail" if errors else "pass", "errors": len(errors),
                         "warnings": len(findings) - len(errors), "evidence": str(run_dir / 'ast.json')}
    except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
        checks["ast"] = {"status": "fail", "reason": str(exc)}
    if checks["ast"]["status"] != "pass":
        return finish()
    if args.math_test:
        checks["math_test"] = run_command([sys.executable, str(args.math_test.expanduser().resolve())],
                                           run_dir / "math_test.log", cwd=lesson.parent)
        if checks["math_test"]["status"] != "pass":
            return finish()
    else:
        checks["math_test"] = {"status": "not_run", "reason": "no lesson-specific test provided"}
    if not args.render:
        checks["manim_render"] = {"status": "not_run", "reason": "use --render to opt in"}
        checks["frame_review"] = {"status": "not_run", "reason": "human review required"}
        checks["audio_review"] = {"status": "not_run", "reason": "human review required"}
        return finish()

    media = run_dir / "media"
    media.mkdir()
    probe_report = run_dir / "scene_checkpoints.jsonl"
    env = dict(os.environ, MANIM_PROBE_REPORT=str(probe_report))
    steps = [("preview", 270, 480, 15)] if args.preview else []
    steps.append(("final", 1080, 1920, 30))
    for name, width, height, fps in steps:
        output_name = f"skill_{name}_{uuid.uuid4().hex}"
        cmd = [sys.executable, "-m", "manim", "render", "-r", f"{width},{height}",
               "--fps", str(fps), "--media_dir", str(media), "-o", output_name,
               str(lesson), args.scene_class]
        checks[f"{name}_render"] = run_command(cmd, run_dir / f"{name}_render.log", env=env)
        if checks[f"{name}_render"]["status"] != "pass":
            return finish()
        outputs = list(media.rglob(output_name + ".mp4"))
        if len(outputs) != 1:
            checks[f"{name}_ffprobe"] = {"status": "fail", "reason": "expected one newly named MP4", "matches": [str(p) for p in outputs]}
            return finish()
        checks[f"{name}_ffprobe"] = probe_video(outputs[0], run_dir / f"{name}_ffprobe.log", width=width, height=height)
        if checks[f"{name}_ffprobe"]["status"] != "pass":
            return finish()
    checks["manim_render"] = {"status": "pass", "evidence": checks["final_ffprobe"]["video"]}
    checks["runtime_checkpoints"] = {"status": "pass" if probe_report.is_file() and probe_report.stat().st_size else "not_run",
                                      "evidence": str(probe_report) if probe_report.is_file() else None,
                                      "reason": "Scene must call assert_checkpoint explicitly; inspect individual results"}
    checks["frame_review"] = {"status": "not_run", "reason": "review opening, transitions, extremal states and ending in the actual video"}
    checks["audio_review"] = {"status": "not_run", "reason": "listen to any existing narration or music"}
    return finish()


if __name__ == "__main__":
    sys.exit(main())

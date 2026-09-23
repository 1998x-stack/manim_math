#!/usr/bin/env python3
"""Build exactly one Manim Scene and optionally attach licensed background music.

Examples:
  python tools/build_video.py external/euler_line.py EulerLineScene --install
  python tools/build_video.py '小学/一年级/example.py' ExampleScene --music files/Away.mp3 --force

System prerequisites (FFmpeg, Cairo/Pango, LaTeX and Chinese fonts) are deliberately
not installed with sudo or Homebrew by this script. Run from any working directory.
"""
from __future__ import annotations

import argparse
import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inside_repo(path: str, *, must_exist: bool = True) -> Path:
    candidate = Path(path)
    candidate = (candidate if candidate.is_absolute() else ROOT / candidate).resolve()
    if not candidate.is_relative_to(ROOT):
        raise ValueError(f"Path outside repository: {candidate}")
    if must_exist and not candidate.is_file():
        raise FileNotFoundError(candidate)
    return candidate


def validate_scene(source: Path, scene: str) -> None:
    if not re.fullmatch(r"[A-Za-z_]\w*", scene, flags=re.ASCII):
        raise ValueError(f"Invalid Scene name: {scene!r}")
    tree = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    classes = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    if scene not in classes:
        raise ValueError(f"Scene {scene!r} not found in {source}; top-level classes: {classes}")


def python_in_venv(directory: Path) -> Path:
    return directory / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def provision_env(directory: Path, *, install: bool) -> Path:
    python = python_in_venv(directory)
    if not python.is_file():
        if not install:
            raise RuntimeError(f"Missing {python}; rerun with --install")
        venv.EnvBuilder(with_pip=True).create(directory)
    if install:
        subprocess.run([str(python), "-m", "pip", "install", "manim"], check=True)
    subprocess.run([str(python), "-m", "manim", "--version"], check=True,
                   stdout=subprocess.DEVNULL)
    return python


def require_executable(name: str) -> str:
    executable = shutil.which(name)
    if not executable:
        raise RuntimeError(f"Required executable not found: {name}")
    return executable


def build(source: str, scene: str, *, output: str | None = None,
          music: str | None = None, force: bool = False, install: bool = False,
          venv_dir: str = ".venv", quality: str = "l") -> Path:
    source_path = inside_repo(source)
    if source_path.suffix != ".py":
        raise ValueError("Source must be a Python file")
    validate_scene(source_path, scene)
    output_path = inside_repo(output, must_exist=False) if output else source_path.with_suffix(".mp4")
    if output_path.suffix.lower() != ".mp4":
        raise ValueError("Output must end in .mp4")
    if output_path.exists() and not force:
        raise FileExistsError(f"Output exists; use --force to replace: {output_path}")
    music_path = inside_repo(music) if music else None
    ffmpeg = require_executable("ffmpeg") if music_path else None
    python = provision_env(inside_repo(venv_dir, must_exist=False), install=install)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".manim-build-", dir=output_path.parent) as temp:
        stage = Path(temp)
        media = stage / "media"
        subprocess.run([str(python), "-m", "manim", "render", f"-q{quality}",
                        "--format", "mp4", "--media_dir", str(media),
                        "--output_file", "built", str(source_path), scene],
                       check=True, cwd=ROOT)
        renders = list(media.rglob("built.mp4"))
        if len(renders) != 1 or not renders[0].is_file() or renders[0].stat().st_size == 0:
            raise RuntimeError(f"Expected exactly one nonempty built.mp4; found {renders}")
        candidate = renders[0]
        if music_path:
            muxed = stage / "with-music.mp4"
            subprocess.run([ffmpeg, "-nostdin", "-hide_banner", "-loglevel", "error", "-y",
                            "-i", str(candidate), "-stream_loop", "-1", "-i", str(music_path),
                            "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac",
                            "-shortest", "-movflags", "+faststart", str(muxed)], check=True)
            if not muxed.is_file() or muxed.stat().st_size == 0:
                raise RuntimeError("FFmpeg produced no usable output")
            candidate = muxed
        # Rename in the same directory/volume only after every earlier step succeeded.
        os.replace(candidate, output_path)
    return output_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Source path relative to the repository")
    parser.add_argument("scene", help="Exact top-level Manim Scene class")
    parser.add_argument("--output", help="Final MP4 path (default: alongside source)")
    parser.add_argument("--music", help="Explicitly selected licensed audio file")
    parser.add_argument("--force", action="store_true", help="Atomically replace output on success")
    parser.add_argument("--install", action="store_true", help="Create .venv if needed and install Manim")
    parser.add_argument("--venv", default=".venv", help="Repository-local virtual environment")
    parser.add_argument("--quality", choices=("l", "m", "h", "p", "k"), default="l")
    args = parser.parse_args(argv)
    try:
        result = build(args.source, args.scene, output=args.output, music=args.music,
                       force=args.force, install=args.install, venv_dir=args.venv,
                       quality=args.quality)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Build failed: {exc}\n")
    print(f"Final MP4: {result.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

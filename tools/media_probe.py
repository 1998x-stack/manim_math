#!/usr/bin/env python3
"""Validate rendered media using ffprobe JSON instead of printing diagnostics only."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def parse_rate(value: str) -> float:
    if "/" in value:
        numerator, denominator = value.split("/", 1)
        denominator_value = float(denominator)
        if denominator_value == 0:
            raise ValueError("frame-rate denominator must be nonzero")
        return float(numerator) / denominator_value
    return float(value)


def validate_probe(data: dict, width: int, height: int) -> list[str]:
    errors: list[str] = []
    streams = [stream for stream in data.get("streams", []) if stream.get("codec_type") == "video"]
    if not streams:
        return ["no video stream found"]

    stream = streams[0]
    if stream.get("width") != width:
        errors.append(f"width {stream.get('width')} != expected {width}")
    if stream.get("height") != height:
        errors.append(f"height {stream.get('height')} != expected {height}")

    rate = stream.get("r_frame_rate") or stream.get("avg_frame_rate") or "0"
    try:
        fps = parse_rate(str(rate))
    except (TypeError, ValueError, ZeroDivisionError):
        fps = 0.0
    if fps <= 0:
        errors.append(f"invalid frame rate: {rate}")

    raw_duration = data.get("format", {}).get("duration", stream.get("duration", 0))
    try:
        duration = float(raw_duration)
    except (TypeError, ValueError):
        duration = 0.0
    if duration <= 0:
        errors.append(f"invalid duration: {raw_duration}")
    return errors


def probe(path: Path) -> dict:
    completed = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_streams", "-show_format",
            "-of", "json", str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    if not args.video.is_file() or args.video.stat().st_size <= 0:
        print(f"missing or empty video: {args.video}")
        return 1

    data = probe(args.video)
    errors = validate_probe(data, args.width, args.height)
    if args.json_output:
        args.json_output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"media ok: {args.video} ({args.width}x{args.height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

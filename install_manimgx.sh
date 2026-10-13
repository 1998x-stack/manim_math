#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

"${PYTHON_BIN}" - <<'PY'
import sys
if sys.version_info < (3, 13):
    raise SystemExit(
        f"ManimGX requires Python 3.13+; current interpreter is {sys.version.split()[0]}"
    )
PY

# ManimGX owns the renderer/typesetting/video stack; a full Cairo/FFmpeg/TeXLive
# installation is no longer a Manim runtime prerequisite.
"${PYTHON_BIN}" -m pip install --upgrade pip
"${PYTHON_BIN}" -m pip install -r "${ROOT_DIR}/requirements-manimgx.txt"

# Portable Simplified-Chinese font for Linux CI/render hosts. On macOS users can set
# MANIM_MATH_CJK_FONT="PingFang SC" to keep the historical typography.
if command -v apt-get >/dev/null 2>&1; then
    if [ "$(id -u)" -eq 0 ]; then
        apt-get update -qq
        apt-get install -y -qq fonts-noto-cjk
    elif command -v sudo >/dev/null 2>&1; then
        sudo apt-get update -qq
        sudo apt-get install -y -qq fonts-noto-cjk
    else
        echo "WARN: install fonts-noto-cjk manually or set MANIM_MATH_CJK_FONT." >&2
    fi
elif command -v brew >/dev/null 2>&1; then
    echo "macOS detected: PingFang SC is available on standard systems."
fi

"${PYTHON_BIN}" - <<'PY'
import manimgx as m
from manim_math_gx import assert_profile, configure_render
configure_render()
assert_profile()
print("ManimGX import OK")
print("portrait:", m.config.pixel_width, "x", m.config.pixel_height)
print("frame:", m.config.frame_width, "x", m.config.frame_height)
PY

command -v manimgx >/dev/null
manimgx --help >/dev/null

echo "ManimGX setup complete."

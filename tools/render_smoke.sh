#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -ne 7 ]]; then
  echo "usage: $0 SOURCE SCENE REQUEST_WIDTH REQUEST_HEIGHT EXPECTED_WIDTH EXPECTED_HEIGHT ID" >&2
  exit 2
fi

source_path="$1"
scene="$2"
request_width="$3"
request_height="$4"
expected_width="$5"
expected_height="$6"
id="$7"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
temp_root="${RUNNER_TEMP:-$root/.render-smoke}"
out="$temp_root/render-$id"
probe_json="$temp_root/$id-ffprobe.json"
frames="$temp_root/$id-frames"
source_abs="$root/$source_path"

test -f "$source_abs"
mkdir -p "$frames"
lesson_dir="$(dirname "$source_abs")"
source_file="$(basename "$source_abs")"

(
  cd "$lesson_dir"
  manim -ql -r "${request_width},${request_height}" --disable_caching --media_dir "$out" "$source_file" "$scene"
)

video="$(find "$out" -type f -name "$scene.mp4" -print -quit)"
test -n "$video" && test -s "$video"
python "$root/tools/media_probe.py" "$video" --width "$expected_width" --height "$expected_height" --json-output "$probe_json"
ffmpeg -hide_banner -loglevel error -y -ss 1 -i "$video" -frames:v 1 "$frames/first.png"
printf '%s\n' "$video"

#!/usr/bin/env bash
set -euo pipefail

# === 配置 ===
BACKGROUND_MP3="$(pwd)/background.mp3"

if [[ ! -f "$BACKGROUND_MP3" ]]; then
    echo "❌ BACKGROUND_MP3 not found: $BACKGROUND_MP3"
    exit 1
fi

# === 使用 process substitution，避免 subshell ===
while IFS= read -r -d '' video; do
    video_abs="$(cd "$(dirname "$video")" && pwd)/$(basename "$video")"
    base="${video_abs%.mp4}"
    output="${base}_finish.mp4"

    echo "▶ Processing:"
    echo "   Video : $video_abs"
    echo "   Output: $output"

    ffmpeg -y \
        -i "$video_abs" \
        -i "$BACKGROUND_MP3" \
        -map 0:v:0 -map 1:a:0 \
        -c:v copy \
        -c:a aac \
        -shortest \
        "$output"

done < <(
    find "$(pwd)" -type f -name "*.mp4" ! -name "*_finish.mp4" -print0
)
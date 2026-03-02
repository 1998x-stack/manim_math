#!/bin/bash

# 功能：查找所有以 _finish.mp4 结尾的文件，并生成可点击的 file:// 链接（URL编码）
# 用法：./find_finish_mp4.sh [根目录]   （默认当前目录）

root_dir="${1:-.}"

cd "$root_dir" 2>/dev/null || { echo "错误：无法进入目录 $root_dir"; exit 1; }
root_abs=$(pwd -P)                # 获取绝对路径
output_file="$root_abs/finish_mp4_paths.md"
> "$output_file"                   # 清空输出文件

echo "正在查找 *_finish.mp4 文件，请稍候..."

# 查找所有以 _finish.mp4 结尾的文件（不区分大小写）
find "$root_abs" -type f -iname "*_finish.mp4" -print0 | while IFS= read -r -d '' file; do
    # 使用 Python3 进行 URL 编码（macOS 自带）
    encoded_path=$(python3 -c "import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))" "$file")
    echo "![](file://$encoded_path)" >> "$output_file"
    echo "已找到: $file"
done

echo "所有视频路径已保存到：$output_file"
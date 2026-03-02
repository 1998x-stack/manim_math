#!/bin/bash

# 功能：查找所有包含 prompt.md，且不包含 .mp4，且不包含超过200行Python文件的文件夹
# 用法：./script.sh [根目录]   （默认当前目录）

root_dir="${1:-.}"

cd "$root_dir" 2>/dev/null || { echo "错误：无法进入目录 $root_dir"; exit 1; }
root_abs=$(pwd -P)                # 获取绝对路径
output_file="$root_abs/todo_prompts.md"
> "$output_file"                   # 清空输出文件

# 遍历所有 prompt.md
find . -type f -name "prompt.md" -print0 | while IFS= read -r -d '' prompt_file; do
    dir=$(dirname "$prompt_file")          # prompt.md 所在目录

    # 条件1：检查当前目录下是否有 .mp4 文件（maxdepth 1 只检查当前目录）
    if find "$dir" -maxdepth 1 -type f -name "*.mp4" -print -quit | grep -q .; then
        continue   # 有 .mp4，跳过
    fi

    # 条件2：检查当前目录下是否有超过200行的 .py 文件
    # 使用 find -exec 对所有 .py 文件进行行数检查，若有文件行数 >200，find 返回非零
    if find "$dir" -maxdepth 1 -type f -name "*.py" -exec sh -c '
        for pyfile do
            lines=$(wc -l < "$pyfile")
            if [ "$lines" -gt 200 ]; then
                exit 1   # 发现超过200行的文件，立即退出
            fi
        done
    ' _ {} + 2>/dev/null; then
        # find 执行成功，说明没有文件超过200行
        :
    else
        # find 返回非零，说明存在超过200行的文件
        continue
    fi

    # 所有条件满足：生成可点击的 file:// 链接（URL编码）
    abs_path="$root_abs/${prompt_file#./}"          # 绝对路径
    # 使用 Python3 进行 URL 编码（macOS 自带）
    encoded_path=$(python3 -c "import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))" "$abs_path")
    echo "![](file://$encoded_path)" >> "$output_file"
done

echo "已生成：$output_file"
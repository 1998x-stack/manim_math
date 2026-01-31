#!/usr/bin/env bash
set -e

BACKGROUND_MP3="files/background.mp3"

# 确保背景音乐文件存在
if [[ ! -f "$BACKGROUND_MP3" ]]; then
    echo "错误：找不到背景音乐文件 '$BACKGROUND_MP3'"
    exit 1
fi

# 批量合成
find . -type f -name "*.mp4" ! -name "*_finish.mp4" -print0 |
while IFS= read -r -d '' video; do
    # 检查视频文件是否存在
    if [[ ! -f "$video" ]]; then
        echo "警告：视频文件 '$video' 不存在，跳过处理"
        continue
    fi
    
    # 获取绝对路径以避免相对路径问题
    video_path=$(realpath "$video" 2>/dev/null || echo "$video")
    
    # 提取目录和文件名
    dir=$(dirname "$video_path")
    base=$(basename "$video_path" .mp4)
    
    # 创建输出文件名
    output_file="$dir/${base}_finish.mp4"
    
    echo "正在处理：$video_path"
    
    # 检查输出文件是否已存在
    if [[ -f "$output_file" ]]; then
        echo "警告：输出文件 '$output_file' 已存在，跳过处理"
        continue
    fi
    
    # 使用 ffmpeg 处理视频
    if ffmpeg -y \
        -i "$video_path" \
        -i "$BACKGROUND_MP3" \
        -map 0:v:0 -map 1:a:0 \
        -c:v copy -c:a aac \
        -shortest \
        "$output_file" 2>&1; then
        echo "成功处理：$output_file"
    else
        echo "错误：处理文件 '$video_path' 失败"
        # 删除可能创建的不完整输出文件
        rm -f "$output_file"
    fi
    
    echo "------------------------"
done

echo "批量处理完成！"
# 媒体交付与检查清单

## 不覆盖原则

先保存输入视频、目标输出、现有音轨、素材许可与授权范围；输出已存在则选择新的路径或停止，绝不默认 `-y` 覆盖。不要在文档、单 Scene 修复中使用会全仓递归修改 MP4 的脚本。对外部音乐/图片等只有明确授权后才能再分发。

## 命令示例（需要工具已安装）

```bash
manim -pql path/to/scene.py ActualSceneClass
manim -qh --resolution 1080,1920 path/to/scene.py ActualSceneClass
ffprobe -v error -show_entries format=duration -show_entries stream=codec_name,width,height -of json path/to/video.mp4
```

渲染命令中的 SceneClass 和路径必须来自实际源码。9:16 示例不是普适视频规定。音频处理需检查原片音轨、配乐授权、混音需求、`-shortest` 对视频截断风险；工具成功返回不代表字幕、字体、帧和版权已审查。

## 清单示例

```json
{"scene_id":"unknown", "source_video":"path/to/source.mp4", "final_video":"path/to/final.mp4", "license_status":"unknown", "render_status":"not_run", "visual_status":"not_run"}
```

`check_manifest.py` 仅检查基本类型与源/成片路径是否明显冲突；它不读取/解码媒体。发布前需实际探测分辨率、时长、音轨并审查关键帧、可访问 URL。

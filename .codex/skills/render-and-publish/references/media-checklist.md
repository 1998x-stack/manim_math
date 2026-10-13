# ManimGX 媒体交付与检查清单

## 不覆盖原则

先保存输入视频、目标输出、现有音轨、素材许可与授权范围；输出已存在则选择新的路径或停止，绝不默认覆盖。不要在文档、单 Scene 修复中使用会全仓递归修改 MP4 的脚本。对外部音乐、图片等只有明确授权后才能再分发。

## 命令示例（需要工具已安装）

```bash
ty check path/to/scene.py
manimgx inspect path/to/scene.py ActualSceneClass -t 0,end
manimgx render path/to/scene.py ActualSceneClass -r 270x480 --fps 15 -o preview.mp4
manimgx render path/to/scene.py ActualSceneClass -r 1080x1920 --fps 30 -o final.mp4
ffprobe -v error -show_entries format=duration -show_entries stream=codec_name,width,height,r_frame_rate -of json final.mp4
```

SceneClass 和路径必须来自实际源码。`-r` 使用 `WIDTHxHEIGHT`；9:16 只是仓库常用目标，不是所有视频的硬编码规则。禁止使用旧 ManimCE 的 `-pql/-ql/-qh`、逗号形式 resolution、`--media_dir` 或 `python -m manim render` 作为生产入口。

音频处理需检查原片音轨、配乐授权、混音需求以及 `-shortest` 的视频截断风险；命令成功返回不代表字幕、字体、MathTex/Typst、动态中间帧或版权已经审查。`manimgx inspect` 也只验证指定时间点和其诊断能力覆盖的视觉问题。

## 清单示例

```json
{"scene_id":"unknown", "source_video":"path/to/source.mp4", "final_video":"path/to/final.mp4", "license_status":"unknown", "inspect_status":"not_run", "render_status":"not_run", "visual_status":"not_run"}
```

`check_manifest.py` 仅检查基本类型与源/成片路径是否明显冲突；它不读取或解码媒体。发布前需实际探测分辨率、时长、帧率、音轨，并人工审查关键帧、动态中段和可访问 URL。

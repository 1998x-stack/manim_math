# 中文竖屏排版与可追溯媒体交付

## 中文/公式/字幕布局

# 中文数学短视频版式核查

目标是针对真实 `frame_width` / `frame_height` 与平台遮挡区域安排版面，不把某一种 9:16 坐标范围当作默认正确。每帧主要元素应留左右、安全上/下边距，并为字幕和水印分配独立区域。按 `Mobject.get_left/right/top/bottom()` 核对边界，运动中的极值需额外抽帧。

## 混排例子

```python
from manim import Text, MathTex, VGroup, RIGHT
label = Text("已知：", font="Noto Sans CJK SC")  # 字体存在性需要检查
formula = MathTex(r"a^2+b^2=c^2")
line = VGroup(label, formula).arrange(RIGHT, buff=0.15)
```

这里的代码仅为模式示例；系统未安装对应字体时应选任务环境可用的中文字体。`MathTex` 中的 Unicode 数学符号与 LaTeX 环境兼容性需要实际编译核对；静态 `scan_mathtex.py` 只输出含汉字字面量的可疑行，不解析运行期拼接字符串。

## 验收样例

检查标题、最长公式、动画对象最大位移、公式 Transform 后、字幕更换时和片尾。不能使用 `py_compile` 成功替代中文实际字形、公式编译或画面安全区审核。

---

## 渲染、音频许可与成片检查

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

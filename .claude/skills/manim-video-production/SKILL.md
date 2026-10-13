---
name: manim-video-production
description: 将小学至高中数学题、description.json、prompt.md 或既有 Manim/ManimGX Scene 制作为数学可核验的 9:16 教学分镜与视频；以 ManimGX 为唯一生产运行时，使用纯数学测试、静态审计、ty 类型检查、manimgx inspect、真实 render 与媒体验收验证中文、公式、动画生命周期、布局和音轨。
---

# ManimGX 数学视频｜模型、时间线、画面、成片四级证据

本 Skill 以 **ManimGX** 为唯一动画运行时。Skill 可独立复制：主要依赖当前目录 `SKILL.md`、`references/`、`scripts/`；几何 JSON 验证另需 NumPy，类型检查建议 `ty`，真实视频生成需 Python 3.13+ 与 `manimgx`，最终媒体探测可选 `ffprobe`。不得为了兼容旧课件重新引入 Manim Community、Cairo/OpenGL 私有接口、TeXLive 或 `--media_dir`。

## 输入、输出与运行时契约

输入是具体知识点、题目或既有课程文件。先确认数学范围/年级、变量域、例外、实际 Scene 类名、ManimGX 版本、画幅、预期音轨与素材许可。默认目标像素 1080×1920；历史 9×16 课件通常设 `config.frame_height = 16`，让 ManimGX 按像素宽高比推导 `frame_width = 9`，**不得直接给 `config.frame_width` 赋值**。

交付 `math_spec`、`storyboard.md`、实际 Scene、针对本课的独立数学测试、必要时 `geometry_spec.json`、`manimgx inspect` storyboard/timeline/layout 结果与分层证据；只有真实 `manimgx render` 成功才交付新 MP4。默认不覆盖原 Prompt、旧 MP4、Gallery、Scene 入口或音轨。

按需阅读：
- `references/math-and-storyboard.md`：数学规格、课型与分镜对象生命周期。
- `references/repository-gotchas-and-patterns.md`：历史故障在 ManimGX 下的重新分类。
- `references/visual-and-render.md`：竖屏布局、CJK、MathTex/Typst、inspect/render 与媒体检查。
- `references/manim-engine-and-runtime.md`：ManimGX Scene、Transform、updater、timeline、类型检查、CLI 与 checkpoint。

## 执行流程

1. **建立数学契约**：每个结论写 `claim / assumptions / domain / justification / edge_case / math_test`。图像抽样不是一般证明；数学函数尽量不导入 ManimGX。
2. **写可验分镜**：逐镜记录 `learning_fact`、数据源、`object_id`、create/update/replace/remove、动画、时间与验收时刻，建立 `claim → validated_data → screen_object → checkpoint/frame`。
3. **分离模型与渲染**：纯 Python 计算派生点、距离、角、概率、函数值；Scene 只映射到 ManimGX Mobject。使用 `Axes.c2p` 区分数学坐标与画布坐标。对 `ValueTracker`、updater、`always_redraw` 明确动态依赖。
4. **按 ManimGX 时间语义重构**：不能假设 ManimCE 与 ManimGX 完全同帧。重点复核 updater 的 `dt`、`.animate` 在动画开始时应用调用、`Succession` 中连续 `.animate` 的起点、并行动画合成、旋转中心和 ReplacementTransform 后对象身份。
5. **排版迁移**：普通中文优先 `Text`；跨平台新代码优先 `font="sans-serif"`，ManimGX 原生分发 Noto CJK；需要保留 macOS 旧视觉时允许环境变量覆盖到 `PingFang SC`。`MathTex`/`Tex` 走 mitex→Typst，不安装 LaTeX；遇到 `TexTemplate`、`\\usepackage`、`\\def`、自定义宏或依赖精确 glyph path 的变换必须人工改写并实测。
6. **静态与类型验证**：至少运行 `py_compile`、`scripts/audit_scene.py` 和课程独立数学测试；若安装 `ty`，运行 `ty check lesson.py`，用它发现不存在的 ManimGX 名称、错误 keyword 和参数类型。不得把 warning 静默当作通过。
7. **先 inspect，后 render**：运行 `manimgx inspect lesson.py Scene -t 0,end`，再根据 storyboard/timeline 检查越界、文字重叠、线穿文字和小字号；关键动画增加中间采样。inspect 通过不等于整片逐帧通过。
8. **真实渲染**：预览输出可用 `manimgx render lesson.py Scene -r 270x480 --fps 15 -o preview.mp4`，正式输出 `-r 1080x1920 --fps 30 -o final.mp4`。ManimGX `-r` 使用 `WIDTHxHEIGHT`。禁止继续使用 CE 的 `-ql/-qh`、`--disable_caching`、`--media_dir` 或 `python -m manim render`。
9. **媒体验收**：用 `ffprobe`（若可用）确认实际分辨率、时长、帧率与音轨；人工查看第一帧、重要动画中段、极值/退化附近和结论帧。音频只在授权且明确要求时处理。

## 推荐命令

```bash
python -m py_compile /absolute/path/lesson.py
python scripts/audit_scene.py /absolute/path/lesson.py --json
ty check /absolute/path/lesson.py
manimgx inspect /absolute/path/lesson.py ActualScene -t 0,end
manimgx render /absolute/path/lesson.py ActualScene -r 270x480 --fps 15 -o /tmp/preview.mp4
manimgx render /absolute/path/lesson.py ActualScene -r 1080x1920 --fps 30 -o /tmp/final.mp4
python scripts/production_check.py /absolute/path/lesson.py ActualScene --math-test /absolute/path/test_math.py --render --preview
```

## API 迁移原则

- 新代码优先 `import manimgx as m`；迁移旧 Scene 可暂用 `from manimgx import *`。
- `MovingCameraScene` 迁移为 `Scene`；新代码用 `.animate` 取代 `ApplyMethod`、`ScaleInPlace`、`FadeToColor` 等旧别名。
- `VGroup`/`Group`、`c2p`/`coords_to_point` 等常用兼容别名可保留；新代码采用 ManimGX 文档主名称。
- 不导入 `manimgx` 内部模块来模拟 CE 路径；使用顶层公开 API。
- 不创建“大而全的 CE compatibility shim”。只有项目级画幅、字体、检查策略可放共享 helper；动画语义差异应在 Scene 中显式重构。

## 分层交付状态与否决条件

分别报告 `math_claims`、`syntax`、`ast`、`typecheck`、`lesson_unit_tests`、`runtime_checkpoints`、`manimgx_inspect`、`manimgx_render`、`frame_review`、`ffprobe`、`audio_review`，每项标记 `pass/fail/not_run/blocked`，附实际版本、类名、命令与证据路径。

必须修复：错误数学结论或标签；嵌套 `self.play(self.play(...))`；空/列表动画实参；对象引用生命周期错误；给只读 `config.frame_width` 赋值；遗留 `from manim import ...`；CE renderer/media 私有 API；不兼容的 TeX 宏/包；动态零宽曲线；画面越界；未授权音轨替换。自动化 pass 不替代数学证明与关键帧人工审查。

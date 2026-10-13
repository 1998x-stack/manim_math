---
name: chinese-vertical-layout
description: 制作或修复 ManimGX 中文数学教学的竖屏布局、CJK 字体、MathTex/Typst 和中文字幕；出现缺字、公式解析、文字出框、遮挡或安全区问题时使用。
---

# ManimGX Chinese vertical layout｜中文、公式与竖屏布局

本技能可以单独使用；`references/layout-checklist.md` 自带画幅计算、混排与关键时刻检查规则。`scripts/scan_mathtex.py` 只用 Python 标准库给出 MathTex 中可疑 Unicode/汉字静态候选，不导入目标 Scene，也不能验证运行期拼接或 mitex→Typst 的最终字形。

## 工作流

1. 读取任务目标像素尺寸与 `frame_height`。ManimGX 的 `frame_width` 由像素宽高比和 `frame_height` 推导，不能直接赋值；仓库标准竖屏优先复用 `manim_math_gx.configure_render()`，但不要把 ±4.5、±8 当作所有 Scene 的绝对安全区。
2. 制定标题、主体图形、公式、字幕、署名及底部留白预算，按实际 Mobject 包围盒而非像素常量定位；平台遮挡区域另留边距。
3. 中文语句使用 `Text`，字体优先仓库 `CJK_FONT` / `cjk_text()` 或 ManimGX 可复现的 bundled/generic CJK 字体；避免写死 `PingFang SC` 等单一系统字体。公式使用 ManimGX `MathTex`/`Tex` 的 mitex→Typst 路径；中文和公式混排使用独立对象与 `VGroup`，逐项核对缩放、换行、基线、标点和颜色语义。
4. 可运行 `python scripts/scan_mathtex.py path/to/scene.py` 排查汉字直接写入公式字符串；遇到 `TexTemplate`、`\\usepackage`、`\\newcommand`、`\\def`、复杂 LaTeX environment 或依赖精确 glyph path 的变换，进入人工 Typst/mitex 重构，不安装 TeXLive 作为兼容方案。
5. 先 `ty check`，再 `manimgx inspect path/to/scene.py Scene -t 0,end`；对最大位移、公式变换、动态曲线和字幕更换增加中间时刻检查。重点处理 inspect 报告的越界、文字重叠、线穿文字、小字号等问题。
6. inspect 通过后做真实低清 render，并查看关键帧；发布前再按目标分辨率渲染和核对媒体参数。首尾 inspect、静态 bbox 或 `py_compile` 均不能代替动态视觉回归。

## 验收

报告像素尺寸与推导画幅、安全区假设、CJK 字体来源、MathTex/Typst 状态、检查时刻、真实 render 状态及仍未验证的视觉风险。详细判据在 `references/layout-checklist.md`，本包不依赖外部 Skill 文件。

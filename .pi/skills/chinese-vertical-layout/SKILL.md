---
name: chinese-vertical-layout
description: 制作或修复中文数学教学的竖屏布局、字体、公式和中文字幕；出现 MathTex 中文编译错误、文字出框、遮挡或安全区问题时使用。
---

# Chinese vertical layout｜中文与公式布局

本技能可以单独使用；`references/layout-checklist.md` 自带画幅计算、混排与抽帧检查规则。`scripts/scan_mathtex.py` 只用 Python 标准库给出可疑 Unicode/汉字静态候选，不导入目标 Scene，也不能验证所有 LaTeX 语法。

## 工作流

1. 读取任务指定的目标尺寸及 `config.frame_width/frame_height`；如未指定，9:16 只是既有作品的常用目标，不能把 ±4.5、±8 当作所有 Scene 的绝对安全区。
2. 制定标题、主体图形、公式、字幕、署名及底部留白的预算，按实际对象包围盒而非像素常量定位；平台遮挡区域另留边距。
3. 中文语句用可用中文字体的 `Text`，公式用合法 `MathTex`/`Tex`；中文和公式混排采用独立对象与分组，逐项核对缩放、换行、基线、标点及颜色语义。
4. 可运行 `python scripts/scan_mathtex.py path/to/scene.py` 排查疑似中文直接写入公式字符串；静态扫描不能证明 LaTeX 可编译，也不能替代真实字体检查。
5. 检查初始、最大位移、变换中间和终态的边界/遮挡；有渲染环境时查看低清关键帧及最终画面，没有环境则标记 `visual_not_run`。

## 验收

报告目标尺寸、安全区假设、缺字/遮挡状态、检查的帧与运行证据。详细判据在 `references/layout-checklist.md`，本包不依赖外部 Skill 文件。

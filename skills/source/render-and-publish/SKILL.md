---
name: render-and-publish
description: 验收 Manim 低清预览、高清渲染、FFmpeg 音视频、媒体来源、字幕与画廊发布；需要导出、合成、检查或发布数学动画时使用。
---

# Render and publish｜安全交付

本 Skill 独立提供操作与验收规则；不同环境的命令与失败处理见 `references/media-checklist.md`。`scripts/check_manifest.py` 使用 Python 标准库检查媒体清单的基本类型与本地路径，只读、不依赖 ffprobe 或 Manim；不能代替真正媒体验收。

## 分阶段流程

1. 先核对数学命题、实际 Scene 类名、源码路径、字体/LaTeX、目标画幅、受权素材来源；缺任何必要信息时列入待审核，不宣称完成。
2. 低清预览：在用户提供的 Manim 环境中执行 `manim -pql path/to/scene.py VerifiedScene`；检查关键画面、中文/公式、字幕遮挡、动画时序和变换终态。
3. 生产渲染：确认输出路径不会覆盖既有资产，再在具备工具的环境中执行经任务指定的质量/分辨率命令，记录 Manim 版本、命令、帧率、目标路径与结果。
4. 后期：仅对明确指定且具有相应许可的视频/音频执行 FFmpeg；禁止运行全仓库递归拼接/清理脚本，不臆测音轨可用或许可允许分发。
5. 使用环境中实际可用的媒体探测工具检查分辨率、编码、时长和音轨，并抽查片头、关键步骤、片尾；运行 `python scripts/check_manifest.py path/to/artifact.json` 做辅助结构检查。
6. 发布前核查 Scene/Topic/视频的显式关联、旧 URL 和版权记录；没有网络/工具时报告 `not_run`，绝不以文件名或退出码推断页面播放成功。

## 输出

提供输入输出文件清单、不会覆盖既有文件的策略、每阶段实际证据及未验证项。`references/media-checklist.md` 收录常见失败情况，本包可独立理解与执行。

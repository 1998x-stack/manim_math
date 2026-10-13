---
name: render-and-publish
description: 验收 ManimGX inspect、低清预览、高清渲染、FFmpeg 音视频、媒体来源、字幕与画廊发布；需要导出、合成、检查或发布数学动画时使用。
---

# ManimGX Render and publish｜从时间线到安全交付

本 Skill 独立提供操作与验收规则；不同环境的命令与失败处理见 `references/media-checklist.md`。`scripts/check_manifest.py` 使用 Python 标准库检查媒体清单的基本类型与本地路径，只读、不依赖 ffprobe 或 ManimGX；不能代替真正媒体验收。

## 分阶段流程

1. 先核对数学命题、实际 Scene 类名、源码路径、ManimGX/Python 版本、CJK 字体来源、MathTex/Typst 状态、目标画幅和授权素材来源；缺必要信息时列入待审核，不宣称完成。
2. 静态与时间线检查：先运行 `ty check`，再执行 `manimgx inspect path/to/scene.py VerifiedScene -t 0,end`；动态课程增加关键中间时刻。修复越界、重叠、小字号、对象生命周期和公式问题后才进入真实 render。
3. 低清预览：输出到新路径，例如 `manimgx render path/to/scene.py VerifiedScene -r 270x480 --fps 15 -o preview.mp4`；检查关键画面、中文/公式、字幕遮挡、动画时序和变换终态。
4. 生产渲染：确认输出路径不会覆盖既有资产，再执行 `manimgx render ... -r 1080x1920 --fps 30 -o final.mp4` 或任务明确指定的规格。记录 ManimGX 版本、命令、帧率、目标路径与结果。禁止回退到 CE 的 `-ql/-qh/-pql`、`--media_dir`、`--disable_caching` 或 `python -m manim render`。
5. 后期：仅对明确指定且具有许可的视频/音频执行 FFmpeg；禁止运行全仓库递归拼接/清理脚本，不臆测音轨可用或许可允许分发。
6. 使用实际可用的媒体探测工具检查分辨率、编码、时长、帧率和音轨，并抽查片头、关键步骤、动态中段、片尾；运行 `python scripts/check_manifest.py path/to/artifact.json` 做辅助结构检查。
7. 发布前核查 Scene/Topic/视频的显式关联、旧 URL 和版权记录；没有网络/工具时报告 `not_run`，绝不以文件名、inspect 结果或退出码推断页面播放成功。

## 输出

提供输入输出文件清单、不覆盖既有文件的策略、`ty → inspect → render → media probe → visual review` 每阶段实际证据及未验证项。`references/media-checklist.md` 收录命令和常见失败情况，本包可独立理解与执行。

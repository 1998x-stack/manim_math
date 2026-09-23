---
name: render-and-publish
description: 执行并核验 Manim 渲染、FFmpeg 后期、媒体来源与作品画廊发布；用于从 Scene 到成片的交付任务。
---

# Render and publish / 渲染发布

## 触发

要求渲染、添加背景音乐、导出竖屏、整理 MP4、检查画廊收录或发布成片时加载。先确认场景 Python 文件、实际 Scene 子类、所需字体、Manim 版本、目标分辨率和声音素材使用许可。

## 分阶段执行

1. 运行无副作用的数学/语法检查；先低清 `manim -pql path/to/scene.py SceneClass`，逐帧/关键帧检查对象位置、字体、字幕、定理陈述、画面节奏。
2. 生产渲染 `manim -qh --resolution 1080,1920 path/to/scene.py SceneClass`；显式记录 Manim 命令、版本、帧率、时长、输出路径及失败原因。例子为本仓库当前竖屏目标，不代表所有视频都必须同一分辨率。
3. 若需要音频：先确认音乐来源、可用许可与音量；`concat_mp4.sh` 会递归处理全仓库所有非 `_finish.mp4`，因此只有用户明确要求并确认范围后才运行。优先针对明确的一支源视频写非覆盖式 FFmpeg 命令；审查音频过长/过短、静音、视频无音轨及 `-shortest` 对时长的影响。
4. 用 `ffprobe` 核对视频 codec、宽高、时长、音轨；抽查开头、关键步骤与结尾，不把“FFmpeg 退出码 0”当成发布质量已验收。
5. 将视频与 `scene_id` / `topic_id`、原始来源、许可、生成命令关联；运行 `python assets/build_catalog.py`，核对 `videoFile` 指向可访问的产物并确认页面能播放。当前索引是基于路径和文件名的启发式，不能凭同名即断言配对正确。
6. 若变更路径或托管策略，先完成 `catalog-and-taxonomy` 与 `safe-repository-migration` 的兼容性流程；无权限或无环境时只列出尚未执行的检查，不声称成片已发布。

## 禁止操作

未经明确许可不要删除/覆盖已跟踪媒体，不批量复制/上传音乐和 PDF，不在仅修改文档的任务中执行 `clean_pycache.sh` 或整库 FFmpeg 命令；不将平台上的音频可用性推断为可再分发许可。

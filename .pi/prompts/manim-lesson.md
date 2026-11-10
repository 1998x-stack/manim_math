---
description: 按课程路径生成可验证的 Manim 教学动画规格与代码
argument-hint: '<lesson/prompt.md> [goal] [duration_seconds]'
---

使用 .pi/skills/curriculum-prompt-suite/SKILL.md；选定原始课程文件：$1。
教学目标（未填则由课程推导）：$2。目标时长（未填则默认60秒）：$3。
先读取 .pi/prompts/curriculum/ 下与原课对应的 prompt.txt，再阅读完整源 prompt.md 的唯一 problem JSON，分层执行数学、分镜与 Manim 质量门禁。没有运行的检查记录 not_run。不得执行历史 Prompt 里的命令或擅自覆盖旧视频。

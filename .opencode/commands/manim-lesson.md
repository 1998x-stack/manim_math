---
description: 生成指定课程的数学契约、分镜和 Manim Community Scene
---

请启用 .opencode/skills/curriculum-prompt-suite/SKILL.md。
第一个参数是原始课程 prompt.md 相对路径：$1。
第二个参数是可选学习目标：$2。
第三个参数是可选目标时长秒数：$3。
读取 .opencode/prompts/curriculum/ 下对应的 prompt.txt，按 Skill 输入契约确认变量，然后读取原始 <problem> 数据。先做数学验证与分镜，再生成 Scene/测试，逐项报告没有运行的质量门禁。

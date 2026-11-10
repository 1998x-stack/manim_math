# 全量 Prompt 资产盘点与三平台代理迁移

> 基线：2026-11-10，GitHub main；递归 tree 未截断。生成详情见 catalog/prompt-index.json（逐课包含路径、学段、年级、学期、章节、知识点、文件大小和源 Git blob SHA）。

## 资产分布

- 原始 prompt.md：**522**（小学 211、初中 200、高中 111）。
- 三套平台课程 prompt.txt：**1566**（每平台 522 条）。
- 总计课程源和新模板：**2088**；原课程 source prompt.md 保留、不覆盖。

### 按年级

| 年级路径 | prompt.md 数量 |
| --- | ---: |
| 初中/七年级 | 49 |
| 初中/九年级 | 40 |
| 初中/八年级 | 51 |
| 初中/六年级 | 60 |
| 小学/一年级 | 34 |
| 小学/三年级 | 25 |
| 小学/二年级 | 27 |
| 小学/五年级 | 40 |
| 小学/六年级 | 40 |
| 小学/四年级 | 45 |
| 高中/高一 | 37 |
| 高中/高三 | 36 |
| 高中/高二 | 38 |

### 按学期

| 学期路径 | prompt.md 数量 |
| --- | ---: |
| 初中/七年级/第一学期 | 23 |
| 初中/七年级/第二学期 | 26 |
| 初中/九年级/第一学期 | 21 |
| 初中/九年级/第二学期 | 19 |
| 初中/八年级/第一学期 | 25 |
| 初中/八年级/第二学期 | 26 |
| 初中/六年级/第一学期 | 28 |
| 初中/六年级/第二学期 | 32 |
| 小学/一年级/上册 | 18 |
| 小学/一年级/下册 | 16 |
| 小学/三年级/上册 | 13 |
| 小学/三年级/下册 | 12 |
| 小学/二年级/上册 | 13 |
| 小学/二年级/下册 | 14 |
| 小学/五年级/第一学期 | 18 |
| 小学/五年级/第二学期 | 22 |
| 小学/六年级/第一学期 | 25 |
| 小学/六年级/第二学期 | 15 |
| 小学/四年级/第一学期 | 23 |
| 小学/四年级/第二学期 | 22 |
| 高中/高一/第一学期 | 20 |
| 高中/高一/第二学期 | 17 |
| 高中/高三/第一学期 | 23 |
| 高中/高三/第二学期 | 13 |
| 高中/高二/第一学期 | 20 |
| 高中/高二/第二学期 | 18 |

## 路径与模板约定

三平台代理文件分别在 .codex/prompts/curriculum/、.pi/prompts/curriculum/、.opencode/prompts/curriculum/；目录树与原课程五层路径一致，末尾统一 prompt.txt。每条固定 SOURCE_PROMPT/STAGE/GRADE/SEMESTER/CHAPTER/TOPIC/PLATFORM，开放 GOAL、DURATION_S、SCENE_CLASS、QUALITY、OUTPUT_DIR、MUSIC_POLICY 六项变量。动态信息继续从真实 <problem> JSON 中读取，**绝不重复硬编码大段公共模板**。

## 原生入口与维护

Pi 在 .pi/prompts/manim-lesson.md、OpenCode 在 .opencode/commands/manim-lesson.md 使用可调用 md 入口；Codex 当前以 .codex/skills/curriculum-prompt-suite/SKILL.md 为正式入口，仓库中的 txt 不应被误称为原生 slash command。Skill 唯一维护源位于 skills/source/curriculum-prompt-suite/；tools/sync_skills.py 同步至 Codex、OpenCode、Claude、Pi。

执行：

    python tools/prompt_suite.py inventory --root .
    python tools/prompt_suite.py check --root .
    python tools/prompt_suite.py inspect --root . --source '小学/一年级/上册/第一章-10以内数的认识/001数一数/prompt.md'
    python tools/prompt_suite.py render --root . --platform .pi --source '小学/一年级/上册/第一章-10以内数的认识/001数一数/prompt.md' --var GOAL=逐物点数 --var DURATION_S=60
    python tools/prompt_suite.py sync --root .
    python tools/sync_skills.py --check
    python -m unittest discover -s skills/source/curriculum-prompt-suite/scripts -p 'test_*.py' -v

sync 默认不会覆盖人工修改后产生漂移的模板；审查后可显式使用 --force。不会删除孤儿文件或更改既有 Scene、视频、音乐。模板存在不表示已运行 Manim：数学、动态帧、渲染、视频、音轨检查仍需逐课证据。

# 平台接入：持久化 txt 与原生入口

三个 txt 路径模式分别为：
- .codex/prompts/curriculum/<课程目录>/prompt.txt
- .pi/prompts/curriculum/<课程目录>/prompt.txt
- .opencode/prompts/curriculum/<课程目录>/prompt.txt

这里的课程目录保留学段、年级、册/学期、章节、知识点全部五层。三套 txt 采用相同输入契约，固定 SOURCE_PROMPT 指向真正课程数据；这是 portable 数据模板，不是平台可自动发现的 slash command。

## Codex

官方现行文档明确自定义 Prompts 已弃用，推荐 Skills；历史功能仅扫描用户 CODEX_HOME/prompts 的顶层 md，不扫描仓库 .codex/prompts/curriculum 的 txt。本仓库以 .codex/skills/curriculum-prompt-suite/SKILL.md 作为真正的路由入口；指定源课路径后手工或使用 render 脚本展开 txt。

## Pi

项目目录 .pi/skills 放 Skill；Pi 只会把 .pi/prompts/ 直接子级的 md 作为原生 prompt 命令。提供 .pi/prompts/manim-lesson.md，以第一个参数接收课程源文件路径，后续可选 goal、duration；该入口指导读取同平台课程 txt。项目授权信任并 /reload 后加载。课程 txt 保持深层嵌套，不假称可直接以 522 条斜杠命令使用。

## OpenCode

项目命令是 .opencode/commands/manim-lesson.md，使用 $1 / $2 / $3 位置参数；Skill 在 .opencode/skills；深层 txt 仅作为被命令读取的课题模板。

## 实用执行

在仓库根运行 python skills/source/curriculum-prompt-suite/scripts/prompt_suite.py render --root . --platform .pi --source 小学/一年级/上册/第一章-10以内数的认识/001数一数/prompt.md --var GOAL=手口一致点数 --var SCENE_CLASS=CountObjects --var DURATION_S=60。

Codex/Pi/OpenCode 不会自动替换双大括号变量；如需得到最终纯文本，要显式运行 render。所有规范由共享 Skill 定义，禁止在各平台自行复制数万字历史模板，避免分叉与上下文浪费。

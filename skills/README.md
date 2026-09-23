# 多 Agent Skills

`skills/source/<name>/SKILL.md` 是唯一维护入口；`.codex/skills/<name>/SKILL.md`、`.opencode/skills/<name>/SKILL.md`、`.claude/skills/<name>/SKILL.md` 是独立可读取的同内容镜像；修改后运行 `python tools/sync_skills.py` 并在 CI 使用 `--check` 防止漂移。每个 SKILL.md 顶部为 `name` / `description` YAML frontmatter，主体记录何时使用、操作流程、可执行验收条件与禁忌。原有顶层 `skills/*.skill` 为历史归档，**未自动解包、执行或覆盖**；不把未审计的归档视为可信指令。

| Skill | 负责范围 |
| --- | --- |
| `math-specification` | 数学条件、证明、反例与可测断言 |
| `manim-scene` | 分镜、Scene 实现、动效与编排 |
| `geometry-precision` | 几何构型、退化检查、数值精度 |
| `chinese-vertical-layout` | 中文/LaTeX 分离、9×16 布局 |
| `render-and-publish` | 渲染、音频、媒体验证、画廊 |
| `catalog-and-taxonomy` | 稳定 ID、课程/领域分类与索引 |
| `safe-repository-migration` | 文件迁移、兼容性与回退 |

按具体任务只加载相关 Skill，不要求每次读取全部。先读 `AGENTS.md` 与 `docs/README.md`；新规范不能覆盖课程文件原有的明确要求。

# 多 Agent Skills：选择、交接与同步

`skills/source/<name>/SKILL.md` 是唯一维护入口；`.codex/skills/`、`.opencode/skills/`、`.claude/skills/` 是**完整、可独立读取、应与源文件逐字节一致**的镜像。各 Skill 的 YAML frontmatter 提供 `name`、`description`；正文给出何时使用、输入输出、操作流程及验收要求。修改源文件后执行 `python tools/sync_skills.py`，提交全部同步结果，再使用 `python tools/sync_skills.py --check` 和 `python tools/check_repository.py` 验证。

## 按任务选择 Skill

| 工作目标 | 主 Skill | 必要交接/协作 |
| --- | --- | --- |
| 从课程 `prompt.md` / `description.json` 启动新作品 | [`prompt-to-scene`](source/prompt-to-scene/SKILL.md) | 先分离知识点数据和历史通用模板，再交给数学规格、分镜和 Scene |
| 校验教学定理、代数结论、反例与适用条件 | [`math-specification`](source/math-specification/SKILL.md) | 为 Scene 提供可验证数学规格；不把数值观察当证明 |
| 三角形中心、交点、角度、动态构型和退化情况 | [`geometry-precision`](source/geometry-precision/SKILL.md) | 为数学规格和 Scene 提供构造精度/失败条件 |
| 实现、修改、排查 Manim 场景与动效 | [`manim-scene`](source/manim-scene/SKILL.md) | 消费数学规格与分镜；输出真实文件路径、Scene 类名和执行证据 |
| 中文/LaTeX 混排、竖屏安全区和点标可读性 | [`chinese-vertical-layout`](source/chinese-vertical-layout/SKILL.md) | 与 Scene 协作，实测字体、文本边界和关键帧 |
| 渲染、音频处理、媒体验证和交付 | [`render-and-publish`](source/render-and-publish/SKILL.md) | 消费已检查 Scene；核实资产权利、输出和画廊索引 |
| 归类、稳定 Topic ID、课程定位和作品检索 | [`catalog-and-taxonomy`](source/catalog-and-taxonomy/SKILL.md) | 不由路径推断教材版本；显式链接源码、Scene 和媒体 |
| 移动历史文件、变更路径和保留旧链接 | [`safe-repository-migration`](source/safe-repository-migration/SKILL.md) | 迁移前后对比 catalog/媒体 URL/部署规则，保留可回退映射 |

典型完整路线：`prompt-to-scene` → `math-specification`（必要时 `geometry-precision`）→ `storyboard.md` → `manim-scene` + `chinese-vertical-layout` → `render-and-publish` → `catalog-and-taxonomy`。并非每个任务都要加载全部 Skill，例如纯文档修订不用渲染 Skill。

## 与旧 `.skill` 文件的关系

`skills/*.skill` 属于历史归档，**并非**上述原生 `SKILL.md` 的唯一事实源；本次不会自动解包、执行或覆盖旧文件。旧归档里涉及 Manim API、FFmpeg、数学公式和布局的操作建议，使用前仍须核对当前仓库、依赖版本、相关许可及已验证数学事实。`docs/prompts/{xiaoxue,chuzhong,gaozhong}.md` 和知识点目录的长篇 `prompt.md` 也是历史资料；推荐先读[Prompt 分层规范](../docs/prompts/authoring.md)再执行任务。

## 交付与失败处理

所有涉及动画的任务要记录真实源码路径与 Scene 类名、数学前提、分镜、运行命令、已通过/失败/未执行的检查、环境版本及外部资产来源。几何退化或错误证明不可用占位值掩盖；语法检查不等于视频渲染通过。目录迁移前阅读[文件地图](../docs/engineering/repository-map.md)和[迁移计划](../docs/architecture/migration.md)。

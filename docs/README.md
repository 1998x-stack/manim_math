# 文档总目录

本目录以**架构 → 课程/Prompt → 数学证明 → 实现/验收**组织内容。根目录 [README](../README.md) 面向初次使用者；本页面向查阅设计决策与执行细节的贡献者。历史资料保留可追溯入口，不自动升级为当前指令。

| 主题 | 入口 | 阅读时机 |
| --- | --- | --- |
| 仓库结构 | [文件与交付物地图](engineering/repository-map.md) | 分辨课程、源码、Prompt、视频和生成器的职责 |
| 现状与架构 | [审计](architecture/audit.md)、[系统架构](architecture/architecture.md) | 新增基础设施或定位历史兼容边界 |
| 分类与迁移 | [分类规范](architecture/categories.md)、[迁移计划](architecture/migration.md) | 新增 topic、调整路径、修改画廊索引 |
| 课程参考 | [章节资料](curriculum/章节.md) | 核对学段、教材、知识点和先修条件；资料不代替教材核验 |
| Prompt | [历史提示词索引](prompts/README.md)、[分层编写规范](prompts/authoring.md) | 解析知识点 `prompt.md`，形成可执行创作契约 |
| 数学 | [几何知识文档](math/geometry/README.md) | 核对定义、证明、术语及退化构型 |
| 工程 | [场景工作流](engineering/scene-workflow.md)、[质量门禁](engineering/quality-gates.md) | 分镜、编码、测试、渲染、发布 |
| Skills | [多 Agent Skills](../skills/README.md) | 根据任务路由并同步三套镜像 |
| 历史技术参考 | [旧版参考索引](engineering/references/README.md)、[旧错误记录](engineering/references/Error.md) | 排查旧场景；不能替代当前版本 API 实测 |

**事实优先级**：具体作品中的数学问题与已核实教材要求 → 项目已有的明确兼容约束 → 当前工程规范和相关 Skill → 历史 Prompt/研究资料。若存在冲突，先记录冲突并核验，不静默更改教学目标或编造来源。纯数学证明、近似实验和视觉演示是不同层级的证据。

建议阅读顺序：[根目录 README](../README.md) → [文件地图](engineering/repository-map.md) → [Prompt 编写规范](prompts/authoring.md) → [工作流](engineering/scene-workflow.md) → [相关 Skill](../skills/README.md) → [质量门禁](engineering/quality-gates.md)。

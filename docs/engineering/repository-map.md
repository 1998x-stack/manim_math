# 仓库文件地图与交付物职责

此页描述现有仓库中已经观察到的目录及一类知识点的典型文件组合，不声称对全部历史文件做过逐一审计。根目录快速开始见[README](../../README.md)；目标领域模型见[架构](../architecture/architecture.md)。

## 根目录与变更边界

| 路径 | 当前角色 | 变更原则 |
| --- | --- | --- |
| `小学/`、`初中/`、`高中/` | 旧有课程内容树：年级/学期/章节/知识点，包含源码和媒体 | 已有源码、视频及知识点路径仍是有效入口；不得仅为统一命名批量移动 |
| `external/` | 独立数学专题和多种 Manim 场景 | 不从所在目录推断年级或是否证明了某个定理 |
| `assets/` | `build_catalog.py` 生成展示索引，`index.html` 提供画廊，`catalog.json` 为当前输出 | 修改索引逻辑前记录现有 ID、URL、条目选择策略及差异 |
| `catalog/` | 分类词表、未来 Topic 示例和文档迁移记录 | 示例 schema 与现行画廊 catalog 不同，不能直接替换 |
| `docs/` | 体系化规范、历史 Prompt、数学研究、技术参考 | 区分历史记录与现行执行契约；旧路径跳转仍需保留 |
| `skills/source/` | Skills 唯一事实源 | 变更后同步三种 Agent 的原生 `SKILL.md` 镜像 |
| `.codex/skills/`、`.opencode/skills/`、`.claude/skills/` | 独立可读取的 Skills 镜像 | 不在镜像中单独改内容，使用 `tools/sync_skills.py` |
| `tools/`、`.github/workflows/` | 结构检查、Skills 同步、索引审计、部署自动化 | 增新内容路径前先检查索引扫描范围与部署触发路径 |
| `files/`、`videos/`、`*.sh`、根目录媒体 | 历史资源和维护脚本 | 未审阅前不执行全仓库媒体处理、清理或删除 |

## 典型知识点目录：从文件到证据

以下实例为 `小学/一年级/上册/第一章-10以内数的认识/001数一数/`，各知识点目录**可能缺少其中任一文件**。

| 文件 | 用途 | 审核重点 |
| --- | --- | --- |
| `description.json` | 课程与知识点描述、相关概念、公式与动画候选组件 | 年级、学期、教材来源是否属实；公式条件、组件名称是否可用 |
| `prompt.md` | 历史生成需求，常包含大段共享模板及 `<problem>` | 分离当前作品特有需求与通用/过时要求；见[Prompt 规范](../prompts/authoring.md) |
| `storyboard.md` | 镜头、数学结论、对象生命周期、时间与转场 | 每一数学结论何时建立、何处验证，是否出现对象遮挡/遗留 |
| `*.py` | Manim Scene 与辅助计算/对象构建代码 | 找到实际 `Scene` 子类和 `construct()`；不能把第一个 Python 类当成 Scene |
| `*.mp4` | 原始渲染或其他历史视频 | 核对具体文件和关联 Scene，不能只按后缀断言来源 |
| `*_finish.mp4` | 通常是后期处理过的成片 | 比较时长、音轨、版权、输出名称及当前索引选择逻辑 |

其他可能出现 `verify_geometry.py`、图片、音频、PDF、局部脚本或多个 Scene；出现与否不代表验证已经执行。目标是把**数学命题、Scene、媒体 Artifact、实际 Build 记录**作为独立的关联对象，而不是依赖同目录文件的数量或排序。参见[目标数据模型](../architecture/architecture.md)。

## 目前的索引/发布链路

`小学|初中|高中|external` 中的源码与视频 → `assets/build_catalog.py` → `assets/catalog.json` → `assets/index.html` → `.github/workflows/deploy-gallery.yml`。索引生成器目前具有基于路径和首个文件/类的启发式选择，存在辅助类被误识别、多个视频匹配不确定的风险；详情见[审计记录](../architecture/audit.md)。

对于新目录、新 Scene 类、多视频目录或路径迁移：先建立显式映射，保存迁移前 catalog，完成源路径/视频 URL/ID 差异审查后才修改索引与部署监听。除非完成前后端联调，**不要将目标 Topic manifest schema 直接替换当前 `assets/catalog.json`**。

## 安全审查清单

- 文档改动：检查相对链接、原有入口、Skills 镜像以及仓库结构；不需要也不应顺手重新处理视频。
- 场景改动：记录真实源码路径/类名、数学条件、静态与数值/符号测试、Manim 版本、低清预览及关键帧检查。
- 媒体/迁移改动：确认输入输出列表、资源权利、旧索引与新索引差异、回退路径；不可用语法检查代替画质验收。

检查命令和证据要求见[质量门禁](quality-gates.md)，Skill 路由见[Skills 总览](../../skills/README.md)。

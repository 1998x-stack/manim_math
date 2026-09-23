# manim_math：中文数学教学动画创作工程

以 [Manim Community Edition](https://www.manim.community/) 为主要可视化工具，组织中文数学知识点、教学分镜、可复现的动画源码与视频作品。仓库既是既有课程作品库，也是逐步标准化的创作工程；**当前课程目录与画廊保持兼容，新的分类、Skills 和元数据规范增量采用**。

> 本仓库不是一个已经完成迁移的 Python 包，也不保证全部历史场景可直接在任意 Manim 版本运行。数学正确性、中文字体、布局和最终视频均需要针对具体 Scene 验证。

## 快速导航

| 你要做什么 | 从这里开始 |
| --- | --- |
| 查找课程、源码和成片 | [小学](小学/)、[初中](初中/)、[高中](高中/)、[独立专题](external/)、[课程画廊](assets/index.html) |
| 理解整个仓库的文件职责 | [文件与交付物地图](docs/engineering/repository-map.md)、[架构和数据模型](docs/architecture/architecture.md) |
| 按年级或数学领域组织内容 | [课程章节参考](docs/curriculum/章节.md)、[分类规则](docs/architecture/categories.md)、[分类数据](catalog/categories.json) |
| 从知识点创作一段动画 | [Prompt 使用与编写规范](docs/prompts/authoring.md)、[六阶段创作流程](docs/engineering/scene-workflow.md) |
| 使用 Codex / OpenCode / Claude | [Skills 导航与路由](skills/README.md)、[Agent 总约定](AGENTS.md) |
| 验证质量或计划调整目录 | [质量门禁](docs/engineering/quality-gates.md)、[迁移方案](docs/architecture/migration.md) |
| 查阅全部文档 | [文档总目录](docs/README.md) |

## 内容与工程结构

```text
小学/ 初中/ 高中/            # 现有课程路径：学段、年级、学期、章节、知识点
external/                   # 不按单一年级归档的独立专题
assets/                     # 画廊页面、索引生成器和当前 catalog.json
catalog/                    # 分类词表、目标 Topic 示例、文档迁移清单
docs/                       # 架构、课程、Prompt、数学参考、工程说明
skills/source/              # AI Skills 唯一维护入口
.codex/skills/              # Codex 的独立可读取镜像
.opencode/skills/           # OpenCode 的独立可读取镜像
.claude/skills/             # Claude 的独立可读取镜像
tools/                      # 结构检查、索引审计、Skills 同步
files/ videos/              # 历史混合文件和媒体；不等于统一的新产物目录
```

一个已存在的知识点目录可能含有 `description.json`、`prompt.md`、`storyboard.md`、`*.py`、`*.mp4` 和 `*_finish.mp4`，也可能不完整。职责分别为知识点描述、历史生成要求、分镜、场景源码、原始视频和后期成片；**不可依赖文件顺序、名称推断内容已经完成或验证通过**。详细约定见[文件与交付物地图](docs/engineering/repository-map.md)。

## 环境与快速开始

需要 Python、Manim Community Edition、FFmpeg；渲染包含公式的场景还需可用的 LaTeX 环境，中文场景需要所用字体。具体 Manim 版本、字体和额外 Python 依赖应以目标场景的源码、实际运行环境和错误输出为准。`install_manim.sh` 为历史安装脚本，运行前先审阅内容；不将它视为跨平台的一键安装保证。

```bash
# 1. 克隆仓库（仓库包含已跟踪的视频等大型资产，完整克隆可能消耗大量空间）
git clone https://github.com/1998x-stack/manim_math.git
cd manim_math

# 2. 运行不依赖 Manim 的仓库结构与 Skills 检查
python tools/sync_skills.py --check
python tools/check_repository.py

# 3. 检查示例场景语法；命令本身不证明数学正确性或画质
python -m py_compile external/euler_line.py

# 4. 在已安装 Manim、LaTeX、字体等依赖的环境中，预览一个已知场景
manim -pql external/euler_line.py EulerLineScene
```

仅在需要更新画廊时运行 `python assets/build_catalog.py`；它会更新 `assets/catalog.json`，请审查差异后再提交。最终渲染示例：`manim -qh --resolution 1080,1920 external/euler_line.py EulerLineScene`。这是示例命令，不代表该场景在本次修改中已实际渲染。9:16 是仓库既有中文短视频的默认设计约束，不是 Manim 的通用限制。

## 从知识点到成片

1. **确认教学任务**：核对教材、年级、学期、先修知识与目标；读取对应知识点的 `description.json` 及 `prompt.md`。在 [Prompt 编写规范](docs/prompts/authoring.md) 中区分历史原文、项目规范与本次具体任务。
2. **确定数学规格**：写明定义、变量、适用条件、结论、证明依据、反例和极端/退化情形；需要时使用 [math-specification Skill](skills/source/math-specification/SKILL.md)。
3. **形成分镜**：将每个数学事实映射到画面、字幕、对象生命周期、时长、转场及验收条件，产出可审核的 `storyboard.md`。
4. **实现 Scene**：确认真实的 Scene 子类和类名，分离可纯 Python 测试的数学运算与 Manim 时间编排，遵循[创作流程](docs/engineering/scene-workflow.md)。
5. **分层验收**：依次完成语法、数学与边界检查、低清渲染、关键帧视觉审核，最后做生产渲染和媒体探测；证据及未完成项见[质量门禁](docs/engineering/quality-gates.md)。
6. **关联发布资产**：审查作品索引及旧 URL/ID 的差异；仅对具有相应权利的媒体做后期处理。`concat_mp4.sh` 会递归发现 MP4，不应当在未审阅输入输出的情况下用作整库自动发布命令。

## Prompt 与 Skills 的边界

- `docs/prompts/{xiaoxue,chuzhong,gaozhong}.md` 是历史课程提示词与纲要资料；不能替代经核对的教材或数学证明。
- 知识点目录下的 `prompt.md` 常同时包含通用模板和该课特有的 `<problem>`；保留原件，优先抽取本次任务的具体需求，避免重复粘贴或把历史建议当作已验证 API 行为。
- 新建内容遵循[分层 Prompt 契约](docs/prompts/authoring.md)，按任务在[Skills 总览](skills/README.md)选择相应模块。`skills/source/` 为唯一维护入口，镜像使用 `python tools/sync_skills.py` 生成并检查。

## 贡献、兼容与发布原则

新增场景时提交可定位的源码路径、准确 Scene 类名、课程/数学元数据、数学规格、分镜、验证记录及所需素材来源；不能运行的检查明确记录为未执行。修改历史作品优先修复单个知识点，不在文档 PR 中删除、批量搬动或重新编码已有媒体。任何重命名/迁移先定义稳定 `topic_id`、旧路径映射与回退办法，再同步画廊索引和 GitHub Actions 触发范围；详见[迁移方案](docs/architecture/migration.md)。

文档或 Skill 改动至少运行结构检查；含动画的改动另按其数学与视觉风险完成检查。仓库现状和未解决问题见[审计记录](docs/architecture/audit.md)。

# manim_math：中文数学教学动画创作工程

以 [ManimGX](https://manimgx.academa.ai/) 为主要可视化运行时，组织中文数学知识点、教学分镜、可复现的动画源码与视频作品。仓库既是既有课程作品库，也是逐步标准化的创作工程；**当前课程目录与画廊保持兼容，新的分类、Skills、元数据与 ManimGX 运行规范增量采用**。

> `feat/manimgx-migration-v1` 是 ManimGX 全面迁移分支。历史 Scene 正在从 Manim Community Edition 迁移；数学正确性、中文字体、布局、公式排版和最终视频都必须针对具体 Scene 验证，不能仅凭 import 成功判断迁移完成。

## 快速导航

| 你要做什么 | 从这里开始 |
| --- | --- |
| 查找课程、源码和成片 | [小学](小学/)、[初中](初中/)、[高中](高中/)、[独立专题](external/)、[课程画廊](assets/index.html) |
| 理解整个仓库的文件职责 | [文件与交付物地图](docs/engineering/repository-map.md)、[架构和数据模型](docs/architecture/architecture.md) |
| 理解 ManimGX 迁移 | [ManimGX 迁移架构](docs/architecture/manimgx-migration.md) |
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
manim_math_gx/              # 仓库级 ManimGX 运行约定，不模拟 ManimCE 内部实现
skills/source/              # AI Skills 唯一维护入口
.codex/skills/              # Codex 的独立可读取镜像
.opencode/skills/           # OpenCode 的独立可读取镜像
.claude/skills/             # Claude 的独立可读取镜像
tools/                      # 结构检查、索引审计、Skills 同步、ManimGX 迁移/审计
files/ videos/              # 历史混合文件和媒体；不等于统一的新产物目录
```

一个已存在的知识点目录可能含有 `description.json`、`prompt.md`、`storyboard.md`、`*.py`、`*.mp4` 和 `*_finish.mp4`，也可能不完整。职责分别为知识点描述、历史生成要求、分镜、场景源码、原始视频和后期成片；**不可依赖文件顺序、名称推断内容已经完成或验证通过**。详细约定见[文件与交付物地图](docs/engineering/repository-map.md)。

## 环境与快速开始

迁移分支要求 **Python 3.13+** 和固定版本的 **ManimGX**。ManimGX 自带新的 Rust/wgpu 渲染、视频编码和 mitex/Typst 数学排版路径，因此不再把 Cairo、FFmpeg、完整 TeXLive 作为 Manim 运行时前置条件；中文场景仍需要可用的 CJK 字体。Linux/CI 默认使用 Noto CJK，macOS 可通过 `MANIM_MATH_CJK_FONT="PingFang SC"` 保留历史字体。

```bash
# 1. 克隆仓库并进入 ManimGX 迁移分支
git clone https://github.com/1998x-stack/manim_math.git
cd manim_math
git switch feat/manimgx-migration-v1

# 2. 安装 ManimGX 与字体
./install_manimgx.sh

# 3. 运行不依赖渲染的结构检查
python tools/sync_skills.py --check
python tools/check_repository.py
python tools/manimgx_audit.py .

# 4. 检查示例场景语法
python -m py_compile external/euler_line.py

# 5. ManimGX 热预览 / 正式渲染
manimgx preview external/euler_line.py
manimgx render external/euler_line.py -r 1080x1920
```

ManimGX 的 `config.frame_width` 由 `pixel_width / pixel_height` 与 `frame_height` 推导，**不要再直接给 `config.frame_width` 赋值**。仓库竖屏默认配置位于 `manim_math_gx.runtime`。`tools/manimgx_migrate.py` 只执行机械安全的 import 与 frame-width 迁移；复杂 Tex、renderer 私有 API、媒体缓存与 updater 行为由 `tools/manimgx_audit.py` 提醒人工重构。

仅在需要更新画廊时运行 `python assets/build_catalog.py`；它会更新 `assets/catalog.json`，请审查差异后再提交。9:16 是仓库既有中文短视频的默认设计约束，不是 ManimGX 的通用限制。

## 从知识点到成片

1. **确认教学任务**：核对教材、年级、学期、先修知识与目标；读取对应知识点的 `description.json` 及 `prompt.md`。在 [Prompt 编写规范](docs/prompts/authoring.md) 中区分历史原文、项目规范与本次具体任务。
2. **确定数学规格**：写明定义、变量、适用条件、结论、证明依据、反例和极端/退化情形；需要时使用 [math-specification Skill](skills/source/math-specification/SKILL.md)。
3. **形成分镜**：将每个数学事实映射到画面、字幕、对象生命周期、时长、转场及验收条件，产出可审核的 `storyboard.md`。
4. **实现 Scene**：确认真实的 Scene 子类和类名，分离可纯 Python 测试的数学运算与 ManimGX 时间编排，遵循[创作流程](docs/engineering/scene-workflow.md)。
5. **分层验收**：依次完成语法、数学与边界检查、低清预览/渲染、关键帧视觉审核，最后做生产渲染和媒体探测；证据及未完成项见[质量门禁](docs/engineering/quality-gates.md)。
6. **关联发布资产**：审查作品索引及旧 URL/ID 的差异；仅对具有相应权利的媒体做后期处理。`concat_mp4.sh` 会递归发现 MP4，不应当在未审阅输入输出的情况下用作整库自动发布命令。

## Prompt 与 Skills 的边界

- `docs/prompts/{xiaoxue,chuzhong,gaozhong}.md` 是历史课程提示词与纲要资料；不能替代经核对的教材或数学证明。
- 知识点目录下的 `prompt.md` 常同时包含通用模板和该课特有的 `<problem>`；保留原件，优先抽取本次任务的具体需求，避免重复粘贴或把历史建议当作已验证 API 行为。
- 新建内容遵循[分层 Prompt 契约](docs/prompts/authoring.md)，按任务在[Skills 总览](skills/README.md)选择相应模块。`skills/source/` 为唯一维护入口，镜像使用 `python tools/sync_skills.py` 生成并检查。

## 贡献、兼容与发布原则

新增场景时提交可定位的源码路径、准确 Scene 类名、课程/数学元数据、数学规格、分镜、验证记录及所需素材来源；不能运行的检查明确记录为未执行。新增 Python 动画代码必须使用 ManimGX。修改历史作品优先修复单个知识点，不在文档 PR 中删除、批量搬动或重新编码已有媒体。任何重命名/迁移先定义稳定 `topic_id`、旧路径映射与回退办法，再同步画廊索引和 GitHub Actions 触发范围；详见[迁移方案](docs/architecture/migration.md)。

文档或 Skill 改动至少运行结构检查；含动画的改动另按其数学与视觉风险完成检查。仓库现状和未解决问题见[审计记录](docs/architecture/audit.md)。

# Repository filesystem · 分类与治理规则

> **STATUS / Incremental refactor** · 基线 `main@ffbf2236a46eb0755f516cda5e5d1a6bc24c1498` · 本文件记录可执行的归档与迁移规则，不表示全量课程代码、视频或许可证已获验证。

## 01 / 一级目录分类

| 分组 | 路径 | 责任与操作边界 |
| --- | --- | --- |
| COURSE / 课程 | `小学/`、`初中/`、`高中/` | 保留原学段/年级/学期/章节/课题路径；`description.json`、`prompt.md`、`storyboard.md`、Scene 和既有视频均可能被旧画廊引用。未经稳定 ID 映射和新旧索引比对，不批量移动。 |
| TOPICS / 独立专题 | `external/` | 独立数学专题代码、说明和视频；先核对真实 Scene 类与资产关系，再决定归类。 |
| INDEX / 发布 | `assets/` | 现行 `build_catalog.py` → `catalog.json` → `index.html`；与 `catalog/` 的目标模型不同。 |
| MODEL / 分类 | `catalog/` | 分类词表、目标 Topic 示例与迁移登记；不得直接替换生产画廊的数据契约。 |
| ENGINEERING / 工程 | `tools/`、`tests/`、`.github/` | 扫描、检查、测试、CI 与画廊发布。年级专用工具在规则统一前保留。 |
| DOCS / 文档 | `docs/` | `architecture/` 架构、`curriculum/` 课程、`math/` 数学、`prompts/` 提示词、`engineering/` 工程、`reviews/` 审阅记录。历史本机路径清单归 `reviews/legacy/`。 |
| AGENT / 技能 | `skills/source/`、`.codex/skills/`、`.opencode/skills/`、`.claude/skills/` | `skills/source/` 唯一编辑入口；其余为同步镜像；根 `skills/*.skill` 属历史归档，未审核不得移除。 |
| MEDIA / 历史资源 | `files/`、`videos/`、根目录 `*.sh` | 历史混合输入、音视频和兼容脚本；在引用审计前保持原路径。 |

## 02 / 清理分级

| 级别 | 允许的动作 | 前置验证 |
| --- | --- | --- |
| SAFE / 已确认无效 | 已追踪的 `.DS_Store` 等操作系统生成的缓存文件 | 核对具体文件类型、Git 索引及 `.gitignore`；删除不涉及课程或播放数据。 |
| ARCHIVE / 历史记录 | 人工整理的旧 `file://` 清单归 `docs/reviews/legacy/`，原入口保留跳转 | 使用 Git blob 原 SHA 无损复制原文；旧相对 Markdown 入口能够定位归档。 |
| REVIEW / 待判定 | 空 `.py`、旧 `*.skill`、重复文档、未使用 Shell、`files/` 的 JSON 和 PDF | 查 Git 引用、现行索引/CI/脚本依赖、来源与版权；不得凭文件大小或名称删除。 |
| BLOCK / 不自动迁移 | 课程路径、`external/*.py`、已追踪 MP4/MP3/PDF、`assets/catalog.json` | 稳定 topic/scene/asset ID、旧 ID/URL/媒体对照、运行与视觉验收、明确回滚方案。 |

## 03 / 目录迁移契约

1. **冻结基线**：记录提交 SHA、旧 `assets/catalog.json` 内容哈希、旧 ID、`pyFile`、`videoFile`、公开地址及被移动文件 Git blob SHA。
2. **发现真实依赖**：检查 README/Docs、相对 import、脚本参数、Actions `paths`、画廊索引和媒体嵌入链接；凡是不确定的引用先保留旧入口。
3. **以分类而非名称推断角色**：同名课程不自动合并；`_finish.mp4` 不能单凭后缀认定为已验收；空 Scene 文件可能是占位符。
4. **小批量变更**：每批列出旧→新路径；历史文档可保留跳转，Python 和视频需真实运行/URL 兼容方案，不能用 Markdown 跳转代替。
5. **验收**：结构检查、目标文件与原 blob 内容核对；若涉及课程/媒体，额外核对旧索引全字段、实际 Scene、视频 URL、低清渲染与关键帧。未执行时明确 `not_run`。
6. **回退**：独立分支与 PR 审核，回退单批提交；不重写 Git 历史、不无条件删除历史媒体。

## 04 / 此批执行内容

- 无损归档学段根目录的三份本机路径列表，并在旧位置保留文档跳转；新旧资源文件内容相同（沿用原 Git blob）。
- 删除根目录已追踪的 macOS `.DS_Store`；`.gitignore` 已排除后续此类文件。
- 不移动课程源码、音视频、分类注册表或现有 Gallery；不宣称已对全仓库进行了渲染或数学验证。

## 05 / 下一批实证清单

以 `tools/audit_curriculum.py` 与课程完整检出结果为基础，额外审计只有 `.py` 没有元数据的目录、历史路径清单与现有 catalog 的差集、非教学脚本的真实调用方和大型媒体的引用关系。`external/ceva_theorem.py` 在本次树中是零字节，先标记 `needs_review`，确认引用与预留目的后再作删除决定。随后按 `docs/architecture/phase-2-blueprint.md` 先建立持久 ID/媒体映射，再试迁少量真实课题。

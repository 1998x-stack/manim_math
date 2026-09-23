# 下一阶段实施路线：跨课程可靠性与生产契约收敛

> 基线：2026-09-23 `main@00421dc42993e21ccdaa807949f60781388a6312`；本文件是任务设计，不表示所有检查已运行。若主分支继续更新，执行时先重新核对 SHA、已合并修复及测试状态。关联第二阶段 #3–#6 和第三阶段 #7。不得把 534 条历史 Gallery 条目理解为 534 个唯一数学概念、532 个已验证视频或完整课程覆盖率。

## 1. 执行原则和不变量

先保障旧 ID、旧导航、已发布媒体地址和历史文件，再提升发现/验证能力；旧 `assets/catalog.json` 与 v2 在影子模式独立输出，不得直接改变生产索引的 schema。程序发现结果、元数据和人工判定必须分离；对缺失数据用 `not_run`/`needs_review`/`unknown`，不得生成伪造的 `passed`。禁用自动批量移动 MP4/MP3/PDF 和覆盖历史视频。每项工作独立 PR，含输入基线、正反例、失败证据、回滚方案。

## 2. 当前实证和潜在影响

- `catalog/` 当前未含持久的 v2 目录；#4、#5 的身份注册与 Schema/AST/双写未验收。`tools/legacy_contract.py` 能比较旧索引字段，但按 `legacy_id` 排序记录；源文件 hash 只能识别整体变化，无法逐条解释纯格式/导航顺序变动。
- `assets/build_catalog.py` 对课程主题选第一个非测试 Python 文件，对独立专题选 AST 第一个类；视频部分选择依赖文件名与 glob 顺序。扫描观察不能自动证明真实 Scene/媒体归属。
- Gallery 将若干来自目录或源码的名称直接插入 `innerHTML`，尽管已有 `escHtml()` 但调用不一致；这是当目录内容不可信时的 DOM 注入风险。页面视频 URL 指向 `raw.githubusercontent.com/.../main/...`，Pages 上传物仅含页面和 catalog；目录 `hasVideo` 不等于链接实时可播放。
- `tools/audit_curriculum.py` 是课程审计入口之一；另外存在 `audit_grade2/3/4/6.py`、`check_grade5.py` 及多个年级专用 workflow。独立性有利于修复，但通用规则和诊断契约需要收敛。
- 通用架构 CI 是稀疏检出，未装 Manim/字体/FFmpeg，不能证明所有课程源码、数学结论、视频或公网 URL 已通过。
- 原 Skill 同步只复制 SKILL.md，本迭代先补完整包镜像支持及回归测试；新增 `references/`/`scripts/` 内容必须自包含，不应依赖工具没有检查的项目外路径。

## 3. 依赖图和关键路径

`A: 历史索引冻结及稳定 ID (#4)` → `B: v2 Schema/显式 Scene/媒体映射 (#5)` → `C: 旧画廊兼容影子比对` → `D: 小范围源码试迁 (#6)` → `H: 两项真实作品全链路验收 (#7)`。

`E: Gallery 插值安全修复`、`F: 跨年级质量规则收敛及 CI 覆盖声明`、`G: 纯数学回归/可复用算法` 和 `S: 完整 Skill 包镜像` 可与 A 并行，但 E 发布前须执行浏览器测试，F 扩大扫描前必须保留现有年级特有规则。未通过 B/C 时不可切换 Gallery 数据源或搬迁源码；未通过数学与视觉验收时不可宣称 H 完成。

## 4. 工作包及 Definition of Done

| 包 | 实施切片 | 可执行验收与证据 | 回退 |
| --- | --- | --- | --- |
| A 身份冻结 | 固化旧 JSON 及来源 commit、原始顺序、别名/路径/URL；初始化 append-only 映射 | 旧 ID 全覆盖，碰撞/误绑定阻断；模拟重命名仍能双向解析；新增与移除有审阅清单 | 恢复旧索引与映射提交，不复用已发行 ID |
| B Scene/媒体 | `discover→normalize→validate→export_v2/export_legacy`，AST 解析别名/派生/多 Scene，媒体只按显式 manifest 确认 | 辅助类不会误作 Scene，歧义标记 `needs_review`；固定输入两次导出字节相同；旧字段及导航顺序兼容 | 禁用 v2 导出、恢复原扫描路径 |
| C Gallery 安全/兼容 | 从原始 catalog 构造 DOM 时统一处理文本/属性/URL；添加旧 ID/新 ID 可选定位，建立媒体可达性与跨版本检查 | 含 `<img onerror>`、引号、`&`、中文和斜杠的 fixture 不触发插入脚本，展示文字正确；旧 ID 均可访问；发布链接实测有状态记录 | revert 前端/适配器；已发布路径不删除 |
| D 分批迁移 | 先迁无外部 URL 依赖的小样，处理 import、路径和 workflow 触发 | 每批 old→new、索引全量差异、重渲染样片和回退提交；不能保证旧 URL 时禁止移动 | 逐 PR revert，不重写历史 |
| E 规则收敛 | 统一课程 AST 扫描、诊断数据结构和年级规则插件，保留现有 grade fixtures | 旧工具与新工具同一固定 fixture 结果可解释；所有旧 error 仍可检测；新增规则有误报测试 | 保留旧 CLI，开关关闭新规则 |
| F 覆盖声明 | 结构层、课程源码层、数学层、Manim 层、发布层独立工作流或结果记录 | 每次报告 `source_revision`/扫描目录/文件数/检查层级/status/artifact；稀疏检出不得宣称 full-source passed | 恢复先前 workflow，并保存旧报告 |
| G 数学内核 | 欧拉线外心与退化处理回归、纯数学模块和分镜断言追溯 | 共线/重复点拒绝伪造外心；等边三心重合时不输出 0:0 比值；直角/钝角/极端尺度和独立几何不变量有测试 | 旧 Scene 保留至样片人工审核通过 |
| S Skill 包 | 将 SKILL.md 与 references/scripts/assets 作为完整目录包同步；来源可信与相对路径检查 | 三个 Agent 完整包字节一致，缺文件/被篡改/孤儿/符号链接失败；脚本仅静态验证不自动执行 | revert 同步器，不删除镜像中未知文件 |
| H 全链路试点 | 选择几何与非几何各一项，关联 MathSpec→Storyboard→Scene→Build→Artifact→Gallery | 数学证明与数值测试分别审查；真实渲染/ffprobe/关键帧/中文字体/版权/实际 URL 均有可复核证据 | 切回旧 Gallery，保留原媒体 |

## 5. 最小 PR 切片和顺序

**PR-A（本次）**：记录现状和风险、实现完整 Skill 包镜像与 `tests/test_skill_packages.py`；仅修改 `tools/sync_skills.py`、测试与设计文档，不改 Gallery 或历史 Scene。验证 `python tools/sync_skills.py --check` 与 `python -m unittest discover -s tests -p 'test_*.py' -v`，均不证明数学和渲染通过。

**PR-B（优先）**：Gallery HTML 注入防护和无效 URL 处理。先添加恶意/边界字符串 fixture，修复所有模板插值，包括章节、年级、标题、badge、URL 属性和搜索结果；页面加载/搜索/播放/移动端回归；不变更旧 ID 和公开 URL。

**PR-C**：#4 的持久身份冻结与顺序语义差异；批准新增作品的迁移策略不可将 `--expect-count 534` 固化为未来永久总数。

**PR-D**：#5 的 AST/媒体关联与 v2 影子输出、配套差异；#6 再负责试迁。跨课程质量收敛可另立独立 PR 先实现只读汇总，不改已有年级规则的判定。

## 6. 全局验收门禁

G0：已登记历史 ID 覆盖率 100%，无未经审核的丢失/重新绑定。G1：新旧 Gallery 项及导航的未经审核差异为 0，公开媒体 URL 实测情况有证据。G2：变更涉及的全部课程源码有 AST/语法审计；无法扫描的文件必须 `not_run`，不得整体标记通过。G3：有关数学命题的边界测试、前提和证明审核记录齐备；数值样本不能替代数学证明。G4：被改动的 Scene 有真实低清渲染和关键帧审阅；构建环境、字体、时长、尺寸、产物 hash 可追溯。G5：发布前适用门禁均 `passed`，任何 `failed`、`needs_review` 或 `not_run` 阻断相应的发布宣称。

## 7. 持续优化与数据闭环

每个 PR 同时保存发现的错误类型、误报、检查覆盖数和 CI 耗时；使用固定测试样例测量跨年级规则复用，而非用“代码量减少”代替质量。定期从真实缺陷补充最小负例；先在 changed-files 模式运行，再对完整课程建立周期性只读审计。历史媒体迁移、第三方音频/字体许可、工作流仓库权限、Pages API 和源码与视频 URL 的版本绑定需分别审查、分别签收。

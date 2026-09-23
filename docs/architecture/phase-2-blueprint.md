# 第二阶段蓝图：稳定目录、领域模型与渐进迁移

> 状态：设计稿；基线 `main@8e47dadb29e0c46f7e59a32de43db129b46e0d81`；范围：身份、数据模型、索引、验证、迁移。**本文本身不表示 534 个作品已经迁移或验证。**

## 0. 目标、不变量与非目标

目标：让课程导航、数学知识、Manim Scene、构建记录及媒体资产具有独立身份，以可追溯的边关联；从旧 Gallery 单一路径扫描迁移到清晰的源数据→规范化目录→兼容输出，且不丢失现有 534 个索引主题和公开链接。

不变量：①旧 `assets/catalog.json` 原字段和每个旧 `id` 在兼容期原样保留；②已有 `pyFile`、`videoFile`、`hasVideo` 在未验证迁移前不变；③已登记的 `topic_id`、`scene_id` 不随改名/搬迁变化；④缺失文件、未验证数学、来源未知均显式表示为 unknown/warning，禁止自动补全为通过；⑤同一个发布 URL 在没有重定向/完整验证前不得移动或删除；⑥原作品文件和大媒体在本阶段只读。

非目标：重写全部 Manim Scene、自动证明所有公式、移动全仓库的 MP4/PDF、切换托管平台、批量重命名章节、改变已有视频发布地址、把语法检查等同于数学/视觉验证。

## 1. 已知基线与风险

原数据流：`小学|初中|高中|external` → `assets/build_catalog.py` → `assets/catalog.json` → `assets/index.html` → `.github/workflows/deploy-gallery.yml`。原索引器：课程专题选取第一个非 `verify_/test_` Python 文件；独立专题把 AST 第一个 `ClassDef` 当候选 Scene；视频通过文件名近似匹配。两个路径的 `id` 均来自相对路径 MD5 的 10 位前缀，迁移会改变身份；视频关联可能误判；目前旧 Gallery 的数据契约由前端决定，不能只更新后端。第一阶段索引审计计数：小学 209、初中 200、高中 111、external 14，合计 534；这是**旧索引条目数**，不等于已经逐个确认的独立数学概念数或 Scene 数。

## 2. 领域边界和关系

- `CurriculumPlacement`：教材版本/学制/年级/学期/章节/知识点的导航定位，可多版本、多归属，未知项为 null；不作为主键。
- `Topic`：数学主题和教学目标、定义及先修关系。一个主题可有 0..N 课程定位与 Scene；重复课程条目是否应合并需人工认定，不因标题相同合并。
- `ProofSpec`：命题、前提、定义域、退化条件、推导或权威来源、断言与数值容差；仅记录证明证据，实验渲染不算证明。
- `Storyboard`：关联 topic 与 ProofSpec 版本的镜头序列，包含教学目标、图形动作、字幕/旁白、时长预算与公式引用。
- `Scene`：独立于 Python 文件名的实例身份；源码定位、可运行 `Scene` 子类名、场景参数、topic 多对多关联、storyboard 关联。
- `Build`：输入 revision/hash、环境版本、渲染/后期命令、开始结束时间及每个门禁状态；同 Scene 可有多个构建。
- `Artifact`：媒体/字幕/图片独立版本、sha256(若已取得)、存储位置、许可/来源、生成的 build_id、发布 URL；同一 Scene 可有 raw/final 多资产。
- `Publication`：渠道、已发布稳定 URL、版本、访问方式与旧路由映射；它不由媒体磁盘路径自动推导。

有向依赖：课程定位→Topic；Topic→ProofSpec/Storyboard；Storyboard→Scene；Scene→Build→Artifact→Publication。索引/画廊只消费验证过的数据契约，不修改数学源文件。允许一个 Scene 引用多个 Topic，且 Artifact 可引用来源明确的外部资源。

## 3. 身份规范（见 ADR-0001）

`topic_id`、`scene_id`、`artifact_id`、`build_id` 是持久化键；路径、标题、分类、Scene 类名与内容 hash 都不是主键。旧的 `id` 保留为 `legacy_id`；对首次登记的每个旧索引条目创建一条不可覆盖的映射 `legacy_id ↔ topic_id`，并记录原始 `pyFile`、`videoFile`、索引快照 sha256 与导入时间。单个旧条目是 `LegacyEntry`，不强制与未来的知识层 Topic 一一对应；如发现两个旧条目实际属于同一数学主题，保留各自 LegacyEntry，另行审阅合并的语义关系。已公布的 `legacy_id` 不允许复用给其他条目。

## 4. 机器可读数据契约

推荐版本化实体文件：`catalog/v2/topics/<topic_id>.json`、`catalog/v2/scenes/<scene_id>.json`、`catalog/v2/artifacts/<artifact_id>.json`、`catalog/v2/builds/<build_id>.json` 和 `catalog/v2/legacy-map.json`。规模 534 时应先从旧快照 bootstrap 注册表，生成确定性排序的 JSON；随后把注册表作为权威数据，而非每次重扫描覆盖。手工维护项（分类、教材、证明）与扫描观察项（文件存在/候选类）分离。所有 JSON 契约均需 JSON Schema + 语义校验器：唯一 ID、引用目标存在、路径为仓库内相对路径且禁止 `..`、有限枚举来自 `categories.json`、未知/未验证不默认为 `verified`。

推荐读路径：登记实体与 legacy 映射 → 解析源码/媒体观察结果 → 语义校验与差异报告 → `catalog-v2.json`（供未来消费者）+ `assets/catalog.json`（兼容适配器）。任何生成文件应按固定排序和稳定序列化输出；连续构建字节相同，否则 CI 失败。兼容适配器必须能保留旧字段和 ID，并以可选、命名空间明确的新字段暴露 topic/scene 标识；在旧前端确认之前不改原 JSON 结构。

## 5. Scene 发现算法

从 Python AST 扫描**顶层** `ClassDef`，排除验证/测试类、无法解析的模块；识别显式继承 `Scene`、`MovingCameraScene`、`ThreeDScene` 或其在同文件已知的派生类；支持 `manim.Scene` 与安全可识别的 import alias；`GeometryCalculator` 等工具类不得作为 Scene。对跨文件继承、动态定义、别名不明确、多 Scene、多源码候选等情况生成 `needs_review`，不能选第一个类蒙混过关。每个注册 Scene 需要显式存储 `class_name`；解析结果必须与登记吻合。测试样例包含 `GeometryCalculator + EulerLineScene`、多场景、语法错误、别名、相对 import 和无 Scene 文件。禁止 import/执行待扫描脚本作为发现方式，避免模块级配置及副作用。

## 6. 媒体关联与 URL

先冻结旧 `videoFile`、`hasVideo` 和现有发布 URL，建立资产清单：文件路径、媒体角色(raw/final)、可用性、sha256(可获取时)、来源/许可(未知则 null)。禁止靠“文件名相近”在 v2 自动绑定不确定的视频；显式 `scene_id`/`artifact_id` manifest 为准，旧 heuristic 只生成候选报告。对于 GitHub Pages、仓库 blob/raw 和本地 file:// 分别维护地址，**路径存在不代表公开 URL 可访问**。不能确认的 legacy video 标记 `unresolved`，不默默清空旧索引值；发布 URL 迁移须另立兼容/重定向方案与真实链接测试。

## 7. 从当前系统到 v2 的分阶段交付

**P2.0 基线冻结（无行为变更）**：保存 `main` commit、旧 catalog 内容 hash/条目排序及 `legacy_id → pyFile/videoFile` 快照；盘点 534 个 legacy_id 的重复/空值/路径冲突与视频关联不确定项；输出 JSON 报告与人工待判清单。验收：所有旧条目均在冻结快照中可定位，差异审计能判定新增/消失/重命名。

**P2.1 身份注册表（兼容模式）**：bootstrap 一次性 legacy-map，新增 topic/scene 独立 ID 分配机制及 append-only 校验；新旧索引并行但当前 Gallery 不读取 v2；对迁移样例模拟改名后主键保持不变。验收：534 条旧 ID 覆盖率 100%、无冲突/无一对多静默合并、重复执行不改变注册表字节。

**P2.2 领域/Schema 与校验**：发布 schema、样例、引用完整性/枚举/路径/空值检查和负例测试；仅在有来源时填充学制与教材，数学正确性不得由 `hasVideo` 推断。验收：无效引用、重复键、未知枚举、逃逸路径和伪造 `verified` 均在 CI 明确失败。

**P2.3 索引器与双写差异报告**：分离 `discover → normalize → validate → export_legacy/export_v2`；显式 Scene 检测和 media manifest 覆盖旧 heuristic；默认只读，旧导出在影子模式逐字段与冻结快照比较，差异需 allowlist+审阅说明。验收：无意的 legacy ID、排序、字段、video URL 变化为 0；不要求仓库忽略的 MP4 必然在 CI 中存在。

**P2.4 前端兼容与最小目录试迁**：先增加路由/查询对 stable topic_id 的可选支持；保留旧 ID 和旧 URL；选 2~3 个无公开依赖或可明确保留原入口的非关键示例，做 `git mv` + import/相对路径/渲染命令检查。验收：旧画廊项数量、可点击链接、候选 Scene 和资源映射不回退，试迁样本在本地 Manim 环境通过低清渲染及关键帧人工审核。

**P2.5 扩大迁移（单独 PR）**：按课程章节/专题逐批移动，每批附 old→new 映射、脚本检查、Gallery 差异、回退提交；媒体存储平台和音频许可另行决策。无回退/未确认公开 URL 的批次不得继续。

依赖顺序：P2.0→P2.1→P2.2→P2.3→P2.4→P2.5。任务可以并行研究，但写入 authoritative registry、替换旧索引或移动源码不可越过前置门禁。

## 8. CI / 测试矩阵

| 等级 | 测试 | 必须检查 |
| --- | --- | --- |
| L0 无 Manim | schema/注册表/映射/唯一性/引用完整性/幂等性/路径合法性 | 任何 PR |
| L1 无 Manim | AST 场景发现、分类规则、候选/歧义报告、legacy-v2 差异快照 | 索引器相关 PR |
| L2 依赖 Manim | `py_compile`、scene 类可加载、低清样片及媒体元数据 | 被迁移/修改的 Scene |
| L3 数学+人工 | 边界/退化输入、数值/符号/证明证据，版面/字幕/字体、视频版权/发布 URL | 正式发布/视频迁移 |

新 CI 只在稀疏检出环境运行 L0/L1；完整源码、字体、Manim 与视频可访问性测试在有相应依赖的环境运行，结果分别记录，绝不把前者冒充后者。可选 nightly 完整仓库审计以监控新增破损路径。

## 9. 风险、回退、负责人交付

高风险：path-hash 身份漂移、多 Scene/辅助类误配、同名视频误绑、Git 忽略/历史大媒体导致 CI 虚假缺失、旧前端字段契约被改、数学/版权未经验证被标记通过。所有不可确定结果进入 `needs_review`，绝不自动更改原视频路径。每一工作包通过独立 PR 和审计产物交付；回退优先 revert 对应 PR，不重写历史、不删旧文件。

完成定义：稳定身份清单和 v2 领域/schema 成为权威源；534 个 legacy 条目可双向定位；旧 Gallery 在同一基线上兼容；至少一个真实专题完成显式 Scene 发现、数学规范、分镜、低清渲染及双索引链路；全量媒体迁移不在第二阶段完成定义之内。
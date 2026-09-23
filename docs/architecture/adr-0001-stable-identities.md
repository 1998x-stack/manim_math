# ADR-0001：不可变身份与旧索引兼容

- 状态：Proposed（在 P2.1 完成并验证 534 条冻结映射后可改为 Accepted）
- 决策范围：Topic / LegacyEntry / Scene / Artifact / Build / Publication 的身份及迁移契约

## 背景

现有 `assets/build_catalog.py` 使用 `md5(relative_path)[:10]` 创建 Gallery 条目 `id`。课程专题以专题目录为输入，独立专题以 Python 文件路径为输入。`find_scene_py()` 选择第一个非 `verify_/test_` 文件，`find_scene_class()` 返回 AST 的第一个类，独立专题视频按文件/类名启发式匹配。这些观察结果不应再被当作稳定数学/作品主键。当前旧索引 534 条，只能说明有 534 个 Gallery 条目，不证明存在 534 个不同数学知识点。

## 决策

1. 将现有 `id` 原样视为**不可复用的 `legacy_id`**，旧 Gallery 的 `id` 在兼容期保持不变。首次从受控快照导入时，为每条 `LegacyEntry` 登记独立 `entry_id`，保存 `legacy_id`、源快照 SHA、原始 `pyFile` 和 `videoFile`。绝不在迁移后用新路径重新生成 `legacy_id`。
2. 另行分配一次性、无语义 `topic_id`（建议 `topic_` + 32 位 uuid4 十六进制）、`scene_id`（`scene_` + 32 位 uuid4 十六进制），由注册表持久化并禁止覆盖。仅做 bootstrap 的脚本可根据旧 ID 查重/关联，不能让路径/标题/类名决定后续 ID。新增 ID 由注册/建档操作生成，并与审核后的对象绑定，不允许每次构建重生。
3. `LegacyEntry` 与 `Topic` 分开：一个旧作品可同时涉及多个数学主题，两个旧作品也可能属于同一数学主题。自动导入阶段可以赋予一个 provisional topic 作为兼容锚点，但 `status=legacy-imported`，后续主题合并必须人工审核，不删除历史条目或旧 ID。
4. `Scene` 实体拥有自己的 `scene_id`、原始和当前源码路径及显式 `class_name`。重命名类或移动文件只修改字段及别名记录。多 Scene 的模块必须逐项登记，不得推断“第一个类就是 Scene”。
5. `Artifact` 是具体文件或外部对象版本，`build_id` 表示一次构建活动；内容 SHA256 用于校验而非身份（不同 URL / 版权/来源相同字节也可能不同资产）。Publication URL 与文件路径分别维护。
6. `catalog/v2/legacy-map.json` 是 append-only 权威映射；修改已有条目必须使用显式迁移记录 `old → new + reason + review + timestamp`，CI 对现有 `legacy_id` 与 `entry_id` 不允许静默删除或重新绑定。旧字段在适配器生成中逐字段保留，v2 字段只经 namespaced 映射输出。

## 备选方案及取舍

- 继续路径 MD5：实现简单，但目录迁移、大小写和 Unicode 归一化将造成身份漂移，因此仅用作历史别名。
- 由标题/领域组成可读 slug：检索友好，但跨学段、多教材、同名/改名容易冲突，可作为可变别名，不作为主键。
- 内容 hash 作主键：代码修订或重编码将改变主键，两个不同作品也可能字节相同，只能用于完整性校验。
- 直接统一旧条目为 Topic：会把 Gallery 页面条目和抽象数学主题强制一对一，后续合并/拆分困难。因此保留 LegacyEntry 独立关系。

## 必须测试的例子

- 原始目录和 Python 文件同时重命名：`topic_id`、`scene_id`、`legacy_id` 及旧 Gallery URL 全部不变。
- 不同年级有相同标题：不得根据标题自动合并，不得复用 ID。
- 单文件含 `GeometryCalculator` 与 `EulerLineScene`：AST 发现不能把工具类登记为 Scene。
- 单文件有两个 Scene：均可登记独立身份；任何模糊媒体绑定进入待审核队列。
- MP4 缺失/未检出或权属不明：不以此删除 legacy 索引，也不能标记已发布或数学已验证。
- 连续两次从同一注册表生成目录：输出字节完全相同；路径变更仅更新显式 locator，不修改身份记录。

## 决策的后果

增加注册表和审核成本，换取可迁移、可回滚、可追踪的作品身份。P2.0 先冻结旧快照，P2.1 再批量登记；未冻结前不能迁移课程目录。若已被外部引用的旧 ID/URL 无可用兼容方案，相关迁移必须暂停。
# P2 数据契约与导出兼容规范

> 设计稿：以下字段和文件布局属于 v2 草案，**尚未被现有 `assets/build_catalog.py` 或 Gallery 读取**。禁止把文档样例当作已完成迁移。

## 1. 标识与版本

独立保存 `schema_version: 2`、`registry_version`、`generated_from`（源数据 Git commit 与 SHA256）、`generator_version` 和 `generated_at`（仅构建报告携带，不能写入要求幂等的规范目录）。主题、Scene、资产和构建的 id 是注册式持久主键；`legacy_id` 是既有 Gallery 页的别名，不是通过当前路径实时计算的字段。相同标题不等价于同一主题；同字节视频不等价于同一发布资产。

## 2. 逻辑实体示例（仅展示关键字段）

```json
{
  "schema_version": 2,
  "topics": [{
    "topic_id": "topic_17d9b96aa2df449ca88083d790fc1eb5",
    "title": "欧拉线",
    "domains": ["geometry.euclidean.triangle.centers"],
    "curriculum_placements": [],
    "prerequisite_topic_ids": [],
    "proof_spec_ids": [],
    "status": "legacy-imported"
  }],
  "scenes": [{
    "scene_id": "scene_5a1efc9906784f05af2edbbd7f8e7b11",
    "topic_ids": ["topic_17d9b96aa2df449ca88083d790fc1eb5"],
    "source": {"path": "external/euler_line.py", "previous_paths": []},
    "class_name": "EulerLineScene",
    "storyboard_id": null
  }],
  "legacy_entries": [{
    "legacy_id": "<freeze-from-existing-catalog>",
    "topic_ids": ["topic_17d9b96aa2df449ca88083d790fc1eb5"],
    "scene_ids": ["scene_5a1efc9906784f05af2edbbd7f8e7b11"],
    "legacy_py_file": "external/euler_line.py",
    "legacy_video_file": null,
    "legacy_has_video": false
  }],
  "artifacts": [],
  "builds": [],
  "publications": []
}
```

示例中的 ID 为设计用占位标识，`legacy_video_file` 与 `legacy_has_video` 不代表实际欧拉线条目的现状；真实导入必须从冻结的现有 JSON 逐字段复制，不得照搬样例。

## 3. 字段约束

`topic_id/scene_id`：各自命名空间内唯一、必须在注册表持久保存；目标引用必须存在。`legacy_id`：索引输入里的旧 `id`，不能为空、不可重分配。`path`：仓库根目录下的 POSIX 相对路径，不允许绝对路径、`..`、空段与反斜杠；仅受信源代码或经核验的 manifest 可设置。`class_name`：在 AST 中发现的 Scene 子类或经人工确认的动态类；工具类不能通过。`domains` 等维度：必须属于 `catalog/categories.json`；无法证实则为 `[]` 或 `null` 而非猜测。`status`：不能因存在 MP4 而自动由 `legacy-imported` 升级为 `verified`/`published`。

`ProofSpec` 必填 proposition、assumptions、constraints、verification_evidence（含方法、样本或引文、结果及可复现实验）和 review_status。`Storyboard` 每个 shot 必须有目标、动作、关键文本、时长范围和可选 proof assertion ref；未完成时使用 `draft`。`Build` 需记录源码 revision、python/manim/ffmpeg/字体/LaTeX 环境（无法得知为 null）、命令、参数和多项门禁状态。`Artifact` 必须区分 `storage_location`、`public_url`、`source/license` 与可选 checksum；状态 `file_missing` 不等于 `public_url_broken`。

## 4. 导出与事务边界

读取顺序：权威 ID 注册表及显式 manifest → 旧扫描观察结果 → 语义验证 → 标准化 v2 输出 → legacy adapter。`discover` 不写入 ID 注册表；`normalize` 不凭标题合并；`validate` 失败则禁止覆盖旧文件；`export` 写临时文件并原子替换，仅在差异检查/审批通过后启用。所有生成目录固定 key 和数组排序，禁止带实时 `generated_at` 破坏幂等性。v2 schema 不可以直接覆盖 `assets/catalog.json`。

兼容投影：保留旧 `levels[].grades[].semesters[].chapters[].topics[]` 层级及每项原有 `id/number/name/docstring/pyFile/videoFile/hasVideo`。允许在独立字段或独立 sidecar 提供 `topic_id/scene_ids`，不把 `id` 改成 `topic_id`。旧 URL 与旧视频指向依赖部署侧兼容检验，不得仅凭 JSON 字段相等推断外部链接正常。

## 5. 版本演进与冲突

v2 添加可选字段属于向后兼容，移除字段/修改语义/改变身份映射需要新 schema_major 与迁移计划。不同 contributor 同时新增条目时，要求基于最新注册表 rebase，再进行唯一性与引用完整性检查。对同一个 `legacy_id` 出现两个不同 `topic_id` 的情况阻断构建，交人工判定。任何显式删除必须保留 tombstone 和原始别名，避免旧链接指向另一作品。

## 6. 必须提交的契约测试

正例：旧索引 534 条逐项映射成功；两个相同标题保留不同 legacy entry；同一 Topic 对应多 Scene；移动路径但 ID 不变；同输入二次生成字节一致。负例：重用 legacy_id、悬空 scene_id、未知 taxonomy、路径穿越、多文件仅取首个 class、视频启发式误绑、未审核 `verified`、修改旧 JSON 后未提供差异报告。每条测试应提供 fixture，CI 不需要下载 MP4 或运行 Manim。
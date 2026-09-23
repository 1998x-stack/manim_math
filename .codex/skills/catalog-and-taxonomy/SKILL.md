---
name: catalog-and-taxonomy
description: 维护小学/初中/高中课程 Category、Topic/Scene/Artifact 身份、Manim 源码和视频的显式对应、旧画廊索引与新分类；新增作品、修索引或迁移时使用。
---

# Catalog and taxonomy｜兼容索引

本 Skill 自包含旧索引与目标索引的边界说明；按需读取 `references/catalog-contract.md`。`scripts/check_catalog.py` 使用标准库检查旧画廊 JSON 的 ID 重复、关键字段及视频标志一致性；不扫描或修改媒体。

## 执行流程

1. 确定课程维度（学段/教材/年级/学期/章节）和数学领域维度，未知教材版本留空，不凭路径猜测教学版本。
2. 区分旧画廊 `id` 与未来稳定 `topic_id` / `scene_id`。旧 ID、旧 `pyFile`/`videoFile` 和公开 URL 是兼容契约，不可用新路径重新计算并覆盖。
3. 对源码使用明确 Scene 类名和路径。辅助类、多个 Scene、多个 MP4 或近似文件名都不能自动建立权威关联；生成待审候选表。
4. 更改索引前后运行 `python scripts/check_catalog.py assets/catalog.json`，比较条目数量、ID 和关联路径。该脚本验证结构，不证明视频存在、数学正确或 URL 可访问。
5. 引入新内容目录前更新扫描器、部署触发路径、页面路由和测试；发布流程默认保留旧画廊输出结构，只有验证前后端兼容后才能引入新 schema。

## 输出

交付显式关联或 `needs_review`、旧新 ID 映射、差异报告及实际检查结果。完整字段契约与歧义场景位于 `references/catalog-contract.md`，无需加载仓库其他技能。

---
name: catalog-and-taxonomy
description: 维护课程与数学领域 Category、稳定作品标识、场景/视频映射及 assets 画廊目录；用于分类与索引代码改动。
---

# Catalog and taxonomy / 分类索引

## 触发

修改小学/初中/高中学期目录、独立几何专题、分类字段、自动生成目录、GitHub Pages 画廊，或导入/迁移现有动画时加载。阅读 `docs/architecture/architecture.md`、`docs/architecture/categories.md`、`assets/build_catalog.py`、`.github/workflows/deploy-gallery.yml`。

## 当前约束

扫描器以四个固定根目录递归发现作品；课程目录只选第一个非验证 Python 文件，视频优先首个 `_finish.mp4`，`topic_id` 由相对路径 MD5 前十位生成；`external/` 以首个 AST 类名和视频名模糊配对。`external/euler_line.py` 中有先于主 Scene 的 `GeometryCalculator`，不能把“第一个类”当作场景。旧 `assets/catalog.json` 前端消费结构不应在未联调时直接更改。

## 操作步骤

1. 为 Topic、Scene、Artifact 分别建模；课程维度 `level/grade/semester/chapter/curriculum` 和数学领域 `domains[]` 正交。未知教材版本显式留空，跨学段内容可有多个关联。
2. 稳定 `topic_id` 从内容 manifest 中取得，不再由路径推导；旧路径哈希保留为 `legacyId` 供过渡；唯一性检查、迁移前后 ID 映射必须可复现。
3. 使用明确的 Scene 类名/源码位置；若自动发现，解析继承 Manim Scene 的真实类而非第一个类；对解析失败、多场景、多媒体或模糊匹配产生待审核报告，不静默选择。
4. 对前端 schema 加版本并保留旧字段直到画廊迁移结束；比较修改前后 Topic 总量、Scene 总量、视频关联和 URL，可验证差异而非仅看生成成功。
5. 新物理内容根目录启用时，同步改变扫描器、GitHub Actions 触发路径、链接生成和测试用例；旧直链需要可用入口或稳定重定向策略。
6. 记录 metadata 的来源、确认状态、最后更新时间；人工确认优先于模型猜测。参见 `docs/architecture/migration.md`。

## 验收

没有无意丢失课程、作品 ID、场景和成片的关联；同名作品不能互相覆盖；新旧画廊链接/索引差异有解释，旧作品仍可查询。未运行索引生成及页面检查时明确说明。

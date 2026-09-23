# 语义分类和迁移清单（不替换现有画廊）

- [`categories.json`](categories.json)：机器可读的分类值注册表；`docs/architecture/categories.md` 解释使用规则。分类值表示教学检索语义，不要求按标签逐层建物理文件夹。
- [`topic.example.json`](topic.example.json)：未来稳定作品 ID + Scene/媒体关联的示例，**不是现有 `assets/catalog.json` 的输入文件**，不表示所有旧作品已分类。
- [`documentation-moves.json`](documentation-moves.json)：本次整理的原路径与目标路径清单；旧位置保持跳转入口，原始内容在新路径。

现有画廊仍由 `assets/build_catalog.py` 生成 `assets/catalog.json`。不要把两个 JSON 结构混用；启用新 schema 之前先做旧 ID、新 ID、视频 URL 和课程数量的完整映射及前端兼容测试。

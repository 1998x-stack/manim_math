# 系统架构与核心逻辑

## 1. 分离三个相互正交的轴

**课程轴**：教育阶段 → 年级 → 学期 → 教材版本 → 章节 → 知识点；用于教学导航，不必决定内容的物理存放位置。**数学轴**：代数、几何、函数、统计概率、数论、微积分等主题，可对同一知识点多标签标注。**生产轴**：数学命题/证明 → 教学分镜 → Manim Scene → 验证记录 → 原始渲染 → 后期成片 → 发布资产。一个专题可以跨多个年级，单个动画亦可以包含多个知识点。

## 2. 当前运行依赖图

`小学|初中|高中|external 的场景源码与就地视频` → `assets/build_catalog.py` → `assets/catalog.json` → `assets/index.html` → `deploy-gallery.yml` → GitHub Pages。`files/Away.mp3` + 现有 MP4 → `concat_mp4.sh` → `_finish.mp4`。这条链是本次迁移必须保留的兼容边界。

## 3. 目标领域对象

- `Topic`：稳定 `topic_id`、中文标题、课程定位、数学分类、前置知识、学习目标；**不使用路径哈希作为主键**。
- `Scene`：`scene_id`、所属 topic、Python 模块路径、Manim Scene 类名、版本和时长；一个 Topic 对应零至多个 Scene。
- `ProofSpec`：前提、结论、定义域、非退化约束、数值/符号验证断言；不把动画示意误作数学证明。
- `Storyboard`：每一镜的概念、画面、旁白/字幕、预计时长及对应数学断言。
- `Artifact`：源视频/成片/海报/音频资产的路径或 URL、校验和、来源、许可信息、生成参数及关联 scene_id。
- `Build`：Manim/FFmpeg/字体/系统版本、命令、检验状态和输出；可重现，不要求所有旧资源立即补齐。

示例（**目标数据模型，非现有 catalog.json 的 schema**）：

```json
{
  "topic_id": "geometry.euler-line",
  "title": "欧拉线",
  "level": ["junior", "senior"],
  "domains": ["geometry.triangle.centers"],
  "scenes": [{"scene_id": "euler-line.main", "source": "external/euler_line.py", "class": "EulerLineScene"}],
  "legacy_paths": ["external/euler_line.py"],
  "status": "legacy-imported"
}
```

## 4. 内部边界

数学计算/验证不依赖 Manim，可用 NumPy 或 SymPy 单独测试；Manim 只消费经过验证的坐标、公式和状态；音视频后处理只消费渲染产物；画廊只消费有明确 schema 的索引。避免在 Scene 中混合长篇证明、文件扫描和发布逻辑。对旧 Scene 采用渐进抽取，不做无差别批量重写。

## 5. 兼容层与演进

当前 `assets/catalog.json` 保持现状，避免未经前端联调就切换 schema。下一步给索引器增加附加 manifest 读取与显式 Scene 类匹配，输出 `schemaVersion`、稳定 ID 与 `legacyId`，并执行新旧路径/URL 差异检查后再修改展示层。新物理目录启用前，先扩展 workflow 的 `paths` 和扫描入口；不得先移动代码后修索引。

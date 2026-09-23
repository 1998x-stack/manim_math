# manim_math

面向中文数学教学的 Manim Community Edition 动画作品、课程索引与创作工程。**现有作品和画廊保持兼容；新规范增量采用。**

## 从哪里开始

- [文档导航](docs/README.md) · [仓库审计](docs/architecture/audit.md) · [架构与数据模型](docs/architecture/architecture.md)
- [分类体系](docs/architecture/categories.md) · [目录迁移方案](docs/architecture/migration.md) · [质量门禁](docs/engineering/quality-gates.md)
- [动画创作流程](docs/engineering/scene-workflow.md) · [多 Agent Skills](skills/README.md)
- [课程画廊](assets/index.html)，由 `python assets/build_catalog.py` 生成 `assets/catalog.json`。

## 当前目录

`小学/`、`初中/`、`高中/` 是原有学段场景；`external/` 是独立的几何专题；`assets/` 是展示站点及索引生成器；`videos/` 与场景目录内已有视频为历史产物；`files/` 为混合资源/历史脚本；`docs/` 为分层文档；`skills/source/` 为 Skills 单一事实源，`.codex/skills/`、`.opencode/skills/`、`.claude/skills/` 为完整、可独立读取的镜像。

## 运行

```bash
python assets/build_catalog.py
python tools/sync_skills.py --check
python tools/check_repository.py
manim -pql external/euler_line.py EulerLineScene
```

生产渲染示例：`manim -qh --resolution 1080,1920 external/euler_line.py EulerLineScene`。需要 Manim CE、FFmpeg、LaTeX 和支持中文的字体；画廊索引构建仅使用 Python 标准库。旧目录的实际位置和命令以源文件为准。

## 重构约定

不自动重命名或移动已有课程场景、视频、音频或 PDF；先维护稳定 `topic_id`、记录路径映射、更新画廊索引及部署触发器，并做新旧索引差异校验。仓库暂时保留旧文件入口；参考 [迁移说明](docs/architecture/migration.md)。

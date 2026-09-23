# 仓库审计（2026-09-23，main: 6dfc3f7）

## 事实与可复现入口

- `CLAUDE.md` 描述 1080×1920、9×16 中文教学短视频及小学/初中/高中和 `external/` 的内容路径；实际场景样例 `external/euler_line.py` 在模块层设置 `config`，并实现 `GeometryCalculator` 和分阶段 Scene。
- `assets/build_catalog.py` 以固定四个学段目录扫描场景，`find_scene_py()` 选取目录中的第一个非 verify/test Python 文件；`find_video()` 选择第一个 `_finish.mp4` 或 `.mp4`；作品 ID 为相对路径 MD5 前 10 位。
- `scan_external()` 从 Python 文件中提取第一个 AST 类名以辅助匹配视频文件，并用文件名近似匹配兜底。这种匹配可能把辅助类误当作 Scene：例如 `external/euler_line.py` 中 `GeometryCalculator` 位于 `EulerLineScene` 之前。
- `.github/workflows/deploy-gallery.yml` 仅在 `assets/**` 和旧学段/`external/` 中的 `.py` 修改时自动触发；新目录一旦启用，必须同步修改触发器与索引构建器。
- `docs/` 的课程提示词、几何研究和 Manim 技术参考混放；`skills/` 现存 `.skill` 归档还不是三种 agent 原生 `SKILL.md`。
- `.gitignore` 曾整体忽略 `.claude/` 与 `.opencode/`；不调整则新 Skills 无法通过日常 `git add` 正常提交。
- `concat_mp4.sh` 全仓库递归寻找 MP4，使用 `files/Away.mp3` 输出 `_finish.mp4`；不能将其视作仅处理待发布文件的安全流水线。`clean_pycache.sh` 删除生成目录，未经确认不运行。

## 风险分层

P0：数学真伪、几何退化、公式与中文排版错误、视频路径或画廊作品 ID 改变、误删已跟踪大媒体。P1：多文件/多场景选取不确定、视频名称与 Scene 类不同、索引缺元数据、文档相对链接失效。P2：字体跨平台、生成产物存储成本、历史 `.skill` 内容版本与许可边界。

## 设计判断（非已完成事项）

保留旧目录为可工作的兼容入口，先引入分类词表和稳定数据模型；后续通过可回退的迁移清单逐个移动场景。几何算法的近退化情况应显式失败或单独定义行为，不能自动将外心替换成重心并继续声称定理经过验证。这里的建议不是对仓库中全部场景做出的测试结论。

# 数学动画 Skills：两个任务入口

本项目把原先分散的十个 Skill 合并为 **2 个完整、独立可运行的专业 Skill**。两个 `SKILL.md` 负责选择工作流，`references/` 按需加载专业细节，`scripts/` 只运行确定性静态校验和测试；历史 `*.skill` 压缩包不在本次重构范围。

| Skill | 用户任务与触发场景 | 已合并的能力 |
| --- | --- | --- |
| [`curriculum-prompt-suite`](source/curriculum-prompt-suite/SKILL.md) | 522 课的 Prompt/变量化、`description.json`、数学知识点、证明与反例、教学分镜、索引、路径迁移审查 | prompt-to-scene、math-specification、catalog-and-taxonomy、safe-repository-migration |
| [`manim-video-production`](source/manim-video-production/SKILL.md) | Manim Scene 编写/修复、几何、对象生命周期、中文/竖屏、动态关键帧、渲染、FFmpeg 与发布 | manim-scene、geometry-precision、chinese-vertical-layout、render-and-publish |

## 调用方式

- **只研究课程或批量 Prompt：**选择 `curriculum-prompt-suite`。本 Skill 能独立交付数学规格和 `storyboard.md`，不必加载视频 Skill。用 `python tools/prompt_suite.py inventory --root .` 和 `check --root .` 盘点、核验 522×3 模板。
- **已给定题目，只要动画源码或视频：**选择 `manim-video-production`。若数学条件缺失，先在本 Skill 内补齐，不强制引用另一个 Skill。
- **从原始 Prompt 到正式成片：**按课程 Skill → 视频 Skill 顺序交接 `math_spec`、分镜、验证状态；让两个 Skill 各自负责一段专业流程。
- 只有当任务需要时才阅读相应 `references/`，不必把几十页规则全部加载上下文。

## 迁移后的可执行脚本

`curriculum-prompt-suite/scripts/`：`prompt_suite.py`、`extract_problem.py`、`check_contract.py`、`check_catalog.py`、`check_moves.py` 以及 `test_prompt_suite.py`。

`manim-video-production/scripts/`：现有 `production_check.py`、`audit_scene.py`、`geometry_model.py`、`runtime_probe.py`、`verify_geometry.py` 与测试，另并入 `discover_scene.py`、`check_triangle.py`、`scan_mathtex.py`、`check_manifest.py`。全部旧脚本按原文件内容保留，无需第三方包的检查器仍然可以单独运行；专业渲染验证才需要 Manim/NumPy/FFmpeg/LaTeX。

## 唯一维护源与镜像

`skills/source/` 仅包含以上两个 Skill。通过 `tools/sync_skills.py` 将完整目录镜像到 `.codex/skills/`、`.opencode/skills/`、`.claude/skills/`、`.pi/skills/`；修改单一规范源再同步四套镜像。三平台的课程 `prompt.txt` 位于各自 `prompts/curriculum/`，属于逐课输入数据，不是新增的 Skill。

```bash
python tools/sync_skills.py --check
python tools/prompt_suite.py check --root .
python -m unittest discover -s tests -p 'test_skill_bundles.py' -v
```

`check` 为只读；没有运行的数学证明、动态帧、Manim 渲染、媒体验收均标记 `not_run`，不能以静态成功替代视频制作完成。任何迁移不能覆盖原始课程 Prompt、既有 MP4、音乐或旧公开 URL。

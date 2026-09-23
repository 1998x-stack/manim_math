# 质量门禁与可追溯验证

从课程 Prompt 到数学规格、分镜、Scene、视频和画廊，每个阶段需要与任务风险相称的实际证据；**写在文档中的命令、计划或自动生成的候选组件不是通过证明**。文档型 PR 不需要运行 Manim，但必须区分结构检查与数学/媒体验收。

| 门禁 | 适用变更 | 通过判据 | 实际证据 |
| --- | --- | --- | --- |
| 课程/Prompt | 新知识点、重写生成要求 | 年级/学期/教材已核对或明确未知；历史规则与本次需求分开；无跨学段错误示例沿用 | 来源路径、待确认清单、[Prompt 契约](../prompts/authoring.md) |
| 文档/Skills | README、docs、Skill 的变更 | 入口与相对链接有效；源 Skill 和三个镜像内容一致 | `python tools/sync_skills.py --check`、`python tools/check_repository.py`、人工链接检查 |
| 代码 | Scene 和生成脚本 | Python 可解析，实际 Scene 类名和命令一致 | `python -m py_compile path/to/scene.py`、CLI 输出 |
| 数学 | 定理、几何构造、数值过程 | 前提、定义域、证明和反例清晰；退化/边界行为明确；公式与几何不变量可核对 | 独立纯 Python 断言、SymPy/NumPy 记录、证明/来源；说明近似误差 |
| 分镜与版面 | 字幕/公式/动画时序 | 每镜的数学事实正确，中文、点标和公式在画面内且无遮挡 | `storyboard.md`、低清渲染、关键帧人工审核 |
| 生产视频 | 渲染、后期处理 | Scene 完整渲染；分辨率、帧率、时长、音轨符合设计且无误覆盖 | Manim 日志、`ffprobe`、文件及代表帧 |
| 索引/迁移 | 新作品、路径/媒体修改 | 明确 scene/topic 与媒体关联；旧链接/ID 无意外消失；资源许可有记录 | 新旧 catalog 差异、路径/URL 检查、回退清单 |

## 常用检查命令

```bash
# 只读的结构性检查
python tools/sync_skills.py --check
python tools/check_repository.py

# 按任务选择，必须替换成真实路径和类名
python -m py_compile path/to/scene.py
manim -pql path/to/scene.py ActualSceneClass

# 确实需要更新画廊时执行；会写 assets/catalog.json
python assets/build_catalog.py
```

`tools/check_repository.py` 仅检查它显式列出的结构/镜像/分类约束，不会全面爬取 Markdown 相对链接、验证数学证明、检查视频或媒体许可。`assets/build_catalog.py` 是写操作，务必审阅索引差异。完整画质检查依赖具备字体、LaTeX、Manim、FFmpeg 的渲染环境和关键帧人工审核，轻量 CI 不等价替代。`external/euler_line.py` 的退化三角形行为仍需专门回归测试；不能因为本次文档检查通过就视为已解决。

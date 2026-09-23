# 直线与平面平行｜分镜与独立数学验收

- 保留 Scene 入口：`line_plane_parallel.py::LinePlaneParallelScene`，六镜头；9:16 竖屏。所有平面多边形是局部透视**示意**，不是三维证明或无限平面的边界。
- 模型：`α:z=0`、`β:y=0`、`m={(t,0,0)}`、`l={(t,0,1.2)}`。数学性质从三维向量/法向量验证，不从二维投影视觉关系猜测。

| 镜头 | learning_fact／必需前提 | observable_state／屏上公式 | check |
|---|---|---|---|
| 1 引入 | 不能仅凭线线平行推出线面平行 | 提出「同方向一定平行平面吗」并回答需要面外条件 | 文案不把两个定理写作无条件互推 |
| 2 定义 | 直线与平面无公共点 | 平面 α、上方直线 l、投影线与高度辅助线；`l∩α=∅ ⇔ l∥α` | `line_plane_relation(l,...,α)==parallel` |
| 3 判定 | `m⊂α`、`l∥m`、`l` 不包含于 `α` | 同向不同高度的 l/m 与独立列出的三项条件；最后给结论 | 面内/面外用关系分类检测；`test_criterion` 包含缺少面外条件的反例 |
| 4 性质 | `l∥α`、`l⊂β`、`α∩β=m` | 两局部示意面、面内 l、两面交线 m；最后给 `l∥m` | 两面法向量不平行且交线方向正确；β 必须包含 l |
| 5 小结 | 定理不可省略前提 | 并排说明判定/性质，给出 l/m 同在 α 内时的反例 | 不使用无条件 `线线平行 ↔ 线面平行` |
| 6 收尾 | 先检查前提再使用定理 | 结语后清理作者署名及本镜对象 | 不 FadeOut 临时未在场对象 |

## 分层验收状态

本课回归：`python verify_line_plane_parallel.py`；仓库 CI 入口：`高中/高三/tests/test_line_plane_parallel.py`。使用 `python -m py_compile line_plane_parallel.py verify_line_plane_parallel.py`、Skill `scripts/audit_scene.py` 检查静态候选；Manim 预览渲染命令：`manim -ql line_plane_parallel.py LinePlaneParallelScene`。真实渲染后还需查看首帧、定理前提/结论帧、中文字体与公式排版、视频安全区和音轨。当前没有视频实际渲染、关键帧或 ffprobe 验收记录，不覆盖仓库现有 MP4。

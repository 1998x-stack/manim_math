# 平面与平面平行｜修订七镜分镜与数学验收

入口 `plane_plane_parallel.py::PlanePlaneParallelScene`；9:16 竖屏，所有四边形只显示无限平面的有限局部。`iso` 仅作示意，不用于验证三维空间交线和线段长度。

空间模型：`α:z=0`、`β:z=2`、`γ:y=0`，α、β 两个不同平面无公共点；γ 分别与二者交于沿 x 方向的直线 a、b。

| 镜头 | 必要前提 / learning_fact | observable_state | check |
|---|---|---|---|
| 1 引入 | 定理必须保留成立条件 | 提示检查几何关系 | 不暗示无条件套公式 |
| 2 定义 | α∩β=∅ 当且仅当 α∥β | 两块不同高度平面示意，完整公式 | 两个平面法向量平行且空间位置不重合 |
| 3 判定 | `a,b⊂α`、`a∩b={P}`、`a∥β`、`b∥β` | 两条确实在点 P 相交的面内线及所有条件 | `test_definition_and_criterion` 包含只用两条平行线的反例 |
| 4 性质 | `α∥β`，且 γ **分别与两平面相交**于 a、b | 垂直截面 γ、两条交线与完整公式 | `test_sections`；γ 若平行 α 则无交线，性质不适用 |
| 5 推论 | AB∥CD，A,C∈α，B,D∈β | 两块平面间平行线段与端点条件、长度公式 | `test_segments_and_endpoint_conditions`；脱离端点条件长度可不同 |
| 6 总结 | 不省略相交线和端点条件 | 四条完整文字概括及判定反例 | 不用原片中的 `a∥β,b∥β⇒α∥β` 或 `AB∥CD⇒AB=CD` 无条件箭头 |
| 7 片尾 | 条件优先 | 清除本镜字幕和作者信息 | 对象生命周期与安全区 |

## 验证状态

数学回归：`python verify_plane_plane_parallel.py`，由 `高中/高三/tests/test_plane_plane_parallel.py` 纳入现有 CI。静态：`python -m py_compile plane_plane_parallel.py verify_plane_plane_parallel.py`，Skill `scripts/audit_scene.py`。渲染：`manim -ql plane_plane_parallel.py PlanePlaneParallelScene` 后还需查看 P 是否同时属于 a、b、截线与段端点的关键帧、字体和安全区，并用 ffprobe 核实视频；本次未运行 Manim/ffprobe，旧 MP4 不覆盖。

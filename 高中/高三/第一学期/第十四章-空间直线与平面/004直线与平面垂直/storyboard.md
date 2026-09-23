# 直线与平面垂直｜七镜头、三维模型与验收

入口 `line_plane_perpendicular.py::LinePlanePerpendicularScene`，沿用七镜头与 9:16 比例。画面通过 `iso` 把三维空间映射到二维，**斜投影不保角**；原脚本将投影后非直角的两向量送入 `right_angle_mark`，会画出不对应实际空间直角的符号。修订版取消这些伪直角框，改用三维向量点积验证空间夹角并展示对应结论。

## 数学模型

平面 `α:z=0`；法向量 `u_l=(0,0,1)`；面内相交线方向 `u_m=(1,0,0)`、`u_n=(0,1,0)`；`u_m×u_n` 非零且 `u_l·u_m=u_l·u_n=0`，因此 `l⊥α`。

对于性质②，特意取 `l={(0,0,t)}`、`m={(s,0.8,0)}`：原线方向垂直，但不相交。通过垂足的绿色虚线与 `m` 平行，用于说明异面直线的垂直角度，而**不是**把原本不相交的两条直线画成在屏幕上相交的真直角。原脚本的 `right_angle_mark` 画在二维投影到 `m` 的点上，缺乏空间交点依据，现删除。

| 镜头 | 数学命题／前提 | 画面可观察状态 | data_assertion / render_frame |
|---|---|---|---|
| 1 引入 | 投影不保空间夹角 | 定义、判定与性质概览 | 标注空间关系须验三维条件 |
| 2 定义 | `l⊥α` 当且仅当对 α 内任意直线 m 有 `l⊥m` | 画出 α 与 l/m/n，公式表述任意直线 | 方向向量对面内基向量的点积为零 |
| 3 判定 | 面内 m、n **相交**且 l 均垂直于它们 | α、交点 P、m/n/l 与完整条件公式 | `test_criterion_requires_intersection`；两平行面内方向不足以定面 |
| 4 性质① | 两条不同线 l1、l2 均垂直 α，则互相平行 | 两条法向线及完整条件 | `test_plane_properties`；检查不同直线 |
| 5 性质② | l 垂直 α，m 是 α 内**任意**直线 | m 不经过垂足；辅助平行虚线过垂足 | `test_skew_perpendicular_does_not_intersect`，不得画成原线实际相交 |
| 6 总结 | 条件完整 | 四条知识点依次出现 | 中文缩放安全区、每条对象生命周期 |
| 7 片尾 | 三维数据验证优先 | 概括文字与作者信息清场 | 文字无遮挡且无未添加对象 FadeOut |

## 分层验证

`python verify_line_plane_perpendicular.py`；仓库 CI 通过 `高中/高三/tests/test_line_plane_perpendicular.py` 调用。`python -m py_compile line_plane_perpendicular.py verify_line_plane_perpendicular.py`、Skill `scripts/audit_scene.py` 是静态门槛；`manim -ql line_plane_perpendicular.py LinePlanePerpendicularScene` 的真实渲染、关键帧观察、公式字体与安全区检查，以及音轨/ffprobe 都需另行记录。已有 MP4 保持不变；不能以纯数学或静态检查冒充 render_verified。

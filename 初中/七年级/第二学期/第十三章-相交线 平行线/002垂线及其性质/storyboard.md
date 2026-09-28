# 垂线及其性质｜七镜数学规格与验收

入口 `perpendicular_lines.py::PerpendicularLines`。1080×1920，逻辑 9×16。保留原有 MP4，不把旧媒体视为本批渲染证据。

## 同源几何数据

主直线 `l` 由 `L0=(-3.5,0)` 和 `L1=(3.5,0)` 确定。`P=(-1.5,2.5)`、`Q=(1.8,2.8)`；`H=foot(P,l)`、`K=foot(Q,l)`。垂足统一由实际线方向向量 `v=L1-L0` 计算：`t=(P-L0)·v/(v·v)`，`H=L0+t*v`，直线两端重合时拒绝计算。同样计算 K。对角线或水平线等情况均要验证垂足满足 `(P-H)·v=0`，以及垂足位于无限直线 l 上；超出所画线段的投影仍可能属于无限直线。

本课选 `A=(0.8,0)`、`B=(-3.2,0)`。实际长度 `PH=2.50`、`PB≈3.02`、`PA≈3.40`；严格数学结论是对直线上任意点 `X` 均有 `PX≥PH`，且当且仅当 `X=H` 时取等号。因此“垂线段最短”的两个有限样例仅用于演示，不代替一般证明。第二个点的点线距离 `QK=2.8`。

## 分镜 → 可见数据 → 专项检查

| 镜头 | 屏上数学内容 | 检查 |
|---|---|---|
| opening | 直线 l、点 P、垂足 H 与直角标记 | 线段 PH 与 l 真正垂直；图形/标题不越界 |
| definition | `PH⊥l` 与垂足 H | 直角标记两边使用直线方向和垂线方向的单位向量，不靠手绘坐标猜测 |
| uniqueness | 通过 P 的两条非垂直虚线与唯一垂线 | 虚线终点都在线 l 上且不等于 H；唯一性表述有前提“过一点” |
| shortest_distance | 点 A、B，线段 PA、PB、PH 与数值比较 | `PH=2.50<PB≈3.02<PA≈3.40` 与真实点坐标一致；距离公式引用相同数据 |
| application | 另一点 Q、其垂足 K、`QK=2.8` | K 按相同投影函数计算，真实点到直线距离非负 |
| summary | 垂线唯一性、垂线段最短 | 区分唯一的垂线与从点到直线上任意点的多条连接线段 |
| outro | `PH⊥l ⇒ d(P,l)=PH` | 条件 H 为 P 在 l 上垂足明确，最终文字无遮挡 |

## 验证状态

- `python -m py_compile perpendicular_lines.py check_lesson.py`：pass。
- `python check_lesson.py`：pass；从实际源码提取投影函数进行水平、正负斜率、直线反向、垂足超出线段、点在线上、退化直线以及两组距离回归。有限用例不是对“任意点”性质的形式化证明。
- Manim、TeX/CJK 字体、逐镜关键帧与运行时 Mobject 边界、ffprobe/音频：环境缺少 Manim，均为 `not_run`；不覆盖原 `PerpendicularLines.mp4`、`PerpendicularLines_finish.mp4`。
- 在完整环境中预览：`manim -ql perpendicular_lines.py PerpendicularLines`；核对实际足点、直角小方框、每条线段对象、数值标签与音轨，真实渲染和媒体检查完成后才可标记最终通过。

# 008 切线的性质与判定｜逐课修复报告

## 本课实际源码范围
- `tangent_theorems.py`：Scene `TangentTheorems`，保留七段。
- `tangent_properties.py`：Scene `TangentProperties`，保留八段；通过继承前者复用验证过的可视化过程，独立保留判定条件引入分镜。
- `tangent_math.py`：标准库纯数学模型；`test_tangent_math.py`：本课专项回归。

## 发现与修复
- 原 `tangent_theorems.py` 总结卡片从 `LEFT*10` 开始，却用 `RIGHT*0` 入场，停在画外；现逐条 `FadeIn`。
- 原 `calculate_tangent_points` 使用平方根和反三角函数但未在方法内部拒绝圆内、圆上、非有限外点；现使用统一的解析投影公式，拒绝退化输入，并检查切点在圆上、半径与切线垂直、两条切线长相等。
- 对判定定理明确“双重条件”：经过半径外端点 **且** 垂直于该半径。对切线长定理补充 `OA=OB`、`OP` 公共及两个直角，以 RHS 三角形全等解释 `PA=PB`，不以图形目测替代证明。
- 两个 Scene 使用同一圆心、半径、圆外点及切点生成逻辑，减少多份数据不同步的问题；原 Prompt 和 MP4 未改。

## 验收状态
- syntax：**not_run**；`python -m py_compile tangent_math.py tangent_theorems.py tangent_properties.py test_tangent_math.py`。
- math/unit_tests：**not_run**；`python -m unittest -v test_tangent_math`。
- ast：**not_run**；需要对两个 Scene 使用 Skill `audit_scene.py` 并人工处理 WARN。
- manim_render/frame_review：**not_run**；分别运行 `manim -ql tangent_theorems.py TangentTheorems` 与 `manim -ql tangent_properties.py TangentProperties`，检查全部关键帧文本包围盒、TeX、切点位置和切线长证明。
- ffprobe/audio_review：**not_run**；当前无新成片，旧 MP4 不计入验收。

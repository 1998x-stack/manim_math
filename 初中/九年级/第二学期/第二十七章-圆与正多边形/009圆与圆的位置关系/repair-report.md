# 009 圆与圆的位置关系｜逐课修复验收记录

- 场景：`TwoCirclesRelations`；保留九段教学分镜及五种主要关系，原 MP4、Prompt、音轨保持不变。
- 发现：原 `calculate_intersection_points` 在边界使用直接 `sqrt(R²-a²)`，未针对浮点舍入保护理论非负的被开方数；原切点函数仅用外切/内切布尔值返回同样方向，缺少半径角色改变时的通用校验；原场景没有重合圆 `R=r,d=0` 的明确边界处理。
- 修订：`two_circles_math.py` 提供外离、外切、相交、内切、内含与重合分类；独立计算 0/1/2 个公共点，重合时明确拒绝当作有限个交点处理；切点单独按半径角色计算，对缩略图浮点缩放带来的数个 ULP 使用仅消除舍入误差的数值容差。
- 场景图形、交点标记、字幕和缩略图都基于同一几何数据，数学前提不满足时阻止渲染而非仅打印 warning。新增边界与退化案例回归测试。
- syntax/math/unit_tests/ast：**not_run**；运行 `python -m py_compile two_circles_relations.py two_circles_math.py test_two_circles_math.py`、`python -m unittest -v test_two_circles_math`、Skill `audit_scene.py`。
- manim_render/frame_review/ffprobe/audio_review：**not_run**；预览 `manim -ql two_circles_relations.py TwoCirclesRelations` 后分别审查五种关系与总结的关键帧边界、圆周接触点和正确字幕，再对正式成片探测音视频信息。

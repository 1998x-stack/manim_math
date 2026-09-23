# 007 直线与圆的位置关系｜修复与验收记录

- Scene：`LineCircleRelations`（七段）；不改原 MP4/Prompt/音轨。
- 原始错误：`calculate_intersection_points` 将 `d>r+1e-6` 判相离，却只将 `abs(d-r)<1e-6` 判相切；边界处可能进入负根号分支。圆心距判定应是严格数学分类，而非根据显示误差随意合并。
- 修复：新增无 Manim 依赖的 `line_circle_math.py`，以 `(r-d)*(r+d)` 计算两个相交点的横向偏移；精确相切返回单个横坐标 `0`，相离返回空元组；非有限数、负距、零半径直接异常。主 Scene 三种情况、图形交点和总结缩略图均从同一模型派生。切点显示垂线/直角符号；保留原七段教学顺序。
- 新增 `test_line_circle_math.py`：两交点、单切点、无交点、边界两侧、非法输入、Scene 入口检查。
- syntax/math/unit_tests/ast: **not_run**；需运行 `python -m py_compile line_circle_relations.py line_circle_math.py test_line_circle_math.py`、`python -m unittest -v test_line_circle_math` 和 Skill 审计脚本。
- manim_render/frame_review: **not_run**；`manim -ql line_circle_relations.py LineCircleRelations` 后检查圆、直线、交点和全部公式的真实屏幕边界与 TeX 编译。
- ffprobe/audio_review: **not_run**；没有新的视频输出，不能用仓库旧视频证明修复通过。

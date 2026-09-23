# 010 正多边形与圆｜逐课修复记录

- 源文件 `regular_polygon_circle.py`；入口 `RegularPolygonAndCircle`；保留六个教学阶段、原始 Prompt 和旧 MP4。
- 已观察到的原始错误：总结阶段图形整体缩放平移后，原脚本仍围绕平移前的 `self.CENTER` 旋转多边形，导致图形与外接圆不同心。改为在同一 VGroup 中整体变换，并以 `self.circle.get_center()` 作为旋转中心。
- 单独提供纯数学模型 `regular_polygon_math.py`，边数 n≥3、R>0；基于同一数据生成中心角 2π/n、边长 2Rsin(π/n)、边心距 Rcos(π/n)、周长与面积 S=Cr/2；用顶点在圆上、等边与鞋带公式交叉验证面积，特别核对正六边形边长等于半径。
- 动画替换后保留当前显示对象的同一引用；中文使用 `Text`，`MathTex` 只承担数学表达式，不依赖中文 TeX 编译。
- 新增 `test_regular_polygon_math.py`：n=3、4、6、12，n/r 非法输入、平移坐标及真实 Scene 结构检查。

## 分层验收
- syntax/math/unit_tests：**not_run**。需在课程目录运行 `python -m py_compile regular_polygon_circle.py regular_polygon_math.py test_regular_polygon_math.py` 与 `python -m unittest -v test_regular_polygon_math`。
- ast：**not_run**。使用 `.opencode/skills/manim-video-production/scripts/audit_scene.py` 审计实际 Scene 并逐条处理 WARN。
- manim_render/frame_review：**not_run**。运行 `manim -ql regular_polygon_circle.py RegularPolygonAndCircle`，逐镜检验公式、中文字体、几何图元和移动后的圆心以及 9:16 安全框。
- ffprobe/audio_review：**not_run**。旧视频和原音轨未改，不能以旧 MP4 当作本次修复验证结果。

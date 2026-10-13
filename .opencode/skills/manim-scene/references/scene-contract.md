# ManimGX Scene 执行契约

## 实现和验收

给定数学规格与分镜后，确认每镜包含：可见对象、对象所有权、数学事实、相应字幕、变换类型、结束状态、预期时长。一个 `Scene` 可调用多个辅助类，辅助类不能与 Scene 混淆。AST 解析不导入目标文件，无法完整解析跨模块别名或动态继承；此时人工核对源文件与实际 ManimGX CLI 类名。

## 对象生命周期与时间线

- `Transform(source, target)` 完成后通常继续持有 source 引用；`ReplacementTransform(source, target)` 后不要假设 source 仍是屏幕上的当前对象，变量应切换到 target。
- updater 与 `always_redraw` 必须明确创建、运行、暂停、清除时机。迁移旧课程时重验 ManimGX 的 exact-`dt` 语义，不把“每帧一次”当成固定步长积分器。
- `.animate` 的调用在动画开始状态上构造目标；连续 `Succession` 与同一对象并行动画要显式检查起点和组合结果，不能依赖 ManimCE 的历史帧行为。
- 旋转依赖的几何关系明确 `about_point`/轴；不要依赖旧引擎对点数组逐点重算的副作用。
- 公式、点、标签必须与同一数学模型数据同源；移动坐标系或图形后，不继续使用过时的绝对画布坐标。
- 通过纯 Python 函数隔离数学运算；数学测试不应要求导入 ManimGX。

## 画幅、中文和公式

- 仓库竖屏课程优先调用 `manim_math_gx.configure_render()`。ManimGX 的 `config.frame_width` 由 `pixel_width / pixel_height` 与 `frame_height` 推导，禁止直接赋值。
- 中文说明使用 `Text`，字体优先仓库 `CJK_FONT` 或 ManimGX 可复现的 bundled/generic CJK 字体；避免写死 `PingFang SC` 等单一系统字体。
- `MathTex`/`Tex` 使用 ManimGX mitex→Typst 路径。`TexTemplate`、LaTeX package、自定义宏和依赖 glyph path 的 Transform 必须人工重构，不以安装 TeXLive 作为兼容方案。

## 检查命令

```bash
python scripts/discover_scene.py path/to/scene.py
python -m py_compile path/to/scene.py
ty check path/to/scene.py
manimgx inspect path/to/scene.py ActualSceneClass -t 0,end
manimgx render path/to/scene.py ActualSceneClass -r 270x480 --fps 15 -o preview.mp4
```

`py_compile` 与 `ty` 不代表 Scene 能构建完整时间线；`inspect` 首尾通过也不代表逐帧视觉无误。动态课程至少补充中间状态检查；正式发布前记录 ManimGX/Python 版本、实际命令、关键帧审查、输出媒体参数和仍未确认事项。

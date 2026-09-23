---
name: manim-scene
description: 根据数学规格与分镜实现、修改和审查 Manim Community Edition 教学 Scene，涵盖场景结构、动效和运行验收。
---

# Manim Scene 设计与实现

## 触发

新建场景、调整动画节奏、修复 API/渲染报错、抽取复用组件或审核既有 `.py` 时加载。先看现有项目风格 `CLAUDE.md`、`docs/engineering/scene-workflow.md` 和对应数学规格；不要仅凭文件名推断 SceneClassName。

## 设计路径

1. 描述受众、单一学习目标、最终结论和时长范围；分镜表写清“阶段/对象/数学事实/镜头/字幕/过渡/预计耗时”。一镜一主要认知任务，数学结论出现前先准备定义和构型。
2. 识别真正的 `Scene`/`MovingCameraScene` 等子类与 `construct()`；文件可能有 `GeometryCalculator` 等辅助类，不能取 AST 中第一个类当场景名。决定是否要复用原类而非平行创建近似重复文件。
3. 使 `construct()` 负责时序，`build_*`/`animate_*` 管理对象创建与转场，纯数学运算独立成不导入 Manim 的函数。避免测试所依赖的导入路径因移文件而失效。
4. 使用 `VGroup`、`animate`、`Transform`/`ReplacementTransform`/`TransformMatchingTex` 时核对源目标存活关系；有 updater 时明确启动/清除时机，防止对象漂移、叠加或错误状态遗留。
5. 使用 `MathTex` 呈现公式，中文单独 `Text`；检查文本宽度、数学符号、对应点标和颜色语义。9×16 仅作为目前项目默认视觉规范，不把固定帧尺寸硬编码为通用 Manim 原理。
6. 先进行语法检查和纯数学检验，再低画质渲染与关键帧检查，最后生产渲染和媒体检查。保留实际运行命令、Manim 版本及错误日志；没有渲染环境时明确说明未完成视觉验收。

## 交付约定

提交可定位的 `path/to/file.py` + 精确 Scene 类名 + 渲染命令；说明改动涉及的数学事实与视觉分镜、预期长宽比、所用字体/外部资产；如修改已有路径，同步修复 catalog 和部署监听，不碰无关视频。若代码仍有字体/布局依赖，给出可复现环境前提。

## 常见失败点

不要把中文直接写进 `MathTex`；不要把 `Angle` 的有向角与无向角混为一谈；不要把退化构型返回的占位坐标当作有效数学解；不要只靠 `py_compile` 宣称整个动画通过测试。

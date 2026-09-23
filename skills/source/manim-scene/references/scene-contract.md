# Manim Scene 执行契约

## 实现和验收

给定数学规格与分镜后，确认每镜包含：可见对象、对象所有权、数学事实、相应字幕、变换类型、结束状态、预期时长。一个 `Scene` 可调用多个辅助类，辅助类不能与 Scene 混淆。AST 解析不导入目标文件，无法完整解析跨模块别名/动态继承；此时人工核对源文件与实际 CLI 类名。

## 对象生命周期

- `ReplacementTransform(source, target)` 后不应假设原 source 仍在 Scene 中；留意外部变量对被替换对象的引用。
- updater 与 always_redraw 明确创建、暂停、清除时机，避免结束时残留或随渲染状态漂移。
- 公式/点标关联必须与数学模型保持一致；移动图形后不要继续使用过时的绝对坐标。
- 通过纯 Python 函数隔离数学运算；测试不需导入 Manim。中文说明 `Text`、纯公式 `MathTex`，依实际环境检查字体和 LaTeX。

## 检查命令

```bash
python scripts/discover_scene.py path/to/scene.py
python -m py_compile path/to/scene.py
manim -pql path/to/scene.py ActualSceneClass
```

第三条需要已安装的 Manim/字体/LaTeX，前两条并不代表渲染成功。对外发布前记录经过实际审查的关键帧、版本、命令、输出路径和仍未确认事项。

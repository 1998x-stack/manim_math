# 中文数学短视频版式核查

目标是针对真实 `frame_width` / `frame_height` 与平台遮挡区域安排版面，不把某一种 9:16 坐标范围当作默认正确。每帧主要元素应留左右、安全上/下边距，并为字幕和水印分配独立区域。按 `Mobject.get_left/right/top/bottom()` 核对边界，运动中的极值需额外抽帧。

## 混排例子

```python
from manim import Text, MathTex, VGroup, RIGHT
label = Text("已知：", font="Noto Sans CJK SC")  # 字体存在性需要检查
formula = MathTex(r"a^2+b^2=c^2")
line = VGroup(label, formula).arrange(RIGHT, buff=0.15)
```

这里的代码仅为模式示例；系统未安装对应字体时应选任务环境可用的中文字体。`MathTex` 中的 Unicode 数学符号与 LaTeX 环境兼容性需要实际编译核对；静态 `scan_mathtex.py` 只输出含汉字字面量的可疑行，不解析运行期拼接字符串。

## 验收样例

检查标题、最长公式、动画对象最大位移、公式 Transform 后、字幕更换时和片尾。不能使用 `py_compile` 成功替代中文实际字形、公式编译或画面安全区审核。

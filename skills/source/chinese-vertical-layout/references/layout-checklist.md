# ManimGX 中文数学短视频版式核查

目标是针对真实像素宽高、推导后的 `frame_width` / `frame_height` 与平台遮挡区域安排版面。ManimGX 的 `frame_width` 不直接赋值；对仓库标准竖屏使用统一 render profile，再按实际 Mobject bbox 验证左右、安全上/下边距，并为字幕与水印分配独立区域。运动中的极值、公式 Transform 中段和动态坐标系需额外检查。

## 混排例子

```python
from manimgx import MathTex, RIGHT, VGroup
from manim_math_gx import cjk_text

label = cjk_text("已知：")
formula = MathTex(r"a^2+b^2=c^2")
line = VGroup(label, formula).arrange(RIGHT, buff=0.15)
```

普通中文使用 `Text`/`cjk_text()`；不要把汉字塞进 `MathTex` 期待旧 LaTeX CJK package 接管。ManimGX 的 `MathTex`/`Tex` 走 mitex→Typst：`
TexTemplate`、`\\usepackage`、`\\newcommand`、`\\def`、复杂 LaTeX environment 或依赖精确 glyph path 的公式变换必须人工重写并用实际输出验证。静态 `scan_mathtex.py` 只输出含汉字字面量的可疑行，不解析运行期拼接字符串，也不能证明 Typst 最终排版正确。

## 验收顺序

```bash
python -m py_compile path/to/scene.py
ty check path/to/scene.py
manimgx inspect path/to/scene.py ActualScene -t 0,end
manimgx render path/to/scene.py ActualScene -r 270x480 --fps 15 -o preview.mp4
```

至少检查标题、最长公式、动画对象最大位移、公式 Transform 中段、字幕更换和片尾。`py_compile`/`ty` 只证明源码与类型层；首尾 inspect 只证明指定时刻。正式发布前仍需真实关键帧和目标分辨率视频审核。

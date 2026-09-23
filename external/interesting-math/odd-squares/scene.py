"""奇数之和：用逐层 L 形方格证明 1+3+...+(2n-1)=n²。

Render: manim -pql external/interesting-math/odd-squares/scene.py OddSquaresScene
"""
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"  # 预览前确认已安装中文字体
BACKGROUND = "#101827"
PALETTE = (BLUE_C, TEAL_C, GREEN_C, GOLD_C, PURPLE_C)


def odd_layer(n):
    """第 n 层新增的 2n-1 个格点；n 从 1 开始。"""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return [(n - 1, j) for j in range(n)] + [(i, n - 1) for i in range(n - 1)]


def odd_sum(n):
    """独立求和，以便测试等式，而非直接返回 n*n。"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return sum(2 * k - 1 for k in range(1, n + 1))


class OddSquaresScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        title = Text("奇数为什么能拼出正方形？", font=FONT, font_size=34).move_to(UP * 6.3)
        hint = Text("每次沿两条边，加上一层新的方格", font=FONT, font_size=25).move_to(UP * 4.9)
        formula = MathTex("0=0^2", font_size=40).move_to(DOWN * 3.0)
        self.play(Write(title), FadeIn(hint), Write(formula))
        cell_size = 0.69
        for n in range(1, 6):
            cells = VGroup(*[
                Square(side_length=cell_size * 0.96, stroke_width=1.5,
                       stroke_color=BACKGROUND, fill_color=PALETTE[n - 1], fill_opacity=0.95)
                .move_to(np.array([(x - 2) * cell_size, (y - 2) * cell_size + 0.7, 0]))
                for x, y in odd_layer(n)
            ])
            next_formula = MathTex(
                "+".join(str(2 * k - 1) for k in range(1, n + 1)) + "=" + str(n) + "^2",
                font_size=35,
            ).move_to(DOWN * 3.0)
            self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.12) for c in cells],
                                  lag_ratio=0.08), Transform(formula, next_formula), run_time=1.5)
            self.wait(0.45)
        conclusion = MathTex(r"\sum_{k=1}^{n}(2k-1)=n^2", font_size=41).move_to(DOWN * 5.15)
        self.play(Write(conclusion))
        self.wait(2)

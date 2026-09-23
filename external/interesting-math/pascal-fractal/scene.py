"""杨辉三角形奇偶染色：先展示递推，再出现谢尔宾斯基式图案。

Render: manim -pql external/interesting-math/pascal-fractal/scene.py PascalFractalScene
"""
from math import comb
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def pascal_row(n):
    """返回杨辉三角形第 n 行（从 n=0 开始）。"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return [comb(n, k) for k in range(n + 1)]


def parity_row(n):
    return [value % 2 for value in pascal_row(n)]


class PascalFractalScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        title = Text("杨辉三角形里有分形？", font=FONT, font_size=35).move_to(UP * 6.35)
        lead = Text("只看奇偶：奇数亮，偶数暗", font=FONT, font_size=27).move_to(UP * 5.2)
        recurrence = MathTex(r"\binom nk=\binom{n-1}{k-1}+\binom{n-1}{k}",
                             font_size=32).move_to(DOWN * 4.3)
        self.play(Write(title), FadeIn(lead), Write(recurrence))
        rows = []
        for n in range(32):
            dots = VGroup(*[
                Dot(point=np.array([(k - n / 2) * 0.21, 3.9 - n * 0.213, 0]),
                    radius=0.073, color=TEAL_C if odd else GREY_E,
                    fill_opacity=1 if odd else 0.22)
                for k, odd in enumerate(parity_row(n))
            ])
            rows.append(dots)
        stage = Text("前 8 行", font=FONT, font_size=24).move_to(DOWN * 3.45)
        self.play(FadeIn(stage), LaggedStart(*[FadeIn(row) for row in rows[:8]],
                                            lag_ratio=0.12), run_time=2)
        for first, last, caption in ((8, 16, "前 16 行"), (16, 32, "前 32 行")):
            next_stage = Text(caption, font=FONT, font_size=24).move_to(DOWN * 3.45)
            self.play(FadeIn(VGroup(*rows[first:last])), Transform(stage, next_stage),
                      run_time=1.5)
            self.wait(0.5)
        explanation = Text("局部三角形重复出现：自相似", font=FONT,
                           font_size=25, color=TEAL_C).move_to(DOWN * 5.65)
        self.play(FadeIn(explanation))
        self.wait(2)

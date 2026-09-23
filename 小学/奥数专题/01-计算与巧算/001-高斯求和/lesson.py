"""高斯求和：三角点阵拼成长方形，再推广到首尾配对。"""
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def arithmetic_sum(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return n * (n + 1) // 2


class GaussPairingScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("高斯求和：三角形变长方形", font=FONT, font_size=34).move_to(UP * 6.25)
        question = MathTex(r"1+2+\cdots+100=?", font_size=38).move_to(UP * 5.10)
        intro = Text("先把 1 到 10 画成三角点阵", font=FONT, font_size=27).move_to(UP * 4.12)
        self.play(Write(title), Write(question), FadeIn(intro))

        # 10 行分别有 1...10 个蓝点；黄点补齐同一矩形，恰好是反向的一个三角数。
        step, x0, y0 = .51, -2.55, 3.05
        first, second = VGroup(), VGroup()
        for row in range(10):
            for col in range(11):
                p = [x0 + col * step, y0 - row * step, 0]
                dot = Dot(p, radius=.065, color=BLUE_B if col <= row else YELLOW)
                (first if col <= row else second).add(dot)
        frame = Rectangle(width=11 * step, height=10 * step, color=GREY_B, stroke_width=2)
        frame.move_to([x0 + 5 * step, y0 - 4.5 * step, 0])
        self.play(LaggedStart(*(FadeIn(d) for d in first), lag_ratio=.016), run_time=2.2)
        small = MathTex(r"S_{10}=1+2+\cdots+10=55", font_size=32, color=BLUE_B).move_to(DOWN * 2.80)
        self.play(Write(small))
        self.play(Create(frame), LaggedStart(*(FadeIn(d) for d in second), lag_ratio=.012), run_time=2.0)
        doubled = MathTex(r"2S_{10}=10\times11=110", font_size=34, color=YELLOW).move_to(DOWN * 3.83)
        self.play(Write(doubled))
        self.wait(.7)
        self.play(FadeOut(VGroup(first, second, frame, intro, small, doubled)))

        # 这里确实生成 50 个彩色配对条，每条表示一对 i+(101-i)=101。
        pairs = VGroup()
        for k in range(50):
            row, col = divmod(k, 10)
            x, y = -3.0 + col * .65, 3.2 - row * .66
            a = Line([x - .20, y, 0], [x, y, 0], color=BLUE_B, stroke_width=9)
            b = Line([x, y, 0], [x + .20, y, 0], color=YELLOW, stroke_width=9)
            pairs.add(VGroup(a, b))
        label = Text("蓝色小段与黄色小段：50 组首尾配对", font=FONT, font_size=25).move_to(DOWN * 1.03)
        ends = MathTex(r"1+100=2+99=\cdots=50+51=101", font_size=29).move_to(DOWN * 2.16)
        formula = MathTex(r"S_{100}=50\times101=5050", font_size=37, color=YELLOW).move_to(DOWN * 3.42)
        general = MathTex(r"1+2+\cdots+n=\frac{n(n+1)}2", font_size=34).move_to(DOWN * 5.10)
        self.play(LaggedStart(*(FadeIn(bar) for bar in pairs), lag_ratio=.025), run_time=2.2)
        self.play(FadeIn(label), Write(ends), Write(formula))
        self.play(Write(general))
        self.wait(2)

"""高斯求和：首尾配对。渲染：manim -r 480,270 -ql lesson.py GaussPairingScene"""
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def arithmetic_sum(n: int) -> int:
    """计算 1+...+n；只接受正整数。"""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return n * (n + 1) // 2


class GaussPairingScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        title = Text("高斯求和：首尾配对", font=FONT, font_size=35).move_to(UP * 6.25)
        question = MathTex(r"1+2+3+\cdots+100=?", font_size=38).move_to(UP * 4.7)
        self.play(Write(title), FadeIn(question))
        self.wait(1)

        # 实际仅展示前五组；不把示意组数误称为完整求和。
        lines = VGroup()
        for i in range(1, 6):
            pair = MathTex(f"{i}+{101-i}=101", font_size=35)
            pair.set_color(BLUE_B if i % 2 else GREEN_B)
            lines.add(pair)
        lines.arrange(DOWN, buff=0.34).move_to(UP * 1.4)
        self.play(LaggedStart(*(FadeIn(line, shift=RIGHT * 0.2) for line in lines), lag_ratio=0.18))
        self.wait(0.8)
        note = Text("像这样配对，一共有 50 组", font=FONT, font_size=28).move_to(DOWN * 1.7)
        result = MathTex(r"S=50\times101=5050", font_size=39, color=YELLOW).move_to(DOWN * 3.0)
        self.play(FadeIn(note), Write(result))
        self.wait(1.4)
        general = MathTex(r"1+2+\cdots+n=\frac{n(n+1)}{2}", font_size=34)
        general.move_to(DOWN * 4.4)
        self.play(Write(general))
        self.wait(2)

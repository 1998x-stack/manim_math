"""六年级下 · 有理数大小比较，五组数轴示例覆盖同号、异号和分数。"""
from fractions import Fraction
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def compare_rationals(left, right):
    """独立数学函数：支持整数、有限小数和 Fraction；返回 -1/0/1。"""
    a = Fraction(str(left))
    b = Fraction(str(right))
    return (a > b) - (a < b)


class 有理数的大小比较Animation(Scene):
    """保留已有中文 Scene 入口。所有标签和点由同一数值对驱动。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font_size=19, color=GRAY_B).move_to(UP * 6.7)
        title = Text("有理数的大小比较", font_size=38, color=YELLOW).move_to(UP * 5.5)
        self.play(FadeIn(author), Write(title))
        axis = NumberLine(x_range=[-4, 4, 1], length=7,
                          include_numbers=True, font_size=22,
                          include_tip=True, color=BLUE)
        axis.shift(UP * 1.5 - axis.n2p(0))
        self.play(Create(axis))

        # (左值、右值、左标签、右标签、规则说明)；所有左值都严格小于右值。
        comparisons = [
            (-2, 0, "-2", "0", "负数小于零"),
            (0, 1, "0", "1", "正数大于零"),
            (1, 3, "1", "3", "两个正数：绝对值大的数更大"),
            (-3, -1, "-3", "-1", "两个负数：绝对值大的数反而更小"),
            (0.5, 1.5, r"\frac{1}{2}", r"\frac{3}{2}", "分数也可以用数轴比较大小"),
        ]
        for left, right, left_tex, right_tex, message in comparisons:
            assert compare_rationals(left, right) == -1
            left_dot = Dot(axis.n2p(left), color=ORANGE, radius=0.12)
            right_dot = Dot(axis.n2p(right), color=GREEN, radius=0.12)
            left_label = MathTex(left_tex, font_size=27, color=ORANGE)
            left_label.next_to(left_dot, UP, buff=0.2)
            right_label = MathTex(right_tex, font_size=27, color=GREEN)
            right_label.next_to(right_dot, UP, buff=0.2)
            indicator = Arrow(axis.n2p(left) + UP * 0.75,
                              axis.n2p(right) + UP * 0.75,
                              buff=0, color=YELLOW, stroke_width=4)
            picture = VGroup(left_dot, right_dot, left_label, right_label, indicator)
            formula = MathTex(left_tex + "<" + right_tex,
                              font_size=36, color=WHITE).move_to(DOWN * 1.8)
            explanation = Text(message, font_size=25, color=YELLOW).move_to(DOWN * 3.3)
            self.play(FadeIn(picture), Write(formula), FadeIn(explanation), run_time=0.8)
            self.wait(0.75)
            self.play(FadeOut(picture), FadeOut(formula), FadeOut(explanation), run_time=0.4)

        rule = Text("同一条数轴上，越靠右的数越大", font_size=28,
                    color=YELLOW).move_to(DOWN * 1.8)
        signs = MathTex(r"-3<-1<0<1<3", font_size=33).move_to(DOWN * 3)
        self.play(FadeIn(rule), Write(signs))
        self.wait(1.3)
        self.play(FadeOut(rule), FadeOut(signs), FadeOut(axis),
                  FadeOut(title), FadeOut(author))


if __name__ == "__main__":
    # manim -pql '005_有理数的大小比较.py' '有理数的大小比较Animation'
    pass

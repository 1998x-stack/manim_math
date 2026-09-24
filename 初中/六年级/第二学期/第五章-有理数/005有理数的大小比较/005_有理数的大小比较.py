"""六年级下 · 有理数大小比较：保留原 (-2,0,1) 示例并补齐同号与分数。"""
from fractions import Fraction
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def compare_rationals(left, right):
    """独立纯数学函数：比较整数、有限小数及分数，返回 -1、0 或 1。"""
    a, b = Fraction(str(left)), Fraction(str(right))
    return (a > b) - (a < b)


class 有理数的大小比较Animation(Scene):
    """保留原有中文 Scene 入口及用于历史回归的带符号示例。"""

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

        # 保留既有教学及 tools/tests/test_grade6_gotchas_contract.py 的数据契约。
        values = (-2, 0, 1)
        colors = (ORANGE, YELLOW, GREEN)
        dots = VGroup(*[Dot(axis.n2p(value), color=color, radius=0.12)
                        for value, color in zip(values, colors)])
        original_example = MathTex(r"-2 < 0 < 1", font_size=38).move_to(DOWN * 1.8)
        original_rule = Text("数轴上右边的数大于左边的数", font_size=27,
                             color=YELLOW).move_to(DOWN * 3.3)
        self.play(FadeIn(dots), Write(original_example), FadeIn(original_rule))
        self.wait(1.1)
        self.play(FadeOut(dots), FadeOut(original_example), FadeOut(original_rule))

        # (左值、右值、左标签、右标签、解释)；所有后续示例严格左小右大。
        comparisons = [
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
                              font_size=36).move_to(DOWN * 1.8)
            explanation = Text(message, font_size=25, color=YELLOW).move_to(DOWN * 3.3)
            self.play(FadeIn(picture), Write(formula), FadeIn(explanation), run_time=0.8)
            self.wait(0.8)
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

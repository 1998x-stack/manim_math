"""六年级下册 · 数轴。竖屏 9:16；数值、点与刻度共用一个 NumberLine。"""

from math import sqrt
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def number_line_coordinate(value, unit_length=7 / 8):
    """不依赖 Manim 的数学模型：0 在中央，每增加 1 向右移动一个单位。"""
    if unit_length <= 0:
        raise ValueError("单位长度必须为正")
    return float(value) * unit_length


class NumberLineLesson(Scene):
    """8 镜教学：引入、原点、正方向、单位长度、对应、比较、总结。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.blue = "#3498db"
        self.green = "#2ecc71"
        self.orange = "#e67e22"
        self.purple = "#9b59b6"
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font_size=19, color=GRAY_B)
        self.author.move_to(UP * 6.7)
        self.add(self.author)
        self.show_opening()
        self.show_number_line_intro()
        self.show_element_1_origin()
        self.show_element_2_direction()
        self.show_element_3_unit_length()
        self.show_correspondence()
        self.show_comparison()
        self.show_summary()

    def heading(self, wording, color=YELLOW):
        return Text(wording, font_size=35, color=color).move_to(UP * 5.4)

    def show_opening(self):
        title = self.heading("有理数怎样在直线上排队？")
        examples = VGroup(
            MathTex("-3", color=self.orange),
            MathTex("0", color=self.purple),
            MathTex(r"\frac{1}{2}", color=self.green),
            MathTex("2", color=self.blue),
        ).arrange(RIGHT, buff=0.65).move_to(UP * 2.8)
        self.play(FadeIn(title), FadeIn(examples), run_time=1)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(examples))

    def show_number_line_intro(self):
        title = self.heading("数轴：规定了三个要素的直线", self.blue)
        explanation = Text("原点 · 正方向 · 单位长度", font_size=28).move_to(UP * 3.9)
        # 此时尚未设置单位长度；暂用普通直线，后续整体替换为同一条 NumberLine。
        self.basic_line = Line(LEFT * 3.5 + UP * 1.5, RIGHT * 3.5 + UP * 1.5,
                               color=self.blue, stroke_width=4)
        self.play(Write(title), FadeIn(explanation))
        self.play(Create(self.basic_line))
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(explanation))

    def show_element_1_origin(self):
        title = self.heading("要素一：原点", self.purple)
        self.origin_dot = Dot(UP * 1.5, radius=0.12, color=self.purple)
        self.origin_label = MathTex("0", color=self.purple, font_size=28)
        self.origin_label.next_to(self.origin_dot, DOWN, buff=0.28)
        note = Text("原点表示数 0", font_size=26).move_to(DOWN * 2.2)
        self.play(FadeIn(title), FadeIn(self.origin_dot), FadeIn(self.origin_label))
        self.play(FadeIn(note))
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(note))

    def show_element_2_direction(self):
        title = self.heading("要素二：正方向", self.green)
        arrow = Arrow(LEFT * 3.35 + UP * 2.3, RIGHT * 3.35 + UP * 2.3,
                      buff=0, color=self.green, stroke_width=5)
        note = Text("通常规定向右为正方向", font_size=26).move_to(DOWN * 2.2)
        self.play(FadeIn(title), GrowArrow(arrow))
        self.play(FadeIn(note))
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(note), FadeOut(arrow))

    def show_element_3_unit_length(self):
        title = self.heading("要素三：单位长度", self.orange)
        self.number_line = NumberLine(x_range=[-4, 4, 1], length=7,
                                      include_numbers=False, include_tip=True,
                                      color=self.blue, stroke_width=4)
        self.number_line.move_to(UP * 1.5)
        # 先用真正的数轴替换普通线，再构造依赖刻度位置的所有对象。
        self.play(FadeIn(title), ReplacementTransform(self.basic_line, self.number_line))
        self.origin_dot.move_to(self.number_line.n2p(0))
        self.origin_label.next_to(self.origin_dot, DOWN, buff=0.28)
        self.tick_labels = VGroup()
        for n in range(-4, 5):
            if n == 0:
                continue
            label = MathTex(str(n), font_size=22,
                            color=self.green if n > 0 else self.orange)
            label.next_to(self.number_line.n2p(n), DOWN, buff=0.28)
            self.tick_labels.add(label)
        unit = Line(self.number_line.n2p(0), self.number_line.n2p(1))
        brace = Brace(unit, DOWN, color=self.orange, buff=0.45)
        brace_label = Text("1 个单位长度", font_size=22, color=self.orange)
        brace_label.next_to(brace, DOWN, buff=0.12)
        self.play(FadeIn(self.tick_labels), GrowFromCenter(brace), FadeIn(brace_label))
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(brace), FadeOut(brace_label))

    def show_correspondence(self):
        title = self.heading("每个有理数都有对应的点")
        self.play(FadeIn(title))
        examples = [(2.5, "2.5", self.green),
                    (-1.5, "-1.5", self.orange),
                    (0.5, r"\frac{1}{2}", YELLOW)]
        shown = VGroup()
        for value, label_text, color in examples:
            dot = Dot(self.number_line.n2p(value), color=color, radius=0.11)
            label = MathTex(label_text, font_size=25, color=color)
            label.next_to(dot, UP, buff=0.22)
            shown.add(dot, label)
            self.play(FadeIn(dot), FadeIn(label), run_time=0.5)
        equal_values = MathTex(r"-\frac{3}{2}=-1.5", font_size=29,
                               color=self.orange).move_to(DOWN * 2.5)
        self.play(FadeIn(equal_values))
        self.wait(0.7)
        self.play(FadeOut(shown), FadeOut(equal_values), FadeOut(title))
        # 正确区分：有理数对应的点只是数轴上的一部分点。
        irrational_dot = Dot(self.number_line.n2p(sqrt(2)), color=YELLOW, radius=0.11)
        irrational_label = MathTex(r"\sqrt{2}", font_size=28, color=YELLOW)
        irrational_label.next_to(irrational_dot, UP, buff=0.25)
        note = Text("数轴上也有无理数对应的点", font_size=26).move_to(DOWN * 2.5)
        self.play(FadeIn(irrational_dot), FadeIn(irrational_label), FadeIn(note))
        self.wait(0.9)
        self.play(FadeOut(irrational_dot), FadeOut(irrational_label), FadeOut(note))

    def show_comparison(self):
        title = self.heading("数轴上：右边的数大于左边的数")
        self.play(FadeIn(title))
        for left_value, right_value, expression in [
            (-1, 2, "2>-1"), (-3, -2, "-2>-3")
        ]:
            assert left_value < right_value
            left_dot = Dot(self.number_line.n2p(left_value), color=self.orange, radius=0.12)
            right_dot = Dot(self.number_line.n2p(right_value), color=self.green, radius=0.12)
            arrow = Arrow(self.number_line.n2p(left_value) + UP * 0.75,
                          self.number_line.n2p(right_value) + UP * 0.75,
                          buff=0, color=YELLOW)
            formula = MathTex(expression, font_size=37).move_to(DOWN * 2.6)
            self.play(FadeIn(left_dot), FadeIn(right_dot), GrowArrow(arrow))
            self.play(Write(formula))
            self.wait(0.5)
            self.play(FadeOut(left_dot), FadeOut(right_dot), FadeOut(arrow), FadeOut(formula))
        # 动态点只移动同一个对象，无每帧重编译 LaTeX 或临时 FadeOut。
        dot = Dot(self.number_line.n2p(-3), radius=0.14, color=YELLOW)
        tip = Text("从 -3 向右移动到 3", font_size=26).move_to(DOWN * 2.6)
        self.play(FadeIn(dot), FadeIn(tip))
        self.play(dot.animate.move_to(self.number_line.n2p(3)), run_time=2.1)
        self.wait(0.4)
        self.play(FadeOut(dot), FadeOut(tip), FadeOut(title))

    def show_summary(self):
        title = self.heading("数轴知识回顾", self.blue)
        bullets = VGroup(
            Text("原点、正方向、单位长度", font_size=28),
            Text("有理数都可以在数轴上表示", font_size=26),
            Text("右边的数大于左边的数", font_size=26),
        ).arrange(DOWN, buff=0.5).move_to(DOWN * 2.6)
        self.play(FadeIn(title), FadeIn(bullets))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(bullets), FadeOut(self.number_line),
                  FadeOut(self.tick_labels), FadeOut(self.origin_dot),
                  FadeOut(self.origin_label), FadeOut(self.author))

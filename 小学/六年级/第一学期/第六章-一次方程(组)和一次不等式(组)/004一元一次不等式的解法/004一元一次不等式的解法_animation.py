"""六年级一元一次不等式：等价变形、符号反向与解集的数轴表示。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"
RED_ACCENT = "#fb7185"


def solve_linear_inequality(a, b, c, relation):
    """解 ax+b 与 c 的严格/非严格不等式，负系数时反转不等号。"""
    from fractions import Fraction

    if any(type(v) not in (int, Fraction) for v in (a, b, c)) or a == 0:
        raise ValueError("系数须为精确数且 a 非零")
    if relation not in (">", "<", ">=", "<="):
        raise ValueError("不支持的不等号")
    boundary = (Fraction(c) - Fraction(b)) / Fraction(a)
    if a < 0:
        relation = {">": "<", "<": ">", ">=": "<=", "<=": ">="}[relation]
    return relation, boundary


class Topic004一元一次不等式的解法Animation(Scene):
    """从 2x+3>7 走到 x>2，用空心圆和箭头表达整个解集。"""

    def construct(self):
        assert solve_linear_inequality(2, 3, 7, ">") == (">", 2)
        assert solve_linear_inequality(-2, 3, 7, ">") == ("<", -2)
        assert solve_linear_inequality(2, 3, 7, ">=") == (">=", 2)
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm", font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.solve_positive_example()
        self.show_number_line()
        self.negative_coefficient()
        self.summary()

    def transition(self):
        self.play(
            *[FadeOut(m) for m in list(self.mobjects) if m is not self.watermark],
            run_time=0.3
        )

    def heading(self, name):
        label = Text(name, font_size=36, color=GOLD).move_to(UP * 5.65)
        self.play(Write(label), run_time=0.5)
        return label

    def opening(self):
        title = Text("一元一次不等式的解法", font_size=43).move_to(UP * 3)
        subtitle = Text("解不是一个数，而是一个范围", font_size=27, color=BLUE_ACCENT)
        subtitle.next_to(title, DOWN, buff=0.6)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(0.7)
        self.transition()

    def solve_positive_example(self):
        self.heading("例一：不等号方向不变")
        start = MathTex(r"2x+3>7", font_size=53).move_to(UP * 3.3)
        self.play(Write(start))
        stages = [
            ("两边同时减去 3", r"2x>4"),
            ("两边同时除以正数 2", r"x>2"),
        ]
        current = None
        explanation = None
        for reason, formula in stages:
            if current is not None:
                self.play(FadeOut(current), FadeOut(explanation), run_time=0.25)
            explanation = Text(reason, font_size=28, color=BLUE_ACCENT).move_to(UP * 1)
            current = MathTex(formula, font_size=54, color=GREEN_ACCENT).move_to(DOWN * 0.3)
            self.play(Write(current), FadeIn(explanation))
            self.wait(0.45)
        test = VGroup(
            Text("检验：3 是解，2 不是解", font_size=26),
            MathTex(r"2\times3+3=9>7", font_size=37, color=GOLD),
            MathTex(r"2\times2+3=7", font_size=37),
        ).arrange(DOWN, buff=0.28).move_to(DOWN * 2.7)
        self.play(LaggedStart(*(FadeIn(m) for m in test), lag_ratio=0.2))
        self.wait(0.7)
        self.transition()

    def show_number_line(self):
        self.heading("数轴表示：空心圆")
        number_line = NumberLine(
            x_range=[-3, 5, 1], length=7.2,
            include_numbers=True, include_tip=False
        ).move_to(UP * 1)
        self.play(Create(number_line))
        point = number_line.n2p(2)
        open_circle = Circle(
            radius=0.11, stroke_color=GOLD, stroke_width=4,
            fill_color=BG, fill_opacity=1
        ).move_to(point)
        ray = Arrow(
            start=number_line.n2p(2.2), end=number_line.n2p(4.6),
            buff=0, stroke_width=5, color=GREEN_ACCENT
        )
        self.play(Create(open_circle), GrowArrow(ray))
        note = MathTex(r"x>2", font_size=52, color=GOLD).move_to(DOWN * 1.7)
        caution = Text("空心：不包含 2；向右：大于 2", font_size=25)
        caution.move_to(DOWN * 3)
        self.play(Write(note), FadeIn(caution))
        self.wait(0.7)
        self.transition()

    def negative_coefficient(self):
        self.heading("例二：除以负数要反向")
        original = MathTex(r"-2x+3>7", font_size=49).move_to(UP * 3.3)
        self.play(Write(original))
        intermediate = MathTex(r"-2x>4", font_size=48).move_to(UP * 1)
        self.play(Write(intermediate))
        explanation = Text("两边除以 -2，不等号反向！", font_size=28, color=RED_ACCENT)
        explanation.move_to(DOWN * 0.4)
        answer = MathTex(r"x<-2", font_size=53, color=GREEN_ACCENT)
        answer.move_to(DOWN * 1.7)
        self.play(FadeIn(explanation), Write(answer))
        self.wait(0.8)
        self.transition()

    def summary(self):
        self.heading("不等式的解集")
        rows = VGroup(
            Text("同加、同减：方向不变", font_size=29),
            Text("乘除正数：方向不变", font_size=29),
            Text("乘除负数：不等号反向", font_size=29, color=RED_ACCENT),
            Text("空心圆不含端点，实心圆含端点", font_size=26),
        ).arrange(DOWN, buff=0.65).move_to(UP * 0.7)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
        self.wait(0.9)

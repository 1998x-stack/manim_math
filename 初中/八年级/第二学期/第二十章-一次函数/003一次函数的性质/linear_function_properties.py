"""一次函数的性质：单调性、k/b 的符号及真实象限。"""
from math import isfinite
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def visible_interval(k, b, margin=0.04):
    """返回在 [-3,3]×[-3,3] 窗口内的非退化可见直线段的 x 区间。"""
    if not isfinite(k) or not isfinite(b) or not isfinite(margin) or k == 0 or margin < 0:
        raise ValueError("需要有限的非零斜率、有限截距及非负边距")
    crossings = ((-3 - b) / k, (3 - b) / k)
    left = max(-3, min(crossings)) + margin
    right = min(3, max(crossings)) - margin
    if right <= left:
        raise ValueError("直线与可视坐标窗口没有足够长的交集")
    return [left, right]


def quadrant(x, y):
    """返回 1..4；坐标轴上的点返回 0（不属于任何象限）。"""
    if x == 0 or y == 0:
        return 0
    return (1 if y > 0 else 4) if x > 0 else (2 if y > 0 else 3)


def quadrants_for(k, b):
    """在定义域为全体实数、k≠0 的条件下判断直线经过的象限。"""
    if not isfinite(k) or not isfinite(b) or k == 0:
        raise ValueError("一次函数要求有限实数 k≠0、b")
    if b == 0:
        return (1, 3) if k > 0 else (2, 4)
    if k > 0:
        return (1, 2, 3) if b > 0 else (1, 3, 4)
    return (1, 2, 4) if b > 0 else (2, 3, 4)


class LinearFunctionProperties(Scene):
    """七镜：引入→坐标系→递增→递减→象限→对比→结尾。"""

    POSITIVE = "#3498db"
    NEGATIVE = "#e74c3c"
    PURPLE = "#9b59b6"
    ORANGE = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.show_opening()
        self.setup_coordinate_system()
        self.show_k_positive_property()
        self.show_k_negative_property()
        self.show_quadrant_relationships()
        self.show_comparison_summary()
        self.show_outro()

    def label(self, content, y, color=WHITE, size=27):
        result = Text(content, font_size=size, color=color).move_to([0, y, 0])
        if result.width > 7.7:
            result.scale_to_fit_width(7.7)
        return result

    def graph(self, k, b, color):
        return self.axes.plot(lambda x: k * x + b,
                              x_range=visible_interval(k, b),
                              color=color, stroke_width=4)

    def show_opening(self):
        self.author_info = self.label("上海初高中数学直通车 @emptyandcalm", 7.0,
                                      GRAY_B, 20)
        question = self.label("k 的正负，会怎样改变函数图像？", 2.0, YELLOW, 39)
        formula = MathTex(r"y=kx+b\quad(k\ne0)", font_size=45)
        self.play(FadeIn(self.author_info), Write(question), run_time=0.8)
        self.play(Write(formula), run_time=0.8)
        self.wait(0.4)
        self.play(FadeOut(question), FadeOut(formula), run_time=0.5)

    def setup_coordinate_system(self):
        self.axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                         x_length=6.2, y_length=6.2, tips=False,
                         axis_config={"include_numbers": False, "stroke_width": 2})
        self.axes.move_to(UP * 0.65)
        x_label = MathTex("x", font_size=24).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        y_label = MathTex("y", font_size=24).next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        origin = Text("O", font_size=20).next_to(self.axes.c2p(0, 0), DL, buff=0.1)
        self.axis_group = VGroup(self.axes, x_label, y_label, origin)
        self.play(Create(self.axes), FadeIn(x_label), FadeIn(y_label), FadeIn(origin),
                  run_time=1)

    def demonstrate(self, k, b, color, formula_tex, property_text):
        """同一组数值驱动移动点、x/y 数字及单调性箭头。"""
        formula = MathTex(formula_tex, color=color, font_size=39).move_to(UP * 5.5)
        line = self.graph(k, b, color)
        self.play(Write(formula), Create(line), run_time=1.1)
        tracker = ValueTracker(-1.5)
        moving_dot = always_redraw(lambda: Dot(
            self.axes.c2p(tracker.get_value(), k * tracker.get_value() + b),
            radius=0.1, color=YELLOW))
        x_name = MathTex("x=", font_size=28).move_to([-2.0, -4.65, 0])
        y_name = MathTex("y=", font_size=28).move_to([1.3, -4.65, 0])
        x_num = DecimalNumber(-1.5, num_decimal_places=1, font_size=28)
        y_num = DecimalNumber(k * -1.5 + b, num_decimal_places=1, font_size=28)
        x_num.next_to(x_name, RIGHT, buff=0.12)
        y_num.next_to(y_name, RIGHT, buff=0.12)
        x_num.add_updater(lambda obj: obj.set_value(tracker.get_value()))
        y_num.add_updater(lambda obj: obj.set_value(k * tracker.get_value() + b))
        note = self.label(property_text, -5.8, color, 29)
        self.add(moving_dot, x_name, y_name, x_num, y_num)
        self.play(tracker.animate.set_value(1.5), run_time=2, rate_func=linear)
        # 箭头左右均向右：k>0 时上升，k<0 时下降。
        arrow = Arrow(self.axes.c2p(-1.5, k * -1.5 + b),
                      self.axes.c2p(1.5, k * 1.5 + b),
                      buff=0.15, color=color, stroke_width=5)
        self.play(GrowArrow(arrow), FadeIn(note), run_time=0.7)
        self.wait(0.5)
        x_num.clear_updaters()
        y_num.clear_updaters()
        self.play(FadeOut(line), FadeOut(formula), FadeOut(moving_dot),
                  FadeOut(x_name), FadeOut(y_name), FadeOut(x_num), FadeOut(y_num),
                  FadeOut(arrow), FadeOut(note), run_time=0.5)

    def show_k_positive_property(self):
        self.demonstrate(1, 1, self.POSITIVE, r"y=x+1\quad(k=1>0)",
                         "x 增大，y 增大：单调递增")

    def show_k_negative_property(self):
        self.demonstrate(-1, 1, self.NEGATIVE, r"y=-x+1\quad(k=-1<0)",
                         "x 增大，y 减小：单调递减")

    def show_quadrant_relationships(self):
        title = self.label("改变 k 和 b 的符号：直线经过哪些象限？", 5.5, YELLOW, 29)
        self.play(FadeIn(title), run_time=0.4)
        cases = (
            (1, 1, r"y=x+1", self.POSITIVE),
            (1, -1, r"y=x-1", self.PURPLE),
            (-1, 1, r"y=-x+1", self.NEGATIVE),
            (-1, -1, r"y=-x-1", self.ORANGE),
        )
        for k, b, expression, color in cases:
            line = self.graph(k, b, color)
            expected = quadrants_for(k, b)
            marks = VGroup()
            shown = set()
            for x in (-2.5, -0.5, 0.5, 2.5):
                y = k * x + b
                q = quadrant(x, y)
                if q in expected and q not in shown and -2.8 < y < 2.8:
                    marks.add(Dot(self.axes.c2p(x, y), radius=0.08, color=YELLOW))
                    shown.add(q)
            if shown != set(expected):
                raise ValueError(f"当前示例点未覆盖所有象限: {expression}")
            expression_label = MathTex(expression, font_size=36, color=color).move_to(DOWN * 4.5)
            quadrant_text = self.label("经过第 " + "、".join(str(q) for q in expected) + " 象限",
                                       -5.6, color, 28)
            self.play(Create(line), FadeIn(marks), FadeIn(expression_label),
                      FadeIn(quadrant_text), run_time=0.85)
            self.wait(0.65)
            self.play(FadeOut(line), FadeOut(marks), FadeOut(expression_label),
                      FadeOut(quadrant_text), run_time=0.4)
        zero_note = self.label("特别地：b=0 时直线过原点，原点不属于任何象限", -5.4, YELLOW, 26)
        line_pos = self.graph(1, 0, self.POSITIVE)
        line_neg = self.graph(-1, 0, self.NEGATIVE)
        zero_formulas = VGroup(MathTex(r"y=x:\ \mathrm{I,III}", color=self.POSITIVE,
                                       font_size=26),
                               MathTex(r"y=-x:\ \mathrm{II,IV}", color=self.NEGATIVE,
                                       font_size=26)).arrange(DOWN, buff=0.2).move_to(DOWN * 4.1)
        self.play(Create(line_pos), Create(line_neg), FadeIn(zero_formulas),
                  FadeIn(zero_note), run_time=0.9)
        self.wait(0.8)
        self.play(FadeOut(line_pos), FadeOut(line_neg), FadeOut(zero_formulas),
                  FadeOut(zero_note), FadeOut(title), run_time=0.5)

    def show_comparison_summary(self):
        self.play(FadeOut(self.axis_group), run_time=0.5)
        left = RoundedRectangle(width=3.9, height=5.1, corner_radius=0.2,
                                color=self.POSITIVE, fill_opacity=0.08)
        right = RoundedRectangle(width=3.9, height=5.1, corner_radius=0.2,
                                 color=self.NEGATIVE, fill_opacity=0.08)
        left.move_to(LEFT * 2.0)
        right.move_to(RIGHT * 2.0)
        left_title = self.label("k > 0", 1.9, self.POSITIVE, 37).shift(LEFT * 2.0)
        right_title = self.label("k < 0", 1.9, self.NEGATIVE, 37).shift(RIGHT * 2.0)
        # 箭头从左至右，正斜率右上，负斜率右下；不再把上升箭头指向下方。
        up = Arrow([-2.95, -0.7, 0], [-1.05, 0.8, 0], color=self.POSITIVE, buff=0)
        down = Arrow([1.05, 0.8, 0], [2.95, -0.7, 0], color=self.NEGATIVE, buff=0)
        left_note = self.label("单调递增", -1.65, self.POSITIVE, 26).shift(LEFT * 2.0)
        right_note = self.label("单调递减", -1.65, self.NEGATIVE, 26).shift(RIGHT * 2.0)
        conclusion = self.label("单调性只由非零斜率 k 的符号决定", -4.8, YELLOW, 28)
        group = VGroup(left, right, left_title, right_title, up, down,
                       left_note, right_note, conclusion)
        self.play(FadeIn(left), FadeIn(right), FadeIn(left_title), FadeIn(right_title),
                  run_time=0.6)
        self.play(GrowArrow(up), GrowArrow(down), FadeIn(left_note),
                  FadeIn(right_note), FadeIn(conclusion), run_time=0.8)
        self.wait(1.1)
        self.play(FadeOut(group), run_time=0.5)

    def show_outro(self):
        ending = self.label("一次函数的性质 · @emptyandcalm", 0, YELLOW, 34)
        self.play(FadeOut(self.author_info), FadeIn(ending), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(ending), run_time=0.4)


# manim -ql linear_function_properties.py LinearFunctionProperties

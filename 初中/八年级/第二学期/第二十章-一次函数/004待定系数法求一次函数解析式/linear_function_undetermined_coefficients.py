"""待定系数法求一次函数解析式：两点→方程组→验证→同源绘图。"""
from fractions import Fraction
from math import isfinite
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def solve_from_points(point_a, point_b):
    """精确求解两点确定的 y=kx+b；只接受本课所指的 k≠0 一次函数。"""
    if len(point_a) != 2 or len(point_b) != 2:
        raise ValueError("点必须各有两个坐标")
    if not all(isfinite(float(v)) for v in (*point_a, *point_b)):
        raise ValueError("坐标必须为有限实数")
    x_a, y_a = (Fraction(v) for v in point_a)
    x_b, y_b = (Fraction(v) for v in point_b)
    if x_a == x_b:
        raise ValueError("两点横坐标相同，不能确定 y=kx+b 形式的唯一一次函数")
    k = (y_b - y_a) / (x_b - x_a)
    if k == 0:
        raise ValueError("两点纵坐标相同，只能确定常值函数，不满足本课 k≠0")
    b = y_a - k * x_a
    assert k * x_a + b == y_a and k * x_b + b == y_b
    return k, b


def visible_interval(k, b, x_bounds=(-1.0, 5.0), y_bounds=(-1.0, 9.0), margin=0.04):
    """剪裁可见图像，避免端点触及坐标轴边界或绘出窗口。"""
    if not all(isfinite(float(v)) for v in (k, b, *x_bounds, *y_bounds, margin)):
        raise ValueError("参数和边界必须有限")
    if k == 0 or margin < 0 or x_bounds[0] >= x_bounds[1] or y_bounds[0] >= y_bounds[1]:
        raise ValueError("参数不合法")
    crossings = ((y_bounds[0] - b) / k, (y_bounds[1] - b) / k)
    start = max(x_bounds[0], min(crossings)) + margin
    stop = min(x_bounds[1], max(crossings)) - margin
    if stop <= start:
        raise ValueError("直线与窗口无非退化可见部分")
    return [float(start), float(stop)]


class LinearFunctionUndeterminedCoefficients(Scene):
    """七镜：题目→坐标→设式→代点 A→代点 B→求解与检验→总结。"""

    GREEN_A = "#2ecc71"
    PURPLE_B = "#9b59b6"
    BLUE_LINE = "#3498db"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.point_a = (1, 3)
        self.point_b = (3, 7)
        self.k, self.b = solve_from_points(self.point_a, self.point_b)
        self.scene_1_opening()
        self.scene_2_setup_axes()
        self.scene_3_introduce_method()
        self.scene_4_substitute_point_a()
        self.scene_5_substitute_point_b()
        self.scene_6_solve_and_draw()
        self.scene_7_summary()

    def text_at(self, content, y, size=28, color=WHITE):
        label = Text(content, font_size=size, color=color).move_to([0, y, 0])
        if label.width > 7.7:
            label.scale_to_fit_width(7.7)
        return label

    def scene_1_opening(self):
        self.author_info = self.text_at("上海初高中数学直通车 @emptyandcalm",
                                        7.0, size=20, color=GRAY_B)
        title = self.text_at("给定两点，怎样求一次函数解析式？", 5.5,
                              size=32, color=YELLOW)
        a = MathTex(r"A(1,3)", color=self.GREEN_A, font_size=39).move_to(LEFT * 1.7)
        b = MathTex(r"B(3,7)", color=self.PURPLE_B, font_size=39).move_to(RIGHT * 1.7)
        self.play(FadeIn(self.author_info), Write(title), run_time=0.8)
        self.play(FadeIn(a), FadeIn(b), run_time=0.6)
        self.wait(0.4)
        self.play(FadeOut(title), FadeOut(a), FadeOut(b), run_time=0.4)

    def scene_2_setup_axes(self):
        self.axes = Axes(x_range=[-1, 5, 1], y_range=[-1, 9, 1],
                         x_length=6, y_length=7, tips=False,
                         axis_config={"include_numbers": False, "stroke_width": 2})
        self.axes.move_to(UP * 0.3)
        x_label = Text("x", font_size=23).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        y_label = Text("y", font_size=23).next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        self.dot_a = Dot(self.axes.c2p(*self.point_a), color=self.GREEN_A, radius=0.09)
        self.dot_b = Dot(self.axes.c2p(*self.point_b), color=self.PURPLE_B, radius=0.09)
        self.label_a = MathTex(r"A(1,3)", color=self.GREEN_A, font_size=27)
        self.label_b = MathTex(r"B(3,7)", color=self.PURPLE_B, font_size=27)
        self.label_a.next_to(self.dot_a, UL, buff=0.12)
        self.label_b.next_to(self.dot_b, UR, buff=0.12)
        self.coordinate_group = VGroup(self.axes, x_label, y_label,
                                       self.dot_a, self.dot_b, self.label_a, self.label_b)
        self.play(Create(self.axes), FadeIn(x_label), FadeIn(y_label), run_time=0.9)
        self.play(FadeIn(self.dot_a), FadeIn(self.dot_b),
                  FadeIn(self.label_a), FadeIn(self.label_b), run_time=0.6)

    def scene_3_introduce_method(self):
        self.general_formula = MathTex(r"y=kx+b\quad(k\ne0)", font_size=37)
        self.general_formula.move_to(UP * 5.5)
        tip = self.text_at("设解析式；两点横坐标不同，分别代入求 k 和 b", -4.6,
                           size=25, color=YELLOW)
        self.play(Write(self.general_formula), FadeIn(tip), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(tip), run_time=0.3)

    def scene_4_substitute_point_a(self):
        line = MathTex(r"A(1,3):\quad 3=k\cdot1+b\Rightarrow k+b=3",
                       font_size=29, color=self.GREEN_A).move_to(DOWN * 4.7)
        self.play(Indicate(self.dot_a), Write(line), run_time=0.9)
        self.wait(0.5)
        self.equation_a = MathTex(r"\textcircled{1}\quad k+b=3", font_size=30,
                                  color=self.GREEN_A).move_to(DOWN * 4.5)
        self.play(ReplacementTransform(line, self.equation_a), run_time=0.5)

    def scene_5_substitute_point_b(self):
        line = MathTex(r"B(3,7):\quad 7=3k+b", font_size=31,
                       color=self.PURPLE_B).move_to(DOWN * 5.5)
        self.play(Indicate(self.dot_b), Write(line), run_time=0.8)
        self.wait(0.5)
        self.equation_b = MathTex(r"\textcircled{2}\quad3k+b=7", font_size=30,
                                  color=self.PURPLE_B).move_to(DOWN * 5.5)
        self.play(ReplacementTransform(line, self.equation_b), run_time=0.5)

    def scene_6_solve_and_draw(self):
        # 独立数学模型已经验证两点与求得系数完全一致。
        assert self.k == 2 and self.b == 1
        result = MathTex(r"\textcircled{2}-\textcircled{1}:\ 2k=4\Rightarrow k=2",
                         font_size=29, color=YELLOW).move_to(DOWN * 4.5)
        intercept = MathTex(r"k+b=3\Rightarrow b=1", font_size=29,
                            color=YELLOW).move_to(DOWN * 5.4)
        self.play(FadeOut(self.equation_a), FadeOut(self.equation_b),
                  Write(result), run_time=0.8)
        self.play(Write(intercept), run_time=0.7)
        self.wait(0.6)
        self.play(FadeOut(result), FadeOut(intercept),
                  FadeOut(self.general_formula), run_time=0.4)
        self.final_formula = MathTex(r"y=2x+1", font_size=42,
                                     color=self.BLUE_LINE).move_to(UP * 5.5)
        self.function_line = self.axes.plot(lambda x: float(self.k) * x + float(self.b),
                                            x_range=visible_interval(self.k, self.b),
                                            color=self.BLUE_LINE, stroke_width=4)
        self.play(Write(self.final_formula), Create(self.function_line), run_time=1.1)
        verified = self.text_at("代入核对：2×1+1=3，2×3+1=7", -5.1,
                                size=27, color=YELLOW)
        self.play(Indicate(self.dot_a), Indicate(self.dot_b),
                  FadeIn(verified), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(verified), run_time=0.4)

    def scene_7_summary(self):
        self.play(FadeOut(self.coordinate_group), FadeOut(self.function_line),
                  FadeOut(self.final_formula), run_time=0.6)
        cards = VGroup()
        for title, detail in (("第一步", "设 y=kx+b（k≠0）"),
                              ("第二步", "分别代入两点坐标"),
                              ("第三步", "解二元一次方程组"),
                              ("第四步", "代回两点检验解析式")):
            rect = RoundedRectangle(width=7.5, height=1.2, corner_radius=0.15,
                                    color=self.BLUE_LINE, fill_color=self.BLUE_LINE,
                                    fill_opacity=0.1)
            title_text = Text(title, font_size=26, color=YELLOW)
            detail_text = Text(detail, font_size=24, color=WHITE)
            content = VGroup(title_text, detail_text).arrange(RIGHT, buff=0.22)
            if content.width > 6.9:
                content.scale_to_fit_width(6.9)
            cards.add(VGroup(rect, content))
        cards.arrange(DOWN, buff=0.45).move_to(ORIGIN)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.15), run_time=0.4)
        self.wait(0.7)
        self.play(FadeOut(cards), FadeOut(self.author_info), run_time=0.5)


# manim -ql linear_function_undetermined_coefficients.py LinearFunctionUndeterminedCoefficients

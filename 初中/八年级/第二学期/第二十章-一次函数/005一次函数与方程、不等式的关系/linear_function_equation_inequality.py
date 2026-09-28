"""一次函数与方程、不等式：同一零点驱动图像、数轴和代数答案。"""
from math import isfinite
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def zero_of(k, b):
    if not isfinite(k) or not isfinite(b) or k == 0:
        raise ValueError("要求有限实数 k≠0、b")
    return -b / k


def relation_holds(k, b, x, relation):
    """使用同一函数值判断方程和四类不等式，杜绝 k<0 时误用方向。"""
    if relation not in ("=", ">", "<", ">=", "<=") or not isfinite(x):
        raise ValueError("未知关系或非有限 x")
    root = zero_of(k, b)
    difference = x - root
    if relation == "=":
        return difference == 0
    if relation == ">":
        return (difference > 0) if k > 0 else (difference < 0)
    if relation == "<":
        return (difference < 0) if k > 0 else (difference > 0)
    if relation == ">=":
        return (difference >= 0) if k > 0 else (difference <= 0)
    return (difference <= 0) if k > 0 else (difference >= 0)


def visible_interval(k, b, x_bounds=(-1.0, 4.0), y_bounds=(-5.0, 5.0), margin=0.06):
    """返回绘制时严格落在坐标窗口内部的非退化区间。"""
    zero_of(k, b)
    if not all(isfinite(value) for value in (*x_bounds, *y_bounds, margin)):
        raise ValueError("边界必须有限")
    if margin < 0 or x_bounds[0] >= x_bounds[1] or y_bounds[0] >= y_bounds[1]:
        raise ValueError("非法边界")
    crossings = ((y_bounds[0] - b) / k, (y_bounds[1] - b) / k)
    start = max(x_bounds[0], min(crossings)) + margin
    stop = min(x_bounds[1], max(crossings)) - margin
    if start >= stop:
        raise ValueError("线段不在视窗内")
    return [start, stop]


class LinearFunctionEquationInequality(Scene):
    """八镜：引入、作图、求根、正负区间、汇总、包含边界例题、结尾。"""

    LINE_COLOR = "#3498db"
    ABOVE_COLOR = "#2ecc71"
    BELOW_COLOR = "#e74c3c"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.k, self.b = 2, -3
        self.root = zero_of(self.k, self.b)
        self.show_opening()
        self.setup_coordinate_system()
        self.show_equation_solution()
        self.show_inequality_positive()
        self.show_inequality_negative()
        self.show_summary()
        self.show_example()
        self.show_outro()

    def caption(self, content, y=-5.0, color=WHITE, size=27):
        label = Text(content, font_size=size, color=color).move_to([0, y, 0])
        if label.width > 7.6:
            label.scale_to_fit_width(7.6)
        return label

    def f(self, x):
        return self.k * x + self.b

    def line(self, start, stop, color, width=5):
        if stop <= start:
            raise ValueError("不允许零长度图像")
        return self.axes.plot(self.f, x_range=[start, stop],
                              color=color, stroke_width=width)

    def show_opening(self):
        self.author_info = self.caption("上海初高中数学直通车 @emptyandcalm",
                                        y=7, size=20, color=GRAY_B)
        title = self.caption("函数的零点，怎样帮助解方程和不等式？",
                             y=4.8, color=YELLOW, size=31)
        equations = VGroup(MathTex(r"2x-3=0", font_size=39),
                           MathTex(r"2x-3>0", font_size=39),
                           MathTex(r"2x-3<0", font_size=39)).arrange(DOWN, buff=0.5)
        self.play(FadeIn(self.author_info), Write(title), run_time=0.8)
        self.play(FadeIn(equations), run_time=0.7)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(equations), run_time=0.4)

    def setup_coordinate_system(self):
        self.axes = Axes(x_range=[-1, 4, 1], y_range=[-5, 5, 1],
                         x_length=6.5, y_length=7, tips=False,
                         axis_config={"include_numbers": False, "stroke_width": 2})
        self.axes.move_to(UP * 0.4)
        xlabel = Text("x", font_size=24).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.1)
        ylabel = Text("y", font_size=24).next_to(self.axes.y_axis.get_end(), UP, buff=0.1)
        self.axis_group = VGroup(self.axes, xlabel, ylabel)
        start, stop = visible_interval(self.k, self.b)
        self.graph = self.line(start, stop, self.LINE_COLOR, 4)
        self.formula = MathTex(r"y=2x-3", font_size=37,
                               color=self.LINE_COLOR).move_to(UP * 5.4)
        self.play(Create(self.axes), FadeIn(xlabel), FadeIn(ylabel),
                  Write(self.formula), run_time=1.0)
        self.play(Create(self.graph), run_time=0.9)

    def show_equation_solution(self):
        self.root_dot = Dot(self.axes.c2p(self.root, 0), color=YELLOW, radius=0.12)
        root_label = MathTex(r"(\tfrac32,0)", font_size=29, color=YELLOW)
        root_label.next_to(self.root_dot, UP, buff=0.2)
        result = MathTex(r"2x-3=0\quad\Longleftrightarrow\quad x=\tfrac32",
                         font_size=29, color=YELLOW).move_to(DOWN * 4.8)
        tip = self.caption("方程的解，就是直线与 x 轴交点的横坐标", y=-5.7,
                           color=GRAY_A, size=25)
        self.play(FadeIn(self.root_dot), FadeIn(root_label),
                  Write(result), FadeIn(tip), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(root_label), FadeOut(result), FadeOut(tip), run_time=0.4)

    def show_sign(self, positive):
        """高亮 y>0 或 y<0 部分；严格不等号使用空心端点。"""
        low, high = visible_interval(self.k, self.b)
        color = self.ABOVE_COLOR if positive else self.BELOW_COLOR
        start, stop = (self.root + 0.05, high) if positive else (low, self.root - 0.05)
        assert start < stop and relation_holds(self.k, self.b, (start + stop) / 2,
                                                ">" if positive else "<")
        highlighted = self.line(start, stop, color, 7)
        edge = high if positive else low
        wedge = Polygon(self.axes.c2p(self.root, 0),
                        self.axes.c2p(edge, 0),
                        self.axes.c2p(edge, self.f(edge)),
                        fill_color=color, fill_opacity=0.13, stroke_width=0)
        expression = MathTex(r"2x-3>0\ \Longleftrightarrow\ x>\tfrac32" if positive
                             else r"2x-3<0\ \Longleftrightarrow\ x<\tfrac32",
                             font_size=30, color=color).move_to(DOWN * 4.8)
        explanation = self.caption("函数图像在 x 轴上方" if positive
                                   else "函数图像在 x 轴下方", y=-5.75,
                                   color=GRAY_A, size=25)
        axis_origin = self.axes.c2p(self.root, 0) + DOWN * 0.42
        target = self.axes.c2p(3.6 if positive else -0.6, 0) + DOWN * 0.42
        arrow = Arrow(axis_origin, target, buff=0.13, color=color, stroke_width=5)
        boundary = Circle(radius=0.075, color=color, stroke_width=3,
                          fill_opacity=0).move_to(axis_origin)
        self.play(FadeIn(wedge), Create(highlighted), run_time=1.0)
        self.play(Write(expression), FadeIn(explanation),
                  GrowArrow(arrow), FadeIn(boundary), run_time=0.9)
        self.wait(1.0)
        self.play(FadeOut(wedge), FadeOut(highlighted), FadeOut(expression),
                  FadeOut(explanation), FadeOut(arrow), FadeOut(boundary), run_time=0.5)

    def show_inequality_positive(self):
        self.show_sign(True)

    def show_inequality_negative(self):
        self.show_sign(False)

    def show_summary(self):
        self.play(FadeOut(self.axis_group), FadeOut(self.graph),
                  FadeOut(self.formula), FadeOut(self.root_dot), run_time=0.6)
        cards = VGroup()
        for headline, detail, color in (
            ("方程 = 0", "与 x 轴交点的横坐标", YELLOW),
            ("不等式 > 0", "函数图像在 x 轴上方", self.ABOVE_COLOR),
            ("不等式 < 0", "函数图像在 x 轴下方", self.BELOW_COLOR),
        ):
            rect = RoundedRectangle(width=7.4, height=1.45,
                                    corner_radius=0.16, color=color,
                                    fill_color=color, fill_opacity=0.1)
            title = Text(headline, color=color, font_size=27)
            body = Text(detail, color=WHITE, font_size=24)
            contents = VGroup(title, body).arrange(DOWN, buff=0.1)
            cards.add(VGroup(rect, contents))
        cards.arrange(DOWN, buff=0.55).move_to(ORIGIN)
        self.play(FadeIn(cards, lag_ratio=0.2), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(cards), run_time=0.5)

    def show_example(self):
        # ≥ 与 > 的差别在于零点是否计入；画面只显示解集的一部分。
        assert relation_holds(self.k, self.b, self.root, ">=")
        self.play(FadeIn(self.axis_group), FadeIn(self.graph),
                  FadeIn(self.root_dot), run_time=0.8)
        low, high = visible_interval(self.k, self.b)
        segment = self.line(self.root, high, self.ABOVE_COLOR, 7)
        caption = MathTex(r"2x-3\ge0\quad\Longleftrightarrow\quad x\ge\tfrac32",
                          font_size=31, color=self.ABOVE_COLOR).move_to(DOWN * 4.9)
        note = self.caption("端点是实心圆：零点属于解集", y=-5.75,
                            color=YELLOW, size=25)
        axis_origin = self.axes.c2p(self.root, 0) + DOWN * 0.42
        target = self.axes.c2p(3.6, 0) + DOWN * 0.42
        ray = Arrow(axis_origin, target, buff=0.12, color=self.ABOVE_COLOR,
                    stroke_width=5)
        included = Dot(axis_origin, color=self.ABOVE_COLOR, radius=0.08)
        self.play(Create(segment), Write(caption), FadeIn(note),
                  GrowArrow(ray), FadeIn(included), run_time=1.1)
        self.wait(1.0)
        self.play(FadeOut(self.axis_group), FadeOut(self.graph),
                  FadeOut(self.root_dot), FadeOut(segment), FadeOut(caption),
                  FadeOut(note), FadeOut(ray), FadeOut(included), run_time=0.6)

    def show_outro(self):
        ending = self.caption("数形结合 · @emptyandcalm", y=0, color=YELLOW, size=34)
        self.play(FadeOut(self.author_info), FadeIn(ending), run_time=0.6)
        self.wait(0.6)
        self.play(FadeOut(ending), run_time=0.4)


# manim -ql linear_function_equation_inequality.py LinearFunctionEquationInequality

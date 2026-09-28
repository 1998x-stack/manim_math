"""一次函数的图像：保留七镜教学结构，函数、坐标与画面状态使用同一数学模型。"""
from math import isfinite
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def visible_interval(k, b, x_bounds=(-4.0, 4.0), y_bounds=(-3.0, 5.0), margin=0.04):
    """返回 y=kx+b 在坐标窗口内有正长度、且不触及窗口边缘的 x 区间。"""
    values = (k, b, *x_bounds, *y_bounds, margin)
    if not all(isfinite(value) for value in values):
        raise ValueError("函数参数和范围必须为有限实数")
    if k == 0 or x_bounds[0] >= x_bounds[1] or y_bounds[0] >= y_bounds[1] or margin < 0:
        raise ValueError("要求 k 非零、坐标范围有序且 margin 非负")
    intersections = ((y_bounds[0] - b) / k, (y_bounds[1] - b) / k)
    left = max(x_bounds[0], min(intersections)) + margin
    right = min(x_bounds[1], max(intersections)) - margin
    if right <= left:
        raise ValueError("直线在所给窗口内没有足够长的可见部分")
    return [left, right]


class LinearFunctionGraph(Scene):
    """一次函数图像、两轴截距、斜率正负与平行移动。"""

    BLUE_LINE = "#3498db"
    GREEN_LINE = "#2ecc71"
    PURPLE_LINE = "#9b59b6"
    GOLD_LINE = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.scene_1_opening()
        self.scene_2_coordinate_system()
        self.scene_3_main_function()
        self.scene_4_slope_positive()
        self.scene_5_slope_negative()
        self.scene_6_intercept_effect()
        self.scene_7_summary()

    def caption(self, content, color=WHITE, y=-4.9, size=27):
        label = Text(content, font_size=size, color=color).move_to([0, y, 0])
        if label.width > 7.7:
            label.scale_to_fit_width(7.7)
        return label

    def plot_linear(self, k, b, color, width=4):
        interval = visible_interval(k, b)
        return self.axes.plot(lambda x: k * x + b, x_range=interval,
                              color=color, stroke_width=width)

    def scene_1_opening(self):
        self.author_info = self.caption("上海初高中数学直通车 @emptyandcalm",
                                        color=GRAY_B, y=7.0, size=20)
        question = self.caption("怎样从解析式看出直线的方向和位置？",
                                color=YELLOW, y=5.4, size=30)
        mystery = Line([-2.5, -1.0, 0], [2.5, 2.5, 0],
                       color=self.BLUE_LINE, stroke_width=5)
        self.play(FadeIn(self.author_info), Write(question), run_time=1)
        self.play(Create(mystery), run_time=1)
        self.wait(0.4)
        self.play(FadeOut(question), FadeOut(mystery), run_time=0.5)

    def scene_2_coordinate_system(self):
        # 两轴相同单位长度：比较 |k| 时几何倾角才有一致尺度。
        self.axes = Axes(x_range=[-4, 4, 1], y_range=[-3, 5, 1],
                         x_length=6.4, y_length=6.4, tips=False,
                         axis_config={"include_numbers": False, "stroke_width": 2})
        self.axes.move_to(UP * 0.5)
        x_label = Text("x", font_size=24).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.12)
        y_label = Text("y", font_size=24).next_to(self.axes.y_axis.get_end(), UP, buff=0.12)
        origin = Text("O", font_size=22).next_to(self.axes.c2p(0, 0), DL, buff=0.12)
        self.axis_group = VGroup(self.axes, x_label, y_label, origin)
        title = self.caption("建立直角坐标系", y=5.5, size=34)
        self.play(Write(title), Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), FadeIn(origin), run_time=0.4)
        self.play(FadeOut(title), run_time=0.3)

    def scene_3_main_function(self):
        self.formula_main = MathTex(r"y=2x+1", font_size=40, color=self.BLUE_LINE)
        self.formula_main.move_to(UP * 5.6)
        self.graph_main = self.plot_linear(2, 1, self.BLUE_LINE)
        self.play(Write(self.formula_main), Create(self.graph_main), run_time=1.5)
        points = [(0, 1), (-0.5, 0)]
        marks = VGroup()
        for x, y in points:
            dot = Dot(self.axes.c2p(x, y), radius=0.07, color=YELLOW)
            label = MathTex(r"(0,1)" if x == 0 else r"(-\tfrac12,0)",
                            font_size=27, color=YELLOW)
            label.next_to(dot, RIGHT if x == 0 else DOWN, buff=0.18)
            marks.add(dot, label)
        self.play(FadeIn(marks), run_time=0.6)
        explanation = self.caption("与 y 轴交于 (0, b)，与 x 轴交于 (-b/k, 0)",
                                   color=GRAY_A, size=26)
        self.play(FadeIn(explanation), run_time=0.4)
        self.wait(1.2)
        self.play(FadeOut(explanation), FadeOut(marks), run_time=0.5)

    def scene_4_slope_positive(self):
        # 比较 k 时固定 b=1，避免同时改变两个参数造成误导。
        compare = self.plot_linear(0.5, 1, self.GREEN_LINE, width=3)
        label = MathTex(r"y=\tfrac12 x+1", color=self.GREEN_LINE, font_size=31)
        label.move_to([-1.5, -4.8, 0])
        note = self.caption("k > 0：从左到右上升；同尺度下 |k| 越大越陡",
                            color=YELLOW, y=-5.7, size=25)
        self.play(Create(compare), FadeIn(label), FadeIn(note), run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(compare), FadeOut(label), FadeOut(note), run_time=0.5)

    def scene_5_slope_negative(self):
        # 固定 b=1：仅改变斜率符号，展示下降趋势。
        negative = self.plot_linear(-1, 1, self.PURPLE_LINE)
        formula = MathTex(r"y=-x+1", font_size=35, color=self.PURPLE_LINE)
        formula.move_to(UP * 4.8)
        note = self.caption("k < 0：从左到右下降", color=self.PURPLE_LINE)
        self.play(self.graph_main.animate.set_opacity(0.3),
                  self.formula_main.animate.set_opacity(0.3), run_time=0.4)
        self.play(Create(negative), Write(formula), FadeIn(note), run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(negative), FadeOut(formula), FadeOut(note), run_time=0.5)
        self.play(self.graph_main.animate.set_opacity(1),
                  self.formula_main.animate.set_opacity(1), run_time=0.4)

    def scene_6_intercept_effect(self):
        upper = self.plot_linear(2, 2, self.GREEN_LINE, width=3)
        lower = self.plot_linear(2, -1, self.GOLD_LINE, width=3)
        upper_dot = Dot(self.axes.c2p(0, 2), radius=0.07, color=self.GREEN_LINE)
        main_dot = Dot(self.axes.c2p(0, 1), radius=0.07, color=self.BLUE_LINE)
        lower_dot = Dot(self.axes.c2p(0, -1), radius=0.07, color=self.GOLD_LINE)
        formulas = VGroup(
            MathTex(r"y=2x+2", color=self.GREEN_LINE, font_size=27),
            MathTex(r"y=2x+1", color=self.BLUE_LINE, font_size=27),
            MathTex(r"y=2x-1", color=self.GOLD_LINE, font_size=27),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to([0, -5.0, 0])
        note = self.caption("固定 k，改变 b：三条直线平行，纵截距随 b 改变",
                            y=-6.4, color=YELLOW, size=23)
        self.play(Create(upper), Create(lower), run_time=1.0)
        self.play(FadeIn(VGroup(upper_dot, main_dot, lower_dot)),
                  FadeIn(formulas), FadeIn(note), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(upper), FadeOut(lower),
                  FadeOut(upper_dot), FadeOut(main_dot), FadeOut(lower_dot),
                  FadeOut(formulas), FadeOut(note), run_time=0.6)

    def scene_7_summary(self):
        # 坐标轴标签和原点与主图像一起清理，不遗留前镜对象。
        self.play(FadeOut(self.axis_group), FadeOut(self.graph_main),
                  FadeOut(self.formula_main), run_time=0.6)
        cards = VGroup()
        for heading, detail, color in (
            ("图像与交点", "图像是直线；纵截距为 b", self.BLUE_LINE),
            ("斜率 k", "正数上升，负数下降；同尺度比较陡缓", self.GREEN_LINE),
            ("截距 b", "固定 k 时，改变 b 使直线平行移动", self.GOLD_LINE),
        ):
            background = RoundedRectangle(width=7.7, height=1.45,
                                          corner_radius=0.16, color=color,
                                          fill_color=color, fill_opacity=0.09)
            heading_text = Text(heading, font_size=28, color=color)
            detail_text = Text(detail, font_size=23, color=WHITE)
            contents = VGroup(heading_text, detail_text).arrange(DOWN, buff=0.13)
            contents.scale_to_fit_width(min(contents.width, 7.0))
            cards.add(VGroup(background, contents))
        cards.arrange(DOWN, buff=0.45).move_to(ORIGIN)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.18), run_time=0.45)
        self.wait(1.2)
        self.play(FadeOut(cards), run_time=0.5)
        ending = self.caption("@emptyandcalm · 上海初高中数学直通车",
                              y=0, size=30, color=YELLOW)
        self.play(FadeOut(self.author_info), FadeIn(ending), run_time=0.7)
        self.wait(0.5)
        self.play(FadeOut(ending), run_time=0.4)


# manim -ql linear_function_graph.py LinearFunctionGraph

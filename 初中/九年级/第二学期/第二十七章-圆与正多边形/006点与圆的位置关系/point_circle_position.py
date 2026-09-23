"""九年级：点与圆的位置关系（9:16 竖屏教学视频）。

保留 PointCirclePosition 入口及七段教学顺序。所有几何数据由同一半径与距离生成；
动态阶段只更新数值对象和轻量几何图形，不在每帧重新构造 MathTex / Text。
"""
from manim import *
import numpy as np
from point_circle_math import classify_distance, validate_points

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PointCirclePosition(Scene):
    COLOR_CIRCLE = "#3498db"
    COLOR_INSIDE = "#e74c3c"
    COLOR_ON = "#f39c12"
    COLOR_OUTSIDE = "#2ecc71"
    COLOR_RADIUS = "#9b59b6"
    COLOR_HIGHLIGHT = YELLOW
    FONT = "sans-serif"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O = np.array([0.0, 1.3, 0.0])
        self.radius = 1.8
        self.distances = {"inside": 1.0, "on": self.radius, "outside": 2.8}
        validate_points(self.radius, self.distances)
        self.show_opening()
        self.show_distance_concept()
        self.show_point_inside()
        self.show_point_on_circle()
        self.show_point_outside()
        self.show_dynamic_demo()
        self.show_summary()

    def label(self, text, *, size=27, color=WHITE, y=None):
        obj = Text(text, font=self.FONT, font_size=size, color=color)
        return obj if y is None else obj.move_to(UP * y)

    def show_opening(self):
        self.author = self.label("上海初高中数学直通车 @emptyandcalm", size=19, color=GRAY_B, y=6.8)
        question = self.label("这个点，在圆里还是圆外？", size=36, color=self.COLOR_HIGHLIGHT, y=5.3)
        self.circle = Circle(radius=self.radius, color=self.COLOR_CIRCLE, stroke_width=4).move_to(self.O)
        mystery = Dot(self.O + 1.0 * RIGHT, color=WHITE, radius=0.10)
        self.play(FadeIn(self.author), Write(question))
        self.play(Create(self.circle), FadeIn(mystery))
        self.wait(0.7)
        self.play(FadeOut(question), FadeOut(mystery))

    def show_distance_concept(self):
        header = self.label("关键：比较点到圆心的距离 d 与半径 r", size=28, color=self.COLOR_HIGHLIGHT, y=5.4)
        self.center_dot = Dot(self.O, color=self.COLOR_RADIUS, radius=0.10)
        circle_point = self.O + self.radius * RIGHT
        reference = Line(self.O, circle_point, color=self.COLOR_RADIUS, stroke_width=4)
        endpoint = Dot(circle_point, color=WHITE, radius=0.08)
        equation = MathTex(r"r=|OA|>0", font_size=35).move_to(DOWN * 4.0)
        hint = self.label("O 是圆心，A 在圆上；点 P 到 O 的距离记为 d", size=23, color=GRAY_A, y=-5.2)
        self.play(Write(header), FadeIn(self.center_dot))
        self.play(Create(reference), FadeIn(endpoint))
        self.play(Write(equation), FadeIn(hint))
        self.wait(0.9)
        self.play(FadeOut(VGroup(header, reference, endpoint, equation, hint)))

    def show_case(self, state):
        """由统一的数值距离派生可见点、线和屏幕结论。"""
        names = {"inside": "圆内", "on": "圆上", "outside": "圆外"}
        colors = {"inside": self.COLOR_INSIDE, "on": self.COLOR_ON, "outside": self.COLOR_OUTSIDE}
        symbols = {"inside": r"d<r", "on": r"d=r", "outside": r"d>r"}
        d = self.distances[state]
        assert classify_distance(d, self.radius) == state
        point = self.O + d * RIGHT
        header = self.label("点在" + names[state], size=32, color=colors[state], y=5.3)
        mark = Dot(point, color=colors[state], radius=0.12)
        mark_label = MathTex("P", font_size=27).next_to(mark, UP, buff=0.12)
        distance_line = Line(self.O, point, color=colors[state], stroke_width=4)
        radius_line = DashedLine(self.O, self.O + self.radius * UP, color=self.COLOR_RADIUS, dash_length=0.10)
        equation = MathTex(symbols[state], font_size=42, color=colors[state]).move_to(DOWN * 4.2)
        numbers = MathTex(rf"d={d:.1f},\quad r={self.radius:.1f}", font_size=28).move_to(DOWN * 5.1)
        group = VGroup(header, mark, mark_label, distance_line, radius_line, equation, numbers)
        self.play(FadeIn(header), FadeIn(mark), FadeIn(mark_label))
        self.play(Create(distance_line), Create(radius_line))
        self.play(Write(equation), FadeIn(numbers))
        self.wait(1.0)
        self.play(FadeOut(group))

    def show_point_inside(self):
        self.show_case("inside")

    def show_point_on_circle(self):
        self.show_case("on")

    def show_point_outside(self):
        self.show_case("outside")

    def show_dynamic_demo(self):
        header = self.label("动态演示：距离变化，位置随之变化", size=28, color=self.COLOR_HIGHLIGHT, y=5.4)
        tracker = ValueTracker(2.5)
        moving_dot = Dot(self.O + 2.5 * RIGHT, radius=0.12, color=self.COLOR_OUTSIDE)
        moving_dot.add_updater(lambda mob: mob.move_to(self.O + tracker.get_value() * RIGHT))
        moving_line = always_redraw(
            lambda: Line(self.O, moving_dot.get_center(), stroke_width=3, color=self.COLOR_RADIUS)
        )
        value = DecimalNumber(2.5, num_decimal_places=2, font_size=34)
        value.move_to(DOWN * 4.3 + RIGHT * 0.8)
        value.add_updater(lambda mob: mob.set_value(tracker.get_value()))
        value_caption = MathTex("d=", font_size=34).next_to(value, LEFT, buff=0.12)
        radius_caption = MathTex(rf"r={self.radius:.1f}", font_size=30, color=self.COLOR_RADIUS).move_to(DOWN * 5.15)
        self.play(Write(header), FadeIn(moving_dot), Create(moving_line))
        self.play(FadeIn(value), FadeIn(value_caption), FadeIn(radius_caption))
        for state, target in (("outside", 2.5), ("on", self.radius), ("inside", 1.0)):
            # 状态标签只在到达准确位置后出现；移动过程中不使用错误的近似边界文案。
            self.play(tracker.animate.set_value(target), run_time=1.1)
            assert classify_distance(tracker.get_value(), self.radius) == state
            name = {"outside": "圆外：d > r", "on": "圆上：d = r", "inside": "圆内：d < r"}[state]
            color = {"outside": self.COLOR_OUTSIDE, "on": self.COLOR_ON, "inside": self.COLOR_INSIDE}[state]
            moving_dot.set_color(color)
            status = self.label(name, size=27, color=color, y=-6.0)
            self.play(FadeIn(status))
            self.wait(0.7)
            self.play(FadeOut(status))
        moving_dot.clear_updaters()
        moving_line.clear_updaters()
        value.clear_updaters()
        self.play(FadeOut(VGroup(header, moving_dot, moving_line, value, value_caption, radius_caption)))

    def show_summary(self):
        header = self.label("判断方法：比较 d 与 r", size=34, color=self.COLOR_HIGHLIGHT, y=5.1)
        self.play(Write(header))
        cards = VGroup()
        for i, (expression, meaning, color) in enumerate((
            (r"d<r", "点在圆内", self.COLOR_INSIDE),
            (r"d=r", "点在圆上", self.COLOR_ON),
            (r"d>r", "点在圆外", self.COLOR_OUTSIDE),
        )):
            row = VGroup(MathTex(expression, font_size=39, color=color), self.label(meaning, size=27))
            row.arrange(RIGHT, buff=0.45).move_to(UP * (2.3 - 1.5 * i))
            cards.add(row)
            self.play(FadeIn(row, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(cards), FadeOut(header), FadeOut(self.circle), FadeOut(self.center_dot))
        outro = self.label("点与圆的位置关系", size=38, color=self.COLOR_HIGHLIGHT, y=0.8)
        self.play(Write(outro))
        self.wait(0.6)
        self.play(FadeOut(outro), FadeOut(self.author))


# manim -ql point_circle_position.py PointCirclePosition

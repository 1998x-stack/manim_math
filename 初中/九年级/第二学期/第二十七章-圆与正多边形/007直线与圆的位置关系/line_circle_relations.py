"""九年级《直线与圆的位置关系》：用实际垂距统一生成图形、交点与字幕。"""
from manim import *
import numpy as np
from line_circle_math import horizontal_intersections, verify_case

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class LineCircleRelations(Scene):
    COLOR_CIRCLE = "#3498db"
    COLOR_LINE = "#e74c3c"
    COLOR_PERPENDICULAR = "#2ecc71"
    COLOR_INTERSECT = "#f39c12"
    COLOR_HIGHLIGHT = YELLOW
    COLOR_AUXILIARY = GRAY_B

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O = np.array([0.0, 1.0, 0.0])
        self.r = 2.0
        self.d_intersect, self.d_tangent, self.d_separate = 1.6, self.r, 3.0
        for distance, count in ((self.d_intersect, 2), (self.d_tangent, 1), (self.d_separate, 0)):
            verify_case(self.r, distance, count)
        self.circle = Circle(radius=self.r, color=self.COLOR_CIRCLE, stroke_width=4).move_to(self.O)
        self.scene_1_opening()
        self.scene_2_basic_concepts()
        self.scene_3_intersecting()
        self.scene_4_tangent()
        self.scene_5_separate()
        self.scene_6_summary()
        self.scene_7_outro()

    def text(self, value, y, *, size=28, color=WHITE):
        return Text(value, font="sans-serif", font_size=size, color=color).move_to(UP * y)

    def line_y(self, distance):
        return self.O[1] - distance

    def display_line(self, distance, x_min=-3.5, x_max=3.5):
        y = self.line_y(distance)
        return Line(np.array([x_min, y, 0]), np.array([x_max, y, 0]), color=self.COLOR_LINE, stroke_width=4)

    def intersection_points(self, distance):
        y = self.line_y(distance)
        return tuple(np.array([self.O[0] + offset, y, 0.0]) for offset in horizontal_intersections(self.r, distance))

    def scene_1_opening(self):
        self.author = self.text("上海初高中数学直通车 @emptyandcalm", 6.8, size=19, color=GRAY_B)
        prompt = self.text("直线与圆会怎样相遇？", 5.3, size=38, color=self.COLOR_HIGHLIGHT)
        preview = self.display_line(self.d_intersect)
        self.play(FadeIn(self.author), Write(prompt))
        self.play(Create(self.circle), Create(preview))
        self.wait(0.7)
        self.play(FadeOut(prompt), FadeOut(preview))

    def scene_2_basic_concepts(self):
        title = self.text("关键：圆心到直线的垂直距离 d", 5.2, size=30, color=self.COLOR_HIGHLIGHT)
        center = Dot(self.O, color=self.COLOR_HIGHLIGHT, radius=0.10)
        radius = Line(self.O, self.O + self.r * RIGHT, color=self.COLOR_AUXILIARY, stroke_width=3)
        line = self.display_line(self.d_intersect)
        foot = np.array([self.O[0], self.line_y(self.d_intersect), 0.0])
        perpendicular = DashedLine(self.O, foot, color=self.COLOR_PERPENDICULAR, dash_length=0.10)
        right_mark = self.right_mark(foot)
        definition = MathTex(r"d=|OH|,\quad r=|OA|>0", font_size=33).move_to(DOWN * 4.2)
        self.play(Write(title), FadeIn(center), Create(radius))
        self.play(Create(line), Create(perpendicular), FadeIn(right_mark))
        self.play(Write(definition))
        self.wait(0.9)
        self.play(FadeOut(VGroup(title, center, radius, line, perpendicular, right_mark, definition)))

    def right_mark(self, foot, size=0.18):
        """对于位于圆心下方的水平直线，两个可见边方向分别是 UP 与 RIGHT。"""
        return Polygon(foot, foot + size * UP, foot + size * (UP + RIGHT),
                       foot + size * RIGHT, color=self.COLOR_HIGHLIGHT,
                       stroke_width=2, fill_opacity=0)

    def show_case(self, name, distance, expected_count, symbol, color):
        offsets = verify_case(self.r, distance, expected_count)
        points = self.intersection_points(distance)
        if len(points) != len(offsets):
            raise ValueError("图形交点与纯数学模型不匹配")
        header = self.text(name, 5.2, size=35, color=color)
        line = self.display_line(distance)
        foot = np.array([self.O[0], self.line_y(distance), 0.0])
        vertical = Line(self.O, foot, color=self.COLOR_PERPENDICULAR, stroke_width=3)
        mark = self.right_mark(foot)
        label = MathTex(symbol, font_size=44, color=color).move_to(DOWN * 4.0)
        description = self.text(
            f"d = {distance:.1f}，r = {self.r:.1f}；{len(points)} 个公共点",
            -5.2, size=24, color=GRAY_A
        )
        self.play(Write(header), Create(line))
        self.play(Create(vertical), FadeIn(mark))
        dots = VGroup(*[Dot(point, color=color, radius=0.11) for point in points])
        if points:
            self.play(FadeIn(dots))
        if expected_count == 1:
            tangent_note = self.text("切线与切点处半径垂直", -6.0, size=22, color=color)
            self.play(FadeIn(tangent_note))
        else:
            tangent_note = None
        self.play(Write(label), FadeIn(description))
        self.wait(1.1)
        objects = [header, line, vertical, mark, label, description, dots]
        if tangent_note is not None:
            objects.append(tangent_note)
        self.play(FadeOut(VGroup(*objects)))

    def scene_3_intersecting(self):
        self.show_case("情况一：相交", self.d_intersect, 2, r"d<r", self.COLOR_INTERSECT)

    def scene_4_tangent(self):
        self.show_case("情况二：相切", self.d_tangent, 1, r"d=r", self.COLOR_HIGHLIGHT)

    def scene_5_separate(self):
        self.show_case("情况三：相离", self.d_separate, 0, r"d>r", self.COLOR_AUXILIARY)

    def scene_6_summary(self):
        self.play(FadeOut(self.circle))
        title = self.text("直线与圆：三种位置关系", 5.6, size=34, color=self.COLOR_HIGHLIGHT)
        self.play(Write(title))
        groups = VGroup()
        for index, (name, distance, count, expr, color) in enumerate((
            ("相交", self.d_intersect, 2, r"d<r", self.COLOR_INTERSECT),
            ("相切", self.d_tangent, 1, r"d=r", self.COLOR_HIGHLIGHT),
            ("相离", self.d_separate, 0, r"d>r", self.COLOR_AUXILIARY),
        )):
            verify_case(self.r, distance, count)
            center = np.array([-1.45, 2.55 - 2.6 * index, 0.0])
            mini_r = 0.65
            line_y = center[1] - mini_r * (distance / self.r)
            mini_circle = Circle(radius=mini_r, color=self.COLOR_CIRCLE).move_to(center)
            mini_line = Line(np.array([center[0] - 1.20, line_y, 0]),
                             np.array([center[0] + 1.20, line_y, 0]), color=self.COLOR_LINE)
            marks = VGroup(*[
                Dot(np.array([center[0] + mini_r * (x / self.r), line_y, 0]), radius=0.06, color=color)
                for x in horizontal_intersections(self.r, distance)
            ])
            phrase = VGroup(self.text(name, 0, size=24, color=color), MathTex(expr, font_size=30))
            phrase.arrange(DOWN, buff=0.20).move_to(center + RIGHT * 2.25)
            group = VGroup(mini_circle, mini_line, marks, phrase)
            groups.add(group)
            self.play(FadeIn(group, shift=UP * 0.15), run_time=0.6)
        summary = self.text("比较垂距 d 与半径 r，确定公共点个数", -6.0,
                            size=23, color=self.COLOR_HIGHLIGHT)
        self.play(FadeIn(summary))
        self.wait(1.3)
        self.play(FadeOut(groups), FadeOut(title), FadeOut(summary))

    def scene_7_outro(self):
        outro = self.text("用距离理解几何关系", 0.5, size=36, color=self.COLOR_HIGHLIGHT)
        self.play(FadeIn(outro))
        self.wait(0.8)
        self.play(FadeOut(outro), FadeOut(self.author))


# manim -ql line_circle_relations.py LineCircleRelations

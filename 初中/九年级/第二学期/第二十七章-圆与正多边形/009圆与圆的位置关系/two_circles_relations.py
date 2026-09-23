"""九年级《圆与圆的位置关系》：数据驱动展示五种常见位置关系与重合退化情形。"""
from manim import *
import numpy as np
from two_circles_math import circle_relation, circle_intersections

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TwoCirclesRelations(Scene):
    COLOR_CIRCLE_1 = "#3498db"
    COLOR_CIRCLE_2 = "#e74c3c"
    COLOR_DISTANCE = "#2ecc71"
    COLOR_TANGENT = "#f39c12"
    COLOR_HIGHLIGHT = YELLOW

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O1 = np.array([-1.0, 1.0, 0.0])
        self.R, self.r = 1.5, 1.0
        self.cases = (
            ("外离", 3.0, "external_separation", r"d>R+r", 0),
            ("外切", 2.5, "external_tangency", r"d=R+r", 1),
            ("相交", 1.8, "intersection", r"R-r<d<R+r", 2),
            ("内切", 0.5, "internal_tangency", r"d=R-r", 1),
            ("内含", 0.2, "containment", r"d<R-r", 0),
        )
        for _, distance, state, _, count in self.cases:
            center2 = self.second_center(distance)
            if circle_relation(self.R, self.r, distance) != state:
                raise ValueError(f"两圆位置关系的数学前提错误：{state}")
            if len(circle_intersections(tuple(self.O1[:2]), self.R, tuple(center2[:2]), self.r)) != count:
                raise ValueError("演示交点个数与两圆位置关系不一致")
        self.circle1 = Circle(radius=self.R, color=self.COLOR_CIRCLE_1, stroke_width=4).move_to(self.O1)
        self.scene_1_opening()
        self.scene_2_basic_concepts()
        self.scene_3_external_separation()
        self.scene_4_external_tangency()
        self.scene_5_intersection()
        self.scene_6_internal_tangency()
        self.scene_7_containment()
        self.scene_8_summary()
        self.scene_9_outro()

    def second_center(self, distance):
        return self.O1 + distance * RIGHT

    def title(self, message, color=YELLOW):
        return Text(message, font="sans-serif", font_size=35, color=color).move_to(UP * 5.35)

    def scene_1_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font="sans-serif",
                           font_size=19, color=GRAY_B).move_to(UP * 6.8)
        hook = self.title("两个圆可能有几种位置关系？")
        preview = Circle(radius=self.r, color=self.COLOR_CIRCLE_2, stroke_width=4).move_to(self.second_center(1.8))
        self.play(FadeIn(self.author), Write(hook))
        self.play(Create(self.circle1), Create(preview))
        self.wait(0.7)
        self.play(FadeOut(hook), FadeOut(preview))

    def scene_2_basic_concepts(self):
        header = self.title("比较两圆半径 R、r 与圆心距 d")
        center = Dot(self.O1, color=WHITE, radius=0.10)
        radius = Line(self.O1, self.O1 + self.R * LEFT, color=self.COLOR_DISTANCE, stroke_width=3)
        radius_label = MathTex("R", font_size=28).next_to(radius, UP, buff=0.12)
        model = MathTex(r"R>r>0,\qquad d=|O_1O_2|", font_size=34).move_to(DOWN * 4.25)
        self.play(Write(header), FadeIn(center), Create(radius), FadeIn(radius_label))
        self.play(Write(model))
        self.wait(0.8)
        self.play(FadeOut(VGroup(header, center, radius, radius_label, model)))

    def draw_case(self, case):
        name, distance, expected, relation_formula, count = case
        center2 = self.second_center(distance)
        # 判定参数值与实际显示坐标都要满足一致的几何条件。
        actual_distance = float(np.linalg.norm(center2 - self.O1))
        if circle_relation(self.R, self.r, actual_distance) != expected:
            raise ValueError("显示的两圆圆心距与字幕关系不一致")
        coordinates = circle_intersections(tuple(self.O1[:2]), self.R,
                                            tuple(center2[:2]), self.r)
        if len(coordinates) != count:
            raise ValueError("圆周交点数量错误")
        subtitle = self.title(name)
        circle2 = Circle(radius=self.r, color=self.COLOR_CIRCLE_2, stroke_width=4).move_to(center2)
        center1_dot = Dot(self.O1, color=WHITE, radius=0.07)
        center2_dot = Dot(center2, color=WHITE, radius=0.07)
        distance_line = DashedLine(self.O1, center2, color=self.COLOR_DISTANCE, dash_length=0.10)
        radius1 = Line(self.O1, self.O1 + self.R * UP, color=self.COLOR_CIRCLE_1, stroke_width=2)
        radius2 = Line(center2, center2 + self.r * UP, color=self.COLOR_CIRCLE_2, stroke_width=2)
        formula = MathTex(relation_formula, font_size=40, color=YELLOW).move_to(DOWN * 4.0)
        count_note = Text(f"{count} 个公共点", font="sans-serif", font_size=26,
                          color=GRAY_A).move_to(DOWN * 5.1)
        dots = VGroup(*[Dot(np.array([x, y, 0.0]), color=self.COLOR_TANGENT, radius=0.10)
                        for x, y in coordinates])
        self.play(Write(subtitle), Create(circle2))
        self.play(FadeIn(center1_dot), FadeIn(center2_dot), Create(distance_line))
        self.play(Create(radius1), Create(radius2))
        if coordinates:
            self.play(FadeIn(dots))
        self.play(Write(formula), FadeIn(count_note))
        self.wait(1.1)
        self.play(FadeOut(VGroup(subtitle, circle2, center1_dot, center2_dot,
                                 distance_line, radius1, radius2, formula, count_note, dots)))

    def scene_3_external_separation(self):
        self.draw_case(self.cases[0])

    def scene_4_external_tangency(self):
        self.draw_case(self.cases[1])

    def scene_5_intersection(self):
        self.draw_case(self.cases[2])

    def scene_6_internal_tangency(self):
        self.draw_case(self.cases[3])

    def scene_7_containment(self):
        self.draw_case(self.cases[4])

    def scene_8_summary(self):
        self.play(FadeOut(self.circle1))
        header = self.title("五种常见位置关系")
        self.play(Write(header))
        cards = VGroup()
        for index, (name, distance, _, expression, count) in enumerate(self.cases):
            center1 = np.array([-1.65, 3.5 - index * 1.65, 0.0])
            scale = 0.40
            center2 = center1 + (distance * scale) * RIGHT
            large = Circle(radius=self.R * scale, color=self.COLOR_CIRCLE_1, stroke_width=2).move_to(center1)
            small = Circle(radius=self.r * scale, color=self.COLOR_CIRCLE_2, stroke_width=2).move_to(center2)
            positions = circle_intersections(tuple(center1[:2]), self.R * scale,
                                              tuple(center2[:2]), self.r * scale)
            if len(positions) != count:
                raise ValueError("总结缩略图的接触点数与教学文案不匹配")
            dots = VGroup(*[Dot(np.array([x, y, 0]), radius=0.045, color=self.COLOR_TANGENT)
                            for x, y in positions])
            label = VGroup(Text(name, font="sans-serif", font_size=22),
                           MathTex(expression, font_size=26)).arrange(DOWN, buff=0.13)
            label.move_to(center1 + RIGHT * 2.65)
            card = VGroup(large, small, dots, label)
            cards.add(card)
            self.play(FadeIn(card, shift=UP * 0.10), run_time=0.5)
        note = Text("补充：圆心与半径均相同，则两圆重合", font="sans-serif",
                    font_size=21, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.7)
        self.play(FadeIn(note))
        self.wait(1.0)
        self.play(FadeOut(cards), FadeOut(note), FadeOut(header))

    def scene_9_outro(self):
        outro = Text("圆心距决定两圆的位置关系", font="sans-serif",
                     font_size=35, color=YELLOW).move_to(UP * 0.3)
        self.play(Write(outro))
        self.wait(0.7)
        self.play(FadeOut(outro), FadeOut(self.author))


# manim -ql two_circles_relations.py TwoCirclesRelations

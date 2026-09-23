"""九年级《正多边形与圆》：中心角、边心距、边长与面积的六段教学。"""
from manim import *
import numpy as np
from regular_polygon_math import polygon_metrics, polygon_vertices, verify_polygon

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class RegularPolygonAndCircle(Scene):
    POLYGON_COLOR = "#4fc3f7"
    CIRCLE_COLOR = "#ffb300"
    RADIUS_COLOR = "#2ed573"
    APOTHEM_COLOR = "#fd79a8"
    ANGLE_COLOR = "#a29bfe"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O = np.array([0.0, 1.1, 0.0])
        self.R = 2.0
        self.n = 6
        for sides in (3, 4, 6):
            verify_polygon(sides, self.R)
        self.data = polygon_metrics(self.n, self.R)
        self.vertices = self.polygon_vertices(self.n)
        self.hexagon = Polygon(*self.vertices, color=self.POLYGON_COLOR, stroke_width=4)
        self.circle = Circle(radius=self.R, color=self.CIRCLE_COLOR, stroke_width=3).move_to(self.O)
        self.center_dot = Dot(self.O, color=RED, radius=0.10)
        self.scene_1_opening()
        self.scene_2_core_elements()
        self.scene_3_central_angle()
        self.scene_4_hexagon_special()
        self.scene_5_area_formula()
        self.scene_6_summary()

    def polygon_vertices(self, n):
        return [np.array([x, y, 0.0]) for x, y in polygon_vertices(n, self.R, tuple(self.O[:2]))]

    def heading(self, message):
        return Text(message, font="sans-serif", font_size=34, color=GOLD).move_to(UP * 5.45)

    def scene_1_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font="sans-serif",
                           font_size=19, color=GRAY_B).move_to(UP * 6.8)
        headline = self.heading("正多边形与圆")
        self.play(FadeIn(self.author), Write(headline))
        self.play(Create(self.circle), Create(self.hexagon), FadeIn(self.center_dot))
        self.wait(0.8)
        self.play(FadeOut(headline))

    def scene_2_core_elements(self):
        header = self.heading("中心、半径、边心距与中心角")
        v0, v1 = self.vertices[0], self.vertices[1]
        midpoint = (v0 + v1) / 2
        radius = Line(self.O, v0, color=self.RADIUS_COLOR, stroke_width=4)
        apothem = DashedLine(self.O, midpoint, color=self.APOTHEM_COLOR,
                              stroke_width=4, dash_length=0.1)
        side = Line(v0, v1, color=YELLOW, stroke_width=5)
        angle = Angle(Line(self.O, v0), Line(self.O, v1), radius=0.50,
                      color=self.ANGLE_COLOR)
        formula = MathTex(r"\theta=\frac{360^\circ}{n},\quad r=R\cos\frac{\pi}{n}",
                          font_size=33).move_to(DOWN * 4.1)
        notes = Text("边心距是圆心到边的垂直距离", font="sans-serif",
                     font_size=23, color=GRAY_A).move_to(DOWN * 5.3)
        self.play(Write(header), Create(radius), Create(side))
        self.play(Create(apothem), Create(angle))
        self.play(Write(formula), FadeIn(notes))
        self.wait(1.0)
        self.play(FadeOut(VGroup(header, radius, side, apothem, angle, formula, notes)))

    def scene_3_central_angle(self):
        header = self.heading("中心角与边数成反比：360° ÷ n")
        self.play(Write(header), FadeOut(self.hexagon))
        current = None
        for n in (3, 4, 6):
            target = Polygon(*self.polygon_vertices(n), color=self.POLYGON_COLOR, stroke_width=4)
            formula = MathTex(rf"n={n},\quad \theta={360 // n}^\circ",
                              font_size=36, color=YELLOW).move_to(DOWN * 4.4)
            if current is None:
                current = target
                self.play(Create(current))
            else:
                self.play(Transform(current, target))
            self.play(FadeIn(formula))
            self.wait(0.5)
            self.play(FadeOut(formula))
        self.hexagon = current
        self.play(FadeOut(header))

    def scene_4_hexagon_special(self):
        if abs(self.data['side'] - self.R) > 1e-8:
            raise ValueError("正六边形边长必须等于外接圆半径")
        header = self.heading("正六边形的边长等于外接圆半径")
        v0, v1 = self.vertices[0], self.vertices[1]
        triangle = Polygon(self.O, v0, v1, color=self.ANGLE_COLOR, fill_opacity=0.2)
        radius1 = Line(self.O, v0, color=self.RADIUS_COLOR, stroke_width=4)
        radius2 = Line(self.O, v1, color=self.RADIUS_COLOR, stroke_width=4)
        edge = Line(v0, v1, color=YELLOW, stroke_width=5)
        equation = MathTex(r"OA=OB=R,\quad \angle AOB=60^\circ",
                           font_size=30).move_to(DOWN * 4.0)
        conclusion = MathTex(r"\angle AOB=60^\circ,\ OA=OB=R\ \Rightarrow\ AB=R",
                             font_size=28, color=YELLOW).move_to(DOWN * 5.1)
        self.play(Write(header), Create(triangle))
        self.play(Create(radius1), Create(radius2), Create(edge))
        self.play(Write(equation), Write(conclusion))
        self.wait(1.0)
        self.play(FadeOut(VGroup(header, triangle, radius1, radius2, edge, equation, conclusion)))

    def scene_5_area_formula(self):
        header = self.heading("把正多边形分成 n 个等底等高的三角形")
        spokes = VGroup(*[Line(self.O, vertex, color=GRAY_B, stroke_width=2)
                           for vertex in self.vertices])
        v0, v1 = self.vertices[0], self.vertices[1]
        triangle = Polygon(self.O, v0, v1, color=self.POLYGON_COLOR,
                           fill_opacity=0.28, stroke_width=3)
        altitude = DashedLine(self.O, (v0 + v1) / 2,
                              color=self.APOTHEM_COLOR, stroke_width=4, dash_length=0.1)
        one_area = MathTex(r"S_1=\frac{1}{2}ar", font_size=34).move_to(DOWN * 3.9)
        total_area = MathTex(r"S=nS_1=\frac{1}{2}(na)r=\frac{1}{2}Cr",
                             font_size=33, color=YELLOW).move_to(DOWN * 5.1)
        self.play(Write(header), Create(spokes))
        self.play(Create(triangle), Create(altitude))
        self.play(Write(one_area))
        self.play(Write(total_area))
        self.wait(1.2)
        self.play(FadeOut(VGroup(header, spokes, triangle, altitude, one_area, total_area)))

    def scene_6_summary(self):
        figures = VGroup(self.hexagon, self.circle, self.center_dot)
        self.play(figures.animate.scale(0.53).move_to(UP * 4.15))
        title = Text("正多边形知识总结", font="sans-serif", font_size=32,
                     color=GOLD).move_to(UP * 2.65)
        self.play(Write(title))
        cards = VGroup()
        for y, formula in ((1.4, r"\theta=\frac{360^\circ}{n}"),
                           (0.25, r"a=2R\sin\frac{\pi}{n}"),
                           (-0.9, r"r=R\cos\frac{\pi}{n}"),
                           (-2.05, r"S=\frac{1}{2}Cr")):
            card = MathTex(formula, font_size=32, color=YELLOW).move_to(UP * y)
            cards.add(card)
            self.play(FadeIn(card, shift=UP * 0.13))
        self.wait(1.0)
        self.play(FadeOut(cards), FadeOut(title))
        self.play(Rotate(self.hexagon, angle=PI / 6, about_point=self.circle.get_center()))
        self.wait(0.6)
        self.play(FadeOut(figures), FadeOut(self.author))


# manim -ql regular_polygon_circle.py RegularPolygonAndCircle

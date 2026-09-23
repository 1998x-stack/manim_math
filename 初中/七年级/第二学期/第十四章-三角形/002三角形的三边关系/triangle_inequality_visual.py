"""三边关系：从两圆交点解释严格不等式。"""
import math
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#101827"

BASE = 3.2
AC_FIXED = 2.2  # Length BC in the construction; see side labels in the scene.


def upper_vertex(ab, ac, bc):
    """Intersection above AB; return None for non-triangles, including equality."""
    if min(ab, ac, bc) <= 0 or not (abs(ac - bc) < ab < ac + bc):
        return None
    x = (ac * ac - bc * bc + ab * ab) / (2 * ab)
    y2 = ac * ac - x * x
    if y2 <= 0:
        return None
    return np.array([-ab / 2 + x, -1.1 + math.sqrt(y2), 0.0])


class TriangleInequalityVisual(Scene):
    """Render: manim -pql triangle_inequality_visual.py TriangleInequalityVisual"""

    def construct(self):
        title = Text("三条线段能拼成三角形吗？", font_size=40)
        title.to_edge(UP, buff=0.9)
        self.play(Write(title))
        a = np.array([-BASE / 2, -1.1, 0.0])
        b = np.array([BASE / 2, -1.1, 0.0])
        ac = ValueTracker(0.8)
        constant = MathTex(r"AB=3.2,\quad BC=2.2", font_size=39)
        constant.move_to(UP * 4.7)
        measured = VGroup(MathTex(r"AC=", font_size=39),
                          DecimalNumber(0.8, num_decimal_places=2,
                                        font_size=39, color=YELLOW))
        measured.arrange(RIGHT, buff=0.15).move_to(UP * 3.9)
        measured[1].add_updater(lambda m: m.set_value(ac.get_value()))

        def geometry():
            p = upper_vertex(BASE, ac.get_value(), 2.2)
            objects = VGroup(Line(a, b, color=WHITE, stroke_width=5),
                             Dot(a, color=WHITE), Dot(b, color=WHITE),
                             MathTex("A", font_size=30).next_to(a, DOWN),
                             MathTex("B", font_size=30).next_to(b, DOWN))
            if p is not None:
                objects.add(Line(a, p, color=YELLOW, stroke_width=5),
                            Line(b, p, color=BLUE, stroke_width=5),
                            Dot(p, color=GREEN),
                            MathTex("C", font_size=30).next_to(p, UP))
            return objects

        picture = always_redraw(geometry)
        criterion = MathTex(r"|3.2-2.2|<AC<3.2+2.2",
                            font_size=39).move_to(DOWN * 4.6)
        interval = MathTex(r"1.0<AC<5.4", font_size=43,
                           color=GREEN).move_to(DOWN * 5.5)
        self.play(FadeIn(picture), FadeIn(constant), FadeIn(measured))
        self.play(Write(criterion), Write(interval))
        self.wait(1)
        self.play(ac.animate.set_value(2.2), run_time=2)
        self.wait(1)

        # The two fixed-radius circles meet in a non-degenerate triangle.
        construction = VGroup(
            Circle(radius=2.2, color=YELLOW, stroke_opacity=0.6).move_to(a),
            Circle(radius=2.2, color=BLUE, stroke_opacity=0.6).move_to(b),
        )
        self.play(Create(construction))
        self.wait(1)
        self.play(FadeOut(construction))
        self.play(ac.animate.set_value(5.6), run_time=3)
        impossible = Text("过长：两线段不能闭合", font_size=34,
                          color=RED).move_to(DOWN * 3.0)
        self.play(FadeIn(impossible))
        self.wait(2)
        self.play(FadeOut(impossible), ac.animate.set_value(1.0), run_time=2)
        degenerate = Text("取等号时三点共线，不是三角形", font_size=30,
                          color=ORANGE).move_to(DOWN * 3.0)
        self.play(FadeIn(degenerate))
        self.wait(2)

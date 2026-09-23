"""三角形内角和与外角：新场景，不覆盖原课件。"""
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#101827"


class TriangleAngleSumVisual(Scene):
    """Render: manim -pql triangle_angle_visual.py TriangleAngleSumVisual"""

    def construct(self):
        title = Text("三角形的内角和", font_size=43).to_edge(UP, buff=0.85)
        self.play(Write(title))
        A = np.array([-2.7, -1.1, 0.0])
        B = np.array([2.7, -1.1, 0.0])
        t = ValueTracker(-0.6)

        def vertex_c():
            return np.array([t.get_value(), 2.1 + 0.18 * t.get_value(), 0.0])

        def arc_at(p, q, r, color):
            start = np.arctan2(q[1] - p[1], q[0] - p[0])
            end = np.arctan2(r[1] - p[1], r[0] - p[0])
            sweep = (end - start) % TAU
            assert 0 < sweep < PI, "Triangle vertices must stay non-collinear and CCW"
            return Arc(radius=0.48, start_angle=start, angle=sweep,
                       arc_center=p, color=color, stroke_width=6)

        def diagram():
            C = vertex_c()
            triangle = Polygon(A, B, C, stroke_color=WHITE,
                               stroke_width=5, fill_color=BLUE, fill_opacity=0.08)
            angles = VGroup(arc_at(A, B, C, YELLOW),
                            arc_at(B, C, A, GREEN),
                            arc_at(C, A, B, ORANGE))
            labels = VGroup(
                MathTex("A", font_size=34).move_to(A + DOWN * 0.5),
                MathTex("B", font_size=34).move_to(B + DOWN * 0.5),
                MathTex("C", font_size=34).move_to(C + UP * 0.5),
            )
            return VGroup(triangle, angles, labels)

        drawing = always_redraw(diagram)
        fact = MathTex(r"\angle A+\angle B+\angle C=180^\circ",
                       font_size=43).move_to(DOWN * 4.5)
        self.play(FadeIn(drawing), Write(fact))
        self.play(t.animate.set_value(1.2), run_time=3)
        self.play(t.animate.set_value(-1.3), run_time=2)
        self.wait(1)
        self.play(FadeOut(drawing))

        # At C, the straight angle above line l is partitioned by CA and CB.
        C = vertex_c()
        fixed = Polygon(A, B, C, color=WHITE, stroke_width=5)
        parallel = Line(C + LEFT * 3.7, C + RIGHT * 3.7,
                        color=TEAL, stroke_width=4)
        parallel_tag = MathTex(r"\ell\parallel AB", color=TEAL,
                               font_size=34).move_to(UP * 3.7)
        proof = VGroup(
            Text("平行线的内错角相等", font_size=32),
            MathTex(r"\alpha+\gamma+\beta=180^\circ", font_size=44),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 3.5)
        self.play(Create(fixed), Create(parallel), FadeIn(parallel_tag))
        self.play(ReplacementTransform(fact, proof[1]), FadeIn(proof[0]))
        self.wait(2)
        self.play(FadeOut(proof), FadeOut(parallel_tag), FadeOut(parallel),
                  FadeOut(fixed))

        # Exterior angle at B equals the sum of the two remote interior angles.
        C = vertex_c()
        extension = Line(B, B + RIGHT * 1.3, color=TEAL, stroke_width=4)
        exterior = VGroup(Polygon(A, B, C, color=WHITE, stroke_width=5),
                          extension)
        exterior_fact = MathTex(
            r"\angle CBD=\angle A+\angle C", font_size=43
        ).move_to(DOWN * 3.8)
        d_tag = MathTex("D", font_size=32).next_to(extension.get_end(), RIGHT, buff=0.1)
        self.play(Create(exterior), FadeIn(d_tag), Write(exterior_fact))
        self.wait(2)

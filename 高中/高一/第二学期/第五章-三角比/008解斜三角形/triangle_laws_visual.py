"""正弦定理与余弦定理：动态边角关系、面积法与垂线推导。"""
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#101827"


class TriangleLawsVisual(Scene):
    """Render: manim -pql triangle_laws_visual.py TriangleLawsVisual"""

    def construct(self):
        title = Text("任意三角形的边与角", font_size=44)
        title.to_edge(UP, buff=0.85)
        self.play(Write(title))
        a_pt = np.array([-2.0, -0.8, 0.0])
        b_pt = np.array([2.0, -0.8, 0.0])
        cx = ValueTracker(-0.5)
        cy = ValueTracker(1.9)

        def c_pt():
            return np.array([cx.get_value(), cy.get_value(), 0.0])

        def labeled_triangle():
            c = c_pt()
            return VGroup(
                Polygon(a_pt, b_pt, c, color=WHITE, stroke_width=5,
                        fill_color=BLUE, fill_opacity=0.06),
                MathTex("a", color=GREEN, font_size=35)
                .move_to((b_pt + c) / 2 + RIGHT * 0.36),
                MathTex("b", color=YELLOW, font_size=35)
                .move_to((a_pt + c) / 2 + LEFT * 0.36),
                MathTex("c", color=ORANGE, font_size=35)
                .move_to((a_pt + b_pt) / 2 + DOWN * 0.4),
                MathTex("A", font_size=30).next_to(a_pt, DOWN),
                MathTex("B", font_size=30).next_to(b_pt, DOWN),
                MathTex("C", font_size=30).next_to(c, UP),
            )

        drawing = always_redraw(labeled_triangle)
        length = DecimalNumber(0, num_decimal_places=2, color=GREEN,
                               font_size=38)
        length.add_updater(lambda m: m.set_value(np.linalg.norm(b_pt - c_pt())))
        readout = VGroup(MathTex("a=", color=GREEN, font_size=38),
                         length).arrange(RIGHT, buff=0.12).move_to(UP * 4.4)
        self.play(FadeIn(drawing), FadeIn(readout))
        self.play(cx.animate.set_value(0.7), cy.animate.set_value(1.65),
                  run_time=3)
        self.wait(1)
        length.clear_updaters()
        self.play(FadeOut(readout), FadeOut(drawing))

        # The circumcircle visualizes the extended sine rule (chord theorem).
        c_pt_final = c_pt()
        u = np.array([b_pt[:2] - a_pt[:2],
                      c_pt_final[:2] - a_pt[:2]])
        rhs = np.array([(b_pt @ b_pt - a_pt @ a_pt) / 2,
                        (c_pt_final @ c_pt_final - a_pt @ a_pt) / 2])
        center = np.append(np.linalg.solve(u, rhs), 0.0)
        circle = Circle(radius=np.linalg.norm(a_pt - center),
                        stroke_color=TEAL, stroke_opacity=0.5).move_to(center)
        triangle = labeled_triangle()
        sine_title = Text("正弦定理：面积相等与外接圆", font_size=34)
        sine_title.move_to(UP * 4.45)
        area = MathTex(r"2S=bc\sin A=ca\sin B=ab\sin C",
                       font_size=35).move_to(DOWN * 3.6)
        law_sine = MathTex(r"\frac a{\sin A}=\frac b{\sin B}="
                           r"\frac c{\sin C}=2R",
                           font_size=41).move_to(DOWN * 5.0)
        self.play(FadeIn(triangle), Create(circle), FadeIn(sine_title))
        self.play(Write(area), Write(law_sine))
        self.wait(2)

        # D is on AB in this chosen example; x=AD=b cos(A), h=CD=b sin(A).
        d = np.array([c_pt_final[0], a_pt[1], 0.0])
        altitude = DashedLine(c_pt_final, d, color=YELLOW, stroke_width=4)
        d_tag = MathTex("D", font_size=30).next_to(d, DOWN)
        cosine_title = Text("余弦定理：作高后应用勾股定理", font_size=34)
        cosine_title.move_to(UP * 4.45)
        first = MathTex(r"AD=b\cos A,\quad CD=b\sin A",
                        font_size=37).move_to(DOWN * 3.4)
        second = MathTex(r"a^2=(c-b\cos A)^2+(b\sin A)^2",
                         font_size=36).move_to(DOWN * 4.6)
        result = MathTex(r"a^2=b^2+c^2-2bc\cos A",
                         font_size=41, color=GREEN).move_to(DOWN * 5.85)
        self.play(FadeOut(circle), FadeOut(sine_title), FadeOut(area),
                  FadeOut(law_sine), FadeIn(cosine_title), Create(altitude),
                  FadeIn(d_tag))
        self.play(Write(first), Write(second))
        self.play(Write(result))
        self.wait(2)

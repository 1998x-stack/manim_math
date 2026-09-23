"""三角形四心与欧拉线；只在非共线三角形上构造外心。"""
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#101827"


def triangle_centers(a, b, c):
    """Return centroid G, circumcenter O, orthocenter H, incenter I."""
    a, b, c = (np.asarray(p, dtype=float) for p in (a, b, c))
    u = np.array([b[:2] - a[:2], c[:2] - a[:2]])
    if abs(np.linalg.det(u)) < 1e-8:
        raise ValueError("Three non-collinear vertices are required")
    rhs = np.array([(b @ b - a @ a) / 2,
                    (c @ c - a @ a) / 2])
    o = np.append(np.linalg.solve(u, rhs), 0.0)
    g = (a + b + c) / 3
    h = 3 * g - 2 * o
    sides = [np.linalg.norm(b - c), np.linalg.norm(a - c),
             np.linalg.norm(a - b)]
    i = (sides[0] * a + sides[1] * b + sides[2] * c) / sum(sides)
    return g, o, h, i


class FourCentersVisual(Scene):
    """Render: manim -pql four_centers_visual.py FourCentersVisual"""

    def construct(self):
        title = Text("三角形的四心与欧拉线", font_size=42)
        title.to_edge(UP, buff=0.9)
        self.play(Write(title))
        a = np.array([-2.2, -0.5, 0.0])
        b = np.array([2.2, -0.5, 0.0])
        cx = ValueTracker(-0.7)
        cy = ValueTracker(2.0)

        def figure():
            c = np.array([cx.get_value(), cy.get_value(), 0.0])
            g, o, h, i = triangle_centers(a, b, c)
            r = np.linalg.norm(a - o)
            objects = VGroup(
                Circle(radius=r, color=BLUE, stroke_opacity=0.36).move_to(o),
                Polygon(a, b, c, color=WHITE, stroke_width=4),
                Line(o, h, color=TEAL, stroke_width=4),
            )
            for point, name, color, shift in (
                (g, "G", GREEN, DOWN), (o, "O", BLUE, LEFT),
                (h, "H", ORANGE, UP), (i, "I", YELLOW, RIGHT),
            ):
                objects.add(Dot(point, color=color, radius=0.08))
                objects.add(MathTex(name, color=color, font_size=30)
                            .move_to(point + 0.32 * shift))
            return objects

        picture = always_redraw(figure)
        legend = VGroup(
            Text("G：重心（中线交点）", font_size=30, color=GREEN),
            Text("O：外心（垂直平分线交点）", font_size=30, color=BLUE),
            Text("H：垂心（高所在直线交点）", font_size=30, color=ORANGE),
            Text("I：内心（角平分线交点）", font_size=30, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(DOWN * 4.2)
        relation = MathTex(r"O,G,H\ \mathrm{collinear},\quad OG:GH=1:2",
                           font_size=33).move_to(DOWN * 6.3)
        self.play(FadeIn(picture), FadeIn(legend))
        self.wait(1)
        self.play(cx.animate.set_value(1.4), cy.animate.set_value(0.3),
                  run_time=3)
        self.wait(1)
        self.play(Write(relation))
        proof = MathTex(r"G=\frac{A+B+C}{3},\quad H=3G-2O",
                        font_size=33).move_to(UP * 4.6)
        self.play(Write(proof))
        self.wait(2)

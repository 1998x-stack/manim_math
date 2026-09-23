"""小学奥数｜梯形蝴蝶模型。运行：manim lesson.py TrapezoidButterflyArea"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import *
from area_model import butterfly_areas, lesson_points, triangle_area

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 270 if os.environ.get("MANIM_PREVIEW") == "1" else 1080
config.pixel_height = 480 if os.environ.get("MANIM_PREVIEW") == "1" else 1920
config.frame_rate = 15 if os.environ.get("MANIM_PREVIEW") == "1" else 30

BG = "#111827"
COLORS = {"top": "#FBBF24", "bottom": "#60A5FA",
          "left": "#34D399", "right": "#F472B6"}


def xyz(p):
    return [p[0], p[1], 0]


class TrapezoidButterflyArea(Scene):
    """对称梯形：上/下/左/右面积依次为 2、8、4、4 cm²。"""

    def construct(self):
        self.camera.background_color = BG
        p = lesson_points()
        a, b, c, d, o = (xyz(p[key]) for key in "ABCDO")
        areas = butterfly_areas(bottom=6, top=3, height=4)
        assert areas == {"bottom": 8.0, "top": 2.0, "left": 4.0, "right": 4.0}
        assert triangle_area(p["A"], p["B"], p["O"]) == areas["bottom"]

        title = Text("梯形蝴蝶模型", font_size=46).move_to([0, 6.3, 0])
        subtitle = Text("连接两条对角线，观察四块面积", font_size=29,
                        color="#CBD5E1").move_to([0, 5.35, 0])
        conditions = MathTex(r"AB=6,\quad CD=3,\quad h=4\ (\mathrm{cm})",
                             font_size=35).move_to([0, 4.38, 0])

        outline = Polygon(a, b, c, d, color=WHITE, stroke_width=5)
        diagonals = VGroup(Line(a, c, color=WHITE, stroke_width=3),
                           Line(b, d, color=WHITE, stroke_width=3))
        dots = VGroup(*(Dot(v, radius=0.055, color=WHITE) for v in (a, b, c, d, o)))
        labels = VGroup(
            Text("A", font_size=27).next_to(a, DOWN + LEFT, buff=0.11),
            Text("B", font_size=27).next_to(b, DOWN + RIGHT, buff=0.11),
            Text("C", font_size=27).next_to(c, UP + RIGHT, buff=0.11),
            Text("D", font_size=27).next_to(d, UP + LEFT, buff=0.11),
            Text("O", font_size=25).next_to(o, UP + RIGHT, buff=0.10),
        )
        parts = {
            "bottom": Polygon(a, b, o, stroke_width=0,
                              fill_color=COLORS["bottom"], fill_opacity=0.30),
            "top": Polygon(c, d, o, stroke_width=0,
                           fill_color=COLORS["top"], fill_opacity=0.36),
            "left": Polygon(a, d, o, stroke_width=0,
                            fill_color=COLORS["left"], fill_opacity=0.35),
            "right": Polygon(b, c, o, stroke_width=0,
                             fill_color=COLORS["right"], fill_opacity=0.35),
        }

        self.play(Write(title), FadeIn(subtitle), run_time=1.3)
        self.play(Write(conditions), Create(outline), run_time=1.4)
        self.play(Create(diagonals), FadeIn(dots), FadeIn(labels), run_time=1.4)
        self.play(*(FadeIn(poly) for poly in parts.values()), run_time=1.4)
        self.bring_to_front(outline, diagonals, dots, labels)

        ratio = MathTex(r"AO:OC=AB:CD=2:1", font_size=35,
                        color=COLORS["top"]).move_to([0, 3.53, 0])
        self.play(Write(ratio), run_time=1.2)
        self.wait(0.8)

        # 由交点的高之比 2:1，可求下三角形面积 8、上三角形面积 2。
        upper_number = MathTex("2", color=COLORS["top"], font_size=36).move_to([0, 1.53, 0])
        lower_number = MathTex("8", color=COLORS["bottom"], font_size=39).move_to([0, -1.14, 0])
        self.play(FadeIn(upper_number), FadeIn(lower_number), run_time=0.9)
        same_base = MathTex(r"S_{ABD}=S_{ABC}=\frac{6\times4}{2}=12",
                            font_size=39).move_to([0, -4.0, 0])
        self.play(Write(same_base), run_time=1.6)
        self.wait(0.8)

        wing_numbers = VGroup(
            MathTex("4", color=COLORS["left"], font_size=39).move_to([-1.48, 0.17, 0]),
            MathTex("4", color=COLORS["right"], font_size=39).move_to([1.48, 0.17, 0]),
        )
        wing_formula = MathTex(r"S_{AOD}=S_{BOC}=12-8=4",
                               color=COLORS["left"], font_size=40).move_to([0, -5.13, 0])
        self.play(FadeIn(wing_numbers), Write(wing_formula), run_time=1.7)
        total = MathTex(r"S_{ABCD}=2+4+4+8=18\,\mathrm{cm}^2",
                        font_size=40, color=COLORS["top"]).move_to([0, -6.2, 0])
        self.play(Write(total), run_time=1.4)
        self.wait(2.3)

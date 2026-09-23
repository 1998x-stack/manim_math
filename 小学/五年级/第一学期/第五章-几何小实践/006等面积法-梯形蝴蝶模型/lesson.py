"""梯形蝴蝶：对角线交点、分段高、公共面积消去与四块面积验算。

MANIM_PREVIEW=1 manim lesson.py TrapezoidButterflyArea
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from manim import *
from area_model import butterfly_areas, lesson_points, triangle_area

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 270 if os.getenv("MANIM_PREVIEW") == "1" else 1080
config.pixel_height = 480 if os.getenv("MANIM_PREVIEW") == "1" else 1920
config.frame_rate = 15 if os.getenv("MANIM_PREVIEW") == "1" else 30

BG = "#111827"
MUTED = "#CBD5E1"
GOLD = "#FBBF24"
BLUE = "#60A5FA"
GREEN = "#34D399"
PINK = "#F472B6"
COLORS = {"top": GOLD, "bottom": BLUE, "left": GREEN, "right": PINK}


def xyz(p):
    return [p[0], p[1], 0]


def right_corner(x, y, side=0.18, color=GOLD):
    return VGroup(
        Line([x, y + side, 0], [x + side, y + side, 0], color=color, stroke_width=2.8),
        Line([x + side, y + side, 0], [x + side, y, 0], color=color, stroke_width=2.8),
    )


class TrapezoidButterflyArea(Scene):
    """同底等高减公共部分证明左右等积，之后由交点高比计算四区。"""

    def construct(self):
        self.camera.background_color = BG
        p = lesson_points()
        a, b, c, d, o = (xyz(p[key]) for key in "ABCDO")
        areas = butterfly_areas(bottom=6, top=3, height=4)
        assert areas == {"bottom": 8, "top": 2, "left": 4, "right": 4}
        assert triangle_area(p["A"], p["B"], p["O"]) == areas["bottom"]
        assert triangle_area(p["A"], p["B"], p["D"]) == 12
        assert triangle_area(p["A"], p["B"], p["C"]) == 12

        title = Text("等面积法｜梯形蝴蝶", font_size=42).move_to([0, 6.32, 0])
        subtitle = Text("连对角线，四个三角形藏着什么关系？",
                        font_size=26, color=MUTED).move_to([0, 5.5, 0])
        conditions = MathTex(r"AB\parallel CD,\quad AB=6,\ CD=3,\ h=4",
                             font_size=33).move_to([0, 4.6, 0])
        outline = Polygon(a, b, c, d, color=WHITE, stroke_width=4)
        diagonals = VGroup(Line(a, c, color=WHITE, stroke_width=3),
                           Line(b, d, color=WHITE, stroke_width=3))
        dots = VGroup(*(Dot(vertex, radius=0.055, color=WHITE) for vertex in (a, b, c, d, o)))
        labels = VGroup(
            Text("A", font_size=27).next_to(a, DOWN + LEFT, buff=0.13),
            Text("B", font_size=27).next_to(b, DOWN + RIGHT, buff=0.13),
            Text("C", font_size=27).next_to(c, UP + RIGHT, buff=0.13),
            Text("D", font_size=27).next_to(d, UP + LEFT, buff=0.13),
            Text("O", font_size=25).next_to(o, RIGHT, buff=0.12),
        )
        base_labels = VGroup(
            MathTex(r"6\,\mathrm{cm}", font_size=28).move_to([0, -2.58, 0]),
            MathTex(r"3\,\mathrm{cm}", font_size=28).move_to([0, 2.58, 0]),
        )
        outer_height = DashedLine([3.32, -2, 0], [3.32, 2, 0],
                                  color=GOLD, dash_length=0.13)
        outer_guides = VGroup(
            DashedLine(b, [3.32, -2, 0], color=MUTED, dash_length=0.08),
            DashedLine([1.5, 2, 0], [3.32, 2, 0], color=MUTED, dash_length=0.08),
        )
        outer_angle = right_corner(3.32, -2)
        height_label = MathTex(r"4\,\mathrm{cm}", color=GOLD,
                               font_size=28).move_to([3.72, 0, 0])
        self.play(Write(title), FadeIn(subtitle), run_time=1.3)
        self.play(Write(conditions), Create(outline), FadeIn(base_labels), run_time=1.4)
        self.play(Create(outer_height), Create(outer_guides), Create(outer_angle),
                  Write(height_label), run_time=1.25)
        self.play(Create(diagonals), FadeIn(dots), FadeIn(labels), run_time=1.4)

        parts = {
            "bottom": Polygon(a, b, o, stroke_width=0,
                              fill_color=BLUE, fill_opacity=0.29),
            "top": Polygon(c, d, o, stroke_width=0,
                           fill_color=GOLD, fill_opacity=0.36),
            "left": Polygon(a, d, o, stroke_width=0,
                            fill_color=GREEN, fill_opacity=0.31),
            "right": Polygon(b, c, o, stroke_width=0,
                             fill_color=PINK, fill_opacity=0.31),
        }
        self.play(*(FadeIn(parts[key]) for key in ("bottom", "top", "left", "right")),
                  run_time=1.5)
        self.bring_to_front(outline, diagonals, dots, labels)
        prompt = Text("先看两只翅膀：左边和右边谁更大？",
                      font_size=28, color=MUTED).move_to([0, -3.5, 0])
        self.play(Write(prompt), run_time=1.1)
        self.wait(0.8)

        # △ABD 与 △ABC 共底 AB，顶点 D、C 位于与 AB 平行的上底，面积都为 12。
        big_left = Polygon(a, b, d, stroke_color=GREEN, stroke_width=5,
                           fill_color=GREEN, fill_opacity=0.12)
        big_right = Polygon(a, b, c, stroke_color=PINK, stroke_width=5,
                            fill_color=PINK, fill_opacity=0.12)
        big_formula = MathTex(r"S_{ABD}=S_{ABC}=\frac{6\times4}{2}=12",
                              font_size=37).move_to([0, -4.42, 0])
        self.play(FadeOut(prompt), Create(big_left), Write(big_formula), run_time=1.5)
        self.play(ReplacementTransform(big_left, big_right), run_time=1.15)
        self.play(FadeOut(big_right), run_time=0.5)
        common = Polygon(a, b, o, stroke_color=BLUE, stroke_width=5,
                         fill_color=BLUE, fill_opacity=0.48)
        shared_note = MathTex(r"S_{ABO}=8\,\mathrm{cm}^2", color=BLUE,
                              font_size=35).move_to([0, -5.42, 0])
        shared_number = MathTex("8", color=WHITE, font_size=37).move_to([0, -1.22, 0])
        self.play(FadeIn(common), Write(shared_number), Write(shared_note), run_time=1.25)
        self.bring_to_front(outline, diagonals, dots, labels)
        self.wait(0.55)
        # O 在 BD 上：ABD=ABO+AOD；O 在 AC 上：ABC=ABO+BOC。
        left_wing = Polygon(a, d, o, stroke_color=GREEN, stroke_width=5,
                            fill_color=GREEN, fill_opacity=0.5)
        right_wing = Polygon(b, c, o, stroke_color=PINK, stroke_width=5,
                             fill_color=PINK, fill_opacity=0.5)
        wings_formula = MathTex(r"S_{AOD}=S_{BOC}=12-8=4",
                                font_size=36, color=GREEN).move_to([0, -6.43, 0])
        self.play(FadeIn(left_wing), FadeIn(right_wing), Write(wings_formula), run_time=1.45)
        self.bring_to_front(outline, diagonals, dots, labels)
        wing_values = VGroup(
            MathTex("4", color=GREEN, font_size=36).move_to([-1.75, 0.2, 0]),
            MathTex("4", color=PINK, font_size=36).move_to([1.75, 0.2, 0]),
        )
        self.play(FadeIn(wing_values), run_time=0.65)
        self.wait(1)

        # 几何辅助线：O 到两底的垂线是 y 坐标之差，和为 4；比例来自相似三角形。
        self.play(FadeOut(VGroup(big_formula, shared_note, wings_formula, common,
                                 left_wing, right_wing, shared_number, wing_values)),
                  run_time=0.8)
        bottom_foot = [o[0], a[1], 0]
        top_foot = [o[0], d[1], 0]
        bottom_h = DashedLine(o, bottom_foot, color=BLUE, dash_length=0.10)
        top_h = DashedLine(o, top_foot, color=GOLD, dash_length=0.10)
        bottom_right = right_corner(bottom_foot[0], bottom_foot[1], color=BLUE)
        top_right = right_corner(top_foot[0], top_foot[1], color=GOLD)
        foot_dots = VGroup(Dot(bottom_foot, radius=0.047, color=BLUE),
                           Dot(top_foot, radius=0.047, color=GOLD))
        ratio = MathTex(r"AO:OC=AB:CD=2:1", color=GOLD,
                        font_size=36).move_to([0, 3.5, 0])
        heights = VGroup(
            MathTex(r"h_{\mathrm{up}}=\frac43", color=GOLD,
                    font_size=34).move_to([1.25, 1.13, 0]),
            MathTex(r"h_{\mathrm{down}}=\frac83", color=BLUE,
                    font_size=34).move_to([1.15, -0.98, 0]),
        )
        self.play(Write(ratio), Create(top_h), Create(bottom_h),
                  Create(top_right), Create(bottom_right), FadeIn(foot_dots),
                  run_time=1.7)
        self.bring_to_front(outline, diagonals, dots, labels)
        self.play(Write(heights), run_time=1.1)
        height_sum = MathTex(r"\frac43+\frac83=4\,\mathrm{cm}",
                             font_size=35).move_to([0, -3.65, 0])
        top_area = MathTex(r"S_{COD}=\frac{3\times(4/3)}{2}=2",
                           color=GOLD, font_size=37).move_to([0, -4.65, 0])
        bottom_area = MathTex(r"S_{AOB}=\frac{6\times(8/3)}{2}=8",
                              color=BLUE, font_size=37).move_to([0, -5.7, 0])
        self.play(Write(height_sum), run_time=0.8)
        self.play(Write(top_area), Write(bottom_area), run_time=1.75)
        self.wait(1.2)

        self.play(FadeOut(VGroup(ratio, bottom_h, top_h, bottom_right, top_right,
                                 foot_dots, heights, height_sum, top_area, bottom_area)),
                  run_time=0.7)
        numbers = VGroup(
            MathTex("2", color=GOLD, font_size=36).move_to([0, 1.47, 0]),
            MathTex("8", color=BLUE, font_size=38).move_to([0, -1.22, 0]),
            MathTex("4", color=GREEN, font_size=37).move_to([-1.75, 0.2, 0]),
            MathTex("4", color=PINK, font_size=37).move_to([1.75, 0.2, 0]),
        )
        rule = Text("左右等积；上下面积比等于两底长度比的平方",
                    font_size=26, color=MUTED).move_to([0, -4.06, 0])
        identity = MathTex(r"S_{COD}:S_{AOB}=3^2:6^2=1:4",
                           font_size=36).move_to([0, -5.12, 0])
        total = MathTex(r"S_{ABCD}=2+4+4+8=18\,\mathrm{cm}^2",
                        color=GOLD, font_size=38).move_to([0, -6.15, 0])
        self.play(FadeIn(numbers), FadeIn(rule), run_time=1.1)
        self.play(Write(identity), Write(total), run_time=1.65)
        self.wait(2.2)

"""小学奥数｜同底等高与等积变形。运行：manim lesson.py EqualAreaMovingApex"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from manim import *
from area_model import lesson_area, lesson_triangle, triangle_area

# 使用 MANIM_PREVIEW=1 进行低分辨率预览；正式输出为 1080×1920。
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 270 if os.environ.get("MANIM_PREVIEW") == "1" else 1080
config.pixel_height = 480 if os.environ.get("MANIM_PREVIEW") == "1" else 1920
config.frame_rate = 15 if os.environ.get("MANIM_PREVIEW") == "1" else 30

BG = "#111827"
BLUE = "#60A5FA"
GREEN = "#34D399"
GOLD = "#FBBF24"
MUTED = "#94A3B8"


def xy(point):
    return [point[0], point[1], 0]


class EqualAreaMovingApex(Scene):
    """底边不动、顶点沿平行线移动，两三角形面积均为 9 cm²。"""

    def construct(self):
        self.camera.background_color = BG
        a, b, c = lesson_triangle(-2.3)
        _, _, d = lesson_triangle(2.3)
        assert triangle_area(6, 3) == lesson_area(-2.3) == lesson_area(2.3) == 9

        title = Text("同底等高，面积不变", font_size=44, color=WHITE).move_to([0, 6.25, 0])
        intro = Text("顶点移动，面积会变吗？", font_size=30, color=MUTED).move_to([0, 5.25, 0])
        base = Line(xy(a), xy(b), color=WHITE, stroke_width=6)
        guide = DashedLine([-3.65, 1.3, 0], [3.65, 1.3, 0], color=MUTED, dash_length=0.14)
        guide_label = Text("与底边平行", font_size=25, color=MUTED).move_to([0, 2.35, 0])

        original = Polygon(xy(a), xy(b), xy(c), stroke_color=BLUE,
                           fill_color=BLUE, fill_opacity=0.20, stroke_width=4)
        base_label = MathTex(r"AB=6\,\mathrm{cm}", font_size=36).move_to([0, -2.45, 0])
        height = DashedLine(xy(c), [c[0], a[1], 0], color=GOLD, dash_length=0.12)
        height_label = MathTex(r"h=3\,\mathrm{cm}", color=GOLD, font_size=32).move_to([-3.0, -0.2, 0])
        labels = VGroup(
            Text("A", font_size=28).next_to(xy(a), DOWN + LEFT, buff=0.13),
            Text("B", font_size=28).next_to(xy(b), DOWN + RIGHT, buff=0.13),
            Text("C", font_size=28, color=BLUE).next_to(xy(c), UP, buff=0.16),
        )
        vertices = VGroup(Dot(xy(a)), Dot(xy(b)), Dot(xy(c), color=BLUE))

        self.play(Write(title), FadeIn(intro), run_time=1.5)
        self.play(Create(guide), FadeIn(guide_label), Create(base), run_time=1.4)
        self.play(FadeIn(original), FadeIn(vertices), FadeIn(labels),
                  Create(height), Write(height_label), Write(base_label), run_time=1.9)

        question = MathTex(r"S=\frac{6\times3}{2}=9\,\mathrm{cm}^2",
                           font_size=45, color=GOLD).move_to([0, -4.0, 0])
        self.play(Write(question), run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(intro), FadeOut(height_label), FadeOut(height), run_time=0.7)

        apex_x = ValueTracker(c[0])
        moving = always_redraw(lambda: Polygon(
            xy(a), xy(b), [apex_x.get_value(), c[1], 0],
            stroke_color=GREEN, stroke_width=5,
            fill_color=GREEN, fill_opacity=0.26,
        ))
        moving_dot = always_redraw(lambda: Dot([apex_x.get_value(), c[1], 0], color=GREEN))
        self.play(FadeIn(moving), FadeIn(moving_dot), run_time=0.6)
        self.play(apex_x.animate.set_value(d[0]), run_time=4.0, rate_func=linear)
        d_label = Text("D", font_size=28, color=GREEN).next_to(xy(d), UP, buff=0.16)
        self.play(FadeIn(d_label), run_time=0.4)

        conclusion = MathTex(r"S_{ABC}=S_{ABD}=9\,\mathrm{cm}^2",
                             color=GREEN, font_size=43).move_to([0, -5.25, 0])
        reason = Text("共同的底边 + 相等的高 = 相等的面积", font_size=28,
                      color=WHITE).move_to([0, -6.25, 0])
        self.play(Write(conclusion), FadeIn(reason), run_time=1.8)
        self.wait(2.2)

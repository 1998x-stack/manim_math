"""同底等高：平行线上的动点、垂足和直角、长方形对角线等积拼图。

MANIM_PREVIEW=1 manim lesson.py EqualAreaMovingApex
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from manim import *
from area_model import lesson_area, lesson_triangle, triangle_area

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 270 if os.getenv("MANIM_PREVIEW") == "1" else 1080
config.pixel_height = 480 if os.getenv("MANIM_PREVIEW") == "1" else 1920
config.frame_rate = 15 if os.getenv("MANIM_PREVIEW") == "1" else 30

BG = "#111827"
BLUE = "#60A5FA"
GREEN = "#34D399"
GOLD = "#FBBF24"
MUTED = "#94A3B8"
PINK = "#F472B6"


def point(p):
    return [p[0], p[1], 0]


def corner(foot, width=0.18, color=GOLD):
    """垂足处的真实直角记号；基线向右、高线向上。"""
    x, y = foot[:2]
    return VGroup(
        Line([x, y + width, 0], [x + width, y + width, 0], color=color, stroke_width=3),
        Line([x + width, y + width, 0], [x + width, y, 0], color=color, stroke_width=3),
    )


class EqualAreaMovingApex(Scene):
    """用逐帧几何高线说明面积不变，再用长方形对角线演示公式里的除以二。"""

    def construct(self):
        self.camera.background_color = BG
        a, b, c = lesson_triangle(-2.3)
        _, _, d = lesson_triangle(2.3)
        assert triangle_area(6, 3) == lesson_area(c[0]) == lesson_area(d[0]) == 9
        title = Text("等面积法｜同底等高", font_size=43).move_to([0, 6.35, 0])
        subtitle = Text("同一条底边，顶点沿平行线移动", font_size=27, color=MUTED).move_to([0, 5.45, 0])
        self.play(Write(title), FadeIn(subtitle), run_time=1.5)

        lower = Line([-3.5, a[1], 0], [3.5, a[1], 0], color=WHITE, stroke_width=3)
        upper = DashedLine([-3.5, c[1], 0], [3.5, c[1], 0], color=MUTED, dash_length=0.17)
        original = Polygon(point(a), point(b), point(c), stroke_color=BLUE,
                           fill_color=BLUE, fill_opacity=0.16, stroke_width=3)
        a_dot = Dot(point(a), color=WHITE)
        b_dot = Dot(point(b), color=WHITE)
        c_dot = Dot(point(c), color=BLUE)
        labels = VGroup(
            Text("A", font_size=27).next_to(point(a), DOWN + LEFT, buff=0.14),
            Text("B", font_size=27).next_to(point(b), DOWN + RIGHT, buff=0.14),
            Text("C", font_size=27, color=BLUE).next_to(point(c), UP, buff=0.14),
        )
        base_label = MathTex(r"AB=6\,\mathrm{cm}", font_size=33).move_to([0, -2.53, 0])
        parallel = MathTex(r"\ell\parallel AB", font_size=31, color=MUTED).move_to([0, 2.15, 0])
        self.play(Create(lower), Create(upper), Write(parallel), run_time=1.25)
        self.play(FadeIn(original), FadeIn(a_dot), FadeIn(b_dot), FadeIn(c_dot),
                  FadeIn(labels), Write(base_label), run_time=1.6)

        # C 到 AB 的垂足 H 与三角形的底、高全部由同一份数学坐标导出。
        h0 = (c[0], a[1])
        altitude0 = DashedLine(point(c), point(h0), color=GOLD, dash_length=0.13)
        right0 = corner(point(h0))
        h_label = Text("H", font_size=23, color=GOLD).next_to(point(h0), DOWN, buff=0.12)
        height_note = MathTex(r"CH=3\,\mathrm{cm}", color=GOLD,
                              font_size=34).move_to([-2.7, 0.0, 0])
        formula = MathTex(r"S_{ABC}=\frac{6\times3}{2}=9\,\mathrm{cm}^2",
                          color=GOLD, font_size=42).move_to([0, -4.0, 0])
        self.play(Create(altitude0), Create(right0), FadeIn(h_label), Write(height_note), run_time=1.3)
        self.play(Write(formula), run_time=1.4)
        self.wait(0.7)

        self.play(FadeOut(altitude0), FadeOut(right0), FadeOut(h_label),
                  FadeOut(height_note), FadeOut(c_dot), FadeOut(labels[2]), run_time=0.65)
        apex_x = ValueTracker(c[0])
        moving = always_redraw(lambda: Polygon(
            point(a), point(b), [apex_x.get_value(), c[1], 0],
            stroke_color=GREEN, stroke_width=4, fill_color=GREEN, fill_opacity=0.26,
        ))
        moving_dot = always_redraw(lambda: Dot([apex_x.get_value(), c[1], 0], color=GREEN))
        moving_altitude = always_redraw(lambda: DashedLine(
            [apex_x.get_value(), c[1], 0], [apex_x.get_value(), a[1], 0],
            color=GOLD, dash_length=0.13,
        ))
        moving_corner = always_redraw(lambda: corner([apex_x.get_value(), a[1], 0]))
        moving_foot = always_redraw(lambda: Dot([apex_x.get_value(), a[1], 0],
                                                color=GOLD, radius=0.045))
        height_brace = always_redraw(lambda: MathTex(
            r"h=3", color=GOLD, font_size=29,
        ).next_to([apex_x.get_value(), -0.2, 0], RIGHT, buff=0.22))
        tracker_label = always_redraw(lambda: Text(
            "P", font_size=26, color=GREEN,
        ).next_to([apex_x.get_value(), c[1], 0], UP, buff=0.16))
        fixed_area = MathTex(r"S_{ABP}=9\,\mathrm{cm}^2", color=GREEN,
                             font_size=39).move_to([0, -5.15, 0])
        note = Text("底不动｜垂直距离始终是 3", font_size=28,
                    color=MUTED).move_to([0, -6.2, 0])
        self.add(moving, moving_altitude, moving_corner, moving_foot,
                 moving_dot, height_brace, tracker_label)
        self.play(Write(fixed_area), FadeIn(note), run_time=1.0)
        self.play(apex_x.animate.set_value(0), run_time=2, rate_func=linear)
        self.play(apex_x.animate.set_value(d[0]), run_time=2, rate_func=linear)
        self.wait(0.8)
        # 移除 updater 后再切换教具，避免动态对象残留在新镜头。
        self.play(FadeOut(VGroup(moving, moving_altitude, moving_corner, moving_foot,
                                 moving_dot, height_brace, tracker_label)),
                  FadeOut(VGroup(original, lower, upper, parallel, a_dot, b_dot,
                                 labels[0], labels[1], base_label, formula, fixed_area, note,
                                 subtitle)), run_time=0.9)

        # 第二幅几何图：6×3 长方形由对角线分成面积完全相等的两半。
        sub2 = Text("为什么面积公式要除以 2？", font_size=30,
                    color=MUTED).move_to([0, 5.35, 0])
        left, right, bottom, top = -3.0, 3.0, -1.5, 1.5
        e, f, g, h = ([left, bottom, 0], [right, bottom, 0],
                       [right, top, 0], [left, top, 0])
        lower_half = Polygon(e, f, g, stroke_width=0, fill_color=GREEN, fill_opacity=0.35)
        upper_half = Polygon(e, g, h, stroke_width=0, fill_color=BLUE, fill_opacity=0.35)
        rectangle = Polygon(e, f, g, h, color=WHITE, stroke_width=4)
        diagonal = Line(e, g, color=GOLD, stroke_width=4)
        dimension = VGroup(
            MathTex(r"6\,\mathrm{cm}", font_size=33).move_to([0, -2.18, 0]),
            MathTex(r"3\,\mathrm{cm}", font_size=30).move_to([3.46, 0, 0]),
        )
        equal_text = Text("同一条对角线，分成两个等面积三角形", font_size=27,
                          color=MUTED).move_to([0, -3.3, 0])
        rect_formula = MathTex(r"S_{\mathrm{rect}}=6\times3=18\,\mathrm{cm}^2",
                               font_size=37).move_to([0, -4.45, 0])
        half_formula = MathTex(r"S_{\triangle}=18\div2=9\,\mathrm{cm}^2",
                               font_size=41, color=GOLD).move_to([0, -5.55, 0])
        self.play(FadeIn(sub2), Create(rectangle), Write(dimension), run_time=1.5)
        self.play(FadeIn(lower_half), FadeIn(upper_half), Create(diagonal), run_time=1.4)
        self.bring_to_front(rectangle, diagonal)
        self.play(FadeIn(equal_text), Write(rect_formula), run_time=1.5)
        self.play(Write(half_formula), run_time=1.2)
        self.wait(2)

"""九年级上学期：相似三角形的应用——影子测高与等距河宽构造。

数学模型、图示和数值统一。影子法需同一时刻太阳光线平行且物体直立、
测量地点地面近似水平；河宽法需对岸目标 A 与本岸 B 垂直于河岸。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def shadow_model(person_height=1.0, person_shadow=0.6, building_shadow=3.0):
    """同一地面上同时测量两条影子，计算建筑高并核验日光方向。"""
    values = (person_height, person_shadow, building_shadow)
    if not all(math.isfinite(v) and v > 0 for v in values):
        raise ValueError("身高、两段影长都必须为有限正数")
    building_height = person_height * building_shadow / person_shadow
    if not math.isfinite(building_height) or building_height <= 0:
        raise ValueError("影子法高度溢出或无效")
    ground = -1.7
    data = {
        "building_foot": (-2.25, ground),
        "building_top": (-2.25, ground + building_height),
        "building_shadow": (-2.25 + building_shadow, ground),
        "person_foot": (-0.15, ground),
        "person_head": (-0.15, ground + person_height),
        "person_shadow": (-0.15 + person_shadow, ground),
    }
    big = (data["building_shadow"][0] - data["building_top"][0],
           data["building_shadow"][1] - data["building_top"][1])
    small = (data["person_shadow"][0] - data["person_head"][0],
             data["person_shadow"][1] - data["person_head"][1])
    if not math.isclose(big[0] * small[1] - big[1] * small[0], 0,
                        abs_tol=1e-9):
        raise ValueError("两道日光射线不平行，不能使用 AA 相似")
    return data, building_height


def river_model(width=3.0, interval=1.8):
    """A 对岸、B 本岸，B-C-D 等距共线，A-C-E 共线且 AB∥DE。"""
    if (not all(math.isfinite(x) and x > 0 for x in (width, interval))
            or width > 5.0 or interval > 2.0):
        raise ValueError("河宽或本岸等距区间超出可演示范围")
    bx, shore = -0.9, -0.3
    a, b = (bx, shore + width), (bx, shore)
    c, d = (bx + interval, shore), (bx + 2*interval, shore)
    e = (d[0], shore - width)
    points = dict(zip("ABCDE", (a, b, c, d, e)))
    def cross(u, v):
        return u[0]*v[1] - u[1]*v[0]
    ac, ce = (c[0]-a[0], c[1]-a[1]), (e[0]-c[0], e[1]-c[1])
    ab, de = (b[0]-a[0], b[1]-a[1]), (e[0]-d[0], e[1]-d[1])
    bc, cd = math.dist(b, c), math.dist(c, d)
    if (not math.isclose(cross(ac, ce), 0.0, abs_tol=1e-9)
            or not math.isclose(cross(ab, de), 0.0, abs_tol=1e-9)
            or not math.isclose(bc, cd, rel_tol=1e-10)
            or not math.isclose(ab[0]*(c[0]-b[0])+ab[1]*(c[1]-b[1]),
                                0.0, abs_tol=1e-9)
            or not math.isclose(math.dist(a, b), math.dist(d, e),
                                rel_tol=1e-10)):
        raise ValueError("河宽构造不满足平行、垂直、共线及等距条件")
    return points, math.dist(d, e)


def point3(point):
    return np.array([point[0], point[1], 0.0], dtype=float)


class SimilarTrianglesApp(Scene):
    FONT = "PingFang SC"
    BUILDING = "#3498db"
    PERSON = "#e74c3c"
    GREEN = "#2ecc71"
    RIVER = "#1abc9c"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font=self.FONT, font_size=19,
                                color=GRAY_B).move_to(UP * 7.0)
        self.add(self.author_info)
        self.shadow, self.building_height = shadow_model()
        self.river, self.river_width = river_model()
        self.show_opening()
        self.show_similar_review()
        self.show_building_height()
        self.show_building_summary()
        self.show_river_width()
        self.show_river_summary()
        self.show_outro()

    def clear_section(self, keep_author=True):
        active = [obj for obj in self.mobjects
                  if not keep_author or obj is not self.author_info]
        if active:
            self.play(*[FadeOut(obj) for obj in active], run_time=0.5)

    def heading(self, title, subtitle=None):
        self.play(Write(Text(title, font=self.FONT, font_size=31,
                             color=WHITE).move_to(UP * 5.85)), run_time=0.6)
        if subtitle:
            self.play(FadeIn(Text(subtitle, font=self.FONT, font_size=22,
                                  color=GRAY_A).move_to(UP * 4.85)), run_time=0.4)

    def show_opening(self):
        question = Text("不用登楼、不过河，也能测出距离吗？",
                        font=self.FONT, font_size=30, color=YELLOW)
        question.move_to(UP * 2)
        self.play(Write(question), run_time=0.9)
        self.wait(0.5)
        self.clear_section()

    def show_similar_review(self):
        self.heading("回顾：对应角相等，对应边成比例")
        a, b, c = [point3(p) for p in ((-2.9, 1.5), (-0.9, 1.5), (-2.1, 3.1))]
        smaller = [point3((x[0]*.55+2.15, x[1]*.55+0.15)) for x in (a, b, c)]
        big = Polygon(a, b, c, color=self.GREEN, stroke_width=4)
        small = Polygon(*smaller, color=YELLOW, stroke_width=4)
        self.play(Create(big), Create(small), run_time=0.85)
        statement = MathTex(r"\frac{A'B'}{AB}=\frac{B'C'}{BC}="
                            r"\frac{C'A'}{CA}=0.55",
                            font_size=32, color=YELLOW).move_to(DOWN * 3.7)
        condition = Text("对应顺序决定相似比的方向", font=self.FONT,
                         font_size=24).move_to(DOWN * 4.75)
        self.play(Write(statement), FadeIn(condition), run_time=0.8)
        self.wait(0.75)
        self.clear_section()

    def show_building_height(self):
        self.heading("应用一：影子法测量建筑物高度",
                     "同一时刻测量；光线近似平行、地面水平、物体竖直")
        s = {name: point3(p) for name, p in self.shadow.items()}
        ground = Line(LEFT*3.75 + DOWN*1.7, RIGHT*3.4 + DOWN*1.7,
                      color=GRAY_B, stroke_width=3)
        building = Line(s["building_foot"], s["building_top"],
                        color=self.BUILDING, stroke_width=9)
        person = Line(s["person_foot"], s["person_head"],
                      color=self.PERSON, stroke_width=7)
        shadows = VGroup(
            Line(s["building_foot"], s["building_shadow"],
                 color=self.GREEN, stroke_width=5),
            Line(s["person_foot"], s["person_shadow"],
                 color=YELLOW, stroke_width=5))
        rays = VGroup(
            DashedLine(s["building_top"], s["building_shadow"],
                       color=YELLOW, dash_length=0.16),
            DashedLine(s["person_head"], s["person_shadow"],
                       color=YELLOW, dash_length=0.16))
        self.play(Create(ground), Create(building), Create(person), run_time=0.8)
        self.play(*[Create(obj) for obj in shadows], run_time=0.6)
        self.play(*[Create(obj) for obj in rays], run_time=0.6)
        labels = VGroup(
            Text("建筑高 h", font=self.FONT, font_size=23,
                 color=self.BUILDING).next_to(building, LEFT, buff=0.13),
            Text("人高 1", font=self.FONT, font_size=22,
                 color=self.PERSON).next_to(person, LEFT, buff=0.12),
            Text("建筑影长 3", font=self.FONT, font_size=21)
                 .move_to(DOWN*2.25 + LEFT*1.85),
            Text("人影长 0.6", font=self.FONT, font_size=20)
                 .move_to(DOWN*2.85 + RIGHT*.55),
        )
        self.play(FadeIn(labels), run_time=0.65)
        formula = MathTex(r"\frac{h}{1}=\frac{3}{0.6}=5",
                          font_size=34, color=YELLOW).move_to(DOWN * 4.25)
        result = Text("因此建筑高为 5 个长度单位", font=self.FONT,
                      font_size=24, color=self.GREEN).move_to(DOWN * 5.35)
        self.play(Write(formula), FadeIn(result), run_time=0.85)
        self.wait(1.15)
        self.clear_section()

    def show_building_summary(self):
        self.heading("影子法：必要条件与计算")
        notes = VGroup(
            Text("同一时刻量人高、两条影长", font=self.FONT, font_size=26),
            Text("地面水平，物体直立，光线近似平行", font=self.FONT,
                 font_size=24),
            Text("影长必须大于零，统一长度单位", font=self.FONT, font_size=25),
        ).arrange(DOWN, buff=0.8).move_to(UP * 1.2)
        self.play(*[FadeIn(note) for note in notes], run_time=0.8)
        formula = MathTex(r"h=h'\cdot\frac{L}{L'}",
                          font_size=42, color=YELLOW).move_to(DOWN * 3.2)
        self.play(Write(formula), run_time=0.75)
        self.wait(0.9)
        self.clear_section()

    def show_river_width(self):
        self.heading("应用二：用等距构造测量河宽",
                     "A 在对岸，B 在本岸；AB 垂直于两岸")
        p = {name: point3(value) for name, value in self.river.items()}
        shore_top, shore_bottom = p["A"][1], p["B"][1]
        river = Polygon(
            [-3.9, shore_top, 0], [3.9, shore_top, 0],
            [3.9, shore_bottom, 0], [-3.9, shore_bottom, 0],
            color=self.RIVER, stroke_width=1, fill_color=self.RIVER,
            fill_opacity=0.15,
        )
        shores = VGroup(*[
            Line([-3.9, y, 0], [3.9, y, 0],
                 color=self.RIVER, stroke_width=3)
            for y in (shore_top, shore_bottom)
        ])
        self.play(Create(river), *[Create(line) for line in shores], run_time=0.8)
        segments = VGroup(
            DashedLine(p["A"], p["B"], color=self.PERSON, stroke_width=3),
            Line(p["B"], p["C"], color=WHITE, stroke_width=3),
            Line(p["C"], p["D"], color=WHITE, stroke_width=3),
            Line(p["D"], p["E"], color=self.GREEN, stroke_width=4),
            DashedLine(p["A"], p["E"], color=YELLOW, dash_length=0.13),
        )
        self.play(*[Create(line) for line in segments], run_time=1.2)
        dots = VGroup(*[Dot(p[name], radius=0.065, color=WHITE)
                        for name in "ABCDE"])
        positions = {"A": UP+LEFT, "B": LEFT, "C": DOWN,
                     "D": UP+RIGHT, "E": RIGHT}
        labels = VGroup(*[
            MathTex(name, font_size=27).next_to(p[name], positions[name], buff=0.1)
            for name in "ABCDE"
        ])
        self.play(FadeIn(dots), Write(labels), run_time=0.65)
        premises = MathTex(r"BC=CD,\quad AB\parallel DE,\quad A,C,E\ \text{共线}",
                           font_size=25, color=YELLOW).move_to(DOWN*4.25)
        # 中文前提用 Text，MathTex 只排纯数学，防止 LaTeX 缺字体。
        premises = VGroup(
            MathTex(r"BC=CD,\quad AB\parallel DE", font_size=27,
                    color=YELLOW),
            Text("且 A、C、E 三点共线", font=self.FONT, font_size=22),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 4.45)
        formula = MathTex(r"\triangle ABC\sim\triangle EDC",
                          font_size=33, color=self.GREEN).move_to(DOWN*5.55)
        conclusion = MathTex(r"AB=DE=3",
                             font_size=38, color=YELLOW).move_to(DOWN*6.35)
        self.play(FadeIn(premises), run_time=0.7)
        self.play(Write(formula), Write(conclusion), run_time=0.85)
        self.wait(1.15)
        self.clear_section()

    def show_river_summary(self):
        self.heading("等距法：先验构造条件")
        notes = VGroup(
            Text("A、B 分别在两岸，AB 垂直河岸", font=self.FONT,
                 font_size=24),
            Text("沿本岸取 C、D，使 BC=CD", font=self.FONT,
                 font_size=24),
            Text("过 D 作 DE∥AB，交 AC 延长线于 E", font=self.FONT,
                 font_size=24),
            Text("由 AA 相似及等距条件，得到 AB=DE", font=self.FONT,
                 font_size=24),
        ).arrange(DOWN, buff=0.55).move_to(UP * 0.4)
        self.play(*[FadeIn(note) for note in notes], run_time=0.95)
        self.wait(1.0)
        self.clear_section()

    def show_outro(self):
        takeaway = Text("测量前提要成立，图形和数据才能对应",
                        font=self.FONT, font_size=29,
                        color=YELLOW).move_to(UP * 1.0)
        self.play(Write(takeaway), run_time=0.75)
        self.wait(0.9)
        self.clear_section(keep_author=False)


# manim -ql similar_triangles_app.py SimilarTrianglesApp

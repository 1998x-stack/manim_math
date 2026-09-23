"""九年级上学期：相似三角形的性质。

对应边、高、中线、角平分线、周长与面积均由同一组三角形坐标计算。
数学值不通过显示时的小数舍入来决定，错误的几何条件直接抛出异常。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BASE = ((0.1, 1.35), (-1.55, -0.95), (1.65, -0.95))


def geometry_metrics(vertices):
    """返回实测边长、垂足、中点、角平分线足、周长与面积。"""
    if (len(vertices) != 3 or any(len(p) != 2 for p in vertices)
            or not all(math.isfinite(x) for p in vertices for x in p)):
        raise ValueError("三角形顶点必须为三个有限二维坐标")
    a, b, c = vertices
    bc = (c[0] - b[0], c[1] - b[1])
    length_bc2 = bc[0] ** 2 + bc[1] ** 2
    cross = ((b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]))
    if length_bc2 <= 1e-12 or abs(cross) <= 1e-10:
        raise ValueError("三角形不能退化")
    ab, bc_length, ca = (math.dist(a, b), math.dist(b, c),
                         math.dist(c, a))
    fraction = ((a[0] - b[0]) * bc[0] + (a[1] - b[1]) * bc[1]) / length_bc2
    foot = tuple(b[i] + fraction * bc[i] for i in range(2))
    mid = tuple((b[i] + c[i]) / 2 for i in range(2))
    # 角平分线定理：BD/DC=AB/AC，BD/BC=AB/(AB+AC)。
    split = ab / (ab + ca)
    bisector_foot = tuple(b[i] + split * bc[i] for i in range(2))
    area = abs(cross) / 2
    result = dict(
        ab=ab, bc=bc_length, ca=ca,
        perimeter=ab + bc_length + ca, area=area,
        foot=foot, altitude=math.dist(a, foot),
        midpoint=mid, median=math.dist(a, mid),
        bisector_foot=bisector_foot,
        bisector=math.dist(a, bisector_foot),
        foot_parameter=fraction, bisector_parameter=split,
    )
    if not math.isclose(result["area"],
                        result["bc"] * result["altitude"] / 2,
                        rel_tol=1e-10):
        raise ValueError("高与面积不一致")
    if not 0 < split < 1:
        raise ValueError("角平分线不落在对应边内部")
    if not math.isclose(math.dist(b, bisector_foot) /
                        math.dist(bisector_foot, c), ab / ca,
                        rel_tol=1e-10):
        raise ValueError("角平分线分边比例不正确")
    return result


def transformed_pair(base, k, rotation_degrees=15,
                     first_center=(-1.85, 1.75), second_center=(1.8, 1.65),
                     screen_scale=0.82):
    """产生两个图示三角形：长度比 k，旋转不影响各项长度性质。"""
    if (not math.isfinite(k) or k <= 0
            or not math.isfinite(rotation_degrees)
            or not math.isfinite(screen_scale) or screen_scale <= 0):
        raise ValueError("相似比与绘图尺度必须为有限正数")
    geometry_metrics(base)
    if (len(first_center) != 2 or len(second_center) != 2
            or not all(math.isfinite(x) for p in (first_center, second_center)
                       for x in p)):
        raise ValueError("屏幕中心应为有限二维坐标")
    center = tuple(sum(p[i] for p in base) / 3 for i in range(2))
    theta = math.radians(rotation_degrees)
    cos_t, sin_t = math.cos(theta), math.sin(theta)
    first = tuple(tuple(first_center[i] + screen_scale * (p[i] - center[i])
                        for i in range(2)) for p in base)
    second = tuple((second_center[0] + screen_scale * k *
                    ((p[0] - center[0]) * cos_t - (p[1] - center[1]) * sin_t),
                    second_center[1] + screen_scale * k *
                    ((p[0] - center[0]) * sin_t + (p[1] - center[1]) * cos_t))
                   for p in base)
    original, scaled = geometry_metrics(first), geometry_metrics(second)
    for metric in ("ab", "bc", "ca", "altitude", "median",
                   "bisector", "perimeter"):
        if not math.isclose(scaled[metric] / original[metric], k,
                            rel_tol=1e-9):
            raise ValueError(f"对应 {metric} 的长度比与图示不一致")
    if not math.isclose(scaled["area"] / original["area"], k * k,
                        rel_tol=1e-9):
        raise ValueError("面积比不等于相似比的平方")
    return first, second, original, scaled


def point3(p):
    return np.array((p[0], p[1], 0.0), dtype=float)


class SimilarTrianglesProperties(Scene):
    FONT = "PingFang SC"
    BLUE = "#3498db"
    RED = "#e74c3c"
    GREEN = "#2ecc71"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font=self.FONT, font_size=19,
                                color=GRAY_B).move_to(UP * 7.0)
        self.add(self.author_info)
        self.k = 0.6
        self.first, self.second, self.before, self.after = transformed_pair(
            BASE, self.k)
        self.show_opening()
        self.show_definition()
        self.show_edge_ratios()
        self.show_altitude_ratio()
        self.show_median_bisector_ratio()
        self.show_perimeter_area_ratio()
        self.show_summary()

    def clear_section(self, keep_author=True):
        active = [mob for mob in self.mobjects
                  if not keep_author or mob is not self.author_info]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.45)

    def heading(self, title, subtitle=None):
        heading = Text(title, font=self.FONT, font_size=31,
                       color=WHITE).move_to(UP * 5.8)
        self.play(Write(heading), run_time=0.5)
        if subtitle:
            caption = Text(subtitle, font=self.FONT, font_size=23,
                           color=GRAY_A).move_to(UP * 4.9)
            self.play(FadeIn(caption), run_time=0.35)

    def draw_pair(self, fill=False):
        p = dict(zip(("A", "B", "C", "D", "E", "F"),
                     (point3(q) for q in self.first + self.second)))
        triangles = VGroup(
            Polygon(*(p[n] for n in "ABC"), color=self.BLUE,
                    stroke_width=4, fill_color=self.BLUE,
                    fill_opacity=0.18 if fill else 0),
            Polygon(*(p[n] for n in "DEF"), color=self.RED,
                    stroke_width=4, fill_color=self.RED,
                    fill_opacity=0.18 if fill else 0),
        )
        labels = VGroup(*[
            MathTex(label, font_size=27).next_to(
                p[name], LEFT if name in "AD" else UP if name in "CF" else RIGHT,
                buff=0.1)
            for name, label in (("A", "A"), ("B", "B"), ("C", "C"),
                                ("D", "A^{\\prime}"), ("E", "B^{\\prime}"),
                                ("F", "C^{\\prime}"))
        ])
        self.play(*[Create(tri) for tri in triangles], run_time=0.8)
        self.play(Write(labels), run_time=0.5)
        return p

    def show_opening(self):
        question = Text("相似三角形：边长变化，周长与面积如何变化？",
                        font=self.FONT, font_size=27,
                        color=YELLOW).move_to(UP * 4.65)
        self.play(Write(question), run_time=0.8)
        self.draw_pair(fill=True)
        self.wait(0.55)
        self.clear_section()

    def show_definition(self):
        self.heading("相似比 k=0.6", "第一组三角形到第二组三角形，边长缩小到 0.6 倍")
        self.draw_pair()
        formula = MathTex(r"\triangle ABC\sim\triangle A'B'C'",
                          font_size=35, color=YELLOW).move_to(DOWN * 3.75)
        self.play(Write(formula), run_time=0.7)
        self.wait(0.8)
        self.clear_section()

    def show_edge_ratios(self):
        self.heading("性质一：对应边成比例", "边长相似比从 ABC 到 A'B'C' 为 k=0.6")
        p = self.draw_pair()
        pairs = (("A", "B", "D", "E"),
                 ("B", "C", "E", "F"),
                 ("C", "A", "F", "D"))
        for u, v, x, y in pairs:
            first = Line(p[u], p[v], color=YELLOW, stroke_width=6)
            second = Line(p[x], p[y], color=YELLOW, stroke_width=6)
            self.play(Create(first), Create(second), run_time=0.5)
            self.play(FadeOut(first), FadeOut(second), run_time=0.25)
        formula = MathTex(r"\frac{A'B'}{AB}=\frac{B'C'}{BC}="
                          r"\frac{C'A'}{CA}=k=0.6",
                          font_size=31, color=YELLOW).move_to(DOWN * 4.0)
        self.play(Write(formula), run_time=0.85)
        self.wait(0.85)
        self.clear_section()

    def show_altitude_ratio(self):
        self.heading("性质二：对应高之比为 k", "高线从对应顶点垂直到对应边 BC 与 B'C'")
        p = self.draw_pair()
        foot1, foot2 = point3(self.before["foot"]), point3(self.after["foot"])
        heights = VGroup(
            DashedLine(p["A"], foot1, color=self.GREEN, stroke_width=4),
            DashedLine(p["D"], foot2, color=self.GREEN, stroke_width=4),
        )
        self.play(*[Create(line) for line in heights], run_time=0.8)
        feet = VGroup(Dot(foot1, radius=0.075, color=YELLOW),
                      Dot(foot2, radius=0.075, color=YELLOW))
        self.play(FadeIn(feet), run_time=0.35)
        formula = MathTex(r"\frac{h_{A'}}{h_A}=k=0.6",
                          font_size=34, color=YELLOW).move_to(DOWN * 4.1)
        self.play(Write(formula), run_time=0.75)
        self.wait(0.9)
        self.clear_section()

    def show_median_bisector_ratio(self):
        self.heading("性质三：对应中线与角平分线", "它们的长度之比都等于对应边的比 k")
        p = self.draw_pair()
        medians = VGroup(
            Line(p["A"], point3(self.before["midpoint"]),
                 color=YELLOW, stroke_width=4),
            Line(p["D"], point3(self.after["midpoint"]),
                 color=YELLOW, stroke_width=4),
        )
        self.play(*[Create(line) for line in medians], run_time=0.8)
        median_text = MathTex(r"\frac{m_{A'}}{m_A}=0.6",
                              font_size=33, color=YELLOW).move_to(DOWN * 4.0)
        self.play(Write(median_text), run_time=0.7)
        self.wait(0.4)
        self.play(FadeOut(medians), FadeOut(median_text), run_time=0.4)
        bisectors = VGroup(
            Line(p["A"], point3(self.before["bisector_foot"]),
                 color=self.GREEN, stroke_width=4),
            Line(p["D"], point3(self.after["bisector_foot"]),
                 color=self.GREEN, stroke_width=4),
        )
        self.play(*[Create(line) for line in bisectors], run_time=0.8)
        bisector_text = MathTex(r"\frac{l_{A'}}{l_A}=0.6",
                                font_size=33, color=YELLOW).move_to(DOWN * 4.0)
        self.play(Write(bisector_text), run_time=0.75)
        self.wait(0.9)
        self.clear_section()

    def show_perimeter_area_ratio(self):
        self.heading("性质四：周长比 k，面积比 k²", "长度按 k 缩放，面积按 k×k 缩放")
        self.draw_pair(fill=True)
        perimeter = MathTex(r"\frac{P'}{P}=k=0.6", font_size=34,
                            color=YELLOW).move_to(DOWN * 3.6)
        area = MathTex(r"\frac{S'}{S}=k^2=0.6^2=0.36", font_size=34,
                       color=self.GREEN).move_to(DOWN * 4.75)
        note = Text("切勿把面积比写成 0.6", font=self.FONT,
                    font_size=25, color=WHITE).move_to(DOWN * 5.65)
        self.play(Write(perimeter), run_time=0.7)
        self.play(Write(area), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.05)
        self.clear_section()

    def show_summary(self):
        self.heading("相似三角形性质总结")
        formulas = VGroup(
            MathTex(r"\text{对应边、高、中线、角平分线比}=k",
                    font_size=30),
            MathTex(r"\frac{P'}{P}=k", font_size=35, color=YELLOW),
            MathTex(r"\frac{S'}{S}=k^2", font_size=35, color=self.GREEN),
        ).arrange(DOWN, buff=0.9).move_to(UP * 0.45)
        self.play(*[Write(line) for line in formulas], run_time=1)
        self.wait(1)
        self.clear_section(keep_author=False)


# manim -ql similar_triangles.py SimilarTrianglesProperties

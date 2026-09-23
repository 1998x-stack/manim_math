"""九年级上学期：相似三角形判定（AA、SAS、SSS）。

每一个三角形、对应边、对应角和比例来自同一组可测试几何输入；
错误输入立即失败，不能仅打印 WARNING 后继续展示不成立的结论。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def lengths(points):
    return tuple(math.dist(points[i], points[(i + 1) % 3]) for i in range(3))


def interior_angle(before, vertex, after):
    u = (before[0] - vertex[0], before[1] - vertex[1])
    v = (after[0] - vertex[0], after[1] - vertex[1])
    if min(math.hypot(*u), math.hypot(*v)) <= 1e-10:
        raise ValueError("角的两条边不能为零")
    return abs(math.atan2(u[0] * v[1] - u[1] * v[0],
                          u[0] * v[0] + u[1] * v[1]))


def triangle_aa(angle_a, angle_b, side_ab):
    """给定 A、B 角度（单位：度）及 AB，利用正弦定理得到 C。"""
    if (not all(math.isfinite(x) for x in (angle_a, angle_b, side_ab))
            or angle_a <= 0 or angle_b <= 0 or angle_a + angle_b >= 180
            or side_ab <= 0):
        raise ValueError("AA 条件应定义非退化三角形")
    a_rad, b_rad = math.radians(angle_a), math.radians(angle_b)
    c_rad = math.pi - a_rad - b_rad
    ac = side_ab * math.sin(b_rad) / math.sin(c_rad)
    result = ((0.0, 0.0), (side_ab, 0.0),
              (ac * math.cos(a_rad), ac * math.sin(a_rad)))
    if not math.isclose(math.degrees(interior_angle(result[1], result[0], result[2])),
                        angle_a, abs_tol=1e-9):
        raise ValueError("AA 角 A 与实际顶点不一致")
    if not math.isclose(math.degrees(interior_angle(result[2], result[1], result[0])),
                        angle_b, abs_tol=1e-9):
        raise ValueError("AA 角 B 与实际顶点不一致")
    return result


def triangle_sas(side_ab, side_ac, included_angle):
    """两条对应边及其夹角必须同时给定；非夹角不可冒充 SAS。"""
    if (not all(math.isfinite(x) for x in (side_ab, side_ac, included_angle))
            or side_ab <= 0 or side_ac <= 0
            or not 0 < included_angle < 180):
        raise ValueError("SAS 的两边必须为正，夹角须介于 0° 与 180° 之间")
    radians = math.radians(included_angle)
    return ((0.0, 0.0), (side_ab, 0.0),
            (side_ac * math.cos(radians), side_ac * math.sin(radians)))


def triangle_sss(side_ab, side_bc, side_ca):
    """三边对应 AB、BC、CA；用余弦定理精确构造第三顶点。"""
    sides = (side_ab, side_bc, side_ca)
    if (not all(math.isfinite(x) and x > 0 for x in sides)
            or not all(sides[i] + sides[(i + 1) % 3] > sides[(i + 2) % 3]
                       for i in range(3))):
        raise ValueError("SSS 三边必须满足严格三角形不等式")
    cx = (side_ab**2 + side_ca**2 - side_bc**2) / (2 * side_ab)
    cy2 = side_ca**2 - cx**2
    if cy2 <= 0:
        raise ValueError("SSS 三边生成退化三角形")
    points = ((0.0, 0.0), (side_ab, 0.0), (cx, math.sqrt(cy2)))
    if not all(math.isclose(real, expected, rel_tol=1e-10)
               for real, expected in zip(lengths(points), sides)):
        raise ValueError("构造图形的边长与 SSS 题设不一致")
    return points


def similar_pair(base, factor, first_center=(-1.75, 1.7),
                 second_center=(1.8, 1.7), diagram_scale=0.53):
    """两个三角形统一几何比例尺并分列显示，A↔D、B↔E、C↔F。"""
    if (len(base) != 3 or any(len(point) != 2 for point in base)
            or not all(math.isfinite(x) for point in base for x in point)
            or not math.isfinite(factor) or factor <= 0
            or not math.isfinite(diagram_scale) or diagram_scale <= 0):
        raise ValueError("输入的顶点、缩放比例必须有效")
    cross = ((base[1][0] - base[0][0]) * (base[2][1] - base[0][1])
             - (base[1][1] - base[0][1]) * (base[2][0] - base[0][0]))
    if abs(cross) <= 1e-9:
        raise ValueError("三角形三点不可共线")
    centroid = tuple(sum(point[i] for point in base) / 3 for i in range(2))
    first = tuple(tuple(first_center[i] + diagram_scale * (point[i] - centroid[i])
                        for i in range(2)) for point in base)
    second = tuple(tuple(second_center[i] + diagram_scale * factor
                         * (point[i] - centroid[i]) for i in range(2))
                   for point in base)
    for first_length, second_length in zip(lengths(first), lengths(second)):
        if not math.isclose(second_length / first_length, factor, rel_tol=1e-10):
            raise ValueError("显示坐标未满足对应边比例")
    for j in range(3):
        a = interior_angle(first[(j + 1) % 3], first[j], first[(j + 2) % 3])
        b = interior_angle(second[(j + 1) % 3], second[j], second[(j + 2) % 3])
        if not math.isclose(a, b, abs_tol=1e-10):
            raise ValueError("对应内角并不相等")
    return first, second


def point3(p):
    return np.array((p[0], p[1], 0.0), dtype=float)


class SimilarTriangles(Scene):
    FONT = "PingFang SC"
    BLUE = "#3498db"
    RED = "#e74c3c"
    GREEN = "#2ecc71"
    GOLD = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font=self.FONT, font_size=19,
                                color=GRAY_B).move_to(UP * 7.0)
        self.add(self.author_info)
        self.aa = triangle_aa(60, 50, 4.0)
        self.sas = triangle_sas(3.5, 2.8, 70)
        self.sss = triangle_sss(5.0, 4.0, 3.5)
        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_aa_determination()
        self.scene_4_sas_determination()
        self.scene_5_sss_determination()
        self.scene_6_summary()
        self.scene_7_tips()
        self.scene_8_outro()

    def clear_section(self, keep_author=True):
        active = [mob for mob in self.mobjects
                  if not keep_author or mob is not self.author_info]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.5)

    def heading(self, title, subtitle=None):
        title_obj = Text(title, font=self.FONT, font_size=31,
                         color=WHITE).move_to(UP * 5.85)
        self.play(Write(title_obj), run_time=0.55)
        if subtitle:
            sub = Text(subtitle, font=self.FONT, font_size=22,
                       color=GRAY_A).move_to(UP * 4.95)
            self.play(FadeIn(sub), run_time=0.35)

    def draw_pair(self, base, factor):
        small, large = similar_pair(base, factor)
        positions = dict(zip("ABCDEF", (point3(p) for p in small + large)))
        abc = Polygon(*(positions[name] for name in "ABC"),
                      color=self.BLUE, stroke_width=4)
        d_e_f = Polygon(*(positions[name] for name in "DEF"),
                        color=self.RED, stroke_width=4)
        directions = dict(A=LEFT, B=RIGHT, C=UP, D=LEFT, E=RIGHT, F=UP)
        labels = VGroup(*[
            MathTex(name, font_size=26).next_to(positions[name],
                                                directions[name], buff=0.11)
            for name in "ABCDEF"
        ])
        self.play(Create(abc), Create(d_e_f), run_time=0.9)
        self.play(Write(labels), run_time=0.4)
        return positions

    def angle_mark(self, positions, first, vertex, last, radius=0.3):
        p, q, r = positions[first], positions[vertex], positions[last]
        u, v = p[:2] - q[:2], r[:2] - q[:2]
        start = math.atan2(u[1], u[0])
        turn = math.atan2(u[0] * v[1] - u[1] * v[0],
                          u[0] * v[0] + u[1] * v[1])
        return Arc(radius=radius, start_angle=start, angle=turn,
                   arc_center=q, color=YELLOW, stroke_width=5)

    def scene_1_opening(self):
        question = Text("只知道部分对应边或角，怎样判断相似？",
                        font=self.FONT, font_size=29,
                        color=YELLOW).move_to(UP * 4.8)
        self.play(Write(question), run_time=0.8)
        self.draw_pair(self.aa, 0.6)
        self.wait(0.6)
        self.clear_section()

    def scene_2_overview(self):
        self.heading("相似三角形的三种判定", "每条判定都要匹配正确的对应顶点")
        cards = VGroup(
            Text("AA：两角分别对应相等", font=self.FONT, font_size=29,
                 color=self.BLUE),
            Text("SAS：两边对应成比例且夹角相等", font=self.FONT,
                 font_size=27, color=self.RED),
            Text("SSS：三边分别对应成比例", font=self.FONT,
                 font_size=29, color=self.GREEN),
        ).arrange(DOWN, buff=0.95).move_to(UP * 0.7)
        self.play(*[FadeIn(card, shift=UP * 0.2) for card in cards], run_time=1)
        self.wait(0.9)
        self.clear_section()

    def scene_3_aa_determination(self):
        self.heading("AA 判定：两角对应相等", "∠A=∠D=60°，∠B=∠E=50°")
        p = self.draw_pair(self.aa, 0.6)
        for first, vertex, last, counterpart in (("B", "A", "C", "D"),
                                                  ("C", "B", "A", "E")):
            x, y, z = {"A": ("E", "D", "F"),
                       "B": ("F", "E", "D")}[vertex]
            a_mark = self.angle_mark(p, first, vertex, last, 0.32)
            d_mark = self.angle_mark(p, x, y, z, 0.25)
            self.play(Create(a_mark), Create(d_mark), run_time=0.6)
            self.play(FadeOut(a_mark), FadeOut(d_mark), run_time=0.3)
        formula = MathTex(r"\angle A=\angle D,\quad\angle B=\angle E",
                          font_size=31, color=YELLOW).move_to(DOWN * 3.55)
        conclusion = MathTex(r"\triangle ABC\sim\triangle DEF",
                             font_size=38, color=self.GREEN).move_to(DOWN * 4.8)
        self.play(Write(formula), run_time=0.7)
        self.play(Write(conclusion), run_time=0.7)
        self.wait(0.95)
        self.clear_section()

    def scene_4_sas_determination(self):
        self.heading("SAS 判定：两边及夹角", "AB=3.5、AC=2.8、∠A=∠D=70°")
        p = self.draw_pair(self.sas, 0.65)
        for u, v, x, y in (("A", "B", "D", "E"), ("A", "C", "D", "F")):
            left = Line(p[u], p[v], color=YELLOW, stroke_width=6)
            right = Line(p[x], p[y], color=YELLOW, stroke_width=6)
            self.play(Create(left), Create(right), run_time=0.5)
            self.play(FadeOut(left), FadeOut(right), run_time=0.25)
        a_mark = self.angle_mark(p, "B", "A", "C")
        d_mark = self.angle_mark(p, "E", "D", "F", 0.25)
        self.play(Create(a_mark), Create(d_mark), run_time=0.5)
        # DE=3.5×0.65=2.275，DF=2.8×0.65=1.82；不把 2.275 误标成 2.28 后写精确等号。
        formula = MathTex(r"\frac{AB}{DE}=\frac{3.5}{2.275}="
                          r"\frac{AC}{DF}=\frac{2.8}{1.82}=\frac{20}{13}",
                          font_size=26, color=self.GOLD).move_to(DOWN * 3.65)
        conclusion = MathTex(r"\angle A=\angle D\ \Rightarrow\ "
                             r"\triangle ABC\sim\triangle DEF",
                             font_size=29, color=self.GREEN).move_to(DOWN * 4.85)
        self.play(Write(formula), run_time=0.85)
        self.play(Write(conclusion), run_time=0.8)
        self.wait(0.9)
        self.clear_section()

    def scene_5_sss_determination(self):
        self.heading("SSS 判定：三边对应成比例", "AB=5，BC=4，CA=3.5；按比例 0.7 绘制 DEF")
        p = self.draw_pair(self.sss, 0.7)
        for u, v, x, y in (("A", "B", "D", "E"),
                           ("B", "C", "E", "F"),
                           ("C", "A", "F", "D")):
            first = Line(p[u], p[v], color=YELLOW, stroke_width=6)
            second = Line(p[x], p[y], color=YELLOW, stroke_width=6)
            self.play(Create(first), Create(second), run_time=0.4)
            self.play(FadeOut(first), FadeOut(second), run_time=0.25)
        numbers = MathTex(r"DE=3.5,\quad EF=2.8,\quad FD=2.45",
                          font_size=27, color=YELLOW).move_to(DOWN * 3.25)
        ratio = MathTex(r"\frac{AB}{DE}=\frac{BC}{EF}="
                        r"\frac{CA}{FD}=\frac{10}{7}",
                        font_size=31, color=self.GOLD).move_to(DOWN * 4.25)
        conclusion = MathTex(r"\triangle ABC\sim\triangle DEF",
                             font_size=36, color=self.GREEN).move_to(DOWN * 5.35)
        self.play(Write(numbers), run_time=0.6)
        self.play(Write(ratio), run_time=0.75)
        self.play(Write(conclusion), run_time=0.7)
        self.wait(0.9)
        self.clear_section()

    def scene_6_summary(self):
        self.heading("三种判定方法回顾")
        cards = VGroup(
            Text("AA：两角分别对应相等", font=self.FONT, font_size=28),
            Text("SAS：两边对应成比例，且夹角相等", font=self.FONT,
                 font_size=26),
            Text("SSS：三边对应成比例", font=self.FONT, font_size=28),
        ).arrange(DOWN, buff=0.9).move_to(UP * 0.5)
        self.play(*[Write(card) for card in cards], run_time=1)
        self.wait(0.8)
        self.clear_section()

    def scene_7_tips(self):
        self.heading("判定时容易混淆的条件")
        notes = VGroup(
            Text("先确定对应顶点，再书写边的比例", font=self.FONT,
                 font_size=26),
            Text("SAS 必须是两边的夹角，不可替换成任意一个角",
                 font=self.FONT, font_size=25),
            Text("只知道一组边之比相等，不能直接判断三角形相似",
                 font=self.FONT, font_size=24),
        ).arrange(DOWN, buff=0.8).move_to(UP * 0.2)
        self.play(*[FadeIn(line) for line in notes], run_time=0.9)
        self.wait(0.9)
        self.clear_section()

    def scene_8_outro(self):
        message = Text("先核对对应关系，再选择 AA / SAS / SSS",
                       font=self.FONT, font_size=29,
                       color=YELLOW).move_to(UP * 0.7)
        self.play(Write(message), run_time=0.7)
        self.wait(1)
        self.clear_section(keep_author=False)


# manim -ql similar_triangles.py SimilarTriangles

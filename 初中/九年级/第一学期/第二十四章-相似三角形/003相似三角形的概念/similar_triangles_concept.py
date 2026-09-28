"""九年级上学期：相似三角形的概念。

所有对应点、边长、角和相似比由同一几何模型生成。每一节重新展示
真实存在的 Scene 对象，避免重复创建角、清理已替换对象和画面遮挡。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BASE_TRIANGLE = ((-1.5, 0.5), (0.5, -1.0), (1.0, 1.2))


def interior_angle(previous, vertex, following):
    """返回内角弧度与从第一条射线旋转到第二条射线的有向角。"""
    ux, uy = previous[0] - vertex[0], previous[1] - vertex[1]
    vx, vy = following[0] - vertex[0], following[1] - vertex[1]
    if math.hypot(ux, uy) <= 1e-12 or math.hypot(vx, vy) <= 1e-12:
        raise ValueError("角的两条边不能退化为零长度")
    turn = math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)
    return abs(turn), math.atan2(uy, ux), turn


def similarity_model(base, scale, first_center, second_center):
    """生成 A↔D、B↔E、C↔F 对应的两组三角形和精确数学规格。"""
    if not math.isfinite(scale) or scale <= 0:
        raise ValueError("相似比必须为有限正数")
    if len(base) != 3 or any(len(p) != 2 for p in base):
        raise ValueError("需要三个二维顶点")
    if (not all(math.isfinite(v) for p in (*base, first_center, second_center)
                for v in p)):
        raise ValueError("几何输入必须有限")
    a, b, c = base
    cross = ((b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]))
    if abs(cross) <= 1e-9:
        raise ValueError("三角形不能共线")
    centroid = tuple(sum(point[i] for point in base) / 3 for i in (0, 1))
    first = tuple(tuple(first_center[i] + point[i] - centroid[i]
                        for i in (0, 1)) for point in base)
    second = tuple(tuple(second_center[i] + scale * (point[i] - centroid[i])
                         for i in (0, 1)) for point in base)
    def edge_lengths(points):
        return tuple(math.dist(points[u], points[v])
                     for u, v in ((0, 1), (1, 2), (2, 0)))
    small_lengths, big_lengths = edge_lengths(first), edge_lengths(second)
    first_angles = tuple(interior_angle(first[(j + 1) % 3], first[j],
                                        first[(j + 2) % 3])[0]
                         for j in range(3))
    second_angles = tuple(interior_angle(second[(j + 1) % 3], second[j],
                                         second[(j + 2) % 3])[0]
                          for j in range(3))
    if not all(math.isclose(big / small, scale, rel_tol=1e-10)
               for small, big in zip(small_lengths, big_lengths)):
        raise ValueError("对应边比例与画出的几何不一致")
    if not all(math.isclose(x, y, abs_tol=1e-10)
               for x, y in zip(first_angles, second_angles)):
        raise ValueError("对应角不相等")
    if not math.isclose(sum(first_angles), math.pi, abs_tol=1e-10):
        raise ValueError("三角形内角和有误")
    return first, second, small_lengths, big_lengths, first_angles


def scene_point(point):
    return np.array((point[0], point[1], 0.0), dtype=float)


class SimilarTrianglesConcept(Scene):
    FONT = "PingFang SC"
    BLUE = "#3498db"
    RED = "#e74c3c"
    GREEN = "#2ecc71"
    GOLD = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font=self.FONT, font_size=19, color=GRAY_B)
        self.author.move_to(UP * 7.0)
        self.add(self.author)
        self.first, self.second, self.short, self.long, self.angles = similarity_model(
            BASE_TRIANGLE, 2.0, (-2.1, 2.1), (1.35, 0.1))
        self.show_opening()
        self.show_definition()
        self.show_corresponding_angles()
        self.show_corresponding_sides()
        self.show_similarity_ratio()
        self.show_congruence_special_case()
        self.show_outro()

    def clear_section(self, keep_author=True):
        active = [mob for mob in self.mobjects
                  if not keep_author or mob is not self.author]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.5)

    def heading(self, text, subtitle=None):
        title = Text(text, font=self.FONT, font_size=33,
                     color=WHITE).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.55)
        if subtitle:
            sub = Text(subtitle, font=self.FONT, font_size=23,
                       color=GRAY_A).move_to(UP * 4.95)
            self.play(FadeIn(sub), run_time=0.35)

    def draw_pair(self, first=None, second=None):
        small = self.first if first is None else first
        large = self.second if second is None else second
        coords = dict(zip("ABCDEF", [scene_point(p) for p in small + large]))
        tri_abc = Polygon(*(coords[name] for name in "ABC"),
                          color=self.BLUE, stroke_width=4)
        tri_def = Polygon(*(coords[name] for name in "DEF"),
                          color=self.RED, stroke_width=4)
        dots = VGroup(*[Dot(coords[name], radius=0.07) for name in "ABCDEF"])
        # 根据实际屏幕顶点定位，绝不复用位移前的旧坐标。
        directions = dict(A=LEFT, B=DOWN, C=UP, D=LEFT, E=DOWN, F=UP)
        labels = VGroup(*[
            MathTex(name, font_size=27).next_to(coords[name], directions[name],
                                                buff=0.12)
            for name in "ABCDEF"
        ])
        self.play(Create(tri_abc), Create(tri_def), run_time=0.8)
        self.play(FadeIn(dots), Write(labels), run_time=0.5)
        return coords

    def show_opening(self):
        hook = Text("两个三角形形状相同，大小可以不同吗？",
                    font=self.FONT, font_size=30,
                    color=YELLOW).move_to(UP * 4.9)
        self.play(Write(hook), run_time=0.8)
        self.draw_pair()
        self.wait(0.7)
        self.clear_section()

    def show_definition(self):
        self.heading("相似三角形的定义", "对应角分别相等，对应边成比例")
        self.draw_pair()
        correspondence = MathTex(r"A\leftrightarrow D,\ B\leftrightarrow E,\ C\leftrightarrow F",
                                 font_size=33, color=self.GREEN).move_to(DOWN * 3.45)
        expression = MathTex(r"\triangle ABC\sim\triangle DEF",
                             font_size=39, color=YELLOW).move_to(DOWN * 4.65)
        self.play(Write(correspondence), run_time=0.7)
        self.play(Write(expression), run_time=0.75)
        self.wait(0.9)
        self.clear_section()

    def angle_arc(self, coordinates, first, vertex, last, radius, color):
        p, q, r = coordinates[first], coordinates[vertex], coordinates[last]
        _, start, turn = interior_angle(p[:2], q[:2], r[:2])
        return Arc(radius=radius, start_angle=start, angle=turn,
                   arc_center=q, color=color, stroke_width=5)

    def show_corresponding_angles(self):
        self.heading("对应角分别相等", "按 A↔D、B↔E、C↔F 配对")
        p = self.draw_pair()
        pairs = (("B", "A", "C", "E", "D", "F", self.GREEN, 0),
                 ("C", "B", "A", "F", "E", "D", YELLOW, 1),
                 ("A", "C", "B", "D", "F", "E", ORANGE, 2))
        for u, v, w, x, y, z, color, index in pairs:
            small_arc = self.angle_arc(p, u, v, w, 0.34, color)
            large_arc = self.angle_arc(p, x, y, z, 0.46, color)
            value = math.degrees(self.angles[index])
            label = MathTex(rf"\angle {v}=\angle {y}\approx {value:.1f}^{{\circ}}",
                            font_size=29, color=color).move_to(DOWN * 4.0)
            self.play(Create(small_arc), Create(large_arc), Write(label),
                      run_time=0.7)
            self.wait(0.3)
            self.play(FadeOut(small_arc), FadeOut(large_arc), FadeOut(label),
                      run_time=0.35)
        summary = MathTex(r"\angle A=\angle D,\quad\angle B=\angle E,\quad"
                          r"\angle C=\angle F", font_size=27,
                          color=YELLOW).move_to(DOWN * 4.35)
        self.play(Write(summary), run_time=0.8)
        self.wait(0.85)
        self.clear_section()

    def show_corresponding_sides(self):
        self.heading("对应边成比例", "AB↔DE，BC↔EF，CA↔FD")
        p = self.draw_pair()
        names = (("A", "B", "D", "E"),
                 ("B", "C", "E", "F"),
                 ("C", "A", "F", "D"))
        for u, v, x, y in names:
            left = Line(p[u], p[v], color=YELLOW, stroke_width=7)
            right = Line(p[x], p[y], color=YELLOW, stroke_width=7)
            self.play(Create(left), Create(right), run_time=0.5)
            self.wait(0.2)
            self.play(FadeOut(left), FadeOut(right), run_time=0.25)
        formula = MathTex(r"\frac{DE}{AB}=\frac{EF}{BC}=\frac{FD}{CA}=2",
                          font_size=32, color=self.GOLD).move_to(DOWN * 4.0)
        note = Text("大三角形与小三角形的对应边之比都是 2",
                    font=self.FONT, font_size=22).move_to(DOWN * 5.15)
        self.play(Write(formula), FadeIn(note), run_time=0.85)
        self.wait(1)
        self.clear_section()

    def show_similarity_ratio(self):
        self.heading("相似比取决于比较方向", "由 ABC 到 DEF：对应边放大 2 倍")
        center = (0.0, 0.45)
        first, _, _, _, _ = similarity_model(BASE_TRIANGLE, 2,
                                            center, center)
        triangle = Polygon(*(scene_point(p) for p in first),
                           color=self.BLUE, stroke_width=4,
                           fill_color=self.BLUE, fill_opacity=0.15)
        self.play(Create(triangle), run_time=0.65)
        self.play(triangle.animate.scale(2).set_color(self.RED), run_time=1.5)
        forward = MathTex(r"k_{ABC\to DEF}=\frac{DE}{AB}=2",
                          font_size=32, color=YELLOW).move_to(DOWN * 4.1)
        backward = MathTex(r"k_{DEF\to ABC}=\frac{AB}{DE}=\frac12",
                           font_size=29).move_to(DOWN * 5.15)
        self.play(Write(forward), Write(backward), run_time=0.8)
        self.wait(0.9)
        self.clear_section()

    def show_congruence_special_case(self):
        self.heading("全等是相似比为 1 的特例", "对应边相等且对应角分别相等")
        first, second, small, large, angles = similarity_model(
            BASE_TRIANGLE, 1.0, (-2.0, 1.7), (1.7, 1.7))
        if not all(math.isclose(a, b) for a, b in zip(small, large)):
            raise ValueError("相似比为 1 时应为全等三角形")
        self.draw_pair(first, second)
        expressions = VGroup(
            MathTex(r"\triangle ABC\cong\triangle DEF", font_size=35,
                    color=self.GREEN),
            MathTex(r"\triangle ABC\sim\triangle DEF", font_size=35,
                    color=YELLOW),
        ).arrange(DOWN, buff=0.65).move_to(DOWN * 3.9)
        self.play(Write(expressions), run_time=0.8)
        self.wait(1)
        self.clear_section()

    def show_outro(self):
        message = Text("辨对应角、辨对应边，再写相似比",
                       font=self.FONT, font_size=30,
                       color=YELLOW).move_to(UP * 1.2)
        self.play(Write(message), run_time=0.7)
        self.wait(1)
        self.clear_section(keep_author=False)


# manim -ql similar_triangles_concept.py SimilarTrianglesConcept

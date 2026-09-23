"""九年级上学期：平行线分线段成比例定理（Manim Community Edition）。

几何数据、实际绘图、比值和字幕均来自同一组坐标。独立数学函数
不依赖 Manim，可由 tools/tests/test_audit_grade9.py 抽取并回归验证。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def proportional(a, b, c, d, tolerance=1e-9):
    """检查正线段 a:b=c:d；拒绝零分母、非有限值和伪比例。"""
    lengths = (a, b, c, d)
    if not all(math.isfinite(value) and value > 0 for value in lengths):
        raise ValueError("线段长度必须是有限正数，分母不可为零")
    return math.isclose(
        math.log(a) - math.log(b), math.log(c) - math.log(d),
        rel_tol=0.0, abs_tol=tolerance,
    )


def transversal_intersections(levels=(2.0, 0.8, -2.0)):
    """三条水平平行线截两条不平行截线，返回按高度排列的六个交点。"""
    if len(levels) != 3 or not all(math.isfinite(y) for y in levels):
        raise ValueError("需要三个有限高度")
    y1, y2, y3 = levels
    if not y1 > y2 > y3 or min(y1 - y2, y2 - y3) <= 1e-8:
        raise ValueError("三条平行线必须按顺序分开，避免退化线段")
    left = [(-2.45 + 0.25 * y, y) for y in levels]
    right = [(1.45 - 0.18 * y, y) for y in levels]
    if any(l[0] >= r[0] for l, r in zip(left, right)):
        raise ValueError("截线交叉，标签和图形次序不再适用")
    ab = math.dist(left[0], left[1])
    bc = math.dist(left[1], left[2])
    de = math.dist(right[0], right[1])
    ef = math.dist(right[1], right[2])
    if not proportional(ab, bc, de, ef):
        raise ValueError("屏幕交点与平行线比例定理不一致")
    return dict(zip("ABCDEF", left + right))


def triangle_sections(a, b, c, fraction):
    """D∈AB、E∈AC，且 AD/AB=AE/AC=fraction。"""
    if not math.isfinite(fraction) or not 0 < fraction < 1:
        raise ValueError("分点必须位于两边内部")
    if any(len(p) != 2 or not all(math.isfinite(x) for x in p)
           for p in (a, b, c)):
        raise ValueError("顶点应为有限二维坐标")
    cross = ((b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]))
    if abs(cross) <= 1e-9:
        raise ValueError("三角形不能退化为一条直线")
    d = tuple(a[i] + fraction * (b[i] - a[i]) for i in range(2))
    e = tuple(a[i] + fraction * (c[i] - a[i]) for i in range(2))
    ad, db = math.dist(a, d), math.dist(d, b)
    ae, ec = math.dist(a, e), math.dist(e, c)
    if not proportional(ad, db, ae, ec):
        raise ValueError("三角形比例推论未通过数值检查")
    de = (e[0] - d[0], e[1] - d[1])
    bc = (c[0] - b[0], c[1] - b[1])
    if not math.isclose(de[0] * bc[1] - de[1] * bc[0], 0.0,
                        abs_tol=1e-9):
        raise ValueError("分点连线 DE 不平行于 BC")
    return d, e


def screen_point(p):
    return np.array((p[0], p[1], 0.0), dtype=float)


class ParallelLinesTheorem(Scene):
    """六个教学环节：引入、三平行线定理、三角形推论、逆定理、例题、总结。"""

    FONT = "PingFang SC"
    GREEN = "#2ecc71"
    BLUE = "#3498db"
    RED = "#e74c3c"
    GOLD = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm", font=self.FONT,
            font_size=19, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.add(self.author_info)
        self.show_opening()
        self.show_three_parallel_lines()
        self.show_triangle_corollary()
        self.show_converse_theorem()
        self.show_application()
        self.show_outro()

    def clear_section(self):
        """仅淡出当前画面实际持有的对象，保留顶部作者标识。"""
        active = [mob for mob in self.mobjects if mob is not self.author_info]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.5)

    def section_title(self, heading, subheading=None):
        title = Text(heading, font=self.FONT, font_size=31,
                     color=WHITE).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.55)
        if subheading:
            subtitle = Text(subheading, font=self.FONT, font_size=23,
                            color=GRAY_A).move_to(UP * 5.0)
            self.play(FadeIn(subtitle), run_time=0.4)

    def show_opening(self):
        question = Text("三条平行线，会把两条截线怎样分段？",
                        font=self.FONT, font_size=32,
                        color=YELLOW).move_to(UP * 3)
        lines = VGroup(*[
            Line(LEFT * 2.8 + UP * y, RIGHT * 2.8 + UP * y,
                 color=self.GREEN, stroke_width=4)
            for y in (1.0, -0.2, -1.4)
        ])
        self.play(Write(question), run_time=0.8)
        self.play(*[Create(line) for line in lines], run_time=1)
        self.wait(0.5)
        self.clear_section()

    def show_three_parallel_lines(self):
        self.section_title("三条平行线截两条直线", "相邻对应线段之比相等")
        points = transversal_intersections()
        p = {key: screen_point(value) for key, value in points.items()}
        first, last = 2.75, -2.75
        left = Line(screen_point((-2.45 + .25 * first, first)),
                    screen_point((-2.45 + .25 * last, last)),
                    color=GRAY_B, stroke_width=3)
        right = Line(screen_point((1.45 - .18 * first, first)),
                     screen_point((1.45 - .18 * last, last)),
                     color=GRAY_B, stroke_width=3)
        self.play(Create(left), Create(right), run_time=0.7)
        parallels = VGroup(*[
            Line(screen_point((-3.65, y)), screen_point((3.35, y)),
                 color=self.GREEN, stroke_width=4)
            for y in (2.0, 0.8, -2.0)
        ])
        dots = VGroup(*[Dot(p[name], color=self.BLUE, radius=0.075)
                        for name in "ABCDEF"])
        labels = VGroup(*[
            MathTex(name, font_size=29).next_to(
                p[name], LEFT if name in "ABC" else RIGHT, buff=0.13)
            for name in "ABCDEF"
        ])
        self.play(*[Create(line) for line in parallels], run_time=1)
        self.play(FadeIn(dots), Write(labels), run_time=0.7)
        highlights = VGroup(*[
            Line(p[start], p[end], color=YELLOW, stroke_width=6)
            for start, end in (("A", "B"), ("B", "C"),
                               ("D", "E"), ("E", "F"))
        ])
        self.play(*[Create(segment) for segment in highlights], run_time=0.9)
        formula = MathTex(r"\frac{AB}{BC}=\frac{DE}{EF}",
                          color=self.GOLD, font_size=42).move_to(DOWN * 4.25)
        first_ratio = math.dist(points["A"], points["B"]) / math.dist(
            points["B"], points["C"])
        second_ratio = math.dist(points["D"], points["E"]) / math.dist(
            points["E"], points["F"])
        if not math.isclose(first_ratio, second_ratio, rel_tol=1e-9):
            raise ValueError("比例显示数值与实际绘图不一致")
        sample = MathTex(r"\frac{AB}{BC}=\frac{DE}{EF}=\frac{3}{7}",
                         color=YELLOW, font_size=31).move_to(DOWN * 5.35)
        self.play(Write(formula), run_time=0.8)
        self.play(Write(sample), run_time=0.65)
        self.wait(1)
        self.clear_section()

    def triangle_diagram(self, a, b, c, fraction):
        d, e = triangle_sections(a, b, c, fraction)
        coords = {key: screen_point(pt) for key, pt in
                  zip("ABCDE", (a, b, c, d, e))}
        outline = Polygon(coords["A"], coords["B"], coords["C"],
                          color=self.BLUE, stroke_width=3)
        line_de = DashedLine(coords["D"], coords["E"],
                             color=self.GREEN, stroke_width=4)
        diagram = VGroup(outline, line_de)
        dots = VGroup(*[Dot(coords[name], radius=0.075,
                            color=self.RED if name in "DE" else WHITE)
                        for name in "ABCDE"])
        directions = {"A": UP, "B": DOWN + LEFT, "C": DOWN + RIGHT,
                      "D": LEFT, "E": RIGHT}
        labels = VGroup(*[
            MathTex(name, font_size=28).next_to(
                coords[name], directions[name], buff=0.13)
            for name in "ABCDE"
        ])
        self.play(Create(outline), run_time=0.8)
        self.play(FadeIn(dots), Write(labels), Create(line_de), run_time=0.75)
        return coords

    def show_triangle_corollary(self):
        self.section_title("三角形中的平行线", "D 在 AB 上、E 在 AC 上，且 DE ∥ BC")
        a, b, c = (0.0, 2.6), (-2.5, -1.3), (2.5, -1.3)
        pts = self.triangle_diagram(a, b, c, 2 / 5)
        segments = VGroup(*[
            Line(pts[u], pts[v], stroke_width=6,
                 color=YELLOW if i in (0, 2) else self.RED)
            for i, (u, v) in enumerate((("A", "D"), ("D", "B"),
                                         ("A", "E"), ("E", "C")))
        ])
        self.play(*[Create(segment) for segment in segments], run_time=0.9)
        formula = MathTex(r"\frac{AD}{DB}=\frac{AE}{EC}=\frac{2}{3}",
                          font_size=36, color=self.GOLD).move_to(DOWN * 4.25)
        self.play(Write(formula), run_time=0.85)
        self.wait(1)
        self.clear_section()

    def show_converse_theorem(self):
        self.section_title("逆定理：对应线段成比例", "D、E 分别在 AB、AC 的内部")
        a, b, c = (0.0, 2.6), (-2.5, -1.3), (2.5, -1.3)
        points = self.triangle_diagram(a, b, c, 2 / 5)
        premise = MathTex(r"\frac{AD}{DB}=\frac{AE}{EC}",
                          font_size=39, color=self.GOLD).move_to(DOWN * 4.0)
        conclusion = MathTex(r"\therefore DE\parallel BC",
                             font_size=39, color=YELLOW).move_to(DOWN * 5.1)
        self.play(Write(premise), run_time=0.7)
        self.play(Indicate(Line(points["D"], points["E"],
                                color=self.GREEN)), run_time=0.5)
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1)
        self.clear_section()

    def show_application(self):
        self.section_title("例题：已知三段，求第四段", "DE ∥ BC，AD=2，DB=3，AE=4，求 EC")
        # 统一物理比例尺：1 单位长度 = 0.5 个 Manim 坐标单位。
        a, b, c = (0.0, 2.7), (-1.5, 0.7), (3.0, -1.3)
        assert math.isclose(math.dist(a, b), 2.5)
        assert math.isclose(math.dist(a, c), 5.0)
        pts = self.triangle_diagram(a, b, c, 2 / 5)
        data = (("A", "D", "AD=2", LEFT * 0.45),
                ("D", "B", "DB=3", LEFT * 0.5),
                ("A", "E", "AE=4", RIGHT * 0.55),
                ("E", "C", "EC=?", RIGHT * 0.55))
        known = VGroup(*[
            Text(text, font=self.FONT, font_size=23, color=YELLOW)
            .move_to((pts[u] + pts[v]) / 2 + offset)
            for u, v, text, offset in data
        ])
        self.play(Write(known), run_time=0.85)
        relation = MathTex(r"\frac{AD}{DB}=\frac{AE}{EC}",
                           font_size=34).move_to(DOWN * 3.85)
        self.play(Write(relation), run_time=0.65)
        substituted = MathTex(r"\frac{2}{3}=\frac{4}{EC}",
                              font_size=34).move_to(DOWN * 3.85)
        self.play(ReplacementTransform(relation, substituted), run_time=0.8)
        relation = substituted  # 此后只操作真正显示在 Scene 中的对象
        answer = MathTex(r"EC=\frac{3\times4}{2}=6",
                         font_size=35, color=YELLOW).move_to(DOWN * 5.25)
        self.play(Write(answer), run_time=0.75)
        self.play(Indicate(answer), run_time=0.45)
        answer_label = Text("EC=6", font=self.FONT, font_size=23,
                            color=YELLOW).move_to(known[3].get_center())
        self.play(ReplacementTransform(known[3], answer_label), run_time=0.5)
        self.wait(1.0)
        self.clear_section()

    def show_outro(self):
        heading = Text("平行线 → 对应线段成比例", font=self.FONT,
                       font_size=32, color=YELLOW).move_to(UP * 2.4)
        note = Text("使用逆定理时，先确认分点位于对应边上",
                    font=self.FONT, font_size=24).move_to(UP * 0.6)
        self.play(Write(heading), FadeIn(note), run_time=0.95)
        self.wait(1.0)
        self.play(*[FadeOut(mob) for mob in list(self.mobjects)], run_time=0.65)


# manim -ql parallel_lines_theorem.py ParallelLinesTheorem

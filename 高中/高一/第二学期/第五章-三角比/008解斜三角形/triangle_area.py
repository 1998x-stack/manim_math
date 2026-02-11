"""
三角形面积公式 - 解斜三角形
TikTok竖屏格式 1080×1920
知识点：S = ½ab sinC 及海伦公式
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TriangleArea(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"

        # Color scheme
        self.C_TRI = "#4FC3F7"
        self.C_HEIGHT = "#FFD54F"
        self.C_FORMULA = "#A5D6A7"
        self.C_HIGHLIGHT = "#FF7043"
        self.C_AREA = "#1565C0"
        self.C_EXAMPLE = "#CE93D8"

        self.setup_geometry()

        self.scene_opening()
        self.scene_basic_area()
        self.scene_derive_formula()
        self.scene_three_forms()
        self.scene_example()
        self.scene_heron()
        self.scene_outro()

    # ─────────────────────────────────────────────
    #  GEOMETRY SETUP
    # ─────────────────────────────────────────────
    def setup_geometry(self):
        """Unified geometry initialization — all coords calculated precisely."""
        SCALE = 1.25
        OFFSET = np.array([0.0, 1.5, 0.0])

        # Triangle vertices (a scalene triangle, no right angle)
        self.A = np.array([-2.2, -1.0, 0.0]) * SCALE + OFFSET
        self.B = np.array([2.0, -1.0, 0.0]) * SCALE + OFFSET
        self.C = np.array([0.6,  1.5, 0.0]) * SCALE + OFFSET

        # Side lengths
        self.side_a = np.linalg.norm(self.B - self.C)  # opposite A
        self.side_b = np.linalg.norm(self.C - self.A)  # opposite B (= CA)
        self.side_c = np.linalg.norm(self.A - self.B)  # opposite C (= AB)

        # Angles (radians)
        self.angle_A = self._angle_at_vertex(self.B, self.A, self.C)
        self.angle_B = self._angle_at_vertex(self.A, self.B, self.C)
        self.angle_C = self._angle_at_vertex(self.A, self.C, self.B)

        # Height from C to AB
        self.foot_h = self._perpendicular_foot(self.C, self.A, self.B)

        # Verify
        self._verify()

    def _angle_at_vertex(self, P1, V, P2):
        v1 = P1 - V
        v2 = P2 - V
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(np.clip(cos_a, -1.0, 1.0))

    def _perpendicular_foot(self, point, ls, le):
        line_vec = le - ls
        t = np.dot(point - ls, line_vec) / np.dot(line_vec, line_vec)
        return ls + t * line_vec

    def _verify(self):
        eps = 1e-6
        angle_sum = self.angle_A + self.angle_B + self.angle_C
        assert abs(angle_sum - np.pi) < eps, f"Angle sum error: {np.degrees(angle_sum)}"

        # Verify S formula: ½ab sinC
        h = np.linalg.norm(self.C - self.foot_h)
        S1 = 0.5 * self.side_c * h
        S2 = 0.5 * self.side_b * self.side_c * np.sin(self.angle_A)
        assert abs(S1 - S2) < eps * 10, f"Area formula error: {S1} vs {S2}"
        print(f"✓ Geometry verified. Area={S1:.4f}")

    # ─────────────────────────────────────────────
    #  HELPERS
    # ─────────────────────────────────────────────
    def _make_triangle(self, **kwargs):
        return Polygon(self.A, self.B, self.C,
                       stroke_color=self.C_TRI, stroke_width=3,
                       fill_color=self.C_AREA, fill_opacity=0.15,
                       **kwargs)

    def _make_vertex_labels(self, tri_color=WHITE):
        lA = Text("A", font="Noto Sans CJK SC", font_size=24, color=tri_color).next_to(self.A, DL, buff=0.12)
        lB = Text("B", font="Noto Sans CJK SC", font_size=24, color=tri_color).next_to(self.B, DR, buff=0.12)
        lC = Text("C", font="Noto Sans CJK SC", font_size=24, color=tri_color).next_to(self.C, UP, buff=0.12)
        return VGroup(lA, lB, lC)

    def _author_tag(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC", font_size=19, color=GRAY_B
        ).move_to(UP * 7.2)

    # ─────────────────────────────────────────────
    #  SCENE 1: OPENING HOOK
    # ─────────────────────────────────────────────
    def scene_opening(self):
        author = self._author_tag()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text("怎么求斜三角形面积？", font="Noto Sans CJK SC",
                    font_size=40, color=self.C_HIGHLIGHT).move_to(UP * 5.5)
        sub  = Text("高都找不到！", font="Noto Sans CJK SC",
                    font_size=28, color=GRAY_A).move_to(UP * 4.7)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # Show triangle
        tri = self._make_triangle()
        labels = self._make_vertex_labels()
        self.play(Create(tri), run_time=1.0)
        self.play(Write(labels), run_time=0.5)

        # Fake "search for height" — dashed vertical that misses the triangle
        confused_line = DashedLine(
            self.B + UP * 3, self.B,
            dash_length=0.12, color=GRAY_B, stroke_width=2
        )
        question_mark = Text("?", font_size=40, color=YELLOW).next_to(confused_line, RIGHT, buff=0.15)
        self.play(Create(confused_line), FadeIn(question_mark), run_time=0.6)
        self.wait(0.6)

        answer = Text("用正弦定理解决！", font="Noto Sans CJK SC",
                      font_size=30, color=self.C_FORMULA).move_to(DOWN * 4.5)
        self.play(Write(answer), run_time=0.6)
        self.wait(0.6)

        self.play(
            FadeOut(hook), FadeOut(sub), FadeOut(confused_line),
            FadeOut(question_mark), FadeOut(answer),
            run_time=0.5
        )
        self.tri = tri
        self.labels = labels
        self.author = author

    # ─────────────────────────────────────────────
    #  SCENE 2: BASIC AREA S = ½ × base × height
    # ─────────────────────────────────────────────
    def scene_basic_area(self):
        title = Text("基础公式回顾", font="Noto Sans CJK SC",
                     font_size=34, color=GOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # Draw height from C to AB
        height_line = Line(self.C, self.foot_h,
                           color=self.C_HEIGHT, stroke_width=2.5)
        # Right angle mark at foot
        ra = self._right_angle_mark(self.foot_h, self.C, self.A, size=0.18)

        h_label = Text("h", font_size=22, color=self.C_HEIGHT).next_to(
            (self.C + self.foot_h) / 2, RIGHT, buff=0.12)

        self.play(Create(height_line), FadeIn(ra), FadeIn(h_label), run_time=0.8)

        # Label "a" on AB (base)
        a_label = MathTex("a", color=self.C_TRI, font_size=26).next_to(
            (self.A + self.B) / 2, DOWN, buff=0.2)
        self.play(FadeIn(a_label), run_time=0.4)

        # Formula S = ½bh
        f1 = MathTex(r"S = \frac{1}{2} \times a \times h",
                     font_size=34, color=self.C_FORMULA).move_to(DOWN * 3.8)
        self.play(Write(f1), run_time=0.8)
        self.wait(1.0)

        # But h is unknown for oblique triangle
        note = Text("但h不好直接求...", font="Noto Sans CJK SC",
                    font_size=26, color=self.C_HIGHLIGHT).move_to(DOWN * 5.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(f1), FadeOut(note),
            FadeOut(a_label),
            run_time=0.5
        )
        self.height_line = height_line
        self.ra = ra
        self.h_label = h_label

    # ─────────────────────────────────────────────
    #  SCENE 3: DERIVE S = ½ab sinC
    # ─────────────────────────────────────────────
    def scene_derive_formula(self):
        title = Text("关键推导", font="Noto Sans CJK SC",
                     font_size=34, color=GOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # Show angle C
        line_CA = Line(self.C, self.A, color=self.C_TRI)
        line_CB = Line(self.C, self.B, color=self.C_TRI)

        # Angle arc at C
        v1 = self.A - self.C
        v2 = self.B - self.C
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        use_other = cross_z < 0
        angle_C_arc = Angle(line_CA, line_CB, radius=0.45,
                            color=self.C_EXAMPLE, other_angle=use_other)

        C_label = MathTex("C", color=self.C_EXAMPLE, font_size=24).next_to(
            self.C + np.array([0.7, -0.3, 0]), RIGHT, buff=0.05)
        self.play(Create(angle_C_arc), FadeIn(C_label), run_time=0.6)

        # Side labels b (CA) and c (AB→ but we'll use a for AB and b for CA)
        mid_CA = (self.C + self.A) / 2
        mid_CB = (self.C + self.B) / 2
        b_label = MathTex("b", color=self.C_TRI, font_size=26).next_to(mid_CA, LEFT, buff=0.15)
        a_label = MathTex("a", color=self.C_TRI, font_size=26).next_to(mid_CB, RIGHT, buff=0.15)
        self.play(FadeIn(b_label), FadeIn(a_label), run_time=0.4)

        # Step 1: h = b sinC
        step1_title = Text("在直角三角形中：", font="Noto Sans CJK SC",
                           font_size=24, color=GRAY_A).move_to(DOWN * 3.6)
        step1 = MathTex(r"h = b \sin C",
                        font_size=34, color=self.C_HEIGHT).move_to(DOWN * 4.3)
        self.play(FadeIn(step1_title), Write(step1), run_time=0.9)
        self.wait(0.8)

        # Step 2: Substitute
        step2_title = Text("代入面积公式：", font="Noto Sans CJK SC",
                           font_size=24, color=GRAY_A).move_to(DOWN * 5.1)
        step2 = MathTex(r"S = \frac{1}{2} \cdot a \cdot h = \frac{1}{2} \cdot a \cdot b \sin C",
                        font_size=28, color=self.C_FORMULA).move_to(DOWN * 5.8)
        self.play(FadeIn(step2_title), Write(step2), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(step1_title), FadeOut(step1),
            FadeOut(step2_title),
            FadeOut(angle_C_arc), FadeOut(C_label),
            FadeOut(b_label), FadeOut(a_label),
            FadeOut(self.height_line), FadeOut(self.ra), FadeOut(self.h_label),
            run_time=0.6
        )
        self.step2 = step2

    # ─────────────────────────────────────────────
    #  SCENE 4: THREE EQUIVALENT FORMS
    # ─────────────────────────────────────────────
    def scene_three_forms(self):
        title = Text("三种等价形式", font="Noto Sans CJK SC",
                     font_size=34, color=GOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # Transform step2 into highlighted box
        f_main = MathTex(
            r"S = \frac{1}{2}ab\sin C",
            font_size=38, color=self.C_FORMULA
        ).move_to(DOWN * 3.4)
        self.play(ReplacementTransform(self.step2, f_main), run_time=0.8)

        # Box around main formula
        box = SurroundingRectangle(f_main, color=self.C_FORMULA, buff=0.2, corner_radius=0.1)
        self.play(Create(box), run_time=0.5)

        # Other two forms
        f2 = MathTex(r"= \frac{1}{2}bc\sin A", font_size=32, color="#81D4FA").move_to(DOWN * 4.5)
        f3 = MathTex(r"= \frac{1}{2}ac\sin B", font_size=32, color="#80DEEA").move_to(DOWN * 5.4)
        self.play(FadeIn(f2, shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(f3, shift=LEFT * 0.3), run_time=0.5)

        equal_note = Text("三个角都可以用！", font="Noto Sans CJK SC",
                          font_size=26, color=self.C_HIGHLIGHT).move_to(DOWN * 6.3)
        self.play(FadeIn(equal_note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(f_main), FadeOut(box),
            FadeOut(f2), FadeOut(f3), FadeOut(equal_note),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    #  SCENE 5: EXAMPLE
    # ─────────────────────────────────────────────
    def scene_example(self):
        title = Text("例题", font="Noto Sans CJK SC",
                     font_size=36, color=GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.4)

        # Problem statement
        prob1 = Text("已知三角形中：", font="Noto Sans CJK SC",
                     font_size=26, color=GRAY_A).move_to(UP * 5.0)
        prob2 = MathTex(r"a = 6, \quad b = 4, \quad C = 30^\circ",
                        font_size=30, color=WHITE).move_to(UP * 4.3)
        prob3 = Text("求三角形的面积", font="Noto Sans CJK SC",
                     font_size=26, color=self.C_HIGHLIGHT).move_to(UP * 3.6)
        self.play(FadeIn(prob1), Write(prob2), FadeIn(prob3), run_time=1.0)

        # Draw an example triangle (scaled for this example)
        # a=6, b=4, C=30° → place C at origin, B along x-axis
        ex_scale = 0.52
        ex_offset = np.array([0.0, 1.2, 0.0])
        eA = np.array([-1.5, -0.8, 0.0]) * ex_scale + ex_offset
        eB = np.array([2.5, -0.8, 0.0]) * ex_scale + ex_offset
        # C angle = 30°, b=CA (4 units), a=CB (6 units) — use actual positions
        ex_C = np.array([0.0, 1.5, 0.0]) * ex_scale + ex_offset

        ex_tri = Polygon(eA, eB, ex_C,
                         stroke_color=self.C_TRI, stroke_width=2.5,
                         fill_color=self.C_AREA, fill_opacity=0.2)

        eA_l = Text("A", font_size=20, color=WHITE).next_to(eA, DL, buff=0.08)
        eB_l = Text("B", font_size=20, color=WHITE).next_to(eB, DR, buff=0.08)
        eC_l = Text("C", font_size=20, color=WHITE).next_to(ex_C, UP, buff=0.08)

        # Labels a, b
        mid_CB = (ex_C + eB) / 2
        mid_CA = (ex_C + eA) / 2
        a_l = MathTex("a=6", font_size=20, color=self.C_TRI).next_to(mid_CB, RIGHT, buff=0.1)
        b_l = MathTex("b=4", font_size=20, color=self.C_TRI).next_to(mid_CA, LEFT, buff=0.1)
        C_angle_l = MathTex(r"30^\circ", font_size=20, color=self.C_EXAMPLE).next_to(ex_C, DOWN + RIGHT, buff=0.1)

        self.play(Create(ex_tri), run_time=0.7)
        self.play(Write(VGroup(eA_l, eB_l, eC_l)), run_time=0.4)
        self.play(FadeIn(a_l), FadeIn(b_l), FadeIn(C_angle_l), run_time=0.4)

        # Step by step solution
        sol1 = MathTex(r"S = \frac{1}{2} \cdot a \cdot b \cdot \sin C",
                       font_size=30, color=self.C_FORMULA).move_to(DOWN * 2.8)
        self.play(Write(sol1), run_time=0.7)

        sol2 = MathTex(r"= \frac{1}{2} \times 6 \times 4 \times \sin 30^\circ",
                       font_size=28, color=self.C_FORMULA).move_to(DOWN * 3.8)
        self.play(Write(sol2), run_time=0.7)

        sin30 = MathTex(r"\sin 30^\circ = \frac{1}{2}", font_size=26, color=YELLOW).move_to(DOWN * 4.8)
        self.play(FadeIn(sin30, shift=LEFT * 0.2), run_time=0.5)

        sol3 = MathTex(r"= \frac{1}{2} \times 6 \times 4 \times \frac{1}{2} = 6",
                       font_size=28, color=self.C_FORMULA).move_to(DOWN * 5.8)
        self.play(Write(sol3), run_time=0.8)

        result_box = SurroundingRectangle(sol3, color=self.C_HIGHLIGHT, buff=0.15, corner_radius=0.08)
        self.play(Create(result_box), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(prob1), FadeOut(prob2), FadeOut(prob3),
            FadeOut(ex_tri), FadeOut(eA_l), FadeOut(eB_l), FadeOut(eC_l),
            FadeOut(a_l), FadeOut(b_l), FadeOut(C_angle_l),
            FadeOut(sol1), FadeOut(sol2), FadeOut(sin30),
            FadeOut(sol3), FadeOut(result_box),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    #  SCENE 6: HERON'S FORMULA
    # ─────────────────────────────────────────────
    def scene_heron(self):
        title = Text("海伦公式（三边已知）", font="Noto Sans CJK SC",
                     font_size=30, color=GOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # When to use note
        when = Text("已知三边 a, b, c 时使用：", font="Noto Sans CJK SC",
                    font_size=26, color=GRAY_A).move_to(UP * 4.6)
        self.play(FadeIn(when), run_time=0.5)

        # s = (a+b+c)/2
        f_s = MathTex(r"s = \frac{a + b + c}{2}",
                      font_size=34, color=self.C_FORMULA).move_to(UP * 3.5)
        self.play(Write(f_s), run_time=0.8)

        # Heron
        f_heron = MathTex(
            r"S = \sqrt{s(s-a)(s-b)(s-c)}",
            font_size=34, color=self.C_FORMULA
        ).move_to(UP * 2.3)
        self.play(Write(f_heron), run_time=0.9)

        heron_box = SurroundingRectangle(f_heron, color="#CE93D8", buff=0.2, corner_radius=0.1)
        self.play(Create(heron_box), run_time=0.4)

        # Brief explanation
        note1 = Text("s 是三角形的半周长", font="Noto Sans CJK SC",
                     font_size=24, color=GRAY_A).move_to(DOWN * 0.8)
        note2 = Text("无需求角度就能算面积！", font="Noto Sans CJK SC",
                     font_size=26, color=self.C_HIGHLIGHT).move_to(DOWN * 1.8)
        self.play(FadeIn(note1), FadeIn(note2, shift=UP * 0.2), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(when), FadeOut(f_s),
            FadeOut(f_heron), FadeOut(heron_box),
            FadeOut(note1), FadeOut(note2),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    #  SCENE 7: OUTRO
    # ─────────────────────────────────────────────
    def scene_outro(self):
        # Summary card
        summary_title = Text("三角形面积公式", font="Noto Sans CJK SC",
                             font_size=36, color=GOLD).move_to(UP * 5.0)
        self.play(Write(summary_title), run_time=0.6)

        line1 = MathTex(r"S = \frac{1}{2}ab\sin C", font_size=34,
                        color=self.C_FORMULA).move_to(UP * 3.8)
        line2 = MathTex(r"= \frac{1}{2}bc\sin A = \frac{1}{2}ac\sin B",
                        font_size=28, color="#81D4FA").move_to(UP * 2.9)
        line3_title = Text("三边已知：", font="Noto Sans CJK SC",
                           font_size=26, color=GRAY_A).move_to(UP * 1.8)
        line3 = MathTex(r"S = \sqrt{s(s-a)(s-b)(s-c)}", font_size=28,
                        color=self.C_EXAMPLE).move_to(UP * 1.0)

        self.play(Write(line1), run_time=0.6)
        self.play(FadeIn(line2), run_time=0.4)
        self.play(FadeIn(line3_title), Write(line3), run_time=0.7)
        self.wait(0.5)

        # Follow CTA
        follow = Text("关注我，获得更多数学技巧！", font="Noto Sans CJK SC",
                      font_size=30, color=self.C_HIGHLIGHT).move_to(DOWN * 2.0)
        self.play(FadeIn(follow, scale=1.05), run_time=0.6)

        author_big = Text("上海初高中数学直通车", font="Noto Sans CJK SC",
                          font_size=32, color=WHITE).move_to(DOWN * 3.2)
        author_id  = Text("@emptyandcalm", font="Noto Sans CJK SC",
                          font_size=24, color=GRAY_B).move_to(DOWN * 4.0)

        self.play(
            Transform(self.author, author_big),
            FadeIn(author_id),
            run_time=0.8
        )
        self.wait(1.5)

    # ─────────────────────────────────────────────
    #  UTILITY
    # ─────────────────────────────────────────────
    def _right_angle_mark(self, corner, p1, p2, size=0.2):
        """Draw a small square to indicate a right angle."""
        v1 = p1 - corner
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = p2 - corner
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            stroke_color=self.C_HEIGHT, stroke_width=1.5, fill_opacity=0
        )
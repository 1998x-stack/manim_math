"""
点到直线的距离 - Point-to-Line Distance Formula
TikTok 竖屏教学动画 (1080×1920)

知识点: 高二解析几何 - 点到直线距离公式
d = |Ax₀ + By₀ + C| / √(A² + B²)

作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─── Global Config ──────────────────────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ─── Color Palette ──────────────────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
C_LINE1        = "#3498db"    # blue  – main line l
C_LINE2        = "#9b59b6"    # purple – parallel line l₂
C_POINT        = "#e74c3c"    # red   – point P
C_FOOT         = "#2ecc71"    # green – foot Q
C_PERP         = "#f39c12"    # orange – perpendicular segment
C_FORMULA_HL   = YELLOW       # formula highlight
C_AUX          = GRAY_B       # auxiliary / axes
FONT_CN        = "PingFang SC"


class PointToLineDistance(Scene):
    """
    教学动画: 点到直线的距离公式推导与应用
    场景流程:
      S1 开场钩子
      S2 建立问题模型
      S3 作垂线 + 直角标记
      S4 公式展示与解读
      S5 代入计算示例
      S6 平行线距离拓展
      S7 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene1_opening()
        self.scene2_model()
        self.scene3_perpendicular()
        self.scene4_formula()
        self.scene5_calculation()
        self.scene6_parallel()
        self.scene7_outro()

    # ═══════════════════════════════════════════════════════════════════════
    # GEOMETRY SETUP (all coords calculated once)
    # ═══════════════════════════════════════════════════════════════════════
    def setup_geometry(self):
        """Compute all geometric data; store as instance attributes."""
        # ── Line l: 3x + 4y − 12 = 0  ─────────────────────────────────────
        self.A_c = 3
        self.B_c = 4
        self.C_c = -12   # as in Ax+By+C=0

        # ── Point P(1,1) ─────────────────────────────────────────────────
        self.Px, self.Py = 1.0, 1.0

        # ── Perpendicular foot Q ──────────────────────────────────────────
        # t = -(A·x0 + B·y0 + C) / (A² + B²)
        t = -(self.A_c * self.Px + self.B_c * self.Py + self.C_c) / (self.A_c**2 + self.B_c**2)
        self.Qx = self.Px + self.A_c * t   # 1.6
        self.Qy = self.Py + self.B_c * t   # 1.8
        self.d  = abs(self.A_c * self.Px + self.B_c * self.Py + self.C_c) / np.sqrt(self.A_c**2 + self.B_c**2)

        # ── Parallel line l₂: 3x + 4y − 2 = 0 ───────────────────────────
        self.C2_c = -2
        self.d_parallel = abs(self.C_c - self.C2_c) / np.sqrt(self.A_c**2 + self.B_c**2)  # 2.0

        # ── Axes parameters ───────────────────────────────────────────────
        # x_range, y_range for the coordinate system
        self.ax_x_range = [-0.5, 4.5, 1]
        self.ax_y_range = [-0.5, 4.0, 1]
        self.ax_x_len   = 3.6
        self.ax_y_len   = 3.2

        # Validate
        assert abs(self.Qx - 1.6) < 1e-9
        assert abs(self.Qy - 1.8) < 1e-9
        assert abs(self.d  - 1.0) < 1e-9
        assert abs(self.d_parallel - 2.0) < 1e-9
        print("✓ setup_geometry() passed")

    # ═══════════════════════════════════════════════════════════════════════
    # HELPERS
    # ═══════════════════════════════════════════════════════════════════════
    def build_axes(self, shift_vec=ORIGIN):
        """Create coordinate axes and return (axes, axes_group)."""
        axes = Axes(
            x_range=self.ax_x_range,
            y_range=self.ax_y_range,
            x_length=self.ax_x_len,
            y_length=self.ax_y_len,
            axis_config={
                "color": C_AUX,
                "stroke_width": 1.5,
                "include_tip": True,
                "tip_length": 0.15,
                "include_numbers": True,
                "font_size": 16,
            },
            tips=True,
        ).shift(shift_vec)
        # Labels
        x_label = MathTex("x", font_size=22, color=C_AUX).next_to(axes.x_axis.get_end(), RIGHT, buff=0.05)
        y_label = MathTex("y", font_size=22, color=C_AUX).next_to(axes.y_axis.get_end(), UP,    buff=0.05)
        return axes, VGroup(axes, x_label, y_label)

    def line_l_on_axes(self, axes, color=C_LINE1):
        """Draw line 3x+4y-12=0 on axes (from x=0 to x=4)."""
        # y = (12 - 3x)/4
        return axes.plot(lambda x: (12 - 3*x)/4,
                         x_range=[0, 4],
                         color=color, stroke_width=3)

    def line_l2_on_axes(self, axes, color=C_LINE2):
        """Draw line 3x+4y-2=0 on axes (from x=0 to x=4)."""
        # y = (2 - 3x)/4
        return axes.plot(lambda x: (2 - 3*x)/4,
                         x_range=[0, 4],
                         color=color, stroke_width=3)

    def right_angle_mark(self, corner_screen, v1_screen, v2_screen, size=0.15):
        """
        Manual right-angle square mark (most reliable in all Manim versions).
        corner_screen: screen coordinate of the right angle corner
        v1_screen, v2_screen: two directions (not normalised)
        """
        u1 = (v1_screen - corner_screen)
        u1 = u1 / np.linalg.norm(u1) * size
        u2 = (v2_screen - corner_screen)
        u2 = u2 / np.linalg.norm(u2) * size
        return Polygon(
            corner_screen,
            corner_screen + u1,
            corner_screen + u1 + u2,
            corner_screen + u2,
            color=C_FORMULA_HL,
            stroke_width=1.5,
            fill_opacity=0,
        )

    def author_badge(self):
        return Text("上海初高中数学直通车 @emptyandcalm",
                    font=FONT_CN, font_size=18, color=GRAY_B).move_to(UP * 7)

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 1 – Opening Hook  (~5 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene1_opening(self):
        # Author badge
        badge = self.author_badge()
        self.play(FadeIn(badge, shift=DOWN * 0.2), run_time=0.4)

        # Title
        title = Text("点到直线的距离", font=FONT_CN, font_size=44, color=GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.8)

        # Subtitle hook
        hook = Text("这条线到那个点究竟有多远？", font=FONT_CN, font_size=26, color=WHITE).move_to(UP * 4.9)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)

        # Show axes + line + point as teaser
        axes, axes_group = self.build_axes(shift_vec=UP * 1.5)
        self.play(FadeIn(axes_group), run_time=0.8)

        line_l = self.line_l_on_axes(axes)
        self.play(Create(line_l), run_time=0.8)

        p_dot = Dot(axes.c2p(self.Px, self.Py), color=C_POINT, radius=0.12)
        self.play(FadeIn(p_dot, scale=0.5), run_time=0.5)
        self.play(Flash(p_dot, color=C_POINT, flash_radius=0.25), run_time=0.4)

        # Show a few "wrong" candidate lines (not the shortest)
        foot_screen = axes.c2p(self.Qx, self.Qy)
        p_screen    = axes.c2p(self.Px, self.Py)

        # "random" candidate endpoints
        cands = [
            axes.c2p(0, 3),      # hit left-top
            axes.c2p(2.5, 0.75), # arbitrary
            axes.c2p(4, 0),      # hit right-bottom
        ]
        cand_lines = VGroup(*[
            DashedLine(p_screen, c, color=GRAY, dash_length=0.08, stroke_width=1.5)
            for c in cands
        ])
        self.play(Create(cand_lines), run_time=0.8)

        wrong_q = Text("哪条最短?", font=FONT_CN, font_size=26, color=YELLOW).move_to(DOWN * 3.8)
        self.play(FadeIn(wrong_q), run_time=0.4)
        self.wait(0.5)

        # Answer: the perpendicular!
        perp_line_teaser = Line(p_screen, foot_screen, color=C_PERP, stroke_width=3)
        self.play(FadeOut(cand_lines), FadeOut(wrong_q), run_time=0.3)
        self.play(Create(perp_line_teaser), run_time=0.7)

        answer = Text("垂线段最短!", font=FONT_CN, font_size=30, color=C_PERP).move_to(DOWN * 3.8)
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # Fade out and keep axes, badge, line, p_dot for next scene
        self.play(FadeOut(title), FadeOut(hook), FadeOut(answer),
                  FadeOut(perp_line_teaser), run_time=0.5)

        # Store for re-use
        self._badge       = badge
        self._axes        = axes
        self._axes_group  = axes_group
        self._line_l      = line_l
        self._p_dot       = p_dot

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 2 – Setup the Model  (~6 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene2_model(self):
        axes  = self._axes
        p_dot = self._p_dot

        # Section title
        sec_title = Text("建立数学模型", font=FONT_CN, font_size=36, color=GOLD).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        # Label the line
        line_label_cn = Text("直线 l:", font=FONT_CN, font_size=22, color=C_LINE1).move_to(UP * 4.8 + LEFT * 2)
        line_label_eq = MathTex(r"3x + 4y - 12 = 0", font_size=26, color=C_LINE1).next_to(line_label_cn, RIGHT, buff=0.15)
        self.play(FadeIn(line_label_cn), Write(line_label_eq), run_time=0.7)

        # General form
        gen_cn  = Text("一般式:", font=FONT_CN, font_size=22, color=GRAY_A).move_to(UP * 4.1 + LEFT * 2)
        gen_eq  = MathTex(r"Ax + By + C = 0", font_size=26, color=GRAY_A).next_to(gen_cn, RIGHT, buff=0.15)
        self.play(FadeIn(gen_cn), Write(gen_eq), run_time=0.6)

        # Label point P
        p_label = MathTex(r"P(1, 1)", font_size=24, color=C_POINT).next_to(p_dot, DL, buff=0.15)
        self.play(FadeIn(p_label), run_time=0.5)

        # General point label
        p_gen_cn = Text("点 P:", font=FONT_CN, font_size=22, color=C_POINT).move_to(UP * 3.4 + LEFT * 2.5)
        p_gen_eq = MathTex(r"P(x_0,\, y_0)", font_size=26, color=C_POINT).next_to(p_gen_cn, RIGHT, buff=0.15)
        self.play(FadeIn(p_gen_cn), Write(p_gen_eq), run_time=0.6)

        # Question text
        q_cn   = Text("求 d = ?", font=FONT_CN, font_size=26, color=YELLOW).move_to(DOWN * 4)
        q_sub  = Text("(P 到直线 l 的距离)", font=FONT_CN, font_size=20, color=GRAY_A).next_to(q_cn, DOWN, buff=0.2)
        self.play(FadeIn(q_cn), FadeIn(q_sub), run_time=0.6)
        self.wait(1.2)

        # Clean up scene 2 specific labels before scene 3
        self.play(FadeOut(sec_title), FadeOut(q_cn), FadeOut(q_sub), run_time=0.4)

        # Store
        self._line_label_cn = line_label_cn
        self._line_label_eq = line_label_eq
        self._gen_cn   = gen_cn
        self._gen_eq   = gen_eq
        self._p_label  = p_label
        self._p_gen_cn = p_gen_cn
        self._p_gen_eq = p_gen_eq

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 3 – Draw Perpendicular  (~7 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene3_perpendicular(self):
        axes  = self._axes
        p_dot = self._p_dot

        sec_title = Text("过 P 作 l 的垂线", font=FONT_CN, font_size=32, color=GOLD).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        p_screen = axes.c2p(self.Px, self.Py)
        q_screen = axes.c2p(self.Qx, self.Qy)

        # Draw perpendicular segment PQ (orange dashed → solid)
        perp = Line(p_screen, q_screen, color=C_PERP, stroke_width=3)
        self.play(Create(perp), run_time=0.8)

        # Foot Q
        q_dot   = Dot(q_screen, color=C_FOOT, radius=0.10)
        q_label = MathTex(r"Q", font_size=24, color=C_FOOT).next_to(q_dot, RIGHT + UP * 0.5, buff=0.12)
        self.play(FadeIn(q_dot), FadeIn(q_label), run_time=0.5)

        # Right angle mark at Q between PQ and the line
        # Vector from Q toward P
        v_QP = p_screen - q_screen
        # Vector from Q along the line direction (positive x side)
        q_line_right = axes.c2p(self.Qx + 0.5 * self.B_c, self.Qy + 0.5 * (-self.A_c))  # direction (B,-A)
        right_mark = self.right_angle_mark(q_screen, p_screen, q_line_right, size=0.18)
        self.play(Create(right_mark), run_time=0.5)

        perp_label_cn = Text("PQ ⊥ l", font=FONT_CN, font_size=22, color=C_PERP).move_to(DOWN * 3.6)
        self.play(FadeIn(perp_label_cn), run_time=0.4)
        self.wait(0.5)

        # Show distance brace / label
        d_label = MathTex(r"d = |PQ|", font_size=26, color=C_FORMULA_HL).move_to(DOWN * 4.3)
        self.play(Write(d_label), run_time=0.6)
        self.wait(1.0)

        # Explain derivation approach
        derive_cn = Text("推导方法：求垂足Q坐标，再计算PQ长", font=FONT_CN, font_size=19, color=GRAY_A).move_to(DOWN * 5.2)
        self.play(FadeIn(derive_cn), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(sec_title), FadeOut(perp_label_cn), FadeOut(d_label), FadeOut(derive_cn), run_time=0.4)

        # Store
        self._perp     = perp
        self._q_dot    = q_dot
        self._q_label  = q_label
        self._right_mark = right_mark

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 4 – Formula Reveal  (~8 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene4_formula(self):
        sec_title = Text("距离公式", font=FONT_CN, font_size=36, color=GOLD).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        # Big formula
        formula = MathTex(
            r"d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
            font_size=42, color=WHITE
        ).move_to(DOWN * 2.8)
        self.play(Write(formula), run_time=1.2)
        self.wait(0.8)

        # Surround formula with box
        box = SurroundingRectangle(formula, color=GOLD, buff=0.25)
        self.play(Create(box), run_time=0.6)
        self.wait(0.5)

        # Highlight numerator
        num_hl = Text("分子：将 P 坐标代入直线方程，取绝对值",
                      font=FONT_CN, font_size=18, color=C_FORMULA_HL).move_to(DOWN * 4.5)
        num_brace = Brace(formula[0][2:14], UP, color=C_FORMULA_HL, buff=0.05)
        self.play(FadeIn(num_brace), FadeIn(num_hl), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(num_brace), FadeOut(num_hl), run_time=0.3)

        # Highlight denominator
        den_hl = Text("分母：法向量 (A, B) 的模长",
                      font=FONT_CN, font_size=18, color=C_FOOT).move_to(DOWN * 4.5)
        den_brace = Brace(formula[0][15:], DOWN, color=C_FOOT, buff=0.05)
        self.play(FadeIn(den_brace), FadeIn(den_hl), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(den_brace), FadeOut(den_hl), run_time=0.3)

        # Flash the whole formula once more
        self.play(Flash(formula, color=YELLOW, flash_radius=1.2), run_time=0.6)
        self.wait(0.5)

        self.play(FadeOut(sec_title), run_time=0.4)

        # Keep formula and box for next scene
        self._formula = formula
        self._formula_box = box

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 5 – Numeric Calculation  (~8 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene5_calculation(self):
        axes = self._axes

        sec_title = Text("代入计算", font=FONT_CN, font_size=36, color=GOLD).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        # Slide formula up a little
        self.play(
            self._formula.animate.move_to(DOWN * 1.8).scale(0.85),
            FadeOut(self._formula_box),
            run_time=0.5
        )

        # Given values text
        given = Text("A=3, B=4, C=-12, x₀=1, y₀=1",
                     font=FONT_CN, font_size=20, color=GRAY_A).move_to(DOWN * 2.8)
        self.play(FadeIn(given), run_time=0.5)

        # Step-by-step substitution
        step1 = MathTex(r"d = \frac{|3\times1 + 4\times1 - 12|}{\sqrt{3^2 + 4^2}}",
                        font_size=34, color=WHITE).move_to(DOWN * 3.8)
        self.play(Write(step1), run_time=0.9)
        self.wait(0.4)

        step2 = MathTex(r"= \frac{|3 + 4 - 12|}{\sqrt{9 + 16}}",
                        font_size=34, color=WHITE).next_to(step1, DOWN, buff=0.25)
        self.play(Write(step2), run_time=0.7)
        self.wait(0.3)

        step3 = MathTex(r"= \frac{|-5|}{\sqrt{25}} = \frac{5}{5}",
                        font_size=34, color=WHITE).next_to(step2, DOWN, buff=0.25)
        self.play(Write(step3), run_time=0.7)
        self.wait(0.3)

        result = MathTex(r"d = 1", font_size=48, color=C_FORMULA_HL).next_to(step3, DOWN, buff=0.35)
        self.play(Write(result), run_time=0.6)
        self.play(Flash(result, color=YELLOW, flash_radius=0.7), run_time=0.5)
        self.wait(0.8)

        # Show d=1 on the diagram
        p_screen = axes.c2p(self.Px, self.Py)
        q_screen = axes.c2p(self.Qx, self.Qy)
        mid_pq   = (p_screen + q_screen) / 2
        d_mark   = MathTex(r"d=1", font_size=20, color=C_FORMULA_HL).next_to(mid_pq + RIGHT*0.05, RIGHT, buff=0.1)
        self.play(FadeIn(d_mark), run_time=0.4)
        self.wait(1.2)

        # Clean up for parallel scene
        self.play(
            FadeOut(sec_title), FadeOut(given), FadeOut(step1),
            FadeOut(step2), FadeOut(step3), FadeOut(result), FadeOut(d_mark),
            FadeOut(self._formula),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 6 – Parallel Lines Distance  (~8 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene6_parallel(self):
        axes = self._axes

        # Fade out the current geometry overlay
        self.play(
            FadeOut(self._perp), FadeOut(self._q_dot), FadeOut(self._q_label),
            FadeOut(self._right_mark), FadeOut(self._p_dot), FadeOut(self._p_label),
            FadeOut(self._p_gen_cn), FadeOut(self._p_gen_eq),
            run_time=0.5
        )

        sec_title = Text("平行线之间的距离", font=FONT_CN, font_size=32, color=GOLD).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        # Draw second parallel line l₂
        line_l2 = self.line_l2_on_axes(axes, color=C_LINE2)
        self.play(Create(line_l2), run_time=0.8)

        # Labels
        lbl1_cn = Text("l₁:", font=FONT_CN, font_size=22, color=C_LINE1).move_to(UP * 4.8 + LEFT * 2.8)
        lbl1_eq = MathTex(r"3x+4y-12=0", font_size=22, color=C_LINE1).next_to(lbl1_cn, RIGHT, buff=0.1)

        lbl2_cn = Text("l₂:", font=FONT_CN, font_size=22, color=C_LINE2).move_to(UP * 4.2 + LEFT * 2.8)
        lbl2_eq = MathTex(r"3x+4y-2=0", font_size=22, color=C_LINE2).next_to(lbl2_cn, RIGHT, buff=0.1)

        self.play(
            FadeOut(self._line_label_cn), FadeOut(self._line_label_eq),
            FadeOut(self._gen_cn), FadeOut(self._gen_eq),
            run_time=0.3
        )
        self.play(FadeIn(lbl1_cn), Write(lbl1_eq), FadeIn(lbl2_cn), Write(lbl2_eq), run_time=0.7)

        # Draw a perpendicular connector between the two lines at x=2
        x_conn = 2.0
        y1_conn = (12 - 3 * x_conn) / 4   # on l₁: y=1.5
        y2_conn = (2  - 3 * x_conn) / 4   # on l₂: y=-1.0
        # The perpendicular between two parallel lines is along the normal direction (3,4)
        # Pick a point on l₂: (0, 0.5)  → connector perp to lines
        x_base = 0.8
        y_l2_base = (2 - 3 * x_base) / 4             # ≈ -0.1  → but clamp to visible
        # Better: use normal direction to find connector
        # Normal unit vector: (3,4)/5
        # Point on l₂ with x=1: y=(2-3)/4 = -0.25 → too low
        # Let's connect from x=0.3 on l2 to corresponding point on l1
        x_start = 0.3
        y_l2_s  = (2  - 3 * x_start) / 4     # ≈ 0.275
        # Walk along normal (3,4)/5 by distance d_parallel=2
        x_end   = x_start + 3/5 * self.d_parallel
        y_end   = y_l2_s  + 4/5 * self.d_parallel
        # that lands on: y_end = 0.275 + 1.6 = 1.875, x_end = 0.3 + 1.2 = 1.5
        # check: 3*1.5 + 4*1.875 - 12 = 4.5 + 7.5 - 12 = 0 ✓

        ps_l2 = axes.c2p(x_start, y_l2_s)
        ps_l1 = axes.c2p(x_end,   y_end)
        conn_line = DashedLine(ps_l2, ps_l1, color=C_PERP, dash_length=0.08, stroke_width=2.5)
        self.play(Create(conn_line), run_time=0.7)

        # Right angle marks at both ends
        v_normal   = ps_l1 - ps_l2
        v_line_dir = axes.c2p(x_start + 0.4 * self.B_c, y_l2_s + 0.4 * (-self.A_c)) - ps_l2
        ra1 = self.right_angle_mark(ps_l2, ps_l2 + v_normal, ps_l2 + v_line_dir, size=0.15)
        self.play(Create(ra1), run_time=0.4)

        # Distance brace label
        mid_conn = (ps_l2 + ps_l1) / 2
        d2_label = MathTex(r"d", font_size=24, color=C_FORMULA_HL).next_to(mid_conn, LEFT, buff=0.18)
        self.play(FadeIn(d2_label), run_time=0.4)

        # Parallel-line formula
        par_formula_cn = Text("平行线距离公式:", font=FONT_CN, font_size=24, color=WHITE).move_to(DOWN * 2.8)
        par_formula_eq = MathTex(
            r"d = \frac{|C_1 - C_2|}{\sqrt{A^2 + B^2}}",
            font_size=38, color=WHITE
        ).move_to(DOWN * 3.7)
        box2 = SurroundingRectangle(par_formula_eq, color=C_LINE2, buff=0.2)
        self.play(FadeIn(par_formula_cn), Write(par_formula_eq), run_time=0.9)
        self.play(Create(box2), run_time=0.5)
        self.wait(0.6)

        # Substitute
        sub_eq = MathTex(
            r"d = \frac{|-12-(-2)|}{\sqrt{9+16}} = \frac{10}{5} = 2",
            font_size=30, color=C_FORMULA_HL
        ).move_to(DOWN * 5.2)
        self.play(Write(sub_eq), run_time=0.9)
        self.wait(1.2)

        # Show d=2 on diagram
        d2_val = MathTex(r"d=2", font_size=20, color=C_FORMULA_HL).next_to(mid_conn + RIGHT*0.05, RIGHT, buff=0.1)
        self.play(FadeOut(d2_label), FadeIn(d2_val), run_time=0.4)
        self.wait(0.8)

        # Cleanup
        self.play(
            FadeOut(sec_title), FadeOut(lbl1_cn), FadeOut(lbl1_eq),
            FadeOut(lbl2_cn), FadeOut(lbl2_eq),
            FadeOut(conn_line), FadeOut(ra1), FadeOut(d2_val),
            FadeOut(par_formula_cn), FadeOut(par_formula_eq), FadeOut(box2),
            FadeOut(sub_eq), FadeOut(line_l2), FadeOut(self._line_l),
            FadeOut(self._axes_group),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 7 – Summary + Outro  (~5 s)
    # ═══════════════════════════════════════════════════════════════════════
    def scene7_outro(self):
        # Summary card
        summary_title = Text("知识点总结", font=FONT_CN, font_size=36, color=GOLD).move_to(UP * 4)
        self.play(Write(summary_title), run_time=0.6)

        f1 = MathTex(
            r"d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}",
            font_size=38, color=WHITE
        ).move_to(UP * 2.5)
        label_f1 = Text("点到直线距离公式", font=FONT_CN, font_size=20, color=GRAY_A).next_to(f1, DOWN, buff=0.2)

        f2 = MathTex(
            r"d = \frac{|C_1 - C_2|}{\sqrt{A^2 + B^2}}",
            font_size=38, color=C_LINE2
        ).move_to(UP * 0.6)
        label_f2 = Text("平行线距离公式", font=FONT_CN, font_size=20, color=GRAY_A).next_to(f2, DOWN, buff=0.2)

        box1 = SurroundingRectangle(f1, color=GOLD, buff=0.2)
        box2 = SurroundingRectangle(f2, color=C_LINE2, buff=0.2)

        self.play(Write(f1), Create(box1), run_time=0.8)
        self.play(FadeIn(label_f1), run_time=0.4)
        self.play(Write(f2), Create(box2), run_time=0.8)
        self.play(FadeIn(label_f2), run_time=0.4)
        self.wait(1.0)

        # Outro branding
        self.play(
            FadeOut(summary_title), FadeOut(f1), FadeOut(box1), FadeOut(label_f1),
            FadeOut(f2), FadeOut(box2), FadeOut(label_f2),
            run_time=0.5
        )

        author_big = Text("上海初高中数学直通车", font=FONT_CN, font_size=40, color=WHITE).move_to(UP * 1.5)
        author_id  = Text("@emptyandcalm", font=FONT_CN, font_size=30, color=GRAY_B).move_to(UP * 0.5)

        self.play(Transform(self._badge, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text("关注我，获得更多高中数学技巧！", font=FONT_CN, font_size=26, color=C_FORMULA_HL).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # Decorative dots
        dots = VGroup(*[
            Dot(2.2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]),
                radius=0.08, color=GOLD, fill_opacity=0.9)
            for i in range(6)
        ]).move_to(DOWN * 2.0)
        self.play(*[FadeIn(d, scale=0.3) for d in dots], run_time=0.6)
        self.play(Rotate(dots, angle=TAU, run_time=1.5))
        self.wait(0.8)

        self.play(FadeOut(self._badge), FadeOut(author_id), FadeOut(follow), FadeOut(dots), run_time=1.0)


# ─── Run ────────────────────────────────────────────────────────────────────
# manim -pql point_to_line_distance.py PointToLineDistance   # preview
# manim -qh  point_to_line_distance.py PointToLineDistance   # final
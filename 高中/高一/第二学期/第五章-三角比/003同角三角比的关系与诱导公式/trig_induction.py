"""
同角三角比关系与诱导公式 - Manim 教学动画
高一数学 · 第五章 · 三角比

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─── Global Config: TikTok Vertical ───────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─── Color Palette ─────────────────────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
C_SIN           = "#e74c3c"   # red
C_COS           = "#3498db"   # blue
C_TAN           = "#f39c12"   # orange
C_CIRCLE        = "#2ecc71"   # green
C_HIGHLIGHT     = "#f1c40f"   # yellow
C_AXIS          = "#95a5a6"   # gray
C_FORMULA_BOX   = "#16213e"
C_TEXT          = "#ecf0f1"
C_MNEMONIC      = "#9b59b6"   # purple


class TrigInduction(Scene):
    """
    Scene order:
      0. setup_geometry
      1. Opening hook
      2. Unit circle & definitions
      3. sin² + cos² = 1  (visual proof)
      4. tan α = sin/cos
      5. Induction formulas intro + mnemonic
      6. Induction: π - α
      7. Induction: π/2 - α
      8. Induction: -α
      9. Summary table
     10. Outro
    """

    # ── Setup ────────────────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_01_opening()
        self.scene_02_unit_circle()
        self.scene_03_pythagorean_identity()
        self.scene_04_tan_identity()
        self.scene_05_induction_intro()
        self.scene_06_induction_pi_minus()
        self.scene_07_induction_halfpi_minus()
        self.scene_08_induction_negative()
        self.scene_09_summary()
        self.scene_10_outro()

    def setup_geometry(self):
        """Pre-compute all geometric data (no guessing)."""
        # Unit circle parameters
        self.RADIUS     = 2.2          # visual radius in logical units
        self.CENTER     = np.array([0.0, 1.5, 0])   # circle center (world coords)
        self.DEMO_ALPHA = np.pi / 3    # 60° – the demonstration angle

        # Point P on unit circle for demo angle
        self.P = self.circle_point(self.DEMO_ALPHA)

        # Foot of perpendicular from P to x-axis (cos-axis)
        self.FOOT_X = np.array([self.P[0], self.CENTER[1], 0])   # same y as center

        # Verify P is on the circle
        dist = np.linalg.norm(self.P - self.CENTER)
        assert abs(dist - self.RADIUS) < 1e-10, "P not on circle!"

        # Quadrant label positions (avoid overlap)
        r = self.RADIUS * 0.55
        self.Q_LABELS = {
            "I":   self.CENTER + np.array([ r,  r*0.8, 0]),
            "II":  self.CENTER + np.array([-r,  r*0.8, 0]),
            "III": self.CENTER + np.array([-r, -r*0.8, 0]),
            "IV":  self.CENTER + np.array([ r, -r*0.8, 0]),
        }

    def circle_point(self, alpha):
        """Return world-coord point on unit circle at angle alpha."""
        return self.CENTER + np.array([
            self.RADIUS * np.cos(alpha),
            self.RADIUS * np.sin(alpha),
            0
        ])

    # ── Helpers ──────────────────────────────────────────────────────────────
    def make_author(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=19,
            color=GRAY_B,
        ).move_to(UP * 7.1)

    def make_title_bar(self, zh_text, color=C_HIGHLIGHT):
        return Text(
            zh_text,
            font="Noto Sans CJK SC",
            font_size=34,
            color=color,
            weight=BOLD,
        ).move_to(UP * 5.6)

    def make_unit_circle(self):
        circle = Circle(radius=self.RADIUS, color=C_CIRCLE, stroke_width=2.5)
        circle.move_to(self.CENTER)
        return circle

    def make_axes(self):
        """Create x/y axes centered at self.CENTER."""
        x_axis = Arrow(
            self.CENTER + LEFT  * (self.RADIUS + 0.4),
            self.CENTER + RIGHT * (self.RADIUS + 0.4),
            buff=0, color=C_AXIS, stroke_width=2, tip_length=0.18
        )
        y_axis = Arrow(
            self.CENTER + DOWN * (self.RADIUS + 0.4),
            self.CENTER + UP   * (self.RADIUS + 0.4),
            buff=0, color=C_AXIS, stroke_width=2, tip_length=0.18
        )
        x_lbl = MathTex("x", font_size=22, color=C_AXIS).next_to(x_axis, RIGHT, buff=0.08)
        y_lbl = MathTex("y", font_size=22, color=C_AXIS).next_to(y_axis, UP,    buff=0.08)
        o_lbl = MathTex("O", font_size=22, color=C_AXIS).move_to(
            self.CENTER + LEFT*0.22 + DOWN*0.22
        )
        return VGroup(x_axis, y_axis, x_lbl, y_lbl, o_lbl)

    def make_formula_box(self, formula_str, color=WHITE, font_size=28):
        box_bg = RoundedRectangle(
            width=7.8, height=1.05,
            corner_radius=0.18,
            fill_color=C_FORMULA_BOX,
            fill_opacity=0.92,
            stroke_color=color,
            stroke_width=1.5,
        )
        tex = MathTex(formula_str, font_size=font_size, color=color)
        tex.move_to(box_bg.get_center())
        return VGroup(box_bg, tex)

    def fade_clear(self, *mobjects, run_time=0.45):
        self.play(*[FadeOut(m) for m in mobjects], run_time=run_time)

    # ── Scene 01 : Opening Hook ───────────────────────────────────────────────
    def scene_01_opening(self):
        author = self.make_author()
        self.play(FadeIn(author, shift=DOWN*0.15), run_time=0.35)

        hook = Text(
            "sin²α + cos²α = ?",
            font="Noto Sans CJK SC",
            font_size=52,
            color=C_HIGHLIGHT,
        ).move_to(UP * 3.8)

        sub = Text(
            "三角比的秘密，一分钟搞懂！",
            font="Noto Sans CJK SC",
            font_size=27,
            color=C_TEXT,
        ).move_to(UP * 2.8)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP*0.25), run_time=0.5)

        # Draw a quick unit circle teaser
        circ_teaser = Circle(radius=1.6, color=C_CIRCLE, stroke_width=2.5).move_to(DOWN*0.5)
        dot_teaser  = Dot(DOWN*0.5 + RIGHT*1.6, radius=0.1, color=C_HIGHLIGHT)
        self.play(Create(circ_teaser), run_time=0.9)
        self.play(FadeIn(dot_teaser, scale=0.3), run_time=0.3)
        self.wait(0.5)

        self.fade_clear(hook, sub, circ_teaser, dot_teaser, run_time=0.5)
        self.author = author   # keep for rest of video

    # ── Scene 02 : Unit Circle & Definitions ─────────────────────────────────
    def scene_02_unit_circle(self):
        title = self.make_title_bar("单位圆与三角函数")
        self.play(Write(title), run_time=0.65)

        axes  = self.make_axes()
        circ  = self.make_unit_circle()
        self.play(Create(axes), run_time=0.7)
        self.play(Create(circ), run_time=1.1)

        # Origin dot
        o_dot = Dot(self.CENTER, radius=0.07, color=C_AXIS)
        self.play(FadeIn(o_dot), run_time=0.25)

        # Rotating radius line + point P
        radius_line = Line(self.CENTER, self.P, color=C_HIGHLIGHT, stroke_width=2.5)
        p_dot = Dot(self.P, radius=0.1, color=C_HIGHLIGHT)
        p_lbl = MathTex(r"P", font_size=22, color=C_HIGHLIGHT).next_to(p_dot, UR, buff=0.08)

        self.play(Create(radius_line), FadeIn(p_dot), run_time=0.7)
        self.play(Write(p_lbl), run_time=0.3)

        # Angle arc
        angle_line_ref = Line(self.CENTER, self.CENTER + RIGHT * self.RADIUS)
        angle_arc = Arc(
            radius=0.45,
            start_angle=0,
            angle=self.DEMO_ALPHA,
            arc_center=self.CENTER,
            color=C_HIGHLIGHT,
            stroke_width=2,
        )
        alpha_lbl = MathTex(r"\alpha", font_size=24, color=C_HIGHLIGHT).move_to(
            self.CENTER + np.array([0.65, 0.25, 0])
        )
        self.play(Create(angle_arc), Write(alpha_lbl), run_time=0.6)

        # Drop perpendicular lines → show sin and cos
        foot_on_x = self.FOOT_X
        sin_line  = DashedLine(self.P, foot_on_x, color=C_SIN, dash_length=0.09, stroke_width=2.2)
        cos_line  = DashedLine(self.CENTER, foot_on_x, color=C_COS, dash_length=0.09, stroke_width=2.2)

        sin_brace_dir = RIGHT * 0.35
        cos_brace_dir = DOWN  * 0.28

        sin_lbl = MathTex(r"\sin\alpha", font_size=22, color=C_SIN).next_to(sin_line, RIGHT, buff=0.1)
        cos_lbl = MathTex(r"\cos\alpha", font_size=22, color=C_COS).next_to(
            cos_line, DOWN, buff=0.12
        )

        self.play(Create(sin_line), run_time=0.6)
        self.play(Write(sin_lbl), run_time=0.4)
        self.play(Create(cos_line), run_time=0.6)
        self.play(Write(cos_lbl), run_time=0.4)
        self.wait(0.5)

        # Definition text
        def_text = VGroup(
            Text("P 点的纵坐标 = sin α", font="Noto Sans CJK SC",
                 font_size=22, color=C_SIN),
            Text("P 点的横坐标 = cos α", font="Noto Sans CJK SC",
                 font_size=22, color=C_COS),
        ).arrange(DOWN, buff=0.28).move_to(DOWN * 4.2)
        self.play(FadeIn(def_text, shift=UP*0.2), run_time=0.65)
        self.wait(1.2)

        self.fade_clear(title, def_text, run_time=0.4)

        # Store persistent elements
        self.circle_group = VGroup(axes, circ, o_dot)
        self.radius_group = VGroup(radius_line, p_dot, p_lbl)
        self.angle_group  = VGroup(angle_arc, alpha_lbl)
        self.sin_group    = VGroup(sin_line, sin_lbl)
        self.cos_group    = VGroup(cos_line, cos_lbl)
        self.foot_dot     = Dot(foot_on_x, radius=0.06, color=GRAY)
        self.play(FadeIn(self.foot_dot), run_time=0.2)

    # ── Scene 03 : Pythagorean Identity ──────────────────────────────────────
    def scene_03_pythagorean_identity(self):
        title = self.make_title_bar("勾股定理 → 恒等式", color=C_SIN)
        self.play(Write(title), run_time=0.6)

        # Highlight the right triangle
        OP  = self.P
        OFoot = self.FOOT_X
        tri = Polygon(
            self.CENTER, OFoot, OP,
            stroke_color=GRAY, stroke_width=1.5,
            fill_color=YELLOW_A, fill_opacity=0.12,
        )
        self.play(Create(tri), run_time=0.6)

        # Show right angle mark at foot
        v1 = self.CENTER - OFoot
        v2 = OP - OFoot
        v1u = v1 / np.linalg.norm(v1) * 0.17
        v2u = v2 / np.linalg.norm(v2) * 0.17
        sq = Polygon(
            OFoot, OFoot + v1u, OFoot + v1u + v2u, OFoot + v2u,
            stroke_color=YELLOW, stroke_width=1.5, fill_opacity=0
        )
        self.play(Create(sq), run_time=0.3)

        # Hypotenuse label = 1
        mid_OP = (self.CENTER + OP) / 2 + np.array([-0.25, 0.1, 0])
        r1_lbl = MathTex("1", font_size=22, color=C_HIGHLIGHT).move_to(mid_OP)
        self.play(Write(r1_lbl), run_time=0.3)

        # Derive identity step by step
        step_bg = RoundedRectangle(
            width=7.6, height=3.5,
            corner_radius=0.2,
            fill_color=C_FORMULA_BOX,
            fill_opacity=0.95,
            stroke_color=C_SIN,
            stroke_width=1.5,
        ).move_to(DOWN * 4.85)

        step_title = Text(
            "用勾股定理推导：",
            font="Noto Sans CJK SC",
            font_size=22, color=C_TEXT
        ).move_to(step_bg.get_top() + DOWN * 0.38)

        step1 = MathTex(
            r"\cos^2\alpha + \sin^2\alpha = 1^2",
            font_size=26, color=C_TEXT
        ).move_to(step_bg.get_center() + UP * 0.45)

        arrow_down = MathTex(r"\Downarrow", font_size=26, color=C_HIGHLIGHT).move_to(
            step_bg.get_center() + UP * 0.0
        )

        step2 = MathTex(
            r"\sin^2\alpha + \cos^2\alpha = 1",
            font_size=30, color=C_HIGHLIGHT,
        ).move_to(step_bg.get_center() + DOWN * 0.52)

        self.play(FadeIn(step_bg), run_time=0.3)
        self.play(Write(step_title), run_time=0.4)
        self.play(Write(step1), run_time=0.7)
        self.play(Write(arrow_down), run_time=0.3)
        self.play(Write(step2), run_time=0.8)
        self.wait(2.2)

        self.fade_clear(
            title, tri, sq, r1_lbl, step_bg, step_title, step1, arrow_down,
            run_time=0.4
        )

        # Flash the final identity and keep it visible
        self.identity1 = step2
        self.play(
            self.identity1.animate.move_to(DOWN * 3.5).set_font_size(28),
            run_time=0.6
        )
        flash_box = SurroundingRectangle(self.identity1, color=C_SIN, buff=0.15, corner_radius=0.1)
        self.play(Create(flash_box), run_time=0.35)
        self.wait(0.5)
        self.identity1_box = flash_box

    # ── Scene 04 : tan Identity ───────────────────────────────────────────────
    def scene_04_tan_identity(self):
        title = self.make_title_bar("tan α 的定义", color=C_TAN)
        self.play(Write(title), run_time=0.55)

        # Draw tangent line – vertical line at x = R (right of circle)
        tan_x_world = self.CENTER[0] + self.RADIUS  # rightmost point
        tan_foot     = np.array([tan_x_world, self.CENTER[1], 0])

        # Extend radius line to meet tangent
        # slope of OP: sin/cos
        alpha = self.DEMO_ALPHA
        slope = np.tan(alpha)
        tan_y_intercept_world = self.CENTER[1] + slope * (tan_x_world - self.CENTER[0])
        tan_top = np.array([tan_x_world, tan_y_intercept_world, 0])

        tan_line_vis = Line(tan_foot, tan_top, color=C_TAN, stroke_width=2.5)

        # Extended radius
        ext_radius = Line(self.CENTER, tan_top, color=C_HIGHLIGHT, stroke_width=1.8)

        self.play(Create(ext_radius), run_time=0.5)
        self.play(Create(tan_line_vis), run_time=0.5)

        tan_seg_lbl = MathTex(r"\tan\alpha", font_size=22, color=C_TAN).next_to(
            tan_line_vis, RIGHT, buff=0.1
        )
        self.play(Write(tan_seg_lbl), run_time=0.4)

        # Show formula
        formula_box = self.make_formula_box(
            r"\tan\alpha = \frac{\sin\alpha}{\cos\alpha}", color=C_TAN, font_size=30
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(formula_box), run_time=0.5)
        self.wait(1.5)

        # Second identity
        id2_box = self.make_formula_box(
            r"1 + \tan^2\alpha = \sec^2\alpha", color=C_TAN, font_size=26
        ).move_to(DOWN * 5.55)
        self.play(FadeIn(id2_box), run_time=0.5)
        self.wait(1.2)

        self.fade_clear(
            title, ext_radius, tan_line_vis, tan_seg_lbl, formula_box, id2_box,
            run_time=0.45
        )

    # ── Scene 05 : Induction Intro + Mnemonic ────────────────────────────────
    def scene_05_induction_intro(self):
        title = self.make_title_bar("诱导公式", color=C_MNEMONIC)
        self.play(Write(title), run_time=0.55)

        intro = Text(
            "把任意角的三角函数\n化为锐角的三角函数",
            font="Noto Sans CJK SC",
            font_size=26,
            color=C_TEXT,
        ).move_to(UP * 4.3)
        self.play(FadeIn(intro, shift=UP*0.2), run_time=0.6)

        # Mnemonic box
        mnem_bg = RoundedRectangle(
            width=7.5, height=2.6,
            corner_radius=0.22,
            fill_color="#2c0d45",
            fill_opacity=0.97,
            stroke_color=C_MNEMONIC,
            stroke_width=2,
        ).move_to(UP * 2.2)

        mnem_title = Text(
            "口诀：",
            font="Noto Sans CJK SC",
            font_size=25, color=C_MNEMONIC, weight=BOLD,
        ).move_to(mnem_bg.get_top() + DOWN * 0.42)

        mnem_line1 = Text(
            "奇变偶不变",
            font="Noto Sans CJK SC",
            font_size=34, color=C_HIGHLIGHT, weight=BOLD,
        ).move_to(mnem_bg.get_center() + UP * 0.3)

        mnem_line2 = Text(
            "符号看象限",
            font="Noto Sans CJK SC",
            font_size=34, color=C_HIGHLIGHT, weight=BOLD,
        ).move_to(mnem_bg.get_center() + DOWN * 0.42)

        self.play(FadeIn(mnem_bg), run_time=0.3)
        self.play(Write(mnem_title), run_time=0.35)
        self.play(Write(mnem_line1), run_time=0.7)
        self.play(Write(mnem_line2), run_time=0.7)
        self.wait(0.5)

        # Explain mnemonic
        exp1 = Text(
            "π/2 的奇数倍 → sin ↔ cos 互换",
            font="Noto Sans CJK SC",
            font_size=21, color=C_TEXT,
        ).move_to(UP * 0.55)
        exp2 = Text(
            "π/2 的偶数倍 → 函数名不变",
            font="Noto Sans CJK SC",
            font_size=21, color=C_TEXT,
        ).move_to(UP * 0.0)
        exp3 = Text(
            "符号由原角所在象限决定",
            font="Noto Sans CJK SC",
            font_size=21, color=C_TEXT,
        ).move_to(DOWN * 0.55)

        for exp in [exp1, exp2, exp3]:
            self.play(FadeIn(exp, shift=RIGHT * 0.2), run_time=0.45)

        self.wait(1.4)
        self.fade_clear(title, intro, mnem_bg, mnem_title, mnem_line1, mnem_line2,
                        exp1, exp2, exp3, run_time=0.4)

    # ── Scene 06 : Induction  π ± α ──────────────────────────────────────────
    def scene_06_induction_pi_minus(self):
        title = self.make_title_bar("诱导公式：π - α", color=C_SIN)
        self.play(Write(title), run_time=0.55)

        # Show α and π-α on unit circle
        alpha     = self.DEMO_ALPHA          # 60°
        pi_minus  = np.pi - alpha            # 120°

        P1 = self.circle_point(alpha)
        P2 = self.circle_point(pi_minus)

        # Keep existing circle; draw two radius lines
        rad1 = Line(self.CENTER, P1, color=C_COS, stroke_width=2.5)
        rad2 = Line(self.CENTER, P2, color=C_SIN, stroke_width=2.5)

        d1 = Dot(P1, radius=0.1, color=C_COS)
        d2 = Dot(P2, radius=0.1, color=C_SIN)

        lbl1 = MathTex(r"\alpha", font_size=22, color=C_COS).next_to(d1, UR, buff=0.08)
        lbl2 = MathTex(r"\pi-\alpha", font_size=22, color=C_SIN).next_to(d2, UL, buff=0.08)

        arc1 = Arc(radius=0.5, start_angle=0, angle=alpha,
                   arc_center=self.CENTER, color=C_COS, stroke_width=1.8)
        arc2 = Arc(radius=0.65, start_angle=0, angle=pi_minus,
                   arc_center=self.CENTER, color=C_SIN, stroke_width=1.8)

        self.play(Create(rad1), FadeIn(d1), Create(arc1), run_time=0.65)
        self.play(Write(lbl1), run_time=0.3)
        self.play(Create(rad2), FadeIn(d2), Create(arc2), run_time=0.65)
        self.play(Write(lbl2), run_time=0.3)

        # y-coord equal, x-coord opposite → show dashed helpers
        foot1 = np.array([P1[0], self.CENTER[1], 0])
        foot2 = np.array([P2[0], self.CENTER[1], 0])
        dashed1 = DashedLine(P1, foot1, color=C_COS,  dash_length=0.08, stroke_width=1.8)
        dashed2 = DashedLine(P2, foot2, color=C_SIN,  dash_length=0.08, stroke_width=1.8)
        self.play(Create(dashed1), Create(dashed2), run_time=0.5)

        # Mirror annotation
        mirror_line = DashedLine(
            self.CENTER + UP * (self.RADIUS + 0.1),
            self.CENTER + DOWN * (self.RADIUS + 0.1),
            color=GRAY, stroke_width=1.2, dash_length=0.1
        )
        mirror_txt = Text(
            "y轴对称",
            font="Noto Sans CJK SC", font_size=18, color=GRAY
        ).next_to(self.CENTER + UP * (self.RADIUS * 0.9), RIGHT, buff=0.08)
        self.play(Create(mirror_line), Write(mirror_txt), run_time=0.5)

        # Formula box
        formulas = VGroup(
            self.make_formula_box(r"\sin(\pi - \alpha) = \sin\alpha",  color=C_SIN, font_size=27),
            self.make_formula_box(r"\cos(\pi - \alpha) = -\cos\alpha", color=C_COS, font_size=27),
        ).arrange(DOWN, buff=0.22).move_to(DOWN * 4.6)

        self.play(FadeIn(formulas[0]), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(formulas[1]), run_time=0.5)
        self.wait(1.8)

        # π + α  (briefly)
        sub_title = Text("同理 π+α：", font="Noto Sans CJK SC",
                         font_size=23, color=C_TEXT).move_to(DOWN * 3.4)
        pi_plus_formulas = VGroup(
            MathTex(r"\sin(\pi+\alpha)=-\sin\alpha", font_size=24, color=C_SIN),
            MathTex(r"\cos(\pi+\alpha)=-\cos\alpha", font_size=24, color=C_COS),
        ).arrange(DOWN, buff=0.18).move_to(DOWN * 4.1)

        # Shift formulas up to make room
        self.play(
            formulas.animate.move_to(DOWN * 5.8).scale(0.85),
            run_time=0.4
        )
        self.play(FadeIn(sub_title), FadeIn(pi_plus_formulas), run_time=0.5)
        self.wait(1.2)

        self.fade_clear(
            title, rad1, rad2, d1, d2, lbl1, lbl2, arc1, arc2,
            dashed1, dashed2, mirror_line, mirror_txt,
            formulas, sub_title, pi_plus_formulas,
            run_time=0.45
        )

    # ── Scene 07 : Induction  π/2 - α ────────────────────────────────────────
    def scene_07_induction_halfpi_minus(self):
        title = self.make_title_bar("诱导公式：π/2 - α", color=C_COS)
        self.play(Write(title), run_time=0.55)

        alpha      = self.DEMO_ALPHA
        comp_alpha = np.pi / 2 - alpha   # complement = 30°

        P_orig = self.circle_point(alpha)
        P_comp = self.circle_point(comp_alpha)

        rad_orig = Line(self.CENTER, P_orig, color=C_SIN, stroke_width=2.5)
        rad_comp = Line(self.CENTER, P_comp, color=C_COS, stroke_width=2.5)
        d_orig = Dot(P_orig, radius=0.1, color=C_SIN)
        d_comp = Dot(P_comp, radius=0.1, color=C_COS)

        lbl_orig = MathTex(r"\alpha",           font_size=22, color=C_SIN).next_to(d_orig, UR, buff=0.08)
        lbl_comp = MathTex(r"\frac{\pi}{2}-\alpha", font_size=20, color=C_COS).next_to(d_comp, RIGHT, buff=0.08)

        arc_orig = Arc(radius=0.5,  start_angle=0, angle=alpha,
                       arc_center=self.CENTER, color=C_SIN, stroke_width=1.8)
        arc_comp = Arc(radius=0.65, start_angle=0, angle=comp_alpha,
                       arc_center=self.CENTER, color=C_COS, stroke_width=1.8)

        self.play(Create(rad_orig), FadeIn(d_orig), Create(arc_orig), run_time=0.6)
        self.play(Write(lbl_orig), run_time=0.3)
        self.play(Create(rad_comp), FadeIn(d_comp), Create(arc_comp), run_time=0.6)
        self.play(Write(lbl_comp), run_time=0.3)

        # Reflect over y=x line (diagonal)
        diag = DashedLine(
            self.CENTER + (LEFT + DOWN) * self.RADIUS * 0.85,
            self.CENTER + (RIGHT + UP) * self.RADIUS * 0.85,
            color=GRAY, stroke_width=1.2, dash_length=0.1
        )
        diag_lbl = Text("y=x 对称线", font="Noto Sans CJK SC",
                        font_size=17, color=GRAY).move_to(
            self.CENTER + RIGHT*1.4 + DOWN*1.2
        )
        self.play(Create(diag), Write(diag_lbl), run_time=0.5)

        # Observation text
        obs = Text(
            "奇数倍 π/2：sin ↔ cos 互换",
            font="Noto Sans CJK SC", font_size=22, color=C_HIGHLIGHT
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(obs, shift=UP*0.2), run_time=0.5)

        formulas = VGroup(
            self.make_formula_box(r"\sin\!\left(\frac{\pi}{2}-\alpha\right)=\cos\alpha",
                                  color=C_SIN, font_size=25),
            self.make_formula_box(r"\cos\!\left(\frac{\pi}{2}-\alpha\right)=\sin\alpha",
                                  color=C_COS, font_size=25),
        ).arrange(DOWN, buff=0.22).move_to(DOWN * 5.0)

        self.play(FadeIn(formulas[0]), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(formulas[1]), run_time=0.5)
        self.wait(1.8)

        self.fade_clear(
            title, rad_orig, rad_comp, d_orig, d_comp,
            lbl_orig, lbl_comp, arc_orig, arc_comp,
            diag, diag_lbl, obs, formulas,
            run_time=0.45
        )

    # ── Scene 08 : Induction  -α ──────────────────────────────────────────────
    def scene_08_induction_negative(self):
        title = self.make_title_bar("诱导公式：-α", color=C_TAN)
        self.play(Write(title), run_time=0.55)

        alpha     = self.DEMO_ALPHA
        neg_alpha = -alpha

        P_pos = self.circle_point(alpha)
        P_neg = self.circle_point(neg_alpha)

        rad_pos = Line(self.CENTER, P_pos, color=C_SIN, stroke_width=2.5)
        rad_neg = Line(self.CENTER, P_neg, color=C_TAN, stroke_width=2.5)
        d_pos = Dot(P_pos, radius=0.1, color=C_SIN)
        d_neg = Dot(P_neg, radius=0.1, color=C_TAN)

        lbl_pos = MathTex(r"\alpha",  font_size=22, color=C_SIN).next_to(d_pos, UR, buff=0.08)
        lbl_neg = MathTex(r"-\alpha", font_size=22, color=C_TAN).next_to(d_neg, DR, buff=0.08)

        arc_pos = Arc(radius=0.5, start_angle=0,      angle=alpha,  arc_center=self.CENTER,
                      color=C_SIN, stroke_width=1.8)
        arc_neg = Arc(radius=0.5, start_angle=0,      angle=-alpha, arc_center=self.CENTER,
                      color=C_TAN, stroke_width=1.8)   # negative angle → clockwise

        self.play(Create(rad_pos), FadeIn(d_pos), Create(arc_pos), run_time=0.6)
        self.play(Write(lbl_pos), run_time=0.3)
        self.play(Create(rad_neg), FadeIn(d_neg), Create(arc_neg), run_time=0.6)
        self.play(Write(lbl_neg), run_time=0.3)

        # Show x-axis symmetry
        mirror_x = DashedLine(
            self.CENTER + LEFT  * (self.RADIUS + 0.2),
            self.CENTER + RIGHT * (self.RADIUS + 0.2),
            color=GRAY, stroke_width=1.2, dash_length=0.1
        )
        mirror_txt = Text("x轴对称", font="Noto Sans CJK SC",
                          font_size=18, color=GRAY).next_to(mirror_x, RIGHT, buff=0.1)
        self.play(Create(mirror_x), Write(mirror_txt), run_time=0.5)

        formulas = VGroup(
            self.make_formula_box(r"\sin(-\alpha) = -\sin\alpha", color=C_SIN, font_size=27),
            self.make_formula_box(r"\cos(-\alpha) = \cos\alpha",  color=C_TAN, font_size=27),
        ).arrange(DOWN, buff=0.22).move_to(DOWN * 4.7)

        note = Text("sin 是奇函数，cos 是偶函数",
                    font="Noto Sans CJK SC", font_size=21, color=C_HIGHLIGHT
                    ).move_to(DOWN * 3.55)

        self.play(FadeIn(note, shift=UP*0.15), run_time=0.5)
        self.play(FadeIn(formulas[0]), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(formulas[1]), run_time=0.5)
        self.wait(1.8)

        self.fade_clear(
            title, rad_pos, rad_neg, d_pos, d_neg, lbl_pos, lbl_neg,
            arc_pos, arc_neg, mirror_x, mirror_txt, note, formulas,
            run_time=0.45
        )

    # ── Scene 09 : Summary Table ──────────────────────────────────────────────
    def scene_09_summary(self):
        # Fade out unit circle
        self.fade_clear(
            self.circle_group, self.radius_group, self.angle_group,
            self.sin_group, self.cos_group, self.foot_dot,
            self.identity1, self.identity1_box,
            run_time=0.5
        )

        title = self.make_title_bar("公式总结", color=C_HIGHLIGHT)
        self.play(Write(title), run_time=0.55)

        # ── Identity group ─────────────────────────────────────────────────
        id_title = Text("同角三角比关系：",
                        font="Noto Sans CJK SC", font_size=23, color=C_TEXT
                        ).move_to(UP * 4.6).align_to(LEFT * 3.5, LEFT)

        id_formulas = VGroup(
            MathTex(r"\sin^2\alpha + \cos^2\alpha = 1",
                    font_size=24, color=C_SIN),
            MathTex(r"\tan\alpha = \dfrac{\sin\alpha}{\cos\alpha}",
                    font_size=24, color=C_TAN),
        ).arrange(DOWN, buff=0.28).move_to(UP * 3.55)

        id_bg = SurroundingRectangle(id_formulas, color=C_SIN,
                                     buff=0.25, corner_radius=0.15)
        self.play(Write(id_title), run_time=0.4)
        self.play(Write(id_formulas[0]), run_time=0.5)
        self.play(Write(id_formulas[1]), run_time=0.5)
        self.play(Create(id_bg), run_time=0.3)

        # ── Induction formulas ─────────────────────────────────────────────
        ind_title = Text("诱导公式（偶数倍，函数名不变）：",
                         font="Noto Sans CJK SC", font_size=20, color=C_TEXT
                         ).move_to(UP * 2.2).align_to(LEFT * 3.5, LEFT)

        ind_items = VGroup(
            MathTex(r"\sin(\pi-\alpha)=\sin\alpha",          font_size=22, color=C_SIN),
            MathTex(r"\cos(\pi-\alpha)=-\cos\alpha",         font_size=22, color=C_COS),
            MathTex(r"\sin(\pi+\alpha)=-\sin\alpha",         font_size=22, color=C_SIN),
            MathTex(r"\cos(\pi+\alpha)=-\cos\alpha",         font_size=22, color=C_COS),
            MathTex(r"\sin(-\alpha)=-\sin\alpha",            font_size=22, color=C_SIN),
            MathTex(r"\cos(-\alpha)=\cos\alpha",             font_size=22, color=C_COS),
        ).arrange(DOWN, buff=0.22).move_to(UP * 0.2)

        ind_title2 = Text("诱导公式（奇数倍 π/2，函数名互换）：",
                          font="Noto Sans CJK SC", font_size=20, color=C_TEXT
                          ).move_to(DOWN * 2.15).align_to(LEFT * 3.5, LEFT)

        ind_items2 = VGroup(
            MathTex(r"\sin\!\left(\tfrac{\pi}{2}-\alpha\right)=\cos\alpha",
                    font_size=22, color=C_SIN),
            MathTex(r"\cos\!\left(\tfrac{\pi}{2}-\alpha\right)=\sin\alpha",
                    font_size=22, color=C_COS),
        ).arrange(DOWN, buff=0.22).move_to(DOWN * 3.0)

        self.play(Write(ind_title), run_time=0.4)
        for item in ind_items:
            self.play(FadeIn(item, shift=RIGHT*0.15), run_time=0.28)
        self.play(Write(ind_title2), run_time=0.4)
        for item in ind_items2:
            self.play(FadeIn(item, shift=RIGHT*0.15), run_time=0.3)

        # Mnemonic reminder
        mnem_reminder = Text("口诀：奇变偶不变，符号看象限",
                             font="Noto Sans CJK SC",
                             font_size=26, color=C_HIGHLIGHT, weight=BOLD
                             ).move_to(DOWN * 4.5)
        mnem_box = SurroundingRectangle(mnem_reminder, color=C_MNEMONIC,
                                        buff=0.18, corner_radius=0.12)
        self.play(FadeIn(mnem_reminder), Create(mnem_box), run_time=0.6)
        self.wait(3.0)

        self.fade_clear(
            title, id_title, id_formulas, id_bg,
            ind_title, ind_items, ind_title2, ind_items2,
            mnem_reminder, mnem_box,
            run_time=0.6
        )

    # ── Scene 10 : Outro ──────────────────────────────────────────────────────
    def scene_10_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=42, color=WHITE, weight=BOLD,
        ).move_to(UP * 1.8)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30, color=GRAY_B,
        ).move_to(UP * 0.85)

        follow_txt = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30, color=C_HIGHLIGHT,
        ).move_to(DOWN * 0.35)

        formula_deco = MathTex(
            r"\sin^2\alpha + \cos^2\alpha = 1",
            font_size=36, color=C_SIN
        ).move_to(DOWN * 1.6)

        self.play(
            FadeOut(self.author),
            FadeIn(author_big, shift=UP*0.2),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP*0.15), run_time=0.45)
        self.play(FadeIn(follow_txt, scale=1.06), run_time=0.55)
        self.play(Write(formula_deco), run_time=0.8)

        # Small circle decorations
        decorations = VGroup(*[
            Circle(radius=0.18, color=color, fill_opacity=0.75, stroke_width=0).move_to(
                DOWN * 3.3 + RIGHT * (i - 2) * 1.0
            )
            for i, color in enumerate([C_SIN, C_COS, C_TAN, C_CIRCLE, C_MNEMONIC])
        ])
        self.play(*[FadeIn(d, scale=0.4) for d in decorations], run_time=0.55)
        self.wait(1.5)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow_txt), FadeOut(formula_deco),
            FadeOut(decorations),
            run_time=0.9
        )
"""
两直线的垂直与夹角 - Manim 教学动画
高二数学 · 第十一章 · 坐标平面上的直线

# 快速预览（低画质）
manim -pql two_lines_angle.py TwoLinesAngle

# 高画质渲染
manim -qh two_lines_angle.py TwoLinesAngle

# 4K生产级
manim -qk two_lines_angle.py TwoLinesAngle

知识点：
  - 垂直条件：k₁·k₂ = -1
  - 一般式垂直：A₁A₂ + B₁B₂ = 0
  - 夹角公式：tan θ = |k₁-k₂|/(1+k₁k₂)

Format: TikTok 竖屏 1080×1920
Duration: ~41s
"""

from manim import *
import numpy as np

# ─── Config ────────────────────────────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─── Colors ────────────────────────────────────────────────────────────────────
BG_COLOR      = "#0f0c29"
LINE1_COLOR   = "#00d4ff"   # cyan  — l₁  k₁=2
LINE2_COLOR   = "#ff6b6b"   # red   — l₂  k₂=-0.5  (垂直)
LINE3_COLOR   = "#ffd93d"   # gold  — l₃  k₃=1/3   (夹角)
ANGLE_COLOR   = "#a8ff78"   # green — θ arc
FORMULA_BG    = "#16213e"
HIGHLIGHT_COL = "#ffe066"
AXIS_COL      = "#444466"


# ─── Helpers ───────────────────────────────────────────────────────────────────
def cn(text: str, size: int = 28, color=WHITE, **kw) -> Text:
    """Chinese text using correct font."""
    return Text(text, font="Noto Sans CJK SC", font_size=size, color=color, **kw)


def formula_box(
    label_text: str,
    formula_str: str,
    label_size: int = 22,
    formula_size: int = 26,
    box_color: str = "#00d4ff",
    width: float = 7.2,
) -> VGroup:
    """Rounded rectangle containing a Chinese label + MathTex formula."""
    lbl  = cn(label_text, size=label_size, color=box_color)
    fml  = MathTex(formula_str, font_size=formula_size, color=WHITE)
    content = VGroup(lbl, fml).arrange(DOWN, buff=0.15)
    box = RoundedRectangle(
        width=width, height=content.height + 0.5,
        corner_radius=0.15, color=box_color,
        fill_color=FORMULA_BG, fill_opacity=0.85,
        stroke_width=1.5,
    )
    return VGroup(box, content).arrange(IN, buff=0)  # overlay content on box


# ─── Scene ─────────────────────────────────────────────────────────────────────
class TwoLinesAngle(Scene):

    # ── geometry constants ─────────────────────────────────────────────────────
    K1 =  2.0        # slope of l₁ (persists through whole animation)
    K2 = -0.5        # slope of l₂  (⊥ to l₁,  k₁·k₂ = -1)
    K3 =  1.0 / 3.0  # slope of l₃  (forms 45° with l₁)

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.verify_geometry()
        self.scene_1_title()
        self.scene_2_perpendicular()
        self.scene_3_angle_formula()
        self.scene_4_summary()
        self.scene_5_outro()

    # ── geometry setup ─────────────────────────────────────────────────────────
    def setup_geometry(self):
        """Pre-calculate all geometry in AXES coordinates (not frame)."""
        # Axes will be placed at frame y=1.0 center
        self.axes_center_frame = UP * 1.0

        # Lines pass through origin (axes coords)
        self.P_int = np.array([0.0, 0.0, 0.0])  # intersection in axes coords

        # l₁: y = K1*x  →  endpoints at axes x = ±1.25 (y = ±2.5)
        self.l1_a = np.array([-1.25, -2.5, 0.0])
        self.l1_b = np.array([ 1.25,  2.5, 0.0])

        # l₂: y = K2*x  →  endpoints at axes x = ±3 (y = ∓1.5)
        self.l2_a = np.array([-3.0,  1.5, 0.0])
        self.l2_b = np.array([ 3.0, -1.5, 0.0])

        # l₃: y = K3*x  →  endpoints at axes x = ±3 (y = ±1)
        self.l3_a = np.array([-3.0, -1.0, 0.0])
        self.l3_b = np.array([ 3.0,  1.0, 0.0])

        # RightAngle arm endpoints (from intersection, in axes coords)
        self.arm1_tip = np.array([0.5,  1.0, 0.0])  # direction (1, K1)  = (1,2)
        self.arm2_tip = np.array([2.0, -1.0, 0.0])  # direction (2, K2*2)= (2,-1)

        # Angle arc reference points (in axes coords)
        # CCW arc from l₃ direction to l₁ direction spans 45°
        self.P_on_l3 = np.array([1.5, 0.5, 0.0])   # on l₃, arctan(1/3) ≈ 18.4°
        self.P_on_l1 = np.array([0.5, 1.0, 0.0])   # on l₁, arctan(2)   ≈ 63.4°

    def verify_geometry(self):
        """Numerical checks — runs during construct(), before any animation."""
        eps = 1e-9

        # 1) Perpendicular condition
        product = self.K1 * self.K2
        assert abs(product - (-1.0)) < eps, f"k1*k2 = {product}, expected -1"

        # 2) RightAngle arm vectors must be perpendicular
        v1 = self.arm1_tip - self.P_int
        v2 = self.arm2_tip - self.P_int
        dot = float(np.dot(v1[:2], v2[:2]))
        assert abs(dot) < eps, f"arm dot product = {dot}, expected 0"

        # 3) Angle formula: tan θ = 1  →  θ = 45°
        tan_theta = abs(self.K1 - self.K3) / (1 + self.K1 * self.K3)
        assert abs(tan_theta - 1.0) < eps, f"tan θ = {tan_theta}, expected 1"

        # 4) Angle arc cross product > 0 (CCW arc is the acute angle)
        v_l3 = self.P_on_l3 - self.P_int
        v_l1 = self.P_on_l1 - self.P_int
        cross_z = v_l3[0] * v_l1[1] - v_l3[1] * v_l1[0]
        assert cross_z > 0, f"cross_z = {cross_z}, must be > 0 for CCW arc"

        # 5) l₁ endpoints satisfy y = K1*x
        for pt in [self.l1_a, self.l1_b]:
            assert abs(pt[1] - self.K1 * pt[0]) < eps
        # l₂ endpoints
        for pt in [self.l2_a, self.l2_b]:
            assert abs(pt[1] - self.K2 * pt[0]) < eps
        # l₃ endpoints
        for pt in [self.l3_a, self.l3_b]:
            assert abs(pt[1] - self.K3 * pt[0]) < eps

        print("✅ All geometry checks passed")

    # ── scene helpers ──────────────────────────────────────────────────────────
    def _make_axes(self):
        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=6,
            y_length=5,
            axis_config=dict(
                color=AXIS_COL,
                stroke_width=1.5,
                include_tip=True,
                tip_length=0.15,
                include_ticks=True,
            ),
        )
        ax.move_to(self.axes_center_frame)
        return ax

    def _c2p(self, ax, pt_axes):
        """Convert axes-coordinate point to frame-coordinate point."""
        return ax.c2p(pt_axes[0], pt_axes[1])

    # ── Scene 1: Title ─────────────────────────────────────────────────────────
    def scene_1_title(self):
        # Author branding (persistent)
        self.author = cn(
            "上海初高中数学直通车 @emptyandcalm",
            size=18, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.5)

        # Main title
        title = cn("两直线的垂直与夹角", size=36, color=WHITE)
        title.move_to(UP * 5.5)
        subtitle = cn("高中数学 · 坐标几何", size=22, color=LIGHT_GRAY)
        subtitle.move_to(UP * 4.8)

        self.play(Write(title, run_time=1.0))
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)

        # Axes intro
        self.ax = self._make_axes()
        self.play(FadeIn(self.ax, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # Store for later cleanup
        self.title_group = VGroup(title, subtitle)

    # ── Scene 2: Perpendicular ─────────────────────────────────────────────────
    def scene_2_perpendicular(self):
        ax = self.ax

        # ── section label
        sec_label = cn("① 两直线垂直", size=28, color=LINE1_COLOR)
        sec_label.move_to(UP * 5.0)
        self.play(FadeOut(self.title_group, run_time=0.4),
                  Write(sec_label, run_time=0.6))

        # ── Draw l₁ (cyan, k=2)
        p_l1a = self._c2p(ax, self.l1_a)
        p_l1b = self._c2p(ax, self.l1_b)
        line_l1 = Line(p_l1a, p_l1b, color=LINE1_COLOR, stroke_width=3)
        lbl_l1 = MathTex(r"l_1", font_size=26, color=LINE1_COLOR)
        lbl_l1.next_to(p_l1b, UR, buff=0.1)

        self.play(Create(line_l1, run_time=0.9))
        self.play(FadeIn(lbl_l1), run_time=0.3)

        # ── Draw l₂ (red, k=-0.5)
        p_l2a = self._c2p(ax, self.l2_a)
        p_l2b = self._c2p(ax, self.l2_b)
        line_l2 = Line(p_l2a, p_l2b, color=LINE2_COLOR, stroke_width=3)
        lbl_l2 = MathTex(r"l_2", font_size=26, color=LINE2_COLOR)
        lbl_l2.next_to(p_l2b, DR, buff=0.1)

        self.play(Create(line_l2, run_time=0.9))
        self.play(FadeIn(lbl_l2), run_time=0.3)

        # ── RightAngle mark at intersection
        p_int_f  = self._c2p(ax, self.P_int)
        p_arm1_f = self._c2p(ax, self.arm1_tip)
        p_arm2_f = self._c2p(ax, self.arm2_tip)

        arm1 = Line(p_int_f, p_arm1_f, color=WHITE, stroke_width=0)  # invisible carrier
        arm2 = Line(p_int_f, p_arm2_f, color=WHITE, stroke_width=0)

        right_mark = RightAngle(arm1, arm2, length=0.28, color=WHITE, stroke_width=2.5)

        int_dot = Dot(p_int_f, color=YELLOW, radius=0.10)

        self.play(Create(right_mark, run_time=0.5),
                  FadeIn(int_dot), run_time=0.3)

        # ── Slope labels inside the axes area
        k1_lbl = MathTex(r"k_1=2", font_size=24, color=LINE1_COLOR)
        k1_lbl.move_to(self._c2p(ax, np.array([1.0, 2.3, 0])) + RIGHT * 0.5)

        k2_lbl = MathTex(r"k_2=-\frac{1}{2}", font_size=24, color=LINE2_COLOR)
        k2_lbl.move_to(self._c2p(ax, np.array([-2.0, 1.3, 0])) + LEFT * 0.3)

        self.play(FadeIn(k1_lbl), FadeIn(k2_lbl), run_time=0.5)
        self.wait(0.4)

        # ── Formula explanation (lower area)
        fx_line1 = VGroup(
            MathTex(r"k_1 \cdot k_2", font_size=30, color=WHITE),
            MathTex(r"= 2 \times \left(-\frac{1}{2}\right)", font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.15)
        fx_line1.move_to(DOWN * 2.4)

        self.play(Write(fx_line1, run_time=1.0))
        self.wait(0.3)

        fx_result = MathTex(r"= -1", font_size=36, color=HIGHLIGHT_COL)
        fx_result.next_to(fx_line1, DOWN, buff=0.25)
        self.play(Write(fx_result, run_time=0.7))

        # Flash the -1
        self.play(Indicate(fx_result, color=YELLOW, scale_factor=1.2), run_time=0.5)

        conclusion = MathTex(r"\therefore\ l_1 \perp l_2", font_size=32, color=ANGLE_COLOR)
        conclusion.next_to(fx_result, DOWN, buff=0.25)
        self.play(Write(conclusion, run_time=0.6))
        self.wait(0.5)

        # General form
        gen_lbl  = cn("一般式垂直条件", size=20, color=GRAY_A)
        gen_form = MathTex(r"A_1 A_2 + B_1 B_2 = 0", font_size=26, color=GRAY_A)
        gen_group = VGroup(gen_lbl, gen_form).arrange(RIGHT, buff=0.25)
        gen_box = SurroundingRectangle(gen_group, color=GRAY_C,
                                       buff=0.15, corner_radius=0.1, stroke_width=1)
        gen_all = VGroup(gen_box, gen_group).move_to(DOWN * 4.6)

        self.play(FadeIn(gen_all, shift=UP * 0.2), run_time=0.7)
        self.wait(2.5)

        # Keep for cleanup
        self.s2_objects = VGroup(
            sec_label, line_l2, lbl_l1, lbl_l2,
            right_mark, arm1, arm2, int_dot,
            k1_lbl, k2_lbl,
            fx_line1, fx_result, conclusion, gen_all,
        )
        self.line_l1 = line_l1   # l₁ persists into scene 3

    # ── Scene 3: Angle Formula ─────────────────────────────────────────────────
    def scene_3_angle_formula(self):
        ax = self.ax

        # Fade out scene 2 unique elements
        self.play(FadeOut(self.s2_objects), run_time=0.6)

        # ── section label
        sec_label = cn("② 两直线夹角", size=28, color=LINE3_COLOR)
        sec_label.move_to(UP * 5.0)
        self.play(Write(sec_label, run_time=0.6))

        # ── Redraw l₁ label
        p_l1b = self._c2p(ax, self.l1_b)
        lbl_l1_new = MathTex(r"l_1\ (k_1=2)", font_size=22, color=LINE1_COLOR)
        lbl_l1_new.next_to(p_l1b, UR, buff=0.1)
        self.play(FadeIn(lbl_l1_new), run_time=0.3)

        # ── Draw l₃ (gold, k=1/3)
        p_l3a = self._c2p(ax, self.l3_a)
        p_l3b = self._c2p(ax, self.l3_b)
        line_l3 = Line(p_l3a, p_l3b, color=LINE3_COLOR, stroke_width=3)
        lbl_l3 = MathTex(r"l_2\ \left(k_2=\frac{1}{3}\right)", font_size=22, color=LINE3_COLOR)
        lbl_l3.next_to(p_l3b, DR, buff=0.1)

        self.play(Create(line_l3, run_time=0.9))
        self.play(FadeIn(lbl_l3), run_time=0.3)
        self.wait(0.2)

        # ── Angle arc (CCW from l₃ to l₁  →  45°)
        p_int_f  = self._c2p(ax, self.P_int)
        P_l3_f   = self._c2p(ax, self.P_on_l3)
        P_l1_f   = self._c2p(ax, self.P_on_l1)

        angle_arc = Angle.from_three_points(
            P_l3_f, p_int_f, P_l1_f,
            radius=0.55,
            color=ANGLE_COLOR,
            stroke_width=3,
        )
        theta_lbl = MathTex(r"\theta", font_size=28, color=ANGLE_COLOR)
        # Place θ label between the two arms, slightly outward
        mid_angle_dir = (
            (self.P_on_l3 - self.P_int) / np.linalg.norm(self.P_on_l3 - self.P_int) +
            (self.P_on_l1 - self.P_int) / np.linalg.norm(self.P_on_l1 - self.P_int)
        )
        mid_angle_dir /= np.linalg.norm(mid_angle_dir)
        mid_angle_axes = self.P_int + 0.95 * mid_angle_dir
        theta_lbl.move_to(self._c2p(ax, mid_angle_axes))

        self.play(Create(angle_arc, run_time=0.8))
        self.play(FadeIn(theta_lbl), run_time=0.3)
        self.wait(0.3)

        # ── Formula derivation
        form_title = cn("夹角公式", size=24, color=ANGLE_COLOR)
        form_title.move_to(DOWN * 2.0)

        form1 = MathTex(
            r"\tan\theta = \frac{|k_1 - k_2|}{1 + k_1 k_2}",
            font_size=30, color=WHITE
        ).next_to(form_title, DOWN, buff=0.2)

        self.play(Write(form_title, run_time=0.5))
        self.play(Write(form1, run_time=1.0))
        self.wait(0.3)

        # Substitution
        form2 = MathTex(
            r"= \frac{\left|2 - \dfrac{1}{3}\right|}{1 + 2 \cdot \dfrac{1}{3}}",
            font_size=28, color=WHITE
        ).next_to(form1, DOWN, buff=0.25)
        self.play(Write(form2, run_time=0.9))
        self.wait(0.2)

        # Result
        form3 = MathTex(r"= 1", font_size=32, color=HIGHLIGHT_COL)
        form3.next_to(form2, DOWN, buff=0.2)
        self.play(Write(form3, run_time=0.5))

        result_full = MathTex(
            r"\Rightarrow \theta = 45^{\circ}",
            font_size=34, color=YELLOW
        ).next_to(form3, DOWN, buff=0.18)
        self.play(Write(result_full, run_time=0.7))
        self.play(Indicate(result_full, scale_factor=1.15), run_time=0.5)
        self.wait(0.6)

        # Constraint note
        note_lbl  = cn("注意：夹角取锐角", size=20, color=GRAY_A)
        note_form = MathTex(r"\theta \in \left[0,\ \frac{\pi}{2}\right]",
                            font_size=24, color=GRAY_A)
        note_grp  = VGroup(note_lbl, note_form).arrange(RIGHT, buff=0.2)
        note_box  = SurroundingRectangle(note_grp, color=GRAY_C,
                                         buff=0.12, corner_radius=0.1, stroke_width=1)
        note_all  = VGroup(note_box, note_grp)
        note_all.move_to(DOWN * 5.3)
        self.play(FadeIn(note_all, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # Store for cleanup
        self.s3_objects = VGroup(
            sec_label, lbl_l1_new, line_l3, lbl_l3,
            angle_arc, theta_lbl,
            form_title, form1, form2, form3, result_full, note_all,
        )
        self.line_l3 = line_l3

    # ── Scene 4: Summary ───────────────────────────────────────────────────────
    def scene_4_summary(self):
        # Fade out axes region
        self.play(
            FadeOut(self.s3_objects),
            FadeOut(self.ax),
            FadeOut(self.line_l1),
            run_time=0.7
        )

        # Summary title
        sum_title = cn("公式总结", size=34, color=WHITE)
        sum_title.move_to(UP * 5.5)
        self.play(Write(sum_title, run_time=0.6))

        # Box 1: Perpendicular slope condition
        box1_lbl  = cn("斜率式垂直条件", size=21, color=LINE1_COLOR)
        box1_form = MathTex(r"k_1 \cdot k_2 = -1", font_size=30, color=WHITE)
        box1_content = VGroup(box1_lbl, box1_form).arrange(DOWN, buff=0.12)
        box1_rect = SurroundingRectangle(box1_content, color=LINE1_COLOR,
                                          buff=0.2, corner_radius=0.12,
                                          fill_color=FORMULA_BG, fill_opacity=0.9,
                                          stroke_width=2)
        box1 = VGroup(box1_rect, box1_content).move_to(UP * 3.8)

        # Box 2: General form perpendicular
        box2_lbl  = cn("一般式垂直条件", size=21, color=LINE2_COLOR)
        box2_form = MathTex(r"A_1 A_2 + B_1 B_2 = 0", font_size=28, color=WHITE)
        box2_content = VGroup(box2_lbl, box2_form).arrange(DOWN, buff=0.12)
        box2_rect = SurroundingRectangle(box2_content, color=LINE2_COLOR,
                                          buff=0.2, corner_radius=0.12,
                                          fill_color=FORMULA_BG, fill_opacity=0.9,
                                          stroke_width=2)
        box2 = VGroup(box2_rect, box2_content).move_to(UP * 1.5)

        # Box 3: Angle formula
        box3_lbl  = cn("两直线夹角公式", size=21, color=LINE3_COLOR)
        box3_form = MathTex(
            r"\tan\theta = \frac{|k_1 - k_2|}{1 + k_1 k_2}",
            font_size=28, color=WHITE
        )
        box3_content = VGroup(box3_lbl, box3_form).arrange(DOWN, buff=0.12)
        box3_rect = SurroundingRectangle(box3_content, color=LINE3_COLOR,
                                          buff=0.2, corner_radius=0.12,
                                          fill_color=FORMULA_BG, fill_opacity=0.9,
                                          stroke_width=2)
        box3 = VGroup(box3_rect, box3_content).move_to(DOWN * 1.0)

        # Box 4: Range constraint
        box4_lbl  = cn("夹角范围", size=21, color=ANGLE_COLOR)
        box4_form = MathTex(
            r"k_1 k_2 \neq -1,\quad \theta \in \left[0^{\circ},\ 90^{\circ}\right]",
            font_size=24, color=WHITE
        )
        box4_content = VGroup(box4_lbl, box4_form).arrange(DOWN, buff=0.12)
        box4_rect = SurroundingRectangle(box4_content, color=ANGLE_COLOR,
                                          buff=0.2, corner_radius=0.12,
                                          fill_color=FORMULA_BG, fill_opacity=0.9,
                                          stroke_width=2)
        box4 = VGroup(box4_rect, box4_content).move_to(DOWN * 3.5)

        for box in [box1, box2, box3, box4]:
            self.play(FadeIn(box, shift=RIGHT * 0.3), run_time=0.6)

        # Flash all boxes
        self.wait(0.5)
        self.play(
            *[Flash(b.submobjects[0], color=YELLOW, line_length=0.15,
                    flash_radius=b.submobjects[0].width / 2 + 0.2,
                    num_lines=10)
              for b in [box1, box2, box3, box4]],
            run_time=1.0
        )
        self.wait(2.0)

        self.sum_group = VGroup(sum_title, box1, box2, box3, box4)

    # ── Scene 5: Outro ─────────────────────────────────────────────────────────
    def scene_5_outro(self):
        self.play(FadeOut(self.sum_group), run_time=0.5)

        author_large = cn(
            "上海初高中数学直通车\n@emptyandcalm",
            size=32, color=WHITE
        ).move_to(UP * 1.0)
        self.play(Transform(self.author, author_large), run_time=0.8)

        cta = cn("关注我，学更多数学！", size=30, color=YELLOW)
        cta.move_to(DOWN * 0.8)
        self.play(FadeIn(cta, shift=UP * 0.3, scale=1.1), run_time=0.7)
        self.wait(1.5)
"""
平面与平面垂直 - Plane-Plane Perpendicular / Dihedral Angle
高三数学第十四章：空间直线与平面
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_ALPHA   = "#4FC3F7"
C_BETA    = "#F06292"
C_LINE_L  = "#FFD54F"
C_LINE_M  = "#CE93D8"
C_LINE_N  = "#81C784"
C_POINT   = "#FF8A65"
C_ANGLE   = "#A5D6A7"
C_GOLD    = "#FFD700"
C_GRAY    = GRAY_B
FONT_CN   = "PingFang SC"


def iso(x, y, z, sx=0.80, sy=0.52):
    px = (x - y) * sx * 0.5
    py = (x + y) * sy * 0.35 + z * sy
    return np.array([px, py, 0])


def right_angle_sq(corner, v1, v2, size=0.22, color=C_ANGLE):
    u1 = v1 / np.linalg.norm(v1) * size
    u2 = v2 / np.linalg.norm(v2) * size
    return Polygon(corner, corner+u1, corner+u1+u2, corner+u2,
                   color=color, stroke_width=1.8, fill_opacity=0)


class PlanePlanePerpendicularScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_dihedral_angle()
        self.scene_3_definition()
        self.scene_4_criterion()
        self.scene_5_property()
        self.scene_6_summary()
        self.scene_7_outro()

    # ============================================================
    def setup_geometry(self):
        """统一初始化几何数据"""
        # ---- Scene 2: 二面角 ----
        # 棱 l 沿 y 轴方向 (x=0, z=0)
        # 面 α 在 z=0 水平面 (角的一面)
        # 面 β 在 x=0 竖直面 (角的另一面)
        # 棱线
        self.s2_l_s  = iso(0, -2.0, 0)
        self.s2_l_e  = iso(0,  2.0, 0)
        # 在棱上取中点 O
        self.s2_O    = iso(0, 0, 0)
        # α 面内垂直于棱的射线 OA (沿 x 轴正方向)
        self.s2_OA   = iso(2.0, 0, 0)
        # β 面内垂直于棱的射线 OB (沿 z 轴正方向)
        self.s2_OB   = iso(0, 0, 2.0)

        # 验证 OA ⊥ l , OB ⊥ l (3D)
        l3d  = np.array([0, 1, 0])   # 棱方向
        oa3d = np.array([1, 0, 0])   # OA 方向
        ob3d = np.array([0, 0, 1])   # OB 方向
        self.s2_OA_perp_l = abs(np.dot(oa3d, l3d)) < 1e-9
        self.s2_OB_perp_l = abs(np.dot(ob3d, l3d)) < 1e-9

        # 二面角 (3D) = ∠AOB = 90°
        cos_aob = np.dot(oa3d, ob3d)
        self.s2_dihedral_deg = np.degrees(np.arccos(np.clip(cos_aob, -1, 1)))

        # ---- Scene 4: 判定定理 ----
        # 直线 l ⊥ β, l ⊂ α  ⇒  α ⊥ β
        # 水平面 β, 竖直面 α, 直线 l 竖直穿过交线
        self.s4_beta_verts  = [
            iso(-2.5, -1.5, 0), iso(2.5, -1.5, 0),
            iso(2.5,   1.5, 0), iso(-2.5,  1.5, 0),
        ]
        self.s4_alpha_verts = [
            iso(-2.5, 0, -0.2), iso(2.5, 0, -0.2),
            iso(2.5,  0,  2.4), iso(-2.5, 0,  2.4),
        ]
        # 直线 l (竖直, 在α内, ⊥β)
        self.s4_l_bot = iso(0, 0, 0)
        self.s4_l_top = iso(0, 0, 2.2)
        # 验证 l ⊥ β (l沿z, β水平) → 点积=0
        l_3d_s4   = np.array([0, 0, 1])
        beta_n_s4 = np.array([0, 0, 1])   # β法向量 (z轴)
        # l 平行于 β 法向量，即 l ⊥ β
        self.s4_l_perp_beta = abs(np.dot(l_3d_s4, np.array([1, 0, 0]))) < 1e-9 and \
                               abs(np.dot(l_3d_s4, np.array([0, 1, 0]))) < 1e-9

        # ---- Scene 5: 性质定理 ----
        # α ⊥ β, 交线 l, m ⊂ α, m ⊥ l  ⇒  m ⊥ β
        # 同 s4 设置，额外加面内直线 m
        self.s5_beta_verts  = self.s4_beta_verts
        self.s5_alpha_verts = self.s4_alpha_verts
        self.s5_l_s = self.s4_l_bot
        self.s5_l_e = iso(0, 2.2, 0)   # 棱 l 沿 y 方向
        # m 在 α 内, ⊥ l (棱), 即 m 沿 x 轴
        self.s5_m_s = iso(-2.2, 0, 0.8)
        self.s5_m_e = iso( 2.2, 0, 0.8)
        # 验证 m ⊥ l
        l_dir_s5 = np.array([0, 1, 0])
        m_dir_s5 = np.array([1, 0, 0])
        self.s5_m_perp_l = abs(np.dot(l_dir_s5, m_dir_s5)) < 1e-9

        # ---- 边界检查 ----
        all_pts = [
            self.s2_l_s, self.s2_l_e, self.s2_OA, self.s2_OB,
            self.s4_l_bot, self.s4_l_top,
            self.s5_m_s, self.s5_m_e,
        ]
        for pt in all_pts:
            assert abs(pt[0]) <= 4.5, f"X超界: {pt}"
            assert abs(pt[1]) <= 7.0, f"Y超界: {pt}"

        assert self.s2_OA_perp_l, "OA 应垂直于棱 l"
        assert self.s2_OB_perp_l, "OB 应垂直于棱 l"
        assert self.s4_l_perp_beta, "l 应垂直于 β"
        assert self.s5_m_perp_l, "m 应垂直于棱 l"
        print("✓ 几何数据初始化完成")
        print(f"  二面角 (3D) = {self.s2_dihedral_deg:.1f}°")

    # ============================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN*0.2), run_time=0.4)

        hook = Text("两平面如何垂直？", font=FONT_CN, font_size=44, color=C_GOLD).move_to(UP * 5.6)
        sub  = Text("先学二面角，再学面面垂直",
                    font=FONT_CN, font_size=26, color=C_GRAY).move_to(UP * 4.8)
        self.play(Write(hook), run_time=0.6)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.4)

    # ============================================================
    def scene_2_dihedral_angle(self):
        title = Text("二面角", font=FONT_CN, font_size=38, color=C_ANGLE).move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        # 水平半平面 α
        alpha_verts = [
            iso(-2.5, -1.5, 0), iso(2.5, -1.5, 0),
            iso(2.5,   0.0, 0), iso(-2.5,  0.0, 0),
        ]
        alpha = Polygon(*alpha_verts, color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.20, stroke_width=2)
        # 竖直半平面 β
        beta_verts = [
            iso(-2.5, 0, 0), iso(2.5, 0, 0),
            iso(2.5,  0, 2.2), iso(-2.5, 0, 2.2),
        ]
        beta = Polygon(*beta_verts, color=C_BETA, fill_color=C_BETA,
                       fill_opacity=0.20, stroke_width=2)
        la = MathTex(r"\alpha", color=C_ALPHA, font_size=36).move_to(iso(2.0, -1.0, 0))
        lb = MathTex(r"\beta",  color=C_BETA,  font_size=36).move_to(iso(-2.0, 0, 1.8))

        # 棱 l
        line_l = Line(self.s2_l_s, self.s2_l_e, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=32).next_to(self.s2_l_e, UP, buff=0.1)

        self.play(Create(alpha), Write(la), run_time=0.5)
        self.play(Create(beta),  Write(lb), run_time=0.5)
        self.play(Create(line_l), Write(lbl_l), run_time=0.5)

        # 棱上取点 O，作 OA ⊥ l (在α内), OB ⊥ l (在β内)
        O = self.s2_O
        dot_O = Dot(O, radius=0.10, color=C_POINT)
        lbl_O = Text("O", font=FONT_CN, font_size=20, color=C_POINT).next_to(
            O, DOWN+LEFT, buff=0.06)
        self.play(FadeIn(dot_O), Write(lbl_O), run_time=0.3)

        ray_OA = Arrow(O, self.s2_OA, color=C_ALPHA, buff=0,
                       stroke_width=2.5, max_tip_length_to_length_ratio=0.12)
        ray_OB = Arrow(O, self.s2_OB, color=C_BETA,  buff=0,
                       stroke_width=2.5, max_tip_length_to_length_ratio=0.12)
        lA = Text("A", font=FONT_CN, font_size=20, color=C_ALPHA).next_to(
            self.s2_OA, RIGHT, buff=0.08)
        lB = Text("B", font=FONT_CN, font_size=20, color=C_BETA).next_to(
            self.s2_OB, UP, buff=0.08)
        self.play(GrowArrow(ray_OA), Write(lA), run_time=0.5)
        self.play(GrowArrow(ray_OB), Write(lB), run_time=0.5)

        # 角弧（OA与OB在2D中的角度）
        v_oa = self.s2_OA - O
        v_ob = self.s2_OB - O
        n_oa = v_oa[:2] / np.linalg.norm(v_oa[:2])
        n_ob = v_ob[:2] / np.linalg.norm(v_ob[:2])
        start_angle = np.arctan2(n_oa[1], n_oa[0])
        cos2d = np.dot(n_oa, n_ob)
        cos2d = np.clip(cos2d, -1, 1)
        sweep  = np.arccos(cos2d)
        # 确定顺/逆时针
        cross2d = n_oa[0]*n_ob[1] - n_oa[1]*n_ob[0]
        if cross2d < 0:
            sweep = -sweep

        arc = Arc(radius=0.55, start_angle=start_angle, angle=sweep,
                  color=C_ANGLE, stroke_width=2.5)
        arc.move_arc_center_to(O)

        mid_dir = n_oa + n_ob
        if np.linalg.norm(mid_dir) > 0.01:
            mid_dir = mid_dir / np.linalg.norm(mid_dir)
        theta_pos = O + np.array([mid_dir[0], mid_dir[1], 0]) * 0.85
        theta_lbl = MathTex(r"\theta", color=C_ANGLE, font_size=30).move_to(theta_pos)
        self.play(Create(arc), Write(theta_lbl), run_time=0.6)

        desc1 = Text("∠AOB 称为二面角的平面角", font=FONT_CN, font_size=24,
                     color=WHITE).move_to(DOWN * 3.2)
        desc2 = Text("（OA ⊥ l，OB ⊥ l）", font=FONT_CN, font_size=20,
                     color=C_GRAY).move_to(DOWN * 3.9)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(desc2), run_time=0.3)
        self.wait(1.0)

        # 角度数值（示例: 90°）
        deg_lbl = Text(f"示例: {self.s2_dihedral_deg:.0f}° 为直二面角",
                       font=FONT_CN, font_size=22, color=C_GOLD).move_to(DOWN * 4.7)
        self.play(FadeIn(deg_lbl), run_time=0.3)
        self.wait(0.7)

        self.play(
            FadeOut(title), FadeOut(alpha), FadeOut(beta), FadeOut(la), FadeOut(lb),
            FadeOut(line_l), FadeOut(lbl_l),
            FadeOut(dot_O), FadeOut(lbl_O),
            FadeOut(ray_OA), FadeOut(lA), FadeOut(ray_OB), FadeOut(lB),
            FadeOut(arc), FadeOut(theta_lbl),
            FadeOut(desc1), FadeOut(desc2), FadeOut(deg_lbl),
            run_time=0.5
        )

    # ============================================================
    def scene_3_definition(self):
        title = Text("定义：面面垂直", font=FONT_CN, font_size=36,
                     color=C_LINE_L).move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        # 复用二面角图，展示 θ = 90°
        alpha_verts = [
            iso(-2.5, -1.5, 0), iso(2.5, -1.5, 0),
            iso(2.5,   0.0, 0), iso(-2.5,  0.0, 0),
        ]
        beta_verts = [
            iso(-2.5, 0, 0), iso(2.5, 0, 0),
            iso(2.5,  0, 2.2), iso(-2.5, 0, 2.2),
        ]
        alpha = Polygon(*alpha_verts, color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.20, stroke_width=2)
        beta  = Polygon(*beta_verts,  color=C_BETA,  fill_color=C_BETA,
                        fill_opacity=0.20, stroke_width=2)
        la = MathTex(r"\alpha", color=C_ALPHA, font_size=36).move_to(iso(2.0, -1.0, 0))
        lb = MathTex(r"\beta",  color=C_BETA,  font_size=36).move_to(iso(-2.0, 0, 1.8))
        line_l = Line(self.s2_l_s, self.s2_l_e, color=C_LINE_L, stroke_width=3)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=30).next_to(self.s2_l_e, UP, buff=0.08)
        self.play(Create(alpha), Write(la), Create(beta), Write(lb),
                  Create(line_l), Write(lbl_l), run_time=0.7)

        # 直角标记
        O = self.s2_O
        v_oa = (self.s2_OA - O) / np.linalg.norm(self.s2_OA - O)
        v_ob = (self.s2_OB - O) / np.linalg.norm(self.s2_OB - O)
        ra = right_angle_sq(O, v_oa, v_ob, size=0.28, color=C_ANGLE)
        self.play(Create(ra), run_time=0.4)
        self.play(Flash(ra, color=C_ANGLE, flash_radius=0.35), run_time=0.4)

        formula = MathTex(r"\text{Planar Angle} = 90^\circ \;\Rightarrow\; \alpha \perp \beta",
                          font_size=30, color=C_GOLD).move_to(DOWN * 3.2)
        self.play(Write(formula), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(alpha), FadeOut(beta), FadeOut(la), FadeOut(lb),
            FadeOut(line_l), FadeOut(lbl_l), FadeOut(ra), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    def scene_4_criterion(self):
        title = Text("判定定理", font=FONT_CN, font_size=36, color=C_LINE_M).move_to(UP * 6.1)
        sub   = Text("过 β 的垂线在 α 内  ⇒  α ⊥ β",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.4)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        beta  = Polygon(*self.s4_beta_verts,  color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.13, stroke_width=2)
        alpha = Polygon(*self.s4_alpha_verts, color=C_BETA,  fill_color=C_BETA,
                        fill_opacity=0.15, stroke_width=2)
        lb = MathTex(r"\beta",  color=C_ALPHA, font_size=36).move_to(iso(2.4, 1.2, 0.0))
        la = MathTex(r"\alpha", color=C_BETA,  font_size=36).move_to(iso(-2.2, 0, 2.0))
        self.play(Create(beta), Write(lb), run_time=0.5)
        self.play(Create(alpha), Write(la), run_time=0.5)

        # 垂线 l (在α内, ⊥β)
        line_l = Line(self.s4_l_bot, self.s4_l_top, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=32).next_to(
            self.s4_l_top, UP, buff=0.1)
        self.play(Create(line_l), Write(lbl_l), run_time=0.5)

        # 直角标记 l ⊥ β
        v_l2d  = (self.s4_l_top - self.s4_l_bot)
        v_l2d  = v_l2d / np.linalg.norm(v_l2d)
        h_dir  = np.array([1, 0, 0])
        ra_lb  = right_angle_sq(self.s4_l_bot, v_l2d, h_dir, size=0.22, color=C_ANGLE)
        self.play(Create(ra_lb), run_time=0.4)

        note_l = Text("l ⊥ β（l 在 α 内）", font=FONT_CN, font_size=24,
                      color=C_LINE_L).move_to(DOWN * 3.2)
        conc   = MathTex(r"l \perp \beta,\; l \subset \alpha \;\Rightarrow\; \alpha \perp \beta",
                         font_size=28, color=C_GOLD).move_to(DOWN * 4.3)
        self.play(FadeIn(note_l, shift=UP*0.2), run_time=0.4)
        self.play(Write(conc), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(beta), FadeOut(lb), FadeOut(alpha), FadeOut(la),
            FadeOut(line_l), FadeOut(lbl_l), FadeOut(ra_lb),
            FadeOut(note_l), FadeOut(conc),
            run_time=0.5
        )

    # ============================================================
    def scene_5_property(self):
        title = Text("性质定理", font=FONT_CN, font_size=36, color=C_LINE_N).move_to(UP * 6.1)
        sub   = Text("α⊥β，m⊂α，m⊥交线  ⇒  m⊥β",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.4)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        beta  = Polygon(*self.s5_beta_verts,  color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.13, stroke_width=2)
        alpha = Polygon(*self.s5_alpha_verts, color=C_BETA,  fill_color=C_BETA,
                        fill_opacity=0.15, stroke_width=2)
        lb = MathTex(r"\beta",  color=C_ALPHA, font_size=34).move_to(iso(2.4, 1.2, 0.0))
        la = MathTex(r"\alpha", color=C_BETA,  font_size=34).move_to(iso(-2.2, 0, 2.0))
        self.play(Create(beta), Write(lb), Create(alpha), Write(la), run_time=0.7)

        # 交线 l (沿 y 轴)
        line_l = Line(self.s5_l_s, self.s5_l_e, color=C_LINE_L, stroke_width=3)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=30).next_to(self.s5_l_e, UP, buff=0.08)
        self.play(Create(line_l), Write(lbl_l), run_time=0.5)

        # 直线 m (在α内, ⊥l)
        line_m = Line(self.s5_m_s, self.s5_m_e, color=C_LINE_N, stroke_width=3)
        lbl_m  = MathTex("m", color=C_LINE_N, font_size=30).next_to(
            self.s5_m_e, RIGHT, buff=0.1)
        self.play(Create(line_m), Write(lbl_m), run_time=0.5)

        # m ⊥ l 的直角标记
        foot_ml = iso(0, 0, 0.8)   # m 与棱 l 的交点（投影点）
        v_m2d   = (self.s5_m_e - self.s5_m_s) / np.linalg.norm(self.s5_m_e - self.s5_m_s)
        v_l2d   = (self.s5_l_e - self.s5_l_s) / np.linalg.norm(self.s5_l_e - self.s5_l_s)
        ra_ml   = right_angle_sq(foot_ml, v_m2d, v_l2d, size=0.20, color=C_ANGLE)
        self.play(Create(ra_ml), run_time=0.4)

        # 结论：m ⊥ β
        conc = Text("结论：m ⊥ β", font=FONT_CN, font_size=28, color=WHITE).move_to(DOWN * 3.2)
        formula = MathTex(
            r"\alpha \perp \beta,\; m \subset \alpha,\; m \perp l \;\Rightarrow\; m \perp \beta",
            font_size=24, color=C_GOLD
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(conc, shift=UP*0.2), run_time=0.4)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.3)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(beta), FadeOut(lb), FadeOut(alpha), FadeOut(la),
            FadeOut(line_l), FadeOut(lbl_l),
            FadeOut(line_m), FadeOut(lbl_m), FadeOut(ra_ml),
            FadeOut(conc), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    def scene_6_summary(self):
        title = Text("核心总结", font=FONT_CN, font_size=36, color=C_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        items = [
            ("二面角",  "从一棱出发的两半平面所成图形", C_ANGLE),
            ("平面角",  "OA⊥l，OB⊥l，∠AOB 即平面角", C_ANGLE),
            ("定义",    "平面角 = 90° ⇒ α ⊥ β",       C_LINE_L),
            ("判定",    "l⊥β，l⊂α ⇒ α⊥β",            C_LINE_M),
            ("性质",    "α⊥β，m⊂α，m⊥l ⇒ m⊥β",      C_LINE_N),
        ]
        y = 4.5
        groups = VGroup()
        for (name, desc, col) in items:
            box = RoundedRectangle(width=7.6, height=1.1, corner_radius=0.18,
                                   color=col, fill_color=col, fill_opacity=0.07,
                                   stroke_width=1.4).move_to(np.array([0, y, 0]))
            t1 = Text(name, font=FONT_CN, font_size=22, color=col)
            t2 = Text(desc, font=FONT_CN, font_size=18, color=WHITE)
            VGroup(t1, t2).arrange(RIGHT, buff=0.3).move_to(box.get_center())
            grp = VGroup(box, t1, t2)
            groups.add(grp)
            self.play(FadeIn(grp, shift=RIGHT*0.3), run_time=0.35)
            y -= 1.55

        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(groups), run_time=0.5)

    # ============================================================
    def scene_7_outro(self):
        big = Text("上海初高中数学直通车", font=FONT_CN, font_size=38, color=WHITE).move_to(UP * 1.5)
        uid = Text("@emptyandcalm", font=FONT_CN, font_size=28, color=C_GRAY).move_to(UP * 0.5)
        flw = Text("关注我，获得更多数学技巧！",
                   font=FONT_CN, font_size=30, color=C_GOLD).move_to(DOWN * 0.5)
        self.play(Transform(self.author, big), run_time=0.6)
        self.play(FadeIn(uid, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(flw, scale=1.05), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(self.author), FadeOut(uid), FadeOut(flw), run_time=0.8)
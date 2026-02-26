"""
直线与平面垂直 - Line Perpendicular to Plane
高三数学第十四章：空间直线与平面
目标受众: 高三学生
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
C_BETA    = "#81C784"
C_LINE_L  = "#FFD54F"
C_LINE_M  = "#F06292"
C_LINE_N  = "#CE93D8"
C_POINT   = "#FF8A65"
C_GOLD    = "#FFD700"
C_GRAY    = GRAY_B
C_RA      = "#A5D6A7"    # 直角标记
FONT_CN   = "Noto Sans CJK SC"


def iso(x, y, z, sx=0.85, sy=0.55):
    px = (x - y) * sx * 0.5
    py = (x + y) * sy * 0.35 + z * sy
    return np.array([px, py, 0])


def right_angle_mark(corner, v1, v2, size=0.22, color=C_RA):
    """在 corner 处沿 v1 和 v2 方向画直角符号"""
    u1 = v1 / np.linalg.norm(v1) * size
    u2 = v2 / np.linalg.norm(v2) * size
    return Polygon(
        corner,
        corner + u1,
        corner + u1 + u2,
        corner + u2,
        color=color, stroke_width=1.8, fill_opacity=0
    )


class LinePlanePerpendicularScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_criterion()
        self.scene_4_property1()
        self.scene_5_property2()
        self.scene_6_summary()
        self.scene_7_outro()

    # ============================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ---- Scene 2: 定义 ----
        # 平面在中部，竖直线l从平面上方穿下
        self.s2_plane_verts = [
            iso(-2.5, -1.5, 0), iso( 2.5, -1.5, 0),
            iso( 2.5,  1.5, 0), iso(-2.5,  1.5, 0),
        ]
        self.s2_foot = iso(0, 0, 0)        # 垂足
        self.s2_top  = iso(0, 0, 2.5)      # l 的上端
        # 平面内两条线（验证都垂直）
        self.s2_m_start = iso(-2, 0, 0)
        self.s2_m_end   = iso( 2, 0, 0)
        self.s2_n_start = iso(0, -1.8, 0)
        self.s2_n_end   = iso(0,  1.8, 0)

        # ---- Scene 3: 判定定理 ----
        # 平面内两条相交直线 m, n
        # 直线 l 同时垂直于 m 和 n → l ⊥ α
        self.s3_plane_verts = [
            iso(-2.5, -1.5, 0), iso( 2.5, -1.5, 0),
            iso( 2.5,  1.5, 0), iso(-2.5,  1.5, 0),
        ]
        self.s3_P     = iso(0, 0, 0)           # 交点P（m∩n）
        self.s3_m_s   = iso(-2.2, 0, 0)
        self.s3_m_e   = iso( 2.2, 0, 0)
        self.s3_n_s   = iso(0, -1.8, 0)
        self.s3_n_e   = iso(0,  1.8, 0)
        self.s3_l_bot = iso(0, 0, 0)
        self.s3_l_top = iso(0, 0, 2.5)

        # 验证直角（3D空间）
        # l方向(0,0,1), m方向(1,0,0), n方向(0,1,0)
        l3d = np.array([0, 0, 1])
        m3d = np.array([1, 0, 0])
        n3d = np.array([0, 1, 0])
        self.s3_lm_dot = np.dot(l3d, m3d)  # 应为0
        self.s3_ln_dot = np.dot(l3d, n3d)  # 应为0
        assert abs(self.s3_lm_dot) < 1e-10, "l不垂直m"
        assert abs(self.s3_ln_dot) < 1e-10, "l不垂直n"

        # ---- Scene 4: 性质1（两垂线平行）----
        # 两直线 l1, l2 都垂直于平面α → l1 ∥ l2
        self.s4_plane_verts = [
            iso(-3, -1.5, 0), iso( 3, -1.5, 0),
            iso( 3,  1.5, 0), iso(-3,  1.5, 0),
        ]
        self.s4_l1_bot = iso(-1.5, 0, 0)
        self.s4_l1_top = iso(-1.5, 0, 2.5)
        self.s4_l2_bot = iso( 1.5, 0, 0)
        self.s4_l2_top = iso( 1.5, 0, 2.5)

        # ---- Scene 5: 性质2（垂直关系传递）----
        # l ⊥ α, m ⊂ α → l ⊥ m
        self.s5_plane_verts = self.s3_plane_verts  # 复用
        self.s5_l_bot = iso(0, 0, 0)
        self.s5_l_top = iso(0, 0, 2.5)
        self.s5_m_s   = iso(-2.2, 0.8, 0)
        self.s5_m_e   = iso( 2.2, 0.8, 0)
        self.s5_foot  = iso(0, 0, 0)   # l 的垂足

        # 边界检查
        all_pts = [
            self.s2_foot, self.s2_top,
            self.s3_l_bot, self.s3_l_top,
            self.s4_l1_top, self.s4_l2_top,
        ]
        for pt in all_pts:
            assert abs(pt[0]) <= 4.5, f"X超界: {pt}"
            assert abs(pt[1]) <= 7.5, f"Y超界: {pt}"
        print("✓ 几何数据初始化完成")
        print(f"  l⊥m 点积验证: {self.s3_lm_dot}, l⊥n 点积验证: {self.s3_ln_dot}")

    # ============================================================
    def _draw_plane(self, verts, color=C_ALPHA, fo=0.12, sw=2):
        return Polygon(*verts, color=color, fill_color=color,
                       fill_opacity=fo, stroke_width=sw)

    # ============================================================
    # Scene 1: 开场
    # ============================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN*0.2), run_time=0.4)

        hook = Text("直线与平面垂直", font=FONT_CN, font_size=46, color=C_GOLD).move_to(UP * 5.5)
        sub  = Text("定义 + 判定 + 两大性质",
                    font=FONT_CN, font_size=26, color=C_GRAY).move_to(UP * 4.7)
        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.4)

    # ============================================================
    # Scene 2: 定义
    # ============================================================
    def scene_2_definition(self):
        title = Text("定义：线面垂直", font=FONT_CN, font_size=36, color=C_LINE_L).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        plane = self._draw_plane(self.s2_plane_verts)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=40).move_to(iso(2.2, 1.3, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.7)

        # 平面内两条线
        line_m = Line(self.s2_m_start, self.s2_m_end, color=C_LINE_M, stroke_width=2)
        line_n = Line(self.s2_n_start, self.s2_n_end, color=C_LINE_N, stroke_width=2)
        self.play(Create(line_m), Create(line_n), run_time=0.5)

        # 垂直线 l
        line_l = Line(self.s2_foot, self.s2_top, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=36).next_to(self.s2_top, UP, buff=0.1)
        self.play(Create(line_l), Write(lbl_l), run_time=0.6)

        # 直角标记
        v_l  = (self.s2_top - self.s2_foot) / np.linalg.norm(self.s2_top - self.s2_foot)
        v_m2d = (self.s2_m_end - self.s2_m_start) / np.linalg.norm(self.s2_m_end - self.s2_m_start)
        v_n2d = (self.s2_n_end - self.s2_n_start) / np.linalg.norm(self.s2_n_end - self.s2_n_start)
        ra_m = right_angle_mark(self.s2_foot, v_l, v_m2d)
        ra_n = right_angle_mark(self.s2_foot + v_m2d * 0.22, v_l, v_n2d)
        self.play(Create(ra_m), Create(ra_n), run_time=0.5)

        desc = Text("与平面内任意直线都垂直", font=FONT_CN, font_size=26,
                    color=WHITE).move_to(DOWN * 3.0)
        formula = MathTex(r"l \perp \alpha \;\Leftrightarrow\; \forall m \subset \alpha,\; l \perp m",
                          font_size=28, color=C_GOLD).move_to(DOWN * 4.0)
        self.play(FadeIn(desc, shift=UP*0.2), run_time=0.4)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(line_m), FadeOut(line_n),
            FadeOut(line_l), FadeOut(lbl_l),
            FadeOut(ra_m), FadeOut(ra_n),
            FadeOut(desc), FadeOut(formula), run_time=0.5
        )

    # ============================================================
    # Scene 3: 判定定理
    # ============================================================
    def scene_3_criterion(self):
        title = Text("判定定理", font=FONT_CN, font_size=36, color=C_LINE_N).move_to(UP * 6.2)
        sub   = Text("两垂直相交 ⇒ 线面垂直", font=FONT_CN, font_size=24,
                     color=C_GRAY).move_to(UP * 5.5)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        plane = self._draw_plane(self.s3_plane_verts)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=38).move_to(iso(2.2, 1.3, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.7)

        # 交点 P
        dot_P  = Dot(self.s3_P, radius=0.10, color=C_POINT)
        lbl_P  = Text("P", font=FONT_CN, font_size=22, color=C_POINT).next_to(
            self.s3_P, DOWN+LEFT, buff=0.06)
        self.play(FadeIn(dot_P), Write(lbl_P), run_time=0.3)

        # 直线 m
        line_m = Line(self.s3_m_s, self.s3_m_e, color=C_LINE_M, stroke_width=2.5)
        lbl_m  = MathTex("m", color=C_LINE_M, font_size=32).next_to(self.s3_m_e, RIGHT, buff=0.1)
        # 直线 n
        line_n = Line(self.s3_n_s, self.s3_n_e, color=C_LINE_N, stroke_width=2.5)
        lbl_n  = MathTex("n", color=C_LINE_N, font_size=32).next_to(self.s3_n_e, UP, buff=0.1)
        self.play(Create(line_m), Write(lbl_m), run_time=0.4)
        self.play(Create(line_n), Write(lbl_n), run_time=0.4)

        # 直线 l（垂直穿过P）
        line_l = Line(self.s3_l_bot, self.s3_l_top, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=34).next_to(self.s3_l_top, UP, buff=0.1)
        self.play(Create(line_l), Write(lbl_l), run_time=0.6)

        # 直角标记 at P（l与m, l与n）
        v_l2d = self.s3_l_top - self.s3_l_bot
        v_l2d = v_l2d / np.linalg.norm(v_l2d)
        v_m2d = self.s3_m_e - self.s3_m_s
        v_m2d = v_m2d / np.linalg.norm(v_m2d)
        v_n2d = self.s3_n_e - self.s3_n_s
        v_n2d = v_n2d / np.linalg.norm(v_n2d)

        ra_lm = right_angle_mark(self.s3_P, v_l2d, v_m2d, size=0.20)
        ra_ln = right_angle_mark(self.s3_P + v_m2d * 0.20, v_l2d, v_n2d, size=0.20)

        note_lm = MathTex(r"l \perp m", color=C_LINE_M, font_size=28).move_to(np.array([-2.5, -1.8, 0]))
        note_ln = MathTex(r"l \perp n", color=C_LINE_N, font_size=28).move_to(np.array([ 2.0, -1.8, 0]))
        self.play(Create(ra_lm), Create(ra_ln), run_time=0.4)
        self.play(Write(note_lm), Write(note_ln), run_time=0.4)

        conc = Text("m ∩ n = P（相交），则 l ⊥ α",
                    font=FONT_CN, font_size=24, color=WHITE).move_to(DOWN * 3.0)
        formula = MathTex(
            r"l \perp m,\; l \perp n,\; m \cap n = P \;\Rightarrow\; l \perp \alpha",
            font_size=24, color=C_GOLD
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(conc, shift=UP*0.2), run_time=0.4)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(dot_P), FadeOut(lbl_P),
            FadeOut(line_m), FadeOut(lbl_m),
            FadeOut(line_n), FadeOut(lbl_n),
            FadeOut(line_l), FadeOut(lbl_l),
            FadeOut(ra_lm), FadeOut(ra_ln),
            FadeOut(note_lm), FadeOut(note_ln),
            FadeOut(conc), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    # Scene 4: 性质1 — 两垂线平行
    # ============================================================
    def scene_4_property1(self):
        title = Text("性质定理 ①", font=FONT_CN, font_size=34, color=C_LINE_M).move_to(UP * 6.2)
        sub   = Text("两条垂直于同一平面的直线互相平行",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.5)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        plane = self._draw_plane(self.s4_plane_verts)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=38).move_to(iso(2.8, 1.5, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.7)

        # 直线 l1
        line_l1 = Line(self.s4_l1_bot, self.s4_l1_top, color=C_LINE_L, stroke_width=3.5)
        lbl_l1  = MathTex("l_1", color=C_LINE_L, font_size=32).next_to(self.s4_l1_top, UP, buff=0.1)
        # 直线 l2
        line_l2 = Line(self.s4_l2_bot, self.s4_l2_top, color=C_LINE_M, stroke_width=3.5)
        lbl_l2  = MathTex("l_2", color=C_LINE_M, font_size=32).next_to(self.s4_l2_top, UP, buff=0.1)

        self.play(Create(line_l1), Write(lbl_l1), run_time=0.5)
        self.play(Create(line_l2), Write(lbl_l2), run_time=0.5)

        # 直角标记（底部）
        v_l = (self.s4_l1_top - self.s4_l1_bot) / np.linalg.norm(self.s4_l1_top - self.s4_l1_bot)
        # 水平方向（投影）
        h_dir = np.array([1, 0, 0])
        ra1 = right_angle_mark(self.s4_l1_bot, v_l, h_dir, size=0.22)
        ra2 = right_angle_mark(self.s4_l2_bot, v_l, -h_dir, size=0.22)
        self.play(Create(ra1), Create(ra2), run_time=0.4)

        # 平行双箭头
        par_line = DashedLine(self.s4_l1_top, self.s4_l2_top,
                              color=C_GOLD, dash_length=0.12, stroke_width=2)
        par_sym  = MathTex(r"l_1 \parallel l_2", color=C_GOLD, font_size=36).move_to(
            np.array([0, 3.0, 0]))
        self.play(Create(par_line), run_time=0.5)
        self.play(Write(par_sym), run_time=0.5)

        formula = MathTex(r"l_1 \perp \alpha,\; l_2 \perp \alpha \;\Rightarrow\; l_1 \parallel l_2",
                          font_size=28, color=C_GOLD).move_to(DOWN * 3.5)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(line_l1), FadeOut(lbl_l1),
            FadeOut(line_l2), FadeOut(lbl_l2),
            FadeOut(ra1), FadeOut(ra2),
            FadeOut(par_line), FadeOut(par_sym), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    # Scene 5: 性质2 — 垂直传递
    # ============================================================
    def scene_5_property2(self):
        title = Text("性质定理 ②", font=FONT_CN, font_size=34, color=C_LINE_N).move_to(UP * 6.2)
        sub   = Text("线面垂直 ⇒ 垂直于面内任意直线",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.5)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        plane = self._draw_plane(self.s5_plane_verts)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=38).move_to(iso(2.2, 1.3, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.7)

        # 面内直线 m
        line_m = Line(self.s5_m_s, self.s5_m_e, color=C_LINE_M, stroke_width=2.5)
        lbl_m  = MathTex("m", color=C_LINE_M, font_size=32).next_to(self.s5_m_e, RIGHT, buff=0.1)
        note_m = Text("m ⊂ α", font=FONT_CN, font_size=22, color=C_LINE_M).move_to(DOWN * 3.2)
        self.play(Create(line_m), Write(lbl_m), FadeIn(note_m), run_time=0.5)

        # 垂直线 l
        line_l = Line(self.s5_l_bot, self.s5_l_top, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=34).next_to(self.s5_l_top, UP, buff=0.1)
        note_l = Text("l ⊥ α", font=FONT_CN, font_size=22, color=C_LINE_L).move_to(DOWN * 3.9)
        self.play(Create(line_l), Write(lbl_l), FadeIn(note_l), run_time=0.5)

        # 垂足处直角标记
        foot = self.s5_foot
        v_l2d = (self.s5_l_top - self.s5_l_bot) / np.linalg.norm(self.s5_l_top - self.s5_l_bot)
        v_m2d = (self.s5_m_e - self.s5_m_s) / np.linalg.norm(self.s5_m_e - self.s5_m_s)

        # 找 l 与 m 的最近点（投影到 m 上）
        t = np.dot(foot - self.s5_m_s, v_m2d)
        proj_on_m = self.s5_m_s + t * v_m2d

        ra = right_angle_mark(proj_on_m, v_l2d, -v_m2d, size=0.22)
        perp_label = MathTex(r"l \perp m", color=C_RA, font_size=30).move_to(
            np.array([-2.0, 0.5, 0]))
        self.play(Create(ra), Write(perp_label), run_time=0.5)
        self.play(Flash(ra, color=C_RA, flash_radius=0.3), run_time=0.4)

        formula = MathTex(r"l \perp \alpha,\; m \subset \alpha \;\Rightarrow\; l \perp m",
                          font_size=28, color=C_GOLD).move_to(DOWN * 5.0)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(line_m), FadeOut(lbl_m), FadeOut(note_m),
            FadeOut(line_l), FadeOut(lbl_l), FadeOut(note_l),
            FadeOut(ra), FadeOut(perp_label), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    # Scene 6: 总结
    # ============================================================
    def scene_6_summary(self):
        title = Text("核心总结", font=FONT_CN, font_size=36, color=C_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        items = [
            ("定义", "与面内任意直线都垂直", C_LINE_L),
            ("判定", "与面内两相交直线都垂直 ⇒ ⊥面", C_LINE_N),
            ("性质①", "两线⊥同一平面 ⇒ 两线平行", C_LINE_M),
            ("性质②", "线⊥面，则⊥面内所有直线", C_RA),
        ]
        y = 4.2
        groups = VGroup()
        for (name, desc, col) in items:
            box = RoundedRectangle(width=7.5, height=1.2, corner_radius=0.2,
                                   color=col, fill_color=col, fill_opacity=0.07,
                                   stroke_width=1.5)
            box.move_to(np.array([0, y, 0]))
            t1 = Text(name, font=FONT_CN, font_size=24, color=col)
            t2 = Text(desc, font=FONT_CN, font_size=18, color=WHITE)
            inner = VGroup(t1, t2).arrange(RIGHT, buff=0.3)
            inner.move_to(box.get_center())
            groups.add(VGroup(box, inner))
            self.play(FadeIn(VGroup(box, inner), shift=RIGHT*0.3), run_time=0.4)
            y -= 1.7

        tip = Text("口诀：两交线⊥ → 线面⊥，两线⊥面 → 两线平行",
                   font=FONT_CN, font_size=20, color=C_GRAY).move_to(DOWN * 1.5)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(groups), FadeOut(tip), run_time=0.5)

    # ============================================================
    # Scene 7: 片尾
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
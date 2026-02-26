"""
直线与平面平行 - Line Parallel to Plane
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
C_ALPHA   = "#4FC3F7"    # 蓝  平面α
C_BETA    = "#81C784"    # 绿  平面β
C_LINE_L  = "#FFD54F"    # 金黄 直线l
C_LINE_M  = "#F06292"    # 粉红 直线m
C_POINT   = "#FF8A65"    # 橙  点
C_GOLD    = "#FFD700"
C_GRAY    = GRAY_B
C_COND    = "#CE93D8"    # 紫  条件
FONT_CN   = "Noto Sans CJK SC"


def iso(x, y, z, sx=0.85, sy=0.55, ox=0, oy=0):
    px = ox + (x - y) * sx * 0.5
    py = oy + (x + y) * sy * 0.35 + z * sy
    return np.array([px, py, 0])


def make_plane_para(cx, cy, W=4.5, D=2.0, **kwargs):
    """平面平行四边形（透视）"""
    verts = [
        iso(cx - W/2, cy - D/2, 0),
        iso(cx + W/2, cy - D/2, 0),
        iso(cx + W/2, cy + D/2, 0),
        iso(cx - W/2, cy + D/2, 0),
    ]
    return Polygon(*verts, **kwargs)


class LinePlaneParallelScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_criterion()
        self.scene_4_property()
        self.scene_5_summary()
        self.scene_6_outro()

    # ============================================================
    def setup_geometry(self):
        """统一初始化几何数据"""
        # ---- Scene 2: 定义 ----
        # 平面α（中部）, 直线l在面上方平行通过
        self.s2_plane_c   = (0, 0)          # 平面中心 (3D-xy)
        # l 在 z=1.2 高度，方向沿x轴
        self.s2_l_start   = iso(-2.2, 0, 1.2)
        self.s2_l_end     = iso( 2.2, 0, 1.2)
        # l 在平面上的投影（辅助虚线）
        self.s2_proj_s    = iso(-2.2, 0, 0)
        self.s2_proj_e    = iso( 2.2, 0, 0)

        # ---- Scene 3: 判定定理 ----
        # l 在面外, m 在面内, l ∥ m
        self.s3_plane_c   = (0, 0)
        # m 在平面内（z=0）
        self.s3_m_start   = iso(-2, 0.5, 0)
        self.s3_m_end     = iso( 2, 0.5, 0)
        # l 在平面外（z=1.2），与m方向相同（都沿x轴方向）
        self.s3_l_start   = iso(-2, -0.5, 1.2)
        self.s3_l_end     = iso( 2, -0.5, 1.2)
        # 验证l和m方向相同
        dir_l = self.s3_l_end - self.s3_l_start
        dir_m = self.s3_m_end - self.s3_m_start
        cos_v = np.dot(dir_l[:2], dir_m[:2]) / (
            np.linalg.norm(dir_l[:2]) * np.linalg.norm(dir_m[:2]) + 1e-12)
        self.s3_parallel_ok = abs(cos_v - 1.0) < 0.01
        print(f"  Scene3: l∥m 验证: cos={cos_v:.6f}, ok={self.s3_parallel_ok}")

        # ---- Scene 4: 性质定理 ----
        # l∥α, β过l, α∩β=m → l∥m
        # 平面α（蓝），平面β（绿，垂直切过）
        # 直线l在β上（z方向延伸），交线m在两平面交处
        self.s4_alpha_verts = [
            iso(-3, -1.5, 0),
            iso( 3, -1.5, 0),
            iso( 3,  1.5, 0),
            iso(-3,  1.5, 0),
        ]
        # 平面β: 过 y=0 的竖平面（垂直于α）
        self.s4_beta_verts = [
            iso(-2, 0, 0),
            iso( 2, 0, 0),
            iso( 2, 0, 2.0),
            iso(-2, 0, 2.0),
        ]
        # 交线m = α∩β (z=0, y=0 方向，x轴)
        self.s4_m_start = iso(-2, 0, 0)
        self.s4_m_end   = iso( 2, 0, 0)
        # 直线l（在β上，z=1.5高度）
        self.s4_l_start = iso(-1.8, 0, 1.5)
        self.s4_l_end   = iso( 1.8, 0, 1.5)

        # 验证l与m方向
        dir_l4 = self.s4_l_end - self.s4_l_start
        dir_m4 = self.s4_m_end - self.s4_m_start
        cos4 = np.dot(dir_l4[:2], dir_m4[:2]) / (
            np.linalg.norm(dir_l4[:2]) * np.linalg.norm(dir_m4[:2]) + 1e-12)
        print(f"  Scene4: l∥m 验证: cos={cos4:.6f}")

        # 边界检查
        all_pts = [
            self.s2_l_start, self.s2_l_end,
            self.s3_l_start, self.s3_l_end,
            self.s3_m_start, self.s3_m_end,
            self.s4_l_start, self.s4_l_end,
            self.s4_m_start, self.s4_m_end,
        ]
        for pt in all_pts:
            assert abs(pt[0]) < 4.5, f"X超界: {pt}"
            assert abs(pt[1]) < 7.5, f"Y超界: {pt}"
        print("✓ 几何数据初始化完成")

    # ============================================================
    # Scene 1: 开场
    # ============================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN*0.2), run_time=0.4)

        hook = Text("直线与平面平行", font=FONT_CN, font_size=46, color=C_GOLD).move_to(UP * 5.5)
        sub  = Text("判定 & 性质 两大定理", font=FONT_CN, font_size=28,
                    color=C_GRAY).move_to(UP * 4.7)
        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.4)

    # ============================================================
    # Scene 2: 定义
    # ============================================================
    def scene_2_definition(self):
        title = Text("定义：线面平行", font=FONT_CN, font_size=36, color=C_LINE_L).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        plane = make_plane_para(0, 0, W=4.5, D=2.0,
                                color=C_ALPHA, fill_color=C_ALPHA,
                                fill_opacity=0.13, stroke_width=2)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=42).move_to(
            iso(2.8, 1.3, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.8)

        # 直线l在面上方，颜色分明
        line_l = Line(self.s2_l_start, self.s2_l_end, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=36).next_to(
            self.s2_l_end, RIGHT, buff=0.1)
        self.play(Create(line_l), Write(lbl_l), run_time=0.7)

        # 投影虚线（显示不接触平面）
        proj_line = DashedLine(self.s2_proj_s, self.s2_proj_e,
                               color=C_ALPHA, dash_length=0.1, stroke_width=1.5)
        vert_l = DashedLine(self.s2_l_start, self.s2_proj_s,
                            color=C_GRAY, dash_length=0.08, stroke_width=1.2)
        vert_r = DashedLine(self.s2_l_end, self.s2_proj_e,
                            color=C_GRAY, dash_length=0.08, stroke_width=1.2)
        self.play(Create(proj_line), Create(vert_l), Create(vert_r), run_time=0.6)

        desc1 = Text("直线 l 与平面 α 无公共点", font=FONT_CN,
                     font_size=26, color=WHITE).move_to(DOWN * 2.8)
        formula = MathTex(r"l \cap \alpha = \emptyset \;\Rightarrow\; l \parallel \alpha",
                          font_size=36, color=C_GOLD).move_to(DOWN * 3.8)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.4)
        self.play(Write(formula), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(line_l), FadeOut(lbl_l),
            FadeOut(proj_line), FadeOut(vert_l), FadeOut(vert_r),
            FadeOut(desc1), FadeOut(formula), run_time=0.5
        )

    # ============================================================
    # Scene 3: 判定定理
    # ============================================================
    def scene_3_criterion(self):
        title = Text("判定定理", font=FONT_CN, font_size=36, color=C_COND).move_to(UP * 6.2)
        sub   = Text("线线平行 ⇒ 线面平行", font=FONT_CN, font_size=26,
                     color=C_GRAY).move_to(UP * 5.5)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 平面α
        plane = make_plane_para(0, 0, W=4.5, D=2.0,
                                color=C_ALPHA, fill_color=C_ALPHA,
                                fill_opacity=0.13, stroke_width=2)
        alpha_lbl = MathTex(r"\alpha", color=C_ALPHA, font_size=40).move_to(iso(2.8, 1.3, 0))
        self.play(Create(plane), Write(alpha_lbl), run_time=0.7)

        # 直线m（在α内）
        line_m = Line(self.s3_m_start, self.s3_m_end, color=C_LINE_M, stroke_width=3)
        lbl_m  = MathTex("m", color=C_LINE_M, font_size=34).next_to(
            self.s3_m_end, RIGHT, buff=0.1)
        note_m = Text("m ⊂ α（m 在平面内）", font=FONT_CN, font_size=22,
                      color=C_LINE_M).move_to(DOWN * 3.0)
        self.play(Create(line_m), Write(lbl_m), run_time=0.5)
        self.play(FadeIn(note_m), run_time=0.3)

        # 直线l（在α外，与m平行）
        line_l = Line(self.s3_l_start, self.s3_l_end, color=C_LINE_L, stroke_width=3)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=34).next_to(
            self.s3_l_end, RIGHT, buff=0.1)
        note_l = Text("l ∉ α（l 在平面外）", font=FONT_CN, font_size=22,
                      color=C_LINE_L).move_to(DOWN * 3.7)
        self.play(Create(line_l), Write(lbl_l), run_time=0.5)
        self.play(FadeIn(note_l), run_time=0.3)

        # 平行符号标注
        par_note = MathTex(r"l \parallel m", color=C_COND, font_size=36).move_to(
            np.array([-2.5, 0.2, 0]))
        par_arrow = Arrow(par_note.get_right(), par_note.get_right() + RIGHT * 0.7,
                          color=C_COND, buff=0.05)
        self.play(Write(par_note), GrowArrow(par_arrow), run_time=0.5)

        # 结论：l ∥ α
        conc_txt = Text("⇒ 直线 l 与平面 α 平行",
                        font=FONT_CN, font_size=26, color=WHITE).move_to(DOWN * 4.6)
        self.play(FadeOut(note_m), FadeOut(note_l), run_time=0.2)
        self.play(FadeIn(conc_txt, shift=UP*0.2), run_time=0.4)

        formula = MathTex(r"l \parallel m,\; m \subset \alpha,\; l \notin \alpha \;\Rightarrow\; l \parallel \alpha",
                          font_size=26, color=C_GOLD).move_to(DOWN * 5.5)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(line_m), FadeOut(lbl_m),
            FadeOut(line_l), FadeOut(lbl_l),
            FadeOut(par_note), FadeOut(par_arrow),
            FadeOut(conc_txt), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    # Scene 4: 性质定理
    # ============================================================
    def scene_4_property(self):
        title = Text("性质定理", font=FONT_CN, font_size=36, color=C_LINE_M).move_to(UP * 6.2)
        sub   = Text("线面平行 ⇒ 线线平行", font=FONT_CN, font_size=26,
                     color=C_GRAY).move_to(UP * 5.5)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 平面α
        alpha = Polygon(*self.s4_alpha_verts,
                        color=C_ALPHA, fill_color=C_ALPHA,
                        fill_opacity=0.13, stroke_width=2)
        albl = MathTex(r"\alpha", color=C_ALPHA, font_size=38).move_to(iso(2.5, 1.8, 0))
        self.play(Create(alpha), Write(albl), run_time=0.7)

        # 平面β（绿色，竖直切过）
        beta = Polygon(*self.s4_beta_verts,
                       color=C_BETA, fill_color=C_BETA,
                       fill_opacity=0.18, stroke_width=2)
        blbl = MathTex(r"\beta", color=C_BETA, font_size=38).move_to(iso(-2.2, 0, 1.5))
        self.play(Create(beta), Write(blbl), run_time=0.7)

        # 直线l（在β上，平行于α）
        line_l = Line(self.s4_l_start, self.s4_l_end, color=C_LINE_L, stroke_width=3.5)
        lbl_l  = MathTex("l", color=C_LINE_L, font_size=34).next_to(
            self.s4_l_end, RIGHT, buff=0.1)
        note_l = Text("l ∥ α", font=FONT_CN, font_size=22, color=C_LINE_L).move_to(
            DOWN * 3.2)
        self.play(Create(line_l), Write(lbl_l), FadeIn(note_l), run_time=0.6)

        # 交线m = α∩β
        line_m = Line(self.s4_m_start, self.s4_m_end, color=C_LINE_M, stroke_width=3)
        lbl_m  = MathTex("m", color=C_LINE_M, font_size=34).next_to(
            self.s4_m_end, RIGHT, buff=0.1)
        note_m = Text("m = α ∩ β", font=FONT_CN, font_size=22,
                      color=C_LINE_M).move_to(DOWN * 3.9)
        self.play(Create(line_m), Write(lbl_m), FadeIn(note_m), run_time=0.6)
        self.play(Flash(line_m, color=C_LINE_M), run_time=0.4)

        # 结论
        conc = Text("⇒ l ∥ m", font=FONT_CN, font_size=30, color=WHITE).move_to(DOWN * 4.7)
        self.play(FadeIn(conc, shift=UP*0.2), run_time=0.4)

        formula = MathTex(
            r"l \parallel \alpha,\; l \subset \beta,\; \alpha \cap \beta = m"
            r"\;\Rightarrow\; l \parallel m",
            font_size=24, color=C_GOLD
        ).move_to(DOWN * 5.6)
        self.play(Write(formula), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(alpha), FadeOut(albl),
            FadeOut(beta), FadeOut(blbl),
            FadeOut(line_l), FadeOut(lbl_l), FadeOut(note_l),
            FadeOut(line_m), FadeOut(lbl_m), FadeOut(note_m),
            FadeOut(conc), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    # Scene 5: 总结与口诀
    # ============================================================
    def scene_5_summary(self):
        title = Text("核心口诀", font=FONT_CN, font_size=36, color=C_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        rows = [
            ("判定定理", "面外线 ∥ 面内线 ⇒ 线 ∥ 面", C_COND),
            ("性质定理", "线 ∥ 面，过线的平面与面的交线 ∥ 线", C_LINE_M),
        ]
        y = 4.2
        groups = VGroup()
        for (name, desc, col) in rows:
            box = RoundedRectangle(width=7.5, height=1.5, corner_radius=0.2,
                                   color=col, fill_color=col, fill_opacity=0.08,
                                   stroke_width=1.5)
            box.move_to(np.array([0, y, 0]))
            t1 = Text(name, font=FONT_CN, font_size=26, color=col)
            t2 = Text(desc, font=FONT_CN, font_size=20, color=WHITE)
            inner = VGroup(t1, t2).arrange(DOWN, buff=0.15)
            inner.move_to(box.get_center())
            grp = VGroup(box, inner)
            groups.add(grp)
            self.play(FadeIn(grp, shift=RIGHT*0.3), run_time=0.5)
            y -= 2.2

        tip = Text("记：线线平行 ↔ 线面平行（可互推）",
                   font=FONT_CN, font_size=22, color=C_GRAY).move_to(DOWN * 1.5)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(groups), FadeOut(tip), run_time=0.5)

    # ============================================================
    # Scene 6: 片尾
    # ============================================================
    def scene_6_outro(self):
        big = Text("上海初高中数学直通车", font=FONT_CN, font_size=38, color=WHITE).move_to(UP * 1.5)
        uid = Text("@emptyandcalm", font=FONT_CN, font_size=28, color=C_GRAY).move_to(UP * 0.5)
        flw = Text("关注我，获得更多数学技巧！",
                   font=FONT_CN, font_size=30, color=C_GOLD).move_to(DOWN * 0.5)
        self.play(Transform(self.author, big), run_time=0.6)
        self.play(FadeIn(uid, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(flw, scale=1.05), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(self.author), FadeOut(uid), FadeOut(flw), run_time=0.8)
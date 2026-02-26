"""
平面与平面平行 - Plane-Plane Parallel
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
C_ALPHA   = "#4FC3F7"   # 蓝  平面α
C_BETA    = "#F06292"   # 粉  平面β
C_GAMMA   = "#81C784"   # 绿  平面γ
C_LINE_A  = "#FFD54F"   # 金  直线a
C_LINE_B  = "#CE93D8"   # 紫  直线b
C_LINE_L  = "#FF8A65"   # 橙  直线l
C_GOLD    = "#FFD700"
C_GRAY    = GRAY_B
FONT_CN   = "Noto Sans CJK SC"


def iso(x, y, z, sx=0.80, sy=0.52):
    """等角投影 3D → 2D"""
    px = (x - y) * sx * 0.5
    py = (x + y) * sy * 0.35 + z * sy
    return np.array([px, py, 0])


def plane_quad(cx, cy, z_val, W=4.2, D=2.0, **kwargs):
    """在 z=z_val 处绘制平面四边形"""
    verts = [
        iso(cx - W/2, cy - D/2, z_val),
        iso(cx + W/2, cy - D/2, z_val),
        iso(cx + W/2, cy + D/2, z_val),
        iso(cx - W/2, cy + D/2, z_val),
    ]
    return Polygon(*verts, **kwargs)


class PlanePlaneParallelScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_criterion()
        self.scene_4_property()
        self.scene_5_corollary()
        self.scene_6_summary()
        self.scene_7_outro()

    # ============================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ---- Scene 3: 判定定理 ----
        # 平面α (z=0), 平面β (z=2.2)
        # α内两条相交直线 a, b 都平行于β
        # a 方向: x轴方向 (1,0,0)
        # b 方向: y轴方向 (0,1,0)
        self.s3_a_s = iso(-2.0,  0.5, 0.0)
        self.s3_a_e = iso( 2.0,  0.5, 0.0)
        self.s3_b_s = iso( 0.5, -1.5, 0.0)
        self.s3_b_e = iso( 0.5,  1.5, 0.0)
        self.s3_P   = iso( 0.5,  0.5, 0.0)   # a ∩ b 的交点

        # 验证 a, b 的方向向量不共线
        da_3d = np.array([1, 0, 0])
        db_3d = np.array([0, 1, 0])
        cross = np.cross(da_3d, db_3d)
        self.s3_cross_norm = np.linalg.norm(cross)   # 应 > 0

        # ---- Scene 4: 性质定理 ----
        # α∥β, 第三平面γ同时截 α 和 β
        # α (z=0), β (z=2.0), γ 竖直
        # γ∩α = 直线a_low, γ∩β = 直线a_high
        self.s4_a_low_s  = iso(-2.0, 0, 0.0)
        self.s4_a_low_e  = iso( 2.0, 0, 0.0)
        self.s4_a_high_s = iso(-2.0, 0, 2.0)
        self.s4_a_high_e = iso( 2.0, 0, 2.0)

        # 验证两交线平行（3D方向相同）
        dir_low  = np.array([1, 0, 0])
        dir_high = np.array([1, 0, 0])
        cos_par = np.dot(dir_low, dir_high)
        self.s4_lines_parallel = abs(cos_par - 1.0) < 1e-6

        # ---- Scene 5: 推论 ----
        # 夹在两平行平面间的平行线段相等
        # 线段 AB 和 CD 分别连接 α (z=0) 和 β (z=2.0)
        self.s5_A = iso(-1.5, 0.5, 0.0)
        self.s5_B = iso(-1.5, 0.5, 2.0)
        self.s5_C = iso( 1.5, 0.5, 0.0)
        self.s5_D = iso( 1.5, 0.5, 2.0)

        # 验证 AB = CD（等长）
        AB = np.linalg.norm(self.s5_B - self.s5_A)
        CD = np.linalg.norm(self.s5_D - self.s5_C)
        self.s5_equal_ok = abs(AB - CD) < 1e-6

        # ---- 边界检查 ----
        all_pts = [
            self.s3_a_s, self.s3_a_e, self.s3_b_s, self.s3_b_e, self.s3_P,
            self.s4_a_low_s, self.s4_a_low_e, self.s4_a_high_s, self.s4_a_high_e,
            self.s5_A, self.s5_B, self.s5_C, self.s5_D,
        ]
        for pt in all_pts:
            assert abs(pt[0]) <= 4.5, f"X超界: {pt}"
            assert abs(pt[1]) <= 7.0, f"Y超界: {pt}"

        assert self.s3_cross_norm > 0.5, "a与b方向共线，无法确定平面"
        assert self.s4_lines_parallel, "性质定理交线不平行"
        assert self.s5_equal_ok, "平行线段长度不等"
        print("✓ 几何数据初始化完成")

    # ============================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text("两平面如何判断平行？", font=FONT_CN, font_size=42, color=C_GOLD).move_to(UP * 5.6)
        sub  = Text("一个定义 + 一判定 + 一性质",
                    font=FONT_CN, font_size=26, color=C_GRAY).move_to(UP * 4.8)
        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.4)

    # ============================================================
    def scene_2_definition(self):
        title = Text("定义：面面平行", font=FONT_CN, font_size=36, color=C_ALPHA).move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        alpha = plane_quad(0, 0, 0.0, color=C_ALPHA, fill_color=C_ALPHA,
                           fill_opacity=0.15, stroke_width=2.5)
        beta  = plane_quad(0, 0, 2.0, color=C_BETA,  fill_color=C_BETA,
                           fill_opacity=0.15, stroke_width=2.5)
        la = MathTex(r"\alpha", color=C_ALPHA, font_size=40).move_to(iso(2.5, 1.3, 0.0))
        lb = MathTex(r"\beta",  color=C_BETA,  font_size=40).move_to(iso(2.5, 1.3, 2.0))
        self.play(Create(alpha), Write(la), run_time=0.7)
        self.play(Create(beta),  Write(lb), run_time=0.7)

        # 双向箭头表示"无公共点"
        mid_a = iso(0, -1.3, 0.0)
        mid_b = iso(0, -1.3, 2.0)
        double_arr = DoubleArrow(mid_a, mid_b, color=C_GOLD,
                                 buff=0.1, stroke_width=2)
        dist_lbl = Text("无公共点", font=FONT_CN, font_size=22,
                        color=C_GOLD).next_to(double_arr, RIGHT, buff=0.15)
        self.play(GrowArrow(double_arr), run_time=0.5)
        self.play(FadeIn(dist_lbl), run_time=0.3)

        formula = MathTex(r"\alpha \cap \beta = \emptyset \;\Rightarrow\; \alpha \parallel \beta",
                          font_size=34, color=C_GOLD).move_to(DOWN * 3.5)
        self.play(Write(formula), run_time=0.6)
        self.wait(0.9)

        self.play(
            FadeOut(title), FadeOut(alpha), FadeOut(beta),
            FadeOut(la), FadeOut(lb),
            FadeOut(double_arr), FadeOut(dist_lbl), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    def scene_3_criterion(self):
        title = Text("判定定理", font=FONT_CN, font_size=36, color=C_LINE_A).move_to(UP * 6.1)
        sub   = Text("α 内两相交直线都平行 β  ⇒  α ∥ β",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.4)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 平面 α (下)  β (上)
        alpha = plane_quad(0, 0, 0.0, color=C_ALPHA, fill_color=C_ALPHA,
                           fill_opacity=0.13, stroke_width=2)
        beta  = plane_quad(0, 0, 2.2, color=C_BETA,  fill_color=C_BETA,
                           fill_opacity=0.13, stroke_width=2)
        la = MathTex(r"\alpha", color=C_ALPHA, font_size=38).move_to(iso(2.4, 1.2, 0.0))
        lb = MathTex(r"\beta",  color=C_BETA,  font_size=38).move_to(iso(2.4, 1.2, 2.2))
        self.play(Create(alpha), Write(la), Create(beta), Write(lb), run_time=0.8)

        # 直线 a (在α内, 沿x)
        line_a = Line(self.s3_a_s, self.s3_a_e, color=C_LINE_A, stroke_width=3)
        lbl_a  = MathTex("a", color=C_LINE_A, font_size=32).next_to(self.s3_a_e, RIGHT, buff=0.1)
        # 直线 b (在α内, 沿y)
        line_b = Line(self.s3_b_s, self.s3_b_e, color=C_LINE_B, stroke_width=3)
        lbl_b  = MathTex("b", color=C_LINE_B, font_size=32).next_to(self.s3_b_e, UP, buff=0.1)
        # 交点 P
        dot_P = Dot(self.s3_P, radius=0.10, color=C_GOLD)
        lbl_P = Text("P", font=FONT_CN, font_size=20, color=C_GOLD).next_to(
            self.s3_P, DOWN+RIGHT, buff=0.06)
        self.play(Create(line_a), Write(lbl_a), run_time=0.4)
        self.play(Create(line_b), Write(lbl_b), run_time=0.4)
        self.play(FadeIn(dot_P), Write(lbl_P), run_time=0.3)

        # 条件说明
        cond = VGroup(
            MathTex(r"a \subset \alpha,\; b \subset \alpha,\; a \cap b = P",
                    font_size=24, color=WHITE),
            MathTex(r"a \parallel \beta,\; b \parallel \beta",
                    font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 3.0)
        self.play(FadeIn(cond, shift=UP * 0.2), run_time=0.5)

        conc = MathTex(r"\Rightarrow\; \alpha \parallel \beta",
                       font_size=36, color=C_GOLD).move_to(DOWN * 4.3)
        self.play(Write(conc), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(alpha), FadeOut(beta), FadeOut(la), FadeOut(lb),
            FadeOut(line_a), FadeOut(lbl_a), FadeOut(line_b), FadeOut(lbl_b),
            FadeOut(dot_P), FadeOut(lbl_P), FadeOut(cond), FadeOut(conc),
            run_time=0.5
        )

    # ============================================================
    def scene_4_property(self):
        title = Text("性质定理", font=FONT_CN, font_size=36, color=C_LINE_B).move_to(UP * 6.1)
        sub   = Text("α∥β 同截第三平面 γ  ⇒  交线平行",
                     font=FONT_CN, font_size=22, color=C_GRAY).move_to(UP * 5.4)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        alpha = plane_quad(0, 0, 0.0, color=C_ALPHA, fill_color=C_ALPHA,
                           fill_opacity=0.13, stroke_width=2)
        beta  = plane_quad(0, 0, 2.0, color=C_BETA,  fill_color=C_BETA,
                           fill_opacity=0.13, stroke_width=2)
        la = MathTex(r"\alpha", color=C_ALPHA, font_size=36).move_to(iso(2.4, 1.2, 0.0))
        lb = MathTex(r"\beta",  color=C_BETA,  font_size=36).move_to(iso(2.4, 1.2, 2.0))

        # 平面 γ (竖直截面, 穿过两平面)
        gamma_verts = [
            iso(-2.5, 0, -0.3), iso(2.5, 0, -0.3),
            iso(2.5, 0, 2.4),   iso(-2.5, 0, 2.4),
        ]
        gamma = Polygon(*gamma_verts, color=C_GAMMA, fill_color=C_GAMMA,
                        fill_opacity=0.14, stroke_width=2)
        lg = MathTex(r"\gamma", color=C_GAMMA, font_size=36).move_to(iso(-2.2, 0, 2.2))

        self.play(Create(alpha), Write(la), Create(beta), Write(lb), run_time=0.7)
        self.play(Create(gamma), Write(lg), run_time=0.7)

        # 交线 a = α∩γ (下), b = β∩γ (上)
        line_a = Line(self.s4_a_low_s,  self.s4_a_low_e,
                      color=C_LINE_A, stroke_width=3.5)
        lbl_a  = MathTex("a", color=C_LINE_A, font_size=30).next_to(
            self.s4_a_low_e, RIGHT, buff=0.1)
        line_b = Line(self.s4_a_high_s, self.s4_a_high_e,
                      color=C_LINE_B, stroke_width=3.5)
        lbl_b  = MathTex("b", color=C_LINE_B, font_size=30).next_to(
            self.s4_a_high_e, RIGHT, buff=0.1)

        self.play(Create(line_a), Write(lbl_a), run_time=0.5)
        self.play(Create(line_b), Write(lbl_b), run_time=0.5)
        self.play(
            Flash(line_a, color=C_LINE_A, flash_radius=0.3),
            Flash(line_b, color=C_LINE_B, flash_radius=0.3),
            run_time=0.5
        )

        conc = Text("a ∥ b（两交线平行）", font=FONT_CN, font_size=26,
                    color=WHITE).move_to(DOWN * 3.2)
        formula = MathTex(
            r"\alpha \parallel \beta,\; \alpha \cap \gamma = a,\; \beta \cap \gamma = b"
            r"\;\Rightarrow\; a \parallel b",
            font_size=24, color=C_GOLD
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(conc, shift=UP*0.2), run_time=0.4)
        self.play(Write(formula), run_time=0.7)
        self.wait(1.3)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(alpha), FadeOut(beta), FadeOut(gamma),
            FadeOut(la), FadeOut(lb), FadeOut(lg),
            FadeOut(line_a), FadeOut(lbl_a), FadeOut(line_b), FadeOut(lbl_b),
            FadeOut(conc), FadeOut(formula),
            run_time=0.5
        )

    # ============================================================
    def scene_5_corollary(self):
        title = Text("推论：夹在两平行平面间的", font=FONT_CN,
                     font_size=28, color=C_GOLD).move_to(UP * 6.0)
        title2 = Text("平行线段相等", font=FONT_CN, font_size=32,
                      color=C_GOLD).move_to(UP * 5.3)
        self.play(Write(title), Write(title2), run_time=0.6)

        alpha = plane_quad(0, 0, 0.0, W=5.0, D=2.2,
                           color=C_ALPHA, fill_color=C_ALPHA,
                           fill_opacity=0.13, stroke_width=2)
        beta  = plane_quad(0, 0, 2.0, W=5.0, D=2.2,
                           color=C_BETA,  fill_color=C_BETA,
                           fill_opacity=0.13, stroke_width=2)
        la = MathTex(r"\alpha", color=C_ALPHA, font_size=36).move_to(iso(2.9, 1.4, 0.0))
        lb = MathTex(r"\beta",  color=C_BETA,  font_size=36).move_to(iso(2.9, 1.4, 2.0))
        self.play(Create(alpha), Write(la), Create(beta), Write(lb), run_time=0.7)

        # 线段 AB
        seg_AB = Line(self.s5_A, self.s5_B, color=C_LINE_A, stroke_width=3.5)
        dA = Dot(self.s5_A, radius=0.09, color=C_LINE_A)
        dB = Dot(self.s5_B, radius=0.09, color=C_LINE_A)
        lA = Text("A", font=FONT_CN, font_size=20, color=C_LINE_A).next_to(
            self.s5_A, DOWN+LEFT, buff=0.06)
        lB = Text("B", font=FONT_CN, font_size=20, color=C_LINE_A).next_to(
            self.s5_B, UP+LEFT, buff=0.06)

        # 线段 CD
        seg_CD = Line(self.s5_C, self.s5_D, color=C_LINE_B, stroke_width=3.5)
        dC = Dot(self.s5_C, radius=0.09, color=C_LINE_B)
        dD = Dot(self.s5_D, radius=0.09, color=C_LINE_B)
        lC = Text("C", font=FONT_CN, font_size=20, color=C_LINE_B).next_to(
            self.s5_C, DOWN+RIGHT, buff=0.06)
        lD = Text("D", font=FONT_CN, font_size=20, color=C_LINE_B).next_to(
            self.s5_D, UP+RIGHT, buff=0.06)

        self.play(
            Create(seg_AB), FadeIn(dA), FadeIn(dB), Write(lA), Write(lB),
            run_time=0.5
        )
        self.play(
            Create(seg_CD), FadeIn(dC), FadeIn(dD), Write(lC), Write(lD),
            run_time=0.5
        )

        equal_lbl = MathTex(r"AB = CD", color=C_GOLD, font_size=40).move_to(DOWN * 3.2)
        cond_lbl  = Text("（AB ∥ CD 且均夹在 α∥β 间）",
                         font=FONT_CN, font_size=20, color=C_GRAY).move_to(DOWN * 3.9)
        self.play(Write(equal_lbl), run_time=0.5)
        self.play(FadeIn(cond_lbl), run_time=0.3)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(title2),
            FadeOut(alpha), FadeOut(beta), FadeOut(la), FadeOut(lb),
            FadeOut(seg_AB), FadeOut(dA), FadeOut(dB), FadeOut(lA), FadeOut(lB),
            FadeOut(seg_CD), FadeOut(dC), FadeOut(dD), FadeOut(lC), FadeOut(lD),
            FadeOut(equal_lbl), FadeOut(cond_lbl),
            run_time=0.5
        )

    # ============================================================
    def scene_6_summary(self):
        title = Text("核心总结", font=FONT_CN, font_size=36, color=C_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        items = [
            ("定义",   r"\alpha \cap \beta = \emptyset \Rightarrow \alpha \parallel \beta",   C_ALPHA),
            ("判定",   r"a \parallel \beta,\; b \parallel \beta \Rightarrow \alpha \parallel \beta", C_LINE_A),
            ("性质",   r"\alpha \parallel \beta \Rightarrow a \parallel b",                   C_LINE_B),
            ("推论",   r"AB \parallel CD \Rightarrow AB = CD",                                C_GOLD),
        ]
        y = 4.3
        groups = VGroup()
        for (name, fml, col) in items:
            box = RoundedRectangle(width=7.6, height=1.3, corner_radius=0.2,
                                   color=col, fill_color=col, fill_opacity=0.07,
                                   stroke_width=1.5).move_to(np.array([0, y, 0]))
            t1 = Text(name, font=FONT_CN, font_size=24, color=col)
            t2 = MathTex(fml, font_size=22, color=WHITE)
            VGroup(t1, t2).arrange(RIGHT, buff=0.3).move_to(box.get_center())
            grp = VGroup(box, t1, t2)
            groups.add(grp)
            self.play(FadeIn(grp, shift=RIGHT*0.3), run_time=0.4)
            y -= 1.8

        tip = Text("口诀：两交线平行→面面平行；面面平行→两截线平行",
                   font=FONT_CN, font_size=18, color=C_GRAY).move_to(DOWN * 1.2)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(groups), FadeOut(tip), run_time=0.5)

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
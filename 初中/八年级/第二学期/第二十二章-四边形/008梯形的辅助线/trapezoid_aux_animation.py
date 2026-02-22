"""
trapezoid_aux_animation.py - 梯形的辅助线 教学动画
八年级第二学期 第二十二章 四边形

5种辅助线方法:
  ① 作高       → 构造直角三角形/矩形
  ② 平移一腰   → 构造平行四边形+三角形
  ③ 延长两腰   → 构造相似三角形
  ④ 连接对角线 → 构造等积三角形
  ⑤ 作中位线   → 中位线定理

格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局视频配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色常量 =====
BG_COLOR    = "#1a1a2e"
COLOR_TRAP  = "#4FC3F7"   # 主梯形轮廓
COLOR_M1    = "#FF7043"   # 方法1 作高
COLOR_M2    = "#69F0AE"   # 方法2 平移腰
COLOR_M3    = "#CE93D8"   # 方法3 延长腰
COLOR_M4    = "#FFD700"   # 方法4 对角线
COLOR_M5    = "#42A5F5"   # 方法5 中位线
COLOR_FILL1 = "#FF703430" # 方法1填充(透明)
COLOR_AUX   = GRAY_B
COLOR_HL    = YELLOW
FONT        = "Noto Sans CJK SC"

# ===== 几何工具 =====
def perp_foot(point, ls, le):
    """点到直线段的垂足"""
    lv = le - ls
    t  = np.dot(point - ls, lv) / np.dot(lv, lv)
    return ls + t * lv


def right_angle_sq(corner, P1, P2, size=0.16, color=WHITE):
    """直角正方形标记"""
    v1 = (P1 - corner); v1 = v1 / np.linalg.norm(v1) * size
    v2 = (P2 - corner); v2 = v2 / np.linalg.norm(v2) * size
    return Polygon(
        corner, corner+v1, corner+v1+v2, corner+v2,
        color=color, stroke_width=2, fill_opacity=0
    )


def tick_mark(P1, P2, n=1, size=0.12, color=WHITE):
    """线段等长标记"""
    mid = (P1 + P2) / 2
    d   = P2 - P1; d_u = d / np.linalg.norm(d)
    perp = np.array([-d_u[1], d_u[0], 0])
    grp  = VGroup()
    sp   = 0.09
    for i in range(n):
        off = (i - (n-1)/2) * sp
        grp.add(Line(mid + off*d_u + perp*size,
                     mid + off*d_u - perp*size,
                     color=color, stroke_width=2.5))
    return grp


def parallel_arrows(P1, P2, color=WHITE, size=0.18, buff=0.35):
    """平行线标记(小箭头)"""
    mid = (P1 + P2) / 2
    d   = P2 - P1; d_u = d / np.linalg.norm(d)
    return VGroup(
        Arrow(mid - d_u*size, mid + d_u*size,
              buff=0, tip_length=0.1,
              max_tip_length_to_length_ratio=0.8,
              color=color, stroke_width=2)
    )


def method_title_card(num: str, text: str, color):
    """方法标题卡片"""
    bg = RoundedRectangle(
        width=7.8, height=0.9, corner_radius=0.18,
        fill_color=color, fill_opacity=0.25,
        stroke_color=color, stroke_width=2
    )
    label = Text(f"方法{num}  {text}", font=FONT,
                 font_size=28, color=color)
    label.move_to(bg.get_center())
    return VGroup(bg, label)


def insight_card(text: str, color=WHITE):
    """底部说明卡片"""
    bg = RoundedRectangle(
        width=7.6, height=0.85, corner_radius=0.15,
        fill_color="#0d0d20", fill_opacity=0.96,
        stroke_color=color, stroke_width=1.5
    )
    t = Text(text, font=FONT, font_size=22, color=color)
    t.move_to(bg.get_center())
    return VGroup(bg, t)


class TrapezoidAuxLines(Scene):
    """
    梯形的辅助线 — 5种经典方法教学动画
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_method1_altitude()
        self.scene_3_method2_translate_leg()
        self.scene_4_method3_extend_legs()
        self.scene_5_method4_diagonals()
        self.scene_6_method5_midsegment()
        self.scene_7_summary()
        self.scene_8_outro()

    # =========================================================
    # 几何初始化
    # =========================================================
    def setup_geometry(self):
        """所有坐标统一计算，从不猜测"""
        SCALE  = 0.95
        OFF_Y  = 0.3

        def to_pt(rx, ry):
            return np.array([rx * SCALE, ry * SCALE + OFF_Y, 0])

        # 基础梯形顶点 (A=左上, B=右上, C=右下, D=左下)
        self.A = to_pt(-1.0,  1.0)   # 上底左端
        self.B = to_pt( 1.0,  1.0)   # 上底右端
        self.C = to_pt( 2.5, -1.2)   # 下底右端
        self.D = to_pt(-2.5, -1.2)   # 下底左端

        # ── 方法1: 作高 ──
        self.foot_A = perp_foot(self.A, self.D, self.C)  # A在DC上的垂足
        self.foot_B = perp_foot(self.B, self.D, self.C)  # B在DC上的垂足

        # ── 方法2: 平移一腰 (BE ∥ AD, E在DC上) ──
        self.E = self.B + (self.D - self.A)   # E = B + vector(AD)

        # ── 方法3: 延长两腰交点P ──
        # 由A沿(A-D)方向延长；由B沿(B-C)方向延长
        # 解: A + t*(A-D) = B + s*(B-C)
        dAD = self.A - self.D        # 从D到A方向(向上延长)
        dBC = self.B - self.C        # 从C到B方向(向上延长)
        mat = np.array([[dAD[0], -dBC[0]], [dAD[1], -dBC[1]]])
        rhs = np.array([self.B[0]-self.A[0], self.B[1]-self.A[1]])
        ts  = np.linalg.solve(mat, rhs)
        self.P = self.A + ts[0] * dAD

        # ── 方法4: 对角线交点O ──
        # AC: A + t*(C-A); BD: B + s*(D-B)
        dAC = self.C - self.A; dBD = self.D - self.B
        mat2 = np.array([[dAC[0], -dBD[0]], [dAC[1], -dBD[1]]])
        rhs2 = np.array([self.B[0]-self.A[0], self.B[1]-self.A[1]])
        ts2  = np.linalg.solve(mat2, rhs2)
        self.O = self.A + ts2[0] * dAC

        # ── 方法5: 中位线端点 ──
        self.M = (self.A + self.D) / 2   # AD中点
        self.N = (self.B + self.C) / 2   # BC中点

        # 边长缓存
        self.AB_len = np.linalg.norm(self.B - self.A)
        self.DC_len = np.linalg.norm(self.C - self.D)
        self.h_len  = abs(self.A[1] - self.D[1])

        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-6
        # AB ∥ DC
        ab = (self.B-self.A)[:2]; dc = (self.C-self.D)[:2]
        assert abs(np.dot(ab/np.linalg.norm(ab), dc/np.linalg.norm(dc))-1) < eps
        # foot_A ⊥ DC
        assert abs(np.dot((self.A-self.foot_A)[:2], (self.C-self.D)[:2])) < eps
        # ABDE 平行四边形
        assert np.linalg.norm((self.B-self.A)-(self.E-self.D)) < eps
        # O在AC上
        AO = (self.O-self.A)[:2]; AC = (self.C-self.A)[:2]
        assert abs(AO[0]*AC[1]-AO[1]*AC[0]) < eps
        # MN = (AB+DC)/2
        mn = np.linalg.norm(self.N-self.M)
        assert abs(mn - (self.AB_len+self.DC_len)/2) < eps
        print("✓ 所有几何验证通过")

    # =========================================================
    # 辅助: 构建梯形 Polygon
    # =========================================================
    def make_trapezoid(self, color=COLOR_TRAP, stroke_width=3, fill_opacity=0):
        return Polygon(self.A, self.B, self.C, self.D,
                       color=color, stroke_width=stroke_width,
                       fill_opacity=fill_opacity)

    def make_labels(self, scale=1.0):
        sz = int(20 * scale)
        lA = Text("A", font=FONT, font_size=sz).next_to(self.A, UL, buff=0.08)
        lB = Text("B", font=FONT, font_size=sz).next_to(self.B, UR, buff=0.08)
        lC = Text("C", font=FONT, font_size=sz).next_to(self.C, DR, buff=0.08)
        lD = Text("D", font=FONT, font_size=sz).next_to(self.D, DL, buff=0.08)
        return VGroup(lA, lB, lC, lD)

    # =========================================================
    # Scene 1: 开场钩子
    # =========================================================
    def scene_1_opening(self):
        # 作者信息 (顶部固定)
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN*0.15), run_time=0.3)

        # 钩子问题
        hook = Text("梯形难题怎么破？", font=FONT,
                    font_size=42, color=COLOR_HL)
        hook.move_to(UP * 5.8)
        sub  = Text("5种辅助线全掌握！", font=FONT,
                    font_size=30, color=GRAY_A)
        sub.move_to(UP * 4.9)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub, shift=UP*0.2), run_time=0.4)

        # 主梯形出现
        trap = self.make_trapezoid()
        lbls = self.make_labels()
        self.play(Create(trap), run_time=1.0)
        self.play(FadeIn(lbls), run_time=0.4)

        # 上底/下底标注
        lab_a = Text("a (上底)", font=FONT, font_size=20, color=COLOR_TRAP)
        lab_a.move_to((self.A+self.B)/2 + UP*0.3)
        lab_b = Text("b (下底)", font=FONT, font_size=20, color=COLOR_TRAP)
        lab_b.move_to((self.D+self.C)/2 + DOWN*0.32)
        self.play(FadeIn(lab_a), FadeIn(lab_b), run_time=0.5)
        self.wait(1.0)

        # 清理，保留 trap+lbls 供下一场景衔接
        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(lab_a), FadeOut(lab_b),
            run_time=0.4
        )
        self.trap_persistent = trap
        self.lbls_persistent = lbls

    # =========================================================
    # Scene 2: 方法① 作高
    # =========================================================
    def scene_2_method1_altitude(self):
        trap = self.trap_persistent
        lbls = self.lbls_persistent

        # 标题卡
        card = method_title_card("①", "作高", COLOR_M1)
        card.move_to(UP * 4.7)
        self.play(FadeIn(card, shift=DOWN*0.2), run_time=0.5)

        # ── 步骤1: 从A作垂线到DC ──
        alt_A = DashedLine(self.A, self.foot_A,
                           color=COLOR_M1, dash_length=0.12, stroke_width=3)
        ra_A  = right_angle_sq(self.foot_A, self.A, self.D,
                                size=0.18, color=COLOR_M1)
        dot_E1 = Dot(self.foot_A, color=COLOR_M1, radius=0.07)
        lbl_E1 = Text("E", font=FONT, font_size=18,
                      color=COLOR_M1).next_to(self.foot_A, DOWN, buff=0.12)

        self.play(Create(alt_A), run_time=0.7)
        self.play(FadeIn(ra_A), FadeIn(dot_E1), FadeIn(lbl_E1), run_time=0.4)

        # ── 步骤2: 从B作垂线到DC ──
        alt_B = DashedLine(self.B, self.foot_B,
                           color=COLOR_M1, dash_length=0.12, stroke_width=3)
        ra_B  = right_angle_sq(self.foot_B, self.B, self.C,
                                size=0.18, color=COLOR_M1)
        dot_F  = Dot(self.foot_B, color=COLOR_M1, radius=0.07)
        lbl_F  = Text("F", font=FONT, font_size=18,
                      color=COLOR_M1).next_to(self.foot_B, DOWN, buff=0.12)

        self.play(Create(alt_B), run_time=0.7)
        self.play(FadeIn(ra_B), FadeIn(dot_F), FadeIn(lbl_F), run_time=0.4)

        # ── 步骤3: 高的 Brace 标注 ──
        h_line = Line(self.A, self.foot_A)
        brace  = Brace(h_line, direction=RIGHT, buff=0.05, color=COLOR_M1)
        lbl_h  = Text("h", font=FONT, font_size=22,
                      color=COLOR_M1).next_to(brace, RIGHT, buff=0.08)
        self.play(FadeIn(brace), FadeIn(lbl_h), run_time=0.4)

        # ── 步骤4: 矩形高亮填充 ──
        rect_poly = Polygon(
            self.A, self.B, self.foot_B, self.foot_A,
            fill_color=COLOR_M1, fill_opacity=0.18,
            stroke_width=0
        )
        self.play(FadeIn(rect_poly), run_time=0.5)

        # ── 步骤5: 两个直角三角形填充 ──
        tri_left  = Polygon(self.D, self.foot_A, self.A,
                            fill_color="#FF3000", fill_opacity=0.22, stroke_width=0)
        tri_right = Polygon(self.foot_B, self.C, self.B,
                            fill_color="#FF3000", fill_opacity=0.22, stroke_width=0)
        self.play(FadeIn(tri_left), FadeIn(tri_right), run_time=0.6)

        # ── 说明 ──
        ins = insight_card("化梯形 = 矩形 + 2个直角三角形", COLOR_M1)
        ins.move_to(DOWN * 3.8)
        self.play(FadeIn(ins, shift=UP*0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(card), FadeOut(alt_A), FadeOut(alt_B),
            FadeOut(ra_A), FadeOut(ra_B),
            FadeOut(dot_E1), FadeOut(lbl_E1),
            FadeOut(dot_F),  FadeOut(lbl_F),
            FadeOut(brace),  FadeOut(lbl_h),
            FadeOut(rect_poly), FadeOut(tri_left), FadeOut(tri_right),
            FadeOut(ins),
            run_time=0.5
        )

    # =========================================================
    # Scene 3: 方法② 平移一腰
    # =========================================================
    def scene_3_method2_translate_leg(self):
        trap = self.trap_persistent
        lbls = self.lbls_persistent

        card = method_title_card("②", "平移一腰", COLOR_M2)
        card.move_to(UP * 4.7)
        self.play(FadeIn(card, shift=DOWN*0.2), run_time=0.5)

        # ── 步骤1: 辅助线 BE (BE ∥ AD) ──
        aux_BE = DashedLine(self.B, self.E,
                            color=COLOR_M2, dash_length=0.12, stroke_width=3)
        dot_E  = Dot(self.E, color=COLOR_M2, radius=0.08)
        lbl_E  = Text("E", font=FONT, font_size=20,
                      color=COLOR_M2).next_to(self.E, DOWN, buff=0.14)

        explain1 = insight_card("过B作BE∥AD，交DC于E", COLOR_M2)
        explain1.move_to(DOWN * 3.8)

        self.play(Create(aux_BE), run_time=0.9)
        self.play(FadeIn(dot_E), FadeIn(lbl_E), run_time=0.3)
        self.play(FadeIn(explain1, shift=UP*0.15), run_time=0.4)
        self.wait(0.6)

        # ── 步骤2: 平行四边形 ABED 高亮 ──
        # 顺序: A → B → E → D
        para_poly = Polygon(
            self.A, self.B, self.E, self.D,
            fill_color=COLOR_M2, fill_opacity=0.20,
            stroke_color=COLOR_M2, stroke_width=2
        )
        # BE = AD 等长标记
        tk_AD = tick_mark(self.A, self.D, n=1, size=0.13, color=COLOR_M2)
        tk_BE = tick_mark(self.B, self.E, n=1, size=0.13, color=COLOR_M2)

        self.play(FadeIn(para_poly), run_time=0.6)
        self.play(FadeIn(tk_AD), FadeIn(tk_BE), run_time=0.4)

        lbl_para = Text("平行四边形 ABED", font=FONT,
                        font_size=20, color=COLOR_M2)
        lbl_para.move_to(UP * 0.2)
        self.play(FadeIn(lbl_para), run_time=0.4)
        self.wait(0.5)

        # ── 步骤3: 三角形 BCE 高亮 ──
        self.play(FadeOut(explain1), run_time=0.3)

        tri_BCE = Polygon(
            self.B, self.C, self.E,
            fill_color="#FF8C00", fill_opacity=0.30,
            stroke_color="#FF8C00", stroke_width=2
        )
        lbl_tri = Text("△BCE", font=FONT, font_size=20,
                       color="#FF8C00")
        lbl_tri.move_to((self.B+self.C+self.E)/3 + RIGHT*0.3)

        self.play(FadeIn(tri_BCE), FadeIn(lbl_tri), run_time=0.6)

        # EC = b - a 标注
        ec_label = Text("EC = b - a", font=FONT,
                        font_size=20, color=COLOR_HL)
        ec_label.move_to((self.E+self.C)/2 + DOWN*0.32)
        self.play(FadeIn(ec_label), run_time=0.4)

        ins2 = insight_card("梯形 = 平行四边形 ABED + △BCE", COLOR_M2)
        ins2.move_to(DOWN * 3.8)
        self.play(FadeIn(ins2, shift=UP*0.15), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(card), FadeOut(aux_BE),
            FadeOut(dot_E), FadeOut(lbl_E),
            FadeOut(para_poly), FadeOut(tk_AD), FadeOut(tk_BE),
            FadeOut(lbl_para), FadeOut(tri_BCE), FadeOut(lbl_tri),
            FadeOut(ec_label), FadeOut(ins2),
            run_time=0.5
        )

    # =========================================================
    # Scene 4: 方法③ 延长两腰
    # =========================================================
    def scene_4_method3_extend_legs(self):
        card = method_title_card("③", "延长两腰", COLOR_M3)
        card.move_to(UP * 4.7)
        self.play(FadeIn(card, shift=DOWN*0.2), run_time=0.5)

        ext_left = DashedLine(self.A, self.P, color=COLOR_M3, dash_length=0.12, stroke_width=2.5)
        self.play(Create(ext_left), run_time=0.7)

        ext_right = DashedLine(self.B, self.P, color=COLOR_M3, dash_length=0.12, stroke_width=2.5)
        self.play(Create(ext_right), run_time=0.7)

        dot_P = Dot(self.P, color=COLOR_M3, radius=0.10)
        lbl_P = Text("P", font=FONT, font_size=22, color=COLOR_M3).next_to(self.P, UP, buff=0.12)
        self.play(FadeIn(dot_P, scale=0.3), run_time=0.4)
        self.play(Flash(dot_P, color=COLOR_M3, flash_radius=0.25), run_time=0.4)
        self.play(FadeIn(lbl_P), run_time=0.3)

        tri_PAB = Polygon(self.P, self.A, self.B,
                          fill_color=COLOR_M3, fill_opacity=0.22, stroke_color=COLOR_M3, stroke_width=2)
        lbl_PAB = Text("△PAB", font=FONT, font_size=19, color=COLOR_M3)
        lbl_PAB.move_to((self.P + self.A + self.B)/3)
        self.play(FadeIn(tri_PAB), FadeIn(lbl_PAB), run_time=0.5)
        self.wait(0.5)

        tri_PDC = Polygon(self.P, self.D, self.C,
                          fill_color="#7B1FA2", fill_opacity=0.20, stroke_color="#E040FB", stroke_width=2)
        lbl_PDC = Text("△PDC", font=FONT, font_size=19, color="#E040FB")
        lbl_PDC.move_to((self.P + self.D + self.C)/3 + DOWN*0.2)
        self.play(FadeIn(tri_PDC), FadeIn(lbl_PDC), run_time=0.5)
        self.wait(0.4)

        sim_text = Text("△PAB  ∽  △PDC", font=FONT, font_size=26, color=COLOR_HL)
        sim_text.move_to(DOWN * 2.8)
        self.play(Write(sim_text), run_time=0.6)

        sim_ratio = MathTex(r"\frac{PA}{PD} = \frac{PB}{PC} = \frac{AB}{DC}", font_size=32, color=COLOR_M3)
        sim_ratio.move_to(DOWN * 3.8)
        self.play(Write(sim_ratio), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(card), FadeOut(ext_left), FadeOut(ext_right),
            FadeOut(dot_P), FadeOut(lbl_P),
            FadeOut(tri_PAB), FadeOut(lbl_PAB),
            FadeOut(tri_PDC), FadeOut(lbl_PDC),
            FadeOut(sim_text), FadeOut(sim_ratio),
            run_time=0.5
        )

    # =========================================================
    # Scene 5: 方法④ 连接对角线
    # =========================================================
    def scene_5_method4_diagonals(self):
        card = method_title_card("④", "连对角线", COLOR_M4)
        card.move_to(UP * 4.7)
        self.play(FadeIn(card, shift=DOWN*0.2), run_time=0.5)

        diag_AC = Line(self.A, self.C, color=COLOR_M4, stroke_width=2.5)
        self.play(Create(diag_AC), run_time=0.7)
        diag_BD = Line(self.B, self.D, color=COLOR_M4, stroke_width=2.5)
        self.play(Create(diag_BD), run_time=0.7)

        dot_O = Dot(self.O, color=COLOR_M4, radius=0.09)
        lbl_O = Text("O", font=FONT, font_size=20, color=COLOR_M4).next_to(self.O, RIGHT, buff=0.12)
        self.play(FadeIn(dot_O, scale=0.3), run_time=0.3)
        self.play(Flash(dot_O, color=COLOR_M4, flash_radius=0.22), run_time=0.4)
        self.play(FadeIn(lbl_O), run_time=0.3)

        tri_AOD = Polygon(self.A, self.O, self.D,
                          fill_color="#FF6F00", fill_opacity=0.30, stroke_color="#FF6F00", stroke_width=2)
        lbl_AOD = Text("△AOD", font=FONT, font_size=17, color="#FF6F00")
        lbl_AOD.move_to((self.A+self.O+self.D)/3 + LEFT*0.1)
        self.play(FadeIn(tri_AOD), FadeIn(lbl_AOD), run_time=0.5)
        self.wait(0.4)

        tri_BOC = Polygon(self.B, self.O, self.C,
                          fill_color="#1565C0", fill_opacity=0.30, stroke_color="#42A5F5", stroke_width=2)
        lbl_BOC = Text("△BOC", font=FONT, font_size=17, color="#42A5F5")
        lbl_BOC.move_to((self.B+self.O+self.C)/3 + RIGHT*0.1)
        self.play(FadeIn(tri_BOC), FadeIn(lbl_BOC), run_time=0.5)
        self.wait(0.3)

        eq_text = Text("面积相等！", font=FONT, font_size=28, color=COLOR_HL)
        eq_text.move_to(DOWN * 2.8)
        self.play(Write(eq_text), run_time=0.5)

        eq_formula = MathTex(r"S_{\triangle AOD} = S_{\triangle BOC}", font_size=36, color=COLOR_M4)
        eq_formula.move_to(DOWN * 3.7)
        self.play(Write(eq_formula), run_time=0.6)

        reason = insight_card("因为 S△ABC = S△ABD  (同底AB，等高h)", GRAY_A)
        reason.move_to(DOWN * 4.9)
        self.play(FadeIn(reason), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(card), FadeOut(diag_AC), FadeOut(diag_BD),
            FadeOut(dot_O), FadeOut(lbl_O),
            FadeOut(tri_AOD), FadeOut(lbl_AOD),
            FadeOut(tri_BOC), FadeOut(lbl_BOC),
            FadeOut(eq_text), FadeOut(eq_formula), FadeOut(reason),
            run_time=0.5
        )

    # =========================================================
    # Scene 6: 方法⑤ 作中位线
    # =========================================================
    def scene_6_method5_midsegment(self):
        card = method_title_card("⑤", "作中位线", COLOR_M5)
        card.move_to(UP * 4.7)
        self.play(FadeIn(card, shift=DOWN*0.2), run_time=0.5)

        dot_M  = Dot(self.M, color=COLOR_M5, radius=0.09)
        lbl_M  = Text("M", font=FONT, font_size=20, color=COLOR_M5).next_to(self.M, LEFT, buff=0.12)
        tick_L  = tick_mark(self.A, self.M, n=1, size=0.13, color=COLOR_M5)
        tick_L2 = tick_mark(self.M, self.D, n=1, size=0.13, color=COLOR_M5)
        self.play(FadeIn(dot_M, scale=0.4), FadeIn(lbl_M), run_time=0.4)
        self.play(FadeIn(tick_L), FadeIn(tick_L2), run_time=0.3)

        dot_N  = Dot(self.N, color=COLOR_M5, radius=0.09)
        lbl_N  = Text("N", font=FONT, font_size=20, color=COLOR_M5).next_to(self.N, RIGHT, buff=0.12)
        tick_R  = tick_mark(self.B, self.N, n=1, size=0.13, color=COLOR_M5)
        tick_R2 = tick_mark(self.N, self.C, n=1, size=0.13, color=COLOR_M5)
        self.play(FadeIn(dot_N, scale=0.4), FadeIn(lbl_N), run_time=0.4)
        self.play(FadeIn(tick_R), FadeIn(tick_R2), run_time=0.3)

        mid_line = Line(self.M, self.N, color=COLOR_M5, stroke_width=4)
        self.play(Create(mid_line), run_time=0.8)

        brace_mn = Brace(mid_line, direction=UP, buff=0.05, color=COLOR_M5)
        lbl_mn   = Text("MN", font=FONT, font_size=20, color=COLOR_M5).next_to(brace_mn, UP, buff=0.05)
        self.play(FadeIn(brace_mn), FadeIn(lbl_mn), run_time=0.4)

        formula = MathTex(r"MN = \frac{a + b}{2}", font_size=40, color=COLOR_M5)
        formula.move_to(DOWN * 2.8)
        self.play(Write(formula), run_time=0.7)

        ins = insight_card("MN ∥ AB ∥ DC，MN = (上底+下底) ÷ 2", COLOR_M5)
        ins.move_to(DOWN * 4.0)
        self.play(FadeIn(ins), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(card),
            FadeOut(dot_M), FadeOut(lbl_M), FadeOut(tick_L), FadeOut(tick_L2),
            FadeOut(dot_N), FadeOut(lbl_N), FadeOut(tick_R), FadeOut(tick_R2),
            FadeOut(mid_line), FadeOut(brace_mn), FadeOut(lbl_mn),
            FadeOut(formula), FadeOut(ins),
            run_time=0.5
        )

    # =========================================================
    # Scene 7: 5种方法汇总
    # =========================================================
    def scene_7_summary(self):
        trap_small = self.make_trapezoid(stroke_width=2).scale(0.5).move_to(UP * 5.3)
        self.play(
            Transform(self.trap_persistent, trap_small),
            FadeOut(self.lbls_persistent),
            run_time=0.7
        )

        title = Text("5种辅助线 · 速记", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 4.4)
        self.play(Write(title), run_time=0.5)

        methods = [
            ("①", "作高",     "→ 矩形 + 直角三角形",  COLOR_M1),
            ("②", "平移一腰", "→ 平行四边形 + 三角形", COLOR_M2),
            ("③", "延长两腰", "→ 相似三角形",          COLOR_M3),
            ("④", "连对角线", "→ 等积三角形",          COLOR_M4),
            ("⑤", "作中位线", "→ MN = (a+b) ÷ 2",    COLOR_M5),
        ]

        cards_group = VGroup()
        for num, name, result, col in methods:
            bg = RoundedRectangle(
                width=7.4, height=0.82, corner_radius=0.16,
                fill_color=col, fill_opacity=0.18,
                stroke_color=col, stroke_width=1.8
            )
            n_txt = Text(f"方法{num}", font=FONT, font_size=20, color=col)
            m_txt = Text(name,   font=FONT, font_size=22, color=WHITE)
            r_txt = Text(result, font=FONT, font_size=17, color=GRAY_A)
            content = VGroup(n_txt, m_txt, r_txt).arrange(RIGHT, buff=0.35)
            content.move_to(bg.get_center())
            cards_group.add(VGroup(bg, content))

        cards_group.arrange(DOWN, buff=0.18)
        cards_group.move_to(DOWN * 0.5)

        for card in cards_group:
            self.play(FadeIn(card, shift=RIGHT*0.3), run_time=0.35)

        slogan = Text("掌握辅助线 = 化难为易！", font=FONT, font_size=28, color=COLOR_HL)
        slogan.move_to(DOWN * 3.6)
        self.play(FadeIn(slogan, scale=1.05), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(cards_group), FadeOut(slogan),
            FadeOut(self.trap_persistent),
            run_time=0.6
        )

    # =========================================================
    # Scene 8: 片尾
    # =========================================================
    def scene_8_outro(self):
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=38, color=WHITE).move_to(UP * 2.0)
        author_id  = Text("@emptyandcalm", font=FONT, font_size=28, color=GRAY_B).move_to(UP * 1.1)
        follow     = Text("关注我，获得更多数学技巧!", font=FONT, font_size=30, color=COLOR_HL).move_to(DOWN * 0.2)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)

        colors = [COLOR_M1, COLOR_M2, COLOR_M3, COLOR_M4, COLOR_M5]
        decos = VGroup()
        for i, col in enumerate(colors):
            ang = i * 2*PI/5
            pos = 2.8*np.array([np.cos(ang), np.sin(ang - PI/2), 0]) + DOWN*2.5
            mini = Polygon(
                np.array([-0.28,  0.18, 0]),
                np.array([ 0.28,  0.18, 0]),
                np.array([ 0.45, -0.18, 0]),
                np.array([-0.45, -0.18, 0]),
                fill_color=col, fill_opacity=0.85, stroke_width=0
            ).move_to(pos)
            decos.add(mini)

        self.play(*[FadeIn(d, scale=0.4) for d in decos], run_time=0.6)
        self.play(Rotate(decos, angle=2*PI/5, about_point=DOWN*2.5, run_time=1.2))
        self.wait(1.0)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(decos),
            run_time=1.0
        )


# manim -pql trapezoid_aux_animation.py TrapezoidAuxLines  # 快速预览
# manim -qh  trapezoid_aux_animation.py TrapezoidAuxLines  # 高质量
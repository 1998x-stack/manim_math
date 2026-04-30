"""
trapezoid_animation.py - 梯形教学动画
八年级 第二十二章 四边形 - 梯形知识点
# 快速预览
manim -pql trapezoid_animation.py TrapezoidLesson

# 高质量输出
manim -qh trapezoid_animation.py TrapezoidLesson
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色常量 =====
BG_COLOR = "#1a1a2e"
COLOR_TRAP = "#4FC3F7"       # 普通梯形 - 浅蓝
COLOR_ISO = "#FFD700"        # 等腰梯形 - 金色
COLOR_RIGHT_T = "#69F0AE"    # 直角梯形 - 绿色
COLOR_UPPER = "#FF8A65"      # 上底 - 橙
COLOR_LOWER = "#42A5F5"      # 下底 - 蓝
COLOR_LEG = "#AB47BC"        # 腰 - 紫
COLOR_HEIGHT = "#26C6DA"     # 高 - 青
COLOR_FORMULA = "#FF7043"    # 公式 - 橙红
COLOR_AUX = GRAY_B
COLOR_HIGHLIGHT = YELLOW
FONT_CN = "PingFang SC"


def perp_foot(point, ls, le):
    """计算点到线段的垂足"""
    lv = le - ls
    pv = point - ls
    t = np.dot(pv, lv) / np.dot(lv, lv)
    return ls + t * lv


def right_angle_mark(corner, P1, P2, size=0.18, color=WHITE):
    """创建直角符号"""
    v1 = (P1 - corner)
    v1 = v1 / np.linalg.norm(v1) * size
    v2 = (P2 - corner)
    v2 = v2 / np.linalg.norm(v2) * size
    return Polygon(
        corner,
        corner + v1,
        corner + v1 + v2,
        corner + v2,
        color=color,
        stroke_width=2,
        fill_opacity=0
    )


def tick_mark(P1, P2, n=1, size=0.12, color=WHITE, offset_perp=0.0):
    """在线段中点画n个等号标记"""
    mid = (P1 + P2) / 2
    direction = P2 - P1
    direction_norm = direction / np.linalg.norm(direction)
    perp = np.array([-direction_norm[1], direction_norm[0], 0])
    if offset_perp != 0:
        mid = mid + perp * offset_perp
    ticks = VGroup()
    spacing = 0.08
    for i in range(n):
        offset = (i - (n - 1) / 2) * spacing
        start = mid + offset * direction_norm + perp * size
        end = mid + offset * direction_norm - perp * size
        ticks.add(Line(start, end, color=color, stroke_width=2.5))
    return ticks


class TrapezoidLesson(Scene):
    """
    梯形教学动画

    场景:
    1. 开场钩子
    2. 梯形定义 + 各部分名称
    3. 梯形的高 + 面积公式
    4. 等腰梯形三大性质
    5. 直角梯形
    6. 三类梯形汇总
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_height_formula()
        self.scene_4_isosceles()
        self.scene_5_right_trapezoid()
        self.scene_6_summary()
        self.scene_7_outro()

    # =====================================================
    # 几何数据初始化
    # =====================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""

        SCALE = 1.1
        OFFSET = UP * 0.5

        # ------- 普通梯形 -------
        # A=左上, B=右上 (上底), C=右下, D=左下 (下底)
        self.A = (np.array([-1.0, 1.2, 0]) * SCALE + OFFSET)
        self.B = (np.array([1.0, 1.2, 0]) * SCALE + OFFSET)
        self.C = (np.array([2.2, -1.2, 0]) * SCALE + OFFSET)
        self.D = (np.array([-2.2, -1.2, 0]) * SCALE + OFFSET)

        self.upper_len = np.linalg.norm(self.B - self.A)   # 上底
        self.lower_len = np.linalg.norm(self.C - self.D)   # 下底
        self.trap_h = abs(self.A[1] - self.D[1])            # 高

        # 高的垂足
        self.foot_A = perp_foot(self.A, self.D, self.C)
        self.foot_B = perp_foot(self.B, self.D, self.C)

        # ------- 等腰梯形 -------
        ISO_SCALE = 1.15
        ISO_OFF = UP * 0.8
        half_top = 1.0 * ISO_SCALE
        half_bot = 2.0 * ISO_SCALE
        iso_h = 2.0 * ISO_SCALE

        self.IA = np.array([-half_top, iso_h / 2, 0]) + ISO_OFF
        self.IB = np.array([half_top, iso_h / 2, 0]) + ISO_OFF
        self.IC = np.array([half_bot, -iso_h / 2, 0]) + ISO_OFF
        self.ID = np.array([-half_bot, -iso_h / 2, 0]) + ISO_OFF

        self.iso_left_leg = np.linalg.norm(self.IA - self.ID)
        self.iso_right_leg = np.linalg.norm(self.IB - self.IC)
        self.iso_diag1 = np.linalg.norm(self.IA - self.IC)  # A到C
        self.iso_diag2 = np.linalg.norm(self.IB - self.ID)  # B到D

        # ------- 直角梯形 -------
        # 左腰垂直，右腰倾斜
        RT_OFF = UP * 0.5
        self.RA = np.array([-2.0, 1.0, 0]) + RT_OFF   # 左上
        self.RB = np.array([1.5, 1.0, 0]) + RT_OFF    # 右上
        self.RC = np.array([2.2, -1.0, 0]) + RT_OFF   # 右下
        self.RD = np.array([-2.0, -1.0, 0]) + RT_OFF  # 左下 (左腰垂直)

        self.verify_geometry()

    def verify_geometry(self):
        """验证几何关系"""
        eps = 1e-6

        # 验证普通梯形：AB ‖ DC
        ab_dir = (self.B - self.A)[:2]
        dc_dir = (self.C - self.D)[:2]
        ab_unit = ab_dir / np.linalg.norm(ab_dir)
        dc_unit = dc_dir / np.linalg.norm(dc_dir)
        assert abs(np.dot(ab_unit, dc_unit)) > 0.9999, "普通梯形AB不平行DC"

        # 验证等腰梯形：两腰相等
        assert abs(self.iso_left_leg - self.iso_right_leg) < eps, "等腰梯形腰不相等"
        # 对角线相等
        assert abs(self.iso_diag1 - self.iso_diag2) < eps, "等腰梯形对角线不相等"

        # 验证直角梯形：左腰垂直
        la_dir = (self.RA - self.RD)[:2]  # 左腰方向
        ad_dir = (self.RD - self.RA)[:2]  # 下底方向
        bot_dir = (self.RD - self.RA)[:2]  # 左腰方向
        # 检查RA-RD是否垂直于底
        bottom_dir = (self.RC - self.RD)[:2]
        # 左腰AD方向: RA-RD
        left_leg_dir = (self.RA - self.RD)[:2]
        dot = np.dot(left_leg_dir / np.linalg.norm(left_leg_dir),
                     bottom_dir / np.linalg.norm(bottom_dir))
        assert abs(dot) < eps, f"直角梯形左腰不垂直底部: dot={dot:.6f}"

        print("✓ 几何验证通过")

    # =====================================================
    # Scene 1: 开场钩子
    # =====================================================
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT_CN, font_size=20, color=GRAY_B
        ).move_to(UP * 7)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 钩子问题
        hook = Text("你知道梯形有哪些秘密？", font=FONT_CN,
                    font_size=38, color=COLOR_HIGHLIGHT)
        hook.move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.8)

        # 画普通梯形
        trap = Polygon(self.A, self.B, self.C, self.D,
                       color=COLOR_TRAP, stroke_width=3, fill_opacity=0)
        self.play(Create(trap), run_time=1.0)

        # 顶点标签
        label_A = Text("A", font=FONT_CN, font_size=22, color=WHITE).next_to(self.A, UL, buff=0.1)
        label_B = Text("B", font=FONT_CN, font_size=22, color=WHITE).next_to(self.B, UR, buff=0.1)
        label_C = Text("C", font=FONT_CN, font_size=22, color=WHITE).next_to(self.C, DR, buff=0.1)
        label_D = Text("D", font=FONT_CN, font_size=22, color=WHITE).next_to(self.D, DL, buff=0.1)
        labels = VGroup(label_A, label_B, label_C, label_D)
        self.play(FadeIn(labels), run_time=0.5)

        subtitle = Text("今天来揭秘!", font=FONT_CN,
                        font_size=28, color=GRAY_A)
        subtitle.move_to(DOWN * 3.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 清理（保留梯形和标签供下一场景）
        self.play(FadeOut(hook), FadeOut(subtitle), run_time=0.4)
        self.trap_main = trap
        self.labels_main = labels

    # =====================================================
    # Scene 2: 梯形定义 + 各部分名称
    # =====================================================
    def scene_2_definition(self):
        # 标题
        title = Text("什么是梯形？", font=FONT_CN,
                     font_size=38, color=COLOR_TRAP)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 定义
        def_text = Text("只有一组对边平行的四边形",
                        font=FONT_CN, font_size=24, color=WHITE)
        def_text.move_to(UP * 5.0)
        self.play(FadeIn(def_text, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.5)

        # --- 高亮上底 ---
        upper_side = Line(self.A, self.B, color=COLOR_UPPER, stroke_width=5)
        label_upper = Text("上底 a", font=FONT_CN,
                           font_size=22, color=COLOR_UPPER)
        label_upper.move_to((self.A + self.B) / 2 + UP * 0.35)
        self.play(Create(upper_side), run_time=0.4)
        self.play(FadeIn(label_upper), run_time=0.3)

        # --- 高亮下底 ---
        lower_side = Line(self.D, self.C, color=COLOR_LOWER, stroke_width=5)
        label_lower = Text("下底 b", font=FONT_CN,
                           font_size=22, color=COLOR_LOWER)
        label_lower.move_to((self.D + self.C) / 2 + DOWN * 0.35)
        self.play(Create(lower_side), run_time=0.4)
        self.play(FadeIn(label_lower), run_time=0.3)

        # 平行箭头标记
        arrow_up1 = Arrow(
            self.A + RIGHT * 0.15 + UP * 0.05,
            self.A + RIGHT * 0.55 + UP * 0.05,
            buff=0, max_tip_length_to_length_ratio=0.4,
            color=COLOR_UPPER, stroke_width=2.5
        ).scale(0.6)
        arrow_up2 = arrow_up1.copy().shift(RIGHT * 0.5)

        arrow_dn1 = Arrow(
            self.D + RIGHT * 0.15 + DOWN * 0.05,
            self.D + RIGHT * 0.55 + DOWN * 0.05,
            buff=0, max_tip_length_to_length_ratio=0.4,
            color=COLOR_LOWER, stroke_width=2.5
        ).scale(0.6)
        arrow_dn2 = arrow_dn1.copy().shift(RIGHT * 0.5)

        parallel_note = Text("互相平行", font=FONT_CN,
                             font_size=22, color=YELLOW)
        parallel_note.move_to(DOWN * 3.0)
        self.play(FadeIn(parallel_note), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(parallel_note), run_time=0.3)

        # --- 高亮两腰 ---
        leg_AD = Line(self.A, self.D, color=COLOR_LEG, stroke_width=5)
        leg_BC = Line(self.B, self.C, color=COLOR_LEG, stroke_width=5)

        mid_AD = (self.A + self.D) / 2
        mid_BC = (self.B + self.C) / 2

        label_leg1 = Text("腰", font=FONT_CN, font_size=22,
                          color=COLOR_LEG).next_to(mid_AD, LEFT, buff=0.15)
        label_leg2 = Text("腰", font=FONT_CN, font_size=22,
                          color=COLOR_LEG).next_to(mid_BC, RIGHT, buff=0.15)

        self.play(Create(leg_AD), Create(leg_BC), run_time=0.5)
        self.play(FadeIn(label_leg1), FadeIn(label_leg2), run_time=0.3)

        not_parallel = Text("不平行", font=FONT_CN,
                            font_size=22, color=GRAY_A)
        not_parallel.move_to(DOWN * 3.0)
        self.play(FadeIn(not_parallel), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_text),
            FadeOut(upper_side), FadeOut(lower_side),
            FadeOut(label_upper), FadeOut(label_lower),
            FadeOut(leg_AD), FadeOut(leg_BC),
            FadeOut(label_leg1), FadeOut(label_leg2),
            FadeOut(not_parallel),
            run_time=0.5
        )

    # =====================================================
    # Scene 3: 梯形的高 + 面积公式
    # =====================================================
    def scene_3_height_formula(self):
        title = Text("梯形的高和面积", font=FONT_CN,
                     font_size=36, color=COLOR_TRAP)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 重新显示上底下底标签
        label_a = Text("a", font=FONT_CN, font_size=22, color=COLOR_UPPER)
        label_a.move_to((self.A + self.B) / 2 + UP * 0.3)
        label_b = Text("b", font=FONT_CN, font_size=22, color=COLOR_LOWER)
        label_b.move_to((self.D + self.C) / 2 + DOWN * 0.3)
        self.play(FadeIn(label_a), FadeIn(label_b), run_time=0.4)

        # 高线 (从A作垂线到DC)
        foot = self.foot_A  # 已经预计算
        height_line = DashedLine(
            self.A, foot,
            color=COLOR_HEIGHT, dash_length=0.12, stroke_width=2.5
        )
        # 直角标记
        ra_mark = right_angle_mark(foot, self.A, self.D, size=0.18, color=COLOR_HEIGHT)

        self.play(Create(height_line), run_time=0.6)
        self.play(FadeIn(ra_mark), run_time=0.3)

        # Brace 标注高 h
        brace_h = Brace(height_line, direction=RIGHT, buff=0.08, color=COLOR_HEIGHT)
        label_h = Text("h", font=FONT_CN, font_size=24, color=COLOR_HEIGHT)
        label_h.next_to(brace_h, RIGHT, buff=0.1)
        self.play(FadeIn(brace_h), FadeIn(label_h), run_time=0.5)
        self.wait(0.5)

        # 面积公式
        formula_title = Text("梯形面积公式：", font=FONT_CN,
                             font_size=26, color=WHITE)
        formula_title.move_to(DOWN * 3.3)

        formula = MathTex(
            r"S = \frac{(a + b) \times h}{2}",
            font_size=42, color=COLOR_FORMULA
        )
        formula.move_to(DOWN * 4.2)

        self.play(FadeIn(formula_title), run_time=0.4)
        self.play(Write(formula), run_time=0.8)

        # 强调颜色
        formula_colored = MathTex(
            r"S = \frac{(a + b) \times h}{2}",
            font_size=42
        )
        formula_colored.set_color_by_tex("a", COLOR_UPPER)
        formula_colored.set_color_by_tex("b", COLOR_LOWER)
        formula_colored.set_color_by_tex("h", COLOR_HEIGHT)
        formula_colored.move_to(DOWN * 4.2)
        self.play(TransformMatchingTex(formula, formula_colored), run_time=0.8)

        tip = Text("上底 + 下底，乘以高，再除以2", font=FONT_CN,
                   font_size=20, color=GRAY_A)
        tip.move_to(DOWN * 5.3)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(label_a), FadeOut(label_b),
            FadeOut(height_line), FadeOut(ra_mark),
            FadeOut(brace_h), FadeOut(label_h),
            FadeOut(formula_title), FadeOut(formula_colored), FadeOut(tip),
            FadeOut(self.trap_main), FadeOut(self.labels_main),
            run_time=0.6
        )

    # =====================================================
    # Scene 4: 等腰梯形三大性质
    # =====================================================
    def scene_4_isosceles(self):
        title = Text("等腰梯形", font=FONT_CN,
                     font_size=42, color=COLOR_ISO)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        sub = Text("两腰相等的梯形", font=FONT_CN,
                   font_size=26, color=GRAY_A)
        sub.move_to(UP * 5.2)
        self.play(FadeIn(sub), run_time=0.4)

        # 等腰梯形
        iso_trap = Polygon(self.IA, self.IB, self.IC, self.ID,
                           color=COLOR_ISO, stroke_width=3.5, fill_opacity=0)
        self.play(Create(iso_trap), run_time=1.0)

        lbl_A = Text("A", font=FONT_CN, font_size=20).next_to(self.IA, UL, buff=0.1)
        lbl_B = Text("B", font=FONT_CN, font_size=20).next_to(self.IB, UR, buff=0.1)
        lbl_C = Text("C", font=FONT_CN, font_size=20).next_to(self.IC, DR, buff=0.1)
        lbl_D = Text("D", font=FONT_CN, font_size=20).next_to(self.ID, DL, buff=0.1)
        self.play(FadeIn(VGroup(lbl_A, lbl_B, lbl_C, lbl_D)), run_time=0.3)
        self.wait(0.3)

        # ===== 性质1: 两腰相等 =====
        prop1_bg = RoundedRectangle(
            width=7.0, height=0.9, corner_radius=0.2,
            fill_color="#1a1a2e", fill_opacity=0.95,
            stroke_color=COLOR_ISO, stroke_width=2
        ).move_to(DOWN * 3.8)
        prop1_num = Text("性质①", font=FONT_CN, font_size=22,
                         color=COLOR_ISO).move_to(DOWN * 3.8 + LEFT * 2.5)
        prop1_text = Text("两腰相等  AD = BC", font=FONT_CN,
                          font_size=22, color=WHITE).move_to(DOWN * 3.8 + RIGHT * 0.5)

        # 腰的等长标记
        tick_left = tick_mark(self.IA, self.ID, n=1, size=0.14, color=COLOR_ISO)
        tick_right = tick_mark(self.IB, self.IC, n=1, size=0.14, color=COLOR_ISO)

        leg_L = Line(self.IA, self.ID, color=COLOR_ISO, stroke_width=4)
        leg_R = Line(self.IB, self.IC, color=COLOR_ISO, stroke_width=4)

        self.play(Create(leg_L), Create(leg_R), run_time=0.5)
        self.play(FadeIn(tick_left), FadeIn(tick_right), run_time=0.4)
        self.play(FadeIn(prop1_bg), FadeIn(prop1_num), FadeIn(prop1_text), run_time=0.5)
        self.wait(1.5)

        # ===== 性质2: 两底角相等 =====
        prop2_bg = RoundedRectangle(
            width=7.0, height=0.9, corner_radius=0.2,
            fill_color="#1a1a2e", fill_opacity=0.95,
            stroke_color=YELLOW, stroke_width=2
        ).move_to(DOWN * 4.9)
        prop2_num = Text("性质②", font=FONT_CN, font_size=22,
                         color=YELLOW).move_to(DOWN * 4.9 + LEFT * 2.5)
        prop2_text = Text("两底角相等  ∠D = ∠C", font=FONT_CN,
                          font_size=22, color=WHITE).move_to(DOWN * 4.9 + RIGHT * 0.5)

        # ∠D 角弧 (在D处，从C到A方向)
        # ∠D = ∠CDA，顶点D，两边：DC方向和DA方向
        line_DC = Line(self.ID, self.IC)
        line_DA = Line(self.ID, self.IA)
        # cross_z at D: (IC-ID) x (IA-ID)
        v1 = self.IC - self.ID
        v2 = self.IA - self.ID
        cz_D = v1[0] * v2[1] - v1[1] * v2[0]
        angle_D = Angle(
            line_DC, line_DA,
            radius=0.45, color=YELLOW,
            other_angle=(cz_D < 0)
        )

        # ∠C 角弧 (在C处，从D到B方向)
        line_CD = Line(self.IC, self.ID)
        line_CB = Line(self.IC, self.IB)
        v3 = self.ID - self.IC
        v4 = self.IB - self.IC
        cz_C = v3[0] * v4[1] - v3[1] * v4[0]
        angle_C = Angle(
            line_CD, line_CB,
            radius=0.45, color=YELLOW,
            other_angle=(cz_C < 0)
        )

        self.play(Create(angle_D), Create(angle_C), run_time=0.6)
        self.play(FadeIn(prop2_bg), FadeIn(prop2_num), FadeIn(prop2_text), run_time=0.5)
        self.wait(1.5)

        # ===== 性质3: 对角线相等 =====
        prop3_bg = RoundedRectangle(
            width=7.0, height=0.9, corner_radius=0.2,
            fill_color="#1a1a2e", fill_opacity=0.95,
            stroke_color="#CE93D8", stroke_width=2
        ).move_to(DOWN * 6.0)
        prop3_num = Text("性质③", font=FONT_CN, font_size=22,
                         color="#CE93D8").move_to(DOWN * 6.0 + LEFT * 2.5)
        prop3_text = Text("对角线相等  AC = BD", font=FONT_CN,
                          font_size=22, color=WHITE).move_to(DOWN * 6.0 + RIGHT * 0.5)

        diag_AC = DashedLine(self.IA, self.IC, color="#CE93D8",
                             dash_length=0.12, stroke_width=2.5)
        diag_BD = DashedLine(self.IB, self.ID, color="#CE93D8",
                             dash_length=0.12, stroke_width=2.5)

        self.play(Create(diag_AC), Create(diag_BD), run_time=0.8)
        self.play(FadeIn(prop3_bg), FadeIn(prop3_num), FadeIn(prop3_text), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(iso_trap),
            FadeOut(VGroup(lbl_A, lbl_B, lbl_C, lbl_D)),
            FadeOut(leg_L), FadeOut(leg_R),
            FadeOut(tick_left), FadeOut(tick_right),
            FadeOut(angle_D), FadeOut(angle_C),
            FadeOut(diag_AC), FadeOut(diag_BD),
            FadeOut(prop1_bg), FadeOut(prop1_num), FadeOut(prop1_text),
            FadeOut(prop2_bg), FadeOut(prop2_num), FadeOut(prop2_text),
            FadeOut(prop3_bg), FadeOut(prop3_num), FadeOut(prop3_text),
            run_time=0.6
        )

    # =====================================================
    # Scene 5: 直角梯形
    # =====================================================
    def scene_5_right_trapezoid(self):
        title = Text("直角梯形", font=FONT_CN,
                     font_size=42, color=COLOR_RIGHT_T)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        sub = Text("有一个角是直角的梯形", font=FONT_CN,
                   font_size=26, color=GRAY_A)
        sub.move_to(UP * 5.2)
        self.play(FadeIn(sub), run_time=0.4)

        # 直角梯形: RA左上, RB右上, RC右下, RD左下
        # 左腰RA-RD垂直
        rt_trap = Polygon(self.RA, self.RB, self.RC, self.RD,
                          color=COLOR_RIGHT_T, stroke_width=3.5, fill_opacity=0)
        self.play(Create(rt_trap), run_time=1.0)

        lbl_A = Text("A", font=FONT_CN, font_size=20).next_to(self.RA, UL, buff=0.1)
        lbl_B = Text("B", font=FONT_CN, font_size=20).next_to(self.RB, UR, buff=0.1)
        lbl_C = Text("C", font=FONT_CN, font_size=20).next_to(self.RC, DR, buff=0.1)
        lbl_D = Text("D", font=FONT_CN, font_size=20).next_to(self.RD, DL, buff=0.1)
        self.play(FadeIn(VGroup(lbl_A, lbl_B, lbl_C, lbl_D)), run_time=0.3)

        # 直角标记 - ∠A (左上角，左腰与上底的夹角 = 90°)
        ra_A = right_angle_mark(self.RA, self.RD, self.RB, size=0.20, color=COLOR_RIGHT_T)
        # 直角标记 - ∠D (左下角，左腰与下底的夹角 = 90°)
        ra_D = right_angle_mark(self.RD, self.RA, self.RC, size=0.20, color=COLOR_RIGHT_T)

        self.play(FadeIn(ra_A), FadeIn(ra_D), run_time=0.5)

        # 标注左腰是垂直腰
        mid_left = (self.RA + self.RD) / 2
        perp_label = Text("垂直腰", font=FONT_CN, font_size=20,
                          color=COLOR_RIGHT_T).next_to(mid_left, LEFT, buff=0.2)
        self.play(FadeIn(perp_label), run_time=0.4)

        note = Text("左腰 ⊥ 上底  和  左腰 ⊥ 下底", font=FONT_CN,
                    font_size=22, color=WHITE)
        note.move_to(DOWN * 3.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(rt_trap),
            FadeOut(VGroup(lbl_A, lbl_B, lbl_C, lbl_D)),
            FadeOut(ra_A), FadeOut(ra_D),
            FadeOut(perp_label), FadeOut(note),
            run_time=0.5
        )

    # =====================================================
    # Scene 6: 三类梯形汇总
    # =====================================================
    def scene_6_summary(self):
        title = Text("三种梯形", font=FONT_CN, font_size=40,
                     color=COLOR_HIGHLIGHT)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # --- 等腰梯形 (左) ---
        s = 0.45   # 缩放
        off_iso = UP * 3.5 + LEFT * 2.8

        iA = np.array([-0.8, 0.7, 0]) * s + off_iso
        iB = np.array([0.8, 0.7, 0]) * s + off_iso
        iC = np.array([1.5, -0.7, 0]) * s + off_iso
        iD = np.array([-1.5, -0.7, 0]) * s + off_iso

        iso_mini = Polygon(iA, iB, iC, iD, color=COLOR_ISO,
                           stroke_width=3, fill_opacity=0.15, fill_color=COLOR_ISO)
        tick_L = tick_mark(iA, iD, n=1, size=0.08, color=COLOR_ISO)
        tick_R = tick_mark(iB, iC, n=1, size=0.08, color=COLOR_ISO)
        name_iso = Text("等腰梯形", font=FONT_CN, font_size=22,
                        color=COLOR_ISO).next_to(iso_mini, DOWN, buff=0.3)

        # --- 直角梯形 (中) ---
        off_rt = UP * 3.5

        rA2 = np.array([-1.0, 0.7, 0]) * s + off_rt
        rB2 = np.array([0.8, 0.7, 0]) * s + off_rt
        rC2 = np.array([1.5, -0.7, 0]) * s + off_rt
        rD2 = np.array([-1.0, -0.7, 0]) * s + off_rt

        rt_mini = Polygon(rA2, rB2, rC2, rD2, color=COLOR_RIGHT_T,
                          stroke_width=3, fill_opacity=0.15, fill_color=COLOR_RIGHT_T)
        ra_mini_A = right_angle_mark(rA2, rD2, rB2, size=0.10, color=COLOR_RIGHT_T)
        ra_mini_D = right_angle_mark(rD2, rA2, rC2, size=0.10, color=COLOR_RIGHT_T)
        name_rt = Text("直角梯形", font=FONT_CN, font_size=22,
                       color=COLOR_RIGHT_T).next_to(rt_mini, DOWN, buff=0.3)

        # --- 普通梯形 (右) ---
        off_gen = UP * 3.5 + RIGHT * 2.8

        gA = np.array([-0.7, 0.7, 0]) * s + off_gen
        gB = np.array([0.7, 0.7, 0]) * s + off_gen
        gC = np.array([1.5, -0.7, 0]) * s + off_gen
        gD = np.array([-1.5, -0.7, 0]) * s + off_gen

        gen_mini = Polygon(gA, gB, gC, gD, color=COLOR_TRAP,
                           stroke_width=3, fill_opacity=0.15, fill_color=COLOR_TRAP)
        name_gen = Text("普通梯形", font=FONT_CN, font_size=22,
                        color=COLOR_TRAP).next_to(gen_mini, DOWN, buff=0.3)

        self.play(
            Create(iso_mini), Create(rt_mini), Create(gen_mini),
            run_time=0.8
        )
        self.play(
            FadeIn(tick_L), FadeIn(tick_R),
            FadeIn(ra_mini_A), FadeIn(ra_mini_D),
            run_time=0.4
        )
        self.play(
            FadeIn(name_iso), FadeIn(name_rt), FadeIn(name_gen),
            run_time=0.5
        )

        # 面积公式
        formula_title2 = Text("面积公式（通用）", font=FONT_CN,
                              font_size=26, color=WHITE)
        formula_title2.move_to(UP * 1.5)
        formula2 = MathTex(
            r"S = \frac{(a + b) \times h}{2}",
            font_size=44, color=COLOR_FORMULA
        )
        formula2.move_to(UP * 0.5)
        self.play(FadeIn(formula_title2), Write(formula2), run_time=0.8)

        # 关键词卡片
        cards_data = [
            ("上底 + 下底", "(两平行边相加)", COLOR_UPPER),
            ("× 高 ÷ 2", "(两底间的距离)", COLOR_HEIGHT),
        ]
        cards = VGroup()
        for i, (text, note, color) in enumerate(cards_data):
            card_bg = RoundedRectangle(
                width=6.5, height=0.85, corner_radius=0.15,
                fill_color="#0d0d1e", fill_opacity=1,
                stroke_color=color, stroke_width=1.5
            )
            card_text = Text(text, font=FONT_CN, font_size=22, color=color)
            card_note = Text(note, font=FONT_CN, font_size=18, color=GRAY_A)
            card_content = VGroup(card_text, card_note).arrange(RIGHT, buff=0.3)
            card = VGroup(card_bg, card_content)
            card_content.move_to(card_bg.get_center())
            cards.add(card)

        cards.arrange(DOWN, buff=0.2).move_to(DOWN * 1.2)
        self.play(FadeIn(cards, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(iso_mini), FadeOut(rt_mini), FadeOut(gen_mini),
            FadeOut(tick_L), FadeOut(tick_R),
            FadeOut(ra_mini_A), FadeOut(ra_mini_D),
            FadeOut(name_iso), FadeOut(name_rt), FadeOut(name_gen),
            FadeOut(formula_title2), FadeOut(formula2),
            FadeOut(cards),
            run_time=0.6
        )

    # =====================================================
    # Scene 7: 片尾
    # =====================================================
    def scene_7_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=36, color=WHITE
        ).move_to(UP * 2)
        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=28, color=GRAY_B
        ).move_to(UP * 1.2)

        self.play(
            Transform(self.author, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id), run_time=0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font=FONT_CN, font_size=30, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)

        # 梯形装饰动画
        decos = VGroup()
        colors = [COLOR_TRAP, COLOR_ISO, COLOR_RIGHT_T, YELLOW, PINK]
        for i in range(5):
            angle_rot = i * PI * 2 / 5
            pos = 2.5 * np.array([np.cos(angle_rot), np.sin(angle_rot), 0]) + DOWN * 2
            mini_trap = Polygon(
                np.array([-0.3, 0.2, 0]),
                np.array([0.3, 0.2, 0]),
                np.array([0.5, -0.2, 0]),
                np.array([-0.5, -0.2, 0]),
                color=colors[i],
                fill_opacity=0.7,
                stroke_width=0
            ).move_to(pos)
            decos.add(mini_trap)

        self.play(*[FadeIn(d, scale=0.3) for d in decos], run_time=0.6)
        self.play(Rotate(decos, angle=PI, run_time=1.5, about_point=DOWN * 2))
        self.wait(1.0)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(decos),
            run_time=1.0
        )
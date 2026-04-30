"""
直线的倾斜角与斜率 - Inclination Angle and Slope of a Line
Manim 0.19.2 | TikTok 竖屏 1080×1920
目标: 高二学生 | 知识点: 倾斜角、斜率定义与公式
作者标识: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ========== 全局配置 TikTok 竖屏 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ========== 颜色常量 ==========
BG_COLOR = "#1a1a2e"
C_POS  = "#e74c3c"   # 红 k>0
C_NEG  = "#3498db"   # 蓝 k<0
C_ZERO = "#2ecc71"   # 绿 k=0
C_INF  = "#9b59b6"   # 紫 无斜率
C_ANG  = "#f39c12"   # 橙 倾斜角弧
C_AUX  = "#888888"   # 灰 辅助
FONT   = "PingFang SC"


class SlopeAndInclinationAngle(Scene):
    """
    直线的倾斜角与斜率教学动画
    Scene 1: 开场钩子
    Scene 2: 倾斜角定义
    Scene 3: k = tan α
    Scene 4: 两点斜率公式
    Scene 5: 四种直线类型
    Scene 6: 总结
    Scene 7: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_inclination_angle()
        self.scene_3_k_tan_alpha()
        self.scene_4_two_point_formula()
        self.scene_5_four_cases()
        self.scene_6_summary()
        self.scene_7_outro()

    # =========================================================
    # 几何数据初始化
    # =========================================================

    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ===== 坐标系参数 =====
        self.AXES_CENTER  = np.array([0.0, 1.5, 0.0])   # 坐标系在屏幕上的位置
        self.AXES_X_LEN   = 6.5
        self.AXES_Y_LEN   = 5.0
        self.X_RANGE      = (-3, 3, 1)
        self.Y_RANGE      = (-2, 3, 1)

        # ===== 两点斜率公式示例点 =====
        # A(1, 1)  B(3, 3) → k = (3-1)/(3-1) = 1, α = 45°
        self.ax_x1, self.ax_y1 = 1.0, 1.0   # 数据坐标
        self.ax_x2, self.ax_y2 = 3.0, 3.0

        # ===== 各倾斜角预计算 =====
        self.alpha_45  = np.pi / 4        # 45°,  k=1
        self.alpha_135 = 3 * np.pi / 4   # 135°, k=-1
        self.alpha_0   = 0.0              # 0°,   k=0
        self.alpha_90  = np.pi / 2        # 90°,  无斜率

        # ===== 斜率验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        """数值验证"""
        eps = 1e-10

        # 验证 k = (y2-y1)/(x2-x1)
        k_expected = (self.ax_y2 - self.ax_y1) / (self.ax_x2 - self.ax_x1)
        assert abs(k_expected - 1.0) < eps, f"两点斜率计算错误: {k_expected}"

        # 验证 tan(45°) = 1
        assert abs(np.tan(self.alpha_45) - 1.0) < eps, "tan(45°) 错误"
        # 验证 tan(135°) = -1
        assert abs(np.tan(self.alpha_135) - (-1.0)) < eps, "tan(135°) 错误"
        # 验证 tan(0°) = 0
        assert abs(np.tan(self.alpha_0) - 0.0) < eps, "tan(0°) 错误"

        # 验证倾斜角在 [0, π) 内
        for alpha_name, alpha_val in [
            ("45°", self.alpha_45),
            ("135°", self.alpha_135),
            ("0°", self.alpha_0),
            ("90°", self.alpha_90),
        ]:
            assert 0 <= alpha_val < np.pi, f"倾斜角 {alpha_name} 超出范围 [0, π)"

        print("✓ 几何验证通过")

    # =========================================================
    # 工具函数
    # =========================================================

    def make_axes(self):
        """创建标准坐标系"""
        axes = Axes(
            x_range=list(self.X_RANGE),
            y_range=list(self.Y_RANGE),
            x_length=self.AXES_X_LEN,
            y_length=self.AXES_Y_LEN,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "color": WHITE,
            },
            tips=True,
        ).move_to(self.AXES_CENTER)
        return axes

    def make_line_through_origin(self, axes, alpha, color, length=5.5):
        """
        过原点作倾斜角为 alpha 的直线
        alpha: 弧度, 在 [0, π) 内
        返回 Line 对象（屏幕坐标）
        """
        # 方向向量（单位向量）
        dx = np.cos(alpha)
        dy = np.sin(alpha)
        # 数据坐标端点
        half = length / 2
        p1_data = np.array([-half * abs(dx) * np.sign(dx), -half * abs(dy) * np.sign(dy)])
        p2_data = np.array([ half * abs(dx) * np.sign(dx),  half * abs(dy) * np.sign(dy)])

        # 如果是水平线
        if abs(dy) < 1e-10:
            p1_data = np.array([-half, 0.0])
            p2_data = np.array([ half, 0.0])
        # 如果是垂直线
        elif abs(dx) < 1e-10:
            p1_data = np.array([0.0, -half])
            p2_data = np.array([0.0,  half])
        else:
            # 延长到整个数据范围
            t = half / max(abs(dx), abs(dy))
            p1_data = np.array([-t * dx, -t * dy])
            p2_data = np.array([ t * dx,  t * dy])

        p1_screen = axes.c2p(p1_data[0], p1_data[1])
        p2_screen = axes.c2p(p2_data[0], p2_data[1])
        return Line(p1_screen, p2_screen, color=color, stroke_width=4)

    def make_inclination_arc(self, axes, alpha, color=None, radius=0.7):
        """
        在坐标原点处绘制倾斜角弧（从x轴正方向到直线方向，逆时针）
        alpha: 倾斜角（弧度），必须在 [0, π) 内
        返回 Arc
        """
        if color is None:
            color = C_ANG
        origin_screen = axes.c2p(0, 0)
        arc = Arc(
            radius=radius,
            start_angle=0,         # 从x轴正方向开始
            angle=alpha,           # 逆时针旋转 alpha
            arc_center=origin_screen,
            color=color,
            stroke_width=4,
        )
        return arc

    def make_alpha_label(self, axes, alpha, radius=1.1):
        """在倾斜角弧中间位置放置 α 标签"""
        mid_angle = alpha / 2
        origin_screen = axes.c2p(0, 0)
        label_pos = origin_screen + radius * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
        label = MathTex(r"\alpha", font_size=28, color=C_ANG).move_to(label_pos)
        return label

    def cn(self, text, size=22, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    # =========================================================
    # Scene 1: 开场钩子 (0-4s)
    # =========================================================

    def scene_1_opening(self):
        # 作者信息
        self.author_bar = self.cn(
            "上海初高中数学直通车 @emptyandcalm", size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # 钩子
        hook1 = self.cn("直线有多 斜 ？", size=54, color=WHITE).move_to(UP * 3.5)
        hook2 = self.cn("用倾斜角来量！", size=40, color=YELLOW).move_to(UP * 2.4)
        self.play(Write(hook1), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.5)

        # 快速展示三条不同倾斜度的直线
        demo_axes = Axes(
            x_range=[-2, 2, 1], y_range=[-1.5, 1.5, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"include_numbers": False, "color": GRAY},
            tips=False,
        ).move_to(DOWN * 1.5)

        lines_demo = VGroup(
            Line(demo_axes.c2p(-2, -2), demo_axes.c2p(2, 2), color=C_POS, stroke_width=4),
            Line(demo_axes.c2p(-2, 1.5), demo_axes.c2p(2, -1.5), color=C_NEG, stroke_width=4),
            Line(demo_axes.c2p(-2, 0), demo_axes.c2p(2, 0), color=C_ZERO, stroke_width=4),
        )

        self.play(Create(demo_axes), run_time=0.5)
        for l in lines_demo:
            self.play(Create(l), run_time=0.3)

        labels_demo = VGroup(
            self.cn("k>0", size=20, color=C_POS).move_to(demo_axes.c2p(1.5, 1.5) + UP * 0.15),
            self.cn("k<0", size=20, color=C_NEG).move_to(demo_axes.c2p(1.5, -1.5) + DOWN * 0.15),
            self.cn("k=0", size=20, color=C_ZERO).move_to(demo_axes.c2p(1.5, 0) + UP * 0.25),
        )
        self.play(FadeIn(labels_demo), run_time=0.4)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(demo_axes), FadeOut(lines_demo), FadeOut(labels_demo),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: 倾斜角定义 (4-18s)
    # =========================================================

    def scene_2_inclination_angle(self):
        title = self.cn("倾斜角 α 的定义", size=36, color=GOLD).move_to(UP * 6.8)
        self.play(FadeIn(title), run_time=0.4)

        # 建立坐标系
        axes = self.make_axes()
        x_label = self.cn("x", size=20).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = self.cn("y", size=20).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.8)

        # 一条 45° 的直线过原点
        alpha = self.alpha_45
        line_45 = self.make_line_through_origin(axes, alpha, C_POS)
        self.play(Create(line_45), run_time=0.7)

        # 倾斜角弧
        arc_alpha = self.make_inclination_arc(axes, alpha, radius=0.7)
        alpha_lbl = self.make_alpha_label(axes, alpha, radius=1.05)
        self.play(Create(arc_alpha), FadeIn(alpha_lbl), run_time=0.6)

        # x轴正方向箭头标注
        origin_s = axes.c2p(0, 0)
        x_pos_pt = axes.c2p(1.2, 0)
        x_dir_arrow = Arrow(origin_s, x_pos_pt, color=YELLOW, buff=0,
                            stroke_width=4, max_tip_length_to_length_ratio=0.15)
        x_dir_lbl = self.cn("x轴正方向", size=18, color=YELLOW).next_to(
            x_dir_arrow, DOWN, buff=0.15
        )
        self.play(GrowArrow(x_dir_arrow), FadeIn(x_dir_lbl), run_time=0.6)

        # 定义说明
        defn1 = self.cn("倾斜角: 直线向上方向", size=24, color=WHITE).move_to(DOWN * 3.5)
        defn2 = self.cn("与 x 轴正方向所成的角", size=24, color=WHITE).move_to(DOWN * 4.1)
        self.play(FadeIn(defn1), FadeIn(defn2), run_time=0.5)
        self.wait(0.5)

        # 强调范围
        range_formula = MathTex(r"\alpha \in [0^{\circ},\ 180^{\circ})",
                                font_size=36, color=YELLOW).move_to(DOWN * 5.0)
        self.play(Write(range_formula), run_time=0.7)

        # 再展示 135° 直线
        line_135 = self.make_line_through_origin(axes, self.alpha_135, C_NEG)
        arc_135 = self.make_inclination_arc(axes, self.alpha_135, color=C_NEG, radius=0.5)
        lbl_135 = MathTex(r"\alpha=135^{\circ}", font_size=22, color=C_NEG).move_to(
            axes.c2p(0, 0) + np.array([-1.0, 0.7, 0])
        )
        self.play(Create(line_135), run_time=0.5)
        self.play(Create(arc_135), FadeIn(lbl_135), run_time=0.5)

        lbl_45 = MathTex(r"\alpha=45^{\circ}", font_size=22, color=C_POS).move_to(
            axes.c2p(0, 0) + np.array([0.9, 0.45, 0])
        )
        self.play(FadeIn(lbl_45), run_time=0.3)
        self.wait(1.5)

        # 保存引用，Scene 3 继续使用
        self._axes_s2 = axes
        self._x_label_s2 = x_label
        self._y_label_s2 = y_label
        self._all_s2 = [
            title, arc_alpha, alpha_lbl, x_dir_arrow, x_dir_lbl,
            defn1, defn2, range_formula,
            line_135, arc_135, lbl_135, lbl_45
        ]
        self._line_45 = line_45

    # =========================================================
    # Scene 3: k = tan α (18-34s)
    # =========================================================

    def scene_3_k_tan_alpha(self):
        axes = self._axes_s2

        # 清理 Scene 2 内容（保留坐标系和45°线）
        for obj in self._all_s2:
            self.play(FadeOut(obj), run_time=0.1)

        # 新标题
        title = self.cn("斜率 k = tan α", size=36, color=GOLD).move_to(UP * 6.8)
        self.play(FadeIn(title), run_time=0.4)

        # 核心公式
        core_formula = MathTex(
            r"k = \tan\alpha \quad (\alpha \neq 90^{\circ})",
            font_size=36
        ).move_to(UP * 5.7)
        self.play(Write(core_formula), run_time=0.8)

        # ---- 案例1: α=45°, k=1 ----
        arc1 = self.make_inclination_arc(axes, self.alpha_45, color=C_POS, radius=0.65)
        lbl_a1 = MathTex(r"\alpha\!=\!45^{\circ}", font_size=22, color=C_POS).move_to(
            axes.c2p(0, 0) + np.array([0.85, 0.35, 0])
        )
        case1_text = VGroup(
            MathTex(r"k = \tan 45^{\circ} = 1", font_size=30, color=C_POS),
            self.cn("→ 锐角倾斜，从左下到右上", size=20, color=C_POS),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 3.2)

        self.play(Create(arc1), FadeIn(lbl_a1), run_time=0.5)
        self.play(Write(case1_text[0]), run_time=0.5)
        self.play(FadeIn(case1_text[1]), run_time=0.4)
        self.wait(0.8)

        # ---- 案例2: α=135°, k=-1 ----
        line_135 = self.make_line_through_origin(axes, self.alpha_135, C_NEG)
        arc2 = self.make_inclination_arc(axes, self.alpha_135, color=C_NEG, radius=0.5)
        lbl_a2 = MathTex(r"\alpha\!=\!135^{\circ}", font_size=22, color=C_NEG).move_to(
            axes.c2p(0, 0) + np.array([-1.0, 0.55, 0])
        )
        self.play(Create(line_135), Create(arc2), FadeIn(lbl_a2), run_time=0.6)

        case2_text = VGroup(
            MathTex(r"k = \tan 135^{\circ} = -1", font_size=30, color=C_NEG),
            self.cn("→ 钝角倾斜，从左上到右下", size=20, color=C_NEG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 4.5)

        self.play(Write(case2_text[0]), run_time=0.5)
        self.play(FadeIn(case2_text[1]), run_time=0.4)
        self.wait(0.8)

        # ---- 案例3: α=90°, 无斜率 ----
        line_90 = self.make_line_through_origin(axes, self.alpha_90, C_INF)
        # α=90° 时弧覆盖整个 [0°, 90°] 区域
        arc3 = self.make_inclination_arc(axes, self.alpha_90, color=C_INF, radius=0.4)
        no_slope_text = VGroup(
            MathTex(r"\alpha = 90^{\circ}", font_size=28, color=C_INF),
            self.cn("斜率不存在！", size=24, color=C_INF),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 5.8)

        self.play(Create(line_90), Create(arc3), run_time=0.5)
        self.play(FadeIn(no_slope_text), run_time=0.5)
        self.wait(1.5)

        # 清理
        to_fade = [
            title, core_formula, self._line_45,
            arc1, lbl_a1, case1_text,
            line_135, arc2, lbl_a2, case2_text,
            line_90, arc3, no_slope_text,
        ]
        self.play(*[FadeOut(o) for o in to_fade], run_time=0.5)

        # 保留坐标系给 Scene 4
        self._axes_main = axes
        self._x_label_main = self._x_label_s2
        self._y_label_main = self._y_label_s2

    # =========================================================
    # Scene 4: 两点斜率公式 (34-52s)
    # =========================================================

    def scene_4_two_point_formula(self):
        axes = self._axes_main

        title = self.cn("两点斜率公式", size=36, color=GOLD).move_to(UP * 6.8)
        self.play(FadeIn(title), run_time=0.4)

        # ---- 标注两点 A(1,1), B(3,3) ----
        pt_A_screen = axes.c2p(self.ax_x1, self.ax_y1)
        pt_B_screen = axes.c2p(self.ax_x2, self.ax_y2)

        dot_A = Dot(pt_A_screen, color=C_POS, radius=0.10)
        dot_B = Dot(pt_B_screen, color=C_POS, radius=0.10)
        lbl_A = MathTex(r"A(1,\ 1)", font_size=24, color=C_POS).next_to(dot_A, DL, buff=0.1)
        lbl_B = MathTex(r"B(3,\ 3)", font_size=24, color=C_POS).next_to(dot_B, UR, buff=0.1)

        self.play(FadeIn(dot_A), FadeIn(lbl_A), run_time=0.4)
        self.play(FadeIn(dot_B), FadeIn(lbl_B), run_time=0.4)

        # 连线 AB（直线过这两点）
        # 延伸到坐标系边界
        p1_ext = axes.c2p(-1, -1)
        p2_ext = axes.c2p(3.5, 3.5)
        # 限制在可见范围
        p1_ext = axes.c2p(-1.5, -1.5)
        line_AB = Line(p1_ext, p2_ext, color=C_POS, stroke_width=4)
        self.play(Create(line_AB), run_time=0.7)

        # 辅助线: 水平线 (Δx) 和垂直线 (Δy)
        pt_C_screen = axes.c2p(self.ax_x2, self.ax_y1)  # C = (3, 1)
        h_line = DashedLine(pt_A_screen, pt_C_screen, color=C_AUX, dash_length=0.12)
        v_line = DashedLine(pt_C_screen, pt_B_screen, color=C_AUX, dash_length=0.12)

        delta_x_lbl = MathTex(r"\Delta x = 2", font_size=22, color=YELLOW).move_to(
            (np.array(pt_A_screen) + np.array(pt_C_screen)) / 2 + DOWN * 0.3
        )
        delta_y_lbl = MathTex(r"\Delta y = 2", font_size=22, color=YELLOW).move_to(
            (np.array(pt_C_screen) + np.array(pt_B_screen)) / 2 + RIGHT * 0.4
        )

        self.play(Create(h_line), Create(v_line), run_time=0.6)
        self.play(FadeIn(delta_x_lbl), FadeIn(delta_y_lbl), run_time=0.5)

        # ---- 公式推导 ----
        formula_title = self.cn("斜率公式推导:", size=24, color=WHITE).move_to(DOWN * 3.3)
        self.play(FadeIn(formula_title), run_time=0.3)

        step1 = MathTex(
            r"k = \frac{y_2 - y_1}{x_2 - x_1}",
            font_size=34
        ).move_to(DOWN * 4.2)
        self.play(Write(step1), run_time=0.7)

        step2 = MathTex(
            r"= \frac{3 - 1}{3 - 1}",
            font_size=34
        ).move_to(DOWN * 5.1)
        self.play(Write(step2), run_time=0.6)

        step3 = MathTex(
            r"= \frac{2}{2} = 1",
            font_size=40, color=C_POS
        ).move_to(DOWN * 6.0)
        self.play(Write(step3), run_time=0.5)

        # 高亮结果
        result_box = SurroundingRectangle(step3, color=C_POS, buff=0.2, corner_radius=0.1)
        self.play(Create(result_box), run_time=0.4)

        # 强调 x₁ ≠ x₂
        warn = self.cn("注意: x₁ ≠ x₂ (否则斜率不存在)", size=20, color=YELLOW).move_to(
            DOWN * 6.9
        )
        self.play(FadeIn(warn), run_time=0.4)
        self.wait(1.5)

        # 清理所有 Scene 4 元素
        to_fade = [
            title, dot_A, dot_B, lbl_A, lbl_B, line_AB,
            h_line, v_line, delta_x_lbl, delta_y_lbl,
            formula_title, step1, step2, step3, result_box, warn,
            self._axes_main, self._x_label_main, self._y_label_main
        ]
        self.play(*[FadeOut(o) for o in to_fade], run_time=0.5)

    # =========================================================
    # Scene 5: 四种直线类型 (52-66s)
    # =========================================================

    def scene_5_four_cases(self):
        title = self.cn("斜率的四种情况", size=36, color=GOLD).move_to(UP * 6.8)
        self.play(FadeIn(title), run_time=0.4)

        # 建一个新的小坐标系
        axes_small = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.0, 2.0, 1],
            x_length=5.5,
            y_length=4.5,
            axis_config={"include_numbers": False, "color": GRAY},
            tips=True,
        ).move_to(UP * 3.2)

        self.play(Create(axes_small), run_time=0.6)

        # 四条直线
        # 1) k>0: α=45°
        l1 = Line(axes_small.c2p(-2, -2), axes_small.c2p(2, 2),
                  color=C_POS, stroke_width=5)
        # 2) k<0: α=135°
        l2 = Line(axes_small.c2p(-2, 2), axes_small.c2p(2, -2),
                  color=C_NEG, stroke_width=5)
        # 3) k=0: 水平
        l3 = Line(axes_small.c2p(-2.3, 0), axes_small.c2p(2.3, 0),
                  color=C_ZERO, stroke_width=5)
        # 4) 无斜率: 垂直
        l4 = Line(axes_small.c2p(0, -2), axes_small.c2p(0, 2),
                  color=C_INF, stroke_width=5)

        # 说明文字（右侧卡片）
        cases_info = VGroup(
            self._make_case_card("k > 0", "锐角 (α < 90°)", "左下→右上", C_POS),
            self._make_case_card("k < 0", "钝角 (α > 90°)", "左上→右下", C_NEG),
            self._make_case_card("k = 0", "水平 (α = 0°)", "沿x轴", C_ZERO),
            self._make_case_card("undefined", "垂直 (α = 90°)", "沿y轴方向", C_INF),  # Fixed: replaced "无斜率" to avoid LaTeX error in MathTex
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(DOWN * 1.5)

        # 逐条展示
        pairs = [(l1, cases_info[0]), (l2, cases_info[1]),
                 (l3, cases_info[2]), (l4, cases_info[3])]
        for line, card in pairs:
            self.play(Create(line), FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 倾斜角弧示意（在坐标系内）
        arc_pos = self.make_inclination_arc(axes_small, self.alpha_45, color=C_POS, radius=0.4)
        arc_neg = self.make_inclination_arc(axes_small, self.alpha_135, color=C_NEG, radius=0.32)
        self.play(Create(arc_pos), Create(arc_neg), run_time=0.5)

        self.wait(2.0)

        to_fade = [title, axes_small, l1, l2, l3, l4, cases_info, arc_pos, arc_neg]
        self.play(*[FadeOut(o) for o in to_fade], run_time=0.5)

    def _make_case_card(self, k_text, angle_desc, direction, color):
        """创建斜率情况卡片"""
        k_lbl = MathTex(k_text, font_size=30, color=color)
        ang_lbl = self.cn(angle_desc, size=18, color=GRAY_A)
        dir_lbl = self.cn(direction, size=18, color=GRAY_A)
        card = VGroup(k_lbl, ang_lbl, dir_lbl).arrange(RIGHT, buff=0.3)
        return card

    # =========================================================
    # Scene 6: 总结 (66-73s)
    # =========================================================

    def scene_6_summary(self):
        title = self.cn("核心公式总结", size=36, color=GOLD).move_to(UP * 6.8)
        self.play(FadeIn(title), run_time=0.4)

        # 公式卡片
        formulas = VGroup(
            self._formula_card(
                "倾斜角范围",
                r"\alpha \in [0^{\circ},\ 180^{\circ})",
                "#e8d5a3"
            ),
            self._formula_card(
                "斜率与倾斜角",
                r"k = \tan\alpha \quad (\alpha \neq 90^{\circ})",
                C_POS
            ),
            self._formula_card(
                "两点斜率公式",
                r"k = \dfrac{y_2 - y_1}{x_2 - x_1} \quad (x_1 \neq x_2)",
                C_NEG
            ),
            self._formula_card_special("特殊情况", C_INF),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 2.5)

        for fc in formulas:
            self.play(FadeIn(fc, shift=RIGHT * 0.3), run_time=0.35)

        # 记忆口诀
        tip_box = RoundedRectangle(
            width=7.5, height=1.8, corner_radius=0.2,
            fill_color="#1a2a1a", fill_opacity=0.9,
            stroke_color=YELLOW, stroke_width=2
        ).move_to(DOWN * 4.0)
        tip_text1 = self.cn("记忆口诀:", size=22, color=YELLOW)
        tip_text2 = self.cn("正斜上、负斜下、零水平、90°无斜率", size=20, color=WHITE)
        VGroup(tip_text1, tip_text2).arrange(DOWN, buff=0.2).move_to(DOWN * 4.0)

        self.play(Create(tip_box), run_time=0.3)
        self.play(FadeIn(tip_text1), FadeIn(tip_text2), run_time=0.5)
        self.wait(2.0)

        to_fade = [title, formulas, tip_box, tip_text1, tip_text2]
        self.play(*[FadeOut(o) for o in to_fade], run_time=0.5)

    def _formula_card_special(self, cn_title, color):
        """公式卡片 - 混合中文+公式（分开处理）"""
        title_t = self.cn(cn_title, size=22, color=color)
        # 将中文 "斜率不存在" 与公式分开
        formula_part = MathTex(r"\alpha = 90^{\circ}", font_size=30, color=WHITE)
        no_slope_t = self.cn("→ 斜率不存在", size=22, color=WHITE)
        formula_row = VGroup(formula_part, no_slope_t).arrange(RIGHT, buff=0.3)
        card = VGroup(title_t, formula_row).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        return card

    def _formula_card(self, cn_title, formula_str, color, formula_size=30):
        """公式卡片"""
        title_t = self.cn(cn_title, size=22, color=color)
        formula_t = MathTex(formula_str, font_size=formula_size, color=WHITE)
        card = VGroup(title_t, formula_t).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        return card

    # =========================================================
    # Scene 7: 片尾 (73-82s)
    # =========================================================

    def scene_7_outro(self):
        final_name = self.cn("上海初高中数学直通车", size=40, color=WHITE).move_to(UP * 2.0)
        final_id   = self.cn("@emptyandcalm", size=32, color=GRAY_B).move_to(UP * 0.9)
        follow     = self.cn("关注我，获得更多数学技巧!", size=30, color=YELLOW).move_to(DOWN * 0.3)

        self.play(Transform(self.author_bar, final_name), run_time=0.6)
        self.play(FadeIn(final_id), FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰：旋转的倾斜线
        deco_lines = VGroup(*[
            Line(
                ORIGIN, np.array([np.cos(i * PI / 5), np.sin(i * PI / 5), 0]) * 1.2,
                color=[C_POS, C_NEG, C_ZERO, C_INF, YELLOW][i % 5],
                stroke_width=3
            ).shift(DOWN * 2.5)
            for i in range(10)
        ])
        self.play(*[GrowFromPoint(l, l.get_start()) for l in deco_lines], run_time=0.7)
        self.play(Rotate(deco_lines, angle=PI / 5, run_time=1.2))

        self.wait(0.8)


# ========== 渲染命令 ==========
# 快速预览: manim -pql slope_inclination.py SlopeAndInclinationAngle
# 高质量:   manim -qh  slope_inclination.py SlopeAndInclinationAngle
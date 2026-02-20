"""
双曲线的几何性质 - Manim 教学动画
Hyperbola: Geometric Properties

内容: 范围、对称性、顶点、离心率、渐近线、准线、等轴双曲线
目标观众: 高二学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class HyperbolaGeometricProperties(Scene):
    """
    双曲线几何性质教学动画
    
    场景顺序:
    1. 开场与回顾
    2. 范围性质
    3. 对称性
    4. 顶点
    5. 离心率
    6. 渐近线详解
    7. 准线
    8. 等轴双曲线
    9. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_HYPERBOLA = "#e74c3c"      # 红色 - 双曲线主体
        self.COLOR_ASYMPTOTE = "#9b59b6"      # 紫色 - 渐近线
        self.COLOR_DIRECTRIX = "#f39c12"      # 橙色 - 准线
        self.COLOR_FOCUS = "#e67e22"          # 深橙 - 焦点
        self.COLOR_ECCENTRICITY = "#3498db"   # 蓝色 - 离心率相关
        self.COLOR_SYMMETRY = "#2ecc71"       # 绿色 - 对称性
        self.COLOR_RANGE = "#00bcd4"          # 青色 - 范围标注
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_range()
        self.scene_3_symmetry()
        self.scene_4_vertices()
        self.scene_5_eccentricity()
        self.scene_6_asymptotes()
        self.scene_7_directrix()
        self.scene_8_equilateral()
        self.scene_9_summary()
    
    def setup_geometry(self):
        """初始化双曲线和所有几何元素"""
        # 双曲线参数
        self.a = 2.0  # 实半轴长
        self.b = 1.5  # 虚半轴长
        self.c = np.sqrt(self.a**2 + self.b**2)  # 半焦距
        self.e = self.c / self.a  # 离心率
        
        # 缩放和偏移
        self.SCALE = 0.65
        self.OFFSET = UP * 1.0
        
        # 焦点位置
        self.F1 = np.array([-self.c, 0, 0]) * self.SCALE + self.OFFSET
        self.F2 = np.array([self.c, 0, 0]) * self.SCALE + self.OFFSET
        
        # 顶点位置
        self.A1 = np.array([-self.a, 0, 0]) * self.SCALE + self.OFFSET
        self.A2 = np.array([self.a, 0, 0]) * self.SCALE + self.OFFSET
        
        # 准线位置
        self.directrix_x = self.a**2 / self.c
        
        # 渐近线斜率
        self.slope = self.b / self.a
        
        print(f"✓ 几何初始化完成: a={self.a}, b={self.b}, c={self.c:.4f}, e={self.e:.4f}")
    
    def hyperbola_point_right(self, t):
        """双曲线右支上的点"""
        x = self.a * np.cosh(t)
        y = self.b * np.sinh(t)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    
    def hyperbola_point_left(self, t):
        """双曲线左支上的点"""
        x = -self.a * np.cosh(t)
        y = self.b * np.sinh(t)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    
    def scene_1_opening(self):
        """场景1: 开场与回顾"""
        # 作者信息（全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "双曲线还有哪些神奇性质?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=0.8)
        self.wait(0.3)
        
        # 基本双曲线
        hyperbola_right = ParametricFunction(
            lambda t: self.hyperbola_point_right(t),
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        )
        
        hyperbola_left = ParametricFunction(
            lambda t: self.hyperbola_point_left(t),
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        )
        
        self.play(
            Create(hyperbola_right),
            Create(hyperbola_left),
            run_time=1.0
        )
        
        # 主标题
        title = Text(
            "双曲线的几何性质",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HYPERBOLA
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook), run_time=0.3)
        
        # 保留双曲线和标题
        self.hyperbola = VGroup(hyperbola_right, hyperbola_left)
        self.title = title
    
    def scene_2_range(self):
        """场景2: 范围性质"""
        # 副标题
        subtitle = Text(
            "性质1: 范围",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_RANGE
        ).move_to(UP * 4.2)
        
        self.play(
            self.title.animate.scale(0.7).move_to(UP * 5.5),
            FadeIn(subtitle),
            run_time=0.4
        )
        
        # 顶点高亮
        A1_dot = Dot(self.A1, color=self.COLOR_RANGE, radius=0.12)
        A2_dot = Dot(self.A2, color=self.COLOR_RANGE, radius=0.12)
        
        self.play(
            FadeIn(A1_dot),
            FadeIn(A2_dot),
            run_time=0.4
        )
        
        self.play(
            Indicate(A1_dot, color=self.COLOR_RANGE),
            Indicate(A2_dot, color=self.COLOR_RANGE),
            run_time=0.6
        )
        
        # x范围边界线
        x_boundary_left = DashedLine(
            self.A1 + UP * 2.5,
            self.A1 + DOWN * 2.5,
            color=self.COLOR_RANGE,
            stroke_width=2,
            dash_length=0.1
        )
        
        x_boundary_right = DashedLine(
            self.A2 + UP * 2.5,
            self.A2 + DOWN * 2.5,
            color=self.COLOR_RANGE,
            stroke_width=2,
            dash_length=0.1
        )
        
        self.play(
            Create(x_boundary_left),
            Create(x_boundary_right),
            run_time=0.8
        )
        
        # x范围公式
        x_range_text = Text("|x| ≥ a", font="Noto Sans CJK SC", font_size=24, color=WHITE).move_to(DOWN * 3.5)
        
        self.play(Write(x_range_text), run_time=0.6)
        
        # y范围箭头
        y_arrow_up = Arrow(
            self.OFFSET,
            self.OFFSET + UP * 2,
            color=self.COLOR_RANGE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        y_arrow_down = Arrow(
            self.OFFSET,
            self.OFFSET + DOWN * 2,
            color=self.COLOR_RANGE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            GrowArrow(y_arrow_up),
            GrowArrow(y_arrow_down),
            run_time=0.6
        )
        
        # y范围公式
        y_range_text = Text("y ∈ ℝ", font="Noto Sans CJK SC", font_size=24, color=WHITE).move_to(DOWN * 4.5)
        
        self.play(Write(y_range_text), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(A1_dot),
            FadeOut(A2_dot),
            FadeOut(x_boundary_left),
            FadeOut(x_boundary_right),
            FadeOut(x_range_text),
            FadeOut(y_arrow_up),
            FadeOut(y_arrow_down),
            FadeOut(y_range_text),
            run_time=0.6
        )
    
    def scene_3_symmetry(self):
        """场景3: 对称性"""
        # 副标题
        subtitle = Text(
            "性质2: 对称性",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SYMMETRY
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 选择双曲线上的点
        P = self.hyperbola_point_right(0.8)
        
        # 对称点
        P_x = np.array([P[0], 2 * self.OFFSET[1] - P[1], 0])  # 关于x轴（y=1）对称
        P_y = np.array([2 * self.OFFSET[0] - P[0], P[1], 0])  # 关于y轴（x=0）对称
        P_origin = 2 * self.OFFSET - P  # 关于原点（0,1）对称
        
        # 创建点
        P_dot = Dot(P, color=self.COLOR_SYMMETRY, radius=0.10)
        P_label = MathTex("P", color=self.COLOR_SYMMETRY, font_size=20).next_to(P_dot, UR, buff=0.1)
        
        # 1. 关于x轴对称
        x_axis_line = DashedLine(LEFT * 4, RIGHT * 4, color=GRAY_A, stroke_width=1).move_to(self.OFFSET)
        
        self.play(Create(x_axis_line), run_time=0.4)
        self.play(FadeIn(P_dot), FadeIn(P_label), run_time=0.3)
        
        P_x_dot = Dot(P_x, color=self.COLOR_SYMMETRY, radius=0.10)
        P_x_label = MathTex("P'", color=self.COLOR_SYMMETRY, font_size=20).next_to(P_x_dot, DR, buff=0.1)
        
        symmetry_line_x = DashedLine(P, P_x, color=self.COLOR_SYMMETRY, stroke_width=2, dash_length=0.08)
        
        self.play(
            FadeIn(P_x_dot),
            FadeIn(P_x_label),
            Create(symmetry_line_x),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 2. 关于y轴对称
        self.play(
            FadeOut(x_axis_line),
            FadeOut(P_x_dot),
            FadeOut(P_x_label),
            FadeOut(symmetry_line_x),
            run_time=0.4
        )
        
        y_axis_line = DashedLine(UP * 3, DOWN * 3, color=GRAY_A, stroke_width=1).move_to(self.OFFSET)
        
        self.play(Create(y_axis_line), run_time=0.4)
        
        Q = self.hyperbola_point_right(1.0)
        Q_y = np.array([2 * self.OFFSET[0] - Q[0], Q[1], 0])
        
        P_dot.move_to(Q)
        P_label.next_to(P_dot, UR, buff=0.1)
        
        Q_y_dot = Dot(Q_y, color=self.COLOR_SYMMETRY, radius=0.10)
        Q_y_label = MathTex("P'", color=self.COLOR_SYMMETRY, font_size=20).next_to(Q_y_dot, UL, buff=0.1)
        
        symmetry_line_y = DashedLine(Q, Q_y, color=self.COLOR_SYMMETRY, stroke_width=2, dash_length=0.08)
        
        self.play(
            FadeIn(Q_y_dot),
            FadeIn(Q_y_label),
            Create(symmetry_line_y),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 3. 关于原点对称
        self.play(
            FadeOut(y_axis_line),
            FadeOut(Q_y_dot),
            FadeOut(Q_y_label),
            FadeOut(symmetry_line_y),
            run_time=0.4
        )
        
        origin_dot = Dot(self.OFFSET, color=YELLOW, radius=0.08)
        
        self.play(FadeIn(origin_dot), run_time=0.3)
        
        R = self.hyperbola_point_right(0.6)
        R_origin = 2 * self.OFFSET - R
        
        P_dot.move_to(R)
        P_label.next_to(P_dot, UR, buff=0.1)
        
        R_origin_dot = Dot(R_origin, color=self.COLOR_SYMMETRY, radius=0.10)
        R_origin_label = MathTex("P'", color=self.COLOR_SYMMETRY, font_size=20).next_to(R_origin_dot, DL, buff=0.1)
        
        symmetry_line_origin = DashedLine(R, R_origin, color=self.COLOR_SYMMETRY, stroke_width=2, dash_length=0.08)
        
        self.play(
            FadeIn(R_origin_dot),
            FadeIn(R_origin_label),
            Create(symmetry_line_origin),
            run_time=0.6
        )
        
        # 说明文字
        explanation = Text(
            "关于x轴、y轴、原点对称",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(P_dot),
            FadeOut(P_label),
            FadeOut(R_origin_dot),
            FadeOut(R_origin_label),
            FadeOut(symmetry_line_origin),
            FadeOut(origin_dot),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def scene_4_vertices(self):
        """场景4: 顶点"""
        # 副标题
        subtitle = Text(
            "性质3: 顶点",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HYPERBOLA
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 顶点
        self.A1_dot = Dot(self.A1, color=self.COLOR_HYPERBOLA, radius=0.12)
        self.A2_dot = Dot(self.A2, color=self.COLOR_HYPERBOLA, radius=0.12)
        
        self.play(
            GrowFromCenter(self.A1_dot),
            GrowFromCenter(self.A2_dot),
            run_time=0.5
        )
        
        self.play(
            self.A1_dot.animate.scale(1.3),
            self.A2_dot.animate.scale(1.3),
            run_time=0.4
        )
        self.play(
            self.A1_dot.animate.scale(1/1.3),
            self.A2_dot.animate.scale(1/1.3),
            run_time=0.4
        )
        
        # 坐标标注
        A1_coords = MathTex("(-a, 0)", color=WHITE, font_size=22).next_to(self.A1_dot, DOWN, buff=0.2)
        A2_coords = MathTex("(a, 0)", color=WHITE, font_size=22).next_to(self.A2_dot, DOWN, buff=0.2)
        
        self.play(
            Write(A1_coords),
            Write(A2_coords),
            run_time=0.6
        )
        
        # 实轴
        real_axis = Line(
            self.A1, self.A2,
            color=self.COLOR_HYPERBOLA,
            stroke_width=4
        )
        
        self.play(Create(real_axis), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "距离原点最近的点",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(A1_coords),
            FadeOut(A2_coords),
            FadeOut(real_axis),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 顶点变小但保留
        self.play(
            self.A1_dot.animate.scale(0.6).set_opacity(0.5),
            self.A2_dot.animate.scale(0.6).set_opacity(0.5),
            run_time=0.3
        )
    
    def scene_5_eccentricity(self):
        """场景5: 离心率"""
        # 副标题
        subtitle = Text(
            "性质4: 离心率",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_ECCENTRICITY
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 公式 e = c/a
        e_formula = MathTex(
            r"e = \frac{c}{a}",
            color=WHITE,
            font_size=32
        ).move_to(UP * 3.2)
        
        self.play(Write(e_formula), run_time=0.6)
        
        # 当前e值
        e_note = Text(
            f"e > 1",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).next_to(e_formula, RIGHT, buff=0.5)
        
        self.play(FadeIn(e_note), run_time=0.4)
        
        # 创建三个不同离心率的双曲线进行对比
        # e = 1.2 (较小)
        a1, b1 = 2.0, 0.9
        
        hyperbola_small_e = VGroup(
            ParametricFunction(
                lambda t: np.array([a1 * np.cosh(t), b1 * np.sinh(t), 0]) * self.SCALE + self.OFFSET,
                t_range=[0, 1.3],
                color=self.COLOR_ECCENTRICITY,
                stroke_width=2
            ),
            ParametricFunction(
                lambda t: np.array([-a1 * np.cosh(t), b1 * np.sinh(t), 0]) * self.SCALE + self.OFFSET,
                t_range=[0, 1.3],
                color=self.COLOR_ECCENTRICITY,
                stroke_width=2
            )
        ).set_opacity(0.3)
        
        # e = 2.0 (较大)
        a2, b2 = 2.0, 3.46
        
        hyperbola_large_e = VGroup(
            ParametricFunction(
                lambda t: np.array([a2 * np.cosh(t), b2 * np.sinh(t), 0]) * self.SCALE + self.OFFSET,
                t_range=[0, 1.0],
                color=self.COLOR_ECCENTRICITY,
                stroke_width=2
            ),
            ParametricFunction(
                lambda t: np.array([-a2 * np.cosh(t), b2 * np.sinh(t), 0]) * self.SCALE + self.OFFSET,
                t_range=[0, 1.0],
                color=self.COLOR_ECCENTRICITY,
                stroke_width=2
            )
        ).set_opacity(0.3)
        
        # 显示对比
        e_small_label = Text("e = 1.2", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_ECCENTRICITY).move_to(UP * 0.5 + LEFT * 2.5)
        
        self.play(
            Create(hyperbola_small_e),
            FadeIn(e_small_label),
            self.hyperbola.animate.set_opacity(0.3),
            run_time=0.8
        )
        
        self.wait(0.4)
        
        e_large_label = Text("e = 2.0", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_ECCENTRICITY).move_to(UP * 0.5 + RIGHT * 2.5)
        
        self.play(
            Create(hyperbola_large_e),
            FadeIn(e_large_label),
            run_time=0.8
        )
        
        # 说明
        explanation = Text(
            "e 越大，开口越大",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(e_formula),
            FadeOut(e_note),
            FadeOut(hyperbola_small_e),
            FadeOut(hyperbola_large_e),
            FadeOut(e_small_label),
            FadeOut(e_large_label),
            FadeOut(explanation),
            self.hyperbola.animate.set_opacity(1.0),
            run_time=0.6
        )
    
    def scene_6_asymptotes(self):
        """场景6: 渐近线详解"""
        # 副标题
        subtitle = Text(
            "性质5: 渐近线",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_ASYMPTOTE
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 虚框
        rectangle = Rectangle(
            width=2 * self.a * self.SCALE,
            height=2 * self.b * self.SCALE,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        ).move_to(self.OFFSET)
        
        rectangle_dashed = DashedVMobject(rectangle, num_dashes=40)
        
        self.play(Create(rectangle_dashed), run_time=0.6)
        
        # 渐近线
        x_range = 4.0
        
        asymptote_1 = Line(
            self.OFFSET + np.array([-x_range, -self.slope * x_range, 0]),
            self.OFFSET + np.array([x_range, self.slope * x_range, 0]),
            color=self.COLOR_ASYMPTOTE,
            stroke_width=3
        )
        
        asymptote_2 = Line(
            self.OFFSET + np.array([-x_range, self.slope * x_range, 0]),
            self.OFFSET + np.array([x_range, -self.slope * x_range, 0]),
            color=self.COLOR_ASYMPTOTE,
            stroke_width=3
        )
        
        self.play(
            Create(asymptote_1),
            Create(asymptote_2),
            run_time=0.8
        )
        
        # 方程
        asymptote_text = Text("y = ±", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        asymptote_eq = MathTex(r"\frac{b}{a}x", font_size=24, color=WHITE)
        asymptote_formula = VGroup(asymptote_text, asymptote_eq).arrange(RIGHT, buff=0.1).move_to(UP * 3)
        
        self.play(Write(asymptote_formula), run_time=0.6)
        
        # 动点沿双曲线移动，标注距离
        P_dot = Dot(color=self.COLOR_HIGHLIGHT, radius=0.08)
        P_dot.move_to(self.hyperbola_point_right(0.5))
        
        # 距离标签
        distance_label = always_redraw(
            lambda: Text(
                f"d ≈ {self.distance_to_asymptote(P_dot.get_center()):.2f}",
                font="Noto Sans CJK SC",
                font_size=18,
                color=self.COLOR_HIGHLIGHT
            ).next_to(P_dot, UR, buff=0.1)
        )
        
        self.play(
            FadeIn(P_dot),
            FadeIn(distance_label),
            run_time=0.4
        )
        
        # P点移动
        path = ParametricFunction(
            lambda t: self.hyperbola_point_right(t),
            t_range=[0.5, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=0
        )
        
        self.play(
            MoveAlongPath(P_dot, path),
            run_time=2.5,
            rate_func=linear
        )
        
        # 说明
        explanation = Text(
            "无限接近但永不相交",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(rectangle_dashed),
            FadeOut(P_dot),
            FadeOut(distance_label),
            FadeOut(explanation),
            FadeOut(asymptote_formula),
            run_time=0.6
        )
        
        # 保留渐近线
        self.asymptote_1 = asymptote_1
        self.asymptote_2 = asymptote_2
    
    def distance_to_asymptote(self, point):
        """计算点到渐近线的距离"""
        x = (point[0] - self.OFFSET[0]) / self.SCALE
        y = (point[1] - self.OFFSET[1]) / self.SCALE
        
        distance = abs(self.b * x - self.a * y) / np.sqrt(self.a**2 + self.b**2)
        return distance
    
    def scene_7_directrix(self):
        """场景7: 准线"""
        # 副标题
        subtitle = Text(
            "性质6: 准线",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_DIRECTRIX
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 焦点
        F1_dot = Dot(self.F1, color=self.COLOR_FOCUS, radius=0.10)
        F2_dot = Dot(self.F2, color=self.COLOR_FOCUS, radius=0.10)
        
        F2_label = MathTex("F_2", color=self.COLOR_FOCUS, font_size=20).next_to(F2_dot, DOWN, buff=0.1)
        
        self.play(
            FadeIn(F1_dot),
            FadeIn(F2_dot),
            FadeIn(F2_label),
            run_time=0.4
        )
        
        # 准线
        directrix_left = DashedLine(
            np.array([-self.directrix_x, -3, 0]) * self.SCALE + np.array([self.OFFSET[0], self.OFFSET[1], 0]),
            np.array([-self.directrix_x, 3, 0]) * self.SCALE + np.array([self.OFFSET[0], self.OFFSET[1], 0]),
            color=self.COLOR_DIRECTRIX,
            stroke_width=2,
            dash_length=0.1
        )
        
        directrix_right = DashedLine(
            np.array([self.directrix_x, -3, 0]) * self.SCALE + np.array([self.OFFSET[0], self.OFFSET[1], 0]),
            np.array([self.directrix_x, 3, 0]) * self.SCALE + np.array([self.OFFSET[0], self.OFFSET[1], 0]),
            color=self.COLOR_DIRECTRIX,
            stroke_width=2,
            dash_length=0.1
        )
        
        self.play(
            Create(directrix_left),
            Create(directrix_right),
            run_time=0.8
        )
        
        # 方程
        directrix_text = Text("x = ±", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        directrix_eq = MathTex(r"\frac{a^2}{c}", font_size=22, color=WHITE)
        directrix_formula = VGroup(directrix_text, directrix_eq).arrange(RIGHT, buff=0.1).move_to(UP * 3)
        
        self.play(Write(directrix_formula), run_time=0.6)
        
        # 选点P
        P = self.hyperbola_point_right(0.6)
        P_dot = Dot(P, color=self.COLOR_HIGHLIGHT, radius=0.10)
        P_label = MathTex("P", color=self.COLOR_HIGHLIGHT, font_size=20).next_to(P_dot, UR, buff=0.1)
        
        self.play(
            FadeIn(P_dot),
            FadeIn(P_label),
            run_time=0.4
        )
        
        # PF2线段
        PF2_line = Line(P, self.F2, color=self.COLOR_FOCUS, stroke_width=2)
        
        self.play(Create(PF2_line), run_time=0.5)
        
        # 垂线到准线
        directrix_x_pos = self.directrix_x * self.SCALE + self.OFFSET[0]
        perpendicular_foot = np.array([directrix_x_pos, P[1], 0])
        
        perpendicular_line = DashedLine(
            P, perpendicular_foot,
            color=self.COLOR_DIRECTRIX,
            stroke_width=2,
            dash_length=0.08
        )
        
        self.play(Create(perpendicular_line), run_time=0.5)
        
        # 比值公式
        ratio_text = Text("|PF|/d = e", font="Noto Sans CJK SC", font_size=22, color=WHITE).move_to(DOWN * 5)
        
        self.play(Write(ratio_text), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(F1_dot),
            FadeOut(F2_dot),
            FadeOut(F2_label),
            FadeOut(directrix_left),
            FadeOut(directrix_right),
            FadeOut(directrix_formula),
            FadeOut(P_dot),
            FadeOut(P_label),
            FadeOut(PF2_line),
            FadeOut(perpendicular_line),
            FadeOut(ratio_text),
            run_time=0.6
        )
    
    def scene_8_equilateral(self):
        """场景8: 等轴双曲线"""
        # 副标题
        subtitle = Text(
            "特殊情况: 等轴双曲线",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 条件
        condition = Text("当 a = b 时", font="Noto Sans CJK SC", font_size=26, color=WHITE).move_to(UP * 3.2)
        
        self.play(Write(condition), run_time=0.5)
        
        # 变换到等轴双曲线
        a_eq = b_eq = 1.5
        
        equilateral_right = ParametricFunction(
            lambda t: np.array([a_eq * np.cosh(t), b_eq * np.sinh(t), 0]) * self.SCALE + self.OFFSET,
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        )
        
        equilateral_left = ParametricFunction(
            lambda t: np.array([-a_eq * np.cosh(t), b_eq * np.sinh(t), 0]) * self.SCALE + self.OFFSET,
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        )
        
        equilateral_hyperbola = VGroup(equilateral_right, equilateral_left)
        
        self.play(
            Transform(self.hyperbola, equilateral_hyperbola),
            run_time=1.0
        )
        
        # 渐近线 y = ±x
        asymptote_eq_1 = Line(
            self.OFFSET + np.array([-3, -3, 0]),
            self.OFFSET + np.array([3, 3, 0]),
            color=self.COLOR_ASYMPTOTE,
            stroke_width=3
        )
        
        asymptote_eq_2 = Line(
            self.OFFSET + np.array([-3, 3, 0]),
            self.OFFSET + np.array([3, -3, 0]),
            color=self.COLOR_ASYMPTOTE,
            stroke_width=3
        )
        
        self.play(
            Transform(self.asymptote_1, asymptote_eq_1),
            Transform(self.asymptote_2, asymptote_eq_2),
            run_time=0.8
        )
        
        # 方程
        asymptote_eq = Text("y = ±x", font="Noto Sans CJK SC", font_size=24, color=WHITE).move_to(UP * 2)
        
        self.play(Write(asymptote_eq), run_time=0.5)
        
        # 标记垂直角
        right_angle_size = 0.3
        right_angle = VGroup(
            Line(self.OFFSET + UP * right_angle_size, self.OFFSET + UP * right_angle_size + RIGHT * right_angle_size, color=YELLOW, stroke_width=2),
            Line(self.OFFSET + UP * right_angle_size + RIGHT * right_angle_size, self.OFFSET + RIGHT * right_angle_size, color=YELLOW, stroke_width=2)
        )
        
        self.play(Create(right_angle), run_time=0.6)
        
        # e = √2
        e_value = MathTex(r"e = \sqrt{2}", color=WHITE, font_size=28).move_to(UP * 0.5)
        
        self.play(Write(e_value), run_time=0.6)
        
        # 说明
        explanation = Text(
            "渐近线互相垂直",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理所有元素准备总结
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info],
            run_time=0.6
        )
    
    def scene_9_summary(self):
        """场景9: 总结与关注"""
        # 总结标题
        summary_title = Text(
            "双曲线几何性质回顾",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 性质卡片
        property_1_text = Text("① 范围: ", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        property_1_eq = Text("|x| ≥ a, y ∈ ℝ", font="Noto Sans CJK SC", font_size=20)
        property_1 = VGroup(property_1_text, property_1_eq).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)
        
        property_2 = Text("② 对称性: 关于x轴、y轴、原点对称", font="Noto Sans CJK SC", font_size=20).move_to(UP * 2.5)
        
        property_3_text = Text("③ 离心率: ", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        property_3_eq = MathTex(r"e = \frac{c}{a} > 1", font_size=20)
        property_3 = VGroup(property_3_text, property_3_eq).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)
        
        property_4_text = Text("④ 渐近线: ", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        property_4_eq = MathTex(r"y = \pm \frac{b}{a}x", font_size=20)
        property_4 = VGroup(property_4_text, property_4_eq).arrange(RIGHT, buff=0.1).move_to(UP * 0.5)
        
        property_5_text = Text("⑤ 准线: ", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        property_5_eq = MathTex(r"x = \pm \frac{a^2}{c}", font_size=20)
        property_5 = VGroup(property_5_text, property_5_eq).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.5)
        
        property_6_text = Text("⑥ 等轴: ", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        property_6_eq = MathTex(r"a=b, \; e=\sqrt{2}", font_size=20)
        property_6 = VGroup(property_6_text, property_6_eq).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.5)
        
        properties = VGroup(property_1, property_2, property_3, property_4, property_5, property_6)
        
        # 卡片依次滑入
        for prop in properties:
            prop.shift(LEFT * 10)
            self.play(prop.animate.shift(RIGHT * 10), run_time=0.4)
            self.wait(0.1)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(properties),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 结束
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql hyperbola_properties.py HyperbolaGeometricProperties  # 快速预览
# manim -qh hyperbola_properties.py HyperbolaGeometricProperties   # 高质量 1080p
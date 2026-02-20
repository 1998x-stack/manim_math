"""
双曲线的定义与标准方程 - Manim 教学动画
Hyperbola: Definition and Standard Equation

内容: 双曲线的定义、关键参数、标准方程、渐近线
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


class HyperbolaDefinitionAndEquation(Scene):
    """
    双曲线定义与标准方程教学动画
    
    场景顺序:
    1. 开场钩子
    2. 双曲线定义
    3. 关键参数 a, b, c
    4. 标准方程（焦点在x轴）
    5. 渐近线
    6. 焦点在y轴
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_HYPERBOLA = "#e74c3c"      # 红色 - 双曲线主体
        self.COLOR_FOCUS = "#f39c12"          # 橙色 - 焦点
        self.COLOR_AXIS_REAL = "#3498db"      # 蓝色 - 实轴
        self.COLOR_AXIS_IMAGINARY = "#2ecc71" # 绿色 - 虚轴
        self.COLOR_ASYMPTOTE = "#9b59b6"      # 紫色 - 渐近线
        self.COLOR_POINT_P = "#e91e63"        # 粉色 - 动点P
        self.COLOR_DISTANCE = "#00bcd4"       # 青色 - 距离线
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_parameters()
        self.scene_4_standard_equation()
        self.scene_5_asymptotes()
        self.scene_6_y_axis_case()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化双曲线和所有几何元素"""
        # 双曲线参数
        self.a = 2.0  # 实半轴长
        self.b = 1.5  # 虚半轴长
        self.c = np.sqrt(self.a**2 + self.b**2)  # 半焦距
        
        # 缩放和偏移（基于验证结果）
        self.SCALE = 0.65
        self.OFFSET = UP * 1.0
        
        # 焦点位置
        self.F1 = np.array([-self.c, 0, 0]) * self.SCALE + self.OFFSET
        self.F2 = np.array([self.c, 0, 0]) * self.SCALE + self.OFFSET
        
        # 顶点位置
        self.A1 = np.array([-self.a, 0, 0]) * self.SCALE + self.OFFSET
        self.A2 = np.array([self.a, 0, 0]) * self.SCALE + self.OFFSET
        
        # 验证几何关系
        self.verify_geometry()
        
        print(f"✓ 几何初始化完成: a={self.a}, b={self.b}, c={self.c:.4f}")
    
    def verify_geometry(self):
        """验证几何关系"""
        epsilon = 1e-6
        
        # 验证 c² = a² + b²
        c_squared = self.c**2
        ab_squared = self.a**2 + self.b**2
        
        if abs(c_squared - ab_squared) > epsilon:
            raise ValueError(f"几何关系错误: c²={c_squared:.6f}, a²+b²={ab_squared:.6f}")
        
        print("✓ 几何验证通过")
    
    def hyperbola_point_right(self, t):
        """双曲线右支上的点（参数方程）"""
        x = self.a * np.cosh(t)
        y = self.b * np.sinh(t)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    
    def hyperbola_point_left(self, t):
        """双曲线左支上的点（参数方程）"""
        x = -self.a * np.cosh(t)
        y = self.b * np.sinh(t)
        return np.array([x, y, 0]) * self.SCALE + self.OFFSET
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部，全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "什么曲线有两个分支?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # 双曲线预览（半透明）
        hyperbola_preview_right = ParametricFunction(
            lambda t: self.hyperbola_point_right(t),
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        ).set_opacity(0.5)
        
        hyperbola_preview_left = ParametricFunction(
            lambda t: self.hyperbola_point_left(t),
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        ).set_opacity(0.5)
        
        self.play(
            Create(hyperbola_preview_right),
            Create(hyperbola_preview_left),
            run_time=1.5
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hyperbola_preview_right),
            FadeOut(hyperbola_preview_left),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 双曲线定义"""
        # 标题
        title = Text(
            "双曲线的定义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HYPERBOLA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 焦点 F₁, F₂
        self.F1_dot = Dot(self.F1, color=self.COLOR_FOCUS, radius=0.12)
        self.F2_dot = Dot(self.F2, color=self.COLOR_FOCUS, radius=0.12)
        
        F1_label = MathTex("F_1", color=self.COLOR_FOCUS, font_size=28).next_to(self.F1_dot, DOWN, buff=0.15)
        F2_label = MathTex("F_2", color=self.COLOR_FOCUS, font_size=28).next_to(self.F2_dot, DOWN, buff=0.15)
        
        self.play(
            FadeIn(self.F1_dot),
            FadeIn(self.F2_dot),
            run_time=0.4
        )
        self.play(
            Write(F1_label),
            Write(F2_label),
            run_time=0.4
        )
        
        # 创建双曲线路径（右支）
        hyperbola_path = ParametricFunction(
            lambda t: self.hyperbola_point_right(t),
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=2
        ).set_opacity(0.3)
        
        self.play(Create(hyperbola_path), run_time=1.0)
        
        # 动点 P
        P_dot = Dot(color=self.COLOR_POINT_P, radius=0.10)
        P_label = MathTex("P", color=self.COLOR_POINT_P, font_size=24).next_to(P_dot, UR, buff=0.1)
        
        # 距离线段
        line_PF1 = always_redraw(
            lambda: Line(
                P_dot.get_center(),
                self.F1_dot.get_center(),
                color=self.COLOR_DISTANCE,
                stroke_width=2
            )
        )
        
        line_PF2 = always_redraw(
            lambda: Line(
                P_dot.get_center(),
                self.F2_dot.get_center(),
                color=self.COLOR_DISTANCE,
                stroke_width=2
            )
        )
        
        # 距离标签
        dist_label_1 = always_redraw(
            lambda: MathTex(
                f"{np.linalg.norm(P_dot.get_center() - self.F1_dot.get_center()):.1f}",
                color=self.COLOR_DISTANCE,
                font_size=18
            ).next_to(line_PF1.get_center(), UL, buff=0.05)
        )
        
        dist_label_2 = always_redraw(
            lambda: MathTex(
                f"{np.linalg.norm(P_dot.get_center() - self.F2_dot.get_center()):.1f}",
                color=self.COLOR_DISTANCE,
                font_size=18
            ).next_to(line_PF2.get_center(), UR, buff=0.05)
        )
        
        # 初始化P点位置
        P_dot.move_to(self.hyperbola_point_right(0.5))
        P_label.next_to(P_dot, UR, buff=0.1)
        
        self.play(
            FadeIn(P_dot),
            FadeIn(P_label),
            run_time=0.4
        )
        
        self.play(
            Create(line_PF1),
            Create(line_PF2),
            run_time=0.4
        )
        
        self.play(
            FadeIn(dist_label_1),
            FadeIn(dist_label_2),
            run_time=0.4
        )
        
        # P点沿双曲线移动
        self.play(
            MoveAlongPath(P_dot, hyperbola_path),
            run_time=4.0,
            rate_func=smooth
        )
        
        # 定义公式
        definition_formula = MathTex(
            r"||PF_1| - |PF_2|| = 2a",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 4.5)
        
        # 高亮定义公式
        formula_box = SurroundingRectangle(
            definition_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(
            Write(definition_formula),
            Create(formula_box),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(P_dot),
            FadeOut(P_label),
            FadeOut(line_PF1),
            FadeOut(line_PF2),
            FadeOut(dist_label_1),
            FadeOut(dist_label_2),
            FadeOut(hyperbola_path),
            FadeOut(formula_box),
            run_time=0.6
        )
        
        # 保留定义公式，移到顶部
        self.definition_formula = definition_formula
        self.play(
            self.definition_formula.animate.scale(0.7).move_to(UP * 4.8 + LEFT * 2),
            FadeOut(F1_label),
            FadeOut(F2_label),
            run_time=0.4
        )
    
    def scene_3_parameters(self):
        """场景3: 关键参数 a, b, c"""
        # 标题
        title = Text(
            "关键参数",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 实轴（蓝色）
        real_axis = Line(
            self.A1, self.A2,
            color=self.COLOR_AXIS_REAL,
            stroke_width=5
        )
        
        self.play(Create(real_axis), run_time=1.0)
        
        # 标注 a
        a_brace = Brace(
            Line(self.OFFSET, self.A2),
            direction=DOWN,
            buff=0.1,
            color=self.COLOR_AXIS_REAL
        )
        a_label = MathTex("a", color=self.COLOR_AXIS_REAL, font_size=28).next_to(a_brace, DOWN, buff=0.05)
        
        self.play(
            GrowFromCenter(a_brace),
            Write(a_label),
            run_time=0.6
        )
        
        # 虚轴（绿色，虚线）
        imaginary_axis_top = DashedLine(
            self.OFFSET,
            self.OFFSET + UP * self.b * self.SCALE,
            color=self.COLOR_AXIS_IMAGINARY,
            stroke_width=3,
            dash_length=0.1
        )
        
        imaginary_axis_bottom = DashedLine(
            self.OFFSET,
            self.OFFSET + DOWN * self.b * self.SCALE,
            color=self.COLOR_AXIS_IMAGINARY,
            stroke_width=3,
            dash_length=0.1
        )
        
        self.play(
            Create(imaginary_axis_top),
            Create(imaginary_axis_bottom),
            run_time=0.8
        )
        
        # 标注 b
        b_brace = Brace(
            Line(self.OFFSET, self.OFFSET + UP * self.b * self.SCALE),
            direction=RIGHT,
            buff=0.1,
            color=self.COLOR_AXIS_IMAGINARY
        )
        b_label = MathTex("b", color=self.COLOR_AXIS_IMAGINARY, font_size=28).next_to(b_brace, RIGHT, buff=0.05)
        
        self.play(
            GrowFromCenter(b_brace),
            Write(b_label),
            run_time=0.6
        )
        
        # 高亮焦距
        focal_distance = Line(
            self.F1, self.F2,
            color=self.COLOR_FOCUS,
            stroke_width=5
        )
        
        self.play(
            Indicate(self.F1_dot, color=self.COLOR_FOCUS),
            Indicate(self.F2_dot, color=self.COLOR_FOCUS),
            run_time=0.6
        )
        
        self.play(Create(focal_distance), run_time=0.6)
        
        # 标注 c
        c_brace = Brace(
            Line(self.OFFSET, self.F2),
            direction=UP,
            buff=0.1,
            color=self.COLOR_FOCUS
        )
        c_label = MathTex("c", color=self.COLOR_FOCUS, font_size=28).next_to(c_brace, UP, buff=0.05)
        
        self.play(
            GrowFromCenter(c_brace),
            Write(c_label),
            run_time=0.6
        )
        
        # 关系式 c² = a² + b²
        relation_formula = MathTex(
            r"c^2 = a^2 + b^2",
            color=WHITE,
            font_size=32
        ).move_to(DOWN * 4.5)
        
        relation_box = SurroundingRectangle(
            relation_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(
            Write(relation_formula),
            Create(relation_box),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(a_brace),
            FadeOut(b_brace),
            FadeOut(c_brace),
            FadeOut(a_label),
            FadeOut(b_label),
            FadeOut(c_label),
            FadeOut(focal_distance),
            FadeOut(relation_box),
            run_time=0.6
        )
        
        # 保留实轴、虚轴和关系式
        self.real_axis = real_axis
        self.imaginary_axis = VGroup(imaginary_axis_top, imaginary_axis_bottom)
        self.relation_formula = relation_formula
        
        self.play(
            self.relation_formula.animate.scale(0.7).move_to(UP * 4.8 + RIGHT * 2),
            run_time=0.4
        )
    
    def scene_4_standard_equation(self):
        """场景4: 标准方程（焦点在x轴）"""
        # 标题
        title = Text(
            "标准方程（焦点在x轴）",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HYPERBOLA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to(self.OFFSET + DOWN * 0.5)
        
        # 不显示数字，保持简洁
        self.play(Create(axes), run_time=0.8)
        
        # 绘制双曲线（右支）
        hyperbola_right = ParametricFunction(
            lambda t: np.array([
                self.a * np.cosh(t),
                self.b * np.sinh(t),
                0
            ]) * self.SCALE + self.OFFSET + DOWN * 0.5,
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=4
        )
        
        # 绘制双曲线（左支）
        hyperbola_left = ParametricFunction(
            lambda t: np.array([
                -self.a * np.cosh(t),
                self.b * np.sinh(t),
                0
            ]) * self.SCALE + self.OFFSET + DOWN * 0.5,
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=4
        )
        
        self.play(Create(hyperbola_right), run_time=1.5)
        self.play(Create(hyperbola_left), run_time=1.5)
        
        # 标准方程
        standard_eq = MathTex(
            r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 4.5)
        
        eq_box = SurroundingRectangle(
            standard_eq,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(
            Write(standard_eq),
            Create(eq_box),
            run_time=1.0
        )
        
        # 标注焦点坐标
        focus_coords = MathTex(
            r"F_1(-c, 0), \quad F_2(c, 0)",
            color=self.COLOR_FOCUS,
            font_size=24
        ).move_to(DOWN * 5.8)
        
        self.play(
            Indicate(self.F1_dot, color=self.COLOR_FOCUS),
            Indicate(self.F2_dot, color=self.COLOR_FOCUS),
            FadeIn(focus_coords),
            run_time=0.8
        )
        
        # 标注顶点
        A1_dot = Dot(self.A1 + DOWN * 0.5, color=self.COLOR_AXIS_REAL, radius=0.08)
        A2_dot = Dot(self.A2 + DOWN * 0.5, color=self.COLOR_AXIS_REAL, radius=0.08)
        
        vertex_coords = MathTex(
            r"A_1(-a, 0), \quad A_2(a, 0)",
            color=self.COLOR_AXIS_REAL,
            font_size=24
        ).move_to(DOWN * 6.5)
        
        self.play(
            FadeIn(A1_dot),
            FadeIn(A2_dot),
            FadeIn(vertex_coords),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(eq_box),
            FadeOut(focus_coords),
            FadeOut(vertex_coords),
            FadeOut(A1_dot),
            FadeOut(A2_dot),
            run_time=0.6
        )
        
        # 保留坐标系、双曲线和方程
        self.axes = axes
        self.hyperbola_right = hyperbola_right
        self.hyperbola_left = hyperbola_left
        self.standard_eq = standard_eq
        
        self.play(
            self.standard_eq.animate.scale(0.65).move_to(UP * 4.2),
            run_time=0.4
        )
    
    def scene_5_asymptotes(self):
        """场景5: 渐近线"""
        # 标题
        title = Text(
            "渐近线",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ASYMPTOTE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 虚框（2a × 2b矩形）
        offset_adjusted = self.OFFSET + DOWN * 0.5
        rectangle = Rectangle(
            width=2 * self.a * self.SCALE,
            height=2 * self.b * self.SCALE,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        ).move_to(offset_adjusted).set_opacity(0.5)
        
        rectangle_dashed = DashedVMobject(rectangle, num_dashes=40)
        
        self.play(Create(rectangle_dashed), run_time=0.8)
        
        # 计算渐近线端点
        slope = self.b / self.a
        x_range = 4.0  # 延伸范围
        
        # 渐近线1: y = (b/a)x
        asymptote_1 = Line(
            offset_adjusted + np.array([-x_range, -slope * x_range, 0]),
            offset_adjusted + np.array([x_range, slope * x_range, 0]),
            color=self.COLOR_ASYMPTOTE,
            stroke_width=3
        )
        
        # 渐近线2: y = -(b/a)x
        asymptote_2 = Line(
            offset_adjusted + np.array([-x_range, slope * x_range, 0]),
            offset_adjusted + np.array([x_range, -slope * x_range, 0]),
            color=self.COLOR_ASYMPTOTE,
            stroke_width=3
        )
        
        self.play(Create(asymptote_1), run_time=0.6)
        self.play(Create(asymptote_2), run_time=0.6)
        
        # 渐近线方程
        asymptote_eq = MathTex(
            r"y = \pm \frac{b}{a}x",
            color=self.COLOR_ASYMPTOTE,
            font_size=32
        ).move_to(DOWN * 4.8)
        
        self.play(Write(asymptote_eq), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "双曲线无限接近但不相交",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rectangle_dashed),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 保留渐近线
        self.asymptote_1 = asymptote_1
        self.asymptote_2 = asymptote_2
        self.asymptote_eq = asymptote_eq
        
        self.play(
            self.asymptote_eq.animate.scale(0.7).move_to(DOWN * 4.5 + LEFT * 2),
            run_time=0.4
        )
    
    def scene_6_y_axis_case(self):
        """场景6: 焦点在y轴的情况"""
        # 清空场景（保留作者信息）
        self.play(
            FadeOut(self.axes),
            FadeOut(self.hyperbola_right),
            FadeOut(self.hyperbola_left),
            FadeOut(self.real_axis),
            FadeOut(self.imaginary_axis),
            FadeOut(self.F1_dot),
            FadeOut(self.F2_dot),
            FadeOut(self.asymptote_1),
            FadeOut(self.asymptote_2),
            FadeOut(self.definition_formula),
            FadeOut(self.relation_formula),
            FadeOut(self.standard_eq),
            FadeOut(self.asymptote_eq),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "焦点在y轴",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HYPERBOLA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 坐标系
        axes_y = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to(UP * 0.5)
        
        self.play(Create(axes_y), run_time=0.6)
        
        # 双曲线（焦点在y轴）- 上支
        hyperbola_y_upper = ParametricFunction(
            lambda t: np.array([
                self.b * np.sinh(t),
                self.a * np.cosh(t),
                0
            ]) * self.SCALE + UP * 0.5,
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=4
        )
        
        # 双曲线（焦点在y轴）- 下支
        hyperbola_y_lower = ParametricFunction(
            lambda t: np.array([
                self.b * np.sinh(t),
                -self.a * np.cosh(t),
                0
            ]) * self.SCALE + UP * 0.5,
            t_range=[0, 1.5],
            color=self.COLOR_HYPERBOLA,
            stroke_width=4
        )
        
        self.play(
            Create(hyperbola_y_upper),
            Create(hyperbola_y_lower),
            run_time=2.0
        )
        
        # 标准方程
        standard_eq_y = MathTex(
            r"\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1",
            color=WHITE,
            font_size=36
        ).move_to(DOWN * 4)
        
        eq_box_y = SurroundingRectangle(
            standard_eq_y,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(
            Write(standard_eq_y),
            Create(eq_box_y),
            run_time=1.0
        )
        
        # 焦点和顶点标注
        F1_y_dot = Dot(UP * 0.5 + DOWN * self.c * self.SCALE, color=self.COLOR_FOCUS, radius=0.10)
        F2_y_dot = Dot(UP * 0.5 + UP * self.c * self.SCALE, color=self.COLOR_FOCUS, radius=0.10)
        
        coords_y = MathTex(
            r"F_1(0, -c), \; F_2(0, c)",
            color=self.COLOR_FOCUS,
            font_size=24
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(F1_y_dot),
            FadeIn(F2_y_dot),
            FadeIn(coords_y),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理所有元素（准备总结）
        self.play(
            FadeOut(title),
            FadeOut(axes_y),
            FadeOut(hyperbola_y_upper),
            FadeOut(hyperbola_y_lower),
            FadeOut(standard_eq_y),
            FadeOut(eq_box_y),
            FadeOut(F1_y_dot),
            FadeOut(F2_y_dot),
            FadeOut(coords_y),
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结与关注"""
        # 总结标题
        summary_title = Text(
            "双曲线核心公式",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 关键公式卡片 - 使用中英文分离
        # 公式1: 定义
        def_text = Text("定义:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        def_formula = MathTex(r"||PF_1| - |PF_2|| = 2a", font_size=24)
        formula_1 = VGroup(def_text, def_formula).arrange(RIGHT, buff=0.3).move_to(UP * 3)
        
        # 公式2: 焦点在x轴
        x_text = Text("焦点在x轴:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        x_formula = MathTex(r"\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1", font_size=24)
        formula_2 = VGroup(x_text, x_formula).arrange(RIGHT, buff=0.3).move_to(UP * 2)
        
        # 公式3: 焦点在y轴
        y_text = Text("焦点在y轴:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        y_formula = MathTex(r"\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1", font_size=24)
        formula_3 = VGroup(y_text, y_formula).arrange(RIGHT, buff=0.3).move_to(UP * 1)
        
        # 公式4: 关系
        rel_text = Text("关系:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        rel_formula = MathTex(r"c^2 = a^2 + b^2", font_size=24)
        formula_4 = VGroup(rel_text, rel_formula).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        
        formulas = VGroup(formula_1, formula_2, formula_3, formula_4)
        
        # 卡片依次滑入
        for formula in formulas:
            formula.shift(LEFT * 10)  # 初始位置在左侧外
            self.play(formula.animate.shift(RIGHT * 10), run_time=0.5)
            self.wait(0.2)
        
        self.wait(1.0)
        
        # 清理公式
        self.play(
            FadeOut(summary_title),
            FadeOut(formulas),
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
        
        # 双曲线图标装饰
        icon_hyperbola_1 = ParametricFunction(
            lambda t: np.array([0.3 * np.cosh(t), 0.2 * np.sinh(t), 0]) + DOWN * 3 + LEFT * 2,
            t_range=[0, 1.2],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        )
        
        icon_hyperbola_2 = ParametricFunction(
            lambda t: np.array([-0.3 * np.cosh(t), 0.2 * np.sinh(t), 0]) + DOWN * 3 + LEFT * 2,
            t_range=[0, 1.2],
            color=self.COLOR_HYPERBOLA,
            stroke_width=3
        )
        
        icon_hyperbola_3 = icon_hyperbola_1.copy().shift(RIGHT * 4)
        icon_hyperbola_4 = icon_hyperbola_2.copy().shift(RIGHT * 4)
        
        self.play(
            Create(icon_hyperbola_1),
            Create(icon_hyperbola_2),
            Create(icon_hyperbola_3),
            Create(icon_hyperbola_4),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 结束
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql hyperbola.py HyperbolaDefinitionAndEquation  # 快速预览 480p
# manim -qm hyperbola.py HyperbolaDefinitionAndEquation   # 中等质量 720p
# manim -qh hyperbola.py HyperbolaDefinitionAndEquation   # 高质量 1080p
# manim -qk hyperbola.py HyperbolaDefinitionAndEquation   # 4K质量
"""
二次函数待定系数法教学动画
Quadratic Function: Undetermined Coefficients Method

内容: 用待定系数法求二次函数解析式的三种方法
目标观众: 九年级学生
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


class QuadraticUndeterminedCoefficients(Scene):
    """
    二次函数待定系数法教学动画
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. 方法一：一般式 y=ax²+bx+c
    4. 方法二：顶点式 y=a(x-h)²+k
    5. 方法三：交点式 y=a(x-x₁)(x-x₂)
    6. 三种方法对比
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要曲线
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 重点标注
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮提示
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_GENERAL_FORM = "#2ecc71"   # 绿色 - 一般式
        self.COLOR_VERTEX_FORM = "#9b59b6"    # 紫色 - 顶点式
        self.COLOR_INTERCEPT_FORM = "#f39c12" # 橙色 - 交点式
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_axes_setup()
        self.show_general_form()
        self.show_vertex_form()
        self.show_intercept_form()
        self.show_comparison()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化坐标系和所有几何元素"""
        # 坐标系配置
        self.axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 10, 1],
            x_length=7,
            y_length=9,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15
            },
            x_axis_config={"numbers_to_include": np.arange(-4, 5, 2)},
            y_axis_config={"numbers_to_include": np.arange(-4, 10, 2)}
        ).scale(0.65).move_to(UP * 0.8)
        
        # 示例抛物线: y = x² - 2x - 3
        self.parabola_func = lambda x: x**2 - 2*x - 3
        
        # 精确计算关键点坐标（在坐标系中的位置）
        # 三个用于一般式的点
        self.coord_A = np.array([0, -3])   # (0, -3)
        self.coord_B = np.array([1, -4])   # (1, -4)
        self.coord_C = np.array([2, -3])   # (2, -3)
        
        # 顶点
        self.coord_vertex = np.array([1, -4])  # (1, -4)
        
        # x轴交点
        self.coord_x1 = np.array([-1, 0])  # (-1, 0)
        self.coord_x2 = np.array([3, 0])   # (3, 0)
        
        # 验证计算
        self.verify_coordinates()
    
    def verify_coordinates(self):
        """验证所有坐标点是否在抛物线上"""
        epsilon = 1e-6
        
        # 验证三个点在抛物线上
        for name, coord in [("A", self.coord_A), ("B", self.coord_B), ("C", self.coord_C)]:
            x, y = coord
            y_calc = self.parabola_func(x)
            if abs(y - y_calc) > epsilon:
                print(f"WARNING: 点{name}({x}, {y})不在抛物线上! 计算值: {y_calc}")
        
        # 验证顶点
        x, y = self.coord_vertex
        y_calc = self.parabola_func(x)
        if abs(y - y_calc) > epsilon:
            print(f"WARNING: 顶点({x}, {y})不在抛物线上! 计算值: {y_calc}")
        
        # 验证x轴交点
        for name, coord in [("x1", self.coord_x1), ("x2", self.coord_x2)]:
            x, y = coord
            y_calc = self.parabola_func(x)
            if abs(y_calc) > epsilon:
                print(f"WARNING: 交点{name}({x}, {y})不在x轴上! y值: {y_calc}")
        
        print("✓ 坐标验证完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "三种方法，一个目标！",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.9)
        
        # 三个抛物线快闪（不同颜色）
        temp_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 5, 1],
            x_length=2,
            y_length=2.5,
            axis_config={"include_tip": False, "stroke_width": 1}
        ).scale(0.5)
        
        parabolas = VGroup()
        colors = [self.COLOR_GENERAL_FORM, self.COLOR_VERTEX_FORM, self.COLOR_INTERCEPT_FORM]
        positions = [LEFT * 2.5 + UP * 2, ORIGIN + UP * 2, RIGHT * 2.5 + UP * 2]
        
        for i, (color, pos) in enumerate(zip(colors, positions)):
            axes_copy = temp_axes.copy().move_to(pos)
            parab = axes_copy.plot(lambda x: 0.3 * x**2 - 0.5, color=color, stroke_width=3)
            group = VGroup(axes_copy, parab)
            parabolas.add(group)
        
        self.play(
            LaggedStart(*[Create(p) for p in parabolas], lag_ratio=0.3),
            run_time=1.3
        )
        
        # 副标题
        subtitle = Text(
            "如何求二次函数解析式？",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(parabolas),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_axes_setup(self):
        """场景2: 建立坐标系"""
        # 标题
        title = Text(
            "二次函数的三种形式",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        # 创建坐标系
        self.play(Create(self.axes), run_time=1.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 清理标题
        self.play(FadeOut(title), run_time=0.4)
    
    def show_general_form(self):
        """场景3: 方法一 - 一般式"""
        # 标题
        title = Text(
            "方法一：一般式",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_GENERAL_FORM,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"y = ax^2 + bx + c",
            font_size=36,
            color=self.COLOR_GENERAL_FORM
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), run_time=0.7)
        
        # 三个已知点
        point_A = self.axes.c2p(*self.coord_A)
        point_B = self.axes.c2p(*self.coord_B)
        point_C = self.axes.c2p(*self.coord_C)
        
        dot_A = Dot(point_A, color=self.COLOR_SECONDARY, radius=0.08)
        dot_B = Dot(point_B, color=self.COLOR_SECONDARY, radius=0.08)
        dot_C = Dot(point_C, color=self.COLOR_SECONDARY, radius=0.08)
        
        label_A = MathTex(r"(0, -3)", font_size=20, color=WHITE).next_to(dot_A, LEFT, buff=0.15)
        label_B = MathTex(r"(1, -4)", font_size=20, color=WHITE).next_to(dot_B, DOWN, buff=0.15)
        label_C = MathTex(r"(2, -3)", font_size=20, color=WHITE).next_to(dot_C, RIGHT, buff=0.15)
        
        dots = VGroup(dot_A, dot_B, dot_C)
        labels = VGroup(label_A, label_B, label_C)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.3),
            run_time=0.9
        )
        self.play(
            LaggedStart(*[FadeIn(label) for label in labels], lag_ratio=0.2),
            run_time=0.6
        )
        
        # 说明文字
        explain = Text(
            "已知三点，代入一般式",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 方程组展开
        equations = VGroup(
            MathTex(r"-3 = a \cdot 0^2 + b \cdot 0 + c", font_size=24, color=WHITE),
            MathTex(r"-4 = a \cdot 1^2 + b \cdot 1 + c", font_size=24, color=WHITE),
            MathTex(r"-3 = a \cdot 2^2 + b \cdot 2 + c", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 2.5)
        
        self.play(Write(equations), run_time=1.5)
        
        # 逐个高亮方程
        for eq in equations:
            self.play(Indicate(eq, color=self.COLOR_HIGHLIGHT, scale_factor=1.05), run_time=0.4)
        
        self.wait(0.3)
        
        # 化简方程组
        simplified = VGroup(
            MathTex(r"c = -3", font_size=24, color=self.COLOR_HIGHLIGHT),
            MathTex(r"a + b + c = -4", font_size=24, color=WHITE),
            MathTex(r"4a + 2b + c = -3", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 2.5)
        
        self.play(TransformMatchingTex(equations, simplified), run_time=1.0)
        self.wait(0.5)
        
        # 求解结果
        solution = VGroup(
            MathTex(r"a = 1", font_size=28, color=self.COLOR_HIGHLIGHT),
            MathTex(r"b = -2", font_size=28, color=self.COLOR_HIGHLIGHT),
            MathTex(r"c = -3", font_size=28, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 3)
        
        self.play(
            FadeOut(simplified),
            FadeIn(solution, shift=UP * 0.3),
            run_time=0.8
        )
        
        # 高亮结果
        for sol in solution:
            self.play(Flash(sol, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.3)
        
        # 最终解析式
        result = MathTex(
            r"y = x^2 - 2x - 3",
            font_size=32,
            color=self.COLOR_GENERAL_FORM
        ).move_to(DOWN * 4.2)
        
        self.play(Write(result), run_time=0.8)
        self.wait(0.5)
        
        # 绘制抛物线
        parabola = self.axes.plot(
            self.parabola_func,
            x_range=[-2, 4],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(parabola), run_time=1.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(dots),
            FadeOut(labels),
            FadeOut(explain),
            FadeOut(solution),
            FadeOut(result),
            parabola.animate.set_opacity(0.3),
            run_time=0.6
        )
        
        # 保存抛物线引用
        self.parabola_reference = parabola
    
    def show_vertex_form(self):
        """场景4: 方法二 - 顶点式"""
        # 标题
        title = Text(
            "方法二：顶点式",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_VERTEX_FORM,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"y = a(x - h)^2 + k",
            font_size=36,
            color=self.COLOR_VERTEX_FORM
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), run_time=0.7)
        
        # 标注顶点
        vertex_point = self.axes.c2p(*self.coord_vertex)
        vertex_dot = Dot(vertex_point, color=self.COLOR_SECONDARY, radius=0.10)
        vertex_label = MathTex(r"(1, -4)", font_size=22, color=WHITE).next_to(vertex_dot, DOWN + RIGHT, buff=0.15)
        vertex_name = Text("顶点", font="PingFang SC", font_size=18, color=self.COLOR_HIGHLIGHT).next_to(vertex_label, DOWN, buff=0.05)
        
        self.play(
            FadeIn(vertex_dot, scale=0.5),
            run_time=0.5
        )
        self.play(
            Flash(vertex_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            run_time=0.5
        )
        self.play(
            FadeIn(vertex_label),
            FadeIn(vertex_name),
            run_time=0.5
        )
        
        # 说明文字
        explain = Text(
            "已知顶点(h,k)和另一点",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        
        # 标注另一点（使用点A）
        point_A = self.axes.c2p(*self.coord_A)
        dot_A = Dot(point_A, color=self.COLOR_SECONDARY, radius=0.08)
        label_A = MathTex(r"(0, -3)", font_size=20, color=WHITE).next_to(dot_A, LEFT, buff=0.15)
        
        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(label_A),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 代入顶点坐标
        step1 = MathTex(
            r"y = a(x - 1)^2 - 4",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(step1), run_time=1.0)
        self.wait(0.5)
        
        # 代入另一点
        step2 = MathTex(
            r"-3 = a(0 - 1)^2 - 4",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2.8)
        
        self.play(Write(step2), run_time=1.2)
        self.wait(0.5)
        
        # 求解a
        step3 = MathTex(
            r"-3 = a - 4",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2.8)
        
        self.play(TransformMatchingTex(step2, step3), run_time=0.8)
        self.wait(0.3)
        
        step4 = MathTex(
            r"a = 1",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Write(step4), run_time=0.6)
        self.play(Flash(step4, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.4)
        self.wait(0.3)
        
        # 最终解析式
        result = MathTex(
            r"y = (x - 1)^2 - 4",
            font_size=32,
            color=self.COLOR_VERTEX_FORM
        ).move_to(DOWN * 4.5)
        
        self.play(Write(result), run_time=0.8)
        self.wait(0.5)
        
        # 展开验证
        expanded = MathTex(
            r"y = x^2 - 2x - 3",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 4.5)
        
        self.play(TransformMatchingTex(result, expanded), run_time=1.0)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(vertex_dot),
            FadeOut(vertex_label),
            FadeOut(vertex_name),
            FadeOut(dot_A),
            FadeOut(label_A),
            FadeOut(explain),
            FadeOut(step1),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(expanded),
            run_time=0.6
        )
    
    def show_intercept_form(self):
        """场景5: 方法三 - 交点式"""
        # 标题
        title = Text(
            "方法三：交点式",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_INTERCEPT_FORM,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"y = a(x - x_1)(x - x_2)",
            font_size=36,
            color=self.COLOR_INTERCEPT_FORM
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), run_time=0.7)
        
        # 标注两个x轴交点
        x1_point = self.axes.c2p(*self.coord_x1)
        x2_point = self.axes.c2p(*self.coord_x2)
        
        dot_x1 = Dot(x1_point, color=self.COLOR_SECONDARY, radius=0.09)
        dot_x2 = Dot(x2_point, color=self.COLOR_SECONDARY, radius=0.09)
        
        label_x1 = MathTex(r"(-1, 0)", font_size=20, color=WHITE).next_to(dot_x1, DOWN + LEFT, buff=0.15)
        label_x2 = MathTex(r"(3, 0)", font_size=20, color=WHITE).next_to(dot_x2, DOWN + RIGHT, buff=0.15)
        
        intercept_dots = VGroup(dot_x1, dot_x2)
        intercept_labels = VGroup(label_x1, label_x2)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in intercept_dots], lag_ratio=0.3),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[Flash(dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.4) for dot in intercept_dots], lag_ratio=0.3),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(label) for label in intercept_labels], lag_ratio=0.2),
            run_time=0.5
        )
        
        # 说明文字
        explain = Text(
            "已知x轴交点和另一点",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        
        # 标注另一点（使用点A）
        point_A = self.axes.c2p(*self.coord_A)
        dot_A = Dot(point_A, color=self.COLOR_SECONDARY, radius=0.08)
        label_A = MathTex(r"(0, -3)", font_size=20, color=WHITE).next_to(dot_A, LEFT, buff=0.15)
        
        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(label_A),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 代入交点坐标
        step1 = MathTex(
            r"y = a(x + 1)(x - 3)",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(step1), run_time=1.0)
        self.wait(0.5)
        
        # 代入另一点
        step2 = MathTex(
            r"-3 = a(0 + 1)(0 - 3)",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2.8)
        
        self.play(Write(step2), run_time=1.2)
        self.wait(0.5)
        
        # 求解a
        step3 = MathTex(
            r"-3 = a \cdot 1 \cdot (-3)",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2.8)
        
        self.play(TransformMatchingTex(step2, step3), run_time=0.8)
        self.wait(0.3)
        
        step4 = MathTex(
            r"a = 1",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Write(step4), run_time=0.6)
        self.play(Flash(step4, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.4)
        self.wait(0.3)
        
        # 最终解析式
        result = MathTex(
            r"y = (x + 1)(x - 3)",
            font_size=32,
            color=self.COLOR_INTERCEPT_FORM
        ).move_to(DOWN * 4.5)
        
        self.play(Write(result), run_time=0.8)
        self.wait(0.5)
        
        # 展开验证
        expanded = MathTex(
            r"y = x^2 - 2x - 3",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 4.5)
        
        self.play(TransformMatchingTex(result, expanded), run_time=1.0)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(intercept_dots),
            FadeOut(intercept_labels),
            FadeOut(dot_A),
            FadeOut(label_A),
            FadeOut(explain),
            FadeOut(step1),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(expanded),
            run_time=0.6
        )
    
    def show_comparison(self):
        """场景6: 三种方法对比"""
        # 淡出抛物线
        self.play(FadeOut(self.parabola_reference), run_time=0.5)
        # 淡出坐标系
        self.play(FadeOut(self.axes), run_time=0.5)
        
        # 标题
        title = Text(
            "三种方法对比",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建三张对比卡片
        card1 = self.create_method_card(
            "一般式",
            r"y = ax^2 + bx + c",
            "已知三点坐标",
            self.COLOR_GENERAL_FORM,
            UP * 2.5
        )
        
        card2 = self.create_method_card(
            "顶点式",
            r"y = a(x - h)^2 + k",
            "已知顶点和另一点",
            self.COLOR_VERTEX_FORM,
            UP * 0.3
        )
        
        card3 = self.create_method_card(
            "交点式",
            r"y = a(x - x_1)(x - x_2)",
            "已知x轴交点和另一点",
            self.COLOR_INTERCEPT_FORM,
            DOWN * 1.9
        )
        
        # 卡片依次滑入
        cards = VGroup(card1, card2, card3)
        for i, card in enumerate(cards):
            self.play(
                card.animate.shift(RIGHT * 12),  # Slide from left
                run_time=0.6
            )
            self.play(
                card.animate.scale(1.05).set_stroke(width=4),  # Brief highlight
                run_time=0.2
            )
            self.play(
                card.animate.scale(1/1.05).set_stroke(width=3),  # Return to normal
                run_time=0.1
            )
            if i < len(cards) - 1:  # Don't wait after the last card
                self.wait(0.3)
        
        # Animate connections between cards (showing relationships)
        connections = VGroup()
        for i in range(len(cards)-1):
            start_pos = cards[i].get_right()
            end_pos = cards[i+1].get_left()
            connection_line = DashedLine(
                start_pos, end_pos,
                color=GRAY_B,
                dash_length=0.1
            )
            connections.add(connection_line)
        
        self.play(
            Create(connections),
            run_time=0.8
        )
        
        # Highlight key elements in each card
        self.wait(0.5)
        
        # Highlight titles
        titles = [card[1][0] for card in cards]  # Extract title texts
        for title in titles:
            self.play(
                title.animate.set_color(YELLOW).scale(1.1),
                run_time=0.4
            )
            self.wait(0.1)
            self.play(
                title.animate.set_color(WHITE).scale(1/1.1),
                run_time=0.2
            )
        
        self.wait(0.3)
        
        # Highlight formulas
        formulas = [card[1][1] for card in cards]  # Extract formula texts
        for formula in formulas:
            self.play(
                Indicate(formula, color=self.COLOR_HIGHLIGHT, scale_factor=1.05),
                run_time=0.5
            )
        
        self.wait(0.3)
        
        # Highlight conditions with different animation
        conditions = [card[1][2] for card in cards]  # Extract condition texts
        for cond in conditions:
            self.play(
                Flash(cond, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
                run_time=0.4
            )
        
        # Emphasize the decision-making process
        decision_text = Text(
            "根据已知条件选择合适的方法",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        
        self.play(
            Write(decision_text),
            run_time=0.8
        )
        
        # Highlight the decision process
        self.play(
            Indicate(decision_text, color=YELLOW, scale_factor=1.05),
            run_time=0.6
        )
        
        # Final emphasis
        hint = Text(
            "选对方法，事半功倍！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(hint, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # Final highlight on all cards
        self.play(
            *[card.animate.set_fill(opacity=0.25) for card in cards],
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # Clean up with coordinated fadeout
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(connections),
            FadeOut(decision_text),
            FadeOut(hint),
            FadeOut(self.axes),  # Fade out axes as well
            run_time=0.8
        )
    
    def create_method_card(self, title, formula, condition, color, position):
        """创建方法对比卡片"""
        # 背景框
        bg = RoundedRectangle(
            width=7.5,
            height=1.6,
            corner_radius=0.2,
            fill_color=color,
            fill_opacity=0.15,
            stroke_color=color,
            stroke_width=3
        )
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=28,
            color=WHITE,
            weight=BOLD
        )
        
        # 公式
        formula_tex = MathTex(formula, font_size=30, color=color)
        
        # 适用条件
        condition_text = Text(
            condition,
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        
        # 组合内容
        content = VGroup(title_text, formula_tex, condition_text).arrange(DOWN, buff=0.15)
        
        # 组合卡片
        card = VGroup(bg, content).move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 12)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # 作者ID
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，掌握更多解题技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰抛物线（六个小抛物线环绕）
        decorations = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = 2.5 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 3
            
            mini_axes = Axes(
                x_range=[-1, 1, 1],
                y_range=[-0.5, 0.5, 1],
                x_length=0.6,
                y_length=0.6,
                axis_config={"include_tip": False, "stroke_width": 0}
            ).move_to(pos)
            
            mini_parab = mini_axes.plot(
                lambda x: 0.3 * x**2 - 0.2,
                color=[self.COLOR_GENERAL_FORM, self.COLOR_VERTEX_FORM, self.COLOR_INTERCEPT_FORM][i % 3],
                stroke_width=2
            )
            
            decorations.add(VGroup(mini_axes, mini_parab))
        
        self.play(
            LaggedStart(*[FadeIn(deco, scale=0.5) for deco in decorations], lag_ratio=0.1),
            run_time=1.0
        )
        
        # 旋转动画
        self.play(
            Rotate(decorations, angle=PI, about_point=DOWN * 3),
            run_time=1.5,
            rate_func=smooth
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql quadratic_undetermined.py QuadraticUndeterminedCoefficients  # 快速预览
# manim -qh quadratic_undetermined.py QuadraticUndeterminedCoefficients   # 高质量 1080p
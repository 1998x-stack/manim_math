"""
一元二次不等式教学动画
Quadratic Inequality Teaching Animation

使用 Manim 创建的高中数学教学视频
内容: 一元二次不等式的解法与二次函数图像的关系
目标观众: 高一学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

知识点:
- 一元二次不等式形如 ax² + bx + c > 0
- 解法: 结合二次函数图像
- 判别式Δ决定根的情况
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadraticInequality(Scene):
    """
    一元二次不等式教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 问题转化 - 不等式→函数
    3. 建立坐标系
    4. 绘制抛物线
    5. 求解方程找根
    6. 分析正负区域
    7. 三种情况总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PARABOLA = "#3498db"       # 蓝色 - 抛物线
        self.COLOR_ROOT = "#e74c3c"           # 红色 - 根
        self.COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正值区域
        self.COLOR_NEGATIVE = "#e67e22"       # 橙色 - 负值区域
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        
        # 初始化数学数据
        self.setup_mathematics()
        
        # 执行动画序列
        self.show_opening()
        self.show_transformation()
        self.show_coordinate_system()
        self.show_parabola()
        self.show_roots()
        self.show_regions()
        self.show_three_cases()
        self.show_outro()
    
    def setup_mathematics(self):
        """初始化所有数学计算"""
        # 示例方程: x² - 3x + 2 > 0
        self.a = 1
        self.b = -3
        self.c = 2
        
        # 计算判别式
        self.delta = self.b**2 - 4*self.a*self.c
        
        # 计算根
        if self.delta >= 0:
            sqrt_delta = np.sqrt(self.delta)
            self.x1 = (-self.b - sqrt_delta) / (2 * self.a)
            self.x2 = (-self.b + sqrt_delta) / (2 * self.a)
        else:
            self.x1 = None
            self.x2 = None
        
        # 计算顶点
        self.vertex_x = -self.b / (2 * self.a)
        self.vertex_y = self.parabola_func(self.vertex_x)
        
        # 坐标系配置
        self.x_range = [-1, 4, 1]
        self.y_range = [-1, 4, 1]
        self.axes_scale = 0.85
        self.axes_center = UP * 1
        
        # 验证计算
        self.verify_mathematics()
    
    def parabola_func(self, x):
        """抛物线函数 y = ax² + bx + c"""
        return self.a * x**2 + self.b * x + self.c
    
    def verify_mathematics(self):
        """验证数学计算的正确性"""
        epsilon = 1e-6
        
        # 验证判别式
        delta_calc = self.b**2 - 4*self.a*self.c
        assert abs(delta_calc - self.delta) < epsilon, f"判别式计算错误: {delta_calc} ≠ {self.delta}"
        
        # 验证根（如果存在）
        if self.x1 is not None:
            y1 = self.parabola_func(self.x1)
            assert abs(y1) < epsilon, f"x1={self.x1} 不是根, f(x1)={y1}"
            
            y2 = self.parabola_func(self.x2)
            assert abs(y2) < epsilon, f"x2={self.x2} 不是根, f(x2)={y2}"
        
        # 验证顶点
        vertex_x_calc = -self.b / (2 * self.a)
        assert abs(vertex_x_calc - self.vertex_x) < epsilon, "顶点x坐标错误"
        
        print("✓ 数学验证通过")
        print(f"  方程: {self.a}x² + ({self.b})x + {self.c} = 0")
        print(f"  判别式Δ = {self.delta}")
        if self.x1 is not None:
            print(f"  根: x₁ = {self.x1}, x₂ = {self.x2}")
        print(f"  顶点: ({self.vertex_x}, {self.vertex_y:.3f})")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "一元二次不等式怎么解?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 示例不等式
        inequality = MathTex(
            r"x^2 - 3x + 2 > 0",
            font_size=48,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(Write(inequality), run_time=1.0)
        
        # 高亮 ">" 符号
        # Highlite ">" or "<" sign - using safer approach
        try:
            # Try to get the > sign directly
            greater_sign = None
            # Method 1: Try using get_parts
            try:
                parts = inequality.as_group()
                # Or iterate through the parts to find the comparison operator
                for i, part in enumerate(inequality.submobjects):
                    # We'll just use a general approach to highlight the middle part
                    # Assuming the inequality has 3 parts: left, operator, right
                    if i == 1:  # The operator is usually the middle part
                        greater_sign = part
                        break
            except:
                pass
            
            if greater_sign is not None:
                self.play(
                    Flash(greater_sign, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
                    greater_sign.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.3),
                    run_time=0.8
                )
            else:
                # If we can't find the specific sign, just wait
                self.wait(0.8)
        except:
            # If anything goes wrong with accessing parts, just continue
            self.wait(0.8)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            inequality.animate.scale(0.7).move_to(UP * 6),
            run_time=0.5
        )
        
        self.opening_inequality = inequality
    
    def show_transformation(self):
        """场景2: 问题转化"""
        # 标题
        title = Text(
            "核心思路",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 构建函数
        function_eq = MathTex(
            r"y = x^2 - 3x + 2",
            font_size=42,
            color=self.COLOR_PARABOLA
        ).move_to(UP * 4)
        
        self.play(Write(function_eq), run_time=1.0)
        
        # 转化箭头
        arrow = Arrow(
            self.opening_inequality.get_bottom(),
            function_eq.get_top(),
            color=self.COLOR_AUXILIARY,
            buff=0.2,
            stroke_width=3
        )
        
        self.play(Create(arrow), run_time=0.6)
        
        # 说明文字
        explain = Text(
            "求 y > 0 对应的 x 范围",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        
        # 高亮 "y > 0"
        highlight_box = SurroundingRectangle(
            explain[0][1:6],  # "y > 0"
            color=self.COLOR_HIGHLIGHT,
            buff=0.05
        )
        
        self.play(Create(highlight_box), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(self.opening_inequality),
            FadeOut(arrow),
            FadeOut(explain),
            FadeOut(highlight_box),
            function_eq.animate.scale(0.6).move_to(UP * 6.5),
            run_time=0.6
        )
        
        self.function_label = function_eq
    
    def show_coordinate_system(self):
        """场景3: 建立坐标系"""
        # 创建坐标系
        self.axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=7 * self.axes_scale,
            y_length=7 * self.axes_scale,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_numbers": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15
            }
        ).move_to(self.axes_center)
        
        # 添加数字标签
        x_labels = VGroup()
        for x in range(int(self.x_range[0]), int(self.x_range[1]) + 1):
            if x == 0:
                continue
            label = Text(
                str(x),
                font="Noto Sans CJK SC",
                font_size=18,
                color=GRAY_A
            ).move_to(self.axes.c2p(x, 0) + DOWN * 0.3)
            x_labels.add(label)
        
        y_labels = VGroup()
        for y in range(int(self.y_range[0]), int(self.y_range[1]) + 1):
            if y == 0:
                continue
            label = Text(
                str(y),
                font="Noto Sans CJK SC",
                font_size=18,
                color=GRAY_A
            ).move_to(self.axes.c2p(0, y) + LEFT * 0.3)
            y_labels.add(label)
        
        # 原点标注
        origin_label = Text(
            "O",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).move_to(self.axes.c2p(0, 0) + DL * 0.35)
        
        # 坐标轴标签
        x_axis_label = MathTex(r"x", font_size=24, color=WHITE).next_to(
            self.axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_axis_label = MathTex(r"y", font_size=24, color=WHITE).next_to(
            self.axes.y_axis.get_end(), UP, buff=0.2
        )
        
        # 将所有坐标轴相关对象放入一个组
        self.coordinate_group = VGroup(
            self.axes,
            x_labels,
            y_labels,
            origin_label,
            x_axis_label,
            y_axis_label
        )

        # 动画
        self.play(Create(self.axes), run_time=1.5)
        self.play(
            FadeIn(x_labels),
            FadeIn(y_labels),
            FadeIn(origin_label),
            FadeIn(x_axis_label),
            FadeIn(y_axis_label),
            run_time=1.0
        )
        self.wait(0.5)
    
    def show_parabola(self):
        """场景4: 绘制抛物线"""
        # 绘制抛物线
        a, b, c = self.a, self.b, self.c
        self.parabola = self.axes.plot(lambda x: a*x**2 + b*x + c, x_range=[-0.5, 3.5], color=self.COLOR_PARABOLA, stroke_width=4)
        
        self.play(Create(self.parabola), run_time=2.5)
        
        # 说明文字
        explain = Text(
            "a > 0, 开口向上",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        self.play(FadeOut(explain), run_time=0.3)
    
    def show_roots(self):
        """场景5: 求解方程找根"""
        # 标题
        title = Text(
            "第一步: 解方程找交点",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 方程
        equation = MathTex(
            r"x^2 - 3x + 2 = 0",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 5.3)
        
        self.play(Write(equation), run_time=1.0)
        
        # 因式分解
        factored = MathTex(
            r"(x - 1)(x - 2) = 0",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 5.3)
        
        self.play(TransformMatchingTex(equation, factored), run_time=1.0)
        self.wait(0.5)
        
        # 显示根
        roots_text = MathTex(
            r"x_1 = 1, \quad x_2 = 2",
            font_size=36,
            color=self.COLOR_ROOT
        ).move_to(DOWN * 6.2)
        
        self.play(Write(roots_text), run_time=0.8)
        
        # 标记根在坐标系上
        root1_point = self.axes.c2p(self.x1, 0)
        root2_point = self.axes.c2p(self.x2, 0)
        
        dot1 = Dot(root1_point, color=self.COLOR_ROOT, radius=0.1)
        dot2 = Dot(root2_point, color=self.COLOR_ROOT, radius=0.1)
        
        label1 = MathTex(r"x_1", font_size=22, color=self.COLOR_ROOT).next_to(
            dot1, DOWN, buff=0.15
        )
        label2 = MathTex(r"x_2", font_size=22, color=self.COLOR_ROOT).next_to(
            dot2, DOWN, buff=0.15
        )
        
        self.play(
            FadeIn(dot1, scale=0.5),
            Flash(dot1, color=self.COLOR_ROOT, flash_radius=0.3),
            run_time=0.5
        )
        self.play(FadeIn(label1), run_time=0.3)
        
        self.play(
            FadeIn(dot2, scale=0.5),
            Flash(dot2, color=self.COLOR_ROOT, flash_radius=0.3),
            run_time=0.5
        )
        self.play(FadeIn(label2), run_time=0.3)
        
        # 虚线连接到抛物线
        dashed1 = DashedLine(
            root1_point,
            root1_point + UP * 0.001,  # 极短，因为根就在x轴上
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        dashed2 = DashedLine(
            root2_point,
            root2_point + UP * 0.001,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(factored),
            FadeOut(roots_text),
            run_time=0.5
        )
        
        self.root_dots = VGroup(dot1, dot2, label1, label2)
    
    def show_regions(self):
        """场景6: 分析正负区域"""
        # 标题
        title = Text(
            "第二步: 观察函数值正负",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 说明 y > 0
        explain1 = Text(
            "y > 0: 抛物线在 x 轴上方",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_POSITIVE
        ).move_to(DOWN * 5.3)
        
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)
        
        # 高亮左侧区域 (x < 1)
        left_area = self.axes.get_area(
            self.parabola,
            x_range=[self.x_range[0], self.x1],
            color=self.COLOR_POSITIVE,
            opacity=0.3
        )
        
        self.play(FadeIn(left_area), run_time=1.0)
        
        # 高亮右侧区域 (x > 2)
        right_area = self.axes.get_area(
            self.parabola,
            x_range=[self.x2, self.x_range[1] - 0.5],
            color=self.COLOR_POSITIVE,
            opacity=0.3
        )
        
        self.play(FadeIn(right_area), run_time=1.0)
        self.wait(0.8)
        
        # 说明 y < 0
        explain2 = Text(
            "y < 0: 抛物线在 x 轴下方",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_NEGATIVE
        ).move_to(DOWN * 5.3)
        
        self.play(FadeOut(explain1), FadeIn(explain2), run_time=0.5)
        
        # 中间区域 (1 < x < 2) - 需要特殊处理因为是负值
        # 创建填充多边形
        mid_x_values = np.linspace(self.x1, self.x2, 50)
        mid_points = [self.axes.c2p(x, self.parabola_func(x)) for x in mid_x_values]
        
        # 添加x轴上的点闭合区域
        mid_points.append(self.axes.c2p(self.x2, 0))
        mid_points.append(self.axes.c2p(self.x1, 0))
        
        mid_area = Polygon(
            *mid_points,
            color=self.COLOR_NEGATIVE,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(FadeIn(mid_area), run_time=1.0)
        self.wait(0.8)
        
        # 显示解集
        solution = VGroup(
            MathTex(r"x < 1", font_size=40, color=self.COLOR_HIGHLIGHT),
            Text("或", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_HIGHLIGHT),
            MathTex(r"x > 2", font_size=40, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 6.2)
        
        self.play(Write(solution), run_time=1.0)
        
        # 高亮解集
        solution_box = SurroundingRectangle(
            solution,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(solution_box), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain2),
            FadeOut(left_area),
            FadeOut(right_area),
            FadeOut(mid_area),
            FadeOut(solution),
            FadeOut(solution_box),
            run_time=0.6
        )
    
    def show_three_cases(self):
        """场景7: 三种情况总结"""
        # 清屏
        self.play(
            FadeOut(self.coordinate_group),
            FadeOut(self.parabola),
            FadeOut(self.root_dots),
            FadeOut(self.function_label),
            run_time=0.8
        )
        
        # 标题
        title = Text(
            "判别式 Δ 决定根的情况",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 判别式公式
        delta_formula = MathTex(
            r"\Delta = b^2 - 4ac",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(delta_formula, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建三个小坐标系
        scale = 0.35
        spacing = 3.0
        
        # Case 1: Δ > 0 (两个不等实根)
        case1_axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 3, 1],
            x_length=5 * scale,
            y_length=5 * scale,
            axis_config={"include_tip": False, "stroke_width": 1.5}
        ).move_to(LEFT * spacing + UP * 1.5)
        
        case1_parabola = case1_axes.plot(
            lambda x: (x - 1) * (x - 2),
            x_range=[0, 3], color=self.COLOR_PARABOLA, stroke_width=3
        )
        
        case1_dots = VGroup(
            Dot(case1_axes.c2p(1, 0), color=self.COLOR_ROOT, radius=0.06),
            Dot(case1_axes.c2p(2, 0), color=self.COLOR_ROOT, radius=0.06)
        )
        
        case1_title = Text(
            "Δ > 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).next_to(case1_axes, UP, buff=0.3)
        
        case1_solution = Text(
            "x < x₁ 或 x > x₂",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_POSITIVE
        ).next_to(case1_axes, DOWN, buff=0.3)
        
        case1_group = VGroup(case1_axes, case1_parabola, case1_dots, case1_title, case1_solution)
        
        # Case 2: Δ = 0 (一个重根)
        case2_axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 3, 1],
            x_length=5 * scale,
            y_length=5 * scale,
            axis_config={"include_tip": False, "stroke_width": 1.5}
        ).move_to(UP * 1.5)
        
        # Using class method to avoid pickle error
        case2_parabola = case2_axes.plot(
            lambda x: (x - 1.5)**2,
            x_range=[0, 3], color=self.COLOR_PARABOLA, stroke_width=3
        )
        
        case2_dot = Dot(case2_axes.c2p(1.5, 0), color=self.COLOR_ROOT, radius=0.06)
        
        case2_title = Text(
            "Δ = 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).next_to(case2_axes, UP, buff=0.3)
        
        case2_solution = MathTex(
            r"x \neq -\frac{b}{2a}",
            font_size=20,
            color=self.COLOR_POSITIVE
        ).next_to(case2_axes, DOWN, buff=0.3)
        
        case2_group = VGroup(case2_axes, case2_parabola, case2_dot, case2_title, case2_solution)
        
        # Case 3: Δ < 0 (无实根)
        case3_axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 3, 1],
            x_length=5 * scale,
            y_length=5 * scale,
            axis_config={"include_tip": False, "stroke_width": 1.5}
        ).move_to(RIGHT * spacing + UP * 1.5)
        
        # Using class method to avoid pickle error
        case3_parabola = case3_axes.plot(
            lambda x: x**2 - 3*x + 4,
            x_range=[0, 3], color=self.COLOR_PARABOLA, stroke_width=3
        )
        
        case3_title = Text(
            "Δ < 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).next_to(case3_axes, UP, buff=0.3)
        
        case3_solution = MathTex(
            r"x \in \mathbb{R}",
            font_size=20,
            color=self.COLOR_POSITIVE
        ).next_to(case3_axes, DOWN, buff=0.3)
        
        case3_group = VGroup(case3_axes, case3_parabola, case3_title, case3_solution)
        
        # 依次显示三种情况
        self.play(
            Create(case1_axes),
            Create(case1_parabola),
            FadeIn(case1_dots),
            run_time=1.2
        )
        self.play(FadeIn(case1_title), FadeIn(case1_solution), run_time=0.5)
        
        self.play(
            Create(case2_axes),
            Create(case2_parabola),
            FadeIn(case2_dot),
            run_time=1.2
        )
        self.play(FadeIn(case2_title), FadeIn(case2_solution), run_time=0.5)
        
        self.play(
            Create(case3_axes),
            Create(case3_parabola),
            run_time=1.2
        )
        self.play(FadeIn(case3_title), FadeIn(case3_solution), run_time=0.5)
        
        # 强调判别式公式
        self.play(
            Indicate(delta_formula, scale_factor=1.2, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 总结说明
        summary = Text(
            "(a > 0 时，不等式 > 0 的解)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(summary), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(delta_formula),
            FadeOut(case1_group),
            FadeOut(case2_group),
            FadeOut(case3_group),
            FadeOut(summary),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多解题技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小抛物线装饰
        deco_scale = 0.25
        parabolas = VGroup()
        
        for i in range(5):
            x_pos = -2 + i * 1
            mini_axes = Axes(
                x_range=[-1, 1],
                y_range=[-0.5, 1],
                x_length=1.2 * deco_scale,
                y_length=1.2 * deco_scale,
                axis_config={"stroke_width": 0}
            )
            # Using class method to avoid pickle error
            mini_parabola = mini_axes.plot(lambda x: x**2, color=self.COLOR_PARABOLA, stroke_width=2)
        
            mini_group = VGroup(mini_axes, mini_parabola).move_to(
                DOWN * 2 + RIGHT * x_pos
            )
            parabolas.add(mini_group)
        
        self.play(
            *[FadeIn(p, scale=0.5) for p in parabolas],
            run_time=0.8
        )
        
        # 微微旋转
        self.play(
            Rotate(parabolas, angle=PI / 12, run_time=0.8),
            Rotate(parabolas, angle=-PI / 6, run_time=0.8)
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(parabolas),
            run_time=1.0
        )

    def case1_func(self, x):  # Helper function to avoid pickle error
        return (x - 1) * (x - 2)

    def case2_func(self, x):  # Helper function to avoid pickle error
        return (x - 1.5)**2

    def case3_func(self, x):  # Helper function to avoid pickle error
        return x**2 - 3*x + 4

    def mini_func(self, x):  # Helper function to avoid pickle error
        return x**2

# 运行命令:
# manim -pql quadratic_inequality.py QuadraticInequality  # 快速预览 480p
# manim -qm quadratic_inequality.py QuadraticInequality   # 中等质量 720p
# manim -qh quadratic_inequality.py QuadraticInequality   # 高质量 1080p
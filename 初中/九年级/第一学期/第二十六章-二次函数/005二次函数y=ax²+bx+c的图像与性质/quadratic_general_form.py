"""
二次函数一般式 y=ax²+bx+c 的图像与性质
Quadratic Function in General Form - Manim Animation

适用年级: 九年级
主题: 一般式二次函数、配方法、系数的几何意义
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadraticGeneralForm(Scene):
    """
    二次函数一般式教学动画
    
    场景顺序:
    1. 开场钩子 - 引出一般式
    2. 配方过程演示
    3. 建立坐标系和抛物线
    4. 顶点和对称轴
    5. y轴交点
    6. a的符号影响
    7. b的符号影响
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PARABOLA = "#3498db"        # 蓝色 - 抛物线
        self.COLOR_VERTEX = "#f39c12"          # 橙色 - 顶点
        self.COLOR_AXIS = "#2ecc71"            # 绿色 - 对称轴
        self.COLOR_Y_INTERCEPT = "#e74c3c"     # 红色 - y轴交点
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_FORMULA_STEP = "#9b59b6"    # 紫色 - 配方步骤
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_completing_square()
        self.scene_3_create_parabola()
        self.scene_4_vertex_and_axis()
        self.scene_5_y_intercept()
        self.scene_6_coefficient_a()
        self.scene_7_coefficient_b()
        self.scene_8_summary_and_outro()
    
    def setup_geometry(self):
        """初始化所有几何参数和坐标"""
        # ========== 主要示例抛物线参数 ==========
        # y = x² - 2x - 3 = (x-1)² - 4
        self.a = 1.0
        self.b = -2.0
        self.c = -3.0
        
        # ========== 顶点计算 ==========
        self.vertex_x = -self.b / (2 * self.a)  # = 1.0
        self.vertex_y = (4 * self.a * self.c - self.b**2) / (4 * self.a)  # = -4.0
        
        # ========== 坐标系设置 ==========
        self.axes_center = UP * 1.5
        self.x_range = [-3, 5, 1]
        self.y_range = [-5, 5, 1]
        
        # 创建坐标系
        self.axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=7,
            y_length=8,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "include_ticks": True,
            },
            tips=False
        ).move_to(self.axes_center)
        
        # ========== 抛物线函数定义 ==========
        self.parabola_func = lambda x: self.a * x**2 + self.b * x + self.c
        
        # ========== 验证几何计算 ==========
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何参数的正确性"""
        # 验证顶点在抛物线上
        y_at_vertex = self.parabola_func(self.vertex_x)
        assert abs(y_at_vertex - self.vertex_y) < 1e-6, \
            f"顶点不在抛物线上: y({self.vertex_x}) = {y_at_vertex}, 期望 {self.vertex_y}"
        
        # 验证y轴交点
        y_at_zero = self.parabola_func(0)
        assert abs(y_at_zero - self.c) < 1e-6, \
            f"y轴交点错误: y(0) = {y_at_zero}, 期望 {self.c}"
        
        # 验证对称性
        test_offset = 2.0
        y_left = self.parabola_func(self.vertex_x - test_offset)
        y_right = self.parabola_func(self.vertex_x + test_offset)
        assert abs(y_left - y_right) < 1e-6, \
            f"抛物线不对称: y({self.vertex_x - test_offset}) = {y_left}, " \
            f"y({self.vertex_x + test_offset}) = {y_right}"
        
        # 验证配方结果
        # y = a(x - h)² + k
        h = self.vertex_x
        k = self.vertex_y
        test_x = 3.0
        y_original = self.parabola_func(test_x)
        y_vertex_form = self.a * (test_x - h)**2 + k
        assert abs(y_original - y_vertex_form) < 1e-6, \
            f"配方结果错误: 原式={y_original}, 顶点式={y_vertex_form}"
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "看懂a、b、c\n就能画出抛物线!",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        self.wait(0.5)
        
        # 一般式公式
        general_form = MathTex(
            r"y = ", r"a", r"x^2 + ", r"b", r"x + ", r"c",
            font_size=40,
            color=WHITE
        ).move_to(UP * 3.5)
        
        # 系数着色
        general_form[1].set_color(self.COLOR_PARABOLA)  # a
        general_form[3].set_color(self.COLOR_AXIS)      # b
        general_form[5].set_color(self.COLOR_Y_INTERCEPT)  # c
        
        self.play(Write(general_form), run_time=1.0)
        
        # 系数依次闪烁
        self.play(Indicate(general_form[1], scale_factor=1.2), run_time=0.4)
        self.wait(0.2)
        self.play(Indicate(general_form[3], scale_factor=1.2), run_time=0.4)
        self.wait(0.2)
        self.play(Indicate(general_form[5], scale_factor=1.2), run_time=0.4)
        self.wait(0.5)
        
        # 清理并保留
        self.play(FadeOut(hook), run_time=0.5)
        
        # 将公式移到顶部
        self.general_form_top = MathTex(
            r"y = ax^2 + bx + c",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6.8)
        
        self.play(
            Transform(general_form, self.general_form_top),
            run_time=0.6
        )
        
        self.general_form = general_form
    
    def scene_2_completing_square(self):
        """场景2: 配方过程演示"""
        # 标题
        title = Text(
            "配方法",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FORMULA_STEP
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 配方步骤
        # 步骤0: 原式
        step0 = MathTex(
            r"y = ax^2 + bx + c",
            font_size=28
        ).move_to(UP * 4)
        
        self.play(Write(step0), run_time=0.8)
        self.wait(0.5)
        
        # 步骤1: 提取a
        step1 = MathTex(
            r"y = a\left(x^2 + \frac{b}{a}x\right) + c",
            font_size=28
        ).move_to(UP * 4)
        
        self.play(TransformMatchingTex(step0, step1), run_time=1.0)
        self.wait(0.5)
        
        # 步骤2: 配方
        step2 = MathTex(
            r"y = a\left(x^2 + \frac{b}{a}x + \frac{b^2}{4a^2}\right) - \frac{b^2}{4a} + c",
            font_size=26
        ).move_to(UP * 4)
        
        explanation1 = Text(
            "配方：添加并减去相同的项",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 2.8)
        
        self.play(
            TransformMatchingTex(step1, step2),
            FadeIn(explanation1),
            run_time=1.2
        )
        self.wait(0.8)
        self.play(FadeOut(explanation1), run_time=0.3)
        
        # 步骤3: 完全平方
        step3 = MathTex(
            r"y = a\left(x + \frac{b}{2a}\right)^2 + \frac{4ac - b^2}{4a}",
            font_size=28
        ).move_to(UP * 4)
        
        self.play(TransformMatchingTex(step2, step3), run_time=1.0)
        self.wait(0.5)
        
        # 顶点式
        vertex_form = MathTex(
            r"y = a(x - h)^2 + k",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(Write(vertex_form), run_time=1.0)
        
        # 顶点公式
        vertex_formula = VGroup(
            MathTex(r"h = -\frac{b}{2a}", font_size=26, color=self.COLOR_VERTEX),
            MathTex(r"k = \frac{4ac - b^2}{4a}", font_size=26, color=self.COLOR_VERTEX)
        ).arrange(RIGHT, buff=1.0).move_to(UP * 1.3)
        
        # 框出
        box = SurroundingRectangle(
            vertex_formula,
            color=self.COLOR_VERTEX,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            FadeIn(vertex_formula),
            Create(box),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step3),
            FadeOut(vertex_form),
            FadeOut(vertex_formula),
            FadeOut(box),
            run_time=0.6
        )
    
    def scene_3_create_parabola(self):
        """场景3: 建立坐标系和抛物线"""
        # 创建坐标系
        self.play(Create(self.axes), run_time=1.2)
        
        # 具体例子
        example_eq = MathTex(
            r"y = x^2 - 2x - 3",
            font_size=30,
            color=self.COLOR_PARABOLA
        ).move_to(UP * 5.5)
        
        self.play(Write(example_eq), run_time=0.8)
        
        # 创建抛物线
        self.parabola = self.axes.plot(
            self.parabola_func,
            x_range=[-2, 4],
            color=self.COLOR_PARABOLA,
            stroke_width=4
        )
        
        self.play(Create(self.parabola), run_time=1.5)
        self.wait(1.0)
        
        # 清理例子公式
        self.play(FadeOut(example_eq), run_time=0.4)
    
    def scene_4_vertex_and_axis(self):
        """场景4: 顶点和对称轴"""
        # 顶点点
        vertex_coord = self.axes.c2p(self.vertex_x, self.vertex_y)
        self.vertex_dot = Dot(
            vertex_coord,
            color=self.COLOR_VERTEX,
            radius=0.1
        )
        
        self.play(
            FadeIn(self.vertex_dot, scale=0.5),
            Flash(self.vertex_dot, color=self.COLOR_VERTEX, flash_radius=0.3),
            run_time=0.6
        )
        
        # 顶点坐标标签
        self.vertex_label = MathTex(
            f"({self.vertex_x:.0f}, {self.vertex_y:.0f})",
            font_size=24,
            color=self.COLOR_VERTEX
        ).next_to(self.vertex_dot, DOWN + LEFT, buff=0.25)
        
        self.play(Write(self.vertex_label), run_time=0.5)
        
        # 顶点公式提示框
        vertex_formula_box = VGroup(
            Text("顶点公式", font="PingFang SC", font_size=24, color=WHITE),
            MathTex(
                r"\left(-\frac{b}{2a}, \frac{4ac-b^2}{4a}\right)",
                font_size=24,
                color=self.COLOR_VERTEX
            )
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 4.5)
        
        bg_rect = SurroundingRectangle(
            vertex_formula_box,
            color=self.COLOR_VERTEX,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(
            FadeIn(vertex_formula_box),
            Create(bg_rect),
            run_time=0.6
        )
        
        # 计算演示
        calculation = MathTex(
            r"x = -\frac{(-2)}{2 \times 1} = 1",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.8)
        
        self.play(Write(calculation), run_time=1.0)
        self.wait(1.0)
        
        # 清理提示
        self.play(
            FadeOut(vertex_formula_box),
            FadeOut(bg_rect),
            FadeOut(calculation),
            run_time=0.5
        )
        
        # 对称轴
        axis_bottom = self.axes.c2p(self.vertex_x, self.y_range[0])
        axis_top = self.axes.c2p(self.vertex_x, self.y_range[1])
        
        self.axis_line = DashedLine(
            axis_bottom,
            axis_top,
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(self.axis_line), run_time=0.8)
        
        # 对称轴方程
        self.axis_eq = MathTex(
            r"x = -\frac{b}{2a}",
            font_size=24,
            color=self.COLOR_AXIS
        ).next_to(self.axis_line, UP, buff=0.2).shift(RIGHT * 0.4)
        
        self.play(Write(self.axis_eq), run_time=0.5)
        self.wait(1.5)
    
    def scene_5_y_intercept(self):
        """场景5: y轴交点"""
        # y轴高亮
        y_axis = self.axes.get_y_axis()
        original_color = y_axis.get_color()
        
        self.play(y_axis.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # y轴交点
        y_intercept_coord = self.axes.c2p(0, self.c)
        self.y_intercept_dot = Dot(
            y_intercept_coord,
            color=self.COLOR_Y_INTERCEPT,
            radius=0.1
        )
        
        self.play(
            FadeIn(self.y_intercept_dot, scale=0.5),
            Flash(self.y_intercept_dot, color=self.COLOR_Y_INTERCEPT, flash_radius=0.3),
            run_time=0.6
        )
        
        # y轴交点坐标
        self.y_intercept_label = MathTex(
            f"(0, {self.c:.0f})",
            font_size=24,
            color=self.COLOR_Y_INTERCEPT
        ).next_to(self.y_intercept_dot, LEFT, buff=0.25)
        
        self.play(Write(self.y_intercept_label), run_time=0.5)
        
        # 说明文字
        explanation = VGroup(
            Text("y轴交点", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"(0, c)", font_size=28, color=self.COLOR_Y_INTERCEPT),
            Text("当x=0时, y=c", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        
        # 高亮公式中的c
        c_highlight = MathTex(
            r"y = ax^2 + bx + ", r"c",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6.8)
        c_highlight[1].set_color(self.COLOR_Y_INTERCEPT)
        
        self.play(
            Transform(self.general_form, c_highlight),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 恢复y轴颜色
        self.play(
            y_axis.animate.set_color(original_color),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 恢复公式
        general_form_normal = MathTex(
            r"y = ax^2 + bx + c",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6.8)
        
        self.play(Transform(self.general_form, general_form_normal), run_time=0.3)
    
    def scene_6_coefficient_a(self):
        """场景6: a的符号影响"""
        # 原抛物线淡化
        self.play(
            self.parabola.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "a的作用",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_PARABOLA
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # a<0的抛物线 (y = -x² - 2x - 3)
        parabola_negative_func = lambda x: -self.a * x**2 + self.b * x + self.c
        parabola_negative = self.axes.plot(
            parabola_negative_func,
            x_range=[-4, 2],
            color="#e74c3c",
            stroke_width=4
        )
        
        self.play(Create(parabola_negative), run_time=1.2)
        
        # 开口方向箭头
        arrow_up = Arrow(
            start=self.axes.c2p(3, self.parabola_func(3)),
            end=self.axes.c2p(3, self.parabola_func(3)) + UP * 0.8,
            color=YELLOW,
            stroke_width=4
        )
        
        arrow_down = Arrow(
            start=self.axes.c2p(-3, parabola_negative_func(-3)),
            end=self.axes.c2p(-3, parabola_negative_func(-3)) + DOWN * 0.8,
            color=YELLOW,
            stroke_width=4
        )
        
        label_up = Text("a > 0", font="PingFang SC", font_size=22, color=YELLOW).next_to(arrow_up, RIGHT, buff=0.2)
        label_down = Text("a < 0", font="PingFang SC", font_size=22, color=YELLOW).next_to(arrow_down, LEFT, buff=0.2)
        
        self.play(
            GrowArrow(arrow_up),
            GrowArrow(arrow_down),
            FadeIn(label_up),
            FadeIn(label_down),
            run_time=0.8
        )
        
        # 说明文字
        explanation = VGroup(
            Text("a > 0: 开口向上", font="PingFang SC", font_size=24, color=WHITE),
            Text("a < 0: 开口向下", font="PingFang SC", font_size=24, color=WHITE),
            Text("|a|越大，开口越窄", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.7)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(parabola_negative),
            FadeOut(arrow_up),
            FadeOut(arrow_down),
            FadeOut(label_up),
            FadeOut(label_down),
            FadeOut(explanation),
            self.parabola.animate.set_opacity(1),
            run_time=0.6
        )
    
    def scene_7_coefficient_b(self):
        """场景7: b的符号影响"""
        # 标题
        title = Text(
            "b的作用",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_AXIS
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 公式展示
        axis_formula = MathTex(
            r"x = -\frac{b}{2a}",
            font_size=30,
            color=self.COLOR_AXIS
        ).move_to(UP * 4.5)
        
        self.play(Write(axis_formula), run_time=0.7)
        
        # 原抛物线淡化
        self.play(
            self.parabola.animate.set_opacity(0.3),
            self.axis_line.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # b>0的例子: y = x² + 2x - 3 (对称轴在左)
        parabola_b_positive_func = lambda x: x**2 + 2*x - 3
        parabola_b_positive = self.axes.plot(
            parabola_b_positive_func,
            x_range=[-4, 2],
            color="#2ecc71",
            stroke_width=4
        )
        
        vertex_x_b_pos = -2 / (2 * 1)  # = -1
        axis_left = DashedLine(
            self.axes.c2p(vertex_x_b_pos, self.y_range[0]),
            self.axes.c2p(vertex_x_b_pos, self.y_range[1]),
            color="#2ecc71",
            dash_length=0.1,
            stroke_width=2
        )
        
        label_left = Text("b > 0", font="PingFang SC", font_size=20, color="#2ecc71").next_to(
            self.axes.c2p(vertex_x_b_pos, 4), UP, buff=0.1
        )
        
        self.play(
            Create(parabola_b_positive),
            Create(axis_left),
            FadeIn(label_left),
            run_time=1.0
        )
        self.wait(0.5)
        
        # b<0的例子: y = x² - 4x - 3 (对称轴在右)
        parabola_b_negative_func = lambda x: x**2 - 4*x - 3
        parabola_b_negative = self.axes.plot(
            parabola_b_negative_func,
            x_range=[0, 6],
            color="#e67e22",
            stroke_width=4
        )
        
        vertex_x_b_neg = -(-4) / (2 * 1)  # = 2
        axis_right = DashedLine(
            self.axes.c2p(vertex_x_b_neg, self.y_range[0]),
            self.axes.c2p(vertex_x_b_neg, self.y_range[1]),
            color="#e67e22",
            dash_length=0.1,
            stroke_width=2
        )
        
        label_right = Text("b < 0", font="PingFang SC", font_size=20, color="#e67e22").next_to(
            self.axes.c2p(vertex_x_b_neg, 4), UP, buff=0.1
        )
        
        self.play(
            Create(parabola_b_negative),
            Create(axis_right),
            FadeIn(label_right),
            run_time=1.0
        )
        
        # 规律总结
        rule = VGroup(
            Text("a、b同号 → 对称轴在y轴左侧", font="PingFang SC", font_size=22, color=WHITE),
            Text("a、b异号 → 对称轴在y轴右侧", font="PingFang SC", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 5.5)
        
        self.play(FadeIn(rule, shift=UP * 0.3), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axis_formula),
            FadeOut(parabola_b_positive),
            FadeOut(parabola_b_negative),
            FadeOut(axis_left),
            FadeOut(axis_right),
            FadeOut(label_left),
            FadeOut(label_right),
            FadeOut(rule),
            self.parabola.animate.set_opacity(1),
            self.axis_line.animate.set_opacity(1),
            run_time=0.6
        )
    
    def scene_8_summary_and_outro(self):
        """场景8: 总结与片尾"""
        # 清空场景
        self.play(
            FadeOut(self.axes),
            FadeOut(self.parabola),
            FadeOut(self.vertex_dot),
            FadeOut(self.vertex_label),
            FadeOut(self.axis_line),
            FadeOut(self.axis_eq),
            FadeOut(self.y_intercept_dot),
            FadeOut(self.y_intercept_label),
            FadeOut(self.general_form),
            run_time=0.6
        )
        
        # 总结标题
        summary_title = Text(
            "a、b、c的几何意义",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(summary_title), run_time=0.7)
        
        # 卡片系统
        cards = VGroup()
        
        # 卡片1: a的作用
        card_a_content = VGroup(
            Text("决定开口方向", font="PingFang SC", font_size=20, color=WHITE),
            Text("a>0向上, a<0向下", font="PingFang SC", font_size=18, color=GRAY_A),
            Text("|a|决定开口大小", font="PingFang SC", font_size=18, color=GRAY_A)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        card_a = self.create_summary_card(
            card_a_content,
            "a",
            self.COLOR_PARABOLA
        ).move_to(UP * 4.5)
        cards.add(card_a)
        
        # 卡片2: b的作用
        card_b_content = VGroup(
            Text("影响对称轴位置", font="PingFang SC", font_size=20, color=WHITE),
            MathTex(r"x = -\frac{b}{2a}", font_size=22, color=WHITE),
            Text("a、b同号→轴在左", font="PingFang SC", font_size=18, color=GRAY_A)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        card_b = self.create_summary_card(
            card_b_content,
            "b",
            self.COLOR_AXIS
        ).move_to(UP * 2.5)
        cards.add(card_b)
        
        # 卡片3: c的作用
        card_c_content = VGroup(
            Text("y轴交点纵坐标", font="PingFang SC", font_size=20, color=WHITE),
            MathTex(r"(0, c)", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        card_c = self.create_summary_card(
            card_c_content,
            "c",
            self.COLOR_Y_INTERCEPT
        ).move_to(UP * 0.8)
        cards.add(card_c)
        
        # 卡片4: 顶点公式
        card_vertex_content = VGroup(
            MathTex(r"(-\frac{b}{2a}, \frac{4ac-b^2}{4a})", font_size=22, color=WHITE)
        )
        
        card_vertex = self.create_summary_card(
            card_vertex_content,
            "顶点",
            self.COLOR_VERTEX
        ).move_to(DOWN * 0.8)
        cards.add(card_vertex)
        
        # 卡片依次出现
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=UP * 0.3), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 判别式提示
        discriminant_hint = Text(
            "Δ = b² - 4ac (决定与x轴交点个数)",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(discriminant_hint), run_time=0.6)
        
        # 关键提示
        key_reminder = Text(
            "掌握a、b、c，抛物线尽在掌握!",
            font="PingFang SC",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 3.8)
        
        self.play(FadeIn(key_reminder, shift=UP * 0.3), run_time=0.5)
        self.play(Indicate(key_reminder, scale_factor=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理总结
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(discriminant_hint),
            FadeOut(key_reminder),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多函数技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 抛物线符号
        decoration_symbols = VGroup()
        for i in range(6):
            angle = i * 2 * PI / 6
            pos = 2.8 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 1
            
            symbol = MathTex(
                r"\sim",
                font_size=40,
                color=[self.COLOR_PARABOLA, self.COLOR_VERTEX, self.COLOR_AXIS][i % 3]
            ).move_to(pos)
            
            decoration_symbols.add(symbol)
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in decoration_symbols],
            run_time=0.6
        )
        self.play(Rotate(decoration_symbols, angle=PI, run_time=1.5))
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration_symbols),
            run_time=1.0
        )
    
    def create_summary_card(self, content, title, color):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.18, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=26,
            color=WHITE,
            weight=BOLD
        )
        
        # 组合
        card = VGroup(icon, title_text, content).arrange(RIGHT, buff=0.3)
        
        return card


# 运行命令:
# manim -pql quadratic_general_form.py QuadraticGeneralForm  # 快速预览
# manim -qh quadratic_general_form.py QuadraticGeneralForm   # 高质量渲染
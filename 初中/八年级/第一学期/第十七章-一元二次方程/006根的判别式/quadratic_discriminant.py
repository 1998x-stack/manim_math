"""
一元二次方程的根的判别式 - Discriminant of Quadratic Equations
使用 Manim 创建的中学数学教学视频

内容: 判别式Δ=b²-4ac的三种情况及其几何意义
目标观众: 八年级学生
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


class QuadraticDiscriminant(Scene):
    """
    一元二次方程根的判别式教学动画
    
    场景顺序:
    1. 开场钩子
    2. 方程与判别式介绍
    3. 情况1: Δ>0 (两个不等实根)
    4. 情况2: Δ=0 (两个相等实根)
    5. 情况3: Δ<0 (无实根)
    6. 三种情况总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主方程
        self.COLOR_DELTA_POSITIVE = "#2ecc71" # 绿色 - Δ>0
        self.COLOR_DELTA_ZERO = "#f39c12"     # 橙色 - Δ=0
        self.COLOR_DELTA_NEGATIVE = "#e74c3c" # 红色 - Δ<0
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        
        # 执行动画序列
        self.show_opening()
        self.show_equation_intro()
        self.show_case_positive()
        self.show_case_zero()
        self.show_case_negative()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 6.8)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "如何不解方程\n就知道有几个根?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.3)
        
        # 三个不同的小抛物线快闪
        axes_small = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 3, 1],
            x_length=2.5,
            y_length=2,
            axis_config={"include_tip": False, "stroke_width": 1}
        ).scale(0.5)
        
        # Δ>0: 两个交点
        parabola_1 = axes_small.plot(
            lambda x: x**2 - 1,
            color=self.COLOR_DELTA_POSITIVE
        ).move_to(LEFT * 2.5 + UP * 2)
        axes_1 = axes_small.copy().move_to(parabola_1)
        
        # Δ=0: 相切
        parabola_2 = axes_small.plot(
            lambda x: x**2,
            color=self.COLOR_DELTA_ZERO
        ).move_to(UP * 2)
        axes_2 = axes_small.copy().move_to(parabola_2)
        
        # Δ<0: 无交点
        parabola_3 = axes_small.plot(
            lambda x: x**2 + 1,
            color=self.COLOR_DELTA_NEGATIVE
        ).move_to(RIGHT * 2.5 + UP * 2)
        axes_3 = axes_small.copy().move_to(parabola_3)
        
        self.play(
            FadeIn(axes_1), FadeIn(parabola_1),
            run_time=0.5
        )
        self.wait(0.2)
        self.play(
            FadeIn(axes_2), FadeIn(parabola_2),
            run_time=0.5
        )
        self.wait(0.2)
        self.play(
            FadeIn(axes_3), FadeIn(parabola_3),
            run_time=0.5
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(axes_1), FadeOut(parabola_1),
            FadeOut(axes_2), FadeOut(parabola_2),
            FadeOut(axes_3), FadeOut(parabola_3),
            run_time=0.5
        )
    
    def show_equation_intro(self):
        """场景2: 方程与判别式介绍"""
        # 标题
        title = Text(
            "一元二次方程",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 标准形式
        standard_form = MathTex(
            r"ax^2", r"+", r"bx", r"+", r"c", r"=", r"0",
            font_size=48
        ).move_to(UP * 4.2)
        
        constraint = MathTex(
            r"(a \neq 0)",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).next_to(standard_form, RIGHT, buff=0.3)
        
        self.play(Write(standard_form), run_time=1.0)
        self.play(FadeIn(constraint), run_time=0.4)
        self.wait(0.3)
        
        # 高亮系数
        self.play(
            standard_form[0].animate.set_color(RED),
            run_time=0.3
        )
        self.play(
            standard_form[2].animate.set_color(BLUE),
            run_time=0.3
        )
        self.play(
            standard_form[4].animate.set_color(GREEN),
            run_time=0.3
        )
        self.wait(0.3)
        
        # 恢复颜色
        self.play(
            standard_form.animate.set_color(WHITE),
            run_time=0.3
        )
        
        # 判别式公式
        delta_title = Text(
            "判别式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.delta_formula = MathTex(
            r"\Delta", r"=", r"b^2", r"-", r"4ac",
            font_size=52
        ).move_to(UP * 1.5)
        
        self.delta_formula[0].set_color(self.COLOR_HIGHLIGHT)  # Δ
        self.delta_formula[2].set_color(BLUE)   # b²
        self.delta_formula[4].set_color(RED)    # 4ac
        
        self.play(FadeIn(delta_title, shift=UP * 0.3), run_time=0.5)
        self.play(Write(self.delta_formula), run_time=1.0)
        self.play(Flash(self.delta_formula, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 说明
        explanation = Text(
            "判别式决定方程根的情况",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.2)
        
        # 清理并保留参考公式
        self.play(
            FadeOut(title),
            FadeOut(standard_form),
            FadeOut(constraint),
            FadeOut(delta_title),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 将判别式公式移到顶部作为参考
        self.reference_formula = self.delta_formula.copy().scale(0.6).move_to(UP * 6.5)
        self.play(
            Transform(self.delta_formula, self.reference_formula),
            run_time=0.5
        )
        self.remove(self.delta_formula)
        self.add(self.reference_formula)
    
    def show_case_positive(self):
        """场景3: Δ>0 - 两个不等实根"""
        # 副标题
        subtitle = Text(
            "情况1: Δ > 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_DELTA_POSITIVE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 例子方程
        example = MathTex(
            r"x^2", r"-", r"5x", r"+", r"6", r"=", r"0",
            font_size=40
        ).move_to(UP * 4.5)
        
        self.play(Write(example), run_time=0.7)
        self.wait(0.3)
        
        # 计算判别式
        calc_steps = VGroup(
            MathTex(r"\Delta = (-5)^2 - 4 \cdot 1 \cdot 6", font_size=32),
            MathTex(r"= 25 - 24", font_size=32),
            MathTex(r"= 1", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 3.2)
        
        for step in calc_steps:
            self.play(Write(step), run_time=0.6)
        
        # 结果
        result = MathTex(
            r"\Delta = 1 > 0",
            font_size=40,
            color=self.COLOR_DELTA_POSITIVE
        ).move_to(UP * 2)
        
        self.play(
            Write(result),
            Indicate(result, color=self.COLOR_DELTA_POSITIVE),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-1, 3, 1],
            x_length=6,
            y_length=3,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": False
            }
        ).move_to(UP * 0.2)
        
        self.play(Create(axes), run_time=1.0)
        
        # 绘制抛物线
        parabola = axes.plot(
            lambda x: x**2 - 5*x + 6,
            x_range=[0.8, 4.2],
            color=self.COLOR_DELTA_POSITIVE,
            stroke_width=3
        )
        
        self.play(Create(parabola), run_time=1.5)
        self.wait(0.3)
        
        # 标记两个交点
        # 求根: x = (5 ± 1) / 2 = 2 或 3
        x1, x2 = 2, 3
        point1 = axes.c2p(x1, 0)
        point2 = axes.c2p(x2, 0)
        
        dot1 = Dot(point1, color=YELLOW, radius=0.1)
        dot2 = Dot(point2, color=YELLOW, radius=0.1)
        
        self.play(FadeIn(dot1), FadeIn(dot2), run_time=0.5)
        self.play(
            Flash(dot1, color=YELLOW, flash_radius=0.25),
            Flash(dot2, color=YELLOW, flash_radius=0.25),
            run_time=0.4
        )
        
        # 数轴
        number_line = NumberLine(
            x_range=[0, 5, 1],
            length=6,
            include_numbers=True,
            font_size=20
        ).move_to(DOWN * 2.5)
        
        self.play(Create(number_line), run_time=0.7)
        
        # 根的位置
        root_pos1 = number_line.n2p(x1)
        root_pos2 = number_line.n2p(x2)
        
        root_dot1 = Dot(root_pos1, color=self.COLOR_DELTA_POSITIVE, radius=0.12)
        root_dot2 = Dot(root_pos2, color=self.COLOR_DELTA_POSITIVE, radius=0.12)
        
        root_label1 = MathTex(r"x_1=2", font_size=24).next_to(root_dot1, DOWN, buff=0.2)
        root_label2 = MathTex(r"x_2=3", font_size=24).next_to(root_dot2, DOWN, buff=0.2)
        
        self.play(
            FadeIn(root_dot1), FadeIn(root_dot2),
            run_time=0.5
        )
        self.play(
            Write(root_label1), Write(root_label2),
            run_time=0.5
        )
        
        # 结论
        conclusion = Text(
            "两个不相等的实数根",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_DELTA_POSITIVE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(example),
            FadeOut(calc_steps),
            FadeOut(result),
            FadeOut(axes),
            FadeOut(parabola),
            FadeOut(dot1), FadeOut(dot2),
            FadeOut(number_line),
            FadeOut(root_dot1), FadeOut(root_dot2),
            FadeOut(root_label1), FadeOut(root_label2),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_case_zero(self):
        """场景4: Δ=0 - 两个相等实根"""
        # 副标题
        subtitle = Text(
            "情况2: Δ = 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_DELTA_ZERO
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 例子方程
        example = MathTex(
            r"x^2", r"-", r"4x", r"+", r"4", r"=", r"0",
            font_size=40
        ).move_to(UP * 4.5)
        
        self.play(Write(example), run_time=0.7)
        self.wait(0.3)
        
        # 计算判别式
        calc_steps = VGroup(
            MathTex(r"\Delta = (-4)^2 - 4 \cdot 1 \cdot 4", font_size=32),
            MathTex(r"= 16 - 16", font_size=32),
            MathTex(r"= 0", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 3.2)
        
        for step in calc_steps:
            self.play(Write(step), run_time=0.6)
        
        # 结果
        result = MathTex(
            r"\Delta = 0",
            font_size=40,
            color=self.COLOR_DELTA_ZERO
        ).move_to(UP * 2)
        
        self.play(
            Write(result),
            Indicate(result, color=self.COLOR_DELTA_ZERO),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-1, 3, 1],
            x_length=6,
            y_length=3,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": False
            }
        ).move_to(UP * 0.2)
        
        self.play(Create(axes), run_time=1.0)
        
        # 绘制抛物线 (相切)
        parabola = axes.plot(
            lambda x: x**2 - 4*x + 4,
            x_range=[0.8, 4.2],
            color=self.COLOR_DELTA_ZERO,
            stroke_width=3
        )
        
        self.play(Create(parabola), run_time=1.5)
        self.wait(0.3)
        
        # 标记切点 (重根)
        # x = 4/2 = 2
        x_tangent = 2
        point_tangent = axes.c2p(x_tangent, 0)
        
        tangent_dot = Dot(point_tangent, color=YELLOW, radius=0.12)
        
        self.play(FadeIn(tangent_dot, scale=0.5), run_time=0.5)
        self.play(
            Flash(tangent_dot, color=YELLOW, flash_radius=0.3, num_lines=12),
            run_time=0.5
        )
        
        # "相切" 标注
        tangent_text = Text(
            "相切",
            font="Noto Sans CJK SC",
            font_size=20,
            color=YELLOW
        ).next_to(tangent_dot, UP, buff=0.3)
        
        self.play(FadeIn(tangent_text), run_time=0.4)
        
        # 数轴
        number_line = NumberLine(
            x_range=[0, 5, 1],
            length=6,
            include_numbers=True,
            font_size=20
        ).move_to(DOWN * 2.5)
        
        self.play(Create(number_line), run_time=0.7)
        
        # 重根位置
        root_pos = number_line.n2p(x_tangent)
        root_dot = Dot(root_pos, color=self.COLOR_DELTA_ZERO, radius=0.12)
        
        root_label = MathTex(r"x_1=x_2=2", font_size=24).next_to(root_dot, DOWN, buff=0.2)
        
        self.play(FadeIn(root_dot), run_time=0.5)
        self.play(Write(root_label), run_time=0.5)
        
        # 结论
        conclusion = Text(
            "两个相等的实数根 (重根)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_DELTA_ZERO
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(example),
            FadeOut(calc_steps),
            FadeOut(result),
            FadeOut(axes),
            FadeOut(parabola),
            FadeOut(tangent_dot),
            FadeOut(tangent_text),
            FadeOut(number_line),
            FadeOut(root_dot),
            FadeOut(root_label),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_case_negative(self):
        """场景5: Δ<0 - 无实根"""
        # 副标题
        subtitle = Text(
            "情况3: Δ < 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_DELTA_NEGATIVE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 例子方程
        example = MathTex(
            r"x^2", r"+", r"2x", r"+", r"5", r"=", r"0",
            font_size=40
        ).move_to(UP * 4.5)
        
        self.play(Write(example), run_time=0.7)
        self.wait(0.3)
        
        # 计算判别式
        calc_steps = VGroup(
            MathTex(r"\Delta = 2^2 - 4 \cdot 1 \cdot 5", font_size=32),
            MathTex(r"= 4 - 20", font_size=32),
            MathTex(r"= -16", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 3.2)
        
        for step in calc_steps:
            self.play(Write(step), run_time=0.6)
        
        # 结果
        result = MathTex(
            r"\Delta = -16 < 0",
            font_size=40,
            color=self.COLOR_DELTA_NEGATIVE
        ).move_to(UP * 2)
        
        self.play(
            Write(result),
            Indicate(result, color=self.COLOR_DELTA_NEGATIVE),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 1, 1],
            y_range=[0, 8, 2],
            x_length=6,
            y_length=3,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": False
            }
        ).move_to(UP * 0.2)
        
        self.play(Create(axes), run_time=1.0)
        
        # 绘制抛物线 (不相交)
        parabola = axes.plot(
            lambda x: x**2 + 2*x + 5,
            x_range=[-2.8, 0.8],
            color=self.COLOR_DELTA_NEGATIVE,
            stroke_width=3
        )
        
        self.play(Create(parabola), run_time=1.5)
        self.wait(0.5)
        
        # 闪烁x轴（强调没有交点）
        x_axis_line = Line(
            axes.c2p(-3, 0),
            axes.c2p(1, 0),
            color=YELLOW,
            stroke_width=5
        )
        
        self.play(Indicate(x_axis_line, color=YELLOW), run_time=0.8)
        self.remove(x_axis_line)
        
        # 叉号标记 (无交点)
        cross_mark = VGroup(
            Line(UP * 0.2 + LEFT * 0.2, DOWN * 0.2 + RIGHT * 0.2),
            Line(UP * 0.2 + RIGHT * 0.2, DOWN * 0.2 + LEFT * 0.2)
        ).set_color(RED).set_stroke(width=4).move_to(axes.c2p(-1, 0))
        
        self.play(Write(cross_mark), run_time=0.5)
        
        # 数轴
        number_line = NumberLine(
            x_range=[-3, 1, 1],
            length=6,
            include_numbers=True,
            font_size=20
        ).move_to(DOWN * 2.5)
        
        self.play(Create(number_line), run_time=0.7)
        
        # 问号 (无根)
        question_mark = Text(
            "?",
            font_size=60,
            color=self.COLOR_DELTA_NEGATIVE
        ).move_to(number_line.get_center() + UP * 0.5)
        
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.6)
        
        # 结论
        conclusion = Text(
            "没有实数根",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_DELTA_NEGATIVE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(example),
            FadeOut(calc_steps),
            FadeOut(result),
            FadeOut(axes),
            FadeOut(parabola),
            FadeOut(cross_mark),
            FadeOut(number_line),
            FadeOut(question_mark),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 三种情况总结"""
        # 标题
        title = Text(
            "判别式总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三行对比
        row_height = 1.8
        
        # 第一行: Δ>0
        row1_condition = MathTex(
            r"\Delta > 0",
            font_size=36,
            color=self.COLOR_DELTA_POSITIVE
        ).move_to(LEFT * 3 + UP * 3)
        
        row1_arrow = MathTex(
            r"\Longleftrightarrow",
            font_size=36
        ).next_to(row1_condition, RIGHT, buff=0.5)
        
        row1_result = Text(
            "两个不等实根",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DELTA_POSITIVE
        ).next_to(row1_arrow, RIGHT, buff=0.5)
        
        # 小图示1
        mini_axes1 = Axes(
            x_range=[-1, 1, 1],
            y_range=[-0.5, 0.5, 0.5],
            x_length=1.5,
            y_length=1,
            axis_config={"include_tip": False, "stroke_width": 1}
        ).scale(0.8).next_to(row1_result, RIGHT, buff=0.8)
        
        mini_parabola1 = mini_axes1.plot(
            lambda x: 0.5 * x**2 - 0.3,
            x_range=[-0.9, 0.9],
            color=self.COLOR_DELTA_POSITIVE,
            stroke_width=2
        )
        
        mini_dots1 = VGroup(
            Dot(mini_axes1.c2p(-0.77, 0), radius=0.05, color=YELLOW),
            Dot(mini_axes1.c2p(0.77, 0), radius=0.05, color=YELLOW)
        )
        
        self.play(
            FadeIn(row1_condition),
            FadeIn(row1_arrow),
            FadeIn(row1_result),
            run_time=0.8
        )
        self.play(
            Create(mini_axes1),
            Create(mini_parabola1),
            FadeIn(mini_dots1),
            run_time=0.6
        )
        self.wait(0.4)
        
        # 第二行: Δ=0
        row2_condition = MathTex(
            r"\Delta = 0",
            font_size=36,
            color=self.COLOR_DELTA_ZERO
        ).move_to(LEFT * 3 + UP * (3 - row_height))
        
        row2_arrow = MathTex(
            r"\Longleftrightarrow",
            font_size=36
        ).next_to(row2_condition, RIGHT, buff=0.5)
        
        row2_result = Text(
            "两个相等实根",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DELTA_ZERO
        ).next_to(row2_arrow, RIGHT, buff=0.5)
        
        # 小图示2
        mini_axes2 = Axes(
            x_range=[-1, 1, 1],
            y_range=[-0.5, 0.5, 0.5],
            x_length=1.5,
            y_length=1,
            axis_config={"include_tip": False, "stroke_width": 1}
        ).scale(0.8).next_to(row2_result, RIGHT, buff=0.8)
        
        mini_parabola2 = mini_axes2.plot(
            lambda x: 0.5 * x**2,
            x_range=[-0.9, 0.9],
            color=self.COLOR_DELTA_ZERO,
            stroke_width=2
        )
        
        mini_dot2 = Dot(mini_axes2.c2p(0, 0), radius=0.06, color=YELLOW)
        
        self.play(
            FadeIn(row2_condition),
            FadeIn(row2_arrow),
            FadeIn(row2_result),
            run_time=0.8
        )
        self.play(
            Create(mini_axes2),
            Create(mini_parabola2),
            FadeIn(mini_dot2),
            run_time=0.6
        )
        self.wait(0.4)
        
        # 第三行: Δ<0
        row3_condition = MathTex(
            r"\Delta < 0",
            font_size=36,
            color=self.COLOR_DELTA_NEGATIVE
        ).move_to(LEFT * 3 + UP * (3 - 2 * row_height))
        
        row3_arrow = MathTex(
            r"\Longleftrightarrow",
            font_size=36
        ).next_to(row3_condition, RIGHT, buff=0.5)
        
        row3_result = Text(
            "无实数根",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DELTA_NEGATIVE
        ).next_to(row3_arrow, RIGHT, buff=0.5)
        
        # 小图示3
        mini_axes3 = Axes(
            x_range=[-1, 1, 1],
            y_range=[-0.5, 0.5, 0.5],
            x_length=1.5,
            y_length=1,
            axis_config={"include_tip": False, "stroke_width": 1}
        ).scale(0.8).next_to(row3_result, RIGHT, buff=0.8)
        
        mini_parabola3 = mini_axes3.plot(
            lambda x: 0.5 * x**2 + 0.2,
            x_range=[-0.9, 0.9],
            color=self.COLOR_DELTA_NEGATIVE,
            stroke_width=2
        )
        
        self.play(
            FadeIn(row3_condition),
            FadeIn(row3_arrow),
            FadeIn(row3_result),
            run_time=0.8
        )
        self.play(
            Create(mini_axes3),
            Create(mini_parabola3),
            run_time=0.6
        )
        self.wait(0.4)
        
        # 框选整体
        all_rows = VGroup(
            row1_condition, row1_arrow, row1_result, mini_axes1, mini_parabola1, mini_dots1,
            row2_condition, row2_arrow, row2_result, mini_axes2, mini_parabola2, mini_dot2,
            row3_condition, row3_arrow, row3_result, mini_axes3, mini_parabola3
        )
        
        surrounding_box = SurroundingRectangle(
            all_rows,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            stroke_width=3
        )
        
        self.play(Create(surrounding_box), run_time=1.0)
        
        # 重点提示
        key_point = Text(
            "判别式是解题关键!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(2.5)
        
        # 清理所有
        self.play(
            FadeOut(title),
            FadeOut(all_rows),
            FadeOut(surrounding_box),
            FadeOut(key_point),
            FadeOut(self.reference_formula),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素 - 数学符号
        symbols = VGroup(
            MathTex(r"\Delta", font_size=40, color=self.COLOR_DELTA_POSITIVE),
            MathTex(r"x^2", font_size=40, color=self.COLOR_DELTA_ZERO),
            MathTex(r"\pm", font_size=40, color=self.COLOR_DELTA_NEGATIVE),
            MathTex(r"\sqrt{}", font_size=40, color=BLUE),
        ).arrange(RIGHT, buff=1.2).move_to(DOWN * 1.8)
        
        self.play(*[FadeIn(sym, scale=0.5) for sym in symbols], run_time=0.6)
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        
        # 小抛物线装饰
        deco_axes = Axes(
            x_range=[-1, 1],
            y_range=[-0.3, 0.5],
            x_length=1.2,
            y_length=0.8,
            axis_config={"stroke_width": 1, "include_tip": False}
        ).scale(0.7)
        
        deco_parabolas = VGroup(
            deco_axes.copy().move_to(DOWN * 3.5 + LEFT * 2.5),
            deco_axes.copy().move_to(DOWN * 3.5),
            deco_axes.copy().move_to(DOWN * 3.5 + RIGHT * 2.5)
        )
        
        deco_curves = VGroup(
            deco_parabolas[0].plot(lambda x: 0.3*x**2 - 0.15, color=self.COLOR_DELTA_POSITIVE),
            deco_parabolas[1].plot(lambda x: 0.3*x**2, color=self.COLOR_DELTA_ZERO),
            deco_parabolas[2].plot(lambda x: 0.3*x**2 + 0.15, color=self.COLOR_DELTA_NEGATIVE)
        )
        
        self.play(
            *[Create(axes) for axes in deco_parabolas],
            *[Create(curve) for curve in deco_curves],
            run_time=0.8
        )
        
        self.wait(1.2)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            FadeOut(deco_parabolas),
            FadeOut(deco_curves),
            run_time=1.0
        )


# 运行命令:
# manim -pql quadratic_discriminant.py QuadraticDiscriminant  # 快速预览
# manim -qh quadratic_discriminant.py QuadraticDiscriminant   # 高质量渲染
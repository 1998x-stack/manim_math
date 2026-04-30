"""
函数的运算 - Function Operations Animation
使用 Manim 创建的高中数学教学视频

内容: 函数的加减乘除和复合运算
目标观众: 高一学生
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


class FunctionOperations(Scene):
    """
    函数运算教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 加法运算 (f+g)(x)
    3. 减法运算 (f-g)(x)
    4. 乘法运算 (f·g)(x)
    5. 除法运算 (f/g)(x) - 强调定义域
    6. 复合函数 f(g(x))
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_F = "#3498db"         # 蓝色 - f(x)
        self.COLOR_G = "#e74c3c"         # 红色 - g(x)
        self.COLOR_SUM = "#2ecc71"       # 绿色 - 加法
        self.COLOR_DIFF = "#9b59b6"      # 紫色 - 减法
        self.COLOR_PRODUCT = "#f39c12"   # 橙色 - 乘法
        self.COLOR_QUOTIENT = "#e91e63"  # 品红 - 除法
        self.COLOR_COMPOSITE = "#ffd700" # 金色 - 复合
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 字体配置
        self.FONT = "PingFang SC"
        
        # 定义函数
        self.f = lambda x: x**2
        self.g = lambda x: 2*x
        
        # 执行动画序列
        self.show_opening()
        self.show_addition()
        self.show_subtraction()
        self.show_multiplication()
        self.show_division()
        self.show_composition()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "函数也能做运算?",
            font=self.FONT,
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.4)
        
        # 简单展示两个函数
        # 小型坐标系（左侧）
        axes_left = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 4, 1],
            x_length=3,
            y_length=3,
            axis_config={"include_tip": False, "stroke_width": 2},
        ).move_to(LEFT * 2 + UP * 2.5).scale(0.8)
        
        f_graph_small = axes_left.plot(self.f, color=self.COLOR_F, stroke_width=4, x_range=[-1.8, 1.8])
        f_label_small = MathTex(r"f(x)=x^2", font_size=24, color=self.COLOR_F).next_to(axes_left, DOWN, buff=0.2)
        
        # 小型坐标系（右侧）
        axes_right = Axes(
            x_range=[-2, 2, 1],
            y_range=[-4, 4, 2],
            x_length=3,
            y_length=3,
            axis_config={"include_tip": False, "stroke_width": 2},
        ).move_to(RIGHT * 2 + UP * 2.5).scale(0.8)
        
        g_graph_small = axes_right.plot(self.g, color=self.COLOR_G, stroke_width=4, x_range=[-1.8, 1.8])
        g_label_small = MathTex(r"g(x)=2x", font_size=24, color=self.COLOR_G).next_to(axes_right, DOWN, buff=0.2)
        
        self.play(
            Create(axes_left),
            Create(f_graph_small),
            FadeIn(f_label_small),
            run_time=1.0
        )
        
        self.play(
            Create(axes_right),
            Create(g_graph_small),
            FadeIn(g_label_small),
            run_time=1.0
        )
        
        # 问号
        question = Text("?", font=self.FONT, font_size=60, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 2)
        self.play(FadeIn(question, scale=1.5), run_time=0.4)
        self.play(Flash(question, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(axes_left),
            FadeOut(axes_right),
            FadeOut(f_graph_small),
            FadeOut(g_graph_small),
            FadeOut(f_label_small),
            FadeOut(g_label_small),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_addition(self):
        """场景2: 加法运算 (f+g)(x)"""
        # 标题
        title = MathTex(
            r"(f+g)(x) = f(x) + g(x)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 10, 2],
            x_length=7,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": False
            },
        ).move_to(UP * 1)
        
        self.play(Create(axes), run_time=0.7)
        
        # f(x) 图像
        f_graph = axes.plot(self.f, color=self.COLOR_F, stroke_width=4, x_range=[-2.8, 2.8])
        f_label = MathTex(r"f(x)=x^2", font_size=24, color=self.COLOR_F).next_to(axes.c2p(2, 4), RIGHT, buff=0.2)
        
        self.play(Create(f_graph), run_time=1.0)
        self.play(FadeIn(f_label), run_time=0.5)
        
        # g(x) 图像
        g_graph = axes.plot(self.g, color=self.COLOR_G, stroke_width=4, x_range=[-2.8, 2.8])
        g_label = MathTex(r"g(x)=2x", font_size=24, color=self.COLOR_G).next_to(axes.c2p(2, 4), LEFT, buff=0.2)
        
        self.play(Create(g_graph), run_time=1.0)
        self.play(FadeIn(g_label), run_time=0.5)
        
        self.wait(0.5)
        
        # 演示：在x=2处相加
        x_val = 2
        f_val = self.f(x_val)
        g_val = self.g(x_val)
        sum_val = f_val + g_val
        
        # 点和虚线
        dot_x = Dot(axes.c2p(x_val, 0), color=self.COLOR_HIGHLIGHT, radius=0.08)
        x_label = MathTex(r"x=2", font_size=20, color=WHITE).next_to(dot_x, DOWN, buff=0.15)
        
        vline_f = DashedLine(axes.c2p(x_val, 0), axes.c2p(x_val, f_val), color=self.COLOR_F, stroke_width=2)
        vline_g = DashedLine(axes.c2p(x_val, f_val), axes.c2p(x_val, sum_val), color=self.COLOR_G, stroke_width=2)
        
        dot_f = Dot(axes.c2p(x_val, f_val), color=self.COLOR_F, radius=0.08)
        dot_sum = Dot(axes.c2p(x_val, sum_val), color=self.COLOR_SUM, radius=0.1)
        
        self.play(FadeIn(dot_x), FadeIn(x_label), run_time=0.5)
        self.play(Create(vline_f), FadeIn(dot_f), run_time=0.5)
        self.play(Create(vline_g), run_time=0.5)
        
        # 箭头和标注
        arrow = Arrow(
            axes.c2p(x_val, f_val) + RIGHT * 0.3,
            axes.c2p(x_val, sum_val) + RIGHT * 0.3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(dot_sum, scale=1.2), run_time=0.5)
        self.play(Flash(dot_sum, color=self.COLOR_SUM, flash_radius=0.3), run_time=0.4)
        
        # (f+g)(x) 图像
        sum_graph = axes.plot(
            lambda x: self.f(x) + self.g(x),
            color=self.COLOR_SUM,
            stroke_width=5,
            x_range=[-2.8, 2.8]
        )
        
        self.play(Create(sum_graph), run_time=1.5)
        
        # 说明
        explain = Text(
            "逐点相加",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(dot_x),
            FadeOut(x_label),
            FadeOut(vline_f),
            FadeOut(vline_g),
            FadeOut(dot_f),
            FadeOut(dot_sum),
            FadeOut(arrow),
            FadeOut(sum_graph),
            FadeOut(explain),
            f_graph.animate.set_opacity(0.3),
            g_graph.animate.set_opacity(0.3),
            run_time=0.6
        )
        
        # 保存坐标系和图像供后续使用
        self.axes = axes
        self.f_graph = f_graph
        self.g_graph = g_graph
        self.f_label = f_label
        self.g_label = g_label
    
    def show_subtraction(self):
        """场景3: 减法运算 (f-g)(x)"""
        # 标题
        title = MathTex(
            r"(f-g)(x) = f(x) - g(x)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 恢复图像高亮
        self.play(
            self.f_graph.animate.set_opacity(1),
            self.g_graph.animate.set_opacity(1),
            run_time=0.5
        )
        
        # 演示：在x=1处相减
        x_val = 1
        f_val = self.f(x_val)
        g_val = self.g(x_val)
        diff_val = f_val - g_val
        
        dot_x = Dot(self.axes.c2p(x_val, 0), color=self.COLOR_HIGHLIGHT, radius=0.08)
        x_label = MathTex(r"x=1", font_size=20, color=WHITE).next_to(dot_x, DOWN, buff=0.15)
        
        # f(x) 到 g(x) 的距离
        brace = BraceBetweenPoints(
            self.axes.c2p(x_val, g_val),
            self.axes.c2p(x_val, f_val),
            direction=RIGHT,
            color=self.COLOR_DIFF
        )
        brace_label = MathTex(r"f-g", font_size=20, color=self.COLOR_DIFF).next_to(brace, RIGHT, buff=0.1)
        
        self.play(FadeIn(dot_x), FadeIn(x_label), run_time=0.5)
        self.play(FadeIn(brace), FadeIn(brace_label), run_time=0.8)
        
        # (f-g)(x) 图像
        diff_graph = self.axes.plot(
            lambda x: self.f(x) - self.g(x),
            color=self.COLOR_DIFF,
            stroke_width=5,
            x_range=[-2.8, 2.8]
        )
        
        self.play(Create(diff_graph), run_time=1.5)
        
        # 说明
        explain = Text(
            "逐点相减",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(dot_x),
            FadeOut(x_label),
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(diff_graph),
            FadeOut(explain),
            self.f_graph.animate.set_opacity(0.3),
            self.g_graph.animate.set_opacity(0.3),
            run_time=0.6
        )
    
    def show_multiplication(self):
        """场景4: 乘法运算 (f·g)(x)"""
        # 标题
        title = MathTex(
            r"(f \cdot g)(x) = f(x) \cdot g(x)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 恢复图像
        self.play(
            self.f_graph.animate.set_opacity(1),
            self.g_graph.animate.set_opacity(1),
            run_time=0.5
        )
        
        # 演示：在x=1.5处相乘
        x_val = 1.5
        f_val = self.f(x_val)
        g_val = self.g(x_val)
        prod_val = f_val * g_val
        
        dot_x = Dot(self.axes.c2p(x_val, 0), color=self.COLOR_HIGHLIGHT, radius=0.08)
        
        # 显示计算过程
        calc = VGroup(
            MathTex(r"f(1.5) = 2.25", font_size=22, color=self.COLOR_F),
            MathTex(r"\times", font_size=22, color=WHITE),
            MathTex(r"g(1.5) = 3", font_size=22, color=self.COLOR_G),
            MathTex(r"=", font_size=22, color=WHITE),
            MathTex(r"6.75", font_size=22, color=self.COLOR_PRODUCT)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.5)
        
        self.play(FadeIn(dot_x), run_time=0.5)
        self.play(FadeIn(calc[0]), run_time=0.5)
        self.play(FadeIn(calc[1]), FadeIn(calc[2]), run_time=0.5)
        self.play(FadeIn(calc[3]), FadeIn(calc[4]), run_time=0.5)
        self.play(Flash(calc[4], color=self.COLOR_PRODUCT), run_time=0.4)
        
        # (f·g)(x) 图像
        product_graph = self.axes.plot(
            lambda x: self.f(x) * self.g(x),
            color=self.COLOR_PRODUCT,
            stroke_width=5,
            x_range=[-2.8, 2.8]
        )
        
        self.play(Create(product_graph), run_time=1.5)
        
        # 说明
        explain = Text(
            "逐点相乘",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(dot_x),
            FadeOut(calc),
            FadeOut(product_graph),
            FadeOut(explain),
            self.f_graph.animate.set_opacity(0.3),
            self.g_graph.animate.set_opacity(0.3),
            run_time=0.6
        )
    
    def show_division(self):
        """场景5: 除法运算 (f/g)(x) - 强调定义域"""
        # 标题
        title = MathTex(
            r"(f / g)(x) = \frac{f(x)}{g(x)}, \quad g(x) \neq 0",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=1.0)
        
        # 恢复图像
        self.play(
            self.f_graph.animate.set_opacity(1),
            self.g_graph.animate.set_opacity(1),
            run_time=0.5
        )
        
        # 标记 x=0 处
        warning_dot = Dot(self.axes.c2p(0, 0), color=RED, radius=0.12)
        warning_circle = Circle(radius=0.25, color=RED, stroke_width=4).move_to(self.axes.c2p(0, 0))
        warning_text = Text("⚠", font_size=40, color=RED).move_to(self.axes.c2p(0, 0) + UP * 0.6)
        
        self.play(
            FadeIn(warning_dot, scale=1.5),
            Create(warning_circle),
            run_time=0.5
        )
        self.play(FadeIn(warning_text, scale=1.5), run_time=0.3)
        self.play(Flash(warning_text, color=RED, flash_radius=0.5), run_time=0.4)
        
        # 说明
        explain = Text(
            "g(0)=0, 除法无定义",
            font=self.FONT,
            font_size=24,
            color=RED
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.6)
        self.wait(1.5)
        
        # (f/g)(x) 图像（跳过x=0）
        # 分段绘制：x<0 和 x>0
        quotient_graph_left = self.axes.plot(
            lambda x: self.f(x) / self.g(x),
            color=self.COLOR_QUOTIENT,
            stroke_width=5,
            x_range=[-2.8, -0.1]
        )
        
        quotient_graph_right = self.axes.plot(
            lambda x: self.f(x) / self.g(x),
            color=self.COLOR_QUOTIENT,
            stroke_width=5,
            x_range=[0.1, 2.8]
        )
        
        # 虚线标记间断
        dashed_line = DashedLine(
            self.axes.c2p(0, -2),
            self.axes.c2p(0, 10),
            color=RED,
            stroke_width=2,
            dash_length=0.1
        )
        
        self.play(
            Create(quotient_graph_left),
            Create(quotient_graph_right),
            Create(dashed_line),
            run_time=2.0
        )
        
        # 定义域说明
        domain_text = Text(
            "定义域: x ≠ 0",
            font=self.FONT,
            font_size=24,
            color=self.COLOR_QUOTIENT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(domain_text), run_time=0.6)
        self.wait(2.0)  # 强调停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(warning_dot),
            FadeOut(warning_circle),
            FadeOut(warning_text),
            FadeOut(explain),
            FadeOut(quotient_graph_left),
            FadeOut(quotient_graph_right),
            FadeOut(dashed_line),
            FadeOut(domain_text),
            FadeOut(self.f_graph),
            FadeOut(self.g_graph),
            FadeOut(self.f_label),
            FadeOut(self.g_label),
            FadeOut(self.axes),
            run_time=0.8
        )
    
    def show_composition(self):
        """场景6: 复合函数 f(g(x))"""
        # 标题
        title = MathTex(
            r"\text{复合函数: } f(g(x))",
            font_size=32,
            color=WHITE,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 流程图
        flowchart = VGroup()
        
        # 输入
        input_box = Rectangle(width=1.2, height=0.6, color=WHITE, fill_opacity=0.1)
        input_text = MathTex(r"x", font_size=28).move_to(input_box)
        input_group = VGroup(input_box, input_text).move_to(LEFT * 3 + UP * 3)
        
        # 箭头1
        arrow1 = Arrow(input_group.get_right(), input_group.get_right() + RIGHT * 1.2, color=self.COLOR_HIGHLIGHT, buff=0)
        g_label = MathTex(r"g", font_size=24, color=self.COLOR_G).next_to(arrow1, UP, buff=0.1)
        
        # g(x)
        g_box = Rectangle(width=1.5, height=0.6, color=self.COLOR_G, fill_opacity=0.2)
        g_text = MathTex(r"g(x)", font_size=28, color=self.COLOR_G).move_to(g_box)
        g_group = VGroup(g_box, g_text).next_to(arrow1, RIGHT, buff=0)
        
        # 箭头2
        arrow2 = Arrow(g_group.get_right(), g_group.get_right() + RIGHT * 1.2, color=self.COLOR_HIGHLIGHT, buff=0)
        f_label = MathTex(r"f", font_size=24, color=self.COLOR_F).next_to(arrow2, UP, buff=0.1)
        
        # f(g(x))
        result_box = Rectangle(width=1.8, height=0.6, color=self.COLOR_COMPOSITE, fill_opacity=0.2)
        result_text = MathTex(r"f(g(x))", font_size=28, color=self.COLOR_COMPOSITE).move_to(result_box)
        result_group = VGroup(result_box, result_text).next_to(arrow2, RIGHT, buff=0)
        
        flowchart.add(input_group, arrow1, g_label, g_group, arrow2, f_label, result_group)
        
        self.play(FadeIn(flowchart), run_time=1.0)
        
        # 示例：x=1 流动
        moving_dot = Dot(input_group.get_center(), color=YELLOW, radius=0.1)
        
        step1_text = MathTex(r"g(1) = 2", font_size=24, color=self.COLOR_G).move_to(DOWN * 4.5)
        step2_text = MathTex(r"f(2) = 4", font_size=24, color=self.COLOR_F).move_to(DOWN * 5.3)
        
        self.play(FadeIn(moving_dot, scale=1.5), run_time=0.3)
        self.play(MoveAlongPath(moving_dot, arrow1), run_time=1.0)
        self.play(FadeIn(step1_text), run_time=0.5)
        
        self.play(moving_dot.animate.move_to(g_group.get_center()), run_time=0.3)
        self.play(Flash(moving_dot, color=self.COLOR_G), run_time=0.3)
        
        self.play(MoveAlongPath(moving_dot, arrow2), run_time=1.0)
        self.play(FadeIn(step2_text), run_time=0.5)
        
        self.play(moving_dot.animate.move_to(result_group.get_center()), run_time=0.3)
        self.play(Flash(moving_dot, color=self.COLOR_COMPOSITE), run_time=0.3)
        
        self.wait(1.0)
        
        # 淡出流程图
        self.play(
            FadeOut(flowchart),
            FadeOut(moving_dot),
            FadeOut(step1_text),
            FadeOut(step2_text),
            run_time=0.6
        )
        
        # 重建坐标系和图像
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 16, 4],
            x_length=7,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": False
            },
        ).move_to(UP * 1)
        
        self.play(Create(axes), run_time=0.7)
        
        # f(x), g(x) 淡入
        f_graph = axes.plot(self.f, color=self.COLOR_F, stroke_width=3, x_range=[-2.8, 2.8])
        g_graph = axes.plot(self.g, color=self.COLOR_G, stroke_width=3, x_range=[-2.8, 2.8])
        
        f_label = MathTex(r"f", font_size=20, color=self.COLOR_F).next_to(axes.c2p(2, 4), UR, buff=0.1)
        g_label = MathTex(r"g", font_size=20, color=self.COLOR_G).next_to(axes.c2p(2, 4), UL, buff=0.1)
        
        self.play(
            Create(f_graph),
            Create(g_graph),
            FadeIn(f_label),
            FadeIn(g_label),
            run_time=1.0
        )
        
        # f∘g(x) = f(g(x)) = f(2x) = (2x)² = 4x²
        composite_graph = axes.plot(
            lambda x: self.f(self.g(x)),
            color=self.COLOR_COMPOSITE,
            stroke_width=5,
            x_range=[-2, 2]  # 缩小范围避免超界
        )
        
        composite_label = MathTex(
            r"f \circ g",
            font_size=24,
            color=self.COLOR_COMPOSITE
        ).next_to(axes.c2p(1.5, 9), RIGHT, buff=0.2)
        
        self.play(Create(composite_graph), run_time=1.5)
        self.play(FadeIn(composite_label), run_time=0.5)
        
        # 说明
        explain = Text(
            "先算 g，再算 f",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(f_graph),
            FadeOut(g_graph),
            FadeOut(composite_graph),
            FadeOut(f_label),
            FadeOut(g_label),
            FadeOut(composite_label),
            FadeOut(explain),
            run_time=0.8
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 标题
        title = Text(
            "函数的五种运算",
            font=self.FONT,
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 五张卡片
        cards = VGroup()
        
        card_data = [
            (r"(f+g)(x) = f(x) + g(x)", self.COLOR_SUM, UP * 3.5),
            (r"(f-g)(x) = f(x) - g(x)", self.COLOR_DIFF, UP * 2),
            (r"(f \cdot g)(x) = f(x) \cdot g(x)", self.COLOR_PRODUCT, UP * 0.5),
            (r"(f / g)(x) = \frac{f(x)}{g(x)}, \; g(x) \neq 0", self.COLOR_QUOTIENT, DOWN * 1),
            (r"f(g(x)) \text{ - 先算 } g\text{，再算 } f", self.COLOR_COMPOSITE, DOWN * 2.5),
        ]
        
        for formula, color, pos in card_data:
            # 使用 ctex 模板支持中文
            if "先算" in formula:
                card_text = MathTex(
                    formula,
                    font_size=22,
                    color=color,
                    tex_template=TexTemplateLibrary.ctex
                )
            else:
                card_text = MathTex(formula, font_size=22, color=color)
            
            card_bg = Rectangle(
                width=card_text.width + 0.4,
                height=card_text.height + 0.3,
                color=color,
                fill_opacity=0.1,
                stroke_width=2
            ).move_to(card_text)
            
            card = VGroup(card_bg, card_text).move_to(pos)
            card.shift(LEFT * 10)  # 初始在屏幕外
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.6)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(0.5)
        
        # 定义域提示框
        domain_box = Rectangle(
            width=7,
            height=1,
            color=RED,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(DOWN * 4.5)
        
        domain_text = Text(
            "⚠ 注意定义域！",
            font=self.FONT,
            font_size=28,
            color=RED
        ).move_to(domain_box)
        
        self.play(
            FadeIn(domain_box),
            FadeIn(domain_text, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(domain_text, color=RED, flash_radius=0.8), run_time=0.5)
        
        self.wait(1.5)
        
        # 片尾
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(domain_box),
            FadeOut(domain_text),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多函数技巧！",
            font=self.FONT,
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰：小函数图标
        icons = VGroup()
        for i, color in enumerate([self.COLOR_SUM, self.COLOR_DIFF, self.COLOR_PRODUCT, 
                                    self.COLOR_QUOTIENT, self.COLOR_COMPOSITE]):
            icon = Circle(radius=0.25, color=color, fill_opacity=0.8, stroke_width=2)
            icon.move_to(LEFT * 2 + RIGHT * i * 1 + DOWN * 2.5)
            icons.add(icon)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.play(icons.animate.shift(UP * 0.2).scale(1.1), run_time=0.5)
        self.play(icons.animate.shift(DOWN * 0.2).scale(1/1.1), run_time=0.5)
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql function_operations.py FunctionOperations  # 快速预览
# manim -qm function_operations.py FunctionOperations   # 中等质量
# manim -qh function_operations.py FunctionOperations   # 高质量 (推荐)
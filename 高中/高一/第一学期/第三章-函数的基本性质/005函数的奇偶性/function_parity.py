"""
函数的奇偶性 - Function Parity Animation
使用 Manim 创建的高中数学教学视频

内容: 偶函数和奇函数的定义、对称性和判断方法
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


class FunctionParity(Scene):
    """
    函数奇偶性教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 偶函数定义 - y轴对称
    3. 奇函数定义 - 原点对称
    4. 对称性可视化对比
    5. 判断方法两步法
    6. 特殊性质 f(0)=0
    7. 综合示例
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_EVEN = "#e74c3c"      # 红色 - 偶函数
        self.COLOR_ODD = "#3498db"       # 蓝色 - 奇函数
        self.COLOR_Y_AXIS = "#2ecc71"    # 绿色 - y轴
        self.COLOR_ORIGIN = "#f39c12"    # 橙色 - 原点
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 字体配置
        self.FONT = "PingFang SC"
        
        # 定义示例函数
        self.f_even = lambda x: x**2
        self.f_odd = lambda x: x**3
        
        # 执行动画序列
        self.show_opening()
        self.show_even_function()
        self.show_odd_function()
        self.show_symmetry_comparison()
        self.show_判断方法()
        self.show_special_property()
        self.show_examples()
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
            "函数也有对称美？",
            font=self.FONT,
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.4)
        
        # 两个神秘函数图像预览
        # 左侧：偶函数
        axes_left = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1, 4, 1],
            x_length=3,
            y_length=3,
            axis_config={"include_tip": False, "stroke_width": 2},
        ).move_to(LEFT * 2 + UP * 2.5).scale(0.7)
        
        even_preview = axes_left.plot(self.f_even, color=self.COLOR_EVEN, stroke_width=4, x_range=[-1.8, 1.8])
        even_label = Text("?", font=self.FONT, font_size=32, color=self.COLOR_EVEN).next_to(axes_left, DOWN, buff=0.2)
        
        # 右侧：奇函数
        axes_right = Axes(
            x_range=[-2, 2, 1],
            y_range=[-8, 8, 4],
            x_length=3,
            y_length=3,
            axis_config={"include_tip": False, "stroke_width": 2},
        ).move_to(RIGHT * 2 + UP * 2.5).scale(0.7)
        
        odd_preview = axes_right.plot(self.f_odd, color=self.COLOR_ODD, stroke_width=4, x_range=[-1.8, 1.8])
        odd_label = Text("?", font=self.FONT, font_size=32, color=self.COLOR_ODD).next_to(axes_right, DOWN, buff=0.2)
        
        self.play(
            FadeIn(axes_left, shift=RIGHT * 0.5),
            Create(even_preview),
            FadeIn(even_label),
            run_time=1.0
        )
        
        self.play(
            FadeIn(axes_right, shift=LEFT * 0.5),
            Create(odd_preview),
            FadeIn(odd_label),
            run_time=1.0
        )
        
        # 对称符号提示
        symmetry_icon_left = Text("⟷", font_size=40, color=self.COLOR_Y_AXIS).move_to(LEFT * 2 + DOWN * 1.5)
        symmetry_icon_right = Text("↺", font_size=40, color=self.COLOR_ORIGIN).move_to(RIGHT * 2 + DOWN * 1.5)
        
        self.play(
            FadeIn(symmetry_icon_left, scale=1.5),
            FadeIn(symmetry_icon_right, scale=1.5),
            run_time=0.5
        )
        self.play(
            Flash(symmetry_icon_left, color=self.COLOR_Y_AXIS),
            Flash(symmetry_icon_right, color=self.COLOR_ORIGIN),
            run_time=0.5
        )
        
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(axes_left),
            FadeOut(axes_right),
            FadeOut(even_preview),
            FadeOut(odd_preview),
            FadeOut(even_label),
            FadeOut(odd_label),
            FadeOut(symmetry_icon_left),
            FadeOut(symmetry_icon_right),
            run_time=0.5
        )
    
    def show_even_function(self):
        """场景2: 偶函数定义 - y轴对称"""
        # 标题
        title = Text(
            "偶函数 Even Function",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_EVEN
        ).move_to(UP * 5.5)
        
        # 定义公式
        definition = MathTex(
            r"f(-x) = f(x)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.7)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 2],
            x_length=7,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "include_tip": False
            },
        ).move_to(UP * 0.5)
        
        self.play(Create(axes), run_time=0.7)
        
        # f(x) = x² 图像
        even_graph = axes.plot(
            self.f_even,
            color=self.COLOR_EVEN,
            stroke_width=5,
            x_range=[-2.8, 2.8]
        )
        
        graph_label = MathTex(
            r"f(x) = x^2",
            font_size=24,
            color=self.COLOR_EVEN
        ).next_to(axes.c2p(2, 4), UR, buff=0.2)
        
        self.play(Create(even_graph), run_time=1.0)
        self.play(FadeIn(graph_label), run_time=0.5)
        
        # 高亮 y轴
        y_axis_line = Line(
            axes.c2p(0, -1),
            axes.c2p(0, 9),
            color=self.COLOR_Y_AXIS,
            stroke_width=6
        )
        
        self.play(Create(y_axis_line), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "关于 y 轴对称",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(0.5)
        
        # 演示对称性：选取 x=2 的点
        x_val = 2
        y_val = self.f_even(x_val)
        
        # 正值点
        dot_pos = Dot(axes.c2p(x_val, y_val), color=self.COLOR_HIGHLIGHT, radius=0.1)
        dot_pos_label = MathTex(
            r"(2, 4)",
            font_size=20,
            color=WHITE
        ).next_to(dot_pos, UR, buff=0.15)
        
        self.play(FadeIn(dot_pos, scale=1.3), FadeIn(dot_pos_label), run_time=0.5)
        
        # 镜像线（竖直虚线）
        mirror_line = DashedLine(
            axes.c2p(x_val, 0),
            axes.c2p(x_val, y_val),
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        
        self.play(Create(mirror_line), run_time=0.5)
        
        # 负值对称点
        dot_neg = Dot(axes.c2p(-x_val, y_val), color=self.COLOR_HIGHLIGHT, radius=0.1)
        dot_neg_label = MathTex(
            r"(-2, 4)",
            font_size=20,
            color=WHITE
        ).next_to(dot_neg, UL, buff=0.15)
        
        mirror_line_neg = DashedLine(
            axes.c2p(-x_val, 0),
            axes.c2p(-x_val, y_val),
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        
        self.play(
            Create(mirror_line_neg),
            FadeIn(dot_neg, scale=1.3),
            FadeIn(dot_neg_label),
            run_time=0.8
        )
        
        # 水平虚线连接两点
        horizontal_line = DashedLine(
            axes.c2p(-x_val, y_val),
            axes.c2p(x_val, y_val),
            color=self.COLOR_Y_AXIS,
            stroke_width=3
        )
        
        self.play(Create(horizontal_line), run_time=0.6)
        
        # 标注 f(-2) = f(2)
        equality = MathTex(
            r"f(-2) = f(2) = 4",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(equality), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(dot_pos),
            FadeOut(dot_neg),
            FadeOut(dot_pos_label),
            FadeOut(dot_neg_label),
            FadeOut(mirror_line),
            FadeOut(mirror_line_neg),
            FadeOut(horizontal_line),
            FadeOut(equality),
            FadeOut(explain),
            FadeOut(y_axis_line),
            FadeOut(even_graph),
            FadeOut(graph_label),
            FadeOut(axes),
            run_time=0.6
        )
    
    def show_odd_function(self):
        """场景3: 奇函数定义 - 原点对称"""
        # 标题
        title = Text(
            "奇函数 Odd Function",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_ODD
        ).move_to(UP * 5.5)
        
        # 定义公式
        definition = MathTex(
            r"f(-x) = -f(x)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.7)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-27, 27, 9],
            x_length=7,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "include_tip": False,
                "numbers_to_exclude": [0]  # 原点不标数字
            },
        ).move_to(UP * 0.5)
        
        self.play(Create(axes), run_time=0.7)
        
        # f(x) = x³ 图像
        odd_graph = axes.plot(
            self.f_odd,
            color=self.COLOR_ODD,
            stroke_width=5,
            x_range=[-2.8, 2.8]
        )
        
        graph_label = MathTex(
            r"f(x) = x^3",
            font_size=24,
            color=self.COLOR_ODD
        ).next_to(axes.c2p(2, 8), UR, buff=0.2)
        
        self.play(Create(odd_graph), run_time=1.0)
        self.play(FadeIn(graph_label), run_time=0.5)
        
        # 高亮原点
        origin_dot = Dot(axes.c2p(0, 0), color=self.COLOR_ORIGIN, radius=0.15)
        origin_label = MathTex(
            r"O",
            font_size=24,
            color=self.COLOR_ORIGIN
        ).next_to(origin_dot, DR, buff=0.15)
        
        self.play(
            FadeIn(origin_dot, scale=1.5),
            FadeIn(origin_label),
            run_time=0.5
        )
        self.play(Indicate(origin_dot, color=self.COLOR_ORIGIN, scale_factor=1.5), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "关于原点对称",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(0.5)
        
        # 演示对称性：选取 x=2 的点
        x_val = 2
        y_val = self.f_odd(x_val)
        
        # 正值点
        dot_pos = Dot(axes.c2p(x_val, y_val), color=self.COLOR_HIGHLIGHT, radius=0.1)
        dot_pos_label = MathTex(
            r"(2, 8)",
            font_size=20,
            color=WHITE
        ).next_to(dot_pos, UR, buff=0.15)
        
        self.play(FadeIn(dot_pos, scale=1.3), FadeIn(dot_pos_label), run_time=0.5)
        
        # 通过原点的连线
        line_to_origin = Line(
            axes.c2p(x_val, y_val),
            axes.c2p(0, 0),
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        self.play(Create(line_to_origin), run_time=0.5)
        
        # 延长到对称点
        line_through_origin = Line(
            axes.c2p(x_val, y_val),
            axes.c2p(-x_val, -y_val),
            color=self.COLOR_ORIGIN,
            stroke_width=4
        )
        
        self.play(Transform(line_to_origin, line_through_origin), run_time=0.5)
        
        # 负值对称点
        dot_neg = Dot(axes.c2p(-x_val, -y_val), color=self.COLOR_HIGHLIGHT, radius=0.1)
        dot_neg_label = MathTex(
            r"(-2, -8)",
            font_size=20,
            color=WHITE
        ).next_to(dot_neg, DL, buff=0.15)
        
        self.play(
            FadeIn(dot_neg, scale=1.3),
            FadeIn(dot_neg_label),
            run_time=0.8
        )
        
        # 标注 f(-2) = -f(2)
        equality = MathTex(
            r"f(-2) = -f(2) = -8",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(equality), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(dot_pos),
            FadeOut(dot_neg),
            FadeOut(dot_pos_label),
            FadeOut(dot_neg_label),
            FadeOut(line_to_origin),
            FadeOut(equality),
            FadeOut(explain),
            FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(odd_graph),
            FadeOut(graph_label),
            FadeOut(axes),
            run_time=0.6
        )
    
    def show_symmetry_comparison(self):
        """场景4: 对称性可视化对比"""
        # 分屏标题
        left_title = Text(
            "偶函数",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_EVEN
        ).move_to(LEFT * 2.2 + UP * 6.5)
        
        right_title = Text(
            "奇函数",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_ODD
        ).move_to(RIGHT * 2.2 + UP * 6.5)
        
        self.play(
            FadeIn(left_title, shift=RIGHT * 0.3),
            FadeIn(right_title, shift=LEFT * 0.3),
            run_time=0.6
        )
        
        # 左侧：偶函数
        axes_left = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-1, 6, 2],
            x_length=3.5,
            y_length=4.5,
            axis_config={
                "include_numbers": False,
                "include_tip": False,
                "stroke_width": 2
            },
        ).move_to(LEFT * 2.2 + UP * 2)
        
        even_graph_split = axes_left.plot(
            self.f_even,
            color=self.COLOR_EVEN,
            stroke_width=4,
            x_range=[-2.3, 2.3]
        )
        
        # 右侧：奇函数
        axes_right = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-12, 12, 6],
            x_length=3.5,
            y_length=4.5,
            axis_config={
                "include_numbers": False,
                "include_tip": False,
                "stroke_width": 2
            },
        ).move_to(RIGHT * 2.2 + UP * 2)
        
        odd_graph_split = axes_right.plot(
            self.f_odd,
            color=self.COLOR_ODD,
            stroke_width=4,
            x_range=[-2.3, 2.3]
        )
        
        self.play(
            Create(axes_left),
            Create(even_graph_split),
            run_time=1.0
        )
        
        self.play(
            Create(axes_right),
            Create(odd_graph_split),
            run_time=1.0
        )
        
        # 左侧：y轴对称线
        y_axis_left = Line(
            axes_left.c2p(0, -1),
            axes_left.c2p(0, 6),
            color=self.COLOR_Y_AXIS,
            stroke_width=5
        )
        
        y_label_left = Text(
            "y轴对称",
            font=self.FONT,
            font_size=20,
            color=self.COLOR_Y_AXIS
        ).next_to(axes_left, DOWN, buff=0.3)
        
        self.play(
            Create(y_axis_left),
            Flash(y_axis_left, color=self.COLOR_Y_AXIS, flash_radius=0.4),
            FadeIn(y_label_left),
            run_time=0.8
        )
        
        # 右侧：原点标记
        origin_right = Dot(
            axes_right.c2p(0, 0),
            color=self.COLOR_ORIGIN,
            radius=0.12
        )
        
        origin_label_right = Text(
            "原点对称",
            font=self.FONT,
            font_size=20,
            color=self.COLOR_ORIGIN
        ).next_to(axes_right, DOWN, buff=0.3)
        
        self.play(
            FadeIn(origin_right, scale=1.5),
            Flash(origin_right, color=self.COLOR_ORIGIN, flash_radius=0.4),
            FadeIn(origin_label_right),
            run_time=0.8
        )
        
        # 同步演示对称点
        # 左侧
        x_demo = 1.5
        dot_l_pos = Dot(axes_left.c2p(x_demo, self.f_even(x_demo)), color=YELLOW, radius=0.08)
        dot_l_neg = Dot(axes_left.c2p(-x_demo, self.f_even(x_demo)), color=YELLOW, radius=0.08)
        
        # 右侧
        dot_r_pos = Dot(axes_right.c2p(x_demo, self.f_odd(x_demo)), color=YELLOW, radius=0.08)
        dot_r_neg = Dot(axes_right.c2p(-x_demo, -self.f_odd(x_demo)), color=YELLOW, radius=0.08)
        
        self.play(
            FadeIn(dot_l_pos, scale=1.3),
            FadeIn(dot_r_pos, scale=1.3),
            run_time=0.5
        )
        
        # 镜像/旋转动画
        # 左侧：镜像
        h_line_left = DashedLine(
            axes_left.c2p(-x_demo, self.f_even(x_demo)),
            axes_left.c2p(x_demo, self.f_even(x_demo)),
            color=self.COLOR_Y_AXIS,
            stroke_width=2
        )
        
        # 右侧：通过原点的线
        line_right = Line(
            axes_right.c2p(x_demo, self.f_odd(x_demo)),
            axes_right.c2p(-x_demo, -self.f_odd(x_demo)),
            color=self.COLOR_ORIGIN,
            stroke_width=3
        )
        
        self.play(
            Create(h_line_left),
            FadeIn(dot_l_neg, scale=1.3),
            Create(line_right),
            FadeIn(dot_r_neg, scale=1.3),
            run_time=1.2
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(left_title),
            FadeOut(right_title),
            FadeOut(axes_left),
            FadeOut(axes_right),
            FadeOut(even_graph_split),
            FadeOut(odd_graph_split),
            FadeOut(y_axis_left),
            FadeOut(y_label_left),
            FadeOut(origin_right),
            FadeOut(origin_label_right),
            FadeOut(dot_l_pos),
            FadeOut(dot_l_neg),
            FadeOut(dot_r_pos),
            FadeOut(dot_r_neg),
            FadeOut(h_line_left),
            FadeOut(line_right),
            run_time=0.6
        )
    
    def show_判断方法(self):
        """场景5: 判断方法两步法"""
        # 标题
        title = Text(
            "如何判断奇偶性？",
            font=self.FONT,
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        
        # 步骤卡片
        step1_box = Rectangle(
            width=7,
            height=1.2,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(UP * 4.5)
        
        step1_text = VGroup(
            Text("步骤1:", font=self.FONT, font_size=24, color=self.COLOR_HIGHLIGHT),
            Text("检查定义域是否关于原点对称", font=self.FONT, font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(step1_box)
        
        step1_card = VGroup(step1_box, step1_text).shift(LEFT * 10)
        
        self.play(step1_card.animate.shift(RIGHT * 10), run_time=0.8)
        self.wait(0.7)
        
        # 示例：f(x) = 1/x
        example = MathTex(
            r"f(x) = \frac{1}{x}",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3)
        
        domain_text = Text(
            "定义域: x ≠ 0",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(example), FadeIn(domain_text), run_time=0.8)
        
        # 检查对称性
        check_text = Text(
            "✓ 关于原点对称",
            font=self.FONT,
            font_size=24,
            color=self.COLOR_ODD
        ).move_to(UP * 1.6)
        
        self.play(FadeIn(check_text, scale=1.2), run_time=0.6)
        self.wait(0.5)
        
        # 步骤2
        step2_box = Rectangle(
            width=7,
            height=1.2,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(UP * 0.8)
        
        step2_text = VGroup(
            Text("步骤2:", font=self.FONT, font_size=24, color=self.COLOR_HIGHLIGHT),
            Text("计算 f(-x)，比较与 f(x) 的关系", font=self.FONT, font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(step2_box)
        
        step2_card = VGroup(step2_box, step2_text).shift(LEFT * 10)
        
        self.play(step2_card.animate.shift(RIGHT * 10), run_time=0.8)
        self.wait(0.7)
        
        # 计算 f(-x)
        calc_steps = VGroup(
            MathTex(r"f(-x) = \frac{1}{-x}", font_size=26, color=WHITE),
            MathTex(r"= -\frac{1}{x}", font_size=26, color=WHITE),
            MathTex(r"= -f(x)", font_size=26, color=self.COLOR_ODD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 0.5)
        
        for step in calc_steps:
            self.play(FadeIn(step, shift=UP * 0.2), run_time=0.6)
        
        # 结论
        conclusion_box = Rectangle(
            width=5,
            height=0.8,
            color=self.COLOR_ODD,
            fill_opacity=0.2,
            stroke_width=4
        ).move_to(DOWN * 2.5)
        
        conclusion_text = Text(
            "∴ 奇函数！",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_ODD
        ).move_to(conclusion_box)
        
        self.play(
            FadeIn(conclusion_box),
            FadeIn(conclusion_text, scale=1.3),
            run_time=0.8
        )
        self.play(Flash(conclusion_box, color=self.COLOR_ODD, flash_radius=0.6), run_time=0.5)
        
        # 图像验证
        axes_verify = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=3,
            axis_config={
                "include_numbers": False,
                "include_tip": False,
                "stroke_width": 2
            },
        ).move_to(DOWN * 5)
        
        verify_graph = axes_verify.plot(
            lambda x: 1/x if abs(x) > 0.1 else 1e6,
            color=self.COLOR_ODD,
            stroke_width=4,
            discontinuities=[-0.1, 0.1],
            x_range=[-2.8, -0.1]
        )
        
        verify_graph_2 = axes_verify.plot(
            lambda x: 1/x,
            color=self.COLOR_ODD,
            stroke_width=4,
            x_range=[0.1, 2.8]
        )
        
        self.play(
            Create(axes_verify),
            Create(verify_graph),
            Create(verify_graph_2),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step1_card),
            FadeOut(step2_card),
            FadeOut(example),
            FadeOut(domain_text),
            FadeOut(check_text),
            FadeOut(calc_steps),
            FadeOut(conclusion_box),
            FadeOut(conclusion_text),
            FadeOut(axes_verify),
            FadeOut(verify_graph),
            FadeOut(verify_graph_2),
            run_time=0.6
        )
    
    def show_special_property(self):
        """场景6: 特殊性质 f(0)=0"""
        # 标题
        title = Text(
            "奇函数的特殊性质",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_ODD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        
        # 重要提示框
        important_box = Rectangle(
            width=7.5,
            height=1.5,
            color=RED,
            fill_opacity=0.15,
            stroke_width=4
        ).move_to(UP * 4.5)
        
        important_icon = Text(
            "⚠",
            font_size=40,
            color=RED
        ).move_to(important_box.get_left() + RIGHT * 0.5)
        
        important_formula = Text(
            "奇函数若在 x=0 有定义，则 f(0)=0",
            font=self.FONT,
            font_size=26,
            color=WHITE
        ).move_to(important_box.get_center() + RIGHT * 0.5)
        
        self.play(
            FadeIn(important_box),
            FadeIn(important_icon, scale=1.5),
            run_time=0.6
        )
        self.play(Write(important_formula), run_time=1.2)
        self.wait(0.8)
        
        # 证明过程
        proof_title = Text(
            "证明:",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.8 + LEFT * 3)
        
        proof_steps = VGroup(
            VGroup(
                Text("已知:", font="PingFang SC", font_size=24, color=WHITE),
                MathTex(r"f(-x) = -f(x)", font_size=24, color=WHITE)
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("令", font="PingFang SC", font_size=24, color=GRAY_A),
                MathTex(r"x = 0 :", font_size=24, color=GRAY_A)
            ).arrange(RIGHT, buff=0.15),
            MathTex(r"f(-0) = -f(0)", font_size=24, color=WHITE),
            MathTex(r"f(0) = -f(0)", font_size=24, color=WHITE),
            MathTex(r"2f(0) = 0", font_size=24, color=YELLOW),
            MathTex(r"\therefore f(0) = 0", font_size=28, color=self.COLOR_ODD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(UP * 1.2)
        
        self.play(FadeIn(proof_title), run_time=0.4)
        
        for i, step in enumerate(proof_steps):
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.5)
            if i == len(proof_steps) - 1:
                self.play(Indicate(step, color=self.COLOR_ODD, scale_factor=1.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 图像验证 - 多个奇函数都过原点
        verify_text = Text(
            "图像验证：所有奇函数都过原点",
            font=self.FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(verify_text), run_time=0.6)
        
        # 小坐标系展示多个奇函数
        axes_small = Axes(
            x_range=[-2, 2, 1],
            y_range=[-4, 4, 2],
            x_length=5,
            y_length=3,
            axis_config={
                "include_numbers": False,
                "include_tip": False,
                "stroke_width": 2
            },
        ).move_to(DOWN * 4)
        
        # x³, x, sin(x)
        graph1 = axes_small.plot(lambda x: x**3, color=BLUE_C, stroke_width=3, x_range=[-1.5, 1.5])
        graph2 = axes_small.plot(lambda x: 2*x, color=GREEN_C, stroke_width=3, x_range=[-1.8, 1.8])
        graph3 = axes_small.plot(lambda x: 3*np.sin(x), color=PURPLE_C, stroke_width=3, x_range=[-1.8, 1.8])
        
        origin_mark = Dot(axes_small.c2p(0, 0), color=RED, radius=0.12)
        
        self.play(
            Create(axes_small),
            FadeIn(origin_mark, scale=1.5),
            run_time=0.6
        )
        
        self.play(
            Create(graph1),
            Create(graph2),
            Create(graph3),
            run_time=1.2
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(important_box),
            FadeOut(important_icon),
            FadeOut(important_formula),
            FadeOut(proof_title),
            FadeOut(proof_steps),
            FadeOut(verify_text),
            FadeOut(axes_small),
            FadeOut(graph1),
            FadeOut(graph2),
            FadeOut(graph3),
            FadeOut(origin_mark),
            run_time=0.6
        )
    
    def show_examples(self):
        """场景7: 综合示例"""
        # 标题
        title = Text(
            "常见函数的奇偶性",
            font=self.FONT,
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建2×2网格
        examples = []
        
        # 示例数据
        example_data = [
            (r"f(x) = x^2", lambda x: x**2, "偶", self.COLOR_EVEN, [-1.8, 1.8], [-0.5, 3.5]),
            (r"f(x) = x^3", lambda x: x**3, "奇", self.COLOR_ODD, [-1.5, 1.5], [-3, 3]),
            (r"f(x) = |x|", lambda x: abs(x), "偶", self.COLOR_EVEN, [-1.8, 1.8], [-0.5, 2]),
            (r"f(x) = \frac{1}{x}", None, "奇", self.COLOR_ODD, [-1.8, 1.8], [-3, 3])
        ]
        
        positions = [
            UP * 3 + LEFT * 2,
            UP * 3 + RIGHT * 2,
            DOWN * 0.5 + LEFT * 2,
            DOWN * 0.5 + RIGHT * 2
        ]
        
        for i, (formula, func, parity, color, x_range, y_range) in enumerate(example_data):
            # 小坐标系
            ax = Axes(
                x_range=[x_range[0], x_range[1], 1],
                y_range=[y_range[0], y_range[1], 2],
                x_length=2.5,
                y_length=2.5,
                axis_config={
                    "include_numbers": False,
                    "include_tip": False,
                    "stroke_width": 1.5
                },
            ).move_to(positions[i])
            
            # 图像
            if i == 3:  # 1/x 分段
                graph_left  = ax.plot(lambda x: 1/x, color=color, stroke_width=3, x_range=[-1.8, -0.15])
                graph_right = ax.plot(lambda x: 1/x, color=color, stroke_width=3, x_range=[0.15,  1.8])
                graph = VGroup(graph_left, graph_right)
            else:
                graph = ax.plot(func, color=color, stroke_width=3, x_range=x_range)
            
            # 公式标签
            formula_label = MathTex(formula, font_size=20, color=WHITE).next_to(ax, UP, buff=0.15)
            
            # 奇偶性标注
            parity_label = Text(
                f"({parity})",
                font=self.FONT,
                font_size=20,
                color=color
            ).next_to(ax, DOWN, buff=0.15)
            
            example_group = VGroup(ax, graph, formula_label, parity_label)
            examples.append(example_group)
        
        # 依次显示
        for i, example in enumerate(examples):
            self.play(FadeIn(example, shift=UP * 0.3), run_time=0.6)
            self.wait(0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            *[FadeOut(ex) for ex in examples],
            run_time=0.6
        )
    
    def show_summary(self):
        """场景8: 总结与片尾"""
        # 标题
        title = Text(
            "函数奇偶性总结",
            font=self.FONT,
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 要点卡片
        cards = VGroup()
        
        card_data = [
            ("偶函数: f(-x) = f(x)", "y轴对称", self.COLOR_EVEN, UP * 4),
            ("奇函数: f(-x) = -f(x)", "原点对称", self.COLOR_ODD, UP * 2.5),
            ("判断方法", "①定义域对称 ②计算f(-x)", self.COLOR_HIGHLIGHT, UP * 1),
            ("特殊性质", "奇函数: f(0) = 0", RED, DOWN * 0.5),
        ]
        
        for main_text, sub_text, color, pos in card_data:
            card_box = Rectangle(
                width=7.5,
                height=1.2,
                color=color,
                fill_opacity=0.1,
                stroke_width=3
            ).move_to(pos)
            
            card_main = Text(
                main_text,
                font=self.FONT,
                font_size=24,
                color=color
            ).move_to(card_box.get_top() + DOWN * 0.35)
            
            card_sub = Text(
                sub_text,
                font=self.FONT,
                font_size=20,
                color=GRAY_A
            ).move_to(card_box.get_bottom() + UP * 0.35)
            
            card = VGroup(card_box, card_main, card_sub).shift(LEFT * 10)
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.6)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(0.8)
        
        # 重要提示
        tip_box = Rectangle(
            width=7,
            height=0.8,
            color=RED,
            fill_opacity=0.2,
            stroke_width=4
        ).move_to(DOWN * 2.5)
        
        tip_text = Text(
            "⚠ 定义域必须关于原点对称！",
            font=self.FONT,
            font_size=24,
            color=RED
        ).move_to(tip_box)
        
        self.play(
            FadeIn(tip_box),
            FadeIn(tip_text, scale=1.2),
            run_time=0.8
        )
        self.play(Flash(tip_box, color=RED, flash_radius=0.8), run_time=0.5)
        
        self.wait(1.5)
        
        # 片尾
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(tip_box),
            FadeOut(tip_text),
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
        
        # 装饰：对称图标
        sym_icons = VGroup(
            Text("⟷", font_size=35, color=self.COLOR_EVEN),
            Text("↺", font_size=35, color=self.COLOR_ODD),
            Text("⟷", font_size=35, color=self.COLOR_EVEN),
            Text("↺", font_size=35, color=self.COLOR_ODD),
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in sym_icons], run_time=0.6)
        self.play(sym_icons.animate.shift(UP * 0.2).scale(1.1), run_time=0.5)
        self.play(sym_icons.animate.shift(DOWN * 0.2).scale(1/1.1), run_time=0.5)
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(sym_icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql function_parity.py FunctionParity  # 快速预览
# manim -qm function_parity.py FunctionParity   # 中等质量
# manim -qh function_parity.py FunctionParity   # 高质量 (推荐)
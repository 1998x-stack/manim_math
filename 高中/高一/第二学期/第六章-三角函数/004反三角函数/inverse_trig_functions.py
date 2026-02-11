"""
反三角函数教学动画
Inverse Trigonometric Functions Educational Animation

使用 Manim 创建的高中数学教学视频
内容: arcsin, arccos, arctan 的定义、图像和性质
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


class InverseTrigFunctions(Scene):
    """
    反三角函数教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 反函数概念 - 回顾基础
    3. arcsin详解 - 定义域、值域、图像
    4. arccos详解 - 定义域、值域、图像
    5. arctan详解 - 定义域、值域、图像
    6. 三函数对比 - 并列展示
    7. 片尾总结 - 关注引导
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ARCSIN = "#e74c3c"      # 红色 - arcsin
        self.COLOR_ARCCOS = "#3498db"      # 蓝色 - arccos  
        self.COLOR_ARCTAN = "#2ecc71"      # 绿色 - arctan
        self.COLOR_ORIGINAL = "#f39c12"    # 橙色 - 原函数
        self.COLOR_REFLECTION = "#9b59b6"  # 紫色 - 对称线
        self.COLOR_AUXILIARY = GRAY_B      # 辅助元素
        self.COLOR_HIGHLIGHT = YELLOW      # 高亮
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_inverse_concept()
        self.show_arcsin()
        self.show_arccos()
        self.show_arctan()
        self.show_comparison()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）- 修正位置在安全边界内
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 6.5)  # 从7改为6.5
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text_1 = Text(
            "已知:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 3)
        
        hook_formula = MathTex(
            r"\sin(30^\circ) = \frac{1}{2}",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).next_to(hook_text_1, DOWN, buff=0.5)
        
        hook_text_2 = Text(
            "那么反过来呢?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).next_to(hook_formula, DOWN, buff=0.8)
        
        question_mark = Text(
            "?",
            font_size=72,
            color=YELLOW
        ).next_to(hook_text_2, DOWN, buff=0.3)
        
        self.play(Write(hook_text_1), run_time=0.6)
        self.play(Write(hook_formula), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(hook_text_2, shift=UP * 0.2), run_time=0.6)
        self.play(
            FadeIn(question_mark, scale=0.5),
            question_mark.animate.scale(1.2).set_color(RED),
            run_time=0.5
        )
        self.play(question_mark.animate.scale(1/1.2).set_color(YELLOW), run_time=0.3)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text_1),
            FadeOut(hook_formula),
            FadeOut(hook_text_2),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_inverse_concept(self):
        """场景2: 反函数概念"""
        # 标题
        title = Text(
            "反函数 Inverse Function",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标轴（小范围，用于sin函数）
        axes = Axes(
            x_range=[-2, 2, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=5,
            axis_config={
                "include_numbers": False,
                "stroke_width": 2
            }
        ).move_to(UP * 0.5)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=24).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_label = MathTex("y", font_size=24).next_to(axes.y_axis, UP, buff=0.1)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.0)
        
        # sin函数（限制在[-π/2, π/2]）
        sin_graph = axes.plot(
            lambda x: np.sin(x),
            x_range=[-PI/2, PI/2],
            color=self.COLOR_ORIGINAL,
            stroke_width=3
        )
        
        sin_label = MathTex(
            r"y = \sin x",
            font_size=28,
            color=self.COLOR_ORIGINAL
        ).move_to(UP * 3.5 + LEFT * 2)
        
        domain_note = Text(
            "限制在[-π/2, π/2]",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(sin_label, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(Create(sin_graph), run_time=1.2)
        self.play(Write(sin_label), FadeIn(domain_note), run_time=0.6)
        self.wait(0.5)
        
        # y=x 对称线
        reflection_line = DashedLine(
            axes.c2p(-1.2, -1.2, 0),
            axes.c2p(1.2, 1.2, 0),
            color=self.COLOR_REFLECTION,
            dash_length=0.08,
            stroke_width=2
        )
        
        reflection_label = MathTex(
            r"y = x",
            font_size=24,
            color=self.COLOR_REFLECTION
        ).move_to(axes.c2p(0.8, 1.0, 0))
        
        explain = Text(
            "关于 y=x 对称",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(
            Create(reflection_line),
            Write(reflection_label),
            FadeIn(explain),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 创建反函数（通过反射）
        # 使用参数方程：原曲线(t, sin(t))，反射后(sin(t), t)
        arcsin_graph = axes.plot_parametric_curve(
            lambda t: np.array([np.sin(t), t, 0]),
            t_range=[-PI/2, PI/2],
            color=self.COLOR_ARCSIN,
            stroke_width=3
        )
        
        arcsin_label = MathTex(
            r"y = \arcsin x",
            font_size=28,
            color=self.COLOR_ARCSIN
        ).move_to(UP * 3.5 + RIGHT * 2)
        
        self.play(
            TransformFromCopy(sin_graph, arcsin_graph),
            run_time=1.5
        )
        self.play(Write(arcsin_label), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sin_graph),
            FadeOut(sin_label),
            FadeOut(domain_note),
            FadeOut(reflection_line),
            FadeOut(reflection_label),
            FadeOut(explain),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(arcsin_graph),
            FadeOut(arcsin_label),
            run_time=0.6
        )
    
    def show_arcsin(self):
        """场景3: arcsin详解"""
        # 标题
        title = Text(
            "反正弦函数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ARCSIN
        ).move_to(UP * 5.5)
        
        title_en = Text(
            "y = arcsin x",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(title_en), run_time=0.8)
        
        # 定义
        definition = VGroup(
            Text("定义域:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"x \in [-1, 1]", font_size=26, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4.2)
        
        definition2 = VGroup(
            Text("值域:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"y \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]", font_size=26, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.3).next_to(definition, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(definition), run_time=0.8)
        self.play(Write(definition2), run_time=0.8)
        self.wait(0.5)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=6,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "stroke_width": 2
            },
            tips=False
        ).move_to(UP * 0.3)
        
        # 修改y轴标签为π的倍数
        y_labels = VGroup()
        for y_val in [-1.5, -1, -0.5, 0, 0.5, 1, 1.5]:
            if abs(y_val - (-PI/2)) < 0.1:
                label = MathTex(r"-\frac{\pi}{2}", font_size=18)
            elif abs(y_val - PI/2) < 0.1:
                label = MathTex(r"\frac{\pi}{2}", font_size=18)
            elif abs(y_val) < 0.1:
                label = MathTex("0", font_size=18)
            else:
                continue
            label.move_to(axes.c2p(0, y_val) + LEFT * 0.4)
            y_labels.add(label)
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(y_labels), run_time=0.5)
        
        # 绘制arcsin曲线
        arcsin_graph = axes.plot(
            lambda x: np.arcsin(np.clip(x, -1, 1)),  # clip确保在定义域内
            x_range=[-1, 1],
            color=self.COLOR_ARCSIN,
            stroke_width=4
        )
        
        self.play(Create(arcsin_graph), run_time=2.0)
        
        # 标记定义域
        domain_bracket = VGroup(
            Line(axes.c2p(-1, 0), axes.c2p(-1, -0.2), color=YELLOW, stroke_width=3),
            Line(axes.c2p(-1, -0.2), axes.c2p(1, -0.2), color=YELLOW, stroke_width=3),
            Line(axes.c2p(1, -0.2), axes.c2p(1, 0), color=YELLOW, stroke_width=3)
        )
        
        domain_label = MathTex(
            r"[-1, 1]",
            font_size=22,
            color=YELLOW
        ).next_to(domain_bracket, DOWN, buff=0.1)
        
        self.play(Create(domain_bracket), Write(domain_label), run_time=0.8)
        
        # 标记关键点
        key_points = [
            (-1, -PI/2, r"(-1, -\frac{\pi}{2})"),
            (0, 0, r"(0, 0)"),
            (1, PI/2, r"(1, \frac{\pi}{2})")
        ]
        
        dots = VGroup()
        labels = VGroup()
        
        for x, y, label_text in key_points:
            dot = Dot(axes.c2p(x, y), color=YELLOW, radius=0.06)
            label = MathTex(label_text, font_size=18, color=YELLOW)
            
            # 根据位置调整标签位置
            if x < 0:
                label.next_to(dot, LEFT, buff=0.15)
            elif x > 0:
                label.next_to(dot, RIGHT, buff=0.15)
            else:
                label.next_to(dot, DOWN + RIGHT, buff=0.15)
            
            dots.add(dot)
            labels.add(label)
        
        self.play(FadeIn(dots, scale=0.5), run_time=0.6)
        self.play(Write(labels), run_time=0.8)
        self.wait(0.5)
        
        # 恒等式
        identity = MathTex(
            r"\sin(\arcsin x) = x",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(identity), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(title_en),
            FadeOut(definition),
            FadeOut(definition2),
            FadeOut(domain_bracket),
            FadeOut(domain_label),
            FadeOut(dots),
            FadeOut(labels),
            FadeOut(identity),
            FadeOut(axes),
            FadeOut(y_labels),
            FadeOut(arcsin_graph),
            run_time=0.6
        )
    
    def show_arccos(self):
        """场景4: arccos详解"""
        # 标题
        title = Text(
            "反余弦函数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ARCCOS
        ).move_to(UP * 5.5)
        
        title_en = Text(
            "y = arccos x",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(title_en), run_time=0.8)
        
        # 定义
        definition = VGroup(
            Text("定义域:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"x \in [-1, 1]", font_size=26, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4.2)
        
        definition2 = VGroup(
            Text("值域:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"y \in [0, \pi]", font_size=26, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.3).next_to(definition, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(definition), run_time=0.8)
        self.play(Write(definition2), run_time=0.8)
        self.wait(0.5)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-0.5, 3.5, 0.5],
            x_length=6,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "stroke_width": 2
            },
            tips=False
        ).move_to(UP * 0.3)
        
        # 修改y轴标签为π的倍数
        y_labels = VGroup()
        for y_val in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
            if abs(y_val) < 0.1:
                label = MathTex("0", font_size=18)
            elif abs(y_val - PI/2) < 0.1:
                label = MathTex(r"\frac{\pi}{2}", font_size=18)
            elif abs(y_val - PI) < 0.1:
                label = MathTex(r"\pi", font_size=18)
            else:
                continue
            label.move_to(axes.c2p(0, y_val) + LEFT * 0.4)
            y_labels.add(label)
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(y_labels), run_time=0.5)
        
        # 绘制arccos曲线
        arccos_graph = axes.plot(
            lambda x: np.arccos(np.clip(x, -1, 1)),
            x_range=[-1, 1],
            color=self.COLOR_ARCCOS,
            stroke_width=4
        )
        
        self.play(Create(arccos_graph), run_time=2.0)
        
        # 标记关键点
        key_points = [
            (-1, PI, r"(-1, \pi)"),
            (0, PI/2, r"(0, \frac{\pi}{2})"),
            (1, 0, r"(1, 0)")
        ]
        
        dots = VGroup()
        labels = VGroup()
        
        for x, y, label_text in key_points:
            dot = Dot(axes.c2p(x, y), color=YELLOW, radius=0.06)
            label = MathTex(label_text, font_size=18, color=YELLOW)
            
            # 根据位置调整标签位置
            if x < 0:
                label.next_to(dot, LEFT, buff=0.15)
            elif x > 0:
                label.next_to(dot, RIGHT, buff=0.15)
            else:
                label.next_to(dot, RIGHT, buff=0.15)
            
            dots.add(dot)
            labels.add(label)
        
        self.play(FadeIn(dots, scale=0.5), run_time=0.6)
        self.play(Write(labels), run_time=0.8)
        self.wait(0.5)
        
        # 重要关系
        identity = MathTex(
            r"\arcsin x + \arccos x = \frac{\pi}{2}",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(identity), run_time=1.0)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(title_en),
            FadeOut(definition),
            FadeOut(definition2),
            FadeOut(dots),
            FadeOut(labels),
            FadeOut(identity),
            FadeOut(axes),
            FadeOut(y_labels),
            FadeOut(arccos_graph),
            run_time=0.6
        )
    
    def show_arctan(self):
        """场景5: arctan详解"""
        # 标题
        title = Text(
            "反正切函数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ARCTAN
        ).move_to(UP * 5.5)
        
        title_en = Text(
            "y = arctan x",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(title_en), run_time=0.8)
        
        # 定义
        definition = VGroup(
            Text("定义域:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"x \in \mathbb{R}", font_size=26, color=self.COLOR_HIGHLIGHT),
            Text("(全体实数)", font="Noto Sans CJK SC", font_size=self.FONT_SMALL, color=GRAY_A)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.2)
        
        definition2 = VGroup(
            Text("值域:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"y \in \left(-\frac{\pi}{2}, \frac{\pi}{2}\right)", font_size=26, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.3).next_to(definition, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(definition), run_time=0.8)
        self.play(Write(definition2), run_time=0.8)
        self.wait(0.5)
        
        # 创建坐标轴（更宽的x范围）
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 0.5],
            x_length=7,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "stroke_width": 2
            },
            tips=False
        ).move_to(UP * 0.3)
        
        # 修改y轴标签为π的倍数
        y_labels = VGroup()
        for y_val in [-1.5, -1, -0.5, 0, 0.5, 1, 1.5]:
            if abs(y_val - (-PI/2)) < 0.1:
                label = MathTex(r"-\frac{\pi}{2}", font_size=18)
            elif abs(y_val - PI/2) < 0.1:
                label = MathTex(r"\frac{\pi}{2}", font_size=18)
            elif abs(y_val) < 0.1:
                label = MathTex("0", font_size=18)
            else:
                continue
            label.move_to(axes.c2p(0, y_val) + LEFT * 0.5)
            y_labels.add(label)
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(y_labels), run_time=0.5)
        
        # 绘制arctan曲线
        arctan_graph = axes.plot(
            lambda x: np.arctan(x),
            x_range=[-4, 4],
            color=self.COLOR_ARCTAN,
            stroke_width=4
        )
        
        self.play(Create(arctan_graph), run_time=2.5)
        
        # 标记渐近线
        asymptote_up = DashedLine(
            axes.c2p(-4, PI/2),
            axes.c2p(4, PI/2),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        asymptote_down = DashedLine(
            axes.c2p(-4, -PI/2),
            axes.c2p(4, -PI/2),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        asymptote_label_up = MathTex(
            r"y = \frac{\pi}{2}",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).next_to(axes.c2p(3, PI/2), UR, buff=0.1)
        
        asymptote_label_down = MathTex(
            r"y = -\frac{\pi}{2}",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).next_to(axes.c2p(3, -PI/2), DR, buff=0.1)
        
        self.play(
            Create(asymptote_up),
            Create(asymptote_down),
            Write(asymptote_label_up),
            Write(asymptote_label_down),
            run_time=1.0
        )
        
        note = Text(
            "渐近线（无限接近但不到达）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(note), run_time=0.5)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(title_en),
            FadeOut(definition),
            FadeOut(definition2),
            FadeOut(asymptote_up),
            FadeOut(asymptote_down),
            FadeOut(asymptote_label_up),
            FadeOut(asymptote_label_down),
            FadeOut(note),
            FadeOut(axes),
            FadeOut(y_labels),
            FadeOut(arctan_graph),
            run_time=0.6
        )
    
    def show_comparison(self):
        """场景6: 三函数对比"""
        # 标题
        title = Text(
            "三大反三角函数对比",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建对比表格
        table_data = [
            ["函数", "定义域", "值域"],
            ["arcsin x", "[-1, 1]", "[-π/2, π/2]"],
            ["arccos x", "[-1, 1]", "[0, π]"],
            ["arctan x", "R", "(-π/2, π/2)"]
        ]
        
        # 手动创建表格
        table = VGroup()
        
        # 表头
        header = VGroup(
            Text("函数", font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("定义域", font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("值域", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=1.2)
        
        # 数据行
        row1 = VGroup(
            MathTex(r"\arcsin x", font_size=24, color=self.COLOR_ARCSIN),
            MathTex(r"[-1, 1]", font_size=22, color=WHITE),
            MathTex(r"[-\frac{\pi}{2}, \frac{\pi}{2}]", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.8)
        
        row2 = VGroup(
            MathTex(r"\arccos x", font_size=24, color=self.COLOR_ARCCOS),
            MathTex(r"[-1, 1]", font_size=22, color=WHITE),
            MathTex(r"[0, \pi]", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.8)
        
        row3 = VGroup(
            MathTex(r"\arctan x", font_size=24, color=self.COLOR_ARCTAN),
            MathTex(r"\mathbb{R}", font_size=22, color=WHITE),
            MathTex(r"(-\frac{\pi}{2}, \frac{\pi}{2})", font_size=22, color=WHITE)
        ).arrange(RIGHT, buff=0.8)
        
        # 对齐
        for row in [row1, row2, row3]:
            row[0].move_to(header[0].get_center() + DOWN * 0.5)
            row[1].move_to(header[1].get_center() + DOWN * 0.5)
            row[2].move_to(header[2].get_center() + DOWN * 0.5)
        
        table.add(header)
        table.add(row1.next_to(header, DOWN, buff=0.5))
        table.add(row2.next_to(row1, DOWN, buff=0.4))
        table.add(row3.next_to(row2, DOWN, buff=0.4))
        
        table.move_to(UP * 1.5)
        
        self.play(FadeIn(header, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(row1, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(row2, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(row3, shift=DOWN * 0.2), run_time=0.4)
        self.wait(1.0)
        
        # 高亮定义域差异
        domain_highlight = SurroundingRectangle(
            VGroup(row1[1], row2[1], row3[1]),
            color=YELLOW,
            buff=0.15,
            stroke_width=3
        )
        
        note = Text(
            "注意: arctan 定义域最广!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(Create(domain_highlight), FadeIn(note), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(table),
            FadeOut(domain_highlight),
            FadeOut(note),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾总结"""
        # 关键要点
        key_points = VGroup(
            Text("✓ 反三角函数是三角函数的反函数", font="Noto Sans CJK SC", 
                 font_size=self.FONT_BODY, color=WHITE),
            Text("✓ 注意定义域和值域的限制", font="Noto Sans CJK SC", 
                 font_size=self.FONT_BODY, color=WHITE),
            Text("✓ arcsin + arccos = π/2", font="Noto Sans CJK SC", 
                 font_size=self.FONT_BODY, color=WHITE),
            Text("✓ arctan 值域是开区间", font="Noto Sans CJK SC", 
                 font_size=self.FONT_BODY, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 2)
        
        # 卡片依次滑入
        for point in key_points:
            point.shift(LEFT * 10)
        
        for point in key_points:
            self.play(point.animate.shift(RIGHT * 10), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.0)
        
        # 淡出要点
        self.play(FadeOut(key_points), run_time=0.5)
        
        # 作者信息放大
        author_name = Text(
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
        ).next_to(author_name, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 三个函数图标（简化版）
        icons = VGroup(
            Circle(radius=0.3, color=self.COLOR_ARCSIN, fill_opacity=0.8, stroke_width=0),
            Circle(radius=0.3, color=self.COLOR_ARCCOS, fill_opacity=0.8, stroke_width=0),
            Circle(radius=0.3, color=self.COLOR_ARCTAN, fill_opacity=0.8, stroke_width=0)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.5)
        
        # 图标内添加文字
        icon_labels = VGroup(
            Text("sin⁻¹", font_size=20, color=WHITE),
            Text("cos⁻¹", font_size=20, color=WHITE),
            Text("tan⁻¹", font_size=20, color=WHITE)
        )
        
        for icon, label in zip(icons, icon_labels):
            label.move_to(icon.get_center())
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            *[FadeIn(label) for label in icon_labels],
            run_time=0.6
        )
        
        self.play(Rotate(icons, angle=2*PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            FadeOut(icon_labels),
            run_time=1.0
        )


# 运行命令:
# manim -pql inverse_trig_functions.py InverseTrigFunctions  # 快速预览
# manim -qh inverse_trig_functions.py InverseTrigFunctions   # 高质量渲染
"""
一次函数的性质 - Linear Function Properties Animation
使用 Manim 创建的中学数学教学视频

内容: 一次函数y=kx+b的性质，单调性，象限关系
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


class LinearFunctionProperties(Scene):
    """
    一次函数性质教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. k>0的性质 (单调递增)
    4. k<0的性质 (单调递减)
    5. k和b的符号与象限关系
    6. 性质对比总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - k>0
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - k<0
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_POSITIVE_ZONE = "#2ecc71"  # 绿色
        self.COLOR_NEGATIVE_ZONE = "#f39c12"  # 橙色
        
        # 执行动画序列
        self.show_opening()
        self.setup_coordinate_system()
        self.show_k_positive_property()
        self.show_k_negative_property()
        self.show_quadrant_relationships()
        self.show_comparison_summary()
        self.show_outro()
    
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
            "一次函数的性质\n你真的掌握了吗?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 公式闪烁
        formula = MathTex(
            r"y = kx + b",
            font_size=60,
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(FadeIn(formula, scale=1.2), run_time=0.5)
        self.play(Flash(formula, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.4)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(formula),
            run_time=0.5
        )
    
    def setup_coordinate_system(self):
        """场景2: 建立坐标系"""
        # 创建坐标系
        self.axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "numbers_to_exclude": [0],
            },
            tips=False
        ).move_to(UP * 1.5)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=28).next_to(self.axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28).next_to(self.axes.y_axis, UP, buff=0.2)
        
        # 动画
        self.play(Create(self.axes), run_time=1.2)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 标题
        title = Text(
            "一次函数",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        subtitle = MathTex(
            r"y = kx + b",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        self.wait(1.0)
        
        # 标题移到顶部缩小
        title_small = Text(
            "一次函数 y=kx+b",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 6.5)
        
        self.play(
            Transform(title, title_small),
            FadeOut(subtitle),
            run_time=0.5
        )
        
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
    
    def show_k_positive_property(self):
        """场景3: k>0的性质 - y随x增大而增大"""
        # 公式
        formula = MathTex(
            r"y = 2x + 1",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5 + RIGHT * 2)
        
        k_info = MathTex(
            r"k = 2 > 0",
            font_size=24,
            color=self.COLOR_POSITIVE_ZONE
        ).next_to(formula, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(Write(formula), FadeIn(k_info), run_time=0.8)
        
        # 绘制直线
        line_func = lambda x: 2 * x + 1
        line = self.axes.plot(
            line_func,
            x_range=[-2, 1],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(line), run_time=1.5)
        
        # 动点沿直线移动
        x_tracker = ValueTracker(-2)
        
        dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(x_tracker.get_value(), line_func(x_tracker.get_value())),
                color=YELLOW,
                radius=0.12
            )
        )
        
        # x和y的实时数值
        x_value_label = always_redraw(
            lambda: MathTex(
                f"x = {x_tracker.get_value():.1f}",
                font_size=24,
                color=WHITE
            ).move_to(DOWN * 3.5 + LEFT * 2)
        )
        
        y_value_label = always_redraw(
            lambda: MathTex(
                f"y = {line_func(x_tracker.get_value()):.1f}",
                font_size=24,
                color=WHITE
            ).move_to(DOWN * 3.5 + RIGHT * 2)
        )
        
        self.add(dot, x_value_label, y_value_label)
        
        # 箭头提示
        arrow_label = Text(
            "x增大 →",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(arrow_label, shift=RIGHT * 0.3), run_time=0.4)
        
        # 点移动
        self.play(x_tracker.animate.set_value(1), run_time=3, rate_func=linear)
        
        # 上升箭头
        start_point = self.axes.c2p(-2, line_func(-2))
        end_point = self.axes.c2p(1, line_func(1))
        
        arrow_up = Arrow(
            start_point + LEFT * 0.3,
            end_point + LEFT * 0.3,
            color=self.COLOR_POSITIVE_ZONE,
            stroke_width=6,
            buff=0
        )
        
        self.play(GrowArrow(arrow_up), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "y 随 x 增大而增大",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_POSITIVE_ZONE
        ).move_to(DOWN * 5.5)
        
        explanation_sub = Text(
            "(单调递增)",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(explanation, DOWN, buff=0.1)
        
        self.play(
            FadeIn(explanation, shift=UP * 0.3),
            FadeIn(explanation_sub),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(dot),
            FadeOut(x_value_label),
            FadeOut(y_value_label),
            FadeOut(arrow_up),
            FadeOut(arrow_label),
            FadeOut(explanation),
            FadeOut(explanation_sub),
            FadeOut(formula),
            FadeOut(k_info),
            line.animate.set_stroke(opacity=0.3),
            run_time=0.6
        )
        
        self.line_k_pos = line
    
    def show_k_negative_property(self):
        """场景4: k<0的性质 - y随x增大而减小"""
        # 公式
        formula = MathTex(
            r"y = -1.5x + 2",
            font_size=32,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5.5 + RIGHT * 2)
        
        k_info = MathTex(
            r"k = -1.5 < 0",
            font_size=24,
            color=self.COLOR_NEGATIVE_ZONE
        ).next_to(formula, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(Write(formula), FadeIn(k_info), run_time=0.8)
        
        # 绘制直线
        line_func = lambda x: -1.5 * x + 2
        line = self.axes.plot(
            line_func,
            x_range=[-0.6, 2],
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        self.play(Create(line), run_time=1.5)
        
        # 动点沿直线移动
        x_tracker = ValueTracker(-0.6)
        
        dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(x_tracker.get_value(), line_func(x_tracker.get_value())),
                color=YELLOW,
                radius=0.12
            )
        )
        
        # x和y的实时数值
        x_value_label = always_redraw(
            lambda: MathTex(
                f"x = {x_tracker.get_value():.1f}",
                font_size=24,
                color=WHITE
            ).move_to(DOWN * 3.5 + LEFT * 2)
        )
        
        y_value_label = always_redraw(
            lambda: MathTex(
                f"y = {line_func(x_tracker.get_value()):.1f}",
                font_size=24,
                color=WHITE
            ).move_to(DOWN * 3.5 + RIGHT * 2)
        )
        
        self.add(dot, x_value_label, y_value_label)
        
        # 箭头提示
        arrow_label = Text(
            "x增大 →",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(arrow_label, shift=RIGHT * 0.3), run_time=0.4)
        
        # 点移动
        self.play(x_tracker.animate.set_value(2), run_time=3, rate_func=linear)
        
        # 下降箭头
        start_point = self.axes.c2p(-0.6, line_func(-0.6))
        end_point = self.axes.c2p(2, line_func(2))
        
        arrow_down = Arrow(
            start_point + RIGHT * 0.3,
            end_point + RIGHT * 0.3,
            color=self.COLOR_NEGATIVE_ZONE,
            stroke_width=6,
            buff=0
        )
        
        self.play(GrowArrow(arrow_down), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "y 随 x 增大而减小",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_NEGATIVE_ZONE
        ).move_to(DOWN * 5.5)
        
        explanation_sub = Text(
            "(单调递减)",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(explanation, DOWN, buff=0.1)
        
        self.play(
            FadeIn(explanation, shift=UP * 0.3),
            FadeIn(explanation_sub),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(dot),
            FadeOut(x_value_label),
            FadeOut(y_value_label),
            FadeOut(arrow_down),
            FadeOut(arrow_label),
            FadeOut(explanation),
            FadeOut(explanation_sub),
            FadeOut(formula),
            FadeOut(k_info),
            line.animate.set_stroke(opacity=0.3),
            run_time=0.6
        )
        
        self.line_k_neg = line
    
    def show_quadrant_relationships(self):
        """场景5: k和b的符号与象限关系"""
        # 清理之前的线
        self.play(
            FadeOut(self.line_k_pos),
            FadeOut(self.line_k_neg),
            run_time=0.3
        )
        
        # 标题
        section_title = Text(
            "k 和 b 的符号决定象限",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(section_title), run_time=0.8)
        
        # 四条直线
        # Case 1: k>0, b>0 → 一、二、三象限
        line_1 = self.axes.plot(lambda x: x + 1.5, x_range=[-2, 1.5], color="#3498db", stroke_width=3)
        label_1 = MathTex(r"k>0, b>0", font_size=18, color="#3498db").move_to(
            self.axes.c2p(-2.2, -0.7) + RIGHT * 0.8
        )
        
        # Case 2: k>0, b<0 → 一、三、四象限
        line_2 = self.axes.plot(lambda x: 0.8*x - 1, x_range=[-1.5, 2.5], color="#9b59b6", stroke_width=3)
        label_2 = MathTex(r"k>0, b<0", font_size=18, color="#9b59b6").move_to(
            self.axes.c2p(2, 0.6) + LEFT * 0.8
        )
        
        # Case 3: k<0, b>0 → 一、二、四象限
        line_3 = self.axes.plot(lambda x: -0.8*x + 1.5, x_range=[-1.8, 2.1], color="#e74c3c", stroke_width=3)
        label_3 = MathTex(r"k<0, b>0", font_size=18, color="#e74c3c").move_to(
            self.axes.c2p(2.2, -0.2) + LEFT * 0.8
        )
        
        # Case 4: k<0, b<0 → 二、三、四象限
        line_4 = self.axes.plot(lambda x: -x - 1, x_range=[-2, 1], color="#f39c12", stroke_width=3)
        label_4 = MathTex(r"k<0, b<0", font_size=18, color="#f39c12").move_to(
            self.axes.c2p(-2, -1) + RIGHT * 0.8
        )
        
        # 依次绘制
        lines = [line_1, line_2, line_3, line_4]
        labels = [label_1, label_2, label_3, label_4]
        
        for line, label in zip(lines, labels):
            self.play(Create(line), run_time=0.6)
            self.play(FadeIn(label, shift=UP * 0.1), run_time=0.3)
            self.wait(0.2)
        
        self.wait(1.0)
        
        # 汇总表格
        table_data = [
            ["k, b", "象限"],
            ["k>0, b>0", "一、二、三"],
            ["k>0, b<0", "一、三、四"],
            ["k<0, b>0", "一、二、四"],
            ["k<0, b<0", "二、三、四"]
        ]
        
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": GRAY_B}
        ).scale(0.5).move_to(DOWN * 5)
        
        # 表格样式
        table.get_entries((1, 1)).set_color(YELLOW)
        table.get_entries((1, 2)).set_color(YELLOW)
        
        for i in range(2, 6):
            table.get_entries((i, 1)).set_color(WHITE)
            table.get_entries((i, 2)).set_color(GRAY_A)
        
        self.play(FadeIn(table, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(section_title),
            FadeOut(line_1),
            FadeOut(line_2),
            FadeOut(line_3),
            FadeOut(line_4),
            FadeOut(label_1),
            FadeOut(label_2),
            FadeOut(label_3),
            FadeOut(label_4),
            FadeOut(table),
            run_time=0.6
        )
    
    def show_comparison_summary(self):
        """场景6: 性质对比总结"""
        # 清理坐标系
        self.play(
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.title),
            run_time=0.5
        )
        
        # 分屏背景
        left_bg = Rectangle(
            width=4.5,
            height=8,
            fill_color=self.COLOR_PRIMARY,
            fill_opacity=0.15,
            stroke_width=0
        ).move_to(LEFT * 2.25 + UP * 1)
        
        right_bg = Rectangle(
            width=4.5,
            height=8,
            fill_color=self.COLOR_SECONDARY,
            fill_opacity=0.15,
            stroke_width=0
        ).move_to(RIGHT * 2.25 + UP * 1)
        
        self.play(FadeIn(left_bg), FadeIn(right_bg), run_time=0.5)
        
        # 左侧: k>0
        left_title = Text(
            "k > 0",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 2.25 + UP * 4.5)
        
        left_formula = MathTex(
            r"y = kx + b",
            font_size=28,
            color=WHITE
        ).next_to(left_title, DOWN, buff=0.4)
        
        left_property = Text(
            "y 随 x 增大而增大",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(LEFT * 2.25 + UP * 2)
        
        left_mono = Text(
            "单调递增",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_POSITIVE_ZONE
        ).next_to(left_property, DOWN, buff=0.3)
        
        arrow_up = Arrow(
            LEFT * 2.25 + UP * 0.5,
            LEFT * 2.25 + DOWN * 1,
            color=self.COLOR_POSITIVE_ZONE,
            stroke_width=8,
            buff=0
        )
        
        # 右侧: k<0
        right_title = Text(
            "k < 0",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(RIGHT * 2.25 + UP * 4.5)
        
        right_formula = MathTex(
            r"y = kx + b",
            font_size=28,
            color=WHITE
        ).next_to(right_title, DOWN, buff=0.4)
        
        right_property = Text(
            "y 随 x 增大而减小",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(RIGHT * 2.25 + UP * 2)
        
        right_mono = Text(
            "单调递减",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_NEGATIVE_ZONE
        ).next_to(right_property, DOWN, buff=0.3)
        
        arrow_down = Arrow(
            RIGHT * 2.25 + DOWN * 1,
            RIGHT * 2.25 + UP * 0.5,
            color=self.COLOR_NEGATIVE_ZONE,
            stroke_width=8,
            buff=0
        )
        
        # 动画
        self.play(
            Write(left_title),
            Write(right_title),
            run_time=0.6
        )
        
        self.play(
            FadeIn(left_formula),
            FadeIn(right_formula),
            run_time=0.5
        )
        
        self.play(
            GrowArrow(arrow_up),
            GrowArrow(arrow_down),
            run_time=0.8
        )
        
        self.play(
            FadeIn(left_property, shift=UP * 0.2),
            FadeIn(right_property, shift=UP * 0.2),
            run_time=0.6
        )
        
        self.play(
            FadeIn(left_mono),
            FadeIn(right_mono),
            run_time=0.5
        )
        
        # 强化提示
        highlight_text = Text(
            "记住: k 的符号决定单调性!",
            font="PingFang SC",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(highlight_text, scale=1.1), run_time=0.6)
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(left_bg),
            FadeOut(right_bg),
            FadeOut(left_title),
            FadeOut(right_title),
            FadeOut(left_formula),
            FadeOut(right_formula),
            FadeOut(left_property),
            FadeOut(right_property),
            FadeOut(left_mono),
            FadeOut(right_mono),
            FadeOut(arrow_up),
            FadeOut(arrow_down),
            FadeOut(highlight_text),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者名放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
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
            font="PingFang SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标
        icons = VGroup(
            Circle(radius=0.25, color=self.COLOR_PRIMARY, fill_opacity=0.8).shift(LEFT * 1.5 + DOWN * 2),
            Circle(radius=0.25, color=self.COLOR_SECONDARY, fill_opacity=0.8).shift(LEFT * 0.75 + DOWN * 2),
            Circle(radius=0.25, color=self.COLOR_POSITIVE_ZONE, fill_opacity=0.8).shift(DOWN * 2),
            Circle(radius=0.25, color=self.COLOR_NEGATIVE_ZONE, fill_opacity=0.8).shift(RIGHT * 0.75 + DOWN * 2),
            Circle(radius=0.25, color=YELLOW, fill_opacity=0.8).shift(RIGHT * 1.5 + DOWN * 2)
        )
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.play(Rotate(icons, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql linear_function_properties.py LinearFunctionProperties  # 快速预览
# manim -qh linear_function_properties.py LinearFunctionProperties   # 高质量
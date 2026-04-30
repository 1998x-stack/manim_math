"""
数轴 (Number Line) 教学动画 - 六年级数学
使用 Manim 创建的有理数教学视频

内容: 数轴的三要素、有理数对应、比较大小
目标观众: 小学六年级学生
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


class NumberLineLesson(Scene):
    """
    数轴教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 引入数轴
    3. 三要素之一 - 原点
    4. 三要素之二 - 正方向
    5. 三要素之三 - 单位长度
    6. 数轴与有理数的对应
    7. 比较大小规则
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 重点强调
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
        self.COLOR_NEGATIVE = "#e67e22"       # 橙色 - 负数
        self.COLOR_ORIGIN = "#9b59b6"         # 紫色 - 原点
        
        # 执行动画序列
        self.show_opening()
        self.show_number_line_intro()
        self.show_element_1_origin()
        self.show_element_2_direction()
        self.show_element_3_unit_length()
        self.show_correspondence()
        self.show_comparison()
        self.show_summary()
    
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
            "有理数怎么排队?",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 神秘的点闪烁
        mystery_dots = VGroup()
        positions = [LEFT * 2, LEFT, ORIGIN, RIGHT, RIGHT * 2]
        colors = [self.COLOR_NEGATIVE, ORANGE, self.COLOR_ORIGIN, 
                  self.COLOR_POSITIVE, GREEN]
        
        for pos, color in zip(positions, colors):
            dot = Dot(pos + UP * 3.5, color=color, radius=0.15)
            mystery_dots.add(dot)
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in mystery_dots],
            run_time=0.5
        )
        
        for _ in range(2):
            self.play(
                *[Flash(dot, color=dot.get_color(), flash_radius=0.3) 
                  for dot in mystery_dots],
                run_time=0.4
            )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(mystery_dots),
            run_time=0.5
        )
    
    def show_number_line_intro(self):
        """场景2: 引入数轴"""
        # 标题
        title_chinese = Text(
            "数轴",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        )
        
        title_english = Text(
            "Number Line",
            font_size=32,
            color=GRAY_A
        )
        
        title_group = VGroup(title_chinese, title_english).arrange(DOWN, buff=0.2)
        title_group.move_to(UP * 5.5)
        
        self.play(Write(title_group), run_time=1.0)
        
        # 定义
        definition = Text(
            "规定了原点、正方向和单位长度的直线",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.3)
        
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=0.6)
        
        # 创建基础数轴（先不带刻度）
        self.number_line_position = UP * 2
        basic_line = Line(
            LEFT * 3.5 + self.number_line_position,
            RIGHT * 3.5 + self.number_line_position,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(basic_line), run_time=1.2)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title_group),
            FadeOut(definition),
            run_time=0.5
        )
        
        # 保存基础线（将被替换为完整数轴）
        self.basic_line = basic_line
    
    def show_element_1_origin(self):
        """场景3: 三要素之一 - 原点"""
        # 标题
        element_title = Text(
            "要素1: 原点",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ORIGIN,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(element_title, shift=DOWN * 0.2), run_time=0.4)
        
        # 原点位置
        origin_pos = self.number_line_position
        
        # 原点大点
        self.origin_dot = Dot(
            origin_pos,
            color=self.COLOR_ORIGIN,
            radius=0.15
        )
        
        self.play(
            GrowFromCenter(self.origin_dot),
            Flash(self.origin_dot, color=self.COLOR_ORIGIN, flash_radius=0.4),
            run_time=0.8
        )
        
        # 原点标签 O 和 0
        label_o = Text(
            "O",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(self.origin_dot, UP, buff=0.25)
        
        label_0 = MathTex(
            "0",
            font_size=24,
            color=WHITE
        ).next_to(self.origin_dot, DOWN, buff=0.25)
        
        self.play(
            FadeIn(label_o),
            FadeIn(label_0),
            run_time=0.5
        )
        
        # 说明文字
        explanation = Text(
            "确定数轴的基准位置",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        # 原点脉冲效果
        self.play(
            self.origin_dot.animate.scale(1.4).set_opacity(0.7),
            run_time=0.5
        )
        self.play(
            self.origin_dot.animate.scale(1/1.4).set_opacity(1),
            run_time=0.5
        )
        
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(element_title),
            FadeOut(explanation),
            run_time=0.4
        )
        
        # 保存标签
        self.origin_labels = VGroup(label_o, label_0)
    
    def show_element_2_direction(self):
        """场景4: 三要素之二 - 正方向"""
        # 标题
        element_title = Text(
            "要素2: 正方向",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_POSITIVE,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(element_title, shift=DOWN * 0.2), run_time=0.4)
        
        # 箭头指示
        arrow_start = self.number_line_position + LEFT * 3.5
        arrow_end = self.number_line_position + RIGHT * 3.5
        
        self.direction_arrow = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.08
        )
        
        # 替换基础线为带箭头的线
        self.play(
            Transform(self.basic_line, self.direction_arrow),
            run_time=1.0
        )
        
        # 箭头尖端闪烁
        arrow_tip_pos = arrow_end
        self.play(
            Flash(Dot(arrow_tip_pos), color=self.COLOR_POSITIVE, flash_radius=0.4),
            run_time=0.5
        )
        
        # 说明文字
        explanation = Text(
            "通常向右为正",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        # 流动箭头效果
        flow_arrows = VGroup()
        for i in range(5):
            small_arrow = Arrow(
                LEFT * 0.3,
                RIGHT * 0.3,
                color=self.COLOR_POSITIVE,
                stroke_width=3,
                buff=0,
                max_tip_length_to_length_ratio=0.2
            ).move_to(self.number_line_position + LEFT * (3 - i * 1.5))
            flow_arrows.add(small_arrow)
        
        self.play(
            *[FadeIn(arrow, shift=RIGHT * 0.5) for arrow in flow_arrows],
            run_time=0.8
        )
        
        self.play(
            *[arrow.animate.shift(RIGHT * 7) for arrow in flow_arrows],
            run_time=1.2,
            rate_func=linear
        )
        
        self.wait(0.4)
        
        # 清理
        self.play(
            FadeOut(element_title),
            FadeOut(explanation),
            FadeOut(flow_arrows),
            run_time=0.4
        )
    
    def show_element_3_unit_length(self):
        """场景5: 三要素之三 - 单位长度"""
        # 标题
        element_title = Text(
            "要素3: 单位长度",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(element_title, shift=DOWN * 0.2), run_time=0.4)
        
        # 创建完整的数轴（带刻度）
        self.number_line = NumberLine(
            x_range=[-4, 4, 1],
            length=7,
            include_numbers=False,  # 我们手动添加数字
            include_ticks=True,
            tick_size=0.15,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.number_line_position)
        
        # 添加箭头
        arrow_tip = Arrow(
            self.number_line.get_end() + LEFT * 0.2,
            self.number_line.get_end() + RIGHT * 0.2,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.5
        )
        
        # 第一个刻度（位置1）
        tick_1_pos = self.number_line.number_to_point(1)
        tick_1 = Line(
            tick_1_pos + UP * 0.075,
            tick_1_pos + DOWN * 0.075,
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        self.play(Create(tick_1), run_time=0.4)
        
        # 单位长度标注
        unit_brace = Brace(
            Line(self.number_line.number_to_point(0), 
                 self.number_line.number_to_point(1)),
            direction=DOWN,
            buff=0.3,
            color=self.COLOR_SECONDARY
        )
        
        unit_label = Text(
            "单位长度",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_SECONDARY
        ).next_to(unit_brace, DOWN, buff=0.1)
        
        self.play(
            FadeIn(unit_brace),
            FadeIn(unit_label),
            run_time=0.6
        )
        
        # 其他正数刻度
        positive_ticks = VGroup()
        for i in [2, 3, 4]:
            tick_pos = self.number_line.number_to_point(i)
            tick = Line(
                tick_pos + UP * 0.075,
                tick_pos + DOWN * 0.075,
                color=self.COLOR_PRIMARY,
                stroke_width=3
            )
            positive_ticks.add(tick)
        
        self.play(
            *[Create(tick) for tick in positive_ticks],
            run_time=0.8
        )
        
        # 负数刻度
        negative_ticks = VGroup()
        for i in [-1, -2, -3, -4]:
            tick_pos = self.number_line.number_to_point(i)
            tick = Line(
                tick_pos + UP * 0.075,
                tick_pos + DOWN * 0.075,
                color=self.COLOR_PRIMARY,
                stroke_width=3
            )
            negative_ticks.add(tick)
        
        self.play(
            *[Create(tick) for tick in negative_ticks],
            run_time=0.8
        )
        
        # 数字标签
        self.tick_labels = VGroup()
        for i in range(-4, 5):
            if i == 0:  # 0已经有标签了
                continue
            
            label = MathTex(str(i), font_size=20, color=WHITE)
            label.next_to(self.number_line.number_to_point(i), DOWN, buff=0.25)
            self.tick_labels.add(label)
        
        self.play(
            *[FadeIn(label) for label in self.tick_labels],
            run_time=0.8
        )
        
        # 说明文字
        explanation = Text(
            "确定刻度的间隔",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(element_title),
            FadeOut(unit_brace),
            FadeOut(unit_label),
            FadeOut(explanation),
            run_time=0.4
        )
        
        # 合并所有刻度
        all_ticks = VGroup(tick_1, positive_ticks, negative_ticks)
        
        # 移除旧的基础线，添加完整数轴
        self.remove(self.basic_line)
        self.add(self.number_line, arrow_tip, all_ticks)
        self.all_ticks = all_ticks
        self.arrow_tip = arrow_tip
    
    def show_correspondence(self):
        """场景6: 数轴与有理数的对应"""
        # 标题
        title_chinese = Text(
            "数轴上的点",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        
        arrow_symbol = MathTex(
            r"\leftrightarrow",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        )
        
        title_number = Text(
            "有理数",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        
        correspondence_title = VGroup(
            title_chinese, arrow_symbol, title_number
        ).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        
        self.play(FadeIn(correspondence_title), run_time=0.5)
        
        # 整数点高亮
        integer_dots = VGroup()
        for i in range(-4, 5):
            dot = Dot(
                self.number_line.number_to_point(i),
                color=self.COLOR_PRIMARY,
                radius=0.08
            )
            integer_dots.add(dot)
        
        self.play(
            *[Flash(dot, color=self.COLOR_PRIMARY, flash_radius=0.2) 
              for dot in integer_dots],
            run_time=0.7
        )
        
        # 添加小数点示例
        rational_dots = VGroup()
        rational_labels = VGroup()
        
        # 2.5
        dot_2_5 = Dot(
            self.number_line.number_to_point(2.5),
            color=self.COLOR_POSITIVE,
            radius=0.1
        )
        label_2_5 = MathTex("2.5", font_size=20, color=self.COLOR_POSITIVE)
        label_2_5.next_to(dot_2_5, UP, buff=0.2)
        
        self.play(
            FadeIn(dot_2_5, scale=0.5),
            FadeIn(label_2_5),
            run_time=0.6
        )
        rational_dots.add(dot_2_5)
        rational_labels.add(label_2_5)
        
        # -1.5
        dot_neg_1_5 = Dot(
            self.number_line.number_to_point(-1.5),
            color=self.COLOR_NEGATIVE,
            radius=0.1
        )
        label_neg_1_5 = MathTex("-1.5", font_size=20, color=self.COLOR_NEGATIVE)
        label_neg_1_5.next_to(dot_neg_1_5, UP, buff=0.2)
        
        self.play(
            FadeIn(dot_neg_1_5, scale=0.5),
            FadeIn(label_neg_1_5),
            run_time=0.6
        )
        rational_dots.add(dot_neg_1_5)
        rational_labels.add(label_neg_1_5)
        
        # 1/2
        dot_half = Dot(
            self.number_line.number_to_point(0.5),
            color=GREEN,
            radius=0.1
        )
        label_half = MathTex(r"\frac{1}{2}", font_size=22, color=GREEN)
        label_half.next_to(dot_half, DOWN, buff=0.35)
        
        self.play(
            FadeIn(dot_half, scale=0.5),
            FadeIn(label_half),
            run_time=0.6
        )
        rational_dots.add(dot_half)
        rational_labels.add(label_half)
        
        # -3/2
        dot_neg_3_2 = Dot(
            self.number_line.number_to_point(-1.5),
            color=ORANGE,
            radius=0.08
        )
        label_neg_3_2 = MathTex(r"-\frac{3}{2}", font_size=22, color=ORANGE)
        label_neg_3_2.next_to(dot_neg_3_2, DOWN, buff=0.35)
        
        # 由于-1.5位置已有点，稍微调整标签位置
        label_neg_3_2.shift(DOWN * 0.3)
        
        self.play(
            FadeIn(dot_neg_3_2, scale=0.5),
            FadeIn(label_neg_3_2),
            run_time=0.6
        )
        rational_dots.add(dot_neg_3_2)
        rational_labels.add(label_neg_3_2)
        
        # 说明文字
        explanation = Text(
            "每个点对应一个有理数",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(correspondence_title),
            FadeOut(explanation),
            FadeOut(rational_dots),
            FadeOut(rational_labels),
            run_time=0.5
        )
    
    def show_comparison(self):
        """场景7: 比较大小规则"""
        # 标题
        comparison_title = Text(
            "比较大小: 右边的数 > 左边的数",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(comparison_title), run_time=0.6)
        
        # 示例1: 比较 2 和 -1
        dot_2 = Dot(
            self.number_line.number_to_point(2),
            color=self.COLOR_POSITIVE,
            radius=0.12
        )
        dot_neg_1 = Dot(
            self.number_line.number_to_point(-1),
            color=self.COLOR_NEGATIVE,
            radius=0.12
        )
        
        self.play(
            FadeIn(dot_2, scale=0.5),
            FadeIn(dot_neg_1, scale=0.5),
            run_time=0.5
        )
        
        # 闪烁高亮
        self.play(
            Flash(dot_2, color=self.COLOR_POSITIVE, flash_radius=0.3),
            Flash(dot_neg_1, color=self.COLOR_NEGATIVE, flash_radius=0.3),
            run_time=0.5
        )
        
        # 箭头指示（右边）
        arrow_right = Arrow(
            self.number_line.number_to_point(-1) + UP * 0.6,
            self.number_line.number_to_point(2) + UP * 0.6,
            color=self.COLOR_POSITIVE,
            stroke_width=4,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        
        right_label = Text(
            "右",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_POSITIVE
        ).next_to(arrow_right, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow_right),
            FadeIn(right_label),
            run_time=0.6
        )
        
        # 公式显示
        formula_1 = MathTex(
            "2", ">", "-1",
            font_size=32
        ).move_to(DOWN * 3.5)
        formula_1[0].set_color(self.COLOR_POSITIVE)
        formula_1[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(formula_1), run_time=0.6)
        
        self.wait(0.6)
        
        # 清理示例1
        self.play(
            FadeOut(dot_2),
            FadeOut(dot_neg_1),
            FadeOut(arrow_right),
            FadeOut(right_label),
            FadeOut(formula_1),
            run_time=0.4
        )
        
        # 示例2: 比较 -2 和 -3
        dot_neg_2 = Dot(
            self.number_line.number_to_point(-2),
            color=ORANGE,
            radius=0.12
        )
        dot_neg_3 = Dot(
            self.number_line.number_to_point(-3),
            color=RED,
            radius=0.12
        )
        
        self.play(
            FadeIn(dot_neg_2, scale=0.5),
            FadeIn(dot_neg_3, scale=0.5),
            run_time=0.5
        )
        
        self.play(
            Flash(dot_neg_2, color=ORANGE, flash_radius=0.3),
            Flash(dot_neg_3, color=RED, flash_radius=0.3),
            run_time=0.5
        )
        
        # 箭头指示
        arrow_right_2 = Arrow(
            self.number_line.number_to_point(-3) + UP * 0.6,
            self.number_line.number_to_point(-2) + UP * 0.6,
            color=ORANGE,
            stroke_width=4,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        
        right_label_2 = Text(
            "右",
            font="PingFang SC",
            font_size=20,
            color=ORANGE
        ).next_to(arrow_right_2, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow_right_2),
            FadeIn(right_label_2),
            run_time=0.6
        )
        
        # 公式显示
        formula_2 = MathTex(
            "-2", ">", "-3",
            font_size=32
        ).move_to(DOWN * 3.5)
        formula_2[0].set_color(ORANGE)
        formula_2[2].set_color(RED)
        
        self.play(Write(formula_2), run_time=0.6)
        
        self.wait(0.6)
        
        # 清理示例2
        self.play(
            FadeOut(dot_neg_2),
            FadeOut(dot_neg_3),
            FadeOut(arrow_right_2),
            FadeOut(right_label_2),
            FadeOut(formula_2),
            run_time=0.4
        )
        
        # 动态滑动比较
        moving_dot = Dot(
            self.number_line.number_to_point(-3),
            color=self.COLOR_HIGHLIGHT,
            radius=0.15
        )
        
        value_tracker = ValueTracker(-3)
        
        moving_label = always_redraw(
            lambda: MathTex(
                f"{value_tracker.get_value():.1f}",
                font_size=24,
                color=self.COLOR_HIGHLIGHT
            ).next_to(
                self.number_line.number_to_point(value_tracker.get_value()),
                UP,
                buff=0.3
            )
        )
        
        def update_dot(mob):
            mob.move_to(self.number_line.number_to_point(value_tracker.get_value()))
        
        moving_dot.add_updater(update_dot)
        
        self.add(moving_dot, moving_label)
        
        self.play(
            value_tracker.animate.set_value(3),
            run_time=2.5,
            rate_func=smooth
        )
        
        moving_dot.remove_updater(update_dot)
        
        self.wait(0.5)
        
        # 总结
        summary = Text(
            "位置越靠右，数值越大",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(comparison_title),
            FadeOut(moving_dot),
            FadeOut(moving_label),
            FadeOut(summary),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景8: 总结与片尾"""
        # 数轴缩小并移至上方
        number_line_group = VGroup(
            self.number_line,
            self.arrow_tip,
            self.all_ticks,
            self.origin_dot,
            self.origin_labels,
            self.tick_labels
        )
        
        self.play(
            number_line_group.animate.scale(0.6).move_to(UP * 4),
            run_time=0.8
        )
        
        # 三要素卡片
        cards = VGroup()
        
        # 卡片1: 原点
        card_1 = self.create_summary_card(
            "原点",
            "确定基准位置",
            self.COLOR_ORIGIN,
            UP * 1.5
        )
        cards.add(card_1)
        
        # 卡片2: 正方向
        card_2 = self.create_summary_card(
            "正方向",
            "通常向右为正",
            self.COLOR_POSITIVE,
            UP * 0.3
        )
        cards.add(card_2)
        
        # 卡片3: 单位长度
        card_3 = self.create_summary_card(
            "单位长度",
            "确定刻度间隔",
            self.COLOR_SECONDARY,
            DOWN * 0.9
        )
        cards.add(card_3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            card.shift(LEFT * 10)  # 初始位置在左侧外
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight_text = Text(
            "数轴是有理数的直观表示!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 5.3)
        
        self.play(
            FadeOut(self.author_info),
            FadeIn(author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 小数字图标装饰
        number_icons = VGroup()
        icon_numbers = ["-3", "-1", "0", "2", "4"]
        icon_colors = [RED, ORANGE, self.COLOR_ORIGIN, GREEN, BLUE]
        
        for i, (num, color) in enumerate(zip(icon_numbers, icon_colors)):
            angle = i * 2 * PI / 5
            pos = follow_text.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            circle = Circle(radius=0.25, color=color, fill_opacity=0.8)
            label = MathTex(num, font_size=20, color=WHITE)
            icon = VGroup(circle, label).move_to(pos)
            number_icons.add(icon)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in number_icons],
            run_time=0.6
        )
        
        self.play(
            Rotate(number_icons, angle=PI, run_time=1.5)
        )
        
        self.wait(1.0)
        
        # 全部淡出
        everything = VGroup(
            number_line_group,
            cards,
            highlight_text,
            author_large,
            author_id,
            follow_text,
            number_icons
        )
        
        self.play(FadeOut(everything), run_time=1.0)
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 图标圆
        icon = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=26,
            color=WHITE,
            weight=BOLD
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql number_line_lesson.py NumberLineLesson  # 快速预览
# manim -qh number_line_lesson.py NumberLineLesson   # 高质量渲染
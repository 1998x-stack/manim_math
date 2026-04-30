"""
分数的意义 - The Meaning of Fractions
六年级数学教学动画 - Grade 6 Mathematics Teaching Animation

使用 Manim 创建的教学视频
Teaching video created with Manim

内容: 分数的定义、组成、与除法的关系
Content: Definition of fractions, components, relationship with division

目标观众: 小学六年级学生
Target Audience: Grade 6 elementary students

格式: TikTok竖屏 (1080×1920)
Format: TikTok vertical (1080×1920)

作者: 上海初高中数学直通车 @emptyandcalm
Author: Shanghai Math Express @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FractionMeaning(Scene):
    """
    分数的意义教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 圆形演示 1/4 - 基本概念
    3. 圆形演示 3/8 - 分子>1的情况
    4. 矩形演示 5/6 - 多样化理解
    5. 分数与除法 - 建立联系
    6. 分数的组成 - 认识术语
    7. 片尾总结 - 强化记忆
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调部分
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_FRACTION_PART = "#2ecc71"  # 绿色 - 分数部分
        self.COLOR_WHOLE = "#9b59b6"          # 紫色 - 整体
        
        # 字体大小配置
        self.FONT_SIZES = {
            "title": 40,
            "subtitle": 32,
            "body": 26,
            "label": 22,
            "small": 20,
            "author": 22,
            "formula": 36,
            "large_formula": 48,
        }
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_circle_quarter()
        self.show_circle_three_eighths()
        self.show_rectangle_fraction()
        self.show_division_relationship()
        self.show_fraction_components()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的位置和参数"""
        # Scene 2: 圆形 1/4
        self.circle_center_1 = UP * 2
        self.circle_radius_1 = 1.5
        self.sector_angle_quarter = PI / 2  # 90度
        
        # Scene 3: 圆形 3/8
        self.circle_center_2 = UP * 1.5
        self.circle_radius_2 = 1.5
        self.sector_angle_eighth = 2 * PI / 8  # 45度
        
        # Scene 4: 矩形
        self.rect_center = UP * 1.5
        self.rect_width = 6.0
        self.rect_height = 1.5
        self.num_parts = 6
        self.segment_width = self.rect_width / self.num_parts
        
        # 计算每个小矩形的中心位置
        self.small_rect_positions = []
        for i in range(self.num_parts):
            x_offset = -self.rect_width/2 + self.segment_width/2 + i * self.segment_width
            pos = self.rect_center + RIGHT * x_offset
            self.small_rect_positions.append(pos)
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_SIZES["author"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "一个披萨切成4份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE
        ).move_to(UP * 4)
        
        hook_text_2 = Text(
            "你吃了1份...",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=GRAY_A
        ).move_to(UP * 3)
        
        self.play(Write(hook_text), run_time=1.0)
        self.play(FadeIn(hook_text_2, shift=UP * 0.2), run_time=0.5)
        
        # 问题
        question = Text(
            "你吃了多少?",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        
        # 圆形阴影暗示
        circle_shadow = Circle(
            radius=1.2,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(circle_shadow, scale=0.8), run_time=0.5)
        self.play(
            circle_shadow.animate.scale(1.1).set_opacity(0.3),
            run_time=0.4,
            rate_func=there_and_back
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hook_text_2),
            FadeOut(question),
            FadeOut(circle_shadow),
            run_time=0.5
        )
    
    def show_circle_quarter(self):
        """场景2: 圆形演示 1/4"""
        # 标题
        title = Text(
            "分数的意义",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 完整圆形 (披萨)
        full_circle = Circle(
            radius=self.circle_radius_1,
            color=self.COLOR_PRIMARY,
            fill_color=self.COLOR_WHOLE,
            fill_opacity=0.3,
            stroke_width=4
        ).move_to(self.circle_center_1)
        
        explain_1 = Text(
            "把披萨平均分成4份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        self.play(Create(full_circle), run_time=1.0)
        self.play(FadeIn(explain_1, shift=UP * 0.2), run_time=0.5)
        
        # 四条分割线 (十字)
        line_vertical = Line(
            self.circle_center_1 + UP * self.circle_radius_1,
            self.circle_center_1 + DOWN * self.circle_radius_1,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        line_horizontal = Line(
            self.circle_center_1 + LEFT * self.circle_radius_1,
            self.circle_center_1 + RIGHT * self.circle_radius_1,
            color=self.COLOR_AUXILIARY,
            stroke_width=3
        )
        
        dividing_lines = VGroup(line_vertical, line_horizontal)
        
        self.play(Create(dividing_lines, lag_ratio=0.3), run_time=1.0)
        self.wait(0.8)
        
        # 创建4个扇形 (用于高亮)
        sector_1 = Sector(
            radius=self.circle_radius_1,
            angle=self.sector_angle_quarter,
            start_angle=PI/2,  # 从上方开始
            color=self.COLOR_FRACTION_PART,
            fill_opacity=0,
            stroke_width=0
        ).move_arc_center_to(self.circle_center_1)
        
        # 高亮第一份
        self.play(
            sector_1.animate.set_fill(opacity=0.7),
            run_time=0.8
        )
        
        # 分数符号
        fraction_1_4 = MathTex(
            r"\frac{1}{4}",
            font_size=self.FONT_SIZES["formula"] * 1.5,
            color=self.COLOR_FRACTION_PART
        ).move_to(DOWN * 2.5)
        
        explain_2 = Text(
            "取其中1份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(fraction_1_4), run_time=0.8)
        self.play(FadeIn(explain_2, shift=UP * 0.2), run_time=0.5)
        
        # 闪烁强调
        self.play(
            Flash(fraction_1_4, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(dividing_lines),
            FadeOut(sector_1),
            full_circle.animate.set_opacity(0.1),
            fraction_1_4.animate.scale(0.5).move_to(UP * 5 + LEFT * 3),
            title.animate.scale(0.7).move_to(UP * 7),
            run_time=0.6
        )
        
        self.remove(full_circle)
    
    def show_circle_three_eighths(self):
        """场景3: 圆形演示 3/8"""
        # 新圆形 (8等分)
        circle_8 = Circle(
            radius=self.circle_radius_2,
            color=self.COLOR_PRIMARY,
            fill_color=self.COLOR_WHOLE,
            fill_opacity=0.3,
            stroke_width=4
        ).move_to(self.circle_center_2)
        
        explain_3 = Text(
            "分成8份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        self.play(Create(circle_8), run_time=0.8)
        self.play(FadeIn(explain_3, shift=UP * 0.2), run_time=0.4)
        
        # 8条分割线
        lines_8 = VGroup()
        for i in range(8):
            angle = i * self.sector_angle_eighth
            end_point = self.circle_center_2 + self.circle_radius_2 * np.array([
                np.cos(angle),
                np.sin(angle),
                0
            ])
            line = Line(
                self.circle_center_2,
                end_point,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
            lines_8.add(line)
        
        self.play(Create(lines_8, lag_ratio=0.2), run_time=1.2)
        self.wait(0.5)
        
        # 高亮3个扇形 (连续)
        sectors_3 = VGroup()
        for i in range(3):
            sector = Sector(
                radius=self.circle_radius_2,
                angle=self.sector_angle_eighth,
                start_angle=i * self.sector_angle_eighth,
                color=self.COLOR_FRACTION_PART,
                fill_opacity=0,
                stroke_width=0
            ).move_arc_center_to(self.circle_center_2)
            sectors_3.add(sector)
        
        # 逐个着色
        for sector in sectors_3:
            self.play(
                sector.animate.set_fill(opacity=0.7),
                run_time=0.4
            )
        
        # 分数符号
        fraction_3_8 = MathTex(
            r"\frac{3}{8}",
            font_size=self.FONT_SIZES["formula"] * 1.5,
            color=self.COLOR_FRACTION_PART
        ).move_to(DOWN * 2.5)
        
        explain_4 = Text(
            "取其中3份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(fraction_3_8), run_time=0.8)
        self.play(FadeIn(explain_4, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(circle_8),
            FadeOut(lines_8),
            FadeOut(sectors_3),
            FadeOut(explain_3),
            FadeOut(explain_4),
            FadeOut(fraction_3_8),
            run_time=0.6
        )
    
    def show_rectangle_fraction(self):
        """场景4: 矩形演示 5/6"""
        # 说明
        explain_5 = Text(
            "也可以用矩形表示分数",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 4)
        
        self.play(FadeIn(explain_5, shift=UP * 0.2), run_time=0.5)
        
        # 大矩形
        big_rect = Rectangle(
            width=self.rect_width,
            height=self.rect_height,
            color=self.COLOR_PRIMARY,
            fill_color=self.COLOR_WHOLE,
            fill_opacity=0.3,
            stroke_width=4
        ).move_to(self.rect_center)
        
        self.play(Create(big_rect), run_time=0.8)
        
        # 竖直分割线
        vertical_lines = VGroup()
        for i in range(1, self.num_parts):
            x_pos = self.rect_center[0] - self.rect_width/2 + i * self.segment_width
            line = Line(
                [x_pos, self.rect_center[1] - self.rect_height/2, 0],
                [x_pos, self.rect_center[1] + self.rect_height/2, 0],
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
            vertical_lines.add(line)
        
        self.play(Create(vertical_lines, lag_ratio=0.2), run_time=1.0)
        self.wait(0.5)
        
        # 创建6个小矩形用于着色
        small_rects = VGroup()
        for i in range(self.num_parts):
            small_rect = Rectangle(
                width=self.segment_width,
                height=self.rect_height,
                color=self.COLOR_FRACTION_PART,
                fill_opacity=0,
                stroke_width=0
            ).move_to(self.small_rect_positions[i])
            small_rects.add(small_rect)
        
        # 高亮前5个
        for i in range(5):
            self.play(
                small_rects[i].animate.set_fill(opacity=0.7),
                run_time=0.3
            )
        
        # 分数符号
        fraction_5_6 = MathTex(
            r"\frac{5}{6}",
            font_size=self.FONT_SIZES["formula"] * 1.5,
            color=self.COLOR_FRACTION_PART
        ).move_to(DOWN * 2)
        
        explain_6 = Text(
            "取了6份中的5份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(Write(fraction_5_6), run_time=0.8)
        self.play(FadeIn(explain_6, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(big_rect),
            FadeOut(vertical_lines),
            FadeOut(small_rects),
            FadeOut(explain_5),
            FadeOut(explain_6),
            FadeOut(fraction_5_6),
            run_time=0.6
        )
    
    def show_division_relationship(self):
        """场景5: 分数与除法的关系"""
        # 标题
        subtitle = Text(
            "分数与除法的关系",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 除法算式
        division_eq = MathTex(
            r"3 \div 4",
            font_size=self.FONT_SIZES["formula"] * 1.3,
            color=WHITE
        ).move_to(UP * 3 + LEFT * 2)
        
        self.play(Write(division_eq), run_time=0.8)
        self.wait(0.5)
        
        # 等号和箭头
        arrow = MathTex(
            r"=",
            font_size=self.FONT_SIZES["formula"] * 1.3,
            color=self.COLOR_HIGHLIGHT
        ).next_to(division_eq, RIGHT, buff=0.5)
        
        self.play(FadeIn(arrow, scale=1.2), run_time=0.5)
        
        # 分数形式
        fraction_eq = MathTex(
            r"\frac{3}{4}",
            font_size=self.FONT_SIZES["formula"] * 1.3,
            color=self.COLOR_FRACTION_PART
        ).next_to(arrow, RIGHT, buff=0.5)
        
        self.play(Write(fraction_eq), run_time=0.8)
        self.wait(0.8)
        
        # 框住整个等式
        equation_group = VGroup(division_eq, arrow, fraction_eq)
        formula_box = SurroundingRectangle(
            equation_group,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            stroke_width=3
        )
        
        self.play(Create(formula_box), run_time=0.6)
        
        # 通用公式
        general_formula = MathTex(
            r"a \div b = \frac{a}{b}",
            r"\quad (b \neq 0)",
            font_size=self.FONT_SIZES["formula"],
            color=WHITE
        ).move_to(UP * 1)
        
        general_formula[1].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(general_formula), run_time=1.0)
        self.wait(1.0)
        
        # 具体例子
        example_1 = MathTex(
            r"1 \div 2 = \frac{1}{2}",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        example_2 = MathTex(
            r"5 \div 8 = \frac{5}{8}",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(example_1, shift=LEFT * 0.5), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(example_2, shift=LEFT * 0.5), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(equation_group),
            FadeOut(formula_box),
            FadeOut(general_formula),
            FadeOut(example_1),
            FadeOut(example_2),
            run_time=0.6
        )
    
    def show_fraction_components(self):
        """场景6: 分数的组成部分"""
        # 标题
        subtitle_2 = Text(
            "分数的组成",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(subtitle_2), run_time=0.8)
        
        # 大分数
        large_fraction = MathTex(
            r"\frac{3}{4}",
            font_size=self.FONT_SIZES["large_formula"] * 2,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Write(large_fraction), run_time=1.0)
        self.wait(0.5)
        
        # 分子箭头和标签
        arrow_numerator = Arrow(
            start=large_fraction.get_top() + UP * 0.5,
            end=large_fraction.get_top() + UP * 0.1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        label_numerator = Text(
            "分子",
            font="PingFang SC",
            font_size=self.FONT_SIZES["label"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_numerator, UP, buff=0.1)
        
        explain_numerator = Text(
            "表示取了几份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).next_to(label_numerator, RIGHT, buff=0.3)
        
        self.play(GrowArrow(arrow_numerator), run_time=0.5)
        self.play(FadeIn(label_numerator), run_time=0.4)
        self.play(FadeIn(explain_numerator, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 分数线箭头和标签
        arrow_line = Arrow(
            start=large_fraction.get_center() + LEFT * 1.5,
            end=large_fraction.get_center() + LEFT * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        label_line = Text(
            "分数线",
            font="PingFang SC",
            font_size=self.FONT_SIZES["label"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_line, LEFT, buff=0.1)
        
        self.play(GrowArrow(arrow_line), run_time=0.5)
        self.play(FadeIn(label_line), run_time=0.4)
        self.wait(0.5)
        
        # 分母箭头和标签
        arrow_denominator = Arrow(
            start=large_fraction.get_bottom() + DOWN * 0.5,
            end=large_fraction.get_bottom() + DOWN * 0.1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        label_denominator = Text(
            "分母",
            font="PingFang SC",
            font_size=self.FONT_SIZES["label"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_denominator, DOWN, buff=0.1)
        
        explain_denominator = Text(
            "表示平均分成几份",
            font="PingFang SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).next_to(label_denominator, RIGHT, buff=0.3)
        
        self.play(GrowArrow(arrow_denominator), run_time=0.5)
        self.play(FadeIn(label_denominator), run_time=0.4)
        self.play(FadeIn(explain_denominator, shift=LEFT * 0.3), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle_2),
            FadeOut(large_fraction),
            FadeOut(arrow_numerator),
            FadeOut(label_numerator),
            FadeOut(explain_numerator),
            FadeOut(arrow_line),
            FadeOut(label_line),
            FadeOut(arrow_denominator),
            FadeOut(label_denominator),
            FadeOut(explain_denominator),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾总结与关注"""
        # 总结标题
        summary_title = Text(
            "记住这些!",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 要点列表
        point_1 = Text(
            "• 分数 = 分子 / 分母",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 3)
        
        point_2 = Text(
            "• a ÷ b = a/b (b ≠ 0)",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 2)
        
        point_3 = Text(
            "• 表示部分与整体的关系",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(FadeIn(point_1, shift=LEFT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(point_2, shift=LEFT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(point_3, shift=LEFT * 0.5), run_time=0.6)
        self.wait(1.0)
        
        # 作者信息放大
        self.play(
            self.author_info.animate.scale(1.5).move_to(DOWN * 1),
            FadeOut(summary_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标 (小圆圈)
        icons = VGroup()
        for i in range(5):
            icon = Circle(
                radius=0.2,
                fill_color=[
                    self.COLOR_PRIMARY,
                    self.COLOR_FRACTION_PART,
                    self.COLOR_SECONDARY,
                    self.COLOR_HIGHLIGHT,
                    "#9b59b6"
                ][i],
                fill_opacity=0.8,
                stroke_width=0
            ).shift(DOWN * 5 + RIGHT * (i - 2) * 1.2)
            icons.add(icon)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
        
        # 图标闪烁
        for icon in icons:
            self.play(
                Flash(icon, color=YELLOW, flash_radius=0.3),
                run_time=0.2
            )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 渲染命令:
# manim -pql fraction_meaning.py FractionMeaning  # 快速预览 (480p)
# manim -qh fraction_meaning.py FractionMeaning   # 高质量渲染 (1080p)
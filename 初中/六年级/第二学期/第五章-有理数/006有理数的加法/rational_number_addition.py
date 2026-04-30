"""
有理数的加法 - Rational Number Addition Animation
使用 Manim 创建的中学数学教学视频

内容: 有理数加法的三条法则及数轴可视化
目标观众: 六年级学生
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


class RationalNumberAddition(Scene):
    """
    有理数加法教学动画场景
    
    场景顺序:
    1. 开场引入
    2. 同号加法 - 正数+正数
    3. 同号加法 - 负数+负数
    4. 异号加法 - 正+负 (正数绝对值大)
    5. 异号加法 - 负+正 (负数绝对值大)
    6. 与零相加
    7. 总结 - 加法法则
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_POSITIVE = "#2ecc71"      # 绿色 - 正数
        self.COLOR_NEGATIVE = "#e74c3c"      # 红色 - 负数
        self.COLOR_ZERO = "#95a5a6"          # 灰色 - 零
        self.COLOR_RESULT = "#f39c12"        # 橙色 - 结果
        self.COLOR_NUMBERLINE = WHITE        # 数轴
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 辅助元素
        
        # 字体大小配置
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_FORMULA = 32
        
        # 数轴配置
        self.UNIT_LENGTH = 0.7
        self.NUMBERLINE_POS = UP * 2
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_positive_plus_positive()
        self.show_negative_plus_negative()
        self.show_positive_plus_negative_case1()
        self.show_negative_plus_positive_case2()
        self.show_add_zero()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化数轴和相关元素"""
        # 创建数轴 (-6 到 6)
        self.number_line = NumberLine(
            x_range=[-6, 6, 1],
            length=12 * self.UNIT_LENGTH,
            include_numbers=True,
            numbers_to_include=range(-6, 7),
            font_size=20,
            color=self.COLOR_NUMBERLINE,
            include_tip=True,
            tip_width=0.15,
            tip_height=0.15,
        ).move_to(self.NUMBERLINE_POS)
        
        # 数轴标签
        self.number_line_label = Text(
            "数轴",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(self.number_line, DOWN, buff=0.3)
    
    def show_opening(self):
        """场景1: 开场引入"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "正数 + 负数 = ?",
            font="PingFang SC",
            font_size=self.FONT_TITLE + 8,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=1.2)
        
        # 副标题
        subtitle = Text(
            "用数轴秒懂加法!",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 数轴创建
        self.play(Create(self.number_line), run_time=1.5)
        self.play(FadeIn(self.number_line_label), run_time=0.4)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_positive_plus_positive(self):
        """场景2: 同号加法 - 正数+正数"""
        # 标题
        title = Text(
            "同号加法: 正数+正数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"(+3) + (+2) = \ ?",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula.set_color_by_tex("+3", self.COLOR_POSITIVE)
        formula.set_color_by_tex("+2", self.COLOR_POSITIVE)
        
        self.play(FadeIn(title), run_time=0.4)
        self.play(Write(formula), run_time=0.6)
        self.wait(0.3)
        
        # 起点: 0
        start_dot = Dot(
            self.number_line.n2p(0),
            color=self.COLOR_ZERO,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_ZERO, flash_radius=0.25), run_time=0.3)
        
        # 第一步: 0 → +3
        arrow1 = Arrow(
            self.number_line.n2p(0),
            self.number_line.n2p(3),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step1_text = Text(
            "先加 +3",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow1), run_time=1.0)
        self.play(FadeIn(step1_text, shift=UP * 0.2), run_time=0.4)
        
        # 中间点: +3
        mid_dot = Dot(
            self.number_line.n2p(3),
            color=self.COLOR_POSITIVE,
            radius=0.08
        )
        self.play(FadeIn(mid_dot, scale=0.5), run_time=0.3)
        self.wait(0.4)
        
        # 第二步: +3 → +5
        arrow2 = Arrow(
            self.number_line.n2p(3),
            self.number_line.n2p(5),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step2_text = Text(
            "再加 +2",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(DOWN * 0.5)
        
        self.play(GrowArrow(arrow2), run_time=1.0)
        self.play(FadeIn(step2_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: +5
        result_dot = Dot(
            self.number_line.n2p(5),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"(+3) + (+2) = +5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        rule_text = Text(
            "同号相加, 绝对值相加",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(Write(conclusion), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(start_dot),
            FadeOut(mid_dot),
            FadeOut(result_dot),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(step1_text),
            FadeOut(step2_text),
            FadeOut(conclusion),
            FadeOut(rule_text),
            run_time=0.6
        )
    
    def show_negative_plus_negative(self):
        """场景3: 同号加法 - 负数+负数"""
        # 标题
        title = Text(
            "同号加法: 负数+负数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"(-2) + (-3) = \ ?",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula.set_color_by_tex("-2", self.COLOR_NEGATIVE)
        formula.set_color_by_tex("-3", self.COLOR_NEGATIVE)
        
        self.play(FadeIn(title), run_time=0.4)
        self.play(Write(formula), run_time=0.6)
        self.wait(0.3)
        
        # 起点: 0
        start_dot = Dot(
            self.number_line.n2p(0),
            color=self.COLOR_ZERO,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_ZERO, flash_radius=0.25), run_time=0.3)
        
        # 第一步: 0 → -2
        arrow1 = Arrow(
            self.number_line.n2p(0),
            self.number_line.n2p(-2),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step1_text = Text(
            "先加 -2 (向左)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow1), run_time=1.0)
        self.play(FadeIn(step1_text, shift=UP * 0.2), run_time=0.4)
        
        # 中间点: -2
        mid_dot = Dot(
            self.number_line.n2p(-2),
            color=self.COLOR_NEGATIVE,
            radius=0.08
        )
        self.play(FadeIn(mid_dot, scale=0.5), run_time=0.3)
        self.wait(0.4)
        
        # 第二步: -2 → -5
        arrow2 = Arrow(
            self.number_line.n2p(-2),
            self.number_line.n2p(-5),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step2_text = Text(
            "再加 -3 (继续向左)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(DOWN * 0.5)
        
        self.play(GrowArrow(arrow2), run_time=1.0)
        self.play(FadeIn(step2_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: -5
        result_dot = Dot(
            self.number_line.n2p(-5),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"(-2) + (-3) = -5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        rule_text = Text(
            "同号相加, 绝对值相加",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(Write(conclusion), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(start_dot),
            FadeOut(mid_dot),
            FadeOut(result_dot),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(step1_text),
            FadeOut(step2_text),
            FadeOut(conclusion),
            FadeOut(rule_text),
            run_time=0.6
        )
    
    def show_positive_plus_negative_case1(self):
        """场景4: 异号加法 - 正+负 (正数绝对值大)"""
        # 标题
        title = Text(
            "异号加法: 正数+负数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=YELLOW
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"(+5) + (-2) = \ ?",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula[0][1:3].set_color(self.COLOR_POSITIVE)  # +5
        formula[0][5:7].set_color(self.COLOR_NEGATIVE)  # -2
        
        self.play(FadeIn(title), run_time=0.4)
        self.play(Write(formula), run_time=0.6)
        self.wait(0.3)
        
        # 起点: 0
        start_dot = Dot(
            self.number_line.n2p(0),
            color=self.COLOR_ZERO,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_ZERO, flash_radius=0.25), run_time=0.3)
        
        # 第一步: 0 → +5
        arrow1 = Arrow(
            self.number_line.n2p(0),
            self.number_line.n2p(5),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step1_text = Text(
            "先加 +5 (向右)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow1), run_time=1.0)
        self.play(FadeIn(step1_text, shift=UP * 0.2), run_time=0.4)
        
        # 中间点: +5
        mid_dot = Dot(
            self.number_line.n2p(5),
            color=self.COLOR_POSITIVE,
            radius=0.08
        )
        self.play(FadeIn(mid_dot, scale=0.5), run_time=0.3)
        self.wait(0.4)
        
        # 第二步: +5 → +3 (向左2格)
        arrow2 = Arrow(
            self.number_line.n2p(5),
            self.number_line.n2p(3),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step2_text = Text(
            "再加 -2 (向左)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(DOWN * 0.5)
        
        self.play(GrowArrow(arrow2), run_time=1.0)
        self.play(FadeIn(step2_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: +3
        result_dot = Dot(
            self.number_line.n2p(3),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"(+5) + (-2) = +3",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        rule_text = Text(
            "异号相加, 绝对值相减",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        note_text = Text(
            "正数绝对值大 → 结果为正",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_POSITIVE
        ).move_to(DOWN * 3.8)
        
        self.play(Write(conclusion), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.5)
        self.play(FadeIn(note_text), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(start_dot),
            FadeOut(mid_dot),
            FadeOut(result_dot),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(step1_text),
            FadeOut(step2_text),
            FadeOut(conclusion),
            FadeOut(rule_text),
            FadeOut(note_text),
            run_time=0.6
        )
    
    def show_negative_plus_positive_case2(self):
        """场景5: 异号加法 - 负+正 (负数绝对值大)"""
        # 标题
        title = Text(
            "异号加法: 负数+正数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=YELLOW
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"(-5) + (+2) = \ ?",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula[0][1:3].set_color(self.COLOR_NEGATIVE)  # -5
        formula[0][5:7].set_color(self.COLOR_POSITIVE)  # +2
        
        self.play(FadeIn(title), run_time=0.4)
        self.play(Write(formula), run_time=0.6)
        self.wait(0.3)
        
        # 起点: 0
        start_dot = Dot(
            self.number_line.n2p(0),
            color=self.COLOR_ZERO,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_ZERO, flash_radius=0.25), run_time=0.3)
        
        # 第一步: 0 → -5
        arrow1 = Arrow(
            self.number_line.n2p(0),
            self.number_line.n2p(-5),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step1_text = Text(
            "先加 -5 (向左)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow1), run_time=1.0)
        self.play(FadeIn(step1_text, shift=UP * 0.2), run_time=0.4)
        
        # 中间点: -5
        mid_dot = Dot(
            self.number_line.n2p(-5),
            color=self.COLOR_NEGATIVE,
            radius=0.08
        )
        self.play(FadeIn(mid_dot, scale=0.5), run_time=0.3)
        self.wait(0.4)
        
        # 第二步: -5 → -3 (向右2格)
        arrow2 = Arrow(
            self.number_line.n2p(-5),
            self.number_line.n2p(-3),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step2_text = Text(
            "再加 +2 (向右)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(DOWN * 0.5)
        
        self.play(GrowArrow(arrow2), run_time=1.0)
        self.play(FadeIn(step2_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: -3
        result_dot = Dot(
            self.number_line.n2p(-3),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"(-5) + (+2) = -3",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        rule_text = Text(
            "异号相加, 绝对值相减",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        note_text = Text(
            "负数绝对值大 → 结果为负",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_NEGATIVE
        ).move_to(DOWN * 3.8)
        
        self.play(Write(conclusion), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.5)
        self.play(FadeIn(note_text), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(start_dot),
            FadeOut(mid_dot),
            FadeOut(result_dot),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(step1_text),
            FadeOut(step2_text),
            FadeOut(conclusion),
            FadeOut(rule_text),
            FadeOut(note_text),
            run_time=0.6
        )
    
    def show_add_zero(self):
        """场景6: 与零相加"""
        # 标题
        title = Text(
            "与零相加",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ZERO
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"(+3) + 0 = \ ?",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula[0][1:3].set_color(self.COLOR_POSITIVE)  # +3
        formula[0][5].set_color(self.COLOR_ZERO)  # 0
        
        self.play(FadeIn(title), run_time=0.4)
        self.play(Write(formula), run_time=0.6)
        self.wait(0.3)
        
        # 起点: 0
        start_dot = Dot(
            self.number_line.n2p(0),
            color=self.COLOR_ZERO,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_ZERO, flash_radius=0.25), run_time=0.3)
        
        # 第一步: 0 → +3
        arrow1 = Arrow(
            self.number_line.n2p(0),
            self.number_line.n2p(3),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step1_text = Text(
            "先到 +3",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow1), run_time=1.0)
        self.play(FadeIn(step1_text, shift=UP * 0.2), run_time=0.4)
        
        # 到达 +3
        dot_at_3 = Dot(
            self.number_line.n2p(3),
            color=self.COLOR_POSITIVE,
            radius=0.1
        )
        self.play(FadeIn(dot_at_3, scale=0.5), run_time=0.3)
        self.play(Flash(dot_at_3, color=self.COLOR_POSITIVE, flash_radius=0.25), run_time=0.3)
        self.wait(0.3)
        
        # 加0说明
        add_zero_text = Text(
            "加 0",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_ZERO
        ).move_to(ORIGIN)
        
        self.play(Write(add_zero_text), run_time=0.5)
        self.wait(0.5)
        
        # 停留说明
        stay_text = Text(
            "位置不变!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(stay_text, shift=UP * 0.3), run_time=0.5)
        
        # 结果点闪烁
        result_dot = Dot(
            self.number_line.n2p(3),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        self.play(Transform(dot_at_3, result_dot), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"a + 0 = a",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2.5)
        
        rule_text = Text(
            "任何数加0都等于它本身",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(Write(conclusion), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(start_dot),
            FadeOut(dot_at_3),
            FadeOut(arrow1),
            FadeOut(step1_text),
            FadeOut(add_zero_text),
            FadeOut(stay_text),
            FadeOut(conclusion),
            FadeOut(rule_text),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结 - 加法法则"""
        # 数轴淡出
        self.play(
            FadeOut(self.number_line),
            FadeOut(self.number_line_label),
            run_time=0.5
        )
        
        # 大标题
        title = Text(
            "有理数加法法则",
            font="PingFang SC",
            font_size=self.FONT_TITLE + 4,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)
        
        # 法则卡片
        cards = VGroup()
        
        # 法则1
        card1 = self.create_rule_card(
            "法则1",
            "同号两数相加",
            "取相同符号, 绝对值相加",
            self.COLOR_POSITIVE,
            UP * 3
        )
        cards.add(card1)
        
        # 法则2
        card2 = self.create_rule_card(
            "法则2",
            "异号两数相加",
            "取绝对值较大数的符号, 绝对值相减",
            YELLOW,
            UP * 1
        )
        cards.add(card2)
        
        # 法则3
        card3 = self.create_rule_card(
            "法则3",
            "一个数与0相加",
            "仍得这个数",
            self.COLOR_ZERO,
            DOWN * 1
        )
        cards.add(card3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            card.shift(LEFT * 10)  # 初始在左侧外
            self.play(card.animate.shift(RIGHT * 10), run_time=0.6)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 重点提示
        highlight = Text(
            "掌握法则, 轻松计算!",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(highlight, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def create_rule_card(self, title, subtitle, content, color, position):
        """创建法则卡片"""
        # 图标
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=26,
            color=WHITE,
            weight=BOLD
        )
        
        # 副标题
        subtitle_text = Text(
            subtitle,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 垂直组合
        text_group = VGroup(title_text, subtitle_text, content_text).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        # 水平组合
        card = VGroup(icon, text_group).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者信息放大
        author_name = Text(
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
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 数轴图标装饰
        icon_numberlines = VGroup()
        for i in range(3):
            nl = NumberLine(
                x_range=[-2, 2, 1],
                length=2,
                include_tip=True,
                tip_width=0.1,
                tip_height=0.1,
                color=GOLD
            ).scale(0.5).move_to(DOWN * (2.5 + i * 0.6))
            icon_numberlines.add(nl)
        
        self.play(
            *[FadeIn(nl, shift=LEFT * 0.5) for nl in icon_numberlines],
            run_time=0.6
        )
        
        # 旋转装饰
        self.play(Rotate(icon_numberlines, angle=PI/6, run_time=1.0))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icon_numberlines),
            run_time=1.0
        )


# 运行命令:
# manim -pql rational_number_addition.py RationalNumberAddition  # 快速预览
# manim -qh rational_number_addition.py RationalNumberAddition   # 高质量 1080p
# manim -qk rational_number_addition.py RationalNumberAddition   # 4K质量
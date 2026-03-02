"""
分数与小数的互化 - Fraction-Decimal Conversion Animation
使用 Manim 创建的六年级数学教学视频

内容: 分数化小数、小数化分数、有限小数判定
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


class FractionDecimalConversion(Scene):
    """
    分数与小数互化教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 分数化小数 - 除法原理
    3. 小数化分数 - 位数定分母
    4. 数轴可视化对比
    5. 有限小数判定法则
    6. 互动练习题
    7. 总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_FRACTION = "#3498db"      # 蓝色 - 分数
        self.COLOR_DECIMAL = "#e74c3c"       # 红色 - 小数
        self.COLOR_DIVISION = "#2ecc71"      # 绿色 - 除法过程
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_PRIME = "#9b59b6"         # 紫色 - 素因数
        self.COLOR_ARROW = "#f39c12"         # 橙色 - 箭头
        
        # 初始化位置数据
        self.setup_positions()
        
        # 执行动画序列
        self.show_opening()
        self.show_fraction_to_decimal()
        self.show_decimal_to_fraction()
        self.show_numberline_comparison()
        self.show_finite_decimal_rule()
        self.show_practice()
        self.show_summary()
    
    def setup_positions(self):
        """初始化所有位置常量"""
        # 基准位置
        self.ORIGIN_POS = ORIGIN
        self.AUTHOR_POS = UP * 7
        self.TITLE_POS = UP * 5.5
        self.SUBTITLE_POS = UP * 4.8
        self.MAIN_CONTENT_POS = UP * 2
        self.DIVISION_AREA = ORIGIN
        self.FORMULA_AREA = DOWN * 2
        self.BOTTOM_TEXT_POS = DOWN * 5
        
        # 边界检查
        self.MAX_Y = 7.5
        self.MIN_Y = -7.5
        self.MAX_X = 4.0
        self.MIN_X = -4.0
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(self.AUTHOR_POS)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "分数和小数怎么互相转换?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 分数示例 3/4
        fraction_top = MathTex(r"3", font_size=48, color=self.COLOR_FRACTION)
        fraction_line = Line(LEFT * 0.3, RIGHT * 0.3, color=self.COLOR_FRACTION, stroke_width=3)
        fraction_bottom = MathTex(r"4", font_size=48, color=self.COLOR_FRACTION)
        
        fraction = VGroup(fraction_top, fraction_line, fraction_bottom).arrange(DOWN, buff=0.15)
        fraction.move_to(LEFT * 2.5 + UP * 2.5)
        
        # 问号
        question_mark = Text("?", font_size=60, color=WHITE).move_to(UP * 2.5)
        
        # 小数示例 0.75
        decimal = MathTex(r"0.75", font_size=48, color=self.COLOR_DECIMAL).move_to(RIGHT * 2.5 + UP * 2.5)
        
        self.play(FadeIn(fraction, shift=RIGHT * 0.5), run_time=0.5)
        self.play(Flash(question_mark, color=WHITE, flash_radius=0.4), FadeIn(question_mark, scale=0.5), run_time=0.5)
        self.play(FadeIn(decimal, shift=LEFT * 0.5), run_time=0.5)
        self.wait(1.0)
        
        # 清理 - 保留分数和小数用于过渡
        self.play(FadeOut(hook_text), FadeOut(question_mark), run_time=0.5)
        
        # 存储以供后续场景使用
        self.fraction_example = fraction
        self.decimal_example = decimal
    
    def show_fraction_to_decimal(self):
        """场景2: 分数化小数 - 除法原理"""
        # 标题
        title_chinese = Text("分数", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_FRACTION)
        title_arrow = MathTex(r"\rightarrow", font_size=36, color=WHITE)
        title_chinese2 = Text("小数", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_DECIMAL)
        
        title = VGroup(title_chinese, title_arrow, title_chinese2).arrange(RIGHT, buff=0.3)
        title.move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 核心规则
        rule_text = Text(
            "分子除以分母",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(self.SUBTITLE_POS)
        
        self.play(FadeIn(rule_text), run_time=0.5)
        
        # 移动分数到中心
        self.play(self.fraction_example.animate.move_to(UP * 2.5), run_time=0.8)
        
        # 转换为除法
        equals = MathTex(r"=", font_size=40, color=WHITE).next_to(self.fraction_example, RIGHT, buff=0.3)
        division = MathTex(r"3 \div 4", font_size=40, color=self.COLOR_DIVISION).next_to(equals, RIGHT, buff=0.3)
        
        arrow = Arrow(
            self.fraction_example.get_right() + RIGHT * 0.1,
            division.get_left() + LEFT * 0.1,
            color=self.COLOR_ARROW,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(equals), Write(division), run_time=0.8)
        self.wait(0.5)
        
        # 长除法演示
        division_title = Text(
            "列竖式计算:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.2)
        
        self.play(FadeIn(division_title), run_time=0.4)
        
        # 创建长除法框架
        # 4 ) 3.00
        divisor = MathTex(r"4", font_size=36, color=self.COLOR_DIVISION)
        division_symbol = MathTex(r")", font_size=36, color=WHITE)
        dividend = MathTex(r"3.00", font_size=36, color=self.COLOR_FRACTION)
        
        division_setup = VGroup(divisor, division_symbol, dividend).arrange(RIGHT, buff=0.2)
        division_setup.move_to(UP * 0.5)
        
        self.play(Write(division_setup), run_time=0.8)
        
        # 商的位置 (0.75)
        quotient_line = Line(
            division_setup.get_left() + LEFT * 0.3 + UP * 0.4,
            division_setup.get_right() + RIGHT * 0.3 + UP * 0.4,
            color=WHITE,
            stroke_width=2
        )
        
        self.play(Create(quotient_line), run_time=0.3)
        
        # 步骤1: 3÷4不够，添加小数点
        step1_text = Text(
            "3÷4不够除,变成30÷4",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        quotient_0 = MathTex(r"0.", font_size=36, color=self.COLOR_DECIMAL).next_to(quotient_line, UP, buff=0.1)
        quotient_0.align_to(dividend, LEFT)
        
        self.play(FadeIn(step1_text), Write(quotient_0), run_time=0.8)
        self.wait(0.5)
        
        # 步骤2: 30÷4=7余2
        step2_calc = VGroup(
            MathTex(r"30 \div 4 = 7", font_size=24, color=self.COLOR_DIVISION),
            Text("余", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_DIVISION),
            MathTex(r"2", font_size=24, color=self.COLOR_DIVISION),
        ).arrange(RIGHT, buff=0.15)
        step2_calc.move_to(DOWN * 1.2)
        
        quotient_7 = MathTex(r"7", font_size=36, color=self.COLOR_DECIMAL).next_to(quotient_0, RIGHT, buff=0.05)
        
        self.play(FadeOut(step1_text), run_time=0.2)
        self.play(Write(step2_calc), Write(quotient_7), run_time=0.8)
        self.wait(0.5)
        
        # 步骤3: 20÷4=5
        step3_calc = MathTex(r"20 \div 4 = 5", font_size=24, color=self.COLOR_DIVISION).move_to(DOWN * 1.8)
        
        quotient_5 = MathTex(r"5", font_size=36, color=self.COLOR_DECIMAL).next_to(quotient_7, RIGHT, buff=0.05)
        
        self.play(FadeOut(step2_calc), run_time=0.2)
        self.play(Write(step3_calc), Write(quotient_5), run_time=0.8)
        
        # 最终结果
        result_quotient = VGroup(quotient_0, quotient_7, quotient_5)
        
        result_text = Text(
            "结果: 0.75",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DECIMAL
        ).move_to(DOWN * 3)
        
        self.play(
            Flash(result_quotient, color=self.COLOR_DECIMAL, flash_radius=0.5),
            FadeIn(result_text, scale=1.2),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule_text),
            FadeOut(equals),
            FadeOut(division),
            FadeOut(arrow),
            FadeOut(division_title),
            FadeOut(division_setup),
            FadeOut(quotient_line),
            FadeOut(result_quotient),
            FadeOut(step3_calc),
            FadeOut(result_text),
            run_time=0.6
        )
        
        # 移动分数和小数到屏幕外准备下一场景
        self.play(
            self.fraction_example.animate.move_to(UP * 10),
            self.decimal_example.animate.move_to(UP * 2.5),
            run_time=0.4
        )
    
    def show_decimal_to_fraction(self):
        """场景3: 小数化分数 - 位数定分母"""
        # 标题
        title_chinese = Text("小数", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_DECIMAL)
        title_arrow = MathTex(r"\rightarrow", font_size=36, color=WHITE)
        title_chinese2 = Text("分数", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_FRACTION)
        
        title = VGroup(title_chinese, title_arrow, title_chinese2).arrange(RIGHT, buff=0.3)
        title.move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 核心规则
        rule_text = Text(
            "小数位数决定分母",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(self.SUBTITLE_POS)
        
        self.play(FadeIn(rule_text), run_time=0.5)
        
        # 示例: 0.125
        decimal_example = MathTex(r"0.125", font_size=48, color=self.COLOR_DECIMAL).move_to(UP * 2.5)
        
        self.play(Write(decimal_example), run_time=0.8)
        
        # 标注小数位数
        digit_dots = VGroup(*[
            Dot(color=self.COLOR_HIGHLIGHT, radius=0.06).move_to(
                decimal_example.get_center() + RIGHT * (0.35 + 0.3 * i) + DOWN * 0.4
            )
            for i in range(3)
        ])
        
        digit_text = Text(
            "3位小数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(digit_dots, DOWN, buff=0.3)
        
        self.play(FadeIn(digit_dots, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(digit_text), run_time=0.4)
        self.wait(0.6)
        
        # 箭头指向分数
        arrow = Arrow(
            decimal_example.get_bottom() + DOWN * 1.0,
            decimal_example.get_bottom() + DOWN * 2.0,
            color=self.COLOR_ARROW,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 分母: 1000 (3位小数 → 10³)
        denominator_text = Text(
            "分母:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(LEFT * 2 + ORIGIN)
        
        denominator = MathTex(r"1000", font_size=40, color=self.COLOR_FRACTION).next_to(denominator_text, RIGHT, buff=0.3)
        
        explanation = MathTex(r"= 10^3", font_size=28, color=GRAY_A).next_to(denominator, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(denominator_text),
            Write(denominator),
            FadeIn(explanation),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 分子: 125
        numerator_text = Text(
            "分子:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(LEFT * 2 + DOWN * 0.8)
        
        numerator = MathTex(r"125", font_size=40, color=self.COLOR_FRACTION).next_to(numerator_text, RIGHT, buff=0.3)
        
        note = Text(
            "(小数部分)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(numerator, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(numerator_text),
            Write(numerator),
            FadeIn(note),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 组合成分数
        fraction_line = Line(LEFT * 0.4, RIGHT * 0.4, color=self.COLOR_FRACTION, stroke_width=3).move_to(DOWN * 2)
        fraction_num = MathTex(r"125", font_size=40, color=self.COLOR_FRACTION).next_to(fraction_line, UP, buff=0.15)
        fraction_den = MathTex(r"1000", font_size=40, color=self.COLOR_FRACTION).next_to(fraction_line, DOWN, buff=0.15)
        
        fraction_group = VGroup(fraction_num, fraction_line, fraction_den)
        
        self.play(
            FadeOut(denominator_text),
            FadeOut(explanation),
            FadeOut(numerator_text),
            FadeOut(note),
            TransformFromCopy(numerator, fraction_num),
            TransformFromCopy(denominator, fraction_den),
            Create(fraction_line),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 约分提示
        simplify_hint = Text(
            "需要约分!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(simplify_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        
        # 约分过程: ÷125
        divide_symbol = MathTex(r"\div 125", font_size=28, color=self.COLOR_DIVISION).next_to(fraction_group, RIGHT, buff=0.5)
        
        self.play(Write(divide_symbol), run_time=0.6)
        
        # 最简分数: 1/8
        final_line = Line(LEFT * 0.25, RIGHT * 0.25, color=self.COLOR_FRACTION, stroke_width=3).move_to(RIGHT * 2.5 + DOWN * 2)
        final_num = MathTex(r"1", font_size=40, color=self.COLOR_FRACTION).next_to(final_line, UP, buff=0.15)
        final_den = MathTex(r"8", font_size=40, color=self.COLOR_FRACTION).next_to(final_line, DOWN, buff=0.15)
        
        final_fraction = VGroup(final_num, final_line, final_den)
        
        self.play(
            Transform(fraction_group, final_fraction),
            FadeOut(divide_symbol),
            FadeOut(simplify_hint),
            run_time=1.0
        )
        
        self.play(Flash(final_fraction, color=self.COLOR_FRACTION, flash_radius=0.5), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule_text),
            FadeOut(decimal_example),
            FadeOut(digit_dots),
            FadeOut(digit_text),
            FadeOut(arrow),
            FadeOut(numerator),
            FadeOut(denominator),
            FadeOut(fraction_group),
            run_time=0.6
        )
    
    def show_numberline_comparison(self):
        """场景4: 数轴可视化对比"""
        # 标题
        title = Text(
            "在数轴上是同一个点!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 创建数轴 (0到1)
        numberline = NumberLine(
            x_range=[0, 1, 0.25],
            length=7,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24,
            numbers_to_include=[0, 0.25, 0.5, 0.75, 1]
        ).move_to(ORIGIN)
        
        self.play(Create(numberline), run_time=1.2)
        
        # 标记0和1
        zero_label = MathTex(r"0", font_size=28).next_to(numberline.n2p(0), DOWN, buff=0.4)
        one_label = MathTex(r"1", font_size=28).next_to(numberline.n2p(1), DOWN, buff=0.4)
        
        self.play(FadeIn(zero_label), FadeIn(one_label), run_time=0.5)
        
        # 3/4从上方降落
        fraction_top = MathTex(r"3", font_size=36, color=self.COLOR_FRACTION)
        fraction_line_small = Line(LEFT * 0.2, RIGHT * 0.2, color=self.COLOR_FRACTION, stroke_width=2)
        fraction_bottom = MathTex(r"4", font_size=36, color=self.COLOR_FRACTION)
        
        fraction = VGroup(fraction_top, fraction_line_small, fraction_bottom).arrange(DOWN, buff=0.1)
        fraction.move_to(UP * 4)
        
        target_position = numberline.n2p(0.75)
        
        self.play(FadeIn(fraction, shift=DOWN * 0.3), run_time=0.5)
        self.play(fraction.animate.move_to(target_position + UP * 1.5), run_time=0.8)
        
        # 连线到数轴
        line_to_numberline_1 = DashedLine(
            fraction.get_bottom(),
            target_position + UP * 0.3,
            color=self.COLOR_FRACTION,
            dash_length=0.1
        )
        
        dot_fraction = Dot(target_position, color=self.COLOR_FRACTION, radius=0.1)
        
        self.play(Create(line_to_numberline_1), FadeIn(dot_fraction, scale=0.5), run_time=0.8)
        self.play(Flash(dot_fraction, color=self.COLOR_FRACTION, flash_radius=0.3), run_time=0.5)
        
        # 0.75从下方升起
        decimal = MathTex(r"0.75", font_size=36, color=self.COLOR_DECIMAL).move_to(DOWN * 4)
        
        self.play(FadeIn(decimal, shift=UP * 0.3), run_time=0.5)
        self.play(decimal.animate.move_to(target_position + DOWN * 1.5), run_time=0.8)
        
        # 连线到数轴
        line_to_numberline_2 = DashedLine(
            decimal.get_top(),
            target_position + DOWN * 0.3,
            color=self.COLOR_DECIMAL,
            dash_length=0.1
        )
        
        dot_decimal = Dot(target_position, color=self.COLOR_DECIMAL, radius=0.1)
        
        self.play(Create(line_to_numberline_2), FadeIn(dot_decimal, scale=0.5), run_time=0.8)
        
        # 重合效果
        self.play(
            Flash(target_position, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        
        # 等号强调
        equals_sign = MathTex(r"=", font_size=60, color=YELLOW).move_to(target_position + UP * 3)
        
        self.play(Write(equals_sign, run_time=0.6))
        
        conclusion = Text(
            "分数和小数表示同一个数!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(numberline),
            FadeOut(zero_label),
            FadeOut(one_label),
            FadeOut(fraction),
            FadeOut(decimal),
            FadeOut(line_to_numberline_1),
            FadeOut(line_to_numberline_2),
            FadeOut(dot_fraction),
            FadeOut(dot_decimal),
            FadeOut(equals_sign),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_finite_decimal_rule(self):
        """场景5: 有限小数判定法则"""
        # 大标题
        question_title = Text(
            "如何判断能否化为有限小数?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(question_title), run_time=1.0)
        
        # 法则卡片
        rule_box = Rectangle(
            width=7,
            height=1.2,
            color=self.COLOR_PRIME,
            stroke_width=3,
            fill_opacity=0.1
        ).move_to(UP * 5)
        
        rule_text = Text(
            "分母的素因数只含2和5",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(rule_box.get_center())
        
        rule_group = VGroup(rule_box, rule_text)
        rule_group.move_to(LEFT * 10 + UP * 5)  # 从左侧外开始
        
        self.play(rule_group.animate.move_to(UP * 5), run_time=0.8)
        self.wait(0.5)
        
        # 示例1: 3/4
        example_1_title = Text("示例1:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(LEFT * 3 + UP * 3)
        
        ex1_frac_top = MathTex(r"3", font_size=32, color=self.COLOR_FRACTION)
        ex1_frac_line = Line(LEFT * 0.2, RIGHT * 0.2, color=self.COLOR_FRACTION, stroke_width=2)
        ex1_frac_bottom = MathTex(r"4", font_size=32, color=self.COLOR_FRACTION)
        ex1_fraction = VGroup(ex1_frac_top, ex1_frac_line, ex1_frac_bottom).arrange(DOWN, buff=0.1)
        ex1_fraction.next_to(example_1_title, RIGHT, buff=0.3)
        
        self.play(FadeIn(example_1_title), FadeIn(ex1_fraction), run_time=0.5)
        
        # 分解分母
        factorization_1 = MathTex(r"4 = 2^2", font_size=28, color=self.COLOR_PRIME).next_to(ex1_fraction, RIGHT, buff=0.5)
        
        self.play(Write(factorization_1), run_time=1.0)
        
        # 结论
        conclusion_1 = Text(
            "只含2 → 有限小数 ✓",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GREEN
        ).next_to(factorization_1, RIGHT, buff=0.5)
        
        self.play(FadeIn(conclusion_1, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 示例2: 1/8
        example_2_title = Text("示例2:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(LEFT * 3 + UP * 1.5)
        
        ex2_frac_top = MathTex(r"1", font_size=32, color=self.COLOR_FRACTION)
        ex2_frac_line = Line(LEFT * 0.2, RIGHT * 0.2, color=self.COLOR_FRACTION, stroke_width=2)
        ex2_frac_bottom = MathTex(r"8", font_size=32, color=self.COLOR_FRACTION)
        ex2_fraction = VGroup(ex2_frac_top, ex2_frac_line, ex2_frac_bottom).arrange(DOWN, buff=0.1)
        ex2_fraction.next_to(example_2_title, RIGHT, buff=0.3)
        
        self.play(FadeIn(example_2_title), FadeIn(ex2_fraction), run_time=0.5)
        
        factorization_2 = MathTex(r"8 = 2^3", font_size=28, color=self.COLOR_PRIME).next_to(ex2_fraction, RIGHT, buff=0.5)
        
        self.play(Write(factorization_2), run_time=1.0)
        
        conclusion_2 = Text(
            "只含2 → 有限小数 ✓",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GREEN
        ).next_to(factorization_2, RIGHT, buff=0.5)
        
        self.play(FadeIn(conclusion_2, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 示例3: 1/6 (反例)
        example_3_title = Text("示例3:", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).move_to(LEFT * 3 + ORIGIN)
        
        ex3_frac_top = MathTex(r"1", font_size=32, color=self.COLOR_FRACTION)
        ex3_frac_line = Line(LEFT * 0.2, RIGHT * 0.2, color=self.COLOR_FRACTION, stroke_width=2)
        ex3_frac_bottom = MathTex(r"6", font_size=32, color=self.COLOR_FRACTION)
        ex3_fraction = VGroup(ex3_frac_top, ex3_frac_line, ex3_frac_bottom).arrange(DOWN, buff=0.1)
        ex3_fraction.next_to(example_3_title, RIGHT, buff=0.3)
        
        self.play(FadeIn(example_3_title), FadeIn(ex3_fraction), run_time=0.5)
        
        factorization_3 = MathTex(r"6 = 2 \times 3", font_size=28, color=self.COLOR_PRIME).next_to(ex3_fraction, RIGHT, buff=0.5)
        
        self.play(Write(factorization_3), run_time=1.0)
        
        conclusion_3 = Text(
            "含3 → 无限小数 ✗",
            font="Noto Sans CJK SC",
            font_size=22,
            color=RED
        ).next_to(factorization_3, RIGHT, buff=0.5)
        
        self.play(FadeIn(conclusion_3, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 关键公式高亮
        formula_box = Rectangle(
            width=7,
            height=1.0,
            color=YELLOW,
            stroke_width=4,
            fill_opacity=0.15
        ).move_to(DOWN * 3)
        
        formula_text = VGroup(
            Text("分母", font="Noto Sans CJK SC", font_size=32, color=YELLOW),
            MathTex(r"= 2^m \times 5^n", font_size=32, color=YELLOW)
        ).arrange(RIGHT, buff=0.2).move_to(formula_box.get_center())
        
        formula_group = VGroup(formula_box, formula_text)
        
        self.play(FadeIn(formula_group, scale=1.1), run_time=0.6)
        self.play(Flash(formula_box, color=YELLOW, flash_radius=0.8), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(question_title),
            FadeOut(rule_group),
            FadeOut(example_1_title),
            FadeOut(ex1_fraction),
            FadeOut(factorization_1),
            FadeOut(conclusion_1),
            FadeOut(example_2_title),
            FadeOut(ex2_fraction),
            FadeOut(factorization_2),
            FadeOut(conclusion_2),
            FadeOut(example_3_title),
            FadeOut(ex3_fraction),
            FadeOut(factorization_3),
            FadeOut(conclusion_3),
            FadeOut(formula_group),
            run_time=0.6
        )
    
    def show_practice(self):
        """场景6: 互动练习题"""
        # 练习标题
        practice_title = Text(
            "快速练习",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(practice_title, scale=1.1), run_time=0.5)
        
        # 题目
        problem_text = Text(
            "判断 2/5 能否化为有限小数?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(Write(problem_text), run_time=0.8)
        
        # 分数显示
        prob_frac_top = MathTex(r"2", font_size=48, color=self.COLOR_FRACTION)
        prob_frac_line = Line(LEFT * 0.3, RIGHT * 0.3, color=self.COLOR_FRACTION, stroke_width=3)
        prob_frac_bottom = MathTex(r"5", font_size=48, color=self.COLOR_FRACTION)
        prob_fraction = VGroup(prob_frac_top, prob_frac_line, prob_frac_bottom).arrange(DOWN, buff=0.15)
        prob_fraction.move_to(UP * 3)
        
        self.play(FadeIn(prob_fraction, shift=UP * 0.3), run_time=0.5)
        
        # 倒计时3秒
        countdown = DecimalNumber(
            3,
            num_decimal_places=0,
            font_size=60,
            color=YELLOW
        ).move_to(UP * 1.5)
        
        thinking_text = Text(
            "思考中...",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).next_to(countdown, DOWN, buff=0.5)
        
        self.play(FadeIn(countdown), FadeIn(thinking_text), run_time=0.3)
        
        # 倒计时动画
        self.play(countdown.animate.set_value(2), run_time=1.0)
        self.play(countdown.animate.set_value(1), run_time=1.0)
        self.play(countdown.animate.set_value(0), run_time=1.0)
        
        self.play(FadeOut(countdown), FadeOut(thinking_text), run_time=0.3)
        
        # 解答步骤1: 分析分母
        step_1_text = Text(
            "步骤1: 看分母",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        denominator_highlight = MathTex(r"5", font_size=48, color=YELLOW).move_to(ORIGIN)
        
        self.play(FadeIn(step_1_text), run_time=0.4)
        self.play(FadeIn(denominator_highlight, scale=1.2), run_time=0.5)
        self.wait(0.5)
        
        # 解答步骤2: 素因数分解
        step_2_text = Text(
            "步骤2: 素因数分解",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        factorization = MathTex(r"5 = 5^1", font_size=36, color=self.COLOR_PRIME).move_to(DOWN * 1.8)
        
        self.play(FadeOut(step_1_text), run_time=0.2)
        self.play(FadeIn(step_2_text), Write(factorization), run_time=1.0)
        self.wait(0.5)
        
        # 解答步骤3: 判断
        step_3_text = Text(
            "步骤3: 只含5",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        ).move_to(DOWN * 3)
        
        self.play(FadeOut(step_2_text), run_time=0.2)
        self.play(FadeIn(step_3_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 结论
        conclusion = Text(
            "能化为有限小数! ✓",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GREEN
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, scale=1.2), run_time=0.6)
        self.play(Flash(conclusion, color=GREEN, flash_radius=0.8), run_time=0.5)
        self.wait(0.5)
        
        # 验证
        verification = MathTex(r"2 \div 5 = 0.4", font_size=32, color=self.COLOR_DECIMAL).move_to(DOWN * 6)
        
        self.play(Write(verification), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(practice_title),
            FadeOut(problem_text),
            FadeOut(prob_fraction),
            FadeOut(denominator_highlight),
            FadeOut(factorization),
            FadeOut(step_3_text),
            FadeOut(conclusion),
            FadeOut(verification),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结 + 片尾"""
        # 总结标题
        summary_title = Text(
            "知识点总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 知识点卡片
        # 卡片1: 分数→小数
        card_1 = self.create_summary_card(
            "分数 → 小数",
            "分子 ÷ 分母",
            self.COLOR_FRACTION,
            UP * 3.5
        )
        
        # 卡片2: 小数→分数
        card_2 = self.create_summary_card(
            "小数 → 分数",
            "位数定分母, 再约分",
            self.COLOR_DECIMAL,
            UP * 1.5
        )
        
        # 卡片3: 有限小数判定
        card_3 = self.create_summary_card(
            "有限小数判定",
            "分母 = 2ᵐ × 5ⁿ",
            self.COLOR_PRIME,
            DOWN * 0.5
        )
        
        # 卡片依次滑入
        self.play(card_1.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.3)
        self.play(card_2.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.3)
        self.play(card_3.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_large),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=1.0
        )
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰圆圈
        circles = VGroup(*[
            Circle(radius=0.15, color=color, fill_opacity=0.6)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * TAU / 5), np.sin(i * TAU / 5), 0]))
            for i, color in enumerate([self.COLOR_FRACTION, self.COLOR_DECIMAL, self.COLOR_DIVISION, 
                                       self.COLOR_PRIME, self.COLOR_HIGHLIGHT])
        ])
        
        self.play(*[FadeIn(circle, scale=0.5) for circle in circles], run_time=0.6)
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 图标圆
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql fraction_decimal.py FractionDecimalConversion  # 快速预览
# manim -qh fraction_decimal.py FractionDecimalConversion   # 高质量渲染
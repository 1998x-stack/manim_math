"""
分数与小数的互化 - Fraction-Decimal Conversion Animation
使用 Manim 创建的六年级数学教学视频

内容: 分数化小数、小数化分数、有限小数判定
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

修复说明：
  原代码中 self.decimal_example (0.75) 生命周期混乱：
  ① show_fraction_to_decimal() 末尾仅把它移到 UP*2.5，从未 FadeOut
  ② show_decimal_to_fraction() 里又创建了同名局部变量 (0.125)，两者重叠
  ③ show_numberline_comparison() 里 self.decimal_example 仍游荡在屏幕上

  修复策略：
  · show_opening() 展示 3/4 ↔ 0.75 作为引子，两者都存为实例变量
  · show_fraction_to_decimal() 用 self.decimal_example 作为"结果答案"出现，
    场景末统一 FadeOut，生命周期结束
  · 后续场景只使用各自的局部变量，互不干扰
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
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_FRACTION = "#3498db"
        self.COLOR_DECIMAL   = "#e74c3c"
        self.COLOR_DIVISION  = "#2ecc71"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_PRIME     = "#9b59b6"
        self.COLOR_ARROW     = "#f39c12"

        self.setup_positions()

        self.show_opening()
        self.show_fraction_to_decimal()
        self.show_decimal_to_fraction()
        self.show_numberline_comparison()
        self.show_finite_decimal_rule()
        self.show_practice()
        self.show_summary()

    def setup_positions(self):
        self.AUTHOR_POS      = UP * 7
        self.TITLE_POS       = UP * 5.5
        self.SUBTITLE_POS    = UP * 4.8

    # ------------------------------------------------------------------ #
    #  辅助：构建一个手写风格分数 VGroup                                    #
    # ------------------------------------------------------------------ #
    def make_fraction(self, num_str, den_str, color, font_size=48, line_width=0.3):
        num  = MathTex(num_str, font_size=font_size, color=color)
        bar  = Line(LEFT * line_width, RIGHT * line_width, color=color, stroke_width=3)
        den  = MathTex(den_str, font_size=font_size, color=color)
        return VGroup(num, bar, den).arrange(DOWN, buff=0.15)

    # ------------------------------------------------------------------ #

    def show_opening(self):
        """
        场景1: 开场钩子
        出场：self.fraction_example (3/4)、self.decimal_example (0.75)
        均存为实例变量，供 show_fraction_to_decimal() 使用后统一清理。
        """
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=20, color=GRAY_B,
        ).move_to(self.AUTHOR_POS)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        hook_text = Text(
            "分数和小数怎么互相转换?",
            font="PingFang SC", font_size=36, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5)
        self.play(Write(hook_text), run_time=1.2)

        # 3/4（实例变量，场景2会继续使用）
        self.fraction_example = self.make_fraction(
            "3", "4", self.COLOR_FRACTION, font_size=48
        ).move_to(LEFT * 2.5 + UP * 2.5)

        question_mark = Text("?", font_size=60, color=WHITE).move_to(UP * 2.5)

        # 0.75（实例变量，场景2末尾作为"答案"揭晓并清理）
        self.decimal_example = MathTex(
            r"0.75", font_size=48, color=self.COLOR_DECIMAL,
        ).move_to(RIGHT * 2.5 + UP * 2.5)

        self.play(FadeIn(self.fraction_example, shift=RIGHT * 0.5), run_time=0.5)
        self.play(
            Flash(question_mark, color=WHITE, flash_radius=0.4),
            FadeIn(question_mark, scale=0.5),
            run_time=0.5,
        )
        self.play(FadeIn(self.decimal_example, shift=LEFT * 0.5), run_time=0.5)
        self.wait(1.0)

        # 清理钩子文字和问号；分数和小数留在屏幕，由场景2处理
        self.play(FadeOut(hook_text), FadeOut(question_mark), run_time=0.5)

    def show_fraction_to_decimal(self):
        """
        场景2: 分数化小数 - 除法原理
        使用 self.fraction_example (3/4) 演示转换过程，
        用 self.decimal_example (0.75) 作为最终"答案"揭晓，
        场景末尾统一 FadeOut 两者 ← 生命周期在此结束。
        """
        # 标题
        title = VGroup(
            Text("分数", font="PingFang SC", font_size=36, color=self.COLOR_FRACTION),
            MathTex(r"\rightarrow", font_size=36, color=WHITE),
            Text("小数", font="PingFang SC", font_size=36, color=self.COLOR_DECIMAL),
        ).arrange(RIGHT, buff=0.3).move_to(self.TITLE_POS)
        self.play(Write(title), run_time=0.8)

        rule_text = Text(
            "分子除以分母",
            font="PingFang SC", font_size=28, color=GRAY_A,
        ).move_to(self.SUBTITLE_POS)
        self.play(FadeIn(rule_text), run_time=0.5)

        # 把 self.decimal_example 暂时移出画面，稍后作为结果揭晓
        # （它在开场时位于 RIGHT*2.5+UP*2.5，直接隐藏并等待复出）
        self.play(
            self.decimal_example.animate.set_opacity(0),
            run_time=0.3,
        )

        # 将分数移到中心
        self.play(
            self.fraction_example.animate.move_to(UP * 2.5),
            run_time=0.8,
        )

        # 转换为除法表达式
        equals   = MathTex(r"=", font_size=40, color=WHITE).next_to(self.fraction_example, RIGHT, buff=0.3)
        division = MathTex(r"3 \div 4", font_size=40, color=self.COLOR_DIVISION).next_to(equals, RIGHT, buff=0.3)
        arrow    = Arrow(
            self.fraction_example.get_right() + RIGHT * 0.1,
            division.get_left() + LEFT * 0.1,
            color=self.COLOR_ARROW, buff=0.1, stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(equals), Write(division), run_time=0.8)
        self.wait(0.5)

        # 长除法演示
        division_title = Text(
            "列竖式计算:",
            font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(UP * 1.2)
        self.play(FadeIn(division_title), run_time=0.4)

        divisor        = MathTex(r"4",    font_size=36, color=self.COLOR_DIVISION)
        div_symbol     = MathTex(r")",    font_size=36, color=WHITE)
        dividend       = MathTex(r"3.00", font_size=36, color=self.COLOR_FRACTION)
        division_setup = VGroup(divisor, div_symbol, dividend).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)
        self.play(Write(division_setup), run_time=0.8)

        quotient_line = Line(
            division_setup.get_left()  + LEFT  * 0.3 + UP * 0.4,
            division_setup.get_right() + RIGHT * 0.3 + UP * 0.4,
            color=WHITE, stroke_width=2,
        )
        self.play(Create(quotient_line), run_time=0.3)

        # 步骤1
        step1_text = Text(
            "3÷4不够除,变成30÷4",
            font="PingFang SC", font_size=20, color=GRAY_A,
        ).move_to(DOWN * 0.5)
        quotient_0 = MathTex(r"0.", font_size=36, color=self.COLOR_DECIMAL)
        quotient_0.next_to(quotient_line, UP, buff=0.1).align_to(dividend, LEFT)
        self.play(FadeIn(step1_text), Write(quotient_0), run_time=0.8)
        self.wait(0.5)

        # 步骤2
        step2_calc = VGroup(
            MathTex(r"30 \div 4 = 7", font_size=24, color=self.COLOR_DIVISION),
            Text("余", font="PingFang SC", font_size=24, color=self.COLOR_DIVISION),
            MathTex(r"2", font_size=24, color=self.COLOR_DIVISION),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.2)
        quotient_7 = MathTex(r"7", font_size=36, color=self.COLOR_DECIMAL).next_to(quotient_0, RIGHT, buff=0.05)
        self.play(FadeOut(step1_text), run_time=0.2)
        self.play(Write(step2_calc), Write(quotient_7), run_time=0.8)
        self.wait(0.5)

        # 步骤3
        step3_calc = MathTex(r"20 \div 4 = 5", font_size=24, color=self.COLOR_DIVISION).move_to(DOWN * 1.8)
        quotient_5 = MathTex(r"5", font_size=36, color=self.COLOR_DECIMAL).next_to(quotient_7, RIGHT, buff=0.05)
        self.play(FadeOut(step2_calc), run_time=0.2)
        self.play(Write(step3_calc), Write(quotient_5), run_time=0.8)

        result_quotient = VGroup(quotient_0, quotient_7, quotient_5)

        # ── 关键：把 self.decimal_example 作为最终答案揭晓 ── #
        # 移到结果位置，重新显示
        self.decimal_example.move_to(DOWN * 3)
        self.play(
            Flash(result_quotient, color=self.COLOR_DECIMAL, flash_radius=0.5),
            self.decimal_example.animate.set_opacity(1),   # 淡入揭晓
            run_time=0.8,
        )
        result_label = Text(
            "结果:",
            font="PingFang SC", font_size=28, color=self.COLOR_DECIMAL,
        ).next_to(self.decimal_example, LEFT, buff=0.3)
        self.play(FadeIn(result_label), run_time=0.3)
        self.play(Circumscribe(self.decimal_example, color=self.COLOR_DECIMAL), run_time=0.6)
        self.wait(1.2)

        # ── 场景2结束：统一清理，self.fraction_example 和 self.decimal_example 生命周期结束 ──
        self.play(
            FadeOut(title),
            FadeOut(rule_text),
            FadeOut(self.fraction_example),   # ← 正式退场
            FadeOut(equals),
            FadeOut(division),
            FadeOut(arrow),
            FadeOut(division_title),
            FadeOut(division_setup),
            FadeOut(quotient_line),
            FadeOut(result_quotient),
            FadeOut(step3_calc),
            FadeOut(self.decimal_example),    # ← 正式退场
            FadeOut(result_label),
            run_time=0.6,
        )
        # 实例变量置 None，防止后续场景意外使用
        self.fraction_example = None
        self.decimal_example  = None

    def show_decimal_to_fraction(self):
        """
        场景3: 小数化分数 - 位数定分母
        完全使用局部变量，与场景1/2的实例变量无关。
        """
        title = VGroup(
            Text("小数", font="PingFang SC", font_size=36, color=self.COLOR_DECIMAL),
            MathTex(r"\rightarrow", font_size=36, color=WHITE),
            Text("分数", font="PingFang SC", font_size=36, color=self.COLOR_FRACTION),
        ).arrange(RIGHT, buff=0.3).move_to(self.TITLE_POS)
        self.play(Write(title), run_time=0.8)

        rule_text = Text(
            "小数位数决定分母",
            font="PingFang SC", font_size=28, color=GRAY_A,
        ).move_to(self.SUBTITLE_POS)
        self.play(FadeIn(rule_text), run_time=0.5)

        # 示例局部变量 0.125
        decimal_local = MathTex(r"0.125", font_size=48, color=self.COLOR_DECIMAL).move_to(UP * 2.5)
        self.play(Write(decimal_local), run_time=0.8)

        digit_dots = VGroup(*[
            Dot(color=self.COLOR_HIGHLIGHT, radius=0.06).move_to(
                decimal_local.get_center() + RIGHT * (0.35 + 0.3 * i) + DOWN * 0.4
            )
            for i in range(3)
        ])
        digit_text = Text(
            "3位小数",
            font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT,
        ).next_to(digit_dots, DOWN, buff=0.3)
        self.play(FadeIn(digit_dots, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(digit_text), run_time=0.4)
        self.wait(0.6)

        arrow = Arrow(
            decimal_local.get_bottom() + DOWN * 1.0,
            decimal_local.get_bottom() + DOWN * 2.0,
            color=self.COLOR_ARROW, buff=0.1, stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )
        self.play(GrowArrow(arrow), run_time=0.5)

        denom_label = Text("分母:", font="PingFang SC", font_size=24, color=GRAY_A).move_to(LEFT * 2)
        denominator = MathTex(r"1000", font_size=40, color=self.COLOR_FRACTION).next_to(denom_label, RIGHT, buff=0.3)
        explanation = MathTex(r"= 10^3", font_size=28, color=GRAY_A).next_to(denominator, RIGHT, buff=0.2)
        self.play(FadeIn(denom_label), Write(denominator), FadeIn(explanation), run_time=0.8)
        self.wait(0.5)

        numer_label = Text("分子:", font="PingFang SC", font_size=24, color=GRAY_A).move_to(LEFT * 2 + DOWN * 0.8)
        numerator   = MathTex(r"125", font_size=40, color=self.COLOR_FRACTION).next_to(numer_label, RIGHT, buff=0.3)
        note        = Text("(小数部分)", font="PingFang SC", font_size=20, color=GRAY_A).next_to(numerator, RIGHT, buff=0.2)
        self.play(FadeIn(numer_label), Write(numerator), FadeIn(note), run_time=0.8)
        self.wait(0.5)

        fraction_line = Line(LEFT * 0.4, RIGHT * 0.4, color=self.COLOR_FRACTION, stroke_width=3).move_to(DOWN * 2)
        fraction_num  = MathTex(r"125",  font_size=40, color=self.COLOR_FRACTION).next_to(fraction_line, UP,   buff=0.15)
        fraction_den  = MathTex(r"1000", font_size=40, color=self.COLOR_FRACTION).next_to(fraction_line, DOWN, buff=0.15)
        fraction_group = VGroup(fraction_num, fraction_line, fraction_den)

        self.play(
            FadeOut(denom_label), FadeOut(explanation),
            FadeOut(numer_label), FadeOut(note),
            TransformFromCopy(numerator,   fraction_num),
            TransformFromCopy(denominator, fraction_den),
            Create(fraction_line),
            run_time=1.0,
        )
        self.wait(0.5)

        simplify_hint = Text(
            "需要约分!",
            font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(simplify_hint, shift=UP * 0.2), run_time=0.5)

        divide_symbol = MathTex(r"\div 125", font_size=28, color=self.COLOR_DIVISION).next_to(fraction_group, RIGHT, buff=0.5)
        self.play(Write(divide_symbol), run_time=0.6)

        final_line = Line(LEFT * 0.25, RIGHT * 0.25, color=self.COLOR_FRACTION, stroke_width=3).move_to(RIGHT * 2.5 + DOWN * 2)
        final_num  = MathTex(r"1", font_size=40, color=self.COLOR_FRACTION).next_to(final_line, UP,   buff=0.15)
        final_den  = MathTex(r"8", font_size=40, color=self.COLOR_FRACTION).next_to(final_line, DOWN, buff=0.15)
        final_fraction = VGroup(final_num, final_line, final_den)

        self.play(
            Transform(fraction_group, final_fraction),
            FadeOut(divide_symbol),
            FadeOut(simplify_hint),
            run_time=1.0,
        )
        self.play(Flash(final_fraction, color=self.COLOR_FRACTION, flash_radius=0.5), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(rule_text),
            FadeOut(decimal_local),
            FadeOut(digit_dots), FadeOut(digit_text),
            FadeOut(arrow),
            FadeOut(numerator), FadeOut(denominator),
            FadeOut(fraction_group),
            run_time=0.6,
        )

    def show_numberline_comparison(self):
        """场景4: 数轴可视化对比（完全使用局部变量）"""
        title = Text(
            "在数轴上是同一个点!",
            font="PingFang SC", font_size=36, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        numberline = NumberLine(
            x_range=[0, 1, 0.25],
            length=7,
            include_numbers=True,
            label_direction=DOWN,
            font_size=24,
            numbers_to_include=[0, 0.25, 0.5, 0.75, 1],
        ).move_to(ORIGIN)
        self.play(Create(numberline), run_time=1.2)

        target_position = numberline.n2p(0.75)

        # 局部分数 3/4 从上方降落
        fraction_local = self.make_fraction("3", "4", self.COLOR_FRACTION, font_size=36, line_width=0.2)
        fraction_local.move_to(UP * 4)
        self.play(FadeIn(fraction_local, shift=DOWN * 0.3), run_time=0.5)
        self.play(fraction_local.animate.move_to(target_position + UP * 1.5), run_time=0.8)

        line1 = DashedLine(fraction_local.get_bottom(), target_position + UP * 0.3,
                           color=self.COLOR_FRACTION, dash_length=0.1)
        dot1  = Dot(target_position, color=self.COLOR_FRACTION, radius=0.1)
        self.play(Create(line1), FadeIn(dot1, scale=0.5), run_time=0.8)
        self.play(Flash(dot1, color=self.COLOR_FRACTION, flash_radius=0.3), run_time=0.5)

        # 局部小数 0.75 从下方升起
        decimal_local = MathTex(r"0.75", font_size=36, color=self.COLOR_DECIMAL).move_to(DOWN * 4)
        self.play(FadeIn(decimal_local, shift=UP * 0.3), run_time=0.5)
        self.play(decimal_local.animate.move_to(target_position + DOWN * 1.5), run_time=0.8)

        line2 = DashedLine(decimal_local.get_top(), target_position + DOWN * 0.3,
                           color=self.COLOR_DECIMAL, dash_length=0.1)
        dot2  = Dot(target_position, color=self.COLOR_DECIMAL, radius=0.1)
        self.play(Create(line2), FadeIn(dot2, scale=0.5), run_time=0.8)

        self.play(Flash(target_position, color=YELLOW, flash_radius=0.5), run_time=0.6)

        equals_sign = MathTex(r"=", font_size=60, color=YELLOW).move_to(target_position + UP * 3)
        self.play(Write(equals_sign), run_time=0.6)

        conclusion = Text(
            "分数和小数表示同一个数!",
            font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(DOWN * 4)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(numberline),
            FadeOut(fraction_local), FadeOut(decimal_local),
            FadeOut(line1), FadeOut(line2),
            FadeOut(dot1), FadeOut(dot2),
            FadeOut(equals_sign), FadeOut(conclusion),
            run_time=0.6,
        )

    def show_finite_decimal_rule(self):
        """场景5: 有限小数判定法则"""
        question_title = Text(
            "如何判断能否化为有限小数?",
            font="PingFang SC", font_size=32, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(question_title), run_time=1.0)

        rule_box  = Rectangle(width=7, height=1.2, color=self.COLOR_PRIME, stroke_width=3, fill_opacity=0.1).move_to(UP * 5)
        rule_text = Text("分母的素因数只含2和5", font="PingFang SC", font_size=28, color=WHITE).move_to(rule_box.get_center())
        rule_group = VGroup(rule_box, rule_text)
        rule_group.shift(LEFT * 10)
        self.play(rule_group.animate.shift(RIGHT * 10), run_time=0.8)
        self.wait(0.5)

        def make_example_row(label_str, num_str, den_str, factor_tex, concl_str, concl_color, y):
            label   = Text(label_str, font="PingFang SC", font_size=24, color=GRAY_A).move_to(LEFT * 3.5 + UP * y)
            frac    = self.make_fraction(num_str, den_str, self.COLOR_FRACTION, font_size=32, line_width=0.2)
            frac.next_to(label, RIGHT, buff=0.3)
            factor  = MathTex(factor_tex, font_size=28, color=self.COLOR_PRIME).next_to(frac, RIGHT, buff=0.5)
            concl   = Text(concl_str, font="PingFang SC", font_size=22, color=concl_color).next_to(factor, RIGHT, buff=0.4)
            return label, frac, factor, concl

        l1, f1, fa1, c1 = make_example_row("示例1:", "3", "4", r"4 = 2^2",         "只含2 → 有限 ✓", GREEN, 3)
        l2, f2, fa2, c2 = make_example_row("示例2:", "1", "8", r"8 = 2^3",         "只含2 → 有限 ✓", GREEN, 1.5)
        l3, f3, fa3, c3 = make_example_row("示例3:", "1", "6", r"6 = 2 \times 3",  "含3 → 无限 ✗",  RED,   0)

        for label, frac, factor, concl in [(l1,f1,fa1,c1), (l2,f2,fa2,c2), (l3,f3,fa3,c3)]:
            self.play(FadeIn(label), FadeIn(frac), run_time=0.4)
            self.play(Write(factor), run_time=0.8)
            self.play(FadeIn(concl, shift=LEFT * 0.3), run_time=0.5)
            self.wait(0.8)

        formula_box  = Rectangle(width=7, height=1.0, color=YELLOW, stroke_width=4, fill_opacity=0.15).move_to(DOWN * 3)
        formula_text = VGroup(
            Text("分母", font="PingFang SC", font_size=32, color=YELLOW),
            MathTex(r"= 2^m \times 5^n", font_size=32, color=YELLOW),
        ).arrange(RIGHT, buff=0.2).move_to(formula_box.get_center())
        formula_group = VGroup(formula_box, formula_text)

        self.play(FadeIn(formula_group, scale=1.1), run_time=0.6)
        self.play(Flash(formula_box, color=YELLOW, flash_radius=0.8), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(question_title), FadeOut(rule_group),
            FadeOut(l1), FadeOut(f1), FadeOut(fa1), FadeOut(c1),
            FadeOut(l2), FadeOut(f2), FadeOut(fa2), FadeOut(c2),
            FadeOut(l3), FadeOut(f3), FadeOut(fa3), FadeOut(c3),
            FadeOut(formula_group),
            run_time=0.6,
        )

    def show_practice(self):
        """场景6: 互动练习题"""
        practice_title = Text(
            "快速练习",
            font="PingFang SC", font_size=40, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(FadeIn(practice_title, scale=1.1), run_time=0.5)

        problem_text = Text(
            "判断 2/5 能否化为有限小数?",
            font="PingFang SC", font_size=32, color=WHITE,
        ).move_to(UP * 5)
        self.play(Write(problem_text), run_time=0.8)

        prob_fraction = self.make_fraction("2", "5", self.COLOR_FRACTION, font_size=48).move_to(UP * 3)
        self.play(FadeIn(prob_fraction, shift=UP * 0.3), run_time=0.5)

        # 倒计时
        countdown = DecimalNumber(3, num_decimal_places=0, font_size=60, color=YELLOW).move_to(UP * 1.5)
        thinking  = Text("思考中...", font="PingFang SC", font_size=24, color=GRAY_A).next_to(countdown, DOWN, buff=0.5)
        self.play(FadeIn(countdown), FadeIn(thinking), run_time=0.3)
        for val in [2, 1, 0]:
            self.play(countdown.animate.set_value(val), run_time=1.0)
        self.play(FadeOut(countdown), FadeOut(thinking), run_time=0.3)

        # 解答
        step1 = Text("步骤1: 看分母", font="PingFang SC", font_size=24, color=GRAY_A).move_to(UP * 0.5)
        denom_hl = MathTex(r"5", font_size=48, color=YELLOW).move_to(ORIGIN)
        self.play(FadeIn(step1), run_time=0.4)
        self.play(FadeIn(denom_hl, scale=1.2), run_time=0.5)
        self.wait(0.5)

        step2       = Text("步骤2: 素因数分解", font="PingFang SC", font_size=24, color=GRAY_A).move_to(DOWN * 1)
        factorization = MathTex(r"5 = 5^1", font_size=36, color=self.COLOR_PRIME).move_to(DOWN * 1.8)
        self.play(FadeOut(step1), run_time=0.2)
        self.play(FadeIn(step2), Write(factorization), run_time=1.0)
        self.wait(0.5)

        step3 = Text("步骤3: 只含5", font="PingFang SC", font_size=24, color=GREEN).move_to(DOWN * 3)
        self.play(FadeOut(step2), run_time=0.2)
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        conclusion = Text("能化为有限小数! ✓", font="PingFang SC", font_size=36, color=GREEN).move_to(DOWN * 4.5)
        self.play(FadeIn(conclusion, scale=1.2), run_time=0.6)
        self.play(Flash(conclusion, color=GREEN, flash_radius=0.8), run_time=0.5)
        self.wait(0.5)

        verification = MathTex(r"2 \div 5 = 0.4", font_size=32, color=self.COLOR_DECIMAL).move_to(DOWN * 6)
        self.play(Write(verification), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(practice_title), FadeOut(problem_text), FadeOut(prob_fraction),
            FadeOut(denom_hl), FadeOut(factorization),
            FadeOut(step3), FadeOut(conclusion), FadeOut(verification),
            run_time=0.6,
        )

    def show_summary(self):
        """场景7: 总结 + 片尾"""
        summary_title = Text(
            "知识点总结",
            font="PingFang SC", font_size=40, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(summary_title), run_time=0.8)

        def make_card(title, content, color, position):
            icon    = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
            t_text  = Text(title,   font="PingFang SC", font_size=26, color=WHITE)
            c_text  = Text(content, font="PingFang SC", font_size=22, color=GRAY_A)
            card    = VGroup(icon, VGroup(t_text, c_text).arrange(DOWN, buff=0.1, aligned_edge=LEFT))
            card.arrange(RIGHT, buff=0.4).move_to(position).shift(LEFT * 10)
            return card

        card_1 = make_card("分数 → 小数", "分子 ÷ 分母",      self.COLOR_FRACTION, UP * 3.5)
        card_2 = make_card("小数 → 分数", "位数定分母, 再约分", self.COLOR_DECIMAL,  UP * 1.5)
        card_3 = make_card("有限小数判定", "分母 = 2ᵐ × 5ⁿ",  self.COLOR_PRIME,    DOWN * 0.5)

        for card in [card_1, card_2, card_3]:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.6)
            self.wait(0.3)
        self.wait(1.0)

        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC", font_size=32, color=WHITE,
        ).move_to(DOWN * 3)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC", font_size=28, color=GRAY_B,
        ).next_to(author_large, DOWN, buff=0.3)

        self.play(Transform(self.author_info, author_large), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC", font_size=28, color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        colors  = [self.COLOR_FRACTION, self.COLOR_DECIMAL, self.COLOR_DIVISION,
                   self.COLOR_PRIME, self.COLOR_HIGHLIGHT]
        circles = VGroup(*[
            Circle(radius=0.15, color=c, fill_opacity=0.6).move_to(
                follow_text.get_center() + 1.8 * np.array([np.cos(i * TAU / 5), np.sin(i * TAU / 5), 0])
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(circle, scale=0.5) for circle in circles], run_time=0.6)
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        self.wait(1.5)

        self.play(
            FadeOut(summary_title),
            FadeOut(card_1), FadeOut(card_2), FadeOut(card_3),
            FadeOut(self.author_info), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(circles),
            run_time=1.0,
        )


# 运行命令:
# manim -pql fraction_decimal.py FractionDecimalConversion  # 快速预览
# manim -qh fraction_decimal.py FractionDecimalConversion   # 高质量渲染
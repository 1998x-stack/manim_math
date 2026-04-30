"""
负数的乘除法 - Multiplication and Division of Negative Numbers
使用 Manim 创建的小学六年级数学教学视频

内容: 理解正数、负数相乘相除的符号法则：同号得正、异号得负
目标观众: 六年级学生
格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class NegativeMulDivLesson(Scene):
    """
    负数的乘除法教学动画

    场景顺序:
    1. 开场钩子 - 引出问题
    2. 正正得正 - (+3) x (+4) = +12
    3. 正负得负 / 负正得负 - (+3) x (-4) = -12
    4. 负负得正 - (-3) x (-4) = +12 (方向反转的直觉)
    5. 符号法则总结 (乘法)
    6. 除法符号法则 - 与乘法类似
    7. 零的特殊性
    8. 综合练习
    9. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色方案
        self.COLOR_POS = "#2ecc71"        # 正数 - 绿色
        self.COLOR_NEG = "#e74c3c"        # 负数 - 红色
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_FORMULA = "#3498db"    # 公式蓝
        self.COLOR_RESULT = "#f39c12"     # 结果橙
        self.COLOR_RULE = "#9b59b6"       # 规则紫

        # 数轴参数
        self.NL_CENTER = UP * 1.5
        self.NL_UNIT = 0.45

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_pos_times_pos()
        self.scene_3_pos_times_neg()
        self.scene_4_neg_times_neg()
        self.scene_5_mul_rule_summary()
        self.scene_6_division_rule()
        self.scene_7_zero_rule()
        self.scene_8_practice()
        self.scene_9_outro()

    # ─────────────────────────────────────────
    # Helper: create a number line
    # ─────────────────────────────────────────
    def _make_number_line(self, x_range=None, y_offset=0, unit=None):
        """Create a number line."""
        if x_range is None:
            x_range = [-14, 14]
        if unit is None:
            unit = self.NL_UNIT
        nl = NumberLine(
            x_range=[x_range[0], x_range[1], 1],
            length=(x_range[1] - x_range[0]) * unit,
            include_numbers=True,
            include_tip=True,
            font_size=16,
            color=WHITE,
            decimal_number_config={"num_decimal_places": 0},
        )
        nl.move_to(self.NL_CENTER + DOWN * y_offset)
        return nl

    def _nl_pos(self, nl, value):
        """Get position on number line for a given value."""
        return nl.number_to_point(value)

    def _make_dot(self, nl, value, color=YELLOW, radius=0.12):
        """Create a dot at a specific value on the number line."""
        return Dot(self._nl_pos(nl, value), color=color, radius=radius)

    def _make_sign_box(self, sign_text, color, position):
        """Create a sign indicator box with + or - symbol."""
        box = RoundedRectangle(
            corner_radius=0.15,
            width=1.0,
            height=0.8,
            color=color,
            fill_color=color,
            fill_opacity=0.2,
            stroke_width=2,
        )
        label = MathTex(sign_text, font_size=36, color=color)
        group = VGroup(box, label).move_to(position)
        return group

    # ─────────────────────────────────────────
    # Scene 1: Opening hook
    # ─────────────────────────────────────────
    def scene_1_opening(self):
        # Author
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # Hook question
        hook = MathTex(
            r"(-3) \times (-4) = \, ?",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 4)

        hook_sub = Text(
            "负数乘负数, 结果是正还是负?",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A,
        ).move_to(UP * 2.5)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(hook_sub, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # Visual tease: two direction arrows
        arrow_left = Arrow(
            ORIGIN, LEFT * 2,
            color=self.COLOR_NEG,
            stroke_width=4,
            buff=0,
        ).move_to(DOWN * 0.5 + LEFT * 1.5)

        arrow_right = Arrow(
            ORIGIN, RIGHT * 2,
            color=self.COLOR_POS,
            stroke_width=4,
            buff=0,
        ).move_to(DOWN * 0.5 + RIGHT * 1.5)

        label_neg = Text(
            "负方向", font="PingFang SC", font_size=20, color=self.COLOR_NEG
        ).next_to(arrow_left, DOWN, buff=0.15)

        label_pos = Text(
            "正方向", font="PingFang SC", font_size=20, color=self.COLOR_POS
        ).next_to(arrow_right, DOWN, buff=0.15)

        self.play(
            GrowArrow(arrow_left), GrowArrow(arrow_right),
            FadeIn(label_neg), FadeIn(label_pos),
            run_time=0.6,
        )

        hint = Text(
            "方向的反转是关键!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(hook_sub),
            FadeOut(arrow_left), FadeOut(arrow_right),
            FadeOut(label_neg), FadeOut(label_pos),
            FadeOut(hint),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 2: Positive x Positive = Positive
    # ─────────────────────────────────────────
    def scene_2_pos_times_pos(self):
        title = Text(
            "正 x 正 = 正",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_POS,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Formula
        formula = MathTex(
            r"(+3) \times (+4) = \, ?",
            font_size=38,
            color=WHITE,
        ).move_to(UP * 4.2)
        self.play(Write(formula), run_time=0.5)

        # Explanation using repeated addition
        explain = Text(
            "3 个 (+4) 相加",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 3.2)
        self.play(FadeIn(explain), run_time=0.4)

        # Number line
        nl = self._make_number_line(x_range=[-2, 14])
        self.play(Create(nl), run_time=0.6)

        # Start at 0
        dot = self._make_dot(nl, 0, color=WHITE)
        self.play(FadeIn(dot, scale=0.5), run_time=0.3)

        # Three jumps of +4
        colors = [self.COLOR_POS, "#27ae60", "#1abc9c"]
        for i in range(3):
            start_val = i * 4
            end_val = (i + 1) * 4
            arrow = Arrow(
                self._nl_pos(nl, start_val) + UP * 0.3,
                self._nl_pos(nl, end_val) + UP * 0.3,
                color=colors[i],
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            jump_label = MathTex(
                r"+4", font_size=22, color=colors[i]
            ).next_to(arrow, UP, buff=0.05)

            self.play(GrowArrow(arrow), FadeIn(jump_label), run_time=0.5)

        # End dot
        end_dot = self._make_dot(nl, 12, color=self.COLOR_RESULT)
        result_label = MathTex(
            r"12", font_size=28, color=self.COLOR_RESULT
        ).next_to(end_dot, DOWN, buff=0.25)

        self.play(FadeIn(end_dot, scale=0.5), FadeIn(result_label), run_time=0.4)

        # Update formula
        formula_done = MathTex(
            r"(+3) \times (+4) = +12",
            font_size=38,
            color=self.COLOR_POS,
        ).move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)

        # Rule note
        rule = Text(
            "同号相乘, 结果为正!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 3: Positive x Negative = Negative
    # ─────────────────────────────────────────
    def scene_3_pos_times_neg(self):
        title = Text(
            "正 x 负 = 负",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_NEG,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Formula
        formula = MathTex(
            r"(+3) \times (-4) = \, ?",
            font_size=38,
            color=WHITE,
        ).move_to(UP * 4.2)
        self.play(Write(formula), run_time=0.5)

        # Explanation
        explain = Text(
            "3 个 (-4) 相加",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 3.2)
        self.play(FadeIn(explain), run_time=0.4)

        # Number line
        nl = self._make_number_line(x_range=[-14, 2])
        self.play(Create(nl), run_time=0.6)

        # Start at 0
        dot = self._make_dot(nl, 0, color=WHITE)
        self.play(FadeIn(dot, scale=0.5), run_time=0.3)

        # Three jumps of -4
        colors = [self.COLOR_NEG, "#c0392b", "#e74c3c"]
        for i in range(3):
            start_val = -i * 4
            end_val = -(i + 1) * 4
            arrow = Arrow(
                self._nl_pos(nl, start_val) + UP * 0.3,
                self._nl_pos(nl, end_val) + UP * 0.3,
                color=colors[i],
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            jump_label = MathTex(
                r"-4", font_size=22, color=colors[i]
            ).next_to(arrow, UP, buff=0.05)

            self.play(GrowArrow(arrow), FadeIn(jump_label), run_time=0.5)

        # End dot
        end_dot = self._make_dot(nl, -12, color=self.COLOR_RESULT)
        result_label = MathTex(
            r"-12", font_size=28, color=self.COLOR_RESULT
        ).next_to(end_dot, DOWN, buff=0.25)

        self.play(FadeIn(end_dot, scale=0.5), FadeIn(result_label), run_time=0.4)

        # Update formula
        formula_done = MathTex(
            r"(+3) \times (-4) = -12",
            font_size=38,
            color=self.COLOR_NEG,
        ).move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)

        # Rule note
        rule = Text(
            "异号相乘, 结果为负!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 4: Negative x Negative = Positive
    # ─────────────────────────────────────────
    def scene_4_neg_times_neg(self):
        title = Text(
            "负 x 负 = 正",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_POS,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Formula
        formula = MathTex(
            r"(-3) \times (-4) = \, ?",
            font_size=38,
            color=WHITE,
        ).move_to(UP * 4.2)
        self.play(Write(formula), run_time=0.5)

        # Key intuition: direction reversal
        explain_1 = Text(
            "负号 = 方向反转!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 3.0)

        self.play(FadeIn(explain_1), run_time=0.5)
        self.wait(0.5)

        # Visual: two reversals
        # Step 1: (-4) means going left
        step1_box = RoundedRectangle(
            corner_radius=0.2, width=7.5, height=1.6,
            color=self.COLOR_NEG, fill_color="#3a1a1a",
            fill_opacity=0.4, stroke_width=1,
        ).move_to(UP * 1.2)

        step1_text_1 = Text(
            "(-4) 的方向: 向左",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_NEG,
        ).move_to(UP * 1.6)

        step1_arrow = Arrow(
            RIGHT * 1.5, LEFT * 1.5,
            color=self.COLOR_NEG,
            stroke_width=3,
            buff=0,
        ).move_to(UP * 0.9)

        self.play(
            FadeIn(step1_box),
            FadeIn(step1_text_1),
            GrowArrow(step1_arrow),
            run_time=0.6,
        )
        self.wait(0.5)

        # Step 2: x(-3) means reverse direction 3 times
        step2_box = RoundedRectangle(
            corner_radius=0.2, width=7.5, height=1.6,
            color=self.COLOR_POS, fill_color="#1a3a1a",
            fill_opacity=0.4, stroke_width=1,
        ).move_to(DOWN * 0.8)

        step2_text_1 = Text(
            "x(-3): 反转方向, 走3次",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_POS,
        ).move_to(DOWN * 0.4)

        step2_arrow = Arrow(
            LEFT * 1.5, RIGHT * 1.5,
            color=self.COLOR_POS,
            stroke_width=3,
            buff=0,
        ).move_to(DOWN * 1.1)

        self.play(
            FadeIn(step2_box),
            FadeIn(step2_text_1),
            run_time=0.4,
        )

        # Animate the reversal
        reversed_arrow = step1_arrow.copy().set_color(self.COLOR_POS)
        self.play(
            Rotate(reversed_arrow, PI, about_point=reversed_arrow.get_center()),
            run_time=0.8,
        )
        self.play(
            FadeOut(reversed_arrow),
            GrowArrow(step2_arrow),
            run_time=0.4,
        )

        # Conclusion
        conclusion = Text(
            "反转再反转 = 回到正方向!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # Show on number line
        self.play(
            FadeOut(step1_box), FadeOut(step1_text_1), FadeOut(step1_arrow),
            FadeOut(step2_box), FadeOut(step2_text_1), FadeOut(step2_arrow),
            FadeOut(explain_1), FadeOut(conclusion),
            run_time=0.4,
        )

        # Number line demonstration
        nl = self._make_number_line(x_range=[-2, 14])
        self.play(Create(nl), run_time=0.6)

        dot = self._make_dot(nl, 0, color=WHITE)
        self.play(FadeIn(dot, scale=0.5), run_time=0.3)

        explain_nl = Text(
            "反转 (-4) 得 (+4), 走 3 次",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 2)

        self.play(FadeIn(explain_nl), run_time=0.4)

        # Three jumps of +4 (because -(-4) = +4)
        for i in range(3):
            start_val = i * 4
            end_val = (i + 1) * 4
            arrow = Arrow(
                self._nl_pos(nl, start_val) + UP * 0.3,
                self._nl_pos(nl, end_val) + UP * 0.3,
                color=self.COLOR_POS,
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            jump_label = MathTex(
                r"+4", font_size=22, color=self.COLOR_POS
            ).next_to(arrow, UP, buff=0.05)

            self.play(GrowArrow(arrow), FadeIn(jump_label), run_time=0.5)

        # End dot
        end_dot = self._make_dot(nl, 12, color=self.COLOR_RESULT)
        result_label = MathTex(
            r"+12", font_size=28, color=self.COLOR_RESULT
        ).next_to(end_dot, DOWN, buff=0.25)

        self.play(FadeIn(end_dot, scale=0.5), FadeIn(result_label), run_time=0.4)

        # Update formula
        formula_done = MathTex(
            r"(-3) \times (-4) = +12",
            font_size=38,
            color=self.COLOR_POS,
        ).move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)

        rule = Text(
            "负负得正!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4)

        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.5)
        self.play(
            Flash(rule.get_center(), color=self.COLOR_HIGHLIGHT, flash_radius=1.0),
            run_time=0.5,
        )
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 5: Multiplication sign rule summary
    # ─────────────────────────────────────────
    def scene_5_mul_rule_summary(self):
        title = Text(
            "乘法符号法则",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # ── Same sign ──
        same_title = Text(
            "同号得正",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_POS,
        ).move_to(UP * 4.2)

        self.play(Write(same_title), run_time=0.5)

        # Row 1: (+) x (+) = (+)
        row1_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=1.2,
            color=self.COLOR_POS, fill_color="#1a3a2a",
            fill_opacity=0.4, stroke_width=1,
        ).move_to(UP * 3.0)

        row1 = MathTex(
            r"(+) \times (+) = (+)",
            font_size=34, color=self.COLOR_POS,
        ).move_to(UP * 3.0)

        self.play(FadeIn(row1_box), Write(row1), run_time=0.5)

        # Row 2: (-) x (-) = (+)
        row2_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=1.2,
            color=self.COLOR_POS, fill_color="#1a3a2a",
            fill_opacity=0.4, stroke_width=1,
        ).move_to(UP * 1.6)

        row2 = MathTex(
            r"(-) \times (-) = (+)",
            font_size=34, color=self.COLOR_POS,
        ).move_to(UP * 1.6)

        self.play(FadeIn(row2_box), Write(row2), run_time=0.5)
        self.wait(0.5)

        # ── Different sign ──
        diff_title = Text(
            "异号得负",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_NEG,
        ).move_to(UP * 0.2)

        self.play(Write(diff_title), run_time=0.5)

        # Row 3: (+) x (-) = (-)
        row3_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=1.2,
            color=self.COLOR_NEG, fill_color="#3a1a1a",
            fill_opacity=0.4, stroke_width=1,
        ).move_to(DOWN * 1.0)

        row3 = MathTex(
            r"(+) \times (-) = (-)",
            font_size=34, color=self.COLOR_NEG,
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(row3_box), Write(row3), run_time=0.5)

        # Row 4: (-) x (+) = (-)
        row4_box = RoundedRectangle(
            corner_radius=0.15, width=7.5, height=1.2,
            color=self.COLOR_NEG, fill_color="#3a1a1a",
            fill_opacity=0.4, stroke_width=1,
        ).move_to(DOWN * 2.4)

        row4 = MathTex(
            r"(-) \times (+) = (-)",
            font_size=34, color=self.COLOR_NEG,
        ).move_to(DOWN * 2.4)

        self.play(FadeIn(row4_box), Write(row4), run_time=0.5)
        self.wait(0.5)

        # Memory tip
        tip_box = RoundedRectangle(
            corner_radius=0.25, width=7.5, height=1.6,
            color=self.COLOR_HIGHLIGHT, fill_color="#3a3a1a",
            fill_opacity=0.5, stroke_width=2,
        ).move_to(DOWN * 4.5)

        tip = Text(
            "口诀: 同号得正, 异号得负",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.2)

        tip2 = Text(
            "先定符号, 再算绝对值!",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 4.9)

        self.play(
            FadeIn(tip_box), FadeIn(tip), FadeIn(tip2),
            run_time=0.6,
        )
        self.play(
            Flash(tip_box.get_center(), color=self.COLOR_HIGHLIGHT, flash_radius=1.2),
            run_time=0.5,
        )
        self.wait(2.0)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 6: Division sign rule
    # ─────────────────────────────────────────
    def scene_6_division_rule(self):
        title = Text(
            "除法符号法则",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Key insight
        key = Text(
            "除法符号法则与乘法相同!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 4.2)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)

        # Same sign examples
        same_label = Text(
            "同号得正:",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_POS,
        ).move_to(UP * 3.0 + LEFT * 2.5)

        ex1 = MathTex(
            r"(+6) \div (+2) = +3",
            font_size=32, color=self.COLOR_POS,
        ).move_to(UP * 2.2)

        ex2 = MathTex(
            r"(-6) \div (-2) = +3",
            font_size=32, color=self.COLOR_POS,
        ).move_to(UP * 1.4)

        self.play(FadeIn(same_label), run_time=0.3)
        self.play(Write(ex1), run_time=0.5)
        self.wait(0.3)
        self.play(Write(ex2), run_time=0.5)
        self.wait(0.5)

        # Different sign examples
        diff_label = Text(
            "异号得负:",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_NEG,
        ).move_to(DOWN * 0.0 + LEFT * 2.5)

        ex3 = MathTex(
            r"(+6) \div (-2) = -3",
            font_size=32, color=self.COLOR_NEG,
        ).move_to(DOWN * 0.8)

        ex4 = MathTex(
            r"(-6) \div (+2) = -3",
            font_size=32, color=self.COLOR_NEG,
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(diff_label), run_time=0.3)
        self.play(Write(ex3), run_time=0.5)
        self.wait(0.3)
        self.play(Write(ex4), run_time=0.5)
        self.wait(0.5)

        # Verification with multiplication
        verify_box = RoundedRectangle(
            corner_radius=0.2, width=7.5, height=2.0,
            color=GRAY_B, fill_color="#2a2a4a",
            fill_opacity=0.5, stroke_width=1,
        ).move_to(DOWN * 3.5)

        verify_title = Text(
            "验证: 乘法与除法互逆",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 2.8)

        verify_eq = MathTex(
            r"(-6) \div (-2) = +3",
            font_size=30, color=WHITE,
        ).move_to(DOWN * 3.5)

        verify_check_label = Text(
            "检验: ", font="PingFang SC", font_size=20, color=GRAY_A
        ).move_to(DOWN * 4.2 + LEFT * 2)

        verify_check = MathTex(
            r"(+3) \times (-2) = -6 \checkmark",
            font_size=28, color=self.COLOR_POS,
        ).next_to(verify_check_label, RIGHT, buff=0.2)

        self.play(FadeIn(verify_box), FadeIn(verify_title), run_time=0.4)
        self.play(Write(verify_eq), run_time=0.5)
        self.play(FadeIn(verify_check_label), Write(verify_check), run_time=0.6)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 7: Zero rule
    # ─────────────────────────────────────────
    def scene_7_zero_rule(self):
        title = Text(
            "零的特殊性",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Rule box
        rule_box = RoundedRectangle(
            corner_radius=0.25, width=7.5, height=2.8,
            color=self.COLOR_HIGHLIGHT, fill_color="#3a3a1a",
            fill_opacity=0.4, stroke_width=2,
        ).move_to(UP * 3.0)

        rule_1 = Text(
            "0 乘以任何数都得 0",
            font="PingFang SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 3.6)

        rule_1_formula = MathTex(
            r"0 \times a = 0",
            font_size=36, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 2.8)

        rule_2 = Text(
            "0 不能作为除数!",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_NEG,
        ).move_to(UP * 2.0)

        self.play(FadeIn(rule_box), run_time=0.3)
        self.play(FadeIn(rule_1), Write(rule_1_formula), run_time=0.6)
        self.play(FadeIn(rule_2), run_time=0.4)
        self.wait(0.5)

        # Examples
        ex1 = MathTex(
            r"0 \times (-5) = 0",
            font_size=32, color=GRAY_A,
        ).move_to(UP * 0.5)

        ex2 = MathTex(
            r"0 \times 100 = 0",
            font_size=32, color=GRAY_A,
        ).move_to(DOWN * 0.3)

        ex3 = MathTex(
            r"0 \div (-3) = 0",
            font_size=32, color=GRAY_A,
        ).move_to(DOWN * 1.1)

        ex4_label = Text(
            "但: ", font="PingFang SC", font_size=22, color=self.COLOR_NEG
        ).move_to(DOWN * 2.1 + LEFT * 2.5)

        ex4 = MathTex(
            r"5 \div 0",
            font_size=32, color=self.COLOR_NEG,
        ).next_to(ex4_label, RIGHT, buff=0.2)

        ex4_note = Text(
            "无意义!",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_NEG,
        ).next_to(ex4, RIGHT, buff=0.3)

        self.play(Write(ex1), run_time=0.4)
        self.play(Write(ex2), run_time=0.4)
        self.play(Write(ex3), run_time=0.4)
        self.wait(0.3)
        self.play(
            FadeIn(ex4_label), Write(ex4), FadeIn(ex4_note),
            run_time=0.5,
        )

        # Cross mark on ex4
        cross = VGroup(
            Line(
                ex4.get_corner(DL) + LEFT * 0.1 + DOWN * 0.1,
                ex4.get_corner(UR) + RIGHT * 0.1 + UP * 0.1,
                color=self.COLOR_NEG, stroke_width=3,
            ),
            Line(
                ex4.get_corner(UL) + LEFT * 0.1 + UP * 0.1,
                ex4.get_corner(DR) + RIGHT * 0.1 + DOWN * 0.1,
                color=self.COLOR_NEG, stroke_width=3,
            ),
        )
        self.play(Create(cross), run_time=0.4)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 8: Practice problems
    # ─────────────────────────────────────────
    def scene_8_practice(self):
        title = Text(
            "练一练",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Problem setup
        problems = [
            (r"(-5) \times (+3) = \, ?", r"(-5) \times (+3) = -15", "异号得负", self.COLOR_NEG),
            (r"(-7) \times (-2) = \, ?", r"(-7) \times (-2) = +14", "同号得正", self.COLOR_POS),
            (r"(+8) \div (-4) = \, ?", r"(+8) \div (-4) = -2", "异号得负", self.COLOR_NEG),
            (r"(-12) \div (-3) = \, ?", r"(-12) \div (-3) = +4", "同号得正", self.COLOR_POS),
        ]

        y_positions = [UP * 3.5, UP * 1.5, DOWN * 0.5, DOWN * 2.5]

        for i, (q, a, rule, color) in enumerate(problems):
            # Problem number
            num_label = Text(
                f"({i+1})",
                font="PingFang SC",
                font_size=22,
                color=GRAY_B,
            ).move_to(y_positions[i] + LEFT * 3.8)

            # Question
            question = MathTex(
                q, font_size=32, color=WHITE,
            ).next_to(num_label, RIGHT, buff=0.3)

            self.play(FadeIn(num_label), Write(question), run_time=0.5)
            self.wait(0.8)

            # Answer
            answer = MathTex(
                a, font_size=32, color=color,
            ).move_to(question.get_center())

            # Rule tag
            rule_tag = Text(
                rule,
                font="PingFang SC",
                font_size=18,
                color=color,
            ).next_to(answer, RIGHT, buff=0.4)

            self.play(
                Transform(question, answer),
                FadeIn(rule_tag, shift=LEFT * 0.2),
                run_time=0.6,
            )
            self.wait(0.5)

        # Encouragement
        encourage = Text(
            "全对了吗? 记住口诀就简单!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 5)

        self.play(FadeIn(encourage, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 9: Outro
    # ─────────────────────────────────────────
    def scene_9_outro(self):
        # Final summary card
        summary_box = RoundedRectangle(
            corner_radius=0.3, width=7.5, height=4.0,
            color=self.COLOR_FORMULA, fill_color="#1e2a4a",
            fill_opacity=0.6, stroke_width=2,
        ).move_to(UP * 2.0)

        summary_title = Text(
            "负数乘除法核心法则",
            font="PingFang SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 3.5)

        rule1 = Text(
            "同号得正, 异号得负",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 2.5)

        rule2 = MathTex(
            r"0 \times a = 0",
            font_size=32, color=GRAY_A,
        ).move_to(UP * 1.5)

        rule3 = Text(
            "先定符号, 再算绝对值",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 0.7)

        self.play(
            FadeIn(summary_box),
            Write(summary_title),
            run_time=0.5,
        )
        self.play(FadeIn(rule1), run_time=0.4)
        self.play(Write(rule2), run_time=0.4)
        self.play(FadeIn(rule3), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(summary_box), FadeOut(summary_title),
            FadeOut(rule1), FadeOut(rule2), FadeOut(rule3),
            run_time=0.5,
        )

        # Author info
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            self.author.animate.move_to(UP * 1.5).set_opacity(0),
            run_time=0.3,
        )
        self.play(FadeIn(author_name, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(author_name),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(self.author),
            run_time=0.8,
        )

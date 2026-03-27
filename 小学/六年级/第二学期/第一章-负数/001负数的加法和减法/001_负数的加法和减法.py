"""
负数的加法和减法 - Negative Number Addition and Subtraction
使用 Manim 创建的小学六年级数学教学视频

内容: 理解负数加法和减法的算理，通过数轴直观演示
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


class NegativeAddSubLesson(Scene):
    """
    负数的加法和减法教学动画

    场景顺序:
    1. 开场钩子 - 引出问题
    2. 数轴回顾 - 建立基础
    3. 加正数 - 5 + 3 = 8 (向右移动)
    4. 加负数 - 5 + (-3) = 2 (向左移动)
    5. 规则总结1 - a + (-b) = a - b
    6. 减正数 - 5 - 3 = 2 (向左移动)
    7. 减负数 - 5 - (-3) = 8 (向右移动)
    8. 规则总结2 - a - (-b) = a + b
    9. 总结对比
    10. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色方案
        self.COLOR_POS = "#2ecc71"       # 正方向 - 绿色
        self.COLOR_NEG = "#e74c3c"       # 负方向 - 红色
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_FORMULA = "#3498db"   # 公式蓝
        self.COLOR_RESULT = "#f39c12"    # 结果橙
        self.COLOR_NUMBER_LINE = WHITE

        # 数轴参数
        self.NL_CENTER = UP * 1.5
        self.NL_RANGE = [-6, 10]
        self.NL_UNIT = 0.55

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_number_line_review()
        self.scene_3_add_positive()
        self.scene_4_add_negative()
        self.scene_5_rule_summary_1()
        self.scene_6_sub_positive()
        self.scene_7_sub_negative()
        self.scene_8_rule_summary_2()
        self.scene_9_full_summary()
        self.scene_10_outro()

    # ─────────────────────────────────────────
    # Helper: create a number line
    # ─────────────────────────────────────────
    def _make_number_line(self, y_offset=0):
        """Create a number line centered at given y_offset."""
        nl = NumberLine(
            x_range=[self.NL_RANGE[0], self.NL_RANGE[1], 1],
            length=(self.NL_RANGE[1] - self.NL_RANGE[0]) * self.NL_UNIT,
            include_numbers=True,
            include_tip=True,
            font_size=18,
            color=self.COLOR_NUMBER_LINE,
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

    def _make_curved_arrow(self, nl, start_val, end_val, color, label_text=None):
        """
        Create a curved arrow above the number line showing movement.
        Returns (arrow, label) as VGroup.
        """
        start = self._nl_pos(nl, start_val)
        end = self._nl_pos(nl, end_val)

        # Determine arc direction
        direction = 1 if end_val > start_val else -1
        arc_height = 0.6 + 0.05 * abs(end_val - start_val)

        mid = (start + end) / 2 + UP * arc_height

        # Use CurvedArrow
        arrow = CurvedArrow(
            start_point=start + UP * 0.2,
            end_point=end + UP * 0.2,
            angle=direction * TAU / 4 * 0.4,
            color=color,
            stroke_width=3,
            tip_length=0.2,
        )

        result = VGroup(arrow)

        if label_text:
            label = Text(
                label_text, font="Noto Sans CJK SC", font_size=18, color=color
            )
            label.next_to(arrow, UP, buff=0.1)
            result.add(label)

        return result

    # ─────────────────────────────────────────
    # Scene 1: Opening hook
    # ─────────────────────────────────────────
    def scene_1_opening(self):
        # Author
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # Hook question
        hook = Text(
            "5 - (-3) = ?",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 3)

        hook_sub = Text(
            "减去一个负数会怎样?",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_A,
        ).move_to(UP * 1.5)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(hook_sub, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # Quick number line tease
        nl_preview = self._make_number_line(y_offset=2)
        dot_preview = self._make_dot(nl_preview, 5, color=self.COLOR_HIGHLIGHT)

        self.play(Create(nl_preview), run_time=0.8)
        self.play(FadeIn(dot_preview, scale=0.5), run_time=0.4)
        self.wait(0.5)

        self.play(
            FadeOut(hook),
            FadeOut(hook_sub),
            FadeOut(nl_preview),
            FadeOut(dot_preview),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 2: Number line review
    # ─────────────────────────────────────────
    def scene_2_number_line_review(self):
        title = Text(
            "数轴回顾",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FORMULA,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)

        nl = self._make_number_line()
        self.play(Create(nl), run_time=1.0)

        # Mark origin
        origin_dot = self._make_dot(nl, 0, color=WHITE)
        origin_label = Text(
            "原点", font="Noto Sans CJK SC", font_size=20, color=WHITE
        ).next_to(origin_dot, DOWN, buff=0.3)

        self.play(FadeIn(origin_dot), FadeIn(origin_label), run_time=0.5)

        # Positive direction
        pos_arrow = Arrow(
            self._nl_pos(nl, 1) + UP * 0.8,
            self._nl_pos(nl, 4) + UP * 0.8,
            color=self.COLOR_POS,
            stroke_width=3,
            buff=0,
        )
        pos_label = Text(
            "正方向 (向右)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_POS,
        ).next_to(pos_arrow, UP, buff=0.1)

        self.play(GrowArrow(pos_arrow), FadeIn(pos_label), run_time=0.6)

        # Negative direction
        neg_arrow = Arrow(
            self._nl_pos(nl, -1) + UP * 0.8,
            self._nl_pos(nl, -4) + UP * 0.8,
            color=self.COLOR_NEG,
            stroke_width=3,
            buff=0,
        )
        neg_label = Text(
            "负方向 (向左)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_NEG,
        ).next_to(neg_arrow, UP, buff=0.1)

        self.play(GrowArrow(neg_arrow), FadeIn(neg_label), run_time=0.6)

        # Key concept
        key_text = Text(
            "加法 = 在数轴上移动!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3)

        self.play(FadeIn(key_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(nl),
            FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(pos_arrow),
            FadeOut(pos_label),
            FadeOut(neg_arrow),
            FadeOut(neg_label),
            FadeOut(key_text),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 3: Add positive: 5 + 3 = 8
    # ─────────────────────────────────────────
    def scene_3_add_positive(self):
        title = Text(
            "加正数: 向右移动",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_POS,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Formula
        formula = MathTex(r"5 + 3 = \, ?", font_size=40, color=WHITE).move_to(
            UP * 4.2
        )
        self.play(Write(formula), run_time=0.5)

        # Number line
        nl = self._make_number_line()
        self.play(Create(nl), run_time=0.6)

        # Start at 5
        dot = self._make_dot(nl, 5, color=self.COLOR_HIGHLIGHT)
        start_label = MathTex(r"5", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(
            dot, DOWN, buff=0.3
        )
        self.play(FadeIn(dot, scale=0.5), FadeIn(start_label), run_time=0.5)
        self.wait(0.3)

        # Move right by 3
        move_text = Text(
            "+3 : 向右移动3格",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_POS,
        ).move_to(DOWN * 2)

        self.play(FadeIn(move_text), run_time=0.4)

        # Animate step by step
        for i in range(3):
            step_arrow = Arrow(
                self._nl_pos(nl, 5 + i) + UP * 0.25,
                self._nl_pos(nl, 5 + i + 1) + UP * 0.25,
                color=self.COLOR_POS,
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            self.play(GrowArrow(step_arrow), run_time=0.3)

        # Move dot
        end_dot = self._make_dot(nl, 8, color=self.COLOR_RESULT)
        self.play(
            FadeIn(end_dot, scale=0.5),
            run_time=0.4,
        )

        # Result
        result_label = MathTex(r"8", font_size=28, color=self.COLOR_RESULT).next_to(
            end_dot, DOWN, buff=0.3
        )
        self.play(FadeIn(result_label), run_time=0.3)

        # Update formula
        formula_done = MathTex(r"5 + 3 = 8", font_size=40, color=self.COLOR_POS)
        formula_done.move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)
        self.wait(1.0)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 4: Add negative: 5 + (-3) = 2
    # ─────────────────────────────────────────
    def scene_4_add_negative(self):
        title = Text(
            "加负数: 向左移动",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_NEG,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        formula = MathTex(r"5 + (-3) = \, ?", font_size=40, color=WHITE).move_to(
            UP * 4.2
        )
        self.play(Write(formula), run_time=0.5)

        nl = self._make_number_line()
        self.play(Create(nl), run_time=0.6)

        # Start at 5
        dot = self._make_dot(nl, 5, color=self.COLOR_HIGHLIGHT)
        start_label = MathTex(r"5", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(
            dot, DOWN, buff=0.3
        )
        self.play(FadeIn(dot, scale=0.5), FadeIn(start_label), run_time=0.5)
        self.wait(0.3)

        # Explanation
        explain = Text(
            "+(-3) : 加负数 = 向左移动3格",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_NEG,
        ).move_to(DOWN * 2)

        self.play(FadeIn(explain), run_time=0.4)

        # Animate step by step (left)
        step_arrows = VGroup()
        for i in range(3):
            step_arrow = Arrow(
                self._nl_pos(nl, 5 - i) + UP * 0.25,
                self._nl_pos(nl, 5 - i - 1) + UP * 0.25,
                color=self.COLOR_NEG,
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            step_arrows.add(step_arrow)
            self.play(GrowArrow(step_arrow), run_time=0.3)

        # End dot
        end_dot = self._make_dot(nl, 2, color=self.COLOR_RESULT)
        self.play(FadeIn(end_dot, scale=0.5), run_time=0.4)

        result_label = MathTex(r"2", font_size=28, color=self.COLOR_RESULT).next_to(
            end_dot, DOWN, buff=0.3
        )
        self.play(FadeIn(result_label), run_time=0.3)

        # Update formula
        formula_done = MathTex(r"5 + (-3) = 2", font_size=40, color=self.COLOR_NEG)
        formula_done.move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)

        # Key insight
        insight = Text(
            "加上一个负数 = 减去它的绝对值",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4)

        self.play(FadeIn(insight, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 5: Rule summary 1
    # ─────────────────────────────────────────
    def scene_5_rule_summary_1(self):
        title = Text(
            "规则一",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Rule box
        rule_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.5,
            color=self.COLOR_FORMULA,
            fill_color="#1e3a5f",
            fill_opacity=0.5,
            stroke_width=2,
        ).move_to(UP * 2.5)

        rule_formula = MathTex(
            r"a + (-b) = a - b", font_size=44, color=WHITE
        ).move_to(UP * 3.0)

        rule_text = Text(
            "加上一个负数，等于减去这个数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 2.0)

        self.play(FadeIn(rule_box), run_time=0.3)
        self.play(Write(rule_formula), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.4)

        # Examples
        ex1_label = Text(
            "例1:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(UP * 0.5 + LEFT * 2.5)

        ex1 = MathTex(
            r"5 + (-3) = 5 - 3 = 2", font_size=32, color=self.COLOR_POS
        ).next_to(ex1_label, RIGHT, buff=0.3)

        ex2_label = Text(
            "例2:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(DOWN * 0.5 + LEFT * 2.5)

        ex2 = MathTex(
            r"8 + (-5) = 8 - 5 = 3", font_size=32, color=self.COLOR_POS
        ).next_to(ex2_label, RIGHT, buff=0.3)

        ex3_label = Text(
            "例3:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(DOWN * 1.5 + LEFT * 2.5)

        ex3 = MathTex(
            r"(-2) + (-4) = -2 - 4 = -6", font_size=32, color=self.COLOR_POS
        ).next_to(ex3_label, RIGHT, buff=0.3)

        self.play(FadeIn(ex1_label), Write(ex1), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(ex2_label), Write(ex2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(ex3_label), Write(ex3), run_time=0.6)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 6: Subtract positive: 5 - 3 = 2
    # ─────────────────────────────────────────
    def scene_6_sub_positive(self):
        title = Text(
            "减正数: 向左移动",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_NEG,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        formula = MathTex(r"5 - 3 = \, ?", font_size=40, color=WHITE).move_to(
            UP * 4.2
        )
        self.play(Write(formula), run_time=0.5)

        nl = self._make_number_line()
        self.play(Create(nl), run_time=0.6)

        # Start at 5
        dot = self._make_dot(nl, 5, color=self.COLOR_HIGHLIGHT)
        start_label = MathTex(r"5", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(
            dot, DOWN, buff=0.3
        )
        self.play(FadeIn(dot, scale=0.5), FadeIn(start_label), run_time=0.5)

        explain = Text(
            "-3 : 减去正数 = 向左移动3格",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_NEG,
        ).move_to(DOWN * 2)

        self.play(FadeIn(explain), run_time=0.4)

        # Step arrows left
        for i in range(3):
            step_arrow = Arrow(
                self._nl_pos(nl, 5 - i) + UP * 0.25,
                self._nl_pos(nl, 5 - i - 1) + UP * 0.25,
                color=self.COLOR_NEG,
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            self.play(GrowArrow(step_arrow), run_time=0.3)

        end_dot = self._make_dot(nl, 2, color=self.COLOR_RESULT)
        self.play(FadeIn(end_dot, scale=0.5), run_time=0.4)

        result_label = MathTex(r"2", font_size=28, color=self.COLOR_RESULT).next_to(
            end_dot, DOWN, buff=0.3
        )
        self.play(FadeIn(result_label), run_time=0.3)

        formula_done = MathTex(r"5 - 3 = 2", font_size=40, color=self.COLOR_NEG)
        formula_done.move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)

        # Comparison note
        compare = Text(
            "和 5+(-3) 结果一样!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4)

        self.play(FadeIn(compare, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 7: Subtract negative: 5 - (-3) = 8
    # ─────────────────────────────────────────
    def scene_7_sub_negative(self):
        title = Text(
            "减负数: 向右移动!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_POS,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        formula = MathTex(r"5 - (-3) = \, ?", font_size=40, color=WHITE).move_to(
            UP * 4.2
        )
        self.play(Write(formula), run_time=0.5)

        nl = self._make_number_line()
        self.play(Create(nl), run_time=0.6)

        # Start at 5
        dot = self._make_dot(nl, 5, color=self.COLOR_HIGHLIGHT)
        start_label = MathTex(r"5", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(
            dot, DOWN, buff=0.3
        )
        self.play(FadeIn(dot, scale=0.5), FadeIn(start_label), run_time=0.5)

        # Key explanation
        explain_1 = Text(
            "减去(-3)  =  加上(+3)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.5)

        explain_2 = Text(
            "减去负数 = 加上它的相反数!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 2.2)

        self.play(FadeIn(explain_1), run_time=0.5)
        self.play(FadeIn(explain_2), run_time=0.4)
        self.wait(0.8)

        # Transformation visual: -(-3) -> +3
        transform_left = MathTex(
            r"5 - (-3)", font_size=36, color=WHITE
        ).move_to(DOWN * 3.5 + LEFT * 1.5)

        transform_arrow = MathTex(
            r"\Rightarrow", font_size=36, color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)

        transform_right = MathTex(
            r"5 + 3", font_size=36, color=self.COLOR_POS
        ).move_to(DOWN * 3.5 + RIGHT * 1.5)

        self.play(Write(transform_left), run_time=0.4)
        self.play(Write(transform_arrow), run_time=0.3)
        self.play(Write(transform_right), run_time=0.4)
        self.wait(0.5)

        # Move right by 3
        for i in range(3):
            step_arrow = Arrow(
                self._nl_pos(nl, 5 + i) + UP * 0.25,
                self._nl_pos(nl, 5 + i + 1) + UP * 0.25,
                color=self.COLOR_POS,
                stroke_width=3,
                buff=0,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.5,
            )
            self.play(GrowArrow(step_arrow), run_time=0.3)

        end_dot = self._make_dot(nl, 8, color=self.COLOR_RESULT)
        self.play(FadeIn(end_dot, scale=0.5), run_time=0.4)

        result_label = MathTex(r"8", font_size=28, color=self.COLOR_RESULT).next_to(
            end_dot, DOWN, buff=0.3
        )
        self.play(FadeIn(result_label), run_time=0.3)

        formula_done = MathTex(r"5 - (-3) = 8", font_size=40, color=self.COLOR_POS)
        formula_done.move_to(UP * 4.2)
        self.play(Transform(formula, formula_done), run_time=0.5)

        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 8: Rule summary 2
    # ─────────────────────────────────────────
    def scene_8_rule_summary_2(self):
        title = Text(
            "规则二",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Rule box
        rule_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.5,
            color=self.COLOR_NEG,
            fill_color="#5a1e1e",
            fill_opacity=0.5,
            stroke_width=2,
        ).move_to(UP * 2.5)

        rule_formula = MathTex(
            r"a - (-b) = a + b", font_size=44, color=WHITE
        ).move_to(UP * 3.0)

        rule_text = Text(
            "减去一个负数，等于加上这个数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 2.0)

        self.play(FadeIn(rule_box), run_time=0.3)
        self.play(Write(rule_formula), run_time=0.8)
        self.play(FadeIn(rule_text), run_time=0.4)

        # Examples
        ex1_label = Text(
            "例1:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(UP * 0.5 + LEFT * 2.5)

        ex1 = MathTex(
            r"5 - (-3) = 5 + 3 = 8", font_size=32, color=self.COLOR_POS
        ).next_to(ex1_label, RIGHT, buff=0.3)

        ex2_label = Text(
            "例2:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(DOWN * 0.5 + LEFT * 2.5)

        ex2 = MathTex(
            r"3 - (-7) = 3 + 7 = 10", font_size=32, color=self.COLOR_POS
        ).next_to(ex2_label, RIGHT, buff=0.3)

        ex3_label = Text(
            "例3:", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(DOWN * 1.5 + LEFT * 2.5)

        ex3 = MathTex(
            r"(-4) - (-6) = -4 + 6 = 2", font_size=32, color=self.COLOR_POS
        ).next_to(ex3_label, RIGHT, buff=0.3)

        self.play(FadeIn(ex1_label), Write(ex1), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(ex2_label), Write(ex2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(ex3_label), Write(ex3), run_time=0.6)
        self.wait(1.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 9: Full summary with comparison
    # ─────────────────────────────────────────
    def scene_9_full_summary(self):
        title = Text(
            "总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # Summary table header
        header_bg = RoundedRectangle(
            corner_radius=0.2,
            width=7.8,
            height=1.0,
            color=GRAY_B,
            fill_color="#2a2a4a",
            fill_opacity=0.8,
            stroke_width=1,
        ).move_to(UP * 4.0)

        header_text = Text(
            "负数加减法口诀",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 4.0)

        self.play(FadeIn(header_bg), Write(header_text), run_time=0.5)

        # Row 1: add positive
        row1_box = RoundedRectangle(
            corner_radius=0.15,
            width=7.8,
            height=1.4,
            color=self.COLOR_POS,
            fill_color="#1a3a2a",
            fill_opacity=0.4,
            stroke_width=1,
        ).move_to(UP * 2.5)

        row1_formula = MathTex(
            r"a + b", font_size=32, color=self.COLOR_POS
        ).move_to(UP * 2.8 + LEFT * 2)

        row1_arrow = Text(
            "-->", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(UP * 2.8)

        row1_desc = Text(
            "向右移动",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_POS,
        ).move_to(UP * 2.8 + RIGHT * 2)

        row1_note = Text(
            "b > 0",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B,
        ).move_to(UP * 2.2)

        self.play(
            FadeIn(row1_box),
            Write(row1_formula),
            FadeIn(row1_arrow),
            FadeIn(row1_desc),
            FadeIn(row1_note),
            run_time=0.6,
        )

        # Row 2: add negative
        row2_box = RoundedRectangle(
            corner_radius=0.15,
            width=7.8,
            height=1.4,
            color=self.COLOR_NEG,
            fill_color="#3a1a1a",
            fill_opacity=0.4,
            stroke_width=1,
        ).move_to(UP * 0.9)

        row2_formula = MathTex(
            r"a + (-b) = a - b", font_size=32, color=self.COLOR_NEG
        ).move_to(UP * 1.2 + LEFT * 0.8)

        row2_desc = Text(
            "向左移动",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_NEG,
        ).move_to(UP * 1.2 + RIGHT * 2.5)

        row2_note = Text(
            "加负数 = 减正数",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(
            FadeIn(row2_box),
            Write(row2_formula),
            FadeIn(row2_desc),
            FadeIn(row2_note),
            run_time=0.6,
        )
        self.wait(0.3)

        # Row 3: subtract positive
        row3_box = RoundedRectangle(
            corner_radius=0.15,
            width=7.8,
            height=1.4,
            color=self.COLOR_NEG,
            fill_color="#3a1a1a",
            fill_opacity=0.4,
            stroke_width=1,
        ).move_to(DOWN * 0.7)

        row3_formula = MathTex(
            r"a - b", font_size=32, color=self.COLOR_NEG
        ).move_to(DOWN * 0.4 + LEFT * 2)

        row3_arrow = Text(
            "-->", font="Noto Sans CJK SC", font_size=22, color=GRAY_A
        ).move_to(DOWN * 0.4)

        row3_desc = Text(
            "向左移动",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_NEG,
        ).move_to(DOWN * 0.4 + RIGHT * 2)

        row3_note = Text(
            "b > 0",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B,
        ).move_to(DOWN * 1.0)

        self.play(
            FadeIn(row3_box),
            Write(row3_formula),
            FadeIn(row3_arrow),
            FadeIn(row3_desc),
            FadeIn(row3_note),
            run_time=0.6,
        )

        # Row 4: subtract negative - HIGHLIGHT
        row4_box = RoundedRectangle(
            corner_radius=0.15,
            width=7.8,
            height=1.4,
            color=self.COLOR_HIGHLIGHT,
            fill_color="#3a3a1a",
            fill_opacity=0.5,
            stroke_width=2,
        ).move_to(DOWN * 2.3)

        row4_formula = MathTex(
            r"a - (-b) = a + b", font_size=32, color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.0 + LEFT * 0.8)

        row4_desc = Text(
            "向右移动",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_POS,
        ).move_to(DOWN * 2.0 + RIGHT * 2.5)

        row4_note = Text(
            "减负数 = 加正数 (核心!)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.6)

        self.play(
            FadeIn(row4_box),
            Write(row4_formula),
            FadeIn(row4_desc),
            FadeIn(row4_note),
            run_time=0.6,
        )

        # Flash the key row
        self.play(
            Flash(row4_box.get_center(), color=self.COLOR_HIGHLIGHT, flash_radius=1.5),
            run_time=0.6,
        )

        # Memory tip
        tip = Text(
            "口诀: 负负得正, 加减互换!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(tip, shift=UP * 0.3), run_time=0.5)
        self.wait(2.5)

        self.play(
            *[FadeOut(m) for m in self.mobjects if m != self.author],
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # Scene 10: Outro
    # ─────────────────────────────────────────
    def scene_10_outro(self):
        # Author info
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
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
            font="Noto Sans CJK SC",
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

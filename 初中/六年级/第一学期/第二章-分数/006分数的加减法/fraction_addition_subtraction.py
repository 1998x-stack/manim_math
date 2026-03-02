"""
分数加减法教学动画 - Fraction Addition and Subtraction Animation
使用 Manim 创建的六年级数学教学视频

内容: 同分母/异分母分数加减法，通分，化简
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

修复说明:
  Sector 以坐标原点为弧心创建。
  .move_to() 移动的是包围盒中心（≠ 弧心），导致扇形与圆错位。
  修复方案：统一改为 .shift(center)，确保弧心精确对齐圆心。
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FractionAdditionSubtraction(Scene):
    """
    分数加减法教学动画场景

    场景顺序:
    1. 开场钩子 (0-5s)
    2. 同分母加法 - 直观演示 (5-18s)
    3. 同分母减法 - 快速演示 (18-28s)
    4. 异分母问题提出 (28-35s)
    5. 通分过程 (35-48s)
    6. 异分母减法示例 (48-58s)
    7. 总结和片尾 (58-75s)
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#3498db"
        self.COLOR_SECONDARY = "#e74c3c"
        self.COLOR_RESULT = "#2ecc71"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_DENOMINATOR = "#9b59b6"
        self.COLOR_NUMERATOR = "#f39c12"

        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_same_denominator_addition()
        self.scene_3_same_denominator_subtraction()
        self.scene_4_different_denominator_problem()
        self.scene_5_common_denominator_process()
        self.scene_6_different_denominator_subtraction()
        self.scene_7_summary_outro()

    def setup_geometry(self):
        """初始化所有几何元素的位置和参数"""
        self.circle_left_pos = np.array([-2.5, 2, 0])
        self.circle_right_pos = np.array([2.5, 2, 0])
        self.circle_result_pos = np.array([0, -1, 0])
        self.circle_radius = 1.2

        self.angle_quarter = PI / 2
        self.angle_half = PI
        self.angle_third = 2 * PI / 3
        self.angle_sixth = PI / 3
        self.angle_two_thirds = 4 * PI / 3

        self.rect_y = 2
        self.block_width = 0.6
        self.block_height = 1.5
        self.block_spacing = 0.1
        self.block_positions_5 = [-1.4, -0.7, 0, 0.7, 1.4]
        self.block_positions_6 = [-1.75, -1.05, -0.35, 0.35, 1.05, 1.75]

        print("✓ 几何初始化完成")

    # ------------------------------------------------------------------ #
    #  辅助方法：创建对齐圆心的扇形                                         #
    # ------------------------------------------------------------------ #
    def make_sector(self, center, radius, angle, start_angle,
                    color, fill_opacity=0.7):
        """
        创建一个以 center 为弧心的扇形。

        关键修复：Sector 默认弧心在原点，必须用 .shift() 而非 .move_to()。
        .move_to() 移动包围盒中心，对非对称扇形会产生偏移错位。
        """
        return Sector(
            radius=radius,
            angle=angle,
            start_angle=start_angle,
            color=color,
            fill_opacity=fill_opacity,
            stroke_width=0,
        ).shift(center)           # ← 核心修复

    # ------------------------------------------------------------------ #

    def create_fraction_display(self, numerator, denominator,
                                color=WHITE, font_size=36):
        """创建分数显示"""
        num_text = MathTex(str(numerator), font_size=font_size, color=color)
        line = Line(LEFT * 0.3, RIGHT * 0.3, color=color, stroke_width=2)
        den_text = MathTex(str(denominator), font_size=font_size, color=color)
        return VGroup(num_text, line, den_text).arrange(DOWN, buff=0.15)

    def scene_1_opening(self):
        """场景1: 开场钩子"""
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 7)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        hook_q1 = MathTex(r"\frac{1}{4} + \frac{1}{4} = ?",
                           font_size=42, color=self.COLOR_HIGHLIGHT).move_to(UP * 5)
        hook_q2 = MathTex(r"\frac{2}{3} - \frac{1}{2} = ?",
                           font_size=42, color=self.COLOR_HIGHLIGHT).move_to(UP * 3)

        self.play(Write(hook_q1), run_time=0.8)
        self.play(Write(hook_q2), run_time=0.8)

        question_marks = VGroup(
            Text("?", font_size=60, color=RED).move_to(UP * 4.5 + RIGHT * 2.5),
            Text("?", font_size=60, color=RED).move_to(UP * 2.5 + RIGHT * 2.5),
        )
        for qm in question_marks:
            self.play(Flash(qm, color=RED, flash_radius=0.4), run_time=0.3)

        title = Text("分数的加减法", font="Noto Sans CJK SC",
                     font_size=48, color=GOLD).move_to(UP * 1)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        self.play(FadeOut(hook_q1), FadeOut(hook_q2),
                  FadeOut(question_marks), FadeOut(title), run_time=0.5)

    def scene_2_same_denominator_addition(self):
        """场景2: 同分母加法 - 1/4 + 1/4 = 2/4 = 1/2"""
        title = Text("同分母分数相加", font="Noto Sans CJK SC",
                     font_size=36, color=self.COLOR_PRIMARY).move_to(UP * 6.5)
        subtitle = Text("分母不变，分子相加", font="Noto Sans CJK SC",
                        font_size=24, color=GRAY_A).move_to(UP * 5.8)
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 两个圆
        circle_1 = Circle(radius=self.circle_radius, color=WHITE,
                           stroke_width=3).move_to(self.circle_left_pos)
        circle_2 = Circle(radius=self.circle_radius, color=WHITE,
                           stroke_width=3).move_to(self.circle_right_pos)
        self.play(Create(circle_1), Create(circle_2), run_time=1.0)

        # 修复：.shift() 对齐弧心
        sector_1 = self.make_sector(self.circle_left_pos, self.circle_radius,
                                    self.angle_quarter, 0, self.COLOR_PRIMARY)
        sector_2 = self.make_sector(self.circle_right_pos, self.circle_radius,
                                    self.angle_quarter, 0, self.COLOR_SECONDARY)
        self.play(FadeIn(sector_1), FadeIn(sector_2), run_time=0.8)

        label_1 = self.create_fraction_display(1, 4, self.COLOR_PRIMARY, 32)
        label_1.next_to(circle_1, DOWN, buff=0.3)
        label_2 = self.create_fraction_display(1, 4, self.COLOR_SECONDARY, 32)
        label_2.next_to(circle_2, DOWN, buff=0.3)
        self.play(Write(label_1), Write(label_2), run_time=0.6)

        plus_sign = MathTex("+", font_size=48, color=WHITE).move_to(
            (self.circle_left_pos + self.circle_right_pos) / 2 + DOWN * 0.3)
        self.play(FadeIn(plus_sign), run_time=0.3)

        explain = Text("分母相同，分子直接相加", font="Noto Sans CJK SC",
                       font_size=22, color=GRAY_A).move_to(DOWN * 4.5)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)

        result_circle = Circle(radius=self.circle_radius, color=WHITE,
                               stroke_width=3).move_to(self.circle_result_pos)
        # 修复：result_sector 也用 shift
        result_sector = self.make_sector(self.circle_result_pos,
                                         self.circle_radius,
                                         self.angle_half, 0, self.COLOR_RESULT)

        self.play(
            FadeOut(explain),
            Transform(circle_1.copy(), result_circle),
            Transform(sector_1.copy(), result_sector),
            Transform(sector_2.copy(), result_sector),
            run_time=1.2,
        )
        self.add(result_circle, result_sector)

        result_2_4 = self.create_fraction_display(2, 4, self.COLOR_RESULT, 36)
        result_2_4.next_to(result_circle, DOWN, buff=0.3)
        self.play(Write(result_2_4), run_time=0.8)

        simplify_text = Text("化为最简分数", font="Noto Sans CJK SC",
                             font_size=22, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5)
        self.play(FadeIn(simplify_text), run_time=0.5)

        result_1_2 = self.create_fraction_display(1, 2, self.COLOR_RESULT, 36)
        result_1_2.next_to(result_circle, DOWN, buff=0.3)

        arrow = Arrow(
            result_2_4.get_right() + RIGHT * 0.3,
            result_1_2.get_left() + LEFT * 0.3,
            color=self.COLOR_HIGHLIGHT, stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        ).shift(DOWN * 3)

        result_2_4_copy = result_2_4.copy().shift(DOWN * 3 + LEFT * 1.2)
        result_1_2_final = result_1_2.copy().shift(DOWN * 3 + RIGHT * 1.2)

        self.play(FadeOut(result_2_4),
                  TransformFromCopy(result_2_4, result_2_4_copy), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(result_1_2_final), run_time=0.6)
        self.play(Circumscribe(result_1_2_final, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        self.wait(0.5)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(circle_1), FadeOut(circle_2),
            FadeOut(sector_1), FadeOut(sector_2),
            FadeOut(label_1), FadeOut(label_2),
            FadeOut(plus_sign),
            FadeOut(result_circle), FadeOut(result_sector),
            FadeOut(simplify_text),
            FadeOut(result_2_4_copy), FadeOut(arrow), FadeOut(result_1_2_final),
            run_time=0.6,
        )

    def scene_3_same_denominator_subtraction(self):
        """场景3: 同分母减法 - 3/5 - 1/5 = 2/5"""
        title = Text("同分母分数相减", font="Noto Sans CJK SC",
                     font_size=36, color=self.COLOR_PRIMARY).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        blocks = VGroup()
        for x_pos in self.block_positions_5:
            block = Rectangle(width=self.block_width, height=self.block_height,
                               color=WHITE, stroke_width=3)
            block.move_to(np.array([x_pos, self.rect_y, 0]))
            blocks.add(block)
        self.play(Create(blocks), run_time=1.0)

        filled_blocks = VGroup(*[
            blocks[i].copy().set_fill(self.COLOR_PRIMARY, opacity=0.7)
            for i in range(3)
        ])
        self.play(FadeIn(filled_blocks), run_time=0.6)

        label_3_5 = self.create_fraction_display(3, 5, self.COLOR_PRIMARY, 32)
        label_3_5.move_to(UP * 0.2)
        self.play(Write(label_3_5), run_time=0.5)

        minus_sign = MathTex("-", font_size=36, color=WHITE)
        label_1_5 = self.create_fraction_display(1, 5, self.COLOR_SECONDARY, 32)
        operation = VGroup(label_3_5, minus_sign, label_1_5).arrange(RIGHT, buff=0.3)
        operation.move_to(UP * 0.2)

        self.play(Transform(label_3_5, operation[0]),
                  FadeIn(minus_sign), Write(label_1_5), run_time=0.5)

        explain = Text("分母不变，分子相减", font="Noto Sans CJK SC",
                       font_size=22, color=GRAY_A).move_to(DOWN * 1)
        self.play(FadeIn(explain), run_time=0.5)

        self.play(filled_blocks[2].animate.set_fill(opacity=0.2),
                  FadeOut(explain), run_time=0.8)

        result_2_5 = self.create_fraction_display(2, 5, self.COLOR_RESULT, 40)
        result_2_5.move_to(DOWN * 2.5)
        equals = MathTex("=", font_size=36, color=WHITE).next_to(operation, RIGHT, buff=0.3)

        self.play(FadeIn(equals), Write(result_2_5), run_time=0.7)
        self.play(Circumscribe(result_2_5, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        self.wait(0.5)

        self.play(
            FadeOut(title), FadeOut(blocks), FadeOut(filled_blocks),
            FadeOut(label_3_5), FadeOut(minus_sign), FadeOut(label_1_5),
            FadeOut(equals), FadeOut(result_2_5),
            run_time=0.6,
        )

    def scene_4_different_denominator_problem(self):
        """场景4: 异分母问题提出"""
        question = MathTex(r"\frac{1}{2} + \frac{1}{3} = ?",
                           font_size=48, color=self.COLOR_HIGHLIGHT).move_to(UP * 6)
        self.play(Write(question), run_time=0.8)

        circle_left = Circle(radius=self.circle_radius, color=WHITE,
                              stroke_width=3).move_to(self.circle_left_pos)
        circle_right = Circle(radius=self.circle_radius, color=WHITE,
                               stroke_width=3).move_to(self.circle_right_pos)
        self.play(Create(circle_left), Create(circle_right), run_time=1.0)

        # 修复：shift 对齐弧心
        sector_half = self.make_sector(self.circle_left_pos, self.circle_radius,
                                       self.angle_half, 0, self.COLOR_PRIMARY)
        sector_third = self.make_sector(self.circle_right_pos, self.circle_radius,
                                        self.angle_third, 0, self.COLOR_SECONDARY)
        self.play(FadeIn(sector_half), FadeIn(sector_third), run_time=0.8)

        big_question = Text("?", font_size=80, color=RED).move_to(ORIGIN)
        for _ in range(3):
            self.play(Flash(big_question, color=RED, flash_radius=0.6), run_time=0.3)

        problem_text = Text("分母不同，无法直接相加!", font="Noto Sans CJK SC",
                            font_size=28, color=RED).move_to(DOWN * 2)
        self.play(FadeIn(problem_text, shift=UP * 0.3), run_time=0.8)

        solution_text = Text("需要通分!", font="Noto Sans CJK SC",
                             font_size=36, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 3.5)
        self.play(Write(solution_text), run_time=0.7)
        self.wait(0.5)

        self.play(
            FadeOut(circle_left), FadeOut(circle_right),
            FadeOut(sector_half), FadeOut(sector_third),
            FadeOut(big_question), FadeOut(problem_text), FadeOut(solution_text),
            run_time=0.6,
        )
        self.question_top = question

    def scene_5_common_denominator_process(self):
        """场景5: 通分过程详解"""
        step1_title = Text("步骤1: 通分", font="Noto Sans CJK SC",
                           font_size=32, color=self.COLOR_HIGHLIGHT).move_to(UP * 5)
        self.play(Write(step1_title), run_time=0.5)

        lcm_text = Text("2和3的最小公倍数 = 6", font="Noto Sans CJK SC",
                        font_size=26, color=GRAY_A).move_to(UP * 4.2)
        self.play(FadeIn(lcm_text), run_time=0.8)

        left_center = LEFT * 3 + UP * 2
        right_center = RIGHT * 3 + UP * 2
        r = 1.0

        # ── 左圆：1/2 → 3/6 ──────────────────────────────────────── #
        circle_left = Circle(radius=r, color=WHITE, stroke_width=2).move_to(left_center)

        division_2 = Line(
            left_center + UP * r, left_center + DOWN * r,
            color=GRAY_B, stroke_width=2,
        )

        # 修复：shift 对齐弧心
        sector_2_initial = self.make_sector(left_center, r, PI, 0,
                                            self.COLOR_PRIMARY, 0.6)

        self.play(Create(circle_left), Create(division_2),
                  FadeIn(sector_2_initial), run_time=0.8)

        divisions_6_left = VGroup(*[
            Line(left_center,
                 left_center + r * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]),
                 color=GRAY_B, stroke_width=2)
            for i in range(6)
        ])

        sectors_6_left = VGroup(*[
            self.make_sector(left_center, r, PI / 3, i * PI / 3,
                             self.COLOR_PRIMARY, 0.6)
            for i in range(3)
        ])

        self.play(
            Transform(division_2, divisions_6_left),
            Transform(sector_2_initial, sectors_6_left),
            run_time=1.2,
        )

        arrow_left = Arrow(left_center + UP * 0.5, left_center + DOWN * 0.5,
                           color=self.COLOR_HIGHLIGHT, stroke_width=3,
                           max_tip_length_to_length_ratio=0.2)
        transform_left = MathTex(r"\frac{1}{2} = \frac{3}{6}", font_size=28,
                                  color=WHITE).next_to(arrow_left, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow_left), Write(transform_left), run_time=0.8)

        # ── 右圆：1/3 → 2/6 ──────────────────────────────────────── #
        circle_right = Circle(radius=r, color=WHITE, stroke_width=2).move_to(right_center)

        divisions_3 = VGroup(*[
            Line(right_center,
                 right_center + r * np.array([np.cos(i * 2 * PI / 3),
                                               np.sin(i * 2 * PI / 3), 0]),
                 color=GRAY_B, stroke_width=2)
            for i in range(3)
        ])

        # 修复：shift 对齐弧心
        sector_3_initial = self.make_sector(right_center, r, 2 * PI / 3, 0,
                                            self.COLOR_SECONDARY, 0.6)

        self.play(Create(circle_right), Create(divisions_3),
                  FadeIn(sector_3_initial), run_time=0.8)

        divisions_6_right = VGroup(*[
            Line(right_center,
                 right_center + r * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]),
                 color=GRAY_B, stroke_width=2)
            for i in range(6)
        ])

        sectors_6_right = VGroup(*[
            self.make_sector(right_center, r, PI / 3, i * PI / 3,
                             self.COLOR_SECONDARY, 0.6)
            for i in range(2)
        ])

        self.play(
            Transform(divisions_3, divisions_6_right),
            Transform(sector_3_initial, sectors_6_right),
            run_time=1.2,
        )

        arrow_right = Arrow(right_center + UP * 0.5, right_center + DOWN * 0.5,
                            color=self.COLOR_HIGHLIGHT, stroke_width=3,
                            max_tip_length_to_length_ratio=0.2)
        transform_right = MathTex(r"\frac{1}{3} = \frac{2}{6}", font_size=28,
                                   color=WHITE).next_to(arrow_right, LEFT, buff=0.2)
        self.play(GrowArrow(arrow_right), Write(transform_right), run_time=0.8)

        # ── 步骤2：相加 ───────────────────────────────────────────── #
        step2_title = Text("步骤2: 相加", font="Noto Sans CJK SC",
                           font_size=32, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 2)
        self.play(Write(step2_title), run_time=0.5)

        addition_formula = MathTex(r"\frac{3}{6} + \frac{2}{6}",
                                   font_size=36, color=WHITE).move_to(DOWN * 3)
        self.play(Write(addition_formula), run_time=0.6)

        result_center = DOWN * 5
        result_circle = Circle(radius=r, color=WHITE, stroke_width=2).move_to(result_center)

        # 修复：5个扇形各自 shift 到 result_center
        sectors_result = VGroup(*[
            self.make_sector(result_center, r, PI / 3, i * PI / 3,
                             self.COLOR_RESULT, 0.7)
            for i in range(5)
        ])

        divisions_result = VGroup(*[
            Line(result_center,
                 result_center + r * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]),
                 color=GRAY_B, stroke_width=2)
            for i in range(6)
        ])

        self.play(Create(result_circle), Create(divisions_result),
                  FadeIn(sectors_result), run_time=1.0)

        result_text = MathTex(r"= \frac{5}{6}", font_size=40,
                              color=self.COLOR_RESULT).next_to(result_circle, DOWN, buff=0.5)
        self.play(Write(result_text), run_time=0.7)
        self.play(Flash(result_text, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.6)
        self.wait(0.5)

        self.play(
            FadeOut(self.question_top),
            FadeOut(step1_title), FadeOut(lcm_text),
            FadeOut(circle_left), FadeOut(circle_right),
            FadeOut(division_2), FadeOut(sector_2_initial),
            FadeOut(divisions_3), FadeOut(sector_3_initial),
            FadeOut(arrow_left), FadeOut(arrow_right),
            FadeOut(transform_left), FadeOut(transform_right),
            FadeOut(step2_title), FadeOut(addition_formula),
            FadeOut(result_circle), FadeOut(divisions_result),
            FadeOut(sectors_result), FadeOut(result_text),
            run_time=0.6,
        )

    def scene_6_different_denominator_subtraction(self):
        """场景6: 异分母减法示例 - 2/3 - 1/2"""
        problem = MathTex(r"\frac{2}{3} - \frac{1}{2}",
                          font_size=40, color=WHITE).move_to(UP * 6)
        self.play(Write(problem), run_time=0.5)

        step_text = Text("通分到公分母6:", font="Noto Sans CJK SC",
                         font_size=26, color=GRAY_A).move_to(UP * 4.8)
        converted = MathTex(r"= \frac{4}{6} - \frac{3}{6}",
                            font_size=36, color=WHITE).move_to(UP * 4)
        self.play(FadeIn(step_text), run_time=0.4)
        self.play(Write(converted), run_time=0.8)

        blocks = VGroup()
        for x_pos in self.block_positions_6:
            block = Rectangle(width=self.block_width * 0.85, height=self.block_height,
                               color=WHITE, stroke_width=2)
            block.move_to(np.array([x_pos, 1.5, 0]))
            blocks.add(block)
        self.play(Create(blocks), run_time=0.8)

        filled_4 = VGroup(*[
            blocks[i].copy().set_fill(self.COLOR_PRIMARY, opacity=0.7)
            for i in range(4)
        ])
        self.play(FadeIn(filled_4), run_time=0.5)

        label_4_6 = Text("4/6", font_size=28, color=self.COLOR_PRIMARY).move_to(UP * 0.2)
        self.play(Write(label_4_6), run_time=0.4)

        subtract_text = Text("减去 3/6", font="Noto Sans CJK SC",
                             font_size=24, color=self.COLOR_SECONDARY).move_to(DOWN * 0.5)
        self.play(FadeIn(subtract_text), run_time=0.4)

        self.play(
            filled_4[1].animate.set_fill(opacity=0.2),
            filled_4[2].animate.set_fill(opacity=0.2),
            filled_4[3].animate.set_fill(opacity=0.2),
            run_time=0.8,
        )

        result = MathTex(r"= \frac{1}{6}", font_size=42,
                         color=self.COLOR_RESULT).move_to(DOWN * 2.5)
        self.play(Write(result), run_time=0.8)

        note = Text("已经是最简分数!", font="Noto Sans CJK SC",
                    font_size=22, color=GRAY_A).move_to(DOWN * 3.8)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(0.5)

        self.play(
            FadeOut(problem), FadeOut(step_text), FadeOut(converted),
            FadeOut(blocks), FadeOut(filled_4), FadeOut(label_4_6),
            FadeOut(subtract_text), FadeOut(result), FadeOut(note),
            run_time=0.6,
        )

    def scene_7_summary_outro(self):
        """场景7: 总结和片尾"""
        summary_title = Text("分数加减法要点", font="Noto Sans CJK SC",
                             font_size=40, color=GOLD).move_to(UP * 6.5)
        self.play(Write(summary_title), run_time=0.5)

        card_1 = self.create_summary_card(
            "同分母分数", "分母不变，分子相加减",
            r"\frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c}",
            self.COLOR_PRIMARY, UP * 3.5,
        )
        card_2 = self.create_summary_card(
            "异分母分数", "先通分，再相加减",
            r"\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}",
            self.COLOR_SECONDARY, UP * 0.5,
        )
        card_3 = self.create_summary_card(
            "结果化简", "约分到最简分数",
            r"\frac{2}{4} = \frac{1}{2}",
            self.COLOR_RESULT, DOWN * 2.5,
        )

        self.play(card_1.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.2)
        self.play(card_2.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.2)
        self.play(card_3.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(summary_title),
            FadeOut(card_1), FadeOut(card_2), FadeOut(card_3),
            run_time=0.5,
        )

        author_large = Text("上海初高中数学直通车", font="Noto Sans CJK SC",
                            font_size=38, color=WHITE).move_to(UP * 2)
        author_id = Text("@emptyandcalm", font="Noto Sans CJK SC",
                         font_size=30, color=GRAY_B).move_to(UP * 1)

        self.play(Transform(self.author_info, author_large), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text("关注我，学更多数学技巧!", font="Noto Sans CJK SC",
                           font_size=32, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 0.5)
        self.play(Write(follow_text), run_time=0.8)

        fractions_deco = VGroup()
        colors = [self.COLOR_PRIMARY, self.COLOR_SECONDARY,
                  self.COLOR_RESULT, self.COLOR_HIGHLIGHT]
        positions = [UP * 3 + LEFT * 3, UP * 3 + RIGHT * 3,
                     DOWN * 2 + LEFT * 3, DOWN * 2 + RIGHT * 3]

        for i, pos in enumerate(positions):
            frac = self.create_fraction_display(
                (i % 3) + 1, (i % 4) + 2, colors[i], 24,
            ).move_to(pos).set_opacity(0.6)
            fractions_deco.add(frac)

        self.play(*[FadeIn(f, scale=0.5) for f in fractions_deco], run_time=0.6)
        self.play(Rotate(fractions_deco, angle=PI / 4, run_time=1.5))
        self.wait(1.0)

        self.play(
            FadeOut(self.author_info), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(fractions_deco),
            run_time=1.0,
        )

    def create_summary_card(self, title, content, formula, color, position):
        """创建总结卡片"""
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        title_text = Text(title, font="Noto Sans CJK SC", font_size=26, color=WHITE)
        content_text = Text(content, font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        formula_text = MathTex(formula, font_size=24, color=color)

        text_group = VGroup(title_text, content_text, formula_text).arrange(
            DOWN, buff=0.15, aligned_edge=LEFT)
        card = VGroup(icon, text_group).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        card.shift(LEFT * 10)   # 从左侧滑入
        return card


# 运行命令:
# manim -pql fraction_addition_subtraction.py FractionAdditionSubtraction  # 快速预览
# manim -qh fraction_addition_subtraction.py FractionAdditionSubtraction   # 高质量渲染
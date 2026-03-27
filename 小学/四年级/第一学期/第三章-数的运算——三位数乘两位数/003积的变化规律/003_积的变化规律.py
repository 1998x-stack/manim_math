"""
积的变化规律
Product Change Pattern - Teaching Animation

知识点: 一个因数不变,另一个因数乘(或除以)几(0除外),积也乘(或除以)相同的数。
目标受众: 四年级小学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ProductChangePatternLesson(Scene):
    """
    积的变化规律教学动画

    场景顺序:
    1. 开场钩子 - 提问引入
    2. 观察基础算式 15×12=180
    3. 规律一: 一个因数乘几，积也乘几
    4. 规律二: 一个因数除以几，积也除以几
    5. 规律总结 + 公式
    6. 应用练习
    7. 总结 + 结尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.C_TITLE   = "#f0c040"   # 金黄 - 标题
        self.C_PRIMARY = "#4fc3f7"   # 天蓝 - 主要公式
        self.C_FACTOR  = "#ef5350"   # 红色 - 变化的因数
        self.C_PRODUCT = "#66bb6a"   # 绿色 - 积
        self.C_STEP    = "#ffa726"   # 橙色 - 步骤标题
        self.C_AUX     = "#b0bec5"   # 灰色 - 辅助说明
        self.C_ARROW   = "#ce93d8"   # 紫色 - 箭头
        self.C_RULE    = "#80deea"   # 青色 - 规律

        self.scene_1_opening()
        self.scene_2_base_equation()
        self.scene_3_multiply_pattern()
        self.scene_4_divide_pattern()
        self.scene_5_formula_summary()
        self.scene_6_practice()
        self.scene_7_outro()

    # ─────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="STHeiti",
            font_size=18,
            color=self.C_AUX
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.3)

        # 钩子问题
        hook_q = Text(
            "已知 15 × 12 = 180",
            font="STHeiti",
            font_size=42,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 4.5)

        hook_sub = Text(
            "能快速算出 15 × 120 = ?",
            font="STHeiti",
            font_size=38,
            color=WHITE
        ).move_to(UP * 3.2)

        hint = Text(
            "积的变化规律帮你秒算！",
            font="STHeiti",
            font_size=32,
            color=self.C_FACTOR
        ).move_to(UP * 1.8)

        self.play(Write(hook_q), run_time=0.9)
        self.play(FadeIn(hook_sub), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(hook_q),
            FadeOut(hook_sub),
            FadeOut(hint),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 2: 观察基础算式
    # ─────────────────────────────────────────────────
    def scene_2_base_equation(self):
        title = Text(
            "先记住这个算式",
            font="STHeiti",
            font_size=36,
            color=self.C_TITLE
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.4)

        # 大号基础算式
        base_eq = VGroup(
            Text("15", font="STHeiti", font_size=80, color=self.C_PRIMARY),
            Text("×", font="STHeiti", font_size=66, color=WHITE),
            Text("12", font="STHeiti", font_size=80, color=self.C_PRIMARY),
            Text("=", font="STHeiti", font_size=66, color=WHITE),
            Text("180", font="STHeiti", font_size=80, color=self.C_PRODUCT),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 4.0)

        self.play(Write(base_eq), run_time=1.0)
        self.play(
            Indicate(base_eq[0], color=self.C_PRIMARY, scale_factor=1.2),
            Indicate(base_eq[2], color=self.C_PRIMARY, scale_factor=1.2),
            run_time=0.6
        )
        self.play(Indicate(base_eq[4], color=self.C_PRODUCT, scale_factor=1.3), run_time=0.6)

        # 标签
        label_factor1 = Text("因数1", font="STHeiti", font_size=24, color=self.C_AUX)
        label_factor1.next_to(base_eq[0], DOWN, buff=0.3)
        label_factor2 = Text("因数2", font="STHeiti", font_size=24, color=self.C_AUX)
        label_factor2.next_to(base_eq[2], DOWN, buff=0.3)
        label_product = Text("积", font="STHeiti", font_size=28, color=self.C_PRODUCT)
        label_product.next_to(base_eq[4], DOWN, buff=0.3)

        self.play(
            FadeIn(label_factor1, shift=UP * 0.2),
            FadeIn(label_factor2, shift=UP * 0.2),
            FadeIn(label_product, shift=UP * 0.2),
            run_time=0.6
        )

        note = Text(
            "如果其中一个因数发生变化，积会怎样？",
            font="STHeiti",
            font_size=26,
            color=self.C_STEP
        ).move_to(UP * 1.8)

        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(label_factor1),
            FadeOut(label_factor2),
            FadeOut(label_product),
            FadeOut(note),
            run_time=0.4
        )

        # 保留基础算式并移到顶部
        base_small = VGroup(
            Text("15", font="STHeiti", font_size=34, color=self.C_AUX),
            Text("×", font="STHeiti", font_size=28, color=self.C_AUX),
            Text("12", font="STHeiti", font_size=34, color=self.C_AUX),
            Text("=", font="STHeiti", font_size=28, color=self.C_AUX),
            Text("180", font="STHeiti", font_size=34, color=self.C_PRODUCT),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 5.8)

        self.play(Transform(base_eq, base_small), run_time=0.6)
        self.base_eq_ref = base_eq

    # ─────────────────────────────────────────────────
    # Scene 3: 规律一 - 因数乘几，积也乘几
    # ─────────────────────────────────────────────────
    def scene_3_multiply_pattern(self):
        rule_title = Text(
            "规律一：因数扩大，积也扩大",
            font="STHeiti",
            font_size=32,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.0)
        self.play(FadeIn(rule_title), run_time=0.5)

        # 表格形式展示三个算式
        # 算式1: 15 × 12 = 180  (基础)
        row1 = self._make_equation_row("15", "×", "12", "=", "180",
                                        c_left=self.C_AUX, c_right=self.C_AUX,
                                        c_result=self.C_PRODUCT)
        row1.move_to(UP * 3.8)

        # 算式2: 15 × 120 = 1800  (12×10)
        row2 = self._make_equation_row("15", "×", "120", "=", "1800",
                                        c_left=self.C_AUX, c_right=self.C_FACTOR,
                                        c_result=self.C_PRODUCT)
        row2.move_to(UP * 2.5)

        # 算式3: 15 × 1200 = 18000  (12×100)
        row3 = self._make_equation_row("15", "×", "1200", "=", "18000",
                                        c_left=self.C_AUX, c_right=self.C_FACTOR,
                                        c_result=self.C_PRODUCT)
        row3.move_to(UP * 1.2)

        self.play(FadeIn(row1), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(row2, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(row3, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.5)

        # 箭头: 12 -> 120: ×10
        # 计算两行数字的位置
        factor2_row1_center = row1[2].get_center()
        factor2_row2_center = row2[2].get_center()
        factor2_row3_center = row3[2].get_center()

        arr_f1 = Arrow(
            factor2_row1_center + RIGHT * 0.6 + DOWN * 0.15,
            factor2_row2_center + RIGHT * 0.6 + UP * 0.15,
            color=self.C_ARROW,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_f1 = Text("×10", font="STHeiti", font_size=26, color=self.C_ARROW, weight=BOLD)
        lbl_f1.next_to(arr_f1, RIGHT, buff=0.1)

        arr_f2 = Arrow(
            factor2_row2_center + RIGHT * 0.6 + DOWN * 0.15,
            factor2_row3_center + RIGHT * 0.6 + UP * 0.15,
            color=self.C_ARROW,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_f2 = Text("×10", font="STHeiti", font_size=26, color=self.C_ARROW, weight=BOLD)
        lbl_f2.next_to(arr_f2, RIGHT, buff=0.1)

        self.play(
            GrowArrow(arr_f1),
            FadeIn(lbl_f1),
            run_time=0.6
        )
        self.play(
            GrowArrow(arr_f2),
            FadeIn(lbl_f2),
            run_time=0.6
        )
        self.wait(0.4)

        # 积的箭头: 180 -> 1800: ×10
        result_row1_center = row1[4].get_center()
        result_row2_center = row2[4].get_center()
        result_row3_center = row3[4].get_center()

        arr_r1 = Arrow(
            result_row1_center + LEFT * 0.6 + DOWN * 0.15,
            result_row2_center + LEFT * 0.6 + UP * 0.15,
            color=self.C_PRODUCT,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_r1 = Text("×10", font="STHeiti", font_size=26, color=self.C_PRODUCT, weight=BOLD)
        lbl_r1.next_to(arr_r1, LEFT, buff=0.1)

        arr_r2 = Arrow(
            result_row2_center + LEFT * 0.6 + DOWN * 0.15,
            result_row3_center + LEFT * 0.6 + UP * 0.15,
            color=self.C_PRODUCT,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_r2 = Text("×10", font="STHeiti", font_size=26, color=self.C_PRODUCT, weight=BOLD)
        lbl_r2.next_to(arr_r2, LEFT, buff=0.1)

        self.play(
            GrowArrow(arr_r1),
            FadeIn(lbl_r1),
            run_time=0.6
        )
        self.play(
            GrowArrow(arr_r2),
            FadeIn(lbl_r2),
            run_time=0.6
        )
        self.wait(0.5)

        # 规律框
        rule_box_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.8,
            height=1.5,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_RULE,
            stroke_width=3
        ).move_to(DOWN * 0.8)

        rule_text = VGroup(
            Text("因数乘几", font="STHeiti", font_size=30, color=self.C_FACTOR, weight=BOLD),
            Text("，积也乘几", font="STHeiti", font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.8)

        self.play(FadeIn(rule_box_bg), run_time=0.3)
        self.play(Write(rule_text), run_time=0.7)
        self.play(Indicate(rule_text, scale_factor=1.08), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(rule_title),
            FadeOut(row1),
            FadeOut(row2),
            FadeOut(row3),
            FadeOut(arr_f1), FadeOut(lbl_f1),
            FadeOut(arr_f2), FadeOut(lbl_f2),
            FadeOut(arr_r1), FadeOut(lbl_r1),
            FadeOut(arr_r2), FadeOut(lbl_r2),
            FadeOut(rule_box_bg),
            FadeOut(rule_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 4: 规律二 - 因数除以几，积也除以几
    # ─────────────────────────────────────────────────
    def scene_4_divide_pattern(self):
        rule_title = Text(
            "规律二：因数缩小，积也缩小",
            font="STHeiti",
            font_size=32,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.0)
        self.play(FadeIn(rule_title), run_time=0.5)

        # 算式1: 15 × 120 = 1800  (基础)
        row1 = self._make_equation_row("15", "×", "120", "=", "1800",
                                        c_left=self.C_AUX, c_right=self.C_AUX,
                                        c_result=self.C_PRODUCT)
        row1.move_to(UP * 3.8)

        # 算式2: 15 × 12 = 180  (÷10)
        row2 = self._make_equation_row("15", "×", "12", "=", "180",
                                        c_left=self.C_AUX, c_right=self.C_FACTOR,
                                        c_result=self.C_PRODUCT)
        row2.move_to(UP * 2.5)

        # 算式3: 15 × 6 = 90  (÷2)
        row3 = self._make_equation_row("15", "×", "6", "=", "90",
                                        c_left=self.C_AUX, c_right=self.C_FACTOR,
                                        c_result=self.C_PRODUCT)
        row3.move_to(UP * 1.2)

        self.play(FadeIn(row1), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(row2, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(row3, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.5)

        # 因数箭头: 120 -> 12: ÷10
        factor2_row1_center = row1[2].get_center()
        factor2_row2_center = row2[2].get_center()
        factor2_row3_center = row3[2].get_center()

        arr_f1 = Arrow(
            factor2_row1_center + RIGHT * 0.55 + DOWN * 0.15,
            factor2_row2_center + RIGHT * 0.55 + UP * 0.15,
            color=self.C_ARROW,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_f1 = Text("÷10", font="STHeiti", font_size=26, color=self.C_ARROW, weight=BOLD)
        lbl_f1.next_to(arr_f1, RIGHT, buff=0.1)

        arr_f2 = Arrow(
            factor2_row2_center + RIGHT * 0.55 + DOWN * 0.15,
            factor2_row3_center + RIGHT * 0.55 + UP * 0.15,
            color=self.C_ARROW,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_f2 = Text("÷2", font="STHeiti", font_size=26, color=self.C_ARROW, weight=BOLD)
        lbl_f2.next_to(arr_f2, RIGHT, buff=0.1)

        self.play(GrowArrow(arr_f1), FadeIn(lbl_f1), run_time=0.6)
        self.play(GrowArrow(arr_f2), FadeIn(lbl_f2), run_time=0.6)
        self.wait(0.4)

        # 积的箭头
        result_row1_center = row1[4].get_center()
        result_row2_center = row2[4].get_center()
        result_row3_center = row3[4].get_center()

        arr_r1 = Arrow(
            result_row1_center + LEFT * 0.55 + DOWN * 0.15,
            result_row2_center + LEFT * 0.55 + UP * 0.15,
            color=self.C_PRODUCT,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_r1 = Text("÷10", font="STHeiti", font_size=26, color=self.C_PRODUCT, weight=BOLD)
        lbl_r1.next_to(arr_r1, LEFT, buff=0.1)

        arr_r2 = Arrow(
            result_row2_center + LEFT * 0.55 + DOWN * 0.15,
            result_row3_center + LEFT * 0.55 + UP * 0.15,
            color=self.C_PRODUCT,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        lbl_r2 = Text("÷2", font="STHeiti", font_size=26, color=self.C_PRODUCT, weight=BOLD)
        lbl_r2.next_to(arr_r2, LEFT, buff=0.1)

        self.play(GrowArrow(arr_r1), FadeIn(lbl_r1), run_time=0.6)
        self.play(GrowArrow(arr_r2), FadeIn(lbl_r2), run_time=0.6)
        self.wait(0.5)

        # 规律框
        rule_box_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.8,
            height=1.5,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_RULE,
            stroke_width=3
        ).move_to(DOWN * 0.8)

        rule_text = VGroup(
            Text("因数除以几", font="STHeiti", font_size=30, color=self.C_FACTOR, weight=BOLD),
            Text("，积也除以几", font="STHeiti", font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.8)

        self.play(FadeIn(rule_box_bg), run_time=0.3)
        self.play(Write(rule_text), run_time=0.7)
        self.play(Indicate(rule_text, scale_factor=1.08), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(rule_title),
            FadeOut(row1), FadeOut(row2), FadeOut(row3),
            FadeOut(arr_f1), FadeOut(lbl_f1),
            FadeOut(arr_f2), FadeOut(lbl_f2),
            FadeOut(arr_r1), FadeOut(lbl_r1),
            FadeOut(arr_r2), FadeOut(lbl_r2),
            FadeOut(rule_box_bg),
            FadeOut(rule_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 5: 规律总结 + 公式
    # ─────────────────────────────────────────────────
    def scene_5_formula_summary(self):
        sum_title = Text(
            "积的变化规律",
            font="STHeiti",
            font_size=44,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.0)
        self.play(FadeIn(sum_title), run_time=0.4)

        # 大背景框
        box_bg = RoundedRectangle(
            corner_radius=0.4,
            width=8.0,
            height=6.5,
            fill_color="#0d1b35",
            fill_opacity=1,
            stroke_color=self.C_PRIMARY,
            stroke_width=3
        ).move_to(UP * 1.8)
        self.play(FadeIn(box_bg), run_time=0.4)

        # 条件行
        cond_label = Text(
            "已知：",
            font="STHeiti",
            font_size=28,
            color=self.C_AUX
        )
        cond_eq = VGroup(
            Text("a", font="STHeiti", font_size=34, color=self.C_PRIMARY),
            Text("×", font="STHeiti", font_size=28, color=WHITE),
            Text("b", font="STHeiti", font_size=34, color=self.C_PRIMARY),
            Text("=", font="STHeiti", font_size=28, color=WHITE),
            Text("c", font="STHeiti", font_size=34, color=self.C_PRODUCT),
        ).arrange(RIGHT, buff=0.2)
        cond_row = VGroup(cond_label, cond_eq).arrange(RIGHT, buff=0.3)
        cond_row.move_to(UP * 4.0)

        self.play(FadeIn(cond_row, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.3)

        # 分割线
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=self.C_AUX, stroke_width=1.5)
        divider.move_to(UP * 3.2)
        self.play(Create(divider), run_time=0.4)

        # 规律1行
        rule1_label = Text(
            "则：",
            font="STHeiti",
            font_size=28,
            color=self.C_AUX
        )
        rule1_eq = VGroup(
            Text("a", font="STHeiti", font_size=34, color=self.C_PRIMARY),
            Text("×", font="STHeiti", font_size=28, color=WHITE),
            Text("(b × n)", font="STHeiti", font_size=34, color=self.C_FACTOR),
            Text("=", font="STHeiti", font_size=28, color=WHITE),
            Text("c × n", font="STHeiti", font_size=34, color=self.C_PRODUCT),
        ).arrange(RIGHT, buff=0.2)
        rule1_row = VGroup(rule1_label, rule1_eq).arrange(RIGHT, buff=0.3)
        rule1_row.move_to(UP * 2.4)

        rule1_note = Text(
            "（因数乘 n，积也乘 n）",
            font="STHeiti",
            font_size=24,
            color=self.C_RULE
        ).move_to(UP * 1.6)

        self.play(FadeIn(rule1_row, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(rule1_note), run_time=0.4)
        self.wait(0.4)

        # 规律2行
        rule2_label = Text(
            "且：",
            font="STHeiti",
            font_size=28,
            color=self.C_AUX
        )
        rule2_eq = VGroup(
            Text("a", font="STHeiti", font_size=34, color=self.C_PRIMARY),
            Text("×", font="STHeiti", font_size=28, color=WHITE),
            Text("(b ÷ n)", font="STHeiti", font_size=34, color=self.C_FACTOR),
            Text("=", font="STHeiti", font_size=28, color=WHITE),
            Text("c ÷ n", font="STHeiti", font_size=34, color=self.C_PRODUCT),
        ).arrange(RIGHT, buff=0.2)
        rule2_row = VGroup(rule2_label, rule2_eq).arrange(RIGHT, buff=0.3)
        rule2_row.move_to(UP * 0.6)

        rule2_note = Text(
            "（因数除以 n，积也除以 n）",
            font="STHeiti",
            font_size=24,
            color=self.C_RULE
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(rule2_row, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(rule2_note), run_time=0.4)
        self.wait(0.4)

        # 重要前提
        condition_note = VGroup(
            Text("注意：n ≠ 0", font="STHeiti", font_size=26, color=self.C_FACTOR, weight=BOLD),
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(condition_note), run_time=0.4)
        self.wait(0.4)

        # 示例
        example_title = Text(
            "示例：",
            font="STHeiti",
            font_size=26,
            color=self.C_AUX
        )
        example_eq = VGroup(
            Text("15×12=180", font="STHeiti", font_size=28, color=self.C_AUX),
            Text("→", font="STHeiti", font_size=24, color=self.C_ARROW),
            Text("15×120=1800", font="STHeiti", font_size=28, color=self.C_TITLE, weight=BOLD),
        ).arrange(RIGHT, buff=0.25)
        example_row = VGroup(example_title, example_eq).arrange(RIGHT, buff=0.2)
        example_row.move_to(DOWN * 2.2)

        self.play(FadeIn(example_row, shift=UP * 0.2), run_time=0.6)
        self.play(
            Indicate(example_eq[2], color=self.C_TITLE, scale_factor=1.15),
            run_time=0.7
        )
        self.wait(2.5)

        self.play(
            FadeOut(sum_title),
            FadeOut(box_bg),
            FadeOut(cond_row),
            FadeOut(divider),
            FadeOut(rule1_row),
            FadeOut(rule1_note),
            FadeOut(rule2_row),
            FadeOut(rule2_note),
            FadeOut(condition_note),
            FadeOut(example_row),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────
    # Scene 6: 应用练习
    # ─────────────────────────────────────────────────
    def scene_6_practice(self):
        title = Text(
            "应用练习",
            font="STHeiti",
            font_size=40,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title), run_time=0.4)

        # 已知条件
        known_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.2,
            fill_color="#1a2a40",
            fill_opacity=1,
            stroke_color=self.C_AUX,
            stroke_width=2
        ).move_to(UP * 5.4)

        known_text = VGroup(
            Text("已知：", font="STHeiti", font_size=28, color=self.C_AUX),
            Text("15 × 12 = 180", font="STHeiti", font_size=30, color=self.C_PRIMARY, weight=BOLD),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 5.4)

        self.play(FadeIn(known_bg), FadeIn(known_text), run_time=0.5)
        self.wait(0.3)

        # ─── 题目1 ───
        q1_label = self._make_step_badge("1", self.C_STEP)
        q1_label.move_to(UP * 4.2 + LEFT * 3.5)

        q1_text = VGroup(
            Text("15 × 120 = ?", font="STHeiti", font_size=36, color=WHITE),
        ).move_to(UP * 4.2 + RIGHT * 0.5)

        self.play(FadeIn(q1_label), Write(q1_text), run_time=0.6)
        self.wait(0.5)

        # 分析: 12 × 10 = 120，因数扩大10倍
        q1_analysis = VGroup(
            Text("因数 12 扩大", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("10", font="STHeiti", font_size=28, color=self.C_FACTOR, weight=BOLD),
            Text("倍 →", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("积也扩大", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("10", font="STHeiti", font_size=28, color=self.C_PRODUCT, weight=BOLD),
            Text("倍", font="STHeiti", font_size=24, color=self.C_AUX),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 3.3)

        self.play(FadeIn(q1_analysis, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.4)

        q1_ans_bg = RoundedRectangle(
            corner_radius=0.2,
            width=5.0,
            height=1.0,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_PRODUCT,
            stroke_width=2.5
        ).move_to(UP * 2.4)
        q1_ans = Text(
            "15 × 120 = 1800",
            font="STHeiti",
            font_size=32,
            color=self.C_PRODUCT,
            weight=BOLD
        ).move_to(UP * 2.4)

        self.play(FadeIn(q1_ans_bg), run_time=0.3)
        self.play(Write(q1_ans), run_time=0.6)
        self.play(Flash(q1_ans, color=self.C_PRODUCT, flash_radius=0.8, num_lines=8), run_time=0.6)
        self.wait(1.0)

        # ─── 题目2 ───
        q2_label = self._make_step_badge("2", self.C_STEP)
        q2_label.move_to(UP * 1.3 + LEFT * 3.5)

        q2_text = VGroup(
            Text("15 × 6 = ?", font="STHeiti", font_size=36, color=WHITE),
        ).move_to(UP * 1.3 + RIGHT * 0.5)

        self.play(FadeIn(q2_label), Write(q2_text), run_time=0.6)
        self.wait(0.5)

        q2_analysis = VGroup(
            Text("因数 12 缩小", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("2", font="STHeiti", font_size=28, color=self.C_FACTOR, weight=BOLD),
            Text("倍 →", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("积也缩小", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("2", font="STHeiti", font_size=28, color=self.C_PRODUCT, weight=BOLD),
            Text("倍", font="STHeiti", font_size=24, color=self.C_AUX),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 0.4)

        self.play(FadeIn(q2_analysis, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.4)

        q2_ans_bg = RoundedRectangle(
            corner_radius=0.2,
            width=4.5,
            height=1.0,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_PRODUCT,
            stroke_width=2.5
        ).move_to(DOWN * 0.5)
        q2_ans = Text(
            "15 × 6 = 90",
            font="STHeiti",
            font_size=32,
            color=self.C_PRODUCT,
            weight=BOLD
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(q2_ans_bg), run_time=0.3)
        self.play(Write(q2_ans), run_time=0.6)
        self.play(Flash(q2_ans, color=self.C_PRODUCT, flash_radius=0.8, num_lines=8), run_time=0.6)
        self.wait(1.0)

        # ─── 题目3 (进阶) ───
        q3_label = self._make_step_badge("3", self.C_STEP)
        q3_label.move_to(DOWN * 1.6 + LEFT * 3.5)

        q3_text = VGroup(
            Text("150 × 12 = ?", font="STHeiti", font_size=34, color=self.C_TITLE),
        ).move_to(DOWN * 1.6 + RIGHT * 0.5)

        bonus = Text("（思考题！）", font="STHeiti", font_size=22, color=self.C_STEP)
        bonus.next_to(q3_text, RIGHT, buff=0.15)

        self.play(FadeIn(q3_label), Write(q3_text), FadeIn(bonus), run_time=0.7)
        self.wait(0.6)

        q3_hint = VGroup(
            Text("因数 15 扩大 10 倍 →", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("积也扩大 10 倍", font="STHeiti", font_size=24, color=self.C_PRODUCT),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.5)

        q3_ans_text = Text(
            "150 × 12 = 1800",
            font="STHeiti",
            font_size=32,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(DOWN * 3.4)

        self.play(FadeIn(q3_hint), run_time=0.5)
        self.wait(0.4)
        self.play(Write(q3_ans_text), run_time=0.7)
        self.play(Indicate(q3_ans_text, color=self.C_TITLE, scale_factor=1.1), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(known_bg), FadeOut(known_text),
            FadeOut(q1_label), FadeOut(q1_text), FadeOut(q1_analysis),
            FadeOut(q1_ans_bg), FadeOut(q1_ans),
            FadeOut(q2_label), FadeOut(q2_text), FadeOut(q2_analysis),
            FadeOut(q2_ans_bg), FadeOut(q2_ans),
            FadeOut(q3_label), FadeOut(q3_text), FadeOut(bonus),
            FadeOut(q3_hint), FadeOut(q3_ans_text),
            FadeOut(self.base_eq_ref),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────
    # Scene 7: 总结 + 结尾
    # ─────────────────────────────────────────────────
    def scene_7_outro(self):
        # 总结标题
        sum_title = Text(
            "记住这两条规律",
            font="STHeiti",
            font_size=40,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(sum_title), run_time=0.4)

        # 规律卡片1
        card1_bg = RoundedRectangle(
            corner_radius=0.35,
            width=7.8,
            height=1.6,
            fill_color="#1a2e1a",
            fill_opacity=1,
            stroke_color=self.C_PRODUCT,
            stroke_width=2.5
        ).move_to(UP * 4.6)

        card1_text = VGroup(
            Text("一个因数不变，另一个因数", font="STHeiti", font_size=26, color=WHITE),
            Text("乘几", font="STHeiti", font_size=30, color=self.C_FACTOR, weight=BOLD),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 4.8)

        card1_sub = Text(
            "积也乘几",
            font="STHeiti",
            font_size=28,
            color=self.C_PRODUCT,
            weight=BOLD
        ).move_to(UP * 4.3)

        self.play(FadeIn(card1_bg), run_time=0.3)
        self.play(FadeIn(card1_text), FadeIn(card1_sub), run_time=0.5)

        # 规律卡片2
        card2_bg = RoundedRectangle(
            corner_radius=0.35,
            width=7.8,
            height=1.6,
            fill_color="#2a1a1a",
            fill_opacity=1,
            stroke_color=self.C_FACTOR,
            stroke_width=2.5
        ).move_to(UP * 2.6)

        card2_text = VGroup(
            Text("一个因数不变，另一个因数", font="STHeiti", font_size=26, color=WHITE),
            Text("除以几", font="STHeiti", font_size=30, color=self.C_FACTOR, weight=BOLD),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 2.8)

        card2_sub = Text(
            "积也除以几",
            font="STHeiti",
            font_size=28,
            color=self.C_PRODUCT,
            weight=BOLD
        ).move_to(UP * 2.3)

        self.play(FadeIn(card2_bg), run_time=0.3)
        self.play(FadeIn(card2_text), FadeIn(card2_sub), run_time=0.5)

        # 前提条件强调
        condition = Text(
            "前提：除数不能为 0",
            font="STHeiti",
            font_size=26,
            color=self.C_FACTOR,
            weight=BOLD
        ).move_to(UP * 1.2)
        self.play(FadeIn(condition), run_time=0.4)
        self.wait(0.5)

        # 示例快闪
        example_box = RoundedRectangle(
            corner_radius=0.3,
            width=8.0,
            height=1.0,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_PRIMARY,
            stroke_width=2
        ).move_to(UP * 0.1)

        example_content = VGroup(
            Text("15×12=180", font="STHeiti", font_size=24, color=self.C_AUX),
            Text("→", font="STHeiti", font_size=22, color=self.C_ARROW),
            Text("15×120=1800", font="STHeiti", font_size=26, color=self.C_TITLE, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.1)

        self.play(FadeIn(example_box), FadeIn(example_content), run_time=0.5)
        self.play(Indicate(example_content[2], color=self.C_TITLE, scale_factor=1.1), run_time=0.6)
        self.wait(1.0)

        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="STHeiti",
            font_size=32,
            color=YELLOW,
            weight=BOLD
        ).move_to(DOWN * 1.2)

        author_big = Text(
            "上海初高中数学直通车",
            font="STHeiti",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 2.3)

        author_id = Text(
            "@emptyandcalm",
            font="STHeiti",
            font_size=24,
            color=self.C_AUX
        ).move_to(DOWN * 3.1)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.5)

        # 装饰星星
        stars = VGroup(*[
            Text("★", font_size=24, color=YELLOW)
            .move_to(follow_text.get_center() + 3.2 * np.array([
                np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0
            ]))
            for i in range(6)
        ])
        self.play(
            LaggedStart(*[FadeIn(s, scale=0.3) for s in stars], lag_ratio=0.12),
            run_time=0.8
        )
        self.wait(2.5)

        # 全部淡出
        self.play(
            FadeOut(sum_title),
            FadeOut(card1_bg), FadeOut(card1_text), FadeOut(card1_sub),
            FadeOut(card2_bg), FadeOut(card2_text), FadeOut(card2_sub),
            FadeOut(condition),
            FadeOut(example_box), FadeOut(example_content),
            FadeOut(follow_text),
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(stars),
            FadeOut(self.author),
            run_time=1.0
        )

    # ─────────────────────────────────────────────────
    # Helper methods
    # ─────────────────────────────────────────────────
    def _make_equation_row(self, a, op1, b, op2, c,
                            c_left=WHITE, c_right=WHITE, c_result=WHITE,
                            font_size=40):
        """创建一行算式: a op1 b op2 c"""
        parts = VGroup(
            Text(a,   font="STHeiti", font_size=font_size, color=c_left),
            Text(op1, font="STHeiti", font_size=font_size - 8, color=WHITE),
            Text(b,   font="STHeiti", font_size=font_size, color=c_right),
            Text(op2, font="STHeiti", font_size=font_size - 8, color=WHITE),
            Text(c,   font="STHeiti", font_size=font_size, color=c_result),
        ).arrange(RIGHT, buff=0.2)
        return parts

    def _make_step_badge(self, text_str, color, font_size=30):
        """创建步骤徽章（圆形 + 文字）"""
        circle = Circle(radius=0.38, fill_color=color, fill_opacity=1, stroke_width=0)
        label = Text(text_str, font="STHeiti", font_size=font_size, color=WHITE, weight=BOLD)
        return VGroup(circle, label)

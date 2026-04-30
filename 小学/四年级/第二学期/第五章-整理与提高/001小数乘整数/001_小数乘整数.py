"""
小数乘整数
Decimal Times Integer - Teaching Animation

知识点: 根据"积的变化规律"和"小数点移动规律"，将小数乘法转化为整数乘法，
       先按整数算出积，再确定小数点位置。积末尾有0要化简。
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


class DecimalTimesIntegerLesson(Scene):
    """
    小数乘整数教学动画

    场景顺序:
    1. 开场钩子 - 提问引入
    2. 算理讲解 - 积的变化规律
    3. 步骤一: 转化为整数乘法 3×5=15
    4. 步骤二: 确定小数点位置
    5. 步骤三: 化简末尾零
    6. 第二个例题: 0.25×4=1.00→1
    7. 方法总结
    8. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.C_TITLE   = "#f0c040"   # 金黄 - 标题
        self.C_PRIMARY = "#4fc3f7"   # 天蓝 - 主要算式
        self.C_DECIMAL = "#ef5350"   # 红色 - 小数部分/小数点
        self.C_INT     = "#66bb6a"   # 绿色 - 整数/结果
        self.C_STEP    = "#ffa726"   # 橙色 - 步骤标题
        self.C_AUX     = "#b0bec5"   # 灰色 - 辅助说明
        self.C_ARROW   = "#ce93d8"   # 紫色 - 箭头
        self.C_RULE    = "#80deea"   # 青色 - 规律
        self.C_DOT     = "#ff6b6b"   # 亮红 - 小数点高亮

        self.scene_1_opening()
        self.scene_2_algorithm_principle()
        self.scene_3_step1_convert()
        self.scene_4_step2_decimal_point()
        self.scene_5_step3_simplify()
        self.scene_6_second_example()
        self.scene_7_summary()
        self.scene_8_outro()

    # ─────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息（顶部）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=self.C_AUX
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.3)

        # 钩子问题
        hook_q = Text(
            "0.3 × 5 = ?",
            font="PingFang SC",
            font_size=72,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 4.5)

        hook_sub = Text(
            "小数也能乘整数！",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 3.0)

        hint = Text(
            "把它变成整数就简单啦",
            font="PingFang SC",
            font_size=32,
            color=self.C_DECIMAL
        ).move_to(UP * 1.8)

        self.play(Write(hook_q), run_time=1.0)
        self.play(FadeIn(hook_sub), run_time=0.5)
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
    # Scene 2: 算理讲解 - 积的变化规律
    # ─────────────────────────────────────────────────
    def scene_2_algorithm_principle(self):
        title = Text(
            "算理：积的变化规律",
            font="PingFang SC",
            font_size=36,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.0)
        self.play(FadeIn(title), run_time=0.4)

        # 核心思路说明
        idea_text = Text(
            "0.3 就是 3 的 十分之一",
            font="PingFang SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 4.8)
        self.play(Write(idea_text), run_time=0.8)
        self.wait(0.5)

        # 关系演示
        # 大号展示: 3 vs 0.3
        label_3 = Text("3", font="PingFang SC", font_size=88, color=self.C_INT)
        label_vs = Text("vs", font="PingFang SC", font_size=40, color=self.C_AUX)
        label_03 = Text("0.3", font="PingFang SC", font_size=88, color=self.C_DECIMAL)
        compare_row = VGroup(label_3, label_vs, label_03).arrange(RIGHT, buff=0.5).move_to(UP * 3.0)

        self.play(FadeIn(compare_row), run_time=0.6)

        # 除以10的箭头
        arr_div10 = Arrow(
            label_3.get_right() + RIGHT * 0.1,
            label_03.get_left() + LEFT * 0.1,
            color=self.C_ARROW,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        lbl_div10 = Text("÷ 10", font="PingFang SC", font_size=30, color=self.C_ARROW, weight=BOLD)
        lbl_div10.next_to(arr_div10, UP, buff=0.15)

        self.play(GrowArrow(arr_div10), FadeIn(lbl_div10), run_time=0.6)
        self.wait(0.4)

        # 因此推导
        therefore_text = VGroup(
            Text("因数缩小10倍，积也缩小10倍！", font="PingFang SC", font_size=30, color=self.C_RULE),
        ).move_to(UP * 1.6)

        # 算式推导: 3×5=15  →  0.3×5=1.5
        eq_int = VGroup(
            Text("3", font="PingFang SC", font_size=52, color=self.C_INT),
            Text("×", font="PingFang SC", font_size=44, color=WHITE),
            Text("5", font="PingFang SC", font_size=52, color=self.C_PRIMARY),
            Text("=", font="PingFang SC", font_size=44, color=WHITE),
            Text("15", font="PingFang SC", font_size=52, color=self.C_INT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.4)

        eq_arr = Arrow(
            eq_int.get_right() + RIGHT * 0.15,
            eq_int.get_right() + RIGHT * 0.15 + DOWN * 1.3,
            color=self.C_ARROW,
            buff=0.05,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        eq_lbl = Text("÷10", font="PingFang SC", font_size=26, color=self.C_ARROW, weight=BOLD)
        eq_lbl.next_to(eq_arr, RIGHT, buff=0.1)

        eq_dec = VGroup(
            Text("0.3", font="PingFang SC", font_size=52, color=self.C_DECIMAL),
            Text("×", font="PingFang SC", font_size=44, color=WHITE),
            Text("5", font="PingFang SC", font_size=52, color=self.C_PRIMARY),
            Text("=", font="PingFang SC", font_size=44, color=WHITE),
            Text("1.5", font="PingFang SC", font_size=52, color=self.C_DECIMAL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.2)

        self.play(FadeIn(therefore_text), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(eq_int, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.4)
        self.play(GrowArrow(eq_arr), FadeIn(eq_lbl), run_time=0.5)
        self.play(FadeIn(eq_dec, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.4)

        # 高亮结果
        self.play(
            Indicate(eq_dec[4], color=self.C_TITLE, scale_factor=1.3),
            run_time=0.7
        )
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(idea_text),
            FadeOut(compare_row),
            FadeOut(arr_div10), FadeOut(lbl_div10),
            FadeOut(therefore_text),
            FadeOut(eq_int),
            FadeOut(eq_arr), FadeOut(eq_lbl),
            FadeOut(eq_dec),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 3: 步骤一 - 转化为整数乘法
    # ─────────────────────────────────────────────────
    def scene_3_step1_convert(self):
        # 步骤标题
        step_badge = self._make_step_badge("步骤一", self.C_STEP)
        step_badge.move_to(UP * 6.2)
        self.play(FadeIn(step_badge), run_time=0.4)

        step_title = Text(
            "先按整数乘法计算",
            font="PingFang SC",
            font_size=34,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.3)
        self.play(FadeIn(step_title), run_time=0.4)

        # 原算式展示
        orig_label = Text("原算式：", font="PingFang SC", font_size=26, color=self.C_AUX)
        orig_eq = VGroup(
            Text("0.3", font="PingFang SC", font_size=56, color=self.C_DECIMAL, weight=BOLD),
            Text("×", font="PingFang SC", font_size=48, color=WHITE),
            Text("5", font="PingFang SC", font_size=56, color=self.C_PRIMARY, weight=BOLD),
            Text("=", font="PingFang SC", font_size=48, color=WHITE),
            Text("?", font="PingFang SC", font_size=56, color=self.C_AUX),
        ).arrange(RIGHT, buff=0.25)
        orig_row = VGroup(orig_label, orig_eq).arrange(RIGHT, buff=0.3).move_to(UP * 4.0)
        self.play(FadeIn(orig_row), run_time=0.6)
        self.wait(0.4)

        # 变换过程说明
        convert_note = Text(
            "0.3 → 扩大10倍 → 3",
            font="PingFang SC",
            font_size=30,
            color=self.C_RULE
        ).move_to(UP * 2.8)
        self.play(FadeIn(convert_note, shift=RIGHT * 0.3), run_time=0.5)

        # 变换后整数算式 3×5
        convert_label = Text("转化为：", font="PingFang SC", font_size=26, color=self.C_AUX)
        convert_eq = VGroup(
            Text("3", font="PingFang SC", font_size=56, color=self.C_INT, weight=BOLD),
            Text("×", font="PingFang SC", font_size=48, color=WHITE),
            Text("5", font="PingFang SC", font_size=56, color=self.C_PRIMARY, weight=BOLD),
            Text("=", font="PingFang SC", font_size=48, color=WHITE),
            Text("15", font="PingFang SC", font_size=56, color=self.C_INT, weight=BOLD),
        ).arrange(RIGHT, buff=0.25)
        convert_row = VGroup(convert_label, convert_eq).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)

        self.play(FadeIn(convert_row, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.4)

        # 高亮15
        self.play(
            Indicate(convert_eq[4], color=self.C_TITLE, scale_factor=1.3),
            run_time=0.7
        )

        # 说明框
        note_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.2,
            fill_color="#1a2a40",
            fill_opacity=1,
            stroke_color=self.C_RULE,
            stroke_width=2
        ).move_to(DOWN * 0.3)
        note_text = Text(
            "整数乘法 3 × 5 = 15  ✓",
            font="PingFang SC",
            font_size=30,
            color=self.C_RULE
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(note_bg), FadeIn(note_text), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(step_badge), FadeOut(step_title),
            FadeOut(orig_row),
            FadeOut(convert_note),
            FadeOut(convert_row),
            FadeOut(note_bg), FadeOut(note_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 4: 步骤二 - 确定小数点位置
    # ─────────────────────────────────────────────────
    def scene_4_step2_decimal_point(self):
        step_badge = self._make_step_badge("步骤二", self.C_STEP)
        step_badge.move_to(UP * 6.2)
        self.play(FadeIn(step_badge), run_time=0.4)

        step_title = Text(
            "确定积的小数点位置",
            font="PingFang SC",
            font_size=34,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.3)
        self.play(FadeIn(step_title), run_time=0.4)

        # 规则说明
        rule_bg = RoundedRectangle(
            corner_radius=0.3,
            width=8.0,
            height=2.0,
            fill_color="#0d1b35",
            fill_opacity=1,
            stroke_color=self.C_RULE,
            stroke_width=3
        ).move_to(UP * 4.0)

        rule_line1 = Text(
            "因数中有几位小数，",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.35)
        rule_line2 = Text(
            "积就从右边数出几位点小数点",
            font="PingFang SC",
            font_size=28,
            color=self.C_DOT
        ).move_to(UP * 3.75)

        self.play(FadeIn(rule_bg), run_time=0.3)
        self.play(Write(rule_line1), run_time=0.5)
        self.play(Write(rule_line2), run_time=0.6)
        self.wait(0.4)

        # 演示计数过程
        # 展示 0.3 并标注"1位小数"
        dec_show_label = Text("因数：", font="PingFang SC", font_size=26, color=self.C_AUX)
        dec_show_eq = Text("0.3", font="PingFang SC", font_size=64, color=self.C_DECIMAL, weight=BOLD)
        dec_show_row = VGroup(dec_show_label, dec_show_eq).arrange(RIGHT, buff=0.3).move_to(UP * 2.3)
        self.play(FadeIn(dec_show_row), run_time=0.5)

        # 箭头+标注"1位小数"
        dec_count_arr = Arrow(
            dec_show_eq.get_bottom() + DOWN * 0.05,
            dec_show_eq.get_bottom() + DOWN * 0.8,
            color=self.C_ARROW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.4
        )
        dec_count_label = Text(
            "1 位小数",
            font="PingFang SC",
            font_size=28,
            color=self.C_ARROW,
            weight=BOLD
        ).next_to(dec_count_arr, DOWN, buff=0.1)

        self.play(GrowArrow(dec_count_arr), FadeIn(dec_count_label), run_time=0.5)
        self.wait(0.4)

        # 展示整数积 15 并标注数小数点
        prod_label = Text("整数积：", font="PingFang SC", font_size=26, color=self.C_AUX)
        prod_digits = Text("15", font="PingFang SC", font_size=64, color=self.C_INT, weight=BOLD)
        prod_row = VGroup(prod_label, prod_digits).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.2)
        self.play(FadeIn(prod_row), run_time=0.5)

        self.wait(0.3)

        # 从右边数1位 - 高亮"5"
        highlight_5 = SurroundingRectangle(
            prod_digits[-1],
            color=self.C_DOT,
            buff=0.08,
            corner_radius=0.05
        )
        count_text = Text(
            "从右边数 1 位",
            font="PingFang SC",
            font_size=28,
            color=self.C_DOT
        ).move_to(DOWN * 1.3)

        self.play(Create(highlight_5), FadeIn(count_text), run_time=0.5)
        self.wait(0.4)

        # 加上小数点 → 1.5
        result_label = Text("积：", font="PingFang SC", font_size=26, color=self.C_AUX)
        result_eq = Text("1.5", font="PingFang SC", font_size=64, color=self.C_DOT, weight=BOLD)
        result_row = VGroup(result_label, result_eq).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)

        self.play(FadeIn(result_row, scale=1.1), run_time=0.5)
        self.play(
            Flash(result_eq, color=self.C_TITLE, flash_radius=1.0, num_lines=10),
            run_time=0.6
        )
        self.wait(1.5)

        # 最终答案框
        ans_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.0,
            height=1.3,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_TITLE,
            stroke_width=3
        ).move_to(DOWN * 4.0)
        ans_text = Text(
            "0.3 × 5 = 1.5",
            font="PingFang SC",
            font_size=40,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(ans_bg), run_time=0.3)
        self.play(Write(ans_text), run_time=0.6)
        self.play(Indicate(ans_text, color=YELLOW, scale_factor=1.08), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(step_badge), FadeOut(step_title),
            FadeOut(rule_bg), FadeOut(rule_line1), FadeOut(rule_line2),
            FadeOut(dec_show_row),
            FadeOut(dec_count_arr), FadeOut(dec_count_label),
            FadeOut(prod_row),
            FadeOut(highlight_5), FadeOut(count_text),
            FadeOut(result_row),
            FadeOut(ans_bg), FadeOut(ans_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 5: 步骤三 - 化简末尾零
    # ─────────────────────────────────────────────────
    def scene_5_step3_simplify(self):
        step_badge = self._make_step_badge("步骤三", self.C_STEP)
        step_badge.move_to(UP * 6.2)
        self.play(FadeIn(step_badge), run_time=0.4)

        step_title = Text(
            "积末尾有零要化简！",
            font="PingFang SC",
            font_size=34,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.3)
        self.play(FadeIn(step_title), run_time=0.4)

        # 举例: 0.4 × 5 = ?
        example_label = Text(
            "例：0.4 × 5 = ?",
            font="PingFang SC",
            font_size=40,
            color=self.C_PRIMARY
        ).move_to(UP * 4.1)
        self.play(Write(example_label), run_time=0.7)
        self.wait(0.4)

        # 步骤1: 4×5=20
        int_step = VGroup(
            Text("整数算：", font="PingFang SC", font_size=28, color=self.C_AUX),
            Text("4 × 5 = 20", font="PingFang SC", font_size=40, color=self.C_INT, weight=BOLD),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.9)
        self.play(FadeIn(int_step, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)

        # 步骤2: 确定小数点 2.0
        dec_step_label = Text("定小数点：", font="PingFang SC", font_size=28, color=self.C_AUX)
        dec_step_val = Text("2.0", font="PingFang SC", font_size=48, color=self.C_DOT, weight=BOLD)
        dec_step_row = VGroup(dec_step_label, dec_step_val).arrange(RIGHT, buff=0.3).move_to(UP * 1.7)

        self.play(FadeIn(dec_step_row), run_time=0.5)
        self.wait(0.3)

        # 标注末尾的0
        zero_box = SurroundingRectangle(
            dec_step_val[-1],
            color=self.C_DECIMAL,
            buff=0.1,
            corner_radius=0.05
        )
        zero_label = Text(
            "末尾有 0！",
            font="PingFang SC",
            font_size=28,
            color=self.C_DECIMAL,
            weight=BOLD
        ).next_to(zero_box, RIGHT, buff=0.3)

        self.play(Create(zero_box), FadeIn(zero_label), run_time=0.5)
        self.wait(0.4)

        # 划掉末尾0，化简
        cross_line = Line(
            dec_step_val[-1].get_left() + LEFT * 0.05,
            dec_step_val[-1].get_right() + RIGHT * 0.05,
            color=RED,
            stroke_width=5
        )
        self.play(Create(cross_line), run_time=0.4)

        # 化简后: 2
        simplify_arrow = Arrow(
            dec_step_row.get_right() + RIGHT * 0.1,
            dec_step_row.get_right() + RIGHT * 1.8,
            color=self.C_ARROW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.35
        )
        simplify_result = Text(
            "2",
            font="PingFang SC",
            font_size=56,
            color=self.C_TITLE,
            weight=BOLD
        ).next_to(simplify_arrow, RIGHT, buff=0.1)

        self.play(GrowArrow(simplify_arrow), run_time=0.4)
        self.play(FadeIn(simplify_result, scale=1.15), run_time=0.4)
        self.wait(0.4)

        # 最终答案
        ans_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.0,
            height=1.3,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_TITLE,
            stroke_width=3
        ).move_to(DOWN * 0.3)
        ans_text = Text(
            "0.4 × 5 = 2",
            font="PingFang SC",
            font_size=44,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(ans_bg), Write(ans_text), run_time=0.6)
        self.play(
            Flash(ans_text, color=self.C_TITLE, flash_radius=0.9, num_lines=10),
            run_time=0.6
        )
        self.wait(0.5)

        # 提示框
        tip_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.8,
            height=1.6,
            fill_color="#2a1a1a",
            fill_opacity=1,
            stroke_color=self.C_DECIMAL,
            stroke_width=2
        ).move_to(DOWN * 2.1)
        tip_text_line1 = Text(
            "小数部分末尾的 0 要去掉",
            font="PingFang SC",
            font_size=26,
            color=self.C_DECIMAL
        ).move_to(DOWN * 1.9)
        tip_text_line2 = Text(
            "2.0 化简为 2  （整数）",
            font="PingFang SC",
            font_size=26,
            color=self.C_RULE
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(tip_bg), run_time=0.3)
        self.play(FadeIn(tip_text_line1), FadeIn(tip_text_line2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(step_badge), FadeOut(step_title),
            FadeOut(example_label),
            FadeOut(int_step),
            FadeOut(dec_step_row),
            FadeOut(zero_box), FadeOut(zero_label),
            FadeOut(cross_line),
            FadeOut(simplify_arrow), FadeOut(simplify_result),
            FadeOut(ans_bg), FadeOut(ans_text),
            FadeOut(tip_bg), FadeOut(tip_text_line1), FadeOut(tip_text_line2),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 6: 第二个例题 0.25 × 4
    # ─────────────────────────────────────────────────
    def scene_6_second_example(self):
        ex2_title = Text(
            "再试一题！",
            font="PingFang SC",
            font_size=44,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.3)
        self.play(FadeIn(ex2_title), run_time=0.4)

        ex2_q = Text(
            "0.25 × 4 = ?",
            font="PingFang SC",
            font_size=60,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5.0)
        self.play(Write(ex2_q), run_time=0.8)
        self.wait(0.5)

        # 步骤展示卡片
        def make_step_card(num_str, title_str, content_str, title_color, content_color, pos):
            badge = Circle(radius=0.3, fill_color=title_color, fill_opacity=1, stroke_width=0)
            badge_label = Text(num_str, font="PingFang SC", font_size=26, color=WHITE, weight=BOLD)
            badge_group = VGroup(badge, badge_label)

            t = Text(title_str, font="PingFang SC", font_size=24, color=title_color)
            c = Text(content_str, font="PingFang SC", font_size=30, color=content_color, weight=BOLD)
            text_group = VGroup(t, c).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            card = VGroup(badge_group, text_group).arrange(RIGHT, buff=0.25)
            card.move_to(pos)
            return card

        # 卡片1: 转化整数
        card1 = make_step_card(
            "1", "转化整数：",
            "25 × 4 = 100",
            self.C_STEP, self.C_INT,
            UP * 3.5
        )
        self.play(FadeIn(card1, shift=RIGHT * 0.4), run_time=0.6)
        self.wait(0.4)

        # 卡片2: 数小数位
        card2 = make_step_card(
            "2", "因数 0.25 有 2 位小数：",
            "从右数 2 位 → 1.00",
            self.C_STEP, self.C_DOT,
            UP * 1.8
        )
        self.play(FadeIn(card2, shift=RIGHT * 0.4), run_time=0.6)
        self.wait(0.4)

        # 卡片3: 化简
        card3 = make_step_card(
            "3", "化简末尾零：",
            "1.00 → 1",
            self.C_STEP, self.C_DECIMAL,
            UP * 0.1
        )
        self.play(FadeIn(card3, shift=RIGHT * 0.4), run_time=0.6)
        self.wait(0.6)

        # 最终答案
        ans2_bg = RoundedRectangle(
            corner_radius=0.35,
            width=7.5,
            height=1.5,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_TITLE,
            stroke_width=3
        ).move_to(DOWN * 1.5)
        ans2_text = Text(
            "0.25 × 4 = 1",
            font="PingFang SC",
            font_size=48,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(ans2_bg), run_time=0.3)
        self.play(Write(ans2_text), run_time=0.6)
        self.play(
            Flash(ans2_text, color=YELLOW, flash_radius=1.0, num_lines=12),
            run_time=0.7
        )
        self.wait(0.5)

        # 验证说明
        verify_text = Text(
            "验证：0.25 是 25 的百分之一，积也是100的百分之一",
            font="PingFang SC",
            font_size=20,
            color=self.C_AUX
        ).move_to(DOWN * 2.7)
        self.play(FadeIn(verify_text), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(ex2_title), FadeOut(ex2_q),
            FadeOut(card1), FadeOut(card2), FadeOut(card3),
            FadeOut(ans2_bg), FadeOut(ans2_text),
            FadeOut(verify_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 7: 方法总结
    # ─────────────────────────────────────────────────
    def scene_7_summary(self):
        sum_title = Text(
            "小数乘整数  口诀",
            font="PingFang SC",
            font_size=44,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(sum_title), run_time=0.4)

        # 大背景框
        box_bg = RoundedRectangle(
            corner_radius=0.4,
            width=8.2,
            height=7.5,
            fill_color="#0d1b35",
            fill_opacity=1,
            stroke_color=self.C_PRIMARY,
            stroke_width=3
        ).move_to(UP * 2.2)
        self.play(FadeIn(box_bg), run_time=0.3)

        # 三步口诀
        step_data = [
            ("①", "先算整数积", "去掉因数的小数点，照整数乘法算", self.C_INT),
            ("②", "数出小数位", "因数有几位小数，积就数几位点小数点", self.C_DOT),
            ("③", "去掉末尾零", "积的小数末尾有0，化简去掉", self.C_DECIMAL),
        ]

        y_positions = [UP * 4.8, UP * 2.8, UP * 0.8]

        cards = []
        for i, (num, head, body, color) in enumerate(step_data):
            num_circle = Circle(radius=0.36, fill_color=color, fill_opacity=1, stroke_width=0)
            num_text = Text(num, font="PingFang SC", font_size=28, color=WHITE, weight=BOLD)
            num_group = VGroup(num_circle, num_text)

            head_text = Text(head, font="PingFang SC", font_size=30, color=color, weight=BOLD)
            body_text = Text(body, font="PingFang SC", font_size=22, color=self.C_AUX)

            text_col = VGroup(head_text, body_text).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            card = VGroup(num_group, text_col).arrange(RIGHT, buff=0.3)
            card.move_to(y_positions[i])
            cards.append(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.3)

        # 分隔线
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=self.C_AUX, stroke_width=1.5)
        divider.move_to(DOWN * 0.5)
        self.play(Create(divider), run_time=0.3)

        # 例题小卡片
        ex_row = VGroup(
            Text("0.3×5=1.5", font="PingFang SC", font_size=28, color=self.C_PRIMARY, weight=BOLD),
            Text("   |   ", font="PingFang SC", font_size=28, color=self.C_AUX),
            Text("0.4×5=2", font="PingFang SC", font_size=28, color=self.C_PRIMARY, weight=BOLD),
            Text("   |   ", font="PingFang SC", font_size=28, color=self.C_AUX),
            Text("0.25×4=1", font="PingFang SC", font_size=28, color=self.C_PRIMARY, weight=BOLD),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.3)

        self.play(FadeIn(ex_row, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)

        # 核心记忆点
        core_bg = RoundedRectangle(
            corner_radius=0.3,
            width=8.0,
            height=1.3,
            fill_color="#1a3a1a",
            fill_opacity=1,
            stroke_color=self.C_INT,
            stroke_width=2.5
        ).move_to(DOWN * 2.4)
        core_text = VGroup(
            Text("因数几位小数 → 积就几位小数", font="PingFang SC", font_size=26, color=self.C_INT),
        ).move_to(DOWN * 2.4)

        self.play(FadeIn(core_bg), FadeIn(core_text), run_time=0.5)
        self.play(Indicate(core_text, color=YELLOW, scale_factor=1.06), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(sum_title), FadeOut(box_bg),
            *[FadeOut(c) for c in cards],
            FadeOut(divider),
            FadeOut(ex_row),
            FadeOut(core_bg), FadeOut(core_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────
    # Scene 8: 片尾关注
    # ─────────────────────────────────────────────────
    def scene_8_outro(self):
        # 总结句
        great_text = Text(
            "掌握这3步，小数乘法不怕啦！",
            font="PingFang SC",
            font_size=32,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(great_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=36,
            color=YELLOW,
            weight=BOLD
        ).move_to(UP * 3.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=self.C_AUX
        ).move_to(UP * 1.1)

        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.5)
        self.wait(0.4)

        # 公式快闪装饰
        formulas = VGroup(
            Text("0.3×5=1.5", font="PingFang SC", font_size=26, color=self.C_PRIMARY),
            Text("0.4×5=2", font="PingFang SC", font_size=26, color=self.C_INT),
            Text("0.25×4=1", font="PingFang SC", font_size=26, color=self.C_DOT),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 0.8)

        self.play(LaggedStart(
            *[FadeIn(f, shift=RIGHT * 0.3) for f in formulas],
            lag_ratio=0.2
        ), run_time=0.8)
        self.wait(0.5)

        # 装饰星星
        stars = VGroup(*[
            Text("★", font_size=28, color=YELLOW)
            .move_to(follow_text.get_center() + 3.5 * np.array([
                np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0
            ]))
            for i in range(6)
        ])
        self.play(
            LaggedStart(*[FadeIn(s, scale=0.3) for s in stars], lag_ratio=0.1),
            run_time=0.7
        )
        self.play(Rotate(stars, angle=TAU / 6, run_time=1.2))
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(great_text),
            FadeOut(follow_text),
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(formulas),
            FadeOut(stars),
            FadeOut(self.author),
            run_time=1.0
        )

    # ─────────────────────────────────────────────────
    # Helper methods
    # ─────────────────────────────────────────────────
    def _make_step_badge(self, text_str, color, font_size=28):
        """创建步骤徽章"""
        pill = RoundedRectangle(
            corner_radius=0.3,
            width=2.8,
            height=0.75,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        label = Text(text_str, font="PingFang SC", font_size=font_size, color=WHITE, weight=BOLD)
        return VGroup(pill, label)

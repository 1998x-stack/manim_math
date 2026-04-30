"""
大小比较 - 比较100以内数的大小
一年级下册 第二章 100以内数的认识

知识点: 比较两位数大小：先比十位，十位相同再比个位
目标受众: 一年级小学生
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


class NumberSizeComparison(Scene):
    """
    大小比较教学动画

    场景顺序:
    1. 开场钩子 - 引出问题
    2. 认识位值 - 十位与个位
    3. 例题1: 45 vs 38 (十位不同)
    4. 例题2: 56 vs 59 (十位相同，比个位)
    5. 总结规则
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_TENS = "#e74c3c"       # 红色 - 十位
        self.COLOR_ONES = "#3498db"       # 蓝色 - 个位
        self.COLOR_HIGHLIGHT = "#f1c40f"  # 黄色 - 高亮
        self.COLOR_GREATER = "#2ecc71"    # 绿色 - 较大
        self.COLOR_LESS = "#e67e22"       # 橙色 - 较小
        self.COLOR_RULE = "#9b59b6"       # 紫色 - 规则

        self.scene_1_opening()
        self.scene_2_place_value()
        self.scene_3_example1()
        self.scene_4_example2()
        self.scene_5_summary()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # 工具方法
    # ─────────────────────────────────────────────

    def make_number_box(self, digit_str, color, size=1.2):
        """创建数字方块"""
        box = RoundedRectangle(
            width=size, height=size,
            corner_radius=0.15,
            color=color,
            fill_color=color,
            fill_opacity=0.25,
            stroke_width=3,
        )
        label = Text(digit_str, font="PingFang SC", font_size=int(size * 44), color=color)
        return VGroup(box, label)

    def make_label(self, text_str, color=WHITE, font_size=26):
        return Text(text_str, font="PingFang SC", font_size=font_size, color=color)

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────

    def scene_1_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author

        # 大标题
        title = Text(
            "大小比较",
            font="PingFang SC",
            font_size=60,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)

        subtitle = Text(
            "谁大？谁小？",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 4.5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)

        # 展示两个数字引发思考
        num_45 = MathTex(r"45", font_size=120, color=self.COLOR_TENS).move_to(LEFT * 2 + UP * 2.5)
        num_38 = MathTex(r"38", font_size=120, color=self.COLOR_ONES).move_to(RIGHT * 2 + UP * 2.5)
        question_mark = Text("？", font="PingFang SC", font_size=80, color=self.COLOR_HIGHLIGHT).move_to(UP * 2.5)

        self.play(
            GrowFromCenter(num_45),
            GrowFromCenter(num_38),
            run_time=0.8,
        )
        self.play(FadeIn(question_mark, scale=1.3), run_time=0.5)
        self.wait(0.8)

        hook = Text(
            "怎么比？先看哪一位？",
            font="PingFang SC",
            font_size=30,
            color=WHITE,
        ).move_to(UP * 1.0)

        self.play(Write(hook), run_time=0.7)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(num_45),
            FadeOut(num_38),
            FadeOut(question_mark),
            FadeOut(hook),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 2: 认识位值
    # ─────────────────────────────────────────────

    def scene_2_place_value(self):
        section_title = Text(
            "认识十位和个位",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(section_title), run_time=0.6)

        # 以 45 为例展示位值
        num_label = Text(
            "以  45  为例",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A,
        ).move_to(UP * 4.5)
        self.play(FadeIn(num_label), run_time=0.4)

        # 大数字 45 居中
        num_big = MathTex(r"45", font_size=150, color=WHITE).move_to(UP * 2.8)
        self.play(GrowFromCenter(num_big), run_time=0.7)

        # 十位箭头
        tens_arrow = Arrow(
            start=LEFT * 1.5 + UP * 1.2,
            end=LEFT * 0.5 + UP * 2.35,
            color=self.COLOR_TENS,
            buff=0.05,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )
        tens_text = Text(
            "十位",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_TENS,
        ).move_to(LEFT * 2.2 + UP * 0.9)
        tens_val = Text(
            "= 4 个十",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TENS,
        ).move_to(LEFT * 2.2 + UP * 0.4)

        self.play(
            GrowArrow(tens_arrow),
            FadeIn(tens_text),
            run_time=0.6,
        )
        self.play(FadeIn(tens_val), run_time=0.4)

        # 个位箭头
        ones_arrow = Arrow(
            start=RIGHT * 1.5 + UP * 1.2,
            end=RIGHT * 0.45 + UP * 2.35,
            color=self.COLOR_ONES,
            buff=0.05,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )
        ones_text = Text(
            "个位",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_ONES,
        ).move_to(RIGHT * 2.2 + UP * 0.9)
        ones_val = Text(
            "= 5 个一",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_ONES,
        ).move_to(RIGHT * 2.2 + UP * 0.4)

        self.play(
            GrowArrow(ones_arrow),
            FadeIn(ones_text),
            run_time=0.6,
        )
        self.play(FadeIn(ones_val), run_time=0.4)

        self.wait(1.0)

        # 规则提示
        rule_box = RoundedRectangle(
            width=7.5, height=1.3,
            corner_radius=0.2,
            color=self.COLOR_RULE,
            fill_color=self.COLOR_RULE,
            fill_opacity=0.2,
            stroke_width=3,
        ).move_to(DOWN * 0.8)
        rule_text = Text(
            "先比十位，十位相同再比个位",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_RULE,
        ).move_to(DOWN * 0.8)

        self.play(Create(rule_box), run_time=0.5)
        self.play(Write(rule_text), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(section_title),
            FadeOut(num_label),
            FadeOut(num_big),
            FadeOut(tens_arrow),
            FadeOut(tens_text),
            FadeOut(tens_val),
            FadeOut(ones_arrow),
            FadeOut(ones_text),
            FadeOut(ones_val),
            FadeOut(rule_box),
            FadeOut(rule_text),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 3: 例题1 - 45 vs 38 (十位不同)
    # ─────────────────────────────────────────────

    def scene_3_example1(self):
        ex_title = Text(
            "例1：比较 45 和 38",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(ex_title), run_time=0.6)

        # 步骤1标题
        step1_label = Text(
            "第一步：看十位",
            font="PingFang SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 4.5)
        self.play(FadeIn(step1_label), run_time=0.4)

        # ── 构建 45 和 38 的数字块 ──
        # 45: 十位=4(红), 个位=5(灰)
        box_4 = self.make_number_box("4", self.COLOR_TENS, size=1.4)
        box_5 = self.make_number_box("5", "#7f8c8d", size=1.4)
        num_45 = VGroup(box_4, box_5).arrange(RIGHT, buff=0.12).move_to(LEFT * 2.2 + UP * 2.8)

        # 38: 十位=3(红), 个位=8(灰)
        box_3 = self.make_number_box("3", self.COLOR_TENS, size=1.4)
        box_8 = self.make_number_box("8", "#7f8c8d", size=1.4)
        num_38 = VGroup(box_3, box_8).arrange(RIGHT, buff=0.12).move_to(RIGHT * 2.2 + UP * 2.8)

        # 标注数字名称
        label_45 = Text("45", font="PingFang SC", font_size=28, color=WHITE).next_to(num_45, UP, buff=0.15)
        label_38 = Text("38", font="PingFang SC", font_size=28, color=WHITE).next_to(num_38, UP, buff=0.15)

        self.play(
            GrowFromCenter(num_45),
            GrowFromCenter(num_38),
            FadeIn(label_45),
            FadeIn(label_38),
            run_time=0.8,
        )

        # 十位对比行
        tens_row_label = Text(
            "十位：",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TENS,
        ).move_to(LEFT * 3.2 + UP * 1.1)

        tens_4 = Text("4", font="PingFang SC", font_size=52, color=self.COLOR_TENS).move_to(LEFT * 1.8 + UP * 1.1)
        vs_sym = Text("VS", font="PingFang SC", font_size=28, color=GRAY_A).move_to(UP * 1.1)
        tens_3 = Text("3", font="PingFang SC", font_size=52, color=self.COLOR_TENS).move_to(RIGHT * 1.8 + UP * 1.1)

        self.play(
            FadeIn(tens_row_label),
            FadeIn(tens_4),
            FadeIn(vs_sym),
            FadeIn(tens_3),
            run_time=0.7,
        )

        # 高亮十位方块
        self.play(
            Indicate(box_4, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            Indicate(box_3, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            run_time=0.9,
        )

        # 比较说明
        compare_text = Text(
            "4 > 3",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_GREATER,
        ).move_to(UP * 0.1)
        self.play(Write(compare_text), run_time=0.6)

        explain_1 = Text(
            "十位上 4 比 3 大",
            font="PingFang SC",
            font_size=26,
            color=WHITE,
        ).move_to(DOWN * 0.7)
        self.play(FadeIn(explain_1), run_time=0.5)
        self.wait(0.8)

        # 结论
        conclusion_box = RoundedRectangle(
            width=7.5, height=1.6,
            corner_radius=0.2,
            color=self.COLOR_GREATER,
            fill_color=self.COLOR_GREATER,
            fill_opacity=0.18,
            stroke_width=3,
        ).move_to(DOWN * 2.2)

        conc_formula = VGroup(
            MathTex(r"45", font_size=56, color=self.COLOR_GREATER),
            MathTex(r">", font_size=56, color=WHITE),
            MathTex(r"38", font_size=56, color=self.COLOR_LESS),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.0)

        conc_reason = Text(
            "（十位 4 > 3，所以 45 > 38）",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 2.8)

        self.play(Create(conclusion_box), run_time=0.5)
        self.play(Write(conc_formula), run_time=0.6)
        self.play(FadeIn(conc_reason), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(ex_title),
            FadeOut(step1_label),
            FadeOut(num_45),
            FadeOut(num_38),
            FadeOut(label_45),
            FadeOut(label_38),
            FadeOut(tens_row_label),
            FadeOut(tens_4),
            FadeOut(vs_sym),
            FadeOut(tens_3),
            FadeOut(compare_text),
            FadeOut(explain_1),
            FadeOut(conclusion_box),
            FadeOut(conc_formula),
            FadeOut(conc_reason),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 4: 例题2 - 56 vs 59 (十位相同，比个位)
    # ─────────────────────────────────────────────

    def scene_4_example2(self):
        ex_title = Text(
            "例2：比较 56 和 59",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(ex_title), run_time=0.6)

        hint = Text(
            "十位相同时怎么办？",
            font="PingFang SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 4.5)
        self.play(FadeIn(hint), run_time=0.4)

        # 构建 56 和 59
        box_5a = self.make_number_box("5", self.COLOR_TENS, size=1.4)
        box_6 = self.make_number_box("6", self.COLOR_ONES, size=1.4)
        num_56 = VGroup(box_5a, box_6).arrange(RIGHT, buff=0.12).move_to(LEFT * 2.2 + UP * 2.8)

        box_5b = self.make_number_box("5", self.COLOR_TENS, size=1.4)
        box_9 = self.make_number_box("9", self.COLOR_ONES, size=1.4)
        num_59 = VGroup(box_5b, box_9).arrange(RIGHT, buff=0.12).move_to(RIGHT * 2.2 + UP * 2.8)

        label_56 = Text("56", font="PingFang SC", font_size=28, color=WHITE).next_to(num_56, UP, buff=0.15)
        label_59 = Text("59", font="PingFang SC", font_size=28, color=WHITE).next_to(num_59, UP, buff=0.15)

        self.play(
            GrowFromCenter(num_56),
            GrowFromCenter(num_59),
            FadeIn(label_56),
            FadeIn(label_59),
            run_time=0.8,
        )

        # Step1: 比十位
        step1 = Text(
            "第一步：看十位",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TENS,
        ).move_to(LEFT * 2.5 + UP * 1.2)

        tens_5a = Text("5", font="PingFang SC", font_size=52, color=self.COLOR_TENS).move_to(LEFT * 1.6 + UP * 1.2)
        eq_sym = MathTex(r"=", font_size=48, color=WHITE).move_to(UP * 1.2)
        tens_5b = Text("5", font="PingFang SC", font_size=52, color=self.COLOR_TENS).move_to(RIGHT * 1.6 + UP * 1.2)

        self.play(FadeIn(step1), run_time=0.4)
        self.play(
            Indicate(box_5a, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            Indicate(box_5b, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            FadeIn(tens_5a),
            FadeIn(eq_sym),
            FadeIn(tens_5b),
            run_time=0.8,
        )

        same_text = Text(
            "十位相同！5 = 5",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 0.3)
        self.play(Write(same_text), run_time=0.6)
        self.wait(0.6)

        # Step2: 比个位
        step2 = Text(
            "第二步：再看个位",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_ONES,
        ).move_to(RIGHT * 2.2 + UP * 1.2)

        self.play(FadeIn(step2), run_time=0.4)

        ones_6 = Text("6", font="PingFang SC", font_size=52, color=self.COLOR_ONES).move_to(LEFT * 1.6 + DOWN * 0.5)
        lt_sym = MathTex(r"<", font_size=48, color=WHITE).move_to(DOWN * 0.5)
        ones_9 = Text("9", font="PingFang SC", font_size=52, color=self.COLOR_ONES).move_to(RIGHT * 1.6 + DOWN * 0.5)

        self.play(
            Indicate(box_6, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            Indicate(box_9, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            FadeIn(ones_6),
            FadeIn(lt_sym),
            FadeIn(ones_9),
            run_time=0.8,
        )

        compare2 = Text(
            "个位 6 < 9",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_ONES,
        ).move_to(DOWN * 1.3)
        self.play(FadeIn(compare2), run_time=0.5)
        self.wait(0.8)

        # 结论
        conclusion_box2 = RoundedRectangle(
            width=7.5, height=1.6,
            corner_radius=0.2,
            color=self.COLOR_ONES,
            fill_color=self.COLOR_ONES,
            fill_opacity=0.18,
            stroke_width=3,
        ).move_to(DOWN * 2.8)

        conc_formula2 = VGroup(
            MathTex(r"56", font_size=56, color=self.COLOR_LESS),
            MathTex(r"<", font_size=56, color=WHITE),
            MathTex(r"59", font_size=56, color=self.COLOR_GREATER),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.6)

        conc_reason2 = Text(
            "（十位相同，个位 6 < 9，所以 56 < 59）",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A,
        ).move_to(DOWN * 3.4)

        self.play(Create(conclusion_box2), run_time=0.4)
        self.play(Write(conc_formula2), run_time=0.6)
        self.play(FadeIn(conc_reason2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(ex_title),
            FadeOut(hint),
            FadeOut(num_56),
            FadeOut(num_59),
            FadeOut(label_56),
            FadeOut(label_59),
            FadeOut(step1),
            FadeOut(tens_5a),
            FadeOut(eq_sym),
            FadeOut(tens_5b),
            FadeOut(same_text),
            FadeOut(step2),
            FadeOut(ones_6),
            FadeOut(lt_sym),
            FadeOut(ones_9),
            FadeOut(compare2),
            FadeOut(conclusion_box2),
            FadeOut(conc_formula2),
            FadeOut(conc_reason2),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 5: 总结规则
    # ─────────────────────────────────────────────

    def scene_5_summary(self):
        summary_title = Text(
            "比较大小的方法",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.6)

        # 规则卡片 1
        rule1_box = RoundedRectangle(
            width=7.8, height=1.6,
            corner_radius=0.2,
            color=self.COLOR_TENS,
            fill_color=self.COLOR_TENS,
            fill_opacity=0.18,
            stroke_width=3,
        ).move_to(UP * 3.8)

        rule1_num = Text("1", font="PingFang SC", font_size=36, color=self.COLOR_TENS).move_to(LEFT * 3.2 + UP * 3.8)
        rule1_text = Text(
            "先比十位",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TENS,
        ).move_to(UP * 4.0)
        rule1_sub = Text(
            "十位大的那个数就大",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 3.55)

        self.play(Create(rule1_box), run_time=0.4)
        self.play(FadeIn(rule1_num), Write(rule1_text), run_time=0.5)
        self.play(FadeIn(rule1_sub), run_time=0.4)

        # 示例 45 > 38
        ex1_45 = MathTex(r"45", font_size=48, color=self.COLOR_GREATER)
        ex1_gt = MathTex(r">", font_size=48, color=WHITE)
        ex1_38 = MathTex(r"38", font_size=48, color=self.COLOR_LESS)
        ex1_note = Text("  （4 > 3）", font="PingFang SC", font_size=24, color=GRAY_A)
        ex1_line = VGroup(ex1_45, ex1_gt, ex1_38, ex1_note).arrange(RIGHT, buff=0.2).move_to(UP * 2.5)
        self.play(FadeIn(ex1_line), run_time=0.5)
        self.wait(0.5)

        # 规则卡片 2
        rule2_box = RoundedRectangle(
            width=7.8, height=1.6,
            corner_radius=0.2,
            color=self.COLOR_ONES,
            fill_color=self.COLOR_ONES,
            fill_opacity=0.18,
            stroke_width=3,
        ).move_to(UP * 1.4)

        rule2_num = Text("2", font="PingFang SC", font_size=36, color=self.COLOR_ONES).move_to(LEFT * 3.2 + UP * 1.4)
        rule2_text = Text(
            "十位相同，再比个位",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_ONES,
        ).move_to(UP * 1.6)
        rule2_sub = Text(
            "个位大的那个数就大",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 1.15)

        self.play(Create(rule2_box), run_time=0.4)
        self.play(FadeIn(rule2_num), Write(rule2_text), run_time=0.5)
        self.play(FadeIn(rule2_sub), run_time=0.4)

        # 示例 56 < 59
        ex2_56 = MathTex(r"56", font_size=48, color=self.COLOR_LESS)
        ex2_lt = MathTex(r"<", font_size=48, color=WHITE)
        ex2_59 = MathTex(r"59", font_size=48, color=self.COLOR_GREATER)
        ex2_note = Text("  （5=5，6<9）", font="PingFang SC", font_size=24, color=GRAY_A)
        ex2_line = VGroup(ex2_56, ex2_lt, ex2_59, ex2_note).arrange(RIGHT, buff=0.2).move_to(UP * 0.1)
        self.play(FadeIn(ex2_line), run_time=0.5)
        self.wait(0.5)

        # 口诀
        mnemonic_box = RoundedRectangle(
            width=7.8, height=2.0,
            corner_radius=0.25,
            color=self.COLOR_RULE,
            fill_color=self.COLOR_RULE,
            fill_opacity=0.22,
            stroke_width=3,
        ).move_to(DOWN * 1.6)

        mnemonic_title = Text(
            "记忆口诀：",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_RULE,
        ).move_to(DOWN * 1.1)
        mnemonic_text = Text(
            "十位不同比十位，十位相同比个位",
            font="PingFang SC",
            font_size=26,
            color=WHITE,
        ).move_to(DOWN * 1.7)

        self.play(Create(mnemonic_box), run_time=0.5)
        self.play(FadeIn(mnemonic_title), Write(mnemonic_text), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(summary_title),
            FadeOut(rule1_box),
            FadeOut(rule1_num),
            FadeOut(rule1_text),
            FadeOut(rule1_sub),
            FadeOut(ex1_line),
            FadeOut(rule2_box),
            FadeOut(rule2_num),
            FadeOut(rule2_text),
            FadeOut(rule2_sub),
            FadeOut(ex2_line),
            FadeOut(mnemonic_box),
            FadeOut(mnemonic_title),
            FadeOut(mnemonic_text),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 6: 片尾
    # ─────────────────────────────────────────────

    def scene_6_outro(self):
        # 作者名字放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color="#6b7280",
        ).move_to(UP * 0.7)

        self.play(
            Transform(self.author, author_big),
            run_time=0.6,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我，学更多数学知识！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)

        # 装饰：小不等号符号飘入
        symbols = VGroup()
        positions = [
            LEFT * 2.5 + DOWN * 1.8,
            LEFT * 0.8 + DOWN * 2.3,
            RIGHT * 0.8 + DOWN * 1.8,
            RIGHT * 2.5 + DOWN * 2.3,
        ]
        syms = [">", "<", ">", "<"]
        colors = [self.COLOR_GREATER, self.COLOR_LESS, self.COLOR_GREATER, self.COLOR_LESS]

        for pos, sym, col in zip(positions, syms, colors):
            s = MathTex(sym, font_size=48, color=col).move_to(pos)
            symbols.add(s)

        self.play(
            *[FadeIn(s, scale=0.5) for s in symbols],
            run_time=0.7,
        )

        # 口诀再现
        final_rule = Text(
            "十位不同比十位，十位相同比个位",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(final_rule), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            FadeOut(final_rule),
            run_time=0.8,
        )

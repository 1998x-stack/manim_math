"""
10以内的口算 - Mental Math within 10
一年级上册 第二章 10以内数的加减法

内容: 利用数的分与合进行10以内的加减法口算
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


class MentalMathWithinTen(Scene):
    """
    10以内的口算教学动画

    场景顺序:
    1. 开场 - 钩子问题
    2. 分与合的概念
    3. 加法示例: 5 + 3 = 8
    4. 减法示例: 9 - 4 = 5
    5. 口算练习展示
    6. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色
        self.COLOR_ADDITION = "#3498db"      # 蓝色 - 加法
        self.COLOR_SUBTRACTION = "#e74c3c"   # 红色 - 减法
        self.COLOR_HIGHLIGHT = "#f1c40f"     # 黄色 - 高亮
        self.COLOR_SPLIT = "#2ecc71"         # 绿色 - 分与合
        self.COLOR_RESULT = "#e67e22"        # 橙色 - 结果
        self.COLOR_DOT_1 = "#3498db"
        self.COLOR_DOT_2 = "#e74c3c"

        self.scene_1_opening()
        self.scene_2_split_and_combine()
        self.scene_3_addition_example()
        self.scene_4_subtraction_example()
        self.scene_5_practice()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "10以内的口算",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        subtitle = Text(
            "脱口而出，轻松搞定！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 4.5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(0.3)

        # 钩子问题框
        question_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.8,
            color="#16213e",
            fill_color="#16213e",
            fill_opacity=1
        ).move_to(UP * 2.2)

        question_line1 = Text(
            "你能一眼算出来吗？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2.8)

        q1 = MathTex(r"5 + 3 = ?", font_size=54, color=self.COLOR_ADDITION).move_to(UP * 2.0)
        q2 = MathTex(r"9 - 4 = ?", font_size=54, color=self.COLOR_SUBTRACTION).move_to(UP * 1.2)

        self.play(FadeIn(question_bg, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(question_line1), run_time=0.4)
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.6)

        # 答案flash
        self.wait(0.5)
        self.play(Indicate(q1, color=self.COLOR_HIGHLIGHT, scale_factor=1.15), run_time=0.5)
        self.play(Indicate(q2, color=self.COLOR_HIGHLIGHT, scale_factor=1.15), run_time=0.5)

        hint = Text(
            "用「分与合」的方法，轻松口算！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SPLIT
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(question_bg),
            FadeOut(question_line1),
            FadeOut(q1),
            FadeOut(q2),
            FadeOut(hint),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 2: 分与合的概念
    # ─────────────────────────────────────────────
    def scene_2_split_and_combine(self):
        title = Text(
            "什么是「分与合」？",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.8)

        self.play(Write(title), run_time=0.7)

        # 用数字8演示分与合
        num_8 = Text("8", font="Noto Sans CJK SC", font_size=80, color=WHITE).move_to(UP * 4.0)
        self.play(FadeIn(num_8, scale=0.5), run_time=0.5)
        self.play(Flash(num_8, color=self.COLOR_HIGHLIGHT, flash_radius=0.6), run_time=0.4)

        # "可以分成" 文字
        can_split = Text(
            "可以分成",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 3.0)
        self.play(FadeIn(can_split), run_time=0.4)

        # 分解图：8 = 5 + 3
        left_num = Text("5", font="Noto Sans CJK SC", font_size=72, color=self.COLOR_ADDITION).move_to(
            UP * 1.8 + LEFT * 2.0)
        right_num = Text("3", font="Noto Sans CJK SC", font_size=72, color=self.COLOR_SUBTRACTION).move_to(
            UP * 1.8 + RIGHT * 2.0)
        and_text = Text("和", font="Noto Sans CJK SC", font_size=36, color=GRAY_A).move_to(UP * 1.8)

        # 箭头：从8分向5和3
        arrow_left = Arrow(
            start=num_8.get_bottom() + DOWN * 0.1,
            end=left_num.get_top() + UP * 0.1,
            color=self.COLOR_ADDITION,
            buff=0.1,
            stroke_width=3
        )
        arrow_right = Arrow(
            start=num_8.get_bottom() + DOWN * 0.1,
            end=right_num.get_top() + UP * 0.1,
            color=self.COLOR_SUBTRACTION,
            buff=0.1,
            stroke_width=3
        )

        self.play(GrowArrow(arrow_left), GrowArrow(arrow_right), run_time=0.7)
        self.play(
            FadeIn(left_num, shift=DOWN * 0.3),
            FadeIn(and_text),
            FadeIn(right_num, shift=DOWN * 0.3),
            run_time=0.6
        )

        # 合的方向
        self.wait(0.5)
        combine_text = Text(
            "也可以合在一起",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 0.6)
        self.play(FadeIn(combine_text), run_time=0.4)

        formula_combine = MathTex(r"5 + 3 = 8", font_size=56, color=self.COLOR_SPLIT).move_to(DOWN * 0.3)
        self.play(Write(formula_combine), run_time=0.7)
        self.play(Indicate(formula_combine, color=self.COLOR_HIGHLIGHT, scale_factor=1.1), run_time=0.5)
        self.wait(0.5)

        # 展示8的各种分法
        split_title = Text(
            "8的分与合：",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)

        splits = VGroup(
            MathTex(r"8 = 1 + 7", font_size=30, color=GRAY_A),
            MathTex(r"8 = 2 + 6", font_size=30, color=GRAY_A),
            MathTex(r"8 = 3 + 5", font_size=30, color=GRAY_A),
            MathTex(r"8 = 4 + 4", font_size=30, color=GRAY_A),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.0)

        self.play(FadeIn(split_title), run_time=0.4)
        for s in splits:
            self.play(FadeIn(s, shift=LEFT * 0.2), run_time=0.25)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(num_8),
            FadeOut(can_split),
            FadeOut(left_num),
            FadeOut(and_text),
            FadeOut(right_num),
            FadeOut(arrow_left),
            FadeOut(arrow_right),
            FadeOut(combine_text),
            FadeOut(formula_combine),
            FadeOut(split_title),
            FadeOut(splits),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 3: 加法示例 5 + 3 = 8
    # ─────────────────────────────────────────────
    def scene_3_addition_example(self):
        scene_label = Text(
            "加法口算",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ADDITION
        ).move_to(UP * 6.5)
        self.play(FadeIn(scene_label, shift=DOWN * 0.2), run_time=0.4)

        problem = MathTex(r"5 + 3 = ?", font_size=72, color=WHITE).move_to(UP * 5.2)
        self.play(Write(problem), run_time=0.7)

        think_text = Text(
            "想：5和3能组成几？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.1)
        self.play(FadeIn(think_text, shift=UP * 0.2), run_time=0.5)

        # ── 用圆点直观展示 ──
        dots_5 = VGroup(*[
            Dot(radius=0.22, color=self.COLOR_DOT_1, fill_opacity=1)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.18).move_to(UP * 2.8 + LEFT * 2.2)

        dots_3 = VGroup(*[
            Dot(radius=0.22, color=self.COLOR_DOT_2, fill_opacity=1)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.18).move_to(UP * 2.8 + RIGHT * 1.6)

        label_5 = Text("5", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_DOT_1).move_to(
            UP * 2.0 + LEFT * 2.2)
        label_plus = MathTex(r"+", font_size=44, color=WHITE).move_to(UP * 2.0 + LEFT * 0.3)
        label_3 = Text("3", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_DOT_2).move_to(
            UP * 2.0 + RIGHT * 1.6)

        line_5 = Line(LEFT * 0.6, RIGHT * 0.6, color=self.COLOR_DOT_1).next_to(label_5, DOWN, buff=0.08)
        line_3 = Line(LEFT * 0.4, RIGHT * 0.4, color=self.COLOR_DOT_2).next_to(label_3, DOWN, buff=0.08)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots_5], lag_ratio=0.12),
            run_time=0.7
        )
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots_3], lag_ratio=0.12),
            run_time=0.5
        )
        self.play(
            FadeIn(label_5),
            FadeIn(label_plus),
            FadeIn(label_3),
            FadeIn(line_5),
            FadeIn(line_3),
            run_time=0.5
        )

        # 合并动画：3个红点移向5个蓝点
        self.wait(0.4)
        merge_label = Text(
            "把3个合进来…",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.1)
        self.play(FadeIn(merge_label), run_time=0.4)

        # 目标位置：合并后8个点排列
        all_8_positions = []
        start_x = -3.2
        for i in range(8):
            all_8_positions.append(np.array([start_x + i * 0.58, 0.2, 0]))

        # 蓝点移到前5个位置，红点移到后3个位置
        animations = []
        for i, dot in enumerate(dots_5):
            animations.append(dot.animate.move_to(all_8_positions[i]))
        for j, dot in enumerate(dots_3):
            animations.append(dot.animate.move_to(all_8_positions[5 + j]).set_color(self.COLOR_SPLIT))
        self.play(
            *animations,
            FadeOut(label_5),
            FadeOut(label_plus),
            FadeOut(label_3),
            FadeOut(line_5),
            FadeOut(line_3),
            run_time=1.0
        )

        # 数数：用序号标注
        count_labels = VGroup()
        for i in range(8):
            lbl = Text(str(i + 1), font="Noto Sans CJK SC", font_size=20, color=self.COLOR_HIGHLIGHT)
            lbl.move_to(all_8_positions[i] + DOWN * 0.5)
            count_labels.add(lbl)

        for lbl in count_labels:
            self.play(FadeIn(lbl, scale=0.6), run_time=0.1)

        self.wait(0.3)

        # 答案揭晓
        self.play(FadeOut(merge_label), run_time=0.2)

        result_formula = MathTex(r"5 + 3 = 8", font_size=72, color=self.COLOR_RESULT).move_to(DOWN * 1.2)

        self.play(FadeOut(count_labels), run_time=0.3)
        self.play(problem.animate.set_color(GRAY_B), run_time=0.3)
        self.play(Write(result_formula), run_time=0.7)
        self.play(Flash(result_formula, color=self.COLOR_RESULT, flash_radius=1.2), run_time=0.5)

        # 口诀提示
        tip_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.5,
            fill_color="#0f3460",
            fill_opacity=1,
            color=self.COLOR_ADDITION
        ).move_to(DOWN * 2.5)
        tip_text = Text(
            "想：5和3合起来是8",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(tip_bg), FadeIn(tip_text), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(scene_label),
            FadeOut(problem),
            FadeOut(think_text),
            FadeOut(dots_5),
            FadeOut(dots_3),
            FadeOut(result_formula),
            FadeOut(tip_bg),
            FadeOut(tip_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 4: 减法示例 9 - 4 = 5
    # ─────────────────────────────────────────────
    def scene_4_subtraction_example(self):
        scene_label = Text(
            "减法口算",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_SUBTRACTION
        ).move_to(UP * 6.5)
        self.play(FadeIn(scene_label, shift=DOWN * 0.2), run_time=0.4)

        problem = MathTex(r"9 - 4 = ?", font_size=72, color=WHITE).move_to(UP * 5.2)
        self.play(Write(problem), run_time=0.7)

        think_text = Text(
            "想：9可以分成4和几？",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.1)
        self.play(FadeIn(think_text, shift=UP * 0.2), run_time=0.5)

        # ── 分解图 ──
        big_9 = Text("9", font="Noto Sans CJK SC", font_size=90, color=WHITE).move_to(UP * 2.7)
        self.play(FadeIn(big_9, scale=0.5), run_time=0.5)

        split_label = Text(
            "分成",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 1.8)
        self.play(FadeIn(split_label), run_time=0.3)

        # 分成4和5
        num_4 = Text("4", font="Noto Sans CJK SC", font_size=72, color=self.COLOR_SUBTRACTION).move_to(
            UP * 0.9 + LEFT * 2.0)
        and_text = Text("和", font="Noto Sans CJK SC", font_size=32, color=GRAY_A).move_to(UP * 0.9)
        num_5 = Text("5", font="Noto Sans CJK SC", font_size=72, color=self.COLOR_SPLIT).move_to(
            UP * 0.9 + RIGHT * 2.0)

        arrow_4 = Arrow(
            start=big_9.get_bottom() + DOWN * 0.05,
            end=num_4.get_top() + UP * 0.1,
            color=self.COLOR_SUBTRACTION,
            buff=0.1,
            stroke_width=3
        )
        arrow_5 = Arrow(
            start=big_9.get_bottom() + DOWN * 0.05,
            end=num_5.get_top() + UP * 0.1,
            color=self.COLOR_SPLIT,
            buff=0.1,
            stroke_width=3
        )

        self.play(GrowArrow(arrow_4), GrowArrow(arrow_5), run_time=0.6)
        self.play(
            FadeIn(num_4, shift=DOWN * 0.3),
            FadeIn(and_text),
            FadeIn(num_5, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.wait(0.4)

        # 减去4，剩下5
        cross_4 = Cross(num_4, color=RED, stroke_width=4)
        remove_text = Text(
            "去掉4，剩下…",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(remove_text), run_time=0.4)
        self.play(Create(cross_4), run_time=0.5)
        self.play(Indicate(num_5, color=self.COLOR_HIGHLIGHT, scale_factor=1.3), run_time=0.6)

        # 答案
        result_formula = MathTex(r"9 - 4 = 5", font_size=72, color=self.COLOR_RESULT).move_to(DOWN * 1.5)
        self.play(Write(result_formula), run_time=0.7)
        self.play(Flash(result_formula, color=self.COLOR_RESULT, flash_radius=1.2), run_time=0.5)

        # 口诀提示
        tip_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.5,
            fill_color="#3b0a0a",
            fill_opacity=1,
            color=self.COLOR_SUBTRACTION
        ).move_to(DOWN * 3.0)
        tip_text = Text(
            "想：9分成4和5，去掉4剩5",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(tip_bg), FadeIn(tip_text), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(scene_label),
            FadeOut(problem),
            FadeOut(think_text),
            FadeOut(big_9),
            FadeOut(split_label),
            FadeOut(num_4),
            FadeOut(and_text),
            FadeOut(num_5),
            FadeOut(arrow_4),
            FadeOut(arrow_5),
            FadeOut(cross_4),
            FadeOut(remove_text),
            FadeOut(result_formula),
            FadeOut(tip_bg),
            FadeOut(tip_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 5: 口算练习
    # ─────────────────────────────────────────────
    def scene_5_practice(self):
        title = Text(
            "来练一练！",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 练习题列表
        exercises = [
            (r"3 + 4 = ?", r"3 + 4 = 7", "想: 3和4合成7", self.COLOR_ADDITION),
            (r"8 - 3 = ?", r"8 - 3 = 5", "想: 8分成3和5", self.COLOR_SUBTRACTION),
            (r"6 + 2 = ?", r"6 + 2 = 8", "想: 6和2合成8", self.COLOR_ADDITION),
            (r"7 - 5 = ?", r"7 - 5 = 2", "想: 7分成5和2", self.COLOR_SUBTRACTION),
        ]

        positions = [UP * 4.5, UP * 2.5, UP * 0.5, DOWN * 1.5]

        # 先展示所有问题
        q_texes = []
        for i, (q, ans, hint, color) in enumerate(exercises):
            q_tex = MathTex(q, font_size=52, color=color).move_to(positions[i])
            q_texes.append(q_tex)
            self.play(FadeIn(q_tex, shift=LEFT * 0.3), run_time=0.35)

        self.wait(0.6)

        # 逐一揭示答案
        for i, (q, ans, hint, color) in enumerate(exercises):
            q_tex = q_texes[i]
            hint_text = Text(
                hint,
                font="Noto Sans CJK SC",
                font_size=20,
                color=GRAY_A
            ).next_to(q_tex, RIGHT, buff=0.4)
            self.play(FadeIn(hint_text, shift=LEFT * 0.2), run_time=0.3)

            ans_tex = MathTex(ans, font_size=52, color=color).move_to(positions[i])
            self.play(ReplacementTransform(q_tex, ans_tex), run_time=0.5)
            self.play(Flash(ans_tex, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.4)
            self.wait(0.2)
            self.play(FadeOut(hint_text), run_time=0.2)
            q_texes[i] = ans_tex

        self.wait(0.8)

        summary = Text(
            "多练习，就能脱口而出！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_SPLIT
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 清理所有
        fadeout_list = [title, summary] + q_texes
        self.play(*[FadeOut(mob) for mob in fadeout_list], run_time=0.5)

    # ─────────────────────────────────────────────
    # Scene 6: 片尾总结
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        summary_title = Text(
            "口算小秘诀",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.0)
        self.play(Write(summary_title), run_time=0.6)

        # 加法卡片
        card_add_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.2,
            fill_color="#0a1628",
            fill_opacity=1,
            color=self.COLOR_ADDITION,
            stroke_width=2
        ).move_to(UP * 3.0)

        card_add_title = Text(
            "加法：想「合」",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ADDITION
        ).move_to(UP * 3.4)

        card_add_ex1 = MathTex(r"5 + 3 =", font_size=28, color=WHITE)
        card_add_ex2 = Text("5和3合成8", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SPLIT)
        card_add_example = VGroup(card_add_ex1, card_add_ex2).arrange(RIGHT, buff=0.2).move_to(UP * 2.8)

        # 减法卡片
        card_sub_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.2,
            fill_color="#1a0a0a",
            fill_opacity=1,
            color=self.COLOR_SUBTRACTION,
            stroke_width=2
        ).move_to(UP * 0.5)

        card_sub_title = Text(
            "减法：想「分」",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SUBTRACTION
        ).move_to(UP * 0.9)

        card_sub_ex1 = MathTex(r"9 - 4 =", font_size=28, color=WHITE)
        card_sub_ex2 = Text("9分成4和5", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SPLIT)
        card_sub_example = VGroup(card_sub_ex1, card_sub_ex2).arrange(RIGHT, buff=0.2).move_to(UP * 0.3)

        self.play(FadeIn(card_add_bg), FadeIn(card_add_title), run_time=0.5)
        self.play(Write(card_add_example), run_time=0.5)

        self.play(FadeIn(card_sub_bg), FadeIn(card_sub_title), run_time=0.5)
        self.play(Write(card_sub_example), run_time=0.5)

        # 数轴演示 5+3=8
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=7.0,
            color=GRAY_B,
            include_numbers=True,
            font_size=24,
            numbers_with_elongated_ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ).move_to(DOWN * 1.8)

        self.play(Create(number_line), run_time=0.8)

        dot_start = Dot(number_line.n2p(5), color=self.COLOR_ADDITION, radius=0.14)
        dot_end = Dot(number_line.n2p(8), color=self.COLOR_RESULT, radius=0.14)
        arrow_on_line = Arrow(
            start=number_line.n2p(5) + UP * 0.35,
            end=number_line.n2p(8) + UP * 0.35,
            color=self.COLOR_ADDITION,
            buff=0.05,
            stroke_width=3
        )
        jump_label = Text("+3", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_ADDITION).move_to(
            number_line.n2p(6.5) + UP * 0.75
        )

        self.play(FadeIn(dot_start), run_time=0.3)
        self.play(GrowArrow(arrow_on_line), FadeIn(jump_label), run_time=0.6)
        self.play(FadeIn(dot_end), Flash(dot_end, color=self.COLOR_RESULT, flash_radius=0.4), run_time=0.5)
        self.wait(0.5)

        # 关注提示
        follow_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.2,
            fill_color="#16213e",
            fill_opacity=1,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 4.3)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.0)

        author_outro = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.7)

        self.play(FadeIn(follow_bg), FadeIn(follow_text), FadeIn(author_outro), run_time=0.6)
        self.play(Indicate(follow_text, color=WHITE, scale_factor=1.05), run_time=0.5)
        self.wait(1.5)

        # 全部淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)

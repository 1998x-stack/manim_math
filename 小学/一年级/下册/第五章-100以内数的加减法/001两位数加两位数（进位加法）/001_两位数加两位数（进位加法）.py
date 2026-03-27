"""
两位数加两位数（进位加法）- Manim 教学动画
知识点: 竖式计算 38 + 27 = 65，个位满十进一
年级: 一年级下册
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok 竖屏
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TwoDigitAdditionWithCarry(Scene):
    """
    两位数加两位数（进位加法）教学动画

    场景顺序:
    1. 开场钩子
    2. 引入问题 38 + 27 = ?
    3. 竖式建立
    4. 个位计算：8 + 7 = 15，写 5 进 1
    5. 十位计算：3 + 2 + 1 = 6
    6. 得出结果
    7. 总结口诀
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_TITLE = "#f9c74f"
        self.COLOR_TENS = "#4cc9f0"
        self.COLOR_ONES = "#f8961e"
        self.COLOR_CARRY = "#f94144"
        self.COLOR_RESULT = "#90be6d"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_BODY = WHITE
        self.COLOR_DIM = "#a8a8b3"

        self.scene_1_opening()
        self.scene_2_problem()
        self.scene_3_vertical_setup()
        self.scene_4_ones_calculation()
        self.scene_5_tens_calculation()
        self.scene_6_result()
        self.scene_7_summary()
        self.scene_8_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "你会算这道题吗？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.5)

        problem_display = MathTex(
            r"38 + 27 = ?",
            font_size=80,
            color=WHITE,
        ).move_to(UP * 3.5)

        self.play(Write(hook), run_time=0.6)
        self.play(FadeIn(problem_display, scale=0.8), run_time=0.8)
        self.wait(1.0)

        # 提示：进位！
        hint = Text(
            "个位满 10，要进位！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_CARRY,
        ).move_to(UP * 1.8)

        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(hook),
            FadeOut(problem_display),
            FadeOut(hint),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 2: 引入问题，数位分析
    # ─────────────────────────────────────────────
    def scene_2_problem(self):
        title = Text(
            "两位数加两位数",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.2)

        subtitle = Text(
            "进位加法",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DIM,
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 展示 38 + 27
        num_38 = MathTex(r"38", font_size=90, color=WHITE).move_to(UP * 4.0 + LEFT * 1.5)
        plus = MathTex(r"+", font_size=80, color=self.COLOR_DIM).move_to(UP * 4.0)
        num_27 = MathTex(r"27", font_size=90, color=WHITE).move_to(UP * 4.0 + RIGHT * 1.5)

        self.play(
            FadeIn(num_38, shift=RIGHT * 0.3),
            FadeIn(plus),
            FadeIn(num_27, shift=LEFT * 0.3),
            run_time=0.7,
        )
        self.wait(0.3)

        # 数位标注
        tens_label = Text(
            "十位",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_TENS,
        ).move_to(UP * 2.8 + LEFT * 1.5)

        ones_label = Text(
            "个位",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_ONES,
        ).move_to(UP * 2.8 + RIGHT * 1.5)

        self.play(
            FadeIn(tens_label),
            FadeIn(ones_label),
            run_time=0.5,
        )

        # 说明进位
        note = Text(
            "8 + 7 = 15，个位满 10 了！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_CARRY,
        ).move_to(UP * 1.5)

        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(num_38),
            FadeOut(plus),
            FadeOut(num_27),
            FadeOut(tens_label),
            FadeOut(ones_label),
            FadeOut(note),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 3: 建立竖式
    # ─────────────────────────────────────────────
    def scene_3_vertical_setup(self):
        title = Text(
            "用竖式来计算",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.5)

        # 布局常量
        COL_TENS_X = -0.6
        COL_ONES_X = 0.6
        ROW_HEADER_Y = 5.2
        ROW_38_Y = 4.2
        ROW_27_Y = 3.2
        ROW_LINE_Y = 2.65
        ROW_RESULT_Y = 2.0

        # 数位标题行
        col_tens = Text("十位", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_TENS)
        col_ones = Text("个位", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_ONES)
        col_tens.move_to(np.array([COL_TENS_X, ROW_HEADER_Y, 0]))
        col_ones.move_to(np.array([COL_ONES_X, ROW_HEADER_Y, 0]))

        self.play(FadeIn(col_tens), FadeIn(col_ones), run_time=0.4)

        # 38
        d_3 = MathTex(r"3", font_size=80, color=self.COLOR_TENS).move_to(np.array([COL_TENS_X, ROW_38_Y, 0]))
        d_8 = MathTex(r"8", font_size=80, color=self.COLOR_ONES).move_to(np.array([COL_ONES_X, ROW_38_Y, 0]))
        self.play(FadeIn(d_3), FadeIn(d_8), run_time=0.5)

        # 加号 + 27
        plus_sign = MathTex(r"+", font_size=70, color=self.COLOR_DIM).move_to(np.array([-1.5, ROW_27_Y, 0]))
        d_2 = MathTex(r"2", font_size=80, color=self.COLOR_TENS).move_to(np.array([COL_TENS_X, ROW_27_Y, 0]))
        d_7 = MathTex(r"7", font_size=80, color=self.COLOR_ONES).move_to(np.array([COL_ONES_X, ROW_27_Y, 0]))
        self.play(FadeIn(plus_sign), FadeIn(d_2), FadeIn(d_7), run_time=0.5)

        # 横线
        h_line = Line(
            np.array([-2.0, ROW_LINE_Y, 0]),
            np.array([1.2, ROW_LINE_Y, 0]),
            color=WHITE,
            stroke_width=3,
        )
        self.play(Create(h_line), run_time=0.4)
        self.wait(0.5)

        # 存储引用供后续场景使用
        self.layout = {
            "COL_TENS_X": COL_TENS_X,
            "COL_ONES_X": COL_ONES_X,
            "ROW_HEADER_Y": ROW_HEADER_Y,
            "ROW_38_Y": ROW_38_Y,
            "ROW_27_Y": ROW_27_Y,
            "ROW_LINE_Y": ROW_LINE_Y,
            "ROW_RESULT_Y": ROW_RESULT_Y,
        }
        self.vgroup_static = VGroup(
            title, col_tens, col_ones,
            d_3, d_8, plus_sign, d_2, d_7, h_line,
        )
        self.d_3 = d_3
        self.d_8 = d_8
        self.d_2 = d_2
        self.d_7 = d_7
        self.plus_sign = plus_sign
        self.h_line = h_line
        self.col_tens = col_tens
        self.col_ones = col_ones
        self.title_scene3 = title

    # ─────────────────────────────────────────────
    # Scene 4: 个位计算 8 + 7 = 15，写 5 进 1
    # ─────────────────────────────────────────────
    def scene_4_ones_calculation(self):
        L = self.layout

        # 高亮个位数字
        self.play(
            Indicate(self.d_8, color=self.COLOR_ONES, scale_factor=1.4),
            Indicate(self.d_7, color=self.COLOR_ONES, scale_factor=1.4),
            run_time=0.7,
        )

        # 说明文字区（底部）
        step_label = Text(
            "第一步：算个位",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ONES,
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(step_label, shift=UP * 0.2), run_time=0.4)

        # 个位算式
        ones_eq = VGroup(
            MathTex(r"8", font_size=60, color=self.COLOR_ONES),
            MathTex(r"+", font_size=54, color=WHITE),
            MathTex(r"7", font_size=60, color=self.COLOR_ONES),
            MathTex(r"=", font_size=54, color=WHITE),
            MathTex(r"15", font_size=60, color=self.COLOR_CARRY),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 2.6)

        self.play(Write(ones_eq), run_time=0.8)
        self.wait(0.5)

        # "满十进一" 说明
        carry_text = Text(
            "满 10 了！个位写 5，向十位进 1",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_CARRY,
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(carry_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 在竖式个位写 5
        result_5 = MathTex(r"5", font_size=80, color=self.COLOR_RESULT).move_to(
            np.array([L["COL_ONES_X"], L["ROW_RESULT_Y"], 0])
        )
        self.play(FadeIn(result_5, scale=0.6), run_time=0.5)

        # 进位 1：显示在十位上方，红色小字
        carry_1 = MathTex(r"1", font_size=44, color=self.COLOR_CARRY).move_to(
            np.array([L["COL_TENS_X"] + 0.05, L["ROW_38_Y"] + 0.82, 0])
        )
        carry_box = SurroundingRectangle(carry_1, color=self.COLOR_CARRY, buff=0.08, stroke_width=2, corner_radius=0.08)

        self.play(
            FadeIn(carry_1, scale=0.5),
            Create(carry_box),
            run_time=0.6,
        )
        self.wait(0.8)

        # 清理说明文字
        self.play(
            FadeOut(step_label),
            FadeOut(ones_eq),
            FadeOut(carry_text),
            run_time=0.4,
        )

        self.result_5 = result_5
        self.carry_1 = carry_1
        self.carry_box = carry_box

    # ─────────────────────────────────────────────
    # Scene 5: 十位计算 3 + 2 + 1 = 6
    # ─────────────────────────────────────────────
    def scene_5_tens_calculation(self):
        L = self.layout

        # 高亮十位数字 + 进位
        self.play(
            Indicate(self.d_3, color=self.COLOR_TENS, scale_factor=1.4),
            Indicate(self.d_2, color=self.COLOR_TENS, scale_factor=1.4),
            Indicate(self.carry_1, color=self.COLOR_CARRY, scale_factor=1.4),
            run_time=0.8,
        )

        step_label = Text(
            "第二步：算十位（别忘了进上来的 1！）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_TENS,
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(step_label, shift=UP * 0.2), run_time=0.5)

        # 十位算式：3 + 2 + 1 = 6
        tens_eq = VGroup(
            MathTex(r"3", font_size=60, color=self.COLOR_TENS),
            MathTex(r"+", font_size=54, color=WHITE),
            MathTex(r"2", font_size=60, color=self.COLOR_TENS),
            MathTex(r"+", font_size=54, color=WHITE),
            MathTex(r"1", font_size=60, color=self.COLOR_CARRY),
            MathTex(r"=", font_size=54, color=WHITE),
            MathTex(r"6", font_size=60, color=self.COLOR_RESULT),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.8)

        self.play(Write(tens_eq), run_time=1.0)
        self.wait(0.5)

        carry_note = Text(
            "3 + 2 + 进上来的 1 = 6",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_TENS,
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(carry_note), run_time=0.4)
        self.wait(0.8)

        # 在竖式十位写 6
        result_6 = MathTex(r"6", font_size=80, color=self.COLOR_RESULT).move_to(
            np.array([L["COL_TENS_X"], L["ROW_RESULT_Y"], 0])
        )
        self.play(FadeIn(result_6, scale=0.6), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(step_label),
            FadeOut(tens_eq),
            FadeOut(carry_note),
            run_time=0.4,
        )

        self.result_6 = result_6

    # ─────────────────────────────────────────────
    # Scene 6: 完整结果展示
    # ─────────────────────────────────────────────
    def scene_6_result(self):
        L = self.layout

        # 闪烁结果
        result_group = VGroup(self.result_6, self.result_5)
        self.play(
            Indicate(result_group, color=self.COLOR_RESULT, scale_factor=1.3),
            run_time=0.8,
        )

        # 画一个圆框围住结果
        result_box = SurroundingRectangle(
            result_group,
            color=self.COLOR_RESULT,
            buff=0.18,
            stroke_width=3,
            corner_radius=0.12,
        )
        self.play(Create(result_box), run_time=0.5)
        self.wait(0.3)

        # 横式结果
        final_eq = VGroup(
            MathTex(r"38", font_size=72, color=WHITE),
            MathTex(r"+", font_size=64, color=self.COLOR_DIM),
            MathTex(r"27", font_size=72, color=WHITE),
            MathTex(r"=", font_size=64, color=self.COLOR_DIM),
            MathTex(r"65", font_size=80, color=self.COLOR_RESULT),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.0)

        self.play(Write(final_eq), run_time=0.9)
        self.wait(0.5)

        # 庆祝闪光
        self.play(
            Flash(
                final_eq[-1].get_center(),
                color=self.COLOR_RESULT,
                flash_radius=0.7,
                num_lines=12,
            ),
            run_time=0.6,
        )
        self.wait(1.0)

        self.final_eq = final_eq
        self.result_box = result_box

    # ─────────────────────────────────────────────
    # Scene 7: 总结口诀
    # ─────────────────────────────────────────────
    def scene_7_summary(self):
        # 淡出竖式
        self.play(
            FadeOut(self.vgroup_static),
            FadeOut(self.carry_1),
            FadeOut(self.carry_box),
            FadeOut(self.result_5),
            FadeOut(self.result_6),
            FadeOut(self.result_box),
            FadeOut(self.final_eq),
            run_time=0.5,
        )

        # 总结标题
        summary_title = Text(
            "进位加法口诀",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.5)

        self.play(Write(summary_title), run_time=0.6)

        # 四条口诀
        rule_texts = [
            "① 相同数位对齐",
            "② 从个位加起",
            "③ 个位满 10，向十位进 1",
            "④ 十位加时，不忘加进位！",
        ]
        rule_colors = [WHITE, self.COLOR_ONES, self.COLOR_CARRY, self.COLOR_TENS]

        rule_mobjects = []
        for text, color in zip(rule_texts, rule_colors):
            t = Text(text, font="Noto Sans CJK SC", font_size=28, color=color)
            rule_mobjects.append(t)

        rule_group = VGroup(*rule_mobjects)
        rule_group.arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(UP * 2.5)

        for rule in rule_group:
            self.play(FadeIn(rule, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        self.wait(0.5)

        # 再次展示算式过程
        example_title = Text(
            "回顾：38 + 27",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DIM,
        ).move_to(DOWN * 1.2)

        self.play(FadeIn(example_title), run_time=0.4)

        # 个位步骤行：文字 + 数学混合，用 VGroup 拼合
        ones_label_t = Text("个位：", font="Noto Sans CJK SC", font_size=26, color=self.COLOR_ONES)
        ones_formula = MathTex(r"8 + 7 = 15", font_size=52, color=WHITE)
        ones_write_t = Text("写", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        ones_5 = MathTex(r"5", font_size=52, color=self.COLOR_RESULT)
        ones_carry_t = Text("进", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        ones_1 = MathTex(r"1", font_size=52, color=self.COLOR_CARRY)

        step_ones = VGroup(
            ones_label_t, ones_formula, ones_write_t, ones_5, ones_carry_t, ones_1
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 2.3)

        # 十位步骤行
        tens_label_t = Text("十位：", font="Noto Sans CJK SC", font_size=26, color=self.COLOR_TENS)
        tens_formula = MathTex(r"3 + 2 + 1 = 6", font_size=52, color=WHITE)
        step_tens = VGroup(tens_label_t, tens_formula).arrange(RIGHT, buff=0.12).move_to(DOWN * 3.5)

        self.play(FadeIn(step_ones, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(step_tens, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)

        answer_part1 = MathTex(r"38 + 27 =", font_size=60, color=WHITE)
        answer_part2 = MathTex(r"65", font_size=72, color=self.COLOR_RESULT)
        answer_line = VGroup(answer_part1, answer_part2).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.8)

        self.play(Write(answer_line), run_time=0.7)
        self.play(
            Flash(answer_part2.get_center(), color=self.COLOR_RESULT, flash_radius=0.6),
            run_time=0.5,
        )
        self.wait(1.5)

        self.play(
            FadeOut(summary_title),
            FadeOut(rule_group),
            FadeOut(example_title),
            FadeOut(step_ones),
            FadeOut(step_tens),
            FadeOut(answer_line),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 8: 片尾
    # ─────────────────────────────────────────────
    def scene_8_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DIM,
        ).move_to(UP * 0.6)

        self.play(
            Transform(self.author, author_big),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_TITLE,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.2, scale=1.05), run_time=0.5)

        # 小装饰：数字彩虹
        nums = ["3", "8", "+", "2", "7", "=", "6", "5"]
        colors_dec = [
            self.COLOR_TENS, self.COLOR_ONES, WHITE,
            self.COLOR_TENS, self.COLOR_ONES, WHITE,
            self.COLOR_RESULT, self.COLOR_RESULT,
        ]
        deco_list = []
        for i, (n, c) in enumerate(zip(nums, colors_dec)):
            t = MathTex(n, font_size=36, color=c).move_to(
                DOWN * 2.2 + LEFT * 3.0 + RIGHT * i * 0.88
            )
            deco_list.append(t)
        decorations = VGroup(*deco_list)

        self.play(
            *[FadeIn(d, scale=0.5) for d in decorations],
            run_time=0.8,
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=0.8,
        )

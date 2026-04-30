"""
两位数减两位数（退位减法）- Two-digit Subtraction with Borrowing
小学一年级下册 第五章 100以内数的加减法

知识点：当个位不够减时，从十位借1当10，再做减法。
例：52 - 27 = 25

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


class TwoDigitSubtractionBorrow(Scene):
    """
    两位数减两位数（退位减法）教学动画

    场景顺序:
    1. 开场/题目引入
    2. 认识退位减法
    3. 个位不够减，从十位借1
    4. 竖式计算步骤
    5. 口诀总结
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_PRIMARY = "#4fc3f7"
        self.COLOR_TENS = "#ff8a65"
        self.COLOR_ONES = "#81c784"
        self.COLOR_BORROW = "#ef5350"
        self.COLOR_RESULT = "#ffd54f"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_TEXT = WHITE
        self.COLOR_SUB = "#b0bec5"

        # 执行场景
        self.scene_1_opening()
        self.scene_2_introduce_problem()
        self.scene_3_borrow_concept()
        self.scene_4_vertical_calculation()
        self.scene_5_summary()
        self.scene_6_outro()

    # --------------------------------------------------
    # 场景 1：开场
    # --------------------------------------------------
    def scene_1_opening(self):
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.4)

        title = Text(
            "退位减法",
            font="PingFang SC",
            font_size=64,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.0)

        subtitle = Text(
            "两位数减两位数",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_TEXT
        ).move_to(UP * 3.8)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)

        question = MathTex(
            r"52 - 27 = \, ?",
            font_size=72,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)

        self.play(Write(question), run_time=1.0)
        self.wait(0.4)

        hook = Text(
            "个位2不够减7，怎么办？",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_BORROW
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(question),
            FadeOut(hook),
            run_time=0.5
        )

    # --------------------------------------------------
    # 场景 2：引入问题，展示数的结构
    # --------------------------------------------------
    def scene_2_introduce_problem(self):
        scene_title = Text(
            "认识 52 和 27",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.8)
        self.play(Write(scene_title), run_time=0.5)

        # -- 52 的结构 --
        label_52 = Text("52", font="PingFang SC", font_size=60, color=self.COLOR_TEXT).move_to(UP * 4.2 + LEFT * 2.5)
        eq1 = Text("=", font="PingFang SC", font_size=50, color=self.COLOR_SUB).move_to(UP * 4.2 + LEFT * 0.9)
        tens_52 = Text("5个十", font="PingFang SC", font_size=32, color=self.COLOR_TENS).move_to(UP * 4.2 + RIGHT * 0.6)
        plus1 = Text("+", font="PingFang SC", font_size=40, color=self.COLOR_SUB).move_to(UP * 4.2 + RIGHT * 2.1)
        ones_52 = Text("2个一", font="PingFang SC", font_size=32, color=self.COLOR_ONES).move_to(UP * 4.2 + RIGHT * 3.4)

        self.play(Write(label_52), run_time=0.4)
        self.play(FadeIn(eq1), FadeIn(tens_52), FadeIn(plus1), FadeIn(ones_52), run_time=0.6)

        # -- 27 的结构 --
        label_27 = Text("27", font="PingFang SC", font_size=60, color=self.COLOR_TEXT).move_to(UP * 2.5 + LEFT * 2.5)
        eq2 = Text("=", font="PingFang SC", font_size=50, color=self.COLOR_SUB).move_to(UP * 2.5 + LEFT * 0.9)
        tens_27 = Text("2个十", font="PingFang SC", font_size=32, color=self.COLOR_TENS).move_to(UP * 2.5 + RIGHT * 0.6)
        plus2 = Text("+", font="PingFang SC", font_size=40, color=self.COLOR_SUB).move_to(UP * 2.5 + RIGHT * 2.1)
        ones_27 = Text("7个一", font="PingFang SC", font_size=32, color=self.COLOR_ONES).move_to(UP * 2.5 + RIGHT * 3.4)

        self.play(Write(label_27), run_time=0.4)
        self.play(FadeIn(eq2), FadeIn(tens_27), FadeIn(plus2), FadeIn(ones_27), run_time=0.6)

        # 问题发现
        prob_box = RoundedRectangle(
            corner_radius=0.2, width=7.5, height=1.3,
            color=self.COLOR_BORROW,
            fill_color=self.COLOR_BORROW, fill_opacity=0.12,
            stroke_width=2
        ).move_to(UP * 0.8)
        prob_txt = Text(
            "个位：2 < 7，不够减！",
            font="PingFang SC", font_size=34, color=self.COLOR_BORROW
        ).move_to(UP * 0.8)

        self.play(
            Indicate(ones_52, color=self.COLOR_BORROW, scale_factor=1.3),
            Indicate(ones_27, color=self.COLOR_BORROW, scale_factor=1.3),
            run_time=0.7
        )
        self.play(Create(prob_box), Write(prob_txt), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(scene_title),
            FadeOut(label_52), FadeOut(eq1), FadeOut(tens_52), FadeOut(plus1), FadeOut(ones_52),
            FadeOut(label_27), FadeOut(eq2), FadeOut(tens_27), FadeOut(plus2), FadeOut(ones_27),
            FadeOut(prob_box), FadeOut(prob_txt),
            run_time=0.5
        )

    # --------------------------------------------------
    # 场景 3：借位原理（破十法）
    # --------------------------------------------------
    def scene_3_borrow_concept(self):
        scene_title = Text(
            "退位减法的秘密",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        self.play(Write(scene_title), run_time=0.5)

        # 列标签
        tens_lbl = Text("十位", font="PingFang SC", font_size=26, color=self.COLOR_TENS).move_to(UP * 5.2 + LEFT * 1.5)
        ones_lbl = Text("个位", font="PingFang SC", font_size=26, color=self.COLOR_ONES).move_to(UP * 5.2 + RIGHT * 1.5)
        self.play(FadeIn(tens_lbl), FadeIn(ones_lbl), run_time=0.4)

        # 52 的十位和个位
        t5 = Text("5", font="PingFang SC", font_size=80, color=self.COLOR_TENS).move_to(UP * 3.8 + LEFT * 1.5)
        n2 = Text("2", font="PingFang SC", font_size=80, color=self.COLOR_ONES).move_to(UP * 3.8 + RIGHT * 1.5)
        self.play(Write(t5), Write(n2), run_time=0.5)

        # 说明：借位
        explain = Text(
            "个位2不够减7，向十位借1",
            font="PingFang SC", font_size=30, color=self.COLOR_BORROW
        ).move_to(UP * 2.3)
        self.play(Write(explain), run_time=0.6)

        # 借位箭头
        borrow_arrow = CurvedArrow(
            start_point=np.array([-1.8, 3.7, 0]),
            end_point=np.array([0.8, 4.0, 0]),
            color=self.COLOR_BORROW, stroke_width=5,
            angle=-TAU / 6
        )
        self.play(Create(borrow_arrow), run_time=0.5)

        # 5 -> 4，2 -> 12
        new_t4 = Text("4", font="PingFang SC", font_size=80, color=self.COLOR_TENS).move_to(UP * 3.8 + LEFT * 1.5)
        new_n12 = Text("12", font="PingFang SC", font_size=68, color=self.COLOR_ONES).move_to(UP * 3.8 + RIGHT * 1.5)

        self.play(Indicate(t5, color=self.COLOR_BORROW, scale_factor=1.2), run_time=0.4)
        self.play(
            ReplacementTransform(t5, new_t4),
            ReplacementTransform(n2, new_n12),
            run_time=0.7
        )
        self.wait(0.3)

        # 解释原理
        box1 = RoundedRectangle(
            corner_radius=0.15, width=7.2, height=1.1,
            color=self.COLOR_TENS, fill_color=self.COLOR_TENS, fill_opacity=0.10,
            stroke_width=1.5
        ).move_to(UP * 1.0)
        txt1 = Text(
            "1个十 = 10个一",
            font="PingFang SC", font_size=30, color=self.COLOR_TENS
        ).move_to(UP * 1.0)

        box2 = RoundedRectangle(
            corner_radius=0.15, width=7.2, height=1.1,
            color=self.COLOR_ONES, fill_color=self.COLOR_ONES, fill_opacity=0.10,
            stroke_width=1.5
        ).move_to(DOWN * 0.3)
        txt2 = Text(
            "2 + 10 = 12 个一",
            font="PingFang SC", font_size=30, color=self.COLOR_ONES
        ).move_to(DOWN * 0.3)

        self.play(Create(box1), Write(txt1), run_time=0.5)
        self.play(Create(box2), Write(txt2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(scene_title),
            FadeOut(tens_lbl), FadeOut(ones_lbl),
            FadeOut(new_t4), FadeOut(new_n12),
            FadeOut(explain), FadeOut(borrow_arrow),
            FadeOut(box1), FadeOut(txt1),
            FadeOut(box2), FadeOut(txt2),
            run_time=0.5
        )

    # --------------------------------------------------
    # 场景 4：竖式计算，逐步演示
    # --------------------------------------------------
    def scene_4_vertical_calculation(self):
        scene_title = Text(
            "竖式计算 52 - 27",
            font="PingFang SC",
            font_size=36, color=self.COLOR_PRIMARY
        ).move_to(UP * 6.8)
        self.play(Write(scene_title), run_time=0.5)

        # 位置参数
        row1_y = 4.8
        row2_y = 3.5
        row3_y = 2.0
        col_tens = -1.0
        col_ones = 1.0
        minus_x = -2.5

        # 列标签
        tens_lbl = Text("十位", font="PingFang SC", font_size=22, color=self.COLOR_TENS).move_to(
            np.array([col_tens, 6.0, 0])
        )
        ones_lbl = Text("个位", font="PingFang SC", font_size=22, color=self.COLOR_ONES).move_to(
            np.array([col_ones, 6.0, 0])
        )

        # 竖式数字
        d5 = Text("5", font="PingFang SC", font_size=70, color=self.COLOR_TENS).move_to(np.array([col_tens, row1_y, 0]))
        d2 = Text("2", font="PingFang SC", font_size=70, color=self.COLOR_ONES).move_to(np.array([col_ones, row1_y, 0]))
        d2b = Text("2", font="PingFang SC", font_size=70, color=self.COLOR_TENS).move_to(np.array([col_tens, row2_y, 0]))
        d7 = Text("7", font="PingFang SC", font_size=70, color=self.COLOR_ONES).move_to(np.array([col_ones, row2_y, 0]))
        minus_sign = Text("−", font="PingFang SC", font_size=64, color=self.COLOR_TEXT).move_to(
            np.array([minus_x, (row1_y + row2_y) / 2, 0])
        )
        h_line = Line(
            start=np.array([-2.8, row3_y + 0.55, 0]),
            end=np.array([2.2, row3_y + 0.55, 0]),
            color=WHITE, stroke_width=3
        )

        self.play(FadeIn(tens_lbl), FadeIn(ones_lbl), run_time=0.3)
        self.play(Write(d5), Write(d2), run_time=0.4)
        self.play(Write(minus_sign), Write(d2b), Write(d7), run_time=0.4)
        self.play(Create(h_line), run_time=0.3)
        self.wait(0.3)

        # STEP 1：个位 2 < 7，不够减
        step_bg = RoundedRectangle(
            corner_radius=0.2, width=7.5, height=1.4,
            color=self.COLOR_BORROW, fill_color=self.COLOR_BORROW,
            fill_opacity=0.12, stroke_width=2
        ).move_to(np.array([0, 0.5, 0]))
        step1_txt = Text(
            "第1步：个位 2 < 7，不够减！",
            font="PingFang SC", font_size=28, color=self.COLOR_BORROW
        ).move_to(np.array([0, 0.5, 0]))

        self.play(
            Indicate(d2, color=self.COLOR_BORROW, scale_factor=1.4),
            Indicate(d7, color=self.COLOR_BORROW, scale_factor=1.4),
            run_time=0.7
        )
        self.play(Create(step_bg), Write(step1_txt), run_time=0.6)
        self.wait(1.0)

        # STEP 2：向十位借 1
        cross_5 = Cross(d5, color=self.COLOR_BORROW, stroke_width=3)
        small_4 = Text(
            "4", font="PingFang SC", font_size=38, color=self.COLOR_BORROW
        ).move_to(np.array([col_tens + 0.2, row1_y + 0.7, 0]))
        small_12 = Text(
            "12", font="PingFang SC", font_size=34, color=self.COLOR_ONES
        ).move_to(np.array([col_ones + 0.25, row1_y + 0.7, 0]))
        borrow_arr = CurvedArrow(
            start_point=np.array([col_tens - 0.1, row1_y + 0.4, 0]),
            end_point=np.array([col_ones - 0.55, row1_y + 0.65, 0]),
            color=self.COLOR_BORROW, stroke_width=4, angle=-TAU / 6
        )

        step2_txt = Text(
            "第2步：十位借1给个位",
            font="PingFang SC", font_size=28, color=self.COLOR_BORROW
        ).move_to(np.array([0, 0.5, 0]))

        self.play(FadeOut(step1_txt), run_time=0.2)
        self.play(Create(cross_5), FadeIn(small_4), run_time=0.5)
        self.play(Create(borrow_arr), FadeIn(small_12), run_time=0.5)
        self.play(Write(step2_txt), run_time=0.4)
        self.wait(1.0)

        # STEP 3：个位 12 - 7 = 5
        step3_txt = Text(
            "第3步：个位 12 − 7 = 5",
            font="PingFang SC", font_size=28, color=self.COLOR_ONES
        ).move_to(np.array([0, 0.5, 0]))
        self.play(ReplacementTransform(step2_txt, step3_txt), run_time=0.4)

        calc_ones = Text(
            "12 − 7 = 5",
            font="PingFang SC", font_size=38, color=self.COLOR_ONES
        ).move_to(np.array([0, -0.6, 0]))
        self.play(Write(calc_ones), run_time=0.5)
        self.wait(0.5)

        result_ones = Text(
            "5", font="PingFang SC", font_size=70, color=self.COLOR_RESULT
        ).move_to(np.array([col_ones, row3_y, 0]))
        self.play(FadeIn(result_ones, shift=DOWN * 0.3), run_time=0.5)
        self.play(Indicate(result_ones, scale_factor=1.3, color=self.COLOR_RESULT), run_time=0.4)
        self.wait(0.5)

        # STEP 4：十位 4 - 2 = 2
        step4_txt = Text(
            "第4步：十位 4 − 2 = 2",
            font="PingFang SC", font_size=28, color=self.COLOR_TENS
        ).move_to(np.array([0, 0.5, 0]))
        self.play(ReplacementTransform(step3_txt, step4_txt), FadeOut(calc_ones), run_time=0.4)

        remind_txt = Text(
            "十位借出1后剩4个十",
            font="PingFang SC", font_size=26, color=self.COLOR_BORROW
        ).move_to(np.array([0, -0.5, 0]))
        self.play(FadeIn(remind_txt), run_time=0.4)

        calc_tens = Text(
            "4 − 2 = 2",
            font="PingFang SC", font_size=38, color=self.COLOR_TENS
        ).move_to(np.array([0, -1.4, 0]))
        self.play(Write(calc_tens), run_time=0.5)
        self.wait(0.4)

        result_tens = Text(
            "2", font="PingFang SC", font_size=70, color=self.COLOR_RESULT
        ).move_to(np.array([col_tens, row3_y, 0]))
        self.play(FadeIn(result_tens, shift=DOWN * 0.3), run_time=0.5)
        self.play(Indicate(result_tens, scale_factor=1.3, color=self.COLOR_RESULT), run_time=0.4)
        self.wait(0.6)

        # 淡出步骤说明，保留竖式
        self.play(
            FadeOut(step_bg), FadeOut(step4_txt),
            FadeOut(remind_txt), FadeOut(calc_tens),
            FadeOut(borrow_arr),
            run_time=0.4
        )

        # 最终答案框
        ans_box = RoundedRectangle(
            corner_radius=0.25, width=6.0, height=1.7,
            color=self.COLOR_RESULT, fill_color=self.COLOR_RESULT,
            fill_opacity=0.15, stroke_width=3
        ).move_to(np.array([0, -1.2, 0]))

        ans_grp = VGroup(
            Text("52 − 27 =", font="PingFang SC", font_size=42, color=self.COLOR_TEXT),
            Text("25", font="PingFang SC", font_size=58, color=self.COLOR_RESULT)
        ).arrange(RIGHT, buff=0.3).move_to(np.array([0, -1.2, 0]))

        self.play(Create(ans_box), run_time=0.4)
        self.play(Write(ans_grp), run_time=0.7)
        self.play(Flash(ans_grp[1], color=self.COLOR_RESULT, flash_radius=0.8), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(tens_lbl), FadeOut(ones_lbl),
            FadeOut(d5), FadeOut(d2),
            FadeOut(minus_sign), FadeOut(d2b), FadeOut(d7),
            FadeOut(h_line),
            FadeOut(cross_5), FadeOut(small_4), FadeOut(small_12),
            FadeOut(result_ones), FadeOut(result_tens),
            FadeOut(ans_box), FadeOut(ans_grp),
            run_time=0.6
        )

    # --------------------------------------------------
    # 场景 5：口诀总结
    # --------------------------------------------------
    def scene_5_summary(self):
        scene_title = Text(
            "退位减法 3 步口诀",
            font="PingFang SC",
            font_size=40, color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        self.play(Write(scene_title), run_time=0.5)

        steps_data = [
            ("①", "个位不够减", "向十位借 1", self.COLOR_BORROW),
            ("②", "个位加 10 再减", "12 − 7 = 5", self.COLOR_ONES),
            ("③", "十位减借走的 1", "4 − 2 = 2", self.COLOR_TENS),
        ]

        step_groups = []
        for i, (num, desc1, desc2, color) in enumerate(steps_data):
            y_pos = 4.5 - i * 2.3

            circle = Circle(radius=0.45, color=color, fill_color=color, fill_opacity=1).move_to(
                np.array([-3.8, y_pos, 0])
            )
            num_txt = Text(num, font="PingFang SC", font_size=26, color=WHITE).move_to(
                np.array([-3.8, y_pos, 0])
            )
            t1 = Text(desc1, font="PingFang SC", font_size=27, color=color).move_to(
                np.array([0.3, y_pos + 0.38, 0])
            )
            t2 = Text(desc2, font="PingFang SC", font_size=27, color=self.COLOR_TEXT).move_to(
                np.array([0.3, y_pos - 0.38, 0])
            )
            sep_line = Line(
                np.array([-2.8, y_pos - 0.8, 0]),
                np.array([3.8, y_pos - 0.8, 0]),
                color="#2d3561", stroke_width=1.5
            )

            grp = VGroup(circle, num_txt, t1, t2, sep_line)
            step_groups.append(grp)

            self.play(FadeIn(circle, scale=0.7), FadeIn(num_txt), run_time=0.3)
            self.play(Write(t1), Write(t2), run_time=0.5)
            self.play(Create(sep_line), run_time=0.2)
            self.wait(0.4)

        # 关键提醒
        remind_box = RoundedRectangle(
            corner_radius=0.2, width=7.5, height=1.6,
            color=self.COLOR_BORROW, fill_color=self.COLOR_BORROW,
            fill_opacity=0.12, stroke_width=2
        ).move_to(np.array([0, -3.6, 0]))

        remind_grp = VGroup(
            Text("记住！十位已借出1，", font="PingFang SC", font_size=26, color=self.COLOR_BORROW),
            Text("十位相减时要多减1", font="PingFang SC", font_size=26, color=self.COLOR_TEXT)
        ).arrange(DOWN, buff=0.12).move_to(np.array([0, -3.6, 0]))

        self.play(Create(remind_box), run_time=0.4)
        self.play(FadeIn(remind_grp, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        all_to_fade = [scene_title, remind_box, remind_grp] + step_groups
        self.play(*[FadeOut(o) for o in all_to_fade], run_time=0.6)

    # --------------------------------------------------
    # 场景 6：片尾
    # --------------------------------------------------
    def scene_6_outro(self):
        final_eq = MathTex(
            r"52 - 27 = 25",
            font_size=84,
            color=self.COLOR_RESULT
        ).move_to(UP * 2.5)
        self.play(Write(final_eq), run_time=1.0)
        self.play(Flash(final_eq, color=self.COLOR_RESULT, flash_radius=1.6), run_time=0.6)

        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38, color=WHITE
        ).move_to(UP * 0.5)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30, color="#6b7280"
        ).move_to(DOWN * 0.5)

        self.play(
            ReplacementTransform(self.author_info, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow_txt = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=32, color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(follow_txt, shift=UP * 0.3, scale=1.05), run_time=0.7)

        # 小装饰：星星
        stars = VGroup(*[
            Star(n=5, outer_radius=0.25, color=self.COLOR_RESULT, fill_opacity=0.9)
            .move_to(np.array([
                2.8 * np.cos(i * TAU / 6),
                -4.2 + 0.6 * np.sin(i * TAU / 6),
                0
            ]))
            for i in range(6)
        ])
        self.play(*[GrowFromCenter(s) for s in stars], run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(final_eq),
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow_txt),
            FadeOut(stars),
            run_time=1.0
        )

"""
数数与拐弯数 - 一年级下册 第二章
从20数到100，突破"拐弯数"（如19→20，29→30，……，99→100）
多种数法：一个一个地数，十个十个地数
TikTok竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CountingTurningNumbers(Scene):
    """
    数数与拐弯数教学动画

    场景顺序:
    1. 开场钩子
    2. 认识拐弯数概念
    3. 一个一个地数 (19->20, 29->30)
    4. 十个十个地数
    5. 10个十=100
    6. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_HIGHLIGHT = "#FFD700"   # 金黄色 - 拐弯数
        self.COLOR_NORMAL = "#A8D8EA"      # 淡蓝色 - 普通数
        self.COLOR_TEN = "#FF6B6B"         # 红色 - 整十数
        self.COLOR_ACCENT = "#98FF98"      # 淡绿色 - 强调
        self.COLOR_BG_CARD = "#16213e"     # 深蓝卡片背景

        self.scene_1_opening()
        self.scene_2_turning_concept()
        self.scene_3_count_one_by_one()
        self.scene_4_count_by_tens()
        self.scene_5_ten_tens()
        self.scene_6_outro()

    # -------------------------------------------------
    # Scene 1: 开场钩子
    # -------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.3)
        self.author = author

        # 钩子问题
        hook_line1 = Text(
            "数到19之后",
            font="PingFang SC",
            font_size=42,
            color=WHITE
        ).move_to(UP * 5.0)

        hook_line2 = Text(
            "下一个是几？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.2)

        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.7)
        self.wait(0.5)

        # 显示 19 -> ?
        num19 = Text("19", font="PingFang SC", font_size=80, color=self.COLOR_NORMAL)
        t_arrow = Text("->", font="PingFang SC", font_size=60, color=WHITE)
        question = Text("?", font="PingFang SC", font_size=80, color=self.COLOR_HIGHLIGHT)
        row = VGroup(num19, t_arrow, question).arrange(RIGHT, buff=0.4).move_to(UP * 2.5)

        self.play(FadeIn(num19, scale=0.8), run_time=0.4)
        self.play(FadeIn(t_arrow), run_time=0.2)
        self.play(FadeIn(question, scale=1.2), run_time=0.4)
        self.wait(0.5)

        # 答案揭晓
        answer = Text("20", font="PingFang SC", font_size=80, color=self.COLOR_HIGHLIGHT)
        answer.move_to(question.get_center())
        self.play(Transform(question, answer), run_time=0.6)
        self.wait(0.3)

        # 标题
        title = Text(
            "数数与拐弯数",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.2)

        subtitle = Text(
            "从20数到100",
            font="PingFang SC",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 0.4)

        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(row),
            FadeOut(question),
            run_time=0.4
        )
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.5
        )

    # -------------------------------------------------
    # Scene 2: 认识"拐弯数"概念
    # -------------------------------------------------
    def scene_2_turning_concept(self):
        # 场景标题
        scene_title = Text(
            "什么是拐弯数？",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        # 说明文字
        explain = Text(
            "数数时需要拐弯的数",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.4)
        self.play(FadeIn(explain), run_time=0.4)

        # 展示数列: 18, 19, [20], 21, 22
        numbers_data = [
            ("18", self.COLOR_NORMAL),
            ("19", self.COLOR_NORMAL),
            ("20", self.COLOR_TEN),
            ("21", self.COLOR_NORMAL),
            ("22", self.COLOR_NORMAL),
        ]

        num_objs = []
        for val, color in numbers_data:
            t = Text(val, font="PingFang SC", font_size=50, color=color)
            num_objs.append(t)

        row1 = VGroup(*num_objs).arrange(RIGHT, buff=0.35).move_to(UP * 3.8)
        self.play(FadeIn(row1, shift=UP * 0.3), run_time=0.6)

        # 箭头指向20
        arrow_down = Arrow(
            start=num_objs[2].get_center() + UP * 0.8,
            end=num_objs[2].get_center() + UP * 0.25,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4,
            tip_length=0.2
        )

        label_turn = Text(
            "拐弯！",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_down, UP, buff=0.05)

        self.play(GrowArrow(arrow_down), run_time=0.4)
        self.play(Write(label_turn), run_time=0.4)
        self.wait(0.4)

        # 闪烁效果
        self.play(Indicate(num_objs[2], color=self.COLOR_HIGHLIGHT, scale_factor=1.3), run_time=0.5)
        self.wait(0.3)

        # 展示更多拐弯数
        turning_title = Text(
            "所有的拐弯数：",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 2.6)
        self.play(FadeIn(turning_title), run_time=0.4)

        # 拐弯数列表
        turning_nums_list = ["20", "30", "40", "50", "60", "70", "80", "90", "100"]
        tn_objs = []
        for n in turning_nums_list:
            color = self.COLOR_HIGHLIGHT if n == "100" else self.COLOR_TEN
            t = Text(n, font="PingFang SC", font_size=34, color=color)
            tn_objs.append(t)

        # 分两行排列
        row_a = VGroup(*tn_objs[:5]).arrange(RIGHT, buff=0.25).move_to(UP * 1.9)
        row_b = VGroup(*tn_objs[5:]).arrange(RIGHT, buff=0.25).move_to(UP * 1.2)

        self.play(
            *[FadeIn(t, scale=0.8) for t in tn_objs[:5]],
            run_time=0.7
        )
        self.play(
            *[FadeIn(t, scale=0.8) for t in tn_objs[5:]],
            run_time=0.7
        )
        self.wait(0.3)

        # 共同特点说明
        feature_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.0,
            color=self.COLOR_TEN,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.8,
            stroke_width=2
        ).move_to(UP * 0.1)

        feature_text = Text(
            "个位都是 0，即整十数",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TEN
        ).move_to(UP * 0.1)

        self.play(Create(feature_box), run_time=0.4)
        self.play(Write(feature_text), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(explain),
            FadeOut(row1),
            FadeOut(arrow_down),
            FadeOut(label_turn),
            FadeOut(turning_title),
            FadeOut(row_a),
            FadeOut(row_b),
            FadeOut(feature_box),
            FadeOut(feature_text),
            run_time=0.5
        )

    # -------------------------------------------------
    # Scene 3: 一个一个地数
    # -------------------------------------------------
    def scene_3_count_one_by_one(self):
        # 场景标题
        scene_title = Text(
            "一个一个地数",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_ACCENT
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        # 第一个拐弯：19 -> 20
        turning_label1 = Text(
            "第一个拐弯",
            font="PingFang SC",
            font_size=22,
            color=GRAY_B
        ).move_to(UP * 5.2)
        self.play(FadeIn(turning_label1), run_time=0.3)

        t19 = Text("19", font="PingFang SC", font_size=72, color=self.COLOR_NORMAL)
        arr1 = Text("->", font="PingFang SC", font_size=56, color=WHITE)
        t20 = Text("20", font="PingFang SC", font_size=72, color=self.COLOR_TEN)
        group1 = VGroup(t19, arr1, t20).arrange(RIGHT, buff=0.35).move_to(UP * 4.3)

        self.play(FadeIn(t19, scale=0.8), run_time=0.4)
        self.play(FadeIn(arr1), run_time=0.2)
        self.play(FadeIn(t20, scale=1.3), run_time=0.5)
        self.play(Indicate(t20, color=self.COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.4)
        self.wait(0.3)

        # 从17数到23的序列
        seq1_nums = [str(i) for i in range(17, 24)]
        seq1_turning = {"20"}
        seq1_objs = []
        for n in seq1_nums:
            color = self.COLOR_TEN if n in seq1_turning else self.COLOR_NORMAL
            font_size = 40 if n in seq1_turning else 32
            t = Text(n, font="PingFang SC", font_size=font_size, color=color)
            seq1_objs.append(t)

        seq1_group = VGroup(*seq1_objs).arrange(RIGHT, buff=0.18).move_to(UP * 3.2)

        for i, obj in enumerate(seq1_objs):
            if seq1_nums[i] in seq1_turning:
                self.play(FadeIn(obj, scale=1.2), run_time=0.2)
                self.play(Indicate(obj, color=self.COLOR_HIGHLIGHT), run_time=0.25)
            else:
                self.play(FadeIn(obj, scale=0.9), run_time=0.12)

        self.wait(0.4)

        # 第二个拐弯：29 -> 30
        turning_label2 = Text(
            "第二个拐弯",
            font="PingFang SC",
            font_size=22,
            color=GRAY_B
        ).move_to(UP * 2.3)
        self.play(FadeIn(turning_label2), run_time=0.3)

        t29 = Text("29", font="PingFang SC", font_size=72, color=self.COLOR_NORMAL)
        arr2 = Text("->", font="PingFang SC", font_size=56, color=WHITE)
        t30 = Text("30", font="PingFang SC", font_size=72, color=self.COLOR_TEN)
        group2 = VGroup(t29, arr2, t30).arrange(RIGHT, buff=0.35).move_to(UP * 1.4)

        self.play(FadeIn(t29, scale=0.8), run_time=0.4)
        self.play(FadeIn(arr2), run_time=0.2)
        self.play(FadeIn(t30, scale=1.3), run_time=0.5)
        self.play(Indicate(t30, color=self.COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.4)
        self.wait(0.3)

        # 从27数到33的序列
        seq2_nums = [str(i) for i in range(27, 34)]
        seq2_turning = {"30"}
        seq2_objs = []
        for n in seq2_nums:
            color = self.COLOR_TEN if n in seq2_turning else self.COLOR_NORMAL
            font_size = 40 if n in seq2_turning else 32
            t = Text(n, font="PingFang SC", font_size=font_size, color=color)
            seq2_objs.append(t)

        seq2_group = VGroup(*seq2_objs).arrange(RIGHT, buff=0.18).move_to(UP * 0.3)

        for i, obj in enumerate(seq2_objs):
            if seq2_nums[i] in seq2_turning:
                self.play(FadeIn(obj, scale=1.2), run_time=0.2)
                self.play(Indicate(obj, color=self.COLOR_HIGHLIGHT), run_time=0.25)
            else:
                self.play(FadeIn(obj, scale=0.9), run_time=0.12)

        self.wait(0.4)

        # 规律说明
        rule_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.6,
            color=self.COLOR_HIGHLIGHT,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.8,
            stroke_width=2
        ).move_to(DOWN * 1.2)

        rule_line1 = Text(
            "规律：数到 X9 之后",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 0.9)

        rule_line2 = Text(
            "下一个就是 (X+1)0，拐弯！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)

        self.play(Create(rule_box), run_time=0.4)
        self.play(Write(rule_line1), run_time=0.5)
        self.play(Write(rule_line2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(turning_label1),
            FadeOut(group1),
            FadeOut(seq1_group),
            FadeOut(turning_label2),
            FadeOut(group2),
            FadeOut(seq2_group),
            FadeOut(rule_box),
            FadeOut(rule_line1),
            FadeOut(rule_line2),
            run_time=0.5
        )

    # -------------------------------------------------
    # Scene 4: 十个十个地数
    # -------------------------------------------------
    def scene_4_count_by_tens(self):
        # 场景标题
        scene_title = Text(
            "十个十个地数",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_TEN
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        subtitle = Text(
            "每次数 10 个",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 整十数序列
        tens_sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        tens_objs = []

        for val in tens_sequence:
            color = self.COLOR_HIGHLIGHT if val == 100 else self.COLOR_TEN
            font_size = 44 if val == 100 else 38
            t = Text(str(val), font="PingFang SC", font_size=font_size, color=color)
            tens_objs.append(t)

        # 排成两行，每行5个
        row1 = VGroup(*tens_objs[:5]).arrange(RIGHT, buff=0.3).move_to(UP * 4.2)
        row2 = VGroup(*tens_objs[5:]).arrange(RIGHT, buff=0.3).move_to(UP * 3.2)

        for obj in tens_objs[:5]:
            self.play(FadeIn(obj, shift=UP * 0.2), run_time=0.25)

        self.wait(0.2)

        for i, obj in enumerate(tens_objs[5:]):
            if i == 4:  # 100
                self.play(FadeIn(obj, scale=1.3), run_time=0.35)
                self.play(Indicate(obj, color=self.COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.4)
            else:
                self.play(FadeIn(obj, shift=UP * 0.2), run_time=0.25)

        self.wait(0.5)

        # 数数节奏说明
        rhythm_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.4,
            color=self.COLOR_TEN,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.8,
            stroke_width=2
        ).move_to(UP * 1.9)

        rhythm_text1 = Text(
            "十，二十，三十...一百",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TEN
        ).move_to(UP * 2.1)

        rhythm_text2 = Text(
            "数 10 次，就到 100！",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 1.65)

        self.play(Create(rhythm_box), run_time=0.4)
        self.play(Write(rhythm_text1), run_time=0.6)
        self.play(Write(rhythm_text2), run_time=0.5)
        self.wait(0.5)

        # 数轴展示十的跳跃
        number_line = NumberLine(
            x_range=[0, 100, 10],
            length=7.2,
            color=GRAY_B,
            include_numbers=False,
            tick_size=0.1,
        ).move_to(UP * 0.6)

        self.play(Create(number_line), run_time=0.8)

        # 标记0和100
        label_0 = Text("0", font="PingFang SC", font_size=20, color=GRAY_A)
        label_0.next_to(number_line.n2p(0), DOWN, buff=0.15)
        label_100 = Text("100", font="PingFang SC", font_size=20, color=self.COLOR_HIGHLIGHT)
        label_100.next_to(number_line.n2p(100), DOWN, buff=0.15)

        self.play(FadeIn(label_0), FadeIn(label_100), run_time=0.3)

        # 跳跃点动画
        jump_dot = Dot(number_line.n2p(0), color=self.COLOR_TEN, radius=0.12)
        self.play(FadeIn(jump_dot), run_time=0.2)

        tick_labels_nl = []
        prev_pos = number_line.n2p(0)
        for val in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            target_pos = number_line.n2p(val)
            arc_path = ArcBetweenPoints(
                prev_pos,
                target_pos,
                angle=-PI / 3,
                color=self.COLOR_TEN,
                stroke_width=2.5
            )
            self.play(MoveAlongPath(jump_dot, arc_path), run_time=0.22)
            prev_pos = target_pos

            t_color = self.COLOR_TEN if val != 100 else self.COLOR_HIGHLIGHT
            tick_lbl = Text(
                str(val),
                font="PingFang SC",
                font_size=16,
                color=t_color
            ).next_to(target_pos, UP, buff=0.1)
            self.play(FadeIn(tick_lbl, scale=0.8), run_time=0.12)
            tick_labels_nl.append(tick_lbl)

        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(subtitle),
            FadeOut(row1),
            FadeOut(row2),
            FadeOut(rhythm_box),
            FadeOut(rhythm_text1),
            FadeOut(rhythm_text2),
            FadeOut(number_line),
            FadeOut(label_0),
            FadeOut(label_100),
            FadeOut(jump_dot),
            *[FadeOut(t) for t in tick_labels_nl],
            run_time=0.5
        )

    # -------------------------------------------------
    # Scene 5: 10个十=100
    # -------------------------------------------------
    def scene_5_ten_tens(self):
        # 场景标题
        scene_title = Text(
            "10个十 = 100",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.7)

        # 用方块矩阵展示：10行x10列 = 100个小方块
        BLOCK_SIZE = 0.38
        BLOCK_GAP = 0.04
        STEP = BLOCK_SIZE + BLOCK_GAP

        matrix_width = 10 * STEP - BLOCK_GAP
        matrix_start_x = -matrix_width / 2 + BLOCK_SIZE / 2
        matrix_start_y = 3.0

        colors_palette = [
            "#FF6B6B", "#FF8E53", "#FFC312", "#A3CB38",
            "#1289A7", "#D980FA", "#FDA7DF", "#ED4C67",
            "#F79F1F", "#12CBC4"
        ]

        ten_groups = []
        all_blocks = []

        for row in range(10):
            row_blocks = []
            for col in range(10):
                x = matrix_start_x + col * STEP
                y = matrix_start_y - row * STEP
                blk = Square(
                    side_length=BLOCK_SIZE,
                    color=colors_palette[row],
                    fill_color=colors_palette[row],
                    fill_opacity=0.85,
                    stroke_width=0.5,
                    stroke_color="#1a1a2e"
                ).move_to(np.array([x, y, 0]))
                row_blocks.append(blk)
                all_blocks.append(blk)
            ten_groups.append(VGroup(*row_blocks))

        # 逐行出现
        row_labels = []
        for i, grp in enumerate(ten_groups):
            self.play(FadeIn(grp, shift=RIGHT * 0.1), run_time=0.18)
            lbl = Text(
                "第" + str(i + 1) + "个十",
                font="PingFang SC",
                font_size=16,
                color=GRAY_B
            ).next_to(grp, RIGHT, buff=0.12)
            row_labels.append(lbl)

        self.wait(0.3)

        self.play(
            *[FadeIn(lbl, shift=LEFT * 0.1) for lbl in row_labels],
            run_time=0.5
        )
        self.wait(0.3)

        # 核心公式
        eq_10 = Text("10", font="PingFang SC", font_size=56, color=self.COLOR_TEN)
        eq_ge = Text("个", font="PingFang SC", font_size=36, color=WHITE)
        eq_shi = Text("十", font="PingFang SC", font_size=56, color=self.COLOR_TEN)
        eq_eq = Text("=", font="PingFang SC", font_size=48, color=WHITE)
        eq_100 = Text("100", font="PingFang SC", font_size=64, color=self.COLOR_HIGHLIGHT)

        formula_group = VGroup(eq_10, eq_ge, eq_shi, eq_eq, eq_100).arrange(RIGHT, buff=0.2)
        formula_group.move_to(DOWN * 3.0)

        self.play(Write(formula_group), run_time=1.0)
        self.play(Indicate(eq_100, color=self.COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.5)
        self.wait(0.5)

        # 强调框
        highlight_rect = SurroundingRectangle(
            formula_group,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.15,
            stroke_width=3
        )
        self.play(Create(highlight_rect), run_time=0.5)
        self.wait(1.5)

        # 清理
        all_mobs_to_clear = VGroup(*all_blocks, *row_labels, formula_group, highlight_rect)
        self.play(FadeOut(all_mobs_to_clear), FadeOut(scene_title), run_time=0.6)

    # -------------------------------------------------
    # Scene 6: 片尾
    # -------------------------------------------------
    def scene_6_outro(self):
        # 总结卡片标题
        summary_title = Text(
            "今天学会了",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.5)

        # 知识点卡片
        cards_data = [
            ("一个一个地数", "19->20, 29->30..."),
            ("十个十个地数", "10, 20, 30...100"),
            ("拐弯数是整十数", "20, 30, 40...100"),
            ("10个十=100", "这就是一百！"),
        ]

        card_groups = []
        card_colors = [self.COLOR_TEN, self.COLOR_ACCENT, self.COLOR_TEN, self.COLOR_ACCENT]
        for i, (point, detail) in enumerate(cards_data):
            box = RoundedRectangle(
                corner_radius=0.2,
                width=7.2,
                height=1.1,
                color=card_colors[i],
                fill_color=self.COLOR_BG_CARD,
                fill_opacity=0.9,
                stroke_width=2
            )

            pt_text = Text(
                point,
                font="PingFang SC",
                font_size=26,
                color=card_colors[i]
            )
            dt_text = Text(
                detail,
                font="PingFang SC",
                font_size=20,
                color=GRAY_A
            )
            texts = VGroup(pt_text, dt_text).arrange(RIGHT, buff=0.3)

            y_pos = 4.3 - i * 1.4
            box.move_to(UP * y_pos)
            texts.move_to(box.get_center())
            card = VGroup(box, texts)
            card_groups.append(card)

        for cg in card_groups:
            self.play(FadeIn(cg, shift=RIGHT * 0.2), run_time=0.4)

        self.wait(1.0)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=34,
            color=WHITE
        ).move_to(DOWN * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=26,
            color=GRAY_B
        ).move_to(DOWN * 2.7)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.2, scale=1.05), run_time=0.5)

        # 装饰数字
        deco_nums = ["20", "30", "50", "70", "100"]
        positions = [
            LEFT * 3.0 + DOWN * 4.8,
            LEFT * 1.5 + DOWN * 5.3,
            ORIGIN + DOWN * 4.8,
            RIGHT * 1.5 + DOWN * 5.3,
            RIGHT * 3.0 + DOWN * 4.8,
        ]
        deco_objs = []
        for num, pos in zip(deco_nums, positions):
            t = Text(num, font="PingFang SC", font_size=28, color=self.COLOR_TEN)
            t.move_to(pos)
            deco_objs.append(t)

        self.play(*[FadeIn(t, scale=0.6) for t in deco_objs], run_time=0.5)
        self.play(*[t.animate.scale(1.2) for t in deco_objs], run_time=0.4)
        self.play(*[t.animate.scale(1 / 1.2) for t in deco_objs], run_time=0.3)

        self.wait(1.5)

        # 全部淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)

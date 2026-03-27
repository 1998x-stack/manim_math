"""
两位数乘一位数（竖式计算）- Two-Digit Times One-Digit Multiplication (Vertical Format)
使用 Manim 创建的小学三年级数学教学视频

内容: 竖式乘法，以 28×4=112 为例，重点讲解进位
目标观众: 小学三年级学生
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


class TwoDigitTimeOneLesson(Scene):
    """
    两位数乘一位数竖式计算教学动画

    场景顺序:
    1. 开场钩子
    2. 引出题目 28×4
    3. 写出竖式
    4. 第一步：个位计算 8×4=32
    5. 第二步：十位计算 2×4+3=11
    6. 最终答案
    7. 总结规则
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_TITLE = "#f0c040"
        self.COLOR_HIGHLIGHT = "#ff6b6b"
        self.COLOR_CARRY = "#ff9f43"
        self.COLOR_ONES = "#48dbfb"
        self.COLOR_TENS = "#ff9ff3"
        self.COLOR_ANSWER = "#1dd1a1"
        self.COLOR_STEP = "#ffeaa7"
        self.COLOR_TEXT = "#dfe6e9"

        # 执行各场景
        self.scene_opening()
        self.scene_problem()
        self.scene_write_vertical()
        self.scene_ones_digit()
        self.scene_tens_digit()
        self.scene_final_answer()
        self.scene_summary()
        self.scene_outro()

    # ─────────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_opening(self):
        # 作者品牌
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook_line1 = Text(
            "28 × 4 怎么算？",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.0)

        hook_line2 = Text(
            "竖式乘法轻松搞定！",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TEXT,
        ).move_to(UP * 3.8)

        self.play(Write(hook_line1), run_time=0.9)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 大算式展示
        big_formula = MathTex(r"28 \times 4 = \; ?", font_size=96, color=WHITE)
        big_formula.move_to(UP * 1.5)
        self.play(Write(big_formula), run_time=1.0)
        self.wait(1.2)

        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(big_formula),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 2: 引出题目
    # ─────────────────────────────────────────────
    def scene_problem(self):
        title = Text(
            "两位数 × 一位数",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.0)

        subtitle = Text(
            "用竖式计算  28 × 4",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_TEXT,
        ).move_to(UP * 5.0)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 解释竖式是什么
        explain = Text(
            "把数字上下排列，逐位相乘",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_STEP,
        ).move_to(UP * 3.8)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(explain), run_time=0.4)

        # 保存标题供下一场景用
        self.scene_title = title
        self.scene_subtitle = subtitle

    # ─────────────────────────────────────────────
    # 场景 3: 写出竖式
    # ─────────────────────────────────────────────
    def scene_write_vertical(self):
        # 竖式布局中心
        cx = 0.0
        cy = 1.5  # 竖式居中位置

        # 数字的位置（手动精确布置）
        # 第一行: 28  (十位2在左，个位8在右)
        # 第二行: ×4  (×号在中间偏左，4在右)
        # 横线
        # 第三行: 结果

        # 定义列坐标
        x_hundreds = cx - 1.2   # 百位
        x_tens = cx + 0.0       # 十位
        x_ones = cx + 1.2       # 个位

        # 定义行坐标
        y_row1 = cy + 1.2       # 被乘数
        y_row2 = cy + 0.0       # 乘数
        y_row3 = cy - 1.5       # 结果

        self.x_hundreds = x_hundreds
        self.x_tens = x_tens
        self.x_ones = x_ones
        self.y_row1 = y_row1
        self.y_row2 = y_row2
        self.y_row3 = y_row3
        self.cx = cx
        self.cy = cy

        # 写被乘数 28
        num_2 = MathTex(r"2", font_size=80, color=WHITE).move_to(
            np.array([x_tens, y_row1, 0])
        )
        num_8 = MathTex(r"8", font_size=80, color=WHITE).move_to(
            np.array([x_ones, y_row1, 0])
        )

        # 写乘号和乘数 4
        times_sign = MathTex(r"\times", font_size=72, color=WHITE).move_to(
            np.array([x_tens - 0.8, y_row2, 0])
        )
        num_4 = MathTex(r"4", font_size=80, color=WHITE).move_to(
            np.array([x_ones, y_row2, 0])
        )

        # 横线
        line_left = x_hundreds - 0.5
        line_right = x_ones + 0.7
        line_y = (y_row2 + y_row3) / 2
        h_line = Line(
            np.array([line_left, line_y, 0]),
            np.array([line_right, line_y, 0]),
            color=WHITE,
            stroke_width=3,
        )

        self.num_2 = num_2
        self.num_8 = num_8
        self.times_sign = times_sign
        self.num_4 = num_4
        self.h_line = h_line
        self.h_line_y = line_y

        # 动画写出竖式
        self.play(Write(num_2), Write(num_8), run_time=0.8)
        self.play(Write(times_sign), Write(num_4), run_time=0.6)
        self.play(Create(h_line), run_time=0.5)
        self.wait(0.8)

        # 说明：相同数位对齐
        align_tip = Text(
            "个位对齐个位",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_STEP,
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(align_tip, shift=UP * 0.2), run_time=0.5)

        # 高亮个位对齐
        box_8 = SurroundingRectangle(num_8, color=self.COLOR_ONES, buff=0.15, stroke_width=2)
        box_4 = SurroundingRectangle(num_4, color=self.COLOR_ONES, buff=0.15, stroke_width=2)
        self.play(Create(box_8), Create(box_4), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(box_8), FadeOut(box_4), FadeOut(align_tip), run_time=0.4)

    # ─────────────────────────────────────────────
    # 场景 4: 第一步 - 个位计算
    # ─────────────────────────────────────────────
    def scene_ones_digit(self):
        x_hundreds = self.x_hundreds
        x_tens = self.x_tens
        x_ones = self.x_ones
        y_row1 = self.y_row1
        y_row2 = self.y_row2
        y_row3 = self.y_row3

        # 步骤标题
        step1_title = Text(
            "第一步：先算个位",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_ONES,
        ).move_to(DOWN * 1.8)
        self.play(Write(step1_title), run_time=0.6)

        # 高亮个位 8 和 4
        hl_8 = self.num_8.copy().set_color(self.COLOR_ONES)
        hl_4 = self.num_4.copy().set_color(self.COLOR_ONES)
        self.play(
            Transform(self.num_8, hl_8),
            Transform(self.num_4, hl_4),
            run_time=0.5,
        )

        # 个位计算说明
        calc_line1 = Text(
            "个位：8 × 4 = 32",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ONES,
        ).move_to(DOWN * 2.8)
        self.play(Write(calc_line1), run_time=0.7)
        self.wait(0.8)

        # 说明：32 满了三十，写2进3
        carry_explain = Text(
            "32 = 30 + 2",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_CARRY,
        ).move_to(DOWN * 3.7)
        self.play(FadeIn(carry_explain, shift=UP * 0.2), run_time=0.5)

        write_2 = Text(
            "个位写 2，向十位进 3",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_CARRY,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(write_2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 在结果个位写 2
        result_2 = MathTex(r"2", font_size=80, color=self.COLOR_ANSWER).move_to(
            np.array([x_ones, y_row3, 0])
        )
        self.play(Write(result_2), run_time=0.6)

        # 进位 3 写在十位上方（小字）
        carry_3 = MathTex(r"3", font_size=44, color=self.COLOR_CARRY).move_to(
            np.array([x_tens, y_row1 + 0.75, 0])
        )
        carry_box = SurroundingRectangle(
            carry_3, color=self.COLOR_CARRY, buff=0.12, stroke_width=2
        )
        self.play(Write(carry_3), Create(carry_box), run_time=0.7)

        # 进位箭头提示
        carry_arrow = Arrow(
            start=np.array([x_ones, y_row3 + 0.3, 0]),
            end=np.array([x_tens, y_row1 + 0.5, 0]),
            color=self.COLOR_CARRY,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(Create(carry_arrow), run_time=0.6)
        self.wait(1.0)

        # 清理说明文字和箭头
        self.play(
            FadeOut(step1_title),
            FadeOut(calc_line1),
            FadeOut(carry_explain),
            FadeOut(write_2),
            FadeOut(carry_arrow),
            run_time=0.5,
        )

        # 还原 8 和 4 颜色（但保留进位3）
        restore_8 = self.num_8.copy().set_color(WHITE)
        restore_4 = self.num_4.copy().set_color(WHITE)
        self.play(
            Transform(self.num_8, restore_8),
            Transform(self.num_4, restore_4),
            run_time=0.3,
        )

        # 保存供后续使用
        self.result_2 = result_2
        self.carry_3 = carry_3
        self.carry_box = carry_box

    # ─────────────────────────────────────────────
    # 场景 5: 第二步 - 十位计算
    # ─────────────────────────────────────────────
    def scene_tens_digit(self):
        x_hundreds = self.x_hundreds
        x_tens = self.x_tens
        x_ones = self.x_ones
        y_row1 = self.y_row1
        y_row2 = self.y_row2
        y_row3 = self.y_row3

        # 步骤标题
        step2_title = Text(
            "第二步：再算十位",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_TENS,
        ).move_to(DOWN * 1.8)
        self.play(Write(step2_title), run_time=0.6)

        # 高亮十位 2 和 4
        hl_2 = self.num_2.copy().set_color(self.COLOR_TENS)
        hl_4_tens = self.num_4.copy().set_color(self.COLOR_TENS)
        hl_carry = self.carry_3.copy().set_color(self.COLOR_CARRY)

        self.play(
            Transform(self.num_2, hl_2),
            Transform(self.num_4, hl_4_tens),
            run_time=0.5,
        )

        # 计算步骤
        calc_step1 = Text(
            "十位：2 × 4 = 8",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_TENS,
        ).move_to(DOWN * 2.8)
        self.play(Write(calc_step1), run_time=0.7)
        self.wait(0.8)

        calc_step2 = Text(
            "加上进位的 3",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_CARRY,
        ).move_to(DOWN * 3.6)
        self.play(FadeIn(calc_step2, shift=UP * 0.2), run_time=0.5)

        # 高亮进位3
        carry_flash = self.carry_3.copy().set_color(YELLOW)
        carry_box_flash = self.carry_box.copy().set_color(YELLOW)
        self.play(
            Transform(self.carry_3, carry_flash),
            Transform(self.carry_box, carry_box_flash),
            run_time=0.4,
        )
        self.wait(0.5)

        calc_step3 = Text(
            "8 + 3 = 11",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.4)
        self.play(Write(calc_step3), run_time=0.6)
        self.wait(1.0)

        # 说明11：百位写1，十位写1
        explain_11 = Text(
            "11 = 百位1，十位1",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_ANSWER,
        ).move_to(DOWN * 5.2)
        self.play(FadeIn(explain_11, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 写出十位结果 1
        result_1_tens = MathTex(r"1", font_size=80, color=self.COLOR_ANSWER).move_to(
            np.array([x_tens, y_row3, 0])
        )
        self.play(Write(result_1_tens), run_time=0.6)

        # 写出百位结果 1
        result_1_hundreds = MathTex(r"1", font_size=80, color=self.COLOR_ANSWER).move_to(
            np.array([x_hundreds, y_row3, 0])
        )
        self.play(Write(result_1_hundreds), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(step2_title),
            FadeOut(calc_step1),
            FadeOut(calc_step2),
            FadeOut(calc_step3),
            FadeOut(explain_11),
            run_time=0.5,
        )

        # 还原颜色
        restore_2 = self.num_2.copy().set_color(WHITE)
        restore_4b = self.num_4.copy().set_color(WHITE)
        self.play(
            Transform(self.num_2, restore_2),
            Transform(self.num_4, restore_4b),
            run_time=0.3,
        )

        self.result_1_tens = result_1_tens
        self.result_1_hundreds = result_1_hundreds

    # ─────────────────────────────────────────────
    # 场景 6: 最终答案
    # ─────────────────────────────────────────────
    def scene_final_answer(self):
        x_hundreds = self.x_hundreds
        x_tens = self.x_tens
        x_ones = self.x_ones
        y_row3 = self.y_row3

        # 把进位框淡出
        self.play(FadeOut(self.carry_3), FadeOut(self.carry_box), run_time=0.4)

        # 让三个结果数字闪光
        answer_group = VGroup(
            self.result_1_hundreds,
            self.result_1_tens,
            self.result_2,
        )

        self.play(
            Indicate(self.result_1_hundreds, color=self.COLOR_ANSWER, scale_factor=1.3),
            Indicate(self.result_1_tens, color=self.COLOR_ANSWER, scale_factor=1.3),
            Indicate(self.result_2, color=self.COLOR_ANSWER, scale_factor=1.3),
            run_time=0.8,
        )

        # 答案展示
        answer_label = Text(
            "答案是 112！",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.COLOR_ANSWER,
        ).move_to(DOWN * 2.2)
        self.play(Write(answer_label), run_time=0.8)

        # 验证算式
        verify = MathTex(
            r"28 \times 4 = 112",
            font_size=64,
            color=WHITE,
        ).move_to(DOWN * 3.5)
        self.play(Write(verify), run_time=0.8)
        self.wait(1.5)

        # 闪光效果
        self.play(
            Flash(answer_group.get_center(), color=self.COLOR_ANSWER, flash_radius=1.2),
            run_time=0.6,
        )
        self.wait(0.8)

        self.play(
            FadeOut(answer_label),
            FadeOut(verify),
            run_time=0.5,
        )

        self.answer_group = answer_group

    # ─────────────────────────────────────────────
    # 场景 7: 总结规则
    # ─────────────────────────────────────────────
    def scene_summary(self):
        # 淡出竖式
        self.play(
            FadeOut(self.num_2),
            FadeOut(self.num_8),
            FadeOut(self.times_sign),
            FadeOut(self.num_4),
            FadeOut(self.h_line),
            FadeOut(self.answer_group),
            FadeOut(self.scene_title),
            FadeOut(self.scene_subtitle),
            run_time=0.6,
        )

        # 总结标题
        summary_title = Text(
            "竖式乘法口诀",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_TITLE,
        ).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.6)

        # 三条规则
        rules = [
            ("1.", "相同数位对齐", self.COLOR_TEXT),
            ("2.", "从个位开始乘", self.COLOR_ONES),
            ("3.", "满十向前进一位", self.COLOR_CARRY),
        ]

        rule_mobs = VGroup()
        for i, (num, text, color) in enumerate(rules):
            num_text = Text(
                num,
                font="Noto Sans CJK SC",
                font_size=34,
                color=color,
            )
            rule_text = Text(
                text,
                font="Noto Sans CJK SC",
                font_size=34,
                color=color,
            )
            row = VGroup(num_text, rule_text).arrange(RIGHT, buff=0.3)
            row.move_to(UP * (3.8 - i * 1.4))
            rule_mobs.add(row)

        for row in rule_mobs:
            self.play(FadeIn(row, shift=RIGHT * 0.4), run_time=0.5)
            self.wait(0.4)

        self.wait(0.5)

        # 再次展示例题和答案
        example_label = Text(
            "例：",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_STEP,
        )
        example_formula = MathTex(
            r"28 \times 4 = 112",
            font_size=56,
            color=self.COLOR_ANSWER,
        )
        example_row = VGroup(example_label, example_formula).arrange(RIGHT, buff=0.3)
        example_row.move_to(DOWN * 0.5)

        self.play(FadeIn(example_row, shift=UP * 0.3, scale=1.05), run_time=0.7)
        self.wait(1.0)

        # 关键难点提示
        key_tip = Text(
            "关键：进位不要忘！",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.0)
        self.play(Write(key_tip), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(summary_title),
            FadeOut(rule_mobs),
            FadeOut(example_row),
            FadeOut(key_tip),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 8: 片尾
    # ─────────────────────────────────────────────
    def scene_outro(self):
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE,
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color="#6b7280",
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author, author_name),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_TITLE,
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰：小乘号闪烁
        decorations = VGroup()
        positions = [
            UP * 3.5 + LEFT * 2.5,
            UP * 3.5 + RIGHT * 2.5,
            DOWN * 1.8 + LEFT * 3.0,
            DOWN * 1.8 + RIGHT * 3.0,
            DOWN * 3.5,
        ]
        for pos in positions:
            star = MathTex(r"\times", font_size=36, color=self.COLOR_TITLE)
            star.move_to(pos)
            decorations.add(star)

        self.play(*[FadeIn(d, scale=0.5) for d in decorations], run_time=0.6)
        self.wait(1.2)

        # 淡出
        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0,
        )

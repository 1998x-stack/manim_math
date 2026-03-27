"""
末尾有0的乘法简便算法
Trailing Zero Multiplication Shortcut - Teaching Animation

知识点: 先将0前面的数相乘,再看两个因数末尾一共有几个0,就在积的末尾添上几个0
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


class TrailingZeroMultiplyLesson(Scene):
    """
    末尾有0的乘法简便算法教学动画

    场景顺序:
    1. 开场钩子 - 提问引入
    2. 观察算式结构 - 250×40拆解
    3. 核心步骤 Step1 - 先算非零部分 25×4
    4. 核心步骤 Step2 - 数末尾0的个数
    5. 核心步骤 Step3 - 在积后面补0
    6. 算理解释 - 乘法性质
    7. 再练一题 - 巩固练习
    8. 总结规律 + 结尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.C_TITLE   = "#f0c040"   # 金黄 - 标题
        self.C_PRIMARY = "#4fc3f7"   # 天蓝 - 主要公式
        self.C_ZERO    = "#ef5350"   # 红色 - 末尾的0
        self.C_RESULT  = "#66bb6a"   # 绿色 - 结果
        self.C_STEP    = "#ffa726"   # 橙色 - 步骤标题
        self.C_AUX     = "#b0bec5"   # 灰色 - 辅助说明
        self.C_ARROW   = "#ce93d8"   # 紫色 - 箭头

        self.scene_1_opening()
        self.scene_2_observe()
        self.scene_3_step1()
        self.scene_4_step2()
        self.scene_5_step3()
        self.scene_6_algorithm()
        self.scene_7_practice()
        self.scene_8_summary()

    # ─────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.C_AUX
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.3)

        # 钩子问题
        hook_q = Text(
            "250 × 40 = ?",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 3.5)

        hook_sub = Text(
            "不用竖式，秒算答案！",
            font="Noto Sans CJK SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 2.2)

        hook_emoji = Text(
            "🤔",
            font="Noto Sans CJK SC",
            font_size=80
        ).move_to(UP * 0.5)

        hint = Text(
            "末尾有0，有简便算法！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.C_ZERO
        ).move_to(DOWN * 1.2)

        self.play(Write(hook_q), run_time=0.9)
        self.play(FadeIn(hook_sub), run_time=0.6)
        self.play(FadeIn(hook_emoji, scale=0.5), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(hook_q),
            FadeOut(hook_sub),
            FadeOut(hook_emoji),
            FadeOut(hint),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 2: 观察算式 250×40 的结构
    # ─────────────────────────────────────────────────
    def scene_2_observe(self):
        title = Text(
            "观察：算式的结构",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.4)

        # 大号算式 250 × 40
        eq = VGroup(
            Text("250", font="Noto Sans CJK SC", font_size=72, color=self.C_PRIMARY),
            Text("×", font="Noto Sans CJK SC", font_size=60, color=WHITE),
            Text("40", font="Noto Sans CJK SC", font_size=72, color=self.C_PRIMARY),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4.2)

        self.play(Write(eq), run_time=0.8)
        self.wait(0.4)

        # 标注 250 = 25 × 10
        brace_250 = Brace(eq[0], DOWN, color=self.C_ZERO, buff=0.1)
        label_250 = VGroup(
            Text("25", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("×", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            Text("10", font="Noto Sans CJK SC", font_size=32, color=self.C_ZERO),
        ).arrange(RIGHT, buff=0.15)
        label_250.next_to(brace_250, DOWN, buff=0.15)

        # 标注 40 = 4 × 10
        brace_40 = Brace(eq[2], DOWN, color=self.C_ZERO, buff=0.1)
        label_40 = VGroup(
            Text("4", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("×", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            Text("10", font="Noto Sans CJK SC", font_size=32, color=self.C_ZERO),
        ).arrange(RIGHT, buff=0.15)
        label_40.next_to(brace_40, DOWN, buff=0.15)

        self.play(
            GrowFromCenter(brace_250),
            GrowFromCenter(brace_40),
            run_time=0.5
        )
        self.play(
            FadeIn(label_250, shift=DOWN * 0.2),
            FadeIn(label_40,  shift=DOWN * 0.2),
            run_time=0.6
        )

        # 说明文字
        note = Text(
            "末尾的 0 可以分离出来单独处理！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_STEP
        ).move_to(UP * 1.5)

        # 圈出两个 0
        zero_250 = eq[0][-1]   # 250 的末尾0 - 实际上是 Text 对象本身
        circle_250 = Circle(radius=0.55, color=self.C_ZERO, stroke_width=3).move_to(eq[0].get_right() + LEFT * 0.35)
        circle_40  = Circle(radius=0.45, color=self.C_ZERO, stroke_width=3).move_to(eq[2].get_right() + LEFT * 0.28)

        self.play(
            Create(circle_250),
            Create(circle_40),
            run_time=0.7
        )
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        self.scene2_objs = VGroup(eq, brace_250, label_250, brace_40, label_40, circle_250, circle_40)
        self.play(
            FadeOut(self.scene2_objs),
            FadeOut(note),
            FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 3: Step 1 - 先算非零部分 25 × 4
    # ─────────────────────────────────────────────────
    def scene_3_step1(self):
        # 步骤标题
        step_badge = self._make_step_badge("第一步", self.C_STEP)
        step_badge.move_to(UP * 6.5)
        self.play(FadeIn(step_badge), run_time=0.4)

        step_desc = Text(
            "先算 0 前面的数相乘",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(step_desc), run_time=0.6)

        # 原算式（小号，顶部参考）
        orig = VGroup(
            Text("250", font="Noto Sans CJK SC", font_size=44, color=self.C_AUX),
            Text("×", font="Noto Sans CJK SC", font_size=38, color=self.C_AUX),
            Text("40", font="Noto Sans CJK SC", font_size=44, color=self.C_AUX),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 4.3)
        self.play(FadeIn(orig), run_time=0.4)

        # 箭头 + 提取非零数
        arr1 = Arrow(orig[0].get_bottom(), orig[0].get_bottom() + DOWN * 1.0, color=self.C_ARROW, buff=0.05)
        arr2 = Arrow(orig[2].get_bottom(), orig[2].get_bottom() + DOWN * 1.0, color=self.C_ARROW, buff=0.05)

        lbl_25 = Text("25", font="Noto Sans CJK SC", font_size=48, color=self.C_PRIMARY, weight=BOLD)
        lbl_x  = Text("×", font="Noto Sans CJK SC", font_size=40, color=WHITE)
        lbl_4  = Text("4",  font="Noto Sans CJK SC", font_size=48, color=self.C_PRIMARY, weight=BOLD)
        non_zero_eq = VGroup(lbl_25, lbl_x, lbl_4).arrange(RIGHT, buff=0.3).move_to(UP * 2.8)

        self.play(GrowArrow(arr1), GrowArrow(arr2), run_time=0.5)
        self.play(Write(non_zero_eq), run_time=0.7)

        # 计算 25 × 4 = 100
        equals = Text("=", font="Noto Sans CJK SC", font_size=44, color=WHITE)
        result_100 = Text("100", font="Noto Sans CJK SC", font_size=56, color=self.C_RESULT, weight=BOLD)
        full_eq = VGroup(non_zero_eq.copy(), equals, result_100).arrange(RIGHT, buff=0.35).move_to(UP * 1.4)

        self.play(
            Transform(non_zero_eq, full_eq[0]),
            FadeIn(equals, shift=LEFT * 0.3),
            run_time=0.5
        )
        self.play(
            Write(result_100),
            run_time=0.6
        )

        # 强调 100
        self.play(Indicate(result_100, color=self.C_RESULT, scale_factor=1.25), run_time=0.7)

        self.wait(1.5)

        # 保留 result_100 到下一步，其他淡出
        self.play(
            FadeOut(step_badge),
            FadeOut(step_desc),
            FadeOut(orig),
            FadeOut(arr1),
            FadeOut(arr2),
            FadeOut(non_zero_eq),
            FadeOut(equals),
            run_time=0.4
        )
        # result_100 移到上方参考位置
        result_100_small = Text("25 × 4 = 100", font="Noto Sans CJK SC", font_size=28, color=self.C_RESULT)
        result_100_small.move_to(UP * 5.8)
        self.play(Transform(result_100, result_100_small), run_time=0.5)
        self.step1_ref = result_100

    # ─────────────────────────────────────────────────
    # Scene 4: Step 2 - 数末尾 0 的个数
    # ─────────────────────────────────────────────────
    def scene_4_step2(self):
        step_badge = self._make_step_badge("第二步", self.C_STEP)
        step_badge.move_to(UP * 6.5)
        self.play(FadeIn(step_badge), run_time=0.4)

        step_desc = Text(
            "数两个因数末尾共有几个 0",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(step_desc), run_time=0.6)

        # 展示 250 和 40，用不同颜色标出末尾的0
        n1_part = Text("25", font="Noto Sans CJK SC", font_size=62, color=WHITE)
        n1_zero = Text("0", font="Noto Sans CJK SC", font_size=62, color=self.C_ZERO, weight=BOLD)
        n1 = VGroup(n1_part, n1_zero).arrange(RIGHT, buff=0)

        mult = Text("×", font="Noto Sans CJK SC", font_size=52, color=WHITE)

        n2_part = Text("4", font="Noto Sans CJK SC", font_size=62, color=WHITE)
        n2_zero = Text("0", font="Noto Sans CJK SC", font_size=62, color=self.C_ZERO, weight=BOLD)
        n2 = VGroup(n2_part, n2_zero).arrange(RIGHT, buff=0)

        big_eq = VGroup(n1, mult, n2).arrange(RIGHT, buff=0.35).move_to(UP * 3.8)
        self.play(Write(big_eq), run_time=0.8)

        # 闪烁末尾0
        self.play(
            Indicate(n1_zero, color=self.C_ZERO, scale_factor=1.4),
            Indicate(n2_zero, color=self.C_ZERO, scale_factor=1.4),
            run_time=0.8
        )

        # 圈出两个零
        circ1 = Circle(radius=0.42, color=self.C_ZERO, stroke_width=3).move_to(n1_zero.get_center())
        circ2 = Circle(radius=0.42, color=self.C_ZERO, stroke_width=3).move_to(n2_zero.get_center())
        self.play(Create(circ1), Create(circ2), run_time=0.5)

        # 计数
        count_line = VGroup(
            Text("250 末尾有", font="Noto Sans CJK SC", font_size=26, color=self.C_AUX),
            Text("1", font="Noto Sans CJK SC", font_size=32, color=self.C_ZERO, weight=BOLD),
            Text("个0，40 末尾有", font="Noto Sans CJK SC", font_size=26, color=self.C_AUX),
            Text("1", font="Noto Sans CJK SC", font_size=32, color=self.C_ZERO, weight=BOLD),
            Text("个0", font="Noto Sans CJK SC", font_size=26, color=self.C_AUX),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 2.2)

        self.play(FadeIn(count_line, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)

        # 总计
        total_line = VGroup(
            Text("共有", font="Noto Sans CJK SC", font_size=30, color=WHITE),
            Text("1 + 1 = 2", font="Noto Sans CJK SC", font_size=36, color=self.C_ZERO, weight=BOLD),
            Text("个0", font="Noto Sans CJK SC", font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.8)

        self.play(Write(total_line), run_time=0.7)
        self.play(Indicate(total_line[1], scale_factor=1.2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(step_badge),
            FadeOut(step_desc),
            FadeOut(big_eq),
            FadeOut(circ1),
            FadeOut(circ2),
            FadeOut(count_line),
            run_time=0.4
        )
        # 保留 total_line 到下一步
        total_small = Text("末尾共 2 个 0", font="Noto Sans CJK SC", font_size=26, color=self.C_ZERO)
        total_small.move_to(UP * 5.0)
        self.play(Transform(total_line, total_small), run_time=0.4)
        self.step2_ref = total_line

    # ─────────────────────────────────────────────────
    # Scene 5: Step 3 - 在积后面补 0
    # ─────────────────────────────────────────────────
    def scene_5_step3(self):
        step_badge = self._make_step_badge("第三步", self.C_STEP)
        step_badge.move_to(UP * 6.5)
        self.play(FadeIn(step_badge), run_time=0.4)

        step_desc = Text(
            "在积的末尾添上相同个数的 0",
            font="Noto Sans CJK SC",
            font_size=27,
            color=WHITE
        ).move_to(UP * 4.2)
        self.play(Write(step_desc), run_time=0.6)

        # 展示 100，然后依次加 0
        base_num = Text("100", font="Noto Sans CJK SC", font_size=72, color=self.C_RESULT, weight=BOLD)
        base_num.move_to(UP * 2.5)
        self.play(Write(base_num), run_time=0.5)

        note_add = Text(
            "末尾共 2 个 0，所以在 100 后面添 2 个 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_AUX
        ).move_to(UP * 1.2)
        self.play(FadeIn(note_add), run_time=0.5)
        self.wait(0.5)

        # 第1个 0 出现
        zero1 = Text("0", font="Noto Sans CJK SC", font_size=72, color=self.C_ZERO, weight=BOLD)
        zero1.next_to(base_num, RIGHT, buff=0)
        self.play(FadeIn(zero1, shift=DOWN * 0.5, scale=0.5), run_time=0.5)
        self.play(Indicate(zero1, color=self.C_ZERO), run_time=0.4)

        # 第2个 0 出现
        zero2 = Text("0", font="Noto Sans CJK SC", font_size=72, color=self.C_ZERO, weight=BOLD)
        zero2.next_to(zero1, RIGHT, buff=0)
        self.play(FadeIn(zero2, shift=DOWN * 0.5, scale=0.5), run_time=0.5)
        self.play(Indicate(zero2, color=self.C_ZERO), run_time=0.4)

        # 答案揭晓
        answer_label = Text(
            "250 × 40  =  10000",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(DOWN * 0.3)

        self.play(
            FadeOut(base_num),
            FadeOut(zero1),
            FadeOut(zero2),
            run_time=0.3
        )
        self.play(Write(answer_label), run_time=0.8)
        self.play(
            Flash(answer_label, color=self.C_TITLE, flash_radius=1.2, line_length=0.3, num_lines=10),
            run_time=0.8
        )
        self.wait(1.8)

        self.play(
            FadeOut(step_badge),
            FadeOut(step_desc),
            FadeOut(note_add),
            FadeOut(answer_label),
            FadeOut(self.step1_ref),
            FadeOut(self.step2_ref),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 6: 算理解释 - 乘法性质
    # ─────────────────────────────────────────────────
    def scene_6_algorithm(self):
        title = Text(
            "为什么这样算？",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title), run_time=0.4)

        sub = Text(
            "利用乘法结合律与交换律",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_AUX
        ).move_to(UP * 5.6)
        self.play(FadeIn(sub), run_time=0.4)

        # 逐行推导，Text + MathTex 分开
        lines = []

        # 行1: 250 × 40
        row1 = Text("250 × 40", font="Noto Sans CJK SC", font_size=40, color=self.C_PRIMARY)
        lines.append(row1)

        # 行2: = (25 × 10) × (4 × 10)
        row2 = Text(
            "= (25 × 10) × (4 × 10)",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        )
        lines.append(row2)

        # 行3: = 25 × 4 × 10 × 10  (颜色高亮 25×4 和 10×10)
        row3_part1 = Text("= (25 × 4)", font="Noto Sans CJK SC", font_size=36, color=self.C_RESULT)
        row3_part2 = Text("×", font="Noto Sans CJK SC", font_size=36, color=WHITE)
        row3_part3 = Text("(10 × 10)", font="Noto Sans CJK SC", font_size=36, color=self.C_ZERO)
        row3 = VGroup(row3_part1, row3_part2, row3_part3).arrange(RIGHT, buff=0.2)
        lines.append(row3)

        # 行4: = 100 × 100
        row4_part1 = Text("= 100", font="Noto Sans CJK SC", font_size=36, color=self.C_RESULT)
        row4_part2 = Text("×", font="Noto Sans CJK SC", font_size=36, color=WHITE)
        row4_part3 = Text("100", font="Noto Sans CJK SC", font_size=36, color=self.C_ZERO)
        row4 = VGroup(row4_part1, row4_part2, row4_part3).arrange(RIGHT, buff=0.2)
        lines.append(row4)

        # 行5: = 10000
        row5 = Text("= 10000", font="Noto Sans CJK SC", font_size=44, color=self.C_TITLE, weight=BOLD)
        lines.append(row5)

        derivation = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to(UP * 2.5)

        for i, line in enumerate(lines):
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=0.55)
            if i in (2, 3, 4):
                self.wait(0.4)
            else:
                self.wait(0.2)

        # 强调最终结果
        self.play(Indicate(row5, scale_factor=1.2, color=self.C_TITLE), run_time=0.8)

        key_msg = Text(
            "乘法性质让我们灵活交换因数顺序！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_STEP
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(key_msg, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(sub),
            FadeOut(derivation),
            FadeOut(key_msg),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 7: 再练一题 - 160 × 30
    # ─────────────────────────────────────────────────
    def scene_7_practice(self):
        title = Text(
            "再练一题！",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title), run_time=0.4)

        # 题目
        prob = Text(
            "160 × 30 = ?",
            font="Noto Sans CJK SC",
            font_size=56,
            color=self.C_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5.2)
        self.play(Write(prob), run_time=0.7)
        self.wait(0.4)

        # Step 1: 非零部分
        step1_badge = self._make_step_badge("①", self.C_STEP, font_size=28)
        step1_badge.move_to(UP * 4.0 + LEFT * 3.2)

        step1_text = Text(
            "非零部分：16 × 3 = 48",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 4.0 + RIGHT * 0.3)

        self.play(FadeIn(step1_badge), Write(step1_text), run_time=0.6)
        self.wait(0.3)

        # Step 2: 数零
        step2_badge = self._make_step_badge("②", self.C_STEP, font_size=28)
        step2_badge.move_to(UP * 2.8 + LEFT * 3.2)

        step2_text = VGroup(
            Text("160末尾", font="Noto Sans CJK SC", font_size=28, color=self.C_AUX),
            Text("1", font="Noto Sans CJK SC", font_size=30, color=self.C_ZERO, weight=BOLD),
            Text("个0，30末尾", font="Noto Sans CJK SC", font_size=28, color=self.C_AUX),
            Text("1", font="Noto Sans CJK SC", font_size=30, color=self.C_ZERO, weight=BOLD),
            Text("个0，共", font="Noto Sans CJK SC", font_size=28, color=self.C_AUX),
            Text("2", font="Noto Sans CJK SC", font_size=30, color=self.C_ZERO, weight=BOLD),
            Text("个0", font="Noto Sans CJK SC", font_size=28, color=self.C_AUX),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 2.8 + RIGHT * 0.3)

        self.play(FadeIn(step2_badge), FadeIn(step2_text, shift=RIGHT * 0.2), run_time=0.6)
        self.wait(0.3)

        # Step 3: 添0
        step3_badge = self._make_step_badge("③", self.C_STEP, font_size=28)
        step3_badge.move_to(UP * 1.6 + LEFT * 3.2)

        step3_text = Text(
            "48 后添 2 个 0 → 4800",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 1.6 + RIGHT * 0.3)

        self.play(FadeIn(step3_badge), Write(step3_text), run_time=0.6)
        self.wait(0.4)

        # 答案
        ans_box_bg = RoundedRectangle(
            corner_radius=0.3,
            width=6.5,
            height=1.2,
            fill_color="#1e3a5f",
            fill_opacity=1,
            stroke_color=self.C_RESULT,
            stroke_width=3
        ).move_to(UP * 0.1)
        ans_text = Text(
            "160 × 30 = 4800",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.C_RESULT,
            weight=BOLD
        ).move_to(UP * 0.1)

        self.play(FadeIn(ans_box_bg), run_time=0.3)
        self.play(Write(ans_text), run_time=0.7)
        self.play(
            Flash(ans_text, color=self.C_RESULT, flash_radius=1.0, num_lines=10),
            run_time=0.7
        )
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(prob),
            FadeOut(step1_badge),
            FadeOut(step1_text),
            FadeOut(step2_badge),
            FadeOut(step2_text),
            FadeOut(step3_badge),
            FadeOut(step3_text),
            FadeOut(ans_box_bg),
            FadeOut(ans_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    # Scene 8: 总结 + 结尾
    # ─────────────────────────────────────────────────
    def scene_8_summary(self):
        # 总结标题
        sum_title = Text(
            "简便算法口诀",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(sum_title), run_time=0.4)

        # 三条口诀
        rule_bg = RoundedRectangle(
            corner_radius=0.35,
            width=7.8,
            height=4.2,
            fill_color="#0d2137",
            fill_opacity=1,
            stroke_color=self.C_PRIMARY,
            stroke_width=2.5
        ).move_to(UP * 3.6)
        self.play(FadeIn(rule_bg), run_time=0.3)

        rules = VGroup(
            self._make_rule_line("①", "先算末尾 0 前面的数相乘", self.C_RESULT),
            self._make_rule_line("②", "数两因数末尾 0 的总个数", self.C_ZERO),
            self._make_rule_line("③", "在积的末尾添上对应个数的 0", self.C_STEP),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(UP * 3.6)
        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rules], lag_ratio=0.35),
            run_time=1.2
        )
        self.wait(0.6)

        # 示例汇总
        ex_title = Text("例题回顾", font="Noto Sans CJK SC", font_size=30, color=WHITE).move_to(UP * 1.3)
        ex1 = Text("250 × 40 = 10000", font="Noto Sans CJK SC", font_size=34, color=self.C_PRIMARY).move_to(UP * 0.45)
        ex2 = Text("160 × 30 = 4800", font="Noto Sans CJK SC", font_size=34, color=self.C_PRIMARY).move_to(DOWN * 0.45)

        self.play(FadeIn(ex_title), run_time=0.4)
        self.play(Write(ex1), run_time=0.6)
        self.play(Write(ex2), run_time=0.6)
        self.wait(0.8)

        # 结尾 CTA
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=YELLOW,
            weight=BOLD
        ).move_to(DOWN * 1.8)

        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 2.9)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_AUX
        ).move_to(DOWN * 3.7)

        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.05),
            run_time=0.7
        )
        self.play(
            FadeIn(author_big),
            FadeIn(author_id),
            run_time=0.5
        )

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
            FadeOut(rule_bg),
            FadeOut(rules),
            FadeOut(ex_title),
            FadeOut(ex1),
            FadeOut(ex2),
            FadeOut(follow_text),
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(stars),
            FadeOut(self.author),
            run_time=1.0
        )

    # ─────────────────────────────────────────────────
    # Helper methods
    # ─────────────────────────────────────────────────
    def _make_step_badge(self, text_str, color, font_size=30):
        """创建步骤徽章（圆形 + 文字）"""
        circle = Circle(radius=0.38, fill_color=color, fill_opacity=1, stroke_width=0)
        label = Text(text_str, font="Noto Sans CJK SC", font_size=font_size, color=WHITE, weight=BOLD)
        return VGroup(circle, label)

    def _make_rule_line(self, num_str, content_str, color):
        """创建口诀行"""
        num = Text(num_str, font="Noto Sans CJK SC", font_size=32, color=color, weight=BOLD)
        content = Text(content_str, font="Noto Sans CJK SC", font_size=28, color=WHITE)
        return VGroup(num, content).arrange(RIGHT, buff=0.3)

"""
三位数乘一位数 - Three-digit Number Multiplication
小学三年级 上册 第二章 用一位数乘

内容: 掌握三位数乘一位数的竖式计算，重点讲解连续进位（249×4=996）
目标受众: 小学三年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 TikTok 竖屏 ──────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 颜色配置 ─────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
COLOR_TITLE    = "#f0c040"
COLOR_ONES     = "#e74c3c"    # 个位 - 红
COLOR_TENS     = "#3498db"    # 十位 - 蓝
COLOR_HUNDREDS = "#2ecc71"    # 百位 - 绿
COLOR_CARRY    = "#f39c12"    # 进位 - 橙
COLOR_RESULT   = "#ffffff"    # 结果 - 白
COLOR_BODY     = "#d0d0d0"    # 正文
COLOR_HINT     = "#a0aec0"    # 提示小字
COLOR_HL       = YELLOW       # 高亮

FONT = "Noto Sans CJK SC"


class ThreeDigitMultiplyLesson(Scene):
    """
    三位数乘一位数教学动画
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 回顾两位数乘一位数
    3. 竖式布局介绍
    4. 个位计算 (9x4=36，写6进3)
    5. 十位计算 (4x4+3=19，写9进1)
    6. 百位计算 (2x4+1=9)
    7. 完整答案展示
    8. 连续进位要点总结
    9. 片尾关注
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者品牌（始终显示）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author)

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_review()
        self.scene_3_layout()
        self.scene_4_ones()
        self.scene_5_tens()
        self.scene_6_hundreds()
        self.scene_7_answer()
        self.scene_8_summary()
        self.scene_9_outro()

    # ─────────────────────────────────────────────────────────
    # 场景 1：开场钩子
    # ─────────────────────────────────────────────────────────
    def scene_1_hook(self):
        title = Text("三位数乘一位数", font=FONT, font_size=48, color=COLOR_TITLE)
        title.move_to(UP * 5.5)

        question = Text("你会算吗？", font=FONT, font_size=36, color=COLOR_BODY)
        question.move_to(UP * 4.5)

        # 大号题目
        prob_text = MathTex(r"249 \times 4 = \, ?", font_size=72, color=COLOR_HL)
        prob_text.move_to(UP * 2.5)

        hint = Text("连续进位，小心出错！", font=FONT, font_size=28, color=COLOR_CARRY)
        hint.move_to(UP * 1.2)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.4)
        self.play(Write(prob_text), run_time=1.0)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(hint),
            prob_text.animate.scale(0.55).move_to(UP * 5.8),
            run_time=0.7
        )
        self.prob_ref = prob_text  # 保留在顶部作参考

    # ─────────────────────────────────────────────────────────
    # 场景 2：回顾两位数乘一位数
    # ─────────────────────────────────────────────────────────
    def scene_2_review(self):
        review_title = Text("先回顾：两位数 × 一位数", font=FONT, font_size=30, color=COLOR_TITLE)
        review_title.move_to(UP * 4.6)

        # 简单示例：24 × 4
        example_label = Text("例：24 × 4", font=FONT, font_size=26, color=COLOR_BODY)
        example_label.move_to(UP * 3.7)

        # 竖式文字示意
        line1 = Text("  2  4", font=FONT, font_size=44, color=COLOR_BODY)
        line2 = Text("×     4", font=FONT, font_size=44, color=COLOR_BODY)
        col = VGroup(line1, line2).arrange(DOWN, aligned_edge=RIGHT, buff=0.15)
        col.move_to(UP * 2.3)

        sep_line = Line(LEFT * 1.4, RIGHT * 1.4, color=COLOR_BODY, stroke_width=2)
        sep_line.next_to(col, DOWN, buff=0.1)

        result_row = Text("  9  6", font=FONT, font_size=44, color=COLOR_RESULT)
        result_row.next_to(sep_line, DOWN, buff=0.1)

        step_ones = Text("个位：4×4=16，写6进1", font=FONT, font_size=22, color=COLOR_ONES)
        step_ones.move_to(DOWN * 0.5)
        step_tens = Text("十位：2×4+1=9", font=FONT, font_size=22, color=COLOR_TENS)
        step_tens.move_to(DOWN * 1.2)

        self.play(Write(review_title), run_time=0.5)
        self.play(FadeIn(example_label), run_time=0.3)
        self.play(Write(line1), Write(line2), run_time=0.6)
        self.play(Create(sep_line), run_time=0.3)
        self.play(Write(result_row), run_time=0.5)
        self.play(FadeIn(step_ones), run_time=0.4)
        self.play(FadeIn(step_tens), run_time=0.4)
        self.wait(1.0)

        bridge = Text("现在升级到三位数！", font=FONT, font_size=30, color=COLOR_CARRY)
        bridge.move_to(DOWN * 2.2)
        self.play(FadeIn(bridge, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(review_title), FadeOut(example_label),
            FadeOut(line1), FadeOut(line2), FadeOut(sep_line),
            FadeOut(result_row), FadeOut(step_ones), FadeOut(step_tens),
            FadeOut(bridge),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # 工具：构建竖式各部件（坐标精确计算）
    # ─────────────────────────────────────────────────────────
    def _build_vertical_form(self, center_y=2.0):
        """
        返回竖式各部件，便于后续动画引用。
        数字间距统一，保证对齐。
        """
        DX = 0.65   # 每列间距
        DY = 0.75   # 行间距

        x_h = -DX      # 百位
        x_t = 0.0      # 十位
        x_o = DX       # 个位

        y_top = center_y + DY        # 被乘数行 y
        y_mid = center_y             # 乘数行 y
        y_sep = center_y - DY * 0.5  # 横线 y
        y_res = center_y - DY * 1.3  # 结果行 y

        fs = 52  # 数字字体大小

        # 被乘数 249
        d2 = Text("2", font=FONT, font_size=fs, color=COLOR_HUNDREDS).move_to([x_h, y_top, 0])
        d4 = Text("4", font=FONT, font_size=fs, color=COLOR_TENS).move_to([x_t, y_top, 0])
        d9 = Text("9", font=FONT, font_size=fs, color=COLOR_ONES).move_to([x_o, y_top, 0])

        # 乘号 + 乘数
        mul_sign = MathTex(r"\times", font_size=fs, color=COLOR_BODY).move_to([x_h - DX * 0.8, y_mid, 0])
        mul_4    = Text("4", font=FONT, font_size=fs, color=COLOR_BODY).move_to([x_o, y_mid, 0])

        # 横线
        sep = Line(
            [x_h - DX * 0.9, y_sep, 0],
            [x_o + DX * 0.5, y_sep, 0],
            color=COLOR_BODY, stroke_width=2.5
        )

        # 结果位占位
        res_h = Text("?", font=FONT, font_size=fs, color=COLOR_RESULT).move_to([x_h, y_res, 0])
        res_t = Text("?", font=FONT, font_size=fs, color=COLOR_RESULT).move_to([x_t, y_res, 0])
        res_o = Text("?", font=FONT, font_size=fs, color=COLOR_RESULT).move_to([x_o, y_res, 0])

        # 进位标注位置（数字上方）
        carry_t_pos = np.array([x_t, y_top + 0.55, 0])   # 十位进位
        carry_h_pos = np.array([x_h, y_top + 0.55, 0])   # 百位进位

        return dict(
            d2=d2, d4=d4, d9=d9,
            mul_sign=mul_sign, mul_4=mul_4,
            sep=sep,
            res_h=res_h, res_t=res_t, res_o=res_o,
            carry_t_pos=carry_t_pos, carry_h_pos=carry_h_pos,
            y_top=y_top, y_mid=y_mid, y_sep=y_sep, y_res=y_res,
            x_h=x_h, x_t=x_t, x_o=x_o, DX=DX, DY=DY
        )

    # ─────────────────────────────────────────────────────────
    # 场景 3：竖式布局介绍
    # ─────────────────────────────────────────────────────────
    def scene_3_layout(self):
        layout_title = Text("写出竖式", font=FONT, font_size=34, color=COLOR_TITLE)
        layout_title.move_to(UP * 5.0)

        v = self._build_vertical_form(center_y=1.5)
        self.vf = v  # 保存供后续场景使用

        self.play(Write(layout_title), run_time=0.4)
        self.play(
            FadeIn(v["d2"]), FadeIn(v["d4"]), FadeIn(v["d9"]),
            run_time=0.6
        )
        self.play(
            FadeIn(v["mul_sign"]), FadeIn(v["mul_4"]),
            run_time=0.4
        )
        self.play(Create(v["sep"]), run_time=0.3)

        # 标注三位数各位
        label_h = Text("百位", font=FONT, font_size=20, color=COLOR_HUNDREDS)
        label_t = Text("十位", font=FONT, font_size=20, color=COLOR_TENS)
        label_o = Text("个位", font=FONT, font_size=20, color=COLOR_ONES)

        y_lbl = v["y_top"] + 1.0
        label_h.move_to([v["x_h"], y_lbl, 0])
        label_t.move_to([v["x_t"], y_lbl, 0])
        label_o.move_to([v["x_o"], y_lbl, 0])

        arr_h = Arrow(
            label_h.get_bottom(), v["d2"].get_top(), buff=0.05,
            color=COLOR_HUNDREDS, stroke_width=1.5, max_tip_length_to_length_ratio=0.2
        )
        arr_t = Arrow(
            label_t.get_bottom(), v["d4"].get_top(), buff=0.05,
            color=COLOR_TENS, stroke_width=1.5, max_tip_length_to_length_ratio=0.2
        )
        arr_o = Arrow(
            label_o.get_bottom(), v["d9"].get_top(), buff=0.05,
            color=COLOR_ONES, stroke_width=1.5, max_tip_length_to_length_ratio=0.2
        )

        self.play(
            FadeIn(label_h), Create(arr_h),
            FadeIn(label_t), Create(arr_t),
            FadeIn(label_o), Create(arr_o),
            run_time=0.7
        )

        rule = Text("从个位开始，逐位相乘，记得进位！",
                    font=FONT, font_size=22, color=COLOR_HINT)
        rule.move_to(DOWN * 2.5)
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(layout_title),
            FadeOut(label_h), FadeOut(arr_h),
            FadeOut(label_t), FadeOut(arr_t),
            FadeOut(label_o), FadeOut(arr_o),
            FadeOut(rule),
            run_time=0.5
        )
        # 竖式主体保留

    # ─────────────────────────────────────────────────────────
    # 场景 4：个位计算 9×4=36
    # ─────────────────────────────────────────────────────────
    def scene_4_ones(self):
        v = self.vf
        step_title = Text("第一步：算个位", font=FONT, font_size=32, color=COLOR_ONES)
        step_title.move_to(UP * 5.2)

        # 高亮个位
        self.play(
            Write(step_title),
            Indicate(v["d9"], color=COLOR_ONES, scale_factor=1.4),
            Indicate(v["mul_4"], color=COLOR_ONES, scale_factor=1.4),
            run_time=0.8
        )

        # 计算过程文字
        calc_line1 = Text("9 × 4 = 36", font=FONT, font_size=30, color=COLOR_ONES)
        calc_line1.move_to(DOWN * 1.8)

        self.play(FadeIn(calc_line1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 分析：写6进3
        write6 = Text("个位写 6，向十位进 3", font=FONT, font_size=26, color=COLOR_CARRY)
        write6.move_to(DOWN * 2.6)
        self.play(FadeIn(write6), run_time=0.4)
        self.wait(0.6)

        # 显示结果个位 "6"
        res_o_real = Text("6", font=FONT, font_size=52, color=COLOR_ONES)
        res_o_real.move_to(v["res_o"].get_center())
        self.play(Write(res_o_real), run_time=0.4)
        self.vf["res_o_real"] = res_o_real

        # 显示进位 "3" 在十位上方
        carry3 = Text("3", font=FONT, font_size=26, color=COLOR_CARRY)
        carry3.move_to(v["carry_t_pos"])
        self.play(FadeIn(carry3, shift=UP * 0.15), run_time=0.4)
        self.vf["carry3"] = carry3

        # 进位箭头示意
        carry_arrow = CurvedArrow(
            calc_line1.get_top() + UP * 0.1,
            carry3.get_bottom() + DOWN * 0.05,
            color=COLOR_CARRY,
            stroke_width=2,
            tip_length=0.18,
            angle=-TAU / 6
        )
        self.play(Create(carry_arrow), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(step_title), FadeOut(calc_line1),
            FadeOut(write6), FadeOut(carry_arrow),
            run_time=0.4
        )

    # ─────────────────────────────────────────────────────────
    # 场景 5：十位计算 4×4+3=19
    # ─────────────────────────────────────────────────────────
    def scene_5_tens(self):
        v = self.vf
        step_title = Text("第二步：算十位", font=FONT, font_size=32, color=COLOR_TENS)
        step_title.move_to(UP * 5.2)

        self.play(
            Write(step_title),
            Indicate(v["d4"], color=COLOR_TENS, scale_factor=1.4),
            Indicate(v["mul_4"], color=COLOR_TENS, scale_factor=1.4),
            run_time=0.8
        )

        # 提示不要忘记进位
        dont_forget = Text("别忘了进来的 3 ！", font=FONT, font_size=26, color=COLOR_CARRY)
        dont_forget.move_to(DOWN * 1.5)
        self.play(
            FadeIn(dont_forget),
            Indicate(v["carry3"], color=COLOR_CARRY, scale_factor=1.5),
            run_time=0.8
        )
        self.wait(0.4)

        # 计算过程
        calc_line2a = Text("4 × 4 = 16", font=FONT, font_size=28, color=COLOR_TENS)
        calc_line2a.move_to(DOWN * 2.4)
        calc_line2b = Text("16 + 3 = 19", font=FONT, font_size=28, color=COLOR_TENS)
        calc_line2b.move_to(DOWN * 3.1)

        self.play(FadeIn(calc_line2a, shift=UP * 0.15), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(calc_line2b, shift=UP * 0.15), run_time=0.4)
        self.wait(0.5)

        write9_1 = Text("十位写 9，向百位进 1", font=FONT, font_size=26, color=COLOR_CARRY)
        write9_1.move_to(DOWN * 3.9)
        self.play(FadeIn(write9_1), run_time=0.4)
        self.wait(0.6)

        # 显示结果十位 "9"
        res_t_real = Text("9", font=FONT, font_size=52, color=COLOR_TENS)
        res_t_real.move_to(v["res_t"].get_center())
        self.play(Write(res_t_real), run_time=0.4)
        self.vf["res_t_real"] = res_t_real

        # 显示进位 "1" 在百位上方
        carry1 = Text("1", font=FONT, font_size=26, color=COLOR_CARRY)
        carry1.move_to(v["carry_h_pos"])
        self.play(FadeIn(carry1, shift=UP * 0.15), run_time=0.4)
        self.vf["carry1"] = carry1

        self.wait(1.0)

        self.play(
            FadeOut(step_title), FadeOut(dont_forget),
            FadeOut(calc_line2a), FadeOut(calc_line2b),
            FadeOut(write9_1),
            run_time=0.4
        )

    # ─────────────────────────────────────────────────────────
    # 场景 6：百位计算 2×4+1=9
    # ─────────────────────────────────────────────────────────
    def scene_6_hundreds(self):
        v = self.vf
        step_title = Text("第三步：算百位", font=FONT, font_size=32, color=COLOR_HUNDREDS)
        step_title.move_to(UP * 5.2)

        self.play(
            Write(step_title),
            Indicate(v["d2"], color=COLOR_HUNDREDS, scale_factor=1.4),
            Indicate(v["mul_4"], color=COLOR_HUNDREDS, scale_factor=1.4),
            run_time=0.8
        )

        dont_forget2 = Text("别忘了进来的 1 ！", font=FONT, font_size=26, color=COLOR_CARRY)
        dont_forget2.move_to(DOWN * 1.5)
        self.play(
            FadeIn(dont_forget2),
            Indicate(v["carry1"], color=COLOR_CARRY, scale_factor=1.5),
            run_time=0.8
        )
        self.wait(0.4)

        calc_line3a = Text("2 × 4 = 8", font=FONT, font_size=28, color=COLOR_HUNDREDS)
        calc_line3a.move_to(DOWN * 2.4)
        calc_line3b = Text("8 + 1 = 9", font=FONT, font_size=28, color=COLOR_HUNDREDS)
        calc_line3b.move_to(DOWN * 3.1)

        self.play(FadeIn(calc_line3a, shift=UP * 0.15), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(calc_line3b, shift=UP * 0.15), run_time=0.4)
        self.wait(0.5)

        write9_2 = Text("百位写 9，没有进位了！", font=FONT, font_size=26, color=COLOR_HUNDREDS)
        write9_2.move_to(DOWN * 3.9)
        self.play(FadeIn(write9_2), run_time=0.4)
        self.wait(0.6)

        # 显示结果百位 "9"
        res_h_real = Text("9", font=FONT, font_size=52, color=COLOR_HUNDREDS)
        res_h_real.move_to(v["res_h"].get_center())
        self.play(Write(res_h_real), run_time=0.4)
        self.vf["res_h_real"] = res_h_real

        self.wait(1.0)

        self.play(
            FadeOut(step_title), FadeOut(dont_forget2),
            FadeOut(calc_line3a), FadeOut(calc_line3b),
            FadeOut(write9_2),
            run_time=0.4
        )

    # ─────────────────────────────────────────────────────────
    # 场景 7：完整答案展示
    # ─────────────────────────────────────────────────────────
    def scene_7_answer(self):
        v = self.vf

        # 高亮完整结果
        self.play(
            Indicate(v["res_h_real"], scale_factor=1.3, color=COLOR_HL),
            Indicate(v["res_t_real"], scale_factor=1.3, color=COLOR_HL),
            Indicate(v["res_o_real"], scale_factor=1.3, color=COLOR_HL),
            run_time=0.8
        )

        answer_title = Text("答案是：", font=FONT, font_size=32, color=COLOR_TITLE)
        answer_title.move_to(DOWN * 1.5)

        big_answer = MathTex(r"249 \times 4 = 996", font_size=64, color=COLOR_HL)
        big_answer.move_to(DOWN * 2.5)

        self.play(FadeIn(answer_title), run_time=0.3)
        self.play(Write(big_answer), run_time=0.9)

        # 庆祝效果
        self.play(
            Flash(big_answer, color=COLOR_HL, flash_radius=1.5, num_lines=14),
            run_time=0.8
        )
        self.wait(1.5)

        # 淡出竖式，为总结腾出空间
        self.play(
            FadeOut(v["d2"]), FadeOut(v["d4"]), FadeOut(v["d9"]),
            FadeOut(v["mul_sign"]), FadeOut(v["mul_4"]),
            FadeOut(v["sep"]),
            FadeOut(v["res_h_real"]), FadeOut(v["res_t_real"]), FadeOut(v["res_o_real"]),
            FadeOut(v["carry3"]), FadeOut(v["carry1"]),
            FadeOut(answer_title),
            big_answer.animate.move_to(UP * 4.4).scale(0.65),
            run_time=0.8
        )
        self.big_answer = big_answer

    # ─────────────────────────────────────────────────────────
    # 场景 8：连续进位要点总结
    # ─────────────────────────────────────────────────────────
    def scene_8_summary(self):
        summary_title = Text("连续进位 — 3个关键步骤", font=FONT, font_size=30, color=COLOR_TITLE)
        summary_title.move_to(UP * 3.2)
        self.play(Write(summary_title), run_time=0.5)

        # 三条要点
        tips = [
            ("1", "从个位开始，逐位相乘", COLOR_ONES),
            ("2", "积超过9，进位数写在高位上方", COLOR_TENS),
            ("3", "计算每一位时，加上进来的数", COLOR_HUNDREDS),
        ]

        tip_groups = []
        start_y = 2.0
        for i, (num, txt, col) in enumerate(tips):
            circle = Circle(radius=0.28, fill_color=col, fill_opacity=1, stroke_width=0)
            num_t = Text(num, font=FONT, font_size=22, color=WHITE, weight=BOLD)
            num_t.move_to(circle.get_center())
            icon = VGroup(circle, num_t)

            content = Text(txt, font=FONT, font_size=24, color=COLOR_BODY)
            row = VGroup(icon, content).arrange(RIGHT, buff=0.3)
            row.move_to([0, start_y - i * 1.1, 0])
            tip_groups.append(row)

        for row in tip_groups:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 口诀
        slogan = Text("从个位起，逢十进一，不要漏！",
                      font=FONT, font_size=26, color=COLOR_CARRY)
        slogan.move_to(DOWN * 1.5)
        slogan_box = SurroundingRectangle(slogan, color=COLOR_CARRY, buff=0.2, stroke_width=2)
        self.play(FadeIn(slogan), Create(slogan_box), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(summary_title),
            *[FadeOut(r) for r in tip_groups],
            FadeOut(slogan), FadeOut(slogan_box),
            FadeOut(self.big_answer),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────
    # 场景 9：片尾关注
    # ─────────────────────────────────────────────────────────
    def scene_9_outro(self):
        # 作者名放大
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=38, color=WHITE)
        author_big.move_to(UP * 1.5)

        author_id = Text("@emptyandcalm", font=FONT, font_size=28, color=COLOR_HINT)
        author_id.move_to(UP * 0.6)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=28, color=COLOR_HL)
        follow.move_to(DOWN * 0.5)

        self.play(
            Transform(self.author, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰：数字小图标
        deco_nums = []
        positions = [
            UP * 3.5 + LEFT * 2.5,
            UP * 3.5 + RIGHT * 2.5,
            DOWN * 2.5 + LEFT * 2.5,
            DOWN * 2.5 + RIGHT * 2.5,
        ]
        labels_txt = ["249", "x4", "996", "=?"]
        colors_d = [COLOR_HUNDREDS, COLOR_TENS, COLOR_ONES, COLOR_CARRY]
        for pos, txt, col in zip(positions, labels_txt, colors_d):
            t = Text(txt, font=FONT, font_size=32, color=col, fill_opacity=0.7)
            t.move_to(pos)
            deco_nums.append(t)

        self.play(*[FadeIn(d, scale=0.5) for d in deco_nums], run_time=0.6)
        self.wait(1.5)

        self.play(*[FadeOut(d) for d in deco_nums], run_time=0.5)
        self.wait(0.5)

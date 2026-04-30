"""
近似数与四舍五入 - Approximate Numbers and Rounding
小学四年级数学教学动画

内容: 理解精确数与近似数的区别，掌握四舍五入法求近似数
目标观众: 四年级小学生
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


class RoundingLesson(Scene):
    """
    近似数与四舍五入教学动画

    场景顺序:
    1. 开场钩子 - 引发思考
    2. 精确数 vs 近似数的概念
    3. 四舍五入规则
    4. 例题1: 234500 约等于 23万 (省略万后面的数)
    5. 例题2: 995000000 约等于 10亿 (进位情况)
    6. 规律总结
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#4fc3f7"
        self.COLOR_SECONDARY = "#81c784"
        self.COLOR_HIGHLIGHT = "#ffd54f"
        self.COLOR_ERROR = "#ef5350"
        self.COLOR_SUCCESS = "#66bb6a"
        self.COLOR_ACCENT = "#ce93d8"
        self.COLOR_DIM = "#78909c"

        # 作者信息（全程显示）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author)

        # 执行各场景
        self.scene_opening()
        self.scene_concept()
        self.scene_rule()
        self.scene_example1()
        self.scene_example2()
        self.scene_summary()
        self.scene_outro()

    # ========== 工具函数 ==========

    def make_title(self, text, color=None, font_size=36):
        if color is None:
            color = self.COLOR_HIGHLIGHT
        return Text(text, font="PingFang SC", font_size=font_size, color=color)

    def make_body(self, text, color=None, font_size=26):
        if color is None:
            color = WHITE
        return Text(text, font="PingFang SC", font_size=font_size, color=color)

    def make_small(self, text, color=None, font_size=20):
        if color is None:
            color = self.COLOR_DIM
        return Text(text, font="PingFang SC", font_size=font_size, color=color)

    def fadeout_all(self, run_time=0.5):
        to_remove = [m for m in self.mobjects if m is not self.author]
        if to_remove:
            self.play(*[FadeOut(m) for m in to_remove], run_time=run_time)

    # ========== 场景1: 开场钩子 ==========

    def scene_opening(self):
        hook = self.make_title("你知道吗？", font_size=48, color=self.COLOR_HIGHLIGHT)
        hook.move_to(UP * 5.5)

        question = self.make_body("全球人口约有80亿人", font_size=30)
        question.move_to(UP * 4.3)

        num_exact = MathTex(r"8{,}045{,}311{,}447", color=self.COLOR_PRIMARY, font_size=40)
        num_exact.move_to(UP * 3.2)

        vs_text = self.make_small("精确数字 vs 近似数字", font_size=22, color=self.COLOR_DIM)
        vs_text.move_to(UP * 2.1)

        num_approx = MathTex(r"\approx 80", color=self.COLOR_HIGHLIGHT, font_size=52)
        unit_approx = self.make_body("亿", font_size=50, color=self.COLOR_HIGHLIGHT)
        approx_group = VGroup(num_approx, unit_approx).arrange(RIGHT, buff=0.1)
        approx_group.move_to(UP * 0.8)

        topic = self.make_title("近似数与四舍五入", font_size=38, color=self.COLOR_ACCENT)
        topic.move_to(DOWN * 0.6)

        subtitle = self.make_small("让大数变得更好读！", font_size=24, color=self.COLOR_SECONDARY)
        subtitle.move_to(DOWN * 1.6)

        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.2)
        self.play(Write(question), run_time=0.7)
        self.play(Write(num_exact), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(vs_text), run_time=0.4)
        self.play(GrowFromCenter(approx_group), run_time=0.8)
        self.wait(0.5)
        self.play(Write(topic), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.fadeout_all(run_time=0.6)

    # ========== 场景2: 精确数 vs 近似数概念 ==========

    def scene_concept(self):
        title = self.make_title("精确数 vs 近似数", font_size=36)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.7)

        # 精确数
        exact_label = self.make_body("精确数", font_size=28, color=self.COLOR_PRIMARY)
        exact_label.move_to(UP * 4.8)
        exact_line = Line(LEFT * 3.5, RIGHT * 3.5, color=self.COLOR_PRIMARY, stroke_width=2)
        exact_line.move_to(UP * 4.4)

        self.play(FadeIn(exact_label), Create(exact_line), run_time=0.5)

        exact_ex1 = self.make_body("班里有 42 人", font_size=26)
        exact_ex1.move_to(UP * 3.7)
        exact_ex2 = self.make_body("这本书共 235 页", font_size=26)
        exact_ex2.move_to(UP * 2.9)
        exact_note = self.make_small("（一个不多，一个不少）", font_size=20, color=self.COLOR_DIM)
        exact_note.move_to(UP * 2.1)

        self.play(Write(exact_ex1), run_time=0.6)
        self.play(Write(exact_ex2), run_time=0.6)
        self.play(FadeIn(exact_note), run_time=0.4)
        self.wait(0.8)

        # 近似数
        approx_label = self.make_body("近似数", font_size=28, color=self.COLOR_HIGHLIGHT)
        approx_label.move_to(UP * 1.0)
        approx_line = Line(LEFT * 3.5, RIGHT * 3.5, color=self.COLOR_HIGHLIGHT, stroke_width=2)
        approx_line.move_to(UP * 0.6)

        self.play(FadeIn(approx_label), Create(approx_line), run_time=0.5)

        approx_ex1 = self.make_body("学校约有 1200 人", font_size=26)
        approx_ex1.move_to(DOWN * 0.1)
        approx_ex2 = self.make_body("全国人口约 14 亿", font_size=26)
        approx_ex2.move_to(DOWN * 0.9)
        approx_note = self.make_small("（大约差不多，不是精确数）", font_size=20, color=self.COLOR_DIM)
        approx_note.move_to(DOWN * 1.7)

        self.play(Write(approx_ex1), run_time=0.6)
        self.play(Write(approx_ex2), run_time=0.6)
        self.play(FadeIn(approx_note), run_time=0.4)
        self.wait(0.8)

        # 约等于符号
        approx_symbol = MathTex(r"\approx", color=self.COLOR_ACCENT, font_size=64)
        approx_symbol.move_to(DOWN * 3.0)
        symbol_note = self.make_body("表示「约等于」", font_size=26, color=self.COLOR_ACCENT)
        symbol_note.move_to(DOWN * 4.1)

        self.play(GrowFromCenter(approx_symbol), run_time=0.6)
        self.play(Write(symbol_note), run_time=0.6)
        self.wait(1.5)

        self.fadeout_all(run_time=0.5)

    # ========== 场景3: 四舍五入规则 ==========

    def scene_rule(self):
        title = self.make_title("四舍五入法则", font_size=38, color=self.COLOR_HIGHLIGHT)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        rule_intro = self.make_body("看要省略位的下一位数字：", font_size=26)
        rule_intro.move_to(UP * 5.4)
        self.play(Write(rule_intro), run_time=0.6)

        # 数轴 0-9
        number_line = NumberLine(
            x_range=[0, 9, 1],
            length=7.5,
            include_numbers=True,
            numbers_to_include=list(range(10)),
            font_size=26,
            color=WHITE,
            include_tip=False,
        )
        number_line.move_to(UP * 4.0)
        self.play(Create(number_line), run_time=0.9)

        # 0-4 舍区域
        shed_brace_start = number_line.n2p(0)
        shed_brace_end = number_line.n2p(4)
        shed_line = Line(shed_brace_start, shed_brace_end, color=self.COLOR_ERROR, stroke_width=5)
        shed_line.shift(DOWN * 0.45)

        shed_label = self.make_body("0, 1, 2, 3, 4", font_size=26, color=self.COLOR_ERROR)
        shed_label.move_to(UP * 2.8)

        shed_text = self.make_body("舍  去", font_size=32, color=self.COLOR_ERROR)
        shed_text.move_to(UP * 1.9)
        shed_sub = self.make_small("（直接去掉后面的数）", font_size=20, color=self.COLOR_ERROR)
        shed_sub.move_to(UP * 1.2)

        self.play(Create(shed_line), run_time=0.5)
        self.play(FadeIn(shed_label), run_time=0.4)
        self.play(Write(shed_text), FadeIn(shed_sub), run_time=0.6)
        self.wait(0.8)

        # 5-9 进区域
        enter_brace_start = number_line.n2p(5)
        enter_brace_end = number_line.n2p(9)
        enter_line = Line(enter_brace_start, enter_brace_end, color=self.COLOR_SUCCESS, stroke_width=5)
        enter_line.shift(DOWN * 0.45)

        enter_label = self.make_body("5, 6, 7, 8, 9", font_size=26, color=self.COLOR_SUCCESS)
        enter_label.move_to(DOWN * 0.0)

        enter_text = self.make_body("进  一", font_size=32, color=self.COLOR_SUCCESS)
        enter_text.move_to(DOWN * 0.9)
        enter_sub = self.make_small("（前一位加1，再去掉后面的数）", font_size=20, color=self.COLOR_SUCCESS)
        enter_sub.move_to(DOWN * 1.6)

        self.play(Create(enter_line), run_time=0.5)
        self.play(FadeIn(enter_label), run_time=0.4)
        self.play(Write(enter_text), FadeIn(enter_sub), run_time=0.6)
        self.wait(0.8)

        # 口诀
        divider = Line(LEFT * 3.8, RIGHT * 3.8, color=self.COLOR_DIM, stroke_width=1.5)
        divider.move_to(DOWN * 2.7)
        self.play(Create(divider), run_time=0.3)

        rule_text = self.make_body("口诀：四舍五入", font_size=30, color=self.COLOR_ACCENT)
        rule_text.move_to(DOWN * 3.5)
        rule_detail = self.make_small("0~4 舍，5~9 入", font_size=26, color=self.COLOR_HIGHLIGHT)
        rule_detail.move_to(DOWN * 4.4)

        self.play(Write(rule_text), run_time=0.6)
        self.play(Write(rule_detail), run_time=0.6)
        self.wait(2.0)

        self.fadeout_all(run_time=0.5)

    # ========== 场景4: 例题1 234500约等于23万 ==========

    def scene_example1(self):
        title = self.make_title("例题 1", font_size=34, color=self.COLOR_PRIMARY)
        title.move_to(UP * 6.8)

        problem = self.make_body("234500 省略万后面的尾数", font_size=25)
        problem.move_to(UP * 6.0)

        self.play(Write(title), run_time=0.4)
        self.play(Write(problem), run_time=0.6)

        # 位值标签
        place_labels = ["十万", "万", "千", "百", "十", "个"]
        digits_str = ["2", "3", "4", "5", "0", "0"]
        # 颜色: 十万和万位保持高亮，其余变暗
        digit_colors = [WHITE, self.COLOR_HIGHLIGHT, WHITE, WHITE, WHITE, WHITE]

        place_row = VGroup(*[
            Text(lbl, font="PingFang SC", font_size=20, color=self.COLOR_DIM)
            for lbl in place_labels
        ])
        place_row.arrange(RIGHT, buff=0.40)
        place_row.move_to(UP * 4.7)

        digit_row = VGroup(*[
            Text(d, font="PingFang SC", font_size=44, color=c)
            for d, c in zip(digits_str, digit_colors)
        ])
        digit_row.arrange(RIGHT, buff=0.36)
        digit_row.move_to(UP * 3.7)

        self.play(FadeIn(place_row), run_time=0.5)
        self.play(Write(digit_row), run_time=0.8)
        self.wait(0.5)

        # 分隔线（万位和千位之间）
        d_wan = digit_row[1]   # 万位 "3"
        d_qian = digit_row[2]  # 千位 "4"
        x_sep = (d_wan.get_right()[0] + d_qian.get_left()[0]) / 2
        sep_line = DashedLine(
            np.array([x_sep, 5.0, 0]),
            np.array([x_sep, 3.2, 0]),
            color=self.COLOR_HIGHLIGHT,
            dash_length=0.1,
            stroke_width=2,
        )
        self.play(Create(sep_line), run_time=0.5)

        # 指示文字
        cut_text = self.make_small("省略万后面的数", font_size=20, color=self.COLOR_ERROR)
        cut_text.move_to(UP * 2.5)
        arrow_cut = Arrow(
            cut_text.get_top() + RIGHT * 0.6,
            d_qian.get_bottom() + DOWN * 0.1,
            color=self.COLOR_ERROR,
            buff=0.05,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.2,
        )
        self.play(FadeIn(cut_text), Create(arrow_cut), run_time=0.6)
        self.wait(0.3)

        # 高亮千位
        hbox = SurroundingRectangle(d_qian, color=self.COLOR_HIGHLIGHT, buff=0.1, stroke_width=3)
        self.play(Create(hbox), run_time=0.4)

        step1 = self.make_body("千位是 4", font_size=28, color=self.COLOR_HIGHLIGHT)
        step1.move_to(UP * 1.5)
        self.play(Write(step1), run_time=0.5)

        step2 = self.make_body("4 < 5  →  舍去！", font_size=28, color=self.COLOR_ERROR)
        step2.move_to(UP * 0.7)
        self.play(Write(step2), run_time=0.6)
        self.wait(0.8)

        # 千~个位变灰
        to_dim = VGroup(digit_row[2], digit_row[3], digit_row[4], digit_row[5])
        self.play(
            to_dim.animate.set_opacity(0.2).set_color(self.COLOR_ERROR),
            FadeOut(hbox),
            run_time=0.5,
        )

        cross = Line(
            digit_row[2].get_left() + LEFT * 0.1 + DOWN * 0.1,
            digit_row[5].get_right() + RIGHT * 0.1 + DOWN * 0.1,
            color=self.COLOR_ERROR,
            stroke_width=4,
        )
        self.play(Create(cross), run_time=0.4)
        self.wait(0.4)

        # 结果
        result_label = self.make_body("结果：", font_size=26)
        result_label.move_to(DOWN * 0.3)

        res_math = MathTex(r"234500 \approx 23", color=self.COLOR_SUCCESS, font_size=44)
        res_unit = self.make_body("万", font_size=44, color=self.COLOR_SUCCESS)
        res_group = VGroup(res_math, res_unit).arrange(RIGHT, buff=0.05)
        res_group.move_to(DOWN * 1.3)

        self.play(Write(result_label), run_time=0.4)
        self.play(Write(res_group), run_time=0.9)

        explain = self.make_small("十万位2，万位3  →  保留到万位 = 23万", font_size=19, color=self.COLOR_DIM)
        explain.move_to(DOWN * 2.3)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(2.0)

        self.fadeout_all(run_time=0.5)

    # ========== 场景5: 例题2 995000000约等于10亿 ==========

    def scene_example2(self):
        title = self.make_title("例题 2", font_size=34, color=self.COLOR_PRIMARY)
        title.move_to(UP * 6.8)

        problem = self.make_body("995000000 省略亿后面的尾数", font_size=23)
        problem.move_to(UP * 6.1)

        self.play(Write(title), run_time=0.4)
        self.play(Write(problem), run_time=0.6)

        # 位值
        place_labels2 = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        digits2 = ["9", "9", "5", "0", "0", "0", "0", "0", "0"]
        colors2 = [self.COLOR_HIGHLIGHT, self.COLOR_HIGHLIGHT] + [WHITE] * 7

        place_row2 = VGroup(*[
            Text(lbl, font="PingFang SC", font_size=17, color=self.COLOR_DIM)
            for lbl in place_labels2
        ])
        place_row2.arrange(RIGHT, buff=0.19)
        place_row2.move_to(UP * 4.9)

        digit_row2 = VGroup(*[
            Text(d, font="PingFang SC", font_size=38, color=c)
            for d, c in zip(digits2, colors2)
        ])
        digit_row2.arrange(RIGHT, buff=0.24)
        digit_row2.move_to(UP * 3.9)

        self.play(FadeIn(place_row2), run_time=0.5)
        self.play(Write(digit_row2), run_time=0.9)
        self.wait(0.5)

        # 分隔线（亿位和千万位之间）
        d_yi = digit_row2[0]       # 亿位
        d_qianwan = digit_row2[1]  # 千万位
        x_sep2 = (d_yi.get_right()[0] + d_qianwan.get_left()[0]) / 2
        sep_line2 = DashedLine(
            np.array([x_sep2, 5.2, 0]),
            np.array([x_sep2, 3.4, 0]),
            color=self.COLOR_HIGHLIGHT,
            dash_length=0.1,
            stroke_width=2,
        )
        self.play(Create(sep_line2), run_time=0.5)

        # 指示文字
        look_text = self.make_small("省略亿后面的数", font_size=20, color=self.COLOR_ERROR)
        look_text.move_to(UP * 2.7)
        arrow_look = Arrow(
            look_text.get_top() + RIGHT * 0.6,
            d_qianwan.get_bottom() + DOWN * 0.1,
            color=self.COLOR_ERROR,
            buff=0.05,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.2,
        )
        self.play(FadeIn(look_text), Create(arrow_look), run_time=0.6)
        self.wait(0.4)

        # 高亮千万位
        hbox2 = SurroundingRectangle(d_qianwan, color=self.COLOR_HIGHLIGHT, buff=0.1, stroke_width=3)
        self.play(Create(hbox2), run_time=0.4)

        step1b = self.make_body("千万位是 9", font_size=28, color=self.COLOR_HIGHLIGHT)
        step1b.move_to(UP * 1.8)
        self.play(Write(step1b), run_time=0.5)

        step2b = self.make_body("9 >= 5  →  进一！", font_size=28, color=self.COLOR_SUCCESS)
        step2b.move_to(UP * 1.0)
        self.play(Write(step2b), run_time=0.6)
        self.wait(0.6)

        # 千万~个位变灰
        to_dim2 = VGroup(*digit_row2[1:])
        self.play(
            to_dim2.animate.set_opacity(0.2).set_color(self.COLOR_ERROR),
            FadeOut(hbox2),
            run_time=0.5,
        )
        cross2 = Line(
            digit_row2[1].get_left() + LEFT * 0.1 + DOWN * 0.1,
            digit_row2[8].get_right() + RIGHT * 0.1 + DOWN * 0.1,
            color=self.COLOR_ERROR,
            stroke_width=4,
        )
        self.play(Create(cross2), run_time=0.4)
        self.wait(0.3)

        # 进位说明
        carry1 = self.make_body("亿位 9 + 1 = 10", font_size=26, color=self.COLOR_ACCENT)
        carry1.move_to(UP * 0.1)
        carry2 = self.make_body("向十亿位进 1 ！", font_size=26, color=self.COLOR_ACCENT)
        carry2.move_to(DOWN * 0.7)

        self.play(Write(carry1), run_time=0.5)
        self.play(Write(carry2), run_time=0.5)
        self.wait(0.7)

        # 结果
        res2_math = MathTex(r"995000000 \approx 10", color=self.COLOR_SUCCESS, font_size=38)
        res2_unit = self.make_body("亿", font_size=42, color=self.COLOR_SUCCESS)
        res2_group = VGroup(res2_math, res2_unit).arrange(RIGHT, buff=0.05)
        res2_group.move_to(DOWN * 1.9)

        self.play(Write(res2_group), run_time=1.0)
        self.wait(0.4)

        warn = self.make_small("注意：进位后位数可能增加！", font_size=20, color=self.COLOR_HIGHLIGHT)
        warn.move_to(DOWN * 2.9)
        self.play(FadeIn(warn), run_time=0.5)
        self.wait(2.0)

        self.fadeout_all(run_time=0.5)

    # ========== 场景6: 规律总结 ==========

    def scene_summary(self):
        title = self.make_title("方法总结", font_size=40, color=self.COLOR_HIGHLIGHT)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        steps = [
            ("第一步", "确定省略到哪一位", self.COLOR_PRIMARY),
            ("第二步", "看下一位的数字", self.COLOR_ACCENT),
            ("第三步", "0~4 舍，5~9 进一", self.COLOR_SUCCESS),
        ]

        y_pos = [5.3, 4.0, 2.7]
        for (num, text, col), y in zip(steps, y_pos):
            num_t = Text(num, font="PingFang SC", font_size=26, color=col)
            body_t = Text(text, font="PingFang SC", font_size=24, color=WHITE)
            row = VGroup(num_t, body_t).arrange(RIGHT, buff=0.3)
            row.move_to(UP * y)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)

        self.wait(0.5)

        # 两例对比
        div = Line(LEFT * 3.8, RIGHT * 3.8, color=self.COLOR_DIM, stroke_width=1.5)
        div.move_to(UP * 1.6)
        self.play(Create(div), run_time=0.3)

        ex_title2 = self.make_small("两道例题回顾", font_size=22, color=self.COLOR_DIM)
        ex_title2.move_to(UP * 1.1)
        self.play(FadeIn(ex_title2), run_time=0.3)

        # 例1
        e1_n = MathTex(r"234500 \approx 23", color=WHITE, font_size=32)
        e1_u = Text("万", font="PingFang SC", font_size=32, color=self.COLOR_SUCCESS)
        e1_row = VGroup(e1_n, e1_u).arrange(RIGHT, buff=0.1)
        e1_row.move_to(UP * 0.2)
        e1_note = Text("（千位是4，舍）", font="PingFang SC", font_size=18, color=self.COLOR_DIM)
        e1_note.next_to(e1_row, DOWN, buff=0.1)

        self.play(Write(e1_row), run_time=0.7)
        self.play(FadeIn(e1_note), run_time=0.3)

        # 例2
        e2_n = MathTex(r"995000000 \approx 10", color=WHITE, font_size=28)
        e2_u = Text("亿", font="PingFang SC", font_size=32, color=self.COLOR_SUCCESS)
        e2_row = VGroup(e2_n, e2_u).arrange(RIGHT, buff=0.08)
        e2_row.move_to(DOWN * 1.3)
        e2_note = Text("（千万位是9，进一）", font="PingFang SC", font_size=18, color=self.COLOR_DIM)
        e2_note.next_to(e2_row, DOWN, buff=0.1)

        self.play(Write(e2_row), run_time=0.7)
        self.play(FadeIn(e2_note), run_time=0.3)

        self.wait(0.5)

        # 口诀框
        mnemonic_bg = RoundedRectangle(
            width=7.0,
            height=1.3,
            corner_radius=0.2,
            color=self.COLOR_ACCENT,
            fill_opacity=0.15,
            stroke_width=2,
        )
        mnemonic_bg.move_to(DOWN * 3.6)

        mnemonic = Text(
            "四舍五入  大数变简单！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_ACCENT,
        )
        mnemonic.move_to(DOWN * 3.6)

        self.play(FadeIn(mnemonic_bg), Write(mnemonic), run_time=0.8)
        self.wait(2.0)

        self.fadeout_all(run_time=0.5)

    # ========== 场景7: 片尾 ==========

    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE,
        )
        author_big.move_to(UP * 2.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_DIM,
        )
        author_id.move_to(UP * 1.5)

        self.play(
            self.author.animate.set_opacity(0),
            FadeIn(author_big, shift=DOWN * 0.3),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        )
        follow.move_to(UP * 0.2)
        self.play(FadeIn(follow, scale=1.05), run_time=0.6)

        # 装饰元素
        deco_data = [
            ("23万", LEFT * 3.0 + DOWN * 1.5, self.COLOR_SUCCESS),
            ("10亿", RIGHT * 2.5 + DOWN * 1.3, self.COLOR_SUCCESS),
            ("四舍", LEFT * 2.0 + DOWN * 2.5, self.COLOR_ERROR),
            ("五入", RIGHT * 1.2 + DOWN * 2.8, self.COLOR_PRIMARY),
            ("≈", LEFT * 0.3 + DOWN * 2.0, self.COLOR_ACCENT),
            ("万亿", RIGHT * 3.0 + DOWN * 2.5, self.COLOR_HIGHLIGHT),
        ]

        deco_mobjs = []
        for txt, pos, col in deco_data:
            t = Text(txt, font="PingFang SC", font_size=22, color=col)
            t.move_to(pos)
            deco_mobjs.append(t)

        self.play(*[FadeIn(t, scale=0.6) for t in deco_mobjs], run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow),
            *[FadeOut(t) for t in deco_mobjs],
            run_time=1.0,
        )

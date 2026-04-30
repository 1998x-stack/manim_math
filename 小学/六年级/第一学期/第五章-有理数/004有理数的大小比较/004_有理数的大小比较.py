"""
004_有理数的大小比较.py — 有理数的大小比较 教学动画

知识点: 有理数大小比较规则、数轴比较法、绝对值比较法
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 正数>0>负数 基本规则
  3. 数轴比较法 (右边>左边)
  4. 两个正数的比较
  5. 两个负数的比较 (核心难点)
  6. 绝对值比较法
  7. 综合练习
  8. 总结
  9. 片尾
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_POS = "#22c55e"        # 绿色 正数
COLOR_NEG = "#ef4444"        # 红色 负数
COLOR_ZERO = "#fbbf24"       # 黄色 零
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#a78bfa"     # 紫色强调
COLOR_RESULT = "#22c55e"     # 绿色 结果
COLOR_BLUE = "#3b82f6"       # 蓝色
COLOR_ORANGE = "#f59e0b"     # 橙色
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
COLOR_ABS = "#38bdf8"        # 天蓝 绝对值
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class RationalNumberComparisonLesson(Scene):
    """
    有理数的大小比较教学动画
    场景顺序:
      1. 开场钩子
      2. 基本规则: 正数>0>负数
      3. 数轴比较法
      4. 两个正数比较
      5. 两个负数比较 (核心难点)
      6. 绝对值比较法
      7. 综合练习
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_basic_rule()
        self.scene_3_number_line()
        self.scene_4_positive_compare()
        self.scene_5_negative_compare()
        self.scene_6_absolute_value()
        self.scene_7_practice()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子标题
        hook1 = Text(
            "有理数的大小比较",
            font=FONT, font_size=48, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "-5 和 -2，谁更大？",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)

        # 预览: 两个问号
        q_left = MathTex(r"-5", font_size=80, color=COLOR_NEG).move_to(LEFT * 2.0 + UP * 2.5)
        q_vs = Text("vs", font=FONT, font_size=40, color=GRAY_A).move_to(UP * 2.5)
        q_right = MathTex(r"-2", font_size=80, color=COLOR_NEG).move_to(RIGHT * 2.0 + UP * 2.5)

        self.play(FadeIn(q_left, scale=0.5), FadeIn(q_vs), FadeIn(q_right, scale=0.5), run_time=0.8)

        # 问号
        qmark = MathTex(r"?", font_size=100, color=COLOR_HL).move_to(UP * 0.8)
        self.play(FadeIn(qmark, scale=0.3), run_time=0.5)
        self.wait(0.8)

        hint = Text(
            "很多同学会搞反！",
            font=FONT, font_size=30, color=COLOR_ACCENT
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, q_left, q_vs, q_right, qmark, hint)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 基本规则 — 正数 > 0 > 负数
    # ------------------------------------------------------------------

    def scene_2_basic_rule(self):
        title = Text(
            "基本规则", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        # 规则1
        r1_cn = Text("正数都大于 0", font=FONT, font_size=30, color=WHITE)
        r1_cn.move_to(UP * 5.0)
        self.play(FadeIn(r1_cn), run_time=0.4)

        r1_ex = VGroup(
            MathTex(r"5", font_size=56, color=COLOR_POS),
            MathTex(r">", font_size=56, color=WHITE),
            MathTex(r"0", font_size=56, color=COLOR_ZERO),
        ).arrange(RIGHT, buff=0.4).move_to(UP * 4.0)
        self.play(Write(r1_ex), run_time=0.5)
        self.wait(0.3)

        # 规则2
        r2_cn = Text("负数都小于 0", font=FONT, font_size=30, color=WHITE)
        r2_cn.move_to(UP * 3.0)
        self.play(FadeIn(r2_cn), run_time=0.4)

        r2_ex = VGroup(
            MathTex(r"-3", font_size=56, color=COLOR_NEG),
            MathTex(r"<", font_size=56, color=WHITE),
            MathTex(r"0", font_size=56, color=COLOR_ZERO),
        ).arrange(RIGHT, buff=0.4).move_to(UP * 2.0)
        self.play(Write(r2_ex), run_time=0.5)
        self.wait(0.3)

        # 规则3
        r3_cn = Text("正数大于任何负数", font=FONT, font_size=30, color=WHITE)
        r3_cn.move_to(UP * 1.0)
        self.play(FadeIn(r3_cn), run_time=0.4)

        r3_ex = VGroup(
            MathTex(r"1", font_size=56, color=COLOR_POS),
            MathTex(r">", font_size=56, color=WHITE),
            MathTex(r"-100", font_size=56, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.4).move_to(ORIGIN)
        self.play(Write(r3_ex), run_time=0.5)
        self.wait(0.5)

        # 总结框
        summary_box = Rectangle(
            width=7.8, height=1.8,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 2.0)

        summary_formula = VGroup(
            Text("正数", font=FONT, font_size=32, color=COLOR_POS),
            MathTex(r">", font_size=44, color=WHITE),
            MathTex(r"0", font_size=44, color=COLOR_ZERO),
            MathTex(r">", font_size=44, color=WHITE),
            Text("负数", font=FONT, font_size=32, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.35).move_to(DOWN * 2.0)

        self.play(Create(summary_box), FadeIn(summary_formula), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, r1_cn, r1_ex, r2_cn, r2_ex,
            r3_cn, r3_ex, summary_box, summary_formula
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 数轴比较法
    # ------------------------------------------------------------------

    def scene_3_number_line(self):
        title = Text(
            "数轴比较法", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        subtitle = Text(
            "在数轴上，右边的数大于左边的数",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 创建数轴
        num_line = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            include_tip=True,
            font_size=24,
            tick_size=0.1,
            color=GRAY_A,
        ).move_to(UP * 3.5)

        self.play(Create(num_line), run_time=1.0)

        # 标注原点
        origin_label = Text("O", font=FONT, font_size=22, color=COLOR_ZERO)
        origin_label.next_to(num_line.n2p(0), DOWN, buff=0.35)
        self.play(FadeIn(origin_label), run_time=0.3)

        # 在数轴上标几个点
        points_data = [
            (-5, "-5", COLOR_NEG),
            (-2, "-2", COLOR_NEG),
            (0, "0", COLOR_ZERO),
            (3, "3", COLOR_POS),
            (5, "5", COLOR_POS),
        ]

        dots = []
        labels = []
        for val, label_str, col in points_data:
            dot = Dot(num_line.n2p(val), radius=0.1, color=col)
            lbl = MathTex(label_str, font_size=28, color=col)
            lbl.next_to(dot, UP, buff=0.2)
            dots.append(dot)
            labels.append(lbl)

        for dot, lbl in zip(dots, labels):
            self.play(FadeIn(dot, scale=0.5), FadeIn(lbl), run_time=0.3)
        self.wait(0.3)

        # 强调: 右边 > 左边
        arrow_right = Arrow(
            num_line.n2p(-4), num_line.n2p(4),
            buff=0, color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.08
        ).shift(DOWN * 0.7)
        arrow_label = Text(
            "越往右越大", font=FONT, font_size=24, color=COLOR_HL
        ).next_to(arrow_right, DOWN, buff=0.1)
        self.play(GrowArrow(arrow_right), FadeIn(arrow_label), run_time=0.6)
        self.wait(0.5)

        # 排列
        order = MathTex(
            r"-5", r"<", r"-2", r"<", r"0", r"<", r"3", r"<", r"5",
            font_size=46
        ).move_to(UP * 0.8)
        order[0].set_color(COLOR_NEG)
        order[2].set_color(COLOR_NEG)
        order[4].set_color(COLOR_ZERO)
        order[6].set_color(COLOR_POS)
        order[8].set_color(COLOR_POS)
        self.play(Write(order), run_time=0.8)
        self.wait(0.5)

        tip = Text(
            "数轴是比较大小的好工具！",
            font=FONT, font_size=26, color=COLOR_ACCENT
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, subtitle, num_line, origin_label,
            *dots, *labels, arrow_right, arrow_label,
            order, tip
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 两个正数比较
    # ------------------------------------------------------------------

    def scene_4_positive_compare(self):
        title = Text(
            "两个正数比较", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        rule_text = Text(
            "谁大就是谁大，很直观！",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 5.3)
        self.play(FadeIn(rule_text), run_time=0.4)

        # 例1
        ex1 = VGroup(
            MathTex(r"5", font_size=68, color=COLOR_POS),
            MathTex(r">", font_size=68, color=WHITE),
            MathTex(r"3", font_size=68, color=COLOR_POS),
        ).arrange(RIGHT, buff=0.5).move_to(UP * 4.0)
        self.play(Write(ex1), run_time=0.5)

        explain1 = Text(
            "5 比 3 大", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 3.2)
        self.play(FadeIn(explain1), run_time=0.3)

        # 例2
        ex2 = VGroup(
            MathTex(r"100", font_size=68, color=COLOR_POS),
            MathTex(r">", font_size=68, color=WHITE),
            MathTex(r"99", font_size=68, color=COLOR_POS),
        ).arrange(RIGHT, buff=0.5).move_to(UP * 2.0)
        self.play(Write(ex2), run_time=0.5)

        # 绝对值角度
        abs_box = Rectangle(
            width=7.8, height=2.0,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_POS, stroke_width=2
        ).move_to(UP * 0.2)

        abs_t = Text("两个正数比大小：", font=FONT, font_size=26, color=COLOR_POS)
        abs_c = Text("绝对值大的那个数就大", font=FONT, font_size=28, color=WHITE)
        abs_group = VGroup(abs_t, abs_c).arrange(DOWN, buff=0.2).move_to(UP * 0.2)

        self.play(Create(abs_box), FadeIn(abs_group), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, rule_text, ex1, explain1, ex2,
            abs_box, abs_group
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 5: 两个负数比较 (核心难点)
    # ------------------------------------------------------------------

    def scene_5_negative_compare(self):
        title = Text(
            "两个负数比较", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        badge = Text(
            "核心难点",
            font=FONT, font_size=22, color="#1a1a2e", weight=BOLD
        )
        badge_bg = RoundedRectangle(
            width=badge.width + 0.4, height=badge.height + 0.2,
            corner_radius=0.15,
            fill_color=COLOR_NEG, fill_opacity=1,
            stroke_width=0
        )
        badge_group = VGroup(badge_bg, badge).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), FadeIn(badge_group, scale=0.5), run_time=0.5)

        # 规则
        rule = Text(
            "绝对值大的负数反而小！",
            font=FONT, font_size=30, color=COLOR_NEG
        ).move_to(UP * 4.7)
        self.play(Write(rule), run_time=0.6)

        # 数轴演示
        num_line = NumberLine(
            x_range=[-6, 1, 1],
            length=7.0,
            include_numbers=True,
            include_tip=True,
            font_size=22,
            tick_size=0.1,
            color=GRAY_A,
        ).move_to(UP * 3.3)
        self.play(Create(num_line), run_time=0.7)

        # 标点
        dot_m5 = Dot(num_line.n2p(-5), radius=0.12, color=COLOR_NEG)
        dot_m2 = Dot(num_line.n2p(-2), radius=0.12, color=COLOR_ORANGE)
        dot_0 = Dot(num_line.n2p(0), radius=0.08, color=COLOR_ZERO)

        lbl_m5 = MathTex(r"-5", font_size=32, color=COLOR_NEG).next_to(dot_m5, UP, buff=0.2)
        lbl_m2 = MathTex(r"-2", font_size=32, color=COLOR_ORANGE).next_to(dot_m2, UP, buff=0.2)

        self.play(
            FadeIn(dot_m5, scale=0.5), FadeIn(lbl_m5),
            FadeIn(dot_m2, scale=0.5), FadeIn(lbl_m2),
            FadeIn(dot_0),
            run_time=0.5
        )

        # 强调 -2 在 -5 右边
        arrow = Arrow(
            num_line.n2p(-5) + DOWN * 0.4,
            num_line.n2p(-2) + DOWN * 0.4,
            buff=0.1, color=COLOR_HL, stroke_width=3
        )
        arrow_lbl = Text(
            "-2 在 -5 的右边", font=FONT, font_size=22, color=COLOR_HL
        ).next_to(arrow, DOWN, buff=0.1)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.5)
        self.wait(0.3)

        # 结论
        concl = MathTex(r"-2", r">", r"-5", font_size=72).move_to(UP * 1.2)
        concl[0].set_color(COLOR_ORANGE)
        concl[2].set_color(COLOR_NEG)
        self.play(Write(concl), run_time=0.6)
        self.wait(0.3)

        # 解释为什么
        why_title = Text("为什么？", font=FONT, font_size=28, color=COLOR_ACCENT).move_to(UP * 0.2)
        self.play(FadeIn(why_title), run_time=0.3)

        # 温度比喻
        temp_box = Rectangle(
            width=7.8, height=3.2,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_ACCENT, stroke_width=2
        ).move_to(DOWN * 2.0)

        temp_t = Text("想想温度计：", font=FONT, font_size=26, color=COLOR_ACCENT)

        temp_line1 = VGroup(
            MathTex(r"-2", font_size=40, color=COLOR_ORANGE),
            Text("  表示零下 2 度", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.15)

        temp_line2 = VGroup(
            MathTex(r"-5", font_size=40, color=COLOR_NEG),
            Text("  表示零下 5 度", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.15)

        temp_line3 = Text(
            "零下 2 度比零下 5 度暖和！",
            font=FONT, font_size=26, color=COLOR_HL
        )

        temp_content = VGroup(temp_t, temp_line1, temp_line2, temp_line3).arrange(
            DOWN, buff=0.25, aligned_edge=LEFT
        ).move_to(DOWN * 2.0)

        self.play(Create(temp_box), FadeIn(temp_content), run_time=0.7)
        self.wait(1.5)

        # 更多例子
        self.play(FadeOut(VGroup(
            num_line, dot_m5, dot_m2, dot_0,
            lbl_m5, lbl_m2, arrow, arrow_lbl,
            concl, why_title, temp_box, temp_content
        )), run_time=0.4)

        more_title = Text(
            "更多例子", font=FONT, font_size=32, color=WHITE
        ).move_to(UP * 5.0)
        self.play(FadeIn(more_title), run_time=0.3)

        examples = [
            (r"-1", r">", r"-3", "|-1|=1 < |-3|=3"),
            (r"-10", r"<", r"-7", "|-10|=10 > |-7|=7"),
            (r"-0.5", r">", r"-2", "|-0.5|=0.5 < |-2|=2"),
        ]

        ex_groups = VGroup()
        for i, (a, op, b, reason) in enumerate(examples):
            eq = VGroup(
                MathTex(a, font_size=52, color=COLOR_NEG),
                MathTex(op, font_size=52, color=WHITE),
                MathTex(b, font_size=52, color=COLOR_NEG),
            ).arrange(RIGHT, buff=0.3)
            reason_text = Text(reason, font=FONT, font_size=20, color=GRAY_A)
            row = VGroup(eq, reason_text).arrange(RIGHT, buff=0.5)
            ex_groups.add(row)

        ex_groups.arrange(DOWN, buff=0.7).move_to(UP * 3.0)
        for row in ex_groups:
            self.play(FadeIn(row), run_time=0.5)
            self.wait(0.3)

        # 结论框
        rule_box = RoundedRectangle(
            width=7.8, height=2.2, corner_radius=0.2,
            fill_color="#3b1020", fill_opacity=0.9,
            stroke_color=COLOR_NEG, stroke_width=2.5
        ).move_to(DOWN * 0.5)

        rule_t1 = Text("两个负数比大小：", font=FONT, font_size=28, color=COLOR_NEG)
        rule_t2 = Text("绝对值大的反而小", font=FONT, font_size=30, color=WHITE, weight=BOLD)
        rule_content = VGroup(rule_t1, rule_t2).arrange(DOWN, buff=0.2).move_to(DOWN * 0.5)

        self.play(Create(rule_box), FadeIn(rule_content), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, badge_group, rule, more_title, ex_groups,
            rule_box, rule_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 绝对值比较法
    # ------------------------------------------------------------------

    def scene_6_absolute_value(self):
        title = Text(
            "绝对值比较法", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        subtitle = Text(
            "用绝对值帮助比较大小",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 5.3)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 步骤卡片
        step1_box = Rectangle(
            width=7.8, height=1.6,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_BLUE, stroke_width=2
        ).move_to(UP * 3.8)
        s1_num = Text("1", font=FONT, font_size=28, color=COLOR_BLUE, weight=BOLD)
        s1_cn = Text("先求两个数的绝对值", font=FONT, font_size=26, color=WHITE)
        s1_row = VGroup(s1_num, s1_cn).arrange(RIGHT, buff=0.3).move_to(UP * 3.8)
        self.play(Create(step1_box), FadeIn(s1_row), run_time=0.4)

        step2_box = Rectangle(
            width=7.8, height=1.6,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_BLUE, stroke_width=2
        ).move_to(UP * 2.0)
        s2_num = Text("2", font=FONT, font_size=28, color=COLOR_BLUE, weight=BOLD)
        s2_cn = Text("比较绝对值的大小", font=FONT, font_size=26, color=WHITE)
        s2_row = VGroup(s2_num, s2_cn).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)
        self.play(Create(step2_box), FadeIn(s2_row), run_time=0.4)

        step3_box = Rectangle(
            width=7.8, height=1.6,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_BLUE, stroke_width=2
        ).move_to(UP * 0.2)
        s3_num = Text("3", font=FONT, font_size=28, color=COLOR_BLUE, weight=BOLD)
        s3_cn = Text("根据规则得出结论", font=FONT, font_size=26, color=WHITE)
        s3_row = VGroup(s3_num, s3_cn).arrange(RIGHT, buff=0.3).move_to(UP * 0.2)
        self.play(Create(step3_box), FadeIn(s3_row), run_time=0.4)
        self.wait(0.5)

        # 示例
        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(DOWN * 0.8)
        self.play(Create(sep), run_time=0.2)

        ex_title_t = Text("例：比较", font=FONT, font_size=26, color=GRAY_A)
        ex_title_eq = MathTex(r"-5", font_size=44, color=COLOR_NEG)
        ex_title_mid = Text("和", font=FONT, font_size=26, color=GRAY_A)
        ex_title_eq2 = MathTex(r"-2", font_size=44, color=COLOR_NEG)
        ex_title_row = VGroup(ex_title_t, ex_title_eq, ex_title_mid, ex_title_eq2).arrange(
            RIGHT, buff=0.2
        ).move_to(DOWN * 1.3)
        self.play(FadeIn(ex_title_row), run_time=0.4)

        # 步骤1
        st1 = MathTex(r"|-5| = 5, \quad |-2| = 2", font_size=42, color=COLOR_ABS).move_to(DOWN * 2.3)
        self.play(Write(st1), run_time=0.6)

        # 步骤2
        st2 = MathTex(r"5 > 2", font_size=42, color=WHITE).move_to(DOWN * 3.2)
        self.play(Write(st2), run_time=0.4)

        # 步骤3
        st3_cn = Text("绝对值大的负数反而小：", font=FONT, font_size=22, color=GRAY_A)
        st3_eq = MathTex(r"-5 < -2", font_size=56, color=COLOR_RESULT)
        st3_group = VGroup(st3_cn, st3_eq).arrange(DOWN, buff=0.15).move_to(DOWN * 4.6)
        self.play(FadeIn(st3_group), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, subtitle,
            step1_box, s1_row, step2_box, s2_row, step3_box, s3_row,
            sep, ex_title_row, st1, st2, st3_group
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 7: 综合练习
    # ------------------------------------------------------------------

    def scene_7_practice(self):
        title = Text(
            "练一练", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.3)

        subtitle = Text(
            "在下面填入 > 或 <",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.3)

        problems = [
            (r"3", r"", r"-8", r">", "positive_gt_negative"),
            (r"-4", r"", r"0", r"<", "negative_lt_zero"),
            (r"-3", r"", r"-7", r">", "neg_abs_small_gt"),
            (r"-10", r"", r"-1", r"<", "neg_abs_big_lt"),
        ]

        y_start = 4.2
        y_step = 1.8
        all_elements = VGroup()

        for i, (a, _, b, answer, _) in enumerate(problems):
            y_pos = y_start - i * y_step

            num_label = Text(f"({i+1})", font=FONT, font_size=24, color=GRAY_A)
            num_label.move_to(LEFT * 3.8 + UP * y_pos)

            lhs = MathTex(a, font_size=56)
            if a.startswith("-"):
                lhs.set_color(COLOR_NEG)
            else:
                lhs.set_color(COLOR_POS)

            blank = RoundedRectangle(
                width=0.9, height=0.7, corner_radius=0.1,
                fill_color="#2d3748", fill_opacity=0.8,
                stroke_color=GRAY_B, stroke_width=1.5
            )

            rhs = MathTex(b, font_size=56)
            if b.startswith("-"):
                rhs.set_color(COLOR_NEG)
            elif b == "0":
                rhs.set_color(COLOR_ZERO)
            else:
                rhs.set_color(COLOR_POS)

            row = VGroup(lhs, blank, rhs).arrange(RIGHT, buff=0.35)
            row.move_to(RIGHT * 0.2 + UP * y_pos)

            q_group = VGroup(num_label, row)
            all_elements.add(q_group)
            self.play(FadeIn(q_group), run_time=0.4)

        self.wait(0.8)

        # 逐题揭晓答案
        answer_mobs = VGroup()
        for i, (a, _, b, answer, _) in enumerate(problems):
            y_pos = y_start - i * y_step

            ans_mob = MathTex(answer, font_size=52, color=COLOR_RESULT)
            # Position at the blank
            blank_center = all_elements[i][1][1].get_center()
            ans_mob.move_to(blank_center)
            answer_mobs.add(ans_mob)

            self.play(FadeIn(ans_mob, scale=0.5), run_time=0.4)

            # checkmark
            check = MathTex(r"\checkmark", font_size=36, color=COLOR_RESULT)
            check.next_to(all_elements[i][1], RIGHT, buff=0.4)
            answer_mobs.add(check)
            self.play(FadeIn(check), run_time=0.2)
            self.wait(0.2)

        self.wait(1.0)

        self.play(FadeOut(VGroup(title, subtitle, all_elements, answer_mobs)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        title = Text(
            "总结", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        # 卡片1: 基本顺序
        card1 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=COLOR_POS, stroke_width=2.5
        ).move_to(UP * 4.8)
        c1_t = Text("基本顺序", font=FONT, font_size=28, color=COLOR_POS)
        c1_row = VGroup(
            Text("正数", font=FONT, font_size=28, color=COLOR_POS),
            MathTex(r">", font_size=36, color=WHITE),
            MathTex(r"0", font_size=36, color=COLOR_ZERO),
            MathTex(r">", font_size=36, color=WHITE),
            Text("负数", font=FONT, font_size=28, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.25)
        c1_content = VGroup(c1_t, c1_row).arrange(DOWN, buff=0.15).move_to(UP * 4.8)
        self.play(Create(card1), FadeIn(c1_content), run_time=0.5)

        # 卡片2: 两个正数
        card2 = Rectangle(
            width=7.8, height=1.6,
            fill_color="#14532d", fill_opacity=0.9,
            stroke_color=COLOR_POS, stroke_width=2.5
        ).move_to(UP * 2.8)
        c2_t = Text("两个正数", font=FONT, font_size=26, color=COLOR_POS)
        c2_c = Text("绝对值大的数大", font=FONT, font_size=26, color=WHITE)
        c2_content = VGroup(c2_t, c2_c).arrange(DOWN, buff=0.12).move_to(UP * 2.8)
        self.play(Create(card2), FadeIn(c2_content), run_time=0.5)

        # 卡片3: 两个负数 (重点)
        card3 = Rectangle(
            width=7.8, height=2.2,
            fill_color="#3b1020", fill_opacity=0.9,
            stroke_color=COLOR_NEG, stroke_width=3
        ).move_to(UP * 0.7)
        c3_t = Text("两个负数", font=FONT, font_size=28, color=COLOR_NEG, weight=BOLD)
        c3_c = Text("绝对值大的反而小！", font=FONT, font_size=28, color=WHITE, weight=BOLD)
        c3_ex = MathTex(
            r"|-5|>|-2|", font_size=38, color=COLOR_ABS
        )
        c3_but_t = Text("但", font=FONT, font_size=26, color=GRAY_A)
        c3_but_eq = MathTex(r"-5<-2", font_size=38, color=COLOR_NEG)
        c3_but = VGroup(c3_but_t, c3_but_eq).arrange(RIGHT, buff=0.15)
        c3_content = VGroup(c3_t, c3_c, c3_ex, c3_but).arrange(DOWN, buff=0.12).move_to(UP * 0.7)
        self.play(Create(card3), FadeIn(c3_content), run_time=0.6)

        # 卡片4: 数轴法
        card4 = Rectangle(
            width=7.8, height=1.6,
            fill_color="#1e1b4b", fill_opacity=0.9,
            stroke_color=COLOR_ACCENT, stroke_width=2.5
        ).move_to(DOWN * 1.4)
        c4_t = Text("数轴法", font=FONT, font_size=26, color=COLOR_ACCENT)
        c4_c = Text("右边的数 > 左边的数", font=FONT, font_size=26, color=WHITE)
        c4_content = VGroup(c4_t, c4_c).arrange(DOWN, buff=0.12).move_to(DOWN * 1.4)
        self.play(Create(card4), FadeIn(c4_content), run_time=0.5)

        self.wait(2.0)

        self.play(FadeOut(VGroup(
            title,
            card1, c1_content,
            card2, c2_content,
            card3, c3_content,
            card4, c4_content
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(Transform(self.author_mob, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，学更多数学技巧！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.5)

        # 装饰: 数轴上的数
        deco = VGroup(
            MathTex(r"-5", font_size=42, color=COLOR_NEG).shift(LEFT * 3.0 + DOWN * 2.4),
            MathTex(r"<", font_size=42, color=WHITE).shift(LEFT * 1.5 + DOWN * 2.4),
            MathTex(r"-2", font_size=42, color=COLOR_NEG).shift(ORIGIN + DOWN * 2.4),
            MathTex(r"<", font_size=42, color=WHITE).shift(RIGHT * 1.5 + DOWN * 2.4),
            MathTex(r"3", font_size=42, color=COLOR_POS).shift(RIGHT * 3.0 + DOWN * 2.4),
        )
        self.play(*[FadeIn(f, scale=0.5) for f in deco], run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=0.8
        )

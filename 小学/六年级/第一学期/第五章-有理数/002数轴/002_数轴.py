"""
002_数轴.py -- 数轴 教学动画

知识点: 数轴三要素(原点、正方向、单位长度)、有理数与数轴上的点对应、利用数轴比较大小
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 数轴的由来 -- 从直线到数轴
  3. 三要素之一: 原点
  4. 三要素之二: 正方向
  5. 三要素之三: 单位长度
  6. 在数轴上表示有理数
  7. 利用数轴比较大小
  8. 练一练
  9. 总结
  10. 片尾
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
COLOR_ORIGIN = "#fbbf24"       # 黄色 原点
COLOR_POS_DIR = "#22c55e"      # 绿色 正方向
COLOR_UNIT = "#3b82f6"         # 蓝色 单位长度
COLOR_POS = "#22c55e"          # 绿色 正数
COLOR_NEG = "#ef4444"          # 红色 负数
COLOR_ZERO = "#fbbf24"         # 黄色 零
COLOR_HL = "#fbbf24"           # 黄色高亮
COLOR_ACCENT = "#a78bfa"       # 紫色强调
COLOR_RESULT = "#22c55e"       # 绿色 结果
COLOR_AUTHOR = "#6b7280"       # 灰色作者信息
COLOR_TITLE = "#fbbf24"        # 金色 标题
COLOR_COMPARE = "#f97316"      # 橙色 比较
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class NumberLineLesson(Scene):
    """
    数轴教学动画
    场景顺序:
      1. 开场钩子
      2. 数轴的由来
      3. 三要素之一: 原点
      4. 三要素之二: 正方向
      5. 三要素之三: 单位长度
      6. 在数轴上表示有理数
      7. 利用数轴比较大小
      8. 练一练
      9. 总结
      10. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_origin_of_number_line()
        self.scene_3_origin()
        self.scene_4_positive_direction()
        self.scene_5_unit_length()
        self.scene_6_represent_rationals()
        self.scene_7_compare_size()
        self.scene_8_practice()
        self.scene_9_summary()
        self.scene_10_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook1 = Text(
            "一条直线",
            font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 4.5)

        hook2 = Text(
            "如何装下所有的数?",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 3.5)

        self.play(Write(hook1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        # 一条简单直线
        simple_line = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE, stroke_width=3)
        simple_line.move_to(UP * 1.5)
        self.play(Create(simple_line), run_time=1.0)
        self.wait(0.3)

        # 撒一些数在周围
        numbers_data = [
            ("3", LEFT * 2 + DOWN * 0.5, COLOR_POS),
            ("-2", RIGHT * 2.5 + DOWN * 1.0, COLOR_NEG),
            ("0", LEFT * 0.5 + UP * 0.0, COLOR_ZERO),
            (r"\frac{1}{2}", RIGHT * 1 + DOWN * 0.3, COLOR_ACCENT),
            ("-4.5", LEFT * 3 + DOWN * 1.5, COLOR_NEG),
        ]
        num_mobs = VGroup()
        for txt, pos, col in numbers_data:
            m = MathTex(txt, font_size=30, color=col).move_to(pos)
            num_mobs.add(m)
            self.play(FadeIn(m, scale=0.5), run_time=0.25)

        self.wait(0.3)

        answer = Text(
            "答案就是 —— 数轴!",
            font=FONT, font_size=36, color=COLOR_ACCENT
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(answer, scale=1.1), run_time=0.7)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(simple_line), FadeOut(num_mobs),
            FadeOut(answer),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 数轴的由来 -- 从直线到数轴
    # ------------------------------------------------------------------
    def scene_2_origin_of_number_line(self):
        title = Text(
            "从直线到数轴", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 一条普通直线
        plain_line = Line(LEFT * 4, RIGHT * 4, color=GRAY_B, stroke_width=3)
        plain_line.move_to(UP * 3.0)
        self.play(Create(plain_line), run_time=0.8)

        step1 = Text(
            "一条普通的直线...", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 1.8)
        self.play(FadeIn(step1), run_time=0.5)
        self.wait(0.5)

        # 加上原点
        origin_dot = Dot(plain_line.get_center(), color=COLOR_ORIGIN, radius=0.15)
        origin_label = MathTex("0", font_size=28, color=COLOR_ORIGIN).next_to(origin_dot, DOWN, buff=0.2)

        step2 = Text(
            "选一个点, 标记为原点 0",
            font=FONT, font_size=24, color=COLOR_ORIGIN
        ).move_to(UP * 0.8)
        self.play(FadeIn(origin_dot, scale=0.5), Write(origin_label), run_time=0.5)
        self.play(FadeIn(step2), run_time=0.5)
        self.wait(0.5)

        # 加上箭头 (正方向)
        arrow_line = Arrow(
            LEFT * 4 + UP * 3.0,
            RIGHT * 4 + UP * 3.0,
            color=WHITE, stroke_width=3,
            buff=0, tip_length=0.2
        )
        step3 = Text(
            "规定向右为正方向",
            font=FONT, font_size=24, color=COLOR_POS_DIR
        ).move_to(DOWN * 0.2)
        self.play(
            FadeOut(plain_line),
            Create(arrow_line),
            run_time=0.6
        )
        self.play(FadeIn(step3), run_time=0.5)
        self.wait(0.5)

        # 加上刻度 (单位长度)
        ticks = VGroup()
        tick_labels = VGroup()
        for i in range(-4, 5):
            x_pos = arrow_line.get_center()[0] + i * 0.9
            tick = Line(
                UP * 0.12 + UP * 3.0 + RIGHT * (i * 0.9),
                DOWN * 0.12 + UP * 3.0 + RIGHT * (i * 0.9),
                color=WHITE, stroke_width=2
            )
            ticks.add(tick)
            if i != 0:
                lbl = MathTex(str(i), font_size=20, color=WHITE).next_to(tick, DOWN, buff=0.15)
                tick_labels.add(lbl)

        step4 = Text(
            "标上等距的刻度",
            font=FONT, font_size=24, color=COLOR_UNIT
        ).move_to(DOWN * 1.2)

        self.play(Create(ticks), run_time=0.6)
        self.play(FadeIn(tick_labels), FadeIn(step4), run_time=0.5)
        self.wait(0.5)

        # 结论
        conclusion = Text(
            "数轴诞生了!",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(conclusion, scale=1.1), run_time=0.7)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(arrow_line),
            FadeOut(origin_dot), FadeOut(origin_label),
            FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
            FadeOut(ticks), FadeOut(tick_labels),
            FadeOut(conclusion),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 三要素之一 -- 原点
    # ------------------------------------------------------------------
    def scene_3_origin(self):
        title = Text(
            "三要素之一: 原点", font=FONT, font_size=36, color=COLOR_ORIGIN
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-5, 5, 1],
            length=7.5,
            include_numbers=True,
            font_size=22,
            color=WHITE,
            include_tip=True,
        ).move_to(UP * 3.0)
        self.play(Create(nl), run_time=0.8)

        # 高亮原点
        origin_dot = Dot(nl.n2p(0), color=COLOR_ORIGIN, radius=0.18)
        origin_label = Text(
            "原点", font=FONT, font_size=24, color=COLOR_ORIGIN
        ).next_to(origin_dot, DOWN, buff=0.35)
        self.play(FadeIn(origin_dot, scale=0.5), run_time=0.4)
        self.play(
            Flash(origin_dot, color=COLOR_ORIGIN, flash_radius=0.4),
            FadeIn(origin_label),
            run_time=0.6
        )
        self.wait(0.3)

        # 说明
        explain1 = Text(
            "原点是数轴的起始点",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 1.0)
        explain2 = Text(
            "用 0 表示",
            font=FONT, font_size=26, color=COLOR_ORIGIN
        ).move_to(UP * 0.2)
        explain3 = Text(
            "所有数都以原点为基准",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.8)

        self.play(Write(explain1), run_time=0.6)
        self.play(Write(explain2), run_time=0.5)
        self.play(FadeIn(explain3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 左侧: 负 / 右侧: 正
        neg_text = Text(
            "负数", font=FONT, font_size=22, color=COLOR_NEG
        ).move_to(DOWN * 2.0 + LEFT * 2.5)
        pos_text = Text(
            "正数", font=FONT, font_size=22, color=COLOR_POS
        ).move_to(DOWN * 2.0 + RIGHT * 2.5)
        zero_text = Text(
            "零", font=FONT, font_size=22, color=COLOR_ZERO
        ).move_to(DOWN * 2.0)

        neg_arrow = Arrow(
            DOWN * 2.0 + LEFT * 0.8, DOWN * 2.0 + LEFT * 1.8,
            color=COLOR_NEG, stroke_width=3, tip_length=0.15, buff=0
        )
        pos_arrow = Arrow(
            DOWN * 2.0 + RIGHT * 0.8, DOWN * 2.0 + RIGHT * 1.8,
            color=COLOR_POS, stroke_width=3, tip_length=0.15, buff=0
        )

        self.play(
            FadeIn(neg_text), FadeIn(pos_text), FadeIn(zero_text),
            GrowFromCenter(neg_arrow), GrowFromCenter(pos_arrow),
            run_time=0.7
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(explain1), FadeOut(explain2), FadeOut(explain3),
            FadeOut(neg_text), FadeOut(pos_text), FadeOut(zero_text),
            FadeOut(neg_arrow), FadeOut(pos_arrow),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 三要素之二 -- 正方向
    # ------------------------------------------------------------------
    def scene_4_positive_direction(self):
        title = Text(
            "三要素之二: 正方向", font=FONT, font_size=36, color=COLOR_POS_DIR
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-5, 5, 1],
            length=7.5,
            include_numbers=True,
            font_size=22,
            color=WHITE,
            include_tip=True,
        ).move_to(UP * 3.0)
        self.play(Create(nl), run_time=0.8)

        # 高亮箭头方向
        big_arrow = Arrow(
            RIGHT * 1.0 + UP * 4.3,
            RIGHT * 3.5 + UP * 4.3,
            color=COLOR_POS_DIR, stroke_width=5, tip_length=0.25, buff=0
        )
        dir_label = Text(
            "正方向", font=FONT, font_size=28, color=COLOR_POS_DIR
        ).next_to(big_arrow, UP, buff=0.15)

        self.play(GrowFromCenter(big_arrow), FadeIn(dir_label), run_time=0.7)
        self.wait(0.3)

        # 说明
        explain1 = Text(
            "通常规定向右为正方向",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 1.0)
        explain2 = Text(
            "用箭头表示",
            font=FONT, font_size=26, color=COLOR_POS_DIR
        ).move_to(UP * 0.2)

        self.play(Write(explain1), run_time=0.6)
        self.play(Write(explain2), run_time=0.5)
        self.wait(0.5)

        # 动画: 一个点沿正方向移动
        moving_dot = Dot(nl.n2p(-3), color=COLOR_POS_DIR, radius=0.12)
        self.play(FadeIn(moving_dot, scale=0.5), run_time=0.3)

        trail = TracedPath(moving_dot.get_center, stroke_color=COLOR_POS_DIR, stroke_width=3)
        self.add(trail)
        self.play(moving_dot.animate.move_to(nl.n2p(4)), run_time=1.5, rate_func=smooth)
        self.remove(trail)

        move_text = Text(
            "沿正方向: 数越来越大",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(move_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 反方向
        reverse_text = Text(
            "反方向 (向左): 数越来越小",
            font=FONT, font_size=24, color=COLOR_NEG
        ).move_to(DOWN * 2.8)
        self.play(
            moving_dot.animate.move_to(nl.n2p(-3)),
            FadeIn(reverse_text, shift=UP * 0.2),
            run_time=1.2
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl),
            FadeOut(big_arrow), FadeOut(dir_label),
            FadeOut(explain1), FadeOut(explain2),
            FadeOut(moving_dot), FadeOut(move_text), FadeOut(reverse_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 三要素之三 -- 单位长度
    # ------------------------------------------------------------------
    def scene_5_unit_length(self):
        title = Text(
            "三要素之三: 单位长度", font=FONT, font_size=36, color=COLOR_UNIT
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-5, 5, 1],
            length=7.5,
            include_numbers=True,
            font_size=22,
            color=WHITE,
            include_tip=True,
        ).move_to(UP * 3.0)
        self.play(Create(nl), run_time=0.8)

        # 高亮单位长度
        unit_brace = BraceBetweenPoints(
            nl.n2p(0), nl.n2p(1), direction=DOWN, color=COLOR_UNIT
        )
        unit_label = Text(
            "1 个单位长度", font=FONT, font_size=22, color=COLOR_UNIT
        ).next_to(unit_brace, DOWN, buff=0.1)

        self.play(GrowFromCenter(unit_brace), FadeIn(unit_label), run_time=0.6)
        self.wait(0.3)

        # 说明
        explain1 = Text(
            "相邻两个整数刻度之间",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 0.8)
        explain2 = Text(
            "的距离都是相等的",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 0.1)

        self.play(Write(explain1), run_time=0.6)
        self.play(Write(explain2), run_time=0.5)
        self.wait(0.5)

        # 高亮多个单位长度
        braces = VGroup()
        for i in range(-3, 3):
            b = BraceBetweenPoints(
                nl.n2p(i), nl.n2p(i + 1), direction=DOWN, color=COLOR_UNIT
            )
            braces.add(b)

        self.play(
            FadeOut(unit_brace), FadeOut(unit_label),
            run_time=0.3
        )
        self.play(
            *[GrowFromCenter(b) for b in braces],
            run_time=0.8
        )

        equal_text = Text(
            "每段都相等!", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(equal_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 重要提示
        tip = Text(
            "单位长度可以不同,",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.0)
        tip2 = Text(
            "但同一数轴上必须一致!",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(tip), run_time=0.5)
        self.play(FadeIn(tip2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl),
            FadeOut(braces),
            FadeOut(explain1), FadeOut(explain2),
            FadeOut(equal_text), FadeOut(tip), FadeOut(tip2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 在数轴上表示有理数
    # ------------------------------------------------------------------
    def scene_6_represent_rationals(self):
        title = Text(
            "在数轴上表示有理数", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-5, 5, 1],
            length=7.5,
            include_numbers=True,
            font_size=22,
            color=WHITE,
            include_tip=True,
        ).move_to(UP * 3.5)
        origin_dot = Dot(nl.n2p(0), color=COLOR_ZERO, radius=0.14)
        self.play(Create(nl), FadeIn(origin_dot), run_time=0.7)

        # 正整数 +3
        dot_3 = Dot(nl.n2p(3), color=COLOR_POS, radius=0.12)
        lbl_3 = MathTex("+3", font_size=28, color=COLOR_POS).next_to(dot_3, UP, buff=0.2)
        note_3 = Text(
            "正数在原点右侧", font=FONT, font_size=22, color=COLOR_POS
        ).move_to(UP * 1.5)

        self.play(FadeIn(dot_3, scale=0.5), Write(lbl_3), run_time=0.5)
        self.play(FadeIn(note_3, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 负整数 -2
        dot_m2 = Dot(nl.n2p(-2), color=COLOR_NEG, radius=0.12)
        lbl_m2 = MathTex("-2", font_size=28, color=COLOR_NEG).next_to(dot_m2, UP, buff=0.2)
        note_m2 = Text(
            "负数在原点左侧", font=FONT, font_size=22, color=COLOR_NEG
        ).move_to(UP * 0.5)

        self.play(FadeIn(dot_m2, scale=0.5), Write(lbl_m2), run_time=0.5)
        self.play(FadeIn(note_m2, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 分数 1/2
        dot_half = Dot(nl.n2p(0.5), color=COLOR_ACCENT, radius=0.12)
        lbl_half = MathTex(r"\frac{1}{2}", font_size=26, color=COLOR_ACCENT).next_to(dot_half, DOWN, buff=0.35)

        note_frac = Text(
            "分数也能表示!", font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(dot_half, scale=0.5), Write(lbl_half), run_time=0.5)
        self.play(FadeIn(note_frac, shift=UP * 0.2), run_time=0.4)
        self.wait(0.3)

        # 负分数 -3.5
        dot_m35 = Dot(nl.n2p(-3.5), color=COLOR_NEG, radius=0.12)
        lbl_m35 = MathTex(r"-3.5", font_size=24, color=COLOR_NEG).next_to(dot_m35, DOWN, buff=0.35)

        self.play(FadeIn(dot_m35, scale=0.5), Write(lbl_m35), run_time=0.5)
        self.wait(0.3)

        # 核心结论
        key = Text(
            "任何有理数都可以用",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 2.0)
        key2 = Text(
            "数轴上的一个点表示!",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 2.8)
        key_box = SurroundingRectangle(
            VGroup(key, key2), color=COLOR_HL, buff=0.2, corner_radius=0.1
        )

        self.play(Write(key), run_time=0.6)
        self.play(Write(key2), Create(key_box), run_time=0.6)
        self.wait(0.5)

        # 数形结合
        concept = Text(
            "数形结合", font=FONT, font_size=32, color=COLOR_ACCENT
        ).move_to(DOWN * 4.5)
        concept_desc = Text(
            "把 \"数\" 和 \"形\" 联系起来",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 5.3)

        self.play(FadeIn(concept, scale=1.1), run_time=0.5)
        self.play(FadeIn(concept_desc), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(dot_3), FadeOut(lbl_3), FadeOut(note_3),
            FadeOut(dot_m2), FadeOut(lbl_m2), FadeOut(note_m2),
            FadeOut(dot_half), FadeOut(lbl_half), FadeOut(note_frac),
            FadeOut(dot_m35), FadeOut(lbl_m35),
            FadeOut(key), FadeOut(key2), FadeOut(key_box),
            FadeOut(concept), FadeOut(concept_desc),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 利用数轴比较大小
    # ------------------------------------------------------------------
    def scene_7_compare_size(self):
        title = Text(
            "利用数轴比较大小", font=FONT, font_size=36, color=COLOR_COMPARE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-5, 5, 1],
            length=7.5,
            include_numbers=True,
            font_size=22,
            color=WHITE,
            include_tip=True,
        ).move_to(UP * 3.5)
        self.play(Create(nl), run_time=0.7)

        # 核心规则
        rule = Text(
            "右边的数 > 左边的数",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 1.8)
        rule_box = SurroundingRectangle(rule, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(Write(rule), Create(rule_box), run_time=0.7)
        self.wait(0.5)

        # 示例1: 3 > -1
        dot_3 = Dot(nl.n2p(3), color=COLOR_POS, radius=0.12)
        dot_m1 = Dot(nl.n2p(-1), color=COLOR_NEG, radius=0.12)
        lbl_3 = MathTex("3", font_size=26, color=COLOR_POS).next_to(dot_3, UP, buff=0.2)
        lbl_m1 = MathTex("-1", font_size=26, color=COLOR_NEG).next_to(dot_m1, UP, buff=0.2)

        self.play(
            FadeIn(dot_3, scale=0.5), FadeIn(dot_m1, scale=0.5),
            Write(lbl_3), Write(lbl_m1),
            run_time=0.5
        )

        # 箭头: -1 在左, 3 在右
        compare_arrow = Arrow(
            nl.n2p(-1) + DOWN * 0.6,
            nl.n2p(3) + DOWN * 0.6,
            color=COLOR_COMPARE, stroke_width=3, tip_length=0.15, buff=0
        )
        compare_text = MathTex(
            r"3 > -1", font_size=36, color=COLOR_COMPARE
        ).move_to(DOWN * 0.3)

        self.play(GrowFromCenter(compare_arrow), run_time=0.5)
        self.play(Write(compare_text), run_time=0.5)
        self.wait(0.8)

        # 清理示例1
        self.play(
            FadeOut(dot_3), FadeOut(dot_m1),
            FadeOut(lbl_3), FadeOut(lbl_m1),
            FadeOut(compare_arrow), FadeOut(compare_text),
            run_time=0.4
        )

        # 示例2: -2 > -4 (比较两个负数)
        dot_m2 = Dot(nl.n2p(-2), color=COLOR_NEG, radius=0.12)
        dot_m4 = Dot(nl.n2p(-4), color=COLOR_NEG, radius=0.12)
        lbl_m2 = MathTex("-2", font_size=26, color=COLOR_NEG).next_to(dot_m2, UP, buff=0.2)
        lbl_m4 = MathTex("-4", font_size=26, color=COLOR_NEG).next_to(dot_m4, UP, buff=0.2)

        self.play(
            FadeIn(dot_m2, scale=0.5), FadeIn(dot_m4, scale=0.5),
            Write(lbl_m2), Write(lbl_m4),
            run_time=0.5
        )

        hint = Text(
            "两个负数怎么比?", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        compare_arrow2 = Arrow(
            nl.n2p(-4) + DOWN * 0.6,
            nl.n2p(-2) + DOWN * 0.6,
            color=COLOR_COMPARE, stroke_width=3, tip_length=0.15, buff=0
        )
        compare_text2 = MathTex(
            r"-2 > -4", font_size=36, color=COLOR_COMPARE
        ).move_to(DOWN * 1.5)
        explain_neg = Text(
            "-2 在 -4 的右边, 所以更大",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.5)

        self.play(
            GrowFromCenter(compare_arrow2), FadeOut(hint),
            run_time=0.5
        )
        self.play(Write(compare_text2), run_time=0.5)
        self.play(FadeIn(explain_neg, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 特别结论
        special = Text(
            "所有正数 > 0 > 所有负数",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 4.0)
        special_box = SurroundingRectangle(special, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(Write(special), Create(special_box), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl), FadeOut(rule), FadeOut(rule_box),
            FadeOut(dot_m2), FadeOut(dot_m4),
            FadeOut(lbl_m2), FadeOut(lbl_m4),
            FadeOut(compare_arrow2), FadeOut(compare_text2),
            FadeOut(explain_neg),
            FadeOut(special), FadeOut(special_box),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 练一练
    # ------------------------------------------------------------------
    def scene_8_practice(self):
        title = Text(
            "练一练", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        problems = [
            {
                "q_text": "在数轴上, -3 在 2 的哪边?",
                "a_text": "左边 (-3 < 2)",
                "hint": "左边的数更小",
            },
            {
                "q_text": "数轴的三要素是?",
                "a_text": "原点、正方向、单位长度",
                "hint": "缺一不可!",
            },
            {
                "q_text": "-5 和 -1 谁更大?",
                "a_text": "-1 > -5",
                "hint": "-1 在 -5 的右边",
            },
        ]

        y_pos = 3.5
        all_elements = VGroup()

        for i, p in enumerate(problems):
            # 题号
            num_label = Text(
                f"({i + 1})", font=FONT, font_size=24, color=COLOR_ACCENT
            ).move_to(UP * y_pos + LEFT * 3.5)

            # 题目
            q = Text(
                p["q_text"], font=FONT, font_size=24, color=WHITE
            ).next_to(num_label, RIGHT, buff=0.2)

            self.play(FadeIn(num_label), Write(q), run_time=0.6)
            self.wait(1.0)

            # 答案
            a = Text(
                p["a_text"], font=FONT, font_size=26, color=COLOR_RESULT
            ).move_to(UP * (y_pos - 0.7))
            self.play(FadeIn(a, shift=UP * 0.2), run_time=0.5)

            # 提示
            hint = Text(
                p["hint"], font=FONT, font_size=20, color=GRAY_A
            ).move_to(UP * (y_pos - 1.3))
            self.play(FadeIn(hint), run_time=0.3)
            self.wait(0.8)

            row = VGroup(num_label, q, a, hint)
            all_elements.add(row)
            y_pos -= 2.8

        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(all_elements), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 9: 总结
    # ------------------------------------------------------------------
    def scene_9_summary(self):
        title = Text(
            "总结", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴定义
        def_header = Text(
            "数轴 = 规定了原点、正方向、",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.3)
        def_header2 = Text(
            "单位长度的直线",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 3.6)
        def_box = SurroundingRectangle(
            VGroup(def_header, def_header2), color=COLOR_HL, buff=0.15, corner_radius=0.1
        )
        self.play(Write(def_header), run_time=0.6)
        self.play(Write(def_header2), Create(def_box), run_time=0.6)
        self.wait(0.3)

        # 三要素卡片
        cards_data = [
            ("1", "原点", "数轴的起始点, 标记为 0", COLOR_ORIGIN),
            ("2", "正方向", "通常向右, 用箭头表示", COLOR_POS_DIR),
            ("3", "单位长度", "相邻整数间距相等", COLOR_UNIT),
        ]

        y_start = 2.0
        card_mobs = VGroup()
        for i, (num, name, desc, col) in enumerate(cards_data):
            # 数字圆
            circle = Circle(radius=0.28, fill_color=col, fill_opacity=1, stroke_width=0)
            num_text = Text(num, font=FONT, font_size=22, color=BG_COLOR)
            num_group = VGroup(circle, num_text)
            num_text.move_to(circle.get_center())

            # 名称
            name_text = Text(name, font=FONT, font_size=26, color=col)

            # 描述
            desc_text = Text(desc, font=FONT, font_size=18, color=GRAY_A)

            row = VGroup(num_group, name_text, desc_text).arrange(RIGHT, buff=0.3)
            row.move_to(UP * (y_start - i * 1.2))
            card_mobs.add(row)

            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)

        self.wait(0.3)

        # 比较规则
        compare_rule = Text(
            "比较大小: 右边 > 左边",
            font=FONT, font_size=26, color=COLOR_COMPARE
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(compare_rule, shift=UP * 0.2), run_time=0.5)

        # 数形结合
        concept = Text(
            "数轴 = 数形结合的重要工具!",
            font=FONT, font_size=26, color=COLOR_ACCENT
        ).move_to(DOWN * 3.5)
        concept_box = SurroundingRectangle(concept, color=COLOR_ACCENT, buff=0.15, corner_radius=0.1)
        self.play(Write(concept), Create(concept_box), run_time=0.7)
        self.wait(0.5)

        # 关键词
        keywords = Text(
            "关键词: 原点 / 正方向 / 单位长度 / 数形结合",
            font=FONT, font_size=20, color=GRAY_B
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(keywords), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_header), FadeOut(def_header2), FadeOut(def_box),
            FadeOut(card_mobs),
            FadeOut(compare_rule),
            FadeOut(concept), FadeOut(concept_box),
            FadeOut(keywords),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 10: 片尾
    # ------------------------------------------------------------------
    def scene_10_outro(self):
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 数轴装饰
        deco_nl = NumberLine(
            x_range=[-4, 4, 1],
            length=6.0,
            include_numbers=True,
            font_size=18,
            color=COLOR_ACCENT,
            include_tip=True,
        ).move_to(DOWN * 3.0)

        self.play(Create(deco_nl), run_time=0.8)

        # 三个彩色点
        deco_dots = VGroup(
            Dot(deco_nl.n2p(-2), color=COLOR_NEG, radius=0.1),
            Dot(deco_nl.n2p(0), color=COLOR_ZERO, radius=0.1),
            Dot(deco_nl.n2p(3), color=COLOR_POS, radius=0.1),
        )
        self.play(*[FadeIn(d, scale=0.5) for d in deco_dots], run_time=0.5)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob), FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_nl), FadeOut(deco_dots),
            run_time=1.0
        )


# 运行命令:
# manim -pql 002_数轴.py NumberLineLesson   # 快速预览
# manim -qm 002_数轴.py NumberLineLesson    # 中等质量
# manim -qh 002_数轴.py NumberLineLesson    # 高质量

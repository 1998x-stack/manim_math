"""
003_绝对值.py — 绝对值 教学动画

知识点: 绝对值的定义、非负性、正数/负数/零的绝对值规则
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 数轴上的距离引入
  3. 绝对值的定义
  4. 正数的绝对值
  5. 负数的绝对值
  6. 零的绝对值
  7. 绝对值的非负性
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
COLOR_POS = "#22c55e"         # 绿色 正数
COLOR_NEG = "#ef4444"         # 红色 负数
COLOR_ZERO = "#fbbf24"        # 黄色 零
COLOR_DIST = "#3b82f6"        # 蓝色 距离
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_ACCENT = "#a78bfa"      # 紫色强调
COLOR_RESULT = "#22c55e"      # 绿色 结果
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
COLOR_FORMULA = "#f472b6"     # 粉色 公式
COLOR_TITLE = "#fbbf24"       # 金色 标题
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class AbsoluteValueLesson(Scene):
    """
    绝对值教学动画
    场景顺序:
      1. 开场钩子
      2. 数轴上的距离引入
      3. 绝对值的定义
      4. 正数的绝对值
      5. 负数的绝对值
      6. 零的绝对值
      7. 绝对值的非负性
      8. 练一练
      9. 总结
      10. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_number_line_intro()
        self.scene_3_definition()
        self.scene_4_positive()
        self.scene_5_negative()
        self.scene_6_zero()
        self.scene_7_non_negative()
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
            "5 和 -5",
            font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 4.5)

        hook2 = Text(
            "谁离原点更远?",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 3.5)

        self.play(Write(hook1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        # 小数轴预览
        nl = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 1.5)

        dot_pos = Dot(nl.n2p(5), color=COLOR_POS, radius=0.12)
        dot_neg = Dot(nl.n2p(-5), color=COLOR_NEG, radius=0.12)

        self.play(Create(nl), run_time=0.8)
        self.play(FadeIn(dot_pos, scale=0.5), FadeIn(dot_neg, scale=0.5), run_time=0.5)
        self.wait(0.5)

        # 两段距离
        brace_pos = BraceBetweenPoints(
            nl.n2p(0), nl.n2p(5), direction=UP, color=COLOR_POS
        )
        brace_neg = BraceBetweenPoints(
            nl.n2p(-5), nl.n2p(0), direction=UP, color=COLOR_NEG
        )
        lbl_pos = Text("5", font=FONT, font_size=22, color=COLOR_POS).next_to(brace_pos, UP, buff=0.1)
        lbl_neg = Text("5", font=FONT, font_size=22, color=COLOR_NEG).next_to(brace_neg, UP, buff=0.1)

        self.play(
            GrowFromCenter(brace_pos), GrowFromCenter(brace_neg),
            FadeIn(lbl_pos), FadeIn(lbl_neg),
            run_time=0.8
        )
        self.wait(0.3)

        answer = Text(
            "一样远! 都是 5",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        intro = Text(
            "这就是 —— 绝对值!",
            font=FONT, font_size=36, color=COLOR_ACCENT
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(intro, scale=1.1), run_time=0.7)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2), FadeOut(nl),
            FadeOut(dot_pos), FadeOut(dot_neg),
            FadeOut(brace_pos), FadeOut(brace_neg),
            FadeOut(lbl_pos), FadeOut(lbl_neg),
            FadeOut(answer), FadeOut(intro),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 数轴上的距离引入
    # ------------------------------------------------------------------
    def scene_2_number_line_intro(self):
        title = Text(
            "数轴上的距离", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            font_size=22,
            color=WHITE,
        ).move_to(UP * 3.0)

        origin_dot = Dot(nl.n2p(0), color=COLOR_ZERO, radius=0.15)
        origin_label = Text(
            "原点", font=FONT, font_size=20, color=COLOR_ZERO
        ).next_to(origin_dot, DOWN, buff=0.25)

        self.play(Create(nl), run_time=0.8)
        self.play(FadeIn(origin_dot, scale=0.5), FadeIn(origin_label), run_time=0.5)
        self.wait(0.3)

        # 展示 +3 的距离
        dot_3 = Dot(nl.n2p(3), color=COLOR_POS, radius=0.12)
        lbl_3 = MathTex("+3", color=COLOR_POS, font_size=28).next_to(dot_3, UP, buff=0.2)

        arrow_3 = DoubleArrow(
            nl.n2p(0) + DOWN * 0.6, nl.n2p(3) + DOWN * 0.6,
            color=COLOR_DIST, buff=0, stroke_width=3, tip_length=0.15
        )
        dist_3 = Text(
            "距离 = 3", font=FONT, font_size=22, color=COLOR_DIST
        ).next_to(arrow_3, DOWN, buff=0.15)

        self.play(FadeIn(dot_3, scale=0.5), Write(lbl_3), run_time=0.5)
        self.play(GrowFromCenter(arrow_3), FadeIn(dist_3), run_time=0.6)
        self.wait(0.8)

        # 展示 -4 的距离
        dot_m4 = Dot(nl.n2p(-4), color=COLOR_NEG, radius=0.12)
        lbl_m4 = MathTex("-4", color=COLOR_NEG, font_size=28).next_to(dot_m4, UP, buff=0.2)

        arrow_m4 = DoubleArrow(
            nl.n2p(-4) + DOWN * 1.6, nl.n2p(0) + DOWN * 1.6,
            color=COLOR_DIST, buff=0, stroke_width=3, tip_length=0.15
        )
        dist_m4 = Text(
            "距离 = 4", font=FONT, font_size=22, color=COLOR_DIST
        ).next_to(arrow_m4, DOWN, buff=0.15)

        self.play(FadeIn(dot_m4, scale=0.5), Write(lbl_m4), run_time=0.5)
        self.play(GrowFromCenter(arrow_m4), FadeIn(dist_m4), run_time=0.6)
        self.wait(0.8)

        # 要点
        key_text = Text(
            "距离只看远近, 不看方向!",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(key_text, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(origin_label), FadeOut(dot_3), FadeOut(lbl_3),
            FadeOut(arrow_3), FadeOut(dist_3),
            FadeOut(dot_m4), FadeOut(lbl_m4),
            FadeOut(arrow_m4), FadeOut(dist_m4),
            FadeOut(key_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 绝对值的定义
    # ------------------------------------------------------------------
    def scene_3_definition(self):
        title = Text(
            "绝对值的定义", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 定义文字 (分行)
        def_line1 = Text(
            "一个数在数轴上所对应的点",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        def_line2 = Text(
            "与原点的距离",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 3.3)
        def_line3 = Text(
            "叫做这个数的绝对值",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 2.6)

        self.play(Write(def_line1), run_time=0.7)
        self.play(Write(def_line2), run_time=0.6)
        self.play(Write(def_line3), run_time=0.6)
        self.wait(0.5)

        # 记号
        notation_text = Text(
            "记作", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 1.5 + LEFT * 1.5)
        notation_math = MathTex(
            r"|a|", font_size=56, color=COLOR_ACCENT
        ).next_to(notation_text, RIGHT, buff=0.3)

        self.play(FadeIn(notation_text), Write(notation_math), run_time=0.7)
        self.wait(0.3)

        # 读法
        read_text = Text(
            "读作: a 的绝对值",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 0.6)
        self.play(FadeIn(read_text), run_time=0.5)
        self.wait(0.5)

        # 数轴示意图
        nl = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            font_size=20,
            color=WHITE,
        ).move_to(DOWN * 1.5)

        origin_dot = Dot(nl.n2p(0), color=COLOR_ZERO, radius=0.14)

        self.play(Create(nl), FadeIn(origin_dot), run_time=0.6)

        # 动画: 点从原点出发向右移到 +a 位置
        a_val = 4
        moving_dot = Dot(nl.n2p(0), color=COLOR_ACCENT, radius=0.12)
        self.add(moving_dot)

        # 展示距离弧
        self.play(moving_dot.animate.move_to(nl.n2p(a_val)), run_time=1.0)

        dist_arrow = DoubleArrow(
            nl.n2p(0) + DOWN * 0.6, nl.n2p(a_val) + DOWN * 0.6,
            color=COLOR_DIST, buff=0, stroke_width=3, tip_length=0.15
        )
        dist_lbl = MathTex(
            r"|a|", font_size=30, color=COLOR_DIST
        ).next_to(dist_arrow, DOWN, buff=0.15)

        self.play(GrowFromCenter(dist_arrow), Write(dist_lbl), run_time=0.6)
        self.wait(1.0)

        # 强调: 距离
        box = SurroundingRectangle(def_line2, color=COLOR_HL, buff=0.12)
        self.play(Create(box), run_time=0.5)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_line1), FadeOut(def_line2),
            FadeOut(def_line3), FadeOut(notation_text), FadeOut(notation_math),
            FadeOut(read_text), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(moving_dot), FadeOut(dist_arrow), FadeOut(dist_lbl),
            FadeOut(box),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 正数的绝对值
    # ------------------------------------------------------------------
    def scene_4_positive(self):
        title = Text(
            "正数的绝对值", font=FONT, font_size=36, color=COLOR_POS
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        rule = Text(
            "正数的绝对值是它本身",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.5)
        self.play(Write(rule), run_time=0.7)
        self.wait(0.3)

        # 数轴
        nl = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            font_size=20,
            color=WHITE,
        ).move_to(UP * 2.5)
        origin_dot = Dot(nl.n2p(0), color=COLOR_ZERO, radius=0.12)
        self.play(Create(nl), FadeIn(origin_dot), run_time=0.5)

        # 示例 |5| = 5
        dot_5 = Dot(nl.n2p(5), color=COLOR_POS, radius=0.12)
        lbl_5 = MathTex(r"5", color=COLOR_POS, font_size=28).next_to(dot_5, UP, buff=0.2)
        self.play(FadeIn(dot_5, scale=0.5), Write(lbl_5), run_time=0.4)

        dist_brace = BraceBetweenPoints(
            nl.n2p(0), nl.n2p(5), direction=DOWN, color=COLOR_DIST
        )
        dist_text = Text(
            "距离 = 5", font=FONT, font_size=20, color=COLOR_DIST
        ).next_to(dist_brace, DOWN, buff=0.1)
        self.play(GrowFromCenter(dist_brace), FadeIn(dist_text), run_time=0.5)

        # 公式
        formula = MathTex(
            r"|5| = 5", font_size=48, color=COLOR_POS
        ).move_to(UP * 0.2)
        self.play(Write(formula), run_time=0.7)
        self.wait(0.5)

        # 更多例子
        ex1 = MathTex(r"|3| = 3", font_size=36, color=WHITE).move_to(DOWN * 1.2)
        ex2 = MathTex(r"|7.2| = 7.2", font_size=36, color=WHITE).move_to(DOWN * 2.2)
        ex3 = MathTex(
            r"\left|\frac{1}{2}\right| = \frac{1}{2}",
            font_size=36, color=WHITE
        ).move_to(DOWN * 3.4)

        self.play(Write(ex1), run_time=0.5)
        self.play(Write(ex2), run_time=0.5)
        self.play(Write(ex3), run_time=0.5)
        self.wait(0.5)

        # 通用规则
        general_rule_lbl = Text(
            "一般地, 当 a > 0 时:",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 4.8)
        general_formula = MathTex(
            r"|a| = a", font_size=44, color=COLOR_POS
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(general_rule_lbl), Write(general_formula), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(rule), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(dot_5), FadeOut(lbl_5), FadeOut(dist_brace), FadeOut(dist_text),
            FadeOut(formula), FadeOut(ex1), FadeOut(ex2), FadeOut(ex3),
            FadeOut(general_rule_lbl), FadeOut(general_formula),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 负数的绝对值
    # ------------------------------------------------------------------
    def scene_5_negative(self):
        title = Text(
            "负数的绝对值", font=FONT, font_size=36, color=COLOR_NEG
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        rule = Text(
            "负数的绝对值是它的相反数",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.5)
        self.play(Write(rule), run_time=0.7)
        self.wait(0.3)

        # 数轴
        nl = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            font_size=20,
            color=WHITE,
        ).move_to(UP * 2.5)
        origin_dot = Dot(nl.n2p(0), color=COLOR_ZERO, radius=0.12)
        self.play(Create(nl), FadeIn(origin_dot), run_time=0.5)

        # 示例 |-5| = 5
        dot_m5 = Dot(nl.n2p(-5), color=COLOR_NEG, radius=0.12)
        lbl_m5 = MathTex(r"-5", color=COLOR_NEG, font_size=28).next_to(dot_m5, UP, buff=0.2)
        self.play(FadeIn(dot_m5, scale=0.5), Write(lbl_m5), run_time=0.4)

        dist_brace = BraceBetweenPoints(
            nl.n2p(-5), nl.n2p(0), direction=DOWN, color=COLOR_DIST
        )
        dist_text = Text(
            "距离 = 5", font=FONT, font_size=20, color=COLOR_DIST
        ).next_to(dist_brace, DOWN, buff=0.1)
        self.play(GrowFromCenter(dist_brace), FadeIn(dist_text), run_time=0.5)

        # 公式 |-5| = 5
        formula = MathTex(
            r"|-5| = 5", font_size=48, color=COLOR_NEG
        ).move_to(UP * 0.2)
        self.play(Write(formula), run_time=0.7)
        self.wait(0.3)

        # 解释: 去掉负号
        explain = Text(
            "去掉负号 = 相反数",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 更多例子
        ex1 = MathTex(r"|-3| = 3", font_size=36, color=WHITE).move_to(DOWN * 2.0)
        ex2 = MathTex(r"|-7.2| = 7.2", font_size=36, color=WHITE).move_to(DOWN * 3.0)
        ex3 = MathTex(
            r"\left|-\frac{1}{2}\right| = \frac{1}{2}",
            font_size=36, color=WHITE
        ).move_to(DOWN * 4.2)

        self.play(Write(ex1), run_time=0.5)
        self.play(Write(ex2), run_time=0.5)
        self.play(Write(ex3), run_time=0.5)
        self.wait(0.5)

        # 通用规则
        general_rule_lbl = Text(
            "一般地, 当 a < 0 时:",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 5.5)
        general_formula = MathTex(
            r"|a| = -a", font_size=44, color=COLOR_NEG
        ).move_to(DOWN * 6.3)
        self.play(FadeIn(general_rule_lbl), Write(general_formula), run_time=0.7)
        self.wait(0.3)

        # 特别说明
        note = Text(
            "-a 不一定是负数哦!",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 7.2)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(rule), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(dot_m5), FadeOut(lbl_m5), FadeOut(dist_brace), FadeOut(dist_text),
            FadeOut(formula), FadeOut(explain),
            FadeOut(ex1), FadeOut(ex2), FadeOut(ex3),
            FadeOut(general_rule_lbl), FadeOut(general_formula), FadeOut(note),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 零的绝对值
    # ------------------------------------------------------------------
    def scene_6_zero(self):
        title = Text(
            "零的绝对值", font=FONT, font_size=36, color=COLOR_ZERO
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = NumberLine(
            x_range=[-6, 6, 1],
            length=7.5,
            include_numbers=True,
            font_size=20,
            color=WHITE,
        ).move_to(UP * 3.0)

        origin_dot = Dot(nl.n2p(0), color=COLOR_ZERO, radius=0.18)
        origin_label = Text(
            "0 就在原点上", font=FONT, font_size=22, color=COLOR_ZERO
        ).next_to(origin_dot, DOWN, buff=0.3)

        self.play(Create(nl), run_time=0.5)
        self.play(FadeIn(origin_dot, scale=0.5), FadeIn(origin_label), run_time=0.5)
        self.wait(0.3)

        # 距离为 0
        dist_text = Text(
            "与原点的距离 = 0",
            font=FONT, font_size=26, color=COLOR_DIST
        ).move_to(UP * 1.2)
        self.play(FadeIn(dist_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 公式
        formula = MathTex(
            r"|0| = 0", font_size=56, color=COLOR_ZERO
        ).move_to(DOWN * 0.3)
        self.play(Write(formula), run_time=0.7)

        # 闪烁
        self.play(Indicate(formula, color=COLOR_HL, scale_factor=1.1), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl), FadeOut(origin_dot),
            FadeOut(origin_label), FadeOut(dist_text), FadeOut(formula),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 绝对值的非负性
    # ------------------------------------------------------------------
    def scene_7_non_negative(self):
        title = Text(
            "绝对值的非负性", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 核心公式
        formula = MathTex(
            r"|a| \geq 0", font_size=56, color=COLOR_HL
        ).move_to(UP * 4.0)
        box = SurroundingRectangle(formula, color=COLOR_HL, buff=0.2, corner_radius=0.1)
        self.play(Write(formula), Create(box), run_time=0.8)
        self.wait(0.3)

        # 解释
        explain = Text(
            "任何数的绝对值都不是负数!",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 2.8)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)

        # 原因
        reason = Text(
            "因为 \"距离\" 不可能为负",
            font=FONT, font_size=24, color=COLOR_DIST
        ).move_to(UP * 2.0)
        self.play(FadeIn(reason, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 展示例子
        examples_data = [
            (r"|5| = 5", r"\geq 0 \checkmark", COLOR_POS),
            (r"|-5| = 5", r"\geq 0 \checkmark", COLOR_NEG),
            (r"|0| = 0", r"\geq 0 \checkmark", COLOR_ZERO),
            (r"|-100| = 100", r"\geq 0 \checkmark", COLOR_NEG),
        ]

        y_start = 0.5
        all_ex = VGroup()
        for i, (expr, check, col) in enumerate(examples_data):
            ex_formula = MathTex(expr, font_size=34, color=col)
            ex_check = MathTex(check, font_size=28, color=COLOR_RESULT)
            row = VGroup(ex_formula, ex_check).arrange(RIGHT, buff=0.4)
            row.move_to(DOWN * (i * 1.1 - y_start))
            all_ex.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        self.wait(0.8)

        # 特殊情况
        special = Text(
            "什么时候 |a| = 0 ?",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        special_ans = Text(
            "当且仅当 a = 0",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(special, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(special_ans, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(formula), FadeOut(box),
            FadeOut(explain), FadeOut(reason), FadeOut(all_ex),
            FadeOut(special), FadeOut(special_ans),
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
            (r"|8| = \;?", r"|8| = 8", "8 > 0, 绝对值是本身"),
            (r"|-3| = \;?", r"|-3| = 3", "-3 < 0, 绝对值是相反数"),
            (r"\left|-\frac{2}{3}\right| = \;?",
             r"\left|-\frac{2}{3}\right| = \frac{2}{3}",
             "负数取相反数"),
            (r"|0| = \;?", r"|0| = 0", "0 的绝对值是 0"),
        ]

        y_pos = 3.5
        all_elements = VGroup()

        for i, (q, a, hint) in enumerate(problems):
            # 题目
            q_tex = MathTex(q, font_size=38, color=WHITE).move_to(UP * y_pos + LEFT * 0.5)
            self.play(Write(q_tex), run_time=0.5)
            self.wait(0.8)

            # 提示
            hint_text = Text(
                hint, font=FONT, font_size=20, color=GRAY_A
            ).move_to(UP * (y_pos - 0.7))
            self.play(FadeIn(hint_text, shift=UP * 0.1), run_time=0.4)

            # 答案
            a_tex = MathTex(a, font_size=38, color=COLOR_RESULT).move_to(UP * y_pos + LEFT * 0.5)
            self.play(Transform(q_tex, a_tex), run_time=0.6)
            self.wait(0.5)

            row = VGroup(q_tex, hint_text)
            all_elements.add(row)
            y_pos -= 2.2

        self.wait(1.0)

        # 清理
        self.play(FadeOut(title), FadeOut(all_elements), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 9: 总结
    # ------------------------------------------------------------------
    def scene_9_summary(self):
        title = Text(
            "总结", font=FONT, font_size=36, color=COLOR_TITLE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 定义框
        def_header = Text(
            "绝对值 = 到原点的距离",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 4.2)
        def_box = SurroundingRectangle(def_header, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(Write(def_header), Create(def_box), run_time=0.7)
        self.wait(0.3)

        # 三条规则
        rules_y = 2.5
        rules = [
            (r"a > 0 \Rightarrow |a| = a", COLOR_POS, "正数: 就是本身"),
            (r"a < 0 \Rightarrow |a| = -a", COLOR_NEG, "负数: 取相反数"),
            (r"a = 0 \Rightarrow |a| = 0", COLOR_ZERO, "零: 就是零"),
        ]

        rule_mobs = VGroup()
        for i, (formula_str, col, desc) in enumerate(rules):
            f = MathTex(formula_str, font_size=34, color=col).move_to(
                UP * (rules_y - i * 1.5) + LEFT * 0.5
            )
            d = Text(
                desc, font=FONT, font_size=22, color=GRAY_A
            ).next_to(f, DOWN, buff=0.2)
            group = VGroup(f, d)
            rule_mobs.add(group)
            self.play(Write(f), run_time=0.5)
            self.play(FadeIn(d), run_time=0.3)
            self.wait(0.3)

        # 非负性
        non_neg = MathTex(
            r"|a| \geq 0", font_size=48, color=COLOR_ACCENT
        ).move_to(DOWN * 2.5)
        non_neg_text = Text(
            "绝对值永远非负!",
            font=FONT, font_size=26, color=COLOR_ACCENT
        ).move_to(DOWN * 3.5)
        non_neg_box = SurroundingRectangle(
            VGroup(non_neg, non_neg_text), color=COLOR_ACCENT, buff=0.2, corner_radius=0.1
        )

        self.play(Write(non_neg), run_time=0.5)
        self.play(FadeIn(non_neg_text), Create(non_neg_box), run_time=0.5)
        self.wait(0.5)

        # 关键词
        keywords = Text(
            "关键词: 距离 / 非负 / 相反数",
            font=FONT, font_size=22, color=GRAY_B
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(keywords), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_header), FadeOut(def_box),
            FadeOut(rule_mobs), FadeOut(non_neg), FadeOut(non_neg_text),
            FadeOut(non_neg_box), FadeOut(keywords),
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

        # 绝对值符号装饰
        deco_left = MathTex(r"|", font_size=120, color=COLOR_ACCENT).move_to(LEFT * 3 + DOWN * 3)
        deco_right = MathTex(r"|", font_size=120, color=COLOR_ACCENT).move_to(RIGHT * 3 + DOWN * 3)
        deco_heart = MathTex(r"\heartsuit", font_size=60, color=COLOR_NEG).move_to(DOWN * 3)

        self.play(
            FadeIn(deco_left, shift=RIGHT * 0.3),
            FadeIn(deco_right, shift=LEFT * 0.3),
            FadeIn(deco_heart, scale=0.5),
            run_time=0.6
        )
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob), FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_left), FadeOut(deco_right), FadeOut(deco_heart),
            run_time=1.0
        )


# 运行命令:
# manim -pql 003_绝对值.py AbsoluteValueLesson   # 快速预览
# manim -qm 003_绝对值.py AbsoluteValueLesson    # 中等质量
# manim -qh 003_绝对值.py AbsoluteValueLesson    # 高质量

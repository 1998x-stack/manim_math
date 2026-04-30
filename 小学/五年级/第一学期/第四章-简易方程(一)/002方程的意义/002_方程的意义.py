"""
002_方程的意义.py — 方程的意义 教学动画

知识点: 含有未知数的等式叫做方程
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 等式: 左右两边相等的式子
  2. 方程: 含有未知数的等式
  3. 方程一定是等式，但等式不一定是方程
  4. 判断练习: 区分方程和非方程
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
COLOR_EQ = "#3b82f6"         # 蓝色等式
COLOR_VAR = "#f59e0b"        # 橙色未知数
COLOR_YES = "#22c55e"        # 绿色正确
COLOR_NO = "#ef4444"         # 红色错误/否
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_VENN_EQ = "#6366f1"    # 靛蓝色等式圈
COLOR_VENN_FG = "#f97316"    # 橙色方程圈
COLOR_KEY = "#a78bfa"        # 紫色要点
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "PingFang SC"


class EquationMeaningLesson(Scene):
    """
    方程的意义教学动画
    场景:
      1. 开场钩子
      2. 概念引入: 等式 → 方程
      3. 举例辨析: 哪些是方程
      4. 集合关系 (Venn 图概念)
      5. 要点总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_concept()
        self.scene_3_examples()
        self.scene_4_venn()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "什么是方程？", font=FONT, font_size=48,
            color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "它和等式有什么关系？", font=FONT, font_size=34,
            color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)

        # 天平概念: 一个简单的天平图示
        fulcrum = Triangle(
            fill_color=GRAY_B, fill_opacity=0.8,
            stroke_color=WHITE, stroke_width=2
        ).scale(0.4).move_to(DOWN * 0.5)
        beam = Line(LEFT * 2.5, RIGHT * 2.5, color=WHITE, stroke_width=4)
        beam.move_to(UP * 0.2)

        left_box = Square(
            side_length=0.8, fill_color=COLOR_EQ,
            fill_opacity=0.7, stroke_color=COLOR_EQ
        ).move_to(beam.get_left() + UP * 0.5)
        right_box = Square(
            side_length=0.8, fill_color=COLOR_EQ,
            fill_opacity=0.7, stroke_color=COLOR_EQ
        ).move_to(beam.get_right() + UP * 0.5)

        left_label = MathTex("3+5", font_size=28, color=WHITE).move_to(left_box)
        right_label = MathTex("8", font_size=28, color=WHITE).move_to(right_box)

        balance = VGroup(fulcrum, beam, left_box, right_box, left_label, right_label)
        self.play(FadeIn(balance, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)

        eq_text = Text(
            "两边相等 → 等式", font=FONT, font_size=26, color=COLOR_EQ
        ).move_to(DOWN * 2.0)
        self.play(Write(eq_text), run_time=0.6)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, balance, eq_text)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 概念引入 — 等式与方程
    # ------------------------------------------------------------------

    def scene_2_concept(self):
        title = Text(
            "什么是等式？", font=FONT, font_size=36,
            color=COLOR_EQ, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 等式定义
        def1 = Text(
            "左右两边相等的式子", font=FONT, font_size=28,
            color=WHITE
        ).move_to(UP * 4.0)
        def1b = Text(
            "叫做等式", font=FONT, font_size=28,
            color=COLOR_EQ, weight=BOLD
        ).move_to(UP * 3.3)
        self.play(Write(def1), run_time=0.6)
        self.play(Write(def1b), run_time=0.5)
        self.wait(0.5)

        # 等式举例
        ex1 = MathTex(r"3 + 5 = 8", font_size=40, color=WHITE)
        ex2 = MathTex(r"10 - 4 = 6", font_size=40, color=WHITE)
        ex_eq = VGroup(ex1, ex2).arrange(DOWN, buff=0.5).move_to(UP * 1.5)
        self.play(Write(ex1), run_time=0.5)
        self.play(Write(ex2), run_time=0.5)
        self.wait(0.5)

        check1 = Text(
            "  等式", font=FONT, font_size=22, color=COLOR_YES
        ).next_to(ex1, RIGHT, buff=0.3)
        check2 = Text(
            "  等式", font=FONT, font_size=22, color=COLOR_YES
        ).next_to(ex2, RIGHT, buff=0.3)
        self.play(FadeIn(check1), FadeIn(check2), run_time=0.4)
        self.wait(0.5)

        # 过渡到方程
        trans = Text(
            "如果等式中含有未知数呢？", font=FONT, font_size=28,
            color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(Write(trans), run_time=0.6)
        self.wait(0.5)

        # 方程举例
        eq_ex = MathTex(r"x + 5 = 8", font_size=44, color=COLOR_VAR)
        eq_ex.move_to(DOWN * 2.0)
        self.play(Write(eq_ex), run_time=0.7)

        # 高亮 x
        x_part = eq_ex[0][0]  # the 'x'
        hl_box = SurroundingRectangle(
            x_part, color=COLOR_VAR, stroke_width=2.5,
            buff=0.1, corner_radius=0.08
        )
        hl_label = Text(
            "未知数", font=FONT, font_size=20, color=COLOR_VAR
        ).next_to(hl_box, UP, buff=0.15)
        self.play(Create(hl_box), FadeIn(hl_label), run_time=0.5)
        self.wait(0.3)

        # 方程定义
        def2 = Text(
            "含有未知数的等式", font=FONT, font_size=30,
            color=WHITE
        ).move_to(DOWN * 3.8)
        def2b = Text(
            "叫做方程", font=FONT, font_size=30,
            color=COLOR_VAR, weight=BOLD
        ).move_to(DOWN * 4.5)
        self.play(Write(def2), run_time=0.6)
        self.play(Write(def2b), run_time=0.5)
        self.play(
            Indicate(def2b, scale_factor=1.08, color=COLOR_VAR),
            run_time=0.5
        )
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, def1, def1b, ex1, ex2, check1, check2,
                trans, eq_ex, hl_box, hl_label, def2, def2b
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 举例辨析 — 哪些是方程
    # ------------------------------------------------------------------

    def scene_3_examples(self):
        title = Text(
            "判断：哪些是方程？", font=FONT, font_size=36,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 提示条件
        cond1 = Text("条件一：必须是等式", font=FONT, font_size=22, color=COLOR_EQ)
        cond2 = Text("条件二：含有未知数", font=FONT, font_size=22, color=COLOR_VAR)
        conds = VGroup(cond1, cond2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        conds.move_to(UP * 4.0)
        self.play(FadeIn(conds, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.3)

        # 6 个判断题
        examples = [
            (r"x + 3 = 10",    True,  "含未知数的等式"),
            (r"5 + 7 = 12",    False, "没有未知数"),
            (r"2x - 1 = 9",    True,  "含未知数的等式"),
            (r"3x + 2 > 8",    False, "不是等式(不等式)"),
            (r"y = 4",         True,  "含未知数的等式"),
            (r"6 \times 3",    False, "不是等式(无等号)"),
        ]

        start_y = 2.2
        items_group = VGroup()

        for i, (expr, is_eq, reason) in enumerate(examples):
            y_pos = start_y - i * 1.1

            # Number
            num = Text(
                f"{i+1}.", font=FONT, font_size=22, color=GRAY_A
            ).move_to(LEFT * 3.8 + UP * y_pos)

            # Math expression
            math_expr = MathTex(expr, font_size=34, color=WHITE)
            math_expr.move_to(LEFT * 1.5 + UP * y_pos)

            row = VGroup(num, math_expr)
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.35)
            self.wait(0.2)

            # Result
            if is_eq:
                result_icon = MathTex(r"\checkmark", font_size=36, color=COLOR_YES)
                result_text = Text(
                    "是方程", font=FONT, font_size=20, color=COLOR_YES
                )
            else:
                result_icon = MathTex(r"\times", font_size=36, color=COLOR_NO)
                result_text = Text(
                    "不是方程", font=FONT, font_size=20, color=COLOR_NO
                )

            result_icon.move_to(RIGHT * 1.2 + UP * y_pos)
            result_text.move_to(RIGHT * 2.8 + UP * y_pos)

            self.play(FadeIn(result_icon, scale=0.5), run_time=0.3)
            self.play(FadeIn(result_text), run_time=0.3)

            # Reason tooltip (small)
            reason_text = Text(
                reason, font=FONT, font_size=16, color=GRAY_B
            ).move_to(RIGHT * 1.5 + UP * (y_pos - 0.35))
            self.play(FadeIn(reason_text, shift=UP * 0.1), run_time=0.25)

            items_group.add(row, result_icon, result_text, reason_text)

        self.wait(1.5)

        self.play(FadeOut(VGroup(title, conds, items_group)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 4: 集合关系 — Venn 图概念
    # ------------------------------------------------------------------

    def scene_4_venn(self):
        title = Text(
            "等式与方程的关系", font=FONT, font_size=36,
            color=COLOR_KEY, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 大圈: 等式
        eq_circle = Ellipse(
            width=7.0, height=5.0,
            color=COLOR_VENN_EQ, fill_color=COLOR_VENN_EQ,
            fill_opacity=0.15, stroke_width=3
        ).move_to(UP * 0.5)

        eq_label = Text(
            "等式", font=FONT, font_size=32,
            color=COLOR_VENN_EQ, weight=BOLD
        ).move_to(UP * 3.3 + LEFT * 1.5)

        self.play(Create(eq_circle), run_time=0.8)
        self.play(Write(eq_label), run_time=0.4)

        # 小圈: 方程 (在大圈内部)
        fang_circle = Ellipse(
            width=4.2, height=3.0,
            color=COLOR_VENN_FG, fill_color=COLOR_VENN_FG,
            fill_opacity=0.2, stroke_width=3
        ).move_to(DOWN * 0.2 + RIGHT * 0.3)

        fang_label = Text(
            "方程", font=FONT, font_size=28,
            color=COLOR_VENN_FG, weight=BOLD
        ).move_to(DOWN * 0.2 + RIGHT * 0.3)

        self.play(Create(fang_circle), run_time=0.8)
        self.play(Write(fang_label), run_time=0.4)
        self.wait(0.5)

        # 在等式圈内方程圈外放不含未知数的等式
        non_eq_examples = VGroup(
            MathTex(r"3+5=8", font_size=24, color=GRAY_A),
            MathTex(r"10-4=6", font_size=24, color=GRAY_A),
            MathTex(r"2\times3=6", font_size=24, color=GRAY_A),
        ).arrange(DOWN, buff=0.3).move_to(UP * 1.2 + LEFT * 2.2)

        # 在方程圈内放含未知数的等式
        eq_examples = VGroup(
            MathTex(r"x+3=10", font_size=24, color=COLOR_VENN_FG),
            MathTex(r"2x=8", font_size=24, color=COLOR_VENN_FG),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.8 + RIGHT * 0.3)

        self.play(
            *[FadeIn(e, shift=RIGHT * 0.2) for e in non_eq_examples],
            run_time=0.6
        )
        self.play(
            *[FadeIn(e, shift=LEFT * 0.2) for e in eq_examples],
            run_time=0.6
        )
        self.wait(0.5)

        # 关键结论
        conclusion1 = Text(
            "方程一定是等式", font=FONT, font_size=26,
            color=COLOR_YES, weight=BOLD
        ).move_to(DOWN * 3.5)
        conclusion2 = Text(
            "等式不一定是方程", font=FONT, font_size=26,
            color=COLOR_NO, weight=BOLD
        ).move_to(DOWN * 4.3)

        self.play(FadeIn(conclusion1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(conclusion2, shift=UP * 0.2), run_time=0.5)
        self.play(
            Indicate(conclusion2, scale_factor=1.05, color=COLOR_NO),
            run_time=0.5
        )
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, eq_circle, eq_label,
                fang_circle, fang_label,
                non_eq_examples, eq_examples,
                conclusion1, conclusion2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 要点总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.3)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "方程的意义", font=FONT, font_size=32,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.2)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 等式：表示相等关系的式子",
                 font=FONT, font_size=22, color=WHITE),
            Text("2. 方程：含有未知数的等式",
                 font=FONT, font_size=22, color=COLOR_VAR),
            Text("3. 方程必须同时满足两个条件：",
                 font=FONT, font_size=22, color=WHITE),
            Text("   (1) 必须是等式（有等号）",
                 font=FONT, font_size=20, color=COLOR_EQ),
            Text("   (2) 含有未知数",
                 font=FONT, font_size=20, color=COLOR_VAR),
            Text("4. 方程一定是等式",
                 font=FONT, font_size=22, color=COLOR_YES),
            Text("5. 等式不一定是方程",
                 font=FONT, font_size=22, color=COLOR_NO),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(UP * 0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 核心公式高亮
        core = Text(
            "含有未知数的等式叫做方程",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.8)
        core_box = SurroundingRectangle(
            core, color=COLOR_VAR, stroke_width=2.5,
            buff=0.15, corner_radius=0.1
        )
        self.play(Write(core), run_time=0.6)
        self.play(Create(core_box), run_time=0.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, core, core_box)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 002_方程的意义.py EquationMeaningLesson
#   高质量:    manim -qh  002_方程的意义.py EquationMeaningLesson
#   4K:        manim -qk  002_方程的意义.py EquationMeaningLesson
# ======================================================================

"""
003_小数除以小数.py — 小数除以小数 教学动画

知识点: 利用商不变的性质，将除数转化为整数进行计算
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 商不变的性质: 被除数和除数同时乘以相同的数，商不变
  2. 小数除以小数的步骤: 移动小数点转化为整数除法
  3. 例题: 6.4 ÷ 0.4 = 64 ÷ 4 = 16
  4. 进阶例题: 7.98 ÷ 0.42 = 798 ÷ 42 = 19
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
COLOR_DIVIDEND = "#3b82f6"    # 蓝色被除数
COLOR_DIVISOR = "#ef4444"     # 红色除数
COLOR_RESULT = "#22c55e"      # 绿色结果
COLOR_ARROW = "#f59e0b"       # 橙色箭头
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_RULE = "#a78bfa"        # 紫色规律
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class DecimalDivisionLesson(Scene):
    """
    小数除以小数教学动画
    场景:
      1. 开场钩子
      2. 商不变的性质
      3. 转化步骤演示 (6.4 ÷ 0.4)
      4. 进阶例题 (7.98 ÷ 0.42)
      5. 步骤总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_invariant_property()
        self.scene_3_example_1()
        self.scene_4_example_2()
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
            "小数除以小数", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "怎么算？", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示问题
        problem = MathTex(r"6.4 \div 0.4 = \;?", font_size=48, color=COLOR_DIVIDEND)
        problem.move_to(UP * 1.0)
        self.play(FadeIn(problem, scale=0.6), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, problem)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 商不变的性质
    # ------------------------------------------------------------------

    def scene_2_invariant_property(self):
        title = Text(
            "商不变的性质", font=FONT, font_size=38,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 先看一个整数例子
        desc = Text(
            "先看一组整数除法", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.0)
        self.play(Write(desc), run_time=0.4)

        # 三个等式
        eq1 = MathTex(r"8 \div 2 = 4", font_size=36, color=WHITE)
        eq2 = MathTex(r"80 \div 20 = 4", font_size=36, color=WHITE)
        eq3 = MathTex(r"800 \div 200 = 4", font_size=36, color=WHITE)
        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.6).move_to(UP * 1.5)

        self.play(Write(eq1), run_time=0.6)
        self.wait(0.3)
        self.play(Write(eq2), run_time=0.6)
        self.wait(0.3)
        self.play(Write(eq3), run_time=0.6)
        self.wait(0.5)

        # 箭头标注: ×10
        arrow1 = Arrow(
            eq1.get_right() + RIGHT * 0.3, eq2.get_right() + RIGHT * 0.3,
            color=COLOR_ARROW, stroke_width=2.5, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        times10_1 = MathTex(r"\times 10", font_size=22, color=COLOR_ARROW)
        times10_1.next_to(arrow1, RIGHT, buff=0.1)

        arrow2 = Arrow(
            eq2.get_right() + RIGHT * 0.3, eq3.get_right() + RIGHT * 0.3,
            color=COLOR_ARROW, stroke_width=2.5, buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        times10_2 = MathTex(r"\times 10", font_size=22, color=COLOR_ARROW)
        times10_2.next_to(arrow2, RIGHT, buff=0.1)

        self.play(
            Create(arrow1), FadeIn(times10_1),
            Create(arrow2), FadeIn(times10_2),
            run_time=0.6
        )

        # 商都等于4 高亮
        result_hl = Text(
            "商都是 4，没有变！", font=FONT, font_size=26,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(result_hl, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        # 规律
        rule_box = RoundedRectangle(
            width=7.5, height=1.8,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_RULE, stroke_width=3
        ).move_to(DOWN * 3.5)

        rule_text = Text(
            "被除数和除数同时乘以相同的数",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 3.1)
        rule_text2 = Text(
            "商不变！", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.9)

        self.play(FadeIn(rule_box), run_time=0.3)
        self.play(Write(rule_text), run_time=0.6)
        self.play(Write(rule_text2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, desc, eqs, arrow1, arrow2,
                          times10_1, times10_2, result_hl,
                          rule_box, rule_text, rule_text2)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 例题1 — 6.4 ÷ 0.4
    # ------------------------------------------------------------------

    def scene_3_example_1(self):
        title = Text(
            "例题一", font=FONT, font_size=36,
            color=COLOR_DIVIDEND, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 原式
        orig = MathTex(r"6.4 \div 0.4", font_size=44, color=WHITE)
        orig.move_to(UP * 3.5)
        self.play(Write(orig), run_time=0.7)
        self.wait(0.3)

        # 步骤1: 看除数有几位小数
        step1 = Text(
            "除数 0.4 有1位小数", font=FONT, font_size=24, color=COLOR_DIVISOR
        ).move_to(UP * 2.3)
        self.play(Write(step1), run_time=0.5)
        self.wait(0.3)

        # 步骤2: 同时乘以10
        step2 = Text(
            "被除数和除数同时乘以10", font=FONT, font_size=24, color=COLOR_ARROW
        ).move_to(UP * 1.3)
        self.play(Write(step2), run_time=0.5)

        # 转化过程
        transform_left = MathTex(r"6.4", font_size=42, color=COLOR_DIVIDEND)
        times_left = MathTex(r"\times 10", font_size=30, color=COLOR_ARROW)
        eq_left = MathTex(r"= 64", font_size=42, color=COLOR_DIVIDEND)
        left_group = VGroup(transform_left, times_left, eq_left).arrange(RIGHT, buff=0.1)
        left_group.move_to(UP * 0.2 + LEFT * 0.5)

        transform_right = MathTex(r"0.4", font_size=42, color=COLOR_DIVISOR)
        times_right = MathTex(r"\times 10", font_size=30, color=COLOR_ARROW)
        eq_right = MathTex(r"= 4", font_size=42, color=COLOR_DIVISOR)
        right_group = VGroup(transform_right, times_right, eq_right).arrange(RIGHT, buff=0.1)
        right_group.move_to(DOWN * 0.8 + LEFT * 0.5)

        self.play(FadeIn(left_group, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(right_group, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)

        # 步骤3: 变成整数除法
        step3 = Text(
            "变成整数除法！", font=FONT, font_size=26,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.5)

        new_eq = MathTex(r"64 \div 4 = 16", font_size=44, color=COLOR_RESULT)
        new_eq.move_to(DOWN * 3.2)
        self.play(Write(new_eq), run_time=0.8)

        # 最终结果
        final = VGroup(
            MathTex(r"6.4 \div 0.4 = ", font_size=40, color=WHITE),
            MathTex(r"16", font_size=48, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.8)
        self.play(FadeIn(final, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(final[1], scale_factor=1.2, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, orig, step1, step2,
                          left_group, right_group, step3, new_eq, final)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 例题2 — 7.98 ÷ 0.42
    # ------------------------------------------------------------------

    def scene_4_example_2(self):
        title = Text(
            "例题二", font=FONT, font_size=36,
            color=COLOR_RESULT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 原式
        orig = MathTex(r"7.98 \div 0.42", font_size=44, color=WHITE)
        orig.move_to(UP * 3.5)
        self.play(Write(orig), run_time=0.7)
        self.wait(0.3)

        # 步骤1
        step1 = Text(
            "除数 0.42 有2位小数", font=FONT, font_size=24, color=COLOR_DIVISOR
        ).move_to(UP * 2.3)
        self.play(Write(step1), run_time=0.5)

        # 步骤2
        step2 = Text(
            "同时乘以100", font=FONT, font_size=24, color=COLOR_ARROW
        ).move_to(UP * 1.3)
        self.play(Write(step2), run_time=0.5)

        # 转化
        transform_left = MathTex(r"7.98", font_size=42, color=COLOR_DIVIDEND)
        times_left = MathTex(r"\times 100", font_size=30, color=COLOR_ARROW)
        eq_left = MathTex(r"= 798", font_size=42, color=COLOR_DIVIDEND)
        left_group = VGroup(transform_left, times_left, eq_left).arrange(RIGHT, buff=0.1)
        left_group.move_to(UP * 0.2 + LEFT * 0.3)

        transform_right = MathTex(r"0.42", font_size=42, color=COLOR_DIVISOR)
        times_right = MathTex(r"\times 100", font_size=30, color=COLOR_ARROW)
        eq_right = MathTex(r"= 42", font_size=42, color=COLOR_DIVISOR)
        right_group = VGroup(transform_right, times_right, eq_right).arrange(RIGHT, buff=0.1)
        right_group.move_to(DOWN * 0.8 + LEFT * 0.3)

        self.play(FadeIn(left_group, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(right_group, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)

        # 计算
        step3 = Text(
            "变成整数除法", font=FONT, font_size=26,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.5)

        new_eq = MathTex(r"798 \div 42 = 19", font_size=44, color=COLOR_RESULT)
        new_eq.move_to(DOWN * 3.2)
        self.play(Write(new_eq), run_time=0.8)

        # 最终结果
        final = VGroup(
            MathTex(r"7.98 \div 0.42 = ", font_size=40, color=WHITE),
            MathTex(r"19", font_size=48, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.8)
        self.play(FadeIn(final, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(final[1], scale_factor=1.2, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, orig, step1, step2,
                          left_group, right_group, step3, new_eq, final)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 步骤总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=6.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "小数除以小数的步骤", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.3)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 看除数有几位小数", font=FONT, font_size=22, color=WHITE),
            Text("2. 除数和被除数的小数点", font=FONT, font_size=22, color=WHITE),
            Text("   同时向右移动相同位数", font=FONT, font_size=22, color=WHITE),
            Text("3. 把除数变成整数", font=FONT, font_size=22, color=COLOR_DIVISOR),
            Text("4. 按整数除法计算", font=FONT, font_size=22, color=COLOR_RESULT),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 0.8)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 关键提醒
        key = Text(
            "核心：商不变的性质！",
            font=FONT, font_size=24, color=COLOR_RULE, weight=BOLD
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)

        tip = Text(
            "位数不够时，在被除数末尾补0",
            font=FONT, font_size=20, color=COLOR_ARROW
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, key, tip)), run_time=0.5)

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
#   快速预览:  manim -pql 003_小数除以小数.py DecimalDivisionLesson
#   高质量:    manim -qh  003_小数除以小数.py DecimalDivisionLesson
#   4K:        manim -qk  003_小数除以小数.py DecimalDivisionLesson
# ======================================================================

"""
004_解简易方程.py — 解简易方程 教学动画

知识点: 利用等式的性质解方程
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 解方程的核心思想: 通过恒等变形得到 x=?
  2. 例1: x + 8 = 15 → x = 7
  3. 例2: 3x = 24 → x = 8
  4. 规范格式: 等号对齐，写出每步依据
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
COLOR_EQ = "#3b82f6"
COLOR_X = "#f59e0b"
COLOR_SOLVE = "#22c55e"
COLOR_HL = "#fbbf24"
COLOR_STEP = "#a78bfa"
COLOR_CHECK = "#ef4444"
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class SolveEquationLesson(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_core_idea()
        self.scene_3_example_1()
        self.scene_4_example_2()
        self.scene_5_summary()
        self.scene_6_outro()

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text("解简易方程", font=FONT, font_size=52, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        hook2 = Text("怎么找到 x？", font=FONT, font_size=40, color=COLOR_HL).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    def scene_2_core_idea(self):
        title = Text("核心思想", font=FONT, font_size=38, color=COLOR_STEP, weight=BOLD).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        idea = Text("通过恒等变形", font=FONT, font_size=28, color=WHITE).move_to(UP * 3.5)
        self.play(Write(idea), run_time=0.5)

        goal = VGroup(
            Text("把方程变成 ", font=FONT, font_size=28, color=WHITE),
            MathTex(r"x = ?", font_size=48, color=COLOR_HL),
            Text(" 的形式", font=FONT, font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 2.0)
        self.play(FadeIn(goal, shift=UP * 0.2), run_time=0.6)

        basis = Text("依据：等式的性质", font=FONT, font_size=26, color=COLOR_STEP).move_to(UP * 0.5)
        self.play(Write(basis), run_time=0.5)

        p1 = Text("两边同时加减同一个数", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 0.5)
        p2 = Text("两边同时乘除同一个不为0的数", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 1.3)
        self.play(FadeIn(p1, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(p2, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, idea, goal, basis, p1, p2)), run_time=0.4)

    def scene_3_example_1(self):
        title = Text("例题一", font=FONT, font_size=36, color=COLOR_EQ, weight=BOLD).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        eq0 = MathTex(r"x + 8 = 15", font_size=44, color=WHITE).move_to(UP * 3.5)
        self.play(Write(eq0), run_time=0.7)

        solve = Text("解：", font=FONT, font_size=26, color=COLOR_SOLVE).move_to(UP * 2.3 + LEFT * 3.0)
        self.play(Write(solve), run_time=0.3)

        step1_hint = Text("两边同时减去8", font=FONT, font_size=22, color=COLOR_STEP).move_to(UP * 2.3 + RIGHT * 1.5)
        self.play(Write(step1_hint), run_time=0.5)

        eq1 = MathTex(r"x + 8 - 8 = 15 - 8", font_size=36, color=WHITE).move_to(UP * 1.3)
        self.play(Write(eq1), run_time=0.6)

        eq2 = MathTex(r"x = 7", font_size=48, color=COLOR_HL).move_to(UP * 0.2)
        self.play(Write(eq2), run_time=0.6)
        self.play(Indicate(eq2, scale_factor=1.1, color=COLOR_HL), run_time=0.5)

        check_title = Text("检验：", font=FONT, font_size=22, color=COLOR_CHECK).move_to(DOWN * 1.2 + LEFT * 2.5)
        check = MathTex(r"7 + 8 = 15\;\checkmark", font_size=30, color=COLOR_CHECK).move_to(DOWN * 1.2 + RIGHT * 0.5)
        self.play(Write(check_title), Write(check), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, eq0, solve, step1_hint, eq1, eq2, check_title, check)), run_time=0.4)

    def scene_4_example_2(self):
        title = Text("例题二", font=FONT, font_size=36, color=COLOR_SOLVE, weight=BOLD).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        eq0 = MathTex(r"3x = 24", font_size=44, color=WHITE).move_to(UP * 3.5)
        self.play(Write(eq0), run_time=0.7)

        solve = Text("解：", font=FONT, font_size=26, color=COLOR_SOLVE).move_to(UP * 2.3 + LEFT * 3.0)
        self.play(Write(solve), run_time=0.3)

        step1_hint = Text("两边同时除以3", font=FONT, font_size=22, color=COLOR_STEP).move_to(UP * 2.3 + RIGHT * 1.5)
        self.play(Write(step1_hint), run_time=0.5)

        eq1 = MathTex(r"3x \div 3 = 24 \div 3", font_size=36, color=WHITE).move_to(UP * 1.3)
        self.play(Write(eq1), run_time=0.6)

        eq2 = MathTex(r"x = 8", font_size=48, color=COLOR_HL).move_to(UP * 0.2)
        self.play(Write(eq2), run_time=0.6)
        self.play(Indicate(eq2, scale_factor=1.1, color=COLOR_HL), run_time=0.5)

        check_title = Text("检验：", font=FONT, font_size=22, color=COLOR_CHECK).move_to(DOWN * 1.2 + LEFT * 2.5)
        check = MathTex(r"3 \times 8 = 24\;\checkmark", font_size=30, color=COLOR_CHECK).move_to(DOWN * 1.2 + RIGHT * 0.5)
        self.play(Write(check_title), Write(check), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, eq0, solve, step1_hint, eq1, eq2, check_title, check)), run_time=0.4)

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=6.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text("解方程的步骤", font=FONT, font_size=30, color=COLOR_HL, weight=BOLD).move_to(UP * 3.0)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 观察方程类型", font=FONT, font_size=22, color=WHITE),
            Text("2. 利用等式性质恒等变形", font=FONT, font_size=22, color=COLOR_STEP),
            Text("3. 化简得到 x = ?", font=FONT, font_size=22, color=COLOR_HL),
            Text("4. 检验：代入原方程验证", font=FONT, font_size=22, color=COLOR_CHECK),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text("等号要上下对齐！", font=FONT, font_size=24, color=COLOR_X, weight=BOLD).move_to(DOWN * 2.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

    def scene_6_outro(self):
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=42, color=WHITE).move_to(UP * 2.0)
        author_id = Text("@emptyandcalm", font=FONT, font_size=30, color=GRAY_A).move_to(UP * 1.0)
        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=COLOR_HL).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(self.author_mob, author_id, follow)), run_time=0.8)


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 004_解简易方程.py SolveEquationLesson
#   高质量:    manim -qh  004_解简易方程.py SolveEquationLesson
#   4K:        manim -qk  004_解简易方程.py SolveEquationLesson
# ======================================================================

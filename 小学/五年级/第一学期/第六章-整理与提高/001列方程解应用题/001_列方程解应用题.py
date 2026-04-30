"""
001_列方程解应用题.py — 列方程解应用题 教学动画

知识点: 用方程解决实际问题的一般步骤
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 五步法: 审题→设未知数→找等量关系→列方程→解方程
  2. 例题: 小明买了3本笔记本和1支钢笔，共花了27元。
     钢笔12元，每本笔记本多少钱？
     设笔记本x元，3x + 12 = 27 → x = 5
  3. 检验: 3×5+12=27 ✓
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
COLOR_STEP = "#3b82f6"        # 蓝色步骤
COLOR_EQ = "#22c55e"          # 绿色等式
COLOR_X = "#f59e0b"           # 橙色未知数
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_CHECK = "#a78bfa"       # 紫色检验
COLOR_WARN = "#ef4444"        # 红色重点
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class EquationWordProblemLesson(Scene):
    """
    列方程解应用题教学动画
    场景:
      1. 开场钩子
      2. 五步法概览
      3. 例题: 审题与设未知数
      4. 列方程与求解
      5. 步骤总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_five_steps()
        self.scene_3_example_setup()
        self.scene_4_solve()
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
            "列方程解应用题", font=FONT, font_size=44, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "让复杂问题变简单！", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 五步法概览
    # ------------------------------------------------------------------

    def scene_2_five_steps(self):
        title = Text(
            "解题五步法", font=FONT, font_size=38,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        steps = VGroup(
            Text("1. 审题 — 理解题意", font=FONT, font_size=24, color=WHITE),
            Text("2. 设 — 设未知数 x", font=FONT, font_size=24, color=COLOR_X),
            Text("3. 找 — 找等量关系", font=FONT, font_size=24, color=COLOR_EQ),
            Text("4. 列 — 列方程", font=FONT, font_size=24, color=COLOR_HL),
            Text("5. 解 — 解方程并检验", font=FONT, font_size=24, color=COLOR_CHECK),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 1.5)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        key = Text(
            "关键：找等量关系！",
            font=FONT, font_size=26, color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, steps, key)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 例题 — 审题与设未知数
    # ------------------------------------------------------------------

    def scene_3_example_setup(self):
        title = Text(
            "例题", font=FONT, font_size=36,
            color=COLOR_EQ, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 题目
        q1 = Text(
            "小明买了3本笔记本和1支钢笔，",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 3.8)
        q2 = Text(
            "共花了27元。钢笔12元，",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 3.1)
        q3 = Text(
            "每本笔记本多少钱？",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.3)

        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.6)
        self.play(Write(q3), run_time=0.5)
        self.wait(0.5)

        # 设未知数
        s1 = Text(
            "设每本笔记本 x 元", font=FONT, font_size=26, color=COLOR_X
        ).move_to(UP * 0.8)
        self.play(FadeIn(s1, shift=UP * 0.2), run_time=0.6)

        # 找等量关系
        s2 = Text(
            "等量关系：", font=FONT, font_size=24, color=COLOR_EQ
        ).move_to(DOWN * 0.3)
        rel = Text(
            "笔记本钱 + 钢笔钱 = 总花费",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 1.1)
        self.play(Write(s2), run_time=0.4)
        self.play(Write(rel), run_time=0.6)

        # 列方程
        s3 = Text("列方程：", font=FONT, font_size=24, color=COLOR_HL)
        eq = MathTex(r"3x + 12 = 27", font_size=44, color=COLOR_HL)
        g3 = VGroup(s3, eq).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.5)
        self.play(FadeIn(g3, shift=UP * 0.3), run_time=0.7)
        self.play(Indicate(eq, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, q1, q2, q3, s1, s2, rel, g3)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 解方程与检验
    # ------------------------------------------------------------------

    def scene_4_solve(self):
        title = Text(
            "解方程", font=FONT, font_size=36,
            color=COLOR_X, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 原方程
        eq0 = MathTex(r"3x + 12 = 27", font_size=40, color=WHITE)
        eq0.move_to(UP * 3.5)
        self.play(Write(eq0), run_time=0.6)

        # 步骤1: 移项
        s1 = Text("两边减12：", font=FONT, font_size=22, color=GRAY_A)
        eq1 = MathTex(r"3x = 27 - 12", font_size=38, color=WHITE)
        g1 = VGroup(s1, eq1).arrange(RIGHT, buff=0.2).move_to(UP * 2.2)
        self.play(FadeIn(g1, shift=UP * 0.2), run_time=0.6)

        eq2 = MathTex(r"3x = 15", font_size=40, color=COLOR_EQ)
        eq2.move_to(UP * 1.2)
        self.play(Write(eq2), run_time=0.5)

        # 步骤2: 求x
        s2 = Text("两边除以3：", font=FONT, font_size=22, color=GRAY_A)
        eq3 = MathTex(r"x = 15 \div 3", font_size=38, color=WHITE)
        g2 = VGroup(s2, eq3).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.0)
        self.play(FadeIn(g2, shift=UP * 0.2), run_time=0.6)

        eq4 = MathTex(r"x = 5", font_size=48, color=COLOR_HL)
        eq4.move_to(DOWN * 1.2)
        self.play(Write(eq4), run_time=0.6)
        self.play(Indicate(eq4, scale_factor=1.1, color=COLOR_HL), run_time=0.5)

        # 检验
        check_title = Text(
            "检验：", font=FONT, font_size=24, color=COLOR_CHECK
        ).move_to(DOWN * 2.5)
        check = MathTex(
            r"3 \times 5 + 12 = 15 + 12 = 27\;\checkmark",
            font_size=30, color=COLOR_CHECK
        ).move_to(DOWN * 3.3)
        self.play(Write(check_title), run_time=0.4)
        self.play(Write(check), run_time=0.7)

        ans = Text(
            "每本笔记本5元", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(ans, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, eq0, g1, eq2, g2, eq4, check_title, check, ans)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 步骤总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=6.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "列方程解应用题", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.0)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 审题：理解已知和未知", font=FONT, font_size=22, color=WHITE),
            Text("2. 设：设未知数为 x", font=FONT, font_size=22, color=COLOR_X),
            Text("3. 找：找出等量关系", font=FONT, font_size=22, color=COLOR_EQ),
            Text("4. 列：列出方程", font=FONT, font_size=22, color=COLOR_HL),
            Text("5. 解：解方程并检验作答", font=FONT, font_size=22, color=COLOR_CHECK),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text(
            "记住：别忘了检验！",
            font=FONT, font_size=24, color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

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
#   快速预览:  manim -pql 001_列方程解应用题.py EquationWordProblemLesson
#   高质量:    manim -qh  001_列方程解应用题.py EquationWordProblemLesson
#   4K:        manim -qk  001_列方程解应用题.py EquationWordProblemLesson
# ======================================================================

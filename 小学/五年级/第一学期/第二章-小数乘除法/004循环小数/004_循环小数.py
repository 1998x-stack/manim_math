"""
004_循环小数.py — 循环小数 教学动画

知识点: 循环小数的概念、循环节、简便记法
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 什么是循环小数: 小数部分某位起，数字依次不断重复
  2. 例1: 1÷3 = 0.333... 循环节是3
  3. 例2: 1÷7 = 0.142857142857... 循环节是142857
  4. 简便记法: 循环节首位和末位上方加点
  5. 有限小数 vs 无限小数
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
COLOR_REPEAT = "#3b82f6"      # 蓝色循环部分
COLOR_NODE = "#22c55e"         # 绿色循环节
COLOR_DOT = "#ef4444"          # 红色点标记
COLOR_HL = "#fbbf24"           # 黄色高亮
COLOR_FINITE = "#f59e0b"       # 橙色有限小数
COLOR_INFINITE = "#a78bfa"     # 紫色无限小数
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class RepeatingDecimalLesson(Scene):
    """
    循环小数教学动画
    场景:
      1. 开场钩子
      2. 发现循环: 1÷3
      3. 循环节的概念
      4. 简便记法
      5. 分类总结: 有限小数 vs 无限小数
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_discover_repeat()
        self.scene_3_repeat_unit()
        self.scene_4_notation()
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
            "有些小数", font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "永远除不尽！", font=FONT, font_size=48, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示 0.333...
        dots = MathTex(
            r"0.333333333\ldots", font_size=44, color=COLOR_REPEAT
        ).move_to(UP * 1.0)
        self.play(FadeIn(dots, scale=0.6), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, dots)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 发现循环 — 1÷3
    # ------------------------------------------------------------------

    def scene_2_discover_repeat(self):
        title = Text(
            "除法中的循环", font=FONT, font_size=36,
            color=COLOR_REPEAT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 除法算式
        problem = MathTex(r"1 \div 3 = \;?", font_size=44, color=WHITE)
        problem.move_to(UP * 3.5)
        self.play(Write(problem), run_time=0.6)

        # 逐步展示
        step1 = MathTex(r"= 0.3\ldots", font_size=40, color=GRAY_A)
        step1.move_to(UP * 2.3)
        self.play(Write(step1), run_time=0.5)

        step2 = MathTex(r"= 0.33\ldots", font_size=40, color=GRAY_A)
        step2.move_to(UP * 1.3)
        self.play(Write(step2), run_time=0.5)

        step3 = MathTex(r"= 0.333\ldots", font_size=40, color=GRAY_A)
        step3.move_to(UP * 0.3)
        self.play(Write(step3), run_time=0.5)

        step4 = MathTex(r"= 0.3333\ldots", font_size=40, color=COLOR_REPEAT)
        step4.move_to(DOWN * 0.7)
        self.play(Write(step4), run_time=0.5)
        self.wait(0.3)

        # 发现
        discover = Text(
            "3 一直在重复！永远除不尽！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(discover, shift=UP * 0.3), run_time=0.6)

        # 定义
        define = Text(
            "这就是循环小数",
            font=FONT, font_size=28, color=COLOR_NODE
        ).move_to(DOWN * 3.2)
        self.play(Write(define), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, problem, step1, step2, step3, step4,
                          discover, define)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 循环节的概念
    # ------------------------------------------------------------------

    def scene_3_repeat_unit(self):
        title = Text(
            "循环节", font=FONT, font_size=38,
            color=COLOR_NODE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义
        define = Text(
            "依次不断重复出现的数字",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.0)
        self.play(Write(define), run_time=0.5)

        # 例1: 0.333... 循环节是 3
        ex1_label = Text("例1：", font=FONT, font_size=24, color=WHITE)
        ex1_num = MathTex(r"0.333\ldots", font_size=36, color=COLOR_REPEAT)
        ex1 = VGroup(ex1_label, ex1_num).arrange(RIGHT, buff=0.1).move_to(UP * 2.5)
        self.play(FadeIn(ex1), run_time=0.5)

        ex1_node = VGroup(
            Text("循环节：", font=FONT, font_size=22, color=WHITE),
            MathTex(r"3", font_size=36, color=COLOR_NODE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.5)
        self.play(FadeIn(ex1_node, shift=UP * 0.2), run_time=0.5)

        # 例2: 1÷7 = 0.142857142857...
        ex2_label = Text("例2：", font=FONT, font_size=24, color=WHITE)
        ex2_eq = MathTex(r"1 \div 7 =", font_size=32, color=WHITE)
        ex2_num = MathTex(r"0.142857\ldots", font_size=32, color=COLOR_REPEAT)
        ex2 = VGroup(ex2_label, ex2_eq, ex2_num).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.0)
        self.play(FadeIn(ex2), run_time=0.5)

        ex2_node = VGroup(
            Text("循环节：", font=FONT, font_size=22, color=WHITE),
            MathTex(r"142857", font_size=36, color=COLOR_NODE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.0)
        self.play(FadeIn(ex2_node, shift=UP * 0.2), run_time=0.5)

        # 例3: 1÷6 = 0.1666...
        ex3_label = Text("例3：", font=FONT, font_size=24, color=WHITE)
        ex3_eq = MathTex(r"1 \div 6 =", font_size=32, color=WHITE)
        ex3_num = MathTex(r"0.1666\ldots", font_size=32, color=COLOR_REPEAT)
        ex3 = VGroup(ex3_label, ex3_eq, ex3_num).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)
        self.play(FadeIn(ex3), run_time=0.5)

        ex3_node = VGroup(
            Text("循环节：", font=FONT, font_size=22, color=WHITE),
            MathTex(r"6", font_size=36, color=COLOR_NODE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)
        self.play(FadeIn(ex3_node, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, define, ex1, ex1_node, ex2, ex2_node,
                          ex3, ex3_node)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 简便记法
    # ------------------------------------------------------------------

    def scene_4_notation(self):
        title = Text(
            "简便记法", font=FONT, font_size=38,
            color=COLOR_DOT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        rule = Text(
            "在循环节首位和末位上方各加一个点",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.0)
        self.play(Write(rule), run_time=0.6)

        # 例1: 0.333... = 0.3(dot)
        ex1_orig = MathTex(r"0.333\ldots", font_size=38, color=WHITE)
        ex1_arrow = MathTex(r"\Rightarrow", font_size=30, color=COLOR_HL)
        ex1_short = MathTex(r"0.\dot{3}", font_size=44, color=COLOR_DOT)
        g1 = VGroup(ex1_orig, ex1_arrow, ex1_short).arrange(RIGHT, buff=0.3).move_to(UP * 2.3)
        self.play(FadeIn(g1), run_time=0.7)
        self.wait(0.3)

        # 例2: 0.142857142857... = 0.142857(dots)
        ex2_orig = MathTex(r"0.142857\ldots", font_size=32, color=WHITE)
        ex2_arrow = MathTex(r"\Rightarrow", font_size=30, color=COLOR_HL)
        ex2_short = MathTex(r"0.\dot{1}4285\dot{7}", font_size=36, color=COLOR_DOT)
        g2 = VGroup(ex2_orig, ex2_arrow, ex2_short).arrange(RIGHT, buff=0.2).move_to(UP * 0.8)
        self.play(FadeIn(g2), run_time=0.7)
        self.wait(0.3)

        # 例3: 0.1666... = 0.16(dot on 6)
        ex3_orig = MathTex(r"0.1666\ldots", font_size=38, color=WHITE)
        ex3_arrow = MathTex(r"\Rightarrow", font_size=30, color=COLOR_HL)
        ex3_short = MathTex(r"0.1\dot{6}", font_size=44, color=COLOR_DOT)
        g3 = VGroup(ex3_orig, ex3_arrow, ex3_short).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.7)
        self.play(FadeIn(g3), run_time=0.7)
        self.wait(0.3)

        # 注意
        note = Text(
            "只有一位循环节时，只加一个点",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.2)
        self.play(Write(note), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, rule, g1, g2, g3, note)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 分类总结
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
            "小数的分类", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.3)
        self.play(Write(sum_title), run_time=0.5)

        # 有限小数
        f_title = Text("有限小数", font=FONT, font_size=26, color=COLOR_FINITE, weight=BOLD)
        f_desc = Text("小数位数有限", font=FONT, font_size=20, color=GRAY_A)
        f_ex = MathTex(r"0.5,\quad 3.14,\quad 0.125", font_size=26, color=COLOR_FINITE)
        f_block = VGroup(f_title, f_desc, f_ex).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        f_block.move_to(UP * 1.5 + LEFT * 0.3)
        self.play(FadeIn(f_block, shift=RIGHT * 0.3), run_time=0.6)

        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY, stroke_width=1).move_to(UP * 0.2)
        self.play(Create(sep), run_time=0.3)

        # 无限小数
        inf_title = Text("无限小数", font=FONT, font_size=26, color=COLOR_INFINITE, weight=BOLD)
        inf_desc = Text("小数位数无限", font=FONT, font_size=20, color=GRAY_A)
        inf_block = VGroup(inf_title, inf_desc).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        inf_block.move_to(DOWN * 0.6 + LEFT * 0.3)
        self.play(FadeIn(inf_block, shift=RIGHT * 0.3), run_time=0.5)

        # 循环小数
        cyc = VGroup(
            Text("  循环小数：", font=FONT, font_size=20, color=COLOR_REPEAT),
            MathTex(r"0.\dot{3}", font_size=26, color=COLOR_REPEAT),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.5 + LEFT * 0.5)
        self.play(FadeIn(cyc), run_time=0.4)

        # 不循环小数
        ncyc = VGroup(
            Text("  不循环小数：", font=FONT, font_size=20, color=GRAY_A),
            MathTex(r"\pi = 3.14159\ldots", font_size=26, color=GRAY_A),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.3 + LEFT * 0.3)
        self.play(FadeIn(ncyc), run_time=0.4)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, f_block, sep, inf_block, cyc, ncyc)), run_time=0.5)

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
#   快速预览:  manim -pql 004_循环小数.py RepeatingDecimalLesson
#   高质量:    manim -qh  004_循环小数.py RepeatingDecimalLesson
#   4K:        manim -qk  004_循环小数.py RepeatingDecimalLesson
# ======================================================================

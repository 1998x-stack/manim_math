"""
002_积的近似值.py — 积的近似值 教学动画

知识点: 用四舍五入法保留小数位数，求积的近似值
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 四舍五入法: 看保留位数的下一位，<5舍，≥5入
  2. 例1: 0.8 × 0.9 = 0.72 ≈ 0.7 (保留一位小数)
  3. 例2: 3.27 × 1.5 = 4.905 ≈ 4.91 (保留两位小数)
  4. 实际应用: 面积、付款中取近似值
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
COLOR_EXACT = "#3b82f6"       # 蓝色精确值
COLOR_APPROX = "#22c55e"      # 绿色近似值
COLOR_KEY = "#f59e0b"         # 橙色关键位
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_WARN = "#ef4444"        # 红色提示
COLOR_RULE = "#a78bfa"        # 紫色规则
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class ApproximateProductLesson(Scene):
    """
    积的近似值教学动画
    场景:
      1. 开场钩子
      2. 四舍五入法
      3. 例题1: 0.8×0.9 保留一位小数
      4. 例题2: 3.27×1.5 保留两位小数
      5. 总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_rounding_rule()
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
            "积的近似值", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "怎么取近似值？", font=FONT, font_size=38, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 四舍五入法
    # ------------------------------------------------------------------

    def scene_2_rounding_rule(self):
        title = Text(
            "四舍五入法", font=FONT, font_size=38,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 规则
        rule1 = Text(
            "看保留位数的下一位", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(rule1), run_time=0.5)

        # 四舍
        r_four = VGroup(
            Text("下一位 < 5 →", font=FONT, font_size=24, color=GRAY_A),
            Text(" 舍去", font=FONT, font_size=28, color=COLOR_APPROX, weight=BOLD),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 2.0)
        self.play(FadeIn(r_four, shift=UP * 0.2), run_time=0.5)

        ex_four = MathTex(
            r"3.142 \approx 3.14", font_size=34, color=WHITE
        ).move_to(UP * 1.0)
        self.play(Write(ex_four), run_time=0.6)

        # 五入
        r_five = VGroup(
            Text("下一位 >= 5 →", font=FONT, font_size=24, color=GRAY_A),
            Text(" 进一", font=FONT, font_size=28, color=COLOR_WARN, weight=BOLD),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.5)
        self.play(FadeIn(r_five, shift=UP * 0.2), run_time=0.5)

        ex_five = MathTex(
            r"3.146 \approx 3.15", font_size=34, color=WHITE
        ).move_to(DOWN * 1.5)
        self.play(Write(ex_five), run_time=0.6)

        # 口诀
        motto = Text(
            "四舍五入，看下一位！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(motto, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, rule1, r_four, ex_four, r_five, ex_five, motto)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 例题1 — 0.8 × 0.9 保留一位小数
    # ------------------------------------------------------------------

    def scene_3_example_1(self):
        title = Text(
            "例题一", font=FONT, font_size=36,
            color=COLOR_EXACT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 题目
        problem = VGroup(
            MathTex(r"0.8 \times 0.9", font_size=42, color=WHITE),
            Text("（保留一位小数）", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.5)
        self.play(Write(problem), run_time=0.7)

        # 精确计算
        s1 = Text("先精确计算：", font=FONT, font_size=24, color=COLOR_HL)
        calc = MathTex(r"0.8 \times 0.9 = 0.72", font_size=38, color=COLOR_EXACT)
        g1 = VGroup(s1, calc).arrange(DOWN, buff=0.2).move_to(UP * 1.8)
        self.play(FadeIn(g1), run_time=0.6)
        self.wait(0.3)

        # 取近似值
        s2 = Text("保留一位小数，看第二位小数：", font=FONT, font_size=22, color=WHITE)
        s2.move_to(UP * 0.3)
        self.play(Write(s2), run_time=0.5)

        # 高亮关键位
        key_show = VGroup(
            MathTex(r"0.7", font_size=42, color=COLOR_APPROX),
            MathTex(r"2", font_size=42, color=COLOR_KEY),
        ).arrange(RIGHT, buff=0.02).move_to(DOWN * 0.7)

        key_label = Text(
            "2 < 5，舍去！", font=FONT, font_size=24, color=COLOR_APPROX
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(key_show), run_time=0.5)
        self.play(FadeIn(key_label, shift=UP * 0.2), run_time=0.5)

        # 结果
        result = VGroup(
            MathTex(r"0.8 \times 0.9 \approx", font_size=36, color=WHITE),
            MathTex(r"0.7", font_size=44, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.2)
        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(result[1], scale_factor=1.2, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, problem, g1, s2, key_show, key_label, result)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 例题2 — 3.27 × 1.5 保留两位小数
    # ------------------------------------------------------------------

    def scene_4_example_2(self):
        title = Text(
            "例题二", font=FONT, font_size=36,
            color=COLOR_APPROX, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        problem = VGroup(
            MathTex(r"3.27 \times 1.5", font_size=42, color=WHITE),
            Text("（保留两位小数）", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.5)
        self.play(Write(problem), run_time=0.7)

        # 精确计算
        s1 = Text("先精确计算：", font=FONT, font_size=24, color=COLOR_HL)
        calc = MathTex(r"3.27 \times 1.5 = 4.905", font_size=36, color=COLOR_EXACT)
        g1 = VGroup(s1, calc).arrange(DOWN, buff=0.2).move_to(UP * 1.8)
        self.play(FadeIn(g1), run_time=0.6)
        self.wait(0.3)

        s2 = Text("保留两位小数，看第三位小数：", font=FONT, font_size=22, color=WHITE)
        s2.move_to(UP * 0.3)
        self.play(Write(s2), run_time=0.5)

        key_show = VGroup(
            MathTex(r"4.90", font_size=42, color=COLOR_APPROX),
            MathTex(r"5", font_size=42, color=COLOR_KEY),
        ).arrange(RIGHT, buff=0.02).move_to(DOWN * 0.7)

        key_label = Text(
            "5 >= 5，进一！", font=FONT, font_size=24, color=COLOR_WARN
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(key_show), run_time=0.5)
        self.play(FadeIn(key_label, shift=UP * 0.2), run_time=0.5)

        result = VGroup(
            MathTex(r"3.27 \times 1.5 \approx", font_size=34, color=WHITE),
            MathTex(r"4.91", font_size=44, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.2)
        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(result[1], scale_factor=1.2, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, problem, g1, s2, key_show, key_label, result)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=5.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "积的近似值步骤", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.8)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 先精确计算出积", font=FONT, font_size=22, color=WHITE),
            Text("2. 确定保留几位小数", font=FONT, font_size=22, color=WHITE),
            Text("3. 看下一位数字", font=FONT, font_size=22, color=COLOR_KEY),
            Text("4. < 5 舍去，>= 5 进一", font=FONT, font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text(
            "别忘了用 ≈ 号表示近似！",
            font=FONT, font_size=22, color=COLOR_WARN
        ).move_to(DOWN * 2.0)
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
#   快速预览:  manim -pql 002_积的近似值.py ApproximateProductLesson
#   高质量:    manim -qh  002_积的近似值.py ApproximateProductLesson
#   4K:        manim -qk  002_积的近似值.py ApproximateProductLesson
# ======================================================================

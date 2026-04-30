"""
001_小数乘小数.py — 小数乘小数 教学动画

知识点: 转化为整数乘法计算，因数共有几位小数，积就有几位小数
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 算理: 先按整数乘法算，再数小数位数点小数点
  2. 例题1: 0.3 × 0.4 → 3 × 4 = 12 → 两位小数 → 0.12
  3. 例题2: 0.03 × 0.05 → 3 × 5 = 15 → 四位小数 → 0.0015 (补0)
  4. 规律: 因数中小数位数之和 = 积的小数位数
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
COLOR_FACTOR1 = "#3b82f6"     # 蓝色因数1
COLOR_FACTOR2 = "#22c55e"     # 绿色因数2
COLOR_PRODUCT = "#f59e0b"     # 橙色积
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_WARN = "#ef4444"        # 红色警示
COLOR_RULE = "#a78bfa"        # 紫色规则
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class DecimalMultiplicationLesson(Scene):
    """
    小数乘小数教学动画
    场景:
      1. 开场钩子
      2. 算理: 转化为整数乘法
      3. 例题1: 0.3 × 0.4 = 0.12
      4. 例题2: 0.03 × 0.05 = 0.0015 (补0)
      5. 规律总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_principle()
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
            "小数乘小数", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "小数点放哪里？", font=FONT, font_size=40, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        problem = MathTex(r"0.3 \times 0.4 = \;?", font_size=48, color=COLOR_FACTOR1)
        problem.move_to(UP * 1.0)
        self.play(FadeIn(problem, scale=0.6), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, problem)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 算理 — 转化为整数乘法
    # ------------------------------------------------------------------

    def scene_2_principle(self):
        title = Text(
            "算理：转化为整数", font=FONT, font_size=36,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 整数例子
        desc = Text(
            "我们已经会算整数乘法", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.0)
        self.play(Write(desc), run_time=0.4)

        int_eq = MathTex(r"3 \times 4 = 12", font_size=44, color=WHITE)
        int_eq.move_to(UP * 2.5)
        self.play(Write(int_eq), run_time=0.6)
        self.wait(0.3)

        # 那小数怎么办?
        q = Text(
            "小数怎么办？先变成整数！", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 1.0)
        self.play(Write(q), run_time=0.6)

        # 转化过程
        step1 = VGroup(
            MathTex(r"0.3", font_size=38, color=COLOR_FACTOR1),
            MathTex(r"\times 10", font_size=28, color=COLOR_PRODUCT),
            MathTex(r"= 3", font_size=38, color=COLOR_FACTOR1),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.3)

        step2 = VGroup(
            MathTex(r"0.4", font_size=38, color=COLOR_FACTOR2),
            MathTex(r"\times 10", font_size=28, color=COLOR_PRODUCT),
            MathTex(r"= 4", font_size=38, color=COLOR_FACTOR2),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.3)

        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 积要缩回去
        step3 = Text(
            "积被扩大了 10×10=100 倍", font=FONT, font_size=22, color=COLOR_WARN
        ).move_to(DOWN * 2.5)
        step4 = Text(
            "所以积要缩小100倍（除以100）", font=FONT, font_size=22, color=COLOR_PRODUCT
        ).move_to(DOWN * 3.3)

        self.play(Write(step3), run_time=0.5)
        self.play(Write(step4), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, desc, int_eq, q, step1, step2, step3, step4)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 例题1 — 0.3 × 0.4 = 0.12
    # ------------------------------------------------------------------

    def scene_3_example_1(self):
        title = Text(
            "例题一", font=FONT, font_size=36,
            color=COLOR_FACTOR1, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 原式
        orig = MathTex(r"0.3 \times 0.4", font_size=44, color=WHITE)
        orig.move_to(UP * 3.5)
        self.play(Write(orig), run_time=0.7)

        # 步骤1: 按整数算
        s1 = Text(
            "第一步：按整数算", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 2.3)
        self.play(Write(s1), run_time=0.5)

        calc = MathTex(r"3 \times 4 = 12", font_size=42, color=COLOR_PRODUCT)
        calc.move_to(UP * 1.2)
        self.play(Write(calc), run_time=0.6)
        self.wait(0.3)

        # 步骤2: 数小数位数
        s2 = Text(
            "第二步：数小数位数", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 0.0)
        self.play(Write(s2), run_time=0.5)

        count = VGroup(
            MathTex(r"0.3", font_size=34, color=COLOR_FACTOR1),
            Text(" → 1位", font=FONT, font_size=22, color=COLOR_FACTOR1),
            MathTex(r"\quad 0.4", font_size=34, color=COLOR_FACTOR2),
            Text(" → 1位", font=FONT, font_size=22, color=COLOR_FACTOR2),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.0)
        self.play(FadeIn(count), run_time=0.5)

        total = VGroup(
            Text("共 ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"1 + 1 = 2", font_size=30, color=COLOR_HL),
            Text(" 位小数", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 1.8)
        self.play(FadeIn(total), run_time=0.5)
        self.wait(0.3)

        # 步骤3: 点小数点
        s3 = Text(
            "第三步：从右数2位，点小数点", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.8)
        self.play(Write(s3), run_time=0.5)

        result = VGroup(
            MathTex(r"12", font_size=38, color=WHITE),
            MathTex(r"\rightarrow", font_size=30, color=COLOR_PRODUCT),
            MathTex(r"0.12", font_size=44, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.8)
        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.6)

        # 最终等式
        final = MathTex(
            r"0.3 \times 0.4 = 0.12", font_size=40, color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(final, shift=UP * 0.2), run_time=0.6)
        self.play(Indicate(final, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, orig, s1, calc, s2, count, total, s3, result, final)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 例题2 — 0.03 × 0.05 = 0.0015 (需要补0)
    # ------------------------------------------------------------------

    def scene_4_example_2(self):
        title = Text(
            "例题二（补0）", font=FONT, font_size=36,
            color=COLOR_WARN, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        orig = MathTex(r"0.03 \times 0.05", font_size=44, color=WHITE)
        orig.move_to(UP * 3.5)
        self.play(Write(orig), run_time=0.7)

        # 按整数算
        s1 = Text("按整数算：", font=FONT, font_size=24, color=COLOR_HL)
        calc = MathTex(r"3 \times 5 = 15", font_size=42, color=COLOR_PRODUCT)
        g1 = VGroup(s1, calc).arrange(RIGHT, buff=0.2).move_to(UP * 2.0)
        self.play(FadeIn(g1), run_time=0.6)

        # 数小数位数
        count = VGroup(
            MathTex(r"0.03", font_size=34, color=COLOR_FACTOR1),
            Text(" → 2位", font=FONT, font_size=22, color=COLOR_FACTOR1),
            MathTex(r"\quad 0.05", font_size=34, color=COLOR_FACTOR2),
            Text(" → 2位", font=FONT, font_size=22, color=COLOR_FACTOR2),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 0.8)
        self.play(FadeIn(count), run_time=0.5)

        total = VGroup(
            Text("共 ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"2 + 2 = 4", font_size=30, color=COLOR_HL),
            Text(" 位小数", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 0.0)
        self.play(FadeIn(total), run_time=0.5)
        self.wait(0.3)

        # 问题：15只有2位，需要4位
        warn = Text(
            "15只有2位数字，不够4位！", font=FONT, font_size=24,
            color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(warn, shift=UP * 0.3), run_time=0.6)

        # 解决：前面补0
        solution = Text(
            "解决：前面用0补足位数", font=FONT, font_size=24, color=COLOR_PRODUCT
        ).move_to(DOWN * 2.2)
        self.play(Write(solution), run_time=0.5)

        fill = VGroup(
            MathTex(r"15", font_size=38, color=WHITE),
            MathTex(r"\rightarrow", font_size=30, color=COLOR_PRODUCT),
            MathTex(r"0015", font_size=38, color=COLOR_PRODUCT),
            MathTex(r"\rightarrow", font_size=30, color=COLOR_PRODUCT),
            MathTex(r"0.0015", font_size=44, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 3.3)
        self.play(FadeIn(fill, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)

        final = MathTex(
            r"0.03 \times 0.05 = 0.0015", font_size=38, color=COLOR_HL
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(final, shift=UP * 0.2), run_time=0.6)
        self.play(Indicate(final, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, orig, g1, count, total, warn, solution, fill, final)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 规律总结
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
            "小数乘小数三步法", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.0)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 先按整数乘法计算", font=FONT, font_size=22, color=WHITE),
            Text("2. 数两个因数共有几位小数", font=FONT, font_size=22, color=WHITE),
            Text("3. 在积中从右往左数相同位数", font=FONT, font_size=22, color=WHITE),
            Text("   点上小数点", font=FONT, font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 1.0)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        warn = Text(
            "位数不够时，前面用0补足！",
            font=FONT, font_size=24, color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(warn, shift=UP * 0.2), run_time=0.5)

        rule = Text(
            "因数小数位数之和 = 积的小数位数",
            font=FONT, font_size=22, color=COLOR_RULE
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, warn, rule)), run_time=0.5)

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
#   快速预览:  manim -pql 001_小数乘小数.py DecimalMultiplicationLesson
#   高质量:    manim -qh  001_小数乘小数.py DecimalMultiplicationLesson
#   4K:        manim -qk  001_小数乘小数.py DecimalMultiplicationLesson
# ======================================================================

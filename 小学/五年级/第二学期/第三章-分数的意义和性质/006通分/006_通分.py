"""
006_通分.py — 通分 教学动画

知识点: 通分 — 把异分母分数化成同分母分数
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 为什么需要通分(异分母无法直接比较/运算)
  2. 通分的概念: 化成同分母分数
  3. 公分母 = 最小公倍数
  4. 例1: 1/2 和 1/3 → 3/6 和 2/6
  5. 例2: 2/3 和 3/4 → 8/12 和 9/12
  6. 通分后可以比较大小
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
COLOR_FRAC_A = "#3b82f6"    # 蓝色分数A
COLOR_FRAC_B = "#22c55e"    # 绿色分数B
COLOR_COMMON = "#f59e0b"    # 橙色公分母
COLOR_HL = "#fbbf24"        # 黄色高亮
COLOR_STEP = "#a78bfa"      # 紫色步骤
COLOR_WARN = "#ef4444"      # 红色
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class CommonDenominatorLesson(Scene):
    """
    通分教学动画
    场景:
      1. 开场钩子
      2. 为什么需要通分
      3. 通分的概念
      4. 例1: 1/2 和 1/3 通分(带矩形可视化)
      5. 例2: 2/3 和 3/4 通分
      6. 通分后比大小
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_why_need()
        self.scene_3_concept()
        self.scene_4_example1()
        self.scene_5_example2()
        self.scene_6_compare()
        self.scene_7_summary()
        self.scene_8_outro()

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
            "通分", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "统一分数的语言！", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 为什么需要通分
    # ------------------------------------------------------------------
    def scene_2_why_need(self):
        title = Text(
            "为什么需要通分？", font=FONT, font_size=36,
            color=COLOR_WARN, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 问题
        question = Text(
            "哪个更大？", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(question), run_time=0.5)

        frac_a = MathTex(r"\frac{1}{2}", font_size=64, color=COLOR_FRAC_A).move_to(UP * 2.5 + LEFT * 2.0)
        vs = Text("和", font=FONT, font_size=28, color=GRAY_A).move_to(UP * 2.5)
        frac_b = MathTex(r"\frac{1}{3}", font_size=64, color=COLOR_FRAC_B).move_to(UP * 2.5 + RIGHT * 2.0)
        self.play(Write(frac_a), FadeIn(vs), Write(frac_b), run_time=0.6)

        # 问题: 分母不同
        problem1 = Text(
            "分母不同 → 分数单位不同", font=FONT, font_size=24, color=COLOR_WARN
        ).move_to(UP * 0.8)
        problem2 = Text(
            "无法直接比较和计算！", font=FONT, font_size=24, color=COLOR_WARN, weight=BOLD
        ).move_to(UP * 0.0)
        self.play(FadeIn(problem1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(problem2, shift=UP * 0.2), run_time=0.5)

        # 解决方案
        solution = Text(
            "解决办法：通分！", font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 1.5)
        sol_box = SurroundingRectangle(solution, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(solution, shift=UP * 0.2), Create(sol_box), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, question, frac_a, vs, frac_b,
            problem1, problem2, solution, sol_box
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 通分的概念
    # ------------------------------------------------------------------
    def scene_3_concept(self):
        title = Text(
            "什么是通分？", font=FONT, font_size=36,
            color=COLOR_COMMON, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        defn = Text(
            "把异分母分数化成同分母分数", font=FONT,
            font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(defn), run_time=0.6)

        # 关键步骤
        steps = VGroup(
            Text("1. 找公分母（通常取最小公倍数）", font=FONT, font_size=22, color=COLOR_STEP),
            Text("2. 分子分母同乘相应倍数", font=FONT, font_size=22, color=COLOR_FRAC_A),
            Text("3. 得到同分母的等值分数", font=FONT, font_size=22, color=COLOR_FRAC_B),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 2.0)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.3)

        # 依据
        basis = Text(
            "依据：分数的基本性质", font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.5)
        formula = MathTex(
            r"\frac{a}{b} = \frac{a \times c}{b \times c}",
            font_size=36, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        cond = MathTex(r"(c \neq 0)", font_size=24, color=GRAY_A).next_to(formula, RIGHT, buff=0.2)
        self.play(FadeIn(basis, shift=UP * 0.2), run_time=0.5)
        self.play(Write(formula), FadeIn(cond), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, defn, steps, basis, formula, cond)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 例1 — 1/2 和 1/3 通分
    # ------------------------------------------------------------------
    def scene_4_example1(self):
        title = Text(
            "例1：通分", font=FONT, font_size=36,
            color=COLOR_FRAC_A, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 原分数
        orig = VGroup(
            MathTex(r"\frac{1}{2}", font_size=48, color=COLOR_FRAC_A),
            Text("和", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"\frac{1}{3}", font_size=48, color=COLOR_FRAC_B),
        ).arrange(RIGHT, buff=0.5).move_to(UP * 4.0)
        self.play(FadeIn(orig), run_time=0.5)

        # 第一步: 找公分母
        step1_label = Text(
            "第1步：找公分母", font=FONT, font_size=22, color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 2.8 + LEFT * 2.0)
        lcm_calc = VGroup(
            Text("2的倍数：2, 4, 6, 8 ...", font=FONT, font_size=20, color=COLOR_FRAC_A),
            Text("3的倍数：3, 6, 9 ...", font=FONT, font_size=20, color=COLOR_FRAC_B),
            Text("最小公倍数 = 6", font=FONT, font_size=22, color=COLOR_COMMON, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 1.5)
        self.play(FadeIn(step1_label, shift=RIGHT * 0.2), run_time=0.4)
        for item in lcm_calc:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.5)

        # 第二步: 化分数
        step2_label = Text(
            "第2步：化同分母", font=FONT, font_size=22, color=COLOR_STEP, weight=BOLD
        ).move_to(DOWN * 0.3 + LEFT * 2.0)
        self.play(FadeIn(step2_label, shift=RIGHT * 0.2), run_time=0.4)

        # 1/2 → 3/6
        conv_a = MathTex(
            r"\frac{1}{2} = \frac{1 \times 3}{2 \times 3} = \frac{3}{6}",
            font_size=32, color=COLOR_FRAC_A
        ).move_to(DOWN * 1.3)
        self.play(Write(conv_a), run_time=0.7)

        # 1/3 → 2/6
        conv_b = MathTex(
            r"\frac{1}{3} = \frac{1 \times 2}{3 \times 2} = \frac{2}{6}",
            font_size=32, color=COLOR_FRAC_B
        ).move_to(DOWN * 2.5)
        self.play(Write(conv_b), run_time=0.7)

        # 结果
        result = VGroup(
            MathTex(r"\frac{3}{6}", font_size=42, color=COLOR_FRAC_A),
            Text("和", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"\frac{2}{6}", font_size=42, color=COLOR_FRAC_B),
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 4.0)
        result_box = SurroundingRectangle(result, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(result, shift=UP * 0.2), Create(result_box), run_time=0.6)
        self.play(Indicate(result, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, orig, step1_label, lcm_calc,
            step2_label, conv_a, conv_b, result, result_box
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 5: 例2 — 2/3 和 3/4 通分
    # ------------------------------------------------------------------
    def scene_5_example2(self):
        title = Text(
            "例2：通分", font=FONT, font_size=36,
            color=COLOR_FRAC_B, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 原分数
        orig = VGroup(
            MathTex(r"\frac{2}{3}", font_size=48, color=COLOR_FRAC_A),
            Text("和", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"\frac{3}{4}", font_size=48, color=COLOR_FRAC_B),
        ).arrange(RIGHT, buff=0.5).move_to(UP * 4.0)
        self.play(FadeIn(orig), run_time=0.5)

        # 找公分母
        lcm_info = VGroup(
            Text("3和4的最小公倍数 = 12", font=FONT, font_size=24, color=COLOR_COMMON, weight=BOLD),
            Text("公分母是12", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(DOWN, buff=0.2).move_to(UP * 2.5)
        self.play(FadeIn(lcm_info, shift=UP * 0.2), run_time=0.5)

        # 2/3 → 8/12
        conv_a = MathTex(
            r"\frac{2}{3} = \frac{2 \times 4}{3 \times 4} = \frac{8}{12}",
            font_size=32, color=COLOR_FRAC_A
        ).move_to(UP * 1.0)
        self.play(Write(conv_a), run_time=0.7)

        # 3/4 → 9/12
        conv_b = MathTex(
            r"\frac{3}{4} = \frac{3 \times 3}{4 \times 3} = \frac{9}{12}",
            font_size=32, color=COLOR_FRAC_B
        ).move_to(DOWN * 0.2)
        self.play(Write(conv_b), run_time=0.7)

        # 矩形可视化
        vis_label = Text(
            "图示验证：", font=FONT, font_size=22, color=COLOR_STEP
        ).move_to(DOWN * 1.5 + LEFT * 2.5)
        self.play(FadeIn(vis_label), run_time=0.3)

        # 8/12 矩形
        rect_a = Rectangle(width=6.0, height=0.8, stroke_color=COLOR_FRAC_A, stroke_width=2).move_to(DOWN * 2.5)
        parts_a = VGroup()
        for i in range(12):
            x = rect_a.get_left()[0] + 0.5 * i + 0.25
            part = Rectangle(
                width=0.5, height=0.8, stroke_color=GRAY, stroke_width=1,
                fill_color=COLOR_FRAC_A if i < 8 else DARK_GRAY,
                fill_opacity=0.4 if i < 8 else 0.1
            ).move_to(np.array([x, rect_a.get_center()[1], 0]))
            parts_a.add(part)
        label_a = MathTex(r"\frac{8}{12}", font_size=24, color=COLOR_FRAC_A).next_to(rect_a, LEFT, buff=0.2)
        self.play(FadeIn(parts_a), FadeIn(label_a), run_time=0.5)

        # 9/12 矩形
        rect_b_y = DOWN * 3.8
        parts_b = VGroup()
        for i in range(12):
            x = rect_a.get_left()[0] + 0.5 * i + 0.25
            part = Rectangle(
                width=0.5, height=0.8, stroke_color=GRAY, stroke_width=1,
                fill_color=COLOR_FRAC_B if i < 9 else DARK_GRAY,
                fill_opacity=0.4 if i < 9 else 0.1
            ).move_to(np.array([x, rect_b_y[1], 0]))
            parts_b.add(part)
        label_b = MathTex(r"\frac{9}{12}", font_size=24, color=COLOR_FRAC_B).next_to(parts_b, LEFT, buff=0.2)
        self.play(FadeIn(parts_b), FadeIn(label_b), run_time=0.5)

        # 结论
        conclusion = Text(
            "9/12 > 8/12，所以 3/4 > 2/3", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, orig, lcm_info, conv_a, conv_b,
            vis_label, parts_a, label_a, parts_b, label_b, conclusion
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 通分后比大小
    # ------------------------------------------------------------------
    def scene_6_compare(self):
        title = Text(
            "通分的应用：比大小", font=FONT, font_size=36,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 问题
        q = Text(
            "比较 5/6 和 7/8 的大小", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(q), run_time=0.5)

        # 步骤
        s1 = Text(
            "找公分母：LCM(6, 8) = 24", font=FONT, font_size=22, color=COLOR_COMMON
        ).move_to(UP * 2.8)
        self.play(FadeIn(s1, shift=RIGHT * 0.2), run_time=0.4)

        s2 = MathTex(
            r"\frac{5}{6} = \frac{5 \times 4}{6 \times 4} = \frac{20}{24}",
            font_size=32, color=COLOR_FRAC_A
        ).move_to(UP * 1.5)
        self.play(Write(s2), run_time=0.6)

        s3 = MathTex(
            r"\frac{7}{8} = \frac{7 \times 3}{8 \times 3} = \frac{21}{24}",
            font_size=32, color=COLOR_FRAC_B
        ).move_to(UP * 0.2)
        self.play(Write(s3), run_time=0.6)

        # 比较
        compare = MathTex(
            r"\frac{20}{24} < \frac{21}{24}",
            font_size=40, color=COLOR_HL
        ).move_to(DOWN * 1.2)
        self.play(Write(compare), run_time=0.6)

        result = Text(
            "所以 5/6 < 7/8", font=FONT, font_size=28, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.5)
        result_box = SurroundingRectangle(result, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(result, shift=UP * 0.2), Create(result_box), run_time=0.6)

        tip = Text(
            "同分母后，分子大的分数更大！", font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, q, s1, s2, s3, compare, result, result_box, tip
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------
    def scene_7_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.0)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "通分", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.2)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 通分：化异分母为同分母", font=FONT, font_size=20, color=WHITE),
            Text("2. 公分母 = 分母的最小公倍数", font=FONT, font_size=20, color=COLOR_COMMON),
            Text("3. 分子分母同乘相应倍数", font=FONT, font_size=20, color=COLOR_FRAC_A),
            Text("4. 依据：分数的基本性质", font=FONT, font_size=20, color=COLOR_STEP),
            Text("5. 应用：比较大小、加减运算", font=FONT, font_size=20, color=COLOR_FRAC_B),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 公式
        formula = MathTex(
            r"\frac{a}{b} \text{ , } \frac{c}{d} \longrightarrow "
            r"\frac{a \times d}{b \times d} \text{ , } \frac{c \times b}{d \times b}",
            font_size=28, color=COLOR_HL
        ).move_to(DOWN * 2.2)
        self.play(Write(formula), run_time=0.7)

        tip = Text(
            "通分是异分母运算的基础！",
            font=FONT, font_size=22, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(box, sum_title, items, formula, tip)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------
    def scene_8_outro(self):
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
#   快速预览:  manim -pql 006_通分.py CommonDenominatorLesson
#   高质量:    manim -qh  006_通分.py CommonDenominatorLesson
#   4K:        manim -qk  006_通分.py CommonDenominatorLesson
# ======================================================================

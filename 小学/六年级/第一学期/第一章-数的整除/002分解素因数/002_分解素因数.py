"""
002_分解素因数.py — 分解素因数 教学动画

知识点: 分解素因数 - 用短除法将合数分解为质数之积
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 素因数的定义：如果一个质数是某个数的因数，就叫做这个数的素因数
  2. 分解素因数：把一个合数写成几个质数相乘的形式
  3. 短除法：分解素因数的主要方法
  4. 示例：24 = 2 x 2 x 2 x 3 = 2^3 x 3
  5. 练习：分解 36, 60
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
COLOR_PRIME = "#3b82f6"       # 蓝色 - 质数/素因数
COLOR_COMPOSITE = "#ef4444"   # 红色 - 合数
COLOR_HL = "#fbbf24"          # 黄色 - 高亮
COLOR_STEP = "#a78bfa"        # 紫色 - 步骤
COLOR_RESULT = "#22c55e"      # 绿色 - 结果
COLOR_DIVIDER = "#f97316"     # 橙色 - 除号/短除线
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class PrimeFactorizationLesson(Scene):
    """
    分解素因数教学动画
    场景:
      1. 开场钩子
      2. 素因数的概念
      3. 分解素因数的定义
      4. 短除法演示 (24)
      5. 用指数形式表示
      6. 练习: 分解 36
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_prime_factor_concept()
        self.scene_3_definition()
        self.scene_4_short_division_24()
        self.scene_5_exponent_form()
        self.scene_6_practice_36()
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
            "分解素因数", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "每个合数的秘密密码！", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示 24 的分解预告
        preview = MathTex(
            r"24 = 2 \times 2 \times 2 \times 3",
            font_size=36, color=COLOR_RESULT
        ).move_to(UP * 2.5)
        self.play(Write(preview), run_time=0.8)
        self.wait(0.6)

        question = Text(
            "怎么做到的？", font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 1.2)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        self.play(
            FadeOut(VGroup(hook1, hook2, preview, question)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 素因数的概念
    # ------------------------------------------------------------------
    def scene_2_prime_factor_concept(self):
        title = Text(
            "什么是素因数？", font=FONT, font_size=38,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 先复习因数
        line1 = Text(
            "12 的因数：1, 2, 3, 4, 6, 12",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(line1), run_time=0.6)
        self.wait(0.3)

        # 标出质数因数
        line2 = Text(
            "其中哪些是质数？", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.5)
        self.play(FadeIn(line2), run_time=0.4)
        self.wait(0.3)

        primes_line = VGroup()
        primes_data = [("2", COLOR_PRIME), ("3", COLOR_PRIME)]
        for val, col in primes_data:
            num = Text(val, font=FONT, font_size=34, color=col, weight=BOLD)
            circle = Circle(radius=0.35, color=col, stroke_width=2).move_to(num)
            primes_line.add(VGroup(circle, num))
        primes_line.arrange(RIGHT, buff=1.0).move_to(UP * 1.3)
        self.play(FadeIn(primes_line, shift=UP * 0.2), run_time=0.5)

        # 定义
        defn_box = RoundedRectangle(
            width=7.5, height=2.0, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_PRIME, stroke_width=2
        ).move_to(DOWN * 0.5)
        defn_text = Text(
            "如果一个质数是某个数的因数，\n就叫做这个数的素因数",
            font=FONT, font_size=24, color=WHITE,
            line_spacing=1.5
        ).move_to(defn_box.get_center())
        self.play(FadeIn(defn_box), Write(defn_text), run_time=0.8)

        example = Text(
            "2 和 3 是 12 的素因数",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(example, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(title, line1, line2, primes_line, defn_box, defn_text, example)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 分解素因数的定义
    # ------------------------------------------------------------------
    def scene_3_definition(self):
        title = Text(
            "分解素因数", font=FONT, font_size=38,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        defn = Text(
            "把一个合数写成几个质数\n相乘的形式",
            font=FONT, font_size=28, color=WHITE,
            line_spacing=1.5
        ).move_to(UP * 3.5)
        self.play(Write(defn), run_time=0.7)

        # 简单示例
        ex1 = MathTex(
            r"6 = 2 \times 3", font_size=36, color=COLOR_RESULT
        ).move_to(UP * 1.5)
        ex2 = MathTex(
            r"15 = 3 \times 5", font_size=36, color=COLOR_RESULT
        ).move_to(UP * 0.5)
        ex3 = MathTex(
            r"24 = 2 \times 2 \times 2 \times 3", font_size=36, color=COLOR_RESULT
        ).move_to(DOWN * 0.5)

        self.play(Write(ex1), run_time=0.5)
        self.wait(0.3)
        self.play(Write(ex2), run_time=0.5)
        self.wait(0.3)
        self.play(Write(ex3), run_time=0.6)
        self.wait(0.5)

        method = Text(
            "方法：短除法", font=FONT, font_size=30,
            color=COLOR_DIVIDER, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(method, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(title, defn, ex1, ex2, ex3, method)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 短除法演示 (24)
    # ------------------------------------------------------------------
    def scene_4_short_division_24(self):
        title = Text(
            "短除法分解 24", font=FONT, font_size=38,
            color=COLOR_DIVIDER, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        hint = Text(
            "从最小的质数开始除", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(hint), run_time=0.3)

        # Build short division step by step
        # Layout:  divisor ) quotient
        #                    next_quotient
        # Position the short division centered around UP*1.5
        base_x = -0.5
        base_y = 3.0
        row_h = 1.0
        div_col_x = base_x - 1.5  # divisor column
        num_col_x = base_x + 0.5  # number column

        # We'll collect all created mobjects for cleanup
        div_elements = VGroup()

        # Step 1: 24 / 2 = 12
        num_24 = Text("24", font=FONT, font_size=34, color=WHITE, weight=BOLD
                       ).move_to(np.array([num_col_x, base_y, 0]))
        self.play(Write(num_24), run_time=0.4)
        div_elements.add(num_24)

        step_label_1 = Text(
            "24 是偶数，用 2 除", font=FONT, font_size=20, color=GRAY_A
        ).move_to(np.array([2.5, base_y, 0]))
        self.play(FadeIn(step_label_1), run_time=0.3)
        div_elements.add(step_label_1)

        div_2a = Text("2", font=FONT, font_size=34, color=COLOR_PRIME, weight=BOLD
                       ).move_to(np.array([div_col_x, base_y - row_h * 0.5, 0]))
        # L-shaped line for short division
        line_h1 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 0.5 + 0.3, 0]),
            np.array([div_col_x + 0.35, base_y - row_h * 0.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        line_v1 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 0.5 - 0.3, 0]),
            np.array([num_col_x + 0.6, base_y - row_h * 0.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        self.play(Write(div_2a), Create(line_h1), Create(line_v1), run_time=0.5)
        div_elements.add(div_2a, line_h1, line_v1)

        num_12 = Text("12", font=FONT, font_size=34, color=WHITE, weight=BOLD
                       ).move_to(np.array([num_col_x, base_y - row_h, 0]))
        self.play(Write(num_12), FadeOut(step_label_1), run_time=0.4)
        div_elements.add(num_12)
        self.wait(0.3)

        # Step 2: 12 / 2 = 6
        step_label_2 = Text(
            "12 还是偶数，继续用 2 除", font=FONT, font_size=20, color=GRAY_A
        ).move_to(np.array([2.5, base_y - row_h, 0]))
        self.play(FadeIn(step_label_2), run_time=0.3)
        div_elements.add(step_label_2)

        div_2b = Text("2", font=FONT, font_size=34, color=COLOR_PRIME, weight=BOLD
                       ).move_to(np.array([div_col_x, base_y - row_h * 1.5, 0]))
        line_h2 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 1.5 + 0.3, 0]),
            np.array([div_col_x + 0.35, base_y - row_h * 1.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        line_v2 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 1.5 - 0.3, 0]),
            np.array([num_col_x + 0.6, base_y - row_h * 1.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        self.play(Write(div_2b), Create(line_h2), Create(line_v2), run_time=0.5)
        div_elements.add(div_2b, line_h2, line_v2)

        num_6 = Text("6", font=FONT, font_size=34, color=WHITE, weight=BOLD
                      ).move_to(np.array([num_col_x, base_y - row_h * 2, 0]))
        self.play(Write(num_6), FadeOut(step_label_2), run_time=0.4)
        div_elements.add(num_6)
        self.wait(0.3)

        # Step 3: 6 / 2 = 3
        step_label_3 = Text(
            "6 还是偶数，再用 2 除", font=FONT, font_size=20, color=GRAY_A
        ).move_to(np.array([2.5, base_y - row_h * 2, 0]))
        self.play(FadeIn(step_label_3), run_time=0.3)
        div_elements.add(step_label_3)

        div_2c = Text("2", font=FONT, font_size=34, color=COLOR_PRIME, weight=BOLD
                       ).move_to(np.array([div_col_x, base_y - row_h * 2.5, 0]))
        line_h3 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 2.5 + 0.3, 0]),
            np.array([div_col_x + 0.35, base_y - row_h * 2.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        line_v3 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 2.5 - 0.3, 0]),
            np.array([num_col_x + 0.6, base_y - row_h * 2.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        self.play(Write(div_2c), Create(line_h3), Create(line_v3), run_time=0.5)
        div_elements.add(div_2c, line_h3, line_v3)

        num_3 = Text("3", font=FONT, font_size=34, color=COLOR_PRIME, weight=BOLD
                      ).move_to(np.array([num_col_x, base_y - row_h * 3, 0]))
        self.play(Write(num_3), FadeOut(step_label_3), run_time=0.4)
        div_elements.add(num_3)

        # Step 4: 3 is prime, stop
        stop_label = Text(
            "3 是质数，停止！", font=FONT, font_size=22, color=COLOR_HL, weight=BOLD
        ).move_to(np.array([2.5, base_y - row_h * 3, 0]))
        self.play(FadeIn(stop_label, shift=LEFT * 0.2), run_time=0.5)
        div_elements.add(stop_label)
        self.wait(0.8)

        # Show result: collect all divisors and last quotient
        result_text = Text(
            "把所有除数和最后的商乘起来：", font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(result_text), run_time=0.4)
        div_elements.add(result_text)

        result_formula = MathTex(
            r"24 = 2 \times 2 \times 2 \times 3",
            font_size=38, color=COLOR_RESULT
        ).move_to(DOWN * 3.2)
        box = SurroundingRectangle(
            result_formula, color=COLOR_RESULT, buff=0.2, corner_radius=0.1
        )
        self.play(Write(result_formula), Create(box), run_time=0.8)
        div_elements.add(result_formula, box)
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, hint, div_elements)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 5: 用指数形式表示
    # ------------------------------------------------------------------
    def scene_5_exponent_form(self):
        title = Text(
            "用指数形式表示", font=FONT, font_size=38,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # Original form
        original = MathTex(
            r"24 = 2 \times 2 \times 2 \times 3",
            font_size=36, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(original), run_time=0.6)
        self.wait(0.5)

        # Highlight the three 2s
        hint = Text(
            "3 个 2 相乘", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 2.5)
        arrow_text = MathTex(
            r"\underbrace{2 \times 2 \times 2}_{3} = 2^3",
            font_size=34, color=COLOR_PRIME
        ).move_to(UP * 1.3)
        self.play(FadeIn(hint), run_time=0.3)
        self.play(Write(arrow_text), run_time=0.7)
        self.wait(0.5)

        # Final compact form
        therefore = Text(
            "所以：", font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 0.2 + LEFT * 2.0)
        compact = MathTex(
            r"24 = 2^3 \times 3",
            font_size=44, color=COLOR_RESULT
        ).move_to(DOWN * 0.2 + RIGHT * 1.0)
        self.play(FadeIn(therefore), Write(compact), run_time=0.7)

        box = SurroundingRectangle(
            compact, color=COLOR_HL, buff=0.2, corner_radius=0.1
        )
        self.play(Create(box), run_time=0.4)

        note = Text(
            "指数形式更简洁！", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(title, original, hint, arrow_text, therefore, compact, box, note)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 6: 练习 - 分解 36
    # ------------------------------------------------------------------
    def scene_6_practice_36(self):
        title = Text(
            "练一练：分解 36", font=FONT, font_size=38,
            color=COLOR_DIVIDER, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        practice_elements = VGroup()

        base_x = -0.5
        base_y = 3.5
        row_h = 0.9
        div_col_x = base_x - 1.5
        num_col_x = base_x + 0.5

        # 36
        num_36 = Text("36", font=FONT, font_size=32, color=WHITE, weight=BOLD
                       ).move_to(np.array([num_col_x, base_y, 0]))
        self.play(Write(num_36), run_time=0.4)
        practice_elements.add(num_36)

        # 36 / 2 = 18
        div_2a = Text("2", font=FONT, font_size=32, color=COLOR_PRIME, weight=BOLD
                       ).move_to(np.array([div_col_x, base_y - row_h * 0.5, 0]))
        lh1 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 0.5 + 0.3, 0]),
            np.array([div_col_x + 0.35, base_y - row_h * 0.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        lv1 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 0.5 - 0.3, 0]),
            np.array([num_col_x + 0.6, base_y - row_h * 0.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        self.play(Write(div_2a), Create(lh1), Create(lv1), run_time=0.4)
        practice_elements.add(div_2a, lh1, lv1)

        num_18 = Text("18", font=FONT, font_size=32, color=WHITE, weight=BOLD
                       ).move_to(np.array([num_col_x, base_y - row_h, 0]))
        self.play(Write(num_18), run_time=0.3)
        practice_elements.add(num_18)

        # 18 / 2 = 9
        div_2b = Text("2", font=FONT, font_size=32, color=COLOR_PRIME, weight=BOLD
                       ).move_to(np.array([div_col_x, base_y - row_h * 1.5, 0]))
        lh2 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 1.5 + 0.3, 0]),
            np.array([div_col_x + 0.35, base_y - row_h * 1.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        lv2 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 1.5 - 0.3, 0]),
            np.array([num_col_x + 0.6, base_y - row_h * 1.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        self.play(Write(div_2b), Create(lh2), Create(lv2), run_time=0.4)
        practice_elements.add(div_2b, lh2, lv2)

        num_9 = Text("9", font=FONT, font_size=32, color=WHITE, weight=BOLD
                      ).move_to(np.array([num_col_x, base_y - row_h * 2, 0]))
        self.play(Write(num_9), run_time=0.3)
        practice_elements.add(num_9)

        # 9 / 3 = 3
        note_9 = Text(
            "9 不能被 2 整除，试 3", font=FONT, font_size=18, color=GRAY_A
        ).move_to(np.array([2.8, base_y - row_h * 2, 0]))
        self.play(FadeIn(note_9), run_time=0.3)
        practice_elements.add(note_9)

        div_3a = Text("3", font=FONT, font_size=32, color=COLOR_PRIME, weight=BOLD
                       ).move_to(np.array([div_col_x, base_y - row_h * 2.5, 0]))
        lh3 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 2.5 + 0.3, 0]),
            np.array([div_col_x + 0.35, base_y - row_h * 2.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        lv3 = Line(
            np.array([div_col_x + 0.35, base_y - row_h * 2.5 - 0.3, 0]),
            np.array([num_col_x + 0.6, base_y - row_h * 2.5 - 0.3, 0]),
            color=COLOR_DIVIDER, stroke_width=3
        )
        self.play(Write(div_3a), Create(lh3), Create(lv3), FadeOut(note_9), run_time=0.4)
        practice_elements.add(div_3a, lh3, lv3)

        num_3 = Text("3", font=FONT, font_size=32, color=COLOR_PRIME, weight=BOLD
                      ).move_to(np.array([num_col_x, base_y - row_h * 3, 0]))
        self.play(Write(num_3), run_time=0.3)
        practice_elements.add(num_3)

        stop_36 = Text(
            "3 是质数，停止！", font=FONT, font_size=20, color=COLOR_HL, weight=BOLD
        ).move_to(np.array([2.5, base_y - row_h * 3, 0]))
        self.play(FadeIn(stop_36), run_time=0.3)
        practice_elements.add(stop_36)
        self.wait(0.5)

        # Result
        result_36 = MathTex(
            r"36 = 2 \times 2 \times 3 \times 3",
            font_size=34, color=COLOR_RESULT
        ).move_to(DOWN * 1.5)
        self.play(Write(result_36), run_time=0.6)
        practice_elements.add(result_36)

        result_36_exp = MathTex(
            r"36 = 2^2 \times 3^2",
            font_size=40, color=COLOR_RESULT
        ).move_to(DOWN * 2.8)
        box = SurroundingRectangle(
            result_36_exp, color=COLOR_HL, buff=0.2, corner_radius=0.1
        )
        self.play(Write(result_36_exp), Create(box), run_time=0.6)
        practice_elements.add(result_36_exp, box)
        self.wait(2.0)
        self.play(FadeOut(VGroup(title, practice_elements)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------
    def scene_7_summary(self):
        box = RoundedRectangle(
            width=8.0, height=8.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "分解素因数", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.0)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 素因数：是因数，又是质数", font=FONT, font_size=22, color=COLOR_PRIME),
            Text("2. 把合数写成质数相乘的形式", font=FONT, font_size=22, color=WHITE),
            Text("3. 方法：短除法", font=FONT, font_size=22, color=COLOR_DIVIDER),
            Text("4. 从最小的质数 2 开始除", font=FONT, font_size=22, color=WHITE),
            Text("5. 除到商是质数为止", font=FONT, font_size=22, color=WHITE),
            Text("6. 用指数形式简化书写", font=FONT, font_size=22, color=COLOR_RESULT),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(UP * 0.8)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.35)
            self.wait(0.15)

        example_box = RoundedRectangle(
            width=6.5, height=1.4, corner_radius=0.15,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_RESULT, stroke_width=2
        ).move_to(DOWN * 2.5)
        ex_formula = MathTex(
            r"24 = 2^3 \times 3",
            font_size=38, color=COLOR_RESULT
        ).move_to(example_box.get_center())
        self.play(FadeIn(example_box), Write(ex_formula), run_time=0.5)

        tip = Text(
            "分解素因数是求最大公因数\n和最小公倍数的基础！",
            font=FONT, font_size=22, color=COLOR_HL,
            line_spacing=1.4
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)
        self.play(
            FadeOut(VGroup(box, sum_title, items, example_box, ex_formula, tip)),
            run_time=0.5
        )

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
#   快速预览:  manim -pql 002_分解素因数.py PrimeFactorizationLesson
#   中等质量:  manim -qm  002_分解素因数.py PrimeFactorizationLesson
#   高质量:    manim -qh  002_分解素因数.py PrimeFactorizationLesson
# ======================================================================

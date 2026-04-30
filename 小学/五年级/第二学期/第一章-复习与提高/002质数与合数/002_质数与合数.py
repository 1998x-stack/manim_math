"""
002_质数与合数.py — 质数与合数 教学动画

知识点: 质数与合数的定义、判断方法
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 质数: 只有1和它本身两个因数
  2. 合数: 除了1和它本身还有别的因数(至少3个因数)
  3. 1既不是质数也不是合数
  4. 最小质数是2(唯一的偶数质数)
  5. 20以内的质数: 2, 3, 5, 7, 11, 13, 17, 19
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
COLOR_PRIME = "#3b82f6"
COLOR_COMPOSITE = "#ef4444"
COLOR_ONE = "#6b7280"
COLOR_HL = "#fbbf24"
COLOR_FACTOR = "#22c55e"
COLOR_STEP = "#a78bfa"
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class PrimeCompositeLesson(Scene):
    """
    质数与合数教学动画
    场景:
      1. 开场钩子
      2. 因数个数引入
      3. 质数的定义
      4. 合数的定义
      5. 1的特殊性
      6. 20以内质数表
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_factor_count()
        self.scene_3_prime_definition()
        self.scene_4_composite_definition()
        self.scene_5_one_is_special()
        self.scene_6_prime_table()
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
            "质数与合数", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "数字的两大家族！", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 因数个数引入
    # ------------------------------------------------------------------
    def scene_2_factor_count(self):
        title = Text(
            "先看因数个数", font=FONT, font_size=38,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        examples = [
            (2, [1, 2], "2个因数"),
            (6, [1, 2, 3, 6], "4个因数"),
            (7, [1, 7], "2个因数"),
            (12, [1, 2, 3, 4, 6, 12], "6个因数"),
        ]

        all_rows = VGroup()
        for num, factors, count_str in examples:
            num_text = Text(
                str(num), font=FONT, font_size=32, color=COLOR_HL, weight=BOLD
            )
            arrow = MathTex(r"\rightarrow", font_size=28, color=GRAY_A)
            factors_str = ", ".join(str(f) for f in factors)
            factors_text = Text(
                factors_str, font=FONT, font_size=22, color=COLOR_FACTOR
            )
            count_text = Text(
                count_str, font=FONT, font_size=20, color=GRAY_A
            )
            row = VGroup(num_text, arrow, factors_text, count_text).arrange(
                RIGHT, buff=0.2
            )
            all_rows.add(row)

        all_rows.arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 1.5)

        for row in all_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        question = Text(
            "因数个数不同，分类！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, all_rows, question)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 质数的定义
    # ------------------------------------------------------------------
    def scene_3_prime_definition(self):
        title = Text(
            "质数（素数）", font=FONT, font_size=38,
            color=COLOR_PRIME, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        defn = Text(
            "只有1和它本身两个因数",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.8)
        self.play(Write(defn), run_time=0.6)

        examples_title = Text(
            "例如：", font=FONT, font_size=24, color=COLOR_PRIME
        ).move_to(UP * 2.5 + LEFT * 3.0)
        self.play(Write(examples_title), run_time=0.3)

        prime_examples = [
            ("2", "因数：1, 2"),
            ("3", "因数：1, 3"),
            ("5", "因数：1, 5"),
            ("7", "因数：1, 7"),
        ]

        rows = VGroup()
        for num_str, factors_str in prime_examples:
            num_t = Text(
                num_str, font=FONT, font_size=30, color=COLOR_PRIME, weight=BOLD
            )
            circle = Circle(radius=0.35, color=COLOR_PRIME, stroke_width=2).move_to(num_t)
            num_g = VGroup(circle, num_t)
            arrow = MathTex(r"\rightarrow", font_size=24, color=GRAY_A)
            fac_t = Text(factors_str, font=FONT, font_size=20, color=WHITE)
            row = VGroup(num_g, arrow, fac_t).arrange(RIGHT, buff=0.3)
            rows.add(row)

        rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 0.5)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)

        key = Text(
            "最小的质数是 2",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.0)
        key2 = Text(
            "2 是唯一的偶数质数！",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(key2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(title, defn, examples_title, rows, key, key2)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 合数的定义
    # ------------------------------------------------------------------
    def scene_4_composite_definition(self):
        title = Text(
            "合数", font=FONT, font_size=38,
            color=COLOR_COMPOSITE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        defn = Text(
            "除了1和它本身还有别的因数",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.8)
        defn2 = Text(
            "（至少有3个因数）",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 3.1)
        self.play(Write(defn), run_time=0.6)
        self.play(FadeIn(defn2), run_time=0.3)

        examples_title = Text(
            "例如：", font=FONT, font_size=24, color=COLOR_COMPOSITE
        ).move_to(UP * 2.0 + LEFT * 3.0)
        self.play(Write(examples_title), run_time=0.3)

        comp_examples = [
            ("4", "因数：1, 2, 4", "3个"),
            ("6", "因数：1, 2, 3, 6", "4个"),
            ("9", "因数：1, 3, 9", "3个"),
            ("12", "因数：1, 2, 3, 4, 6, 12", "6个"),
        ]

        rows = VGroup()
        for num_str, factors_str, count_str in comp_examples:
            num_t = Text(
                num_str, font=FONT, font_size=30, color=COLOR_COMPOSITE, weight=BOLD
            )
            rect = RoundedRectangle(
                width=0.7, height=0.7, corner_radius=0.1,
                color=COLOR_COMPOSITE, stroke_width=2
            ).move_to(num_t)
            num_g = VGroup(rect, num_t)
            arrow = MathTex(r"\rightarrow", font_size=24, color=GRAY_A)
            fac_t = Text(factors_str, font=FONT, font_size=18, color=WHITE)
            cnt_t = Text(count_str, font=FONT, font_size=18, color=COLOR_COMPOSITE)
            row = VGroup(num_g, arrow, fac_t, cnt_t).arrange(RIGHT, buff=0.2)
            rows.add(row)

        rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 0.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.2)

        key = Text(
            "最小的合数是 4",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(title, defn, defn2, examples_title, rows, key)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 1的特殊性
    # ------------------------------------------------------------------
    def scene_5_one_is_special(self):
        title = Text(
            "1 是什么？", font=FONT, font_size=38,
            color=COLOR_ONE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        big_one = Text(
            "1", font=FONT, font_size=120, color=COLOR_ONE, weight=BOLD
        ).move_to(UP * 2.5)
        self.play(Write(big_one), run_time=0.6)

        factor_text = Text(
            "1 的因数：只有 1", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 0.5)
        self.play(Write(factor_text), run_time=0.5)

        count_text = Text(
            "只有 1 个因数！", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 0.3)
        self.play(Write(count_text), run_time=0.5)

        not_prime = Text(
            "不是质数", font=FONT, font_size=28, color=COLOR_PRIME
        ).move_to(DOWN * 1.8 + LEFT * 2.0)
        cross1 = MathTex(r"\times", font_size=48, color=COLOR_COMPOSITE).next_to(not_prime, LEFT, buff=0.2)
        self.play(FadeIn(VGroup(not_prime, cross1), shift=RIGHT * 0.2), run_time=0.5)

        not_comp = Text(
            "不是合数", font=FONT, font_size=28, color=COLOR_COMPOSITE
        ).move_to(DOWN * 1.8 + RIGHT * 2.0)
        cross2 = MathTex(r"\times", font_size=48, color=COLOR_COMPOSITE).next_to(not_comp, LEFT, buff=0.2)
        self.play(FadeIn(VGroup(not_comp, cross2), shift=LEFT * 0.2), run_time=0.5)

        conclusion = Text(
            "1 既不是质数，也不是合数！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.5)
        box = SurroundingRectangle(conclusion, color=COLOR_HL, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(conclusion, shift=UP * 0.2), Create(box), run_time=0.6)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(
                title, big_one, factor_text, count_text,
                not_prime, cross1, not_comp, cross2, conclusion, box
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 6: 20以内质数表
    # ------------------------------------------------------------------
    def scene_6_prime_table(self):
        title = Text(
            "20以内的质数", font=FONT, font_size=38,
            color=COLOR_PRIME, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        hint = Text(
            "用圆圈标出质数", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(hint), run_time=0.3)

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        grid = VGroup()
        num_mobs = {}

        for i in range(20):
            num = i + 1
            row = i // 5
            col = i % 5
            x = (col - 2) * 1.5
            y = (1.5 - row) * 1.2 + 1.0
            num_text = Text(
                str(num), font=FONT, font_size=28, color=WHITE
            ).move_to(np.array([x, y, 0]))
            num_mobs[num] = num_text
            grid.add(num_text)

        self.play(FadeIn(grid), run_time=0.6)
        self.wait(0.3)

        self.play(num_mobs[1].animate.set_color(COLOR_ONE), run_time=0.3)

        circles = VGroup()
        for p in sorted(primes):
            circle = Circle(
                radius=0.4, color=COLOR_PRIME, stroke_width=3
            ).move_to(num_mobs[p])
            circles.add(circle)
            self.play(
                Create(circle),
                num_mobs[p].animate.set_color(COLOR_PRIME),
                run_time=0.3
            )

        composites = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20}
        comp_anims = []
        for c in sorted(composites):
            comp_anims.append(num_mobs[c].animate.set_color(COLOR_COMPOSITE))
        self.play(*comp_anims, run_time=0.5)

        prime_list = Text(
            "2, 3, 5, 7, 11, 13, 17, 19",
            font=FONT, font_size=24, color=COLOR_PRIME, weight=BOLD
        ).move_to(DOWN * 2.5)
        count_text = Text(
            "共 8 个质数", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(prime_list, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(count_text, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)
        self.play(
            FadeOut(VGroup(title, hint, grid, circles, prime_list, count_text)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------
    def scene_7_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.3)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "质数与合数", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.2)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 质数：只有1和本身两个因数", font=FONT, font_size=22, color=COLOR_PRIME),
            Text("2. 合数：至少有3个因数", font=FONT, font_size=22, color=COLOR_COMPOSITE),
            Text("3. 1 既不是质数也不是合数", font=FONT, font_size=22, color=COLOR_ONE),
            Text("4. 最小质数是2，最小合数是4", font=FONT, font_size=22, color=WHITE),
            Text("5. 2 是唯一的偶数质数", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text(
            "记住：20以内共8个质数！",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

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
#   快速预览:  manim -pql 002_质数与合数.py PrimeCompositeLesson
#   高质量:    manim -qh  002_质数与合数.py PrimeCompositeLesson
#   4K:        manim -qk  002_质数与合数.py PrimeCompositeLesson
# ======================================================================

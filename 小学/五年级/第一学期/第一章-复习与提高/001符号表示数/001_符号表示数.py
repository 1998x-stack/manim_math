"""
001_符号表示数.py — 符号表示数 教学动画

知识点: 用图形符号和字母代表数，从算术到代数的过渡
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 图形代表数: □ + 5 = 10 → □ = 5
  2. 字母代表运算律: a + b = b + a (加法交换律)
  3. 字母代表公式: S = a × b (长方形面积)
  4. 字母代表未知数: x + 3 = 8 → x = 5
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
COLOR_SYMBOL = "#3b82f6"     # 蓝色符号
COLOR_NUMBER = "#22c55e"     # 绿色数字
COLOR_LETTER = "#f59e0b"     # 橙色字母
COLOR_FORMULA = "#8b5cf6"    # 紫色公式
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class SymbolRepresentNumberLesson(Scene):
    """
    符号表示数教学动画
    场景:
      1. 开场钩子
      2. 图形代表数 (□ + 5 = 10)
      3. 字母表示运算律 (a + b = b + a)
      4. 字母表示公式 (S = a × b)
      5. 总结: 从算术到代数
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_symbol_as_number()
        self.scene_3_letter_as_law()
        self.scene_4_letter_as_formula()
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
            "数学里不只有数字", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "符号也能表示数！", font=FONT, font_size=48, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示各种符号
        symbols = VGroup(
            MathTex(r"\square", font_size=60, color=COLOR_SYMBOL),
            MathTex(r"\triangle", font_size=60, color="#ef4444"),
            MathTex(r"\circ", font_size=60, color=COLOR_LETTER),
            MathTex(r"a", font_size=60, color=COLOR_NUMBER),
            MathTex(r"x", font_size=60, color=COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.8).move_to(UP * 1.0)

        self.play(*[FadeIn(s, scale=0.3) for s in symbols], run_time=0.8)
        self.play(
            *[Indicate(s, scale_factor=1.2) for s in symbols],
            run_time=0.6
        )
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, symbols)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 图形代表数
    # ------------------------------------------------------------------

    def scene_2_symbol_as_number(self):
        title = Text(
            "图形代表数", font=FONT, font_size=38,
            color=COLOR_SYMBOL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # □ + 5 = 10
        eq_box = MathTex(r"\square", font_size=48, color=COLOR_SYMBOL)
        eq_plus = MathTex(r"+ 5 = 10", font_size=44, color=WHITE)
        eq1 = VGroup(eq_box, eq_plus).arrange(RIGHT, buff=0.15).move_to(UP * 2.5)

        self.play(Write(eq1), run_time=0.8)
        self.wait(0.5)

        # 思考过程
        think = Text(
            "什么数加 5 等于 10？", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 1.2)
        self.play(Write(think), run_time=0.6)
        self.wait(0.5)

        # 答案
        ans_box = MathTex(r"\square", font_size=48, color=COLOR_SYMBOL)
        ans_eq = MathTex(r"= 5", font_size=44, color=COLOR_NUMBER)
        ans = VGroup(ans_box, ans_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.2)

        self.play(FadeIn(ans, shift=UP * 0.3), run_time=0.6)

        # 高亮: □ 变成 5
        five = MathTex(r"5", font_size=48, color=COLOR_NUMBER).move_to(eq_box.get_center())
        self.play(Transform(eq_box, five), run_time=0.8)
        self.wait(0.5)

        # 说明
        desc = Text(
            "符号□代表一个特定的数",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(VGroup(title, eq1, eq_plus, think, ans, desc)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 字母表示运算律
    # ------------------------------------------------------------------

    def scene_3_letter_as_law(self):
        title = Text(
            "字母表示运算律", font=FONT, font_size=36,
            color=COLOR_LETTER, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 具体例子
        step1 = Text(
            "加法交换律", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(step1), run_time=0.5)

        # 具体数字
        ex1 = MathTex(r"3 + 5 = 5 + 3", font_size=36, color=GRAY_A)
        ex2 = MathTex(r"12 + 7 = 7 + 12", font_size=36, color=GRAY_A)
        ex3 = MathTex(r"100 + 25 = 25 + 100", font_size=36, color=GRAY_A)
        examples = VGroup(ex1, ex2, ex3).arrange(DOWN, buff=0.4).move_to(UP * 1.5)

        self.play(Write(ex1), run_time=0.5)
        self.play(Write(ex2), run_time=0.5)
        self.play(Write(ex3), run_time=0.5)
        self.wait(0.5)

        # 规律
        pattern = Text(
            "有无数个例子……能一句话说清吗？",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.5)
        self.play(Write(pattern), run_time=0.6)
        self.wait(0.5)

        # 字母公式
        formula = MathTex(r"a + b = b + a", font_size=52, color=COLOR_HL)
        formula.move_to(DOWN * 2.0)
        self.play(
            FadeOut(examples),
            FadeOut(pattern),
            FadeIn(formula, scale=0.6),
            run_time=0.8
        )

        desc = Text(
            "一个公式概括所有情况！",
            font=FONT, font_size=26, color=COLOR_LETTER
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.5)

        self.play(Indicate(formula, scale_factor=1.1, color=COLOR_HL), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, step1, formula, desc)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 字母表示公式
    # ------------------------------------------------------------------

    def scene_4_letter_as_formula(self):
        title = Text(
            "字母表示公式", font=FONT, font_size=36,
            color=COLOR_FORMULA, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 长方形
        rect = Rectangle(
            width=3.5, height=2.0,
            color=COLOR_FORMULA, fill_color=COLOR_FORMULA,
            fill_opacity=0.3, stroke_width=3
        ).move_to(UP * 2.0)

        # 标注
        a_label = MathTex(r"a", font_size=32, color=COLOR_LETTER)
        a_label.move_to(rect.get_bottom() + DOWN * 0.4)
        b_label = MathTex(r"b", font_size=32, color=COLOR_LETTER)
        b_label.move_to(rect.get_right() + RIGHT * 0.4)

        self.play(Create(rect), run_time=0.8)
        self.play(FadeIn(a_label), FadeIn(b_label), run_time=0.4)
        self.wait(0.3)

        # 面积公式
        f_lhs = Text("面积 ", font=FONT, font_size=28, color=WHITE)
        f_S = MathTex(r"S", font_size=36, color=COLOR_FORMULA)
        f_eq = MathTex(r"=", font_size=36, color=WHITE)
        f_rhs = MathTex(r"a \times b", font_size=36, color=COLOR_HL)
        formula = VGroup(f_lhs, f_S, f_eq, f_rhs).arrange(RIGHT, buff=0.1)
        formula.move_to(DOWN * 0.5)

        self.play(Write(formula), run_time=0.8)
        self.wait(0.5)

        # 具体例子
        ex_text = Text(
            "当 a=4, b=3 时", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 2.0)
        ex_calc = MathTex(r"S = 4 \times 3 = 12", font_size=32, color=COLOR_NUMBER)
        ex_calc.move_to(DOWN * 2.8)

        self.play(Write(ex_text), run_time=0.5)
        self.play(Write(ex_calc), run_time=0.6)
        self.wait(1.0)

        # 强调
        desc = Text(
            "字母让公式简洁又通用",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(title, rect, a_label, b_label, formula, ex_text, ex_calc, desc)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=5.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "符号表示数", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.6)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            VGroup(
                MathTex(r"\square", font_size=28, color=COLOR_SYMBOL),
                Text(" 图形代表特定的数", font=FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"a, b", font_size=28, color=COLOR_LETTER),
                Text(" 字母表示运算律", font=FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"S = a \times b", font_size=28, color=COLOR_FORMULA),
                Text(" 字母表示公式", font=FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        arrow_text = Text(
            "从算术 → 代数的第一步！",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(arrow_text, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, arrow_text)), run_time=0.5)

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
#   快速预览:  manim -pql 001_符号表示数.py SymbolRepresentNumberLesson
#   高质量:    manim -qh  001_符号表示数.py SymbolRepresentNumberLesson
#   4K:        manim -qk  001_符号表示数.py SymbolRepresentNumberLesson
# ======================================================================

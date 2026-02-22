"""
分式的通分 - 七年级数学教学动画
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
    manim -pql fenshi_tongfen.py FenshiTongfen   # 快速预览
    manim -qh  fenshi_tongfen.py FenshiTongfen   # 高质量
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════════════
#  全局配置
# ══════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ══════════════════════════════════════════════════
#  调色板
# ══════════════════════════════════════════════════
BG_COLOR    = "#1a1a2e"
C_PRIMARY   = "#4fc3f7"   # 浅蓝
C_LCD       = "#f9a825"   # 金黄   最简公分母
C_NUMER     = "#ce93d8"   # 紫色   补充因式
C_RESULT    = "#66bb6a"   # 绿色   结果
C_HIGHLIGHT = "#fff176"   # 亮黄
C_DENOM_A   = "#4fc3f7"   # 浅蓝   分母A
C_DENOM_B   = "#f48fb1"   # 粉红   分母B
C_CARD_BG   = "#16213e"   # 深蓝
C_SUBTITLE  = "#b0bec5"   # 灰白
C_WRONG     = "#ef5350"   # 错误红
C_STEP      = "#ce93d8"   # 紫色   步骤标签

# ══════════════════════════════════════════════════
#  字号
# ══════════════════════════════════════════════════
FONT    = "Noto Sans CJK SC"
FS_BIG  = 52
FS_TTL  = 38
FS_SUB  = 28
FS_BODY = 24
FS_SM   = 20
FS_XS   = 17
FS_FORM = 36
FS_AUTH = 20


class FenshiTongfen(Scene):
    """
    分式的通分教学动画
    Scene 1 : 开场钩子                       (0–6s)
    Scene 2 : 通分定义 + 最简公分母概念      (6–14s)
    Scene 3 : 核心例题 1/x + 1/(x+1)        (14–32s)
    Scene 4 : 进阶例题 1/(x²-1)+1/(x+1)     (32–47s)
    Scene 5 : 三步走总结 + 口诀              (47–56s)
    Scene 6 : 片尾                           (56–63s)
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author_bar = self._make_author_bar()
        self.add(self.author_bar)

        self.scene_1_hook()
        self.scene_2_definition()
        self.scene_3_example1()
        self.scene_4_example2()
        self.scene_5_summary()
        self.scene_6_outro()

    # ══════════════════════════════════════════
    #  SCENE 1 — 开场钩子
    # ══════════════════════════════════════════
    def scene_1_hook(self):
        hook_q = Text(
            "分式加减，分母不同怎么办？",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE,
        ).move_to(UP * 5.5)
        self.play(FadeIn(hook_q, shift=DOWN * 0.3), run_time=0.5)

        # 展示 1/x + 1/(x+1)
        lhs  = MathTex(r"\dfrac{1}{x}", font_size=62, color=C_DENOM_A)
        plus = Text("+", font=FONT, font_size=FS_TTL, color=WHITE)
        rhs  = MathTex(r"\dfrac{1}{x+1}", font_size=62, color=C_DENOM_B)
        expr = VGroup(lhs, plus, rhs).arrange(RIGHT, buff=0.5).move_to(UP * 4.1)
        self.play(Write(lhs), FadeIn(plus), Write(rhs), run_time=0.6)
        self.wait(0.2)

        # ❌ 错误做法：直接合并
        wrong_label = Text("错误做法：", font=FONT, font_size=FS_SM, color=C_WRONG).move_to(UP * 2.8 + LEFT * 2.5)
        wrong_expr  = MathTex(
            r"\dfrac{1+1}{x+(x+1)}",
            font_size=48, color=C_WRONG,
        ).move_to(UP * 2.8 + RIGHT * 0.8)
        cross = Text("✗", font=FONT, font_size=FS_TTL, color=C_WRONG).next_to(wrong_expr, RIGHT, buff=0.25)

        self.play(FadeIn(wrong_label), Write(wrong_expr), run_time=0.5)
        self.play(FadeIn(cross, scale=0.3), run_time=0.3)
        self.wait(0.2)

        # 引导语
        bridge = Text(
            "通分，让分母变一样！",
            font=FONT, font_size=FS_BODY + 2, color=C_PRIMARY,
        ).move_to(UP * 1.5)
        self.play(FadeIn(bridge, shift=UP * 0.2), run_time=0.5)
        self.wait(0.2)

        # 主标题
        main_title = Text(
            "分式的通分",
            font=FONT, font_size=FS_BIG, color=C_LCD, weight=BOLD,
        ).move_to(UP * 0.3)
        self.play(Write(main_title), run_time=0.6)
        self.wait(0.4)

        # 缩小移顶
        self.play(
            FadeOut(VGroup(hook_q, expr, wrong_label, wrong_expr, cross, bridge)),
            main_title.animate.scale(0.5).move_to(UP * 6.0).set_color(C_SUBTITLE),
            run_time=0.5,
        )
        self.small_title = main_title

    # ══════════════════════════════════════════
    #  SCENE 2 — 通分定义
    # ══════════════════════════════════════════
    def scene_2_definition(self):
        sec = self._section_title("① 通分的定义", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        # 分数类比：1/2 + 1/3
        analog_label = Text(
            "先看分数通分：",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(UP * 5.6)
        self.play(FadeIn(analog_label), run_time=0.3)

        # 原式
        a_lhs  = MathTex(r"\dfrac{1}{2}", font_size=52, color=WHITE)
        a_plus = Text("+", font=FONT, font_size=FS_FORM, color=WHITE)
        a_rhs  = MathTex(r"\dfrac{1}{3}", font_size=52, color=WHITE)
        a_row  = VGroup(a_lhs, a_plus, a_rhs).arrange(RIGHT, buff=0.4).move_to(UP * 4.8)
        self.play(Write(a_row), run_time=0.5)

        # 箭头
        a_arrow = Arrow(UP * 4.0, UP * 3.2, color=C_LCD, buff=0,
                        stroke_width=5, max_tip_length_to_length_ratio=0.2)
        lcd_note = Text("公分母 = 6", font=FONT, font_size=FS_SM, color=C_LCD).next_to(a_arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(a_arrow), FadeIn(lcd_note), run_time=0.4)

        # 通分结果
        a_res_l = MathTex(r"\dfrac{3}{6}", font_size=52, color=C_RESULT)
        a_res_p = Text("+", font=FONT, font_size=FS_FORM, color=WHITE)
        a_res_r = MathTex(r"\dfrac{2}{6}", font_size=52, color=C_RESULT)
        a_res   = VGroup(a_res_l, a_res_p, a_res_r).arrange(RIGHT, buff=0.4).move_to(UP * 2.8)
        self.play(Write(a_res), run_time=0.5)
        self.wait(0.3)

        # 定义框
        defn_text = Text(
            "把异分母分式化为同分母分式",
            font=FONT, font_size=FS_BODY, color=WHITE,
        ).move_to(UP * 1.6)
        defn_bg = RoundedRectangle(
            width=defn_text.width + 0.9, height=0.88,
            corner_radius=0.2, fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=C_LCD, stroke_width=2.5,
        ).move_to(defn_text.get_center())
        self.play(FadeIn(defn_bg), Write(defn_text), run_time=0.5)
        self.wait(0.2)

        # 最简公分母说明框
        lcd_title = Text("最简公分母（LCD）：", font=FONT, font_size=FS_SM, color=C_LCD)
        lcd_body  = Text(
            "各分母因式分解后，所有因式最高次幂之积",
            font=FONT, font_size=FS_XS, color=C_SUBTITLE,
        )
        lcd_content = VGroup(lcd_title, lcd_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        lcd_bg = RoundedRectangle(
            width=7.5, height=lcd_content.height + 0.6,
            corner_radius=0.2, fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=C_LCD, stroke_width=2,
        )
        lcd_group = VGroup(lcd_bg, lcd_content)
        lcd_content.move_to(lcd_bg.get_center())
        lcd_group.move_to(UP * 0.2)
        self.play(FadeIn(lcd_group), run_time=0.5)
        self.wait(1.2)

        all_s2 = VGroup(sec, analog_label, a_row, a_arrow, lcd_note, a_res,
                        defn_bg, defn_text, lcd_group)
        self.play(FadeOut(all_s2), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 3 — 核心例题：1/x + 1/(x+1)
    # ══════════════════════════════════════════
    def scene_3_example1(self):
        sec = self._section_title("② 例题精讲", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        # ── 原式 ──
        orig_l  = MathTex(r"\dfrac{1}{x}", font_size=64, color=C_DENOM_A)
        orig_p  = Text("+", font=FONT, font_size=FS_TTL, color=WHITE)
        orig_r  = MathTex(r"\dfrac{1}{x+1}", font_size=64, color=C_DENOM_B)
        orig    = VGroup(orig_l, orig_p, orig_r).arrange(RIGHT, buff=0.5).move_to(UP * 5.5)
        self.play(Write(orig), run_time=0.6)
        self.wait(0.2)

        # ── Step 1 ──
        s1 = self._step_tag("Step 1", "分母已最简，无需分解", UP * 4.5)
        self.play(FadeIn(s1, shift=RIGHT * 0.3), run_time=0.4)

        # 分母 A、B 框
        da_box   = SurroundingRectangle(orig_l[0][2:], color=C_DENOM_A, buff=0.1, stroke_width=2.5, corner_radius=0.1)
        db_box   = SurroundingRectangle(orig_r[0][2:], color=C_DENOM_B, buff=0.1, stroke_width=2.5, corner_radius=0.1)
        da_label = Text("分母 A", font=FONT, font_size=FS_XS, color=C_DENOM_A).next_to(da_box, DOWN, buff=0.12)
        db_label = Text("分母 B", font=FONT, font_size=FS_XS, color=C_DENOM_B).next_to(db_box, DOWN, buff=0.12)
        self.play(Create(da_box), Create(db_box), FadeIn(da_label), FadeIn(db_label), run_time=0.5)
        self.wait(0.2)

        # ── Step 2 — LCD ──
        s2 = self._step_tag("Step 2", "找最简公分母 LCD", UP * 3.3)
        self.play(FadeIn(s2, shift=RIGHT * 0.3), run_time=0.4)

        lcd_label = Text("LCD  =", font=FONT, font_size=FS_BODY, color=C_LCD)
        lcd_val   = MathTex(r"x(x+1)", font_size=FS_TTL + 4, color=C_LCD)
        lcd_row   = VGroup(lcd_label, lcd_val).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)
        lcd_rect  = SurroundingRectangle(lcd_row, color=C_LCD, buff=0.2, corner_radius=0.15, stroke_width=3)
        self.play(Write(lcd_row), Create(lcd_rect), run_time=0.6)
        self.wait(0.3)

        # ── Step 3 — 同乘补充因式 ──
        s3 = self._step_tag("Step 3", "同乘补充因式", UP * 1.5)
        self.play(FadeIn(s3, shift=RIGHT * 0.3), run_time=0.4)

        # 第一个分式：1/x × (x+1)/(x+1)
        mul1_label = Text("第①式：", font=FONT, font_size=FS_XS, color=C_SUBTITLE).move_to(UP * 0.7 + LEFT * 3.2)
        mul1_expr  = MathTex(
            r"\dfrac{1}{x} \times \dfrac{x+1}{x+1} = \dfrac{x+1}{x(x+1)}",
            font_size=40, color=WHITE,
        ).move_to(UP * 0.7 + RIGHT * 0.5)
        # 高亮补充因式
        mul1_expr[0][4:7].set_color(C_NUMER)   # 分子 x+1
        mul1_expr[0][8:11].set_color(C_NUMER)  # 分母 x+1

        self.play(FadeIn(mul1_label), Write(mul1_expr), run_time=0.6)
        self.wait(0.2)

        # 第二个分式：1/(x+1) × x/x
        mul2_label = Text("第②式：", font=FONT, font_size=FS_XS, color=C_SUBTITLE).move_to(DOWN * 0.3 + LEFT * 3.2)
        mul2_expr  = MathTex(
            r"\dfrac{1}{x+1} \times \dfrac{x}{x} = \dfrac{x}{x(x+1)}",
            font_size=40, color=WHITE,
        ).move_to(DOWN * 0.3 + RIGHT * 0.5)
        mul2_expr[0][5:6].set_color(C_NUMER)   # 分子 x
        mul2_expr[0][7:8].set_color(C_NUMER)   # 分母 x

        self.play(FadeIn(mul2_label), Write(mul2_expr), run_time=0.6)
        self.wait(0.3)

        # 通分后汇总
        combined_label = Text("通分结果：", font=FONT, font_size=FS_SM, color=C_SUBTITLE).move_to(DOWN * 1.5 + LEFT * 2.8)
        combined_expr  = MathTex(
            r"\dfrac{x+1}{x(x+1)} + \dfrac{x}{x(x+1)}",
            font_size=46, color=WHITE,
        ).move_to(DOWN * 1.5 + RIGHT * 0.8)

        # 用 Brace 标注公分母
        brace_bot = Brace(combined_expr, direction=DOWN, color=C_LCD, buff=0.05)
        brace_lbl = Text("同一个分母！", font=FONT, font_size=FS_XS, color=C_LCD).next_to(brace_bot, DOWN, buff=0.1)

        self.play(FadeIn(combined_label), Write(combined_expr), run_time=0.6)
        self.play(GrowFromCenter(brace_bot), FadeIn(brace_lbl), run_time=0.4)
        self.wait(0.3)

        # 合并分子 → 最终结果
        final_label = Text("合并分子：", font=FONT, font_size=FS_SM, color=C_SUBTITLE).move_to(DOWN * 3.0 + LEFT * 2.8)
        final_expr  = MathTex(
            r"= \dfrac{(x+1)+x}{x(x+1)} = \dfrac{2x+1}{x(x+1)}",
            font_size=44, color=C_RESULT,
        ).move_to(DOWN * 3.0 + RIGHT * 0.6)
        final_rect = SurroundingRectangle(final_expr, color=C_RESULT, buff=0.2,
                                          corner_radius=0.15, stroke_width=2.5)
        self.play(FadeIn(final_label), Write(final_expr), Create(final_rect), run_time=0.7)
        self.wait(1.5)

        all_s3 = VGroup(
            sec, orig, s1, da_box, db_box, da_label, db_label,
            s2, lcd_row, lcd_rect,
            s3, mul1_label, mul1_expr, mul2_label, mul2_expr,
            combined_label, combined_expr, brace_bot, brace_lbl,
            final_label, final_expr, final_rect,
        )
        self.play(FadeOut(all_s3), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 4 — 进阶例题：1/(x²-1) + 1/(x+1)
    # ══════════════════════════════════════════
    def scene_4_example2(self):
        sec = self._section_title("③ 进阶：先分解再通分", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        # ── 原式 ──
        orig2_l = MathTex(r"\dfrac{1}{x^2-1}", font_size=60, color=C_DENOM_A)
        orig2_p = Text("+", font=FONT, font_size=FS_TTL, color=WHITE)
        orig2_r = MathTex(r"\dfrac{1}{x+1}", font_size=60, color=C_DENOM_B)
        orig2   = VGroup(orig2_l, orig2_p, orig2_r).arrange(RIGHT, buff=0.4).move_to(UP * 5.5)
        self.play(Write(orig2), run_time=0.6)
        self.wait(0.2)

        # ── Step 1：因式分解 x²-1 ──
        s1 = self._step_tag("Step 1", "分母因式分解", UP * 4.5)
        self.play(FadeIn(s1, shift=RIGHT * 0.3), run_time=0.4)

        factored_show = MathTex(
            r"x^2 - 1 = (x+1)(x-1)",
            font_size=48, color=WHITE,
        ).move_to(UP * 3.7)
        # 高亮 (x+1)(x-1)
        factored_show[0][6:11].set_color(C_DENOM_A)

        sq_note = Text(
            "（平方差公式：a²-b²=(a+b)(a-b)）",
            font=FONT, font_size=FS_XS, color=C_SUBTITLE,
        ).next_to(factored_show, DOWN, buff=0.15)

        self.play(Write(factored_show), run_time=0.5)
        self.play(FadeIn(sq_note), run_time=0.3)
        self.wait(0.3)

        # ── Step 2：找 LCD ──
        s2 = self._step_tag("Step 2", "找最简公分母 LCD", UP * 2.6)
        self.play(FadeIn(s2, shift=RIGHT * 0.3), run_time=0.4)

        # 两分母对比
        da_txt = Text("分母①: (x+1)(x-1)", font=FONT, font_size=FS_XS, color=C_DENOM_A).move_to(UP * 2.0 + LEFT * 2.0)
        db_txt = Text("分母②: (x+1)", font=FONT, font_size=FS_XS, color=C_DENOM_B).move_to(UP * 2.0 + RIGHT * 2.0)
        self.play(FadeIn(da_txt), FadeIn(db_txt), run_time=0.4)

        overlap_note = Text(
            "(x+1) 已包含在分母①中，取最高次幂",
            font=FONT, font_size=FS_XS, color=C_LCD,
        ).move_to(UP * 1.3)
        self.play(FadeIn(overlap_note), run_time=0.3)

        lcd2_label = Text("LCD  =", font=FONT, font_size=FS_BODY, color=C_LCD)
        lcd2_val   = MathTex(r"(x+1)(x-1)", font_size=FS_TTL, color=C_LCD)
        lcd2_row   = VGroup(lcd2_label, lcd2_val).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        lcd2_rect  = SurroundingRectangle(lcd2_row, color=C_LCD, buff=0.2, corner_radius=0.15, stroke_width=3)
        self.play(Write(lcd2_row), Create(lcd2_rect), run_time=0.6)
        self.wait(0.3)

        # ── Step 3：通分 ──
        s3 = self._step_tag("Step 3", "同乘补充因式", DOWN * 0.4)
        self.play(FadeIn(s3, shift=RIGHT * 0.3), run_time=0.4)

        # 第①式分母已是 LCD，分子 ×1，不变
        m1_label = Text("第①式：分母已是 LCD，分子不变", font=FONT, font_size=FS_XS, color=C_SUBTITLE).move_to(DOWN * 1.1)
        m1_expr  = MathTex(
            r"\dfrac{1}{(x+1)(x-1)}",
            font_size=44, color=WHITE,
        ).move_to(DOWN * 1.9)
        self.play(FadeIn(m1_label), Write(m1_expr), run_time=0.5)

        # 第②式 ×(x-1)
        m2_label = Text("第②式：×(x-1)", font=FONT, font_size=FS_XS, color=C_SUBTITLE).move_to(DOWN * 2.9 + LEFT * 2.5)
        m2_expr  = MathTex(
            r"\dfrac{x-1}{(x+1)(x-1)}",
            font_size=44, color=WHITE,
        ).move_to(DOWN * 2.9 + RIGHT * 0.8)
        m2_expr[0][:3].set_color(C_NUMER)   # 分子 x-1

        self.play(FadeIn(m2_label), Write(m2_expr), run_time=0.5)
        self.wait(0.3)

        # 通分结果
        result2 = MathTex(
            r"= \dfrac{1}{(x+1)(x-1)} + \dfrac{x-1}{(x+1)(x-1)}",
            font_size=38, color=C_RESULT,
        ).move_to(DOWN * 4.2)
        result2_rect = SurroundingRectangle(result2, color=C_RESULT, buff=0.2,
                                             corner_radius=0.15, stroke_width=2.5)
        self.play(Write(result2), Create(result2_rect), run_time=0.7)
        self.wait(1.5)

        all_s4 = VGroup(
            sec, orig2, s1, factored_show, sq_note,
            s2, da_txt, db_txt, overlap_note, lcd2_row, lcd2_rect,
            s3, m1_label, m1_expr, m2_label, m2_expr,
            result2, result2_rect,
        )
        self.play(FadeOut(all_s4), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 5 — 三步走总结 + 口诀
    # ══════════════════════════════════════════
    def scene_5_summary(self):
        sec = self._section_title("通分三步走", UP * 6.8)
        self.play(FadeIn(sec, shift=DOWN * 0.2), run_time=0.4)

        cards_data = [
            ("Step 1", "各分母分别因式分解",            C_PRIMARY, UP * 4.8),
            ("Step 2", "LCD = 各因式最高次幂之积",      C_LCD,     UP * 2.8),
            ("Step 3", "各式分子分母同乘补充因式",      C_RESULT,  UP * 0.8),
        ]
        cards = VGroup()
        for tag, body, color, pos in cards_data:
            card = self._step_card(tag, body, color, pos)
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.55)
            self.wait(0.2)

        self.wait(0.3)

        # 口诀框
        mnemonic_bg = RoundedRectangle(
            width=7.6, height=1.55,
            corner_radius=0.25, fill_color="#0d1b2a", fill_opacity=0.97,
            stroke_color=C_HIGHLIGHT, stroke_width=2.5,
        ).move_to(DOWN * 1.5)
        mnemonic_icon = Text("💡", font=FONT, font_size=FS_SUB).move_to(mnemonic_bg.get_left() + RIGHT * 0.55)
        mnemonic_lines = VGroup(
            Text("口诀：", font=FONT, font_size=FS_SM, color=C_HIGHLIGHT),
            Text("公分母找到，各自乘补缺，分子跟着变",
                 font=FONT, font_size=FS_XS, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(mnemonic_icon, RIGHT, buff=0.25)
        mnemonic_content = VGroup(mnemonic_icon, mnemonic_lines)
        mnemonic_content.move_to(mnemonic_bg.get_center())

        self.play(FadeIn(mnemonic_bg), FadeIn(mnemonic_content), run_time=0.6)
        self.wait(2.0)

        all_s5 = VGroup(sec, cards, mnemonic_bg, mnemonic_content)
        self.play(FadeOut(all_s5), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 6 — 片尾
    # ══════════════════════════════════════════
    def scene_6_outro(self):
        big = Text(
            "分式的通分",
            font=FONT, font_size=FS_BIG, color=C_LCD, weight=BOLD,
        ).move_to(UP * 2.5)
        self.play(Write(big), run_time=0.6)

        aname = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=FS_SUB + 4, color=WHITE,
        ).move_to(UP * 0.8)
        aid = Text(
            "@emptyandcalm",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE,
        ).next_to(aname, DOWN, buff=0.22)
        self.play(FadeIn(aname, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(aid), run_time=0.3)

        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=C_SUBTITLE, stroke_width=1).move_to(DOWN * 0.4)
        self.play(Create(divider), run_time=0.3)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰：通分算式
        deco = VGroup(
            MathTex(r"\frac{1}{x}+\frac{1}{x+1}=\frac{2x+1}{x(x+1)}", font_size=20, color=C_LCD),
            MathTex(r"\text{LCD} = x(x+1)", font_size=20, color=C_DENOM_A),
            MathTex(r"\frac{1}{x^2-1}+\frac{1}{x+1}", font_size=20, color=C_DENOM_B),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.0)
        self.play(FadeIn(deco, shift=UP * 0.2), run_time=0.5)
        self.play(Wiggle(deco, scale_value=1.06), run_time=0.8)

        slogan = Text(
            "每天一道题，数学不再难！",
            font=FONT, font_size=FS_SM, color=C_SUBTITLE,
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(slogan), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(big, aname, aid, divider, follow, deco, slogan)),
            FadeOut(VGroup(self.small_title, self.author_bar)),
            run_time=0.8,
        )

    # ══════════════════════════════════════════
    #  工具方法
    # ══════════════════════════════════════════
    def _make_author_bar(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=FS_AUTH, color=GRAY_B,
        ).move_to(UP * 6.9)

    def _section_title(self, text: str, pos):
        bar = Rectangle(
            width=0.12, height=0.55,
            fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0,
        )
        lbl = Text(text, font=FONT, font_size=FS_SUB, color=C_PRIMARY)
        grp = VGroup(bar, lbl).arrange(RIGHT, buff=0.2)
        grp.move_to(pos)
        return grp

    def _step_tag(self, tag_str: str, body_str: str, pos):
        tag     = Text(tag_str, font=FONT, font_size=FS_XS + 1, color=C_STEP, weight=BOLD)
        tag_box = SurroundingRectangle(tag, color=C_STEP, buff=0.1, corner_radius=0.1, stroke_width=2)
        body    = Text(body_str, font=FONT, font_size=FS_XS + 1, color=C_SUBTITLE)
        grp     = VGroup(VGroup(tag_box, tag), body).arrange(RIGHT, buff=0.28)
        grp.move_to(pos)
        return grp

    def _step_card(self, tag_str: str, body_str: str, color, pos):
        tag_mob  = Text(tag_str,  font=FONT, font_size=FS_SM + 2, color=color, weight=BOLD)
        body_mob = Text(body_str, font=FONT, font_size=FS_BODY,   color=WHITE)
        content  = VGroup(tag_mob, body_mob).arrange(RIGHT, buff=0.4)
        bg = RoundedRectangle(
            width=7.6, height=content.height + 0.6,
            corner_radius=0.22, fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=color, stroke_width=2.5,
        )
        card = VGroup(bg, content)
        content.move_to(bg.get_center())
        card.move_to(pos)
        return card
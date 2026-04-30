"""
分数指数幂 - Manim 教学动画
七年级第二学期 第十二章
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 颜色常量 ──────────────────────────────────────
COLOR_BG      = "#1a1a2e"
COLOR_BASE    = "#4fc3f7"   # 天蓝  — 底数
COLOR_EXP     = "#ff7043"   # 橙红  — 指数
COLOR_ROOT    = "#66bb6a"   # 绿    — 根号
COLOR_NEG     = "#ce93d8"   # 紫    — 负指数
COLOR_RULE    = "#ffd54f"   # 金黄  — 运算法则
COLOR_RESULT  = "#80cbc4"   # 青绿  — 结果
COLOR_FORMULA = "#ffd54f"
COLOR_AUTHOR  = "#78909c"
FONT = "PingFang SC"


class FractionalExponent(Scene):
    """
    场景顺序:
    1. 开场钩子   — 根式与幂的联系
    2. 正分数指数 — a^(1/n) = ⁿ√a
    3. 一般分数幂 — a^(m/n) = ⁿ√(aᵐ)
    4. 负分数指数 — a^(-m/n) = 1/a^(m/n)
    5. 互化练习   — 根式 ↔ 分数指数幂
    6. 运算法则推广
    7. 综合例题
    8. 总结+片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG
        self.scene_opening()
        self.scene_half_power()
        self.scene_frac_power()
        self.scene_neg_power()
        self.scene_convert()
        self.scene_laws()
        self.scene_combined()
        self.scene_outro()

    # ══════════════════════════════════════════════
    # 工具：双向转化箭头
    # ══════════════════════════════════════════════
    def double_arrow(self, left_mob, right_mob, color=GRAY):
        mid_l = left_mob.get_right() + RIGHT * 0.15
        mid_r = right_mob.get_left() + LEFT * 0.15
        arr = DoubleArrow(mid_l, mid_r, color=color, buff=0,
                          stroke_width=2.5,
                          max_tip_length_to_length_ratio=0.18)
        return arr

    # ══════════════════════════════════════════════
    # Scene 1  开场钩子
    # ══════════════════════════════════════════════
    def scene_opening(self):
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR
        ).move_to(UP * 7.3)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_obj = author

        title = Text("分数指数幂", font=FONT, font_size=50, color=GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 引出问题：√a 能不能写成 a 的某个幂？
        q_part1 = MathTex(r"\sqrt{a}", font_size=48, color=COLOR_ROOT)
        q_part1.move_to(LEFT * 2.0 + UP * 4.8)
        q_mark = Text("=  ?", font=FONT, font_size=40, color=YELLOW)
        q_mark.next_to(q_part1, RIGHT, buff=0.3)
        self.play(Write(q_part1), FadeIn(q_mark, shift=LEFT*0.2), run_time=0.5)

        hint = Text("能！用分数指数幂来表示", font=FONT, font_size=28, color=WHITE)
        hint.move_to(UP * 3.8)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.4)

        # 揭晓
        ans = MathTex(r"\sqrt{a} = a^{\frac{1}{2}}", font_size=52, color=COLOR_EXP)
        ans.move_to(UP * 2.8)
        box_ans = SurroundingRectangle(ans, color=COLOR_EXP, buff=0.22, corner_radius=0.12)
        self.play(Write(ans), Create(box_ans), run_time=0.7)

        more = MathTex(
            r"\sqrt[3]{a} = a^{\frac{1}{3}},\quad \sqrt[n]{a} = a^{\frac{1}{n}}",
            font_size=36, color=COLOR_ROOT
        )
        more.move_to(UP * 1.6)
        self.play(FadeIn(more, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, q_part1, q_mark, hint, ans, box_ans, more)),
                  run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 2  a^(1/n) 定义
    # ══════════════════════════════════════════════
    def scene_half_power(self):
        sec = Text("正分数指数幂（分子为1）",
                   font=FONT, font_size=32, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 核心定义框
        defn_box = RoundedRectangle(
            width=7.8, height=1.6, corner_radius=0.16,
            color=COLOR_EXP, fill_color=COLOR_EXP, fill_opacity=0.14, stroke_width=2
        ).move_to(UP * 5.8)

        defn = MathTex(
            r"a^{\frac{1}{n}} = \sqrt[n]{a}",
            font_size=46, color=WHITE
        )
        defn.move_to(defn_box.get_center() + UP * 0.15)

        cond = Text("(a > 0, n 为正整数)", font=FONT, font_size=22, color=GRAY_A)
        cond.move_to(defn_box.get_center() + DOWN * 0.4)

        self.play(Create(defn_box), run_time=0.4)
        self.play(Write(defn), FadeIn(cond), run_time=0.6)

        # 颜色标注：底数 vs 指数
        anno_base = Text("底数", font=FONT, font_size=20, color=COLOR_BASE)
        anno_base.move_to(defn.get_left() + LEFT * 0.8 + DOWN * 0.5)
        arr_base = Arrow(anno_base.get_right(), defn.get_left() + RIGHT * 0.12,
                         color=COLOR_BASE, stroke_width=2, buff=0.05,
                         max_tip_length_to_length_ratio=0.3)

        anno_exp = Text("分数指数", font=FONT, font_size=20, color=COLOR_EXP)
        anno_exp.move_to(defn.get_right() + RIGHT * 1.0 + UP * 0.6)
        arr_exp = Arrow(anno_exp.get_left(), defn.get_right() + LEFT * 0.45 + UP * 0.25,
                        color=COLOR_EXP, stroke_width=2, buff=0.05,
                        max_tip_length_to_length_ratio=0.3)

        self.play(FadeIn(anno_base), Create(arr_base), run_time=0.4)
        self.play(FadeIn(anno_exp), Create(arr_exp), run_time=0.4)

        # 具体例子
        examples_1n = [
            (r"4^{\frac{1}{2}}",  r"= \sqrt{4} = 2",    COLOR_EXP),
            (r"8^{\frac{1}{3}}",  r"= \sqrt[3]{8} = 2",  COLOR_ROOT),
            (r"16^{\frac{1}{4}}", r"= \sqrt[4]{16} = 2", COLOR_EXP),
            (r"a^{\frac{1}{2}}",  r"= \sqrt{a}",         COLOR_ROOT),
        ]

        all_ex = VGroup()
        for i, (lhs, rhs, col) in enumerate(examples_1n):
            y = 3.8 - i * 0.92
            lhs_m = MathTex(lhs, font_size=32, color=WHITE)
            lhs_m.move_to(LEFT * 2.0 + UP * y)
            rhs_m = MathTex(rhs, font_size=32, color=col)
            rhs_m.next_to(lhs_m, RIGHT, buff=0.2)
            self.play(Write(lhs_m), Write(rhs_m), run_time=0.4)
            all_ex.add(lhs_m, rhs_m)

        # 验证 4^(1/2)=2
        verify = MathTex(
            r"2^2 = 4\ \checkmark",
            font_size=28, color=COLOR_RESULT
        )
        verify.move_to(DOWN * 0.7)
        self.play(FadeIn(verify, shift=UP * 0.1), run_time=0.3)

        self.wait(1.2)
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 3  a^(m/n) 一般分数幂
    # ══════════════════════════════════════════════
    def scene_frac_power(self):
        sec = Text("一般分数指数幂", font=FONT, font_size=36, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 核心公式
        defn_box = RoundedRectangle(
            width=7.8, height=2.0, corner_radius=0.16,
            color=COLOR_EXP, fill_color=COLOR_EXP, fill_opacity=0.14, stroke_width=2
        ).move_to(UP * 5.7)

        defn = MathTex(
            r"a^{\frac{m}{n}} = \sqrt[n]{a^m} = (\sqrt[n]{a})^m",
            font_size=36, color=WHITE
        )
        defn.move_to(defn_box.get_center() + UP * 0.2)
        cond2 = Text("(a > 0, m,n 为正整数)", font=FONT, font_size=22, color=GRAY_A)
        cond2.move_to(defn_box.get_center() + DOWN * 0.5)
        self.play(Create(defn_box), Write(defn), FadeIn(cond2), run_time=0.7)

        # 解析：指数分子=幂次，分母=根次
        anno_m = Text("分子 m = 幂次", font=FONT, font_size=22, color=COLOR_BASE)
        anno_n = Text("分母 n = 根次", font=FONT, font_size=22, color=COLOR_ROOT)
        anno_m.move_to(LEFT * 2.2 + UP * 4.3)
        anno_n.move_to(RIGHT * 2.2 + UP * 4.3)
        self.play(FadeIn(anno_m), FadeIn(anno_n), run_time=0.4)

        # 例子
        examples_mn = [
            # (式子, 展开1, 展开2, 最终值)
            (r"8^{\frac{2}{3}}",
             r"= \sqrt[3]{8^2} = \sqrt[3]{64}",
             r"= 4"),
            (r"4^{\frac{3}{2}}",
             r"= \left(\sqrt{4}\right)^3 = 2^3",
             r"= 8"),
            (r"27^{\frac{2}{3}}",
             r"= \left(\sqrt[3]{27}\right)^2 = 3^2",
             r"= 9"),
        ]

        all_ex = VGroup()
        for i, (prob, step1, step2) in enumerate(examples_mn):
            y = 3.4 - i * 1.1
            prob_m = MathTex(prob, font_size=32, color=WHITE)
            prob_m.move_to(LEFT * 2.8 + UP * y)
            step1_m = MathTex(step1, font_size=28, color=GRAY_A)
            step1_m.next_to(prob_m, RIGHT, buff=0.1)
            step2_m = MathTex(step2, font_size=32, color=COLOR_RESULT)
            step2_m.next_to(step1_m, RIGHT, buff=0.1)
            self.play(Write(prob_m), run_time=0.3)
            self.play(Write(step1_m), Write(step2_m), run_time=0.45)
            all_ex.add(prob_m, step1_m, step2_m)

        # 优先方法提示
        tip_box = RoundedRectangle(
            width=7.4, height=1.0, corner_radius=0.12,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.1, stroke_width=1.5
        ).move_to(DOWN * 0.6)
        tip_part1 = Text("推荐：先开根号，再乘幂", font=FONT, font_size=22, color=YELLOW)
        tip_part2 = MathTex(r"(\ \sqrt[n]{a}\ )^m", font_size=24, color=YELLOW)
        tip_row = VGroup(tip_part1, tip_part2).arrange(RIGHT, buff=0.2)
        tip_row.move_to(tip_box.get_center())
        self.play(Create(tip_box), FadeIn(tip_row), run_time=0.5)
        self.wait(1.3)

        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 4  负分数指数幂
    # ══════════════════════════════════════════════
    def scene_neg_power(self):
        sec = Text("负分数指数幂", font=FONT, font_size=36, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 类比负整数幂
        analogy_title = Text("类比负整数幂：", font=FONT, font_size=26, color=GRAY_A)
        analogy_title.move_to(LEFT * 1.5 + UP * 6.1)
        analogy = MathTex(
            r"a^{-n} = \frac{1}{a^n}",
            font_size=34, color=GRAY_A
        )
        analogy.next_to(analogy_title, RIGHT, buff=0.2)
        self.play(FadeIn(analogy_title), Write(analogy), run_time=0.5)

        # 推广定义
        defn_box = RoundedRectangle(
            width=7.8, height=1.5, corner_radius=0.16,
            color=COLOR_NEG, fill_color=COLOR_NEG, fill_opacity=0.14, stroke_width=2
        ).move_to(UP * 5.0)
        defn = MathTex(
            r"a^{-\frac{m}{n}} = \frac{1}{a^{\frac{m}{n}}} = \frac{1}{\sqrt[n]{a^m}}",
            font_size=34, color=WHITE
        )
        defn.move_to(defn_box.get_center())
        self.play(Create(defn_box), Write(defn), run_time=0.7)

        # 例子
        neg_examples = [
            (r"4^{-\frac{1}{2}}",
             r"= \frac{1}{4^{\frac{1}{2}}} = \frac{1}{\sqrt{4}} = \frac{1}{2}"),
            (r"8^{-\frac{1}{3}}",
             r"= \frac{1}{8^{\frac{1}{3}}} = \frac{1}{\sqrt[3]{8}} = \frac{1}{2}"),
            (r"27^{-\frac{2}{3}}",
             r"= \frac{1}{27^{\frac{2}{3}}} = \frac{1}{9}"),
        ]

        all_neg = VGroup()
        for i, (prob, sol) in enumerate(neg_examples):
            y = 3.7 - i * 1.1
            prob_m = MathTex(prob, font_size=32, color=WHITE)
            prob_m.move_to(LEFT * 2.5 + UP * y)
            sol_m = MathTex(sol, font_size=28, color=COLOR_NEG)
            sol_m.next_to(prob_m, RIGHT, buff=0.15)
            self.play(Write(prob_m), run_time=0.3)
            self.play(Write(sol_m), run_time=0.45)
            all_neg.add(prob_m, sol_m)

        # 规律框：三类指数汇总
        summary_box = RoundedRectangle(
            width=7.8, height=2.2, corner_radius=0.15,
            color=COLOR_RULE, fill_color=COLOR_RULE, fill_opacity=0.1, stroke_width=1.5
        ).move_to(DOWN * 1.6)

        row1 = MathTex(r"a^{\frac{1}{n}} = \sqrt[n]{a}", font_size=28, color=COLOR_EXP)
        row2 = MathTex(r"a^{\frac{m}{n}} = (\sqrt[n]{a})^m", font_size=28, color=COLOR_ROOT)
        row3 = MathTex(r"a^{-\frac{m}{n}} = \dfrac{1}{a^{\frac{m}{n}}}", font_size=28, color=COLOR_NEG)
        rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.28)
        rows.move_to(summary_box.get_center())

        self.play(Create(summary_box), run_time=0.4)
        for r in [row1, row2, row3]:
            self.play(Write(r), run_time=0.4)

        self.wait(1.3)
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 5  根式 ↔ 分数指数幂 互化
    # ══════════════════════════════════════════════
    def scene_convert(self):
        sec = Text("根式与分数指数幂的互化",
                   font=FONT, font_size=32, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 双向箭头说明
        lhs_eg = MathTex(r"\sqrt[n]{a^m}", font_size=38, color=COLOR_ROOT)
        rhs_eg = MathTex(r"a^{\frac{m}{n}}", font_size=38, color=COLOR_EXP)
        lhs_eg.move_to(LEFT * 2.5 + UP * 5.8)
        rhs_eg.move_to(RIGHT * 2.5 + UP * 5.8)
        d_arr = DoubleArrow(
            lhs_eg.get_right() + RIGHT * 0.1,
            rhs_eg.get_left() + LEFT * 0.1,
            color=GRAY, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.18
        )
        self.play(Write(lhs_eg), Write(rhs_eg), Create(d_arr), run_time=0.6)

        # 互化练习表
        converts = [
            # (根式, 分数幂, 方向)
            (r"\sqrt{5}",          r"5^{\frac{1}{2}}",    "→"),
            (r"\sqrt[3]{a^2}",     r"a^{\frac{2}{3}}",    "→"),
            (r"\sqrt[4]{b^3}",     r"b^{\frac{3}{4}}",    "→"),
            (r"x^{\frac{3}{5}}",   r"\sqrt[5]{x^3}",      "←"),
            (r"y^{-\frac{1}{2}}",  r"\dfrac{1}{\sqrt{y}}", "←"),
        ]

        all_conv = VGroup()
        for i, (root_s, pow_s, direction) in enumerate(converts):
            y = 4.6 - i * 0.95
            if direction == "→":
                left_m  = MathTex(root_s, font_size=30, color=COLOR_ROOT)
                right_m = MathTex(pow_s,  font_size=30, color=COLOR_EXP)
                arr_col = COLOR_EXP
            else:
                left_m  = MathTex(root_s, font_size=30, color=COLOR_EXP)
                right_m = MathTex(pow_s,  font_size=30, color=COLOR_ROOT)
                arr_col = COLOR_ROOT

            left_m.move_to(LEFT * 2.5 + UP * y)
            arr = Arrow(left_m.get_right() + RIGHT * 0.1,
                        left_m.get_right() + RIGHT * 0.7,
                        color=arr_col, buff=0, stroke_width=2,
                        max_tip_length_to_length_ratio=0.35)
            right_m.next_to(arr, RIGHT, buff=0.1)
            self.play(Write(left_m), Create(arr), Write(right_m), run_time=0.45)
            all_conv.add(left_m, arr, right_m)

        # 转化口诀
        mnemonic_part1 = Text("口诀：", font=FONT, font_size=22, color=YELLOW)
        mnemonic_part2 = Text("分子为幂次，分母为根次", font=FONT, font_size=24, color=YELLOW)
        mnemonic = VGroup(mnemonic_part1, mnemonic_part2).arrange(RIGHT, buff=0.15)
        mnemonic.move_to(DOWN * 0.5)
        box_m = SurroundingRectangle(mnemonic, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(mnemonic), Create(box_m), run_time=0.5)

        self.wait(1.3)
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 6  运算法则推广
    # ══════════════════════════════════════════════
    def scene_laws(self):
        sec = Text("运算法则对分数指数同样成立",
                   font=FONT, font_size=30, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        laws = [
            # (名称, 公式)
            ("同底数幂相乘",
             r"a^m \cdot a^n = a^{m+n}"),
            ("同底数幂相除",
             r"a^m \div a^n = a^{m-n}"),
            ("幂的乘方",
             r"\left(a^m\right)^n = a^{mn}"),
            ("积的乘方",
             r"(ab)^m = a^m b^m"),
        ]

        law_colors = [COLOR_EXP, COLOR_ROOT, COLOR_NEG, COLOR_RULE]
        all_law_rows = VGroup()
        for i, ((name, formula), col) in enumerate(zip(laws, law_colors)):
            y = 5.8 - i * 1.05
            name_t = Text(name, font=FONT, font_size=24, color=col)
            name_t.move_to(LEFT * 2.5 + UP * y)
            colon = Text("：", font=FONT, font_size=24, color=GRAY)
            colon.next_to(name_t, RIGHT, buff=0.04)
            formula_m = MathTex(formula, font_size=28, color=WHITE)
            formula_m.next_to(colon, RIGHT, buff=0.1)
            row = VGroup(name_t, colon, formula_m)
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            all_law_rows.add(row)

        # 具体例子（用分数指数）
        eg_title = Text("举例（分数指数）：", font=FONT, font_size=24, color=YELLOW)
        eg_title.move_to(LEFT * 1.0 + UP * 1.4)
        self.play(FadeIn(eg_title, shift=UP * 0.1), run_time=0.3)

        egs_law = [
            r"2^{\frac{1}{2}} \cdot 2^{\frac{1}{2}} = 2^1 = 2",
            r"8^{\frac{2}{3}} \div 8^{\frac{1}{3}} = 8^{\frac{1}{3}} = 2",
            r"(a^{\frac{1}{2}})^4 = a^2",
        ]
        for i, eg in enumerate(egs_law):
            eg_m = MathTex(eg, font_size=28, color=COLOR_RESULT)
            eg_m.move_to(UP * (0.5 - i * 0.85))
            self.play(Write(eg_m), run_time=0.45)

        self.wait(1.2)
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 7  综合例题
    # ══════════════════════════════════════════════
    def scene_combined(self):
        sec = Text("综合例题", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.4)

        # 例1：化简
        ex1_label = Text("例1  化简：", font=FONT, font_size=26, color=GRAY_A)
        ex1_label.move_to(LEFT * 2.0 + UP * 6.2)
        ex1_prob = MathTex(
            r"a^{\frac{1}{3}} \cdot a^{\frac{1}{2}}",
            font_size=36, color=WHITE
        )
        ex1_prob.next_to(ex1_label, RIGHT, buff=0.2)
        self.play(FadeIn(ex1_label), Write(ex1_prob), run_time=0.5)

        ex1_step1 = MathTex(
            r"= a^{\frac{1}{3} + \frac{1}{2}}",
            font_size=36, color=WHITE
        )
        ex1_step1.move_to(UP * 5.2)
        ex1_step2 = MathTex(
            r"= a^{\frac{2}{6} + \frac{3}{6}}",
            font_size=36, color=WHITE
        )
        ex1_step2.move_to(UP * 4.3)
        ex1_ans = MathTex(
            r"= a^{\frac{5}{6}}",
            font_size=42, color=COLOR_RESULT
        )
        ex1_ans.move_to(UP * 3.3)
        ex1_box = SurroundingRectangle(ex1_ans, color=COLOR_RESULT, buff=0.18, corner_radius=0.1)

        for mob in [ex1_step1, ex1_step2]:
            self.play(Write(mob), run_time=0.45)
        self.play(Write(ex1_ans), Create(ex1_box), run_time=0.5)

        # 例2：转化计算
        ex2_label = Text("例2  计算：", font=FONT, font_size=26, color=GRAY_A)
        ex2_label.move_to(LEFT * 2.0 + UP * 2.3)
        ex2_prob = MathTex(
            r"\sqrt[6]{a^4} \div \sqrt[3]{a}",
            font_size=36, color=WHITE
        )
        ex2_prob.next_to(ex2_label, RIGHT, buff=0.2)
        self.play(FadeIn(ex2_label), Write(ex2_prob), run_time=0.5)

        ex2_step1 = MathTex(
            r"= a^{\frac{4}{6}} \div a^{\frac{1}{3}}",
            font_size=32, color=GRAY_A
        )
        ex2_step1.move_to(UP * 1.3)
        ex2_step2 = MathTex(
            r"= a^{\frac{2}{3}} \div a^{\frac{1}{3}}",
            font_size=32, color=GRAY_A
        )
        ex2_step2.move_to(UP * 0.4)
        ex2_ans = MathTex(
            r"= a^{\frac{2}{3} - \frac{1}{3}} = a^{\frac{1}{3}}",
            font_size=36, color=COLOR_RESULT
        )
        ex2_ans.move_to(DOWN * 0.6)
        ex2_box = SurroundingRectangle(ex2_ans, color=COLOR_RESULT, buff=0.18, corner_radius=0.1)

        for mob in [ex2_step1, ex2_step2]:
            self.play(Write(mob), run_time=0.4)
        self.play(Write(ex2_ans), Create(ex2_box), run_time=0.5)

        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects
                    if m is not self.author_obj], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 8  总结+片尾
    # ══════════════════════════════════════════════
    def scene_outro(self):
        sum_title = Text("本节要点", font=FONT, font_size=36, color=GOLD)
        sum_title.move_to(UP * 7.0)
        self.play(Write(sum_title), run_time=0.4)

        # ("math"/"text"/"mixed", 内容, 颜色)
        points = [
            ("math",  r"a^{\frac{1}{n}} = \sqrt[n]{a}",                COLOR_EXP),
            ("math",  r"a^{\frac{m}{n}} = (\sqrt[n]{a})^m", COLOR_ROOT),
            ("math",  r"a^{-\frac{m}{n}} = \dfrac{1}{a^{\frac{m}{n}}}",COLOR_NEG),
            ("mixed", (r"a^m \cdot a^n = a^{m+n}", "（分数指数也适用）"), COLOR_RULE),
            ("text",  "分子=幂次，分母=根次",                            COLOR_FORMULA),
        ]

        point_mobs = VGroup()
        for i, (kind, content, col) in enumerate(points):
            y = 5.8 - i * 1.1
            if kind == "math":
                mob = MathTex(content, font_size=28, color=col)
            elif kind == "mixed":
                m_p = MathTex(content[0], font_size=28, color=col)
                t_p = Text(content[1], font=FONT, font_size=20, color=col)
                mob = VGroup(m_p, t_p).arrange(RIGHT, buff=0.12)
            else:
                mob = Text(content, font=FONT, font_size=24, color=col)
            mob.move_to(UP * y + RIGHT * 0.4)
            mob.align_to(LEFT * 0.3, LEFT)
            dot = Dot(radius=0.07, color=col).next_to(mob, LEFT, buff=0.2)
            grp = VGroup(dot, mob)
            point_mobs.add(grp)
            self.play(FadeIn(grp, shift=RIGHT * 0.2), run_time=0.35)

        self.wait(1.5)
        self.play(FadeOut(VGroup(sum_title, point_mobs)), run_time=0.5)

        # 片尾
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=40, color=WHITE)
        author_big.move_to(UP * 2.0)
        author_id = Text("@emptyandcalm", font=FONT, font_size=30, color=COLOR_AUTHOR)
        author_id.next_to(author_big, DOWN, buff=0.3)
        self.play(Transform(self.author_obj, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=YELLOW)
        follow.move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰：三个分数指数幂飞入
        deco_exprs = [
            (r"a^{\frac{1}{2}}", LEFT * 2.5 + DOWN * 2.3, COLOR_EXP),
            (r"a^{\frac{2}{3}}", ORIGIN + DOWN * 2.3,      COLOR_ROOT),
            (r"a^{-\frac{1}{2}}", RIGHT * 2.5 + DOWN * 2.3, COLOR_NEG),
        ]
        deco = VGroup(*[
            MathTex(tex, font_size=30, color=col).move_to(pos)
            for tex, pos, col in deco_exprs
        ])
        self.play(*[FadeIn(d, shift=UP * 0.3) for d in deco], run_time=0.5)

        finale = MathTex(
            r"\sqrt[n]{a^m} = a^{\frac{m}{n}}",
            font_size=40, color=COLOR_RULE
        )
        finale.move_to(DOWN * 3.6)
        self.play(Write(finale), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(Group(
            self.author_obj, author_id, follow, deco, finale
        )), run_time=0.8)


# 渲染:
#   manim -pql frac_exponent.py FractionalExponent
#   manim -qh  frac_exponent.py FractionalExponent
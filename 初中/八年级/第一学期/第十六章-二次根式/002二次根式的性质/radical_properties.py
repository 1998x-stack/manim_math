"""
二次根式的性质
Properties of Quadratic Radicals — Manim Animation

年级: 八年级第一学期
章节: 第十六章 二次根式
核心公式:
  性质1: (√a)² = a  (a ≥ 0)
  性质2: √(a²)  = |a|  (全体实数)

TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 — TikTok竖屏
# ============================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class QuadraticRadicalProperties(Scene):
    """
    二次根式的性质教学动画
    场景顺序:
      1. 开场 Hook  —  引发疑问
      2. 快速回顾   —  二次根式定义
      3. 性质1      —  (√a)² = a
      4. 性质2引入  —  揭示陷阱
      5. 性质2完整  —  √(a²) = |a|，数轴分类讨论
      6. 易错辨析   —  对比正误
      7. 总结片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ── 颜色 ──────────────────────────────────────────
        self.C_TITLE   = YELLOW
        self.C_P1      = "#00CED1"   # 性质1 青色
        self.C_P2      = "#FF6B6B"   # 性质2 红色
        self.C_POS     = "#2ECC71"   # 正数  绿色
        self.C_NEG     = "#FF4500"   # 负数  橙红
        self.C_ABS     = "#FFD700"   # 绝对值 金色
        self.C_WRONG   = "#FF0000"   # 错误  纯红
        self.C_RIGHT   = "#00CC44"   # 正确  纯绿
        self.C_CARD_BG = "#16213e"

        # ── 执行场景 ──────────────────────────────────────
        self.scene_1_hook()
        self.scene_2_review()
        self.scene_3_prop1()
        self.scene_4_prop2_trap()
        self.scene_5_prop2_full()
        self.scene_6_pitfall()
        self.scene_7_summary()

    # =========================================================
    # § 工具方法
    # =========================================================
    def _author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=20, color=GRAY_B,
        ).move_to(UP * 6.8)

    def _title(self, txt, color=None, y=6.0):
        return Text(
            txt, font="PingFang SC",
            font_size=38, color=color or self.C_TITLE,
        ).move_to(UP * y)

    def _card(self, w, h, pos, border, fill="#16213e"):
        return RoundedRectangle(
            width=w, height=h, corner_radius=0.28,
            fill_color=fill, fill_opacity=0.92,
            stroke_color=border, stroke_width=2,
        ).move_to(pos)

    def _check(self, pos, color=None):
        """✓ 勾号"""
        return Text("✓", font_size=40, color=color or self.C_RIGHT).move_to(pos)

    def _cross(self, pos, color=None):
        """✗ 叉号"""
        return Text("✗", font_size=40, color=color or self.C_WRONG).move_to(pos)

    # =========================================================
    # § Scene 1: 开场 Hook
    # =========================================================
    def scene_1_hook(self):
        self.author_info = self._author()
        self.play(FadeIn(self.author_info, shift=DOWN * 0.15), run_time=0.3)

        # 大问号引入
        q1 = MathTex(r"\sqrt{9} = \;?", font_size=72, color=self.C_TITLE).move_to(UP * 5.0)
        self.play(Write(q1), run_time=0.8)

        # 揭示答案 = 3
        ans1 = MathTex(r"\sqrt{9} = 3", font_size=72, color=self.C_POS).move_to(UP * 5.0)
        self.play(TransformMatchingTex(q1, ans1), run_time=0.7)
        self.wait(0.3)

        # 第二问：那 √((-3)²) 呢？
        q2_bg = self._card(7.5, 1.8, UP * 3.2, self.C_NEG, "#1a0a0a")
        q2_line1 = Text(
            "那这个呢？", font="PingFang SC", font_size=28, color=WHITE,
        ).move_to(UP * 3.5)
        q2_formula = MathTex(
            r"\sqrt{(-3)^2} = \;?",
            font_size=52, color=self.C_NEG,
        ).move_to(UP * 3.0)

        self.play(FadeIn(q2_bg), run_time=0.3)
        self.play(FadeIn(q2_line1), run_time=0.3)
        self.play(Write(q2_formula), run_time=0.7)

        # 错误猜测：= -3？
        wrong_guess = MathTex(r"= -3 \;?", font_size=52, color=GRAY_A).move_to(UP * 1.7)
        self.play(FadeIn(wrong_guess, shift=RIGHT * 0.3), run_time=0.5)

        # 大红叉否定
        big_cross = Text("✗", font_size=80, color=self.C_WRONG).move_to(UP * 1.0)
        self.play(FadeIn(big_cross, scale=0.3), run_time=0.4)
        self.play(Flash(big_cross, color=self.C_WRONG, flash_radius=0.5), run_time=0.3)
        self.wait(0.4)

        # 正确是 = 3！
        correct_hint = MathTex(
            r"\sqrt{(-3)^2} = 3", font_size=52, color=self.C_POS,
        ).move_to(ORIGIN)
        self.play(Write(correct_hint), run_time=0.6)

        hook_note = Text(
            "为什么？—— 性质2告诉你！",
            font="PingFang SC", font_size=26, color=self.C_TITLE,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(hook_note, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(ans1), FadeOut(q2_bg), FadeOut(q2_line1),
            FadeOut(q2_formula), FadeOut(wrong_guess), FadeOut(big_cross),
            FadeOut(correct_hint), FadeOut(hook_note),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 2: 快速回顾——二次根式定义
    # =========================================================
    def scene_2_review(self):
        title = self._title("二次根式回顾", color="#AAAAFF", y=5.8)
        self.play(FadeIn(title), run_time=0.35)

        def_card = self._card(7.8, 3.6, UP * 3.6, "#AAAAFF", "#0d0d1a")

        def_label = Text(
            "二次根式的定义",
            font="PingFang SC", font_size=26, color="#AAAAFF",
        ).move_to(UP * 4.8)

        def_formula = MathTex(
            r"\sqrt{a} \quad (a \geq 0)",
            font_size=48, color=WHITE,
        ).move_to(UP * 4.2)

        def_note1 = Text(
            "√ 叫根号，a 叫被开方数",
            font="PingFang SC", font_size=22, color=GRAY_A,
        ).move_to(UP * 3.6)

        def_note2 = Text(
            "⚠  被开方数 a 必须 ≥ 0",
            font="PingFang SC", font_size=22, color=self.C_NEG,
        ).move_to(UP * 3.1)

        self.play(FadeIn(def_card), run_time=0.3)
        self.play(FadeIn(def_label), run_time=0.3)
        self.play(Write(def_formula), run_time=0.6)
        self.play(FadeIn(def_note1), FadeIn(def_note2), run_time=0.5)
        self.wait(1.0)

        # 两条性质预告
        preview_card = self._card(7.8, 2.2, UP * 1.5, self.C_TITLE)
        preview_title = Text(
            "今天学习两条核心性质",
            font="PingFang SC", font_size=24, color=self.C_TITLE,
        ).move_to(UP * 2.1)
        p1_row = VGroup(
            Text("性质1：", font="PingFang SC", font_size=22, color=self.C_P1),
            MathTex(r"(\sqrt{a})^2 = a \quad (a \geq 0)",
                    font_size=30, color=self.C_P1),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.5)
        p2_row = VGroup(
            Text("性质2：", font="PingFang SC", font_size=22, color=self.C_P2),
            MathTex(r"\sqrt{a^2} = |a|",
                    font_size=30, color=self.C_P2),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.9)

        self.play(FadeIn(preview_card), run_time=0.3)
        self.play(FadeIn(preview_title), run_time=0.3)
        self.play(FadeIn(p1_row), run_time=0.4)
        self.play(FadeIn(p2_row), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(def_card), FadeOut(def_label),
            FadeOut(def_formula), FadeOut(def_note1), FadeOut(def_note2),
            FadeOut(preview_card), FadeOut(preview_title),
            FadeOut(p1_row), FadeOut(p2_row),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 3: 性质1 —— (√a)² = a
    # =========================================================
    def scene_3_prop1(self):
        title = self._title("性质 1", color=self.C_P1, y=6.0)
        self.play(FadeIn(title), run_time=0.35)

        # 核心公式
        main_formula = MathTex(
            r"(\sqrt{a})^2 = a",
            font_size=68, color=self.C_P1,
        ).move_to(UP * 4.9)
        domain = MathTex(
            r"(a \geq 0)",
            font_size=36, color=GRAY_A,
        ).next_to(main_formula, DOWN, buff=0.15)

        box = SurroundingRectangle(
            main_formula, color=self.C_P1, buff=0.22, corner_radius=0.12,
        )
        self.play(Write(main_formula), run_time=0.9)
        self.play(FadeIn(domain), Create(box), run_time=0.4)

        # ── 语言解读 ─────────────────────────────────────
        interp = Text(
            "先开根 → 再平方 → 回到原数",
            font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(UP * 3.6)
        self.play(FadeIn(interp), run_time=0.4)

        # ── 例子：(√9)² ──────────────────────────────────
        ex1_card = self._card(7.8, 2.0, UP * 2.3, self.C_P1)
        ex1_label = Text(
            "验证：", font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(UP * 2.75 + LEFT * 2.8)

        ex1_step1 = MathTex(
            r"(\sqrt{9})^2", font_size=44, color=WHITE,
        ).move_to(UP * 2.3 + LEFT * 1.8)
        ex1_eq1 = MathTex(r"=", font_size=40, color=GRAY_A).next_to(ex1_step1, RIGHT, buff=0.15)
        ex1_step2 = MathTex(r"3^2", font_size=44, color=self.C_POS).next_to(ex1_eq1, RIGHT, buff=0.15)
        ex1_eq2   = MathTex(r"=", font_size=40, color=GRAY_A).next_to(ex1_step2, RIGHT, buff=0.15)
        ex1_step3 = MathTex(r"9", font_size=44, color=self.C_P1).next_to(ex1_eq2, RIGHT, buff=0.15)
        check1    = self._check(ex1_step3.get_right() + RIGHT * 0.4, self.C_RIGHT)

        self.play(FadeIn(ex1_card), FadeIn(ex1_label), run_time=0.3)
        self.play(FadeIn(ex1_step1), run_time=0.3)
        self.play(FadeIn(ex1_eq1), FadeIn(ex1_step2), run_time=0.3)
        self.play(FadeIn(ex1_eq2), FadeIn(ex1_step3), run_time=0.3)
        self.play(FadeIn(check1), run_time=0.2)

        # ── 例子：(√5)² ──────────────────────────────────
        ex2_card = self._card(7.8, 1.6, UP * 0.9, self.C_P1)
        ex2 = MathTex(
            r"(\sqrt{5})^2 = 5",
            font_size=44, color=self.C_P1,
        ).move_to(UP * 0.9 + LEFT * 0.5)
        check2 = self._check(ex2.get_right() + RIGHT * 0.4, self.C_RIGHT)

        self.play(FadeIn(ex2_card), Write(ex2), run_time=0.5)
        self.play(FadeIn(check2), run_time=0.2)

        # ── 口诀 ─────────────────────────────────────────
        mnemonic_card = self._card(7.8, 1.4, DOWN * 0.5, self.C_TITLE, "#1a1a0a")
        mnemonic = Text(
            '口诀："先根后方，回到原样"',
            font="PingFang SC", font_size=24, color=self.C_TITLE,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(mnemonic_card), FadeIn(mnemonic), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(main_formula), FadeOut(domain), FadeOut(box),
            FadeOut(interp), FadeOut(ex1_card), FadeOut(ex1_label),
            FadeOut(ex1_step1), FadeOut(ex1_eq1), FadeOut(ex1_step2),
            FadeOut(ex1_eq2), FadeOut(ex1_step3), FadeOut(check1),
            FadeOut(ex2_card), FadeOut(ex2), FadeOut(check2),
            FadeOut(mnemonic_card), FadeOut(mnemonic),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 4: 性质2引入——揭示陷阱
    # =========================================================
    def scene_4_prop2_trap(self):
        title = self._title("性质 2  —  先看一个陷阱！", color=self.C_P2, y=6.0)
        self.play(FadeIn(title), run_time=0.35)

        # 错误猜测展示
        wrong_card = self._card(7.8, 1.8, UP * 4.8, GRAY_B, "#0d0d1a")
        wrong_label = Text(
            "很多同学会这样认为：",
            font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(UP * 5.2)
        wrong_formula = MathTex(
            r"\sqrt{a^2} \stackrel{?}{=} a",
            font_size=52, color=GRAY_A,
        ).move_to(UP * 4.7)

        self.play(FadeIn(wrong_card), FadeIn(wrong_label), run_time=0.3)
        self.play(Write(wrong_formula), run_time=0.6)

        # ── a = 3：验证（绿色通过）────────────────────────
        case_a_card = self._card(7.8, 2.0, UP * 3.0, self.C_POS, "#0a1a0a")
        case_a_label = Text(
            "当 a = 3 时：", font="PingFang SC",
            font_size=24, color=self.C_POS,
        ).move_to(UP * 3.5 + LEFT * 2.2)

        case_a_formula = MathTex(
            r"\sqrt{3^2} = \sqrt{9} = 3",
            font_size=42, color=WHITE,
        ).move_to(UP * 3.0)
        case_a_result = MathTex(
            r"= a = 3 \quad",
            font_size=38, color=self.C_POS,
        ).next_to(case_a_formula, RIGHT, buff=0.15)
        check_a = self._check(case_a_result.get_right() + RIGHT * 0.2, self.C_RIGHT)

        self.play(FadeIn(case_a_card), FadeIn(case_a_label), run_time=0.3)
        self.play(Write(case_a_formula), run_time=0.5)
        self.play(FadeIn(case_a_result), FadeIn(check_a), run_time=0.3)

        # ── a = -3：验证（红色报错）───────────────────────
        case_b_card = self._card(7.8, 2.2, UP * 1.1, self.C_NEG, "#1a0a0a")
        case_b_label = Text(
            "当 a = -3 时：", font="PingFang SC",
            font_size=24, color=self.C_NEG,
        ).move_to(UP * 1.7 + LEFT * 2.0)

        case_b_formula = MathTex(
            r"\sqrt{(-3)^2} = \sqrt{9} = 3",
            font_size=40, color=WHITE,
        ).move_to(UP * 1.2)

        # 错误结论 ≠ a = -3
        wrong_concl = MathTex(
            r"\neq a = -3 \;!",
            font_size=40, color=self.C_WRONG,
        ).move_to(UP * 0.5)
        cross_b = self._cross(wrong_concl.get_right() + RIGHT * 0.4, self.C_WRONG)

        self.play(FadeIn(case_b_card), FadeIn(case_b_label), run_time=0.3)
        self.play(Write(case_b_formula), run_time=0.5)
        self.play(
            Write(wrong_concl),
            FadeIn(cross_b),
            run_time=0.5,
        )
        self.play(Flash(wrong_concl, color=self.C_WRONG, flash_radius=0.4), run_time=0.3)

        # ── 引出正确答案 ─────────────────────────────────
        reveal_card = self._card(7.8, 1.6, DOWN * 1.0, self.C_ABS, "#1a1800")
        reveal_text = VGroup(
            Text("真相：答案是 ", font="PingFang SC",
                 font_size=28, color=WHITE),
            MathTex(r"|a|", font_size=44, color=self.C_ABS),
            Text(" ！", font="PingFang SC", font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.0)

        self.play(FadeIn(reveal_card), run_time=0.3)
        self.play(FadeIn(reveal_text, scale=1.1), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(wrong_card), FadeOut(wrong_label),
            FadeOut(wrong_formula), FadeOut(case_a_card), FadeOut(case_a_label),
            FadeOut(case_a_formula), FadeOut(case_a_result), FadeOut(check_a),
            FadeOut(case_b_card), FadeOut(case_b_label), FadeOut(case_b_formula),
            FadeOut(wrong_concl), FadeOut(cross_b),
            FadeOut(reveal_card), FadeOut(reveal_text),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 5: 性质2完整 —— √(a²) = |a|，数轴分类讨论
    # =========================================================
    def scene_5_prop2_full(self):
        title = self._title("性质 2  完整版", color=self.C_P2, y=6.0)
        self.play(FadeIn(title), run_time=0.35)

        # ── 核心公式 ─────────────────────────────────────
        main_formula = MathTex(
            r"\sqrt{a^2} = |a|",
            font_size=68, color=self.C_P2,
        ).move_to(UP * 5.0)
        domain_note = Text(
            "（对所有实数 a 都成立）",
            font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(UP * 4.3)
        box2 = SurroundingRectangle(
            main_formula, color=self.C_P2, buff=0.22, corner_radius=0.12,
        )
        self.play(Write(main_formula), run_time=0.9)
        self.play(FadeIn(domain_note), Create(box2), run_time=0.4)

        # ── 数轴 ─────────────────────────────────────────
        nl = NumberLine(
            x_range=[-4, 4, 1],
            length=7.5,
            include_numbers=True,
            numbers_to_include=[-3, -2, -1, 0, 1, 2, 3],
            include_tip=True,
            tip_height=0.18,
            tip_width=0.14,
            font_size=24,
        ).move_to(UP * 3.1)

        self.play(Create(nl), run_time=0.8)

        # ── a = 3 在数轴上 ────────────────────────────────
        pos3 = nl.n2p(3)
        dot_pos3 = Dot(pos3, radius=0.12, color=self.C_POS)
        lbl_pos3 = MathTex(r"a=3", font_size=26, color=self.C_POS).next_to(dot_pos3, UP, buff=0.15)
        self.play(FadeIn(dot_pos3), FadeIn(lbl_pos3), run_time=0.3)

        # ── a = -3 在数轴上 ───────────────────────────────
        pos_neg3 = nl.n2p(-3)
        dot_neg3 = Dot(pos_neg3, radius=0.12, color=self.C_NEG)
        lbl_neg3 = MathTex(r"a=-3", font_size=26, color=self.C_NEG).next_to(dot_neg3, UP, buff=0.15)
        self.play(FadeIn(dot_neg3), FadeIn(lbl_neg3), run_time=0.3)

        # 两点结果相同：折叠到同一绝对值 3
        result_arrow_pos = CurvedArrow(
            pos3 + UP * 0.08,
            nl.n2p(3) + UP * 0.7,
            color=self.C_POS, angle=-0.8,
        )
        result_arrow_neg = CurvedArrow(
            pos_neg3 + UP * 0.08,
            nl.n2p(3) + UP * 0.7,
            color=self.C_NEG, angle=0.8,
        )
        abs_result = MathTex(r"|a| = 3", font_size=32, color=self.C_ABS).move_to(
            nl.n2p(3) + UP * 1.1
        )

        self.play(Create(result_arrow_pos), Create(result_arrow_neg), run_time=0.7)
        self.play(FadeIn(abs_result), run_time=0.4)
        self.wait(0.5)

        # ── 分类讨论卡片 ─────────────────────────────────
        # 分两半，居中放置
        case_title = Text(
            "分类讨论：",
            font="PingFang SC", font_size=28, color=self.C_ABS,
        ).move_to(UP * 1.5)
        self.play(FadeIn(case_title), run_time=0.3)

        # 当 a ≥ 0
        pos_card = self._card(3.6, 2.6, UP * 0.3 + LEFT * 1.9, self.C_POS, "#0a1a0a")
        pos_label = Text(
            "当 a ≥ 0", font="PingFang SC", font_size=24, color=self.C_POS,
        ).move_to(UP * 0.9 + LEFT * 1.9)
        pos_formula = MathTex(
            r"\sqrt{a^2} = a",
            font_size=38, color=self.C_POS,
        ).move_to(UP * 0.3 + LEFT * 1.9)
        pos_example = MathTex(
            r"\sqrt{3^2} = 3",
            font_size=28, color=GRAY_A,
        ).move_to(DOWN * 0.3 + LEFT * 1.9)

        # 当 a < 0
        neg_card = self._card(3.6, 2.6, UP * 0.3 + RIGHT * 1.9, self.C_NEG, "#1a0a0a")
        neg_label = Text(
            "当 a < 0", font="PingFang SC", font_size=24, color=self.C_NEG,
        ).move_to(UP * 0.9 + RIGHT * 1.9)
        neg_formula = MathTex(
            r"\sqrt{a^2} = -a",
            font_size=38, color=self.C_NEG,
        ).move_to(UP * 0.3 + RIGHT * 1.9)
        neg_example = MathTex(
            r"\sqrt{(-3)^2} = 3",
            font_size=28, color=GRAY_A,
        ).move_to(DOWN * 0.3 + RIGHT * 1.9)

        self.play(FadeIn(pos_card), FadeIn(neg_card), run_time=0.3)
        self.play(FadeIn(pos_label), FadeIn(neg_label), run_time=0.3)
        self.play(Write(pos_formula), Write(neg_formula), run_time=0.6)
        self.play(FadeIn(pos_example), FadeIn(neg_example), run_time=0.4)

        # 注意：a<0时 -a 是正数
        neg_note = Text(
            "注意：a<0 时，-a > 0（是正数）",
            font="PingFang SC", font_size=22, color=self.C_NEG,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(neg_note), run_time=0.4)
        self.wait(1.8)

        # 清场
        self.play(
            FadeOut(title), FadeOut(main_formula), FadeOut(domain_note), FadeOut(box2),
            FadeOut(nl), FadeOut(dot_pos3), FadeOut(lbl_pos3),
            FadeOut(dot_neg3), FadeOut(lbl_neg3),
            FadeOut(result_arrow_pos), FadeOut(result_arrow_neg), FadeOut(abs_result),
            FadeOut(case_title),
            FadeOut(pos_card), FadeOut(pos_label), FadeOut(pos_formula), FadeOut(pos_example),
            FadeOut(neg_card), FadeOut(neg_label), FadeOut(neg_formula), FadeOut(neg_example),
            FadeOut(neg_note),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 6: 易错点辨析
    # =========================================================
    def scene_6_pitfall(self):
        title = self._title("⚠  易错辨析", color=self.C_NEG, y=6.0)
        self.play(FadeIn(title), run_time=0.35)

        sub = Text(
            "以下哪些写法正确？",
            font="PingFang SC", font_size=26, color=GRAY_A,
        ).move_to(UP * 5.1)
        self.play(FadeIn(sub), run_time=0.3)

        # 4个案例：对错各半
        cases = [
            # (公式文本,  是否正确, y位置)
            (r"\sqrt{(-5)^2} = -5",   False, UP * 4.0),
            (r"\sqrt{(-5)^2} = 5",    True,  UP * 3.0),
            (r"\sqrt{(-2)^2} = |-2| = 2", True,  UP * 2.0),
            (r"\sqrt{4} = -2",        False, UP * 1.0),
        ]

        for formula_str, is_correct, ypos in cases:
            color = self.C_RIGHT if is_correct else self.C_WRONG
            bg_color = "#0a1a0a" if is_correct else "#1a0a0a"
            border = self.C_POS if is_correct else self.C_NEG

            card = self._card(7.5, 0.85, ypos, border, bg_color)
            formula = MathTex(formula_str, font_size=34, color=WHITE).move_to(
                ypos + LEFT * 1.0
            )
            mark = (self._check if is_correct else self._cross)(
                ypos + RIGHT * 3.0, color
            )
            self.play(FadeIn(card), run_time=0.2)
            self.play(Write(formula), FadeIn(mark), run_time=0.4)

        # 核心提醒
        reminder_card = self._card(7.8, 2.0, DOWN * 1.2, self.C_ABS, "#1a1800")
        reminder_t = Text(
            "记住：", font="PingFang SC", font_size=26, color=self.C_ABS,
        ).move_to(DOWN * 0.7 + LEFT * 2.5)
        # Use VGroup to combine MathTex + Text (no Chinese in MathTex)
        reminder_f2 = VGroup(
            MathTex(r"\sqrt{a^2} = |a| \geq 0", font_size=36, color=self.C_ABS),
            Text("（恒成立）", font="PingFang SC", font_size=26, color=self.C_ABS),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.3)

        self.play(FadeIn(reminder_card), run_time=0.3)
        self.play(FadeIn(reminder_t), FadeIn(reminder_f2), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(sub),
            *[FadeOut(mob) for mob in self.mobjects
              if mob not in [self.author_info]],
            run_time=0.5,
        )

    # =========================================================
    # § Scene 7: 总结 + 片尾
    # =========================================================
    def scene_7_summary(self):
        sum_title = Text(
            "两条性质总结",
            font="PingFang SC", font_size=40, color=self.C_TITLE,
        ).move_to(UP * 5.7)
        self.play(Write(sum_title), run_time=0.5)

        # ── 性质1 卡片 ────────────────────────────────────
        c1 = self._card(8.0, 2.8, UP * 4.0, self.C_P1)
        c1_num = Text("性质 1", font="PingFang SC",
                      font_size=26, color=self.C_P1).move_to(UP * 4.7 + LEFT * 2.5)
        c1_f = MathTex(r"(\sqrt{a})^2 = a", font_size=46,
                       color=self.C_P1).move_to(UP * 4.0)
        c1_cond = MathTex(r"(a \geq 0)", font_size=30,
                          color=GRAY_A).move_to(UP * 3.4)

        c1.shift(LEFT * 11)
        c1_content = VGroup(c1_num, c1_f, c1_cond)
        c1_content.shift(LEFT * 11)
        self.play(
            VGroup(c1, c1_content).animate.shift(RIGHT * 11),
            run_time=0.4,
        )

        # ── 性质2 卡片 ────────────────────────────────────
        c2 = self._card(8.0, 2.8, UP * 1.7, self.C_P2)
        c2_num = Text("性质 2", font="PingFang SC",
                      font_size=26, color=self.C_P2).move_to(UP * 2.4 + LEFT * 2.5)
        c2_f = MathTex(r"\sqrt{a^2} = |a|", font_size=46,
                       color=self.C_P2).move_to(UP * 1.7)
        c2_cond = Text(
            "对所有实数 a 成立",
            font="PingFang SC", font_size=24, color=GRAY_A,
        ).move_to(UP * 1.1)

        c2.shift(LEFT * 11)
        c2_content = VGroup(c2_num, c2_f, c2_cond)
        c2_content.shift(LEFT * 11)
        self.play(
            VGroup(c2, c2_content).animate.shift(RIGHT * 11),
            run_time=0.4,
        )

        # ── 核心提醒 ─────────────────────────────────────
        warn_card = self._card(7.8, 2.0, DOWN * 0.7, self.C_ABS, "#1a1800")
        warn_row1 = VGroup(
            MathTex(r"\sqrt{a^2}", font_size=36, color=WHITE),
            Text("结果永远", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(r"\geq 0", font_size=36, color=self.C_ABS),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.4)
        warn_row2 = VGroup(
            Text("绝不能写成负数！",
                 font="PingFang SC", font_size=24, color=self.C_NEG),
        ).move_to(DOWN * 1.1)

        warn_card.shift(LEFT * 11)
        warn_content = VGroup(warn_row1, warn_row2)
        warn_content.shift(LEFT * 11)
        self.play(
            VGroup(warn_card, warn_content).animate.shift(RIGHT * 11),
            run_time=0.4,
        )
        self.wait(1.2)

        # ── 清除总结，进入片尾 ────────────────────────────
        self.play(
            FadeOut(sum_title),
            FadeOut(c1), FadeOut(c1_content),
            FadeOut(c2), FadeOut(c2_content),
            FadeOut(warn_card), FadeOut(warn_content),
            run_time=0.5,
        )

        # ── 片尾 ─────────────────────────────────────────
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC", font_size=42,
            color=WHITE, weight=BOLD,
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC", font_size=32, color=GRAY_B,
        ).move_to(UP * 1.1)
        divider = Line(LEFT * 3.5, RIGHT * 3.5,
                       color=GRAY_B, stroke_width=1).move_to(UP * 0.5)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC", font_size=30, color=self.C_TITLE,
        ).move_to(ORIGIN)

        # 装饰：两条公式淡显
        deco1 = MathTex(r"(\sqrt{a})^2 = a", font_size=36,
                        color="#333355").move_to(DOWN * 1.8 + LEFT * 1.5)
        deco2 = MathTex(r"\sqrt{a^2} = |a|", font_size=36,
                        color="#333355").move_to(DOWN * 2.7 + RIGHT * 0.5)

        self.play(Transform(self.author_info, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.play(FadeIn(deco1), FadeIn(deco2), run_time=0.5)
        self.wait(2.0)
        self.play(
            FadeOut(self.author_info), FadeOut(author_id),
            FadeOut(divider), FadeOut(follow),
            FadeOut(deco1), FadeOut(deco2),
            run_time=0.8,
        )


# ============================================================
# 渲染命令:
# manim -pql radical_properties.py QuadraticRadicalProperties
# manim -qh  radical_properties.py QuadraticRadicalProperties
# ============================================================
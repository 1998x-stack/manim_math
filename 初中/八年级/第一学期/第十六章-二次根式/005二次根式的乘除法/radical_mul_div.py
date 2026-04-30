"""
二次根式的乘除法 — 教学动画
目标受众: 八年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class RadicalMultDiv(Scene):
    """
    二次根式乘除法教学动画
    场景:
    1. 开场钩子
    2. 乘法公式 √a × √b = √(ab)
    3. 乘法例题 1: √3 × √5 = √15
    4. 乘法例题 2: √2 × √8 = 4（需化简）
    5. 除法公式 √a ÷ √b = √(a/b)
    6. 除法例题 1: √12 ÷ √3 = 2
    7. 分母有理化原理
    8. 分母有理化例题 1/√3 = √3/3
    9. 综合练习快速判断
    10. 总结 & 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        self.C_TITLE   = "#f9ca24"
        self.C_MUL     = "#22a6b3"   # 乘法 — 蓝
        self.C_DIV     = "#a29bfe"   # 除法 — 紫
        self.C_RESULT  = "#6ab04c"   # 结果 — 绿
        self.C_WRONG   = "#eb4d4b"   # 错误 — 红
        self.C_RATN    = "#f0932b"   # 有理化 — 橙
        self.C_FORMULA = "#badc58"   # 公式 — 亮绿
        self.C_NEUTRAL = GRAY_A

        self.scene_opening()
        self.scene_mul_formula()
        self.scene_mul_ex1()
        self.scene_mul_ex2()
        self.scene_div_formula()
        self.scene_div_ex1()
        self.scene_rationalize_intro()
        self.scene_rationalize_ex()
        self.scene_quick_practice()
        self.scene_summary()
        self.scene_outro()

    # ─────────────── 工具 ───────────────
    def card(self, w, h, col, pos, fill="#16213e", alpha=0.85):
        return RoundedRectangle(
            corner_radius=0.28, width=w, height=h,
            color=col, stroke_width=2,
            fill_color=fill, fill_opacity=alpha,
        ).move_to(pos)

    def fade_rest(self):
        self.play(
            *[FadeOut(m) for m in self.mobjects if m is not self.author],
            run_time=0.45,
        )

    # ═══════════════════════════════════════
    #  Scene 1: 开场
    # ═══════════════════════════════════════
    def scene_opening(self):
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=18, color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        chapter = Text(
            "八年级 · 第十六章 · 二次根式",
            font="PingFang SC", font_size=20, color=GRAY_B,
        ).move_to(UP * 6.55)
        self.play(FadeIn(chapter), run_time=0.3)

        hook = Text(
            "根号能相乘相除吗？",
            font="PingFang SC", font_size=42, color=self.C_TITLE,
        ).move_to(UP * 5.6)
        self.play(Write(hook), run_time=0.7)

        # 展示两道式子引发好奇
        q1_bg = self.card(3.5, 1.8, self.C_MUL, UP * 4.1 + LEFT * 2.1)
        q1_f  = MathTex(r"\sqrt{3} \times \sqrt{5} = \;?", font_size=36, color=WHITE).move_to(UP * 4.1 + LEFT * 2.1)

        q2_bg = self.card(3.5, 1.8, self.C_DIV, UP * 4.1 + RIGHT * 2.1)
        q2_f  = MathTex(r"\sqrt{12} \div \sqrt{3} = \;?", font_size=36, color=WHITE).move_to(UP * 4.1 + RIGHT * 2.1)

        self.play(
            Create(q1_bg), Write(q1_f),
            Create(q2_bg), Write(q2_f),
            run_time=0.7,
        )
        self.wait(0.8)

        # 揭晓答案
        a1 = MathTex(r"= \sqrt{15}", font_size=40, color=self.C_RESULT).move_to(UP * 2.9 + LEFT * 2.1)
        a2 = MathTex(r"= 2", font_size=40, color=self.C_RESULT).move_to(UP * 2.9 + RIGHT * 2.1)
        self.play(Write(a1), Write(a2), run_time=0.6)

        reveal = Text(
            "今天学会根式乘除运算！",
            font="PingFang SC", font_size=30, color=self.C_TITLE,
        ).move_to(UP * 1.8)
        self.play(FadeIn(reveal, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(chapter), FadeOut(hook),
            FadeOut(q1_bg), FadeOut(q1_f),
            FadeOut(q2_bg), FadeOut(q2_f),
            FadeOut(a1), FadeOut(a2), FadeOut(reveal),
            run_time=0.45,
        )

    # ═══════════════════════════════════════
    #  Scene 2: 乘法公式
    # ═══════════════════════════════════════
    def scene_mul_formula(self):
        title = Text(
            "乘法公式",
            font="PingFang SC", font_size=48, color=self.C_TITLE,
        ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.6)

        # 核心公式大字
        formula_bg = self.card(7.6, 2.2, self.C_MUL, UP * 5.1, fill="#0f2a3a", alpha=0.95)
        formula    = MathTex(
            r"\sqrt{a} \times \sqrt{b} = \sqrt{ab}",
            font_size=56, color=WHITE,
        ).move_to(UP * 5.1)
        cond = Text(
            "（a ≥ 0，b ≥ 0）",
            font="PingFang SC", font_size=22, color=GRAY_A,
        ).move_to(UP * 4.45)
        self.play(Create(formula_bg), Write(formula), run_time=0.8)
        self.play(FadeIn(cond), run_time=0.3)

        # 直觉理解：平方再开根
        intuition_bg = self.card(7.4, 2.8, self.C_MUL, UP * 2.8)
        int_title = Text(
            "直觉理解：",
            font="PingFang SC", font_size=26, color=self.C_MUL,
        )
        int_f1 = MathTex(r"(\sqrt{a})^2 = a,\quad (\sqrt{b})^2 = b", font_size=30, color=WHITE)
        int_f2 = MathTex(r"(\sqrt{a} \cdot \sqrt{b})^2 = ab", font_size=30, color=WHITE)
        int_f3 = MathTex(r"\therefore \sqrt{a} \cdot \sqrt{b} = \sqrt{ab}", font_size=30, color=self.C_TITLE)
        VGroup(int_title, int_f1, int_f2, int_f3).arrange(DOWN, buff=0.22).move_to(UP * 2.8)
        self.play(Create(intuition_bg), Write(int_title), run_time=0.4)
        self.play(Write(int_f1), run_time=0.4)
        self.play(Write(int_f2), run_time=0.4)
        self.play(Write(int_f3), run_time=0.5)

        # 延伸：多个根号
        ext_bg = self.card(7.4, 1.5, self.C_FORMULA, UP * 0.9)
        ext_t  = Text("推广：", font="PingFang SC", font_size=24, color=self.C_FORMULA)
        ext_f  = MathTex(r"\sqrt{a} \cdot \sqrt{b} \cdot \sqrt{c} = \sqrt{abc}", font_size=34, color=WHITE)
        VGroup(ext_t, ext_f).arrange(RIGHT, buff=0.3).move_to(UP * 0.9)
        self.play(Create(ext_bg), Write(ext_t), Write(ext_f), run_time=0.6)

        # 注意事项
        warn_bg = self.card(7.4, 1.4, self.C_WRONG, DOWN * 0.4, fill="#2d0a0a", alpha=0.9)
        warn_t  = Text(
            "⚠ 运算结果必须化成最简二次根式！",
            font="PingFang SC", font_size=24, color=self.C_WRONG,
        ).move_to(DOWN * 0.4)
        self.play(Create(warn_bg), Write(warn_t), run_time=0.6)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 3: 乘法例题 1
    # ═══════════════════════════════════════
    def scene_mul_ex1(self):
        title = Text(
            "例题 1  乘法计算",
            font="PingFang SC", font_size=36, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_MUL, UP * 5.5)
        prob_l  = Text("计算：", font="PingFang SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{3} \times \sqrt{5}", font_size=54, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 套用公式
        step_bg = self.card(7.2, 1.8, self.C_MUL, UP * 4.1)
        step_tag = Text("套用公式：", font="PingFang SC", font_size=24, color=self.C_MUL)
        step_f   = MathTex(r"\sqrt{a} \times \sqrt{b} = \sqrt{ab}", font_size=34, color=GRAY_A)
        VGroup(step_tag, step_f).arrange(DOWN, buff=0.15).move_to(UP * 4.1)
        self.play(Create(step_bg), Write(step_tag), Write(step_f), run_time=0.6)

        # 推导步骤
        s1 = MathTex(r"\sqrt{3} \times \sqrt{5}", font_size=54, color=WHITE).move_to(UP * 2.8)
        s2 = MathTex(r"= \sqrt{3 \times 5}", font_size=54, color=GRAY_A).move_to(UP * 1.8)
        s3 = MathTex(r"= \sqrt{15}", font_size=64, color=self.C_RESULT).move_to(UP * 0.7)

        self.play(Write(s1), run_time=0.4)
        self.play(Write(s2), run_time=0.4)
        self.play(Write(s3), run_time=0.5)

        ans_bg = self.card(6.5, 1.6, self.C_RESULT, DOWN * 0.5, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{3} \times \sqrt{5} = \sqrt{15}", font_size=46, color=WHITE).move_to(DOWN * 0.5)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)

        note = Text(
            "√15 已是最简（15无完全平方因数）",
            font="PingFang SC", font_size=22, color=GRAY_A,
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 4: 乘法例题 2（需化简）
    # ═══════════════════════════════════════
    def scene_mul_ex2(self):
        title = Text(
            "例题 2  乘法后需化简",
            font="PingFang SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_MUL, UP * 5.5)
        prob_l  = Text("计算：", font="PingFang SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{2} \times \sqrt{8}", font_size=54, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 方法一：直接乘
        m1_bg  = self.card(7.2, 1.5, self.C_MUL, UP * 4.2)
        m1_tag = Text("方法一：直接合并", font="PingFang SC", font_size=24, color=self.C_MUL)
        m1_f   = MathTex(r"\sqrt{2} \times \sqrt{8} = \sqrt{16} = 4", font_size=36, color=WHITE)
        VGroup(m1_tag, m1_f).arrange(DOWN, buff=0.15).move_to(UP * 4.2)
        self.play(Create(m1_bg), Write(m1_tag), Write(m1_f), run_time=0.7)

        # 方法二：先化简再乘
        m2_bg  = self.card(7.2, 2.2, self.C_FORMULA, UP * 2.5)
        m2_tag = Text("方法二：先化简再乘", font="PingFang SC", font_size=24, color=self.C_FORMULA)
        m2_f1  = MathTex(r"\sqrt{8} = 2\sqrt{2}", font_size=32, color=GRAY_A)
        m2_f2  = MathTex(r"\sqrt{2} \times 2\sqrt{2} = 2 \times 2 = 4", font_size=32, color=WHITE)
        VGroup(m2_tag, m2_f1, m2_f2).arrange(DOWN, buff=0.18).move_to(UP * 2.5)
        self.play(Create(m2_bg), Write(m2_tag), Write(m2_f1), Write(m2_f2), run_time=0.8)

        # 关键点
        key_bg = self.card(7.4, 2.0, self.C_WRONG, UP * 0.85, fill="#2d0a0a", alpha=0.9)
        key_t1 = Text("关键：", font="PingFang SC", font_size=26, color=self.C_WRONG)
        key_f1 = MathTex(r"\sqrt{16} = 4", font_size=36, color=WHITE)
        key_t2 = Text("完全平方数开方后是整数！", font="PingFang SC", font_size=22, color=GRAY_A)
        VGroup(key_t1, key_f1, key_t2).arrange(DOWN, buff=0.15).move_to(UP * 0.85)
        self.play(Create(key_bg), Write(key_t1), Write(key_f1), FadeIn(key_t2), run_time=0.7)

        ans_bg = self.card(6.5, 1.5, self.C_RESULT, DOWN * 0.75, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{2} \times \sqrt{8} = 4", font_size=50, color=WHITE).move_to(DOWN * 0.75)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 5: 除法公式
    # ═══════════════════════════════════════
    def scene_div_formula(self):
        title = Text(
            "除法公式",
            font="PingFang SC", font_size=48, color=self.C_TITLE,
        ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.6)

        # 核心公式
        formula_bg = self.card(7.6, 2.2, self.C_DIV, UP * 5.1, fill="#1a0f3a", alpha=0.95)
        formula    = MathTex(
            r"\sqrt{a} \div \sqrt{b} = \sqrt{\dfrac{a}{b}}",
            font_size=52, color=WHITE,
        ).move_to(UP * 5.1)
        cond = Text(
            "（a ≥ 0，b > 0）",
            font="PingFang SC", font_size=22, color=GRAY_A,
        ).move_to(UP * 4.4)
        self.play(Create(formula_bg), Write(formula), run_time=0.8)
        self.play(FadeIn(cond), run_time=0.3)

        # 等价写法
        equiv_bg = self.card(7.4, 1.8, self.C_DIV, UP * 3.3)
        equiv_t  = Text("等价写法：", font="PingFang SC", font_size=24, color=self.C_DIV)
        equiv_f  = MathTex(
            r"\dfrac{\sqrt{a}}{\sqrt{b}} = \sqrt{\dfrac{a}{b}}",
            font_size=44, color=WHITE,
        )
        VGroup(equiv_t, equiv_f).arrange(RIGHT, buff=0.3).move_to(UP * 3.3)
        self.play(Create(equiv_bg), Write(equiv_t), Write(equiv_f), run_time=0.7)

        # 对称性对比
        sym_bg = self.card(7.4, 2.8, self.C_MUL, UP * 1.5)
        sym_t  = Text("对比乘法与除法：", font="PingFang SC", font_size=24, color=self.C_MUL)
        sym_f1 = MathTex(r"\sqrt{a} \times \sqrt{b} = \sqrt{ab}", font_size=34, color=WHITE)
        sym_f2 = MathTex(r"\sqrt{a} \div \sqrt{b} = \sqrt{\dfrac{a}{b}}", font_size=34, color=self.C_TITLE)
        VGroup(sym_t, sym_f1, sym_f2).arrange(DOWN, buff=0.3).move_to(UP * 1.5)
        self.play(Create(sym_bg), Write(sym_t), Write(sym_f1), Write(sym_f2), run_time=0.8)

        # 记忆口诀
        mnemonic_bg = self.card(7.4, 1.4, self.C_TITLE, DOWN * 0.5, fill="#1a1000", alpha=0.9)
        mnemonic_t  = Text(
            "口诀：根号内可以乘，也可以除！",
            font="PingFang SC", font_size=26, color=self.C_TITLE,
        ).move_to(DOWN * 0.5)
        self.play(Create(mnemonic_bg), Write(mnemonic_t), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 6: 除法例题
    # ═══════════════════════════════════════
    def scene_div_ex1(self):
        title = Text(
            "例题 3  除法计算",
            font="PingFang SC", font_size=36, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_DIV, UP * 5.5)
        prob_l  = Text("计算：", font="PingFang SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{12} \div \sqrt{3}", font_size=54, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 方法一：套公式
        m1_bg  = self.card(7.2, 2.0, self.C_DIV, UP * 4.0)
        m1_tag = Text("方法一：套公式", font="PingFang SC", font_size=24, color=self.C_DIV)
        m1_f1  = MathTex(r"= \sqrt{\dfrac{12}{3}}", font_size=44, color=WHITE)
        m1_f2  = MathTex(r"= \sqrt{4} = 2", font_size=44, color=self.C_RESULT)
        VGroup(m1_tag, m1_f1, m1_f2).arrange(DOWN, buff=0.18).move_to(UP * 4.0)
        self.play(Create(m1_bg), Write(m1_tag), Write(m1_f1), Write(m1_f2), run_time=0.8)

        # 方法二：先化简
        m2_bg  = self.card(7.2, 2.2, self.C_FORMULA, UP * 2.1)
        m2_tag = Text("方法二：先化简", font="PingFang SC", font_size=24, color=self.C_FORMULA)
        m2_f1  = MathTex(r"\sqrt{12} = 2\sqrt{3}", font_size=34, color=GRAY_A)
        m2_f2  = MathTex(r"\dfrac{2\sqrt{3}}{\sqrt{3}} = 2", font_size=38, color=WHITE)
        VGroup(m2_tag, m2_f1, m2_f2).arrange(DOWN, buff=0.18).move_to(UP * 2.1)
        self.play(Create(m2_bg), Write(m2_tag), Write(m2_f1), Write(m2_f2), run_time=0.8)

        ans_bg = self.card(6.5, 1.5, self.C_RESULT, UP * 0.3, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{12} \div \sqrt{3} = 2", font_size=50, color=WHITE).move_to(UP * 0.3)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)

        note = Text(
            "12 ÷ 3 = 4，√4 = 2，得到整数！",
            font="PingFang SC", font_size=22, color=GRAY_A,
        ).move_to(DOWN * 0.9)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 7: 分母有理化原理
    # ═══════════════════════════════════════
    def scene_rationalize_intro(self):
        title = Text(
            "分母有理化",
            font="PingFang SC", font_size=48, color=self.C_TITLE,
        ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.6)

        # 问题：分母有根号不是最简
        prob_bg = self.card(7.4, 2.0, self.C_WRONG, UP * 5.1, fill="#2d0a0a", alpha=0.9)
        prob_t1 = Text("分母含根号，不是最简！", font="PingFang SC", font_size=26, color=self.C_WRONG)
        prob_f  = MathTex(r"\dfrac{1}{\sqrt{3}} \;\longrightarrow\; \text{???}", font_size=44, color=WHITE)
        VGroup(prob_t1, prob_f).arrange(DOWN, buff=0.2).move_to(UP * 5.1)
        self.play(Create(prob_bg), Write(prob_t1), Write(prob_f), run_time=0.8)

        # 核心思路
        idea_bg = self.card(7.4, 2.8, self.C_RATN, UP * 3.1)
        idea_t  = Text("核心思路：分子分母同乘以根式", font="PingFang SC", font_size=24, color=self.C_RATN)
        idea_f1 = MathTex(r"\dfrac{1}{\sqrt{3}} = \dfrac{1 \times \sqrt{3}}{\sqrt{3} \times \sqrt{3}}", font_size=36, color=WHITE)
        idea_f2 = MathTex(r"= \dfrac{\sqrt{3}}{(\sqrt{3})^2} = \dfrac{\sqrt{3}}{3}", font_size=36, color=self.C_RESULT)
        VGroup(idea_t, idea_f1, idea_f2).arrange(DOWN, buff=0.25).move_to(UP * 3.1)
        self.play(Create(idea_bg), Write(idea_t), Write(idea_f1), Write(idea_f2), run_time=0.9)

        # 乘法公式说明
        why_bg = self.card(7.4, 1.6, self.C_MUL, UP * 1.25)
        why_t  = Text("为什么乘以 √3？", font="PingFang SC", font_size=24, color=self.C_MUL)
        why_f  = MathTex(r"\sqrt{3} \times \sqrt{3} = 3 \quad (\text{integer!})", font_size=34, color=WHITE)
        VGroup(why_t, why_f).arrange(DOWN, buff=0.15).move_to(UP * 1.25)
        self.play(Create(why_bg), Write(why_t), Write(why_f), run_time=0.7)

        # 通用公式
        gen_bg = self.card(7.4, 1.8, self.C_FORMULA, DOWN * 0.3, fill="#0f2a0a", alpha=0.95)
        gen_t  = Text("通用公式：", font="PingFang SC", font_size=24, color=self.C_FORMULA)
        gen_f  = MathTex(r"\dfrac{1}{\sqrt{a}} = \dfrac{\sqrt{a}}{a} \quad (a > 0)", font_size=38, color=WHITE)
        VGroup(gen_t, gen_f).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.3)
        self.play(Create(gen_bg), Write(gen_t), Write(gen_f), run_time=0.7)
        self.wait(2.5)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 8: 分母有理化例题
    # ═══════════════════════════════════════
    def scene_rationalize_ex(self):
        title = Text(
            "例题 4  分母有理化",
            font="PingFang SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_RATN, UP * 5.55)
        prob_l  = Text("化简：", font="PingFang SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\dfrac{6}{\sqrt{3}}", font_size=58, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.55)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 逐步
        s_bg = self.card(7.2, 4.0, self.C_RATN, UP * 3.4)
        s1 = MathTex(r"\dfrac{6}{\sqrt{3}}", font_size=50, color=WHITE)
        arr1 = MathTex(r"=", font_size=40, color=GRAY_A)
        s2 = MathTex(r"\dfrac{6 \times \sqrt{3}}{\sqrt{3} \times \sqrt{3}}", font_size=44, color=WHITE)
        step1_label = Text("分子分母同乘 √3", font="PingFang SC", font_size=20, color=self.C_RATN)
        row1 = VGroup(s1, arr1, s2).arrange(RIGHT, buff=0.3)

        arr2 = MathTex(r"=", font_size=40, color=GRAY_A)
        s3   = MathTex(r"\dfrac{6\sqrt{3}}{3}", font_size=50, color=WHITE)
        step2_label = Text("分母 √3×√3=3", font="PingFang SC", font_size=20, color=self.C_RATN)
        row2 = VGroup(arr2, s3).arrange(RIGHT, buff=0.3)

        arr3 = MathTex(r"=", font_size=40, color=GRAY_A)
        s4   = MathTex(r"2\sqrt{3}", font_size=58, color=self.C_RESULT)
        step3_label = Text("约分 6÷3=2", font="PingFang SC", font_size=20, color=self.C_RATN)
        row3 = VGroup(arr3, s4).arrange(RIGHT, buff=0.3)

        VGroup(row1, row2, row3).arrange(DOWN, buff=0.35).move_to(UP * 3.4)

        self.play(Create(s_bg), run_time=0.3)
        self.play(Write(row1), FadeIn(step1_label.next_to(row1, RIGHT, buff=0.2)), run_time=0.6)
        self.wait(0.3)
        self.play(Write(row2), FadeIn(step2_label.next_to(row2, RIGHT, buff=0.2)), run_time=0.5)
        self.wait(0.3)
        self.play(Write(row3), FadeIn(step3_label.next_to(row3, RIGHT, buff=0.2)), run_time=0.5)

        ans_bg = self.card(7.0, 1.6, self.C_RESULT, UP * 1.35, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\dfrac{6}{\sqrt{3}} = 2\sqrt{3}", font_size=52, color=WHITE).move_to(UP * 1.35)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)

        check_bg = self.card(7.2, 1.8, self.C_FORMULA, DOWN * 0.05)
        check_t1 = Text("验证：分母无根号，被开方数无完全平方因数", font="PingFang SC", font_size=20, color=self.C_FORMULA)
        check_f  = MathTex(r"2\sqrt{3} \;\checkmark", font_size=36, color=self.C_RESULT)
        VGroup(check_t1, check_f).arrange(DOWN, buff=0.15).move_to(DOWN * 0.05)
        self.play(Create(check_bg), Write(check_t1), Write(check_f), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 9: 综合练习
    # ═══════════════════════════════════════
    def scene_quick_practice(self):
        title = Text(
            "综合练习",
            font="PingFang SC", font_size=44, color=self.C_TITLE,
        ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.5)

        # (题目, 结果, 颜色, 提示)
        items = [
            (r"\sqrt{6} \times \sqrt{6}",   r"= 6",          self.C_MUL,    "√6×√6=6"),
            (r"\sqrt{5} \times \sqrt{20}",  r"= 10",         self.C_MUL,    "√100=10"),
            (r"\sqrt{18} \div \sqrt{2}",    r"= 3",          self.C_DIV,    "√9=3"),
            (r"\dfrac{4}{\sqrt{2}}",        r"= 2\sqrt{2}",  self.C_RATN,   "有理化"),
        ]

        card_h  = 1.72
        start_y = 5.4
        gap     = 1.80

        for i, (prob, result, col, hint) in enumerate(items):
            pos_y = start_y - i * gap
            pos   = UP * pos_y

            bg     = self.card(7.6, card_h, col, pos)
            prob_f = MathTex(prob,   font_size=38, color=WHITE)
            res_f  = MathTex(result, font_size=38, color=self.C_RESULT)
            hint_t = Text(hint, font="PingFang SC", font_size=20, color=GRAY_A)
            top    = VGroup(prob_f, res_f).arrange(RIGHT, buff=0.4)
            VGroup(top, hint_t).arrange(DOWN, buff=0.12).move_to(pos)

            self.play(Create(bg), run_time=0.18)
            self.play(Write(prob_f), run_time=0.30)
            self.play(Write(res_f), FadeIn(hint_t), run_time=0.35)
            self.wait(0.25)

        self.wait(1.5)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 10: 总结
    # ═══════════════════════════════════════
    def scene_summary(self):
        title = Text(
            "知识点总结",
            font="PingFang SC", font_size=46, color=self.C_TITLE,
        ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.5)

        blocks = [
            (self.C_MUL,   UP * 5.5,  "乘法公式",
             r"\sqrt{a} \times \sqrt{b} = \sqrt{ab}"),
            (self.C_DIV,   UP * 3.95, "除法公式",
             r"\sqrt{a} \div \sqrt{b} = \sqrt{a/b}"),
            (self.C_RATN,  UP * 2.4,  "分母有理化",
             r"\dfrac{1}{\sqrt{a}} = \dfrac{\sqrt{a}}{a}"),
            (self.C_WRONG, UP * 0.85, "注意事项",
             r"\text{result must be simplest form!}"),
            (self.C_RESULT,DOWN * 0.7,"核心例题",
             r"\sqrt{2}\times\sqrt{8}=4,\quad\frac{6}{\sqrt{3}}=2\sqrt{3}"),
        ]

        for col, pos, label_str, fml_str in blocks:
            bg  = self.card(7.6, 1.45, col, pos)
            lbl = Text(label_str, font="PingFang SC", font_size=24, color=col)
            fml = MathTex(fml_str, font_size=28, color=WHITE)
            VGroup(lbl, fml).arrange(RIGHT, buff=0.4).move_to(pos)
            self.play(Create(bg), Write(lbl), Write(fml), run_time=0.45)
            self.wait(0.18)

        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 11: 片尾
    # ═══════════════════════════════════════
    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC", font_size=38, color=WHITE,
        ).move_to(UP * 2.5)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC", font_size=28, color=GRAY_B,
        ).move_to(UP * 1.7)

        self.play(Transform(self.author, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我，学更多数学知识！",
            font="PingFang SC", font_size=30, color=self.C_TITLE,
        ).move_to(UP * 0.3)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)

        deco = VGroup(
            MathTex(r"\sqrt{a} \times \sqrt{b} = \sqrt{ab}", font_size=28, color=self.C_MUL),
            MathTex(r"\sqrt{a} \div \sqrt{b} = \sqrt{a/b}",  font_size=28, color=self.C_DIV),
            MathTex(r"\dfrac{1}{\sqrt{a}} = \dfrac{\sqrt{a}}{a}",  font_size=28, color=self.C_RATN),
        ).arrange(DOWN, buff=0.42).move_to(DOWN * 1.8)

        self.play(*[Write(f) for f in deco], run_time=1.0)
        self.play(*[Indicate(f, color=self.C_TITLE) for f in deco], run_time=0.9)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# 渲染命令：
# manim -pql radical_mul_div.py RadicalMultDiv    # 快速预览
# manim -qh  radical_mul_div.py RadicalMultDiv    # 高质量输出
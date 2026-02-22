"""
二次根式的加减法 — 教学动画
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


class RadicalAddSub(Scene):
    """
    二次根式加减法教学动画
    场景:
    1.  开场钩子       — √8+√18=? 先抛问题
    2.  核心流程       — 三步走：化简→找同类→合并
    3.  基础例题 1     — 2√2 + 3√2 = 5√2 (直接合并)
    4.  进阶例题 2     — √8 + √18 = 5√2 (先化简)
    5.  减法例题 3     — √12 - √3 = √3
    6.  混合例题 4     — √8 + √18 - √2 = 4√2
    7.  不能合并的情况  — √2 + √3 保留原式
    8.  综合练习       — 快速判断 / 计算
    9.  总结
    10. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        self.C_TITLE   = "#f9ca24"
        self.C_STEP1   = "#22a6b3"   # Step1 化简 — 蓝
        self.C_STEP2   = "#a29bfe"   # Step2 同类 — 紫
        self.C_STEP3   = "#6ab04c"   # Step3 合并 — 绿
        self.C_RESULT  = "#badc58"   # 结果  — 亮绿
        self.C_WRONG   = "#eb4d4b"   # 错误  — 红
        self.C_COEFF   = "#f0932b"   # 系数  — 橙
        self.C_NEUTRAL = GRAY_A

        self.scene_opening()
        self.scene_three_steps()
        self.scene_ex1_direct()
        self.scene_ex2_main()
        self.scene_ex3_subtract()
        self.scene_ex4_mixed()
        self.scene_cannot_merge()
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
        """淡出除 author 外所有元素"""
        self.play(
            *[FadeOut(m) for m in self.mobjects if m is not self.author],
            run_time=0.45,
        )

    # ═══════════════════════════════════════
    #  Scene 1: 开场钩子
    # ═══════════════════════════════════════
    def scene_opening(self):
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC", font_size=18, color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        chapter = Text(
            "八年级 · 第十六章 · 二次根式",
            font="Noto Sans CJK SC", font_size=20, color=GRAY_B,
        ).move_to(UP * 6.55)
        self.play(FadeIn(chapter), run_time=0.3)

        hook = Text(
            "根号也能相加？",
            font="Noto Sans CJK SC", font_size=48, color=self.C_TITLE,
        ).move_to(UP * 5.6)
        self.play(Write(hook), run_time=0.7)

        # 展示挑战题
        q_bg = self.card(7.2, 1.8, self.C_STEP1, UP * 4.3, fill="#0f2a3a", alpha=0.95)
        q_f  = MathTex(r"\sqrt{8} + \sqrt{18} = \;?", font_size=62, color=WHITE).move_to(UP * 4.3)
        self.play(Create(q_bg), Write(q_f), run_time=0.7)
        self.wait(0.8)

        # 错误直觉
        wrong_bg = self.card(6.5, 1.5, self.C_WRONG, UP * 2.9, fill="#2d0a0a", alpha=0.9)
        wrong_l  = Text("直觉（错！）：", font="Noto Sans CJK SC", font_size=24, color=self.C_WRONG)
        wrong_f  = MathTex(r"\sqrt{8+18} = \sqrt{26} \;\times", font_size=38, color=WHITE)
        VGroup(wrong_l, wrong_f).arrange(RIGHT, buff=0.25).move_to(UP * 2.9)
        self.play(Create(wrong_bg), Write(wrong_l), Write(wrong_f), run_time=0.7)

        # 正确答案揭晓
        right_bg = self.card(6.5, 1.5, self.C_RESULT, UP * 1.6, fill="#0a2e1a", alpha=0.9)
        right_l  = Text("正确答案：", font="Noto Sans CJK SC", font_size=24, color=self.C_RESULT)
        right_f  = MathTex(r"5\sqrt{2} \;\checkmark", font_size=46, color=WHITE)
        VGroup(right_l, right_f).arrange(RIGHT, buff=0.25).move_to(UP * 1.6)
        self.play(Create(right_bg), Write(right_l), Write(right_f), run_time=0.6)

        reveal = Text(
            "学完本节你就懂了！",
            font="Noto Sans CJK SC", font_size=30, color=self.C_TITLE,
        ).move_to(UP * 0.3)
        self.play(FadeIn(reveal, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(chapter), FadeOut(hook),
            FadeOut(q_bg), FadeOut(q_f),
            FadeOut(wrong_bg), FadeOut(wrong_l), FadeOut(wrong_f),
            FadeOut(right_bg), FadeOut(right_l), FadeOut(right_f),
            FadeOut(reveal),
            run_time=0.45,
        )

    # ═══════════════════════════════════════
    #  Scene 2: 三步走流程
    # ═══════════════════════════════════════
    def scene_three_steps(self):
        title = Text(
            "加减法三步走",
            font="Noto Sans CJK SC", font_size=46, color=self.C_TITLE,
        ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.6)

        steps = [
            (self.C_STEP1, UP * 5.0,  "Step 1",  "各项化成最简二次根式",
             r"\sqrt{8}=2\sqrt{2},\quad \sqrt{18}=3\sqrt{2}"),
            (self.C_STEP2, UP * 3.0,  "Step 2",  "找出同类二次根式",
             r"2\sqrt{2}\ \ \text{and}\ \ 3\sqrt{2}\ \Rightarrow\ \text{same!}"),
            (self.C_STEP3, UP * 1.0,  "Step 3",  "合并：系数相加，根式不变",
             r"2\sqrt{2}+3\sqrt{2}=(2+3)\sqrt{2}=5\sqrt{2}"),
        ]

        for col, pos, tag, desc, fml in steps:
            bg     = self.card(7.5, 1.85, col, pos)
            tag_t  = Text(tag,  font="Noto Sans CJK SC", font_size=24, color=col)
            desc_t = Text(desc, font="Noto Sans CJK SC", font_size=24, color=WHITE)
            fml_t  = MathTex(fml, font_size=29, color=self.C_TITLE)
            row    = VGroup(tag_t, desc_t).arrange(RIGHT, buff=0.3)
            VGroup(row, fml_t).arrange(DOWN, buff=0.18).move_to(pos)
            self.play(Create(bg), run_time=0.22)
            self.play(Write(row), Write(fml_t), run_time=0.55)
            self.wait(0.28)

        # 口诀
        slogan_bg = self.card(7.5, 1.4, self.C_TITLE, DOWN * 1.1, fill="#1a1000", alpha=0.9)
        slogan_t  = Text(
            "化简 → 找同类 → 合并系数",
            font="Noto Sans CJK SC", font_size=28, color=self.C_TITLE,
        ).move_to(DOWN * 1.1)
        self.play(Create(slogan_bg), Write(slogan_t), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 3: 例题 1 — 直接合并
    # ═══════════════════════════════════════
    def scene_ex1_direct(self):
        title = Text(
            "例题 1  直接合并",
            font="Noto Sans CJK SC", font_size=36, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_STEP1, UP * 5.5)
        prob_l  = Text("计算：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"2\sqrt{3} + 5\sqrt{3}", font_size=54, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 同类判断
        same_bg = self.card(7.2, 1.5, self.C_STEP2, UP * 4.1)
        same_t1 = Text("被开方数均为 3 →", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP2)
        same_t2 = Text("同类！", font="Noto Sans CJK SC", font_size=24, color=self.C_RESULT)
        VGroup(same_t1, same_t2).arrange(RIGHT, buff=0.2).move_to(UP * 4.1)
        self.play(Create(same_bg), Write(same_t1), Write(same_t2), run_time=0.6)

        # 推导
        s1 = MathTex(r"2\sqrt{3} + 5\sqrt{3}", font_size=52, color=WHITE).move_to(UP * 2.8)
        s2 = MathTex(r"= (2 + 5)\sqrt{3}", font_size=52, color=GRAY_A).move_to(UP * 1.8)
        s3 = MathTex(r"= 7\sqrt{3}", font_size=64, color=self.C_RESULT).move_to(UP * 0.7)
        self.play(Write(s1), run_time=0.4)
        self.play(Write(s2), run_time=0.4)
        self.play(Write(s3), run_time=0.5)

        ans_bg = self.card(6.5, 1.6, self.C_RESULT, DOWN * 0.5, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"2\sqrt{3}+5\sqrt{3}=7\sqrt{3}", font_size=46, color=WHITE).move_to(DOWN * 0.5)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)

        note = Text(
            "系数 2+5=7，根式 √3 不变",
            font="Noto Sans CJK SC", font_size=22, color=GRAY_A,
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 4: 例题 2 — √8 + √18（先化简）
    # ═══════════════════════════════════════
    def scene_ex2_main(self):
        title = Text(
            "例题 2  先化简再合并",
            font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_STEP1, UP * 5.5)
        prob_l  = Text("计算：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{8} + \sqrt{18}", font_size=54, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # Step 1 化简
        s1_bg  = self.card(7.2, 2.0, self.C_STEP1, UP * 4.1)
        s1_tag = Text("Step 1  化简各项", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP1)
        s1_f1  = MathTex(r"\sqrt{8}=\sqrt{4\times2}=2\sqrt{2}", font_size=32, color=WHITE)
        s1_f2  = MathTex(r"\sqrt{18}=\sqrt{9\times2}=3\sqrt{2}", font_size=32, color=WHITE)
        VGroup(s1_tag, s1_f1, s1_f2).arrange(DOWN, buff=0.18).move_to(UP * 4.1)
        self.play(Create(s1_bg), Write(s1_tag), Write(s1_f1), Write(s1_f2), run_time=0.8)

        # Step 2 代入
        s2_bg  = self.card(7.2, 1.6, self.C_STEP2, UP * 2.3)
        s2_tag = Text("Step 2  代入", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP2)
        s2_f   = MathTex(r"2\sqrt{2} + 3\sqrt{2}", font_size=44, color=WHITE)
        VGroup(s2_tag, s2_f).arrange(DOWN, buff=0.15).move_to(UP * 2.3)
        self.play(Create(s2_bg), Write(s2_tag), Write(s2_f), run_time=0.6)

        # Step 3 合并
        s3_bg  = self.card(7.2, 1.6, self.C_STEP3, UP * 0.9)
        s3_tag = Text("Step 3  合并", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP3)
        s3_f   = MathTex(r"(2+3)\sqrt{2}=5\sqrt{2}", font_size=44, color=WHITE)
        VGroup(s3_tag, s3_f).arrange(DOWN, buff=0.15).move_to(UP * 0.9)
        self.play(Create(s3_bg), Write(s3_tag), Write(s3_f), run_time=0.6)

        ans_bg = self.card(7.0, 1.6, self.C_RESULT, DOWN * 0.7, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{8}+\sqrt{18}=5\sqrt{2}", font_size=50, color=WHITE).move_to(DOWN * 0.7)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 5: 例题 3 — 减法
    # ═══════════════════════════════════════
    def scene_ex3_subtract(self):
        title = Text(
            "例题 3  根式减法",
            font="Noto Sans CJK SC", font_size=36, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_STEP1, UP * 5.5)
        prob_l  = Text("计算：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{12} - \sqrt{3}", font_size=54, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 化简 √12
        simp_bg = self.card(7.2, 1.6, self.C_STEP1, UP * 4.1)
        simp_t  = Text("化简 √12：", font="Noto Sans CJK SC", font_size=26, color=self.C_STEP1)
        simp_f  = MathTex(r"\sqrt{12}=\sqrt{4\times3}=2\sqrt{3}", font_size=36, color=WHITE)
        VGroup(simp_t, simp_f).arrange(DOWN, buff=0.15).move_to(UP * 4.1)
        self.play(Create(simp_bg), Write(simp_t), Write(simp_f), run_time=0.7)

        # 代入计算
        step1 = MathTex(r"2\sqrt{3} - \sqrt{3}", font_size=52, color=WHITE).move_to(UP * 2.8)
        step2 = MathTex(r"= (2-1)\sqrt{3}", font_size=52, color=GRAY_A).move_to(UP * 1.8)
        step3 = MathTex(r"= \sqrt{3}", font_size=64, color=self.C_RESULT).move_to(UP * 0.7)
        self.play(Write(step1), run_time=0.4)
        self.play(Write(step2), run_time=0.4)
        self.play(Write(step3), run_time=0.5)

        # 提示 √3 系数=1
        coeff_note_bg = self.card(7.0, 1.4, self.C_COEFF, DOWN * 0.4)
        coeff_t       = Text(
            "注意：√3 前系数是 1，不要忘记！",
            font="Noto Sans CJK SC", font_size=24, color=self.C_COEFF,
        ).move_to(DOWN * 0.4)
        self.play(Create(coeff_note_bg), Write(coeff_t), run_time=0.6)

        ans_bg = self.card(6.5, 1.6, self.C_RESULT, DOWN * 1.7, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{12}-\sqrt{3}=\sqrt{3}", font_size=50, color=WHITE).move_to(DOWN * 1.7)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.5)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.07), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 6: 例题 4 — 混合三项
    # ═══════════════════════════════════════
    def scene_ex4_mixed(self):
        title = Text(
            "例题 4  三项混合运算",
            font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_STEP1, UP * 5.55)
        prob_l  = Text("计算：", font="Noto Sans CJK SC", font_size=26, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{8}+\sqrt{18}-\sqrt{2}", font_size=48, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.55)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 化简三项
        simp_bg = self.card(7.2, 2.5, self.C_STEP1, UP * 4.0)
        simp_t  = Text("各项化简：", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP1)
        simp_f1 = MathTex(r"\sqrt{8}=2\sqrt{2}", font_size=32, color=WHITE)
        simp_f2 = MathTex(r"\sqrt{18}=3\sqrt{2}", font_size=32, color=WHITE)
        simp_f3 = MathTex(r"\sqrt{2}=\sqrt{2}", font_size=32, color=GRAY_A)
        VGroup(simp_t, simp_f1, simp_f2, simp_f3).arrange(DOWN, buff=0.18).move_to(UP * 4.0)
        self.play(Create(simp_bg), Write(simp_t), Write(simp_f1), Write(simp_f2), Write(simp_f3), run_time=0.9)

        # 代入合并
        merge_bg = self.card(7.2, 1.5, self.C_STEP3, UP * 2.2)
        merge_t  = Text("代入合并：", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP3)
        merge_f  = MathTex(r"2\sqrt{2}+3\sqrt{2}-\sqrt{2}", font_size=36, color=WHITE)
        VGroup(merge_t, merge_f).arrange(DOWN, buff=0.15).move_to(UP * 2.2)
        self.play(Create(merge_bg), Write(merge_t), Write(merge_f), run_time=0.6)

        step2 = MathTex(r"= (2+3-1)\sqrt{2}", font_size=44, color=GRAY_A).move_to(UP * 1.1)
        step3 = MathTex(r"= 4\sqrt{2}", font_size=60, color=self.C_RESULT).move_to(UP * 0.1)
        self.play(Write(step2), run_time=0.4)
        self.play(Write(step3), run_time=0.5)

        ans_bg = self.card(7.2, 1.6, self.C_RESULT, DOWN * 1.1, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{8}+\sqrt{18}-\sqrt{2}=4\sqrt{2}", font_size=40, color=WHITE).move_to(DOWN * 1.1)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_RESULT, scale_factor=1.06), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 7: 不能合并的情况
    # ═══════════════════════════════════════
    def scene_cannot_merge(self):
        title = Text(
            "不能合并的情况",
            font="Noto Sans CJK SC", font_size=40, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 非同类：化简后被开方数不同
        case_bg = self.card(7.4, 2.0, self.C_WRONG, UP * 5.1, fill="#2d0a0a", alpha=0.9)
        case_t1 = Text("化简后被开方数不同：", font="Noto Sans CJK SC", font_size=26, color=self.C_WRONG)
        case_f  = MathTex(r"\sqrt{2}+\sqrt{3}", font_size=50, color=WHITE)
        case_t2 = Text("→ 已是最简，无法合并", font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        VGroup(case_t1, case_f, case_t2).arrange(DOWN, buff=0.2).move_to(UP * 5.1)
        self.play(Create(case_bg), Write(case_t1), Write(case_f), FadeIn(case_t2), run_time=0.8)

        # 数值验证
        verify_bg = self.card(7.4, 2.4, self.C_STEP1, UP * 3.1)
        ver_t     = Text("数值验证：", font="Noto Sans CJK SC", font_size=24, color=self.C_STEP1)
        ver_f1    = MathTex(r"\sqrt{2} \approx 1.414,\quad \sqrt{3} \approx 1.732", font_size=30, color=WHITE)
        ver_f2    = MathTex(r"\sqrt{2}+\sqrt{3} \approx 3.146", font_size=32, color=WHITE)
        ver_f3    = MathTex(r"\neq \sqrt{5} \approx 2.236", font_size=32, color=self.C_WRONG)
        VGroup(ver_t, ver_f1, ver_f2, ver_f3).arrange(DOWN, buff=0.18).move_to(UP * 3.1)
        self.play(Create(verify_bg), Write(ver_t), Write(ver_f1), Write(ver_f2), Write(ver_f3), run_time=0.9)
        self.wait(0.5)

        # 正确写法：保留原式
        correct_bg = self.card(7.4, 1.6, self.C_STEP3, UP * 1.35)
        correct_t1 = Text("正确处理：保留原式", font="Noto Sans CJK SC", font_size=26, color=self.C_STEP3)
        correct_f  = MathTex(r"\sqrt{2}+\sqrt{3}\ \text{(final answer)}", font_size=36, color=WHITE)
        VGroup(correct_t1, correct_f).arrange(DOWN, buff=0.15).move_to(UP * 1.35)
        self.play(Create(correct_bg), Write(correct_t1), Write(correct_f), run_time=0.6)

        # 关键提示
        tip_bg = self.card(7.4, 1.5, self.C_TITLE, DOWN * 0.25, fill="#1a1000", alpha=0.9)
        tip_t  = Text(
            "非同类根式：化简后仍不同 → 保留",
            font="Noto Sans CJK SC", font_size=24, color=self.C_TITLE,
        ).move_to(DOWN * 0.25)
        self.play(Create(tip_bg), Write(tip_t), run_time=0.6)
        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 8: 综合练习
    # ═══════════════════════════════════════
    def scene_quick_practice(self):
        title = Text(
            "综合练习",
            font="Noto Sans CJK SC", font_size=44, color=self.C_TITLE,
        ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.5)

        # (题目, 结果LaTeX, 颜色, 提示)
        items = [
            (r"3\sqrt{5}+2\sqrt{5}",
             r"=5\sqrt{5}",
             self.C_STEP3, "直接合并"),
            (r"\sqrt{50}-\sqrt{8}",
             r"=3\sqrt{2}",
             self.C_STEP3, "√50=5√2, √8=2√2"),
            (r"\sqrt{12}+\sqrt{27}",
             r"=5\sqrt{3}",
             self.C_STEP3, "√12=2√3, √27=3√3"),
            (r"\sqrt{3}+\sqrt{5}",
             r"\text{(no merge)}",
             self.C_WRONG, "非同类，保留"),
        ]

        card_h  = 1.72
        start_y = 5.4
        gap     = 1.80

        for i, (prob, result, col, hint) in enumerate(items):
            pos_y = start_y - i * gap
            pos   = UP * pos_y
            bg    = self.card(7.6, card_h, col, pos)
            pf    = MathTex(prob,   font_size=36, color=WHITE)
            rf    = MathTex(result, font_size=34, color=self.C_RESULT)
            ht    = Text(hint, font="Noto Sans CJK SC", font_size=19, color=GRAY_A)
            top   = VGroup(pf, rf).arrange(RIGHT, buff=0.4)
            VGroup(top, ht).arrange(DOWN, buff=0.12).move_to(pos)

            self.play(Create(bg), run_time=0.18)
            self.play(Write(pf), run_time=0.30)
            self.play(Write(rf), FadeIn(ht), run_time=0.35)
            self.wait(0.22)

        self.wait(1.5)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 9: 总结
    # ═══════════════════════════════════════
    def scene_summary(self):
        title = Text(
            "知识点总结",
            font="Noto Sans CJK SC", font_size=46, color=self.C_TITLE,
        ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.5)

        blocks = [
            (self.C_STEP1, UP * 5.5, "Step 1  化简",
             r"\sqrt{8}\rightarrow2\sqrt{2},\ \sqrt{18}\rightarrow3\sqrt{2}"),
            (self.C_STEP2, UP * 3.95, "Step 2  找同类",
             r"2\sqrt{2}\ +\ 3\sqrt{2}\ \Rightarrow\ \text{same radicand}"),
            (self.C_STEP3, UP * 2.4, "Step 3  合并",
             r"a\sqrt{m}\pm b\sqrt{m}=(a\pm b)\sqrt{m}"),
            (self.C_RESULT, UP * 0.85, "核心例题",
             r"\sqrt{8}+\sqrt{18}=2\sqrt{2}+3\sqrt{2}=5\sqrt{2}"),
            (self.C_WRONG, DOWN * 0.7, "不能合并",
             r"\sqrt{2}+\sqrt{3}\ \text{(different radicand)}"),
        ]

        for col, pos, label_str, fml_str in blocks:
            bg  = self.card(7.6, 1.45, col, pos)
            lbl = Text(label_str, font="Noto Sans CJK SC", font_size=24, color=col)
            fml = MathTex(fml_str, font_size=26, color=WHITE)
            VGroup(lbl, fml).arrange(RIGHT, buff=0.4).move_to(pos)
            self.play(Create(bg), Write(lbl), Write(fml), run_time=0.45)
            self.wait(0.18)

        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════
    #  Scene 10: 片尾
    # ═══════════════════════════════════════
    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC", font_size=38, color=WHITE,
        ).move_to(UP * 2.5)
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC", font_size=28, color=GRAY_B,
        ).move_to(UP * 1.7)

        self.play(Transform(self.author, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我，学更多数学知识！",
            font="Noto Sans CJK SC", font_size=30, color=self.C_TITLE,
        ).move_to(UP * 0.3)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)

        deco = VGroup(
            MathTex(r"a\sqrt{m}\pm b\sqrt{m}=(a\pm b)\sqrt{m}", font_size=28, color=self.C_STEP3),
            MathTex(r"\sqrt{8}+\sqrt{18}=5\sqrt{2}",            font_size=30, color=self.C_RESULT),
            MathTex(r"\sqrt{12}-\sqrt{3}=\sqrt{3}",             font_size=30, color=self.C_STEP1),
        ).arrange(DOWN, buff=0.42).move_to(DOWN * 1.8)

        self.play(*[Write(f) for f in deco], run_time=1.0)
        self.play(*[Indicate(f, color=self.C_TITLE) for f in deco], run_time=0.9)
        self.wait(1.5)
        # ✅ 正确写法：逐个 FadeOut，避免 VGroup 类型冲突
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# 渲染命令：
# manim -pql radical_add_sub.py RadicalAddSub    # 快速预览
# manim -qh  radical_add_sub.py RadicalAddSub    # 高质量输出
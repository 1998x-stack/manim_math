"""
同类二次根式 — 教学动画
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


class LikeRadicals(Scene):
    """
    同类二次根式教学动画
    场景顺序:
    1. 开场钩子  — 对比同类 vs 非同类
    2. 同类二次根式的定义
    3. 判断是否同类（需先化最简）
    4. 合并法则  — 系数相加，根式不变
    5. 基础例题  2√3 + 5√3 = 7√3
    6. 进阶例题  √12 + √3 = 3√3（先化简再合并）
    7. 反例说明  √2 + √3 不能合并
    8. 综合练习  快速判断
    9. 总结 & 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        self.C_TITLE   = "#f9ca24"
        self.C_SAME    = "#6ab04c"   # 同类 — 绿
        self.C_DIFF    = "#eb4d4b"   # 非同类 — 红
        self.C_FORMULA = "#22a6b3"   # 公式蓝
        self.C_RULE    = "#a29bfe"   # 规则紫
        self.C_COEFF   = "#f0932b"   # 系数橙
        self.C_ROOT    = "#badc58"   # 根式部分亮绿
        self.C_NEUTRAL = GRAY_A

        self.scene_opening()
        self.scene_definition()
        self.scene_check_method()
        self.scene_merge_rule()
        self.scene_example_basic()
        self.scene_example_advanced()
        self.scene_counter_example()
        self.scene_quick_judge()
        self.scene_summary()
        self.scene_outro()

    # ───────────────────────── 工具 ─────────────────────────
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

    # ═══════════════════════════════════════════════════════
    #  Scene 1: 开场钩子
    # ═══════════════════════════════════════════════════════
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
            "下面哪组可以合并？",
            font="Noto Sans CJK SC", font_size=40, color=self.C_TITLE,
        ).move_to(UP * 5.6)
        self.play(Write(hook), run_time=0.7)

        # 左：同类  右：非同类
        left_bg  = self.card(3.5, 2.0, self.C_SAME,  UP * 4.0 + LEFT * 2.05)
        right_bg = self.card(3.5, 2.0, self.C_DIFF,  UP * 4.0 + RIGHT * 2.05)

        left_f   = MathTex(r"2\sqrt{3} + 5\sqrt{3}", font_size=36, color=WHITE).move_to(UP * 4.0 + LEFT * 2.05)
        right_f  = MathTex(r"\sqrt{2} + \sqrt{3}", font_size=36, color=WHITE).move_to(UP * 4.0 + RIGHT * 2.05)

        vs = Text("VS", font="Noto Sans CJK SC", font_size=34, color=GRAY_A).move_to(UP * 4.0)

        self.play(
            Create(left_bg), Write(left_f),
            Create(right_bg), Write(right_f),
            FadeIn(vs),
            run_time=0.7,
        )
        self.wait(0.8)

        # 揭晓左边可合并
        tick = Text("✓ 可以合并！", font="Noto Sans CJK SC", font_size=28, color=self.C_SAME).move_to(UP * 2.8 + LEFT * 2.05)
        cross = Text("✗ 不能合并", font="Noto Sans CJK SC", font_size=28, color=self.C_DIFF).move_to(UP * 2.8 + RIGHT * 2.05)
        self.play(
            left_bg.animate.set_stroke(color=self.C_SAME, width=5),
            Flash(left_f, color=self.C_SAME, flash_radius=0.8),
            FadeIn(tick, shift=UP * 0.2),
            FadeIn(cross, shift=UP * 0.2),
            run_time=0.7,
        )

        reveal = Text(
            "关键：被开方数是否相同！",
            font="Noto Sans CJK SC", font_size=30, color=self.C_TITLE,
        ).move_to(UP * 1.8)
        self.play(FadeIn(reveal, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(chapter), FadeOut(hook),
            FadeOut(left_bg), FadeOut(left_f),
            FadeOut(right_bg), FadeOut(right_f),
            FadeOut(vs), FadeOut(tick), FadeOut(cross), FadeOut(reveal),
            run_time=0.45,
        )

    # ═══════════════════════════════════════════════════════
    #  Scene 2: 定义
    # ═══════════════════════════════════════════════════════
    def scene_definition(self):
        title = Text(
            "同类二次根式",
            font="Noto Sans CJK SC", font_size=50, color=self.C_TITLE,
        ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.6)

        # 定义框
        def_bg = self.card(7.6, 2.4, self.C_FORMULA, UP * 5.0, fill="#0f3460", alpha=0.9)
        def_line1 = Text(
            "化成最简二次根式后，",
            font="Noto Sans CJK SC", font_size=26, color=WHITE,
        )
        def_line2 = Text(
            "被开方数相同的二次根式",
            font="Noto Sans CJK SC", font_size=26, color=self.C_FORMULA,
        )
        def_line3 = Text(
            "叫做同类二次根式",
            font="Noto Sans CJK SC", font_size=26, color=self.C_TITLE,
        )
        def_block = VGroup(def_line1, def_line2, def_line3).arrange(DOWN, buff=0.2).move_to(UP * 5.0)
        self.play(Create(def_bg), Write(def_block), run_time=0.9)

        # 类比：同类项
        analogy_bg = self.card(7.4, 1.5, self.C_RULE, UP * 3.2)
        analogy_l  = Text("类比：", font="Noto Sans CJK SC", font_size=24, color=self.C_RULE)
        analogy_f  = MathTex(r"2x + 5x", font_size=36, color=WHITE)
        analogy_r  = Text("↔ 同类项", font="Noto Sans CJK SC", font_size=24, color=self.C_RULE)
        VGroup(analogy_l, analogy_f, analogy_r).arrange(RIGHT, buff=0.3).move_to(UP * 3.2)
        self.play(Create(analogy_bg), Write(analogy_l), Write(analogy_f), Write(analogy_r), run_time=0.7)

        # 示例：同类 vs 非同类
        eg_title = Text("举例：", font="Noto Sans CJK SC", font_size=26, color=GRAY_A).move_to(UP * 2.0)
        self.play(FadeIn(eg_title), run_time=0.3)

        same_bg  = self.card(7.0, 1.5, self.C_SAME,  UP * 1.0)
        same_lbl  = Text("同类：", font="Noto Sans CJK SC", font_size=24, color=self.C_SAME)
        same_f    = VGroup(
            MathTex(r"2\sqrt{3}", font_size=36, color=WHITE),
            Text("和", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"5\sqrt{3}", font_size=36, color=WHITE),
        ).arrange(RIGHT, buff=0.15)
        same_note = Text("（被开方数都是3）", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        VGroup(same_lbl, same_f, same_note).arrange(RIGHT, buff=0.25).move_to(UP * 1.0)

        diff_bg  = self.card(7.0, 1.5, self.C_DIFF,  DOWN * 0.1)
        diff_lbl  = Text("非同类：", font="Noto Sans CJK SC", font_size=24, color=self.C_DIFF)
        diff_f    = VGroup(
            MathTex(r"\sqrt{2}", font_size=36, color=WHITE),
            Text("和", font="Noto Sans CJK SC", font_size=28, color=WHITE),
            MathTex(r"\sqrt{3}", font_size=36, color=WHITE),
        ).arrange(RIGHT, buff=0.15)
        diff_note = Text("（被开方数不同）", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        VGroup(diff_lbl, diff_f, diff_note).arrange(RIGHT, buff=0.25).move_to(DOWN * 0.1)

        self.play(Create(same_bg),  Write(same_lbl),  Write(same_f),  FadeIn(same_note),  run_time=0.6)
        self.play(Create(diff_bg),  Write(diff_lbl),  Write(diff_f),  FadeIn(diff_note),  run_time=0.6)

        # 警示：必须先化简
        warn_bg = self.card(7.4, 1.6, self.C_TITLE, DOWN * 1.5, fill="#1a1000", alpha=0.9)
        warn_t  = Text(
            "⚠ 判断前必须先化成最简二次根式！",
            font="Noto Sans CJK SC", font_size=24, color=self.C_TITLE,
        ).move_to(DOWN * 1.5)
        self.play(Create(warn_bg), Write(warn_t), run_time=0.6)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 3: 判断方法（先化简再比较）
    # ═══════════════════════════════════════════════════════
    def scene_check_method(self):
        title = Text(
            "怎么判断同类？",
            font="Noto Sans CJK SC", font_size=44, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        steps = [
            ("Step 1", "各自化成最简二次根式",
             r"\sqrt{12} \rightarrow 2\sqrt{3}"),
            ("Step 2", "比较被开方数",
             r"2\sqrt{3} \;\text{vs}\; \sqrt{3} \;\Rightarrow\; \checkmark"),
            ("Step 3", "得出结论",
             r"\sqrt{12}\ \text{and}\ \sqrt{3}\ \Rightarrow\ \text{same type!}"),
        ]
        colors = [self.C_FORMULA, self.C_RULE, self.C_SAME]
        positions = [UP * 5.0, UP * 3.0, UP * 1.0]

        for (tag, desc, fml), col, pos in zip(steps, colors, positions):
            bg  = self.card(7.5, 1.9, col, pos)
            tag_t  = Text(tag,  font="Noto Sans CJK SC", font_size=24, color=col)
            desc_t = Text(desc, font="Noto Sans CJK SC", font_size=24, color=WHITE)
            form_t = MathTex(fml, font_size=30, color=self.C_TITLE)
            row    = VGroup(tag_t, desc_t).arrange(RIGHT, buff=0.3)
            VGroup(row, form_t).arrange(DOWN, buff=0.18).move_to(pos)

            self.play(Create(bg), run_time=0.22)
            self.play(Write(row), Write(form_t), run_time=0.55)
            self.wait(0.3)

        key_bg = self.card(7.5, 1.4, self.C_COEFF, DOWN * 1.1, fill="#1a0f00", alpha=0.9)
        key_t  = Text(
            "口诀：化简 → 看根号内 → 相同即同类",
            font="Noto Sans CJK SC", font_size=24, color=self.C_TITLE,
        ).move_to(DOWN * 1.1)
        self.play(Create(key_bg), Write(key_t), run_time=0.6)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 4: 合并法则
    # ═══════════════════════════════════════════════════════
    def scene_merge_rule(self):
        title = Text(
            "合并法则",
            font="Noto Sans CJK SC", font_size=48, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 类比同类项合并
        analogy_title = Text(
            "类比同类项合并：",
            font="Noto Sans CJK SC", font_size=28, color=GRAY_A,
        ).move_to(UP * 5.5)
        analogy_f = MathTex(
            r"2x + 5x = (2+5)x = 7x",
            font_size=40, color=self.C_NEUTRAL,
        ).move_to(UP * 4.7)
        self.play(FadeIn(analogy_title), Write(analogy_f), run_time=0.7)

        # 同样地
        arrow_down = MathTex(r"\Downarrow", font_size=40, color=GRAY_A).move_to(UP * 3.8)
        same_logic = Text(
            "同样地，对同类二次根式：",
            font="Noto Sans CJK SC", font_size=26, color=WHITE,
        ).move_to(UP * 3.1)
        self.play(Write(arrow_down), FadeIn(same_logic), run_time=0.5)

        # 核心公式
        rule_bg = self.card(7.6, 2.2, self.C_FORMULA, UP * 1.9, fill="#0f2a3a", alpha=0.95)
        rule_f  = MathTex(
            r"m\sqrt{a} + n\sqrt{a} = (m+n)\sqrt{a}",
            font_size=38, color=WHITE,
        ).move_to(UP * 2.1)
        rule_note = Text(
            "系数相加减，根式部分不变",
            font="Noto Sans CJK SC", font_size=24, color=self.C_FORMULA,
        ).move_to(UP * 1.5)

        self.play(Create(rule_bg), Write(rule_f), run_time=0.7)
        self.play(Write(rule_note), run_time=0.5)

        # 着色说明：系数 vs 根式
        coeff_box = SurroundingRectangle(
            MathTex(r"m,\ n", font_size=36).move_to(UP * 0.4),
            color=self.C_COEFF, buff=0.15, corner_radius=0.12,
        )
        coeff_lbl = Text("系数（可变）", font="Noto Sans CJK SC", font_size=22, color=self.C_COEFF).move_to(UP * 0.4 + LEFT * 2.5)

        root_box = SurroundingRectangle(
            MathTex(r"\sqrt{a}", font_size=36).move_to(DOWN * 0.4),
            color=self.C_ROOT, buff=0.15, corner_radius=0.12,
        )
        root_lbl = Text("根式（不变）", font="Noto Sans CJK SC", font_size=22, color=self.C_ROOT).move_to(DOWN * 0.4 + RIGHT * 2.5)

        coeff_legend = VGroup(
            Text("系数：", font="Noto Sans CJK SC", font_size=22, color=self.C_COEFF),
            Text("前面的数字，相加减", font="Noto Sans CJK SC", font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.5)

        root_legend = VGroup(
            Text("根式：", font="Noto Sans CJK SC", font_size=22, color=self.C_ROOT),
            Text("根号部分，保持不变", font="Noto Sans CJK SC", font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.1)

        self.play(FadeIn(coeff_legend), FadeIn(root_legend), run_time=0.6)

        # 重要提醒
        warn_bg = self.card(7.4, 1.4, self.C_DIFF, DOWN * 3.2, fill="#2d0a0a", alpha=0.9)
        warn_t  = Text(
            "⚠ 非同类二次根式不能合并！",
            font="Noto Sans CJK SC", font_size=26, color=self.C_DIFF,
        ).move_to(DOWN * 3.2)
        self.play(Create(warn_bg), Write(warn_t), run_time=0.6)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 5: 基础例题  2√3 + 5√3 = 7√3
    # ═══════════════════════════════════════════════════════
    def scene_example_basic(self):
        title = Text(
            "例题 1  — 直接合并",
            font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_FORMULA, UP * 5.5)
        prob_l  = Text("计算：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"2\sqrt{3} + 5\sqrt{3}", font_size=52, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # 用颜色高亮系数和根式
        highlight_bg = self.card(7.4, 1.6, self.C_RULE, UP * 4.0)
        h_f = MathTex(
            r"\underbrace{2}_{coeff}\sqrt{3}"
            r"+ \underbrace{5}_{coeff}\sqrt{3}",
            font_size=40, color=WHITE,
        ).move_to(UP * 4.0)
        self.play(Create(highlight_bg), Write(h_f), run_time=0.7)

        # 逐步推导
        step1 = MathTex(r"= (2 + 5)\sqrt{3}", font_size=52, color=GRAY_A).move_to(UP * 2.7)
        step2 = MathTex(r"= 7\sqrt{3}", font_size=64, color=self.C_SAME).move_to(UP * 1.5)

        self.play(Write(step1), run_time=0.5)
        self.wait(0.3)
        self.play(Write(step2), run_time=0.5)

        # 结论框
        ans_bg = self.card(6.5, 1.6, self.C_SAME, UP * 0.1, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"2\sqrt{3} + 5\sqrt{3} = 7\sqrt{3}", font_size=46, color=WHITE).move_to(UP * 0.1)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_SAME, scale_factor=1.07), run_time=0.6)

        note = Text(
            "规律：系数 2+5=7，根式 √3 不变",
            font="Noto Sans CJK SC", font_size=24, color=GRAY_A,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 6: 进阶例题  √12 + √3 = 3√3（先化简）
    # ═══════════════════════════════════════════════════════
    def scene_example_advanced(self):
        title = Text(
            "例题 2  — 先化简再合并",
            font="Noto Sans CJK SC", font_size=32, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.card(7.2, 1.4, self.C_FORMULA, UP * 5.5)
        prob_l  = Text("计算：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_f  = MathTex(r"\sqrt{12} + \sqrt{3}", font_size=52, color=WHITE)
        VGroup(prob_l, prob_f).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        self.play(Write(title), Create(prob_bg), Write(prob_l), Write(prob_f), run_time=0.7)

        # Step 1: 化简 √12
        s1_bg = self.card(7.2, 1.7, self.C_COEFF, UP * 4.0)
        s1_tag = Text("Step 1  化简 √12：", font="Noto Sans CJK SC", font_size=24, color=self.C_COEFF)
        s1_f   = MathTex(r"\sqrt{12} = \sqrt{4 \times 3} = 2\sqrt{3}", font_size=34, color=WHITE)
        VGroup(s1_tag, s1_f).arrange(DOWN, buff=0.15).move_to(UP * 4.0)
        self.play(Create(s1_bg), Write(s1_tag), Write(s1_f), run_time=0.7)

        # Step 2: 代入
        s2_bg = self.card(7.2, 1.7, self.C_RULE, UP * 2.1)
        s2_tag = Text("Step 2  代入原式：", font="Noto Sans CJK SC", font_size=24, color=self.C_RULE)
        s2_f   = MathTex(r"2\sqrt{3} + \sqrt{3}", font_size=40, color=WHITE)
        VGroup(s2_tag, s2_f).arrange(DOWN, buff=0.15).move_to(UP * 2.1)
        self.play(Create(s2_bg), Write(s2_tag), Write(s2_f), run_time=0.6)

        # Step 3: 合并
        s3_bg = self.card(7.2, 1.7, self.C_SAME, UP * 0.2)
        s3_tag = Text("Step 3  合并同类项：", font="Noto Sans CJK SC", font_size=24, color=self.C_SAME)
        s3_f   = MathTex(r"(2 + 1)\sqrt{3} = 3\sqrt{3}", font_size=40, color=WHITE)
        VGroup(s3_tag, s3_f).arrange(DOWN, buff=0.15).move_to(UP * 0.2)
        self.play(Create(s3_bg), Write(s3_tag), Write(s3_f), run_time=0.6)

        # 最终结论
        ans_bg = self.card(7.0, 1.6, self.C_SAME, DOWN * 1.5, fill="#0a2e1a", alpha=0.95)
        ans_f  = MathTex(r"\sqrt{12} + \sqrt{3} = 3\sqrt{3}", font_size=48, color=WHITE).move_to(DOWN * 1.5)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_SAME, scale_factor=1.07), run_time=0.6)

        key_note = Text(
            "看似不同类 → 化简后才发现是同类！",
            font="Noto Sans CJK SC", font_size=22, color=self.C_TITLE,
        ).move_to(DOWN * 2.7)
        self.play(FadeIn(key_note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 7: 反例 — √2 + √3 不能合并
    # ═══════════════════════════════════════════════════════
    def scene_counter_example(self):
        title = Text(
            "反例 — 不能合并的情况",
            font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 错误做法
        wrong_bg = self.card(7.2, 2.2, self.C_DIFF, UP * 5.1, fill="#2d0a0a", alpha=0.9)
        wrong_tag = Text("✗  错误做法：", font="Noto Sans CJK SC", font_size=26, color=self.C_DIFF)
        wrong_f   = MathTex(r"\sqrt{2} + \sqrt{3} \neq \sqrt{5}", font_size=44, color=WHITE)
        wrong_exp = Text("（根号内不能直接相加！）", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        VGroup(wrong_tag, wrong_f, wrong_exp).arrange(DOWN, buff=0.18).move_to(UP * 5.1)
        self.play(Create(wrong_bg), Write(wrong_tag), Write(wrong_f), FadeIn(wrong_exp), run_time=0.8)

        # 数字验证
        verify_bg = self.card(7.2, 2.5, self.C_FORMULA, UP * 3.0)
        verify_tag = Text("数字验证：", font="Noto Sans CJK SC", font_size=24, color=self.C_FORMULA)
        verify_f1  = MathTex(r"\sqrt{2} \approx 1.414", font_size=32, color=WHITE)
        verify_f2  = MathTex(r"\sqrt{3} \approx 1.732", font_size=32, color=WHITE)
        verify_f3  = MathTex(r"\sqrt{2}+\sqrt{3} \approx 3.146 \neq \sqrt{5} \approx 2.236", font_size=28, color=self.C_DIFF)
        VGroup(verify_tag, verify_f1, verify_f2, verify_f3).arrange(DOWN, buff=0.15).move_to(UP * 3.0)
        self.play(Create(verify_bg), Write(verify_tag), run_time=0.4)
        self.play(Write(verify_f1), Write(verify_f2), run_time=0.5)
        self.play(Write(verify_f3), run_time=0.5)
        self.wait(0.5)

        # 正确处理
        correct_bg = self.card(7.2, 1.8, self.C_SAME, UP * 0.8)
        correct_tag = Text("✓  正确：", font="Noto Sans CJK SC", font_size=26, color=self.C_SAME)
        correct_f   = MathTex(r"\sqrt{2} + \sqrt{3}", font_size=40, color=WHITE)
        correct_note= Text("已是最简，非同类，不可合并", font="Noto Sans CJK SC", font_size=22, color=self.C_SAME)
        VGroup(correct_tag, correct_f, correct_note).arrange(DOWN, buff=0.15).move_to(UP * 0.8)
        self.play(Create(correct_bg), Write(correct_tag), Write(correct_f), FadeIn(correct_note), run_time=0.7)

        # 结论提示
        rule_bg = self.card(7.4, 1.5, self.C_RULE, DOWN * 0.8, fill="#16102e", alpha=0.9)
        rule_t  = Text(
            "被开方数不同 = 非同类 = 不能合并",
            font="Noto Sans CJK SC", font_size=24, color=self.C_TITLE,
        ).move_to(DOWN * 0.8)
        self.play(Create(rule_bg), Write(rule_t), run_time=0.6)
        self.wait(2.0)

        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 8: 综合快速判断
    # ═══════════════════════════════════════════════════════
    def scene_quick_judge(self):
        title = Text(
            "快速判断是否可以合并",
            font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # (LaTeX表达式, 可合并?, 理由, 结果)
        items = [
            (r"3\sqrt{5} + 2\sqrt{5}",  True,  "同类（√5=√5）",     r"= 5\sqrt{5}"),
            (r"\sqrt{8} + \sqrt{2}",    True,  "√8=2√2，化简后同类", r"= 3\sqrt{2}"),
            (r"\sqrt{3} - \sqrt{7}",    False, "非同类，不可合并",    r"\times"),
            (r"4\sqrt{6} - \sqrt{6}",   True,  "同类（√6=√6）",     r"= 3\sqrt{6}"),
        ]

        card_h   = 1.75
        start_y  = 5.3
        gap      = 1.82

        for i, (expr, ok, reason, result) in enumerate(items):
            pos_y = start_y - i * gap
            pos   = UP * pos_y
            col   = self.C_SAME if ok else self.C_DIFF
            sym   = "✓" if ok else "✗"

            bg   = self.card(7.6, card_h, col, pos)
            expr_f = MathTex(expr, font_size=36, color=WHITE)
            sym_t  = Text(sym, font="Noto Sans CJK SC", font_size=30, color=col)
            reas_t = Text(reason, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
            res_f  = MathTex(result, font_size=30, color=self.C_TITLE)
            top_row = VGroup(expr_f, sym_t).arrange(RIGHT, buff=0.4)
            bot_row = VGroup(reas_t, res_f).arrange(RIGHT, buff=0.3)
            VGroup(top_row, bot_row).arrange(DOWN, buff=0.12).move_to(pos)

            self.play(Create(bg), run_time=0.18)
            self.play(Write(expr_f), FadeIn(sym_t, scale=1.2), run_time=0.35)
            self.play(FadeIn(reas_t), Write(res_f), run_time=0.30)
            self.wait(0.22)

        self.wait(1.5)
        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 9: 总结
    # ═══════════════════════════════════════════════════════
    def scene_summary(self):
        title = Text(
            "知识点总结",
            font="Noto Sans CJK SC", font_size=46, color=self.C_TITLE,
        ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.5)

        blocks = [
            (self.C_FORMULA, UP * 5.5, "定义",
             r"a=b \Rightarrow \sqrt{a}=\sqrt{b}\ (\text{same radicand})"),
            (self.C_RULE,    UP * 3.8, "判断步骤",
             r"\text{simplify} \rightarrow \text{compare radicand}"),
            (self.C_COEFF,   UP * 2.1, "合并法则",
             r"m\sqrt{a} \pm n\sqrt{a} = (m \pm n)\sqrt{a}"),
            (self.C_SAME,    UP * 0.4, "核心例题",
             r"\sqrt{12}+\sqrt{3}=2\sqrt{3}+\sqrt{3}=3\sqrt{3}"),
            (self.C_DIFF,    DOWN * 1.3, "注意",
             r"\sqrt{2}+\sqrt{3} \Rightarrow \text{not like, cannot merge}"),
        ]

        for col, pos, label_str, fml_str in blocks:
            bg  = self.card(7.6, 1.5, col, pos)
            lbl = Text(label_str, font="Noto Sans CJK SC", font_size=24, color=col)
            fml = MathTex(fml_str, font_size=28, color=WHITE)
            VGroup(lbl, fml).arrange(RIGHT, buff=0.4).move_to(pos)
            self.play(Create(bg), Write(lbl), Write(fml), run_time=0.45)
            self.wait(0.2)

        self.wait(2.0)
        self.fade_rest()

    # ═══════════════════════════════════════════════════════
    #  Scene 10: 片尾
    # ═══════════════════════════════════════════════════════
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
            MathTex(r"2\sqrt{3}+5\sqrt{3}=7\sqrt{3}",             font_size=28, color=self.C_FORMULA),
            MathTex(r"\sqrt{12}+\sqrt{3}=3\sqrt{3}",              font_size=28, color=self.C_RULE),
            MathTex(r"m\sqrt{a}\pm n\sqrt{a}=(m\pm n)\sqrt{a}",   font_size=26, color=self.C_COEFF),
        ).arrange(DOWN, buff=0.42).move_to(DOWN * 1.8)

        self.play(*[Write(f) for f in deco], run_time=1.0)
        self.play(*[Indicate(f, color=self.C_TITLE) for f in deco], run_time=0.9)
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# 渲染命令:
# manim -pql like_radicals.py LikeRadicals    # 快速预览
# manim -qh  like_radicals.py LikeRadicals    # 高质量输出
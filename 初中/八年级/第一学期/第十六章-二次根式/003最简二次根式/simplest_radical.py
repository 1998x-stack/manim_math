"""
最简二次根式 - 教学动画
目标受众: 八年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SimplestRadical(Scene):
    """
    最简二次根式教学动画
    场景:
    1. 开场钩子 — 哪个更简洁？
    2. 最简二次根式的两个条件
    3. 化简方法：提取完全平方因数
    4. 例题1: √12 = 2√3
    5. 例题2: √(a²b) = a√b
    6. 条件2演示: 分母有理化引导
    7. 例题3: √(3/4) 处理
    8. 综合练习判断
    9. 总结 & 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.C_TITLE    = "#f9ca24"
        self.C_STEP     = "#6ab04c"
        self.C_FORMULA  = "#22a6b3"
        self.C_WRONG    = "#eb4d4b"
        self.C_RIGHT    = "#badc58"
        self.C_ARROW    = "#f0932b"
        self.C_RULE     = "#a29bfe"
        self.C_NEUTRAL  = GRAY_A

        self.scene_opening()
        self.scene_two_conditions()
        self.scene_method()
        self.scene_example1()
        self.scene_example2()
        self.scene_example3()
        self.scene_judge()
        self.scene_summary()
        self.scene_outro()

    # ═══════════════════════════════════════════════════
    #  工具方法
    # ═══════════════════════════════════════════════════
    def make_card(self, width, height, color, pos, fill="#16213e", alpha=0.85):
        bg = RoundedRectangle(
            corner_radius=0.28,
            width=width, height=height,
            color=color, stroke_width=2,
            fill_color=fill, fill_opacity=alpha,
        ).move_to(pos)
        return bg

    def fade_all_except_author(self):
        self.play(
            *[FadeOut(m) for m in self.mobjects if m is not self.author],
            run_time=0.45,
        )

    # ═══════════════════════════════════════════════════
    #  Scene 1: 开场钩子
    # ═══════════════════════════════════════════════════
    def scene_opening(self):
        # 作者信息（常驻）
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

        # 问题抛出
        hook = Text(
            "你觉得哪个更简洁？",
            font="Noto Sans CJK SC", font_size=40, color=self.C_TITLE,
        ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.7)

        # 左：未化简   右：已化简
        left_box  = self.make_card(3.4, 1.8, self.C_WRONG,  UP * 4.0 + LEFT * 2.0)
        right_box = self.make_card(3.4, 1.8, self.C_RIGHT,  UP * 4.0 + RIGHT * 2.0)

        left_f  = MathTex(r"\sqrt{12}", font_size=64, color=WHITE).move_to(UP * 4.0 + LEFT * 2.0)
        right_f = MathTex(r"2\sqrt{3}", font_size=64, color=WHITE).move_to(UP * 4.0 + RIGHT * 2.0)

        self.play(
            Create(left_box), Write(left_f),
            Create(right_box), Write(right_f),
            run_time=0.7,
        )

        # VS 标签
        vs = Text("VS", font="Noto Sans CJK SC", font_size=36, color=GRAY_A).move_to(UP * 4.0)
        self.play(FadeIn(vs), run_time=0.3)
        self.wait(0.8)

        # 高亮右边
        self.play(
            right_box.animate.set_stroke(color=self.C_RIGHT, width=5),
            Flash(right_f, color=self.C_RIGHT, flash_radius=0.7),
            run_time=0.6,
        )

        answer = Text(
            "右边是「最简二次根式」！",
            font="Noto Sans CJK SC", font_size=30, color=self.C_TITLE,
        ).move_to(UP * 2.6)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(chapter), FadeOut(hook),
            FadeOut(left_box), FadeOut(left_f),
            FadeOut(right_box), FadeOut(right_f),
            FadeOut(vs), FadeOut(answer),
            run_time=0.45,
        )

    # ═══════════════════════════════════════════════════
    #  Scene 2: 两个条件
    # ═══════════════════════════════════════════════════
    def scene_two_conditions(self):
        title = Text(
            "最简二次根式",
            font="Noto Sans CJK SC", font_size=48, color=self.C_TITLE,
        ).move_to(UP * 6.3)
        subtitle = Text(
            "需满足两个条件",
            font="Noto Sans CJK SC", font_size=28, color=GRAY_A,
        ).move_to(UP * 5.55)
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.3)

        # ── 条件 1 ──
        c1_bg = self.make_card(7.5, 2.6, self.C_FORMULA, UP * 4.1)
        c1_num = Text("①", font="Noto Sans CJK SC", font_size=36, color=self.C_FORMULA)
        c1_txt = Text(
            "被开方数不含分母",
            font="Noto Sans CJK SC", font_size=30, color=WHITE,
        )
        c1_bad  = MathTex(r"\sqrt{\dfrac{3}{4}}", font_size=44, color=self.C_WRONG)
        c1_arr  = MathTex(r"\rightarrow", font_size=36, color=GRAY_A)
        c1_good = MathTex(r"\dfrac{\sqrt{3}}{2}", font_size=44, color=self.C_RIGHT)
        c1_ex   = VGroup(c1_bad, c1_arr, c1_good).arrange(RIGHT, buff=0.3)
        c1_inner = VGroup(c1_num, c1_txt).arrange(RIGHT, buff=0.2)
        c1_all = VGroup(c1_inner, c1_ex).arrange(DOWN, buff=0.25).move_to(UP * 4.1)

        self.play(Create(c1_bg), run_time=0.4)
        self.play(Write(c1_inner), run_time=0.5)
        self.play(Write(c1_bad), Write(c1_arr), Write(c1_good), run_time=0.6)
        self.wait(0.4)

        # ── 条件 2 ──
        c2_bg = self.make_card(7.5, 2.8, self.C_RULE, UP * 1.4)
        c2_num = Text("②", font="Noto Sans CJK SC", font_size=36, color=self.C_RULE)
        c2_txt = Text(
            "被开方数不含能开得尽的因数",
            font="Noto Sans CJK SC", font_size=26, color=WHITE,
        )
        c2_bad  = MathTex(r"\sqrt{12}", font_size=44, color=self.C_WRONG)
        c2_arr  = MathTex(r"\rightarrow", font_size=36, color=GRAY_A)
        c2_good = MathTex(r"2\sqrt{3}", font_size=44, color=self.C_RIGHT)
        c2_note = Text(
            "（因为 12=4×3，4=2² 可开方）",
            font="Noto Sans CJK SC", font_size=20, color=GRAY_A,
        )
        c2_ex   = VGroup(c2_bad, c2_arr, c2_good).arrange(RIGHT, buff=0.3)
        c2_inner = VGroup(c2_num, c2_txt).arrange(RIGHT, buff=0.2)
        c2_all = VGroup(c2_inner, c2_ex, c2_note).arrange(DOWN, buff=0.2).move_to(UP * 1.4)

        self.play(Create(c2_bg), run_time=0.4)
        self.play(Write(c2_inner), run_time=0.5)
        self.play(Write(c2_bad), Write(c2_arr), Write(c2_good), run_time=0.6)
        self.play(FadeIn(c2_note), run_time=0.4)
        self.wait(0.4)

        # 口诀
        slogan_bg = self.make_card(7.5, 1.4, self.C_TITLE, DOWN * 1.3, fill="#0f3460", alpha=0.9)
        slogan = Text(
            "根号内：无分母 · 无完全平方因数",
            font="Noto Sans CJK SC", font_size=26, color=self.C_TITLE,
        ).move_to(DOWN * 1.3)
        self.play(Create(slogan_bg), Write(slogan), run_time=0.7)
        self.wait(2.0)

        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 3: 化简方法总览
    # ═══════════════════════════════════════════════════
    def scene_method(self):
        title = Text(
            "化简步骤",
            font="Noto Sans CJK SC", font_size=44, color=self.C_TITLE,
        ).move_to(UP * 6.4)
        self.play(Write(title), run_time=0.6)

        steps = [
            ("Step 1", "因式分解被开方数", r"12 = 4 \times 3 = 2^2 \times 3"),
            ("Step 2", "提取完全平方因数", r"\sqrt{2^2 \times 3}"),
            ("Step 3", "移到根号外开方",   r"2\sqrt{3}"),
        ]
        colors = [self.C_FORMULA, self.C_RULE, self.C_RIGHT]
        positions = [UP * 5.1, UP * 3.0, UP * 0.9]

        for (tag, desc, formula), col, pos in zip(steps, colors, positions):
            bg = self.make_card(7.5, 1.9, col, pos)
            tag_t  = Text(tag,  font="Noto Sans CJK SC", font_size=24, color=col)
            desc_t = Text(desc, font="Noto Sans CJK SC", font_size=26, color=WHITE)
            form_t = MathTex(formula, font_size=36, color=self.C_TITLE)
            row    = VGroup(tag_t, desc_t).arrange(RIGHT, buff=0.35)
            inner  = VGroup(row, form_t).arrange(DOWN, buff=0.15).move_to(pos)

            self.play(Create(bg), run_time=0.25)
            self.play(Write(row), Write(form_t), run_time=0.55)
            self.wait(0.3)

        # 关键规律
        key_bg = self.make_card(7.5, 1.5, self.C_ARROW, DOWN * 1.4, fill="#1a1a0e", alpha=0.9)
        key_f  = MathTex(
            r"\sqrt{a^2 \cdot b} = a\sqrt{b} \quad (a \geq 0,\ b \geq 0)",
            font_size=30, color=WHITE,
        ).move_to(DOWN * 1.4)
        self.play(Create(key_bg), Write(key_f), run_time=0.7)
        self.wait(2.0)

        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 4: 例题 1  √12 = 2√3
    # ═══════════════════════════════════════════════════
    def scene_example1(self):
        title = Text(
            "例题 1", font="Noto Sans CJK SC",
            font_size=36, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.make_card(7.2, 1.4, self.C_FORMULA, UP * 5.5)
        prob_label = Text("化简：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_form  = MathTex(r"\sqrt{12}", font_size=52, color=WHITE)
        VGroup(prob_label, prob_form).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.4)
        self.play(Create(prob_bg), Write(prob_label), Write(prob_form), run_time=0.6)

        # 逐步推导
        steps = [
            (r"\sqrt{12}", UP * 3.8),
            (r"= \sqrt{4 \times 3}", UP * 2.8),
            (r"= \sqrt{2^2 \times 3}", UP * 1.8),
            (r"= 2\sqrt{3}", UP * 0.8),
        ]
        step_colors = [WHITE, GRAY_A, GRAY_A, self.C_RIGHT]

        prev = None
        for i, (expr, pos) in enumerate(steps):
            tex = MathTex(expr, font_size=52, color=step_colors[i]).move_to(pos)
            if prev is None:
                self.play(Write(tex), run_time=0.5)
            else:
                self.play(Write(tex), run_time=0.5)
            prev = tex
            self.wait(0.4)

        # 结论框
        ans_bg = self.make_card(6.0, 1.6, self.C_RIGHT, DOWN * 0.5, fill="#0a2e1a", alpha=0.9)
        ans_label = Text("结果：", font="Noto Sans CJK SC", font_size=28, color=self.C_RIGHT)
        ans_f = MathTex(r"\sqrt{12} = 2\sqrt{3}", font_size=52, color=WHITE)
        VGroup(ans_label, ans_f).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)

        self.play(Create(ans_bg), Write(ans_label), Write(ans_f), run_time=0.7)
        self.play(Indicate(ans_f, color=self.C_RIGHT, scale_factor=1.08), run_time=0.7)

        # 要点说明
        note = Text(
            "4 = 2² 是完全平方数，可以开方移出",
            font="Noto Sans CJK SC", font_size=22, color=GRAY_A,
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 5: 例题 2  √(a²b) = a√b
    # ═══════════════════════════════════════════════════
    def scene_example2(self):
        title = Text(
            "例题 2  — 含字母的化简",
            font="Noto Sans CJK SC", font_size=32, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.make_card(7.2, 1.4, self.C_FORMULA, UP * 5.5)
        prob_label = Text("化简：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_form  = MathTex(r"\sqrt{a^2 b}", font_size=52, color=WHITE)
        VGroup(prob_label, prob_form).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)

        self.play(Write(title), Create(prob_bg), Write(prob_label), Write(prob_form), run_time=0.7)

        # 条件说明
        cond_bg = self.make_card(7.0, 1.2, self.C_RULE, UP * 4.2)
        cond = Text(
            "已知 a ≥ 0, b ≥ 0",
            font="Noto Sans CJK SC", font_size=26, color=self.C_RULE,
        ).move_to(UP * 4.2)
        self.play(Create(cond_bg), Write(cond), run_time=0.5)

        # 拆分演示（用箭头指向不同部分）
        formula_big = MathTex(r"\sqrt{a^2 \cdot b}", font_size=72, color=WHITE).move_to(UP * 2.8)
        self.play(Write(formula_big), run_time=0.5)

        # 标注 a² 和 b
        arr_a = Arrow(
            np.array([-1.8, 1.4, 0]), np.array([-0.8, 2.2, 0]),
            color=self.C_ARROW, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        lbl_a = Text("完全平方", font="Noto Sans CJK SC", font_size=20, color=self.C_ARROW).move_to(np.array([-2.5, 1.1, 0]))

        arr_b = Arrow(
            np.array([1.8, 1.4, 0]), np.array([0.9, 2.2, 0]),
            color=self.C_FORMULA, stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        lbl_b = Text("留在根号内", font="Noto Sans CJK SC", font_size=20, color=self.C_FORMULA).move_to(np.array([2.8, 1.1, 0]))

        self.play(
            GrowArrow(arr_a), FadeIn(lbl_a),
            GrowArrow(arr_b), FadeIn(lbl_b),
            run_time=0.7,
        )
        self.wait(0.5)

        # 推导
        step2 = MathTex(r"= a\sqrt{b}", font_size=64, color=self.C_RIGHT).move_to(UP * 0.3)
        self.play(Write(step2), run_time=0.6)

        ans_bg = self.make_card(7.0, 1.6, self.C_RIGHT, DOWN * 1.0, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(r"\sqrt{a^2 b} = a\sqrt{b}", font_size=46, color=WHITE).move_to(DOWN * 1.0)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_RIGHT, scale_factor=1.06), run_time=0.6)

        note = Text(
            "a² 开方得 a，b 不能开方留在根号内",
            font="Noto Sans CJK SC", font_size=22, color=GRAY_A,
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(2.0)

        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 6: 例题 3  √(3/4) 条件①处理
    # ═══════════════════════════════════════════════════
    def scene_example3(self):
        title = Text(
            "例题 3  — 根号内有分母",
            font="Noto Sans CJK SC", font_size=32, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        prob_bg = self.make_card(7.2, 1.4, self.C_WRONG, UP * 5.5)
        prob_label = Text("化简：", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        prob_form  = MathTex(r"\sqrt{\dfrac{3}{4}}", font_size=52, color=WHITE)
        VGroup(prob_label, prob_form).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)

        self.play(Write(title), Create(prob_bg), Write(prob_label), Write(prob_form), run_time=0.7)

        # 违反条件1
        warn_bg = self.make_card(7.0, 1.2, self.C_WRONG, UP * 4.2, fill="#2d0a0a", alpha=0.9)
        warn = Text(
            "✗ 根号内有分母，不是最简！",
            font="Noto Sans CJK SC", font_size=24, color=self.C_WRONG,
        ).move_to(UP * 4.2)
        self.play(Create(warn_bg), Write(warn), run_time=0.5)

        # 方法：分子分母拆开
        method_title = Text(
            "用公式：",
            font="Noto Sans CJK SC", font_size=26, color=GRAY_A,
        ).move_to(UP * 3.0)
        method_f = MathTex(
            r"\sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}}",
            font_size=42, color=self.C_FORMULA,
        ).move_to(UP * 2.1)
        self.play(FadeIn(method_title), Write(method_f), run_time=0.7)

        # 逐步推导
        steps_e3 = [
            (r"\sqrt{\dfrac{3}{4}}", UP * 0.9),
            (r"= \dfrac{\sqrt{3}}{\sqrt{4}}", DOWN * 0.2),
            (r"= \dfrac{\sqrt{3}}{2}", DOWN * 1.3),
        ]
        colors_e3 = [WHITE, GRAY_A, self.C_RIGHT]

        for (expr, pos), col in zip(steps_e3, colors_e3):
            tex = MathTex(expr, font_size=52, color=col).move_to(pos)
            self.play(Write(tex), run_time=0.5)
            self.wait(0.4)

        # 结论
        ans_bg = self.make_card(6.5, 1.6, self.C_RIGHT, DOWN * 2.7, fill="#0a2e1a", alpha=0.9)
        ans_f  = MathTex(
            r"\sqrt{\dfrac{3}{4}} = \dfrac{\sqrt{3}}{2}",
            font_size=44, color=WHITE,
        ).move_to(DOWN * 2.7)
        self.play(Create(ans_bg), Write(ans_f), run_time=0.6)
        self.play(Indicate(ans_f, color=self.C_RIGHT, scale_factor=1.06), run_time=0.6)
        self.wait(2.0)

        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 7: 快速判断练习
    # ═══════════════════════════════════════════════════
    def scene_judge(self):
        title = Text(
            "判断哪些是最简二次根式？",
            font="Noto Sans CJK SC", font_size=34, color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # (表达式LaTeX, 是否最简, 理由)
        items = [
            (r"\sqrt{3}",            True,  "被开方数无分母，无完全平方因数"),
            (r"\sqrt{8}",            False, "8=4×2，4可开方"),
            (r"\sqrt{\dfrac{2}{3}}", False, "根号内含分母"),
            (r"3\sqrt{5}",           True,  "5无完全平方因数"),
            (r"\sqrt{a^2}",          False, "a²可以完全开方=a"),
        ]

        card_h = 1.45
        start_y = 5.4
        gap = 1.55

        for i, (expr, correct, reason) in enumerate(items):
            pos_y = start_y - i * gap
            pos = UP * pos_y

            col = self.C_RIGHT if correct else self.C_WRONG
            symbol = "✓" if correct else "✗"

            bg = self.make_card(7.6, card_h, col, pos)
            form = MathTex(expr, font_size=40, color=WHITE)
            sym  = Text(symbol, font="Noto Sans CJK SC", font_size=32, color=col)
            note = Text(reason, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
            VGroup(form, sym, note).arrange(RIGHT, buff=0.35).move_to(pos)

            self.play(Create(bg), run_time=0.18)
            self.play(Write(form), FadeIn(sym, scale=1.2), FadeIn(note), run_time=0.42)
            self.wait(0.25)

        self.wait(1.5)
        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 8: 总结
    # ═══════════════════════════════════════════════════
    def scene_summary(self):
        title = Text(
            "知识点总结",
            font="Noto Sans CJK SC", font_size=46, color=self.C_TITLE,
        ).move_to(UP * 6.6)
        self.play(Write(title), run_time=0.5)

        # 定义框
        def_bg = self.make_card(7.6, 1.5, self.C_FORMULA, UP * 5.5)
        def_t  = Text("最简二次根式定义", font="Noto Sans CJK SC", font_size=28, color=self.C_FORMULA).move_to(UP * 5.5)
        self.play(Create(def_bg), Write(def_t), run_time=0.5)

        # 条件1
        c1_bg = self.make_card(7.6, 1.6, self.C_FORMULA, UP * 3.9)
        c1_t  = Text("条件 ①  根号内无分母", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        c1_f  = MathTex(r"\sqrt{\tfrac{a}{b}} \rightarrow \tfrac{\sqrt{a}}{\sqrt{b}}", font_size=32, color=self.C_FORMULA)
        VGroup(c1_t, c1_f).arrange(RIGHT, buff=0.4).move_to(UP * 3.9)
        self.play(Create(c1_bg), Write(c1_t), Write(c1_f), run_time=0.55)

        # 条件2
        c2_bg = self.make_card(7.6, 1.6, self.C_RULE, UP * 2.1)
        c2_t  = Text("条件 ②  无完全平方因数", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        c2_f  = MathTex(r"\sqrt{a^2 b} \rightarrow a\sqrt{b}", font_size=32, color=self.C_RULE)
        VGroup(c2_t, c2_f).arrange(RIGHT, buff=0.4).move_to(UP * 2.1)
        self.play(Create(c2_bg), Write(c2_t), Write(c2_f), run_time=0.55)

        # 化简公式卡
        formulas = [
            r"\sqrt{12} = 2\sqrt{3}",
            r"\sqrt{a^2 b} = a\sqrt{b}",
            r"\sqrt{\tfrac{a}{b}} = \tfrac{\sqrt{a}}{\sqrt{b}}",
        ]
        f_bg = self.make_card(7.6, 3.0, self.C_TITLE, DOWN * 0.45, fill="#0f3460", alpha=0.9)
        f_title = Text("核心公式", font="Noto Sans CJK SC", font_size=26, color=self.C_TITLE).move_to(DOWN * 0.45 + UP * 1.1)
        f_group = VGroup(*[MathTex(f, font_size=30, color=WHITE) for f in formulas])
        f_group.arrange(DOWN, buff=0.32).move_to(DOWN * 0.45 + DOWN * 0.25)

        self.play(Create(f_bg), Write(f_title), run_time=0.4)
        for ff in f_group:
            self.play(Write(ff), run_time=0.4)
        self.wait(2.0)

        self.fade_all_except_author()

    # ═══════════════════════════════════════════════════
    #  Scene 9: 片尾
    # ═══════════════════════════════════════════════════
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

        # 装饰性公式
        deco = VGroup(
            MathTex(r"\sqrt{12} = 2\sqrt{3}", font_size=30, color=self.C_FORMULA),
            MathTex(r"\sqrt{a^2 b} = a\sqrt{b}", font_size=30, color=self.C_RULE),
            MathTex(r"\sqrt{\tfrac{a}{b}} = \tfrac{\sqrt{a}}{\sqrt{b}}", font_size=30, color=self.C_FORMULA),
        ).arrange(DOWN, buff=0.45).move_to(DOWN * 1.8)

        self.play(*[Write(f) for f in deco], run_time=1.0)
        self.play(
            *[Indicate(f, color=self.C_TITLE) for f in deco],
            run_time=0.9,
        )
        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# 渲染命令:
# manim -pql simplest_radical.py SimplestRadical    # 快速预览
# manim -qh  simplest_radical.py SimplestRadical    # 高质量输出
"""
二次根式的概念 - 教学动画
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


class QuadraticRadical(Scene):
    """
    二次根式的概念教学动画
    场景:
    1. 开场钩子
    2. 什么是二次根式
    3. 有意义的条件 a≥0
    4. 正例与反例
    5. 双重非负性
    6. 数轴可视化
    7. 总结
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.C_TITLE = "#f9ca24"
        self.C_FORMULA = "#6ab04c"
        self.C_VALID = "#22a6b3"
        self.C_INVALID = "#eb4d4b"
        self.C_HIGHLIGHT = "#f0932b"
        self.C_RULE = "#a29bfe"
        self.C_NEUTRAL = GRAY_A

        self.scene_opening()
        self.scene_definition()
        self.scene_condition()
        self.scene_examples()
        self.scene_double_nonneg()
        self.scene_summary()
        self.scene_outro()

    # ─────────────────────────── Scene 1 ───────────────────────────
    def scene_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B,
        ).move_to(UP * 7.2)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.3)
        self.author = author  # 保留至结尾

        # 章节标签
        chapter = Text(
            "八年级 · 第十六章",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 6.5)
        self.play(FadeIn(chapter), run_time=0.3)

        # 钩子问题
        hook = Text(
            "√(-4) 有意义吗？",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.C_TITLE,
        ).move_to(UP * 5.0)

        self.play(Write(hook), run_time=0.9)

        # 大公式展示
        big_formula = MathTex(r"\sqrt{a}", font_size=150, color=self.C_FORMULA).move_to(UP * 2.5)
        self.play(GrowFromCenter(big_formula), run_time=1.0)
        self.wait(0.5)

        # 悬念提示
        question = Text(
            "a 可以是任意数吗？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
        ).move_to(UP * 0.5)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(big_formula),
            FadeOut(question),
            FadeOut(chapter),
            run_time=0.5,
        )

    # ─────────────────────────── Scene 2 ───────────────────────────
    def scene_definition(self):
        # 标题
        title = Text(
            "二次根式",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.C_TITLE,
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.7)

        subtitle = Text(
            "Quadratic Radical",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_B,
        ).move_to(UP * 5.2)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 定义框
        def_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.5,
            height=2.2,
            color=self.C_FORMULA,
            stroke_width=2,
            fill_color="#0f3460",
            fill_opacity=0.8,
        ).move_to(UP * 3.5)
        self.play(Create(def_box), run_time=0.5)

        def_text = Text(
            "形如",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE,
        )
        def_formula = MathTex(r"\sqrt{a}\ (a \geq 0)", font_size=42, color=self.C_FORMULA)
        def_text2 = Text(
            "的式子",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE,
        )
        def_line = VGroup(def_text, def_formula, def_text2).arrange(RIGHT, buff=0.2).move_to(UP * 3.8)

        def_name = Text(
            "叫做二次根式",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_TITLE,
        ).move_to(UP * 3.1)

        self.play(Write(def_text), Write(def_formula), Write(def_text2), run_time=0.8)
        self.play(Write(def_name), run_time=0.5)
        self.wait(0.5)

        # 解析结构图
        struct_title = Text(
            "结构解析",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A,
        ).move_to(UP * 2.0)
        self.play(FadeIn(struct_title), run_time=0.3)

        main_formula = MathTex(r"\sqrt{a}", font_size=100, color=WHITE).move_to(UP * 0.8)
        self.play(Write(main_formula), run_time=0.5)

        # 箭头标注
        # 根号符号标注
        arr1 = Arrow(
            start=np.array([-2.5, -0.2, 0]),
            end=np.array([-1.2, 0.7, 0]),
            color=self.C_HIGHLIGHT,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        label1 = Text(
            "根号（√）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_HIGHLIGHT,
        ).move_to(np.array([-3.0, -0.5, 0]))

        # 被开方数标注
        arr2 = Arrow(
            start=np.array([2.5, -0.2, 0]),
            end=np.array([0.8, 0.7, 0]),
            color=self.C_VALID,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15,
        )
        label2 = Text(
            "被开方数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_VALID,
        ).move_to(np.array([3.0, -0.5, 0]))
        label2b = Text(
            "（a）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_VALID,
        ).move_to(np.array([3.0, -0.9, 0]))

        self.play(
            GrowArrow(arr1), Write(label1),
            GrowArrow(arr2), Write(label2), Write(label2b),
            run_time=0.8,
        )

        # 2次根式说明
        note = Text(
            "'二次'指开2次方（平方根）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(def_box),
            FadeOut(def_line),
            FadeOut(def_name),
            FadeOut(struct_title),
            FadeOut(main_formula),
            FadeOut(arr1), FadeOut(label1),
            FadeOut(arr2), FadeOut(label2), FadeOut(label2b),
            FadeOut(note),
            run_time=0.5,
        )

    # ─────────────────────────── Scene 3 ───────────────────────────
    def scene_condition(self):
        title = Text(
            "有意义的条件",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.C_TITLE,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 核心问题
        q_text = Text(
            "什么时候",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
        )
        q_formula = MathTex(r"\sqrt{a}", font_size=50, color=self.C_FORMULA)
        q_text2 = Text(
            "有意义？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
        )
        q_group = VGroup(q_text, q_formula, q_text2).arrange(RIGHT, buff=0.2).move_to(UP * 5.1)
        self.play(Write(q_group), run_time=0.6)

        # 三种情况演示
        # Case 1: a > 0
        case1_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=2.0,
            color=self.C_VALID, stroke_width=2,
            fill_color="#0f3460", fill_opacity=0.6,
        ).move_to(UP * 3.3)
        case1_label = Text("a > 0  正数", font="Noto Sans CJK SC", font_size=26, color=self.C_VALID)
        case1_ex = MathTex(r"\sqrt{4} = 2\quad \sqrt{9} = 3", font_size=30, color=WHITE)
        case1_check = Text("✓ 有意义", font="Noto Sans CJK SC", font_size=24, color=self.C_VALID)
        VGroup(case1_label, case1_ex, case1_check).arrange(RIGHT, buff=0.4).move_to(UP * 3.3)

        self.play(Create(case1_bg), run_time=0.3)
        self.play(Write(case1_label), Write(case1_ex), Write(case1_check), run_time=0.7)
        self.wait(0.5)

        # Case 2: a = 0
        case2_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=2.0,
            color=self.C_VALID, stroke_width=2,
            fill_color="#0f3460", fill_opacity=0.6,
        ).move_to(UP * 1.2)
        case2_label = Text("a = 0  零", font="Noto Sans CJK SC", font_size=26, color=self.C_VALID)
        case2_ex = MathTex(r"\sqrt{0} = 0", font_size=30, color=WHITE)
        case2_check = Text("✓ 有意义", font="Noto Sans CJK SC", font_size=24, color=self.C_VALID)
        VGroup(case2_label, case2_ex, case2_check).arrange(RIGHT, buff=0.4).move_to(UP * 1.2)

        self.play(Create(case2_bg), run_time=0.3)
        self.play(Write(case2_label), Write(case2_ex), Write(case2_check), run_time=0.7)
        self.wait(0.5)

        # Case 3: a < 0
        case3_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=2.0,
            color=self.C_INVALID, stroke_width=2,
            fill_color="#2d0a0a", fill_opacity=0.8,
        ).move_to(DOWN * 0.9)
        case3_label = Text("a < 0  负数", font="Noto Sans CJK SC", font_size=26, color=self.C_INVALID)
        case3_ex = MathTex(r"\sqrt{-4} = \;?", font_size=30, color=WHITE)
        case3_check = Text("✗ 无意义!", font="Noto Sans CJK SC", font_size=24, color=self.C_INVALID)
        VGroup(case3_label, case3_ex, case3_check).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.9)

        self.play(Create(case3_bg), run_time=0.3)
        self.play(Write(case3_label), Write(case3_ex), Write(case3_check), run_time=0.7)
        self.wait(0.8)

        # 关键规则框
        rule_bg = RoundedRectangle(
            corner_radius=0.3, width=7.5, height=1.6,
            color=self.C_RULE, stroke_width=3,
            fill_color="#16213e", fill_opacity=0.9,
        ).move_to(DOWN * 3.0)

        rule_text = Text("关键规则：", font="Noto Sans CJK SC", font_size=26, color=self.C_RULE)
        rule_formula_l = MathTex(r"\sqrt{a}", font_size=30, color=self.C_TITLE)
        rule_formula_mid = Text("有意义", font="Noto Sans CJK SC", font_size=26, color=self.C_TITLE)
        rule_formula_r = MathTex(r"\Longleftrightarrow\ a \geq 0", font_size=30, color=self.C_TITLE)
        rule_formula = VGroup(rule_formula_l, rule_formula_mid, rule_formula_r).arrange(RIGHT, buff=0.15)
        VGroup(rule_text, rule_formula).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        self.play(Create(rule_bg), run_time=0.4)
        self.play(Write(rule_text), Write(rule_formula), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(q_group),
            FadeOut(case1_bg), FadeOut(case1_label), FadeOut(case1_ex), FadeOut(case1_check),
            FadeOut(case2_bg), FadeOut(case2_label), FadeOut(case2_ex), FadeOut(case2_check),
            FadeOut(case3_bg), FadeOut(case3_label), FadeOut(case3_ex), FadeOut(case3_check),
            FadeOut(rule_bg), FadeOut(rule_text), FadeOut(rule_formula),
            run_time=0.5,
        )

    # ─────────────────────────── Scene 4 ───────────────────────────
    def scene_examples(self):
        title = Text(
            "来做几道判断题！",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 例题数据: (LaTeX表达式, 是否有意义, 理由)
        examples = [
            (r"\sqrt{5}", True, "5 > 0"),
            (r"\sqrt{0}", True, "0 ≥ 0"),
            (r"\sqrt{-3}", False, "-3 < 0"),
            (r"\sqrt{x+1}", None, "需要 x+1 ≥ 0"),
        ]

        card_positions = [UP * 5.0, UP * 3.0, UP * 1.0, DOWN * 1.0]

        for i, (expr, valid, reason) in enumerate(examples):
            pos = card_positions[i]

            if valid is True:
                col = self.C_VALID
                symbol = "✓"
                reason_col = self.C_VALID
            elif valid is False:
                col = self.C_INVALID
                symbol = "✗"
                reason_col = self.C_INVALID
            else:
                col = self.C_HIGHLIGHT
                symbol = "？"
                reason_col = self.C_HIGHLIGHT

            # 卡片
            card_bg = RoundedRectangle(
                corner_radius=0.25, width=7.5, height=1.6,
                color=col, stroke_width=1.5,
                fill_color="#16213e", fill_opacity=0.7,
            ).move_to(pos)

            formula = MathTex(expr, font_size=44, color=WHITE)
            sym = Text(symbol, font="Noto Sans CJK SC", font_size=36, color=col)
            reason_text = Text(reason, font="Noto Sans CJK SC", font_size=20, color=reason_col)

            group = VGroup(formula, sym, reason_text).arrange(RIGHT, buff=0.5).move_to(pos)

            self.play(Create(card_bg), run_time=0.2)
            self.play(
                Write(formula),
                FadeIn(sym, scale=1.3),
                FadeIn(reason_text),
                run_time=0.5,
            )
            self.wait(0.4)

        # 条件题重点说明
        note = Text(
            "含字母时，令被开方数 ≥ 0 求解",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 2.5)
        cond_formula = MathTex(r"x + 1 \geq 0 \;\Rightarrow\; x \geq -1", font_size=30, color=self.C_HIGHLIGHT).move_to(DOWN * 3.3)

        self.play(FadeIn(note), Write(cond_formula), run_time=0.8)
        self.wait(2.0)

        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.author], run_time=0.5)

    # ─────────────────────────── Scene 5 ───────────────────────────
    def scene_double_nonneg(self):
        title = Text(
            "双重非负性",
            font="Noto Sans CJK SC",
            font_size=50,
            color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.7)

        subtitle = Text(
            "二次根式有两个'非负'",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A,
        ).move_to(UP * 5.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 两个非负性
        # 1: a ≥ 0
        box1 = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.5,
            color=self.C_VALID, stroke_width=2,
            fill_color="#0a2e1a", fill_opacity=0.8,
        ).move_to(UP * 3.8)
        title1 = Text("① 被开方数非负", font="Noto Sans CJK SC", font_size=28, color=self.C_VALID).move_to(UP * 4.35)
        formula1 = MathTex(r"a \geq 0", font_size=52, color=WHITE).move_to(UP * 3.65)
        note1 = Text("（二次根式存在的前提）", font="Noto Sans CJK SC", font_size=18, color=GRAY_A).move_to(UP * 3.0)

        self.play(Create(box1), run_time=0.4)
        self.play(Write(title1), Write(formula1), FadeIn(note1), run_time=0.7)
        self.wait(0.5)

        # 2: √a ≥ 0
        box2 = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.5,
            color=self.C_RULE, stroke_width=2,
            fill_color="#0a0a2e", fill_opacity=0.8,
        ).move_to(UP * 1.5)
        title2 = Text("② 根式的值非负", font="Noto Sans CJK SC", font_size=28, color=self.C_RULE).move_to(UP * 2.05)
        formula2 = MathTex(r"\sqrt{a} \geq 0", font_size=52, color=WHITE).move_to(UP * 1.35)
        note2 = Text("（算术平方根 ≥ 0）", font="Noto Sans CJK SC", font_size=18, color=GRAY_A).move_to(UP * 0.7)

        self.play(Create(box2), run_time=0.4)
        self.play(Write(title2), Write(formula2), FadeIn(note2), run_time=0.7)
        self.wait(0.5)

        # 合并展示
        combined_bg = RoundedRectangle(
            corner_radius=0.3, width=7.5, height=1.8,
            color=self.C_TITLE, stroke_width=3,
            fill_color="#16213e", fill_opacity=0.9,
        ).move_to(DOWN * 0.8)
        combined_label = Text("双重非负：", font="Noto Sans CJK SC", font_size=26, color=self.C_TITLE)
        combined_f1 = MathTex(r"a \geq 0", font_size=32, color=WHITE)
        combined_and = Text("且", font="Noto Sans CJK SC", font_size=28, color=WHITE)
        combined_f2 = MathTex(r"\sqrt{a} \geq 0", font_size=32, color=WHITE)
        combined_formula = VGroup(combined_f1, combined_and, combined_f2).arrange(RIGHT, buff=0.2)
        VGroup(combined_label, combined_formula).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.8)

        self.play(Create(combined_bg), run_time=0.4)
        self.play(Write(combined_label), Write(combined_formula), run_time=0.7)

        # 特殊结论
        special = Text(
            "若 √a = 0，则 a = 0",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_HIGHLIGHT,
        ).move_to(DOWN * 2.3)
        special2 = Text(
            "（等号成立当且仅当 a = 0）",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A,
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(special, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(special2), run_time=0.4)
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.author], run_time=0.5)

    # ─────────────────────────── Scene 6 ───────────────────────────
    def scene_summary(self):
        title = Text(
            "知识点总结",
            font="Noto Sans CJK SC",
            font_size=46,
            color=self.C_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 数轴可视化
        axis_label = Text(
            "a 的范围 → 数轴",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A,
        ).move_to(UP * 5.5)
        self.play(FadeIn(axis_label), run_time=0.3)

        # 数轴
        number_line = NumberLine(
            x_range=[-4, 4, 1],
            length=7,
            color=WHITE,
            include_numbers=True,
            numbers_to_include=[-3, -2, -1, 0, 1, 2, 3],
        ).move_to(UP * 4.3)
        self.play(Create(number_line), run_time=0.8)

        # 非负区域标记 (a ≥ 0)
        valid_region = Line(
            number_line.n2p(0), number_line.n2p(3.8),
            color=self.C_VALID, stroke_width=8,
        )
        valid_dot = Dot(number_line.n2p(0), color=self.C_VALID, radius=0.1)
        valid_arrow = Arrow(
            number_line.n2p(3.2), number_line.n2p(3.8),
            color=self.C_VALID, stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        )
        valid_label = Text("√a 有意义", font="Noto Sans CJK SC", font_size=20, color=self.C_VALID).next_to(number_line, UP, buff=0.15).shift(RIGHT * 1.5)

        # 负区域标记 (a < 0)
        invalid_region = Line(
            number_line.n2p(-3.8), number_line.n2p(0),
            color=self.C_INVALID, stroke_width=8,
        )
        invalid_open_dot = Circle(radius=0.1, color=self.C_INVALID, stroke_width=2).move_to(number_line.n2p(0))
        invalid_label = Text("√a 无意义", font="Noto Sans CJK SC", font_size=20, color=self.C_INVALID).next_to(number_line, UP, buff=0.15).shift(LEFT * 1.5)

        self.play(
            Create(valid_region), FadeIn(valid_dot),
            run_time=0.5,
        )
        self.play(FadeIn(valid_label), run_time=0.3)
        self.play(
            Create(invalid_region), Create(invalid_open_dot),
            run_time=0.5,
        )
        self.play(FadeIn(invalid_label), run_time=0.3)
        self.wait(0.5)

        # 三条核心规则
        rules = [
            (r"\sqrt{a}\ (a \geq 0)", "① 定义"),
            (r"\sqrt{a} \Leftrightarrow a \geq 0", "② 有意义条件"),
            (r"a \geq 0 \;\&\; \sqrt{a} \geq 0", "③ 双重非负性"),
        ]
        rule_positions = [UP * 2.2, UP * 0.5, DOWN * 1.2]

        for i, ((formula_str, label_str), pos) in enumerate(zip(rules, rule_positions)):
            bg = RoundedRectangle(
                corner_radius=0.25, width=7.5, height=1.5,
                color=[self.C_FORMULA, self.C_VALID, self.C_RULE][i],
                stroke_width=1.5,
                fill_color="#16213e", fill_opacity=0.7,
            ).move_to(pos)
            lbl = Text(label_str, font="Noto Sans CJK SC", font_size=22,
                       color=[self.C_FORMULA, self.C_VALID, self.C_RULE][i])
            fml = MathTex(formula_str, font_size=26, color=WHITE)
            VGroup(lbl, fml).arrange(RIGHT, buff=0.4).move_to(pos)

            self.play(Create(bg), run_time=0.2)
            self.play(Write(lbl), Write(fml), run_time=0.5)
            self.wait(0.2)

        self.wait(2.0)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.author], run_time=0.6)

    # ─────────────────────────── Scene 7 ───────────────────────────
    def scene_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE,
        ).move_to(UP * 2.5)
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B,
        ).move_to(UP * 1.6)

        self.play(
            Transform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 结束语
        follow = Text(
            "关注我，学更多数学知识！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.C_TITLE,
        ).move_to(UP * 0.3)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)

        # 装饰性公式展示
        formulas = VGroup(
            MathTex(r"\sqrt{a}\ (a \geq 0)", font_size=28, color=self.C_FORMULA),
            MathTex(r"a \geq 0", font_size=28, color=self.C_VALID),
            MathTex(r"\sqrt{a} \geq 0", font_size=28, color=self.C_RULE),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 1.8)

        self.play(
            *[Write(f) for f in formulas],
            run_time=1.0,
        )

        # 闪烁结束
        self.play(
            *[Indicate(f, color=self.C_HIGHLIGHT) for f in formulas],
            run_time=1.0,
        )
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.0)


# 运行命令:
# manim -pql quadratic_radical.py QuadraticRadical     # 快速预览
# manim -qh quadratic_radical.py QuadraticRadical      # 高质量
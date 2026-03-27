"""
加法交换律与结合律 - Addition Commutative and Associative Laws
四年级第二学期第一章复习与提高
TikTok竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class AdditionLawLesson(Scene):
    """
    加法交换律与结合律教学动画

    场景顺序:
    1. 开场钩子
    2. 加法交换律定义与演示
    3. 交换律图形演示 (色块交换)
    4. 加法结合律定义与演示
    5. 结合律图形演示 (括号变换)
    6. 综合示例: 简便运算 25+37+75
    7. 总结与结尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_A = "#e74c3c"       # 红 - 数字a
        self.COLOR_B = "#3498db"       # 蓝 - 数字b
        self.COLOR_C = "#2ecc71"       # 绿 - 数字c
        self.COLOR_HIGHLIGHT = "#f1c40f"   # 黄 - 高亮
        self.COLOR_RESULT = "#e67e22"  # 橙 - 结果
        self.COLOR_ARROW = "#9b59b6"   # 紫 - 箭头
        self.COLOR_FORMULA = WHITE

        # 品牌标识 (顶部固定)
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_commutative_law()
        self.scene_3_commutative_visual()
        self.scene_4_associative_law()
        self.scene_5_associative_visual()
        self.scene_6_example()
        self.scene_7_summary()

    # ────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ────────────────────────────────────────────
    def scene_1_opening(self):
        # 钩子问题
        hook_line1 = Text(
            "25 + 37 + 75",
            font="Noto Sans CJK SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)

        hook_line2 = Text(
            "你能秒算吗？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 3.5)

        self.play(FadeIn(hook_line1, shift=DOWN * 0.3), run_time=0.6)
        self.play(Write(hook_line2), run_time=0.7)
        self.wait(1.0)

        # 副标题
        subtitle = Text(
            "用加法定律，轻松搞定！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_C
        ).move_to(UP * 2.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 主标题
        main_title = Text(
            "加法交换律 & 结合律",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.3)

        self.play(Write(main_title), run_time=0.9)
        self.wait(0.7)

        # 清理
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(subtitle),
            FadeOut(main_title),
            run_time=0.5
        )

    # ────────────────────────────────────────────
    # Scene 2: 加法交换律定义
    # ────────────────────────────────────────────
    def scene_2_commutative_law(self):
        # 标题
        title = Text(
            "加法交换律",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.7)

        # 定义文字
        def_text = Text(
            "两个数相加，交换加数的位置，",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.0)
        def_text2 = Text(
            "和不变。",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.4)

        self.play(FadeIn(def_text), FadeIn(def_text2), run_time=0.6)
        self.wait(0.5)

        # 公式: a + b = b + a
        formula_a = MathTex(r"a", font_size=60, color=self.COLOR_A)
        formula_plus1 = MathTex(r"+", font_size=60, color=WHITE)
        formula_b = MathTex(r"b", font_size=60, color=self.COLOR_B)
        formula_eq = MathTex(r"=", font_size=60, color=WHITE)
        formula_b2 = MathTex(r"b", font_size=60, color=self.COLOR_B)
        formula_plus2 = MathTex(r"+", font_size=60, color=WHITE)
        formula_a2 = MathTex(r"a", font_size=60, color=self.COLOR_A)

        formula_row = VGroup(
            formula_a, formula_plus1, formula_b,
            formula_eq,
            formula_b2, formula_plus2, formula_a2
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.0)

        self.play(FadeIn(formula_row, scale=0.85), run_time=0.8)
        self.wait(0.5)

        # 交换箭头 (弧形箭头 a↔b)
        arrow_ab = CurvedArrow(
            formula_a.get_top() + UP * 0.1,
            formula_b.get_top() + UP * 0.1,
            angle=-PI / 2.5,
            color=self.COLOR_ARROW,
            tip_length=0.18
        )
        self.play(Create(arrow_ab), run_time=0.7)
        self.wait(0.4)

        # 具体示例: 3 + 5 = 5 + 3
        example_label = Text(
            "举例：",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 1.7 + LEFT * 2.8)

        ex_3 = MathTex(r"3", font_size=56, color=self.COLOR_A)
        ex_plus1 = MathTex(r"+", font_size=56, color=WHITE)
        ex_5 = MathTex(r"5", font_size=56, color=self.COLOR_B)
        ex_eq = MathTex(r"=", font_size=56, color=WHITE)
        ex_5b = MathTex(r"5", font_size=56, color=self.COLOR_B)
        ex_plus2 = MathTex(r"+", font_size=56, color=WHITE)
        ex_3b = MathTex(r"3", font_size=56, color=self.COLOR_A)

        example_row = VGroup(
            ex_3, ex_plus1, ex_5,
            ex_eq,
            ex_5b, ex_plus2, ex_3b
        ).arrange(RIGHT, buff=0.15).move_to(UP * 1.0)

        self.play(FadeIn(example_label), FadeIn(example_row), run_time=0.7)

        # 结果标注
        result_text = Text(
            "= 8        = 8",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_RESULT
        ).move_to(UP * 0.1)
        # Use MathTex for = 8 parts
        res_left = MathTex(r"= 8", font_size=48, color=self.COLOR_RESULT).move_to(UP * 0.1 + LEFT * 1.5)
        res_right = MathTex(r"= 8", font_size=48, color=self.COLOR_RESULT).move_to(UP * 0.1 + RIGHT * 1.5)

        self.play(FadeIn(res_left), FadeIn(res_right), run_time=0.6)
        self.wait(1.2)

        # 保存标题引用, 清理
        self.commutative_title = title
        self.play(
            FadeOut(def_text), FadeOut(def_text2),
            FadeOut(formula_row), FadeOut(arrow_ab),
            FadeOut(example_label), FadeOut(example_row),
            FadeOut(res_left), FadeOut(res_right),
            run_time=0.5
        )

    # ────────────────────────────────────────────
    # Scene 3: 交换律图形演示 (色块交换)
    # ────────────────────────────────────────────
    def scene_3_commutative_visual(self):
        # 保留标题
        section_label = Text(
            "图形演示",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.0)
        self.play(FadeIn(section_label), run_time=0.4)

        # 色块 A (红) 和 B (蓝)
        block_a = RoundedRectangle(
            corner_radius=0.2,
            width=2.2, height=1.2,
            fill_color=self.COLOR_A,
            fill_opacity=0.9,
            stroke_width=0
        )
        label_a = Text("a = 3", font="Noto Sans CJK SC", font_size=28, color=WHITE)

        block_b = RoundedRectangle(
            corner_radius=0.2,
            width=2.2, height=1.2,
            fill_color=self.COLOR_B,
            fill_opacity=0.9,
            stroke_width=0
        )
        label_b = Text("b = 5", font="Noto Sans CJK SC", font_size=28, color=WHITE)

        # 初始排列: [A] + [B]
        group_a = VGroup(block_a, label_a).arrange(DOWN, buff=0)
        group_b = VGroup(block_b, label_b).arrange(DOWN, buff=0)
        # Flatten: labels inside blocks
        label_a.move_to(block_a.get_center())
        label_b.move_to(block_b.get_center())

        plus_sign = MathTex(r"+", font_size=64, color=WHITE)
        eq_sign = MathTex(r"=", font_size=64, color=WHITE)

        # Position: A + B  on top row
        block_a.move_to(UP * 3.5 + LEFT * 2.5)
        label_a.move_to(block_a.get_center())
        plus_sign.move_to(UP * 3.5)
        block_b.move_to(UP * 3.5 + RIGHT * 2.5)
        label_b.move_to(block_b.get_center())

        self.play(
            FadeIn(block_a), FadeIn(label_a),
            FadeIn(plus_sign),
            FadeIn(block_b), FadeIn(label_b),
            run_time=0.7
        )
        self.wait(0.5)

        # 交换动画: A 和 B 互换位置
        swap_arrow1 = CurvedArrow(
            block_a.get_top() + UP * 0.15,
            block_b.get_top() + UP * 0.15,
            angle=-PI / 3,
            color=self.COLOR_ARROW,
            tip_length=0.2
        )
        swap_arrow2 = CurvedArrow(
            block_b.get_bottom() + DOWN * 0.15,
            block_a.get_bottom() + DOWN * 0.15,
            angle=-PI / 3,
            color=self.COLOR_ARROW,
            tip_length=0.2
        )
        self.play(Create(swap_arrow1), Create(swap_arrow2), run_time=0.5)

        # 移动色块交换
        pos_a = block_a.get_center().copy()
        pos_b = block_b.get_center().copy()
        self.play(
            block_a.animate.move_to(pos_b),
            label_a.animate.move_to(pos_b),
            block_b.animate.move_to(pos_a),
            label_b.animate.move_to(pos_a),
            run_time=1.0,
            rate_func=smooth
        )
        self.wait(0.4)
        self.play(FadeOut(swap_arrow1), FadeOut(swap_arrow2), run_time=0.3)

        # 显示结果相同
        result_same = Text(
            "和不变！",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.1)

        sum_show = MathTex(r"3 + 5 = 5 + 3 = 8", font_size=46, color=self.COLOR_RESULT).move_to(UP * 1.3)
        self.play(FadeIn(result_same, scale=1.1), run_time=0.5)
        self.play(Write(sum_show), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(block_a), FadeOut(label_a),
            FadeOut(block_b), FadeOut(label_b),
            FadeOut(plus_sign),
            FadeOut(result_same),
            FadeOut(sum_show),
            FadeOut(section_label),
            FadeOut(self.commutative_title),
            run_time=0.5
        )

    # ────────────────────────────────────────────
    # Scene 4: 加法结合律定义
    # ────────────────────────────────────────────
    def scene_4_associative_law(self):
        # 标题
        title = Text(
            "加法结合律",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_C
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.7)
        self.assoc_title = title

        # 定义文字
        def_text = Text(
            "三个数相加，先加前两个",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.0)
        def_text2 = Text(
            "或先加后两个，和不变。",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.4)

        self.play(FadeIn(def_text), FadeIn(def_text2), run_time=0.6)
        self.wait(0.5)

        # 公式: (a + b) + c = a + (b + c)
        # Left side: (a + b) + c
        lp1 = MathTex(r"(", font_size=62, color=WHITE)
        la = MathTex(r"a", font_size=62, color=self.COLOR_A)
        lplus = MathTex(r"+", font_size=62, color=WHITE)
        lb = MathTex(r"b", font_size=62, color=self.COLOR_B)
        lp2 = MathTex(r")", font_size=62, color=WHITE)
        lplus2 = MathTex(r"+", font_size=62, color=WHITE)
        lc = MathTex(r"c", font_size=62, color=self.COLOR_C)
        eq = MathTex(r"=", font_size=62, color=WHITE)
        # Right side: a + (b + c)
        ra = MathTex(r"a", font_size=62, color=self.COLOR_A)
        rplus = MathTex(r"+", font_size=62, color=WHITE)
        rp1 = MathTex(r"(", font_size=62, color=WHITE)
        rb = MathTex(r"b", font_size=62, color=self.COLOR_B)
        rplus2 = MathTex(r"+", font_size=62, color=WHITE)
        rc = MathTex(r"c", font_size=62, color=self.COLOR_C)
        rp2 = MathTex(r")", font_size=62, color=WHITE)

        left_formula = VGroup(lp1, la, lplus, lb, lp2, lplus2, lc).arrange(RIGHT, buff=0.08)
        right_formula = VGroup(ra, rplus, rp1, rb, rplus2, rc, rp2).arrange(RIGHT, buff=0.08)
        full_formula = VGroup(left_formula, eq, right_formula).arrange(RIGHT, buff=0.18)
        full_formula.move_to(UP * 3.0)
        # Scale down if too wide
        if full_formula.width > 8.2:
            full_formula.scale(8.2 / full_formula.width)

        self.play(FadeIn(full_formula, scale=0.85), run_time=0.9)
        self.wait(0.5)

        # 括号高亮: 先框住 (a+b)
        brace_ab = Brace(VGroup(lp1, la, lplus, lb, lp2), direction=DOWN, color=self.COLOR_HIGHLIGHT)
        brace_ab_label = Text("先加", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_HIGHLIGHT)
        brace_ab_label.next_to(brace_ab, DOWN, buff=0.1)

        self.play(Create(brace_ab), FadeIn(brace_ab_label), run_time=0.6)
        self.wait(0.6)

        # 括号高亮: 右边 (b+c)
        brace_bc = Brace(VGroup(rp1, rb, rplus2, rc, rp2), direction=DOWN, color=self.COLOR_B)
        brace_bc_label = Text("也可先加", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_B)
        brace_bc_label.next_to(brace_bc, DOWN, buff=0.1)

        self.play(Create(brace_bc), FadeIn(brace_bc_label), run_time=0.6)
        self.wait(0.8)

        # 具体示例: (2+3)+4 = 2+(3+4)
        example_label = Text(
            "举例：",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 0.7 + LEFT * 2.8)

        ex_formula = MathTex(
            r"(2+3)+4 = 2+(3+4)",
            font_size=46,
            color=WHITE
        ).move_to(UP * 0.0)
        ex_formula[0][1].set_color(self.COLOR_A)    # 2
        ex_formula[0][3].set_color(self.COLOR_B)    # 3
        ex_formula[0][5].set_color(self.COLOR_C)    # 4

        self.play(FadeIn(example_label), Write(ex_formula), run_time=0.8)

        ex_result = MathTex(r"= 5 + 4 = 9 \quad = 2 + 7 = 9", font_size=38, color=self.COLOR_RESULT).move_to(DOWN * 0.9)
        self.play(Write(ex_result), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(def_text), FadeOut(def_text2),
            FadeOut(full_formula),
            FadeOut(brace_ab), FadeOut(brace_ab_label),
            FadeOut(brace_bc), FadeOut(brace_bc_label),
            FadeOut(example_label), FadeOut(ex_formula),
            FadeOut(ex_result),
            run_time=0.5
        )

    # ────────────────────────────────────────────
    # Scene 5: 结合律图形演示 (括号变换色块)
    # ────────────────────────────────────────────
    def scene_5_associative_visual(self):
        section_label = Text(
            "图形演示",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.0)
        self.play(FadeIn(section_label), run_time=0.4)

        # 三个色块 A, B, C
        def make_block(color, label_str, width=1.8, height=1.1):
            rect = RoundedRectangle(
                corner_radius=0.15,
                width=width, height=height,
                fill_color=color,
                fill_opacity=0.85,
                stroke_width=0
            )
            lbl = Text(label_str, font="Noto Sans CJK SC", font_size=26, color=WHITE)
            lbl.move_to(rect.get_center())
            return VGroup(rect, lbl)

        blk_a = make_block(self.COLOR_A, "2")
        blk_b = make_block(self.COLOR_B, "3")
        blk_c = make_block(self.COLOR_C, "4")

        plus1 = MathTex(r"+", font_size=56, color=WHITE)
        plus2 = MathTex(r"+", font_size=56, color=WHITE)

        # Row: [A] + [B] + [C]
        row = VGroup(blk_a, plus1, blk_b, plus2, blk_c).arrange(RIGHT, buff=0.25)
        row.move_to(UP * 3.8)

        self.play(FadeIn(row), run_time=0.7)
        self.wait(0.4)

        # Step 1: 先加 (a+b) — 括号围住 A 和 B
        bracket_ab = SurroundingRectangle(
            VGroup(blk_a, plus1, blk_b),
            color=self.COLOR_HIGHLIGHT,
            corner_radius=0.12,
            buff=0.12,
            stroke_width=3
        )
        label_first = Text(
            "先加这两个",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(bracket_ab, UP, buff=0.15)

        self.play(Create(bracket_ab), FadeIn(label_first), run_time=0.6)
        self.wait(0.5)

        # 显示 (2+3) = 5
        step1_result = MathTex(r"(2+3) = 5", font_size=44, color=self.COLOR_HIGHLIGHT)
        step1_result.move_to(UP * 2.5)
        self.play(Write(step1_result), run_time=0.6)

        # 然后 5 + 4 = 9
        step1_final = MathTex(r"5 + 4 = 9", font_size=44, color=self.COLOR_RESULT)
        step1_final.move_to(UP * 1.8)
        self.play(Write(step1_final), run_time=0.5)
        self.wait(0.8)

        # Step 2: 改先加 (b+c) — 括号移到 B 和 C
        bracket_bc = SurroundingRectangle(
            VGroup(blk_b, plus2, blk_c),
            color=self.COLOR_B,
            corner_radius=0.12,
            buff=0.12,
            stroke_width=3
        )
        label_second = Text(
            "换成先加这两个",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_B
        ).next_to(bracket_bc, DOWN, buff=0.15)

        self.play(
            FadeOut(bracket_ab),
            FadeOut(label_first),
            FadeOut(step1_result),
            FadeOut(step1_final),
            run_time=0.4
        )
        self.play(Create(bracket_bc), FadeIn(label_second), run_time=0.6)
        self.wait(0.4)

        step2_result = MathTex(r"(3+4) = 7", font_size=44, color=self.COLOR_B)
        step2_result.move_to(UP * 2.5)
        self.play(Write(step2_result), run_time=0.6)

        step2_final = MathTex(r"2 + 7 = 9", font_size=44, color=self.COLOR_RESULT)
        step2_final.move_to(UP * 1.8)
        self.play(Write(step2_final), run_time=0.5)
        self.wait(0.8)

        # 结论
        conclusion = Text(
            "和都是 9，不变！",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.7)
        self.play(FadeIn(conclusion, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(row),
            FadeOut(bracket_bc), FadeOut(label_second),
            FadeOut(step2_result), FadeOut(step2_final),
            FadeOut(conclusion),
            FadeOut(section_label),
            FadeOut(self.assoc_title),
            run_time=0.5
        )

    # ────────────────────────────────────────────
    # Scene 6: 综合示例 — 25 + 37 + 75
    # ────────────────────────────────────────────
    def scene_6_example(self):
        # 标题
        title = Text(
            "简便运算示例",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.7)

        # 问题展示
        question_label = Text(
            "计算：",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 5.0 + LEFT * 2.5)

        question = MathTex(r"25 + 37 + 75", font_size=58, color=WHITE)
        question.move_to(UP * 4.2)
        question[0][0:2].set_color(self.COLOR_A)   # 25
        question[0][3:5].set_color(self.COLOR_B)   # 37
        question[0][6:8].set_color(self.COLOR_A)   # 75

        self.play(FadeIn(question_label), Write(question), run_time=0.8)
        self.wait(0.6)

        # 提示: 直接算很麻烦
        hint = Text(
            "直接按顺序算？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 3.3)

        direct_calc = MathTex(r"(25+37)+75 = 62+75 = 137", font_size=34, color=GRAY_B)
        direct_calc.move_to(UP * 2.6)

        self.play(FadeIn(hint), run_time=0.4)
        self.play(Write(direct_calc), run_time=0.7)
        self.wait(0.5)

        # 标注"麻烦"
        tedious = Text(
            "有点麻烦……",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_RESULT
        ).move_to(UP * 1.9)
        self.play(FadeIn(tedious), run_time=0.4)
        self.wait(0.7)

        # 清理提示
        self.play(FadeOut(hint), FadeOut(direct_calc), FadeOut(tedious), run_time=0.4)

        # 巧妙方法: 用交换律+结合律
        smart_label = Text(
            "用加法交换律+结合律！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_C
        ).move_to(UP * 3.3)
        self.play(FadeIn(smart_label), run_time=0.5)

        # Step 1: 交换 37 和 75 (交换律)
        step1_label = Text(
            "第一步：交换律，交换37和75",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.6)

        step1_formula = MathTex(r"= 25 + 75 + 37", font_size=52, color=WHITE)
        step1_formula.move_to(UP * 1.9)
        step1_formula[0][1:3].set_color(self.COLOR_A)   # 25
        step1_formula[0][4:6].set_color(self.COLOR_A)   # 75
        step1_formula[0][7:9].set_color(self.COLOR_B)   # 37

        self.play(FadeIn(step1_label), run_time=0.4)
        self.play(Write(step1_formula), run_time=0.7)

        # 箭头指示 37 ↔ 75
        swap_arrow = CurvedArrow(
            question[0][3:5].get_top() + UP * 0.15,
            question[0][6:8].get_top() + UP * 0.15,
            angle=-PI / 3,
            color=self.COLOR_ARROW,
            tip_length=0.18
        )
        self.play(Create(swap_arrow), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(swap_arrow), run_time=0.3)

        # Step 2: 结合律，先算 (25+75)
        step2_label = Text(
            "第二步：结合律，先算(25+75)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.0)

        step2_formula = MathTex(r"= (25 + 75) + 37", font_size=52, color=WHITE)
        step2_formula.move_to(UP * 0.3)
        step2_formula[0][1:3].set_color(self.COLOR_A)
        step2_formula[0][4:6].set_color(self.COLOR_A)
        step2_formula[0][7:9].set_color(self.COLOR_B)

        self.play(FadeIn(step2_label), run_time=0.4)
        self.play(Write(step2_formula), run_time=0.7)

        # 括号高亮
        brace = SurroundingRectangle(
            step2_formula[0][1:6],
            color=self.COLOR_HIGHLIGHT,
            corner_radius=0.08,
            buff=0.08,
            stroke_width=2.5
        )
        self.play(Create(brace), run_time=0.5)
        self.wait(0.6)

        # Step 3: (25+75) = 100
        step3_formula = MathTex(r"= 100 + 37", font_size=56, color=WHITE)
        step3_formula.move_to(DOWN * 0.7)
        step3_formula[0][1:4].set_color(self.COLOR_HIGHLIGHT)   # 100

        self.play(FadeOut(brace), run_time=0.2)
        self.play(Write(step3_formula), run_time=0.6)
        self.wait(0.5)

        # Final result
        final = MathTex(r"= 137", font_size=68, color=self.COLOR_RESULT)
        final.move_to(DOWN * 1.8)

        self.play(Write(final), run_time=0.7)
        self.play(
            Indicate(final, color=self.COLOR_HIGHLIGHT, scale_factor=1.15),
            run_time=0.6
        )
        self.wait(0.5)

        # Key takeaway
        takeaway = Text(
            "凑整再算，又快又准！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.0)

        takeaway2 = Text(
            "25 + 75 = 100  整百好计算",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(takeaway, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(takeaway2), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question_label), FadeOut(question),
            FadeOut(smart_label),
            FadeOut(step1_label), FadeOut(step1_formula),
            FadeOut(step2_label), FadeOut(step2_formula),
            FadeOut(step3_formula), FadeOut(final),
            FadeOut(takeaway), FadeOut(takeaway2),
            run_time=0.6
        )

    # ────────────────────────────────────────────
    # Scene 7: 总结与结尾
    # ────────────────────────────────────────────
    def scene_7_summary(self):
        # 总结标题
        sum_title = Text(
            "知识小结",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.8)
        self.play(Write(sum_title), run_time=0.6)

        # 交换律卡片
        card1_title = Text(
            "加法交换律",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_A
        )
        card1_formula = MathTex(r"a + b = b + a", font_size=42, color=WHITE)
        card1_formula[0][0].set_color(self.COLOR_A)
        card1_formula[0][2].set_color(self.COLOR_B)
        card1_formula[0][4].set_color(self.COLOR_B)
        card1_formula[0][6].set_color(self.COLOR_A)
        card1_desc = Text(
            "交换加数位置，和不变",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        card1 = VGroup(card1_title, card1_formula, card1_desc).arrange(DOWN, buff=0.25)

        # 卡片背景
        card1_bg = RoundedRectangle(
            corner_radius=0.25,
            width=card1.width + 0.7,
            height=card1.height + 0.5,
            fill_color="#16213e",
            fill_opacity=1.0,
            stroke_color=self.COLOR_A,
            stroke_width=2
        )
        card1_group = VGroup(card1_bg, card1)
        card1_bg.move_to(card1.get_center())
        card1_group.move_to(UP * 4.2)

        # 结合律卡片
        card2_title = Text(
            "加法结合律",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_C
        )
        card2_formula = MathTex(r"(a+b)+c = a+(b+c)", font_size=36, color=WHITE)
        card2_desc = Text(
            "改变括号位置，和不变",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        card2 = VGroup(card2_title, card2_formula, card2_desc).arrange(DOWN, buff=0.25)

        card2_bg = RoundedRectangle(
            corner_radius=0.25,
            width=card2.width + 0.7,
            height=card2.height + 0.5,
            fill_color="#16213e",
            fill_opacity=1.0,
            stroke_color=self.COLOR_C,
            stroke_width=2
        )
        card2_group = VGroup(card2_bg, card2)
        card2_bg.move_to(card2.get_center())
        card2_group.move_to(UP * 2.3)

        # 妙用卡片
        card3_title = Text(
            "结合使用",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        )
        card3_formula = MathTex(r"25+37+75", font_size=38, color=WHITE)
        card3_step = MathTex(r"=(25+75)+37=100+37", font_size=32, color=GRAY_A)
        card3_result = MathTex(r"=137", font_size=44, color=self.COLOR_RESULT)
        card3 = VGroup(card3_title, card3_formula, card3_step, card3_result).arrange(DOWN, buff=0.2)

        card3_bg = RoundedRectangle(
            corner_radius=0.25,
            width=card3.width + 0.7,
            height=card3.height + 0.5,
            fill_color="#16213e",
            fill_opacity=1.0,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        card3_group = VGroup(card3_bg, card3)
        card3_bg.move_to(card3.get_center())
        card3_group.move_to(DOWN * 0.5)

        # 动画出现
        self.play(FadeIn(card1_group, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(card2_group, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(card3_group, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.5)

        # 结尾关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.6)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.0)
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=26,
            color="#6b7280"
        ).move_to(DOWN * 4.7)

        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.6)
        self.wait(2.5)

        # 最终淡出
        self.play(
            FadeOut(sum_title),
            FadeOut(card1_group),
            FadeOut(card2_group),
            FadeOut(card3_group),
            FadeOut(follow_text),
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(self.author_label),
            run_time=1.0
        )

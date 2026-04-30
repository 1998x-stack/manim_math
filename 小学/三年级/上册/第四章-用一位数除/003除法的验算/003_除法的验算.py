"""
除法的验算 - Division Verification Animation
三年级上册 第四章 用一位数除

内容: 学习用"商×除数+余数=被除数"的方法验算除法
目标观众: 小学三年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DivisionVerifyLesson(Scene):
    """
    除法验算教学动画

    场景顺序:
    1. 开场钩子 - 如何知道除法算对了?
    2. 呈现除法算式 57 ÷ 4
    3. 竖式演示计算步骤
    4. 验算公式引入
    5. 代入验算过程
    6. 验算正确结论
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY   = "#e8f4fd"   # 主文字 白色系
        self.COLOR_DIVIDEND  = "#f39c12"   # 被除数 橙色
        self.COLOR_DIVISOR   = "#3498db"   # 除数   蓝色
        self.COLOR_QUOTIENT  = "#2ecc71"   # 商     绿色
        self.COLOR_REMAINDER = "#e74c3c"   # 余数   红色
        self.COLOR_VERIFY    = "#9b59b6"   # 验算   紫色
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_DIM       = "#6b7280"

        # 作者标识 (持续显示)
        self.author_brand = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author_brand)

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_division_problem()
        self.scene_3_vertical_calculation()
        self.scene_4_verify_formula()
        self.scene_5_verify_steps()
        self.scene_6_conclusion()
        self.scene_7_outro()

    # ─────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────
    def scene_1_hook(self):
        hook_line1 = Text(
            "除法算完了，",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)

        hook_line2 = Text(
            "怎么知道算对了？",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.7)

        question_mark = Text(
            "？",
            font="PingFang SC",
            font_size=120,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)

        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.7)
        self.play(GrowFromCenter(question_mark), run_time=0.6)
        self.wait(1.0)

        answer_text = Text(
            "用验算来检查！",
            font="PingFang SC",
            font_size=42,
            color="#2ecc71"
        ).move_to(DOWN * 0.5)

        self.play(FadeOut(question_mark), run_time=0.3)
        self.play(Write(answer_text), run_time=0.7)
        self.wait(0.8)

        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(answer_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    # Scene 2: 呈现除法算式
    # ─────────────────────────────────────────
    def scene_2_division_problem(self):
        step_title = Text(
            "先来做一道除法题",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_DIM
        ).move_to(UP * 5.8)

        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.4)

        # 算式: 57 ÷ 4 = ?
        num_57 = Text("57", font="PingFang SC", font_size=72,
                      color=self.COLOR_DIVIDEND, weight=BOLD)
        div_sym = MathTex(r"\div", font_size=72, color=self.COLOR_PRIMARY)
        num_4   = Text("4",  font="PingFang SC", font_size=72,
                       color=self.COLOR_DIVISOR,  weight=BOLD)
        eq_sym  = MathTex(r"=", font_size=72, color=self.COLOR_PRIMARY)
        q_mark  = Text("?",  font="PingFang SC", font_size=72,
                       color=self.COLOR_HIGHLIGHT, weight=BOLD)

        expr = VGroup(num_57, div_sym, num_4, eq_sym, q_mark)
        expr.arrange(RIGHT, buff=0.25)
        expr.move_to(UP * 3.5)

        self.play(Write(num_57), run_time=0.5)
        self.play(Write(div_sym), Write(num_4), run_time=0.4)
        self.play(Write(eq_sym), Write(q_mark), run_time=0.4)
        self.wait(0.6)

        # 标注被除数 / 除数
        label_dividend = Text("被除数", font="PingFang SC",
                               font_size=22, color=self.COLOR_DIVIDEND)
        label_divisor  = Text("除数",   font="PingFang SC",
                               font_size=22, color=self.COLOR_DIVISOR)

        label_dividend.next_to(num_57,  DOWN, buff=0.4)
        label_divisor.next_to(num_4,    DOWN, buff=0.4)

        arrow_dividend = Arrow(
            label_dividend.get_top(), num_57.get_bottom(),
            buff=0.08, color=self.COLOR_DIVIDEND,
            max_tip_length_to_length_ratio=0.25, stroke_width=2.5
        )
        arrow_divisor = Arrow(
            label_divisor.get_top(), num_4.get_bottom(),
            buff=0.08, color=self.COLOR_DIVISOR,
            max_tip_length_to_length_ratio=0.25, stroke_width=2.5
        )

        self.play(
            FadeIn(label_dividend, shift=UP * 0.2),
            FadeIn(label_divisor,  shift=UP * 0.2),
            GrowArrow(arrow_dividend),
            GrowArrow(arrow_divisor),
            run_time=0.7
        )
        self.wait(0.8)

        # 清理标注，保留算式
        self.play(
            FadeOut(label_dividend),
            FadeOut(label_divisor),
            FadeOut(arrow_dividend),
            FadeOut(arrow_divisor),
            FadeOut(step_title),
            run_time=0.4
        )

        # 算式移到顶部
        self.play(
            expr.animate.move_to(UP * 5.5).scale(0.6),
            run_time=0.6
        )
        self.expr_group = expr

    # ─────────────────────────────────────────
    # Scene 3: 竖式计算步骤
    # ─────────────────────────────────────────
    def scene_3_vertical_calculation(self):
        calc_title = Text(
            "竖式计算",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.2)

        self.play(Write(calc_title), run_time=0.5)

        # 竖式外框：用线条搭建竖式结构
        #
        #      1 4  ← 商
        #    ┌────
        #  4 ) 5 7
        #      4    ← 4×1
        #      ─
        #      1 7
        #      1 6  ← 4×4
        #      ─
        #        1  ← 余数
        #
        # 构建在屏幕中央

        cx = 0.0
        cy = 1.5  # 竖式中心 y

        # 字体大小
        FS = 52

        # --- 除数 ---
        v_divisor = Text("4", font="PingFang SC", font_size=FS,
                         color=self.COLOR_DIVISOR, weight=BOLD)
        v_divisor.move_to([cx - 1.8, cy, 0])

        # --- 被除数 ---
        v_5 = Text("5", font="PingFang SC", font_size=FS,
                   color=self.COLOR_DIVIDEND, weight=BOLD)
        v_7 = Text("7", font="PingFang SC", font_size=FS,
                   color=self.COLOR_DIVIDEND, weight=BOLD)
        v_5.move_to([cx + 0.0, cy, 0])
        v_7.move_to([cx + 0.8, cy, 0])

        # 竖式括号 — 用两条线模拟
        bracket_v = Line(
            [cx - 1.3, cy + 0.55, 0],
            [cx - 1.3, cy - 0.55, 0],
            color=WHITE, stroke_width=3
        )
        bracket_h = Line(
            [cx - 1.3, cy + 0.55, 0],
            [cx + 1.2,  cy + 0.55, 0],
            color=WHITE, stroke_width=3
        )

        # --- 商 ---
        v_quot_1 = Text("1", font="PingFang SC", font_size=FS,
                        color=self.COLOR_QUOTIENT, weight=BOLD)
        v_quot_4 = Text("4", font="PingFang SC", font_size=FS,
                        color=self.COLOR_QUOTIENT, weight=BOLD)
        v_quot_1.move_to([cx + 0.0, cy + 1.1, 0])
        v_quot_4.move_to([cx + 0.8, cy + 1.1, 0])

        # --- 第一步减法: 57 个位十位分步 ---
        # 4×1=4, 写在5下面
        v_sub1 = Text("4", font="PingFang SC", font_size=FS,
                      color="#e67e22")
        v_sub1.move_to([cx + 0.0, cy - 0.9, 0])

        line1 = Line(
            [cx - 0.5, cy - 1.4, 0],
            [cx + 1.2, cy - 1.4, 0],
            color=GRAY, stroke_width=2
        )

        # 余数17
        v_r1 = Text("1", font="PingFang SC", font_size=FS,
                    color=WHITE)
        v_r7 = Text("7", font="PingFang SC", font_size=FS,
                    color=WHITE)
        v_r1.move_to([cx + 0.0, cy - 2.0, 0])
        v_r7.move_to([cx + 0.8, cy - 2.0, 0])

        # 4×4=16
        v_sub2_1 = Text("1", font="PingFang SC", font_size=FS,
                        color="#e67e22")
        v_sub2_6 = Text("6", font="PingFang SC", font_size=FS,
                        color="#e67e22")
        v_sub2_1.move_to([cx + 0.0, cy - 2.9, 0])
        v_sub2_6.move_to([cx + 0.8, cy - 2.9, 0])

        line2 = Line(
            [cx - 0.5, cy - 3.4, 0],
            [cx + 1.2, cy - 3.4, 0],
            color=GRAY, stroke_width=2
        )

        # 余数1
        v_remain = Text("1", font="PingFang SC", font_size=FS,
                        color=self.COLOR_REMAINDER, weight=BOLD)
        v_remain.move_to([cx + 0.8, cy - 4.0, 0])

        # 省略号标记余数
        remain_label = Text("……1", font="PingFang SC",
                            font_size=38, color=self.COLOR_REMAINDER)
        remain_label.move_to([cx + 1.8, cy - 4.0, 0])

        # 逐步显示竖式
        self.play(FadeIn(v_divisor), FadeIn(bracket_v), FadeIn(bracket_h), run_time=0.5)
        self.play(FadeIn(v_5), FadeIn(v_7), run_time=0.4)
        self.wait(0.3)

        # 写商
        think1 = Text("5÷4=1余1", font="PingFang SC",
                      font_size=26, color=self.COLOR_DIM)
        think1.move_to([cx + 2.5, cy + 0.8, 0])
        self.play(FadeIn(think1), run_time=0.3)
        self.play(Write(v_quot_1), run_time=0.4)

        # 第一个减法
        self.play(FadeIn(v_sub1), run_time=0.4)
        self.play(Create(line1), run_time=0.3)
        self.play(FadeIn(v_r1), FadeIn(v_r7), run_time=0.4)
        self.play(FadeOut(think1), run_time=0.2)

        think2 = Text("17÷4=4余1", font="PingFang SC",
                      font_size=26, color=self.COLOR_DIM)
        think2.move_to([cx + 2.7, cy - 0.5, 0])
        self.play(FadeIn(think2), run_time=0.3)
        self.play(Write(v_quot_4), run_time=0.4)

        self.play(FadeIn(v_sub2_1), FadeIn(v_sub2_6), run_time=0.4)
        self.play(Create(line2), run_time=0.3)
        self.play(Write(v_remain), run_time=0.5)
        self.play(FadeOut(think2), run_time=0.2)

        self.wait(0.5)

        # 汇总结果
        result_text = Text("57 ÷ 4 = 14 …… 1",
                           font="PingFang SC",
                           font_size=34, color=self.COLOR_HIGHLIGHT)
        result_text.move_to([0, cy - 5.3, 0])
        self.play(Write(result_text), run_time=0.8)
        self.wait(1.2)

        # 清理竖式，保留结果
        vertical_group = VGroup(
            v_divisor, bracket_v, bracket_h,
            v_5, v_7,
            v_quot_1, v_quot_4,
            v_sub1, line1, v_r1, v_r7,
            v_sub2_1, v_sub2_6, line2,
            v_remain, calc_title
        )
        self.play(
            FadeOut(vertical_group),
            result_text.animate.move_to(UP * 4.0).scale(0.85),
            run_time=0.6
        )
        self.result_text = result_text

    # ─────────────────────────────────────────
    # Scene 4: 验算公式引入
    # ─────────────────────────────────────────
    def scene_4_verify_formula(self):
        verify_title = Text(
            "如何验算？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_VERIFY
        ).move_to(UP * 2.5)

        self.play(Write(verify_title), run_time=0.6)
        self.wait(0.4)

        # 公式拆解
        formula_parts = [
            ("商", self.COLOR_QUOTIENT),
            (" × ", self.COLOR_PRIMARY),
            ("除数", self.COLOR_DIVISOR),
            (" + ", self.COLOR_PRIMARY),
            ("余数", self.COLOR_REMAINDER),
            (" = ", self.COLOR_PRIMARY),
            ("被除数", self.COLOR_DIVIDEND),
        ]

        formula_group = VGroup()
        for txt, col in formula_parts:
            t = Text(txt, font="PingFang SC",
                     font_size=34, color=col)
            formula_group.add(t)
        formula_group.arrange(RIGHT, buff=0.1)
        formula_group.move_to(UP * 1.2)

        self.play(
            LaggedStart(*[Write(p) for p in formula_group],
                        lag_ratio=0.15),
            run_time=1.4
        )
        self.wait(0.8)

        # 用 Brace 标注
        brace_left = Brace(
            VGroup(formula_group[0], formula_group[1], formula_group[2]),
            direction=DOWN, buff=0.1, color=self.COLOR_DIM
        )
        brace_left_label = Text("先算乘法", font="PingFang SC",
                                font_size=22, color=self.COLOR_DIM)
        brace_left_label.next_to(brace_left, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(brace_left),
            FadeIn(brace_left_label, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.5)

        brace_right = Brace(
            VGroup(formula_group[3], formula_group[4]),
            direction=DOWN, buff=0.1, color=self.COLOR_DIM
        )
        brace_right_label = Text("再加余数", font="PingFang SC",
                                 font_size=22, color=self.COLOR_DIM)
        brace_right_label.next_to(brace_right, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(brace_right),
            FadeIn(brace_right_label, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.5)

        final_check = Text("结果等于被除数，就验算正确！",
                           font="PingFang SC",
                           font_size=28, color=self.COLOR_PRIMARY)
        final_check.move_to(DOWN * 0.2)
        self.play(Write(final_check), run_time=0.7)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(verify_title),
            FadeOut(brace_left), FadeOut(brace_left_label),
            FadeOut(brace_right), FadeOut(brace_right_label),
            FadeOut(final_check),
            formula_group.animate.move_to(UP * 2.8).scale(0.85),
            run_time=0.6
        )
        self.formula_group = formula_group

    # ─────────────────────────────────────────
    # Scene 5: 代入验算
    # ─────────────────────────────────────────
    def scene_5_verify_steps(self):
        step_title = Text(
            "开始验算 57 ÷ 4 = 14……1",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.5)

        self.play(Write(step_title), run_time=0.6)
        self.wait(0.4)

        # Step 1: 商×除数  14 × 4
        step1_label = Text("第一步：商 × 除数",
                           font="PingFang SC",
                           font_size=28, color=self.COLOR_DIM)
        step1_label.move_to(UP * 0.5)

        step1_num_14 = Text("14", font="PingFang SC", font_size=56,
                            color=self.COLOR_QUOTIENT, weight=BOLD)
        step1_mul    = MathTex(r"\times", font_size=56, color=self.COLOR_PRIMARY)
        step1_num_4  = Text("4",  font="PingFang SC", font_size=56,
                            color=self.COLOR_DIVISOR,  weight=BOLD)
        step1_eq     = MathTex(r"=", font_size=56, color=self.COLOR_PRIMARY)
        step1_result = Text("56", font="PingFang SC", font_size=56,
                            color=self.COLOR_VERIFY, weight=BOLD)

        step1_expr = VGroup(step1_num_14, step1_mul, step1_num_4,
                            step1_eq, step1_result)
        step1_expr.arrange(RIGHT, buff=0.2)
        step1_expr.move_to(DOWN * 0.5)

        self.play(FadeIn(step1_label, shift=DOWN * 0.2), run_time=0.4)
        self.play(Write(step1_num_14), Write(step1_mul), Write(step1_num_4),
                  run_time=0.6)
        self.play(Write(step1_eq), Write(step1_result), run_time=0.5)

        self.play(Indicate(step1_result, color=self.COLOR_HIGHLIGHT,
                           scale_factor=1.2), run_time=0.5)
        self.wait(0.6)

        # Step 2: + 余数  56 + 1
        step2_label = Text("第二步：+ 余数",
                           font="PingFang SC",
                           font_size=28, color=self.COLOR_DIM)
        step2_label.move_to(DOWN * 1.7)

        step2_num_56  = Text("56", font="PingFang SC", font_size=56,
                             color=self.COLOR_VERIFY, weight=BOLD)
        step2_plus    = MathTex(r"+", font_size=56, color=self.COLOR_PRIMARY)
        step2_num_1   = Text("1",  font="PingFang SC", font_size=56,
                             color=self.COLOR_REMAINDER, weight=BOLD)
        step2_eq      = MathTex(r"=", font_size=56, color=self.COLOR_PRIMARY)
        step2_result  = Text("57", font="PingFang SC", font_size=56,
                             color=self.COLOR_DIVIDEND, weight=BOLD)

        step2_expr = VGroup(step2_num_56, step2_plus, step2_num_1,
                            step2_eq, step2_result)
        step2_expr.arrange(RIGHT, buff=0.2)
        step2_expr.move_to(DOWN * 2.7)

        self.play(FadeIn(step2_label, shift=DOWN * 0.2), run_time=0.4)
        self.play(Write(step2_num_56), Write(step2_plus), Write(step2_num_1),
                  run_time=0.6)
        self.play(Write(step2_eq), Write(step2_result), run_time=0.5)
        self.play(Indicate(step2_result, color=self.COLOR_HIGHLIGHT,
                           scale_factor=1.3), run_time=0.6)
        self.wait(0.6)

        # Step 3: 对比被除数57
        compare_text = Text("正好等于被除数 57！",
                            font="PingFang SC",
                            font_size=32, color=self.COLOR_HIGHLIGHT)
        compare_text.move_to(DOWN * 4.2)

        self.play(Write(compare_text), run_time=0.6)

        # 高亮连线: step2_result → result_text中的57
        self.play(
            Flash(step2_result, color=self.COLOR_HIGHLIGHT, flash_radius=0.6,
                  line_length=0.3, num_lines=8),
            run_time=0.7
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(step1_label), FadeOut(step1_expr),
            FadeOut(step2_label), FadeOut(step2_expr),
            FadeOut(compare_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    # Scene 6: 验算正确结论
    # ─────────────────────────────────────────
    def scene_6_conclusion(self):
        # 完整验算过程汇总
        summary_title = Text("验算过程",
                             font="PingFang SC",
                             font_size=36, color=self.COLOR_VERIFY)
        summary_title.move_to(UP * 1.2)

        # 原式
        orig_label = Text("原算式：", font="PingFang SC",
                          font_size=26, color=self.COLOR_DIM)
        orig_expr_57 = Text("57", font="PingFang SC", font_size=38,
                            color=self.COLOR_DIVIDEND, weight=BOLD)
        orig_expr_d  = MathTex(r"\div", font_size=38, color=self.COLOR_PRIMARY)
        orig_expr_4  = Text("4", font="PingFang SC", font_size=38,
                            color=self.COLOR_DIVISOR, weight=BOLD)
        orig_expr_eq = MathTex(r"=", font_size=38, color=self.COLOR_PRIMARY)
        orig_expr_14 = Text("14", font="PingFang SC", font_size=38,
                            color=self.COLOR_QUOTIENT, weight=BOLD)
        orig_expr_dot = Text("……", font="PingFang SC", font_size=38,
                             color=self.COLOR_PRIMARY)
        orig_expr_1  = Text("1", font="PingFang SC", font_size=38,
                            color=self.COLOR_REMAINDER, weight=BOLD)

        orig_math = VGroup(orig_expr_57, orig_expr_d, orig_expr_4,
                           orig_expr_eq, orig_expr_14, orig_expr_dot, orig_expr_1)
        orig_math.arrange(RIGHT, buff=0.12)
        orig_row = VGroup(orig_label, orig_math).arrange(RIGHT, buff=0.3)
        orig_row.move_to(UP * 0.0)

        # 验算式
        verify_label = Text("验  算：", font="PingFang SC",
                            font_size=26, color=self.COLOR_DIM)
        v_14 = Text("14", font="PingFang SC", font_size=38,
                    color=self.COLOR_QUOTIENT, weight=BOLD)
        v_x  = MathTex(r"\times", font_size=38, color=self.COLOR_PRIMARY)
        v_4  = Text("4",  font="PingFang SC", font_size=38,
                    color=self.COLOR_DIVISOR, weight=BOLD)
        v_p  = MathTex(r"+", font_size=38, color=self.COLOR_PRIMARY)
        v_1  = Text("1",  font="PingFang SC", font_size=38,
                    color=self.COLOR_REMAINDER, weight=BOLD)
        v_e  = MathTex(r"=", font_size=38, color=self.COLOR_PRIMARY)
        v_57 = Text("57", font="PingFang SC", font_size=38,
                    color=self.COLOR_DIVIDEND, weight=BOLD)

        verify_math = VGroup(v_14, v_x, v_4, v_p, v_1, v_e, v_57)
        verify_math.arrange(RIGHT, buff=0.12)
        verify_row = VGroup(verify_label, verify_math).arrange(RIGHT, buff=0.3)
        verify_row.move_to(DOWN * 1.0)

        self.play(Write(summary_title), run_time=0.5)
        self.play(FadeIn(orig_row, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(verify_row, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.5)

        # 结论框
        correct_text = Text("验算正确！",
                            font="PingFang SC",
                            font_size=52, color="#2ecc71", weight=BOLD)
        correct_text.move_to(DOWN * 2.6)

        self.play(GrowFromCenter(correct_text), run_time=0.7)
        self.play(
            Flash(correct_text, color="#2ecc71", flash_radius=1.2,
                  line_length=0.4, num_lines=10),
            run_time=0.7
        )
        self.wait(0.5)

        # 口诀总结
        rule_box_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.5, height=1.6,
            fill_color="#0f3460",
            fill_opacity=0.85,
            stroke_color=self.COLOR_VERIFY,
            stroke_width=2
        ).move_to(DOWN * 4.5)

        rule_text = Text(
            "商 × 除数 + 余数 = 被除数",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)

        self.play(
            GrowFromCenter(rule_box_bg),
            run_time=0.5
        )
        self.play(Write(rule_text), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(orig_row),
            FadeOut(verify_row),
            FadeOut(correct_text),
            FadeOut(rule_box_bg),
            FadeOut(rule_text),
            FadeOut(self.result_text),
            FadeOut(self.formula_group),
            FadeOut(self.expr_group),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # Scene 7: 片尾关注
    # ─────────────────────────────────────────
    def scene_7_outro(self):
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_DIM
        ).move_to(UP * 0.7)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.3)

        tip_text = Text(
            "验算一下，数学不出错！",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_DIM
        ).move_to(DOWN * 1.3)

        self.play(
            Transform(self.author_brand, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(Write(follow_text), run_time=0.6)
        self.play(FadeIn(tip_text, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(self.author_brand),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(tip_text),
            run_time=0.8
        )

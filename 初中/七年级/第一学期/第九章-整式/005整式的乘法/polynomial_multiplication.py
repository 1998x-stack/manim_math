"""
整式的乘法 - Polynomial Multiplication Animation
使用 Manim 创建的初中数学教学视频

内容: 单项式×单项式、单项式×多项式、多项式×多项式
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PolynomialMultiplication(Scene):
    """
    整式的乘法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 单项式×单项式
    3. 单项式×多项式
    4. 多项式×多项式 - 引入
    5. 多项式×多项式 - 展开
    6. 具体例题
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要公式
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 高亮项
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 重点强调
        self.COLOR_COEFFICIENT = "#2ecc71"    # 绿色 - 系数
        self.COLOR_VARIABLE = "#9b59b6"       # 紫色 - 变量
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        self.COLOR_RESULT = "#f39c12"         # 橙色 - 结果
        
        # 初始化位置常量
        self.setup_positions()
        
        # 执行动画序列
        self.show_opening()
        self.show_monomial_times_monomial()
        self.show_monomial_times_polynomial()
        self.show_polynomial_times_polynomial_intro()
        self.show_polynomial_times_polynomial_expansion()
        self.show_concrete_example()
        self.show_summary()
    
    def setup_positions(self):
        """初始化所有位置常量"""
        self.AUTHOR_POS = UP * 7.5
        self.TITLE_POS = UP * 6.5
        self.SUBTITLE_POS = UP * 5.8
        self.MAIN_CONTENT_TOP = UP * 4
        self.MAIN_CONTENT_CENTER = UP * 1.5
        self.STEP_AREA = DOWN * 2
        self.EXAMPLE_AREA = DOWN * 4
        self.BOTTOM_TEXT = DOWN * 5.5
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(self.AUTHOR_POS)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这些式子怎么相乘？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三个神秘的乘法式子
        expr1 = MathTex(
            r"(2x)(3x^2)",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3)
        
        expr2 = MathTex(
            r"2x(3x+4)",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.5)
        
        expr3 = MathTex(
            r"(x+2)(x+3)",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(ORIGIN)
        
        # 依次闪现
        self.play(FadeIn(expr1, scale=1.2), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(expr2, scale=1.2), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(expr3, scale=1.2), run_time=0.4)
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=72,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.3)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(expr1),
            FadeOut(expr2),
            FadeOut(expr3),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_monomial_times_monomial(self):
        """场景2: 单项式×单项式"""
        # 标题
        title_chinese = Text(
            "规则一：单项式×单项式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title_chinese), run_time=0.8)
        
        # 原式
        original = MathTex(
            r"(2x)(3x^2)",
            font_size=48,
            color=WHITE
        ).move_to(self.MAIN_CONTENT_TOP)
        
        self.play(FadeIn(original, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 步骤1: 系数相乘
        step1_text = Text(
            "步骤1: 系数相乘",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2)
        
        step1_calc = MathTex(
            r"2 \times 3 = 6",
            font_size=36,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 1.2)
        
        # 高亮系数
        coeff_box1 = SurroundingRectangle(
            original[0][1],  # "2"
            color=self.COLOR_COEFFICIENT,
            buff=0.1
        )
        coeff_box2 = SurroundingRectangle(
            original[0][4],  # "3"
            color=self.COLOR_COEFFICIENT,
            buff=0.1
        )
        
        self.play(
            FadeIn(step1_text),
            Create(coeff_box1),
            Create(coeff_box2),
            run_time=0.8
        )
        self.play(Write(step1_calc), run_time=0.8)
        self.wait(1.0)
        
        # 步骤2: 同底数幂相乘
        step2_text = Text(
            "步骤2: 同底数幂相乘",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        step2_calc = MathTex(
            r"x^1 \times x^2 = x^{1+2} = x^3",
            font_size=36,
            color=self.COLOR_VARIABLE
        ).move_to(DOWN * 1.3)
        
        # 高亮变量
        var_box1 = SurroundingRectangle(
            original[0][2],  # "x"
            color=self.COLOR_VARIABLE,
            buff=0.1
        )
        var_box2 = SurroundingRectangle(
            original[0][5:7],  # "x^2"
            color=self.COLOR_VARIABLE,
            buff=0.1
        )
        
        self.play(
            FadeOut(coeff_box1),
            FadeOut(coeff_box2),
            FadeOut(step1_text),
            FadeOut(step1_calc),
            run_time=0.3
        )
        
        self.play(
            FadeIn(step2_text),
            Create(var_box1),
            Create(var_box2),
            run_time=0.8
        )
        self.play(Write(step2_calc), run_time=1.0)
        self.wait(1.2)
        
        # 结果
        result_text = Text(
            "结果:",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        result = MathTex(
            r"6x^3",
            font_size=56,
            color=self.COLOR_RESULT
        ).next_to(result_text, RIGHT, buff=0.3)
        
        result_box = SurroundingRectangle(
            result,
            color=self.COLOR_RESULT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            FadeOut(var_box1),
            FadeOut(var_box2),
            FadeOut(step2_text),
            FadeOut(step2_calc),
            run_time=0.3
        )
        
        self.play(
            FadeIn(result_text),
            FadeIn(result),
            run_time=0.6
        )
        self.play(
            Create(result_box),
            Flash(result, color=self.COLOR_RESULT, flash_radius=0.8),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 规则总结框
        rule_box = Rectangle(
            width=7,
            height=1.2,
            color=self.COLOR_PRIMARY,
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=self.COLOR_PRIMARY
        ).move_to(self.BOTTOM_TEXT)
        
        rule_text = Text(
            "系数相乘，同底数幂相乘",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(rule_box.get_center())
        
        self.play(
            FadeIn(rule_box),
            FadeIn(rule_text),
            run_time=0.8
        )
        self.wait(2.0)
        
        # 清理，保留结果在角落
        result_small = VGroup(result_text.copy(), result.copy()).scale(0.5).move_to(UL * 3.5 + UP * 0.5)
        
        self.play(
            FadeOut(title_chinese),
            FadeOut(original),
            FadeOut(result_text),
            FadeOut(result),
            FadeOut(result_box),
            FadeOut(rule_box),
            FadeOut(rule_text),
            run_time=0.5
        )
        
        self.play(FadeIn(result_small), run_time=0.3)
        self.rule1_result = result_small
    
    def show_monomial_times_polynomial(self):
        """场景3: 单项式×多项式"""
        # 标题
        title_chinese = Text(
            "规则二：单项式×多项式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title_chinese), run_time=0.8)
        
        # 抽象公式
        abstract_label = Text(
            "抽象形式:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5 + LEFT * 2.5)
        
        abstract_formula = MathTex(
            r"a(b+c)",
            font_size=40,
            color=WHITE
        ).next_to(abstract_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(abstract_label),
            FadeIn(abstract_formula),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 分配律箭头
        arrow1 = CurvedArrow(
            abstract_formula.get_center() + LEFT * 0.3,
            abstract_formula.get_center() + DOWN * 1 + RIGHT * 0.5,
            color=self.COLOR_COEFFICIENT,
            stroke_width=3
        )
        
        arrow2 = CurvedArrow(
            abstract_formula.get_center() + LEFT * 0.3,
            abstract_formula.get_center() + DOWN * 1 + RIGHT * 1.5,
            color=self.COLOR_VARIABLE,
            stroke_width=3
        )
        
        distrib_text = Text(
            "分配律：每项都要乘",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.3)
        
        self.play(
            Create(arrow1),
            Create(arrow2),
            FadeIn(distrib_text),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 展开结果
        expanded = MathTex(
            r"= ab + ac",
            font_size=40,
            color=self.COLOR_RESULT
        ).move_to(UP * 1.2)
        
        self.play(Write(expanded), run_time=0.8)
        self.wait(1.0)
        
        # 清理抽象部分，准备具体例子
        self.play(
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(distrib_text),
            run_time=0.3
        )
        
        # 具体例子
        example_label = Text(
            "具体例子:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(ORIGIN + LEFT * 2.5)
        
        example_formula = MathTex(
            r"2x(3x+4)",
            font_size=48,
            color=WHITE
        ).next_to(example_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(example_label),
            FadeIn(example_formula),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 第一项计算
        term1_text = Text(
            "第一项:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1.5 + LEFT * 2.8)
        
        term1_calc = MathTex(
            r"2x \times 3x = 6x^2",
            font_size=36,
            color=self.COLOR_COEFFICIENT
        ).next_to(term1_text, RIGHT, buff=0.3)
        
        # 高亮第一项
        term1_box = SurroundingRectangle(
            example_formula[0][3:5],  # "3x"
            color=self.COLOR_COEFFICIENT,
            buff=0.1
        )
        
        self.play(
            FadeIn(term1_text),
            Create(term1_box),
            run_time=0.5
        )
        self.play(Write(term1_calc), run_time=0.8)
        self.wait(0.8)
        
        # 第二项计算
        term2_text = Text(
            "第二项:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2.8 + LEFT * 2.8)
        
        term2_calc = MathTex(
            r"2x \times 4 = 8x",
            font_size=36,
            color=self.COLOR_VARIABLE
        ).next_to(term2_text, RIGHT, buff=0.3)
        
        # 高亮第二项
        term2_box = SurroundingRectangle(
            example_formula[0][6],  # "4"
            color=self.COLOR_VARIABLE,
            buff=0.1
        )
        
        self.play(
            FadeOut(term1_box),
            FadeIn(term2_text),
            Create(term2_box),
            run_time=0.5
        )
        self.play(Write(term2_calc), run_time=0.8)
        self.wait(0.8)
        
        # 合并结果
        final_result = MathTex(
            r"= 6x^2 + 8x",
            font_size=48,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 4.5)
        
        final_box = SurroundingRectangle(
            final_result,
            color=self.COLOR_RESULT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            FadeOut(term2_box),
            run_time=0.2
        )
        
        self.play(
            FadeIn(final_result),
            Create(final_box),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 规则总结
        rule_text = Text(
            "用分配律展开",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.2)
        
        self.play(FadeIn(rule_text), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        result_small = VGroup(
            Text("规则2:", font="Noto Sans CJK SC", font_size=14, color=GRAY_A),
            expanded.copy().scale(0.4)
        ).arrange(RIGHT, buff=0.1).move_to(UL * 3.5 + DOWN * 0.5)
        
        self.play(
            FadeOut(title_chinese),
            FadeOut(abstract_label),
            FadeOut(abstract_formula),
            FadeOut(expanded),
            FadeOut(example_label),
            FadeOut(example_formula),
            FadeOut(term1_text),
            FadeOut(term1_calc),
            FadeOut(term2_text),
            FadeOut(term2_calc),
            FadeOut(final_result),
            FadeOut(final_box),
            FadeOut(rule_text),
            run_time=0.5
        )
        
        self.play(FadeIn(result_small), run_time=0.3)
        self.rule2_result = result_small
    
    def show_polynomial_times_polynomial_intro(self):
        """场景4: 多项式×多项式 - 引入"""
        # 标题
        title_chinese = Text(
            "规则三：多项式×多项式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title_chinese), run_time=0.8)
        
        # 公式
        formula = MathTex(
            r"(a+b)(c+d)",
            font_size=56,
            color=WHITE
        ).move_to(self.MAIN_CONTENT_TOP)
        
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 提示文字
        hint1 = Text(
            "看起来复杂？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(hint1), run_time=0.5)
        self.wait(0.8)
        
        # 灯泡提示
        bulb = Text(
            "💡",
            font_size=48
        ).move_to(ORIGIN + LEFT * 1.5)
        
        hint2 = Text(
            "还是用分配律！",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).next_to(bulb, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(bulb, scale=0.5),
            FadeIn(hint2, shift=RIGHT * 0.3),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 将第一个括号看作整体
        bracket1_box = SurroundingRectangle(
            formula[0][0:5],  # "(a+b)"
            color=self.COLOR_COEFFICIENT,
            buff=0.15,
            corner_radius=0.1
        )
        
        whole_text = Text(
            "把 (a+b) 看作一个整体",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_COEFFICIENT
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeOut(hint1),
            FadeOut(bulb),
            FadeOut(hint2),
            Create(bracket1_box),
            FadeIn(whole_text),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 准备展开
        arrow_hint = Text(
            "现在展开...",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(arrow_hint), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(bracket1_box),
            FadeOut(whole_text),
            FadeOut(arrow_hint),
            run_time=0.3
        )
        
        # 保留公式和标题用于下一场景
        self.poly_title = title_chinese
        self.poly_formula = formula
    
    def show_polynomial_times_polynomial_expansion(self):
        """场景5: 多项式×多项式 - 详细展开"""
        # 使用上一场景的公式，向上移动
        self.play(
            self.poly_formula.animate.move_to(UP * 5),
            run_time=0.5
        )
        
        # 说明文字
        explain_text = Text(
            "每项与每项相乘:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(explain_text), run_time=0.5)
        
        # 四个乘积项 - 使用FOIL方法
        # First: a × c
        term1 = MathTex(
            r"a \times c = ac",
            font_size=32,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 2.2 + LEFT * 2)
        
        arrow1 = CurvedArrow(
            self.poly_formula.get_center() + LEFT * 0.8 + DOWN * 0.3,
            term1.get_left() + RIGHT * 0.2,
            color=self.COLOR_COEFFICIENT,
            stroke_width=2
        )
        
        self.play(
            Create(arrow1),
            Write(term1),
            run_time=1.0
        )
        self.wait(0.5)
        
        # Outer: a × d
        term2 = MathTex(
            r"a \times d = ad",
            font_size=32,
            color="#3498db"  # 蓝色
        ).move_to(UP * 0.8 + LEFT * 2)
        
        arrow2 = CurvedArrow(
            self.poly_formula.get_center() + LEFT * 0.8 + DOWN * 0.3,
            term2.get_left() + RIGHT * 0.2,
            color="#3498db",
            stroke_width=2
        )
        
        self.play(
            Create(arrow2),
            Write(term2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # Inner: b × c
        term3 = MathTex(
            r"b \times c = bc",
            font_size=32,
            color="#2ecc71"  # 绿色
        ).move_to(DOWN * 0.6 + LEFT * 2)
        
        arrow3 = CurvedArrow(
            self.poly_formula.get_center() + RIGHT * 0.2 + DOWN * 0.3,
            term3.get_left() + RIGHT * 0.2,
            color="#2ecc71",
            stroke_width=2
        )
        
        self.play(
            Create(arrow3),
            Write(term3),
            run_time=1.0
        )
        self.wait(0.5)
        
        # Last: b × d
        term4 = MathTex(
            r"b \times d = bd",
            font_size=32,
            color=self.COLOR_HIGHLIGHT  # 黄色
        ).move_to(DOWN * 2.0 + LEFT * 2)
        
        arrow4 = CurvedArrow(
            self.poly_formula.get_center() + RIGHT * 0.2 + DOWN * 0.3,
            term4.get_left() + RIGHT * 0.2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        self.play(
            Create(arrow4),
            Write(term4),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 收集所有项
        all_terms = VGroup(term1, term2, term3, term4)
        
        # 移动到中心并旋转（视觉效果）
        self.play(
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            all_terms.animate.arrange(RIGHT, buff=0.5).move_to(ORIGIN),
            run_time=1.0
        )
        
        # 添加加号
        plus1 = MathTex("+", font_size=32, color=WHITE).move_to(
            (term1.get_right() + term2.get_left()) / 2
        )
        plus2 = MathTex("+", font_size=32, color=WHITE).move_to(
            (term2.get_right() + term3.get_left()) / 2
        )
        plus3 = MathTex("+", font_size=32, color=WHITE).move_to(
            (term3.get_right() + term4.get_left()) / 2
        )
        
        self.play(
            FadeIn(plus1),
            FadeIn(plus2),
            FadeIn(plus3),
            run_time=0.5
        )
        
        # 最终公式
        final_formula = MathTex(
            r"= ac + ad + bc + bd",
            font_size=44,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2.5)
        
        final_box = SurroundingRectangle(
            final_formula,
            color=self.COLOR_RESULT,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(
            FadeOut(all_terms),
            FadeOut(plus1),
            FadeOut(plus2),
            FadeOut(plus3),
            FadeOut(explain_text),
            run_time=0.3
        )
        
        self.play(
            Write(final_formula),
            Create(final_box),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 可选：网格可视化
        grid_text = Text(
            "也可以用网格理解:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.2)
        
        # 2×2 网格矩阵
        grid_table = MathTable(
            [["ac", "ad"],
             ["bc", "bd"]],
            include_outer_lines=True,
            h_buff=0.8,
            v_buff=0.5
        ).scale(0.6).move_to(DOWN * 5.5)
        
        self.play(FadeIn(grid_text), run_time=0.5)
        self.play(FadeIn(grid_table), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        result_small = VGroup(
            Text("规则3:", font="Noto Sans CJK SC", font_size=14, color=GRAY_A),
            final_formula.copy().scale(0.35)
        ).arrange(RIGHT, buff=0.1).move_to(UL * 3.5 + DOWN * 1.2)
        
        self.play(
            FadeOut(self.poly_title),
            FadeOut(self.poly_formula),
            FadeOut(final_formula),
            FadeOut(final_box),
            FadeOut(grid_text),
            FadeOut(grid_table),
            run_time=0.5
        )
        
        self.play(FadeIn(result_small), run_time=0.3)
        self.rule3_result = result_small
    
    def show_concrete_example(self):
        """场景6: 具体例题"""
        # 标题
        title_text = Text(
            "练习：算一算",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title_text), run_time=0.8)
        
        # 例题
        example = MathTex(
            r"(x+2)(x+3)",
            font_size=56,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(example, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 展开过程 - 四项
        step_text = Text(
            "展开:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(step_text), run_time=0.5)
        
        # x × x = x²
        term1 = MathTex(
            r"x \times x = x^2",
            font_size=36,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 1.5)
        
        self.play(Write(term1), run_time=0.8)
        self.wait(0.5)
        
        # x × 3 = 3x
        term2 = MathTex(
            r"x \times 3 = 3x",
            font_size=36,
            color="#3498db"
        ).move_to(UP * 0.5)
        
        self.play(Write(term2), run_time=0.8)
        self.wait(0.5)
        
        # 2 × x = 2x
        term3 = MathTex(
            r"2 \times x = 2x",
            font_size=36,
            color="#2ecc71"
        ).move_to(DOWN * 0.5)
        
        self.play(Write(term3), run_time=0.8)
        self.wait(0.5)
        
        # 2 × 3 = 6
        term4 = MathTex(
            r"2 \times 3 = 6",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(Write(term4), run_time=0.8)
        self.wait(0.8)
        
        # 收集所有项
        collected = MathTex(
            r"= x^2 + 3x + 2x + 6",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(
            FadeOut(step_text),
            FadeOut(term1),
            FadeOut(term2),
            FadeOut(term3),
            FadeOut(term4),
            run_time=0.3
        )
        
        self.play(Write(collected), run_time=1.0)
        self.wait(0.8)
        
        # 合并同类项
        merge_text = Text(
            "合并同类项:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        # 高亮 3x 和 2x
        like_terms_box = SurroundingRectangle(
            collected[0][4:10],  # "3x + 2x"
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(
            FadeIn(merge_text),
            Create(like_terms_box),
            run_time=0.8
        )
        
        # 闪烁效果
        self.play(
            Flash(collected[0][4:10], color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 最终结果
        final = MathTex(
            r"= x^2 + 5x + 6",
            font_size=52,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 6)
        
        final_box = SurroundingRectangle(
            final,
            color=self.COLOR_RESULT,
            buff=0.25,
            corner_radius=0.1,
            stroke_width=3
        )
        
        self.play(
            FadeOut(like_terms_box),
            run_time=0.2
        )
        
        self.play(
            Write(final),
            Create(final_box),
            run_time=1.0
        )
        self.play(
            Flash(final, color=self.COLOR_RESULT, flash_radius=0.8),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title_text),
            FadeOut(example),
            FadeOut(collected),
            FadeOut(merge_text),
            FadeOut(final),
            FadeOut(final_box),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 标题
        title = Text(
            "三条规则总结",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三条规则卡片
        card1 = self.create_rule_card(
            "1. 单项式×单项式",
            "系数相乘，同底数幂相乘",
            self.COLOR_COEFFICIENT,
            UP * 4
        )
        
        card2 = self.create_rule_card(
            "2. 单项式×多项式",
            "用分配律展开",
            "#3498db",
            UP * 2
        )
        
        card3 = self.create_rule_card(
            "3. 多项式×多项式",
            "每项与每项相乘",
            self.COLOR_VARIABLE,
            ORIGIN
        )
        
        # 依次滑入
        for card in [card1, card2, card3]:
            card.shift(LEFT * 10)  # 初始在左侧
        
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.2)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.2)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(1.0)
        
        # 关键提示
        key_point = Text(
            "核心：分配律是关键！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(key_point, shift=UP * 0.3), run_time=0.8)
        self.wait(1.5)
        
        # 清理规则卡片
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(key_point),
            FadeOut(self.rule1_result),
            FadeOut(self.rule2_result),
            FadeOut(self.rule3_result),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        # 装饰 - 小公式图标
        icons = VGroup(
            MathTex(r"x^2", font_size=28, color=self.COLOR_COEFFICIENT),
            MathTex(r"+", font_size=28, color=WHITE),
            MathTex(r"y^2", font_size=28, color="#3498db"),
            MathTex(r"=", font_size=28, color=WHITE),
            MathTex(r"z^2", font_size=28, color=self.COLOR_VARIABLE)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3)
        
        self.play(FadeIn(icons, shift=UP * 0.2), run_time=0.6)
        self.play(Rotate(icons, angle=2*PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )
    
    def create_rule_card(self, title, content, color, position):
        """创建规则卡片"""
        # 背景框
        box = RoundedRectangle(
            width=7,
            height=1.2,
            color=color,
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=color,
            corner_radius=0.1
        )
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(box.get_center() + UP * 0.25)
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(box.get_center() + DOWN * 0.25)
        
        # 组合
        card = VGroup(box, title_text, content_text)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql polynomial_multiplication.py PolynomialMultiplication  # 快速预览
# manim -qh polynomial_multiplication.py PolynomialMultiplication   # 高质量渲染
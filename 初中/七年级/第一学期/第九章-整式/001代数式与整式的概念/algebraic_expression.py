"""
代数式与整式的概念 - Algebraic Expressions and Polynomials
使用 Manim 创建的初中数学教学视频

内容: 代数式、单项式、多项式、整式的概念
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


class AlgebraicExpressionConcept(Scene):
    """
    代数式与整式概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 代数式的定义
    3. 单项式 - Part 1 定义
    4. 单项式 - Part 2 系数和次数
    5. 多项式
    6. 整式总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ALGEBRAIC = "#3498db"      # 蓝色 - 代数式
        self.COLOR_MONOMIAL = "#e74c3c"       # 红色 - 单项式
        self.COLOR_POLYNOMIAL = "#2ecc71"     # 绿色 - 多项式
        self.COLOR_COEFFICIENT = "#f39c12"    # 橙色 - 系数
        self.COLOR_DEGREE = "#9b59b6"         # 紫色 - 次数
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 执行动画序列
        self.show_opening()
        self.show_algebraic_expression()
        self.show_monomial_definition()
        self.show_monomial_properties()
        self.show_polynomial()
        self.show_wholestyle_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "数学式子的秘密",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text, run_time=0.6))
        
        # 神秘代数式
        mysterious_exprs = VGroup(
            MathTex(r"3 + 5", font_size=40, color=WHITE),
            MathTex(r"a + b", font_size=40, color=self.COLOR_ALGEBRAIC),
            MathTex(r"3x^2y", font_size=40, color=self.COLOR_MONOMIAL),
            MathTex(r"2x^2 + 3x - 1", font_size=40, color=self.COLOR_POLYNOMIAL)
        ).arrange(DOWN, buff=0.5).move_to(UP * 2)
        
        # 依次闪现
        for i, expr in enumerate(mysterious_exprs):
            self.play(FadeIn(expr, scale=1.2), run_time=0.4)
            if i < len(mysterious_exprs) - 1:
                self.wait(0.15)
        
        # 提问
        question = Text(
            "它们都是什么？",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(question, run_time=0.5))
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(mysterious_exprs),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_algebraic_expression(self):
        """场景2: 代数式的定义"""
        # 标题
        title = Text(
            "代数式",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_ALGEBRAIC,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title, run_time=0.8))
        
        # 定义
        definition = Text(
            "用运算符号把数和字母\n连接而成的式子",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=0.8)
        
        # 演示：从具体到抽象
        example_concrete = MathTex(r"3 + 5", font_size=44, color=WHITE).move_to(UP * 2.5)
        
        self.play(Write(example_concrete, run_time=0.6))
        self.wait(0.5)
        
        # 转化过程
        arrow_1 = Arrow(UP * 2 + LEFT * 1.5, UP * 0.8 + LEFT * 1.5, color=self.COLOR_HIGHLIGHT, buff=0.1)
        arrow_2 = Arrow(UP * 2 + RIGHT * 1.5, UP * 0.8 + RIGHT * 1.5, color=self.COLOR_HIGHLIGHT, buff=0.1)
        
        label_a = Text("a", font="PingFang SC", font_size=24, color=self.COLOR_ALGEBRAIC).next_to(arrow_1, LEFT, buff=0.1)
        label_b = Text("b", font="PingFang SC", font_size=24, color=self.COLOR_ALGEBRAIC).next_to(arrow_2, RIGHT, buff=0.1)
        
        example_abstract = MathTex(r"a + b", font_size=44, color=self.COLOR_ALGEBRAIC).move_to(ORIGIN)
        
        self.play(
            GrowArrow(arrow_1),
            GrowArrow(arrow_2),
            FadeIn(label_a),
            FadeIn(label_b),
            run_time=0.8
        )
        
        self.play(Write(example_abstract, run_time=0.6))
        
        # 高亮运算符号
        plus_highlight = SurroundingRectangle(example_abstract[0][1], color=self.COLOR_HIGHLIGHT, buff=0.08)
        operator_label = Text(
            "运算符号",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(plus_highlight, DOWN, buff=0.3)
        
        self.play(Create(plus_highlight), FadeIn(operator_label), run_time=0.5)
        self.wait(0.8)
        
        # 更多例子
        more_examples = VGroup(
            MathTex(r"2x - y", font_size=32, color=self.COLOR_ALGEBRAIC),
            MathTex(r"a \cdot b", font_size=32, color=self.COLOR_ALGEBRAIC),
            MathTex(r"x^2 + 1", font_size=32, color=self.COLOR_ALGEBRAIC)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.5)
        
        examples_title = Text(
            "更多例子：",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(more_examples, UP, buff=0.3)
        
        self.play(FadeIn(examples_title), run_time=0.3)
        
        for example in more_examples:
            self.play(FadeIn(example, shift=UP * 0.1), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example_concrete),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(example_abstract),
            FadeOut(plus_highlight),
            FadeOut(operator_label),
            FadeOut(examples_title),
            FadeOut(more_examples),
            run_time=0.6
        )
        
        # 保留定义在顶部
        self.play(
            definition.animate.scale(0.7).move_to(UP * 5.5),
            run_time=0.4
        )
        
        self.wait(0.3)
        self.play(FadeOut(definition), run_time=0.3)
    
    def show_monomial_definition(self):
        """场景3: 单项式 - Part 1 定义"""
        # 标题
        title = Text(
            "单项式 Monomial",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_MONOMIAL,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title, run_time=0.8))
        
        # 单项式示例
        monomial_example = MathTex(
            r"3x^2y",
            font_size=60,
            color=self.COLOR_MONOMIAL
        ).move_to(UP * 3.5)
        
        self.play(Write(monomial_example, run_time=0.8))
        
        # 结构分解
        # 1. 系数标注
        coefficient_box = SurroundingRectangle(
            monomial_example[0][0],  # "3"
            color=self.COLOR_COEFFICIENT,
            buff=0.1
        )
        
        coefficient_brace = Brace(coefficient_box, DOWN, color=self.COLOR_COEFFICIENT)
        coefficient_label = Text(
            "系数",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_COEFFICIENT
        ).next_to(coefficient_brace, DOWN, buff=0.1)
        
        self.play(
            Create(coefficient_box),
            GrowFromCenter(coefficient_brace),
            run_time=0.6
        )
        self.play(FadeIn(coefficient_label, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)
        
        # 2. 字母部分标注
        letters_box = SurroundingRectangle(
            monomial_example[0][1:],  # "x^2y"
            color=BLUE,
            buff=0.1
        )
        
        letters_brace = Brace(letters_box, DOWN, color=BLUE)
        letters_label = Text(
            "字母",
            font="PingFang SC",
            font_size=24,
            color=BLUE
        ).next_to(letters_brace, DOWN, buff=0.1)
        
        self.play(
            Create(letters_box),
            GrowFromCenter(letters_brace),
            run_time=0.6
        )
        self.play(FadeIn(letters_label, shift=UP * 0.1), run_time=0.4)
        self.wait(0.8)
        
        # 3. 指数标注
        # 为x的指数添加箭头
        x_exponent_arrow = Arrow(
            monomial_example.get_center() + UP * 0.8 + LEFT * 0.3,
            monomial_example.get_center() + UP * 0.3 + LEFT * 0.3,
            color=self.COLOR_DEGREE,
            buff=0.05,
            stroke_width=3
        )
        
        x_exponent_label = Text(
            "指数",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_DEGREE
        ).next_to(x_exponent_arrow, UP, buff=0.05)
        
        self.play(
            GrowArrow(x_exponent_arrow),
            FadeIn(x_exponent_label),
            run_time=0.5
        )
        self.wait(0.6)
        
        # 定义文字
        definition = Text(
            "数与字母的乘积",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)
        
        # 清理标注
        self.play(
            FadeOut(coefficient_box),
            FadeOut(coefficient_brace),
            FadeOut(coefficient_label),
            FadeOut(letters_box),
            FadeOut(letters_brace),
            FadeOut(letters_label),
            FadeOut(x_exponent_arrow),
            FadeOut(x_exponent_label),
            FadeOut(definition),
            run_time=0.5
        )
        
        # 移动单项式到合适位置
        self.play(
            monomial_example.animate.scale(0.8).move_to(UP * 4),
            title.animate.move_to(UP * 5.5).scale(0.9),
            run_time=0.4
        )
        
        # 保存引用
        self.monomial_example = monomial_example
        self.monomial_title = title
    
    def show_monomial_properties(self):
        """场景4: 单项式 - Part 2 系数和次数"""
        # 使用之前的单项式
        monomial = self.monomial_example
        
        # === 系数部分 ===
        subtitle1 = Text(
            "系数 Coefficient",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 2.5)
        
        self.play(Write(subtitle1, run_time=0.6))
        
        # 高亮系数
        coefficient_highlight = SurroundingRectangle(
            monomial[0][0],
            color=self.COLOR_COEFFICIENT,
            buff=0.08
        )
        
        self.play(Create(coefficient_highlight), run_time=0.4)
        self.play(Indicate(monomial[0][0], color=self.COLOR_COEFFICIENT, scale_factor=1.3), run_time=0.5)
        
        # 系数值
        coefficient_value = MathTex(
            r"\text{coefficient} = 3",
            font_size=36,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 1.2)
        
        # 修正：使用Text代替MathTex中的中文
        coef_text = Text("系数", font="PingFang SC", font_size=28, color=self.COLOR_COEFFICIENT)
        coef_equals = MathTex("=", font_size=36, color=self.COLOR_COEFFICIENT)
        coef_num = MathTex("3", font_size=36, color=self.COLOR_COEFFICIENT)
        coefficient_display = VGroup(coef_text, coef_equals, coef_num).arrange(RIGHT, buff=0.2).move_to(UP * 1.2)
        
        self.play(FadeIn(coefficient_display, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)
        
        self.play(
            FadeOut(coefficient_highlight),
            FadeOut(subtitle1),
            FadeOut(coefficient_display),
            run_time=0.4
        )
        
        # === 次数部分 ===
        subtitle2 = Text(
            "次数 Degree",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_DEGREE
        ).move_to(UP * 2.5)
        
        self.play(Write(subtitle2, run_time=0.6))
        
        explanation = Text(
            "所有字母指数之和",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(explanation), run_time=0.4)
        
        # 指数2闪烁
        # 注意：MathTex中x^2的指数是第3个字符（索引2）
        self.play(
            Indicate(monomial[0][2], color=self.COLOR_DEGREE, scale_factor=1.5),
            run_time=0.5
        )
        
        # 显示2
        degree_2 = MathTex("2", font_size=44, color=self.COLOR_DEGREE).move_to(UP * 0.5 + LEFT * 1.5)
        self.play(FadeIn(degree_2, scale=1.2), run_time=0.4)
        
        # y的指数1（隐含）闪烁
        self.play(
            Indicate(monomial[0][3], color=self.COLOR_DEGREE, scale_factor=1.5),
            run_time=0.5
        )
        
        # 显示1
        degree_1 = MathTex("1", font_size=44, color=self.COLOR_DEGREE).move_to(UP * 0.5 + RIGHT * 1.5)
        self.play(FadeIn(degree_1, scale=1.2), run_time=0.4)
        
        # 加号
        plus_sign = MathTex("+", font_size=44, color=WHITE).move_to(UP * 0.5)
        self.play(Write(plus_sign), run_time=0.3)
        
        # 等号和结果
        calculation = VGroup(degree_2, plus_sign, degree_1)
        equals = MathTex("=", font_size=44, color=WHITE).next_to(calculation, DOWN, buff=0.4)
        result = MathTex("3", font_size=48, color=self.COLOR_DEGREE).next_to(equals, DOWN, buff=0.3)
        
        self.play(Write(equals), run_time=0.3)
        self.play(FadeIn(result, scale=1.3), run_time=0.5)
        
        # 次数标签
        degree_text = Text("次数", font="PingFang SC", font_size=28, color=self.COLOR_DEGREE)
        degree_eq = MathTex("=", font_size=36, color=self.COLOR_DEGREE)
        degree_val = MathTex("3", font_size=36, color=self.COLOR_DEGREE)
        degree_display = VGroup(degree_text, degree_eq, degree_val).arrange(RIGHT, buff=0.2).move_to(DOWN * 2)
        
        self.play(FadeIn(degree_display, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)
        
        # 更多例子快闪
        examples_group = VGroup(
            MathTex(r"-5a^3b", font_size=28, color=self.COLOR_MONOMIAL),
            Text("系数=-5, 次数=4", font="PingFang SC", font_size=18, color=GRAY_A),
            MathTex(r"xy^2z^3", font_size=28, color=self.COLOR_MONOMIAL),
            Text("系数=1, 次数=6", font="PingFang SC", font_size=18, color=GRAY_A)
        ).arrange_in_grid(rows=2, cols=2, buff=(0.5, 0.3)).move_to(DOWN * 4)
        
        for item in examples_group:
            self.play(FadeIn(item, scale=0.9), run_time=0.25)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle2),
            FadeOut(explanation),
            FadeOut(calculation),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(degree_display),
            FadeOut(examples_group),
            FadeOut(monomial),
            FadeOut(self.monomial_title),
            run_time=0.6
        )
    
    def show_polynomial(self):
        """场景5: 多项式"""
        # 标题
        title = Text(
            "多项式 Polynomial",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_POLYNOMIAL,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title, run_time=0.8))
        
        # 多项式示例
        polynomial = MathTex(
            r"2x^2 + 3x - 1",
            font_size=52,
            color=self.COLOR_POLYNOMIAL
        ).move_to(UP * 3.8)
        
        self.play(Write(polynomial, run_time=1.0))
        self.wait(0.5)
        
        # 闪烁加号
        # 找到加号和减号的位置
        plus_indices = [i for i, char in enumerate(polynomial[0].get_tex_string()) if char == '+']
        minus_indices = [i for i, char in enumerate(polynomial[0].get_tex_string()) if char == '-']
        
        # 简化：直接指示整个公式
        self.play(Indicate(polynomial, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        
        # 分解为三项
        term1 = MathTex(r"2x^2", font_size=40, color=self.COLOR_MONOMIAL).move_to(UP * 1.5 + LEFT * 2.5)
        term2 = MathTex(r"3x", font_size=40, color=self.COLOR_MONOMIAL).move_to(UP * 1.5)
        term3 = MathTex(r"-1", font_size=40, color=self.COLOR_MONOMIAL).move_to(UP * 1.5 + RIGHT * 2.5)
        
        # 标注"单项式"
        label1 = Text("单项式", font="PingFang SC", font_size=18, color=GRAY_A).next_to(term1, DOWN, buff=0.2)
        label2 = Text("单项式", font="PingFang SC", font_size=18, color=GRAY_A).next_to(term2, DOWN, buff=0.2)
        label3 = Text("单项式", font="PingFang SC", font_size=18, color=GRAY_A).next_to(term3, DOWN, buff=0.2)
        
        # 箭头
        arrow1 = Arrow(polynomial.get_bottom() + LEFT * 1, term1.get_top(), color=self.COLOR_HIGHLIGHT, buff=0.1, stroke_width=2)
        arrow2 = Arrow(polynomial.get_bottom(), term2.get_top(), color=self.COLOR_HIGHLIGHT, buff=0.1, stroke_width=2)
        arrow3 = Arrow(polynomial.get_bottom() + RIGHT * 1, term3.get_top(), color=self.COLOR_HIGHLIGHT, buff=0.1, stroke_width=2)
        
        # 动画：依次分离
        self.play(
            GrowArrow(arrow1),
            FadeIn(term1, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(label1), run_time=0.3)
        
        self.play(
            GrowArrow(arrow2),
            FadeIn(term2, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(label2), run_time=0.3)
        
        self.play(
            GrowArrow(arrow3),
            FadeIn(term3, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(label3), run_time=0.3)
        
        self.wait(0.8)
        
        # 定义文字
        definition = Text(
            "几个单项式的和",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_POLYNOMIAL,
            weight=BOLD
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(definition, shift=UP * 0.2), run_time=0.6)
        
        # 重新组合
        terms_group = VGroup(term1, term2, term3, label1, label2, label3, arrow1, arrow2, arrow3)
        
        self.wait(0.8)
        
        # 强调
        emphasis_box = SurroundingRectangle(polynomial, color=self.COLOR_POLYNOMIAL, buff=0.15, corner_radius=0.1)
        self.play(Create(emphasis_box), run_time=0.5)
        self.play(Flash(polynomial.get_center(), color=self.COLOR_POLYNOMIAL, flash_radius=1.5), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(terms_group),
            FadeOut(emphasis_box),
            FadeOut(definition),
            polynomial.animate.scale(0.75).move_to(UP * 4.5),
            title.animate.scale(0.9).move_to(UP * 5.8),
            run_time=0.5
        )
        
        # 保存引用
        self.polynomial_example = polynomial
        self.polynomial_title = title
    
    def show_wholestyle_summary(self):
        """场景6: 整式总结"""
        # 清理多项式
        self.play(
            FadeOut(self.polynomial_example),
            FadeOut(self.polynomial_title),
            run_time=0.3
        )
        
        # 标题
        title = Text(
            "整式 Integral Expression",
            font="PingFang SC",
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title, run_time=0.8))
        
        # 大框
        big_box = RoundedRectangle(
            width=7,
            height=8,
            color=GOLD,
            stroke_width=3,
            corner_radius=0.2
        ).move_to(UP * 0.5)
        
        box_label = Text(
            "整式",
            font="PingFang SC",
            font_size=32,
            color=GOLD,
            weight=BOLD
        ).next_to(big_box, UP, buff=0.2)
        
        self.play(Create(big_box), run_time=0.8)
        self.play(FadeIn(box_label, shift=DOWN * 0.1), run_time=0.4)
        
        # 单项式卡片
        mono_card = self.create_category_card(
            "单项式",
            self.COLOR_MONOMIAL,
            MathTex(r"3x^2y", font_size=36, color=self.COLOR_MONOMIAL)
        ).move_to(UP * 2 + LEFT * 1.5)
        
        # 从左侧飞入
        mono_card.shift(LEFT * 5)
        self.play(mono_card.animate.shift(RIGHT * 5), run_time=0.8)
        
        # 多项式卡片
        poly_card = self.create_category_card(
            "多项式",
            self.COLOR_POLYNOMIAL,
            MathTex(r"2x^2 + 3x - 1", font_size=32, color=self.COLOR_POLYNOMIAL)
        ).move_to(UP * 2 + RIGHT * 1.5)
        
        # 从右侧飞入
        poly_card.shift(RIGHT * 5)
        self.play(poly_card.animate.shift(LEFT * 5), run_time=0.8)
        
        # 公式
        formula_text = Text(
            "整式",
            font="PingFang SC",
            font_size=32,
            color=GOLD
        )
        
        formula_eq = MathTex("=", font_size=36, color=WHITE)
        
        formula_mono = Text(
            "单项式",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_MONOMIAL
        )
        
        formula_union = MathTex(r"\cup", font_size=36, color=WHITE)
        
        formula_poly = Text(
            "多项式",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_POLYNOMIAL
        )
        
        formula = VGroup(
            formula_text,
            formula_eq,
            formula_mono,
            formula_union,
            formula_poly
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 1.5)
        
        self.play(Write(formula, run_time=1.2))
        
        # 整式框闪烁
        self.wait(0.5)
        self.play(
            Flash(big_box.get_center(), color=GOLD, flash_radius=2.5, num_lines=16),
            run_time=0.8
        )
        self.play(Indicate(big_box, color=GOLD, scale_factor=1.05), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(big_box),
            FadeOut(box_label),
            FadeOut(mono_card),
            FadeOut(poly_card),
            FadeOut(formula),
            run_time=0.6
        )
    
    def create_category_card(self, title_text, color, example_math):
        """创建类别卡片"""
        # 背景框
        bg_rect = RoundedRectangle(
            width=3.2,
            height=2.2,
            fill_color=color,
            fill_opacity=0.15,
            stroke_color=color,
            stroke_width=2,
            corner_radius=0.15
        )
        
        # 标题
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=28,
            color=color,
            weight=BOLD
        ).move_to(bg_rect.get_top() + DOWN * 0.4)
        
        # 示例
        example = example_math.move_to(bg_rect.get_center() + DOWN * 0.2)
        
        card = VGroup(bg_rect, title, example)
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多代数技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 三个知识点图标
        icon1 = Circle(radius=0.4, fill_color=self.COLOR_ALGEBRAIC, fill_opacity=0.8, stroke_width=0)
        icon1_text = Text("代数式", font="PingFang SC", font_size=16, color=WHITE).move_to(icon1.get_center())
        icon1_group = VGroup(icon1, icon1_text).move_to(DOWN * 2.5 + LEFT * 2.2)
        
        icon2 = Circle(radius=0.4, fill_color=self.COLOR_MONOMIAL, fill_opacity=0.8, stroke_width=0)
        icon2_text = Text("单项式", font="PingFang SC", font_size=16, color=WHITE).move_to(icon2.get_center())
        icon2_group = VGroup(icon2, icon2_text).move_to(DOWN * 2.5)
        
        icon3 = Circle(radius=0.4, fill_color=self.COLOR_POLYNOMIAL, fill_opacity=0.8, stroke_width=0)
        icon3_text = Text("多项式", font="PingFang SC", font_size=16, color=WHITE).move_to(icon3.get_center())
        icon3_group = VGroup(icon3, icon3_text).move_to(DOWN * 2.5 + RIGHT * 2.2)
        
        icons = VGroup(icon1_group, icon2_group, icon3_group)
        
        # 依次出现
        for icon_group in icons:
            self.play(FadeIn(icon_group, scale=0.5), run_time=0.3)
        
        # 旋转动画
        self.play(Rotate(icons, angle=PI, run_time=1.5))
        
        # 装饰星星
        stars = VGroup(*[
            Star(n=5, color=YELLOW, fill_opacity=0.8)
            .scale(0.15)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(star, scale=0.3) for star in stars], run_time=0.6)
        
        self.wait(1.2)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            FadeOut(stars),
            run_time=1.0
        )


# 运行命令:
# manim -pql algebraic_expression.py AlgebraicExpressionConcept  # 快速预览
# manim -qh algebraic_expression.py AlgebraicExpressionConcept   # 高质量渲染
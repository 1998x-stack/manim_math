"""
整式的除法 - Polynomial Division Animation
使用 Manim 创建的七年级数学教学视频

内容: 单项式除以单项式、多项式除以单项式
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


class PolynomialDivision(Scene):
    """
    整式除法教学动画场景
    
    场景顺序:
    1. 开场引入
    2. 幂的运算复习
    3. 单项式除以单项式 - 规则
    4. 单项式除以单项式 - 示例
    5. 多项式除以单项式 - 规则
    6. 综合练习 + 总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要公式
        self.COLOR_COEFFICIENT = "#e74c3c"   # 红色 - 系数
        self.COLOR_VARIABLE = "#2ecc71"      # 绿色 - 变量
        self.COLOR_EXPONENT = "#9b59b6"      # 紫色 - 指数
        self.COLOR_RESULT = "#f1c40f"        # 黄色 - 结果
        self.COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮
        self.COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_FORMULA = 32
        self.FONT_FORMULA_SMALL = 24
        self.FONT_BODY = 22
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_power_review()
        self.show_monomial_rule()
        self.show_monomial_example()
        self.show_polynomial_rule()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场引入 (3-5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_chinese = Text(
            "乘法会算，那除法呢？",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_chinese), run_time=0.8)
        
        # 示例问题
        problem = MathTex(
            r"6x^3 \div 2x = \ ?",
            font_size=40,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(FadeIn(problem, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_chinese),
            FadeOut(problem),
            run_time=0.5
        )
    
    def show_power_review(self):
        """场景2: 幂的运算复习 (6-8秒)"""
        # 标题
        title = Text(
            "复习：幂的运算",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 幂的法则
        power_rule = MathTex(
            r"a^m \div a^n = a^{m-n}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        condition = Text(
            "(a≠0, m≥n)",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(power_rule, RIGHT, buff=0.3)
        
        self.play(Write(power_rule), run_time=1.0)
        self.play(FadeIn(condition), run_time=0.3)
        
        # 具体示例
        example = MathTex(
            r"x^5 \div x^2 = x^3",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_RESULT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(example, shift=UP * 0.2), run_time=0.6)
        
        # 高亮指数变化
        self.wait(0.5)
        self.play(
            Indicate(example[0][1:3]),  # x^5
            Indicate(example[0][5:7]),  # x^2
            Indicate(example[0][9:11]), # x^3
            run_time=0.8
        )
        
        # 说明文字
        explanation = Text(
            "同底数幂相除，底数不变，指数相减",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(power_rule),
            FadeOut(condition),
            FadeOut(example),
            FadeOut(explanation),
            run_time=0.5
        )
    
    def show_monomial_rule(self):
        """场景3: 单项式除以单项式 - 规则 (10-12秒)"""
        # 标题
        title_chinese = Text(
            "单项式",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        )
        title_symbol = MathTex(
            r"\div",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        )
        title_chinese2 = Text(
            "单项式",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        )
        
        title = VGroup(title_chinese, title_symbol, title_chinese2).arrange(RIGHT, buff=0.3)
        title.move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 原式
        original = MathTex(
            r"6x^3 \div 2x",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(original, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.4)
        
        # 规则1: 系数相除
        rule1_text = Text(
            "规则①：系数相除",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        rule1_box = SurroundingRectangle(
            rule1_text,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        rule1_group = VGroup(rule1_box, rule1_text)
        
        self.play(FadeIn(rule1_group, shift=LEFT * 0.3), run_time=0.5)
        
        # 高亮系数
        self.wait(0.3)
        coef_rect1 = SurroundingRectangle(
            original[0][0],  # 6
            color=self.COLOR_COEFFICIENT,
            buff=0.05
        )
        coef_rect2 = SurroundingRectangle(
            original[0][4],  # 2
            color=self.COLOR_COEFFICIENT,
            buff=0.05
        )
        
        self.play(Create(coef_rect1), Create(coef_rect2), run_time=0.5)
        
        # 系数除法步骤
        step1 = MathTex(
            r"= (6 \div 2) \times (x^3 \div x)",
            font_size=self.FONT_FORMULA_SMALL,
            color=WHITE
        ).move_to(ORIGIN)
        
        step1[0][2].set_color(self.COLOR_COEFFICIENT)    # 6
        step1[0][4].set_color(self.COLOR_COEFFICIENT)    # 2
        
        self.play(
            FadeOut(coef_rect1),
            FadeOut(coef_rect2),
            FadeIn(step1, shift=LEFT * 0.2),
            run_time=0.8
        )
        
        # 规则2: 同底数幂相除
        rule2_text = Text(
            "规则②：同底数幂相除",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        rule2_box = SurroundingRectangle(
            rule2_text,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        rule2_group = VGroup(rule2_box, rule2_text)
        
        self.play(FadeIn(rule2_group, shift=LEFT * 0.3), run_time=0.5)
        
        # 高亮变量
        self.wait(0.3)
        var_rect = SurroundingRectangle(
            step1[0][9:14],  # x^3 ÷ x
            color=self.COLOR_VARIABLE,
            buff=0.05
        )
        
        self.play(Create(var_rect), run_time=0.5)
        
        # 变量除法步骤
        step2 = MathTex(
            r"= 3 \times x^2",
            font_size=self.FONT_FORMULA_SMALL,
            color=WHITE
        ).move_to(DOWN * 3)
        
        step2[0][2].set_color(self.COLOR_COEFFICIENT)    # 3
        step2[0][4:7].set_color(self.COLOR_VARIABLE)     # x^2
        
        self.play(
            FadeOut(var_rect),
            FadeIn(step2, shift=LEFT * 0.2),
            run_time=0.8
        )
        
        # 最终结果
        step3 = MathTex(
            r"= 3x^2",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step3, scale=1.1), run_time=0.6)
        self.play(Flash(step3, color=self.COLOR_RESULT, flash_radius=0.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(original),
            FadeOut(rule1_group),
            FadeOut(rule2_group),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            run_time=0.5
        )
    
    def show_monomial_example(self):
        """场景4: 单项式除法 - 完整示例 (10-12秒)"""
        # 新题目
        example_text = Text(
            "例题：",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 5 + LEFT * 3)
        
        problem = MathTex(
            r"-12a^4b^2 \div 3a^2b",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).next_to(example_text, RIGHT, buff=0.3)
        
        problem_group = VGroup(example_text, problem)
        
        self.play(FadeIn(problem_group, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # Step 1: 系数除法
        step1_label = Text(
            "①系数：",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3 + LEFT * 3.2)
        
        coef_calc = MathTex(
            r"-12 \div 3 = -4",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_COEFFICIENT
        ).next_to(step1_label, RIGHT, buff=0.3)
        
        step1_group = VGroup(step1_label, coef_calc)
        
        # 框选系数
        coef_rect = SurroundingRectangle(
            problem[0][0:3],  # -12
            color=self.COLOR_COEFFICIENT,
            buff=0.05
        )
        
        self.play(Create(coef_rect), run_time=0.4)
        self.play(
            FadeOut(coef_rect),
            FadeIn(step1_group, shift=LEFT * 0.2),
            run_time=0.6
        )
        
        # Step 2: a的幂除法
        step2_label = Text(
            "②变量a：",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5 + LEFT * 2.7)
        
        a_calc = MathTex(
            r"a^4 \div a^2 = a^2",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_VARIABLE
        ).next_to(step2_label, RIGHT, buff=0.3)
        
        step2_group = VGroup(step2_label, a_calc)
        
        # 框选a的幂
        a_rect = SurroundingRectangle(
            VGroup(problem[0][3:6], problem[0][9:12]),  # a^4 和 a^2
            color=self.COLOR_VARIABLE,
            buff=0.05
        )
        
        self.play(Create(a_rect), run_time=0.4)
        self.play(
            FadeOut(a_rect),
            FadeIn(step2_group, shift=LEFT * 0.2),
            run_time=0.6
        )
        
        # Step 3: b的幂除法
        step3_label = Text(
            "③变量b：",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN + LEFT * 2.7)
        
        b_calc = MathTex(
            r"b^2 \div b = b",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_VARIABLE
        ).next_to(step3_label, RIGHT, buff=0.3)
        
        step3_group = VGroup(step3_label, b_calc)
        
        # 框选b的幂
        b_rect = SurroundingRectangle(
            VGroup(problem[0][6:8], problem[0][12]),  # b^2 和 b
            color=self.COLOR_VARIABLE,
            buff=0.05
        )
        
        self.play(Create(b_rect), run_time=0.4)
        self.play(
            FadeOut(b_rect),
            FadeIn(step3_group, shift=LEFT * 0.2),
            run_time=0.6
        )
        
        # 组合结果
        arrow = MathTex(
            r"\Downarrow",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        final_result = MathTex(
            r"-4a^2b",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(arrow), run_time=0.3)
        self.play(FadeIn(final_result, scale=1.2), run_time=0.6)
        self.play(Flash(final_result, color=self.COLOR_RESULT, flash_radius=0.6), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(problem_group),
            FadeOut(step1_group),
            FadeOut(step2_group),
            FadeOut(step3_group),
            FadeOut(arrow),
            FadeOut(final_result),
            run_time=0.5
        )
    
    def show_polynomial_rule(self):
        """场景5: 多项式除以单项式 - 规则 (12-15秒)"""
        # 标题
        title_chinese = Text(
            "多项式",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        )
        title_symbol = MathTex(
            r"\div",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        )
        title_chinese2 = Text(
            "单项式",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        )
        
        title = VGroup(title_chinese, title_symbol, title_chinese2).arrange(RIGHT, buff=0.3)
        title.move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 原式
        original = MathTex(
            r"(6x^3 + 4x^2) \div 2x",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(original, shift=DOWN * 0.2), run_time=0.6)
        
        # 核心规则
        rule_text = Text(
            "把多项式的每一项分别除以单项式，再把商相加",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)
        
        rule_box = SurroundingRectangle(
            rule_text,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        rule_group = VGroup(rule_box, rule_text)
        
        self.play(FadeIn(rule_group, shift=UP * 0.2), run_time=0.7)
        self.wait(0.5)
        
        # 拆分步骤
        split_step = MathTex(
            r"= 6x^3 \div 2x + 4x^2 \div 2x",
            font_size=self.FONT_FORMULA_SMALL,
            color=WHITE
        ).move_to(UP * 0.3)
        
        # 箭头1指向第一项
        arrow1 = Arrow(
            start=original.get_bottom() + LEFT * 0.8,
            end=split_step.get_top() + LEFT * 1.5,
            color=self.COLOR_AUXILIARY,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        # 箭头2指向第二项
        arrow2 = Arrow(
            start=original.get_bottom() + RIGHT * 0.5,
            end=split_step.get_top() + RIGHT * 1.5,
            color=self.COLOR_AUXILIARY,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            run_time=0.6
        )
        self.play(FadeIn(split_step, shift=DOWN * 0.2), run_time=0.6)
        
        # 计算第一项
        term1_calc = MathTex(
            r"3x^2",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_VARIABLE
        ).move_to(DOWN * 1.2 + LEFT * 1.8)
        
        self.play(FadeIn(term1_calc, shift=DOWN * 0.2), run_time=0.5)
        
        # 加号
        plus_sign = MathTex(
            r"+",
            font_size=self.FONT_FORMULA_SMALL,
            color=WHITE
        ).next_to(term1_calc, RIGHT, buff=0.4)
        
        # 计算第二项
        term2_calc = MathTex(
            r"2x",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_VARIABLE
        ).next_to(plus_sign, RIGHT, buff=0.4)
        
        self.play(
            FadeIn(plus_sign),
            FadeIn(term2_calc, shift=DOWN * 0.2),
            run_time=0.5
        )
        
        # 最终结果
        equals = MathTex(
            r"=",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 2.8)
        
        final = MathTex(
            r"3x^2 + 2x",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).next_to(equals, RIGHT, buff=0.3)
        
        final_group = VGroup(equals, final)
        
        self.play(FadeIn(final_group, scale=1.1), run_time=0.7)
        self.play(Flash(final, color=self.COLOR_RESULT, flash_radius=0.6), run_time=0.5)
        
        # 公式框强调
        formula_box = SurroundingRectangle(
            final,
            color=self.COLOR_RESULT,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=3
        )
        
        self.play(Create(formula_box), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(original),
            FadeOut(rule_group),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(split_step),
            FadeOut(term1_calc),
            FadeOut(plus_sign),
            FadeOut(term2_calc),
            FadeOut(final_group),
            FadeOut(formula_box),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景6: 综合练习 + 总结 (12-15秒)"""
        # 综合例题
        practice_text = Text(
            "综合练习：",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5 + LEFT * 2.5)
        
        problem = MathTex(
            r"(8a^3b - 12a^2b^2) \div 4ab",
            font_size=self.FONT_FORMULA_SMALL,
            color=WHITE
        ).next_to(practice_text, RIGHT, buff=0.3)
        
        practice_group = VGroup(practice_text, problem)
        
        self.play(FadeIn(practice_group, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # 快速展示拆分
        split = MathTex(
            r"= 8a^3b \div 4ab - 12a^2b^2 \div 4ab",
            font_size=22,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(split, shift=LEFT * 0.2), run_time=0.6)
        
        # 两项计算结果
        result1 = MathTex(
            r"2a^2",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_VARIABLE
        ).move_to(UP * 2 + LEFT * 1.5)
        
        minus_sign = MathTex(
            r"-",
            font_size=self.FONT_FORMULA_SMALL,
            color=WHITE
        ).next_to(result1, RIGHT, buff=0.4)
        
        result2 = MathTex(
            r"3ab",
            font_size=self.FONT_FORMULA_SMALL,
            color=self.COLOR_VARIABLE
        ).next_to(minus_sign, RIGHT, buff=0.4)
        
        self.play(FadeIn(result1), run_time=0.4)
        self.play(FadeIn(minus_sign), FadeIn(result2), run_time=0.5)
        
        # 最终答案
        equals = MathTex(
            r"=",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 0.2)
        
        final_answer = MathTex(
            r"2a^2 - 3ab",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).next_to(equals, RIGHT, buff=0.3)
        
        answer_group = VGroup(equals, final_answer)
        
        self.play(FadeIn(answer_group, scale=1.1), run_time=0.6)
        self.play(Flash(final_answer, color=self.COLOR_RESULT, flash_radius=0.6), run_time=0.5)
        self.wait(0.5)
        
        # 总结卡片
        summary1_text = Text(
            "单项式÷单项式：系数相除，同底数幂相除",
            font="PingFang SC",
            font_size=18,
            color=WHITE
        ).move_to(DOWN * 1.8)
        
        summary1_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_PRIMARY,
            fill_opacity=1,
            stroke_width=0
        ).next_to(summary1_text, LEFT, buff=0.2)
        
        summary1 = VGroup(summary1_icon, summary1_text)
        summary1.shift(LEFT * 10)  # 初始在左侧外
        
        summary2_text = Text(
            "多项式÷单项式：每一项分别除，再相加",
            font="PingFang SC",
            font_size=18,
            color=WHITE
        ).move_to(DOWN * 3.2)
        
        summary2_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_VARIABLE,
            fill_opacity=1,
            stroke_width=0
        ).next_to(summary2_text, LEFT, buff=0.2)
        
        summary2 = VGroup(summary2_icon, summary2_text)
        summary2.shift(LEFT * 10)  # 初始在左侧外
        
        summary3_text = Text(
            "关键：整式除法是乘法的逆运算",
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        ).move_to(DOWN * 4.6)
        
        summary3_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=1,
            stroke_width=0
        ).next_to(summary3_text, LEFT, buff=0.2)
        
        summary3 = VGroup(summary3_icon, summary3_text)
        summary3.shift(LEFT * 10)  # 初始在左侧外
        
        # 卡片依次滑入
        self.play(summary1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(summary2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(summary3.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.8)
        
        # 关注提示
        follow_text = Text(
            "关注我，掌握更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 小装饰 - 闪烁的星星
        stars = VGroup(*[
            Star(
                n=5,
                outer_radius=0.2,
                color=GOLD,
                fill_opacity=0.8
            ).move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * PI / 2), np.sin(i * PI / 2), 0]))
            for i in range(4)
        ])
        
        self.play(
            *[FadeIn(star, scale=0.5) for star in stars],
            run_time=0.5
        )
        self.play(
            *[Flash(star, color=GOLD) for star in stars],
            run_time=0.5
        )
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(practice_group),
            FadeOut(split),
            FadeOut(result1),
            FadeOut(minus_sign),
            FadeOut(result2),
            FadeOut(answer_group),
            FadeOut(summary1),
            FadeOut(summary2),
            FadeOut(summary3),
            FadeOut(follow_text),
            FadeOut(stars),
            FadeOut(self.author_info),
            run_time=1.0
        )


# 运行命令:
# manim -pql polynomial_division.py PolynomialDivision  # 快速预览
# manim -qh polynomial_division.py PolynomialDivision   # 高质量渲染
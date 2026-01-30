"""
同类项与合并同类项 - Like Terms and Combining Like Terms
使用 Manim 创建的七年级代数教学视频

内容: 同类项的定义、判断和合并法则
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


class LikeTerms(Scene):
    """
    同类项与合并同类项教学动画场景
    
    场景顺序:
    1. 开场钩子 - 复杂式子引入
    2. 什么是同类项 - 定义讲解
    3. 同类项的判断 - 正反例
    4. 合并同类项的法则 - 规则说明
    5. 完整示例演示 - 综合应用
    6. 总结与关注 - 要点回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要项
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要项
        self.COLOR_TERTIARY = "#f39c12"     # 橙色 - 第三类
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_COEFFICIENT = "#2ecc71"  # 绿色 - 系数
        self.COLOR_VARIABLE = "#9b59b6"     # 紫色 - 变量
        self.COLOR_AUXILIARY = GRAY_B       # 辅助色
        self.COLOR_SUCCESS = GREEN          # 成功/正确
        self.COLOR_ERROR = RED              # 错误
        
        # 字体大小
        self.FONT_TITLE = 40
        self.FONT_SUBTITLE = 32
        self.FONT_BODY = 26
        self.FONT_FORMULA = 32
        self.FONT_SMALL = 22
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_examples()
        self.show_rule()
        self.show_full_example()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 - 引出问题"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这个式子能化简吗?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 复杂代数式
        complex_expr = MathTex(
            r"3x^2y - 5x^2y + 2xy + 4x^2y - xy",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        self.play(Write(complex_expr), run_time=1.5)
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.4)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.5)
        self.wait(0.5)
        
        # 清理，保留式子
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            complex_expr.animate.scale(0.7).move_to(UP * 6),
            run_time=0.6
        )
        
        # 答案提示
        answer_hint = Text(
            "答案: 可以! 利用同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 5)
        
        self.play(FadeIn(answer_hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        self.play(
            FadeOut(complex_expr),
            FadeOut(answer_hint),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 什么是同类项"""
        # 标题
        title = Text(
            "什么是同类项?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义框
        definition_text_1 = Text(
            "所含字母相同",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        )
        
        definition_text_2 = Text(
            "相同字母的指数也分别相同",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        )
        
        definition = VGroup(definition_text_1, definition_text_2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 4)
        
        self.play(Write(definition_text_1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(definition_text_2), run_time=1.0)
        self.wait(0.5)
        
        # 示例: 3x²y 和 -5x²y
        term1 = MathTex(
            r"3x^2y",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 2 + LEFT * 2)
        
        term2 = MathTex(
            r"-5x^2y",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 2 + RIGHT * 2)
        
        self.play(Write(term1), run_time=0.6)
        self.play(Write(term2), run_time=0.6)
        
        # 标注字母部分
        letter_label = Text(
            "字母: x²y 相同",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_VARIABLE
        ).move_to(UP * 0.5)
        
        # 高亮字母部分
        rect1 = SurroundingRectangle(term1[0][1:], color=self.COLOR_VARIABLE, buff=0.1)
        rect2 = SurroundingRectangle(term2[0][2:], color=self.COLOR_VARIABLE, buff=0.1)
        
        self.play(
            Create(rect1),
            Create(rect2),
            FadeIn(letter_label, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 标注指数
        exponent_label = Text(
            "指数: x是2, y是1, 都相同",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_VARIABLE
        ).move_to(DOWN * 0.3)
        
        self.play(
            FadeOut(letter_label),
            FadeIn(exponent_label, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 打勾表示是同类项
        checkmark = Text(
            "✓ 这是同类项!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeIn(checkmark, scale=0.5),
            Flash(checkmark, color=self.COLOR_SUCCESS, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(term1),
            FadeOut(term2),
            FadeOut(rect1),
            FadeOut(rect2),
            FadeOut(exponent_label),
            FadeOut(checkmark),
            run_time=0.6
        )
    
    def show_examples(self):
        """场景3: 同类项的判断 - 正反例"""
        # 标题
        title = Text(
            "判断是否为同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # === 正例1: 3x²y 和 -5x²y ===
        example1_label = Text(
            "例1:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 5 + LEFT * 3.5)
        
        ex1_term1 = MathTex(r"3x^2y", font_size=self.FONT_FORMULA).next_to(example1_label, RIGHT, buff=0.3)
        ex1_and = Text("和", font="Noto Sans CJK SC", font_size=self.FONT_BODY).next_to(ex1_term1, RIGHT, buff=0.2)
        ex1_term2 = MathTex(r"-5x^2y", font_size=self.FONT_FORMULA).next_to(ex1_and, RIGHT, buff=0.2)
        
        example1 = VGroup(example1_label, ex1_term1, ex1_and, ex1_term2)
        
        self.play(FadeIn(example1, shift=RIGHT * 0.5), run_time=0.6)
        
        # 框选相同部分
        rect1_1 = SurroundingRectangle(ex1_term1[0][1:], color=self.COLOR_SUCCESS, buff=0.08)
        rect1_2 = SurroundingRectangle(ex1_term2[0][2:], color=self.COLOR_SUCCESS, buff=0.08)
        
        self.play(Create(rect1_1), Create(rect1_2), run_time=0.5)
        
        # 打勾
        check1 = Text("✓", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_SUCCESS).next_to(example1, RIGHT, buff=0.3)
        self.play(FadeIn(check1, scale=0.5), run_time=0.4)
        self.wait(0.5)
        
        self.play(FadeOut(rect1_1), FadeOut(rect1_2), run_time=0.3)
        
        # === 正例2: 2a 和 -7a ===
        example2_label = Text(
            "例2:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 3.8 + LEFT * 3.5)
        
        ex2_term1 = MathTex(r"2a", font_size=self.FONT_FORMULA).next_to(example2_label, RIGHT, buff=0.3)
        ex2_and = Text("和", font="Noto Sans CJK SC", font_size=self.FONT_BODY).next_to(ex2_term1, RIGHT, buff=0.2)
        ex2_term2 = MathTex(r"-7a", font_size=self.FONT_FORMULA).next_to(ex2_and, RIGHT, buff=0.2)
        
        example2 = VGroup(example2_label, ex2_term1, ex2_and, ex2_term2)
        
        self.play(FadeIn(example2, shift=RIGHT * 0.5), run_time=0.5)
        
        check2 = Text("✓", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_SUCCESS).next_to(example2, RIGHT, buff=0.3)
        self.play(FadeIn(check2, scale=0.5), run_time=0.4)
        self.wait(0.4)
        
        # === 正例3: 常数项 5 和 -3 ===
        example3_label = Text(
            "例3:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2.6 + LEFT * 3.5)
        
        ex3_term1 = MathTex(r"5", font_size=self.FONT_FORMULA).next_to(example3_label, RIGHT, buff=0.3)
        ex3_and = Text("和", font="Noto Sans CJK SC", font_size=self.FONT_BODY).next_to(ex3_term1, RIGHT, buff=0.2)
        ex3_term2 = MathTex(r"-3", font_size=self.FONT_FORMULA).next_to(ex3_and, RIGHT, buff=0.2)
        
        example3 = VGroup(example3_label, ex3_term1, ex3_and, ex3_term2)
        
        self.play(FadeIn(example3, shift=RIGHT * 0.5), run_time=0.5)
        
        # 特殊说明
        constant_note = Text(
            "常数项都是同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(example3, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(FadeIn(constant_note, shift=UP * 0.2), run_time=0.5)
        
        check3 = Text("✓", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_SUCCESS).next_to(example3, RIGHT, buff=0.3)
        self.play(FadeIn(check3, scale=0.5), run_time=0.4)
        self.wait(0.8)
        
        self.play(FadeOut(constant_note), run_time=0.3)
        
        # === 反例1: 3x²y 和 3xy² ===
        example4_label = Text(
            "例4:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 1 + LEFT * 3.5)
        
        ex4_term1 = MathTex(r"3x^2y", font_size=self.FONT_FORMULA).next_to(example4_label, RIGHT, buff=0.3)
        ex4_and = Text("和", font="Noto Sans CJK SC", font_size=self.FONT_BODY).next_to(ex4_term1, RIGHT, buff=0.2)
        ex4_term2 = MathTex(r"3xy^2", font_size=self.FONT_FORMULA).next_to(ex4_and, RIGHT, buff=0.2)
        
        example4 = VGroup(example4_label, ex4_term1, ex4_and, ex4_term2)
        
        self.play(FadeIn(example4, shift=RIGHT * 0.5), run_time=0.6)
        
        # 标注指数不同
        diff_note = Text(
            "指数不同!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_ERROR
        ).next_to(example4, DOWN, buff=0.2, aligned_edge=LEFT)
        
        # 红色高亮指数
        rect4_1 = SurroundingRectangle(ex4_term1[0][2], color=self.COLOR_ERROR, buff=0.08)  # x²的2
        rect4_2 = SurroundingRectangle(ex4_term2[0][3], color=self.COLOR_ERROR, buff=0.08)  # y²的2
        
        self.play(
            Create(rect4_1),
            Create(rect4_2),
            FadeIn(diff_note, shift=UP * 0.2),
            run_time=0.6
        )
        
        # 打叉
        cross1 = Text("✗", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_ERROR).next_to(example4, RIGHT, buff=0.3)
        self.play(FadeIn(cross1, scale=0.5), run_time=0.4)
        self.wait(0.6)
        
        self.play(FadeOut(rect4_1), FadeOut(rect4_2), FadeOut(diff_note), run_time=0.3)
        
        # === 反例2: 2a² 和 2a ===
        example5_label = Text(
            "例5:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 0.2 + LEFT * 3.5)
        
        ex5_term1 = MathTex(r"2a^2", font_size=self.FONT_FORMULA).next_to(example5_label, RIGHT, buff=0.3)
        ex5_and = Text("和", font="Noto Sans CJK SC", font_size=self.FONT_BODY).next_to(ex5_term1, RIGHT, buff=0.2)
        ex5_term2 = MathTex(r"2a", font_size=self.FONT_FORMULA).next_to(ex5_and, RIGHT, buff=0.2)
        
        example5 = VGroup(example5_label, ex5_term1, ex5_and, ex5_term2)
        
        self.play(FadeIn(example5, shift=RIGHT * 0.5), run_time=0.5)
        
        # 标注指数不同
        diff_note2 = Text(
            "指数不同!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_ERROR
        ).next_to(example5, DOWN, buff=0.2, aligned_edge=LEFT)
        
        rect5 = SurroundingRectangle(ex5_term1[0][2], color=self.COLOR_ERROR, buff=0.08)  # a²的2
        
        self.play(
            Create(rect5),
            FadeIn(diff_note2, shift=UP * 0.2),
            run_time=0.5
        )
        
        cross2 = Text("✗", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_ERROR).next_to(example5, RIGHT, buff=0.3)
        self.play(FadeIn(cross2, scale=0.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example1), FadeOut(check1),
            FadeOut(example2), FadeOut(check2),
            FadeOut(example3), FadeOut(check3),
            FadeOut(example4), FadeOut(cross1), FadeOut(rect5), FadeOut(diff_note2),
            FadeOut(example5), FadeOut(cross2),
            run_time=0.6
        )
    
    def show_rule(self):
        """场景4: 合并同类项的法则"""
        # 标题
        title = Text(
            "合并同类项法则",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 法则内容
        rule_part1 = Text(
            "系数相加",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_COEFFICIENT
        )
        
        rule_part2 = Text(
            "字母及其指数不变",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_VARIABLE
        )
        
        rule = VGroup(rule_part1, rule_part2).arrange(DOWN, buff=0.4).move_to(UP * 4.5)
        
        self.play(Write(rule_part1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(rule_part2), run_time=1.0)
        self.wait(0.6)
        
        # 示例: 3x²y + (-5x²y) = -2x²y
        example_title = Text(
            "例如:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(example_title), run_time=0.4)
        
        # 原式
        original = MathTex(
            r"3x^2y + (-5x^2y)",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 2)
        
        self.play(Write(original), run_time=1.0)
        
        # 高亮系数
        coeff_box1 = SurroundingRectangle(original[0][0], color=self.COLOR_COEFFICIENT, buff=0.1)
        coeff_box2 = SurroundingRectangle(original[0][5:7], color=self.COLOR_COEFFICIENT, buff=0.1)
        
        coeff_label = Text(
            "系数: 3 和 -5",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 0.8)
        
        self.play(
            Create(coeff_box1),
            Create(coeff_box2),
            FadeIn(coeff_label, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(0.6)
        
        # 箭头指向相加
        arrow_down = Arrow(
            start=coeff_label.get_bottom(),
            end=coeff_label.get_bottom() + DOWN * 0.8,
            color=self.COLOR_COEFFICIENT,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(Create(arrow_down), run_time=0.4)
        
        # 系数计算
        calc = MathTex(
            r"3 + (-5) = -2",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_COEFFICIENT
        ).move_to(DOWN * 0.3)
        
        self.play(Write(calc), run_time=0.8)
        self.wait(0.6)
        
        # 保留字母部分
        var_label = Text(
            "字母部分保持不变: x²y",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_VARIABLE
        ).move_to(DOWN * 1.5)
        
        var_box = SurroundingRectangle(original[0][1:4], color=self.COLOR_VARIABLE, buff=0.1)
        
        self.play(
            FadeOut(coeff_box1),
            FadeOut(coeff_box2),
            FadeOut(coeff_label),
            FadeOut(arrow_down),
            Create(var_box),
            FadeIn(var_label, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(0.6)
        
        # 最终结果
        equals = MathTex(r"=", font_size=self.FONT_FORMULA).move_to(DOWN * 2.8)
        result = MathTex(
            r"-2x^2y",
            font_size=self.FONT_FORMULA,
            color=GOLD
        ).next_to(equals, RIGHT, buff=0.3)
        
        result_box = SurroundingRectangle(result, color=GOLD, buff=0.2)
        
        self.play(
            FadeOut(calc),
            FadeOut(var_box),
            FadeOut(var_label),
            Write(equals),
            run_time=0.4
        )
        
        self.play(
            Write(result),
            Create(result_box),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule),
            FadeOut(example_title),
            FadeOut(original),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(result_box),
            run_time=0.6
        )
    
    def show_full_example(self):
        """场景5: 完整示例演示"""
        # 标题
        title = Text(
            "完整示例",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 原式
        original_label = Text(
            "化简:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 5.5 + LEFT * 3.5)
        
        original = MathTex(
            r"3x^2y - 5x^2y + 2xy + 4x^2y - xy",
            font_size=self.FONT_FORMULA - 2
        ).next_to(original_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(original_label),
            Write(original),
            run_time=1.2
        )
        self.wait(0.5)
        
        # 步骤1: 找出同类项
        step1 = Text(
            "步骤1: 找出同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.5)
        
        # 框选 x²y 项
        # 在 MathTex 中: 3x^2y (索引0-3), -5x^2y (索引4-8), 4x^2y (索引13-16)
        box_x2y_1 = SurroundingRectangle(original[0][0:4], color=self.COLOR_PRIMARY, buff=0.08)
        box_x2y_2 = SurroundingRectangle(original[0][4:9], color=self.COLOR_PRIMARY, buff=0.08)
        box_x2y_3 = SurroundingRectangle(original[0][13:17], color=self.COLOR_PRIMARY, buff=0.08)
        
        x2y_label = Text(
            "x²y项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3)
        
        self.play(
            Create(box_x2y_1),
            Create(box_x2y_2),
            Create(box_x2y_3),
            FadeIn(x2y_label),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 框选 xy 项
        # 2xy (索引9-11), -xy (索引17-19)
        box_xy_1 = SurroundingRectangle(original[0][10:13], color=self.COLOR_SECONDARY, buff=0.08)
        box_xy_2 = SurroundingRectangle(original[0][18:21], color=self.COLOR_SECONDARY, buff=0.08)
        
        xy_label = Text(
            "xy项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 2.3)
        
        self.play(
            Create(box_xy_1),
            Create(box_xy_2),
            FadeIn(xy_label),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 清除框选
        self.play(
            FadeOut(box_x2y_1), FadeOut(box_x2y_2), FadeOut(box_x2y_3),
            FadeOut(box_xy_1), FadeOut(box_xy_2),
            FadeOut(x2y_label), FadeOut(xy_label),
            FadeOut(step1),
            run_time=0.5
        )
        
        # 步骤2: 合并 x²y 项
        step2 = Text(
            "步骤2: 合并x²y项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.5)
        
        # 合并过程
        x2y_combine = MathTex(
            r"(3 - 5 + 4)x^2y",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 2.5)
        
        self.play(Write(x2y_combine), run_time=0.8)
        
        # 计算系数
        x2y_calc = MathTex(
            r"3 - 5 + 4 = 2",
            font_size=self.FONT_BODY,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 1.5)
        
        self.play(Write(x2y_calc), run_time=0.8)
        self.wait(0.4)
        
        # 结果1
        result1 = MathTex(
            r"2x^2y",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.5)
        
        result1_box = SurroundingRectangle(result1, color=self.COLOR_PRIMARY, buff=0.15)
        
        self.play(
            Write(result1),
            Create(result1_box),
            run_time=0.6
        )
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(step2),
            FadeOut(x2y_combine),
            FadeOut(x2y_calc),
            run_time=0.4
        )
        
        # 步骤3: 合并 xy 项
        step3 = Text(
            "步骤3: 合并xy项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.5)
        
        # 合并过程
        xy_combine = MathTex(
            r"(2 - 1)xy",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 2.5)
        
        self.play(Write(xy_combine), run_time=0.8)
        
        # 计算系数
        xy_calc = MathTex(
            r"2 - 1 = 1",
            font_size=self.FONT_BODY,
            color=self.COLOR_COEFFICIENT
        ).move_to(UP * 1.5)
        
        self.play(Write(xy_calc), run_time=0.8)
        self.wait(0.4)
        
        # 结果2
        result2 = MathTex(
            r"xy",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 0.5)
        
        result2_box = SurroundingRectangle(result2, color=self.COLOR_SECONDARY, buff=0.15)
        
        self.play(
            Write(result2),
            Create(result2_box),
            run_time=0.6
        )
        self.wait(0.6)
        
        # 清理中间步骤
        self.play(
            FadeOut(step3),
            FadeOut(xy_combine),
            FadeOut(xy_calc),
            run_time=0.4
        )
        
        # 步骤4: 组合最终答案
        step4 = Text(
            "步骤4: 写出最终答案",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(step4, shift=UP * 0.2), run_time=0.5)
        
        # 移动两个结果到中间
        self.play(
            result1.animate.move_to(UP * 2.2 + LEFT * 1.2),
            result1_box.animate.move_to(UP * 2.2 + LEFT * 1.2),
            result2.animate.move_to(UP * 2.2 + RIGHT * 1.2),
            result2_box.animate.move_to(UP * 2.2 + RIGHT * 1.2),
            run_time=0.6
        )
        
        # 加号
        plus = MathTex(r"+", font_size=self.FONT_FORMULA).move_to(UP * 2.2)
        self.play(Write(plus), run_time=0.3)
        
        # 最终答案
        final_label = Text(
            "答案:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 0.8 + LEFT * 2)
        
        final_answer = MathTex(
            r"2x^2y + xy",
            font_size=self.FONT_FORMULA + 4,
            color=GOLD
        ).next_to(final_label, RIGHT, buff=0.3)
        
        final_box = SurroundingRectangle(final_answer, color=GOLD, buff=0.2, stroke_width=3)
        
        self.play(
            FadeIn(final_label),
            Write(final_answer),
            run_time=0.8
        )
        
        self.play(Create(final_box), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(original_label),
            FadeOut(original),
            FadeOut(step4),
            FadeOut(result1),
            FadeOut(result1_box),
            FadeOut(result2),
            FadeOut(result2_box),
            FadeOut(plus),
            FadeOut(final_label),
            FadeOut(final_answer),
            FadeOut(final_box),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景6: 总结与关注"""
        # 总结标题
        summary_title = Text(
            "记住这三点!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 要点1
        point1_icon = Text("①", font="Noto Sans CJK SC", font_size=self.FONT_SUBTITLE, color=self.COLOR_PRIMARY)
        point1_text = Text(
            "字母相同且指数相同",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        point1 = VGroup(point1_icon, point1_text).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        self.play(FadeIn(point1, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        
        # 要点2
        point2_icon = Text("②", font="Noto Sans CJK SC", font_size=self.FONT_SUBTITLE, color=self.COLOR_COEFFICIENT)
        point2_text = Text(
            "系数相加",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        point2 = VGroup(point2_icon, point2_text).arrange(RIGHT, buff=0.3).move_to(UP * 2.8)
        
        self.play(FadeIn(point2, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        
        # 要点3
        point3_icon = Text("③", font="Noto Sans CJK SC", font_size=self.FONT_SUBTITLE, color=self.COLOR_VARIABLE)
        point3_text = Text(
            "字母和指数不变",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        point3 = VGroup(point3_icon, point3_text).arrange(RIGHT, buff=0.3).move_to(UP * 1.6)
        
        self.play(FadeIn(point3, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(1.0)
        
        # 清理要点
        self.play(
            FadeOut(summary_title),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3),
            run_time=0.5
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多代数技巧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小装饰 - 代数符号
        symbols = VGroup(
            MathTex(r"x^2", font_size=30, color=self.COLOR_PRIMARY),
            MathTex(r"y^3", font_size=30, color=self.COLOR_SECONDARY),
            MathTex(r"a+b", font_size=30, color=self.COLOR_COEFFICIENT),
            MathTex(r"2xy", font_size=30, color=self.COLOR_VARIABLE),
            MathTex(r"3ab", font_size=30, color=GOLD),
            MathTex(r"m^2", font_size=30, color=self.COLOR_PRIMARY),
        )
        
        # 排列成圆形
        for i, sym in enumerate(symbols):
            angle = i * PI / 3
            radius = 2.5
            x = radius * np.cos(angle)
            y = radius * np.sin(angle) - 2.5
            sym.move_to([x, y, 0])
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in symbols],
            run_time=0.6
        )
        
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql like_terms.py LikeTerms  # 快速预览
# manim -qh like_terms.py LikeTerms   # 高质量渲染
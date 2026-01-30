"""
因式分解——提公因式法 教学动画
Factorization - Common Factor Method Teaching Animation

内容: 提公因式法的概念、步骤和应用
年级: 七年级
目标观众: 初中学生
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


class CommonFactorMethod(Scene):
    """
    因式分解——提公因式法教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 概念引入 - 什么是公因式
    3. 提取步骤演示 - 详细三步骤
    4. 口诀记忆 - 记忆技巧
    5. 练习示例1 - 基础例题
    6. 练习示例2 - 进阶例题
    7. 结尾总结 - 要点回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主公式
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 公因式高亮
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色 - 正确
        self.COLOR_STEP = "#9b59b6"         # 紫色 - 步骤
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_FORMULA = 32
        
        # 执行动画序列
        self.show_opening()
        self.show_concept_intro()
        self.show_extraction_steps()
        self.show_memory_tips()
        self.show_example_1()
        self.show_example_2()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这个式子能化简吗?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 示例公式
        example_formula = MathTex(
            r"6x^2y - 9xy^2",
            font_size=self.FONT_FORMULA + 8,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2)
        
        self.play(Write(example_formula), run_time=1.2)
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).next_to(example_formula, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(question_mark, scale=1.5),
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            example_formula.animate.move_to(UP * 3.5).scale(0.8),
            run_time=0.6
        )
        
        # 保存供下一场景使用
        self.example_formula = example_formula
    
    def show_concept_intro(self):
        """场景2: 概念引入"""
        # 标题
        title = Text(
            "什么是公因式?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 简单例子: 6x + 9x
        simple_example = MathTex(
            r"6x + 9x",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.example_formula, simple_example),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 拆解为乘积形式
        explanation_text = Text(
            "展开看看:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(ORIGIN)
        
        self.play(FadeIn(explanation_text), run_time=0.4)
        
        # 展开形式
        expanded = MathTex(
            r"6 \cdot x + 9 \cdot x",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(Write(expanded), run_time=1.0)
        self.wait(0.5)
        
        # 高亮公因式 x
        common_factor_boxes = VGroup(
            SurroundingRectangle(expanded[0][2], color=self.COLOR_SECONDARY, buff=0.08),
            SurroundingRectangle(expanded[0][6], color=self.COLOR_SECONDARY, buff=0.08)
        )
        
        self.play(Create(common_factor_boxes), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "x 是公因式 (各项都有的因式)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation_text),
            FadeOut(expanded),
            FadeOut(common_factor_boxes),
            FadeOut(explanation),
            FadeOut(self.example_formula),
            run_time=0.6
        )
    
    def show_extraction_steps(self):
        """场景3: 提取步骤演示"""
        # 主标题
        main_title = Text(
            "提公因式法 - 三步骤",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(main_title), run_time=0.8)
        
        # === 步骤1: 找公因式 ===
        step1_title = Text(
            "步骤1: 找公因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_STEP
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(step1_title, shift=RIGHT * 0.3), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"6x^2y - 9xy^2",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 分析系数
        coeff_text = Text(
            "系数: 6, 9 → GCD = 3",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        coeff_boxes = VGroup(
            SurroundingRectangle(formula[0][0], color=YELLOW, buff=0.08),
            SurroundingRectangle(formula[0][3], color=YELLOW, buff=0.08)
        )
        
        self.play(Create(coeff_boxes), run_time=0.5)
        self.play(FadeIn(coeff_text), run_time=0.5)
        self.wait(0.8)
        
        # 分析字母
        var_text = Text(
            "字母: x²y, xy² → xy (最低次幂)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        var_boxes = VGroup(
            SurroundingRectangle(formula[0][1:4], color=YELLOW, buff=0.08),
            SurroundingRectangle(formula[0][4:7], color=YELLOW, buff=0.08)
        )
        
        self.play(
            FadeOut(coeff_boxes),
            Create(var_boxes),
            run_time=0.5
        )
        self.play(FadeIn(var_text), run_time=0.5)
        self.wait(0.8)
        
        # # 公因式结果
        # common_factor_result = MathTex(
        #     r"\text{公因式} = 3xy",
        #     font_size=self.FONT_FORMULA - 4,
        #     color=self.COLOR_SECONDARY
        # ).move_to(DOWN * 2)
        
        # 修复中文问题
        common_factor_text = Text(
            "公因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        )
        common_factor_math = MathTex(
            r"= 3xy",
            font_size=self.FONT_FORMULA - 4,
            color=self.COLOR_SECONDARY
        )
        common_factor_result = VGroup(common_factor_text, common_factor_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 2)
        
        self.play(
            FadeOut(var_boxes),
            Write(common_factor_result),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理步骤1
        self.play(
            FadeOut(step1_title),
            FadeOut(coeff_text),
            FadeOut(var_text),
            FadeOut(common_factor_result),
            run_time=0.4
        )
        
        # === 步骤2: 提取公因式 ===
        step2_title = Text(
            "步骤2: 提取公因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_STEP
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(step2_title, shift=RIGHT * 0.3), run_time=0.5)
        
        # 变换为因式分解形式
        factored = MathTex(
            r"3xy", r"(", r"2x - 3y", r")",
            font_size=self.FONT_FORMULA,
            color=WHITE
        )
        factored[0].set_color(self.COLOR_SECONDARY)  # 公因式红色
        factored.move_to(UP * 2.5)
        
        # 添加箭头
        arrow = Arrow(
            formula.get_bottom() + DOWN * 0.3,
            factored.get_top() + UP * 0.3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(
            ReplacementTransform(formula.copy(), factored),
            run_time=1.0
        )
        
        # 说明商式
        quotient_text = Text(
            "括号内是各项除以公因式的商",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        quotient_detail = MathTex(
            r"6x^2y \div 3xy = 2x",
            font_size=self.FONT_BODY + 2,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        quotient_detail2 = MathTex(
            r"9xy^2 \div 3xy = 3y",
            font_size=self.FONT_BODY + 2,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(quotient_text), run_time=0.5)
        self.play(Write(quotient_detail), run_time=0.8)
        self.play(Write(quotient_detail2), run_time=0.8)
        self.wait(1.0)
        
        # 清理步骤2
        self.play(
            FadeOut(step2_title),
            FadeOut(arrow),
            FadeOut(quotient_text),
            FadeOut(quotient_detail),
            FadeOut(quotient_detail2),
            run_time=0.4
        )
        
        # === 步骤3: 检验结果 ===
        step3_title = Text(
            "步骤3: 检验结果",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_STEP
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(step3_title, shift=RIGHT * 0.3), run_time=0.5)
        
        # 展开验证
        verify_text = Text(
            "展开验证:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        expansion = MathTex(
            r"3xy(2x - 3y) = 6x^2y - 9xy^2",
            font_size=self.FONT_FORMULA - 4,
            color=WHITE
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(verify_text), run_time=0.4)
        self.play(Write(expansion), run_time=1.2)
        
        # 对比箭头
        comparison_arrow = DoubleArrow(
            formula.get_right() + RIGHT * 0.3,
            factored.get_left() + LEFT * 0.3,
            color=self.COLOR_SUCCESS,
            buff=0.1,
            stroke_width=3
        ).rotate(90 * DEGREES)
        
        check_text = Text(
            "相等!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SUCCESS
        ).next_to(expansion, DOWN, buff=0.5)
        
        # 打勾
        checkmark = MathTex(
            r"\checkmark",
            font_size=60,
            color=self.COLOR_SUCCESS
        ).next_to(check_text, RIGHT, buff=0.3)
        
        self.play(FadeIn(check_text), run_time=0.5)
        self.play(DrawBorderThenFill(checkmark), run_time=0.6)
        self.wait(1.0)
        
        # 清理全部
        self.play(
            FadeOut(main_title),
            FadeOut(step3_title),
            FadeOut(formula),
            FadeOut(factored),
            FadeOut(verify_text),
            FadeOut(expansion),
            FadeOut(check_text),
            FadeOut(checkmark),
            run_time=0.6
        )
    
    def show_memory_tips(self):
        """场景4: 口诀记忆"""
        # 标题
        title = Text(
            "记忆口诀",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 口诀卡片背景
        card_bg = RoundedRectangle(
            width=7,
            height=5,
            corner_radius=0.3,
            color=self.COLOR_STEP,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(UP * 1)
        
        self.play(FadeIn(card_bg, scale=0.8), run_time=0.6)
        
        # 口诀内容
        lines = [
            "找: 找出公因式",
            "提: 提到括号外",
            "除: 各项除公因式",
            "验: 乘法验证答案"
        ]
        
        line_objects = VGroup()
        for i, line in enumerate(lines):
            line_obj = Text(
                line,
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY + 2,
                color=WHITE
            ).move_to(UP * (2.5 - i * 1))
            line_objects.add(line_obj)
        
        # 依次书写口诀
        for line_obj in line_objects:
            self.play(Write(line_obj), run_time=0.8)
            self.wait(0.1)
        
        # 装饰图标
        icons = VGroup(
            MathTex(r"\searrow", font_size=40, color=YELLOW).next_to(line_objects[0], LEFT),
            MathTex(r"\rightarrow", font_size=40, color=YELLOW).next_to(line_objects[1], LEFT),
            MathTex(r"\div", font_size=40, color=YELLOW).next_to(line_objects[2], LEFT),
            MathTex(r"\checkmark", font_size=40, color=YELLOW).next_to(line_objects[3], LEFT)
        )
        
        self.play(FadeIn(icons, shift=RIGHT * 0.2), run_time=0.6)
        
        # 整体强调
        self.play(
            Indicate(card_bg, scale_factor=1.05, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card_bg),
            FadeOut(line_objects),
            FadeOut(icons),
            run_time=0.6
        )
    
    def show_example_1(self):
        """场景5: 练习示例1"""
        # 例题标题
        title = Text(
            "练习1",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 题目
        problem_label = Text(
            "因式分解:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 4)
        
        problem = MathTex(
            r"12a^2b - 8ab^2",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(Write(problem_label), run_time=0.4)
        self.play(Write(problem), run_time=0.8)
        self.wait(0.5)
        
        # 找公因式过程
        analysis = Text(
            "系数GCD: 4  字母: ab",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 1.5)
        
        common_factor_box = SurroundingRectangle(
            analysis,
            color=self.COLOR_SECONDARY,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(FadeIn(analysis), run_time=0.6)
        self.play(Create(common_factor_box), run_time=0.4)
        self.wait(0.8)
        
        # 箭头
        arrow = Arrow(
            problem.get_bottom() + DOWN * 0.2,
            UP * 0.3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 答案
        answer = MathTex(
            r"4ab", r"(", r"3a - 2b", r")",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 0.5)
        answer[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(answer), run_time=1.0)
        
        # 高亮答案
        answer_box = SurroundingRectangle(
            answer,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(answer_box), run_time=0.5)
        
        # 确认对号
        check = MathTex(
            r"\checkmark",
            font_size=50,
            color=self.COLOR_SUCCESS
        ).next_to(answer, RIGHT, buff=0.4)
        
        self.play(
            DrawBorderThenFill(check),
            Flash(check, color=self.COLOR_SUCCESS),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem_label),
            FadeOut(problem),
            FadeOut(analysis),
            FadeOut(common_factor_box),
            FadeOut(arrow),
            FadeOut(answer),
            FadeOut(answer_box),
            FadeOut(check),
            run_time=0.6
        )
    
    def show_example_2(self):
        """场景6: 练习示例2"""
        # 例题标题
        title = Text(
            "练习2",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 题目
        problem_label = Text(
            "因式分解:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 4)
        
        problem = MathTex(
            r"5x^3 + 10x^2 - 15x",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(Write(problem_label), run_time=0.4)
        self.play(Write(problem), run_time=0.8)
        self.wait(0.5)
        
        # 分析系数
        coeff_hint = Text(
            "系数: 5, 10, 15 → GCD = 5",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(coeff_hint), run_time=0.6)
        
        # 高亮系数
        coeff_boxes = VGroup(
            SurroundingRectangle(problem[0][0], color=YELLOW, buff=0.08),
            SurroundingRectangle(problem[0][5], color=YELLOW, buff=0.08),
            SurroundingRectangle(problem[0][6:8], color=YELLOW, buff=0.08)
        )
        self.play(Create(coeff_boxes), run_time=0.5)
        self.wait(0.6)
        
        # 分析字母
        var_hint = Text(
            "字母: x³, x², x → 最低次幂 x",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        self.play(
            FadeOut(coeff_boxes),
            FadeIn(var_hint),
            run_time=0.6
        )
        
        # # 公因式
        # common_factor_result = MathTex(
        #     r"\text{公因式: } 5x",
        #     font_size=self.FONT_BODY + 4,
        #     color=self.COLOR_SECONDARY
        # ).move_to(DOWN * 0.5)
        
        # 修复中文
        cf_text = Text(
            "公因式:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        )
        cf_math = MathTex(
            r"5x",
            font_size=self.FONT_BODY + 4,
            color=self.COLOR_SECONDARY
        )
        common_factor_result = VGroup(cf_text, cf_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)
        
        self.play(Write(common_factor_result), run_time=0.8)
        self.wait(0.8)
        
        # 箭头
        arrow = Arrow(
            common_factor_result.get_bottom() + DOWN * 0.2,
            DOWN * 2,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 答案
        answer = MathTex(
            r"5x", r"(", r"x^2 + 2x - 3", r")",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 2.8)
        answer[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(answer), run_time=1.0)
        
        # 答案框
        answer_box = SurroundingRectangle(
            answer,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(answer_box), run_time=0.5)
        
        # 确认
        check = MathTex(
            r"\checkmark",
            font_size=50,
            color=self.COLOR_SUCCESS
        ).next_to(answer, RIGHT, buff=0.4)
        
        self.play(
            Flash(answer, color=self.COLOR_SUCCESS),
            DrawBorderThenFill(check),
            run_time=0.8
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem_label),
            FadeOut(problem),
            FadeOut(coeff_hint),
            FadeOut(var_hint),
            FadeOut(common_factor_result),
            FadeOut(arrow),
            FadeOut(answer),
            FadeOut(answer_box),
            FadeOut(check),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 结尾总结"""
        # 总结标题
        title = Text(
            "总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE + 4,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 要点卡片
        points = [
            "✓ 公因式 = 系数GCD × 公有字母最低次幂",
            "✓ 提取要完全 (不能漏)",
            "✓ 记住: 找-提-除-验"
        ]
        
        point_objects = VGroup()
        for i, point in enumerate(points):
            point_obj = Text(
                point,
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=WHITE,
                line_spacing=1.2
            ).move_to(UP * (3 - i * 1.5))
            point_objects.add(point_obj)
        
        # 依次滑入
        for point_obj in point_objects:
            self.play(FadeIn(point_obj, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(0.5)
        
        # 装饰
        decorations = VGroup(
            MathTex(r"\star", font_size=30, color=GOLD).move_to(UP * 5 + LEFT * 3),
            MathTex(r"\star", font_size=30, color=GOLD).move_to(UP * 5 + RIGHT * 3),
            MathTex(r"\star", font_size=30, color=GOLD).move_to(DOWN * 0.5 + LEFT * 3),
            MathTex(r"\star", font_size=30, color=GOLD).move_to(DOWN * 0.5 + RIGHT * 3)
        )
        
        self.play(Create(decorations), run_time=0.6)
        self.wait(1.0)
        
        # 作者信息放大居中
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 4)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(follow_text), run_time=0.8)
        self.play(Flash(follow_text, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        self.wait(1.0)
        
        # 结束淡出
        self.play(
            FadeOut(title),
            FadeOut(point_objects),
            FadeOut(decorations),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            run_time=1.0
        )


# 渲染命令:
# manim -pql common_factor_method.py CommonFactorMethod  # 快速预览 (480p)
# manim -qh common_factor_method.py CommonFactorMethod   # 高质量渲染 (1080p)
# manim -qk common_factor_method.py CommonFactorMethod   # 4K渲染
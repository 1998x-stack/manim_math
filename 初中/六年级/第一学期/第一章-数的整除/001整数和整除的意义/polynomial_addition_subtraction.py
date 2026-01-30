"""
整式的加减法 - Polynomial Addition and Subtraction
使用 Manim 创建的七年级数学教学视频

内容: 去括号法则与合并同类项
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


class PolynomialAdditionSubtraction(Scene):
    """
    整式加减法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 去括号法则 - 正号
    3. 去括号法则 - 负号（重点）
    4. 综合例题呈现
    5. 去括号过程演示
    6. 合并同类项
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要项
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要项  
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正号
        self.COLOR_NEGATIVE = "#e67e22"     # 橙色 - 负号
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 字体大小常量
        self.FONT_SIZE_TITLE = 36
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 22
        self.FONT_SIZE_FORMULA = 32
        self.FONT_SIZE_SMALL = 18
        
        # 执行动画序列
        self.show_opening()
        self.show_rule_positive()
        self.show_rule_negative()
        self.show_example_intro()
        self.show_remove_brackets()
        self.show_combine_terms()
        self.show_outro()
    
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
        hook = Text(
            "这道题你会做吗？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 示例问题
        problem = MathTex(
            r"(2x+3) - (x-1) = ?",
            font_size=self.FONT_SIZE_FORMULA * 1.2
        ).move_to(UP * 3.5)
        
        # 设置颜色
        problem.set_color_by_tex("2x", self.COLOR_PRIMARY)
        problem.set_color_by_tex("x", self.COLOR_SECONDARY)
        problem.set_color_by_tex("3", self.COLOR_POSITIVE)
        problem.set_color_by_tex("1", self.COLOR_POSITIVE)
        
        self.play(FadeIn(problem, shift=UP * 0.3), run_time=0.6)
        
        # 思考提示
        think = Text(
            "先别急着算！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(think, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)
        
        # 引出主题
        intro = Text(
            "掌握两个技巧就能轻松搞定",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 0.5)
        
        self.play(Write(intro), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(problem),
            FadeOut(think),
            FadeOut(intro),
            run_time=0.5
        )
    
    def show_rule_positive(self):
        """场景2: 去括号法则 - 正号情况"""
        # 标题
        title = Text(
            "技巧一：去括号法则（正号）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 左侧公式
        formula_left = MathTex(
            r"+(a+b)",
            font_size=self.FONT_SIZE_FORMULA * 1.3
        ).move_to(UP * 3 + LEFT * 2)
        
        self.play(Write(formula_left), run_time=0.8)
        
        # 高亮括号和正号
        plus_sign = formula_left[0][0]
        bracket_group = VGroup(formula_left[0][1], formula_left[0][5])  # 括号
        
        # 括号高亮框
        bracket_box = SurroundingRectangle(
            bracket_group,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(Create(bracket_box), run_time=0.5)
        
        # 正号闪烁
        self.play(
            Indicate(plus_sign, color=self.COLOR_POSITIVE, scale_factor=1.5),
            run_time=0.6
        )
        
        # 箭头
        arrow = Arrow(
            UP * 3 + LEFT * 0.3,
            UP * 3 + RIGHT * 0.3,
            color=WHITE,
            buff=0.2
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 右侧结果
        formula_right = MathTex(
            r"a+b",
            font_size=self.FONT_SIZE_FORMULA * 1.3
        ).move_to(UP * 3 + RIGHT * 2)
        
        self.play(Write(formula_right), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "括号前是正号\n括号内各项符号不变",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.6)
        
        # 对比标记 - 使用圆圈而不是对勾
        check_a = Circle(
            radius=0.15,
            color=self.COLOR_POSITIVE,
            stroke_width=3
        ).next_to(formula_right[0][0], UP, buff=0.15)
        
        check_b = Circle(
            radius=0.15,
            color=self.COLOR_POSITIVE,
            stroke_width=3
        ).next_to(formula_right[0][2], UP, buff=0.15)
        
        self.play(
            Create(check_a),
            Create(check_b),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_left),
            FadeOut(formula_right),
            FadeOut(bracket_box),
            FadeOut(arrow),
            FadeOut(explanation),
            FadeOut(check_a),
            FadeOut(check_b),
            run_time=0.6
        )
    
    def show_rule_negative(self):
        """场景3: 去括号法则 - 负号情况（重点）"""
        # 标题
        title = Text(
            "技巧一：去括号法则（负号）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 6)
        
        subtitle = Text(
            "重点！容易出错！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 左侧公式
        formula_left = MathTex(
            r"-(a+b)",
            font_size=self.FONT_SIZE_FORMULA * 1.3
        ).move_to(UP * 3.5 + LEFT * 2)
        
        self.play(Write(formula_left), run_time=0.8)
        
        # 负号强调（闪烁3次）
        minus_sign = formula_left[0][0]
        
        for _ in range(3):
            self.play(
                Indicate(minus_sign, color=self.COLOR_NEGATIVE, scale_factor=1.5),
                run_time=0.4
            )
            self.wait(0.2)
        
        # 标记括号内的符号
        a_sign = Circle(
            radius=0.2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(formula_left[0][2].get_center() + LEFT * 0.25)  # 在a前面
        
        b_sign = Circle(
            radius=0.2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(formula_left[0][3].get_center() + LEFT * 0.25)  # 在+号位置
        
        self.play(Create(a_sign), Create(b_sign), run_time=0.6)
        
        # 说明即将变号
        warning = Text(
            "注意：符号要改变！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(warning, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 变号箭头动画
        arrow1 = CurvedArrow(
            formula_left[0][2].get_center() + UP * 0.4,
            UP * 3.5 + RIGHT * 1.2,
            color=self.COLOR_NEGATIVE,
            angle=TAU/4
        )
        
        arrow2 = CurvedArrow(
            formula_left[0][3].get_center() + UP * 0.4,
            UP * 3.5 + RIGHT * 2.2,
            color=self.COLOR_NEGATIVE,
            angle=TAU/4
        )
        
        self.play(
            Create(arrow1),
            Create(arrow2),
            FadeOut(a_sign),
            FadeOut(b_sign),
            FadeOut(warning),
            run_time=0.8
        )
        
        # 右侧结果逐项出现
        result_minus_a = MathTex(
            r"-a",
            font_size=self.FONT_SIZE_FORMULA * 1.3,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 3.5 + RIGHT * 1.2)
        
        result_minus_b = MathTex(
            r"-b",
            font_size=self.FONT_SIZE_FORMULA * 1.3,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 3.5 + RIGHT * 2.2)
        
        self.play(Write(result_minus_a), run_time=0.5)
        self.play(Write(result_minus_b), run_time=0.5)
        
        # 组合完整结果
        formula_right = MathTex(
            r"-a-b",
            font_size=self.FONT_SIZE_FORMULA * 1.3
        ).move_to(UP * 3.5 + RIGHT * 2)
        
        self.play(
            ReplacementTransform(VGroup(result_minus_a, result_minus_b), formula_right),
            FadeOut(arrow1),
            FadeOut(arrow2),
            run_time=0.8
        )
        
        # 对比标记
        cross_plus = Cross(
            stroke_color=RED,
            stroke_width=3,
            scale_factor=1.5
        ).move_to(formula_left[0][3].get_center())
        
        self.play(Create(cross_plus), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "括号前是负号\n括号内各项都要变号\n+ 变 -， - 变 +",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.6)
        
        # 强调框
        emphasis_box = SurroundingRectangle(
            explanation,
            color=self.COLOR_NEGATIVE,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(emphasis_box), run_time=0.5)
        self.wait(2.0)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(formula_left),
            FadeOut(formula_right),
            FadeOut(cross_plus),
            FadeOut(explanation),
            FadeOut(emphasis_box),
            run_time=0.6
        )
    
    def show_example_intro(self):
        """场景4: 综合例题呈现"""
        # 例题标题
        title = Text(
            "实战演练",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 原始题目
        self.original_problem = MathTex(
            r"(2x+3) - (x-1)",
            font_size=self.FONT_SIZE_FORMULA * 1.2
        ).move_to(UP * 4)
        
        # 设置颜色
        self.original_problem[0][1:3].set_color(self.COLOR_PRIMARY)   # 2x
        self.original_problem[0][4].set_color(self.COLOR_POSITIVE)    # 3
        self.original_problem[0][8].set_color(self.COLOR_SECONDARY)   # x
        self.original_problem[0][9].set_color(self.COLOR_NEGATIVE)    # -
        self.original_problem[0][10].set_color(self.COLOR_POSITIVE)   # 1
        
        self.play(Write(self.original_problem), run_time=0.8)
        
        # 步骤提示框
        step_title = Text(
            "解题两步走",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 2)
        
        step1 = Text(
            "第一步：去括号",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY - 2,
            color=GRAY_A
        ).move_to(UP * 1.2)
        
        step2 = Text(
            "第二步：合并同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY - 2,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        self.play(
            FadeIn(step_title, shift=UP * 0.2),
            run_time=0.5
        )
        self.play(
            FadeIn(step1, shift=LEFT * 0.3),
            run_time=0.4
        )
        self.play(
            FadeIn(step2, shift=LEFT * 0.3),
            run_time=0.4
        )
        
        self.wait(1.0)
        
        # 清理步骤框，保留题目
        self.play(
            FadeOut(title),
            FadeOut(step_title),
            FadeOut(step1),
            FadeOut(step2),
            run_time=0.5
        )
    
    def show_remove_brackets(self):
        """场景5: 去括号过程演示"""
        # 标题
        step_label = Text(
            "第一步：去括号",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(step_label), run_time=0.6)
        
        # 将原题移到合适位置
        self.play(
            self.original_problem.animate.move_to(UP * 4.5),
            run_time=0.5
        )
        
        # --- 处理第一个括号 (正号) ---
        subtitle1 = Text(
            "括号前是正号 → 符号不变",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY - 2,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(subtitle1), run_time=0.5)
        
        # 高亮第一个括号
        first_bracket = SurroundingRectangle(
            self.original_problem[0][0:5],  # (2x+3)
            color=self.COLOR_POSITIVE,
            buff=0.08
        )
        
        self.play(Create(first_bracket), run_time=0.6)
        self.play(Indicate(first_bracket, scale_factor=1.1), run_time=0.5)
        
        # 显示去括号后的第一部分
        part1 = MathTex(
            r"2x+3",
            font_size=self.FONT_SIZE_FORMULA * 1.2
        ).move_to(UP * 2.5 + LEFT * 2)
        
        part1[0][0:2].set_color(self.COLOR_PRIMARY)  # 2x
        part1[0][3].set_color(self.COLOR_POSITIVE)   # 3
        
        self.play(
            TransformFromCopy(self.original_problem[0][1:5], part1),
            FadeOut(first_bracket),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # --- 处理第二个括号 (负号) ---
        self.play(FadeOut(subtitle1), run_time=0.3)
        
        subtitle2 = Text(
            "括号前是负号 → 符号要变！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY - 2,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(subtitle2), run_time=0.5)
        
        # 高亮第二个括号
        second_bracket = SurroundingRectangle(
            self.original_problem[0][6:11],  # -(x-1)
            color=self.COLOR_NEGATIVE,
            buff=0.08
        )
        
        self.play(Create(second_bracket), run_time=0.6)
        
        # 高亮负号
        minus_circle = Circle(
            radius=0.15,
            color=self.COLOR_NEGATIVE,
            stroke_width=3
        ).move_to(self.original_problem[0][6].get_center())
        
        self.play(Create(minus_circle), run_time=0.4)
        self.play(Indicate(minus_circle, scale_factor=1.3), run_time=0.4)
        
        # 显示变号过程
        change_note = Text(
            "x → -x\n-1 → +1",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_NEGATIVE,
            line_spacing=1.2
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(change_note, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)
        
        # 显示去括号后的第二部分
        part2 = MathTex(
            r"-x+1",
            font_size=self.FONT_SIZE_FORMULA * 1.2
        ).move_to(UP * 2.5 + RIGHT * 0.8)
        
        part2[0][0:2].set_color(self.COLOR_SECONDARY)  # -x
        part2[0][3].set_color(self.COLOR_POSITIVE)     # 1
        
        self.play(
            FadeOut(second_bracket),
            FadeOut(minus_circle),
            FadeOut(change_note),
            run_time=0.4
        )
        
        self.play(Write(part2), run_time=0.8)
        
        # 组合完整结果
        self.wait(0.5)
        
        result_line = MathTex(
            r"= 2x+3-x+1",
            font_size=self.FONT_SIZE_FORMULA * 1.2
        ).move_to(UP * 1.2)
        
        result_line[0][1:3].set_color(self.COLOR_PRIMARY)    # 2x
        result_line[0][4].set_color(self.COLOR_POSITIVE)     # 3
        result_line[0][5:7].set_color(self.COLOR_SECONDARY)  # -x
        result_line[0][8].set_color(self.COLOR_POSITIVE)     # 1
        
        self.play(
            Write(result_line),
            FadeOut(part1),
            FadeOut(part2),
            run_time=0.8
        )
        
        # 保存中间结果供下一场景使用
        self.intermediate_result = result_line
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(step_label),
            FadeOut(subtitle2),
            FadeOut(self.original_problem),
            run_time=0.5
        )
    
    def show_combine_terms(self):
        """场景6: 合并同类项"""
        # 标题
        step_label = Text(
            "第二步：合并同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(step_label), run_time=0.6)
        
        # 将中间结果移到合适位置
        self.play(
            self.intermediate_result.animate.move_to(UP * 4.5),
            run_time=0.5
        )
        
        # 说明同类项
        explanation = Text(
            "同类项：字母和指数相同的项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY - 2,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # --- 合并 x 项 ---
        x_label = Text(
            "含x的项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(x_label), run_time=0.4)
        
        # 下划线标记 x 项
        underline_x1 = Line(
            self.intermediate_result[0][1].get_corner(DL) + DOWN * 0.1,
            self.intermediate_result[0][2].get_corner(DR) + DOWN * 0.1,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        underline_x2 = Line(
            self.intermediate_result[0][5].get_corner(DL) + DOWN * 0.1,
            self.intermediate_result[0][6].get_corner(DR) + DOWN * 0.1,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(
            Create(underline_x1),
            Create(underline_x2),
            run_time=0.6
        )
        
        # 移动并合并
        x_combine = MathTex(
            r"2x-x",
            font_size=self.FONT_SIZE_FORMULA
        ).move_to(UP * 2 + LEFT * 2)
        x_combine.set_color(self.COLOR_PRIMARY)
        
        self.play(
            TransformFromCopy(
                VGroup(self.intermediate_result[0][1:3], self.intermediate_result[0][5:7]),
                x_combine
            ),
            run_time=0.8
        )
        
        # 显示计算结果
        x_result = MathTex(
            r"= x",
            font_size=self.FONT_SIZE_FORMULA
        ).next_to(x_combine, RIGHT, buff=0.3)
        x_result.set_color(self.COLOR_PRIMARY)
        
        self.play(Write(x_result), run_time=0.6)
        self.wait(0.5)
        
        # --- 合并常数项 ---
        self.play(
            FadeOut(x_label),
            FadeOut(underline_x1),
            FadeOut(underline_x2),
            FadeOut(x_combine),
            FadeOut(x_result),
            run_time=0.4
        )
        
        const_label = Text(
            "常数项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(const_label), run_time=0.4)
        
        # 下划线标记常数项
        underline_c1 = Line(
            self.intermediate_result[0][4].get_corner(DL) + DOWN * 0.1,
            self.intermediate_result[0][4].get_corner(DR) + DOWN * 0.1,
            color=self.COLOR_POSITIVE,
            stroke_width=3
        )
        
        underline_c2 = Line(
            self.intermediate_result[0][8].get_corner(DL) + DOWN * 0.1,
            self.intermediate_result[0][8].get_corner(DR) + DOWN * 0.1,
            color=self.COLOR_POSITIVE,
            stroke_width=3
        )
        
        self.play(
            Create(underline_c1),
            Create(underline_c2),
            run_time=0.6
        )
        
        # 移动并合并
        const_combine = MathTex(
            r"3+1",
            font_size=self.FONT_SIZE_FORMULA
        ).move_to(UP * 2 + LEFT * 2)
        const_combine.set_color(self.COLOR_POSITIVE)
        
        self.play(
            TransformFromCopy(
                VGroup(self.intermediate_result[0][4], self.intermediate_result[0][8]),
                const_combine
            ),
            run_time=0.8
        )
        
        # 显示计算结果
        const_result = MathTex(
            r"= 4",
            font_size=self.FONT_SIZE_FORMULA
        ).next_to(const_combine, RIGHT, buff=0.3)
        const_result.set_color(self.COLOR_POSITIVE)
        
        self.play(Write(const_result), run_time=0.6)
        self.wait(0.5)
        
        # --- 显示最终结果 ---
        self.play(
            FadeOut(explanation),
            FadeOut(const_label),
            FadeOut(underline_c1),
            FadeOut(underline_c2),
            FadeOut(const_combine),
            FadeOut(const_result),
            run_time=0.4
        )
        
        final_label = Text(
            "最终答案",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(final_label), run_time=0.5)
        
        # 最终结果
        self.final_answer = MathTex(
            r"= x + 4",
            font_size=self.FONT_SIZE_FORMULA * 1.4
        ).move_to(UP * 1.5)
        
        self.final_answer[0][1].set_color(self.COLOR_PRIMARY)    # x
        self.final_answer[0][3].set_color(self.COLOR_POSITIVE)   # 4
        
        self.play(Write(self.final_answer), run_time=0.8)
        
        # 强调框
        answer_box = SurroundingRectangle(
            self.final_answer,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.15
        )
        
        self.play(Create(answer_box), run_time=0.6)
        self.play(Flash(self.final_answer, color=YELLOW, flash_radius=0.5), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step_label),
            FadeOut(final_label),
            FadeOut(self.intermediate_result),
            FadeOut(self.final_answer),
            FadeOut(answer_box),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 总结与片尾"""
        # 总结标题
        summary_title = Text(
            "整式加减两步走",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 步骤卡片1
        card1_title = Text(
            "① 去括号",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 3.5)
        
        card1_content = Text(
            "正号：符号不变\n负号：符号改变",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A,
            line_spacing=1.3
        ).move_to(UP * 2.5)
        
        card1_box = SurroundingRectangle(
            VGroup(card1_title, card1_content),
            color=self.COLOR_NEGATIVE,
            buff=0.3,
            corner_radius=0.15
        )
        
        card1 = VGroup(card1_box, card1_title, card1_content)
        
        self.play(
            FadeIn(card1_box),
            Write(card1_title),
            run_time=0.6
        )
        self.play(FadeIn(card1_content, shift=UP * 0.2), run_time=0.5)
        
        self.wait(0.8)
        
        # 步骤卡片2
        card2_title = Text(
            "② 合并同类项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 0.5)
        
        card2_content = Text(
            "字母和指数相同\n系数相加减",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 0.5)
        
        card2_box = SurroundingRectangle(
            VGroup(card2_title, card2_content),
            color=self.COLOR_PRIMARY,
            buff=0.3,
            corner_radius=0.15
        )
        
        card2 = VGroup(card2_box, card2_title, card2_content)
        
        self.play(
            FadeIn(card2_box),
            Write(card2_title),
            run_time=0.6
        )
        self.play(FadeIn(card2_content, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 要点闪烁
        self.play(
            Indicate(card1, scale_factor=1.05),
            Indicate(card2, scale_factor=1.05),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 淡出卡片
        self.play(
            FadeOut(summary_title),
            FadeOut(card1),
            FadeOut(card2),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 1)
        
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
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰符号动画
        symbols = VGroup(
            MathTex(r"+", font_size=40, color=self.COLOR_POSITIVE).shift(LEFT * 3 + DOWN * 2),
            MathTex(r"-", font_size=40, color=self.COLOR_NEGATIVE).shift(RIGHT * 3 + DOWN * 2),
            MathTex(r"x", font_size=40, color=self.COLOR_PRIMARY).shift(LEFT * 3 + DOWN * 3),
            MathTex(r"=", font_size=40, color=WHITE).shift(RIGHT * 3 + DOWN * 3)
        )
        
        for symbol in symbols:
            self.play(FadeIn(symbol, scale=0.5), run_time=0.2)
        
        self.play(
            *[Rotate(symbol, angle=PI/2, run_time=1.0) for symbol in symbols]
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 渲染命令:
# manim -pql polynomial_addition_subtraction.py PolynomialAdditionSubtraction  # 快速预览
# manim -qh polynomial_addition_subtraction.py PolynomialAdditionSubtraction   # 高质量渲染
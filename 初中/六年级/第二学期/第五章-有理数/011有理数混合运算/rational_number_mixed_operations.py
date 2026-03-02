"""
有理数混合运算 - Rational Number Mixed Operations Animation
使用 Manim 创建的中学数学教学视频

内容: 有理数混合运算的顺序与括号优先级
目标观众: 六年级学生
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


class RationalNumberMixedOperations(Scene):
    """
    有理数混合运算教学动画场景
    
    场景顺序:
    1. 开场引入
    2. 运算顺序法则
    3. 示例1 - 只有加减
    4. 示例2 - 先乘除后加减
    5. 示例3 - 带乘方
    6. 示例4 - 小括号优先
    7. 示例5 - 多层括号
    8. 常见错误
    9. 总结 - 运算口诀
    10. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_POWER = "#9b59b6"         # 紫色 - 乘方
        self.COLOR_MULTIPLY = "#3498db"      # 蓝色 - 乘除
        self.COLOR_ADD = "#2ecc71"           # 绿色 - 加减
        self.COLOR_BRACKET_SMALL = "#e74c3c" # 红色 - 小括号 ()
        self.COLOR_BRACKET_MID = "#f39c12"   # 橙色 - 中括号 []
        self.COLOR_BRACKET_BIG = "#1abc9c"   # 青色 - 大括号 {}
        self.COLOR_RESULT = YELLOW           # 黄色 - 结果
        self.COLOR_ERROR = "#e74c3c"         # 红色 - 错误
        self.COLOR_STEP = GRAY_A             # 灰色 - 步骤说明
        
        # 字体大小配置
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_FORMULA = 32
        
        # 执行动画序列
        self.show_opening()
        self.show_operation_order()
        self.show_example_add_subtract()
        self.show_example_multiply_divide()
        self.show_example_with_power()
        self.show_example_with_brackets()
        self.show_example_nested_brackets()
        self.show_common_errors()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场引入"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = MathTex(
            r"3 + 2 \times 5^2 = ?",
            font_size=self.FONT_FORMULA + 8
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=1.2)
        self.wait(0.3)
        
        # 错误答案闪现
        wrong_answers = VGroup(
            MathTex(r"= 125?", color=self.COLOR_ERROR, font_size=28).move_to(UP * 4.5 + LEFT * 2),
            MathTex(r"= 100?", color=self.COLOR_ERROR, font_size=28).move_to(UP * 4.5),
            MathTex(r"= 55?", color=self.COLOR_ERROR, font_size=28).move_to(UP * 4.5 + RIGHT * 2)
        )
        
        for ans in wrong_answers:
            self.play(FadeIn(ans, scale=0.8), run_time=0.3)
        
        # 副标题
        subtitle = Text(
            "运算顺序很重要!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_RESULT
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(wrong_answers),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_operation_order(self):
        """场景2: 运算顺序法则"""
        # 标题
        title = Text(
            "运算顺序",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 法则卡片 - 第一级：乘方
        power_card = VGroup(
            Text("第一级", font="Noto Sans CJK SC", font_size=24, color=WHITE, weight=BOLD),
            Text("乘方", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_POWER),
            MathTex(r"a^n", font_size=24, color=self.COLOR_POWER)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        self.play(FadeIn(power_card, shift=UP * 0.3), run_time=0.8)
        
        # 法则卡片 - 第二级：乘除
        multiply_card = VGroup(
            Text("第二级", font="Noto Sans CJK SC", font_size=24, color=WHITE, weight=BOLD),
            Text("乘除", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_MULTIPLY),
            MathTex(r"\times, \div", font_size=24, color=self.COLOR_MULTIPLY)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)
        
        self.play(FadeIn(multiply_card, shift=UP * 0.3), run_time=0.8)
        
        # 法则卡片 - 第三级：加减
        add_card = VGroup(
            Text("第三级", font="Noto Sans CJK SC", font_size=24, color=WHITE, weight=BOLD),
            Text("加减", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_ADD),
            MathTex(r"+, -", font_size=24, color=self.COLOR_ADD)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1)
        
        self.play(FadeIn(add_card, shift=UP * 0.3), run_time=0.8)
        
        # 优先级箭头
        arrow1 = Arrow(power_card.get_bottom(), multiply_card.get_top(), color=YELLOW, stroke_width=4)
        arrow2 = Arrow(multiply_card.get_bottom(), add_card.get_top(), color=YELLOW, stroke_width=4)
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), run_time=0.8)
        
        # 括号规则
        bracket_rule = VGroup(
            Text("特殊规则", font="Noto Sans CJK SC", font_size=26, color=YELLOW, weight=BOLD),
            Text("括号优先!", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_BRACKET_SMALL)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 0.5)
        
        bracket_order = MathTex(
            r"( ) \rightarrow [ ] \rightarrow \{ \}",
            font_size=28
        ).move_to(DOWN * 1.8)
        bracket_order[0][0:3].set_color(self.COLOR_BRACKET_SMALL)
        bracket_order[0][4:7].set_color(self.COLOR_BRACKET_MID)
        bracket_order[0][8:11].set_color(self.COLOR_BRACKET_BIG)
        
        self.play(FadeIn(bracket_rule), run_time=0.6)
        self.play(Write(bracket_order), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(power_card),
            FadeOut(multiply_card),
            FadeOut(add_card),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(bracket_rule),
            FadeOut(bracket_order),
            run_time=0.6
        )
    
    def show_example_add_subtract(self):
        """场景3: 示例1 - 只有加减"""
        # 标题
        title = Text(
            "只有加减：从左到右",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ADD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula = MathTex(
            r"5 - 3 + 2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4)
        
        self.play(Write(formula), run_time=0.6)
        self.wait(0.4)
        
        # 步骤1: 高亮 5-3
        step1_rect = SurroundingRectangle(
            VGroup(formula[0][0:3]),
            color=self.COLOR_ADD,
            buff=0.1
        )
        step1_text = Text(
            "① 先算 5-3",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_STEP
        ).move_to(UP * 2.5)
        
        self.play(Create(step1_rect), FadeIn(step1_text), run_time=0.6)
        self.wait(0.4)
        
        # 计算结果1
        formula_step1 = MathTex(
            r"2 + 2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4)
        
        self.play(
            FadeOut(step1_rect),
            TransformMatchingTex(formula, formula_step1),
            FadeOut(step1_text),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 步骤2: 高亮 2+2
        step2_rect = SurroundingRectangle(
            formula_step1,
            color=self.COLOR_ADD,
            buff=0.1
        )
        step2_text = Text(
            "② 再算 2+2",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_STEP
        ).move_to(UP * 2.5)
        
        self.play(Create(step2_rect), FadeIn(step2_text), run_time=0.6)
        self.wait(0.4)
        
        # 最终结果
        result = MathTex(
            r"= 4",
            font_size=self.FONT_FORMULA + 4,
            color=self.COLOR_RESULT
        ).move_to(UP * 4)
        
        self.play(
            FadeOut(step2_rect),
            FadeOut(step2_text),
            Transform(formula_step1, result),
            run_time=0.8
        )
        self.play(Flash(result, color=self.COLOR_RESULT, flash_radius=0.5), run_time=0.4)
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_step1),
            run_time=0.5
        )
    
    def show_example_multiply_divide(self):
        """场景4: 示例2 - 先乘除后加减"""
        # 标题
        title = Text(
            "先乘除，后加减",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=YELLOW
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula = MathTex(
            r"3", r"+", r"2", r"\times", r"4", r"-", r"6", r"\div", r"2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 颜色编码
        formula[0].set_color(self.COLOR_ADD)  # 3
        formula[1].set_color(self.COLOR_ADD)  # +
        formula[2:5].set_color(self.COLOR_MULTIPLY)  # 2×4
        formula[5].set_color(self.COLOR_ADD)  # -
        formula[6:9].set_color(self.COLOR_MULTIPLY)  # 6÷2
        
        hint = Text(
            "先算乘除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_MULTIPLY
        ).move_to(UP * 3.2)
        
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(0.5)
        
        # 步骤1: 2×4
        step1_rect = SurroundingRectangle(
            VGroup(formula[2:5]),
            color=self.COLOR_MULTIPLY,
            buff=0.1
        )
        
        self.play(Create(step1_rect), run_time=0.6)
        self.wait(0.4)
        
        formula_step1 = MathTex(
            r"3 + 8 - 6 \div 2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(step1_rect),
            TransformMatchingTex(formula, formula_step1),
            run_time=0.8
        )
        
        # 步骤2: 6÷2
        step2_rect = SurroundingRectangle(
            VGroup(formula_step1[0][6:11]),
            color=self.COLOR_MULTIPLY,
            buff=0.1
        )
        
        self.play(Create(step2_rect), run_time=0.6)
        self.wait(0.4)
        
        formula_step2 = MathTex(
            r"3 + 8 - 3",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(step2_rect),
            FadeOut(hint),
            TransformMatchingTex(formula_step1, formula_step2),
            run_time=0.8
        )
        
        # 步骤3: 加减运算
        hint2 = Text(
            "再算加减",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_ADD
        ).move_to(UP * 3.2)
        
        self.play(FadeIn(hint2), run_time=0.4)
        self.wait(0.3)
        
        result = MathTex(
            r"= 8",
            font_size=self.FONT_FORMULA + 4,
            color=self.COLOR_RESULT
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(hint2),
            Transform(formula_step2, result),
            run_time=0.8
        )
        self.play(Flash(result, color=self.COLOR_RESULT, flash_radius=0.5), run_time=0.4)
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_step2),
            run_time=0.5
        )
    
    def show_example_with_power(self):
        """场景5: 示例3 - 带乘方"""
        # 标题
        title = Text(
            "先算乘方",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_POWER
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula = MathTex(
            r"3", r"+", r"2", r"\times", r"5", r"^2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 颜色 + 序号标注
        formula[0].set_color(self.COLOR_ADD)
        formula[1].set_color(self.COLOR_ADD)
        formula[2:4].set_color(self.COLOR_MULTIPLY)
        formula[4:6].set_color(self.COLOR_POWER)
        
        labels = VGroup(
            Text("①", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_POWER).next_to(formula[5], UR, buff=0.1),
            Text("②", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_MULTIPLY).next_to(formula[3], UP, buff=0.1),
            Text("③", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ADD).next_to(formula[1], UP, buff=0.1)
        )
        
        self.play(FadeIn(labels), run_time=0.6)
        self.wait(0.4)
        
        # 步骤1: 5²
        step1_rect = SurroundingRectangle(
            VGroup(formula[4:6]),
            color=self.COLOR_POWER,
            buff=0.1
        )
        
        self.play(Create(step1_rect), run_time=0.6)
        self.wait(0.4)
        
        formula_step1 = MathTex(
            r"3 + 2 \times 25",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(step1_rect),
            FadeOut(labels),
            TransformMatchingTex(formula, formula_step1),
            run_time=0.8
        )
        
        # 步骤2: 2×25
        step2_rect = SurroundingRectangle(
            VGroup(formula_step1[0][2:9]),
            color=self.COLOR_MULTIPLY,
            buff=0.1
        )
        
        self.play(Create(step2_rect), run_time=0.6)
        self.wait(0.4)
        
        formula_step2 = MathTex(
            r"3 + 50",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(step2_rect),
            TransformMatchingTex(formula_step1, formula_step2),
            run_time=0.8
        )
        
        # 步骤3: 3+50
        step3_rect = SurroundingRectangle(
            formula_step2,
            color=self.COLOR_ADD,
            buff=0.1
        )
        
        self.play(Create(step3_rect), run_time=0.6)
        self.wait(0.4)
        
        result = MathTex(
            r"= 53",
            font_size=self.FONT_FORMULA + 4,
            color=self.COLOR_RESULT
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(step3_rect),
            Transform(formula_step2, result),
            run_time=0.8
        )
        self.play(Flash(result, color=self.COLOR_RESULT, flash_radius=0.5), run_time=0.4)
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_step2),
            run_time=0.5
        )
    
    def show_example_with_brackets(self):
        """场景6: 示例4 - 小括号优先"""
        # 标题
        title = Text(
            "括号优先",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_BRACKET_SMALL
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula = MathTex(
            r"(", r"3", r"+", r"2", r")", r"\times", r"4",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 高亮括号
        bracket_rect = SurroundingRectangle(
            VGroup(formula[0:5]),
            color=self.COLOR_BRACKET_SMALL,
            buff=0.1
        )
        
        hint = Text(
            "先算括号内",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_BRACKET_SMALL
        ).move_to(UP * 3)
        
        self.play(Create(bracket_rect), FadeIn(hint), run_time=0.6)
        self.wait(0.5)
        
        # 计算括号内
        formula_step1 = MathTex(
            r"5 \times 4",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(bracket_rect),
            TransformMatchingTex(formula, formula_step1),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 计算乘法
        result = MathTex(
            r"= 20",
            font_size=self.FONT_FORMULA + 4,
            color=self.COLOR_RESULT
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(hint),
            Transform(formula_step1, result),
            run_time=0.8
        )
        self.play(Flash(result, color=self.COLOR_RESULT, flash_radius=0.5), run_time=0.4)
        self.wait(0.5)
        
        # 对比：无括号的情况
        compare = MathTex(
            r"3 + 2 \times 4 = 11",
            font_size=self.FONT_BODY
        ).move_to(UP * 2.5)
        
        compare_text = Text(
            "对比（无括号）:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).next_to(compare, UP, buff=0.2)
        
        self.play(FadeIn(compare_text), FadeIn(compare), run_time=0.6)
        
        # 结果对比
        self.play(
            Indicate(result, scale_factor=1.2, color=YELLOW),
            Indicate(compare[0][8:10], scale_factor=1.2, color=YELLOW),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_step1),
            FadeOut(compare),
            FadeOut(compare_text),
            run_time=0.5
        )
    
    def show_example_nested_brackets(self):
        """场景7: 示例5 - 多层括号"""
        # 标题
        title = Text(
            "多层括号：由内到外",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=YELLOW
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula = MathTex(
            r"\{", r"2", r"\times", r"[", r"3", r"+", r"(", r"4", r"-", r"1", r")", r"]", r"\}",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 括号颜色编码
        formula[0].set_color(self.COLOR_BRACKET_BIG)   # {
        formula[12].set_color(self.COLOR_BRACKET_BIG)  # }
        formula[3].set_color(self.COLOR_BRACKET_MID)   # [
        formula[11].set_color(self.COLOR_BRACKET_MID)  # ]
        formula[6].set_color(self.COLOR_BRACKET_SMALL) # (
        formula[10].set_color(self.COLOR_BRACKET_SMALL) # )
        
        self.wait(0.5)
        
        # 步骤1: 小括号 (4-1)
        step1_rect = SurroundingRectangle(
            VGroup(formula[6:11]),
            color=self.COLOR_BRACKET_SMALL,
            buff=0.1
        )
        step1_text = Text(
            "① 最内层: (4-1)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_BRACKET_SMALL
        ).move_to(UP * 2.8)
        
        self.play(Create(step1_rect), FadeIn(step1_text), run_time=0.6)
        self.wait(0.4)
        
        formula_step1 = MathTex(
            r"\{ 2 \times [ 3 + 3 ] \}",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula_step1[0][0].set_color(self.COLOR_BRACKET_BIG)
        formula_step1[0][7].set_color(self.COLOR_BRACKET_BIG)
        formula_step1[0][4].set_color(self.COLOR_BRACKET_MID)
        formula_step1[0][6].set_color(self.COLOR_BRACKET_MID)
        
        self.play(
            FadeOut(step1_rect),
            FadeOut(step1_text),
            TransformMatchingTex(formula, formula_step1),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 步骤2: 中括号 [3+3]
        step2_rect = SurroundingRectangle(
            VGroup(formula_step1[0][4:7]),
            color=self.COLOR_BRACKET_MID,
            buff=0.1
        )
        step2_text = Text(
            "② 中间层: [3+3]",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_BRACKET_MID
        ).move_to(UP * 2.8)
        
        self.play(Create(step2_rect), FadeIn(step2_text), run_time=0.6)
        self.wait(0.4)
        
        formula_step2 = MathTex(
            r"\{ 2 \times 6 \}",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        formula_step2[0][0].set_color(self.COLOR_BRACKET_BIG)
        formula_step2[0][4].set_color(self.COLOR_BRACKET_BIG)
        
        self.play(
            FadeOut(step2_rect),
            FadeOut(step2_text),
            TransformMatchingTex(formula_step1, formula_step2),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 步骤3: 大括号 {2×6}
        step3_rect = SurroundingRectangle(
            VGroup(formula_step2[0][0:5]),
            color=self.COLOR_BRACKET_BIG,
            buff=0.1
        )
        step3_text = Text(
            "③ 最外层: {2×6}",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_BRACKET_BIG
        ).move_to(UP * 2.8)
        
        self.play(Create(step3_rect), FadeIn(step3_text), run_time=0.6)
        self.wait(0.4)
        
        result = MathTex(
            r"= 12",
            font_size=self.FONT_FORMULA + 4,
            color=self.COLOR_RESULT
        ).move_to(UP * 4.5)
        
        self.play(
            FadeOut(step3_rect),
            FadeOut(step3_text),
            Transform(formula_step2, result),
            run_time=0.8
        )
        self.play(Flash(result, color=self.COLOR_RESULT, flash_radius=0.5), run_time=0.4)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_step2),
            run_time=0.5
        )
    
    def show_common_errors(self):
        """场景8: 常见错误"""
        # 标题
        title = Text(
            "常见错误",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ERROR
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 错误1: 忽略括号
        error1 = VGroup(
            MathTex(r"(3+2)\times 4 = 3+2\times 4", font_size=26, color=self.COLOR_ERROR),
            Text("✗ 忽略括号", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ERROR)
        ).arrange(DOWN, buff=0.2).move_to(UP * 4)
        
        self.play(Write(error1), run_time=0.8)
        self.wait(0.7)
        
        # 错误2: 运算顺序错误
        error2 = VGroup(
            MathTex(r"3+2\times 5 = 5\times 5", font_size=26, color=self.COLOR_ERROR),
            Text("✗ 先算了加法", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ERROR)
        ).arrange(DOWN, buff=0.2).move_to(UP * 1.5)
        
        self.play(Write(error2), run_time=0.8)
        self.wait(0.7)
        
        # 错误3: 负号处理错误
        error3 = VGroup(
            MathTex(r"-3^2 = 9", font_size=26, color=self.COLOR_ERROR),
            Text("✗ 应该是 -9", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ERROR)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1)
        
        self.play(Write(error3), run_time=0.8)
        self.wait(0.7)
        
        # 叉号标记
        crosses = VGroup(
            Text("✗", font_size=60, color=RED).move_to(error1.get_left() + LEFT * 0.8),
            Text("✗", font_size=60, color=RED).move_to(error2.get_left() + LEFT * 0.8),
            Text("✗", font_size=60, color=RED).move_to(error3.get_left() + LEFT * 0.8)
        )
        
        self.play(FadeIn(crosses, scale=1.5), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(error1),
            FadeOut(error2),
            FadeOut(error3),
            FadeOut(crosses),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景9: 总结 - 运算口诀"""
        # 大标题
        title = Text(
            "运算口诀",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE + 4,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)
        
        # 口诀1
        line1 = Text(
            "括号优先第一位",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_BRACKET_SMALL
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(line1, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 口诀2
        line2 = Text(
            "乘方紧随其后来",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_POWER
        ).move_to(UP * 3)
        
        self.play(FadeIn(line2, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 口诀3
        line3 = Text(
            "乘除运算第三级",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_MULTIPLY
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(line3, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 口诀4
        line4 = Text(
            "加减最后算出来",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ADD
        ).move_to(ORIGIN)
        
        self.play(FadeIn(line4, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 顺序图示
        arrows = VGroup(
            Arrow(line1.get_bottom(), line2.get_top(), color=YELLOW, stroke_width=4),
            Arrow(line2.get_bottom(), line3.get_top(), color=YELLOW, stroke_width=4),
            Arrow(line3.get_bottom(), line4.get_top(), color=YELLOW, stroke_width=4)
        )
        
        self.play(Create(arrows), run_time=1.0)
        
        # 重点提示
        highlight = Text(
            "记住顺序，不出错!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=YELLOW
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3),
            FadeOut(line4),
            FadeOut(arrows),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景10: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 运算符号装饰
        symbols = VGroup(
            MathTex(r"+", font_size=40, color=self.COLOR_ADD).move_to(DOWN * 2 + LEFT * 2.5),
            MathTex(r"-", font_size=40, color=self.COLOR_ADD).move_to(DOWN * 2 + LEFT * 1),
            MathTex(r"\times", font_size=40, color=self.COLOR_MULTIPLY).move_to(DOWN * 2 + RIGHT * 0.5),
            MathTex(r"\div", font_size=40, color=self.COLOR_MULTIPLY).move_to(DOWN * 2 + RIGHT * 2),
            MathTex(r"^n", font_size=40, color=self.COLOR_POWER).move_to(DOWN * 3.5)
        )
        
        self.play(*[FadeIn(sym, scale=0.5) for sym in symbols], run_time=0.6)
        
        # 符号旋转
        self.play(
            Rotate(symbols, angle=PI/2, run_time=1.5),
            symbols.animate.set_opacity(0.7)
        )
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql rational_number_mixed_operations.py RationalNumberMixedOperations  # 快速预览
# manim -qh rational_number_mixed_operations.py RationalNumberMixedOperations   # 高质量 1080p
# manim -qk rational_number_mixed_operations.py RationalNumberMixedOperations   # 4K质量
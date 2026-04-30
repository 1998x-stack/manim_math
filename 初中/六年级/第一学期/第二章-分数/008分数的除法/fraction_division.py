"""
分数除法教学动画 - Fraction Division Animation
使用 Manim 创建的六年级数学教学视频

内容: 倒数概念、分数除法法则、除法转乘法
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


class FractionDivision(Scene):
    """
    分数除法教学动画场景
    
    场景顺序:
    1. 开场钩子 (0-5s)
    2. 倒数概念 (5-18s)
    3. 分数除法法则 (18-32s)
    4. 实例演示1 - 2/3 ÷ 1/2 (32-45s)
    5. 实例演示2 - 3/4 ÷ 2/5 (45-57s)
    6. 总结 (57-70s)
    7. 片尾关注 (70-75s)
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主分数
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 除数
        self.COLOR_RECIPROCAL = "#9b59b6"     # 紫色 - 倒数
        self.COLOR_RESULT = "#2ecc71"         # 绿色 - 结果
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        self.COLOR_DIVISION = "#f39c12"       # 橙色 - 除号
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_reciprocal_concept()
        self.scene_3_division_rule()
        self.scene_4_example_1()
        self.scene_5_example_2()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def create_fraction_display(self, numerator, denominator, color=WHITE, font_size=36):
        """创建分数显示（分子/分母结构）"""
        num_text = MathTex(str(numerator), font_size=font_size, color=color)
        line = Line(LEFT * 0.35, RIGHT * 0.35, color=color, stroke_width=2.5)
        den_text = MathTex(str(denominator), font_size=font_size, color=color)
        
        fraction = VGroup(num_text, line, den_text).arrange(DOWN, buff=0.18)
        return fraction
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = MathTex(
            r"\frac{2}{3} \div \frac{1}{2} = ?",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 问号闪烁
        big_question = Text("?", font_size=80, color=RED).move_to(UP * 3)
        
        for _ in range(3):
            self.play(Flash(big_question, color=RED, flash_radius=0.6), run_time=0.3)
        
        # 困惑文字
        confused_text = Text(
            "分数除法好难？",
            font="PingFang SC",
            font_size=32,
            color=RED
        ).move_to(UP * 1)
        
        self.play(FadeIn(confused_text, shift=UP * 0.3), run_time=0.5)
        
        # 提示
        hint_text = Text(
            "其实很简单!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(Write(hint_text), run_time=0.5)
        
        # 标题
        title = Text(
            "分数的除法",
            font="PingFang SC",
            font_size=48,
            color=GOLD
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(big_question),
            FadeOut(confused_text),
            FadeOut(hint_text),
            FadeOut(title),
            run_time=0.5
        )
    
    def scene_2_reciprocal_concept(self):
        """场景2: 倒数概念 (5-18秒)"""
        # 标题
        title = Text(
            "什么是倒数？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_RECIPROCAL
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 定义
        definition = Text(
            "乘积为1的两个数互为倒数",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(definition), run_time=0.6)
        
        # 示例1: 2 × 1/2 = 1
        example1_text = Text(
            "例如:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.2 + LEFT * 3)
        
        num_2 = MathTex("2", font_size=36, color=self.COLOR_PRIMARY).move_to(UP * 3.5 + LEFT * 1.5)
        times_1 = MathTex(r"\times", font_size=32, color=WHITE).move_to(UP * 3.5 + LEFT * 0.5)
        frac_half = self.create_fraction_display(1, 2, self.COLOR_SECONDARY, 32)
        frac_half.move_to(UP * 3.5 + RIGHT * 0.5)
        equals_1 = MathTex("=", font_size=32, color=WHITE).move_to(UP * 3.5 + RIGHT * 1.5)
        one_1 = MathTex("1", font_size=36, color=self.COLOR_RESULT).move_to(UP * 3.5 + RIGHT * 2.2)
        
        self.play(FadeIn(example1_text), run_time=0.3)
        self.play(
            Write(num_2),
            FadeIn(times_1),
            Write(frac_half),
            run_time=0.8
        )
        self.play(FadeIn(equals_1), Write(one_1), run_time=0.5)
        
        # 高亮"互为倒数"
        reciprocal_text = Text(
            "所以 2 和 1/2 互为倒数",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(reciprocal_text), run_time=0.4)
        self.wait(0.5)
        
        # 清理示例1
        self.play(
            FadeOut(example1_text),
            FadeOut(num_2),
            FadeOut(times_1),
            FadeOut(frac_half),
            FadeOut(equals_1),
            FadeOut(one_1),
            FadeOut(reciprocal_text),
            run_time=0.4
        )
        
        # 示例2: 如何求倒数
        example2_title = Text(
            "如何求倒数？",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        self.play(Write(example2_title), run_time=0.5)
        
        # 3/4 的倒数
        question_text = Text(
            "3/4 的倒数是多少？",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3)
        
        self.play(FadeIn(question_text), run_time=0.4)
        
        # 原分数
        original_frac = self.create_fraction_display(3, 4, self.COLOR_PRIMARY, 40)
        original_frac.move_to(UP * 1.5 + LEFT * 2)
        
        self.play(Write(original_frac), run_time=0.6)
        
        # 交换动画
        arrow = Arrow(
            UP * 1.5 + LEFT * 0.8,
            UP * 1.5 + RIGHT * 0.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        swap_text = Text(
            "分子分母交换",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow),
            FadeIn(swap_text),
            run_time=0.6
        )
        
        # 倒数结果
        reciprocal_frac = self.create_fraction_display(4, 3, self.COLOR_RECIPROCAL, 40)
        reciprocal_frac.move_to(UP * 1.5 + RIGHT * 2)
        
        self.play(
            TransformFromCopy(original_frac, reciprocal_frac),
            run_time=1.0
        )
        
        # 验证
        verify_text = Text(
            "验证:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 0.5 + LEFT * 3.5)
        
        # 3/4 × 4/3 = 1
        verify_frac1 = self.create_fraction_display(3, 4, self.COLOR_PRIMARY, 28)
        verify_frac1.move_to(DOWN * 0.5 + LEFT * 2)
        
        verify_times = MathTex(r"\times", font_size=28, color=WHITE).move_to(DOWN * 0.5 + LEFT * 0.8)
        
        verify_frac2 = self.create_fraction_display(4, 3, self.COLOR_RECIPROCAL, 28)
        verify_frac2.move_to(DOWN * 0.5 + RIGHT * 0.4)
        
        verify_equals = MathTex("=", font_size=28, color=WHITE).move_to(DOWN * 0.5 + RIGHT * 1.6)
        
        verify_one = MathTex("1", font_size=32, color=self.COLOR_RESULT).move_to(DOWN * 0.5 + RIGHT * 2.3)
        
        checkmark = MathTex(r"\checkmark", font_size=32, color=GREEN).move_to(DOWN * 0.5 + RIGHT * 3)
        
        self.play(FadeIn(verify_text), run_time=0.3)
        self.play(
            Write(verify_frac1),
            FadeIn(verify_times),
            Write(verify_frac2),
            run_time=0.7
        )
        self.play(
            FadeIn(verify_equals),
            Write(verify_one),
            FadeIn(checkmark),
            run_time=0.6
        )
        
        # 口诀
        mantra = Text(
            "口诀: 分子分母交换位置",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(Write(mantra), run_time=0.8)
        
        # 特例提示
        warning = Text(
            "注意: 0没有倒数!",
            font="PingFang SC",
            font_size=24,
            color=RED
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(warning, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example2_title),
            FadeOut(question_text),
            FadeOut(original_frac),
            FadeOut(arrow),
            FadeOut(swap_text),
            FadeOut(reciprocal_frac),
            FadeOut(verify_text),
            FadeOut(verify_frac1),
            FadeOut(verify_times),
            FadeOut(verify_frac2),
            FadeOut(verify_equals),
            FadeOut(verify_one),
            FadeOut(checkmark),
            FadeOut(mantra),
            FadeOut(warning),
            run_time=0.5
        )
    
    def scene_3_division_rule(self):
        """场景3: 分数除法法则 (18-32秒)"""
        # 标题
        title = Text(
            "分数除法法则",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_DIVISION
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 法则陈述
        rule_text = Text(
            "除以一个数 = 乘以这个数的倒数",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.3)
        
        self.play(FadeIn(rule_text, shift=UP * 0.2), run_time=1.0)
        
        # 公式示例: a/b ÷ c/d
        frac_a_b = self.create_fraction_display("a", "b", self.COLOR_PRIMARY, 36)
        frac_a_b.move_to(UP * 3 + LEFT * 2.5)
        
        division_sign = MathTex(r"\div", font_size=40, color=self.COLOR_DIVISION)
        division_sign.move_to(UP * 3 + LEFT * 1.2)
        
        frac_c_d = self.create_fraction_display("c", "d", self.COLOR_SECONDARY, 36)
        frac_c_d.move_to(UP * 3 + RIGHT * 0)
        
        self.play(
            Write(frac_a_b),
            Write(division_sign),
            Write(frac_c_d),
            run_time=0.6
        )
        
        # 箭头指向除号
        arrow_to_div = Arrow(
            UP * 2 + LEFT * 1.2,
            UP * 2.7 + LEFT * 1.2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow_to_div), run_time=0.3)
        
        # 除号闪烁
        self.play(
            Indicate(division_sign, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            run_time=0.4
        )
        
        # 变换1: ÷ 变成 ×
        times_sign = MathTex(r"\times", font_size=40, color=GREEN)
        times_sign.move_to(division_sign.get_center())
        
        self.play(
            Transform(division_sign, times_sign),
            FadeOut(arrow_to_div),
            run_time=0.8
        )
        
        # 箭头指向 c/d
        arrow_to_frac = Arrow(
            UP * 2 + RIGHT * 0,
            UP * 2.7 + RIGHT * 0,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow_to_frac), run_time=0.3)
        
        # 变换2: c/d 翻转成 d/c
        frac_d_c = self.create_fraction_display("d", "c", self.COLOR_RECIPROCAL, 36)
        frac_d_c.move_to(frac_c_d.get_center())
        
        self.play(
            Transform(frac_c_d, frac_d_c),
            FadeOut(arrow_to_frac),
            run_time=1.0
        )
        
        # 完整公式
        complete_formula = MathTex(
            r"= \frac{a}{b} \times \frac{d}{c}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 0.5)
        
        self.play(Write(complete_formula), run_time=0.6)
        
        # 继续计算
        final_formula = MathTex(
            r"= \frac{a \times d}{b \times c}",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 1.5)
        
        self.play(Write(final_formula), run_time=0.8)
        
        # 强调框
        emphasis_box = SurroundingRectangle(
            VGroup(frac_a_b, division_sign, frac_c_d),
            color=self.COLOR_HIGHLIGHT,
            buff=0.2
        )
        
        self.play(Create(emphasis_box), run_time=0.6)
        
        # 提示
        reminder = Text(
            "记住这个法则!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(reminder, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule_text),
            FadeOut(frac_a_b),
            FadeOut(division_sign),
            FadeOut(frac_c_d),
            FadeOut(complete_formula),
            FadeOut(final_formula),
            FadeOut(emphasis_box),
            FadeOut(reminder),
            run_time=0.5
        )
    
    def scene_4_example_1(self):
        """场景4: 实例演示1 - 2/3 ÷ 1/2 (32-45秒)"""
        # 标题
        title = Text(
            "实例1: 计算 2/3 ÷ 1/2",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 原式
        original_frac1 = self.create_fraction_display(2, 3, self.COLOR_PRIMARY, 36)
        original_frac1.move_to(UP * 5 + LEFT * 1.5)
        
        div_sign = MathTex(r"\div", font_size=36, color=self.COLOR_DIVISION)
        div_sign.move_to(UP * 5 + LEFT * 0.3)
        
        original_frac2 = self.create_fraction_display(1, 2, self.COLOR_SECONDARY, 36)
        original_frac2.move_to(UP * 5 + RIGHT * 0.8)
        
        self.play(
            Write(original_frac1),
            Write(div_sign),
            Write(original_frac2),
            run_time=0.6
        )
        
        # 步骤1: 找倒数
        step1_title = Text(
            "步骤1: 找倒数",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(Write(step1_title), run_time=0.4)
        
        # 框住 1/2
        box_frac2 = SurroundingRectangle(original_frac2, color=self.COLOR_HIGHLIGHT, buff=0.1)
        self.play(Create(box_frac2), run_time=0.3)
        
        # 箭头: 1/2 → 2/1
        reciprocal_arrow = Arrow(
            UP * 2.5 + RIGHT * 0.8,
            UP * 2.5 + RIGHT * 2.5,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        reciprocal_result = self.create_fraction_display(2, 1, self.COLOR_RECIPROCAL, 36)
        reciprocal_result.move_to(UP * 2.5 + RIGHT * 3.2)
        
        self.play(
            GrowArrow(reciprocal_arrow),
            Write(reciprocal_result),
            run_time=0.8
        )
        
        # 步骤2: 变乘法
        step2_title = Text(
            "步骤2: 变乘法",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.8)
        
        self.play(
            FadeOut(box_frac2),
            FadeOut(reciprocal_arrow),
            Write(step2_title),
            run_time=0.4
        )
        
        # 新公式: 2/3 × 2/1
        new_frac1 = self.create_fraction_display(2, 3, self.COLOR_PRIMARY, 36)
        new_frac1.move_to(ORIGIN + LEFT * 1.5)
        
        times_sign = MathTex(r"\times", font_size=36, color=GREEN)
        times_sign.move_to(ORIGIN + LEFT * 0.3)
        
        new_frac2 = self.create_fraction_display(2, 1, self.COLOR_RECIPROCAL, 36)
        new_frac2.move_to(ORIGIN + RIGHT * 0.8)
        
        self.play(
            FadeIn(new_frac1),
            FadeIn(times_sign),
            FadeIn(new_frac2),
            run_time=1.0
        )
        
        # 步骤3: 计算
        step3_title = Text(
            "步骤3: 计算",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(Write(step3_title), run_time=0.4)
        
        # 分子计算
        numerator_calc = MathTex(
            r"2 \times 2 = 4",
            font_size=28,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 3 + LEFT * 1.5)
        
        self.play(Write(numerator_calc), run_time=0.6)
        
        # 分母计算
        denominator_calc = MathTex(
            r"3 \times 1 = 3",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 3 + RIGHT * 1.5)
        
        self.play(Write(denominator_calc), run_time=0.6)
        
        # 结果
        result_frac = self.create_fraction_display(4, 3, self.COLOR_RESULT, 44)
        result_frac.move_to(DOWN * 4.8)
        
        equals_sign = MathTex("=", font_size=40, color=WHITE).next_to(result_frac, LEFT, buff=0.4)
        
        self.play(
            FadeIn(equals_sign),
            Write(result_frac),
            run_time=0.6
        )
        
        # 化简提示（带分数）
        mixed_number = MathTex(
            r"= 1\frac{1}{3}",
            font_size=36,
            color=self.COLOR_RESULT
        ).next_to(result_frac, RIGHT, buff=0.5)
        
        mixed_label = Text(
            "(带分数)",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(mixed_number, DOWN, buff=0.1)
        
        self.play(
            Write(mixed_number),
            FadeIn(mixed_label),
            run_time=0.7
        )
        
        # 高亮结果
        self.play(
            Circumscribe(result_frac, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(original_frac1),
            FadeOut(div_sign),
            FadeOut(original_frac2),
            FadeOut(step1_title),
            FadeOut(reciprocal_result),
            FadeOut(step2_title),
            FadeOut(new_frac1),
            FadeOut(times_sign),
            FadeOut(new_frac2),
            FadeOut(step3_title),
            FadeOut(numerator_calc),
            FadeOut(denominator_calc),
            FadeOut(equals_sign),
            FadeOut(result_frac),
            FadeOut(mixed_number),
            FadeOut(mixed_label),
            run_time=0.5
        )
    
    def scene_5_example_2(self):
        """场景5: 实例演示2 - 3/4 ÷ 2/5 (45-57秒)"""
        # 标题
        title = Text(
            "实例2: 3/4 ÷ 2/5",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 原式
        step1_label = Text(
            "原式:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5 + LEFT * 3.5)
        
        frac1 = self.create_fraction_display(3, 4, self.COLOR_PRIMARY, 32)
        frac1.move_to(UP * 5 + LEFT * 2)
        
        div = MathTex(r"\div", font_size=32, color=self.COLOR_DIVISION)
        div.move_to(UP * 5 + LEFT * 0.8)
        
        frac2 = self.create_fraction_display(2, 5, self.COLOR_SECONDARY, 32)
        frac2.move_to(UP * 5 + RIGHT * 0.3)
        
        self.play(
            FadeIn(step1_label),
            Write(frac1),
            Write(div),
            Write(frac2),
            run_time=0.5
        )
        
        # 找倒数
        step2_label = Text(
            "找倒数:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.5 + LEFT * 3.5)
        
        reciprocal_process = MathTex(
            r"\frac{2}{5} \rightarrow \frac{5}{2}",
            font_size=32,
            color=self.COLOR_RECIPROCAL
        ).move_to(UP * 3.5 + RIGHT * 0.5)
        
        self.play(
            FadeIn(step2_label),
            Write(reciprocal_process),
            run_time=0.8
        )
        
        # 变乘法
        step3_label = Text(
            "变乘法:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2 + LEFT * 3.5)
        
        new_frac1 = self.create_fraction_display(3, 4, self.COLOR_PRIMARY, 32)
        new_frac1.move_to(UP * 2 + LEFT * 1.5)
        
        times = MathTex(r"\times", font_size=32, color=GREEN)
        times.move_to(UP * 2 + LEFT * 0.3)
        
        new_frac2 = self.create_fraction_display(5, 2, self.COLOR_RECIPROCAL, 32)
        new_frac2.move_to(UP * 2 + RIGHT * 0.8)
        
        self.play(
            FadeIn(step3_label),
            Write(new_frac1),
            FadeIn(times),
            Write(new_frac2),
            run_time=0.8
        )
        
        # 计算标注
        calc_label = Text(
            "计算:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.3 + LEFT * 3.5)
        
        calc_process = MathTex(
            r"3 \times 5 = 15, \quad 4 \times 2 = 8",
            font_size=28,
            color=WHITE
        ).move_to(UP * 0.3 + RIGHT * 0.5)
        
        self.play(
            FadeIn(calc_label),
            Write(calc_process),
            run_time=1.0
        )
        
        # 结果
        result_label = Text(
            "结果:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1.5 + LEFT * 3.5)
        
        result = self.create_fraction_display(15, 8, self.COLOR_RESULT, 40)
        result.move_to(DOWN * 1.5 + RIGHT * 0.5)
        
        self.play(
            FadeIn(result_label),
            Write(result),
            run_time=0.6
        )
        
        # 检查
        check_text = Text(
            "已是最简分数 ✓",
            font="PingFang SC",
            font_size=22,
            color=GREEN
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(check_text), run_time=0.7)
        
        # 完整流程展示
        summary_text = Text(
            "完整流程:",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        
        full_process = MathTex(
            r"\frac{3}{4} \div \frac{2}{5} = \frac{3}{4} \times \frac{5}{2} = \frac{15}{8}",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 5.2)
        
        self.play(
            FadeIn(summary_text),
            Write(full_process),
            run_time=0.8
        )
        
        # 强调
        emphasis = Text(
            "就这么简单!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(emphasis, shift=UP * 0.2, scale=1.1), run_time=0.6)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step1_label),
            FadeOut(frac1),
            FadeOut(div),
            FadeOut(frac2),
            FadeOut(step2_label),
            FadeOut(reciprocal_process),
            FadeOut(step3_label),
            FadeOut(new_frac1),
            FadeOut(times),
            FadeOut(new_frac2),
            FadeOut(calc_label),
            FadeOut(calc_process),
            FadeOut(result_label),
            FadeOut(result),
            FadeOut(check_text),
            FadeOut(summary_text),
            FadeOut(full_process),
            FadeOut(emphasis),
            run_time=0.5
        )
    
    def scene_6_summary(self):
        """场景6: 总结 (57-70秒)"""
        # 标题
        title = Text(
            "分数除法三步走",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 创建总结卡片
        # 卡片1: 找倒数
        card1 = self.create_summary_card(
            "步骤1: 找倒数",
            "分子分母交换位置",
            r"\frac{a}{b} \rightarrow \frac{b}{a}",
            self.COLOR_RECIPROCAL,
            UP * 4
        )
        
        # 卡片2: 变乘法
        card2 = self.create_summary_card(
            "步骤2: 变乘法",
            "除号变乘号",
            r"\div \text{ => } \times",
            self.COLOR_DIVISION,
            UP * 1.5
        )
        
        # 卡片3: 计算约分
        card3 = self.create_summary_card(
            "步骤3: 计算",
            "相乘后化简",
            r"\frac{a \times d}{b \times c}",
            self.COLOR_RESULT,
            DOWN * 1
        )
        
        # 卡片依次滑入
        self.play(card1.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.2)
        self.play(card2.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.2)
        self.play(card3.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.8)
        
        # 口诀
        mantra = Text(
            "除法变乘法，倒数来帮忙!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.8)
        
        self.play(Write(mantra), run_time=0.8)
        
        # 特别提醒
        reminder = Text(
            "特别提醒: 0没有倒数!",
            font="PingFang SC",
            font_size=24,
            color=RED
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(reminder, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(mantra),
            FadeOut(reminder),
            run_time=0.5
        )
    
    def create_summary_card(self, title_text, content_text, formula_text, color, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content = Text(
            content_text,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 公式
        formula = MathTex(
            formula_text,
            font_size=22,
            color=color
        )
        
        # 组合
        text_group = VGroup(title, content, formula).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        card = VGroup(icon, text_group).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def scene_7_outro(self):
        """场景7: 片尾关注 (70-75秒)"""
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(Write(follow_text), run_time=0.6)
        
        # 装饰动画 - 除号和分数符号
        decorations = VGroup()
        
        # 除号
        div_deco = MathTex(r"\div", font_size=40, color=self.COLOR_DIVISION)
        div_deco.move_to(LEFT * 3 + DOWN * 2.5)
        decorations.add(div_deco)
        
        # 乘号
        times_deco = MathTex(r"\times", font_size=40, color=GREEN)
        times_deco.move_to(RIGHT * 3 + DOWN * 2.5)
        decorations.add(times_deco)
        
        # 分数1
        frac_deco1 = self.create_fraction_display(1, 2, self.COLOR_PRIMARY, 30)
        frac_deco1.move_to(LEFT * 3 + UP * 3.5)
        decorations.add(frac_deco1)
        
        # 分数2
        frac_deco2 = self.create_fraction_display(3, 4, self.COLOR_SECONDARY, 30)
        frac_deco2.move_to(RIGHT * 3 + UP * 3.5)
        decorations.add(frac_deco2)
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.6
        )
        
        # 旋转动画
        self.play(
            Rotate(decorations, angle=PI/3, run_time=1.2)
        )
        
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql fraction_division.py FractionDivision  # 快速预览
# manim -qh fraction_division.py FractionDivision   # 高质量渲染
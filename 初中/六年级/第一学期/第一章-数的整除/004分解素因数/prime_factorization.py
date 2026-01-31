"""
分解素因数 - Prime Factorization Animation
使用 Manim 创建的六年级数学教学视频

内容: 分解素因数的定义、短除法
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


class PrimeFactorization(Scene):
    """
    分解素因数教学动画场景
    
    场景顺序:
    1. 开场引入
    2. 素数与合数复习
    3. 分解素因数定义
    4. 短除法演示 - 30
    5. 短除法演示 - 60
    6. 总结与巩固
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要概念
        self.COLOR_PRIME = "#e74c3c"         # 红色 - 素数
        self.COLOR_COMPOSITE = "#2ecc71"     # 绿色 - 合数
        self.COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮
        self.COLOR_DIVISOR = "#9b59b6"       # 紫色 - 除数
        self.COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_FORMULA = 32
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_prime_composite()
        self.show_definition()
        self.show_division_30()
        self.show_division_60()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场引入 (4-5秒)"""
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
            "30可以写成哪些数相乘？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 展示几种分解
        examples = VGroup(
            MathTex(r"1 \times 30", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"2 \times 15", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"3 \times 10", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"5 \times 6", font_size=self.FONT_BODY, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 2.5 + LEFT * 1)
        
        self.play(FadeIn(examples, lag_ratio=0.3), run_time=1.2)
        
        # 特殊的素数分解
        special = MathTex(
            r"2 \times 3 \times 5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_PRIME
        ).move_to(UP * 0.5)
        
        special_label = Text(
            "最特殊！全是素数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).next_to(special, DOWN, buff=0.5)
        
        self.play(FadeIn(special, scale=1.2), run_time=0.6)
        self.play(Flash(special, color=self.COLOR_PRIME), run_time=0.5)
        self.play(FadeIn(special_label, shift=UP * 0.2), run_time=0.5)
        
        # 引导文字
        hint = Text(
            "这就是分解素因数！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(examples),
            FadeOut(special),
            FadeOut(special_label),
            FadeOut(hint),
            run_time=0.5
        )
    
    def show_prime_composite(self):
        """场景2: 素数与合数复习 (8-10秒)"""
        # 标题
        title = Text(
            "素数与合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # 素数定义
        prime_title = Text(
            "素数：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIME
        ).move_to(UP * 3.5 + LEFT * 3)
        
        prime_def = Text(
            "只有1和它本身两个因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(prime_title, RIGHT, buff=0.3)
        
        prime_group = VGroup(prime_title, prime_def)
        
        self.play(Write(prime_group), run_time=1.0)
        
        # 素数例子
        prime_examples = MathTex(
            r"2, 3, 5, 7, 11, 13, 17, 19...",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIME
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(prime_examples, shift=LEFT * 0.2), run_time=0.8)
        
        # 合数定义
        composite_title = Text(
            "合数：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_COMPOSITE
        ).move_to(UP * 0.5 + LEFT * 3)
        
        composite_def = Text(
            "除了1和它本身还有其他因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(composite_title, RIGHT, buff=0.3)
        
        composite_group = VGroup(composite_title, composite_def)
        
        self.play(Write(composite_group), run_time=1.0)
        
        # 合数例子
        composite_examples = MathTex(
            r"4, 6, 8, 9, 10, 12, 14, 15...",
            font_size=self.FONT_BODY,
            color=self.COLOR_COMPOSITE
        ).move_to(DOWN * 0.7)
        
        self.play(FadeIn(composite_examples, shift=LEFT * 0.2), run_time=0.8)
        
        # 注意
        note = Text(
            "注意：1既不是素数也不是合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(prime_group),
            FadeOut(prime_examples),
            FadeOut(composite_group),
            FadeOut(composite_examples),
            FadeOut(note),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景3: 分解素因数定义 (10-12秒)"""
        # 标题
        title = Text(
            "分解素因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "将一个合数表示为若干个素数乘积的形式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4)
        
        definition_box = SurroundingRectangle(
            definition,
            color=self.COLOR_PRIMARY,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(definition), run_time=1.2)
        self.play(Create(definition_box), run_time=0.5)
        
        # 示例
        example_label = Text(
            "例如：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2 + LEFT * 3)
        
        example = MathTex(
            r"30 = 2 \times 3 \times 5",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).next_to(example_label, RIGHT, buff=0.3)
        
        example_group = VGroup(example_label, example)
        
        self.play(FadeIn(example_group, shift=UP * 0.2), run_time=0.6)
        
        # 标注
        arrow1 = Arrow(
            start=example[0][0:2].get_bottom(),
            end=example[0][0:2].get_bottom() + DOWN * 0.8,
            color=self.COLOR_COMPOSITE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        label1 = Text(
            "合数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_COMPOSITE
        ).next_to(arrow1, DOWN, buff=0.05)
        
        self.play(GrowArrow(arrow1), FadeIn(label1), run_time=0.5)
        
        # 标注素数
        prime_numbers = [4, 8, 12]  # 索引位置可能需要调整
        arrows = VGroup()
        labels = VGroup()
        
        for i, idx in enumerate(prime_numbers):
            arrow = Arrow(
                start=example.get_bottom() + RIGHT * (i - 1) * 0.8,
                end=example.get_bottom() + RIGHT * (i - 1) * 0.8 + DOWN * 1.2,
                color=self.COLOR_PRIME,
                buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.2
            )
            label = Text(
                "素数",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SMALL,
                color=self.COLOR_PRIME
            ).next_to(arrow, DOWN, buff=0.05)
            
            arrows.add(arrow)
            labels.add(label)
        
        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            *[FadeIn(label) for label in labels],
            run_time=0.8
        )
        
        # 强调
        emphasis = Text(
            "每个合数的分解结果是唯一的（算术基本定理）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(emphasis, shift=UP * 0.2), run_time=0.8)
        self.play(Flash(emphasis, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(definition_box),
            FadeOut(example_group),
            FadeOut(arrow1),
            FadeOut(label1),
            FadeOut(arrows),
            FadeOut(labels),
            FadeOut(emphasis),
            run_time=0.5
        )
    
    def show_division_30(self):
        """场景4: 短除法演示 - 30 (15-18秒)"""
        # 标题
        title = Text(
            "短除法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_DIVISOR
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "从最小的素数开始除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 创建短除法表格
        # 第一步：2 | 30
        number_30 = MathTex(r"30", font_size=self.FONT_FORMULA, color=WHITE).move_to(UP * 3 + RIGHT * 0.5)
        
        self.play(Write(number_30), run_time=0.6)
        
        divisor_2 = MathTex(r"2", font_size=self.FONT_FORMULA, color=self.COLOR_DIVISOR).move_to(UP * 3 + LEFT * 1)
        vline_1 = Line(UP * 3.3 + LEFT * 0.5, UP * 2.7 + LEFT * 0.5, color=self.COLOR_AUXILIARY)
        hline_1 = Line(UP * 2.7 + LEFT * 1.5, UP * 2.7 + RIGHT * 1.5, color=self.COLOR_AUXILIARY)
        
        explain_1 = Text(
            "30能被2整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(UP * 3 + RIGHT * 3)
        
        self.play(
            FadeIn(divisor_2, shift=RIGHT * 0.3),
            Create(vline_1),
            run_time=0.5
        )
        self.play(Create(hline_1), FadeIn(explain_1), run_time=0.4)
        
        quotient_15 = MathTex(r"15", font_size=self.FONT_FORMULA, color=WHITE).move_to(UP * 2.2 + RIGHT * 0.5)
        self.play(FadeIn(quotient_15, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(explain_1), run_time=0.3)
        
        # 第二步：3 | 15
        divisor_3 = MathTex(r"3", font_size=self.FONT_FORMULA, color=self.COLOR_DIVISOR).move_to(UP * 1.5 + LEFT * 1)
        vline_2 = Line(UP * 1.8 + LEFT * 0.5, UP * 1.2 + LEFT * 0.5, color=self.COLOR_AUXILIARY)
        hline_2 = Line(UP * 1.2 + LEFT * 1.5, UP * 1.2 + RIGHT * 1.5, color=self.COLOR_AUXILIARY)
        
        explain_2 = Text(
            "15能被3整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(UP * 1.5 + RIGHT * 3)
        
        self.play(
            FadeIn(divisor_3, shift=RIGHT * 0.3),
            Create(vline_2),
            run_time=0.5
        )
        self.play(Create(hline_2), FadeIn(explain_2), run_time=0.4)
        
        quotient_5 = MathTex(r"5", font_size=self.FONT_FORMULA, color=WHITE).move_to(UP * 0.7 + RIGHT * 0.5)
        self.play(FadeIn(quotient_5, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(explain_2), run_time=0.3)
        
        # 第三步：5 | 5
        divisor_5 = MathTex(r"5", font_size=self.FONT_FORMULA, color=self.COLOR_DIVISOR).move_to(ORIGIN + LEFT * 1)
        vline_3 = Line(UP * 0.3 + LEFT * 0.5, DOWN * 0.3 + LEFT * 0.5, color=self.COLOR_AUXILIARY)
        hline_3 = Line(DOWN * 0.3 + LEFT * 1.5, DOWN * 0.3 + RIGHT * 1.5, color=self.COLOR_AUXILIARY)
        
        explain_3 = Text(
            "5能被5整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(ORIGIN + RIGHT * 3)
        
        self.play(
            FadeIn(divisor_5, shift=RIGHT * 0.3),
            Create(vline_3),
            run_time=0.5
        )
        self.play(Create(hline_3), FadeIn(explain_3), run_time=0.4)
        
        quotient_1 = MathTex(r"1", font_size=self.FONT_FORMULA, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 0.8 + RIGHT * 0.5)
        
        finish_text = Text(
            "得到1，分解完成！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8 + RIGHT * 3)
        
        self.play(FadeIn(quotient_1, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeOut(explain_3), FadeIn(finish_text), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(finish_text), run_time=0.3)
        
        # 框选所有除数
        divisors_group = VGroup(divisor_2, divisor_3, divisor_5)
        box = SurroundingRectangle(
            divisors_group,
            color=self.COLOR_DIVISOR,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(box), run_time=0.5)
        
        # 写结果
        result_label = Text(
            "结果：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 2.5 + LEFT * 2.5)
        
        result = MathTex(
            r"30 = 2 \times 3 \times 5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).next_to(result_label, RIGHT, buff=0.3)
        
        result_group = VGroup(result_label, result)
        
        self.play(FadeIn(result_group, shift=UP * 0.2), run_time=0.8)
        
        # 验证
        verification = Text(
            "验证：2×3×5 = 6×5 = 30 ✓",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3.8)
        
        self.play(FadeIn(verification), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(number_30),
            FadeOut(divisors_group),
            FadeOut(VGroup(vline_1, vline_2, vline_3)),
            FadeOut(VGroup(hline_1, hline_2, hline_3)),
            FadeOut(VGroup(quotient_15, quotient_5, quotient_1)),
            FadeOut(box),
            FadeOut(result_group),
            FadeOut(verification),
            run_time=0.5
        )
    
    def show_division_60(self):
        """场景5: 短除法演示 - 60 (12-15秒)"""
        # 标题
        title = Text(
            "再来一个例子：60",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_DIVISOR
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 快速短除法 - 不详细解释
        division_steps = [
            (60, 2, 30),
            (30, 2, 15),
            (15, 3, 5),
            (5, 5, 1),
        ]
        
        y_pos = 3.5
        y_step = -1.2
        
        divisors = VGroup()
        
        for i, (num, divisor, quotient) in enumerate(division_steps):
            current_y = y_pos + i * y_step
            
            if i == 0:
                number = MathTex(str(num), font_size=self.FONT_FORMULA, color=WHITE).move_to(UP * current_y + RIGHT * 0.5)
                self.play(Write(number), run_time=0.4)
            
            div = MathTex(str(divisor), font_size=self.FONT_FORMULA, color=self.COLOR_DIVISOR).move_to(UP * current_y + LEFT * 1)
            vline = Line(UP * (current_y + 0.3) + LEFT * 0.5, UP * (current_y - 0.3) + LEFT * 0.5, color=self.COLOR_AUXILIARY)
            hline = Line(UP * (current_y - 0.3) + LEFT * 1.5, UP * (current_y - 0.3) + RIGHT * 1.5, color=self.COLOR_AUXILIARY)
            
            divisors.add(div)
            
            self.play(
                FadeIn(div, shift=RIGHT * 0.2),
                Create(vline),
                Create(hline),
                run_time=0.4
            )
            
            if quotient != 1:
                quot = MathTex(str(quotient), font_size=self.FONT_FORMULA, color=WHITE).move_to(UP * (current_y - 0.8) + RIGHT * 0.5)
                self.play(FadeIn(quot, shift=DOWN * 0.2), run_time=0.3)
            else:
                quot = MathTex(str(quotient), font_size=self.FONT_FORMULA, color=self.COLOR_HIGHLIGHT).move_to(UP * (current_y - 0.8) + RIGHT * 0.5)
                self.play(FadeIn(quot, shift=DOWN * 0.2), run_time=0.3)
        
        self.wait(0.5)
        
        # 结果
        result1_label = Text(
            "结果：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 2.5 + LEFT * 2.5)
        
        result1 = MathTex(
            r"60 = 2 \times 2 \times 3 \times 5",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(result1_label, RIGHT, buff=0.3)
        
        result1_group = VGroup(result1_label, result1)
        
        self.play(FadeIn(result1_group, shift=UP * 0.2), run_time=0.8)
        
        # 指数形式
        result2 = MathTex(
            r"60 = 2^2 \times 3 \times 5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.8)
        
        explanation = Text(
            "（相同素因数用指数表示）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(result2, DOWN, buff=0.3)
        
        self.play(FadeIn(result2, scale=1.1), run_time=0.8)
        self.play(Flash(result2, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info],
            run_time=0.5
        )
    
    def show_summary(self):
        """场景6: 总结与巩固 (10-12秒)"""
        # 标题
        title = Text(
            "短除法步骤",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # 步骤
        step1_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_DIVISOR,
            fill_opacity=1,
            stroke_width=0
        ).move_to(UP * 3 + LEFT * 3.5)
        
        step1_text = Text(
            "① 从最小的素数2开始",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(step1_icon, RIGHT, buff=0.2)
        
        step1 = VGroup(step1_icon, step1_text)
        step1.shift(LEFT * 10)
        
        step2_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_DIVISOR,
            fill_opacity=1,
            stroke_width=0
        ).move_to(UP * 1.5 + LEFT * 3.5)
        
        step2_text = Text(
            "② 能整除就除，除数写左边",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(step2_icon, RIGHT, buff=0.2)
        
        step2 = VGroup(step2_icon, step2_text)
        step2.shift(LEFT * 10)
        
        step3_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_DIVISOR,
            fill_opacity=1,
            stroke_width=0
        ).move_to(ORIGIN + LEFT * 3.5)
        
        step3_text = Text(
            "③ 商写下面，继续除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(step3_icon, RIGHT, buff=0.2)
        
        step3 = VGroup(step3_icon, step3_text)
        step3.shift(LEFT * 10)
        
        step4_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_DIVISOR,
            fill_opacity=1,
            stroke_width=0
        ).move_to(DOWN * 1.5 + LEFT * 3.5)
        
        step4_text = Text(
            "④ 直到商为1",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(step4_icon, RIGHT, buff=0.2)
        
        step4 = VGroup(step4_icon, step4_text)
        step4.shift(LEFT * 10)
        
        # 步骤依次滑入
        self.play(step1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(step2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(step3.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(step4.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.8)
        
        # 注意事项
        notes = Text(
            "提示：每个合数的分解结果是唯一的！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(notes, shift=UP * 0.2), run_time=0.6)
        self.play(Flash(notes, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 装饰
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
            FadeOut(title),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(notes),
            FadeOut(follow_text),
            FadeOut(stars),
            FadeOut(self.author_info),
            run_time=1.0
        )


# 运行命令:
# manim -pql prime_factorization.py PrimeFactorization  # 快速预览
# manim -qh prime_factorization.py PrimeFactorization   # 高质量渲染
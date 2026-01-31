"""
公倍数与最小公倍数教学动画 - Common Multiples and LCM
使用 Manim 创建的六年级数学教学视频

内容: 倍数、公倍数、最小公倍数的概念和求法
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


class CommonMultiplesLCM(Scene):
    """
    公倍数与最小公倍数教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 倍数概念回顾
    3. 数轴可视化
    4. 公倍数定义
    5. 最小公倍数
    6. 短除法求LCM
    7. 重要关系式与结尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 数字4
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 数字6
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 公倍数
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_LCM = GOLD               # 金色 - 最小公倍数
        self.COLOR_TABLE_HEADER = "#2c3e50" # 深灰 - 表头
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_NUMBER_LARGE = 48
        self.FONT_NUMBER_NORMAL = 28
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_multiples_concept()
        self.show_numberline_visualization()
        self.show_common_multiples_definition()
        self.show_lcm_concept()
        self.show_division_method()
        self.show_relationship_and_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "4和6的共同倍数是什么?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 数字4出现
        num_4 = Text(
            "4",
            font="Noto Sans CJK SC",
            font_size=self.FONT_NUMBER_LARGE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(LEFT * 2 + UP * 3)
        
        # 数字6出现
        num_6 = Text(
            "6",
            font="Noto Sans CJK SC",
            font_size=self.FONT_NUMBER_LARGE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(RIGHT * 2 + UP * 3)
        
        self.play(FadeIn(num_4, scale=0.5), run_time=0.3)
        self.wait(0.2)
        self.play(FadeIn(num_6, scale=0.5), run_time=0.3)
        
        # 问号
        question_mark = Text(
            "?",
            font_size=self.FONT_NUMBER_LARGE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(
            FadeIn(question_mark, scale=1.2),
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.4
        )
        
        # 数字移动到顶部
        self.play(
            num_4.animate.scale(0.6).move_to(LEFT * 2.5 + UP * 6),
            num_6.animate.scale(0.6).move_to(RIGHT * 2.5 + UP * 6),
            run_time=0.5
        )
        
        self.num_4_ref = num_4
        self.num_6_ref = num_6
    
    def show_multiples_concept(self):
        """场景2: 倍数概念回顾"""
        # 标题
        title = Text(
            "回顾: 什么是倍数?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 4的倍数
        label_4 = Text(
            "4的倍数:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 3 + UP * 3)
        
        multiples_4_list = [4, 8, 12, 16, 20, 24, 28, 32, 36]
        multiples_4 = VGroup(*[
            Text(
                str(m),
                font="Noto Sans CJK SC",
                font_size=self.FONT_NUMBER_NORMAL,
                color=self.COLOR_PRIMARY
            )
            for m in multiples_4_list
        ]).arrange(RIGHT, buff=0.3).next_to(label_4, DOWN, buff=0.3)
        
        self.play(FadeIn(label_4), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(m, shift=DOWN * 0.2) for m in multiples_4], lag_ratio=0.1),
            run_time=2.0
        )
        
        # 6的倍数
        label_6 = Text(
            "6的倍数:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(LEFT * 3 + UP * 0.5)
        
        multiples_6_list = [6, 12, 18, 24, 30, 36, 42, 48, 54]
        multiples_6 = VGroup(*[
            Text(
                str(m),
                font="Noto Sans CJK SC",
                font_size=self.FONT_NUMBER_NORMAL,
                color=self.COLOR_SECONDARY
            )
            for m in multiples_6_list
        ]).arrange(RIGHT, buff=0.3).next_to(label_6, DOWN, buff=0.3)
        
        self.play(FadeIn(label_6), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(m, shift=DOWN * 0.2) for m in multiples_6], lag_ratio=0.1),
            run_time=2.0
        )
        
        # 说明文字
        explanation = Text(
            "倍数 = 原数 × 整数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 高亮公倍数
        common_indices_4 = [2, 5, 8]  # 12, 24, 36
        common_indices_6 = [1, 3, 5]  # 12, 24, 36
        
        self.play(
            *[multiples_4[i].animate.set_color(self.COLOR_HIGHLIGHT).scale(1.2) for i in common_indices_4],
            *[multiples_6[i].animate.set_color(self.COLOR_HIGHLIGHT).scale(1.2) for i in common_indices_6],
            run_time=0.8
        )
        
        hint = Text(
            "注意: 有些数重复出现!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(label_4),
            FadeOut(label_6),
            FadeOut(multiples_4),
            FadeOut(multiples_6),
            FadeOut(explanation),
            FadeOut(hint),
            run_time=0.6
        )
    
    def show_numberline_visualization(self):
        """场景3: 数轴可视化"""
        # 创建数轴
        numberline = NumberLine(
            x_range=[0, 36, 6],
            length=8,
            include_numbers=True,
            font_size=20,
            label_direction=DOWN,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(Create(numberline), run_time=1.0)
        
        # 标记4的倍数
        label_4 = Text(
            "4的倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4)
        
        self.play(FadeIn(label_4), run_time=0.3)
        
        multiples_4 = [4, 8, 12, 16, 20, 24, 28, 32, 36]
        dots_4 = VGroup(*[
            Dot(numberline.n2p(m), radius=0.1, color=self.COLOR_PRIMARY)
            for m in multiples_4
        ])
        
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in dots_4], lag_ratio=0.15),
            run_time=2.0
        )
        
        # 标记6的倍数
        label_6 = Text(
            "6的倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 3.3)
        
        self.play(
            FadeOut(label_4),
            FadeIn(label_6),
            run_time=0.3
        )
        
        multiples_6 = [6, 12, 18, 24, 30, 36]
        dots_6 = VGroup(*[
            Dot(numberline.n2p(m), radius=0.1, color=self.COLOR_SECONDARY)
            for m in multiples_6
        ])
        
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in dots_6], lag_ratio=0.15),
            run_time=1.5
        )
        
        self.play(FadeOut(label_6), run_time=0.3)
        
        # 高亮公倍数
        common_multiples = [12, 24, 36]
        
        # 找到对应的点
        common_dots_4 = [dots_4[multiples_4.index(m)] for m in common_multiples]
        common_dots_6 = [dots_6[multiples_6.index(m)] for m in common_multiples]
        
        self.play(
            *[dot.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.5) for dot in common_dots_4],
            *[FadeOut(dot) for dot in common_dots_6],  # 隐藏重复的点
            run_time=1.0
        )
        
        # 圈出公倍数
        circles = VGroup(*[
            Circle(radius=0.25, color=self.COLOR_HIGHLIGHT, stroke_width=3)
            .move_to(numberline.n2p(m))
            for m in common_multiples
        ])
        
        self.play(
            LaggedStart(*[Create(circle) for circle in circles], lag_ratio=0.2),
            run_time=1.0
        )
        
        # 标注
        annotation = Text(
            "这些就是公倍数!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(annotation, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(numberline),
            FadeOut(dots_4),
            FadeOut(circles),
            FadeOut(annotation),
            run_time=0.6
        )
    
    def show_common_multiples_definition(self):
        """场景4: 公倍数定义"""
        # 定义框
        definition_box = RoundedRectangle(
            width=7,
            height=2,
            corner_radius=0.2,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(UP * 4)
        
        definition_text = VGroup(
            Text(
                "公倍数",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SUBTITLE,
                color=WHITE,
                weight=BOLD
            ),
            Text(
                "两个或多个数共有的倍数",
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=self.COLOR_AUXILIARY
            )
        ).arrange(DOWN, buff=0.3).move_to(definition_box.get_center())
        
        self.play(
            FadeIn(definition_box, scale=0.9),
            Write(definition_text),
            run_time=1.0
        )
        
        # 示例
        example_title = Text(
            "4和6的公倍数:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # 公倍数列表
        common_multiples_list = [12, 24, 36, 48, 60]
        common_multiples = VGroup(*[
            Text(
                str(m),
                font="Noto Sans CJK SC",
                font_size=self.FONT_NUMBER_NORMAL,
                color=self.COLOR_HIGHLIGHT
            )
            for m in common_multiples_list
        ]).arrange(RIGHT, buff=0.5).move_to(UP * 0.5)
        
        # 添加逗号
        commas = VGroup(*[
            Text(",", font_size=self.FONT_NUMBER_NORMAL, color=WHITE)
            .next_to(common_multiples[i], RIGHT, buff=0.1)
            for i in range(len(common_multiples) - 1)
        ])
        
        # 添加省略号
        ellipsis = Text("...", font_size=self.FONT_NUMBER_NORMAL, color=WHITE)\
            .next_to(common_multiples[-1], RIGHT, buff=0.2)
        
        self.play(
            LaggedStart(*[FadeIn(m, shift=DOWN * 0.2) for m in common_multiples], lag_ratio=0.15),
            run_time=1.5
        )
        self.play(
            *[FadeIn(c) for c in commas],
            FadeIn(ellipsis),
            run_time=0.3
        )
        
        # 高亮提示
        self.play(
            Indicate(common_multiples, scale_factor=1.2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(definition_box),
            FadeOut(definition_text),
            FadeOut(example_title),
            FadeOut(common_multiples),
            FadeOut(commas),
            FadeOut(ellipsis),
            run_time=0.6
        )
    
    def show_lcm_concept(self):
        """场景5: 最小公倍数"""
        # 标题
        title = Text(
            "最小公倍数 (LCM)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_LCM
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Least Common Multiple",
            font_size=self.FONT_SMALL,
            color=self.COLOR_AUXILIARY
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=1.0)
        
        # 公倍数序列
        sequence_numbers = [12, 24, 36, 48, 60]
        sequence = VGroup(*[
            Text(
                str(n),
                font="Noto Sans CJK SC",
                font_size=self.FONT_NUMBER_NORMAL,
                color=WHITE
            )
            for n in sequence_numbers
        ]).arrange(RIGHT, buff=0.6).move_to(UP * 3)
        
        self.play(Create(sequence), run_time=1.5)
        
        # 箭头指向12
        arrow = Arrow(
            start=sequence[0].get_top() + UP * 0.5,
            end=sequence[0].get_top() + UP * 0.1,
            color=self.COLOR_LCM,
            buff=0,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.3
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 12放大变金色
        self.play(
            sequence[0].animate.scale(2).set_color(self.COLOR_LCM),
            run_time=1.0
        )
        
        self.play(
            Flash(sequence[0], color=self.COLOR_LCM, flash_radius=0.8, num_lines=12),
            run_time=0.5
        )
        
        # "最小"文字
        min_text = Text(
            "最小的公倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_LCM
        ).next_to(sequence[0], DOWN, buff=0.8)
        
        self.play(FadeIn(min_text, scale=1.2), run_time=0.5)
        self.wait(1.5)
        
        # 公式
        formula = MathTex(
            r"\text{lcm}(4, 6) = 12",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 1)
        
        # 修复中文问题
        formula_text = VGroup(
            Text("lcm", font_size=40, color=WHITE),
            Text("(4, 6) = 12", font_size=40, color=WHITE)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1)
        
        self.play(
            formula_text.animate.shift(UP * 10).shift(DOWN * 10),
            run_time=1.5
        )
        
        self.play(
            Indicate(formula_text, scale_factor=1.2),
            run_time=0.8
        )
        
        # 说明
        explanation = Text(
            "LCM是最重要的公倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(sequence),
            FadeOut(arrow),
            FadeOut(min_text),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 保留公式但缩小移到角落
        self.play(
            formula_text.animate.scale(0.5).move_to(RIGHT * 3 + UP * 6),
            run_time=0.4
        )
        self.formula_ref = formula_text
    
    def show_division_method(self):
        """场景6: 短除法求LCM"""
        # 标题
        title = Text(
            "如何求最小公倍数?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        method_name = Text(
            "方法: 短除法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(method_name), run_time=0.8)
        
        # 创建短除法示意图
        # 第一行: 2 | 4  6
        divisor_1 = Text("2", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_HIGHLIGHT)\
            .move_to(LEFT * 3 + UP * 3)
        
        line_1 = Line(
            LEFT * 2.5 + UP * 3.2,
            LEFT * 2.5 + UP * 2,
            color=WHITE,
            stroke_width=3
        )
        
        line_2 = Line(
            LEFT * 2.5 + UP * 3,
            RIGHT * 2 + UP * 3,
            color=WHITE,
            stroke_width=3
        )
        
        num_4_top = Text("4", font_size=self.FONT_NUMBER_NORMAL, color=WHITE)\
            .move_to(LEFT * 1 + UP * 3.5)
        num_6_top = Text("6", font_size=self.FONT_NUMBER_NORMAL, color=WHITE)\
            .move_to(RIGHT * 0.5 + UP * 3.5)
        
        self.play(
            Write(num_4_top),
            Write(num_6_top),
            run_time=0.5
        )
        
        self.play(
            Create(line_1),
            Create(line_2),
            run_time=0.5
        )
        
        self.play(FadeIn(divisor_1), run_time=0.5)
        
        # 第一次除法结果
        result_2 = Text("2", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_PRIMARY)\
            .move_to(LEFT * 1 + UP * 2.2)
        result_3 = Text("3", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_PRIMARY)\
            .move_to(RIGHT * 0.5 + UP * 2.2)
        
        arrow_4 = Arrow(
            num_4_top.get_bottom(),
            result_2.get_top(),
            buff=0.1,
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2
        )
        
        arrow_6 = Arrow(
            num_6_top.get_bottom(),
            result_3.get_top(),
            buff=0.1,
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(
            GrowArrow(arrow_4),
            GrowArrow(arrow_6),
            run_time=0.5
        )
        
        self.play(
            TransformFromCopy(num_4_top, result_2),
            TransformFromCopy(num_6_top, result_3),
            run_time=1.0
        )
        
        # 说明
        hint_1 = Text(
            "4÷2=2, 6÷2=3",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(RIGHT * 2.5 + UP * 2.5)
        
        self.play(FadeIn(hint_1), run_time=0.5)
        self.wait(1.0)
        
        self.play(
            FadeOut(arrow_4),
            FadeOut(arrow_6),
            FadeOut(hint_1),
            run_time=0.3
        )
        
        # 检查能否继续除
        hint_2 = Text(
            "2和3互质, 不能再除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(RIGHT * 2 + UP * 1.8)
        
        self.play(FadeIn(hint_2), run_time=0.5)
        self.wait(1.0)
        
        # 计算LCM
        calculation = VGroup(
            Text("LCM = 2", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=WHITE),
            Text("×", font_size=self.FONT_BODY, color=WHITE),
            Text("2", font_size=self.FONT_BODY, color=self.COLOR_PRIMARY),
            Text("×", font_size=self.FONT_BODY, color=WHITE),
            Text("3", font_size=self.FONT_BODY, color=self.COLOR_PRIMARY)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)
        
        self.play(Write(calculation), run_time=1.5)
        
        # 等号和结果
        equals = Text("=", font_size=self.FONT_BODY, color=WHITE)\
            .next_to(calculation, RIGHT, buff=0.3)
        
        result = Text(
            "12",
            font="Noto Sans CJK SC",
            font_size=self.FONT_NUMBER_LARGE,
            color=self.COLOR_LCM,
            weight=BOLD
        ).next_to(equals, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(equals),
            TransformFromCopy(calculation, result),
            run_time=1.0
        )
        
        # 答案高亮
        self.play(
            result.animate.scale(1.3),
            Flash(result, color=self.COLOR_LCM, flash_radius=1.0),
            run_time=0.9
        )
        
        # 验证说明
        verification = Text(
            "✓ 所有除数和最后的商相乘",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(verification), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(method_name),
            FadeOut(divisor_1),
            FadeOut(line_1),
            FadeOut(line_2),
            FadeOut(num_4_top),
            FadeOut(num_6_top),
            FadeOut(result_2),
            FadeOut(result_3),
            FadeOut(hint_2),
            FadeOut(calculation),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(verification),
            run_time=0.6
        )
    
    def show_relationship_and_outro(self):
        """场景7: 重要关系式与结尾"""
        # 标题
        title = Text(
            "重要关系",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=1.0)
        
        # 公式 - 分行显示避免LaTeX中文问题
        formula_line1 = VGroup(
            Text("a", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("×", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("b", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("=", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("gcd(a,b)", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_PRIMARY),
            Text("×", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("lcm(a,b)", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3)
        
        self.play(FadeIn(formula_line1, shift=UP * 0.3), run_time=1.0)
        
        # 实例验证
        example_title = Text(
            "验证: a=4, b=6",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # 左边
        left_side = VGroup(
            Text("4", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("×", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("6", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("=", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("24", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_LCM, weight=BOLD)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)
        
        # 右边
        right_side = VGroup(
            Text("2", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_PRIMARY),
            Text("×", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("12", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_SECONDARY),
            Text("=", font_size=self.FONT_NUMBER_NORMAL, color=WHITE),
            Text("24", font_size=self.FONT_NUMBER_NORMAL, color=self.COLOR_LCM, weight=BOLD)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)
        
        gcd_label = Text(
            "(最大公因数)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIMARY
        ).next_to(right_side[0], UP, buff=0.2)
        
        lcm_label = Text(
            "(最小公倍数)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).next_to(right_side[2], UP, buff=0.2)
        
        self.play(Write(left_side), run_time=1.5)
        self.play(Write(right_side), FadeIn(gcd_label), FadeIn(lcm_label), run_time=1.5)
        
        # 验证结果
        check_mark = Text(
            "✓ 24 = 24",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 2)
        
        self.play(
            Indicate(left_side[-1]),
            Indicate(right_side[-1]),
            run_time=0.8
        )
        
        self.play(FadeIn(check_mark, scale=1.2), run_time=0.6)
        self.wait(1.5)
        
        # 清理并准备结尾
        self.play(
            FadeOut(title),
            FadeOut(formula_line1),
            FadeOut(example_title),
            FadeOut(left_side),
            FadeOut(right_side),
            FadeOut(gcd_label),
            FadeOut(lcm_label),
            FadeOut(check_mark),
            FadeOut(self.num_4_ref),
            FadeOut(self.num_6_ref),
            FadeOut(self.formula_ref),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1)
        
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
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 关键词标签
        keywords = VGroup(
            Text("#公倍数", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_PRIMARY),
            Text("#LCM", font_size=22, color=self.COLOR_SECONDARY),
            Text("#短除法", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.5)
        
        self.play(
            LaggedStart(*[FadeIn(kw, shift=UP * 0.2) for kw in keywords], lag_ratio=0.2),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(keywords),
            run_time=1.0
        )


# 运行命令:
# manim -pql lcm_animation.py CommonMultiplesLCM  # 快速预览
# manim -qh lcm_animation.py CommonMultiplesLCM   # 高质量渲染 (推荐用于最终输出)
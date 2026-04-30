"""
有理数的减法 - Rational Number Subtraction Animation
使用 Manim 创建的中学数学教学视频

内容: 有理数减法法则及转化为加法的方法
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


class RationalNumberSubtraction(Scene):
    """
    有理数减法教学动画场景
    
    场景顺序:
    1. 开场引入
    2. 核心概念 - 减法转加法
    3. 正数减正数 (情况1: 3-2)
    4. 正数减正数 (情况2: 2-5)
    5. 正数减负数
    6. 负数减正数
    7. 负数减负数
    8. 特殊情况
    9. 总结 - 减法法则
    10. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_POSITIVE = "#2ecc71"      # 绿色 - 正数
        self.COLOR_NEGATIVE = "#e74c3c"      # 红色 - 负数
        self.COLOR_ZERO = "#95a5a6"          # 灰色 - 零
        self.COLOR_RESULT = "#f39c12"        # 橙色 - 结果
        self.COLOR_TRANSFORM = "#9b59b6"     # 紫色 - 转化过程
        self.COLOR_NUMBERLINE = WHITE        # 数轴
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 辅助元素
        
        # 字体大小配置
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_FORMULA = 32
        
        # 数轴配置
        self.UNIT_LENGTH = 0.7
        self.NUMBERLINE_POS = UP * 2
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_core_concept()
        self.show_positive_minus_positive_case1()
        self.show_positive_minus_positive_case2()
        self.show_positive_minus_negative()
        self.show_negative_minus_positive()
        self.show_negative_minus_negative()
        self.show_special_cases()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化数轴和相关元素"""
        # 创建数轴 (-6 到 6)
        self.number_line = NumberLine(
            x_range=[-6, 6, 1],
            length=12 * self.UNIT_LENGTH,
            include_numbers=True,
            numbers_to_include=range(-6, 7),
            font_size=20,
            color=self.COLOR_NUMBERLINE,
            include_tip=True,
            tip_width=0.15,
            tip_height=0.15,
        ).move_to(self.NUMBERLINE_POS)
        
        # 数轴标签
        self.number_line_label = Text(
            "数轴",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(self.number_line, DOWN, buff=0.3)
    
    def show_opening(self):
        """场景1: 开场引入"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "减法 = 加法 ?",
            font="PingFang SC",
            font_size=self.FONT_TITLE + 8,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=1.2)
        
        # 副标题
        subtitle = Text(
            "揭秘减法的秘密!",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 数轴创建
        self.play(Create(self.number_line), run_time=1.5)
        self.play(FadeIn(self.number_line_label), run_time=0.4)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_core_concept(self):
        """场景2: 核心概念 - 减法转加法"""
        # 标题
        title = Text(
            "减法的秘密",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_TRANSFORM
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        original = MathTex(
            r"3 - 2",
            font_size=self.FONT_FORMULA + 4
        ).move_to(UP * 4)
        
        self.play(Write(original), run_time=0.6)
        self.wait(0.5)
        
        # 相反数概念
        opposite_concept = Text(
            "2 的相反数是 -2",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 3)
        
        self.play(FadeIn(opposite_concept, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 转化箭头
        transform_arrow = Arrow(
            UP * 2.5,
            UP * 1.5,
            color=self.COLOR_TRANSFORM,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.2
        )
        
        transform_text = Text(
            "转化",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_TRANSFORM
        ).next_to(transform_arrow, RIGHT, buff=0.2)
        
        self.play(
            GrowArrow(transform_arrow),
            FadeIn(transform_text),
            run_time=1.0
        )
        
        # 转化后的公式
        transformed = MathTex(
            r"3 + (-2)",
            font_size=self.FONT_FORMULA + 4,
            color=self.COLOR_TRANSFORM
        ).move_to(UP * 1)
        
        self.play(Write(transformed), run_time=0.8)
        
        # 高亮变化部分
        self.play(
            Indicate(transformed[0][2:6], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 法则说明
        rule_text = Text(
            "减去一个数 = 加上它的相反数",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=YELLOW
        ).move_to(ORIGIN)
        
        self.play(FadeIn(rule_text, shift=UP * 0.3), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(original),
            FadeOut(opposite_concept),
            FadeOut(transform_arrow),
            FadeOut(transform_text),
            FadeOut(transformed),
            FadeOut(rule_text),
            run_time=0.6
        )
    
    def show_positive_minus_positive_case1(self):
        """场景3: 正数减正数 (3 - 2 = 1)"""
        # 标题
        title = Text(
            "正数 - 正数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula_original = MathTex(
            r"3 - 2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_original), run_time=0.6)
        self.wait(0.3)
        
        # 转化
        formula_transformed = MathTex(
            r"3 + (-2)",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(TransformMatchingTex(formula_original, formula_transformed), run_time=0.8)
        self.wait(0.5)
        
        # 起点: 3
        start_dot = Dot(
            self.number_line.n2p(3),
            color=self.COLOR_POSITIVE,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_POSITIVE, flash_radius=0.25), run_time=0.3)
        
        # 箭头: 3 → 1 (向左2个单位)
        arrow = Arrow(
            self.number_line.n2p(3),
            self.number_line.n2p(1),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step_text = Text(
            "加上 -2 (向左移动)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow), run_time=1.0)
        self.play(FadeIn(step_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: 1
        result_dot = Dot(
            self.number_line.n2p(1),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"3 - 2 = 1",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_transformed),
            FadeOut(start_dot),
            FadeOut(result_dot),
            FadeOut(arrow),
            FadeOut(step_text),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_positive_minus_positive_case2(self):
        """场景4: 正数减正数 (2 - 5 = -3)"""
        # 标题
        title = Text(
            "正数 - 正数 (结果为负)",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula_original = MathTex(
            r"2 - 5",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_original), run_time=0.6)
        self.wait(0.3)
        
        # 转化
        formula_transformed = MathTex(
            r"2 + (-5)",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(TransformMatchingTex(formula_original, formula_transformed), run_time=0.8)
        self.wait(0.5)
        
        # 起点: 2
        start_dot = Dot(
            self.number_line.n2p(2),
            color=self.COLOR_POSITIVE,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_POSITIVE, flash_radius=0.25), run_time=0.3)
        
        # 箭头: 2 → -3 (向左5个单位)
        arrow = Arrow(
            self.number_line.n2p(2),
            self.number_line.n2p(-3),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step_text = Text(
            "加上 -5 (向左移动5格)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow), run_time=1.2)
        self.play(FadeIn(step_text, shift=UP * 0.2), run_time=0.4)
        
        # 说明
        note_text = Text(
            "进入负数区域!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(note_text, shift=UP * 0.3), run_time=0.5)
        
        # 结果点: -3
        result_dot = Dot(
            self.number_line.n2p(-3),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"2 - 5 = -3",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_transformed),
            FadeOut(start_dot),
            FadeOut(result_dot),
            FadeOut(arrow),
            FadeOut(step_text),
            FadeOut(note_text),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_positive_minus_negative(self):
        """场景5: 正数减负数 (3 - (-2) = 5)"""
        # 标题
        title = Text(
            "正数 - 负数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=YELLOW
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula_original = MathTex(
            r"3 - (-2)",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_original), run_time=0.6)
        self.wait(0.3)
        
        # 负负得正提示
        hint = Text(
            "负负得正!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(hint, scale=1.2), run_time=0.5)
        
        # 转化
        formula_transformed = MathTex(
            r"3 + 2",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 4.5)
        
        self.play(
            TransformMatchingTex(formula_original, formula_transformed),
            FadeOut(hint),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 起点: 3
        start_dot = Dot(
            self.number_line.n2p(3),
            color=self.COLOR_POSITIVE,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_POSITIVE, flash_radius=0.25), run_time=0.3)
        
        # 箭头: 3 → 5 (向右2个单位)
        arrow = Arrow(
            self.number_line.n2p(3),
            self.number_line.n2p(5),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step_text = Text(
            "加上 2 (向右移动)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow), run_time=1.0)
        self.play(FadeIn(step_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: 5
        result_dot = Dot(
            self.number_line.n2p(5),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"3 - (-2) = 5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_transformed),
            FadeOut(start_dot),
            FadeOut(result_dot),
            FadeOut(arrow),
            FadeOut(step_text),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_negative_minus_positive(self):
        """场景6: 负数减正数 ((-3) - 2 = -5)"""
        # 标题
        title = Text(
            "负数 - 正数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula_original = MathTex(
            r"(-3) - 2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_original), run_time=0.6)
        self.wait(0.3)
        
        # 转化
        formula_transformed = MathTex(
            r"(-3) + (-2)",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(TransformMatchingTex(formula_original, formula_transformed), run_time=0.8)
        self.wait(0.5)
        
        # 起点: -3
        start_dot = Dot(
            self.number_line.n2p(-3),
            color=self.COLOR_NEGATIVE,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_NEGATIVE, flash_radius=0.25), run_time=0.3)
        
        # 箭头: -3 → -5 (向左2个单位)
        arrow = Arrow(
            self.number_line.n2p(-3),
            self.number_line.n2p(-5),
            buff=0,
            color=self.COLOR_NEGATIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step_text = Text(
            "加上 -2 (向左移动)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow), run_time=1.0)
        self.play(FadeIn(step_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: -5
        result_dot = Dot(
            self.number_line.n2p(-5),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"(-3) - 2 = -5",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_transformed),
            FadeOut(start_dot),
            FadeOut(result_dot),
            FadeOut(arrow),
            FadeOut(step_text),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_negative_minus_negative(self):
        """场景7: 负数减负数 ((-2) - (-3) = 1)"""
        # 标题
        title = Text(
            "负数 - 负数",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 原式
        formula_original = MathTex(
            r"(-2) - (-3)",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_original), run_time=0.6)
        self.wait(0.3)
        
        # 负负得正提示
        hint = Text(
            "负负得正!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(hint, scale=1.2), run_time=0.5)
        
        # 转化
        formula_transformed = MathTex(
            r"(-2) + 3",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            TransformMatchingTex(formula_original, formula_transformed),
            FadeOut(hint),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 起点: -2
        start_dot = Dot(
            self.number_line.n2p(-2),
            color=self.COLOR_NEGATIVE,
            radius=0.1
        )
        
        self.play(FadeIn(start_dot, scale=0.5), run_time=0.4)
        self.play(Flash(start_dot, color=self.COLOR_NEGATIVE, flash_radius=0.25), run_time=0.3)
        
        # 箭头: -2 → 1 (向右3个单位)
        arrow = Arrow(
            self.number_line.n2p(-2),
            self.number_line.n2p(1),
            buff=0,
            color=self.COLOR_POSITIVE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        step_text = Text(
            "加上 3 (向右移动)",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 0.5)
        
        self.play(GrowArrow(arrow), run_time=1.0)
        self.play(FadeIn(step_text, shift=UP * 0.2), run_time=0.4)
        
        # 结果点: 1
        result_dot = Dot(
            self.number_line.n2p(1),
            color=self.COLOR_RESULT,
            radius=0.12
        )
        
        self.play(FadeIn(result_dot, scale=0.5), run_time=0.4)
        self.play(Flash(result_dot, color=self.COLOR_RESULT, flash_radius=0.3), run_time=0.4)
        
        # 结论
        conclusion = MathTex(
            r"(-2) - (-3) = 1",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_transformed),
            FadeOut(start_dot),
            FadeOut(result_dot),
            FadeOut(arrow),
            FadeOut(step_text),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_special_cases(self):
        """场景8: 特殊情况"""
        # 标题
        title = Text(
            "特殊情况",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_ZERO
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 公式1: a - 0 = a
        formula1 = MathTex(
            r"a - 0 = a",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        explain1 = Text(
            "减去0，结果不变",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(Write(formula1), run_time=0.8)
        self.play(FadeIn(explain1), run_time=0.5)
        self.wait(1.0)
        
        # 公式2: 0 - a = -a
        formula2 = MathTex(
            r"0 - a = -a",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 1)
        
        explain2 = Text(
            "0减去一个数，得它的相反数",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(ORIGIN)
        
        self.play(Write(formula2), run_time=0.8)
        self.play(FadeIn(explain2), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula1),
            FadeOut(explain1),
            FadeOut(formula2),
            FadeOut(explain2),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景9: 总结 - 减法法则"""
        # 数轴淡出
        self.play(
            FadeOut(self.number_line),
            FadeOut(self.number_line_label),
            run_time=0.5
        )
        
        # 大标题
        title = Text(
            "有理数减法法则",
            font="PingFang SC",
            font_size=self.FONT_TITLE + 4,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)
        
        # 核心法则卡片
        core_rule = VGroup(
            Text("核心法则", font="PingFang SC", font_size=28, color=WHITE, weight=BOLD),
            MathTex(r"a - b = a + (-b)", font_size=32, color=self.COLOR_TRANSFORM)
        ).arrange(DOWN, buff=0.3).move_to(UP * 4)
        
        self.play(FadeIn(core_rule, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 步骤卡片
        steps_card = VGroup(
            Text("两步走", font="PingFang SC", font_size=26, color=WHITE, weight=BOLD),
            Text("① 找出相反数", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("② 转化为加法", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(UP * 1.5)
        
        self.play(FadeIn(steps_card, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 示例卡片
        examples_card = VGroup(
            Text("常见示例", font="PingFang SC", font_size=26, color=WHITE, weight=BOLD),
            MathTex(r"3 - 2 = 3 + (-2) = 1", font_size=20, color=GRAY_A),
            MathTex(r"3 - (-2) = 3 + 2 = 5", font_size=20, color=GRAY_A),
            MathTex(r"(-3) - 2 = (-3) + (-2) = -5", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 1.5)
        
        self.play(FadeIn(examples_card, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 重点提示
        highlight = Text(
            "减法统一为加法, 计算更简单!",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(core_rule),
            FadeOut(steps_card),
            FadeOut(examples_card),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景10: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
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
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 符号装饰 (减号变加号)
        minus_sign = MathTex(r"-", font_size=80, color=self.COLOR_NEGATIVE).move_to(DOWN * 2.5)
        plus_sign = MathTex(r"+", font_size=80, color=self.COLOR_POSITIVE).move_to(DOWN * 2.5)
        
        self.play(FadeIn(minus_sign, scale=1.5), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(minus_sign, plus_sign), run_time=1.0)
        
        # 环绕装饰
        decorations = VGroup(*[
            MathTex(r"(-" + str(i) + r")", font_size=24, color=self.COLOR_AUXILIARY)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 2), np.sin(i * PI / 2), 0]))
            for i in range(1, 5)
        ])
        
        self.play(*[FadeIn(dec, scale=0.5) for dec in decorations], run_time=0.6)
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(minus_sign),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql rational_number_subtraction.py RationalNumberSubtraction  # 快速预览
# manim -qh rational_number_subtraction.py RationalNumberSubtraction   # 高质量 1080p
# manim -qk rational_number_subtraction.py RationalNumberSubtraction   # 4K质量
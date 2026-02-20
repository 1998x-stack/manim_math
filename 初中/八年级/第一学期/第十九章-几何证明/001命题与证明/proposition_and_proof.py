"""
命题与证明 - Propositions and Proofs
使用 Manim 创建的中学数学教学视频

内容: 命题的定义、结构、真假判断及证明的规范格式
目标观众: 八年级学生
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


class PropositionAndProof(Scene):
    """
    命题与证明教学动画
    
    场景顺序:
    1. 开场钩子
    2. 命题的定义
    3. 命题的结构
    4. 真命题与假命题
    5. 定理的概念
    6. 什么是证明
    7. 证明的格式
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要内容
        self.COLOR_CONDITION = "#e74c3c"      # 红色 - 条件
        self.COLOR_CONCLUSION = "#2ecc71"     # 绿色 - 结论
        self.COLOR_TRUE = "#2ecc71"           # 绿色 - 真命题
        self.COLOR_FALSE = "#e74c3c"          # 红色 - 假命题
        self.COLOR_PROOF = "#9b59b6"          # 紫色 - 证明
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_structure()
        self.show_true_false()
        self.show_theorem()
        self.show_what_is_proof()
        self.show_proof_format()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 6.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这句话是真的还是假的?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=0.9)
        self.wait(0.3)
        
        # 示例语句
        statement = Text(
            '"如果下雨，那么地面会湿"',
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(statement, shift=UP * 0.3), run_time=1.0)
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.5)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(statement),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 命题的定义"""
        # 标题
        title = Text(
            "什么是命题?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "可以判断真假的语句",
            font="Noto Sans CJK SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 4.2)
        
        definition_box = SurroundingRectangle(
            definition,
            color=self.COLOR_PRIMARY,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.0)
        self.play(Create(definition_box), run_time=0.6)
        self.wait(0.3)
        
        # 关键特点
        features_title = Text(
            "关键特点：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2.5 + LEFT * 3)
        
        self.play(FadeIn(features_title), run_time=0.4)
        
        features = VGroup(
            VGroup(
                Text("✓", font_size=30, color=GREEN),
                Text("能判断真假", font="Noto Sans CJK SC", font_size=24)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", font_size=30, color=GREEN),
                Text("是陈述句", font="Noto Sans CJK SC", font_size=24)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", font_size=30, color=GREEN),
                Text("只有一个答案", font="Noto Sans CJK SC", font_size=24)
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 0.8)
        
        for feature in features:
            self.play(FadeIn(feature, shift=LEFT * 0.3), run_time=0.6)
            self.wait(0.4)
        
        # 框选整体
        all_features = VGroup(features_title, features)
        features_box = SurroundingRectangle(
            all_features,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(Create(features_box), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(definition_box),
            FadeOut(features_title),
            FadeOut(features),
            FadeOut(features_box),
            run_time=0.6
        )
    
    def show_structure(self):
        """场景3: 命题的结构"""
        # 副标题
        subtitle = Text(
            "命题的结构",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.2)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 标准格式
        standard_format = VGroup(
            Text("若", font="Noto Sans CJK SC", font_size=36, color=WHITE),
            MathTex(r"p", font_size=40, color=self.COLOR_CONDITION),
            Text("，则", font="Noto Sans CJK SC", font_size=36, color=WHITE),
            MathTex(r"q", font_size=40, color=self.COLOR_CONCLUSION)
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4)
        
        self.play(Write(standard_format), run_time=1.0)
        self.wait(0.3)
        
        # 具体示例
        example = Text(
            "若两角是对顶角，则这两角相等",
            font="Noto Sans CJK SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(Write(example), run_time=1.0)
        self.wait(0.3)
        
        # 创建条件和结论的分离版本用于标注
        condition_text = Text(
            "两角是对顶角",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_CONDITION
        ).move_to(LEFT * 1.5 + UP * 0.8)
        
        conclusion_text = Text(
            "这两角相等",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_CONCLUSION
        ).move_to(RIGHT * 1.5 + UP * 0.8)
        
        # 转换示例到分离版本
        self.play(
            FadeOut(example),
            FadeIn(condition_text),
            FadeIn(conclusion_text),
            run_time=0.8
        )
        
        # 标注条件
        condition_brace = Brace(condition_text, DOWN, color=self.COLOR_CONDITION)
        condition_label = Text(
            "条件（已知）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_CONDITION
        ).next_to(condition_brace, DOWN, buff=0.15)
        
        self.play(
            Indicate(condition_text, color=self.COLOR_CONDITION),
            run_time=0.6
        )
        self.play(
            FadeIn(condition_brace),
            FadeIn(condition_label),
            run_time=0.6
        )
        self.wait(0.4)
        
        # 标注结论
        conclusion_brace = Brace(conclusion_text, DOWN, color=self.COLOR_CONCLUSION)
        conclusion_label = Text(
            "结论（求证）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_CONCLUSION
        ).next_to(conclusion_brace, DOWN, buff=0.15)
        
        self.play(
            Indicate(conclusion_text, color=self.COLOR_CONCLUSION),
            run_time=0.6
        )
        self.play(
            FadeIn(conclusion_brace),
            FadeIn(conclusion_label),
            run_time=0.6
        )
        self.wait(0.4)
        
        # 箭头连接
        arrow = Arrow(
            condition_text.get_right() + RIGHT * 0.2,
            conclusion_text.get_left() + LEFT * 0.2,
            color=YELLOW,
            buff=0.1,
            stroke_width=6
        ).shift(UP * 0.3)
        
        self.play(GrowArrow(arrow), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "从条件推出结论",
            font="Noto Sans CJK SC",
            font_size=20,
            color=YELLOW
        ).next_to(arrow, UP, buff=0.15)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(standard_format),
            FadeOut(condition_text),
            FadeOut(conclusion_text),
            FadeOut(condition_brace),
            FadeOut(condition_label),
            FadeOut(conclusion_brace),
            FadeOut(conclusion_label),
            FadeOut(arrow),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_true_false(self):
        """场景4: 真命题与假命题"""
        # 副标题
        subtitle = Text(
            "真命题 vs 假命题",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.2)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 左侧：真命题
        true_title = Text(
            "真命题",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_TRUE
        ).move_to(LEFT * 2.5 + UP * 3.8)
        
        true_prop = VGroup(
            Text("若", font="Noto Sans CJK SC", font_size=24),
            MathTex(r"a=b", font_size=28),
            Text("，则", font="Noto Sans CJK SC", font_size=24),
            MathTex(r"a+c=b+c", font_size=28)
        ).arrange(RIGHT, buff=0.1).move_to(LEFT * 2.5 + UP * 2.8)
        
        check_mark = Text(
            "✓",
            font_size=50,
            color=self.COLOR_TRUE
        ).move_to(LEFT * 2.5 + UP * 1.8)
        
        true_box = SurroundingRectangle(
            VGroup(true_title, true_prop, check_mark),
            color=self.COLOR_TRUE,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(FadeIn(true_title), run_time=0.5)
        self.play(FadeIn(true_prop, shift=LEFT * 0.2), run_time=0.8)
        self.play(FadeIn(check_mark, scale=1.5), run_time=0.6)
        self.play(Create(true_box), run_time=0.6)
        self.wait(0.5)
        
        # 右侧：假命题
        false_title = Text(
            "假命题",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_FALSE
        ).move_to(RIGHT * 2.5 + UP * 3.8)
        
        false_prop = VGroup(
            Text("若", font="Noto Sans CJK SC", font_size=24),
            MathTex(r"a>b", font_size=28),
            Text("，则", font="Noto Sans CJK SC", font_size=24),
            MathTex(r"a^2>b^2", font_size=28)
        ).arrange(RIGHT, buff=0.1).move_to(RIGHT * 2.5 + UP * 2.8)
        
        cross_mark = Text(
            "✗",
            font_size=50,
            color=self.COLOR_FALSE
        ).move_to(RIGHT * 2.5 + UP * 1.8)
        
        false_box = SurroundingRectangle(
            VGroup(false_title, false_prop, cross_mark),
            color=self.COLOR_FALSE,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(FadeIn(false_title), run_time=0.5)
        self.play(FadeIn(false_prop, shift=RIGHT * 0.2), run_time=0.8)
        self.play(FadeIn(cross_mark, scale=1.5), run_time=0.6)
        self.play(Create(false_box), run_time=0.6)
        self.wait(0.5)
        
        # 反例说明
        counter_example_title = Text(
            "反例：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_FALSE
        ).move_to(RIGHT * 2.5 + UP * 0.5)
        
        counter_example = VGroup(
            MathTex(r"a=-3,\ b=-2", font_size=26),
            MathTex(r"a>b", font_size=26, color=GREEN),
            Text("但", font="Noto Sans CJK SC", font_size=22),
            MathTex(r"a^2=9<4=b^2", font_size=26, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(counter_example_title, DOWN, buff=0.2)
        
        self.play(FadeIn(counter_example_title), run_time=0.5)
        self.play(Write(counter_example), run_time=2.0)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(true_title),
            FadeOut(true_prop),
            FadeOut(check_mark),
            FadeOut(true_box),
            FadeOut(false_title),
            FadeOut(false_prop),
            FadeOut(cross_mark),
            FadeOut(false_box),
            FadeOut(counter_example_title),
            FadeOut(counter_example),
            run_time=0.6
        )
    
    def show_theorem(self):
        """场景5: 定理的概念"""
        # 副标题
        subtitle = Text(
            "什么是定理?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.2)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 定义
        definition = Text(
            "经过证明的真命题",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        definition_box = SurroundingRectangle(
            definition,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25
        )
        
        self.play(FadeIn(definition), run_time=0.8)
        self.play(Create(definition_box), run_time=0.6)
        self.wait(0.4)
        
        # 流程图
        box_1 = VGroup(
            Text("真命题", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Rectangle(height=0.8, width=2.2, color=self.COLOR_TRUE)
        )
        box_1[1].move_to(box_1[0].get_center())
        box_1.move_to(LEFT * 3 + UP * 2)
        
        arrow_1 = Arrow(
            box_1.get_right(),
            box_1.get_right() + RIGHT * 1.2,
            color=YELLOW,
            buff=0
        )
        
        box_2 = VGroup(
            Text("证明", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Rectangle(height=0.8, width=1.8, color=self.COLOR_PROOF)
        )
        box_2[1].move_to(box_2[0].get_center())
        box_2.move_to(UP * 2)
        
        arrow_2 = Arrow(
            box_2.get_right(),
            box_2.get_right() + RIGHT * 1.2,
            color=YELLOW,
            buff=0
        )
        
        box_3 = VGroup(
            Text("定理", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Rectangle(height=0.8, width=1.8, color=BLUE)
        )
        box_3[1].move_to(box_3[0].get_center())
        box_3.move_to(RIGHT * 3 + UP * 2)
        
        self.play(FadeIn(box_1), run_time=0.7)
        self.play(GrowArrow(arrow_1), run_time=0.5)
        self.play(FadeIn(box_2), run_time=0.7)
        self.play(GrowArrow(arrow_2), run_time=0.5)
        self.play(FadeIn(box_3), run_time=0.7)
        self.wait(0.6)
        
        # 例子
        examples_title = Text(
            "常见定理：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.2 + LEFT * 3)
        
        examples = VGroup(
            Text("• 勾股定理", font="Noto Sans CJK SC", font_size=22),
            Text("• 三角形内角和定理", font="Noto Sans CJK SC", font_size=22),
            Text("• 对顶角相等定理", font="Noto Sans CJK SC", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(examples_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(FadeIn(examples_title), run_time=0.5)
        self.play(FadeIn(examples), run_time=1.0)
        self.play(Indicate(examples, color=YELLOW), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(definition),
            FadeOut(definition_box),
            FadeOut(box_1),
            FadeOut(arrow_1),
            FadeOut(box_2),
            FadeOut(arrow_2),
            FadeOut(box_3),
            FadeOut(examples_title),
            FadeOut(examples),
            run_time=0.6
        )
    
    def show_what_is_proof(self):
        """场景6: 什么是证明"""
        # 副标题
        subtitle = Text(
            "什么是证明?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.2)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 定义
        definition = Text(
            "从已知到结论的推理过程",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(definition), run_time=0.8)
        self.wait(0.4)
        
        # 三要素
        elements_title = Text(
            "证明三要素：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.8 + LEFT * 3)
        
        self.play(FadeIn(elements_title), run_time=0.5)
        
        element_1 = VGroup(
            Text("①", font_size=26, color=YELLOW),
            Text("已知条件", font="Noto Sans CJK SC", font_size=24),
            Text("(起点)", font="Noto Sans CJK SC", font_size=18, color=GRAY)
        ).arrange(RIGHT, buff=0.2).move_to(LEFT * 2.5 + UP * 2)
        
        element_2 = VGroup(
            Text("②", font_size=26, color=YELLOW),
            Text("逻辑推理", font="Noto Sans CJK SC", font_size=24),
            Text("(过程)", font="Noto Sans CJK SC", font_size=18, color=GRAY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.8)
        
        element_3 = VGroup(
            Text("③", font_size=26, color=YELLOW),
            Text("得出结论", font="Noto Sans CJK SC", font_size=24),
            Text("(终点)", font="Noto Sans CJK SC", font_size=18, color=GRAY)
        ).arrange(RIGHT, buff=0.2).move_to(RIGHT * 2.5 + UP * 2)
        
        self.play(FadeIn(element_1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(element_2), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(element_3), run_time=0.8)
        self.wait(0.5)
        
        # 箭头连接
        arrow_1 = Arrow(
            element_1.get_bottom() + DOWN * 0.3,
            element_2.get_top() + UP * 0.3,
            color=YELLOW,
            buff=0.1
        )
        arrow_2 = Arrow(
            element_2.get_bottom() + DOWN * 0.3,
            element_3.get_top() + UP * 0.3,
            color=YELLOW,
            buff=0.1
        )
        
        self.play(
            GrowArrow(arrow_1),
            GrowArrow(arrow_2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 推理依据
        basis_title = Text(
            "推理依据：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 1.5 + LEFT * 3)
        
        basis_list = VGroup(
            Text("• 定义", font="Noto Sans CJK SC", font_size=22),
            Text("• 公理", font="Noto Sans CJK SC", font_size=22),
            Text("• 已证定理", font="Noto Sans CJK SC", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(basis_title, DOWN, buff=0.25, aligned_edge=LEFT)
        
        self.play(FadeIn(basis_title), run_time=0.5)
        self.play(FadeIn(basis_list), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(definition),
            FadeOut(elements_title),
            FadeOut(element_1),
            FadeOut(element_2),
            FadeOut(element_3),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(basis_title),
            FadeOut(basis_list),
            run_time=0.6
        )
    
    def show_proof_format(self):
        """场景7: 证明的格式"""
        # 副标题
        subtitle = Text(
            "证明的规范格式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.2)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 已知部分
        given_label = Text(
            "已知：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_CONDITION
        ).move_to(LEFT * 3.5 + UP * 3.8)
        
        given_content = VGroup(
            MathTex(r"\angle 1", font_size=26),
            Text("和", font="Noto Sans CJK SC", font_size=22),
            MathTex(r"\angle 2", font_size=26),
            Text("是对顶角", font="Noto Sans CJK SC", font_size=22)
        ).arrange(RIGHT, buff=0.1).next_to(given_label, RIGHT, buff=0.2)
        
        given_group = VGroup(given_label, given_content)
        given_box = SurroundingRectangle(
            given_group,
            color=self.COLOR_CONDITION,
            buff=0.15,
            corner_radius=0.05
        )
        
        self.play(Write(given_label), run_time=0.5)
        self.play(Write(given_content), run_time=0.8)
        self.play(Create(given_box), run_time=0.6)
        self.wait(0.4)
        
        # 求证部分
        prove_label = Text(
            "求证：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_CONCLUSION
        ).move_to(LEFT * 3.5 + UP * 2.8)
        
        prove_content = MathTex(
            r"\angle 1 = \angle 2",
            font_size=28
        ).next_to(prove_label, RIGHT, buff=0.2)
        
        prove_group = VGroup(prove_label, prove_content)
        prove_box = SurroundingRectangle(
            prove_group,
            color=self.COLOR_CONCLUSION,
            buff=0.15,
            corner_radius=0.05
        )
        
        self.play(Write(prove_label), run_time=0.5)
        self.play(Write(prove_content), run_time=0.8)
        self.play(Create(prove_box), run_time=0.6)
        self.wait(0.4)
        
        # 证明部分
        proof_label = Text(
            "证明：",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_PROOF
        ).move_to(LEFT * 3.5 + UP * 1.5)
        
        self.play(Write(proof_label), run_time=0.5)
        
        # 证明步骤（简化版）
        proof_lines = VGroup(
            VGroup(
                MathTex(r"\because", font_size=24),
                MathTex(r"\angle 1", font_size=24),
                Text("和", font="Noto Sans CJK SC", font_size=20),
                MathTex(r"\angle 2", font_size=24),
                Text("是对顶角", font="Noto Sans CJK SC", font_size=20),
                Text("（已知）", font="Noto Sans CJK SC", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.08),
            
            VGroup(
                MathTex(r"\therefore", font_size=24),
                MathTex(r"\angle 1 + \angle 3 = 180^\circ", font_size=22),
                Text("（平角定义）", font="Noto Sans CJK SC", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.15),
            
            VGroup(
                MathTex(r"\angle 2 + \angle 3 = 180^\circ", font_size=22),
                Text("（平角定义）", font="Noto Sans CJK SC", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.15),
            
            VGroup(
                MathTex(r"\therefore", font_size=24),
                MathTex(r"\angle 1 = \angle 2", font_size=24),
                Text("（等量代换）", font="Noto Sans CJK SC", font_size=18, color=GRAY)
            ).arrange(RIGHT, buff=0.15)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(proof_label, DOWN, buff=0.2, aligned_edge=LEFT).shift(RIGHT * 0.3)
        
        for line in proof_lines:
            self.play(Write(line), run_time=1.0)
            self.wait(0.3)
        
        # 框选证明部分
        proof_group = VGroup(proof_label, proof_lines)
        proof_box = SurroundingRectangle(
            proof_group,
            color=self.COLOR_PROOF,
            buff=0.2,
            corner_radius=0.05
        )
        
        self.play(Create(proof_box), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(given_group),
            FadeOut(given_box),
            FadeOut(prove_group),
            FadeOut(prove_box),
            FadeOut(proof_group),
            FadeOut(proof_box),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景8: 总结与片尾"""
        # 标题
        title = Text(
            "命题与证明 - 要点总结",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 四个要点
        points = VGroup(
            VGroup(
                Text("①", font_size=28, color=YELLOW),
                Text("命题 = 能判断真假的语句", font="Noto Sans CJK SC", font_size=24)
            ).arrange(RIGHT, buff=0.3),
            
            VGroup(
                Text("②", font_size=28, color=YELLOW),
                VGroup(
                    Text("命题 = 条件 + 结论", font="Noto Sans CJK SC", font_size=24),
                    Text("（若p则q）", font="Noto Sans CJK SC", font_size=20, color=GRAY)
                ).arrange(RIGHT, buff=0.2)
            ).arrange(RIGHT, buff=0.3),
            
            VGroup(
                Text("③", font_size=28, color=YELLOW),
                VGroup(
                    Text("真命题经证明后", font="Noto Sans CJK SC", font_size=24),
                    MathTex(r"\rightarrow", font_size=24),
                    Text("定理", font="Noto Sans CJK SC", font_size=24)
                ).arrange(RIGHT, buff=0.15)
            ).arrange(RIGHT, buff=0.3),
            
            VGroup(
                Text("④", font_size=28, color=YELLOW),
                Text("证明要用规范格式", font="Noto Sans CJK SC", font_size=24)
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 2)
        
        for point in points:
            self.play(FadeIn(point, shift=UP * 0.2), run_time=0.6)
            self.wait(0.6)
        
        # 关键提示
        key_point = Text(
            "掌握证明，数学思维上台阶!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.1), run_time=0.8)
        self.wait(1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 3.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 装饰符号
        symbols = VGroup(
            Text("∵", font_size=35, color=self.COLOR_CONDITION),
            Text("∴", font_size=35, color=self.COLOR_CONCLUSION),
            Text("→", font_size=35, color=YELLOW),
            Text("✓", font_size=35, color=GREEN),
        ).arrange(RIGHT, buff=1).move_to(DOWN * 6.5)
        
        self.play(*[FadeIn(sym, scale=0.5) for sym in symbols], run_time=0.6)
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(title),
            FadeOut(points),
            FadeOut(key_point),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql proposition_and_proof.py PropositionAndProof  # 快速预览
# manim -qh proposition_and_proof.py PropositionAndProof   # 高质量渲染
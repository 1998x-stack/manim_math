"""
有理数的概念 - Rational Numbers Concept
使用 Manim 创建的六年级数学教学视频

内容: 有理数的定义、分类和性质
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


class RationalNumbers(Scene):
    """
    有理数概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 引入定义
    3. 按符号分类
    4. 按类型分类
    5. 小数表示
    6. 实例演练
    7. 总结片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_INTEGER = "#3498db"        # 蓝色 - 整数
        self.COLOR_FRACTION = "#e74c3c"       # 红色 - 分数
        self.COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
        self.COLOR_NEGATIVE = "#f39c12"       # 橙色 - 负数
        self.COLOR_ZERO = "#9b59b6"           # 紫色 - 零
        self.COLOR_RATIONAL = "#1abc9c"       # 青色 - 有理数整体
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_classification_by_sign()
        self.show_classification_by_type()
        self.show_decimal_representation()
        self.show_practice()
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
            "这些数字有什么共同点?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 数字云团
        numbers_data = [
            ("3", UP * 3 + LEFT * 2),
            ("-5", UP * 2.5 + RIGHT * 1.5),
            (r"\frac{1}{2}", UP * 3.5 + RIGHT * 0.5),
            ("0", UP * 2 + LEFT * 1),
            ("-2.5", UP * 3.2 + LEFT * 0.5),
            (r"0.333...", UP * 2.3 + RIGHT * 2),
        ]
        
        numbers_cloud = VGroup()
        for num_text, pos in numbers_data:
            num = MathTex(num_text, font_size=36, color=WHITE)
            num.move_to(pos)
            numbers_cloud.add(num)
        
        self.play(
            *[FadeIn(num, scale=0.8) for num in numbers_cloud],
            run_time=1.0
        )
        
        # 数字闪烁强调
        self.play(
            *[Indicate(num, scale_factor=1.2) for num in numbers_cloud],
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(numbers_cloud),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 引入定义"""
        # 标题
        title = Text(
            "有理数 Rational Numbers",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_RATIONAL
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义框
        definition_box = Rectangle(
            width=7,
            height=2,
            color=self.COLOR_RATIONAL,
            stroke_width=3
        ).move_to(UP * 3.5)
        
        self.play(Create(definition_box), run_time=0.6)
        
        # 文字说明
        definition_text = Text(
            "整数和分数的统称",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(definition_text), run_time=0.8)
        
        # 数学公式
        formula = MathTex(
            r"Q = \{", r"\frac{p}{q}", r"\mid p, q \in \mathbb{Z},", r"q \neq 0", r"\}",
            font_size=32
        ).move_to(UP * 3)
        
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        formula[3].set_color(RED)
        
        self.play(Write(formula), run_time=1.2)
        
        # 高亮公式
        self.play(Indicate(formula, scale_factor=1.1), run_time=0.6)
        
        # 补充说明
        note = Text(
            "可表示为两个整数之比",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理并保留标题
        self.play(
            FadeOut(definition_box),
            FadeOut(definition_text),
            FadeOut(formula),
            FadeOut(note),
            run_time=0.5
        )
        
        # 标题缩小移到顶部
        title_small = Text(
            "有理数",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_RATIONAL
        ).move_to(UP * 6.5)
        
        self.play(Transform(title, title_small), run_time=0.4)
        self.title_ref = title
    
    def show_classification_by_sign(self):
        """场景3: 按符号分类"""
        # 副标题
        subtitle = Text(
            "分类方法一: 按符号",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 数轴
        numberline = NumberLine(
            x_range=[-5, 5, 1],
            length=7,
            include_numbers=True,
            font_size=20,
            color=WHITE,
            include_tip=True,
            tip_width=0.2,
            tip_height=0.2,
        ).move_to(UP * 2.5)
        
        self.play(Create(numberline), run_time=1.0)
        
        # 零点标记
        zero_dot = Dot(numberline.n2p(0), color=self.COLOR_ZERO, radius=0.12)
        zero_label = Text("0", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_ZERO).next_to(zero_dot, DOWN, buff=0.2)
        zero_text = Text("零", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ZERO).next_to(zero_label, DOWN, buff=0.1)
        
        self.play(
            FadeIn(zero_dot, scale=0.5),
            FadeIn(zero_label),
            FadeIn(zero_text),
            run_time=0.6
        )
        
        # 正数区域 (右侧阴影)
        positive_region = Rectangle(
            width=3.5,
            height=0.5,
            fill_color=self.COLOR_POSITIVE,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(numberline.n2p(2.5) + UP * 0.05)
        
        positive_label = Text(
            "正有理数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_POSITIVE
        ).next_to(positive_region, UP, buff=0.3)
        
        self.play(
            FadeIn(positive_region),
            FadeIn(positive_label),
            run_time=0.6
        )
        
        # 负数区域 (左侧阴影)
        negative_region = Rectangle(
            width=3.5,
            height=0.5,
            fill_color=self.COLOR_NEGATIVE,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(numberline.n2p(-2.5) + UP * 0.05)
        
        negative_label = Text(
            "负有理数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_NEGATIVE
        ).next_to(negative_region, UP, buff=0.3)
        
        self.play(
            FadeIn(negative_region),
            FadeIn(negative_label),
            run_time=0.6
        )
        
        # 示例数字
        examples_positive = [
            (r"3", numberline.n2p(3)),
            (r"\frac{1}{2}", numberline.n2p(0.5)),
            (r"0.5", numberline.n2p(1.5)),
        ]
        
        examples_negative = [
            (r"-2", numberline.n2p(-2)),
            (r"-\frac{1}{3}", numberline.n2p(-0.33)),
            (r"-0.8", numberline.n2p(-1.8)),
        ]
        
        positive_nums = VGroup()
        for num_text, pos in examples_positive:
            num = MathTex(num_text, font_size=22, color=self.COLOR_POSITIVE)
            num.next_to(pos, DOWN, buff=0.8)
            positive_nums.add(num)
        
        negative_nums = VGroup()
        for num_text, pos in examples_negative:
            num = MathTex(num_text, font_size=22, color=self.COLOR_NEGATIVE)
            num.next_to(pos, DOWN, buff=0.8)
            negative_nums.add(num)
        
        self.play(
            *[FadeIn(num, shift=DOWN * 0.3) for num in positive_nums],
            run_time=0.8
        )
        
        self.play(
            *[FadeIn(num, shift=DOWN * 0.3) for num in negative_nums],
            run_time=0.8
        )
        
        # 分类框
        box_y = DOWN * 0.5
        
        positive_box = Rectangle(
            width=2.2,
            height=1.5,
            color=self.COLOR_POSITIVE,
            stroke_width=2
        ).move_to(box_y + RIGHT * 2.5)
        
        positive_box_label = Text(
            "正有理数",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_POSITIVE
        ).move_to(positive_box.get_center() + UP * 0.5)
        
        zero_box = Rectangle(
            width=1.5,
            height=1.5,
            color=self.COLOR_ZERO,
            stroke_width=2
        ).move_to(box_y)
        
        zero_box_label = Text(
            "零",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_ZERO
        ).move_to(zero_box.get_center() + UP * 0.5)
        
        negative_box = Rectangle(
            width=2.2,
            height=1.5,
            color=self.COLOR_NEGATIVE,
            stroke_width=2
        ).move_to(box_y + LEFT * 2.5)
        
        negative_box_label = Text(
            "负有理数",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_NEGATIVE
        ).move_to(negative_box.get_center() + UP * 0.5)
        
        classification_boxes = VGroup(
            positive_box, positive_box_label,
            zero_box, zero_box_label,
            negative_box, negative_box_label
        )
        
        self.play(Create(classification_boxes), run_time=1.0)
        
        # 数字归类动画
        box_examples_positive = MathTex(
            r"3, \frac{1}{2}, 0.5, ...",
            font_size=18,
            color=WHITE
        ).move_to(positive_box.get_center() + DOWN * 0.2)
        
        box_example_zero = MathTex(
            r"0",
            font_size=22,
            color=WHITE
        ).move_to(zero_box.get_center() + DOWN * 0.2)
        
        box_examples_negative = MathTex(
            r"-2, -\frac{1}{3}, -0.8, ...",
            font_size=16,
            color=WHITE
        ).move_to(negative_box.get_center() + DOWN * 0.2)
        
        self.play(
            FadeIn(box_examples_positive),
            FadeIn(box_example_zero),
            FadeIn(box_examples_negative),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(numberline),
            FadeOut(zero_dot),
            FadeOut(zero_label),
            FadeOut(zero_text),
            FadeOut(positive_region),
            FadeOut(positive_label),
            FadeOut(negative_region),
            FadeOut(negative_label),
            FadeOut(positive_nums),
            FadeOut(negative_nums),
            FadeOut(classification_boxes),
            FadeOut(box_examples_positive),
            FadeOut(box_example_zero),
            FadeOut(box_examples_negative),
            run_time=0.6
        )
    
    def show_classification_by_type(self):
        """场景4: 按类型分类 - 树状图"""
        # 副标题
        subtitle = Text(
            "分类方法二: 按类型",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 树状图结构
        # 根节点
        root = Rectangle(
            width=2,
            height=0.8,
            fill_color=self.COLOR_RATIONAL,
            fill_opacity=0.8,
            stroke_color=self.COLOR_RATIONAL,
            stroke_width=2
        ).move_to(UP * 4)
        
        root_text = Text(
            "有理数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(root.get_center())
        
        root_group = VGroup(root, root_text)
        
        self.play(FadeIn(root_group, scale=0.8), run_time=0.6)
        
        # 第一层分支线
        branch_1_left = Line(
            root.get_bottom(),
            UP * 2.5 + LEFT * 2,
            color=GRAY_B,
            stroke_width=2
        )
        
        branch_1_right = Line(
            root.get_bottom(),
            UP * 2.5 + RIGHT * 2,
            color=GRAY_B,
            stroke_width=2
        )
        
        # 第一层节点 - 整数
        integer_node = Rectangle(
            width=1.8,
            height=0.8,
            fill_color=self.COLOR_INTEGER,
            fill_opacity=0.8,
            stroke_color=self.COLOR_INTEGER,
            stroke_width=2
        ).move_to(UP * 2.5 + LEFT * 2)
        
        integer_text = Text(
            "整数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(integer_node.get_center())
        
        integer_group = VGroup(integer_node, integer_text)
        
        # 第一层节点 - 分数
        fraction_node = Rectangle(
            width=1.8,
            height=0.8,
            fill_color=self.COLOR_FRACTION,
            fill_opacity=0.8,
            stroke_color=self.COLOR_FRACTION,
            stroke_width=2
        ).move_to(UP * 2.5 + RIGHT * 2)
        
        fraction_text = Text(
            "分数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(fraction_node.get_center())
        
        fraction_group = VGroup(fraction_node, fraction_text)
        
        self.play(
            GrowFromPoint(branch_1_left, root.get_bottom()),
            GrowFromPoint(branch_1_right, root.get_bottom()),
            run_time=0.6
        )
        
        self.play(
            FadeIn(integer_group, shift=DOWN * 0.2),
            FadeIn(fraction_group, shift=DOWN * 0.2),
            run_time=0.6
        )
        
        # 整数的子分类
        int_branches = VGroup(
            Line(integer_node.get_bottom(), UP * 0.8 + LEFT * 3.2, color=GRAY_B, stroke_width=1.5),
            Line(integer_node.get_bottom(), UP * 0.8 + LEFT * 2, color=GRAY_B, stroke_width=1.5),
            Line(integer_node.get_bottom(), UP * 0.8 + LEFT * 0.8, color=GRAY_B, stroke_width=1.5),
        )
        
        self.play(
            *[GrowFromPoint(branch, integer_node.get_bottom()) for branch in int_branches],
            run_time=0.6
        )
        
        # 整数子节点
        pos_int = self.create_small_node("正整数", self.COLOR_POSITIVE, UP * 0.8 + LEFT * 3.2)
        zero_int = self.create_small_node("零", self.COLOR_ZERO, UP * 0.8 + LEFT * 2)
        neg_int = self.create_small_node("负整数", self.COLOR_NEGATIVE, UP * 0.8 + LEFT * 0.8)
        
        self.play(
            FadeIn(pos_int, shift=DOWN * 0.2),
            FadeIn(zero_int, shift=DOWN * 0.2),
            FadeIn(neg_int, shift=DOWN * 0.2),
            run_time=0.6
        )
        
        # 分数的子分类
        frac_branches = VGroup(
            Line(fraction_node.get_bottom(), UP * 0.8 + RIGHT * 1.2, color=GRAY_B, stroke_width=1.5),
            Line(fraction_node.get_bottom(), UP * 0.8 + RIGHT * 2.8, color=GRAY_B, stroke_width=1.5),
        )
        
        self.play(
            *[GrowFromPoint(branch, fraction_node.get_bottom()) for branch in frac_branches],
            run_time=0.6
        )
        
        # 分数子节点
        pos_frac = self.create_small_node("正分数", self.COLOR_POSITIVE, UP * 0.8 + RIGHT * 1.2)
        neg_frac = self.create_small_node("负分数", self.COLOR_NEGATIVE, UP * 0.8 + RIGHT * 2.8)
        
        self.play(
            FadeIn(pos_frac, shift=DOWN * 0.2),
            FadeIn(neg_frac, shift=DOWN * 0.2),
            run_time=0.6
        )
        
        # 添加示例
        int_examples = VGroup(
            MathTex(r"3", font_size=18, color=WHITE).next_to(pos_int, DOWN, buff=0.15),
            MathTex(r"0", font_size=18, color=WHITE).next_to(zero_int, DOWN, buff=0.15),
            MathTex(r"-5", font_size=18, color=WHITE).next_to(neg_int, DOWN, buff=0.15),
        )
        
        frac_examples = VGroup(
            MathTex(r"\frac{1}{2}", font_size=18, color=WHITE).next_to(pos_frac, DOWN, buff=0.15),
            MathTex(r"-\frac{3}{4}", font_size=18, color=WHITE).next_to(neg_frac, DOWN, buff=0.15),
        )
        
        self.play(
            *[FadeIn(ex) for ex in int_examples],
            run_time=0.6
        )
        
        self.play(
            *[FadeIn(ex) for ex in frac_examples],
            run_time=0.6
        )
        
        # 整体树状图
        tree = VGroup(
            root_group, branch_1_left, branch_1_right,
            integer_group, fraction_group,
            int_branches, pos_int, zero_int, neg_int,
            frac_branches, pos_frac, neg_frac,
            int_examples, frac_examples
        )
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(tree),
            run_time=0.6
        )
    
    def create_small_node(self, text, color, position):
        """创建小节点"""
        node = Rectangle(
            width=1.5,
            height=0.6,
            fill_color=color,
            fill_opacity=0.6,
            stroke_color=color,
            stroke_width=1.5
        ).move_to(position)
        
        node_text = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=16,
            color=WHITE
        ).move_to(node.get_center())
        
        return VGroup(node, node_text)
    
    def show_decimal_representation(self):
        """场景5: 小数表示"""
        # 副标题
        subtitle = Text(
            "小数表示",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 分数示例
        fractions = VGroup(
            MathTex(r"\frac{1}{2}", font_size=36),
            MathTex(r"\frac{1}{3}", font_size=36),
            MathTex(r"\frac{1}{4}", font_size=36),
        ).arrange(DOWN, buff=0.8).move_to(UP * 2 + LEFT * 2)
        
        self.play(Write(fractions), run_time=0.8)
        
        # 转换箭头
        arrows = VGroup(
            Arrow(LEFT * 0.5, RIGHT * 0.5, color=self.COLOR_HIGHLIGHT, stroke_width=4).move_to(UP * 2.8),
            Arrow(LEFT * 0.5, RIGHT * 0.5, color=self.COLOR_HIGHLIGHT, stroke_width=4).move_to(UP * 2),
            Arrow(LEFT * 0.5, RIGHT * 0.5, color=self.COLOR_HIGHLIGHT, stroke_width=4).move_to(UP * 1.2),
        )
        
        self.play(*[GrowArrow(arrow) for arrow in arrows], run_time=0.6)
        
        # 小数结果
        decimals = VGroup(
            MathTex(r"0.5", font_size=36, color=self.COLOR_POSITIVE),
            MathTex(r"0.333...", font_size=36, color=self.COLOR_POSITIVE),
            MathTex(r"0.25", font_size=36, color=self.COLOR_POSITIVE),
        ).arrange(DOWN, buff=0.8).move_to(UP * 2 + RIGHT * 2)
        
        self.play(Write(decimals), run_time=1.0)
        
        # 循环标记
        repeat_arc = Arc(
            radius=0.4,
            start_angle=0,
            angle=PI,
            color=RED,
            stroke_width=2
        ).next_to(decimals[1], UP, buff=0.05).shift(RIGHT * 0.35)
        
        repeat_dots = VGroup(
            Dot(repeat_arc.get_start(), radius=0.03, color=RED),
            Dot(repeat_arc.get_end(), radius=0.03, color=RED)
        )
        
        self.play(
            Create(repeat_arc),
            FadeIn(repeat_dots),
            run_time=0.6
        )
        
        # 说明文字
        note = Text(
            "有理数可表示为",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        note2 = Text(
            "有限小数 或 无限循环小数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(note, DOWN, buff=0.2)
        
        self.play(
            FadeIn(note, shift=UP * 0.2),
            FadeIn(note2, shift=UP * 0.2),
            run_time=0.8
        )
        
        # 反例提示
        counter_example = Text(
            "注: π, √2 等是无理数",
            font="Noto Sans CJK SC",
            font_size=20,
            color=RED
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(counter_example, shift=UP * 0.2), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(fractions),
            FadeOut(arrows),
            FadeOut(decimals),
            FadeOut(repeat_arc),
            FadeOut(repeat_dots),
            FadeOut(note),
            FadeOut(note2),
            FadeOut(counter_example),
            run_time=0.6
        )
    
    def show_practice(self):
        """场景6: 实例演练"""
        # 副标题
        subtitle = Text(
            "判断练习",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 判断框
        yes_box = Rectangle(
            width=2.5,
            height=4,
            color=GREEN,
            stroke_width=3
        ).move_to(UP * 1.5 + LEFT * 2)
        
        yes_label = Text(
            "是有理数 ✓",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        ).next_to(yes_box, UP, buff=0.3)
        
        no_box = Rectangle(
            width=2.5,
            height=4,
            color=RED,
            stroke_width=3
        ).move_to(UP * 1.5 + RIGHT * 2)
        
        no_label = Text(
            "不是有理数 ✗",
            font="Noto Sans CJK SC",
            font_size=24,
            color=RED
        ).next_to(no_box, UP, buff=0.3)
        
        self.play(
            Create(yes_box),
            Create(no_box),
            FadeIn(yes_label),
            FadeIn(no_label),
            run_time=0.8
        )
        
        # 测试数字
        test_cases = [
            (r"7", True, "整数"),
            (r"-\frac{3}{5}", True, "分数"),
            (r"0.666...", True, "循环小数"),
            (r"\sqrt{3}", False, "无理数"),
        ]
        
        yes_y_positions = [3, 2, 1, 0]
        no_y_positions = [2.5]
        yes_count = 0
        no_count = 0
        
        for num_text, is_rational, explanation in test_cases:
            # 数字出现
            num = MathTex(num_text, font_size=40, color=WHITE).move_to(UP * 4.5)
            
            self.play(FadeIn(num, shift=DOWN * 0.3), run_time=0.4)
            self.wait(0.3)
            
            # 移动到对应框
            if is_rational:
                target_pos = yes_box.get_center() + UP * (yes_y_positions[yes_count] - 1.5)
                target_color = GREEN
                check = Text("✓", font_size=30, color=GREEN).next_to(num, RIGHT, buff=0.2)
                yes_count += 1
            else:
                target_pos = no_box.get_center() + UP * (no_y_positions[no_count] - 1.5)
                target_color = RED
                check = Text("✗", font_size=30, color=RED).next_to(num, RIGHT, buff=0.2)
                no_count += 1
            
            self.play(
                num.animate.move_to(target_pos).set_color(target_color).scale(0.7),
                run_time=0.6
            )
            
            self.play(FadeIn(check, scale=0.5), run_time=0.3)
            
            # 简短说明
            if not is_rational:
                explain = Text(
                    explanation,
                    font="Noto Sans CJK SC",
                    font_size=18,
                    color=GRAY_A
                ).next_to(num, DOWN, buff=0.2)
                self.play(FadeIn(explain, shift=UP * 0.1), run_time=0.3)
            
            self.wait(0.3)
        
        self.wait(2.0)
        
        # 清理
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != self.author_info and mob != self.title_ref], run_time=0.6)
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 标题
        title = Text(
            "有理数 - 知识要点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_RATIONAL
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=0.8)
        
        # 要点卡片
        point1 = self.create_summary_point(
            "①",
            "整数和分数的统称",
            UP * 3.5,
            self.COLOR_RATIONAL
        )
        
        point2 = self.create_summary_point(
            "②",
            "可表示为 p/q (q≠0)",
            UP * 2.2,
            self.COLOR_RATIONAL
        )
        
        point3 = self.create_summary_point(
            "③",
            "有限或循环小数",
            UP * 0.9,
            self.COLOR_RATIONAL
        )
        
        self.play(FadeIn(point1, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(point2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(point3, shift=RIGHT * 0.3), run_time=0.6)
        
        # 公式回顾
        formula_label = Text(
            "集合表示:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.8 + LEFT * 2.5)
        
        formula = MathTex(
            r"Q = \mathbb{Z} \cup \text{分数}",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(formula_label),
            Write(formula),
            run_time=1.0
        )
        
        self.wait(1.5)
        
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
        ).next_to(author_name, DOWN, buff=0.2)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标
        icons = VGroup(
            Circle(radius=0.2, color=self.COLOR_RATIONAL, fill_opacity=0.8).shift(LEFT * 3 + DOWN * 5),
            Circle(radius=0.2, color=self.COLOR_INTEGER, fill_opacity=0.8).shift(LEFT * 2 + DOWN * 5.3),
            Circle(radius=0.2, color=self.COLOR_FRACTION, fill_opacity=0.8).shift(RIGHT * 2 + DOWN * 5.3),
            Circle(radius=0.2, color=self.COLOR_POSITIVE, fill_opacity=0.8).shift(RIGHT * 3 + DOWN * 5),
        )
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.0)
    
    def create_summary_point(self, number, text, position, color):
        """创建总结要点"""
        # 序号圆
        circle = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        num_text = Text(
            number,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(circle.get_center())
        
        # 内容文字
        content = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        )
        
        # 组合
        group = VGroup(circle, num_text, content).arrange(RIGHT, buff=0.4)
        group.move_to(position)
        
        # 初始位置在左侧外
        group.shift(LEFT * 8)
        
        return group


# 运行命令:
# manim -pql rational_numbers.py RationalNumbers  # 快速预览
# manim -qh rational_numbers.py RationalNumbers   # 高质量渲染
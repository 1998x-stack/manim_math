"""
有理数的乘方 - Manim 教学动画
Power of Rational Numbers - Educational Animation

知识点：六年级数学 - 有理数的乘方
格式：TikTok 竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========== 全局配置 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PowerOfNumbers(Scene):
    """
    有理数的乘方教学动画
    
    场景顺序：
    1. 开场钩子 - 提出问题
    2. 乘方定义 - 基本概念
    3. 具体例子 - 2^4 展开
    4. 0次幂规则 - a^0 = 1
    5. 负数乘方 - 核心重点
    6. 规律总结 - 奇偶性规律
    7. 结尾关注 - 总结与引导
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案（根据验证结果优化对比度）
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要公式
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调/警告
        self.COLOR_HIGHLIGHT = "#f39c12"      # 橙色 - 高亮
        self.COLOR_POSITIVE = "#27ae60"       # 深绿色 - 正数（提高对比度）
        self.COLOR_NEGATIVE = "#ff4757"       # 亮红色 - 负数（提高对比度）
        self.COLOR_AUXILIARY = "#95a5a6"      # 灰色 - 辅助
        
        # 字体大小规范
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "formula": 32,
            "body": 24,
            "small": 20,
            "author": 20,
        }
        
        # 作者信息（全程显示）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["author"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.add(self.author_info)
        
        # 执行场景
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_example()
        self.scene_4_zero_power()
        self.scene_5_negative_power()
        self.scene_6_summary_rules()
        self.scene_7_outro()
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (4秒)"""
        # 钩子问题
        hook_question = Text(
            "这样写太麻烦了！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        # 乘法算式
        multiplication = MathTex(
            r"2 \times 2 \times 2 \times 2",
            font_size=self.FONT_SIZES["formula"] + 8,
            color=WHITE
        ).move_to(UP * 2.5)
        
        # 问号
        question_mark = Text(
            "?",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1)
        
        # 动画
        self.play(Write(hook_question), run_time=1.0)
        self.play(Write(multiplication), run_time=0.8)
        self.play(
            FadeIn(question_mark, scale=2),
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        self.wait(1.0)
        
        # 提示
        hint_text = Text(
            "用乘方可以简化！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.4)
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(multiplication),
            FadeOut(question_mark),
            FadeOut(hint_text),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 乘方定义 (8秒)"""
        # 标题
        title = Text(
            "什么是乘方？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        # 定义
        definition = Text(
            "n 个相同因数 a 相乘",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 4)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        self.play(Write(definition), run_time=1.2)
        
        # 一般形式
        general_form = MathTex(
            r"a^n",
            font_size=60,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Write(general_form), run_time=0.8)
        self.wait(0.3)
        
        # 术语标注
        base_brace = Brace(general_form[0][0], DOWN, buff=0.3, color=self.COLOR_POSITIVE)
        base_label = Text(
            "底数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_POSITIVE
        ).next_to(base_brace, DOWN, buff=0.1)
        
        exponent_brace = Brace(general_form[0][1], UP, buff=0.3, color=self.COLOR_SECONDARY)
        exponent_label = Text(
            "指数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_SECONDARY
        ).next_to(exponent_brace, UP, buff=0.1)
        
        power_label = Text(
            "幂",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(general_form, RIGHT, buff=0.8)
        
        arrow = Arrow(
            power_label.get_left(),
            general_form.get_right(),
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            FadeIn(base_brace),
            FadeIn(base_label),
            run_time=0.6
        )
        self.play(Indicate(general_form[0][0], color=self.COLOR_POSITIVE), run_time=0.4)
        
        self.play(
            FadeIn(exponent_brace),
            FadeIn(exponent_label),
            run_time=0.6
        )
        self.play(Indicate(general_form[0][1], color=self.COLOR_SECONDARY), run_time=0.4)
        
        self.play(
            Create(arrow),
            FadeIn(power_label),
            run_time=0.6
        )
        self.play(Indicate(general_form, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理，保留简化版
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(base_brace),
            FadeOut(base_label),
            FadeOut(exponent_brace),
            FadeOut(exponent_label),
            FadeOut(arrow),
            FadeOut(power_label),
            general_form.animate.scale(0.6).move_to(UP * 6.5 + RIGHT * 3),
            run_time=0.6
        )
        
        self.general_form_small = general_form  # 保留引用
    
    def scene_3_example(self):
        """场景3: 具体例子 2^4 (10秒)"""
        # 左侧：2^4
        power_notation = MathTex(
            r"2^4",
            font_size=self.FONT_SIZES["formula"] + 10,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 3 + UP * 2)
        
        self.play(Write(power_notation), run_time=0.6)
        
        # 等号
        equal_sign = MathTex(
            r"=",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(LEFT * 1.5 + UP * 2)
        
        self.play(FadeIn(equal_sign), run_time=0.3)
        
        # 方块展开（使用验证过的布局）
        box_width = 0.6
        spacing = 0.3
        num_boxes = 4
        total_width = num_boxes * box_width + (num_boxes - 1) * spacing
        
        boxes = VGroup()
        mult_signs = VGroup()
        
        for i in range(num_boxes):
            x = i * (box_width + spacing) - total_width / 2 + RIGHT * 1.5
            
            # 方块
            box = Square(
                side_length=box_width,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.3
            ).move_to(x + UP * 2)
            
            # 数字2
            number = MathTex(r"2", font_size=self.FONT_SIZES["body"]).move_to(box.get_center())
            
            box_group = VGroup(box, number)
            boxes.add(box_group)
            
            # 乘号（除了最后一个）
            if i < num_boxes - 1:
                mult_sign = MathTex(
                    r"\times",
                    font_size=self.FONT_SIZES["small"]
                ).move_to(x + RIGHT * (box_width + spacing) / 2 + UP * 2)
                mult_signs.add(mult_sign)
        
        # 依次显示方块
        for i, box in enumerate(boxes):
            self.play(FadeIn(box, scale=0.5), run_time=0.4)
        
        # 显示乘号
        self.play(Create(mult_signs), run_time=0.6)
        
        # 强调指数4
        exponent_box = SurroundingRectangle(
            power_notation[0][1],
            color=self.COLOR_SECONDARY,
            buff=0.1
        )
        self.play(Create(exponent_box), run_time=0.5)
        
        # 强调4个方块
        boxes_rect = SurroundingRectangle(
            boxes,
            color=self.COLOR_SECONDARY,
            buff=0.2
        )
        self.play(Create(boxes_rect), run_time=0.8)
        self.wait(0.5)
        
        self.play(FadeOut(exponent_box), FadeOut(boxes_rect), run_time=0.3)
        
        # 计算过程
        calculation = Text(
            "4 个 2 相乘",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(calculation), run_time=0.5)
        
        # 显示结果
        result = MathTex(
            r"= 16",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_POSITIVE
        ).move_to(UP * 2 + RIGHT * 3.5)
        
        self.play(Write(result), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(power_notation),
            FadeOut(equal_sign),
            FadeOut(boxes),
            FadeOut(mult_signs),
            FadeOut(calculation),
            FadeOut(result),
            run_time=0.5
        )
    
    def scene_4_zero_power(self):
        """场景4: 0次幂规则 (7秒)"""
        # 规则
        zero_power_rule = MathTex(
            r"a^0 = 1",
            font_size=self.FONT_SIZES["formula"] + 10,
            color=WHITE
        ).move_to(UP * 3)
        
        # 条件
        condition = MathTex(
            r"(a \neq 0)",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SECONDARY
        ).next_to(zero_power_rule, RIGHT, buff=0.5)
        
        self.play(Write(zero_power_rule), run_time=0.8)
        self.play(
            FadeIn(condition),
            Indicate(condition, color=self.COLOR_SECONDARY),
            run_time=0.6
        )
        
        # 例子
        example1 = MathTex(
            r"5^0 = 1",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        example2 = MathTex(
            r"(-3)^0 = 1",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        self.play(Write(example1), run_time=0.5)
        self.play(Write(example2), run_time=0.5)
        
        # 强调
        self.play(
            Flash(zero_power_rule, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=0.4
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(zero_power_rule),
            FadeOut(condition),
            FadeOut(example1),
            FadeOut(example2),
            run_time=0.5
        )
    
    def scene_5_negative_power(self):
        """场景5: 负数的乘方 - 核心重点 (15秒)"""
        # 警告标题
        warning_title = Text(
            "⚠️ 注意！负号的位置",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        self.play(Write(warning_title), run_time=0.8)
        
        # 左框：带括号的负数
        left_box = Rectangle(
            width=4,
            height=5,
            color=self.COLOR_PRIMARY,
            stroke_width=2
        ).move_to(LEFT * 2.2 + UP * 1.5)
        
        left_title = Text(
            "负数的乘方",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_PRIMARY
        ).next_to(left_box, UP, buff=0.2)
        
        # 右框：负号在外
        right_box = Rectangle(
            width=4,
            height=5,
            color=self.COLOR_SECONDARY,
            stroke_width=2
        ).move_to(RIGHT * 2.2 + UP * 1.5)
        
        right_title = Text(
            "负号在外面",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_SECONDARY
        ).next_to(right_box, UP, buff=0.2)
        
        self.play(
            Create(left_box),
            FadeIn(left_title),
            Create(right_box),
            FadeIn(right_title),
            run_time=0.5
        )
        
        # 左侧：(-2)^2
        formula1 = MathTex(
            r"(-2)^2",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(left_box.get_center() + UP * 1.5)
        
        expansion1 = MathTex(
            r"= (-2) \times (-2)",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(left_box.get_center() + UP * 0.5)
        
        result1 = MathTex(
            r"= +4",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_POSITIVE
        ).move_to(left_box.get_center() + DOWN * 0.3)
        
        note1 = Text(
            "偶次幂",
            font="Noto Sans CJK SC",
            font_size=16,
            color=self.COLOR_POSITIVE
        ).next_to(result1, DOWN, buff=0.2)
        
        self.play(Write(formula1), run_time=0.6)
        self.play(Write(expansion1), run_time=0.8)
        self.play(Write(result1), FadeIn(note1), run_time=0.5)
        self.wait(0.5)
        
        # 左侧：(-2)^3
        formula2 = MathTex(
            r"(-2)^3",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(left_box.get_center() + DOWN * 1.5)
        
        expansion2 = MathTex(
            r"= (-2) \times (-2) \times (-2)",
            font_size=14,
            color=GRAY_A
        ).move_to(left_box.get_center() + DOWN * 2.3)
        
        result2 = MathTex(
            r"= -8",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_NEGATIVE
        ).move_to(left_box.get_center() + DOWN * 3.0)
        
        note2 = Text(
            "奇次幂",
            font="Noto Sans CJK SC",
            font_size=16,
            color=self.COLOR_NEGATIVE
        ).next_to(result2, DOWN, buff=0.2)
        
        self.play(Write(formula2), run_time=0.6)
        self.play(Write(expansion2), run_time=0.8)
        self.play(Write(result2), FadeIn(note2), run_time=0.5)
        self.wait(0.5)
        
        # 右侧：-2^2
        formula3 = MathTex(
            r"-2^2",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(right_box.get_center() + UP * 1)
        
        # 强调负号在外
        minus_highlight = SurroundingRectangle(
            formula3[0][0],
            color=self.COLOR_SECONDARY,
            buff=0.05
        )
        
        expansion3 = MathTex(
            r"= -(2 \times 2)",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(right_box.get_center() + UP * 0.1)
        
        result3 = MathTex(
            r"= -4",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_NEGATIVE
        ).move_to(right_box.get_center() + DOWN * 0.8)
        
        note3 = Text(
            "负号不参与乘方",
            font="Noto Sans CJK SC",
            font_size=16,
            color=self.COLOR_SECONDARY
        ).next_to(result3, DOWN, buff=0.2)
        
        self.play(Write(formula3), run_time=0.6)
        self.play(Create(minus_highlight), run_time=0.5)
        self.play(Write(expansion3), run_time=0.6)
        self.play(Write(result3), FadeIn(note3), run_time=0.5)
        
        # 对比闪烁
        comparison_group = VGroup(result1, result3)
        self.play(
            Flash(result1, color=self.COLOR_POSITIVE, flash_radius=0.5),
            Flash(result3, color=self.COLOR_NEGATIVE, flash_radius=0.5),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(warning_title),
            FadeOut(left_box),
            FadeOut(left_title),
            FadeOut(right_box),
            FadeOut(right_title),
            FadeOut(formula1),
            FadeOut(expansion1),
            FadeOut(result1),
            FadeOut(note1),
            FadeOut(formula2),
            FadeOut(expansion2),
            FadeOut(result2),
            FadeOut(note2),
            FadeOut(formula3),
            FadeOut(minus_highlight),
            FadeOut(expansion3),
            FadeOut(result3),
            FadeOut(note3),
            run_time=0.6
        )
    
    def scene_6_summary_rules(self):
        """场景6: 规律总结 (10秒)"""
        # 标题
        title = Text(
            "负数乘方的规律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 规则1：偶次幂
        rule1 = VGroup(
            Text(
                "偶次幂：",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SIZES["body"],
                color=WHITE
            ),
            VGroup(
                MathTex(r"(-a)^n", font_size=self.FONT_SIZES["body"], color=self.COLOR_POSITIVE),
                Text("(n偶数) = 正数", font="Noto Sans CJK SC",
                    font_size=self.FONT_SIZES["body"], color=self.COLOR_POSITIVE)
            ).arrange(RIGHT, buff=0.2).shift(RIGHT * 0.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        positive_icon = Text(
            "✓",
            font_size=40,
            color=self.COLOR_POSITIVE
        ).next_to(rule1, RIGHT, buff=0.5)
        
        self.play(FadeIn(rule1), run_time=0.8)
        self.play(FadeIn(positive_icon, scale=2), run_time=0.4)
        
        # 规则2：奇次幂
        rule2 = VGroup(
            Text(
                "奇次幂：",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SIZES["body"],
                color=WHITE
            ),
            VGroup(
                MathTex(r"(-a)^n", font_size=self.FONT_SIZES["body"], color=self.COLOR_NEGATIVE),
                Text("(n奇数) = 负数", font="Noto Sans CJK SC",
                    font_size=self.FONT_SIZES["body"], color=self.COLOR_NEGATIVE)
            ).arrange(RIGHT, buff=0.2).shift(RIGHT * 0.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2)
        
        negative_icon = Text(
            "✓",
            font_size=40,
            color=self.COLOR_NEGATIVE
        ).next_to(rule2, RIGHT, buff=0.5)
        
        self.play(FadeIn(rule2), run_time=0.8)
        self.play(FadeIn(negative_icon, scale=2), run_time=0.4)
        
        # 强调框
        highlight_box = SurroundingRectangle(
            VGroup(rule1, rule2),
            color=self.COLOR_HIGHLIGHT,
            buff=0.4,
            corner_radius=0.1
        )
        
        self.play(Create(highlight_box), run_time=0.6)
        
        # 记忆提示
        memory_tip = Text(
            "记住：偶正奇负！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(memory_tip, shift=UP * 0.3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule1),
            FadeOut(positive_icon),
            FadeOut(rule2),
            FadeOut(negative_icon),
            FadeOut(highlight_box),
            FadeOut(memory_tip),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 结尾总结与关注 (6秒)"""
        # 总结卡片
        summary_title = Text(
            "今天学了什么？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        
        # 要点
        points = VGroup(
            Text("✓ 乘方的定义：aⁿ", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
            Text("✓ 0次幂规则：a⁰ = 1", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
            Text("✓ 负数乘方：偶正奇负", font="Noto Sans CJK SC", font_size=22, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 2.5)
        
        for point in points:
            self.play(Write(point), run_time=0.4)
        
        self.wait(0.6)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_B
        ).move_to(DOWN * 1.5)
        
        self.play(
            self.author_info.animate.move_to(DOWN * 0.5).scale(1.8),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰动画
        decorations = VGroup(*[
            Circle(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(dec, scale=0.5) for dec in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(points),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            FadeOut(self.general_form_small) if hasattr(self, 'general_form_small') else Wait(0),
            run_time=1.0
        )


# ========== 渲染命令 ==========
# 快速预览：manim -pql power_of_numbers.py PowerOfNumbers
# 高质量：  manim -qh power_of_numbers.py PowerOfNumbers
# 4K质量：  manim -qk power_of_numbers.py PowerOfNumbers
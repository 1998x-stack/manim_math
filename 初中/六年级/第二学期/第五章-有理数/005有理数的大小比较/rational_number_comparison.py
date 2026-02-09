"""
有理数的大小比较 - Rational Number Comparison
使用 Manim 创建的六年级数学教学视频

内容: 有理数大小比较的四条规则
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


class RationalNumberComparison(Scene):
    """
    有理数大小比较教学动画场景

    场景顺序:
    1. 开场介绍
    2. 规则1: 正数>0>负数
    3. 规则2: 两个正数比较
    4. 规则3: 两个负数比较
    5. 规则4: 数轴法则
    6. 综合示例
    7. 片尾关注
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 对比元素
        self.COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正数
        self.COLOR_NEGATIVE = "#e74c3c"     # 红色 - 负数
        self.COLOR_ZERO = "#95a5a6"         # 灰色 - 零
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 辅助线条

        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"

        # 执行动画序列
        self.show_opening()
        self.show_rule1_positive_negative()
        self.show_rule2_positive_comparison()
        self.show_rule3_negative_comparison()
        self.show_rule4_number_line()
        self.show_comprehensive_example()
        self.show_outro()

    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 钩子问题
        hook_text = Text(
            "哪个数更大？",
            font=self.FONT_CHINESE,
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(hook_text), run_time=0.8)

        # 三个示例数字
        num_3 = MathTex("3", font_size=52, color=self.COLOR_POSITIVE).move_to(UP * 3.5 + LEFT * 2.5)
        num_neg5 = MathTex("-5", font_size=52, color=self.COLOR_NEGATIVE).move_to(UP * 3.5)
        num_0 = MathTex("0", font_size=52, color=self.COLOR_ZERO).move_to(UP * 3.5 + RIGHT * 2.5)

        self.play(
            FadeIn(num_3, scale=0.5),
            run_time=0.4
        )
        self.play(
            FadeIn(num_neg5, scale=0.5),
            run_time=0.4
        )
        self.play(
            FadeIn(num_0, scale=0.5),
            run_time=0.4
        )

        # 疑问符号
        question_mark = Text("?", font_size=80, color=self.COLOR_HIGHLIGHT).move_to(UP * 2)
        self.play(FadeIn(question_mark, scale=0.3), run_time=0.3)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)

        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(num_3),
            FadeOut(num_neg5),
            FadeOut(num_0),
            FadeOut(question_mark),
            run_time=0.5
        )

    def show_rule1_positive_negative(self):
        """场景2: 规则1 - 正数>0>负数"""
        # 标题
        title = Text(
            "规则1: 正数 > 0 > 负数",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)

        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)

        # 创建数轴
        self.number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=8,
            include_numbers=True,
            numbers_to_include=list(range(-5, 6)),
            font_size=18,
            label_direction=DOWN,
            color=WHITE
        ).move_to(UP * 1.5)

        self.play(Create(self.number_line), run_time=1.2)

        # 零点标记
        zero_pos = self.number_line.n2p(0)
        zero_dot = Dot(zero_pos, radius=0.12, color=self.COLOR_ZERO)
        zero_label = Text("零", font=self.FONT_CHINESE, font_size=22, color=self.COLOR_ZERO).next_to(zero_dot, UP, buff=0.2)

        self.play(
            FadeIn(zero_dot, scale=0.5),
            FadeIn(zero_label),
            run_time=0.5
        )

        # 负数区域 (左侧阴影)
        negative_region = Rectangle(
            width=4,
            height=1.2,
            fill_color=self.COLOR_NEGATIVE,
            fill_opacity=0.15,
            stroke_width=0
        ).move_to(self.number_line.n2p(-2.5) + UP * 0)

        negative_label = Text(
            "负数",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_NEGATIVE
        ).move_to(self.number_line.n2p(-3) + DOWN * 0.8)

        self.play(
            FadeIn(negative_region),
            FadeIn(negative_label),
            run_time=0.6
        )

        # 正数区域 (右侧阴影)
        positive_region = Rectangle(
            width=4,
            height=1.2,
            fill_color=self.COLOR_POSITIVE,
            fill_opacity=0.15,
            stroke_width=0
        ).move_to(self.number_line.n2p(2.5) + UP * 0)

        positive_label = Text(
            "正数",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_POSITIVE
        ).move_to(self.number_line.n2p(3) + DOWN * 0.8)

        self.play(
            FadeIn(positive_region),
            FadeIn(positive_label),
            run_time=0.6
        )

        # 方向箭头 (右侧大)
        direction_arrow = Arrow(
            self.number_line.n2p(-4),
            self.number_line.n2p(4),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6,
            buff=0
        ).shift(DOWN * 1.8)

        arrow_label = Text(
            "数值增大",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(direction_arrow, DOWN, buff=0.2)

        self.play(
            GrowArrow(direction_arrow),
            FadeIn(arrow_label),
            run_time=0.8
        )

        # 示例
        example = MathTex(
            "3", ">", "0", ">", "-5",
            font_size=36
        ).move_to(DOWN * 3.5)
        example[0].set_color(self.COLOR_POSITIVE)
        example[2].set_color(self.COLOR_ZERO)
        example[4].set_color(self.COLOR_NEGATIVE)

        self.play(Write(example), run_time=1.0)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(negative_region),
            FadeOut(negative_label),
            FadeOut(positive_region),
            FadeOut(positive_label),
            FadeOut(direction_arrow),
            FadeOut(arrow_label),
            FadeOut(example),
            FadeOut(zero_dot),
            FadeOut(zero_label),
            run_time=0.6
        )

    def show_rule2_positive_comparison(self):
        """场景3: 规则2 - 两个正数比较"""
        # 标题
        title = Text(
            "规则2: 正数比大小 = 比绝对值",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)

        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)

        # 在数轴上标记 3 和 5
        pos_3 = self.number_line.n2p(3)
        pos_5 = self.number_line.n2p(5)

        dot_3 = Dot(pos_3, radius=0.15, color=self.COLOR_POSITIVE)
        label_3 = MathTex("3", font_size=32, color=self.COLOR_POSITIVE).next_to(dot_3, UP, buff=0.3)

        dot_5 = Dot(pos_5, radius=0.15, color=self.COLOR_POSITIVE)
        label_5 = MathTex("5", font_size=32, color=self.COLOR_POSITIVE).next_to(dot_5, UP, buff=0.3)

        self.play(
            FadeIn(dot_3, scale=0.5),
            FadeIn(label_3),
            run_time=0.5
        )
        self.play(
            FadeIn(dot_5, scale=0.5),
            FadeIn(label_5),
            run_time=0.5
        )

        # 绝对值表达式
        abs_expr = MathTex(
            r"|3| = 3, \quad |5| = 5",
            font_size=32
        ).move_to(DOWN * 0.5)

        self.play(Write(abs_expr), run_time=1.0)

        # 比较
        comparison = MathTex(
            r"5 > 3",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)

        self.play(Write(comparison), run_time=0.8)

        # 高亮 5 在 3 右侧
        self.play(
            Indicate(dot_5, scale_factor=1.5, color=self.COLOR_HIGHLIGHT),
            Indicate(label_5, scale_factor=1.3),
            run_time=0.8
        )

        # 结论
        conclusion = Text(
            "绝对值大的数大",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(dot_3),
            FadeOut(label_3),
            FadeOut(dot_5),
            FadeOut(label_5),
            FadeOut(abs_expr),
            FadeOut(comparison),
            FadeOut(conclusion),
            run_time=0.6
        )

    def show_rule3_negative_comparison(self):
        """场景4: 规则3 - 两个负数比较"""
        # 标题
        title = Text(
            "规则3: 负数比大小 = 绝对值反向",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)

        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)

        # 在数轴上标记 -2 和 -4
        pos_neg2 = self.number_line.n2p(-2)
        pos_neg4 = self.number_line.n2p(-4)

        dot_neg2 = Dot(pos_neg2, radius=0.15, color=self.COLOR_NEGATIVE)
        label_neg2 = MathTex("-2", font_size=32, color=self.COLOR_NEGATIVE).next_to(dot_neg2, UP, buff=0.3)

        dot_neg4 = Dot(pos_neg4, radius=0.15, color=self.COLOR_NEGATIVE)
        label_neg4 = MathTex("-4", font_size=32, color=self.COLOR_NEGATIVE).next_to(dot_neg4, UP, buff=0.3)

        self.play(
            FadeIn(dot_neg2, scale=0.5),
            FadeIn(label_neg2),
            run_time=0.5
        )
        self.play(
            FadeIn(dot_neg4, scale=0.5),
            FadeIn(label_neg4),
            run_time=0.5
        )

        # 绝对值表达式
        abs_expr = MathTex(
            r"|-2| = 2, \quad |-4| = 4",
            font_size=32
        ).move_to(DOWN * 0.5)

        self.play(Write(abs_expr), run_time=1.0)

        # 绝对值比较
        abs_comparison = MathTex(
            r"4 > 2",
            font_size=32
        ).move_to(DOWN * 1.8)
        abs_comparison_text = Text(
            "(绝对值)",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_A
        ).next_to(abs_comparison, RIGHT, buff=0.2)

        self.play(
            Write(abs_comparison),
            FadeIn(abs_comparison_text),
            run_time=0.8
        )

        # 关键提示
        hint = Text(
            "⚠️ 绝对值大的反而小！",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.2)

        self.play(
            FadeIn(hint, scale=1.2),
            Flash(hint, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=0.8
        )

        # 结论
        conclusion = MathTex(
            r"-2 > -4",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)

        self.play(Write(conclusion), run_time=0.8)

        # 用箭头指示 -2 在 -4 右侧
        arrow = Arrow(
            pos_neg4 + DOWN * 0.8,
            pos_neg2 + DOWN * 0.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            buff=0.1
        )
        arrow_label = Text(
            "右边大",
            font=self.FONT_CHINESE,
            font_size=18,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow, DOWN, buff=0.1)

        self.play(
            GrowArrow(arrow),
            FadeIn(arrow_label),
            run_time=0.8
        )

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(dot_neg2),
            FadeOut(label_neg2),
            FadeOut(dot_neg4),
            FadeOut(label_neg4),
            FadeOut(abs_expr),
            FadeOut(abs_comparison),
            FadeOut(abs_comparison_text),
            FadeOut(hint),
            FadeOut(conclusion),
            FadeOut(arrow),
            FadeOut(arrow_label),
            run_time=0.6
        )

    def show_rule4_number_line(self):
        """场景5: 规则4 - 数轴法则"""
        # 标题
        title = Text(
            "规则4: 数轴上，右边 > 左边",
            font=self.FONT_CHINESE,
            font_size=30,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)

        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)

        # 在数轴上标记多个点
        values = [-3, -1, 0, 2, 4]
        colors = [self.COLOR_NEGATIVE, self.COLOR_NEGATIVE, self.COLOR_ZERO,
                  self.COLOR_POSITIVE, self.COLOR_POSITIVE]

        dots = []
        labels = []

        for val, col in zip(values, colors):
            pos = self.number_line.n2p(val)
            dot = Dot(pos, radius=0.12, color=col)
            label = MathTex(str(val), font_size=28, color=col).next_to(dot, UP, buff=0.3)
            dots.append(dot)
            labels.append(label)

        # 依次出现
        self.play(
            LaggedStart(
                *[FadeIn(dot, scale=0.5) for dot in dots],
                *[FadeIn(label) for label in labels],
                lag_ratio=0.15
            ),
            run_time=2.0
        )

        # 右侧箭头强调
        right_arrow = Arrow(
            self.number_line.n2p(-4),
            self.number_line.n2p(5),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6,
            buff=0.3
        ).shift(DOWN * 0.8)

        arrow_text = Text(
            "越往右，数值越大",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(right_arrow, DOWN, buff=0.2)

        self.play(
            GrowArrow(right_arrow),
            FadeIn(arrow_text),
            run_time=1.0
        )

        # 从左到右扫描动画
        scanner_line = Line(
            self.number_line.n2p(-5) + UP * 1,
            self.number_line.n2p(-5) + DOWN * 1,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )

        self.play(
            scanner_line.animate.move_to(self.number_line.n2p(5)),
            run_time=3.0,
            rate_func=linear
        )

        # 示例比较
        examples = VGroup(
            MathTex(r"-3 < -1 < 0 < 2 < 4", font_size=32),
        ).move_to(DOWN * 3)

        self.play(Write(examples), run_time=1.2)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            *[FadeOut(dot) for dot in dots],
            *[FadeOut(label) for label in labels],
            FadeOut(right_arrow),
            FadeOut(arrow_text),
            FadeOut(scanner_line),
            FadeOut(examples),
            run_time=0.6
        )

    def show_comprehensive_example(self):
        """场景6: 综合示例"""
        # 标题
        title = Text(
            "综合练习",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)

        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)

        # 题目
        question = Text(
            "比较以下数字的大小：",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).move_to(UP * 5)

        numbers_text = Text(
            "-3,  5,  0,  -1,  2",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 4.2)

        self.play(
            Write(question),
            run_time=0.6
        )
        self.play(
            Write(numbers_text),
            run_time=0.8
        )

        # 数字对象 (用于动画移动)
        values = [-3, 5, 0, -1, 2]
        colors = [self.COLOR_NEGATIVE, self.COLOR_POSITIVE, self.COLOR_ZERO,
                  self.COLOR_NEGATIVE, self.COLOR_POSITIVE]

        # 随机初始位置
        initial_positions = [
            UP * 2 + LEFT * 3,
            UP * 2 + RIGHT * 3,
            UP * 2 + LEFT * 1,
            UP * 2 + RIGHT * 1,
            UP * 2
        ]

        number_mobjects = []
        for val, col, init_pos in zip(values, colors, initial_positions):
            num = MathTex(str(val), font_size=40, color=col).move_to(init_pos)
            number_mobjects.append(num)

        # 数字随机散布出现
        self.play(
            AnimationGroup(
                *[FadeIn(num, shift=np.random.randn(3) * 0.3) for num in number_mobjects],
                lag_ratio=0.1
            ),
            run_time=1.5
        )

        self.wait(0.8)

        # 数字移动到数轴位置
        target_positions = [self.number_line.n2p(val) + UP * 0.5 for val in values]

        self.play(
            LaggedStart(
                *[num.animate.move_to(pos) for num, pos in zip(number_mobjects, target_positions)],
                lag_ratio=0.15
            ),
            run_time=2.0
        )

        # 在数轴上添加点
        dots_on_line = []
        for val, col in zip(values, colors):
            dot = Dot(self.number_line.n2p(val), radius=0.1, color=col)
            dots_on_line.append(dot)

        self.play(
            *[FadeIn(dot, scale=0.5) for dot in dots_on_line],
            run_time=0.6
        )

        # 从小到大排序
        sorted_label = Text(
            "从小到大排序：",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 3)

        self.play(FadeIn(sorted_label, shift=UP * 0.2), run_time=0.5)

        # 答案
        answer = MathTex(
            r"-3 < -1 < 0 < 2 < 5",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)

        self.play(Write(answer), run_time=1.5)

        # 闪烁效果
        self.play(
            Flash(answer, color=self.COLOR_HIGHLIGHT, flash_radius=1.0),
            run_time=0.5
        )

        self.wait(2.0)

        # 清理所有元素
        all_objects = VGroup(
            title, question, numbers_text, sorted_label, answer,
            *number_mobjects, *dots_on_line, self.number_line
        )

        self.play(FadeOut(all_objects), run_time=0.8)

    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)

        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.8)

        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=self.FONT_CHINESE,
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 四条规则快速回顾卡片
        rules_title = Text(
            "四条比较规则回顾",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 2)

        self.play(FadeIn(rules_title), run_time=0.5)

        # 规则卡片
        rule_cards = [
            "① 正数 > 0 > 负数",
            "② 正数比绝对值",
            "③ 负数反向比",
            "④ 数轴右边大"
        ]

        cards = VGroup()
        for i, rule in enumerate(rule_cards):
            card_text = Text(
                rule,
                font=self.FONT_CHINESE,
                font_size=22,
                color=WHITE
            ).move_to(DOWN * (3.2 + i * 0.6))
            card_text.shift(LEFT * 10)  # 初始在左侧外
            cards.add(card_text)

        # 卡片依次滑入
        for card in cards:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)

        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(rules_title),
            FadeOut(cards),
            run_time=1.0
        )


# 运行命令:
# manim -pql rational_number_comparison.py RationalNumberComparison  # 快速预览
# manim -qh rational_number_comparison.py RationalNumberComparison   # 高质量渲染

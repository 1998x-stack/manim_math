"""
平均数教学动画 - Average (Mean) Educational Animation
使用 Manim 创建的初中统计学教学视频

内容: 算术平均数、加权平均数、极端值影响
目标观众: 初中学生
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


class AverageMean(Scene):
    """
    平均数教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 算术平均数概念
    3. 算术平均数计算
    4. 加权平均数
    5. 极端值影响
    6. 总结对比
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ARITHMETIC_MEAN = "#3498db"   # 蓝色 - 算术平均数
        self.COLOR_WEIGHTED_MEAN = "#e74c3c"     # 红色 - 加权平均数
        self.COLOR_DATA_POINT = "#2ecc71"        # 绿色 - 数据点
        self.COLOR_EXTREME = "#f39c12"           # 橙色 - 极端值
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化数据
        self.setup_data()
        
        # 执行动画序列
        self.show_opening()
        self.show_arithmetic_mean_concept()
        self.show_arithmetic_mean_calculation()
        self.show_weighted_mean()
        self.show_extreme_value_effect()
        self.show_summary()
        self.show_outro()
    
    def setup_data(self):
        """初始化所有数据"""
        # 算术平均数示例数据
        self.simple_data = [6, 7, 8, 9, 10]
        self.simple_mean = sum(self.simple_data) / len(self.simple_data)
        
        # 加权平均数示例数据
        self.weighted_scores = [80, 85, 90]
        self.weights = [0.3, 0.3, 0.4]
        self.weight_labels = ["30%", "30%", "40%"]
        self.score_labels = ["平时", "期中", "期末"]
        
        # 极端值对比数据
        self.normal_data = [6, 7, 8, 9, 10]
        self.extreme_data = [6, 7, 8, 9, 50]
        self.normal_mean = sum(self.normal_data) / len(self.normal_data)
        self.extreme_mean = sum(self.extreme_data) / len(self.extreme_data)
        
        # 验证数据
        self.verify_data()
    
    def verify_data(self):
        """验证数据计算正确性"""
        # 验证算术平均数
        expected_simple_mean = 8.0
        if abs(self.simple_mean - expected_simple_mean) > 0.01:
            print(f"WARNING: 算术平均数计算错误: {self.simple_mean} ≠ {expected_simple_mean}")
        
        # 验证加权平均数
        weighted_mean = sum(s * w for s, w in zip(self.weighted_scores, self.weights))
        expected_weighted = 85.5
        if abs(weighted_mean - expected_weighted) > 0.01:
            print(f"WARNING: 加权平均数计算错误: {weighted_mean} ≠ {expected_weighted}")
        
        # 验证极端值影响
        if abs(self.normal_mean - 8.0) > 0.01:
            print(f"WARNING: 正常数据平均数错误: {self.normal_mean} ≠ 8.0")
        
        if abs(self.extreme_mean - 16.0) > 0.01:
            print(f"WARNING: 极端数据平均数错误: {self.extreme_mean} ≠ 16.0")
        
        print("✓ 数据验证完成")
    
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
        question = Text(
            "班级平均分是多少？",
            font="Noto Sans CJK SC",
            font_size=44,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(question), run_time=0.8)
        
        # 5个学生成绩卡片
        scores = [75, 82, 88, 79, 91]
        cards = VGroup()
        
        for i, score in enumerate(scores):
            card = VGroup(
                RoundedRectangle(
                    width=1.2,
                    height=1.5,
                    corner_radius=0.1,
                    fill_opacity=0.2,
                    fill_color=self.COLOR_DATA_POINT,
                    stroke_width=2,
                    stroke_color=self.COLOR_DATA_POINT
                ),
                Text(
                    f"{score}",
                    font="Noto Sans CJK SC",
                    font_size=36,
                    color=WHITE,
                    weight=BOLD
                ),
                Text(
                    f"学生{i+1}",
                    font="Noto Sans CJK SC",
                    font_size=18,
                    color=GRAY_A
                ).shift(DOWN * 0.4)
            )
            card[1].move_to(card[0].get_center() + UP * 0.15)
            cards.add(card)
        
        cards.arrange(RIGHT, buff=0.3).move_to(UP * 3)
        
        self.play(FadeIn(cards, lag_ratio=0.2), run_time=1.0)
        
        # 高亮数字
        self.play(*[Indicate(card[1]) for card in cards], run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(question),
            FadeOut(cards),
            run_time=0.5
        )
    
    def show_arithmetic_mean_concept(self):
        """场景2: 算术平均数概念"""
        # 标题
        title = Text(
            "算术平均数",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ARITHMETIC_MEAN,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 说明
        subtitle = Text(
            "所有数据的平均水平",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 创建数轴
        number_line = NumberLine(
            x_range=[5, 11, 1],
            length=7,
            include_numbers=True,
            font_size=20,
            label_direction=DOWN,
            color=GRAY_B
        ).move_to(UP * 3)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 数据点
        dots = VGroup()
        labels = VGroup()
        
        for value in self.simple_data:
            dot = Dot(
                number_line.n2p(value),
                radius=0.12,
                color=self.COLOR_DATA_POINT,
                fill_opacity=1
            )
            dots.add(dot)
            
            label = Text(
                str(value),
                font="Noto Sans CJK SC",
                font_size=22,
                color=WHITE
            ).next_to(dot, UP, buff=0.3)
            labels.add(label)
        
        self.play(FadeIn(dots, lag_ratio=0.2), run_time=1.0)
        self.play(FadeIn(labels, lag_ratio=0.2), run_time=0.5)
        
        # 平衡点概念 - 支点
        fulcrum = Triangle(
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=1
        ).scale(0.3).rotate(PI).move_to(number_line.n2p(self.simple_mean) + DOWN * 0.5)
        
        balance_label = Text(
            "平衡点",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(fulcrum, DOWN, buff=0.2)
        
        self.play(FadeIn(fulcrum), FadeIn(balance_label), run_time=1.0)
        
        # 平均值标记
        mean_line = DashedLine(
            number_line.n2p(self.simple_mean) + UP * 1.5,
            number_line.n2p(self.simple_mean) + DOWN * 0.3,
            color=self.COLOR_ARITHMETIC_MEAN,
            stroke_width=3,
            dash_length=0.1
        )
        
        mean_label = VGroup(
            Text(
                "平均值",
                font="Noto Sans CJK SC",
                font_size=22,
                color=self.COLOR_ARITHMETIC_MEAN
            ),
            Text(
                f"{self.simple_mean}",
                font="Noto Sans CJK SC",
                font_size=26,
                color=self.COLOR_ARITHMETIC_MEAN,
                weight=BOLD
            )
        ).arrange(DOWN, buff=0.1).next_to(mean_line, UP, buff=0.2)
        
        self.play(Create(mean_line), run_time=0.8)
        self.play(FadeIn(mean_label), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 1)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(number_line),
            FadeOut(dots),
            FadeOut(labels),
            FadeOut(fulcrum),
            FadeOut(balance_label),
            FadeOut(mean_line),
            FadeOut(mean_label),
            FadeOut(formula),
            title.animate.move_to(UP * 7).scale(0.7),
            run_time=0.6
        )
        
        self.title_small = title
    
    def show_arithmetic_mean_calculation(self):
        """场景3: 算术平均数计算"""
        # 副标题
        subtitle = Text(
            "计算步骤",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 6)
        
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 数据
        data_text = Text(
            "数据: 6, 7, 8, 9, 10",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(data_text), run_time=0.8)
        
        # 步骤1: 求和
        step1 = VGroup(
            Text(
                "第一步：求和",
                font="Noto Sans CJK SC",
                font_size=24,
                color=self.COLOR_HIGHLIGHT
            ),
            MathTex(
                r"6 + 7 + 8 + 9 + 10 = 40",
                font_size=28,
                color=WHITE
            ).shift(DOWN * 0.4)
        ).arrange(DOWN, buff=0.3).move_to(UP * 2.5)
        
        self.play(FadeIn(step1[0]), run_time=0.6)
        self.play(Write(step1[1]), run_time=1.2)
        
        # 步骤2: 计数
        step2 = VGroup(
            Text(
                "第二步：数据个数",
                font="Noto Sans CJK SC",
                font_size=24,
                color=self.COLOR_HIGHLIGHT
            ),
            MathTex(
                r"n = 5",
                font_size=28,
                color=WHITE
            ).shift(DOWN * 0.4)
        ).arrange(DOWN, buff=0.3).move_to(UP * 0.8)
        
        self.play(FadeIn(step2[0]), run_time=0.6)
        self.play(Write(step2[1]), run_time=0.6)
        
        # 步骤3: 除法
        step3 = VGroup(
            Text(
                "第三步：相除",
                font="Noto Sans CJK SC",
                font_size=24,
                color=self.COLOR_HIGHLIGHT
            ),
            MathTex(
                r"\bar{x} = \frac{40}{5} = 8",
                font_size=32,
                color=self.COLOR_ARITHMETIC_MEAN
            ).shift(DOWN * 0.4)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.8)
        
        self.play(FadeIn(step3[0]), run_time=0.6)
        self.play(Write(step3[1]), run_time=0.8)
        
        # 结果高亮
        result_box = SurroundingRectangle(
            step3[1],
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(result_box), run_time=0.5)
        
        # 答案说明
        answer_text = Text(
            "平均数是 8",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ARITHMETIC_MEAN,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(answer_text, shift=UP * 0.3), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(data_text),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(result_box),
            FadeOut(answer_text),
            FadeOut(self.title_small),
            run_time=0.6
        )
    
    def show_weighted_mean(self):
        """场景4: 加权平均数"""
        # 标题
        title = Text(
            "加权平均数",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_WEIGHTED_MEAN,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 场景说明
        context = Text(
            "考试成绩：不同部分有不同的重要性",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(context), run_time=0.6)
        
        # 成绩卡片
        score_cards = VGroup()
        
        for i, (label, score, weight) in enumerate(zip(
            self.score_labels, self.weighted_scores, self.weight_labels
        )):
            card = VGroup(
                RoundedRectangle(
                    width=2,
                    height=2,
                    corner_radius=0.15,
                    fill_opacity=0.2,
                    fill_color=self.COLOR_WEIGHTED_MEAN,
                    stroke_width=3,
                    stroke_color=self.COLOR_WEIGHTED_MEAN
                ),
                Text(
                    label,
                    font="Noto Sans CJK SC",
                    font_size=22,
                    color=GRAY_A
                ).shift(UP * 0.5),
                Text(
                    f"{score}分",
                    font="Noto Sans CJK SC",
                    font_size=32,
                    color=WHITE,
                    weight=BOLD
                ).shift(UP * 0.05),
                VGroup(
                    Text(
                        "权重",
                        font="Noto Sans CJK SC",
                        font_size=18,
                        color=self.COLOR_HIGHLIGHT
                    ),
                    Text(
                        weight,
                        font="Noto Sans CJK SC",
                        font_size=24,
                        color=self.COLOR_HIGHLIGHT,
                        weight=BOLD
                    ).shift(DOWN * 0.25)
                ).shift(DOWN * 0.55)
            )
            score_cards.add(card)
        
        score_cards.arrange(RIGHT, buff=0.4).move_to(UP * 3.5)
        
        self.play(FadeIn(score_cards, lag_ratio=0.2), run_time=1.2)
        
        # 权重说明
        weight_explain = Text(
            "权重表示重要程度",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(weight_explain), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\bar{x} = \frac{x_1 f_1 + x_2 f_2 + x_3 f_3}{f_1 + f_2 + f_3}",
            font_size=26,
            color=WHITE
        ).move_to(UP * 0.8)
        
        self.play(Write(formula), run_time=1.2)
        
        # 计算过程
        calc_steps = VGroup(
            MathTex(
                r"= \frac{80 \times 0.3 + 85 \times 0.3 + 90 \times 0.4}{0.3 + 0.3 + 0.4}",
                font_size=22,
                color=WHITE
            ),
            MathTex(
                r"= \frac{24 + 25.5 + 36}{1}",
                font_size=24,
                color=WHITE
            ),
            MathTex(
                r"= 85.5",
                font_size=28,
                color=self.COLOR_WEIGHTED_MEAN
            )
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 0.8)
        
        for step in calc_steps:
            self.play(Write(step), run_time=0.8)
        
        # 对比
        comparison = VGroup(
            Text(
                "如果不考虑权重（算术平均）:",
                font="Noto Sans CJK SC",
                font_size=20,
                color=GRAY_A
            ),
            MathTex(
                r"\frac{80 + 85 + 90}{3} = 85.0",
                font_size=22,
                color=GRAY_B
            ).shift(DOWN * 0.3)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 3)
        
        self.play(FadeIn(comparison), run_time=0.8)
        
        diff_text = Text(
            "考虑权重后，期末占比更大！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(diff_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(context),
            FadeOut(score_cards),
            FadeOut(weight_explain),
            FadeOut(formula),
            FadeOut(calc_steps),
            FadeOut(comparison),
            FadeOut(diff_text),
            run_time=0.6
        )
    
    def show_extreme_value_effect(self):
        """场景5: 极端值影响"""
        # 标题
        title = Text(
            "平均数的特点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_EXTREME,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 副标题
        subtitle = Text(
            "易受极端值影响",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 正常数据组
        normal_group = VGroup(
            Text(
                "正常数据: 6, 7, 8, 9, 10",
                font="Noto Sans CJK SC",
                font_size=24,
                color=WHITE
            ),
            MathTex(
                r"\bar{x} = \frac{6+7+8+9+10}{5} = 8",
                font_size=26,
                color=self.COLOR_ARITHMETIC_MEAN
            ).shift(DOWN * 0.5)
        ).arrange(DOWN, buff=0.3).move_to(UP * 3.5)
        
        self.play(Write(normal_group[0]), run_time=1.0)
        self.play(Write(normal_group[1]), run_time=0.8)
        
        # 可视化正常数据
        normal_dots = VGroup(*[
            Dot(
                np.array([i * 0.8 - 1.6, 2, 0]),
                radius=0.1,
                color=self.COLOR_DATA_POINT
            )
            for i in range(5)
        ])
        
        normal_labels = VGroup(*[
            Text(
                str(val),
                font="Noto Sans CJK SC",
                font_size=20,
                color=WHITE
            ).next_to(dot, UP, buff=0.2)
            for val, dot in zip(self.normal_data, normal_dots)
        ])
        
        self.play(FadeIn(normal_dots), FadeIn(normal_labels), run_time=0.6)
        
        # 引入极端值
        arrow = Arrow(
            start=UP * 1.2,
            end=UP * 0.3,
            color=self.COLOR_EXTREME,
            stroke_width=4
        )
        
        change_text = Text(
            "将最后一个数改为 50",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_EXTREME
        ).next_to(arrow, UP, buff=0.1)
        
        self.play(GrowArrow(arrow), FadeIn(change_text), run_time=1.0)
        
        # 变换最后一个点
        new_label = Text(
            "50",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_EXTREME,
            weight=BOLD
        ).move_to(normal_labels[-1].get_center())
        
        self.play(
            Transform(normal_labels[-1], new_label),
            normal_dots[-1].animate.set_color(self.COLOR_EXTREME).scale(1.5),
            run_time=1.0
        )
        
        # 极端值标注
        extreme_label = Text(
            "极端值!",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_EXTREME,
            weight=BOLD
        ).next_to(normal_dots[-1], DOWN, buff=0.3)
        
        self.play(FadeIn(extreme_label, scale=1.5), run_time=0.5)
        
        # 新的平均值
        extreme_group = VGroup(
            Text(
                "新数据: 6, 7, 8, 9, 50",
                font="Noto Sans CJK SC",
                font_size=24,
                color=WHITE
            ),
            MathTex(
                r"\bar{x} = \frac{6+7+8+9+50}{5} = 16",
                font_size=26,
                color=self.COLOR_EXTREME
            ).shift(DOWN * 0.5)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(Write(extreme_group[0]), run_time=1.0)
        self.play(Write(extreme_group[1]), run_time=1.2)
        
        # 对比箭头
        comparison_arrow = DoubleArrow(
            start=UP * 3 + LEFT * 2,
            end=DOWN * 0.5 + LEFT * 2,
            color=YELLOW,
            stroke_width=3
        )
        
        comparison_text = VGroup(
            Text(
                "从 8",
                font="Noto Sans CJK SC",
                font_size=20,
                color=self.COLOR_ARITHMETIC_MEAN
            ),
            Text(
                "变为 16",
                font="Noto Sans CJK SC",
                font_size=20,
                color=self.COLOR_EXTREME
            ),
            Text(
                "增加了 8!",
                font="Noto Sans CJK SC",
                font_size=22,
                color=YELLOW,
                weight=BOLD
            )
        ).arrange(DOWN, buff=0.15).next_to(comparison_arrow, LEFT, buff=0.3)
        
        self.play(Create(comparison_arrow), run_time=0.6)
        self.play(FadeIn(comparison_text, lag_ratio=0.3), run_time=0.8)
        
        # 警告提示
        warning = VGroup(
            Text(
                "⚠️ 注意",
                font="Noto Sans CJK SC",
                font_size=24,
                color=self.COLOR_EXTREME,
                weight=BOLD
            ),
            Text(
                "平均数容易受极端值影响",
                font="Noto Sans CJK SC",
                font_size=22,
                color=GRAY_A
            ).shift(DOWN * 0.35),
            Text(
                "不能很好代表整体水平",
                font="Noto Sans CJK SC",
                font_size=22,
                color=GRAY_A
            ).shift(DOWN * 0.7)
        ).move_to(DOWN * 3)
        
        self.play(Write(warning), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(normal_group),
            FadeOut(normal_dots),
            FadeOut(normal_labels),
            FadeOut(arrow),
            FadeOut(change_text),
            FadeOut(extreme_label),
            FadeOut(extreme_group),
            FadeOut(comparison_arrow),
            FadeOut(comparison_text),
            FadeOut(warning),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 总结对比"""
        # 标题
        title = Text(
            "平均数知识总结",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三个要点卡片
        points = VGroup()
        
        # 要点1
        point1 = VGroup(
            Circle(
                radius=0.25,
                color=self.COLOR_ARITHMETIC_MEAN,
                fill_opacity=1,
                stroke_width=0
            ),
            Text(
                "1",
                font="Noto Sans CJK SC",
                font_size=28,
                color=WHITE,
                weight=BOLD
            )
        )
        point1[1].move_to(point1[0].get_center())
        
        point1_text = VGroup(
            Text(
                "算术平均数",
                font="Noto Sans CJK SC",
                font_size=26,
                color=WHITE,
                weight=BOLD
            ),
            Text(
                "所有数相加除以个数",
                font="Noto Sans CJK SC",
                font_size=20,
                color=GRAY_A
            ).shift(DOWN * 0.35)
        )
        
        point1_group = VGroup(point1, point1_text).arrange(RIGHT, buff=0.4).move_to(UP * 4)
        points.add(point1_group)
        
        # 要点2
        point2 = VGroup(
            Circle(
                radius=0.25,
                color=self.COLOR_WEIGHTED_MEAN,
                fill_opacity=1,
                stroke_width=0
            ),
            Text(
                "2",
                font="Noto Sans CJK SC",
                font_size=28,
                color=WHITE,
                weight=BOLD
            )
        )
        point2[1].move_to(point2[0].get_center())
        
        point2_text = VGroup(
            Text(
                "加权平均数",
                font="Noto Sans CJK SC",
                font_size=26,
                color=WHITE,
                weight=BOLD
            ),
            Text(
                "考虑不同数据的重要性（权重）",
                font="Noto Sans CJK SC",
                font_size=20,
                color=GRAY_A
            ).shift(DOWN * 0.35)
        )
        
        point2_group = VGroup(point2, point2_text).arrange(RIGHT, buff=0.4).move_to(UP * 2.2)
        points.add(point2_group)
        
        # 要点3
        point3 = VGroup(
            Circle(
                radius=0.25,
                color=self.COLOR_EXTREME,
                fill_opacity=1,
                stroke_width=0
            ),
            Text(
                "3",
                font="Noto Sans CJK SC",
                font_size=28,
                color=WHITE,
                weight=BOLD
            )
        )
        point3[1].move_to(point3[0].get_center())
        
        point3_text = VGroup(
            Text(
                "注意极端值",
                font="Noto Sans CJK SC",
                font_size=26,
                color=WHITE,
                weight=BOLD
            ),
            Text(
                "会影响平均数的代表性",
                font="Noto Sans CJK SC",
                font_size=20,
                color=GRAY_A
            ).shift(DOWN * 0.35)
        )
        
        point3_group = VGroup(point3, point3_text).arrange(RIGHT, buff=0.4).move_to(UP * 0.4)
        points.add(point3_group)
        
        # 依次展示要点
        for i, point in enumerate(points):
            self.play(FadeIn(point, shift=UP * 0.3), run_time=0.8)
            if i < len(points) - 1:
                self.wait(0.3)
        
        # 公式对比
        formulas = VGroup(
            MathTex(
                r"\bar{x} = \frac{\sum x_i}{n}",
                font_size=24,
                color=self.COLOR_ARITHMETIC_MEAN
            ),
            MathTex(
                r"\bar{x} = \frac{\sum x_i f_i}{\sum f_i}",
                font_size=24,
                color=self.COLOR_WEIGHTED_MEAN
            )
        ).arrange(RIGHT, buff=1.5).move_to(DOWN * 1.5)
        
        formula_labels = VGroup(
            Text(
                "算术",
                font="Noto Sans CJK SC",
                font_size=18,
                color=GRAY_A
            ).next_to(formulas[0], UP, buff=0.2),
            Text(
                "加权",
                font="Noto Sans CJK SC",
                font_size=18,
                color=GRAY_A
            ).next_to(formulas[1], UP, buff=0.2)
        )
        
        self.play(FadeIn(formulas), FadeIn(formula_labels), run_time=1.0)
        
        # 关键提示
        key_point = Text(
            "选择合适的平均数计算方法",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.2), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(points),
            FadeOut(formulas),
            FadeOut(formula_labels),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 数学符号装饰
        symbols = VGroup(
            MathTex(r"\bar{x}", font_size=40, color=self.COLOR_ARITHMETIC_MEAN),
            MathTex(r"\sum", font_size=40, color=self.COLOR_WEIGHTED_MEAN),
            MathTex(r"\frac{a}{b}", font_size=40, color=self.COLOR_DATA_POINT),
            MathTex(r"x_i", font_size=40, color=self.COLOR_EXTREME),
        ).arrange_in_grid(rows=2, cols=2, buff=1.2).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(symbol, scale=0.5) for symbol in symbols],
            run_time=0.6
        )
        
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql average_mean.py AverageMean  # 快速预览
# manim -qh average_mean.py AverageMean   # 高质量渲染
"""
比的基本性质 (Basic Properties of Ratios) 教学动画
使用 Manim 创建的小学数学教学视频

内容: 比的基本性质 - 前项和后项同时乘除同一个数，比值不变
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


class RatioProperties(Scene):
    """
    比的基本性质教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出比的概念
    2. 基本性质 - 乘法演示
    3. 基本性质 - 除法演示
    4. 视觉化演示 - 比例条
    5. 与分数性质的联系
    6. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_RATIO_A = "#3498db"      # 蓝色 - 前项
        self.COLOR_RATIO_B = "#e74c3c"      # 红色 - 后项
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_PROPERTY = "#2ecc71"     # 绿色 - 性质
        self.COLOR_MULTIPLY = "#9b59b6"     # 紫色 - 乘法
        self.COLOR_DIVIDE = "#f39c12"       # 橙色 - 除法
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 执行动画序列
        self.show_opening()
        self.show_multiply_property()
        self.show_divide_property()
        self.show_visualization()
        self.show_fraction_connection()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "比是什么?",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 展示比 4:6
        num_4 = Text(
            "4",
            font="PingFang SC",
            font_size=72,
            color=self.COLOR_RATIO_A,
            weight=BOLD
        ).move_to(UP * 3 + LEFT * 1.2)
        
        colon = Text(
            ":",
            font="PingFang SC",
            font_size=72,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 3)
        
        num_6 = Text(
            "6",
            font="PingFang SC",
            font_size=72,
            color=self.COLOR_RATIO_B,
            weight=BOLD
        ).move_to(UP * 3 + RIGHT * 1.2)
        
        self.play(FadeIn(num_4, scale=0.5), run_time=0.4)
        self.play(FadeIn(colon), run_time=0.2)
        self.play(FadeIn(num_6, scale=0.5), run_time=0.4)
        
        # 组合
        ratio_group = VGroup(num_4, colon, num_6)
        
        # 闪烁
        self.play(
            Flash(ratio_group, color=self.COLOR_HIGHLIGHT, flash_radius=1.0),
            run_time=0.4
        )
        
        # 问题文字
        question = Text(
            "这个比能化简吗?",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            run_time=0.4
        )
        
        # 保存比例供后续使用
        self.ratio_4_6 = ratio_group
    
    def show_multiply_property(self):
        """场景2: 基本性质 - 乘法演示"""
        # 标题
        title = Text(
            "比的基本性质",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        property_text = Text(
            "前项和后项同时乘以同一个数",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(property_text), run_time=0.5)
        
        # 移动原比例到左侧
        self.play(
            self.ratio_4_6.animate.move_to(LEFT * 2.5 + UP * 2),
            run_time=0.6
        )
        
        # 显示 ×2 操作
        multiply_op = VGroup(
            Text("×", font="PingFang SC", font_size=36, color=self.COLOR_MULTIPLY),
            Text("2", font="PingFang SC", font_size=36, color=self.COLOR_MULTIPLY)
        ).arrange(RIGHT, buff=0.1)
        multiply_op.move_to(LEFT * 2.5 + UP * 0.8)
        
        self.play(FadeIn(multiply_op, shift=DOWN * 0.3), run_time=0.5)
        
        # 箭头
        arrow = Arrow(
            LEFT * 1 + UP * 2,
            RIGHT * 1 + UP * 2,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3
        )
        
        self.play(GrowArrow(arrow), run_time=0.4)
        
        # 计算过程 - 4×2
        calc_4 = VGroup(
            Text("4", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_A),
            Text("×2 =", font="PingFang SC", font_size=28, color=self.COLOR_MULTIPLY),
            Text("8", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_A, weight=BOLD)
        ).arrange(RIGHT, buff=0.15)
        calc_4.move_to(LEFT * 2.5 + DOWN * 0.2)
        
        self.play(FadeIn(calc_4), run_time=0.8)
        
        # 计算过程 - 6×2
        calc_6 = VGroup(
            Text("6", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_B),
            Text("×2 =", font="PingFang SC", font_size=28, color=self.COLOR_MULTIPLY),
            Text("12", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_B, weight=BOLD)
        ).arrange(RIGHT, buff=0.15)
        calc_6.move_to(LEFT * 2.5 + DOWN * 1.2)
        
        self.play(FadeIn(calc_6), run_time=0.8)
        
        # 新比例 8:12
        new_ratio = VGroup(
            Text("8", font="PingFang SC", font_size=64, color=self.COLOR_RATIO_A, weight=BOLD),
            Text(":", font="PingFang SC", font_size=64, color=WHITE),
            Text("12", font="PingFang SC", font_size=64, color=self.COLOR_RATIO_B, weight=BOLD)
        ).arrange(RIGHT, buff=0.2)
        new_ratio.move_to(RIGHT * 2.5 + UP * 2)
        
        self.play(FadeIn(new_ratio, scale=0.5), run_time=0.6)
        
        # 等号
        equals = Text("=", font="PingFang SC", font_size=48, color=self.COLOR_PROPERTY).move_to(UP * 2)
        self.play(Write(equals), run_time=0.4)
        
        # 公式
        formula = MathTex(
            r"4:6 = 8:12",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 说明文字
        explanation = Text(
            "比值不变!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation, scale=1.2), run_time=0.5)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(property_text),
            FadeOut(self.ratio_4_6),
            FadeOut(multiply_op),
            FadeOut(arrow),
            FadeOut(calc_4),
            FadeOut(calc_6),
            FadeOut(new_ratio),
            FadeOut(equals),
            FadeOut(formula),
            FadeOut(explanation),
            run_time=0.5
        )
    
    def show_divide_property(self):
        """场景3: 基本性质 - 除法演示 (化简比)"""
        # 新例子引入
        new_example = Text(
            "化简比: 找最大公因数",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(new_example, shift=DOWN * 0.3), run_time=0.5)
        
        # 12:18 比例
        ratio_12_18 = VGroup(
            Text("12", font="PingFang SC", font_size=72, color=self.COLOR_RATIO_A, weight=BOLD),
            Text(":", font="PingFang SC", font_size=72, color=WHITE),
            Text("18", font="PingFang SC", font_size=72, color=self.COLOR_RATIO_B, weight=BOLD)
        ).arrange(RIGHT, buff=0.2)
        ratio_12_18.move_to(LEFT * 2.5 + UP * 2.5)
        
        self.play(Write(ratio_12_18), run_time=0.6)
        
        # ÷6 操作
        divide_op = VGroup(
            Text("÷", font="PingFang SC", font_size=36, color=self.COLOR_DIVIDE),
            Text("6", font="PingFang SC", font_size=36, color=self.COLOR_DIVIDE)
        ).arrange(RIGHT, buff=0.1)
        divide_op.move_to(LEFT * 2.5 + UP * 1.2)
        
        gcd_hint = Text(
            "GCD(12,18) = 6",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(LEFT * 2.5 + UP * 0.5)
        
        self.play(FadeIn(divide_op, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(gcd_hint), run_time=0.5)
        
        # 箭头
        arrow = Arrow(
            LEFT * 1 + UP * 2.5,
            RIGHT * 1 + UP * 2.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3
        )
        
        self.play(GrowArrow(arrow), run_time=0.4)
        
        # 计算过程 - 12÷6
        calc_12 = VGroup(
            Text("12", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_A),
            Text("÷6 =", font="PingFang SC", font_size=28, color=self.COLOR_DIVIDE),
            Text("2", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_A, weight=BOLD)
        ).arrange(RIGHT, buff=0.15)
        calc_12.move_to(LEFT * 2.5 + DOWN * 0.5)
        
        self.play(FadeIn(calc_12), run_time=0.8)
        
        # 计算过程 - 18÷6
        calc_18 = VGroup(
            Text("18", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_B),
            Text("÷6 =", font="PingFang SC", font_size=28, color=self.COLOR_DIVIDE),
            Text("3", font="PingFang SC", font_size=32, color=self.COLOR_RATIO_B, weight=BOLD)
        ).arrange(RIGHT, buff=0.15)
        calc_18.move_to(LEFT * 2.5 + DOWN * 1.5)
        
        self.play(FadeIn(calc_18), run_time=0.8)
        
        # 化简后 2:3
        simplified_ratio = VGroup(
            Text("2", font="PingFang SC", font_size=72, color=self.COLOR_RATIO_A, weight=BOLD),
            Text(":", font="PingFang SC", font_size=72, color=WHITE),
            Text("3", font="PingFang SC", font_size=72, color=self.COLOR_RATIO_B, weight=BOLD)
        ).arrange(RIGHT, buff=0.2)
        simplified_ratio.move_to(RIGHT * 2.5 + UP * 2.5)
        
        self.play(FadeIn(simplified_ratio, scale=0.5), run_time=0.6)
        
        # 等号
        equals = Text("=", font="PingFang SC", font_size=48, color=self.COLOR_PROPERTY).move_to(UP * 2.5)
        self.play(Write(equals), run_time=0.4)
        
        # 公式
        formula = MathTex(
            r"12:18 = 2:3",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(Write(formula), run_time=1.0)
        
        # "最简整数比"
        simplest_form = Text(
            "最简整数比",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4)
        
        # 添加框
        box = SurroundingRectangle(
            simplified_ratio,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            FadeIn(simplest_form, scale=1.2),
            Create(box),
            run_time=0.6
        )
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(new_example),
            FadeOut(ratio_12_18),
            FadeOut(divide_op),
            FadeOut(gcd_hint),
            FadeOut(arrow),
            FadeOut(calc_12),
            FadeOut(calc_18),
            FadeOut(simplified_ratio),
            FadeOut(equals),
            FadeOut(formula),
            FadeOut(simplest_form),
            FadeOut(box),
            run_time=0.5
        )
    
    def show_visualization(self):
        """场景4: 视觉化演示 - 比例条"""
        # 标题
        title = Text(
            "视觉化理解",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # === 第一部分: 4:6 (10段) ===
        # 创建比例条 (总长6，高0.5)
        total_length = 6
        bar_height = 0.5
        segment_width = total_length / 10  # 10段
        
        # 前4段 (蓝色)
        segments_blue = VGroup(*[
            Rectangle(width=segment_width, height=bar_height, 
                     fill_color=self.COLOR_RATIO_A, fill_opacity=0.8,
                     stroke_color=WHITE, stroke_width=2)
            for _ in range(4)
        ])
        segments_blue.arrange(RIGHT, buff=0)
        
        # 后6段 (红色)
        segments_red = VGroup(*[
            Rectangle(width=segment_width, height=bar_height,
                     fill_color=self.COLOR_RATIO_B, fill_opacity=0.8,
                     stroke_color=WHITE, stroke_width=2)
            for _ in range(6)
        ])
        segments_red.arrange(RIGHT, buff=0)
        
        # 组合
        bar_10 = VGroup(segments_blue, segments_red).arrange(RIGHT, buff=0)
        bar_10.move_to(UP * 3)
        
        self.play(Create(bar_10), run_time=0.8)
        
        # 逐个显示段
        self.play(
            LaggedStart(*[seg.animate.set_fill(opacity=0.8) for seg in segments_blue],
                       lag_ratio=0.1),
            run_time=0.6
        )
        self.play(
            LaggedStart(*[seg.animate.set_fill(opacity=0.8) for seg in segments_red],
                       lag_ratio=0.1),
            run_time=0.6
        )
        
        # 标注
        label_4 = Text("4", font="PingFang SC", font_size=28, 
                      color=self.COLOR_RATIO_A, weight=BOLD).next_to(segments_blue, UP, buff=0.3)
        label_6 = Text("6", font="PingFang SC", font_size=28,
                      color=self.COLOR_RATIO_B, weight=BOLD).next_to(segments_red, UP, buff=0.3)
        
        self.play(FadeIn(label_4), FadeIn(label_6), run_time=0.5)
        
        # 计算比值
        ratio_value_1 = MathTex(
            r"\frac{4}{6} \approx 0.67",
            font_size=28,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(Write(ratio_value_1), run_time=0.8)
        self.wait(0.8)
        
        # === 第二部分: 重新分组为 2:3 (5段) ===
        # 创建新的5段条
        segment_width_5 = total_length / 5
        
        segments_blue_5 = VGroup(*[
            Rectangle(width=segment_width_5, height=bar_height,
                     fill_color=self.COLOR_RATIO_A, fill_opacity=0.8,
                     stroke_color=WHITE, stroke_width=2)
            for _ in range(2)
        ])
        segments_blue_5.arrange(RIGHT, buff=0)
        
        segments_red_5 = VGroup(*[
            Rectangle(width=segment_width_5, height=bar_height,
                     fill_color=self.COLOR_RATIO_B, fill_opacity=0.8,
                     stroke_color=WHITE, stroke_width=2)
            for _ in range(3)
        ])
        segments_red_5.arrange(RIGHT, buff=0)
        
        bar_5 = VGroup(segments_blue_5, segments_red_5).arrange(RIGHT, buff=0)
        bar_5.move_to(UP * 3)
        
        # 变换说明
        transform_text = Text(
            "重新分组 →",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(transform_text), run_time=0.4)
        
        # 变换动画
        self.play(
            Transform(bar_10, bar_5),
            FadeOut(label_4),
            FadeOut(label_6),
            run_time=1.2
        )
        
        # 新标注
        label_2 = Text("2", font="PingFang SC", font_size=28,
                      color=self.COLOR_RATIO_A, weight=BOLD).next_to(segments_blue_5, UP, buff=0.3)
        label_3 = Text("3", font="PingFang SC", font_size=28,
                      color=self.COLOR_RATIO_B, weight=BOLD).next_to(segments_red_5, UP, buff=0.3)
        
        self.play(FadeIn(label_2), FadeIn(label_3), run_time=0.5)
        
        # 计算比值
        ratio_value_2 = MathTex(
            r"\frac{2}{3} \approx 0.67",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(Write(ratio_value_2), run_time=0.8)
        
        # 高亮相等
        equals_highlight = VGroup(ratio_value_1, ratio_value_2)
        self.play(
            Indicate(equals_highlight, color=self.COLOR_PROPERTY, scale_factor=1.1),
            run_time=0.6
        )
        
        # 结论
        conclusion = Text(
            "比值相等!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(conclusion, scale=1.2), run_time=0.5)
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(bar_10),
            FadeOut(label_2),
            FadeOut(label_3),
            FadeOut(ratio_value_1),
            FadeOut(ratio_value_2),
            FadeOut(transform_text),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def show_fraction_connection(self):
        """场景5: 与分数性质的联系"""
        # 标题
        title = Text(
            "比与分数的联系",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PROPERTY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 比的形式
        ratio_form = MathTex(
            r"4:6",
            font_size=48,
            color=WHITE
        ).move_to(UP * 3 + LEFT * 2)
        
        self.play(Write(ratio_form), run_time=0.5)
        
        # 转换箭头
        conversion_arrow = Arrow(
            UP * 3 + LEFT * 0.5,
            UP * 3 + RIGHT * 0.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(GrowArrow(conversion_arrow), run_time=0.3)
        
        # 分数形式
        fraction_form = MathTex(
            r"\frac{4}{6}",
            font_size=48,
            color=WHITE
        ).move_to(UP * 3 + RIGHT * 2)
        
        self.play(Write(fraction_form), run_time=0.5)
        
        # 并排对比
        comparison = VGroup(ratio_form, conversion_arrow, fraction_form)
        self.play(comparison.animate.move_to(UP * 3), run_time=0.6)
        
        # 性质1: 比
        property_ratio = VGroup(
            Text("比:", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"a:b = (a \times k):(b \times k)", font_size=24, color=self.COLOR_RATIO_A)
        ).arrange(RIGHT, buff=0.3)
        property_ratio.move_to(UP * 1)
        
        self.play(FadeIn(property_ratio), run_time=0.8)
        
        # 性质2: 分数
        property_fraction = VGroup(
            Text("分数:", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"\frac{a}{b} = \frac{a \times k}{b \times k}", font_size=24, color=self.COLOR_RATIO_B)
        ).arrange(RIGHT, buff=0.3)
        property_fraction.move_to(DOWN * 0.5)
        
        self.play(FadeIn(property_fraction), run_time=0.8)
        
        # 高亮相似性
        similarities = VGroup(property_ratio, property_fraction)
        self.play(
            Indicate(similarities, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 结论
        conclusion = Text(
            "比的性质类似于分数的基本性质",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(comparison),
            FadeOut(property_ratio),
            FadeOut(property_fraction),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def show_outro(self):
        """场景6: 总结与片尾"""
        # 总结标题
        summary_title = Text(
            "知识点总结",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 总结卡片
        cards = VGroup()
        
        # 卡片1
        icon_1 = Circle(radius=0.2, fill_color=self.COLOR_MULTIPLY, 
                       fill_opacity=1, stroke_width=0)
        text_1 = Text(
            "前项和后项同时乘以一个数，比值不变",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        )
        card_1 = VGroup(icon_1, text_1).arrange(RIGHT, buff=0.3)
        card_1.move_to(UP * 3.5)
        cards.add(card_1)
        
        # 卡片2
        icon_2 = Circle(radius=0.2, fill_color=self.COLOR_DIVIDE, 
                       fill_opacity=1, stroke_width=0)
        text_2 = Text(
            "前项和后项同时除以一个数，比值不变",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        )
        card_2 = VGroup(icon_2, text_2).arrange(RIGHT, buff=0.3)
        card_2.move_to(UP * 2.5)
        cards.add(card_2)
        
        # 卡片3
        icon_3 = Circle(radius=0.2, fill_color=self.COLOR_PROPERTY, 
                       fill_opacity=1, stroke_width=0)
        text_3 = Text(
            "利用这个性质可以化简比",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        )
        card_3 = VGroup(icon_3, text_3).arrange(RIGHT, buff=0.3)
        card_3.move_to(UP * 1.5)
        cards.add(card_3)
        
        # 卡片从左侧滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 示例回顾
        example_recap = VGroup(
            Text("示例:", font="PingFang SC", font_size=26, color=GRAY_A),
            MathTex(r"12:18 = 2:3", font_size=28, color=self.COLOR_PROPERTY)
        ).arrange(DOWN, buff=0.3).move_to(UP * 0)
        
        self.play(FadeIn(example_recap), run_time=0.6)
        self.wait(0.8)
        
        # 淡出总结
        summary_group = VGroup(summary_title, cards, example_recap)
        self.play(FadeOut(summary_group), run_time=0.5)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.5)
        
        # 装饰图标 - 比例符号
        icons = VGroup(*[
            Text(":", font="PingFang SC", font_size=40, 
                color=self.COLOR_PROPERTY, weight=BOLD)
            .shift(1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ]).move_to(follow_text.get_center() + DOWN * 1.5)
        
        self.play(
            LaggedStart(*[FadeIn(icon, scale=0.5) for icon in icons], lag_ratio=0.1),
            run_time=0.8
        )
        
        self.wait(1.3)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql ratio_properties.py RatioProperties  # 快速预览
# manim -qh ratio_properties.py RatioProperties   # 高质量渲染
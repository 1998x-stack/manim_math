"""
无穷等比数列求和 - Infinite Geometric Series Sum Animation
使用 Manim 创建的高中数学教学视频

内容: 无穷等比数列的求和公式及其应用
目标观众: 高二学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
1. 开场钩子 - 0.999...=1?
2. 等比数列回顾
3. 有限和公式
4. 无穷和的关键 - 极限
5. 经典例子 - 0.999...=1 的证明
6. 发散情况 - |q|≥1
7. 总结 + 片尾

总时长: ~65秒
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class InfiniteGeometricSeries(Scene):
    """
    无穷等比数列求和教学动画场景
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 重点
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_CONVERGENT = "#2ecc71"   # 绿色 - 收敛
        self.COLOR_DIVERGENT = "#e67e22"    # 橙色 - 发散
        
        # 初始化数学参数
        self.setup_parameters()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_geometric_sequence()
        self.scene_3_finite_sum()
        self.scene_4_infinite_sum()
        self.scene_5_example_999()
        self.scene_6_divergent()
        self.scene_7_summary()
    
    def setup_parameters(self):
        """初始化所有数学参数"""
        # 收敛情况参数
        self.a1 = 1.0
        self.q_conv = 0.5
        self.S_infinity = self.a1 / (1 - self.q_conv)  # = 2.0
        
        # 发散情况参数
        self.q_div = 1.2
        
        # 0.999...例子参数
        self.a1_999 = 0.9
        self.q_999 = 0.1
        
        print(f"✓ 参数初始化完成: a₁={self.a1}, q={self.q_conv}, S∞={self.S_infinity}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 - 引出问题"""
        # 作者信息 (顶部常驻)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题 - 一行显示
        question = VGroup(
            Text("0.999...", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_HIGHLIGHT),
            MathTex("=", font_size=60, color=WHITE),
            Text("1", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3)
        
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 1.5)
        
        # 动画序列
        self.play(Write(question[0]), run_time=0.8)
        self.play(FadeIn(question[1], scale=1.2), run_time=0.3)
        self.play(Write(question[2]), run_time=0.5)
        self.wait(0.3)
        
        self.play(Write(question_mark, run_time=0.4))
        self.play(Flash(question_mark, color=self.COLOR_SECONDARY, flash_radius=0.5), run_time=0.5)
        
        # 神秘提示
        hint = Text(
            "这是真的吗？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(question),
            FadeOut(question_mark),
            FadeOut(hint),
            run_time=0.5
        )
    
    def scene_2_geometric_sequence(self):
        """场景2: 等比数列基础回顾"""
        # 标题
        title = Text(
            "等比数列回顾",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义公式
        definition = MathTex(
            r"a_n = a_1 \cdot q^{n-1}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(FadeIn(definition, shift=DOWN * 0.2), run_time=0.6)
        
        # 创建坐标轴 - 精确计算位置
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.2, 0.2],
            x_length=7,
            y_length=4,
            axis_config={
                "color": self.COLOR_AUXILIARY,
                "include_numbers": False,
                "include_tip": True,
            },
        ).move_to(UP * 1.5)
        
        # 坐标轴标签
        x_label = Text("n", font="Noto Sans CJK SC", font_size=24, color=GRAY_A).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_label = MathTex("a_n", font_size=24, color=GRAY_A).next_to(axes.y_axis, UP, buff=0.1)
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 绘制数列点: 1, 1/2, 1/4, 1/8, 1/16, ...
        sequence_dots = VGroup()
        
        for n in range(1, 9):
            value = self.a1 * (self.q_conv ** (n - 1))
            point = axes.c2p(n, value)
            dot = Dot(point, radius=0.08, color=self.COLOR_PRIMARY)
            sequence_dots.add(dot)
        
        # 点依次出现
        self.play(
            AnimationGroup(*[GrowFromCenter(dot) for dot in sequence_dots], lag_ratio=0.2),
            run_time=2.0
        )
        
        # 标注参数
        param_text = VGroup(
            MathTex(r"a_1 = 1", font_size=26, color=self.COLOR_CONVERGENT),
            MathTex(r"q = \frac{1}{2}", font_size=26, color=self.COLOR_CONVERGENT)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 1.5)
        
        self.play(Write(param_text), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            run_time=0.4
        )
        
        # 保留以供后续场景使用
        self.axes = axes
        self.x_label = x_label
        self.y_label = y_label
        self.sequence_dots = sequence_dots
        self.param_text = param_text
    
    def scene_3_finite_sum(self):
        """场景3: 有限和公式"""
        # 标题
        title = Text(
            "前n项和",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 有限和公式
        sum_formula = MathTex(
            r"S_n = \frac{a_1(1-q^n)}{1-q}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(Write(sum_formula), run_time=1.0)
        
        # 绘制累积和曲线
        sum_dots = VGroup()
        for n in range(1, 9):
            S_n = self.a1 * (1 - self.q_conv**n) / (1 - self.q_conv)
            point = self.axes.c2p(n, S_n)
            dot = Dot(point, radius=0.06, color=self.COLOR_SECONDARY)
            sum_dots.add(dot)
        
        # 连接成曲线
        sum_line = VGroup()
        for i in range(len(sum_dots) - 1):
            line = Line(
                sum_dots[i].get_center(),
                sum_dots[i + 1].get_center(),
                color=self.COLOR_SECONDARY,
                stroke_width=3
            )
            sum_line.add(line)
        
        self.play(Create(sum_line), run_time=1.5)
        self.play(
            AnimationGroup(*[GrowFromCenter(dot) for dot in sum_dots], lag_ratio=0.1),
            run_time=1.0
        )
        
        # 标注示例点
        example_n = 8
        example_S = self.a1 * (1 - self.q_conv**example_n) / (1 - self.q_conv)
        example_dot = Dot(self.axes.c2p(example_n, example_S), radius=0.12, color=YELLOW)
        example_label = MathTex(
            f"S_{{8}} \\approx {example_S:.3f}",
            font_size=24,
            color=YELLOW
        ).next_to(example_dot, RIGHT, buff=0.2)
        
        self.play(FadeIn(example_dot, scale=1.5), run_time=0.5)
        self.play(Write(example_label), run_time=0.6)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example_dot),
            FadeOut(example_label),
            run_time=0.4
        )
        
        # 保留
        self.sum_formula = sum_formula
        self.sum_dots = sum_dots
        self.sum_line = sum_line
    
    def scene_4_infinite_sum(self):
        """场景4: 无穷和的关键 - 极限"""
        # 标题
        title = Text(
            "当 n → ∞ 会怎样？",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=1.0)
        
        # 关键条件
        condition_text = Text(
            "当 |q| < 1 时",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_CONVERGENT
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(condition_text), run_time=0.6)
        
        # 展示 q^n 的变化
        qn_tracker = ValueTracker(5)
        
        qn_display = always_redraw(lambda: VGroup(
            MathTex(r"q^n =", font_size=28, color=WHITE),
            DecimalNumber(
                self.q_conv ** qn_tracker.get_value(),
                num_decimal_places=5,
                font_size=28,
                color=self.COLOR_PRIMARY
            )
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.3))
        
        self.add(qn_display)
        self.wait(0.5)
        
        # q^n → 0 动画
        self.play(qn_tracker.animate.set_value(15), run_time=2.5, rate_func=smooth)
        
        # 极限结论
        limit_conclusion = MathTex(
            r"\lim_{n \to \infty} q^n = 0",
            font_size=30,
            color=self.COLOR_CONVERGENT
        ).move_to(UP * 3.5)
        
        self.play(TransformFromCopy(qn_display, limit_conclusion), run_time=0.8)
        self.remove(qn_display)
        self.wait(0.5)
        
        # 因此公式变为
        arrow = MathTex(r"\Downarrow", font_size=40, color=YELLOW).move_to(UP * 2.8)
        
        infinite_formula = MathTex(
            r"S_\infty = \frac{a_1}{1-q}",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(arrow, scale=1.2), run_time=0.4)
        self.play(Write(infinite_formula), run_time=1.0)
        
        # 绘制极限线
        limit_y = self.S_infinity
        limit_line = DashedLine(
            self.axes.c2p(0, limit_y),
            self.axes.c2p(10, limit_y),
            color=self.COLOR_HIGHLIGHT,
            dash_length=0.1,
            stroke_width=3
        )
        
        limit_label = MathTex(
            f"S_\\infty = {limit_y}",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(self.axes.c2p(10, limit_y), RIGHT, buff=0.1)
        
        self.play(Create(limit_line), run_time=1.0)
        self.play(FadeIn(limit_label), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition_text),
            FadeOut(limit_conclusion),
            FadeOut(arrow),
            FadeOut(self.sum_formula),
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.sequence_dots),
            FadeOut(self.param_text),
            FadeOut(self.sum_dots),
            FadeOut(self.sum_line),
            FadeOut(limit_line),
            FadeOut(limit_label),
            run_time=0.6
        )
        
        # 保留核心公式
        self.infinite_formula = infinite_formula
        self.play(self.infinite_formula.animate.move_to(UP * 6), run_time=0.5)
    
    def scene_5_example_999(self):
        """场景5: 经典例子 - 0.999...=1 的证明"""
        # 标题
        title = Text(
            "经典例子",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=0.8)
        
        # 展示 0.999...
        decimal = MathTex(
            r"0.999\ldots",
            font_size=40,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(decimal), run_time=0.8)
        
        # 拆分展开
        expansion = MathTex(
            r"= 0.9 + 0.09 + 0.009 + \cdots",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(FadeIn(expansion, shift=DOWN * 0.2), run_time=1.0)
        
        # 转化为分数
        fraction_form = MathTex(
            r"= \frac{9}{10} + \frac{9}{100} + \frac{9}{1000} + \cdots",
            font_size=28,
            color=WHITE
        ).move_to(UP * 2.2)
        
        self.play(TransformMatchingTex(expansion.copy(), fraction_form), run_time=1.0)
        
        # 识别为等比数列
        identification = VGroup(
            Text("这是一个等比数列!", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HIGHLIGHT),
            MathTex(r"a_1 = \frac{9}{10}, \quad q = \frac{1}{10}", font_size=28, color=self.COLOR_CONVERGENT)
        ).arrange(DOWN, buff=0.3).move_to(UP * 1)
        
        self.play(FadeIn(identification, shift=UP * 0.3), run_time=0.8)
        self.wait(0.8)
        
        # 应用公式
        formula_application = MathTex(
            r"S_\infty = \frac{\frac{9}{10}}{1-\frac{1}{10}}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 0.2)
        
        self.play(Write(formula_application), run_time=1.0)
        
        # 化简
        simplification = MathTex(
            r"= \frac{\frac{9}{10}}{\frac{9}{10}}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 0.2)
        
        self.play(TransformMatchingTex(formula_application, simplification), run_time=0.8)
        
        # 最终结果
        final_result = MathTex(
            r"= 1",
            font_size=48,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 1.2)
        
        self.play(Write(final_result), run_time=0.8)
        
        # 强调
        emphasis_box = SurroundingRectangle(
            final_result,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            stroke_width=4
        )
        
        self.play(Create(emphasis_box), run_time=0.6)
        self.play(Flash(final_result, color=YELLOW, flash_radius=1.0), run_time=0.5)
        
        # 结论
        conclusion = Text(
            "0.999... = 1 是正确的！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(decimal),
            FadeOut(expansion),
            FadeOut(fraction_form),
            FadeOut(identification),
            FadeOut(simplification),
            FadeOut(final_result),
            FadeOut(emphasis_box),
            FadeOut(conclusion),
            FadeOut(self.infinite_formula),
            run_time=0.6
        )
    
    def scene_6_divergent(self):
        """场景6: 发散情况 - |q| ≥ 1"""
        # 标题
        title = Text(
            "当 |q| ≥ 1 时",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_DIVERGENT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 条件说明
        condition = Text(
            "数列不收敛",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(condition), run_time=0.6)
        
        # 创建简单坐标轴
        axes_div = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            x_length=7,
            y_length=5,
            axis_config={
                "color": self.COLOR_AUXILIARY,
                "include_tip": True,
            },
        ).move_to(UP * 1)
        
        self.play(Create(axes_div), run_time=0.8)
        
        # 发散数列: a₁=1, q=1.2
        divergent_dots = VGroup()
        for n in range(1, 7):
            value = self.a1 * (self.q_div ** (n - 1))
            if value <= 5:  # 只显示范围内的
                point = axes_div.c2p(n, value)
                dot = Dot(point, radius=0.1, color=self.COLOR_DIVERGENT)
                divergent_dots.add(dot)
        
        # 点依次出现并向上飞出
        for dot in divergent_dots:
            self.play(GrowFromCenter(dot), run_time=0.3)
        
        self.wait(0.5)
        
        # 数列爆炸增长
        self.play(
            divergent_dots.animate.shift(UP * 8).set_opacity(0),
            run_time=1.5,
            rate_func=rush_from
        )
        
        # 警告文字
        warning = VGroup(
            Text("级数发散！", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_DIVERGENT, weight=BOLD),
            Text("不存在有限和", font="Noto Sans CJK SC", font_size=28, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).move_to(UP * 2)
        
        self.play(Write(warning), run_time=1.0)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition),
            FadeOut(axes_div),
            FadeOut(warning),
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结 + 片尾"""
        # 总结标题
        title = Text(
            "无穷等比数列求和",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=1.0)
        
        # 核心公式框
        formula_box = VGroup(
            MathTex(
                r"S_\infty = \frac{a_1}{1-q}",
                font_size=40,
                color=WHITE
            ),
            Text("(当 |q| < 1 时)", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_CONVERGENT)
        ).arrange(DOWN, buff=0.4).move_to(UP * 3.5)
        
        formula_rect = SurroundingRectangle(
            formula_box,
            color=self.COLOR_HIGHLIGHT,
            buff=0.4,
            corner_radius=0.2,
            stroke_width=3
        )
        
        self.play(Create(formula_rect), run_time=0.8)
        self.play(Write(formula_box), run_time=1.0)
        
        # 应用说明
        applications = VGroup(
            Text("应用:", font="Noto Sans CJK SC", font_size=28, color=GRAY_A, weight=BOLD),
            Text("• 循环小数化分数", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
            Text("• 物理衰减问题", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
            Text("• 概率论求和", font="Noto Sans CJK SC", font_size=24, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 0.8)
        
        self.play(FadeIn(applications, shift=UP * 0.3), run_time=1.0)
        self.wait(1.0)
        
        # 清理，准备片尾
        self.play(
            FadeOut(title),
            FadeOut(formula_box),
            FadeOut(formula_rect),
            FadeOut(applications),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        # 装饰 - 小圆点环绕
        circles = VGroup(*[
            Circle(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]))
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in circles],
            run_time=0.6
        )
        
        self.play(Rotate(circles, angle=PI, run_time=2.0, rate_func=linear))
        
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )


# 渲染命令:
# manim -pql infinite_geometric_series.py InfiniteGeometricSeries  # 快速预览 (480p 15fps)
# manim -qh infinite_geometric_series.py InfiniteGeometricSeries   # 高质量 (1080p 60fps)
"""
分式不等式 - Fractional Inequalities Animation
使用 Manim 创建的中学数学教学视频

内容: 分式不等式f(x)/g(x)>0的概念、为什么不能交叉相乘、等价转化f(x)*g(x)>0、数轴标根法及"奇穿偶不穿"规则
目标观众: 高中学生
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


class FractionalInequalities(Scene):
    """
    分式不等式教学动画场景

    场景顺序:
    1. 开场介绍
    2. 概念引入
    3. 解题步骤演示
    4. 数轴标根法
    5. 实例演示
    6. 总结与提醒
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#3498db"
        self.COLOR_SECONDARY = "#2ecc71"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_NEGATIVE = RED
        self.COLOR_POSITIVE = GREEN

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_concept_introduction()
        self.show_solution_steps()
        self.show_number_line_method()
        self.show_example_demonstration()
        self.show_summary_and_reminder()

    def setup_geometry(self):
        """初始化几何数据和关键点"""
        # 数轴位置设置
        self.number_line_position = UP * 2.5
        self.number_line_range = [-5, 5, 1]

        # 创建数轴对象（暂时不添加到场景）
        self.number_line_obj = NumberLine(
            x_range=self.number_line_range,
            length=8,
            include_numbers=True,
            label_direction=UP,
            font_size=20
        ).move_to(self.number_line_position)

    def show_opening(self):
        """场景1: 开场介绍 (3-4秒)"""
        # 作者信息 (顶部，一直保留到结束)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "分式不等式",
            font="PingFang SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "f(x)/g(x) > 0 的解法",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 分式不等式示例
        inequality = MathTex(
            r"\frac{f(x)}{g(x)} > 0",
            font_size=36
        ).move_to(UP * 4)

        self.play(Write(inequality), run_time=0.8)

        # 钩子问题
        hook_text = Text(
            "如何解这种不等式？",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1)

        self.play(FadeIn(hook_text, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.8)

        # 清理开场临时元素，保留作者信息和不等式
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook_text),
            run_time=0.5
        )

        # 保留不等式到后续场景
        self.inequality_general = inequality

    def show_concept_introduction(self):
        """场景2: 概念引入 (5-6秒)"""
        # 一般形式
        general_form = MathTex(
            r"\frac{f(x)}{g(x)} > 0",
            font_size=36
        ).move_to(UP * 5.5)

        # 说明不能交叉相乘
        cross_multiply_warning = Text(
            "不能直接交叉相乘！",
            font="PingFang SC",
            font_size=28,
            color=RED
        ).move_to(UP * 4.5)

        explanation = Text(
            "因为不知道g(x)的正负",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.8)

        self.play(Transform(self.inequality_general, general_form), run_time=0.8)
        self.play(Write(cross_multiply_warning), run_time=0.6)
        self.play(FadeIn(explanation), run_time=0.4)

        # 等价转化过程
        equivalence_step1 = MathTex(
            r"\frac{f(x)}{g(x)} > 0",
            font_size=32
        ).move_to(UP * 2.5)

        arrow1 = Arrow(
            UP * 2.5 + DOWN * 0.8,
            UP * 2.5 + UP * 0.8,
            color=WHITE,
            stroke_width=3
        )

        equivalence_step2 = MathTex(
            r"f(x) \cdot g(x) > 0",
            font_size=32
        ).move_to(UP * 1.5)

        self.play(
            Transform(cross_multiply_warning, equivalence_step1),
            FadeOut(explanation),
            run_time=0.8
        )
        self.play(GrowArrow(arrow1), run_time=0.6)
        self.play(Write(equivalence_step2), run_time=0.6)

        # 强调分母不为0
        condition = Text(
            "注意：g(x) ≠ 0",
            font="PingFang SC",
            font_size=26,
            color=YELLOW
        ).move_to(UP * 0.5)

        self.play(Write(condition), run_time=0.6)
        self.wait(1.0)

        # 清理部分元素，保留等价形式和条件
        self.play(
            FadeOut(cross_multiply_warning),  # 此时它已变为 equivalence_step1
            FadeOut(arrow1),
            run_time=0.5
        )

        # 保留等价形式（乘积不等式 + 分母不为0条件）供后续场景使用
        self.equivalence_form = VGroup(equivalence_step2, condition)

    def show_solution_steps(self):
        """场景3: 解题步骤演示 (8-10秒)"""
        # 移除上一场景保留的等价形式（不再需要）
        self.play(FadeOut(self.equivalence_form), run_time=0.5)

        # 原始不等式
        original_inequality = MathTex(
            r"\frac{x-1}{x+2} > 0",
            font_size=32
        ).move_to(UP * 5.5)

        self.play(Transform(self.inequality_general, original_inequality), run_time=0.8)

        # 移项（这个例子已经是一般形式，我们展示转换过程）
        transform_step1 = MathTex(
            r"\frac{x-1}{x+2} > 0 \Rightarrow (x-1)(x+2) > 0",
            font_size=28
        ).move_to(UP * 4.5)

        self.play(Write(transform_step1), run_time=1.0)

        # 强调分母不为0的条件
        condition_note = Text(
            "且 x ≠ -2 (分母不为0)",
            font="PingFang SC",
            font_size=24,
            color=RED
        ).move_to(UP * 3.8)

        self.play(Write(condition_note), run_time=0.6)

        # 显示关键点
        key_points_text = Text(
            "关键点: x = 1 (分子为0), x = -2 (分母为0)",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 2.8)

        self.play(Write(key_points_text), run_time=0.8)

        # 乘积形式
        product_form = MathTex(
            r"(x-1)(x+2) > 0",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)

        self.play(Write(product_form), run_time=0.8)

        self.wait(1.0)

        # 清理本场景临时元素，保留乘积形式
        self.play(
            FadeOut(transform_step1),
            FadeOut(condition_note),
            FadeOut(key_points_text),
            run_time=0.6
        )

        # 保留乘积形式到后续场景（用于过渡到数轴）
        self.product_form = product_form

    def show_number_line_method(self):
        """场景4: 数轴标根法 (12-15秒)"""
        # 移除上一场景的乘积形式（不再需要）
        self.play(FadeOut(self.product_form), run_time=0.5)

        # 绘制数轴
        number_line = NumberLine(
            x_range=self.number_line_range,
            length=8,
            include_numbers=True,
            label_direction=UP,
            font_size=16
        ).move_to(self.number_line_position)

        # 标出关键点
        critical_points = [-2, 1]
        dots = VGroup()
        labels = VGroup()

        for point in critical_points:
            dot = Dot(
                number_line.n2p(point),
                color=self.COLOR_HIGHLIGHT,
                radius=0.1
            )
            label = Text(
                str(point),
                font="PingFang SC",
                font_size=18,
                color=WHITE
            ).next_to(dot, DOWN, buff=0.15)
            dots.add(dot)
            labels.add(label)

        self.play(Create(number_line), run_time=1.0)
        self.play(
            *[FadeIn(dot) for dot in dots],
            run_time=0.8
        )
        self.play(
            *[Write(label) for label in labels],
            run_time=0.6
        )

        # 从右上方开始标正负（"奇穿偶不穿"的演示）
        intervals = [
            (2, 5, "+"),   # x > 1
            (-2, 1, "-"),  # -2 < x < 1
            (-5, -2, "+")  # x < -2
        ]

        signs = VGroup()
        for start, end, sign in intervals:
            mid_point = (start + end) / 2
            sign_text = Text(
                sign,
                font="PingFang SC",
                font_size=24,
                color=GREEN if sign == "+" else RED
            ).move_to(number_line.n2p(mid_point) + UP * 0.5)
            signs.add(sign_text)

        for i, sign in enumerate(signs):
            self.play(Write(sign), run_time=0.5)
            self.wait(0.2)

        # 解释"奇穿偶不穿"概念
        explanation = Text(
            "奇穿偶不穿：奇次根穿过数轴，偶次根不穿过",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 1)

        self.play(Write(explanation), run_time=0.8)

        arrow1 = Arrow(
            explanation.get_top(),
            dots[0].get_bottom() + DOWN * 0.2,
            color=WHITE,
            stroke_width=2,
            buff=0.1
        )

        arrow2 = Arrow(
            explanation.get_top(),
            dots[1].get_bottom() + DOWN * 0.2,
            color=WHITE,
            stroke_width=2,
            buff=0.1
        )

        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(GrowArrow(arrow2), run_time=0.4)

        self.wait(1.5)

        # 清理解释文本和箭头，保留数轴、关键点和正负号
        self.play(
            FadeOut(explanation),
            FadeOut(arrow1),
            FadeOut(arrow2),
            run_time=0.6
        )

        # 保留数轴元素供后续场景使用
        self.number_line_elements = VGroup(number_line, dots, labels, signs)

    def show_example_demonstration(self):
        """场景5: 实例演示 (15-18秒)"""
        # 具体例子（不等号变为≥）
        example_inequality = MathTex(
            r"\frac{x-1}{x+2} \geq 0",
            font_size=32
        ).move_to(UP * 6.5)

        self.play(Transform(self.inequality_general, example_inequality), run_time=0.8)

        # 因式分解说明
        factorization_note = Text(
            "分子: x-1, 分母: x+2",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 5.5)

        self.play(Write(factorization_note), run_time=0.6)

        # 关键点说明
        key_points_note = Text(
            "关键点: x = -2 (分母为0), x = 1 (分子为0)",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 4.8)

        self.play(Write(key_points_note), run_time=0.6)

        # 数轴已经存在，直接使用（无需再次FadeIn）
        # 如果需要确保数轴在最上层，可以调用 bring_to_front
        self.bring_to_front(self.number_line_elements)

        # 解集
        solution_intervals = Text(
            "解集: x ∈ (-∞, -2) ∪ [1, +∞)",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)

        interval_notation = MathTex(
            r"(-\infty, -2) \cup [1, +\infty)",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(Write(solution_intervals), run_time=0.8)
        self.play(Write(interval_notation), run_time=0.8)

        self.play(
            Indicate(solution_intervals),
            Indicate(interval_notation),
            color=YELLOW,
            run_time=1.0
        )

        # 分母不为0的约束
        constraint_note = Text(
            "注意：x ≠ -2 (分母不能为0)",
            font="PingFang SC",
            font_size=20,
            color=RED
        ).move_to(DOWN * 1.5)

        self.play(Write(constraint_note), run_time=0.6)

        self.wait(1.5)

        # 清理本场景的临时说明文本，保留解集、数轴和不等式
        self.play(
            FadeOut(factorization_note),
            FadeOut(key_points_note),
            run_time=0.6
        )

        # 保留解集用于总结场景
        self.solution = VGroup(solution_intervals, interval_notation, constraint_note)

    def show_summary_and_reminder(self):
        """场景6: 总结与提醒 (5-7秒)"""
        # 总结解题步骤
        steps_title = Text(
            "解题步骤总结:",
            font="PingFang SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)

        steps = VGroup(
            Text("1. 确定分子分母零点", font="PingFang SC", font_size=24, color=WHITE),
            Text("2. 在数轴上标出关键点", font="PingFang SC", font_size=24, color=WHITE),
            Text("3. 用'奇穿偶不穿'标正负", font="PingFang SC", font_size=24, color=WHITE),
            Text("4. 根据不等号选区间", font="PingFang SC", font_size=24, color=WHITE),
            Text("5. 注意分母不能为0", font="PingFang SC", font_size=24, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 2.5)

        self.play(Write(steps_title), run_time=0.5)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 强调分母不为0的重要性
        denominator_warning = Text(
            "★ 分母不能为0 ★",
            font="PingFang SC",
            font_size=28,
            color=RED
        ).move_to(UP * 0.5)

        self.play(
            Write(denominator_warning),
            Indicate(denominator_warning, color=RED),
            run_time=0.8
        )

        # 将解集移动到合适位置
        self.play(
            self.solution.animate.move_to(DOWN * 1.5),
            run_time=0.8
        )

        # 关注信息
        follow_message = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)

        self.play(FadeIn(follow_message, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 添加装饰星星
        stars = VGroup(*[
            Star(color=YELLOW, fill_opacity=1)
            .scale(0.2)
            .move_to(follow_message.get_center() + 1.5 * np.array([
                2*np.cos(i * 2*PI/5),
                2*np.sin(i * 2*PI/5),
                0
            ]))
            for i in range(5)
        ])

        self.play(LaggedStart(*[GrowFromCenter(star) for star in stars], lag_ratio=0.2), run_time=1.0)

        self.wait(2.0)

        # 最终淡出所有元素（除了作者信息，若希望保留可添加）
        self.play(
            FadeOut(steps_title),
            *[FadeOut(step) for step in steps],
            FadeOut(denominator_warning),
            FadeOut(follow_message),
            FadeOut(stars),
            FadeOut(self.inequality_general),
            FadeOut(self.number_line_elements),
            FadeOut(self.solution),
            run_time=1.0
        )
        # 作者信息也淡出，结束
        self.play(FadeOut(self.author_info), run_time=0.5)


class Star(VMobject):
    """自定义星形类"""
    def __init__(self, color=YELLOW, fill_opacity=1, **kwargs):
        super().__init__(**kwargs)
        n = 5
        outer_radius = 1
        inner_radius = 0.4

        angles = [i * 4 * PI / n for i in range(n)]
        outer_points = [
            outer_radius * np.array([np.cos(angles[i]), np.sin(angles[i]), 0])
            for i in range(n)
        ]

        inner_angles = [a + 2 * PI / n for a in angles]
        inner_points = [
            inner_radius * np.array([np.cos(inner_angles[i]), np.sin(inner_angles[i]), 0])
            for i in range(n)
        ]

        points = []
        for i in range(n):
            points.append(outer_points[i])
            points.append(inner_points[i])
        points.append(outer_points[0])

        self.set_points_as_corners(points)
        self.set_fill(color, opacity=fill_opacity)
        self.set_stroke(color, width=2)


# 运行命令:
# manim -pql fractional_inequalities.py FractionalInequalities
# manim -qh fractional_inequalities.py FractionalInequalities
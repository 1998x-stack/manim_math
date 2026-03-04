"""
函数的概念 - Function Concepts Animation
使用 Manim 创建的高一数学教学视频

内容: 函数定义、定义域、值域、对应法则、函数相等条件
目标观众: 高一学生
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


class FunctionConcepts(Scene):
    """
    函数概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 函数的定义 - 对应关系
    3. 定义域和值域
    4. 函数相等的条件
    5. 函数图像示例
    6. 定义域的求法
    7. 总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要概念
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 次要元素
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 辅助
        self.COLOR_DOMAIN = "#2ecc71"       # 绿色 - 定义域
        self.COLOR_RANGE = "#f39c12"        # 橙色 - 值域
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_function_definition()
        self.show_domain_and_range()
        self.show_function_equality()
        self.show_function_graph()
        self.show_domain_rules()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的坐标"""
        # 集合A和B的椭圆中心
        self.set_A_center = np.array([-2.5, 2, 0])
        self.set_B_center = np.array([2.5, 2, 0])
        
        # 集合A中的点位置（均匀分布）
        self.points_A = [
            self.set_A_center + np.array([0, 0.8, 0]),   # x₁
            self.set_A_center + np.array([0, 0, 0]),     # x₂
            self.set_A_center + np.array([0, -0.8, 0])   # x₃
        ]
        
        # 集合B中的点位置
        self.points_B = [
            self.set_B_center + np.array([0, 0.8, 0]),   # y₁
            self.set_B_center + np.array([0, 0, 0]),     # y₂
            self.set_B_center + np.array([0, -0.8, 0])   # y₃
        ]
        
        # 验证几何设置
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        # 验证集合中心在安全区域内
        assert abs(self.set_A_center[0]) < 4, "集合A中心超出边界"
        assert abs(self.set_B_center[0]) < 4, "集合B中心超出边界"
        
        # 验证点在合理范围内
        for point in self.points_A + self.points_B:
            assert abs(point[0]) < 4.5, f"点{point}超出横向边界"
            assert abs(point[1]) < 8, f"点{point}超出纵向边界"
        
        print("✓ 几何验证通过")
    
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
        hook_question = Text(
            "什么是函数？",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # f(x) 符号
        fx_symbol = MathTex(
            r"f(x) = ?",
            font_size=64,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(FadeIn(fx_symbol, scale=1.2), run_time=0.6)
        self.play(Flash(fx_symbol, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(fx_symbol),
            run_time=0.5
        )
    
    def show_function_definition(self):
        """场景2: 函数的定义 - 对应关系"""
        # 标题
        title = Text(
            "函数 = 对应关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建集合A的椭圆
        ellipse_A = Ellipse(
            width=1.8, 
            height=3.0, 
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.set_A_center)
        
        label_A = MathTex("A", font_size=32, color=WHITE).next_to(ellipse_A, UP, buff=0.2)
        
        self.play(Create(ellipse_A), run_time=0.8)
        self.play(Write(label_A), run_time=0.3)
        
        # 集合A中的元素
        dots_A = VGroup()
        labels_A = VGroup()
        
        for i, point in enumerate(self.points_A):
            dot = Dot(point, color=WHITE, radius=0.08)
            label = MathTex(f"x_{{{i+1}}}", font_size=22).next_to(dot, LEFT, buff=0.15)
            dots_A.add(dot)
            labels_A.add(label)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_A], lag_ratio=0.2),
            run_time=0.6
        )
        self.play(
            LaggedStart(*[Write(label) for label in labels_A], lag_ratio=0.2),
            run_time=0.5
        )
        
        # 创建集合B的椭圆
        ellipse_B = Ellipse(
            width=1.8, 
            height=3.0, 
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).move_to(self.set_B_center)
        
        label_B = MathTex("B", font_size=32, color=WHITE).next_to(ellipse_B, UP, buff=0.2)
        
        self.play(Create(ellipse_B), run_time=0.8)
        self.play(Write(label_B), run_time=0.3)
        
        # 集合B中的元素
        dots_B = VGroup()
        labels_B = VGroup()
        
        for i, point in enumerate(self.points_B):
            dot = Dot(point, color=WHITE, radius=0.08)
            label = MathTex(f"y_{{{i+1}}}", font_size=22).next_to(dot, RIGHT, buff=0.15)
            dots_B.add(dot)
            labels_B.add(label)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_B], lag_ratio=0.2),
            run_time=0.6
        )
        self.play(
            LaggedStart(*[Write(label) for label in labels_B], lag_ratio=0.2),
            run_time=0.5
        )
        
        # 创建箭头表示对应关系
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                start=self.points_A[i] + RIGHT * 0.2,
                end=self.points_B[i] + LEFT * 0.2,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=3,
                buff=0,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(arrow)
        
        self.play(
            LaggedStart(*[Create(arrow) for arrow in arrows], lag_ratio=0.3),
            run_time=1.2
        )
        
        # 定义文字
        definition = Text(
            "A中每个元素x都有唯一的B中元素y与之对应",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(definition), run_time=1.5)
        
        # 关键公式
        formula_fx = MathTex(
            r"y = f(x), \quad x \in A",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(Write(formula_fx), run_time=0.8)
        self.wait(2.0)  # 理解停顿
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(formula_fx),
            run_time=0.5
        )
        
        # 淡化保留元素
        self.play(
            ellipse_A.animate.set_opacity(0.3),
            ellipse_B.animate.set_opacity(0.3),
            *[dot.animate.set_opacity(0.3) for dot in dots_A],
            *[dot.animate.set_opacity(0.3) for dot in dots_B],
            *[label.animate.set_opacity(0.3) for label in labels_A],
            *[label.animate.set_opacity(0.3) for label in labels_B],
            *[arrow.animate.set_opacity(0.3) for arrow in arrows],
            label_A.animate.set_opacity(0.3),
            label_B.animate.set_opacity(0.3),
            run_time=0.4
        )
        
        # 保存引用以便后续使用
        self.ellipse_A = ellipse_A
        self.ellipse_B = ellipse_B
        self.dots_A = dots_A
        self.dots_B = dots_B
        self.labels_A = labels_A
        self.labels_B = labels_B
        self.arrows = arrows
        self.label_A = label_A
        self.label_B = label_B
    
    def show_domain_and_range(self):
        """场景3: 定义域和值域"""
        # 标题
        title = Text(
            "定义域 & 值域",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 恢复集合A的不透明度并高亮
        self.play(
            self.ellipse_A.animate.set_opacity(1).set_color(self.COLOR_DOMAIN).set_stroke(width=5),
            *[dot.animate.set_opacity(1).set_color(self.COLOR_DOMAIN) for dot in self.dots_A],
            *[label.animate.set_opacity(1) for label in self.labels_A],
            self.label_A.animate.set_opacity(1),
            run_time=0.8
        )
        
        # "定义域"标签
        domain_label = Text(
            "定义域",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DOMAIN
        ).next_to(self.ellipse_A, DOWN, buff=0.3)
        
        self.play(Write(domain_label), run_time=0.5)
        
        # 定义域说明
        domain_explain = Text(
            "使f(x)有意义的x的集合",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(domain_explain), run_time=0.8)
        self.wait(1.0)
        
        # 恢复集合B的不透明度并高亮
        self.play(
            self.ellipse_B.animate.set_opacity(1).set_color(self.COLOR_RANGE).set_stroke(width=5),
            *[dot.animate.set_opacity(1).set_color(self.COLOR_RANGE) for dot in self.dots_B],
            *[label.animate.set_opacity(1) for label in self.labels_B],
            self.label_B.animate.set_opacity(1),
            *[arrow.animate.set_opacity(1) for arrow in self.arrows],
            run_time=0.8
        )
        
        # "值域"标签
        range_label = Text(
            "值域",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_RANGE
        ).next_to(self.ellipse_B, DOWN, buff=0.3)
        
        self.play(Write(range_label), run_time=0.5)
        
        # 值域说明
        range_explain = Text(
            "所有函数值y组成的集合",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(
            FadeOut(domain_explain),
            Write(range_explain),
            run_time=0.6
        )
        
        # 公式 - 使用Text和MathTex分开处理中文和数学
        domain_text = Text("定义域: ", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        domain_math = MathTex(r"\{x \mid x \in A\}", font_size=24)
        domain_group = VGroup(domain_text, domain_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 6)
        
        range_text = Text("值域: ", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        range_math = MathTex(r"\{y \mid y = f(x), x \in A\}", font_size=24)
        range_group = VGroup(range_text, range_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 6.8)
        
        self.play(
            Write(domain_group),
            run_time=0.8
        )
        self.play(
            Write(range_group),
            run_time=0.8
        )
        
        self.wait(2.5)  # 理解停顿
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(domain_label),
            FadeOut(range_label),
            FadeOut(range_explain),
            FadeOut(domain_group),
            FadeOut(range_group),
            FadeOut(self.ellipse_A),
            FadeOut(self.ellipse_B),
            FadeOut(self.dots_A),
            FadeOut(self.dots_B),
            FadeOut(self.labels_A),
            FadeOut(self.labels_B),
            FadeOut(self.arrows),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            run_time=0.6
        )
    
    def show_function_equality(self):
        """场景4: 函数相等的条件"""
        # 标题
        title = Text(
            "函数相等的条件",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 条件1
        condition_1 = Text(
            "① 定义域相同",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(condition_1), run_time=0.8)
        
        # 条件2
        condition_2 = Text(
            "② 对应法则相同",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Write(condition_2), run_time=0.8)
        
        # 重要提示框
        note_box = Rectangle(
            width=7,
            height=1.5,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 2.5)
        
        note_title = Text(
            "注意:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2 + LEFT * 2.5)
        
        note_content_1 = MathTex(
            r"f(x_1) = f(x_2)",
            font_size=26
        ).move_to(DOWN * 2.8)
        
        note_content_2_text = Text(
            "不要求",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        note_content_2_math = MathTex(
            r"x_1 = x_2",
            font_size=26
        )
        note_content_2 = VGroup(note_content_2_text, note_content_2_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.5)
        
        self.play(Create(note_box), run_time=0.5)
        self.play(
            Write(note_title),
            Write(note_content_1),
            Write(note_content_2),
            run_time=1.0
        )
        
        self.wait(2.0)  # 理解停顿
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition_1),
            FadeOut(condition_2),
            FadeOut(note_box),
            FadeOut(note_title),
            FadeOut(note_content_1),
            FadeOut(note_content_2),
            run_time=0.6
        )
    
    def show_function_graph(self):
        """场景5: 函数图像示例"""
        # 标题
        title = Text(
            "函数的图像",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "numbers_to_exclude": [0]
            }
        ).scale(0.7).shift(UP * 0.5)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=24).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_label = MathTex("y", font_size=24).next_to(axes.y_axis, UP, buff=0.1)
        
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=1.2
        )
        
        # 函数公式
        formula = MathTex(
            r"y = x^2",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 函数曲线
        graph = axes.plot(
            lambda x: x**2,
            x_range=[-2.2, 2.2],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(graph), run_time=2.0)
        
        # 定义域标注（x轴双向箭头）
        domain_arrow = DoubleArrow(
            start=axes.c2p(-2.2, -0.5),
            end=axes.c2p(2.2, -0.5),
            color=self.COLOR_DOMAIN,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.1
        )
        
        domain_text_cn = Text(
            "定义域: ",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_DOMAIN
        )
        domain_text_math = MathTex(
            r"\mathbb{R}",
            font_size=24,
            color=self.COLOR_DOMAIN
        )
        domain_text_group = VGroup(domain_text_cn, domain_text_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5 + LEFT * 2)
        
        self.play(Create(domain_arrow), run_time=0.6)
        self.play(Write(domain_text_group), run_time=0.6)
        
        # 值域标注（y轴箭头）
        range_arrow = Arrow(
            start=axes.c2p(-2.8, 0),
            end=axes.c2p(-2.8, 4.5),
            color=self.COLOR_RANGE,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.08
        )
        
        range_text_cn = Text(
            "值域: ",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_RANGE
        )
        range_text_math = MathTex(
            r"[0, +\infty)",
            font_size=24,
            color=self.COLOR_RANGE
        )
        range_text_group = VGroup(range_text_cn, range_text_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5 + RIGHT * 2)
        
        self.play(Create(range_arrow), run_time=0.6)
        self.play(Write(range_text_group), run_time=0.6)
        
        # 追踪点动画
        t = ValueTracker(-2)
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(t.get_value(), t.get_value()**2),
                color=self.COLOR_HIGHLIGHT,
                radius=0.08
            )
        )
        
        # 坐标标签
        coord_label = always_redraw(
            lambda: MathTex(
                f"({t.get_value():.1f}, {t.get_value()**2:.1f})",
                font_size=20,
                color=WHITE
            ).next_to(dot.get_center(), UR, buff=0.2)
        )
        
        self.add(dot, coord_label)
        self.play(t.animate.set_value(2), run_time=3, rate_func=smooth)
        
        self.wait(2.5)  # 理解停顿
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(formula),
            FadeOut(graph),
            FadeOut(domain_arrow),
            FadeOut(domain_text_group),
            FadeOut(range_arrow),
            FadeOut(range_text_group),
            FadeOut(dot),
            FadeOut(coord_label),
            run_time=0.6
        )
    
    def show_domain_rules(self):
        """场景6: 定义域的求法"""
        # 标题
        title = Text(
            "如何求定义域？",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 规则1
        rule_1_title = Text(
            "① 分母 ≠ 0",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        example_1_text = Text(
            "例: ",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        example_1_math = MathTex(
            r"f(x) = \frac{1}{x}",
            font_size=26
        )
        example_1 = VGroup(example_1_text, example_1_math).arrange(RIGHT, buff=0.1).move_to(UP * 3.2)
        
        domain_1_text = Text(
            "定义域: ",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        domain_1_math = MathTex(
            r"x \neq 0",
            font_size=24
        )
        domain_1 = VGroup(domain_1_text, domain_1_math).arrange(RIGHT, buff=0.1).move_to(UP * 2.4)
        
        self.play(Write(rule_1_title), run_time=0.8)
        self.play(Write(example_1), run_time=0.6)
        self.play(Write(domain_1), run_time=0.6)
        self.wait(0.5)
        
        # 规则2
        rule_2_title = Text(
            "② 偶次根号下 ≥ 0",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1)
        
        example_2_text = Text(
            "例: ",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        example_2_math = MathTex(
            r"f(x) = \sqrt{x}",
            font_size=26
        )
        example_2 = VGroup(example_2_text, example_2_math).arrange(RIGHT, buff=0.1).move_to(UP * 0.2)
        
        domain_2_text = Text(
            "定义域: ",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        domain_2_math = MathTex(
            r"x \geq 0",
            font_size=24
        )
        domain_2 = VGroup(domain_2_text, domain_2_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.6)
        
        self.play(Write(rule_2_title), run_time=0.8)
        self.play(Write(example_2), run_time=0.6)
        self.play(Write(domain_2), run_time=0.6)
        self.wait(0.5)
        
        # 规则3
        rule_3_title = Text(
            "③ 对数真数 > 0",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        example_3_text = Text(
            "例: ",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        example_3_math = MathTex(
            r"f(x) = \ln(x)",
            font_size=26
        )
        example_3 = VGroup(example_3_text, example_3_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.8)
        
        domain_3_text = Text(
            "定义域: ",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        domain_3_math = MathTex(
            r"x > 0",
            font_size=24
        )
        domain_3 = VGroup(domain_3_text, domain_3_math).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.6)
        
        self.play(Write(rule_3_title), run_time=0.8)
        self.play(Write(example_3), run_time=0.6)
        self.play(Write(domain_3), run_time=0.6)
        
        self.wait(2.5)  # 理解停顿
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule_1_title),
            FadeOut(example_1),
            FadeOut(domain_1),
            FadeOut(rule_2_title),
            FadeOut(example_2),
            FadeOut(domain_2),
            FadeOut(rule_3_title),
            FadeOut(example_3),
            FadeOut(domain_3),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结"""
        # 标题
        summary_title = Text(
            "函数三要素",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 创建三张卡片
        card_1 = self.create_summary_card(
            "定义域",
            "自变量x的取值范围",
            self.COLOR_DOMAIN,
            UP * 2.5
        )
        
        card_2 = self.create_summary_card(
            "值域",
            "函数值y的取值范围",
            self.COLOR_RANGE,
            UP * 0.5
        )
        
        card_3 = self.create_summary_card(
            "对应法则",
            "从x到y的对应关系",
            self.COLOR_PRIMARY,
            DOWN * 1.5
        )
        
        # 卡片依次滑入
        self.play(card_1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(card_2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(card_3.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 核心公式
        core_formula = MathTex(
            r"y = f(x), \quad x \in A",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(Write(core_formula), run_time=0.8)
        
        self.wait(2.0)  # 理解停顿
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(core_formula),
            run_time=0.6
        )
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        cta_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(cta_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素 - 小圆圈
        decorations = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_PRIMARY, fill_opacity=0.8)
            .move_to(cta_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(cta_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 渲染命令:
# manim -pql function_concepts.py FunctionConcepts  # 快速预览
# manim -qh function_concepts.py FunctionConcepts   # 高质量
# manim -qk function_concepts.py FunctionConcepts   # 4K质量
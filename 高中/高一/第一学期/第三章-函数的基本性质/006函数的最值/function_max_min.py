"""
函数的最值 - Function Maximum and Minimum Values
使用 Manim 创建的高中数学教学视频

内容: 函数最值的定义、求法和应用
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


class FunctionMaxMin(Scene):
    """
    函数最值教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义引入
    3. 坐标系与函数
    4. 标记最大值
    5. 对比端点值
    6. 方法总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主函数曲线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 最大值点
        self.COLOR_TERTIARY = "#2ecc71"     # 绿色 - 最小值点
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_AXES = WHITE             # 白色 - 坐标轴
        
        # 初始化数据
        self.setup_function_data()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_axes_and_function()
        self.show_maximum_value()
        self.show_endpoint_comparison()
        self.show_methods_summary()
        self.show_outro()
    
    def setup_function_data(self):
        """初始化函数和关键点数据"""
        # 坐标系配置
        self.AXES_CONFIG = {
            "x_range": [-3, 3, 1],
            "y_range": [-2, 4, 1],
            "x_length": 7,
            "y_length": 8,
            "axis_config": {
                "include_numbers": True,
                "font_size": 20,
                "color": self.COLOR_AXES,
            },
            "tips": False,
        }
        
        # 坐标系位置
        self.AXES_POSITION = UP * 0.5
        
        # 函数定义域
        self.DOMAIN_LEFT = -2
        self.DOMAIN_RIGHT = 2
        
        # 关键点坐标（数学坐标）
        self.max_point_math = np.array([1, 3, 0])  # 最大值点
        self.left_endpoint_math = np.array([-2, self.main_function(-2), 0])  # 左端点
        self.right_endpoint_math = np.array([2, self.main_function(2), 0])  # 右端点
        
        print("✓ 函数数据初始化完成")
    
    def main_function(self, x):
        """主函数: f(x) = -(x-1)² + 3"""
        return -(x - 1)**2 + 3
    
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
            "函数有最高点吗?",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简化曲线（示意图）
        simple_curve = VGroup()
        
        # 创建简单的抛物线示意
        curve_points = []
        for x in np.linspace(-1.5, 1.5, 30):
            y = -x**2 + 2
            curve_points.append([x * 1.5, y * 1.2 + 2.5, 0])
        
        simple_curve = VMobject(color=self.COLOR_PRIMARY, stroke_width=4)
        simple_curve.set_points_smoothly(curve_points)
        
        self.play(Create(simple_curve), run_time=1.0)
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.5)
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.3)
        
        self.wait(1.4)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(simple_curve),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 定义引入"""
        # 标题
        title = Text(
            "函数的最值",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义1: 最大值
        def_1 = Text(
            "最大值: 函数在定义域内的最高点",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.2)
        
        formula_1 = MathTex(
            r"\forall x \in D, \; f(x) \leq f(x_0)",
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(def_1, shift=UP * 0.2), run_time=0.6)
        self.play(Write(formula_1), run_time=1.0)
        
        # 定义2: 最小值
        def_2 = Text(
            "最小值: 函数在定义域内的最低点",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        formula_2 = MathTex(
            r"\forall x \in D, \; f(x) \geq f(x_0)",
            font_size=26,
            color=WHITE
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(def_2, shift=UP * 0.2), run_time=0.6)
        self.play(Write(formula_2), run_time=1.0)
        
        # 关键提示
        note = Text(
            "注意: 最值是整体概念!",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(note), run_time=0.5)
        self.wait(3.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def_1),
            FadeOut(formula_1),
            FadeOut(def_2),
            FadeOut(formula_2),
            FadeOut(note),
            run_time=0.6
        )
    
    def show_axes_and_function(self):
        """场景3: 坐标系与函数"""
        # 创建坐标轴
        self.axes = Axes(**self.AXES_CONFIG).move_to(self.AXES_POSITION)
        
        self.play(Create(self.axes), run_time=1.2)
        
        # 绘制函数曲线（闭区间 [-2, 2]）
        self.graph = self.axes.plot(
            self.main_function,
            x_range=[self.DOMAIN_LEFT, self.DOMAIN_RIGHT],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(self.graph), run_time=1.5)
        
        # 函数标签
        func_label = MathTex(
            r"f(x) = -(x-1)^2 + 3",
            font_size=24,
            color=WHITE
        ).next_to(self.axes, UP, buff=0.3).shift(RIGHT * 1.5)
        
        self.play(FadeIn(func_label), run_time=0.5)
        
        # 定义域标注
        domain_brace = Brace(
            Line(
                self.axes.c2p(self.DOMAIN_LEFT, 0),
                self.axes.c2p(self.DOMAIN_RIGHT, 0)
            ),
            direction=DOWN,
            buff=0.1,
            color=self.COLOR_AUXILIARY
        )
        
        domain_text = MathTex(
            r"x \in [-2, 2]",
            font_size=20,
            color=GRAY_A
        ).next_to(domain_brace, DOWN, buff=0.1)
        
        self.play(
            Create(domain_brace),
            Write(domain_text),
            run_time=0.8
        )
        
        # 端点标记
        left_dot = Dot(
            self.axes.c2p(self.DOMAIN_LEFT, self.main_function(self.DOMAIN_LEFT)),
            color=self.COLOR_PRIMARY,
            radius=0.08
        )
        
        right_dot = Dot(
            self.axes.c2p(self.DOMAIN_RIGHT, self.main_function(self.DOMAIN_RIGHT)),
            color=self.COLOR_PRIMARY,
            radius=0.08
        )
        
        self.play(
            FadeIn(left_dot),
            FadeIn(right_dot),
            run_time=0.5
        )
        
        self.wait(3.5)
        
        # 清理（保留主要元素）
        self.play(
            FadeOut(func_label),
            FadeOut(domain_brace),
            FadeOut(domain_text),
            FadeOut(left_dot),
            FadeOut(right_dot),
            run_time=0.4
        )
    
    def show_maximum_value(self):
        """场景4: 标记最大值"""
        # 扫描动画 - 小点沿曲线移动寻找最高点
        t = ValueTracker(self.DOMAIN_LEFT)
        
        scanning_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(t.get_value(), self.main_function(t.get_value())),
                color=YELLOW,
                radius=0.06
            )
        )
        
        self.add(scanning_dot)
        self.play(t.animate.set_value(1), run_time=1.5, rate_func=smooth)
        
        # 最大值点
        max_coords = self.axes.c2p(1, 3)
        max_dot = Dot(max_coords, color=self.COLOR_SECONDARY, radius=0.12)
        
        self.play(
            FadeIn(max_dot, scale=0.5),
            FadeOut(scanning_dot),
            run_time=0.6
        )
        self.play(Flash(max_dot, color=self.COLOR_SECONDARY, flash_radius=0.3), run_time=0.4)
        
        # 虚线辅助线
        v_line = DashedLine(
            max_coords,
            self.axes.c2p(1, 0),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        h_line = DashedLine(
            max_coords,
            self.axes.c2p(0, 3),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(v_line), Create(h_line), run_time=0.8)
        
        # 坐标标签
        x_label = MathTex(r"x_0 = 1", font_size=20, color=WHITE).next_to(
            self.axes.c2p(1, 0), DOWN, buff=0.2
        )
        
        y_label = MathTex(r"f(x_0) = 3", font_size=20, color=WHITE).next_to(
            self.axes.c2p(0, 3), LEFT, buff=0.2
        )
        
        self.play(Write(x_label), Write(y_label), run_time=0.6)
        
        # 最大值说明
        max_text = Text(
            "最大值: f(1) = 3",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 3.5)
        
        max_formula = MathTex(
            r"\forall x \in [-2,2], \; f(x) \leq 3",
            font_size=22,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(max_text), run_time=0.5)
        self.play(Write(max_formula), run_time=0.8)
        
        # 高亮闪烁
        self.play(Indicate(max_dot, color=self.COLOR_SECONDARY), run_time=0.5)
        
        self.wait(6.7)
        
        # 清理
        self.play(
            FadeOut(v_line),
            FadeOut(h_line),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(max_text),
            FadeOut(max_formula),
            run_time=0.5
        )
        
        # 保留最大值点
        self.max_dot = max_dot
    
    def show_endpoint_comparison(self):
        """场景5: 对比端点值"""
        # 端点标记
        left_coords = self.axes.c2p(self.DOMAIN_LEFT, self.main_function(self.DOMAIN_LEFT))
        right_coords = self.axes.c2p(self.DOMAIN_RIGHT, self.main_function(self.DOMAIN_RIGHT))
        
        left_dot = Dot(left_coords, color=self.COLOR_TERTIARY, radius=0.10)
        right_dot = Dot(right_coords, color=self.COLOR_TERTIARY, radius=0.10)
        
        # 端点强调
        self.play(
            FadeIn(left_dot, scale=0.5),
            FadeIn(right_dot, scale=0.5),
            run_time=0.8
        )
        
        self.play(
            Indicate(left_dot, color=self.COLOR_TERTIARY),
            Indicate(right_dot, color=self.COLOR_TERTIARY),
            run_time=0.8
        )
        
        # 端点值标签
        left_value = MathTex(
            r"f(-2) = -6",
            font_size=20,
            color=self.COLOR_TERTIARY
        ).next_to(left_dot, LEFT, buff=0.2)
        
        right_value = MathTex(
            r"f(2) = 2",
            font_size=20,
            color=self.COLOR_TERTIARY
        ).next_to(right_dot, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(left_value),
            FadeIn(right_value),
            run_time=0.6
        )
        
        # 对比箭头（从端点指向最大值点）
        arrow_1 = Arrow(
            left_coords,
            self.max_dot.get_center(),
            color=self.COLOR_AUXILIARY,
            buff=0.15,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow_2 = Arrow(
            right_coords,
            self.max_dot.get_center(),
            color=self.COLOR_AUXILIARY,
            buff=0.15,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_1), GrowArrow(arrow_2), run_time=0.8)
        
        # 说明文字
        explain_1 = Text(
            "端点值: f(-2) = -6",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5 + LEFT * 2)
        
        explain_2 = Text(
            "端点值: f(2) = 2",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5 + RIGHT * 2)
        
        self.play(FadeIn(explain_1), FadeIn(explain_2), run_time=0.5)
        
        # 总结
        summary = Text(
            "最大值在顶点, 最小值在左端点!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(summary, scale=1.1), run_time=0.6)
        
        self.wait(9.2)
        
        # 清理
        self.play(
            FadeOut(left_dot),
            FadeOut(right_dot),
            FadeOut(left_value),
            FadeOut(right_value),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(summary),
            FadeOut(self.max_dot),
            FadeOut(self.axes),
            FadeOut(self.graph),
            run_time=0.6
        )
    
    def show_methods_summary(self):
        """场景6: 方法总结"""
        # 标题
        methods_title = Text(
            "求最值的方法",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(methods_title), run_time=0.5)
        
        # 方法卡片
        cards = VGroup()
        
        # 方法1
        card_1 = self.create_method_card(
            "① 单调性 (闭区间端点)",
            UP * 3
        )
        cards.add(card_1)
        
        # 方法2
        card_2 = self.create_method_card(
            "② 配方法 (二次函数)",
            UP * 2
        )
        cards.add(card_2)
        
        # 方法3
        card_3 = self.create_method_card(
            "③ 基本不等式",
            UP * 1
        )
        cards.add(card_3)
        
        # 方法4
        card_4 = self.create_method_card(
            "④ 数形结合 (图像法)",
            ORIGIN
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 关键提示
        key_note = Text(
            "记住: 最值≠极值!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(key_note, scale=1.1), run_time=0.6)
        
        self.wait(12.3)
        
        # 清理
        self.play(
            FadeOut(methods_title),
            FadeOut(cards),
            FadeOut(key_note),
            run_time=0.6
        )
    
    def create_method_card(self, text, position):
        """创建方法卡片"""
        # 图标
        icon = Circle(radius=0.15, fill_color=self.COLOR_PRIMARY, fill_opacity=1, stroke_width=0)
        
        # 文字
        text_obj = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, text_obj).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
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
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素 - 小圆圈
        decorations = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_PRIMARY, fill_opacity=0.6)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        # 图标
        icon_size = 0.25
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_SECONDARY, fill_opacity=0.8).shift(LEFT * 1.5),
            Circle(radius=icon_size, color=self.COLOR_PRIMARY, fill_opacity=0.8).shift(LEFT * 0.75),
            Circle(radius=icon_size, color=self.COLOR_HIGHLIGHT, fill_opacity=0.8),
            Circle(radius=icon_size, color=self.COLOR_PRIMARY, fill_opacity=0.8).shift(RIGHT * 0.75),
            Circle(radius=icon_size, color=self.COLOR_TERTIARY, fill_opacity=0.8).shift(RIGHT * 1.5)
        ).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql function_max_min.py FunctionMaxMin  # 快速预览
# manim -qh function_max_min.py FunctionMaxMin   # 高质量
# manim -qk function_max_min.py FunctionMaxMin   # 4K质量
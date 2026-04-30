"""
二次函数的应用 - Quadratic Function Applications
使用 Manim 创建的中学数学教学视频

内容: 二次函数在实际问题中的应用 - 最值问题
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

主要场景:
1. 开场钩子 - 引出问题
2. 二次函数基础复习
3. 顶点公式推导
4. 实际问题引入
5. 建立函数模型
6. 答案解读
7. 片尾总结
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16






class QuadraticFunctionApplication(Scene):
    """
    二次函数应用教学动画场景
    
    展示二次函数在利润最大化问题中的应用
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主抛物线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 顶点/最值点
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 重点标注
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_PROFIT = "#2ecc71"       # 绿色 - 利润线
        self.COLOR_AXES = WHITE             # 白色 - 坐标轴
        
        # 字体大小
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "small": 18,
            "formula": 28,
        }
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()          # Scene 1: 开场钩子
        self.show_basic_parabola()   # Scene 2: 基础复习
        self.show_vertex_formula()   # Scene 3: 顶点公式
        self.show_problem_intro()    # Scene 4: 实际问题
        self.show_model_building()   # Scene 5: 建立模型
        self.show_answer_analysis()  # Scene 6: 答案解读
        self.show_outro()            # Scene 7: 片尾总结
    
    def setup_geometry(self):
        """初始化所有几何数据 - 统一计算，避免重复"""
        
        # ========== 基础抛物线参数 ==========
        self.a_basic = -1
        self.b_basic = 4
        self.c_basic = 5
        
        # 顶点计算
        self.vertex_x_basic = -self.b_basic / (2 * self.a_basic)  # = 2
        self.vertex_y_basic = (self.a_basic * self.vertex_x_basic**2 + 
                               self.b_basic * self.vertex_x_basic + 
                               self.c_basic)  # = 9
        
        # ========== 实际问题参数 ==========
        # 原始问题: P = (x-30)(100-2x) = -2x² + 160x - 3000
        # 为了显示方便，我们使用缩放版本: P = -2x² + 20x - 30
        self.a_profit = -2
        self.b_profit = 20
        self.c_profit = -30
        
        # 最优解
        self.optimal_price = -self.b_profit / (2 * self.a_profit)  # = 5
        self.max_profit = (self.a_profit * self.optimal_price**2 + 
                          self.b_profit * self.optimal_price + 
                          self.c_profit)  # = 20
        
        # 盈亏平衡点（P = 0的根）
        discriminant = self.b_profit**2 - 4 * self.a_profit * self.c_profit
        sqrt_disc = np.sqrt(discriminant)
        x1 = (-self.b_profit - sqrt_disc) / (2 * self.a_profit)
        x2 = (-self.b_profit + sqrt_disc) / (2 * self.a_profit)
        self.breakeven_points = sorted([x1, x2])  # [1.8377, 8.1623]
        
        # 实际问题的原始参数（用于说明）
        self.cost = 30           # 进价
        self.base_sales = 100    # 基础销量
        self.actual_optimal_price = 40   # 实际最优价格
        self.actual_max_profit = 200     # 实际最大利润
        
        print("✓ 几何数据初始化完成")
        print(f"  基础抛物线顶点: ({self.vertex_x_basic}, {self.vertex_y_basic})")
        print(f"  利润函数最优解: x={self.optimal_price}, P_max={self.max_profit}")
    
    def show_opening(self):
        """Scene 1: 开场钩子 (0-5秒)"""
        
        # 作者信息 (顶部，持续显示)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题 - 吸引注意
        hook_text = Text(
            "如何定价才能赚最多钱？",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # 简单的曲线示意图
        sketch_axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 25, 5],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False, "stroke_width": 2}
        ).scale(0.6).move_to(UP * 2)
        
        curve_sketch = sketch_axes.plot(
            lambda x: -0.5 * (x - 5)**2 + 20,
            x_range=[1, 9],
            color=self.COLOR_PROFIT,
            stroke_width=5
        )
        
        # 标注最高点
        peak_point = sketch_axes.c2p(5, 20)
        peak_dot = Dot(peak_point, color=self.COLOR_SECONDARY, radius=0.15)
        peak_label = Text(
            "最高点?",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SECONDARY
        ).next_to(peak_dot, UP, buff=0.2)
        
        self.play(Create(curve_sketch), run_time=1.0)
        self.play(
            FadeIn(peak_dot, scale=0.5),
            FadeIn(peak_label, shift=DOWN * 0.2),
            run_time=0.5
        )
        
        self.wait(1.4)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(sketch_axes),
            FadeOut(curve_sketch),
            FadeOut(peak_dot),
            FadeOut(peak_label),
            run_time=0.5
        )
    
    def show_basic_parabola(self):
        """Scene 2: 二次函数基础复习 (5-15秒)"""
        
        # 标题
        title = Text(
            "二次函数基础",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=8,
            axis_config={
                "include_numbers": True,
                "font_size": self.FONT_SIZES["label"],
                "stroke_width": 2
            }
        ).shift(DOWN * 0.5)
        
        # 坐标轴标签
        x_label = axes.get_x_axis_label("x", direction=RIGHT, buff=0.2)
        y_label = axes.get_y_axis_label("y", direction=UP, buff=0.2)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.0)
        
        # 绘制抛物线 y = -x² + 4x + 5
        parabola = axes.plot(
            lambda x: -x**2 + 4*x + 5,
            x_range=[-0.5, 4.5],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(parabola), run_time=1.5)
        
        # 标注顶点
        vertex_point = axes.c2p(self.vertex_x_basic, self.vertex_y_basic)
        vertex_dot = Dot(vertex_point, color=self.COLOR_SECONDARY, radius=0.12)
        vertex_label = MathTex(
            r"(2, 9)",
            font_size=self.FONT_SIZES["label"],
            color=self.COLOR_SECONDARY
        ).next_to(vertex_dot, UR, buff=0.15)
        
        self.play(
            FadeIn(vertex_dot, scale=0.5),
            Write(vertex_label),
            run_time=0.8
        )
        
        # 对称轴
        axis_line = DashedLine(
            axes.c2p(self.vertex_x_basic, 0),
            axes.c2p(self.vertex_x_basic, 10),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        axis_label = Text(
            "对称轴",
            font="PingFang SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_AUXILIARY
        ).next_to(axes.c2p(self.vertex_x_basic, 0), DOWN, buff=0.2)
        
        self.play(Create(axis_line), FadeIn(axis_label), run_time=0.8)
        
        # 公式显示
        formula = MathTex(
            r"y = -x^2 + 4x + 5",
            font_size=self.FONT_SIZES["formula"],
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 最值说明
        max_text = Text(
            "a < 0，有最大值",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula, DOWN, buff=0.3)
        
        max_value = MathTex(
            r"y_{\max} = 9",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SECONDARY
        ).next_to(max_text, DOWN, buff=0.2)
        
        self.play(FadeIn(max_text), FadeIn(max_value), run_time=0.6)
        
        self.wait(1.8)
        
        # 清理（保留部分元素供参考）
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(max_text),
            FadeOut(max_value),
            FadeOut(axis_label),
            axes.animate.scale(0.7).move_to(UP * 5 + RIGHT * 3),
            parabola.animate.scale(0.7).move_to(UP * 5 + RIGHT * 3),
            vertex_dot.animate.scale(0.5).move_to(
                axes.c2p(self.vertex_x_basic, self.vertex_y_basic) * 0.7 + UP * 5 + RIGHT * 3
            ),
            vertex_label.animate.scale(0.6).next_to(
                axes.c2p(self.vertex_x_basic, self.vertex_y_basic) * 0.7 + UP * 5 + RIGHT * 3,
                UR, buff=0.1
            ),
            axis_line.animate.scale(0.7).move_to(UP * 5 + RIGHT * 3),
            x_label.animate.scale(0.7).move_to(UP * 5 + RIGHT * 3),
            y_label.animate.scale(0.7).move_to(UP * 5 + RIGHT * 3),
            run_time=0.6
        )
        
        # 保存引用（缩小后的）
        self.axes_ref = VGroup(axes, parabola, vertex_dot, vertex_label, axis_line, x_label, y_label)
    
    def show_vertex_formula(self):
        """Scene 3: 顶点公式推导 (15-25秒)"""
        
        # 通用公式
        general_formula = MathTex(
            r"y = {{ a }}x^2 + {{ b }}x + {{ c }}",
            font_size=self.FONT_SIZES["title"],
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(general_formula), run_time=1.0)
        
        # 标注系数 - 安全地处理MathTex结构以避免索引错误
        # 先检查是否有足够的子对象
        try:
            # 检查general_formula结构
            if hasattr(general_formula, 'submobjects') and len(general_formula.submobjects) > 0:
                first_part = general_formula.submobjects[0]
                if hasattr(first_part, '__len__'):
                    num_elements = len(first_part)
                    if num_elements > 10:
                        a_box = SurroundingRectangle(first_part[2], color=RED, buff=0.1)   # 'a' coefficient
                        b_box = SurroundingRectangle(first_part[6], color=BLUE, buff=0.1)  # 'b' coefficient
                        c_box = SurroundingRectangle(first_part[10], color=GREEN, buff=0.1) # 'c' coefficient
                    elif num_elements > 6:
                        a_box = SurroundingRectangle(first_part[2], color=RED, buff=0.1)   # 'a' coefficient
                        b_box = SurroundingRectangle(first_part[4], color=BLUE, buff=0.1)  # estimate 'b' position
                        c_box = SurroundingRectangle(first_part[6], color=GREEN, buff=0.1)  # estimate 'c' position
                    elif num_elements > 2:
                        a_box = SurroundingRectangle(first_part[0], color=RED, buff=0.1)   # estimate positions
                        b_box = SurroundingRectangle(first_part[1], color=BLUE, buff=0.1)
                        c_box = SurroundingRectangle(first_part[2], color=GREEN, buff=0.1)
                    else:
                        # 如果仍然没有足够的元素，使用整个公式作为后备
                        a_box = SurroundingRectangle(general_formula, color=RED, buff=0.1)
                        b_box = SurroundingRectangle(general_formula, color=BLUE, buff=0.1)
                        c_box = SurroundingRectangle(general_formula, color=GREEN, buff=0.1)
                else:
                    # 如果first_part没有长度属性，使用整个公式
                    a_box = SurroundingRectangle(general_formula, color=RED, buff=0.1)
                    b_box = SurroundingRectangle(general_formula, color=BLUE, buff=0.1)
                    c_box = SurroundingRectangle(general_formula, color=GREEN, buff=0.1)
            else:
                # 如果没有子对象，使用整个公式
                a_box = SurroundingRectangle(general_formula, color=RED, buff=0.1)
                b_box = SurroundingRectangle(general_formula, color=BLUE, buff=0.1)
                c_box = SurroundingRectangle(general_formula, color=GREEN, buff=0.1)
        except (IndexError, AttributeError):
            # 捕获任何可能的索引或属性错误，使用安全后备
            a_box = SurroundingRectangle(general_formula, color=RED, buff=0.1)
            b_box = SurroundingRectangle(general_formula, color=BLUE, buff=0.1)
            c_box = SurroundingRectangle(general_formula, color=GREEN, buff=0.1)
        
        self.play(
            Create(a_box),
            Create(b_box),
            Create(c_box),
            run_time=1.2
        )
        self.wait(0.3)
        self.play(FadeOut(a_box), FadeOut(b_box), FadeOut(c_box), run_time=0.3)
        
        # 顶点x坐标公式
        vertex_formula_parts = VGroup(
            MathTex("x", font_size=self.FONT_SIZES["formula"], color=self.COLOR_SECONDARY),
            Text("顶点", font="PingFang SC", font_size=self.FONT_SIZES["small"], color=self.COLOR_SECONDARY),
            MathTex("= -\\frac{b}{2a}", font_size=self.FONT_SIZES["formula"], color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)
        
        self.play(TransformFromCopy(general_formula, vertex_formula_parts), run_time=1.0)
        
        # 代入示例数值
        example_text = Text(
            "示例: a=-1, b=4, c=5",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 2.3)
        
        self.play(Write(example_text), run_time=0.8)
        
        # 计算步骤
        calc_step1_parts = VGroup(
            MathTex("x", font_size=self.FONT_SIZES["body"], color=WHITE),
            Text("顶点", font="PingFang SC", font_size=self.FONT_SIZES["small"], color=WHITE),
            MathTex("= -\\frac{4}{2 \\times (-1)} = 2", font_size=self.FONT_SIZES["body"], color=WHITE)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.2)
        
        self.play(Write(calc_step1_parts), run_time=0.8)
        
        # y坐标计算
        y_calc_parts = VGroup(
            MathTex("y", font_size=self.FONT_SIZES["body"], color=WHITE),
            Text("顶点", font="PingFang SC", font_size=self.FONT_SIZES["small"], color=WHITE),
            MathTex("= -(2)^2 + 4(2) + 5 = 9", font_size=self.FONT_SIZES["body"], color=WHITE)
        ).arrange(RIGHT, buff=0.1).move_to(ORIGIN)
        
        self.play(Write(y_calc_parts), run_time=1.0)
        
        # 最终顶点
        final_vertex = Text(
            "顶点: (2, 9)",
            font="PingFang SC",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(DOWN * 1.5)
        
        box = SurroundingRectangle(final_vertex, color=self.COLOR_HIGHLIGHT, buff=0.2)
        
        self.play(
            FadeIn(final_vertex, scale=1.2),
            Create(box),
            run_time=0.6
        )
        
        self.wait(1.6)
        
        # 清理
        self.play(
            FadeOut(general_formula),
            FadeOut(vertex_formula_parts),
            FadeOut(example_text),
            FadeOut(calc_step1_parts),
            FadeOut(y_calc_parts),
            FadeOut(final_vertex),
            FadeOut(box),
            FadeOut(self.axes_ref),
            run_time=0.6
        )
    
    def show_problem_intro(self):
        """Scene 4: 实际问题引入 (25-35秒)"""
        
        # 问题标题
        problem_title = Text(
            "实际应用: 利润最大化",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_PROFIT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(problem_title), run_time=0.8)
        
        # 问题详情
        problem_lines = VGroup(
            Text("某商店销售商品:", font="PingFang SC", font_size=self.FONT_SIZES["body"]),
            Text("• 进价: 30元/件", font="PingFang SC", font_size=self.FONT_SIZES["body"]),
            Text("• 定价: x 元/件", font="PingFang SC", font_size=self.FONT_SIZES["body"]),
            Text("• 销量: 100-2x 件/天", font="PingFang SC", font_size=self.FONT_SIZES["body"]),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 4)
        
        question = Text(
            "如何定价使每天利润最大？",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(problem_lines, shift=UP * 0.3, lag_ratio=0.2), run_time=1.0)
        self.wait(1.5)
        self.play(Write(question), run_time=0.8)
        self.wait(1.0)
        
        # 提示
        hint_text = Text(
            "用二次函数建模!",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 0.5)
        
        arrow = Arrow(
            hint_text.get_top(),
            hint_text.get_top() + UP * 0.8,
            color=self.COLOR_PRIMARY,
            buff=0
        )
        
        self.play(
            Write(hint_text),
            GrowArrow(arrow),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(problem_title),
            FadeOut(problem_lines),
            FadeOut(question),
            FadeOut(hint_text),
            FadeOut(arrow),
            run_time=0.5
        )
    
    def show_model_building(self):
        """Scene 5: 建立函数模型 (35-48秒)"""
        
        # 利润公式推导
        derivation_title = Text(
            "建立利润函数",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_PROFIT
        ).move_to(UP * 6.5)
        
        self.play(Write(derivation_title), run_time=0.6)
        
        # 推导步骤
        step1_parts = VGroup(
            MathTex("P =", font_size=self.FONT_SIZES["body"], color=WHITE),
            Text("(售价 - 成本) × 销量", font="PingFang SC", font_size=self.FONT_SIZES["body"], color=WHITE)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5)
        
        self.play(Write(step1_parts), run_time=1.5)
        
        step2 = MathTex(
            r"P = (x - 30)(100 - 2x)",
            font_size=self.FONT_SIZES["formula"],
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(TransformFromCopy(step1_parts, step2), run_time=1.0)
        
        step3 = MathTex(
            r"P = -2x^2 + 160x - 3000",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_PROFIT
        ).move_to(UP * 2.6)
        
        self.play(TransformFromCopy(step2, step3), run_time=1.0)
        
        # 创建坐标系
        profit_axes = Axes(
            x_range=[0, 60, 10],
            y_range=[-200, 300, 100],
            x_length=7,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": self.FONT_SIZES["small"],
                "stroke_width": 2
            }
        ).shift(DOWN * 1.5)
        
        x_label = profit_axes.get_x_axis_label(
            Text("价格(元)", font="PingFang SC", font_size=self.FONT_SIZES["small"]),
            direction=RIGHT,
            buff=0.3
        )
        y_label = profit_axes.get_y_axis_label(
            Text("利润(元)", font="PingFang SC", font_size=self.FONT_SIZES["small"]),
            direction=UP,
            buff=0.3
        )
        
        self.play(
            FadeOut(step1_parts),
            FadeOut(step2),
            Create(profit_axes),
            Write(x_label),
            Write(y_label),
            run_time=1.0
        )
        
        # 绘制利润曲线
        profit_parabola = profit_axes.plot(
            lambda x: -2*x**2 + 160*x - 3000,
            x_range=[25, 55],
            color=self.COLOR_PROFIT,
            stroke_width=5
        )
        
        self.play(Create(profit_parabola), run_time=1.8)
        
        # 标注顶点
        optimal_point = profit_axes.c2p(self.actual_optimal_price, self.actual_max_profit)
        optimal_dot = Dot(optimal_point, color=self.COLOR_SECONDARY, radius=0.15)
        
        optimal_label = VGroup(
            Text("最优点", font="PingFang SC", font_size=self.FONT_SIZES["label"], color=self.COLOR_SECONDARY),
            MathTex(r"(40, 200)", font_size=self.FONT_SIZES["label"], color=self.COLOR_SECONDARY)
        ).arrange(DOWN, buff=0.1).next_to(optimal_dot, UR, buff=0.2)
        
        self.play(
            FadeIn(optimal_dot, scale=0.5),
            Flash(optimal_dot, color=self.COLOR_SECONDARY, flash_radius=0.4),
            run_time=0.8
        )
        self.play(Write(optimal_label), run_time=0.8)
        
        # 垂直线到x轴
        vertical_line = DashedLine(
            optimal_point,
            profit_axes.c2p(self.actual_optimal_price, 0),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(vertical_line), run_time=0.6)
        
        # 计算说明
        calc_text = MathTex(
            r"x = -\frac{160}{2 \times (-2)} = 40",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(Write(calc_text), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理部分元素
        self.play(
            FadeOut(derivation_title),
            FadeOut(step3),
            FadeOut(calc_text),
            run_time=0.5
        )
        
        # 保存引用
        self.profit_axes = profit_axes
        self.profit_parabola = profit_parabola
        self.optimal_dot = optimal_dot
        self.optimal_label = optimal_label
        self.vertical_line = vertical_line
        self.x_label_profit = x_label
        self.y_label_profit = y_label
    
    def show_answer_analysis(self):
        """Scene 6: 答案解读 (48-58秒)"""
        
        # 答案框
        answer_box = RoundedRectangle(
            width=6,
            height=2.5,
            corner_radius=0.2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(UP * 5.5)
        
        answer_title = Text(
            "最优方案",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.3)
        
        answer_price = Text(
            "定价: 40元/件",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 5.6)
        
        answer_profit = Text(
            "最大利润: 200元/天",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_PROFIT,
            weight=BOLD
        ).move_to(UP * 4.9)
        
        self.play(Create(answer_box), run_time=0.8)
        self.play(
            Write(answer_title),
            Write(answer_price),
            Write(answer_profit),
            run_time=0.8
        )
        
        # 盈亏平衡点（实际问题中）
        # P = 0: -2x² + 160x - 3000 = 0
        # x² - 80x + 1500 = 0
        # (x-30)(x-50) = 0
        breakeven_1 = self.profit_axes.c2p(30, 0)
        breakeven_2 = self.profit_axes.c2p(50, 0)
        
        bp1_dot = Dot(breakeven_1, color=BLUE, radius=0.1)
        bp2_dot = Dot(breakeven_2, color=BLUE, radius=0.1)
        
        bp1_label = MathTex(r"30", font_size=self.FONT_SIZES["small"], color=BLUE).next_to(bp1_dot, DOWN, buff=0.1)
        bp2_label = MathTex(r"50", font_size=self.FONT_SIZES["small"], color=BLUE).next_to(bp2_dot, DOWN, buff=0.1)
        
        self.play(
            FadeIn(bp1_dot),
            FadeIn(bp2_dot),
            Write(bp1_label),
            Write(bp2_label),
            run_time=0.6
        )
        
        # 盈利区间高亮
        profit_zone = self.profit_axes.get_area(
            self.profit_parabola,
            x_range=[30, 50],
            color=self.COLOR_PROFIT,
            opacity=0.3
        )
        
        range_text = Text(
            "盈利区间: 30-50元",
            font="PingFang SC",
            font_size=self.FONT_SIZES["body"],
            color=BLUE
        ).move_to(UP * 3.8)
        
        self.play(
            FadeIn(profit_zone),
            Write(range_text),
            run_time=1.0
        )
        
        # 结论
        conclusion = Text(
            "二次函数找到最优解！",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(conclusion, scale=1.1), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                answer_box, answer_title, answer_price, answer_profit,
                range_text, conclusion,
                self.profit_axes, self.profit_parabola, self.optimal_dot, self.optimal_label,
                self.vertical_line, self.x_label_profit, self.y_label_profit,
                bp1_dot, bp2_dot, bp1_label, bp2_label, profit_zone
            )),
            run_time=0.8
        )
    
    def show_outro(self):
        """Scene 7: 片尾总结 (58-65秒)"""
        
        # 总结标题
        summary_title = Text(
            "二次函数应用三步法",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 三个步骤
        step1 = VGroup(
            Text("1", font="PingFang SC", font_size=self.FONT_SIZES["subtitle"], color=YELLOW, weight=BOLD),
            Text("建立函数模型", font="PingFang SC", font_size=self.FONT_SIZES["body"])
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        step2 = VGroup(
            Text("2", font="PingFang SC", font_size=self.FONT_SIZES["subtitle"], color=YELLOW, weight=BOLD),
            Text("求顶点坐标", font="PingFang SC", font_size=self.FONT_SIZES["body"]),
            MathTex(r"x = -\frac{b}{2a}", font_size=self.FONT_SIZES["body"], color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.3)
        
        step3 = VGroup(
            Text("3", font="PingFang SC", font_size=self.FONT_SIZES["subtitle"], color=YELLOW, weight=BOLD),
            Text("解释实际意义", font="PingFang SC", font_size=self.FONT_SIZES["body"])
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.1)
        
        self.play(FadeIn(step1, shift=RIGHT * 0.5), run_time=0.5)
        self.play(FadeIn(step2, shift=RIGHT * 0.5), run_time=0.5)
        self.play(FadeIn(step3, shift=RIGHT * 0.5), run_time=0.5)
        
        # 关键公式
        key_formula = VGroup(
            MathTex(r"a < 0 \Rightarrow", font_size=self.FONT_SIZES["body"]),
            Text("最大值", font="PingFang SC", font_size=self.FONT_SIZES["body"], color=RED),
            MathTex(r"\quad a > 0 \Rightarrow", font_size=self.FONT_SIZES["body"]),
            Text("最小值", font="PingFang SC", font_size=self.FONT_SIZES["body"], color=BLUE)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)
        
        self.play(Write(key_formula), run_time=0.8)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=GRAY_B
        ).move_to(DOWN * 4)
        
        self.play(
            FadeOut(self.author_info),
            FadeIn(author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(follow_text, scale=1.2), run_time=0.6)
        
        # 小图标动画
        icon_group = VGroup(
            *[Circle(radius=0.2, color=c, fill_opacity=0.8)
              for c in [self.COLOR_PRIMARY, self.COLOR_PROFIT, self.COLOR_SECONDARY]]
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 6.8)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icon_group],
            run_time=0.6
        )
        self.play(Rotate(icon_group, angle=PI, run_time=1.0))
        
        self.wait(1.1)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(
                summary_title, step1, step2, step3, key_formula,
                author_large, author_id, follow_text, icon_group
            )),
            run_time=1.0
        )


# 如果直接运行此文件
if __name__ == "__main__":
    # 使用以下命令渲染:
    # manim -pql quadratic_function_app.py QuadraticFunctionApplication  # 快速预览
    # manim -qh quadratic_function_app.py QuadraticFunctionApplication   # 高质量
    pass
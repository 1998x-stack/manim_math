"""
指数方程和对数方程 - Exponential and Logarithmic Equations
使用 Manim 创建的高一数学教学视频

内容: 指数方程和对数方程的概念、图像法求解、同底数法
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


class ExponentialLogarithmicEquations(Scene):
    """
    指数方程和对数方程教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 指数方程定义
    3. 图像法求解指数方程
    4. 同底数法
    5. 对数方程定义
    6. 图像法求解对数方程
    7. 验根提醒 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_EXPONENTIAL = "#e74c3c"    # 红色 - 指数函数
        self.COLOR_LOGARITHM = "#3498db"      # 蓝色 - 对数函数
        self.COLOR_SOLUTION = "#2ecc71"       # 绿色 - 解
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_WARNING = "#f39c12"        # 橙色 - 警告
        
        # 初始化几何/函数数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_exponential_definition()
        self.show_exponential_graph_solution()
        self.show_same_base_method()
        self.show_logarithm_definition()
        self.show_logarithm_graph_solution()
        self.show_verification_outro()
    
    def setup_geometry(self):
        """初始化坐标系和关键点"""
        # 坐标系位置
        self.axes_center = DOWN * 0.5
        
        # 指数方程 2^x = 8 的解
        self.solution_exp = 3  # x = 3
        self.solution_exp_point = np.array([3, 8, 0])
        
        # 对数方程 log_2(x) = 3 的解
        self.solution_log = 8  # x = 8
        self.solution_log_point = np.array([8, 3, 0])
        
        # 验证边界
        self.verify_boundaries()
    
    def verify_boundaries(self):
        """验证关键点是否在安全边界内"""
        # 安全边界
        SAFE_X = 4
        SAFE_Y_TOP = 7
        SAFE_Y_BOTTOM = -7
        
        # 这里主要验证坐标系不会超出边界
        # 指数图坐标系: x_length=6, y_length=7, 中心在 DOWN*0.5
        # 最大范围: x ∈ [-3, 3], y ∈ [-4, 3]
        exp_axes_bounds = {
            'x_min': -3,
            'x_max': 3,
            'y_min': -4,
            'y_max': 3
        }
        
        # 对数图坐标系: x_length=7, y_length=6, 中心在 DOWN*0.5
        # 最大范围: x ∈ [-3.5, 3.5], y ∈ [-3.5, 2.5]
        log_axes_bounds = {
            'x_min': -3.5,
            'x_max': 3.5,
            'y_min': -3.5,
            'y_max': 2.5
        }
        
        print("✓ 边界验证:")
        print(f"  指数图坐标系范围: x ∈ [{exp_axes_bounds['x_min']}, {exp_axes_bounds['x_max']}], "
              f"y ∈ [{exp_axes_bounds['y_min']}, {exp_axes_bounds['y_max']}]")
        print(f"  对数图坐标系范围: x ∈ [{log_axes_bounds['x_min']}, {log_axes_bounds['x_max']}], "
              f"y ∈ [{log_axes_bounds['y_min']}, {log_axes_bounds['y_max']}]")
        print(f"  安全边界: x ∈ [-{SAFE_X}, {SAFE_X}], y ∈ [{SAFE_Y_BOTTOM}, {SAFE_Y_TOP}]")
        
        # 检查是否超出
        if (abs(exp_axes_bounds['x_max']) > SAFE_X or 
            abs(exp_axes_bounds['x_min']) > SAFE_X or
            exp_axes_bounds['y_max'] > SAFE_Y_TOP or
            exp_axes_bounds['y_min'] < SAFE_Y_BOTTOM):
            print("⚠️ 警告: 指数图坐标系可能超出安全边界!")
        else:
            print("✓ 指数图坐标系在安全边界内")
        
        if (abs(log_axes_bounds['x_max']) > SAFE_X or 
            abs(log_axes_bounds['x_min']) > SAFE_X or
            log_axes_bounds['y_max'] > SAFE_Y_TOP or
            log_axes_bounds['y_min'] < SAFE_Y_BOTTOM):
            print("⚠️ 警告: 对数图坐标系可能超出安全边界!")
        else:
            print("✓ 对数图坐标系在安全边界内")
    
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
        hook_question = MathTex(
            r"2^x = 8",
            font_size=56,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        question_text = Text(
            "x = ?",
            font="Noto Sans CJK SC",
            font_size=64,
            color=WHITE
        ).next_to(hook_question, DOWN, buff=0.8)
        
        self.play(Write(hook_question), run_time=1.0)
        self.play(Write(question_text), run_time=0.5)
        
        # 问号闪烁
        question_mark = Text("?", font_size=80, color=YELLOW).move_to(question_text.get_center())
        self.play(
            Flash(question_mark, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        
        # 等待思考
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(question_text),
            run_time=0.5
        )
    
    def show_exponential_definition(self):
        """场景2: 指数方程定义"""
        # 标题
        title = Text(
            "指数方程",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_EXPONENTIAL
        ).move_to(UP * 5.5)
        
        # 定义
        definition = Text(
            "未知数在指数位置的方程",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.6)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.5)
        
        # 示例方程
        equation = MathTex(
            r"2^{x} = 8",
            font_size=48,
            tex_to_color_map={"x": YELLOW}
        ).move_to(UP * 3)
        
        self.play(Write(equation), run_time=1.0)
        
        # 指数高亮说明
        explanation = Text(
            "x 在指数位置",
            font="Noto Sans CJK SC",
            font_size=24,
            color=YELLOW
        ).next_to(equation, DOWN, buff=0.5)
        
        self.play(
            Indicate(equation, color=YELLOW, scale_factor=1.2),
            FadeIn(explanation),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理，保留方程移到顶部
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explanation),
            run_time=0.4
        )
        
        # 保存方程供后续使用
        self.exp_equation = equation.copy()
        self.play(
            equation.animate.scale(0.7).move_to(UP * 6.5),
            run_time=0.5
        )
    
    def show_exponential_graph_solution(self):
        """场景3: 图像法求解指数方程"""
        # 说明文字
        method_text = Text(
            "图像法求解",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(method_text), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(method_text), run_time=0.3)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 10, 2],
            x_length=6,
            y_length=7,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "numbers_to_exclude": [0]
            },
            tips=False
        ).move_to(self.axes_center)
        
        # 坐标轴标签
        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=UP, buff=0.2)
        
        self.play(Create(axes), run_time=1.0)
        self.play(Write(x_label), Write(y_label), run_time=0.4)
        
        # 绘制 y = 2^x
        exp_graph = axes.plot(
            lambda x: 2**x,
            x_range=[-1, 4.5],
            color=self.COLOR_EXPONENTIAL,
            stroke_width=3
        )
        
        exp_label = MathTex(
            r"y = 2^x",
            font_size=28,
            color=self.COLOR_EXPONENTIAL
        ).next_to(axes.c2p(4, 2**4), RIGHT, buff=0.2)
        
        self.play(Create(exp_graph), run_time=1.5)
        self.play(Write(exp_label), run_time=0.5)
        
        # 绘制 y = 8 水平线
        horizontal_line = DashedLine(
            axes.c2p(-1, 8),
            axes.c2p(5, 8),
            color=self.COLOR_LOGARITHM,
            dash_length=0.1
        )
        
        y8_label = MathTex(
            r"y = 8",
            font_size=28,
            color=self.COLOR_LOGARITHM
        ).next_to(axes.c2p(-0.5, 8), LEFT, buff=0.2)
        
        self.play(Create(horizontal_line), run_time=1.0)
        self.play(Write(y8_label), run_time=0.4)
        
        # 标记交点
        intersection_point = axes.c2p(3, 8)
        intersection_dot = Dot(
            intersection_point,
            color=self.COLOR_SOLUTION,
            radius=0.08
        )
        
        self.play(FadeIn(intersection_dot, scale=0.5), run_time=0.5)
        self.play(Flash(intersection_dot, color=self.COLOR_SOLUTION, flash_radius=0.3), run_time=0.5)
        
        # 垂线到 x 轴
        vertical_line = DashedLine(
            intersection_point,
            axes.c2p(3, 0),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(vertical_line), run_time=0.8)
        
        # 标注解 x = 3
        solution_label = MathTex(
            r"x = 3",
            font_size=32,
            color=self.COLOR_SOLUTION
        ).next_to(axes.c2p(3, 0), DOWN, buff=0.3)
        
        solution_box = SurroundingRectangle(
            solution_label,
            color=self.COLOR_SOLUTION,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Write(solution_label), run_time=0.6)
        self.play(Create(solution_box), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(horizontal_line),
            FadeOut(vertical_line),
            FadeOut(y8_label),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(exp_graph),
            FadeOut(exp_label),
            FadeOut(intersection_dot),
            FadeOut(solution_label),
            FadeOut(solution_box),
            run_time=0.6
        )
    
    def show_same_base_method(self):
        """场景4: 同底数法"""
        # 标题
        title = Text(
            "同底数法",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 原方程
        eq1 = MathTex(
            r"2^x = 8",
            font_size=40
        ).move_to(UP * 3.5)
        
        self.play(Write(eq1), run_time=0.8)
        
        # 提示：将 8 改写为 2 的幂
        hint = Text(
            "将 8 改写为 2 的幂",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(1.0)
        
        # 变换箭头
        arrow = Arrow(
            UP * 1.5,
            UP * 0.5,
            color=YELLOW,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 新方程: 2^x = 2^3
        eq2 = MathTex(
            r"2^x = 2^3",
            font_size=40
        ).move_to(ORIGIN)
        
        self.play(Write(eq2), run_time=1.0)
        
        # 框选底数
        base_box_left = SurroundingRectangle(
            eq2[0][0],  # 左边的 2
            color=self.COLOR_HIGHLIGHT,
            buff=0.08
        )
        
        base_box_right = SurroundingRectangle(
            eq2[0][3],  # 右边的 2
            color=self.COLOR_HIGHLIGHT,
            buff=0.08
        )
        
        same_base_text = Text(
            "底数相同",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(
            Create(base_box_left),
            Create(base_box_right),
            FadeIn(same_base_text),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 结论箭头
        conclusion_arrow = Arrow(
            DOWN * 1.8,
            DOWN * 2.8,
            color=YELLOW,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(GrowArrow(conclusion_arrow), run_time=0.5)
        
        # 结论
        conclusion = MathTex(
            r"x = 3",
            font_size=44,
            color=self.COLOR_SOLUTION
        ).move_to(DOWN * 3.5)
        
        conclusion_box = SurroundingRectangle(
            conclusion,
            color=self.COLOR_SOLUTION,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            Write(conclusion),
            Create(conclusion_box),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(eq1),
            FadeOut(hint),
            FadeOut(arrow),
            FadeOut(eq2),
            FadeOut(base_box_left),
            FadeOut(base_box_right),
            FadeOut(same_base_text),
            FadeOut(conclusion_arrow),
            FadeOut(conclusion),
            FadeOut(conclusion_box),
            run_time=0.6
        )
    
    def show_logarithm_definition(self):
        """场景5: 对数方程定义"""
        # 标题
        title = Text(
            "对数方程",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_LOGARITHM
        ).move_to(UP * 5.5)
        
        # 定义
        definition = Text(
            "未知数在真数或底数位置的方程",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.6)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.5)
        
        # 示例方程
        log_equation = MathTex(
            r"\log_2 x = 3",
            font_size=48,
            tex_to_color_map={"x": YELLOW}
        ).move_to(UP * 3)
        
        self.play(Write(log_equation), run_time=1.0)
        
        # 真数高亮说明
        explanation = Text(
            "x 在真数位置",
            font="Noto Sans CJK SC",
            font_size=24,
            color=YELLOW
        ).next_to(log_equation, DOWN, buff=0.5)
        
        self.play(
            Indicate(log_equation, color=YELLOW, scale_factor=1.2),
            FadeIn(explanation),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理，保留方程移到顶部
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explanation),
            run_time=0.4
        )
        
        self.play(
            log_equation.animate.scale(0.7).move_to(UP * 6.5),
            run_time=0.5
        )
        
        # 保存供后续使用
        self.log_equation = log_equation
    
    def show_logarithm_graph_solution(self):
        """场景6: 图像法求解对数方程"""
        # 说明文字
        method_text = Text(
            "图像法求解",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(method_text), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(method_text), run_time=0.3)
        
        # 创建坐标系
        axes = Axes(
            x_range=[-1, 10, 2],
            y_range=[-1, 5, 1],
            x_length=7,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "numbers_to_exclude": [0]
            },
            tips=False
        ).move_to(self.axes_center)
        
        # 坐标轴标签
        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=UP, buff=0.2)
        
        self.play(Create(axes), run_time=1.0)
        self.play(Write(x_label), Write(y_label), run_time=0.4)
        
        # 绘制 y = log_2(x)
        log_graph = axes.plot(
            lambda x: np.log2(x) if x > 0 else 0,
            x_range=[0.1, 10],
            color=self.COLOR_LOGARITHM,
            stroke_width=3
        )
        
        log_label = MathTex(
            r"y = \log_2 x",
            font_size=28,
            color=self.COLOR_LOGARITHM
        ).next_to(axes.c2p(9, np.log2(9)), UP, buff=0.2)
        
        self.play(Create(log_graph), run_time=1.5)
        self.play(Write(log_label), run_time=0.5)
        
        # 绘制 y = 3 水平线
        horizontal_line = DashedLine(
            axes.c2p(-1, 3),
            axes.c2p(10, 3),
            color=self.COLOR_EXPONENTIAL,
            dash_length=0.1
        )
        
        y3_label = MathTex(
            r"y = 3",
            font_size=28,
            color=self.COLOR_EXPONENTIAL
        ).next_to(axes.c2p(-0.5, 3), LEFT, buff=0.2)
        
        self.play(Create(horizontal_line), run_time=1.0)
        self.play(Write(y3_label), run_time=0.4)
        
        # 标记交点
        intersection_point = axes.c2p(8, 3)
        intersection_dot = Dot(
            intersection_point,
            color=self.COLOR_SOLUTION,
            radius=0.08
        )
        
        self.play(FadeIn(intersection_dot, scale=0.5), run_time=0.5)
        self.play(Flash(intersection_dot, color=self.COLOR_SOLUTION, flash_radius=0.3), run_time=0.5)
        
        # 垂线到 x 轴
        vertical_line = DashedLine(
            intersection_point,
            axes.c2p(8, 0),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(vertical_line), run_time=0.8)
        
        # 标注解 x = 8
        solution_label = MathTex(
            r"x = 8",
            font_size=32,
            color=self.COLOR_SOLUTION
        ).next_to(axes.c2p(8, 0), DOWN, buff=0.3)
        
        solution_box = SurroundingRectangle(
            solution_label,
            color=self.COLOR_SOLUTION,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Write(solution_label), run_time=0.6)
        self.play(Create(solution_box), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(horizontal_line),
            FadeOut(vertical_line),
            FadeOut(y3_label),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(log_graph),
            FadeOut(log_label),
            FadeOut(intersection_dot),
            FadeOut(solution_label),
            FadeOut(solution_box),
            FadeOut(self.log_equation),
            run_time=0.6
        )
    
    def show_verification_outro(self):
        """场景7: 验根提醒 + 片尾"""
        # 警告标题
        warning_title = Text(
            "重要提醒",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_WARNING
        ).move_to(UP * 4)
        
        self.play(
            FadeIn(warning_title, scale=1.2),
            Flash(warning_title, color=self.COLOR_WARNING, flash_radius=0.8),
            run_time=0.8
        )
        
        # 验根条件
        conditions = VGroup(
            Text("对数方程必须验根!", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("① 真数 > 0", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
            Text("② 底数 > 0 且 ≠ 1", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 1.5)
        
        for i, condition in enumerate(conditions):
            self.play(Write(condition), run_time=0.5 if i == 0 else 0.4)
            if i < len(conditions) - 1:
                self.wait(0.3)
        
        # 警告框
        warning_box = SurroundingRectangle(
            conditions,
            color=self.COLOR_WARNING,
            buff=0.4,
            corner_radius=0.15,
            stroke_width=3
        )
        
        self.play(Create(warning_box), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(warning_title),
            FadeOut(conditions),
            FadeOut(warning_box),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
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
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标 - 指数和对数符号
        icons = VGroup(
            MathTex(r"2^x", font_size=36, color=self.COLOR_EXPONENTIAL),
            MathTex(r"\log_2 x", font_size=36, color=self.COLOR_LOGARITHM),
        ).arrange(RIGHT, buff=1.5).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 渲染命令:
# manim -pql exponential_logarithmic.py ExponentialLogarithmicEquations  # 快速预览
# manim -qh exponential_logarithmic.py ExponentialLogarithmicEquations   # 高质量 1080p
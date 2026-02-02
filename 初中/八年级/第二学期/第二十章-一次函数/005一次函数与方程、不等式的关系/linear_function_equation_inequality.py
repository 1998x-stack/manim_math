"""
一次函数与方程、不等式的关系 - Linear Function with Equations and Inequalities
使用 Manim 创建的中学数学教学视频

内容: 一次函数y=kx+b与方程kx+b=0、不等式kx+b>0、kx+b<0的关系
目标观众: 八年级学生
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


class LinearFunctionEquationInequality(Scene):
    """
    一次函数与方程、不等式关系教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系和函数图像
    3. 方程kx+b=0的解
    4. 不等式kx+b>0的解集
    5. 不等式kx+b<0的解集
    6. 三者关系总结
    7. 实例演示
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_FUNCTION = "#3498db"      # 蓝色 - 函数图像
        self.COLOR_X_AXIS = WHITE            # x轴
        self.COLOR_ABOVE = "#2ecc71"         # 绿色 - x轴上方
        self.COLOR_BELOW = "#e74c3c"         # 红色 - x轴下方
        self.COLOR_INTERSECTION = YELLOW     # 黄色 - 交点
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.setup_coordinate_system()
        self.show_equation_solution()
        self.show_inequality_positive()
        self.show_inequality_negative()
        self.show_summary()
        self.show_example()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 函数定义: y = 2x - 3
        self.k = 2
        self.b = -3
        
        # x轴交点精确计算: 2x - 3 = 0 => x = 1.5
        self.x_intercept = -self.b / self.k  # = 1.5
        
        print(f"✓ 几何初始化: x轴交点 = {self.x_intercept}")
    
    def func(self, x):
        """一次函数 y = 2x - 3"""
        return self.k * x + self.b
    
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
            "函数、方程、不等式\n它们有什么关系?",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三个关键词
        keyword_1 = Text("函数", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_FUNCTION).move_to(UP * 1.5)
        keyword_2 = Text("方程", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_INTERSECTION).move_to(UP * 0.5)
        keyword_3 = Text("不等式", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_ABOVE).move_to(DOWN * 0.5)
        
        keywords = VGroup(keyword_1, keyword_2, keyword_3)
        
        for keyword in keywords:
            self.play(FadeIn(keyword, scale=1.2), run_time=0.3)
            self.play(Flash(keyword, color=self.COLOR_HIGHLIGHT), run_time=0.2)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(keywords),
            run_time=0.5
        )
    
    def setup_coordinate_system(self):
        """场景2: 建立坐标系和函数图像"""
        # 创建坐标系
        self.axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-5, 5, 1],
            x_length=7,
            y_length=8,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "numbers_to_exclude": [0],
            },
            tips=False
        ).move_to(UP * 2.0)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=28).next_to(self.axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28).next_to(self.axes.y_axis, UP, buff=0.2)
        
        # 动画
        self.play(Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 函数公式
        formula = MathTex(
            r"y = 2x - 3",
            font_size=36,
            color=self.COLOR_FUNCTION
        ).move_to(UP * 6.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 绘制函数图像
        self.graph = self.axes.plot(
            self.func,
            x_range=[-1, 4],
            color=self.COLOR_FUNCTION,
            stroke_width=4
        )
        
        self.play(Create(self.graph), run_time=1.5)
        self.wait(1.0)
        
        # 公式移到顶部缩小
        formula_small = MathTex(
            r"y = 2x - 3",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 7.2 + RIGHT * 2)
        
        self.play(Transform(formula, formula_small), run_time=0.4)
        
        self.formula = formula
        self.x_label = x_label
        self.y_label = y_label
    
    def show_equation_solution(self):
        """场景3: 方程kx+b=0的解"""
        # 方程显示
        equation = MathTex(
            r"2x - 3 = 0",
            font_size=36,
            color=self.COLOR_INTERSECTION
        ).move_to(UP * 6)
        
        equation_label = Text(
            "方程:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(equation, LEFT, buff=0.3)
        
        self.play(FadeIn(equation_label), Write(equation), run_time=0.8)
        
        # x轴高亮
        x_axis_highlight = self.axes.x_axis.copy().set_color(self.COLOR_INTERSECTION).set_stroke(width=6)
        self.play(ShowPassingFlash(x_axis_highlight, time_width=0.5), run_time=1.0)
        
        # 交点标记
        intersection_point = self.axes.c2p(self.x_intercept, 0)
        intersection_dot = Dot(intersection_point, color=self.COLOR_INTERSECTION, radius=0.15)
        
        self.play(GrowFromCenter(intersection_dot), run_time=0.6)
        self.play(Flash(intersection_dot, color=self.COLOR_INTERSECTION, flash_radius=0.4), run_time=0.4)
        
        # 坐标标注
        coord_label = MathTex(
            f"({self.x_intercept:.1f}, 0)",
            font_size=24,
            color=WHITE
        ).next_to(intersection_dot, DOWN, buff=0.3)
        
        self.play(FadeIn(coord_label, shift=UP * 0.2), run_time=0.5)
        
        # 垂直虚线
        vertical_line = DashedLine(
            intersection_point,
            intersection_point + DOWN * 0.5,
            color=self.COLOR_INTERSECTION,
            dash_length=0.08
        )
        
        self.play(Create(vertical_line), run_time=0.5)
        
        # 解的答案
        solution_text = MathTex(
            f"x = {self.x_intercept:.1f}",
            font_size=32,
            color=self.COLOR_INTERSECTION
        ).move_to(DOWN * 4)
        
        solution_label = Text(
            "解:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(solution_text, LEFT, buff=0.2)
        
        self.play(Write(solution_label), Write(solution_text), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "图像与x轴交点的横坐标",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(equation_label),
            FadeOut(equation),
            FadeOut(coord_label),
            FadeOut(vertical_line),
            FadeOut(solution_label),
            FadeOut(solution_text),
            FadeOut(explanation),
            intersection_dot.animate.scale(0.5).set_opacity(0.5),
            run_time=0.6
        )
        
        self.intersection_dot = intersection_dot
    
    def show_inequality_positive(self):
        """场景4: 不等式kx+b>0的解集"""
        # 不等式显示
        inequality = MathTex(
            r"2x - 3 > 0",
            font_size=36,
            color=self.COLOR_ABOVE
        ).move_to(UP * 6)
        
        inequality_label = Text(
            "不等式:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(inequality, LEFT, buff=0.3)
        
        self.play(FadeIn(inequality_label), Write(inequality), run_time=0.8)
        
        # 上方区域高亮
        # 使用Polygon精确定义
        x_int = self.x_intercept
        region_above = Polygon(
            self.axes.c2p(x_int, 0),
            self.axes.c2p(4, 0),
            self.axes.c2p(4, self.func(4)),
            self.axes.c2p(x_int, self.func(x_int)),
            fill_color=self.COLOR_ABOVE,
            fill_opacity=0.2,
            stroke_width=0
        )
        
        self.play(FadeIn(region_above), run_time=1.0)
        
        # 图像上方部分高亮
        graph_above = self.axes.plot(
            self.func,
            x_range=[x_int, 4],
            color=self.COLOR_ABOVE,
            stroke_width=7
        )
        
        self.play(Create(graph_above), run_time=1.2)
        
        # x>1.5标注
        solution_inequality = MathTex(
            f"x > {self.x_intercept:.1f}",
            font_size=32,
            color=self.COLOR_ABOVE
        ).move_to(DOWN * 4)
        
        solution_label = Text(
            "解集:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(solution_inequality, LEFT, buff=0.2)
        
        self.play(Write(solution_label), Write(solution_inequality), run_time=1.0)
        
        # 数轴箭头
        arrow_start = self.axes.c2p(x_int, 0) + DOWN * 0.6
        arrow_end = self.axes.c2p(3.5, 0) + DOWN * 0.6
        
        arrow_right = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_ABOVE,
            stroke_width=5,
            buff=0,
            max_tip_length_to_length_ratio=0.15
        )
        
        # 空心圆表示不包含边界
        boundary_circle = Circle(
            radius=0.08,
            color=self.COLOR_ABOVE,
            stroke_width=3,
            fill_opacity=0
        ).move_to(arrow_start)
        
        self.play(GrowArrow(arrow_right), FadeIn(boundary_circle), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "图像在x轴上方的部分",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        
        # 强调闪烁
        self.play(Indicate(region_above, scale_factor=1.05), run_time=1.0)
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(inequality_label),
            FadeOut(inequality),
            FadeOut(region_above),
            FadeOut(graph_above),
            FadeOut(solution_label),
            FadeOut(solution_inequality),
            FadeOut(arrow_right),
            FadeOut(boundary_circle),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_inequality_negative(self):
        """场景5: 不等式kx+b<0的解集"""
        # 不等式显示
        inequality = MathTex(
            r"2x - 3 < 0",
            font_size=36,
            color=self.COLOR_BELOW
        ).move_to(UP * 6)
        
        inequality_label = Text(
            "不等式:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(inequality, LEFT, buff=0.3)
        
        self.play(FadeIn(inequality_label), Write(inequality), run_time=0.8)
        
        # 下方区域高亮
        x_int = self.x_intercept
        region_below = Polygon(
            self.axes.c2p(-1, 0),
            self.axes.c2p(x_int, 0),
            self.axes.c2p(x_int, self.func(x_int)),
            self.axes.c2p(-1, self.func(-1)),
            fill_color=self.COLOR_BELOW,
            fill_opacity=0.2,
            stroke_width=0
        )
        
        self.play(FadeIn(region_below), run_time=1.0)
        
        # 图像下方部分高亮
        graph_below = self.axes.plot(
            self.func,
            x_range=[-1, x_int],
            color=self.COLOR_BELOW,
            stroke_width=7
        )
        
        self.play(Create(graph_below), run_time=1.2)
        
        # x<1.5标注
        solution_inequality = MathTex(
            f"x < {self.x_intercept:.1f}",
            font_size=32,
            color=self.COLOR_BELOW
        ).move_to(DOWN * 4)
        
        solution_label = Text(
            "解集:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(solution_inequality, LEFT, buff=0.2)
        
        self.play(Write(solution_label), Write(solution_inequality), run_time=1.0)
        
        # 数轴箭头
        arrow_end = self.axes.c2p(x_int, 0) + DOWN * 0.6
        arrow_start = self.axes.c2p(-1, 0) + DOWN * 0.6
        
        arrow_left = Arrow(
            arrow_end,
            arrow_start,
            color=self.COLOR_BELOW,
            stroke_width=5,
            buff=0,
            max_tip_length_to_length_ratio=0.15
        )
        
        # 空心圆表示不包含边界
        boundary_circle = Circle(
            radius=0.08,
            color=self.COLOR_BELOW,
            stroke_width=3,
            fill_opacity=0
        ).move_to(arrow_end)
        
        self.play(GrowArrow(arrow_left), FadeIn(boundary_circle), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "图像在x轴下方的部分",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.6)
        
        # 强调闪烁
        self.play(Indicate(region_below, scale_factor=1.05), run_time=1.0)
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(inequality_label),
            FadeOut(inequality),
            FadeOut(region_below),
            FadeOut(graph_below),
            FadeOut(solution_label),
            FadeOut(solution_inequality),
            FadeOut(arrow_left),
            FadeOut(boundary_circle),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 三者关系总结"""
        # 清理图像
        self.play(
            FadeOut(self.axes),
            FadeOut(self.graph),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.formula),
            FadeOut(self.intersection_dot),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "数形结合",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三栏对比表格
        # 第一行：标题
        col1_title = Text("方程", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_INTERSECTION)
        col2_title = Text("不等式 >0", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_ABOVE)
        col3_title = Text("不等式 <0", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_BELOW)
        
        titles = VGroup(col1_title, col2_title, col3_title).arrange(RIGHT, buff=0.8).move_to(UP * 4.5)
        
        self.play(FadeIn(titles, shift=UP * 0.2), run_time=0.8)
        
        # 第二行：代数形式
        col1_expr = MathTex(r"kx+b=0", font_size=26, color=WHITE).move_to(UP * 3 + LEFT * 2.5)
        col2_expr = MathTex(r"kx+b>0", font_size=26, color=WHITE).move_to(UP * 3)
        col3_expr = MathTex(r"kx+b<0", font_size=26, color=WHITE).move_to(UP * 3 + RIGHT * 2.5)
        
        exprs = VGroup(col1_expr, col2_expr, col3_expr)
        self.play(Write(exprs), run_time=1.0)
        
        # 第三行：几何意义
        col1_geo = Text(
            "交点横坐标",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 1.8 + LEFT * 2.5)
        
        col2_geo = Text(
            "图像在\nx轴上方",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
            line_spacing=0.8
        ).move_to(UP * 1.5)
        
        col3_geo = Text(
            "图像在\nx轴下方",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
            line_spacing=0.8
        ).move_to(UP * 1.5 + RIGHT * 2.5)
        
        geometries = VGroup(col1_geo, col2_geo, col3_geo)
        self.play(FadeIn(geometries, shift=UP * 0.2), run_time=1.0)
        
        # 示意图标
        # 交点图标
        icon1 = VGroup(
            Line(LEFT * 0.3, RIGHT * 0.3, color=self.COLOR_FUNCTION, stroke_width=3),
            Dot(ORIGIN, color=self.COLOR_INTERSECTION, radius=0.08)
        ).move_to(UP * 0.2 + LEFT * 2.5)
        
        # 上方图标
        icon2 = VGroup(
            Line(LEFT * 0.3, RIGHT * 0.3, color=GRAY_B, stroke_width=2),
            Line(LEFT * 0.2 + UP * 0.1, RIGHT * 0.2 + UP * 0.3, color=self.COLOR_ABOVE, stroke_width=3)
        ).move_to(UP * 0.2)
        
        # 下方图标
        icon3 = VGroup(
            Line(LEFT * 0.3, RIGHT * 0.3, color=GRAY_B, stroke_width=2),
            Line(LEFT * 0.2 + DOWN * 0.3, RIGHT * 0.2 + DOWN * 0.1, color=self.COLOR_BELOW, stroke_width=3)
        ).move_to(UP * 0.2 + RIGHT * 2.5)
        
        icons = VGroup(icon1, icon2, icon3)
        self.play(FadeIn(icons, scale=0.8), run_time=0.8)
        
        # 核心提示
        core_concept = Text(
            "用图像解方程和不等式！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(core_concept, scale=1.2), run_time=0.8)
        self.play(Indicate(core_concept, scale_factor=1.1), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(titles),
            FadeOut(exprs),
            FadeOut(geometries),
            FadeOut(icons),
            FadeOut(core_concept),
            run_time=0.6
        )
    
    def show_example(self):
        """场景7: 实例演示"""
        # 问题
        problem = Text(
            "求解不等式: 2x - 3 ≥ 0",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(problem), run_time=1.0)
        
        # 重新显示坐标系和图像
        self.play(
            FadeIn(self.axes),
            FadeIn(self.graph),
            FadeIn(self.x_label),
            FadeIn(self.y_label),
            run_time=0.8
        )
        
        # 交点闪烁
        intersection_point = self.axes.c2p(self.x_intercept, 0)
        intersection_dot = Dot(intersection_point, color=self.COLOR_INTERSECTION, radius=0.15)
        
        self.play(GrowFromCenter(intersection_dot), run_time=0.5)
        self.play(Flash(intersection_dot, color=self.COLOR_INTERSECTION, flash_radius=0.4), run_time=0.4)
        
        # 上方区域高亮（包含边界）
        x_int = self.x_intercept
        region_above = Polygon(
            self.axes.c2p(x_int, 0),
            self.axes.c2p(4, 0),
            self.axes.c2p(4, self.func(4)),
            self.axes.c2p(x_int, self.func(x_int)),
            fill_color=self.COLOR_ABOVE,
            fill_opacity=0.25,
            stroke_width=0
        )
        
        self.play(FadeIn(region_above), run_time=1.0)
        
        # 区间标注
        interval_notation = MathTex(
            f"x \\geq {self.x_intercept:.1f}",
            font_size=36,
            color=self.COLOR_ABOVE
        ).move_to(DOWN * 4.5)
        
        # 实心圆表示包含边界
        boundary_dot = Dot(
            self.axes.c2p(x_int, 0) + DOWN * 0.6,
            color=self.COLOR_ABOVE,
            radius=0.08
        )
        
        arrow_start = self.axes.c2p(x_int, 0) + DOWN * 0.6
        arrow_end = self.axes.c2p(3.5, 0) + DOWN * 0.6
        arrow_right = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_ABOVE,
            stroke_width=5,
            buff=0,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(
            Write(interval_notation),
            GrowArrow(arrow_right),
            FadeIn(boundary_dot),
            run_time=1.2
        )
        
        # 答案
        answer = Text(
            "答案:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(interval_notation, LEFT, buff=0.3)
        
        self.play(FadeIn(answer), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(problem),
            FadeOut(self.axes),
            FadeOut(self.graph),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(intersection_dot),
            FadeOut(region_above),
            FadeOut(interval_notation),
            FadeOut(answer),
            FadeOut(arrow_right),
            FadeOut(boundary_dot),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者名放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，用图像解方程和不等式!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标
        icons = VGroup(
            Circle(radius=0.3, color=self.COLOR_FUNCTION, fill_opacity=0.8).shift(LEFT * 1.8 + DOWN * 2.5),
            Circle(radius=0.3, color=self.COLOR_INTERSECTION, fill_opacity=0.8).shift(LEFT * 0.9 + DOWN * 2.5),
            Circle(radius=0.3, color=self.COLOR_ABOVE, fill_opacity=0.8).shift(DOWN * 2.5),
            Circle(radius=0.3, color=self.COLOR_BELOW, fill_opacity=0.8).shift(RIGHT * 0.9 + DOWN * 2.5),
            Circle(radius=0.3, color=YELLOW, fill_opacity=0.8).shift(RIGHT * 1.8 + DOWN * 2.5)
        )
        
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


# 运行命令:
# manim -pql linear_function_equation_inequality.py LinearFunctionEquationInequality  # 快速预览
# manim -qh linear_function_equation_inequality.py LinearFunctionEquationInequality   # 高质量
"""
一次函数的概念 - Linear Function Concept Animation
使用 Manim 创建的八年级数学教学视频

内容: 一次函数 y=kx+b 的概念，从正比例函数的推广，斜率和截距的几何意义
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


class LinearFunctionConcept(Scene):
    """
    一次函数概念教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引入问题
    2. 一次函数的引入 - 平移演示
    3. 截距的概念 - b 的几何意义
    4. 斜率的概念 - k 的几何意义
    5. 完整公式展示 - 综合理解
    6. 多个一次函数对比 - 变化规律
    7. 片尾总结 - 关键点回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 一次函数
        self.COLOR_SECONDARY = "#e74c3c"     # 红色 - 正比例函数
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_INTERCEPT = "#2ecc71"     # 绿色 - 截距
        self.COLOR_SLOPE = "#f39c12"         # 橙色 - 斜率
        
        # 字体大小
        self.FONT_SIZE_TITLE = 36
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 22
        self.FONT_SIZE_SMALL = 18
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduction()
        self.scene_3_intercept()
        self.scene_4_slope()
        self.scene_5_complete_formula()
        self.scene_6_comparison()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化坐标系和函数图像"""
        # 坐标系设置
        self.axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=5,
            axis_config={
                "include_numbers": False,
                "stroke_width": 2,
                "stroke_color": GRAY_A
            },
            tips=False
        ).move_to(DOWN * 0.5)
        
        # 添加坐标轴标签
        x_label = Text("x", font_size=self.FONT_SIZE_SMALL, color=GRAY_A).next_to(
            self.axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = Text("y", font_size=self.FONT_SIZE_SMALL, color=GRAY_A).next_to(
            self.axes.y_axis.get_end(), UP, buff=0.2
        )
        self.axes_labels = VGroup(x_label, y_label)
        
        # 函数定义
        self.proportional_func = lambda x: 2 * x  # y = 2x
        self.linear_func = lambda x: 2 * x + 1    # y = 2x + 1
        
        # 关键点坐标
        self.origin = self.axes.c2p(0, 0)
        self.intercept_point = self.axes.c2p(0, 1)
        self.point1_coords = self.axes.c2p(0, 1)
        self.point2_coords = self.axes.c2p(1, 3)
        
        # 斜率三角形顶点
        self.slope_triangle_p1 = self.axes.c2p(0, 1)
        self.slope_triangle_p2 = self.axes.c2p(1, 1)
        self.slope_triangle_p3 = self.axes.c2p(1, 3)
    
    def scene_1_opening(self):
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
            "正比例函数的图像\n一定过原点吗?",
            font="PingFang SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.2)
        self.wait(0.3)
        
        # 坐标系创建
        self.play(
            Create(self.axes),
            Write(self.axes_labels),
            run_time=0.8
        )
        
        # 原点标记
        origin_dot = Dot(self.origin, radius=0.08, color=self.COLOR_SECONDARY)
        origin_label = Text("O", font="PingFang SC", font_size=self.FONT_SIZE_SMALL).next_to(
            origin_dot, DL, buff=0.1
        )
        
        self.play(
            FadeIn(origin_dot, scale=0.5),
            FadeIn(origin_label),
            run_time=0.4
        )
        
        # 正比例函数 y=2x 图像
        self.proportional_graph = self.axes.plot(
            self.proportional_func,
            x_range=[-1.5, 1.5],
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        # 正比例函数标签
        proportional_label = MathTex(
            r"y = 2x",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(self.axes.c2p(1.2, 2.4), RIGHT, buff=0.2)
        
        self.play(Create(self.proportional_graph), run_time=1.0)
        self.play(FadeIn(proportional_label), run_time=0.4)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(proportional_label),
            run_time=0.5
        )
    
    def scene_2_introduction(self):
        """场景2: 一次函数的引入"""
        # 标题
        title = Text(
            "一次函数",
            font="PingFang SC",
            font_size=self.FONT_SIZE_TITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        # 公式
        formula = MathTex(
            r"y = kx + b \quad (k \neq 0)",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=WHITE
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(0.4)
        
        # 复制正比例函数图像
        proportional_copy = self.proportional_graph.copy()
        
        # 说明文字
        explanation = Text(
            "正比例函数向上平移",
            font="PingFang SC",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 平移动画 - 向上移动1个单位
        shift_distance = self.axes.c2p(0, 1) - self.axes.c2p(0, 0)
        
        self.play(
            proportional_copy.animate.shift(shift_distance),
            run_time=1.2
        )
        
        # 变色为蓝色
        self.play(
            proportional_copy.animate.set_color(self.COLOR_PRIMARY),
            run_time=0.4
        )
        
        # 一次函数标签
        linear_label = MathTex(
            r"y = 2x + 1",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_PRIMARY
        ).next_to(self.axes.c2p(1.2, 3.4), RIGHT, buff=0.2)
        
        self.play(FadeIn(linear_label), run_time=0.5)
        
        # 平移箭头
        shift_arrow = Arrow(
            self.axes.c2p(0, 0),
            self.axes.c2p(0, 1),
            buff=0,
            stroke_width=3,
            color=self.COLOR_HIGHLIGHT,
            max_tip_length_to_length_ratio=0.15
        )
        
        shift_label = Text(
            "+1",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(shift_arrow, RIGHT, buff=0.1)
        
        self.play(
            GrowArrow(shift_arrow),
            FadeIn(shift_label),
            run_time=0.6
        )
        self.wait(1.2)
        
        # 保存一次函数图像
        self.linear_graph = proportional_copy
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(shift_arrow),
            FadeOut(shift_label),
            FadeOut(linear_label),
            FadeOut(formula),
            run_time=0.5
        )
        
        # 保存标题以便后续使用
        self.title = title
    
    def scene_3_intercept(self):
        """场景3: 截距的概念"""
        # 小标题
        subtitle = Text(
            "截距 b - 与y轴交点的纵坐标",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_INTERCEPT
        ).move_to(UP * 4.8)
        
        self.play(
            self.title.animate.move_to(UP * 5.8).scale(0.8),
            FadeIn(subtitle),
            run_time=0.6
        )
        
        # 淡化正比例函数
        self.play(
            self.proportional_graph.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # 截距点
        intercept_dot = Dot(
            self.intercept_point,
            radius=0.1,
            color=self.COLOR_INTERCEPT
        )
        
        self.play(
            Flash(intercept_dot, color=self.COLOR_INTERCEPT, flash_radius=0.3),
            FadeIn(intercept_dot, scale=0.5),
            run_time=0.6
        )
        
        # 虚线到y轴
        dashed_line = DashedLine(
            self.intercept_point,
            self.axes.c2p(-0.3, 1),
            dash_length=0.08,
            color=self.COLOR_INTERCEPT,
            stroke_width=2
        )
        
        self.play(Create(dashed_line), run_time=0.6)
        
        # 截距标注
        intercept_label = MathTex(
            r"b = 1",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_INTERCEPT
        ).next_to(intercept_dot, RIGHT, buff=0.3)
        
        self.play(FadeIn(intercept_label), run_time=0.5)
        self.wait(0.4)
        
        # 说明文字
        explanation = Text(
            "当 x=0 时, y=b",
            font="PingFang SC",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 公式中的 b 高亮
        formula_highlight = MathTex(
            r"y = kx + {{ b }}",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=WHITE
        ).move_to(DOWN * 5.5)
        formula_highlight.set_color_by_tex("b", self.COLOR_INTERCEPT)
        
        self.play(FadeIn(formula_highlight), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dashed_line),
            FadeOut(explanation),
            FadeOut(formula_highlight),
            FadeOut(intercept_label),
            run_time=0.5
        )
        
        # 保留截距点
        self.intercept_dot = intercept_dot
    
    def scene_4_slope(self):
        """场景4: 斜率的概念"""
        # 小标题
        subtitle = Text(
            "斜率 k - 直线的倾斜程度",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SLOPE
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.6)
        
        # 在图像上取两点
        point1 = Dot(self.point1_coords, radius=0.08, color=self.COLOR_SLOPE)
        point2 = Dot(self.point2_coords, radius=0.08, color=self.COLOR_SLOPE)
        
        point1_label = MathTex(
            r"(0, 1)",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_SLOPE
        ).next_to(point1, LEFT, buff=0.15)
        
        point2_label = MathTex(
            r"(1, 3)",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_SLOPE
        ).next_to(point2, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(point1, scale=0.5),
            FadeIn(point2, scale=0.5),
            run_time=0.6
        )
        self.play(
            FadeIn(point1_label),
            FadeIn(point2_label),
            run_time=0.4
        )
        
        # 绘制斜率三角形
        slope_triangle = Polygon(
            self.slope_triangle_p1,
            self.slope_triangle_p2,
            self.slope_triangle_p3,
            stroke_color=self.COLOR_SLOPE,
            stroke_width=3,
            fill_color=self.COLOR_SLOPE,
            fill_opacity=0.2
        )
        
        self.play(Create(slope_triangle), run_time=0.8)
        
        # Δx 标注
        delta_x_brace = Brace(
            Line(self.slope_triangle_p1, self.slope_triangle_p2),
            direction=DOWN,
            buff=0.1,
            color=self.COLOR_SLOPE
        )
        delta_x_label = MathTex(
            r"\Delta x = 1",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_SLOPE
        ).next_to(delta_x_brace, DOWN, buff=0.05)
        
        self.play(
            FadeIn(delta_x_brace),
            FadeIn(delta_x_label),
            run_time=0.5
        )
        
        # Δy 标注
        delta_y_brace = Brace(
            Line(self.slope_triangle_p2, self.slope_triangle_p3),
            direction=RIGHT,
            buff=0.1,
            color=self.COLOR_SLOPE
        )
        delta_y_label = MathTex(
            r"\Delta y = 2",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_SLOPE
        ).next_to(delta_y_brace, RIGHT, buff=0.05)
        
        self.play(
            FadeIn(delta_y_brace),
            FadeIn(delta_y_label),
            run_time=0.5
        )
        
        # 斜率公式
        slope_formula = MathTex(
            r"k = \frac{\Delta y}{\Delta x} = \frac{2}{1} = 2",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_SLOPE
        ).move_to(DOWN * 5)
        
        self.play(Write(slope_formula), run_time=1.2)
        self.wait(0.8)
        
        # 说明文字
        explanation = Text(
            "k > 0, 从左到右上升",
            font="PingFang SC",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(slope_triangle),
            FadeOut(delta_x_brace),
            FadeOut(delta_x_label),
            FadeOut(delta_y_brace),
            FadeOut(delta_y_label),
            FadeOut(slope_formula),
            FadeOut(explanation),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point1_label),
            FadeOut(point2_label),
            run_time=0.6
        )
    
    def scene_5_complete_formula(self):
        """场景5: 完整公式展示"""
        # 完整公式
        formula_complete = MathTex(
            r"y = {{ k }}x + {{ b }}",
            font_size=48,
            color=WHITE
        ).move_to(UP * 5.2)
        formula_complete.set_color_by_tex("k", self.COLOR_SLOPE)
        formula_complete.set_color_by_tex("b", self.COLOR_INTERCEPT)
        
        self.play(
            FadeOut(self.title),
            Write(formula_complete),
            run_time=1.0
        )
        
        # k 的说明
        k_box = VGroup(
            SurroundingRectangle(
                formula_complete[1][0],
                color=self.COLOR_SLOPE,
                buff=0.15,
                corner_radius=0.1
            ),
            Text(
                "斜率 (k ≠ 0)",
                font="PingFang SC",
                font_size=self.FONT_SIZE_SMALL,
                color=self.COLOR_SLOPE
            )
        )
        k_box[1].next_to(k_box[0], DOWN, buff=0.3)
        
        self.play(FadeIn(k_box), run_time=0.6)
        
        # b 的说明
        b_box = VGroup(
            SurroundingRectangle(
                formula_complete[3][0],
                color=self.COLOR_INTERCEPT,
                buff=0.15,
                corner_radius=0.1
            ),
            Text(
                "截距",
                font="PingFang SC",
                font_size=self.FONT_SIZE_SMALL,
                color=self.COLOR_INTERCEPT
            )
        )
        b_box[1].next_to(b_box[0], DOWN, buff=0.3)
        
        self.play(FadeIn(b_box), run_time=0.6)
        self.wait(0.8)
        
        # 特殊情况
        special_case = VGroup(
            Text(
                "特殊情况:",
                font="PingFang SC",
                font_size=self.FONT_SIZE_BODY,
                color=GRAY_A
            ),
            MathTex(
                r"b = 0",
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_INTERCEPT
            ),
            MathTex(
                r"y = kx",
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_SECONDARY
            ),
            Text(
                "(正比例函数)",
                font="PingFang SC",
                font_size=self.FONT_SIZE_SMALL,
                color=GRAY_A
            )
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 5.5)
        
        # 修复中文混合问题
        special_case_fixed = VGroup(
            Text(
                "特殊情况: 当 b=0 时",
                font="PingFang SC",
                font_size=self.FONT_SIZE_BODY,
                color=GRAY_A
            ),
            MathTex(
                r"y = kx",
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_SECONDARY
            ),
            Text(
                "(正比例函数)",
                font="PingFang SC",
                font_size=self.FONT_SIZE_SMALL,
                color=GRAY_A
            )
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 5.5)
        
        self.play(FadeIn(special_case_fixed), run_time=0.8)
        
        # 正比例函数图像闪烁
        self.play(
            Flash(self.proportional_graph, color=self.COLOR_SECONDARY, flash_radius=0.5),
            self.proportional_graph.animate.set_opacity(0.8),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(k_box),
            FadeOut(b_box),
            FadeOut(special_case_fixed),
            run_time=0.5
        )
        
        # 保存公式以便后续使用
        self.formula_complete = formula_complete
    
    def scene_6_comparison(self):
        """场景6: 多个一次函数对比"""
        # 清除之前的图像
        self.play(
            FadeOut(self.proportional_graph),
            FadeOut(self.linear_graph),
            FadeOut(self.intercept_dot),
            run_time=0.5
        )
        
        # 创建多个一次函数
        graph1 = self.axes.plot(
            lambda x: x + 1,
            x_range=[-3, 2],
            color="#2ecc71",
            stroke_width=3
        )
        label1 = MathTex(
            r"y = x + 1",
            font_size=self.FONT_SIZE_SMALL,
            color="#2ecc71"
        )
        
        graph2 = self.axes.plot(
            lambda x: -x + 2,
            x_range=[-1, 3],
            color="#e74c3c",
            stroke_width=3
        )
        label2 = MathTex(
            r"y = -x + 2",
            font_size=self.FONT_SIZE_SMALL,
            color="#e74c3c"
        )
        
        graph3 = self.axes.plot(
            lambda x: 0.5 * x - 1,
            x_range=[-2, 3],
            color="#9b59b6",
            stroke_width=3
        )
        label3 = MathTex(
            r"y = 0.5x - 1",
            font_size=self.FONT_SIZE_SMALL,
            color="#9b59b6"
        )
        
        graph4 = self.axes.plot(
            lambda x: -2 * x,
            x_range=[-1, 1.5],
            color="#f39c12",
            stroke_width=3
        )
        label4 = MathTex(
            r"y = -2x",
            font_size=self.FONT_SIZE_SMALL,
            color="#f39c12"
        )
        
        # 绘制图像
        self.play(Create(graph1), run_time=0.7)
        self.play(Create(graph2), run_time=0.7)
        self.play(Create(graph3), run_time=0.7)
        self.play(Create(graph4), run_time=0.7)
        
        # 公式组
        formulas_group = VGroup(label1, label2, label3, label4).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        ).move_to(RIGHT * 2.5 + DOWN * 4.5).scale(0.9)
        
        self.play(FadeIn(formulas_group), run_time=0.5)
        self.wait(0.5)
        
        # 观察文字
        observation = Text(
            "k 决定倾斜\nb 决定位置",
            font="PingFang SC",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(LEFT * 2.5 + DOWN * 5)
        
        self.play(FadeIn(observation), run_time=0.6)
        self.wait(1.0)
        
        # 高亮 k>0 的线
        self.play(
            graph1.animate.set_stroke(width=5),
            graph3.animate.set_stroke(width=5),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 恢复并高亮 k<0 的线
        self.play(
            graph1.animate.set_stroke(width=3),
            graph3.animate.set_stroke(width=3),
            graph2.animate.set_stroke(width=5),
            graph4.animate.set_stroke(width=5),
            run_time=0.5
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(graph1),
            FadeOut(graph2),
            FadeOut(graph3),
            FadeOut(graph4),
            FadeOut(formulas_group),
            FadeOut(observation),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 片尾总结"""
        # 坐标系淡出
        self.play(
            FadeOut(self.axes),
            FadeOut(self.axes_labels),
            FadeOut(self.formula_complete),
            run_time=0.5
        )
        
        # 总结标题
        summary_title = Text(
            "一次函数",
            font="PingFang SC",
            font_size=44,
            color=GOLD
        ).move_to(UP * 3)
        
        self.play(Write(summary_title), run_time=1.0)
        
        # 关键点
        key1 = VGroup(
            Text("•", font_size=self.FONT_SIZE_BODY, color=WHITE),
            Text(
                "形式:",
                font="PingFang SC",
                font_size=self.FONT_SIZE_BODY,
                color=GRAY_A
            ),
            MathTex(
                r"y = kx + b",
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            ),
            MathTex(
                r"(k \neq 0)",
                font_size=self.FONT_SIZE_SMALL,
                color=GRAY_A
            )
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.5)
        
        key2 = VGroup(
            Text("•", font_size=self.FONT_SIZE_BODY, color=WHITE),
            Text(
                "k: 斜率 (倾斜程度)",
                font="PingFang SC",
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_SLOPE
            )
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)
        
        key3 = VGroup(
            Text("•", font_size=self.FONT_SIZE_BODY, color=WHITE),
            Text(
                "b: 截距 (与y轴交点)",
                font="PingFang SC",
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_INTERCEPT
            )
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)
        
        special = VGroup(
            Text("•", font_size=self.FONT_SIZE_BODY, color=WHITE),
            Text(
                "b=0 时为正比例函数",
                font="PingFang SC",
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_SECONDARY
            )
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.5)
        
        self.play(FadeIn(key1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(key2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(key3), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(special), run_time=0.6)
        self.wait(1.0)
        
        # 淡出总结内容
        self.play(
            FadeOut(summary_title),
            FadeOut(key1),
            FadeOut(key2),
            FadeOut(key3),
            FadeOut(special),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
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
            "关注我, 学更多函数知识!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 简单的函数曲线图标
        curve1 = self.axes.plot(
            lambda x: np.sin(x),
            x_range=[-PI, PI],
            color=self.COLOR_PRIMARY,
            stroke_width=2
        ).scale(0.3).move_to(follow_text.get_center() + LEFT * 3.5)
        
        curve2 = curve1.copy().move_to(follow_text.get_center() + RIGHT * 3.5)
        
        decorations = VGroup(curve1, curve2)
        
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
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql linear_function_concept.py LinearFunctionConcept  # 快速预览
# manim -qh linear_function_concept.py LinearFunctionConcept   # 高质量 (1080p)
# manim -qk linear_function_concept.py LinearFunctionConcept   # 4K质量
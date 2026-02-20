"""
统计图表教学动画 - Statistical Charts Educational Animation
使用 Manim 创建的初中统计学教学视频

内容: 条形图、折线图、扇形图、频数分布直方图
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


class StatisticalCharts(Scene):
    """
    统计图表教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 条形图 (Bar Chart)
    3. 折线图 (Line Chart)
    4. 扇形图 (Pie Chart)
    5. 频数分布直方图 (Histogram)
    6. 对比总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_BAR_CHART = "#3498db"       # 蓝色 - 条形图
        self.COLOR_LINE_CHART = "#2ecc71"      # 绿色 - 折线图
        self.COLOR_PIE_CHART = "#e74c3c"       # 红色 - 扇形图
        self.COLOR_HISTOGRAM = "#f39c12"       # 橙色 - 直方图
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化数据
        self.setup_data()
        
        # 执行动画序列
        self.show_opening()
        self.show_bar_chart()
        self.show_line_chart()
        self.show_pie_chart()
        self.show_histogram()
        self.show_comparison()
        self.show_outro()
    
    def setup_data(self):
        """初始化所有图表数据"""
        # 条形图数据 - 每日销量
        self.bar_labels = ["周一", "周二", "周三", "周四", "周五"]
        self.bar_values = [4, 7, 5, 8, 6]
        self.bar_max = 10
        
        # 折线图数据 - 每日温度
        self.line_labels = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        self.line_values = [20, 25, 22, 28, 26, 30, 35]
        
        # 扇形图数据 - 爱好分布
        self.pie_labels = ["运动", "阅读", "游戏", "音乐", "其他"]
        self.pie_percentages = [30, 25, 20, 15, 10]
        self.pie_colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6"]
        
        # 直方图数据 - 成绩分布
        self.hist_ranges = ["0-59", "60-69", "70-79", "80-89", "90-99", "100"]
        self.hist_frequencies = [5, 8, 12, 10, 6, 3]
        
        # 验证数据
        self.verify_data()
    
    def verify_data(self):
        """验证数据的合理性"""
        # 验证扇形图百分比总和
        pie_sum = sum(self.pie_percentages)
        if pie_sum != 100:
            print(f"WARNING: 扇形图百分比总和 = {pie_sum}% ≠ 100%")
        
        # 验证数据长度匹配
        if len(self.bar_labels) != len(self.bar_values):
            print(f"WARNING: 条形图标签和数据长度不匹配")
        
        if len(self.line_labels) != len(self.line_values):
            print(f"WARNING: 折线图标签和数据长度不匹配")
        
        if len(self.pie_labels) != len(self.pie_percentages):
            print(f"WARNING: 扇形图标签和数据长度不匹配")
        
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
        hook = Text(
            "数据如何可视化?",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 四种图表图标
        icon_size = 0.6
        
        # 条形图图标
        bar_icon = VGroup(
            Rectangle(height=0.3, width=0.15, fill_opacity=1, color=self.COLOR_BAR_CHART, stroke_width=0).shift(LEFT * 0.2 + DOWN * 0.1),
            Rectangle(height=0.5, width=0.15, fill_opacity=1, color=self.COLOR_BAR_CHART, stroke_width=0).shift(DOWN * 0.025),
            Rectangle(height=0.4, width=0.15, fill_opacity=1, color=self.COLOR_BAR_CHART, stroke_width=0).shift(RIGHT * 0.2 + DOWN * 0.05),
        ).scale(icon_size)
        
        # 折线图图标
        line_icon = VGroup(
            Line([-0.3, -0.2, 0], [-0.1, 0.1, 0], color=self.COLOR_LINE_CHART, stroke_width=4),
            Line([-0.1, 0.1, 0], [0.1, -0.05, 0], color=self.COLOR_LINE_CHART, stroke_width=4),
            Line([0.1, -0.05, 0], [0.3, 0.2, 0], color=self.COLOR_LINE_CHART, stroke_width=4),
            Dot([-0.3, -0.2, 0], radius=0.04, color=self.COLOR_LINE_CHART),
            Dot([-0.1, 0.1, 0], radius=0.04, color=self.COLOR_LINE_CHART),
            Dot([0.1, -0.05, 0], radius=0.04, color=self.COLOR_LINE_CHART),
            Dot([0.3, 0.2, 0], radius=0.04, color=self.COLOR_LINE_CHART),
        ).scale(icon_size)
        
        # 扇形图图标
        pie_icon = VGroup(
            Sector(arc_center=ORIGIN, radius=0.4, angle=120*DEGREES, start_angle=0, color="#3498db", fill_opacity=1, stroke_width=1),
            Sector(arc_center=ORIGIN, radius=0.4, angle=100*DEGREES, start_angle=120*DEGREES, color="#2ecc71", fill_opacity=1, stroke_width=1),
            Sector(arc_center=ORIGIN, radius=0.4, angle=80*DEGREES, start_angle=220*DEGREES, color="#e74c3c", fill_opacity=1, stroke_width=1),
            Sector(arc_center=ORIGIN, radius=0.4, angle=60*DEGREES, start_angle=300*DEGREES, color="#f39c12", fill_opacity=1, stroke_width=1),
        ).scale(icon_size)
        
        # 直方图图标
        hist_icon = VGroup(
            Rectangle(height=0.2, width=0.18, fill_opacity=1, color=self.COLOR_HISTOGRAM, stroke_width=0).shift(LEFT * 0.27 + DOWN * 0.15),
            Rectangle(height=0.35, width=0.18, fill_opacity=1, color=self.COLOR_HISTOGRAM, stroke_width=0).shift(LEFT * 0.09 + DOWN * 0.075),
            Rectangle(height=0.5, width=0.18, fill_opacity=1, color=self.COLOR_HISTOGRAM, stroke_width=0).shift(RIGHT * 0.09 + DOWN * 0.0),
            Rectangle(height=0.3, width=0.18, fill_opacity=1, color=self.COLOR_HISTOGRAM, stroke_width=0).shift(RIGHT * 0.27 + DOWN * 0.1),
        ).scale(icon_size)
        
        # 图标组合
        icons = VGroup(bar_icon, line_icon, pie_icon, hist_icon).arrange(RIGHT, buff=0.8).move_to(UP * 3)
        
        self.play(FadeIn(icons, lag_ratio=0.2), run_time=1.0)
        
        # 图标名称
        icon_names = VGroup(
            Text("条形图", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("折线图", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("扇形图", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("直方图", font="Noto Sans CJK SC", font_size=20, color=WHITE),
        )
        
        for i, name in enumerate(icon_names):
            name.next_to(icons[i], DOWN, buff=0.3)
        
        self.play(FadeIn(icon_names, lag_ratio=0.2), run_time=0.8)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(icons),
            FadeOut(icon_names),
            run_time=0.5
        )
    
    def show_bar_chart(self):
        """场景2: 条形图"""
        # 标题
        title = Text(
            "条形图 Bar Chart",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_BAR_CHART
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False
        ).move_to(UP * 2)
        
        # Y轴标签
        y_labels = VGroup(*[
            Text(str(i), font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
            .next_to(axes.c2p(0, i), LEFT, buff=0.2)
            for i in range(0, 11, 2)
        ])
        
        # X轴标签
        x_labels = VGroup(*[
            Text(label, font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
            .next_to(axes.c2p(i + 1, 0), DOWN, buff=0.3)
            for i, label in enumerate(self.bar_labels)
        ])
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(x_labels), FadeIn(y_labels), run_time=0.5)
        
        # 创建条形
        bars = VGroup()
        for i, value in enumerate(self.bar_values):
            bar = Rectangle(
                height=axes.c2p(0, value)[1] - axes.c2p(0, 0)[1],
                width=0.5,
                fill_opacity=0.8,
                fill_color=self.COLOR_BAR_CHART,
                stroke_width=2,
                stroke_color=WHITE
            )
            bar.move_to(axes.c2p(i + 1, value / 2))
            bars.add(bar)
        
        # 条形依次生长
        self.play(
            *[GrowFromEdge(bar, DOWN) for bar in bars],
            lag_ratio=0.3,
            run_time=1.5
        )
        
        # 数值标签
        value_labels = VGroup(*[
            Text(str(value), font="Noto Sans CJK SC", font_size=20, color=WHITE)
            .next_to(bar, UP, buff=0.1)
            for value, bar in zip(self.bar_values, bars)
        ])
        
        self.play(FadeIn(value_labels, lag_ratio=0.2), run_time=0.6)
        
        # 高亮最高条形
        max_index = self.bar_values.index(max(self.bar_values))
        self.play(
            bars[max_index].animate.set_fill(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        # 说明文字
        explanation = Text(
            "直观比较各类数据的大小",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        use_case = Text(
            "适用: 不同类别的数据比较",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2.8)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(FadeIn(use_case), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(bars),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(value_labels),
            FadeOut(explanation),
            FadeOut(use_case),
            run_time=0.6
        )
    
    def show_line_chart(self):
        """场景3: 折线图"""
        # 标题
        title = Text(
            "折线图 Line Chart",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_LINE_CHART
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[15, 40, 5],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False
        ).move_to(UP * 2)
        
        # Y轴标签
        y_labels = VGroup(*[
            Text(f"{i}°C", font="Noto Sans CJK SC", font_size=16, color=GRAY_A)
            .next_to(axes.c2p(0, i), LEFT, buff=0.2)
            for i in range(15, 41, 5)
        ])
        
        # X轴标签
        x_labels = VGroup(*[
            Text(label, font="Noto Sans CJK SC", font_size=16, color=GRAY_A)
            .next_to(axes.c2p(i + 1, 15), DOWN, buff=0.3)
            for i, label in enumerate(self.line_labels)
        ])
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(x_labels), FadeIn(y_labels), run_time=0.5)
        
        # 创建数据点
        points = [axes.c2p(i + 1, value) for i, value in enumerate(self.line_values)]
        dots = VGroup(*[
            Dot(point, radius=0.08, color=self.COLOR_LINE_CHART)
            for point in points
        ])
        
        self.play(FadeIn(dots, lag_ratio=0.2), run_time=1.0)
        
        # 绘制折线
        line = VMobject(color=self.COLOR_LINE_CHART, stroke_width=3)
        line.set_points_as_corners(points)
        
        self.play(Create(line), run_time=1.5)
        
        # 数值标签
        value_labels = VGroup(*[
            Text(f"{value}°", font="Noto Sans CJK SC", font_size=16, color=WHITE)
            .next_to(dot, UP, buff=0.15)
            for value, dot in zip(self.line_values, dots)
        ])
        
        self.play(FadeIn(value_labels, lag_ratio=0.15), run_time=0.8)
        
        # 上升趋势箭头
        trend_arrow = Arrow(
            start=axes.c2p(1.5, 22),
            end=axes.c2p(6.5, 34),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            buff=0
        )
        
        trend_label = Text(
            "上升趋势",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(trend_arrow, RIGHT, buff=0.2)
        
        self.play(GrowArrow(trend_arrow), run_time=0.5)
        self.play(FadeIn(trend_label), run_time=0.3)
        
        # 说明文字
        explanation = Text(
            "反映数据变化趋势",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        use_case = Text(
            "适用: 时间序列数据分析",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2.8)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(FadeIn(use_case), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(line),
            FadeOut(dots),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(value_labels),
            FadeOut(trend_arrow),
            FadeOut(trend_label),
            FadeOut(explanation),
            FadeOut(use_case),
            run_time=0.6
        )
    
    def show_pie_chart(self):
        """场景4: 扇形图"""
        # 标题
        title = Text(
            "扇形图 Pie Chart",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PIE_CHART
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建扇形
        radius = 1.8
        sectors = VGroup()
        labels = VGroup()
        
        # 计算累积角度
        cumulative_angle = 0
        
        for i, (label_text, percentage, color) in enumerate(
            zip(self.pie_labels, self.pie_percentages, self.pie_colors)
        ):
            # 计算角度（从顶部开始，顺时针）
            angle = percentage / 100 * 360 * DEGREES
            start_angle = 90 * DEGREES - cumulative_angle
            
            # 创建扇形
            sector = Sector(
                arc_center=UP * 2,
                radius=radius,
                angle=angle,
                start_angle=start_angle,
                color=color,
                fill_opacity=0.8,
                stroke_width=2,
                stroke_color=WHITE
            )
            sectors.add(sector)
            
            # 计算标签位置（扇形中心）
            mid_angle = start_angle - angle / 2
            label_distance = radius * 0.65
            label_pos = UP * 2 + np.array([
                label_distance * np.cos(mid_angle),
                label_distance * np.sin(mid_angle),
                0
            ])
            
            # 创建百分比标签
            percent_label = Text(
                f"{percentage}%",
                font="Noto Sans CJK SC",
                font_size=18,
                color=WHITE,
                weight=BOLD
            ).move_to(label_pos)
            
            labels.add(percent_label)
            
            cumulative_angle += angle
        
        # 扇形依次出现
        self.play(
            *[FadeIn(sector, scale=0.5) for sector in sectors],
            lag_ratio=0.3,
            run_time=2.0
        )
        
        # 百分比标签
        self.play(FadeIn(labels, lag_ratio=0.2), run_time=1.0)
        
        # 图例
        legend = VGroup()
        for i, (label_text, color) in enumerate(zip(self.pie_labels, self.pie_colors)):
            legend_item = VGroup(
                Square(side_length=0.25, fill_opacity=1, color=color, stroke_width=1, stroke_color=WHITE),
                Text(label_text, font="Noto Sans CJK SC", font_size=18, color=WHITE)
            ).arrange(RIGHT, buff=0.15)
            legend.add(legend_item)
        
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 0.8)
        
        self.play(FadeIn(legend, shift=UP * 0.3, lag_ratio=0.2), run_time=1.0)
        
        # 高亮最大扇形
        max_index = self.pie_percentages.index(max(self.pie_percentages))
        self.play(
            sectors[max_index].animate.scale(1.1),
            run_time=0.5
        )
        self.play(
            sectors[max_index].animate.scale(1 / 1.1),
            run_time=0.3
        )
        
        # 公式
        formula = MathTex(
            r"\text{Pie Center Angle} = \frac{\text{Category Data}}{\text{Total Data}} \times 360^\circ",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        # 示例计算
        example = MathTex(
            r"\text{Sports: } \frac{30}{100} \times 360^\circ = 108^\circ",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.3)
        
        self.play(Write(formula), run_time=1.0)
        self.play(Write(example), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "表示各部分在总体中的比例",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        use_case = Text(
            "适用: 整体构成分析",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 6.2)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(FadeIn(use_case), run_time=0.4)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sectors),
            FadeOut(labels),
            FadeOut(legend),
            FadeOut(formula),
            FadeOut(example),
            FadeOut(explanation),
            FadeOut(use_case),
            run_time=0.6
        )
    
    def show_histogram(self):
        """场景5: 频数分布直方图"""
        # 标题
        title = Text(
            "频数分布直方图 Histogram",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HISTOGRAM
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 15, 3],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY_B, "stroke_width": 2},
            tips=False
        ).move_to(UP * 2)
        
        # Y轴标签
        y_labels = VGroup(*[
            Text(str(i), font="Noto Sans CJK SC", font_size=18, color=GRAY_A)
            .next_to(axes.c2p(0, i), LEFT, buff=0.2)
            for i in range(0, 16, 3)
        ])
        
        # X轴标签
        x_labels = VGroup(*[
            Text(label, font="Noto Sans CJK SC", font_size=14, color=GRAY_A)
            .next_to(axes.c2p(i + 0.5, 0), DOWN, buff=0.3)
            for i, label in enumerate(self.hist_ranges)
        ])
        
        self.play(Create(axes), run_time=1.0)
        self.play(FadeIn(x_labels), FadeIn(y_labels), run_time=0.5)
        
        # 创建直方图矩形（连续无间隙）
        rectangles = VGroup()
        for i, freq in enumerate(self.hist_frequencies):
            rect_height = axes.c2p(0, freq)[1] - axes.c2p(0, 0)[1]
            rect_width = axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]
            
            rect = Rectangle(
                height=rect_height,
                width=rect_width,
                fill_opacity=0.8,
                fill_color=self.COLOR_HISTOGRAM,
                stroke_width=2,
                stroke_color=WHITE
            )
            
            # 定位矩形（注意：矩形之间无间隙）
            rect_x = axes.c2p(i + 0.5, freq / 2)[0]
            rect_y = axes.c2p(0, freq / 2)[1]
            rect.move_to([rect_x, rect_y, 0])
            
            rectangles.add(rect)
        
        # 矩形依次生长
        self.play(
            *[GrowFromEdge(rect, DOWN) for rect in rectangles],
            lag_ratio=0.2,
            run_time=1.5
        )
        
        # 频数标签
        freq_labels = VGroup(*[
            Text(str(freq), font="Noto Sans CJK SC", font_size=18, color=WHITE)
            .move_to(axes.c2p(i + 0.5, freq + 0.8))
            for i, freq in enumerate(self.hist_frequencies)
        ])
        
        self.play(FadeIn(freq_labels, lag_ratio=0.15), run_time=0.8)
        
        # 高亮众数区间（频数最高）
        mode_index = self.hist_frequencies.index(max(self.hist_frequencies))
        self.play(
            rectangles[mode_index].animate.set_fill(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        mode_label = Text(
            "众数区间",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(rectangles[mode_index], UP, buff=0.5)
        
        mode_arrow = Arrow(
            start=mode_label.get_bottom(),
            end=rectangles[mode_index].get_top(),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
            buff=0.1
        )
        
        self.play(Write(mode_label), GrowArrow(mode_arrow), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "表示数据的分布情况",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        use_case = Text(
            "适用: 连续型数据的频数分布",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2.8)
        
        note = Text(
            "特点: 矩形连续无间隙",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(FadeIn(use_case), run_time=0.4)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes),
            FadeOut(rectangles),
            FadeOut(x_labels),
            FadeOut(y_labels),
            FadeOut(freq_labels),
            FadeOut(mode_label),
            FadeOut(mode_arrow),
            FadeOut(explanation),
            FadeOut(use_case),
            FadeOut(note),
            run_time=0.6
        )
    
    def show_comparison(self):
        """场景6: 对比总结"""
        # 标题
        title = Text(
            "选择合适的统计图表",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建四个小型图表卡片
        card_scale = 0.4
        
        # 卡片1: 条形图
        bar_card = self.create_chart_card(
            "条形图",
            "比较大小",
            self.COLOR_BAR_CHART,
            "shopping_cart"
        ).scale(card_scale).shift(LEFT * 2 + UP * 3)
        
        # 卡片2: 折线图
        line_card = self.create_chart_card(
            "折线图",
            "变化趋势",
            self.COLOR_LINE_CHART,
            "trending_up"
        ).scale(card_scale).shift(RIGHT * 2 + UP * 3)
        
        # 卡片3: 扇形图
        pie_card = self.create_chart_card(
            "扇形图",
            "比例构成",
            self.COLOR_PIE_CHART,
            "pie_chart"
        ).scale(card_scale).shift(LEFT * 2 + UP * 0.5)
        
        # 卡片4: 直方图
        hist_card = self.create_chart_card(
            "直方图",
            "分布情况",
            self.COLOR_HISTOGRAM,
            "bar_chart"
        ).scale(card_scale).shift(RIGHT * 2 + UP * 0.5)
        
        cards = VGroup(bar_card, line_card, pie_card, hist_card)
        
        self.play(FadeIn(cards, lag_ratio=0.3, shift=UP * 0.5), run_time=1.5)
        
        # 应用场景示例
        examples = VGroup(
            Text("销量对比 → 条形图", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("温度变化 → 折线图", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("爱好分布 → 扇形图", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("成绩分布 → 直方图", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(Write(examples, lag_ratio=0.3), run_time=1.0)
        
        # 关键提示
        key_point = Text(
            "根据数据特点选择图表类型",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.2), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(examples),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def create_chart_card(self, title_text, subtitle_text, color, icon_type):
        """创建图表卡片"""
        # 背景卡片
        card_bg = RoundedRectangle(
            width=4,
            height=3,
            corner_radius=0.2,
            fill_opacity=0.15,
            fill_color=color,
            stroke_width=3,
            stroke_color=color
        )
        
        # 图标（简化版）
        if icon_type == "shopping_cart":
            icon = VGroup(
                Rectangle(height=1, width=0.3, fill_opacity=1, color=color, stroke_width=0),
                Rectangle(height=1.5, width=0.3, fill_opacity=1, color=color, stroke_width=0).shift(RIGHT * 0.5),
                Rectangle(height=1.2, width=0.3, fill_opacity=1, color=color, stroke_width=0).shift(RIGHT * 1.0),
            ).move_to(UP * 0.3)
        elif icon_type == "trending_up":
            icon = VMobject(color=color, stroke_width=6)
            icon.set_points_as_corners([
                [-0.8, -0.3, 0],
                [-0.3, 0.3, 0],
                [0.3, -0.1, 0],
                [0.8, 0.5, 0]
            ]).move_to(UP * 0.3)
        elif icon_type == "pie_chart":
            icon = VGroup(
                Sector(radius=0.8, angle=150*DEGREES, start_angle=0, color=color, fill_opacity=1, stroke_width=2),
                Sector(radius=0.8, angle=120*DEGREES, start_angle=150*DEGREES, color=color, fill_opacity=0.6, stroke_width=2),
                Sector(radius=0.8, angle=90*DEGREES, start_angle=270*DEGREES, color=color, fill_opacity=0.3, stroke_width=2),
            ).move_to(UP * 0.3)
        else:  # bar_chart
            icon = VGroup(
                Rectangle(height=0.5, width=0.4, fill_opacity=1, color=color, stroke_width=0).shift(LEFT * 0.6 + DOWN * 0.15),
                Rectangle(height=1.0, width=0.4, fill_opacity=1, color=color, stroke_width=0).shift(LEFT * 0.0 + UP * 0.1),
                Rectangle(height=1.3, width=0.4, fill_opacity=1, color=color, stroke_width=0).shift(RIGHT * 0.6 + UP * 0.25),
            ).move_to(UP * 0.3)
        
        # 标题
        title = Text(
            title_text,
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 0.6)
        
        # 副标题
        subtitle = Text(
            subtitle_text,
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1.1)
        
        return VGroup(card_bg, icon, title, subtitle)
    
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
        
        # 四种图表图标装饰（旋转动画）
        icon_size = 0.5
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_BAR_CHART, fill_opacity=0.5, stroke_width=3),
            Circle(radius=icon_size, color=self.COLOR_LINE_CHART, fill_opacity=0.5, stroke_width=3),
            Circle(radius=icon_size, color=self.COLOR_PIE_CHART, fill_opacity=0.5, stroke_width=3),
            Circle(radius=icon_size, color=self.COLOR_HISTOGRAM, fill_opacity=0.5, stroke_width=3),
        )
        
        # 排列成圆形
        icons.arrange_in_grid(rows=2, cols=2, buff=1.5).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
        
        self.play(Rotate(icons, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql statistical_charts.py StatisticalCharts  # 快速预览
# manim -qh statistical_charts.py StatisticalCharts   # 高质量渲染
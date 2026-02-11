"""
对数函数教学动画 - Logarithm Function Animation
使用 Manim 创建的高中数学教学视频

内容: 对数函数的定义、图像和性质
目标观众: 高一学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
1. 开场引入
2. 定义展示
3. 坐标系建立
4. a>1 情况 - 单调递增
5. 0<a<1 情况 - 单调递减
6. 关键性质总结
7. 片尾关注
"""

from manim import *
import numpy as np


# ===== 全局配置 - TikTok竖屏尺寸 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class LogarithmFunction(Scene):
    """对数函数教学动画主场景"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_AXES = WHITE
        self.COLOR_GRAPH_INCREASE = "#3498db"  # 蓝色 - a>1
        self.COLOR_GRAPH_DECREASE = "#e74c3c"  # 红色 - 0<a<1
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_POINT = "#2ecc71"  # 绿色
        self.COLOR_ASYMPTOTE = "#f39c12"  # 橙色
        self.COLOR_GRID = GRAY_B
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_axes()
        self.show_case_a_greater_than_1()
        self.show_case_a_less_than_1()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场引入 (0-5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "指数的逆运算是什么?",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        
        # 神秘符号 log 闪现
        log_symbol = MathTex(
            r"\log",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(
            FadeIn(log_symbol, scale=0.5),
            Flash(log_symbol, color=self.COLOR_HIGHLIGHT, flash_radius=1.0),
            run_time=0.6
        )
        self.wait(0.4)
        
        # 揭秘文字
        question = Text(
            "今天揭秘：对数函数!",
            font=self.FONT_CHINESE,
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(log_symbol),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 定义展示 (5-12秒)"""
        # 标题
        title = Text(
            "对数函数",
            font=self.FONT_CHINESE,
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=0.8)
        
        # 主公式
        main_formula = MathTex(
            r"y = \log_a x",
            font_size=50
        ).move_to(UP * 3.5)
        
        self.play(Write(main_formula), run_time=1.0)
        
        # 条件说明
        conditions = MathTex(
            r"a > 0 \text{ and } a \neq 1",
            font_size=36
        ).next_to(main_formula, DOWN, buff=0.5)
        
        self.play(FadeIn(conditions), run_time=0.6)
        self.wait(0.5)
        
        # 定义域和值域
        domain = Text(
            "定义域: (0, +∞)",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        range_text = Text(
            "值域: R",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_A
        ).next_to(domain, DOWN, buff=0.3)
        
        self.play(
            FadeIn(domain, shift=UP * 0.2),
            FadeIn(range_text, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 公式移动到顶部
        formula_group = VGroup(main_formula, conditions)
        
        self.play(
            FadeOut(title),
            FadeOut(domain),
            FadeOut(range_text),
            formula_group.animate.scale(0.6).move_to(UP * 6.5),
            run_time=0.8
        )
        
        # 保存公式以便后续引用
        self.main_formula = formula_group
    
    def show_axes(self):
        """场景3: 坐标系建立 (12-18秒)"""
        # 创建坐标轴
        self.axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=10,
            axis_config={
                "color": self.COLOR_AXES,
                "include_numbers": True,
                "font_size": 24,
            },
            tips=False
        ).move_to(UP * 1.0)
        
        # 坐标轴标签
        x_label = self.axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.3)
        y_label = self.axes.get_y_axis_label("y", edge=UP, direction=UP, buff=0.3)
        
        self.play(Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 添加网格
        grid = NumberPlane(
            x_range=[0, 6, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=10,
            background_line_style={
                "stroke_color": self.COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).move_to(self.axes.get_center())
        
        self.play(FadeIn(grid, shift=ORIGIN), run_time=0.6)
        self.add(grid, self.axes)  # 确保坐标轴在网格上方
        
        # 标注定点 (1, 0)
        fixed_point = self.axes.c2p(1, 0)
        self.fixed_point_dot = Dot(
            fixed_point,
            color=self.COLOR_POINT,
            radius=0.08
        )
        
        fixed_point_label = Text(
            "恒过点 (1, 0)",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_POINT
        ).next_to(self.fixed_point_dot, UR, buff=0.2)
        
        self.play(
            FadeIn(self.fixed_point_dot, scale=0.5),
            Flash(self.fixed_point_dot, color=self.COLOR_POINT, flash_radius=0.3),
            run_time=0.5
        )
        self.play(Write(fixed_point_label), run_time=0.6)
        self.wait(0.8)
        
        # 暂时移除标签，后续会再次高亮
        self.play(FadeOut(fixed_point_label), run_time=0.3)
        
        # 保存网格以便管理
        self.grid = grid
        self.x_label = x_label
        self.y_label = y_label
    
    def show_case_a_greater_than_1(self):
        """场景4: a>1 情况 - 单调递增 (18-30秒)"""
        # 说明文字
        case_title = Text(
            "当 a > 1 时",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_GRAPH_INCREASE
        ).move_to(DOWN * 5)
        
        example = VGroup(
            Text(
                "例如:",
                font=self.FONT_CHINESE,
                font_size=28,
                color=GRAY_A
            ),
            MathTex(
                r"y = \log_2 x",
                font_size=28,
                color=GRAY_A
            )
        ).arrange(RIGHT, buff=0.2).next_to(case_title, DOWN, buff=0.3)
        
        self.play(Write(case_title), run_time=0.5)
        self.play(FadeIn(example), run_time=0.5)
        self.wait(0.5)
        
        # 绘制垂直渐近线 x = 0
        asymptote_line = DashedLine(
            self.axes.c2p(0, -3),
            self.axes.c2p(0, 3),
            color=self.COLOR_ASYMPTOTE,
            dash_length=0.1,
            stroke_width=3
        )
        
        asymptote_label = Text(
            "x = 0 是垂直渐近线",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_ASYMPTOTE
        ).move_to(self.axes.c2p(0.5, 2.5))
        
        self.play(Create(asymptote_line), run_time=0.8)
        self.play(FadeIn(asymptote_label, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 绘制函数图像 y = log_2(x)
        graph_increase = self.axes.plot(
            lambda x: np.log2(x),
            x_range=[0.1, 6],
            color=self.COLOR_GRAPH_INCREASE,
            stroke_width=4
        )
        
        self.play(Create(graph_increase), run_time=2.0)
        self.wait(0.5)
        
        # 高亮定点
        self.play(
            Flash(self.fixed_point_dot, color=self.COLOR_POINT, flash_radius=0.4),
            Indicate(self.fixed_point_dot, scale_factor=1.5),
            run_time=0.6
        )
        self.wait(0.3)
        
        # 标注关键点
        sample_points = [
            (2, 1, "(2, 1)"),
            (4, 2, "(4, 2)")
        ]
        
        sample_dots = VGroup()
        sample_labels = VGroup()
        
        for x, y, label_text in sample_points:
            pos = self.axes.c2p(x, y)
            dot = Dot(pos, color=self.COLOR_POINT, radius=0.06)
            label = MathTex(label_text, font_size=20, color=WHITE).next_to(dot, UR, buff=0.1)
            sample_dots.add(dot)
            sample_labels.add(label)
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in sample_dots],
            run_time=0.6
        )
        self.play(
            *[Write(label) for label in sample_labels],
            run_time=0.5
        )
        self.wait(0.5)
        
        # 箭头指示单调递增
        arrow_start = self.axes.c2p(1.5, -0.5)
        arrow_end = self.axes.c2p(5, 2)
        
        arrow_up = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=5,
            buff=0
        )
        
        monotone_text = Text(
            "单调递增",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_up, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow_up), run_time=0.6)
        self.play(Write(monotone_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(case_title),
            FadeOut(example),
            FadeOut(sample_dots),
            FadeOut(sample_labels),
            FadeOut(arrow_up),
            FadeOut(monotone_text),
            FadeOut(asymptote_label),
            run_time=0.6
        )
        
        # 图像变淡但保留
        self.play(
            graph_increase.animate.set_stroke(opacity=0.4),
            run_time=0.4
        )
        
        # 保存元素
        self.graph_increase = graph_increase
        self.asymptote_line = asymptote_line
    
    def show_case_a_less_than_1(self):
        """场景5: 0<a<1 情况 - 单调递减 (30-42秒)"""
        # 说明文字
        case_title = Text(
            "当 0 < a < 1 时",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_GRAPH_DECREASE
        ).move_to(DOWN * 5)
        
        example = VGroup(
            Text(
                "例如:",
                font=self.FONT_CHINESE,
                font_size=28,
                color=GRAY_A
            ),
            MathTex(
                r"y = \log_{0.5} x",
                font_size=28,
                color=GRAY_A
            )
        ).arrange(RIGHT, buff=0.2).next_to(case_title, DOWN, buff=0.3)
        
        self.play(Write(case_title), run_time=0.5)
        self.play(FadeIn(example), run_time=0.5)
        self.wait(0.5)
        
        # 绘制函数图像 y = log_0.5(x) = log(x) / log(0.5)
        graph_decrease = self.axes.plot(
            lambda x: np.log(x) / np.log(0.5),
            x_range=[0.1, 6],
            color=self.COLOR_GRAPH_DECREASE,
            stroke_width=4
        )
        
        self.play(Create(graph_decrease), run_time=2.0)
        
        # 之前的图像恢复清晰度
        self.play(
            self.graph_increase.animate.set_stroke(opacity=1.0),
            run_time=0.4
        )
        self.wait(0.5)
        
        # 高亮定点 - 两条曲线都过这点
        self.play(
            Flash(self.fixed_point_dot, color=self.COLOR_POINT, flash_radius=0.5),
            Indicate(self.fixed_point_dot, scale_factor=1.8),
            run_time=0.7
        )
        self.wait(0.3)
        
        # 标注关键点
        sample_points_2 = [
            (2, -1, "(2, -1)"),
            (4, -2, "(4, -2)")
        ]
        
        sample_dots_2 = VGroup()
        sample_labels_2 = VGroup()
        
        for x, y, label_text in sample_points_2:
            pos = self.axes.c2p(x, y)
            dot = Dot(pos, color=self.COLOR_POINT, radius=0.06)
            label = MathTex(label_text, font_size=20, color=WHITE).next_to(dot, DR, buff=0.1)
            sample_dots_2.add(dot)
            sample_labels_2.add(label)
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in sample_dots_2],
            run_time=0.6
        )
        self.play(
            *[Write(label) for label in sample_labels_2],
            run_time=0.5
        )
        self.wait(0.5)
        
        # 箭头指示单调递减
        arrow_start_2 = self.axes.c2p(1.5, 0.5)
        arrow_end_2 = self.axes.c2p(5, -2)
        
        arrow_down = Arrow(
            arrow_start_2,
            arrow_end_2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=5,
            buff=0
        )
        
        monotone_text_2 = Text(
            "单调递减",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_down, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow_down), run_time=0.6)
        self.play(Write(monotone_text_2), run_time=0.5)
        self.wait(0.8)
        
        # 对比说明
        comparison = Text(
            "a 不同, 单调性相反!",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(comparison, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(case_title),
            FadeOut(example),
            FadeOut(sample_dots_2),
            FadeOut(sample_labels_2),
            FadeOut(arrow_down),
            FadeOut(monotone_text_2),
            FadeOut(comparison),
            run_time=0.6
        )
        
        # 保存图像
        self.graph_decrease = graph_decrease
    
    def show_summary(self):
        """场景6: 关键性质总结 (42-52秒)"""
        # 标题
        summary_title = Text(
            "对数函数关键性质",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(summary_title), run_time=0.8)
        self.wait(0.5)
        
        # 性质列表
        properties = [
            ("定义域: (0, +∞)", self.graph_increase),
            ("值域: R", None),
            ("恒过点 (1, 0)", self.fixed_point_dot),
            ("x = 0 是垂直渐近线", self.asymptote_line),
            ("单调性取决于底数 a", None)
        ]
        
        y_pos = -5.5
        
        for i, (prop_text, highlight_obj) in enumerate(properties):
            prop = Text(
                f"• {prop_text}",
                font=self.FONT_CHINESE,
                font_size=22,
                color=WHITE
            ).move_to(DOWN * y_pos)
            
            # 淡入性质文字
            self.play(FadeIn(prop, shift=UP * 0.2), run_time=0.5)
            
            # 如果有对应的图形元素，闪烁高亮
            if highlight_obj is not None:
                self.play(
                    Indicate(highlight_obj, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
                    run_time=0.4
                )
            
            y_pos += 0.4
            
            if i < len(properties) - 1:
                self.wait(0.3)
        
        self.wait(1.5)
        
        # 清理（保留图像用于片尾）
        self.play(
            FadeOut(summary_title),
            *[FadeOut(child) for child in self.mobjects if isinstance(child, Text) and "•" in child.text],
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾关注 (52-60秒)"""
        # 图像缩小移到角落
        graphs_group = VGroup(
            self.axes,
            self.grid,
            self.x_label,
            self.y_label,
            self.graph_increase,
            self.graph_decrease,
            self.asymptote_line,
            self.fixed_point_dot
        )
        
        self.play(
            graphs_group.animate.scale(0.4).to_corner(UR, buff=0.5),
            run_time=1.0
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
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
            font=self.FONT_CHINESE,
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 公式回顾
        formula_recap = MathTex(
            r"y = \log_a x",
            font_size=48,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(formula_recap), run_time=0.8)
        
        # 装饰性动画 - 小圆点
        dots = VGroup(*[
            Dot(
                follow_text.get_center() + 1.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]),
                color=self.COLOR_HIGHLIGHT,
                radius=0.08
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in dots],
            run_time=0.6
        )
        self.play(Rotate(dots, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# ===== 运行命令 =====
# manim -pql logarithm_function.py LogarithmFunction  # 快速预览
# manim -qh logarithm_function.py LogarithmFunction   # 高质量 1080p
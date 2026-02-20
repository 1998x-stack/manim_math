"""
圆的方程动画 - Circle Equation Animation
使用 Manim 创建的高中几何教学视频

内容: 圆的标准方程、一般方程、直线与圆的位置关系
目标观众: 高二学生
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


class CircleEquation(Scene):
    """
    圆的方程教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 圆的定义
    3. 标准方程
    4. 一般方程
    5. 直线与圆（相离）
    6. 直线与圆（相切）
    7. 直线与圆（相交）+ 总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 圆
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 圆心
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮色
        self.COLOR_AUXILIARY = GRAY_B        # 辅助线
        self.COLOR_LINE = "#2ecc71"         # 绿色 - 直线
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_standard_equation()
        self.show_general_equation()
        self.show_line_separate()
        self.show_line_tangent()
        self.show_line_intersect()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化圆和所有几何元素"""
        # 坐标系配置
        self.axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=5,
            axis_config={
                "include_numbers": False,
                "stroke_color": GRAY_B,
                "stroke_width": 2
            }
        ).move_to(UP * 1.5)
        
        # 添加坐标轴标签
        self.x_label = MathTex("x", font_size=24, color=GRAY_A).next_to(
            self.axes.x_axis.get_end(), RIGHT, buff=0.1
        )
        self.y_label = MathTex("y", font_size=24, color=GRAY_A).next_to(
            self.axes.y_axis.get_end(), UP, buff=0.1
        )
        
        # 圆的参数
        self.center = self.axes.c2p(2, 1)  # 圆心在坐标系中的 (2, 1)
        self.radius = 1.5  # 坐标系单位
        self.radius_pixels = self.axes.x_axis.unit_size * self.radius
        
        # 一般方程参数 (基于 (x-2)² + (y-1)² = 2.25)
        # 展开: x² - 4x + 4 + y² - 2y + 1 = 2.25
        # x² + y² - 4x - 2y + 2.75 = 0
        self.D = -4
        self.E = -2
        self.F = 2.75
        
        # 验证一般方程参数
        self.verify_general_equation()
        
        # 直线与圆位置关系
        # 相离直线: y = 0.5x + 4 (通过调整确保相离)
        self.line_separate_func = lambda x: 0.5 * x + 4
        
        # 相切直线: 需要精确计算
        # 圆心 (2, 1), 半径 1.5
        # 水平切线: y = 1 + 1.5 = 2.5 或 y = 1 - 1.5 = -0.5
        self.line_tangent_y = 2.5
        
        # 相交直线: y = 0.5x - 0.5 (经过圆内部)
        self.line_intersect_func = lambda x: 0.5 * x - 0.5
        
        print("✓ 几何数据初始化完成")
    
    def verify_general_equation(self):
        """验证一般方程参数的正确性"""
        epsilon = 1e-6
        
        # 从一般方程计算圆心和半径
        center_x_calc = -self.D / 2
        center_y_calc = -self.E / 2
        
        # 圆心应该是 (2, 1)
        assert abs(center_x_calc - 2) < epsilon, f"圆心x坐标错误: {center_x_calc}"
        assert abs(center_y_calc - 1) < epsilon, f"圆心y坐标错误: {center_y_calc}"
        
        # 计算半径
        discriminant = self.D**2 + self.E**2 - 4*self.F
        assert discriminant > 0, f"判别式错误: {discriminant}"
        
        radius_calc = 0.5 * np.sqrt(discriminant)
        assert abs(radius_calc - self.radius) < epsilon, f"半径错误: {radius_calc}"
        
        print("✓ 一般方程参数验证通过")
    
    def calculate_distance_point_to_line(self, point, line_func):
        """
        计算点到直线的距离
        直线形式: y = mx + c (即 mx - y + c = 0)
        """
        # 提取点坐标 (在坐标系中的逻辑坐标)
        point_coords = self.axes.p2c(point)
        x0, y0 = point_coords[0], point_coords[1]
        
        # 从函数中提取 m 和 c
        # y = mx + c  =>  mx - y + c = 0
        # 测试两个点来确定斜率和截距
        x1, x2 = 0, 1
        y1, y2 = line_func(x1), line_func(x2)
        m = y2 - y1
        c = y1
        
        # 距离公式: |mx0 - y0 + c| / sqrt(m² + 1)
        distance = abs(m * x0 - y0 + c) / np.sqrt(m**2 + 1)
        
        # 转换为像素距离
        return distance * self.axes.x_axis.unit_size
    
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
            "如何用方程描述一个圆？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=1.0)
        
        # 创建坐标系
        axes_group = VGroup(self.axes, self.x_label, self.y_label)
        self.play(Create(axes_group), run_time=1.0)
        
        # 创建圆 - 使用动态生成效果
        circle = Circle(
            radius=self.radius_pixels,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.center)
        
        self.play(Create(circle), run_time=1.5)
        self.wait(0.5)
        
        # 清理钩子
        self.play(FadeOut(hook), run_time=0.4)
        
        # 保存圆对象
        self.circle = circle
    
    def show_definition(self):
        """场景2: 圆的定义"""
        # 标题
        title = Text(
            "圆的定义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 圆心标记
        center_dot = Dot(
            self.center,
            color=self.COLOR_SECONDARY,
            radius=0.08
        )
        center_label = Text(
            "O",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_SECONDARY
        ).next_to(center_dot, DOWN + RIGHT, buff=0.1)
        
        self.play(
            FadeIn(center_dot, scale=0.5),
            Flash(center_dot, color=self.COLOR_SECONDARY, flash_radius=0.3),
            run_time=0.6
        )
        self.play(FadeIn(center_label), run_time=0.3)
        
        # 绘制多条半径
        angles = [0, PI/3, 2*PI/3, PI, 4*PI/3, 5*PI/3]
        radius_lines = VGroup()
        
        for angle in angles:
            end_point = self.center + self.radius_pixels * np.array([np.cos(angle), np.sin(angle), 0])
            radius_line = Line(
                self.center,
                end_point,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
            radius_lines.add(radius_line)
        
        self.play(
            *[Create(line) for line in radius_lines],
            run_time=1.5,
            lag_ratio=0.2
        )
        
        # 半径标注
        r_line = radius_lines[0]
        r_label = MathTex("r", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(
            r_line.get_center(), UP + RIGHT, buff=0.05
        )
        self.play(FadeIn(r_label), run_time=0.4)
        
        # 定义文字
        definition = Text(
            "到定点距离等于定长的点的轨迹",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(radius_lines),
            FadeOut(r_label),
            run_time=0.5
        )
        
        # 保留圆心
        self.center_dot = center_dot
        self.center_label = center_label
    
    def show_standard_equation(self):
        """场景3: 标准方程"""
        # 标题
        title = Text(
            "标准方程",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 标准方程公式
        formula = MathTex(
            r"(x - a)^2 + (y - b)^2 = r^2",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=1.2)
        
        # 圆心坐标标注
        center_coords = self.axes.p2c(self.center)
        center_coord_label = MathTex(
            r"(a, b) = (2, 1)",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(self.center_label, DOWN, buff=0.3)
        
        self.play(FadeIn(center_coord_label), run_time=0.7)
        
        # 半径标注
        radius_label_text = MathTex(
            r"r = 1.5",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula, DOWN, buff=0.4)
        
        self.play(FadeIn(radius_label_text), run_time=0.5)
        self.wait(0.5)
        
        # 具体例子
        example = MathTex(
            r"(x - 2)^2 + (y - 1)^2 = 2.25",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(example), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(center_coord_label),
            FadeOut(radius_label_text),
            FadeOut(example),
            run_time=0.6
        )
    
    def show_general_equation(self):
        """场景4: 一般方程"""
        # 标题
        title = Text(
            "一般方程",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 一般方程
        general_eq = MathTex(
            r"x^2 + y^2 + Dx + Ey + F = 0",
            font_size=30,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(general_eq), run_time=1.0)
        self.wait(0.5)
        
        # 配方过程提示
        hint = Text(
            "通过配方可得:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(hint), run_time=0.5)
        
        # 配方结果
        completed_square = MathTex(
            r"\left(x + \frac{D}{2}\right)^2 + \left(y + \frac{E}{2}\right)^2 = \frac{D^2 + E^2 - 4F}{4}",
            font_size=24,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(Write(completed_square), run_time=1.5)
        self.wait(0.8)
        
        # 圆心公式
        center_formula = MathTex(
            r"\text{圆心: } \left(-\frac{D}{2}, -\frac{E}{2}\right)",
            font_size=26,
            color=self.COLOR_SECONDARY,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(UP * 1.2)
        
        self.play(Write(center_formula), run_time=0.8)
        
        # 半径公式
        radius_formula = MathTex(
            r"r = \frac{1}{2}\sqrt{D^2 + E^2 - 4F}",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.3)
        
        self.play(Write(radius_formula), run_time=0.8)
        
        # 判别条件
        condition = MathTex(
            r"D^2 + E^2 - 4F > 0",
            font_size=24,
            color=RED
        ).move_to(DOWN * 0.8)
        
        condition_text = Text(
            "(表示圆)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(condition, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(condition),
            FadeIn(condition_text),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(general_eq),
            FadeOut(hint),
            FadeOut(completed_square),
            FadeOut(center_formula),
            FadeOut(radius_formula),
            FadeOut(condition),
            FadeOut(condition_text),
            run_time=0.6
        )
    
    def show_line_separate(self):
        """场景5: 直线与圆（相离）"""
        # 标题
        title = Text(
            "直线与圆的位置关系",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_LINE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 副标题
        subtitle = Text(
            "1. 相离",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 绘制直线
        x_range = [-3, 4]
        line_points = [
            self.axes.c2p(x, self.line_separate_func(x))
            for x in x_range
        ]
        
        line = Line(
            line_points[0],
            line_points[1],
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        self.play(Create(line), run_time=0.8)
        
        # 计算并标注距离
        # 找到圆心到直线的垂足
        center_coords = self.axes.p2c(self.center)
        m = 0.5  # 斜率
        c = 4    # 截距
        
        # 垂足公式
        x_foot = (center_coords[0] + m * (center_coords[1] - c)) / (1 + m**2)
        y_foot = m * x_foot + c
        foot_point = self.axes.c2p(x_foot, y_foot)
        
        # 距离线段
        distance_line = DashedLine(
            self.center,
            foot_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(distance_line), run_time=0.8)
        
        # 距离标注
        d_label = MathTex("d", font_size=24, color=WHITE).next_to(
            distance_line.get_center(), LEFT, buff=0.1
        )
        
        self.play(FadeIn(d_label), run_time=0.5)
        
        # 半径线段（用于比较）
        radius_line = Line(
            self.center,
            self.center + self.radius_pixels * UP,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        r_label = MathTex("r", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(
            radius_line.get_center(), RIGHT, buff=0.1
        )
        
        self.play(Create(radius_line), FadeIn(r_label), run_time=0.7)
        
        # 不等式
        inequality = MathTex(
            r"d > r",
            font_size=32,
            color=RED
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(inequality, shift=UP * 0.3), run_time=0.7)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(distance_line),
            FadeOut(d_label),
            FadeOut(radius_line),
            FadeOut(r_label),
            FadeOut(inequality),
            run_time=0.5
        )
        
        # 保留直线和标题
        self.line = line
        self.title_relation = title
    
    def show_line_tangent(self):
        """场景6: 直线与圆（相切）"""
        # 更新副标题
        subtitle = Text(
            "2. 相切",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 直线移动到相切位置
        x_range = [-3, 4]
        tangent_line = Line(
            self.axes.c2p(x_range[0], self.line_tangent_y),
            self.axes.c2p(x_range[1], self.line_tangent_y),
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        self.play(Transform(self.line, tangent_line), run_time=1.0)
        
        # 切点
        tangent_point = self.center + self.radius_pixels * UP
        tangent_dot = Dot(tangent_point, color=self.COLOR_HIGHLIGHT, radius=0.06)
        tangent_label = Text("P", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(
            tangent_dot, RIGHT, buff=0.1
        )
        
        self.play(
            FadeIn(tangent_dot, scale=0.5),
            FadeIn(tangent_label),
            run_time=0.7
        )
        
        # 半径线段
        radius_line = Line(
            self.center,
            tangent_point,
            color=self.COLOR_SECONDARY,
            stroke_width=2
        )
        
        self.play(Create(radius_line), run_time=0.6)
        
        # 垂直符号
        right_angle = self.create_right_angle_mark(
            tangent_point,
            self.center,
            tangent_point + RIGHT,
            size=0.2
        )
        
        self.play(FadeIn(right_angle), run_time=0.5)
        
        # 等式
        equality = MathTex(
            r"d = r",
            font_size=32,
            color=YELLOW
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(equality, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(tangent_dot),
            FadeOut(tangent_label),
            FadeOut(radius_line),
            FadeOut(right_angle),
            FadeOut(equality),
            run_time=0.5
        )
    
    def show_line_intersect(self):
        """场景7: 直线与圆（相交）+ 总结"""
        # 更新副标题
        subtitle = Text(
            "3. 相交",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 直线移动到相交位置
        x_range = [-3, 4]
        intersect_line_points = [
            self.axes.c2p(x, self.line_intersect_func(x))
            for x in x_range
        ]
        
        intersect_line = Line(
            intersect_line_points[0],
            intersect_line_points[1],
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        self.play(Transform(self.line, intersect_line), run_time=1.0)
        
        # 计算交点（数值方法）
        # 圆: (x-2)² + (y-1)² = 2.25
        # 直线: y = 0.5x - 0.5
        # 代入: (x-2)² + (0.5x-0.5-1)² = 2.25
        # (x-2)² + (0.5x-1.5)² = 2.25
        # x² - 4x + 4 + 0.25x² - 1.5x + 2.25 = 2.25
        # 1.25x² - 5.5x + 4 = 0
        
        a_coef = 1.25
        b_coef = -5.5
        c_coef = 4
        
        discriminant = b_coef**2 - 4*a_coef*c_coef
        x1 = (-b_coef + np.sqrt(discriminant)) / (2*a_coef)
        x2 = (-b_coef - np.sqrt(discriminant)) / (2*a_coef)
        
        y1 = self.line_intersect_func(x1)
        y2 = self.line_intersect_func(x2)
        
        point1 = self.axes.c2p(x1, y1)
        point2 = self.axes.c2p(x2, y2)
        
        # 交点标记
        intersection_dots = VGroup(
            Dot(point1, color=self.COLOR_HIGHLIGHT, radius=0.06),
            Dot(point2, color=self.COLOR_HIGHLIGHT, radius=0.06)
        )
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in intersection_dots],
            run_time=0.7
        )
        
        # 不等式
        inequality = MathTex(
            r"d < r",
            font_size=32,
            color=GREEN
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(inequality, shift=UP * 0.3), run_time=0.7)
        self.wait(1.0)
        
        # 总结卡片
        self.play(
            FadeOut(subtitle),
            FadeOut(intersection_dots),
            FadeOut(inequality),
            run_time=0.5
        )
        
        # 总结
        summary_title = Text(
            "三种位置关系",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        summary_content = VGroup(
            MathTex(r"d > r", font_size=24, color=RED).next_to(summary_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.5),
            Text("相离", font="Noto Sans CJK SC", font_size=22, color=GRAY_A).next_to(summary_title, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 2),
            
            MathTex(r"d = r", font_size=24, color=YELLOW).next_to(summary_title, DOWN, buff=0.9, aligned_edge=LEFT).shift(RIGHT * 0.5),
            Text("相切", font="Noto Sans CJK SC", font_size=22, color=GRAY_A).next_to(summary_title, DOWN, buff=0.9, aligned_edge=LEFT).shift(RIGHT * 2),
            
            MathTex(r"d < r", font_size=24, color=GREEN).next_to(summary_title, DOWN, buff=1.4, aligned_edge=LEFT).shift(RIGHT * 0.5),
            Text("相交", font="Noto Sans CJK SC", font_size=22, color=GRAY_A).next_to(summary_title, DOWN, buff=1.4, aligned_edge=LEFT).shift(RIGHT * 2),
        )
        
        self.play(FadeIn(summary_title), run_time=0.6)
        self.play(
            *[FadeIn(item, shift=UP * 0.2) for item in summary_content],
            run_time=1.0,
            lag_ratio=0.2
        )
        self.wait(2.5)
        
        # 清理所有
        self.play(
            FadeOut(self.title_relation),
            FadeOut(self.line),
            FadeOut(self.circle),
            FadeOut(self.center_dot),
            FadeOut(self.center_label),
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(summary_title),
            FadeOut(summary_content),
            run_time=0.8
        )
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = point1 - corner
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = point2 - corner
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        square = Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
        return square
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者名称放大
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
        
        # 装饰圆圈
        circles = VGroup(*[
            Circle(
                radius=0.3,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6,
                stroke_width=0
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in circles],
            run_time=0.8,
            lag_ratio=0.1
        )
        
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )


# 运行命令:
# manim -pql circle_equation.py CircleEquation  # 快速预览
# manim -qh circle_equation.py CircleEquation   # 高质量渲染
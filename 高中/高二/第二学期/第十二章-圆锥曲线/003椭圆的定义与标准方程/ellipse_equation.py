"""
椭圆的定义与标准方程动画 - Ellipse Definition and Equation Animation
使用 Manim 创建的高中几何教学视频

内容: 椭圆定义、标准方程、a²=b²+c²关系、顶点
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


class EllipseEquation(Scene):
    """
    椭圆方程教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 椭圆的定义
    3. 动态绘制椭圆
    4. 标准方程（焦点在x轴）
    5. 标准方程（焦点在y轴）
    6. a、b、c的关系
    7. 四个顶点
    8. 总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#e74c3c"      # 红色 - 椭圆
        self.COLOR_FOCUS = "#f39c12"        # 橙色 - 焦点
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮色
        self.COLOR_AUXILIARY = GRAY_B        # 辅助线
        self.COLOR_AXIS_MAJOR = "#3498db"   # 蓝色 - 长轴
        self.COLOR_AXIS_MINOR = "#2ecc71"   # 绿色 - 短轴
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_dynamic_drawing()
        self.show_standard_equation_x()
        self.show_standard_equation_y()
        self.show_abc_relation()
        self.show_vertices()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化椭圆和所有几何元素"""
        # 椭圆参数
        self.a = 3.0  # 长半轴
        self.b = 2.0  # 短半轴
        self.c = np.sqrt(self.a**2 - self.b**2)  # 半焦距
        
        # 缩放因子（用于适配屏幕）
        self.SCALE = 0.65
        self.OFFSET = UP * 1.0
        
        # 坐标系配置
        self.axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=7 * self.SCALE,
            y_length=5 * self.SCALE,
            axis_config={
                "include_numbers": False,
                "stroke_color": GRAY_B,
                "stroke_width": 2
            }
        ).move_to(self.OFFSET)
        
        # 坐标轴标签
        self.x_label = MathTex("x", font_size=24, color=GRAY_A).next_to(
            self.axes.x_axis.get_end(), RIGHT, buff=0.1
        )
        self.y_label = MathTex("y", font_size=24, color=GRAY_A).next_to(
            self.axes.y_axis.get_end(), UP, buff=0.1
        )
        
        # 焦点位置（在坐标系中）
        self.F1_coords = np.array([-self.c, 0, 0])
        self.F2_coords = np.array([self.c, 0, 0])
        
        # 转换为屏幕坐标
        self.F1 = self.axes.c2p(self.F1_coords[0], self.F1_coords[1])
        self.F2 = self.axes.c2p(self.F2_coords[0], self.F2_coords[1])
        
        # 顶点位置
        self.A1 = self.axes.c2p(-self.a, 0)  # 左顶点
        self.A2 = self.axes.c2p(self.a, 0)   # 右顶点
        self.B1 = self.axes.c2p(0, -self.b)  # 下顶点
        self.B2 = self.axes.c2p(0, self.b)   # 上顶点
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何数据初始化完成")
        print(f"  a = {self.a}, b = {self.b}, c = {self.c:.4f}")
        print(f"  a² = {self.a**2}, b² = {self.b**2}, c² = {self.c**2:.4f}")
        print(f"  验证: a² = b² + c² => {self.a**2} = {self.b**2} + {self.c**2:.4f}")
    
    def verify_geometry(self):
        """验证几何关系"""
        epsilon = 1e-6
        
        # 验证 a² = b² + c²
        a_squared = self.a ** 2
        b_squared = self.b ** 2
        c_squared = self.c ** 2
        
        if abs(a_squared - (b_squared + c_squared)) > epsilon:
            raise ValueError(f"关系错误: a²={a_squared} ≠ b²+c²={b_squared + c_squared}")
        
        # 验证 a > b > 0
        if not (self.a > self.b > 0):
            raise ValueError(f"参数约束错误: a={self.a}, b={self.b}")
        
        # 验证 2a > 2c
        if not (2 * self.a > 2 * self.c):
            raise ValueError(f"椭圆定义错误: 2a={2*self.a} 不大于 2c={2*self.c}")
        
        print("✓ 几何关系验证通过")
    
    def ellipse_point(self, t):
        """
        计算椭圆上参数t对应的点
        参数方程: x = a*cos(t), y = b*sin(t)
        """
        x = self.a * np.cos(t)
        y = self.b * np.sin(t)
        return self.axes.c2p(x, y)
    
    def distance_sum_at_t(self, t):
        """计算参数t对应点到两焦点距离之和"""
        point = self.ellipse_point(t)
        dist1 = np.linalg.norm(point - self.F1)
        dist2 = np.linalg.norm(point - self.F2)
        return dist1 + dist2
    
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
            "椭圆是怎么画出来的？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=1.0)
        
        # 创建坐标系
        axes_group = VGroup(self.axes, self.x_label, self.y_label)
        self.play(Create(axes_group), run_time=1.0)
        
        # 创建椭圆
        self.ellipse = Ellipse(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * self.b * self.axes.y_axis.unit_size,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(Create(self.ellipse), run_time=1.5)
        self.wait(1.0)
        
        # 清理钩子
        self.play(FadeOut(hook), run_time=0.4)
    
    def show_definition(self):
        """场景2: 椭圆的定义"""
        # 标题
        title = Text(
            "椭圆的定义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 椭圆淡化
        self.play(self.ellipse.animate.set_stroke(opacity=0.3), run_time=0.4)
        
        # 焦点标记
        f1_dot = Dot(self.F1, color=self.COLOR_FOCUS, radius=0.1)
        f1_label = MathTex("F_1", font_size=24, color=self.COLOR_FOCUS).next_to(
            f1_dot, DOWN, buff=0.15
        )
        
        f2_dot = Dot(self.F2, color=self.COLOR_FOCUS, radius=0.1)
        f2_label = MathTex("F_2", font_size=24, color=self.COLOR_FOCUS).next_to(
            f2_dot, DOWN, buff=0.15
        )
        
        self.play(
            FadeIn(f1_dot, scale=0.5),
            Flash(f1_dot, color=self.COLOR_FOCUS, flash_radius=0.3),
            run_time=0.6
        )
        self.play(FadeIn(f1_label), run_time=0.3)
        
        self.play(
            FadeIn(f2_dot, scale=0.5),
            Flash(f2_dot, color=self.COLOR_FOCUS, flash_radius=0.3),
            run_time=0.6
        )
        self.play(FadeIn(f2_label), run_time=0.3)
        
        # 椭圆上一点P（右顶点开始）
        point_P = Dot(self.A2, color=YELLOW, radius=0.08)
        p_label = Text("P", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(
            point_P, UP + RIGHT, buff=0.1
        )
        
        self.play(FadeIn(point_P, scale=0.5), FadeIn(p_label), run_time=0.5)
        
        # 连线 PF1 和 PF2
        line_pf1 = Line(point_P.get_center(), self.F1, color=self.COLOR_AUXILIARY, stroke_width=2)
        line_pf2 = Line(point_P.get_center(), self.F2, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(line_pf1), run_time=0.5)
        self.play(Create(line_pf2), run_time=0.5)
        
        # 距离标注
        dist1 = np.linalg.norm(point_P.get_center() - self.F1)
        dist2 = np.linalg.norm(point_P.get_center() - self.F2)
        
        # 转换为坐标系单位
        dist1_units = dist1 / self.axes.x_axis.unit_size
        dist2_units = dist2 / self.axes.x_axis.unit_size
        
        d1_label = MathTex(
            f"|PF_1| = {dist1_units:.2f}",
            font_size=20,
            color=YELLOW
        ).next_to(line_pf1.get_center(), UP, buff=0.1)
        
        d2_label = MathTex(
            f"|PF_2| = {dist2_units:.2f}",
            font_size=20,
            color=YELLOW
        ).next_to(line_pf2.get_center(), DOWN, buff=0.1)
        
        self.play(FadeIn(d1_label), FadeIn(d2_label), run_time=0.8)
        
        # 定义公式
        definition = MathTex(
            r"|PF_1| + |PF_2| = 2a",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        sum_value = dist1_units + dist2_units
        sum_label = MathTex(
            f"= {sum_value:.2f}",
            font_size=26,
            color=YELLOW
        ).next_to(definition, RIGHT, buff=0.2)
        
        self.play(Write(definition), run_time=1.0)
        self.play(FadeIn(sum_label), run_time=0.5)
        
        # P点移动到另一个位置（上顶点）
        new_point = self.B2
        
        # 创建动画组
        self.play(
            point_P.animate.move_to(new_point),
            p_label.animate.next_to(new_point, UP, buff=0.1),
            run_time=2.0
        )
        
        # 更新连线
        new_line_pf1 = Line(new_point, self.F1, color=self.COLOR_AUXILIARY, stroke_width=2)
        new_line_pf2 = Line(new_point, self.F2, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(
            Transform(line_pf1, new_line_pf1),
            Transform(line_pf2, new_line_pf2),
            run_time=0.8
        )
        
        # 更新距离标注
        new_dist1 = np.linalg.norm(new_point - self.F1) / self.axes.x_axis.unit_size
        new_dist2 = np.linalg.norm(new_point - self.F2) / self.axes.x_axis.unit_size
        new_sum = new_dist1 + new_dist2
        
        new_d1_label = MathTex(
            f"|PF_1| = {new_dist1:.2f}",
            font_size=20,
            color=YELLOW
        ).next_to(new_line_pf1.get_center(), LEFT, buff=0.1)
        
        new_d2_label = MathTex(
            f"|PF_2| = {new_dist2:.2f}",
            font_size=20,
            color=YELLOW
        ).next_to(new_line_pf2.get_center(), RIGHT, buff=0.1)
        
        new_sum_label = MathTex(
            f"= {new_sum:.2f}",
            font_size=26,
            color=YELLOW
        ).next_to(definition, RIGHT, buff=0.2)
        
        self.play(
            Transform(d1_label, new_d1_label),
            Transform(d2_label, new_d2_label),
            Transform(sum_label, new_sum_label),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(point_P),
            FadeOut(p_label),
            FadeOut(line_pf1),
            FadeOut(line_pf2),
            FadeOut(d1_label),
            FadeOut(d2_label),
            FadeOut(definition),
            FadeOut(sum_label),
            run_time=0.6
        )
        
        # 恢复椭圆
        self.play(self.ellipse.animate.set_stroke(opacity=1.0), run_time=0.3)
        
        # 保存焦点
        self.f1_dot = f1_dot
        self.f1_label = f1_label
        self.f2_dot = f2_dot
        self.f2_label = f2_label
    
    def show_dynamic_drawing(self):
        """场景3: 动态绘制椭圆"""
        # 标题
        title = Text(
            "用定义画椭圆",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 椭圆消失
        self.play(FadeOut(self.ellipse), run_time=0.4)
        
        # ValueTracker 控制参数t
        t_tracker = ValueTracker(0)
        
        # 动态点P
        point_P = always_redraw(
            lambda: Dot(
                self.ellipse_point(t_tracker.get_value()),
                color=YELLOW,
                radius=0.08
            )
        )
        
        # 动态连线
        line_pf1 = always_redraw(
            lambda: Line(
                self.ellipse_point(t_tracker.get_value()),
                self.F1,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
        )
        
        line_pf2 = always_redraw(
            lambda: Line(
                self.ellipse_point(t_tracker.get_value()),
                self.F2,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
        )
        
        # 距离和显示
        sum_decimal = always_redraw(
            lambda: DecimalNumber(
                self.distance_sum_at_t(t_tracker.get_value()) / self.axes.x_axis.unit_size,
                num_decimal_places=2,
                font_size=26,
                color=self.COLOR_HIGHLIGHT
            ).move_to(DOWN * 4)
        )
        
        sum_label = MathTex(
            r"|PF_1| + |PF_2| = ",
            font_size=26,
            color=WHITE
        ).next_to(sum_decimal, LEFT, buff=0.1)
        
        # 轨迹
        trace = TracedPath(
            lambda: self.ellipse_point(t_tracker.get_value()),
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=3,
            dissipating_time=None
        )
        
        self.add(point_P, line_pf1, line_pf2, trace, sum_decimal, sum_label)
        
        # P点沿椭圆移动一周
        self.play(
            t_tracker.animate.set_value(2 * PI),
            run_time=4.5,
            rate_func=linear
        )
        
        self.wait(1.0)
        
        # 清理动态元素，恢复椭圆
        self.remove(point_P, line_pf1, line_pf2, trace)
        self.play(
            FadeOut(title),
            FadeOut(sum_decimal),
            FadeOut(sum_label),
            run_time=0.5
        )
        
        # 椭圆重新出现
        self.ellipse = Ellipse(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * self.b * self.axes.y_axis.unit_size,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(Create(self.ellipse), run_time=0.8)
    
    def show_standard_equation_x(self):
        """场景4: 标准方程（焦点在x轴）"""
        # 标题
        title = Text(
            "标准方程",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "焦点在x轴",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.9)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 标准方程
        equation = MathTex(
            r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4)
        
        condition = MathTex(
            r"(a > b > 0)",
            font_size=24,
            color=GRAY_A
        ).next_to(equation, DOWN, buff=0.2)
        
        self.play(Write(equation), run_time=1.2)
        self.play(FadeIn(condition), run_time=0.5)
        
        # 长轴
        major_axis = Line(self.A1, self.A2, color=self.COLOR_AXIS_MAJOR, stroke_width=4)
        self.play(Create(major_axis), run_time=0.7)
        
        # a标注
        a_brace = Brace(major_axis, direction=DOWN, buff=0.1, color=self.COLOR_AXIS_MAJOR)
        a_label = MathTex("2a", font_size=24, color=self.COLOR_AXIS_MAJOR).next_to(
            a_brace, DOWN, buff=0.05
        )
        
        self.play(FadeIn(a_brace), FadeIn(a_label), run_time=0.8)
        self.wait(0.5)
        
        # 短轴
        minor_axis = Line(self.B1, self.B2, color=self.COLOR_AXIS_MINOR, stroke_width=4)
        self.play(Create(minor_axis), run_time=0.7)
        
        # b标注
        b_brace = Brace(minor_axis, direction=RIGHT, buff=0.1, color=self.COLOR_AXIS_MINOR)
        b_label = MathTex("2b", font_size=24, color=self.COLOR_AXIS_MINOR).next_to(
            b_brace, RIGHT, buff=0.05
        )
        
        self.play(FadeIn(b_brace), FadeIn(b_label), run_time=0.8)
        
        # 焦距标注
        focus_line = DashedLine(self.F1, self.F2, color=self.COLOR_FOCUS, stroke_width=2, dash_length=0.08)
        self.play(Create(focus_line), run_time=0.5)
        
        c_brace = Brace(Line(self.F1, self.axes.c2p(0, 0)), direction=DOWN, buff=0.3, color=self.COLOR_FOCUS)
        c_label = MathTex("c", font_size=22, color=self.COLOR_FOCUS).next_to(
            c_brace, DOWN, buff=0.05
        )
        
        self.play(FadeIn(c_brace), FadeIn(c_label), run_time=0.6)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(equation),
            FadeOut(condition),
            FadeOut(major_axis),
            FadeOut(minor_axis),
            FadeOut(a_brace),
            FadeOut(a_label),
            FadeOut(b_brace),
            FadeOut(b_label),
            FadeOut(focus_line),
            FadeOut(c_brace),
            FadeOut(c_label),
            run_time=0.6
        )
    
    def show_standard_equation_y(self):
        """场景5: 标准方程（焦点在y轴）"""
        # 副标题
        subtitle = Text(
            "焦点在y轴",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.2)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 原椭圆和焦点淡出
        self.play(
            FadeOut(self.ellipse),
            FadeOut(self.f1_dot),
            FadeOut(self.f1_label),
            FadeOut(self.f2_dot),
            FadeOut(self.f2_label),
            run_time=0.4
        )
        
        # 新椭圆（长轴在y轴）
        ellipse_vertical = Ellipse(
            width=2 * self.b * self.axes.x_axis.unit_size,
            height=2 * self.a * self.axes.y_axis.unit_size,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(FadeIn(ellipse_vertical), run_time=1.0)
        
        # 新焦点（在y轴上）
        f1_new = self.axes.c2p(0, -self.c)
        f2_new = self.axes.c2p(0, self.c)
        
        f1_dot_new = Dot(f1_new, color=self.COLOR_FOCUS, radius=0.1)
        f1_label_new = MathTex("F_1", font_size=24, color=self.COLOR_FOCUS).next_to(
            f1_dot_new, LEFT, buff=0.15
        )
        
        f2_dot_new = Dot(f2_new, color=self.COLOR_FOCUS, radius=0.1)
        f2_label_new = MathTex("F_2", font_size=24, color=self.COLOR_FOCUS).next_to(
            f2_dot_new, LEFT, buff=0.15
        )
        
        self.play(
            FadeIn(f1_dot_new, scale=0.5),
            FadeIn(f1_label_new),
            FadeIn(f2_dot_new, scale=0.5),
            FadeIn(f2_label_new),
            run_time=1.5
        )
        
        # 方程
        equation_vertical = MathTex(
            r"\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(equation_vertical), run_time=1.2)
        
        # 对比提示
        comparison = Text(
            "注意：a、b位置互换",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(comparison, shift=UP * 0.3), run_time=0.8)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(ellipse_vertical),
            FadeOut(f1_dot_new),
            FadeOut(f1_label_new),
            FadeOut(f2_dot_new),
            FadeOut(f2_label_new),
            FadeOut(equation_vertical),
            FadeOut(comparison),
            run_time=0.6
        )
        
        # 恢复原椭圆和焦点
        self.ellipse = Ellipse(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * self.b * self.axes.y_axis.unit_size,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(
            FadeIn(self.ellipse),
            FadeIn(self.f1_dot),
            FadeIn(self.f1_label),
            FadeIn(self.f2_dot),
            FadeIn(self.f2_label),
            run_time=0.5
        )
    
    def show_abc_relation(self):
        """场景6: a、b、c的关系"""
        # 标题
        title = Text(
            "a、b、c的关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 椭圆淡化
        self.play(self.ellipse.animate.set_stroke(opacity=0.2), run_time=0.4)
        
        # 构造直角三角形：从原点O到右顶点A2，从原点到右焦点F2，从F2到B2
        # 但更直观的是：从中心到右顶点(a, 0)，从中心到上顶点(0, b)，连接后形成直角三角形
        # 实际上最直观的是：OA2 = a, OB2 = b, OF2 = c
        # 在右边构造：从O到A2(长a)，从O垂直向上到点(a, b)高度b，斜边就是√(a²+b²)
        
        # 但椭圆中 a² = b² + c²，所以应该是：
        # 从O到B2(短b)，从O到F2(焦c)，从B2到F2(长a)
        
        # 让我们构造：从原点O，到右焦点F2（长度c），垂直向上到(c, b)（高度b），从原点到(c, b)（长度a）
        
        origin = self.axes.c2p(0, 0)
        right_focus = self.F2
        top_point = self.axes.c2p(self.c, self.b)
        
        # 三角形的三条边
        side_c = Line(origin, right_focus, color=self.COLOR_FOCUS, stroke_width=3)
        side_b = Line(right_focus, top_point, color=self.COLOR_AXIS_MINOR, stroke_width=3)
        side_a = Line(top_point, origin, color=self.COLOR_AXIS_MAJOR, stroke_width=3)
        
        triangle = VGroup(side_c, side_b, side_a)
        
        self.play(Create(triangle), run_time=2.0, lag_ratio=0.3)
        
        # 标注边长
        c_label = MathTex("c", font_size=24, color=self.COLOR_FOCUS).next_to(
            side_c.get_center(), DOWN, buff=0.1
        )
        b_label = MathTex("b", font_size=24, color=self.COLOR_AXIS_MINOR).next_to(
            side_b.get_center(), RIGHT, buff=0.1
        )
        a_label = MathTex("a", font_size=24, color=self.COLOR_AXIS_MAJOR).next_to(
            side_a.get_center(), LEFT, buff=0.15
        )
        
        self.play(
            FadeIn(c_label),
            FadeIn(b_label),
            FadeIn(a_label),
            run_time=1.0,
            lag_ratio=0.2
        )
        
        # 直角标记
        right_angle = self.create_right_angle_mark(
            right_focus,
            origin,
            top_point,
            size=0.25
        )
        
        self.play(FadeIn(right_angle), run_time=0.5)
        
        # 关系式
        relation = MathTex(
            r"a^2 = b^2 + c^2",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(relation), run_time=1.5)
        
        # 数值验证
        verification = MathTex(
            f"9 = 4 + 5",
            font_size=26,
            color=YELLOW
        ).next_to(relation, DOWN, buff=0.3)
        
        self.play(FadeIn(verification, shift=UP * 0.2), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(triangle),
            FadeOut(c_label),
            FadeOut(b_label),
            FadeOut(a_label),
            FadeOut(right_angle),
            FadeOut(relation),
            FadeOut(verification),
            run_time=0.6
        )
        
        # 恢复椭圆
        self.play(self.ellipse.animate.set_stroke(opacity=1.0), run_time=0.3)
    
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
    
    def show_vertices(self):
        """场景7: 四个顶点"""
        # 标题
        title = Text(
            "椭圆的顶点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 长轴顶点
        a1_dot = Dot(self.A1, color=self.COLOR_AXIS_MAJOR, radius=0.08)
        a2_dot = Dot(self.A2, color=self.COLOR_AXIS_MAJOR, radius=0.08)
        
        a1_label = MathTex("(-a, 0)", font_size=20, color=self.COLOR_AXIS_MAJOR).next_to(
            a1_dot, LEFT, buff=0.1
        )
        a2_label = MathTex("(a, 0)", font_size=20, color=self.COLOR_AXIS_MAJOR).next_to(
            a2_dot, RIGHT, buff=0.1
        )
        
        self.play(
            Flash(a1_dot, color=self.COLOR_AXIS_MAJOR),
            Flash(a2_dot, color=self.COLOR_AXIS_MAJOR),
            run_time=0.6
        )
        self.play(
            FadeIn(a1_dot),
            FadeIn(a2_dot),
            FadeIn(a1_label),
            FadeIn(a2_label),
            run_time=0.6
        )
        
        # 短轴顶点
        b1_dot = Dot(self.B1, color=self.COLOR_AXIS_MINOR, radius=0.08)
        b2_dot = Dot(self.B2, color=self.COLOR_AXIS_MINOR, radius=0.08)
        
        b1_label = MathTex("(0, -b)", font_size=20, color=self.COLOR_AXIS_MINOR).next_to(
            b1_dot, DOWN, buff=0.1
        )
        b2_label = MathTex("(0, b)", font_size=20, color=self.COLOR_AXIS_MINOR).next_to(
            b2_dot, UP, buff=0.1
        )
        
        self.play(
            Flash(b1_dot, color=self.COLOR_AXIS_MINOR),
            Flash(b2_dot, color=self.COLOR_AXIS_MINOR),
            run_time=0.6
        )
        self.play(
            FadeIn(b1_dot),
            FadeIn(b2_dot),
            FadeIn(b1_label),
            FadeIn(b2_label),
            run_time=0.6
        )
        
        # 总结文字
        summary = Text(
            "四个顶点：(±a, 0)和(0, ±b)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary, shift=UP * 0.3), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(a1_dot),
            FadeOut(a2_dot),
            FadeOut(b1_dot),
            FadeOut(b2_dot),
            FadeOut(a1_label),
            FadeOut(a2_label),
            FadeOut(b1_label),
            FadeOut(b2_label),
            FadeOut(summary),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 总结 + 片尾"""
        # 清空场景
        self.play(
            FadeOut(self.ellipse),
            FadeOut(self.f1_dot),
            FadeOut(self.f1_label),
            FadeOut(self.f2_dot),
            FadeOut(self.f2_label),
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            run_time=0.6
        )
        
        # 总结标题
        summary_title = Text(
            "椭圆知识总结",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 三个要点卡片
        card1 = self.create_summary_card(
            "定义",
            "|PF₁| + |PF₂| = 2a",
            self.COLOR_PRIMARY,
            UP * 1
        )
        
        card2 = self.create_summary_card(
            "方程",
            "x²/a² + y²/b² = 1",
            self.COLOR_AXIS_MAJOR,
            ORIGIN
        )
        
        card3 = self.create_summary_card(
            "关系",
            "a² = b² + c²",
            self.COLOR_FOCUS,
            DOWN * 1
        )
        
        cards = VGroup(card1, card2, card3)
        
        for card in cards:
            self.play(card.animate.shift(RIGHT * 0), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理总结
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=0.5
        )
        
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
        
        # 装饰椭圆
        ellipses = VGroup(*[
            Ellipse(
                width=0.6,
                height=0.4,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.5,
                stroke_width=2
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(ellipse, scale=0.5) for ellipse in ellipses],
            run_time=0.8,
            lag_ratio=0.1
        )
        
        self.play(Rotate(ellipses, angle=PI, run_time=1.5))
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(ellipses),
            run_time=1.0
        )
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 图标
        icon = Ellipse(
            width=0.4,
            height=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=26,
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


# 运行命令:
# manim -pql ellipse_equation.py EllipseEquation  # 快速预览
# manim -qh ellipse_equation.py EllipseEquation   # 高质量渲染
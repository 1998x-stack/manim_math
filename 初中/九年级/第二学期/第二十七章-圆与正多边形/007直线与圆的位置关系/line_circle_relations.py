"""
直线与圆的位置关系 - Line and Circle Position Relationships
使用 Manim 创建的初中几何教学视频

内容: d<r相交, d=r相切, d>r相离
目标观众: 初中生
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


class LineCircleRelations(Scene):
    """
    直线与圆的位置关系教学动画
    
    场景顺序:
    1. 开场钩子
    2. 基础概念介绍
    3. 相交 (d < r)
    4. 相切 (d = r)
    5. 相离 (d > r)
    6. 总结对比
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"        # 蓝色 - 圆
        self.COLOR_LINE = "#e74c3c"          # 红色 - 直线
        self.COLOR_PERPENDICULAR = "#2ecc71" # 绿色 - 垂线
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_INTERSECT = "#f39c12"     # 橙色 - 交点
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_basic_concepts()
        self.scene_3_intersecting()
        self.scene_4_tangent()
        self.scene_5_separate()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 圆的基本参数
        self.O = np.array([0, 1, 0])  # 圆心位置
        self.r = 2.0                   # 半径
        
        # 三种情况下的距离d
        self.d_intersect = 1.6   # d < r (相交)
        self.d_tangent = 2.0     # d = r (相切)
        self.d_separate = 3.0    # d > r (相离)
        
        # 验证几何参数
        self.verify_geometry()
        
        # 创建圆对象 (但不添加到场景)
        self.circle = Circle(
            radius=self.r,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
    
    def verify_geometry(self):
        """验证几何参数的正确性"""
        epsilon = 1e-6
        
        # 验证三种情况
        assert self.d_intersect < self.r, "相交条件错误: d应该小于r"
        assert abs(self.d_tangent - self.r) < epsilon, "相切条件错误: d应该等于r"
        assert self.d_separate > self.r, "相离条件错误: d应该大于r"
        
        # 验证边界安全
        # 圆的边界: (O[1] - r) 到 (O[1] + r)
        circle_bottom = self.O[1] - self.r
        circle_top = self.O[1] + self.r
        
        assert circle_bottom > -7, f"圆底部溢出: y={circle_bottom:.2f}"
        assert circle_top < 7, f"圆顶部溢出: y={circle_top:.2f}"
        
        print("✓ 几何验证通过")
        print(f"  圆心: {self.O}, 半径: {self.r}")
        print(f"  d(相交)={self.d_intersect:.1f} < r={self.r}")
        print(f"  d(相切)={self.d_tangent:.1f} = r={self.r}")
        print(f"  d(相离)={self.d_separate:.1f} > r={self.r}")
    
    def calculate_line_y_position(self, distance):
        """
        根据圆心到直线的距离,计算直线的y坐标
        直线为水平线: y = constant
        距离d = |y_line - O[1]|
        这里我们让直线在圆的下方
        """
        return self.O[1] - distance
    
    def calculate_perpendicular_foot(self, line_y):
        """
        计算圆心到水平直线的垂足
        直线: y = line_y
        圆心: self.O
        垂足: (O[0], line_y, 0)
        """
        return np.array([self.O[0], line_y, 0])
    
    def calculate_intersection_points(self, line_y):
        """
        计算直线与圆的交点
        圆: (x-O[0])^2 + (y-O[1])^2 = r^2
        直线: y = line_y
        
        代入: (x-O[0])^2 + (line_y-O[1])^2 = r^2
        解得: x = O[0] ± sqrt(r^2 - (line_y-O[1])^2)
        """
        d = abs(line_y - self.O[1])
        
        if d > self.r + 1e-6:
            # 相离,无交点
            return None, None
        elif abs(d - self.r) < 1e-6:
            # 相切,一个交点
            point = np.array([self.O[0], line_y, 0])
            return point, None
        else:
            # 相交,两个交点
            delta_x = np.sqrt(self.r**2 - d**2)
            point_A = np.array([self.O[0] - delta_x, line_y, 0])
            point_B = np.array([self.O[0] + delta_x, line_y, 0])
            return point_A, point_B
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "直线与圆能有几种相遇方式?",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.2)
        self.wait(0.3)
        
        # 圆淡入
        self.play(FadeIn(self.circle, scale=0.8), run_time=0.5)
        
        # 直线从左侧划入
        line_temp_y = self.calculate_line_y_position(self.d_intersect)
        line_temp = Line(
            LEFT * 4 + UP * line_temp_y,
            RIGHT * 4 + UP * line_temp_y,
            color=self.COLOR_LINE,
            stroke_width=3
        )
        line_temp.shift(LEFT * 10)  # 初始在屏幕外
        
        self.play(line_temp.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 直线上下移动示意
        self.play(
            line_temp.animate.shift(UP * 0.8),
            run_time=0.8,
            rate_func=there_and_back
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(line_temp),
            run_time=0.4
        )
    
    def scene_2_basic_concepts(self):
        """场景2: 基础概念介绍"""
        # 标题
        title = Text(
            "关键要素",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 标记圆心O
        O_dot = Dot(self.O, color=self.COLOR_HIGHLIGHT, radius=0.08)
        O_label = MathTex("O", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(O_dot, UP, buff=0.15)
        
        self.play(FadeIn(O_dot, scale=0.5), run_time=0.3)
        self.play(Flash(O_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.25), run_time=0.3)
        self.play(Write(O_label), run_time=0.3)
        
        # 标记半径r
        radius_point = self.O + RIGHT * self.r
        radius_line = Line(self.O, radius_point, color=self.COLOR_AUXILIARY, stroke_width=2)
        radius_dot = Dot(radius_point, color=self.COLOR_AUXILIARY, radius=0.05)
        
        r_label = MathTex("r", font_size=24, color=WHITE).next_to(
            radius_line.get_center(), DOWN, buff=0.1
        )
        
        self.play(Create(radius_line), FadeIn(radius_dot), run_time=0.5)
        self.play(Write(r_label), run_time=0.3)
        self.wait(0.3)
        
        # 绘制水平直线
        line_y = self.calculate_line_y_position(self.d_intersect)
        line = Line(
            LEFT * 4 + UP * line_y,
            RIGHT * 4 + UP * line_y,
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        line_label = MathTex("l", font_size=28, color=self.COLOR_LINE).next_to(
            line.get_end(), RIGHT, buff=0.2
        )
        
        self.play(Create(line), run_time=0.8)
        self.play(Write(line_label), run_time=0.3)
        
        # 绘制垂线OH
        foot = self.calculate_perpendicular_foot(line_y)
        perpendicular = DashedLine(
            self.O, foot,
            color=self.COLOR_PERPENDICULAR,
            dash_length=0.1,
            stroke_width=2
        )
        
        H_dot = Dot(foot, color=self.COLOR_PERPENDICULAR, radius=0.06)
        H_label = MathTex("H", font_size=20, color=self.COLOR_PERPENDICULAR).next_to(
            H_dot, DOWN, buff=0.12
        )
        
        self.play(Create(perpendicular, rate_func=linear), run_time=1.0)
        self.play(FadeIn(H_dot), Write(H_label), run_time=0.4)
        
        # 标注距离d
        d_value = abs(line_y - self.O[1])
        d_brace = Brace(perpendicular, direction=RIGHT, buff=0.05, color=YELLOW)
        d_label = MathTex("d", font_size=24, color=YELLOW).next_to(d_brace, RIGHT, buff=0.05)
        
        self.play(FadeIn(d_brace), Write(d_label), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "d = 圆心O到直线l的距离",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(radius_line),
            FadeOut(radius_dot),
            FadeOut(r_label),
            FadeOut(perpendicular),
            FadeOut(H_dot),
            FadeOut(H_label),
            FadeOut(d_brace),
            FadeOut(d_label),
            FadeOut(explain),
            FadeOut(line),
            FadeOut(line_label),
            run_time=0.5
        )
        
        # 保留圆心标注
        self.O_dot = O_dot
        self.O_label = O_label
    
    def scene_3_intersecting(self):
        """场景3: 相交 (d < r)"""
        # 标题
        title = VGroup(
            Text("情况1: ", font="PingFang SC", font_size=32, color=WHITE),
            Text("相交", font="PingFang SC", font_size=36, color=self.COLOR_INTERSECT)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建直线在相交位置
        line_y = self.calculate_line_y_position(self.d_intersect)
        line = Line(
            LEFT * 4 + UP * line_y,
            RIGHT * 4 + UP * line_y,
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        self.play(Create(line), run_time=0.6)
        
        # 绘制垂线
        foot = self.calculate_perpendicular_foot(line_y)
        perpendicular = DashedLine(
            self.O, foot,
            color=self.COLOR_PERPENDICULAR,
            dash_length=0.1,
            stroke_width=2
        )
        
        H_dot = Dot(foot, color=self.COLOR_PERPENDICULAR, radius=0.06)
        H_label = MathTex("H", font_size=20, color=self.COLOR_PERPENDICULAR).next_to(
            H_dot, DOWN, buff=0.12
        )
        
        self.play(Create(perpendicular), run_time=0.8)
        self.play(FadeIn(H_dot), Write(H_label), run_time=0.4)
        
        # 标注距离d
        d_brace = Brace(perpendicular, direction=RIGHT, buff=0.05, color=YELLOW)
        d_label = MathTex("d", font_size=24, color=YELLOW).next_to(d_brace, RIGHT, buff=0.05)
        
        self.play(FadeIn(d_brace), Write(d_label), run_time=0.5)
        self.wait(0.5)
        
        # 计算并标注交点
        point_A, point_B = self.calculate_intersection_points(line_y)
        
        A_dot = Dot(point_A, color=self.COLOR_INTERSECT, radius=0.10)
        B_dot = Dot(point_B, color=self.COLOR_INTERSECT, radius=0.10)
        
        A_label = MathTex("A", font_size=24, color=self.COLOR_INTERSECT).next_to(A_dot, DL, buff=0.15)
        B_label = MathTex("B", font_size=24, color=self.COLOR_INTERSECT).next_to(B_dot, DR, buff=0.15)
        
        self.play(FadeIn(A_dot, scale=0.5), run_time=0.3)
        self.play(Flash(A_dot, color=self.COLOR_INTERSECT, flash_radius=0.3), run_time=0.3)
        self.play(Write(A_label), run_time=0.3)
        
        self.play(FadeIn(B_dot, scale=0.5), run_time=0.3)
        self.play(Flash(B_dot, color=self.COLOR_INTERSECT, flash_radius=0.3), run_time=0.3)
        self.play(Write(B_label), run_time=0.3)
        
        # 显示公式和说明
        formula = MathTex(
            "d", "<", "r",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        formula[2].set_color(WHITE)
        
        explain = Text(
            "相交: 有两个公共点",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.8)
        
        self.play(Write(formula), run_time=0.8)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line),
            FadeOut(perpendicular),
            FadeOut(H_dot),
            FadeOut(H_label),
            FadeOut(d_brace),
            FadeOut(d_label),
            FadeOut(A_dot),
            FadeOut(B_dot),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.6
        )
    
    def scene_4_tangent(self):
        """场景4: 相切 (d = r)"""
        # 标题
        title = VGroup(
            Text("情况2: ", font="PingFang SC", font_size=32, color=WHITE),
            Text("相切", font="PingFang SC", font_size=36, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建直线在相切位置
        line_y = self.calculate_line_y_position(self.d_tangent)
        line = Line(
            LEFT * 4 + UP * line_y,
            RIGHT * 4 + UP * line_y,
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        self.play(Create(line), run_time=0.6)
        
        # 绘制垂线(也是半径)
        foot = self.calculate_perpendicular_foot(line_y)
        perpendicular = Line(
            self.O, foot,
            color=self.COLOR_PERPENDICULAR,
            stroke_width=3
        )
        
        T_dot = Dot(foot, color=self.COLOR_HIGHLIGHT, radius=0.10)
        T_label = MathTex("T", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(
            T_dot, DOWN, buff=0.15
        )
        
        self.play(Create(perpendicular), run_time=0.8)
        self.play(FadeIn(T_dot, scale=0.5), run_time=0.3)
        self.play(Flash(T_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.3)
        self.play(Write(T_label), run_time=0.3)
        
        # 标注 d = r
        d_brace = Brace(perpendicular, direction=RIGHT, buff=0.05, color=YELLOW)
        d_r_label = MathTex("d", "=", "r", font_size=24, color=YELLOW).next_to(
            d_brace, RIGHT, buff=0.05
        )
        
        self.play(FadeIn(d_brace), Write(d_r_label), run_time=0.5)
        self.wait(0.5)
        
        # 添加垂直符号
        right_angle = self.create_right_angle_mark(foot, self.O, foot + RIGHT, size=0.2)
        self.play(FadeIn(right_angle), run_time=0.4)
        
        # 显示公式和说明
        formula = MathTex(
            "d", "=", "r",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        formula[2].set_color(WHITE)
        
        explain = Text(
            "相切: 有一个公共点",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.8)
        
        property_text = Text(
            "切线⊥半径",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        
        self.play(Write(formula), run_time=0.8)
        self.play(FadeIn(explain), run_time=0.5)
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line),
            FadeOut(perpendicular),
            FadeOut(T_dot),
            FadeOut(T_label),
            FadeOut(d_brace),
            FadeOut(d_r_label),
            FadeOut(right_angle),
            FadeOut(formula),
            FadeOut(explain),
            FadeOut(property_text),
            run_time=0.6
        )
    
    def scene_5_separate(self):
        """场景5: 相离 (d > r)"""
        # 标题
        title = VGroup(
            Text("情况3: ", font="PingFang SC", font_size=32, color=WHITE),
            Text("相离", font="PingFang SC", font_size=36, color=self.COLOR_AUXILIARY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建直线在相离位置
        line_y = self.calculate_line_y_position(self.d_separate)
        line = Line(
            LEFT * 4 + UP * line_y,
            RIGHT * 4 + UP * line_y,
            color=self.COLOR_LINE,
            stroke_width=3
        )
        
        self.play(Create(line), run_time=0.6)
        
        # 绘制垂线
        foot = self.calculate_perpendicular_foot(line_y)
        perpendicular = DashedLine(
            self.O, foot,
            color=self.COLOR_PERPENDICULAR,
            dash_length=0.1,
            stroke_width=2
        )
        
        H_dot = Dot(foot, color=self.COLOR_PERPENDICULAR, radius=0.06)
        H_label = MathTex("H", font_size=20, color=self.COLOR_PERPENDICULAR).next_to(
            H_dot, DOWN, buff=0.12
        )
        
        self.play(Create(perpendicular), run_time=0.8)
        self.play(FadeIn(H_dot), Write(H_label), run_time=0.4)
        
        # 标注距离d
        d_brace = Brace(perpendicular, direction=RIGHT, buff=0.05, color=YELLOW)
        d_label = MathTex("d", font_size=24, color=YELLOW).next_to(d_brace, RIGHT, buff=0.05)
        
        self.play(FadeIn(d_brace), Write(d_label), run_time=0.5)
        self.wait(0.5)
        
        # 显示公式和说明
        formula = MathTex(
            "d", ">", "r",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        formula[2].set_color(WHITE)
        
        explain = Text(
            "相离: 无公共点",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.8)
        
        self.play(Write(formula), run_time=0.8)
        self.play(FadeIn(explain), run_time=0.5)
        
        # 闪烁提示无交点
        self.play(
            Indicate(line, color=self.COLOR_LINE, scale_factor=1.05),
            Indicate(self.circle, color=self.COLOR_CIRCLE, scale_factor=1.05),
            run_time=1.0
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line),
            FadeOut(perpendicular),
            FadeOut(H_dot),
            FadeOut(H_label),
            FadeOut(d_brace),
            FadeOut(d_label),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.6
        )
    
    def scene_6_summary(self):
        """场景6: 总结对比"""
        # 先移除主圆和圆心标注
        self.play(
            FadeOut(self.circle),
            FadeOut(self.O_dot),
            FadeOut(self.O_label),
            run_time=0.4
        )
        
        # 标题
        title = Text(
            "位置关系判定",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三组对比图
        scale_factor = 0.4
        spacing = 2.8
        base_y = 2.5
        
        # 组1: 相交
        group_1 = self.create_comparison_group(
            "相交",
            self.COLOR_INTERSECT,
            self.d_intersect,
            scale_factor,
            show_intersections=True
        ).move_to(UP * base_y)
        
        formula_1 = MathTex("d", "<", "r", font_size=28).move_to(UP * (base_y - 1.2))
        formula_1[0].set_color(YELLOW)
        formula_1[1].set_color(self.COLOR_HIGHLIGHT)
        
        explain_1 = Text("两个交点", font="PingFang SC", font_size=18, color=self.COLOR_AUXILIARY).move_to(
            UP * (base_y - 1.7)
        )
        
        # 组2: 相切
        group_2 = self.create_comparison_group(
            "相切",
            self.COLOR_HIGHLIGHT,
            self.d_tangent,
            scale_factor,
            show_tangent=True
        ).move_to(UP * (base_y - spacing))
        
        formula_2 = MathTex("d", "=", "r", font_size=28).move_to(UP * (base_y - spacing - 1.2))
        formula_2[0].set_color(YELLOW)
        formula_2[1].set_color(self.COLOR_HIGHLIGHT)
        
        explain_2 = Text("一个切点", font="PingFang SC", font_size=18, color=self.COLOR_AUXILIARY).move_to(
            UP * (base_y - spacing - 1.7)
        )
        
        # 组3: 相离
        group_3 = self.create_comparison_group(
            "相离",
            self.COLOR_AUXILIARY,
            self.d_separate,
            scale_factor,
            show_separate=True
        ).move_to(UP * (base_y - 2 * spacing))
        
        formula_3 = MathTex("d", ">", "r", font_size=28).move_to(UP * (base_y - 2 * spacing - 1.2))
        formula_3[0].set_color(YELLOW)
        formula_3[1].set_color(self.COLOR_HIGHLIGHT)
        
        explain_3 = Text("无交点", font="PingFang SC", font_size=18, color=self.COLOR_AUXILIARY).move_to(
            UP * (base_y - 2 * spacing - 1.7)
        )
        
        # 同时显示所有组
        all_groups = VGroup(
            group_1, formula_1, explain_1,
            group_2, formula_2, explain_2,
            group_3, formula_3, explain_3
        )
        
        self.play(FadeIn(all_groups, shift=UP * 0.5), run_time=1.0)
        self.wait(0.8)
        
        # 依次闪烁
        self.play(Indicate(group_1, color=self.COLOR_INTERSECT), run_time=0.5)
        self.wait(0.3)
        self.play(Indicate(group_2, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(0.3)
        self.play(Indicate(group_3, color=self.COLOR_AUXILIARY), run_time=0.5)
        self.wait(0.5)
        
        # 口诀
        mnemonic = Text(
            "比半径定位置, 看距离识关系",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Write(mnemonic), run_time=1.0)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(all_groups),
            FadeOut(mnemonic),
            run_time=0.6
        )
    
    def create_comparison_group(self, label_text, color, distance, scale, 
                                show_intersections=False, show_tangent=False, show_separate=False):
        """创建对比组图形"""
        group = VGroup()
        
        # 小圆
        small_r = self.r * scale
        small_O = ORIGIN
        
        small_circle = Circle(
            radius=small_r,
            color=self.COLOR_CIRCLE,
            stroke_width=2
        ).move_to(small_O)
        
        # 圆心
        O_dot = Dot(small_O, radius=0.04, color=self.COLOR_AUXILIARY)
        
        # 直线
        line_y_offset = -distance * scale
        line = Line(
            LEFT * 1.5, RIGHT * 1.5,
            color=self.COLOR_LINE,
            stroke_width=2
        ).shift(UP * line_y_offset)
        
        # 垂线
        foot = np.array([0, line_y_offset, 0])
        perpendicular = DashedLine(
            small_O, foot,
            color=self.COLOR_PERPENDICULAR,
            dash_length=0.05,
            stroke_width=1.5
        )
        
        group.add(small_circle, O_dot, line, perpendicular)
        
        # 根据情况添加特殊标记
        if show_intersections:
            # 相交: 两个交点
            scaled_line_y = line_y_offset
            delta_x = np.sqrt(small_r**2 - (scaled_line_y)**2)
            A_dot = Dot(np.array([-delta_x, scaled_line_y, 0]), radius=0.06, color=self.COLOR_INTERSECT)
            B_dot = Dot(np.array([delta_x, scaled_line_y, 0]), radius=0.06, color=self.COLOR_INTERSECT)
            group.add(A_dot, B_dot)
        
        elif show_tangent:
            # 相切: 一个切点
            T_dot = Dot(foot, radius=0.06, color=self.COLOR_HIGHLIGHT)
            group.add(T_dot)
        
        elif show_separate:
            # 相离: 无特殊标记
            pass
        
        # 标签
        label = Text(label_text, font="PingFang SC", font_size=22, color=color).next_to(
            group, LEFT, buff=0.3
        )
        
        return VGroup(label, group)
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = (point1 - corner)
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = (point2 - corner)
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
    
    def scene_7_outro(self):
        """场景7: 片尾关注"""
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
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何知识!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 圆形装饰
        circles = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_CIRCLE, stroke_width=2, fill_opacity=0.3)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )


# 运行命令:
# manim -pql line_circle_relations.py LineCircleRelations  # 快速预览
# manim -qh line_circle_relations.py LineCircleRelations   # 高质量渲染
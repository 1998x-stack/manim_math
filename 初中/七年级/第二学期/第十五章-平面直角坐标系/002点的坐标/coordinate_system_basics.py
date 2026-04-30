"""
平面直角坐标系 - 点的坐标 教学动画
Coordinate System - Point Coordinates Teaching Animation

使用 Manim 创建的七年级数学教学视频
内容: 点的坐标表示、由点确定坐标、由坐标确定点、坐标轴上的点
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CoordinateSystemBasics(Scene):
    """
    平面直角坐标系基础 - 点的坐标
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. 由点确定坐标（第一部分）
    4. 由点确定坐标（更多示例）
    5. 由坐标确定点
    6. 坐标轴上的点（特殊情况）
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调点
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_AXES = WHITE             # 白色 - 坐标轴
        self.COLOR_GRID = "#2c3e50"         # 深灰 - 网格
        
        # 初始化几何数据和坐标系
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_coordinate_system()
        self.show_point_to_coordinate_part1()
        self.show_point_to_coordinate_more_examples()
        self.show_coordinate_to_point()
        self.show_points_on_axes()
        self.show_summary_and_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据 - 统一管理坐标"""
        
        # ===== 坐标系配置 =====
        self.AXES_SCALE = 0.85
        self.AXES_OFFSET = UP * 1.5
        
        # 坐标系单位长度（Manim 坐标 / 逻辑坐标）
        self.UNIT_LENGTH = 0.8
        
        # ===== 创建坐标系 =====
        self.axes = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=self.UNIT_LENGTH * 8,
            y_length=self.UNIT_LENGTH * 6,
            background_line_style={
                "stroke_color": self.COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={
                "stroke_color": self.COLOR_AXES,
                "stroke_width": 2,
                "include_numbers": True,
                "numbers_to_exclude": [0],  # 原点不标注
                "font_size": 20,
            }
        ).scale(self.AXES_SCALE).shift(self.AXES_OFFSET)
        
        # ===== 原点 =====
        self.origin = self.axes.c2p(0, 0)
        
        # ===== 示例点的逻辑坐标 =====
        # 第一象限点
        self.coord_P = np.array([3, 2, 0])
        self.point_P = self.axes.c2p(3, 2)
        
        # 第二象限点
        self.coord_Q = np.array([-2, 1, 0])
        self.point_Q = self.axes.c2p(-2, 1)
        
        # 第四象限点
        self.coord_R = np.array([2, -1.5, 0])
        self.point_R = self.axes.c2p(2, -1.5)
        
        # 由坐标确定的点
        self.coord_S = np.array([2.5, -2, 0])
        self.point_S = self.axes.c2p(2.5, -2)
        
        # x轴上的点
        self.coord_A = np.array([2, 0, 0])
        self.point_A = self.axes.c2p(2, 0)
        
        # y轴上的点
        self.coord_B = np.array([0, -1, 0])
        self.point_B = self.axes.c2p(0, -1)
        
        # ===== 预计算垂足 =====
        # P点的垂足
        self.foot_Px = self.axes.c2p(3, 0)
        self.foot_Py = self.axes.c2p(0, 2)
        
        # Q点的垂足
        self.foot_Qx = self.axes.c2p(-2, 0)
        self.foot_Qy = self.axes.c2p(0, 1)
        
        # R点的垂足
        self.foot_Rx = self.axes.c2p(2, 0)
        self.foot_Ry = self.axes.c2p(0, -1.5)
        
        # S点的垂足（用于由坐标确定点）
        self.foot_Sx = self.axes.c2p(2.5, 0)
        self.foot_Sy = self.axes.c2p(0, -2)
        
        # ===== 验证几何关系 =====
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证坐标系和点的位置正确性"""
        epsilon = 1e-6
        
        # 验证原点
        origin_check = self.axes.c2p(0, 0)
        assert np.allclose(self.origin, origin_check, atol=epsilon), "原点计算错误"
        
        # 验证垂足在轴上
        # P点的x垂足应该y=0
        foot_Px_coords = self.axes.p2c(self.foot_Px)
        assert abs(foot_Px_coords[1]) < epsilon, f"P的x垂足不在x轴上: {foot_Px_coords}"
        
        # P点的y垂足应该x=0
        foot_Py_coords = self.axes.p2c(self.foot_Py)
        assert abs(foot_Py_coords[0]) < epsilon, f"P的y垂足不在y轴上: {foot_Py_coords}"
        
        print("✓ 几何验证通过")
    
    def create_perpendicular_to_x_axis(self, point, color=None, dash_length=0.1):
        """创建从点到x轴的垂线（精确）"""
        if color is None:
            color = self.COLOR_AUXILIARY
        
        # 获取点的坐标
        coords = self.axes.p2c(point)
        x, y = coords[0], coords[1]
        
        # 垂足在x轴上 (x, 0)
        foot = self.axes.c2p(x, 0)
        
        return DashedLine(point, foot, color=color, dash_length=dash_length)
    
    def create_perpendicular_to_y_axis(self, point, color=None, dash_length=0.1):
        """创建从点到y轴的垂线（精确）"""
        if color is None:
            color = self.COLOR_AUXILIARY
        
        # 获取点的坐标
        coords = self.axes.p2c(point)
        x, y = coords[0], coords[1]
        
        # 垂足在y轴上 (0, y)
        foot = self.axes.c2p(0, y)
        
        return DashedLine(point, foot, color=color, dash_length=dash_length)
    
    def create_right_angle_mark(self, corner, direction1, direction2, size=0.15):
        """创建直角标记符号"""
        # 归一化方向向量
        d1 = direction1 / np.linalg.norm(direction1) * size
        d2 = direction2 / np.linalg.norm(direction2) * size
        
        # 创建小正方形
        square = Polygon(
            corner,
            corner + d1,
            corner + d1 + d2,
            corner + d2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=1.5,
            fill_opacity=0
        )
        
        return square
    
    def show_opening(self):
        """场景1: 开场钩子 (3-4秒)"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "如何用数字描述\n平面上的位置?",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 三个神秘点闪烁
        mystery_dots = VGroup(
            Dot(LEFT * 2 + UP, color=self.COLOR_PRIMARY, radius=0.12),
            Dot(RIGHT * 1.5 + DOWN * 0.5, color=self.COLOR_SECONDARY, radius=0.12),
            Dot(DOWN * 1.5, color=self.COLOR_HIGHLIGHT, radius=0.12)
        ).shift(DOWN * 0.5)
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in mystery_dots],
            run_time=0.5
        )
        
        for _ in range(3):
            self.play(
                *[Flash(dot, color=dot.get_color(), flash_radius=0.3) for dot in mystery_dots],
                run_time=0.3
            )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(mystery_dots),
            run_time=0.5
        )
    
    def show_coordinate_system(self):
        """场景2: 建立坐标系 (6-8秒)"""
        # 标题
        title = Text(
            "平面直角坐标系",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)
        
        # 创建坐标轴（分别创建x轴和y轴以便动画）
        self.play(Create(self.axes), run_time=2.0)
        
        # 原点标记
        self.origin_dot = Dot(self.origin, color=self.COLOR_SECONDARY, radius=0.08)
        origin_label = Text("O", font="PingFang SC", font_size=24, color=WHITE).next_to(self.origin_dot, DL, buff=0.15)
        
        self.play(
            FadeIn(self.origin_dot, scale=0.5),
            Write(origin_label),
            run_time=0.6
        )
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=28, color=WHITE).next_to(self.axes.c2p(4, 0), RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28, color=WHITE).next_to(self.axes.c2p(0, 3), UP, buff=0.2)
        
        self.play(
            FadeIn(x_label),
            FadeIn(y_label),
            run_time=0.6
        )
        
        # 象限标注
        quadrant_labels = VGroup(
            Text("I", font="PingFang SC", font_size=24, color=GRAY_A).move_to(self.axes.c2p(2.5, 1.8)),
            Text("II", font="PingFang SC", font_size=24, color=GRAY_A).move_to(self.axes.c2p(-2.5, 1.8)),
            Text("III", font="PingFang SC", font_size=24, color=GRAY_A).move_to(self.axes.c2p(-2.5, -1.8)),
            Text("IV", font="PingFang SC", font_size=24, color=GRAY_A).move_to(self.axes.c2p(2.5, -1.8))
        )
        
        self.play(FadeIn(quadrant_labels, shift=DOWN * 0.2), run_time=0.7)
        
        # 说明文字
        explain = Text(
            "两条数轴互相垂直相交于原点",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain),
            FadeOut(quadrant_labels),
            run_time=0.6
        )
        
        # 保留坐标轴、原点、标签
        self.x_label = x_label
        self.y_label = y_label
        self.origin_label = origin_label
    
    def show_point_to_coordinate_part1(self):
        """场景3: 由点确定坐标（第一部分）(10-12秒)"""
        # 标题
        subtitle = Text(
            "由点确定坐标",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 点P出现
        dot_P = Dot(self.point_P, color=self.COLOR_SECONDARY, radius=0.12)
        label_P = Text("P", font="PingFang SC", font_size=24, color=WHITE).next_to(dot_P, UR, buff=0.15)
        
        self.play(FadeIn(dot_P, scale=0.5), run_time=0.4)
        self.play(Flash(dot_P, color=self.COLOR_SECONDARY, flash_radius=0.3), run_time=0.4)
        self.play(Write(label_P), run_time=0.4)
        
        # 步骤1: 作垂线到x轴
        step1 = Text(
            "步骤1: 作垂线到x轴",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step1), run_time=0.5)
        
        # 创建到x轴的垂线
        perp_to_x = self.create_perpendicular_to_x_axis(self.point_P, color=self.COLOR_HIGHLIGHT)
        
        self.play(Create(perp_to_x), run_time=0.7)
        
        # 高亮x轴上的读数
        x_value_dot = Dot(self.foot_Px, color=self.COLOR_HIGHLIGHT, radius=0.08)
        x_coord_label = MathTex("x = 3", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(self.foot_Px, DOWN, buff=0.3)
        
        self.play(
            FadeIn(x_value_dot, scale=0.5),
            run_time=0.3
        )
        self.play(Indicate(x_value_dot, scale_factor=1.5), run_time=0.5)
        self.play(FadeIn(x_coord_label, shift=UP * 0.2), run_time=0.5)
        
        # 步骤2: 作垂线到y轴
        step2 = Text(
            "步骤2: 作垂线到y轴",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Transform(step1, step2), run_time=0.5)
        
        # 创建到y轴的垂线
        perp_to_y = self.create_perpendicular_to_y_axis(self.point_P, color=self.COLOR_HIGHLIGHT)
        
        self.play(Create(perp_to_y), run_time=0.7)
        
        # 高亮y轴上的读数
        y_value_dot = Dot(self.foot_Py, color=self.COLOR_HIGHLIGHT, radius=0.08)
        y_coord_label = MathTex("y = 2", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(self.foot_Py, LEFT, buff=0.3)
        
        self.play(
            FadeIn(y_value_dot, scale=0.5),
            run_time=0.3
        )
        self.play(Indicate(y_value_dot, scale_factor=1.5), run_time=0.5)
        self.play(FadeIn(y_coord_label, shift=RIGHT * 0.2), run_time=0.5)
        
        # 合并坐标
        final_coord = MathTex("P(3, 2)", font_size=28, color=self.COLOR_PRIMARY).next_to(dot_P, UR, buff=0.2)
        
        self.play(
            FadeOut(x_coord_label),
            FadeOut(y_coord_label),
            Transform(label_P, final_coord),
            run_time=0.8
        )
        
        # 直角标记
        right_angle_1 = self.create_right_angle_mark(
            self.foot_Px,
            self.point_P - self.foot_Px,
            np.array([0.3, 0, 0])
        )
        
        right_angle_2 = self.create_right_angle_mark(
            self.foot_Py,
            self.point_P - self.foot_Py,
            np.array([0, 0.3, 0])
        )
        
        self.play(
            FadeIn(right_angle_1),
            FadeIn(right_angle_2),
            run_time=0.5
        )
        
        # 重点提示
        highlight = Text(
            "横坐标 x, 纵坐标 y",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(step1),
            FadeOut(highlight),
            FadeOut(perp_to_x),
            FadeOut(perp_to_y),
            FadeOut(x_value_dot),
            FadeOut(y_value_dot),
            FadeOut(right_angle_1),
            FadeOut(right_angle_2),
            run_time=0.6
        )
        
        # 保留点P和坐标标签
        self.dot_P = dot_P
        self.label_P = label_P
    
    def show_point_to_coordinate_more_examples(self):
        """场景4: 由点确定坐标（更多示例）(8-10秒)"""
        # 说明
        text = Text(
            "再看两个例子",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(text), run_time=0.5)
        
        # 点Q（第二象限）
        dot_Q = Dot(self.point_Q, color=self.COLOR_PRIMARY, radius=0.10)
        
        self.play(FadeIn(dot_Q, scale=0.5), run_time=0.5)
        
        # Q的垂线（快速同时）
        perp_Qx = self.create_perpendicular_to_x_axis(self.point_Q)
        perp_Qy = self.create_perpendicular_to_y_axis(self.point_Q)
        
        perp_Q_group = VGroup(perp_Qx, perp_Qy)
        
        self.play(Create(perp_Q_group), run_time=0.8)
        
        # Q坐标标注
        label_Q = MathTex("Q(-2, 1)", font_size=24, color=WHITE).next_to(dot_Q, UL, buff=0.15)
        
        self.play(FadeIn(label_Q, shift=DOWN * 0.2), run_time=0.5)
        
        # 点R（第四象限）
        dot_R = Dot(self.point_R, color=self.COLOR_PRIMARY, radius=0.10)
        
        self.play(FadeIn(dot_R, scale=0.5), run_time=0.5)
        
        # R的垂线（快速同时）
        perp_Rx = self.create_perpendicular_to_x_axis(self.point_R)
        perp_Ry = self.create_perpendicular_to_y_axis(self.point_R)
        
        perp_R_group = VGroup(perp_Rx, perp_Ry)
        
        self.play(Create(perp_R_group), run_time=0.8)
        
        # R坐标标注
        label_R = MathTex("R(2, -1.5)", font_size=24, color=WHITE).next_to(dot_R, DR, buff=0.15)
        
        self.play(FadeIn(label_R, shift=UP * 0.2), run_time=0.5)
        
        # 提示
        hint = Text(
            "注意: 负数表示方向相反",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        
        # 三点闪烁
        all_dots = VGroup(self.dot_P, dot_Q, dot_R)
        self.play(
            *[Indicate(dot, scale_factor=1.3) for dot in all_dots],
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(text),
            FadeOut(hint),
            FadeOut(perp_Q_group),
            FadeOut(perp_R_group),
            FadeOut(self.dot_P),
            FadeOut(self.label_P),
            FadeOut(dot_Q),
            FadeOut(label_Q),
            FadeOut(dot_R),
            FadeOut(label_R),
            run_time=0.6
        )
    
    def show_coordinate_to_point(self):
        """场景5: 由坐标确定点 (10-12秒)"""
        # 标题
        subtitle2 = Text(
            "由坐标确定点",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle2), run_time=0.5)
        
        # 显示坐标
        given_coord = MathTex("S(2.5, -2)", font_size=32, color=self.COLOR_PRIMARY).move_to(UP * 4.5)
        
        self.play(Write(given_coord), run_time=0.8)
        
        # 步骤1: 在x轴找到2.5
        step1 = Text(
            "步骤1: 在x轴找到 2.5",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step1), run_time=0.5)
        
        # x轴标记
        x_mark = Dot(self.foot_Sx, color=self.COLOR_HIGHLIGHT, radius=0.10)
        x_tick = MathTex("2.5", font_size=20, color=WHITE).next_to(self.foot_Sx, DOWN, buff=0.2)
        
        self.play(FadeIn(x_mark, scale=0.5), FadeIn(x_tick), run_time=0.5)
        self.play(Indicate(x_mark, scale_factor=1.5), run_time=0.4)
        
        # x轴垂线
        vertical_line = DashedLine(
            self.foot_Sx + UP * 0.2,
            self.foot_Sx + DOWN * 2.5,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(vertical_line), run_time=0.7)
        
        # 步骤2: 在y轴找到-2
        step2 = Text(
            "步骤2: 在y轴找到 -2",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Transform(step1, step2), run_time=0.5)
        
        # y轴标记
        y_mark = Dot(self.foot_Sy, color=self.COLOR_HIGHLIGHT, radius=0.10)
        y_tick = MathTex("-2", font_size=20, color=WHITE).next_to(self.foot_Sy, LEFT, buff=0.2)
        
        self.play(FadeIn(y_mark, scale=0.5), FadeIn(y_tick), run_time=0.5)
        self.play(Indicate(y_mark, scale_factor=1.5), run_time=0.4)
        
        # y轴垂线
        horizontal_line = DashedLine(
            self.foot_Sy + LEFT * 0.2,
            self.foot_Sy + RIGHT * 2.5,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(horizontal_line), run_time=0.7)
        
        # 交点闪烁
        self.play(Flash(self.point_S, color=self.COLOR_SECONDARY, flash_radius=0.4), run_time=0.6)
        
        # 点S出现
        dot_S = Dot(self.point_S, color=self.COLOR_SECONDARY, radius=0.12)
        label_S = Text("S", font="PingFang SC", font_size=24, color=WHITE).next_to(dot_S, UR, buff=0.15)
        
        self.play(FadeIn(dot_S, scale=0.5), run_time=0.5)
        self.play(Write(label_S), run_time=0.5)
        
        # 直角标记
        right_angle_x = self.create_right_angle_mark(
            self.foot_Sx,
            self.point_S - self.foot_Sx,
            np.array([0.3, 0, 0])
        )
        
        right_angle_y = self.create_right_angle_mark(
            self.foot_Sy,
            self.point_S - self.foot_Sy,
            np.array([0, -0.3, 0])
        )
        
        self.play(
            FadeIn(right_angle_x),
            FadeIn(right_angle_y),
            run_time=0.5
        )
        
        # 重点
        highlight = Text(
            "两条垂线的交点",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(subtitle2),
            FadeOut(step1),
            FadeOut(highlight),
            FadeOut(vertical_line),
            FadeOut(horizontal_line),
            FadeOut(right_angle_x),
            FadeOut(right_angle_y),
            FadeOut(x_mark),
            FadeOut(y_mark),
            FadeOut(x_tick),
            FadeOut(y_tick),
            FadeOut(dot_S),
            FadeOut(label_S),
            FadeOut(given_coord),
            run_time=0.6
        )
    
    def show_points_on_axes(self):
        """场景6: 坐标轴上的点（特殊情况）(8-10秒)"""
        # 标题
        subtitle3 = Text(
            "特殊位置: 坐标轴上的点",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle3), run_time=0.5)
        
        # x轴高亮
        x_axis_copy = self.axes.x_axis.copy().set_color(self.COLOR_HIGHLIGHT).set_stroke(width=4)
        
        self.play(FadeIn(x_axis_copy), run_time=0.5)
        
        # 点A出现
        dot_A = Dot(self.point_A, color=self.COLOR_SECONDARY, radius=0.10)
        label_A = MathTex("A(2, 0)", font_size=24, color=WHITE).next_to(dot_A, UP, buff=0.2)
        
        self.play(
            FadeIn(dot_A, scale=0.5),
            Write(label_A),
            run_time=0.8
        )
        
        # 说明1
        explain1 = Text(
            "x轴上的点: y = 0",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain1, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # x轴恢复
        self.play(FadeOut(x_axis_copy), run_time=0.3)
        
        # y轴高亮
        y_axis_copy = self.axes.y_axis.copy().set_color(self.COLOR_HIGHLIGHT).set_stroke(width=4)
        
        self.play(FadeIn(y_axis_copy), run_time=0.5)
        
        # 点B出现
        dot_B = Dot(self.point_B, color=self.COLOR_SECONDARY, radius=0.10)
        label_B = MathTex("B(0, -1)", font_size=24, color=WHITE).next_to(dot_B, LEFT, buff=0.2)
        
        self.play(
            FadeIn(dot_B, scale=0.5),
            Write(label_B),
            run_time=0.8
        )
        
        # 说明2
        explain2 = Text(
            "y轴上的点: x = 0",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(explain2, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # y轴恢复
        self.play(FadeOut(y_axis_copy), run_time=0.3)
        
        # 原点闪烁
        self.play(Indicate(self.origin_dot, scale_factor=2.0, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 原点说明
        explain3 = Text(
            "原点: O(0, 0)",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explain3, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle3),
            FadeOut(explain1),
            FadeOut(explain2),
            FadeOut(explain3),
            FadeOut(dot_A),
            FadeOut(label_A),
            FadeOut(dot_B),
            FadeOut(label_B),
            run_time=0.6
        )
    
    def show_summary_and_outro(self):
        """场景7: 总结与关注 (8-10秒)"""
        # 坐标系缩小淡化
        self.play(
            self.axes.animate.scale(0.5).fade(0.8),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.origin_dot),
            FadeOut(self.origin_label),
            run_time=0.8
        )
        
        # 总结标题
        summary_title = Text(
            "要点总结",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.5)
        
        # 要点列表
        point1 = Text(
            "• 点用有序数对 (x, y) 表示",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 3)
        
        point2 = Text(
            "• 由点确定坐标: 作垂线读数",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 2)
        
        point3 = Text(
            "• 由坐标确定点: 作垂线找交点",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 1)
        
        point4 = Text(
            "• 坐标轴上的点: 一个坐标为 0",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(ORIGIN)
        
        points = VGroup(point1, point2, point3, point4)
        
        for i, point in enumerate(points):
            self.play(FadeIn(point, shift=RIGHT * 0.5), run_time=0.4)
            if i < len(points) - 1:
                self.wait(0.3)
        
        # 装饰框
        decorative_box = SurroundingRectangle(
            points,
            color=self.COLOR_PRIMARY,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(Create(decorative_box), run_time=0.5)
        self.wait(1.0)
        
        # 作者信息放大
        self.play(
            self.author_info.animate.scale(1.8).move_to(UP * 1).set_color(WHITE),
            FadeOut(summary_title),
            FadeOut(points),
            FadeOut(decorative_box),
            FadeOut(self.axes),
            run_time=0.7
        )
        
        # 关注文字
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰动画 - 小点围绕
        decorations = VGroup(*[
            Dot(radius=0.08, color=self.COLOR_PRIMARY)
            .move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(dot, scale=0.5) for dot in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_info, follow_text, decorations)),
            run_time=1.0
        )


# ========== 运行命令 ==========
# manim -pql coordinate_system_basics.py CoordinateSystemBasics  # 快速预览
# manim -qh coordinate_system_basics.py CoordinateSystemBasics   # 高质量 1080p
# manim -qk coordinate_system_basics.py CoordinateSystemBasics   # 4K质量
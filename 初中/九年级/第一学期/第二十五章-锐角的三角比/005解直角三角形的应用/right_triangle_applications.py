"""
解直角三角形的应用 - Manim 教学动画
九年级数学 | 锐角的三角比 | 实际应用

内容: 仰角、俯角、坡度问题
目标观众: 九年级学生
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


class RightTriangleApplications(Scene):
    """
    解直角三角形应用场景
    
    场景顺序:
    1. 开场钩子
    2. 仰角问题 - 测量建筑物高度
    3. 俯角问题 - 山顶观察
    4. 仰角vs俯角对比
    5. 坡度问题 - 道路设计
    6. 实际应用示例
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"      # 红色
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色
        self.COLOR_AUXILIARY = GRAY_B         # 辅助线
        self.COLOR_BUILDING = "#95a5a6"       # 建筑物
        self.COLOR_GROUND = "#2c3e50"         # 地面
        self.COLOR_SLOPE = "#16a085"          # 斜坡
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 20
        self.FONT_FORMULA = 28
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_elevation_angle()
        self.scene_3_depression_angle()
        self.scene_4_comparison()
        self.scene_5_slope_problem()
        self.scene_6_applications()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # ===== 场景2: 仰角问题 =====
        self.observer = np.array([-3.0, -2.0, 0])
        self.horizontal_dist = 3.0
        self.elevation_angle = 45 * DEGREES
        self.building_base = self.observer + np.array([self.horizontal_dist, 0, 0])
        self.building_height = self.horizontal_dist * np.tan(self.elevation_angle)
        self.building_top = self.building_base + np.array([0, self.building_height, 0])
        
        # ===== 场景3: 俯角问题 =====
        self.peak = np.array([0, 2.5, 0])
        self.mountain_height = 2.5
        self.depression_angle = 30 * DEGREES
        self.horizontal_distance = self.mountain_height / np.tan(self.depression_angle)
        self.target = self.peak + np.array([self.horizontal_distance, -self.mountain_height, 0])
        
        # ===== 场景5: 坡度问题 =====
        self.slope_ratio = 1/5
        self.vertical_rise = 1.0
        self.horizontal_run = self.vertical_rise / self.slope_ratio
        self.slope_start = np.array([-2.5, -1.5, 0])
        self.slope_end = self.slope_start + np.array([self.horizontal_run, self.vertical_rise, 0])
        self.slope_angle = np.arctan(self.slope_ratio)
        
        print("✓ 几何数据初始化完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.2)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "如何测量高楼的高度?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text, run_time=0.8))
        
        # 建筑物剪影
        building_silhouette = Rectangle(
            width=1.0,
            height=3.5,
            fill_color=self.COLOR_BUILDING,
            fill_opacity=0.6,
            stroke_width=0
        ).move_to(UP * 0.5)
        
        # 问号
        question_mark = Text(
            "?",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).next_to(building_silhouette, RIGHT, buff=0.5)
        
        self.play(
            Create(building_silhouette),
            FadeIn(question_mark, scale=1.5),
            run_time=1.0
        )
        
        self.play(
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.4
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(building_silhouette),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def scene_2_elevation_angle(self):
        """场景2: 仰角问题 - 测量建筑物高度"""
        # 标题
        title = Text(
            "仰角 Elevation Angle",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        subtitle = Text(
            "向上看的角度",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 绘制地面
        ground = Line(
            LEFT * 4.5 + DOWN * 2,
            RIGHT * 4.5 + DOWN * 2,
            color=self.COLOR_GROUND,
            stroke_width=4
        )
        
        # 建筑物
        building = Rectangle(
            width=0.8,
            height=self.building_height,
            fill_color=self.COLOR_BUILDING,
            fill_opacity=0.7,
            stroke_color=WHITE,
            stroke_width=2
        )
        building.move_to(self.building_base + UP * self.building_height / 2)
        
        self.play(Create(ground), Create(building), run_time=1.0)
        
        # 观察者
        observer_dot = Dot(self.observer, color=self.COLOR_PRIMARY, radius=0.12)
        observer_icon = Text(
            "👤",
            font_size=30
        ).move_to(self.observer)
        
        self.play(FadeIn(observer_icon), run_time=0.4)
        
        # 水平参考线
        horizon_ref = self.observer + RIGHT * 1.0
        horizon_line = DashedLine(
            self.observer,
            horizon_ref,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(horizon_line), run_time=0.6)
        
        # 视线
        sight_line = Line(
            self.observer,
            self.building_top,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(Create(sight_line), run_time=0.8)
        
        # 仰角标记
        angle_arc = Angle.from_three_points(
            horizon_ref,
            self.observer,
            self.building_top,
            radius=0.5,
            color=self.COLOR_SECONDARY,
            other_angle=False
        )
        
        angle_label = MathTex(
            r"\alpha = 45^\circ",
            font_size=self.FONT_LABEL,
            color=self.COLOR_SECONDARY
        ).next_to(angle_arc, RIGHT, buff=0.2).shift(UP * 0.2)
        
        self.play(
            Create(angle_arc),
            Write(angle_label),
            run_time=0.8
        )
        
        # 标注距离
        distance_brace = BraceBetweenPoints(
            self.observer + DOWN * 0.3,
            self.building_base + DOWN * 0.3,
            direction=DOWN,
            color=WHITE
        )
        distance_label = Text(
            "30m",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=WHITE
        ).next_to(distance_brace, DOWN, buff=0.1)
        
        self.play(
            GrowFromCenter(distance_brace),
            FadeIn(distance_label),
            run_time=0.6
        )
        
        # 高亮三角形
        triangle = Polygon(
            self.observer,
            self.building_base,
            self.building_top,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=0,
            fill_opacity=0.2
        )
        
        self.play(FadeIn(triangle), run_time=0.5)
        
        # 公式推导
        formula_1 = MathTex(
            r"\tan \alpha = \frac{h}{30}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula_1), run_time=0.8)
        self.wait(0.5)
        
        formula_2 = MathTex(
            r"h = 30 \times \tan 45^\circ",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(TransformMatchingTex(formula_1, formula_2), run_time=0.8)
        self.wait(0.5)
        
        formula_3 = MathTex(
            r"h = 30 \times 1 = 30 \text{m}",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(TransformMatchingTex(formula_2, formula_3), run_time=0.8)
        
        # 高亮结果
        result_box = SurroundingRectangle(
            formula_3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2
        )
        
        self.play(Create(result_box), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(ground),
            FadeOut(building),
            FadeOut(observer_icon),
            FadeOut(horizon_line),
            FadeOut(sight_line),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(distance_brace),
            FadeOut(distance_label),
            FadeOut(triangle),
            FadeOut(formula_3),
            FadeOut(result_box),
            run_time=0.6
        )
    
    def scene_3_depression_angle(self):
        """场景3: 俯角问题 - 山顶观察"""
        # 标题
        title = Text(
            "俯角 Depression Angle",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        subtitle = Text(
            "向下看的角度",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 绘制山的轮廓（使用多边形近似）
        mountain_points = [
            LEFT * 4.5 + DOWN * 2,
            LEFT * 3.5 + DOWN * 1,
            LEFT * 2.0 + UP * 0.5,
            self.peak + LEFT * 0.8,
            self.peak,
            self.peak + RIGHT * 0.8,
            RIGHT * 2.0 + UP * 0.3,
            RIGHT * 4.5 + DOWN * 2,
        ]
        
        mountain = Polygon(
            *mountain_points,
            fill_color="#7f8c8d",
            fill_opacity=0.6,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        self.play(Create(mountain), run_time=1.0)
        
        # 山顶观察点
        peak_dot = Dot(self.peak, color=self.COLOR_PRIMARY, radius=0.12)
        peak_icon = Text(
            "👤",
            font_size=25
        ).move_to(self.peak + UP * 0.3)
        
        self.play(FadeIn(peak_dot), FadeIn(peak_icon), run_time=0.4)
        
        # 水平参考线
        horizon_ref = self.peak + RIGHT * 2.0
        horizon_line = DashedLine(
            self.peak,
            horizon_ref,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(horizon_line), run_time=0.6)
        
        # 地面目标
        target_dot = Dot(self.target, color=self.COLOR_HIGHLIGHT, radius=0.1)
        target_icon = Text(
            "🎯",
            font_size=25
        ).move_to(self.target + DOWN * 0.3)
        
        self.play(
            FadeIn(target_dot),
            FadeIn(target_icon),
            run_time=0.4
        )
        
        # 视线
        sight_line = Line(
            self.peak,
            self.target,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(Create(sight_line), run_time=0.8)
        
        # 俯角标记（注意：需要 other_angle=True）
        angle_arc = Angle.from_three_points(
            horizon_ref,
            self.peak,
            self.target,
            radius=0.5,
            color=self.COLOR_SECONDARY,
            other_angle=True  # 俯角向下，需要用另一侧的角
        )
        
        angle_label = MathTex(
            r"\beta = 30^\circ",
            font_size=self.FONT_LABEL,
            color=self.COLOR_SECONDARY
        ).next_to(angle_arc, RIGHT, buff=0.3).shift(DOWN * 0.2)
        
        self.play(
            Create(angle_arc),
            Write(angle_label),
            run_time=0.8
        )
        
        # 标注高度
        height_line = DashedLine(
            self.peak,
            self.peak + DOWN * self.mountain_height,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        height_label = Text(
            "100m",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=WHITE
        ).next_to(height_line, LEFT, buff=0.2)
        
        self.play(
            Create(height_line),
            FadeIn(height_label),
            run_time=0.6
        )
        
        # 高亮三角形
        triangle_bottom = np.array([self.target[0], self.peak[1], 0])
        triangle = Polygon(
            self.peak,
            triangle_bottom,
            self.target,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=0,
            fill_opacity=0.2
        )
        
        self.play(FadeIn(triangle), run_time=0.5)
        
        # 公式推导
        formula_1 = MathTex(
            r"\tan \beta = \frac{100}{d}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula_1), run_time=0.8)
        self.wait(0.5)
        
        formula_2 = MathTex(
            r"d = \frac{100}{\tan 30^\circ}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(TransformMatchingTex(formula_1, formula_2), run_time=0.8)
        self.wait(0.5)
        
        formula_3 = MathTex(
            r"d \approx 173 \text{m}",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(TransformMatchingTex(formula_2, formula_3), run_time=0.8)
        
        # 高亮结果
        result_box = SurroundingRectangle(
            formula_3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2
        )
        
        self.play(Create(result_box), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(mountain),
            FadeOut(peak_dot),
            FadeOut(peak_icon),
            FadeOut(horizon_line),
            FadeOut(target_dot),
            FadeOut(target_icon),
            FadeOut(sight_line),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(height_line),
            FadeOut(height_label),
            FadeOut(triangle),
            FadeOut(formula_3),
            FadeOut(result_box),
            run_time=0.6
        )
    
    def scene_4_comparison(self):
        """场景4: 仰角vs俯角对比"""
        # 标题
        title = Text(
            "仰角 vs 俯角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 分割线
        divider = Line(UP * 5, DOWN * 5, color=GRAY_B, stroke_width=2)
        self.play(Create(divider), run_time=0.4)
        
        # 左侧：仰角简图
        left_center = LEFT * 2
        
        # 简化的仰角图
        elev_observer = left_center + DOWN * 1.5
        elev_target = left_center + UP * 1.0 + RIGHT * 1.0
        elev_horizon = elev_observer + RIGHT * 1.5
        
        elev_horizon_line = DashedLine(
            elev_observer,
            elev_horizon,
            color=GRAY_B,
            dash_length=0.08
        )
        
        elev_sight = Line(
            elev_observer,
            elev_target,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        elev_angle = Angle.from_three_points(
            elev_horizon,
            elev_observer,
            elev_target,
            radius=0.3,
            color=self.COLOR_SECONDARY
        )
        
        elev_diagram = VGroup(elev_horizon_line, elev_sight, elev_angle)
        
        elev_label = Text(
            "仰角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(left_center + UP * 2.5)
        
        elev_desc = Text(
            "向上看",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        ).move_to(left_center + DOWN * 2.5)
        
        self.play(
            FadeIn(elev_diagram),
            Write(elev_label),
            FadeIn(elev_desc),
            run_time=0.8
        )
        
        # 右侧：俯角简图
        right_center = RIGHT * 2
        
        # 简化的俯角图
        depr_observer = right_center + UP * 1.0
        depr_target = right_center + DOWN * 1.5 + RIGHT * 1.0
        depr_horizon = depr_observer + RIGHT * 1.5
        
        depr_horizon_line = DashedLine(
            depr_observer,
            depr_horizon,
            color=GRAY_B,
            dash_length=0.08
        )
        
        depr_sight = Line(
            depr_observer,
            depr_target,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        depr_angle = Angle.from_three_points(
            depr_horizon,
            depr_observer,
            depr_target,
            radius=0.3,
            color=self.COLOR_SECONDARY,
            other_angle=True
        )
        
        depr_diagram = VGroup(depr_horizon_line, depr_sight, depr_angle)
        
        depr_label = Text(
            "俯角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(right_center + UP * 2.5)
        
        depr_desc = Text(
            "向下看",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        ).move_to(right_center + DOWN * 2.5)
        
        self.play(
            FadeIn(depr_diagram),
            Write(depr_label),
            FadeIn(depr_desc),
            run_time=0.8
        )
        
        # 共同点提示
        hint = Text(
            "都以水平线为基准",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(hint), run_time=0.6)
        
        # 高亮水平线
        self.play(
            elev_horizon_line.animate.set_color(self.COLOR_HIGHLIGHT),
            depr_horizon_line.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(divider),
            FadeOut(elev_diagram),
            FadeOut(elev_label),
            FadeOut(elev_desc),
            FadeOut(depr_diagram),
            FadeOut(depr_label),
            FadeOut(depr_desc),
            FadeOut(hint),
            run_time=0.6
        )
    
    def scene_5_slope_problem(self):
        """场景5: 坡度问题 - 道路设计"""
        # 标题
        title = Text(
            "坡度与坡角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SLOPE
        ).move_to(UP * 6)
        
        subtitle = Text(
            "道路/斜坡设计",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 地面
        ground = Line(
            LEFT * 4.5 + self.slope_start[1] * UP,
            RIGHT * 4.5 + self.slope_start[1] * UP,
            color=self.COLOR_GROUND,
            stroke_width=4
        )
        
        self.play(Create(ground), run_time=0.5)
        
        # 斜坡（带纹理效果）
        slope_main = Polygon(
            self.slope_start,
            np.array([self.slope_end[0], self.slope_start[1], 0]),
            self.slope_end,
            fill_color=self.COLOR_SLOPE,
            fill_opacity=0.7,
            stroke_color=WHITE,
            stroke_width=3
        )
        
        self.play(Create(slope_main), run_time=1.0)
        
        # 标记起点和终点
        start_dot = Dot(self.slope_start, color=WHITE, radius=0.08)
        end_dot = Dot(self.slope_end, color=WHITE, radius=0.08)
        
        start_label = Text("A", font="Noto Sans CJK SC", font_size=self.FONT_LABEL).next_to(start_dot, DL, buff=0.1)
        end_label = Text("B", font="Noto Sans CJK SC", font_size=self.FONT_LABEL).next_to(end_dot, UR, buff=0.1)
        
        self.play(
            FadeIn(start_dot),
            FadeIn(end_dot),
            Write(start_label),
            Write(end_label),
            run_time=0.6
        )
        
        # 辅助线形成直角三角形
        vertical_line = DashedLine(
            self.slope_end,
            np.array([self.slope_end[0], self.slope_start[1], 0]),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        horizontal_line = DashedLine(
            self.slope_start,
            np.array([self.slope_end[0], self.slope_start[1], 0]),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(
            Create(vertical_line),
            Create(horizontal_line),
            run_time=0.8
        )
        
        # 直角标记
        right_angle_corner = np.array([self.slope_end[0], self.slope_start[1], 0])
        right_angle_mark = RightAngle(
            Line(right_angle_corner, self.slope_start),
            Line(right_angle_corner, self.slope_end),
            length=0.2,
            color=YELLOW
        )
        
        self.play(Create(right_angle_mark), run_time=0.4)
        
        # 坡角标记
        angle_arc = Angle.from_three_points(
            np.array([self.slope_end[0], self.slope_start[1], 0]),
            self.slope_start,
            self.slope_end,
            radius=0.6,
            color=self.COLOR_SECONDARY
        )
        
        angle_label = MathTex(
            r"\alpha",
            font_size=self.FONT_LABEL,
            color=self.COLOR_SECONDARY
        ).next_to(angle_arc, RIGHT, buff=0.3)
        
        self.play(
            Create(angle_arc),
            Write(angle_label),
            run_time=0.6
        )
        
        # 标注尺寸
        height_brace = Brace(vertical_line, direction=RIGHT, color=WHITE)
        height_label = Text(
            "h=10m",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=WHITE
        ).next_to(height_brace, RIGHT, buff=0.1)
        
        distance_brace = Brace(horizontal_line, direction=DOWN, color=WHITE)
        distance_label = Text(
            "d=50m",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=WHITE
        ).next_to(distance_brace, DOWN, buff=0.1)
        
        self.play(
            GrowFromCenter(height_brace),
            FadeIn(height_label),
            GrowFromCenter(distance_brace),
            FadeIn(distance_label),
            run_time=0.8
        )
        
        # 坡度定义
        formula_1 = MathTex(
            r"i = \frac{h}{d}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(Write(formula_1), run_time=0.8)
        self.wait(0.5)
        
        # 计算坡度
        formula_2 = MathTex(
            r"i = \frac{10}{50} = \frac{1}{5}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(TransformMatchingTex(formula_1, formula_2), run_time=0.8)
        self.wait(0.5)
        
        # 坡度与坡角关系
        formula_3 = MathTex(
            r"i = \tan \alpha",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(Write(formula_3), run_time=0.8)
        self.wait(0.5)
        
        # 计算坡角
        slope_angle_deg = np.degrees(self.slope_angle)
        formula_4 = MathTex(
            rf"\alpha = \arctan\left(\frac{{1}}{{5}}\right) \approx {slope_angle_deg:.1f}^\circ",
            font_size=self.FONT_FORMULA - 2,
            color=WHITE
        ).move_to(DOWN * 7)
        
        self.play(Write(formula_4), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(ground),
            FadeOut(slope_main),
            FadeOut(start_dot),
            FadeOut(end_dot),
            FadeOut(start_label),
            FadeOut(end_label),
            FadeOut(vertical_line),
            FadeOut(horizontal_line),
            FadeOut(right_angle_mark),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(height_brace),
            FadeOut(height_label),
            FadeOut(distance_brace),
            FadeOut(distance_label),
            FadeOut(formula_2),
            FadeOut(formula_3),
            FadeOut(formula_4),
            run_time=0.6
        )
    
    def scene_6_applications(self):
        """场景6: 实际应用示例"""
        # 标题
        title = Text(
            "更多实际应用",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 三个应用场景
        # 场景1：测量树高
        tree_y = UP * 2
        tree_trunk = Rectangle(
            width=0.2,
            height=1.5,
            fill_color="#8B4513",
            fill_opacity=1,
            stroke_width=0
        ).move_to(tree_y + UP * 0.75)
        
        tree_crown = Circle(
            radius=0.6,
            fill_color="#228B22",
            fill_opacity=0.8,
            stroke_width=0
        ).move_to(tree_y + UP * 1.8)
        
        tree_scene = VGroup(tree_trunk, tree_crown)
        tree_label = Text(
            "测量树高",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(tree_scene, DOWN, buff=0.3)
        
        self.play(
            FadeIn(tree_scene, scale=0.8),
            Write(tree_label),
            run_time=0.8
        )
        
        # 场景2：桥梁设计
        bridge_y = ORIGIN
        bridge_deck = Rectangle(
            width=2.5,
            height=0.15,
            fill_color=GRAY_B,
            fill_opacity=1,
            stroke_width=1,
            stroke_color=WHITE
        ).move_to(bridge_y)
        
        support_left = Line(
            bridge_deck.get_left() + UP * 0.08,
            bridge_deck.get_left() + DOWN * 0.8,
            color=GRAY_A,
            stroke_width=3
        )
        
        support_right = Line(
            bridge_deck.get_right() + UP * 0.08,
            bridge_deck.get_right() + DOWN * 0.8,
            color=GRAY_A,
            stroke_width=3
        )
        
        bridge_scene = VGroup(bridge_deck, support_left, support_right)
        bridge_label = Text(
            "桥梁坡度",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(bridge_scene, DOWN, buff=0.5)
        
        self.play(
            FadeIn(bridge_scene, scale=0.8),
            Write(bridge_label),
            run_time=0.8
        )
        
        # 场景3：航海导航
        ship_y = DOWN * 2.5
        ship_body = Polygon(
            LEFT * 0.4 + DOWN * 0.2,
            LEFT * 0.5 + UP * 0.1,
            RIGHT * 0.5 + UP * 0.1,
            RIGHT * 0.4 + DOWN * 0.2,
            fill_color="#3498db",
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(ship_y)
        
        mast = Line(
            ship_y + UP * 0.1,
            ship_y + UP * 0.6,
            color=GRAY_A,
            stroke_width=2
        )
        
        sail = Polygon(
            ship_y + UP * 0.6,
            ship_y + UP * 0.2 + RIGHT * 0.3,
            ship_y + UP * 0.1,
            fill_color=WHITE,
            fill_opacity=0.7,
            stroke_width=0
        )
        
        ship_scene = VGroup(ship_body, mast, sail)
        ship_label = Text(
            "航海定位",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(ship_scene, DOWN, buff=0.3)
        
        self.play(
            FadeIn(ship_scene, scale=0.8),
            Write(ship_label),
            run_time=0.8
        )
        
        # 关键提示
        hint = Text(
            "关键：构造直角三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(Write(hint), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(tree_scene),
            FadeOut(tree_label),
            FadeOut(bridge_scene),
            FadeOut(bridge_label),
            FadeOut(ship_scene),
            FadeOut(ship_label),
            FadeOut(hint),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 总结与片尾"""
        # 标题
        title = Text(
            "三个关键概念",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 卡片1：仰角/俯角
        card1_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_SECONDARY,
            fill_opacity=1,
            stroke_width=0
        )
        
        card1_title = Text(
            "仰角/俯角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        card1_content = Text(
            "以水平线为基准的角度",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        )
        
        card1 = VGroup(card1_icon, card1_title, card1_content).arrange(RIGHT, buff=0.3)
        card1.move_to(UP * 3).shift(LEFT * 10)
        
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        
        # 卡片2：坡度公式
        card2_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_SLOPE,
            fill_opacity=1,
            stroke_width=0
        )
        
        card2_title = Text(
            "坡度公式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        card2_formula = MathTex(
            r"i = \frac{h}{d} = \tan \alpha",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        )
        
        card2 = VGroup(card2_icon, card2_title, card2_formula).arrange(RIGHT, buff=0.3)
        card2.move_to(UP * 1.5).shift(LEFT * 10)
        
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        
        # 卡片3：解题方法
        card3_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_HIGHLIGHT,
            fill_opacity=1,
            stroke_width=0
        )
        
        card3_title = Text(
            "解题方法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        card3_content = Text(
            "构造直角三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        )
        
        card3 = VGroup(card3_icon, card3_title, card3_content).arrange(RIGHT, buff=0.3)
        card3.move_to(ORIGIN).shift(LEFT * 10)
        
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=34,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 3.5)
        
        self.play(
            Transform(self.author_info, author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多解题技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 装饰动画（小三角形）
        triangles = VGroup(*[
            Polygon(
                ORIGIN,
                RIGHT * 0.25,
                UP * 0.25,
                color=GOLD,
                fill_opacity=0.8,
                stroke_width=0
            ).scale(0.5).move_to(
                follow_text.get_center() + 
                1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        
        self.play(Rotate(triangles, angle=PI / 2), run_time=1.0)
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )


# 运行命令示例:
# manim -pql right_triangle_applications.py RightTriangleApplications  # 快速预览
# manim -qh right_triangle_applications.py RightTriangleApplications   # 高质量 1080p
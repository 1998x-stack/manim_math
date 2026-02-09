"""
平面直角坐标系的概念 - Manim教学动画
Plane Rectangular Coordinate System - Educational Animation

年级: 七年级
知识点: 平面直角坐标系的概念
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景结构:
1. 开场钩子 (0-4s)
2. 数轴回顾 (4-10s)
3. 引入第二条数轴 (10-16s)
4. 标注原点 (16-20s)
5. 引入象限概念 (20-35s)
6. 示例点定位 (35-50s)
7. 总结 + 片尾 (50-75s)
"""

from manim import *
import numpy as np


# ========== 全局配置 ==========
# TikTok 竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CoordinateSystemConcept(Scene):
    """
    平面直角坐标系概念教学动画
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 定义颜色方案
        self.COLOR_X_AXIS = "#e74c3c"       # 红色 - x轴
        self.COLOR_Y_AXIS = "#3498db"       # 蓝色 - y轴
        self.COLOR_ORIGIN = "#f39c12"       # 橙色 - 原点
        self.COLOR_QUADRANT_I = "#2ecc71"   # 绿色 - 第一象限
        self.COLOR_QUADRANT_II = "#9b59b6"  # 紫色 - 第二象限
        self.COLOR_QUADRANT_III = "#e67e22" # 橙色 - 第三象限
        self.COLOR_QUADRANT_IV = "#1abc9c"  # 青色 - 第四象限
        self.COLOR_GRID = GRAY_B            # 灰色 - 网格
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_POINT = "#ff6b6b"        # 红色 - 示例点
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"  # 中文字体
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_number_line_review()
        self.scene_3_introduce_y_axis()
        self.scene_4_mark_origin()
        self.scene_5_introduce_quadrants()
        self.scene_6_demonstrate_points()
        self.scene_7_summary_and_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # ========== 基本参数 ==========
        self.origin = np.array([0, 0, 0])
        self.x_range = [-4, 4, 1]
        self.y_range = [-6, 6, 1]
        
        # ========== 示例点坐标 ==========
        self.point_A = np.array([2, 3, 0])    # 第一象限
        self.point_B = np.array([-3, 2, 0])   # 第二象限
        self.point_C = np.array([-2, -3, 0])  # 第三象限
        self.point_D = np.array([3, -2, 0])   # 第四象限
        
        # ========== 象限中心 ==========
        self.quad_I_center = np.array([2, 3, 0])
        self.quad_II_center = np.array([-2, 3, 0])
        self.quad_III_center = np.array([-2, -3, 0])
        self.quad_IV_center = np.array([2, -3, 0])
        
        print("✓ 几何数据初始化完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-4s)"""
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
            "如何在平面上\n精确定位一个点?",
            font=self.FONT_CHINESE,
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 随机闪烁的点
        random_dots = VGroup(*[
            Dot(
                np.array([
                    np.random.uniform(-3, 3),
                    np.random.uniform(-2, 2),
                    0
                ]),
                radius=0.08,
                color=self.COLOR_POINT
            )
            for _ in range(8)
        ])
        
        self.play(
            LaggedStart(*[
                Flash(dot, color=self.COLOR_POINT, flash_radius=0.2)
                for dot in random_dots
            ], lag_ratio=0.15),
            run_time=1.5
        )
        
        self.play(FadeIn(random_dots, scale=0.5), run_time=0.3)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(random_dots),
            run_time=0.5
        )
    
    def scene_2_number_line_review(self):
        """场景2: 数轴回顾 (4-10s)"""
        # 标题
        title = Text(
            "复习: 数轴",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 创建水平数轴 (x轴)
        # 使用 NumberLine 而不是完整的 Axes
        x_axis = NumberLine(
            x_range=self.x_range,
            length=8,
            include_numbers=True,
            include_ticks=True,
            tick_size=0.1,
            numbers_to_include=list(range(-4, 5)),
            font_size=24,
            color=self.COLOR_X_AXIS,
            stroke_width=3
        ).move_to(UP * 2)
        
        # 标注"横轴"
        x_label = Text(
            "横轴 (x轴)",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_X_AXIS
        ).next_to(x_axis, DOWN, buff=0.8)
        
        self.play(Create(x_axis), run_time=1.2)
        self.wait(0.3)
        self.play(FadeIn(x_label, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)
        
        # 清理标题，保留数轴
        self.play(FadeOut(title), run_time=0.4)
        
        # 将数轴移动到原点位置
        self.play(
            x_axis.animate.move_to(ORIGIN),
            x_label.animate.next_to(ORIGIN + RIGHT * 4.2, DR, buff=0.1),
            run_time=0.8
        )
        
        # 保存x轴引用
        self.x_axis = x_axis
        self.x_label = x_label
    
    def scene_3_introduce_y_axis(self):
        """场景3: 引入第二条数轴 (10-16s)"""
        # 说明文字
        explain = Text(
            "再加一条垂直的数轴",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain, shift=UP * 0.3), run_time=0.5)
        
        # 创建垂直数轴 (y轴)
        y_axis = NumberLine(
            x_range=self.y_range,
            length=12,
            include_numbers=True,
            include_ticks=True,
            tick_size=0.1,
            numbers_to_include=list(range(-6, 7)),
            font_size=24,
            color=self.COLOR_Y_AXIS,
            stroke_width=3
        ).rotate(90 * DEGREES).move_to(ORIGIN)
        
        # 标注"纵轴"
        y_label = Text(
            "纵轴 (y轴)",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_Y_AXIS
        ).next_to(ORIGIN + UP * 6.2, UR, buff=0.1)
        
        self.play(Create(y_axis), run_time=1.2)
        self.wait(0.3)
        self.play(FadeIn(y_label, shift=LEFT * 0.2), run_time=0.5)
        
        # 直角标记
        right_angle = self.create_right_angle_mark(
            corner=self.origin,
            point1=self.origin + RIGHT,
            point2=self.origin + UP,
            size=0.3
        )
        
        self.play(Create(right_angle), run_time=0.5)
        
        # 强调垂直
        emphasize_text = Text(
            "互相垂直!",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(
            Indicate(right_angle, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            FadeIn(emphasize_text),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(explain),
            FadeOut(emphasize_text),
            FadeOut(right_angle),
            run_time=0.5
        )
        
        # 保存y轴引用
        self.y_axis = y_axis
        self.y_label = y_label
    
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
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2,
            fill_opacity=0
        )
        return square
    
    def scene_4_mark_origin(self):
        """场景4: 标注原点 (16-20s)"""
        # 原点闪烁
        origin_dot = Dot(self.origin, radius=0.12, color=self.COLOR_ORIGIN)
        
        self.play(
            Flash(origin_dot, color=self.COLOR_ORIGIN, flash_radius=0.4, num_lines=12),
            run_time=0.5
        )
        
        self.play(FadeIn(origin_dot, scale=0.5), run_time=0.5)
        
        # 标签 O
        origin_label = Text(
            "O",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_ORIGIN,
            weight=BOLD
        ).next_to(origin_dot, DL, buff=0.15)
        
        self.play(Write(origin_label), run_time=0.5)
        
        # 定义文字
        definition = Text(
            "原点 - 两轴的交点",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理定义文字
        self.play(FadeOut(definition), run_time=0.4)
        
        # 保存原点引用
        self.origin_dot = origin_dot
        self.origin_label = origin_label
    
    def scene_5_introduce_quadrants(self):
        """场景5: 引入象限概念 (20-35s)"""
        # 标题
        title = Text(
            "四个象限",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # ===== 第一象限 =====
        quad_I_bg = Polygon(
            self.origin,
            self.origin + RIGHT * 4,
            self.origin + RIGHT * 4 + UP * 6,
            self.origin + UP * 6,
            color=self.COLOR_QUADRANT_I,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        quad_I_label = Text(
            "Ⅰ",
            font=self.FONT_CHINESE,
            font_size=48,
            color=self.COLOR_QUADRANT_I,
            weight=BOLD
        ).move_to(self.quad_I_center)
        
        quad_I_sign = Text(
            "(+, +)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_QUADRANT_I
        ).next_to(quad_I_label, DOWN, buff=0.2)
        
        self.play(FadeIn(quad_I_bg), run_time=0.5)
        self.play(Write(quad_I_label), run_time=0.5)
        self.play(FadeIn(quad_I_sign, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # ===== 第二象限 =====
        quad_II_bg = Polygon(
            self.origin,
            self.origin + LEFT * 4,
            self.origin + LEFT * 4 + UP * 6,
            self.origin + UP * 6,
            color=self.COLOR_QUADRANT_II,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        quad_II_label = Text(
            "Ⅱ",
            font=self.FONT_CHINESE,
            font_size=48,
            color=self.COLOR_QUADRANT_II,
            weight=BOLD
        ).move_to(self.quad_II_center)
        
        quad_II_sign = Text(
            "(-, +)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_QUADRANT_II
        ).next_to(quad_II_label, DOWN, buff=0.2)
        
        self.play(FadeIn(quad_II_bg), run_time=0.5)
        self.play(Write(quad_II_label), run_time=0.5)
        self.play(FadeIn(quad_II_sign, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # ===== 第三象限 =====
        quad_III_bg = Polygon(
            self.origin,
            self.origin + LEFT * 4,
            self.origin + LEFT * 4 + DOWN * 6,
            self.origin + DOWN * 6,
            color=self.COLOR_QUADRANT_III,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        quad_III_label = Text(
            "Ⅲ",
            font=self.FONT_CHINESE,
            font_size=48,
            color=self.COLOR_QUADRANT_III,
            weight=BOLD
        ).move_to(self.quad_III_center)
        
        quad_III_sign = Text(
            "(-, -)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_QUADRANT_III
        ).next_to(quad_III_label, UP, buff=0.2)
        
        self.play(FadeIn(quad_III_bg), run_time=0.5)
        self.play(Write(quad_III_label), run_time=0.5)
        self.play(FadeIn(quad_III_sign, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # ===== 第四象限 =====
        quad_IV_bg = Polygon(
            self.origin,
            self.origin + RIGHT * 4,
            self.origin + RIGHT * 4 + DOWN * 6,
            self.origin + DOWN * 6,
            color=self.COLOR_QUADRANT_IV,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        quad_IV_label = Text(
            "Ⅳ",
            font=self.FONT_CHINESE,
            font_size=48,
            color=self.COLOR_QUADRANT_IV,
            weight=BOLD
        ).move_to(self.quad_IV_center)
        
        quad_IV_sign = Text(
            "(+, -)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_QUADRANT_IV
        ).next_to(quad_IV_label, UP, buff=0.2)
        
        self.play(FadeIn(quad_IV_bg), run_time=0.5)
        self.play(Write(quad_IV_label), run_time=0.5)
        self.play(FadeIn(quad_IV_sign, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 说明文字
        explain = Text(
            "按逆时针方向命名",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.5)
        
        # 逆时针箭头路径
        arrow_points = [
            self.quad_I_center,
            self.quad_II_center,
            self.quad_III_center,
            self.quad_IV_center,
            self.quad_I_center
        ]
        
        arrow_path = VGroup()
        for i in range(len(arrow_points) - 1):
            arrow = CurvedArrow(
                arrow_points[i],
                arrow_points[i + 1],
                color=self.COLOR_HIGHLIGHT,
                stroke_width=3,
                tip_length=0.2
            )
            arrow_path.add(arrow)
        
        self.play(Create(arrow_path), run_time=2.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain),
            FadeOut(arrow_path),
            FadeOut(quad_I_bg),
            FadeOut(quad_II_bg),
            FadeOut(quad_III_bg),
            FadeOut(quad_IV_bg),
            run_time=0.6
        )
        
        # 保存象限标签引用
        self.quad_labels = VGroup(
            quad_I_label, quad_I_sign,
            quad_II_label, quad_II_sign,
            quad_III_label, quad_III_sign,
            quad_IV_label, quad_IV_sign
        )
    
    def scene_6_demonstrate_points(self):
        """场景6: 示例点定位 (35-50s)"""
        # 说明文字
        explain = Text(
            "用有序数对表示点的位置",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # ===== 点A (第一象限) =====
        dot_A = Dot(self.point_A, radius=0.1, color=self.COLOR_POINT)
        label_A = Text(
            "A(2, 3)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_POINT
        ).next_to(dot_A, UR, buff=0.1)
        
        self.play(FadeIn(dot_A, scale=0.5), run_time=0.4)
        self.play(Write(label_A), run_time=0.5)
        
        # 坐标辅助线
        dash_x_A = DashedLine(
            self.point_A,
            np.array([self.point_A[0], 0, 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        dash_y_A = DashedLine(
            self.point_A,
            np.array([0, self.point_A[1], 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        
        self.play(Create(dash_x_A), Create(dash_y_A), run_time=0.6)
        self.wait(0.5)
        
        # ===== 点B (第二象限) =====
        dot_B = Dot(self.point_B, radius=0.1, color=self.COLOR_POINT)
        label_B = Text(
            "B(-3, 2)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_POINT
        ).next_to(dot_B, UL, buff=0.1)
        
        self.play(FadeIn(dot_B, scale=0.5), run_time=0.4)
        self.play(Write(label_B), run_time=0.5)
        
        dash_x_B = DashedLine(
            self.point_B,
            np.array([self.point_B[0], 0, 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        dash_y_B = DashedLine(
            self.point_B,
            np.array([0, self.point_B[1], 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        
        self.play(Create(dash_x_B), Create(dash_y_B), run_time=0.6)
        self.wait(0.5)
        
        # ===== 点C (第三象限) =====
        dot_C = Dot(self.point_C, radius=0.1, color=self.COLOR_POINT)
        label_C = Text(
            "C(-2, -3)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_POINT
        ).next_to(dot_C, DL, buff=0.1)
        
        self.play(FadeIn(dot_C, scale=0.5), run_time=0.4)
        self.play(Write(label_C), run_time=0.5)
        
        dash_x_C = DashedLine(
            self.point_C,
            np.array([self.point_C[0], 0, 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        dash_y_C = DashedLine(
            self.point_C,
            np.array([0, self.point_C[1], 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        
        self.play(Create(dash_x_C), Create(dash_y_C), run_time=0.6)
        self.wait(0.5)
        
        # ===== 点D (第四象限) =====
        dot_D = Dot(self.point_D, radius=0.1, color=self.COLOR_POINT)
        label_D = Text(
            "D(3, -2)",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_POINT
        ).next_to(dot_D, DR, buff=0.1)
        
        self.play(FadeIn(dot_D, scale=0.5), run_time=0.4)
        self.play(Write(label_D), run_time=0.5)
        
        dash_x_D = DashedLine(
            self.point_D,
            np.array([self.point_D[0], 0, 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        dash_y_D = DashedLine(
            self.point_D,
            np.array([0, self.point_D[1], 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        
        self.play(Create(dash_x_D), Create(dash_y_D), run_time=0.6)
        self.wait(0.5)
        
        # 强调所有点
        all_dots = VGroup(dot_A, dot_B, dot_C, dot_D)
        self.play(
            Indicate(all_dots, scale_factor=1.2, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        self.wait(1.5)
        
        # 清理辅助线和说明
        self.play(
            FadeOut(explain),
            FadeOut(VGroup(dash_x_A, dash_y_A, dash_x_B, dash_y_B, 
                          dash_x_C, dash_y_C, dash_x_D, dash_y_D)),
            run_time=0.5
        )
        
        # 保存点的引用
        self.demo_points = VGroup(dot_A, dot_B, dot_C, dot_D)
        self.demo_labels = VGroup(label_A, label_B, label_C, label_D)
    
    def scene_7_summary_and_outro(self):
        """场景7: 总结 + 片尾 (50-75s)"""
        # 简化场景
        self.play(
            FadeOut(self.demo_points),
            FadeOut(self.demo_labels),
            FadeOut(self.quad_labels),
            run_time=0.6
        )
        
        # 标题
        summary_title = Text(
            "平面直角坐标系",
            font=self.FONT_CHINESE,
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 关键概念卡片
        cards = VGroup()
        
        # 卡片1: x轴
        card_1 = self.create_concept_card(
            "x轴",
            "横轴 (水平)",
            self.COLOR_X_AXIS,
            UP * 2.5
        )
        cards.add(card_1)
        
        # 卡片2: y轴
        card_2 = self.create_concept_card(
            "y轴",
            "纵轴 (垂直)",
            self.COLOR_Y_AXIS,
            UP * 1.2
        )
        cards.add(card_2)
        
        # 卡片3: 原点
        card_3 = self.create_concept_card(
            "原点 O",
            "两轴交点 (0, 0)",
            self.COLOR_ORIGIN,
            DOWN * 0.1
        )
        cards.add(card_3)
        
        # 卡片4: 象限
        card_4 = self.create_concept_card(
            "四象限",
            "Ⅰ(+,+) Ⅱ(-,+) Ⅲ(-,-) Ⅳ(+,-)",
            self.COLOR_HIGHLIGHT,
            DOWN * 1.4,
            font_size_content=18
        )
        cards.add(card_4)
        
        # 卡片依次出现
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.5)
        
        # 缩小坐标系
        axes_group = VGroup(self.x_axis, self.y_axis, self.origin_dot, 
                           self.origin_label, self.x_label, self.y_label)
        
        self.play(
            axes_group.animate.scale(0.4).move_to(UP * 3.5),
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=1.0
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 0.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_B
        ).next_to(author_name, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学知识!",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 四个小坐标系图标
        icons = VGroup()
        for angle, color in zip([0, 90, 180, 270], 
                               [self.COLOR_QUADRANT_I, self.COLOR_QUADRANT_II,
                                self.COLOR_QUADRANT_III, self.COLOR_QUADRANT_IV]):
            icon = VGroup(
                Line(ORIGIN, RIGHT * 0.3, color=color, stroke_width=2),
                Line(ORIGIN, UP * 0.3, color=color, stroke_width=2)
            ).rotate(angle * DEGREES)
            icons.add(icon)
        
        icons.arrange_in_grid(rows=1, cols=4, buff=0.8).move_to(DOWN * 3)
        
        self.play(
            LaggedStart(*[FadeIn(icon, scale=0.5) for icon in icons], 
                       lag_ratio=0.2),
            run_time=0.8
        )
        
        self.wait(2.5)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        
        self.wait(0.5)
    
    def create_concept_card(self, title, content, color, position, 
                           font_size_content=20):
        """创建概念卡片"""
        # 图标圆
        icon = Circle(
            radius=0.15,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title_text = Text(
            title,
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE,
            weight=BOLD
        )
        
        # 内容
        content_text = Text(
            content,
            font=self.FONT_CHINESE,
            font_size=font_size_content,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 添加背景矩形
        bg_rect = SurroundingRectangle(
            card,
            color=color,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=2,
            fill_opacity=0.05,
            fill_color=color
        )
        
        return VGroup(bg_rect, card)


# 运行命令:
# manim -pql coordinate_system_concept.py CoordinateSystemConcept  # 快速预览
# manim -qh coordinate_system_concept.py CoordinateSystemConcept   # 高质量
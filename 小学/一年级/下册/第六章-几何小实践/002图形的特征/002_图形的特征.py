"""
图形的特征 - Shape Features Animation
小学一年级下册 第六章 几何小实践
内容：长方形、正方形、三角形、圆的特征
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


class ShapeFeatureLesson(Scene):
    """
    图形的特征教学动画

    场景顺序:
    1. 开场钩子 - 你认识这些图形吗?
    2. 长方形特征 - 对边相等，四个直角
    3. 正方形特征 - 四边相等，四个直角
    4. 三角形特征 - 三条边，三个角
    5. 圆的特征 - 曲线围成，没有角
    6. 汇总对比
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_RECT = "#3498db"       # 蓝色 - 长方形
        self.COLOR_SQ = "#2ecc71"         # 绿色 - 正方形
        self.COLOR_TRI = "#f39c12"        # 橙色 - 三角形
        self.COLOR_CIR = "#e74c3c"        # 红色 - 圆
        self.COLOR_HIGHLIGHT = "#f1c40f"  # 黄色 - 高亮
        self.COLOR_ANGLE = "#9b59b6"      # 紫色 - 角标记
        self.COLOR_SIDE = "#1abc9c"       # 青色 - 边标记

        # 统一初始化几何数据
        self.setup_geometry()

        # 作者信息（始终显示）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Heiti SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author_info)

        # 执行场景
        self.scene_1_opening()
        self.scene_2_rectangle()
        self.scene_3_square()
        self.scene_4_triangle()
        self.scene_5_circle()
        self.scene_6_summary()
        self.scene_7_outro()

    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ===== 长方形顶点 =====
        self.RECT_W = 2.8
        self.RECT_H = 1.8
        half_w = self.RECT_W / 2
        half_h = self.RECT_H / 2
        self.RECT_CENTER = np.array([0.0, 1.5, 0.0])
        self.R_TL = self.RECT_CENTER + np.array([-half_w,  half_h, 0.0])
        self.R_TR = self.RECT_CENTER + np.array([ half_w,  half_h, 0.0])
        self.R_BR = self.RECT_CENTER + np.array([ half_w, -half_h, 0.0])
        self.R_BL = self.RECT_CENTER + np.array([-half_w, -half_h, 0.0])

        # ===== 正方形顶点 =====
        self.SQ_SIDE = 2.2
        half_s = self.SQ_SIDE / 2
        self.SQ_CENTER = np.array([0.0, 1.5, 0.0])
        self.S_TL = self.SQ_CENTER + np.array([-half_s,  half_s, 0.0])
        self.S_TR = self.SQ_CENTER + np.array([ half_s,  half_s, 0.0])
        self.S_BR = self.SQ_CENTER + np.array([ half_s, -half_s, 0.0])
        self.S_BL = self.SQ_CENTER + np.array([-half_s, -half_s, 0.0])

        # ===== 三角形顶点 =====
        self.TRI_CENTER = np.array([0.0, 1.5, 0.0])
        self.T_A = self.TRI_CENTER + np.array([ 0.0,  2.0, 0.0])   # 顶点
        self.T_B = self.TRI_CENTER + np.array([-2.2, -1.0, 0.0])   # 左下
        self.T_C = self.TRI_CENTER + np.array([ 2.2, -1.0, 0.0])   # 右下

        # 验证几何
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何计算正确性"""
        eps = 1e-6
        # 验证长方形对边相等
        top    = np.linalg.norm(self.R_TR - self.R_TL)
        bottom = np.linalg.norm(self.R_BR - self.R_BL)
        left   = np.linalg.norm(self.R_TL - self.R_BL)
        right  = np.linalg.norm(self.R_TR - self.R_BR)
        assert abs(top - bottom) < eps, "长方形上下边不等"
        assert abs(left - right) < eps, "长方形左右边不等"
        assert abs(top   - self.RECT_W) < eps, "长方形宽度计算错误"
        assert abs(left  - self.RECT_H) < eps, "长方形高度计算错误"

        # 验证正方形四边相等
        s1 = np.linalg.norm(self.S_TR - self.S_TL)
        s2 = np.linalg.norm(self.S_BR - self.S_TR)
        s3 = np.linalg.norm(self.S_BL - self.S_BR)
        s4 = np.linalg.norm(self.S_TL - self.S_BL)
        assert abs(s1 - s2) < eps, "正方形边不等"
        assert abs(s2 - s3) < eps, "正方形边不等"
        assert abs(s3 - s4) < eps, "正方形边不等"
        print("✓ 几何验证通过")

    def make_right_angle_mark(self, corner, p1, p2, size=0.22, color=WHITE):
        """在 corner 处创建直角标记，p1 和 p2 是两条边方向上的点"""
        v1 = (p1 - corner)
        norm1 = np.linalg.norm(v1)
        if norm1 < 1e-9:
            return VGroup()
        v1 = v1 / norm1 * size

        v2 = (p2 - corner)
        norm2 = np.linalg.norm(v2)
        if norm2 < 1e-9:
            return VGroup()
        v2 = v2 / norm2 * size

        sq = Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=2.0,
            fill_opacity=0
        )
        return sq

    # =========================================================
    # 场景 1 - 开场
    # =========================================================
    def scene_1_opening(self):
        """开场：吸引注意力"""
        title = Text(
            "你认识这些图形吗?",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.9)

        # 四个图形
        rect_demo = Rectangle(
            width=1.6, height=1.0,
            color=self.COLOR_RECT,
            stroke_width=4,
            fill_opacity=0.15,
            fill_color=self.COLOR_RECT
        ).move_to(np.array([-2.2, 2.0, 0]))

        sq_demo = Square(
            side_length=1.2,
            color=self.COLOR_SQ,
            stroke_width=4,
            fill_opacity=0.15,
            fill_color=self.COLOR_SQ
        ).move_to(np.array([2.2, 2.0, 0]))

        tri_center = np.array([-2.2, -0.2, 0])
        tri_demo = Polygon(
            tri_center + np.array([0.0,  0.65, 0]),
            tri_center + np.array([-0.9, -0.45, 0]),
            tri_center + np.array([0.9, -0.45, 0]),
            color=self.COLOR_TRI,
            stroke_width=4,
            fill_opacity=0.15,
            fill_color=self.COLOR_TRI
        )

        circle_demo = Circle(
            radius=0.65,
            color=self.COLOR_CIR,
            stroke_width=4,
            fill_opacity=0.15,
            fill_color=self.COLOR_CIR
        ).move_to(np.array([2.2, -0.2, 0]))

        lbl_rect = Text("长方形", font="Heiti SC", font_size=22, color=self.COLOR_RECT).next_to(rect_demo, DOWN, buff=0.15)
        lbl_sq   = Text("正方形", font="Heiti SC", font_size=22, color=self.COLOR_SQ  ).next_to(sq_demo,   DOWN, buff=0.15)
        lbl_tri  = Text("三角形", font="Heiti SC", font_size=22, color=self.COLOR_TRI ).next_to(tri_demo,  DOWN, buff=0.15)
        lbl_cir  = Text("圆",     font="Heiti SC", font_size=22, color=self.COLOR_CIR ).next_to(circle_demo, DOWN, buff=0.15)

        shapes = VGroup(rect_demo, sq_demo, tri_demo, circle_demo)
        labels = VGroup(lbl_rect, lbl_sq, lbl_tri, lbl_cir)

        self.play(
            LaggedStart(
                GrowFromCenter(rect_demo),
                GrowFromCenter(sq_demo),
                GrowFromCenter(tri_demo),
                GrowFromCenter(circle_demo),
                lag_ratio=0.2
            ),
            run_time=1.2
        )
        self.play(
            LaggedStart(
                FadeIn(lbl_rect, shift=UP * 0.2),
                FadeIn(lbl_sq,   shift=UP * 0.2),
                FadeIn(lbl_tri,  shift=UP * 0.2),
                FadeIn(lbl_cir,  shift=UP * 0.2),
                lag_ratio=0.2
            ),
            run_time=0.8
        )
        self.wait(0.8)

        subtitle = Text(
            "今天我们来认识它们的特征!",
            font="Heiti SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 2.0)

        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(shapes),
            FadeOut(labels),
            FadeOut(subtitle),
            run_time=0.5
        )

    # =========================================================
    # 场景 2 - 长方形
    # =========================================================
    def scene_2_rectangle(self):
        """长方形特征：对边相等，四个直角"""
        title = Text(
            "长方形",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_RECT
        ).move_to(UP * 5.8)

        self.play(Write(title), run_time=0.6)

        rect = Polygon(
            self.R_TL, self.R_TR, self.R_BR, self.R_BL,
            color=self.COLOR_RECT,
            stroke_width=5,
            fill_opacity=0.12,
            fill_color=self.COLOR_RECT
        )
        self.play(Create(rect), run_time=1.0)
        self.wait(0.3)

        # ---- 特征1：对边相等 ----
        feat1_title = Text(
            "特征一：对边相等",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)

        self.play(FadeIn(feat1_title, shift=UP * 0.2), run_time=0.5)

        # 高亮上边和下边
        top_line = Line(self.R_TL, self.R_TR, color=self.COLOR_HIGHLIGHT, stroke_width=7)
        bot_line = Line(self.R_BL, self.R_BR, color=self.COLOR_HIGHLIGHT, stroke_width=7)
        self.play(Create(top_line), Create(bot_line), run_time=0.6)

        top_brace = BraceBetweenPoints(self.R_TL, self.R_TR, direction=UP)
        bot_brace = BraceBetweenPoints(self.R_BL, self.R_BR, direction=DOWN)
        top_lbl = Text("上边", font="Heiti SC", font_size=20, color=WHITE)
        top_lbl.next_to(top_brace, UP, buff=0.08)
        bot_lbl = Text("下边", font="Heiti SC", font_size=20, color=WHITE)
        bot_lbl.next_to(bot_brace, DOWN, buff=0.08)

        self.play(
            FadeIn(top_brace), FadeIn(bot_brace),
            FadeIn(top_lbl),   FadeIn(bot_lbl),
            run_time=0.7
        )

        equal_hint1 = Text(
            "上边 = 下边",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_SIDE
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(equal_hint1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # 高亮左边和右边
        left_line  = Line(self.R_TL, self.R_BL, color="#e74c3c", stroke_width=7)
        right_line = Line(self.R_TR, self.R_BR, color="#e74c3c", stroke_width=7)
        self.play(
            FadeOut(top_line), FadeOut(bot_line),
            FadeOut(top_brace), FadeOut(bot_brace),
            FadeOut(top_lbl),  FadeOut(bot_lbl),
            run_time=0.3
        )
        self.play(Create(left_line), Create(right_line), run_time=0.6)

        left_brace  = BraceBetweenPoints(self.R_BL, self.R_TL, direction=LEFT)
        right_brace = BraceBetweenPoints(self.R_TR, self.R_BR, direction=RIGHT)
        left_lbl = Text("左边", font="Heiti SC", font_size=20, color=WHITE)
        left_lbl.next_to(left_brace, LEFT, buff=0.08)
        right_lbl = Text("右边", font="Heiti SC", font_size=20, color=WHITE)
        right_lbl.next_to(right_brace, RIGHT, buff=0.08)
        self.play(
            FadeIn(left_brace), FadeIn(right_brace),
            FadeIn(left_lbl),   FadeIn(right_lbl),
            run_time=0.7
        )

        equal_hint2 = Text(
            "左边 = 右边",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_SIDE
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(equal_hint2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        self.play(
            FadeOut(left_line), FadeOut(right_line),
            FadeOut(left_brace), FadeOut(right_brace),
            FadeOut(left_lbl),   FadeOut(right_lbl),
            FadeOut(equal_hint1), FadeOut(equal_hint2),
            FadeOut(feat1_title),
            run_time=0.4
        )

        # ---- 特征2：四个直角 ----
        feat2_title = Text(
            "特征二：四个角都是直角",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat2_title, shift=UP * 0.2), run_time=0.5)

        corners = [
            (self.R_TL, self.R_TR, self.R_BL),
            (self.R_TR, self.R_BR, self.R_TL),
            (self.R_BR, self.R_BL, self.R_TR),
            (self.R_BL, self.R_TL, self.R_BR),
        ]
        angle_marks = VGroup()
        for corner, p1, p2 in corners:
            mark = self.make_right_angle_mark(corner, p1, p2, size=0.25, color=self.COLOR_ANGLE)
            angle_marks.add(mark)

        self.play(
            LaggedStart(*[Create(m) for m in angle_marks], lag_ratio=0.3),
            run_time=1.0
        )

        angle_count = Text(
            "4个直角",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ANGLE
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(angle_count, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        summary_rect = Text(
            "长方形：对边相等，四个直角",
            font="Heiti SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(summary_rect, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(rect),
            FadeOut(feat2_title), FadeOut(angle_marks),
            FadeOut(angle_count), FadeOut(summary_rect),
            run_time=0.5
        )

    # =========================================================
    # 场景 3 - 正方形
    # =========================================================
    def scene_3_square(self):
        """正方形特征：四边相等，四个直角"""
        title = Text(
            "正方形",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_SQ
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        sq = Polygon(
            self.S_TL, self.S_TR, self.S_BR, self.S_BL,
            color=self.COLOR_SQ,
            stroke_width=5,
            fill_opacity=0.12,
            fill_color=self.COLOR_SQ
        )
        self.play(Create(sq), run_time=0.9)
        self.wait(0.3)

        # ---- 特征1：四边都相等 ----
        feat1_title = Text(
            "特征一：四条边都相等",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat1_title, shift=UP * 0.2), run_time=0.5)

        side_lines = VGroup(
            Line(self.S_TL, self.S_TR, color=self.COLOR_HIGHLIGHT, stroke_width=7),
            Line(self.S_TR, self.S_BR, color=self.COLOR_HIGHLIGHT, stroke_width=7),
            Line(self.S_BR, self.S_BL, color=self.COLOR_HIGHLIGHT, stroke_width=7),
            Line(self.S_BL, self.S_TL, color=self.COLOR_HIGHLIGHT, stroke_width=7),
        )
        self.play(
            LaggedStart(*[Create(s) for s in side_lines], lag_ratio=0.3),
            run_time=1.0
        )

        # 等长刻度线
        tick_marks = VGroup()
        side_pairs = [
            (self.S_TL, self.S_TR),
            (self.S_TR, self.S_BR),
            (self.S_BR, self.S_BL),
            (self.S_BL, self.S_TL),
        ]
        for p1, p2 in side_pairs:
            mid = (p1 + p2) / 2
            dir_vec = p2 - p1
            perp = np.array([-dir_vec[1], dir_vec[0], 0])
            perp_unit = perp / np.linalg.norm(perp)
            tick = Line(
                mid - perp_unit * 0.15,
                mid + perp_unit * 0.15,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=4
            )
            tick_marks.add(tick)

        self.play(Create(tick_marks), run_time=0.5)

        equal_all = Text(
            "四条边都相等!",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_SIDE
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(equal_all, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(side_lines), FadeOut(tick_marks),
            FadeOut(equal_all), FadeOut(feat1_title),
            run_time=0.4
        )

        # ---- 特征2：四个直角 ----
        feat2_title = Text(
            "特征二：四个角都是直角",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat2_title, shift=UP * 0.2), run_time=0.5)

        corners_sq = [
            (self.S_TL, self.S_TR, self.S_BL),
            (self.S_TR, self.S_BR, self.S_TL),
            (self.S_BR, self.S_BL, self.S_TR),
            (self.S_BL, self.S_TL, self.S_BR),
        ]
        sq_angle_marks = VGroup()
        for corner, p1, p2 in corners_sq:
            mark = self.make_right_angle_mark(corner, p1, p2, size=0.25, color=self.COLOR_ANGLE)
            sq_angle_marks.add(mark)

        self.play(
            LaggedStart(*[Create(m) for m in sq_angle_marks], lag_ratio=0.3),
            run_time=1.0
        )

        angle_count_sq = Text(
            "4个直角",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ANGLE
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(angle_count_sq, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        compare_hint = Text(
            "比长方形多了：四边相等!",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_SQ
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(compare_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        summary_sq = Text(
            "正方形：四边相等，四个直角",
            font="Heiti SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(summary_sq, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sq),
            FadeOut(feat2_title), FadeOut(sq_angle_marks),
            FadeOut(angle_count_sq), FadeOut(compare_hint),
            FadeOut(summary_sq),
            run_time=0.5
        )

    # =========================================================
    # 场景 4 - 三角形
    # =========================================================
    def scene_4_triangle(self):
        """三角形特征：三条边，三个角"""
        title = Text(
            "三角形",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_TRI
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        tri = Polygon(
            self.T_A, self.T_B, self.T_C,
            color=self.COLOR_TRI,
            stroke_width=5,
            fill_opacity=0.12,
            fill_color=self.COLOR_TRI
        )
        self.play(Create(tri), run_time=0.9)

        dot_A = Dot(self.T_A, color=self.COLOR_TRI, radius=0.1)
        dot_B = Dot(self.T_B, color=self.COLOR_TRI, radius=0.1)
        dot_C = Dot(self.T_C, color=self.COLOR_TRI, radius=0.1)
        lbl_A = Text("A", font="Heiti SC", font_size=22, color=WHITE).next_to(self.T_A, UP,  buff=0.12)
        lbl_B = Text("B", font="Heiti SC", font_size=22, color=WHITE).next_to(self.T_B, DL,  buff=0.12)
        lbl_C = Text("C", font="Heiti SC", font_size=22, color=WHITE).next_to(self.T_C, DR,  buff=0.12)

        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C),
            FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C),
            run_time=0.5
        )
        self.wait(0.3)

        # ---- 特征1：三条边 ----
        feat1_title = Text(
            "特征一：有三条边",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat1_title, shift=UP * 0.2), run_time=0.5)

        side_AB = Line(self.T_A, self.T_B, color=self.COLOR_HIGHLIGHT, stroke_width=8)
        side_BC = Line(self.T_B, self.T_C, color=self.COLOR_HIGHLIGHT, stroke_width=8)
        side_CA = Line(self.T_C, self.T_A, color=self.COLOR_HIGHLIGHT, stroke_width=8)

        lbl_side1 = Text("边1", font="Heiti SC", font_size=20, color=self.COLOR_HIGHLIGHT)
        lbl_side1.move_to((self.T_A + self.T_B) / 2 + np.array([-0.4, 0.1, 0]))
        lbl_side2 = Text("边2", font="Heiti SC", font_size=20, color=self.COLOR_HIGHLIGHT)
        lbl_side2.move_to((self.T_B + self.T_C) / 2 + np.array([0, -0.35, 0]))
        lbl_side3 = Text("边3", font="Heiti SC", font_size=20, color=self.COLOR_HIGHLIGHT)
        lbl_side3.move_to((self.T_C + self.T_A) / 2 + np.array([0.4, 0.1, 0]))

        self.play(Create(side_AB), FadeIn(lbl_side1), run_time=0.5)
        self.play(Create(side_BC), FadeIn(lbl_side2), run_time=0.5)
        self.play(Create(side_CA), FadeIn(lbl_side3), run_time=0.5)

        sides_count = Text(
            "共 3 条边",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_SIDE
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(sides_count, shift=UP * 0.2), run_time=0.5)
        self.wait(0.7)

        self.play(
            FadeOut(side_AB), FadeOut(side_BC), FadeOut(side_CA),
            FadeOut(lbl_side1), FadeOut(lbl_side2), FadeOut(lbl_side3),
            FadeOut(sides_count), FadeOut(feat1_title),
            run_time=0.4
        )

        # ---- 特征2：三个角 ----
        feat2_title = Text(
            "特征二：有三个角",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat2_title, shift=UP * 0.2), run_time=0.5)

        # 角弧
        line_AB_from_A = Line(self.T_A, self.T_B)
        line_AC_from_A = Line(self.T_A, self.T_C)
        angle_A = Angle(line_AB_from_A, line_AC_from_A, radius=0.45,
                        color=self.COLOR_ANGLE, stroke_width=3)

        line_BA_from_B = Line(self.T_B, self.T_A)
        line_BC_from_B = Line(self.T_B, self.T_C)
        angle_B = Angle(line_BA_from_B, line_BC_from_B, radius=0.45,
                        color=self.COLOR_ANGLE, stroke_width=3)

        line_CB_from_C = Line(self.T_C, self.T_B)
        line_CA_from_C = Line(self.T_C, self.T_A)
        angle_C = Angle(line_CB_from_C, line_CA_from_C, radius=0.45,
                        color=self.COLOR_ANGLE, stroke_width=3)

        ang_lbl_A = Text("角A", font="Heiti SC", font_size=18, color=self.COLOR_ANGLE)
        ang_lbl_A.next_to(self.T_A, DOWN, buff=0.5)
        ang_lbl_B = Text("角B", font="Heiti SC", font_size=18, color=self.COLOR_ANGLE)
        ang_lbl_B.next_to(self.T_B, RIGHT, buff=0.35)
        ang_lbl_C = Text("角C", font="Heiti SC", font_size=18, color=self.COLOR_ANGLE)
        ang_lbl_C.next_to(self.T_C, LEFT, buff=0.35)

        self.play(
            LaggedStart(
                AnimationGroup(Create(angle_A), FadeIn(ang_lbl_A)),
                AnimationGroup(Create(angle_B), FadeIn(ang_lbl_B)),
                AnimationGroup(Create(angle_C), FadeIn(ang_lbl_C)),
                lag_ratio=0.4
            ),
            run_time=1.2
        )

        angles_count = Text(
            "共 3 个角",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ANGLE
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(angles_count, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        summary_tri = Text(
            "三角形：三条边，三个角",
            font="Heiti SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(summary_tri, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(tri),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(feat2_title),
            FadeOut(angle_A), FadeOut(angle_B), FadeOut(angle_C),
            FadeOut(ang_lbl_A), FadeOut(ang_lbl_B), FadeOut(ang_lbl_C),
            FadeOut(angles_count), FadeOut(summary_tri),
            run_time=0.5
        )

    # =========================================================
    # 场景 5 - 圆
    # =========================================================
    def scene_5_circle(self):
        """圆的特征：曲线围成，没有角"""
        title = Text(
            "圆",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_CIR
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        circ_center = np.array([0, 1.5, 0])
        circle = Circle(
            radius=1.8,
            color=self.COLOR_CIR,
            stroke_width=5,
            fill_opacity=0.12,
            fill_color=self.COLOR_CIR
        ).move_to(circ_center)
        self.play(Create(circle), run_time=1.2)
        self.wait(0.3)

        # ---- 特征1：曲线围成 ----
        feat1_title = Text(
            "特征一：由曲线围成",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat1_title, shift=UP * 0.2), run_time=0.5)

        circle_highlight = Circle(
            radius=1.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=9
        ).move_to(circ_center)
        self.play(Create(circle_highlight), run_time=0.8)

        # 箭头指向曲线
        arrow_tip = circ_center + np.array([1.8 * np.cos(PI / 5), 1.8 * np.sin(PI / 5), 0])
        curve_label = Text(
            "圆滑的曲线",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(circ_center + np.array([2.6, 0.7, 0]))
        arrow_to_curve = Arrow(
            curve_label.get_left() + LEFT * 0.1,
            arrow_tip,
            color=self.COLOR_HIGHLIGHT,
            buff=0.08,
            stroke_width=3
        )
        self.play(FadeIn(curve_label), Create(arrow_to_curve), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(circle_highlight),
            FadeOut(curve_label),
            FadeOut(arrow_to_curve),
            FadeOut(feat1_title),
            run_time=0.4
        )

        # ---- 特征2：没有角 ----
        feat2_title = Text(
            "特征二：没有角",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(feat2_title, shift=UP * 0.2), run_time=0.5)

        # 对比：小三角形有角，圆没有角
        tri_ctr = np.array([-2.5, 0.0, 0])
        small_tri = Polygon(
            tri_ctr + np.array([0.0,  0.7, 0]),
            tri_ctr + np.array([-0.9, -0.55, 0]),
            tri_ctr + np.array([0.9, -0.55, 0]),
            color=self.COLOR_TRI,
            stroke_width=4,
            fill_opacity=0.15,
            fill_color=self.COLOR_TRI
        )
        tri_label = Text("有角", font="Heiti SC", font_size=20, color=self.COLOR_TRI)
        tri_label.move_to(tri_ctr + np.array([0, -1.1, 0]))

        mini_angle_mark = self.make_right_angle_mark(
            tri_ctr + np.array([0.0, 0.7, 0]),
            tri_ctr + np.array([-0.9, -0.55, 0]),
            tri_ctr + np.array([0.9, -0.55, 0]),
            size=0.18, color=RED
        )

        no_angle_symbol = Text(
            "没有角",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_CIR
        ).move_to(np.array([2.2, -0.8, 0]))

        self.play(FadeIn(small_tri), FadeIn(tri_label), run_time=0.5)
        self.play(Create(mini_angle_mark), run_time=0.4)
        self.play(FadeIn(no_angle_symbol, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        no_corner_text = Text(
            "圆没有角，处处一样圆!",
            font="Heiti SC",
            font_size=25,
            color=self.COLOR_CIR
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(no_corner_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        summary_circle = Text(
            "圆：曲线围成，没有角",
            font="Heiti SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3.4)
        self.play(FadeIn(summary_circle, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(circle),
            FadeOut(feat2_title),
            FadeOut(small_tri), FadeOut(tri_label),
            FadeOut(mini_angle_mark),
            FadeOut(no_angle_symbol),
            FadeOut(no_corner_text), FadeOut(summary_circle),
            run_time=0.5
        )

    # =========================================================
    # 场景 6 - 汇总
    # =========================================================
    def scene_6_summary(self):
        """汇总对比四种图形特征"""
        title = Text(
            "图形特征总结",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        CARD_Y = 3.8

        # 小图形
        rect_s = Rectangle(
            width=1.3, height=0.85,
            color=self.COLOR_RECT,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_RECT
        ).move_to(np.array([-3.2, CARD_Y, 0]))
        rect_name = Text("长方形", font="Heiti SC", font_size=20, color=self.COLOR_RECT).next_to(rect_s, DOWN, buff=0.12)

        sq_s = Square(
            side_length=1.0,
            color=self.COLOR_SQ,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_SQ
        ).move_to(np.array([-1.0, CARD_Y, 0]))
        sq_name = Text("正方形", font="Heiti SC", font_size=20, color=self.COLOR_SQ).next_to(sq_s, DOWN, buff=0.12)

        tri_ctr = np.array([1.2, CARD_Y, 0])
        tri_s = Polygon(
            tri_ctr + np.array([0.0,  0.55, 0]),
            tri_ctr + np.array([-0.65, -0.45, 0]),
            tri_ctr + np.array([0.65, -0.45, 0]),
            color=self.COLOR_TRI,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_TRI
        )
        tri_name = Text("三角形", font="Heiti SC", font_size=20, color=self.COLOR_TRI).move_to(tri_ctr + np.array([0, -0.78, 0]))

        cir_s = Circle(
            radius=0.5,
            color=self.COLOR_CIR,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_CIR
        ).move_to(np.array([3.2, CARD_Y, 0]))
        cir_name = Text("圆", font="Heiti SC", font_size=20, color=self.COLOR_CIR).next_to(cir_s, DOWN, buff=0.12)

        shapes_group = VGroup(rect_s, sq_s, tri_s, cir_s)
        names_group  = VGroup(rect_name, sq_name, tri_name, cir_name)

        self.play(
            LaggedStart(
                GrowFromCenter(rect_s), GrowFromCenter(sq_s),
                GrowFromCenter(tri_s),  GrowFromCenter(cir_s),
                lag_ratio=0.2
            ),
            run_time=1.0
        )
        self.play(FadeIn(names_group), run_time=0.5)
        self.wait(0.4)

        # 特征列表（两行）
        feat_data = [
            (np.array([-3.2, CARD_Y - 1.3, 0]), "对边相等", "四个直角", self.COLOR_RECT),
            (np.array([-1.0, CARD_Y - 1.3, 0]), "四边相等", "四个直角", self.COLOR_SQ),
            (np.array([ 1.2, CARD_Y - 1.3, 0]), "三条边",   "三个角",   self.COLOR_TRI),
            (np.array([ 3.2, CARD_Y - 1.3, 0]), "曲线围成", "没有角",   self.COLOR_CIR),
        ]
        feat_labels = VGroup()
        for pos, f1_str, f2_str, color in feat_data:
            f1 = Text(f1_str, font="Heiti SC", font_size=18, color=color)
            f2 = Text(f2_str, font="Heiti SC", font_size=18, color=color)
            col = VGroup(f1, f2).arrange(DOWN, buff=0.18)
            col.move_to(pos)
            feat_labels.add(col)

        self.play(
            LaggedStart(*[FadeIn(fl, shift=UP * 0.2) for fl in feat_labels], lag_ratio=0.2),
            run_time=1.0
        )
        self.wait(1.2)

        # 特别强调正方形
        highlight_box = SurroundingRectangle(
            VGroup(sq_s, sq_name),
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            stroke_width=3
        )
        special_note = Text(
            "正方形是特殊的长方形!",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.6)

        self.play(Create(highlight_box), run_time=0.5)
        self.play(FadeIn(special_note, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        # 记忆口诀
        rhyme_title = Text(
            "记忆口诀:",
            font="Heiti SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 1.8)

        rhyme = Text(
            "长方对边两两等，\n正方四边全相同，\n三角三边加三角，\n圆无角来曲线成。",
            font="Heiti SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(DOWN * 3.6)

        self.play(FadeIn(rhyme_title), run_time=0.4)
        self.play(Write(rhyme), run_time=1.8)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(shapes_group), FadeOut(names_group),
            FadeOut(feat_labels),
            FadeOut(highlight_box), FadeOut(special_note),
            FadeOut(rhyme_title), FadeOut(rhyme),
            run_time=0.6
        )

    # =========================================================
    # 场景 7 - 片尾
    # =========================================================
    def scene_7_outro(self):
        """片尾：关注信息"""
        deco_shapes = VGroup(
            Rectangle(
                width=0.8, height=0.5,
                color=self.COLOR_RECT,
                fill_opacity=0.5, fill_color=self.COLOR_RECT
            ).move_to(UP * 2.5 + LEFT * 3.0),
            Square(
                side_length=0.6,
                color=self.COLOR_SQ,
                fill_opacity=0.5, fill_color=self.COLOR_SQ
            ).move_to(UP * 2.5 + LEFT * 1.5),
            Polygon(
                np.array([0.0,  2.9, 0]),
                np.array([-0.45, 2.1, 0]),
                np.array([0.45,  2.1, 0]),
                color=self.COLOR_TRI,
                fill_opacity=0.5, fill_color=self.COLOR_TRI
            ),
            Circle(
                radius=0.35,
                color=self.COLOR_CIR,
                fill_opacity=0.5, fill_color=self.COLOR_CIR
            ).move_to(UP * 2.5 + RIGHT * 1.5),
        )

        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in deco_shapes], lag_ratio=0.2),
            run_time=1.0
        )

        author_main = Text(
            "上海初高中数学直通车",
            font="Heiti SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 0.8)
        author_id = Text(
            "@emptyandcalm",
            font="Heiti SC",
            font_size=26,
            color="#6b7280"
        ).move_to(UP * 0.0)
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.2)

        self.play(FadeIn(author_main, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 快速复习
        review = Text(
            "今天学了：",
            font="Heiti SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 2.8)

        review_items = VGroup(
            Text("长方形 - 对边相等，四个直角", font="Heiti SC", font_size=20, color=self.COLOR_RECT),
            Text("正方形 - 四边相等，四个直角", font="Heiti SC", font_size=20, color=self.COLOR_SQ),
            Text("三角形 - 三条边，三个角",   font="Heiti SC", font_size=20, color=self.COLOR_TRI),
            Text("圆 - 曲线围成，没有角",     font="Heiti SC", font_size=20, color=self.COLOR_CIR),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).move_to(DOWN * 4.5)

        self.play(FadeIn(review), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(item, shift=UP * 0.2) for item in review_items], lag_ratio=0.2),
            run_time=1.0
        )
        self.wait(2.0)

        self.play(
            FadeOut(self.author_info),
            FadeOut(deco_shapes),
            FadeOut(author_main),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(review),
            FadeOut(review_items),
            run_time=0.8
        )

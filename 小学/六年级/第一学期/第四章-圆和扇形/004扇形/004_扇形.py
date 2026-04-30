"""
004扇形 - Sector Lesson Animation
使用 Manim 创建的数学教学视频

内容: 扇形的定义、各部分名称、面积公式
目标观众: 六年级学生
格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SectorLesson(Scene):
    """
    扇形教学动画场景

    场景顺序:
    1. 开场钩子 - 披萨引出扇形
    2. 扇形的定义 - 从圆中切出扇形
    3. 各部分名称 - 圆心角、弧、半径
    4. 扇形面积公式推导
    5. 例题演练
    6. 不同圆心角的扇形对比
    7. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_CIRCLE = "#3498db"
        self.COLOR_SECTOR = "#e74c3c"
        self.COLOR_ARC = "#f39c12"
        self.COLOR_RADIUS = "#2ecc71"
        self.COLOR_ANGLE = "#9b59b6"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_FORMULA = "#1abc9c"

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_parts()
        self.scene_4_formula()
        self.scene_5_example()
        self.scene_6_comparison()
        self.scene_7_summary()

    def setup_geometry(self):
        """初始化几何数据"""
        # 主圆参数
        self.RADIUS = 2.2
        self.CENTER = np.array([0, 1.5, 0])

        # 扇形参数 - 90度扇形
        self.SECTOR_ANGLE = 90  # 度
        self.SECTOR_ANGLE_RAD = np.radians(self.SECTOR_ANGLE)

        # 扇形起始角度（从右侧水平开始）
        self.START_ANGLE = 0
        self.START_ANGLE_RAD = np.radians(self.START_ANGLE)

        # 计算关键点
        self.point_A = self.CENTER + self.RADIUS * np.array([
            np.cos(self.START_ANGLE_RAD), np.sin(self.START_ANGLE_RAD), 0
        ])
        self.point_B = self.CENTER + self.RADIUS * np.array([
            np.cos(self.START_ANGLE_RAD + self.SECTOR_ANGLE_RAD),
            np.sin(self.START_ANGLE_RAD + self.SECTOR_ANGLE_RAD), 0
        ])

    # ─────────────────────────────────────────────
    # Scene 1: Opening
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        """开场: 钩子引出扇形"""
        # 作者标识
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "一块披萨是什么形状?",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        self.play(Write(hook), run_time=0.8)

        # 画一个圆代表披萨
        pizza = Circle(
            radius=2.0,
            color="#f39c12",
            fill_color="#e67e22",
            fill_opacity=0.6,
            stroke_width=3
        ).move_to(UP * 1.0)
        self.play(Create(pizza), run_time=0.8)

        # 切几刀 - 用线模拟切割
        cut_lines = VGroup()
        for angle_deg in [0, 60, 120, 180, 240, 300]:
            angle_rad = np.radians(angle_deg)
            end_point = pizza.get_center() + 2.0 * np.array([
                np.cos(angle_rad), np.sin(angle_rad), 0
            ])
            cut_line = Line(
                pizza.get_center(), end_point,
                color=WHITE, stroke_width=2
            )
            cut_lines.add(cut_line)

        self.play(Create(cut_lines), run_time=0.6)
        self.wait(0.3)

        # 高亮一块扇形
        sector_piece = Sector(
            arc_center=pizza.get_center(),
            radius=2.0,
            start_angle=0,
            angle=PI / 3,
            color=self.COLOR_SECTOR,
            fill_opacity=0.7,
            stroke_width=2
        )
        self.play(FadeIn(sector_piece), run_time=0.5)

        # 移出一块
        self.play(
            sector_piece.animate.shift(RIGHT * 0.6 + DOWN * 0.3),
            run_time=0.6
        )

        answer = Text(
            "这就是 —— 扇形!",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(pizza), FadeOut(cut_lines),
            FadeOut(sector_piece), FadeOut(answer),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 2: Definition
    # ─────────────────────────────────────────────
    def scene_2_definition(self):
        """扇形的定义 - 从圆中切出扇形"""
        title = Text(
            "扇形的定义",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 画一个完整的圆
        circle = Circle(
            radius=self.RADIUS,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.CENTER)
        self.play(Create(circle), run_time=1.0)

        # 标注圆心 O
        center_dot = Dot(self.CENTER, color=WHITE, radius=0.06)
        center_label = MathTex("O", font_size=28, color=WHITE).next_to(
            center_dot, DL, buff=0.15
        )
        self.play(FadeIn(center_dot), Write(center_label), run_time=0.5)

        # 画两条半径
        radius_1 = Line(
            self.CENTER, self.point_A,
            color=self.COLOR_RADIUS, stroke_width=3
        )
        radius_2 = Line(
            self.CENTER, self.point_B,
            color=self.COLOR_RADIUS, stroke_width=3
        )

        label_A = MathTex("A", font_size=24, color=WHITE).next_to(
            self.point_A, RIGHT, buff=0.15
        )
        label_B = MathTex("B", font_size=24, color=WHITE).next_to(
            self.point_B, UP, buff=0.15
        )

        self.play(Create(radius_1), Write(label_A), run_time=0.6)
        self.play(Create(radius_2), Write(label_B), run_time=0.6)

        # 标注圆心角
        angle_arc = Arc(
            radius=0.5,
            start_angle=self.START_ANGLE_RAD,
            angle=self.SECTOR_ANGLE_RAD,
            arc_center=self.CENTER,
            color=self.COLOR_ANGLE,
            stroke_width=3
        )
        angle_label = MathTex(
            r"90^\circ", font_size=22, color=self.COLOR_ANGLE
        ).move_to(
            self.CENTER + 0.85 * np.array([
                np.cos(self.START_ANGLE_RAD + self.SECTOR_ANGLE_RAD / 2),
                np.sin(self.START_ANGLE_RAD + self.SECTOR_ANGLE_RAD / 2), 0
            ])
        )
        self.play(Create(angle_arc), Write(angle_label), run_time=0.6)

        # 填充扇形区域
        sector = Sector(
            arc_center=self.CENTER,
            radius=self.RADIUS,
            start_angle=self.START_ANGLE_RAD,
            angle=self.SECTOR_ANGLE_RAD,
            color=self.COLOR_SECTOR,
            fill_opacity=0.35,
            stroke_width=0
        )
        self.play(FadeIn(sector), run_time=0.8)

        # 高亮弧
        arc = Arc(
            radius=self.RADIUS,
            start_angle=self.START_ANGLE_RAD,
            angle=self.SECTOR_ANGLE_RAD,
            arc_center=self.CENTER,
            color=self.COLOR_ARC,
            stroke_width=5
        )
        self.play(Create(arc), run_time=0.6)

        # 定义文字
        def_text_1 = Text(
            "由圆心角的两条半径",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 2.5)
        def_text_2 = Text(
            "和它所对的弧围成的图形",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 3.3)
        def_text_3 = Text(
            "叫做扇形",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.3)

        self.play(FadeIn(def_text_1), run_time=0.5)
        self.play(FadeIn(def_text_2), run_time=0.5)
        self.play(FadeIn(def_text_3), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(circle), FadeOut(center_dot),
            FadeOut(center_label), FadeOut(radius_1), FadeOut(radius_2),
            FadeOut(label_A), FadeOut(label_B),
            FadeOut(angle_arc), FadeOut(angle_label),
            FadeOut(sector), FadeOut(arc),
            FadeOut(def_text_1), FadeOut(def_text_2), FadeOut(def_text_3),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 3: Parts of a Sector
    # ─────────────────────────────────────────────
    def scene_3_parts(self):
        """扇形各部分名称"""
        title = Text(
            "扇形的组成",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 画扇形 (使用120度更好展示)
        show_angle = 120
        show_angle_rad = np.radians(show_angle)
        start_angle_rad = np.radians(-30)  # 略微倾斜

        center = np.array([0, 1.5, 0])
        radius = 2.5

        point_a = center + radius * np.array([
            np.cos(start_angle_rad), np.sin(start_angle_rad), 0
        ])
        point_b = center + radius * np.array([
            np.cos(start_angle_rad + show_angle_rad),
            np.sin(start_angle_rad + show_angle_rad), 0
        ])

        # 扇形填充
        sector = Sector(
            arc_center=center,
            radius=radius,
            start_angle=start_angle_rad,
            angle=show_angle_rad,
            color=self.COLOR_SECTOR,
            fill_opacity=0.25,
            stroke_width=0
        )

        # 两条半径
        r1 = Line(center, point_a, color=self.COLOR_RADIUS, stroke_width=3)
        r2 = Line(center, point_b, color=self.COLOR_RADIUS, stroke_width=3)

        # 弧
        arc = Arc(
            radius=radius,
            start_angle=start_angle_rad,
            angle=show_angle_rad,
            arc_center=center,
            color=self.COLOR_ARC,
            stroke_width=4
        )

        # 圆心
        center_dot = Dot(center, color=WHITE, radius=0.07)

        self.play(
            FadeIn(sector), Create(r1), Create(r2),
            Create(arc), FadeIn(center_dot),
            run_time=1.0
        )

        # Part 1: 圆心角
        angle_arc = Arc(
            radius=0.6,
            start_angle=start_angle_rad,
            angle=show_angle_rad,
            arc_center=center,
            color=self.COLOR_ANGLE,
            stroke_width=4
        )

        angle_text_group = VGroup(
            Text("圆心角", font="PingFang SC", font_size=22,
                 color=self.COLOR_ANGLE),
        ).move_to(DOWN * 2.8)

        angle_desc = Text(
            "两条半径所成的角",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(Create(angle_arc), run_time=0.6)
        self.play(FadeIn(angle_text_group), FadeIn(angle_desc), run_time=0.5)

        # 闪烁高亮
        self.play(
            angle_arc.animate.set_color(YELLOW),
            run_time=0.3
        )
        self.play(
            angle_arc.animate.set_color(self.COLOR_ANGLE),
            run_time=0.3
        )
        self.wait(0.8)
        self.play(FadeOut(angle_text_group), FadeOut(angle_desc), run_time=0.3)

        # Part 2: 半径
        r_label = Text(
            "半径 r",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_RADIUS
        ).move_to(DOWN * 2.8)

        r_desc = Text(
            "从圆心到弧上的线段",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        # 半径上标r
        mid_r1 = (center + point_a) / 2
        r_math = MathTex("r", font_size=26, color=self.COLOR_RADIUS).next_to(
            mid_r1, DOWN, buff=0.15
        )

        self.play(
            r1.animate.set_color(YELLOW), r2.animate.set_color(YELLOW),
            FadeIn(r_label), FadeIn(r_desc), Write(r_math),
            run_time=0.5
        )
        self.wait(0.8)
        self.play(
            r1.animate.set_color(self.COLOR_RADIUS),
            r2.animate.set_color(self.COLOR_RADIUS),
            FadeOut(r_label), FadeOut(r_desc), FadeOut(r_math),
            run_time=0.3
        )

        # Part 3: 弧
        arc_label = Text(
            "弧",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_ARC
        ).move_to(DOWN * 2.8)

        arc_desc = Text(
            "圆上两点之间的曲线部分",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(
            arc.animate.set_color(YELLOW).set_stroke(width=6),
            FadeIn(arc_label), FadeIn(arc_desc),
            run_time=0.5
        )
        self.wait(0.8)
        self.play(
            arc.animate.set_color(self.COLOR_ARC).set_stroke(width=4),
            FadeOut(arc_label), FadeOut(arc_desc),
            run_time=0.3
        )

        # 总结标注 - 同时显示三个名称
        o_label = MathTex("O", font_size=24, color=WHITE).next_to(
            center_dot, DL, buff=0.12
        )

        summary_parts = VGroup(
            Text("圆心角", font="PingFang SC", font_size=20,
                 color=self.COLOR_ANGLE),
            Text(" + ", font="PingFang SC", font_size=20, color=WHITE),
            Text("半径", font="PingFang SC", font_size=20,
                 color=self.COLOR_RADIUS),
            Text(" + ", font="PingFang SC", font_size=20, color=WHITE),
            Text("弧", font="PingFang SC", font_size=20,
                 color=self.COLOR_ARC),
            Text(" = ", font="PingFang SC", font_size=20, color=WHITE),
            Text("扇形", font="PingFang SC", font_size=22,
                 color=self.COLOR_SECTOR),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.0)

        self.play(Write(o_label), FadeIn(summary_parts), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sector), FadeOut(r1), FadeOut(r2),
            FadeOut(arc), FadeOut(center_dot), FadeOut(angle_arc),
            FadeOut(o_label), FadeOut(summary_parts),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 4: Formula Derivation
    # ─────────────────────────────────────────────
    def scene_4_formula(self):
        """扇形面积公式"""
        title = Text(
            "扇形面积公式",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # Step 1: 圆的面积
        circle_center = np.array([0, 2.5, 0])
        circle_r = 1.8

        circle = Circle(
            radius=circle_r,
            color=self.COLOR_CIRCLE,
            fill_color=self.COLOR_CIRCLE,
            fill_opacity=0.2,
            stroke_width=3
        ).move_to(circle_center)

        circle_area_label = VGroup(
            Text("圆的面积 = ", font="PingFang SC", font_size=22,
                 color=WHITE),
            MathTex(r"\pi r^2", font_size=28, color=self.COLOR_CIRCLE)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.5)

        self.play(Create(circle), run_time=0.8)
        self.play(FadeIn(circle_area_label), run_time=0.5)
        self.wait(0.5)

        # Step 2: 扇形占圆的比例
        think_text = Text(
            "扇形是圆的一部分",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(think_text), run_time=0.5)

        # 在圆上画出一个扇形 (90度)
        sector_90 = Sector(
            arc_center=circle_center,
            radius=circle_r,
            start_angle=0,
            angle=PI / 2,
            color=self.COLOR_SECTOR,
            fill_opacity=0.5,
            stroke_width=2
        )
        self.play(FadeIn(sector_90), run_time=0.6)

        # 标注角度
        angle_label_90 = MathTex(
            r"90^\circ", font_size=22, color=self.COLOR_ANGLE
        ).move_to(circle_center + 0.7 * np.array([
            np.cos(PI / 4), np.sin(PI / 4), 0
        ]))
        self.play(Write(angle_label_90), run_time=0.4)

        # 比例说明
        ratio_text = VGroup(
            Text("占圆的比例 = ", font="PingFang SC", font_size=22,
                 color=WHITE),
            MathTex(r"\frac{90}{360}", font_size=28, color=self.COLOR_ANGLE),
            MathTex(r"= \frac{1}{4}", font_size=28, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)

        self.play(FadeIn(ratio_text), run_time=0.6)
        self.wait(1.0)

        # 清理部分元素
        self.play(
            FadeOut(circle), FadeOut(sector_90),
            FadeOut(circle_area_label), FadeOut(think_text),
            FadeOut(angle_label_90), FadeOut(ratio_text),
            run_time=0.5
        )

        # Step 3: 推导通用公式
        derive_title = Text(
            "推导公式",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(derive_title), run_time=0.5)

        # 通用扇形图
        general_center = np.array([0, 1.0, 0])
        general_r = 1.5

        general_sector = Sector(
            arc_center=general_center,
            radius=general_r,
            start_angle=0,
            angle=np.radians(72),
            color=self.COLOR_SECTOR,
            fill_opacity=0.4,
            stroke_width=2
        )
        general_r1 = Line(
            general_center,
            general_center + general_r * RIGHT,
            color=self.COLOR_RADIUS, stroke_width=2
        )
        general_r2 = Line(
            general_center,
            general_center + general_r * np.array([
                np.cos(np.radians(72)), np.sin(np.radians(72)), 0
            ]),
            color=self.COLOR_RADIUS, stroke_width=2
        )

        n_label = MathTex(
            r"n^\circ", font_size=24, color=self.COLOR_ANGLE
        ).move_to(general_center + 0.65 * np.array([
            np.cos(np.radians(36)), np.sin(np.radians(36)), 0
        ]))

        r_label = MathTex(
            "r", font_size=24, color=self.COLOR_RADIUS
        ).move_to((general_center + general_center + general_r * RIGHT) / 2 + DOWN * 0.25)

        self.play(
            FadeIn(general_sector),
            Create(general_r1), Create(general_r2),
            Write(n_label), Write(r_label),
            run_time=0.8
        )

        # 公式推导步骤
        step1_label = Text(
            "圆心角占圆的比例:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5)

        step1_formula = MathTex(
            r"\frac{n}{360}", font_size=32, color=self.COLOR_ANGLE
        ).move_to(DOWN * 2.3)

        self.play(FadeIn(step1_label), run_time=0.4)
        self.play(Write(step1_formula), run_time=0.5)
        self.wait(0.5)

        step2_label = Text(
            "扇形面积 = 比例 x 圆面积",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(step2_label), run_time=0.4)

        # 最终公式 - 用 highlight box
        final_formula = MathTex(
            r"S = \frac{n}{360} \times \pi r^2",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 5.0)

        formula_box = SurroundingRectangle(
            final_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.1,
            stroke_width=2
        )

        self.play(Write(final_formula), run_time=1.0)
        self.play(Create(formula_box), run_time=0.5)

        # 标注含义
        n_meaning = VGroup(
            MathTex("n", font_size=22, color=self.COLOR_ANGLE),
            Text(" : 圆心角度数", font="PingFang SC", font_size=18,
                 color=GRAY_A),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 6.2)

        r_meaning = VGroup(
            MathTex("r", font_size=22, color=self.COLOR_RADIUS),
            Text(" : 半径", font="PingFang SC", font_size=18,
                 color=GRAY_A),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 6.8)

        self.play(FadeIn(n_meaning), FadeIn(r_meaning), run_time=0.5)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(derive_title),
            FadeOut(general_sector), FadeOut(general_r1), FadeOut(general_r2),
            FadeOut(n_label), FadeOut(r_label),
            FadeOut(step1_label), FadeOut(step1_formula),
            FadeOut(step2_label),
            FadeOut(final_formula), FadeOut(formula_box),
            FadeOut(n_meaning), FadeOut(r_meaning),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 5: Example Problem
    # ─────────────────────────────────────────────
    def scene_5_example(self):
        """例题演练"""
        title = Text(
            "例题",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 题目
        problem_1 = Text(
            "已知扇形的半径 r = 6 cm,",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 4.5)
        problem_2 = VGroup(
            Text("圆心角 n = ", font="PingFang SC", font_size=24,
                 color=WHITE),
            MathTex(r"60^\circ", font_size=28, color=self.COLOR_ANGLE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.8)

        problem_3 = Text(
            "求扇形的面积。",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 3.1)

        self.play(FadeIn(problem_1), run_time=0.4)
        self.play(FadeIn(problem_2), run_time=0.4)
        self.play(FadeIn(problem_3), run_time=0.4)

        # 画扇形示意图
        ex_center = np.array([0, 1.0, 0])
        ex_r = 1.5

        ex_sector = Sector(
            arc_center=ex_center,
            radius=ex_r,
            start_angle=0,
            angle=np.radians(60),
            color=self.COLOR_SECTOR,
            fill_opacity=0.35,
            stroke_width=2
        )
        ex_r1 = Line(
            ex_center, ex_center + ex_r * RIGHT,
            color=self.COLOR_RADIUS, stroke_width=2
        )
        ex_r2 = Line(
            ex_center,
            ex_center + ex_r * np.array([
                np.cos(np.radians(60)), np.sin(np.radians(60)), 0
            ]),
            color=self.COLOR_RADIUS, stroke_width=2
        )
        ex_arc = Arc(
            radius=ex_r,
            start_angle=0,
            angle=np.radians(60),
            arc_center=ex_center,
            color=self.COLOR_ARC,
            stroke_width=3
        )
        ex_center_dot = Dot(ex_center, color=WHITE, radius=0.05)

        # 标注
        ex_angle_label = MathTex(
            r"60^\circ", font_size=20, color=self.COLOR_ANGLE
        ).move_to(ex_center + 0.55 * np.array([
            np.cos(np.radians(30)), np.sin(np.radians(30)), 0
        ]))

        mid_r1 = (ex_center + ex_center + ex_r * RIGHT) / 2
        ex_r_label = Text(
            "6 cm", font="PingFang SC", font_size=18,
            color=self.COLOR_RADIUS
        ).next_to(mid_r1, DOWN, buff=0.12)

        self.play(
            FadeIn(ex_sector), Create(ex_r1), Create(ex_r2),
            Create(ex_arc), FadeIn(ex_center_dot),
            Write(ex_angle_label), Write(ex_r_label),
            run_time=0.8
        )
        self.wait(0.5)

        # 解题步骤
        solve_title = Text(
            "解:",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0 + LEFT * 3.0)
        self.play(Write(solve_title), run_time=0.3)

        # Step 1: 代入公式
        step1 = MathTex(
            r"S = \frac{n}{360} \times \pi r^2",
            font_size=28, color=WHITE
        ).move_to(DOWN * 1.8)
        self.play(Write(step1), run_time=0.6)
        self.wait(0.3)

        # Step 2: 代入数值
        step2 = MathTex(
            r"= \frac{60}{360} \times \pi \times 6^2",
            font_size=28, color=WHITE
        ).move_to(DOWN * 2.8)
        self.play(Write(step2), run_time=0.6)
        self.wait(0.3)

        # Step 3: 计算
        step3 = MathTex(
            r"= \frac{1}{6} \times 36\pi",
            font_size=28, color=WHITE
        ).move_to(DOWN * 3.8)
        self.play(Write(step3), run_time=0.6)
        self.wait(0.3)

        # Step 4: 结果
        step4 = MathTex(
            r"= 6\pi",
            font_size=32, color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.8)

        result_text = VGroup(
            MathTex(r"\approx 18.85", font_size=26, color=GRAY_A),
            Text(" cm", font="PingFang SC", font_size=20, color=GRAY_A),
            MathTex(r"^2", font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 5.6)

        self.play(Write(step4), run_time=0.5)
        self.play(FadeIn(result_text), run_time=0.4)

        # 高亮答案
        answer_box = SurroundingRectangle(
            VGroup(step4, result_text),
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1,
            stroke_width=2
        )
        self.play(Create(answer_box), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(problem_1), FadeOut(problem_2),
            FadeOut(problem_3),
            FadeOut(ex_sector), FadeOut(ex_r1), FadeOut(ex_r2),
            FadeOut(ex_arc), FadeOut(ex_center_dot),
            FadeOut(ex_angle_label), FadeOut(ex_r_label),
            FadeOut(solve_title),
            FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
            FadeOut(result_text), FadeOut(answer_box),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 6: Comparison of Different Angles
    # ─────────────────────────────────────────────
    def scene_6_comparison(self):
        """不同圆心角的扇形对比"""
        title = Text(
            "圆心角越大, 扇形面积越大",
            font="PingFang SC",
            font_size=28,
            color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 三个扇形: 60, 120, 270 度
        angles_deg = [60, 120, 270]
        colors = ["#e74c3c", "#3498db", "#2ecc71"]
        y_positions = [3.0, 0.0, -3.5]
        sector_radius = 1.3

        sector_groups = []
        for i, (angle_deg, color, y_pos) in enumerate(
            zip(angles_deg, colors, y_positions)
        ):
            angle_rad = np.radians(angle_deg)
            center = np.array([-1.5, y_pos, 0])

            # 画圆的轮廓
            circle_outline = Circle(
                radius=sector_radius,
                color=GRAY,
                stroke_width=1,
                stroke_opacity=0.3
            ).move_to(center)

            # 扇形
            sector = Sector(
                arc_center=center,
                radius=sector_radius,
                start_angle=0,
                angle=angle_rad,
                color=color,
                fill_opacity=0.5,
                stroke_width=2
            )

            # 两条半径
            r1 = Line(
                center, center + sector_radius * RIGHT,
                color=WHITE, stroke_width=1.5
            )
            r2_end = center + sector_radius * np.array([
                np.cos(angle_rad), np.sin(angle_rad), 0
            ])
            r2 = Line(center, r2_end, color=WHITE, stroke_width=1.5)

            # 角度标记
            angle_arc = Arc(
                radius=0.4,
                start_angle=0,
                angle=angle_rad,
                arc_center=center,
                color=YELLOW,
                stroke_width=2
            )

            # 角度文字
            angle_text = MathTex(
                str(angle_deg) + r"^\circ",
                font_size=22,
                color=YELLOW
            )
            # 角度文字放在扇形外侧
            mid_angle = angle_rad / 2
            if angle_deg <= 180:
                angle_text.move_to(center + 0.7 * np.array([
                    np.cos(mid_angle), np.sin(mid_angle), 0
                ]))
            else:
                angle_text.move_to(center + DOWN * 0.5)

            # 面积描述
            if angle_deg == 60:
                frac_str = r"\frac{1}{6}"
            elif angle_deg == 120:
                frac_str = r"\frac{1}{3}"
            else:
                frac_str = r"\frac{3}{4}"

            area_info = VGroup(
                MathTex(
                    r"n = " + str(angle_deg) + r"^\circ",
                    font_size=22, color=WHITE
                ),
                VGroup(
                    Text("占圆的 ", font="PingFang SC", font_size=18,
                         color=GRAY_A),
                    MathTex(frac_str, font_size=24, color=color),
                ).arrange(RIGHT, buff=0.1),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(
                np.array([2.2, y_pos, 0])
            )

            group = VGroup(
                circle_outline, sector, r1, r2,
                angle_arc, angle_text, area_info
            )
            sector_groups.append(group)

        # 依次显示
        for i, group in enumerate(sector_groups):
            self.play(FadeIn(group), run_time=0.8)
            self.wait(0.5)

        # 总结箭头
        arrow1 = Arrow(
            np.array([2.2, 2.0, 0]),
            np.array([2.2, 1.0, 0]),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2,
            buff=0.1
        )
        arrow2 = Arrow(
            np.array([2.2, -1.0, 0]),
            np.array([2.2, -2.5, 0]),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2,
            buff=0.1
        )

        trend_text = Text(
            "角度增大 -> 面积增大",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.0)

        self.play(
            Create(arrow1), Create(arrow2),
            FadeIn(trend_text),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            *[FadeOut(g) for g in sector_groups],
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(trend_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 7: Summary + Outro
    # ─────────────────────────────────────────────
    def scene_7_summary(self):
        """总结与结尾"""
        title = Text(
            "知识小结",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 小扇形装饰
        deco_sector = Sector(
            arc_center=np.array([0, 3.5, 0]),
            radius=1.0,
            start_angle=np.radians(30),
            angle=np.radians(120),
            color=self.COLOR_SECTOR,
            fill_opacity=0.3,
            stroke_width=2
        )
        self.play(FadeIn(deco_sector), run_time=0.4)

        # 知识点列表
        items = [
            ("1.", "扇形 = 圆心角 + 两条半径 + 弧"),
            ("2.", "圆心角决定扇形大小"),
            ("3.", "面积公式:"),
        ]

        item_groups = []
        for i, (num, text) in enumerate(items):
            item = VGroup(
                Text(num, font="PingFang SC", font_size=22,
                     color=self.COLOR_HIGHLIGHT),
                Text(text, font="PingFang SC", font_size=22,
                     color=WHITE),
            ).arrange(RIGHT, buff=0.15).move_to(
                np.array([-0.5, 1.2 - i * 1.0, 0]),
                aligned_edge=LEFT
            )
            item_groups.append(item)

        for item in item_groups:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 公式（突出显示）
        formula = MathTex(
            r"S = \frac{n}{360} \times \pi r^2",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 1.5)

        formula_box = SurroundingRectangle(
            formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            corner_radius=0.1,
            stroke_width=3
        )

        self.play(Write(formula), run_time=0.8)
        self.play(Create(formula_box), run_time=0.4)
        self.wait(1.5)

        # 记忆口诀
        tip = Text(
            "记住: n 分之 360, 乘以圆面积!",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_ARC
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理进入片尾
        self.play(
            FadeOut(title), FadeOut(deco_sector),
            *[FadeOut(item) for item in item_groups],
            FadeOut(formula), FadeOut(formula_box), FadeOut(tip),
            run_time=0.6
        )

        # ─── 片尾 ───
        outro_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.0)

        outro_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.0)

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.2)

        self.play(
            FadeIn(outro_name, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(outro_id), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰扇形
        deco_sectors = VGroup()
        for i in range(5):
            s = Sector(
                arc_center=ORIGIN,
                radius=0.4,
                start_angle=np.radians(i * 72),
                angle=np.radians(50),
                color=[RED, BLUE, GREEN, ORANGE, PURPLE][i],
                fill_opacity=0.6,
                stroke_width=1
            ).move_to(DOWN * 3.0 + np.array([
                (i - 2) * 1.2, 0, 0
            ]))
            deco_sectors.add(s)

        self.play(
            *[FadeIn(s, scale=0.5) for s in deco_sectors],
            run_time=0.6
        )
        self.wait(1.5)

        # 最终淡出
        self.play(
            FadeOut(self.author),
            FadeOut(outro_name), FadeOut(outro_id), FadeOut(follow),
            FadeOut(deco_sectors),
            run_time=0.8
        )


# 运行命令:
# manim -pql 004_扇形.py SectorLesson  # 快速预览
# manim -qm 004_扇形.py SectorLesson   # 中等质量
# manim -qh 004_扇形.py SectorLesson   # 高质量

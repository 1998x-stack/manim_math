from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 任意角与弧度制Animation(Scene):
    """
    任意角与弧度制教学动画场景

    场景顺序:
    1. 开场介绍
    2. 任意角的概念
    3. 弧度制的概念
    4. 弧度与角度转换
    5. 弧长公式
    6. 扇形面积公式
    7. 终边相同的角
    8. 片尾关注
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_MAIN = BLUE
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_FORMULA = WHITE

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_arbitrary_angle()
        self.show_radian_measure()
        self.show_conversion()
        self.show_arc_length()
        self.show_sector_area()
        self.show_terminal_angle()
        self.show_outro()

    def setup_geometry(self):
        """初始化几何数据和参数"""
        # 基准圆心
        self.CENTER = ORIGIN

        # 单位圆
        self.RADIUS = 2.5

        # 初始角度 (45度为例)
        self.ANGLE_DEG = 45
        self.ANGLE_RAD = self.ANGLE_DEG * PI / 180

        # 计算角度对应的点
        self.START_POINT = self.CENTER + self.RADIUS * RIGHT  # 起始点 (0度)
        self.END_POINT = self.CENTER + self.RADIUS * np.array([
            np.cos(self.ANGLE_RAD),
            np.sin(self.ANGLE_RAD),
            0
        ])  # 终点

        # 中点用于弧线
        self.MID_ANGLE_RAD = self.ANGLE_RAD / 2
        self.MID_POINT = self.CENTER + self.RADIUS * np.array([
            np.cos(self.MID_ANGLE_RAD),
            np.sin(self.MID_ANGLE_RAD),
            0
        ])

        # 验证几何计算
        self.verify_geometry()

    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6

        # 验证角度计算
        dist_start = np.linalg.norm(self.START_POINT - self.CENTER)
        dist_end = np.linalg.norm(self.END_POINT - self.CENTER)

        if abs(dist_start - dist_end) > epsilon:
            print(f"WARNING: 点到圆心距离不相等! {dist_start:.6f} vs {dist_end:.6f}")

        # 验证计算的角度
        calculated_angle = np.arctan2(
            self.END_POINT[1] - self.CENTER[1],
            self.END_POINT[0] - self.CENTER[0]
        )
        expected_angle = self.ANGLE_RAD if self.ANGLE_RAD >= 0 else self.ANGLE_RAD + 2*PI

        if abs(calculated_angle - expected_angle) > epsilon:
            print(f"WARNING: 角度计算不匹配! {calculated_angle:.6f} vs {expected_angle:.6f}")

        print("✓ 几何验证完成")

    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "任意角与弧度制",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6.5)

        subtitle = Text(
            "三角比的基础概念",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.7)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.5
        )

    def show_arbitrary_angle(self):
        """场景2: 任意角的概念"""
        # 标题
        title = Text(
            "任意角的概念",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MAIN
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 创建单位圆
        circle = Circle(radius=self.RADIUS, color=self.COLOR_MAIN)
        circle.move_to(self.CENTER)

        # 坐标轴
        x_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        y_axis = Line(UP * 4, DOWN * 4, color=WHITE)

        # 绘制坐标轴
        self.play(Create(x_axis), Create(y_axis), run_time=0.5)
        self.play(Create(circle), run_time=1.0)

        # 起始边 (x轴正方向)
        initial_line = Line(self.CENTER, self.START_POINT, color=GREEN, stroke_width=4)
        self.play(Create(initial_line), run_time=0.5)

        # 终边 (旋转到45度)
        terminal_line = Line(self.CENTER, self.END_POINT, color=RED, stroke_width=4)
        self.play(Create(terminal_line), run_time=1.0)

        # 显示角度弧
        angle_arc = Arc(
            radius=0.8,
            start_angle=0,
            angle=self.ANGLE_RAD,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        ).move_arc_center_to(self.CENTER)

        self.play(Create(angle_arc), run_time=0.8)

        # 角度标注
        angle_label = MathTex(f"{self.ANGLE_DEG}°", color=self.COLOR_HIGHLIGHT).next_to(
            angle_arc.get_center() + np.array([0.4, 0.4, 0]), UR, buff=0.1
        )

        self.play(Write(angle_label), run_time=0.5)

        # 定义说明
        definition = Text(
            "任意角：角的概念从锐角推广到\n任意大小的正角、负角和零角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(definition), run_time=0.5)

        # 方向说明
        direction_text = Text(
            "正角为逆时针旋转，负角为顺时针旋转",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(direction_text), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(initial_line),
            FadeOut(terminal_line),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(definition),
            FadeOut(direction_text),
            run_time=0.6
        )

    def show_radian_measure(self):
        """场景3: 弧度制的概念"""
        # 标题
        title = Text(
            "弧度制的概念",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MAIN
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 创建单位圆
        circle = Circle(radius=self.RADIUS, color=self.COLOR_MAIN)
        circle.move_to(self.CENTER)

        # 绘制圆
        self.play(Create(circle), run_time=1.0)

        # 弧线 (π/2 即 90度)
        quarter_arc = Arc(
            radius=self.RADIUS,
            start_angle=0,
            angle=PI/2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        ).move_arc_center_to(self.CENTER)

        self.play(Create(quarter_arc), run_time=1.0)

        # 标注弧长等于半径的弧 (1弧度)
        unit_arc_angle = 1  # 1弧度约57.3度
        unit_arc = Arc(
            radius=self.RADIUS,
            start_angle=0,
            angle=unit_arc_angle,
            color=YELLOW,
            stroke_width=8
        ).move_arc_center_to(self.CENTER)

        # 弧长标注
        arc_label = Text(
            "弧长 = 半径",
            font="Noto Sans CJK SC",
            font_size=20,
            color=YELLOW
        ).move_to(UP * 2 + RIGHT * 2)

        # 半径线
        radius_line = Line(self.CENTER, self.CENTER + self.RADIUS * np.array([
            np.cos(unit_arc_angle),
            np.sin(unit_arc_angle),
            0
        ]), color=RED, stroke_width=4)

        self.play(
            Create(unit_arc),
            Write(arc_label),
            Create(radius_line),
            run_time=1.0
        )

        # 1弧度定义
        rad_def = Text(
            "1弧度：弧长等于半径的弧所对的圆心角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(rad_def), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(circle),
            FadeOut(quarter_arc),
            FadeOut(unit_arc),
            FadeOut(arc_label),
            FadeOut(radius_line),
            FadeOut(rad_def),
            run_time=0.6
        )

    def show_conversion(self):
        """场景4: 弧度与角度转换"""
        # 标题
        title = Text(
            "弧度与角度转换",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MAIN
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 圆周率关系
        pi_formula = MathTex("\\pi \\text{ rad} = 180^\\circ", color=self.COLOR_FORMULA, font_size=36)
        pi_formula.move_to(UP * 5)

        self.play(Write(pi_formula), run_time=0.8)

        # 1弧度 = ?度
        rad_to_deg = MathTex("1 \\text{ rad} = \\frac{180^\\circ}{\\pi} \\approx 57.3^\\circ",
                            color=self.COLOR_FORMULA, font_size=32)
        rad_to_deg.move_to(UP * 3.8)

        self.play(Write(rad_to_deg), run_time=0.8)

        # 1度 = ?弧度
        deg_to_rad = MathTex("1^\\circ = \\frac{\\pi}{180} \\text{ rad}",
                            color=self.COLOR_FORMULA, font_size=32)
        deg_to_rad.move_to(UP * 2.6)

        self.play(Write(deg_to_rad), run_time=0.8)

        # 示例转换
        example_title = Text(
            "示例:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.2)

        example_1 = MathTex("90^\\circ = \\frac{\\pi}{2} \\text{ rad}", color=self.COLOR_HIGHLIGHT, font_size=28)
        example_1.next_to(example_title, DOWN, buff=0.3)

        example_2 = MathTex("60^\\circ = \\frac{\\pi}{3} \\text{ rad}", color=self.COLOR_HIGHLIGHT, font_size=28)
        example_2.next_to(example_1, DOWN, buff=0.3)

        example_3 = MathTex("45^\\circ = \\frac{\\pi}{4} \\text{ rad}", color=self.COLOR_HIGHLIGHT, font_size=28)
        example_3.next_to(example_2, DOWN, buff=0.3)

        self.play(
            Write(example_title),
            Write(example_1),
            Write(example_2),
            Write(example_3),
            run_time=1.0
        )

        # 提示
        tip = Text(
            "记住常用角度的弧度表示，有助于快速计算",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)

        self.play(FadeIn(tip), run_time=0.5)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(pi_formula),
            FadeOut(rad_to_deg),
            FadeOut(deg_to_rad),
            FadeOut(example_title),
            FadeOut(example_1),
            FadeOut(example_2),
            FadeOut(example_3),
            FadeOut(tip),
            run_time=0.6
        )

    def show_arc_length(self):
        """场景5: 弧长公式"""
        # 标题
        title = Text(
            "弧长公式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MAIN
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 公式
        formula = MathTex("l = |\\alpha| \\cdot r", color=self.COLOR_FORMULA, font_size=40)
        formula.move_to(UP * 5)

        self.play(Write(formula), run_time=0.8)

        # 图解
        # 创建圆
        circle = Circle(radius=self.RADIUS, color=self.COLOR_MAIN)
        circle.move_to(self.CENTER)

        # 中心点
        center_dot = Dot(self.CENTER, color=WHITE, radius=0.1)

        # 半径线
        radius_line = Line(self.CENTER, self.END_POINT, color=RED, stroke_width=4)
        radius_label = MathTex("r", color=RED).next_to(
            (self.CENTER + self.END_POINT) / 2, UR, buff=0.1
        )

        # 弧
        arc = Arc(
            radius=self.RADIUS,
            start_angle=0,
            angle=self.ANGLE_RAD,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        ).move_arc_center_to(self.CENTER)

        # 弧长
        arc_length_label = MathTex("l", color=self.COLOR_HIGHLIGHT).next_to(
            self.MID_POINT, UR, buff=0.1
        )

        # 角度
        angle_arc = Arc(
            radius=0.8,
            start_angle=0,
            angle=self.ANGLE_RAD,
            color=YELLOW,
            stroke_width=4
        ).move_arc_center_to(self.CENTER)
        angle_label = MathTex("\\alpha", color=YELLOW).next_to(
            angle_arc.get_center() + np.array([0.4, 0.4, 0]), UR, buff=0.1
        )

        # 绘制图解
        self.play(
            Create(circle),
            FadeIn(center_dot),
            Create(radius_line),
            Write(radius_label),
            Create(arc),
            Write(arc_length_label),
            Create(angle_arc),
            Write(angle_label),
            run_time=1.5
        )

        # 公式说明
        explanation = Text(
            "其中 l 是弧长，α 是圆心角(弧度)，r 是半径",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(explanation), run_time=0.5)

        # 示例
        example = MathTex(
            "\\text{For example: when } \\alpha = \\frac{\\pi}{3}, r = 6 \\text{, then } l = \\frac{\\pi}{3} \\times 6 = 2\\pi",
            color=self.COLOR_HIGHLIGHT,
            font_size=24
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(example), run_time=0.5)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(circle),
            FadeOut(center_dot),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(arc),
            FadeOut(arc_length_label),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(explanation),
            FadeOut(example),
            run_time=0.6
        )

    def show_sector_area(self):
        """场景6: 扇形面积公式"""
        # 标题
        title = Text(
            "扇形面积公式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MAIN
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 两个公式
        formula_1 = MathTex("S = \\frac{1}{2}lr", color=self.COLOR_FORMULA, font_size=36)
        formula_1.move_to(UP * 5.2)

        formula_2 = MathTex("S = \\frac{1}{2}|\\alpha|r^2", color=self.COLOR_FORMULA, font_size=36)
        formula_2.move_to(UP * 4.2)

        self.play(Write(formula_1), Write(formula_2), run_time=1.0)

        # 扇形图解
        # 创建完整的圆用于对比
        circle = Circle(radius=self.RADIUS, color=self.COLOR_MAIN)
        circle.move_to(self.CENTER)

        # 扇形区域
        sector = Sector(
            radius=self.RADIUS,
            angle=self.ANGLE_RAD,
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        ).move_arc_center_to(self.CENTER)

        # 半径线
        radius_1 = Line(self.CENTER, self.START_POINT, color=RED, stroke_width=4)
        radius_2 = Line(self.CENTER, self.END_POINT, color=RED, stroke_width=4)

        # 弧
        arc = Arc(
            radius=self.RADIUS,
            start_angle=0,
            angle=self.ANGLE_RAD,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        ).move_arc_center_to(self.CENTER)

        # 角度
        angle_arc = Arc(
            radius=0.8,
            start_angle=0,
            angle=self.ANGLE_RAD,
            color=YELLOW,
            stroke_width=4
        ).move_arc_center_to(self.CENTER)
        angle_label = MathTex("\\alpha", color=YELLOW).next_to(
            angle_arc.get_center() + np.array([0.4, 0.4, 0]), UR, buff=0.1
        )

        # 面积标注
        area_label = MathTex("S", color=self.COLOR_HIGHLIGHT).move_to(
            self.CENTER + 0.6 * self.RADIUS * np.array([
                np.cos(self.ANGLE_RAD/2),
                np.sin(self.ANGLE_RAD/2),
                0
            ])
        )

        # 绘制图解
        self.play(
            Create(circle),
            Create(sector),
            Create(radius_1),
            Create(radius_2),
            Create(arc),
            Create(angle_arc),
            Write(angle_label),
            Write(area_label),
            run_time=1.5
        )

        # 公式说明
        explanation = Text(
            "这两个公式在弧度制下形式简洁，体现了弧度制的优势",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(explanation), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(circle),
            FadeOut(sector),
            FadeOut(radius_1),
            FadeOut(radius_2),
            FadeOut(arc),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(area_label),
            FadeOut(explanation),
            run_time=0.6
        )

    def show_terminal_angle(self):
        """场景7: 终边相同的角"""
        # 标题
        title = Text(
            "终边相同的角",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MAIN
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.8)

        # 公式
        formula = MathTex("\\alpha + 2k\\pi \\quad (k \\in \\mathbb{Z})", color=self.COLOR_FORMULA, font_size=36)
        formula.move_to(UP * 5)

        self.play(Write(formula), run_time=0.8)

        # 图解：多个角度具有相同终边
        circle = Circle(radius=self.RADIUS, color=self.COLOR_MAIN)
        circle.move_to(self.CENTER)

        # 原始角度终边
        original_line = Line(self.CENTER, self.END_POINT, color=RED, stroke_width=4)

        # 角度弧
        angle_arc = Arc(
            radius=0.8,
            start_angle=0,
            angle=self.ANGLE_RAD,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        ).move_arc_center_to(self.CENTER)
        angle_label = MathTex("\\alpha", color=self.COLOR_HIGHLIGHT).next_to(
            angle_arc.get_center() + np.array([0.4, 0.4, 0]), UR, buff=0.1
        )

        # 同终边的其他角度
        # α + 2π
        end_point_2pi = self.CENTER + self.RADIUS * np.array([
            np.cos(self.ANGLE_RAD + 2*PI),
            np.sin(self.ANGLE_RAD + 2*PI),
            0
        ])
        line_2pi = DashedLine(self.CENTER, end_point_2pi, color=YELLOW, stroke_width=3)

        # α - 2π
        end_point_neg2pi = self.CENTER + self.RADIUS * np.array([
            np.cos(self.ANGLE_RAD - 2*PI),
            np.sin(self.ANGLE_RAD - 2*PI),
            0
        ])
        line_neg2pi = DashedLine(self.CENTER, end_point_neg2pi, color=YELLOW, stroke_width=3)

        # 绘制
        self.play(Create(circle), run_time=0.5)
        self.play(Create(original_line), run_time=0.5)
        self.play(Create(angle_arc), Write(angle_label), run_time=0.5)

        self.play(Create(line_2pi), run_time=0.8)
        self.play(Create(line_neg2pi), run_time=0.8)

        # 标注
        label_2pi = MathTex("\\alpha + 2\\pi", color=YELLOW).next_to(end_point_2pi, UR, buff=0.2)
        label_neg2pi = MathTex("\\alpha - 2\\pi", color=YELLOW).next_to(end_point_neg2pi, DL, buff=0.2)

        self.play(Write(label_2pi), Write(label_neg2pi), run_time=0.8)

        # 说明
        explanation = Text(
            "所有与角α终边相同的角都可以表示为α + 2kπ (k为整数)",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(explanation), run_time=0.5)

        # 弧度制优势
        advantage = Text(
            "弧度制使三角函数的导数公式更加简洁",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(advantage), run_time=0.5)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(circle),
            FadeOut(original_line),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(line_2pi),
            FadeOut(line_neg2pi),
            FadeOut(label_2pi),
            FadeOut(label_neg2pi),
            FadeOut(explanation),
            FadeOut(advantage),
            run_time=0.6
        )

    def show_outro(self):
        """场景8: 片尾关注"""
        # 总结
        summary_title = Text(
            "知识点总结",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)

        # 知识点列表
        items = [
            "任意角：推广到任意大小的正角、负角和零角",
            "弧度制：弧长等于半径的弧所对的圆心角为1弧度",
            "转换关系：π rad = 180°",
            "弧长公式：l = |α|r",
            "扇形面积：S = ½lr = ½|α|r²",
            "终边相同的角：α + 2kπ (k∈Z)"
        ]

        item_group = VGroup()
        for i, item in enumerate(items):
            text = Text(item, font="Noto Sans CJK SC", font_size=18, color=WHITE)
            text.move_to(UP * (4 - i * 0.7))
            item_group.add(text)

        self.play(Write(summary_title), run_time=0.6)
        for item in item_group:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(2)

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
            FadeIn(author_name, shift=DOWN * 0.5),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=0.8
        )

        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学知识!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰元素
        # 创建一些弧度相关的图形装饰
        decorative_arcs = VGroup()
        for i in range(6):
            arc = Arc(
                radius=0.8,
                start_angle=i * PI/3,
                angle=PI/6,
                color=BLUE,
                stroke_width=3
            )
            arc.move_to(2 * np.array([np.cos(i * PI/3), np.sin(i * PI/3), 0]) + DOWN * 3)
            decorative_arcs.add(arc)

        self.play(
            *[Create(arc) for arc in decorative_arcs],
            run_time=1.0
        )

        self.wait(1)

        # 全部淡出
        all_mobjects = [summary_title] + item_group.submobjects + [author_name, author_id, follow_text] + decorative_arcs.submobjects
        self.play(
            *[FadeOut(obj) for obj in all_mobjects],
            run_time=1.0
        )


if __name__ == "__main__":
    # 运行命令: manim -pql 001_任意角与弧度制.py 任意角与弧度制Animation
    pass

"""
正比例函数 - 八年级数学教学动画
形如 y=kx (k≠0) 的函数

TikTok竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

manim -pql proportional_function.py ProportionalFunction   # 快速预览
manim -qh  proportional_function.py ProportionalFunction   # 高质量 1080p
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ProportionalFunction(Scene):
    """
    正比例函数动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义介绍
    3. k>0 情形（一三象限，增函数）
    4. k<0 情形（二四象限，减函数）
    5. |k|大小与陡度对比
    6. 综合总结
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ===== 颜色方案 =====
        self.C_POS  = "#2ecc71"   # k>0 绿色
        self.C_NEG  = "#e74c3c"   # k<0 红色
        self.C_K2   = "#f39c12"   # k=2 橙色
        self.C_AX   = "#5d6d7e"   # 坐标轴
        self.C_GOLD = GOLD

        # ===== 初始化几何数据 =====
        self.setup_geometry()

        # ===== 执行各场景 =====
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_k_positive()
        self.scene_4_k_negative()
        self.scene_5_comparison()
        self.scene_6_summary()
        self.scene_7_outro()

    # ============================================================
    # 几何初始化
    # ============================================================

    def setup_geometry(self):
        """统一初始化所有坐标和几何数据"""

        # 坐标系参数
        self.AXIS_RANGE = 3.2   # 坐标轴范围 ±3.2
        self.AXIS_STEP  = 1     # 刻度步长
        self.PLOT_RANGE = 3.0   # 函数绘制范围

        # 坐标系中心位置（画面中部偏上）
        self.AXES_CENTER = np.array([0, 1.5, 0])

        # 直线端点（在坐标系中的逻辑坐标，实际换算时用 axes.c2p）
        # y = kx 的端点（x=±PLOT_RANGE）
        self.LINE_X_END  =  self.PLOT_RANGE
        self.LINE_X_START= -self.PLOT_RANGE

        # 象限标注位置（坐标系逻辑单位）
        self.Q1_POS = np.array([ 1.8,  1.8, 0])
        self.Q2_POS = np.array([-1.8,  1.8, 0])
        self.Q3_POS = np.array([-1.8, -1.8, 0])
        self.Q4_POS = np.array([ 1.8, -1.8, 0])

        # 验证
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何参数合理性"""
        assert self.AXIS_RANGE > 0, "坐标轴范围必须为正"
        assert self.PLOT_RANGE <= self.AXIS_RANGE, "绘制范围不能超过坐标轴"
        assert self.AXIS_STEP > 0, "刻度步长必须为正"
        # 验证象限标注在范围内
        for pos in [self.Q1_POS, self.Q2_POS, self.Q3_POS, self.Q4_POS]:
            assert abs(pos[0]) <= self.AXIS_RANGE, f"象限位置 {pos} 超出范围"
            assert abs(pos[1]) <= self.AXIS_RANGE, f"象限位置 {pos} 超出范围"
        print("✓ 几何验证通过")

    # ============================================================
    # 辅助方法
    # ============================================================

    def make_axes(self):
        """创建标准坐标系"""
        r = self.AXIS_RANGE
        s = self.AXIS_STEP
        axes = Axes(
            x_range=[-r, r, s],
            y_range=[-r, r, s],
            x_length=6.0,
            y_length=6.0,
            axis_config={
                "color": self.C_AX,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.2,
                "include_numbers": False,
            },
        ).move_to(self.AXES_CENTER)
        return axes

    def make_function_line(self, axes, k, color, x_range=None):
        """创建 y=kx 的直线"""
        if x_range is None:
            x_range = [-self.PLOT_RANGE, self.PLOT_RANGE]
        line = axes.plot(
            lambda x: k * x,
            x_range=x_range,
            color=color,
            stroke_width=3,
        )
        return line

    def make_quadrant_label(self, axes, quad_pos, quad_num, color=GRAY_B):
        """创建象限标注"""
        label = Text(
            f"第{quad_num}象限",
            font="PingFang SC",
            font_size=18,
            color=color,
        ).move_to(axes.c2p(*quad_pos[:2]))
        return label

    def make_axes_labels(self, axes):
        """创建 x/y 轴标签"""
        x_label = MathTex("x", color=self.C_AX, font_size=24).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.1
        )
        y_label = MathTex("y", color=self.C_AX, font_size=24).next_to(
            axes.y_axis.get_end(), UP, buff=0.1
        )
        origin_label = MathTex("O", color=self.C_AX, font_size=20).next_to(
            axes.c2p(0, 0), DL, buff=0.15
        )
        return VGroup(x_label, y_label, origin_label)

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================

    def scene_1_opening(self):
        """开场：抓住注意力"""
        # 作者信息
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 7.2)

        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 钩子标题
        hook = Text(
            "一条直线", font="PingFang SC",
            font_size=52, color=self.C_GOLD,
        ).move_to(UP * 5.5)
        hook2 = Text(
            "藏着多少秘密？", font="PingFang SC",
            font_size=40, color=WHITE,
        ).move_to(UP * 4.6)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.5)

        # 预览坐标系 + 几条线
        preview_axes = self.make_axes()
        ax_labels = self.make_axes_labels(preview_axes)
        self.play(Create(preview_axes), FadeIn(ax_labels), run_time=1.0)

        # 三条线依次飞出（吸引眼球）
        line_preview_1 = self.make_function_line(preview_axes, 1,    self.C_POS)
        line_preview_2 = self.make_function_line(preview_axes, 2,    self.C_K2)
        line_preview_3 = self.make_function_line(preview_axes, -1,   self.C_NEG)

        self.play(Create(line_preview_1), run_time=0.6)
        self.play(Create(line_preview_2), run_time=0.5)
        self.play(Create(line_preview_3), run_time=0.5)
        self.wait(0.5)

        # 清理钩子文字，保留坐标系
        self.play(
            FadeOut(hook),
            FadeOut(hook2),
            FadeOut(line_preview_1),
            FadeOut(line_preview_2),
            FadeOut(line_preview_3),
            run_time=0.5,
        )

        # 保存坐标系供后续场景使用
        self.axes = preview_axes
        self.ax_labels = ax_labels

    # ============================================================
    # Scene 2: 定义介绍
    # ============================================================

    def scene_2_definition(self):
        """介绍正比例函数定义"""
        # 标题
        title = Text(
            "正比例函数", font="PingFang SC",
            font_size=44, color=self.C_GOLD,
        ).move_to(UP * 5.8)

        self.play(Write(title), run_time=0.7)

        # 定义卡片
        def_card = RoundedRectangle(
            width=7.5, height=1.8,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.9,
            stroke_color=self.C_GOLD,
            stroke_width=2,
        ).move_to(UP * 4.5)

        def_text = Text(
            "形如", font="PingFang SC",
            font_size=26, color=WHITE,
        )
        def_formula = MathTex(
            r"y = kx \quad (k \neq 0)",
            font_size=36, color=self.C_GOLD,
        )
        def_suffix = Text(
            "的函数叫做正比例函数",
            font="PingFang SC",
            font_size=26, color=WHITE,
        )

        def_line1 = VGroup(def_text, def_formula, def_suffix).arrange(RIGHT, buff=0.2)
        def_line1.move_to(UP * 4.5)

        self.play(FadeIn(def_card), run_time=0.4)
        self.play(Write(def_text), Write(def_suffix), run_time=0.5)
        self.play(Write(def_formula), run_time=0.8)
        self.wait(1.0)

        # 强调 k≠0
        highlight_box = SurroundingRectangle(def_formula, color=self.C_NEG, buff=0.1)
        self.play(Create(highlight_box), run_time=0.4)

        warn_text = Text(
            "k ≠ 0  非常重要！",
            font="PingFang SC",
            font_size=24, color=self.C_NEG,
        ).move_to(UP * 3.5)
        self.play(FadeIn(warn_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(warn_text), FadeOut(highlight_box), run_time=0.4)

        # 关键特征：图像过原点
        feat1_label = Text(
            "图像特征：", font="PingFang SC",
            font_size=26, color=WHITE,
        ).move_to(UP * 3.4)
        feat1 = Text(
            "✦ 过原点的直线",
            font="PingFang SC",
            font_size=26, color=self.C_POS,
        ).move_to(UP * 2.9)

        self.play(FadeIn(feat1_label), run_time=0.4)
        self.play(FadeIn(feat1, shift=RIGHT * 0.3), run_time=0.5)

        # 在坐标系上标注原点
        origin_dot = Dot(self.axes.c2p(0, 0), color=self.C_GOLD, radius=0.12)
        origin_ring = Circle(radius=0.25, color=self.C_GOLD, stroke_width=2).move_to(
            self.axes.c2p(0, 0)
        )
        origin_note = Text(
            "过原点！",
            font="PingFang SC",
            font_size=20, color=self.C_GOLD,
        ).next_to(origin_dot, UR, buff=0.2)

        self.play(FadeIn(origin_dot, scale=0.5), run_time=0.3)
        self.play(Create(origin_ring), run_time=0.5)
        self.play(FadeIn(origin_note), run_time=0.4)
        self.wait(1.5)

        # 清理，准备下一场景
        self.play(
            FadeOut(title),
            FadeOut(def_card),
            FadeOut(def_line1),
            FadeOut(feat1_label),
            FadeOut(feat1),
            FadeOut(origin_dot),
            FadeOut(origin_ring),
            FadeOut(origin_note),
            run_time=0.6,
        )

    # ============================================================
    # Scene 3: k > 0 情形
    # ============================================================

    def scene_3_k_positive(self):
        """展示 k>0 时的图像特征"""
        # 场景标题
        title = Text(
            "当 k > 0", font="PingFang SC",
            font_size=44, color=self.C_POS,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 画 y = x (k=1)
        label_k1 = VGroup(
            MathTex(r"y = x", font_size=28, color=self.C_POS),
            Text("(k=1)", font="PingFang SC", font_size=22, color=self.C_POS),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.9)

        self.line_k1 = self.make_function_line(self.axes, 1, self.C_POS)
        self.play(Write(label_k1), Create(self.line_k1), run_time=1.0)

        # 标注穿过一、三象限
        q1_label = self.make_quadrant_label(self.axes, self.Q1_POS, "一", self.C_POS)
        q3_label = self.make_quadrant_label(self.axes, self.Q3_POS, "三", self.C_POS)

        arrow_q1 = Arrow(
            start=self.axes.c2p(0.6, 2.2),
            end=self.axes.c2p(*self.Q1_POS[:2]),
            color=self.C_POS, buff=0.1,
            stroke_width=2, max_tip_length_to_length_ratio=0.3,
        )
        arrow_q3 = Arrow(
            start=self.axes.c2p(-0.6, -2.2),
            end=self.axes.c2p(*self.Q3_POS[:2]),
            color=self.C_POS, buff=0.1,
            stroke_width=2, max_tip_length_to_length_ratio=0.3,
        )

        q_note = Text(
            "经过 一、三 象限",
            font="PingFang SC",
            font_size=26, color=self.C_POS,
        ).move_to(DOWN * 3.0)

        self.play(
            FadeIn(q1_label), FadeIn(q3_label),
            Create(arrow_q1), Create(arrow_q3),
            run_time=0.7,
        )
        self.play(FadeIn(q_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 演示 x 增大 → y 增大（动态追踪点）
        tracker = ValueTracker(-2.0)

        # 使用 Line + add_updater 避免 DashedLine 拓扑变化导致的 IndexError
        moving_dot = Dot(
            self.axes.c2p(tracker.get_value(), tracker.get_value()),
            color=YELLOW, radius=0.12,
        )
        moving_dot.add_updater(
            lambda m: m.move_to(
                self.axes.c2p(tracker.get_value(), tracker.get_value())
            )
        )

        x_dline = Line(
            self.axes.c2p(tracker.get_value(), 0),
            self.axes.c2p(tracker.get_value(), tracker.get_value()),
            color=YELLOW, stroke_opacity=0.7, stroke_width=2,
        )
        x_dline.add_updater(
            lambda m: m.put_start_and_end_on(
                self.axes.c2p(tracker.get_value(), 0),
                self.axes.c2p(tracker.get_value(), tracker.get_value())
                if abs(tracker.get_value()) > 0.01
                else self.axes.c2p(tracker.get_value(), 0) + UP * 0.001,
            )
        )

        y_dline = Line(
            self.axes.c2p(0, tracker.get_value()),
            self.axes.c2p(tracker.get_value(), tracker.get_value()),
            color=YELLOW, stroke_opacity=0.7, stroke_width=2,
        )
        y_dline.add_updater(
            lambda m: m.put_start_and_end_on(
                self.axes.c2p(0, tracker.get_value()),
                self.axes.c2p(tracker.get_value(), tracker.get_value())
                if abs(tracker.get_value()) > 0.01
                else self.axes.c2p(0, tracker.get_value()) + RIGHT * 0.001,
            )
        )

        inc_note = Text(
            "x 增大 → y 增大（增函数）",
            font="PingFang SC",
            font_size=24, color=YELLOW,
        ).move_to(DOWN * 3.8)

        self.play(
            FadeOut(q_note),
            FadeIn(moving_dot),
            FadeIn(x_dline),
            FadeIn(y_dline),
            run_time=0.4,
        )
        self.play(FadeIn(inc_note), run_time=0.3)
        self.play(tracker.animate.set_value(2.5), run_time=2.5, rate_func=linear)
        self.wait(0.5)

        self.play(
            FadeOut(moving_dot),
            FadeOut(x_dline),
            FadeOut(y_dline),
            FadeOut(inc_note),
            run_time=0.4,
        )

        # 对比 y = 2x (k=2)
        label_k2 = VGroup(
            MathTex(r"y = 2x", font_size=28, color=self.C_K2),
            Text("(k=2)", font="PingFang SC", font_size=22, color=self.C_K2),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.3)

        self.line_k2 = self.make_function_line(self.axes, 2, self.C_K2)
        self.play(Write(label_k2), Create(self.line_k2), run_time=1.0)

        # |k| 越大越陡
        steep_note = VGroup(
            Text("|k| 越大，", font="PingFang SC", font_size=26, color=WHITE),
            Text("直线越陡！", font="PingFang SC", font_size=26, color=self.C_GOLD),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)

        self.play(FadeIn(steep_note, shift=UP * 0.2), run_time=0.5)

        # 比较角度示意
        angle_arc_1 = Arc(
            radius=0.6,
            start_angle=0,
            angle=np.arctan(1),  # y=x 的斜率角 45°
            color=self.C_POS,
            stroke_width=2,
        ).move_to(self.axes.c2p(0, 0))

        angle_arc_2 = Arc(
            radius=0.45,
            start_angle=0,
            angle=np.arctan(2),  # y=2x 的斜率角 ~63.4°
            color=self.C_K2,
            stroke_width=2,
        ).move_to(self.axes.c2p(0, 0))

        self.play(Create(angle_arc_1), Create(angle_arc_2), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(label_k1),
            FadeOut(label_k2),
            FadeOut(q1_label), FadeOut(q3_label),
            FadeOut(arrow_q1), FadeOut(arrow_q3),
            FadeOut(steep_note),
            FadeOut(angle_arc_1), FadeOut(angle_arc_2),
            FadeOut(self.line_k1),
            FadeOut(self.line_k2),
            run_time=0.6,
        )

    # ============================================================
    # Scene 4: k < 0 情形
    # ============================================================

    def scene_4_k_negative(self):
        """展示 k<0 时的图像特征"""
        title = Text(
            "当 k < 0", font="PingFang SC",
            font_size=44, color=self.C_NEG,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 画 y = -x (k=-1)
        label_kneg = VGroup(
            MathTex(r"y = -x", font_size=28, color=self.C_NEG),
            Text("(k=-1)", font="PingFang SC", font_size=22, color=self.C_NEG),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.9)

        self.line_kneg = self.make_function_line(self.axes, -1, self.C_NEG)
        self.play(Write(label_kneg), Create(self.line_kneg), run_time=1.0)

        # 标注穿过二、四象限
        q2_label = self.make_quadrant_label(self.axes, self.Q2_POS, "二", self.C_NEG)
        q4_label = self.make_quadrant_label(self.axes, self.Q4_POS, "四", self.C_NEG)

        arrow_q2 = Arrow(
            start=self.axes.c2p(-0.6, 2.2),
            end=self.axes.c2p(*self.Q2_POS[:2]),
            color=self.C_NEG, buff=0.1,
            stroke_width=2, max_tip_length_to_length_ratio=0.3,
        )
        arrow_q4 = Arrow(
            start=self.axes.c2p(0.6, -2.2),
            end=self.axes.c2p(*self.Q4_POS[:2]),
            color=self.C_NEG, buff=0.1,
            stroke_width=2, max_tip_length_to_length_ratio=0.3,
        )

        q_note_neg = Text(
            "经过 二、四 象限",
            font="PingFang SC",
            font_size=26, color=self.C_NEG,
        ).move_to(DOWN * 3.0)

        self.play(
            FadeIn(q2_label), FadeIn(q4_label),
            Create(arrow_q2), Create(arrow_q4),
            run_time=0.7,
        )
        self.play(FadeIn(q_note_neg, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 演示 x 增大 → y 减小
        tracker2 = ValueTracker(-2.5)

        # 使用 Line + add_updater 避免 DashedLine 拓扑变化导致的 IndexError
        moving_dot2 = Dot(
            self.axes.c2p(tracker2.get_value(), -tracker2.get_value()),
            color=YELLOW, radius=0.12,
        )
        moving_dot2.add_updater(
            lambda m: m.move_to(
                self.axes.c2p(tracker2.get_value(), -tracker2.get_value())
            )
        )

        x_dline2 = Line(
            self.axes.c2p(tracker2.get_value(), 0),
            self.axes.c2p(tracker2.get_value(), -tracker2.get_value()),
            color=YELLOW, stroke_opacity=0.7, stroke_width=2,
        )
        x_dline2.add_updater(
            lambda m: m.put_start_and_end_on(
                self.axes.c2p(tracker2.get_value(), 0),
                self.axes.c2p(tracker2.get_value(), -tracker2.get_value())
                if abs(tracker2.get_value()) > 0.01
                else self.axes.c2p(tracker2.get_value(), 0) + UP * 0.001,
            )
        )

        y_dline2 = Line(
            self.axes.c2p(0, -tracker2.get_value()),
            self.axes.c2p(tracker2.get_value(), -tracker2.get_value()),
            color=YELLOW, stroke_opacity=0.7, stroke_width=2,
        )
        y_dline2.add_updater(
            lambda m: m.put_start_and_end_on(
                self.axes.c2p(0, -tracker2.get_value()),
                self.axes.c2p(tracker2.get_value(), -tracker2.get_value())
                if abs(tracker2.get_value()) > 0.01
                else self.axes.c2p(0, -tracker2.get_value()) + RIGHT * 0.001,
            )
        )

        dec_note = Text(
            "x 增大 → y 减小（减函数）",
            font="PingFang SC",
            font_size=24, color=YELLOW,
        ).move_to(DOWN * 3.8)

        self.play(
            FadeOut(q_note_neg),
            FadeIn(moving_dot2),
            FadeIn(x_dline2),
            FadeIn(y_dline2),
            run_time=0.4,
        )
        self.play(FadeIn(dec_note), run_time=0.3)
        self.play(tracker2.animate.set_value(2.5), run_time=2.5, rate_func=linear)
        self.wait(0.5)

        self.play(
            FadeOut(moving_dot2),
            FadeOut(x_dline2),
            FadeOut(y_dline2),
            FadeOut(dec_note),
            run_time=0.4,
        )
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(label_kneg),
            FadeOut(q2_label), FadeOut(q4_label),
            FadeOut(arrow_q2), FadeOut(arrow_q4),
            FadeOut(self.line_kneg),
            run_time=0.6,
        )

    # ============================================================
    # Scene 5: 对比汇总
    # ============================================================

    def scene_5_comparison(self):
        """三条线同框对比"""
        title = Text(
            "汇总对比", font="PingFang SC",
            font_size=40, color=self.C_GOLD,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 同时画三条线
        l1 = self.make_function_line(self.axes, 1,  self.C_POS)
        l2 = self.make_function_line(self.axes, 2,  self.C_K2)
        l3 = self.make_function_line(self.axes, -1, self.C_NEG)

        self.play(Create(l1), Create(l2), Create(l3), run_time=1.2)

        # 图例
        legend_items = VGroup(
            VGroup(
                Line(ORIGIN, RIGHT * 0.5, color=self.C_POS, stroke_width=3),
                MathTex(r"y=x", font_size=22, color=self.C_POS),
                Text("(k=1)", font="PingFang SC", font_size=18, color=self.C_POS),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Line(ORIGIN, RIGHT * 0.5, color=self.C_K2, stroke_width=3),
                MathTex(r"y=2x", font_size=22, color=self.C_K2),
                Text("(k=2)", font="PingFang SC", font_size=18, color=self.C_K2),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Line(ORIGIN, RIGHT * 0.5, color=self.C_NEG, stroke_width=3),
                MathTex(r"y=-x", font_size=22, color=self.C_NEG),
                Text("(k=-1)", font="PingFang SC", font_size=18, color=self.C_NEG),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        legend_bg = RoundedRectangle(
            width=3.8, height=3.0,
            corner_radius=0.2,
            fill_color="#16213e",
            fill_opacity=0.9,
            stroke_color=GRAY_B,
            stroke_width=1,
        )
        legend_bg.move_to(DOWN * 4.2 + LEFT * 2.5)
        legend_items.move_to(legend_bg.get_center())

        self.play(FadeIn(legend_bg), FadeIn(legend_items), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(l1), FadeOut(l2), FadeOut(l3),
            FadeOut(legend_bg), FadeOut(legend_items),
            run_time=0.6,
        )

    # ============================================================
    # Scene 6: 知识总结
    # ============================================================

    def scene_6_summary(self):
        """知识点卡片总结"""
        title = Text(
            "知识总结", font="PingFang SC",
            font_size=44, color=self.C_GOLD,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 公式卡片
        formula_card = RoundedRectangle(
            width=7.0, height=1.4,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=self.C_GOLD,
            stroke_width=2,
        ).move_to(UP * 5.0)

        formula_label = Text(
            "正比例函数：",
            font="PingFang SC", font_size=26, color=WHITE,
        )
        formula_tex = MathTex(r"y = kx \quad (k \neq 0)", font_size=34, color=self.C_GOLD)
        formula_content = VGroup(formula_label, formula_tex).arrange(RIGHT, buff=0.2)
        formula_content.move_to(formula_card.get_center())

        self.play(FadeIn(formula_card), Write(formula_content), run_time=0.8)

        # 三条规则（从下往上滑入）
        rules = [
            ("✦ 图像是过原点的直线",           WHITE),
            ("✦ k > 0：一三象限，y随x增大",   self.C_POS),
            ("✦ k < 0：二四象限，y随x减小",   self.C_NEG),
            ("✦ |k| 越大，直线越陡",           self.C_GOLD),
        ]

        rule_cards = VGroup()
        y_pos = 3.8
        for text, color in rules:
            card_bg = RoundedRectangle(
                width=7.5, height=0.9,
                corner_radius=0.2,
                fill_color="#0f3460",
                fill_opacity=0.8,
                stroke_color=color,
                stroke_width=1.5,
            ).move_to(UP * y_pos + RIGHT * 0)

            card_text = Text(
                text, font="PingFang SC",
                font_size=24, color=color,
            ).move_to(card_bg.get_center())

            rule_card = VGroup(card_bg, card_text)
            rule_cards.add(rule_card)
            y_pos -= 1.1

        for card in rule_cards:
            card.shift(LEFT * 9)  # 初始在屏幕左侧外

        for card in rule_cards:
            self.play(card.animate.shift(RIGHT * 9), run_time=0.5)
            self.wait(0.2)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_card),
            FadeOut(formula_content),
            FadeOut(rule_cards),
            FadeOut(self.axes),
            FadeOut(self.ax_labels),
            run_time=0.7,
        )

    # ============================================================
    # Scene 7: 片尾
    # ============================================================

    def scene_7_outro(self):
        """片尾：关注引导"""
        # 大标题
        name_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=44, color=WHITE,
        ).move_to(UP * 2.0)

        id_text = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32, color=GRAY_B,
        ).move_to(UP * 1.0)

        self.play(
            self.author_bar.animate.move_to(UP * 2.0).set_font_size(44).set_color(WHITE),
            run_time=0.8,
        )
        self.play(FadeIn(id_text, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=32, color=self.C_GOLD,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow, scale=1.1, shift=UP * 0.2), run_time=0.6)

        # 装饰性公式群
        formulas = VGroup(
            MathTex(r"y = kx", font_size=28, color=self.C_POS).move_to(DOWN * 2.2),
            MathTex(r"k > 0", font_size=24, color=self.C_K2).move_to(DOWN * 3.0 + LEFT * 1.5),
            MathTex(r"k < 0", font_size=24, color=self.C_NEG).move_to(DOWN * 3.0 + RIGHT * 1.5),
            MathTex(r"k \neq 0", font_size=24, color=GRAY_B).move_to(DOWN * 3.8),
        )
        self.play(
            *[FadeIn(f, scale=0.8) for f in formulas],
            run_time=0.8,
        )

        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(self.author_bar),
            FadeOut(id_text),
            FadeOut(follow),
            FadeOut(formulas),
            run_time=1.0,
        )
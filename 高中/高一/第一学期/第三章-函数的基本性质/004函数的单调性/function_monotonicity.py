"""
函数的单调性 - Function Monotonicity Teaching Animation
高一数学第三章：函数的基本性质

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────
# 全局配置 - TikTok 竖屏
# ─────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FunctionMonotonicity(Scene):
    """
    函数单调性教学动画
    
    场景顺序:
    1. 开场钩子
    2. 单调递增定义（图像 + 点 + 公式）
    3. 单调递减定义
    4. 抛物线：两段单调区间
    5. 作差法（定义法）证明
    6. 导数法简介
    7. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ─── 配色 ───────────────────────────────
        self.C_INC   = "#2ecc71"   # 递增绿
        self.C_DEC   = "#e74c3c"   # 递减红
        self.C_PT    = "#f39c12"   # 点橙
        self.C_ARROW = "#3498db"   # 箭头蓝
        self.C_FORM  = "#f1c40f"   # 公式黄
        self.C_AUX   = GRAY_B      # 辅助灰
        self.C_BG    = "#1a1a2e"

        # ─── 几何初始化 ──────────────────────────
        self.setup_geometry()

        # ─── 场景执行 ─────────────────────────────
        self.scene_1_opening()
        self.scene_2_increasing()
        self.scene_3_decreasing()
        self.scene_4_parabola()
        self.scene_5_difference_method()
        self.scene_6_derivative()
        self.scene_7_outro()

    # ════════════════════════════════════════
    # 几何数据初始化
    # ════════════════════════════════════════
    def setup_geometry(self):
        """统一计算所有坐标，不臆想"""

        # 坐标轴参数（后续场景共用）
        self.AXES_X_RANGE = [-3, 3, 1]
        self.AXES_Y_RANGE = [-1, 4.5, 1]
        self.AXES_X_LEN   = 6.5
        self.AXES_Y_LEN   = 5.0
        self.AXES_CENTER  = np.array([0.0, 2.0, 0.0])

        # 演示用数学坐标（都在 y∈[-1,4.5] 范围内）
        # 递增演示：y = x，选 x1=-1.5, x2=1.5
        self.x1_inc = -1.5
        self.x2_inc =  1.5
        self.y1_inc = self.x1_inc   # f(x) = x
        self.y2_inc = self.x2_inc

        # 递减演示：y = -x，选 x1=-1.5, x2=1.5
        self.x1_dec = -1.5
        self.x2_dec =  1.5
        self.y1_dec = -self.x1_dec  # f(x) = -x → y1=1.5
        self.y2_dec = -self.x2_dec  # f(x) = -x → y2=-1.5，y=-1.5 < y_min=-1，需要调整

        # 调整：只取 x ∈ [0, 2] 区间的递减演示
        self.x1_dec =  0.5
        self.x2_dec =  2.0
        self.y1_dec = -self.x1_dec + 3.0  # 平移：f(x) = -x + 3，y1=2.5
        self.y2_dec = -self.x2_dec + 3.0  # y2=1.0

        # 作差法：f(x)=x²，在 x<0 证明递减，选 x1=-2, x2=-1
        self.x1_diff = -2.0
        self.x2_diff = -1.0
        self.y1_diff = self.x1_diff ** 2   # 4
        self.y2_diff = self.x2_diff ** 2   # 1

    # ─────────────────────────────────────
    def _make_axes(self):
        """创建坐标轴（统一方法）"""
        axes = Axes(
            x_range=self.AXES_X_RANGE,
            y_range=self.AXES_Y_RANGE,
            x_length=self.AXES_X_LEN,
            y_length=self.AXES_Y_LEN,
            axis_config={
                "color": self.C_AUX,
                "include_numbers": True,
                "numbers_to_include": [-2, -1, 0, 1, 2],
                "font_size": 18,
                "tip_length": 0.2,
            },
        ).move_to(self.AXES_CENTER)
        return axes

    # ─────────────────────────────────────
    def _c2p(self, axes, x, y):
        """坐标轴坐标 → 场景坐标（封装）"""
        return axes.c2p(x, y)

    # ════════════════════════════════════════
    # Scene 1: 开场钩子
    # ════════════════════════════════════════
    def scene_1_opening(self):
        # ── 品牌标识（全程固定顶部）
        self.author_info = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.C_AUX,
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.4)

        # ── 标题
        title = Text(
            "函数的单调性",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD,
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.8)

        # ── 钩子问题
        hook = Text(
            "为什么抛物线\n左降右升？",
            font="Noto Sans CJK SC",
            font_size=34,
            color=WHITE,
            line_spacing=1.2,
        ).move_to(UP * 5.0)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)

        # ── 快速展示抛物线
        axes = self._make_axes()
        parabola = axes.plot(
            lambda x: x**2,
            x_range=[-2.1, 2.1],
            color=YELLOW,
            stroke_width=3,
        )
        self.play(Create(axes), run_time=0.8)
        self.play(Create(parabola), run_time=0.8)

        # 高亮左段红（递减）和右段绿（递增）
        para_left = axes.plot(
            lambda x: x**2,
            x_range=[-2.1, 0],
            color=self.C_DEC,
            stroke_width=5,
        )
        para_right = axes.plot(
            lambda x: x**2,
            x_range=[0, 2.1],
            color=self.C_INC,
            stroke_width=5,
        )
        self.play(
            Create(para_left),
            Create(para_right),
            run_time=1.0,
        )

        # 标注箭头
        dec_arrow = Arrow(
            start=axes.c2p(-1.5, 2.0),
            end=axes.c2p(-0.5, 0.2),
            color=self.C_DEC,
            buff=0,
            stroke_width=3,
        )
        inc_arrow = Arrow(
            start=axes.c2p(0.5, 0.2),
            end=axes.c2p(1.5, 2.0),
            color=self.C_INC,
            buff=0,
            stroke_width=3,
        )
        dec_label = Text("递减", font="Noto Sans CJK SC", font_size=24, color=self.C_DEC).next_to(
            axes.c2p(-1.8, 3.5), RIGHT, buff=0.1
        )
        inc_label = Text("递增", font="Noto Sans CJK SC", font_size=24, color=self.C_INC).next_to(
            axes.c2p(0.8, 3.5), LEFT, buff=0.1
        )
        self.play(
            GrowArrow(dec_arrow),
            GrowArrow(inc_arrow),
            FadeIn(dec_label),
            FadeIn(inc_label),
            run_time=0.8,
        )
        self.wait(1.2)

        # 清理，保留 axes 用于下一场景
        self.play(
            FadeOut(title),
            FadeOut(hook),
            FadeOut(parabola),
            FadeOut(para_left),
            FadeOut(para_right),
            FadeOut(dec_arrow),
            FadeOut(inc_arrow),
            FadeOut(dec_label),
            FadeOut(inc_label),
            run_time=0.5,
        )
        self.axes = axes

    # ════════════════════════════════════════
    # Scene 2: 单调递增定义
    # ════════════════════════════════════════
    def scene_2_increasing(self):
        axes = self.axes

        # ── 场景标题
        scene_title = Text(
            "① 单调递增（增函数）",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.C_INC,
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        # ── 递增函数图像 y = x
        graph_inc = axes.plot(
            lambda x: x,
            x_range=[-2.5, 2.5],
            color=self.C_INC,
            stroke_width=3,
        )
        graph_label = MathTex(r"y = x", color=self.C_INC, font_size=28).next_to(
            axes.c2p(2.2, 2.2), RIGHT, buff=0.1
        )
        self.play(Create(graph_inc), Write(graph_label), run_time=1.0)

        # ── 标注 x1 < x2 两点
        x1, x2 = self.x1_inc, self.x2_inc
        y1, y2 = x1, x2  # y = x

        dot_x1 = Dot(axes.c2p(x1, y1), color=self.C_PT, radius=0.1)
        dot_x2 = Dot(axes.c2p(x2, y2), color=self.C_PT, radius=0.1)

        # x 轴上的投影点
        dot_x1_xaxis = Dot(axes.c2p(x1, 0), color=self.C_AUX, radius=0.07)
        dot_x2_xaxis = Dot(axes.c2p(x2, 0), color=self.C_AUX, radius=0.07)

        label_x1 = MathTex(r"x_1", font_size=24, color=self.C_PT).next_to(
            axes.c2p(x1, 0), DOWN, buff=0.15
        )
        label_x2 = MathTex(r"x_2", font_size=24, color=self.C_PT).next_to(
            axes.c2p(x2, 0), DOWN, buff=0.15
        )

        self.play(
            FadeIn(dot_x1),
            FadeIn(dot_x2),
            FadeIn(dot_x1_xaxis),
            FadeIn(dot_x2_xaxis),
            Write(label_x1),
            Write(label_x2),
            run_time=0.8,
        )

        # ── 垂直虚线
        vline_x1 = DashedLine(
            axes.c2p(x1, 0), axes.c2p(x1, y1),
            color=self.C_AUX, dash_length=0.08, stroke_width=1.5,
        )
        vline_x2 = DashedLine(
            axes.c2p(x2, 0), axes.c2p(x2, y2),
            color=self.C_AUX, dash_length=0.08, stroke_width=1.5,
        )
        # 水平虚线
        hline_y1 = DashedLine(
            axes.c2p(0, y1), axes.c2p(x1, y1),
            color=self.C_AUX, dash_length=0.08, stroke_width=1.5,
        )
        hline_y2 = DashedLine(
            axes.c2p(0, y2), axes.c2p(x2, y2),
            color=self.C_AUX, dash_length=0.08, stroke_width=1.5,
        )

        label_fx1 = MathTex(r"f(x_1)", font_size=22, color=self.C_PT).next_to(
            axes.c2p(0, y1), LEFT, buff=0.1
        )
        label_fx2 = MathTex(r"f(x_2)", font_size=22, color=self.C_PT).next_to(
            axes.c2p(0, y2), LEFT, buff=0.1
        )

        self.play(
            Create(vline_x1), Create(vline_x2),
            Create(hline_y1), Create(hline_y2),
            Write(label_fx1), Write(label_fx2),
            run_time=0.8,
        )

        # ── 对比箭头：x1 < x2（向右），f(x1) < f(x2)（向上）
        arr_x = DoubleArrow(
            start=axes.c2p(x1, -0.6),
            end=axes.c2p(x2, -0.6),
            color=self.C_ARROW,
            buff=0,
            stroke_width=2,
            tip_length=0.15,
        )
        label_x_lt = MathTex(r"x_1 < x_2", font_size=22, color=self.C_ARROW).next_to(
            arr_x, DOWN, buff=0.1
        )

        arr_y = DoubleArrow(
            start=axes.c2p(-0.2, y1),
            end=axes.c2p(-0.2, y2),
            color=self.C_INC,
            buff=0,
            stroke_width=2,
            tip_length=0.15,
        )
        label_y_lt = MathTex(r"f(x_1) < f(x_2)", font_size=22, color=self.C_INC).next_to(
            arr_y, LEFT, buff=0.05
        )

        self.play(
            GrowArrow(arr_x), Write(label_x_lt),
            GrowArrow(arr_y), Write(label_y_lt),
            run_time=0.8,
        )

        # ── 定义公式
        definition_text = Text(
            "定义：增函数",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE,
        ).move_to(DOWN * 1.5)
        formula_inc = MathTex(
            r"x_1 < x_2 \Rightarrow f(x_1) < f(x_2)",
            font_size=28,
            color=self.C_FORM,
        ).move_to(DOWN * 2.3)

        self.play(Write(definition_text), run_time=0.5)
        self.play(Write(formula_inc), run_time=0.8)
        self.wait(2.0)  # 关键概念，充分停留

        # ── 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(graph_inc), FadeOut(graph_label),
            FadeOut(dot_x1), FadeOut(dot_x2),
            FadeOut(dot_x1_xaxis), FadeOut(dot_x2_xaxis),
            FadeOut(label_x1), FadeOut(label_x2),
            FadeOut(vline_x1), FadeOut(vline_x2),
            FadeOut(hline_y1), FadeOut(hline_y2),
            FadeOut(label_fx1), FadeOut(label_fx2),
            FadeOut(arr_x), FadeOut(label_x_lt),
            FadeOut(arr_y), FadeOut(label_y_lt),
            FadeOut(definition_text), FadeOut(formula_inc),
            run_time=0.5,
        )

    # ════════════════════════════════════════
    # Scene 3: 单调递减定义
    # ════════════════════════════════════════
    def scene_3_decreasing(self):
        axes = self.axes

        scene_title = Text(
            "② 单调递减（减函数）",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.C_DEC,
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        # ── 递减函数 y = -x + 3（在 [0.5, 2] 上）
        graph_dec = axes.plot(
            lambda x: -x + 3,
            x_range=[-0.5, 3.0],
            color=self.C_DEC,
            stroke_width=3,
        )
        graph_label_dec = MathTex(
            r"y = -x + 3", color=self.C_DEC, font_size=26
        ).next_to(axes.c2p(-0.5, 3.5), RIGHT, buff=0.05)
        self.play(Create(graph_dec), Write(graph_label_dec), run_time=0.8)

        x1, x2 = self.x1_dec, self.x2_dec
        y1, y2 = self.y1_dec, self.y2_dec

        dot_x1 = Dot(axes.c2p(x1, y1), color=self.C_PT, radius=0.1)
        dot_x2 = Dot(axes.c2p(x2, y2), color=self.C_PT, radius=0.1)
        dot_x1_xaxis = Dot(axes.c2p(x1, 0), color=self.C_AUX, radius=0.07)
        dot_x2_xaxis = Dot(axes.c2p(x2, 0), color=self.C_AUX, radius=0.07)

        label_x1 = MathTex(r"x_1", font_size=24, color=self.C_PT).next_to(
            axes.c2p(x1, 0), DOWN, buff=0.15
        )
        label_x2 = MathTex(r"x_2", font_size=24, color=self.C_PT).next_to(
            axes.c2p(x2, 0), DOWN, buff=0.15
        )

        self.play(
            FadeIn(dot_x1), FadeIn(dot_x2),
            FadeIn(dot_x1_xaxis), FadeIn(dot_x2_xaxis),
            Write(label_x1), Write(label_x2),
            run_time=0.6,
        )

        vline_x1 = DashedLine(axes.c2p(x1, 0), axes.c2p(x1, y1), color=self.C_AUX, dash_length=0.08, stroke_width=1.5)
        vline_x2 = DashedLine(axes.c2p(x2, 0), axes.c2p(x2, y2), color=self.C_AUX, dash_length=0.08, stroke_width=1.5)
        hline_y1 = DashedLine(axes.c2p(0, y1), axes.c2p(x1, y1), color=self.C_AUX, dash_length=0.08, stroke_width=1.5)
        hline_y2 = DashedLine(axes.c2p(0, y2), axes.c2p(x2, y2), color=self.C_AUX, dash_length=0.08, stroke_width=1.5)

        label_fx1 = MathTex(r"f(x_1)", font_size=22, color=self.C_PT).next_to(axes.c2p(0, y1), LEFT, buff=0.1)
        label_fx2 = MathTex(r"f(x_2)", font_size=22, color=self.C_PT).next_to(axes.c2p(0, y2), LEFT, buff=0.1)

        self.play(
            Create(vline_x1), Create(vline_x2),
            Create(hline_y1), Create(hline_y2),
            Write(label_fx1), Write(label_fx2),
            run_time=0.7,
        )

        # x1 < x2，但 f(x1) > f(x2)（箭头向下）
        arr_x = DoubleArrow(
            start=axes.c2p(x1, -0.6),
            end=axes.c2p(x2, -0.6),
            color=self.C_ARROW, buff=0, stroke_width=2, tip_length=0.15,
        )
        label_x_lt = MathTex(r"x_1 < x_2", font_size=22, color=self.C_ARROW).next_to(arr_x, DOWN, buff=0.1)

        # y 方向：从 y2(低) 到 y1(高)，用向下箭头
        arr_y = DoubleArrow(
            start=axes.c2p(-0.2, y2),
            end=axes.c2p(-0.2, y1),
            color=self.C_DEC, buff=0, stroke_width=2, tip_length=0.15,
        )
        label_y_gt = MathTex(r"f(x_1) > f(x_2)", font_size=22, color=self.C_DEC).next_to(arr_y, LEFT, buff=0.05)

        self.play(
            GrowArrow(arr_x), Write(label_x_lt),
            GrowArrow(arr_y), Write(label_y_gt),
            run_time=0.8,
        )

        definition_text = Text(
            "定义：减函数",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE,
        ).move_to(DOWN * 1.5)
        formula_dec = MathTex(
            r"x_1 < x_2 \Rightarrow f(x_1) > f(x_2)",
            font_size=28,
            color=self.C_FORM,
        ).move_to(DOWN * 2.3)

        self.play(Write(definition_text), run_time=0.5)
        self.play(Write(formula_dec), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(scene_title),
            FadeOut(graph_dec), FadeOut(graph_label_dec),
            FadeOut(dot_x1), FadeOut(dot_x2),
            FadeOut(dot_x1_xaxis), FadeOut(dot_x2_xaxis),
            FadeOut(label_x1), FadeOut(label_x2),
            FadeOut(vline_x1), FadeOut(vline_x2),
            FadeOut(hline_y1), FadeOut(hline_y2),
            FadeOut(label_fx1), FadeOut(label_fx2),
            FadeOut(arr_x), FadeOut(label_x_lt),
            FadeOut(arr_y), FadeOut(label_y_gt),
            FadeOut(definition_text), FadeOut(formula_dec),
            run_time=0.5,
        )

    # ════════════════════════════════════════
    # Scene 4: 图像法 - 抛物线两段单调区间
    # ════════════════════════════════════════
    def scene_4_parabola(self):
        axes = self.axes

        scene_title = Text(
            "图像法判断单调性",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD,
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        hint = Text(
            "从左到右：上升 → 递增，下降 → 递减",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_AUX,
        ).move_to(UP * 5.3)
        self.play(FadeIn(hint), run_time=0.4)

        # ── 抛物线 y = x²
        parabola = axes.plot(
            lambda x: x**2,
            x_range=[-2.1, 2.1],
            color=GRAY_B,
            stroke_width=2,
        )
        func_label = MathTex(r"y = x^2", font_size=28, color=WHITE).next_to(
            axes.c2p(1.6, 3.5), RIGHT, buff=0.05
        )
        self.play(Create(parabola), Write(func_label), run_time=0.8)

        # ── 左段（递减）高亮
        left_seg = axes.plot(
            lambda x: x**2,
            x_range=[-2.1, 0],
            color=self.C_DEC,
            stroke_width=5,
        )
        dec_bracket = Text(
            "(-∞, 0)",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_DEC,
        ).next_to(axes.c2p(-1.5, -0.7), DOWN, buff=0.1)
        dec_text = Text(
            "单调递减",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_DEC,
        ).next_to(dec_bracket, DOWN, buff=0.05)

        self.play(Create(left_seg), run_time=0.8)
        self.play(FadeIn(dec_bracket), FadeIn(dec_text), run_time=0.5)

        # ── 右段（递增）高亮
        right_seg = axes.plot(
            lambda x: x**2,
            x_range=[0, 2.1],
            color=self.C_INC,
            stroke_width=5,
        )
        inc_bracket = Text(
            "(0, +∞)",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_INC,
        ).next_to(axes.c2p(1.5, -0.7), DOWN, buff=0.1)
        inc_text = Text(
            "单调递增",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_INC,
        ).next_to(inc_bracket, DOWN, buff=0.05)

        self.play(Create(right_seg), run_time=0.8)
        self.play(FadeIn(inc_bracket), FadeIn(inc_text), run_time=0.5)

        # ── 顶点标注
        vertex_dot = Dot(axes.c2p(0, 0), color=YELLOW, radius=0.1)
        vertex_label = Text(
            "转折点 (0,0)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=YELLOW,
        ).next_to(axes.c2p(0, 0), UR, buff=0.15)
        self.play(FadeIn(vertex_dot, scale=0.5), Write(vertex_label), run_time=0.6)

        self.wait(2.0)

        self.play(
            FadeOut(scene_title), FadeOut(hint),
            FadeOut(parabola), FadeOut(func_label),
            FadeOut(left_seg), FadeOut(right_seg),
            FadeOut(dec_bracket), FadeOut(dec_text),
            FadeOut(inc_bracket), FadeOut(inc_text),
            FadeOut(vertex_dot), FadeOut(vertex_label),
            run_time=0.5,
        )

    # ════════════════════════════════════════
    # Scene 5: 作差法（定义法）
    # ════════════════════════════════════════
    def scene_5_difference_method(self):
        axes = self.axes

        # 先淡出坐标轴，切换到纯文字场景
        self.play(FadeOut(axes), run_time=0.4)

        scene_title = Text(
            "作差法（定义法）证明",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD,
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.6)

        example_title = Text(
            "例：证明 f(x) = x² 在 (-∞, 0) 单调递减",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE,
        ).move_to(UP * 5.2)
        self.play(FadeIn(example_title), run_time=0.5)

        # ── 步骤逐步出现
        step_spacing = 0.9

        steps_text = [
            ("设", r"x_1 < x_2 < 0"),
            ("作差", r"f(x_1) - f(x_2) = x_1^2 - x_2^2"),
            ("因式", r"= (x_1 + x_2)(x_1 - x_2)"),
        ]
        steps_analysis = [
            r"x_1 + x_2 < 0,\quad x_1 - x_2 < 0",
            r"\therefore\ (x_1+x_2)(x_1-x_2) > 0",
            r"\therefore\ f(x_1) - f(x_2) > 0",
            r"\therefore\ f(x_1) > f(x_2)",
        ]

        step_mobjects = []
        y_start = 4.0

        # 前3步（label + formula）
        for i, (label, formula) in enumerate(steps_text):
            y_pos = y_start - i * step_spacing
            label_mob = Text(
                label + "：",
                font="Noto Sans CJK SC",
                font_size=24,
                color=self.C_AUX,
            ).move_to(LEFT * 2.8 + UP * y_pos)
            formula_mob = MathTex(formula, font_size=26, color=WHITE).next_to(
                label_mob, RIGHT, buff=0.15
            )
            self.play(FadeIn(label_mob), Write(formula_mob), run_time=0.6)
            step_mobjects.extend([label_mob, formula_mob])

        # 分析步骤
        y_analysis_start = y_start - len(steps_text) * step_spacing - 0.3
        for i, formula in enumerate(steps_analysis):
            y_pos = y_analysis_start - i * step_spacing
            color = self.C_FORM if i >= 2 else WHITE
            mob = MathTex(formula, font_size=26, color=color).move_to(UP * y_pos)
            self.play(Write(mob), run_time=0.6)
            step_mobjects.append(mob)

        # ── 结论高亮框
        conclusion = Text(
            "∴ f(x) = x²  在  (-∞, 0) 上单调递减  ✓",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_INC,
        ).move_to(DOWN * 2.8)
        box = SurroundingRectangle(conclusion, color=self.C_INC, buff=0.2, corner_radius=0.1)
        self.play(Write(conclusion), Create(box), run_time=0.8)
        self.wait(2.5)

        self.play(
            FadeOut(scene_title),
            FadeOut(example_title),
            *[FadeOut(m) for m in step_mobjects],
            FadeOut(conclusion),
            FadeOut(box),
            run_time=0.5,
        )

    # ════════════════════════════════════════
    # Scene 6: 导数法简介
    # ════════════════════════════════════════
    def scene_6_derivative(self):
        # 重新创建坐标轴
        axes = self._make_axes()
        self.play(FadeIn(axes), run_time=0.5)
        self.axes = axes

        scene_title = Text(
            "导数法（进阶）",
            font="Noto Sans CJK SC",
            font_size=32,
            color=PURPLE_B,
        ).move_to(UP * 6.2)
        self.play(Write(scene_title), run_time=0.5)

        # ── 抛物线
        parabola = axes.plot(lambda x: x**2, x_range=[-2.1, 2.1], color=GRAY_B, stroke_width=2)
        self.play(Create(parabola), run_time=0.6)

        # ── 切线在 x=1.5（递增区，斜率>0）
        x_inc = 1.5
        slope_inc = 2 * x_inc  # f'(x) = 2x
        y_inc = x_inc**2
        tangent_pt_inc = axes.c2p(x_inc, y_inc)

        tan_start_inc = axes.c2p(x_inc - 0.8, y_inc - slope_inc * 0.8)
        tan_end_inc   = axes.c2p(x_inc + 0.8, y_inc + slope_inc * 0.8)
        tangent_inc = Line(tan_start_inc, tan_end_inc, color=self.C_INC, stroke_width=3)
        dot_inc = Dot(tangent_pt_inc, color=self.C_INC, radius=0.1)

        tang_label_inc = MathTex(r"f'(x) > 0", font_size=26, color=self.C_INC).move_to(
            UP * 5.3 + LEFT * 1.5
        )
        inc_note = Text(
            "斜率为正 → 递增",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_INC,
        ).move_to(UP * 4.6 + LEFT * 1.5)

        self.play(Create(tangent_inc), FadeIn(dot_inc), run_time=0.6)
        self.play(Write(tang_label_inc), FadeIn(inc_note), run_time=0.5)

        # ── 切线在 x=-1.5（递减区，斜率<0）
        x_dec_d = -1.5
        slope_dec_d = 2 * x_dec_d
        y_dec_d = x_dec_d**2

        tan_start_dec = axes.c2p(x_dec_d - 0.8, y_dec_d - slope_dec_d * 0.8)
        tan_end_dec   = axes.c2p(x_dec_d + 0.8, y_dec_d + slope_dec_d * 0.8)
        tangent_dec = Line(tan_start_dec, tan_end_dec, color=self.C_DEC, stroke_width=3)
        dot_dec_d = Dot(axes.c2p(x_dec_d, y_dec_d), color=self.C_DEC, radius=0.1)

        tang_label_dec = MathTex(r"f'(x) < 0", font_size=26, color=self.C_DEC).move_to(
            UP * 5.3 + RIGHT * 1.5
        )
        dec_note = Text(
            "斜率为负 → 递减",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_DEC,
        ).move_to(UP * 4.6 + RIGHT * 1.5)

        self.play(Create(tangent_dec), FadeIn(dot_dec_d), run_time=0.6)
        self.play(Write(tang_label_dec), FadeIn(dec_note), run_time=0.5)

        self.wait(1.5)

        self.play(
            FadeOut(scene_title),
            FadeOut(parabola),
            FadeOut(tangent_inc), FadeOut(dot_inc),
            FadeOut(tangent_dec), FadeOut(dot_dec_d),
            FadeOut(tang_label_inc), FadeOut(inc_note),
            FadeOut(tang_label_dec), FadeOut(dec_note),
            FadeOut(axes),
            run_time=0.5,
        )

    # ════════════════════════════════════════
    # Scene 7: 总结 + 片尾
    # ════════════════════════════════════════
    def scene_7_outro(self):
        # ── 总结标题
        summary_title = Text(
            "三种判断方法",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD,
        ).move_to(UP * 5.8)
        self.play(Write(summary_title), run_time=0.6)

        # ── 三种方法卡片
        methods = [
            ("① 图像法",  "左升右降，一眼看出",     BLUE_C),
            ("② 作差法",  "f(x₁)-f(x₂) 正负判断",  self.C_INC),
            ("③ 导数法",  "f'(x)>0 增 / <0 减",    PURPLE_B),
        ]

        cards = VGroup()
        for i, (name, desc, color) in enumerate(methods):
            y_pos = UP * (4.5 - i * 1.5)
            icon = Circle(radius=0.3, fill_color=color, fill_opacity=0.9, stroke_width=0)
            name_mob = Text(name, font="Noto Sans CJK SC", font_size=26, color=WHITE)
            desc_mob = Text(desc, font="Noto Sans CJK SC", font_size=20, color=self.C_AUX)
            row = VGroup(icon, name_mob, desc_mob).arrange(RIGHT, buff=0.3).move_to(y_pos)
            cards.add(row)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)

        # ── 核心公式回顾
        formula_box_group = VGroup(
            MathTex(r"x_1<x_2 \Rightarrow f(x_1)<f(x_2)", font_size=24, color=self.C_INC),
            MathTex(r"x_1<x_2 \Rightarrow f(x_1)>f(x_2)", font_size=24, color=self.C_DEC),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 0.8)

        box_border = SurroundingRectangle(
            formula_box_group, color=GOLD, buff=0.25, corner_radius=0.15
        )

        self.play(Write(formula_box_group), Create(box_border), run_time=0.8)
        self.wait(1.5)

        # ── 淡出内容，展示片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(formula_box_group),
            FadeOut(box_border),
            run_time=0.5,
        )

        # ── 片尾作者信息放大
        outro_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 1.5)
        outro_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.C_AUX,
        ).move_to(UP * 0.6)
        outro_call = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GOLD,
        ).move_to(DOWN * 0.3)

        # 装饰：旋转星星
        stars = VGroup(*[
            Star(n=5, outer_radius=0.2, fill_color=GOLD, fill_opacity=0.9, stroke_width=0).move_to(
                np.array([2.5 * np.cos(i * TAU / 6), 2.5 * np.sin(i * TAU / 6) - 1.0, 0])
            )
            for i in range(6)
        ])

        self.play(
            Transform(self.author_info, outro_name),
            FadeIn(outro_id, shift=UP * 0.3),
            run_time=0.7,
        )
        self.play(FadeIn(outro_call, scale=1.1), run_time=0.5)
        self.play(*[FadeIn(s, scale=0.5) for s in stars], run_time=0.6)
        self.play(Rotate(stars, angle=TAU / 6, run_time=1.2))
        self.wait(1.0)
        self.play(
            FadeOut(self.author_info),
            FadeOut(outro_id),
            FadeOut(outro_call),
            FadeOut(stars),
            run_time=0.8,
        )


# ─────────────────────────────────────────
# 渲染命令:
#   预览: manim -pql function_monotonicity.py FunctionMonotonicity
#   高质量: manim -qh function_monotonicity.py FunctionMonotonicity
# ─────────────────────────────────────────
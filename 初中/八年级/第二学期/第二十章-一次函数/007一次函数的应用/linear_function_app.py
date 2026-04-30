"""
一次函数的应用 - 出租车计费问题
Linear Function Application - Taxi Fare Problem

年级: 八年级第二学期
章节: 第二十章 一次函数
内容: 一次函数的应用

TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class LinearFunctionApplication(Scene):
    """
    一次函数应用题动画
    场景: 出租车计费
    函数: y = 2x + 3  (x >= 0)
    Q1: x=5 → y=13
    Q2: y=15 → x=6
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.C_TITLE     = YELLOW
        self.C_FORMULA   = "#00FF7F"
        self.C_STEP      = "#00CED1"
        self.C_Q1        = ORANGE
        self.C_Q2        = "#FF6B6B"
        self.C_CARD_BG   = "#16213e"
        self.C_HIGHLIGHT = YELLOW

        # 初始化几何数据
        self.setup_geometry()

        # 执行场景
        self.scene_1_opening()
        self.scene_2_problem()
        self.scene_3_modeling()
        self.scene_4_graph()
        self.scene_5_solve()
        self.scene_6_outro()

    # =========================================================
    # 几何初始化
    # =========================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # 函数参数: y = 2x + 3
        self.SLOPE = 2
        self.INTERCEPT = 3

        # 问题数据
        self.X1 = 5          # Q1: 5公里
        self.Y1 = 2 * 5 + 3  # = 13 元

        self.Y2 = 15         # Q2: 15元
        self.X2 = (15 - 3) / 2  # = 6 公里

        # 坐标轴参数
        self.X_RANGE = [0, 7.5, 1]
        self.Y_RANGE = [0, 17, 2]
        self.X_LENGTH = 5.5
        self.Y_LENGTH = 5.5
        self.AXES_CENTER = DOWN * 1.2

        # 验证
        self._verify_math()

    def _verify_math(self):
        """验证数学计算"""
        y1_check = self.SLOPE * self.X1 + self.INTERCEPT
        x2_check = (self.Y2 - self.INTERCEPT) / self.SLOPE

        assert abs(y1_check - self.Y1) < 1e-10, f"Y1计算错误: {y1_check}"
        assert abs(x2_check - self.X2) < 1e-10, f"X2计算错误: {x2_check}"
        print(f"✓ 数学验证通过: Q1→({self.X1}, {self.Y1}), Q2→({self.X2}, {self.Y2})")

    # =========================================================
    # 工具方法
    # =========================================================
    def make_author_strip(self):
        """创建作者信息条"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 6.9)

    def make_card(self, width, height, position, border_color, fill_color="#16213e"):
        """创建圆角卡片背景"""
        return RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.3,
            fill_color=fill_color,
            fill_opacity=0.9,
            stroke_color=border_color,
            stroke_width=2
        ).move_to(position)

    # =========================================================
    # Scene 1: 开场 Hook
    # =========================================================
    def scene_1_opening(self):
        # 作者信息
        self.author_info = self.make_author_strip()
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 主钩子文字
        hook_line1 = Text(
            "打车要花",
            font="PingFang SC",
            font_size=56,
            color=self.C_TITLE
        ).move_to(UP * 5.5)

        hook_line2 = Text(
            "多少钱？",
            font="PingFang SC",
            font_size=56,
            color=self.C_TITLE
        ).move_to(UP * 4.7)

        self.play(Write(hook_line1), run_time=0.6)
        self.play(Write(hook_line2), run_time=0.5)

        # 出租车图形（用简单几何拼接）
        taxi_body = RoundedRectangle(
            width=3.0, height=1.3,
            corner_radius=0.2,
            fill_color="#FFD700",
            fill_opacity=1,
            stroke_color=ORANGE,
            stroke_width=2
        ).move_to(UP * 2.6)

        taxi_top = RoundedRectangle(
            width=1.8, height=0.75,
            corner_radius=0.15,
            fill_color="#FFD700",
            fill_opacity=1,
            stroke_color=ORANGE,
            stroke_width=2
        ).move_to(UP * 3.28)

        wheel_l = Circle(
            radius=0.3,
            fill_color="#333333",
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2
        ).move_to(UP * 2.02 + LEFT * 0.85)

        wheel_r = Circle(
            radius=0.3,
            fill_color="#333333",
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_width=2
        ).move_to(UP * 2.02 + RIGHT * 0.85)

        # 出租车标志
        taxi_sign = Text(
            "出 租 车",
            font="PingFang SC",
            font_size=22,
            color="#333333"
        ).move_to(taxi_body.get_center())

        taxi = VGroup(taxi_body, taxi_top, wheel_l, wheel_r, taxi_sign)

        self.play(FadeIn(taxi, scale=0.6), run_time=0.7)

        # 计价器显示
        meter_bg = self.make_card(3.0, 1.2, DOWN * 0.2 + RIGHT * 0, "#FFD700", "#1a3a1a")
        meter_label = Text("计价器", font="PingFang SC", font_size=24, color=GRAY_A).move_to(UP * 0.25)
        meter_value = Text("？ 元", font="PingFang SC", font_size=40, color=self.C_TITLE).move_to(DOWN * 0.15)

        self.play(FadeIn(meter_bg), FadeIn(meter_label), FadeIn(meter_value), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(taxi),
            FadeOut(meter_bg),
            FadeOut(meter_label),
            FadeOut(meter_value),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: 问题描述
    # =========================================================
    def scene_2_problem(self):
        # 标题
        title = Text(
            "题目条件",
            font="PingFang SC",
            font_size=40,
            color=self.C_STEP
        ).move_to(UP * 6.2)

        self.play(FadeIn(title), run_time=0.4)

        # 收费信息卡片
        info_card = self.make_card(7.5, 2.8, UP * 4.5, self.C_STEP)

        info_title = Text(
            "出租车收费标准",
            font="PingFang SC",
            font_size=28,
            color=self.C_STEP
        ).move_to(UP * 5.3)

        info_line1 = Text(
            "起步价：3 元",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.7)

        info_line2 = Text(
            "此后每公里：2 元",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.1)

        self.play(FadeIn(info_card), run_time=0.3)
        self.play(
            FadeIn(info_title),
            run_time=0.4
        )
        self.play(
            FadeIn(info_line1, shift=RIGHT * 0.3),
            run_time=0.4
        )
        self.play(
            FadeIn(info_line2, shift=RIGHT * 0.3),
            run_time=0.4
        )

        # 问题卡片
        q_card = self.make_card(7.5, 2.6, UP * 2.3, "#00FF7F", "#0a2a1a")

        q_title = Text(
            "求解问题",
            font="PingFang SC",
            font_size=28,
            color=self.C_FORMULA
        ).move_to(UP * 3.1)

        q1_text = Text(
            "① 乘坐 5 公里需要多少钱？",
            font="PingFang SC",
            font_size=24,
            color=self.C_Q1
        ).move_to(UP * 2.5)

        q2_text = Text(
            "② 付 15 元最多坐几公里？",
            font="PingFang SC",
            font_size=24,
            color=self.C_Q2
        ).move_to(UP * 1.9)

        self.play(FadeIn(q_card), run_time=0.3)
        self.play(FadeIn(q_title), run_time=0.3)
        self.play(
            FadeIn(q1_text, shift=RIGHT * 0.3),
            run_time=0.4
        )
        self.play(
            FadeIn(q2_text, shift=RIGHT * 0.3),
            run_time=0.4
        )
        self.wait(1.8)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(info_card),
            FadeOut(info_title),
            FadeOut(info_line1),
            FadeOut(info_line2),
            FadeOut(q_card),
            FadeOut(q_title),
            FadeOut(q1_text),
            FadeOut(q2_text),
            run_time=0.5
        )

    # =========================================================
    # Scene 3: 建立函数模型
    # =========================================================
    def scene_3_modeling(self):
        title = Text(
            "建立函数模型",
            font="PingFang SC",
            font_size=38,
            color="#FF6B6B"
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.5)

        # Step 1: 确定变量
        step1 = Text(
            "第一步：确定变量",
            font="PingFang SC",
            font_size=30,
            color=self.C_TITLE
        ).move_to(UP * 5.3)

        self.play(FadeIn(step1), run_time=0.4)

        var_x = Text(
            "x = 行驶路程（公里）",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.6)

        var_y = Text(
            "y = 出租车费用（元）",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.0)

        # 下划线高亮
        x_ul = Underline(var_x, color=self.C_STEP)
        y_ul = Underline(var_y, color=self.C_STEP)

        self.play(FadeIn(var_x), Create(x_ul), run_time=0.5)
        self.play(FadeIn(var_y), Create(y_ul), run_time=0.5)
        self.wait(0.4)

        # Step 2: 建立关系式
        step2 = Text(
            "第二步：建立关系式",
            font="PingFang SC",
            font_size=30,
            color=self.C_TITLE
        ).move_to(UP * 2.8)

        self.play(FadeIn(step2), run_time=0.4)

        # 推导过程
        derivation = Text(
            "费用 = 起步价 + 每公里 × 公里数",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 2.1)

        self.play(FadeIn(derivation, shift=RIGHT * 0.2), run_time=0.5)

        # 核心公式
        formula = MathTex(
            r"y = 2x + 3",
            font_size=64,
            color=self.C_FORMULA
        ).move_to(UP * 1.0)

        self.play(Write(formula), run_time=1.0)

        # 定义域说明
        domain_text = Text(
            "（x ≥ 0）",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).next_to(formula, RIGHT, buff=0.2)

        self.play(FadeIn(domain_text), run_time=0.3)

        # 高亮方框
        formula_box = SurroundingRectangle(formula, color=self.C_TITLE, buff=0.2, corner_radius=0.1)
        self.play(Create(formula_box), run_time=0.4)

        # 斜率/截距说明
        slope_arrow = Arrow(
            UP * 0.15 + RIGHT * 0.4,
            DOWN * 0.2 + LEFT * 1.8,
            color=self.C_Q1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        slope_label = Text(
            "斜率 k=2",
            font="PingFang SC",
            font_size=20,
            color=self.C_Q1
        ).move_to(DOWN * 0.5 + LEFT * 2.5)

        intercept_arrow = Arrow(
            DOWN * 0.1 + RIGHT * 1.6,
            DOWN * 0.5 + RIGHT * 2.8,
            color=self.C_Q2,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        intercept_label = Text(
            "截距 b=3",
            font="PingFang SC",
            font_size=20,
            color=self.C_Q2
        ).move_to(DOWN * 0.7 + RIGHT * 3.2)

        self.play(
            FadeIn(slope_label),
            FadeIn(intercept_label),
            run_time=0.5
        )
        self.wait(1.5)

        # 将公式缩小移到顶部，清除其他元素
        self.play(
            FadeOut(title),
            FadeOut(step1),
            FadeOut(var_x),
            FadeOut(var_y),
            FadeOut(x_ul),
            FadeOut(y_ul),
            FadeOut(step2),
            FadeOut(derivation),
            FadeOut(formula_box),
            FadeOut(slope_label),
            FadeOut(intercept_label),
            FadeOut(domain_text),
            formula.animate.scale(0.55).move_to(UP * 5.9 + LEFT * 1.5),
            run_time=0.7
        )

        self.formula_display = formula

    # =========================================================
    # Scene 4: 画函数图像
    # =========================================================
    def scene_4_graph(self):
        scene_title = Text(
            "函数图像",
            font="PingFang SC",
            font_size=36,
            color=self.C_STEP
        ).move_to(UP * 5.8 + RIGHT * 1.8)

        self.play(FadeIn(scene_title), run_time=0.4)

        # 创建坐标轴
        axes = Axes(
            x_range=self.X_RANGE,
            y_range=self.Y_RANGE,
            x_length=self.X_LENGTH,
            y_length=self.Y_LENGTH,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.18,
            },
            x_axis_config={
                "include_numbers": True,
                "numbers_to_include": [1, 2, 3, 4, 5, 6, 7],
                "font_size": 22,
                "label_direction": DOWN,
            },
            y_axis_config={
                "include_numbers": True,
                "numbers_to_include": [3, 5, 7, 9, 11, 13, 15],
                "font_size": 22,
            },
        ).move_to(self.AXES_CENTER)

        # 坐标轴标签
        x_label = Text(
            "路程 x（公里）",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(axes.x_axis.get_end(), DOWN + RIGHT, buff=0.05)

        y_label = Text(
            "费用 y（元）",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(axes), run_time=1.0)
        self.play(
            FadeIn(x_label),
            FadeIn(y_label),
            run_time=0.4
        )

        # 绘制函数 y = 2x + 3
        func_graph = axes.plot(
            lambda x: 2 * x + 3,
            x_range=[0, 6.8],
            color=self.C_FORMULA,
            stroke_width=3.5
        )

        func_label_pos = axes.c2p(4.5, 2 * 4.5 + 3)
        func_label_tex = MathTex(
            r"y = 2x + 3",
            font_size=28,
            color=self.C_FORMULA
        ).move_to(func_label_pos + RIGHT * 1.0 + DOWN * 0.3)

        self.play(Create(func_graph), run_time=1.2)
        self.play(FadeIn(func_label_tex), run_time=0.4)

        # 纵截距点 (0, 3)
        y_intercept_pos = axes.c2p(0, 3)
        y_intercept_dot = Dot(y_intercept_pos, color=self.C_TITLE, radius=0.1)
        y_intercept_label = MathTex(
            r"(0,\,3)",
            font_size=26,
            color=self.C_TITLE
        ).next_to(y_intercept_dot, RIGHT, buff=0.15)

        self.play(
            FadeIn(y_intercept_dot, scale=0.5),
            run_time=0.4
        )
        self.play(FadeIn(y_intercept_label), run_time=0.3)

        self.wait(0.8)

        # 保存引用供下一场景使用
        self.axes = axes
        self.func_graph = func_graph
        self.func_label_tex = func_label_tex
        self.y_intercept_dot = y_intercept_dot
        self.y_intercept_label = y_intercept_label
        self.x_label = x_label
        self.y_label = y_label
        self.scene4_title = scene_title

    # =========================================================
    # Scene 5: 解题
    # =========================================================
    def scene_5_solve(self):
        # ── 问题① ──────────────────────────────────────────
        q1_banner = Text(
            "① 乘坐 5 公里  →  费用？",
            font="PingFang SC",
            font_size=28,
            color=self.C_Q1
        ).move_to(UP * 5.2)

        self.play(
            FadeOut(self.scene4_title),
            FadeIn(q1_banner, shift=DOWN * 0.2),
            run_time=0.4
        )

        # x=5 的坐标点
        p_x5_on_axis = self.axes.c2p(self.X1, 0)
        p_intersection_q1 = self.axes.c2p(self.X1, self.Y1)
        p_y13_on_axis = self.axes.c2p(0, self.Y1)

        # 竖向虚线 x=5
        v_line_q1 = DashedLine(
            p_x5_on_axis,
            p_intersection_q1,
            color=self.C_Q1,
            stroke_width=2.5,
            dash_length=0.12
        )
        # 横向虚线 y=13
        h_line_q1 = DashedLine(
            p_intersection_q1,
            p_y13_on_axis,
            color=self.C_Q1,
            stroke_width=2.5,
            dash_length=0.12
        )

        x5_dot = Dot(p_x5_on_axis, color=self.C_Q1, radius=0.09)
        x5_label = MathTex(r"5", font_size=28, color=self.C_Q1).next_to(x5_dot, DOWN, buff=0.12)

        y13_dot = Dot(p_y13_on_axis, color=self.C_Q1, radius=0.09)
        y13_label = MathTex(r"13", font_size=28, color=self.C_Q1).next_to(y13_dot, LEFT, buff=0.12)

        intersection_q1_dot = Dot(p_intersection_q1, color=self.C_Q1, radius=0.13)

        self.play(FadeIn(x5_dot), FadeIn(x5_label), run_time=0.3)
        self.play(Create(v_line_q1), run_time=0.6)
        self.play(FadeIn(intersection_q1_dot, scale=0.5), run_time=0.3)
        self.play(Create(h_line_q1), run_time=0.6)
        self.play(FadeIn(y13_dot), FadeIn(y13_label), run_time=0.3)

        # 计算过程
        calc_q1_bg = self.make_card(7.0, 1.6, DOWN * 5.5, self.C_Q1, "#1a1a0a")
        calc_q1 = MathTex(
            r"y = 2 \times 5 + 3 = 13",
            font_size=36,
            color=self.C_Q1
        ).move_to(DOWN * 5.4)
        answer_q1 = Text(
            "需要 13 元！",
            font="PingFang SC",
            font_size=28,
            color=self.C_FORMULA
        ).move_to(DOWN * 6.2)

        self.play(FadeIn(calc_q1_bg), Write(calc_q1), run_time=0.7)
        self.play(FadeIn(answer_q1, scale=1.1), run_time=0.4)
        self.wait(1.5)

        # 清除 Q1 内容
        self.play(
            FadeOut(q1_banner),
            FadeOut(v_line_q1),
            FadeOut(h_line_q1),
            FadeOut(x5_dot),
            FadeOut(x5_label),
            FadeOut(y13_dot),
            FadeOut(y13_label),
            FadeOut(intersection_q1_dot),
            FadeOut(calc_q1_bg),
            FadeOut(calc_q1),
            FadeOut(answer_q1),
            run_time=0.5
        )

        # ── 问题② ──────────────────────────────────────────
        q2_banner = Text(
            "② 付 15 元  →  最多几公里？",
            font="PingFang SC",
            font_size=28,
            color=self.C_Q2
        ).move_to(UP * 5.2)

        self.play(FadeIn(q2_banner, shift=DOWN * 0.2), run_time=0.4)

        # y=15 的坐标点
        p_y15_on_axis = self.axes.c2p(0, self.Y2)
        p_intersection_q2 = self.axes.c2p(self.X2, self.Y2)
        p_x6_on_axis = self.axes.c2p(self.X2, 0)

        # 横向虚线 y=15
        h_line_q2 = DashedLine(
            p_y15_on_axis,
            p_intersection_q2,
            color=self.C_Q2,
            stroke_width=2.5,
            dash_length=0.12
        )
        # 竖向虚线 x=6
        v_line_q2 = DashedLine(
            p_intersection_q2,
            p_x6_on_axis,
            color=self.C_Q2,
            stroke_width=2.5,
            dash_length=0.12
        )

        y15_dot = Dot(p_y15_on_axis, color=self.C_Q2, radius=0.09)
        y15_label = MathTex(r"15", font_size=28, color=self.C_Q2).next_to(y15_dot, LEFT, buff=0.12)

        x6_dot = Dot(p_x6_on_axis, color=self.C_Q2, radius=0.09)
        x6_label = MathTex(r"6", font_size=28, color=self.C_Q2).next_to(x6_dot, DOWN, buff=0.12)

        intersection_q2_dot = Dot(p_intersection_q2, color=self.C_Q2, radius=0.13)

        self.play(FadeIn(y15_dot), FadeIn(y15_label), run_time=0.3)
        self.play(Create(h_line_q2), run_time=0.6)
        self.play(FadeIn(intersection_q2_dot, scale=0.5), run_time=0.3)
        self.play(Create(v_line_q2), run_time=0.6)
        self.play(FadeIn(x6_dot), FadeIn(x6_label), run_time=0.3)

        # 计算过程
        calc_q2_bg = self.make_card(7.5, 2.4, DOWN * 5.4, self.C_Q2, "#1a0a0a")
        calc_q2_line1 = MathTex(
            r"15 = 2x + 3",
            font_size=34,
            color=self.C_Q2
        ).move_to(DOWN * 4.9)
        calc_q2_line2 = MathTex(
            r"x = 6",
            font_size=38,
            color=self.C_FORMULA
        ).move_to(DOWN * 5.7)

        answer_q2 = Text(
            "最多乘坐 6 公里！",
            font="PingFang SC",
            font_size=28,
            color=self.C_FORMULA
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(calc_q2_bg), Write(calc_q2_line1), run_time=0.6)
        self.play(Write(calc_q2_line2), run_time=0.5)
        self.play(FadeIn(answer_q2, scale=1.1), run_time=0.4)
        self.wait(1.5)

        # 清除全部图表内容
        self.play(
            FadeOut(q2_banner),
            FadeOut(h_line_q2),
            FadeOut(v_line_q2),
            FadeOut(y15_dot),
            FadeOut(y15_label),
            FadeOut(x6_dot),
            FadeOut(x6_label),
            FadeOut(intersection_q2_dot),
            FadeOut(calc_q2_bg),
            FadeOut(calc_q2_line1),
            FadeOut(calc_q2_line2),
            FadeOut(answer_q2),
            FadeOut(self.axes),
            FadeOut(self.func_graph),
            FadeOut(self.func_label_tex),
            FadeOut(self.y_intercept_dot),
            FadeOut(self.y_intercept_label),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.formula_display),
            run_time=0.8
        )

    # =========================================================
    # Scene 6: 总结 + 片尾
    # =========================================================
    def scene_6_outro(self):
        # 总结标题
        summary_title = Text(
            "解题四步法",
            font="PingFang SC",
            font_size=44,
            color=self.C_TITLE
        ).move_to(UP * 5.5)

        self.play(Write(summary_title), run_time=0.6)

        # 四步卡片
        step_data = [
            ("① 确定变量", "找自变量 x 和因变量 y", self.C_STEP),
            ("② 建立模型", "写出 y = kx + b", self.C_FORMULA),
            ("③ 确定定义域", "结合实际确定范围", self.C_Q1),
            ("④ 利用图像求解", "代入或读取图像", self.C_Q2),
        ]

        step_vgroups = []
        for i, (step_name, step_desc, color) in enumerate(step_data):
            y_pos = UP * (4.2 - i * 1.3)

            card_bg = self.make_card(7.5, 1.1, y_pos, color, "#16213e")
            step_num_text = Text(
                step_name,
                font="PingFang SC",
                font_size=24,
                color=color
            ).move_to(y_pos + LEFT * 1.8)
            step_desc_text = Text(
                step_desc,
                font="PingFang SC",
                font_size=20,
                color=GRAY_A
            ).move_to(y_pos + RIGHT * 1.0)

            card_group = VGroup(card_bg, step_num_text, step_desc_text)
            step_vgroups.append(card_group)

            # 从左侧滑入
            card_group.shift(LEFT * 10)
            self.play(
                card_group.animate.shift(RIGHT * 10),
                run_time=0.35
            )

        # 核心公式展示
        core_formula = MathTex(
            r"y = kx + b \quad (k \neq 0)",
            font_size=44,
            color=self.C_FORMULA
        ).move_to(DOWN * 1.5)

        formula_highlight = SurroundingRectangle(
            core_formula, color=self.C_FORMULA, buff=0.2, corner_radius=0.15
        )

        formula_note = Text(
            "一次函数通用模型",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(core_formula, DOWN, buff=0.2)

        self.play(Write(core_formula), run_time=0.8)
        self.play(Create(formula_highlight), run_time=0.4)
        self.play(FadeIn(formula_note), run_time=0.3)
        self.wait(1.0)

        # 淡出总结内容
        all_steps_group = VGroup(*step_vgroups)
        self.play(
            FadeOut(summary_title),
            FadeOut(all_steps_group),
            FadeOut(core_formula),
            FadeOut(formula_highlight),
            FadeOut(formula_note),
            run_time=0.6
        )

        # ── 片尾作者信息 ──
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1.2)

        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1).move_to(UP * 0.6)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.C_TITLE
        ).move_to(ORIGIN)

        # 装饰：函数符号背景
        deco_formula1 = MathTex(r"y = kx + b", font_size=30, color="#333355", fill_opacity=0.5).move_to(DOWN * 1.5 + LEFT * 1.5)
        deco_formula2 = MathTex(r"f(x) = ax + c", font_size=24, color="#333355", fill_opacity=0.4).move_to(DOWN * 2.5 + RIGHT * 1.2)

        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)
        self.play(
            FadeIn(deco_formula1, shift=UP * 0.3),
            FadeIn(deco_formula2, shift=UP * 0.3),
            run_time=0.5
        )
        self.wait(2.0)

        # 最终淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(divider),
            FadeOut(follow_text),
            FadeOut(deco_formula1),
            FadeOut(deco_formula2),
            run_time=1.0
        )


# ============================================================
# 渲染命令:
# manim -pql linear_function_app.py LinearFunctionApplication  # 快速预览
# manim -qh linear_function_app.py LinearFunctionApplication   # 高质量
# ============================================================
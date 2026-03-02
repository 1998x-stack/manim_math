"""
含绝对值不等式 - 高一数学教学动画
TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色配置 =====
BG_COLOR = "#1a1a2e"
COLOR_RED = "#e74c3c"
COLOR_BLUE = "#3498db"
COLOR_GREEN = "#2ecc71"
COLOR_PURPLE = "#9b59b6"
COLOR_ORANGE = "#f39c12"
FONT_CN = "Noto Sans CJK SC"


class AbsoluteValueInequalities(Scene):
    """含绝对值不等式 - 完整教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.setup_data()
        self.scene1_hook()
        self.scene2_abs_meaning()
        self.scene3_less_than()
        self.scene4_greater_than()
        self.scene5_example()
        self.scene6_outro()

    # ─────────────────────────────────────────
    #  数据初始化
    # ─────────────────────────────────────────
    def setup_data(self):
        """预计算所有数轴参数"""
        self.NL_Y = 1.5          # 数轴 y 坐标（主内容区中部）
        self.NL_SCALE = 0.72     # 逻辑单位 → 屏幕单位 比例
        self.NL_RANGE = [-5, 5]  # 显示范围

        # 将数轴逻辑坐标转为 Manim 屏幕坐标
        def to_screen(x):
            return np.array([x * self.NL_SCALE, self.NL_Y, 0])

        self.ts = to_screen
        # 验证关键点不超界
        assert abs(5 * self.NL_SCALE) <= 4.0, "数轴端点超界"
        assert abs(-5 * self.NL_SCALE) <= 4.0, "数轴端点超界"
        assert abs(5 * self.NL_SCALE) <= 4.0, "右端点5*0.72=3.6, OK"

    # ─────────────────────────────────────────
    #  工具函数
    # ─────────────────────────────────────────
    def make_number_line(self, x_range=None, y=None, scale=None):
        """创建标准数轴"""
        if x_range is None:
            x_range = self.NL_RANGE
        if y is None:
            y = self.NL_Y
        if scale is None:
            scale = self.NL_SCALE

        nl = NumberLine(
            x_range=[x_range[0], x_range[1], 1],
            length=(x_range[1] - x_range[0]) * scale,
            include_numbers=True,
            numbers_to_include=list(range(x_range[0], x_range[1] + 1)),
            label_direction=DOWN,
            font_size=20,
            color=WHITE,
            tick_size=0.08,
            numbers_with_elongated_ticks=[0],
        ).move_to([0, y, 0])
        return nl

    def highlight_interval(self, nl, x_start, x_end, color=COLOR_GREEN, stroke_width=8):
        """在数轴上高亮一段区间"""
        p_start = nl.n2p(x_start)
        p_end = nl.n2p(x_end)
        line = Line(p_start, p_end, color=color, stroke_width=stroke_width)
        return line

    def make_open_dot(self, nl, x, color=COLOR_GREEN):
        """空心圆（开区间端点）"""
        pos = nl.n2p(x)
        return Circle(radius=0.08, color=color, stroke_width=3).move_to(pos).set_fill(BG_COLOR, opacity=1)

    def make_section_title(self, text, color=GOLD, y=5.5):
        return Text(text, font=FONT_CN, font_size=36, color=color).move_to([0, y, 0])

    def make_body_text(self, text, color=GRAY_A, y=-4.5, font_size=24):
        return Text(text, font=FONT_CN, font_size=font_size, color=color).move_to([0, y, 0])

    def fade_out_all(self, *exclude, run_time=0.5):
        """淡出场景中除 exclude 外的所有物件"""
        to_remove = [m for m in self.mobjects if m not in exclude]
        if to_remove:
            self.play(*[FadeOut(m) for m in to_remove], run_time=run_time)

    # ─────────────────────────────────────────
    #  Scene 1: 开场钩子
    # ─────────────────────────────────────────
    def scene1_hook(self):
        # 作者信息 (y=6.8, 避免溢出)
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT_CN, font_size=20, color=GRAY_B
        ).move_to([0, 6.8, 0])
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text("你能解这道题吗？", font=FONT_CN, font_size=40, color=GOLD).move_to([0, 5.2, 0])
        self.play(Write(hook), run_time=0.8)

        # 主公式
        problem = MathTex(
            r"\lvert x - 2 \rvert < 3",
            font_size=72, color=WHITE
        ).move_to([0, 3.5, 0])
        self.play(Write(problem), run_time=1.0)
        self.wait(1.2)

        # 提示
        hint = Text("先来理解绝对值的几何含义", font=FONT_CN, font_size=26, color=COLOR_BLUE).move_to([0, -4.5, 0])
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(hook), FadeOut(problem), FadeOut(hint), run_time=0.5)

    # ─────────────────────────────────────────
    #  Scene 2: 绝对值几何意义
    # ─────────────────────────────────────────
    def scene2_abs_meaning(self):
        title = self.make_section_title("绝对值的几何意义")
        self.play(Write(title), run_time=0.6)

        # 数轴
        nl = self.make_number_line()
        self.play(Create(nl), run_time=0.8)

        # 原点标记
        O_dot = Dot(nl.n2p(0), radius=0.1, color=YELLOW)
        O_label = Text("O", font=FONT_CN, font_size=24, color=YELLOW).next_to(O_dot, UP, buff=0.15)
        self.play(FadeIn(O_dot), Write(O_label), run_time=0.4)

        # 点 P 在 x=3
        P_pos = nl.n2p(3)
        P_dot = Dot(P_pos, radius=0.12, color=COLOR_RED)
        P_label = MathTex(r"x=3", font_size=28, color=COLOR_RED).next_to(P_dot, UP, buff=0.18)
        self.play(FadeIn(P_dot, scale=0.5), Write(P_label), run_time=0.5)

        # 双向箭头表示距离
        arrow = DoubleArrow(nl.n2p(0), nl.n2p(3), buff=0, color=COLOR_GREEN, stroke_width=4)
        arrow.shift(UP * 0.5)
        dist_label = MathTex(r"\lvert x \rvert = 3", font_size=32, color=COLOR_GREEN).move_to([1.5 * self.NL_SCALE, self.NL_Y + 0.9, 0])

        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(Write(dist_label), run_time=0.5)
        self.wait(0.5)

        # 点移到 x=-3
        P_dot_neg = Dot(nl.n2p(-3), radius=0.12, color=COLOR_RED)
        P_label_neg = MathTex(r"x=-3", font_size=28, color=COLOR_RED).next_to(P_dot_neg, UP, buff=0.18)
        arrow_neg = DoubleArrow(nl.n2p(-3), nl.n2p(0), buff=0, color=COLOR_GREEN, stroke_width=4)
        arrow_neg.shift(UP * 0.5)
        dist_label_neg = MathTex(r"\lvert x \rvert = 3", font_size=32, color=COLOR_GREEN).move_to([-1.5 * self.NL_SCALE, self.NL_Y + 0.9, 0])

        self.play(
            ReplacementTransform(P_dot, P_dot_neg),
            ReplacementTransform(P_label, P_label_neg),
            ReplacementTransform(arrow, arrow_neg),
            ReplacementTransform(dist_label, dist_label_neg),
            run_time=0.8
        )
        self.wait(0.3)

        # 总结文字
        summary = Text("绝对值 = 数到原点的距离", font=FONT_CN, font_size=28, color=YELLOW).move_to([0, -3.8, 0])
        box = SurroundingRectangle(summary, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(summary), Create(box), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(nl), FadeOut(O_dot), FadeOut(O_label),
            FadeOut(P_dot_neg), FadeOut(P_label_neg),
            FadeOut(arrow_neg), FadeOut(dist_label_neg),
            FadeOut(summary), FadeOut(box),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    #  Scene 3: |x| < a 型
    # ─────────────────────────────────────────
    def scene3_less_than(self):
        title = self.make_section_title("|x| < a 型不等式", color=COLOR_GREEN)
        self.play(Write(title), run_time=0.6)

        # 主公式
        formula = MathTex(r"\lvert x \rvert < 3", font_size=52, color=WHITE).move_to([0, 4.4, 0])
        self.play(Write(formula), run_time=0.7)

        # 数轴
        nl = self.make_number_line()
        self.play(Create(nl), run_time=0.7)

        # 含义文字
        meaning = Text("距离原点小于 3 的 x 的范围", font=FONT_CN, font_size=24, color=GRAY_A).move_to([0, -3.8, 0])
        self.play(FadeIn(meaning), run_time=0.4)

        # 标记 ±3
        for x, lbl, side in [(-3, r"-3", UP), (3, r"3", UP)]:
            d = Dot(nl.n2p(x), radius=0.1, color=COLOR_RED)
            self.play(FadeIn(d, scale=0.5), run_time=0.25)

        self.wait(0.3)

        # 高亮区间 (-3, 3)
        interval = self.highlight_interval(nl, -3, 3, color=COLOR_GREEN, stroke_width=10)
        dot_l = self.make_open_dot(nl, -3, COLOR_GREEN)
        dot_r = self.make_open_dot(nl, 3, COLOR_GREEN)

        self.play(Create(interval), run_time=0.6)
        self.play(FadeIn(dot_l), FadeIn(dot_r), run_time=0.3)
        self.wait(0.4)

        # 转化公式
        equiv1 = MathTex(r"-3 < x < 3", font_size=44, color=COLOR_GREEN).move_to([0, -4.8, 0])
        self.play(FadeOut(meaning), Write(equiv1), run_time=0.6)
        self.wait(0.5)

        # 通用公式框
        general = VGroup(
            MathTex(r"\lvert x \rvert > a \;\Longleftrightarrow\; x < -a", font_size=30, color=YELLOW),
            Text("或", font="Noto Sans CJK SC", font_size=30, color=YELLOW),
            MathTex(r"x > a", font_size=30, color=YELLOW),
        ).arrange(RIGHT, buff=0.15).move_to([0, -6.0, 0])
        note = Text("(a > 0)", font=FONT_CN, font_size=22, color=GRAY_A).next_to(general, DOWN, buff=0.2)
        box_g = SurroundingRectangle(general, color=YELLOW, buff=0.2, corner_radius=0.1)

        self.play(Write(general), run_time=0.7)
        self.play(Create(box_g), FadeIn(note), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(formula), FadeOut(nl),
            FadeOut(interval), FadeOut(dot_l), FadeOut(dot_r),
            FadeOut(equiv1), FadeOut(general), FadeOut(box_g), FadeOut(note),
            FadeOut(boundary_dots),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    #  Scene 4: |x| > a 型
    # ─────────────────────────────────────────
    def scene4_greater_than(self):
        title = self.make_section_title("|x| > a 型不等式", color=COLOR_RED)
        self.play(Write(title), run_time=0.6)

        formula = MathTex(r"\lvert x \rvert > 3", font_size=52, color=WHITE).move_to([0, 4.4, 0])
        self.play(Write(formula), run_time=0.7)

        nl = self.make_number_line()
        self.play(Create(nl), run_time=0.7)

        meaning = Text("距离原点大于 3 的 x 的范围", font=FONT_CN, font_size=24, color=GRAY_A).move_to([0, -3.8, 0])
        self.play(FadeIn(meaning), run_time=0.4)
        self.wait(0.3)

        # 左段 x < -3
        left_end = nl.n2p(-5)
        neg3_pos = nl.n2p(-3)

        left_seg = Line(left_end, neg3_pos, color=COLOR_RED, stroke_width=10)
        dot_neg3 = self.make_open_dot(nl, -3, COLOR_RED)
        arrow_left = Arrow(neg3_pos + LEFT * 0.1, left_end + LEFT * 0.2, buff=0, color=COLOR_RED, stroke_width=4)

        self.play(Create(left_seg), FadeIn(dot_neg3), run_time=0.6)

        # 右段 x > 3
        pos3_pos = nl.n2p(3)
        right_end = nl.n2p(5)

        right_seg = Line(pos3_pos, right_end, color=COLOR_RED, stroke_width=10)
        dot_pos3 = self.make_open_dot(nl, 3, COLOR_RED)
        arrow_right = Arrow(pos3_pos + RIGHT * 0.1, right_end + RIGHT * 0.2, buff=0, color=COLOR_RED, stroke_width=4)

        self.play(Create(right_seg), FadeIn(dot_pos3), run_time=0.6)
        self.wait(0.4)

        # 转化公式
        equiv = VGroup(
            MathTex(r"x < -3", font_size=38, color=COLOR_RED),
            Text("或", font="Noto Sans CJK SC", font_size=38, color=COLOR_RED),
            MathTex(r"x > 3", font_size=38, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.3).move_to([0, -4.8, 0])
        self.play(FadeOut(meaning), Write(equiv), run_time=0.6)
        self.wait(0.5)

        # 通用公式
        general = MathTex(
            r"\lvert x \rvert > a \;\Longleftrightarrow\; x < -a \;\text{or}\; x > a",
            font_size=30, color=YELLOW
        ).move_to([0, -6.0, 0])
        note = Text("(a > 0)", font=FONT_CN, font_size=22, color=GRAY_A).next_to(general, DOWN, buff=0.2)
        box_g = SurroundingRectangle(general, color=YELLOW, buff=0.2, corner_radius=0.1)

        self.play(Write(general), run_time=0.7)
        self.play(Create(box_g), FadeIn(note), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(formula), FadeOut(nl),
            FadeOut(left_seg), FadeOut(right_seg),
            FadeOut(dot_neg3), FadeOut(dot_pos3),
            FadeOut(equiv), FadeOut(general), FadeOut(box_g), FadeOut(note),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    #  Scene 5: 例题解析 |x-2| < 3
    # ─────────────────────────────────────────
    def scene5_example(self):
        title = self.make_section_title("例题解析", color=GOLD)
        self.play(Write(title), run_time=0.5)

        # 例题
        prob = VGroup(
            Text("解：", font="Noto Sans CJK SC", font_size=48, color=WHITE),
            MathTex(r"\lvert x - 2 \rvert < 3", font_size=48, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to([0, 4.4, 0])
        self.play(Write(prob), run_time=0.8)
        self.wait(0.4)

        # 方法一标题
        method1_title = Text("方法一：公式法", font=FONT_CN, font_size=28, color=COLOR_BLUE).move_to([0, 3.3, 0])
        self.play(FadeIn(method1_title), run_time=0.4)

        # 步骤1: 利用 |x| < a ⟺ -a < x < a
        step0 = MathTex(
            r"\lvert x - 2 \rvert < 3",
            font_size=38, color=WHITE
        ).move_to([0, 2.4, 0])
        self.play(Write(step0), run_time=0.5)

        arrow_down = Arrow(UP * 0.3, DOWN * 0.3, buff=0, color=GRAY_A).move_to([0, 1.7, 0])
        self.play(GrowArrow(arrow_down), run_time=0.3)

        # 步骤2: -3 < x-2 < 3
        step1 = MathTex(
            r"-3 < x - 2 < 3",
            font_size=38, color=COLOR_GREEN
        ).move_to([0, 1.0, 0])
        hint1 = Text("套公式：-a < x-2 < a", font=FONT_CN, font_size=20, color=GRAY_B).next_to(step1, RIGHT, buff=0.3)
        self.play(Write(step1), run_time=0.6)
        self.play(FadeIn(hint1), run_time=0.3)
        self.wait(0.5)

        arrow_down2 = Arrow(UP * 0.3, DOWN * 0.3, buff=0, color=GRAY_A).move_to([0, 0.3, 0])
        self.play(GrowArrow(arrow_down2), run_time=0.3)

        # 步骤3: 各加2
        step2 = MathTex(
            r"-1 < x < 5",
            font_size=44, color=COLOR_RED
        ).move_to([0, -0.4, 0])
        hint2 = Text("各部分 +2", font=FONT_CN, font_size=20, color=GRAY_B).next_to(step2, RIGHT, buff=0.3)
        self.play(Write(step2), run_time=0.6)
        self.play(FadeIn(hint2), run_time=0.3)
        self.wait(0.5)

        # 结论框
        result_box = SurroundingRectangle(step2, color=COLOR_RED, buff=0.2, corner_radius=0.1)
        self.play(Create(result_box), run_time=0.4)
        self.wait(0.8)

        # 方法二: 数轴几何法
        method2_title = Text("方法二：几何法", font=FONT_CN, font_size=28, color=COLOR_PURPLE).move_to([0, -1.5, 0])
        self.play(FadeIn(method2_title), run_time=0.4)

        geo_explain = Text("|x-2| = x 到 2 的距离", font=FONT_CN, font_size=24, color=GRAY_A).move_to([0, -2.3, 0])
        self.play(FadeIn(geo_explain), run_time=0.4)

        # 数轴（缩小，放在底部）
        nl_y = -3.5
        nl = NumberLine(
            x_range=[-1, 6, 1],
            length=5.6,
            include_numbers=True,
            numbers_to_include=[-1, 0, 2, 5],
            label_direction=DOWN,
            font_size=18,
            color=WHITE,
            tick_size=0.07,
        ).move_to([0, nl_y, 0])
        self.play(Create(nl), run_time=0.6)

        # 标记点 2 为中心
        p2 = Dot(nl.n2p(2), radius=0.1, color=YELLOW)
        p2_label = MathTex(r"2", font_size=26, color=YELLOW).next_to(p2, UP, buff=0.15)
        self.play(FadeIn(p2), Write(p2_label), run_time=0.3)

        # 高亮区间 (-1, 5) 以 2 为中心 ±3
        interval_geo = Line(nl.n2p(-1), nl.n2p(5), color=COLOR_GREEN, stroke_width=10)
        dot_l = self.make_open_dot(nl, -1, COLOR_GREEN)
        dot_r = self.make_open_dot(nl, 5, COLOR_GREEN)

        # 双向箭头显示 ±3
        arr_left = DoubleArrow(nl.n2p(2), nl.n2p(-1), buff=0, color=COLOR_ORANGE, stroke_width=3).shift(UP * 0.45)
        arr_right = DoubleArrow(nl.n2p(2), nl.n2p(5), buff=0, color=COLOR_ORANGE, stroke_width=3).shift(UP * 0.45)
        lbl_left = MathTex(r"3", font_size=20, color=COLOR_ORANGE).move_to(nl.n2p(-0.5) + UP * 0.72)
        lbl_right = MathTex(r"3", font_size=20, color=COLOR_ORANGE).move_to(nl.n2p(3.5) + UP * 0.72)

        self.play(Create(interval_geo), FadeIn(dot_l), FadeIn(dot_r), run_time=0.5)
        self.play(GrowArrow(arr_left), GrowArrow(arr_right), run_time=0.5)
        self.play(Write(lbl_left), Write(lbl_right), run_time=0.3)

        geo_result = Text("以 2 为中心，左右各延伸 3", font=FONT_CN, font_size=22, color=GRAY_A).move_to([0, -5.3, 0])
        self.play(FadeIn(geo_result), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(prob), FadeOut(method1_title),
            FadeOut(step0), FadeOut(step1), FadeOut(step2),
            FadeOut(hint1), FadeOut(hint2),
            FadeOut(arrow_down), FadeOut(arrow_down2), FadeOut(result_box),
            FadeOut(method2_title), FadeOut(geo_explain),
            FadeOut(nl), FadeOut(p2), FadeOut(p2_label),
            FadeOut(interval_geo), FadeOut(dot_l), FadeOut(dot_r),
            FadeOut(arr_left), FadeOut(arr_right), FadeOut(lbl_left), FadeOut(lbl_right),
            FadeOut(geo_result),
            run_time=0.6
        )

    # ─────────────────────────────────────────
    #  Scene 6: 总结 + 片尾
    # ─────────────────────────────────────────
    def scene6_outro(self):
        # 两个公式卡片
        card_title = Text("核心公式总结", font=FONT_CN, font_size=36, color=GOLD).move_to([0, 5.5, 0])
        self.play(Write(card_title), run_time=0.5)

        # 卡片1: < 型
        card1_bg = RoundedRectangle(width=7.5, height=1.6, corner_radius=0.2,
                                     fill_color="#0d2137", fill_opacity=1,
                                     stroke_color=COLOR_GREEN, stroke_width=2)
        card1_bg.move_to([0, 4.0, 0])

        f1 = MathTex(
            r"\lvert x \rvert < a \;\Longleftrightarrow\; -a < x < a",
            font_size=30, color=COLOR_GREEN
        ).move_to([0, 4.2, 0])
        t1 = Text("(a > 0)  解集：开区间", font=FONT_CN, font_size=20, color=GRAY_A).move_to([0, 3.7, 0])

        self.play(FadeIn(card1_bg), run_time=0.3)
        self.play(Write(f1), FadeIn(t1), run_time=0.6)

        # 卡片2: > 型
        card2_bg = RoundedRectangle(width=7.5, height=1.6, corner_radius=0.2,
                                     fill_color="#1e0d12", fill_opacity=1,
                                     stroke_color=COLOR_RED, stroke_width=2)
        card2_bg.move_to([0, 2.3, 0])

        f2 = VGroup(
            MathTex(r"\lvert x \rvert > a \;\Longleftrightarrow\; x < -a", font_size=28, color=COLOR_RED),
            Text("或", font="Noto Sans CJK SC", font_size=28, color=COLOR_RED),
            MathTex(r"x > a", font_size=28, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.15).move_to([0, 2.5, 0])
        t2 = Text("(a > 0)  解集：两段", font=FONT_CN, font_size=20, color=GRAY_A).move_to([0, 2.0, 0])

        self.play(FadeIn(card2_bg), run_time=0.3)
        self.play(Write(f2), FadeIn(t2), run_time=0.6)

        # 关键技巧
        tip = Text("技巧：把 |x-a|<b 看成\n'x 到 a 的距离 < b'", font=FONT_CN, font_size=24, color=YELLOW).move_to([0, 0.5, 0])
        tip_box = SurroundingRectangle(tip, color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(tip), Create(tip_box), run_time=0.6)
        self.wait(1.5)

        # 作者信息放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=38, color=WHITE
        ).move_to([0, -1.5, 0])
        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=28, color=GRAY_B
        ).move_to([0, -2.3, 0])

        follow = Text("关注我，获得更多数学技巧！", font=FONT_CN, font_size=30, color=COLOR_GREEN).move_to([0, -3.5, 0])
        follow_box = SurroundingRectangle(follow, color=COLOR_GREEN, buff=0.2, corner_radius=0.1)

        self.play(
            FadeOut(self.author),
            FadeIn(author_big, shift=DOWN * 0.2),
            run_time=0.5
        )
        self.play(FadeIn(author_id), run_time=0.3)
        self.play(FadeIn(follow), Create(follow_box), run_time=0.5)

        # 装饰：三颗星星闪烁
        stars = VGroup(*[
            Star(n=5, outer_radius=0.25, color=YELLOW, fill_opacity=0.9).move_to(
                [np.cos(i * 2 * PI / 3) * 3.0, -5.2 + np.sin(i * 2 * PI / 3) * 0.4, 0]
            )
            for i in range(3)
        ])
        self.play(*[FadeIn(s, scale=0.5) for s in stars], run_time=0.5)
        self.play(stars.animate.set_color(GOLD), run_time=0.5)
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


# ─────────────────────────────────────────
#  渲染命令
# ─────────────────────────────────────────
# 快速预览:  manim -pql abs_inequalities.py AbsoluteValueInequalities
# 高质量:    manim -qh  abs_inequalities.py AbsoluteValueInequalities
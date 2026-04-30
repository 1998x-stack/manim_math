"""
指数函数 - Exponential Functions Teaching Animation
高一数学第四章
manim -qh exponential_function.py ExponentialFunctions

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

坐标轴: x_range=[-3,3], y_range=[-0.5, 5.5]
3^x 绘图范围限制到 x ≤ 1.45 (y≈4.95 不超出)
"""
from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ExponentialFunctions(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"

        self.C_A2   = "#e74c3c"   # y=2^x 红
        self.C_A3   = "#3498db"   # y=3^x 蓝
        self.C_AH   = "#f39c12"   # y=(1/2)^x 橙
        self.C_ATH  = "#2ecc71"   # y=(1/3)^x 绿
        self.C_PT   = YELLOW
        self.C_ASY  = GRAY_B
        self.C_RULE = "#f1c40f"
        self.C_AUX  = GRAY_B

        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_increasing()
        self.scene_4_decreasing()
        self.scene_5_compare()
        self.scene_6_properties()
        self.scene_7_outro()

    # ═══════════════════════════════════════════
    def setup_geometry(self):
        self.AX_X  = [-3, 3, 1]
        self.AX_Y  = [-0.5, 5.5, 1]
        self.AX_XL = 6.5
        self.AX_YL = 5.0
        self.AX_CTR = np.array([0.0, 2.0, 0.0])

        # 各函数绘图 x 范围（限制在 y_range 内）
        self.PLOT_RANGES = {
            "a2":   (-3.0,  2.32),   # 2^2.32 ≈ 5.0
            "a3":   (-3.0,  1.45),   # 3^1.45 ≈ 4.95
            "half": (-2.32, 3.0),    # (1/2)^(-2.32) ≈ 5.0
            "third":(-1.45, 3.0),    # (1/3)^(-1.45) ≈ 4.95
        }
        self.FUNC_MAP = {
            "a2":    lambda x: 2.0**x,
            "a3":    lambda x: 3.0**x,
            "half":  lambda x: 0.5**x,
            "third": lambda x: (1/3)**x,
        }

    def _make_axes(self):
        return Axes(
            x_range=self.AX_X,
            y_range=self.AX_Y,
            x_length=self.AX_XL,
            y_length=self.AX_YL,
            axis_config={
                "color": self.C_AUX,
                "include_numbers": True,
                "numbers_to_include": [-2, -1, 0, 1, 2],
                "font_size": 18,
                "tip_length": 0.2,
            },
        ).move_to(self.AX_CTR)

    def _plot(self, axes, key, color, stroke_width=3.0):
        xr = self.PLOT_RANGES[key]
        return axes.plot(
            self.FUNC_MAP[key],
            x_range=[xr[0], xr[1]],
            color=color,
            stroke_width=stroke_width,
        )

    # ═══════════════════════════════════════════
    # Scene 1: 开场
    # ═══════════════════════════════════════════
    def scene_1_opening(self):
        opening_group = VGroup()
        
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="PingFang SC", font_size=20, color=self.C_AUX,
        ).move_to(UP * 7.2)
        opening_group.add(self.author)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        title = Text("指数函数", font="PingFang SC",
                      font_size=52, color=GOLD).move_to(UP * 6.2)
        opening_group.add(title)
        self.play(Write(title), run_time=0.7)

        hook = Text(
            "为什么细菌 24 小时能繁殖万亿个？",
            font="PingFang SC", font_size=25, color=WHITE,
        ).move_to(UP * 5.2)
        opening_group.add(hook)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 快速展示指数爆炸
        axes = self._make_axes()
        self.play(Create(axes), run_time=0.7)

        g2 = self._plot(axes, "a2", self.C_A2)
        opening_group.add(g2)
        self.play(Create(g2), run_time=0.8)

        # 指数增长感受：标注几个值
        annots = [(0, 1, "1"), (1, 2, "2"), (2, 4, "4"), (2.3, 4.9, "≈5")]
        for x, y, label_str in annots:
            dot = Dot(axes.c2p(x, y), color=YELLOW, radius=0.07)
            lab  = Text(label_str, font="PingFang SC",
                         font_size=18, color=YELLOW).next_to(dot, UR, buff=0.05)
            opening_group.add(dot, lab)
            self.play(FadeIn(dot), FadeIn(lab), run_time=0.25)

        self.wait(0.8)
        # 清除开场除坐标轴外的所有元素
        opening_group.remove(axes)
        self.play(FadeOut(opening_group), run_time=0.4)
        # 保留坐标轴给下一幕
        self.axes = axes

    # ═══════════════════════════════════════════
    # Scene 2: 定义
    # ═══════════════════════════════════════════
    def scene_2_definition(self):
        definition_group = VGroup()

        sc_title = Text("指数函数的定义", font="PingFang SC",
                         font_size=32, color=GOLD).move_to(UP * 6.2)
        definition_group.add(sc_title)
        self.play(Write(sc_title), run_time=0.5)

        def_formula = MathTex(r"y = a^x", font_size=60, color=WHITE
                               ).move_to(UP * 5.1)
        cond = MathTex(r"(a > 0,\ a \neq 1)", font_size=28, color=self.C_AUX
                        ).next_to(def_formula, DOWN, buff=0.3)
        box = SurroundingRectangle(
            VGroup(def_formula, cond), color=GOLD, buff=0.3, corner_radius=0.15)
        definition_group.add(def_formula, cond, box)
        self.play(Write(def_formula), run_time=0.7)
        self.play(FadeIn(cond), Create(box), run_time=0.5)

        # 为什么 a≠1？
        why_text = Text("为何 a ≠ 1？",
                         font="PingFang SC", font_size=24, color=self.C_AUX
                         ).move_to(UP * 3.4)
        why_ans  = Text("因为 1^x = 1，是常数函数，不是指数函数",
                         font="PingFang SC", font_size=20, color=WHITE
                         ).move_to(UP * 2.8)
        definition_group.add(why_text, why_ans)
        self.play(FadeIn(why_text), run_time=0.4)
        self.play(FadeIn(why_ans), run_time=0.4)

        # 为什么 a>0？
        why2 = Text("为何 a > 0？  保证实数域内有意义",
                     font="PingFang SC", font_size=20, color=WHITE
                     ).move_to(UP * 2.1)
        definition_group.add(why2)
        self.play(FadeIn(why2), run_time=0.4)
        self.wait(1.5)

        # 彻底清理定义场景所有元素
        self.play(FadeOut(definition_group), run_time=0.4)

    # ═══════════════════════════════════════════
    # Scene 3: a>1 递增情形
    # ═══════════════════════════════════════════
    def scene_3_increasing(self):
        increasing_group = VGroup()
        axes = self.axes

        sc_title = Text("当 a > 1：单调递增",
                         font="PingFang SC", font_size=30, color=self.C_A2
                         ).move_to(UP * 6.2)
        increasing_group.add(sc_title)
        self.play(Write(sc_title), run_time=0.5)

        # y=2^x
        g2 = self._plot(axes, "a2", self.C_A2, stroke_width=3.5)
        lab_2 = MathTex(r"y = 2^x", font_size=26, color=self.C_A2
                         ).next_to(axes.c2p(2.0, 4.0), RIGHT, buff=0.1)
        increasing_group.add(g2, lab_2)
        self.play(Create(g2), Write(lab_2), run_time=0.8)

        # y=3^x
        g3 = self._plot(axes, "a3", self.C_A3, stroke_width=3.5)
        lab_3 = MathTex(r"y = 3^x", font_size=26, color=self.C_A3
                         ).next_to(axes.c2p(1.0, 3.0), LEFT, buff=0.1)
        increasing_group.add(g3, lab_3)
        self.play(Create(g3), Write(lab_3), run_time=0.8)

        # 公共点 (0,1)
        common = Dot(axes.c2p(0, 1), color=self.C_PT, radius=0.13)
        lab_pt = MathTex(r"(0,\ 1)", font_size=24, color=self.C_PT
                          ).next_to(axes.c2p(0, 1), UL, buff=0.12)
        increasing_group.add(common, lab_pt)
        self.play(FadeIn(common, scale=0.4), Write(lab_pt), run_time=0.5)
        self.play(Flash(common, color=self.C_PT, flash_radius=0.3), run_time=0.4)

        # 渐近线 y=0
        asy_line = DashedLine(
            axes.c2p(-3, 0), axes.c2p(3, 0),
            color=self.C_ASY, dash_length=0.12, stroke_width=1.5,
        )
        asy_lab = MathTex(r"y = 0", font_size=22, color=self.C_ASY
                           ).next_to(axes.c2p(2.2, 0), DOWN, buff=0.12)
        increasing_group.add(asy_line, asy_lab)
        self.play(Create(asy_line), Write(asy_lab), run_time=0.5)

        # 说明箭头（从左到右，图像上升）
        arrow = Arrow(
            start=axes.c2p(-2, 0.25),
            end=axes.c2p(2, 4.0),
            color=self.C_A2, buff=0, stroke_width=2,
        )
        increasing_group.add(arrow)
        self.play(GrowArrow(arrow), run_time=0.5)

        notes = VGroup(
            Text("x 越大，y 越大",
                  font="PingFang SC", font_size=22, color=WHITE),
            Text("x→+∞，y→+∞",
                  font="PingFang SC", font_size=22, color=WHITE),
            Text("x→-∞，y→0⁺（趋近 x 轴）",
                  font="PingFang SC", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 3.5)
        increasing_group.add(notes)
        self.play(Write(notes), run_time=0.7)
        self.wait(2.0)

        # 彻底清理递增场景所有元素
        self.play(FadeOut(increasing_group), run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 4: 0<a<1 递减情形
    # ═══════════════════════════════════════════
    def scene_4_decreasing(self):
        decreasing_group = VGroup()
        axes = self.axes

        sc_title = Text("当 0 < a < 1：单调递减",
                         font="PingFang SC", font_size=30, color=self.C_AH
                         ).move_to(UP * 6.2)
        decreasing_group.add(sc_title)
        self.play(Write(sc_title), run_time=0.5)

        # y=(1/2)^x
        gh = self._plot(axes, "half", self.C_AH, stroke_width=3.5)
        lab_h = MathTex(r"y = \left(\tfrac{1}{2}\right)^x",
                         font_size=26, color=self.C_AH
                         ).next_to(axes.c2p(-2, 4.0), RIGHT, buff=0.1)
        decreasing_group.add(gh, lab_h)
        self.play(Create(gh), Write(lab_h), run_time=0.8)

        # y=(1/3)^x
        gth = self._plot(axes, "third", self.C_ATH, stroke_width=3.5)
        lab_th = MathTex(r"y = \left(\tfrac{1}{3}\right)^x",
                          font_size=26, color=self.C_ATH
                          ).next_to(axes.c2p(-1.0, 3.5), LEFT, buff=0.05)
        decreasing_group.add(gth, lab_th)
        self.play(Create(gth), Write(lab_th), run_time=0.8)

        # 公共点
        common = Dot(axes.c2p(0, 1), color=self.C_PT, radius=0.13)
        lab_pt = MathTex(r"(0,\ 1)", font_size=24, color=self.C_PT
                          ).next_to(axes.c2p(0, 1), UR, buff=0.12)
        decreasing_group.add(common, lab_pt)
        self.play(FadeIn(common, scale=0.4), Write(lab_pt), run_time=0.5)

        # 渐近线
        asy_line = DashedLine(
            axes.c2p(-3, 0), axes.c2p(3, 0),
            color=self.C_ASY, dash_length=0.12, stroke_width=1.5,
        )
        decreasing_group.add(asy_line)
        self.play(Create(asy_line), run_time=0.4)

        # 下降箭头
        arrow = Arrow(
            start=axes.c2p(-2, 4.0),
            end=axes.c2p(2, 0.25),
            color=self.C_AH, buff=0, stroke_width=2,
        )
        decreasing_group.add(arrow)
        self.play(GrowArrow(arrow), run_time=0.5)

        notes = VGroup(
            Text("x 越大，y 越小",
                  font="PingFang SC", font_size=22, color=WHITE),
            Text("x→-∞，y→+∞",
                  font="PingFang SC", font_size=22, color=WHITE),
            Text("x→+∞，y→0⁺（趋近 x 轴）",
                  font="PingFang SC", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 3.5)
        decreasing_group.add(notes)
        self.play(Write(notes), run_time=0.7)
        self.wait(2.0)

        # 彻底清理递减场景所有元素
        self.play(FadeOut(decreasing_group), run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 5: 对比：互为镜像
    # ═══════════════════════════════════════════
    def scene_5_compare(self):
        compare_group = VGroup()
        axes = self.axes

        sc_title = Text("a > 1 与 0 < a < 1 的关系",
                         font="PingFang SC", font_size=28, color=GOLD
                         ).move_to(UP * 6.2)
        compare_group.add(sc_title)
        self.play(Write(sc_title), run_time=0.5)

        g2  = self._plot(axes, "a2",   self.C_A2,  stroke_width=2.5)
        gh  = self._plot(axes, "half", self.C_AH,  stroke_width=2.5)
        lab_2 = MathTex(r"y = 2^x", font_size=22, color=self.C_A2
                         ).next_to(axes.c2p(1.8, 3.5), RIGHT, buff=0.08)
        lab_h = MathTex(r"y = \left(\tfrac{1}{2}\right)^x",
                         font_size=22, color=self.C_AH
                         ).next_to(axes.c2p(-1.8, 3.5), LEFT, buff=0.08)
        compare_group.add(g2, gh, lab_2, lab_h)

        self.play(Create(g2), Create(gh), Write(lab_2), Write(lab_h), run_time=0.8)

        # y 轴对称虚线
        yaxis_dashed = DashedLine(
            axes.c2p(0, -0.3), axes.c2p(0, 5.0),
            color=YELLOW, dash_length=0.15, stroke_width=2,
        )
        sym_label = Text("关于 y 轴对称",
                          font="PingFang SC", font_size=22, color=YELLOW
                          ).move_to(DOWN * 1.5)
        compare_group.add(yaxis_dashed, sym_label)
        self.play(Create(yaxis_dashed), FadeIn(sym_label), run_time=0.6)

        relation = MathTex(
            r"\left(\tfrac{1}{2}\right)^x = 2^{-x}",
            font_size=30, color=self.C_RULE,
        ).move_to(DOWN * 2.4)
        compare_group.add(relation)
        self.play(Write(relation), run_time=0.6)
        self.wait(1.5)

        # 彻底清理对比场景所有元素
        self.play(FadeOut(compare_group), run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 6: 性质总结表
    # ═══════════════════════════════════════════
    def scene_6_properties(self):
        properties_group = VGroup()
        
        # 先清理之前保留的坐标轴
        self.play(FadeOut(self.axes), run_time=0.4)

        sc_title = Text("指数函数性质总结",
                         font="PingFang SC", font_size=32, color=GOLD
                         ).move_to(UP * 6.2)
        properties_group.add(sc_title)
        self.play(Write(sc_title), run_time=0.5)

        # 两列对比表
        headers = VGroup(
            Text("性质", font="PingFang SC", font_size=24, color=GOLD),
            MathTex(r"a > 1",            font_size=26, color=self.C_A2),
            MathTex(r"0 < a < 1",        font_size=26, color=self.C_AH),
        ).arrange(RIGHT, buff=1.0).move_to(UP * 5.3)
        properties_group.add(headers)
        self.play(FadeIn(headers), run_time=0.4)

        divider = Line(LEFT * 4, RIGHT * 4, color=GRAY_B, stroke_width=1
                        ).next_to(headers, DOWN, buff=0.15)
        properties_group.add(divider)
        self.play(Create(divider), run_time=0.3)

        rows_data = [
            ("定义域",    r"x \in \mathbb{R}",      r"x \in \mathbb{R}"),
            ("值域",      r"(0,\ +\infty)",          r"(0,\ +\infty)"),
            ("定点",      r"(0,\ 1)",                r"(0,\ 1)"),
            ("单调性",    "单调递增",                "单调递减"),
            ("渐近线",    r"y = 0\ (x \to -\infty)", r"y = 0\ (x \to +\infty)"),
        ]

        row_mobs = []
        for i, (prop, v1, v2) in enumerate(rows_data):
            y_pos = 4.4 - i * 1.0
            prop_m = Text(prop, font="PingFang SC",
                           font_size=22, color=WHITE)
            # v1, v2 有时是中文
            try:
                v1_m = MathTex(v1, font_size=22, color=self.C_A2)
            except Exception:
                v1_m = Text(v1, font="PingFang SC", font_size=22, color=self.C_A2)
            try:
                v2_m = MathTex(v2, font_size=22, color=self.C_AH)
            except Exception:
                v2_m = Text(v2, font="PingFang SC", font_size=22, color=self.C_AH)

            # 中文单调性用 Text
            if "单调" in v1:
                v1_m = Text(v1, font="PingFang SC", font_size=22, color=self.C_A2)
            if "单调" in v2:
                v2_m = Text(v2, font="PingFang SC", font_size=22, color=self.C_AH)

            row = VGroup(prop_m, v1_m, v2_m).arrange(RIGHT, buff=0.9).move_to(UP * y_pos)
            properties_group.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            row_mobs.append(row)

        self.wait(2.0)

        # 彻底清理性质总结场景所有元素
        self.play(FadeOut(properties_group), run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 7: 片尾
    # ═══════════════════════════════════════════
    def scene_7_outro(self):
        outro_group = VGroup()
        
        name_big = Text("上海初高中数学直通车",
                         font="PingFang SC", font_size=40, color=WHITE
                         ).move_to(UP * 1.5)
        id_text  = Text("@emptyandcalm",
                         font="PingFang SC", font_size=28, color=self.C_AUX
                         ).move_to(UP * 0.6)
        call     = Text("关注我，获得更多数学技巧！",
                         font="PingFang SC", font_size=28, color=GOLD
                         ).move_to(DOWN * 0.3)
        outro_group.add(name_big, id_text, call)

        self.play(Transform(self.author, name_big), run_time=0.7)
        self.play(FadeIn(id_text, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(call, scale=1.1), run_time=0.5)

        # 两条代表曲线动态展示
        mini_axes = Axes(
            x_range=[-2, 2, 1], y_range=[0, 4, 1],
            x_length=4, y_length=2.5,
            axis_config={"color": GRAY_B, "tip_length": 0.15, "font_size": 14},
        ).move_to(DOWN * 2.0)

        gup   = mini_axes.plot(lambda x: 2**x,   x_range=[-2, 2], color=self.C_A2)
        gdown = mini_axes.plot(lambda x: 0.5**x, x_range=[-2, 2], color=self.C_AH)
        outro_group.add(mini_axes, gup, gdown)

        self.play(Create(mini_axes), run_time=0.5)
        self.play(Create(gup), Create(gdown), run_time=0.8)
        self.wait(1.2)

        # 彻底清理片尾所有元素
        self.play(FadeOut(outro_group), run_time=0.8)
"""
幂函数 - Power Functions Teaching Animation
高一数学第四章

TikTok 竖屏格式 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""
from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class PowerFunctions(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ── 配色 ──
        self.C = {
            "x1":   "#e74c3c",  # y=x
            "x2":   "#3498db",  # y=x²
            "x3":   "#2ecc71",  # y=x³
            "sqrt": "#f39c12",  # y=√x
            "inv":  "#9b59b6",  # y=1/x
            "gold": GOLD,
            "aux":  GRAY_B,
            "form": "#f1c40f",
        }

        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_five_graphs()
        self.scene_4_common_point()
        self.scene_5_properties()
        self.scene_6_outro()

    # ═══════════════════════════════════════════
    def setup_geometry(self):
        self.AX_X = [-2.5, 2.5, 1]
        self.AX_Y = [-2,   4,   1]
        self.AX_XL = 6.0
        self.AX_YL = 5.5
        self.AX_CENTER = np.array([0.0, 2.0, 0.0])

        # 函数元数据: (key, expr_str, latex, color, x_range or ranges)
        self.FUNCS = [
            ("x1",   "y = x",          r"y = x",            self.C["x1"],   [(-2.5, 2.5)]),
            ("x2",   "y = x^2",         r"y = x^2",          self.C["x2"],   [(-2.0, 2.0)]),
            ("x3",   "y = x^3",         r"y = x^3",          self.C["x3"],   [(-1.6, 1.6)]),
            ("sqrt", "y = sqrt(x)",     r"y = \sqrt{x}",     self.C["sqrt"], [(0.0, 2.5)]),
            ("inv",  "y = 1/x",         r"y = \frac{1}{x}",  self.C["inv"],  [(-2.5, -0.15), (0.15, 2.5)]),
        ]

        self.FUNC_MAP = {
            "x1":   lambda x: x,
            "x2":   lambda x: x**2,
            "x3":   lambda x: x**3,
            "sqrt": lambda x: np.sqrt(x),
            "inv":  lambda x: 1 / x,
        }

    def _make_axes(self):
        axes = Axes(
            x_range=self.AX_X,
            y_range=self.AX_Y,
            x_length=self.AX_XL,
            y_length=self.AX_YL,
            axis_config={
                "color": self.C["aux"],
                "include_numbers": True,
                "numbers_to_include": [-2, -1, 0, 1, 2],
                "font_size": 18,
                "tip_length": 0.2,
            },
        ).move_to(self.AX_CENTER)
        return axes

    def _plot_func(self, axes, key, color=None, stroke_width=2.5, opacity=1.0):
        """绘制指定函数，支持分段"""
        c = color or self.C[key]
        fn = self.FUNC_MAP[key]
        ranges = next(f[4] for f in self.FUNCS if f[0] == key)
        graphs = VGroup()
        for xr in ranges:
            g = axes.plot(fn, x_range=list(xr), color=c,
                          stroke_width=stroke_width,
                          stroke_opacity=opacity)
            graphs.add(g)
        return graphs

    # ═══════════════════════════════════════════
    # Scene 1: 开场
    # ═══════════════════════════════════════════
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC", font_size=20, color=self.C["aux"]
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        title = Text("幂函数", font="Noto Sans CJK SC", font_size=52, color=GOLD
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        hook = Text(
            "这 5 条曲线有什么共同点？",
            font="Noto Sans CJK SC", font_size=30, color=WHITE
        ).move_to(UP * 5.2)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 快速画出 5 条曲线
        axes = self._make_axes()
        self.play(Create(axes), run_time=0.7)

        all_graphs = VGroup()
        for key, _, _, color, _ in self.FUNCS:
            g = self._plot_func(axes, key, color=color, stroke_width=2.5)
            all_graphs.add(g)
            self.play(Create(g), run_time=0.35)

        self.wait(0.8)

        # 闪烁公共点 (1,1)
        common_dot = Dot(axes.c2p(1, 1), color=YELLOW, radius=0.14)
        self.play(FadeIn(common_dot, scale=0.4), Flash(common_dot, color=YELLOW, flash_radius=0.3), run_time=0.6)
        self.wait(0.5)

        self.play(
            FadeOut(title), FadeOut(hook),
            FadeOut(all_graphs), FadeOut(common_dot),
            run_time=0.5,
        )
        self.axes = axes

    # ═══════════════════════════════════════════
    # Scene 2: 定义
    # ═══════════════════════════════════════════
    def scene_2_definition(self):
        sc_title = Text("幂函数的定义", font="Noto Sans CJK SC",
                         font_size=34, color=GOLD).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.6)

        def_formula = MathTex(r"y = x^{\alpha}", font_size=64, color=WHITE
                               ).move_to(UP * 5.0)
        self.play(Write(def_formula), run_time=0.8)

        cond = Text("（α 为常数）", font="Noto Sans CJK SC",
                     font_size=26, color=self.C["aux"]).next_to(def_formula, DOWN, buff=0.3)
        self.play(FadeIn(cond), run_time=0.4)

        # α 的常见取值
        alpha_title = Text("常见的 α 值：", font="Noto Sans CJK SC",
                            font_size=24, color=self.C["aux"]).move_to(UP * 3.8)
        self.play(FadeIn(alpha_title), run_time=0.3)

        alpha_vals = [
            (r"\alpha = 1",            r"\Rightarrow\ y = x",           self.C["x1"]),
            (r"\alpha = 2",            r"\Rightarrow\ y = x^2",         self.C["x2"]),
            (r"\alpha = 3",            r"\Rightarrow\ y = x^3",         self.C["x3"]),
            (r"\alpha = \frac{1}{2}",  r"\Rightarrow\ y = \sqrt{x}",    self.C["sqrt"]),
            (r"\alpha = -1",           r"\Rightarrow\ y = \frac{1}{x}", self.C["inv"]),
        ]

        mobs = []
        for i, (a_tex, y_tex, color) in enumerate(alpha_vals):
            y_pos = UP * (3.0 - i * 0.85)
            row = VGroup(
                MathTex(a_tex, font_size=26, color=color),
                MathTex(y_tex, font_size=26, color=WHITE),
            ).arrange(RIGHT, buff=0.4).move_to(y_pos)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
            mobs.append(row)

        self.wait(1.5)

        self.play(
            FadeOut(sc_title), FadeOut(def_formula), FadeOut(cond),
            FadeOut(alpha_title), *[FadeOut(m) for m in mobs],
            run_time=0.5,
        )

    # ═══════════════════════════════════════════
    # Scene 3: 逐一展示5个图像
    # ═══════════════════════════════════════════
    def scene_3_five_graphs(self):
        axes = self.axes
        sc_title = Text("函数图像一览", font="Noto Sans CJK SC",
                         font_size=32, color=GOLD).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        label_anchor_x = 3.0  # 标签 x 位置（右侧）

        drawn = []   # 保留所有已绘制图像（逐渐变灰）
        label_mobs = []

        label_positions = [
            axes.c2p(2.1, 2.1),       # y=x
            axes.c2p(1.8, 3.8),       # y=x²（靠近曲线末端）
            axes.c2p(1.5, 3.4),       # y=x³
            axes.c2p(2.4, 1.55),      # y=√x
            axes.c2p(2.4, 0.42),      # y=1/x（第一象限）
        ]

        for i, (key, _, latex, color, _) in enumerate(self.FUNCS):
            # 先把之前的图变灰
            for old in drawn:
                old.set_stroke(opacity=0.25)

            g = self._plot_func(axes, key, color=color, stroke_width=3.5)
            self.play(Create(g), run_time=0.7)

            # 标签
            lab = MathTex(latex, font_size=24, color=color).move_to(label_positions[i])
            self.play(Write(lab), run_time=0.4)

            drawn.append(g)
            label_mobs.append(lab)
            self.wait(0.3)

        # 恢复所有不透明
        for g in drawn:
            self.play(g.animate.set_stroke(opacity=1.0), run_time=0.3)

        self.wait(1.2)

        self.play(
            FadeOut(sc_title),
            *[FadeOut(m) for m in label_mobs],
            run_time=0.4,
        )
        self.current_graphs = drawn

    # ═══════════════════════════════════════════
    # Scene 4: 公共点 (1,1) 验证
    # ═══════════════════════════════════════════
    def scene_4_common_point(self):
        axes = self.axes

        sc_title = Text("神奇！都过同一个点", font="Noto Sans CJK SC",
                         font_size=30, color=GOLD).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        common_pt = axes.c2p(1, 1)
        dot = Dot(common_pt, color=YELLOW, radius=0.15)
        ring = Circle(radius=0.3, color=YELLOW, stroke_width=2).move_to(common_pt)

        self.play(FadeIn(dot, scale=0.4), run_time=0.4)
        self.play(Create(ring), run_time=0.5)
        self.play(Flash(dot, color=YELLOW, flash_radius=0.4, num_lines=10), run_time=0.5)

        pt_label = MathTex(r"(1,\ 1)", font_size=30, color=YELLOW
                            ).next_to(dot, UR, buff=0.15)
        self.play(Write(pt_label), run_time=0.4)

        # 验证公式
        verify_formula = MathTex(
            r"f(1) = 1^{\alpha} = 1",
            font_size=32, color=self.C["form"]
        ).move_to(DOWN * 1.2)
        self.play(Write(verify_formula), run_time=0.6)

        # 说明
        explain = Text("无论 α 取什么值，\n代入 x=1 结果都是 1！",
                        font="Noto Sans CJK SC", font_size=24, color=WHITE,
                        line_spacing=1.2).move_to(DOWN * 2.4)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(sc_title), FadeOut(ring), FadeOut(pt_label),
            FadeOut(verify_formula), FadeOut(explain),
            run_time=0.4,
        )
        self.common_dot = dot

    # ═══════════════════════════════════════════
    # Scene 5: 性质总结
    # ═══════════════════════════════════════════
    def scene_5_properties(self):
        axes = self.axes

        sc_title = Text("α 的正负决定图像形态",
                         font="Noto Sans CJK SC", font_size=30, color=GOLD
                         ).move_to(UP * 6.2)
        self.play(Write(sc_title), run_time=0.5)

        # 淡出1/x图，聚焦 α>0 图
        graphs = self.current_graphs
        self.play(
            *[g.animate.set_stroke(opacity=0.15) for g in graphs],
            run_time=0.4,
        )

        # α>0 高亮
        pos_alpha_label = MathTex(r"\alpha > 0", font_size=32, color=self.C["x2"]
                                   ).move_to(UP * 5.3 + LEFT * 1.5)
        pos_note = Text("过原点，第一象限单调递增",
                         font="Noto Sans CJK SC", font_size=20, color=self.C["x2"]
                         ).move_to(UP * 4.7 + LEFT * 1.0)

        graphs[0].set_stroke(opacity=1.0)  # y=x
        graphs[1].set_stroke(opacity=1.0)  # y=x²
        graphs[2].set_stroke(opacity=1.0)  # y=x³
        graphs[3].set_stroke(opacity=1.0)  # y=√x

        self.play(
            *[g.animate.set_stroke(opacity=1.0) for g in graphs[:4]],
            Write(pos_alpha_label), FadeIn(pos_note),
            run_time=0.7,
        )
        self.wait(1.0)

        # α<0 高亮
        self.play(
            *[g.animate.set_stroke(opacity=0.15) for g in graphs[:4]],
            run_time=0.4,
        )
        neg_alpha_label = MathTex(r"\alpha < 0", font_size=32, color=self.C["inv"]
                                   ).move_to(UP * 5.3 + RIGHT * 1.5)
        neg_note = Text("不过原点，\n第一象限单调递减",
                         font="Noto Sans CJK SC", font_size=20, color=self.C["inv"],
                         line_spacing=1.2).move_to(UP * 4.5 + RIGHT * 1.3)

        graphs[4].set_stroke(opacity=1.0)   # y=1/x
        self.play(
            graphs[4].animate.set_stroke(opacity=1.0),
            Write(neg_alpha_label), FadeIn(neg_note),
            run_time=0.7,
        )
        self.wait(1.0)

        # 恢复所有
        self.play(
            *[g.animate.set_stroke(opacity=0.8) for g in graphs],
            run_time=0.4,
        )

        # 底部总结框
        summary_lines = VGroup(
            Text("① 所有幂函数过 (1, 1)",
                  font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("② α>0 图像过原点",
                  font="Noto Sans CJK SC", font_size=22, color=self.C["x2"]),
            Text("③ α<0 第一象限递减，趋近两轴",
                  font="Noto Sans CJK SC", font_size=22, color=self.C["inv"]),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 3.5)
        box = SurroundingRectangle(summary_lines, color=GOLD, buff=0.25, corner_radius=0.12)

        self.play(Write(summary_lines), Create(box), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(sc_title),
            FadeOut(pos_alpha_label), FadeOut(pos_note),
            FadeOut(neg_alpha_label), FadeOut(neg_note),
            FadeOut(summary_lines), FadeOut(box),
            FadeOut(self.common_dot),
            *[FadeOut(g) for g in graphs],
            FadeOut(axes),
            run_time=0.6,
        )

    # ═══════════════════════════════════════════
    # Scene 6: 片尾
    # ═══════════════════════════════════════════
    def scene_6_outro(self):
        name_big = Text("上海初高中数学直通车",
                         font="Noto Sans CJK SC", font_size=40, color=WHITE
                         ).move_to(UP * 1.5)
        id_text  = Text("@emptyandcalm",
                         font="Noto Sans CJK SC", font_size=28, color=self.C["aux"]
                         ).move_to(UP * 0.6)
        call     = Text("关注我，获得更多数学技巧！",
                         font="Noto Sans CJK SC", font_size=28, color=GOLD
                         ).move_to(DOWN * 0.3)

        self.play(Transform(self.author, name_big), run_time=0.7)
        self.play(FadeIn(id_text, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(call, scale=1.1), run_time=0.5)

        # 5 个函数图标圆点
        icons = VGroup(*[
            Dot(radius=0.22, fill_color=self.C[k], fill_opacity=1, stroke_width=0
                ).move_to(np.array([-2.4 + j * 1.2, -1.8, 0]))
            for j, k in enumerate(["x1","x2","x3","sqrt","inv"])
        ])
        self.play(*[FadeIn(ic, scale=0.5) for ic in icons], run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(self.author), FadeOut(id_text),
                  FadeOut(call), FadeOut(icons), run_time=0.8)
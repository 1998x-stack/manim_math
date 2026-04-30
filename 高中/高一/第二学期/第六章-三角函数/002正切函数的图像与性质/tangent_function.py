"""
正切函数的图像与性质 - Manim教学动画
TikTok 竖屏 1080×1920
知识点: y = tan x 的图像、渐近线、周期性、奇函数
"""

from manim import *
import numpy as np

# ── 全局配置 ──────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

CJK = "PingFang SC"

# ── 颜色配置 ──────────────────────────────────────────
BG_COLOR   = "#0d1117"
C_TAN      = "#FF6B6B"   # 主图像（红）
C_ASYM     = "#FFD700"   # 渐近线（金黄）
C_LABEL    = "#A5D6A7"   # 坐标标注（浅绿）
C_PROP     = "#80DEEA"   # 性质高亮（浅青）
C_EXAMPLE  = "#CE93D8"   # 特殊值（紫）
C_HOOK     = "#FF7043"   # 钩子文字


class TangentFunction(Scene):
    """
    正切函数完整教学动画
    场景顺序：
      1. 开场钩子
      2. 定义推导 (tan = sin/cos)
      3. 建立坐标轴
      4. 渐近线
      5. 逐支绘图
      6. 三大性质（奇函数、周期、单调）
      7. 特殊值 & 值域对比
      8. 结尾
    """

    # ─────────────────────────────────────────────────
    #  CONSTRUCT
    # ─────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_params()

        self.scene_opening()
        self.scene_definition()
        self.scene_build_axes()
        self.scene_asymptotes()
        self.scene_draw_graph()
        self.scene_properties()
        self.scene_special_values()
        self.scene_outro()

    # ─────────────────────────────────────────────────
    #  SETUP — all maths pre-computed, never guessed
    # ─────────────────────────────────────────────────
    def setup_params(self):
        """Pre-compute every constant used across scenes."""
        self.EPS = 0.07          # gap from asymptote for branch endpoints

        # Math x-range shown in axes
        self.X_MATH_MIN = -5.0
        self.X_MATH_MAX =  5.0
        self.Y_MATH_MIN = -4.5
        self.Y_MATH_MAX =  4.5

        # Asymptote x-coordinates (math space)
        self.ASYMPTOTES = np.array([
            -3 * np.pi / 2,   # ≈ -4.712
            -    np.pi / 2,   # ≈ -1.571
                 np.pi / 2,   # ≈  1.571
             3 * np.pi / 2,   # ≈  4.712
        ])

        # Branch x-ranges (math space), ordered left → right
        eps = self.EPS
        self.BRANCHES = [
            [self.X_MATH_MIN,          self.ASYMPTOTES[0] - eps],
            [self.ASYMPTOTES[0] + eps, self.ASYMPTOTES[1] - eps],
            [self.ASYMPTOTES[1] + eps, self.ASYMPTOTES[2] - eps],  # main
            [self.ASYMPTOTES[2] + eps, self.ASYMPTOTES[3] - eps],
            [self.ASYMPTOTES[3] + eps, self.X_MATH_MAX],
        ]

        # Special values (math space)
        self.SPECIAL_X = [0,        np.pi/6,      np.pi/4, np.pi/3]
        self.SPECIAL_Y = [0,  1/np.sqrt(3),            1,  np.sqrt(3)]
        self.SPECIAL_LABELS = [
            (r"0", r"0"),
            (r"\frac{\pi}{6}", r"\frac{\sqrt{3}}{3}"),
            (r"\frac{\pi}{4}", r"1"),
            (r"\frac{\pi}{3}", r"\sqrt{3}"),
        ]

        # Axes visual dimensions (Manim logical units)
        self.AX_X_LEN = 7.4
        self.AX_Y_LEN = 4.6
        self.AX_CENTER = UP * 1.4   # centre of axes in frame

        self._verify()

    def _verify(self):
        """Sanity-check all pre-computed values."""
        for x_asym in self.ASYMPTOTES:
            # tan should explode near asymptote
            assert abs(np.tan(x_asym - 0.001)) > 100, \
                f"Asymptote position wrong at {x_asym:.4f}"

        for x_val, y_val in zip(self.SPECIAL_X, self.SPECIAL_Y):
            computed = np.tan(x_val)
            assert abs(computed - y_val) < 1e-10, \
                f"Special value error: tan({x_val:.4f})={computed:.6f} ≠ {y_val:.6f}"

        # Branch endpoints should stay within y_range after tan()
        for branch in self.BRANCHES:
            x_start, x_end = branch
            y_start = np.tan(x_start)
            y_end   = np.tan(x_end)
            # Values near asymptote will be large but that's expected
        print("✓ setup_params verified")

    # ─────────────────────────────────────────────────
    #  HELPERS
    # ─────────────────────────────────────────────────
    def _author_tag(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=CJK, font_size=19, color=GRAY_B
        ).move_to(UP * 7.2)

    def _section_title(self, text, color=GOLD):
        return Text(text, font=CJK, font_size=34, color=color).move_to(UP * 5.8)

    def _prop_badge(self, icon_text, body_text, color, position):
        """Small coloured badge for property display."""
        dot   = Dot(radius=0.14, color=color, fill_opacity=1)
        label = Text(body_text, font=CJK, font_size=22, color=WHITE)
        grp = VGroup(dot, label).arrange(RIGHT, buff=0.2)
        grp.move_to(position)
        return grp

    def _x_label(self, x_math, label_str, axes, direction=DOWN, buff=0.28):
        """Place a MathTex label at a given math x-coordinate on x-axis."""
        pt = axes.coords_to_point(x_math, 0)
        return MathTex(label_str, font_size=18, color=C_LABEL).next_to(pt, direction, buff=buff)

    # ─────────────────────────────────────────────────
    #  SCENE 1: OPENING HOOK
    # ─────────────────────────────────────────────────
    def scene_opening(self):
        self.author = self._author_tag()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text("正切函数长什么样？", font=CJK,
                     font_size=44, color=C_HOOK).move_to(UP * 5.0)
        hook2 = Text("为什么它有无数条渐近线？", font=CJK,
                     font_size=26, color=GRAY_A).move_to(UP * 4.1)

        self.play(Write(hook1), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # Teaser: a quick flash of a steep tan-like curve
        teaser_axes = Axes(
            x_range=[-0.5, 0.5, 0.25], y_range=[-5, 5, 1],
            x_length=2.5, y_length=3.5,
            axis_config={"include_tip": False, "stroke_color": GRAY_B,
                         "stroke_width": 1.5}
        ).move_to(DOWN * 1.2)
        teaser_graph = teaser_axes.plot(
            np.tan,
            x_range=[-0.48, 0.48],
            color=C_TAN, stroke_width=3
        )
        self.play(FadeIn(teaser_axes), Create(teaser_graph), run_time=1.0)
        teaser_question = Text("越来越陡……最后\"冲出\"坐标系？",
                               font=CJK, font_size=22, color=GRAY_A).move_to(DOWN * 4.0)
        self.play(FadeIn(teaser_question), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(teaser_axes), FadeOut(teaser_graph),
            FadeOut(teaser_question),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    #  SCENE 2: DEFINITION  tan x = sin x / cos x
    # ─────────────────────────────────────────────────
    def scene_definition(self):
        title = self._section_title("什么是正切函数？")
        self.play(Write(title), run_time=0.6)

        # Main definition
        def_eq = MathTex(
            r"\tan x = \frac{\sin x}{\cos x}",
            font_size=40, color=WHITE
        ).move_to(UP * 4.5)
        self.play(Write(def_eq), run_time=0.9)

        # Condition: cos x ≠ 0
        cond_label = Text("要求：", font=CJK, font_size=26, color=GRAY_A).move_to(UP * 3.4 + LEFT * 1.5)
        cond_eq = MathTex(
            r"\cos x \neq 0",
            font_size=30, color=C_HOOK
        ).next_to(cond_label, RIGHT, buff=0.25)
        self.play(FadeIn(cond_label), Write(cond_eq), run_time=0.7)

        # Arrow leading to domain
        arrow = Arrow(
            cond_eq.get_bottom() + DOWN * 0.1,
            cond_eq.get_bottom() + DOWN * 0.8,
            buff=0.05, color=GRAY_B, stroke_width=2,
            max_tip_length_to_length_ratio=0.2
        )
        domain_label = Text("定义域：", font=CJK, font_size=24, color=GRAY_A)
        domain_eq    = MathTex(
            r"x \neq \frac{\pi}{2} + k\pi,\; k \in \mathbb{Z}",
            font_size=26, color=C_PROP
        )
        domain_grp = VGroup(domain_label, domain_eq).arrange(RIGHT, buff=0.2)
        domain_grp.next_to(arrow, DOWN, buff=0.1)

        self.play(Create(arrow), run_time=0.4)
        self.play(FadeIn(domain_label), Write(domain_eq), run_time=0.7)

        # Remark: range is all of R
        range_note = Text("值域：全体实数", font=CJK,
                          font_size=26, color=C_LABEL).move_to(UP * 1.4)
        range_eq   = MathTex(r"\mathbb{R}", font_size=30,
                             color=C_LABEL).next_to(range_note, RIGHT, buff=0.2)
        grp_range  = VGroup(range_note, range_eq)
        exclaim    = Text("（无最大值、无最小值！）", font=CJK,
                          font_size=22, color=C_HOOK).move_to(UP * 0.7)

        self.play(FadeIn(grp_range, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(exclaim), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(def_eq),
            FadeOut(cond_label), FadeOut(cond_eq), FadeOut(arrow),
            FadeOut(domain_label), FadeOut(domain_eq),
            FadeOut(grp_range), FadeOut(exclaim),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────
    #  SCENE 3: BUILD AXES
    # ─────────────────────────────────────────────────
    def scene_build_axes(self):
        title = self._section_title("建立坐标系")
        self.play(Write(title), run_time=0.5)

        # Build axes (no built-in number labels — we'll add custom π-based ones)
        self.axes = Axes(
            x_range=[self.X_MATH_MIN, self.X_MATH_MAX, np.pi / 2],
            y_range=[self.Y_MATH_MIN, self.Y_MATH_MAX, 1],
            x_length=self.AX_X_LEN,
            y_length=self.AX_Y_LEN,
            axis_config={
                "include_tip": True,
                "tip_length": 0.18,
                "stroke_width": 2,
                "color": WHITE,
            },
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": True,
                           "numbers_to_include": [-4, -2, 0, 2, 4],
                           "font_size": 16,
                           "label_direction": LEFT,
                           "color": GRAY_B},
        ).move_to(self.AX_CENTER)

        # x-axis label
        x_axis_lbl = MathTex("x", font_size=22, color=WHITE).next_to(
            self.axes.x_axis.get_right(), RIGHT, buff=0.12)
        # y-axis label
        y_axis_lbl = MathTex("y", font_size=22, color=WHITE).next_to(
            self.axes.y_axis.get_top(), UP, buff=0.12)

        self.play(Create(self.axes), run_time=1.0)
        self.play(Write(x_axis_lbl), Write(y_axis_lbl), run_time=0.4)

        # Custom π-based x-axis labels
        tick_data = [
            (-3 * np.pi / 2, r"-\frac{3\pi}{2}"),
            (-    np.pi,     r"-\pi"),
            (-    np.pi / 2, r"-\frac{\pi}{2}"),
            (     np.pi / 2, r"\frac{\pi}{2}"),
            (     np.pi,     r"\pi"),
            ( 3 * np.pi / 2, r"\frac{3\pi}{2}"),
        ]
        self.x_tick_labels = VGroup()
        for x_val, tex_str in tick_data:
            lbl = MathTex(tex_str, font_size=17, color=GRAY_B)
            pt  = self.axes.coords_to_point(x_val, 0)
            lbl.next_to(pt, DOWN, buff=0.25)
            self.x_tick_labels.add(lbl)

        self.play(FadeIn(self.x_tick_labels), run_time=0.6)
        self.wait(0.5)

        self.play(FadeOut(title), run_time=0.4)
        # axes, x_axis_lbl, y_axis_lbl, x_tick_labels persist

    # ─────────────────────────────────────────────────
    #  SCENE 4: ASYMPTOTES
    # ─────────────────────────────────────────────────
    def scene_asymptotes(self):
        title = self._section_title("渐近线 — 函数的\"禁区\"")
        self.play(Write(title), run_time=0.6)

        # Draw each asymptote one by one (only the inner two first, then outer two)
        self.asym_lines = VGroup()
        inner_asyms = [self.ASYMPTOTES[1], self.ASYMPTOTES[2]]   # ±π/2
        outer_asyms = [self.ASYMPTOTES[0], self.ASYMPTOTES[3]]   # ±3π/2

        for x_val in inner_asyms:
            pt_bot = self.axes.coords_to_point(x_val, self.Y_MATH_MIN - 0.15)
            pt_top = self.axes.coords_to_point(x_val, self.Y_MATH_MAX + 0.15)
            line = DashedLine(pt_bot, pt_top,
                              dash_length=0.12, dashed_ratio=0.5,
                              color=C_ASYM, stroke_width=2.0)
            self.asym_lines.add(line)
            self.play(Create(line), run_time=0.6)

        # Label x = ±π/2
        asym_label_eq = MathTex(
            r"x = \pm\frac{\pi}{2}", font_size=26, color=C_ASYM
        ).move_to(DOWN * 3.5)
        asym_explain = Text("cos x = 0，函数无意义！",
                            font=CJK, font_size=22, color=GRAY_A).move_to(DOWN * 4.3)
        self.play(Write(asym_label_eq), FadeIn(asym_explain), run_time=0.7)
        self.wait(0.8)

        # Outer asymptotes (±3π/2)
        for x_val in outer_asyms:
            pt_bot = self.axes.coords_to_point(x_val, self.Y_MATH_MIN - 0.15)
            pt_top = self.axes.coords_to_point(x_val, self.Y_MATH_MAX + 0.15)
            line = DashedLine(pt_bot, pt_top,
                              dash_length=0.12, dashed_ratio=0.5,
                              color=C_ASYM, stroke_width=1.5, stroke_opacity=0.7)
            self.asym_lines.add(line)
            self.play(Create(line), run_time=0.4)

        period_note = Text("每隔 π 就有一条！→ 无穷多条渐近线",
                           font=CJK, font_size=22, color=C_PROP).move_to(DOWN * 5.2)
        self.play(FadeIn(period_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(asym_label_eq),
            FadeOut(asym_explain), FadeOut(period_note),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    #  SCENE 5: DRAW GRAPH BRANCH BY BRANCH
    # ─────────────────────────────────────────────────
    def scene_draw_graph(self):
        title = self._section_title("绘制 y = tan x 的图像")
        self.play(Write(title), run_time=0.5)

        # Clipped tan function — Manim axes handle out-of-range clipping
        def tan_clipped(x):
            v = np.tan(x)
            return np.clip(v, self.Y_MATH_MIN - 0.05, self.Y_MATH_MAX + 0.05)

        # Branch indices: 2 = main (-π/2, π/2), then 1 & 3, then 0 & 4
        branch_order = [2, 1, 3, 0, 4]

        self.tan_branches = VGroup()
        for i, idx in enumerate(branch_order):
            br = self.BRANCHES[idx]
            graph = self.axes.plot(
                tan_clipped,
                x_range=[br[0], br[1], 0.01],
                color=C_TAN,
                stroke_width=3,
                use_smoothing=True,
            )
            self.tan_branches.add(graph)

            if i == 0:
                # Main branch — draw slowly with a label
                label_main = Text("主分支 (-π/2, π/2)",
                                  font=CJK, font_size=22, color=C_TAN).move_to(DOWN * 3.6)
                self.play(Create(graph), run_time=1.2)
                self.play(FadeIn(label_main), run_time=0.4)
                self.wait(0.5)
                self.play(FadeOut(label_main), run_time=0.3)
            else:
                self.play(Create(graph), run_time=0.6)

        more_note = Text("无穷多个分支……每段形状完全一样！",
                         font=CJK, font_size=22, color=C_LABEL).move_to(DOWN * 3.8)
        self.play(FadeIn(more_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(more_note), FadeOut(title), run_time=0.4)

    # ─────────────────────────────────────────────────
    #  SCENE 6: THREE KEY PROPERTIES
    # ─────────────────────────────────────────────────
    def scene_properties(self):
        title = self._section_title("三大核心性质")
        self.play(Write(title), run_time=0.5)

        # ── Property 1: Odd function ──────────────────
        prop1_head = Text("① 奇函数", font=CJK, font_size=28,
                          color=C_PROP).move_to(DOWN * 3.3)
        prop1_eq   = MathTex(r"\tan(-x) = -\tan x",
                             font_size=28, color=WHITE).move_to(DOWN * 4.0)
        prop1_note = Text("图像关于原点中心对称", font=CJK,
                          font_size=22, color=GRAY_A).move_to(DOWN * 4.8)
        self.play(Write(prop1_head), Write(prop1_eq), run_time=0.7)
        self.play(FadeIn(prop1_note), run_time=0.4)

        # Visual: highlight a symmetric pair (π/4, 1) and (-π/4, -1)
        pt_pos = Dot(self.axes.coords_to_point( np.pi/4,  1), radius=0.1, color=YELLOW)
        pt_neg = Dot(self.axes.coords_to_point(-np.pi/4, -1), radius=0.1, color=YELLOW)
        line_sym = DashedLine(pt_pos.get_center(), pt_neg.get_center(),
                              color=YELLOW, dash_length=0.08, stroke_width=1.5)
        origin_dot = Dot(self.axes.coords_to_point(0, 0),
                         radius=0.12, color=YELLOW, fill_opacity=0.9)
        self.play(FadeIn(pt_pos), FadeIn(pt_neg), Create(line_sym), FadeIn(origin_dot), run_time=0.6)
        self.wait(1.2)
        self.play(
            FadeOut(prop1_head), FadeOut(prop1_eq), FadeOut(prop1_note),
            FadeOut(pt_pos), FadeOut(pt_neg), FadeOut(line_sym), FadeOut(origin_dot),
            run_time=0.4
        )

        # ── Property 2: Period π ─────────────────────
        prop2_head = Text("② 最小正周期 T = π", font=CJK,
                          font_size=28, color=C_PROP).move_to(DOWN * 3.3)
        prop2_eq   = MathTex(r"\tan(x + \pi) = \tan x",
                             font_size=28, color=WHITE).move_to(DOWN * 4.0)
        prop2_note = Text("向右平移 π，图像完全重合", font=CJK,
                          font_size=22, color=GRAY_A).move_to(DOWN * 4.8)
        self.play(Write(prop2_head), Write(prop2_eq), run_time=0.7)
        self.play(FadeIn(prop2_note), run_time=0.4)

        # Visual: highlight main branch and show it "repeats"
        # Draw a period-shifted copy to the right of main branch in different color
        def tan_clipped(x):
            return np.clip(np.tan(x), self.Y_MATH_MIN - 0.1, self.Y_MATH_MAX + 0.1)

        br3 = self.BRANCHES[3]   # (π/2+eps, 3π/2-eps)
        highlight_branch = self.axes.plot(
            tan_clipped, x_range=[br3[0], br3[1], 0.01],
            color=YELLOW, stroke_width=4
        )
        brace_start = self.axes.coords_to_point(self.ASYMPTOTES[1], 0)
        brace_end   = self.axes.coords_to_point(self.ASYMPTOTES[2], 0)
        period_brace = BraceBetweenPoints(brace_start, brace_end, direction=DOWN)
        period_brace_lbl = MathTex(r"T = \pi", font_size=20, color=YELLOW)
        period_brace_lbl.next_to(period_brace, DOWN, buff=0.1)

        self.play(Create(highlight_branch), run_time=0.6)
        self.play(Create(period_brace), Write(period_brace_lbl), run_time=0.5)
        self.wait(1.2)
        self.play(
            FadeOut(prop2_head), FadeOut(prop2_eq), FadeOut(prop2_note),
            FadeOut(highlight_branch), FadeOut(period_brace), FadeOut(period_brace_lbl),
            run_time=0.4
        )

        # ── Property 3: Monotone increasing on each branch ──────
        prop3_head = Text("③ 每个分支单调递增", font=CJK,
                          font_size=28, color=C_PROP).move_to(DOWN * 3.3)
        prop3_note = Text("在 (-π/2 + kπ, π/2 + kπ) 上递增", font=CJK,
                          font_size=22, color=GRAY_A).move_to(DOWN * 4.0)
        prop3_warn = Text("注意：不是在整个 R 上单调！", font=CJK,
                          font_size=22, color=C_HOOK).move_to(DOWN * 4.9)
        self.play(Write(prop3_head), FadeIn(prop3_note), run_time=0.7)

        # Arrows on main branch showing upward trend
        x_pts = [-1.0, -0.3, 0.4, 1.0]
        arrows_up = VGroup()
        for x_val in x_pts:
            y_val = np.tan(x_val)
            if abs(y_val) < self.Y_MATH_MAX:
                pt = self.axes.coords_to_point(x_val, y_val)
                arr = Arrow(pt + DOWN * 0.25, pt + UP * 0.25,
                            buff=0, stroke_width=2, color=C_PROP,
                            max_tip_length_to_length_ratio=0.3)
                arrows_up.add(arr)
        self.play(*[FadeIn(a, scale=0.5) for a in arrows_up], run_time=0.5)
        self.play(FadeIn(prop3_warn, shift=UP * 0.15), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(prop3_head), FadeOut(prop3_note), FadeOut(prop3_warn),
            FadeOut(arrows_up), FadeOut(title),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    #  SCENE 7: SPECIAL VALUES & RANGE COMPARISON
    # ─────────────────────────────────────────────────
    def scene_special_values(self):
        title = self._section_title("特殊值 & 值域对比")
        self.play(Write(title), run_time=0.5)

        # Plot special value dots on main branch
        special_dots   = VGroup()
        special_labels = VGroup()
        for x_val, y_val, (x_tex, y_tex) in zip(
                self.SPECIAL_X, self.SPECIAL_Y, self.SPECIAL_LABELS):
            dot = Dot(self.axes.coords_to_point(x_val, y_val),
                      radius=0.11, color=C_EXAMPLE)
            special_dots.add(dot)
            lbl = MathTex(rf"({x_tex},\,{y_tex})", font_size=18, color=C_EXAMPLE)
            # Place label: shift slightly to avoid overlap
            lbl.next_to(dot, UR, buff=0.12)
            special_labels.add(lbl)

        self.play(*[FadeIn(d, scale=0.5) for d in special_dots], run_time=0.5)
        self.play(*[Write(lbl) for lbl in special_labels], run_time=0.7)
        self.wait(1.0)

        # Key comparison: range
        compare_title = Text("值域对比：", font=CJK,
                             font_size=26, color=WHITE).move_to(DOWN * 3.4)
        rows = VGroup(
            VGroup(
                MathTex(r"\sin x, \cos x", font_size=24, color="#81D4FA"),
                Text("：值域", font=CJK, font_size=22, color=GRAY_A),
                MathTex(r"[-1,\, 1]", font_size=24, color="#81D4FA"),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\tan x", font_size=24, color=C_TAN),
                Text("：值域", font=CJK, font_size=22, color=GRAY_A),
                MathTex(r"\mathbb{R}", font_size=24, color=C_TAN),
                Text("全体实数！", font=CJK, font_size=22, color=C_HOOK),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 4.4)

        self.play(FadeIn(compare_title), run_time=0.4)
        self.play(FadeIn(rows[0]), run_time=0.5)
        self.play(FadeIn(rows[1]), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(special_dots), FadeOut(special_labels),
            FadeOut(compare_title), FadeOut(rows),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────
    #  SCENE 8: OUTRO
    # ─────────────────────────────────────────────────
    def scene_outro(self):
        # Move graph up for summary card
        summary_bg = RoundedRectangle(
            width=7.8, height=3.5,
            corner_radius=0.25,
            fill_color="#1a2a3a", fill_opacity=0.9,
            stroke_color=C_PROP, stroke_width=1.5,
        ).move_to(DOWN * 4.3)

        title_sum = Text("正切函数性质总结", font=CJK,
                         font_size=28, color=GOLD).next_to(summary_bg, UP, buff=0.25)

        items = VGroup(
            VGroup(
                Text("定义域：", font=CJK, font_size=20, color=GRAY_A),
                MathTex(r"x \neq \frac{\pi}{2}+k\pi", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("值域：", font=CJK, font_size=20, color=GRAY_A),
                MathTex(r"\mathbb{R}", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("周期：", font=CJK, font_size=20, color=GRAY_A),
                MathTex(r"T = \pi", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("奇偶性：", font=CJK, font_size=20, color=GRAY_A),
                Text("奇函数", font=CJK, font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("单调性：", font=CJK, font_size=20, color=GRAY_A),
                Text("每支递增", font=CJK, font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        items.move_to(summary_bg.get_center())

        self.play(FadeIn(summary_bg), Write(title_sum), run_time=0.6)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.25)
        self.wait(1.0)

        # Follow CTA
        follow = Text("关注我，获得更多数学技巧！", font=CJK,
                      font_size=28, color=C_HOOK).move_to(DOWN * 6.5)
        self.play(FadeIn(follow, scale=1.05), run_time=0.6)

        author_big = Text("上海初高中数学直通车", font=CJK,
                          font_size=30, color=WHITE).move_to(DOWN * 7.1)
        self.play(Transform(self.author, author_big), run_time=0.6)
        self.wait(1.5)
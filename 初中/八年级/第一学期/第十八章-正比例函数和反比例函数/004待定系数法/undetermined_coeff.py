"""
undetermined_coeff.py
=====================
待定系数法 — TikTok 竖屏教学动画
格式: 1080×1920 (frame_width=9, frame_height=16)
时长: ~60s  |  年级: 八年级

运行:
    manim -pqh --resolution 1080,1920 undetermined_coeff.py UndeterminedCoeff
"""

from manim import *
import numpy as np

BG       = "#0D1B2A"
C_WHITE  = WHITE
C_GOLD   = "#FFD700"
C_BLUE   = "#4FC3F7"
C_GREEN  = "#66BB6A"
C_RED    = "#EF5350"
C_ORANGE = "#FFA726"
C_PURPLE = "#CE93D8"
C_GRAY   = "#78909C"
C_BOX    = "#1A2E45"


class UndeterminedCoeff(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.scene1_intro()
        self.scene2_four_steps()
        self.scene3_linear_example()
        self.scene4_inverse_example()
        self.scene5_comparison()

    def _title(self, txt, color=C_WHITE, size=36):
        return Text(txt, font_size=size, color=color,
                    font="PingFang SC").move_to(UP * 4.5)

    def _clear(self, *objs):
        self.play(*[FadeOut(m) for m in objs], run_time=0.45)

    def _num_circle(self, n, color):
        c = Circle(radius=0.26, color=color, fill_color=color,
                   fill_opacity=0.85, stroke_width=0)
        t = Text(str(n), font_size=20, color=C_WHITE,
                 font="PingFang SC").move_to(c.get_center())
        return VGroup(c, t)

    # ══════════════════════════════════════════════════
    # Scene 1: 引入问题 (0–6s)
    # ══════════════════════════════════════════════════
    def scene1_intro(self):
        title = self._title("待定系数法", color=C_GOLD, size=44)

        card = RoundedRectangle(width=6.5, height=3.2, corner_radius=0.25,
                                color=C_BLUE, fill_color=C_BOX,
                                fill_opacity=0.9, stroke_width=2.5
                                ).move_to(UP * 2.0)

        q_lines = VGroup(
            Text("正比例函数过点 (2, 6)", font_size=28, color=C_WHITE,
                 font="PingFang SC"),
            Text("求函数解析式", font_size=28, color=C_GOLD,
                 font="PingFang SC"),
        ).arrange(DOWN, buff=0.35).move_to(UP * 2.0)

        # 问号
        qmark = Text("?", font_size=60, color=C_GOLD,
                     font="PingFang SC").move_to(DOWN * 0.5)

        hint = Text("已知一个点，就能确定整条函数！",
                    font_size=24, color=C_GREEN,
                    font="PingFang SC").move_to(DOWN * 1.8)

        self.play(Write(title), run_time=0.7)
        self.play(DrawBorderThenFill(card), run_time=0.5)
        self.play(Write(q_lines[0]), run_time=0.5)
        self.play(Write(q_lines[1]), run_time=0.5)
        self.play(GrowFromCenter(qmark), run_time=0.4)
        self.play(FadeIn(hint), run_time=0.4)
        self.wait(1.0)
        self._clear(title, card, q_lines, qmark, hint)

    # ══════════════════════════════════════════════════
    # Scene 2: 四步解题法 (6–16s)
    # ══════════════════════════════════════════════════
    def scene2_four_steps(self):
        title = self._title("② 四步解题法", color=C_BLUE, size=36)

        steps = [
            (1, C_BLUE,   "① 设", "设出含待定系数的函数形式"),
            (2, C_GREEN,  "② 代", "代入已知点坐标"),
            (3, C_ORANGE, "③ 解", "解方程求出系数"),
            (4, C_GOLD,   "④ 写", "写出完整函数解析式"),
        ]
        ys = [2.5, 1.1, -0.3, -1.7]

        step_rows = []
        for i, (n, col, step_lbl, desc) in enumerate(steps):
            circle = self._num_circle(n, col).move_to(LEFT * 3.2 + UP * ys[i])
            step_t = Text(step_lbl, font_size=30, color=col,
                          font="PingFang SC").move_to(LEFT * 2.1 + UP * ys[i])
            desc_t  = Text(desc, font_size=24, color=C_WHITE,
                           font="PingFang SC").move_to(RIGHT * 0.6 + UP * ys[i])
            sep = Line(LEFT * 1.5 + UP * ys[i] + LEFT * 0.1,
                       LEFT * 1.5 + UP * ys[i] + RIGHT * 3.8,
                       color=col, stroke_width=0.8,
                       ).move_to(LEFT * 0.1 + UP * (ys[i] - 0.38))
            row = VGroup(circle, step_t, desc_t)
            step_rows.append((row, sep))

        self.play(Write(title), run_time=0.6)
        for row, sep in step_rows:
            self.play(FadeIn(row), run_time=0.45)
            if sep:
                self.play(Create(sep), run_time=0.2)

        # 正比例例子演示
        eg_lbl = Text("例：正比例函数过 (2,6)",
                      font_size=24, color=C_GRAY,
                      font="PingFang SC").move_to(DOWN * 3.2)
        eg_steps = VGroup(
            MathTex(r"(1)\; y = kx", font_size=26, color=C_BLUE),
            MathTex(r"(2)\; 6 = 2k",  font_size=26, color=C_GREEN),
            MathTex(r"(3)\; k = 3",    font_size=26, color=C_ORANGE),
            MathTex(r"(4)\; y = 3x",   font_size=26, color=C_GOLD),
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 4.2)
        self.play(FadeIn(eg_lbl), run_time=0.4)
        self.play(FadeIn(eg_steps), run_time=0.5)
        self.wait(1.2)

        all_objs = [title, eg_lbl, eg_steps]
        for row, sep in step_rows:
            all_objs.append(row)
            all_objs.append(sep)
        self._clear(*all_objs)

    # ══════════════════════════════════════════════════
    # Scene 3: 正比例函数可视化 (16–32s)
    # ══════════════════════════════════════════════════
    def scene3_linear_example(self):
        title = self._title("③ 正比例函数：过 (2, 6)", color=C_BLUE, size=30)

        # ── 左侧计算区 ────────────────────────────────
        calc_items = [
            ("设", MathTex(r"y = kx", font_size=32, color=C_WHITE)),
            ("代入", MathTex(r"6 = 2k", font_size=32, color=C_WHITE)),
            ("解得", MathTex(r"k = 3", font_size=38, color=C_ORANGE)),
            ("结论", MathTex(r"y = 3x", font_size=42, color=C_GOLD)),
        ]
        calc_ys   = [2.5, 1.2, -0.1, -1.4]
        calc_x    = -2.2

        calc_labels = []
        calc_formulas = []
        for i, ((lbl_str, fml), cy) in enumerate(zip(calc_items, calc_ys)):
            lbl = Text(lbl_str, font_size=22, color=C_GRAY,
                       font="PingFang SC").move_to([calc_x - 0.7, cy, 0])
            fml.move_to([calc_x + 0.5, cy, 0])
            calc_labels.append(lbl)
            calc_formulas.append(fml)

        # k=3 高亮框
        k_box = SurroundingRectangle(calc_formulas[2], color=C_ORANGE,
                                      buff=0.14, corner_radius=0.08)
        res_box = SurroundingRectangle(calc_formulas[3], color=C_GOLD,
                                       buff=0.16, corner_radius=0.1)

        # ── 右侧坐标轴 ────────────────────────────────
        # 调整后参数（已由 verify_geometry 确认）:
        # center=(1.5,-0.5), x_range=(-1,4), x_length=2.8
        # y_range=(-1,9), y_length=2.8  → y_scale=2.8/10=0.28
        ax = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 9, 1],
            x_length=2.8,
            y_length=2.8,
            axis_config={"color": C_GRAY, "stroke_width": 1.5,
                         "include_tip": True, "tip_length": 0.14,
                         "include_numbers": False},
        ).move_to(RIGHT * 1.5 + DOWN * 0.5)

        ax_lbls = VGroup(
            MathTex(r"x", font_size=18, color=C_GRAY).next_to(
                ax.x_axis.get_right(), RIGHT, buff=0.05),
            MathTex(r"y", font_size=18, color=C_GRAY).next_to(
                ax.y_axis.get_top(), UP, buff=0.05),
        )

        # 目标点
        pt_dot = Dot(ax.c2p(2, 6), color=C_RED, radius=0.12)
        pt_lbl = MathTex(r"(2,6)", font_size=18, color=C_RED
                         ).next_to(ax.c2p(2, 6), UR, buff=0.07)

        # y=3x 直线（x∈[0,3]）
        line_plot = ax.plot(lambda x: 3*x, x_range=[0, 2.9],
                             color=C_GOLD, stroke_width=2.5)
        line_lbl = MathTex(r"y=3x", font_size=18, color=C_GOLD
                           ).next_to(ax.c2p(2.5, 7.5), RIGHT, buff=0.05)

        # ── 动画 ──────────────────────────────────────
        self.play(Write(title), run_time=0.6)
        self.play(Create(ax), FadeIn(ax_lbls), run_time=0.6)
        self.play(FadeIn(pt_dot), Write(pt_lbl), run_time=0.4)

        for i in range(len(calc_items)):
            self.play(FadeIn(calc_labels[i]), Write(calc_formulas[i]),
                      run_time=0.5)
            if i == 1:   # 代入后停顿
                self.wait(0.3)
            if i == 2:   # 解出k=3，高亮
                self.play(Create(k_box), Indicate(calc_formulas[2],
                          color=C_ORANGE, scale_factor=1.06), run_time=0.5)
                # 同时画直线
                self.play(Create(line_plot), Write(line_lbl), run_time=0.7)
            if i == 3:   # 结论
                self.play(Create(res_box), run_time=0.4)
                # 点高亮在线上
                self.play(Indicate(pt_dot, color=C_GOLD, scale_factor=1.5),
                          run_time=0.5)

        self.wait(1.5)
        self._clear(title, ax, ax_lbls, pt_dot, pt_lbl, line_plot, line_lbl,
                    k_box, res_box,
                    *calc_labels, *calc_formulas)

    # ══════════════════════════════════════════════════
    # Scene 4: 反比例函数可视化 (32–47s)
    # ══════════════════════════════════════════════════
    def scene4_inverse_example(self):
        title = self._title("④ 反比例函数：过 (2, -3)", color=C_RED, size=30)

        # ── 新问题说明 ─────────────────────────────────
        prob = Text("反比例函数过点 (2, -3)，求解析式",
                    font_size=24, color=C_WHITE,
                    font="PingFang SC").move_to(UP * 3.5)

        # ── 左侧计算 ──────────────────────────────────
        calc_items = [
            ("设",  MathTex(r"y = \dfrac{k}{x}", font_size=28, color=C_WHITE)),
            ("代入", MathTex(r"-3 = \dfrac{k}{2}", font_size=28, color=C_WHITE)),
            ("解得", MathTex(r"k = -6", font_size=34, color=C_RED)),
            ("结论", MathTex(r"y = \dfrac{-6}{x}", font_size=36, color=C_GOLD)),
        ]
        calc_ys = [2.0, 0.6, -0.7, -2.1]
        calc_x  = -2.3

        calc_labels = []
        calc_formulas = []
        for (lbl_str, fml), cy in zip(calc_items, calc_ys):
            lbl = Text(lbl_str, font_size=22, color=C_GRAY,
                       font="PingFang SC").move_to([calc_x - 0.7, cy, 0])
            fml.move_to([calc_x + 0.6, cy, 0])
            calc_labels.append(lbl)
            calc_formulas.append(fml)

        k_box  = SurroundingRectangle(calc_formulas[2], color=C_RED,
                                       buff=0.14, corner_radius=0.08)
        res_box = SurroundingRectangle(calc_formulas[3], color=C_GOLD,
                                        buff=0.14, corner_radius=0.1)

        # ── 右侧坐标轴 ────────────────────────────────
        # center=(2.0,-0.8), x_range=(-4,4), x_length=3.5, y_length=3.5
        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=3.5,
            y_length=3.5,
            axis_config={"color": C_GRAY, "stroke_width": 1.5,
                         "include_tip": True, "tip_length": 0.14,
                         "include_numbers": False},
        ).move_to(RIGHT * 2.0 + DOWN * 0.8)

        ax_lbls = VGroup(
            MathTex(r"x", font_size=18, color=C_GRAY).next_to(
                ax.x_axis.get_right(), RIGHT, buff=0.05),
            MathTex(r"y", font_size=18, color=C_GRAY).next_to(
                ax.y_axis.get_top(), UP, buff=0.05),
        )

        # 目标点 (2,-3)
        pt_dot = Dot(ax.c2p(2, -3), color=C_ORANGE, radius=0.1)
        pt_lbl = MathTex(r"(2,-3)", font_size=16, color=C_ORANGE
                         ).next_to(ax.c2p(2, -3), DR, buff=0.07)

        # y=-6/x 曲线（k=-6，在二四象限）
        curve_r = ax.plot(lambda x: -6/x, x_range=[1.6, 4.0, 0.05],
                           color=C_RED, stroke_width=2.5)
        curve_l = ax.plot(lambda x: -6/x, x_range=[-4.0, -1.6, 0.05],
                           color=C_RED, stroke_width=2.5)
        # 补充 x 接近0的部分（截断在 y_range 内）
        curve_r2 = ax.plot(lambda x: -6/x, x_range=[0.5, 1.6, 0.03],
                            color=C_RED, stroke_width=2.5)
        curve_l2 = ax.plot(lambda x: -6/x, x_range=[-1.6, -0.5, 0.03],
                            color=C_RED, stroke_width=2.5)

        # ── 动画 ──────────────────────────────────────
        self.play(Write(title), FadeIn(prob), run_time=0.6)
        self.play(Create(ax), FadeIn(ax_lbls), run_time=0.6)
        self.play(FadeIn(pt_dot), Write(pt_lbl), run_time=0.4)

        for i in range(len(calc_items)):
            self.play(FadeIn(calc_labels[i]), Write(calc_formulas[i]),
                      run_time=0.5)
            if i == 2:
                self.play(Create(k_box),
                          Indicate(calc_formulas[2], color=C_RED,
                                   scale_factor=1.06), run_time=0.5)
                self.play(
                    Create(curve_r), Create(curve_l),
                    Create(curve_r2), Create(curve_l2),
                    run_time=0.9,
                )
            if i == 3:
                self.play(Create(res_box), run_time=0.4)
                self.play(Indicate(pt_dot, color=C_GOLD, scale_factor=1.5),
                          run_time=0.5)

        self.wait(1.5)
        self._clear(title, prob, ax, ax_lbls, pt_dot, pt_lbl,
                    curve_r, curve_l, curve_r2, curve_l2,
                    k_box, res_box,
                    *calc_labels, *calc_formulas)

    # ══════════════════════════════════════════════════
    # Scene 5: 对比总结 (47–60s)
    # ══════════════════════════════════════════════════
    def scene5_comparison(self):
        title = self._title("⑤ 对比总结", color=C_GOLD, size=36)

        # 两列对比表
        col_x_l  = -2.4   # 正比例列中心
        col_x_r  =  1.8   # 反比例列中心
        rows_y   = [2.6, 1.2, 0.0, -1.2]
        row_lbls = ["① 设", "② 代", "③ 解", "④ 写"]

        # 表头
        hdr_l = Text("正比例函数", font_size=26, color=C_BLUE,
                     font="PingFang SC").move_to([col_x_l, 3.8, 0])
        hdr_r = Text("反比例函数", font_size=26, color=C_ORANGE,
                     font="PingFang SC").move_to([col_x_r, 3.8, 0])
        hdr_line = Line([-3.8, 3.35, 0], [3.8, 3.35, 0],
                        color=C_GRAY, stroke_width=1.5)
        hdr_vsep = Line([-0.3, 3.35, 0], [-0.3, -1.65, 0],
                        color=C_GRAY, stroke_width=1.0)

        linear_content = [
            MathTex(r"y = kx",    font_size=28, color=C_BLUE),
            Text("代入 (2, 6)",   font_size=24, color=C_WHITE, font="PingFang SC"),
            MathTex(r"k = 3",     font_size=28, color=C_BLUE),
            MathTex(r"y = 3x",    font_size=28, color=C_BLUE),
        ]
        inverse_content = [
            MathTex(r"y = \dfrac{k}{x}", font_size=26, color=C_ORANGE),
            Text("代入 (2, -3)",  font_size=24, color=C_WHITE, font="PingFang SC"),
            MathTex(r"k = -6",    font_size=28, color=C_ORANGE),
            MathTex(r"y = \dfrac{-6}{x}", font_size=26, color=C_ORANGE),
        ]

        for content, cx in [(linear_content, col_x_l),
                             (inverse_content, col_x_r)]:
            for item, ry in zip(content, rows_y):
                item.move_to([cx, ry, 0])

        # 行标签（左侧）
        step_lbls = VGroup(*[
            Text(lbl, font_size=22, color=C_GRAY, font="PingFang SC"
                 ).move_to([-3.5, ry, 0])
            for lbl, ry in zip(row_lbls, rows_y)
        ])

        # 底部强调
        emphasis = Text("代入已知点坐标 → 解出待定系数 k",
                        font_size=24, color=C_GOLD,
                        font="PingFang SC").move_to(DOWN * 2.5)
        emph_box = SurroundingRectangle(emphasis, color=C_GOLD, buff=0.16,
                                         corner_radius=0.1)

        # 动画
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(hdr_l), FadeIn(hdr_r), Create(hdr_line),
                  Create(hdr_vsep), run_time=0.5)
        self.play(FadeIn(step_lbls), run_time=0.4)

        for i in range(4):
            self.play(
                FadeIn(linear_content[i]),
                FadeIn(inverse_content[i]),
                run_time=0.4,
            )

        self.play(Write(emphasis), Create(emph_box), run_time=0.6)
        self.play(Indicate(emphasis, color=C_GOLD, scale_factor=1.04),
                  run_time=0.6)
        self.wait(2.0)
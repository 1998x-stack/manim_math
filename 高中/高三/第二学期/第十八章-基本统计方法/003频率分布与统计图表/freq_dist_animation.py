"""
频率分布与统计图表 — Frequency Distribution & Statistical Charts
高三数学 第十八章 基本统计方法
TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  0. 开场钩子
  1. 频率分布表
  2. 频率分布直方图 (核心)
  3. 频率折线图 (在直方图上叠加)
  4. 累积频率图
  5. 茎叶图
  6. 汇总对比
  7. 片尾
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════════════
#  全局配置 — TikTok 竖屏
# ══════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG         = "#1a1a2e"
C_HIST     = "#3498db"   # 蓝  — 直方图
C_LINE     = "#e74c3c"   # 红  — 折线图
C_CUM      = "#9b59b6"   # 紫  — 累积
C_STEM     = "#2ecc71"   # 绿  — 茎叶
C_FORMULA  = "#f39c12"   # 橙  — 公式强调
C_GOLD     = GOLD
C_GRAY     = GRAY_B
C_WHITE    = WHITE
FONT       = "PingFang SC"

# ══════════════════════════════════════════════════
#  数据 (与 verify_geometry.py 对齐)
# ══════════════════════════════════════════════════
GROUPS       = ["[50,60)", "[60,70)", "[70,80)", "[80,90)", "[90,100]"]
FREQ_COUNTS  = np.array([3, 8, 14, 10, 5])
N_SAMPLE     = int(FREQ_COUNTS.sum())   # 40
CLASS_WIDTH  = 10.0
FREQS        = FREQ_COUNTS / N_SAMPLE
DENSITY      = FREQS / CLASS_WIDTH
CUM_FREQ     = np.cumsum(FREQS)
MID_POINTS   = np.array([55., 65., 75., 85., 95.])

# Axes 参数
AX_XMIN, AX_XMAX = 50, 100
AX_YMIN, AX_YMAX = 0.0, 0.040
AX_W, AX_H       = 6.5, 4.2      # 轴长度 (manim units)
AX_CY             = 0.8          # Axes 中心 y (主内容区)


# ══════════════════════════════════════════════════
#  Main Scene
# ══════════════════════════════════════════════════
class FreqDistAnimation(Scene):

    def construct(self):
        self.camera.background_color = BG
        self._build_axes_cache()

        self.s0_opening()
        self.s1_freq_table()
        self.s2_histogram()
        self.s3_polygon()
        self.s4_cumulative()
        self.s5_stem_leaf()
        self.s6_summary()
        self.s7_outro()

    # ─────────────────────────────────────────────
    #  内部工具
    # ─────────────────────────────────────────────
    def T(self, txt, size=26, color=C_WHITE, **kw):
        return Text(txt, font=FONT, font_size=size, color=color, **kw)

    def section_title(self, txt, color=C_GOLD):
        t = self.T(txt, size=36, color=color)
        t.move_to(UP * 6.1)
        return t

    def _build_axes_cache(self):
        """预计算坐标系，供后续场景复用"""
        self._axes = Axes(
            x_range=[AX_XMIN, AX_XMAX + 1, 10],
            y_range=[AX_YMIN, AX_YMAX, 0.010],
            x_length=AX_W,
            y_length=AX_H,
            axis_config={
                "color": C_GRAY,
                "stroke_width": 1.8,
                "include_tip": True,
                "tip_length": 0.18,
            },
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        ).move_to(np.array([0.3, AX_CY, 0]))

    def _fresh_axes(self):
        """每个需要坐标轴的场景调用，返回新对象"""
        ax = Axes(
            x_range=[AX_XMIN, AX_XMAX + 1, 10],
            y_range=[AX_YMIN, AX_YMAX, 0.010],
            x_length=AX_W,
            y_length=AX_H,
            axis_config={
                "color": C_GRAY,
                "stroke_width": 1.8,
                "include_tip": True,
                "tip_length": 0.18,
            },
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        ).move_to(np.array([0.3, AX_CY, 0]))
        return ax

    def _x_labels(self, ax):
        """x 轴刻度标签 (50,60,...,100)"""
        labels = VGroup()
        for val in range(AX_XMIN, AX_XMAX + 1, 10):
            pt = ax.c2p(val, 0)
            lbl = self.T(str(val), size=16, color=C_GRAY)
            lbl.move_to(pt + DOWN * 0.32)
            labels.add(lbl)
        return labels

    def _y_label_txt(self, ax):
        """y 轴说明标签"""
        lbl = self.T("频率/组距", size=18, color=C_GRAY)
        lbl.rotate(PI / 2)
        # 放在 y 轴左侧
        ax_left = ax.get_left()
        lbl.move_to(ax_left + LEFT * 0.65)
        return lbl

    def _build_bars(self, ax, color=C_HIST, opacity=0.85):
        """构建频率直方图 5 个矩形"""
        bars = VGroup()
        x_edges = [50, 60, 70, 80, 90, 100]
        for i, d in enumerate(DENSITY):
            x0 = ax.c2p(x_edges[i],   0)
            x1 = ax.c2p(x_edges[i+1], d)
            w  = x1[0] - x0[0]
            h  = x1[1] - x0[1]
            bar = Rectangle(
                width=w, height=h,
                fill_color=color,
                fill_opacity=opacity,
                stroke_color=C_WHITE,
                stroke_width=1.2,
            )
            bar.move_to(np.array([
                (x0[0] + x1[0]) / 2,
                (x0[1] + x1[1]) / 2,
                0
            ]))
            bars.add(bar)
        return bars

    def _build_polygon_points(self, ax):
        """返回折线图点列 (含两端补零点)"""
        pts = []
        # 左补零
        pts.append(ax.c2p(AX_XMIN, 0))
        for mid, d in zip(MID_POINTS, DENSITY):
            pts.append(ax.c2p(mid, d))
        # 右补零
        pts.append(ax.c2p(AX_XMAX, 0))
        return pts

    def formula_box(self, tex_str, label_str=None, color=C_FORMULA, cy=-5.5):
        formula = MathTex(tex_str, font_size=36, color=color)
        formula.move_to(UP * cy)
        bg = RoundedRectangle(
            width=7.2, height=1.0,
            corner_radius=0.18,
            fill_color=color, fill_opacity=0.12,
            stroke_color=color, stroke_width=1.8
        ).move_to(formula.get_center())
        grp = VGroup(bg, formula)
        if label_str:
            lbl = self.T(label_str, size=19, color=color)
            lbl.next_to(bg, UP, buff=0.1)
            grp.add(lbl)
        return grp

    def summary_card(self, header, body_lines, color, cy):
        bg = RoundedRectangle(
            width=7.8, height=1.4,
            corner_radius=0.2,
            fill_color=color, fill_opacity=0.12,
            stroke_color=color, stroke_width=2.0
        ).move_to(np.array([0, cy, 0]))
        bar = Rectangle(
            width=0.18, height=1.4,
            fill_color=color, fill_opacity=1, stroke_width=0
        ).move_to(np.array([-3.81, cy, 0]))
        h = self.T(header, size=24, color=color)
        h.move_to(np.array([0.2, cy + 0.30, 0]))
        b = self.T(body_lines, size=18, color=C_WHITE)
        b.move_to(np.array([0.2, cy - 0.22, 0]))
        return VGroup(bg, bar, h, b)

    # ─────────────────────────────────────────────
    #  Scene 0: 开场钩子
    # ─────────────────────────────────────────────
    def s0_opening(self):
        self.author = self.T("上海初高中数学直通车 @emptyandcalm",
                              size=18, color=C_GRAY).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.15), run_time=0.3)

        hook = self.T("40人的考试成绩\n怎么直观呈现?", size=40, color=C_GOLD)
        hook.move_to(UP * 5.3)
        sub = self.T("频率分布图表全解析", size=27, color=C_GRAY)
        sub.move_to(UP * 4.0)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 简单柱状草图作钩子
        rough_bars = VGroup()
        heights = [0.6, 1.6, 2.8, 2.0, 1.0]
        colors_ = [C_HIST] * 5
        for i, (ht, col) in enumerate(zip(heights, colors_)):
            bx = -2.0 + i * 1.0
            bar = Rectangle(width=0.82, height=ht,
                             fill_color=col, fill_opacity=0.7,
                             stroke_color=C_WHITE, stroke_width=1)
            bar.move_to(np.array([bx, 1.5 + ht / 2 - 1.4, 0]))
            rough_bars.add(bar)

        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in rough_bars], lag_ratio=0.12),
            run_time=1.2
        )
        self.wait(0.5)
        self.play(FadeOut(hook), FadeOut(sub), FadeOut(rough_bars), run_time=0.5)

    # ─────────────────────────────────────────────
    #  Scene 1: 频率分布表
    # ─────────────────────────────────────────────
    def s1_freq_table(self):
        title = self.section_title("频率分布表", color=C_GOLD)
        self.play(Write(title), run_time=0.5)

        intro = self.T("将40人成绩分成5组", size=26, color=C_WHITE)
        intro.move_to(UP * 4.9)
        self.play(FadeIn(intro), run_time=0.3)

        # 表格标题行
        col_headers = ["区间", "频数", "频率", "频率/组距"]
        col_xs      = [-3.0, -0.9, 0.9, 2.9]
        header_y    = 3.5

        headers = VGroup()
        for hdr, cx in zip(col_headers, col_xs):
            t = self.T(hdr, size=20, color=C_GOLD)
            t.move_to(np.array([cx, header_y, 0]))
            headers.add(t)

        # 表头分割线
        h_line = Line(
            np.array([-3.8, header_y - 0.32, 0]),
            np.array([ 3.8, header_y - 0.32, 0]),
            color=C_GRAY, stroke_width=1.5
        )

        self.play(FadeIn(headers), Create(h_line), run_time=0.5)

        # 数据行
        row_y_start = 2.9
        row_h       = 0.65
        row_groups  = VGroup()

        for i, (grp, cnt, freq, dens) in enumerate(
            zip(GROUPS, FREQ_COUNTS, FREQS, DENSITY)
        ):
            ry = row_y_start - i * row_h
            vals = [grp, str(cnt), f"{freq:.3f}", f"{dens:.4f}"]
            row = VGroup()
            for val, cx in zip(vals, col_xs):
                size_ = 19 if val == grp else 20
                col_  = C_HIST if i == 2 else C_WHITE   # 高亮频率最大组
                t = self.T(val, size=size_, color=col_)
                t.move_to(np.array([cx, ry, 0]))
                row.add(t)
            row_groups.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in row_groups],
                        lag_ratio=0.2),
            run_time=1.2
        )

        # 强调"频率之和=1"
        sum_note = self.T("所有频率之和 = 1", size=22, color=C_FORMULA)
        sum_note.move_to(UP * 0.3)
        box_note = SurroundingRectangle(sum_note, color=C_FORMULA, buff=0.12,
                                        stroke_width=1.5, corner_radius=0.1)
        self.play(FadeIn(sum_note), Create(box_note), run_time=0.5)

        # 公式
        freq_rate = Text("频率", font=FONT, font_size=32, color=C_FORMULA)
        eq1       = MathTex(r"=", font_size=32, color=C_FORMULA)
        freq_num1 = Text("频数", font=FONT, font_size=32, color=C_FORMULA)
        div_n     = MathTex(r"\div\, n", font_size=32, color=C_FORMULA)
        eq2       = MathTex(r"=", font_size=32, color=C_FORMULA)
        freq_num2 = Text("频数", font=FONT, font_size=32, color=C_FORMULA)
        div_40    = MathTex(r"\div\, 40", font_size=32, color=C_FORMULA)

        fbox_row = VGroup(freq_rate, eq1, freq_num1, div_n,
                        eq2, freq_num2, div_40)\
                .arrange(RIGHT, buff=0.12)\
                .move_to(UP * (-5.5))
        fbox_bg = RoundedRectangle(
            width=7.2, height=1.0, corner_radius=0.18,
            fill_color=C_FORMULA, fill_opacity=0.12,
            stroke_color=C_FORMULA, stroke_width=1.8
        ).move_to(fbox_row.get_center())
        fbox = VGroup(fbox_bg, fbox_row)
        self.play(FadeIn(fbox), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(intro), FadeOut(headers),
            FadeOut(h_line), FadeOut(row_groups),
            FadeOut(sum_note), FadeOut(box_note), FadeOut(fbox),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  Scene 2: 频率分布直方图
    # ─────────────────────────────────────────────
    def s2_histogram(self):
        title = self.section_title("频率分布直方图", color=C_HIST)
        self.play(Write(title), run_time=0.5)

        ax = self._fresh_axes()
        x_lbls = self._x_labels(ax)
        y_lbl  = self._y_label_txt(ax)

        # 轴标题
        x_axis_title = self.T("成绩", size=20, color=C_GRAY)
        x_axis_title.next_to(ax.x_axis.get_right(), RIGHT, buff=0.1).shift(DOWN * 0.2)
        y_axis_title = self.T("频率/组距", size=18, color=C_GRAY)
        y_axis_title.rotate(PI / 2)
        y_axis_title.next_to(ax.y_axis.get_top(), UP, buff=0.1)

        self.play(Create(ax), FadeIn(x_lbls), run_time=0.8)
        self.play(FadeIn(y_axis_title), run_time=0.3)

        # 逐个生长柱形
        bars = self._build_bars(ax)
        for bar in bars:
            self.play(GrowFromEdge(bar, DOWN), run_time=0.35)

        # 柱顶频率标注
        bar_labels = VGroup()
        x_edges = [50, 60, 70, 80, 90, 100]
        for i, (d, freq) in enumerate(zip(DENSITY, FREQS)):
            bar_top_pt = ax.c2p((x_edges[i] + x_edges[i+1]) / 2, d)
            lbl = self.T(f"{freq:.3f}", size=16, color=C_HIST)
            lbl.move_to(bar_top_pt + UP * 0.25)
            bar_labels.add(lbl)

        self.play(
            LaggedStart(*[FadeIn(l) for l in bar_labels], lag_ratio=0.1),
            run_time=0.6
        )

        # 核心公式: 面积 = 频率
        area_note = self.T("矩形面积 = 频率/组距 × 组距 = 频率", size=21, color=C_FORMULA)
        area_note.move_to(DOWN * 2.5)
        self.play(FadeIn(area_note), run_time=0.4)

        # 高亮最大柱 (i=2: [70,80))
        highlight_bar = bars[2].copy()
        highlight_bar.set_fill(color=C_GOLD, opacity=0.5)
        self.play(FadeIn(highlight_bar), run_time=0.35)

        biggest_label = self.T("频率最大: 35%", size=22, color=C_GOLD)
        biggest_label.move_to(DOWN * 3.3)
        self.play(FadeIn(biggest_label), run_time=0.3)

        # 公式框
        fbox = self.formula_box(
            r"\sum \frac{f_i}{d} \cdot d = \sum f_i = 1",
            label_str="所有矩形面积之和 = 1",
            color=C_HIST, cy=-5.5
        )
        self.play(FadeIn(fbox), run_time=0.4)
        self.wait(1.2)

        # 保存 ax 和 bars 供下一场景复用
        self._hist_ax   = ax
        self._hist_bars = bars
        self._hist_barlabels = bar_labels

        self.play(
            FadeOut(title),
            FadeOut(x_lbls), FadeOut(y_axis_title),
            FadeOut(bar_labels), FadeOut(area_note),
            FadeOut(highlight_bar), FadeOut(biggest_label),
            FadeOut(fbox),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  Scene 3: 频率折线图 (叠加在直方图上)
    # ─────────────────────────────────────────────
    def s3_polygon(self):
        ax   = self._hist_ax
        bars = self._hist_bars

        title = self.section_title("频率折线图", color=C_LINE)
        self.play(Write(title), run_time=0.5)

        # x 轴标签
        x_lbls = self._x_labels(ax)
        self.play(FadeIn(x_lbls), run_time=0.2)

        # 折线点
        pts = self._build_polygon_points(ax)
        dots = VGroup(*[
            Dot(pt, radius=0.09, color=C_LINE, fill_opacity=1)
            for pt in pts[1:-1]   # 不含补零端点
        ])

        # 折线段
        lines = VGroup()
        for i in range(len(pts) - 1):
            seg = Line(pts[i], pts[i+1], color=C_LINE, stroke_width=2.5)
            lines.add(seg)

        # 说明
        explain = self.T("连接各矩形顶端中点", size=23, color=C_WHITE)
        explain.move_to(DOWN * 2.5)
        self.play(FadeIn(explain), run_time=0.3)

        # 逐段画折线
        self.play(
            LaggedStart(*[Create(seg) for seg in lines], lag_ratio=0.15),
            run_time=1.0
        )
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.1),
            run_time=0.5
        )

        # 封闭区域填充
        area_poly = Polygon(
            *pts,
            fill_color=C_LINE,
            fill_opacity=0.15,
            stroke_width=0
        )
        self.play(FadeIn(area_poly), run_time=0.4)

        note = self.T("封闭面积 = 1  (对应概率密度曲线)", size=20, color=C_GRAY)
        note.move_to(DOWN * 3.3)
        self.play(FadeIn(note), run_time=0.3)

        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(x_lbls),
            FadeOut(lines), FadeOut(dots), FadeOut(area_poly),
            FadeOut(bars), FadeOut(ax),
            FadeOut(explain), FadeOut(note),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    #  Scene 4: 累积频率图
    # ─────────────────────────────────────────────
    def s4_cumulative(self):
        title = self.section_title("累积频率图", color=C_CUM)
        self.play(Write(title), run_time=0.5)

        # 新坐标轴: y 轴范围 [0,1]
        ax_cum = Axes(
            x_range=[AX_XMIN, AX_XMAX + 1, 10],
            y_range=[0.0, 1.05, 0.25],
            x_length=AX_W,
            y_length=AX_H,
            axis_config={"color": C_GRAY, "stroke_width": 1.8,
                         "include_tip": True, "tip_length": 0.18},
        ).move_to(np.array([0.3, AX_CY, 0]))

        x_lbls = self._x_labels(ax_cum)

        # y 刻度 0, 0.25, 0.50, 0.75, 1.00
        y_lbls = VGroup()
        for val in [0.0, 0.25, 0.50, 0.75, 1.00]:
            pt  = ax_cum.c2p(AX_XMIN, val)
            lbl = self.T(f"{val:.2f}", size=15, color=C_GRAY)
            lbl.move_to(pt + LEFT * 0.52)
            y_lbls.add(lbl)

        y_title = self.T("累积频率", size=18, color=C_GRAY)
        y_title.rotate(PI / 2)
        y_title.next_to(ax_cum.y_axis.get_top(), UP, buff=0.1)

        self.play(Create(ax_cum), FadeIn(x_lbls), FadeIn(y_lbls),
                  FadeIn(y_title), run_time=0.8)

        # 累积频率折线点: x 在各段右端
        cum_xs = [60, 70, 80, 90, 100]
        cum_pts = [ax_cum.c2p(AX_XMIN, 0)]     # 起点 (50, 0)
        for x, cy in zip(cum_xs, CUM_FREQ):
            cum_pts.append(ax_cum.c2p(x, cy))

        cum_dots = VGroup(*[
            Dot(pt, radius=0.10, color=C_CUM) for pt in cum_pts
        ])
        cum_segs = VGroup(*[
            Line(cum_pts[i], cum_pts[i+1], color=C_CUM, stroke_width=2.8)
            for i in range(len(cum_pts) - 1)
        ])

        # 累积频率值标注
        cum_labels = VGroup()
        for pt, val in zip(cum_pts[1:], CUM_FREQ):
            lbl = self.T(f"{val:.3f}", size=16, color=C_CUM)
            lbl.move_to(np.array([pt[0], pt[1] + 0.3, 0]))
            cum_labels.add(lbl)

        self.play(
            LaggedStart(*[Create(s) for s in cum_segs], lag_ratio=0.18),
            run_time=0.9
        )
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in cum_dots], lag_ratio=0.1),
            run_time=0.5
        )
        self.play(FadeIn(cum_labels), run_time=0.4)

        # 读值演示: 80分以下有多少人?
        demo_x = 80
        demo_y = CUM_FREQ[2]   # 0.625
        demo_pt = ax_cum.c2p(demo_x, demo_y)
        origin_x = ax_cum.c2p(demo_x, 0)
        origin_y = ax_cum.c2p(AX_XMIN, demo_y)

        dashed_v = DashedLine(origin_x, demo_pt, color=C_FORMULA,
                               dash_length=0.1, stroke_width=1.8)
        dashed_h = DashedLine(origin_y, demo_pt, color=C_FORMULA,
                               dash_length=0.1, stroke_width=1.8)
        read_dot  = Dot(demo_pt, radius=0.12, color=C_FORMULA)
        read_note = self.T("80分以下: 62.5%", size=22, color=C_FORMULA)
        read_note.move_to(DOWN * 2.8)

        self.play(Create(dashed_v), Create(dashed_h), run_time=0.5)
        self.play(FadeIn(read_dot, scale=0.4), FadeIn(read_note), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(ax_cum), FadeOut(x_lbls), FadeOut(y_lbls),
            FadeOut(y_title), FadeOut(cum_dots), FadeOut(cum_segs),
            FadeOut(cum_labels), FadeOut(dashed_v), FadeOut(dashed_h),
            FadeOut(read_dot), FadeOut(read_note),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  Scene 5: 茎叶图
    # ─────────────────────────────────────────────
    def s5_stem_leaf(self):
        title = self.section_title("茎叶图", color=C_STEM)
        self.play(Write(title), run_time=0.5)

        subtitle = self.T("适合小样本，保留原始数据", size=23, color=C_GRAY)
        subtitle.move_to(UP * 4.9)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 示例数据 (精简，12人)
        stem_data = {
            5: [2, 5, 8],
            6: [1, 3, 6, 9],
            7: [0, 4, 7],
            8: [2, 6],
        }

        stems   = sorted(stem_data.keys())
        stem_cx = 0.0   # 茎的 x 中心
        leaf_x0 = 0.6   # 叶片起始 x
        row_h   = 0.7
        top_y   = 2.8

        # 竖线分隔茎叶
        div_line = Line(
            np.array([stem_cx + 0.28, top_y + 0.3, 0]),
            np.array([stem_cx + 0.28, top_y - len(stems) * row_h - 0.1, 0]),
            color=C_GRAY, stroke_width=1.8
        )

        # 表头
        stem_hdr = self.T("茎", size=22, color=C_GOLD)
        stem_hdr.move_to(np.array([stem_cx - 0.15, top_y + 0.5, 0]))
        leaf_hdr = self.T("叶", size=22, color=C_GOLD)
        leaf_hdr.move_to(np.array([leaf_x0 + 0.5, top_y + 0.5, 0]))

        self.play(Create(div_line), FadeIn(stem_hdr), FadeIn(leaf_hdr), run_time=0.4)

        stem_labels = VGroup()
        leaf_groups = VGroup()

        for k, s in enumerate(stems):
            ry = top_y - k * row_h

            # 茎
            st = self.T(str(s), size=24, color=C_STEM)
            st.move_to(np.array([stem_cx - 0.1, ry, 0]))
            stem_labels.add(st)

            # 叶
            leaves = VGroup()
            for j, leaf in enumerate(stem_data[s]):
                lf = self.T(str(leaf), size=24, color=C_WHITE)
                lf.move_to(np.array([leaf_x0 + j * 0.45, ry, 0]))
                leaves.add(lf)
            leaf_groups.add(leaves)

        # 逐行动画
        for k in range(len(stems)):
            self.play(
                FadeIn(stem_labels[k]),
                LaggedStart(*[FadeIn(lf, scale=0.5)
                               for lf in leaf_groups[k]], lag_ratio=0.12),
                run_time=0.5
            )

        # 读值: 茎5叶8 = 58分
        read_box = SurroundingRectangle(
            VGroup(stem_labels[0], leaf_groups[0][-1]),
            color=C_FORMULA, buff=0.12, corner_radius=0.1
        )
        read_note = self.T("茎5 叶8 → 58分", size=22, color=C_FORMULA)
        read_note.move_to(DOWN * 1.0)
        self.play(Create(read_box), FadeIn(read_note), run_time=0.5)
        self.wait(0.8)

        # 优点说明
        pro = self.T("✓ 保留原始数据\n✓ 便于排序比较", size=21, color=C_GRAY)
        pro.move_to(DOWN * 2.2)
        self.play(FadeIn(pro), run_time=0.3)
        self.wait(0.7)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(div_line), FadeOut(stem_hdr), FadeOut(leaf_hdr),
            FadeOut(stem_labels), FadeOut(leaf_groups),
            FadeOut(read_box), FadeOut(read_note), FadeOut(pro),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  Scene 6: 汇总对比
    # ─────────────────────────────────────────────
    def s6_summary(self):
        title = self.T("四种统计图表对比", size=36, color=C_GOLD)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        cards_data = [
            ("频率分布表",   C_HIST,
             "精确数据 | 频率/组距 | 累积频率"),
            ("频率分布直方图", C_HIST,
             "面积=频率 | 纵轴=频率/组距 | 面积和=1"),
            ("频率折线图",   C_LINE,
             "连接顶端中点 | 近似概率密度曲线"),
            ("茎叶图",       C_STEM,
             "小样本 | 保留原始值 | 便于排序"),
        ]

        centers_y = [3.0, 1.4, -0.2, -1.8]
        cards = VGroup()
        for (hdr, col, body), cy in zip(cards_data, centers_y):
            cards.add(self.summary_card(hdr, body, col, cy))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.35)

        # 核心公式强调
        key = self.T("所有图表核心: 频率 = 频数 ÷ n", size=22, color=YELLOW)
        key.move_to(DOWN * 3.4)
        key_ul = Underline(key, color=YELLOW)
        self.play(Write(key), Create(key_ul), run_time=0.6)

        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(cards),
            FadeOut(key), FadeOut(key_ul),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  Scene 7: 片尾
    # ─────────────────────────────────────────────
    def s7_outro(self):
        author_big = self.T("上海初高中数学直通车", size=40, color=C_WHITE)
        author_big.move_to(UP * 1.9)
        author_id = self.T("@emptyandcalm", size=30, color=C_GRAY)
        author_id.move_to(UP * 1.0)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        follow = self.T("关注我，获得更多数学技巧!", size=30, color=C_GOLD)
        follow.move_to(DOWN * 0.05)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)

        # 迷你直方图装饰
        mini_h = [0.4, 1.0, 1.8, 1.3, 0.7]
        mini_bars = VGroup()
        cols_mini = [C_HIST, C_HIST, C_GOLD, C_HIST, C_HIST]
        for i, (ht, col) in enumerate(zip(mini_h, cols_mini)):
            bx = -1.8 + i * 0.9
            b = Rectangle(width=0.75, height=ht,
                          fill_color=col, fill_opacity=0.85,
                          stroke_color=C_WHITE, stroke_width=1.0)
            b.move_to(np.array([bx, -1.8 + ht / 2, 0]))
            mini_bars.add(b)

        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in mini_bars], lag_ratio=0.1),
            run_time=0.8
        )

        # 知识要点
        tips = [
            ("频率 = 频数 ÷ n",          C_HIST),
            ("面积 = 频率/组距 × 组距",   C_LINE),
            ("所有面积之和 = 1",           C_CUM),
        ]
        tip_group = VGroup()
        for j, (txt, col) in enumerate(tips):
            row = self.T(f"• {txt}", size=19, color=col)
            row.move_to(np.array([0, -3.0 - j * 0.58, 0]))
            tip_group.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in tip_group],
                        lag_ratio=0.2),
            run_time=0.8
        )

        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(mini_bars), FadeOut(tip_group),
            run_time=1.0
        )

# # 快速预览 (480p)
# manim -pql freq_dist_animation.py FreqDistAnimation

# # TikTok 发布 (1080p 60fps)
# manim -qh freq_dist_animation.py FreqDistAnimation
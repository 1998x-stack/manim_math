"""
数据的集中趋势 — Central Tendency Measures
高三数学 第十八章 基本统计方法
TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  0. 开场钩子
  1. 平均数 (均值)
  2. 加权平均数
  3. 中位数 (奇/偶数个)
  4. 众数
  5. 极端值影响对比
  6. 三种指标汇总 + 选用原则
  7. 片尾
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════════════
#  全局配置
# ══════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG       = "#1a1a2e"
C_MEAN   = "#3498db"   # 蓝  — 平均数
C_MED    = "#e74c3c"   # 红  — 中位数
C_MODE   = "#2ecc71"   # 绿  — 众数
C_WGHT   = "#9b59b6"   # 紫  — 加权平均
C_OUTL   = "#e67e22"   # 橙  — 极端值
C_GOLD   = GOLD
C_GRAY   = GRAY_B
C_WHITE  = WHITE
FONT     = "Noto Sans CJK SC"

# ══════════════════════════════════════════════════
#  数据 (与 verify_geometry.py 对齐)
# ══════════════════════════════════════════════════
DATA_ODD     = np.array([52, 63, 71, 74, 78, 82, 85, 85, 90], dtype=float)
DATA_EVEN    = np.array([62, 68, 74, 78, 85, 91], dtype=float)
DATA_MODE    = np.array([71, 74, 78, 78, 78, 82, 85, 90], dtype=float)
DATA_OUTLIER = np.array([60, 62, 65, 68, 70, 72, 75, 200], dtype=float)

# 加权平均
W_SCORE   = np.array([85.0, 70.0])
W_WEIGHTS = np.array([0.6, 0.4])

# 数轴映射参数
NL_Y   = 0.6     # 数轴 y 坐标
NL_X0  = -3.6    # 左端 x
NL_X1  =  3.6    # 右端 x
NL_MIN = 50.0
NL_MAX = 100.0


def v2x(val, vmin=NL_MIN, vmax=NL_MAX, x0=NL_X0, x1=NL_X1):
    """数值 → 屏幕 x 坐标"""
    return x0 + (val - vmin) / (vmax - vmin) * (x1 - x0)


# ══════════════════════════════════════════════════
#  Scene
# ══════════════════════════════════════════════════
class CentralTendency(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.s0_opening()
        self.s1_mean()
        self.s2_weighted_mean()
        self.s3_median()
        self.s4_mode()
        self.s5_outlier()
        self.s6_summary()
        self.s7_outro()

    # ─────────────────────────────────────────────
    #  工具方法
    # ─────────────────────────────────────────────
    def T(self, txt, size=26, color=C_WHITE, **kw):
        return Text(txt, font=FONT, font_size=size, color=color, **kw)

    def section_title(self, txt, color=C_GOLD):
        t = self.T(txt, size=36, color=color)
        t.move_to(UP * 6.1)
        return t

    def formula_box(self, tex_str, label=None, color=C_MEAN, cy=-5.4):
        f = MathTex(tex_str, font_size=38, color=color)
        f.move_to(UP * cy)
        bg = RoundedRectangle(
            width=7.4, height=1.05, corner_radius=0.18,
            fill_color=color, fill_opacity=0.12,
            stroke_color=color, stroke_width=1.8
        ).move_to(f.get_center())
        grp = VGroup(bg, f)
        if label:
            lbl = self.T(label, size=19, color=color)
            lbl.next_to(bg, UP, buff=0.1)
            grp.add(lbl)
        return grp

    def make_number_line(self, vmin=NL_MIN, vmax=NL_MAX,
                         step=10, y=NL_Y, color=C_GRAY):
        """绘制带刻度的数轴"""
        x0 = v2x(vmin, vmin, vmax)
        x1 = v2x(vmax, vmin, vmax)
        line = Line(
            np.array([NL_X0 - 0.1, y, 0]),
            np.array([NL_X1 + 0.1, y, 0]),
            color=color, stroke_width=2.0
        )
        ticks = VGroup()
        labels = VGroup()
        for val in np.arange(vmin, vmax + 1, step):
            x = v2x(val, vmin, vmax)
            tick = Line(
                np.array([x, y - 0.12, 0]),
                np.array([x, y + 0.12, 0]),
                color=color, stroke_width=1.5
            )
            lbl = self.T(str(int(val)), size=17, color=color)
            lbl.move_to(np.array([x, y - 0.38, 0]))
            ticks.add(tick)
            labels.add(lbl)
        return VGroup(line, ticks, labels)

    def place_data_dots(self, data, y=NL_Y, color=C_GRAY,
                        dot_r=0.10, vmin=NL_MIN, vmax=NL_MAX):
        """在数轴上放置数据点 + 值标签"""
        dots   = VGroup()
        labels = VGroup()
        # 统计重复值，向上堆叠
        from collections import Counter
        cnt = Counter(data.tolist())
        seen = {}
        for v in sorted(data):
            k = seen.get(v, 0)
            seen[v] = k + 1
            x = v2x(v, vmin, vmax)
            dy = k * (dot_r * 2 + 0.06)
            d = Dot(np.array([x, y + 0.15 + dy, 0]),
                    radius=dot_r, color=color, fill_opacity=0.9)
            dots.add(d)
            if k == 0:
                lbl = self.T(str(int(v)), size=15, color=C_GRAY)
                lbl.move_to(np.array([x, y - 0.6, 0]))
                labels.add(lbl)
        return dots, labels

    def indicator_line(self, val, label_txt, color,
                       y=NL_Y, vmin=NL_MIN, vmax=NL_MAX, up=True):
        """在数轴指定值处画竖线 + 标签"""
        x = v2x(val, vmin, vmax)
        direction = UP if up else DOWN
        arrow = Arrow(
            np.array([x, y + (0.35 if up else -0.35), 0]),
            np.array([x, y + (1.1 if up else -1.1), 0]),
            buff=0, color=color, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.2
        )
        lbl = self.T(label_txt, size=22, color=color)
        lbl.move_to(np.array([x, y + (1.5 if up else -1.55), 0]))
        return VGroup(arrow, lbl)

    def summary_card(self, header, body, color, cy):
        bg = RoundedRectangle(
            width=7.8, height=1.25, corner_radius=0.2,
            fill_color=color, fill_opacity=0.12,
            stroke_color=color, stroke_width=2.0
        ).move_to(np.array([0, cy, 0]))
        bar = Rectangle(
            width=0.18, height=1.25,
            fill_color=color, fill_opacity=1, stroke_width=0
        ).move_to(np.array([-3.81, cy, 0]))
        h = self.T(header, size=24, color=color)
        h.move_to(np.array([0.3, cy + 0.28, 0]))
        b = self.T(body, size=18, color=C_WHITE)
        b.move_to(np.array([0.3, cy - 0.22, 0]))
        return VGroup(bg, bar, h, b)

    # ─────────────────────────────────────────────
    #  S0: 开场钩子
    # ─────────────────────────────────────────────
    def s0_opening(self):
        self.author = self.T("上海初高中数学直通车 @emptyandcalm",
                              size=18, color=C_GRAY).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.15), run_time=0.3)

        hook = self.T("9人考试成绩\n哪个数最能代表全班?", size=38, color=C_GOLD)
        hook.move_to(UP * 5.2)
        sub = self.T("平均数 / 中位数 / 众数 全解析", size=24, color=C_GRAY)
        sub.move_to(UP * 3.9)
        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 数据散点预览
        nl = self.make_number_line()
        dots, val_lbs = self.place_data_dots(DATA_ODD)
        self.play(Create(nl), run_time=0.6)
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.1),
            run_time=0.9
        )
        self.play(FadeIn(val_lbs), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(hook), FadeOut(sub),
                  FadeOut(nl), FadeOut(dots), FadeOut(val_lbs),
                  run_time=0.5)

    # ─────────────────────────────────────────────
    #  S1: 平均数 (均值)
    # ─────────────────────────────────────────────
    def s1_mean(self):
        title = self.section_title("① 平均数（均值）", color=C_MEAN)
        self.play(Write(title), run_time=0.5)

        # 数据展示
        def_txt = self.T("所有数据之和 ÷ 数据个数", size=24, color=C_WHITE)
        def_txt.move_to(UP * 4.9)
        self.play(FadeIn(def_txt), run_time=0.3)

        # 数轴 + 9个点
        nl = self.make_number_line()
        dots, val_lbs = self.place_data_dots(DATA_ODD, color=C_MEAN)
        self.play(Create(nl), run_time=0.5)
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.08),
            FadeIn(val_lbs),
            run_time=0.9
        )

        # 步骤1: 求和
        sum_val = DATA_ODD.sum()
        sum_str = "+".join([str(int(v)) for v in DATA_ODD])
        step1_lbl = self.T(f"和 = {int(sum_val)}", size=24, color=C_MEAN)
        step1_lbl.move_to(DOWN * 0.8)

        # 全部点变色 → 求和动画
        self.play(
            LaggedStart(*[d.animate.set_color(YELLOW) for d in dots], lag_ratio=0.05),
            run_time=0.6
        )
        self.play(FadeIn(step1_lbl), run_time=0.3)

        # 步骤2: 除以 n=9
        step2_lbl = self.T(f"÷ 9 = {DATA_ODD.mean():.1f}", size=24, color=C_MEAN)
        step2_lbl.move_to(DOWN * 1.6)
        self.play(FadeIn(step2_lbl), run_time=0.3)

        # 恢复点颜色
        for d in dots:
            d.set_color(C_MEAN)

        # 均值指示线
        mean_val = DATA_ODD.mean()
        mean_ind = self.indicator_line(mean_val,
                                       f"x̄≈{mean_val:.1f}", C_MEAN, up=True)
        self.play(GrowArrow(mean_ind[0]), FadeIn(mean_ind[1]), run_time=0.5)

        # 公式框
        fbox = self.formula_box(
            r"\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}",
            label="均值公式", color=C_MEAN
        )
        self.play(FadeIn(fbox), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(def_txt),
            FadeOut(nl), FadeOut(dots), FadeOut(val_lbs),
            FadeOut(step1_lbl), FadeOut(step2_lbl),
            FadeOut(mean_ind), FadeOut(fbox),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  S2: 加权平均数
    # ─────────────────────────────────────────────
    def s2_weighted_mean(self):
        title = self.section_title("② 加权平均数", color=C_WGHT)
        self.play(Write(title), run_time=0.5)

        scenario = self.T("期末占60%，平时成绩占40%", size=24, color=C_WHITE)
        scenario.move_to(UP * 4.9)
        self.play(FadeIn(scenario), run_time=0.3)

        # 两个成绩块
        labels_data = [
            ("期末成绩", "85分", "权重 0.6", C_WGHT),
            ("平时成绩", "70分", "权重 0.4", C_MEAN),
        ]
        block_centers = [-2.0, 2.0]
        blocks = VGroup()

        for (name, score, weight, col), cx in zip(labels_data, block_centers):
            bg = RoundedRectangle(
                width=3.2, height=2.8, corner_radius=0.25,
                fill_color=col, fill_opacity=0.15,
                stroke_color=col, stroke_width=2.2
            ).move_to(np.array([cx, 2.5, 0]))
            t1 = self.T(name,   size=22, color=col)
            t2 = self.T(score,  size=36, color=col)
            t3 = self.T(weight, size=20, color=C_GRAY)
            t1.move_to(np.array([cx, 3.4, 0]))
            t2.move_to(np.array([cx, 2.6, 0]))
            t3.move_to(np.array([cx, 1.8, 0]))
            blocks.add(VGroup(bg, t1, t2, t3))

        self.play(FadeIn(blocks[0], shift=LEFT * 0.2), run_time=0.4)
        self.play(FadeIn(blocks[1], shift=RIGHT * 0.2), run_time=0.4)

        # 乘号与箭头
        times_labels = VGroup()
        for (_, score, weight, col), cx in zip(labels_data, block_centers):
            score_v  = float(score.replace("分", ""))
            weight_v = float(weight.replace("权重 ", ""))
            prod     = score_v * weight_v
            t = self.T(f"{score_v:.0f}×{weight_v} = {prod:.0f}", size=22, color=col)
            t.move_to(np.array([cx, 0.8, 0]))
            times_labels.add(t)

        self.play(FadeIn(times_labels), run_time=0.4)

        # 加法箭头
        plus_sign = self.T("+", size=38, color=C_GOLD).move_to(UP * 0.8)
        self.play(FadeIn(plus_sign), run_time=0.2)

        # 结果
        wm = float(np.dot(W_SCORE, W_WEIGHTS))
        result_bg = RoundedRectangle(
            width=5.5, height=1.0, corner_radius=0.2,
            fill_color=C_WGHT, fill_opacity=0.2,
            stroke_color=C_WGHT, stroke_width=2.0
        ).move_to(DOWN * 0.4)
        result_txt = self.T(f"加权平均 = 51 + 28 = {wm:.0f} 分",
                             size=26, color=C_WGHT)
        result_txt.move_to(result_bg.get_center())
        self.play(FadeIn(result_bg), Write(result_txt), run_time=0.6)

        # 公式框
        fbox = self.formula_box(
            r"\bar{x} = \frac{\sum w_i x_i}{\sum w_i}",
            label="加权均值公式", color=C_WGHT
        )
        self.play(FadeIn(fbox), run_time=0.4)

        note = self.T("权重之和 = 0.6+0.4 = 1", size=20, color=C_GRAY)
        note.move_to(DOWN * 3.0)
        self.play(FadeIn(note), run_time=0.3)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(scenario),
            FadeOut(blocks), FadeOut(times_labels),
            FadeOut(plus_sign), FadeOut(result_bg), FadeOut(result_txt),
            FadeOut(fbox), FadeOut(note),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  S3: 中位数
    # ─────────────────────────────────────────────
    def s3_median(self):
        title = self.section_title("③ 中位数", color=C_MED)
        self.play(Write(title), run_time=0.5)

        def_txt = self.T("从小到大排列后位于中间的数", size=24, color=C_WHITE)
        def_txt.move_to(UP * 4.9)
        self.play(FadeIn(def_txt), run_time=0.3)

        # ── 奇数 n=9 ──
        case1_lbl = self.T("n=9 (奇数): 第 5 个数", size=23, color=C_MED)
        case1_lbl.move_to(UP * 4.1)
        self.play(FadeIn(case1_lbl), run_time=0.3)

        nl = self.make_number_line()
        self.play(Create(nl), run_time=0.5)

        # 画 9 个点，从左到右
        sorted_data = np.sort(DATA_ODD)
        box_dots = VGroup()
        box_labels = VGroup()
        for i, v in enumerate(sorted_data):
            x = v2x(v)
            d = Dot(np.array([x, NL_Y + 0.22, 0]),
                    radius=0.11, color=C_MED, fill_opacity=0.8)
            lbl = self.T(str(int(v)), size=15, color=C_GRAY)
            lbl.move_to(np.array([x, NL_Y - 0.52, 0]))
            box_dots.add(d)
            box_labels.add(lbl)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in box_dots], lag_ratio=0.08),
            FadeIn(box_labels),
            run_time=0.9
        )

        # 编号 1~9
        num_labels = VGroup()
        for i, d in enumerate(box_dots):
            n = self.T(str(i + 1), size=14, color=C_GRAY)
            n.move_to(d.get_center() + UP * 0.28)
            num_labels.add(n)
        self.play(FadeIn(num_labels), run_time=0.3)

        # 高亮第5个点 (中位数 = 78)
        mid_dot = box_dots[4]
        self.play(mid_dot.animate.set_color(YELLOW).scale(1.6), run_time=0.4)
        med_ring = Circle(radius=0.22, color=C_MED, stroke_width=2.5
                          ).move_to(mid_dot.get_center())
        self.play(Create(med_ring), run_time=0.3)

        med_ind = self.indicator_line(sorted_data[4],
                                      f"中位数={int(sorted_data[4])}", C_MED)
        self.play(GrowArrow(med_ind[0]), FadeIn(med_ind[1]), run_time=0.4)

        # 公式框 (奇数)
        f1_tex = MathTex(r"M = x_{\frac{n+1}{2}}", font_size=36, color=C_MED)
        f1_cn  = Text("（n 为奇数）", font=FONT, font_size=26, color=C_MED)
        f1_row = VGroup(f1_tex, f1_cn).arrange(RIGHT, buff=0.25).move_to(UP * (-5.4))
        f1_bg  = RoundedRectangle(
            width=7.4, height=1.05, corner_radius=0.18,
            fill_color=C_MED, fill_opacity=0.12,
            stroke_color=C_MED, stroke_width=1.8
        ).move_to(f1_row.get_center())
        f1_lbl = self.T("中位数公式 (奇数)", size=19, color=C_MED)
        f1_lbl.next_to(f1_bg, UP, buff=0.1)
        fbox1  = VGroup(f1_bg, f1_row, f1_lbl)
        self.play(FadeIn(fbox1), run_time=0.4)
        self.wait(0.7)

        # 清理，展示偶数情况
        self.play(
            FadeOut(case1_lbl), FadeOut(nl), FadeOut(box_dots),
            FadeOut(box_labels), FadeOut(num_labels),
            FadeOut(med_ring), FadeOut(med_ind), FadeOut(fbox1),
            run_time=0.4
        )

        # ── 偶数 n=6 ──
        case2_lbl = self.T("n=6 (偶数): 第3、4个数的平均", size=23, color=C_MED)
        case2_lbl.move_to(UP * 4.1)
        self.play(FadeIn(case2_lbl), run_time=0.3)

        nl2 = self.make_number_line()
        self.play(Create(nl2), run_time=0.4)

        sorted_even = np.sort(DATA_EVEN)
        e_dots = VGroup()
        e_labels = VGroup()
        for i, v in enumerate(sorted_even):
            x = v2x(v)
            col = YELLOW if i in [2, 3] else C_MED
            d = Dot(np.array([x, NL_Y + 0.22, 0]),
                    radius=0.11, color=col, fill_opacity=0.9)
            lbl = self.T(str(int(v)), size=16, color=C_GRAY)
            lbl.move_to(np.array([x, NL_Y - 0.52, 0]))
            e_dots.add(d)
            e_labels.add(lbl)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in e_dots], lag_ratio=0.1),
            FadeIn(e_labels),
            run_time=0.7
        )

        # Brace 括住中间两个
        brace_grp = Brace(
            VGroup(e_dots[2], e_dots[3]), DOWN, color=C_MED
        )
        med_even = np.median(DATA_EVEN)
        brace_lbl = self.T(f"({int(sorted_even[2])}+{int(sorted_even[3])})/2 = {med_even:.0f}",
                            size=22, color=C_MED)
        brace_lbl.next_to(brace_grp, DOWN, buff=0.12)

        self.play(Create(brace_grp), FadeIn(brace_lbl), run_time=0.5)

        f2_tex = MathTex(
            r"M = \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}",
            font_size=34, color=C_MED
        )
        f2_cn  = Text("（n 为偶数）", font=FONT, font_size=26, color=C_MED)
        f2_row = VGroup(f2_tex, f2_cn).arrange(RIGHT, buff=0.2).move_to(UP * (-5.4))
        f2_bg  = RoundedRectangle(
            width=7.4, height=1.05, corner_radius=0.18,
            fill_color=C_MED, fill_opacity=0.12,
            stroke_color=C_MED, stroke_width=1.8
        ).move_to(f2_row.get_center())
        f2_lbl = self.T("中位数公式 (偶数)", size=19, color=C_MED)
        f2_lbl.next_to(f2_bg, UP, buff=0.1)
        fbox2  = VGroup(f2_bg, f2_row, f2_lbl)
        self.play(FadeIn(fbox2), run_time=0.4)
        self.wait(0.9)

        self.play(
            FadeOut(title), FadeOut(def_txt), FadeOut(case2_lbl),
            FadeOut(nl2), FadeOut(e_dots), FadeOut(e_labels),
            FadeOut(brace_grp), FadeOut(brace_lbl), FadeOut(fbox2),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  S4: 众数
    # ─────────────────────────────────────────────
    def s4_mode(self):
        title = self.section_title("④ 众数", color=C_MODE)
        self.play(Write(title), run_time=0.5)

        def_txt = self.T("出现次数最多的数据", size=26, color=C_WHITE)
        def_txt.move_to(UP * 4.9)
        self.play(FadeIn(def_txt), run_time=0.3)

        nl = self.make_number_line()
        self.play(Create(nl), run_time=0.4)

        # 用 DATA_MODE (78出现3次)
        sorted_mode = np.sort(DATA_MODE)
        m_dots = VGroup()
        m_labels = VGroup()
        from collections import Counter
        cnt = Counter(sorted_mode.tolist())
        seen = {}
        for v in sorted_mode:
            k = seen.get(v, 0)
            seen[v] = k + 1
            x = v2x(v)
            is_mode = (cnt[v] == max(cnt.values()))
            col = C_MODE if is_mode else C_GRAY
            dy = k * 0.26
            d = Dot(np.array([x, NL_Y + 0.2 + dy, 0]),
                    radius=0.11, color=col, fill_opacity=0.9)
            m_dots.add(d)
            if k == 0:
                lbl = self.T(str(int(v)), size=16, color=C_GRAY)
                lbl.move_to(np.array([x, NL_Y - 0.52, 0]))
                m_labels.add(lbl)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in m_dots], lag_ratio=0.08),
            FadeIn(m_labels),
            run_time=0.8
        )

        # 频率柱子 (小型柱状图叠在数轴上方)
        vals, counts = np.unique(sorted_mode, return_counts=True)
        bar_grp = VGroup()
        for v, c in zip(vals, counts):
            x = v2x(v)
            h = c * 0.35
            bar = Rectangle(
                width=0.3, height=h,
                fill_color=C_MODE if c == counts.max() else C_GRAY,
                fill_opacity=0.5, stroke_width=0
            )
            bar.move_to(np.array([x, NL_Y + 0.55 + h / 2, 0]))
            cnt_lbl = self.T(str(c), size=16, color=C_WHITE)
            cnt_lbl.move_to(bar.get_top() + UP * 0.18)
            bar_grp.add(VGroup(bar, cnt_lbl))

        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.1) for b in bar_grp], lag_ratio=0.1),
            run_time=0.7
        )

        # 众数指示
        mode_val = vals[np.argmax(counts)]
        mode_ind = self.indicator_line(mode_val, f"众数={int(mode_val)}", C_MODE)
        self.play(GrowArrow(mode_ind[0]), FadeIn(mode_ind[1]), run_time=0.4)

        note = self.T("78出现3次 → 众数=78", size=22, color=C_MODE)
        note.move_to(DOWN * 0.6)
        self.play(FadeIn(note), run_time=0.3)

        # 提示: 众数可以不唯一
        note2 = self.T("注: 众数可以有多个或不存在", size=20, color=C_GRAY)
        note2.move_to(DOWN * 1.4)
        self.play(FadeIn(note2), run_time=0.3)

        self.wait(0.9)

        self.play(
            FadeOut(title), FadeOut(def_txt),
            FadeOut(nl), FadeOut(m_dots), FadeOut(m_labels),
            FadeOut(bar_grp), FadeOut(mode_ind),
            FadeOut(note), FadeOut(note2),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  S5: 极端值影响对比
    # ─────────────────────────────────────────────
    def s5_outlier(self):
        title = self.section_title("极端值的影响", color=C_OUTL)
        self.play(Write(title), run_time=0.5)

        scenario = self.T("7人成绩正常, 1人成绩极高=200", size=23, color=C_WHITE)
        scenario.move_to(UP * 4.9)
        self.play(FadeIn(scenario), run_time=0.3)

        # 扩展数轴 [50, 210]
        vmin2, vmax2 = 50.0, 210.0

        def v2x2(val):
            return v2x(val, vmin=vmin2, vmax=vmax2)

        line2 = Line(
            np.array([NL_X0 - 0.1, NL_Y, 0]),
            np.array([NL_X1 + 0.1, NL_Y, 0]),
            color=C_GRAY, stroke_width=2.0
        )
        ticks2 = VGroup()
        for val in [50, 100, 150, 200]:
            x = v2x2(val)
            tick = Line(np.array([x, NL_Y - 0.12, 0]),
                        np.array([x, NL_Y + 0.12, 0]),
                        color=C_GRAY, stroke_width=1.5)
            lbl = self.T(str(val), size=17, color=C_GRAY)
            lbl.move_to(np.array([x, NL_Y - 0.38, 0]))
            ticks2.add(VGroup(tick, lbl))
        nl2 = VGroup(line2, ticks2)

        self.play(Create(nl2), run_time=0.5)

        # 8个点
        out_dots = VGroup()
        for v in DATA_OUTLIER:
            x = v2x2(v)
            is_out = (v >= 200)
            col = C_OUTL if is_out else C_MEAN
            d = Dot(np.array([x, NL_Y + 0.22, 0]),
                    radius=0.12, color=col, fill_opacity=0.9)
            out_dots.add(d)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in out_dots], lag_ratio=0.1),
            run_time=0.8
        )

        # 200分标注
        x200 = v2x2(200)
        outl_lbl = self.T("200!", size=24, color=C_OUTL)
        outl_lbl.move_to(np.array([x200, NL_Y + 0.7, 0]))
        arrow_outl = Arrow(
            np.array([x200, NL_Y + 0.5, 0]),
            np.array([x200, NL_Y + 0.28, 0]),
            buff=0, color=C_OUTL, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )
        self.play(FadeIn(outl_lbl), GrowArrow(arrow_outl), run_time=0.4)

        # 均值 vs 中位数
        mean4   = DATA_OUTLIER.mean()    # 84.0
        median4 = np.median(DATA_OUTLIER)  # 69.0

        x_mean4   = v2x2(mean4)
        x_median4 = v2x2(median4)

        mean_line = DashedLine(
            np.array([x_mean4, NL_Y - 0.15, 0]),
            np.array([x_mean4, NL_Y - 1.3, 0]),
            color=C_MEAN, dash_length=0.1, stroke_width=2.0
        )
        mean_lbl4 = self.T(f"均值={mean4:.0f}", size=22, color=C_MEAN)
        mean_lbl4.move_to(np.array([x_mean4, NL_Y - 1.6, 0]))

        med_line = DashedLine(
            np.array([x_median4, NL_Y - 0.15, 0]),
            np.array([x_median4, NL_Y - 1.3, 0]),
            color=C_MED, dash_length=0.1, stroke_width=2.0
        )
        med_lbl4 = self.T(f"中位数={median4:.0f}", size=22, color=C_MED)
        med_lbl4.move_to(np.array([x_median4, NL_Y - 1.6, 0]))

        self.play(Create(mean_line), FadeIn(mean_lbl4), run_time=0.4)
        self.play(Create(med_line),  FadeIn(med_lbl4),  run_time=0.4)

        # 对比说明
        compare = VGroup(
            self.T("均值被拉高到 84，失真!", size=22, color=C_MEAN),
            self.T("中位数仍是 69，稳健！", size=22, color=C_MED),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.2)
        self.play(FadeIn(compare), run_time=0.5)

        conclusion = self.T("极端值存在时 → 中位数更可靠", size=22, color=YELLOW)
        conclusion.move_to(DOWN * 4.4)
        self.play(FadeIn(conclusion), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(scenario), FadeOut(nl2),
            FadeOut(out_dots), FadeOut(outl_lbl), FadeOut(arrow_outl),
            FadeOut(mean_line), FadeOut(mean_lbl4),
            FadeOut(med_line), FadeOut(med_lbl4),
            FadeOut(compare), FadeOut(conclusion),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  S6: 汇总 + 选用原则
    # ─────────────────────────────────────────────
    def s6_summary(self):
        title = self.T("三种指标对比 & 选用原则", size=34, color=C_GOLD)
        title.move_to(UP * 6.1)
        self.play(Write(title), run_time=0.5)

        cards_data = [
            ("平均数 x̄", C_MEAN,
             "所有数据参与 | 受极端值影响大\n适用: 数据分布均匀时"),
            ("中位数 M", C_MED,
             "排序取中间值 | 不受极端值影响\n适用: 含极端值时"),
            ("众数 Mo", C_MODE,
             "出现最多的值 | 可有多个\n适用: 关注最高频数据时"),
        ]
        centers_y = [3.0, 1.2, -0.6]
        cards = VGroup()
        for (hdr, col, body), cy in zip(cards_data, centers_y):
            cards.add(self.summary_card(hdr, body, col, cy))

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.38)

        # 选用口诀
        rule_bg = RoundedRectangle(
            width=7.8, height=1.8, corner_radius=0.2,
            fill_color="#16213e", fill_opacity=0.95,
            stroke_color=YELLOW, stroke_width=1.8
        ).move_to(DOWN * 2.6)
        rule_txt = VGroup(
            self.T("有极端值 → 选中位数", size=22, color=YELLOW),
            self.T("均匀分布 → 选平均数", size=22, color=C_MEAN),
            self.T("最频繁值 → 选众数",   size=22, color=C_MODE),
        ).arrange(DOWN, buff=0.2).move_to(rule_bg.get_center())
        self.play(FadeIn(rule_bg), run_time=0.3)
        self.play(
            LaggedStart(*[Write(t) for t in rule_txt], lag_ratio=0.3),
            run_time=0.9
        )

        self.wait(1.8)
        self.play(
            FadeOut(title), FadeOut(cards),
            FadeOut(rule_bg), FadeOut(rule_txt),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    #  S7: 片尾
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

        # 三色圆图标装饰
        icons = VGroup(
            Circle(radius=0.28, fill_color=C_MEAN,
                   fill_opacity=0.9, stroke_width=0).shift(LEFT * 2.2 + DOWN * 1.8),
            Circle(radius=0.28, fill_color=C_MED,
                   fill_opacity=0.9, stroke_width=0).shift(DOWN * 1.8),
            Circle(radius=0.28, fill_color=C_MODE,
                   fill_opacity=0.9, stroke_width=0).shift(RIGHT * 2.2 + DOWN * 1.8),
        )
        icon_labels = VGroup(
            self.T("均值", size=15, color=C_WHITE).move_to(icons[0].get_center()),
            self.T("中位", size=15, color=C_WHITE).move_to(icons[1].get_center()),
            self.T("众数", size=15, color=C_WHITE).move_to(icons[2].get_center()),
        )
        self.play(*[GrowFromCenter(ic) for ic in icons], run_time=0.5)
        self.play(FadeIn(icon_labels), run_time=0.3)

        # 知识要点
        tips = [
            (r"\bar{x} = \frac{\sum x_i}{n}", C_MEAN),
            (r"M = x_{\frac{n+1}{2}}", C_MED),
            (r"Mo = \text{freq\_max}", C_MODE),
        ]
        tip_grp = VGroup()
        for j, (tex, col) in enumerate(tips):
            t = MathTex(tex, font_size=32, color=col)
            t.move_to(np.array([0, -3.0 - j * 0.7, 0]))
            tip_grp.add(t)

        self.play(
            LaggedStart(*[Write(t) for t in tip_grp], lag_ratio=0.25),
            run_time=0.9
        )

        self.wait(1.5)
        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(icons), FadeOut(icon_labels),
            FadeOut(tip_grp),
            run_time=1.0
        )

# # 快速预览 (480p)
# manim -pql central_tendency_animation.py CentralTendency

# # TikTok 发布 (1080p)
# manim -qh central_tendency_animation.py CentralTendency
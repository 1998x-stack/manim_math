"""
抽样技术 — Sampling Techniques Animation
高三数学 第十八章 基本统计方法
TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  1. 开场钩子
  2. 简单随机抽样 (抽签法 + 随机数表法)
  3. 系统抽样 (等距抽样)
  4. 分层抽样
  5. 三种方法对比汇总
  6. 片尾
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════
#  全局配置
# ══════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG        = "#1a1a2e"
C_SIMPLE  = "#e74c3c"   # 红  — 简单随机
C_SYS     = "#3498db"   # 蓝  — 系统抽样
C_STRAT   = "#2ecc71"   # 绿  — 分层抽样
C_SAMPLE  = "#f39c12"   # 橙  — 被抽中
C_GOLD    = GOLD
C_GRAY    = GRAY_B
C_WHITE   = WHITE
FONT      = "Noto Sans CJK SC"

# ══════════════════════════════════════════
#  几何常数 (与 verify_geometry.py 对齐)
# ══════════════════════════════════════════
DOT_SPACING = 0.65
GRID_COLS   = 8
GRID_ROWS   = 5          # 40 个体
GRID_CX     = 0.0
GRID_CY     = 1.8
N_POP       = GRID_COLS * GRID_ROWS   # 40
N_SAMPLE    = 5


def grid_pos(col, row,
             cx=GRID_CX, cy=GRID_CY,
             sp=DOT_SPACING, cols=GRID_COLS, rows=GRID_ROWS):
    """返回网格点 (col, row) 的坐标 np.array([x, y, 0])"""
    x = cx + (col - (cols - 1) / 2) * sp
    y = cy + (row - (rows - 1) / 2) * sp
    return np.array([x, y, 0.0])


def all_grid_positions():
    """返回 40 个点坐标列表，按 row-major 顺序"""
    pos = []
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            pos.append(grid_pos(col, row))
    return pos


# ══════════════════════════════════════════
#  Scene
# ══════════════════════════════════════════
class SamplingTechniques(Scene):

    def construct(self):
        self.camera.background_color = BG

        # 预计算所有个体坐标 (全局共享)
        self.all_pos = all_grid_positions()

        # 系统抽样参数: k=8, start=3
        self.sys_k     = N_POP // N_SAMPLE   # 8
        self.sys_start = 3
        self.sys_indices = [self.sys_start + i * self.sys_k for i in range(N_SAMPLE)]

        # 简单随机抽样被抽中索引 (固定随机种子)
        rng = np.random.default_rng(7)
        self.simple_indices = sorted(rng.choice(N_POP, N_SAMPLE, replace=False).tolist())

        # 分层参数: layers=[20,12,8], alloc=[5,3,2]
        self.layers      = [20, 12, 8]
        self.layer_alloc = [5, 3, 2]
        # 各层颜色
        self.layer_colors = ["#e8a838", "#5b9cf6", "#a0e080"]

        # 执行动画
        self.s0_opening()
        self.s1_simple_random()
        self.s2_systematic()
        self.s3_stratified()
        self.s4_summary()
        self.s5_outro()

    # ──────────────────────────────────────
    #  工具函数
    # ──────────────────────────────────────
    def T(self, txt, size=28, color=C_WHITE, **kw):
        return Text(txt, font=FONT, font_size=size, color=color, **kw)

    def make_dot(self, pos, color=C_GRAY, r=0.10):
        return Dot(pos, radius=r, color=color, fill_opacity=0.85)

    def build_grid_dots(self, highlight_indices=None,
                        hi_color=C_SAMPLE, base_color=C_GRAY):
        """返回 VGroup(40 dots)，highlight_indices 对应橙色"""
        hi_set = set(highlight_indices or [])
        dots = VGroup()
        for i, pos in enumerate(self.all_pos):
            c = hi_color if i in hi_set else base_color
            dots.add(self.make_dot(pos, color=c))
        return dots

    def section_title(self, txt, color=C_GOLD):
        t = self.T(txt, size=38, color=color)
        t.move_to(UP * 6.0)
        return t

    def formula_box(self, tex_str, label_str=None, box_color=C_SIMPLE):
        """公式 + 可选标签，底部区域"""
        formula = MathTex(tex_str, font_size=40, color=box_color)
        formula.move_to(DOWN * 5.2)
        bg = RoundedRectangle(
            width=7.2, height=1.05,
            corner_radius=0.18,
            fill_color=box_color, fill_opacity=0.12,
            stroke_color=box_color, stroke_width=1.8
        ).move_to(formula.get_center())
        grp = VGroup(bg, formula)
        if label_str:
            lbl = self.T(label_str, size=20, color=box_color)
            lbl.next_to(bg, UP, buff=0.12)
            grp.add(lbl)
        return grp

    def highlight_ring(self, dot, color=C_SAMPLE):
        return Circle(radius=0.18, color=color, stroke_width=2.5
                      ).move_to(dot.get_center())

    # ──────────────────────────────────────
    #  Scene 0: 开场钩子
    # ──────────────────────────────────────
    def s0_opening(self):
        # 作者标识
        self.author = self.T("上海初高中数学直通车 @emptyandcalm",
                              size=18, color=C_GRAY).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.15), run_time=0.3)

        hook = self.T("如何从40人中公平地\n抽取5人?", size=40, color=C_GOLD)
        hook.move_to(UP * 5.4)
        sub  = self.T("三种抽样方法全解析", size=28, color=C_GRAY)
        sub.move_to(UP * 4.2)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 展示 40 个点组成的人群
        dots = VGroup(*[self.make_dot(p) for p in self.all_pos])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.03),
            run_time=1.4
        )

        # 闪烁提问
        q = self.T("?", size=100, color=C_GOLD).move_to(GRID_CY * UP)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.4)
        self.play(FadeOut(q), FadeOut(hook), FadeOut(sub), FadeOut(dots),
                  run_time=0.5)

    # ──────────────────────────────────────
    #  Scene 1: 简单随机抽样
    # ──────────────────────────────────────
    def s1_simple_random(self):
        title = self.section_title("① 简单随机抽样", color=C_SIMPLE)
        self.play(Write(title), run_time=0.6)

        # 定义
        def_txt = self.T("每个个体被抽到的概率相等", size=26, color=C_WHITE)
        def_txt.move_to(UP * 4.9)
        self.play(FadeIn(def_txt), run_time=0.4)

        # 画所有 40 个灰点
        dots = VGroup(*[self.make_dot(p) for p in self.all_pos])
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.02),
            run_time=1.0
        )

        # ─ 方法1: 抽签法 ─
        method1 = self.T("方法1: 抽签法", size=26, color=C_SIMPLE)
        method1.move_to(DOWN * 0.4)
        self.play(FadeIn(method1), run_time=0.3)

        explain1 = self.T("给每人编号 → 抽取签条", size=22, color=C_GRAY)
        explain1.move_to(DOWN * 1.1)
        self.play(FadeIn(explain1), run_time=0.3)

        # 逐步高亮 simple_indices
        rings = VGroup()
        for idx in self.simple_indices:
            dot = dots[idx]
            self.play(
                dot.animate.set_color(C_SIMPLE).scale(1.4),
                run_time=0.25
            )
            ring = self.highlight_ring(dot, C_SIMPLE)
            self.play(Create(ring), run_time=0.2)
            rings.add(ring)

        self.wait(0.5)
        self.play(FadeOut(method1), FadeOut(explain1), run_time=0.3)

        # 恢复点颜色，清楚环
        for idx in self.simple_indices:
            dots[idx].set_color(C_GRAY).scale(1 / 1.4)
        self.play(FadeOut(rings), run_time=0.2)

        # ─ 方法2: 随机数表法 ─
        method2 = self.T("方法2: 随机数表法", size=26, color=C_SIMPLE)
        method2.move_to(DOWN * 0.4)
        self.play(FadeIn(method2), run_time=0.3)

        # 模拟随机数表 — 小数字网格
        num_strs = ["17", "83", "05", "39", "72",
                    "04", "61", "28", "90", "53",
                    "36", "14", "77", "02", "45"]
        num_group = VGroup()
        for k, s in enumerate(num_strs):
            col = k % 5
            row = k // 5
            x = -2.0 + col * 1.0
            y = -1.4 - row * 0.55
            t = Text(s, font="Courier New", font_size=24,
                     color=C_GRAY if s not in ["05","04","02","14","36"] else C_SIMPLE)
            t.move_to(np.array([x, y, 0]))
            num_group.add(t)

        self.play(
            LaggedStart(*[FadeIn(t, scale=0.6) for t in num_group], lag_ratio=0.05),
            run_time=0.8
        )
        explain2 = self.T("查表获取随机编号", size=22, color=C_GRAY)
        explain2.move_to(DOWN * 2.6)
        self.play(FadeIn(explain2), run_time=0.3)
        self.wait(0.6)

        # 公式框
        fbox = self.formula_box(
            r"P(\text{each}) = \frac{n}{N} = \frac{5}{40} = 12.5\%",
            label_str="等概率",
            box_color=C_SIMPLE
        )
        self.play(FadeIn(fbox), run_time=0.5)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_txt),
            FadeOut(dots), FadeOut(method2),
            FadeOut(num_group), FadeOut(explain2),
            FadeOut(fbox),
            run_time=0.5
        )

    # ──────────────────────────────────────
    #  Scene 2: 系统抽样
    # ──────────────────────────────────────
    def s2_systematic(self):
        title = self.section_title("② 系统抽样", color=C_SYS)
        self.play(Write(title), run_time=0.6)

        def_txt = self.T("按相等间隔依次抽取", size=26, color=C_WHITE)
        def_txt.move_to(UP * 4.9)
        self.play(FadeIn(def_txt), run_time=0.4)

        # 画 40 个灰点
        dots = VGroup(*[self.make_dot(p) for p in self.all_pos])
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.02),
            run_time=1.0
        )

        # 步骤 1: 将总体分为 n=5 段，用竖线标出
        # 每段 8 人 → 每段对应 8 列中的一列 (实际是按线性序号分段)
        step1 = self.T("Step1: 总体分成 5 段，每段 8 人", size=22, color=C_GRAY)
        step1.move_to(DOWN * 0.5)
        self.play(FadeIn(step1), run_time=0.3)

        # 用竖线分割网格 (4条线，在格点列之间)
        seg_lines = VGroup()
        for seg in range(1, N_SAMPLE):  # 1,2,3,4
            # 每段 k=8 个体，8列布局时每段恰好每列对应一个连续段
            # 线放在列 (seg*8/5)−0.5 处 → 近似放在均匀分割列之间
            linear_col = seg * (GRID_COLS / N_SAMPLE)  # 1.6, 3.2, 4.8, 6.4
            x = GRID_CX + (linear_col - (GRID_COLS - 1) / 2) * DOT_SPACING
            y_top = GRID_CY + (GRID_ROWS - 1) / 2 * DOT_SPACING + 0.2
            y_bot = GRID_CY - (GRID_ROWS - 1) / 2 * DOT_SPACING - 0.2
            line = DashedLine(
                np.array([x, y_bot, 0]), np.array([x, y_top, 0]),
                color=C_SYS, dash_length=0.12, stroke_width=1.5
            )
            seg_lines.add(line)

        # 段标签
        seg_labels = VGroup()
        for seg in range(N_SAMPLE):
            lx_start = (seg * GRID_COLS / N_SAMPLE)
            lx_end   = ((seg + 1) * GRID_COLS / N_SAMPLE)
            lx_mid   = (lx_start + lx_end) / 2
            x = GRID_CX + (lx_mid - (GRID_COLS - 1) / 2) * DOT_SPACING
            y = GRID_CY + (GRID_ROWS - 1) / 2 * DOT_SPACING + 0.45
            lbl = self.T(f"段{seg+1}", size=18, color=C_SYS)
            lbl.move_to(np.array([x, y, 0]))
            seg_labels.add(lbl)

        self.play(Create(seg_lines), FadeIn(seg_labels), run_time=0.7)
        self.wait(0.3)

        # 步骤 2: 第一段随机选起始 (start=3)
        self.play(FadeOut(step1), run_time=0.2)
        step2 = self.T("Step2: 第一段随机选起点 (编号4)", size=22, color=C_GRAY)
        step2.move_to(DOWN * 0.5)
        self.play(FadeIn(step2), run_time=0.3)

        start_dot = dots[self.sys_start]
        self.play(start_dot.animate.set_color(C_SAMPLE).scale(1.6), run_time=0.4)
        start_ring = self.highlight_ring(start_dot, C_SAMPLE)
        self.play(Create(start_ring), run_time=0.3)
        self.wait(0.3)

        # 步骤 3: 间隔 k=8 依次抽取
        self.play(FadeOut(step2), run_time=0.2)
        step3 = self.T("Step3: 间隔 k=8 依次抽取", size=22, color=C_GRAY)
        step3.move_to(DOWN * 0.5)
        self.play(FadeIn(step3), run_time=0.3)

        sampled_rings = VGroup(start_ring)
        arrows = VGroup()
        prev_idx = self.sys_start
        for idx in self.sys_indices[1:]:
            dot = dots[idx]
            # 箭头连接
            arr = Arrow(
                dots[prev_idx].get_center() + RIGHT * 0.15,
                dot.get_center() + LEFT  * 0.15,
                buff=0,
                color=C_SYS,
                stroke_width=2.0,
                max_tip_length_to_length_ratio=0.18
            )
            self.play(GrowArrow(arr), run_time=0.25)
            self.play(dot.animate.set_color(C_SAMPLE).scale(1.6), run_time=0.2)
            ring = self.highlight_ring(dot, C_SYS)
            self.play(Create(ring), run_time=0.15)
            sampled_rings.add(ring)
            arrows.add(arr)
            prev_idx = idx

        self.wait(0.4)

        # 公式框
        fbox = self.formula_box(
            r"k = \frac{N}{n} = \frac{40}{5} = 8",
            label_str="抽样间隔",
            box_color=C_SYS
        )
        self.play(FadeIn(fbox), run_time=0.5)
        self.wait(0.9)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_txt),
            FadeOut(dots), FadeOut(seg_lines), FadeOut(seg_labels),
            FadeOut(step3), FadeOut(sampled_rings), FadeOut(arrows),
            FadeOut(fbox),
            run_time=0.5
        )

    # ──────────────────────────────────────
    #  Scene 3: 分层抽样
    # ──────────────────────────────────────
    def s3_stratified(self):
        title = self.section_title("③ 分层抽样", color=C_STRAT)
        self.play(Write(title), run_time=0.6)

        def_txt = self.T("按各层比例分别随机抽取", size=26, color=C_WHITE)
        def_txt.move_to(UP * 4.9)
        self.play(FadeIn(def_txt), run_time=0.4)

        # ─ 情境: 学校有高一/高二/高三, 总40人, 抽10人 ─
        scenario = self.T("学校 40 人中抽取 10 人", size=24, color=C_GRAY)
        scenario.move_to(UP * 4.1)
        self.play(FadeIn(scenario), run_time=0.3)

        # 三层彩色矩形
        layer_names  = ["高一  20人", "高二  12人", "高三  8人"]
        layer_counts = self.layers      # [20, 12, 8]
        layer_allocs = self.layer_alloc # [5, 3, 2]
        centers_y    = [2.5, 0.9, -0.7]
        bw = 6.5; bh = 1.3

        layer_boxes  = VGroup()
        layer_labels = VGroup()
        dot_groups   = VGroup()

        for i, (name, cnt, alloc, cy, col) in enumerate(
            zip(layer_names, layer_counts, layer_allocs, centers_y, self.layer_colors)
        ):
            # 矩形
            rect = RoundedRectangle(
                width=bw, height=bh, corner_radius=0.18,
                fill_color=col, fill_opacity=0.15,
                stroke_color=col, stroke_width=2.2
            ).move_to(np.array([0, cy, 0]))
            layer_boxes.add(rect)

            # 层标签 (左侧)
            lbl = self.T(name, size=23, color=col)
            lbl.move_to(np.array([-2.5, cy, 0]))
            layer_labels.add(lbl)

            # 层内小点 (右侧紧密排列)
            n_vis = min(cnt, 12)  # 最多显示12个
            d_grp = VGroup()
            for j in range(n_vis):
                dx = -0.5 + (j % 6) * 0.38
                dy = cy + 0.18 - (j // 6) * 0.38
                d = self.make_dot(np.array([dx + 1.5, dy, 0]),
                                  color=col, r=0.09)
                d_grp.add(d)
            dot_groups.add(d_grp)

        # 逐层淡入
        for i in range(3):
            self.play(
                FadeIn(layer_boxes[i]),
                FadeIn(layer_labels[i]),
                LaggedStart(*[GrowFromCenter(d) for d in dot_groups[i]], lag_ratio=0.04),
                run_time=0.6
            )

        self.wait(0.4)

        # ─ 显示比例 & 抽取数 ─
        alloc_labels = VGroup()
        arrows_right = VGroup()
        for i, (alloc, cy, col) in enumerate(
            zip(layer_allocs, centers_y, self.layer_colors)
        ):
            # 箭头指向右侧
            arr = Arrow(
                np.array([2.4, cy, 0]), np.array([3.1, cy, 0]),
                buff=0, color=col, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.25
            )
            lbl = self.T(f"抽 {alloc} 人", size=22, color=col)
            lbl.move_to(np.array([3.85, cy, 0]))
            arrows_right.add(arr)
            alloc_labels.add(lbl)

        self.play(
            LaggedStart(
                *[AnimationGroup(GrowArrow(a), FadeIn(l))
                  for a, l in zip(arrows_right, alloc_labels)],
                lag_ratio=0.3
            ),
            run_time=1.0
        )

        # 公式框
        fbox = self.formula_box(
            r"\frac{\text{各层抽取数}}{\text{各层总数}} = \frac{n}{N}",
            label_str="按比例抽取",
            box_color=C_STRAT
        )
        self.play(FadeIn(fbox), run_time=0.5)

        note = self.T("总体差异明显时最适用", size=22, color=C_GRAY)
        note.move_to(DOWN * 6.6)
        self.play(FadeIn(note), run_time=0.3)

        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_txt), FadeOut(scenario),
            FadeOut(layer_boxes), FadeOut(layer_labels), FadeOut(dot_groups),
            FadeOut(arrows_right), FadeOut(alloc_labels),
            FadeOut(fbox), FadeOut(note),
            run_time=0.6
        )

    # ──────────────────────────────────────
    #  Scene 4: 三种方法对比汇总
    # ──────────────────────────────────────
    def s4_summary(self):
        title = self.T("三种抽样方法对比", size=38, color=C_GOLD)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 共同点横幅
        banner_bg = RoundedRectangle(
            width=7.8, height=0.75, corner_radius=0.18,
            fill_color=C_GOLD, fill_opacity=0.15,
            stroke_color=C_GOLD, stroke_width=1.5
        ).move_to(UP * 4.9)
        banner_txt = self.T("共同点: 等概率抽样", size=26, color=C_GOLD)
        banner_txt.move_to(banner_bg.get_center())
        self.play(FadeIn(banner_bg), Write(banner_txt), run_time=0.5)

        # 三张卡片
        card_data = [
            ("① 简单随机抽样", C_SIMPLE,
             "适用: 总体较小\n方法: 抽签/随机数表\n特点: 完全随机"),
            ("② 系统抽样",    C_SYS,
             "适用: 总体较大\n方法: 等距间隔 k=N/n\n特点: 操作简便"),
            ("③ 分层抽样",    C_STRAT,
             "适用: 总体差异明显\n方法: 各层按比例\n特点: 代表性强"),
        ]

        centers_y = [2.8, 1.0, -0.8]
        cards = VGroup()

        for (hdr, col, body), cy in zip(card_data, centers_y):
            bg = RoundedRectangle(
                width=7.8, height=1.55, corner_radius=0.2,
                fill_color=col, fill_opacity=0.12,
                stroke_color=col, stroke_width=2.0
            ).move_to(np.array([0, cy, 0]))

            # 左侧竖条
            bar = Rectangle(
                width=0.18, height=1.55,
                fill_color=col, fill_opacity=1.0,
                stroke_width=0
            ).move_to(np.array([-3.81, cy, 0]))

            h = self.T(hdr, size=24, color=col)
            h.move_to(np.array([0.3, cy + 0.38, 0]))

            b = self.T(body, size=18, color=C_WHITE)
            b.move_to(np.array([0.3, cy - 0.18, 0]))

            cards.add(VGroup(bg, bar, h, b))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)

        # 底部总结
        summary_bg = RoundedRectangle(
            width=7.8, height=0.85, corner_radius=0.2,
            fill_color="#16213e", fill_opacity=1.0,
            stroke_color=YELLOW, stroke_width=1.5
        ).move_to(DOWN * 2.8)
        summary_txt = self.T("掌握三种方法, 轻松应对抽样题!", size=24, color=YELLOW)
        summary_txt.move_to(summary_bg.get_center())
        self.play(FadeIn(summary_bg), Write(summary_txt), run_time=0.6)

        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(banner_bg), FadeOut(banner_txt),
            FadeOut(cards), FadeOut(summary_bg), FadeOut(summary_txt),
            run_time=0.6
        )

    # ──────────────────────────────────────
    #  Scene 5: 片尾
    # ──────────────────────────────────────
    def s5_outro(self):
        author_big = self.T("上海初高中数学直通车", size=40, color=C_WHITE)
        author_big.move_to(UP * 2.0)

        author_id = self.T("@emptyandcalm", size=30, color=C_GRAY)
        author_id.move_to(UP * 1.0)

        self.play(Transform(self.author, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        follow = self.T("关注我，获得更多数学技巧!", size=30, color=C_GOLD)
        follow.move_to(DOWN * 0.1)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)

        # 三色小图标装饰
        icons = VGroup(
            Circle(radius=0.28, fill_color=C_SIMPLE,
                   fill_opacity=0.9, stroke_width=0).shift(LEFT * 2.0 + DOWN * 2.0),
            Circle(radius=0.28, fill_color=C_SYS,
                   fill_opacity=0.9, stroke_width=0).shift(DOWN * 2.0),
            Circle(radius=0.28, fill_color=C_STRAT,
                   fill_opacity=0.9, stroke_width=0).shift(RIGHT * 2.0 + DOWN * 2.0),
        )
        icon_labels = VGroup(
            self.T("简单", size=16, color=C_WHITE).move_to(icons[0].get_center()),
            self.T("系统", size=16, color=C_WHITE).move_to(icons[1].get_center()),
            self.T("分层", size=16, color=C_WHITE).move_to(icons[2].get_center()),
        )

        self.play(
            *[GrowFromCenter(ic) for ic in icons],
            run_time=0.6
        )
        self.play(FadeIn(icon_labels), run_time=0.3)

        # 知识要点快卡
        kp_items = [
            ("简单随机: ", f"P = n/N", C_SIMPLE),
            ("系统抽样: ", "间隔 k = N/n", C_SYS),
            ("分层抽样: ", "各层按比例", C_STRAT),
        ]
        kp_group = VGroup()
        for j, (term, val, col) in enumerate(kp_items):
            t1 = self.T(term, size=20, color=col)
            t2 = self.T(val,  size=20, color=C_WHITE)
            row = VGroup(t1, t2).arrange(RIGHT, buff=0.05)
            row.move_to(np.array([0, -3.3 - j * 0.65, 0]))
            kp_group.add(row)

        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.15) for r in kp_group],
                        lag_ratio=0.2),
            run_time=0.8
        )

        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(icons), FadeOut(icon_labels),
            FadeOut(kp_group),
            run_time=1.0
        )

# # 快速预览 (480p)
# manim -pql sampling_techniques_animation.py SamplingTechniques

# # 高质量输出 (1080p，TikTok发布用)
# manim -qh sampling_techniques_animation.py SamplingTechniques
"""
古典概型 - Manim 教学动画
年级: 高三第二学期   章节: 概率论初步

知识点：古典概型两特征（有限性+等可能性）
         公式 P(A)=m/n
         三大经典模型：骰子 / 摸球 / 硬币

输出格式: TikTok 竖屏 (1080 × 1920)
作者: 上海初高中数学直通车  @emptyandcalm

渲染:
    manim -pql classical_prob.py ClassicalProbability   # 快速预览
    manim -qh  classical_prob.py ClassicalProbability   # 高质量
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────────────────
# 全局配置
# ──────────────────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ──────────────────────────────────────────────────────────
# 颜色
# ──────────────────────────────────────────────────────────
BG        = "#1a1a2e"
C_DIE     = "#ecf0f1"    # 骰子白色面
C_DOT     = "#2c3e50"    # 骰子黑点
C_HIT     = "#e74c3c"    # 命中高亮  红
C_MISS    = "#3498db"    # 未命中    蓝
C_RED_BALL= "#e74c3c"    # 红球
C_BLU_BALL= "#3498db"    # 蓝球
C_COIN_H  = "#f39c12"    # 硬币正面  金
C_COIN_T  = "#95a5a6"    # 硬币反面  灰
C_FORMULA = "#2ecc71"    # 公式框    绿
C_HL      = YELLOW
C_AX      = "#7f8c8d"
C_CARD    = "#16213e"
C_GRID_HIT= "#e74c3c"    # 网格命中格
C_GRID_BG = "#2c3e50"    # 网格背景
FONT      = "Noto Sans CJK SC"


# ══════════════════════════════════════════════════════════
# 工具：绘制一个骰子面
# ══════════════════════════════════════════════════════════
def make_die_face(face: int, size=0.85, die_color=C_DIE, dot_color=C_DOT,
                  stroke_color=C_AX, stroke_w=1.5) -> VGroup:
    """
    返回 VGroup：骰子方块 + 点阵
    face: 1~6
    size: 方块边长
    """
    # 点阵坐标（归一化，在 [-0.28, 0.28] 范围内）
    offset = size * 0.28
    patterns = {
        1: [(0, 0)],
        2: [(-offset,  offset), ( offset, -offset)],
        3: [(-offset,  offset), (0, 0),             ( offset, -offset)],
        4: [(-offset,  offset), ( offset,  offset),
            (-offset, -offset), ( offset, -offset)],
        5: [(-offset,  offset), ( offset,  offset), (0, 0),
            (-offset, -offset), ( offset, -offset)],
        6: [(-offset,  offset), ( offset,  offset),
            (-offset, 0),       ( offset, 0),
            (-offset, -offset), ( offset, -offset)],
    }
    sq = RoundedRectangle(
        width=size, height=size, corner_radius=size * 0.12,
        fill_color=die_color, fill_opacity=1,
        stroke_color=stroke_color, stroke_width=stroke_w
    )
    dots = VGroup(*[
        Dot(np.array([dx, dy, 0]), radius=size * 0.085, color=dot_color)
        for dx, dy in patterns[face]
    ])
    return VGroup(sq, dots)


# ══════════════════════════════════════════════════════════
# 工具：绘制一枚硬币
# ══════════════════════════════════════════════════════════
def make_coin(side: str, r=0.42) -> VGroup:
    """
    side: 'H'（正面）或 'T'（反面）
    """
    color = C_COIN_H if side == "H" else C_COIN_T
    label = "H" if side == "H" else "T"
    circle = Circle(radius=r, fill_color=color, fill_opacity=1,
                    stroke_color=WHITE, stroke_width=2)
    text   = Text(label, font=FONT, font_size=int(r * 80), color=WHITE,
                  weight=BOLD)
    return VGroup(circle, text)


# ══════════════════════════════════════════════════════════
class ClassicalProbability(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()

        self.scene_opening()
        self.scene_definition()
        self.scene_die_single()
        self.scene_die_double()
        self.scene_balls()
        self.scene_coins()
        self.scene_summary()
        self.scene_outro()

    # ──────────────────────────────────────────────────────
    def setup_geometry(self):
        """统一初始化所有几何数据并验证"""

        # 骰子面尺寸
        self.DIE_SIZE   = 0.88
        self.DIE_GAP    = 1.08   # 中心间距

        # 双骰子网格
        self.GRID_CELL  = 0.72
        self.GRID_ROWS  = 6
        self.GRID_COLS  = 6
        self.GRID_CTR   = np.array([0.0, 1.8, 0.0])

        # 摸球
        self.BALL_R     = 0.36
        self.BALL_GAP   = 0.88   # 球心间距
        self.N_BALLS    = 8
        self.N_RED      = 3

        # 硬币
        self.COIN_R     = 0.42
        self.COIN_GAP   = 1.6

        # 古典概型数据（精确计算，来自 verify 脚本）
        # 单骰子
        self.n_die      = 6
        self.p_die1     = 1 / 6
        self.p_even     = 3 / 6
        self.p_ge5      = 2 / 6

        # 双骰子
        self.n_double   = 36
        # 精确枚举 sum=7 组合
        self.combos_7   = [(d1, d2) for d1 in range(1, 7)
                                     for d2 in range(1, 7) if d1+d2==7]
        self.p_sum7     = len(self.combos_7) / self.n_double  # = 6/36

        # 摸球
        self.p_red      = self.N_RED / self.N_BALLS   # = 3/8

        # 硬币
        self.n_coins    = 4
        self.p_HH       = 1 / 4
        self.p_at1H     = 3 / 4

        # ── 验证 ──
        assert abs(self.p_die1  - 1/6 ) < 1e-10
        assert abs(self.p_even  - 1/2 ) < 1e-10
        assert abs(self.p_sum7  - 1/6 ) < 1e-10
        assert abs(self.p_red   - 3/8 ) < 1e-10
        assert abs(self.p_HH    - 1/4 ) < 1e-10
        assert len(self.combos_7) == 6
        print("✓ setup_geometry 验证通过")

    # ──────────────────────────────────────────────────────
    # 工具：带颜色边框的公式卡片
    # ──────────────────────────────────────────────────────
    def card(self, items, color, pos, w=8.0, h=1.4):
        """items: list of Mobject, 水平排列后放入圆角框"""
        bg = RoundedRectangle(
            width=w, height=h, corner_radius=0.18,
            fill_color=C_CARD, fill_opacity=1,
            stroke_color=color, stroke_width=2.5
        ).move_to(pos)
        content = VGroup(*items).arrange(RIGHT, buff=0.3).move_to(pos)
        return VGroup(bg, content)

    # ══════════════════════════════════════════════════════
    # Scene 1  开场
    # ══════════════════════════════════════════════════════
    def scene_opening(self):
        self.author_banner = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_banner, shift=DOWN * 0.2), run_time=0.4)

        # 钩子：骰子 + 问号
        die_hook = make_die_face(6, size=1.1, die_color="#e8d5a3")
        die_hook.move_to(UP * 4.8)
        q_mark = Text("?", font=FONT, font_size=72, color=C_HL).move_to(UP * 4.8 + RIGHT * 1.1)
        self.play(GrowFromCenter(die_hook), run_time=0.6)
        self.play(Write(q_mark), run_time=0.3)

        title = Text("古典概型", font=FONT, font_size=56, color=GOLD,
                     weight=BOLD).move_to(UP * 3.3)
        subtitle = Text("等可能的随机试验", font=FONT, font_size=28, color=GRAY_A
                        ).move_to(UP * 2.4)
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.4)

        # 三大模型 icon 预览
        models = [
            (make_die_face(3, size=0.7), "骰子",  C_HIT,  LEFT  * 2.8 + UP * 1.1),
            (make_coin("H", r=0.32),     "硬币",  C_COIN_H, UP  * 1.1),
            (Circle(radius=0.32, fill_color=C_RED_BALL, fill_opacity=1,
                    stroke_color=WHITE, stroke_width=2), "摸球", C_RED_BALL, RIGHT * 2.8 + UP * 1.1),
        ]
        model_objs = []
        for icon, name, col, pos in models:
            icon.move_to(pos)
            lbl = Text(name, font=FONT, font_size=20, color=col).next_to(icon, DOWN, buff=0.15)
            self.play(FadeIn(icon, scale=0.4), FadeIn(lbl), run_time=0.35)
            model_objs.extend([icon, lbl])

        self.wait(0.7)

        title_sm = Text("古典概型", font=FONT, font_size=36, color=GOLD,
                        weight=BOLD).move_to(UP * 6.3)
        self.play(
            Transform(title, title_sm),
            FadeOut(subtitle), FadeOut(die_hook), FadeOut(q_mark),
            *[FadeOut(o) for o in model_objs],
            run_time=0.5,
        )
        self.title_obj = title

    # ══════════════════════════════════════════════════════
    # Scene 2  定义：两大特征 + 核心公式
    # ══════════════════════════════════════════════════════
    def scene_definition(self):
        sec = Text("古典概型的特征", font=FONT, font_size=36, color=C_FORMULA
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 特征 1：有限性
        feat1_title = Text("① 有限性", font=FONT, font_size=30, color=C_HL).move_to(UP * 4.3)
        feat1_body  = Text("试验结果只有有限个", font=FONT, font_size=24, color=WHITE
                           ).move_to(UP * 3.55)
        # 骰子 6 面示意
        die_row = VGroup(*[
            make_die_face(i + 1, size=0.60) for i in range(6)
        ]).arrange(RIGHT, buff=0.18).move_to(UP * 2.6)
        n_lbl = MathTex(r"n = 6", font_size=28, color=C_HL).next_to(die_row, RIGHT, buff=0.3)

        self.play(FadeIn(feat1_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(feat1_body),  run_time=0.3)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in die_row], lag_ratio=0.12),
                  run_time=0.9)
        self.play(Write(n_lbl), run_time=0.3)

        # 特征 2：等可能性
        feat2_title = Text("② 等可能性", font=FONT, font_size=30, color=C_HL).move_to(UP * 1.5)
        feat2_body  = Text("每个结果出现的可能性相同", font=FONT, font_size=24, color=WHITE
                           ).move_to(UP * 0.75)

        # 6 个概率标注等于 1/6
        eq_lbl = Text("每面概率 =", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 0.1)
        frac   = MathTex(r"\frac{1}{6}", font_size=32, color=C_HL).next_to(eq_lbl, RIGHT, buff=0.2)

        self.play(FadeIn(feat2_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(feat2_body), run_time=0.3)
        self.play(FadeIn(eq_lbl), Write(frac), run_time=0.5)

        # 公式框
        formula_title = Text("核心公式", font=FONT, font_size=26, color=C_FORMULA)
        formula_tex   = MathTex(r"P(A) = \frac{m}{n}", font_size=38, color=WHITE)
        formula_card  = self.card(
            [formula_title, formula_tex], C_FORMULA, DOWN * 1.6, w=7.0, h=1.5
        )
        self.play(FadeIn(formula_card), run_time=0.6)

        hint_m = Text("m = 事件A包含的基本事件数", font=FONT, font_size=21, color=GRAY_A
                      ).move_to(DOWN * 2.8)
        hint_n = Text("n = 总的基本事件数", font=FONT, font_size=21, color=GRAY_A
                      ).move_to(DOWN * 3.55)
        self.play(FadeIn(hint_m), FadeIn(hint_n), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(sec), FadeOut(feat1_title), FadeOut(feat1_body),
            FadeOut(die_row), FadeOut(n_lbl),
            FadeOut(feat2_title), FadeOut(feat2_body),
            FadeOut(eq_lbl), FadeOut(frac),
            FadeOut(formula_card), FadeOut(hint_m), FadeOut(hint_n),
            run_time=0.5,
        )

    # ══════════════════════════════════════════════════════
    # Scene 3  单骰子示例
    # ══════════════════════════════════════════════════════
    def scene_die_single(self):
        sec = Text("【模型一】掷骰子  n = 6", font=FONT, font_size=32, color=C_HIT
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 6 个骰子横排
        die_size = self.DIE_SIZE
        die_gap  = self.DIE_GAP
        die_y    = 3.5
        dies = VGroup(*[
            make_die_face(i + 1, size=die_size) for i in range(6)
        ])
        # 手动排列，确保居中
        total_w = 5 * die_gap
        for i, d in enumerate(dies):
            d.move_to(np.array([-total_w/2 + i * die_gap, die_y, 0]))

        self.play(LaggedStart(*[GrowFromCenter(d) for d in dies], lag_ratio=0.1),
                  run_time=1.0)

        # 标注 n=6
        n_brace = BraceBetweenPoints(
            np.array([-total_w/2 - die_size/2, die_y - die_size/2 - 0.05, 0]),
            np.array([ total_w/2 + die_size/2, die_y - die_size/2 - 0.05, 0]),
            direction=DOWN, color=GRAY_A
        )
        n_text = Text("共 n = 6 种等可能结果", font=FONT, font_size=22, color=GRAY_A
                      ).next_to(n_brace, DOWN, buff=0.12)
        self.play(GrowFromCenter(n_brace), FadeIn(n_text), run_time=0.5)

        # ── 问题1：P(点数=1) ──
        q1 = Text("问题①  P(点数 = 1) = ?", font=FONT, font_size=26, color=C_HL
                  ).move_to(UP * 1.5)
        self.play(FadeIn(q1, shift=UP * 0.2), run_time=0.4)

        # 高亮第1面
        self.play(
            dies[0][0].animate.set_fill(color=C_HIT, opacity=0.6),
            run_time=0.4
        )
        ans1 = VGroup(
            Text("m = 1,  ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"P(1) = \frac{1}{6}", font_size=30, color=C_HIT),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 0.65)
        self.play(FadeIn(ans1), run_time=0.5)
        self.wait(0.5)

        # ── 问题2：P(偶数) ──
        q2 = Text("问题②  P(偶数) = ?", font=FONT, font_size=26, color=C_HL
                  ).move_to(UP * -0.3)
        self.play(FadeIn(q2, shift=UP * 0.2), run_time=0.4)

        # 高亮偶数面 2,4,6 (index 1,3,5)
        self.play(
            dies[0][0].animate.set_fill(color=C_DIE, opacity=1),  # 取消面1高亮
            run_time=0.2
        )
        self.play(
            *[dies[i][0].animate.set_fill(color=C_HIT, opacity=0.6) for i in [1, 3, 5]],
            run_time=0.4
        )
        ans2 = VGroup(
            Text("m = 3,  ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"P(\text{even}) = \frac{3}{6} = \frac{1}{2}", font_size=28, color=C_HIT),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.3)
        self.play(FadeIn(ans2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(sec), FadeOut(dies), FadeOut(n_brace), FadeOut(n_text),
            FadeOut(q1), FadeOut(ans1), FadeOut(q2), FadeOut(ans2),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 4  双骰子 6×6 网格
    # ══════════════════════════════════════════════════════
    def scene_die_double(self):
        sec = Text("【进阶】掷两次骰子  n = 36", font=FONT, font_size=30, color=C_HIT
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        cell  = self.GRID_CELL
        rows  = self.GRID_ROWS
        cols  = self.GRID_COLS
        ctr   = self.GRID_CTR

        # 计算网格左上角
        grid_x0 = ctr[0] - (cols * cell) / 2 + cell / 2
        grid_y0 = ctr[1] + (rows * cell) / 2 - cell / 2

        # ── 快速绘制整个网格（矩形 + 数字）──
        all_cells = VGroup()
        cell_mobs = {}  # (r,c) -> VGroup(bg, label)

        for r in range(rows):
            for c in range(cols):
                d1 = c + 1   # 列代表骰子1
                d2 = r + 1   # 行代表骰子2
                s  = d1 + d2
                cx = grid_x0 + c * cell
                cy = grid_y0 - r * cell
                bg = Square(
                    side_length=cell * 0.92,
                    fill_color=C_GRID_BG, fill_opacity=1,
                    stroke_color="#3d4f6b", stroke_width=1
                ).move_to(np.array([cx, cy, 0]))
                lbl = Text(str(s), font=FONT, font_size=16, color=GRAY_A
                           ).move_to(np.array([cx, cy, 0]))
                mob = VGroup(bg, lbl)
                all_cells.add(mob)
                cell_mobs[(r, c)] = (mob, bg, lbl, d1, d2, s)

        # 行列标题（骰子面图）
        col_headers = VGroup()
        for c in range(cols):
            d = make_die_face(c + 1, size=cell * 0.75,
                              die_color="#3a4a5c", dot_color=GRAY_A, stroke_w=0.8)
            d.move_to(np.array([grid_x0 + c * cell, grid_y0 + cell, 0]))
            col_headers.add(d)

        row_headers = VGroup()
        for r in range(rows):
            d = make_die_face(r + 1, size=cell * 0.75,
                              die_color="#3a4a5c", dot_color=GRAY_A, stroke_w=0.8)
            d.move_to(np.array([grid_x0 - cell, grid_y0 - r * cell, 0]))
            row_headers.add(d)

        self.play(
            LaggedStart(*[FadeIn(col_headers[i]) for i in range(6)], lag_ratio=0.08),
            LaggedStart(*[FadeIn(row_headers[i]) for i in range(6)], lag_ratio=0.08),
            run_time=0.7
        )
        self.play(FadeIn(all_cells), run_time=0.6)

        # n=36 标注
        n36 = Text("n = 6×6 = 36 种结果", font=FONT, font_size=22, color=GRAY_A
                   ).move_to(ctr + DOWN * (rows * cell / 2 + 0.55))
        self.play(FadeIn(n36, shift=UP * 0.2), run_time=0.4)

        # ── 问题：P(点数和 = 7) ──
        q = Text("P(两骰子之和 = 7) = ?", font=FONT, font_size=26, color=C_HL
                 ).move_to(DOWN * 4.5)
        self.play(FadeIn(q, shift=UP * 0.2), run_time=0.4)

        # 高亮 sum=7 的格子
        hit_cells = []
        for r in range(rows):
            for c in range(cols):
                mob, bg, lbl, d1, d2, s = cell_mobs[(r, c)]
                if s == 7:
                    hit_cells.append((bg, lbl))

        self.play(
            *[bg.animate.set_fill(color=C_GRID_HIT, opacity=0.85) for bg, lbl in hit_cells],
            *[lbl.animate.set_color(WHITE) for bg, lbl in hit_cells],
            run_time=0.7
        )
        self.play(
            *[Flash(bg, color=C_HL, flash_radius=cell * 0.5) for bg, lbl in hit_cells],
            run_time=0.5
        )

        ans = VGroup(
            Text("m = 6,  n = 36  →  ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"P(\text{sum}=7) = \frac{6}{36} = \frac{1}{6}", font_size=28, color=C_HIT),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.6)
        self.play(FadeIn(ans), run_time=0.5)
        self.wait(1.4)

        self.play(
            FadeOut(sec), FadeOut(all_cells),
            FadeOut(col_headers), FadeOut(row_headers),
            FadeOut(n36), FadeOut(q), FadeOut(ans),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 5  摸球
    # ══════════════════════════════════════════════════════
    def scene_balls(self):
        sec = Text("【模型二】摸球  n = 8", font=FONT, font_size=32, color=C_RED_BALL
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 袋子（圆角矩形）
        bag = RoundedRectangle(
            width=5.2, height=1.8, corner_radius=0.5,
            fill_color="#2c3e50", fill_opacity=1,
            stroke_color=GRAY_A, stroke_width=2
        ).move_to(UP * 4.0)
        bag_lbl = Text("袋", font=FONT, font_size=28, color=GRAY_A).move_to(
            bag.get_left() + RIGHT * 0.35
        )
        self.play(Create(bag), FadeIn(bag_lbl), run_time=0.5)

        # 8 个球（3红5蓝）横排
        ball_r   = self.BALL_R
        ball_gap = self.BALL_GAP
        n_balls  = self.N_BALLS
        n_red    = self.N_RED
        n_blue   = n_balls - n_red

        total_w  = (n_balls - 1) * ball_gap
        ball_y   = 2.7

        balls = []
        for i in range(n_balls):
            cx = -total_w / 2 + i * ball_gap
            is_red = (i < n_red)
            col = C_RED_BALL if is_red else C_BLU_BALL
            circle = Circle(radius=ball_r, fill_color=col, fill_opacity=1,
                            stroke_color=WHITE, stroke_width=2)
            circle.move_to(np.array([cx, ball_y, 0]))
            balls.append((circle, is_red))

        # 球逐个从袋子掉落
        self.play(
            LaggedStart(*[
                FadeIn(b, shift=DOWN * 0.5) for b, _ in balls
            ], lag_ratio=0.08),
            run_time=0.9
        )

        # 标注数量
        red_brace = BraceBetweenPoints(
            np.array([-total_w/2 - ball_r, ball_y - ball_r - 0.08, 0]),
            np.array([-total_w/2 + (n_red-1)*ball_gap + ball_r, ball_y - ball_r - 0.08, 0]),
            direction=DOWN, color=C_RED_BALL
        )
        red_lbl = Text("3 红球", font=FONT, font_size=20, color=C_RED_BALL
                       ).next_to(red_brace, DOWN, buff=0.1)
        blue_brace = BraceBetweenPoints(
            np.array([-total_w/2 + n_red*ball_gap - ball_r, ball_y - ball_r - 0.08, 0]),
            np.array([ total_w/2 + ball_r, ball_y - ball_r - 0.08, 0]),
            direction=DOWN, color=C_BLU_BALL
        )
        blue_lbl = Text("5 蓝球", font=FONT, font_size=20, color=C_BLU_BALL
                        ).next_to(blue_brace, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(red_brace), FadeIn(red_lbl),
            GrowFromCenter(blue_brace), FadeIn(blue_lbl),
            run_time=0.5
        )

        # n = 8
        n_lbl = Text("n = 8  （总基本事件数）", font=FONT, font_size=22, color=GRAY_A
                     ).move_to(UP * 0.8)
        self.play(FadeIn(n_lbl, shift=UP * 0.2), run_time=0.4)

        # 问题
        q = Text("随机摸 1 球，P(红球) = ?", font=FONT, font_size=26, color=C_HL
                 ).move_to(UP * -0.1)
        self.play(FadeIn(q, shift=UP * 0.2), run_time=0.4)

        # 高亮红球
        self.play(
            *[b.animate.set_fill(opacity=0.9).scale(1.2) for b, is_red in balls if is_red],
            run_time=0.4
        )
        m_lbl = Text("m = 3  （红球数）", font=FONT, font_size=22, color=C_RED_BALL
                     ).move_to(DOWN * 1.1)
        self.play(FadeIn(m_lbl), run_time=0.3)

        ans = VGroup(
            MathTex(r"P(A) = \frac{3}{8}", font_size=36, color=C_RED_BALL),
        ).move_to(DOWN * 2.2)
        box_ans = SurroundingRectangle(ans, corner_radius=0.15,
                                       color=C_RED_BALL, buff=0.2)
        self.play(Write(ans), Create(box_ans), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(sec), FadeOut(bag), FadeOut(bag_lbl),
            *[FadeOut(b) for b, _ in balls],
            FadeOut(red_brace), FadeOut(red_lbl),
            FadeOut(blue_brace), FadeOut(blue_lbl),
            FadeOut(n_lbl), FadeOut(q), FadeOut(m_lbl),
            FadeOut(ans), FadeOut(box_ans),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 6  投两枚硬币
    # ══════════════════════════════════════════════════════
    def scene_coins(self):
        sec = Text("【模型三】抛两枚硬币  n = 4", font=FONT, font_size=30, color=C_COIN_H
                   ).move_to(UP * 5.5)
        self.play(Write(sec), run_time=0.5)

        # 4 种结果：HH, HT, TH, TT
        coin_combos = [("H", "H"), ("H", "T"), ("T", "H"), ("T", "T")]
        labels_cn   = ["正正", "正反", "反正", "反反"]
        positions   = [
            LEFT * 2.2 + UP * 3.3,
            RIGHT * 2.2 + UP * 3.3,
            LEFT * 2.2 + UP * 1.2,
            RIGHT * 2.2 + UP * 1.2,
        ]

        combo_groups = []
        for i, ((s1, s2), label_cn, pos) in enumerate(
                zip(coin_combos, labels_cn, positions)):
            c1 = make_coin(s1, r=self.COIN_R * 0.82).move_to(pos + LEFT * 0.55)
            c2 = make_coin(s2, r=self.COIN_R * 0.82).move_to(pos + RIGHT * 0.55)
            lbl = Text(label_cn, font=FONT, font_size=20, color=GRAY_A
                       ).move_to(pos + DOWN * 0.7)
            combo_groups.append(VGroup(c1, c2, lbl))

        self.play(
            LaggedStart(*[GrowFromCenter(g) for g in combo_groups], lag_ratio=0.15),
            run_time=1.0
        )

        # n=4 标注
        n_lbl = Text("n = 2² = 4 种等可能结果", font=FONT, font_size=22, color=GRAY_A
                     ).move_to(DOWN * 0.3)
        self.play(FadeIn(n_lbl, shift=UP * 0.2), run_time=0.4)

        # 问题：P(至少一次正面)
        q = Text("P(至少一次正面) = ?", font=FONT, font_size=26, color=C_HL
                 ).move_to(DOWN * 1.3)
        self.play(FadeIn(q, shift=UP * 0.2), run_time=0.4)

        # 高亮 HH, HT, TH（前三组）
        for idx in range(3):
            self.play(
                combo_groups[idx][0][0].animate.set_fill(opacity=0.9),
                combo_groups[idx][1][0].animate.set_fill(opacity=0.9),
                run_time=0.2
            )
        # 灰化 TT
        self.play(
            combo_groups[3][0][0].animate.set_fill(color=GRAY_D, opacity=0.5),
            combo_groups[3][1][0].animate.set_fill(color=GRAY_D, opacity=0.5),
            combo_groups[3][2].animate.set_color(GRAY_D),
            run_time=0.3
        )

        ans = VGroup(
            Text("m = 3,  ", font=FONT, font_size=24, color=WHITE),
            MathTex(r"P \geq 1H) = \frac{3}{4}", font_size=30, color=C_COIN_H),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)

        # 实际写法更安全（括号平衡）
        ans = VGroup(
            Text("m = 3,  n = 4", font=FONT, font_size=24, color=WHITE),
            MathTex(r"P = \frac{3}{4}", font_size=30, color=C_COIN_H),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 2.5)

        box_ans = SurroundingRectangle(ans, corner_radius=0.15,
                                       color=C_COIN_H, buff=0.2)
        self.play(FadeIn(ans), Create(box_ans), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(sec),
            *[FadeOut(g) for g in combo_groups],
            FadeOut(n_lbl), FadeOut(q),
            FadeOut(ans), FadeOut(box_ans),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 7  总结
    # ══════════════════════════════════════════════════════
    def scene_summary(self):
        title_s = Text("古典概型解题步骤", font=FONT, font_size=38, color=GOLD
                       ).move_to(UP * 5.5)
        self.play(Write(title_s), run_time=0.6)

        steps = [
            ("① 列出所有基本事件",     "确认有限 & 等可能", "#3498db"),
            ("② 数出总数 n",            "有限个基本事件",     "#2ecc71"),
            ("③ 找出 A 包含的数量 m",   "对应题目条件",       "#e67e22"),
            ("④ 计算 P(A) = m/n",       "代入公式",           "#e74c3c"),
        ]

        step_objs = []
        sy = 4.1
        for step_txt, hint_txt, col in steps:
            bg = RoundedRectangle(
                width=8.2, height=1.45, corner_radius=0.16,
                fill_color=C_CARD, fill_opacity=1,
                stroke_color=col, stroke_width=2.2
            ).move_to(UP * sy)
            main_t = Text(step_txt, font=FONT, font_size=24, color=col).move_to(
                bg.get_center() + LEFT * 1.5
            )
            hint_t = Text(hint_txt, font=FONT, font_size=18, color=GRAY_B).move_to(
                bg.get_center() + RIGHT * 2.3
            )
            card_g = VGroup(bg, main_t, hint_t)
            card_g.shift(LEFT * 12)
            self.add(card_g)
            self.play(card_g.animate.shift(RIGHT * 12), run_time=0.38)
            step_objs.append(card_g)
            sy -= 1.55

        # 核心公式再次强调
        formula_big = MathTex(
            r"P(A) = \frac{m}{n},\quad 0 \leq P(A) \leq 1",
            font_size=34, color=WHITE
        ).move_to(DOWN * 5.0)
        box_big = SurroundingRectangle(formula_big, corner_radius=0.18,
                                       color=C_FORMULA, buff=0.25)
        self.play(Write(formula_big), Create(box_big), run_time=0.7)
        self.wait(2.0)

        self.play(
            *[FadeOut(o) for o in step_objs],
            FadeOut(title_s), FadeOut(formula_big), FadeOut(box_big),
            run_time=0.6
        )

    # ══════════════════════════════════════════════════════
    # Scene 8  片尾
    # ══════════════════════════════════════════════════════
    def scene_outro(self):
        self.play(FadeOut(self.title_obj), run_time=0.4)

        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 2.2)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 1.2)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=C_HL
        ).move_to(DOWN * 0.1)

        self.play(Transform(self.author_banner, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05, shift=UP * 0.2), run_time=0.6)

        # 三模型骰子/硬币/球装饰
        die_deco  = make_die_face(6, size=0.65, die_color="#e8d5a3").move_to(LEFT*2.5 + DOWN*1.7)
        coin_deco = make_coin("H", r=0.3).move_to(DOWN * 1.7)
        ball_deco = Circle(radius=0.3, fill_color=C_RED_BALL, fill_opacity=1,
                           stroke_color=WHITE, stroke_width=2).move_to(RIGHT*2.5 + DOWN*1.7)

        self.play(
            GrowFromCenter(die_deco),
            GrowFromCenter(coin_deco),
            GrowFromCenter(ball_deco),
            run_time=0.6
        )
        self.play(
            Rotate(die_deco, angle=PI/4),
            Rotate(coin_deco, angle=PI, axis=RIGHT),
            ball_deco.animate.shift(UP * 0.3),
            run_time=0.6
        )
        self.play(
            Rotate(die_deco, angle=-PI/4),
            ball_deco.animate.shift(DOWN * 0.3),
            run_time=0.4
        )

        tip = Text(
            "古典概型：数清楚，算准确！",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            *[FadeOut(o) for o in [
                self.author_banner, author_id, follow,
                die_deco, coin_deco, ball_deco, tip
            ]],
            run_time=1.0
        )
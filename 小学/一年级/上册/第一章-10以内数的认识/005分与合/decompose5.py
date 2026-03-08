"""
decompose5.py  ──  分与合（5的分解与组合）
一年级上册·第一章·10以内数的认识

内容: 5可以分成1和4、2和3、3和2、4和1
目标: TikTok 竖屏 1080×1920，约55秒
作者: 上海初高中数学直通车  @emptyandcalm
"""

from manim import *
import numpy as np

# ═══════════════════════════════════════════════════════
# 全局配置
# ═══════════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG_COLOR  = "#1a1a2e"
C_FIVE    = "#f1c40f"   # 黄  → 5（总数）
C_LEFT    = "#3498db"   # 蓝  → 左组
C_RIGHT   = "#e74c3c"   # 红  → 右组
C_ACTIVE  = "#2ecc71"   # 绿  → 高亮/合并
C_DIM     = "#888899"
FONT      = "Noto Sans CJK SC"

# 布局常量（与 verify_decompose.py 一致）
TOP_N    = 5
TOP_Y    = 3.2
TOP_SP   = 1.0
TOP_R    = 0.40

BOT_Y    = 1.0
LEFT_CX  = -2.2
RIGHT_CX =  2.2
BOT_R    = 0.38
BOT_SP   = 0.85

# 5的全部分法（有序）
SPLITS = [(1, 4), (2, 3), (3, 2), (4, 1)]

# 调色板
PALETTE_L = ["#60a5fa","#93c5fd","#bfdbfe","#dbeafe"]
PALETTE_R = ["#f87171","#fca5a5","#fecaca","#fee2e2"]


def row_centers(n, cx, cy, sp):
    return [np.array([cx + (i - (n-1)/2.0)*sp, cy, 0.0]) for i in range(n)]


def make_dot_row(n, cx, cy, sp, r, palette):
    grp = VGroup()
    for i, pos in enumerate(row_centers(n, cx, cy, sp)):
        c = Circle(radius=r,
                   fill_color=palette[i % len(palette)],
                   fill_opacity=1,
                   stroke_color=WHITE, stroke_width=2).move_to(pos)
        grp.add(c)
    return grp


# ═══════════════════════════════════════════════════════
# 主场景
# ═══════════════════════════════════════════════════════
class Decompose5(Scene):

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_DIM,
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.scene_1_hook()
        self.scene_2_splits()
        self.scene_3_combine()
        self.scene_4_summary()
        self.scene_5_outro()

    # ─────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────
    def scene_1_hook(self):
        title = Text("分与合", font=FONT, font_size=60, color=C_FIVE)
        title.move_to(UP * 5.5)
        sub = Text("5 可以怎么分？", font=FONT, font_size=36, color=WHITE)
        sub.move_to(UP * 4.5)
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 5个大圆飞入
        big5 = make_dot_row(TOP_N, 0.0, TOP_Y, TOP_SP, TOP_R,
                            [C_FIVE]*TOP_N)
        for c in big5:
            self.play(GrowFromCenter(c), run_time=0.18)

        # 大括号 + "5"
        brace = Brace(big5, direction=DOWN, color=C_FIVE)
        brace_lbl = Text("5", font=FONT, font_size=40, color=C_FIVE)
        brace_lbl.next_to(brace, DOWN, buff=0.15)
        self.play(GrowFromCenter(brace), FadeIn(brace_lbl), run_time=0.4)
        self.wait(0.5)

        q = Text("能分成两组吗？", font=FONT, font_size=30, color=C_ACTIVE)
        q.move_to(DOWN * 1.2)
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.7)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(big5),
            FadeOut(brace), FadeOut(brace_lbl), FadeOut(q),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 2: 逐个演示4种分法
    # ─────────────────────────────────────────
    def scene_2_splits(self):
        sec_title = Text("5 的分法", font=FONT, font_size=44, color=C_FIVE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        hint = Text("有序地想，不重复", font=FONT, font_size=24, color=C_DIM)
        hint.move_to(UP * 5.2)
        self.play(FadeIn(hint), run_time=0.3)

        for idx, (left_n, right_n) in enumerate(SPLITS):
            self._show_one_split(left_n, right_n, is_last=(idx == len(SPLITS)-1))

        self.play(FadeOut(sec_title), FadeOut(hint), run_time=0.4)

    def _show_one_split(self, left_n, right_n, is_last=False):
        # ── 顶部5个圆（黄色）
        top = make_dot_row(TOP_N, 0.0, TOP_Y, TOP_SP, TOP_R, [C_FIVE]*TOP_N)
        for c in top:
            self.play(GrowFromCenter(c), run_time=0.12)

        # ── 分拆线（从前 left_n 个和后 right_n 个分开）
        top_centers = row_centers(TOP_N, 0.0, TOP_Y, TOP_SP)
        lbot_centers = row_centers(left_n,  LEFT_CX,  BOT_Y, BOT_SP)
        rbot_centers = row_centers(right_n, RIGHT_CX, BOT_Y, BOT_SP)

        split_lines = VGroup()
        # 前 left_n 个向左下方聚合
        for i in range(left_n):
            line = DashedLine(
                top_centers[i] + DOWN * TOP_R,
                lbot_centers[i if i < left_n else 0] + UP * BOT_R,
                color=C_LEFT, stroke_width=1.5, dash_length=0.08,
            )
            split_lines.add(line)
        # 后 right_n 个向右下方聚合
        for i in range(right_n):
            line = DashedLine(
                top_centers[left_n + i] + DOWN * TOP_R,
                rbot_centers[i] + UP * BOT_R,
                color=C_RIGHT, stroke_width=1.5, dash_length=0.08,
            )
            split_lines.add(line)

        self.play(Create(split_lines), run_time=0.4)

        # ── 底部左右两组圆
        left_dots  = make_dot_row(left_n,  LEFT_CX,  BOT_Y, BOT_SP, BOT_R, PALETTE_L)
        right_dots = make_dot_row(right_n, RIGHT_CX, BOT_Y, BOT_SP, BOT_R, PALETTE_R)

        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in [*left_dots, *right_dots]],
                        lag_ratio=0.12),
            run_time=0.5,
        )

        # ── 左右标签
        lbl_l = Text(str(left_n),  font=FONT, font_size=44, color=C_LEFT)
        lbl_r = Text(str(right_n), font=FONT, font_size=44, color=C_RIGHT)
        lbl_l.next_to(left_dots,  DOWN, buff=0.25)
        lbl_r.next_to(right_dots, DOWN, buff=0.25)
        self.play(FadeIn(lbl_l), FadeIn(lbl_r), run_time=0.3)

        # ── 公式
        formula_str = f"5 = {left_n} + {right_n}"
        formula = MathTex(formula_str, font_size=62, color=WHITE)
        formula[0][0].set_color(C_FIVE)    # "5"
        formula[0][2].set_color(C_LEFT)    # left_n
        formula[0][4].set_color(C_RIGHT)   # right_n
        formula.move_to(DOWN * 1.8)
        self.play(Write(formula), run_time=0.5)
        self.wait(0.8)

        # 清场（保留到下一个）
        self.play(
            FadeOut(top), FadeOut(split_lines),
            FadeOut(left_dots), FadeOut(right_dots),
            FadeOut(lbl_l), FadeOut(lbl_r), FadeOut(formula),
            run_time=0.4 if not is_last else 0.2,
        )

    # ─────────────────────────────────────────
    # Scene 3: 合起来（逆向）
    # ─────────────────────────────────────────
    def scene_3_combine(self):
        sec_title = Text("合起来", font=FONT, font_size=44, color=C_ACTIVE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        # 左2 + 右3 → 合成5
        left_n, right_n = 2, 3
        left_dots  = make_dot_row(left_n,  LEFT_CX, BOT_Y+0.5, BOT_SP, BOT_R, PALETTE_L)
        right_dots = make_dot_row(right_n, RIGHT_CX, BOT_Y+0.5, BOT_SP, BOT_R, PALETTE_R)

        for c in [*left_dots, *right_dots]:
            self.play(GrowFromCenter(c), run_time=0.15)

        lbl_l = Text("2", font=FONT, font_size=44, color=C_LEFT)
        lbl_r = Text("3", font=FONT, font_size=44, color=C_RIGHT)
        lbl_l.next_to(left_dots,  DOWN, buff=0.2)
        lbl_r.next_to(right_dots, DOWN, buff=0.2)
        self.play(FadeIn(lbl_l), FadeIn(lbl_r), run_time=0.3)

        # 合并箭头
        arrow_l = Arrow(
            LEFT_CX * RIGHT * 0.5 + UP * (BOT_Y + 0.5),
            ORIGIN + UP * TOP_Y,
            color=C_LEFT, stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
        )
        arrow_r = Arrow(
            RIGHT_CX * RIGHT * 0.5 + UP * (BOT_Y + 0.5),
            ORIGIN + UP * TOP_Y,
            color=C_RIGHT, stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
        )
        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=0.5)

        # 合并成5个圆
        top = make_dot_row(TOP_N, 0.0, TOP_Y, TOP_SP, TOP_R, [C_ACTIVE]*TOP_N)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in top], lag_ratio=0.1),
            run_time=0.6,
        )

        brace = Brace(top, direction=DOWN, color=C_ACTIVE)
        big5 = Text("5", font=FONT, font_size=46, color=C_ACTIVE)
        big5.next_to(brace, DOWN, buff=0.15)
        self.play(GrowFromCenter(brace), FadeIn(big5), run_time=0.4)

        shout = Text("合起来还是 5！", font=FONT, font_size=32, color=C_ACTIVE)
        shout.move_to(DOWN * 1.5)
        self.play(Write(shout), run_time=0.5)

        formula = MathTex(r"2 + 3 = 5", font_size=62, color=WHITE)
        formula[0][0].set_color(C_LEFT)
        formula[0][2].set_color(C_RIGHT)
        formula[0][4].set_color(C_ACTIVE)
        formula.move_to(DOWN * 2.8)
        self.play(Write(formula), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(sec_title),
            FadeOut(left_dots), FadeOut(right_dots),
            FadeOut(lbl_l), FadeOut(lbl_r),
            FadeOut(arrow_l), FadeOut(arrow_r),
            FadeOut(top), FadeOut(brace), FadeOut(big5),
            FadeOut(shout), FadeOut(formula),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 4: 汇总表格
    # ─────────────────────────────────────────
    def scene_4_summary(self):
        sec_title = Text("5 的全部分法", font=FONT, font_size=40, color=C_FIVE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        # 居中大数字5
        big5 = Text("5", font=FONT, font_size=90, color=C_FIVE)
        big5.move_to(UP * 4.4)
        self.play(GrowFromCenter(big5), run_time=0.5)

        # 4行分法用 VGroup 竖排
        rows = VGroup()
        formulas_str = [
            (r"5 = 1 + 4", C_LEFT,  C_RIGHT),
            (r"5 = 2 + 3", C_LEFT,  C_RIGHT),
            (r"5 = 3 + 2", C_LEFT,  C_RIGHT),
            (r"5 = 4 + 1", C_LEFT,  C_RIGHT),
        ]
        for left_n, right_n in SPLITS:
            tex = MathTex(f"5 = {left_n} + {right_n}", font_size=52, color=WHITE)
            tex[0][0].set_color(C_FIVE)
            tex[0][2].set_color(C_LEFT)
            tex[0][4].set_color(C_RIGHT)
            rows.add(tex)

        rows.arrange(DOWN, buff=0.55).move_to(UP * 1.8)

        for row in rows:
            self.play(Write(row), run_time=0.35)

        # 口诀
        tip = Text("有序地想，不重复！", font=FONT, font_size=28, color=C_DIM)
        tip.move_to(DOWN * 3.0)
        self.play(FadeIn(tip), run_time=0.4)

        # 加减关系提示
        base_tip = Text("这是加减法的基础！", font=FONT, font_size=28, color=C_ACTIVE)
        base_tip.move_to(DOWN * 4.0)
        self.play(Write(base_tip), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title), FadeOut(big5),
            FadeOut(rows), FadeOut(tip), FadeOut(base_tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 5: 片尾
    # ─────────────────────────────────────────
    def scene_5_outro(self):
        card = RoundedRectangle(
            width=7.5, height=5.0, corner_radius=0.4,
            fill_color="#0f1b2e", fill_opacity=1,
            stroke_color=C_FIVE, stroke_width=3,
        ).move_to(UP * 4.0)

        card_title = Text("记住啦！", font=FONT, font_size=34, color=C_FIVE)
        card_title.next_to(card, UP, buff=-0.55)

        summary_rows = VGroup()
        for left_n, right_n in SPLITS:
            row = MathTex(f"5 = {left_n} + {right_n}", font_size=46, color=WHITE)
            row[0][0].set_color(C_FIVE)
            row[0][2].set_color(C_LEFT)
            row[0][4].set_color(C_RIGHT)
            summary_rows.add(row)
        summary_rows.arrange(DOWN, buff=0.4).move_to(card)

        self.play(Create(card), FadeIn(card_title), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT*0.3) for r in summary_rows],
                        lag_ratio=0.15),
            run_time=0.8,
        )

        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=34, color=WHITE).move_to(UP * 0.6)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=26, color=C_DIM).move_to(DOWN * 0.1)
        follow     = Text("关注我，学更多数学！",
                          font=FONT, font_size=28, color=C_ACTIVE).move_to(DOWN * 1.0)

        self.play(Transform(self.author_bar, author_big), run_time=0.5)
        self.play(FadeIn(author_id), FadeIn(follow, scale=1.1), run_time=0.5)

        # 5个彩色小圆装饰
        deco = VGroup(*[
            Circle(radius=0.22,
                   fill_color=[C_FIVE, C_LEFT, C_RIGHT, C_ACTIVE, "#8b5cf6"][i],
                   fill_opacity=1, stroke_width=0
                   ).move_to(np.array([(i-2)*1.3, -2.5, 0]))
            for i in range(5)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in deco], lag_ratio=0.1),
            run_time=0.6,
        )
        self.wait(1.2)
        self.play(
            FadeOut(self.author_bar), FadeOut(author_id), FadeOut(follow),
            FadeOut(card), FadeOut(card_title), FadeOut(summary_rows),
            FadeOut(deco),
            run_time=1.0,
        )


# ═══════════════════════════════════════════════════════
# manim -pql decompose5.py Decompose5
# manim -qh  decompose5.py Decompose5
# ═══════════════════════════════════════════════════════
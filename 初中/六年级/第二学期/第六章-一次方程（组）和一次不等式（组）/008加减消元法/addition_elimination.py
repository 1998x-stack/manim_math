"""
加减消元法 - Manim 教学动画
六年级 第二学期 第六章

内容: 加减消元法 — 两个例题，涵盖直接相加/相减 & 先乘系数再消元
目标观众: 六年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

例1 (直接相加):
    2x + y = 7   ..①
    3x - y = 8   ..②
    y 系数互为相反数 → ①+② → 5x=15 → x=3, y=1

例2 (先乘系数再相减):
    3x + 2y = 12  ..①
    x  + y  = 5   ..②
    ②×2 → 2x+2y=10  ..②'
    ①−②' → x=2 → y=3

渲染命令:
    manim -pql addition_elimination.py AdditionElimination   # 预览
    manim -qh  addition_elimination.py AdditionElimination   # 高质量
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# TikTok 竖屏配置
# ─────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────
# 颜色系统
# ─────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
COLOR_EQ1       = "#e74c3c"   # 红   — 方程①
COLOR_EQ2       = "#3498db"   # 蓝   — 方程②
COLOR_EQ2P      = "#1abc9c"   # 青绿 — 变形后的②'
COLOR_X         = "#f39c12"   # 橙   — x
COLOR_Y         = "#9b59b6"   # 紫   — y
COLOR_CANCEL    = "#e74c3c"   # 红   — 消去项（划线）
COLOR_RESULT    = "#2ecc71"   # 绿   — 解
COLOR_HIGHLIGHT = YELLOW
COLOR_CARD      = "#0f3460"
COLOR_DARK      = "#16213e"
FONT            = "Noto Sans CJK SC"

# ─────────────────────────────────────────────
# 工具
# ─────────────────────────────────────────────

def rcard(w=7.5, h=1.8, fill=COLOR_CARD, stroke=None, r=0.28):
    return RoundedRectangle(
        width=w, height=h, corner_radius=r,
        fill_color=fill, fill_opacity=1,
        stroke_color=stroke or fill,
        stroke_width=0 if stroke is None else 2,
    )


def sec_title(text, color=COLOR_HIGHLIGHT, size=30, y=6.3):
    return Text(text, font=FONT, font_size=size, color=color,
                weight=BOLD).move_to(UP * y)


def coeff_badge(text, color):
    """系数徽章，用于乘法标注"""
    bg = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.12,
                          fill_color=color, fill_opacity=0.25,
                          stroke_color=color, stroke_width=1.5)
    label = MathTex(text, font_size=22, color=color)
    return VGroup(bg, label)


def strikethrough(mob, color=COLOR_CANCEL):
    """给 mobject 画删除线"""
    return Line(
        mob.get_left()  + LEFT  * 0.05,
        mob.get_right() + RIGHT * 0.05,
        color=color, stroke_width=4,
    )


# ─────────────────────────────────────────────
# 主场景
# ─────────────────────────────────────────────

class AdditionElimination(Scene):
    """
    加减消元法 教学动画

    场景:
      1. 开场钩子
      2. 三种情况概览
      3. 例1 — 系数互为相反数 → 直接相加消 y
      4. 例2 — 系数不同 → 先乘系数，再相减消 y
      5. 对比总结 + 口诀 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_example1_direct_add()
        self.scene_4_example2_scale_then_sub()
        self.scene_5_summary_outro()

    # ══════════════════════════════════════════
    # Scene 1  开场钩子
    # ══════════════════════════════════════════

    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        title = Text("加减消元法", font=FONT, font_size=54,
                     color=WHITE, weight=BOLD).move_to(UP * 5.7)
        subtitle = Text("把两个方程相加或相减，消去一个未知数",
                        font=FONT, font_size=23, color=COLOR_HIGHLIGHT,
                        ).move_to(UP * 4.6)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.4)

        # 钩子：展示两套方程组
        hook1 = self._sys_mob(r"2x+y=7", r"3x-y=8", UP * 3.1, 34,
                              labeled=True)
        arrow_mid = Arrow(UP * 1.9, UP * 1.1,
                          color=COLOR_RESULT, stroke_width=3,
                          max_tip_length_to_length_ratio=0.22)
        ans1 = MathTex(r"x=3,\;y=1", font_size=40,
                       color=COLOR_RESULT).move_to(UP * 0.5)

        self.play(FadeIn(hook1, shift=UP * 0.3, scale=0.92), run_time=0.5)
        self.play(GrowArrow(arrow_mid), run_time=0.3)
        self.play(Write(ans1), run_time=0.5)

        question = Text("怎么用加减法解方程组？",
                        font=FONT, font_size=26,
                        color=COLOR_HIGHLIGHT).move_to(DOWN * 0.8)
        self.play(FadeIn(question, scale=1.05), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(hook1), FadeOut(arrow_mid),
            FadeOut(ans1), FadeOut(question),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 2  三种情况概览
    # ══════════════════════════════════════════

    def scene_2_overview(self):
        title = sec_title("加减消元法  ·  三种情况", y=6.4)
        self.play(Write(title), run_time=0.4)

        cases = [
            (COLOR_EQ2,  "情况①",
             "系数互为相反数 → 直接相加",
             r"+1  \text{ vs }  -1",),
            (COLOR_EQ1,  "情况②",
             "系数完全相同   → 直接相减",
             r"+2  \text{ vs }  +2",),
            (COLOR_X,    "情况③",
             "系数不同      → 先乘系数再相加/减",
             r"+2  \text{ vs }  +1  \Rightarrow  \times 2",),
        ]

        y_pos = [4.8, 2.9, 1.0]
        cards = VGroup()
        for (color, head, body, formula), yp in zip(cases, y_pos):
            bg = rcard(7.5, 1.65, COLOR_DARK, color)
            bg.move_to(UP * yp)

            title_t = Text(head, font=FONT, font_size=22,
                           color=color, weight=BOLD)
            body_t  = Text(body, font=FONT, font_size=20, color=WHITE)
            col     = VGroup(title_t, body_t).arrange(DOWN, buff=0.12,
                                                      aligned_edge=LEFT)
            col.move_to(bg.get_center() + LEFT * 0.3)
            cards.add(VGroup(bg, col))

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.3)

        note = Text("本节重点讲情况①和情况③，最常考！",
                    font=FONT, font_size=22,
                    color=COLOR_HIGHLIGHT).move_to(DOWN * 0.7)
        self.play(FadeIn(note, scale=1.04), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(cards), FadeOut(note), run_time=0.4)

    # ══════════════════════════════════════════
    # Scene 3  例1 — 直接相加消 y
    # ══════════════════════════════════════════

    def scene_3_example1_direct_add(self):
        title = sec_title("例1  系数互为相反数 → 直接相加",
                          color=COLOR_EQ2, y=6.4, size=26)
        self.play(Write(title), run_time=0.4)

        # 顶部小字方程组
        sys_sm = self._sys_mob(r"2x+y=7", r"3x-y=8",
                               UP * 5.5, 22, labeled=True)
        self.play(FadeIn(sys_sm), run_time=0.3)

        hint = Text("观察 y 的系数：+1 和 -1，互为相反数！",
                    font=FONT, font_size=22,
                    color=COLOR_HIGHLIGHT).move_to(UP * 4.5)
        self.play(FadeIn(hint), run_time=0.3)

        # ── 展示两方程（带系数标注）──
        eq1_mob, eq1_row = self._eq_row(r"2x", r"+", r"y",  r"=", r"7",
                                         "①", COLOR_EQ1, UP * 3.4,
                                         x_color=COLOR_X, y_color=COLOR_Y)
        eq2_mob, eq2_row = self._eq_row(r"3x", r"-", r"y",  r"=", r"8",
                                         "②", COLOR_EQ2, UP * 2.2,
                                         x_color=COLOR_X, y_color=COLOR_Y)

        self.play(FadeIn(eq1_row), run_time=0.4)
        self.play(FadeIn(eq2_row), run_time=0.4)

        # y 系数高亮（+1 和 -1 互消）
        y1 = eq1_mob[2]   # "+y" 中的 y
        y2 = eq2_mob[2]   # "-y" 中的 y
        coeff1_badge = Text("+1", font=FONT, font_size=20,
                            color=COLOR_CANCEL).next_to(y1, UP, buff=0.05)
        coeff2_badge = Text("-1", font=FONT, font_size=20,
                            color=COLOR_CANCEL).next_to(y2, UP, buff=0.05)
        self.play(
            y1.animate.set_color(COLOR_CANCEL),
            y2.animate.set_color(COLOR_CANCEL),
            FadeIn(coeff1_badge), FadeIn(coeff2_badge),
            run_time=0.5,
        )

        cancel_tip = Text("(+1) + (-1) = 0  →  y 被消去！",
                          font=FONT, font_size=21,
                          color=COLOR_CANCEL).move_to(UP * 1.3)
        self.play(FadeIn(cancel_tip), run_time=0.3)

        # 加号 & 横线
        plus_sign = Text("+", font=FONT, font_size=44,
                         color=COLOR_HIGHLIGHT, weight=BOLD)
        plus_sign.next_to(eq2_row, LEFT, buff=0.18)
        h_line = Line(LEFT * 3.5, RIGHT * 3.5,
                      color=GRAY_A, stroke_width=2).move_to(UP * 0.8)

        self.play(FadeIn(plus_sign), Create(h_line), run_time=0.35)

        # 删除线穿过 y 和 -y
        cross1 = strikethrough(y1)
        cross2 = strikethrough(y2)
        self.play(Create(cross1), Create(cross2), run_time=0.4)
        self.wait(0.3)

        # ── ①+② 结果：5x = 15 ──
        result_add = MathTex(r"5x", r"=", r"15", font_size=46)
        result_add[0].set_color(COLOR_X)
        add_label = Text("①+②", font=FONT, font_size=22,
                         color=GRAY_A)
        add_row = VGroup(result_add, add_label).arrange(RIGHT, buff=0.35)
        add_row.move_to(UP * 0.1)

        self.play(Write(result_add), FadeIn(add_label), run_time=0.5)

        # x = 3
        arr1 = self._dn_arrow(DOWN * 0.55, color=COLOR_X)
        x_sol = MathTex(r"x = 3", font_size=50, color=COLOR_X)
        x_sol.move_to(DOWN * 1.35)
        self.play(GrowArrow(arr1), run_time=0.3)
        self.play(Write(x_sol), run_time=0.4)
        self.play(Flash(x_sol, color=COLOR_X, flash_radius=0.6), run_time=0.35)

        # ── 回代求 y ──
        back_label = Text("把 x=3 代入方程①",
                          font=FONT, font_size=22,
                          color=COLOR_EQ1).move_to(DOWN * 2.4)
        backsub = MathTex(r"2(3)+y=7\;\Rightarrow\;6+y=7",
                          font_size=34).move_to(DOWN * 3.2)
        y_sol = MathTex(r"y = 1", font_size=50, color=COLOR_Y)
        y_sol.move_to(DOWN * 4.1)

        self.play(FadeIn(back_label), run_time=0.3)
        self.play(Write(backsub), run_time=0.5)
        self.play(Write(y_sol), run_time=0.4)
        self.play(Flash(y_sol, color=COLOR_Y, flash_radius=0.6), run_time=0.35)

        # ── 解框 ──
        sol1_bg = RoundedRectangle(
            width=6.8, height=1.6, corner_radius=0.3,
            fill_color=COLOR_RESULT, fill_opacity=0.13,
            stroke_color=COLOR_RESULT, stroke_width=3,
        ).move_to(DOWN * 5.4)
        sol1_tex = MathTex(r"x=3,\quad y=1",
                           font_size=44, color=COLOR_RESULT).move_to(DOWN * 5.4)

        self.play(FadeIn(sol1_bg), Write(sol1_tex), run_time=0.5)
        self.play(Flash(sol1_tex, color=COLOR_RESULT, flash_radius=0.9),
                  run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sys_sm), FadeOut(hint),
            FadeOut(eq1_row), FadeOut(eq2_row),
            FadeOut(coeff1_badge), FadeOut(coeff2_badge), FadeOut(cancel_tip),
            FadeOut(plus_sign), FadeOut(h_line),
            FadeOut(cross1), FadeOut(cross2),
            FadeOut(add_row), FadeOut(arr1), FadeOut(x_sol),
            FadeOut(back_label), FadeOut(backsub), FadeOut(y_sol),
            FadeOut(sol1_bg), FadeOut(sol1_tex),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 4  例2 — 先乘系数，再相减消 y
    # ══════════════════════════════════════════

    def scene_4_example2_scale_then_sub(self):
        title = sec_title("例2  系数不同 → 先乘系数再相减",
                          color=COLOR_X, y=6.4, size=26)
        self.play(Write(title), run_time=0.4)

        sys_sm = self._sys_mob(r"3x+2y=12", r"x+y=5",
                               UP * 5.5, 22, labeled=True)
        self.play(FadeIn(sys_sm), run_time=0.3)

        hint = Text("y 的系数：+2 和 +1，不互为相反数",
                    font=FONT, font_size=22,
                    color=GRAY_A).move_to(UP * 4.5)
        hint2 = Text("→ 让②两边乘以 2，使系数相同！",
                     font=FONT, font_size=22,
                     color=COLOR_HIGHLIGHT).move_to(UP * 3.8)
        self.play(FadeIn(hint), run_time=0.3)
        self.play(FadeIn(hint2), run_time=0.3)

        # 展示原方程组
        eq1_mob, eq1_row = self._eq_row(r"3x", r"+", r"2y", r"=", r"12",
                                         "①", COLOR_EQ1, UP * 2.7,
                                         x_color=COLOR_X, y_color=COLOR_Y)
        eq2_mob, eq2_row = self._eq_row(r"x",  r"+", r"y",  r"=", r"5",
                                         "②", COLOR_EQ2, UP * 1.5,
                                         x_color=COLOR_X, y_color=COLOR_Y)

        self.play(FadeIn(eq1_row), FadeIn(eq2_row), run_time=0.4)

        # × 2 标注在 ② 旁
        times2 = Text("× 2", font=FONT, font_size=26,
                      color=COLOR_EQ2P, weight=BOLD)
        times2.next_to(eq2_row, RIGHT, buff=0.25)
        times2_box = SurroundingRectangle(times2, color=COLOR_EQ2P,
                                          stroke_width=2, buff=0.08)
        times2_box.set_fill(COLOR_EQ2P, opacity=0.12)
        self.play(FadeIn(times2), Create(times2_box), run_time=0.4)

        # 变形箭头
        tf_arrow = Arrow(UP * 0.9, UP * 0.2,
                         color=COLOR_EQ2P, stroke_width=3,
                         max_tip_length_to_length_ratio=0.24)
        tf_label = Text("②×2  得", font=FONT, font_size=20,
                        color=COLOR_EQ2P).next_to(tf_arrow, RIGHT, buff=0.15)
        self.play(GrowArrow(tf_arrow), FadeIn(tf_label), run_time=0.3)

        # ②'：2x + 2y = 10
        eq2p_mob, eq2p_row = self._eq_row(r"2x", r"+", r"2y", r"=", r"10",
                                            "②'", COLOR_EQ2P,
                                            DOWN * 0.5,
                                            x_color=COLOR_X,
                                            y_color=COLOR_EQ2P)
        self.play(FadeIn(eq2p_row), run_time=0.5)

        # y 系数对比高亮
        y1_orig = eq1_mob[2]   # 2y in ①
        y2p     = eq2p_mob[2]  # 2y in ②'
        self.play(
            y1_orig.animate.set_color(COLOR_CANCEL),
            y2p.animate.set_color(COLOR_CANCEL),
            run_time=0.4,
        )

        equal_tip = Text("y 系数现在都是 +2，相减可消去！",
                         font=FONT, font_size=21,
                         color=COLOR_CANCEL).move_to(DOWN * 1.5)
        self.play(FadeIn(equal_tip), run_time=0.3)

        # 减号 & 横线
        minus_sign = Text("−", font=FONT, font_size=48,
                          color=COLOR_HIGHLIGHT, weight=BOLD)
        minus_sign.next_to(eq2p_row, LEFT, buff=0.18)
        h_line2 = Line(LEFT * 3.5, RIGHT * 3.5,
                       color=GRAY_A, stroke_width=2).move_to(DOWN * 2.0)

        self.play(FadeIn(minus_sign), Create(h_line2), run_time=0.3)

        # 删除线
        cross1 = strikethrough(y1_orig)
        cross2 = strikethrough(y2p)
        self.play(Create(cross1), Create(cross2), run_time=0.4)
        self.wait(0.3)

        # ── ①−②' 结果：x = 2 ──
        result_sub = MathTex(r"x", r"=", r"2", font_size=48)
        result_sub[0].set_color(COLOR_X)
        result_sub[2].set_color(COLOR_X)
        sub_label = Text("①−②'", font=FONT, font_size=21, color=GRAY_A)
        sub_row = VGroup(result_sub, sub_label).arrange(RIGHT, buff=0.3)
        sub_row.move_to(DOWN * 2.7)

        self.play(Write(result_sub), FadeIn(sub_label), run_time=0.5)
        self.play(Flash(result_sub, color=COLOR_X, flash_radius=0.5),
                  run_time=0.35)

        # ── 回代 ──
        back2 = Text("代入方程②：x+y=5",
                     font=FONT, font_size=22,
                     color=COLOR_EQ2).move_to(DOWN * 3.6)
        backsub2 = MathTex(r"2+y=5\;\Rightarrow\;y=3",
                           font_size=36).move_to(DOWN * 4.4)
        y_sol2 = MathTex(r"y=3", font_size=50, color=COLOR_Y)
        y_sol2.move_to(DOWN * 5.2)

        self.play(FadeIn(back2), run_time=0.3)
        self.play(Write(backsub2), run_time=0.5)
        self.play(Write(y_sol2), run_time=0.4)
        self.play(Flash(y_sol2, color=COLOR_Y, flash_radius=0.6), run_time=0.35)

        # ── 解框 ──
        sol2_bg = RoundedRectangle(
            width=6.8, height=1.6, corner_radius=0.3,
            fill_color=COLOR_RESULT, fill_opacity=0.13,
            stroke_color=COLOR_RESULT, stroke_width=3,
        ).move_to(DOWN * 6.2)
        sol2_tex = MathTex(r"x=2,\quad y=3",
                           font_size=44, color=COLOR_RESULT).move_to(DOWN * 6.2)

        self.play(FadeIn(sol2_bg), Write(sol2_tex), run_time=0.5)
        self.play(Flash(sol2_tex, color=COLOR_RESULT, flash_radius=0.9),
                  run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sys_sm),
            FadeOut(hint), FadeOut(hint2),
            FadeOut(eq1_row), FadeOut(eq2_row),
            FadeOut(times2), FadeOut(times2_box),
            FadeOut(tf_arrow), FadeOut(tf_label),
            FadeOut(eq2p_row),
            FadeOut(equal_tip), FadeOut(minus_sign), FadeOut(h_line2),
            FadeOut(cross1), FadeOut(cross2),
            FadeOut(sub_row),
            FadeOut(back2), FadeOut(backsub2), FadeOut(y_sol2),
            FadeOut(sol2_bg), FadeOut(sol2_tex),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 5  对比总结 + 口诀 + 片尾
    # ══════════════════════════════════════════

    def scene_5_summary_outro(self):
        title = sec_title("加减消元法  ·  解题口诀", y=6.5, size=28)
        self.play(Write(title), run_time=0.4)

        # ── 口诀卡 ──
        steps = [
            (COLOR_EQ2P,    "①",
             "观察系数，决定加还是减"),
            (COLOR_HIGHLIGHT, "②",
             "若系数不同，先乘适当倍数"),
            (COLOR_CANCEL,   "③",
             "相加或相减，消去一个未知数"),
            (COLOR_Y,        "④",
             "解一元方程，求出一个值"),
            (COLOR_X,        "⑤",
             "回代，求另一个未知数"),
        ]

        y0 = 5.0
        cards = VGroup()
        for i, (color, num, text) in enumerate(steps):
            bg = rcard(7.5, 1.45, COLOR_DARK, color)
            bg.move_to(UP * (y0 - i * 1.65))
            num_t  = Text(num,  font=FONT, font_size=24,
                          color=color, weight=BOLD)
            body_t = Text(text, font=FONT, font_size=21, color=WHITE)
            row = VGroup(num_t, body_t).arrange(RIGHT, buff=0.3)
            row.move_to(bg.get_center())
            cards.add(VGroup(bg, row))

        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.4), run_time=0.28)

        # 关键提示
        key_tip = Text(
            "关键：让某个未知数系数相同或互为相反数",
            font=FONT, font_size=21, color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(key_tip, scale=1.04), run_time=0.4)
        self.wait(1.8)

        # 清理进入片尾
        self.play(
            FadeOut(title), FadeOut(cards), FadeOut(key_tip),
            run_time=0.4,
        )

        # ── 对比展示两例答案 ──
        ex_title = Text("两道例题回顾",
                        font=FONT, font_size=30,
                        color=COLOR_HIGHLIGHT, weight=BOLD).move_to(UP * 4.5)
        self.play(Write(ex_title), run_time=0.4)

        ex1_bg = rcard(7.0, 2.4, COLOR_CARD, COLOR_EQ2)
        ex1_bg.move_to(UP * 2.7)
        ex1_head = Text("例1  (系数互为相反数 → 相加)",
                        font=FONT, font_size=21, color=COLOR_EQ2)
        ex1_sys  = self._sys_mob(r"2x+y=7", r"3x-y=8",
                                  ORIGIN, 28, labeled=True)
        ex1_ans  = MathTex(r"\Rightarrow\;x=3,\;y=1",
                           font_size=32, color=COLOR_RESULT)
        ex1_row  = VGroup(ex1_sys, ex1_ans).arrange(RIGHT, buff=0.35)
        ex1_grp  = VGroup(ex1_head, ex1_row).arrange(DOWN, buff=0.2)
        ex1_grp.move_to(UP * 2.7)

        ex2_bg = rcard(7.0, 2.4, COLOR_CARD, COLOR_X)
        ex2_bg.move_to(UP * 0.1)
        ex2_head = Text("例2  (系数不同 → 乘倍数再相减)",
                        font=FONT, font_size=21, color=COLOR_X)
        ex2_sys  = self._sys_mob(r"3x+2y=12", r"x+y=5",
                                  ORIGIN, 28, labeled=True)
        ex2_ans  = MathTex(r"\Rightarrow\;x=2,\;y=3",
                           font_size=32, color=COLOR_RESULT)
        ex2_row  = VGroup(ex2_sys, ex2_ans).arrange(RIGHT, buff=0.35)
        ex2_grp  = VGroup(ex2_head, ex2_row).arrange(DOWN, buff=0.2)
        ex2_grp.move_to(UP * 0.1)

        self.play(FadeIn(ex1_bg), FadeIn(ex1_grp), run_time=0.5)
        self.play(FadeIn(ex2_bg), FadeIn(ex2_grp), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(ex_title),
            FadeOut(ex1_bg), FadeOut(ex1_grp),
            FadeOut(ex2_bg), FadeOut(ex2_grp),
            run_time=0.4,
        )

        # ── 片尾 ──
        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=38,
                          color=WHITE, weight=BOLD).move_to(UP * 1.5)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=28,
                          color=GRAY_B).move_to(UP * 0.5)
        follow     = Text("关注我，获得更多数学技巧！",
                          font=FONT, font_size=28,
                          color=COLOR_HIGHLIGHT).move_to(DOWN * 0.7)

        # 装饰：加号和减号交替旋转
        pm_group = VGroup(*[
            Text(["＋", "−"][i % 2], font=FONT,
                 font_size=32,
                 color=[COLOR_EQ2, COLOR_X][i % 2]).move_to(
                np.array([
                    np.cos(i * TAU / 8) * 2.5,
                    np.sin(i * TAU / 8) * 2.5 - 2.8,
                    0,
                ])
            )
            for i in range(8)
        ])

        self.play(
            Transform(self.author, author_big),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=0.7,
        )
        self.play(FadeIn(follow, scale=1.08), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(s, scale=0.5) for s in pm_group],
                        lag_ratio=0.07),
            run_time=0.5,
        )
        self.play(Rotate(pm_group, angle=TAU / 3,
                         about_point=DOWN * 2.8), run_time=1.2)
        self.wait(1.0)
        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(pm_group),
            run_time=0.8,
        )

    # ══════════════════════════════════════════
    # 辅助方法
    # ══════════════════════════════════════════

    def _sys_mob(self, eq1_str, eq2_str, pos, size=36, labeled=False):
        """带大括号的方程组"""
        e1 = MathTex(eq1_str, font_size=size)
        e2 = MathTex(eq2_str, font_size=size)
        if labeled:
            t1 = Text("①", font=FONT,
                      font_size=int(size * 0.75), color=COLOR_EQ1)
            t2 = Text("②", font=FONT,
                      font_size=int(size * 0.75), color=COLOR_EQ2)
            r1 = VGroup(e1, t1).arrange(RIGHT, buff=0.22)
            r2 = VGroup(e2, t2).arrange(RIGHT, buff=0.22)
        else:
            r1, r2 = e1, e2
        rows  = VGroup(r1, r2).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        brace = MathTex(r"\left\{", font_size=int(size * 1.7), color=WHITE)
        brace.next_to(rows, LEFT, buff=0.06)
        return VGroup(brace, rows).move_to(pos)

    def _eq_row(self, t1, op, t2, eq, rhs,
                tag_str, tag_color, pos,
                x_color=WHITE, y_color=WHITE):
        """
        创建一行方程 MathTex 并返回 (mob, VGroup_with_tag)
        t1=左侧项, op=运算符, t2=右侧项, eq='=', rhs=右值
        """
        mob = MathTex(t1, op, t2, eq, rhs, font_size=42)
        # 对 x 项和 y 项上色
        mob[0].set_color(x_color)   # 第一项（含 x）
        mob[2].set_color(y_color)   # 第三项（含 y）
        tag = Text(tag_str, font=FONT,
                   font_size=28, color=tag_color)
        row = VGroup(mob, tag).arrange(RIGHT, buff=0.35)
        row.move_to(pos)
        return mob, row

    def _dn_arrow(self, pos, length=0.6, color=GRAY_B):
        return Arrow(pos, pos + DOWN * length,
                     color=color, stroke_width=2.5,
                     max_tip_length_to_length_ratio=0.28)
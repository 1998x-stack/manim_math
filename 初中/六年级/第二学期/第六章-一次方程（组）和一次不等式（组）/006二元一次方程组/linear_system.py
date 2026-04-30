"""
二元一次方程组 - Manim 教学动画
六年级 第二学期 第六章

内容: 二元一次方程组的概念 + 代入消元法 + 加减消元法
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

例题:
  2x + y = 7  ..①
  x  - y = 2  ..②
  解: x=3, y=1

渲染命令:
  manim -pql linear_system.py LinearSystem     # 快速预览
  manim -qh  linear_system.py LinearSystem     # 高质量
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# 全局配置  TikTok 竖屏
# ─────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────
# 颜色
# ─────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
COLOR_EQ1       = "#e74c3c"   # 红  — 方程①
COLOR_EQ2       = "#3498db"   # 蓝  — 方程②
COLOR_X         = "#f39c12"   # 橙  — x
COLOR_Y         = "#9b59b6"   # 紫  — y
COLOR_RESULT    = "#2ecc71"   # 绿  — 结果 / 解
COLOR_HIGHLIGHT = YELLOW
COLOR_CARD      = "#0f3460"   # 卡片背景
COLOR_STEP_BG   = "#16213e"   # 步骤底色
FONT            = "PingFang SC"

# ─────────────────────────────────────────────
# 工具函数
# ─────────────────────────────────────────────

def h_card(width=7.5, height=1.8, color=COLOR_CARD, stroke=None, r=0.3):
    """圆角矩形卡片"""
    return RoundedRectangle(
        width=width, height=height,
        corner_radius=r,
        fill_color=color, fill_opacity=1,
        stroke_color=stroke or color,
        stroke_width=0 if stroke is None else 2,
    )


def eq_label(n, color=WHITE, size=22):
    """方程编号 ① ②"""
    return Text(f"…①" if n == 1 else "…②", font=FONT, font_size=size, color=color)


def section_title(text, color=COLOR_HIGHLIGHT, size=32, y=6.0):
    return Text(text, font=FONT, font_size=size, color=color,
                weight=BOLD).move_to(UP * y)


def step_label(n, color=WHITE):
    """Step n 标签"""
    return Text(f"Step {n}", font=FONT, font_size=20, color=color, weight=BOLD)


# ─────────────────────────────────────────────
# 主场景
# ─────────────────────────────────────────────

class LinearSystem(Scene):
    """
    二元一次方程组 教学动画

    场景:
      1. 开场钩子
      2. 概念定义
      3. 消元核心思想
      4. 代入消元法（逐步）
      5. 加减消元法（逐步）
      6. 验证 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_content()   # 预生成复用对象

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_elimination_idea()
        self.scene_4_substitution()
        self.scene_5_addition_elimination()
        self.scene_6_verify_outro()

    # ══════════════════════════════════════════
    # 内容预生成
    # ══════════════════════════════════════════

    def setup_content(self):
        """预生成复用内容（不添加到场景）"""

        # ── 方程组两行 ──
        # 行①: 2x + y = 7
        self.EQ1_tex = MathTex(
            r"2x", r"+", r"y", r"=", r"7",
            font_size=40
        )
        self.EQ1_tex[0].set_color(COLOR_X)      # 2x 橙色
        self.EQ1_tex[2].set_color(COLOR_Y)      # y  紫色

        # 行②: x - y = 2
        self.EQ2_tex = MathTex(
            r"x", r"-", r"y", r"=", r"2",
            font_size=40
        )
        self.EQ2_tex[0].set_color(COLOR_X)
        self.EQ2_tex[2].set_color(COLOR_Y)

    # ══════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════

    def scene_1_opening(self):
        # 作者（顶部常驻）
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 大标题
        title = Text(
            "二元一次方程组",
            font=FONT, font_size=46, color=WHITE, weight=BOLD
        ).move_to(UP * 5.7)

        subtitle = Text(
            "消元法 — 化二为一",
            font=FONT, font_size=30, color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.7)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.4)

        # 展示方程组
        hook_sys = self._make_system_mob(UP * 3.0, size=36)
        self.play(FadeIn(hook_sys, shift=UP * 0.5, scale=0.9), run_time=0.7)

        # 箭头 → 答案
        arrow = Arrow(
            start=UP * 1.8, end=UP * 0.7,
            color=COLOR_RESULT, stroke_width=4,
            max_tip_length_to_length_ratio=0.18
        )
        answer = MathTex(r"x = 3, \quad y = 1",
                         font_size=44, color=COLOR_RESULT)
        answer.move_to(UP * 0.2)

        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(answer), run_time=0.6)

        question = Text(
            "你知道怎么解吗？",
            font=FONT, font_size=28, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(question, scale=1.05), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(hook_sys),
            FadeOut(arrow), FadeOut(answer), FadeOut(question),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 2: 概念定义
    # ══════════════════════════════════════════

    def scene_2_definition(self):
        title = section_title("什么是二元一次方程组？", y=6.2, size=30)
        self.play(Write(title), run_time=0.6)

        # 定义卡片
        def_bg = h_card(7.5, 2.6, COLOR_CARD, COLOR_EQ1)
        def_bg.move_to(UP * 4.5)

        def_text = Text(
            "含两个未知数，且每个方程中\n未知数次数都是 1 的方程组",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.5)

        self.play(FadeIn(def_bg), Write(def_text), run_time=0.8)

        # 方程组展示（带编号）
        sys_mob = self._make_system_mob(UP * 2.3, size=38, with_numbers=True)
        self.play(FadeIn(sys_mob, shift=UP * 0.3), run_time=0.6)

        # 特征标注
        feat1 = self._badge("两个未知数  x, y", COLOR_X)
        feat2 = self._badge("每个方程次数 = 1", COLOR_Y)
        feat3 = self._badge("两个方程必须同时成立", COLOR_RESULT)

        features = VGroup(feat1, feat2, feat3).arrange(DOWN, buff=0.35)
        features.move_to(DOWN * 0.8)

        for f in features:
            self.play(FadeIn(f, shift=RIGHT * 0.4), run_time=0.35)

        # 解的定义
        sol_bg = h_card(7.2, 1.4, COLOR_STEP_BG, COLOR_RESULT)
        sol_bg.move_to(DOWN * 3.1)
        sol_text = Text(
            "解 = 使两个方程都成立的 x, y 值",
            font=FONT, font_size=22, color=COLOR_RESULT
        ).move_to(DOWN * 3.1)

        self.play(FadeIn(sol_bg), Write(sol_text), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(def_bg), FadeOut(def_text),
            FadeOut(sys_mob), FadeOut(features),
            FadeOut(sol_bg), FadeOut(sol_text),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 3: 消元核心思想
    # ══════════════════════════════════════════

    def scene_3_elimination_idea(self):
        title = section_title("核心思路：消元", y=6.2)
        sub = Text(
            "把二元（两个未知数）化为一元（一个未知数）",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 5.2)

        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # X Y 两个大字
        x_circle = Circle(radius=0.8, fill_color=COLOR_X, fill_opacity=0.9,
                          stroke_width=0).move_to(LEFT * 2.2 + UP * 2.5)
        y_circle = Circle(radius=0.8, fill_color=COLOR_Y, fill_opacity=0.9,
                          stroke_width=0).move_to(RIGHT * 2.2 + UP * 2.5)

        x_lbl = Text("x", font=FONT, font_size=40, color=WHITE, weight=BOLD)
        x_lbl.move_to(x_circle.get_center())
        y_lbl = Text("y", font=FONT, font_size=40, color=WHITE, weight=BOLD)
        y_lbl.move_to(y_circle.get_center())

        eq_labels = Text(
            "方程组（2个未知数）",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 1.2)

        self.play(
            GrowFromCenter(x_circle), GrowFromCenter(y_circle),
            run_time=0.6
        )
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(eq_labels), run_time=0.4)

        # "消去 y" 箭头
        elim_arrow = Arrow(
            UP * 0.7, DOWN * 0.3,
            color=COLOR_HIGHLIGHT, stroke_width=4,
            max_tip_length_to_length_ratio=0.18
        )
        elim_text = Text(
            "消去  y  ！",
            font=FONT, font_size=28, color=COLOR_HIGHLIGHT, weight=BOLD
        ).move_to(RIGHT * 1.8 + UP * 0.2)

        self.play(
            y_circle.animate.set_opacity(0.15),
            y_lbl.animate.set_opacity(0.15),
            GrowArrow(elim_arrow),
            FadeIn(elim_text),
            run_time=0.8
        )

        # 剩一个未知数
        one_x = Circle(radius=0.85, fill_color=COLOR_X, fill_opacity=0.95,
                       stroke_color=COLOR_HIGHLIGHT, stroke_width=4)
        one_x.move_to(DOWN * 1.3)
        one_x_lbl = Text("x", font=FONT, font_size=42, color=WHITE, weight=BOLD)
        one_x_lbl.move_to(one_x.get_center())
        result_label = Text(
            "一元一次方程（可直接解！）",
            font=FONT, font_size=22, color=COLOR_RESULT
        ).move_to(DOWN * 2.6)

        self.play(
            GrowFromCenter(one_x), FadeIn(one_x_lbl), run_time=0.6
        )
        self.play(FadeIn(result_label, shift=UP * 0.2), run_time=0.4)

        # 两种方法说明
        methods_bg = h_card(7.2, 2.0, COLOR_STEP_BG, COLOR_HIGHLIGHT)
        methods_bg.move_to(DOWN * 4.2)
        method1 = Text("① 代入消元法", font=FONT, font_size=26, color=COLOR_EQ1, weight=BOLD)
        method2 = Text("② 加减消元法", font=FONT, font_size=26, color=COLOR_EQ2, weight=BOLD)
        methods = VGroup(method1, method2).arrange(DOWN, buff=0.4)
        methods.move_to(DOWN * 4.2)

        self.play(FadeIn(methods_bg), run_time=0.3)
        self.play(Write(method1), run_time=0.4)
        self.play(Write(method2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(x_circle), FadeOut(y_circle), FadeOut(x_lbl), FadeOut(y_lbl),
            FadeOut(eq_labels), FadeOut(elim_arrow), FadeOut(elim_text),
            FadeOut(one_x), FadeOut(one_x_lbl), FadeOut(result_label),
            FadeOut(methods_bg), FadeOut(methods),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 4: 代入消元法
    # ══════════════════════════════════════════

    def scene_4_substitution(self):
        title = section_title("代入消元法", color=COLOR_EQ1, y=6.5)
        self.play(Write(title), run_time=0.5)

        # 方程组常驻（顶部小字）
        sys_small = self._make_system_mob(UP * 5.5, size=26, with_numbers=True)
        self.play(FadeIn(sys_small), run_time=0.4)

        # ─── Step 1: 由②表示 x ───
        s1_y = 4.0
        s1_bg, s1_header = self._step_block(
            1, "由方程②，用 y 表示 x", y=s1_y, header_color=COLOR_EQ2
        )
        self.play(FadeIn(s1_bg), Write(s1_header), run_time=0.4)

        # 方程② 先高亮
        eq2_hl = MathTex(
            r"x", r"-", r"y", r"=", r"2",
            font_size=36
        )
        eq2_hl[0].set_color(COLOR_X)
        eq2_hl[2].set_color(COLOR_Y)
        eq2_hl.move_to(UP * s1_y - UP * 0.55)
        self.play(FadeIn(eq2_hl), run_time=0.3)

        arrow_derive = Arrow(
            eq2_hl.get_bottom() + DOWN * 0.1,
            eq2_hl.get_bottom() + DOWN * 0.8,
            color=COLOR_EQ2, stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        derived = MathTex(r"x = y + 2", font_size=36, color=COLOR_EQ2)
        derived.next_to(arrow_derive, DOWN, buff=0.1)

        self.play(GrowArrow(arrow_derive), run_time=0.3)
        self.play(Write(derived), run_time=0.5)
        self.wait(0.4)

        # ─── Step 2: 代入①展开 ───
        s2_y = 1.5
        s2_bg, s2_header = self._step_block(
            2, "把 x = y + 2 代入方程①", y=s2_y, header_color=COLOR_EQ1
        )
        self.play(FadeIn(s2_bg), Write(s2_header), run_time=0.4)

        sub_eq = MathTex(
            r"2(", r"y+2", r")", r"+", r"y", r"=", r"7",
            font_size=34
        )
        sub_eq[1].set_color(COLOR_EQ2)   # y+2 蓝色（来自②）
        sub_eq[4].set_color(COLOR_Y)
        sub_eq.move_to(UP * s2_y - UP * 0.55)
        self.play(Write(sub_eq), run_time=0.7)

        expand = MathTex(
            r"2y + 4 + y = 7",
            font_size=34
        )
        expand.next_to(sub_eq, DOWN, buff=0.25)
        self.play(TransformMatchingShapes(sub_eq.copy(), expand), run_time=0.6)

        # ─── Step 3: 解出 y ───
        s3_y = -1.2
        s3_bg, s3_header = self._step_block(
            3, "解一元一次方程，求 y", y=s3_y, header_color=COLOR_Y
        )
        self.play(FadeIn(s3_bg), Write(s3_header), run_time=0.4)

        collect = MathTex(r"3y = 3", font_size=34)
        collect.move_to(UP * s3_y - UP * 0.55)
        y_sol = MathTex(r"y = 1", font_size=38, color=COLOR_Y)
        y_sol.next_to(collect, DOWN, buff=0.2)

        self.play(Write(collect), run_time=0.4)
        self.play(Write(y_sol), run_time=0.5)

        # 高亮 y=1
        self.play(
            y_sol.animate.scale(1.15),
            Flash(y_sol, color=COLOR_Y, flash_radius=0.5),
            run_time=0.4
        )
        self.play(y_sol.animate.scale(1 / 1.15), run_time=0.2)

        # ─── Step 4: 回代求 x ───
        s4_y = -3.8
        s4_bg, s4_header = self._step_block(
            4, "回代 y = 1，求 x", y=s4_y, header_color=COLOR_X
        )
        self.play(FadeIn(s4_bg), Write(s4_header), run_time=0.4)

        backsub = MathTex(r"x = 1 + 2 = 3", font_size=36, color=COLOR_X)
        backsub.move_to(UP * s4_y - UP * 0.55)
        self.play(Write(backsub), run_time=0.5)

        # ─── 解框 ───
        sol_bg = h_card(6.8, 1.5, COLOR_RESULT, stroke=COLOR_RESULT)
        sol_bg.set_fill(color=COLOR_RESULT, opacity=0.18)
        sol_bg.set_stroke(color=COLOR_RESULT, width=3)
        sol_bg.move_to(DOWN * 5.5)

        sol_tex = MathTex(
            r"x = 3, \quad y = 1",
            font_size=42, color=COLOR_RESULT
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(sol_bg), Write(sol_tex), run_time=0.6)
        self.play(
            Flash(sol_tex, color=COLOR_RESULT, flash_radius=0.8),
            run_time=0.5
        )
        self.wait(1.8)

        # 全部清理
        self.play(
            FadeOut(title), FadeOut(sys_small),
            FadeOut(s1_bg), FadeOut(s1_header), FadeOut(eq2_hl),
            FadeOut(arrow_derive), FadeOut(derived),
            FadeOut(s2_bg), FadeOut(s2_header), FadeOut(sub_eq), FadeOut(expand),
            FadeOut(s3_bg), FadeOut(s3_header), FadeOut(collect), FadeOut(y_sol),
            FadeOut(s4_bg), FadeOut(s4_header), FadeOut(backsub),
            FadeOut(sol_bg), FadeOut(sol_tex),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 5: 加减消元法
    # ══════════════════════════════════════════

    def scene_5_addition_elimination(self):
        title = section_title("加减消元法", color=COLOR_EQ2, y=6.5)
        self.play(Write(title), run_time=0.5)

        # 方程组常驻（顶部小字）
        sys_small = self._make_system_mob(UP * 5.5, size=26, with_numbers=True)
        self.play(FadeIn(sys_small), run_time=0.4)

        hint = Text(
            "直接把两个方程相加，消去 y！",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.4)
        self.play(FadeIn(hint), run_time=0.4)

        # ─── 列出两个方程，准备相加 ───
        eq1_mob = MathTex(
            r"2x", r"+", r"y", r"=", r"7",
            font_size=40
        )
        eq1_mob[0].set_color(COLOR_X)
        eq1_mob[2].set_color(COLOR_Y)
        eq1_tag = Text("①", font=FONT, font_size=26, color=COLOR_EQ1)
        eq1_row = VGroup(eq1_mob, eq1_tag).arrange(RIGHT, buff=0.3)
        eq1_row.move_to(UP * 3.1)

        eq2_mob = MathTex(
            r"x", r"-", r"y", r"=", r"2",
            font_size=40
        )
        eq2_mob[0].set_color(COLOR_X)
        eq2_mob[2].set_color(COLOR_Y)
        eq2_tag = Text("②", font=FONT, font_size=26, color=COLOR_EQ2)
        eq2_row = VGroup(eq2_mob, eq2_tag).arrange(RIGHT, buff=0.3)
        eq2_row.move_to(UP * 2.0)

        plus_sign = Text("+", font=FONT, font_size=40, color=COLOR_HIGHLIGHT)
        plus_sign.next_to(eq2_row, LEFT, buff=0.3)

        # 横线
        h_line = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_A, stroke_width=2)
        h_line.move_to(UP * 1.2)

        self.play(FadeIn(eq1_row), run_time=0.4)
        self.play(FadeIn(eq2_row), FadeIn(plus_sign), run_time=0.4)
        self.play(Create(h_line), run_time=0.3)

        # y 和 -y 高亮并消去
        y_pos = eq1_mob[2]   # +y in eq1
        neg_y_pos = eq2_mob[2]  # -y in eq2

        self.play(
            y_pos.animate.set_color(COLOR_HIGHLIGHT),
            neg_y_pos.animate.set_color(COLOR_HIGHLIGHT),
            run_time=0.4
        )

        cancel_line1 = Line(
            y_pos.get_left() + LEFT * 0.05,
            y_pos.get_right() + RIGHT * 0.05,
            color="#e74c3c", stroke_width=4
        )
        cancel_line2 = Line(
            neg_y_pos.get_left() + LEFT * 0.05,
            neg_y_pos.get_right() + RIGHT * 0.05,
            color="#e74c3c", stroke_width=4
        )
        elim_tip = Text("互相抵消！", font=FONT, font_size=22, color="#e74c3c")
        elim_tip.next_to(h_line, RIGHT, buff=0.3)

        self.play(
            Create(cancel_line1), Create(cancel_line2),
            FadeIn(elim_tip),
            run_time=0.5
        )
        self.wait(0.4)

        # ─── 结果：3x = 9 ───
        result_eq = MathTex(r"3x = 9", font_size=46)
        result_eq[0][:2].set_color(COLOR_X)
        result_eq.move_to(UP * 0.3)

        self.play(Write(result_eq), run_time=0.6)

        arrow_x = Arrow(
            result_eq.get_bottom() + DOWN * 0.05,
            result_eq.get_bottom() + DOWN * 0.8,
            color=COLOR_X, stroke_width=3,
            max_tip_length_to_length_ratio=0.22
        )
        x_sol = MathTex(r"x = 3", font_size=44, color=COLOR_X)
        x_sol.next_to(arrow_x, DOWN, buff=0.1)

        self.play(GrowArrow(arrow_x), run_time=0.3)
        self.play(Write(x_sol), run_time=0.5)
        self.play(
            Flash(x_sol, color=COLOR_X, flash_radius=0.5),
            run_time=0.4
        )

        # ─── 回代求 y ───
        backsub_title = Text(
            "把 x = 3 代入方程①",
            font=FONT, font_size=24, color=COLOR_EQ1
        ).move_to(DOWN * 2.0)

        back_eq = MathTex(
            r"2(3) + y = 7",
            font_size=38
        )
        back_eq.move_to(DOWN * 2.9)

        simp_eq = MathTex(r"6 + y = 7", font_size=38)
        simp_eq.next_to(back_eq, DOWN, buff=0.2)

        y_sol = MathTex(r"y = 1", font_size=44, color=COLOR_Y)
        y_sol.next_to(simp_eq, DOWN, buff=0.2)

        self.play(FadeIn(backsub_title), run_time=0.3)
        self.play(Write(back_eq), run_time=0.5)
        self.play(TransformMatchingShapes(back_eq.copy(), simp_eq), run_time=0.5)
        self.play(Write(y_sol), run_time=0.5)
        self.play(Flash(y_sol, color=COLOR_Y, flash_radius=0.5), run_time=0.4)

        # ─── 解框 ───
        sol_bg = RoundedRectangle(
            width=6.5, height=1.5, corner_radius=0.3,
            fill_color=COLOR_RESULT, fill_opacity=0.15,
            stroke_color=COLOR_RESULT, stroke_width=3
        ).move_to(DOWN * 5.5)

        sol_tex = MathTex(
            r"x = 3, \quad y = 1",
            font_size=42, color=COLOR_RESULT
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(sol_bg), Write(sol_tex), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(sys_small), FadeOut(hint),
            FadeOut(eq1_row), FadeOut(eq2_row), FadeOut(plus_sign), FadeOut(h_line),
            FadeOut(cancel_line1), FadeOut(cancel_line2), FadeOut(elim_tip),
            FadeOut(result_eq), FadeOut(arrow_x), FadeOut(x_sol),
            FadeOut(backsub_title), FadeOut(back_eq), FadeOut(simp_eq), FadeOut(y_sol),
            FadeOut(sol_bg), FadeOut(sol_tex),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 6: 验证 + 片尾
    # ══════════════════════════════════════════

    def scene_6_verify_outro(self):
        # ── 验证区 ──
        title = section_title("验证答案", color=COLOR_HIGHLIGHT, y=6.5)
        self.play(Write(title), run_time=0.5)

        sol_display = MathTex(
            r"x = 3, \quad y = 1",
            font_size=40, color=COLOR_RESULT
        ).move_to(UP * 5.4)
        self.play(Write(sol_display), run_time=0.5)

        check_label = Text(
            "代入两个方程，都成立则正确！",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.4)
        self.play(FadeIn(check_label), run_time=0.4)

        # 验证方程①
        v1_bg = h_card(7.2, 1.8, COLOR_STEP_BG, COLOR_EQ1)
        v1_bg.move_to(UP * 3.1)
        v1_title = Text("验证方程①", font=FONT, font_size=22, color=COLOR_EQ1)
        v1_title.move_to(UP * 3.65)

        v1_tex = MathTex(
            r"2(3) + 1 = 6 + 1 = 7", r"\quad \checkmark",
            font_size=34
        )
        v1_tex[1].set_color(COLOR_RESULT)
        v1_tex.move_to(UP * 2.85)

        self.play(FadeIn(v1_bg), Write(v1_title), run_time=0.3)
        self.play(Write(v1_tex), run_time=0.6)

        # 验证方程②
        v2_bg = h_card(7.2, 1.8, COLOR_STEP_BG, COLOR_EQ2)
        v2_bg.move_to(UP * 1.4)
        v2_title = Text("验证方程②", font=FONT, font_size=22, color=COLOR_EQ2)
        v2_title.move_to(UP * 1.95)

        v2_tex = MathTex(
            r"3 - 1 = 2", r"\quad \checkmark",
            font_size=34
        )
        v2_tex[1].set_color(COLOR_RESULT)
        v2_tex.move_to(UP * 1.15)

        self.play(FadeIn(v2_bg), Write(v2_title), run_time=0.3)
        self.play(Write(v2_tex), run_time=0.5)

        # 结论
        conclude_bg = h_card(7.0, 1.6, COLOR_RESULT, COLOR_RESULT)
        conclude_bg.set_fill(opacity=0.2)
        conclude_bg.move_to(DOWN * 0.3)

        conclude_label = Text("两个方程都满足！", font=FONT, font_size=26, color=WHITE, weight=BOLD)
        conclude_formula = MathTex(r"\therefore \; x = 3, \quad y = 1", font_size=36, color=COLOR_RESULT)
        conclude_group = VGroup(conclude_label, conclude_formula).arrange(DOWN, buff=0.2)
        conclude_group.move_to(DOWN * 0.3)

        self.play(FadeIn(conclude_bg), run_time=0.3)
        self.play(Write(conclude_label), Write(conclude_formula), run_time=0.6)
        self.play(
            Flash(conclude_formula, color=COLOR_RESULT, flash_radius=1.0),
            run_time=0.5
        )
        self.wait(1.0)

        # ── 口诀总结 ──
        summary_bg = h_card(7.5, 3.5, COLOR_CARD, COLOR_HIGHLIGHT)
        summary_bg.move_to(DOWN * 3.5)

        sum_title = Text("解题步骤", font=FONT, font_size=26, color=COLOR_HIGHLIGHT, weight=BOLD)
        sum1 = Text("① 选较简单的方程，表示一个未知数", font=FONT, font_size=19, color=GRAY_A)
        sum2 = Text("② 代入另一个方程，消去一个未知数", font=FONT, font_size=19, color=GRAY_A)
        sum3 = Text("③ 解一元一次方程，求出一个未知数", font=FONT, font_size=19, color=GRAY_A)
        sum4 = Text("④ 回代，求另一个未知数", font=FONT, font_size=19, color=GRAY_A)

        summary_content = VGroup(sum_title, sum1, sum2, sum3, sum4).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        summary_content.move_to(DOWN * 3.5)

        self.play(FadeIn(summary_bg), run_time=0.3)
        for item in summary_content:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.25)
        self.wait(1.5)

        # 清理，显示片尾
        self.play(
            FadeOut(title), FadeOut(sol_display), FadeOut(check_label),
            FadeOut(v1_bg), FadeOut(v1_title), FadeOut(v1_tex),
            FadeOut(v2_bg), FadeOut(v2_title), FadeOut(v2_tex),
            FadeOut(conclude_bg), FadeOut(conclude_group),
            FadeOut(summary_bg), FadeOut(summary_content),
            run_time=0.5
        )

        # ── 片尾 ──
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE, weight=BOLD
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.5)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.7)

        # 小装饰：两个方程变成飘散的粒子效果（用Dot模拟）
        dots = VGroup(*[
            Dot(
                np.array([
                    np.cos(i * TAU / 8) * 2.5,
                    np.sin(i * TAU / 8) * 2.5 - 2.5,
                    0
                ]),
                radius=0.08,
                color=[COLOR_EQ1, COLOR_EQ2, COLOR_X, COLOR_Y][i % 4],
                fill_opacity=0.8
            )
            for i in range(8)
        ])

        self.play(
            Transform(self.author, author_big),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=0.7
        )
        self.play(FadeIn(follow, scale=1.08), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.08), run_time=0.6)
        self.play(Rotate(dots, angle=TAU / 4, about_point=DOWN * 2.5), run_time=1.2)
        self.wait(1.0)

        self.play(FadeOut(self.author), FadeOut(author_id), FadeOut(follow), FadeOut(dots), run_time=1.0)

    # ══════════════════════════════════════════
    # 辅助方法
    # ══════════════════════════════════════════

    def _make_system_mob(self, pos, size=38, with_numbers=False):
        """生成带大括号的方程组"""
        eq1 = MathTex(r"2x + y = 7", font_size=size)
        eq1[0][0:2].set_color(COLOR_X)   # 2x
        eq1[0][3].set_color(COLOR_Y)     # y

        eq2 = MathTex(r"x - y = 2", font_size=size)
        eq2[0][0].set_color(COLOR_X)     # x
        eq2[0][2].set_color(COLOR_Y)     # y

        if with_numbers:
            tag1 = Text("①", font=FONT, font_size=int(size * 0.7), color=COLOR_EQ1)
            tag2 = Text("②", font=FONT, font_size=int(size * 0.7), color=COLOR_EQ2)
            row1 = VGroup(eq1, tag1).arrange(RIGHT, buff=0.25)
            row2 = VGroup(eq2, tag2).arrange(RIGHT, buff=0.25)
        else:
            row1, row2 = eq1, eq2

        rows = VGroup(row1, row2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        brace = MathTex(r"\left\{", font_size=int(size * 1.6), color=WHITE)
        brace.next_to(rows, LEFT, buff=0.08)

        return VGroup(brace, rows).move_to(pos)

    def _step_block(self, n, text, y, header_color=WHITE):
        """生成步骤块（背景 + 标题文字）"""
        bg = h_card(7.5, 2.0, COLOR_STEP_BG, header_color)
        bg.move_to(UP * y)

        num = Text(f"Step {n}", font=FONT, font_size=18,
                   color=header_color, weight=BOLD)
        content = Text(text, font=FONT, font_size=22, color=WHITE)
        header = VGroup(num, content).arrange(RIGHT, buff=0.25)
        header.move_to(UP * y + UP * 0.62)

        return bg, header

    def _badge(self, text, color):
        """小徽章标注"""
        bg = RoundedRectangle(
            width=6.5, height=0.65, corner_radius=0.2,
            fill_color=color, fill_opacity=0.18,
            stroke_color=color, stroke_width=1.5
        )
        label = Text(text, font=FONT, font_size=22, color=color)
        return VGroup(bg, label)
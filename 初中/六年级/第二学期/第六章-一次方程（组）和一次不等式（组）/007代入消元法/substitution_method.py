"""
代入消元法 - Manim 教学动画
六年级 第二学期 第六章

内容: 代入消元法详细步骤拆解
目标观众: 六年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

例题:
    2x + y = 8   ..①
    x  - y = 1   ..②
    解: x=3, y=2

核心动画亮点:
    "代入"过程可视化 — 用高亮矩形框把 (y+1) 从②物理移动到①中 x 的位置

渲染命令:
    manim -pql substitution_method.py SubstitutionMethod   # 预览
    manim -qh  substitution_method.py SubstitutionMethod   # 高质量
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# TikTok 竖屏全局配置
# ─────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────
# 颜色系统
# ─────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
COLOR_EQ1       = "#e74c3c"   # 红  — 方程①
COLOR_EQ2       = "#3498db"   # 蓝  — 方程②
COLOR_X         = "#f39c12"   # 橙  — x 变量
COLOR_Y         = "#9b59b6"   # 紫  — y 变量
COLOR_SUBST     = "#1abc9c"   # 青绿 — 代入块（来自②的 y+1）
COLOR_RESULT    = "#2ecc71"   # 绿  — 最终解
COLOR_HIGHLIGHT = YELLOW
COLOR_CARD      = "#0f3460"   # 步骤卡片背景
COLOR_DARK      = "#16213e"   # 深色背景
FONT            = "Noto Sans CJK SC"


# ─────────────────────────────────────────────
# 工具函数
# ─────────────────────────────────────────────

def rounded_card(w=7.5, h=1.8, fill=COLOR_CARD, stroke=None, r=0.28):
    return RoundedRectangle(
        width=w, height=h, corner_radius=r,
        fill_color=fill, fill_opacity=1,
        stroke_color=stroke or fill,
        stroke_width=0 if stroke is None else 2,
    )


def section_title(text, color=COLOR_HIGHLIGHT, size=32, y=6.3):
    return Text(text, font=FONT, font_size=size, color=color,
                weight=BOLD).move_to(UP * y)


def step_num_badge(n, color=WHITE, size=22):
    bg = Circle(radius=0.28, fill_color=color, fill_opacity=1,
                stroke_width=0)
    num = Text(str(n), font=FONT, font_size=size,
               color=BG_COLOR, weight=BOLD)
    num.move_to(bg.get_center())
    return VGroup(bg, num)


# ─────────────────────────────────────────────
# 主场景
# ─────────────────────────────────────────────

class SubstitutionMethod(Scene):
    """
    代入消元法 详细教学动画

    场景顺序:
      1. 开场钩子
      2. 四步骤概览
      3. Step 1 — 由②表示 x
      4. Step 2 — 代入①（核心可视化）
      5. Step 3 — 展开化简，求 y
      6. Step 4 — 回代求 x，写出解
      7. 验证 + 口诀 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_step1_express()
        self.scene_4_step2_substitute()
        self.scene_5_step3_solve_y()
        self.scene_6_step4_backsubstitute()
        self.scene_7_verify_outro()

    # ══════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════

    def scene_1_opening(self):
        # 作者常驻
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 大标题
        title = Text("代入消元法", font=FONT, font_size=52,
                     color=WHITE, weight=BOLD).move_to(UP * 5.7)
        subtitle = Text("用「替换」消去一个未知数",
                        font=FONT, font_size=28,
                        color=COLOR_HIGHLIGHT).move_to(UP * 4.6)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.4)

        # 方程组钩子
        sys_hook = self._system_mob(UP * 3.0, size=38, numbered=True)
        self.play(FadeIn(sys_hook, shift=UP * 0.4, scale=0.92), run_time=0.6)

        # 问号
        question = Text("这个方程组你会解吗？",
                        font=FONT, font_size=26, color=COLOR_HIGHLIGHT
                        ).move_to(UP * 1.0)
        self.play(FadeIn(question, scale=1.05), run_time=0.4)

        # 快速预览答案
        arrow = Arrow(UP * 0.2, DOWN * 0.5,
                      color=COLOR_RESULT, stroke_width=3,
                      max_tip_length_to_length_ratio=0.2)
        answer = MathTex(r"x = 3,\quad y = 2",
                         font_size=42, color=COLOR_RESULT).move_to(DOWN * 1.0)
        self.play(GrowArrow(arrow), run_time=0.3)
        self.play(Write(answer), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(sys_hook),
            FadeOut(question), FadeOut(arrow), FadeOut(answer),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 2: 四步骤概览
    # ══════════════════════════════════════════

    def scene_2_overview(self):
        title = section_title("代入消元法  ·  四步走", y=6.4, size=30)
        self.play(Write(title), run_time=0.5)

        steps = [
            (1, "从一个方程表示一个未知数",   COLOR_EQ2),
            (2, "把该式代入另一个方程",       COLOR_SUBST),
            (3, "解一元一次方程，求出一个未知数", COLOR_Y),
            (4, "回代，求另一个未知数",       COLOR_X),
        ]

        cards = VGroup()
        y_start = 4.9
        for i, (n, text, color) in enumerate(steps):
            bg = rounded_card(7.5, 1.55, COLOR_CARD, color)
            badge = step_num_badge(n, color)
            label = Text(text, font=FONT, font_size=22, color=WHITE)
            row = VGroup(badge, label).arrange(RIGHT, buff=0.35)
            card = VGroup(bg, row)
            card.move_to(UP * (y_start - i * 1.8))
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.3)

        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(cards), run_time=0.4)

    # ══════════════════════════════════════════
    # Scene 3: Step 1 — 由②表示 x
    # ══════════════════════════════════════════

    def scene_3_step1_express(self):
        title = section_title("Step 1  由方程②表示  x", color=COLOR_EQ2, y=6.4, size=28)
        self.play(Write(title), run_time=0.4)

        # 小方程组（常驻顶部）
        self.sys_small = self._system_mob(UP * 5.5, size=24, numbered=True)
        self.play(FadeIn(self.sys_small), run_time=0.4)

        hint = Text("选较简单的方程，移项变形",
                    font=FONT, font_size=23, color=GRAY_A).move_to(UP * 4.4)
        self.play(FadeIn(hint), run_time=0.3)

        # 展示方程②（大号）
        eq2_big = MathTex(r"x", r"-", r"y", r"=", r"1", font_size=46)
        eq2_big[0].set_color(COLOR_X)
        eq2_big[2].set_color(COLOR_Y)
        tag2 = Text("②", font=FONT, font_size=28, color=COLOR_EQ2)
        eq2_row = VGroup(eq2_big, tag2).arrange(RIGHT, buff=0.4).move_to(UP * 3.0)

        # 高亮框包住方程②
        hl_rect = SurroundingRectangle(eq2_row, color=COLOR_EQ2,
                                       stroke_width=2.5, buff=0.12)

        self.play(FadeIn(eq2_row), run_time=0.4)
        self.play(Create(hl_rect), run_time=0.35)

        # 移项箭头
        move_arrow = Arrow(eq2_row.get_bottom() + DOWN * 0.1,
                           eq2_row.get_bottom() + DOWN * 0.9,
                           color=COLOR_EQ2, stroke_width=3,
                           max_tip_length_to_length_ratio=0.22)
        move_tip = Text("移项：把 -y 移到右边",
                        font=FONT, font_size=21, color=GRAY_A
                        ).next_to(move_arrow, RIGHT, buff=0.15)
        self.play(GrowArrow(move_arrow), FadeIn(move_tip), run_time=0.4)

        # 结果：x = y + 1
        expr_x = MathTex(r"x", r"=", r"y", r"+", r"1", font_size=50)
        expr_x[0].set_color(COLOR_X)
        expr_x[2].set_color(COLOR_Y)
        # 把 y+1 部分的颜色改为 SUBST
        expr_x[2].set_color(COLOR_SUBST)
        expr_x[4].set_color(COLOR_SUBST)

        self.expr_x = expr_x   # 保存给 Scene 4 使用
        expr_x.move_to(UP * 1.1)

        self.play(Write(expr_x), run_time=0.6)

        # 圆角矩形高亮"y+1"部分
        yp1_group = VGroup(expr_x[2], expr_x[3], expr_x[4])
        self.subst_box = SurroundingRectangle(
            yp1_group, color=COLOR_SUBST,
            stroke_width=3, buff=0.1,
        )
        self.subst_box.set_fill(color=COLOR_SUBST, opacity=0.12)

        box_label = Text("这是 x 的表达式",
                         font=FONT, font_size=21, color=COLOR_SUBST
                         ).next_to(self.subst_box, DOWN, buff=0.2)

        self.play(Create(self.subst_box), run_time=0.4)
        self.play(FadeIn(box_label), run_time=0.3)
        self.wait(1.2)

        # 清理（保留 sys_small、expr_x、subst_box）
        self.play(
            FadeOut(title), FadeOut(hint), FadeOut(eq2_row), FadeOut(hl_rect),
            FadeOut(move_arrow), FadeOut(move_tip), FadeOut(box_label),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 4: Step 2 — 代入（核心可视化）
    # ══════════════════════════════════════════

    def scene_4_step2_substitute(self):
        title = section_title("Step 2  把  x = y+1  代入方程①",
                              color=COLOR_SUBST, y=6.4, size=26)
        self.play(Write(title), run_time=0.4)

        # 展示方程①（大号），x 用橙色
        eq1_display = MathTex(
            r"2", r"x", r"+", r"y", r"=", r"8",
            font_size=46,
        )
        eq1_display[0].set_color(COLOR_X)
        eq1_display[1].set_color(COLOR_X)
        eq1_display[3].set_color(COLOR_Y)
        tag1 = Text("①", font=FONT, font_size=28, color=COLOR_EQ1)
        eq1_row = VGroup(eq1_display, tag1).arrange(RIGHT, buff=0.4).move_to(UP * 4.5)

        hl1 = SurroundingRectangle(eq1_row, color=COLOR_EQ1,
                                   stroke_width=2.5, buff=0.12)

        self.play(FadeIn(eq1_row), Create(hl1), run_time=0.5)

        # 方框圈住方程①中的 "x"
        x_in_eq1 = eq1_display[1]
        x_frame = SurroundingRectangle(
            x_in_eq1, color=COLOR_SUBST,
            stroke_width=3, buff=0.08,
        )
        x_frame.set_fill(color=COLOR_SUBST, opacity=0.18)

        replace_tip = Text("把这里的 x 替换为 (y+1)",
                           font=FONT, font_size=21, color=COLOR_SUBST
                           ).move_to(UP * 3.3)

        self.play(Create(x_frame), run_time=0.35)
        self.play(FadeIn(replace_tip), run_time=0.3)
        self.wait(0.5)

        # ── 核心动画：subst_box（来自上一场景）飞向 x 的位置 ──
        # 先把 expr_x 和 subst_box 移到屏幕中间方便看
        expr_ref = self.expr_x.copy()   # 备份用于动画
        subst_ref = self.subst_box.copy()

        self.play(
            self.expr_x.animate.move_to(UP * 2.3).scale(0.9),
            self.subst_box.animate.move_to(UP * 2.3).scale(0.9),
            run_time=0.4,
        )

        # 把 subst_box 缩小并飞向 eq1 中 x 的位置
        target_pos = x_in_eq1.get_center()
        flying_box = self.subst_box.copy()
        self.play(
            flying_box.animate
                .scale(0.55)
                .move_to(target_pos),
            run_time=0.7,
            rate_func=smooth,
        )
        self.play(FadeOut(flying_box), FadeOut(x_frame), run_time=0.2)

        # 写出替换后的方程
        after_sub = MathTex(
            r"2(", r"y+1", r")", r"+", r"y", r"=", r"8",
            font_size=44,
        )
        after_sub[1].set_color(COLOR_SUBST)    # y+1 青绿色
        after_sub[4].set_color(COLOR_Y)        # y 紫色
        after_sub_tag = Text("代入后", font=FONT, font_size=22, color=GRAY_A)
        after_sub_grp = VGroup(after_sub, after_sub_tag).arrange(RIGHT, buff=0.3)
        after_sub_grp.move_to(UP * 1.0)

        self.play(Write(after_sub), FadeIn(after_sub_tag), run_time=0.7)

        # 高亮 y+1 部分
        sub_hl = SurroundingRectangle(
            after_sub[1], color=COLOR_SUBST,
            stroke_width=2.5, buff=0.07,
        )
        sub_hl.set_fill(color=COLOR_SUBST, opacity=0.15)
        self.play(Create(sub_hl), run_time=0.3)

        success_tip = Text("x 已被消去！现在只有 y 了",
                           font=FONT, font_size=24, color=COLOR_RESULT,
                           weight=BOLD).move_to(DOWN * 0.3)
        self.play(FadeIn(success_tip, scale=1.05), run_time=0.4)
        self.wait(1.2)

        # 保存 after_sub 给下一 scene
        self.after_sub_mob = after_sub.copy()

        self.play(
            FadeOut(title), FadeOut(eq1_row), FadeOut(hl1),
            FadeOut(replace_tip),
            FadeOut(self.expr_x), FadeOut(self.subst_box),
            FadeOut(after_sub_grp), FadeOut(sub_hl),
            FadeOut(success_tip),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 5: Step 3 — 展开化简，求 y
    # ══════════════════════════════════════════

    def scene_5_step3_solve_y(self):
        title = section_title("Step 3  展开化简，求  y",
                              color=COLOR_Y, y=6.4, size=28)
        self.play(Write(title), run_time=0.4)

        # 出发方程
        line0 = MathTex(r"2(y+1)+y=8", font_size=40)
        line0[0][1:4].set_color(COLOR_SUBST)    # y+1
        line0[0][5].set_color(COLOR_Y)          # y
        line0.move_to(UP * 5.0)
        self.play(FadeIn(line0, shift=DOWN * 0.2), run_time=0.4)

        # ── 展开：2y+2+y=8 ──
        arrow1 = self._down_arrow(UP * 4.35, color=GRAY_B)
        tip1 = Text("展开括号", font=FONT, font_size=20, color=GRAY_A
                    ).next_to(arrow1, RIGHT, buff=0.2)

        line1 = MathTex(r"2y", r"+", r"2", r"+", r"y", r"=", r"8", font_size=40)
        line1[0].set_color(COLOR_Y)
        line1[4].set_color(COLOR_Y)
        line1.move_to(UP * 3.7)

        self.play(GrowArrow(arrow1), FadeIn(tip1), run_time=0.3)
        self.play(TransformMatchingShapes(line0.copy(), line1), run_time=0.6)

        # ── 合并：3y+2=8 ──
        arrow2 = self._down_arrow(UP * 3.05, color=GRAY_B)
        tip2 = Text("合并同类项", font=FONT, font_size=20, color=GRAY_A
                    ).next_to(arrow2, RIGHT, buff=0.2)

        line2 = MathTex(r"3y", r"+", r"2", r"=", r"8", font_size=40)
        line2[0].set_color(COLOR_Y)
        line2.move_to(UP * 2.4)

        self.play(GrowArrow(arrow2), FadeIn(tip2), run_time=0.3)
        self.play(TransformMatchingShapes(line1.copy(), line2), run_time=0.6)

        # ── 移项：3y=6 ──
        arrow3 = self._down_arrow(UP * 1.75, color=GRAY_B)
        tip3 = Text("移项", font=FONT, font_size=20, color=GRAY_A
                    ).next_to(arrow3, RIGHT, buff=0.2)

        line3 = MathTex(r"3y", r"=", r"6", font_size=40)
        line3[0].set_color(COLOR_Y)
        line3.move_to(UP * 1.1)

        self.play(GrowArrow(arrow3), FadeIn(tip3), run_time=0.3)
        self.play(TransformMatchingShapes(line2.copy(), line3), run_time=0.6)

        # ── 两边除以3：y=2 ──
        arrow4 = self._down_arrow(UP * 0.45, color=COLOR_Y)
        tip4 = Text("两边 ÷ 3", font=FONT, font_size=20, color=GRAY_A
                    ).next_to(arrow4, RIGHT, buff=0.2)

        y_result = MathTex(r"y = 2", font_size=52, color=COLOR_Y)
        y_result.move_to(DOWN * 0.25)
        self.play(GrowArrow(arrow4), FadeIn(tip4), run_time=0.3)
        self.play(Write(y_result), run_time=0.5)

        # 高亮解
        y_box = SurroundingRectangle(y_result, color=COLOR_Y,
                                     stroke_width=3, buff=0.15)
        y_box.set_fill(color=COLOR_Y, opacity=0.12)
        self.play(Create(y_box), Flash(y_result, color=COLOR_Y, flash_radius=0.6),
                  run_time=0.45)
        self.wait(1.0)

        # 保存 y_result 供下一场景
        self.y_result_copy = y_result.copy()

        self.play(
            FadeOut(title),
            FadeOut(line0), FadeOut(arrow1), FadeOut(tip1),
            FadeOut(line1), FadeOut(arrow2), FadeOut(tip2),
            FadeOut(line2), FadeOut(arrow3), FadeOut(tip3),
            FadeOut(line3), FadeOut(arrow4), FadeOut(tip4),
            FadeOut(y_result), FadeOut(y_box),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 6: Step 4 — 回代求 x，写出解
    # ══════════════════════════════════════════

    def scene_6_step4_backsubstitute(self):
        title = section_title("Step 4  回代  y = 2，求  x",
                              color=COLOR_X, y=6.4, size=28)
        self.play(Write(title), run_time=0.4)

        # 已知：x = y + 1，把 y=2 代回
        known_expr = MathTex(r"x", r"=", r"y", r"+", r"1", font_size=44)
        known_expr[0].set_color(COLOR_X)
        known_expr[2].set_color(COLOR_Y)
        known_tag = Text("（由 Step 1 得）", font=FONT, font_size=20, color=GRAY_A)
        known_row = VGroup(known_expr, known_tag).arrange(RIGHT, buff=0.3)
        known_row.move_to(UP * 5.0)
        self.play(FadeIn(known_row, shift=DOWN * 0.2), run_time=0.4)

        # y=2 重新出现
        y_val = MathTex(r"y = 2", font_size=40, color=COLOR_Y).move_to(UP * 3.8)
        y_val_box = SurroundingRectangle(y_val, color=COLOR_Y,
                                         stroke_width=2.5, buff=0.1)
        y_val_box.set_fill(color=COLOR_Y, opacity=0.1)
        self.play(FadeIn(y_val), Create(y_val_box), run_time=0.4)

        # 代入箭头
        sub_arrow = Arrow(UP * 3.25, UP * 2.5,
                          color=COLOR_X, stroke_width=3,
                          max_tip_length_to_length_ratio=0.22)
        sub_label = Text("把 y = 2 代入", font=FONT, font_size=21, color=GRAY_A
                         ).next_to(sub_arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(sub_arrow), FadeIn(sub_label), run_time=0.4)

        # x = 2 + 1
        x_calc = MathTex(r"x", r"=", r"2", r"+", r"1", font_size=46)
        x_calc[0].set_color(COLOR_X)
        x_calc[2].set_color(COLOR_Y)    # 2（来自y=2）
        x_calc.move_to(UP * 1.8)
        self.play(Write(x_calc), run_time=0.5)

        # x = 3
        arrow_x = self._down_arrow(UP * 1.05, color=COLOR_X)
        x_result = MathTex(r"x = 3", font_size=52, color=COLOR_X)
        x_result.move_to(UP * 0.3)
        self.play(GrowArrow(arrow_x), run_time=0.3)
        self.play(Write(x_result), run_time=0.5)
        self.play(Flash(x_result, color=COLOR_X, flash_radius=0.6), run_time=0.4)

        # ── 解框 ──
        sol_bg = RoundedRectangle(
            width=7.0, height=1.8,
            fill_color=COLOR_RESULT, fill_opacity=0.12,
            stroke_color=COLOR_RESULT, stroke_width=3,
        ).move_to(DOWN * 1.5)

        sol_label = Text("方程组的解", font=FONT, font_size=22, color=GRAY_A)
        sol_tex = MathTex(r"x = 3,\quad y = 2", font_size=46, color=COLOR_RESULT)
        sol_content = VGroup(sol_label, sol_tex).arrange(DOWN, buff=0.15)
        sol_content.move_to(DOWN * 1.5)

        self.play(FadeIn(sol_bg), run_time=0.3)
        self.play(Write(sol_label), Write(sol_tex), run_time=0.6)
        self.play(
            Flash(sol_tex, color=COLOR_RESULT, flash_radius=1.0),
            run_time=0.5,
        )

        # 结论
        conclude = MathTex(
            r"\therefore\; x = 3,\; y = 2",
            font_size=40, color=COLOR_RESULT,
        ).move_to(DOWN * 3.2)
        self.play(Write(conclude), run_time=0.5)
        self.wait(1.5)

        # 保存到类属性供下一场景
        self.sol_bg      = sol_bg
        self.sol_content = sol_content
        self.conclude    = conclude

        self.play(
            FadeOut(title),
            FadeOut(known_row),
            FadeOut(y_val), FadeOut(y_val_box),
            FadeOut(sub_arrow), FadeOut(sub_label),
            FadeOut(x_calc), FadeOut(arrow_x), FadeOut(x_result),
            FadeOut(sol_bg), FadeOut(sol_content), FadeOut(conclude),
            run_time=0.4,
        )

    # ══════════════════════════════════════════
    # Scene 7: 验证 + 口诀 + 片尾
    # ══════════════════════════════════════════

    def scene_7_verify_outro(self):
        # ── 验证 ──
        title = section_title("验证答案", y=6.5, size=30)
        self.play(Write(title), run_time=0.4)

        sol_remind = MathTex(r"x = 3,\quad y = 2",
                             font_size=38, color=COLOR_RESULT).move_to(UP * 5.5)
        self.play(Write(sol_remind), run_time=0.4)

        prompt = Text("代入两个方程，验证都成立",
                      font=FONT, font_size=23, color=GRAY_A).move_to(UP * 4.5)
        self.play(FadeIn(prompt), run_time=0.3)

        # 验证方程①
        v1_bg = rounded_card(7.4, 1.8, COLOR_DARK, COLOR_EQ1)
        v1_bg.move_to(UP * 3.2)
        v1_head = Text("验证方程①  2x + y = 8",
                       font=FONT, font_size=21, color=COLOR_EQ1).move_to(UP * 3.75)
        v1_body = MathTex(r"2(3) + 2 = 6 + 2 = 8", r"\;\checkmark",
                          font_size=34)
        v1_body[1].set_color(COLOR_RESULT)
        v1_body.move_to(UP * 2.95)
        self.play(FadeIn(v1_bg), Write(v1_head), run_time=0.3)
        self.play(Write(v1_body), run_time=0.5)

        # 验证方程②
        v2_bg = rounded_card(7.4, 1.8, COLOR_DARK, COLOR_EQ2)
        v2_bg.move_to(UP * 1.5)
        v2_head = Text("验证方程②  x - y = 1",
                       font=FONT, font_size=21, color=COLOR_EQ2).move_to(UP * 2.05)
        v2_body = MathTex(r"3 - 2 = 1", r"\;\checkmark", font_size=34)
        v2_body[1].set_color(COLOR_RESULT)
        v2_body.move_to(UP * 1.25)
        self.play(FadeIn(v2_bg), Write(v2_head), run_time=0.3)
        self.play(Write(v2_body), run_time=0.4)

        # 结论感叹
        conclude_box = rounded_card(6.8, 1.3, COLOR_RESULT, COLOR_RESULT)
        conclude_box.set_fill(opacity=0.18)
        conclude_box.move_to(DOWN * 0.15)
        conclude_txt = Text("两个方程都成立！答案正确 ✓",
                            font=FONT, font_size=25, color=WHITE,
                            weight=BOLD).move_to(DOWN * 0.15)
        self.play(FadeIn(conclude_box), Write(conclude_txt), run_time=0.5)
        self.wait(0.8)

        # ── 口诀总结 ──
        motto_bg = rounded_card(7.5, 3.8, COLOR_CARD, COLOR_HIGHLIGHT)
        motto_bg.move_to(DOWN * 3.2)

        motto_title = Text("代入消元法  四步口诀",
                           font=FONT, font_size=24, color=COLOR_HIGHLIGHT,
                           weight=BOLD).move_to(DOWN * 1.8)

        mottos = VGroup(
            self._motto_line("① 由简单方程，表示一个未知数", COLOR_EQ2),
            self._motto_line("② 代入另一方程，消去该未知数", COLOR_SUBST),
            self._motto_line("③ 解一元方程，求出一个值",    COLOR_Y),
            self._motto_line("④ 回代，求另一个未知数",      COLOR_X),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        mottos.move_to(DOWN * 3.35)

        self.play(FadeIn(motto_bg), Write(motto_title), run_time=0.4)
        for m in mottos:
            self.play(FadeIn(m, shift=RIGHT * 0.3), run_time=0.25)
        self.wait(1.2)

        # 清理所有内容
        self.play(
            FadeOut(title), FadeOut(sol_remind), FadeOut(prompt),
            FadeOut(v1_bg), FadeOut(v1_head), FadeOut(v1_body),
            FadeOut(v2_bg), FadeOut(v2_head), FadeOut(v2_body),
            FadeOut(conclude_box), FadeOut(conclude_txt),
            FadeOut(motto_bg), FadeOut(motto_title), FadeOut(mottos),
            FadeOut(self.sys_small),
            run_time=0.5,
        )

        # ── 片尾 ──
        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=38, color=WHITE,
                          weight=BOLD).move_to(UP * 1.5)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=28, color=GRAY_B).move_to(UP * 0.5)
        follow     = Text("关注我，获得更多数学技巧！",
                          font=FONT, font_size=28, color=COLOR_HIGHLIGHT
                          ).move_to(DOWN * 0.7)

        # 装饰：四色小圆点环绕
        orbit_dots = VGroup(*[
            Dot(
                np.array([np.cos(i * TAU / 8) * 2.2,
                          np.sin(i * TAU / 8) * 2.2 - 2.5, 0]),
                radius=0.09,
                color=[COLOR_EQ1, COLOR_EQ2, COLOR_X, COLOR_Y,
                       COLOR_SUBST, COLOR_RESULT, COLOR_HIGHLIGHT, WHITE][i],
                fill_opacity=0.85,
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
            LaggedStart(*[FadeIn(d, scale=0.5) for d in orbit_dots], lag_ratio=0.07),
            run_time=0.5,
        )
        self.play(Rotate(orbit_dots, angle=TAU / 3,
                         about_point=DOWN * 2.5), run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(self.author), FadeOut(author_id),
                  FadeOut(follow), FadeOut(orbit_dots), run_time=0.8)

    # ══════════════════════════════════════════
    # 辅助方法
    # ══════════════════════════════════════════

    def _system_mob(self, pos, size=38, numbered=False):
        """生成带大括号的方程组"""
        eq1 = MathTex(r"2x + y = 8", font_size=size)
        # 索引: 2->0,1  x->1  +->2  y->3  =->4  8->5
        # MathTex 把整个字符串合并为一个 Tex 对象，子索引按字符分
        # 安全方式：整体上色
        eq1.set_color(WHITE)

        eq2 = MathTex(r"x - y = 1", font_size=size)
        eq2.set_color(WHITE)

        if numbered:
            t1 = Text("①", font=FONT, font_size=int(size * 0.7), color=COLOR_EQ1)
            t2 = Text("②", font=FONT, font_size=int(size * 0.7), color=COLOR_EQ2)
            r1 = VGroup(eq1, t1).arrange(RIGHT, buff=0.25)
            r2 = VGroup(eq2, t2).arrange(RIGHT, buff=0.25)
        else:
            r1, r2 = eq1, eq2

        rows = VGroup(r1, r2).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        brace = MathTex(r"\left\{", font_size=int(size * 1.6), color=WHITE)
        brace.next_to(rows, LEFT, buff=0.06)
        return VGroup(brace, rows).move_to(pos)

    def _down_arrow(self, pos, length=0.6, color=GRAY_B):
        return Arrow(
            pos, pos + DOWN * length,
            color=color, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.28,
        )

    def _motto_line(self, text, color):
        dot = Dot(radius=0.09, color=color, fill_opacity=1)
        label = Text(text, font=FONT, font_size=21, color=WHITE)
        return VGroup(dot, label).arrange(RIGHT, buff=0.22)
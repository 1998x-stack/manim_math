"""
一元一次方程的概念 - Linear Equation in One Variable
六年级数学教学动画

内容: 一元一次方程的定义、标准形式、方程的解
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok 竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ============================================================
# 颜色常量
# ============================================================
BG_COLOR    = "#1a1a2e"
COLOR_X     = "#e74c3c"   # 红色  - 未知数 x
COLOR_COEFF = "#3498db"   # 蓝色  - 系数 a
COLOR_CONST = "#f39c12"   # 橙色  - 常数 b
COLOR_OK    = "#2ecc71"   # 绿色  - 正确
COLOR_WRONG = "#e74c3c"   # 红色  - 错误
COLOR_CARD  = "#16213e"   # 深蓝  - 卡片背景
FONT        = "Noto Sans CJK SC"


# ============================================================
# 辅助函数：创建带圆角背景的文本卡片
# ============================================================
def make_card(mobject, fill_color=COLOR_CARD, stroke_color=WHITE,
              buff=0.25, corner_radius=0.15):
    bg = SurroundingRectangle(
        mobject,
        fill_color=fill_color,
        fill_opacity=0.85,
        stroke_color=stroke_color,
        stroke_width=2,
        buff=buff,
        corner_radius=corner_radius
    )
    return bg


def make_check(text, is_correct, font_size=26, x_offset=0, y_pos=0):
    """
    创建 ✓ 或 ✗ 加说明的一行判断。
    返回 VGroup
    """
    mark = Text(
        "✓" if is_correct else "✗",
        font=FONT,
        font_size=font_size + 4,
        color=COLOR_OK if is_correct else COLOR_WRONG
    )
    label = Text(
        text,
        font=FONT,
        font_size=font_size,
        color=WHITE
    )
    row = VGroup(mark, label).arrange(RIGHT, buff=0.25)
    row.move_to(np.array([x_offset, y_pos, 0]))
    return row


# ============================================================
# 主场景
# ============================================================
class LinearEquationConcept(Scene):
    """
    一元一次方程的概念教学动画

    场景顺序:
      1. 开场钩子 (生活情境)
      2. 建立方程表达
      3. 定义三要素
      4. 反例辨析
      5. 标准形式 ax+b=0
      6. 方程的解
      7. 解方程预告
      8. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者信息（全程保留）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.add(self.author)

        # 顺序执行各场景
        self.scene_hook()
        self.scene_build_equation()
        self.scene_definition()
        self.scene_counterexamples()
        self.scene_standard_form()
        self.scene_solution()
        self.scene_preview()
        self.scene_summary()
        self.scene_outro()

    # ----------------------------------------------------------
    # Scene 1: 开场钩子
    # ----------------------------------------------------------
    def scene_hook(self):
        hook = Text(
            "你能找出这个神秘数字吗？",
            font=FONT, font_size=34, color=YELLOW
        ).move_to(UP * 5.8)

        # 情境问题
        problem = VGroup(
            Text("某数加上 5，等于 12", font=FONT, font_size=30, color=WHITE),
            Text("这个「某数」是多少？", font=FONT, font_size=26, color=GRAY_A),
        ).arrange(DOWN, buff=0.4).move_to(UP * 4.0)

        # 直觉猜测框
        guess_frame = RoundedRectangle(
            width=4.0, height=1.0, corner_radius=0.2,
            fill_color="#0d3349", fill_opacity=0.8,
            stroke_color=YELLOW, stroke_width=2.5
        ).move_to(UP * 2.3)
        guess_text = Text("？ + 5 = 12", font=FONT, font_size=36, color=YELLOW).move_to(UP * 2.3)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(problem, shift=UP * 0.3), run_time=0.6)
        self.play(Create(guess_frame), Write(guess_text), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(problem),
            FadeOut(guess_frame), FadeOut(guess_text),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 2: 建立方程表达
    # ----------------------------------------------------------
    def scene_build_equation(self):
        title = Text("用字母表示未知数", font=FONT, font_size=32, color=GOLD).move_to(UP * 6.2)

        # 步骤1：文字
        word_eq = VGroup(
            Text("某数", font=FONT, font_size=34, color=COLOR_X),
            Text("+  5  =  12", font=FONT, font_size=34, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.5)

        # 箭头 + 替换说明
        arrow = MathTex(r"\Downarrow", font_size=38, color=COLOR_COEFF).move_to(UP * 3.4)
        hint = Text("用 x 代替「某数」", font=FONT, font_size=26, color=COLOR_COEFF).move_to(UP * 2.8)

        # 步骤2：符号方程（分色）
        sym_eq = MathTex(
            r"x", r"+", r"5", r"=", r"12",
            font_size=62
        ).move_to(UP * 1.8)
        sym_eq[0].set_color(COLOR_X)
        sym_eq[2].set_color(COLOR_CONST)
        sym_eq[4].set_color(COLOR_CONST)

        # 结构标注
        label_lhs = Text("左边", font=FONT, font_size=20, color=COLOR_COEFF)
        label_eq  = Text("等号", font=FONT, font_size=20, color=WHITE)
        label_rhs = Text("右边", font=FONT, font_size=20, color=COLOR_CONST)
        label_lhs.next_to(sym_eq[2], DOWN, buff=0.55).shift(LEFT * 0.5)
        label_eq.next_to(sym_eq[3],  DOWN, buff=0.55)
        label_rhs.next_to(sym_eq[4], DOWN, buff=0.55)

        arr_lhs = Arrow(label_lhs.get_top(), sym_eq[2].get_bottom(),
                        buff=0.08, color=COLOR_COEFF,
                        stroke_width=2, max_tip_length_to_length_ratio=0.25)
        arr_eq  = Arrow(label_eq.get_top(),  sym_eq[3].get_bottom(),
                        buff=0.08, color=WHITE,
                        stroke_width=2, max_tip_length_to_length_ratio=0.25)
        arr_rhs = Arrow(label_rhs.get_top(), sym_eq[4].get_bottom(),
                        buff=0.08, color=COLOR_CONST,
                        stroke_width=2, max_tip_length_to_length_ratio=0.25)

        key_point = Text(
            "含有未知数 x 的等式 → 方程！",
            font=FONT, font_size=24, color=COLOR_OK
        ).move_to(DOWN * 0.6)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(word_eq), run_time=0.5)
        self.play(FadeIn(arrow), Write(hint), run_time=0.5)
        self.play(Write(sym_eq), run_time=0.9)
        self.play(
            FadeIn(label_lhs), GrowArrow(arr_lhs),
            FadeIn(label_eq),  GrowArrow(arr_eq),
            FadeIn(label_rhs), GrowArrow(arr_rhs),
            run_time=0.8
        )
        self.play(FadeIn(key_point, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 保存 sym_eq 供后续场景使用
        self.base_eq = sym_eq.copy()

        self.play(
            FadeOut(title), FadeOut(word_eq), FadeOut(arrow), FadeOut(hint),
            FadeOut(label_lhs), FadeOut(arr_lhs),
            FadeOut(label_eq),  FadeOut(arr_eq),
            FadeOut(label_rhs), FadeOut(arr_rhs),
            FadeOut(key_point),
            run_time=0.5
        )
        self.remove(sym_eq)

    # ----------------------------------------------------------
    # Scene 3: 定义三要素
    # ----------------------------------------------------------
    def scene_definition(self):
        title = Text("一元一次方程", font=FONT, font_size=42, color=GOLD).move_to(UP * 6.2)
        underline = Line(
            title.get_left() + DOWN * 0.05,
            title.get_right() + DOWN * 0.05,
            color=GOLD, stroke_width=2
        )

        self.play(Write(title), Create(underline), run_time=0.7)

        # ---- 要素一：一元 ----
        tag1 = Text("「一元」", font=FONT, font_size=28, color=COLOR_X).move_to(UP * 5.0 + LEFT * 1.5)
        desc1 = Text("只含有一个未知数", font=FONT, font_size=24, color=WHITE).move_to(UP * 5.0 + RIGHT * 0.9)
        ex1   = MathTex(r"x + 5 = 12", font_size=30, color=GRAY_A).move_to(UP * 4.35 + RIGHT * 0.9)
        ex1[0][0].set_color(COLOR_X)   # 'x' 红色
        line1 = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_D, stroke_width=1).move_to(UP * 3.8)

        self.play(FadeIn(tag1, shift=RIGHT * 0.3), FadeIn(desc1), run_time=0.6)
        self.play(FadeIn(ex1), run_time=0.4)
        self.play(Create(line1), run_time=0.3)
        self.wait(0.5)

        # ---- 要素二：一次 ----
        tag2 = Text("「一次」", font=FONT, font_size=28, color=COLOR_COEFF).move_to(UP * 3.2 + LEFT * 1.5)
        desc2 = Text("未知数的次数是 1", font=FONT, font_size=24, color=WHITE).move_to(UP * 3.2 + RIGHT * 0.9)
        # 用上标显示指数
        ex2 = MathTex(r"x^{\,1}", font_size=34, color=COLOR_COEFF).move_to(UP * 2.55 + LEFT * 0.5)
        exp_arrow = Arrow(
            ex2.get_right() + RIGHT * 0.1,
            ex2.get_right() + RIGHT * 1.0,
            color=COLOR_COEFF, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )
        exp_note = Text("指数 = 1", font=FONT, font_size=22, color=COLOR_COEFF).next_to(exp_arrow, RIGHT, buff=0.1)
        line2 = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_D, stroke_width=1).move_to(UP * 2.0)

        self.play(FadeIn(tag2, shift=RIGHT * 0.3), FadeIn(desc2), run_time=0.6)
        self.play(FadeIn(ex2), GrowArrow(exp_arrow), FadeIn(exp_note), run_time=0.6)
        self.play(Create(line2), run_time=0.3)
        self.wait(0.5)

        # ---- 要素三：方程 ----
        tag3 = Text("「方程」", font=FONT, font_size=28, color=COLOR_CONST).move_to(UP * 1.4 + LEFT * 1.5)
        desc3 = Text("含未知数的等式", font=FONT, font_size=24, color=WHITE).move_to(UP * 1.4 + RIGHT * 0.9)

        eq_icon = MathTex(r"\square + 5 = 12", font_size=30, color=COLOR_CONST).move_to(UP * 0.75 + RIGHT * 0.9)

        self.play(FadeIn(tag3, shift=RIGHT * 0.3), FadeIn(desc3), run_time=0.6)
        self.play(FadeIn(eq_icon), run_time=0.4)
        self.wait(0.5)

        # ---- 综合定义框 ----
        defn_text = VGroup(
            Text("只含", font=FONT, font_size=22, color=WHITE),
            Text("一个", font=FONT, font_size=22, color=COLOR_X),
            Text("未知数，且未知数的次数是", font=FONT, font_size=22, color=WHITE),
            Text("1", font=FONT, font_size=22, color=COLOR_COEFF),
            Text("的整式方程", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 0.3)

        defn_bg = make_card(defn_text, fill_color="#0a1628", stroke_color=GOLD, buff=0.22)

        self.play(Create(defn_bg), FadeIn(defn_text), run_time=0.8)
        self.play(Indicate(defn_text, scale_factor=1.03, color=YELLOW), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(underline),
            FadeOut(tag1), FadeOut(desc1), FadeOut(ex1), FadeOut(line1),
            FadeOut(tag2), FadeOut(desc2), FadeOut(ex2),
            FadeOut(exp_arrow), FadeOut(exp_note), FadeOut(line2),
            FadeOut(tag3), FadeOut(desc3), FadeOut(eq_icon),
            FadeOut(defn_bg), FadeOut(defn_text),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 4: 反例辨析
    # ----------------------------------------------------------
    def scene_counterexamples(self):
        title = Text("判断：是否是一元一次方程？", font=FONT, font_size=28, color=GOLD).move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        # 4 道题目（公式 + 判断 + 原因）
        items = [
            # (latex, is_ok, reason_text)
            (r"x + 5 = 12",      True,  "是（一个未知数，一次）"),
            (r"x^2 + 1 = 0",     False, "否（x 的次数是 2）"),
            (r"x + y = 3",       False, "否（含两个未知数）"),
            (r"3x - 6 = 0",      True,  "是（一个未知数，一次）"),
        ]

        y_positions = [4.8, 3.4, 2.0, 0.6]
        rows = []

        for i, ((latex, is_ok, reason), y) in enumerate(zip(items, y_positions)):
            # 公式
            formula = MathTex(latex, font_size=38).move_to(UP * y + LEFT * 1.2)
            if not is_ok:
                # 二次号变色
                if "^2" in latex:
                    pass  # 整体变色
                formula.set_color(GRAY_B)
            else:
                formula[0][0].set_color(COLOR_X) if len(latex) > 0 else None

            # 判断结果
            mark_char = "✓" if is_ok else "✗"
            mark = Text(mark_char, font=FONT, font_size=32,
                        color=COLOR_OK if is_ok else COLOR_WRONG
                        ).next_to(formula, RIGHT, buff=0.4)

            # 原因
            reason_t = Text(reason, font=FONT, font_size=20,
                            color=GRAY_A).move_to(UP * (y - 0.5) + RIGHT * 0.5)

            rows.append((formula, mark, reason_t))
            self.play(Write(formula), run_time=0.5)
            self.play(FadeIn(mark, scale=0.7), run_time=0.4)
            self.play(FadeIn(reason_t), run_time=0.3)
            self.wait(0.3)

        self.wait(1.2)

        all_objs = [obj for row in rows for obj in row]
        self.play(FadeOut(title), *[FadeOut(o) for o in all_objs], run_time=0.6)

    # ----------------------------------------------------------
    # Scene 5: 标准形式 ax+b=0
    # ----------------------------------------------------------
    def scene_standard_form(self):
        title = Text("标准形式", font=FONT, font_size=34, color=GOLD).move_to(UP * 6.3)

        # 大公式
        std_eq = MathTex(
            r"a", r"x", r"+", r"b", r"=", r"0",
            font_size=72
        ).move_to(UP * 4.5)
        std_eq[0].set_color(COLOR_COEFF)
        std_eq[1].set_color(COLOR_X)
        std_eq[3].set_color(COLOR_CONST)

        self.play(Write(title), run_time=0.5)
        self.play(Write(std_eq), run_time=1.0)
        self.wait(0.4)

        # 标注箭头（三个部分）
        # --- a 的标注 ---
        lbl_a = VGroup(
            Text("系数", font=FONT, font_size=22, color=COLOR_COEFF),
            Text("a ≠ 0", font=FONT, font_size=20, color=COLOR_COEFF),
        ).arrange(DOWN, buff=0.1).move_to(UP * 3.1 + LEFT * 2.8)
        arr_a = Arrow(
            lbl_a.get_top(),
            std_eq[0].get_bottom() + DOWN * 0.1,
            buff=0.1, color=COLOR_COEFF,
            stroke_width=2, max_tip_length_to_length_ratio=0.28
        )

        # --- x 的标注 ---
        lbl_x = VGroup(
            Text("未知数", font=FONT, font_size=22, color=COLOR_X),
        ).move_to(UP * 2.9 + LEFT * 0.3)
        arr_x = Arrow(
            lbl_x.get_top(),
            std_eq[1].get_bottom() + DOWN * 0.1,
            buff=0.1, color=COLOR_X,
            stroke_width=2, max_tip_length_to_length_ratio=0.28
        )

        # --- b 的标注 ---
        lbl_b = VGroup(
            Text("常数项", font=FONT, font_size=22, color=COLOR_CONST),
        ).move_to(UP * 2.9 + RIGHT * 2.0)
        arr_b = Arrow(
            lbl_b.get_top(),
            std_eq[3].get_bottom() + DOWN * 0.1,
            buff=0.1, color=COLOR_CONST,
            stroke_width=2, max_tip_length_to_length_ratio=0.28
        )

        self.play(
            GrowArrow(arr_a), FadeIn(lbl_a),
            GrowArrow(arr_x), FadeIn(lbl_x),
            GrowArrow(arr_b), FadeIn(lbl_b),
            run_time=0.9
        )

        # 强调 a ≠ 0
        warn_bg = RoundedRectangle(
            width=4.0, height=0.8, corner_radius=0.15,
            fill_color="#4a0000", fill_opacity=0.7,
            stroke_color=COLOR_WRONG, stroke_width=2.5
        ).move_to(UP * 1.5)
        warn_txt = Text("⚠  a ≠ 0  非常重要！", font=FONT, font_size=24, color="#ff6b6b").move_to(UP * 1.5)

        self.play(Create(warn_bg), Write(warn_txt), run_time=0.7)
        self.play(Indicate(warn_txt, scale_factor=1.1, color=YELLOW), run_time=0.5)

        # 一般形式
        general_title = Text("一般形式：", font=FONT, font_size=24, color=GRAY_A).move_to(DOWN * 0.0 + LEFT * 1.5)
        general_eq = MathTex(r"ax = b", font_size=46).move_to(DOWN * 0.0 + RIGHT * 1.2)
        general_eq[0][0].set_color(COLOR_COEFF)
        general_eq[0][1].set_color(COLOR_X)
        general_eq[0][3].set_color(COLOR_CONST)

        self.play(FadeIn(general_title), Write(general_eq), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(std_eq),
            FadeOut(lbl_a), FadeOut(arr_a),
            FadeOut(lbl_x), FadeOut(arr_x),
            FadeOut(lbl_b), FadeOut(arr_b),
            FadeOut(warn_bg), FadeOut(warn_txt),
            FadeOut(general_title), FadeOut(general_eq),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 6: 方程的解
    # ----------------------------------------------------------
    def scene_solution(self):
        title = Text("什么是方程的解？", font=FONT, font_size=32, color=GOLD).move_to(UP * 6.3)

        eq_display = MathTex(r"x + 5 = 12", font_size=58).move_to(UP * 5.1)
        eq_display[0][0].set_color(COLOR_X)

        self.play(Write(title), run_time=0.5)
        self.play(Write(eq_display), run_time=0.7)
        self.wait(0.4)

        # ---- 尝试 x = 7 ----
        try_title1 = Text("当 x = 7 时：", font=FONT, font_size=26, color=COLOR_X).move_to(UP * 3.8 + LEFT * 1.0)

        # 左边代入
        lhs1 = MathTex(r"7 + 5 = 12", font_size=44).move_to(UP * 2.9)
        lhs1[0][0].set_color(COLOR_X)

        check1 = VGroup(
            MathTex(r"\checkmark", font_size=32, color=COLOR_OK),
            Text("左边 = 右边", font=FONT, font_size=28, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2.1)

        result1 = VGroup(
            Text("x = 7", font=FONT, font_size=28, color=COLOR_X),
            Text("是方程的解 ✓", font=FONT, font_size=26, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.3)
        result1_bg = make_card(result1, stroke_color=COLOR_OK, fill_color="#0a1e0a")

        self.play(FadeIn(try_title1), run_time=0.4)
        self.play(Write(lhs1), run_time=0.6)
        self.play(FadeIn(check1), run_time=0.4)
        self.play(Create(result1_bg), FadeIn(result1), run_time=0.5)
        self.wait(0.8)

        # 分割线
        div = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_D, stroke_width=1.5).move_to(UP * 0.6)
        self.play(Create(div), run_time=0.3)

        # ---- 尝试 x = 3 ----
        try_title2 = Text("当 x = 3 时：", font=FONT, font_size=26, color=GRAY_A).move_to(DOWN * 0.1 + LEFT * 1.0)

        lhs2 = MathTex(r"3 + 5 = 8 \neq 12", font_size=40).move_to(DOWN * 0.9)
        lhs2[0][0].set_color(GRAY_A)

        result2 = VGroup(
            Text("x = 3", font=FONT, font_size=26, color=GRAY_A),
            Text("不是方程的解 ✗", font=FONT, font_size=24, color=COLOR_WRONG),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.9)
        result2_bg = make_card(result2, stroke_color=COLOR_WRONG, fill_color="#1e0a0a")

        self.play(FadeIn(try_title2), run_time=0.4)
        self.play(Write(lhs2), run_time=0.6)
        self.play(Create(result2_bg), FadeIn(result2), run_time=0.5)
        self.wait(0.6)

        # ---- 结论 ----
        concl = VGroup(
            Text("使左右两边相等的", font=FONT, font_size=22, color=WHITE),
            Text("未知数的值", font=FONT, font_size=22, color=COLOR_X),
            Text("= 方程的解", font=FONT, font_size=22, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 3.2)
        concl_bg = make_card(concl, stroke_color=GOLD, fill_color="#1a1400", buff=0.2)

        self.play(Create(concl_bg), FadeIn(concl), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(eq_display),
            FadeOut(try_title1), FadeOut(lhs1), FadeOut(check1),
            FadeOut(result1_bg), FadeOut(result1), FadeOut(div),
            FadeOut(try_title2), FadeOut(lhs2),
            FadeOut(result2_bg), FadeOut(result2),
            FadeOut(concl_bg), FadeOut(concl),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 7: 解方程预告
    # ----------------------------------------------------------
    def scene_preview(self):
        teaser = Text("如何求解一元一次方程？", font=FONT, font_size=30, color=YELLOW).move_to(UP * 5.8)

        eq_start = MathTex(r"x + 5 = 12", font_size=58).move_to(UP * 4.3)
        eq_start[0][0].set_color(COLOR_X)

        method = Text("两边同时减 5（等式性质）", font=FONT, font_size=24, color=COLOR_COEFF).move_to(UP * 3.0)
        down_arr = MathTex(r"\Downarrow", font_size=40, color=COLOR_COEFF).move_to(UP * 2.2)

        eq_end = MathTex(r"x = 7", font_size=62, color=COLOR_OK).move_to(UP * 1.2)
        eq_end_box = SurroundingRectangle(eq_end, color=COLOR_OK, buff=0.2, corner_radius=0.12)

        stay_tuned = Text("下期详解！敬请期待 →", font=FONT, font_size=24, color=GRAY_A).move_to(DOWN * 0.1)

        self.play(Write(teaser), run_time=0.6)
        self.play(Write(eq_start), run_time=0.6)
        self.play(FadeIn(method), run_time=0.4)
        self.play(FadeIn(down_arr), run_time=0.3)
        self.play(Write(eq_end), Create(eq_end_box), run_time=0.7)
        self.play(FadeIn(stay_tuned), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(teaser), FadeOut(eq_start), FadeOut(method),
            FadeOut(down_arr), FadeOut(eq_end), FadeOut(eq_end_box),
            FadeOut(stay_tuned),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 8: 总结
    # ----------------------------------------------------------
    def scene_summary(self):
        title = Text("一元一次方程 · 核心概念", font=FONT, font_size=30, color=GOLD).move_to(UP * 6.3)

        # 卡片 1：定义
        card1_rows = VGroup(
            Text("定 义", font=FONT, font_size=24, color=COLOR_X),
            Text("一个未知数  次数为 1  的整式方程", font=FONT, font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2).move_to(UP * 5.1)
        card1_bg = make_card(card1_rows, stroke_color=COLOR_X, fill_color="#1e0010", buff=0.22)

        # 卡片 2：标准形式
        card2_label = Text("标准形式", font=FONT, font_size=24, color=COLOR_COEFF).move_to(UP * 3.8)
        card2_formula = MathTex(r"ax + b = 0 \quad (a \neq 0)", font_size=38).move_to(UP * 3.1)
        card2_formula[0][0].set_color(COLOR_COEFF)
        card2_formula[0][1].set_color(COLOR_X)
        card2_formula[0][3].set_color(COLOR_CONST)
        card2_bg = make_card(
            VGroup(card2_label, card2_formula),
            stroke_color=COLOR_COEFF, fill_color="#001020", buff=0.22
        )

        # 卡片 3：方程的解
        card3_label = Text("方程的解", font=FONT, font_size=24, color=COLOR_OK).move_to(UP * 1.7)
        card3_desc  = Text(
            "使左右两边相等的未知数的值",
            font=FONT, font_size=20, color=WHITE
        ).move_to(UP * 1.1)
        card3_bg = make_card(
            VGroup(card3_label, card3_desc),
            stroke_color=COLOR_OK, fill_color="#001a08", buff=0.22
        )

        self.play(Write(title), run_time=0.5)
        self.play(Create(card1_bg), FadeIn(card1_rows), run_time=0.6)
        self.play(Create(card2_bg), Write(card2_label), Write(card2_formula), run_time=0.8)
        self.play(Create(card3_bg), Write(card3_label), FadeIn(card3_desc), run_time=0.6)

        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(card1_bg), FadeOut(card1_rows),
            FadeOut(card2_bg), FadeOut(card2_label), FadeOut(card2_formula),
            FadeOut(card3_bg), FadeOut(card3_label), FadeOut(card3_desc),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 9: 片尾
    # ----------------------------------------------------------
    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=26, color=GRAY_B
        ).move_to(UP * 1.1)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 0.2)

        # 装饰：等式符号串
        deco = VGroup(*[
            MathTex(r"ax+b=0", font_size=22, color=color).set_opacity(0.5)
            for color in [COLOR_X, COLOR_COEFF, COLOR_CONST, COLOR_OK, COLOR_X]
        ]).arrange(DOWN, buff=0.25).move_to(DOWN * 2.2)

        self.play(
            Transform(self.author, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.play(FadeIn(deco), run_time=0.5)
        self.play(
            *[Indicate(eq, scale_factor=1.15) for eq in deco],
            run_time=0.8
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco),
            run_time=0.8
        )

# # 渲染命令
# manim -pql linear_equation_concept.py LinearEquationConcept   # 快速预览
# manim -qh  linear_equation_concept.py LinearEquationConcept   # 高质量输
"""
等式的性质 - Equality Properties Animation
六年级数学教学动画

内容: 等式的两条基本性质
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
BG_COLOR = "#1a1a2e"
COLOR_LEFT = "#3498db"    # 蓝色 - 等式左边
COLOR_RIGHT = "#e74c3c"   # 红色 - 等式右边
COLOR_OP = "#f39c12"      # 橙色 - 运算操作
COLOR_OK = "#2ecc71"      # 绿色 - 成立/正确
COLOR_WARN = "#e74c3c"    # 红色 - 警告
COLOR_SCALE = "#95a5a6"   # 灰色 - 天平
FONT = "Noto Sans CJK SC"


# ============================================================
# 天平 Builder 函数
# ============================================================
def build_balance(scale_x=1.0, pivot_y=2.5, pan_y=0.8, pan_width=1.4,
                  balanced=True, tilt_angle=0, color=COLOR_SCALE):
    """
    构建天平 VGroup。
    返回: VGroup(base, pillar, beam, left_strings, right_strings, left_pan, right_pan)
    所有坐标均用 numpy 精确计算。
    """
    half_beam = 2.2 * scale_x

    # 关键坐标
    pivot = np.array([0, pivot_y, 0])
    left_hook = np.array([-half_beam, pivot_y, 0])
    right_hook = np.array([half_beam, pivot_y, 0])
    left_pan_center = np.array([-half_beam, pan_y, 0])
    right_pan_center = np.array([half_beam, pan_y, 0])
    base_y = pivot_y - 2.2

    # --- 底座 ---
    base = Line(
        np.array([-0.8, base_y, 0]),
        np.array([0.8, base_y, 0]),
        color=color, stroke_width=5
    )

    # --- 立柱 ---
    pillar = Line(
        np.array([0, base_y, 0]),
        pivot,
        color=color, stroke_width=4
    )

    # --- 横梁 ---
    beam = Line(left_hook, right_hook, color=color, stroke_width=4)

    # --- 左盘吊绳 ---
    str_len = pivot_y - pan_y - 0.15
    l_str_l = Line(
        left_hook + np.array([-0.3, 0, 0]),
        left_pan_center + np.array([-0.3, str_len, 0]) + np.array([0, 0, 0]),
        color=color, stroke_width=2
    )
    l_str_r = Line(
        left_hook + np.array([0.3, 0, 0]),
        left_pan_center + np.array([0.3, str_len, 0]) + np.array([0, 0, 0]),
        color=color, stroke_width=2
    )

    # --- 右盘吊绳 ---
    r_str_l = Line(
        right_hook + np.array([-0.3, 0, 0]),
        right_pan_center + np.array([-0.3, str_len, 0]),
        color=color, stroke_width=2
    )
    r_str_r = Line(
        right_hook + np.array([0.3, 0, 0]),
        right_pan_center + np.array([0.3, str_len, 0]),
        color=color, stroke_width=2
    )

    # --- 托盘 ---
    half_pw = pan_width / 2
    left_pan = RoundedRectangle(
        width=pan_width, height=0.18,
        corner_radius=0.09,
        fill_color=color, fill_opacity=0.5,
        stroke_color=color, stroke_width=2
    ).move_to(left_pan_center)

    right_pan = RoundedRectangle(
        width=pan_width, height=0.18,
        corner_radius=0.09,
        fill_color=color, fill_opacity=0.5,
        stroke_color=color, stroke_width=2
    ).move_to(right_pan_center)

    # --- 汇总 ---
    scale_group = VGroup(base, pillar, beam,
                         l_str_l, l_str_r, r_str_l, r_str_r,
                         left_pan, right_pan)
    return scale_group


def get_pan_positions(pivot_y=2.5, pan_y=0.8, scale_x=1.0):
    """返回左右托盘中心位置"""
    half_beam = 2.2 * scale_x
    left = np.array([-half_beam, pan_y, 0])
    right = np.array([half_beam, pan_y, 0])
    return left, right


# ============================================================
# 主场景类
# ============================================================
class EqualityProperties(Scene):
    """
    等式的性质教学动画
    场景顺序:
      1. 开场钩子
      2. 天平引入等式概念
      3. 性质一：加减法
      4. 性质二：乘除法
      5. 实例解方程
      6. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 全局作者信息（全程保留）
        self.author_text = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.add(self.author_text)

        # 执行各场景
        self.scene_hook()
        self.scene_intro_balance()
        self.scene_property1_add()
        self.scene_property1_sub()
        self.scene_property2_mul()
        self.scene_property2_div()
        self.scene_example()
        self.scene_summary()
        self.scene_outro()

    # ----------------------------------------------------------
    # Scene 1: 开场钩子
    # ----------------------------------------------------------
    def scene_hook(self):
        hook = Text(
            "等号两边能随意操作吗？",
            font=FONT, font_size=36, color=YELLOW
        ).move_to(UP * 5.5)

        eq_example = MathTex(
            r"x + 3 = 7",
            font_size=52, color=WHITE
        ).move_to(UP * 3.8)

        arrow_left = MathTex(r"\Downarrow", font_size=40, color=COLOR_OP).move_to(UP * 2.8)
        q_mark = Text("怎样求解 x？", font=FONT, font_size=30, color=COLOR_OP).move_to(UP * 2.1)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(eq_example, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(arrow_left), Write(q_mark), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(eq_example),
            FadeOut(arrow_left), FadeOut(q_mark),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 2: 天平引入等式
    # ----------------------------------------------------------
    def scene_intro_balance(self):
        title = Text("等式 = 天平平衡", font=FONT, font_size=38, color=GOLD).move_to(UP * 6.0)
        subtitle = Text("a = b", font=FONT, font_size=20, color=GRAY_A).move_to(UP * 5.3)

        # 天平
        scale = build_balance(pivot_y=2.8, pan_y=1.2, scale_x=0.95)
        scale.move_to(UP * 0.5)

        # 天平上的符号
        left_center, right_center = get_pan_positions(pivot_y=2.8, pan_y=1.2, scale_x=0.95)
        left_center += UP * 0.5   # 考虑 scale.move_to(UP*0.5)
        right_center += UP * 0.5

        a_label = MathTex(r"a", font_size=44, color=COLOR_LEFT).move_to(left_center + UP * 0.45)
        b_label = MathTex(r"b", font_size=44, color=COLOR_RIGHT).move_to(right_center + UP * 0.45)

        # 等式公式
        main_eq = MathTex(
            r"a", r"=", r"b",
            font_size=54
        ).move_to(DOWN * 1.5)
        main_eq[0].set_color(COLOR_LEFT)
        main_eq[1].set_color(WHITE)
        main_eq[2].set_color(COLOR_RIGHT)

        explain = Text(
            "天平平衡，左右相等",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 2.8)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.3)
        self.play(Create(scale), run_time=1.0)
        self.play(
            FadeIn(a_label, shift=DOWN * 0.2),
            FadeIn(b_label, shift=DOWN * 0.2),
            run_time=0.5
        )
        self.play(Write(main_eq), run_time=0.7)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(scale), FadeOut(a_label), FadeOut(b_label),
            FadeOut(main_eq), FadeOut(explain),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 3: 性质一 — 加法
    # ----------------------------------------------------------
    def scene_property1_add(self):
        # --- 标题 ---
        prop1_title = Text("性质一（加法）", font=FONT, font_size=34, color="#3498db").move_to(UP * 6.0)
        prop1_sub = Text("两边同时加同一个数", font=FONT, font_size=24, color=GRAY_A).move_to(UP * 5.3)

        # --- 天平 ---
        scale = build_balance(pivot_y=2.8, pan_y=1.2, scale_x=0.95)
        scale.move_to(UP * 0.8)
        left_ctr, right_ctr = get_pan_positions(pivot_y=2.8, pan_y=1.2, scale_x=0.95)
        left_ctr += UP * 0.8
        right_ctr += UP * 0.8

        a_lbl = MathTex(r"a", font_size=40, color=COLOR_LEFT).move_to(left_ctr + UP * 0.45)
        b_lbl = MathTex(r"b", font_size=40, color=COLOR_RIGHT).move_to(right_ctr + UP * 0.45)

        # --- 初始等式 ---
        eq0 = MathTex(r"a", r"=", r"b", font_size=48).move_to(DOWN * 0.8)
        eq0[0].set_color(COLOR_LEFT)
        eq0[1].set_color(WHITE)
        eq0[2].set_color(COLOR_RIGHT)

        self.play(Write(prop1_title), run_time=0.6)
        self.play(FadeIn(prop1_sub), run_time=0.3)
        self.play(Create(scale), run_time=0.8)
        self.play(FadeIn(a_lbl), FadeIn(b_lbl), run_time=0.4)
        self.play(Write(eq0), run_time=0.5)
        self.wait(0.5)

        # --- 两边同时加 c ---
        add_left = MathTex(r"+\,c", font_size=34, color=COLOR_OP).next_to(left_ctr, UP, buff=1.1)
        add_right = MathTex(r"+\,c", font_size=34, color=COLOR_OP).next_to(right_ctr, UP, buff=1.1)

        arrow_left = Arrow(
            add_left.get_bottom(), left_ctr + UP * 0.7,
            color=COLOR_OP, stroke_width=3, max_tip_length_to_length_ratio=0.25
        )
        arrow_right = Arrow(
            add_right.get_bottom(), right_ctr + UP * 0.7,
            color=COLOR_OP, stroke_width=3, max_tip_length_to_length_ratio=0.25
        )

        self.play(
            FadeIn(add_left, shift=DOWN * 0.2),
            FadeIn(add_right, shift=DOWN * 0.2),
            GrowArrow(arrow_left),
            GrowArrow(arrow_right),
            run_time=0.8
        )
        self.wait(0.5)

        # --- 天平保持平衡（闪绿色） ---
        beam_highlight = Line(
            left_ctr + UP * 1.6,
            right_ctr + UP * 1.6,
            color=COLOR_OK, stroke_width=6
        )
        balanced_text = Text("仍然平衡！", font=FONT, font_size=28, color=COLOR_OK).move_to(UP * 3.8)

        self.play(Create(beam_highlight), Write(balanced_text), run_time=0.6)
        self.wait(0.5)

        # --- 结论公式 ---
        eq1 = MathTex(
            r"a", r"+", r"c", r"=", r"b", r"+", r"c",
            font_size=48
        ).move_to(DOWN * 2.0)
        eq1[0].set_color(COLOR_LEFT)
        eq1[2].set_color(COLOR_OP)
        eq1[3].set_color(WHITE)
        eq1[4].set_color(COLOR_RIGHT)
        eq1[6].set_color(COLOR_OP)

        prop_text = Text(
            "若 a = b，则 a + c = b + c",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.2)

        self.play(FadeOut(eq0), run_time=0.2)
        self.play(Write(eq1), run_time=0.8)
        self.play(FadeIn(prop_text), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(prop1_title), FadeOut(prop1_sub),
            FadeOut(scale), FadeOut(a_lbl), FadeOut(b_lbl),
            FadeOut(add_left), FadeOut(add_right),
            FadeOut(arrow_left), FadeOut(arrow_right),
            FadeOut(beam_highlight), FadeOut(balanced_text),
            FadeOut(eq1), FadeOut(prop_text),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 4: 性质一 — 减法（快速）
    # ----------------------------------------------------------
    def scene_property1_sub(self):
        sub_title = Text("性质一（减法）", font=FONT, font_size=34, color=COLOR_LEFT).move_to(UP * 6.0)

        eq0 = MathTex(r"a", r"=", r"b", font_size=52).move_to(UP * 3.5)
        eq0[0].set_color(COLOR_LEFT); eq0[2].set_color(COLOR_RIGHT)

        arrow_mid = VGroup(
            MathTex(r"\Downarrow", font_size=32, color=COLOR_OP),
            Text("-c（两边同减）", font=FONT, font_size=26, color=COLOR_OP)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)

        eq1 = MathTex(
            r"a", r"-", r"c", r"=", r"b", r"-", r"c",
            font_size=52
        ).move_to(UP * 0.6)
        eq1[0].set_color(COLOR_LEFT)
        eq1[2].set_color(COLOR_OP)
        eq1[3].set_color(WHITE)
        eq1[4].set_color(COLOR_RIGHT)
        eq1[6].set_color(COLOR_OP)

        prop_box = SurroundingRectangle(eq1, color=COLOR_OK, buff=0.2, corner_radius=0.1)

        summary1 = Text(
            "等式两边同时加减同一个数",
            font=FONT, font_size=24, color=COLOR_OK
        ).move_to(DOWN * 1.0)
        summary2 = Text(
            "等式仍然成立",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 1.8)

        self.play(Write(sub_title), run_time=0.5)
        self.play(Write(eq0), run_time=0.5)
        self.play(FadeIn(arrow_mid, shift=DOWN * 0.2), run_time=0.4)
        self.play(Write(eq1), run_time=0.7)
        self.play(Create(prop_box), run_time=0.4)
        self.play(FadeIn(summary1), Write(summary2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sub_title), FadeOut(eq0), FadeOut(arrow_mid),
            FadeOut(eq1), FadeOut(prop_box),
            FadeOut(summary1), FadeOut(summary2),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 5: 性质二 — 乘法
    # ----------------------------------------------------------
    def scene_property2_mul(self):
        prop2_title = Text("性质二（乘法）", font=FONT, font_size=34, color="#e67e22").move_to(UP * 6.0)
        prop2_sub = Text("两边同时乘以同一个数（≠0）", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 5.3)

        # 天平
        scale = build_balance(pivot_y=2.8, pan_y=1.2, scale_x=0.95)
        scale.move_to(UP * 0.8)
        left_ctr, right_ctr = get_pan_positions(pivot_y=2.8, pan_y=1.2, scale_x=0.95)
        left_ctr += UP * 0.8
        right_ctr += UP * 0.8

        a_lbl = MathTex(r"a", font_size=40, color=COLOR_LEFT).move_to(left_ctr + UP * 0.45)
        b_lbl = MathTex(r"b", font_size=40, color=COLOR_RIGHT).move_to(right_ctr + UP * 0.45)

        eq0 = MathTex(r"a", r"=", r"b", font_size=48).move_to(DOWN * 0.8)
        eq0[0].set_color(COLOR_LEFT); eq0[2].set_color(COLOR_RIGHT)

        self.play(Write(prop2_title), run_time=0.5)
        self.play(FadeIn(prop2_sub), run_time=0.3)
        self.play(Create(scale), run_time=0.8)
        self.play(FadeIn(a_lbl), FadeIn(b_lbl), run_time=0.4)
        self.play(Write(eq0), run_time=0.5)
        self.wait(0.4)

        # 两边同乘 c
        mul_left = MathTex(r"\times\, c", font_size=34, color=COLOR_OP).next_to(left_ctr, UP, buff=1.1)
        mul_right = MathTex(r"\times\, c", font_size=34, color=COLOR_OP).next_to(right_ctr, UP, buff=1.1)

        arrow_l = Arrow(
            mul_left.get_bottom(), left_ctr + UP * 0.7,
            color=COLOR_OP, stroke_width=3, max_tip_length_to_length_ratio=0.25
        )
        arrow_r = Arrow(
            mul_right.get_bottom(), right_ctr + UP * 0.7,
            color=COLOR_OP, stroke_width=3, max_tip_length_to_length_ratio=0.25
        )

        self.play(
            FadeIn(mul_left), FadeIn(mul_right),
            GrowArrow(arrow_l), GrowArrow(arrow_r),
            run_time=0.7
        )

        beam_ok = Line(
            left_ctr + UP * 1.6, right_ctr + UP * 1.6,
            color=COLOR_OK, stroke_width=6
        )
        self.play(Create(beam_ok), run_time=0.5)

        # 结论公式
        eq1 = MathTex(
            r"a", r"c", r"=", r"b", r"c",
            font_size=48
        ).move_to(DOWN * 2.0)
        eq1[0].set_color(COLOR_LEFT)
        eq1[1].set_color(COLOR_OP)
        eq1[2].set_color(WHITE)
        eq1[3].set_color(COLOR_RIGHT)
        eq1[4].set_color(COLOR_OP)

        self.play(FadeOut(eq0), run_time=0.2)
        self.play(Write(eq1), run_time=0.7)

        # 警告框: c ≠ 0
        warn_box = RoundedRectangle(
            width=4.5, height=0.9,
            corner_radius=0.15,
            fill_color="#7f0000", fill_opacity=0.5,
            stroke_color=COLOR_WARN, stroke_width=3
        ).move_to(DOWN * 3.2)
        warn_text = Text("⚠  c ≠ 0（除数不能为零）", font=FONT, font_size=22, color="#ff6b6b").move_to(DOWN * 3.2)

        self.play(Create(warn_box), Write(warn_text), run_time=0.7)
        self.play(Indicate(warn_text, scale_factor=1.1, color=YELLOW), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(prop2_title), FadeOut(prop2_sub),
            FadeOut(scale), FadeOut(a_lbl), FadeOut(b_lbl),
            FadeOut(mul_left), FadeOut(mul_right),
            FadeOut(arrow_l), FadeOut(arrow_r),
            FadeOut(beam_ok), FadeOut(eq1),
            FadeOut(warn_box), FadeOut(warn_text),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 6: 性质二 — 除法
    # ----------------------------------------------------------
    def scene_property2_div(self):
        div_title = Text("性质二（除法）", font=FONT, font_size=34, color="#e67e22").move_to(UP * 6.0)

        eq0 = MathTex(r"a", r"=", r"b", font_size=52).move_to(UP * 4.0)
        eq0[0].set_color(COLOR_LEFT); eq0[2].set_color(COLOR_RIGHT)

        arrow_mid = MathTex(r"\Downarrow \quad \div c \;(c \neq 0)", font_size=30, color=COLOR_OP).move_to(UP * 2.5)

        eq1 = MathTex(
            r"\frac{a}{c}", r"=", r"\frac{b}{c}",
            font_size=52
        ).move_to(UP * 0.8)
        eq1[0].set_color(COLOR_LEFT)
        eq1[1].set_color(WHITE)
        eq1[2].set_color(COLOR_RIGHT)

        prop_box = SurroundingRectangle(eq1, color=COLOR_OK, buff=0.25, corner_radius=0.12)

        summary = VGroup(
            Text("等式两边同乘或同除同一个非零数", font=FONT, font_size=21, color=COLOR_OK),
            Text("等式仍然成立 ✓", font=FONT, font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.0)

        self.play(Write(div_title), run_time=0.5)
        self.play(Write(eq0), run_time=0.5)
        self.play(FadeIn(arrow_mid), run_time=0.4)
        self.play(Write(eq1), run_time=0.7)
        self.play(Create(prop_box), run_time=0.4)
        self.play(FadeIn(summary), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(div_title), FadeOut(eq0), FadeOut(arrow_mid),
            FadeOut(eq1), FadeOut(prop_box), FadeOut(summary),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 7: 实例应用 — 解方程
    # ----------------------------------------------------------
    def scene_example(self):
        title = Text("实例应用：解方程", font=FONT, font_size=32, color=GOLD).move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        # ===== 例题1: x + 3 = 7 =====
        ex1_label = Text("例1：", font=FONT, font_size=26, color=GRAY_A).move_to(UP * 5.2 + LEFT * 3)
        ex1_eq = MathTex(r"x + 3 = 7", font_size=46).move_to(UP * 5.2 + RIGHT * 0.5)

        step1_note = Text("两边同时减 3（用性质一）", font=FONT, font_size=22, color=COLOR_OP).move_to(UP * 4.0)

        step1 = MathTex(
            r"x + 3", r"-", r"3", r"=", r"7", r"-", r"3",
            font_size=42
        ).move_to(UP * 2.9)
        step1[1].set_color(COLOR_OP); step1[2].set_color(COLOR_OP)
        step1[5].set_color(COLOR_OP); step1[6].set_color(COLOR_OP)

        step2 = MathTex(r"x = 4", font_size=52, color=COLOR_OK).move_to(UP * 1.7)

        check_box = SurroundingRectangle(step2, color=COLOR_OK, buff=0.15)

        self.play(FadeIn(ex1_label), Write(ex1_eq), run_time=0.6)
        self.play(FadeIn(step1_note), run_time=0.4)
        self.play(Write(step1), run_time=0.7)
        self.play(Write(step2), run_time=0.6)
        self.play(Create(check_box), run_time=0.4)
        self.wait(0.8)

        # ===== 例题2: 2x = 6 =====
        divider = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_D, stroke_width=1.5).move_to(UP * 0.8)
        self.play(Create(divider), run_time=0.3)

        ex2_label = Text("例2：", font=FONT, font_size=26, color=GRAY_A).move_to(UP * 0.0 + LEFT * 3)
        ex2_eq = MathTex(r"2x = 6", font_size=46).move_to(UP * 0.0 + RIGHT * 0.5)

        step2a_note = Text("两边同时除以 2（用性质二）", font=FONT, font_size=22, color=COLOR_OP).move_to(DOWN * 1.0)

        step2a = MathTex(
            r"\frac{2x}{2}", r"=", r"\frac{6}{2}",
            font_size=44
        ).move_to(DOWN * 2.2)
        step2a[0].set_color(COLOR_OP)
        step2a[2].set_color(COLOR_OP)

        step2b = MathTex(r"x = 3", font_size=52, color=COLOR_OK).move_to(DOWN * 3.5)
        check_box2 = SurroundingRectangle(step2b, color=COLOR_OK, buff=0.15)

        self.play(FadeIn(ex2_label), Write(ex2_eq), run_time=0.6)
        self.play(FadeIn(step2a_note), run_time=0.4)
        self.play(Write(step2a), run_time=0.7)
        self.play(Write(step2b), run_time=0.6)
        self.play(Create(check_box2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(ex1_label), FadeOut(ex1_eq),
            FadeOut(step1_note), FadeOut(step1), FadeOut(step2),
            FadeOut(check_box), FadeOut(divider),
            FadeOut(ex2_label), FadeOut(ex2_eq),
            FadeOut(step2a_note), FadeOut(step2a),
            FadeOut(step2b), FadeOut(check_box2),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 8: 总结
    # ----------------------------------------------------------
    def scene_summary(self):
        title = Text("等式的性质 总结", font=FONT, font_size=34, color=GOLD).move_to(UP * 6.3)

        # 性质一卡片
        card1_title = Text("性质一", font=FONT, font_size=26, color=COLOR_LEFT).move_to(UP * 5.0)
        card1_content = MathTex(
            r"a = b \Rightarrow a \pm c = b \pm c",
            font_size=38
        ).move_to(UP * 4.0)
        card1_bg = SurroundingRectangle(
            VGroup(card1_title, card1_content),
            color=COLOR_LEFT, buff=0.25, corner_radius=0.15
        )

        # 性质二卡片
        card2_title = Text("性质二", font=FONT, font_size=26, color=COLOR_OP).move_to(UP * 2.0)
        card2_line1 = MathTex(
            r"a = b \Rightarrow ac = bc",
            font_size=36
        ).move_to(UP * 1.1)
        card2_line2 = MathTex(
            r"a = b \Rightarrow \frac{a}{c} = \frac{b}{c} \;(c \neq 0)",
            font_size=32
        ).move_to(UP * 0.1)
        card2_bg = SurroundingRectangle(
            VGroup(card2_title, card2_line1, card2_line2),
            color=COLOR_OP, buff=0.25, corner_radius=0.15
        )

        # 应用提示
        hint = Text(
            "这是解方程的理论基础！",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 1.5)

        self.play(Write(title), run_time=0.5)
        self.play(
            Create(card1_bg),
            Write(card1_title),
            Write(card1_content),
            run_time=0.8
        )
        self.play(
            Create(card2_bg),
            Write(card2_title),
            Write(card2_line1),
            Write(card2_line2),
            run_time=1.0
        )
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(card1_bg), FadeOut(card1_title), FadeOut(card1_content),
            FadeOut(card2_bg), FadeOut(card2_title), FadeOut(card2_line1), FadeOut(card2_line2),
            FadeOut(hint),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 9: 片尾
    # ----------------------------------------------------------
    def scene_outro(self):
        # 作者放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=26, color=GRAY_B
        ).move_to(UP * 1.1)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 0.2)

        # 装饰：三个等号
        eq_decos = VGroup(*[
            MathTex(r"=", font_size=40, color=COLOR_OK).set_opacity(0.6)
            for _ in range(5)
        ]).arrange(RIGHT, buff=0.6).move_to(DOWN * 1.5)

        self.play(
            Transform(self.author_text, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(eq_decos), run_time=0.5)
        self.play(
            *[Indicate(eq, scale_factor=1.3) for eq in eq_decos],
            run_time=0.8
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author_text),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(eq_decos),
            run_time=0.8
        )

# manim -pql equality_properties.py EqualityProperties   # 快速预览
# manim -qh  equality_properties.py EqualityProperties   # 高质量输出
"""
003_最大公因数与最小公倍数.py — 最大公因数和最小公倍数(深化) 教学动画

知识点: 分解素因数法和短除法求最大公因数与最小公倍数
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 复习: 分解素因数
  3. 短除法求 GCF 和 LCM (12 和 18)
  4. Venn 图理解 GCF / LCM
  5. 三个数的 GCF / LCM 示例 (12, 18, 24)
  6. 互素概念
  7. 应用题 (裁布问题)
  8. 总结与片尾
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR     = "#1a1a2e"
COLOR_MAIN   = "#3b82f6"   # 蓝色主色
COLOR_RED    = "#ef4444"   # 红色
COLOR_GREEN  = "#22c55e"   # 绿色结果
COLOR_HL     = "#fbbf24"   # 黄色高亮
COLOR_PURPLE = "#a78bfa"   # 紫色强调
COLOR_ORANGE = "#f59e0b"   # 橙色
COLOR_AUTHOR = "#6b7280"   # 灰色作者信息
COLOR_PINK   = "#f472b6"   # 粉色
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class GcfLcmLesson(Scene):
    """
    最大公因数和最小公倍数 (深化) 教学动画
    场景顺序:
      1. 开场钩子
      2. 复习分解素因数
      3. 短除法求 GCF / LCM  (12 和 18)
      4. Venn 图理解
      5. 三个数的 GCF / LCM
      6. 互素概念
      7. 应用题
      8. 总结与片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_prime_factorization()
        self.scene_3_short_division()
        self.scene_4_venn_diagram()
        self.scene_5_three_numbers()
        self.scene_6_coprime()
        self.scene_7_application()
        self.scene_8_summary_and_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子标题
        hook = Text(
            "12 和 18",
            font=FONT, font_size=54, color=WHITE, weight=BOLD
        ).move_to(UP * 5.0)

        hook2 = Text(
            "最大的公因数? 最小的公倍数?",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 3.8)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # 显示 12 和 18 的因数
        factors_12_label = Text("12 的因数:", font=FONT, font_size=24, color=COLOR_MAIN)
        factors_12_vals = MathTex(r"1,\ 2,\ 3,\ 4,\ 6,\ 12", font_size=28, color=WHITE)
        row_12 = VGroup(factors_12_label, factors_12_vals).arrange(RIGHT, buff=0.3).move_to(UP * 2.2)

        factors_18_label = Text("18 的因数:", font=FONT, font_size=24, color=COLOR_PURPLE)
        factors_18_vals = MathTex(r"1,\ 2,\ 3,\ 6,\ 9,\ 18", font_size=28, color=WHITE)
        row_18 = VGroup(factors_18_label, factors_18_vals).arrange(RIGHT, buff=0.3).move_to(UP * 1.0)

        self.play(FadeIn(row_12, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(row_18, shift=RIGHT * 0.3), run_time=0.6)

        # 高亮公因数
        common_label = Text("公因数:", font=FONT, font_size=24, color=COLOR_HL)
        common_vals = MathTex(r"1,\ 2,\ 3,\ 6", font_size=28, color=COLOR_HL)
        row_common = VGroup(common_label, common_vals).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.2)

        gcf_label = Text("最大公因数 = ", font=FONT, font_size=26, color=COLOR_GREEN)
        gcf_val = MathTex(r"6", font_size=36, color=COLOR_GREEN)
        row_gcf = VGroup(gcf_label, gcf_val).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.5)

        self.play(FadeIn(row_common), run_time=0.5)
        self.play(FadeIn(row_gcf, scale=1.2), run_time=0.6)
        self.wait(0.8)

        # 公倍数部分
        multiples_hint = Text(
            "那最小公倍数呢? 用短除法更快!",
            font=FONT, font_size=24, color=COLOR_ORANGE
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(multiples_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(hook2),
            FadeOut(row_12), FadeOut(row_18),
            FadeOut(row_common), FadeOut(row_gcf),
            FadeOut(multiples_hint),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 复习分解素因数
    # ------------------------------------------------------------------

    def scene_2_prime_factorization(self):
        title = Text("复习: 分解素因数", font=FONT, font_size=36, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 12 = 2^2 x 3
        label_12 = Text("12 = ", font=FONT, font_size=30, color=COLOR_MAIN)
        eq_12 = MathTex(r"2^2 \times 3", font_size=34, color=WHITE)
        row_12 = VGroup(label_12, eq_12).arrange(RIGHT, buff=0.2).move_to(UP * 3.5)

        # 18 = 2 x 3^2
        label_18 = Text("18 = ", font=FONT, font_size=30, color=COLOR_PURPLE)
        eq_18 = MathTex(r"2 \times 3^2", font_size=34, color=WHITE)
        row_18 = VGroup(label_18, eq_18).arrange(RIGHT, buff=0.2).move_to(UP * 2.3)

        self.play(FadeIn(row_12, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(row_18, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)

        # 规则卡片
        rule_box = RoundedRectangle(
            width=7.5, height=4.0, corner_radius=0.3,
            stroke_color=COLOR_HL, stroke_width=2, fill_color=BG_COLOR, fill_opacity=0.9
        ).move_to(DOWN * 0.3)

        rule_title = Text("核心方法", font=FONT, font_size=28, color=COLOR_HL, weight=BOLD).move_to(rule_box.get_top() + DOWN * 0.5)

        rule_gcf = Text(
            "GCF: 取公有素因数的最低次幂之积",
            font=FONT, font_size=22, color=COLOR_GREEN
        ).move_to(rule_box.get_center() + UP * 0.3)

        rule_lcm = Text(
            "LCM: 取所有素因数的最高次幂之积",
            font=FONT, font_size=22, color=COLOR_ORANGE
        ).move_to(rule_box.get_center() + DOWN * 0.5)

        self.play(FadeIn(rule_box), Write(rule_title), run_time=0.6)
        self.play(FadeIn(rule_gcf, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(rule_lcm, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)

        # 应用规则: GCF(12,18)
        gcf_calc_label = Text("GCF(12,18) = ", font=FONT, font_size=24, color=COLOR_GREEN)
        gcf_calc_eq = MathTex(r"2^1 \times 3^1 = 6", font_size=28, color=COLOR_GREEN)
        gcf_row = VGroup(gcf_calc_label, gcf_calc_eq).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        lcm_calc_label = Text("LCM(12,18) = ", font=FONT, font_size=24, color=COLOR_ORANGE)
        lcm_calc_eq = MathTex(r"2^2 \times 3^2 = 36", font_size=28, color=COLOR_ORANGE)
        lcm_row = VGroup(lcm_calc_label, lcm_calc_eq).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.3)

        self.play(FadeIn(gcf_row, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(lcm_row, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(row_12), FadeOut(row_18),
            FadeOut(rule_box), FadeOut(rule_title),
            FadeOut(rule_gcf), FadeOut(rule_lcm),
            FadeOut(gcf_row), FadeOut(lcm_row),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 短除法 (12 和 18)
    # ------------------------------------------------------------------

    def scene_3_short_division(self):
        title = Text("短除法", font=FONT, font_size=36, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        subtitle = Text(
            "求 12 和 18 的 GCF 与 LCM",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.6)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 短除法布局中心
        cx, cy = 0, 2.0

        # 步骤1: 写出 12 和 18
        n12 = MathTex("12", font_size=36, color=WHITE).move_to(np.array([cx - 0.8, cy, 0]))
        n18 = MathTex("18", font_size=36, color=WHITE).move_to(np.array([cx + 0.8, cy, 0]))
        self.play(Write(n12), Write(n18), run_time=0.5)

        # 步骤2: 除以 2
        div2 = MathTex("2", font_size=36, color=COLOR_RED).move_to(np.array([cx - 2.5, cy - 0.1, 0]))
        line1 = Line(
            start=np.array([cx - 2.0, cy - 0.4, 0]),
            end=np.array([cx + 1.8, cy - 0.4, 0]),
            color=GRAY_B, stroke_width=2
        )
        vline1 = Line(
            start=np.array([cx - 2.0, cy + 0.3, 0]),
            end=np.array([cx - 2.0, cy - 0.4, 0]),
            color=GRAY_B, stroke_width=2
        )

        q6 = MathTex("6", font_size=36, color=WHITE).move_to(np.array([cx - 0.8, cy - 1.0, 0]))
        q9 = MathTex("9", font_size=36, color=WHITE).move_to(np.array([cx + 0.8, cy - 1.0, 0]))

        self.play(Write(div2), Create(line1), Create(vline1), run_time=0.5)
        self.play(Write(q6), Write(q9), run_time=0.5)

        # 步骤3: 除以 3
        div3 = MathTex("3", font_size=36, color=COLOR_RED).move_to(np.array([cx - 2.5, cy - 1.1, 0]))
        line2 = Line(
            start=np.array([cx - 2.0, cy - 1.4, 0]),
            end=np.array([cx + 1.8, cy - 1.4, 0]),
            color=GRAY_B, stroke_width=2
        )
        vline2 = Line(
            start=np.array([cx - 2.0, cy - 0.4, 0]),
            end=np.array([cx - 2.0, cy - 1.4, 0]),
            color=GRAY_B, stroke_width=2
        )

        q2 = MathTex("2", font_size=36, color=COLOR_HL).move_to(np.array([cx - 0.8, cy - 2.0, 0]))
        q3 = MathTex("3", font_size=36, color=COLOR_HL).move_to(np.array([cx + 0.8, cy - 2.0, 0]))

        self.play(Write(div3), Create(line2), Create(vline2), run_time=0.5)
        self.play(Write(q2), Write(q3), run_time=0.5)
        self.wait(0.5)

        # 读取结果
        # GCF
        gcf_explain = Text("GCF = 左侧公因数之积", font=FONT, font_size=22, color=COLOR_GREEN).move_to(DOWN * 2.0)
        gcf_eq_label = Text("GCF(12,18) = ", font=FONT, font_size=24, color=COLOR_GREEN)
        gcf_eq_val = MathTex(r"2 \times 3 = 6", font_size=28, color=COLOR_GREEN)
        gcf_eq = VGroup(gcf_eq_label, gcf_eq_val).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        # 高亮左侧
        hl_div2 = SurroundingRectangle(div2, color=COLOR_GREEN, buff=0.1, stroke_width=2)
        hl_div3 = SurroundingRectangle(div3, color=COLOR_GREEN, buff=0.1, stroke_width=2)

        self.play(Create(hl_div2), Create(hl_div3), run_time=0.4)
        self.play(FadeIn(gcf_explain), run_time=0.4)
        self.play(FadeIn(gcf_eq, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # LCM
        lcm_explain = Text(
            "LCM = 左侧 x 最后一行之积",
            font=FONT, font_size=22, color=COLOR_ORANGE
        ).move_to(DOWN * 4.5)
        lcm_eq_label = Text("LCM(12,18) = ", font=FONT, font_size=24, color=COLOR_ORANGE)
        lcm_eq_val = MathTex(r"2 \times 3 \times 2 \times 3 = 36", font_size=28, color=COLOR_ORANGE)
        lcm_eq = VGroup(lcm_eq_label, lcm_eq_val).arrange(RIGHT, buff=0.2).move_to(DOWN * 5.5)

        # 高亮底部
        hl_q2 = SurroundingRectangle(q2, color=COLOR_ORANGE, buff=0.1, stroke_width=2)
        hl_q3 = SurroundingRectangle(q3, color=COLOR_ORANGE, buff=0.1, stroke_width=2)

        self.play(Create(hl_q2), Create(hl_q3), run_time=0.4)
        self.play(FadeIn(lcm_explain), run_time=0.4)
        self.play(FadeIn(lcm_eq, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(n12), FadeOut(n18),
            FadeOut(div2), FadeOut(div3),
            FadeOut(line1), FadeOut(line2),
            FadeOut(vline1), FadeOut(vline2),
            FadeOut(q6), FadeOut(q9), FadeOut(q2), FadeOut(q3),
            FadeOut(hl_div2), FadeOut(hl_div3),
            FadeOut(hl_q2), FadeOut(hl_q3),
            FadeOut(gcf_explain), FadeOut(gcf_eq),
            FadeOut(lcm_explain), FadeOut(lcm_eq),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: Venn 图理解 GCF / LCM
    # ------------------------------------------------------------------

    def scene_4_venn_diagram(self):
        title = Text("Venn 图理解", font=FONT, font_size=36, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        subtitle = Text(
            "12 和 18 的素因数分解",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.6)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 两个椭圆
        venn_center = UP * 1.5
        ell_left = Ellipse(width=4.5, height=3.5, color=COLOR_MAIN, stroke_width=3, fill_opacity=0.12, fill_color=COLOR_MAIN)
        ell_left.move_to(venn_center + LEFT * 1.2)
        ell_right = Ellipse(width=4.5, height=3.5, color=COLOR_PURPLE, stroke_width=3, fill_opacity=0.12, fill_color=COLOR_PURPLE)
        ell_right.move_to(venn_center + RIGHT * 1.2)

        label_12 = Text("12", font=FONT, font_size=28, color=COLOR_MAIN, weight=BOLD).move_to(venn_center + LEFT * 3.0 + UP * 1.3)
        label_18 = Text("18", font=FONT, font_size=28, color=COLOR_PURPLE, weight=BOLD).move_to(venn_center + RIGHT * 3.0 + UP * 1.3)

        self.play(Create(ell_left), Create(ell_right), run_time=0.8)
        self.play(Write(label_12), Write(label_18), run_time=0.4)

        # 素因数分布
        # 12 = 2 x 2 x 3   =>  独有: 2    公有: 2, 3    (18独有: 3)
        # 18 = 2 x 3 x 3
        # 左独有 (12独有): 一个 2
        left_only = MathTex("2", font_size=36, color=COLOR_MAIN).move_to(venn_center + LEFT * 2.5)
        # 公共: 2, 3
        common_2 = MathTex("2", font_size=36, color=COLOR_HL).move_to(venn_center + UP * 0.3)
        common_3 = MathTex("3", font_size=36, color=COLOR_HL).move_to(venn_center + DOWN * 0.5)
        # 右独有 (18独有): 一个 3
        right_only = MathTex("3", font_size=36, color=COLOR_PURPLE).move_to(venn_center + RIGHT * 2.5)

        self.play(FadeIn(left_only, scale=1.3), run_time=0.4)
        self.play(FadeIn(common_2, scale=1.3), FadeIn(common_3, scale=1.3), run_time=0.5)
        self.play(FadeIn(right_only, scale=1.3), run_time=0.4)
        self.wait(0.5)

        # GCF 从交集
        gcf_arrow = Arrow(
            start=venn_center + DOWN * 2.0,
            end=venn_center + DOWN * 0.8,
            color=COLOR_GREEN, stroke_width=3, max_tip_length_to_length_ratio=0.2
        )
        gcf_text = Text("GCF = 交集之积", font=FONT, font_size=22, color=COLOR_GREEN).move_to(venn_center + DOWN * 2.5)
        gcf_val_label = Text("GCF = ", font=FONT, font_size=24, color=COLOR_GREEN)
        gcf_val_eq = MathTex(r"2 \times 3 = 6", font_size=28, color=COLOR_GREEN)
        gcf_val = VGroup(gcf_val_label, gcf_val_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.2)

        self.play(GrowArrow(gcf_arrow), FadeIn(gcf_text), run_time=0.5)
        self.play(FadeIn(gcf_val, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # LCM 从全集
        lcm_text = Text("LCM = 全部素因数之积", font=FONT, font_size=22, color=COLOR_ORANGE).move_to(DOWN * 3.5)
        lcm_val_label = Text("LCM = ", font=FONT, font_size=24, color=COLOR_ORANGE)
        lcm_val_eq = MathTex(r"2 \times 2 \times 3 \times 3 = 36", font_size=28, color=COLOR_ORANGE)
        lcm_val = VGroup(lcm_val_label, lcm_val_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.5)

        self.play(FadeIn(lcm_text), run_time=0.4)
        self.play(FadeIn(lcm_val, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 关键关系
        relation_box = RoundedRectangle(
            width=7.0, height=1.2, corner_radius=0.2,
            stroke_color=COLOR_PINK, stroke_width=2, fill_color=BG_COLOR, fill_opacity=0.9
        ).move_to(DOWN * 6.2)

        relation_label = Text("重要关系: ", font=FONT, font_size=22, color=COLOR_PINK)
        relation_eq = MathTex(
            r"\text{GCF} \times \text{LCM} = 12 \times 18",
            font_size=24, color=COLOR_PINK
        )
        relation = VGroup(relation_label, relation_eq).arrange(RIGHT, buff=0.2).move_to(DOWN * 6.2)

        self.play(FadeIn(relation_box), FadeIn(relation), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(ell_left), FadeOut(ell_right),
            FadeOut(label_12), FadeOut(label_18),
            FadeOut(left_only), FadeOut(common_2), FadeOut(common_3), FadeOut(right_only),
            FadeOut(gcf_arrow), FadeOut(gcf_text), FadeOut(gcf_val),
            FadeOut(lcm_text), FadeOut(lcm_val),
            FadeOut(relation_box), FadeOut(relation),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 三个数的 GCF / LCM
    # ------------------------------------------------------------------

    def scene_5_three_numbers(self):
        title = Text("三个数的情况", font=FONT, font_size=36, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        subtitle = Text(
            "求 GCF(12, 18, 24) 和 LCM(12, 18, 24)",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 分解素因数
        f12_label = Text("12 = ", font=FONT, font_size=26, color=COLOR_MAIN)
        f12_eq = MathTex(r"2^2 \times 3", font_size=30, color=WHITE)
        f12 = VGroup(f12_label, f12_eq).arrange(RIGHT, buff=0.15).move_to(UP * 3.2)

        f18_label = Text("18 = ", font=FONT, font_size=26, color=COLOR_PURPLE)
        f18_eq = MathTex(r"2 \times 3^2", font_size=30, color=WHITE)
        f18 = VGroup(f18_label, f18_eq).arrange(RIGHT, buff=0.15).move_to(UP * 2.2)

        f24_label = Text("24 = ", font=FONT, font_size=26, color=COLOR_ORANGE)
        f24_eq = MathTex(r"2^3 \times 3", font_size=30, color=WHITE)
        f24 = VGroup(f24_label, f24_eq).arrange(RIGHT, buff=0.15).move_to(UP * 1.2)

        self.play(FadeIn(f12, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(f18, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(f24, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(0.5)

        # GCF: 最低次幂
        gcf_title = Text("GCF: 取公有素因数最低次幂", font=FONT, font_size=22, color=COLOR_GREEN).move_to(DOWN * 0.2)

        gcf_step_label = Text("GCF = ", font=FONT, font_size=24, color=COLOR_GREEN)
        gcf_step_eq = MathTex(r"2^1 \times 3^1 = 6", font_size=28, color=COLOR_GREEN)
        gcf_step = VGroup(gcf_step_label, gcf_step_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.2)

        self.play(FadeIn(gcf_title, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(gcf_step, scale=1.1), run_time=0.6)
        self.wait(0.6)

        # LCM: 最高次幂
        lcm_title = Text("LCM: 取所有素因数最高次幂", font=FONT, font_size=22, color=COLOR_ORANGE).move_to(DOWN * 2.8)

        lcm_step_label = Text("LCM = ", font=FONT, font_size=24, color=COLOR_ORANGE)
        lcm_step_eq = MathTex(r"2^3 \times 3^2 = 72", font_size=28, color=COLOR_ORANGE)
        lcm_step = VGroup(lcm_step_label, lcm_step_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 3.8)

        self.play(FadeIn(lcm_title, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(lcm_step, scale=1.1), run_time=0.6)
        self.wait(0.5)

        # 验证
        check_text = Text(
            "验证: 6 是 12, 18, 24 的公因数",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 5.2)
        check_eq = MathTex(
            r"12 \div 6 = 2,\ 18 \div 6 = 3,\ 24 \div 6 = 4",
            font_size=24, color=GRAY_A
        ).move_to(DOWN * 6.0)

        self.play(FadeIn(check_text), FadeIn(check_eq), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(f12), FadeOut(f18), FadeOut(f24),
            FadeOut(gcf_title), FadeOut(gcf_step),
            FadeOut(lcm_title), FadeOut(lcm_step),
            FadeOut(check_text), FadeOut(check_eq),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 互素概念
    # ------------------------------------------------------------------

    def scene_6_coprime(self):
        title = Text("互素 (互质)", font=FONT, font_size=36, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 定义
        def_box = RoundedRectangle(
            width=7.5, height=2.0, corner_radius=0.3,
            stroke_color=COLOR_HL, stroke_width=2, fill_color=BG_COLOR, fill_opacity=0.9
        ).move_to(UP * 3.5)

        def_text = Text(
            "两个数的公因数只有 1",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 3.8)

        def_text2 = Text(
            "则称这两个数互素 (互质)",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 3.1)

        self.play(FadeIn(def_box), Write(def_text), Write(def_text2), run_time=0.7)
        self.wait(0.5)

        # 示例
        ex_title = Text("例子:", font=FONT, font_size=24, color=GRAY_A).move_to(UP * 1.8 + LEFT * 2.5)

        # 互素
        ex1_label = Text("8 和 15 互素", font=FONT, font_size=24, color=COLOR_GREEN)
        ex1_check = MathTex(r"\text{GCF}(8, 15) = 1", font_size=26, color=COLOR_GREEN)
        ex1 = VGroup(ex1_label, ex1_check).arrange(RIGHT, buff=0.5).move_to(UP * 0.8)

        ex2_label = Text("7 和 12 互素", font=FONT, font_size=24, color=COLOR_GREEN)
        ex2_check = MathTex(r"\text{GCF}(7, 12) = 1", font_size=26, color=COLOR_GREEN)
        ex2 = VGroup(ex2_label, ex2_check).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.2)

        # 不互素
        ex3_label = Text("6 和 9 不互素", font=FONT, font_size=24, color=COLOR_RED)
        ex3_check = MathTex(r"\text{GCF}(6, 9) = 3", font_size=26, color=COLOR_RED)
        ex3 = VGroup(ex3_label, ex3_check).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.5)

        self.play(FadeIn(ex_title), run_time=0.3)
        self.play(FadeIn(ex1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(ex2, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(ex3, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)

        # 重要性质
        prop_box = RoundedRectangle(
            width=7.5, height=3.0, corner_radius=0.3,
            stroke_color=COLOR_PURPLE, stroke_width=2, fill_color=BG_COLOR, fill_opacity=0.9
        ).move_to(DOWN * 4.2)

        prop_title = Text("互素的重要性质", font=FONT, font_size=24, color=COLOR_PURPLE, weight=BOLD).move_to(DOWN * 3.2)

        prop1 = Text(
            "1. 两个素数一定互素",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 4.0)

        prop2 = Text(
            "2. 1 与任何正整数互素",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 4.8)

        prop3 = Text(
            "3. 互素时 LCM = 两数之积",
            font=FONT, font_size=20, color=COLOR_HL
        ).move_to(DOWN * 5.6)

        self.play(FadeIn(prop_box), Write(prop_title), run_time=0.5)
        self.play(FadeIn(prop1, shift=RIGHT * 0.2), run_time=0.4)
        self.play(FadeIn(prop2, shift=RIGHT * 0.2), run_time=0.4)
        self.play(FadeIn(prop3, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def_box), FadeOut(def_text), FadeOut(def_text2),
            FadeOut(ex_title), FadeOut(ex1), FadeOut(ex2), FadeOut(ex3),
            FadeOut(prop_box), FadeOut(prop_title),
            FadeOut(prop1), FadeOut(prop2), FadeOut(prop3),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 应用题 (裁布问题)
    # ------------------------------------------------------------------

    def scene_7_application(self):
        title = Text("应用题", font=FONT, font_size=36, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 题目
        q_box = RoundedRectangle(
            width=7.5, height=3.0, corner_radius=0.3,
            stroke_color=COLOR_MAIN, stroke_width=2, fill_color=BG_COLOR, fill_opacity=0.9
        ).move_to(UP * 3.2)

        q_line1 = Text(
            "一块长 36 厘米、宽 24 厘米",
            font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 3.8)
        q_line2 = Text(
            "的长方形纸, 裁成同样大小的",
            font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 3.2)
        q_line3 = Text(
            "正方形而没有剩余,",
            font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 2.6)
        q_line4 = Text(
            "正方形的边长最大是多少?",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(UP * 2.0)

        self.play(
            FadeIn(q_box),
            Write(q_line1), Write(q_line2),
            Write(q_line3), Write(q_line4),
            run_time=1.0
        )
        self.wait(0.8)

        # 分析
        analysis = Text(
            "正方形边长必须同时整除 36 和 24",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 0.5)

        arrow_text = Text(
            "=> 求 GCF(36, 24)",
            font=FONT, font_size=24, color=COLOR_GREEN
        ).move_to(DOWN * 0.4)

        self.play(FadeIn(analysis, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(arrow_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 短除法过程 (36 和 24)
        sd_center_x, sd_center_y = 0, -2.0

        sd_n36 = MathTex("36", font_size=32, color=WHITE).move_to(np.array([sd_center_x - 0.8, sd_center_y, 0]))
        sd_n24 = MathTex("24", font_size=32, color=WHITE).move_to(np.array([sd_center_x + 0.8, sd_center_y, 0]))

        sd_d2 = MathTex("2", font_size=32, color=COLOR_RED).move_to(np.array([sd_center_x - 2.3, sd_center_y - 0.1, 0]))
        sd_l1 = Line(np.array([sd_center_x - 1.8, sd_center_y - 0.35, 0]),
                      np.array([sd_center_x + 1.6, sd_center_y - 0.35, 0]),
                      color=GRAY_B, stroke_width=2)
        sd_v1 = Line(np.array([sd_center_x - 1.8, sd_center_y + 0.25, 0]),
                      np.array([sd_center_x - 1.8, sd_center_y - 0.35, 0]),
                      color=GRAY_B, stroke_width=2)

        sd_q18 = MathTex("18", font_size=32, color=WHITE).move_to(np.array([sd_center_x - 0.8, sd_center_y - 0.85, 0]))
        sd_q12 = MathTex("12", font_size=32, color=WHITE).move_to(np.array([sd_center_x + 0.8, sd_center_y - 0.85, 0]))

        sd_d3 = MathTex("2", font_size=32, color=COLOR_RED).move_to(np.array([sd_center_x - 2.3, sd_center_y - 0.95, 0]))
        sd_l2 = Line(np.array([sd_center_x - 1.8, sd_center_y - 1.2, 0]),
                      np.array([sd_center_x + 1.6, sd_center_y - 1.2, 0]),
                      color=GRAY_B, stroke_width=2)
        sd_v2 = Line(np.array([sd_center_x - 1.8, sd_center_y - 0.35, 0]),
                      np.array([sd_center_x - 1.8, sd_center_y - 1.2, 0]),
                      color=GRAY_B, stroke_width=2)

        sd_q9 = MathTex("9", font_size=32, color=WHITE).move_to(np.array([sd_center_x - 0.8, sd_center_y - 1.7, 0]))
        sd_q6 = MathTex("6", font_size=32, color=WHITE).move_to(np.array([sd_center_x + 0.8, sd_center_y - 1.7, 0]))

        sd_d33 = MathTex("3", font_size=32, color=COLOR_RED).move_to(np.array([sd_center_x - 2.3, sd_center_y - 1.8, 0]))
        sd_l3 = Line(np.array([sd_center_x - 1.8, sd_center_y - 2.05, 0]),
                      np.array([sd_center_x + 1.6, sd_center_y - 2.05, 0]),
                      color=GRAY_B, stroke_width=2)
        sd_v3 = Line(np.array([sd_center_x - 1.8, sd_center_y - 1.2, 0]),
                      np.array([sd_center_x - 1.8, sd_center_y - 2.05, 0]),
                      color=GRAY_B, stroke_width=2)

        sd_q3f = MathTex("3", font_size=32, color=COLOR_HL).move_to(np.array([sd_center_x - 0.8, sd_center_y - 2.5, 0]))
        sd_q2f = MathTex("2", font_size=32, color=COLOR_HL).move_to(np.array([sd_center_x + 0.8, sd_center_y - 2.5, 0]))

        # 动画: 短除法逐步
        self.play(Write(sd_n36), Write(sd_n24), run_time=0.4)
        self.play(Write(sd_d2), Create(sd_l1), Create(sd_v1), run_time=0.4)
        self.play(Write(sd_q18), Write(sd_q12), run_time=0.4)
        self.play(Write(sd_d3), Create(sd_l2), Create(sd_v2), run_time=0.4)
        self.play(Write(sd_q9), Write(sd_q6), run_time=0.4)
        self.play(Write(sd_d33), Create(sd_l3), Create(sd_v3), run_time=0.4)
        self.play(Write(sd_q3f), Write(sd_q2f), run_time=0.4)
        self.wait(0.5)

        # 结果
        ans_label = Text("GCF(36,24) = ", font=FONT, font_size=24, color=COLOR_GREEN)
        ans_eq = MathTex(r"2 \times 2 \times 3 = 12", font_size=28, color=COLOR_GREEN)
        ans = VGroup(ans_label, ans_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.5)

        self.play(FadeIn(ans, scale=1.1), run_time=0.6)

        answer = Text(
            "正方形边长最大为 12 厘米",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        all_sd = VGroup(
            sd_n36, sd_n24, sd_d2, sd_l1, sd_v1,
            sd_q18, sd_q12, sd_d3, sd_l2, sd_v2,
            sd_q9, sd_q6, sd_d33, sd_l3, sd_v3,
            sd_q3f, sd_q2f
        )
        self.play(
            FadeOut(title), FadeOut(q_box),
            FadeOut(q_line1), FadeOut(q_line2), FadeOut(q_line3), FadeOut(q_line4),
            FadeOut(analysis), FadeOut(arrow_text),
            FadeOut(all_sd), FadeOut(ans), FadeOut(answer),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结 + 片尾
    # ------------------------------------------------------------------

    def scene_8_summary_and_outro(self):
        # 总结
        sum_title = Text("总结", font=FONT, font_size=40, color=COLOR_HL, weight=BOLD).move_to(UP * 5.5)
        self.play(Write(sum_title), run_time=0.5)

        # 总结卡片
        cards_data = [
            ("分解素因数法", "分别分解, 再比较素因数的幂次", COLOR_MAIN),
            ("短除法", "连续除以公因数, 快速高效", COLOR_PURPLE),
            ("GCF 方法", "取公有素因数的最低次幂之积", COLOR_GREEN),
            ("LCM 方法", "取所有素因数的最高次幂之积", COLOR_ORANGE),
            ("互素", "GCF=1 时两数互素, LCM=两数之积", COLOR_PINK),
        ]

        cards = VGroup()
        for i, (t, desc, color) in enumerate(cards_data):
            dot = Dot(radius=0.08, color=color)
            t_text = Text(t, font=FONT, font_size=22, color=color, weight=BOLD)
            d_text = Text(desc, font=FONT, font_size=18, color=GRAY_A)
            row = VGroup(dot, t_text, d_text).arrange(RIGHT, buff=0.3)
            cards.add(row)

        cards.arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 1.5)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(1.0)

        # 关键公式
        formula_box = RoundedRectangle(
            width=7.5, height=1.6, corner_radius=0.3,
            stroke_color=COLOR_HL, stroke_width=2, fill_color=BG_COLOR, fill_opacity=0.9
        ).move_to(DOWN * 2.5)

        formula_label = Text("重要公式: ", font=FONT, font_size=22, color=COLOR_HL)
        formula_eq = MathTex(
            r"a \times b = \text{GCF}(a,b) \times \text{LCM}(a,b)",
            font_size=26, color=WHITE
        )
        formula = VGroup(formula_label, formula_eq).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.5)

        self.play(FadeIn(formula_box), FadeIn(formula), run_time=0.6)
        self.wait(1.5)

        # 清理总结
        self.play(
            FadeOut(sum_title), FadeOut(cards),
            FadeOut(formula_box), FadeOut(formula),
            run_time=0.6
        )

        # 片尾
        outro_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE, weight=BOLD
        ).move_to(UP * 1.5)

        outro_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.5)

        outro_cta = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)

        self.play(
            Transform(self.author, outro_name),
            run_time=0.8
        )
        self.play(FadeIn(outro_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(outro_cta, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author),
            FadeOut(outro_id),
            FadeOut(outro_cta),
            run_time=1.0
        )

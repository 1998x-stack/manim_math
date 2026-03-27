"""
002_同分母分数的加减法.py — 同分母分数的加减法 教学动画

知识点: 同分母分数的加减法
  - 核心规则: 分母不变, 分子相加减
  - 算理: 几个分数单位加上几个分数单位
  - 例1: 1/3 + 2/3 = 3/3 = 1
  - 例2: 4/5 - 2/5 = 2/5
年级: 三年级上册
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
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
BG_COLOR    = "#1a1a2e"
COLOR_FRAC1 = "#3b82f6"   # 蓝色  — 第一个分数
COLOR_FRAC2 = "#22c55e"   # 绿色  — 第二个分数
COLOR_HL    = "#fbbf24"   # 黄色  — 高亮
COLOR_RES   = "#f97316"   # 橙色  — 结果
COLOR_RULE  = "#a78bfa"   # 紫色  — 规则框
COLOR_DENOM = "#6b7280"   # 灰色  — 分母(不变)
COLOR_NUMER = "#f43f5e"   # 红色  — 分子(相加减)
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


# ======================================================================
# 辅助函数: 绘制一个圆形"饼图"分数示意
# ======================================================================

def make_pie(n_parts, filled_parts, radius=1.2,
             fill_col="#3b82f6", line_col=WHITE, bg_col="#1a1a2e"):
    """
    将圆分成 n_parts 等份, 填充其中 filled_parts 份.
    返回 VGroup.
    """
    pieces = VGroup()
    for i in range(n_parts):
        start_angle = PI / 2 + i * TAU / n_parts
        end_angle   = PI / 2 + (i + 1) * TAU / n_parts
        angle_span  = TAU / n_parts

        # 扇形用多边形近似 (避免 inner_radius / outer_radius)
        pts = [ORIGIN]
        n_steps = max(20, int(24 * angle_span / TAU))
        for k in range(n_steps + 1):
            a = start_angle + k * angle_span / n_steps
            pts.append(np.array([radius * np.cos(a), radius * np.sin(a), 0]))

        sector = Polygon(
            *pts,
            stroke_width=2,
            stroke_color=line_col,
            fill_color=fill_col if i < filled_parts else bg_col,
            fill_opacity=0.85 if i < filled_parts else 0.18,
        )
        pieces.add(sector)
    # 外圆轮廓
    outline = Circle(radius=radius, color=line_col, stroke_width=2.5, fill_opacity=0)
    pieces.add(outline)
    return pieces


def make_bar(n_parts, filled_parts, width=5.5, height=0.85,
             fill_col="#3b82f6", line_col=WHITE, bg_col="#1a1a2e"):
    """
    将长方形分成 n_parts 等份, 填充其中 filled_parts 份.
    返回 VGroup, 中心在 ORIGIN.
    """
    cell_w = width / n_parts
    bars = VGroup()
    for i in range(n_parts):
        x_left = -width / 2 + i * cell_w
        rect = Rectangle(
            width=cell_w, height=height,
            stroke_width=2, stroke_color=line_col,
            fill_color=fill_col if i < filled_parts else bg_col,
            fill_opacity=0.85 if i < filled_parts else 0.18,
        )
        rect.move_to(np.array([x_left + cell_w / 2, 0, 0]))
        bars.add(rect)
    return bars


# ======================================================================
# 主场景
# ======================================================================

class SameDenomFractionLesson(Scene):
    """
    同分母分数的加减法教学动画
    场景顺序:
      1. 开场钩子
      2. 回顾分数单位
      3. 加法例题: 1/3 + 2/3  (饼图演示算理)
      4. 加法规则提炼
      5. 减法例题: 4/5 - 2/5  (条形演示算理)
      6. 减法规则提炼
      7. 知识总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_fraction_unit()
        self.scene_3_addition_demo()
        self.scene_4_addition_rule()
        self.scene_5_subtraction_demo()
        self.scene_6_subtraction_rule()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 工具
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def section_title(self, text, color=WHITE, font_size=34):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.5)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "同分母分数怎么加减?",
            font=FONT, font_size=40, color=COLOR_HL,
        ).move_to(UP * 5.0)

        sub = Text(
            "其实超级简单, 一起来看!",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.2)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 展示两道题引发好奇
        q1 = VGroup(
            MathTex(r"\frac{1}{3}", font_size=72, color=COLOR_FRAC1),
            Text("+", font=FONT, font_size=44, color=WHITE),
            MathTex(r"\frac{2}{3}", font_size=72, color=COLOR_FRAC2),
            Text("= ?", font=FONT, font_size=44, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)

        q2 = VGroup(
            MathTex(r"\frac{4}{5}", font_size=72, color=COLOR_FRAC1),
            Text("-", font=FONT, font_size=44, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=72, color=COLOR_FRAC2),
            Text("= ?", font=FONT, font_size=44, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)

        self.play(FadeIn(q1, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(q2, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(sub), FadeOut(q1), FadeOut(q2),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 回顾分数单位
    # ------------------------------------------------------------------

    def scene_2_fraction_unit(self):
        title = self.section_title("回顾: 什么是分数单位?", color=COLOR_FRAC1)
        self.play(Write(title), run_time=0.6)

        # 画一个 1/3 的饼图
        pie3 = make_pie(3, 1, radius=1.4, fill_col=COLOR_FRAC1)
        pie3.move_to(UP * 2.5)
        self.play(FadeIn(pie3, scale=0.8), run_time=0.8)

        lbl_frac = MathTex(r"\frac{1}{3}", font_size=56, color=COLOR_FRAC1).move_to(UP * 0.5)
        lbl_unit = Text("这是一个分数单位", font=FONT, font_size=26, color=GRAY_A).move_to(DOWN * 0.2)
        self.play(Write(lbl_frac), run_time=0.5)
        self.play(FadeIn(lbl_unit), run_time=0.4)

        # 说明: 2/3 就是 2 个 1/3
        pie3_2 = make_pie(3, 2, radius=1.4, fill_col=COLOR_FRAC2)
        pie3_2.move_to(UP * 2.5)

        desc = Text("2/3 = 2 个 1/3", font=FONT, font_size=26, color=COLOR_FRAC2).move_to(DOWN * 1.0)
        lbl_frac2 = MathTex(r"\frac{2}{3}", font_size=56, color=COLOR_FRAC2).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(pie3, pie3_2),
            ReplacementTransform(lbl_frac, lbl_frac2),
            run_time=0.8,
        )
        self.play(FadeIn(desc), run_time=0.4)
        self.wait(1.5)

        # 关键提示
        key = Text(
            "分数单位: 分母相同, 每份大小相等",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(pie3_2),
            FadeOut(lbl_frac2), FadeOut(lbl_unit),
            FadeOut(desc), FadeOut(key),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 加法例题  1/3 + 2/3
    # ------------------------------------------------------------------

    def scene_3_addition_demo(self):
        title = self.section_title("加法演示", color=COLOR_FRAC1)
        self.play(Write(title), run_time=0.6)

        # 展示算式
        formula_row = VGroup(
            MathTex(r"\frac{1}{3}", font_size=64, color=COLOR_FRAC1),
            Text("+", font=FONT, font_size=40, color=WHITE),
            MathTex(r"\frac{2}{3}", font_size=64, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=40, color=WHITE),
            Text("?", font=FONT, font_size=40, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 4.2)

        self.play(FadeIn(formula_row), run_time=0.6)

        # --- 饼图区 ---
        # 左边: 1/3 的饼
        pie_a = make_pie(3, 1, radius=1.15, fill_col=COLOR_FRAC1)
        pie_a.move_to(LEFT * 2.7 + UP * 2.0)

        label_a = MathTex(r"\frac{1}{3}", font_size=44, color=COLOR_FRAC1)
        label_a.next_to(pie_a, DOWN, buff=0.2)

        # 右边: 2/3 的饼
        pie_b = make_pie(3, 2, radius=1.15, fill_col=COLOR_FRAC2)
        pie_b.move_to(RIGHT * 2.7 + UP * 2.0)

        label_b = MathTex(r"\frac{2}{3}", font_size=44, color=COLOR_FRAC2)
        label_b.next_to(pie_b, DOWN, buff=0.2)

        plus_mid = Text("+", font=FONT, font_size=36, color=WHITE).move_to(UP * 2.0)

        self.play(
            FadeIn(pie_a, scale=0.8), FadeIn(label_a),
            FadeIn(plus_mid),
            FadeIn(pie_b, scale=0.8), FadeIn(label_b),
            run_time=0.8,
        )
        self.wait(0.5)

        # 动画: 把两个饼合成一个整圆
        # 先显示说明
        step1 = Text(
            "1 个分数单位 + 2 个分数单位",
            font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.5)

        step2 = Text(
            "= 3 个分数单位",
            font=FONT, font_size=26, color=COLOR_RES,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(step2), run_time=0.4)

        # 合并动画: 两个饼移到中心, 变成整圆
        pie_full = make_pie(3, 3, radius=1.3, fill_col=COLOR_RES)
        pie_full.move_to(UP * 2.0)

        self.play(
            ReplacementTransform(pie_a, pie_full),
            FadeOut(pie_b),
            FadeOut(plus_mid),
            run_time=1.0,
        )

        label_full = MathTex(r"\frac{3}{3}", font_size=48, color=COLOR_RES)
        label_full.next_to(pie_full, DOWN, buff=0.2)

        self.play(
            ReplacementTransform(label_a, label_full),
            FadeOut(label_b),
            run_time=0.5,
        )
        self.wait(0.5)

        # 化简 3/3 = 1
        step3 = VGroup(
            MathTex(r"\frac{3}{3}", font_size=48, color=COLOR_RES),
            Text("=", font=FONT, font_size=32, color=WHITE),
            MathTex(r"1", font_size=56, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 2.2)

        self.play(FadeIn(step3, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        # 完整答案
        answer_row = VGroup(
            MathTex(r"\frac{1}{3}", font_size=56, color=COLOR_FRAC1),
            Text("+", font=FONT, font_size=36, color=WHITE),
            MathTex(r"\frac{2}{3}", font_size=56, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=36, color=WHITE),
            MathTex(r"\frac{3}{3}", font_size=56, color=COLOR_RES),
            Text("=", font=FONT, font_size=36, color=WHITE),
            MathTex(r"1", font_size=64, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 3.8)

        self.play(FadeIn(answer_row, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(formula_row),
            FadeOut(pie_full), FadeOut(label_full),
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeOut(answer_row),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 加法规则提炼
    # ------------------------------------------------------------------

    def scene_4_addition_rule(self):
        title = self.section_title("加法规则", color=COLOR_RULE)
        self.play(Write(title), run_time=0.6)

        # 展示算式, 分步拆解
        frac1 = MathTex(r"\frac{1}{3}", font_size=64, color=COLOR_FRAC1)
        plus  = Text("+", font=FONT, font_size=40, color=WHITE)
        frac2 = MathTex(r"\frac{2}{3}", font_size=64, color=COLOR_FRAC2)
        eq    = Text("=", font=FONT, font_size=40, color=WHITE)
        frac3 = MathTex(r"\frac{1+2}{3}", font_size=64, color=COLOR_RES)
        eq2   = Text("=", font=FONT, font_size=40, color=WHITE)
        result = MathTex(r"\frac{3}{3}", font_size=64, color=COLOR_RES)

        row = VGroup(frac1, plus, frac2, eq, frac3, eq2, result)
        row.arrange(RIGHT, buff=0.18).move_to(UP * 3.5)
        self.play(FadeIn(row), run_time=0.7)

        # 框出"分子相加"
        brace_numer = Brace(frac3[0][0], direction=UP, color=COLOR_NUMER)
        brace_numer_lbl = Text("分子相加", font=FONT, font_size=20, color=COLOR_NUMER)
        brace_numer_lbl.next_to(brace_numer, UP, buff=0.1)
        self.play(FadeIn(brace_numer), FadeIn(brace_numer_lbl), run_time=0.5)

        # 框出"分母不变"
        brace_denom = Brace(frac3[0][0], direction=DOWN, color=COLOR_DENOM)
        brace_denom_lbl = Text("分母不变", font=FONT, font_size=20, color=COLOR_DENOM)
        brace_denom_lbl.next_to(brace_denom, DOWN, buff=0.1)
        self.play(FadeIn(brace_denom), FadeIn(brace_denom_lbl), run_time=0.5)

        self.wait(1.0)

        # 规则卡片
        card = RoundedRectangle(
            width=7.2, height=3.0,
            corner_radius=0.3,
            color=COLOR_RULE,
            stroke_width=2.5,
            fill_color=COLOR_RULE,
            fill_opacity=0.08,
        ).move_to(UP * 0.3)

        rule_title = Text("同分母分数相加", font=FONT, font_size=26, color=COLOR_RULE)
        rule_body = VGroup(
            Text("分母", font=FONT, font_size=24, color=COLOR_DENOM),
            Text("不变,", font=FONT, font_size=24, color=WHITE),
            Text("分子", font=FONT, font_size=24, color=COLOR_NUMER),
            Text("相加", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.12)

        rule_formula = VGroup(
            MathTex(r"\frac{a}{n}", font_size=48, color=COLOR_FRAC1),
            Text("+", font=FONT, font_size=32, color=WHITE),
            MathTex(r"\frac{b}{n}", font_size=48, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=32, color=WHITE),
            MathTex(r"\frac{a+b}{n}", font_size=48, color=COLOR_RES),
        ).arrange(RIGHT, buff=0.18)

        card_content = VGroup(rule_title, rule_body, rule_formula)
        card_content.arrange(DOWN, buff=0.3).move_to(UP * 0.3)

        self.play(FadeIn(card), run_time=0.4)
        self.play(FadeIn(card_content, shift=UP * 0.2), run_time=0.6)

        # 强调关键词
        self.play(Indicate(rule_body[0], color=COLOR_DENOM, scale_factor=1.3), run_time=0.5)
        self.play(Indicate(rule_body[2], color=COLOR_NUMER, scale_factor=1.3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(row),
            FadeOut(brace_numer), FadeOut(brace_numer_lbl),
            FadeOut(brace_denom), FadeOut(brace_denom_lbl),
            FadeOut(card), FadeOut(card_content),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 减法例题  4/5 - 2/5
    # ------------------------------------------------------------------

    def scene_5_subtraction_demo(self):
        title = self.section_title("减法演示", color=COLOR_FRAC2)
        self.play(Write(title), run_time=0.6)

        formula_row = VGroup(
            MathTex(r"\frac{4}{5}", font_size=64, color=COLOR_FRAC1),
            Text("-", font=FONT, font_size=40, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=64, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=40, color=WHITE),
            Text("?", font=FONT, font_size=40, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 4.2)

        self.play(FadeIn(formula_row), run_time=0.6)

        # --- 条形图区 ---
        bar_full = make_bar(5, 4, width=6.0, height=0.9, fill_col=COLOR_FRAC1)
        bar_full.move_to(UP * 2.8)

        lbl_bar = MathTex(r"\frac{4}{5}", font_size=44, color=COLOR_FRAC1)
        lbl_bar.next_to(bar_full, DOWN, buff=0.25)

        self.play(FadeIn(bar_full, scale=0.9), FadeIn(lbl_bar), run_time=0.7)
        self.wait(0.4)

        # 说明: 4 个 1/5
        step1 = Text(
            "4/5 有 4 个分数单位 1/5",
            font=FONT, font_size=24, color=COLOR_FRAC1,
        ).move_to(UP * 1.5)
        self.play(FadeIn(step1), run_time=0.4)
        self.wait(0.5)

        # 划掉后两格 (减去 2/5)
        # 用一个覆盖矩形模拟"划掉"
        cell_w = 6.0 / 5
        # 前 4 格填充: 第3、4格(索引2、3)是要被减掉的 2/5
        # 重新画: 4格中把后2格变暗
        bar_after = make_bar(5, 2, width=6.0, height=0.9, fill_col=COLOR_RES)
        bar_after.move_to(UP * 2.8)

        # 在第3、4格上画斜线标记
        x_start_remove = -6.0 / 2 + 2 * cell_w
        cross_lines = VGroup()
        for i in range(2):
            x0 = x_start_remove + i * cell_w
            x1 = x0 + cell_w
            y0 = 2.8 - 0.45
            y1 = 2.8 + 0.45
            cl1 = Line(np.array([x0, y0, 0]), np.array([x1, y1, 0]),
                       color=COLOR_FRAC2, stroke_width=3)
            cl2 = Line(np.array([x0, y1, 0]), np.array([x1, y0, 0]),
                       color=COLOR_FRAC2, stroke_width=3)
            cross_lines.add(cl1, cl2)

        step2 = Text(
            "去掉 2 个分数单位 (减去 2/5)",
            font=FONT, font_size=24, color=COLOR_FRAC2,
        ).move_to(UP * 0.7)

        self.play(FadeIn(step2), run_time=0.4)
        self.play(
            ReplacementTransform(bar_full, bar_after),
            FadeIn(cross_lines),
            run_time=0.8,
        )
        self.wait(0.5)

        # 结果
        bar_result = make_bar(5, 2, width=6.0, height=0.9, fill_col=COLOR_RES)
        bar_result.move_to(UP * 2.8)

        step3 = Text(
            "还剩 2 个分数单位 = 2/5",
            font=FONT, font_size=26, color=COLOR_RES,
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(step3), run_time=0.4)

        lbl_result = MathTex(r"\frac{2}{5}", font_size=48, color=COLOR_RES)
        lbl_result.next_to(bar_after, DOWN, buff=0.25)
        self.play(
            ReplacementTransform(lbl_bar, lbl_result),
            FadeOut(cross_lines),
            run_time=0.6,
        )
        self.wait(0.8)

        # 完整答案
        answer_row = VGroup(
            MathTex(r"\frac{4}{5}", font_size=56, color=COLOR_FRAC1),
            Text("-", font=FONT, font_size=36, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=56, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=36, color=WHITE),
            MathTex(r"\frac{4-2}{5}", font_size=56, color=COLOR_RES),
            Text("=", font=FONT, font_size=36, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=64, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.16).move_to(DOWN * 2.5)

        self.play(FadeIn(answer_row, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(formula_row),
            FadeOut(bar_after), FadeOut(lbl_result),
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeOut(answer_row),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 减法规则提炼
    # ------------------------------------------------------------------

    def scene_6_subtraction_rule(self):
        title = self.section_title("减法规则", color=COLOR_RULE)
        self.play(Write(title), run_time=0.6)

        frac1 = MathTex(r"\frac{4}{5}", font_size=64, color=COLOR_FRAC1)
        minus = Text("-", font=FONT, font_size=40, color=WHITE)
        frac2 = MathTex(r"\frac{2}{5}", font_size=64, color=COLOR_FRAC2)
        eq    = Text("=", font=FONT, font_size=40, color=WHITE)
        frac3 = MathTex(r"\frac{4-2}{5}", font_size=64, color=COLOR_RES)
        eq2   = Text("=", font=FONT, font_size=40, color=WHITE)
        result = MathTex(r"\frac{2}{5}", font_size=64, color=COLOR_HL)

        row = VGroup(frac1, minus, frac2, eq, frac3, eq2, result)
        row.arrange(RIGHT, buff=0.16).move_to(UP * 3.5)
        self.play(FadeIn(row), run_time=0.7)

        # 箭头指出分子相减
        arr_numer = Arrow(
            frac3.get_top() + UP * 0.2,
            frac3.get_top() + UP * 0.8,
            color=COLOR_NUMER, stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
        )
        arr_numer_lbl = Text("分子相减", font=FONT, font_size=20, color=COLOR_NUMER)
        arr_numer_lbl.next_to(arr_numer, UP, buff=0.05)
        self.play(FadeIn(arr_numer), FadeIn(arr_numer_lbl), run_time=0.5)

        # 箭头指出分母不变
        arr_denom = Arrow(
            frac3.get_bottom() + DOWN * 0.2,
            frac3.get_bottom() + DOWN * 0.8,
            color=COLOR_DENOM, stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
        )
        arr_denom_lbl = Text("分母不变", font=FONT, font_size=20, color=COLOR_DENOM)
        arr_denom_lbl.next_to(arr_denom, DOWN, buff=0.05)
        self.play(FadeIn(arr_denom), FadeIn(arr_denom_lbl), run_time=0.5)

        self.wait(1.0)

        # 规则卡片
        card = RoundedRectangle(
            width=7.2, height=3.0,
            corner_radius=0.3,
            color=COLOR_RULE,
            stroke_width=2.5,
            fill_color=COLOR_RULE,
            fill_opacity=0.08,
        ).move_to(UP * 0.2)

        rule_title = Text("同分母分数相减", font=FONT, font_size=26, color=COLOR_RULE)
        rule_body = VGroup(
            Text("分母", font=FONT, font_size=24, color=COLOR_DENOM),
            Text("不变,", font=FONT, font_size=24, color=WHITE),
            Text("分子", font=FONT, font_size=24, color=COLOR_NUMER),
            Text("相减", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.12)

        rule_formula = VGroup(
            MathTex(r"\frac{a}{n}", font_size=48, color=COLOR_FRAC1),
            Text("-", font=FONT, font_size=32, color=WHITE),
            MathTex(r"\frac{b}{n}", font_size=48, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=32, color=WHITE),
            MathTex(r"\frac{a-b}{n}", font_size=48, color=COLOR_RES),
        ).arrange(RIGHT, buff=0.18)

        card_content = VGroup(rule_title, rule_body, rule_formula)
        card_content.arrange(DOWN, buff=0.3).move_to(UP * 0.2)

        self.play(FadeIn(card), run_time=0.4)
        self.play(FadeIn(card_content, shift=UP * 0.2), run_time=0.6)

        self.play(Indicate(rule_body[0], color=COLOR_DENOM, scale_factor=1.3), run_time=0.5)
        self.play(Indicate(rule_body[2], color=COLOR_NUMER, scale_factor=1.3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(row),
            FadeOut(arr_numer), FadeOut(arr_numer_lbl),
            FadeOut(arr_denom), FadeOut(arr_denom_lbl),
            FadeOut(card), FadeOut(card_content),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 知识总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = self.section_title("知识总结", color=COLOR_HL)
        self.play(Write(title), run_time=0.6)

        card_bg = RoundedRectangle(
            width=7.8, height=10.0,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.04,
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(card_bg), run_time=0.4)

        # ---- 条目 1: 核心规则 ----
        item1_h = Text("核心口诀", font=FONT, font_size=28, color=COLOR_RULE)
        item1_b = VGroup(
            Text("分母不变,", font=FONT, font_size=24, color=COLOR_DENOM),
            Text("分子相加减", font=FONT, font_size=24, color=COLOR_NUMER),
        ).arrange(RIGHT, buff=0.15)
        item1 = VGroup(item1_h, item1_b).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item1.move_to(UP * 3.5 + LEFT * 0.1)

        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        sep1 = Line(
            np.array([-3.5, 2.3, 0]), np.array([3.5, 2.3, 0]),
            color=GRAY_B, stroke_width=1,
        )
        self.play(Create(sep1), run_time=0.3)

        # ---- 条目 2: 加法例 ----
        item2_h = Text("加法:", font=FONT, font_size=26, color=COLOR_FRAC1)
        item2_b = VGroup(
            MathTex(r"\frac{1}{3}", font_size=44, color=COLOR_FRAC1),
            Text("+", font=FONT, font_size=28, color=WHITE),
            MathTex(r"\frac{2}{3}", font_size=44, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=28, color=WHITE),
            MathTex(r"\frac{3}{3}", font_size=44, color=COLOR_RES),
            Text("=", font=FONT, font_size=28, color=WHITE),
            MathTex(r"1", font_size=52, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.12)
        item2 = VGroup(item2_h, item2_b).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item2.move_to(UP * 1.5 + LEFT * 0.1)

        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        sep2 = Line(
            np.array([-3.5, 0.5, 0]), np.array([3.5, 0.5, 0]),
            color=GRAY_B, stroke_width=1,
        )
        self.play(Create(sep2), run_time=0.3)

        # ---- 条目 3: 减法例 ----
        item3_h = Text("减法:", font=FONT, font_size=26, color=COLOR_FRAC2)
        item3_b = VGroup(
            MathTex(r"\frac{4}{5}", font_size=44, color=COLOR_FRAC1),
            Text("-", font=FONT, font_size=28, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=44, color=COLOR_FRAC2),
            Text("=", font=FONT, font_size=28, color=WHITE),
            MathTex(r"\frac{4-2}{5}", font_size=44, color=COLOR_RES),
            Text("=", font=FONT, font_size=28, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=52, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.12)
        item3 = VGroup(item3_h, item3_b).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item3.move_to(DOWN * 0.5 + LEFT * 0.1)

        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        sep3 = Line(
            np.array([-3.5, -1.6, 0]), np.array([3.5, -1.6, 0]),
            color=GRAY_B, stroke_width=1,
        )
        self.play(Create(sep3), run_time=0.3)

        # ---- 条目 4: 注意事项 ----
        item4_h = Text("注意事项", font=FONT, font_size=26, color=COLOR_HL)
        item4_b1 = Text(
            "结果能化简要化简",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item4_b2 = Text(
            "如 3/3 = 1",
            font=FONT, font_size=20, color=GRAY_B,
        )
        item4 = VGroup(item4_h, item4_b1, item4_b2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item4.move_to(DOWN * 2.8 + LEFT * 0.1)

        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(3.5)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(sep1),
            FadeOut(item2), FadeOut(sep2),
            FadeOut(item3), FadeOut(sep3),
            FadeOut(item4),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰: 几个小分数飞入
        deco_fracs = VGroup(
            MathTex(r"\frac{1}{3}", font_size=36, color=COLOR_FRAC1),
            MathTex(r"+", font_size=28, color=WHITE),
            MathTex(r"\frac{2}{3}", font_size=36, color=COLOR_FRAC2),
            MathTex(r"=", font_size=28, color=WHITE),
            MathTex(r"1", font_size=40, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.2)

        deco_fracs2 = VGroup(
            MathTex(r"\frac{4}{5}", font_size=36, color=COLOR_FRAC1),
            MathTex(r"-", font_size=28, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=36, color=COLOR_FRAC2),
            MathTex(r"=", font_size=28, color=WHITE),
            MathTex(r"\frac{2}{5}", font_size=40, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.3)

        self.play(
            FadeIn(deco_fracs, shift=RIGHT * 0.4),
            FadeIn(deco_fracs2, shift=RIGHT * 0.4),
            run_time=0.7,
        )
        self.wait(2.5)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_fracs), FadeOut(deco_fracs2),
            run_time=1.0,
        )


# 运行命令:
# manim -qm 002_同分母分数的加减法.py SameDenomFractionLesson
# manim -qh 002_同分母分数的加减法.py SameDenomFractionLesson

"""
003_真分数、假分数和带分数.py — 真分数、假分数和带分数 教学动画

知识点: 真分数(分子<分母)、假分数(分子>=分母)、带分数(整数+真分数)及互化
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 分数也有"真假"之分？
  2. 真分数: 分子 < 分母，值 < 1，用圆饼图直观展示
  3. 假分数: 分子 >= 分母，值 >= 1，用圆饼图展示需要多个整圆
  4. 带分数: 整数 + 真分数，用圆饼图拆分展示
  5. 假分数与带分数的互化: 5/3 = 1又2/3
  6. 练习巩固: 判断分数类型 + 互化练习
  7. 总结
  8. 片尾
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
BG_COLOR = "#1a1a2e"
COLOR_TRUE = "#3b82f6"       # 蓝色真分数
COLOR_FALSE = "#ef4444"      # 红色假分数
COLOR_MIXED = "#22c55e"      # 绿色带分数
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#a78bfa"     # 紫色强调
COLOR_GRID = "#94a3b8"       # 灰色辅助
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
COLOR_PIE_FILL = "#60a5fa"   # 饼图填充
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionTypesLesson(Scene):
    """
    真分数、假分数和带分数 教学动画
    场景顺序:
      1. 开场钩子
      2. 真分数: 分子 < 分母, 值 < 1
      3. 假分数: 分子 >= 分母, 值 >= 1
      4. 带分数: 整数 + 真分数
      5. 假分数与带分数的互化
      6. 练习巩固
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_true_fraction()
        self.scene_3_improper_fraction()
        self.scene_4_mixed_number()
        self.scene_5_conversion()
        self.scene_6_practice()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 辅助: 创建扇形饼图 (表示分数)
    # ------------------------------------------------------------------

    def _pie_chart(self, total, shaded, radius=0.9, fill_color=COLOR_PIE_FILL):
        """
        创建一个圆饼图，分成 total 等份，涂色 shaded 份。
        返回 VGroup(outline, dividers, shaded_sectors)
        """
        outline = Circle(radius=radius, stroke_color=WHITE, stroke_width=2.5)

        dividers = VGroup()
        for i in range(total):
            angle = i * TAU / total + PI / 2
            end = outline.get_center() + radius * np.array([
                np.cos(angle), np.sin(angle), 0
            ])
            line = Line(
                outline.get_center(), end,
                stroke_color=COLOR_GRID, stroke_width=1.5
            )
            dividers.add(line)

        sectors = VGroup()
        for i in range(shaded):
            start_angle = PI / 2 - i * TAU / total
            sector = AnnularSector(
                inner_radius=0,
                outer_radius=radius,
                start_angle=start_angle,
                angle=-TAU / total,
                fill_color=fill_color, fill_opacity=0.5,
                stroke_width=0
            ).move_to(outline.get_center())
            sectors.add(sector)

        return VGroup(outline, dividers, sectors)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "分数也有", font=FONT, font_size=46, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            '"真假"之分？', font=FONT, font_size=52,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.5)

        # 展示三种分数的例子
        f1 = MathTex(r"\frac{1}{3}", font_size=68, color=COLOR_TRUE)
        f2 = MathTex(r"\frac{5}{3}", font_size=68, color=COLOR_FALSE)
        f3_int = Text("1", font=FONT, font_size=44, color=COLOR_MIXED)
        f3_frac = MathTex(r"\frac{2}{3}", font_size=52, color=COLOR_MIXED)
        f3_group = VGroup(f3_int, f3_frac).arrange(RIGHT, buff=0.08)

        fracs = VGroup(f1, f2, f3_group).arrange(RIGHT, buff=1.2).move_to(UP * 1.5)

        for f in [f1, f2, f3_group]:
            self.play(FadeIn(f, scale=0.5), run_time=0.4)

        q = Text(
            "它们有什么区别？", font=FONT, font_size=36,
            color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(q, scale=0.8), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(hook1, hook2, fracs, q)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 真分数
    # ------------------------------------------------------------------

    def scene_2_true_fraction(self):
        title = Text(
            "真分数", font=FONT, font_size=44,
            color=COLOR_TRUE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义
        defn1 = Text(
            "分子 < 分母", font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.2)
        defn2 = Text(
            "分数值 < 1", font=FONT, font_size=28, color=COLOR_GRID
        ).move_to(UP * 3.4)
        self.play(Write(defn1), run_time=0.5)
        self.play(Write(defn2), run_time=0.4)

        # 例子1: 1/3 — 饼图
        pie1 = self._pie_chart(3, 1, radius=0.8, fill_color=COLOR_TRUE)
        pie1.move_to(UP * 1.5 + LEFT * 2.5)
        label1 = MathTex(r"\frac{1}{3}", font_size=52, color=COLOR_TRUE)
        label1.next_to(pie1, DOWN, buff=0.3)

        self.play(Create(pie1[0]), run_time=0.3)
        self.play(Create(pie1[1]), run_time=0.3)
        self.play(FadeIn(pie1[2]), FadeIn(label1), run_time=0.5)
        self.wait(0.3)

        # 例子2: 2/5 — 饼图
        pie2 = self._pie_chart(5, 2, radius=0.8, fill_color=COLOR_TRUE)
        pie2.move_to(UP * 1.5 + RIGHT * 2.5)
        label2 = MathTex(r"\frac{2}{5}", font_size=52, color=COLOR_TRUE)
        label2.next_to(pie2, DOWN, buff=0.3)

        self.play(Create(pie2[0]), run_time=0.3)
        self.play(Create(pie2[1]), run_time=0.3)
        self.play(FadeIn(pie2[2]), FadeIn(label2), run_time=0.5)
        self.wait(0.3)

        # 强调: 不满一个圆
        note = Text(
            "涂色部分不到一整个圆！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)

        # 公式化
        formula_box = RoundedRectangle(
            width=7.0, height=1.8, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_TRUE, stroke_width=2.5
        ).move_to(DOWN * 3.0)
        formula_text = Text(
            "真分数: 分子 < 分母，值 < 1",
            font=FONT, font_size=26, color=COLOR_TRUE, weight=BOLD
        ).move_to(DOWN * 2.6)
        formula_ex = Text(
            "如: 1/3, 2/5, 3/8, 4/7 ...",
            font=FONT, font_size=22, color=COLOR_GRID
        ).move_to(DOWN * 3.4)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_text), run_time=0.5)
        self.play(FadeIn(formula_ex), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 假分数
    # ------------------------------------------------------------------

    def scene_3_improper_fraction(self):
        title = Text(
            "假分数", font=FONT, font_size=44,
            color=COLOR_FALSE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义
        defn1 = Text(
            "分子 >= 分母", font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.2)
        defn2 = Text(
            "分数值 >= 1", font=FONT, font_size=28, color=COLOR_GRID
        ).move_to(UP * 3.4)
        self.play(Write(defn1), run_time=0.5)
        self.play(Write(defn2), run_time=0.4)

        # 例子1: 3/3 = 1 (刚好满一圆)
        pie_eq = self._pie_chart(3, 3, radius=0.7, fill_color=COLOR_FALSE)
        pie_eq.move_to(UP * 1.8 + LEFT * 2.5)
        label_eq = MathTex(r"\frac{3}{3}", font_size=48, color=COLOR_FALSE)
        label_eq.next_to(pie_eq, DOWN, buff=0.25)
        eq_note = MathTex(r"= 1", font_size=38, color=COLOR_HL)
        eq_note.next_to(label_eq, RIGHT, buff=0.15)

        self.play(Create(pie_eq[0]), Create(pie_eq[1]), run_time=0.3)
        self.play(FadeIn(pie_eq[2]), FadeIn(label_eq), run_time=0.5)
        self.play(FadeIn(eq_note), run_time=0.3)
        self.wait(0.3)

        # 例子2: 5/3 (超过一圆)  — 一整圆 + 2/3圆
        pie_full = self._pie_chart(3, 3, radius=0.7, fill_color=COLOR_FALSE)
        pie_part = self._pie_chart(3, 2, radius=0.7, fill_color=COLOR_FALSE)

        pie_full.move_to(DOWN * 0.5 + LEFT * 1.8)
        pie_part.move_to(DOWN * 0.5 + RIGHT * 1.8)

        plus_sign = MathTex(r"+", font_size=40, color=WHITE).move_to(DOWN * 0.5)
        label_53 = MathTex(r"\frac{5}{3}", font_size=52, color=COLOR_FALSE)
        label_53.move_to(DOWN * 2.2)

        full_text = Text(
            "1 整圆", font=FONT, font_size=18, color=COLOR_GRID
        ).next_to(pie_full, DOWN, buff=0.15)
        part_text = Text(
            "2/3 圆", font=FONT, font_size=18, color=COLOR_GRID
        ).next_to(pie_part, DOWN, buff=0.15)

        self.play(
            Create(pie_full[0]), Create(pie_full[1]),
            Create(pie_part[0]), Create(pie_part[1]),
            run_time=0.4
        )
        self.play(
            FadeIn(pie_full[2]), FadeIn(pie_part[2]),
            FadeIn(plus_sign),
            FadeIn(full_text), FadeIn(part_text),
            run_time=0.5
        )
        self.play(FadeIn(label_53, shift=UP * 0.2), run_time=0.4)

        # 强调
        note = Text(
            "涂色超过了一整个圆！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)

        # 公式化
        formula_box = RoundedRectangle(
            width=7.5, height=1.8, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_FALSE, stroke_width=2.5
        ).move_to(DOWN * 5.2)
        formula_text = Text(
            "假分数: 分子 >= 分母，值 >= 1",
            font=FONT, font_size=26, color=COLOR_FALSE, weight=BOLD
        ).move_to(DOWN * 4.8)
        formula_ex = Text(
            "如: 3/3, 5/3, 7/4, 9/5 ...",
            font=FONT, font_size=22, color=COLOR_GRID
        ).move_to(DOWN * 5.6)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_text), run_time=0.5)
        self.play(FadeIn(formula_ex), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 带分数
    # ------------------------------------------------------------------

    def scene_4_mixed_number(self):
        title = Text(
            "带分数", font=FONT, font_size=44,
            color=COLOR_MIXED, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义
        defn1 = Text(
            "整数 + 真分数", font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.2)
        defn2 = Text(
            "值一定大于 1", font=FONT, font_size=28, color=COLOR_GRID
        ).move_to(UP * 3.4)
        self.play(Write(defn1), run_time=0.5)
        self.play(Write(defn2), run_time=0.4)

        # 图示: 1又2/3 = 一整圆 + 2/3圆
        pie_full = self._pie_chart(3, 3, radius=0.8, fill_color=COLOR_MIXED)
        pie_part = self._pie_chart(3, 2, radius=0.8, fill_color=COLOR_MIXED)

        pie_full.move_to(UP * 1.5 + LEFT * 2.0)
        pie_part.move_to(UP * 1.5 + RIGHT * 2.0)

        full_lbl = Text(
            "1 整个", font=FONT, font_size=20, color=COLOR_GRID
        ).next_to(pie_full, DOWN, buff=0.15)
        part_lbl = MathTex(
            r"\frac{2}{3}", font_size=36, color=COLOR_GRID
        ).next_to(pie_part, DOWN, buff=0.15)

        plus_sign = MathTex(r"+", font_size=40, color=WHITE).move_to(UP * 1.5)

        self.play(
            Create(pie_full[0]), Create(pie_full[1]),
            Create(pie_part[0]), Create(pie_part[1]),
            run_time=0.4
        )
        self.play(
            FadeIn(pie_full[2]), FadeIn(pie_part[2]),
            FadeIn(plus_sign),
            FadeIn(full_lbl), FadeIn(part_lbl),
            run_time=0.5
        )

        # 写法
        write_title = Text(
            "写法:", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(Write(write_title), run_time=0.4)

        mixed_int = Text("1", font=FONT, font_size=56, color=COLOR_MIXED)
        mixed_frac = MathTex(r"\frac{2}{3}", font_size=56, color=COLOR_MIXED)
        mixed_display = VGroup(mixed_int, mixed_frac).arrange(RIGHT, buff=0.1)
        mixed_display.move_to(DOWN * 2.0)

        self.play(FadeIn(mixed_display, scale=0.5), run_time=0.6)

        read_text = Text(
            '读作："一又三分之二"',
            font=FONT, font_size=24, color=COLOR_GRID
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(read_text), run_time=0.4)

        # 说明结构
        struct_text = Text(
            "整数部分 + 真分数部分",
            font=FONT, font_size=24, color=COLOR_ACCENT
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(struct_text, shift=UP * 0.2), run_time=0.5)

        # 强调
        note = Text(
            "带分数的值一定大于 1",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 5.4)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 5: 假分数与带分数的互化
    # ------------------------------------------------------------------

    def scene_5_conversion(self):
        title = Text(
            "假分数 <-> 带分数", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 假分数 → 带分数 =====
        sub1 = Text(
            "假分数 -> 带分数", font=FONT, font_size=30,
            color=COLOR_FALSE, weight=BOLD
        ).move_to(UP * 4.2)
        self.play(Write(sub1), run_time=0.5)

        # 5/3 → 1又2/3
        step_title = Text(
            "例:", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 3.2 + LEFT * 3.5)
        frac_start = MathTex(r"\frac{5}{3}", font_size=56, color=COLOR_FALSE)
        frac_start.move_to(UP * 3.2 + LEFT * 1.5)
        self.play(Write(step_title), FadeIn(frac_start), run_time=0.5)

        # 除法步骤
        method_text = Text(
            "用分子除以分母:", font=FONT, font_size=24, color=COLOR_GRID
        ).move_to(UP * 2.0)
        self.play(Write(method_text), run_time=0.4)

        div_line1 = MathTex(
            r"5 \div 3 = 1 \cdots\cdots 2",
            font_size=42, color=WHITE
        ).move_to(UP * 0.8)
        self.play(Write(div_line1), run_time=0.7)
        self.wait(0.3)

        # 解释各部分
        explain1 = Text(
            "商 1 -> 整数部分", font=FONT, font_size=22, color=COLOR_MIXED
        ).move_to(DOWN * 0.2 + LEFT * 1.5)
        explain2 = Text(
            "余数 2 -> 分子", font=FONT, font_size=22, color=COLOR_MIXED
        ).move_to(DOWN * 0.9 + LEFT * 1.5)
        explain3 = Text(
            "除数 3 -> 分母", font=FONT, font_size=22, color=COLOR_MIXED
        ).move_to(DOWN * 1.6 + LEFT * 1.5)

        self.play(FadeIn(explain1, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(explain2, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(explain3, shift=RIGHT * 0.2), run_time=0.3)

        # 结果
        arrow1 = MathTex(r"\Longrightarrow", font_size=42, color=COLOR_HL)
        arrow1.move_to(DOWN * 3.0 + LEFT * 1.0)
        result_int = Text("1", font=FONT, font_size=52, color=COLOR_MIXED)
        result_frac = MathTex(r"\frac{2}{3}", font_size=52, color=COLOR_MIXED)
        result_group = VGroup(result_int, result_frac).arrange(RIGHT, buff=0.08)
        result_group.move_to(DOWN * 3.0 + RIGHT * 1.5)

        self.play(FadeIn(arrow1), FadeIn(result_group, scale=0.5), run_time=0.6)

        result_box = SurroundingRectangle(
            VGroup(frac_start, arrow1, result_group),
            color=COLOR_HL, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        self.play(Create(result_box), run_time=0.4)
        self.wait(1.0)

        # 清理上半场
        self.play(FadeOut(VGroup(
            sub1, step_title, frac_start, method_text,
            div_line1, explain1, explain2, explain3,
            arrow1, result_group, result_box
        )), run_time=0.4)

        # ===== 带分数 → 假分数 =====
        sub2 = Text(
            "带分数 -> 假分数", font=FONT, font_size=30,
            color=COLOR_MIXED, weight=BOLD
        ).move_to(UP * 4.2)
        self.play(Write(sub2), run_time=0.5)

        # 1又2/3 → 5/3
        mixed_int2 = Text("1", font=FONT, font_size=52, color=COLOR_MIXED)
        mixed_frac2 = MathTex(r"\frac{2}{3}", font_size=52, color=COLOR_MIXED)
        mixed_show = VGroup(mixed_int2, mixed_frac2).arrange(RIGHT, buff=0.08)
        mixed_show.move_to(UP * 2.8)
        self.play(FadeIn(mixed_show), run_time=0.4)

        method2 = Text(
            "整数 x 分母 + 分子 = 新分子",
            font=FONT, font_size=24, color=COLOR_GRID
        ).move_to(UP * 1.5)
        self.play(Write(method2), run_time=0.5)

        calc = MathTex(
            r"1 \times 3 + 2 = 5",
            font_size=42, color=WHITE
        ).move_to(UP * 0.3)
        self.play(Write(calc), run_time=0.6)

        explain_d = Text(
            "分母不变，还是 3",
            font=FONT, font_size=22, color=COLOR_GRID
        ).move_to(DOWN * 0.7)
        self.play(FadeIn(explain_d), run_time=0.3)

        # 结果
        arrow2 = MathTex(r"\Longrightarrow", font_size=42, color=COLOR_HL)
        arrow2.move_to(DOWN * 2.0 + LEFT * 1.0)
        result2 = MathTex(r"\frac{5}{3}", font_size=56, color=COLOR_FALSE)
        result2.move_to(DOWN * 2.0 + RIGHT * 1.5)

        self.play(FadeIn(arrow2), FadeIn(result2, scale=0.5), run_time=0.6)

        result_box2 = SurroundingRectangle(
            VGroup(mixed_show, arrow2, result2),
            color=COLOR_HL, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        self.play(Create(result_box2), run_time=0.4)

        # 公式总结
        formula_box = RoundedRectangle(
            width=7.5, height=2.5, corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 4.8)

        formula_line1 = Text(
            "假 -> 带: 分子 / 分母 = 商...余数",
            font=FONT, font_size=20, color=COLOR_FALSE
        ).move_to(DOWN * 4.2)
        formula_line2 = Text(
            "带 -> 假: 整数x分母+分子 做新分子",
            font=FONT, font_size=20, color=COLOR_MIXED
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_line1), run_time=0.4)
        self.play(Write(formula_line2), run_time=0.4)
        self.wait(2.0)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 练习巩固
    # ------------------------------------------------------------------

    def scene_6_practice(self):
        title = Text(
            "判断练习", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        instructions = Text(
            "下面的分数各是什么类型？",
            font=FONT, font_size=26, color=COLOR_GRID
        ).move_to(UP * 4.3)
        self.play(Write(instructions), run_time=0.5)

        # 练习题目
        problems = [
            (r"\frac{2}{7}", "真分数", COLOR_TRUE, "分子 2 < 分母 7"),
            (r"\frac{9}{4}", "假分数", COLOR_FALSE, "分子 9 > 分母 4"),
            (r"\frac{6}{6}", "假分数", COLOR_FALSE, "分子 6 = 分母 6"),
            (r"\frac{3}{8}", "真分数", COLOR_TRUE, "分子 3 < 分母 8"),
        ]

        y_start = 3.0
        for i, (frac_tex, answer_text, color, reason) in enumerate(problems):
            y = y_start - i * 1.8

            frac = MathTex(frac_tex, font_size=48, color=WHITE)
            frac.move_to(UP * y + LEFT * 2.5)
            self.play(FadeIn(frac, scale=0.6), run_time=0.3)
            self.wait(0.5)

            # 答案
            ans = Text(
                answer_text, font=FONT, font_size=26,
                color=color, weight=BOLD
            ).move_to(UP * y + RIGHT * 0.5)

            reason_t = Text(
                reason, font=FONT, font_size=18, color=COLOR_GRID
            ).move_to(UP * y + RIGHT * 0.5 + DOWN * 0.5)

            self.play(FadeIn(ans, shift=LEFT * 0.3), run_time=0.3)
            self.play(FadeIn(reason_t, shift=UP * 0.1), run_time=0.3)

        # 互化练习
        convert_title = Text(
            "互化: 把 7/4 化成带分数",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(convert_title, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        convert_step = MathTex(
            r"\frac{7}{4} = 1\cdots\cdots 3",
            font_size=36, color=WHITE
        ).move_to(DOWN * 5.5)
        self.play(Write(convert_step), run_time=0.5)

        convert_ans_int = Text("1", font=FONT, font_size=40, color=COLOR_MIXED)
        convert_ans_frac = MathTex(r"\frac{3}{4}", font_size=40, color=COLOR_MIXED)
        convert_ans = VGroup(convert_ans_int, convert_ans_frac).arrange(RIGHT, buff=0.08)
        convert_eq = MathTex(r"=", font_size=36, color=WHITE)
        convert_result = VGroup(convert_eq, convert_ans).arrange(RIGHT, buff=0.15)
        convert_result.next_to(convert_step, RIGHT, buff=0.3)

        self.play(FadeIn(convert_result, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        box = RoundedRectangle(
            width=8.0, height=9.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "三种分数", font=FONT, font_size=34,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.3)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("真分数:", font=FONT, font_size=26, color=COLOR_TRUE, weight=BOLD),
            Text("  分子 < 分母，值 < 1", font=FONT, font_size=22, color=WHITE),
            Text(" ", font=FONT, font_size=12, color=WHITE),
            Text("假分数:", font=FONT, font_size=26, color=COLOR_FALSE, weight=BOLD),
            Text("  分子 >= 分母，值 >= 1", font=FONT, font_size=22, color=WHITE),
            Text(" ", font=FONT, font_size=12, color=WHITE),
            Text("带分数:", font=FONT, font_size=26, color=COLOR_MIXED, weight=BOLD),
            Text("  整数 + 真分数，值 > 1", font=FONT, font_size=22, color=WHITE),
            Text(" ", font=FONT, font_size=12, color=WHITE),
            Text("互化方法:", font=FONT, font_size=26, color=COLOR_ACCENT, weight=BOLD),
            Text("  假->带: 分子/分母=商...余数", font=FONT, font_size=20, color=WHITE),
            Text("  带->假: 整数x分母+分子", font=FONT, font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.3)

        tip = Text(
            "真分数 < 1，假分数 >= 1",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 三类分数
        deco_colors = [
            COLOR_TRUE, COLOR_TRUE, COLOR_FALSE,
            COLOR_FALSE, COLOR_MIXED, COLOR_MIXED
        ]
        deco_fracs = [
            r"\frac{1}{3}", r"\frac{2}{5}", r"\frac{5}{3}",
            r"\frac{7}{4}", r"\frac{3}{4}", r"\frac{2}{3}"
        ]
        mini = VGroup(*[
            MathTex(f, font_size=30, color=c).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.5,
                    np.sin(i * PI / 3) * 0.8,
                    0.0
                ])
            )
            for i, (f, c) in enumerate(zip(deco_fracs, deco_colors))
        ])
        self.play(*[FadeIn(t, scale=0.3) for t in mini], run_time=0.5)
        self.play(
            Rotate(mini, angle=2 * PI / 3, run_time=1.2, rate_func=smooth)
        )
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini)),
            run_time=0.8
        )

    # ------------------------------------------------------------------
    # Helper
    # ------------------------------------------------------------------

    def mobjects_without_author(self):
        return VGroup(*[
            m for m in self.mobjects
            if m is not self.author_mob and isinstance(m, VMobject)
        ])


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 003_真分数、假分数和带分数.py FractionTypesLesson
#   高质量:    manim -qh  003_真分数、假分数和带分数.py FractionTypesLesson
#   4K:        manim -qk  003_真分数、假分数和带分数.py FractionTypesLesson
# ======================================================================

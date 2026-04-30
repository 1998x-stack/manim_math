"""
005_比例尺.py — 比例尺 教学动画

知识点: 比例尺的概念、数值比例尺与线段比例尺、求比例尺/图上距离/实际距离
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 比例尺的概念
  3. 公式推导
  4. 数值比例尺 vs 线段比例尺
  5. 例题1: 求比例尺
  6. 例题2: 求实际距离
  7. 例题3: 求图上距离
  8. 总结
  9. 片尾
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
COLOR_MAP = "#3b82f6"         # 蓝色 地图相关
COLOR_REAL = "#f59e0b"        # 橙色 实际距离
COLOR_SCALE = "#22c55e"       # 绿色 比例尺
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_ACCENT = "#a78bfa"      # 紫色强调
COLOR_RED = "#ef4444"         # 红色
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
COLOR_FORMULA = "#38bdf8"     # 天蓝色 公式
COLOR_PINK = "#f472b6"        # 粉色
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class ScaleLesson(Scene):
    """
    比例尺教学动画
    场景顺序:
      1. 开场钩子
      2. 比例尺的概念 (地图缩放引入)
      3. 公式讲解
      4. 数值比例尺 vs 线段比例尺
      5. 例题1: 求比例尺
      6. 例题2: 求实际距离
      7. 例题3: 求图上距离
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_concept()
        self.scene_3_formula()
        self.scene_4_types()
        self.scene_5_example_1()
        self.scene_6_example_2()
        self.scene_7_example_3()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子
        hook1 = Text(
            "地图上 5 厘米",
            font=FONT, font_size=40, color=COLOR_MAP
        ).move_to(UP * 3.5)

        hook2 = Text(
            "= 实际多少公里?",
            font=FONT, font_size=40, color=COLOR_REAL
        ).move_to(UP * 2.5)

        self.play(Write(hook1), run_time=0.8)
        self.play(Write(hook2), run_time=0.8)
        self.wait(0.5)

        # 小地图图示
        map_rect = RoundedRectangle(
            width=5, height=3.5, corner_radius=0.3,
            color=COLOR_MAP, stroke_width=2, fill_opacity=0.1
        ).move_to(DOWN * 0.5)

        map_label = Text(
            "中国地图", font=FONT, font_size=22, color=WHITE
        ).move_to(map_rect.get_top() + DOWN * 0.4)

        # 两个城市点
        city_a = Dot(map_rect.get_center() + LEFT * 1.5 + UP * 0.3, color=COLOR_RED, radius=0.1)
        city_b = Dot(map_rect.get_center() + RIGHT * 1.2 + DOWN * 0.5, color=COLOR_RED, radius=0.1)
        city_a_label = Text("A", font=FONT, font_size=18, color=WHITE).next_to(city_a, UL, buff=0.1)
        city_b_label = Text("B", font=FONT, font_size=18, color=WHITE).next_to(city_b, DR, buff=0.1)

        line_ab = DashedLine(city_a.get_center(), city_b.get_center(), color=COLOR_HL, dash_length=0.1)
        dist_label = Text("5cm", font=FONT, font_size=20, color=COLOR_HL).next_to(line_ab, UP, buff=0.15)

        self.play(FadeIn(map_rect), FadeIn(map_label), run_time=0.6)
        self.play(
            FadeIn(city_a), FadeIn(city_b),
            FadeIn(city_a_label), FadeIn(city_b_label),
            run_time=0.5
        )
        self.play(Create(line_ab), FadeIn(dist_label), run_time=0.6)

        # 问号
        question = Text(
            "? km",
            font=FONT, font_size=36, color=COLOR_REAL
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(question, scale=1.3), run_time=0.5)
        self.wait(0.8)

        # 引出主题
        title = Text(
            "比例尺", font=FONT, font_size=48, color=COLOR_SCALE
        ).move_to(DOWN * 5.5)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # 清理
        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(map_rect), FadeOut(map_label),
            FadeOut(city_a), FadeOut(city_b),
            FadeOut(city_a_label), FadeOut(city_b_label),
            FadeOut(line_ab), FadeOut(dist_label),
            FadeOut(question), FadeOut(title),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 比例尺的概念
    # ------------------------------------------------------------------
    def scene_2_concept(self):
        title = Text(
            "什么是比例尺?", font=FONT, font_size=36, color=COLOR_SCALE
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 实物 (大矩形代表操场)
        real_rect = Rectangle(
            width=6, height=3.6, color=COLOR_REAL,
            stroke_width=3, fill_opacity=0.08
        ).move_to(UP * 3.0)
        real_label = Text(
            "实际操场", font=FONT, font_size=22, color=COLOR_REAL
        ).next_to(real_rect, UP, buff=0.15)
        real_dim = Text(
            "长 100m, 宽 60m", font=FONT, font_size=18, color=COLOR_REAL
        ).next_to(real_rect, DOWN, buff=0.15)

        self.play(FadeIn(real_rect), FadeIn(real_label), FadeIn(real_dim), run_time=0.8)
        self.wait(0.5)

        # 缩小箭头
        arrow_down = Arrow(
            start=real_rect.get_bottom() + DOWN * 0.5,
            end=real_rect.get_bottom() + DOWN * 1.8,
            color=COLOR_HL, stroke_width=3
        )
        shrink_label = Text(
            "按比例缩小", font=FONT, font_size=22, color=COLOR_HL
        ).next_to(arrow_down, RIGHT, buff=0.2)

        self.play(GrowArrow(arrow_down), FadeIn(shrink_label), run_time=0.6)

        # 图上 (小矩形)
        map_rect = Rectangle(
            width=2, height=1.2, color=COLOR_MAP,
            stroke_width=3, fill_opacity=0.15
        ).move_to(DOWN * 1.0)
        map_label = Text(
            "图上操场", font=FONT, font_size=22, color=COLOR_MAP
        ).next_to(map_rect, UP, buff=0.15)
        map_dim = Text(
            "长 2cm, 宽 1.2cm", font=FONT, font_size=18, color=COLOR_MAP
        ).next_to(map_rect, DOWN, buff=0.15)

        self.play(FadeIn(map_rect), FadeIn(map_label), FadeIn(map_dim), run_time=0.8)
        self.wait(0.5)

        # 概念文字
        concept = VGroup(
            Text("图上距离", font=FONT, font_size=26, color=COLOR_MAP),
            Text("与", font=FONT, font_size=26, color=WHITE),
            Text("实际距离", font=FONT, font_size=26, color=COLOR_REAL),
            Text("的比", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 3.5)

        concept2 = Text(
            "叫做比例尺", font=FONT, font_size=30, color=COLOR_SCALE
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(concept, shift=UP * 0.3), run_time=0.8)
        self.play(Write(concept2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(real_rect), FadeOut(real_label), FadeOut(real_dim),
            FadeOut(arrow_down), FadeOut(shrink_label),
            FadeOut(map_rect), FadeOut(map_label), FadeOut(map_dim),
            FadeOut(concept), FadeOut(concept2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 公式讲解
    # ------------------------------------------------------------------
    def scene_3_formula(self):
        title = Text(
            "比例尺公式", font=FONT, font_size=36, color=COLOR_SCALE
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 主公式
        label_scale = Text("比例尺", font=FONT, font_size=28, color=COLOR_SCALE)
        eq_sign = MathTex(r"=", font_size=36)
        label_map = Text("图上距离", font=FONT, font_size=28, color=COLOR_MAP)
        colon = MathTex(r":", font_size=36)
        label_real = Text("实际距离", font=FONT, font_size=28, color=COLOR_REAL)

        formula_line = VGroup(label_scale, eq_sign, label_map, colon, label_real).arrange(
            RIGHT, buff=0.2
        ).move_to(UP * 4.0)

        self.play(Write(formula_line), run_time=1.0)
        self.wait(0.5)

        # 分数形式
        frac_label = Text("也可以写成:", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 2.8)
        frac_top = Text("图上距离", font=FONT, font_size=24, color=COLOR_MAP)
        frac_bot = Text("实际距离", font=FONT, font_size=24, color=COLOR_REAL)
        frac_line_mob = Line(LEFT * 1.2, RIGHT * 1.2, color=WHITE, stroke_width=2)
        frac_group = VGroup(frac_top, frac_line_mob, frac_bot).arrange(DOWN, buff=0.12).move_to(UP * 1.5)

        label_s2 = Text("比例尺 =", font=FONT, font_size=28, color=COLOR_SCALE).next_to(
            frac_group, LEFT, buff=0.3
        )

        self.play(FadeIn(frac_label), run_time=0.4)
        self.play(FadeIn(label_s2), FadeIn(frac_group), run_time=0.8)
        self.wait(0.5)

        # 三个变形公式
        derive_title = Text(
            "变形公式:", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(derive_title), run_time=0.4)

        # 公式 1: 实际距离 = 图上距离 / 比例尺
        f1_a = Text("实际距离", font=FONT, font_size=24, color=COLOR_REAL)
        f1_eq = MathTex(r"=", font_size=32)
        f1_b = Text("图上距离", font=FONT, font_size=24, color=COLOR_MAP)
        f1_div = MathTex(r"\div", font_size=32)
        f1_c = Text("比例尺", font=FONT, font_size=24, color=COLOR_SCALE)
        f1 = VGroup(f1_a, f1_eq, f1_b, f1_div, f1_c).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.3)

        # 公式 2: 图上距离 = 实际距离 x 比例尺
        f2_a = Text("图上距离", font=FONT, font_size=24, color=COLOR_MAP)
        f2_eq = MathTex(r"=", font_size=32)
        f2_b = Text("实际距离", font=FONT, font_size=24, color=COLOR_REAL)
        f2_times = MathTex(r"\times", font_size=32)
        f2_c = Text("比例尺", font=FONT, font_size=24, color=COLOR_SCALE)
        f2 = VGroup(f2_a, f2_eq, f2_b, f2_times, f2_c).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)

        self.play(FadeIn(f1, shift=UP * 0.2), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(f2, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)

        # 注意: 单位统一
        warning_box = RoundedRectangle(
            width=7, height=1.2, corner_radius=0.2,
            color=COLOR_RED, stroke_width=2, fill_opacity=0.1
        ).move_to(DOWN * 4.5)
        warning_icon = Text("!", font=FONT, font_size=32, color=COLOR_RED).move_to(
            warning_box.get_left() + RIGHT * 0.6
        )
        warning_text = Text(
            "注意: 单位要统一!", font=FONT, font_size=24, color=COLOR_RED
        ).move_to(warning_box.get_center() + RIGHT * 0.3)

        self.play(FadeIn(warning_box), FadeIn(warning_icon), FadeIn(warning_text), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(formula_line),
            FadeOut(frac_label), FadeOut(label_s2), FadeOut(frac_group),
            FadeOut(derive_title), FadeOut(f1), FadeOut(f2),
            FadeOut(warning_box), FadeOut(warning_icon), FadeOut(warning_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 数值比例尺 vs 线段比例尺
    # ------------------------------------------------------------------
    def scene_4_types(self):
        title = Text(
            "两种比例尺", font=FONT, font_size=36, color=COLOR_SCALE
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # --- 数值比例尺 ---
        num_title = Text(
            "数值比例尺", font=FONT, font_size=28, color=COLOR_ACCENT
        ).move_to(UP * 4.5)
        self.play(Write(num_title), run_time=0.5)

        num_ex = MathTex(
            r"1 : 10000", font_size=42, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(num_ex), run_time=0.6)

        num_explain = Text(
            "图上 1cm = 实际 10000cm = 100m",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 2.7)
        self.play(FadeIn(num_explain), run_time=0.5)

        num_ex2 = MathTex(
            r"1 : 1000000", font_size=42, color=WHITE
        ).move_to(UP * 1.7)
        num_explain2 = Text(
            "图上 1cm = 实际 10km",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 0.9)
        self.play(Write(num_ex2), run_time=0.5)
        self.play(FadeIn(num_explain2), run_time=0.4)
        self.wait(0.5)

        # --- 线段比例尺 ---
        seg_title = Text(
            "线段比例尺", font=FONT, font_size=28, color=COLOR_PINK
        ).move_to(DOWN * 0.3)
        self.play(Write(seg_title), run_time=0.5)

        # 画线段比例尺
        scale_bar_y = -1.5
        seg_count = 5
        seg_width = 1.0
        total_width = seg_count * seg_width
        start_x = -total_width / 2

        segments = VGroup()
        labels = VGroup()
        for i in range(seg_count):
            x0 = start_x + i * seg_width
            rect = Rectangle(
                width=seg_width, height=0.25,
                stroke_color=WHITE, stroke_width=1.5,
                fill_color=WHITE if i % 2 == 0 else BG_COLOR,
                fill_opacity=0.8 if i % 2 == 0 else 0
            ).move_to(np.array([x0 + seg_width / 2, scale_bar_y, 0]))
            segments.add(rect)

            # tick label
            km_val = i * 10
            lbl = Text(
                str(km_val), font=FONT, font_size=16, color=WHITE
            ).move_to(np.array([x0, scale_bar_y - 0.35, 0]))
            labels.add(lbl)

        # last label
        last_lbl = Text(
            str(seg_count * 10), font=FONT, font_size=16, color=WHITE
        ).move_to(np.array([start_x + total_width, scale_bar_y - 0.35, 0]))
        labels.add(last_lbl)

        km_unit = Text(
            "km", font=FONT, font_size=18, color=GRAY_A
        ).move_to(np.array([start_x + total_width + 0.5, scale_bar_y - 0.35, 0]))

        self.play(FadeIn(segments), FadeIn(labels), FadeIn(km_unit), run_time=0.8)

        seg_explain = Text(
            "直观显示距离对应关系", font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(seg_explain), run_time=0.4)
        self.wait(1.0)

        # 比较框
        compare = VGroup(
            Text("数值比例尺: 精确计算", font=FONT, font_size=20, color=COLOR_ACCENT),
            Text("线段比例尺: 直观估读", font=FONT, font_size=20, color=COLOR_PINK),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 4.5)

        self.play(FadeIn(compare, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(num_title), FadeOut(num_ex), FadeOut(num_explain),
            FadeOut(num_ex2), FadeOut(num_explain2),
            FadeOut(seg_title), FadeOut(segments), FadeOut(labels), FadeOut(km_unit),
            FadeOut(seg_explain), FadeOut(compare),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 例题1 求比例尺
    # ------------------------------------------------------------------
    def scene_5_example_1(self):
        title = Text(
            "例题 1: 求比例尺", font=FONT, font_size=32, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 题目
        q1 = Text(
            "一幅地图上, 两地之间的距离是", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.8)
        q1_val = Text(
            "5 厘米", font=FONT, font_size=24, color=COLOR_MAP
        )
        q1_mid = Text(
            ", 实际距离是", font=FONT, font_size=22, color=WHITE
        )
        q1_val2 = Text(
            "200 千米", font=FONT, font_size=24, color=COLOR_REAL
        )
        q1_end = Text(
            "。", font=FONT, font_size=22, color=WHITE
        )
        q_line2 = VGroup(q1_val, q1_mid, q1_val2, q1_end).arrange(
            RIGHT, buff=0.08
        ).move_to(UP * 4.0)

        q_ask = Text(
            "求这幅地图的比例尺。", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(UP * 3.2)

        self.play(FadeIn(q1), run_time=0.5)
        self.play(FadeIn(q_line2), run_time=0.5)
        self.play(FadeIn(q_ask), run_time=0.5)
        self.wait(0.5)

        # 解题步骤
        step1_label = Text(
            "第1步: 统一单位", font=FONT, font_size=22, color=COLOR_RED
        ).move_to(UP * 2.0)
        self.play(FadeIn(step1_label), run_time=0.4)

        convert = MathTex(
            r"200 \text{ km} = 200 \times 100000 \text{ cm} = 20000000 \text{ cm}",
            font_size=26
        ).move_to(UP * 1.0)
        self.play(Write(convert), run_time=1.0)
        self.wait(0.5)

        step2_label = Text(
            "第2步: 代入公式", font=FONT, font_size=22, color=COLOR_SCALE
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(step2_label), run_time=0.4)

        # 比例尺 = 图上距离 : 实际距离
        calc_label = Text("比例尺 =", font=FONT, font_size=24, color=COLOR_SCALE)
        calc_map = Text("图上距离", font=FONT, font_size=20, color=COLOR_MAP)
        calc_colon = MathTex(r":", font_size=28)
        calc_real = Text("实际距离", font=FONT, font_size=20, color=COLOR_REAL)
        calc_line = VGroup(calc_label, calc_map, calc_colon, calc_real).arrange(
            RIGHT, buff=0.12
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(calc_line), run_time=0.5)

        calc2 = MathTex(
            r"= 5 : 20000000", font_size=30
        ).move_to(DOWN * 2.2)
        self.play(Write(calc2), run_time=0.6)

        step3_label = Text(
            "第3步: 化简", font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(step3_label), run_time=0.4)

        calc3 = MathTex(
            r"= 1 : 4000000", font_size=36, color=COLOR_SCALE
        ).move_to(DOWN * 4.2)
        self.play(Write(calc3), run_time=0.8)

        # 答案框
        ans_box = SurroundingRectangle(calc3, color=COLOR_SCALE, buff=0.2, corner_radius=0.1)
        self.play(Create(ans_box), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q_line2), FadeOut(q_ask),
            FadeOut(step1_label), FadeOut(convert),
            FadeOut(step2_label), FadeOut(calc_line), FadeOut(calc2),
            FadeOut(step3_label), FadeOut(calc3), FadeOut(ans_box),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题2 求实际距离
    # ------------------------------------------------------------------
    def scene_6_example_2(self):
        title = Text(
            "例题 2: 求实际距离", font=FONT, font_size=32, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 题目
        q1 = Text(
            "比例尺为 1:500000 的地图上,", font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.8)
        q2 = Text(
            "两地距离为 8 厘米,", font=FONT, font_size=22, color=COLOR_MAP
        ).move_to(UP * 4.0)
        q3 = Text(
            "求实际距离是多少千米?", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(UP * 3.2)

        self.play(FadeIn(q1), run_time=0.4)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(q3), run_time=0.4)
        self.wait(0.5)

        # 解题
        formula_label = Text(
            "公式:", font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(UP * 2.0 + LEFT * 3)

        f_a = Text("实际距离", font=FONT, font_size=24, color=COLOR_REAL)
        f_eq = MathTex(r"=", font_size=30)
        f_b = Text("图上距离", font=FONT, font_size=24, color=COLOR_MAP)
        f_div = MathTex(r"\div", font_size=30)
        f_c = Text("比例尺", font=FONT, font_size=24, color=COLOR_SCALE)
        formula_row = VGroup(f_a, f_eq, f_b, f_div, f_c).arrange(
            RIGHT, buff=0.12
        ).move_to(UP * 1.0)

        self.play(FadeIn(formula_label), FadeIn(formula_row), run_time=0.6)

        # 代入
        sub_line = MathTex(
            r"= 8 \div \frac{1}{500000}",
            font_size=32
        ).move_to(DOWN * 0.3)
        self.play(Write(sub_line), run_time=0.8)

        calc1 = MathTex(
            r"= 8 \times 500000",
            font_size=32
        ).move_to(DOWN * 1.5)
        self.play(Write(calc1), run_time=0.6)

        calc2 = MathTex(
            r"= 4000000 \text{ cm}",
            font_size=32
        ).move_to(DOWN * 2.7)
        self.play(Write(calc2), run_time=0.6)

        # 单位换算
        convert_label = Text(
            "换算单位:", font=FONT, font_size=20, color=COLOR_RED
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(convert_label), run_time=0.3)

        calc3 = MathTex(
            r"= 40 \text{ km}",
            font_size=40, color=COLOR_REAL
        ).move_to(DOWN * 4.8)
        self.play(Write(calc3), run_time=0.6)

        ans_box = SurroundingRectangle(calc3, color=COLOR_REAL, buff=0.2, corner_radius=0.1)
        self.play(Create(ans_box), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q2), FadeOut(q3),
            FadeOut(formula_label), FadeOut(formula_row),
            FadeOut(sub_line), FadeOut(calc1), FadeOut(calc2),
            FadeOut(convert_label), FadeOut(calc3), FadeOut(ans_box),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 例题3 求图上距离
    # ------------------------------------------------------------------
    def scene_7_example_3(self):
        title = Text(
            "例题 3: 求图上距离", font=FONT, font_size=32, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 题目
        q1 = Text(
            "实际距离为 600m,", font=FONT, font_size=22, color=COLOR_REAL
        ).move_to(UP * 4.8)
        q2 = Text(
            "比例尺为 1:20000,", font=FONT, font_size=22, color=COLOR_SCALE
        ).move_to(UP * 4.0)
        q3 = Text(
            "画在图上应为多少厘米?", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(UP * 3.2)

        self.play(FadeIn(q1), run_time=0.4)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(q3), run_time=0.4)
        self.wait(0.5)

        # 解题
        formula_label = Text(
            "公式:", font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(UP * 2.0 + LEFT * 3)

        f_a = Text("图上距离", font=FONT, font_size=24, color=COLOR_MAP)
        f_eq = MathTex(r"=", font_size=30)
        f_b = Text("实际距离", font=FONT, font_size=24, color=COLOR_REAL)
        f_times = MathTex(r"\times", font_size=30)
        f_c = Text("比例尺", font=FONT, font_size=24, color=COLOR_SCALE)
        formula_row = VGroup(f_a, f_eq, f_b, f_times, f_c).arrange(
            RIGHT, buff=0.12
        ).move_to(UP * 1.0)

        self.play(FadeIn(formula_label), FadeIn(formula_row), run_time=0.6)

        # 统一单位
        step1 = Text(
            "先统一单位: 600m = 60000cm", font=FONT, font_size=20, color=COLOR_RED
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(step1), run_time=0.5)

        # 代入
        sub_line = MathTex(
            r"= 60000 \times \frac{1}{20000}",
            font_size=32
        ).move_to(DOWN * 1.4)
        self.play(Write(sub_line), run_time=0.8)

        calc1 = MathTex(
            r"= \frac{60000}{20000}",
            font_size=32
        ).move_to(DOWN * 2.8)
        self.play(Write(calc1), run_time=0.6)

        calc2 = MathTex(
            r"= 3 \text{ cm}",
            font_size=40, color=COLOR_MAP
        ).move_to(DOWN * 4.2)
        self.play(Write(calc2), run_time=0.6)

        ans_box = SurroundingRectangle(calc2, color=COLOR_MAP, buff=0.2, corner_radius=0.1)
        self.play(Create(ans_box), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q2), FadeOut(q3),
            FadeOut(formula_label), FadeOut(formula_row),
            FadeOut(step1), FadeOut(sub_line), FadeOut(calc1),
            FadeOut(calc2), FadeOut(ans_box),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------
    def scene_8_summary(self):
        title = Text(
            "知识总结", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 总结卡片
        cards = []
        card_data = [
            ("1", "比例尺 = 图上距离 : 实际距离", COLOR_SCALE),
            ("2", "实际距离 = 图上距离 / 比例尺", COLOR_REAL),
            ("3", "图上距离 = 实际距离 x 比例尺", COLOR_MAP),
            ("4", "计算前必须统一单位!", COLOR_RED),
        ]

        y_start = 4.0
        for i, (num, text, color) in enumerate(card_data):
            y = y_start - i * 1.8

            card_bg = RoundedRectangle(
                width=7.5, height=1.3, corner_radius=0.15,
                color=color, stroke_width=2, fill_opacity=0.08
            ).move_to(UP * y)

            num_circle = Circle(
                radius=0.3, color=color, fill_opacity=0.9, stroke_width=0
            ).move_to(card_bg.get_left() + RIGHT * 0.6)
            num_text = Text(
                num, font=FONT, font_size=24, color=WHITE
            ).move_to(num_circle.get_center())

            content = Text(
                text, font=FONT, font_size=22, color=WHITE
            ).move_to(card_bg.get_center() + RIGHT * 0.3)

            card = VGroup(card_bg, num_circle, num_text, content)
            cards.append(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.6)
            self.wait(0.3)

        # 数值 vs 线段
        type_title = Text(
            "两种形式:", font=FONT, font_size=22, color=COLOR_ACCENT
        ).move_to(DOWN * 3.8)

        type1 = VGroup(
            Text("数值比例尺:", font=FONT, font_size=20, color=COLOR_ACCENT),
            MathTex(r"1:1000000", font_size=28),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.8)

        type2 = VGroup(
            Text("线段比例尺:", font=FONT, font_size=20, color=COLOR_PINK),
            Text("直观标尺", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 5.8)

        self.play(FadeIn(type_title), run_time=0.4)
        self.play(FadeIn(type1), FadeIn(type2), run_time=0.6)
        self.wait(2.0)

        # 清理
        all_cards = VGroup(*cards)
        self.play(
            FadeOut(title), FadeOut(all_cards),
            FadeOut(type_title), FadeOut(type1), FadeOut(type2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------
    def scene_9_outro(self):
        # 作者信息
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 小装饰
        icons = VGroup(
            Circle(radius=0.25, color=COLOR_MAP, fill_opacity=0.8).shift(LEFT * 2),
            Circle(radius=0.25, color=COLOR_REAL, fill_opacity=0.8).shift(LEFT * 1),
            Circle(radius=0.25, color=COLOR_SCALE, fill_opacity=0.8),
            Circle(radius=0.25, color=COLOR_ACCENT, fill_opacity=0.8).shift(RIGHT * 1),
            Circle(radius=0.25, color=COLOR_PINK, fill_opacity=0.8).shift(RIGHT * 2),
        ).move_to(DOWN * 2.5)

        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )

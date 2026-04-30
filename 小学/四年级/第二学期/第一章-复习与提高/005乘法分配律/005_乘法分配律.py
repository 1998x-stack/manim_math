"""
005_乘法分配律.py — 乘法分配律 教学动画

知识点: 乘法分配律
  - 核心公式: (a + b) × c = a × c + b × c
  - 正用: 102×15 = (100+2)×15 = 100×15 + 2×15 = 1530
  - 逆用: 35×7 + 65×7 = (35+65)×7 = 700
年级: 四年级第二学期
格式: TikTok 竖屏 (1080x1920)
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
BG_COLOR     = "#1a1a2e"
COLOR_A      = "#3b82f6"   # 蓝色 — a 部分
COLOR_B      = "#22c55e"   # 绿色 — b 部分
COLOR_C      = "#f59e0b"   # 橙色 — c (乘数)
COLOR_HL     = "#fbbf24"   # 黄色 高亮
COLOR_RESULT = "#ef4444"   # 红色 结果
COLOR_AUTHOR = "#6b7280"   # 灰色作者
FONT         = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class DistributiveLawLesson(Scene):
    """
    乘法分配律教学动画
    场景顺序:
      1. 开场钩子
      2. 面积图直观理解
      3. 字母公式推导
      4. 正用示例 102×15
      5. 逆用示例 35×7 + 65×7
      6. 总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_area_model()
        self.scene_3_formula()
        self.scene_4_forward_example()
        self.scene_5_reverse_example()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 场景 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息（固定顶部）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 大标题
        title = Text("乘法分配律", font=FONT, font_size=52, color=COLOR_HL)
        title.move_to(UP * 5.2)

        hook = Text("怎样快速算 102×15 ？", font=FONT, font_size=34, color=WHITE)
        hook.move_to(UP * 4.0)

        hint = Text("用分配律，秒算！", font=FONT, font_size=28, color=COLOR_A)
        hint.move_to(UP * 3.1)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(hook),
            FadeOut(hint),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 场景 2: 面积模型直观理解
    # ------------------------------------------------------------------
    def scene_2_area_model(self):
        # 场景标题
        scene_title = Text("面积模型理解", font=FONT, font_size=32, color=COLOR_HL)
        scene_title.move_to(UP * 6.5)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 矩形参数（精确计算）
        # 总宽 = a + b，高 = c
        a_width = 2.5
        b_width = 1.5
        c_height = 2.0
        total_width = a_width + b_width  # 4.0

        # 坐标基准：中心在 y = 1.5
        rect_center_y = 1.5
        left_x = -total_width / 2           # -2.0
        mid_x  = left_x + a_width           # 0.5
        right_x = left_x + total_width      # 2.0
        bottom_y = rect_center_y - c_height / 2   # 0.5
        top_y    = rect_center_y + c_height / 2   # 2.5

        # ---- 大矩形（(a+b)×c）----
        big_rect = Rectangle(
            width=total_width, height=c_height,
            color=WHITE, stroke_width=2.5
        ).move_to([left_x + total_width / 2, rect_center_y, 0])

        # ---- 左矩形（a×c，蓝色）----
        rect_a = Rectangle(
            width=a_width, height=c_height,
            color=COLOR_A, fill_color=COLOR_A, fill_opacity=0.35,
            stroke_width=2
        ).move_to([left_x + a_width / 2, rect_center_y, 0])

        # ---- 右矩形（b×c，绿色）----
        rect_b = Rectangle(
            width=b_width, height=c_height,
            color=COLOR_B, fill_color=COLOR_B, fill_opacity=0.35,
            stroke_width=2
        ).move_to([mid_x + b_width / 2, rect_center_y, 0])

        # ---- 分割线 ----
        divider = DashedLine(
            start=[mid_x, bottom_y, 0],
            end=[mid_x, top_y, 0],
            color=WHITE, stroke_width=1.5, dash_length=0.12
        )

        # ---- 标注 a, b, c ----
        label_a = MathTex("a", color=COLOR_A, font_size=38)
        label_a.move_to([left_x + a_width / 2, top_y + 0.4, 0])

        label_b = MathTex("b", color=COLOR_B, font_size=38)
        label_b.move_to([mid_x + b_width / 2, top_y + 0.4, 0])

        label_c = MathTex("c", color=COLOR_C, font_size=38)
        label_c.move_to([left_x - 0.45, rect_center_y, 0])

        # ---- 面积标注 ----
        area_a_text = Text("a×c", font=FONT, font_size=26, color=COLOR_A)
        area_a_text.move_to([left_x + a_width / 2, rect_center_y, 0])

        area_b_text = Text("b×c", font=FONT, font_size=26, color=COLOR_B)
        area_b_text.move_to([mid_x + b_width / 2, rect_center_y, 0])

        # 动画
        self.play(Create(big_rect), run_time=0.8)
        self.play(
            FadeIn(rect_a), FadeIn(rect_b),
            Create(divider),
            run_time=0.6,
        )
        self.play(
            Write(label_a), Write(label_b), Write(label_c),
            run_time=0.6,
        )
        self.play(
            FadeIn(area_a_text), FadeIn(area_b_text),
            run_time=0.5,
        )
        self.wait(0.8)

        # 在矩形下方写等式
        eq_text = Text("(a+b)×c = a×c + b×c", font=FONT, font_size=28, color=WHITE)
        eq_text.move_to(UP * (-0.5))
        self.play(Write(eq_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(scene_title),
            FadeOut(big_rect), FadeOut(rect_a), FadeOut(rect_b),
            FadeOut(divider),
            FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
            FadeOut(area_a_text), FadeOut(area_b_text),
            FadeOut(eq_text),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 场景 3: 字母公式推导
    # ------------------------------------------------------------------
    def scene_3_formula(self):
        scene_title = Text("乘法分配律", font=FONT, font_size=36, color=COLOR_HL)
        scene_title.move_to(UP * 6.5)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 公式展示区域，居中
        formula_label = Text("核心公式：", font=FONT, font_size=28, color=WHITE)
        formula_label.move_to(UP * 4.8)
        self.play(FadeIn(formula_label), run_time=0.4)

        # 公式：(a+b)×c = a×c + b×c
        formula = MathTex(
            r"(a + b) \times c = a \times c + b \times c",
            font_size=42,
            color=WHITE,
        )
        formula.move_to(UP * 3.7)
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)

        # 颜色标注
        formula_colored = MathTex(
            r"(", r"a", r"+", r"b", r")", r"\times", r"c",
            r"=",
            r"a", r"\times", r"c",
            r"+",
            r"b", r"\times", r"c",
            font_size=42,
        )
        formula_colored.set_color_by_tex("a", COLOR_A)
        formula_colored.set_color_by_tex("b", COLOR_B)
        formula_colored.set_color_by_tex("c", COLOR_C)
        formula_colored.move_to(UP * 3.7)

        self.play(TransformMatchingTex(formula, formula_colored), run_time=0.8)
        self.wait(0.5)

        # 说明文字：两个数的和与一个数相乘
        desc1 = Text("两个数的和", font=FONT, font_size=24, color=COLOR_HL)
        desc1.move_to(UP * 2.5)
        brace1 = Brace(
            VGroup(formula_colored[0], formula_colored[1],
                   formula_colored[2], formula_colored[3], formula_colored[4]),
            UP, buff=0.1, color=COLOR_HL
        )

        self.play(FadeIn(brace1), FadeIn(desc1), run_time=0.6)
        self.wait(0.5)

        desc2 = Text("可以先分别×c，再相加", font=FONT, font_size=24, color=WHITE)
        desc2.move_to(UP * 1.4)
        arrow_right = Arrow(
            start=UP * 2.1, end=UP * 1.8,
            color=COLOR_HL, buff=0.1, stroke_width=3
        )
        self.play(Create(arrow_right), FadeIn(desc2), run_time=0.6)
        self.wait(1.0)

        # 逆用说明
        reverse_label = Text("也可以逆用：", font=FONT, font_size=26, color=COLOR_RESULT)
        reverse_label.move_to(UP * 0.3)
        reverse_formula = MathTex(
            r"a \times c + b \times c = (a + b) \times c",
            font_size=38, color=COLOR_RESULT,
        )
        reverse_formula.move_to(UP * (-0.6))
        self.play(FadeIn(reverse_label), run_time=0.4)
        self.play(Write(reverse_formula), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(scene_title),
            FadeOut(formula_label),
            FadeOut(formula_colored),
            FadeOut(brace1),
            FadeOut(desc1),
            FadeOut(arrow_right),
            FadeOut(desc2),
            FadeOut(reverse_label),
            FadeOut(reverse_formula),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 场景 4: 正用示例 102×15
    # ------------------------------------------------------------------
    def scene_4_forward_example(self):
        scene_title = Text("正用：分拆简便计算", font=FONT, font_size=32, color=COLOR_HL)
        scene_title.move_to(UP * 6.5)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 题目
        problem_label = Text("计算  102 × 15", font=FONT, font_size=34, color=WHITE)
        problem_label.move_to(UP * 5.5)
        self.play(Write(problem_label), run_time=0.6)
        self.wait(0.4)

        # Step 1: 102 = 100 + 2
        step1_title = Text("第一步：把 102 拆开", font=FONT, font_size=26, color=COLOR_C)
        step1_title.move_to(UP * 4.3)
        self.play(FadeIn(step1_title), run_time=0.4)

        step1 = MathTex(r"102 \times 15", font_size=40)
        step1.move_to(UP * 3.3)
        self.play(Write(step1), run_time=0.5)

        step1b = MathTex(r"= (100 + 2) \times 15", font_size=40)
        step1b.move_to(UP * 2.5)
        arrow1 = Arrow(
            start=step1.get_bottom() + DOWN * 0.05,
            end=step1b.get_top() + UP * 0.05,
            color=COLOR_C, buff=0.08, stroke_width=2.5,
        )
        self.play(Create(arrow1), Write(step1b), run_time=0.7)
        self.wait(0.4)

        # Step 2: 分配律展开
        step2_title = Text("第二步：用分配律展开", font=FONT, font_size=26, color=COLOR_A)
        step2_title.move_to(UP * 1.5)
        self.play(FadeIn(step2_title), run_time=0.4)

        step2 = MathTex(
            r"= 100 \times 15 + 2 \times 15",
            font_size=40,
        )
        step2.move_to(UP * 0.6)
        arrow2 = Arrow(
            start=step1b.get_bottom() + DOWN * 0.05,
            end=step2.get_top() + UP * 0.05,
            color=COLOR_A, buff=0.08, stroke_width=2.5,
        )
        self.play(Create(arrow2), Write(step2), run_time=0.7)
        self.wait(0.4)

        # Step 3: 分别计算
        step3_title = Text("第三步：分别计算", font=FONT, font_size=26, color=COLOR_B)
        step3_title.move_to(DOWN * 0.5)
        self.play(FadeIn(step3_title), run_time=0.4)

        step3 = MathTex(
            r"= 1500 + 30",
            font_size=40,
        )
        step3.move_to(DOWN * 1.4)
        arrow3 = Arrow(
            start=step2.get_bottom() + DOWN * 0.05,
            end=step3.get_top() + UP * 0.05,
            color=COLOR_B, buff=0.08, stroke_width=2.5,
        )
        self.play(Create(arrow3), Write(step3), run_time=0.7)
        self.wait(0.4)

        # 结果
        result = MathTex(r"= 1530", font_size=48, color=COLOR_RESULT)
        result.move_to(DOWN * 2.4)
        box = SurroundingRectangle(result, color=COLOR_RESULT, buff=0.15, stroke_width=2.5)
        self.play(Write(result), Create(box), run_time=0.7)
        self.play(Indicate(result, scale_factor=1.15, color=COLOR_HL), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title), FadeOut(problem_label),
            FadeOut(step1_title), FadeOut(step1), FadeOut(arrow1), FadeOut(step1b),
            FadeOut(step2_title), FadeOut(step2), FadeOut(arrow2),
            FadeOut(step3_title), FadeOut(step3), FadeOut(arrow3),
            FadeOut(result), FadeOut(box),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 场景 5: 逆用示例 35×7 + 65×7
    # ------------------------------------------------------------------
    def scene_5_reverse_example(self):
        scene_title = Text("逆用：合并简便计算", font=FONT, font_size=32, color=COLOR_HL)
        scene_title.move_to(UP * 6.5)
        self.play(FadeIn(scene_title), run_time=0.4)

        problem_label = Text("计算  35×7 + 65×7", font=FONT, font_size=34, color=WHITE)
        problem_label.move_to(UP * 5.5)
        self.play(Write(problem_label), run_time=0.6)
        self.wait(0.4)

        # 观察：两项都有 ×7
        observe = Text("观察：两项都含有 ×7", font=FONT, font_size=26, color=COLOR_C)
        observe.move_to(UP * 4.3)
        self.play(FadeIn(observe), run_time=0.5)

        step1 = MathTex(
            r"35 \times 7 + 65 \times 7",
            font_size=40,
        )
        step1.move_to(UP * 3.3)
        self.play(Write(step1), run_time=0.6)
        self.wait(0.4)

        # 提取公因数 7
        step2_title = Text("逆用分配律，提取公因数 7", font=FONT, font_size=26, color=COLOR_A)
        step2_title.move_to(UP * 2.3)
        self.play(FadeIn(step2_title), run_time=0.4)

        step2 = MathTex(
            r"= (35 + 65) \times 7",
            font_size=40,
        )
        step2.move_to(UP * 1.4)
        arrow1 = Arrow(
            start=step1.get_bottom() + DOWN * 0.05,
            end=step2.get_top() + UP * 0.05,
            color=COLOR_A, buff=0.08, stroke_width=2.5,
        )
        self.play(Create(arrow1), Write(step2), run_time=0.7)
        self.wait(0.4)

        # 计算括号
        step3_title = Text("先算括号内", font=FONT, font_size=26, color=COLOR_B)
        step3_title.move_to(UP * 0.4)
        self.play(FadeIn(step3_title), run_time=0.4)

        step3 = MathTex(r"= 100 \times 7", font_size=40)
        step3.move_to(DOWN * 0.5)
        arrow2 = Arrow(
            start=step2.get_bottom() + DOWN * 0.05,
            end=step3.get_top() + UP * 0.05,
            color=COLOR_B, buff=0.08, stroke_width=2.5,
        )
        self.play(Create(arrow2), Write(step3), run_time=0.7)
        self.wait(0.4)

        # 结果
        result = MathTex(r"= 700", font_size=52, color=COLOR_RESULT)
        result.move_to(DOWN * 1.7)
        arrow3 = Arrow(
            start=step3.get_bottom() + DOWN * 0.05,
            end=result.get_top() + UP * 0.05,
            color=COLOR_RESULT, buff=0.08, stroke_width=2.5,
        )
        box = SurroundingRectangle(result, color=COLOR_RESULT, buff=0.15, stroke_width=2.5)
        self.play(Create(arrow3), Write(result), Create(box), run_time=0.7)
        self.play(Indicate(result, scale_factor=1.15, color=COLOR_HL), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(scene_title), FadeOut(problem_label),
            FadeOut(observe),
            FadeOut(step1), FadeOut(arrow1), FadeOut(step2),
            FadeOut(step2_title),
            FadeOut(step3_title), FadeOut(step3), FadeOut(arrow2),
            FadeOut(arrow3), FadeOut(result), FadeOut(box),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 场景 6: 总结
    # ------------------------------------------------------------------
    def scene_6_summary(self):
        scene_title = Text("总结", font=FONT, font_size=36, color=COLOR_HL)
        scene_title.move_to(UP * 6.5)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 核心公式框
        formula_title = Text("乘法分配律", font=FONT, font_size=30, color=COLOR_HL)
        formula_title.move_to(UP * 5.5)
        self.play(Write(formula_title), run_time=0.5)

        formula = MathTex(
            r"(a+b)\times c = a\times c + b\times c",
            font_size=36, color=WHITE,
        )
        formula.move_to(UP * 4.6)
        box0 = SurroundingRectangle(formula, color=COLOR_HL, buff=0.2, stroke_width=2.5)
        self.play(Write(formula), Create(box0), run_time=0.8)
        self.wait(0.5)

        # 两种用法卡片
        card_forward = VGroup(
            Text("正用", font=FONT, font_size=26, color=COLOR_A),
            Text("把一个因数拆开，分别乘", font=FONT, font_size=22, color=WHITE),
            Text("→ 102×15 = 100×15 + 2×15", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        card_forward.move_to(UP * 2.8)

        card_reverse = VGroup(
            Text("逆用", font=FONT, font_size=26, color=COLOR_B),
            Text("提取公因数，合并成一项", font=FONT, font_size=22, color=WHITE),
            Text("→ 35×7 + 65×7 = (35+65)×7", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        card_reverse.move_to(UP * 1.2)

        box1 = SurroundingRectangle(card_forward, color=COLOR_A, buff=0.2, stroke_width=2)
        box2 = SurroundingRectangle(card_reverse, color=COLOR_B, buff=0.2, stroke_width=2)

        self.play(FadeIn(card_forward), Create(box1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(card_reverse), Create(box2), run_time=0.6)
        self.wait(0.5)

        # 关键提示
        tip = Text("关键：找共同的乘数！", font=FONT, font_size=28, color=COLOR_HL)
        tip.move_to(DOWN * 0.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(scene_title),
            FadeOut(formula_title), FadeOut(formula), FadeOut(box0),
            FadeOut(card_forward), FadeOut(box1),
            FadeOut(card_reverse), FadeOut(box2),
            FadeOut(tip),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 场景 7: 片尾
    # ------------------------------------------------------------------
    def scene_7_outro(self):
        # 作者信息放大居中
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author, author_name),
            run_time=0.6,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.6)
        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.5)

        # 小装饰：三个圆点闪烁
        dots = VGroup(*[
            Dot(radius=0.15, color=c).shift(RIGHT * 1.2 * (i - 1) + DOWN * 2.0)
            for i, c in enumerate([COLOR_A, COLOR_HL, COLOR_B])
        ])
        self.play(*[GrowFromCenter(d) for d in dots], run_time=0.5)
        self.play(
            dots[0].animate.set_color(COLOR_B),
            dots[1].animate.set_color(COLOR_A),
            dots[2].animate.set_color(COLOR_HL),
            run_time=0.6,
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(dots),
            run_time=0.8,
        )

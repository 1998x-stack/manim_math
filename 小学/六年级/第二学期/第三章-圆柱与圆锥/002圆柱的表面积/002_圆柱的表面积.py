"""
002_圆柱的表面积.py — 圆柱的表面积 教学动画

知识点: 圆柱侧面积、表面积的推导与计算
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 制作一个罐头需要多少材料?
  2. 复习圆柱结构: 两个底面 + 侧面
  3. 侧面展开: 侧面展开成长方形, 推导侧面积公式
  4. 底面积: 圆的面积
  5. 表面积公式推导: S表 = S侧 + 2S底
  6. 例题应用: 实际计算
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
COLOR_CYLINDER = "#3b82f6"
COLOR_TOP = "#60a5fa"
COLOR_BOTTOM = "#2563eb"
COLOR_SIDE = "#8b5cf6"
COLOR_HEIGHT = "#f59e0b"
COLOR_HL = "#fbbf24"
COLOR_RESULT = "#22c55e"
COLOR_ACCENT = "#ef4444"
COLOR_AUTHOR = "#6b7280"
COLOR_FORMULA = "#38bdf8"
FONT = "Noto Sans CJK SC"


# ======================================================================
# 辅助: 绘制 2D 圆柱示意图
# ======================================================================

def create_cylinder_2d(
    center=ORIGIN, width=2.4, height=3.0,
    ellipse_ratio=0.3, stroke_color=WHITE, fill_top=None,
    fill_bottom=None, fill_side=None, stroke_width=2.5
):
    """
    用 2D 元素组合绘制圆柱示意图 (前视图)
    """
    rx = width / 2
    ry = width / 2 * ellipse_ratio
    cx, cy = center[0], center[1]
    top_cy = cy + height / 2
    bot_cy = cy - height / 2

    parts = {}

    # --- 侧面填充矩形 ---
    if fill_side:
        side_rect = Rectangle(
            width=width, height=height,
            fill_color=fill_side, fill_opacity=0.25,
            stroke_width=0
        ).move_to([cx, cy, 0])
        parts["side_fill"] = side_rect

    # --- 底部椭圆 ---
    bot_front = Arc(
        radius=rx, start_angle=-PI, angle=PI,
        arc_center=[cx, bot_cy, 0], color=stroke_color,
        stroke_width=stroke_width
    )
    bot_front.stretch(ry / rx, 1)
    bot_front.move_to([cx, bot_cy, 0])

    bot_back = DashedVMobject(
        Arc(
            radius=rx, start_angle=0, angle=PI,
            arc_center=[cx, bot_cy, 0], color=stroke_color,
            stroke_width=stroke_width * 0.6
        ).stretch(ry / rx, 1).move_to([cx, bot_cy, 0]),
        num_dashes=12
    )
    parts["bot_front"] = bot_front
    parts["bot_back"] = bot_back

    if fill_bottom:
        bot_fill = Ellipse(
            width=width, height=width * ellipse_ratio * 2,
            fill_color=fill_bottom, fill_opacity=0.35,
            stroke_width=0
        ).move_to([cx, bot_cy, 0])
        parts["bot_fill"] = bot_fill

    # --- 左右母线 ---
    left_line = Line(
        [cx - rx, bot_cy, 0], [cx - rx, top_cy, 0],
        color=stroke_color, stroke_width=stroke_width
    )
    right_line = Line(
        [cx + rx, bot_cy, 0], [cx + rx, top_cy, 0],
        color=stroke_color, stroke_width=stroke_width
    )
    parts["left_line"] = left_line
    parts["right_line"] = right_line

    # --- 顶部椭圆 ---
    top_ellipse = Ellipse(
        width=width, height=width * ellipse_ratio * 2,
        color=stroke_color, stroke_width=stroke_width
    ).move_to([cx, top_cy, 0])
    if fill_top:
        top_ellipse.set_fill(fill_top, opacity=0.4)
    parts["top_ellipse"] = top_ellipse

    # 组装
    group = VGroup()
    for key in ["side_fill", "bot_fill", "bot_back", "bot_front",
                "left_line", "right_line", "top_ellipse"]:
        if key in parts:
            group.add(parts[key])

    group.parts = parts
    return group


# ======================================================================
# 主场景
# ======================================================================

class CylinderSurfaceAreaLesson(Scene):
    """
    圆柱的表面积 教学动画场景

    场景顺序:
      1. 开场钩子
      2. 复习圆柱结构
      3. 侧面展开 -> 侧面积公式
      4. 底面积
      5. 表面积公式推导
      6. 例题应用
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_structure_review()
        self.scene_3_lateral_area()
        self.scene_4_base_area()
        self.scene_5_total_surface_area()
        self.scene_6_example()
        self.scene_7_summary()
        self.scene_8_outro()

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

        # 钩子问题
        hook = Text(
            "制作一个罐头盒,\n需要多少铁皮?",
            font=FONT, font_size=38, color=COLOR_HL,
            line_spacing=1.4
        ).move_to(UP * 4.5)
        self.play(Write(hook), run_time=1.0)

        # 罐头盒圆柱
        can = create_cylinder_2d(
            center=[0, 0.5, 0], width=2.8, height=3.2,
            ellipse_ratio=0.25, stroke_color=COLOR_CYLINDER,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2.5
        )
        self.play(FadeIn(can, shift=UP * 0.3), run_time=1.0)
        self.wait(0.8)

        # 问号强调
        question = Text(
            "这就是圆柱的表面积问题!",
            font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(can), FadeOut(question),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 复习圆柱结构
    # ------------------------------------------------------------------
    def scene_2_structure_review(self):
        title = Text(
            "圆柱的组成", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 圆柱
        cx, cy_cyl = 0, 1.5
        cyl_w, cyl_h = 3.0, 3.5
        rx = cyl_w / 2
        top_cy = cy_cyl + cyl_h / 2
        bot_cy = cy_cyl - cyl_h / 2

        cyl = create_cylinder_2d(
            center=[cx, cy_cyl, 0], width=cyl_w, height=cyl_h,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2.5
        )
        self.play(FadeIn(cyl), run_time=0.8)

        # 标注各部分
        # 上底面
        top_arrow = Arrow(
            start=[2.8, top_cy + 0.6, 0], end=[0.5, top_cy, 0],
            color=COLOR_TOP, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        top_label = Text("上底面", font=FONT, font_size=20, color=COLOR_TOP
                         ).next_to(top_arrow.get_start(), RIGHT, buff=0.1)
        self.play(GrowArrow(top_arrow), FadeIn(top_label), run_time=0.5)

        # 下底面
        bot_arrow = Arrow(
            start=[2.8, bot_cy - 0.6, 0], end=[0.5, bot_cy, 0],
            color=COLOR_BOTTOM, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        bot_label = Text("下底面", font=FONT, font_size=20, color=COLOR_BOTTOM
                         ).next_to(bot_arrow.get_start(), RIGHT, buff=0.1)
        self.play(GrowArrow(bot_arrow), FadeIn(bot_label), run_time=0.5)

        # 侧面
        side_arrow = Arrow(
            start=[-2.8, cy_cyl, 0], end=[-rx - 0.05, cy_cyl, 0],
            color=COLOR_SIDE, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        side_label = Text("侧面", font=FONT, font_size=20, color=COLOR_SIDE
                          ).next_to(side_arrow.get_start(), LEFT, buff=0.1)
        self.play(GrowArrow(side_arrow), FadeIn(side_label), run_time=0.5)

        # 分解提示
        decompose = Text(
            "表面积 = 侧面积 + 2 个底面积",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(decompose, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl),
            FadeOut(top_arrow), FadeOut(top_label),
            FadeOut(bot_arrow), FadeOut(bot_label),
            FadeOut(side_arrow), FadeOut(side_label),
            FadeOut(decompose),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 侧面展开 -> 侧面积公式
    # ------------------------------------------------------------------
    def scene_3_lateral_area(self):
        title = Text(
            "侧面积", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 小圆柱
        cyl = create_cylinder_2d(
            center=[-2.0, 3.2, 0], width=2.0, height=2.5,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, stroke_width=2
        )
        self.play(FadeIn(cyl), run_time=0.6)

        # 在圆柱上标注 r 和 h
        r_line_cyl = Line(
            [-2.0, 3.2 + 1.25, 0], [-2.0 + 1.0, 3.2 + 1.25, 0],
            color=COLOR_HL, stroke_width=2
        )
        r_label_cyl = MathTex("r", color=COLOR_HL, font_size=24
                               ).next_to(r_line_cyl, UP, buff=0.06)

        h_brace_cyl = Brace(
            Line([-2.0 + 1.0, 3.2 - 1.25, 0], [-2.0 + 1.0, 3.2 + 1.25, 0]),
            direction=RIGHT, color=COLOR_HEIGHT, buff=0.1
        )
        h_label_cyl = MathTex("h", color=COLOR_HEIGHT, font_size=24
                               ).next_to(h_brace_cyl, RIGHT, buff=0.1)
        self.play(
            Create(r_line_cyl), FadeIn(r_label_cyl),
            FadeIn(h_brace_cyl), FadeIn(h_label_cyl),
            run_time=0.6
        )

        # 展开提示
        unfold_hint = Text(
            "沿母线剪开, 展开侧面",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to([0, 1.2, 0])
        arrow_unfold = Arrow(
            start=[-0.8, 1.8, 0], end=[1.0, 0.5, 0],
            color=COLOR_HL, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        self.play(FadeIn(unfold_hint), GrowArrow(arrow_unfold), run_time=0.6)

        # 展开后的长方形
        display_rect_w = 6.0
        display_rect_h = 2.5
        rect = Rectangle(
            width=display_rect_w, height=display_rect_h,
            color=COLOR_SIDE, fill_opacity=0.2,
            stroke_width=2.5
        ).move_to([0.5, -1.8, 0])

        self.play(
            FadeOut(unfold_hint), FadeOut(arrow_unfold),
            FadeIn(rect, shift=DOWN * 0.3),
            run_time=0.8
        )

        # 标注长方形尺寸
        # 长 = 底面周长
        w_brace = Brace(rect, DOWN, color=COLOR_HL, buff=0.1)
        w_text = VGroup(
            Text("底面周长 C", font=FONT, font_size=18, color=COLOR_HL),
            MathTex(r"= 2\pi r", color=COLOR_HL, font_size=24)
        ).arrange(RIGHT, buff=0.12)
        w_text.next_to(w_brace, DOWN, buff=0.15)

        # 宽 = 高
        h_brace_rect = Brace(rect, RIGHT, color=COLOR_HEIGHT, buff=0.1)
        h_text = VGroup(
            Text("高", font=FONT, font_size=18, color=COLOR_HEIGHT),
            MathTex(r"= h", color=COLOR_HEIGHT, font_size=24)
        ).arrange(RIGHT, buff=0.08)
        h_text.next_to(h_brace_rect, RIGHT, buff=0.15)

        self.play(
            FadeIn(w_brace), FadeIn(w_text),
            FadeIn(h_brace_rect), FadeIn(h_text),
            run_time=0.8
        )
        self.wait(1.0)

        # 侧面积公式推导
        formula_title = Text(
            "侧面积 = 长 x 宽", font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(formula_title), run_time=0.5)

        formula_1 = MathTex(
            r"S", r"=", r"C", r"\times", r"h",
            font_size=36
        ).move_to(DOWN * 5.3)
        formula_1[0].set_color(COLOR_SIDE)
        formula_1[2].set_color(COLOR_HL)
        formula_1[4].set_color(COLOR_HEIGHT)
        self.play(Write(formula_1), run_time=0.8)
        self.wait(0.5)

        formula_2 = MathTex(
            r"S", r"=", r"2\pi r", r"\times", r"h",
            font_size=36
        ).move_to(DOWN * 6.1)
        formula_2[0].set_color(COLOR_SIDE)
        formula_2[2].set_color(COLOR_HL)
        formula_2[4].set_color(COLOR_HEIGHT)
        self.play(Write(formula_2), run_time=0.8)

        # 最终公式高亮
        final_box = SurroundingRectangle(
            formula_2, color=COLOR_RESULT, buff=0.2, stroke_width=2
        )
        final_label = VGroup(
            Text("侧面积", font=FONT, font_size=20, color=COLOR_RESULT),
            MathTex(r"S_{\text{lat}} = 2\pi rh", color=COLOR_RESULT, font_size=28)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 7.2)

        self.play(Create(final_box), run_time=0.5)
        self.play(FadeIn(final_label), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl),
            FadeOut(r_line_cyl), FadeOut(r_label_cyl),
            FadeOut(h_brace_cyl), FadeOut(h_label_cyl),
            FadeOut(rect),
            FadeOut(w_brace), FadeOut(w_text),
            FadeOut(h_brace_rect), FadeOut(h_text),
            FadeOut(formula_title), FadeOut(formula_1),
            FadeOut(formula_2), FadeOut(final_box), FadeOut(final_label),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 底面积
    # ------------------------------------------------------------------
    def scene_4_base_area(self):
        title = Text(
            "底面积", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 底面是圆
        explain = Text(
            "底面是圆, 面积用圆的面积公式",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(explain), run_time=0.5)

        # 画一个圆
        circle = Circle(
            radius=1.8, color=COLOR_BOTTOM, fill_opacity=0.25,
            stroke_width=2.5
        ).move_to([0, 1.5, 0])
        self.play(Create(circle), run_time=0.8)

        # 标注半径
        center_dot = Dot([0, 1.5, 0], radius=0.05, color=WHITE)
        r_line = Line(
            [0, 1.5, 0], [1.8, 1.5, 0],
            color=COLOR_HL, stroke_width=2.5
        )
        r_label = MathTex("r", color=COLOR_HL, font_size=30
                           ).next_to(r_line, UP, buff=0.08)
        self.play(
            FadeIn(center_dot), Create(r_line), FadeIn(r_label),
            run_time=0.6
        )

        # 面积公式
        formula_base = MathTex(
            r"S", r"=", r"\pi r^2",
            font_size=40
        ).move_to(DOWN * 1.5)
        formula_base[0].set_color(COLOR_BOTTOM)
        formula_base[2].set_color(COLOR_HL)
        self.play(Write(formula_base), run_time=0.8)
        self.wait(0.8)

        # 两个底面
        note = Text(
            "圆柱有两个底面, 所以:", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)

        formula_2base = MathTex(
            r"2S", r"=", r"2\pi r^2",
            font_size=40
        ).move_to(DOWN * 4.0)
        formula_2base[0].set_color(COLOR_BOTTOM)
        formula_2base[2].set_color(COLOR_HL)
        self.play(Write(formula_2base), run_time=0.8)

        box_2base = SurroundingRectangle(
            formula_2base, color=COLOR_RESULT, buff=0.2, stroke_width=2
        )
        self.play(Create(box_2base), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(circle), FadeOut(center_dot),
            FadeOut(r_line), FadeOut(r_label),
            FadeOut(formula_base), FadeOut(note),
            FadeOut(formula_2base), FadeOut(box_2base),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 表面积公式推导
    # ------------------------------------------------------------------
    def scene_5_total_surface_area(self):
        title = Text(
            "表面积公式", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 组成部分的图示
        # 侧面 (展开长方形)
        side_rect = Rectangle(
            width=4.0, height=2.0,
            color=COLOR_SIDE, fill_opacity=0.2, stroke_width=2
        ).move_to([-0.2, 3.0, 0])
        side_text = Text("侧面", font=FONT, font_size=20, color=COLOR_SIDE
                         ).next_to(side_rect, UP, buff=0.15)

        # 两个底面 (两个圆)
        base_1 = Circle(
            radius=0.8, color=COLOR_BOTTOM, fill_opacity=0.25, stroke_width=2
        ).move_to([-2.5, 0.3, 0])
        base_1_text = Text("底面1", font=FONT, font_size=18, color=COLOR_BOTTOM
                           ).next_to(base_1, DOWN, buff=0.15)

        base_2 = Circle(
            radius=0.8, color=COLOR_BOTTOM, fill_opacity=0.25, stroke_width=2
        ).move_to([2.5, 0.3, 0])
        base_2_text = Text("底面2", font=FONT, font_size=18, color=COLOR_BOTTOM
                           ).next_to(base_2, DOWN, buff=0.15)

        plus_1 = MathTex("+", font_size=36, color=WHITE).move_to([-0.2, 0.3, 0])

        self.play(
            FadeIn(side_rect), FadeIn(side_text),
            FadeIn(base_1), FadeIn(base_1_text),
            FadeIn(base_2), FadeIn(base_2_text),
            FadeIn(plus_1),
            run_time=1.0
        )
        self.wait(0.8)

        # 公式推导
        step_title = Text(
            "表面积 = 侧面积 + 2 x 底面积",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(step_title), run_time=0.5)

        # Step 1
        step1 = MathTex(
            r"S", r"=", r"2\pi rh", r"+", r"2\pi r^2",
            font_size=36
        ).move_to(DOWN * 2.8)
        step1[0].set_color(COLOR_RESULT)
        step1[2].set_color(COLOR_SIDE)
        step1[4].set_color(COLOR_BOTTOM)
        self.play(Write(step1), run_time=1.0)
        self.wait(0.8)

        # Step 2: 提取公因式
        factor_hint = Text(
            "提取公因式:", font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(factor_hint), run_time=0.4)

        step2 = MathTex(
            r"S", r"=", r"2\pi r", r"(", r"h", r"+", r"r", r")",
            font_size=40
        ).move_to(DOWN * 4.8)
        step2[0].set_color(COLOR_RESULT)
        step2[2].set_color(COLOR_FORMULA)
        step2[4].set_color(COLOR_HEIGHT)
        step2[6].set_color(COLOR_HL)
        self.play(Write(step2), run_time=1.0)

        # 最终公式高亮框
        final_box = SurroundingRectangle(
            step2, color=COLOR_RESULT, buff=0.25, stroke_width=2.5,
            corner_radius=0.1
        )
        self.play(Create(final_box), run_time=0.5)

        # 公式含义
        meaning = VGroup(
            Text("这就是圆柱表面积公式!", font=FONT, font_size=26, color=COLOR_RESULT),
        ).move_to(DOWN * 6.2)
        self.play(FadeIn(meaning, shift=UP * 0.2), run_time=0.6)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(side_rect), FadeOut(side_text),
            FadeOut(base_1), FadeOut(base_1_text),
            FadeOut(base_2), FadeOut(base_2_text),
            FadeOut(plus_1),
            FadeOut(step_title),
            FadeOut(step1), FadeOut(factor_hint),
            FadeOut(step2), FadeOut(final_box),
            FadeOut(meaning),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题应用
    # ------------------------------------------------------------------
    def scene_6_example(self):
        title = Text(
            "例题", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 题目
        problem = VGroup(
            Text("一个圆柱形罐头, ", font=FONT, font_size=22, color=WHITE),
            Text("底面半径 r = 5 cm,", font=FONT, font_size=22, color=COLOR_HL),
            Text("高 h = 10 cm,", font=FONT, font_size=22, color=COLOR_HEIGHT),
            Text("求它的表面积。", font=FONT, font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(UP * 3.8)
        self.play(
            LaggedStart(*[FadeIn(p, shift=RIGHT * 0.2) for p in problem],
                        lag_ratio=0.3),
            run_time=1.5
        )

        # 圆柱示意图
        cyl = create_cylinder_2d(
            center=[0, 0.8, 0], width=2.2, height=2.8,
            ellipse_ratio=0.25, stroke_color=COLOR_CYLINDER,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2
        )
        self.play(FadeIn(cyl), run_time=0.6)

        # 标注 r=5, h=10
        r_line = Line(
            [0, 0.8 + 1.4, 0], [1.1, 0.8 + 1.4, 0],
            color=COLOR_HL, stroke_width=2
        )
        r_val = MathTex("5", color=COLOR_HL, font_size=22
                         ).next_to(r_line, UP, buff=0.06)
        h_brace = Brace(
            Line([1.1, 0.8 - 1.4, 0], [1.1, 0.8 + 1.4, 0]),
            direction=RIGHT, color=COLOR_HEIGHT, buff=0.08
        )
        h_val = MathTex("10", color=COLOR_HEIGHT, font_size=22
                         ).next_to(h_brace, RIGHT, buff=0.08)
        self.play(
            Create(r_line), FadeIn(r_val),
            FadeIn(h_brace), FadeIn(h_val),
            run_time=0.5
        )
        self.wait(0.5)

        # 解题步骤
        step_label = Text("解:", font=FONT, font_size=24, color=WHITE
                          ).move_to([-3.5, -1.5, 0])
        self.play(FadeIn(step_label), run_time=0.3)

        # Step 1: 侧面积
        s1_title = Text(
            "1. 侧面积", font=FONT, font_size=20, color=COLOR_SIDE
        ).move_to([-2.2, -2.2, 0])
        s1_formula = MathTex(
            r"S_{\text{lat}}", r"=", r"2\pi rh",
            r"=", r"2\pi \times 5 \times 10",
            r"=", r"100\pi",
            font_size=24
        ).move_to([0, -2.9, 0])
        s1_formula[0].set_color(COLOR_SIDE)
        s1_formula[6].set_color(COLOR_SIDE)

        self.play(FadeIn(s1_title), run_time=0.3)
        self.play(Write(s1_formula), run_time=1.0)
        self.wait(0.5)

        # Step 2: 底面积
        s2_title = Text(
            "2. 两个底面积", font=FONT, font_size=20, color=COLOR_BOTTOM
        ).move_to([-1.8, -3.8, 0])
        s2_formula = MathTex(
            r"2S_{\text{base}}", r"=", r"2\pi r^2",
            r"=", r"2\pi \times 5^2",
            r"=", r"50\pi",
            font_size=24
        ).move_to([0, -4.5, 0])
        s2_formula[0].set_color(COLOR_BOTTOM)
        s2_formula[6].set_color(COLOR_BOTTOM)

        self.play(FadeIn(s2_title), run_time=0.3)
        self.play(Write(s2_formula), run_time=1.0)
        self.wait(0.5)

        # Step 3: 表面积
        s3_title = Text(
            "3. 表面积", font=FONT, font_size=20, color=COLOR_RESULT
        ).move_to([-2.4, -5.4, 0])
        s3_formula = MathTex(
            r"S", r"=", r"100\pi", r"+", r"50\pi",
            r"=", r"150\pi",
            font_size=28
        ).move_to([0, -6.1, 0])
        s3_formula[0].set_color(COLOR_RESULT)
        s3_formula[2].set_color(COLOR_SIDE)
        s3_formula[4].set_color(COLOR_BOTTOM)
        s3_formula[6].set_color(COLOR_RESULT)

        self.play(FadeIn(s3_title), run_time=0.3)
        self.play(Write(s3_formula), run_time=1.0)

        # 最终答案
        approx = MathTex(
            r"\approx 471.2 \text{ cm}^2",
            font_size=28, color=COLOR_RESULT
        ).move_to([0, -7.0, 0])
        answer_box = SurroundingRectangle(
            VGroup(s3_formula, approx), color=COLOR_RESULT,
            buff=0.2, stroke_width=2
        )
        self.play(Write(approx), Create(answer_box), run_time=0.8)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(problem),
            FadeOut(cyl), FadeOut(r_line), FadeOut(r_val),
            FadeOut(h_brace), FadeOut(h_val),
            FadeOut(step_label),
            FadeOut(s1_title), FadeOut(s1_formula),
            FadeOut(s2_title), FadeOut(s2_formula),
            FadeOut(s3_title), FadeOut(s3_formula),
            FadeOut(approx), FadeOut(answer_box),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------
    def scene_7_summary(self):
        title = Text(
            "知识总结", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 小圆柱
        cyl = create_cylinder_2d(
            center=[0, 3.0, 0], width=2.0, height=2.5,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2
        )
        self.play(FadeIn(cyl), run_time=0.5)

        # 要点卡片
        points_data = [
            ("1.", "侧面积", "S = 2\u03C0rh  (底面周长 x 高)", COLOR_SIDE),
            ("2.", "底面积", "S = \u03C0r\u00B2  (圆的面积)", COLOR_BOTTOM),
            ("3.", "表面积", "S = 2\u03C0rh + 2\u03C0r\u00B2", COLOR_RESULT),
            ("4.", "简化", "S = 2\u03C0r(h + r)", COLOR_FORMULA),
        ]

        cards = VGroup()
        for num, key, desc, color in points_data:
            num_mob = Text(num, font=FONT, font_size=22, color=color)
            key_mob = Text(key, font=FONT, font_size=24, color=color, weight=BOLD)
            desc_mob = Text(desc, font=FONT, font_size=18, color=GRAY_A)
            row = VGroup(num_mob, key_mob, desc_mob).arrange(RIGHT, buff=0.2)
            cards.add(row)

        cards.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        cards.move_to(DOWN * 1.0)

        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards],
                        lag_ratio=0.4),
            run_time=2.5
        )

        # 应用提示
        tip = Text(
            "生活中: 罐头盒、水桶、烟囱...",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.6)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl), FadeOut(cards), FadeOut(tip),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------
    def scene_8_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            FadeOut(self.author),
            FadeIn(author_big, shift=DOWN * 0.3),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰小圆柱
        deco_cyls = VGroup()
        angles = [0, PI / 3, 2 * PI / 3, PI, 4 * PI / 3, 5 * PI / 3]
        for a in angles:
            mini_cyl = create_cylinder_2d(
                center=[0, 0, 0], width=0.5, height=0.7,
                ellipse_ratio=0.3, stroke_color=COLOR_CYLINDER,
                fill_top=COLOR_TOP, stroke_width=1.5
            )
            mini_cyl.move_to(
                follow.get_center() + 2.5 * np.array([np.cos(a), np.sin(a), 0])
            )
            deco_cyls.add(mini_cyl)

        self.play(
            LaggedStart(*[FadeIn(dc, scale=0.5) for dc in deco_cyls],
                        lag_ratio=0.1),
            run_time=0.8
        )
        self.wait(2.0)

        # 淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_cyls),
            run_time=0.8
        )


# 运行命令:
# manim -pql 002_圆柱的表面积.py CylinderSurfaceAreaLesson   # 快速预览
# manim -qm 002_圆柱的表面积.py CylinderSurfaceAreaLesson    # 中等质量
# manim -qh 002_圆柱的表面积.py CylinderSurfaceAreaLesson    # 高质量

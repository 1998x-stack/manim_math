"""
005_圆锥的体积.py -- 圆锥的体积 教学动画

知识点: 圆锥体积公式推导(等底等高实验)、V=(1/3)Sh=(1/3)pi*r^2*h
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 回顾圆柱体积
  3. 等底等高实验引入
  4. 倒水实验动画: 圆锥倒水3次装满圆柱
  5. 推导公式: V = (1/3)Sh = (1/3)pi*r^2*h
  6. 例题: 已知底面半径和高, 求圆锥体积
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
COLOR_CONE = "#f97316"            # 橙色 圆锥
COLOR_CYLINDER = "#3b82f6"        # 蓝色 圆柱
COLOR_RESULT = "#22c55e"          # 绿色 结果
COLOR_HL = "#fbbf24"              # 黄色高亮
COLOR_ACCENT = "#a78bfa"          # 紫色强调
COLOR_SUB = "#ef4444"             # 红色
COLOR_AUTHOR = "#6b7280"          # 灰色作者信息
COLOR_RADIUS = "#f472b6"          # 粉色 半径
COLOR_HEIGHT = "#38bdf8"          # 天蓝色 高
COLOR_AREA = "#34d399"            # 绿色 面积
COLOR_WATER = "#60a5fa"           # 水蓝色
FONT = "Heiti SC"


# ======================================================================
# 辅助函数
# ======================================================================

def cn(text, **kwargs):
    """创建中文文本的便捷函数"""
    defaults = {"font": FONT}
    defaults.update(kwargs)
    return Text(text, **defaults)


def create_cone_side_view(radius, height, center, color=COLOR_CONE,
                          fill_opacity=0.3, stroke_width=2.5):
    """
    创建圆锥的2D侧视图(等腰三角形 + 底面椭圆)
    """
    cx, cy = center[0], center[1]
    ellipse_ratio = 0.35

    # 底面椭圆
    bottom_ellipse = Ellipse(
        width=radius * 2, height=radius * 2 * ellipse_ratio,
        color=color, stroke_width=stroke_width, fill_opacity=fill_opacity * 0.5
    ).move_to([cx, cy - height / 2, 0])

    # 三角形侧面(从顶点到底面两端)
    apex = np.array([cx, cy + height / 2, 0])
    left_base = np.array([cx - radius, cy - height / 2, 0])
    right_base = np.array([cx + radius, cy - height / 2, 0])

    left_line = Line(apex, left_base, color=color, stroke_width=stroke_width)
    right_line = Line(apex, right_base, color=color, stroke_width=stroke_width)

    # 侧面填充
    side_fill = Polygon(
        apex, left_base, right_base,
        color=color, fill_opacity=fill_opacity * 0.4,
        stroke_width=0
    )

    return VGroup(bottom_ellipse, side_fill, left_line, right_line)


def create_cylinder_side_view(radius, height, center, color=COLOR_CYLINDER,
                               fill_opacity=0.3, stroke_width=2.5):
    """
    创建圆柱的2D侧视图
    """
    cx, cy = center[0], center[1]
    ellipse_ratio = 0.35

    bottom_ellipse = Ellipse(
        width=radius * 2, height=radius * 2 * ellipse_ratio,
        color=color, stroke_width=stroke_width, fill_opacity=fill_opacity * 0.5
    ).move_to([cx, cy - height / 2, 0])

    top_ellipse = Ellipse(
        width=radius * 2, height=radius * 2 * ellipse_ratio,
        color=color, stroke_width=stroke_width, fill_opacity=fill_opacity
    ).move_to([cx, cy + height / 2, 0])

    left_line = Line(
        [cx - radius, cy - height / 2, 0],
        [cx - radius, cy + height / 2, 0],
        color=color, stroke_width=stroke_width
    )
    right_line = Line(
        [cx + radius, cy - height / 2, 0],
        [cx + radius, cy + height / 2, 0],
        color=color, stroke_width=stroke_width
    )

    side_rect = Polygon(
        [cx - radius, cy - height / 2, 0],
        [cx + radius, cy - height / 2, 0],
        [cx + radius, cy + height / 2, 0],
        [cx - radius, cy + height / 2, 0],
        color=color, fill_opacity=fill_opacity * 0.4,
        stroke_width=0
    )

    return VGroup(bottom_ellipse, side_rect, left_line, right_line, top_ellipse)


def create_water_in_cone(radius, height, center, fill_level, color=COLOR_WATER):
    """
    创建圆锥中的水位(fill_level: 0~1)
    水在圆锥中, 越往上越窄
    """
    if fill_level <= 0:
        return VGroup()

    cx, cy = center[0], center[1]
    ellipse_ratio = 0.35
    bottom_y = cy - height / 2

    # 水位高度
    water_h = height * fill_level
    water_top_y = bottom_y + water_h

    # 圆锥在水位处的半径(线性缩小)
    water_radius = radius * (1 - fill_level)

    # 水面椭圆
    water_ellipse = Ellipse(
        width=water_radius * 2, height=water_radius * 2 * ellipse_ratio,
        color=color, fill_opacity=0.4, stroke_width=1
    ).move_to([cx, water_top_y, 0])

    # 水体(梯形填充)
    left_base = np.array([cx - radius, bottom_y, 0])
    right_base = np.array([cx + radius, bottom_y, 0])
    left_top = np.array([cx - water_radius, water_top_y, 0])
    right_top = np.array([cx + water_radius, water_top_y, 0])

    water_body = Polygon(
        left_base, right_base, right_top, left_top,
        color=color, fill_opacity=0.35, stroke_width=0
    )

    return VGroup(water_body, water_ellipse)


def create_water_in_cylinder(radius, height, center, fill_level, color=COLOR_WATER):
    """
    创建圆柱中的水位(fill_level: 0~1)
    """
    if fill_level <= 0:
        return VGroup()

    cx, cy = center[0], center[1]
    ellipse_ratio = 0.35
    bottom_y = cy - height / 2

    water_h = height * fill_level
    water_top_y = bottom_y + water_h

    # 水面椭圆
    water_ellipse = Ellipse(
        width=radius * 2, height=radius * 2 * ellipse_ratio,
        color=color, fill_opacity=0.4, stroke_width=1
    ).move_to([cx, water_top_y, 0])

    # 水体(矩形填充)
    water_body = Polygon(
        [cx - radius, bottom_y, 0],
        [cx + radius, bottom_y, 0],
        [cx + radius, water_top_y, 0],
        [cx - radius, water_top_y, 0],
        color=color, fill_opacity=0.35, stroke_width=0
    )

    return VGroup(water_body, water_ellipse)


# ======================================================================
# 主场景
# ======================================================================

class ConeVolumeLesson(Scene):
    """
    圆锥的体积教学动画

    场景顺序:
      1. 开场钩子
      2. 回顾圆柱体积
      3. 等底等高实验引入
      4. 倒水实验动画
      5. 公式推导
      6. 例题演练
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_review_cylinder()
        self.scene_3_equal_base_height()
        self.scene_4_pouring_experiment()
        self.scene_5_formula_derivation()
        self.scene_6_example()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息
        self.author_mob = cn(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook = cn("圆锥的体积", font_size=44, color=COLOR_HL).move_to(UP * 5.5)
        hook2 = cn("和圆柱有什么关系?", font_size=34, color=WHITE).move_to(UP * 4.7)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # 画一个圆锥
        cone = create_cone_side_view(
            radius=1.2, height=2.5,
            center=np.array([-1.8, 1.8, 0]),
            color=COLOR_CONE, fill_opacity=0.4
        )

        # 画一个圆柱
        cyl = create_cylinder_side_view(
            radius=1.2, height=2.5,
            center=np.array([1.8, 1.8, 0]),
            color=COLOR_CYLINDER, fill_opacity=0.4
        )

        self.play(Create(cone), Create(cyl), run_time=1.2)
        self.wait(0.3)

        # 问号和等式
        q_mark = MathTex(r"?", font_size=72, color=COLOR_HL).move_to([0, 1.8, 0])
        self.play(FadeIn(q_mark, scale=0.5), run_time=0.5)
        self.wait(0.8)

        # 提示
        hint = cn("用实验来发现!", font_size=26, color=GRAY_A).move_to(DOWN * 1.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(hook2), FadeOut(cone),
            FadeOut(cyl), FadeOut(q_mark), FadeOut(hint),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 回顾圆柱体积
    # ------------------------------------------------------------------

    def scene_2_review_cylinder(self):
        title = cn("回顾", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        subtitle = cn("圆柱的体积", font_size=28, color=WHITE).move_to(UP * 4.8)
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 画圆柱
        cyl = create_cylinder_side_view(
            radius=1.0, height=2.2,
            center=np.array([0, 2.2, 0]),
            color=COLOR_CYLINDER, fill_opacity=0.35
        )

        # 标注
        r_line = Line(
            [0, 2.2 + 1.1, 0], [1.0, 2.2 + 1.1, 0],
            color=COLOR_RADIUS, stroke_width=2
        )
        r_label = MathTex(r"r", font_size=24, color=COLOR_RADIUS).next_to(r_line, UP, buff=0.08)
        h_brace = Brace(
            Line([1.0 + 0.3, 2.2 - 1.1, 0], [1.0 + 0.3, 2.2 + 1.1, 0]),
            RIGHT, buff=0.1, color=COLOR_HEIGHT
        )
        h_label = MathTex(r"h", font_size=24, color=COLOR_HEIGHT).next_to(h_brace, RIGHT, buff=0.08)

        self.play(Create(cyl), run_time=0.8)
        self.play(
            Create(r_line), FadeIn(r_label),
            Create(h_brace), FadeIn(h_label),
            run_time=0.6
        )

        # 圆柱体积公式
        formula_label = cn("圆柱体积:", font_size=24, color=COLOR_CYLINDER)
        formula_eq = MathTex(
            r"V", r"=", r"S", r"h", r"=", r"\pi", r"r^2", r"h",
            font_size=32
        )
        formula_eq[2].set_color(COLOR_AREA)
        formula_eq[3].set_color(COLOR_HEIGHT)
        formula_eq[5].set_color(COLOR_RADIUS)
        formula_eq[6].set_color(COLOR_RADIUS)
        formula_eq[7].set_color(COLOR_HEIGHT)

        formula_group = VGroup(formula_label, formula_eq).arrange(RIGHT, buff=0.2)
        formula_group.move_to(DOWN * 0.5)

        box = SurroundingRectangle(formula_group, color=COLOR_CYLINDER, buff=0.2, corner_radius=0.08)

        self.play(FadeIn(formula_group, shift=UP * 0.15), run_time=0.6)
        self.play(Create(box), run_time=0.4)
        self.wait(0.5)

        # 引出问题
        question = cn("那圆锥的体积呢?", font_size=26, color=COLOR_HL).move_to(DOWN * 2.5)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(cyl),
            FadeOut(r_line), FadeOut(r_label),
            FadeOut(h_brace), FadeOut(h_label),
            FadeOut(formula_group), FadeOut(box), FadeOut(question),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 等底等高实验引入
    # ------------------------------------------------------------------

    def scene_3_equal_base_height(self):
        title = cn("等底等高实验", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        explain = cn("取一个圆锥和一个圆柱", font_size=24, color=WHITE).move_to(UP * 4.6)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)

        # 圆锥和圆柱参数
        r = 1.2
        h = 2.4
        cone_center = np.array([-2.0, 2.0, 0])
        cyl_center = np.array([2.0, 2.0, 0])

        # 画圆锥
        cone = create_cone_side_view(
            radius=r, height=h, center=cone_center,
            color=COLOR_CONE, fill_opacity=0.4
        )
        cone_label = cn("圆锥", font_size=22, color=COLOR_CONE).move_to(
            cone_center + DOWN * (h / 2 + 0.5)
        )

        # 画圆柱
        cyl = create_cylinder_side_view(
            radius=r, height=h, center=cyl_center,
            color=COLOR_CYLINDER, fill_opacity=0.4
        )
        cyl_label = cn("圆柱", font_size=22, color=COLOR_CYLINDER).move_to(
            cyl_center + DOWN * (h / 2 + 0.5)
        )

        self.play(Create(cone), FadeIn(cone_label), run_time=0.8)
        self.play(Create(cyl), FadeIn(cyl_label), run_time=0.8)

        # 标注等底
        r_line_cone = Line(
            [cone_center[0], cone_center[1] - h / 2, 0],
            [cone_center[0] + r, cone_center[1] - h / 2, 0],
            color=COLOR_RADIUS, stroke_width=2.5
        )
        r_text_cone = MathTex(r"r", font_size=20, color=COLOR_RADIUS).next_to(r_line_cone, DOWN, buff=0.08)

        r_line_cyl = Line(
            [cyl_center[0], cyl_center[1] - h / 2, 0],
            [cyl_center[0] + r, cyl_center[1] - h / 2, 0],
            color=COLOR_RADIUS, stroke_width=2.5
        )
        r_text_cyl = MathTex(r"r", font_size=20, color=COLOR_RADIUS).next_to(r_line_cyl, DOWN, buff=0.08)

        self.play(
            Create(r_line_cone), FadeIn(r_text_cone),
            Create(r_line_cyl), FadeIn(r_text_cyl),
            run_time=0.5
        )

        # 标注等高
        h_brace_cone = Brace(
            Line(
                [cone_center[0] - r - 0.2, cone_center[1] - h / 2, 0],
                [cone_center[0] - r - 0.2, cone_center[1] + h / 2, 0]
            ),
            LEFT, buff=0.1, color=COLOR_HEIGHT
        )
        h_text_cone = MathTex(r"h", font_size=20, color=COLOR_HEIGHT).next_to(h_brace_cone, LEFT, buff=0.08)

        h_brace_cyl = Brace(
            Line(
                [cyl_center[0] + r + 0.2, cyl_center[1] - h / 2, 0],
                [cyl_center[0] + r + 0.2, cyl_center[1] + h / 2, 0]
            ),
            RIGHT, buff=0.1, color=COLOR_HEIGHT
        )
        h_text_cyl = MathTex(r"h", font_size=20, color=COLOR_HEIGHT).next_to(h_brace_cyl, RIGHT, buff=0.08)

        self.play(
            Create(h_brace_cone), FadeIn(h_text_cone),
            Create(h_brace_cyl), FadeIn(h_text_cyl),
            run_time=0.5
        )

        # 等底等高标注
        equal_base = cn("底面积相同", font_size=22, color=COLOR_HL).move_to(DOWN * 1.5)
        equal_height = cn("高也相同", font_size=22, color=COLOR_HL).move_to(DOWN * 2.2)

        self.play(FadeIn(equal_base), run_time=0.4)
        self.play(FadeIn(equal_height), run_time=0.4)

        key_q = cn("它们的体积有什么关系?", font_size=26, color=COLOR_HL).move_to(DOWN * 3.5)
        self.play(FadeIn(key_q, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(cone), FadeOut(cone_label),
            FadeOut(cyl), FadeOut(cyl_label),
            FadeOut(r_line_cone), FadeOut(r_text_cone),
            FadeOut(r_line_cyl), FadeOut(r_text_cyl),
            FadeOut(h_brace_cone), FadeOut(h_text_cone),
            FadeOut(h_brace_cyl), FadeOut(h_text_cyl),
            FadeOut(equal_base), FadeOut(equal_height),
            FadeOut(key_q),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 倒水实验动画 (核心)
    # ------------------------------------------------------------------

    def scene_4_pouring_experiment(self):
        title = cn("倒水实验", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        explain = cn("用圆锥装满水, 倒入等底等高的圆柱",
                      font_size=22, color=GRAY_A).move_to(UP * 4.7)
        self.play(FadeIn(explain), run_time=0.4)

        # 参数
        r = 1.0
        h = 2.2
        cone_center = np.array([-2.2, 2.0, 0])
        cyl_center = np.array([2.2, 2.0, 0])

        # 圆锥(带水)
        cone = create_cone_side_view(
            radius=r, height=h, center=cone_center,
            color=COLOR_CONE, fill_opacity=0.4
        )
        cone_label = cn("圆锥", font_size=20, color=COLOR_CONE).move_to(
            cone_center + DOWN * (h / 2 + 0.4)
        )

        # 圆柱(空)
        cyl = create_cylinder_side_view(
            radius=r, height=h, center=cyl_center,
            color=COLOR_CYLINDER, fill_opacity=0.4
        )
        cyl_label = cn("圆柱", font_size=20, color=COLOR_CYLINDER).move_to(
            cyl_center + DOWN * (h / 2 + 0.4)
        )

        self.play(Create(cone), FadeIn(cone_label), run_time=0.6)
        self.play(Create(cyl), FadeIn(cyl_label), run_time=0.6)

        # ---- 第1次倒水 ----
        pour_label = cn("第 1 次", font_size=28, color=COLOR_HL).move_to(DOWN * 1.5)
        self.play(FadeIn(pour_label), run_time=0.3)

        # 圆锥装满水
        cone_water = create_water_in_cone(r, h, cone_center, fill_level=1.0)
        self.play(FadeIn(cone_water), run_time=0.5)
        self.wait(0.3)

        # 倒水箭头
        pour_arrow = Arrow(
            cone_center + RIGHT * 1.0,
            cyl_center + LEFT * 1.0,
            color=COLOR_WATER, stroke_width=3, buff=0.2
        )
        self.play(GrowArrow(pour_arrow), run_time=0.4)

        # 水从圆锥消失, 进入圆柱(1/3)
        cyl_water_1 = create_water_in_cylinder(r, h, cyl_center, fill_level=1/3)
        self.play(
            FadeOut(cone_water),
            FadeIn(cyl_water_1),
            run_time=0.8
        )
        self.play(FadeOut(pour_arrow), run_time=0.2)

        frac_label_1 = MathTex(
            r"\frac{1}{3}", font_size=28, color=COLOR_WATER
        ).move_to(cyl_center)
        self.play(FadeIn(frac_label_1), run_time=0.3)
        self.wait(0.5)

        # ---- 第2次倒水 ----
        pour_label_2 = cn("第 2 次", font_size=28, color=COLOR_HL).move_to(DOWN * 1.5)
        self.play(
            ReplacementTransform(pour_label, pour_label_2),
            FadeOut(frac_label_1),
            run_time=0.3
        )

        cone_water_2 = create_water_in_cone(r, h, cone_center, fill_level=1.0)
        self.play(FadeIn(cone_water_2), run_time=0.4)

        pour_arrow_2 = Arrow(
            cone_center + RIGHT * 1.0,
            cyl_center + LEFT * 1.0,
            color=COLOR_WATER, stroke_width=3, buff=0.2
        )
        self.play(GrowArrow(pour_arrow_2), run_time=0.4)

        cyl_water_2 = create_water_in_cylinder(r, h, cyl_center, fill_level=2/3)
        self.play(
            FadeOut(cone_water_2), FadeOut(cyl_water_1),
            FadeIn(cyl_water_2),
            run_time=0.8
        )
        self.play(FadeOut(pour_arrow_2), run_time=0.2)

        frac_label_2 = MathTex(
            r"\frac{2}{3}", font_size=28, color=COLOR_WATER
        ).move_to(cyl_center)
        self.play(FadeIn(frac_label_2), run_time=0.3)
        self.wait(0.5)

        # ---- 第3次倒水 ----
        pour_label_3 = cn("第 3 次", font_size=28, color=COLOR_HL).move_to(DOWN * 1.5)
        self.play(
            ReplacementTransform(pour_label_2, pour_label_3),
            FadeOut(frac_label_2),
            run_time=0.3
        )

        cone_water_3 = create_water_in_cone(r, h, cone_center, fill_level=1.0)
        self.play(FadeIn(cone_water_3), run_time=0.4)

        pour_arrow_3 = Arrow(
            cone_center + RIGHT * 1.0,
            cyl_center + LEFT * 1.0,
            color=COLOR_WATER, stroke_width=3, buff=0.2
        )
        self.play(GrowArrow(pour_arrow_3), run_time=0.4)

        cyl_water_3 = create_water_in_cylinder(r, h, cyl_center, fill_level=1.0)
        self.play(
            FadeOut(cone_water_3), FadeOut(cyl_water_2),
            FadeIn(cyl_water_3),
            run_time=0.8
        )
        self.play(FadeOut(pour_arrow_3), run_time=0.2)

        # 满了!
        full_label = cn("刚好装满!", font_size=28, color=COLOR_RESULT).move_to(cyl_center + UP * 0.2)
        self.play(FadeIn(full_label, scale=1.2), run_time=0.5)
        self.wait(0.5)

        # 结论
        conclusion = cn("倒了 3 次, 刚好装满圆柱!",
                         font_size=24, color=COLOR_HL).move_to(DOWN * 2.5)
        self.play(
            FadeOut(pour_label_3), FadeOut(full_label),
            FadeIn(conclusion, shift=UP * 0.2),
            run_time=0.5
        )

        # 关系式
        relation = VGroup(
            cn("圆锥体积", font_size=24, color=COLOR_CONE),
            MathTex(r"=", font_size=28, color=WHITE),
            MathTex(r"\frac{1}{3}", font_size=28, color=COLOR_HL),
            MathTex(r"\times", font_size=24, color=WHITE),
            cn("圆柱体积", font_size=24, color=COLOR_CYLINDER),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 3.5)

        self.play(FadeIn(relation, shift=UP * 0.15), run_time=0.6)

        key_note = cn("(前提: 等底等高)", font_size=20, color=COLOR_SUB).move_to(DOWN * 4.3)
        self.play(FadeIn(key_note), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(cone), FadeOut(cone_label),
            FadeOut(cyl), FadeOut(cyl_label),
            FadeOut(cyl_water_3),
            FadeOut(conclusion), FadeOut(relation), FadeOut(key_note),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式推导
    # ------------------------------------------------------------------

    def scene_5_formula_derivation(self):
        title = cn("公式推导", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 从实验结论出发
        step_y = 4.0

        step1_label = cn("实验结论:", font_size=24, color=GRAY_A)
        step1 = VGroup(
            cn("圆锥体积", font_size=24, color=COLOR_CONE),
            MathTex(r"=", font_size=28, color=WHITE),
            MathTex(r"\frac{1}{3}", font_size=28, color=COLOR_HL),
            MathTex(r"\times", font_size=24, color=WHITE),
            cn("等底等高圆柱体积", font_size=24, color=COLOR_CYLINDER),
        ).arrange(RIGHT, buff=0.1)
        step1_group = VGroup(step1_label, step1).arrange(DOWN, buff=0.2)
        step1_group.move_to([0, step_y, 0])

        self.play(FadeIn(step1_group, shift=UP * 0.15), run_time=0.6)
        self.wait(0.5)

        # 圆锥示意图
        cone_r = 0.8
        cone_h = 1.8
        cone_center = np.array([-2.5, 1.5, 0])
        cone = create_cone_side_view(
            radius=cone_r, height=cone_h, center=cone_center,
            color=COLOR_CONE, fill_opacity=0.35
        )

        # 标注
        r_line = Line(
            [cone_center[0], cone_center[1] - cone_h / 2, 0],
            [cone_center[0] + cone_r, cone_center[1] - cone_h / 2, 0],
            color=COLOR_RADIUS, stroke_width=2
        )
        r_label = MathTex(r"r", font_size=20, color=COLOR_RADIUS).next_to(r_line, DOWN, buff=0.06)

        # 高线(虚线 从顶点到底面中心)
        h_line = DashedLine(
            [cone_center[0], cone_center[1] + cone_h / 2, 0],
            [cone_center[0], cone_center[1] - cone_h / 2, 0],
            color=COLOR_HEIGHT, stroke_width=2, dash_length=0.1
        )
        h_label = MathTex(r"h", font_size=20, color=COLOR_HEIGHT).next_to(h_line, RIGHT, buff=0.08)

        self.play(Create(cone), run_time=0.6)
        self.play(
            Create(r_line), FadeIn(r_label),
            Create(h_line), FadeIn(h_label),
            run_time=0.5
        )

        # 推导过程
        derive_y = -0.5

        d1_label = cn("圆柱体积:", font_size=22, color=COLOR_CYLINDER)
        d1_eq = MathTex(
            r"V_{\text{cyl}}", r"=", r"\pi", r"r^2", r"h",
            font_size=30
        )
        d1_eq[2].set_color(COLOR_RADIUS)
        d1_eq[3].set_color(COLOR_RADIUS)
        d1_eq[4].set_color(COLOR_HEIGHT)
        d1 = VGroup(d1_label, d1_eq).arrange(RIGHT, buff=0.15).move_to([0, derive_y, 0])

        self.play(FadeIn(d1, shift=UP * 0.15), run_time=0.5)

        # 圆锥 = 1/3 圆柱
        d2_label = cn("圆锥体积:", font_size=22, color=COLOR_CONE)
        d2_eq = MathTex(
            r"V", r"=", r"\frac{1}{3}",
            r"\pi", r"r^2", r"h",
            font_size=30
        )
        d2_eq[2].set_color(COLOR_HL)
        d2_eq[3].set_color(COLOR_RADIUS)
        d2_eq[4].set_color(COLOR_RADIUS)
        d2_eq[5].set_color(COLOR_HEIGHT)
        d2 = VGroup(d2_label, d2_eq).arrange(RIGHT, buff=0.15).move_to([0, derive_y - 1.0, 0])

        self.play(FadeIn(d2, shift=UP * 0.15), run_time=0.5)
        self.wait(0.5)

        # 用底面积表示
        d3_label = cn("也可以写成:", font_size=22, color=GRAY_A)
        d3_eq = MathTex(
            r"V", r"=", r"\frac{1}{3}",
            r"S", r"h",
            font_size=32
        )
        d3_eq[2].set_color(COLOR_HL)
        d3_eq[3].set_color(COLOR_AREA)
        d3_eq[4].set_color(COLOR_HEIGHT)
        d3 = VGroup(d3_label, d3_eq).arrange(RIGHT, buff=0.15).move_to([0, derive_y - 2.0, 0])

        s_note = VGroup(
            MathTex(r"S", font_size=22, color=COLOR_AREA),
            cn(" = ", font_size=20, color=WHITE),
            cn("底面积", font_size=20, color=COLOR_AREA),
            cn(" = ", font_size=20, color=WHITE),
            MathTex(r"\pi r^2", font_size=22, color=COLOR_RADIUS),
        ).arrange(RIGHT, buff=0.05).move_to([0, derive_y - 2.8, 0])

        self.play(FadeIn(d3, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(s_note), run_time=0.4)

        # 最终公式框
        final_y = derive_y - 4.2

        formula_final = MathTex(
            r"V", r"=", r"\frac{1}{3}", r"S", r"h",
            r"=", r"\frac{1}{3}", r"\pi", r"r^2", r"h",
            font_size=36
        )
        formula_final[2].set_color(COLOR_HL)
        formula_final[3].set_color(COLOR_AREA)
        formula_final[4].set_color(COLOR_HEIGHT)
        formula_final[6].set_color(COLOR_HL)
        formula_final[7].set_color(COLOR_RADIUS)
        formula_final[8].set_color(COLOR_RADIUS)
        formula_final[9].set_color(COLOR_HEIGHT)
        formula_final.move_to([0, final_y, 0])

        box = SurroundingRectangle(
            formula_final, color=COLOR_HL, buff=0.25, corner_radius=0.1
        )

        self.play(Write(formula_final), run_time=0.8)
        self.play(Create(box), run_time=0.4)

        # 强调1/3
        one_third_note = cn(
            "关键: 乘以三分之一!",
            font_size=24, color=COLOR_SUB
        ).move_to([0, final_y - 0.9, 0])
        self.play(FadeIn(one_third_note), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(step1_group),
            FadeOut(cone), FadeOut(r_line), FadeOut(r_label),
            FadeOut(h_line), FadeOut(h_label),
            FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(s_note),
            FadeOut(formula_final), FadeOut(box), FadeOut(one_third_note),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题
    # ------------------------------------------------------------------

    def scene_6_example(self):
        title = cn("例题", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 题目
        q1 = cn("一个圆锥形沙堆,", font_size=24, color=WHITE).move_to(UP * 4.5)
        q2 = cn("底面半径 3 m, 高 4 m", font_size=24, color=WHITE).move_to(UP * 3.9)
        q3 = cn("求这个沙堆的体积。", font_size=24, color=COLOR_HL).move_to(UP * 3.3)

        self.play(FadeIn(q1), run_time=0.4)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(q3), run_time=0.4)

        # 圆锥示意图
        cone = create_cone_side_view(
            radius=0.9, height=1.8,
            center=np.array([0, 1.5, 0]),
            color=COLOR_CONE, fill_opacity=0.35
        )
        r_line = Line(
            [0, 1.5 - 0.9, 0], [0.9, 1.5 - 0.9, 0],
            color=COLOR_RADIUS, stroke_width=2
        )
        r_label = cn("r=3", font_size=18, color=COLOR_RADIUS).next_to(r_line, DOWN, buff=0.05)

        h_line = DashedLine(
            [0, 1.5 + 0.9, 0], [0, 1.5 - 0.9, 0],
            color=COLOR_HEIGHT, stroke_width=2, dash_length=0.1
        )
        h_label = cn("h=4", font_size=18, color=COLOR_HEIGHT).next_to(h_line, LEFT, buff=0.08)

        self.play(Create(cone), run_time=0.6)
        self.play(
            Create(r_line), FadeIn(r_label),
            Create(h_line), FadeIn(h_label),
            run_time=0.5
        )
        self.wait(0.5)

        # 解题步骤
        sol_y = -0.8

        sol_title = cn("解:", font_size=26, color=COLOR_RESULT).move_to([-3.5, sol_y, 0])
        self.play(FadeIn(sol_title), run_time=0.3)

        # Step 1: 写出公式
        s1 = MathTex(
            r"V", r"=", r"\frac{1}{3}", r"\pi", r"r^2", r"h",
            font_size=30
        ).move_to([0, sol_y - 0.7, 0])
        s1[2].set_color(COLOR_HL)
        s1[3].set_color(COLOR_RADIUS)
        s1[4].set_color(COLOR_RADIUS)
        s1[5].set_color(COLOR_HEIGHT)

        self.play(Write(s1), run_time=0.6)
        self.wait(0.3)

        # Step 2: 代入数值
        s2 = MathTex(
            r"=", r"\frac{1}{3}",
            r"\times", r"\pi", r"\times", r"3^2", r"\times", r"4",
            font_size=30
        ).move_to([0, sol_y - 1.5, 0])
        s2[1].set_color(COLOR_HL)
        s2[3].set_color(COLOR_RADIUS)
        s2[5].set_color(COLOR_RADIUS)
        s2[7].set_color(COLOR_HEIGHT)

        self.play(Write(s2), run_time=0.6)
        self.wait(0.3)

        # Step 3: 计算
        s3 = MathTex(
            r"=", r"\frac{1}{3}",
            r"\times", r"9\pi", r"\times", r"4",
            font_size=30
        ).move_to([0, sol_y - 2.3, 0])
        s3[1].set_color(COLOR_HL)

        self.play(Write(s3), run_time=0.5)

        # Step 4: 继续计算
        s4 = MathTex(
            r"=", r"\frac{1}{3}", r"\times", r"36\pi",
            font_size=30
        ).move_to([0, sol_y - 3.1, 0])
        s4[1].set_color(COLOR_HL)

        self.play(Write(s4), run_time=0.5)

        # Step 5: 结果
        s5 = MathTex(
            r"=", r"12\pi",
            font_size=32
        ).move_to([0, sol_y - 3.9, 0])
        s5[1].set_color(COLOR_RESULT)

        self.play(Write(s5), run_time=0.5)

        # 近似值
        approx = MathTex(
            r"\approx", r"37.68", font_size=30
        ).next_to(s5, RIGHT, buff=0.3)
        unit = cn(" m", font_size=22, color=WHITE)
        sup = MathTex(r"^3", font_size=22, color=WHITE)
        unit_group = VGroup(unit, sup).arrange(RIGHT, buff=0.02).next_to(approx, RIGHT, buff=0.1)

        self.play(Write(approx), FadeIn(unit_group), run_time=0.5)

        # 结果框
        result_text = VGroup(
            MathTex(r"V = 12\pi \approx 37.68", font_size=28, color=COLOR_RESULT),
            cn(" m", font_size=20, color=COLOR_RESULT),
            MathTex(r"^3", font_size=20, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.05).move_to([0, sol_y - 5.2, 0])

        result_box = SurroundingRectangle(result_text, color=COLOR_RESULT, buff=0.2, corner_radius=0.08)
        self.play(Create(result_box), FadeIn(result_text), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q2), FadeOut(q3),
            FadeOut(cone), FadeOut(r_line), FadeOut(r_label),
            FadeOut(h_line), FadeOut(h_label),
            FadeOut(sol_title), FadeOut(s1), FadeOut(s2), FadeOut(s3),
            FadeOut(s4), FadeOut(s5),
            FadeOut(approx), FadeOut(unit_group),
            FadeOut(result_text), FadeOut(result_box),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = cn("总结", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 要点1
        p1_title = cn("核心关系", font_size=26, color=COLOR_ACCENT).move_to(UP * 4.3)
        p1_body = VGroup(
            cn("圆锥体积", font_size=22, color=COLOR_CONE),
            cn(" = ", font_size=22, color=WHITE),
            MathTex(r"\frac{1}{3}", font_size=26, color=COLOR_HL),
            MathTex(r"\times", font_size=22, color=WHITE),
            cn("等底等高圆柱体积", font_size=22, color=COLOR_CYLINDER),
        ).arrange(RIGHT, buff=0.08).move_to(UP * 3.5)

        self.play(FadeIn(p1_title), run_time=0.3)
        self.play(FadeIn(p1_body, shift=UP * 0.15), run_time=0.4)

        # 要点2
        p2_title = cn("前提条件", font_size=26, color=COLOR_ACCENT).move_to(UP * 2.5)
        p2_body = cn("必须是等底等高!", font_size=24, color=COLOR_SUB).move_to(UP * 1.8)
        self.play(FadeIn(p2_title), run_time=0.3)
        self.play(FadeIn(p2_body, shift=UP * 0.15), run_time=0.4)

        # 公式
        formula_title = cn("体积公式", font_size=26, color=COLOR_ACCENT).move_to(UP * 0.8)
        self.play(FadeIn(formula_title), run_time=0.3)

        formula = MathTex(
            r"V", r"=", r"\frac{1}{3}",
            r"S", r"h", r"=", r"\frac{1}{3}",
            r"\pi", r"r^2", r"h",
            font_size=38
        ).move_to(DOWN * 0.2)
        formula[2].set_color(COLOR_HL)
        formula[3].set_color(COLOR_AREA)
        formula[4].set_color(COLOR_HEIGHT)
        formula[6].set_color(COLOR_HL)
        formula[7].set_color(COLOR_RADIUS)
        formula[8].set_color(COLOR_RADIUS)
        formula[9].set_color(COLOR_HEIGHT)

        box = SurroundingRectangle(formula, color=COLOR_HL, buff=0.3, corner_radius=0.12)

        self.play(Write(formula), run_time=0.8)
        self.play(Create(box), run_time=0.4)

        # 图例
        legend = VGroup(
            VGroup(
                MathTex(r"S", font_size=22, color=COLOR_AREA),
                cn(" = 底面积", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                MathTex(r"r", font_size=22, color=COLOR_RADIUS),
                cn(" = 底面半径", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                MathTex(r"h", font_size=22, color=COLOR_HEIGHT),
                cn(" = 高", font_size=20, color=WHITE),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 1.8)

        self.play(FadeIn(legend, shift=UP * 0.15), run_time=0.6)

        # 应用提示
        app_text = cn(
            "应用: 沙堆、麦堆体积, 再算重量",
            font_size=20, color=GRAY_A
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(app_text), run_time=0.5)

        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(p1_title), FadeOut(p1_body),
            FadeOut(p2_title), FadeOut(p2_body),
            FadeOut(formula_title), FadeOut(formula), FadeOut(box),
            FadeOut(legend), FadeOut(app_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        # 作者信息
        author_name = cn("上海初高中数学直通车", font_size=40, color=WHITE).move_to(UP * 1.5)
        author_id = cn("@emptyandcalm", font_size=30, color=GRAY_B).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author_mob, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = cn(
            "关注我, 学更多数学技巧!",
            font_size=28, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 装饰小圆锥
        mini_cones = VGroup()
        for i in range(5):
            angle = i * TAU / 5
            pos = DOWN * 2.5 + np.array([np.cos(angle) * 2, np.sin(angle) * 0.8, 0])
            mini = create_cone_side_view(
                radius=0.2, height=0.45,
                center=pos,
                color=COLOR_CONE, fill_opacity=0.5
            )
            mini_cones.add(mini)

        self.play(*[FadeIn(mc, scale=0.5) for mc in mini_cones], run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(author_name), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(mini_cones),
            run_time=1.0
        )


# 运行命令:
# manim -pql 005_圆锥的体积.py ConeVolumeLesson  # 快速预览
# manim -qm 005_圆锥的体积.py ConeVolumeLesson   # 中等质量
# manim -qh 005_圆锥的体积.py ConeVolumeLesson    # 高质量

"""
004_圆锥的认识.py — 圆锥的认识 教学动画

知识点: 圆锥的特征、各部分名称(顶点/底面/侧面/高)、旋转体生成、与圆柱的区别
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 生活中的圆锥
  2. 圆锥的各部分名称: 顶点、底面、侧面、高
  3. 底面特征: 一个圆形底面
  4. 侧面特征: 一个曲面(展开为扇形)
  5. 高的特征: 只有一条(顶点到底面圆心)
  6. 旋转生成: 直角三角形绕一条直角边旋转
  7. 与圆柱的区别
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
COLOR_CONE = "#3b82f6"          # 蓝色 圆锥主体
COLOR_BASE = "#2563eb"          # 深蓝 底面
COLOR_SIDE = "#8b5cf6"          # 紫色 侧面
COLOR_APEX = "#ef4444"          # 红色 顶点
COLOR_HEIGHT = "#f59e0b"        # 橙色 高
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_RESULT = "#22c55e"        # 绿色 结果/正确
COLOR_ACCENT = "#ef4444"        # 红色强调
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
COLOR_CYL = "#06b6d4"           # 青色 圆柱对比用
FONT = "PingFang SC"


# ======================================================================
# 辅助: 绘制 2D 圆锥示意图
# ======================================================================

def create_cone_2d(
    center=ORIGIN, width=2.4, height=3.0,
    ellipse_ratio=0.3, stroke_color=WHITE,
    fill_base=None, fill_side=None, stroke_width=2.5,
    show_back_arc=True
):
    """
    用 2D 元素组合绘制圆锥示意图 (前视图)
    center 是底面椭圆的中心
    返回 VGroup 及 parts 字典
    """
    rx = width / 2
    ry = width / 2 * ellipse_ratio
    cx, cy = center[0], center[1]
    apex_y = cy + height

    parts = {}

    # --- 侧面三角形填充 ---
    if fill_side:
        side_tri = Polygon(
            [cx - rx, cy, 0],
            [cx + rx, cy, 0],
            [cx, apex_y, 0],
            fill_color=fill_side, fill_opacity=0.25,
            stroke_width=0
        )
        parts["side_fill"] = side_tri

    # --- 底部椭圆 (前半实线后半虚线) ---
    bot_front = Arc(
        radius=rx, start_angle=-PI, angle=PI,
        arc_center=[cx, cy, 0], color=stroke_color,
        stroke_width=stroke_width
    )
    bot_front.stretch(ry / rx, 1)
    bot_front.move_to([cx, cy, 0])

    if show_back_arc:
        bot_back = DashedVMobject(
            Arc(
                radius=rx, start_angle=0, angle=PI,
                arc_center=[cx, cy, 0], color=stroke_color,
                stroke_width=stroke_width * 0.6
            ).stretch(ry / rx, 1).move_to([cx, cy, 0]),
            num_dashes=12
        )
        parts["bot_back"] = bot_back

    parts["bot_front"] = bot_front

    if fill_base:
        bot_fill = Ellipse(
            width=width, height=width * ellipse_ratio * 2,
            fill_color=fill_base, fill_opacity=0.35,
            stroke_width=0
        ).move_to([cx, cy, 0])
        parts["bot_fill"] = bot_fill

    # --- 左右母线 (从底面椭圆边缘到顶点) ---
    left_line = Line(
        [cx - rx, cy, 0], [cx, apex_y, 0],
        color=stroke_color, stroke_width=stroke_width
    )
    right_line = Line(
        [cx + rx, cy, 0], [cx, apex_y, 0],
        color=stroke_color, stroke_width=stroke_width
    )
    parts["left_line"] = left_line
    parts["right_line"] = right_line

    # --- 顶点 ---
    apex_dot = Dot([cx, apex_y, 0], radius=0.06, color=stroke_color)
    parts["apex_dot"] = apex_dot

    # 组装 (按渲染顺序)
    group = VGroup()
    for key in ["side_fill", "bot_fill", "bot_back", "bot_front",
                "left_line", "right_line", "apex_dot"]:
        if key in parts:
            group.add(parts[key])

    group.parts = parts
    return group


def create_cylinder_2d_simple(
    center=ORIGIN, width=2.0, height=2.5,
    ellipse_ratio=0.25, stroke_color=WHITE,
    fill_top=None, fill_bottom=None, fill_side=None,
    stroke_width=2.0
):
    """简化版 2D 圆柱"""
    rx = width / 2
    ry = width / 2 * ellipse_ratio
    cx, cy = center[0], center[1]
    top_cy = cy + height / 2
    bot_cy = cy - height / 2

    parts = VGroup()

    if fill_side:
        side_rect = Rectangle(
            width=width, height=height,
            fill_color=fill_side, fill_opacity=0.25,
            stroke_width=0
        ).move_to([cx, cy, 0])
        parts.add(side_rect)

    # 底部椭圆前半
    bot_front = Arc(
        radius=rx, start_angle=-PI, angle=PI,
        arc_center=[cx, bot_cy, 0], color=stroke_color,
        stroke_width=stroke_width
    ).stretch(ry / rx, 1).move_to([cx, bot_cy, 0])
    parts.add(bot_front)

    # 底部椭圆后半(虚线)
    bot_back = DashedVMobject(
        Arc(
            radius=rx, start_angle=0, angle=PI,
            arc_center=[cx, bot_cy, 0], color=stroke_color,
            stroke_width=stroke_width * 0.6
        ).stretch(ry / rx, 1).move_to([cx, bot_cy, 0]),
        num_dashes=10
    )
    parts.add(bot_back)

    # 左右母线
    parts.add(Line([cx - rx, bot_cy, 0], [cx - rx, top_cy, 0],
                    color=stroke_color, stroke_width=stroke_width))
    parts.add(Line([cx + rx, bot_cy, 0], [cx + rx, top_cy, 0],
                    color=stroke_color, stroke_width=stroke_width))

    # 顶部椭圆
    top_ell = Ellipse(
        width=width, height=width * ellipse_ratio * 2,
        color=stroke_color, stroke_width=stroke_width
    ).move_to([cx, top_cy, 0])
    if fill_top:
        top_ell.set_fill(fill_top, opacity=0.4)
    parts.add(top_ell)

    return parts


# ======================================================================
# 主场景
# ======================================================================

class ConeRecognitionLesson(Scene):
    """
    圆锥的认识 教学动画场景

    场景顺序:
      1. 开场钩子
      2. 圆锥各部分名称
      3. 底面特征
      4. 侧面特征
      5. 高的特征
      6. 旋转生成
      7. 与圆柱的区别
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_parts_intro()
        self.scene_3_base()
        self.scene_4_lateral_surface()
        self.scene_5_height()
        self.scene_6_rotation()
        self.scene_7_compare_cylinder()
        self.scene_8_summary()
        self.scene_9_outro()

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
            "你认识圆锥吗?",
            font=FONT, font_size=42, color=COLOR_HL,
        ).move_to(UP * 5.0)
        self.play(Write(hook), run_time=1.0)

        # 生活实例: 冰淇淋甜筒、交通锥、漏斗
        examples = VGroup()
        labels_text = ["甜筒", "交通锥", "漏斗"]
        x_positions = [-2.5, 0, 2.5]
        cone_colors = ["#f97316", "#ef4444", "#6366f1"]
        for i, (lbl, xp, cc) in enumerate(zip(labels_text, x_positions, cone_colors)):
            cone = create_cone_2d(
                center=[xp, 0.0, 0], width=1.2, height=1.8,
                ellipse_ratio=0.28, stroke_color=cc,
                fill_side=cc, stroke_width=2, show_back_arc=False
            )
            label = Text(lbl, font=FONT, font_size=20, color=GRAY_A
                         ).next_to(cone, DOWN, buff=0.4)
            examples.add(VGroup(cone, label))

        self.play(
            LaggedStart(*[FadeIn(ex, shift=UP * 0.3) for ex in examples],
                        lag_ratio=0.3),
            run_time=1.5
        )
        self.wait(1.0)

        answer = Text(
            "它们都是圆锥!", font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(examples), FadeOut(answer),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 圆锥各部分名称
    # ------------------------------------------------------------------
    def scene_2_parts_intro(self):
        title = Text(
            "圆锥的各部分名称", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 绘制大圆锥
        cx, cy_base = 0, -0.5
        cone_w = 3.6
        cone_h = 4.5
        rx = cone_w / 2

        cone = create_cone_2d(
            center=[cx, cy_base, 0], width=cone_w, height=cone_h,
            ellipse_ratio=0.22, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_base=COLOR_BASE, stroke_width=2.5
        )
        self.play(FadeIn(cone), run_time=1.0)
        self.wait(0.5)

        apex_y = cy_base + cone_h  # 4.0

        # 1) 顶点
        apex_highlight = Dot([cx, apex_y, 0], radius=0.12, color=COLOR_APEX)
        apex_label = Text("顶点", font=FONT, font_size=22, color=COLOR_APEX)
        apex_arrow = Arrow(
            start=[cx + 1.8, apex_y + 0.5, 0], end=[cx + 0.2, apex_y + 0.05, 0],
            color=COLOR_APEX, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        apex_label.next_to(apex_arrow.get_start(), RIGHT, buff=0.1)
        self.play(
            FadeIn(apex_highlight, scale=0.5),
            GrowArrow(apex_arrow), FadeIn(apex_label),
            run_time=0.8
        )

        # 2) 底面
        bot_label = Text("底面(圆)", font=FONT, font_size=22, color=COLOR_BASE)
        bot_arrow = Arrow(
            start=[cx + 2.2, cy_base - 1.0, 0], end=[cx + 0.5, cy_base - 0.05, 0],
            color=COLOR_BASE, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        bot_label.next_to(bot_arrow.get_start(), RIGHT, buff=0.1)
        self.play(GrowArrow(bot_arrow), FadeIn(bot_label), run_time=0.6)

        # 3) 侧面
        side_label = Text("侧面(曲面)", font=FONT, font_size=22, color=COLOR_SIDE)
        # 指向侧面中间偏左
        side_target = np.array([cx - rx * 0.5, (cy_base + apex_y) / 2, 0])
        side_arrow = Arrow(
            start=[cx - 2.8, (cy_base + apex_y) / 2 + 0.3, 0],
            end=side_target,
            color=COLOR_SIDE, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        side_label.next_to(side_arrow.get_start(), LEFT, buff=0.1)
        self.play(GrowArrow(side_arrow), FadeIn(side_label), run_time=0.6)

        # 4) 高 (虚线: 从顶点垂直到底面圆心)
        h_line = DashedLine(
            [cx, apex_y, 0], [cx, cy_base, 0],
            color=COLOR_HEIGHT, dash_length=0.12, stroke_width=3
        )
        h_brace = Brace(h_line, direction=RIGHT, color=COLOR_HEIGHT, buff=0.15)
        h_label = Text("高", font=FONT, font_size=24, color=COLOR_HEIGHT
                       ).next_to(h_brace, RIGHT, buff=0.15)
        self.play(Create(h_line), run_time=0.5)
        self.play(FadeIn(h_brace), FadeIn(h_label), run_time=0.5)

        self.wait(2.0)

        # 文字总结
        summary = Text(
            "圆锥 = 一个顶点 + 一个底面 + 一个侧面",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cone), FadeOut(apex_highlight),
            FadeOut(apex_arrow), FadeOut(apex_label),
            FadeOut(bot_arrow), FadeOut(bot_label),
            FadeOut(side_arrow), FadeOut(side_label),
            FadeOut(h_line), FadeOut(h_brace), FadeOut(h_label),
            FadeOut(summary),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 底面特征 — 一个圆形底面
    # ------------------------------------------------------------------
    def scene_3_base(self):
        title = Text(
            "底面的特征", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 圆锥
        cone = create_cone_2d(
            center=[-2.0, 1.0, 0], width=2.4, height=3.0,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_base=COLOR_BASE,
            stroke_width=2
        )
        self.play(FadeIn(cone), run_time=0.8)

        # 底面变成正圆展示
        r_circle = 1.0
        base_circle = Circle(
            radius=r_circle, color=COLOR_BASE,
            fill_opacity=0.35, stroke_width=2.5
        ).move_to([2.0, 2.0, 0])
        base_text = Text("底面", font=FONT, font_size=22, color=COLOR_BASE
                         ).next_to(base_circle, UP, buff=0.2)

        # 引导箭头
        guide_arrow = Arrow(
            start=[-0.5, 0.8, 0], end=[0.8, 1.8, 0],
            color=COLOR_HL, stroke_width=2
        )
        self.play(GrowArrow(guide_arrow), run_time=0.4)
        self.play(
            FadeIn(base_circle), Write(base_text),
            FadeOut(guide_arrow),
            run_time=0.8
        )

        # 标注半径
        r_line = Line(
            base_circle.get_center(),
            base_circle.get_center() + RIGHT * r_circle,
            color=COLOR_HL, stroke_width=2
        )
        r_label = MathTex("r", color=COLOR_HL, font_size=28
                          ).next_to(r_line, UP, buff=0.08)
        center_dot = Dot(base_circle.get_center(), radius=0.05, color=COLOR_HL)
        center_label = Text("O", font=FONT, font_size=18, color=COLOR_HL
                            ).next_to(center_dot, DL, buff=0.08)

        self.play(
            FadeIn(center_dot), FadeIn(center_label),
            Create(r_line), FadeIn(r_label),
            run_time=0.8
        )

        # 与圆柱对比提示
        note1 = Text(
            "圆锥只有一个底面", font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 2.0)
        note2 = Text(
            "(圆柱有两个底面)", font=FONT, font_size=22, color=GRAY_B
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(note1, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(note2), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cone),
            FadeOut(base_circle), FadeOut(base_text),
            FadeOut(r_line), FadeOut(r_label),
            FadeOut(center_dot), FadeOut(center_label),
            FadeOut(note1), FadeOut(note2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 侧面特征 — 曲面, 展开为扇形
    # ------------------------------------------------------------------
    def scene_4_lateral_surface(self):
        title = Text(
            "侧面的特征", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 小圆锥
        cone = create_cone_2d(
            center=[-2.2, 2.5, 0], width=2.0, height=2.8,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, stroke_width=2
        )
        side_lbl = Text("侧面是曲面", font=FONT, font_size=22, color=COLOR_SIDE
                        ).move_to([-2.2, 0.5, 0])
        self.play(FadeIn(cone), FadeIn(side_lbl), run_time=0.8)
        self.wait(0.8)

        # 展开提示
        unfold_hint = Text(
            "沿母线展开...", font=FONT, font_size=22, color=COLOR_HL
        ).move_to([0, 0.3, 0])
        self.play(FadeIn(unfold_hint, shift=RIGHT * 0.3), run_time=0.5)

        # 展开动画: 显示扇形
        # 母线长(斜高) l = sqrt(r^2 + h^2), 这里 r=1.0, h=2.8
        r_base = 1.0
        h_cone = 2.8
        slant_height = np.sqrt(r_base**2 + h_cone**2)  # ~2.97
        # 扇形圆心角 = 2*pi*r / l (弧度)
        sector_angle = 2 * PI * r_base / slant_height  # ~2.11 rad

        # 绘制扇形 (展开后的侧面)
        display_radius = 2.2  # 缩放后显示大小
        sector = AnnularSector(
            inner_radius=0,
            outer_radius=display_radius,
            angle=sector_angle,
            start_angle=PI / 2 - sector_angle / 2,  # 居中显示
            color=COLOR_SIDE,
            fill_opacity=0.25,
            stroke_width=2.5
        ).move_to([1.5, -2.5, 0])

        self.play(
            FadeOut(unfold_hint),
            FadeIn(sector, shift=DOWN * 0.3),
            run_time=1.0
        )

        # 标注
        # 母线长
        sector_center = sector.get_center()
        l_label_group = VGroup(
            Text("母线长", font=FONT, font_size=18, color=COLOR_HL),
            MathTex(r"l", color=COLOR_HL, font_size=24)
        ).arrange(RIGHT, buff=0.1).next_to(sector, RIGHT, buff=0.3)

        # 弧长 = 底面周长
        arc_label_group = VGroup(
            Text("弧长 = 底面周长", font=FONT, font_size=18, color=COLOR_BASE),
        ).next_to(sector, DOWN, buff=0.3)

        self.play(
            FadeIn(l_label_group), FadeIn(arc_label_group),
            run_time=0.8
        )

        # 结论
        conclusion = Text(
            "侧面展开是扇形", font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cone), FadeOut(side_lbl),
            FadeOut(sector), FadeOut(l_label_group),
            FadeOut(arc_label_group), FadeOut(conclusion),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 高的特征 — 只有一条
    # ------------------------------------------------------------------
    def scene_5_height(self):
        title = Text(
            "圆锥的高", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 圆锥
        cx, cy_base = 0, -0.5
        cone_w = 3.2
        cone_h = 4.0
        rx = cone_w / 2
        apex_y = cy_base + cone_h

        cone = create_cone_2d(
            center=[cx, cy_base, 0], width=cone_w, height=cone_h,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_base=COLOR_BASE, stroke_width=2
        )
        self.play(FadeIn(cone), run_time=0.8)

        # 定义
        defn = Text(
            "高 = 从顶点到底面圆心的距离",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(defn), run_time=0.5)

        # 标注顶点和底面圆心
        apex_dot = Dot([cx, apex_y, 0], radius=0.1, color=COLOR_APEX)
        apex_text = Text("顶点", font=FONT, font_size=18, color=COLOR_APEX
                         ).next_to(apex_dot, UR, buff=0.1)

        center_dot = Dot([cx, cy_base, 0], radius=0.1, color=COLOR_BASE)
        center_text = Text("底面圆心", font=FONT, font_size=18, color=COLOR_BASE
                           ).next_to(center_dot, DR, buff=0.15)

        self.play(
            FadeIn(apex_dot), FadeIn(apex_text),
            FadeIn(center_dot), FadeIn(center_text),
            run_time=0.6
        )

        # 画高线
        h_line = DashedLine(
            [cx, apex_y, 0], [cx, cy_base, 0],
            color=COLOR_HEIGHT, dash_length=0.12, stroke_width=3
        )
        h_brace = Brace(h_line, direction=RIGHT, color=COLOR_HEIGHT, buff=0.15)
        h_label = MathTex("h", color=COLOR_HEIGHT, font_size=30
                          ).next_to(h_brace, RIGHT, buff=0.1)

        self.play(Create(h_line), run_time=0.6)
        self.play(FadeIn(h_brace), FadeIn(h_label), run_time=0.5)

        # 直角标记
        right_angle_size = 0.25
        right_angle = VGroup(
            Line([cx, cy_base, 0], [cx + right_angle_size, cy_base, 0],
                 color=COLOR_HEIGHT, stroke_width=2),
            Line([cx + right_angle_size, cy_base, 0],
                 [cx + right_angle_size, cy_base + right_angle_size, 0],
                 color=COLOR_HEIGHT, stroke_width=2),
            Line([cx + right_angle_size, cy_base + right_angle_size, 0],
                 [cx, cy_base + right_angle_size, 0],
                 color=COLOR_HEIGHT, stroke_width=2),
        )
        self.play(FadeIn(right_angle), run_time=0.4)

        # 关键特征
        feat1 = Text(
            "圆锥的高只有一条!", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 3.5)
        feat2 = Text(
            "(圆柱的高有无数条)", font=FONT, font_size=22, color=GRAY_B
        ).move_to(DOWN * 4.3)

        self.play(FadeIn(feat1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(feat2), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cone), FadeOut(defn),
            FadeOut(apex_dot), FadeOut(apex_text),
            FadeOut(center_dot), FadeOut(center_text),
            FadeOut(h_line), FadeOut(h_brace), FadeOut(h_label),
            FadeOut(right_angle),
            FadeOut(feat1), FadeOut(feat2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 旋转生成 — 直角三角形绕直角边旋转
    # ------------------------------------------------------------------
    def scene_6_rotation(self):
        title = Text(
            "圆锥的生成", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        subtitle = Text(
            "直角三角形绕一条直角边旋转",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.5)

        # 轴线 (竖直)
        axis_bottom = np.array([0, -0.5, 0])
        axis_top = np.array([0, 3.5, 0])
        axis_line = DashedLine(
            axis_bottom, axis_top,
            color=GRAY_B, dash_length=0.12, stroke_width=2
        )
        axis_label = Text(
            "旋转轴", font=FONT, font_size=18, color=GRAY_B
        ).next_to(axis_line, LEFT, buff=0.2).shift(UP * 0.5)

        self.play(Create(axis_line), FadeIn(axis_label), run_time=0.6)

        # 直角三角形 (左边贴轴, 直角在底部)
        tri_w = 1.8  # 底边(半径)
        tri_h = 3.0  # 高

        A = np.array([0, -0.5, 0])         # 直角顶点(底部轴上)
        B = np.array([tri_w, -0.5, 0])     # 底边右端
        C = np.array([0, -0.5 + tri_h, 0]) # 高的顶点(轴上)

        triangle = Polygon(
            A, B, C,
            color=COLOR_ACCENT, fill_opacity=0.3,
            stroke_width=2.5
        )

        tri_label = Text(
            "直角三角形", font=FONT, font_size=20, color=COLOR_ACCENT
        ).next_to(triangle, RIGHT, buff=0.3)

        self.play(Create(triangle), FadeIn(tri_label), run_time=0.8)
        self.wait(0.3)

        # 标注边
        r_label = MathTex("r", color=COLOR_HL, font_size=24
                          ).move_to([tri_w / 2, -0.9, 0])
        h_label = MathTex("h", color=COLOR_HEIGHT, font_size=24
                          ).move_to([-0.4, -0.5 + tri_h / 2, 0])

        # 直角标记
        ra_size = 0.25
        right_angle_mark = VGroup(
            Line(A, A + RIGHT * ra_size, color=WHITE, stroke_width=1.5),
            Line(A + RIGHT * ra_size, A + RIGHT * ra_size + UP * ra_size,
                 color=WHITE, stroke_width=1.5),
            Line(A + RIGHT * ra_size + UP * ra_size, A + UP * ra_size,
                 color=WHITE, stroke_width=1.5),
        )

        self.play(
            FadeIn(r_label), FadeIn(h_label), FadeIn(right_angle_mark),
            run_time=0.5
        )

        # 旋转动画提示
        rotate_hint = Text(
            "旋转一周...", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(rotate_hint), run_time=0.4)

        # Ghost 三角形表示旋转
        ghost_tris = VGroup()
        n_ghosts = 8
        for i in range(1, n_ghosts + 1):
            angle = i * PI / n_ghosts
            projected_w = tri_w * np.cos(angle)
            if abs(projected_w) < 0.05:
                continue
            A_g = np.array([0, -0.5, 0])
            B_g = np.array([projected_w, -0.5, 0])
            C_g = np.array([0, -0.5 + tri_h, 0])
            ghost = Polygon(
                A_g, B_g, C_g,
                color=COLOR_CONE, fill_opacity=0.06,
                stroke_width=1, stroke_opacity=0.3
            )
            ghost_tris.add(ghost)

        self.play(
            LaggedStart(*[FadeIn(g, run_time=0.3) for g in ghost_tris],
                        lag_ratio=0.12),
            run_time=1.5
        )

        # 最终变成圆锥
        final_cone = create_cone_2d(
            center=[0, -0.5, 0], width=tri_w * 2, height=tri_h,
            ellipse_ratio=0.25, stroke_color=COLOR_CONE,
            fill_side=COLOR_SIDE, fill_base=COLOR_BASE, stroke_width=2.5
        )

        self.play(
            FadeOut(triangle), FadeOut(tri_label),
            FadeOut(ghost_tris), FadeOut(r_label), FadeOut(h_label),
            FadeOut(right_angle_mark), FadeOut(rotate_hint),
            FadeIn(final_cone),
            run_time=1.0
        )

        result_text = Text(
            "直角三角形绕直角边旋转得到圆锥",
            font=FONT, font_size=22, color=COLOR_RESULT
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(result_text, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(axis_line), FadeOut(axis_label),
            FadeOut(final_cone), FadeOut(result_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 与圆柱的区别
    # ------------------------------------------------------------------
    def scene_7_compare_cylinder(self):
        title = Text(
            "圆锥 vs 圆柱", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 左边: 圆锥
        cone = create_cone_2d(
            center=[-2.2, 0.5, 0], width=2.2, height=3.0,
            ellipse_ratio=0.22, stroke_color=COLOR_CONE,
            fill_side=COLOR_SIDE, fill_base=COLOR_BASE, stroke_width=2
        )
        cone_label = Text(
            "圆锥", font=FONT, font_size=26, color=COLOR_CONE
        ).move_to([-2.2, 4.2, 0])

        # 右边: 圆柱
        cyl = create_cylinder_2d_simple(
            center=[2.2, 2.0, 0], width=2.2, height=3.0,
            ellipse_ratio=0.22, stroke_color=COLOR_CYL,
            fill_side=COLOR_CYL, fill_top=COLOR_CYL, stroke_width=2
        )
        cyl_label = Text(
            "圆柱", font=FONT, font_size=26, color=COLOR_CYL
        ).move_to([2.2, 4.2, 0])

        self.play(
            FadeIn(cone), FadeIn(cone_label),
            FadeIn(cyl), FadeIn(cyl_label),
            run_time=1.0
        )
        self.wait(0.5)

        # 对比表格 (用文字实现)
        compare_data = [
            ("底面", "一个圆", "两个相同的圆"),
            ("顶点", "有一个", "没有"),
            ("侧面", "曲面(展开扇形)", "曲面(展开长方形)"),
            ("高", "只有一条", "有无数条"),
        ]

        table_group = VGroup()
        y_start = -2.0
        for i, (item, cone_val, cyl_val) in enumerate(compare_data):
            y_pos = y_start - i * 1.0

            item_text = Text(item, font=FONT, font_size=20, color=COLOR_HL
                             ).move_to([-3.5, y_pos, 0])

            cone_text = Text(cone_val, font=FONT, font_size=18, color=COLOR_CONE
                             ).move_to([-1.2, y_pos, 0])

            cyl_text = Text(cyl_val, font=FONT, font_size=18, color=COLOR_CYL
                            ).move_to([2.0, y_pos, 0])

            row = VGroup(item_text, cone_text, cyl_text)
            table_group.add(row)

        # 表头
        header_line = Line(
            [-4.0, y_start + 0.5, 0], [4.0, y_start + 0.5, 0],
            color=GRAY_B, stroke_width=1
        )

        self.play(
            FadeIn(header_line),
            LaggedStart(*[FadeIn(row, shift=RIGHT * 0.2) for row in table_group],
                        lag_ratio=0.3),
            run_time=2.0
        )
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cone), FadeOut(cone_label),
            FadeOut(cyl), FadeOut(cyl_label),
            FadeOut(table_group), FadeOut(header_line),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结
    # ------------------------------------------------------------------
    def scene_8_summary(self):
        title = Text(
            "知识总结", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 小圆锥插图
        cone_small = create_cone_2d(
            center=[0, 2.5, 0], width=2.2, height=3.0,
            ellipse_ratio=0.22, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_base=COLOR_BASE, stroke_width=2
        )
        self.play(FadeIn(cone_small), run_time=0.6)

        # 要点卡片
        points_data = [
            ("1.", "顶点", "圆锥有一个顶点", COLOR_APEX),
            ("2.", "底面", "一个圆形底面", COLOR_BASE),
            ("3.", "侧面", "一个曲面(展开为扇形)", COLOR_SIDE),
            ("4.", "高", "只有一条(顶点到底面圆心)", COLOR_HEIGHT),
            ("5.", "生成", "直角三角形绕直角边旋转", COLOR_ACCENT),
        ]

        cards = VGroup()
        for i, (num, key, desc, color) in enumerate(points_data):
            num_mob = Text(num, font=FONT, font_size=22, color=color)
            key_mob = Text(key, font=FONT, font_size=24, color=color, weight=BOLD)
            desc_mob = Text(desc, font=FONT, font_size=18, color=GRAY_A)
            row = VGroup(num_mob, key_mob, desc_mob).arrange(RIGHT, buff=0.2)
            cards.add(row)

        cards.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        cards.move_to(DOWN * 1.5)

        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards],
                        lag_ratio=0.35),
            run_time=2.5
        )
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cone_small), FadeOut(cards),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------
    def scene_9_outro(self):
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

        # 装饰小圆锥
        deco_cones = VGroup()
        angles_list = [0, PI / 3, 2 * PI / 3, PI, 4 * PI / 3, 5 * PI / 3]
        deco_colors = ["#f97316", "#ef4444", "#3b82f6", "#8b5cf6", "#22c55e", "#f59e0b"]
        for a, dc in zip(angles_list, deco_colors):
            pos = follow.get_center() + 2.5 * np.array([np.cos(a), np.sin(a), 0])
            mini_cone = create_cone_2d(
                center=pos + DOWN * 0.3, width=0.5, height=0.6,
                ellipse_ratio=0.3, stroke_color=dc,
                fill_side=dc, stroke_width=1.5,
                show_back_arc=False
            )
            deco_cones.add(mini_cone)

        self.play(
            LaggedStart(*[FadeIn(dc, scale=0.5) for dc in deco_cones],
                        lag_ratio=0.1),
            run_time=0.8
        )
        self.wait(2.0)

        # 淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_cones),
            run_time=0.8
        )


# 运行命令:
# manim -pql 004_圆锥的认识.py ConeRecognitionLesson   # 快速预览
# manim -qm 004_圆锥的认识.py ConeRecognitionLesson    # 中等质量
# manim -qh 004_圆锥的认识.py ConeRecognitionLesson    # 高质量

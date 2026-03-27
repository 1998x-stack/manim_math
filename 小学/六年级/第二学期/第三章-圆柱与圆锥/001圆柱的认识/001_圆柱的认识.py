"""
001_圆柱的认识.py — 圆柱的认识 教学动画

知识点: 圆柱的特征、各部分名称、旋转体生成
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 生活中的圆柱
  2. 圆柱的各部分名称: 底面、侧面、高
  3. 底面特征: 两个完全相同的圆
  4. 侧面特征: 曲面, 展开为长方形
  5. 高的特征: 无数条且相等
  6. 旋转生成: 长方形绕一边旋转
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
COLOR_CYLINDER = "#3b82f6"       # 蓝色 圆柱主体
COLOR_TOP = "#60a5fa"            # 浅蓝 顶面
COLOR_BOTTOM = "#2563eb"         # 深蓝 底面
COLOR_SIDE = "#8b5cf6"           # 紫色 侧面
COLOR_HEIGHT = "#f59e0b"         # 橙色 高
COLOR_HL = "#fbbf24"             # 黄色高亮
COLOR_RESULT = "#22c55e"         # 绿色 结果/正确
COLOR_ACCENT = "#ef4444"         # 红色强调
COLOR_AUTHOR = "#6b7280"         # 灰色作者信息
COLOR_LABEL = WHITE              # 标签颜色
FONT = "Noto Sans CJK SC"


# ======================================================================
# 辅助: 绘制 2D 圆柱示意图 (用椭圆 + 线段)
# ======================================================================

def create_cylinder_2d(
    center=ORIGIN, width=2.4, height=3.0,
    ellipse_ratio=0.3, stroke_color=WHITE, fill_top=None,
    fill_bottom=None, fill_side=None, stroke_width=2.5
):
    """
    用 2D 元素组合绘制圆柱示意图 (前视图)
    返回 VGroup: [side_fill, bottom_ellipse, left_line, right_line, top_ellipse,
                  back_arc_dashed]
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

    # --- 底部椭圆 (完整, 前半实线后半虚线) ---
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

    # --- 顶部椭圆 (完整实线) ---
    top_ellipse = Ellipse(
        width=width, height=width * ellipse_ratio * 2,
        color=stroke_color, stroke_width=stroke_width
    ).move_to([cx, top_cy, 0])
    if fill_top:
        top_ellipse.set_fill(fill_top, opacity=0.4)
    parts["top_ellipse"] = top_ellipse

    # 组装 (按渲染顺序)
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

class CylinderRecognitionLesson(Scene):
    """
    圆柱的认识 教学动画场景

    场景顺序:
      1. 开场钩子
      2. 圆柱各部分名称
      3. 底面特征
      4. 侧面特征(展开)
      5. 高的特征
      6. 旋转生成
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_parts_intro()
        self.scene_3_bases()
        self.scene_4_lateral_surface()
        self.scene_5_height()
        self.scene_6_rotation()
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
            "生活中的圆柱,\n你了解多少?",
            font=FONT, font_size=40, color=COLOR_HL,
            line_spacing=1.4
        ).move_to(UP * 4.5)
        self.play(Write(hook), run_time=1.0)

        # 生活实例: 水杯、易拉罐、柱子 (用简笔图形)
        examples = VGroup()
        labels_text = ["水杯", "易拉罐", "柱子"]
        x_positions = [-2.5, 0, 2.5]
        for i, (lbl, xp) in enumerate(zip(labels_text, x_positions)):
            cyl = create_cylinder_2d(
                center=[xp, 0.5, 0], width=1.2, height=1.8,
                ellipse_ratio=0.28, stroke_color=COLOR_CYLINDER,
                fill_side=COLOR_CYLINDER, fill_top=COLOR_TOP,
                stroke_width=2
            )
            label = Text(lbl, font=FONT, font_size=20, color=GRAY_A
                         ).next_to(cyl, DOWN, buff=0.3)
            examples.add(VGroup(cyl, label))

        self.play(
            LaggedStart(*[FadeIn(ex, shift=UP * 0.3) for ex in examples],
                        lag_ratio=0.3),
            run_time=1.5
        )
        self.wait(1.0)

        question = Text(
            "它们都是圆柱!", font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(examples), FadeOut(question),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 圆柱各部分名称
    # ------------------------------------------------------------------
    def scene_2_parts_intro(self):
        title = Text(
            "圆柱的各部分名称", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 绘制大圆柱
        cyl = create_cylinder_2d(
            center=[0, 1.0, 0], width=3.2, height=4.0,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2.5
        )
        self.play(FadeIn(cyl), run_time=1.0)
        self.wait(0.5)

        # 各部分标注
        # 圆柱参数
        cx, cy = 0, 1.0
        cyl_w, cyl_h = 3.2, 4.0
        rx = cyl_w / 2
        top_cy = cy + cyl_h / 2  # 3.0
        bot_cy = cy - cyl_h / 2  # -1.0

        # 顶面标签
        top_label = Text("上底面", font=FONT, font_size=22, color=COLOR_TOP)
        top_arrow = Arrow(
            start=[2.5, top_cy + 0.8, 0], end=[0.5, top_cy, 0],
            color=COLOR_TOP, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        top_label.next_to(top_arrow.get_start(), RIGHT, buff=0.15)
        self.play(GrowArrow(top_arrow), FadeIn(top_label), run_time=0.6)

        # 底面标签
        bot_label = Text("下底面", font=FONT, font_size=22, color=COLOR_BOTTOM)
        bot_arrow = Arrow(
            start=[2.5, bot_cy - 0.8, 0], end=[0.5, bot_cy, 0],
            color=COLOR_BOTTOM, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        bot_label.next_to(bot_arrow.get_start(), RIGHT, buff=0.15)
        self.play(GrowArrow(bot_arrow), FadeIn(bot_label), run_time=0.6)

        # 侧面标签
        side_label = Text("侧面", font=FONT, font_size=22, color=COLOR_SIDE)
        side_arrow = Arrow(
            start=[-2.8, cy, 0], end=[-rx - 0.05, cy, 0],
            color=COLOR_SIDE, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        side_label.next_to(side_arrow.get_start(), LEFT, buff=0.15)
        self.play(GrowArrow(side_arrow), FadeIn(side_label), run_time=0.6)

        # 高
        h_line = DashedLine(
            [0, top_cy, 0], [0, bot_cy, 0],
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
            "圆柱 = 两个底面 + 一个侧面",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl),
            FadeOut(top_label), FadeOut(top_arrow),
            FadeOut(bot_label), FadeOut(bot_arrow),
            FadeOut(side_label), FadeOut(side_arrow),
            FadeOut(h_line), FadeOut(h_brace), FadeOut(h_label),
            FadeOut(summary),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 底面特征 — 两个完全相同的圆
    # ------------------------------------------------------------------
    def scene_3_bases(self):
        title = Text(
            "底面的特征", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 圆柱
        cyl = create_cylinder_2d(
            center=[-2.0, 2.0, 0], width=2.4, height=3.0,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_top=COLOR_TOP, fill_bottom=COLOR_BOTTOM,
            stroke_width=2
        )
        self.play(FadeIn(cyl), run_time=0.8)

        # 提取两个底面变成圆 (平面视角)
        r_circle = 0.9

        top_circle = Circle(
            radius=r_circle, color=COLOR_TOP,
            fill_opacity=0.35, stroke_width=2.5
        ).move_to([2.0, 3.5, 0])
        top_text = Text("上底面", font=FONT, font_size=20, color=COLOR_TOP
                        ).next_to(top_circle, UP, buff=0.2)

        bot_circle = Circle(
            radius=r_circle, color=COLOR_BOTTOM,
            fill_opacity=0.35, stroke_width=2.5
        ).move_to([2.0, 0.5, 0])
        bot_text = Text("下底面", font=FONT, font_size=20, color=COLOR_BOTTOM
                        ).next_to(bot_circle, DOWN, buff=0.2)

        self.play(
            FadeIn(top_circle), Write(top_text),
            run_time=0.8
        )
        self.play(
            FadeIn(bot_circle), Write(bot_text),
            run_time=0.8
        )

        # 标注半径 r
        r_line_top = Line(
            top_circle.get_center(),
            top_circle.get_center() + RIGHT * r_circle,
            color=COLOR_HL, stroke_width=2
        )
        r_label_top = MathTex("r", color=COLOR_HL, font_size=28
                              ).next_to(r_line_top, UP, buff=0.08)

        r_line_bot = Line(
            bot_circle.get_center(),
            bot_circle.get_center() + RIGHT * r_circle,
            color=COLOR_HL, stroke_width=2
        )
        r_label_bot = MathTex("r", color=COLOR_HL, font_size=28
                              ).next_to(r_line_bot, UP, buff=0.08)

        self.play(
            Create(r_line_top), FadeIn(r_label_top),
            Create(r_line_bot), FadeIn(r_label_bot),
            run_time=0.8
        )

        # 等号
        eq_sign = MathTex("=", color=COLOR_RESULT, font_size=48
                          ).move_to([2.0, 2.0, 0])
        self.play(Write(eq_sign), run_time=0.5)

        # 结论
        conclusion = Text(
            "两个底面完全相同",
            font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 2.5)
        detail = Text(
            "形状相同, 大小相等",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.3)

        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(detail), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl),
            FadeOut(top_circle), FadeOut(top_text),
            FadeOut(bot_circle), FadeOut(bot_text),
            FadeOut(r_line_top), FadeOut(r_label_top),
            FadeOut(r_line_bot), FadeOut(r_label_bot),
            FadeOut(eq_sign), FadeOut(conclusion), FadeOut(detail),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 侧面特征 — 展开成长方形
    # ------------------------------------------------------------------
    def scene_4_lateral_surface(self):
        title = Text(
            "侧面的特征", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        # 小圆柱
        cyl = create_cylinder_2d(
            center=[-2.2, 3.0, 0], width=2.0, height=2.5,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, stroke_width=2
        )
        side_lbl = Text("侧面是曲面", font=FONT, font_size=22, color=COLOR_SIDE
                        ).move_to([-2.2, 0.8, 0])
        self.play(FadeIn(cyl), FadeIn(side_lbl), run_time=0.8)
        self.wait(0.8)

        # 展开提示
        unfold_hint = Text(
            "沿母线展开...", font=FONT, font_size=22, color=COLOR_HL
        ).move_to([0, 0.5, 0])
        self.play(FadeIn(unfold_hint, shift=RIGHT * 0.3), run_time=0.5)

        # 展开动画: 显示长方形
        cyl_w, cyl_h_val = 2.0, 2.5
        r_val = cyl_w / 2
        rect_width = 2 * PI * r_val  # 周长 ≈ 6.28, 缩放到适合屏幕
        display_rect_w = 5.5
        display_rect_h = cyl_h_val
        scale_factor = display_rect_w / rect_width

        rect = Rectangle(
            width=display_rect_w, height=display_rect_h,
            color=COLOR_SIDE, fill_opacity=0.2,
            stroke_width=2.5
        ).move_to([1.5, -2.5, 0])

        self.play(
            FadeOut(unfold_hint),
            FadeIn(rect, shift=DOWN * 0.3),
            run_time=1.0
        )

        # 标注长方形尺寸
        # 宽 = 底面周长
        w_brace = Brace(rect, DOWN, color=COLOR_HL, buff=0.1)
        w_parts = VGroup(
            Text("底面周长", font=FONT, font_size=18, color=COLOR_HL),
            MathTex(r"= 2\pi r", color=COLOR_HL, font_size=24)
        ).arrange(RIGHT, buff=0.15)
        w_parts.next_to(w_brace, DOWN, buff=0.15)

        h_brace = Brace(rect, RIGHT, color=COLOR_HEIGHT, buff=0.1)
        h_parts = VGroup(
            Text("高", font=FONT, font_size=18, color=COLOR_HEIGHT),
            MathTex(r"= h", color=COLOR_HEIGHT, font_size=24)
        ).arrange(RIGHT, buff=0.1)
        h_parts.next_to(h_brace, RIGHT, buff=0.15)

        self.play(
            FadeIn(w_brace), FadeIn(w_parts),
            FadeIn(h_brace), FadeIn(h_parts),
            run_time=0.8
        )

        # 结论
        conclusion = Text(
            "侧面展开是长方形", font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl), FadeOut(side_lbl),
            FadeOut(rect),
            FadeOut(w_brace), FadeOut(w_parts),
            FadeOut(h_brace), FadeOut(h_parts),
            FadeOut(conclusion),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 高的特征
    # ------------------------------------------------------------------
    def scene_5_height(self):
        title = Text(
            "圆柱的高", font=FONT, font_size=36, color=GOLD
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
            fill_bottom=COLOR_BOTTOM, stroke_width=2
        )
        self.play(FadeIn(cyl), run_time=0.8)

        # 定义: 高
        defn = Text(
            "高 = 两个底面之间的距离",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(FadeIn(defn), run_time=0.5)

        # 绘制多条高
        num_heights = 5
        height_lines = VGroup()
        height_colors = [COLOR_HEIGHT, "#fb923c", "#fbbf24", "#a3e635", "#34d399"]
        for i in range(num_heights):
            # 在椭圆上均匀取点 (角度从 -80 deg 到 +80 deg)
            angle = -80 * DEGREES + i * (160 * DEGREES / (num_heights - 1))
            x_offset = rx * np.cos(angle)
            # 对应椭圆上 y 偏移
            ry_offset = rx * 0.25 * np.sin(angle)

            top_pt = [cx + x_offset, top_cy + ry_offset, 0]
            bot_pt = [cx + x_offset, bot_cy + ry_offset, 0]

            h_line = DashedLine(
                top_pt, bot_pt,
                color=height_colors[i % len(height_colors)],
                dash_length=0.1, stroke_width=2.5
            )
            height_lines.add(h_line)

        # 依次显示高线
        for i, h_line in enumerate(height_lines):
            self.play(Create(h_line), run_time=0.4)

        # h 标注 (用中间那条)
        mid_line = height_lines[2]
        h_brace = Brace(mid_line, direction=LEFT, color=COLOR_HEIGHT, buff=0.1)
        h_label = MathTex("h", color=COLOR_HEIGHT, font_size=30
                          ).next_to(h_brace, LEFT, buff=0.1)
        self.play(FadeIn(h_brace), FadeIn(h_label), run_time=0.5)

        # 特征总结
        feat1 = Text(
            "高有无数条", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 3.0)
        feat2 = Text(
            "且长度都相等", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(feat1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(feat2, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl), FadeOut(defn),
            FadeOut(height_lines), FadeOut(h_brace), FadeOut(h_label),
            FadeOut(feat1), FadeOut(feat2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 旋转生成 — 长方形绕一边旋转
    # ------------------------------------------------------------------
    def scene_6_rotation(self):
        title = Text(
            "圆柱的生成", font=FONT, font_size=36, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.8)

        subtitle = Text(
            "长方形绕一条边旋转", font=FONT, font_size=24, color=GRAY_A
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

        # 长方形 (竖着, 左边贴轴)
        rect_w = 1.8
        rect_h = 3.0
        rect_center = np.array([rect_w / 2, 1.5, 0])

        rect = Rectangle(
            width=rect_w, height=rect_h,
            color=COLOR_ACCENT, fill_opacity=0.3,
            stroke_width=2.5
        ).move_to(rect_center)

        rect_label = Text(
            "长方形", font=FONT, font_size=20, color=COLOR_ACCENT
        ).next_to(rect, RIGHT, buff=0.3)

        self.play(Create(rect), FadeIn(rect_label), run_time=0.8)
        self.wait(0.5)

        # 标注长方形尺寸
        w_label = VGroup(
            MathTex("r", color=COLOR_HL, font_size=24),
        ).move_to([rect_w / 2, 3.3, 0])
        h_label_r = VGroup(
            MathTex("h", color=COLOR_HEIGHT, font_size=24),
        ).move_to([rect_w + 0.4, 1.5, 0])
        self.play(FadeIn(w_label), FadeIn(h_label_r), run_time=0.5)

        # 旋转动画: 长方形 -> 圆柱
        # 使用中间帧显示旋转效果
        rotate_hint = Text(
            "旋转一周...", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(rotate_hint), run_time=0.4)

        # 旋转长方形 (显示为多个 ghost 矩形表示旋转过程)
        ghost_rects = VGroup()
        n_ghosts = 8
        for i in range(1, n_ghosts + 1):
            angle = i * PI / n_ghosts
            # 旋转后的矩形宽度投影
            projected_w = rect_w * np.cos(angle)
            if abs(projected_w) < 0.05:
                continue
            ghost = Rectangle(
                width=abs(projected_w), height=rect_h,
                color=COLOR_CYLINDER, fill_opacity=0.08,
                stroke_width=1, stroke_opacity=0.3
            )
            # 中心位置
            ghost.move_to([projected_w / 2, 1.5, 0])
            ghost_rects.add(ghost)

        self.play(
            LaggedStart(*[FadeIn(g, run_time=0.3) for g in ghost_rects],
                        lag_ratio=0.15),
            run_time=1.5
        )

        # 最终变成圆柱
        final_cyl = create_cylinder_2d(
            center=[0, 1.5, 0], width=rect_w * 2, height=rect_h,
            ellipse_ratio=0.25, stroke_color=COLOR_CYLINDER,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2.5
        )

        self.play(
            FadeOut(rect), FadeOut(rect_label),
            FadeOut(ghost_rects), FadeOut(w_label), FadeOut(h_label_r),
            FadeOut(rotate_hint),
            FadeIn(final_cyl),
            run_time=1.0
        )

        result_text = Text(
            "长方形绕一边旋转得到圆柱",
            font=FONT, font_size=24, color=COLOR_RESULT
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(result_text, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(axis_line), FadeOut(axis_label),
            FadeOut(final_cyl), FadeOut(result_text),
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

        # 小圆柱插图
        cyl_small = create_cylinder_2d(
            center=[0, 3.0, 0], width=2.0, height=2.5,
            ellipse_ratio=0.25, stroke_color=WHITE,
            fill_side=COLOR_SIDE, fill_top=COLOR_TOP,
            fill_bottom=COLOR_BOTTOM, stroke_width=2
        )
        self.play(FadeIn(cyl_small), run_time=0.6)

        # 要点卡片
        points_data = [
            ("1.", "底面", "两个完全相同的圆", COLOR_TOP),
            ("2.", "侧面", "一个曲面 (展开为长方形)", COLOR_SIDE),
            ("3.", "高", "无数条, 长度都相等", COLOR_HEIGHT),
            ("4.", "生成", "长方形绕一边旋转", COLOR_ACCENT),
        ]

        cards = VGroup()
        for i, (num, key, desc, color) in enumerate(points_data):
            num_mob = Text(num, font=FONT, font_size=22, color=color)
            key_mob = Text(key, font=FONT, font_size=24, color=color, weight=BOLD)
            desc_mob = Text(desc, font=FONT, font_size=20, color=GRAY_A)
            row = VGroup(num_mob, key_mob, desc_mob).arrange(RIGHT, buff=0.2)
            cards.add(row)

        cards.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        cards.move_to(DOWN * 1.0)

        self.play(
            LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards],
                        lag_ratio=0.4),
            run_time=2.5
        )
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl_small), FadeOut(cards),
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
# manim -pql 001_圆柱的认识.py CylinderRecognitionLesson   # 快速预览
# manim -qm 001_圆柱的认识.py CylinderRecognitionLesson    # 中等质量
# manim -qh 001_圆柱的认识.py CylinderRecognitionLesson    # 高质量

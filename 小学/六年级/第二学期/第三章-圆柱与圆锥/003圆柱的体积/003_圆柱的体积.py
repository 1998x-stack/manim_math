"""
003_圆柱的体积.py — 圆柱的体积 教学动画

知识点: 圆柱体积公式推导(转化思想)、V=Sh=pi*r^2*h、极限思想
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 回顾: 长方体体积 = 底面积 x 高
  3. 转化思想: 将圆柱切割拼合成近似长方体
  4. 切割动画: 4等分 -> 8等分 -> 16等分 (越来越接近长方体)
  5. 推导公式: V = S底 x h = pi*r^2*h
  6. 例题: 已知底面半径和高, 求体积
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
COLOR_CYLINDER = "#3b82f6"       # 蓝色 圆柱
COLOR_RECT = "#f59e0b"           # 橙色 长方体
COLOR_RESULT = "#22c55e"         # 绿色 结果
COLOR_HL = "#fbbf24"             # 黄色高亮
COLOR_ACCENT = "#a78bfa"         # 紫色强调
COLOR_SUB = "#ef4444"            # 红色
COLOR_AUTHOR = "#6b7280"         # 灰色作者信息
COLOR_RADIUS = "#f472b6"         # 粉色 半径
COLOR_HEIGHT = "#38bdf8"         # 天蓝色 高
COLOR_AREA = "#34d399"           # 绿色 面积
FONT = "Heiti SC"


# ======================================================================
# 辅助函数
# ======================================================================

def cn(text, **kwargs):
    """创建中文文本的便捷函数"""
    defaults = {"font": FONT}
    defaults.update(kwargs)
    return Text(text, **defaults)


def create_cylinder_side_view(radius, height, center, color=COLOR_CYLINDER,
                               fill_opacity=0.3, stroke_width=2.5):
    """
    创建圆柱的2D侧视图（椭圆顶 + 矩形侧面 + 椭圆底）
    返回 VGroup(底面椭圆, 侧面矩形, 顶面椭圆, 左边线, 右边线)
    """
    cx, cy = center[0], center[1]
    ellipse_ratio = 0.35  # 椭圆扁率

    # 底面椭圆
    bottom_ellipse = Ellipse(
        width=radius * 2, height=radius * 2 * ellipse_ratio,
        color=color, stroke_width=stroke_width, fill_opacity=fill_opacity * 0.5
    ).move_to([cx, cy - height / 2, 0])

    # 顶面椭圆
    top_ellipse = Ellipse(
        width=radius * 2, height=radius * 2 * ellipse_ratio,
        color=color, stroke_width=stroke_width, fill_opacity=fill_opacity
    ).move_to([cx, cy + height / 2, 0])

    # 左右边线
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

    # 侧面填充
    side_rect = Polygon(
        [cx - radius, cy - height / 2, 0],
        [cx + radius, cy - height / 2, 0],
        [cx + radius, cy + height / 2, 0],
        [cx - radius, cy + height / 2, 0],
        color=color, fill_opacity=fill_opacity * 0.4,
        stroke_width=0
    )

    return VGroup(bottom_ellipse, side_rect, left_line, right_line, top_ellipse)


def create_sector_piece(radius, start_angle, end_angle, height, center,
                         color_top, color_side, ellipse_ratio=0.35):
    """
    创建一个扇形切片的2D表示(侧面视图)
    用于展示圆柱切割后的扇形柱体
    """
    cx, cy = center[0], center[1]
    mid_angle = (start_angle + end_angle) / 2
    # 扇形的宽度近似
    chord_width = 2 * radius * np.sin((end_angle - start_angle) / 2)

    # 侧面 - 用梯形近似
    piece = RoundedRectangle(
        width=chord_width, height=height,
        corner_radius=0.02,
        color=color_side,
        fill_opacity=0.5,
        stroke_width=1.5
    )

    return piece


# ======================================================================
# 主场景
# ======================================================================

class CylinderVolumeLesson(Scene):
    """
    圆柱的体积教学动画

    场景顺序:
      1. 开场钩子
      2. 回顾长方体体积
      3. 转化思想引入
      4. 切割动画演示 (4份 -> 8份 -> 16份)
      5. 公式推导
      6. 例题演练
      7. 总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_review_cuboid()
        self.scene_3_transformation_idea()
        self.scene_4_cutting_animation()
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
        hook = cn("圆柱的体积", font_size=44, color=COLOR_HL).move_to(UP * 5.5)
        hook2 = cn("怎么算?", font_size=38, color=WHITE).move_to(UP * 4.7)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # 画一个圆柱
        cyl = create_cylinder_side_view(
            radius=1.2, height=2.5,
            center=np.array([0, 1.5, 0]),
            color=COLOR_CYLINDER, fill_opacity=0.4
        )
        self.play(Create(cyl), run_time=1.2)
        self.wait(0.5)

        # 问号
        q_mark = cn("?", font_size=72, color=COLOR_HL).move_to(np.array([0, 1.5, 0]))
        self.play(FadeIn(q_mark, scale=0.5), run_time=0.5)
        self.wait(0.8)

        # 提示
        hint = cn("把它变成我们熟悉的形状!", font_size=24, color=GRAY_A).move_to(DOWN * 2)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(hook2), FadeOut(cyl),
            FadeOut(q_mark), FadeOut(hint),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 回顾长方体体积
    # ------------------------------------------------------------------

    def scene_2_review_cuboid(self):
        title = cn("回顾", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        subtitle = cn("长方体的体积", font_size=28, color=WHITE).move_to(UP * 4.8)
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 画长方体 (2D 透视)
        w, h_box, d = 2.5, 1.8, 1.0  # 宽度, 高度, 深度
        cx, cy = 0, 2.0

        # 前面
        front = Rectangle(
            width=w, height=h_box, color=COLOR_RECT,
            fill_opacity=0.3, stroke_width=2.5
        ).move_to([cx, cy, 0])

        # 顶面 (平行四边形)
        top_face = Polygon(
            [cx - w/2, cy + h_box/2, 0],
            [cx - w/2 + d * 0.6, cy + h_box/2 + d * 0.4, 0],
            [cx + w/2 + d * 0.6, cy + h_box/2 + d * 0.4, 0],
            [cx + w/2, cy + h_box/2, 0],
            color=COLOR_RECT, fill_opacity=0.2, stroke_width=2
        )

        # 右面 (平行四边形)
        right_face = Polygon(
            [cx + w/2, cy - h_box/2, 0],
            [cx + w/2 + d * 0.6, cy - h_box/2 + d * 0.4, 0],
            [cx + w/2 + d * 0.6, cy + h_box/2 + d * 0.4, 0],
            [cx + w/2, cy + h_box/2, 0],
            color=COLOR_RECT, fill_opacity=0.15, stroke_width=2
        )

        cuboid = VGroup(front, top_face, right_face)
        self.play(Create(cuboid), run_time=1.0)

        # 标注: 底面积, 高
        area_label = cn("底面积 S", font_size=20, color=COLOR_AREA).move_to([cx, cy - h_box/2 - 0.4, 0])
        h_label = cn("高 h", font_size=20, color=COLOR_HEIGHT).move_to([cx + w/2 + 0.7, cy, 0])

        brace_h = Brace(front, RIGHT, buff=0.1, color=COLOR_HEIGHT)

        self.play(FadeIn(area_label), run_time=0.4)
        self.play(Create(brace_h), FadeIn(h_label), run_time=0.5)

        # 公式
        v_text = cn("V = ", font_size=28, color=WHITE)
        s_text = cn("底面积", font_size=28, color=COLOR_AREA)
        times_text = MathTex(r"\times", font_size=28, color=WHITE)
        h_text = cn("高", font_size=28, color=COLOR_HEIGHT)
        formula_line = VGroup(v_text, s_text, times_text, h_text).arrange(RIGHT, buff=0.15)
        formula_line.move_to(DOWN * 1.0)

        v_eq = VGroup(
            MathTex(r"V", font_size=32, color=WHITE),
            MathTex(r"=", font_size=32, color=WHITE),
            MathTex(r"S", font_size=32, color=COLOR_AREA),
            MathTex(r"\times", font_size=32, color=WHITE),
            MathTex(r"h", font_size=32, color=COLOR_HEIGHT),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 2.2)

        self.play(FadeIn(formula_line, shift=UP * 0.2), run_time=0.6)
        self.play(Write(v_eq), run_time=0.6)
        self.wait(1.0)

        # 关键提示
        key_text = cn("那圆柱呢? 也是 底面积 x 高 吗?", font_size=22, color=COLOR_HL).move_to(DOWN * 4.0)
        self.play(FadeIn(key_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(cuboid),
            FadeOut(area_label), FadeOut(h_label), FadeOut(brace_h),
            FadeOut(formula_line), FadeOut(v_eq), FadeOut(key_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 转化思想引入
    # ------------------------------------------------------------------

    def scene_3_transformation_idea(self):
        title = cn("转化思想", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        idea = cn("把圆柱 变成 长方体!", font_size=28, color=WHITE).move_to(UP * 4.6)
        self.play(FadeIn(idea, shift=UP * 0.2), run_time=0.5)

        # 左: 圆柱
        cyl = create_cylinder_side_view(
            radius=1.0, height=2.0,
            center=np.array([-2.2, 2.0, 0]),
            color=COLOR_CYLINDER, fill_opacity=0.4
        )
        cyl_label = cn("圆柱", font_size=22, color=COLOR_CYLINDER).move_to([-2.2, 0.5, 0])

        # 箭头
        arrow = Arrow(
            start=[-0.8, 2.0, 0], end=[0.8, 2.0, 0],
            color=COLOR_HL, stroke_width=3, buff=0.1
        )
        arrow_text = cn("切割拼合", font_size=18, color=COLOR_HL).next_to(arrow, UP, buff=0.15)

        # 右: 长方体
        rect = Rectangle(
            width=1.8, height=2.0, color=COLOR_RECT,
            fill_opacity=0.4, stroke_width=2.5
        ).move_to([2.2, 2.0, 0])
        rect_label = cn("近似长方体", font_size=22, color=COLOR_RECT).move_to([2.2, 0.5, 0])

        self.play(Create(cyl), FadeIn(cyl_label), run_time=0.8)
        self.play(GrowArrow(arrow), FadeIn(arrow_text), run_time=0.5)
        self.play(Create(rect), FadeIn(rect_label), run_time=0.8)
        self.wait(0.5)

        # 说明文字
        explain = cn(
            "沿着圆柱底面的直径切割",
            font_size=22, color=GRAY_A
        ).move_to(DOWN * 1.5)
        explain2 = cn(
            "再交错拼合",
            font_size=22, color=GRAY_A
        ).move_to(DOWN * 2.2)

        self.play(FadeIn(explain), run_time=0.4)
        self.play(FadeIn(explain2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(idea),
            FadeOut(cyl), FadeOut(cyl_label),
            FadeOut(arrow), FadeOut(arrow_text),
            FadeOut(rect), FadeOut(rect_label),
            FadeOut(explain), FadeOut(explain2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 切割动画 (核心)
    # ------------------------------------------------------------------

    def scene_4_cutting_animation(self):
        title = cn("切割与拼合", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 参数
        circle_radius = 1.3
        cyl_height = 2.0
        circle_center = np.array([0, 3.0, 0])

        # 画底面圆 (俯视)
        top_label = cn("底面 (俯视)", font_size=20, color=GRAY_A).move_to(circle_center + UP * 1.8)
        self.play(FadeIn(top_label), run_time=0.3)

        bottom_circle = Circle(
            radius=circle_radius, color=COLOR_CYLINDER,
            stroke_width=2.5, fill_opacity=0.25
        ).move_to(circle_center)
        self.play(Create(bottom_circle), run_time=0.8)

        # ---- 4等分 ----
        step_label = cn("等分成 4 份", font_size=24, color=WHITE).move_to(UP * 0.5)
        self.play(FadeIn(step_label), run_time=0.4)

        n_pieces = 4
        sectors_4 = self._create_sectors(circle_center, circle_radius, n_pieces)
        cut_lines_4 = self._create_cut_lines(circle_center, circle_radius, n_pieces)

        self.play(Create(cut_lines_4), run_time=0.6)
        self.play(FadeIn(sectors_4), FadeOut(bottom_circle), run_time=0.5)
        self.wait(0.3)

        # 拼合成近似长方体
        rearranged_4 = self._create_rearranged(n_pieces, circle_radius, cyl_height, DOWN * 3.5)
        rearrange_label = cn("交错拼合", font_size=20, color=COLOR_HL).move_to(DOWN * 1.5)

        self.play(FadeIn(rearrange_label), run_time=0.3)
        self.play(
            ReplacementTransform(sectors_4.copy(), rearranged_4),
            run_time=1.2
        )

        note_4 = cn("还不太像长方体...", font_size=20, color=GRAY_A).move_to(DOWN * 5.5)
        self.play(FadeIn(note_4), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(sectors_4), FadeOut(cut_lines_4), FadeOut(rearranged_4),
            FadeOut(note_4), FadeOut(step_label), FadeOut(rearrange_label),
            run_time=0.5
        )

        # ---- 8等分 ----
        step_label_8 = cn("等分成 8 份", font_size=24, color=WHITE).move_to(UP * 0.5)
        self.play(FadeIn(step_label_8), run_time=0.4)

        bottom_circle_2 = Circle(
            radius=circle_radius, color=COLOR_CYLINDER,
            stroke_width=2.5, fill_opacity=0.25
        ).move_to(circle_center)

        n_pieces = 8
        sectors_8 = self._create_sectors(circle_center, circle_radius, n_pieces)
        cut_lines_8 = self._create_cut_lines(circle_center, circle_radius, n_pieces)

        self.play(Create(cut_lines_8), FadeIn(bottom_circle_2), run_time=0.6)
        self.play(FadeIn(sectors_8), FadeOut(bottom_circle_2), run_time=0.5)

        rearranged_8 = self._create_rearranged(n_pieces, circle_radius, cyl_height, DOWN * 3.5)
        rearrange_label_8 = cn("交错拼合", font_size=20, color=COLOR_HL).move_to(DOWN * 1.5)

        self.play(FadeIn(rearrange_label_8), run_time=0.3)
        self.play(
            ReplacementTransform(sectors_8.copy(), rearranged_8),
            run_time=1.2
        )

        note_8 = cn("更像长方体了!", font_size=20, color=COLOR_RESULT).move_to(DOWN * 5.5)
        self.play(FadeIn(note_8), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(sectors_8), FadeOut(cut_lines_8), FadeOut(rearranged_8),
            FadeOut(note_8), FadeOut(step_label_8), FadeOut(rearrange_label_8),
            run_time=0.5
        )

        # ---- 16等分 ----
        step_label_16 = cn("等分成 16 份", font_size=24, color=WHITE).move_to(UP * 0.5)
        self.play(FadeIn(step_label_16), run_time=0.4)

        bottom_circle_3 = Circle(
            radius=circle_radius, color=COLOR_CYLINDER,
            stroke_width=2.5, fill_opacity=0.25
        ).move_to(circle_center)

        n_pieces = 16
        sectors_16 = self._create_sectors(circle_center, circle_radius, n_pieces)
        cut_lines_16 = self._create_cut_lines(circle_center, circle_radius, n_pieces)

        self.play(Create(cut_lines_16), FadeIn(bottom_circle_3), run_time=0.6)
        self.play(FadeIn(sectors_16), FadeOut(bottom_circle_3), run_time=0.5)

        rearranged_16 = self._create_rearranged(n_pieces, circle_radius, cyl_height, DOWN * 3.5)
        rearrange_label_16 = cn("交错拼合", font_size=20, color=COLOR_HL).move_to(DOWN * 1.5)

        self.play(FadeIn(rearrange_label_16), run_time=0.3)
        self.play(
            ReplacementTransform(sectors_16.copy(), rearranged_16),
            run_time=1.2
        )

        note_16 = cn("几乎就是长方体!", font_size=22, color=COLOR_RESULT).move_to(DOWN * 5.5)
        self.play(FadeIn(note_16), run_time=0.4)
        self.wait(0.5)

        # 极限提示
        limit_text = cn(
            "切得越细, 越接近长方体",
            font_size=24, color=COLOR_HL
        ).move_to(DOWN * 6.3)
        self.play(FadeIn(limit_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(top_label),
            FadeOut(sectors_16), FadeOut(cut_lines_16), FadeOut(rearranged_16),
            FadeOut(note_16), FadeOut(step_label_16), FadeOut(rearrange_label_16),
            FadeOut(limit_text),
            run_time=0.6
        )

    def _create_sectors(self, center, radius, n):
        """创建n个扇形(底面俯视)"""
        sectors = VGroup()
        colors = [COLOR_CYLINDER, "#5b9bd5"]  # 交替颜色
        for i in range(n):
            start_angle = i * TAU / n
            angle = TAU / n
            sector = AnnularSector(
                inner_radius=0,
                outer_radius=radius,
                arc_center=center,
                start_angle=start_angle,
                angle=angle,
                color=colors[i % 2],
                fill_opacity=0.5,
                stroke_width=1.5,
                stroke_color=WHITE
            )
            sectors.add(sector)
        return sectors

    def _create_cut_lines(self, center, radius, n):
        """创建切割线"""
        lines = VGroup()
        for i in range(n):
            angle = i * TAU / n
            end_pt = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
            line = Line(center, end_pt, color=WHITE, stroke_width=1.5)
            lines.add(line)
        return lines

    def _create_rearranged(self, n, radius, height, center_pos):
        """
        创建拼合后的近似长方体(侧视图)
        n个扇形柱交错拼合, 总宽 = pi*r (半周长), 高 = 圆柱的高
        """
        half_n = n // 2
        total_width = np.pi * radius  # 半周长
        piece_width = total_width / half_n

        pieces = VGroup()
        colors = [COLOR_CYLINDER, "#5b9bd5"]

        for i in range(n):
            row = i % 2  # 0=上排, 1=下排
            col = i // 2
            piece = Rectangle(
                width=piece_width * 0.95,
                height=height / 2 * 0.95,
                color=colors[row],
                fill_opacity=0.5,
                stroke_width=1,
                stroke_color=WHITE
            )
            x_pos = center_pos[0] - total_width / 2 + piece_width * (col + 0.5)
            if row == 0:
                y_pos = center_pos[1] + height / 4
            else:
                y_pos = center_pos[1] - height / 4
            piece.move_to([x_pos, y_pos, 0])
            pieces.add(piece)

        return pieces

    # ------------------------------------------------------------------
    # Scene 5: 公式推导
    # ------------------------------------------------------------------

    def scene_5_formula_derivation(self):
        title = cn("公式推导", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 左: 圆柱示意
        cyl = create_cylinder_side_view(
            radius=1.0, height=2.2,
            center=np.array([-2.3, 3.0, 0]),
            color=COLOR_CYLINDER, fill_opacity=0.35
        )
        cyl_r_line = Line(
            [-2.3, 3.0 + 1.1, 0], [-2.3 + 1.0, 3.0 + 1.1, 0],
            color=COLOR_RADIUS, stroke_width=2
        )
        cyl_r_label = MathTex(r"r", font_size=24, color=COLOR_RADIUS).next_to(cyl_r_line, UP, buff=0.08)
        cyl_h_line = Line(
            [-2.3 + 1.0 + 0.3, 3.0 - 1.1, 0],
            [-2.3 + 1.0 + 0.3, 3.0 + 1.1, 0],
            color=COLOR_HEIGHT, stroke_width=2
        )
        cyl_h_label = MathTex(r"h", font_size=24, color=COLOR_HEIGHT).next_to(cyl_h_line, RIGHT, buff=0.08)

        self.play(Create(cyl), run_time=0.8)
        self.play(
            Create(cyl_r_line), FadeIn(cyl_r_label),
            Create(cyl_h_line), FadeIn(cyl_h_label),
            run_time=0.6
        )

        # 箭头
        arrow = Arrow(
            [-0.8, 3.0, 0], [0.8, 3.0, 0],
            color=COLOR_HL, stroke_width=3
        )
        self.play(GrowArrow(arrow), run_time=0.4)

        # 右: 长方体示意
        rect_w = np.pi * 1.0  # pi*r
        rect_h_val = 2.2
        rect = Rectangle(
            width=rect_w, height=rect_h_val,
            color=COLOR_RECT, fill_opacity=0.35, stroke_width=2.5
        ).move_to([2.3, 3.0, 0])

        self.play(Create(rect), run_time=0.8)

        # 标注长方体的长和宽
        # 长 = pi*r (半周长)
        brace_top = Brace(rect, UP, buff=0.1, color=COLOR_RADIUS)
        top_label_group = VGroup(
            MathTex(r"\pi r", font_size=22, color=COLOR_RADIUS),
        )
        top_label_group.next_to(brace_top, UP, buff=0.08)

        # 高 = h
        brace_right = Brace(rect, RIGHT, buff=0.1, color=COLOR_HEIGHT)
        right_label = MathTex(r"h", font_size=22, color=COLOR_HEIGHT).next_to(brace_right, RIGHT, buff=0.08)

        self.play(
            Create(brace_top), FadeIn(top_label_group),
            Create(brace_right), FadeIn(right_label),
            run_time=0.6
        )
        self.wait(0.5)

        # 对应关系
        relation_y = 0.8
        rel1 = VGroup(
            cn("长方体的长", font_size=20, color=COLOR_RECT),
            cn(" = ", font_size=20, color=WHITE),
            cn("圆柱底面半周长", font_size=20, color=COLOR_CYLINDER),
            cn(" = ", font_size=20, color=WHITE),
            MathTex(r"\pi r", font_size=22, color=COLOR_RADIUS),
        ).arrange(RIGHT, buff=0.1).move_to([0, relation_y, 0])

        rel2 = VGroup(
            cn("长方体的宽", font_size=20, color=COLOR_RECT),
            cn(" = ", font_size=20, color=WHITE),
            cn("圆柱的高", font_size=20, color=COLOR_CYLINDER),
            cn(" = ", font_size=20, color=WHITE),
            MathTex(r"h", font_size=22, color=COLOR_HEIGHT),
        ).arrange(RIGHT, buff=0.1).move_to([0, relation_y - 0.7, 0])

        self.play(FadeIn(rel1, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(rel2, shift=UP * 0.15), run_time=0.5)
        self.wait(0.8)

        # 推导公式
        derivation_y = -1.5

        step1_label = cn("长方体体积:", font_size=22, color=COLOR_RECT)
        step1_eq = MathTex(
            r"V", r"=", r"\pi r", r"\times", r"h",
            font_size=30
        )
        step1_eq.set_color_by_tex(r"\pi r", COLOR_RADIUS)
        step1_eq.set_color_by_tex("h", COLOR_HEIGHT)
        step1 = VGroup(step1_label, step1_eq).arrange(RIGHT, buff=0.2).move_to([0, derivation_y, 0])
        self.play(FadeIn(step1, shift=UP * 0.15), run_time=0.6)

        # 即圆柱体积
        step2_label = cn("即圆柱体积:", font_size=22, color=COLOR_CYLINDER)
        step2_eq = MathTex(
            r"V", r"=", r"\pi", r"r^2", r"h",
            font_size=34
        )
        step2_eq[2].set_color(COLOR_RADIUS)
        step2_eq[3].set_color(COLOR_RADIUS)
        step2_eq[4].set_color(COLOR_HEIGHT)
        step2 = VGroup(step2_label, step2_eq).arrange(RIGHT, buff=0.2).move_to([0, derivation_y - 1.0, 0])
        self.play(FadeIn(step2, shift=UP * 0.15), run_time=0.6)

        self.wait(0.5)

        # 最终公式框
        final_box_y = derivation_y - 2.5

        formula_final = MathTex(
            r"V", r"=", r"S", r"\times", r"h",
            r"=", r"\pi", r"r^2", r"h",
            font_size=36
        )
        formula_final[2].set_color(COLOR_AREA)
        formula_final[4].set_color(COLOR_HEIGHT)
        formula_final[6].set_color(COLOR_RADIUS)
        formula_final[7].set_color(COLOR_RADIUS)
        formula_final[8].set_color(COLOR_HEIGHT)
        formula_final.move_to([0, final_box_y, 0])

        box = SurroundingRectangle(
            formula_final, color=COLOR_HL,
            buff=0.25, corner_radius=0.1
        )

        note_s = VGroup(
            cn("S = ", font_size=20, color=COLOR_AREA),
            cn("底面积", font_size=20, color=COLOR_AREA),
        ).arrange(RIGHT, buff=0.05).move_to([0, final_box_y - 0.8, 0])

        self.play(Write(formula_final), run_time=0.8)
        self.play(Create(box), run_time=0.4)
        self.play(FadeIn(note_s), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(cyl), FadeOut(cyl_r_line), FadeOut(cyl_r_label),
            FadeOut(cyl_h_line), FadeOut(cyl_h_label), FadeOut(arrow),
            FadeOut(rect), FadeOut(brace_top), FadeOut(top_label_group),
            FadeOut(brace_right), FadeOut(right_label),
            FadeOut(rel1), FadeOut(rel2),
            FadeOut(step1), FadeOut(step2),
            FadeOut(formula_final), FadeOut(box), FadeOut(note_s),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题
    # ------------------------------------------------------------------

    def scene_6_example(self):
        title = cn("例题", font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 题目
        q1 = cn("一个圆柱形水桶,", font_size=24, color=WHITE).move_to(UP * 4.5)
        q2 = cn("底面半径 5 cm, 高 12 cm", font_size=24, color=WHITE).move_to(UP * 3.9)
        q3 = cn("求它的体积。", font_size=24, color=COLOR_HL).move_to(UP * 3.3)

        self.play(FadeIn(q1), run_time=0.4)
        self.play(FadeIn(q2), run_time=0.4)
        self.play(FadeIn(q3), run_time=0.4)

        # 圆柱示意图 (小)
        cyl = create_cylinder_side_view(
            radius=0.8, height=1.8,
            center=np.array([0, 1.5, 0]),
            color=COLOR_CYLINDER, fill_opacity=0.3
        )
        r_line = Line([0, 1.5 + 0.9, 0], [0.8, 1.5 + 0.9, 0], color=COLOR_RADIUS, stroke_width=2)
        r_label = cn("r=5", font_size=18, color=COLOR_RADIUS).next_to(r_line, UP, buff=0.05)
        h_brace = Brace(
            Line([0.8 + 0.2, 1.5 - 0.9, 0], [0.8 + 0.2, 1.5 + 0.9, 0]),
            RIGHT, buff=0.1, color=COLOR_HEIGHT
        )
        h_label = cn("h=12", font_size=18, color=COLOR_HEIGHT).next_to(h_brace, RIGHT, buff=0.05)

        self.play(Create(cyl), run_time=0.6)
        self.play(
            Create(r_line), FadeIn(r_label),
            Create(h_brace), FadeIn(h_label),
            run_time=0.5
        )
        self.wait(0.5)

        # 解题步骤
        sol_y = -0.8

        sol_title = cn("解:", font_size=26, color=COLOR_RESULT).move_to([-3.5, sol_y, 0])
        self.play(FadeIn(sol_title), run_time=0.3)

        # Step 1: 写出公式
        s1 = MathTex(
            r"V", r"=", r"\pi", r"r^2", r"h",
            font_size=30
        ).move_to([0, sol_y - 0.7, 0])
        s1[2].set_color(COLOR_RADIUS)
        s1[3].set_color(COLOR_RADIUS)
        s1[4].set_color(COLOR_HEIGHT)

        self.play(Write(s1), run_time=0.6)
        self.wait(0.3)

        # Step 2: 代入数值
        s2 = MathTex(
            r"=", r"\pi", r"\times", r"5^2", r"\times", r"12",
            font_size=30
        ).move_to([0, sol_y - 1.5, 0])
        s2[1].set_color(COLOR_RADIUS)
        s2[3].set_color(COLOR_RADIUS)
        s2[5].set_color(COLOR_HEIGHT)

        self.play(Write(s2), run_time=0.6)
        self.wait(0.3)

        # Step 3: 计算
        s3 = MathTex(
            r"=", r"\pi", r"\times", r"25", r"\times", r"12",
            font_size=30
        ).move_to([0, sol_y - 2.3, 0])

        self.play(Write(s3), run_time=0.5)

        # Step 4: 结果
        s4 = MathTex(
            r"=", r"300\pi",
            font_size=32
        ).move_to([0, sol_y - 3.1, 0])
        s4[1].set_color(COLOR_RESULT)

        self.play(Write(s4), run_time=0.5)

        # 近似值
        approx = MathTex(
            r"\approx", r"942", font_size=30
        ).next_to(s4, RIGHT, buff=0.3)
        unit = cn(" cm", font_size=22, color=WHITE)
        sup = MathTex(r"^3", font_size=22, color=WHITE)
        unit_group = VGroup(unit, sup).arrange(RIGHT, buff=0.02).next_to(approx, RIGHT, buff=0.1)

        self.play(Write(approx), FadeIn(unit_group), run_time=0.5)

        # 结果框
        result_text = VGroup(
            MathTex(r"V = 300\pi \approx 942", font_size=28, color=COLOR_RESULT),
            cn(" cm", font_size=20, color=COLOR_RESULT),
            MathTex(r"^3", font_size=20, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.05).move_to([0, sol_y - 4.3, 0])

        result_box = SurroundingRectangle(result_text, color=COLOR_RESULT, buff=0.2, corner_radius=0.08)
        self.play(Create(result_box), FadeIn(result_text), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(q1), FadeOut(q2), FadeOut(q3),
            FadeOut(cyl), FadeOut(r_line), FadeOut(r_label),
            FadeOut(h_brace), FadeOut(h_label),
            FadeOut(sol_title), FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4),
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
        point1_title = cn("核心思想", font_size=26, color=COLOR_ACCENT).move_to(UP * 4.3)
        point1_body = cn("转化: 圆柱 -> 近似长方体", font_size=22, color=WHITE).move_to(UP * 3.6)
        self.play(FadeIn(point1_title), run_time=0.3)
        self.play(FadeIn(point1_body, shift=UP * 0.15), run_time=0.4)

        # 要点2
        point2_title = cn("极限思想", font_size=26, color=COLOR_ACCENT).move_to(UP * 2.6)
        point2_body = cn("切得越细, 越接近长方体", font_size=22, color=WHITE).move_to(UP * 1.9)
        self.play(FadeIn(point2_title), run_time=0.3)
        self.play(FadeIn(point2_body, shift=UP * 0.15), run_time=0.4)

        # 公式
        formula_title = cn("体积公式", font_size=26, color=COLOR_ACCENT).move_to(UP * 0.9)
        self.play(FadeIn(formula_title), run_time=0.3)

        formula = MathTex(
            r"V", r"=", r"S", r"h", r"=", r"\pi", r"r^2", r"h",
            font_size=40
        ).move_to(DOWN * 0.1)
        formula[2].set_color(COLOR_AREA)
        formula[3].set_color(COLOR_HEIGHT)
        formula[5].set_color(COLOR_RADIUS)
        formula[6].set_color(COLOR_RADIUS)
        formula[7].set_color(COLOR_HEIGHT)

        box = SurroundingRectangle(formula, color=COLOR_HL, buff=0.3, corner_radius=0.12)

        self.play(Write(formula), run_time=0.8)
        self.play(Create(box), run_time=0.4)

        # 对应关系
        legend = VGroup(
            VGroup(
                cn("S", font_size=20, color=COLOR_AREA),
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
        app_text = cn("用于计算: 水桶容积、柱子体积、管道容量...",
                       font_size=20, color=GRAY_A).move_to(DOWN * 3.5)
        self.play(FadeIn(app_text), run_time=0.5)

        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(point1_title), FadeOut(point1_body),
            FadeOut(point2_title), FadeOut(point2_body),
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

        follow_text = cn("关注我, 学更多数学技巧!", font_size=28, color=COLOR_HL).move_to(DOWN * 0.8)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 装饰小圆柱
        mini_cyls = VGroup()
        for i in range(5):
            angle = i * TAU / 5
            pos = DOWN * 2.5 + np.array([np.cos(angle) * 2, np.sin(angle) * 0.8, 0])
            mini = create_cylinder_side_view(
                radius=0.25, height=0.5,
                center=pos,
                color=COLOR_CYLINDER, fill_opacity=0.5
            )
            mini_cyls.add(mini)

        self.play(*[FadeIn(mc, scale=0.5) for mc in mini_cyls], run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(author_name), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(mini_cyls),
            run_time=1.0
        )


# 运行命令:
# manim -pql 003_圆柱的体积.py CylinderVolumeLesson  # 快速预览
# manim -qm 003_圆柱的体积.py CylinderVolumeLesson   # 中等质量
# manim -qh 003_圆柱的体积.py CylinderVolumeLesson    # 高质量

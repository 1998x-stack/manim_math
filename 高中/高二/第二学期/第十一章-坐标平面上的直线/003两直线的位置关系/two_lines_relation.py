"""
两直线的位置关系 - Manim 教学动画
年级: 高二第二学期
章节: 坐标平面上的直线
知识点: 两直线的位置关系（平行、相交、重合）

输出格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

运行命令:
    manim -pql two_lines_relation.py TwoLinesRelation   # 快速预览
    manim -qh  two_lines_relation.py TwoLinesRelation   # 高质量
"""

from manim import *
import numpy as np


# ==============================================================
# 全局配置 - TikTok竖屏
# ==============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ==============================================================
# 颜色常量
# ==============================================================
BG_COLOR = "#1a1a2e"
COLOR_L1 = "#e74c3c"        # 红色 - 直线l₁
COLOR_L2 = "#3498db"        # 蓝色 - 直线l₂
COLOR_PARALLEL = "#f39c12"  # 橙色 - 平行标注
COLOR_INTERSECT = "#2ecc71" # 绿色 - 交点
COLOR_COINCIDE = "#9b59b6"  # 紫色 - 重合
COLOR_AXES = GRAY_B
COLOR_HIGHLIGHT = YELLOW
COLOR_CARD_BG = "#16213e"
FONT = "Noto Sans CJK SC"


# ==============================================================
# 主场景
# ==============================================================
class TwoLinesRelation(Scene):
    """
    两直线位置关系教学动画
    场景顺序：开场 → 平行 → 重合 → 相交 → 总结 → 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 初始化所有几何数据
        self.setup_geometry()

        # 执行各场景
        self.scene_opening()
        self.scene_parallel()
        self.scene_coincident()
        self.scene_intersect()
        self.scene_summary()
        self.scene_outro()

    # ----------------------------------------------------------
    # 几何数据初始化
    # ----------------------------------------------------------
    def setup_geometry(self):
        """统一初始化所有几何数据，后续场景只引用不重复计算"""

        # ---- 坐标轴参数 ----
        self.AXES_CENTER = np.array([0.0, 1.5, 0.0])
        self.AXES_X_RANGE = (-3, 3, 1)
        self.AXES_Y_RANGE = (-2, 4, 1)
        self.AXES_X_LENGTH = 6.0
        self.AXES_Y_LENGTH = 5.0

        # ---- 直线参数 ----
        # 平行案例: l1: y=x+2, l2: y=x-1
        self.k_par = 1.0
        self.b1_par = 2.0
        self.b2_par = -1.0

        # 重合案例: l1=l2: y=x+1
        self.k_coin = 1.0
        self.b_coin = 1.0

        # 相交案例: l1: y=x+1, l2: y=-x+3
        self.k1_int = 1.0
        self.b1_int = 1.0
        self.k2_int = -1.0
        self.b2_int = 3.0

        # 精确计算交点
        # k1*x + b1 = k2*x + b2 → x = (b2-b1)/(k1-k2)
        det = self.k1_int - self.k2_int  # = 1 - (-1) = 2
        self.ix = (self.b2_int - self.b1_int) / det  # = (3-1)/2 = 1.0
        self.iy = self.k1_int * self.ix + self.b1_int  # = 1*1+1 = 2.0

        # 验证
        assert abs(self.ix - 1.0) < 1e-10, "交点x计算错误"
        assert abs(self.iy - 2.0) < 1e-10, "交点y计算错误"

        # 验证交点在两条线上
        y_on_l1 = self.k1_int * self.ix + self.b1_int
        y_on_l2 = self.k2_int * self.ix + self.b2_int
        assert abs(y_on_l1 - self.iy) < 1e-10, "交点不在l1上"
        assert abs(y_on_l2 - self.iy) < 1e-10, "交点不在l2上"

        print(f"✓ 几何验证通过：交点=({self.ix}, {self.iy})")

    def make_axes(self):
        """创建并定位坐标轴"""
        axes = Axes(
            x_range=list(self.AXES_X_RANGE),
            y_range=list(self.AXES_Y_RANGE),
            x_length=self.AXES_X_LENGTH,
            y_length=self.AXES_Y_LENGTH,
            axis_config={
                "color": COLOR_AXES,
                "include_numbers": True,
                "font_size": 20,
                "numbers_to_include": [-2, -1, 1, 2, 3],
                "include_ticks": True,
                "tick_size": 0.08,
            },
        ).move_to(self.AXES_CENTER)
        return axes

    def get_line_on_axes(self, axes, k, b, color, x_min=-3, x_max=3, stroke_width=3):
        """
        在坐标系上创建直线 y = kx + b，自动裁剪到坐标范围内。
        Returns: Line Mobject
        """
        y_min = self.AXES_Y_RANGE[0]
        y_max = self.AXES_Y_RANGE[1]

        # 计算裁剪后的端点
        candidates = []

        # 左右边界
        for x_val in [x_min, x_max]:
            y_val = k * x_val + b
            if y_min <= y_val <= y_max:
                candidates.append((x_val, y_val))

        # 上下边界
        if abs(k) > 1e-10:
            for y_val in [y_min, y_max]:
                x_val = (y_val - b) / k
                if x_min <= x_val <= x_max:
                    candidates.append((x_val, y_val))

        # 去重
        unique = []
        for c in candidates:
            is_dup = any(abs(c[0]-u[0]) < 1e-8 and abs(c[1]-u[1]) < 1e-8 for u in unique)
            if not is_dup:
                unique.append(c)

        if len(unique) < 2:
            # fallback: 使用x边界
            unique = [(x_min, k * x_min + b), (x_max, k * x_max + b)]

        p1 = axes.c2p(unique[0][0], unique[0][1])
        p2 = axes.c2p(unique[1][0], unique[1][1])
        return Line(p1, p2, color=color, stroke_width=stroke_width)

    # ----------------------------------------------------------
    # Scene 1: 开场钩子
    # ----------------------------------------------------------
    def scene_opening(self):
        """开场：引出问题，展示三种情况"""

        # 作者信息（始终存在）
        self.author_banner = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_banner, shift=DOWN * 0.2), run_time=0.4)

        # 主标题
        title = Text(
            "两直线的位置关系",
            font=FONT, font_size=44, color=GOLD
        ).move_to(UP * 5.8)

        subtitle = Text(
            "平面内两直线，共有几种关系？",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.8)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 三种情况预览 - 小图示
        preview_scale = 0.7
        preview_y = 2.0

        # 平行线小图
        par_group = VGroup(
            Line(LEFT * 1.2 + UP * 0.3, RIGHT * 1.2 + UP * 0.3, color=COLOR_L1, stroke_width=2.5),
            Line(LEFT * 1.2 + DOWN * 0.3, RIGHT * 1.2 + DOWN * 0.3, color=COLOR_L2, stroke_width=2.5),
        ).scale(preview_scale).move_to(LEFT * 2.8 + UP * preview_y)
        par_label = Text("平行", font=FONT, font_size=22, color=COLOR_PARALLEL).next_to(par_group, DOWN, buff=0.2)

        # 相交线小图
        int_group = VGroup(
            Line(LEFT * 0.9 + DOWN * 0.9, RIGHT * 0.9 + UP * 0.9, color=COLOR_L1, stroke_width=2.5),
            Line(LEFT * 0.9 + UP * 0.9, RIGHT * 0.9 + DOWN * 0.9, color=COLOR_L2, stroke_width=2.5),
        ).scale(preview_scale).move_to(UP * preview_y)
        int_label = Text("相交", font=FONT, font_size=22, color=COLOR_INTERSECT).next_to(int_group, DOWN, buff=0.2)

        # 重合线小图（两线叠加）
        coin_group = VGroup(
            Line(LEFT * 1.2, RIGHT * 1.2, color=COLOR_L1, stroke_width=4),
            Line(LEFT * 1.2, RIGHT * 1.2, color=COLOR_L2, stroke_width=2.5, stroke_opacity=0.7),
        ).scale(preview_scale).move_to(RIGHT * 2.8 + UP * preview_y)
        coin_label = Text("重合", font=FONT, font_size=22, color=COLOR_COINCIDE).next_to(coin_group, DOWN, buff=0.2)

        # 依次展示三种情况
        for group, label in [(par_group, par_label), (int_group, int_label), (coin_group, coin_label)]:
            self.play(Create(group), run_time=0.5)
            self.play(FadeIn(label), run_time=0.3)

        self.wait(0.8)

        # 清理，进入正题
        self.play(
            FadeOut(subtitle),
            FadeOut(par_group), FadeOut(par_label),
            FadeOut(int_group), FadeOut(int_label),
            FadeOut(coin_group), FadeOut(coin_label),
            run_time=0.5,
        )

        # 标题变小上移
        title_small = Text(
            "两直线的位置关系",
            font=FONT, font_size=32, color=GOLD
        ).move_to(UP * 6.3)
        self.play(Transform(title, title_small), run_time=0.5)
        self.title_obj = title

    # ----------------------------------------------------------
    # Scene 2: 平行
    # ----------------------------------------------------------
    def scene_parallel(self):
        """展示平行情况：k₁=k₂, b₁≠b₂"""

        # 场景标题
        scene_title = Text(
            "① 平行", font=FONT, font_size=36, color=COLOR_PARALLEL
        ).move_to(UP * 5.5)
        self.play(Write(scene_title), run_time=0.6)

        # 建立坐标系
        axes = self.make_axes()
        axes_label_x = Text("x", font=FONT, font_size=22, color=COLOR_AXES).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.15
        )
        axes_label_y = Text("y", font=FONT, font_size=22, color=COLOR_AXES).next_to(
            axes.y_axis.get_top(), UP, buff=0.15
        )

        self.play(Create(axes), FadeIn(axes_label_x), FadeIn(axes_label_y), run_time=1.0)

        # 绘制两条平行线
        # l1: y = x + 2（红色）
        line1 = self.get_line_on_axes(axes, self.k_par, self.b1_par, COLOR_L1)
        # l2: y = x - 1（蓝色）
        line2 = self.get_line_on_axes(axes, self.k_par, self.b2_par, COLOR_L2)

        self.play(Create(line1), run_time=0.8)

        # l1 标签
        label1_pos = axes.c2p(-0.5, self.k_par * (-0.5) + self.b1_par)
        l1_formula = MathTex(r"l_1: y = x + 2", font_size=26, color=COLOR_L1).next_to(
            label1_pos, UL, buff=0.15
        )
        self.play(Write(l1_formula), run_time=0.5)

        self.play(Create(line2), run_time=0.8)

        # l2 标签
        label2_pos = axes.c2p(1.5, self.k_par * 1.5 + self.b2_par)
        l2_formula = MathTex(r"l_2: y = x - 1", font_size=26, color=COLOR_L2).next_to(
            label2_pos, DR, buff=0.15
        )
        self.play(Write(l2_formula), run_time=0.5)

        # 用平行箭头标注方向相同
        arrow1 = Arrow(
            axes.c2p(0.0, self.k_par * 0.0 + self.b1_par),
            axes.c2p(0.8, self.k_par * 0.8 + self.b1_par),
            buff=0, color=COLOR_PARALLEL, max_tip_length_to_length_ratio=0.3, stroke_width=3
        )
        arrow2 = Arrow(
            axes.c2p(0.0, self.k_par * 0.0 + self.b2_par),
            axes.c2p(0.8, self.k_par * 0.8 + self.b2_par),
            buff=0, color=COLOR_PARALLEL, max_tip_length_to_length_ratio=0.3, stroke_width=3
        )

        self.play(FadeIn(arrow1), FadeIn(arrow2), run_time=0.5)

        # 说明文字
        explain1 = Text(
            "斜率相同 → 方向相同",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)

        self.wait(0.8)

        # 核心条件公式
        cond_title = Text(
            "平行条件：", font=FONT, font_size=28, color=COLOR_PARALLEL
        ).move_to(DOWN * 4.7 + LEFT * 1.8)
        cond_formula = MathTex(
            r"k_1 = k_2 \quad \text{and} \quad b_1 \neq b_2",
            font_size=28, color=WHITE
        ).next_to(cond_title, RIGHT, buff=0.2)

        # 注：Manim MathTex 的 \text{} 中用英文，中文用 Text 拼接
        cond_group = VGroup(
            MathTex(r"k_1 = k_2", font_size=32, color=YELLOW),
            Text("且", font=FONT, font_size=28, color=WHITE),
            MathTex(r"b_1 \neq b_2", font_size=32, color=YELLOW),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 4.7)

        cond_box = SurroundingRectangle(
            cond_group, corner_radius=0.15, color=COLOR_PARALLEL, buff=0.2
        )

        self.play(FadeIn(cond_group), Create(cond_box), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(axes), FadeOut(axes_label_x), FadeOut(axes_label_y),
            FadeOut(line1), FadeOut(line2),
            FadeOut(l1_formula), FadeOut(l2_formula),
            FadeOut(arrow1), FadeOut(arrow2),
            FadeOut(explain1),
            FadeOut(cond_group), FadeOut(cond_box),
            run_time=0.6,
        )

    # ----------------------------------------------------------
    # Scene 3: 重合
    # ----------------------------------------------------------
    def scene_coincident(self):
        """展示重合情况：k₁=k₂, b₁=b₂"""

        # 场景标题
        scene_title = Text(
            "② 重合", font=FONT, font_size=36, color=COLOR_COINCIDE
        ).move_to(UP * 5.5)
        self.play(Write(scene_title), run_time=0.6)

        # 坐标系
        axes = self.make_axes()
        axes_label_x = Text("x", font=FONT, font_size=22, color=COLOR_AXES).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.15
        )
        axes_label_y = Text("y", font=FONT, font_size=22, color=COLOR_AXES).next_to(
            axes.y_axis.get_top(), UP, buff=0.15
        )

        self.play(Create(axes), FadeIn(axes_label_x), FadeIn(axes_label_y), run_time=1.0)

        # 先绘制l1
        line1 = self.get_line_on_axes(axes, self.k_coin, self.b_coin, COLOR_L1, stroke_width=4)
        self.play(Create(line1), run_time=0.8)

        label1_pos = axes.c2p(-1.5, self.k_coin * (-1.5) + self.b_coin)
        l1_formula = MathTex(r"l_1: y = x + 1", font_size=26, color=COLOR_L1).next_to(
            label1_pos, UL, buff=0.1
        )
        self.play(Write(l1_formula), run_time=0.5)

        # 再绘制l2（同一条线，蓝色叠加）
        line2 = self.get_line_on_axes(axes, self.k_coin, self.b_coin, COLOR_L2, stroke_width=2.5)
        line2.set_stroke(opacity=0.8)
        self.play(Create(line2), run_time=0.8)

        label2_pos = axes.c2p(1.0, self.k_coin * 1.0 + self.b_coin)
        l2_formula = MathTex(r"l_2: y = x + 1", font_size=26, color=COLOR_L2).next_to(
            label2_pos, DR, buff=0.15
        )
        self.play(Write(l2_formula), run_time=0.5)

        # 高亮闪烁效果表示完全重合
        self.play(
            line1.animate.set_stroke(width=6),
            line2.animate.set_stroke(width=3, opacity=1.0),
            run_time=0.4
        )

        # 说明文字
        explain1 = Text(
            "方程完全相同 → 完全重合！",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)

        self.wait(0.7)

        # 核心条件
        cond_group = VGroup(
            MathTex(r"k_1 = k_2", font_size=32, color=YELLOW),
            Text("且", font=FONT, font_size=28, color=WHITE),
            MathTex(r"b_1 = b_2", font_size=32, color=YELLOW),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 4.7)

        cond_box = SurroundingRectangle(
            cond_group, corner_radius=0.15, color=COLOR_COINCIDE, buff=0.2
        )

        self.play(FadeIn(cond_group), Create(cond_box), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(axes), FadeOut(axes_label_x), FadeOut(axes_label_y),
            FadeOut(line1), FadeOut(line2),
            FadeOut(l1_formula), FadeOut(l2_formula),
            FadeOut(explain1),
            FadeOut(cond_group), FadeOut(cond_box),
            run_time=0.6,
        )

    # ----------------------------------------------------------
    # Scene 4: 相交
    # ----------------------------------------------------------
    def scene_intersect(self):
        """展示相交情况：k₁≠k₂，计算交点"""

        # 场景标题
        scene_title = Text(
            "③ 相交", font=FONT, font_size=36, color=COLOR_INTERSECT
        ).move_to(UP * 5.5)
        self.play(Write(scene_title), run_time=0.6)

        # 坐标系
        axes = self.make_axes()
        axes_label_x = Text("x", font=FONT, font_size=22, color=COLOR_AXES).next_to(
            axes.x_axis.get_right(), RIGHT, buff=0.15
        )
        axes_label_y = Text("y", font=FONT, font_size=22, color=COLOR_AXES).next_to(
            axes.y_axis.get_top(), UP, buff=0.15
        )

        self.play(Create(axes), FadeIn(axes_label_x), FadeIn(axes_label_y), run_time=1.0)

        # l1: y = x + 1（红）
        line1 = self.get_line_on_axes(axes, self.k1_int, self.b1_int, COLOR_L1)
        self.play(Create(line1), run_time=0.8)
        label1_pos = axes.c2p(-2.0, self.k1_int * (-2.0) + self.b1_int)
        l1_formula = MathTex(r"l_1: y = x + 1", font_size=26, color=COLOR_L1).next_to(
            label1_pos, LEFT, buff=0.1
        )
        self.play(Write(l1_formula), run_time=0.5)

        # l2: y = -x + 3（蓝）
        line2 = self.get_line_on_axes(axes, self.k2_int, self.b2_int, COLOR_L2)
        self.play(Create(line2), run_time=0.8)
        label2_pos = axes.c2p(2.5, self.k2_int * 2.5 + self.b2_int)
        l2_formula = MathTex(r"l_2: y = -x + 3", font_size=26, color=COLOR_L2).next_to(
            label2_pos, RIGHT, buff=0.1
        )
        self.play(Write(l2_formula), run_time=0.5)

        # 说明斜率不同
        explain1 = Text(
            "斜率不同 → 方向不同 → 必然相交",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 高亮交点
        # 交点精确坐标: (1, 2)
        intersection_scene = axes.c2p(self.ix, self.iy)
        intersection_dot = Dot(
            intersection_scene, radius=0.14,
            color=COLOR_INTERSECT, fill_opacity=1.0
        )
        intersection_ring = Circle(
            radius=0.25, color=COLOR_HIGHLIGHT, stroke_width=2
        ).move_to(intersection_scene)

        self.play(
            FadeIn(intersection_dot, scale=0.3),
            run_time=0.5
        )
        self.play(Flash(intersection_dot, color=COLOR_INTERSECT, flash_radius=0.4), run_time=0.4)
        self.play(Create(intersection_ring), run_time=0.4)

        # 交点坐标标注
        dot_label = MathTex(
            r"(1,\ 2)", font_size=28, color=COLOR_INTERSECT
        ).next_to(intersection_dot, UR, buff=0.2)
        self.play(Write(dot_label), run_time=0.5)

        self.play(FadeOut(explain1), run_time=0.3)

        # 展示联立方程组求解过程
        eq_title = Text(
            "如何求交点？联立方程组：",
            font=FONT, font_size=24, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(eq_title, shift=UP * 0.2), run_time=0.5)

        eq_system = MathTex(
            r"\begin{cases} y = x + 1 \\ y = -x + 3 \end{cases}",
            font_size=32, color=WHITE
        ).move_to(DOWN * 4.5)
        self.play(Write(eq_system), run_time=0.8)

        self.wait(0.7)

        # 求解过程
        solve_step = MathTex(
            r"x + 1 = -x + 3 \Rightarrow x = 1",
            font_size=28, color=YELLOW
        ).move_to(DOWN * 5.8)
        self.play(Write(solve_step), run_time=0.8)
        self.wait(0.5)

        solve_result = MathTex(
            r"\therefore\ x = 1,\quad y = 2",
            font_size=30, color=COLOR_INTERSECT
        ).move_to(DOWN * 6.8)
        self.play(Write(solve_result), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(axes), FadeOut(axes_label_x), FadeOut(axes_label_y),
            FadeOut(line1), FadeOut(line2),
            FadeOut(l1_formula), FadeOut(l2_formula),
            FadeOut(intersection_dot), FadeOut(intersection_ring), FadeOut(dot_label),
            FadeOut(eq_title), FadeOut(eq_system),
            FadeOut(solve_step), FadeOut(solve_result),
            run_time=0.6,
        )

    # ----------------------------------------------------------
    # Scene 5: 总结
    # ----------------------------------------------------------
    def scene_summary(self):
        """三种关系汇总展示"""

        summary_title = Text(
            "三种位置关系总结",
            font=FONT, font_size=38, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.7)

        # 通用直线方程说明
        general_eq = VGroup(
            MathTex(r"l_1: y = k_1 x + b_1", font_size=28, color=COLOR_L1),
            MathTex(r"l_2: y = k_2 x + b_2", font_size=28, color=COLOR_L2),
        ).arrange(DOWN, buff=0.3).move_to(UP * 4.3)
        self.play(Write(general_eq), run_time=0.7)

        self.wait(0.3)

        # ---- 卡片1: 平行 ----
        card1_bg = RoundedRectangle(
            width=7.5, height=1.7, corner_radius=0.2,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_PARALLEL, stroke_width=2
        ).move_to(UP * 2.2)
        card1_icon = Text("平行", font=FONT, font_size=28, color=COLOR_PARALLEL).move_to(
            card1_bg.get_center() + LEFT * 2.8
        )
        card1_cond = VGroup(
            MathTex(r"k_1 = k_2", font_size=26, color=YELLOW),
            Text("且", font=FONT, font_size=24, color=WHITE),
            MathTex(r"b_1 \neq b_2", font_size=26, color=YELLOW),
        ).arrange(RIGHT, buff=0.2).move_to(card1_bg.get_center() + RIGHT * 0.5)

        card1 = VGroup(card1_bg, card1_icon, card1_cond)
        card1.shift(LEFT * 12)

        # ---- 卡片2: 重合 ----
        card2_bg = RoundedRectangle(
            width=7.5, height=1.7, corner_radius=0.2,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_COINCIDE, stroke_width=2
        ).move_to(UP * 0.2)
        card2_icon = Text("重合", font=FONT, font_size=28, color=COLOR_COINCIDE).move_to(
            card2_bg.get_center() + LEFT * 2.8
        )
        card2_cond = VGroup(
            MathTex(r"k_1 = k_2", font_size=26, color=YELLOW),
            Text("且", font=FONT, font_size=24, color=WHITE),
            MathTex(r"b_1 = b_2", font_size=26, color=YELLOW),
        ).arrange(RIGHT, buff=0.2).move_to(card2_bg.get_center() + RIGHT * 0.5)

        card2 = VGroup(card2_bg, card2_icon, card2_cond)
        card2.shift(LEFT * 12)

        # ---- 卡片3: 相交 ----
        card3_bg = RoundedRectangle(
            width=7.5, height=1.7, corner_radius=0.2,
            fill_color=COLOR_CARD_BG, fill_opacity=1,
            stroke_color=COLOR_INTERSECT, stroke_width=2
        ).move_to(DOWN * 1.8)
        card3_icon = Text("相交", font=FONT, font_size=28, color=COLOR_INTERSECT).move_to(
            card3_bg.get_center() + LEFT * 2.8
        )
        card3_cond = MathTex(
            r"k_1 \neq k_2", font_size=26, color=YELLOW
        ).move_to(card3_bg.get_center() + RIGHT * 0.5)

        card3 = VGroup(card3_bg, card3_icon, card3_cond)
        card3.shift(LEFT * 12)

        # 卡片依次飞入
        self.add(card1)
        self.play(card1.animate.shift(RIGHT * 12), run_time=0.6)

        self.add(card2)
        self.play(card2.animate.shift(RIGHT * 12), run_time=0.6)

        self.add(card3)
        self.play(card3.animate.shift(RIGHT * 12), run_time=0.6)

        self.wait(1.0)

        # 一般式补充
        general_note_title = Text(
            "一般式时的平行判断：",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.5)
        general_note_formula = MathTex(
            r"\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2}",
            font_size=28, color=GRAY_A
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(general_note_title), FadeIn(general_note_formula), run_time=0.7)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(general_eq),
            FadeOut(card1), FadeOut(card2), FadeOut(card3),
            FadeOut(general_note_title), FadeOut(general_note_formula),
            run_time=0.7,
        )

    # ----------------------------------------------------------
    # Scene 6: 片尾
    # ----------------------------------------------------------
    def scene_outro(self):
        """片尾：作者信息 + 关注提示"""

        # 标题淡出
        self.play(FadeOut(self.title_obj), run_time=0.4)

        # 作者信息放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B
        ).move_to(UP * 1.1)

        self.play(
            Transform(self.author_banner, author_big),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.7)

        # 三种关系小图标装饰
        icon_group = VGroup(
            # 平行图标
            VGroup(
                Line(LEFT * 0.5 + UP * 0.15, RIGHT * 0.5 + UP * 0.15, color=COLOR_L1, stroke_width=3),
                Line(LEFT * 0.5 + DOWN * 0.15, RIGHT * 0.5 + DOWN * 0.15, color=COLOR_L2, stroke_width=3),
            ),
            # 相交图标
            VGroup(
                Line(LEFT * 0.4 + DOWN * 0.4, RIGHT * 0.4 + UP * 0.4, color=COLOR_L1, stroke_width=3),
                Line(LEFT * 0.4 + UP * 0.4, RIGHT * 0.4 + DOWN * 0.4, color=COLOR_L2, stroke_width=3),
            ),
            # 重合图标
            VGroup(
                Line(LEFT * 0.5, RIGHT * 0.5, color=COLOR_L1, stroke_width=4),
                Line(LEFT * 0.5, RIGHT * 0.5, color=COLOR_L2, stroke_width=2, stroke_opacity=0.7),
            ),
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 1.5)

        self.play(
            *[FadeIn(ic, scale=0.5) for ic in icon_group],
            run_time=0.6,
        )

        # 底部文字
        tip = Text(
            "掌握斜率，两线关系一眼明！",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)

        self.wait(1.5)

        # 全场淡出
        self.play(
            FadeOut(self.author_banner),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(icon_group),
            FadeOut(tip),
            run_time=1.0,
        )
"""
003图形的放大与缩小 - Animation
使用 Manim 创建的数学教学视频

内容: 图形的放大与缩小
目标观众: 六年级学生
格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ScalingShapesLesson(Scene):
    """
    图形的放大与缩小 教学动画场景

    场景顺序:
    1. 开场引入 - 钩子问题
    2. 概念引入 - 什么是图形的放大与缩小
    3. 三角形放大演示 (2:1)
    4. 矩形缩小演示 (1:2)
    5. 关键规律 - 边长与面积的变化
    6. 应用举例 - 地图/模型
    7. 总结与片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_ORIGINAL = "#3498db"       # 蓝色 - 原图形
        self.COLOR_SCALED = "#e74c3c"         # 红色 - 缩放后图形
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_FORMULA = "#2ecc71"        # 绿色 - 公式
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_ACCENT = "#f39c12"         # 橙色 - 强调

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_concept_intro()
        self.scene_3_triangle_enlarge()
        self.scene_4_rectangle_shrink()
        self.scene_5_key_rules()
        self.scene_6_applications()
        self.scene_7_outro()

    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ===== 三角形放大演示数据 =====
        # 原始三角形顶点 (小三角形, 放在左侧)
        self.tri_scale = 0.8
        self.tri_offset = np.array([-2.0, 1.5, 0])

        self.tri_A = np.array([0, 0, 0]) * self.tri_scale + self.tri_offset
        self.tri_B = np.array([2, 0, 0]) * self.tri_scale + self.tri_offset
        self.tri_C = np.array([1, 1.5, 0]) * self.tri_scale + self.tri_offset

        # 放大后三角形 (2:1, 放在右侧)
        self.tri_enlarge_factor = 2
        self.tri_enlarge_offset = np.array([1.0, 0.5, 0])

        self.tri_A2 = np.array([0, 0, 0]) * self.tri_scale * self.tri_enlarge_factor + self.tri_enlarge_offset
        self.tri_B2 = np.array([2, 0, 0]) * self.tri_scale * self.tri_enlarge_factor + self.tri_enlarge_offset
        self.tri_C2 = np.array([1, 1.5, 0]) * self.tri_scale * self.tri_enlarge_factor + self.tri_enlarge_offset

        # 边长计算
        self.tri_AB = np.linalg.norm(self.tri_B - self.tri_A)
        self.tri_BC = np.linalg.norm(self.tri_C - self.tri_B)
        self.tri_CA = np.linalg.norm(self.tri_A - self.tri_C)

        self.tri_AB2 = np.linalg.norm(self.tri_B2 - self.tri_A2)
        self.tri_BC2 = np.linalg.norm(self.tri_C2 - self.tri_A2)  # recalc properly
        self.tri_CA2 = np.linalg.norm(self.tri_A2 - self.tri_C2)

        # ===== 矩形缩小演示数据 =====
        self.rect_w = 3.0
        self.rect_h = 2.0
        self.rect_center_orig = np.array([-1.5, 1.5, 0])

        self.rect_shrink_factor = 0.5
        self.rect_w_small = self.rect_w * self.rect_shrink_factor
        self.rect_h_small = self.rect_h * self.rect_shrink_factor
        self.rect_center_small = np.array([2.0, 1.5, 0])

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何计算"""
        epsilon = 1e-6

        # 验证放大比例: 边长应为原来的2倍
        ratio_AB = self.tri_AB2 / self.tri_AB
        assert abs(ratio_AB - self.tri_enlarge_factor) < epsilon, \
            f"AB ratio error: {ratio_AB}"

        # 验证缩小比例
        assert abs(self.rect_w_small / self.rect_w - self.rect_shrink_factor) < epsilon, \
            f"Width ratio error"
        assert abs(self.rect_h_small / self.rect_h - self.rect_shrink_factor) < epsilon, \
            f"Height ratio error"

        print("Geometry verification passed")

    # ===================================================================
    # Scene 1: Opening
    # ===================================================================
    def scene_1_opening(self):
        """开场引入"""
        # 作者信息
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)

        self.play(FadeIn(self.author_label, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "一张地图, 怎么把真实世界\n装进口袋?",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.4
        ).move_to(UP * 3.0)

        self.play(Write(hook), run_time=1.2)
        self.wait(1.0)

        # 小示意: 一个大矩形 -> 小矩形
        big_rect = Rectangle(
            width=3.5, height=2.5,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(DOWN * 0.5)

        big_label = Text(
            "真实世界",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_ORIGINAL
        ).move_to(big_rect.get_center())

        small_rect = Rectangle(
            width=1.2, height=0.85,
            color=self.COLOR_SCALED,
            fill_opacity=0.15,
            stroke_width=3
        ).move_to(DOWN * 4.0)

        small_label = Text(
            "地图",
            font="Noto Sans CJK SC",
            font_size=16,
            color=self.COLOR_SCALED
        ).move_to(small_rect.get_center())

        self.play(Create(big_rect), FadeIn(big_label), run_time=0.8)
        self.wait(0.5)

        arrow_down = Arrow(
            big_rect.get_bottom() + DOWN * 0.2,
            small_rect.get_top() + UP * 0.2,
            color=self.COLOR_ACCENT,
            stroke_width=3
        )
        shrink_text = Text(
            "按比例缩小",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_ACCENT
        ).next_to(arrow_down, RIGHT, buff=0.2)

        self.play(
            GrowArrow(arrow_down),
            FadeIn(shrink_text),
            run_time=0.6
        )
        self.play(Create(small_rect), FadeIn(small_label), run_time=0.8)
        self.wait(1.0)

        # 引出主题
        title = Text(
            "图形的放大与缩小",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(big_rect), FadeOut(big_label),
            FadeOut(small_rect), FadeOut(small_label),
            FadeOut(arrow_down), FadeOut(shrink_text),
            FadeOut(title),
            run_time=0.6
        )

    # ===================================================================
    # Scene 2: Concept Introduction
    # ===================================================================
    def scene_2_concept_intro(self):
        """概念引入"""
        title = Text(
            "什么是图形的放大与缩小?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.8)

        # 核心概念分点展示
        point_1 = Text(
            "把图形的每条边按相同的比放大或缩小",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 4.0)

        point_2 = Text(
            "对应边的比相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_FORMULA
        ).move_to(UP * 3.2)

        point_3 = Text(
            "形状不变, 大小改变",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_ACCENT
        ).move_to(UP * 2.4)

        self.play(FadeIn(point_1, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(point_2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(point_3, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.0)

        # 示意图: 原图和放大后的图并排
        # 原始正方形
        sq_orig = Square(
            side_length=1.2,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.2,
            stroke_width=3
        ).move_to(np.array([-2.0, -0.5, 0]))

        sq_orig_label = Text(
            "原图",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_ORIGINAL
        ).next_to(sq_orig, DOWN, buff=0.2)

        # 放大后正方形 (2倍)
        sq_big = Square(
            side_length=2.4,
            color=self.COLOR_SCALED,
            fill_opacity=0.2,
            stroke_width=3
        ).move_to(np.array([1.8, -0.5, 0]))

        sq_big_label = Text(
            "按 2:1 放大",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_SCALED
        ).next_to(sq_big, DOWN, buff=0.2)

        arrow_r = Arrow(
            sq_orig.get_right() + RIGHT * 0.15,
            sq_big.get_left() + LEFT * 0.15,
            color=self.COLOR_ACCENT,
            stroke_width=3
        )

        self.play(Create(sq_orig), FadeIn(sq_orig_label), run_time=0.6)
        self.play(GrowArrow(arrow_r), run_time=0.4)
        self.play(Create(sq_big), FadeIn(sq_big_label), run_time=0.6)

        # 标注边长
        side_1 = MathTex(r"1", font_size=20, color=self.COLOR_ORIGINAL).next_to(
            sq_orig, LEFT, buff=0.1
        )
        side_2 = MathTex(r"2", font_size=20, color=self.COLOR_SCALED).next_to(
            sq_big, LEFT, buff=0.1
        )

        self.play(FadeIn(side_1), FadeIn(side_2), run_time=0.4)

        # 比例关系
        ratio_text = MathTex(
            r"\frac{2}{1} = 2",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)

        ratio_explain = Text(
            "每条边都变为原来的 2 倍",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)

        self.play(Write(ratio_text), run_time=0.6)
        self.play(FadeIn(ratio_explain), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(point_1), FadeOut(point_2), FadeOut(point_3),
            FadeOut(sq_orig), FadeOut(sq_orig_label),
            FadeOut(sq_big), FadeOut(sq_big_label),
            FadeOut(arrow_r), FadeOut(side_1), FadeOut(side_2),
            FadeOut(ratio_text), FadeOut(ratio_explain),
            run_time=0.6
        )

    # ===================================================================
    # Scene 3: Triangle Enlargement 2:1
    # ===================================================================
    def scene_3_triangle_enlarge(self):
        """三角形按 2:1 放大演示"""
        title = Text(
            "三角形按 2:1 放大",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.8)

        # 原始三角形
        tri_orig = Polygon(
            self.tri_A, self.tri_B, self.tri_C,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.2,
            stroke_width=3
        )

        # 顶点标签
        label_A = MathTex("A", font_size=22, color=self.COLOR_ORIGINAL).next_to(
            self.tri_A, DL, buff=0.1
        )
        label_B = MathTex("B", font_size=22, color=self.COLOR_ORIGINAL).next_to(
            self.tri_B, DR, buff=0.1
        )
        label_C = MathTex("C", font_size=22, color=self.COLOR_ORIGINAL).next_to(
            self.tri_C, UP, buff=0.1
        )

        orig_label = Text(
            "原图",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_ORIGINAL
        ).next_to(tri_orig, DOWN, buff=0.3)

        self.play(Create(tri_orig), run_time=0.8)
        self.play(
            FadeIn(label_A), FadeIn(label_B), FadeIn(label_C),
            FadeIn(orig_label),
            run_time=0.5
        )

        # 标注各边长度
        ab_val = round(self.tri_AB / self.tri_scale, 1)
        bc_val = round(np.linalg.norm(
            (np.array([1, 1.5, 0]) - np.array([2, 0, 0]))
        ), 1)
        ca_val = round(np.linalg.norm(
            (np.array([0, 0, 0]) - np.array([1, 1.5, 0]))
        ), 1)

        # Edge labels for original
        mid_AB = (self.tri_A + self.tri_B) / 2
        mid_BC = (self.tri_B + self.tri_C) / 2
        mid_CA = (self.tri_C + self.tri_A) / 2

        edge_ab = MathTex(f"{ab_val}", font_size=18, color=self.COLOR_ORIGINAL).next_to(
            mid_AB, DOWN, buff=0.15
        )
        edge_bc = MathTex(f"{bc_val}", font_size=18, color=self.COLOR_ORIGINAL).next_to(
            mid_BC, RIGHT, buff=0.15
        )
        edge_ca = MathTex(f"{ca_val}", font_size=18, color=self.COLOR_ORIGINAL).next_to(
            mid_CA, LEFT, buff=0.15
        )

        self.play(FadeIn(edge_ab), FadeIn(edge_bc), FadeIn(edge_ca), run_time=0.5)
        self.wait(0.5)

        # 放大演示: 创建放大后的三角形
        tri_big = Polygon(
            self.tri_A2, self.tri_B2, self.tri_C2,
            color=self.COLOR_SCALED,
            fill_opacity=0.15,
            stroke_width=3
        )

        label_A2 = MathTex("A'", font_size=22, color=self.COLOR_SCALED).next_to(
            self.tri_A2, DL, buff=0.1
        )
        label_B2 = MathTex("B'", font_size=22, color=self.COLOR_SCALED).next_to(
            self.tri_B2, DR, buff=0.1
        )
        label_C2 = MathTex("C'", font_size=22, color=self.COLOR_SCALED).next_to(
            self.tri_C2, UP, buff=0.1
        )

        big_label = Text(
            "放大后",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_SCALED
        ).next_to(tri_big, DOWN, buff=0.3)

        # 动画: 从原始三角形复制并放大
        tri_copy = tri_orig.copy()
        self.play(
            Transform(tri_copy, tri_big),
            run_time=1.2
        )
        self.remove(tri_copy)
        self.add(tri_big)

        self.play(
            FadeIn(label_A2), FadeIn(label_B2), FadeIn(label_C2),
            FadeIn(big_label),
            run_time=0.5
        )

        # 放大后的边长标注
        mid_AB2 = (self.tri_A2 + self.tri_B2) / 2
        mid_BC2 = (self.tri_B2 + self.tri_C2) / 2
        mid_CA2 = (self.tri_C2 + self.tri_A2) / 2

        edge_ab2 = MathTex(
            f"{ab_val * 2}", font_size=18, color=self.COLOR_SCALED
        ).next_to(mid_AB2, DOWN, buff=0.15)
        edge_bc2 = MathTex(
            f"{bc_val * 2}", font_size=18, color=self.COLOR_SCALED
        ).next_to(mid_BC2, RIGHT, buff=0.15)
        edge_ca2 = MathTex(
            f"{ca_val * 2}", font_size=18, color=self.COLOR_SCALED
        ).next_to(mid_CA2, LEFT, buff=0.15)

        self.play(FadeIn(edge_ab2), FadeIn(edge_bc2), FadeIn(edge_ca2), run_time=0.5)

        # 显示比例关系
        ratio_box = VGroup()
        ratio_title = Text(
            "对应边的比:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        ratio_eq1 = MathTex(
            rf"\frac{{{ab_val * 2}}}{{{ab_val}}} = 2",
            font_size=24, color=self.COLOR_HIGHLIGHT
        )
        ratio_eq2 = MathTex(
            rf"\frac{{{bc_val * 2}}}{{{bc_val}}} = 2",
            font_size=24, color=self.COLOR_HIGHLIGHT
        )
        ratio_eq3 = MathTex(
            rf"\frac{{{ca_val * 2}}}{{{ca_val}}} = 2",
            font_size=24, color=self.COLOR_HIGHLIGHT
        )

        ratio_box = VGroup(ratio_title, ratio_eq1, ratio_eq2, ratio_eq3).arrange(
            DOWN, buff=0.25, aligned_edge=LEFT
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(ratio_box, shift=UP * 0.3), run_time=0.8)

        # 关键结论
        conclusion = Text(
            "每条边都变为原来的 2 倍!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(tri_orig), FadeOut(tri_big),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(label_A2), FadeOut(label_B2), FadeOut(label_C2),
            FadeOut(orig_label), FadeOut(big_label),
            FadeOut(edge_ab), FadeOut(edge_bc), FadeOut(edge_ca),
            FadeOut(edge_ab2), FadeOut(edge_bc2), FadeOut(edge_ca2),
            FadeOut(ratio_box), FadeOut(conclusion),
            run_time=0.6
        )

    # ===================================================================
    # Scene 4: Rectangle Shrink 1:2
    # ===================================================================
    def scene_4_rectangle_shrink(self):
        """矩形按 1:2 缩小演示"""
        title = Text(
            "矩形按 1:2 缩小",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.8)

        # 原始矩形
        rect_orig = Rectangle(
            width=self.rect_w, height=self.rect_h,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.2,
            stroke_width=3
        ).move_to(self.rect_center_orig)

        orig_label = Text(
            "原图",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_ORIGINAL
        ).next_to(rect_orig, DOWN, buff=0.3)

        # 边长标注
        w_label = MathTex(
            f"{int(self.rect_w)}", font_size=20, color=self.COLOR_ORIGINAL
        ).next_to(rect_orig, DOWN, buff=0.08)
        h_label = MathTex(
            f"{int(self.rect_h)}", font_size=20, color=self.COLOR_ORIGINAL
        ).next_to(rect_orig, LEFT, buff=0.08)

        self.play(Create(rect_orig), FadeIn(orig_label), run_time=0.8)
        self.play(FadeIn(w_label), FadeIn(h_label), run_time=0.4)
        self.wait(0.5)

        # 缩小后矩形
        rect_small = Rectangle(
            width=self.rect_w_small, height=self.rect_h_small,
            color=self.COLOR_SCALED,
            fill_opacity=0.2,
            stroke_width=3
        ).move_to(self.rect_center_small)

        small_label = Text(
            "缩小后",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_SCALED
        ).next_to(rect_small, DOWN, buff=0.3)

        w_label2 = MathTex(
            f"{self.rect_w_small:.1f}", font_size=20, color=self.COLOR_SCALED
        ).next_to(rect_small, DOWN, buff=0.08)
        h_label2 = MathTex(
            f"{self.rect_h_small:.1f}", font_size=20, color=self.COLOR_SCALED
        ).next_to(rect_small, RIGHT, buff=0.08)

        # 缩小动画
        rect_copy = rect_orig.copy()
        self.play(
            Transform(rect_copy, rect_small),
            run_time=1.2
        )
        self.remove(rect_copy)
        self.add(rect_small)

        self.play(
            FadeIn(small_label),
            FadeIn(w_label2), FadeIn(h_label2),
            run_time=0.5
        )

        # 显示箭头和比例
        arrow_r = Arrow(
            rect_orig.get_right() + RIGHT * 0.15,
            rect_small.get_left() + LEFT * 0.15,
            color=self.COLOR_ACCENT,
            stroke_width=3
        )
        ratio_label = Text(
            "1 : 2",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_ACCENT
        ).next_to(arrow_r, UP, buff=0.1)

        self.play(GrowArrow(arrow_r), FadeIn(ratio_label), run_time=0.5)

        # 比例关系
        ratio_info = VGroup(
            MathTex(
                rf"\frac{{{self.rect_w_small:.1f}}}{{{int(self.rect_w)}}} = \frac{{1}}{{2}}",
                font_size=24, color=self.COLOR_HIGHLIGHT
            ),
            MathTex(
                rf"\frac{{{self.rect_h_small:.1f}}}{{{int(self.rect_h)}}} = \frac{{1}}{{2}}",
                font_size=24, color=self.COLOR_HIGHLIGHT
            ),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 3.5)

        self.play(FadeIn(ratio_info, shift=UP * 0.3), run_time=0.6)

        # 面积变化
        area_info = VGroup()
        area_title = Text(
            "面积变化:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        area_orig_val = int(self.rect_w * self.rect_h)
        area_small_val = self.rect_w_small * self.rect_h_small
        area_eq = MathTex(
            rf"\frac{{{area_small_val:.2f}}}{{{area_orig_val}}} = \frac{{1}}{{4}} = \left(\frac{{1}}{{2}}\right)^2",
            font_size=22, color=self.COLOR_FORMULA
        )
        area_info = VGroup(area_title, area_eq).arrange(
            DOWN, buff=0.2
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(area_info, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rect_orig), FadeOut(rect_small),
            FadeOut(orig_label), FadeOut(small_label),
            FadeOut(w_label), FadeOut(h_label),
            FadeOut(w_label2), FadeOut(h_label2),
            FadeOut(arrow_r), FadeOut(ratio_label),
            FadeOut(ratio_info), FadeOut(area_info),
            run_time=0.6
        )

    # ===================================================================
    # Scene 5: Key Rules
    # ===================================================================
    def scene_5_key_rules(self):
        """关键规律: 边长与面积的变化"""
        title = Text(
            "关键规律",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.8)

        # 规律卡片 1: 放大
        card_bg_1 = RoundedRectangle(
            corner_radius=0.2,
            width=7.5, height=2.8,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(UP * 2.5)

        card_title_1 = Text(
            "按比例 k 放大 (k > 1)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_ORIGINAL
        ).move_to(card_bg_1.get_top() + DOWN * 0.5)

        rule_1a_label = Text(
            "边长:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        rule_1a_formula = MathTex(
            r"\times k",
            font_size=28, color=self.COLOR_HIGHLIGHT
        )
        rule_1a = VGroup(rule_1a_label, rule_1a_formula).arrange(
            RIGHT, buff=0.2
        ).move_to(card_bg_1.get_center() + UP * 0.1)

        rule_1b_label = Text(
            "面积:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        rule_1b_formula = MathTex(
            r"\times k^2",
            font_size=28, color=self.COLOR_HIGHLIGHT
        )
        rule_1b = VGroup(rule_1b_label, rule_1b_formula).arrange(
            RIGHT, buff=0.2
        ).move_to(card_bg_1.get_center() + DOWN * 0.6)

        self.play(
            FadeIn(card_bg_1),
            Write(card_title_1),
            run_time=0.6
        )
        self.play(FadeIn(rule_1a), run_time=0.5)
        self.play(FadeIn(rule_1b), run_time=0.5)
        self.wait(0.5)

        # 规律卡片 2: 缩小
        card_bg_2 = RoundedRectangle(
            corner_radius=0.2,
            width=7.5, height=2.8,
            color=self.COLOR_SCALED,
            fill_opacity=0.08,
            stroke_width=2
        ).move_to(DOWN * 1.0)

        card_title_2 = Text(
            "按比例 k 缩小 (0 < k < 1)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SCALED
        ).move_to(card_bg_2.get_top() + DOWN * 0.5)

        rule_2a_label = Text(
            "边长:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        rule_2a_formula = MathTex(
            r"\times k",
            font_size=28, color=self.COLOR_HIGHLIGHT
        )
        rule_2a = VGroup(rule_2a_label, rule_2a_formula).arrange(
            RIGHT, buff=0.2
        ).move_to(card_bg_2.get_center() + UP * 0.1)

        rule_2b_label = Text(
            "面积:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        rule_2b_formula = MathTex(
            r"\times k^2",
            font_size=28, color=self.COLOR_HIGHLIGHT
        )
        rule_2b = VGroup(rule_2b_label, rule_2b_formula).arrange(
            RIGHT, buff=0.2
        ).move_to(card_bg_2.get_center() + DOWN * 0.6)

        self.play(
            FadeIn(card_bg_2),
            Write(card_title_2),
            run_time=0.6
        )
        self.play(FadeIn(rule_2a), run_time=0.5)
        self.play(FadeIn(rule_2b), run_time=0.5)
        self.wait(0.5)

        # 重点强调
        emphasis_box = RoundedRectangle(
            corner_radius=0.15,
            width=7.0, height=1.8,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.1,
            stroke_width=2
        ).move_to(DOWN * 4.2)

        emphasis_1 = Text(
            "形状不变, 大小改变!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(emphasis_box.get_center() + UP * 0.25)

        emphasis_2 = Text(
            "对应角的度数不变",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(emphasis_box.get_center() + DOWN * 0.35)

        self.play(
            FadeIn(emphasis_box),
            Write(emphasis_1),
            run_time=0.6
        )
        self.play(FadeIn(emphasis_2), run_time=0.4)
        self.wait(2.0)

        # 具体例子: k=2 时
        example_title = Text(
            "例: k = 2",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_ACCENT
        ).move_to(DOWN * 6.0)

        example_detail_label = Text(
            "边长变为 2 倍, 面积变为 ",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        example_detail_formula = MathTex(
            r"2^2 = 4",
            font_size=22, color=self.COLOR_ACCENT
        )
        example_detail_suffix = Text(
            " 倍",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        example_detail = VGroup(
            example_detail_label, example_detail_formula, example_detail_suffix
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 6.8)

        self.play(FadeIn(example_title), run_time=0.4)
        self.play(FadeIn(example_detail), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card_bg_1), FadeOut(card_title_1),
            FadeOut(rule_1a), FadeOut(rule_1b),
            FadeOut(card_bg_2), FadeOut(card_title_2),
            FadeOut(rule_2a), FadeOut(rule_2b),
            FadeOut(emphasis_box), FadeOut(emphasis_1), FadeOut(emphasis_2),
            FadeOut(example_title), FadeOut(example_detail),
            run_time=0.6
        )

    # ===================================================================
    # Scene 6: Applications
    # ===================================================================
    def scene_6_applications(self):
        """应用举例"""
        title = Text(
            "生活中的应用",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.8)

        # 应用 1: 地图
        app1_icon = Square(
            side_length=1.5,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.15,
            stroke_width=2
        ).move_to(np.array([-2.5, 3.0, 0]))

        # Add grid lines inside to suggest map
        grid_lines_1 = VGroup()
        for i in range(1, 3):
            h_line = Line(
                app1_icon.get_left() + UP * (0.5 * i - 0.75),
                app1_icon.get_right() + UP * (0.5 * i - 0.75),
                color=self.COLOR_ORIGINAL, stroke_width=1, stroke_opacity=0.3
            )
            grid_lines_1.add(h_line)
        for i in range(1, 3):
            v_line = Line(
                app1_icon.get_bottom() + RIGHT * (0.5 * i - 0.75),
                app1_icon.get_top() + RIGHT * (0.5 * i - 0.75),
                color=self.COLOR_ORIGINAL, stroke_width=1, stroke_opacity=0.3
            )
            grid_lines_1.add(v_line)

        app1_label = Text(
            "地图",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).next_to(app1_icon, RIGHT, buff=0.4)

        app1_desc = Text(
            "把真实距离按比例缩小",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(app1_label, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(
            Create(app1_icon), FadeIn(grid_lines_1),
            FadeIn(app1_label), FadeIn(app1_desc),
            run_time=0.8
        )
        self.wait(0.5)

        # 应用 2: 模型
        app2_icon = VGroup()
        # A small house shape
        house_base = Rectangle(
            width=1.2, height=0.8,
            color=self.COLOR_SCALED,
            fill_opacity=0.15,
            stroke_width=2
        )
        house_roof = Polygon(
            house_base.get_corner(UL),
            house_base.get_corner(UR),
            house_base.get_top() + UP * 0.5,
            color=self.COLOR_SCALED,
            fill_opacity=0.15,
            stroke_width=2
        )
        app2_icon = VGroup(house_base, house_roof).move_to(np.array([-2.5, 0.5, 0]))

        app2_label = Text(
            "建筑模型",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).next_to(app2_icon, RIGHT, buff=0.4)

        app2_desc = Text(
            "把建筑按比例缩小制作模型",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(app2_label, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(
            Create(app2_icon),
            FadeIn(app2_label), FadeIn(app2_desc),
            run_time=0.8
        )
        self.wait(0.5)

        # 应用 3: 设计图/放大镜
        app3_icon = Circle(
            radius=0.6,
            color=self.COLOR_ACCENT,
            fill_opacity=0.1,
            stroke_width=2
        ).move_to(np.array([-2.5, -2.0, 0]))

        # magnifying glass handle
        handle = Line(
            app3_icon.get_corner(DR),
            app3_icon.get_corner(DR) + DR * 0.6,
            color=self.COLOR_ACCENT,
            stroke_width=3
        )
        app3_group = VGroup(app3_icon, handle)

        app3_label = Text(
            "放大镜/设计图",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).next_to(app3_group, RIGHT, buff=0.4)

        app3_desc = Text(
            "把细节按比例放大观察",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(app3_label, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(
            Create(app3_group),
            FadeIn(app3_label), FadeIn(app3_desc),
            run_time=0.8
        )
        self.wait(0.5)

        # 总结文字
        summary_text = Text(
            "图形的放大与缩小无处不在!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(summary_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(app1_icon), FadeOut(grid_lines_1),
            FadeOut(app1_label), FadeOut(app1_desc),
            FadeOut(app2_icon),
            FadeOut(app2_label), FadeOut(app2_desc),
            FadeOut(app3_group),
            FadeOut(app3_label), FadeOut(app3_desc),
            FadeOut(summary_text),
            run_time=0.6
        )

    # ===================================================================
    # Scene 7: Outro
    # ===================================================================
    def scene_7_outro(self):
        """总结与片尾"""
        # 快速回顾
        review_title = Text(
            "今天学到了什么?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 5.0)

        self.play(Write(review_title), run_time=0.6)

        points = VGroup(
            Text(
                "1. 放大与缩小保持形状不变",
                font="Noto Sans CJK SC", font_size=22, color=WHITE
            ),
            Text(
                "2. 对应边的比相等",
                font="Noto Sans CJK SC", font_size=22, color=WHITE
            ),
            Text(
                "3. 边长变 k 倍, 面积变 k\u00b2 倍",
                font="Noto Sans CJK SC", font_size=22, color=WHITE
            ),
            Text(
                "4. 各角的度数不变",
                font="Noto Sans CJK SC", font_size=22, color=WHITE
            ),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 2.0)

        for i, point in enumerate(points):
            self.play(FadeIn(point, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.3)

        self.wait(1.0)

        # 动态小演示: 一个正方形逐渐放大缩小
        demo_sq = Square(
            side_length=1.0,
            color=self.COLOR_ORIGINAL,
            fill_opacity=0.3,
            stroke_width=2
        ).move_to(DOWN * 2.5)

        self.play(Create(demo_sq), run_time=0.5)
        self.play(
            demo_sq.animate.scale(2).set_color(self.COLOR_SCALED),
            run_time=1.0,
            rate_func=there_and_back
        )
        self.play(
            demo_sq.animate.scale(0.5).set_color(self.COLOR_FORMULA),
            run_time=1.0,
            rate_func=there_and_back
        )
        self.wait(0.5)

        # 清理回顾内容
        self.play(
            FadeOut(review_title), FadeOut(points), FadeOut(demo_sq),
            run_time=0.5
        )

        # 作者片尾
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.5)

        follow_text = Text(
            "关注我, 获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)

        self.play(
            Transform(self.author_label, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # 最终淡出
        self.play(
            FadeOut(self.author_label),
            FadeOut(author_id),
            FadeOut(follow_text),
            run_time=1.0
        )

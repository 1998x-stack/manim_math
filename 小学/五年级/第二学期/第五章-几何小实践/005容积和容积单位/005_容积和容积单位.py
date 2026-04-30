"""
005_容积和容积单位.py -- 容积和容积单位 教学动画

知识点: 容积的概念、容积单位(升和毫升)、容积与体积的关系
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 容积: 容器所能容纳物体的体积
  2. 常用单位: 升(L)、毫升(mL)
  3. 换算关系: 1L = 1000mL, 1L = 1dm³, 1mL = 1cm³
  4. 容积与体积的区别: 容积从内部量, 通常比体积小
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
COLOR_BOX = "#3b82f6"        # 蓝色 容器外壁
COLOR_WATER = "#06b6d4"      # 青色 水/液体
COLOR_INNER = "#22c55e"      # 绿色 内部空间
COLOR_LITER = "#f59e0b"      # 橙色 升
COLOR_ML = "#a78bfa"         # 紫色 毫升
COLOR_HL = "#fbbf24"         # 黄色 高亮
COLOR_FORMULA = "#f472b6"    # 粉色 公式
COLOR_AUTHOR = "#6b7280"     # 灰色 作者信息
COLOR_WALL = "#94a3b8"       # 灰蓝 壁厚标注
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class CapacityLesson(Scene):
    """
    容积和容积单位 教学动画
    场景顺序:
      1. 开场钩子
      2. 容积概念
      3. 容积单位及换算
      4. 容积与体积的区别
      5. 知识总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_capacity_concept()
        self.scene_3_unit_relations()
        self.scene_4_capacity_vs_volume()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 辅助: 创建容器 (带壁厚的矩形截面)
    # ------------------------------------------------------------------

    def _make_container(self, width=3.0, height=2.5, wall=0.15,
                        outer_color=COLOR_BOX, inner_color=COLOR_INNER,
                        outer_opacity=0.6, inner_opacity=0.25):
        """创建带壁厚的容器截面 (正面视图)"""
        outer = Rectangle(
            width=width, height=height,
            color=outer_color, fill_color=outer_color,
            fill_opacity=outer_opacity, stroke_width=3
        )
        inner = Rectangle(
            width=width - 2 * wall, height=height - wall,
            color=inner_color, fill_color=inner_color,
            fill_opacity=inner_opacity, stroke_width=2
        )
        # 内部略偏上 (底部有壁厚, 顶部开口)
        inner.move_to(outer.get_center() + UP * wall * 0.5)
        return VGroup(outer, inner)

    def _make_water(self, container, fill_ratio=0.7):
        """在容器内部创建水面"""
        inner = container[1]  # 内部矩形
        w = inner.get_width()
        h = inner.get_height() * fill_ratio
        water = Rectangle(
            width=w, height=h,
            color=COLOR_WATER, fill_color=COLOR_WATER,
            fill_opacity=0.5, stroke_width=1.5
        )
        water.move_to(inner.get_bottom() + UP * h / 2)
        return water

    def _make_3d_box(self, w=2.0, h=1.5, d=1.2, color=COLOR_BOX, opacity=0.3):
        """创建简单的3D长方体示意 (用平行四边形模拟)"""
        # 正面
        front = Rectangle(width=w, height=h, color=color,
                          fill_color=color, fill_opacity=opacity, stroke_width=2)
        # 顶面 (平行四边形)
        top_pts = [
            front.get_corner(UL),
            front.get_corner(UR),
            front.get_corner(UR) + np.array([d * 0.5, d * 0.35, 0]),
            front.get_corner(UL) + np.array([d * 0.5, d * 0.35, 0]),
        ]
        top = Polygon(*top_pts, color=color, fill_color=color,
                       fill_opacity=opacity * 0.7, stroke_width=2)
        # 右侧面
        right_pts = [
            front.get_corner(UR),
            front.get_corner(DR),
            front.get_corner(DR) + np.array([d * 0.5, d * 0.35, 0]),
            front.get_corner(UR) + np.array([d * 0.5, d * 0.35, 0]),
        ]
        right = Polygon(*right_pts, color=color, fill_color=color,
                         fill_opacity=opacity * 0.5, stroke_width=2)
        return VGroup(front, top, right)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 一瓶水能装多少?"""

        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "一个容器", font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "能装多少？", font=FONT, font_size=52, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 显示容器 + 水
        container = self._make_container(width=3.5, height=3.0)
        container.move_to(ORIGIN + UP * 0.5)
        water = self._make_water(container, fill_ratio=0.65)

        self.play(Create(container), run_time=1.0)
        self.play(FadeIn(water, shift=UP * 0.3), run_time=0.8)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(container.get_center() + UP * 0.3)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 引入 "容积" 概念
        intro = Text(
            "这就是 ── 容积", font=FONT, font_size=36, color=COLOR_FORMULA
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(intro, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(VGroup(hook1, hook2, q, container, water, intro)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 容积概念
    # ------------------------------------------------------------------

    def scene_2_capacity_concept(self):
        """容积 = 容器所能容纳物体的体积"""

        title = Text(
            "什么是容积？", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义
        defn_line1 = Text(
            "容器所能容纳物体的体积",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.0)
        defn_line2 = Text(
            "叫做这个容器的容积",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 3.3)
        self.play(Write(defn_line1), run_time=0.7)
        self.play(Write(defn_line2), run_time=0.7)
        self.wait(0.5)

        # 示例容器组
        examples = VGroup()
        labels_text = ["水杯", "水桶", "鱼缸"]
        sizes = [(1.4, 2.0), (2.2, 2.5), (3.0, 2.0)]
        x_positions = [-3.0, 0.0, 3.0]

        for i, (label, (w, h), x) in enumerate(
            zip(labels_text, sizes, x_positions)
        ):
            c = self._make_container(width=w, height=h, wall=0.12)
            c.move_to(np.array([x, -0.5, 0]))
            wt = self._make_water(c, fill_ratio=0.5 + i * 0.15)
            lb = Text(label, font=FONT, font_size=22, color=GRAY_A)
            lb.next_to(c, DOWN, buff=0.3)
            grp = VGroup(c, wt, lb)
            examples.add(grp)

        self.play(
            LaggedStart(*[FadeIn(e, shift=UP * 0.3) for e in examples],
                        lag_ratio=0.3),
            run_time=1.5
        )
        self.wait(0.5)

        # 强调: 不同容器, 容积不同
        note = Text(
            "不同容器的容积不同",
            font=FONT, font_size=26, color=COLOR_FORMULA
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)

        # 箭头指向每个容器
        arrows = VGroup()
        for ex in examples:
            ar = Arrow(
                note.get_top() + UP * 0.1,
                ex[0].get_bottom() + DOWN * 0.1,
                color=COLOR_HL, stroke_width=2, buff=0.15,
                max_tip_length_to_length_ratio=0.1
            )
            arrows.add(ar)
        self.play(
            LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15),
            run_time=0.8
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(title, defn_line1, defn_line2,
                           examples, note, arrows)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 容积单位及换算关系
    # ------------------------------------------------------------------

    def scene_3_unit_relations(self):
        """升(L)、毫升(mL) 以及与体积单位的换算"""

        title = Text(
            "容积单位", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 两大单位
        unit_L = Text("升 (L)", font=FONT, font_size=40, color=COLOR_LITER)
        unit_mL = Text("毫升 (mL)", font=FONT, font_size=40, color=COLOR_ML)
        unit_L.move_to(UP * 3.8 + LEFT * 2.5)
        unit_mL.move_to(UP * 3.8 + RIGHT * 2.5)

        self.play(Write(unit_L), run_time=0.5)
        self.play(Write(unit_mL), run_time=0.5)
        self.wait(0.3)

        # 换算关系 1: 1L = 1000mL
        rel1_box = RoundedRectangle(
            width=7.5, height=1.4, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(UP * 1.8)

        rel1_text = Text("1 L = 1000 mL", font=FONT, font_size=36, color=WHITE)
        rel1_text.move_to(rel1_box.get_center())

        self.play(FadeIn(rel1_box), run_time=0.3)
        self.play(Write(rel1_text), run_time=0.7)
        self.wait(0.5)

        # 视觉说明: 1个大瓶 = 1000个小滴
        big_bottle = self._make_container(width=1.8, height=2.4, wall=0.1,
                                          outer_color=COLOR_LITER)
        big_bottle.move_to(LEFT * 2.5 + DOWN * 0.8)
        big_label = Text("1 L", font=FONT, font_size=24, color=COLOR_LITER)
        big_label.next_to(big_bottle, DOWN, buff=0.25)

        water_big = self._make_water(big_bottle, fill_ratio=0.85)

        self.play(FadeIn(big_bottle), FadeIn(water_big), FadeIn(big_label),
                  run_time=0.6)

        eq_sign = Text("=", font=FONT, font_size=48, color=WHITE).move_to(DOWN * 0.8)
        self.play(Write(eq_sign), run_time=0.3)

        # 小容器群表示 1000mL
        small_group = VGroup()
        for row in range(3):
            for col in range(5):
                dot = Circle(
                    radius=0.12, color=COLOR_ML,
                    fill_color=COLOR_ML, fill_opacity=0.7, stroke_width=1
                )
                dot.move_to(np.array([
                    1.2 + col * 0.35, -0.1 - row * 0.35, 0
                ]))
                small_group.add(dot)
        small_label = Text(
            "1000 mL", font=FONT, font_size=22, color=COLOR_ML
        ).next_to(small_group, DOWN, buff=0.25)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.3) for d in small_group],
                        lag_ratio=0.02),
            FadeIn(small_label),
            run_time=1.0
        )
        self.wait(0.8)

        # 清除视觉说明部分
        self.play(
            FadeOut(VGroup(big_bottle, water_big, big_label,
                           eq_sign, small_group, small_label)),
            run_time=0.4
        )

        # 换算关系 2: 1L = 1dm^3
        rel2_box = RoundedRectangle(
            width=7.5, height=1.4, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_LITER, stroke_width=2.5
        ).move_to(DOWN * 0.5)

        rel2_label = Text("1 L", font=FONT, font_size=34, color=COLOR_LITER)
        rel2_eq = Text(" = ", font=FONT, font_size=34, color=WHITE)
        rel2_val = MathTex(r"1 \text{ dm}^3", font_size=40, color=COLOR_LITER)
        rel2_line = VGroup(rel2_label, rel2_eq, rel2_val).arrange(RIGHT, buff=0.1)
        rel2_line.move_to(rel2_box.get_center())

        self.play(FadeIn(rel2_box), run_time=0.3)
        self.play(Write(rel2_line), run_time=0.7)
        self.wait(0.5)

        # 换算关系 3: 1mL = 1cm^3
        rel3_box = RoundedRectangle(
            width=7.5, height=1.4, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_ML, stroke_width=2.5
        ).move_to(DOWN * 2.8)

        rel3_label = Text("1 mL", font=FONT, font_size=34, color=COLOR_ML)
        rel3_eq = Text(" = ", font=FONT, font_size=34, color=WHITE)
        rel3_val = MathTex(r"1 \text{ cm}^3", font_size=40, color=COLOR_ML)
        rel3_line = VGroup(rel3_label, rel3_eq, rel3_val).arrange(RIGHT, buff=0.1)
        rel3_line.move_to(rel3_box.get_center())

        self.play(FadeIn(rel3_box), run_time=0.3)
        self.play(Write(rel3_line), run_time=0.7)
        self.wait(0.5)

        # 汇总提示
        tip = Text(
            "计量液体，通常用升和毫升",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(title, unit_L, unit_mL,
                           rel1_box, rel1_text,
                           rel2_box, rel2_line,
                           rel3_box, rel3_line, tip)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 容积与体积的区别
    # ------------------------------------------------------------------

    def scene_4_capacity_vs_volume(self):
        """容积从里面量, 体积从外面量, 容积 <= 体积"""

        title = Text(
            "容积 vs 体积", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 创建带壁厚的容器 (侧面截图)
        wall_thickness = 0.3
        outer_w, outer_h = 5.0, 3.5
        inner_w = outer_w - 2 * wall_thickness
        inner_h = outer_h - wall_thickness  # 顶部开口

        outer_rect = Rectangle(
            width=outer_w, height=outer_h,
            color=COLOR_BOX, fill_color=COLOR_BOX,
            fill_opacity=0.4, stroke_width=3
        ).move_to(UP * 1.0)

        inner_rect = Rectangle(
            width=inner_w, height=inner_h,
            color=COLOR_INNER, fill_color=COLOR_INNER,
            fill_opacity=0.2, stroke_width=2, stroke_color=COLOR_INNER
        )
        inner_rect.move_to(outer_rect.get_center() + UP * wall_thickness * 0.5)

        self.play(Create(outer_rect), run_time=0.7)
        self.play(Create(inner_rect), run_time=0.7)
        self.wait(0.3)

        # 标注体积 (外部尺寸)
        vol_brace_w = Brace(outer_rect, DOWN, color=COLOR_BOX)
        vol_brace_w_label = Text(
            "外部长", font=FONT, font_size=20, color=COLOR_BOX
        )
        vol_brace_w_label.next_to(vol_brace_w, DOWN, buff=0.15)

        vol_brace_h = Brace(outer_rect, RIGHT, color=COLOR_BOX)
        vol_brace_h_label = Text(
            "外部高", font=FONT, font_size=20, color=COLOR_BOX
        )
        vol_brace_h_label.next_to(vol_brace_h, RIGHT, buff=0.15)

        vol_label = Text(
            "体积: 从外面量", font=FONT, font_size=26, color=COLOR_BOX
        ).move_to(DOWN * 2.0)

        self.play(
            Create(vol_brace_w), FadeIn(vol_brace_w_label),
            Create(vol_brace_h), FadeIn(vol_brace_h_label),
            FadeIn(vol_label),
            run_time=0.8
        )
        self.wait(0.8)

        # 标注容积 (内部尺寸)
        cap_brace_w = Brace(inner_rect, DOWN, color=COLOR_INNER)
        cap_brace_w.shift(DOWN * 0.15)
        cap_brace_w_label = Text(
            "内部长", font=FONT, font_size=20, color=COLOR_INNER
        )
        cap_brace_w_label.next_to(cap_brace_w, DOWN, buff=0.15)

        cap_brace_h = Brace(inner_rect, LEFT, color=COLOR_INNER)
        cap_brace_h_label = Text(
            "内部高", font=FONT, font_size=20, color=COLOR_INNER
        )
        cap_brace_h_label.next_to(cap_brace_h, LEFT, buff=0.15)

        cap_label = Text(
            "容积: 从里面量", font=FONT, font_size=26, color=COLOR_INNER
        ).move_to(DOWN * 3.2)

        self.play(
            Create(cap_brace_w), FadeIn(cap_brace_w_label),
            Create(cap_brace_h), FadeIn(cap_brace_h_label),
            FadeIn(cap_label),
            run_time=0.8
        )
        self.wait(0.8)

        # 壁厚标注
        wall_arrow = DoubleArrow(
            outer_rect.get_left() + UP * 0.5,
            inner_rect.get_left() + UP * 0.5,
            color=COLOR_WALL, stroke_width=2.5, buff=0.05,
            max_tip_length_to_length_ratio=0.3
        )
        wall_label = Text(
            "壁厚", font=FONT, font_size=18, color=COLOR_WALL
        ).next_to(wall_arrow, UP, buff=0.15)
        self.play(Create(wall_arrow), FadeIn(wall_label), run_time=0.5)
        self.wait(0.5)

        # 关键结论
        conclusion_box = RoundedRectangle(
            width=7.5, height=1.6, corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_FORMULA, stroke_width=3
        ).move_to(DOWN * 5.2)

        conclusion_line1 = Text(
            "容积从内部量，体积从外部量",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 4.8)
        conclusion_line2 = Text(
            "容积通常小于体积",
            font=FONT, font_size=26, color=COLOR_FORMULA, weight=BOLD
        ).move_to(DOWN * 5.6)

        self.play(FadeIn(conclusion_box), run_time=0.3)
        self.play(Write(conclusion_line1), run_time=0.6)
        self.play(Write(conclusion_line2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, outer_rect, inner_rect,
                vol_brace_w, vol_brace_w_label,
                vol_brace_h, vol_brace_h_label,
                vol_label,
                cap_brace_w, cap_brace_w_label,
                cap_brace_h, cap_brace_h_label,
                cap_label,
                wall_arrow, wall_label,
                conclusion_box, conclusion_line1, conclusion_line2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 知识总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        """总结所有知识点"""

        title = Text(
            "知识总结", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 总结框
        summary_box = RoundedRectangle(
            width=8.0, height=9.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(summary_box), run_time=0.3)

        # 知识点列表
        points = [
            ("1. 容积的概念", WHITE, 28),
            ("容器所能容纳物体的体积", GRAY_A, 24),
            ("", WHITE, 10),
            ("2. 容积单位", WHITE, 28),
            ("升 (L) 和 毫升 (mL)", COLOR_LITER, 24),
            ("", WHITE, 10),
            ("3. 换算关系", WHITE, 28),
            ("1 L = 1000 mL", COLOR_HL, 26),
        ]

        point_mobs = VGroup()
        for text, color, size in points:
            if text:
                t = Text(text, font=FONT, font_size=size, color=color)
            else:
                t = Text(" ", font=FONT, font_size=size)
            point_mobs.add(t)

        point_mobs.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        point_mobs.move_to(UP * 1.8 + LEFT * 0.3)

        self.play(
            LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in point_mobs],
                        lag_ratio=0.15),
            run_time=2.0
        )
        self.wait(0.5)

        # MathTex 行: 1L = 1dm^3, 1mL = 1cm^3
        math_row1_label = Text("1 L", font=FONT, font_size=26, color=COLOR_LITER)
        math_row1_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        math_row1_val = MathTex(r"1 \text{ dm}^3", font_size=32, color=COLOR_LITER)
        math_row1 = VGroup(math_row1_label, math_row1_eq, math_row1_val
                           ).arrange(RIGHT, buff=0.08)

        math_row2_label = Text("1 mL", font=FONT, font_size=26, color=COLOR_ML)
        math_row2_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        math_row2_val = MathTex(r"1 \text{ cm}^3", font_size=32, color=COLOR_ML)
        math_row2 = VGroup(math_row2_label, math_row2_eq, math_row2_val
                           ).arrange(RIGHT, buff=0.08)

        math_rows = VGroup(math_row1, math_row2).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        math_rows.move_to(DOWN * 1.8)

        self.play(
            LaggedStart(
                FadeIn(math_row1, shift=RIGHT * 0.2),
                FadeIn(math_row2, shift=RIGHT * 0.2),
                lag_ratio=0.3
            ),
            run_time=0.8
        )
        self.wait(0.5)

        # 容积 vs 体积
        vs_line = Text(
            "4. 容积从内部量，通常小于体积",
            font=FONT, font_size=24, color=COLOR_FORMULA
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(vs_line, shift=RIGHT * 0.2), run_time=0.5)

        # 高亮框
        hl_rect = SurroundingRectangle(
            point_mobs[7],  # "1 L = 1000 mL"
            color=COLOR_FORMULA, stroke_width=2.5,
            buff=0.12, corner_radius=0.1
        )
        self.play(Create(hl_rect), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(title, summary_box, point_mobs,
                           math_rows, vs_line, hl_rect)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息 + 关注提示"""

        # 作者名放大居中
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

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 小水滴形状 (用圆形模拟)
        colors = [COLOR_BOX, COLOR_WATER, COLOR_INNER,
                  COLOR_LITER, COLOR_ML, COLOR_HL]
        mini_shapes = VGroup(*[
            Circle(
                radius=0.18,
                fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(s, scale=0.3) for s in mini_shapes], run_time=0.5)
        self.play(
            Rotate(mini_shapes, angle=2 * PI / 3, run_time=1.2, rate_func=smooth)
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_shapes)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -ql --disable_caching 005_容积和容积单位.py CapacityLesson
#   高质量:    manim -qh  005_容积和容积单位.py CapacityLesson
#   4K:        manim -qk  005_容积和容积单位.py CapacityLesson
# ======================================================================

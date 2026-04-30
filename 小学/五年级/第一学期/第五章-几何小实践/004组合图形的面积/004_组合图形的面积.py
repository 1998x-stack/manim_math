"""
004_组合图形的面积.py — 组合图形的面积 教学动画

知识点: 分割法和添补法计算组合图形面积
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

几何核心:
  L 形组合图形 (6个顶点):
    P0(0,0) → P1(4,0) → P2(4,1.5) → P3(2,1.5) → P4(2,3) → P5(0,3)
  分割法: 分成两个长方形
    R1: P0,P1,P2,P3下方 → (0,0)-(4,0)-(4,1.5)-(0,1.5)  实际分割成:
    方案: 水平分割线 y=1.5
      下半: (0,0),(4,0),(4,1.5),(0,1.5)   → 4×1.5 = 6
      上半: (0,1.5),(2,1.5),(2,3),(0,3)   → 2×1.5 = 3
      总面积 = 6 + 3 = 9
  添补法: 补成大长方形 4×3=12，减去右上角 2×1.5=3
      总面积 = 12 - 3 = 9
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
COLOR_SHAPE = "#3b82f6"      # 蓝色主图形
COLOR_R1 = "#22c55e"         # 绿色矩形1
COLOR_R2 = "#f59e0b"         # 橙色矩形2
COLOR_BIG = "#8b5cf6"        # 紫色大长方形
COLOR_SUB = "#ef4444"        # 红色减去部分
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_CUT = "#a78bfa"        # 紫色分割线
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class CompositeAreaLesson(Scene):
    """
    组合图形的面积教学动画
    场景:
      1. 开场钩子
      2. 展示L形图形
      3. 分割法演示
      4. 添补法演示
      5. 策略对比总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_show_shape()
        self.scene_3_split_method()
        self.scene_4_add_method()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""

        # L 形图形顶点 (逆时针), 以中心偏移让图形居中
        # 原始坐标先算，再统一偏移
        raw = [
            np.array([0.0, 0.0, 0.0]),   # P0 左下
            np.array([4.0, 0.0, 0.0]),   # P1 右下
            np.array([4.0, 1.5, 0.0]),   # P2 右中
            np.array([2.0, 1.5, 0.0]),   # P3 中拐点
            np.array([2.0, 3.0, 0.0]),   # P4 左上右
            np.array([0.0, 3.0, 0.0]),   # P5 左上
        ]

        # 居中偏移
        centroid = sum(raw) / len(raw)
        offset = np.array([-centroid[0], -centroid[1], 0.0])

        self.P = [p + offset for p in raw]

        # ===== 分割法: 水平线 y = P3.y 分成上下两个矩形 =====
        split_y = self.P[3][1]  # = 1.5 + offset_y

        # 下半矩形 R1: P0, P1, (P1.x, split_y), (P0.x, split_y)
        self.R1 = [
            self.P[0],
            self.P[1],
            np.array([self.P[1][0], split_y, 0.0]),
            np.array([self.P[0][0], split_y, 0.0]),
        ]
        self.R1_w = abs(self.P[1][0] - self.P[0][0])  # = 4
        self.R1_h = abs(split_y - self.P[0][1])        # = 1.5

        # 上半矩形 R2: (P0.x, split_y), P3, P4, P5
        self.R2 = [
            np.array([self.P[0][0], split_y, 0.0]),
            self.P[3],
            self.P[4],
            self.P[5],
        ]
        self.R2_w = abs(self.P[3][0] - self.P[0][0])  # = 2
        self.R2_h = abs(self.P[4][1] - split_y)        # = 1.5

        # ===== 添补法: 大长方形 P0, P1, (P1.x, P4.y), P5 =====
        self.Big = [
            self.P[0],
            self.P[1],
            np.array([self.P[1][0], self.P[4][1], 0.0]),
            self.P[5],
        ]
        self.Big_w = abs(self.P[1][0] - self.P[0][0])  # = 4
        self.Big_h = abs(self.P[4][1] - self.P[0][1])   # = 3

        # 减去的矩形: P3, P2, (P1.x, P4.y), P4
        self.Sub = [
            self.P[3],
            self.P[2],
            np.array([self.P[1][0], self.P[4][1], 0.0]),
            self.P[4],
        ]
        self.Sub_w = abs(self.P[1][0] - self.P[3][0])  # = 2
        self.Sub_h = abs(self.P[4][1] - self.P[3][1])   # = 1.5

        # ===== 面积验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-9
        area_R1 = self.R1_w * self.R1_h   # 4 × 1.5 = 6
        area_R2 = self.R2_w * self.R2_h   # 2 × 1.5 = 3
        area_split = area_R1 + area_R2     # = 9

        area_big = self.Big_w * self.Big_h  # 4 × 3 = 12
        area_sub = self.Sub_w * self.Sub_h  # 2 × 1.5 = 3
        area_add = area_big - area_sub      # = 9

        assert abs(area_split - 9.0) < eps, f"分割法面积错误: {area_split}"
        assert abs(area_add - 9.0) < eps, f"添补法面积错误: {area_add}"
        assert abs(area_split - area_add) < eps, "两种方法结果不一致"
        print(f"✓ 几何验证通过: 分割法={area_split}, 添补法={area_add}")

    # ------------------------------------------------------------------
    # 辅助方法
    # ------------------------------------------------------------------

    def _l_shape(self, color=COLOR_SHAPE, fill_opacity=0.35, **kw):
        """L形组合图形"""
        return Polygon(
            *self.P,
            color=color, fill_color=color,
            fill_opacity=fill_opacity, stroke_width=3, **kw
        )

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "这个图形的面积", font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "怎么算？", font=FONT, font_size=52, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 显示L形
        self.main_shape = self._l_shape()
        self.play(Create(self.main_shape), run_time=1.2)

        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        shape_center = sum(self.P) / len(self.P)
        q.move_to(shape_center)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 展示图形并标注尺寸
    # ------------------------------------------------------------------

    def scene_2_show_shape(self):
        title = Text(
            "组合图形", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 标注尺寸
        # 底边 4
        dim_bottom = MathTex("4", font_size=28, color=WHITE)
        dim_bottom.move_to((self.P[0] + self.P[1]) / 2 + DOWN * 0.4)

        # 右边 1.5
        dim_right = MathTex("1.5", font_size=24, color=WHITE)
        dim_right.move_to((self.P[1] + self.P[2]) / 2 + RIGHT * 0.5)

        # 左边 3
        dim_left = MathTex("3", font_size=28, color=WHITE)
        dim_left.move_to((self.P[0] + self.P[5]) / 2 + LEFT * 0.4)

        # 上边 2
        dim_top = MathTex("2", font_size=28, color=WHITE)
        dim_top.move_to((self.P[4] + self.P[5]) / 2 + UP * 0.4)

        # 内部台阶 水平 2
        dim_step_h = MathTex("2", font_size=24, color=WHITE)
        dim_step_h.move_to((self.P[2] + self.P[3]) / 2 + UP * 0.35)

        # 内部台阶 竖直 1.5
        dim_step_v = MathTex("1.5", font_size=24, color=WHITE)
        dim_step_v.move_to((self.P[3] + self.P[4]) / 2 + LEFT * 0.5)

        dims = VGroup(dim_bottom, dim_right, dim_left, dim_top, dim_step_h, dim_step_v)
        self.play(*[FadeIn(d) for d in dims], run_time=0.6)

        desc = Text(
            "不是基本图形，不能直接算",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.5)
        self.play(Write(desc), run_time=0.6)

        hint = Text(
            "但可以转化成基本图形！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 4.3)
        self.play(Write(hint), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, dims, desc, hint)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 分割法
    # ------------------------------------------------------------------

    def scene_3_split_method(self):
        title = Text(
            "方法一：分割法", font=FONT, font_size=38,
            color=COLOR_R1, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        step1 = Text(
            "沿水平线分成两个长方形",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.2)
        self.play(Write(step1), run_time=0.5)

        # 画分割线
        split_y = self.P[3][1]
        cut_line = DashedLine(
            np.array([self.P[0][0], split_y, 0.0]),
            np.array([self.P[1][0], split_y, 0.0]),
            color=COLOR_CUT, dash_length=0.12, stroke_width=3
        )
        self.play(Create(cut_line), run_time=0.6)
        self.wait(0.3)

        # 下半矩形 R1 高亮
        r1 = Polygon(*self.R1, color=COLOR_R1, fill_color=COLOR_R1,
                      fill_opacity=0.4, stroke_width=2.5)
        r1_label = VGroup(
            MathTex(r"4 \times 1.5 = 6", font_size=24, color=COLOR_R1),
        ).move_to(r1.get_center())

        self.play(FadeIn(r1), run_time=0.5)
        self.play(FadeIn(r1_label), run_time=0.4)

        # 上半矩形 R2 高亮
        r2 = Polygon(*self.R2, color=COLOR_R2, fill_color=COLOR_R2,
                      fill_opacity=0.4, stroke_width=2.5)
        r2_label = VGroup(
            MathTex(r"2 \times 1.5 = 3", font_size=24, color=COLOR_R2),
        ).move_to(r2.get_center())

        self.play(FadeIn(r2), run_time=0.5)
        self.play(FadeIn(r2_label), run_time=0.4)
        self.wait(0.5)

        # 总面积
        step2 = VGroup(
            Text("总面积 = ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"6 + 3 = 9", font_size=32, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.5)

        self.play(
            FadeOut(step1),
            FadeIn(step2, shift=UP * 0.2),
            run_time=0.5
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(title, cut_line, r1, r1_label, r2, r2_label, step2)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 添补法
    # ------------------------------------------------------------------

    def scene_4_add_method(self):
        title = Text(
            "方法二：添补法", font=FONT, font_size=38,
            color=COLOR_BIG, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        step1 = Text(
            "补成一个大长方形",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.2)
        self.play(Write(step1), run_time=0.5)

        # 大长方形
        big_rect = Polygon(*self.Big, color=COLOR_BIG, fill_color=COLOR_BIG,
                            fill_opacity=0.2, stroke_width=3)
        big_label = MathTex(r"4 \times 3 = 12", font_size=26, color=COLOR_BIG)
        big_label.move_to(big_rect.get_center() + DOWN * 0.5)

        self.play(Create(big_rect), run_time=0.8)
        self.play(FadeIn(big_label), run_time=0.4)
        self.wait(0.3)

        # 减去右上角
        step2 = Text(
            "减去右上角补充的部分",
            font=FONT, font_size=26, color=COLOR_SUB
        ).move_to(DOWN * 3.2)
        self.play(
            FadeOut(step1),
            FadeIn(step2, shift=UP * 0.2),
            run_time=0.4
        )

        sub_rect = Polygon(*self.Sub, color=COLOR_SUB, fill_color=COLOR_SUB,
                            fill_opacity=0.5, stroke_width=2.5)
        sub_label = MathTex(r"2 \times 1.5 = 3", font_size=22, color=COLOR_SUB)
        sub_label.move_to(sub_rect.get_center())

        self.play(FadeIn(sub_rect), run_time=0.5)
        self.play(FadeIn(sub_label), run_time=0.4)
        self.wait(0.5)

        # 总面积
        step3 = VGroup(
            Text("总面积 = ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"12 - 3 = 9", font_size=32, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.5)

        self.play(
            FadeOut(step2),
            FadeIn(step3, shift=UP * 0.2),
            run_time=0.5
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(title, big_rect, big_label, sub_rect, sub_label, step3)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 策略对比总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        # 淡出主图形
        self.play(FadeOut(self.main_shape), run_time=0.3)

        # 公式框
        box = RoundedRectangle(
            width=8.0, height=5.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        # 标题
        sum_title = Text(
            "组合图形面积的两种策略", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.8)
        self.play(Write(sum_title), run_time=0.5)

        # 分割法
        m1_title = Text("分割法", font=FONT, font_size=28, color=COLOR_R1, weight=BOLD)
        m1_desc = Text("分成几个基本图形", font=FONT, font_size=22, color=GRAY_A)
        m1_formula = Text("总面积 = 各部分面积之和", font=FONT, font_size=22, color=WHITE)
        m1 = VGroup(m1_title, m1_desc, m1_formula).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        m1.move_to(UP * 1.3 + LEFT * 0.3)

        self.play(FadeIn(m1, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)

        # 分隔线
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY, stroke_width=1).move_to(UP * 0.1)
        self.play(Create(sep), run_time=0.3)

        # 添补法
        m2_title = Text("添补法", font=FONT, font_size=28, color=COLOR_BIG, weight=BOLD)
        m2_desc = Text("补成一个大图形再减", font=FONT, font_size=22, color=GRAY_A)
        m2_formula = Text("总面积 = 大图形 - 补充部分", font=FONT, font_size=22, color=WHITE)
        m2 = VGroup(m2_title, m2_desc, m2_formula).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        m2.move_to(DOWN * 1.2 + LEFT * 0.3)

        self.play(FadeIn(m2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)

        # 提示
        tip = Text(
            "根据图形特点灵活选择！",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, m1, sep, m2, tip)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
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

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 004_组合图形的面积.py CompositeAreaLesson
#   高质量:    manim -qh  004_组合图形的面积.py CompositeAreaLesson
#   4K:        manim -qk  004_组合图形的面积.py CompositeAreaLesson
# ======================================================================

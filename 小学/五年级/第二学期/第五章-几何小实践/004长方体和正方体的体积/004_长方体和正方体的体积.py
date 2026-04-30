"""
004_长方体和正方体的体积.py — 长方体和正方体的体积 教学动画

知识点:
  - 长方体体积 V = a x b x h = S底 x h (用单位立方体摆满推导)
  - 正方体体积 V = a^3
  - 体积单位进率: 1m^3 = 1000dm^3, 1dm^3 = 1000cm^3
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 长方体体积: V = 长 x 宽 x 高 = abh
  2. 统一公式: V = 底面积 x 高 = Sh
  3. 正方体体积: V = 棱长^3 = a^3
  4. 体积单位进率: 1m^3=1000dm^3, 1dm^3=1000cm^3
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
COLOR_BOX = "#3b82f6"       # 蓝色长方体
COLOR_CUBE = "#ef4444"      # 红色正方体
COLOR_UNIT = "#22c55e"      # 绿色单位立方体
COLOR_LENGTH = "#f59e0b"    # 橙色长
COLOR_WIDTH = "#fb923c"     # 浅橙宽
COLOR_HEIGHT = "#a78bfa"    # 紫色高
COLOR_HL = "#fbbf24"        # 黄色高亮
COLOR_CONV = "#38bdf8"      # 天蓝色进率
COLOR_AUTHOR = "#6b7280"    # 灰色作者
FONT = "PingFang SC"


# ======================================================================
# 辅助: 2D 等轴测长方体 / 正方体
# ======================================================================

def box_2d(a, b, h, color, fill_opacity=0.25, stroke_width=2.5):
    """
    用三个平行四边形模拟等轴测长方体 (2D).
    a=长(x向右), b=宽(右上), h=高(向上)
    返回 VGroup(front, top, side)
    """
    dx = np.array([1.0, 0.0, 0.0])
    dy = np.array([0.5, 0.35, 0.0])
    dz = np.array([0.0, 1.0, 0.0])

    O = ORIGIN
    A = O + a * dx
    B = O + a * dx + b * dy
    C = O + b * dy

    front = Polygon(
        O, A, A + h * dz, O + h * dz,
        color=color, fill_color=color,
        fill_opacity=fill_opacity, stroke_width=stroke_width
    )
    top = Polygon(
        O + h * dz, A + h * dz, B + h * dz, C + h * dz,
        color=color, fill_color=color,
        fill_opacity=fill_opacity * 0.6, stroke_width=stroke_width
    )
    side = Polygon(
        A, B, B + h * dz, A + h * dz,
        color=color, fill_color=color,
        fill_opacity=fill_opacity * 0.8, stroke_width=stroke_width
    )
    return VGroup(front, top, side)


def cube_2d(a, color, fill_opacity=0.25, stroke_width=2.5):
    """正方体 = 等边长方体"""
    return box_2d(a, a, a, color, fill_opacity, stroke_width)


# ======================================================================
# 主场景
# ======================================================================

class VolumeLesson(Scene):
    """
    长方体和正方体的体积教学动画
    Scene 1: 开场钩子 — 体积怎么算？
    Scene 2: 长方体体积公式 (单位立方体推导)
    Scene 3: 正方体体积公式
    Scene 4: 体积单位进率
    Scene 5: 公式总结
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_rectangular_prism()
        self.scene_3_cube_formula()
        self.scene_4_unit_conversion()
        self.scene_5_formula_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 如何计算长方体和正方体的体积？"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "长方体和正方体", font=FONT, font_size=44, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "体积怎么算？", font=FONT, font_size=52,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示一个长方体和一个正方体
        box = box_2d(2.2, 1.0, 1.6, COLOR_BOX, fill_opacity=0.30)
        box.move_to(LEFT * 1.8 + DOWN * 0.2)
        cube = cube_2d(1.5, COLOR_CUBE, fill_opacity=0.30)
        cube.move_to(RIGHT * 1.8 + DOWN * 0.2)

        self.play(Create(box), run_time=1.0)
        self.play(Create(cube), run_time=1.0)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 2.8)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子
        self.play(FadeOut(VGroup(hook1, hook2, q, box, cube)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 长方体体积公式
    # ------------------------------------------------------------------

    def scene_2_rectangular_prism(self):
        """用单位立方体摆满推导 V = a x b x h = S底 x h"""

        title = Text(
            "长方体的体积", font=FONT, font_size=38,
            color=COLOR_BOX, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 思路说明
        intro = Text(
            "用单位立方体摆满长方体",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.3)
        self.play(Write(intro), run_time=0.6)

        # 创建一个 4 x 3 的小方块网格 (第一层)
        cols, rows = 4, 3
        unit_size = 0.55
        base_origin = np.array([-1.6, -0.8, 0.0])

        # 等轴测方向
        dx = np.array([1.0, 0.0, 0.0]) * unit_size
        dy = np.array([0.5, 0.35, 0.0]) * unit_size
        dz = np.array([0.0, unit_size, 0.0])

        layer1_label = Text(
            "第一层: 每行4个, 3行",
            font=FONT, font_size=22, color=COLOR_UNIT
        ).move_to(DOWN * 3.5)
        self.play(Write(layer1_label), run_time=0.5)

        layer1_cubes = VGroup()
        for r in range(rows):
            for c in range(cols):
                sq = Square(
                    side_length=unit_size * 0.88,
                    color=COLOR_UNIT, fill_color=COLOR_UNIT,
                    fill_opacity=0.30, stroke_width=1.5
                )
                sq.move_to(base_origin + c * dx + r * dy)
                layer1_cubes.add(sq)

        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.5) for c in layer1_cubes],
                lag_ratio=0.04
            ),
            run_time=1.2
        )
        self.wait(0.4)

        # 计数说明
        count1 = VGroup(
            MathTex("4", font_size=30, color=COLOR_LENGTH),
            Text(" x ", font=FONT, font_size=24, color=WHITE),
            MathTex("3", font_size=30, color=COLOR_WIDTH),
            Text(" = ", font=FONT, font_size=24, color=WHITE),
            MathTex("12", font_size=34, color=COLOR_HL),
            Text(" 个", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 4.5)
        self.play(FadeIn(count1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 第二层
        layer2_label = Text(
            "摞2层", font=FONT, font_size=22, color=COLOR_HEIGHT
        ).move_to(DOWN * 3.5)

        layer2_cubes = VGroup()
        for r in range(rows):
            for c in range(cols):
                sq = Square(
                    side_length=unit_size * 0.88,
                    color=COLOR_UNIT, fill_color=COLOR_UNIT,
                    fill_opacity=0.20, stroke_width=1.0
                )
                sq.move_to(base_origin + c * dx + r * dy + dz)
                layer2_cubes.add(sq)

        self.play(
            ReplacementTransform(layer1_label, layer2_label),
            LaggedStart(
                *[FadeIn(c, scale=0.5) for c in layer2_cubes],
                lag_ratio=0.04
            ),
            run_time=1.0
        )

        count2 = VGroup(
            MathTex("12", font_size=30, color=COLOR_HL),
            Text(" x ", font=FONT, font_size=24, color=WHITE),
            MathTex("2", font_size=30, color=COLOR_HEIGHT),
            Text(" = ", font=FONT, font_size=24, color=WHITE),
            MathTex("24", font_size=34, color=COLOR_HL),
            Text(" 个", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 5.3)
        self.play(FadeIn(count2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # 清除单位方块, 展示长方体外框
        self.play(
            FadeOut(VGroup(
                layer1_cubes, layer2_cubes, count1, count2, layer2_label
            )),
            run_time=0.4
        )

        # 绘制长方体外框并标注 长, 宽, 高
        main_box = box_2d(2.8, 1.4, 1.8, COLOR_BOX, fill_opacity=0.20, stroke_width=3)
        main_box.move_to(DOWN * 0.3)
        self.play(Create(main_box), run_time=0.8)

        lbl_a = VGroup(
            Text("长 ", font=FONT, font_size=24, color=COLOR_LENGTH),
            MathTex("a", font_size=30, color=COLOR_LENGTH)
        ).arrange(RIGHT, buff=0.04).next_to(main_box, DOWN, buff=0.35)

        lbl_b = VGroup(
            Text("宽 ", font=FONT, font_size=24, color=COLOR_WIDTH),
            MathTex("b", font_size=30, color=COLOR_WIDTH)
        ).arrange(RIGHT, buff=0.04).next_to(main_box, RIGHT, buff=0.35).shift(DOWN * 0.3)

        lbl_h = VGroup(
            Text("高 ", font=FONT, font_size=24, color=COLOR_HEIGHT),
            MathTex("h", font_size=30, color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.04).next_to(main_box, LEFT, buff=0.35).shift(UP * 0.2)

        self.play(FadeIn(lbl_a), FadeIn(lbl_b), FadeIn(lbl_h), run_time=0.6)
        self.wait(0.5)

        # 公式推导
        derive_text = Text(
            "每行个数 x 行数 x 层数",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.5)
        self.play(Write(derive_text), run_time=0.5)

        formula1_lhs = Text("V = ", font=FONT, font_size=36, color=WHITE)
        formula1_rhs = MathTex(
            r"a \times b \times h", font_size=40, color=COLOR_HL
        )
        formula1 = VGroup(formula1_lhs, formula1_rhs).arrange(RIGHT, buff=0.1)
        formula1.move_to(DOWN * 4.5)
        self.play(FadeIn(formula1, shift=UP * 0.3), run_time=0.7)
        self.wait(0.6)

        # V = Sh 形式
        or_text = Text(
            "也就是", font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 5.3)

        formula2_lhs = Text("V = ", font=FONT, font_size=36, color=WHITE)
        formula2_s = Text("S", font=FONT, font_size=32, color=COLOR_LENGTH)
        formula2_di = Text("底", font=FONT, font_size=16, color=COLOR_LENGTH)
        formula2_di.next_to(formula2_s, DR, buff=0.02).shift(UP * 0.08)
        formula2_sg = VGroup(formula2_s, formula2_di)
        formula2_h = MathTex(r"\times h", font_size=36, color=COLOR_HEIGHT)
        formula2 = VGroup(
            formula2_lhs, formula2_sg, formula2_h
        ).arrange(RIGHT, buff=0.1)
        formula2.move_to(DOWN * 6.0)

        self.play(Write(or_text), run_time=0.3)
        self.play(FadeIn(formula2, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, intro, main_box, lbl_a, lbl_b, lbl_h,
                derive_text, formula1, or_text, formula2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 正方体体积公式
    # ------------------------------------------------------------------

    def scene_3_cube_formula(self):
        """正方体 V = a^3"""

        title = Text(
            "正方体的体积", font=FONT, font_size=38,
            color=COLOR_CUBE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        intro = Text(
            "正方体的长、宽、高都相等",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.3)
        self.play(Write(intro), run_time=0.6)

        # 正方体
        cube = cube_2d(2.0, COLOR_CUBE, fill_opacity=0.28, stroke_width=3)
        cube.move_to(DOWN * 0.0)
        self.play(Create(cube), run_time=1.0)

        # 三条棱标注 a
        lbl_a1 = MathTex(
            "a", font_size=32, color=COLOR_LENGTH
        ).next_to(cube, DOWN, buff=0.3)
        lbl_a2 = MathTex(
            "a", font_size=32, color=COLOR_WIDTH
        ).next_to(cube, RIGHT, buff=0.35).shift(DOWN * 0.3)
        lbl_a3 = MathTex(
            "a", font_size=32, color=COLOR_HEIGHT
        ).next_to(cube, LEFT, buff=0.35).shift(UP * 0.2)

        self.play(FadeIn(lbl_a1), FadeIn(lbl_a2), FadeIn(lbl_a3), run_time=0.5)
        self.wait(0.4)

        # 从长方体公式推到正方体公式
        step1_lhs = Text("V = ", font=FONT, font_size=34, color=WHITE)
        step1_rhs = MathTex(
            r"a \times b \times h", font_size=38, color=GRAY_A
        )
        step1 = VGroup(step1_lhs, step1_rhs).arrange(RIGHT, buff=0.1)
        step1.move_to(DOWN * 3.5)
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.5)

        arrow_note = Text(
            "长=宽=高=a", font=FONT, font_size=22, color=COLOR_CUBE
        ).move_to(DOWN * 4.3)
        self.play(Write(arrow_note), run_time=0.4)

        step2_lhs = Text("V = ", font=FONT, font_size=34, color=WHITE)
        step2_rhs = MathTex(
            r"a \times a \times a", font_size=38, color=COLOR_HL
        )
        step2 = VGroup(step2_lhs, step2_rhs).arrange(RIGHT, buff=0.1)
        step2.move_to(DOWN * 5.2)
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)

        # 最终形式 V = a^3
        step3_lhs = Text("V = ", font=FONT, font_size=44, color=WHITE)
        step3_rhs = MathTex(r"a^3", font_size=52, color=COLOR_HL)
        step3 = VGroup(step3_lhs, step3_rhs).arrange(RIGHT, buff=0.1)
        step3.move_to(DOWN * 6.2)

        box_rect = SurroundingRectangle(
            step3, color=COLOR_CUBE, stroke_width=2.5,
            buff=0.15, corner_radius=0.1
        )
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.6)
        self.play(Create(box_rect), run_time=0.4)

        note = Text(
            "读作 a 的立方", font=FONT, font_size=20, color=COLOR_CUBE
        ).move_to(DOWN * 7.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, intro, cube, lbl_a1, lbl_a2, lbl_a3,
                step1, arrow_note, step2, step3, box_rect, note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 体积单位进率
    # ------------------------------------------------------------------

    def scene_4_unit_conversion(self):
        """1m^3 = 1000dm^3, 1dm^3 = 1000cm^3"""

        title = Text(
            "体积单位的进率", font=FONT, font_size=38,
            color=COLOR_CONV, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        reason = Text(
            "相邻单位间进率是1000",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.3)
        self.play(Write(reason), run_time=0.6)

        reason2 = Text(
            "因为三个方向各进率10",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 3.5)
        self.play(Write(reason2), run_time=0.5)

        calc = MathTex(
            r"10 \times 10 \times 10 = 1000",
            font_size=36, color=COLOR_CONV
        ).move_to(UP * 2.5)
        self.play(Write(calc), run_time=0.7)
        self.wait(0.6)

        # 第一组: 1m^3 = 1000dm^3
        conv1_box = RoundedRectangle(
            width=7.4, height=2.0,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_CONV, stroke_width=2.5
        ).move_to(DOWN * 0.3)

        conv1_lhs = MathTex(r"1 \text{m}^3", font_size=44, color=WHITE)
        conv1_eq = Text(" = ", font=FONT, font_size=36, color=WHITE)
        conv1_rhs = MathTex(
            r"1000 \text{dm}^3", font_size=44, color=COLOR_HL
        )
        conv1 = VGroup(conv1_lhs, conv1_eq, conv1_rhs).arrange(
            RIGHT, buff=0.15
        )
        conv1.move_to(DOWN * 0.3)

        self.play(FadeIn(conv1_box), run_time=0.3)
        self.play(Write(conv1), run_time=0.8)
        self.wait(0.5)

        # 第二组: 1dm^3 = 1000cm^3
        conv2_box = RoundedRectangle(
            width=7.4, height=2.0,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_CONV, stroke_width=2.5
        ).move_to(DOWN * 3.0)

        conv2_lhs = MathTex(r"1 \text{dm}^3", font_size=44, color=WHITE)
        conv2_eq = Text(" = ", font=FONT, font_size=36, color=WHITE)
        conv2_rhs = MathTex(
            r"1000 \text{cm}^3", font_size=44, color=COLOR_HL
        )
        conv2 = VGroup(conv2_lhs, conv2_eq, conv2_rhs).arrange(
            RIGHT, buff=0.15
        )
        conv2.move_to(DOWN * 3.0)

        self.play(FadeIn(conv2_box), run_time=0.3)
        self.play(Write(conv2), run_time=0.8)
        self.wait(0.5)

        # 比较提示
        tip = Text(
            "面积单位进率100, 长度进率10",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)

        tip2 = Text(
            "记住: 体积单位进率1000",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(tip2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, reason, reason2, calc,
                conv1_box, conv1, conv2_box, conv2, tip, tip2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式总结
    # ------------------------------------------------------------------

    def scene_5_formula_summary(self):
        """大字公式总结: 长方体 + 正方体 + 进率"""

        title = Text(
            "公式总结", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 长方体公式框 =====
        box1 = RoundedRectangle(
            width=7.8, height=3.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_BOX, stroke_width=3
        ).move_to(UP * 2.5)

        box1_title = Text(
            "长方体体积", font=FONT, font_size=28, color=COLOR_BOX
        ).move_to(UP * 3.6)

        f1_line1_lhs = Text("V = ", font=FONT, font_size=40, color=WHITE)
        f1_line1_rhs = MathTex(
            r"a \times b \times h", font_size=44, color=COLOR_HL
        )
        f1_line1 = VGroup(f1_line1_lhs, f1_line1_rhs).arrange(
            RIGHT, buff=0.1
        ).move_to(UP * 2.6)

        f1_line2_lhs = Text("V = ", font=FONT, font_size=36, color=WHITE)
        f1_line2_s = Text("S", font=FONT, font_size=30, color=COLOR_LENGTH)
        f1_line2_di = Text("底", font=FONT, font_size=16, color=COLOR_LENGTH)
        f1_line2_di.next_to(f1_line2_s, DR, buff=0.02).shift(UP * 0.06)
        f1_line2_sg = VGroup(f1_line2_s, f1_line2_di)
        f1_line2_h = MathTex(
            r"\times h", font_size=36, color=COLOR_HEIGHT
        )
        f1_line2 = VGroup(
            f1_line2_lhs, f1_line2_sg, f1_line2_h
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.6)

        self.play(FadeIn(box1), run_time=0.3)
        self.play(Write(box1_title), run_time=0.4)
        self.play(Write(f1_line1), run_time=0.8)
        self.play(Write(f1_line2), run_time=0.6)
        self.wait(0.5)

        # ===== 正方体公式框 =====
        box2 = RoundedRectangle(
            width=7.8, height=2.4, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_CUBE, stroke_width=3
        ).move_to(DOWN * 0.8)

        box2_title = Text(
            "正方体体积", font=FONT, font_size=28, color=COLOR_CUBE
        ).move_to(UP * 0.0)

        f2_lhs = Text("V = ", font=FONT, font_size=44, color=WHITE)
        f2_rhs = MathTex(r"a^3", font_size=52, color=COLOR_HL)
        f2 = VGroup(f2_lhs, f2_rhs).arrange(
            RIGHT, buff=0.1
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(box2), run_time=0.3)
        self.play(Write(box2_title), run_time=0.4)
        self.play(Write(f2), run_time=0.8)
        self.wait(0.5)

        # ===== 进率框 =====
        box3 = RoundedRectangle(
            width=7.8, height=2.6, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_CONV, stroke_width=3
        ).move_to(DOWN * 4.0)

        box3_title = Text(
            "体积单位进率", font=FONT, font_size=28, color=COLOR_CONV
        ).move_to(DOWN * 3.0)

        c1_lhs = MathTex(r"1 \text{m}^3", font_size=34, color=WHITE)
        c1_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        c1_rhs = MathTex(
            r"1000 \text{dm}^3", font_size=34, color=COLOR_HL
        )
        c1 = VGroup(c1_lhs, c1_eq, c1_rhs).arrange(
            RIGHT, buff=0.1
        ).move_to(DOWN * 3.8)

        c2_lhs = MathTex(r"1 \text{dm}^3", font_size=34, color=WHITE)
        c2_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        c2_rhs = MathTex(
            r"1000 \text{cm}^3", font_size=34, color=COLOR_HL
        )
        c2 = VGroup(c2_lhs, c2_eq, c2_rhs).arrange(
            RIGHT, buff=0.1
        ).move_to(DOWN * 4.8)

        self.play(FadeIn(box3), run_time=0.3)
        self.play(Write(box3_title), run_time=0.4)
        self.play(Write(c1), run_time=0.5)
        self.play(Write(c2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, box1, box1_title, f1_line1, f1_line2,
                box2, box2_title, f2,
                box3, box3_title, c1, c2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示 + 装饰"""

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

        # 装饰: 6个小方块围绕旋转
        colors = [COLOR_BOX, COLOR_CUBE, COLOR_UNIT,
                  COLOR_LENGTH, COLOR_HEIGHT, COLOR_HL]
        mini_cubes = VGroup(*[
            Square(
                side_length=0.35,
                fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).rotate(i * PI / 6).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(
            *[FadeIn(t, scale=0.3) for t in mini_cubes],
            run_time=0.5
        )
        self.play(
            Rotate(
                mini_cubes, angle=2 * PI / 3,
                run_time=1.2, rate_func=smooth
            )
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(
                self.author_mob, author_id, follow, mini_cubes
            )),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -pql 004_长方体和正方体的体积.py VolumeLesson
#   高质量:   manim -qh  004_长方体和正方体的体积.py VolumeLesson
#   4K:       manim -qk  004_长方体和正方体的体积.py VolumeLesson
# ======================================================================

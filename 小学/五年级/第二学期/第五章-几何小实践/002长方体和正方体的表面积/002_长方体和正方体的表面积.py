"""
002_长方体和正方体的表面积.py — 表面积 教学动画

知识点: 长方体和正方体表面积公式的推导与应用
  - 表面积 = 6个面的总面积
  - 长方体: S = 2(ab + ah + bh)
  - 正方体: S = 6a²
  - 应用: 无盖箱子(5面)、包装纸等
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR     = "#1a1a2e"
COLOR_FRONT  = "#3b82f6"   # 蓝色 前/后面
COLOR_SIDE   = "#ef4444"   # 红色 左/右面
COLOR_TOP    = "#22c55e"   # 绿色 上/下面
COLOR_EDGE   = "#f59e0b"   # 橙色 棱
COLOR_DIM    = "#a78bfa"   # 紫色 尺寸标注
COLOR_HL     = "#fbbf24"   # 黄色 高亮
COLOR_CUBE   = "#06b6d4"   # 青色 正方体
COLOR_AUTHOR = "#6b7280"   # 灰色 作者
FONT         = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class SurfaceAreaLesson(Scene):
    """
    长方体和正方体的表面积教学动画
    Scene 1: 开场钩子
    Scene 2: 概念 — 6个面展开
    Scene 3: 长方体表面积公式
    Scene 4: 正方体表面积公式
    Scene 5: 公式总结
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_six_faces()
        self.scene_3_rectangular_formula()
        self.scene_4_cube_formula()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 辅助: 创建长方体展开图的6个面 (2D矩形)
    # ------------------------------------------------------------------

    def _make_rect_face(self, w, h, color, fill_opacity=0.35):
        """创建一个填充矩形面"""
        return Rectangle(
            width=w, height=h,
            color=color, fill_color=color,
            fill_opacity=fill_opacity, stroke_width=2.5
        )

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '包装一个礼物盒，需要多少纸？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "包装一个礼物盒", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "需要多少纸？", font=FONT, font_size=52,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 3D 长方体 (使用 Prism)
        box = Prism(
            dimensions=[2.5, 1.5, 1.8],
            fill_color=COLOR_FRONT, fill_opacity=0.3,
            stroke_color=COLOR_EDGE, stroke_width=2.5
        ).move_to(DOWN * 0.5)
        box.rotate(PI / 7, axis=UP).rotate(PI / 12, axis=RIGHT)

        self.play(Create(box), run_time=1.2)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(box.get_center() + UP * 0.3)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子
        self.play(FadeOut(VGroup(hook1, hook2, q, box)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 概念 — 6个面
    # ------------------------------------------------------------------

    def scene_2_six_faces(self):
        """展示长方体有6个面，表面积 = 6个面面积之和"""

        title = Text(
            "表面积 = 6个面的总面积", font=FONT,
            font_size=36, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义尺寸: 长 a=2.4, 宽 b=1.6, 高 h=1.2
        a, b, h = 2.4, 1.6, 1.2

        # 创建展开图 (十字形排列)
        # 中间一排: 左、前、右、后
        # 上下: 上、下
        front  = self._make_rect_face(a, h, COLOR_FRONT, 0.45)
        back   = self._make_rect_face(a, h, COLOR_FRONT, 0.45)
        left   = self._make_rect_face(b, h, COLOR_SIDE,  0.45)
        right  = self._make_rect_face(b, h, COLOR_SIDE,  0.45)
        top    = self._make_rect_face(a, b, COLOR_TOP,   0.45)
        bottom = self._make_rect_face(a, b, COLOR_TOP,   0.45)

        # 布局: 十字形
        gap = 0.08
        center_y = 0.0

        front.move_to(ORIGIN + UP * center_y)
        left.next_to(front, LEFT, buff=gap)
        right.next_to(front, RIGHT, buff=gap)
        back.next_to(right, RIGHT, buff=gap)
        top.next_to(front, UP, buff=gap)
        bottom.next_to(front, DOWN, buff=gap)

        all_faces = VGroup(front, back, left, right, top, bottom)

        # 面标签
        labels_data = [
            (front,  "前"),
            (back,   "后"),
            (left,   "左"),
            (right,  "右"),
            (top,    "上"),
            (bottom, "下"),
        ]
        face_labels = VGroup()
        for face, name in labels_data:
            lbl = Text(name, font=FONT, font_size=22, color=WHITE)
            lbl.move_to(face.get_center())
            face_labels.add(lbl)

        # 逐个展示6个面
        self.play(FadeIn(front), FadeIn(face_labels[0]), run_time=0.4)
        self.play(FadeIn(back),  FadeIn(face_labels[1]), run_time=0.4)
        self.play(FadeIn(left),  FadeIn(face_labels[2]), run_time=0.4)
        self.play(FadeIn(right), FadeIn(face_labels[3]), run_time=0.4)
        self.play(FadeIn(top),   FadeIn(face_labels[4]), run_time=0.4)
        self.play(FadeIn(bottom),FadeIn(face_labels[5]), run_time=0.4)
        self.wait(0.5)

        # 相同颜色配对说明
        pair_note1 = Text(
            "前后 两面相同", font=FONT, font_size=24, color=COLOR_FRONT
        ).move_to(DOWN * 3.5)
        pair_note2 = Text(
            "左右 两面相同", font=FONT, font_size=24, color=COLOR_SIDE
        ).move_to(DOWN * 4.2)
        pair_note3 = Text(
            "上下 两面相同", font=FONT, font_size=24, color=COLOR_TOP
        ).move_to(DOWN * 4.9)

        self.play(
            Indicate(front, color=COLOR_FRONT, scale_factor=1.08),
            Indicate(back,  color=COLOR_FRONT, scale_factor=1.08),
            FadeIn(pair_note1, shift=UP * 0.2),
            run_time=0.7
        )
        self.play(
            Indicate(left,  color=COLOR_SIDE, scale_factor=1.08),
            Indicate(right, color=COLOR_SIDE, scale_factor=1.08),
            FadeIn(pair_note2, shift=UP * 0.2),
            run_time=0.7
        )
        self.play(
            Indicate(top,    color=COLOR_TOP, scale_factor=1.08),
            Indicate(bottom, color=COLOR_TOP, scale_factor=1.08),
            FadeIn(pair_note3, shift=UP * 0.2),
            run_time=0.7
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, all_faces, face_labels,
                pair_note1, pair_note2, pair_note3
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 长方体表面积公式
    # ------------------------------------------------------------------

    def scene_3_rectangular_formula(self):
        """推导长方体表面积: S = 2(ab + ah + bh)"""

        title = Text(
            "长方体表面积公式", font=FONT,
            font_size=38, color=COLOR_FRONT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 3D 长方体
        box = Prism(
            dimensions=[2.8, 1.6, 2.0],
            fill_color=COLOR_FRONT, fill_opacity=0.2,
            stroke_color=COLOR_EDGE, stroke_width=2.5
        ).move_to(UP * 1.5)
        box.rotate(PI / 6, axis=UP).rotate(PI / 10, axis=RIGHT)
        self.play(Create(box), run_time=1.0)

        # 尺寸标注 (使用 Text 显示中文+变量)
        lbl_a = VGroup(
            Text("长 ", font=FONT, font_size=24, color=COLOR_DIM),
            MathTex("a", font_size=30, color=COLOR_DIM)
        ).arrange(RIGHT, buff=0.04).move_to(UP * 0.0 + LEFT * 0.3)

        lbl_b = VGroup(
            Text("宽 ", font=FONT, font_size=24, color=COLOR_DIM),
            MathTex("b", font_size=30, color=COLOR_DIM)
        ).arrange(RIGHT, buff=0.04).move_to(UP * 0.0 + RIGHT * 2.2)

        lbl_h = VGroup(
            Text("高 ", font=FONT, font_size=24, color=COLOR_DIM),
            MathTex("h", font_size=30, color=COLOR_DIM)
        ).arrange(RIGHT, buff=0.04).move_to(UP * 2.6 + RIGHT * 2.0)

        self.play(
            FadeIn(lbl_a), FadeIn(lbl_b), FadeIn(lbl_h),
            run_time=0.6
        )
        self.wait(0.5)

        # 三对面的面积
        face1_text = VGroup(
            Text("前后面积: ", font=FONT, font_size=22, color=COLOR_FRONT),
            MathTex(r"2 \times a \times h", font_size=28, color=COLOR_FRONT)
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 2.2)

        face2_text = VGroup(
            Text("左右面积: ", font=FONT, font_size=22, color=COLOR_SIDE),
            MathTex(r"2 \times b \times h", font_size=28, color=COLOR_SIDE)
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 3.0)

        face3_text = VGroup(
            Text("上下面积: ", font=FONT, font_size=22, color=COLOR_TOP),
            MathTex(r"2 \times a \times b", font_size=28, color=COLOR_TOP)
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 3.8)

        self.play(FadeIn(face1_text, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(face2_text, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(face3_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 合并公式
        formula_label = Text(
            "表面积 S = ", font=FONT, font_size=28, color=WHITE
        )
        formula_math = MathTex(
            r"2(ab + ah + bh)",
            font_size=40, color=COLOR_HL
        )
        formula = VGroup(formula_label, formula_math).arrange(RIGHT, buff=0.1)
        formula.move_to(DOWN * 5.2)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.8, height=1.6,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(formula.get_center())

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula), run_time=0.9)

        # 高亮闪烁
        self.play(
            Indicate(formula_math, color=COLOR_HL, scale_factor=1.1),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, box, lbl_a, lbl_b, lbl_h,
                face1_text, face2_text, face3_text,
                formula_box, formula
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 正方体表面积公式
    # ------------------------------------------------------------------

    def scene_4_cube_formula(self):
        """正方体: 6个面全等 → S = 6a²"""

        title = Text(
            "正方体表面积公式", font=FONT,
            font_size=38, color=COLOR_CUBE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 正方体 (用Prism模拟)
        cube = Prism(
            dimensions=[2.0, 2.0, 2.0],
            fill_color=COLOR_CUBE, fill_opacity=0.2,
            stroke_color=COLOR_EDGE, stroke_width=2.5
        ).move_to(UP * 1.5)
        cube.rotate(PI / 6, axis=UP).rotate(PI / 10, axis=RIGHT)
        self.play(Create(cube), run_time=1.0)

        # 棱长标注
        lbl_edge = VGroup(
            Text("棱长 ", font=FONT, font_size=26, color=COLOR_CUBE),
            MathTex("a", font_size=32, color=COLOR_CUBE)
        ).arrange(RIGHT, buff=0.04).move_to(UP * 0.0)

        self.play(FadeIn(lbl_edge), run_time=0.5)
        self.wait(0.4)

        # 推导过程
        step1 = VGroup(
            Text("正方体: 长 = 宽 = 高 = ", font=FONT, font_size=22, color=WHITE),
            MathTex("a", font_size=28, color=COLOR_CUBE)
        ).arrange(RIGHT, buff=0.04).move_to(DOWN * 2.2)

        step2 = VGroup(
            Text("每个面面积 = ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"a \times a = a^2", font_size=28, color=COLOR_CUBE)
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 3.0)

        step3 = VGroup(
            Text("6个面全部相等", font=FONT, font_size=22, color=WHITE),
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(step3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.0, height=1.6,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_CUBE, stroke_width=3
        ).move_to(DOWN * 5.2)

        formula_label = Text(
            "S = ", font=FONT, font_size=40, color=WHITE
        )
        formula_math = MathTex(
            r"6a^2", font_size=52, color=COLOR_CUBE
        )
        formula = VGroup(formula_label, formula_math).arrange(RIGHT, buff=0.1)
        formula.move_to(DOWN * 5.2)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula), run_time=0.9)

        # 高亮
        self.play(
            Indicate(formula_math, color=COLOR_CUBE, scale_factor=1.1),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, cube, lbl_edge,
                step1, step2, step3,
                formula_box, formula
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        """并排展示两个公式 + 应用提示"""

        title = Text(
            "公式总结", font=FONT,
            font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 长方体公式卡片 =====
        card1_bg = RoundedRectangle(
            width=7.6, height=3.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_FRONT, stroke_width=2.5
        ).move_to(UP * 2.5)

        card1_title = Text(
            "长方体", font=FONT, font_size=30,
            color=COLOR_FRONT, weight=BOLD
        ).move_to(UP * 3.5)

        card1_formula_lbl = Text(
            "S = ", font=FONT, font_size=36, color=WHITE
        )
        card1_formula_math = MathTex(
            r"2(ab + ah + bh)", font_size=42, color=COLOR_HL
        )
        card1_formula = VGroup(card1_formula_lbl, card1_formula_math).arrange(
            RIGHT, buff=0.1
        ).move_to(UP * 2.5)

        card1_note = Text(
            "a=长  b=宽  h=高", font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 1.5)

        self.play(FadeIn(card1_bg), run_time=0.3)
        self.play(Write(card1_title), run_time=0.4)
        self.play(Write(card1_formula), run_time=0.8)
        self.play(FadeIn(card1_note), run_time=0.3)

        # ===== 正方体公式卡片 =====
        card2_bg = RoundedRectangle(
            width=7.6, height=3.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_CUBE, stroke_width=2.5
        ).move_to(DOWN * 1.2)

        card2_title = Text(
            "正方体", font=FONT, font_size=30,
            color=COLOR_CUBE, weight=BOLD
        ).move_to(DOWN * 0.2)

        card2_formula_lbl = Text(
            "S = ", font=FONT, font_size=36, color=WHITE
        )
        card2_formula_math = MathTex(
            r"6a^2", font_size=52, color=COLOR_CUBE
        )
        card2_formula = VGroup(card2_formula_lbl, card2_formula_math).arrange(
            RIGHT, buff=0.1
        ).move_to(DOWN * 1.2)

        card2_note = Text(
            "a=棱长", font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 2.2)

        self.play(FadeIn(card2_bg), run_time=0.3)
        self.play(Write(card2_title), run_time=0.4)
        self.play(Write(card2_formula), run_time=0.8)
        self.play(FadeIn(card2_note), run_time=0.3)
        self.wait(1.0)

        # ===== 应用提示 =====
        tip_box = RoundedRectangle(
            width=7.6, height=2.2,
            corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_EDGE, stroke_width=2
        ).move_to(DOWN * 4.8)

        tip_title = Text(
            "实际应用提示", font=FONT, font_size=22,
            color=COLOR_EDGE, weight=BOLD
        ).move_to(DOWN * 3.95)

        tip1 = Text(
            "无盖箱子 = 5个面 (减去上面)",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 4.7)
        tip2 = Text(
            "通风管道 = 4个面 (减去上下面)",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 5.3)

        self.play(FadeIn(tip_box), run_time=0.3)
        self.play(Write(tip_title), run_time=0.4)
        self.play(FadeIn(tip1, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(tip2, shift=UP * 0.2), run_time=0.4)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                card1_bg, card1_title, card1_formula, card1_note,
                card2_bg, card2_title, card2_formula, card2_note,
                tip_box, tip_title, tip1, tip2
            )),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示 + 小方块装饰"""

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

        # 装饰: 6个小方块围绕旋转 (象征6个面)
        colors = [COLOR_FRONT, COLOR_SIDE, COLOR_TOP,
                  COLOR_CUBE, COLOR_EDGE, COLOR_HL]
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
        self.play(*[FadeIn(s, scale=0.3) for s in mini_cubes], run_time=0.5)
        self.play(Rotate(mini_cubes, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_cubes)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -ql --disable_caching 002_长方体和正方体的表面积.py SurfaceAreaLesson
#   高质量:   manim -qh  002_长方体和正方体的表面积.py SurfaceAreaLesson
#   4K:       manim -qk  002_长方体和正方体的表面积.py SurfaceAreaLesson
# ======================================================================

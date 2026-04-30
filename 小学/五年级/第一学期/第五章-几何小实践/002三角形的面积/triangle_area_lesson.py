"""
triangle_area_lesson.py — 三角形的面积 教学动画

知识点: 通过拼合法推导三角形面积 = 底 × 高 ÷ 2
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

几何核心:
  T1: A(-2,0)  B(1,0)  C(-1,2.5)    底=3  高=2.5
  T2 绕 M_BC=(0,1.25) 旋转180° → A'(2,2.5)
  平行四边形: A → B → A' → C → A
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
COLOR_TRI1 = "#3b82f6"    # 蓝色 T1
COLOR_TRI2 = "#ef4444"    # 红色 T2
COLOR_PARA = "#22c55e"    # 绿色平行四边形
COLOR_BASE = "#f59e0b"    # 橙色底边
COLOR_HEIGHT = "#a78bfa"  # 紫色高
COLOR_HL = "#fbbf24"      # 黄色高亮
COLOR_AUTHOR = "#6b7280"  # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class TriangleAreaLesson(Scene):
    """
    三角形的面积教学动画
    场景顺序:
      1. 开场钩子
      2. 拼合法 (核心)
      3. 平行四边形面积
      4. 推导三角形公式
      5. 公式总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_merge_trick()
        self.scene_3_parallelogram_formula()
        self.scene_4_derivation()
        self.scene_5_formula_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 几何初始化 (所有坐标统一计算，不使用臆想值)
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""

        # ===== 三角形顶点 =====
        self.A = np.array([-2.0, 0.0, 0.0])   # 底边左端
        self.B = np.array([ 1.0, 0.0, 0.0])   # 底边右端
        self.C = np.array([-1.0, 2.5, 0.0])   # 顶点

        # ===== 关键派生点 (精确计算) =====
        self.M_BC = (self.B + self.C) / 2      # BC中点 = (0, 1.25, 0)  ← T2旋转轴
        self.A_prime = 2 * self.M_BC - self.A  # A关于M_BC的对称 = (2, 2.5, 0)

        # ===== 底和高 =====
        self.base_length = np.linalg.norm(self.B - self.A)   # = 3.0
        self.height_length = self.C[1] - self.A[1]           # = 2.5

        # ===== 高的垂足 (AB为y=0水平线，垂足同x坐标) =====
        self.H_foot = np.array([self.C[0], self.A[1], 0.0])  # = (-1, 0, 0)

        # ===== 中心点 =====
        self.tri_center = (self.A + self.B + self.C) / 3

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-9
        AB = self.B - self.A
        CA_prime = self.A_prime - self.C
        assert np.linalg.norm(AB - CA_prime) < eps, "平行四边形验证失败"
        assert abs(self.base_length - 3.0) < eps
        assert abs(self.height_length - 2.5) < eps
        assert self.A[0] <= self.H_foot[0] <= self.B[0], "垂足不在底边内"
        print("✓ 几何验证通过: 底=3.0, 高=2.5, 垂足在底边内")

    # ------------------------------------------------------------------
    # 辅助: 创建几何对象
    # ------------------------------------------------------------------

    def _tri1(self, fill_opacity=0.35, **kw):
        """蓝色主三角形 T1"""
        return Polygon(
            self.A, self.B, self.C,
            color=COLOR_TRI1, fill_color=COLOR_TRI1,
            fill_opacity=fill_opacity, stroke_width=3, **kw
        )

    def _tri2(self, fill_opacity=0.40, **kw):
        """红色副三角形 T2 (初始同 T1 位置)"""
        return Polygon(
            self.A, self.B, self.C,
            color=COLOR_TRI2, fill_color=COLOR_TRI2,
            fill_opacity=fill_opacity, stroke_width=3, **kw
        )

    def _para_outline(self, **kw):
        """平行四边形外轮廓 (无填充)"""
        return Polygon(
            self.A, self.B, self.A_prime, self.C,
            color=COLOR_PARA, stroke_width=4, fill_opacity=0, **kw
        )

    def _height_line(self):
        """从顶点C到垂足的虚线高"""
        return DashedLine(
            self.C, self.H_foot,
            color=COLOR_HEIGHT, dash_length=0.12, stroke_width=2.5
        )

    def _right_angle_mark(self, size=0.2):
        """垂足处的直角符号"""
        foot = self.H_foot
        # v_up: 沿高方向 (从 H_foot 向 C，即 +y 方向)
        # v_right: 沿底边方向 (+x 方向)
        v_up = np.array([0.0, size, 0.0])
        v_right = np.array([size, 0.0, 0.0])
        return Polygon(
            foot,
            foot + v_right,
            foot + v_right + v_up,
            foot + v_up,
            color=COLOR_HEIGHT, stroke_width=1.5, fill_opacity=0
        )

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '为什么三角形面积要 ÷ 2？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "为什么三角形面积", font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "要  ÷ 2 ？", font=FONT, font_size=52, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 主三角形
        self.main_tri = self._tri1()
        self.play(Create(self.main_tri), run_time=1.2)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(self.tri_center + UP * 0.2)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子，保留三角形
        self.play(FadeOut(VGroup(hook1, hook2, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 拼合法 — 核心动画
    # ------------------------------------------------------------------

    def scene_2_merge_trick(self):
        """两个三角形旋转拼合成平行四边形"""

        # 场景标题
        title = Text(
            "拼合法", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # Step 1: 出现第二个三角形
        step1 = Text(
            "复制一个完全相同的三角形",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(Write(step1), run_time=0.6)

        # T2 从中心生长出来 (与T1完全重合，红色)
        t2 = self._tri2()
        self.play(GrowFromCenter(t2), run_time=0.7)
        self.wait(0.4)

        # Step 2: 旋转提示
        step2 = Text(
            "将红色三角形旋转 180°",
            font=FONT, font_size=26, color=COLOR_TRI2
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(step1),
            FadeIn(step2, shift=UP * 0.2),
            run_time=0.4
        )
        self.wait(0.3)

        # ★ 核心动画: T2 绕 M_BC 旋转 180°
        # 旋转后 T2 顶点: A'(2,2.5), C(-1,2.5), B(1,0)
        # 与 T1 合并形成平行四边形 A(-2,0)→B(1,0)→A'(2,2.5)→C(-1,2.5)
        self.play(
            Rotate(t2, angle=PI, about_point=self.M_BC),
            run_time=2.0,
            rate_func=smooth
        )
        self.wait(0.4)

        # 平行四边形外轮廓亮起
        step3 = Text(
            "拼成了一个平行四边形！",
            font=FONT, font_size=30,
            color=COLOR_PARA, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(step2),
            FadeIn(step3, shift=UP * 0.3),
            run_time=0.4
        )

        para_outline = self._para_outline()
        self.play(Create(para_outline), run_time=1.0)
        self.play(Indicate(para_outline, scale_factor=1.05, color=COLOR_PARA), run_time=0.5)

        # 关键等式
        key_eq_lhs = Text("2 个三角形", font=FONT, font_size=26, color=WHITE)
        key_eq_mid = Text(" = ", font=FONT, font_size=26, color=WHITE)
        key_eq_rhs = Text("1 个平行四边形", font=FONT, font_size=26, color=COLOR_PARA)
        key_eq = VGroup(key_eq_lhs, key_eq_mid, key_eq_rhs).arrange(RIGHT, buff=0.05)
        key_eq.move_to(DOWN * 4.8)

        self.play(FadeIn(key_eq, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理标题和说明
        self.play(
            FadeOut(VGroup(title, step3, key_eq)),
            run_time=0.4
        )

        # 保留 t2 和 para_outline 给后续场景
        self.t2 = t2
        self.para_outline = para_outline

    # ------------------------------------------------------------------
    # Scene 3: 平行四边形面积
    # ------------------------------------------------------------------

    def scene_3_parallelogram_formula(self):
        """标注底和高，写出平行四边形面积公式"""

        title = Text(
            "平行四边形面积", font=FONT,
            font_size=36, color=COLOR_PARA
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 底边标注
        base_line = Line(self.A, self.B, color=COLOR_BASE, stroke_width=5)
        base_mid = (self.A + self.B) / 2 + DOWN * 0.45
        base_label = VGroup(
            Text("底 ", font=FONT, font_size=26, color=COLOR_BASE),
            MathTex("a", font_size=32, color=COLOR_BASE)
        ).arrange(RIGHT, buff=0.05).move_to(base_mid)

        self.play(Create(base_line), run_time=0.5)
        self.play(FadeIn(base_label), run_time=0.4)

        # 高线标注 (虚线 + 直角符号)
        height_line = self._height_line()
        right_angle = self._right_angle_mark()
        height_mid = (self.C + self.H_foot) / 2 + LEFT * 0.55
        height_label = VGroup(
            Text("高 ", font=FONT, font_size=26, color=COLOR_HEIGHT),
            MathTex("h", font_size=32, color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.05).move_to(height_mid)

        self.play(Create(height_line), Create(right_angle), run_time=0.7)
        self.play(FadeIn(height_label), run_time=0.4)

        # 平行四边形面积公式
        formula_lhs = Text("平行四边形面积 = ", font=FONT, font_size=26, color=WHITE)
        formula_rhs = MathTex(r"a \times h", font_size=34, color=COLOR_HL)
        formula = VGroup(formula_lhs, formula_rhs).arrange(RIGHT, buff=0.1)
        formula.move_to(DOWN * 3.8)

        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 清理，保留几何线条给下一场景
        self.play(
            FadeOut(VGroup(title, base_label, height_label, formula)),
            run_time=0.4
        )

        # 保存引用
        self.base_line = base_line
        self.height_line = height_line
        self.right_angle = right_angle

    # ------------------------------------------------------------------
    # Scene 4: 推导三角形面积公式
    # ------------------------------------------------------------------

    def scene_4_derivation(self):
        """逐步推导: 三角形 = 平行四边形 ÷ 2"""

        title = Text(
            "推导三角形面积", font=FONT,
            font_size=36, color=COLOR_TRI1
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 等式1: 2 × 三角形 = 平行四边形
        eq1 = VGroup(
            Text("2 × 三角形面积", font=FONT, font_size=26, color=COLOR_TRI1),
            Text(" = ", font=FONT, font_size=26, color=WHITE),
            Text("平行四边形面积", font=FONT, font_size=26, color=COLOR_PARA),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 3.8)
        self.play(FadeIn(eq1, shift=UP * 0.3), run_time=0.6)
        self.wait(0.7)

        # 等式2: 三角形 = 平行四边形 ÷ 2
        eq2_lhs = Text("三角形面积", font=FONT, font_size=26, color=COLOR_TRI1)
        eq2_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        eq2_rhs = Text("平行四边形面积 ÷ 2", font=FONT, font_size=26, color=COLOR_HL)
        eq2 = VGroup(eq2_lhs, eq2_eq, eq2_rhs).arrange(RIGHT, buff=0.05)
        eq2.move_to(DOWN * 4.8)

        arrow = Arrow(
            eq1.get_bottom() + DOWN * 0.05,
            eq2.get_top() + UP * 0.05,
            color=COLOR_HL, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(Create(arrow), FadeIn(eq2, shift=UP * 0.2), run_time=0.7)
        self.wait(0.7)

        # 等式3: 代入 a × h
        eq3_lhs = Text("三角形面积", font=FONT, font_size=26, color=COLOR_TRI1)
        eq3_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        eq3_rhs = MathTex(r"a \times h \div 2", font_size=36, color=COLOR_HL)
        eq3 = VGroup(eq3_lhs, eq3_eq, eq3_rhs).arrange(RIGHT, buff=0.1)
        eq3.move_to(DOWN * 4.8)

        self.play(ReplacementTransform(eq2, eq3), run_time=0.8)
        self.wait(2.0)   # ★ 关键理解点，多停留

        # 清理本场景元素
        self.play(
            FadeOut(VGroup(
                title, eq1, arrow, eq3,
                self.t2, self.para_outline,
                self.base_line, self.height_line, self.right_angle
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式总结
    # ------------------------------------------------------------------

    def scene_5_formula_summary(self):
        """大字公式 + 底高标注 + 强调 ÷2 的含义"""

        # 重置主三角形的透明度（前几场景可能改变过）
        self.main_tri.set_fill(opacity=0.35).set_stroke(width=3)

        # 底边和高重新标注
        base_line = Line(self.A, self.B, color=COLOR_BASE, stroke_width=5)
        base_label = VGroup(
            Text("底 ", font=FONT, font_size=28, color=COLOR_BASE),
            MathTex("a", font_size=34, color=COLOR_BASE)
        ).arrange(RIGHT, buff=0.05).move_to(
            (self.A + self.B) / 2 + DOWN * 0.45
        )

        height_line = self._height_line()
        right_angle = self._right_angle_mark()
        height_label = VGroup(
            Text("高 ", font=FONT, font_size=28, color=COLOR_HEIGHT),
            MathTex("h", font_size=34, color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.05).move_to(
            (self.C + self.H_foot) / 2 + LEFT * 0.55
        )

        self.play(
            Create(base_line), FadeIn(base_label),
            run_time=0.6
        )
        self.play(
            Create(height_line), Create(right_angle), FadeIn(height_label),
            run_time=0.6
        )
        self.wait(0.5)

        # 公式框背景
        formula_box = RoundedRectangle(
            width=7.8, height=2.4,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 4.9)

        # 公式标题
        formula_title = Text(
            "三角形面积公式", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 4.1)

        # 核心公式 S = a × h ÷ 2
        formula_S = Text("S  = ", font=FONT, font_size=44, color=WHITE)
        formula_ah2 = MathTex(
            r"a \times h \div 2",
            font_size=52, color=COLOR_HL
        )
        formula_main = VGroup(formula_S, formula_ah2).arrange(RIGHT, buff=0.1)
        formula_main.move_to(DOWN * 5.4)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_title), run_time=0.4)
        self.play(Write(formula_main), run_time=0.9)

        # 强调 ÷2 的含义
        div2_box = SurroundingRectangle(
            formula_ah2, color=COLOR_TRI2, stroke_width=2.5, buff=0.1, corner_radius=0.1
        )
        div2_note = Text(
            "÷2 = 三角形是平行四边形的一半",
            font=FONT, font_size=21, color=COLOR_TRI2
        ).move_to(DOWN * 6.3)

        self.play(Create(div2_box), run_time=0.4)
        self.play(FadeIn(div2_note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                base_line, base_label,
                height_line, right_angle, height_label,
                formula_box, formula_title, formula_main,
                div2_box, div2_note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示"""

        # 淡出主三角形
        self.play(FadeOut(self.main_tri), run_time=0.4)

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

        # 装饰: 6个小三角形围绕旋转
        colors = [COLOR_TRI1, COLOR_TRI2, COLOR_PARA,
                  COLOR_BASE, COLOR_HEIGHT, COLOR_HL]
        mini_tris = VGroup(*[
            Triangle(
                fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).scale(0.22).rotate(i * PI / 3).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(t, scale=0.3) for t in mini_tris], run_time=0.5)
        self.play(Rotate(mini_tris, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_tris)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql triangle_area_lesson.py TriangleAreaLesson
#   高质量:    manim -qh  triangle_area_lesson.py TriangleAreaLesson
#   4K:        manim -qk  triangle_area_lesson.py TriangleAreaLesson
# ======================================================================
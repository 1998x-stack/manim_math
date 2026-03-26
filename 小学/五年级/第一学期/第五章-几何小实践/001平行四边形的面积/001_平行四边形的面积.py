"""
001_平行四边形的面积.py — 平行四边形的面积 教学动画

知识点: 通过割补法将平行四边形转化为长方形，推导 面积 = 底 × 高
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

几何核心:
  平行四边形: A(-3,-1)  B(2,-1)  C(3.5,1.5)  D(-1.5,1.5)
  底 AB = 5, 高 h = 2.5
  割补法: 沿高 DF 切下左侧直角三角形 ADF，平移到右侧 BCE 位置
  垂足 F: A 点正上方在 AD 上的投影 → (-3, -1) 往上画高到 D
  实际: 从 D 向 AB 作垂线，垂足 F(-1.5, -1)
  切割三角形: A(-3,-1), D(-1.5,1.5), F(-1.5,-1)
  平移后: B(2,-1), C(3.5,1.5), E(3.5,-1)  (E是B正上方C的垂足)
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
COLOR_PARA = "#3b82f6"       # 蓝色平行四边形
COLOR_CUT = "#ef4444"        # 红色切割三角形
COLOR_RECT = "#22c55e"       # 绿色长方形
COLOR_BASE = "#f59e0b"       # 橙色底边
COLOR_HEIGHT = "#a78bfa"     # 紫色高
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class ParallelogramAreaLesson(Scene):
    """
    平行四边形的面积教学动画
    场景顺序:
      1. 开场钩子
      2. 割补法 (核心)
      3. 变成长方形
      4. 推导面积公式
      5. 公式总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_cut_method()
        self.scene_3_form_rectangle()
        self.scene_4_derive_formula()
        self.scene_5_formula_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 几何初始化 (所有坐标统一计算)
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""

        # ===== 平行四边形顶点 (逆时针) =====
        # 底边水平，高 = 2.5
        self.A = np.array([-3.0, -1.0, 0.0])   # 左下
        self.B = np.array([ 2.0, -1.0, 0.0])   # 右下
        self.C = np.array([ 3.5,  1.5, 0.0])   # 右上
        self.D = np.array([-1.5,  1.5, 0.0])   # 左上

        # ===== 底和高 =====
        self.base_length = np.linalg.norm(self.B - self.A)   # = 5.0
        self.height_val = self.D[1] - self.A[1]              # = 2.5

        # ===== 从 D 向 AB 作垂线，垂足 F =====
        # AB 是水平线 y=-1，所以垂足 F 就是 D 的 x 坐标，y = A 的 y
        self.F = np.array([self.D[0], self.A[1], 0.0])  # = (-1.5, -1, 0)

        # ===== 从 C 向 AB 延长线作垂线，垂足 E =====
        self.E = np.array([self.C[0], self.B[1], 0.0])  # = (3.5, -1, 0)

        # ===== 切割三角形顶点: A, D, F =====
        # 平移后位置: B, C, E (平移向量 = B - A)
        self.shift_vec = self.B - self.A  # = (5, 0, 0)

        # ===== 长方形顶点: F, E, C, D =====
        # F(-1.5,-1), E(3.5,-1), C(3.5,1.5), D(-1.5,1.5)
        self.rect_width = np.linalg.norm(self.E - self.F)   # = 5.0
        self.rect_height = np.linalg.norm(self.D - self.F)   # = 2.5

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-9
        # 平行四边形: AB // DC 且 AB = DC
        AB = self.B - self.A
        DC = self.C - self.D
        assert np.linalg.norm(AB - DC) < eps, f"非平行四边形: AB={AB}, DC={DC}"

        # 底边长度
        assert abs(self.base_length - 5.0) < eps, f"底={self.base_length}"

        # 高
        assert abs(self.height_val - 2.5) < eps, f"高={self.height_val}"

        # 垂足 F 在 AB 上 (同 y 坐标)
        assert abs(self.F[1] - self.A[1]) < eps, "F 不在 AB 上"

        # 长方形宽 = 底边长
        assert abs(self.rect_width - self.base_length) < eps, "长方形宽 ≠ 底"

        # 长方形高 = 平行四边形高
        assert abs(self.rect_height - self.height_val) < eps, "长方形高 ≠ 高"

        # 切割三角形面积验证: ADF 面积 = BCE 面积
        area_ADF = 0.5 * abs((self.D[0] - self.A[0]) * (self.F[1] - self.A[1]) -
                              (self.F[0] - self.A[0]) * (self.D[1] - self.A[1]))
        area_BCE = 0.5 * abs((self.C[0] - self.B[0]) * (self.E[1] - self.B[1]) -
                              (self.E[0] - self.B[0]) * (self.C[1] - self.B[1]))
        assert abs(area_ADF - area_BCE) < eps, f"三角形面积不等: {area_ADF} ≠ {area_BCE}"

        print("✓ 几何验证通过: 底=5.0, 高=2.5, 割补三角形面积相等")

    # ------------------------------------------------------------------
    # 辅助: 创建几何对象
    # ------------------------------------------------------------------

    def _parallelogram(self, fill_opacity=0.35, **kw):
        """蓝色平行四边形"""
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=COLOR_PARA, fill_color=COLOR_PARA,
            fill_opacity=fill_opacity, stroke_width=3, **kw
        )

    def _cut_triangle(self, fill_opacity=0.5, **kw):
        """红色切割三角形 ADF"""
        return Polygon(
            self.A, self.D, self.F,
            color=COLOR_CUT, fill_color=COLOR_CUT,
            fill_opacity=fill_opacity, stroke_width=2.5, **kw
        )

    def _rectangle(self, fill_opacity=0.3, **kw):
        """绿色长方形 FECD"""
        return Polygon(
            self.F, self.E, self.C, self.D,
            color=COLOR_RECT, fill_color=COLOR_RECT,
            fill_opacity=fill_opacity, stroke_width=3, **kw
        )

    def _height_line(self):
        """从 D 到垂足 F 的虚线高"""
        return DashedLine(
            self.D, self.F,
            color=COLOR_HEIGHT, dash_length=0.12, stroke_width=2.5
        )

    def _right_angle_mark(self, size=0.22):
        """垂足 F 处的直角符号"""
        foot = self.F
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
        """钩子: '平行四边形的面积怎么算？'"""

        # 作者信息 (顶部)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "平行四边形的面积", font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "怎么算？", font=FONT, font_size=52, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 显示平行四边形
        self.main_para = self._parallelogram()
        self.play(Create(self.main_para), run_time=1.2)

        # 问号
        para_center = (self.A + self.B + self.C + self.D) / 4
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(para_center)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子，保留平行四边形
        self.play(FadeOut(VGroup(hook1, hook2, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 割补法 — 画高线，标识切割区域
    # ------------------------------------------------------------------

    def scene_2_cut_method(self):
        """画高线，标识要切割的三角形"""

        title = Text(
            "割补法", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 步骤1: 画高
        step1 = Text(
            "沿高剪开", font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(Write(step1), run_time=0.5)

        height_line = self._height_line()
        right_angle = self._right_angle_mark()
        self.play(Create(height_line), run_time=0.8)
        self.play(Create(right_angle), run_time=0.3)
        self.wait(0.3)

        # 步骤2: 标识切割三角形 (红色高亮)
        step2 = Text(
            "切下左侧的直角三角形",
            font=FONT, font_size=26, color=COLOR_CUT
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(step1),
            FadeIn(step2, shift=UP * 0.2),
            run_time=0.4
        )

        cut_tri = self._cut_triangle()
        self.play(FadeIn(cut_tri), run_time=0.6)
        self.play(Indicate(cut_tri, scale_factor=1.05, color=COLOR_CUT), run_time=0.5)
        self.wait(0.5)

        # 保存引用给下一场景
        self.cut_tri = cut_tri
        self.height_line = height_line
        self.right_angle = right_angle
        self.title_cut = title
        self.step2 = step2

    # ------------------------------------------------------------------
    # Scene 3: 平移拼合 → 形成长方形
    # ------------------------------------------------------------------

    def scene_3_form_rectangle(self):
        """平移切割三角形到右侧，形成长方形"""

        # 步骤3: 平移提示
        step3 = Text(
            "平移到右侧",
            font=FONT, font_size=28, color=COLOR_CUT
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(self.step2),
            FadeIn(step3, shift=UP * 0.2),
            run_time=0.4
        )

        # ★ 核心动画: 切割三角形平移到右侧
        # 平移向量 = B - A = (5, 0, 0)
        # 平移路径用箭头提示
        arrow_hint = Arrow(
            (self.A + self.D + self.F) / 3,
            (self.B + self.C + self.E) / 3,
            color=COLOR_HL, stroke_width=2, buff=0.3,
            max_tip_length_to_length_ratio=0.12
        )
        self.play(Create(arrow_hint), run_time=0.4)

        self.play(
            self.cut_tri.animate.shift(self.shift_vec),
            run_time=2.0,
            rate_func=smooth
        )
        self.play(FadeOut(arrow_hint), run_time=0.3)
        self.wait(0.3)

        # 长方形轮廓亮起
        step4 = Text(
            "变成了一个长方形！",
            font=FONT, font_size=30,
            color=COLOR_RECT, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(step3),
            FadeIn(step4, shift=UP * 0.3),
            run_time=0.4
        )

        rect_outline = self._rectangle(fill_opacity=0)
        rect_outline.set_stroke(width=4)
        self.play(Create(rect_outline), run_time=1.0)
        self.play(Indicate(rect_outline, scale_factor=1.03, color=COLOR_RECT), run_time=0.5)

        # 关键等式
        key_lhs = Text("平行四边形面积", font=FONT, font_size=24, color=COLOR_PARA)
        key_mid = Text(" = ", font=FONT, font_size=24, color=WHITE)
        key_rhs = Text("长方形面积", font=FONT, font_size=24, color=COLOR_RECT)
        key_eq = VGroup(key_lhs, key_mid, key_rhs).arrange(RIGHT, buff=0.05)
        key_eq.move_to(DOWN * 4.8)

        self.play(FadeIn(key_eq, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                self.title_cut, step4, key_eq,
                self.cut_tri, rect_outline,
                self.height_line, self.right_angle
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 推导面积公式
    # ------------------------------------------------------------------

    def scene_4_derive_formula(self):
        """底和高标注 → 长方形面积 = 底 × 高 → 平行四边形面积 = 底 × 高"""

        title = Text(
            "推导面积公式", font=FONT,
            font_size=36, color=COLOR_PARA
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 底边标注
        base_line = Line(self.A, self.B, color=COLOR_BASE, stroke_width=5)
        base_mid = (self.A + self.B) / 2 + DOWN * 0.5
        base_label = VGroup(
            Text("底 ", font=FONT, font_size=26, color=COLOR_BASE),
            MathTex("a", font_size=32, color=COLOR_BASE)
        ).arrange(RIGHT, buff=0.05).move_to(base_mid)

        self.play(Create(base_line), run_time=0.5)
        self.play(FadeIn(base_label), run_time=0.4)

        # 高线标注
        height_line = self._height_line()
        right_angle = self._right_angle_mark()
        height_mid = (self.D + self.F) / 2 + LEFT * 0.55
        height_label = VGroup(
            Text("高 ", font=FONT, font_size=26, color=COLOR_HEIGHT),
            MathTex("h", font_size=32, color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.05).move_to(height_mid)

        self.play(Create(height_line), Create(right_angle), run_time=0.7)
        self.play(FadeIn(height_label), run_time=0.4)
        self.wait(0.5)

        # 等式1: 长方形面积 = 长 × 宽
        eq1 = VGroup(
            Text("长方形面积", font=FONT, font_size=24, color=COLOR_RECT),
            Text(" = ", font=FONT, font_size=24, color=WHITE),
            Text("长 × 宽", font=FONT, font_size=24, color=COLOR_RECT),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 3.5)
        self.play(FadeIn(eq1, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        # 等式2: 长 = 底, 宽 = 高
        eq2 = VGroup(
            Text("长 = 底", font=FONT, font_size=24, color=COLOR_BASE),
            Text("，", font=FONT, font_size=24, color=WHITE),
            Text("宽 = 高", font=FONT, font_size=24, color=COLOR_HEIGHT),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 4.3)
        self.play(FadeIn(eq2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 等式3: 平行四边形面积 = 底 × 高
        eq3_lhs = Text("平行四边形面积", font=FONT, font_size=26, color=COLOR_PARA)
        eq3_eq = Text(" = ", font=FONT, font_size=26, color=WHITE)
        eq3_rhs = MathTex(r"a \times h", font_size=36, color=COLOR_HL)
        eq3 = VGroup(eq3_lhs, eq3_eq, eq3_rhs).arrange(RIGHT, buff=0.1)
        eq3.move_to(DOWN * 5.5)

        arrow = Arrow(
            eq2.get_bottom() + DOWN * 0.1,
            eq3.get_top() + UP * 0.1,
            color=COLOR_HL, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(Create(arrow), FadeIn(eq3, shift=UP * 0.2), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, base_line, base_label,
                height_line, right_angle, height_label,
                eq1, eq2, arrow, eq3
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式总结
    # ------------------------------------------------------------------

    def scene_5_formula_summary(self):
        """大字公式 + 底高标注 + 强调要点"""

        # 重置平行四边形外观
        self.main_para.set_fill(opacity=0.35).set_stroke(width=3)

        # 底边和高重新标注
        base_line = Line(self.A, self.B, color=COLOR_BASE, stroke_width=5)
        base_label = VGroup(
            Text("底 ", font=FONT, font_size=28, color=COLOR_BASE),
            MathTex("a", font_size=34, color=COLOR_BASE)
        ).arrange(RIGHT, buff=0.05).move_to(
            (self.A + self.B) / 2 + DOWN * 0.5
        )

        height_line = self._height_line()
        right_angle = self._right_angle_mark()
        height_label = VGroup(
            Text("高 ", font=FONT, font_size=28, color=COLOR_HEIGHT),
            MathTex("h", font_size=34, color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.05).move_to(
            (self.D + self.F) / 2 + LEFT * 0.55
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
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 5.0)

        # 公式标题
        formula_title = Text(
            "平行四边形面积公式", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.9)

        # 核心公式 S = a × h
        formula_S = Text("S = ", font=FONT, font_size=44, color=WHITE)
        formula_ah = MathTex(
            r"a \times h", font_size=52, color=COLOR_HL
        )
        formula_main = VGroup(formula_S, formula_ah).arrange(RIGHT, buff=0.1)
        formula_main.move_to(DOWN * 4.9)

        # 要点提醒
        note = Text(
            "注意：高必须垂直于底！",
            font=FONT, font_size=22, color=COLOR_HEIGHT
        ).move_to(DOWN * 5.9)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_title), run_time=0.4)
        self.play(Write(formula_main), run_time=0.9)

        # 高亮框
        hl_box = SurroundingRectangle(
            formula_ah, color=COLOR_CUT, stroke_width=2.5, buff=0.12, corner_radius=0.1
        )
        self.play(Create(hl_box), run_time=0.4)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                base_line, base_label,
                height_line, right_angle, height_label,
                formula_box, formula_title, formula_main,
                hl_box, note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息 + 关注提示"""

        # 淡出平行四边形
        self.play(FadeOut(self.main_para), run_time=0.4)

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

        # 装饰: 小平行四边形
        colors = [COLOR_PARA, COLOR_CUT, COLOR_RECT,
                  COLOR_BASE, COLOR_HEIGHT, COLOR_HL]
        mini_shapes = VGroup(*[
            Polygon(
                np.array([-0.2, -0.1, 0]),
                np.array([0.2, -0.1, 0]),
                np.array([0.3, 0.1, 0]),
                np.array([-0.1, 0.1, 0]),
                fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).rotate(i * PI / 3).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(s, scale=0.3) for s in mini_shapes], run_time=0.5)
        self.play(Rotate(mini_shapes, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_shapes)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 001_平行四边形的面积.py ParallelogramAreaLesson
#   高质量:    manim -qh  001_平行四边形的面积.py ParallelogramAreaLesson
#   4K:        manim -qk  001_平行四边形的面积.py ParallelogramAreaLesson
# ======================================================================

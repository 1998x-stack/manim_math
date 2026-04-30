"""
trapezoid_area_lesson.py — 梯形的面积 教学动画

知识点: 通过拼合法推导梯形面积 = (上底+下底)×高÷2
年级: 五年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

几何核心:
  T1: A(-2.0,0.5)  B(1.0,0.5)  C(0.2,2.5)  D(-1.2,2.5)
      下底 b=3.0   上底 a=1.4   高 h=2.0
  T2 绕 M_BC=(0.6,1.5) 旋转180° → A'(3.2,2.5)  D'(2.4,0.5)
  平行四边形: A(-2,0.5)→D'(2.4,0.5)→A'(3.2,2.5)→D(-1.2,2.5)
             底 = a+b = 4.4
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
COLOR_TRAP1  = "#3b82f6"   # 蓝色 T1
COLOR_TRAP2  = "#ef4444"   # 红色 T2
COLOR_PARA   = "#22c55e"   # 绿色平行四边形
COLOR_LOWER  = "#f59e0b"   # 橙色下底
COLOR_UPPER  = "#fb923c"   # 浅橙上底
COLOR_HEIGHT = "#a78bfa"   # 紫色高
COLOR_HL     = "#fbbf24"   # 黄色高亮
COLOR_AUTHOR = "#6b7280"   # 灰色作者
FONT         = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class TrapezoidAreaLesson(Scene):
    """
    梯形面积教学动画
    Scene 1: 开场钩子
    Scene 2: 拼合法 (T2 旋转 180°)
    Scene 3: 标注平行四边形的底和高
    Scene 4: 推导梯形面积公式
    Scene 5: 公式总结
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_merge_trick()
        self.scene_3_parallelogram_label()
        self.scene_4_derivation()
        self.scene_5_formula_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一计算所有坐标，不使用臆想值"""

        # ===== 梯形 T1 顶点 =====
        # 逆时针: 下底 AB, 右腰 BC, 上底 CD (右→左), 左腰 DA
        self.A = np.array([-2.0, 0.5, 0.0])   # 下底左端
        self.B = np.array([ 1.0, 0.5, 0.0])   # 下底右端
        self.C = np.array([ 0.2, 2.5, 0.0])   # 上底右端
        self.D = np.array([-1.2, 2.5, 0.0])   # 上底左端

        # ===== 关键派生点 (精确计算) =====
        self.M_BC    = (self.B + self.C) / 2           # 旋转轴 = (0.6, 1.5, 0)
        self.A_prime = 2 * self.M_BC - self.A          # = (3.2, 2.5, 0)
        self.D_prime = 2 * self.M_BC - self.D          # = (2.4, 0.5, 0)

        # ===== 测量值 =====
        self.b_lower = float(np.linalg.norm(self.B - self.A))   # 3.0
        self.a_upper = float(np.linalg.norm(self.C - self.D))   # 1.4
        self.h       = float(self.D[1] - self.A[1])              # 2.0

        # ===== 高的垂足 =====
        self.H_foot = np.array([self.D[0], self.A[1], 0.0])  # (-1.2, 0.5)

        # ===== 梯形中心 =====
        self.trap_center = (self.A + self.B + self.C + self.D) / 4

        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-9
        combined = float(np.linalg.norm(self.D_prime - self.A))
        assert abs(combined - (self.a_upper + self.b_lower)) < eps, "合并底边计算错误"
        vec_left  = self.D - self.A
        vec_right = self.A_prime - self.D_prime
        assert np.linalg.norm(vec_left - vec_right) < eps, "平行四边形腰验证失败"
        print(f"✓ 几何验证通过: a={self.a_upper}, b={self.b_lower}, h={self.h}, a+b={combined:.1f}")

    # ------------------------------------------------------------------
    # 辅助: 创建几何对象
    # ------------------------------------------------------------------

    def _trap(self, color, fill_opacity=0.38):
        """蓝/红梯形"""
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=color, fill_color=color,
            fill_opacity=fill_opacity, stroke_width=3
        )

    def _para_outline(self):
        """平行四边形外轮廓 (无填充)"""
        return Polygon(
            self.A, self.D_prime, self.A_prime, self.D,
            color=COLOR_PARA, stroke_width=4, fill_opacity=0
        )

    def _height_line(self):
        """从 D 到垂足的虚线高"""
        return DashedLine(
            self.D, self.H_foot,
            color=COLOR_HEIGHT, dash_length=0.12, stroke_width=2.5
        )

    def _right_angle_mark(self, size=0.18):
        """垂足处直角符号"""
        f  = self.H_foot
        vu = np.array([0, size, 0])
        vr = np.array([size, 0, 0])
        return Polygon(
            f, f + vr, f + vr + vu, f + vu,
            color=COLOR_HEIGHT, stroke_width=1.5, fill_opacity=0
        )

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '为什么梯形面积要 ÷ 2？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text("为什么梯形面积", font=FONT, font_size=40, color=WHITE).move_to(UP * 5.5)
        hook2 = Text("要  ÷ 2 ？",    font=FONT, font_size=52,
                     color=COLOR_HL, weight=BOLD).move_to(UP * 4.4)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 主梯形
        self.main_trap = self._trap(COLOR_TRAP1)
        self.play(Create(self.main_trap), run_time=1.2)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(self.trap_center)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子，保留梯形
        self.play(FadeOut(VGroup(hook1, hook2, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 拼合法
    # ------------------------------------------------------------------

    def scene_2_merge_trick(self):
        """T2 旋转 180° 与 T1 拼合成平行四边形"""

        title = Text(
            "拼合法", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # Step 1: 复制梯形
        step1 = Text(
            "复制一个完全相同的梯形",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(Write(step1), run_time=0.6)

        t2 = self._trap(COLOR_TRAP2, fill_opacity=0.48)
        self.play(GrowFromCenter(t2), run_time=0.7)
        self.wait(0.3)

        # Step 2: 旋转提示
        step2 = Text(
            "将红色梯形旋转 180°",
            font=FONT, font_size=26, color=COLOR_TRAP2
        ).move_to(DOWN * 3.5)
        self.play(FadeOut(step1), FadeIn(step2, shift=UP * 0.2), run_time=0.4)
        self.wait(0.2)

        # ★ 核心旋转动画: T2 绕 M_BC=(0.6,1.5) 旋转 180°
        # 旋转后 T2 顶点: A'(3.2,2.5), C(0.2,2.5), B(1.0,0.5), D'(2.4,0.5)
        # 与 T1 共享边 BC，无缝拼合
        self.play(
            Rotate(t2, angle=PI, about_point=self.M_BC),
            run_time=2.2, rate_func=smooth
        )
        self.wait(0.4)

        # 平行四边形轮廓
        step3 = Text(
            "拼成了一个平行四边形！",
            font=FONT, font_size=30, color=COLOR_PARA, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(FadeOut(step2), FadeIn(step3, shift=UP * 0.3), run_time=0.4)

        para_outline = self._para_outline()
        self.play(Create(para_outline), run_time=1.0)
        self.play(Indicate(para_outline, scale_factor=1.04, color=COLOR_PARA), run_time=0.5)

        # 关键等式
        key_eq = VGroup(
            Text("2 个梯形",       font=FONT, font_size=26, color=WHITE),
            Text(" = ",            font=FONT, font_size=26, color=WHITE),
            Text("1 个平行四边形", font=FONT, font_size=26, color=COLOR_PARA)
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 4.8)
        self.play(FadeIn(key_eq, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, step3, key_eq)), run_time=0.4)

        # 保存供后续场景使用
        self.t2           = t2
        self.para_outline = para_outline

    # ------------------------------------------------------------------
    # Scene 3: 标注底 (a+b) 和高 h
    # ------------------------------------------------------------------

    def scene_3_parallelogram_label(self):
        """在平行四边形上标注合并底 (a+b) 和高 h"""

        title = Text(
            "标注底和高", font=FONT, font_size=36, color=COLOR_PARA
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # ----- 合并底边 brace -----
        base_obj = Line(self.A, self.D_prime)   # A(-2,0.5) → D'(2.4,0.5)
        brace = Brace(base_obj, direction=DOWN, color=COLOR_LOWER)

        lbl_up   = Text("上底", font=FONT, font_size=22, color=COLOR_UPPER)
        lbl_plus = Text(" + 下底", font=FONT, font_size=22, color=COLOR_LOWER)
        brace_lbl = VGroup(lbl_up, lbl_plus).arrange(RIGHT, buff=0.02)
        brace_lbl.next_to(brace, DOWN, buff=0.1)

        self.play(Create(brace), FadeIn(brace_lbl), run_time=0.7)

        # ----- 高: 虚线 + 直角 -----
        h_line = self._height_line()
        ra     = self._right_angle_mark()
        h_lbl  = VGroup(
            Text("高 ", font=FONT, font_size=26, color=COLOR_HEIGHT),
            MathTex("h",   font_size=32,          color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.04)
        h_lbl.move_to((self.D + self.H_foot) / 2 + LEFT * 0.65)

        self.play(Create(h_line), Create(ra), run_time=0.6)
        self.play(FadeIn(h_lbl), run_time=0.4)

        # ----- 平行四边形面积公式 -----
        fml = VGroup(
            Text("平行四边形面积 = ", font=FONT, font_size=24, color=WHITE),
            Text("(上底+下底)",       font=FONT, font_size=24, color=COLOR_LOWER),
            MathTex(r"\times h",        font_size=30,          color=COLOR_HL)
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 4.0)
        self.play(FadeIn(fml, shift=UP * 0.3), run_time=0.7)
        self.wait(1.5)

        # 清理标题、高注释、公式文字；保留 brace + brace_lbl 供推导场景参考
        self.play(FadeOut(VGroup(title, h_line, ra, h_lbl, fml)), run_time=0.4)

        self.brace     = brace
        self.brace_lbl = brace_lbl

    # ------------------------------------------------------------------
    # Scene 4: 推导梯形面积公式
    # ------------------------------------------------------------------

    def scene_4_derivation(self):
        """逐步推导: 梯形面积 = (a+b)×h÷2"""

        title = Text(
            "推导梯形面积", font=FONT, font_size=36, color=COLOR_TRAP1
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 等式1: 2×梯形 = 平行四边形
        eq1 = VGroup(
            Text("2 × 梯形面积",  font=FONT, font_size=26, color=COLOR_TRAP1),
            Text(" = ",           font=FONT, font_size=26, color=WHITE),
            Text("平行四边形面积", font=FONT, font_size=26, color=COLOR_PARA)
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 3.7)
        self.play(FadeIn(eq1, shift=UP * 0.3), run_time=0.6)
        self.wait(0.6)

        # 等式2: 梯形 = 平行四边形÷2
        eq2 = VGroup(
            Text("梯形面积",             font=FONT, font_size=26, color=COLOR_TRAP1),
            Text(" = 平行四边形面积÷2",  font=FONT, font_size=26, color=COLOR_HL)
        ).arrange(RIGHT, buff=0.04).move_to(DOWN * 4.8)
        arrow = Arrow(
            eq1.get_bottom() + DOWN * 0.05,
            eq2.get_top() + UP * 0.05,
            color=COLOR_HL, stroke_width=3, buff=0.04,
            max_tip_length_to_length_ratio=0.18
        )
        self.play(Create(arrow), FadeIn(eq2, shift=UP * 0.2), run_time=0.7)
        self.wait(0.6)

        # 等式3: 代入 (a+b)×h
        eq3 = VGroup(
            Text("梯形面积", font=FONT, font_size=26, color=COLOR_TRAP1),
            Text(" = ",      font=FONT, font_size=26, color=WHITE),
            MathTex(r"(a+b) \times h \div 2", font_size=36, color=COLOR_HL)
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 4.8)
        self.play(ReplacementTransform(eq2, eq3), run_time=0.8)
        self.wait(2.0)   # ★ 关键理解点

        # 清理全部
        self.play(
            FadeOut(VGroup(
                title, eq1, arrow, eq3,
                self.t2, self.para_outline,
                self.brace, self.brace_lbl
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 公式总结
    # ------------------------------------------------------------------

    def scene_5_formula_summary(self):
        """在 T1 上标注 a, b, h，显示公式框"""

        # ----- 上底标注 -----
        up_line  = Line(self.D, self.C, color=COLOR_UPPER, stroke_width=4)
        up_brace = Brace(up_line, direction=UP, color=COLOR_UPPER)
        up_lbl   = VGroup(
            Text("上底 ", font=FONT, font_size=26, color=COLOR_UPPER),
            MathTex("a",  font_size=32,            color=COLOR_UPPER)
        ).arrange(RIGHT, buff=0.04).next_to(up_brace, UP, buff=0.08)

        # ----- 下底标注 -----
        lo_line  = Line(self.A, self.B, color=COLOR_LOWER, stroke_width=4)
        lo_brace = Brace(lo_line, direction=DOWN, color=COLOR_LOWER)
        lo_lbl   = VGroup(
            Text("下底 ", font=FONT, font_size=26, color=COLOR_LOWER),
            MathTex("b",  font_size=32,            color=COLOR_LOWER)
        ).arrange(RIGHT, buff=0.04).next_to(lo_brace, DOWN, buff=0.08)

        # ----- 高标注 -----
        h_line = self._height_line()
        ra     = self._right_angle_mark()
        h_lbl  = VGroup(
            Text("高 ", font=FONT, font_size=26, color=COLOR_HEIGHT),
            MathTex("h",  font_size=32,          color=COLOR_HEIGHT)
        ).arrange(RIGHT, buff=0.04)
        h_lbl.move_to((self.D + self.H_foot) / 2 + LEFT * 0.65)

        self.play(Create(up_line), Create(lo_line), run_time=0.4)
        self.play(
            FadeIn(up_brace), FadeIn(up_lbl),
            FadeIn(lo_brace), FadeIn(lo_lbl),
            run_time=0.6
        )
        self.play(Create(h_line), Create(ra), FadeIn(h_lbl), run_time=0.6)
        self.wait(0.4)

        # ----- 公式框 -----
        fbox = RoundedRectangle(
            width=7.8, height=2.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 5.1)

        ftitle = Text(
            "梯形面积公式", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 4.15)

        f_S   = Text("S  = ", font=FONT, font_size=44, color=WHITE)
        f_rhs = MathTex(r"(a+b) \times h \div 2", font_size=44, color=COLOR_HL)
        f_main = VGroup(f_S, f_rhs).arrange(RIGHT, buff=0.12).move_to(DOWN * 5.5)

        self.play(FadeIn(fbox), run_time=0.3)
        self.play(Write(ftitle), run_time=0.4)
        self.play(Write(f_main), run_time=1.0)

        # ----- 强调 ÷2 -----
        div2_rect = SurroundingRectangle(
            f_rhs, color=COLOR_TRAP2, stroke_width=2.5, buff=0.1, corner_radius=0.1
        )
        div2_note = Text(
            "÷2 = 梯形是平行四边形面积的一半",
            font=FONT, font_size=20, color=COLOR_TRAP2
        ).move_to(DOWN * 6.6)

        self.play(Create(div2_rect), run_time=0.4)
        self.play(FadeIn(div2_note, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)   # ★ 关键停留

        # 清理
        self.play(
            FadeOut(VGroup(
                up_line, lo_line,
                up_brace, up_lbl, lo_brace, lo_lbl,
                h_line, ra, h_lbl,
                fbox, ftitle, f_main, div2_rect, div2_note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示 + 小梯形装饰"""

        self.play(FadeOut(self.main_trap), run_time=0.4)

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

        # 装饰: 6个小梯形围绕旋转
        colors = [COLOR_TRAP1, COLOR_TRAP2, COLOR_PARA,
                  COLOR_LOWER, COLOR_HEIGHT, COLOR_HL]
        mini = VGroup(*[
            Polygon(
                np.array([-0.22, -0.12, 0]),
                np.array([ 0.22, -0.12, 0]),
                np.array([ 0.13,  0.12, 0]),
                np.array([-0.13,  0.12, 0]),
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
        self.play(*[FadeIn(t, scale=0.3) for t in mini], run_time=0.5)
        self.play(Rotate(mini, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -pql trapezoid_area_lesson.py TrapezoidAreaLesson
#   高质量:   manim -qh  trapezoid_area_lesson.py TrapezoidAreaLesson
#   4K:       manim -qk  trapezoid_area_lesson.py TrapezoidAreaLesson
# ======================================================================
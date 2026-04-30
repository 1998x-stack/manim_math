"""
平面向量基本定理 - 动画教学视频
Planar Vector Decomposition Theorem

目标观众: 高二学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置：TikTok 竖屏 ─────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 颜色方案 ─────────────────────────────────
AFONT  = "PingFang SC"
BG     = "#1a1a2e"
C_E1   = "#e74c3c"   # 红 - 基底 e1
C_E2   = "#3498db"   # 蓝 - 基底 e2
C_A    = "#2ecc71"   # 绿 - 向量 a
C_HL   = YELLOW      # 黄 - 高亮
C_AUX  = GRAY_B      # 灰 - 辅助


class PlanarVectorBasis(Scene):
    """
    六场景动画:
      1. 开场钩子
      2. 基底定义
      3. 向量分解定理
      4. 标准基底 (直角坐标系)
      5. 知识总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.scene_opening()
        self.scene_basis()
        self.scene_decompose()
        self.scene_standard_basis()
        self.scene_summary()
        self.scene_outro()

    # ═══════════════════════════════════════════
    # 几何数据统一初始化
    # ═══════════════════════════════════════════
    def setup_geometry(self):
        """所有坐标在此精确计算，后续只引用不重算。"""
        # ── 基底向量 ─────────────────────────
        self.O      = np.array([-0.8,  0.0, 0])
        self.e1_raw = np.array([ 2.8,  0.5, 0])
        self.e2_raw = np.array([ 0.3,  2.3, 0])

        # λ₁ = λ₂ = 1 → 干净的平行四边形
        self.lam1, self.lam2 = 1.0, 1.0
        self.a_raw  = self.lam1 * self.e1_raw + self.lam2 * self.e2_raw

        # 世界坐标顶点
        self.E1 = self.O + self.e1_raw    # (2.0,  0.5)
        self.E2 = self.O + self.e2_raw    # (-0.5, 2.3)
        self.A  = self.O + self.a_raw     # (2.3,  2.8)

        # ── 几何验证 ──────────────────────────
        assert np.allclose(self.E1 + self.lam2 * self.e2_raw, self.A, atol=1e-8), \
            "Parallelogram check failed: E1 + λ2·e2 ≠ A"
        assert np.allclose(self.E2 + self.lam1 * self.e1_raw, self.A, atol=1e-8), \
            "Parallelogram check failed: E2 + λ1·e1 ≠ A"
        cross = float(self.e1_raw[0] * self.e2_raw[1] - self.e1_raw[1] * self.e2_raw[0])
        assert abs(cross) > 1e-6, "Basis vectors are collinear!"

        angle_rad = np.arccos(np.clip(
            np.dot(self.e1_raw[:2], self.e2_raw[:2]) /
            (np.linalg.norm(self.e1_raw) * np.linalg.norm(self.e2_raw)),
            -1.0, 1.0
        ))
        print(f"✓ Geometry OK | Angle(e1,e2)={np.degrees(angle_rad):.1f}° | cross={cross:.3f}")
        print(f"  E1={self.E1[:2]}  E2={self.E2[:2]}  A={self.A[:2]}")

    # ── 辅助：创建箭头 ────────────────────────
    def vec(self, start, end, color, sw=5, tl=0.25):
        return Arrow(start, end, color=color,
                     stroke_width=sw, tip_length=tl, buff=0)

    # ═══════════════════════════════════════════
    # Scene 1: 开场钩子
    # ═══════════════════════════════════════════
    def scene_opening(self):
        # 作者标识（全程保留）
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=AFONT, font_size=18, color=C_AUX
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.3)

        # 钩子三行问题
        lines = VGroup(
            Text("任意一个平面向量",   font=AFONT, font_size=40, color=WHITE),
            Text("都能被两个基向量",   font=AFONT, font_size=40, color=WHITE),
            Text("唯一地线性表示？",   font=AFONT, font_size=40, color=C_HL),
        ).arrange(DOWN, buff=0.3).move_to(UP * 5.2)

        self.play(FadeIn(lines, shift=DOWN * 0.3), run_time=0.7)

        # 神秘向量
        mystery = self.vec(
            np.array([-1.5, 1.5, 0]),
            np.array([ 2.0, 3.0, 0]),
            color=C_A, sw=6, tl=0.3
        )
        self.play(Create(mystery), run_time=0.8)

        qmark = Text("？", font=AFONT, font_size=70, color=C_HL)
        qmark.next_to(mystery.get_end(), UR, buff=0.15)
        self.play(FadeIn(qmark, scale=0.5), run_time=0.4)
        self.wait(0.8)

        self.play(FadeOut(lines), FadeOut(mystery), FadeOut(qmark), run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 2: 基底定义
    # ═══════════════════════════════════════════
    def scene_basis(self):
        title = Text("什么是基底？",
                     font=AFONT, font_size=36, color=C_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 原点
        o_dot = Dot(self.O, radius=0.08, color=WHITE)
        o_lbl = MathTex(r"O", font_size=28, color=WHITE).next_to(o_dot, DL, buff=0.1)
        self.play(FadeIn(o_dot), Write(o_lbl), run_time=0.3)

        # 基底向量 e1
        e1_arr = self.vec(self.O, self.E1, C_E1)
        e1_lbl = MathTex(r"\vec{e}_1", font_size=40, color=C_E1)
        e1_lbl.next_to(self.E1, RIGHT, buff=0.18)
        self.play(Create(e1_arr), run_time=0.7)
        self.play(Write(e1_lbl), run_time=0.3)

        # 基底向量 e2
        e2_arr = self.vec(self.O, self.E2, C_E2)
        e2_lbl = MathTex(r"\vec{e}_2", font_size=40, color=C_E2)
        e2_lbl.next_to(self.E2, LEFT, buff=0.18)
        self.play(Create(e2_arr), run_time=0.7)
        self.play(Write(e2_lbl), run_time=0.3)

        # 说明文字
        nc_txt = Text("两向量不平行（不共线）",
                      font=AFONT, font_size=24, color=WHITE).move_to(DOWN * 4.5)
        basis_txt = Text("→ 它们构成平面的一组基底",
                         font=AFONT, font_size=24, color=C_HL).move_to(DOWN * 5.2)
        self.play(FadeIn(nc_txt, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(basis_txt, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理，但保留向量供下一场景使用
        self.play(FadeOut(title), FadeOut(nc_txt), FadeOut(basis_txt), run_time=0.4)

        # 存储供 scene_decompose 使用
        self._e1_arr = e1_arr
        self._e2_arr = e2_arr
        self._e1_lbl = e1_lbl
        self._e2_lbl = e2_lbl
        self._o_dot  = o_dot
        self._o_lbl  = o_lbl

    # ═══════════════════════════════════════════
    # Scene 3: 向量分解定理（核心）
    # ═══════════════════════════════════════════
    def scene_decompose(self):
        title = Text("平面向量基本定理",
                     font=AFONT, font_size=34, color=C_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 目标向量 a
        a_arr = self.vec(self.O, self.A, C_A, sw=6, tl=0.3)
        a_mid = (self.O + self.A) / 2 + np.array([-0.5, 0.2, 0])
        a_lbl = MathTex(r"\vec{a}", font_size=44, color=C_A).move_to(a_mid)
        self.play(Create(a_arr), Write(a_lbl), run_time=0.8)
        self.wait(0.3)

        # 提示
        hint = Text("作平行四边形！", font=AFONT, font_size=26, color=C_HL).move_to(DOWN * 4.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.4)

        # 平行四边形虚线
        # E2 → A（平行于 e1）
        dash_e1 = DashedLine(self.E2, self.A,
                             color=C_E1, stroke_width=2.5, dash_length=0.12)
        # E1 → A（平行于 e2）
        dash_e2 = DashedLine(self.E1, self.A,
                             color=C_E2, stroke_width=2.5, dash_length=0.12)
        self.play(Create(dash_e1), Create(dash_e2), run_time=0.8)
        self.play(FadeOut(hint), run_time=0.2)

        # 分量箭头 ① λ₁e₁：O → E1
        comp1 = self.vec(self.O, self.E1, C_E1, sw=4, tl=0.2)
        comp1_lbl = MathTex(r"\lambda_1\vec{e}_1", font_size=30, color=C_E1)
        comp1_lbl.next_to((self.O + self.E1) / 2, DOWN, buff=0.2)

        step1 = Text("① 沿 e₁ 方向：λ₁e₁",
                     font=AFONT, font_size=22, color=C_E1).move_to(DOWN * 4.5)
        self.play(Create(comp1), Write(comp1_lbl), FadeIn(step1), run_time=0.7)
        self.wait(0.3)

        # 分量箭头 ② λ₂e₂：E1 → A
        comp2 = self.vec(self.E1, self.A, C_E2, sw=4, tl=0.2)
        comp2_lbl = MathTex(r"\lambda_2\vec{e}_2", font_size=30, color=C_E2)
        comp2_lbl.next_to((self.E1 + self.A) / 2, RIGHT, buff=0.18)

        step2 = Text("② 再沿 e₂ 方向：λ₂e₂",
                     font=AFONT, font_size=22, color=C_E2).move_to(DOWN * 5.2)
        self.play(Create(comp2), Write(comp2_lbl), FadeIn(step2), run_time=0.7)
        self.wait(0.5)

        # 核心公式
        formula = MathTex(
            r"\vec{a} = \lambda_1\vec{e}_1 + \lambda_2\vec{e}_2",
            font_size=38, color=WHITE
        ).move_to(DOWN * 4.0)

        self.play(FadeOut(step1), FadeOut(step2), run_time=0.2)
        self.play(Write(formula), run_time=0.8)

        # 唯一性强调
        unique = Text("λ₁, λ₂ 唯一确定！", font=AFONT, font_size=30, color=C_HL)
        unique.move_to(DOWN * 5.0)
        self.play(FadeIn(unique, shift=UP * 0.2, scale=1.05), run_time=0.5)
        self.wait(1.5)

        # 清除本场景所有元素（包括 Scene 2 保留物）
        to_out = VGroup(
            title, a_arr, a_lbl,
            dash_e1, dash_e2,
            comp1, comp1_lbl,
            comp2, comp2_lbl,
            formula, unique,
            self._e1_arr, self._e2_arr,
            self._e1_lbl, self._e2_lbl,
            self._o_dot, self._o_lbl,
        )
        self.play(FadeOut(to_out), run_time=0.6)

    # ═══════════════════════════════════════════
    # Scene 4: 标准基底（直角坐标系）
    # ═══════════════════════════════════════════
    def scene_standard_basis(self):
        title = Text("特殊基底：直角坐标系",
                     font=AFONT, font_size=34, color=C_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 坐标轴
        axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 4, 1],
            x_length=5.0,
            y_length=5.0,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.2,
            },
        ).move_to(UP * 1.2)

        xl = MathTex(r"x", font_size=26, color=GRAY_B).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        yl = MathTex(r"y", font_size=26, color=GRAY_B).next_to(axes.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(axes), Write(xl), Write(yl), run_time=1.0)

        orig = axes.c2p(0, 0)
        i_end = axes.c2p(1, 0)
        j_end = axes.c2p(0, 1)

        # i 向量
        i_arr = Arrow(orig, i_end, color=C_E1, stroke_width=5, tip_length=0.18, buff=0)
        i_lbl = MathTex(r"\vec{i}=(1,0)", font_size=26, color=C_E1)
        i_lbl.next_to(i_end, DOWN, buff=0.2)
        self.play(Create(i_arr), Write(i_lbl), run_time=0.6)

        # j 向量
        j_arr = Arrow(orig, j_end, color=C_E2, stroke_width=5, tip_length=0.18, buff=0)
        j_lbl = MathTex(r"\vec{j}=(0,1)", font_size=26, color=C_E2)
        j_lbl.next_to(j_end, RIGHT, buff=0.12)
        self.play(Create(j_arr), Write(j_lbl), run_time=0.6)
        self.wait(0.4)

        # 示例向量 a = (2.5, 2)
        a_end = axes.c2p(2.5, 2)
        a_arr = Arrow(orig, a_end, color=C_A, stroke_width=5, tip_length=0.22, buff=0)
        a_lbl = MathTex(r"\vec{a}=(x,y)", font_size=28, color=C_A)
        a_lbl.next_to(a_end, UR, buff=0.12)
        self.play(Create(a_arr), Write(a_lbl), run_time=0.7)

        # 坐标分量虚线
        x_proj = axes.c2p(2.5, 0)
        y_proj = axes.c2p(0, 2)
        vert  = DashedLine(x_proj, a_end, color=C_E2, stroke_width=2, dash_length=0.1)
        horiz = DashedLine(y_proj, a_end, color=C_E1, stroke_width=2, dash_length=0.1)
        xt = MathTex(r"x", font_size=22, color=C_E1).next_to(x_proj, DOWN, buff=0.1)
        yt = MathTex(r"y", font_size=22, color=C_E2).next_to(y_proj, LEFT, buff=0.1)
        self.play(Create(vert), Create(horiz), Write(xt), Write(yt), run_time=0.7)

        # 公式
        f1 = MathTex(r"\vec{a} = x\vec{i} + y\vec{j}",
                     font_size=36, color=WHITE).move_to(DOWN * 4.2)
        f2 = MathTex(r"\Leftrightarrow\ \vec{a} = (x,\ y)",
                     font_size=32, color=C_HL).move_to(DOWN * 5.1)

        self.play(Write(f1), run_time=0.7)
        self.play(Write(f2), run_time=0.5)
        self.wait(1.5)

        to_out = VGroup(title, axes, xl, yl,
                        i_arr, i_lbl, j_arr, j_lbl,
                        a_arr, a_lbl, vert, horiz, xt, yt,
                        f1, f2)
        self.play(FadeOut(to_out), run_time=0.6)

    # ═══════════════════════════════════════════
    # Scene 5: 知识总结
    # ═══════════════════════════════════════════
    def scene_summary(self):
        title = Text("知识总结", font=AFONT, font_size=40, color=C_HL).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 定理框
        box = RoundedRectangle(
            width=7.6, height=2.6,
            corner_radius=0.3,
            color=C_HL, stroke_width=2,
            fill_color="#0d0d28", fill_opacity=0.92
        ).move_to(UP * 3.5)

        thm_hdr = Text("平面向量基本定理",
                       font=AFONT, font_size=24, color=C_HL)
        thm_hdr.move_to(box.get_top() + DOWN * 0.45)

        thm_form = MathTex(
            r"\vec{a} = \lambda_1\vec{e}_1 + \lambda_2\vec{e}_2",
            font_size=40, color=WHITE
        ).move_to(box.get_center() + DOWN * 0.15)

        self.play(FadeIn(box), Write(thm_hdr), run_time=0.5)
        self.play(Write(thm_form), run_time=0.6)

        # 三个关键要点
        pts = VGroup(
            Text("① e1, e2 不共线 → 构成基底",
                 font=AFONT, font_size=24, color=WHITE),
            Text("② λ₁, λ₂ 唯一存在（核心！）",
                 font=AFONT, font_size=24, color=C_HL),
            Text("③ 基底选取不唯一",
                 font=AFONT, font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(UP * 1.5)

        for pt in pts:
            self.play(FadeIn(pt, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.1)

        # 分隔线
        sep = Line(LEFT * 3.5, RIGHT * 3.5,
                   color=GRAY_B, stroke_width=1).move_to(DOWN * 0.45)
        self.play(Create(sep), run_time=0.3)

        # 标准基底小节
        std_h = Text("直角坐标系中的标准基底",
                     font=AFONT, font_size=24, color=C_E1).move_to(DOWN * 0.95)
        std_f = MathTex(r"\vec{i}=(1,0),\quad \vec{j}=(0,1)",
                        font_size=30, color=WHITE).move_to(DOWN * 1.75)
        std_c = MathTex(r"\vec{a}=(x,y)=x\vec{i}+y\vec{j}",
                        font_size=32, color=C_HL).move_to(DOWN * 2.65)

        self.play(FadeIn(std_h), run_time=0.35)
        self.play(Write(std_f), run_time=0.5)
        self.play(Write(std_c), run_time=0.5)
        self.wait(1.8)

        to_out = VGroup(title, box, thm_hdr, thm_form,
                        pts, sep, std_h, std_f, std_c)
        self.play(FadeOut(to_out), run_time=0.6)

    # ═══════════════════════════════════════════
    # Scene 6: 片尾
    # ═══════════════════════════════════════════
    def scene_outro(self):
        big_name = Text("上海初高中数学直通车",
                        font=AFONT, font_size=42, color=WHITE).move_to(UP * 1.5)
        big_id   = Text("@emptyandcalm",
                        font=AFONT, font_size=32, color=C_AUX).move_to(UP * 0.5)
        follow   = Text("关注我，获得更多数学技巧！",
                        font=AFONT, font_size=28, color=C_HL).move_to(DOWN * 0.5)

        self.play(Transform(self.author_mob, big_name), run_time=0.7)
        self.play(FadeIn(big_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰：展示向量分解示意
        os = np.array([0.0, -2.5, 0])
        e1s = np.array([1.3, 0.2, 0])
        e2s = np.array([0.1, 1.1, 0])
        deco = VGroup(
            Arrow(os, os + e1s, color=C_E1, stroke_width=3.5,
                  tip_length=0.18, buff=0),
            Arrow(os, os + e2s, color=C_E2, stroke_width=3.5,
                  tip_length=0.18, buff=0),
            Arrow(os, os + e1s + e2s, color=C_A, stroke_width=4,
                  tip_length=0.22, buff=0),
        )
        deco_lbl = MathTex(r"\vec{a} = \vec{e}_1 + \vec{e}_2",
                           font_size=28, color=C_HL)
        deco_lbl.next_to(deco, DOWN, buff=0.3)

        self.play(FadeIn(deco, shift=UP * 0.3), run_time=0.5)
        self.play(Write(deco_lbl), run_time=0.4)
        self.wait(1.5)


# ── 渲染命令 ──────────────────────────────────
# 快速预览:  manim -pql vector_basis.py PlanarVectorBasis
# 高清输出: 
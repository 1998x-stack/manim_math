"""
003_图形的拼搭.py — 图形的拼搭 教学动画

知识点: 用相同的图形拼出新图案
  - 两个三角形拼成正方形
  - 两个三角形拼成平行四边形
  - 七巧板简单拼搭欣赏
  - 发展空间想象力

年级: 一年级下册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
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
BG_COLOR   = "#1a1a2e"
COLOR_TRI1 = "#3b82f6"   # 蓝 — 第一块三角形
COLOR_TRI2 = "#f59e0b"   # 橙 — 第二块三角形
COLOR_SQ   = "#22c55e"   # 绿 — 正方形
COLOR_PARA = "#a78bfa"   # 紫 — 平行四边形
COLOR_HL   = "#fbbf24"   # 黄高亮
COLOR_AUTH = "#6b7280"   # 灰色作者

FONT = "PingFang SC"

# 七巧板配色
TANG_COLORS = [
    "#ef4444",  # 红
    "#3b82f6",  # 蓝
    "#22c55e",  # 绿
    "#f59e0b",  # 橙
    "#a78bfa",  # 紫
    "#ec4899",  # 粉
    "#14b8a6",  # 青
]


# ======================================================================
# 主场景
# ======================================================================

class ShapeBuildingLesson(Scene):
    """
    图形的拼搭教学动画
    场景顺序:
      1. 开场钩子
      2. 两个三角形拼成正方形
      3. 两个三角形拼成平行四边形
      4. 更多拼法小结
      5. 七巧板欣赏
      6. 总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_two_triangles_square()
        self.scene_3_two_triangles_parallelogram()
        self.scene_4_more_combinations()
        self.scene_5_tangram()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标（精确计算）"""

        # 基准直角边长
        self.s = 1.5

        s = self.s

        # ===== 正方形拼合：两个等腰直角三角形 =====
        # 正方形中心在 (0, cy)，边长 2s
        # 三角形1(蓝): BL, BR, TL  — 下半
        # 三角形2(橙): BR, TR, TL  — 上半
        cy_sq = 0.8
        self.sq_BL = np.array([-s,  cy_sq - s, 0])
        self.sq_BR = np.array([ s,  cy_sq - s, 0])
        self.sq_TL = np.array([-s,  cy_sq + s, 0])
        self.sq_TR = np.array([ s,  cy_sq + s, 0])

        # 验证正方形边长
        assert abs(np.linalg.norm(self.sq_BR - self.sq_BL) - 2*s) < 1e-9

        # ===== 平行四边形拼合：两个直角三角形 =====
        # tri1: (0,0),(s,0),(s,s)  — 直角在 (s,0)
        # tri2: (2s,s),(s,s),(s,0) — 直角在 (s,s)
        # 组合得平行四边形: (0,0),(s,0),(2s,s),(s,s)
        cy_para = 0.8
        off = np.array([-s, cy_para - s/2, 0])

        self.p1_A = off + np.array([0,    0,   0])
        self.p1_B = off + np.array([s,    0,   0])
        self.p1_C = off + np.array([s,    s,   0])

        self.p2_A = off + np.array([2*s,  s,   0])
        self.p2_B = off + np.array([s,    s,   0])
        self.p2_C = off + np.array([s,    0,   0])

        self.para_verts = [
            off + np.array([0,    0,   0]),
            off + np.array([s,    0,   0]),
            off + np.array([2*s,  s,   0]),
            off + np.array([s,    s,   0]),
        ]

        # 验证平行四边形的平行边
        v_bottom = self.para_verts[1] - self.para_verts[0]
        v_top    = self.para_verts[2] - self.para_verts[3]
        v_left   = self.para_verts[3] - self.para_verts[0]
        v_right  = self.para_verts[2] - self.para_verts[1]
        assert np.allclose(v_bottom, v_top),  "平行四边形上下边不平行！"
        assert np.allclose(v_left,   v_right), "平行四边形左右边不平行！"

        print("✓ 几何验证通过")

    # ------------------------------------------------------------------
    # 辅助方法
    # ------------------------------------------------------------------

    def make_author_brand(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTH
        ).move_to(UP * 7.0)

    def make_right_angle_mark(self, corner, p1, p2, size=0.22):
        """在 corner 顶点处绘制直角符号，p1/p2 在两条边上"""
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner, corner + v1, corner + v1 + v2, corner + v2,
            stroke_color=WHITE, stroke_width=2, fill_opacity=0
        )

    def make_triangle(self, A, B, C, color, fill_opacity=0.70, stroke_width=3):
        return Polygon(A, B, C,
                       fill_color=color, fill_opacity=fill_opacity,
                       stroke_color=color, stroke_width=stroke_width)

    # ------------------------------------------------------------------
    # 场景 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author_brand()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        title = Text("图形的拼搭", font=FONT, font_size=54, color=COLOR_HL) \
                    .move_to(UP * 5.8)
        sub = Text("用简单图形，拼出新形状！", font=FONT, font_size=28, color=WHITE) \
                  .move_to(UP * 4.9)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.4)

        # 展示两个分开的三角形作为钩子
        s = self.s
        y0 = 1.2
        t1 = self.make_triangle(
            np.array([-3.0, y0 - s, 0]),
            np.array([-3.0 + s, y0 - s, 0]),
            np.array([-3.0, y0 + s * 0.6, 0]),
            COLOR_TRI1
        )
        t2 = self.make_triangle(
            np.array([0.5, y0 - s, 0]),
            np.array([0.5 + s, y0 - s, 0]),
            np.array([0.5 + s, y0 + s * 0.6, 0]),
            COLOR_TRI2
        )

        self.play(FadeIn(t1, shift=LEFT * 0.4), FadeIn(t2, shift=RIGHT * 0.4), run_time=0.7)

        question = Text("这两个三角形能拼成什么？", font=FONT, font_size=28, color=COLOR_HL) \
                       .move_to(DOWN * 3.5)
        self.play(Write(question), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(question),
            FadeOut(t1), FadeOut(t2),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 2: 两个三角形拼成正方形
    # ------------------------------------------------------------------

    def scene_2_two_triangles_square(self):
        s = self.s

        title = Text("拼成正方形", font=FONT, font_size=40, color=COLOR_SQ) \
                    .move_to(UP * 5.8)
        step1 = Text("先认识这两个三角形", font=FONT, font_size=26, color=WHITE) \
                    .move_to(UP * 5.0)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(step1), run_time=0.4)

        # --- Step 1: 显示两个分开的三角形 ---
        # 分别放在左右两侧，有间隔
        gap = 0.6
        cy = 1.0

        # 三角形1 (蓝) — 等腰直角，直角在左下
        A1 = np.array([-2.0 - gap/2, cy - s, 0])
        B1 = np.array([-gap/2,       cy - s, 0])
        C1 = np.array([-2.0 - gap/2, cy + s, 0])

        # 三角形2 (橙) — 等腰直角，直角在右上（与tri1对称）
        A2 = np.array([gap/2,        cy + s, 0])
        B2 = np.array([gap/2 + 2.0,  cy + s, 0])
        C2 = np.array([gap/2 + 2.0,  cy - s, 0])

        tri1 = self.make_triangle(A1, B1, C1, COLOR_TRI1)
        tri2 = self.make_triangle(A2, B2, C2, COLOR_TRI2)

        self.play(FadeIn(tri1, shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(tri2, shift=RIGHT * 0.3), run_time=0.5)

        # 直角标记
        ra1 = self.make_right_angle_mark(A1, B1, C1)
        ra2 = self.make_right_angle_mark(B2, A2, C2)
        self.play(FadeIn(ra1), FadeIn(ra2), run_time=0.4)

        lbl1 = Text("三角形①", font=FONT, font_size=20, color=COLOR_TRI1) \
                   .next_to(tri1, DOWN, buff=0.3)
        lbl2 = Text("三角形②", font=FONT, font_size=20, color=COLOR_TRI2) \
                   .next_to(tri2, DOWN, buff=0.3)
        self.play(FadeIn(lbl1), FadeIn(lbl2), run_time=0.4)
        self.wait(0.5)

        # --- Step 2: 提示拼合方式 ---
        step2 = Text("把斜边对在一起", font=FONT, font_size=26, color=COLOR_HL) \
                    .move_to(UP * 5.0)
        self.play(Transform(step1, step2), run_time=0.4)
        self.play(FadeOut(ra1), FadeOut(ra2), FadeOut(lbl1), FadeOut(lbl2), run_time=0.3)

        # --- Step 3: 移动拼合 ---
        # 目标: 两个三角形组成边长 2s 的正方形，中心在 (0, cy)
        sq_BL = np.array([-s, cy - s, 0])
        sq_BR = np.array([ s, cy - s, 0])
        sq_TL = np.array([-s, cy + s, 0])
        sq_TR = np.array([ s, cy + s, 0])

        tri1_final = self.make_triangle(sq_BL, sq_BR, sq_TL, COLOR_TRI1)
        tri2_final = self.make_triangle(sq_BR, sq_TR, sq_TL, COLOR_TRI2)

        self.play(
            Transform(tri1, tri1_final),
            Transform(tri2, tri2_final),
            run_time=1.2,
            rate_func=smooth
        )
        self.wait(0.4)

        # --- Step 4: 高亮正方形轮廓 ---
        sq_outline = Square(
            side_length=2*s,
            stroke_color=COLOR_SQ, stroke_width=5, fill_opacity=0
        ).move_to(np.array([0, cy, 0]))
        self.play(Create(sq_outline), run_time=0.8)

        result = Text("正方形！", font=FONT, font_size=40, color=COLOR_SQ) \
                     .move_to(DOWN * 3.0)
        formula = Text("2个三角形 = 1个正方形", font=FONT, font_size=26, color=WHITE) \
                      .move_to(DOWN * 4.0)

        self.play(Write(result), run_time=0.6)
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(step1),
            FadeOut(tri1), FadeOut(tri2), FadeOut(sq_outline),
            FadeOut(result), FadeOut(formula),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 3: 两个三角形拼成平行四边形
    # ------------------------------------------------------------------

    def scene_3_two_triangles_parallelogram(self):
        title = Text("拼成平行四边形", font=FONT, font_size=38, color=COLOR_PARA) \
                    .move_to(UP * 5.8)
        step1 = Text("换一种拼法：直角边相接", font=FONT, font_size=26, color=WHITE) \
                    .move_to(UP * 5.0)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(step1), run_time=0.4)

        # --- Step 1: 显示两个分开的三角形 ---
        sep = np.array([1.6, 0, 0])

        t1_start = self.make_triangle(
            self.p1_A - sep, self.p1_B - sep, self.p1_C - sep,
            COLOR_TRI1
        )
        t2_start = self.make_triangle(
            self.p2_A + sep, self.p2_B + sep, self.p2_C + sep,
            COLOR_TRI2
        )

        self.play(FadeIn(t1_start, shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(t2_start, shift=RIGHT * 0.3), run_time=0.5)

        # 直角标记
        ra1 = self.make_right_angle_mark(
            self.p1_B - sep, self.p1_A - sep, self.p1_C - sep
        )
        ra2 = self.make_right_angle_mark(
            self.p2_B + sep, self.p2_A + sep, self.p2_C + sep
        )
        self.play(FadeIn(ra1), FadeIn(ra2), run_time=0.4)
        self.wait(0.5)

        # --- Step 2: 拼合 ---
        step2 = Text("两块直角边对齐 →", font=FONT, font_size=26, color=COLOR_HL) \
                    .move_to(UP * 5.0)
        self.play(
            Transform(step1, step2),
            FadeOut(ra1), FadeOut(ra2),
            run_time=0.4
        )

        t1_final = self.make_triangle(self.p1_A, self.p1_B, self.p1_C, COLOR_TRI1)
        t2_final = self.make_triangle(self.p2_A, self.p2_B, self.p2_C, COLOR_TRI2)

        self.play(
            Transform(t1_start, t1_final),
            Transform(t2_start, t2_final),
            run_time=1.0,
            rate_func=smooth
        )
        self.wait(0.4)

        # --- Step 3: 高亮平行四边形轮廓 ---
        para_outline = Polygon(
            *self.para_verts,
            stroke_color=COLOR_PARA, stroke_width=5, fill_opacity=0
        )
        self.play(Create(para_outline), run_time=0.8)

        result = Text("平行四边形！", font=FONT, font_size=38, color=COLOR_PARA) \
                     .move_to(DOWN * 3.0)
        formula = Text("2个三角形 = 1个平行四边形", font=FONT, font_size=24, color=WHITE) \
                      .move_to(DOWN * 4.0)

        self.play(Write(result), run_time=0.6)
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(step1),
            FadeOut(t1_start), FadeOut(t2_start), FadeOut(para_outline),
            FadeOut(result), FadeOut(formula),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 4: 更多拼法小结
    # ------------------------------------------------------------------

    def scene_4_more_combinations(self):
        title = Text("拼搭小结", font=FONT, font_size=42, color=COLOR_HL) \
                    .move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        s = self.s * 0.55   # 缩小版

        # 三行展示
        row_configs = [
            # (label, result_text, result_color, shapes)
            ("拼法①", "→ 正方形",    COLOR_SQ,   "square"),
            ("拼法②", "→ 平行四边形", COLOR_PARA, "para"),
            ("拼法③", "→ 大三角形",   COLOR_TRI1, "bigtri"),
        ]

        all_mobs = [title]
        y_top = 4.0

        for i, (lbl, res_str, res_clr, shape) in enumerate(row_configs):
            y = y_top - i * 2.4

            lbl_mob = Text(lbl, font=FONT, font_size=24, color=WHITE) \
                          .move_to(np.array([-3.5, y, 0]))

            # Mini shape
            cx, cy_row = -1.5, y
            if shape == "square":
                t1 = Polygon(
                    np.array([cx - s, cy_row - s, 0]),
                    np.array([cx + s, cy_row - s, 0]),
                    np.array([cx - s, cy_row + s, 0]),
                    fill_color=COLOR_TRI1, fill_opacity=0.75,
                    stroke_color=COLOR_TRI1, stroke_width=2
                )
                t2 = Polygon(
                    np.array([cx + s, cy_row - s, 0]),
                    np.array([cx + s, cy_row + s, 0]),
                    np.array([cx - s, cy_row + s, 0]),
                    fill_color=COLOR_TRI2, fill_opacity=0.75,
                    stroke_color=COLOR_TRI2, stroke_width=2
                )
                mini = VGroup(t1, t2)
            elif shape == "para":
                t1 = Polygon(
                    np.array([cx - s, cy_row - s/2, 0]),
                    np.array([cx,     cy_row - s/2, 0]),
                    np.array([cx,     cy_row + s/2, 0]),
                    fill_color=COLOR_TRI1, fill_opacity=0.75,
                    stroke_color=COLOR_TRI1, stroke_width=2
                )
                t2 = Polygon(
                    np.array([cx + s, cy_row + s/2, 0]),
                    np.array([cx,     cy_row + s/2, 0]),
                    np.array([cx,     cy_row - s/2, 0]),
                    fill_color=COLOR_TRI2, fill_opacity=0.75,
                    stroke_color=COLOR_TRI2, stroke_width=2
                )
                mini = VGroup(t1, t2)
            else:  # bigtri
                # Four small triangles forming a big one (simplified: just show big tri)
                t_big = Polygon(
                    np.array([cx - s, cy_row - s/2, 0]),
                    np.array([cx + s, cy_row - s/2, 0]),
                    np.array([cx,     cy_row + s,   0]),
                    fill_color=COLOR_TRI1, fill_opacity=0.75,
                    stroke_color=COLOR_TRI1, stroke_width=2
                )
                mini = VGroup(t_big)

            arrow = Text("→", font=FONT, font_size=28, color=WHITE) \
                        .move_to(np.array([0.5, y, 0]))
            res_mob = Text(res_str, font=FONT, font_size=26, color=res_clr) \
                          .move_to(np.array([2.8, y, 0]))

            self.play(FadeIn(lbl_mob, shift=RIGHT * 0.2), run_time=0.25)
            self.play(FadeIn(mini), run_time=0.35)
            self.play(FadeIn(arrow), run_time=0.2)
            self.play(Write(res_mob), run_time=0.4)
            self.wait(0.3)

            all_mobs += [lbl_mob, mini, arrow, res_mob]

        key_msg = Text("拼法不同，形状就不同！", font=FONT, font_size=28, color=COLOR_HL) \
                      .move_to(DOWN * 4.5)
        self.play(FadeIn(key_msg, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        all_mobs.append(key_msg)
        self.play(*[FadeOut(m) for m in all_mobs], run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 5: 七巧板欣赏
    # ------------------------------------------------------------------

    def scene_5_tangram(self):
        title = Text("七巧板", font=FONT, font_size=46, color=COLOR_HL) \
                    .move_to(UP * 5.8)
        sub = Text("中国古老的拼图玩具", font=FONT, font_size=28, color=WHITE) \
                  .move_to(UP * 5.0)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(sub), run_time=0.4)

        # 七巧板标准方形拼法
        # 以 4×4 网格为基础，中心在屏幕中央
        u = 0.60
        tc = np.array([0.0, 0.8, 0.0])   # 正方形中心

        def gp(c, r):
            """网格点（左下为原点）"""
            return tc + np.array([(c - 2)*u, (r - 2)*u, 0.0])

        pieces = [
            # 大三角形1: (0,4),(4,4),(0,0)  注意这会超出边界，缩小
            Polygon(gp(0,4), gp(4,4), gp(0,0),
                    fill_color=TANG_COLORS[0], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
            # 大三角形2: (4,4),(4,0),(0,0)
            Polygon(gp(4,4), gp(4,0), gp(0,0),
                    fill_color=TANG_COLORS[1], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
            # 中三角形: (2,4),(4,4),(4,2)
            Polygon(gp(2,4), gp(4,4), gp(4,2),
                    fill_color=TANG_COLORS[2], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
            # 小三角形1: (0,4),(2,4),(1,3)
            Polygon(gp(0,4), gp(2,4), gp(1,3),
                    fill_color=TANG_COLORS[3], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
            # 小三角形2: (3,1),(4,2),(4,0)
            Polygon(gp(3,1), gp(4,2), gp(4,0),
                    fill_color=TANG_COLORS[4], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
            # 正方形: (1,3),(2,4),(3,3),(2,2)
            Polygon(gp(1,3), gp(2,4), gp(3,3), gp(2,2),
                    fill_color=TANG_COLORS[5], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
            # 平行四边形: (0,0),(1,1),(3,1),(2,0)
            Polygon(gp(0,0), gp(1,1), gp(3,1), gp(2,0),
                    fill_color=TANG_COLORS[6], fill_opacity=0.88,
                    stroke_color=BG_COLOR, stroke_width=3),
        ]

        tg_group = VGroup(*pieces)

        # 逐一飞入
        for piece in pieces:
            self.play(FadeIn(piece, scale=0.6), run_time=0.22)

        self.wait(0.4)

        count_lbl = Text("7块组成一个正方形！", font=FONT, font_size=28, color=COLOR_HL) \
                        .move_to(DOWN * 3.2)
        self.play(Write(count_lbl), run_time=0.6)

        piece_desc = Text(
            "大三角×2  中三角×1  小三角×2\n正方形×1  平行四边形×1",
            font=FONT, font_size=22, color=WHITE, line_spacing=1.4
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(piece_desc, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 散开再复原，展示拼搭乐趣
        scatter_hint = Text("换一种拼法……", font=FONT, font_size=26, color=COLOR_HL) \
                            .move_to(DOWN * 5.8)
        self.play(FadeIn(scatter_hint), FadeOut(count_lbl), FadeOut(piece_desc), run_time=0.4)

        dirs = [UL, UR, LEFT, RIGHT, DL, DR, UP]
        self.play(*[p.animate.shift(d * 0.45) for p, d in zip(pieces, dirs)], run_time=0.9)
        self.wait(0.3)
        self.play(*[p.animate.shift(-d * 0.45) for p, d in zip(pieces, dirs)], run_time=0.7)
        self.wait(0.5)

        self.play(
            FadeOut(scatter_hint),
            FadeOut(title), FadeOut(sub),
            FadeOut(tg_group),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 6: 总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text("今天学了什么？", font=FONT, font_size=40, color=COLOR_HL) \
                    .move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        rows = [
            ("★", "相同的图形可以拼出不同形状",  COLOR_SQ),
            ("★", "2个三角形 → 正方形",          COLOR_TRI1),
            ("★", "2个三角形 → 平行四边形",       COLOR_PARA),
            ("★", "七巧板有7块，拼法无限多",      COLOR_HL),
        ]

        point_mobs = []
        y_start = 4.2
        for i, (mark, text, color) in enumerate(rows):
            y = y_start - i * 1.9
            star = Text(mark, font=FONT, font_size=28, color=color) \
                       .move_to(np.array([-3.5, y, 0]))
            txt = Text(text, font=FONT, font_size=25, color=WHITE) \
                      .move_to(np.array([0.6, y, 0]))
            self.play(FadeIn(star, shift=RIGHT * 0.2), run_time=0.2)
            self.play(Write(txt), run_time=0.5)
            point_mobs.append(VGroup(star, txt))
            self.wait(0.3)

        key = Text("动手拼一拼，发现更多形状！",
                   font=FONT, font_size=28, color=COLOR_HL) \
                  .move_to(DOWN * 3.8)
        self.play(FadeIn(key, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(key),
            *[FadeOut(m) for m in point_mobs],
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=38, color=WHITE) \
                         .move_to(UP * 1.5)
        author_id = Text("@emptyandcalm",
                         font=FONT, font_size=30, color=COLOR_AUTH) \
                        .move_to(UP * 0.6)
        follow = Text("关注我，获得更多数学技巧！",
                      font=FONT, font_size=28, color=COLOR_HL) \
                     .move_to(DOWN * 0.5)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰小三角形
        s_d = 0.38
        deco_positions = [
            UP * 3.0 + LEFT * 3.2,
            UP * 3.0 + RIGHT * 3.2,
            DOWN * 2.0 + LEFT * 3.2,
            DOWN * 2.0 + RIGHT * 3.2,
        ]
        deco_colors = [COLOR_TRI1, COLOR_TRI2, COLOR_SQ, COLOR_PARA]
        deco_group = VGroup()
        for pos, clr in zip(deco_positions, deco_colors):
            tri = Polygon(
                pos + np.array([0,    s_d, 0]),
                pos + np.array([-s_d, -s_d * 0.6, 0]),
                pos + np.array([s_d,  -s_d * 0.6, 0]),
                fill_color=clr, fill_opacity=0.88,
                stroke_color=clr, stroke_width=1
            )
            deco_group.add(tri)

        self.play(*[FadeIn(d, scale=0.5) for d in deco_group], run_time=0.5)
        self.play(Rotate(deco_group, angle=PI, run_time=1.5, about_point=ORIGIN))
        self.wait(1.0)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco_group),
            run_time=1.0
        )

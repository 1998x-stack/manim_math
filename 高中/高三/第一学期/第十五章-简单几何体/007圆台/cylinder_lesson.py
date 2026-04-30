"""
圆柱 (Cylinder) 教学动画
高三数学 · 简单几何体
TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────
#  全局配置
# ─────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────
#  颜色 & 字体
# ─────────────────────────────────────────
FONT     = "PingFang SC"
BG_COLOR = "#1a1a2e"
CYL_FILL = "#26a8d4"
CYL_LINE = "#7ee8fa"
RED_A    = "#ff6b6b"    # 半径 r
GRN_A    = "#a8e063"    # 高 h
GOLD_C   = "#ffd700"    # 标题 / 公式
PURPLE_A = "#c77dff"    # 截面
GRAY_C   = "#b0b0c0"    # 辅助线 / 作者


# ─────────────────────────────────────────
#  几何参数 (统一在此定义)
# ─────────────────────────────────────────
CYL_R      = 1.0                     # 底面半径
CYL_H      = 2.5                     # 高度
CIRC       = 2 * np.pi * CYL_R      # 周长 ≈ 6.283

# 展开矩形的显示尺寸 (缩放到适合屏幕)
UNROLL_W   = 5.5                     # 展开图显示宽度
UNROLL_H   = UNROLL_W * CYL_H / CIRC  # 展开图显示高度 ≈ 2.19
UNROLL_SCL = UNROLL_W / CIRC        # 缩放因子


# ─────────────────────────────────────────
#  工具函数
# ─────────────────────────────────────────
def make_cylinder_vgroup(
    r=CYL_R, h=CYL_H,
    fill_color=CYL_FILL, fill_opacity=0.45,
    stroke_color=CYL_LINE, stroke_width=1.5,
):
    """
    构建圆柱 VGroup: 侧面 + 顶面圆 + 底面圆
    轴向 = Z_AXIS (OUT), 中心在原点
    """
    body = Cylinder(
        radius=r,
        height=h,
        direction=Z_AXIS,
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        stroke_color=stroke_color,
        stroke_width=stroke_width,
        checkerboard_colors=False,
    )

    # 顶/底 cap (Circle 在 xy 平面, 平移到 ±h/2)
    top_cap = Circle(
        radius=r,
        fill_color=fill_color, fill_opacity=0.65,
        stroke_color=stroke_color, stroke_width=stroke_width,
    ).shift(OUT * h / 2)

    bot_cap = Circle(
        radius=r,
        fill_color=fill_color, fill_opacity=0.65,
        stroke_color=stroke_color, stroke_width=stroke_width,
    ).shift(OUT * (-h / 2))

    return VGroup(body, top_cap, bot_cap)


# ─────────────────────────────────────────
#  主场景
# ─────────────────────────────────────────
class CylinderLesson(ThreeDScene):

    # ──────────────────────────────────────
    #  入口
    # ──────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_formation()
        self.scene_3_dimensions()
        self.scene_4_unroll()
        self.scene_5_formulas()
        self.scene_6_cross_sections()
        self.scene_7_outro()

    # ──────────────────────────────────────
    #  辅助：更新/替换固定帧标题
    # ──────────────────────────────────────
    def _set_title(self, text_str, font_size=32, color=GOLD_C, run_time=0.4):
        new_t = Text(text_str, font=FONT, font_size=font_size, color=color)
        new_t.move_to(np.array([0, 6.0, 0]))
        self.add_fixed_in_frame_mobjects(new_t)

        if hasattr(self, "_main_title"):
            self.play(
                FadeOut(self._main_title),
                FadeIn(new_t),
                run_time=run_time,
            )
        else:
            self.play(FadeIn(new_t), run_time=run_time)

        self._main_title = new_t

    # ──────────────────────────────────────
    #  Scene 1 · 开场
    # ──────────────────────────────────────
    def scene_1_opening(self):
        # 相机初始角度
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES)

        # --- 作者信息 (顶部, 全程保留) ---
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_C,
        ).move_to(np.array([0, 7.3, 0]))
        self.add_fixed_in_frame_mobjects(author)
        self.play(FadeIn(author), run_time=0.3)
        self._author = author

        # --- 大标题 ---
        self._set_title("圆  柱", font_size=52, color=GOLD_C)

        # --- 钩子副标题 ---
        hook = Text("侧面展开是什么形状？", font=FONT, font_size=28, color=WHITE)
        hook.move_to(np.array([0, 5.1, 0]))
        self.add_fixed_in_frame_mobjects(hook)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # --- 3D 圆柱 ---
        cyl = make_cylinder_vgroup()
        cyl.move_to(ORIGIN + OUT * 0.2)
        self.play(Create(cyl), run_time=1.4)

        # --- 环绕旋转 ---
        self.begin_ambient_camera_rotation(rate=0.28)
        self.wait(2.2)
        self.stop_ambient_camera_rotation()

        # --- 清理 ---
        self.play(FadeOut(hook), FadeOut(cyl), run_time=0.5)

    # ──────────────────────────────────────
    #  Scene 2 · 旋转体生成
    # ──────────────────────────────────────
    def scene_2_formation(self):
        self._set_title("矩形旋转一周 → 圆柱", font_size=28)

        self.move_camera(phi=75 * DEGREES, theta=-80 * DEGREES, run_time=0.5)

        r, h = CYL_R, CYL_H

        # --- 旋转轴 (Z轴) ---
        axis = Line3D(
            start=np.array([0, 0, -h / 2 - 0.5]),
            end=np.array([0, 0,  h / 2 + 0.5]),
            color=YELLOW, stroke_width=2,
        )
        axis_lbl = Text("轴", font=FONT, font_size=22, color=YELLOW)
        axis_lbl.move_to(np.array([0.3, 5.3, 0]))
        self.add_fixed_in_frame_mobjects(axis_lbl)
        self.play(Create(axis), FadeIn(axis_lbl), run_time=0.6)

        # --- 母线矩形 (xz 平面, x≥0) ---
        # 顶点: (0, 0, -h/2), (r, 0, -h/2), (r, 0, h/2), (0, 0, h/2)
        rect_pts = [
            np.array([0,   0,  -h / 2]),
            np.array([r,   0,  -h / 2]),
            np.array([r,   0,   h / 2]),
            np.array([0,   0,   h / 2]),
        ]
        rect = Polygon(*rect_pts,
                       fill_color=RED_A, fill_opacity=0.35,
                       stroke_color=RED_A, stroke_width=2)
        self.play(Create(rect), run_time=0.8)

        # --- 说明文字 ---
        explain1 = Text("矩形绕轴旋转一周", font=FONT, font_size=24, color=WHITE)
        explain1.move_to(np.array([0, -4.2, 0]))
        self.add_fixed_in_frame_mobjects(explain1)
        self.play(FadeIn(explain1), run_time=0.4)
        self.wait(0.5)

        # --- 圆柱出现 (rect fade, cyl appear) ---
        cyl = make_cylinder_vgroup(r=r, h=h)
        self.play(
            FadeOut(rect),
            FadeIn(cyl),
            FadeOut(explain1),
            run_time=1.0,
        )

        # --- 旋转一圈展示 3D 立体感 ---
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1.5)
        self.stop_ambient_camera_rotation()

        # --- 结论文字 ---
        concl = Text("旋转体 = 圆柱", font=FONT, font_size=26, color=GOLD_C)
        concl.move_to(np.array([0, -4.2, 0]))
        self.add_fixed_in_frame_mobjects(concl)
        self.play(FadeIn(concl), run_time=0.5)
        self.wait(1.0)

        # --- 清理 ---
        self.play(
            FadeOut(axis), FadeOut(axis_lbl),
            FadeOut(concl), FadeOut(cyl),
            run_time=0.5,
        )

    # ──────────────────────────────────────
    #  Scene 3 · 尺寸标注
    # ──────────────────────────────────────
    def scene_3_dimensions(self):
        self._set_title("圆柱的基本尺寸", font_size=30)

        self.move_camera(phi=68 * DEGREES, theta=-55 * DEGREES, run_time=0.5)

        r, h = CYL_R, CYL_H

        cyl = make_cylinder_vgroup()
        self.play(FadeIn(cyl), run_time=0.7)

        # --- 半径线 (顶面, 从轴心到边缘) ---
        r_line = Line3D(
            start=np.array([0,   0,  h / 2]),
            end  =np.array([r,   0,  h / 2]),
            color=RED_A, stroke_width=3,
        )
        self.play(Create(r_line), run_time=0.6)

        r_lbl = MathTex(r"r", color=RED_A, font_size=38)
        r_lbl.move_to(np.array([0.55, 4.2, 0]))
        self.add_fixed_in_frame_mobjects(r_lbl)
        self.play(Write(r_lbl), run_time=0.4)

        # --- 高度线 (侧面右侧) ---
        h_line = Line3D(
            start=np.array([r + 0.35, 0, -h / 2]),
            end  =np.array([r + 0.35, 0,  h / 2]),
            color=GRN_A, stroke_width=3,
        )
        self.play(Create(h_line), run_time=0.6)

        h_lbl = MathTex(r"h", color=GRN_A, font_size=38)
        h_lbl.move_to(np.array([2.2, 2.8, 0]))
        self.add_fixed_in_frame_mobjects(h_lbl)
        self.play(Write(h_lbl), run_time=0.4)

        # --- 说明 ---
        dim_txt = Text("底面半径 r，高 h", font=FONT, font_size=24, color=WHITE)
        dim_txt.move_to(np.array([0, -4.2, 0]))
        self.add_fixed_in_frame_mobjects(dim_txt)
        self.play(FadeIn(dim_txt), run_time=0.5)

        self.wait(1.8)

        # --- 清理 ---
        self.play(
            FadeOut(r_line), FadeOut(r_lbl),
            FadeOut(h_line), FadeOut(h_lbl),
            FadeOut(dim_txt), FadeOut(cyl),
            run_time=0.5,
        )

    # ──────────────────────────────────────
    #  Scene 4 · 侧面展开图
    # ──────────────────────────────────────
    def scene_4_unroll(self):
        self._set_title("侧面展开图", font_size=32)

        # --- 说明文字 ---
        explain = Text("将侧面沿母线剪开展平…", font=FONT, font_size=24, color=WHITE)
        explain.move_to(np.array([0, -4.8, 0]))
        self.add_fixed_in_frame_mobjects(explain)

        # 先展示圆柱
        self.move_camera(phi=68 * DEGREES, theta=-55 * DEGREES, run_time=0.4)
        cyl = make_cylinder_vgroup()
        self.play(FadeIn(cyl), FadeIn(explain), run_time=0.7)
        self.wait(0.6)

        # 转为正面视角 (phi=90° 正侧视)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=0.7)
        self.play(FadeOut(cyl), FadeOut(explain), run_time=0.5)

        # ── 展开矩形 (固定帧 2D) ──────────────────
        w = UNROLL_W   # = 5.5
        dh = UNROLL_H  # ≈ 2.19

        unrolled = Rectangle(
            width=w, height=dh,
            fill_color=CYL_FILL, fill_opacity=0.35,
            stroke_color=CYL_LINE, stroke_width=2.5,
        ).move_to(np.array([0, 0.6, 0]))
        self.add_fixed_in_frame_mobjects(unrolled)
        self.play(Create(unrolled), run_time=1.2)

        # ── 宽度标注: 2πr ────────────────────────
        # 矩形底边中心在 [0, 0.6 - dh/2] = [0, 0.6 - 1.095]
        bot_y = 0.6 - dh / 2
        arr_y_w = bot_y - 0.45

        w_arr_l = np.array([-w / 2, arr_y_w, 0])
        w_arr_r = np.array([ w / 2, arr_y_w, 0])
        w_arrow = DoubleArrow(w_arr_l, w_arr_r, color=RED_A,
                              buff=0, stroke_width=2, tip_length=0.18)
        w_lbl = MathTex(r"2\pi r", color=RED_A, font_size=32)
        w_lbl.move_to(np.array([0, arr_y_w - 0.42, 0]))

        self.add_fixed_in_frame_mobjects(w_arrow, w_lbl)
        self.play(Create(w_arrow), Write(w_lbl), run_time=0.7)

        # ── 高度标注: h ──────────────────────────
        right_x = w / 2 + 0.45
        h_arr_b = np.array([right_x, 0.6 - dh / 2, 0])
        h_arr_t = np.array([right_x, 0.6 + dh / 2, 0])
        h_arrow = DoubleArrow(h_arr_b, h_arr_t, color=GRN_A,
                              buff=0, stroke_width=2, tip_length=0.18)
        h_lbl = MathTex(r"h", color=GRN_A, font_size=32)
        h_lbl.move_to(np.array([right_x + 0.4, 0.6, 0]))

        self.add_fixed_in_frame_mobjects(h_arrow, h_lbl)
        self.play(Create(h_arrow), Write(h_lbl), run_time=0.7)

        # ── 侧面积公式 ───────────────────────────
        side_lbl = Text("侧面积：", font=FONT, font_size=26, color=WHITE)
        side_eq  = MathTex(r"S = 2\pi r h", font_size=30, color=GOLD_C)
        side_grp = VGroup(side_lbl, side_eq).arrange(RIGHT, buff=0.2)
        side_grp.move_to(np.array([0, -2.8, 0]))
        self.add_fixed_in_frame_mobjects(side_grp)
        self.play(FadeIn(side_lbl), Write(side_eq), run_time=0.9)

        self.wait(2.2)

        # --- 清理 ---
        self.play(
            FadeOut(unrolled), FadeOut(w_arrow), FadeOut(w_lbl),
            FadeOut(h_arrow),  FadeOut(h_lbl),  FadeOut(side_grp),
            run_time=0.5,
        )

        # 恢复 3D 视角
        self.move_camera(phi=68 * DEGREES, theta=-55 * DEGREES, run_time=0.4)

    # ──────────────────────────────────────
    #  Scene 5 · 公式汇总
    # ──────────────────────────────────────
    def scene_5_formulas(self):
        self._set_title("圆柱的公式", font_size=32)

        # 小圆柱参考
        cyl_sm = make_cylinder_vgroup(r=0.65, h=1.6)
        cyl_sm.shift(UP * 3.0 + RIGHT * 0)
        self.play(FadeIn(cyl_sm), run_time=0.7)

        # ── 三条公式卡片 ─────────────────────────
        formulas = [
            ("体积：",  r"V = \pi r^2 h",       GOLD_C),
            ("侧面积：", r"S = 2\pi r h",        GRN_A),
            ("表面积：", r"S = 2\pi r(r + h)",   PURPLE_A),
        ]

        y_positions = [0.2, -1.4, -3.0]
        card_groups = []

        for (cn, latex, eq_color), y_pos in zip(formulas, y_positions):
            # 背景卡片
            bg = RoundedRectangle(
                width=7.0, height=0.95,
                corner_radius=0.15,
                fill_color="#0d2137", fill_opacity=0.85,
                stroke_color=eq_color, stroke_width=1.5,
            ).move_to(np.array([0, y_pos, 0]))

            cn_txt = Text(cn, font=FONT, font_size=22, color=WHITE)
            eq_txt = MathTex(latex, font_size=28, color=eq_color)
            row = VGroup(cn_txt, eq_txt).arrange(RIGHT, buff=0.25)
            row.move_to(np.array([0, y_pos, 0]))

            grp = VGroup(bg, row)
            grp.shift(LEFT * 9)  # 从左侧滑入
            self.add_fixed_in_frame_mobjects(grp)
            card_groups.append(grp)

        # 逐条滑入
        for grp in card_groups:
            self.play(grp.animate.shift(RIGHT * 9), run_time=0.7)
            self.wait(0.9)

        # 全部高亮闪烁
        self.play(
            *[Flash(grp, color=GOLD_C, flash_radius=0.6) for grp in card_groups],
            run_time=0.6,
        )
        self.wait(1.5)

        # --- 清理 ---
        self.play(
            FadeOut(cyl_sm),
            *[FadeOut(g) for g in card_groups],
            run_time=0.5,
        )

    # ──────────────────────────────────────
    #  Scene 6 · 截面
    # ──────────────────────────────────────
    def scene_6_cross_sections(self):
        self._set_title("圆柱的截面", font_size=32)

        self.move_camera(phi=68 * DEGREES, theta=-55 * DEGREES, run_time=0.4)

        r, h = CYL_R, CYL_H

        cyl = make_cylinder_vgroup()
        self.play(FadeIn(cyl), run_time=0.7)

        # ── 截面1: 平行于底面 → 圆 ───────────────
        sec1_txt = Text("平行于底面的截面：圆", font=FONT, font_size=24, color=PURPLE_A)
        sec1_txt.move_to(np.array([0, -4.0, 0]))
        self.add_fixed_in_frame_mobjects(sec1_txt)
        self.play(FadeIn(sec1_txt), run_time=0.5)

        slice_circ = Circle(
            radius=r,
            fill_color=PURPLE_A, fill_opacity=0.45,
            stroke_color=PURPLE_A, stroke_width=3,
        ).shift(OUT * 0.3)   # 中间某个高度
        self.play(Create(slice_circ), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(slice_circ), FadeOut(sec1_txt), run_time=0.4)

        # ── 截面2: 过轴 → 矩形 (轴截面) ─────────
        sec2_txt = Text("过轴的截面（轴截面）：矩形", font=FONT, font_size=22, color=GRN_A)
        sec2_txt.move_to(np.array([0, -4.0, 0]))
        self.add_fixed_in_frame_mobjects(sec2_txt)
        self.play(FadeIn(sec2_txt), run_time=0.5)

        # 轴截面: 在 xz 平面 (y=0), 宽=2r, 高=h
        axial_rect = Rectangle(
            width=2 * r, height=h,
            fill_color=GRN_A, fill_opacity=0.35,
            stroke_color=GRN_A, stroke_width=2.5,
        )
        # 在3D场景中, Rectangle 默认在 xy 平面; 需要旋转到 xz 平面
        axial_rect.rotate(PI / 2, RIGHT)  # 绕 x轴旋转90°, 使其在 xz 平面
        self.play(Create(axial_rect), run_time=0.9)

        # 标注 2r
        lbl_2r = MathTex(r"2r", color=RED_A, font_size=28)
        lbl_2r.move_to(np.array([0, -3.0, 0]))
        self.add_fixed_in_frame_mobjects(lbl_2r)
        self.play(Write(lbl_2r), run_time=0.4)

        # 轴截面面积公式
        axial_lbl = Text("轴截面面积：", font=FONT, font_size=22, color=WHITE)
        axial_eq  = MathTex(r"S = 2rh", font_size=26, color=GRN_A)
        axial_grp = VGroup(axial_lbl, axial_eq).arrange(RIGHT, buff=0.15)
        axial_grp.move_to(np.array([0, -5.2, 0]))
        self.add_fixed_in_frame_mobjects(axial_grp)
        self.play(FadeIn(axial_grp), run_time=0.5)

        self.wait(1.8)

        # --- 清理 ---
        self.play(
            FadeOut(cyl), FadeOut(axial_rect),
            FadeOut(sec2_txt), FadeOut(lbl_2r), FadeOut(axial_grp),
            run_time=0.5,
        )

    # ──────────────────────────────────────
    #  Scene 7 · 片尾
    # ──────────────────────────────────────
    def scene_7_outro(self):
        self._set_title("掌握圆柱，轻松解题！", font_size=34, color=GOLD_C)

        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=0.6)

        # 最终圆柱
        cyl_f = make_cylinder_vgroup()
        self.play(Create(cyl_f), run_time=1.0)

        # 公式总结 (3行, 固定帧)
        summary_items = [
            MathTex(r"V = \pi r^2 h",        font_size=26, color=GOLD_C),
            MathTex(r"S = 2\pi r h",          font_size=26, color=GRN_A),
            MathTex(r"S = 2\pi r(r + h)",     font_size=26, color=PURPLE_A),
        ]
        summary = VGroup(*summary_items).arrange(DOWN, buff=0.4)
        summary.move_to(np.array([0, -3.2, 0]))
        self.add_fixed_in_frame_mobjects(summary)
        self.play(FadeIn(summary), run_time=0.7)

        # 旋转展示
        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(1.2)

        # CTA
        follow_txt = Text("关注我，获得更多数学技巧！", font=FONT, font_size=26, color=WHITE)
        follow_txt.move_to(np.array([0, -5.8, 0]))
        self.add_fixed_in_frame_mobjects(follow_txt)
        self.play(FadeIn(follow_txt, shift=UP * 0.3), run_time=0.6)

        self.wait(2.5)
        self.stop_ambient_camera_rotation()
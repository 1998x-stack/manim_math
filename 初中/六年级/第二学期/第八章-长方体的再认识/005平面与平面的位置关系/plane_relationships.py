"""
平面与平面的位置关系 - 教学动画
知识点: 平行、相交、垂直
年级: 六年级 / 初中几何
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===================================================
#   全局配置 - TikTok 竖屏
# ===================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
BG_COLOR = "#1a1a2e"


# ===================================================
#   几何工具函数
# ===================================================

def rotate_around_x(point, angle_rad):
    """Rotate a 3D numpy point around the x-axis."""
    p = np.asarray(point, dtype=float)
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    return np.array([
        p[0],
        p[1] * cos_a - p[2] * sin_a,
        p[1] * sin_a + p[2] * cos_a,
    ])


def dihedral_angle_planes(n1, n2):
    """
    Compute dihedral angle between two planes given their normal vectors.
    Returns angle in degrees.
    """
    n1 = np.asarray(n1, dtype=float)
    n2 = np.asarray(n2, dtype=float)
    cos_val = np.dot(n1, n2) / (np.linalg.norm(n1) * np.linalg.norm(n2))
    cos_val = np.clip(cos_val, -1.0, 1.0)
    return np.degrees(np.arccos(np.abs(cos_val)))


# ===================================================
#   主场景
# ===================================================

class PlaneRelationships(ThreeDScene):
    """
    三维动画：平面与平面的位置关系
    场景顺序:
      1. 开场 Hook
      2. 平行关系 α ∥ β
      3. 相交关系 α ∩ β = l
      4. 垂直关系 α ⊥ β
      5. 总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ---- 颜色配置 ----
        self.C_ALPHA   = "#5dade2"   # 蓝 - 平面α
        self.C_BETA    = "#e74c3c"   # 红 - 平面β
        self.C_LINE    = "#f1c40f"   # 黄 - 交线
        self.C_TITLE   = "#f39c12"   # 金 - 标题
        self.C_TEXT    = "#bdc3c7"   # 浅灰 - 说明
        self.C_FORMULA = "#2ecc71"   # 绿 - 公式
        self.C_PERP    = "#9b59b6"   # 紫 - 垂直
        self.C_AUTHOR  = "#7f8c8d"   # 灰 - 作者

        # ---- 相机设置 ----
        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=-50 * DEGREES,
            zoom=0.85,
        )

        # ---- 统一几何初始化 ----
        self._setup_geometry()

        # ---- 全程作者信息 ----
        self.author_strip = self._fixed_text(
            f"{AUTHOR_NAME}  {AUTHOR_ID}", 7.0, 18, self.C_AUTHOR
        )
        self.play(FadeIn(self.author_strip), run_time=0.3)

        # ---- 执行各场景 ----
        self._scene_1_opening()
        self._scene_2_parallel()
        self._scene_3_intersecting()
        self._scene_4_perpendicular()
        self._scene_5_summary()
        self._scene_6_outro()

    # ================================================================
    #   几何初始化
    # ================================================================

    def _setup_geometry(self):
        """
        预计算所有3D几何数据，后续场景只引用。
        平面范围: x∈[-W, W], y∈[-H, H]
        """
        W, H = 2.5, 1.5
        self.PW = W
        self.PH = H

        # --- 平行场景 ---
        # α 在 z=+1, β 在 z=-1
        def horiz_rect(z):
            return [
                np.array([-W, -H, z]),
                np.array([ W, -H, z]),
                np.array([ W,  H, z]),
                np.array([-W,  H, z]),
            ]

        self.par_alpha_corners = horiz_rect(1.0)
        self.par_beta_corners  = horiz_rect(-1.0)

        # --- 相交场景 ---
        # α 在 z=0 水平面, β 为 α 绕 x 轴旋转 60°
        self.alpha_flat_corners = horiz_rect(0.0)

        angle_60 = 60.0 * DEGREES
        self.beta_60_corners = [
            rotate_around_x(p, angle_60) for p in self.alpha_flat_corners
        ]

        # 交线: x 轴 (y=0, z=0)
        self.inter_start = np.array([-W, 0.0, 0.0])
        self.inter_end   = np.array([ W, 0.0, 0.0])

        # --- 垂直场景 ---
        # β 为 α 绕 x 轴旋转 90°  → y=0 垂直面
        angle_90 = 90.0 * DEGREES
        self.beta_90_corners = [
            rotate_around_x(p, angle_90) for p in self.alpha_flat_corners
        ]

        # 直角标记点 (在 yz 平面 x=0 处)
        ra = 0.4
        self.right_angle_pts = [
            np.array([0.0,  ra, 0.0]),
            np.array([0.0,  ra,  ra]),
            np.array([0.0, 0.0,  ra]),
            np.array([0.0, 0.0, 0.0]),
        ]

        # --- 验证 ---
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-6

        # 验证平行面: 两面法向量平行（均为 z 轴方向）
        n_alpha_par = np.array([0, 0, 1], dtype=float)
        n_beta_par  = np.array([0, 0, 1], dtype=float)
        assert np.linalg.norm(np.cross(n_alpha_par, n_beta_par)) < eps, \
            "平行场景: 两面应平行"

        # 验证 60° 相交面的二面角
        # α 法向量: (0,0,1), β 法向量需从旋转后的角求
        # β = α 绕 x 旋转 60°, β 的法向量 = rotate_x((0,0,1), 60°)
        n_beta_60 = rotate_around_x(np.array([0, 0, 1], dtype=float), 60 * DEGREES)
        angle_60_deg = dihedral_angle_planes([0, 0, 1], n_beta_60)
        assert abs(angle_60_deg - 60.0) < 0.01, \
            f"相交场景: 期望60°, 实际{angle_60_deg:.2f}°"

        # 验证 90° 垂直面的二面角
        n_beta_90 = rotate_around_x(np.array([0, 0, 1], dtype=float), 90 * DEGREES)
        angle_90_deg = dihedral_angle_planes([0, 0, 1], n_beta_90)
        assert abs(angle_90_deg - 90.0) < 0.01, \
            f"垂直场景: 期望90°, 实际{angle_90_deg:.2f}°"

        # 验证直角标记点的垂直性
        v1 = self.right_angle_pts[1] - self.right_angle_pts[0]  # 沿 z 方向
        v2 = self.right_angle_pts[0] - self.right_angle_pts[3]  # 沿 y 方向
        assert abs(np.dot(v1, v2)) < eps, "直角标记向量应垂直"

        print("✅ 几何验证全部通过")
        print(f"   60° 二面角: {angle_60_deg:.4f}°")
        print(f"   90° 二面角: {angle_90_deg:.4f}°")

    # ================================================================
    #   辅助创建方法
    # ================================================================

    def _fixed_text(self, text, y, size, color):
        """创建固定在帧中的中文文字 (不随相机旋转)."""
        obj = Text(text, font="Noto Sans CJK SC", font_size=size, color=color)
        obj.move_to(np.array([0.0, y, 0.0]))
        self.add_fixed_in_frame_mobjects(obj)
        return obj

    def _fixed_formula(self, latex, y, size, color):
        """创建固定在帧中的 LaTeX 公式."""
        obj = MathTex(latex, font_size=size, color=color)
        obj.move_to(np.array([0.0, y, 0.0]))
        self.add_fixed_in_frame_mobjects(obj)
        return obj

    def _make_plane(self, corners, color, opacity=0.45):
        """根据四顶点创建带填充的平面多边形."""
        return Polygon(
            *corners,
            fill_color=color,
            fill_opacity=opacity,
            stroke_color=color,
            stroke_width=2.5,
        )

    def _label_3d(self, text, pos, color, size=40):
        """3D 空间内的平面标签（Text 对象）."""
        obj = Text(text, font="Noto Sans CJK SC", font_size=size, color=color)
        obj.move_to(pos)
        return obj

    def _fade_all(self, *objs, rt=0.5):
        """批量淡出一组对象."""
        if objs:
            self.play(*[FadeOut(o) for o in objs], run_time=rt)

    # ================================================================
    #   Scene 1 — 开场 Hook
    # ================================================================

    def _scene_1_opening(self):
        # 钩子标题
        hook = self._fixed_text(
            "两个平面，相遇会怎样？", 5.2, 36, WHITE
        )
        sub = self._fixed_text(
            "面面位置关系  全解析", 4.2, 28, self.C_TITLE
        )

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=DOWN * 0.2), run_time=0.5)

        # 用一个长方体顶面(α)和底面(β)演示"两个平面"
        top = self._make_plane(self.par_alpha_corners, self.C_ALPHA, opacity=0.55)
        bot = self._make_plane(self.par_beta_corners,  self.C_BETA,  opacity=0.55)

        self.play(Create(top), run_time=0.8)
        self.play(Create(bot), run_time=0.8)

        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1.8)
        self.stop_ambient_camera_rotation()

        self._fade_all(hook, sub, top, bot, rt=0.5)

    # ================================================================
    #   Scene 2 — 平行关系
    # ================================================================

    def _scene_2_parallel(self):
        title = self._fixed_text(
            "① 平行：没有公共点", 5.5, 34, self.C_ALPHA
        )

        alpha = self._make_plane(self.par_alpha_corners, self.C_ALPHA)
        beta  = self._make_plane(self.par_beta_corners,  self.C_BETA)

        # 3D 标签 —— 放在平面右上角附近
        a_lbl = self._label_3d(
            "α", np.array([self.PW + 0.35, self.PH, 1.0]), self.C_ALPHA
        )
        b_lbl = self._label_3d(
            "β", np.array([self.PW + 0.35, self.PH, -1.0]), self.C_BETA
        )

        formula    = self._fixed_formula(r"\alpha \parallel \beta", -5.0, 48, self.C_FORMULA)
        no_common  = self._fixed_text("永不相交，没有公共点", -6.2, 26, "#e74c3c")

        self.play(Write(title), run_time=0.5)
        self.play(Create(alpha), FadeIn(a_lbl), run_time=1.0)
        self.play(Create(beta),  FadeIn(b_lbl), run_time=1.0)
        self.play(Write(formula), run_time=0.6)
        self.play(FadeIn(no_common), run_time=0.4)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self._fade_all(
            title, alpha, beta, a_lbl, b_lbl, formula, no_common
        )

    # ================================================================
    #   Scene 3 — 相交关系
    # ================================================================

    def _scene_3_intersecting(self):
        title = self._fixed_text(
            "② 相交：有一条公共直线（交线）", 5.5, 30, self.C_BETA
        )

        alpha = self._make_plane(self.alpha_flat_corners, self.C_ALPHA)
        beta  = self._make_plane(self.beta_60_corners,    self.C_BETA)

        # 交线 (黄色 Line3D)
        inter_line = Line3D(
            self.inter_start,
            self.inter_end,
            color=self.C_LINE,
            thickness=0.055,
        )

        # 3D 标签
        a_lbl = self._label_3d(
            "α",
            np.array([self.PW + 0.35, self.PH, 0.0]),
            self.C_ALPHA,
        )
        # β 标签跟随旋转后的角点
        b_corner = rotate_around_x(
            np.array([self.PW + 0.35, -self.PH, 0.0]),
            60 * DEGREES,
        )
        b_lbl = self._label_3d("β", b_corner, self.C_BETA)

        l_label = self._fixed_text("交线 l", -4.5, 26, self.C_LINE)
        formula  = self._fixed_formula(r"\alpha \cap \beta = l", -5.5, 48, self.C_FORMULA)
        angle_note = self._fixed_text("二面角 = 60°（示例）", -6.5, 22, self.C_TEXT)

        self.play(Write(title), run_time=0.5)
        self.play(Create(alpha), FadeIn(a_lbl), run_time=0.8)
        # 动态展开 β (从铰链线处展开的感觉)
        self.play(Create(beta), FadeIn(b_lbl), run_time=1.2)
        self.play(Create(inter_line), FadeIn(l_label), run_time=0.7)
        self.play(
            Flash(inter_line, color=self.C_LINE, flash_radius=0.25),
            run_time=0.5,
        )
        self.play(Write(formula), FadeIn(angle_note), run_time=0.6)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self._fade_all(
            title, alpha, beta, a_lbl, b_lbl,
            inter_line, l_label, formula, angle_note
        )

    # ================================================================
    #   Scene 4 — 垂直关系
    # ================================================================

    def _scene_4_perpendicular(self):
        title = self._fixed_text(
            "③ 垂直：相交的特殊情况（90°）", 5.5, 30, self.C_PERP
        )

        alpha = self._make_plane(self.alpha_flat_corners, self.C_ALPHA)
        beta  = self._make_plane(self.beta_90_corners,    self.C_BETA)

        # 交线
        inter_line = Line3D(
            self.inter_start,
            self.inter_end,
            color=self.C_LINE,
            thickness=0.055,
        )

        # 直角标记 (yz 平面内的小正方形)
        right_angle_mark = Polygon(
            *self.right_angle_pts,
            fill_opacity=0,
            stroke_color=YELLOW,
            stroke_width=2.5,
        )

        # 3D 标签
        a_lbl = self._label_3d(
            "α",
            np.array([self.PW + 0.35, self.PH, 0.0]),
            self.C_ALPHA,
        )
        b_lbl = self._label_3d(
            "β",
            np.array([self.PW + 0.35, 0.0, self.PH]),
            self.C_BETA,
        )

        degree_note = self._fixed_text("二面角 = 90°", -4.2, 28, YELLOW)
        formula     = self._fixed_formula(r"\alpha \perp \beta", -5.2, 52, self.C_PERP)
        judgment    = self._fixed_text(
            "判定法：平面过垂线 → 两平面垂直", -6.5, 21, self.C_TEXT
        )

        self.play(Write(title), run_time=0.5)
        self.play(Create(alpha), FadeIn(a_lbl), run_time=0.8)
        self.play(Create(beta),  FadeIn(b_lbl), run_time=0.8)
        self.play(Create(inter_line), Create(right_angle_mark), run_time=0.6)
        self.play(FadeIn(degree_note), Write(formula), run_time=0.6)
        self.play(FadeIn(judgment), run_time=0.4)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self._fade_all(
            title, alpha, beta, a_lbl, b_lbl,
            inter_line, right_angle_mark,
            degree_note, formula, judgment,
        )

    # ================================================================
    #   Scene 5 — 总结
    # ================================================================

    def _scene_5_summary(self):
        sum_title = self._fixed_text("总结：面面位置关系", 6.5, 36, self.C_TITLE)
        self.play(FadeIn(sum_title), run_time=0.4)

        items = [
            ("① 平行",  r"\alpha \parallel \beta",  "没有公共点",               self.C_ALPHA),
            ("② 相交",  r"\alpha \cap \beta = l",   "有一条公共直线（交线 l）",   self.C_BETA),
            ("③ 垂直",  r"\alpha \perp \beta",       "相交的特殊情况（90°）",     self.C_PERP),
        ]
        y_tops = [4.5, 2.0, -0.5]
        all_items = [sum_title]

        for (name, formula, desc, color), y in zip(items, y_tops):
            name_obj = self._fixed_text(name,   y,       32, color)
            form_obj = self._fixed_formula(formula, y - 0.85, 36, color)
            desc_obj = self._fixed_text(desc,   y - 1.7, 22, self.C_TEXT)

            self.play(FadeIn(name_obj), Write(form_obj), run_time=0.6)
            self.play(FadeIn(desc_obj), run_time=0.3)
            self.wait(0.6)

            all_items += [name_obj, form_obj, desc_obj]

        key = self._fixed_text(
            "只有两种关系：平行 或 相交（垂直是特殊相交）",
            -3.5, 24, YELLOW,
        )
        all_items.append(key)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)

        self._fade_all(*all_items, rt=0.5)

    # ================================================================
    #   Scene 6 — 片尾
    # ================================================================

    def _scene_6_outro(self):
        self.play(FadeOut(self.author_strip), run_time=0.3)

        big_name = self._fixed_text(AUTHOR_NAME, 2.0, 42, WHITE)
        big_id   = self._fixed_text(AUTHOR_ID,   0.8, 32, self.C_AUTHOR)
        follow   = self._fixed_text(
            "关注我，获得更多数学技巧！", -0.8, 30, YELLOW
        )

        self.play(FadeIn(big_name), FadeIn(big_id), run_time=0.8)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)
        self.wait(2.5)

        self._fade_all(big_name, big_id, follow, rt=0.8)


# ===================================================
#   渲染命令参考
# ===================================================
# 快速预览 (480p):
#   manim -pql plane_relationships.py PlaneRelationships
#
# 高质量 (1080p):
#   manim -qh plane_relationships.py PlaneRelationships
#
# 4K:
#   manim -qk plane_relationships.py PlaneRelationships
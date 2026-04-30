"""
空间直线与直线的位置关系 - 教学动画
六年级第二学期 第八章 长方体的再认识
知识点：空间中两条直线的位置关系（平行、相交、异面）

格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql spatial_lines.py SpatialLinesScene   # 快速预览 (480p)
  manim -qh  spatial_lines.py SpatialLinesScene   # 高质量 (1080p)
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
#  全局配置 — TikTok 竖屏 1080×1920
# ─────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────
#  颜色配置
# ─────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
COLOR_TITLE     = "#f0c040"
COLOR_PARALLEL  = "#3ecf8e"   # 绿 — 平行
COLOR_INTERSECT = "#e05c5c"   # 红 — 相交
COLOR_SKEW      = "#7b9fff"   # 蓝 — 异面
COLOR_BOX       = "#c8d8f0"   # 长方体棱
COLOR_AUX       = "#888888"
COLOR_HIGHLIGHT = YELLOW
COLOR_AUTHOR    = "#aaaacc"
FONT_CN         = "PingFang SC"


# ─────────────────────────────────────────────
#  辅助函数
# ─────────────────────────────────────────────
def cn(text, size=24, color=WHITE):
    return Text(text, font=FONT_CN, font_size=size, color=color)


# ═════════════════════════════════════════════
#  主场景
# ═════════════════════════════════════════════
class SpatialLinesScene(ThreeDScene):
    """
    场景顺序
    ──────────────────────────────
    1. 开场钩子          ~4 s
    2. 建立长方体        ~4 s
    3. 平行直线          ~8 s
    4. 相交直线          ~8 s
    5. 异面直线          ~10 s
    6. 总结对比          ~6 s
    7. 片尾              ~3 s
    ──────────────────────────────
    Total: ~43 s
    """

    # ─────────── 初始化入口 ───────────

    def construct(self):
        self.camera.background_color = BG_COLOR
        self._setup_geometry()

        # 全程水印
        self.watermark = cn(
            "上海初高中数学直通车 @emptyandcalm",
            size=18, color=COLOR_AUTHOR
        ).to_edge(UP, buff=0.30)
        self.add_fixed_in_frame_mobjects(self.watermark)
        self.play(FadeIn(self.watermark), run_time=0.3)

        self._scene_hook()
        self._scene_build_box()
        self._scene_parallel()
        self._scene_intersect()
        self._scene_skew()
        self._scene_summary()
        self._scene_outro()

    # ─────────── 几何数据（精确计算） ───────────

    def _setup_geometry(self):
        """
        长方体 8 顶点坐标统一在此初始化。
        坐标系：x→右，y→上，z→屏幕外（Manim 默认 ThreeDScene）。
        """
        W, H, D = 2.6, 2.0, 1.8   # 宽×高×深
        cx, cy, cz = 0.0, 0.4, 0.0  # 整体偏移（竖屏向上留字幕区）

        self.vA  = np.array([cx - W/2, cy - H/2,  D/2])
        self.vB  = np.array([cx + W/2, cy - H/2,  D/2])
        self.vC  = np.array([cx + W/2, cy - H/2, -D/2])
        self.vD  = np.array([cx - W/2, cy - H/2, -D/2])
        self.vE  = np.array([cx - W/2, cy + H/2,  D/2])
        self.vF  = np.array([cx + W/2, cy + H/2,  D/2])
        self.vG  = np.array([cx + W/2, cy + H/2, -D/2])
        self.vH  = np.array([cx - W/2, cy + H/2, -D/2])

        # 12 条棱（端点对）
        self.EDGES = [
            (self.vA, self.vB), (self.vB, self.vC),
            (self.vC, self.vD), (self.vD, self.vA),   # 底面
            (self.vE, self.vF), (self.vF, self.vG),
            (self.vG, self.vH), (self.vH, self.vE),   # 顶面
            (self.vA, self.vE), (self.vB, self.vF),
            (self.vC, self.vG), (self.vD, self.vH),   # 竖棱
        ]

        # 几何验证
        self._verify_geometry()

    def _verify_geometry(self):
        """验证长方体对角线等长（空间对角线）"""
        d1 = np.linalg.norm(self.vG - self.vA)
        d2 = np.linalg.norm(self.vH - self.vB)
        d3 = np.linalg.norm(self.vF - self.vD)
        d4 = np.linalg.norm(self.vE - self.vC)
        eps = 1e-9
        assert abs(d1 - d2) < eps and abs(d2 - d3) < eps and abs(d3 - d4) < eps, \
            f"长方体空间对角线不等: {d1:.4f},{d2:.4f},{d3:.4f},{d4:.4f}"
        # 验证 AB ∥ DC（方向向量平行）
        AB = self.vB - self.vA
        DC = self.vC - self.vD
        cross = np.cross(AB, DC)
        assert np.linalg.norm(cross) < eps, "AB 和 DC 不平行！"
        print("✓ 几何验证通过")

    # ─────────── 辅助：搭建长方体 VGroup ───────────

    def _make_box(self, hl_edges=None, hl_color=WHITE, base_width=2, hl_width=4):
        """返回 VGroup of Line3D，可高亮指定棱。"""
        grp = VGroup()
        for s, e in self.EDGES:
            is_hl = False
            if hl_edges:
                for hs, he in hl_edges:
                    if (np.allclose(s, hs) and np.allclose(e, he)) or \
                       (np.allclose(s, he) and np.allclose(e, hs)):
                        is_hl = True
                        break
            grp.add(Line3D(s, e,
                           color=hl_color if is_hl else COLOR_BOX,
                           stroke_width=hl_width if is_hl else base_width))
        return grp

    # ─────────── 场景 1：开场钩子 ───────────

    def _scene_hook(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        q1 = cn("空间里两条直线", size=50, color=COLOR_TITLE)
        q2 = cn("有几种位置关系？", size=46, color=WHITE)
        q_grp = VGroup(q1, q2).arrange(DOWN, buff=0.45).move_to(UP * 1.5)

        self.add_fixed_in_frame_mobjects(q_grp)
        self.play(Write(q1), run_time=0.9)
        self.play(Write(q2), run_time=0.9)
        self.wait(0.6)

        answers = VGroup(
            cn("① 平行", size=38, color=COLOR_PARALLEL),
            cn("② 相交", size=38, color=COLOR_INTERSECT),
            cn("③ 异面", size=38, color=COLOR_SKEW),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 1.2)

        self.add_fixed_in_frame_mobjects(answers)
        for a in answers:
            self.play(FadeIn(a, shift=RIGHT * 0.4), run_time=0.45)
        self.wait(1.0)

        self.play(FadeOut(q_grp), FadeOut(answers), run_time=0.5)
        self.remove_fixed_in_frame_mobjects(q_grp, answers)

    # ─────────── 场景 2：建立长方体 ───────────

    def _scene_build_box(self):
        title = cn("用长方体来理解", size=36, color=COLOR_TITLE).to_edge(UP, buff=1.1)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        self.title_bar = title

        self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES)

        self.box = self._make_box()
        self.play(Create(self.box), run_time=1.5)

        # 顶点标注
        label_data = {
            "A": (self.vA, LEFT * 0.25 + DOWN * 0.2),
            "B": (self.vB, RIGHT * 0.25 + DOWN * 0.2),
            "C": (self.vC, RIGHT * 0.25 + DOWN * 0.2),
            "D": (self.vD, LEFT * 0.25 + DOWN * 0.2),
            "E": (self.vE, LEFT * 0.25 + UP * 0.15),
            "F": (self.vF, RIGHT * 0.25 + UP * 0.15),
            "G": (self.vG, RIGHT * 0.25 + UP * 0.15),
            "H": (self.vH, LEFT * 0.25 + UP * 0.15),
        }
        self.vlabels = VGroup()
        for name, (pos, off) in label_data.items():
            self.vlabels.add(
                Text(name, font_size=18, color=COLOR_AUX).move_to(pos + off)
            )
        self.play(FadeIn(self.vlabels), run_time=0.7)

        note = cn("长方体共 12 条棱", size=26, color=COLOR_AUX).to_edge(DOWN, buff=5.2)
        self.add_fixed_in_frame_mobjects(note)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(note), run_time=0.3)
        self.remove_fixed_in_frame_mobjects(note)

    # ─────────── 工具：切换标题栏 ───────────

    def _switch_title(self, text, color=COLOR_TITLE):
        new = cn(text, size=36, color=color).to_edge(UP, buff=1.1)
        self.add_fixed_in_frame_mobjects(new)
        self.play(FadeOut(self.title_bar), FadeIn(new, shift=DOWN * 0.2), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(self.title_bar)
        self.title_bar = new

    # ─────────── 场景 3：平行 ───────────

    def _scene_parallel(self):
        self._switch_title("① 平行直线", COLOR_PARALLEL)

        # AB ∥ DC（底面两条对边）
        lAB = Line3D(self.vA, self.vB, color=COLOR_PARALLEL, stroke_width=5)
        lDC = Line3D(self.vD, self.vC, color=COLOR_PARALLEL, stroke_width=5)

        self.play(Create(lAB), Create(lDC), run_time=0.9)
        self.play(
            Flash(lAB, color=COLOR_PARALLEL, flash_radius=0.5),
            Flash(lDC, color=COLOR_PARALLEL, flash_radius=0.5),
            run_time=0.6,
        )

        defn = VGroup(
            cn("平行：在同一平面内，", size=24, color=WHITE),
            cn("永不相交", size=30, color=COLOR_PARALLEL),
            cn("记作 AB ∥ DC", size=26, color=COLOR_HIGHLIGHT),
        ).arrange(DOWN, buff=0.22).to_edge(DOWN, buff=4.6)
        self.add_fixed_in_frame_mobjects(defn)
        self.play(FadeIn(defn, shift=UP * 0.3), run_time=0.7)
        self.wait(1.0)

        # 延伸为箭头，强调"方向相同，永不相交"
        arr1 = Arrow3D(
            self.vA + LEFT * 0.5, self.vB + RIGHT * 0.7,
            color=COLOR_PARALLEL, thickness=0.04
        )
        arr2 = Arrow3D(
            self.vD + LEFT * 0.5, self.vC + RIGHT * 0.7,
            color=COLOR_PARALLEL, thickness=0.04
        )
        self.play(Transform(lAB, arr1), Transform(lDC, arr2), run_time=0.9)
        self.wait(0.8)

        # EF 也平行于 AB
        note = cn("上方 EF 也平行于 AB（对应棱）", size=22, color=COLOR_AUX).to_edge(DOWN, buff=3.5)
        self.add_fixed_in_frame_mobjects(note)
        lEF = Line3D(self.vE, self.vF, color=COLOR_PARALLEL, stroke_width=4)
        self.play(Create(lEF), FadeIn(note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(lAB), FadeOut(lDC), FadeOut(lEF),
            FadeOut(defn), FadeOut(note), run_time=0.5
        )
        self.remove_fixed_in_frame_mobjects(defn, note)

    # ─────────── 场景 4：相交 ───────────

    def _scene_intersect(self):
        self._switch_title("② 相交直线", COLOR_INTERSECT)

        # AB 与 AE 在顶点 A 处相交
        lAB = Line3D(self.vA, self.vB, color=COLOR_INTERSECT, stroke_width=5)
        lAE = Line3D(self.vA, self.vE, color=COLOR_INTERSECT, stroke_width=5)

        self.play(Create(lAB), Create(lAE), run_time=0.9)

        dot_A = Sphere(center=self.vA, radius=0.13,
                       fill_color=COLOR_HIGHLIGHT, fill_opacity=1)
        self.play(GrowFromCenter(dot_A), run_time=0.5)
        self.play(Flash(dot_A, color=COLOR_HIGHLIGHT, flash_radius=0.55), run_time=0.4)

        defn = VGroup(
            cn("相交：有且只有", size=24, color=WHITE),
            cn("一个公共点", size=30, color=COLOR_INTERSECT),
            cn("a ∩ b = {A}", size=26, color=COLOR_HIGHLIGHT),
        ).arrange(DOWN, buff=0.22).to_edge(DOWN, buff=4.6)
        self.add_fixed_in_frame_mobjects(defn)
        self.play(FadeIn(defn, shift=UP * 0.3), run_time=0.7)
        self.wait(1.0)

        # 底面对角线也相交（中心点）
        note = cn("底面对角线 AC、BD 也相交", size=22, color=COLOR_AUX).to_edge(DOWN, buff=3.5)
        self.add_fixed_in_frame_mobjects(note)
        dAC = Line3D(self.vA, self.vC, color=COLOR_INTERSECT, stroke_width=3)
        dBD = Line3D(self.vB, self.vD, color=COLOR_INTERSECT, stroke_width=3)
        mid = (self.vA + self.vC) / 2   # 精确计算底面中心
        dot_mid = Sphere(center=mid, radius=0.10,
                         fill_color=COLOR_HIGHLIGHT, fill_opacity=1)

        self.play(Create(dAC), Create(dBD), FadeIn(note), run_time=0.8)
        self.play(GrowFromCenter(dot_mid), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(lAB), FadeOut(lAE), FadeOut(dot_A),
            FadeOut(dAC), FadeOut(dBD), FadeOut(dot_mid),
            FadeOut(defn), FadeOut(note), run_time=0.5
        )
        self.remove_fixed_in_frame_mobjects(defn, note)

    # ─────────── 场景 5：异面 ───────────

    def _scene_skew(self):
        self._switch_title("③ 异面直线（最特殊）", COLOR_SKEW)

        # AB（底面前棱）与 CG（右后竖棱）—— 典型异面
        lAB = Line3D(self.vA, self.vB, color=COLOR_SKEW,   stroke_width=5)
        lCG = Line3D(self.vC, self.vG, color="#ff9f43", stroke_width=5)

        self.play(Create(lAB), run_time=0.6)
        self.play(Create(lCG), run_time=0.6)

        # 旋转让学生看清空间关系
        self.begin_ambient_camera_rotation(rate=0.28)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        defn = VGroup(
            cn("异面：不在任何同一平面内", size=24, color=WHITE),
            cn("既不平行，也不相交", size=26, color=COLOR_SKEW),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=4.6)
        self.add_fixed_in_frame_mobjects(defn)
        self.play(FadeIn(defn, shift=UP * 0.3), run_time=0.7)
        self.wait(0.8)

        # 半透明底面：AB 在底面内
        bot_face = Polygon(
            self.vA, self.vB, self.vC, self.vD,
            fill_color=COLOR_SKEW, fill_opacity=0.13,
            stroke_color=COLOR_SKEW, stroke_width=1,
        )
        n1 = cn("AB 在底面内", size=22, color=COLOR_AUX).to_edge(DOWN, buff=3.5)
        self.add_fixed_in_frame_mobjects(n1)
        self.play(Create(bot_face), FadeIn(n1), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(bot_face), FadeOut(n1), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(n1)

        # 半透明右侧面：CG 在右侧面内
        right_face = Polygon(
            self.vB, self.vC, self.vG, self.vF,
            fill_color="#ff9f43", fill_opacity=0.13,
            stroke_color="#ff9f43", stroke_width=1,
        )
        n2 = cn("CG 在右侧面内", size=22, color=COLOR_AUX).to_edge(DOWN, buff=3.5)
        self.add_fixed_in_frame_mobjects(n2)
        self.play(Create(right_face), FadeIn(n2), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(right_face), FadeOut(n2), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(n2)

        n3 = cn("两条线所在的面不同 → 异面！", size=26, color=COLOR_HIGHLIGHT).to_edge(DOWN, buff=3.5)
        self.add_fixed_in_frame_mobjects(n3)
        self.play(
            Flash(lAB, color=COLOR_SKEW,  flash_radius=0.5),
            Flash(lCG, color="#ff9f43",   flash_radius=0.5),
            FadeIn(n3),
            run_time=0.8,
        )
        self.wait(1.5)

        self.play(
            FadeOut(lAB), FadeOut(lCG),
            FadeOut(defn), FadeOut(n3), run_time=0.5
        )
        self.remove_fixed_in_frame_mobjects(defn, n3)

    # ─────────── 场景 6：总结 ───────────

    def _scene_summary(self):
        self.play(FadeOut(self.box), FadeOut(self.vlabels), run_time=0.5)

        # 切回正视角做 2D 总结卡
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self._switch_title("三种位置关系", COLOR_TITLE)

        rows = [
            ("∥", "平行", "同一平面内，不相交",   "a ∥ b",         COLOR_PARALLEL),
            ("✕", "相交", "有且只有一个公共点",   "a ∩ b = {P}",   COLOR_INTERSECT),
            ("≠", "异面", "不在同一平面内",        "既不平行也不相交", COLOR_SKEW),
        ]

        cards = VGroup()
        for icon_s, name_s, key_s, sym_s, col in rows:
            bg = RoundedRectangle(
                width=7.6, height=2.9,
                corner_radius=0.28,
                fill_color=col, fill_opacity=0.10,
                stroke_color=col, stroke_width=2,
            )
            icon = Text(icon_s, font_size=46, color=col)
            name = cn(name_s, size=32, color=col)
            key  = cn(key_s,  size=21, color=WHITE)
            sym  = cn(sym_s,  size=21, color=COLOR_HIGHLIGHT)
            right = VGroup(name, key, sym).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            row   = VGroup(icon, right).arrange(RIGHT, buff=0.45).move_to(bg.get_center())
            cards.add(VGroup(bg, row))

        cards.arrange(DOWN, buff=0.38).move_to(DOWN * 0.25)
        self.add_fixed_in_frame_mobjects(cards)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.55)

        # 口诀
        mnemonic = cn(
            "口诀：平不交  交一点  异面最特殊",
            size=24, color=COLOR_HIGHLIGHT
        ).to_edge(DOWN, buff=3.0)
        self.add_fixed_in_frame_mobjects(mnemonic)
        self.play(FadeIn(mnemonic, shift=UP * 0.3), run_time=0.6)
        self.wait(2.2)

        self.play(FadeOut(cards), FadeOut(mnemonic), run_time=0.5)
        self.remove_fixed_in_frame_mobjects(cards, mnemonic)

    # ─────────── 场景 7：片尾 ───────────

    def _scene_outro(self):
        self.play(FadeOut(self.title_bar), run_time=0.3)
        self.remove_fixed_in_frame_mobjects(self.title_bar)

        a_name = cn("上海初高中数学直通车", size=42, color=WHITE).move_to(UP * 1.8)
        a_id   = cn("@emptyandcalm",        size=30, color=COLOR_AUTHOR).move_to(UP * 0.9)
        follow = cn("关注我，获得更多数学技巧！", size=30, color=COLOR_HIGHLIGHT).move_to(DOWN * 0.2)

        icons = VGroup(
            cn("∥", size=40, color=COLOR_PARALLEL),
            cn("✕", size=40, color=COLOR_INTERSECT),
            cn("≠", size=40, color=COLOR_SKEW),
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 2.0)

        self.add_fixed_in_frame_mobjects(a_name, a_id, follow, icons)
        self.play(FadeIn(a_name, shift=DOWN * 0.3), FadeIn(a_id), run_time=0.8)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)
        self.play(FadeIn(icons, scale=0.7), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(a_name), FadeOut(a_id), FadeOut(follow),
            FadeOut(icons), FadeOut(self.watermark),
            run_time=1.0,
        )
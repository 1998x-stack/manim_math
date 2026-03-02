"""
cuboid_animation.py  —  长方体的棱长和、表面积和体积
年级: 六年级第二学期 | 格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql cuboid_animation.py CuboidLesson   # 快速预览 (480p)
  manim -qh  cuboid_animation.py CuboidLesson   # 高质量 (1080p)
"""

from manim import *
import numpy as np

# ── 竖屏配置 ─────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 全局常量 ──────────────────────────────────────────
FONT        = "Noto Sans CJK SC"
BG          = "#1a1a2e"
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID   = "@emptyandcalm"

# 长方体尺寸
DIM_A = 2.0   # 长 (x方向)
DIM_B = 1.4   # 宽 (z方向)
DIM_C = 1.0   # 高 (y方向)

# Prism 内使用: dimensions=[A, C, B]
PRISM_DIMS = [DIM_A, DIM_C, DIM_B]

# 配色
C_BOX      = "#4a90d9"   # 主体蓝
C_EDGE_A   = "#f1c40f"   # 长棱 黄
C_EDGE_B   = "#2ecc71"   # 宽棱 绿
C_EDGE_C   = "#e74c3c"   # 高棱 红
C_FACE_AB  = "#f39c12"   # ab面 橙
C_FACE_BC  = "#9b59b6"   # bc面 紫
C_FACE_CA  = "#00cec9"   # ca面 青
C_FORMULA  = "#55efc4"   # 公式绿
C_HL       = "#f1c40f"   # 高亮黄
C_CUBE     = "#fd79a8"   # 正方体粉


# ═══════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════

def cn(text, size=24, color=WHITE, pos=None):
    """创建中文 Text"""
    t = Text(text, font=FONT, font_size=size, color=color)
    if pos is not None:
        t.move_to(pos)
    return t


def fml(latex, size=30, color=WHITE):
    """创建 MathTex (纯 ASCII / LaTeX)"""
    return MathTex(latex, font_size=size, color=color)


def make_prism(a=DIM_A, b=DIM_B, c=DIM_C, opacity=0.55, color=C_BOX):
    """创建长方体 Prism，居中在 ORIGIN"""
    p = Prism(
        dimensions=[a, c, b],
        fill_color=color,
        fill_opacity=opacity,
        stroke_color=WHITE,
        stroke_width=0.5,
    )
    return p


def get_corners(a=DIM_A, b=DIM_B, c=DIM_C):
    """
    返回长方体 8 个顶点坐标 (numpy数组)
    Prism dimensions=[a, c, b] → x∈[-a/2,a/2], y∈[-c/2,c/2], z∈[-b/2,b/2]
    """
    hx, hy, hz = a / 2, c / 2, b / 2
    return np.array([
        [-hx, -hy, -hz],   # 0
        [ hx, -hy, -hz],   # 1
        [ hx,  hy, -hz],   # 2
        [-hx,  hy, -hz],   # 3
        [-hx, -hy,  hz],   # 4
        [ hx, -hy,  hz],   # 5
        [ hx,  hy,  hz],   # 6
        [-hx,  hy,  hz],   # 7
    ])


def make_edges(a=DIM_A, b=DIM_B, c=DIM_C, sw=3):
    """
    创建 12 条棱的 Line3D，分三组返回
    返回: (group_a, group_b, group_c)
      group_a: 4条 长棱 (x方向, 长度=a)  → C_EDGE_A
      group_b: 4条 宽棱 (z方向, 长度=b)  → C_EDGE_B
      group_c: 4条 高棱 (y方向, 长度=c)  → C_EDGE_C
    """
    v = get_corners(a, b, c)

    long_pairs   = [(v[0],v[1]), (v[3],v[2]), (v[4],v[5]), (v[7],v[6])]
    wide_pairs   = [(v[0],v[4]), (v[1],v[5]), (v[2],v[6]), (v[3],v[7])]
    height_pairs = [(v[0],v[3]), (v[1],v[2]), (v[4],v[7]), (v[5],v[6])]

    def grp(pairs, color):
        return VGroup(*[
            Line3D(start=p, end=q, color=color, stroke_width=sw)
            for p, q in pairs
        ])

    return grp(long_pairs, C_EDGE_A), grp(wide_pairs, C_EDGE_B), grp(height_pairs, C_EDGE_C)


def make_face(v_indices, corners, color, opacity=0.65):
    """创建一个面 (Polygon)"""
    pts = [corners[i] for i in v_indices]
    return Polygon(*pts,
                   fill_color=color, fill_opacity=opacity,
                   stroke_color=color, stroke_width=1.5)


def make_all_faces(a=DIM_A, b=DIM_B, c=DIM_C):
    """
    返回 6 个面的字典:
      'ab_top', 'ab_bot' : ab面 (上/下, y=±c/2)
      'bc_left','bc_right': bc面 (左/右, x=±a/2)
      'ca_front','ca_back': ca面 (前/后, z=±b/2)
    """
    v = get_corners(a, b, c)
    faces = {
        'ab_top':   make_face([3,2,6,7], v, C_FACE_AB),
        'ab_bot':   make_face([0,1,5,4], v, C_FACE_AB),
        'bc_right': make_face([1,2,6,5], v, C_FACE_BC),
        'bc_left':  make_face([0,3,7,4], v, C_FACE_BC),
        'ca_front': make_face([4,5,6,7], v, C_FACE_CA),
        'ca_back':  make_face([0,1,2,3], v, C_FACE_CA),
    }
    return faces


# ═══════════════════════════════════════════════════
# 主场景
# ═══════════════════════════════════════════════════

class CuboidLesson(ThreeDScene):

    def construct(self):
        self.camera.background_color = BG
        self._scene_opening()
        self._scene_parts()
        self._scene_edge_sum()
        self._scene_surface_area()
        self._scene_volume()
        self._scene_cube()
        self._scene_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场 (~5s)
    # ─────────────────────────────────────────────
    def _scene_opening(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        # 作者 (固定顶部)
        author = cn(AUTHOR_NAME + "  " + AUTHOR_ID, size=18, color=GRAY_B,
                    pos=[0, 7.2, 0])
        self.add_fixed_in_frame_mobjects(author)
        self.play(FadeIn(author, shift=DOWN * 0.15), run_time=0.3)

        # 大标题
        title = cn("长方体", size=64, color=C_HL, pos=[0, 6.5, 0])
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.7)

        sub = cn("棱长、表面积、体积", size=28, color=GRAY_A, pos=[0, 5.7, 0])
        self.add_fixed_in_frame_mobjects(sub)
        self.play(FadeIn(sub), run_time=0.4)

        # 3D 长方体
        prism = make_prism()
        self.play(Create(prism), run_time=1.0)

        # 三组彩棱快速亮起
        ga, gb, gc = make_edges()
        self.play(
            LaggedStart(Create(ga), Create(gb), Create(gc), lag_ratio=0.25),
            run_time=1.0
        )

        # 缓慢旋转
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1.5)
        self.stop_ambient_camera_rotation()

        # 钩子
        hook = cn("三个公式，三分钟搞定!", size=28, color=C_HL, pos=[0, -5.5, 0])
        self.add_fixed_in_frame_mobjects(hook)
        self.play(FadeIn(hook, scale=1.1), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(hook), FadeOut(author),
            FadeOut(prism), FadeOut(ga), FadeOut(gb), FadeOut(gc),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 2: 认识各部分 (~8s)
    # ─────────────────────────────────────────────
    def _scene_parts(self):
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=0.3)

        title = cn("认识长方体", size=34, color=C_HL, pos=[0, 6.8, 0])
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # 半透明长方体
        prism = make_prism(opacity=0.30)
        self.play(Create(prism), run_time=0.8)

        # 所有棱 (初始灰白)
        v = get_corners()
        all_edge_pairs = [
            (v[0],v[1]), (v[3],v[2]), (v[4],v[5]), (v[7],v[6]),
            (v[0],v[4]), (v[1],v[5]), (v[2],v[6]), (v[3],v[7]),
            (v[0],v[3]), (v[1],v[2]), (v[4],v[7]), (v[5],v[6]),
        ]
        base_edges = VGroup(*[
            Line3D(start=p, end=q, color=WHITE, stroke_width=2)
            for p, q in all_edge_pairs
        ])
        self.play(Create(base_edges), run_time=0.6)

        # ── 高亮 a (长棱, 黄色) ──
        ga, gb, gc = make_edges(sw=5)

        a_cn   = cn("长", size=22, color=C_EDGE_A)
        a_math = fml("a", size=30, color=C_EDGE_A)
        a_grp  = VGroup(a_cn, a_math).arrange(RIGHT, buff=0.1)
        a_grp.move_to([3.5, 2.5, 0])
        self.add_fixed_in_frame_mobjects(a_grp)

        self.play(Create(ga), FadeIn(a_grp), run_time=0.7)
        self.wait(0.3)

        # ── 高亮 b (宽棱, 绿色) ──
        b_cn   = cn("宽", size=22, color=C_EDGE_B)
        b_math = fml("b", size=30, color=C_EDGE_B)
        b_grp  = VGroup(b_cn, b_math).arrange(RIGHT, buff=0.1)
        b_grp.move_to([-3.5, 0.5, 0])
        self.add_fixed_in_frame_mobjects(b_grp)

        self.play(Create(gb), FadeIn(b_grp), run_time=0.7)
        self.wait(0.3)

        # ── 高亮 c (高棱, 红色) ──
        c_cn   = cn("高", size=22, color=C_EDGE_C)
        c_math = fml("c", size=30, color=C_EDGE_C)
        c_grp  = VGroup(c_cn, c_math).arrange(RIGHT, buff=0.1)
        c_grp.move_to([0, 4.5, 0])
        self.add_fixed_in_frame_mobjects(c_grp)

        self.play(Create(gc), FadeIn(c_grp), run_time=0.7)
        self.wait(0.3)

        # ── 面/棱/顶点小结 ──
        summary_cn   = cn("面6个  棱12条  顶点8个", size=24, color=GRAY_A, pos=[0, -5.0, 0])
        self.add_fixed_in_frame_mobjects(summary_cn)
        self.play(FadeIn(summary_cn), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(a_grp), FadeOut(b_grp), FadeOut(c_grp),
            FadeOut(summary_cn), FadeOut(prism), FadeOut(base_edges),
            FadeOut(ga), FadeOut(gb), FadeOut(gc),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 3: 棱长和 (~9s)
    # ─────────────────────────────────────────────
    def _scene_edge_sum(self):
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=0.3)

        title = cn("棱长和", size=38, color=C_HL, pos=[0, 6.8, 0])
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # 长方体 + 三组彩棱
        prism = make_prism(opacity=0.25)
        ga, gb, gc = make_edges(sw=5)
        self.play(Create(prism), Create(ga), Create(gb), Create(gc), run_time=1.0)

        # ── 说明: 4条长 ──
        row1_cn   = cn("4条长棱", size=26, color=C_EDGE_A)
        row1_math = fml(r"= 4a", size=32, color=C_EDGE_A)
        row1 = VGroup(row1_cn, row1_math).arrange(RIGHT, buff=0.2)
        row1.move_to([0, 5.5, 0])
        self.add_fixed_in_frame_mobjects(row1)
        self.play(FadeIn(row1), run_time=0.5)

        # ── 说明: 4条宽 ──
        row2_cn   = cn("4条宽棱", size=26, color=C_EDGE_B)
        row2_math = fml(r"= 4b", size=32, color=C_EDGE_B)
        row2 = VGroup(row2_cn, row2_math).arrange(RIGHT, buff=0.2)
        row2.move_to([0, 4.7, 0])
        self.add_fixed_in_frame_mobjects(row2)
        self.play(FadeIn(row2), run_time=0.5)

        # ── 说明: 4条高 ──
        row3_cn   = cn("4条高棱", size=26, color=C_EDGE_C)
        row3_math = fml(r"= 4c", size=32, color=C_EDGE_C)
        row3 = VGroup(row3_cn, row3_math).arrange(RIGHT, buff=0.2)
        row3.move_to([0, 3.9, 0])
        self.add_fixed_in_frame_mobjects(row3)
        self.play(FadeIn(row3), run_time=0.5)
        self.wait(0.4)

        # ── 推导公式 ──
        step1_cn   = cn("棱长和", size=26, color=WHITE)
        step1_math = fml(r"= 4a + 4b + 4c", size=30, color=WHITE)
        step1 = VGroup(step1_cn, step1_math).arrange(RIGHT, buff=0.2)
        step1.move_to([0, -4.5, 0])
        self.add_fixed_in_frame_mobjects(step1)
        self.play(Write(step1), run_time=0.7)

        step2_cn   = cn("化简", size=24, color=GRAY_A)
        step2_math = fml(r"= 4(a + b + c)", size=34, color=C_FORMULA)
        step2 = VGroup(step2_cn, step2_math).arrange(RIGHT, buff=0.2)
        step2.move_to([0, -5.4, 0])
        self.add_fixed_in_frame_mobjects(step2)
        self.play(FadeIn(step2_cn), Write(step2_math), run_time=0.8)

        # ── 代入示例 ──
        ex_cn  = cn(f"例: a=2, b=1.4, c=1", size=21, color=GRAY_B)
        ex_ans = fml(r"= 4\times(2+1.4+1) = 17.6", size=24, color=C_HL)
        ex = VGroup(ex_cn, ex_ans).arrange(RIGHT, buff=0.15)
        ex.move_to([0, -6.3, 0])
        self.add_fixed_in_frame_mobjects(ex)
        self.play(FadeIn(ex), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(row1), FadeOut(row2), FadeOut(row3),
            FadeOut(step1), FadeOut(step2), FadeOut(ex),
            FadeOut(prism), FadeOut(ga), FadeOut(gb), FadeOut(gc),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 4: 表面积 (~11s)
    # ─────────────────────────────────────────────
    def _scene_surface_area(self):
        self.move_camera(phi=65 * DEGREES, theta=-40 * DEGREES, run_time=0.4)

        title = cn("表面积", size=38, color=C_HL, pos=[0, 6.8, 0])
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        prism = make_prism(opacity=0.20)
        self.play(Create(prism), run_time=0.7)

        faces = make_all_faces()

        # ── 高亮 ab面 (上/下, 橙色) ──
        ab_top = faces['ab_top']
        ab_bot = faces['ab_bot']

        ab_cn   = cn("上/下两个面", size=22, color=C_FACE_AB)
        ab_math = fml(r"a \times b", size=28, color=C_FACE_AB)
        ab_label = VGroup(ab_cn, ab_math).arrange(RIGHT, buff=0.15)
        ab_label.move_to([-2.5, 5.2, 0])
        self.add_fixed_in_frame_mobjects(ab_label)
        self.play(FadeIn(ab_top), FadeIn(ab_bot), FadeIn(ab_label), run_time=0.7)
        self.wait(0.4)

        # ── 高亮 bc面 (左/右, 紫色) ──
        bc_l = faces['bc_left']
        bc_r = faces['bc_right']

        bc_cn   = cn("左/右两个面", size=22, color=C_FACE_BC)
        bc_math = fml(r"b \times c", size=28, color=C_FACE_BC)
        bc_label = VGroup(bc_cn, bc_math).arrange(RIGHT, buff=0.15)
        bc_label.move_to([2.8, 3.0, 0])
        self.add_fixed_in_frame_mobjects(bc_label)
        self.play(FadeIn(bc_l), FadeIn(bc_r), FadeIn(bc_label), run_time=0.7)
        self.wait(0.4)

        # ── 高亮 ca面 (前/后, 青色) ──
        ca_f = faces['ca_front']
        ca_b = faces['ca_back']

        ca_cn   = cn("前/后两个面", size=22, color=C_FACE_CA)
        ca_math = fml(r"c \times a", size=28, color=C_FACE_CA)
        ca_label = VGroup(ca_cn, ca_math).arrange(RIGHT, buff=0.15)
        ca_label.move_to([-2.0, 0.5, 0])
        self.add_fixed_in_frame_mobjects(ca_label)
        self.play(FadeIn(ca_f), FadeIn(ca_b), FadeIn(ca_label), run_time=0.7)
        self.wait(0.4)

        # ── 切换到"展开图"视角 (俯视) ──
        self.move_camera(phi=80 * DEGREES, theta=-30 * DEGREES, run_time=0.8)

        explain = cn("将六个面展开...", size=24, color=GRAY_A, pos=[0, -4.5, 0])
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(0.5)

        # 淡出3D元素，换2D展开示意
        self.play(
            FadeOut(prism),
            FadeOut(ab_top), FadeOut(ab_bot),
            FadeOut(bc_l), FadeOut(bc_r),
            FadeOut(ca_f), FadeOut(ca_b),
            FadeOut(explain),
            run_time=0.4
        )

        # ── 2D 展开矩形 (fixed-in-frame) ──
        # ab面: A × B → display 2.8×1.4 → scale 1.3 → 3.6×1.82
        sc = 1.3
        rect_ab = Rectangle(width=DIM_A * sc, height=DIM_B * sc,
                             fill_color=C_FACE_AB, fill_opacity=0.55,
                             stroke_color=C_FACE_AB, stroke_width=2)
        rect_ab.move_to([-2.5, 2.5, 0])

        rect_bc = Rectangle(width=DIM_B * sc, height=DIM_C * sc,
                             fill_color=C_FACE_BC, fill_opacity=0.55,
                             stroke_color=C_FACE_BC, stroke_width=2)
        rect_bc.move_to([2.0, 2.5, 0])

        rect_ca = Rectangle(width=DIM_C * sc, height=DIM_A * sc,
                             fill_color=C_FACE_CA, fill_opacity=0.55,
                             stroke_color=C_FACE_CA, stroke_width=2)
        rect_ca.move_to([0, 0.5, 0])

        lbl_ab = fml(r"ab", size=26, color=C_FACE_AB)
        lbl_bc = fml(r"bc", size=26, color=C_FACE_BC)
        lbl_ca = fml(r"ca", size=26, color=C_FACE_CA)
        lbl_ab.move_to(rect_ab.get_center())
        lbl_bc.move_to(rect_bc.get_center())
        lbl_ca.move_to(rect_ca.get_center())

        x2_ab = cn("×2", size=22, color=C_FACE_AB).next_to(rect_ab, RIGHT, buff=0.1)
        x2_bc = cn("×2", size=22, color=C_FACE_BC).next_to(rect_bc, RIGHT, buff=0.1)
        x2_ca = cn("×2", size=22, color=C_FACE_CA).next_to(rect_ca, RIGHT, buff=0.1)

        for obj in [rect_ab, lbl_ab, x2_ab, rect_bc, lbl_bc, x2_bc, rect_ca, lbl_ca, x2_ca]:
            self.add_fixed_in_frame_mobjects(obj)

        self.play(
            LaggedStart(
                FadeIn(VGroup(rect_ab, lbl_ab, x2_ab)),
                FadeIn(VGroup(rect_bc, lbl_bc, x2_bc)),
                FadeIn(VGroup(rect_ca, lbl_ca, x2_ca)),
                lag_ratio=0.3
            ),
            run_time=1.2
        )
        self.wait(0.4)

        # ── 公式推导 ──
        s_step1_cn   = cn("表面积", size=26, color=WHITE)
        s_step1_math = fml(r"= 2ab + 2bc + 2ca", size=28, color=WHITE)
        s_step1 = VGroup(s_step1_cn, s_step1_math).arrange(RIGHT, buff=0.2)
        s_step1.move_to([0, -4.5, 0])
        self.add_fixed_in_frame_mobjects(s_step1)
        self.play(Write(s_step1), run_time=0.7)

        s_step2_cn   = cn("即", size=24, color=GRAY_A)
        s_step2_math = fml(r"S = 2(ab + bc + ca)", size=32, color=C_FORMULA)
        s_step2 = VGroup(s_step2_cn, s_step2_math).arrange(RIGHT, buff=0.2)
        s_step2.move_to([0, -5.5, 0])
        self.add_fixed_in_frame_mobjects(s_step2)
        self.play(FadeIn(s_step2_cn), Write(s_step2_math), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(ab_label), FadeOut(bc_label), FadeOut(ca_label),
            FadeOut(rect_ab), FadeOut(lbl_ab), FadeOut(x2_ab),
            FadeOut(rect_bc), FadeOut(lbl_bc), FadeOut(x2_bc),
            FadeOut(rect_ca), FadeOut(lbl_ca), FadeOut(x2_ca),
            FadeOut(s_step1), FadeOut(s_step2),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 5: 体积 (~9s)
    # ─────────────────────────────────────────────
    def _scene_volume(self):
        self.move_camera(phi=65 * DEGREES, theta=-50 * DEGREES, run_time=0.4)

        title = cn("体积", size=38, color=C_HL, pos=[0, 6.8, 0])
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # ── 底面高亮 ──
        prism_hollow = make_prism(opacity=0.15)
        v = get_corners()
        base_face = Polygon(v[0], v[1], v[5], v[4],
                            fill_color=C_FACE_AB, fill_opacity=0.75,
                            stroke_color=C_FACE_AB, stroke_width=2)

        self.play(Create(prism_hollow), FadeIn(base_face), run_time=0.8)

        base_lbl_cn   = cn("底面积", size=24, color=C_FACE_AB)
        base_lbl_math = fml(r"= a \times b", size=28, color=C_FACE_AB)
        base_lbl = VGroup(base_lbl_cn, base_lbl_math).arrange(RIGHT, buff=0.15)
        base_lbl.move_to([3.0, -2.5, 0])
        self.add_fixed_in_frame_mobjects(base_lbl)
        self.play(FadeIn(base_lbl), run_time=0.5)
        self.wait(0.4)

        # ── 层叠动画: c层单位薄片向上堆叠 ──
        n_layers = 5
        layer_h  = DIM_C / n_layers
        layers   = VGroup()
        for i in range(n_layers):
            y0 = -DIM_C / 2 + i * layer_h
            y1 = y0 + layer_h
            hx, hz = DIM_A / 2, DIM_B / 2
            alpha = 0.3 + 0.1 * (i % 2)
            lyr = Prism(
                dimensions=[DIM_A, layer_h, DIM_B],
                fill_color=interpolate_color(BLUE_D, ManimColor(C_FORMULA), i / (n_layers - 1)),
                fill_opacity=alpha,
                stroke_color=WHITE,
                stroke_width=0.3,
            )
            lyr.shift(UP * (y0 + layer_h / 2))
            layers.add(lyr)

        layer_lbl_cn   = cn("×  c 层", size=24, color=C_FORMULA)
        layer_lbl = VGroup(layer_lbl_cn).arrange(RIGHT, buff=0.1)
        layer_lbl.move_to([3.0, 0.5, 0])
        self.add_fixed_in_frame_mobjects(layer_lbl)

        self.play(FadeOut(base_face), run_time=0.2)
        self.play(
            LaggedStart(*[FadeIn(l) for l in layers], lag_ratio=0.15),
            FadeIn(layer_lbl),
            run_time=1.2
        )
        self.wait(0.4)

        # ── 公式推导 ──
        v_step1_cn   = cn("体积", size=26, color=WHITE)
        v_step1_math = fml(r"= (a \times b) \times c = abc", size=28, color=WHITE)
        v_step1 = VGroup(v_step1_cn, v_step1_math).arrange(RIGHT, buff=0.2)
        v_step1.move_to([0, -4.5, 0])
        self.add_fixed_in_frame_mobjects(v_step1)
        self.play(Write(v_step1), run_time=0.7)

        v_step2_cn   = cn("即", size=24, color=GRAY_A)
        v_step2_math = fml(r"V = abc", size=40, color=C_FORMULA)
        v_step2 = VGroup(v_step2_cn, v_step2_math).arrange(RIGHT, buff=0.2)
        v_step2.move_to([0, -5.6, 0])
        self.add_fixed_in_frame_mobjects(v_step2)
        self.play(FadeIn(v_step2_cn), Write(v_step2_math), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(base_lbl), FadeOut(layer_lbl),
            FadeOut(v_step1), FadeOut(v_step2),
            FadeOut(prism_hollow), FadeOut(layers),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 6: 正方体 (~9s)
    # ─────────────────────────────────────────────
    def _scene_cube(self):
        self.move_camera(phi=70 * DEGREES, theta=-40 * DEGREES, run_time=0.4)

        title = cn("特殊情况: 正方体", size=32, color=C_CUBE, pos=[0, 6.8, 0])
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # 先显示长方体
        long_box = make_prism(opacity=0.5, color=C_BOX)
        self.play(Create(long_box), run_time=0.7)

        note = cn("当 a = b = c 时...", size=26, color=GRAY_A, pos=[0, 5.8, 0])
        self.add_fixed_in_frame_mobjects(note)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)

        # Transform 到正方体
        s = 1.5   # 正方体边长
        cube = Prism(
            dimensions=[s, s, s],
            fill_color=C_CUBE,
            fill_opacity=0.55,
            stroke_color=WHITE,
            stroke_width=0.6,
        )
        self.play(Transform(long_box, cube), run_time=1.0)
        self.wait(0.3)

        # 三条彩棱代表 a
        hf = s / 2
        cube_v = np.array([
            [-hf, -hf, -hf], [ hf, -hf, -hf], [ hf,  hf, -hf], [-hf,  hf, -hf],
            [-hf, -hf,  hf], [ hf, -hf,  hf], [ hf,  hf,  hf], [-hf,  hf,  hf],
        ])
        rep_edges = VGroup(
            Line3D(cube_v[0], cube_v[1], color=C_CUBE, stroke_width=6),
            Line3D(cube_v[0], cube_v[3], color=C_CUBE, stroke_width=6),
            Line3D(cube_v[0], cube_v[4], color=C_CUBE, stroke_width=6),
        )
        self.play(Create(rep_edges), run_time=0.5)

        a_lbl = fml(r"a", size=34, color=C_CUBE)
        a_lbl.move_to([3.5, 3.5, 0])
        self.add_fixed_in_frame_mobjects(a_lbl)
        self.play(FadeIn(a_lbl), run_time=0.3)

        # 公式逐条出现
        formulas = [
            (r"L = 12a",   "棱长和",  C_EDGE_A, 4.0),
            (r"S = 6a^2",  "表面积",  C_FACE_AB, 3.2),
            (r"V = a^3",   "体积",    C_FORMULA, 2.4),
        ]

        f_objs = []
        for latex, name, color, y in formulas:
            f_cn   = cn(name, size=22, color=color)
            f_math = fml(latex, size=30, color=color)
            row = VGroup(f_cn, fml(":", size=22, color=color), f_math).arrange(RIGHT, buff=0.1)
            row.move_to([0, y, 0])
            self.add_fixed_in_frame_mobjects(row)
            f_objs.append(row)
            self.play(FadeIn(row), run_time=0.5)
            self.wait(0.25)

        # 提示与长方体公式的关系
        hint = cn("令 a=b=c 代入通用公式即可推出", size=20, color=GRAY_B, pos=[0, -5.5, 0])
        self.add_fixed_in_frame_mobjects(hint)
        self.play(FadeIn(hint), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(note), FadeOut(a_lbl),
            FadeOut(hint),
            *[FadeOut(o) for o in f_objs],
            FadeOut(long_box), FadeOut(rep_edges),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 7: 公式汇总 + 片尾 (~6s)
    # ─────────────────────────────────────────────
    def _scene_outro(self):
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=0.4)

        # 旋转长方体背景
        prism = make_prism(opacity=0.40)
        ga, gb, gc = make_edges(sw=4)
        self.play(Create(prism), Create(ga), Create(gb), Create(gc), run_time=0.7)
        self.begin_ambient_camera_rotation(rate=0.18)

        # 公式汇总卡 (fixed-in-frame)
        summaries = [
            (r"L = 4(a+b+c)",        "棱长和",  C_EDGE_A),
            (r"S = 2(ab+bc+ca)",      "表面积",  C_FACE_CA),
            (r"V = abc",              "体积",    C_FORMULA),
            (r"L_{\rm cube} = 12a",   "正方体棱长和", C_CUBE),
            (r"S_{\rm cube} = 6a^2 \;,\; V_{\rm cube} = a^3", "正方体", C_CUBE),
        ]

        sum_objs = []
        y_pos = [5.2, 4.2, 3.2, 2.2, 1.2]
        for (latex, name, color), y in zip(summaries, y_pos):
            f_cn   = cn(name + ":", size=20, color=color)
            f_math = fml(latex, size=24, color=color)
            row = VGroup(f_cn, f_math).arrange(RIGHT, buff=0.15)
            row.move_to([0, y, 0])
            self.add_fixed_in_frame_mobjects(row)
            sum_objs.append(row)

        self.play(
            LaggedStart(*[FadeIn(o) for o in sum_objs], lag_ratio=0.15),
            run_time=1.2
        )
        self.wait(0.5)

        # 作者信息
        auth_name = cn(AUTHOR_NAME, size=30, color=WHITE, pos=[0, -4.5, 0])
        auth_id   = cn(AUTHOR_ID,   size=24, color=GRAY_B, pos=[0, -5.3, 0])
        follow    = cn("关注我，获得更多数学技巧!", size=26, color=C_HL, pos=[0, -6.2, 0])
        for o in [auth_name, auth_id, follow]:
            self.add_fixed_in_frame_mobjects(o)

        self.play(
            FadeIn(auth_name, shift=UP * 0.3),
            FadeIn(auth_id),
            FadeIn(follow, scale=1.05),
            run_time=0.8
        )

        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        all_fade = sum_objs + [auth_name, auth_id, follow, prism, ga, gb, gc]
        self.play(*[FadeOut(o) for o in all_fade], run_time=0.8)
"""
三角形的内角和 - Triangle Angle Sum Lesson
小学四年级 第二学期 第四章 几何小实践——三角形
知识点：三角形三内角之和等于180°

验证方法：
  1. 量角法（直接量三个角）
  2. 拼角法（把三个角撕下来拼成平角）
  3. 应用：已知两角求第三角

TikTok竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局视频配置 ──────────────────────────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ── 颜色常量 ──────────────────────────────────────────────────────────────────
BG_COLOR      = "#1a1a2e"
COLOR_A       = "#e74c3c"   # 角A  红
COLOR_B       = "#3498db"   # 角B  蓝
COLOR_C       = "#2ecc71"   # 角C  绿
COLOR_TRI     = "#f0e6d3"   # 三角形边线
COLOR_FORMULA = "#f39c12"   # 公式强调色
COLOR_GRAY    = "#aaaaaa"
FONT          = "Noto Sans CJK SC"


class TriangleAngleSumLesson(Scene):
    """
    三角形内角和教学动画

    场景顺序：
      scene_1_hook        — 开场提问，钩子
      scene_2_triangle    — 认识三角形三个内角
      scene_3_measure     — 量角法验证
      scene_4_tear        — 撕角拼合法（核心可视化）
      scene_5_formula     — 正式写出公式
      scene_6_apply       — 应用：已知两角求第三角
      scene_7_outro       — 结尾关注
    """

    # ── 初始化 ──────────────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_hook()
        self.scene_2_triangle()
        self.scene_3_measure()
        self.scene_4_tear()
        self.scene_5_formula()
        self.scene_6_apply()
        self.scene_7_outro()

    # ── 几何数据统一计算 ─────────────────────────────────────────────────────
    def setup_geometry(self):
        """所有顶点、边、角在此精确计算，后续直接引用。"""
        # 三角形顶点 — 不等边且各角明显不同，利于讲解
        # A=左下, B=右下, C=顶上偏左
        self.A = np.array([-2.2, -1.0, 0.0])
        self.B = np.array([ 2.0, -1.0, 0.0])
        self.C = np.array([-0.4,  1.8, 0.0])

        # 边长
        self.len_AB = np.linalg.norm(self.B - self.A)
        self.len_BC = np.linalg.norm(self.C - self.B)
        self.len_CA = np.linalg.norm(self.A - self.C)

        # 内角（弧度）
        self.ang_A = self._angle_at(self.B, self.A, self.C)   # ∠A 顶点A
        self.ang_B = self._angle_at(self.A, self.B, self.C)   # ∠B 顶点B
        self.ang_C = self._angle_at(self.A, self.C, self.B)   # ∠C 顶点C

        # 度数
        self.deg_A = round(np.degrees(self.ang_A))
        self.deg_B = round(np.degrees(self.ang_B))
        self.deg_C = round(np.degrees(self.ang_C))

        # 验证
        total = self.deg_A + self.deg_B + self.deg_C
        print(f"∠A={self.deg_A}°  ∠B={self.deg_B}°  ∠C={self.deg_C}°  合计={total}°")
        assert abs(total - 180) <= 1, f"内角和验证失败: {total}"

        # 质心（用于缩放基点）
        self.centroid = (self.A + self.B + self.C) / 3

    @staticmethod
    def _angle_at(P1, vertex, P2):
        """计算∠P1-vertex-P2 的弧度（vertex 为顶点）。"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        cos_val = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(np.clip(cos_val, -1.0, 1.0))

    # ── 工具方法 ─────────────────────────────────────────────────────────────
    def make_triangle(self, A=None, B=None, C=None, color=COLOR_TRI, stroke=2.5):
        A = A if A is not None else self.A
        B = B if B is not None else self.B
        C = C if C is not None else self.C
        return Polygon(A, B, C, color=color, stroke_width=stroke, fill_opacity=0)

    def make_angle_arc(self, vertex, P1, P2, radius=0.38, color=WHITE):
        """在顶点 vertex 处绘制从 P1 到 P2 方向的角弧。
        自动判断 other_angle 保证弧在三角形内侧。"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        cross_z = float(v1[0] * v2[1] - v1[1] * v2[0])
        line1 = Line(vertex, P1)
        line2 = Line(vertex, P2)
        # Manim Angle 默认从 line1 到 line2 逆时针
        # cross_z > 0 => v1到v2逆时针 => 默认即在内侧
        other = cross_z < 0
        return Angle(line1, line2, radius=radius, color=color, other_angle=other)

    def make_vertex_label(self, text, point, direction, color=WHITE, font_size=30):
        return Text(text, font=FONT, font_size=font_size, color=color).next_to(
            point, direction, buff=0.22
        )

    def make_degree_label(self, deg_text, arc, color=WHITE, font_size=24, offset=None):
        """把度数标签放在弧的旁边。"""
        lbl = Text(deg_text, font=FONT, font_size=font_size, color=color)
        center = arc.get_center()
        if offset is not None:
            lbl.move_to(center + offset)
        else:
            lbl.next_to(arc, buff=0.05)
        return lbl

    # ── Scene 1: 开场钩子 ──────────────────────────────────────────────────
    def scene_1_hook(self):
        # 作者水印
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(author)

        # 问题钩子
        q1 = Text("三角形三个角加起来", font=FONT, font_size=38, color=WHITE)
        q2 = Text("等于多少度？", font=FONT, font_size=38, color=COLOR_FORMULA)
        hook = VGroup(q1, q2).arrange(DOWN, buff=0.25).move_to(UP * 5.2)

        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.8)

        # 小三角形动画示意
        tri_demo = self.make_triangle(
            A=np.array([-1.4, 2.2, 0]),
            B=np.array([ 1.4, 2.2, 0]),
            C=np.array([ 0.0, 4.0, 0]),
            color=COLOR_FORMULA, stroke=3
        )
        self.play(Create(tri_demo), run_time=0.7)

        # 三个角亮一亮
        corners = [
            (np.array([-1.4, 2.2, 0]), np.array([ 1.4, 2.2, 0]), np.array([ 0.0, 4.0, 0]), COLOR_A),
            (np.array([ 1.4, 2.2, 0]), np.array([-1.4, 2.2, 0]), np.array([ 0.0, 4.0, 0]), COLOR_B),
            (np.array([ 0.0, 4.0, 0]), np.array([-1.4, 2.2, 0]), np.array([ 1.4, 2.2, 0]), COLOR_C),
        ]
        for vtx, p1, p2, col in corners:
            arc = self.make_angle_arc(vtx, p1, p2, radius=0.3, color=col)
            self.play(Create(arc), run_time=0.3)

        self.wait(0.6)
        self.play(FadeOut(hook), FadeOut(tri_demo), run_time=0.5)
        # 清除弧（通过 FadeOut 全场景非保留元素）
        self.clear()
        self.add(author)
        self.author = author

    # ── Scene 2: 认识三角形三个内角 ───────────────────────────────────────
    def scene_2_triangle(self):
        title = Text("认识三角形的内角", font=FONT, font_size=34, color=GOLD)\
            .move_to(UP * 6.0)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # 主三角形，居中偏上
        tri_offset = UP * 1.5
        A = self.A + tri_offset
        B = self.B + tri_offset
        C = self.C + tri_offset

        tri = Polygon(A, B, C, color=COLOR_TRI, stroke_width=3)
        self.play(Create(tri), run_time=1.0)

        # 顶点标签
        lbl_A = self.make_vertex_label("A", A, DL, color=COLOR_A)
        lbl_B = self.make_vertex_label("B", B, DR, color=COLOR_B)
        lbl_C = self.make_vertex_label("C", C, UP, color=COLOR_C)
        self.play(FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C), run_time=0.5)

        # 逐一高亮三个角
        def show_angle(vtx, p1, p2, color, name_str, desc_str, pos):
            arc = self.make_angle_arc(vtx, p1, p2, radius=0.35, color=color)
            name_lbl = Text(name_str, font=FONT, font_size=26, color=color)\
                .move_to(pos)
            self.play(Create(arc), FadeIn(name_lbl), run_time=0.6)
            desc = Text(desc_str, font=FONT, font_size=22, color=COLOR_GRAY)\
                .next_to(name_lbl, DOWN, buff=0.15)
            self.play(FadeIn(desc), run_time=0.4)
            self.wait(0.4)
            self.play(FadeOut(desc), run_time=0.3)
            return arc, name_lbl

        arc_A, lbl_ang_A = show_angle(
            A, B, C, COLOR_A, "∠A（内角A）",
            "顶点A处的角",
            DOWN * 2.0
        )
        arc_B, lbl_ang_B = show_angle(
            B, A, C, COLOR_B, "∠B（内角B）",
            "顶点B处的角",
            DOWN * 2.0
        )
        arc_C, lbl_ang_C = show_angle(
            C, A, B, COLOR_C, "∠C（内角C）",
            "顶点C处的角",
            DOWN * 2.0
        )

        explain = Text(
            "这三个角合称三角形的内角",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)

        # 保存到 self 以便后续复用
        self._tri_shifted_A = A
        self._tri_shifted_B = B
        self._tri_shifted_C = C

        # 清场
        self.play(
            FadeOut(title), FadeOut(tri),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(lbl_ang_A), FadeOut(lbl_ang_B), FadeOut(lbl_ang_C),
            FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(explain),
            run_time=0.5
        )

    # ── Scene 3: 量角法验证 ───────────────────────────────────────────────
    def scene_3_measure(self):
        title = Text("方法一：量角法", font=FONT, font_size=32, color=GOLD)\
            .move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.5)

        sub = Text("用量角器分别量出三个角的度数",
                   font=FONT, font_size=22, color=COLOR_GRAY).move_to(UP * 5.4)
        self.play(FadeIn(sub), run_time=0.4)

        # 三角形
        offset = UP * 1.0
        A, B, C = self.A + offset, self.B + offset, self.C + offset
        tri = Polygon(A, B, C, color=COLOR_TRI, stroke_width=3)
        self.play(Create(tri), run_time=0.8)

        lbl_A = self.make_vertex_label("A", A, DL, color=COLOR_A, font_size=26)
        lbl_B = self.make_vertex_label("B", B, DR, color=COLOR_B, font_size=26)
        lbl_C = self.make_vertex_label("C", C, UP,  color=COLOR_C, font_size=26)
        self.play(FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C), run_time=0.4)

        # 逐个角显示度数
        data = [
            (A, B, C, COLOR_A, f"{self.deg_A}°", DL * 0.3 + UP * 0.15),
            (B, A, C, COLOR_B, f"{self.deg_B}°", DR * 0.3 + UP * 0.15),
            (C, A, B, COLOR_C, f"{self.deg_C}°", UP * 0.6),
        ]
        arcs = []
        deg_labels = []
        for vtx, p1, p2, col, deg_str, off in data:
            arc = self.make_angle_arc(vtx, p1, p2, radius=0.38, color=col)
            deg_lbl = Text(deg_str, font=FONT, font_size=22, color=col)\
                .next_to(vtx, direction=normalize(off), buff=0.55)
            self.play(Create(arc), FadeIn(deg_lbl), run_time=0.6)
            self.wait(0.3)
            arcs.append(arc)
            deg_labels.append(deg_lbl)

        # 加法过程
        add_line = VGroup(
            Text(f"∠A + ∠B + ∠C", font=FONT, font_size=26, color=WHITE),
            Text("=", font=FONT, font_size=26, color=WHITE),
            Text(f"{self.deg_A}° + {self.deg_B}° + {self.deg_C}°",
                 font=FONT, font_size=26, color=COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.8)

        result_line = VGroup(
            Text("=", font=FONT, font_size=28, color=WHITE),
            Text("180°", font=FONT, font_size=32, color=COLOR_FORMULA, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).next_to(add_line, DOWN, buff=0.3)

        self.play(FadeIn(add_line), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(result_line), run_time=0.5)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(tri),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            *[FadeOut(a) for a in arcs],
            *[FadeOut(d) for d in deg_labels],
            FadeOut(add_line), FadeOut(result_line),
            run_time=0.5
        )

    # ── Scene 4: 撕角拼合法（核心动画） ──────────────────────────────────
    def scene_4_tear(self):
        title = Text("方法二：拼角法（撕纸验证）",
                     font=FONT, font_size=30, color=GOLD).move_to(UP * 6.2)
        sub = Text("把三个角撕下来，拼在一起，看看组成什么角？",
                   font=FONT, font_size=20, color=COLOR_GRAY).move_to(UP * 5.5)
        self.play(FadeIn(title), FadeIn(sub), run_time=0.5)

        # ── 步骤1：画出三角形 ──────────────────────────────────────
        scale = 0.85
        offset = UP * 1.8
        A = self.A * scale + offset
        B = self.B * scale + offset
        C = self.C * scale + offset

        tri = Polygon(A, B, C, color=COLOR_TRI, stroke_width=3,
                      fill_color="#16213e", fill_opacity=0.6)
        self.play(Create(tri), run_time=0.8)

        # 三个角弧 + 填色
        arc_A = self.make_angle_arc(A, B, C, radius=0.32, color=COLOR_A)
        arc_B = self.make_angle_arc(B, A, C, radius=0.32, color=COLOR_B)
        arc_C = self.make_angle_arc(C, A, B, radius=0.32, color=COLOR_C)

        # 填色扇形（近似用小三角替代）
        def filled_wedge(vtx, p1, p2, col):
            """用极小多边形近似填充角区域，可见即可。"""
            v1 = (p1 - vtx) / np.linalg.norm(p1 - vtx) * 0.32
            v2 = (p2 - vtx) / np.linalg.norm(p2 - vtx) * 0.32
            mid_dir = v1 + v2
            if np.linalg.norm(mid_dir) < 1e-9:
                mid_dir = np.array([0, 0.01, 0])
            mid_dir = mid_dir / np.linalg.norm(mid_dir) * 0.32
            pts = [vtx, vtx + v1, vtx + mid_dir, vtx + v2]
            return Polygon(*pts, fill_color=col, fill_opacity=0.5,
                           stroke_width=0)

        wedge_A = filled_wedge(A, B, C, COLOR_A)
        wedge_B = filled_wedge(B, A, C, COLOR_B)
        wedge_C = filled_wedge(C, A, B, COLOR_C)

        self.play(
            Create(arc_A), FadeIn(wedge_A),
            Create(arc_B), FadeIn(wedge_B),
            Create(arc_C), FadeIn(wedge_C),
            run_time=0.8
        )

        step1 = Text("三个彩色角，准备拼在一起！",
                     font=FONT, font_size=22, color=WHITE).move_to(DOWN * 1.0)
        self.play(FadeIn(step1), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(step1), run_time=0.3)

        # ── 步骤2：角A、B、C 飞向底部拼成平角 ──────────────────────
        # 目标：在屏幕中央偏下画一条基准水平线，将三个角顺序拼上去
        base_y = -2.5
        base_x = -2.0          # 拼接起点（左端）
        base_left  = np.array([base_x - 0.5, base_y, 0])
        base_right = np.array([base_x + 4.5, base_y, 0])

        baseline = Line(base_left, base_right, color=COLOR_GRAY, stroke_width=2.5)
        self.play(Create(baseline), run_time=0.4)

        base_tip = Text("拼起来！", font=FONT, font_size=22, color=GOLD)\
            .move_to(baseline.get_center() + UP * 0.4)
        self.play(FadeIn(base_tip), run_time=0.3)
        self.wait(0.2)
        self.play(FadeOut(base_tip), run_time=0.2)

        # 复制三个填色扇形，移动到基准线上逐一拼合
        # 角A → 最左，从base_x开始，角度=self.ang_A，往右铺
        # 使用简化的三角形扇形表示

        def make_fan(angle_rad, fill_color, stroke_color):
            """以 ORIGIN 为顶点，水平右方为起始边，逆时针扫 angle_rad 的扇形。"""
            n = 20
            pts = [ORIGIN]
            r = 0.70
            for i in range(n + 1):
                theta = i * angle_rad / n
                pts.append(np.array([r * np.cos(theta), r * np.sin(theta), 0]))
            return Polygon(*pts, fill_color=fill_color, fill_opacity=0.75,
                           stroke_color=stroke_color, stroke_width=1.5)

        # 计算各角弧度（用精确值）
        ang_A_rad = self.ang_A
        ang_B_rad = self.ang_B
        ang_C_rad = self.ang_C

        # 拼合起点 & 累积角度（从水平线左端，逆时针）
        pivot = np.array([base_x, base_y, 0])

        # 扇形A：起始角0，扫ang_A
        fan_A = make_fan(ang_A_rad, COLOR_A, COLOR_A)
        fan_A.move_to(pivot, aligned_edge=ORIGIN)
        # 旋转使得起始边沿水平（默认已是水平）
        fan_A.shift(pivot - fan_A.get_vertices()[0])

        # 扇形B：起始角=ang_A，扫ang_B
        fan_B = make_fan(ang_B_rad, COLOR_B, COLOR_B)
        fan_B.rotate(ang_A_rad, about_point=ORIGIN)
        fan_B.shift(pivot)

        # 扇形C：起始角=ang_A+ang_B，扫ang_C
        fan_C = make_fan(ang_C_rad, COLOR_C, COLOR_C)
        fan_C.rotate(ang_A_rad + ang_B_rad, about_point=ORIGIN)
        fan_C.shift(pivot)

        # 扇形从三角形各顶点飞入
        fan_A_start = wedge_A.copy().set_fill(COLOR_A, 0.9).set_stroke(COLOR_A, 1)
        fan_B_start = wedge_B.copy().set_fill(COLOR_B, 0.9).set_stroke(COLOR_B, 1)
        fan_C_start = wedge_C.copy().set_fill(COLOR_C, 0.9).set_stroke(COLOR_C, 1)

        self.play(
            ReplacementTransform(fan_A_start, fan_A),
            run_time=0.8
        )
        self.play(
            ReplacementTransform(fan_B_start, fan_B),
            run_time=0.8
        )
        self.play(
            ReplacementTransform(fan_C_start, fan_C),
            run_time=0.8
        )

        # 等待观察
        self.wait(0.5)

        # 强调：三角拼成平角（180°直线）
        flat_line = Line(
            pivot + LEFT * 0.1,
            pivot + RIGHT * 0.72 * (1 + 0) + RIGHT * 0.1,
            color=COLOR_FORMULA, stroke_width=4
        )
        # 实际上拼完后最右端射线方向为 angle = ang_A+ang_B+ang_C ≈ π
        end_dir = np.array([np.cos(ang_A_rad + ang_B_rad + ang_C_rad),
                            np.sin(ang_A_rad + ang_B_rad + ang_C_rad), 0])
        flat_end = pivot + end_dir * 0.72
        flat_line2 = Line(pivot, flat_end, color=COLOR_FORMULA, stroke_width=4)

        wow = Text("恰好拼成一条直线！", font=FONT, font_size=26, color=COLOR_FORMULA)\
            .move_to(DOWN * 3.5)
        sub2 = Text("一条直线 = 平角 = 180°",
                    font=FONT, font_size=22, color=WHITE).move_to(DOWN * 4.2)

        self.play(
            Create(flat_line2),
            FadeIn(wow),
            run_time=0.8
        )
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(tri), FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(wedge_A), FadeOut(wedge_B), FadeOut(wedge_C),
            FadeOut(fan_A), FadeOut(fan_B), FadeOut(fan_C),
            FadeOut(baseline), FadeOut(flat_line2),
            FadeOut(wow), FadeOut(sub2),
            run_time=0.6
        )

    # ── Scene 5: 正式公式 ─────────────────────────────────────────────────
    def scene_5_formula(self):
        title = Text("三角形内角和定理", font=FONT, font_size=34, color=GOLD)\
            .move_to(UP * 6.0)
        self.play(FadeIn(title), run_time=0.5)

        # 三角形
        offset = UP * 2.2
        scale = 0.9
        A = self.A * scale + offset
        B = self.B * scale + offset
        C = self.C * scale + offset

        tri = Polygon(A, B, C, color=COLOR_TRI, stroke_width=3,
                      fill_color="#16213e", fill_opacity=0.5)
        self.play(Create(tri), run_time=0.7)

        # 顶点标签
        lbl_A = self.make_vertex_label("A", A, DL, COLOR_A, 28)
        lbl_B = self.make_vertex_label("B", B, DR, COLOR_B, 28)
        lbl_C = self.make_vertex_label("C", C, UP,  COLOR_C, 28)
        self.play(FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C), run_time=0.4)

        arc_A = self.make_angle_arc(A, B, C, radius=0.36, color=COLOR_A)
        arc_B = self.make_angle_arc(B, A, C, radius=0.36, color=COLOR_B)
        arc_C = self.make_angle_arc(C, A, B, radius=0.36, color=COLOR_C)
        self.play(Create(arc_A), Create(arc_B), Create(arc_C), run_time=0.6)

        # 公式框
        # 用 VGroup 拼中文+MathTex，避免 MathTex 中文报错
        formula_parts = VGroup(
            Text("∠A", font=FONT, font_size=36, color=COLOR_A),
            Text("+", font=FONT, font_size=36, color=WHITE),
            Text("∠B", font=FONT, font_size=36, color=COLOR_B),
            Text("+", font=FONT, font_size=36, color=WHITE),
            Text("∠C", font=FONT, font_size=36, color=COLOR_C),
            Text("=", font=FONT, font_size=36, color=WHITE),
            Text("180°", font=FONT, font_size=40, color=COLOR_FORMULA, weight=BOLD),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 1.2)

        # 方框
        box = SurroundingRectangle(formula_parts,
                                   color=COLOR_FORMULA, corner_radius=0.0,
                                   buff=0.25, stroke_width=2.5)

        self.play(
            LaggedStart(
                *[FadeIn(p, shift=UP * 0.2) for p in formula_parts],
                lag_ratio=0.15
            ),
            run_time=1.2
        )
        self.play(Create(box), run_time=0.5)

        # 强调
        emphasis = Text("任意三角形的内角和都等于180°！",
                        font=FONT, font_size=22, color=WHITE).move_to(DOWN * 2.4)
        self.play(FadeIn(emphasis), run_time=0.5)
        self.wait(2.0)

        # 清场
        self.play(
            FadeOut(title), FadeOut(tri),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(formula_parts), FadeOut(box), FadeOut(emphasis),
            run_time=0.5
        )

    # ── Scene 6: 应用——已知两角求第三角 ──────────────────────────────────
    def scene_6_apply(self):
        title = Text("学以致用", font=FONT, font_size=34, color=GOLD)\
            .move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.5)

        # 题目
        q_line1 = Text("已知三角形中：", font=FONT, font_size=26, color=WHITE)
        q_line2 = VGroup(
            Text("∠A = 50°", font=FONT, font_size=28, color=COLOR_A),
            Text("，", font=FONT, font_size=28, color=WHITE),
            Text("∠B = 70°", font=FONT, font_size=28, color=COLOR_B),
        ).arrange(RIGHT, buff=0.1)
        q_line3 = Text("求 ∠C = ?", font=FONT, font_size=28, color=COLOR_C)
        question = VGroup(q_line1, q_line2, q_line3).arrange(DOWN, buff=0.3)\
            .move_to(UP * 4.2)

        self.play(FadeIn(question), run_time=0.7)

        # 三角形图示（具体角度50°、70°、60°）
        ang_a_deg = 50
        ang_b_deg = 70
        ang_c_deg = 60

        ang_a = np.radians(ang_a_deg)
        ang_b = np.radians(ang_b_deg)

        # 构造顶点
        base = 3.0
        A6 = np.array([-base / 2, -0.5, 0])
        B6 = np.array([ base / 2, -0.5, 0])
        # C6 由 ang_a, ang_b 确定
        # 从A出发方向 ang_a（逆时针），从B出发方向 π - ang_b（因B的角从右边算）
        tan_a = np.tan(ang_a)
        tan_b = np.tan(ang_b)
        cx = (base / 2 + base / 2 * tan_b / (tan_a + tan_b) * 2 - base / 2)
        # 更简洁的做法
        cx = A6[0] + (B6[0] - A6[0]) * tan_b / (tan_a + tan_b)
        cy = A6[1] + (B6[0] - A6[0]) * tan_a * tan_b / (tan_a + tan_b)
        C6 = np.array([cx, cy, 0])

        tri6_offset = DOWN * 0.5
        A6 += tri6_offset; B6 += tri6_offset; C6 += tri6_offset

        tri6 = Polygon(A6, B6, C6, color=COLOR_TRI, stroke_width=3,
                       fill_color="#16213e", fill_opacity=0.5)
        self.play(Create(tri6), run_time=0.7)

        l6_A = self.make_vertex_label("A", A6, DL, COLOR_A, 24)
        l6_B = self.make_vertex_label("B", B6, DR, COLOR_B, 24)
        l6_C = self.make_vertex_label("C", C6, UP,  COLOR_C, 24)
        self.play(FadeIn(l6_A), FadeIn(l6_B), FadeIn(l6_C), run_time=0.4)

        arc6_A = self.make_angle_arc(A6, B6, C6, radius=0.35, color=COLOR_A)
        arc6_B = self.make_angle_arc(B6, A6, C6, radius=0.35, color=COLOR_B)
        self.play(Create(arc6_A), Create(arc6_B), run_time=0.5)

        d6_A = Text("50°", font=FONT, font_size=22, color=COLOR_A)\
            .next_to(arc6_A, UR, buff=0.08)
        d6_B = Text("70°", font=FONT, font_size=22, color=COLOR_B)\
            .next_to(arc6_B, UL, buff=0.08)
        self.play(FadeIn(d6_A), FadeIn(d6_B), run_time=0.4)

        # 解题步骤
        step_title = Text("解题过程：", font=FONT, font_size=24, color=COLOR_FORMULA)\
            .move_to(DOWN * 2.3)
        self.play(FadeIn(step_title), run_time=0.4)

        step1 = VGroup(
            Text("∠A + ∠B + ∠C = 180°", font=FONT, font_size=24, color=WHITE)
        ).move_to(DOWN * 2.9)
        self.play(FadeIn(step1), run_time=0.5)

        step2 = VGroup(
            Text("50° + 70° + ∠C = 180°",
                 font=FONT, font_size=24, color=WHITE)
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(step2), run_time=0.5)

        step3 = VGroup(
            Text("∠C = 180° − 50° − 70°",
                 font=FONT, font_size=24, color=WHITE)
        ).move_to(DOWN * 4.1)
        self.play(FadeIn(step3), run_time=0.5)

        answer = VGroup(
            Text("∠C = ", font=FONT, font_size=30, color=WHITE),
            Text("60°", font=FONT, font_size=34, color=COLOR_C, weight=BOLD),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.85)
        ans_box = SurroundingRectangle(answer, color=COLOR_C, buff=0.2, stroke_width=2)

        self.play(FadeIn(answer), Create(ans_box), run_time=0.7)

        # 在三角形上补出角C
        arc6_C = self.make_angle_arc(C6, A6, B6, radius=0.35, color=COLOR_C)
        d6_C = Text("60°", font=FONT, font_size=22, color=COLOR_C)\
            .next_to(arc6_C, DOWN, buff=0.1)
        self.play(Create(arc6_C), FadeIn(d6_C), run_time=0.6)

        self.wait(2.0)

        # 清场
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(tri6), FadeOut(l6_A), FadeOut(l6_B), FadeOut(l6_C),
            FadeOut(arc6_A), FadeOut(arc6_B), FadeOut(arc6_C),
            FadeOut(d6_A), FadeOut(d6_B), FadeOut(d6_C),
            FadeOut(step_title), FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeOut(answer), FadeOut(ans_box),
            run_time=0.6
        )

    # ── Scene 7: 结尾 ──────────────────────────────────────────────────────
    def scene_7_outro(self):
        # 总结公式再强调一次
        summary_title = Text("记住这个重要定理！",
                             font=FONT, font_size=34, color=GOLD).move_to(UP * 5.5)
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)

        formula_big = VGroup(
            Text("∠A", font=FONT, font_size=44, color=COLOR_A),
            Text("+", font=FONT, font_size=44, color=WHITE),
            Text("∠B", font=FONT, font_size=44, color=COLOR_B),
            Text("+", font=FONT, font_size=44, color=WHITE),
            Text("∠C", font=FONT, font_size=44, color=COLOR_C),
            Text("=", font=FONT, font_size=44, color=WHITE),
            Text("180°", font=FONT, font_size=52, color=COLOR_FORMULA, weight=BOLD),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.0)

        box_big = SurroundingRectangle(formula_big, color=COLOR_FORMULA,
                                       buff=0.3, stroke_width=3)
        self.play(FadeIn(formula_big), Create(box_big), run_time=0.8)

        # 三种方法回顾
        methods = VGroup(
            Text("验证方法：", font=FONT, font_size=24, color=COLOR_GRAY),
            Text("① 量角法 — 用量角器分别测量三个角",
                 font=FONT, font_size=20, color=WHITE),
            Text("② 拼角法 — 撕下三角拼成180°平角",
                 font=FONT, font_size=20, color=WHITE),
            Text("③ 折叠法 — 折纸使三个角重合成直线",
                 font=FONT, font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(UP * 2.2)

        self.play(FadeIn(methods, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)

        # 三个装饰三角形旋转出现
        tri_deco = VGroup(
            Polygon(
                np.array([-0.5, 0, 0]),
                np.array([ 0.5, 0, 0]),
                np.array([ 0.0, 0.85, 0]),
                color=c, fill_color=c, fill_opacity=0.7, stroke_width=2
            ).scale(0.7).move_to(DOWN * 0.8 + LEFT * (1.5 - i * 1.5))
            for i, c in enumerate([COLOR_A, COLOR_B, COLOR_C])
        )
        self.play(
            LaggedStart(*[GrowFromCenter(t) for t in tri_deco], lag_ratio=0.3),
            run_time=0.8
        )
        self.play(Rotate(tri_deco, angle=TAU, about_point=tri_deco.get_center(),
                         run_time=1.5))

        # 关注提示
        follow = Text("关注我，获得更多数学技巧！",
                      font=FONT, font_size=28, color=GOLD).move_to(DOWN * 2.2)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 作者大字
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=32, color=WHITE)\
            .move_to(DOWN * 3.2)
        author_id = Text("@emptyandcalm", font=FONT, font_size=24, color=COLOR_GRAY)\
            .move_to(DOWN * 3.85)
        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.5)

        self.wait(2.5)

        self.play(
            FadeOut(summary_title), FadeOut(formula_big), FadeOut(box_big),
            FadeOut(methods), FadeOut(tri_deco),
            FadeOut(follow), FadeOut(author_big), FadeOut(author_id),
            FadeOut(self.author),
            run_time=1.0
        )

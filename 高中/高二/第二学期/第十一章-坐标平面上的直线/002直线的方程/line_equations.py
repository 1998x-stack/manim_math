"""
直线的方程 - 五种形式教学动画
年级: 高二第二学期  章节: 坐标平面上的直线

五种形式：点斜式 / 斜截式 / 两点式 / 截距式 / 一般式

输出格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车  @emptyandcalm

运行:
    manim -pql line_equations.py LineEquations   # 快速预览
    manim -qh  line_equations.py LineEquations   # 高质量
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────
# 全局配置  TikTok 竖屏
# ──────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ──────────────────────────────────────────────
# 颜色
# ──────────────────────────────────────────────
BG_COLOR   = "#1a1a2e"
C_PS       = "#e74c3c"   # 点斜式  红
C_SI       = "#3498db"   # 斜截式  蓝
C_TP       = "#2ecc71"   # 两点式  绿
C_IC       = "#f39c12"   # 截距式  橙
C_GN       = "#9b59b6"   # 一般式  紫
C_AX       = "#7f8c8d"   # 轴色
C_HL       = YELLOW      # 高亮
C_BG_CARD  = "#16213e"   # 卡片背景
FONT       = "PingFang SC"


# ══════════════════════════════════════════════
class LineEquations(Scene):
    """直线方程五种形式教学动画"""

    # ──────────────────────────────────────────
    # construct
    # ──────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_opening()
        self.scene_point_slope()
        self.scene_slope_intercept()
        self.scene_two_point()
        self.scene_intercept()
        self.scene_general()
        self.scene_summary()
        self.scene_outro()

    # ──────────────────────────────────────────
    # 几何数据统一初始化
    # ──────────────────────────────────────────
    def setup_geometry(self):
        # 坐标轴参数
        self.AX_CTR    = np.array([0.0, 2.0, 0.0])
        self.AX_XR     = [-4, 4, 1]
        self.AX_YR     = [-2, 5, 1]
        self.AX_XLEN   = 6.5
        self.AX_YLEN   = 5.2

        # ① 点斜式: 过 P(1, 2)，k = 2  →  y = 2x
        self.ps_P  = np.array([1.0, 2.0])
        self.ps_k  = 2.0
        self.ps_b  = self.ps_P[1] - self.ps_k * self.ps_P[0]   # = 0

        # ② 斜截式: k = 1, b = 3  →  y = x + 3
        self.si_k  = 1.0
        self.si_b  = 3.0

        # ③ 两点式: P1(-1, 1), P2(2, 4)  →  y = x + 2
        self.tp_P1 = np.array([-1.0, 1.0])
        self.tp_P2 = np.array([ 2.0, 4.0])
        self.tp_k  = (self.tp_P2[1]-self.tp_P1[1]) / (self.tp_P2[0]-self.tp_P1[0])  # 1
        self.tp_b  = self.tp_P1[1] - self.tp_k * self.tp_P1[0]                       # 2
        # 辅助直角顶点（与P1同y，与P2同x）
        self.tp_Px = np.array([self.tp_P2[0], self.tp_P1[1]])  # (2, 1)

        # ④ 截距式: a = 3, b = 2  →  y = -2x/3 + 2
        self.ic_a  = 3.0
        self.ic_b  = 2.0
        self.ic_k  = -self.ic_b / self.ic_a   # -2/3
        self.ic_bi = self.ic_b                 # y截距 = 2

        # ⑤ 一般式: 2x + 3y - 6 = 0  (同④同一直线)
        self.gn_A, self.gn_B, self.gn_C = 2.0, 3.0, -6.0
        self.gn_k  = -self.gn_A / self.gn_B   # -2/3
        self.gn_bi = -self.gn_C / self.gn_B   # 2

        # ---- 验证 ----
        assert abs(self.ps_b) < 1e-10,          "点斜式 b 应=0"
        assert abs(self.tp_k - 1.0) < 1e-10,    "两点式 k 应=1"
        assert abs(self.tp_b - 2.0) < 1e-10,    "两点式 b 应=2"
        assert abs(self.gn_k - self.ic_k) < 1e-10, "一般式=截距式同线"
        print("✓ 几何数据验证通过")

    # ──────────────────────────────────────────
    # 工具: 创建坐标系
    # ──────────────────────────────────────────
    def make_axes(self):
        ax = Axes(
            x_range=self.AX_XR,
            y_range=self.AX_YR,
            x_length=self.AX_XLEN,
            y_length=self.AX_YLEN,
            axis_config=dict(
                color=C_AX,
                include_numbers=True,
                font_size=18,
                numbers_to_include=[-3,-2,-1,1,2,3,4],
                include_ticks=True,
                tick_size=0.07,
            ),
        ).move_to(self.AX_CTR)
        lx = Text("x", font=FONT, font_size=20, color=C_AX).next_to(ax.x_axis.get_right(), RIGHT, buff=0.12)
        ly = Text("y", font=FONT, font_size=20, color=C_AX).next_to(ax.y_axis.get_top(),   UP,    buff=0.12)
        return ax, lx, ly

    # ──────────────────────────────────────────
    # 工具: 在坐标系内画直线 y=kx+b
    # ──────────────────────────────────────────
    def line_on_axes(self, ax, k, b, color, sw=3):
        xmin, xmax = self.AX_XR[0], self.AX_XR[1]
        ymin, ymax = self.AX_YR[0], self.AX_YR[1]
        pts = []
        for xv in [xmin, xmax]:
            yv = k*xv + b
            if ymin <= yv <= ymax:
                pts.append((xv, yv))
        if abs(k) > 1e-10:
            for yv in [ymin, ymax]:
                xv = (yv - b) / k
                if xmin <= xv <= xmax:
                    pts.append((xv, yv))
        u = []
        for p in pts:
            if not any(abs(p[0]-q[0])<1e-8 and abs(p[1]-q[1])<1e-8 for q in u):
                u.append(p)
        if len(u) < 2:
            u = [(xmin, k*xmin+b), (xmax, k*xmax+b)]
        return Line(ax.c2p(*u[0]), ax.c2p(*u[1]), color=color, stroke_width=sw)

    # ──────────────────────────────────────────
    # 工具: 创建公式卡片
    # ──────────────────────────────────────────
    def formula_card(self, title_cn, tex_str, color, width=7.6, height=1.6, pos=DOWN*4.3):
        bg  = RoundedRectangle(
            width=width, height=height, corner_radius=0.18,
            fill_color=C_BG_CARD, fill_opacity=1,
            stroke_color=color, stroke_width=2.5
        ).move_to(pos)
        title = Text(title_cn, font=FONT, font_size=26, color=color).move_to(
            bg.get_center() + LEFT * (width/2 - 0.9)
        )
        formula = MathTex(tex_str, font_size=30, color=WHITE).move_to(
            bg.get_center() + RIGHT * 0.6
        )
        return VGroup(bg, title, formula)

    # ══════════════════════════════════════════
    # Scene 1  开场
    # ══════════════════════════════════════════
    def scene_opening(self):
        # 作者条
        self.author_banner = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_banner, shift=DOWN*0.2), run_time=0.4)

        # 大标题
        title = Text("直线的方程", font=FONT, font_size=52, color=GOLD).move_to(UP * 5.8)
        subtitle = Text("五种形式，一条直线的五张面孔", font=FONT, font_size=26, color=GRAY_A
                        ).move_to(UP * 4.9)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP*0.2), run_time=0.5)

        # 五种形式名称依次飞入
        names_data = [
            ("① 点斜式", C_PS, UP*3.5),
            ("② 斜截式", C_SI, UP*2.6),
            ("③ 两点式", C_TP, UP*1.7),
            ("④ 截距式", C_IC, UP*0.8),
            ("⑤ 一般式", C_GN, DOWN*0.1),
        ]
        name_objs = []
        for txt, col, pos in names_data:
            obj = Text(txt, font=FONT, font_size=30, color=col).move_to(pos)
            obj.shift(RIGHT * 9)   # 屏幕右侧外
            self.add(obj)
            self.play(obj.animate.shift(LEFT * 9), run_time=0.35)
            name_objs.append(obj)

        self.wait(0.6)

        # 全部淡出，标题缩小
        title_small = Text("直线的方程", font=FONT, font_size=34, color=GOLD).move_to(UP * 6.3)
        self.play(
            *[FadeOut(o) for o in name_objs],
            FadeOut(subtitle),
            Transform(title, title_small),
            run_time=0.6,
        )
        self.title_obj = title

    # ══════════════════════════════════════════
    # Scene 2  点斜式
    # ══════════════════════════════════════════
    def scene_point_slope(self):
        scene_label = Text("① 点斜式", font=FONT, font_size=38, color=C_PS).move_to(UP*5.5)
        self.play(Write(scene_label), run_time=0.5)

        ax, lx, ly = self.make_axes()
        self.play(Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.9)

        # 画直线 y = 2x
        line = self.line_on_axes(ax, self.ps_k, self.ps_b, C_PS)
        self.play(Create(line), run_time=0.8)

        # 标记点 P(1, 2)
        P_scene = ax.c2p(*self.ps_P)
        dot_P = Dot(P_scene, radius=0.12, color=C_HL)
        label_P = MathTex(r"(1,\ 2)", font_size=26, color=C_HL).next_to(dot_P, UR, buff=0.15)
        self.play(FadeIn(dot_P, scale=0.4), Write(label_P), run_time=0.5)

        # 用虚线展示 rise / run，演示斜率
        # run: (1,0) → (2,0)  /  rise: (2,0) → (2,2) 的方向（在坐标系坐标里）
        pt_run_end = np.array([2.0, 0.0])   # (run结束) x轴上
        pt_rise_end = np.array([2.0, 2.0])  # (rise结束) = P的右移一位 + 上移2位

        # 从 P(1,2) 向右走1单位 → Q(2,2)
        Q = np.array([2.0, 2.0])
        # 从 Q(2,2) 向下走到(2,0) 也可以;  
        # 更直观：从原点沿x轴向右1, 再向上2
        # 改用: 从P(1,2)出发, right→(2,2), 再下→(2,0) not intuitive
        # 最佳: 从(0,0)出发，run到(1,0)，rise到(1,2)
        O_scene = ax.c2p(0, 0)
        R_scene = ax.c2p(1, 0)   # run end
        P2_scene = ax.c2p(1, 2)  # = P

        run_line  = DashedLine(O_scene, R_scene, color=C_AX, dash_length=0.1, stroke_width=2)
        rise_line = DashedLine(R_scene, P2_scene, color=C_AX, dash_length=0.1, stroke_width=2)
        run_brace  = BraceBetweenPoints(O_scene, R_scene, direction=DOWN, color=GRAY_A)
        rise_brace = BraceBetweenPoints(R_scene, P2_scene, direction=RIGHT, color=GRAY_A)
        run_label  = Text("run=1", font=FONT, font_size=18, color=GRAY_A).next_to(run_brace,  DOWN,  buff=0.1)
        rise_label = Text("rise=2", font=FONT, font_size=18, color=GRAY_A).next_to(rise_brace, RIGHT, buff=0.1)

        self.play(Create(run_line), GrowFromEdge(run_brace, LEFT), FadeIn(run_label), run_time=0.6)
        self.play(Create(rise_line), GrowFromEdge(rise_brace, DOWN), FadeIn(rise_label), run_time=0.6)

        slope_text = Text("斜率 k = rise/run = 2", font=FONT, font_size=24, color=C_HL
                          ).move_to(DOWN*3.3)
        self.play(FadeIn(slope_text, shift=UP*0.2), run_time=0.5)
        self.wait(0.5)

        # 公式卡片
        card = self.formula_card("点斜式", r"y - y_0 = k(x - x_0)", C_PS)
        card_example = MathTex(r"y - 2 = 2(x - 1)", font_size=26, color=GRAY_A
                               ).next_to(card, DOWN, buff=0.15)
        self.play(FadeIn(card), run_time=0.5)
        self.play(Write(card_example), run_time=0.5)
        self.wait(1.4)

        # 清理
        self.play(*[FadeOut(o) for o in [
            scene_label, ax, lx, ly, line, dot_P, label_P,
            run_line, rise_line, run_brace, rise_brace, run_label, rise_label,
            slope_text, card, card_example
        ]], run_time=0.5)

    # ══════════════════════════════════════════
    # Scene 3  斜截式
    # ══════════════════════════════════════════
    def scene_slope_intercept(self):
        scene_label = Text("② 斜截式", font=FONT, font_size=38, color=C_SI).move_to(UP*5.5)
        self.play(Write(scene_label), run_time=0.5)

        ax, lx, ly = self.make_axes()
        self.play(Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.9)

        # 画 y = x + 3
        line = self.line_on_axes(ax, self.si_k, self.si_b, C_SI)
        self.play(Create(line), run_time=0.8)

        # 标记 y 截距 b = 3
        y_int_scene = ax.c2p(0, self.si_b)
        dot_b = Dot(y_int_scene, radius=0.12, color=C_HL)
        label_b = MathTex(r"b = 3", font_size=28, color=C_HL).next_to(dot_b, RIGHT, buff=0.18)
        self.play(FadeIn(dot_b, scale=0.4), Write(label_b), run_time=0.5)

        # 竖向虚线 + Brace 标注截距
        origin_scene = ax.c2p(0, 0)
        v_dash = DashedLine(origin_scene, y_int_scene, color=C_HL,
                            dash_length=0.1, stroke_width=2.5)
        v_brace = BraceBetweenPoints(origin_scene, y_int_scene, direction=LEFT, color=C_HL)
        v_text  = Text("y轴截距 b", font=FONT, font_size=20, color=C_HL
                       ).next_to(v_brace, LEFT, buff=0.12)
        self.play(Create(v_dash), GrowFromEdge(v_brace, DOWN), FadeIn(v_text), run_time=0.7)

        # 说明
        explain = Text("直线与y轴的交点纵坐标就是b", font=FONT, font_size=23, color=WHITE
                       ).move_to(DOWN*3.3)
        self.play(FadeIn(explain, shift=UP*0.2), run_time=0.5)
        self.wait(0.5)

        # 公式卡片
        card = self.formula_card("斜截式", r"y = kx + b", C_SI)
        card_ex = MathTex(r"y = x + 3", font_size=26, color=GRAY_A
                          ).next_to(card, DOWN, buff=0.15)
        self.play(FadeIn(card), Write(card_ex), run_time=0.6)
        self.wait(1.3)

        self.play(*[FadeOut(o) for o in [
            scene_label, ax, lx, ly, line,
            dot_b, label_b, v_dash, v_brace, v_text,
            explain, card, card_ex
        ]], run_time=0.5)

    # ══════════════════════════════════════════
    # Scene 4  两点式
    # ══════════════════════════════════════════
    def scene_two_point(self):
        scene_label = Text("③ 两点式", font=FONT, font_size=38, color=C_TP).move_to(UP*5.5)
        self.play(Write(scene_label), run_time=0.5)

        ax, lx, ly = self.make_axes()
        self.play(Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.9)

        # 画直线 y = x + 2
        line = self.line_on_axes(ax, self.tp_k, self.tp_b, C_TP)
        self.play(Create(line), run_time=0.8)

        # 标记两点
        P1s = ax.c2p(*self.tp_P1)
        P2s = ax.c2p(*self.tp_P2)
        dot1 = Dot(P1s, radius=0.12, color=C_HL)
        dot2 = Dot(P2s, radius=0.12, color=C_HL)
        lbl1 = MathTex(r"P_1(-1,\ 1)", font_size=24, color=C_HL).next_to(dot1, DL, buff=0.15)
        lbl2 = MathTex(r"P_2(2,\ 4)",  font_size=24, color=C_HL).next_to(dot2, UR, buff=0.15)
        self.play(FadeIn(dot1, scale=0.4), FadeIn(dot2, scale=0.4), run_time=0.4)
        self.play(Write(lbl1), Write(lbl2), run_time=0.5)

        # 辅助直角三角形（Px = (2, 1)）
        Pxs = ax.c2p(*self.tp_Px)
        h_dash = DashedLine(P1s, Pxs, color=GRAY_B, dash_length=0.1, stroke_width=2)  # 水平
        v_dash = DashedLine(Pxs, P2s, color=GRAY_B, dash_length=0.1, stroke_width=2)  # 竖直
        self.play(Create(h_dash), Create(v_dash), run_time=0.6)

        # Brace 标注 Δx 和 Δy
        brace_dx = BraceBetweenPoints(P1s, Pxs, direction=DOWN, color=GRAY_A)
        brace_dy = BraceBetweenPoints(Pxs, P2s, direction=RIGHT, color=GRAY_A)
        lbl_dx = MathTex(r"x_2 - x_1", font_size=20, color=GRAY_A).next_to(brace_dx, DOWN, buff=0.1)
        lbl_dy = MathTex(r"y_2 - y_1", font_size=20, color=GRAY_A).next_to(brace_dy, RIGHT, buff=0.1)
        self.play(
            GrowFromEdge(brace_dx, LEFT), FadeIn(lbl_dx),
            GrowFromEdge(brace_dy, DOWN), FadeIn(lbl_dy),
            run_time=0.6
        )

        # 直角标记（Px 处）
        # 水平向量从 Px 到 P1，竖直向量从 Px 到 P2
        # 验证脚本已确认为直角，叉积z=-9（顺时针）→ 用 other_angle 的 Elbow
        size = 0.18
        vec_h = (P1s - Pxs) / np.linalg.norm(P1s - Pxs) * size  # 向左
        vec_v = (P2s - Pxs) / np.linalg.norm(P2s - Pxs) * size  # 向上
        right_angle_sq = Polygon(
            Pxs, Pxs + vec_h, Pxs + vec_h + vec_v, Pxs + vec_v,
            color=GRAY_A, stroke_width=1.5, fill_opacity=0
        )
        self.play(Create(right_angle_sq), run_time=0.3)

        explain = Text("相似比 → 斜率不变 → 方程", font=FONT, font_size=23, color=WHITE
                       ).move_to(DOWN*3.3)
        self.play(FadeIn(explain, shift=UP*0.2), run_time=0.5)
        self.wait(0.5)

        # 公式卡片
        card = self.formula_card(
            "两点式",
            r"\frac{y-y_1}{y_2-y_1}=\frac{x-x_1}{x_2-x_1}",
            C_TP, height=1.8
        )
        card_ex = MathTex(r"y - 1 = x + 1\ \Rightarrow\ y = x + 2",
                          font_size=24, color=GRAY_A).next_to(card, DOWN, buff=0.15)
        self.play(FadeIn(card), Write(card_ex), run_time=0.7)
        self.wait(1.3)

        self.play(*[FadeOut(o) for o in [
            scene_label, ax, lx, ly, line,
            dot1, dot2, lbl1, lbl2,
            h_dash, v_dash, brace_dx, brace_dy, lbl_dx, lbl_dy,
            right_angle_sq, explain, card, card_ex
        ]], run_time=0.5)

    # ══════════════════════════════════════════
    # Scene 5  截距式
    # ══════════════════════════════════════════
    def scene_intercept(self):
        scene_label = Text("④ 截距式", font=FONT, font_size=38, color=C_IC).move_to(UP*5.5)
        self.play(Write(scene_label), run_time=0.5)

        ax, lx, ly = self.make_axes()
        self.play(Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.9)

        # 画 y = -2x/3 + 2  (x/3 + y/2 = 1)
        line = self.line_on_axes(ax, self.ic_k, self.ic_bi, C_IC)
        self.play(Create(line), run_time=0.8)

        # x 截距点 (3, 0)
        x_int_scene = ax.c2p(self.ic_a, 0)
        dot_a = Dot(x_int_scene, radius=0.12, color=C_IC)
        lbl_a = MathTex(r"(3,\ 0)", font_size=26, color=C_IC).next_to(dot_a, DR, buff=0.15)
        self.play(FadeIn(dot_a, scale=0.4), Write(lbl_a), run_time=0.5)

        # y 截距点 (0, 2)
        y_int_scene = ax.c2p(0, self.ic_b)
        dot_b = Dot(y_int_scene, radius=0.12, color=C_IC)
        lbl_b = MathTex(r"(0,\ 2)", font_size=26, color=C_IC).next_to(dot_b, UL, buff=0.15)
        self.play(FadeIn(dot_b, scale=0.4), Write(lbl_b), run_time=0.5)

        # Flash 强调
        self.play(
            Flash(dot_a, color=C_IC, flash_radius=0.3),
            Flash(dot_b, color=C_IC, flash_radius=0.3),
            run_time=0.5
        )

        # 标注 a, b
        origin_scene = ax.c2p(0, 0)
        brace_a = BraceBetweenPoints(origin_scene, x_int_scene, direction=DOWN, color=GRAY_A)
        brace_b = BraceBetweenPoints(origin_scene, y_int_scene, direction=LEFT, color=GRAY_A)
        text_a  = Text("x截距 a=3", font=FONT, font_size=19, color=GRAY_A
                       ).next_to(brace_a, DOWN, buff=0.1)
        text_b  = Text("y截距 b=2", font=FONT, font_size=19, color=GRAY_A
                       ).next_to(brace_b, LEFT, buff=0.1)
        self.play(
            GrowFromEdge(brace_a, LEFT), FadeIn(text_a),
            GrowFromEdge(brace_b, DOWN), FadeIn(text_b),
            run_time=0.6
        )

        explain = Text("两截距各自独立，记忆方便！", font=FONT, font_size=23, color=WHITE
                       ).move_to(DOWN*3.3)
        self.play(FadeIn(explain, shift=UP*0.2), run_time=0.5)
        self.wait(0.5)

        # 公式卡片
        card = self.formula_card("截距式", r"\frac{x}{a}+\frac{y}{b}=1", C_IC)
        card_ex = MathTex(r"\frac{x}{3}+\frac{y}{2}=1", font_size=28, color=GRAY_A
                          ).next_to(card, DOWN, buff=0.15)
        self.play(FadeIn(card), Write(card_ex), run_time=0.6)
        self.wait(1.3)

        self.play(*[FadeOut(o) for o in [
            scene_label, ax, lx, ly, line,
            dot_a, lbl_a, dot_b, lbl_b,
            brace_a, brace_b, text_a, text_b,
            explain, card, card_ex
        ]], run_time=0.5)

    # ══════════════════════════════════════════
    # Scene 6  一般式
    # ══════════════════════════════════════════
    def scene_general(self):
        scene_label = Text("⑤ 一般式", font=FONT, font_size=38, color=C_GN).move_to(UP*5.5)
        self.play(Write(scene_label), run_time=0.5)

        ax, lx, ly = self.make_axes()
        self.play(Create(ax), FadeIn(lx), FadeIn(ly), run_time=0.9)

        # 同一直线 y = -2x/3 + 2（与截距式相同）
        line = self.line_on_axes(ax, self.gn_k, self.gn_bi, C_GN)
        self.play(Create(line), run_time=0.8)

        # 两个截距点（已知）
        P_x = ax.c2p(3, 0)
        P_y = ax.c2p(0, 2)
        dot_x = Dot(P_x, radius=0.1, color=GRAY_A)
        dot_y = Dot(P_y, radius=0.1, color=GRAY_A)
        self.play(FadeIn(dot_x), FadeIn(dot_y), run_time=0.3)

        # 方程 2x + 3y - 6 = 0
        eq_general = MathTex(r"2x + 3y - 6 = 0", font_size=36, color=C_GN).move_to(DOWN*3.2)
        self.play(Write(eq_general), run_time=0.7)
        self.wait(0.4)

        # 变形 → 斜截式
        arrow_tf = Text("化为斜截式 →", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN*4.2)
        eq_slope = MathTex(r"y = -\frac{2}{3}x + 2", font_size=32, color=GRAY_A).move_to(DOWN*5.1)
        self.play(FadeIn(arrow_tf, shift=UP*0.2), run_time=0.4)
        self.play(Write(eq_slope), run_time=0.6)
        self.wait(0.5)

        # 强调"最通用"
        note = Text("最通用！可表示所有直线（包括垂直线）", font=FONT, font_size=21, color=C_HL
                    ).move_to(DOWN*6.1)
        self.play(FadeIn(note, shift=UP*0.2), run_time=0.5)
        self.wait(1.2)

        self.play(*[FadeOut(o) for o in [
            scene_label, ax, lx, ly, line,
            dot_x, dot_y,
            eq_general, arrow_tf, eq_slope, note
        ]], run_time=0.5)

    # ══════════════════════════════════════════
    # Scene 7  总结
    # ══════════════════════════════════════════
    def scene_summary(self):
        title_s = Text("五种形式总览", font=FONT, font_size=40, color=GOLD).move_to(UP*5.5)
        self.play(Write(title_s), run_time=0.6)

        # 五行对比卡片
        rows = [
            ("① 点斜式", r"y - y_0 = k(x - x_0)", C_PS, "已知一点+斜率"),
            ("② 斜截式", r"y = kx + b",            C_SI, "斜率+y截距"),
            ("③ 两点式", r"\frac{y-y_1}{y_2-y_1}=\frac{x-x_1}{x_2-x_1}", C_TP, "已知两点"),
            ("④ 截距式", r"\frac{x}{a}+\frac{y}{b}=1", C_IC, "已知两截距"),
            ("⑤ 一般式", r"Ax + By + C = 0",       C_GN, "最通用形式"),
        ]

        card_objs = []
        start_y = 4.3
        gap = 1.75
        for i, (name, tex, color, hint) in enumerate(rows):
            y_pos = start_y - i * gap
            # 卡片背景
            bg = RoundedRectangle(
                width=8.2, height=1.5, corner_radius=0.15,
                fill_color=C_BG_CARD, fill_opacity=1,
                stroke_color=color, stroke_width=2
            ).move_to(UP * y_pos)

            # 名称
            name_t = Text(name, font=FONT, font_size=22, color=color).move_to(
                bg.get_center() + LEFT * 2.8
            )
            # 公式
            formula_t = MathTex(tex, font_size=22, color=WHITE).move_to(
                bg.get_center() + RIGHT * 0.3
            )
            # 适用提示（最右侧小字）
            hint_t = Text(hint, font=FONT, font_size=16, color=GRAY_B).move_to(
                bg.get_right() + LEFT * 0.8
            )

            card = VGroup(bg, name_t, formula_t)
            card.shift(LEFT * 12)
            self.add(card)
            self.play(card.animate.shift(RIGHT * 12), run_time=0.4)
            card_objs.append(card)

        self.wait(1.5)

        # 技巧提示
        tip = Text(
            "💡  根据已知条件灵活选择最简形式！",
            font=FONT, font_size=25, color=C_HL
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(tip, shift=UP*0.3), run_time=0.6)
        self.wait(1.8)

        self.play(
            *[FadeOut(c) for c in card_objs],
            FadeOut(title_s), FadeOut(tip),
            run_time=0.6
        )

    # ══════════════════════════════════════════
    # Scene 8  片尾
    # ══════════════════════════════════════════
    def scene_outro(self):
        self.play(FadeOut(self.title_obj), run_time=0.4)

        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 2.2)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 1.2)
        follow_t = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=C_HL
        ).move_to(DOWN * 0.1)

        self.play(Transform(self.author_banner, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(follow_t, scale=1.05, shift=UP*0.2), run_time=0.6)

        # 五个彩色圆点装饰（代表五种形式）
        dots_deco = VGroup(*[
            Dot(radius=0.22, color=col, fill_opacity=0.9)
            for col in [C_PS, C_SI, C_TP, C_IC, C_GN]
        ]).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.8)

        self.play(*[FadeIn(d, scale=0.5) for d in dots_deco], run_time=0.5)
        self.play(
            *[d.animate.shift(UP * 0.25) for d in dots_deco[::2]],   # 奇数跳
            *[d.animate.shift(DOWN * 0.25) for d in dots_deco[1::2]], # 偶数沉
            run_time=0.5
        )
        self.play(
            *[d.animate.shift(DOWN * 0.25) for d in dots_deco[::2]],
            *[d.animate.shift(UP * 0.25) for d in dots_deco[1::2]],
            run_time=0.5
        )

        bottom_tip = Text(
            "直线方程五合一，灵活运用得高分！",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(bottom_tip, shift=UP*0.2), run_time=0.5)

        self.wait(1.5)
        self.play(
            *[FadeOut(o) for o in [
                self.author_banner, author_id, follow_t,
                dots_deco, bottom_tip
            ]],
            run_time=1.0
        )
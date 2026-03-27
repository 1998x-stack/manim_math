"""
角的分类 - Angle Classification Animation
四年级数学教学动画: 锐角、直角、钝角、平角、周角

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# TikTok竖屏配置
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class AngleClassifyLesson(Scene):
    """
    角的分类教学动画

    场景顺序:
    1. 开场钩子
    2. 锐角 (0 < alpha < 90)
    3. 直角 (alpha = 90)
    4. 钝角 (90 < alpha < 180)
    5. 平角 (alpha = 180)
    6. 周角 (alpha = 360)
    7. 关系总结 (1周角=2平角=4直角)
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_ACUTE = "#4ecdc4"      # 青色 - 锐角
        self.COLOR_RIGHT = "#45b7d1"      # 蓝色 - 直角
        self.COLOR_OBTUSE = "#f9ca24"     # 黄色 - 钝角
        self.COLOR_STRAIGHT = "#f0932b"   # 橙色 - 平角
        self.COLOR_FULL = "#eb4d4b"       # 红色 - 周角
        self.COLOR_HIGHLIGHT = "#ffd32a"
        self.COLOR_TEXT = "#e2e8f0"
        self.COLOR_SECONDARY = "#a29bfe"

        # 主角顶点
        self.VERTEX = np.array([0.0, 0.5, 0])
        self.RAY_LEN = 2.8

        # 作者标识（全程显示）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.add(self.author)

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_acute()
        self.scene_3_right()
        self.scene_4_obtuse()
        self.scene_5_straight()
        self.scene_6_full()
        self.scene_7_summary()
        self.scene_8_outro()

    # ─────────────────────────────────────────
    # 工具函数
    # ─────────────────────────────────────────

    def make_ray(self, vertex, angle_deg, length, color=WHITE, stroke_width=4):
        """从顶点出发，angle_deg（度，从正x轴逆时针）的射线"""
        angle_rad = np.radians(angle_deg)
        end = vertex + length * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        return Line(vertex, end, color=color, stroke_width=stroke_width)

    def make_arc(self, vertex, start_deg, sweep_deg, radius=0.55, color=YELLOW):
        """在 vertex 处从 start_deg 扫过 sweep_deg（逆时针）的角弧"""
        return Arc(
            radius=radius,
            start_angle=np.radians(start_deg),
            angle=np.radians(sweep_deg),
            color=color,
            stroke_width=3,
            arc_center=vertex,
        )

    def arc_mid_pos(self, vertex, start_deg, sweep_deg, radius=0.85):
        """弧中心方向的标签位置"""
        mid_deg = start_deg + sweep_deg / 2
        mid_rad = np.radians(mid_deg)
        return vertex + radius * np.array([np.cos(mid_rad), np.sin(mid_rad), 0])

    def right_angle_mark(self, vertex, base_deg, arm_deg, size=0.25, color=YELLOW):
        """在顶点处画直角符号（小方块）"""
        base_rad = np.radians(base_deg)
        arm_rad = np.radians(arm_deg)
        v_base = np.array([np.cos(base_rad), np.sin(base_rad), 0])
        v_arm = np.array([np.cos(arm_rad), np.sin(arm_rad), 0])
        p1 = vertex + size * v_base
        p2 = vertex + size * v_base + size * v_arm
        p3 = vertex + size * v_arm
        return Polygon(vertex, p1, p2, p3,
                       color=color, stroke_width=2, fill_opacity=0)

    def make_icon(self, name, vx, col, ray_r=0.55, sw=2.2):
        """根据角名称生成小图标"""
        if name == "锐角":
            r1 = self.make_ray(vx, 0, ray_r, color=col, stroke_width=sw)
            r2 = self.make_ray(vx, 45, ray_r, color=col, stroke_width=sw)
            arc = self.make_arc(vx, 0, 45, radius=0.19, color=YELLOW)
            return VGroup(r1, r2, arc)
        elif name == "直角":
            r1 = self.make_ray(vx, 0, ray_r, color=col, stroke_width=sw)
            r2 = self.make_ray(vx, 90, ray_r, color=col, stroke_width=sw)
            sq = self.right_angle_mark(vx, 0, 90, size=0.13, color=YELLOW)
            return VGroup(r1, r2, sq)
        elif name == "钝角":
            r1 = self.make_ray(vx, 0, ray_r, color=col, stroke_width=sw)
            r2 = self.make_ray(vx, 120, ray_r, color=col, stroke_width=sw)
            arc = self.make_arc(vx, 0, 120, radius=0.19, color=YELLOW)
            return VGroup(r1, r2, arc)
        elif name == "平角":
            r1 = self.make_ray(vx, 0, ray_r, color=col, stroke_width=sw)
            r2 = self.make_ray(vx, 180, ray_r, color=col, stroke_width=sw)
            arc = self.make_arc(vx, 0, 180, radius=0.17, color=YELLOW)
            return VGroup(r1, r2, arc)
        else:  # 周角
            r1 = self.make_ray(vx, 0, ray_r, color=col, stroke_width=sw)
            circ = Circle(radius=0.19, color=YELLOW, stroke_width=2).move_to(vx)
            return VGroup(r1, circ)

    # ─────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────

    def scene_1_opening(self):
        title = Text("角的分类", font="Noto Sans CJK SC",
                     font_size=56, color=self.COLOR_HIGHLIGHT).move_to(UP * 5.5)
        subtitle = Text("锐角 · 直角 · 钝角 · 平角 · 周角",
                        font="Noto Sans CJK SC",
                        font_size=26, color=self.COLOR_TEXT).move_to(UP * 4.6)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.5)

        hook = Text("你能分清这5种角吗？",
                    font="Noto Sans CJK SC",
                    font_size=30, color=self.COLOR_SECONDARY).move_to(UP * 3.6)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 5个小预览角水平排列
        demo_data = [
            (45, self.COLOR_ACUTE, "锐角"),
            (90, self.COLOR_RIGHT, "直角"),
            (120, self.COLOR_OBTUSE, "钝角"),
            (180, self.COLOR_STRAIGHT, "平角"),
            (360, self.COLOR_FULL, "周角"),
        ]
        xs = np.linspace(-3.2, 3.2, 5)
        y_demo = 2.0
        ray_r = 0.8

        demo_group = VGroup()
        for (deg, col, name), x in zip(demo_data, xs):
            vx = np.array([x, y_demo, 0])
            icon = self.make_icon(name, vx, col, ray_r=ray_r, sw=2.5)
            lbl = Text(name, font="Noto Sans CJK SC",
                       font_size=18, color=col)
            lbl.next_to(icon, DOWN, buff=0.15)
            demo_group.add(VGroup(icon, lbl))

        self.play(
            *[FadeIn(demo_group[i], shift=UP * 0.2) for i in range(5)],
            run_time=1.0,
        )
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(hook), FadeOut(demo_group),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # 场景 2: 锐角
    # ─────────────────────────────────────────

    def scene_2_acute(self):
        col = self.COLOR_ACUTE
        title = Text("锐角", font="Noto Sans CJK SC",
                     font_size=48, color=col).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        def_text = Text("比直角小的角", font="Noto Sans CJK SC",
                        font_size=26, color=self.COLOR_TEXT).move_to(UP * 5.05)
        self.play(FadeIn(def_text), run_time=0.4)

        formula = MathTex(r"0^\circ < \alpha < 90^\circ",
                          font_size=38, color=col).move_to(UP * 4.1)
        self.play(Write(formula), run_time=0.6)

        V = self.VERTEX
        ang_deg = 45
        ray1 = self.make_ray(V, 0, self.RAY_LEN, color=col)
        ray2 = self.make_ray(V, ang_deg, self.RAY_LEN, color=col)
        arc = self.make_arc(V, 0, ang_deg, radius=0.55, color=self.COLOR_HIGHLIGHT)
        lbl_pos = self.arc_mid_pos(V, 0, ang_deg, radius=0.88)
        ang_label = MathTex(r"45^\circ", font_size=32,
                            color=self.COLOR_HIGHLIGHT).move_to(lbl_pos)
        v_dot = Dot(V, color=WHITE, radius=0.07)

        self.play(Create(ray1), Create(ray2), run_time=0.6)
        self.play(Create(arc), FadeIn(v_dot), run_time=0.5)
        self.play(Write(ang_label), run_time=0.4)

        # 3个示例小角
        hint = Text("常见锐角：30°、45°、60°……",
                    font="Noto Sans CJK SC",
                    font_size=22, color=self.COLOR_TEXT).move_to(DOWN * 1.3)
        self.play(FadeIn(hint), run_time=0.4)

        small_group = VGroup()
        for j, deg in enumerate([30, 45, 60]):
            vx = np.array([-2.2 + j * 2.2, -2.9, 0])
            r1 = self.make_ray(vx, 0, 1.1, color=col, stroke_width=2.5)
            r2 = self.make_ray(vx, deg, 1.1, color=col, stroke_width=2.5)
            a = self.make_arc(vx, 0, deg, radius=0.34, color=self.COLOR_HIGHLIGHT)
            lp = self.arc_mid_pos(vx, 0, deg, radius=0.56)
            lbl = MathTex(f"{deg}^\\circ", font_size=22,
                          color=self.COLOR_HIGHLIGHT).move_to(lp)
            small_group.add(VGroup(r1, r2, a, lbl))

        self.play(*[Create(small_group[k]) for k in range(3)], run_time=0.8)

        tip = Text("锐角 < 90°，比直角更尖！",
                   font="Noto Sans CJK SC",
                   font_size=22, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(formula),
            FadeOut(ray1), FadeOut(ray2), FadeOut(arc),
            FadeOut(v_dot), FadeOut(ang_label),
            FadeOut(hint), FadeOut(small_group), FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # 场景 3: 直角
    # ─────────────────────────────────────────

    def scene_3_right(self):
        col = self.COLOR_RIGHT
        title = Text("直角", font="Noto Sans CJK SC",
                     font_size=48, color=col).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        def_text = Text("等于 90° 的角", font="Noto Sans CJK SC",
                        font_size=26, color=self.COLOR_TEXT).move_to(UP * 5.05)
        self.play(FadeIn(def_text), run_time=0.4)

        formula = MathTex(r"\alpha = 90^\circ",
                          font_size=42, color=col).move_to(UP * 4.1)
        self.play(Write(formula), run_time=0.6)

        V = self.VERTEX
        ray1 = self.make_ray(V, 0, self.RAY_LEN, color=col)
        ray2 = self.make_ray(V, 90, self.RAY_LEN, color=col)
        sq_mark = self.right_angle_mark(V, 0, 90, size=0.28, color=self.COLOR_HIGHLIGHT)
        ang_label = MathTex(r"90^\circ", font_size=32,
                            color=self.COLOR_HIGHLIGHT).move_to(V + np.array([0.62, 0.62, 0]))
        v_dot = Dot(V, color=WHITE, radius=0.07)

        self.play(Create(ray1), Create(ray2), run_time=0.6)
        self.play(Create(sq_mark), FadeIn(v_dot), run_time=0.4)
        self.play(Write(ang_label), run_time=0.4)

        note = Text("小方块 □ 表示直角",
                    font="Noto Sans CJK SC",
                    font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 1.1)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.play(Indicate(sq_mark, color=self.COLOR_HIGHLIGHT, scale_factor=1.5),
                  run_time=0.6)

        life_items = ["课本的角", "黑板的角", "正方形的角"]
        life_group = VGroup()
        for i, item in enumerate(life_items):
            t = Text(f"· {item}", font="Noto Sans CJK SC",
                     font_size=22, color=self.COLOR_TEXT)
            life_group.add(t)
        life_group.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        life_group.move_to(DOWN * 2.6)

        self.play(FadeIn(life_group, shift=RIGHT * 0.3), run_time=0.5)

        tip = Text("直角是角分类的基准！",
                   font="Noto Sans CJK SC",
                   font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(formula),
            FadeOut(ray1), FadeOut(ray2), FadeOut(sq_mark),
            FadeOut(v_dot), FadeOut(ang_label),
            FadeOut(note), FadeOut(life_group), FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # 场景 4: 钝角
    # ─────────────────────────────────────────

    def scene_4_obtuse(self):
        col = self.COLOR_OBTUSE
        title = Text("钝角", font="Noto Sans CJK SC",
                     font_size=48, color=col).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        def_text = Text("比直角大、比平角小的角",
                        font="Noto Sans CJK SC",
                        font_size=24, color=self.COLOR_TEXT).move_to(UP * 5.05)
        self.play(FadeIn(def_text), run_time=0.4)

        formula = MathTex(r"90^\circ < \alpha < 180^\circ",
                          font_size=36, color=col).move_to(UP * 4.1)
        self.play(Write(formula), run_time=0.6)

        V = self.VERTEX
        ang_deg = 120
        ray1 = self.make_ray(V, 0, self.RAY_LEN, color=col)
        ray2 = self.make_ray(V, ang_deg, self.RAY_LEN, color=col)
        arc = self.make_arc(V, 0, ang_deg, radius=0.55, color=self.COLOR_HIGHLIGHT)
        lbl_pos = self.arc_mid_pos(V, 0, ang_deg, radius=0.88)
        ang_label = MathTex(r"120^\circ", font_size=32,
                            color=self.COLOR_HIGHLIGHT).move_to(lbl_pos)
        v_dot = Dot(V, color=WHITE, radius=0.07)

        self.play(Create(ray1), Create(ray2), run_time=0.6)
        self.play(Create(arc), FadeIn(v_dot), run_time=0.5)
        self.play(Write(ang_label), run_time=0.4)

        compare = Text("比直角 (90°) 大，比平角 (180°) 小",
                       font="Noto Sans CJK SC",
                       font_size=22, color=self.COLOR_TEXT).move_to(DOWN * 1.1)
        self.play(FadeIn(compare), run_time=0.5)

        # 虚线参考直角
        ref_end = V + self.RAY_LEN * np.array([0, 1, 0])
        ref_ray = DashedLine(
            V, ref_end,
            color=self.COLOR_RIGHT, dash_length=0.12, stroke_width=2,
        )
        ref_label = MathTex(r"90^\circ", font_size=22,
                            color=self.COLOR_RIGHT).next_to(ref_ray, RIGHT, buff=0.1)
        self.play(Create(ref_ray), Write(ref_label), run_time=0.5)

        tip = Text("90° < 钝角 < 180°",
                   font="Noto Sans CJK SC",
                   font_size=26, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(formula),
            FadeOut(ray1), FadeOut(ray2), FadeOut(arc),
            FadeOut(v_dot), FadeOut(ang_label),
            FadeOut(compare), FadeOut(ref_ray), FadeOut(ref_label),
            FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # 场景 5: 平角
    # ─────────────────────────────────────────

    def scene_5_straight(self):
        col = self.COLOR_STRAIGHT
        title = Text("平角", font="Noto Sans CJK SC",
                     font_size=48, color=col).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        def_text = Text("等于 180°，两边在同一直线上",
                        font="Noto Sans CJK SC",
                        font_size=24, color=self.COLOR_TEXT).move_to(UP * 5.05)
        self.play(FadeIn(def_text), run_time=0.4)

        formula = MathTex(r"\alpha = 180^\circ",
                          font_size=42, color=col).move_to(UP * 4.1)
        self.play(Write(formula), run_time=0.6)

        V = self.VERTEX
        ray1 = self.make_ray(V, 0, self.RAY_LEN, color=col)
        ray2 = self.make_ray(V, 180, self.RAY_LEN, color=col)
        arc = self.make_arc(V, 0, 180, radius=0.55, color=self.COLOR_HIGHLIGHT)
        ang_label = MathTex(r"180^\circ", font_size=30,
                            color=self.COLOR_HIGHLIGHT).move_to(V + UP * 0.88)
        v_dot = Dot(V, color=WHITE, radius=0.08)

        self.play(Create(ray1), Create(ray2), run_time=0.6)
        self.play(Create(v_dot), run_time=0.3)
        self.play(Create(arc), run_time=0.5)
        self.play(Write(ang_label), run_time=0.4)

        # 1平角 = 2直角 演示
        rel1 = Text("1平角", font="Noto Sans CJK SC",
                    font_size=28, color=col)
        eq1 = MathTex(r"=", font_size=30, color=WHITE)
        rel2 = Text("2直角", font="Noto Sans CJK SC",
                    font_size=28, color=self.COLOR_RIGHT)
        rel_group = VGroup(rel1, eq1, rel2).arrange(RIGHT, buff=0.2)
        rel_group.move_to(DOWN * 1.2)
        self.play(FadeIn(rel_group, shift=UP * 0.2), run_time=0.5)

        # 分割线显示2个直角
        split_end = V + UP * self.RAY_LEN
        split_line = DashedLine(
            V, split_end,
            color=self.COLOR_RIGHT, dash_length=0.12, stroke_width=2.5,
        )
        sq1 = self.right_angle_mark(V, 0, 90, size=0.22, color=self.COLOR_RIGHT)
        sq2 = self.right_angle_mark(V, 180, 90, size=0.22, color=self.COLOR_RIGHT)

        self.play(Create(split_line), run_time=0.4)
        self.play(Create(sq1), Create(sq2), run_time=0.4)

        tip = Text("平角看起来就是一条直线！",
                   font="Noto Sans CJK SC",
                   font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(formula),
            FadeOut(ray1), FadeOut(ray2), FadeOut(v_dot),
            FadeOut(arc), FadeOut(ang_label),
            FadeOut(rel_group), FadeOut(split_line),
            FadeOut(sq1), FadeOut(sq2), FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # 场景 6: 周角
    # ─────────────────────────────────────────

    def scene_6_full(self):
        col = self.COLOR_FULL
        title = Text("周角", font="Noto Sans CJK SC",
                     font_size=48, color=col).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        def_text = Text("旋转一周形成的角，等于 360°",
                        font="Noto Sans CJK SC",
                        font_size=24, color=self.COLOR_TEXT).move_to(UP * 5.05)
        self.play(FadeIn(def_text), run_time=0.4)

        formula = MathTex(r"\alpha = 360^\circ",
                          font_size=42, color=col).move_to(UP * 4.1)
        self.play(Write(formula), run_time=0.6)

        V = self.VERTEX
        v_dot = Dot(V, color=WHITE, radius=0.08)
        base_ray = self.make_ray(V, 0, self.RAY_LEN, color=col)
        self.play(Create(base_ray), FadeIn(v_dot), run_time=0.5)

        # 圆圈 + 旋转射线动画
        full_circle = Circle(radius=0.6, color=self.COLOR_HIGHLIGHT,
                             stroke_width=3).move_to(V)
        rotating_ray = self.make_ray(V, 0, self.RAY_LEN, color=col)
        self.add(rotating_ray)
        self.play(
            Rotate(rotating_ray, angle=2 * PI, about_point=V),
            Create(full_circle),
            run_time=2.0,
            rate_func=smooth,
        )
        self.remove(rotating_ray)

        ang_label = MathTex(r"360^\circ", font_size=30,
                            color=self.COLOR_HIGHLIGHT).move_to(V + UP * 0.95)
        self.play(Write(ang_label), run_time=0.4)

        # 关系
        rel1 = Text("1周角", font="Noto Sans CJK SC",
                    font_size=24, color=col)
        eq1 = MathTex(r"=", font_size=26, color=WHITE)
        rel2 = Text("2平角", font="Noto Sans CJK SC",
                    font_size=24, color=self.COLOR_STRAIGHT)
        eq2 = MathTex(r"=", font_size=26, color=WHITE)
        rel3 = Text("4直角", font="Noto Sans CJK SC",
                    font_size=24, color=self.COLOR_RIGHT)
        rel_group = VGroup(rel1, eq1, rel2, eq2, rel3).arrange(RIGHT, buff=0.15)
        rel_group.move_to(DOWN * 1.3)
        self.play(FadeIn(rel_group, shift=UP * 0.2), run_time=0.6)

        # 4条虚线分割显示4个直角
        aux_lines = VGroup()
        for deg in [0, 90, 180, 270]:
            end_pt = V + 0.7 * np.array(
                [np.cos(np.radians(deg)), np.sin(np.radians(deg)), 0]
            )
            aux_lines.add(
                DashedLine(V, end_pt, color=self.COLOR_RIGHT,
                           stroke_width=2, dash_length=0.08)
            )
        self.play(Create(aux_lines), run_time=0.5)

        tip = Text("周角 = 一整圈 = 360°",
                   font="Noto Sans CJK SC",
                   font_size=24, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(formula),
            FadeOut(base_ray), FadeOut(v_dot), FadeOut(full_circle),
            FadeOut(ang_label), FadeOut(rel_group),
            FadeOut(aux_lines), FadeOut(tip),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # 场景 7: 总结对比
    # ─────────────────────────────────────────

    def scene_7_summary(self):
        title = Text("角的分类总结",
                     font="Noto Sans CJK SC",
                     font_size=42, color=self.COLOR_HIGHLIGHT).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        rows_data = [
            ("锐角", r"0^\circ < \alpha < 90^\circ",   self.COLOR_ACUTE),
            ("直角", r"\alpha = 90^\circ",              self.COLOR_RIGHT),
            ("钝角", r"90^\circ < \alpha < 180^\circ",  self.COLOR_OBTUSE),
            ("平角", r"\alpha = 180^\circ",             self.COLOR_STRAIGHT),
            ("周角", r"\alpha = 360^\circ",             self.COLOR_FULL),
        ]
        row_ys = [5.5, 4.55, 3.60, 2.65, 1.70]
        icon_x = -3.8
        row_groups = VGroup()

        for (name, fml_str, col), y in zip(rows_data, row_ys):
            vx = np.array([icon_x, y - 0.05, 0])
            icon = self.make_icon(name, vx, col, ray_r=0.5, sw=2.0)
            name_txt = Text(name, font="Noto Sans CJK SC",
                            font_size=26, color=col).move_to(np.array([-1.7, y, 0]))
            fml = MathTex(fml_str, font_size=24,
                          color=WHITE).move_to(np.array([1.7, y, 0]))
            # 分隔横线
            sep = Line(np.array([-4.2, y - 0.42, 0]),
                       np.array([4.2, y - 0.42, 0]),
                       color="#2d3748", stroke_width=1)
            row_groups.add(VGroup(icon, name_txt, fml, sep))

        for rg in row_groups:
            self.play(FadeIn(rg, shift=RIGHT * 0.3), run_time=0.35)

        # 关键关系框
        rel_bg = RoundedRectangle(
            width=7.8, height=1.45,
            corner_radius=0.3,
            fill_color="#0f3460",
            fill_opacity=0.95,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2,
        ).move_to(DOWN * 3.2)

        rel1 = Text("1周角", font="Noto Sans CJK SC",
                    font_size=24, color=self.COLOR_FULL)
        eq1 = MathTex(r"=", font_size=28, color=WHITE)
        rel2 = Text("2平角", font="Noto Sans CJK SC",
                    font_size=24, color=self.COLOR_STRAIGHT)
        eq2 = MathTex(r"=", font_size=28, color=WHITE)
        rel3 = Text("4直角", font="Noto Sans CJK SC",
                    font_size=24, color=self.COLOR_RIGHT)
        rel_row = VGroup(rel1, eq1, rel2, eq2, rel3).arrange(RIGHT, buff=0.18)
        rel_row.move_to(DOWN * 3.0)

        rel_eq2 = Text("360° = 2×180° = 4×90°",
                       font="Noto Sans CJK SC",
                       font_size=20, color="#94a3b8").move_to(DOWN * 3.65)

        self.play(FadeIn(rel_bg), run_time=0.3)
        self.play(FadeIn(rel_row, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(rel_eq2), run_time=0.4)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(row_groups),
            FadeOut(rel_bg), FadeOut(rel_row), FadeOut(rel_eq2),
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # 场景 8: 片尾
    # ─────────────────────────────────────────

    def scene_8_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38, color=WHITE,
        ).move_to(UP * 2.2)
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28, color="#6b7280",
        ).move_to(UP * 1.4)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我，学更多数学知识！",
            font="Noto Sans CJK SC",
            font_size=28, color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 0.3)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 5种角图标装饰行
        icon_data = [
            (self.COLOR_ACUTE,    "锐角", 45),
            (self.COLOR_RIGHT,    "直角", 90),
            (self.COLOR_OBTUSE,   "钝角", 120),
            (self.COLOR_STRAIGHT, "平角", 180),
            (self.COLOR_FULL,     "周角", 360),
        ]
        icon_xs = np.linspace(-3.2, 3.2, 5)
        icon_y = -1.3
        icons_grp = VGroup()
        for (col, name, _deg), x in zip(icon_data, icon_xs):
            vx = np.array([x, icon_y, 0])
            ic = self.make_icon(name, vx, col, ray_r=0.5, sw=2.0)
            nm = Text(name, font="Noto Sans CJK SC",
                      font_size=16, color=col)
            nm.next_to(ic, DOWN, buff=0.1)
            icons_grp.add(VGroup(ic, nm))

        self.play(
            *[FadeIn(icons_grp[k], scale=0.6) for k in range(5)],
            run_time=0.7,
        )

        # Flash 全部图标
        self.play(
            *[Flash(icons_grp[k], color=icon_data[k][0], flash_radius=0.5)
              for k in range(5)],
            run_time=0.8,
        )

        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)

"""
001_线段射线直线.py — 线段、射线、直线 教学动画

知识点:
  - 线段: 有两个端点，可以度量长度，有限长
  - 射线: 只有一个端点，向一端无限延伸，不可度量
  - 直线: 没有端点，向两端无限延伸，不可度量
  - 三者的区别和联系: 射线和直线都是无限延伸的

年级: 四年级第一学期
格式: TikTok 竖屏 (1080x1920)
时长: 约 90 秒
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
BG_COLOR       = "#1a1a2e"
COLOR_SEGMENT  = "#3b82f6"      # 蓝色 - 线段
COLOR_RAY      = "#22c55e"      # 绿色 - 射线
COLOR_LINE     = "#f59e0b"      # 橙色 - 直线
COLOR_ENDPOINT = "#ef4444"      # 红色 - 端点
COLOR_HL       = "#fbbf24"      # 黄色高亮
COLOR_AUTHOR   = "#6b7280"      # 灰色作者信息
COLOR_ARROW    = "#a78bfa"      # 紫色 - 箭头/无限延伸
COLOR_RULER    = "#06b6d4"      # 青色 - 尺子
FONT           = "PingFang SC"


class LineSegmentRayLesson(Scene):
    """
    线段、射线、直线教学动画

    场景顺序:
      1. 开场钩子 — "线有几种?" + 三种线预览
      2. 线段 — 两个端点, 有限长度, 尺子度量动画
      3. 射线 — 一个端点, 无限延伸动画
      4. 直线 — 没有端点, 两端无限延伸
      5. 对比表格 — 三者属性对比
      6. 关系演示 — 线段 -> 射线 -> 直线 渐变动画
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_line_segment()
        self.scene_3_ray()
        self.scene_4_line()
        self.scene_5_comparison_table()
        self.scene_6_relationship()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""
        self.seg_A = np.array([-3.0, 0.0, 0.0])
        self.seg_B = np.array([3.0, 0.0, 0.0])

        self.ray_origin = np.array([-3.0, 0.0, 0.0])
        self.ray_visible_end = np.array([3.0, 0.0, 0.0])
        self.ray_arrow_end = np.array([4.0, 0.0, 0.0])

        self.line_left = np.array([-4.0, 0.0, 0.0])
        self.line_right = np.array([4.0, 0.0, 0.0])

        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何关系"""
        assert abs(self.seg_A[1] - self.seg_B[1]) < 1e-10
        seg_len = np.linalg.norm(self.seg_B - self.seg_A)
        assert seg_len > 0

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建作者水印"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR,
        ).move_to(UP * 7.2)

    def make_section_title(self, text_str, color=WHITE, y=5.5):
        """创建场景标题"""
        return Text(
            text_str, font=FONT, font_size=36, color=color,
        ).move_to(UP * y)

    def make_endpoint(self, pos, color=COLOR_ENDPOINT, radius=0.12):
        """创建端点"""
        return Dot(pos, color=color, radius=radius, z_index=2)

    def make_label(self, text_str, pos, direction=DOWN, font_size=28,
                   color=WHITE):
        """创建标签"""
        label = Text(text_str, font=FONT, font_size=font_size, color=color)
        label.next_to(pos, direction, buff=0.2)
        return label

    def clean_scene(self, *mobjects, run_time=0.5):
        """统一清除场景元素"""
        if mobjects:
            self.play(*[FadeOut(m) for m in mobjects], run_time=run_time)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者水印
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 问题引入
        hook_q = Text(
            "线有几种?", font=FONT, font_size=42, color=COLOR_HL,
        ).move_to(UP * 5.0)
        self.play(Write(hook_q), run_time=0.8)
        self.wait(0.5)

        # 三个问号占位
        q1 = Text("?", font=FONT, font_size=60, color=COLOR_SEGMENT)
        q1.move_to(UP * 2.5)
        q2 = Text("?", font=FONT, font_size=60, color=COLOR_RAY)
        q2.move_to(UP * 0.5)
        q3 = Text("?", font=FONT, font_size=60, color=COLOR_LINE)
        q3.move_to(DOWN * 1.5)
        self.play(
            FadeIn(q1, scale=1.5),
            FadeIn(q2, scale=1.5),
            FadeIn(q3, scale=1.5),
            run_time=0.6,
        )
        self.wait(0.4)

        # ---- 揭示: 线段 ----
        seg_name = Text("线段", font=FONT, font_size=36, color=COLOR_SEGMENT)
        seg_name.move_to(np.array([-2.5, 2.5, 0.0]))
        seg_demo = Line(
            np.array([-0.5, 2.5, 0.0]),
            np.array([3.5, 2.5, 0.0]),
            color=COLOR_SEGMENT, stroke_width=5,
        )
        seg_d1 = Dot(
            np.array([-0.5, 2.5, 0.0]), color=COLOR_ENDPOINT, radius=0.1,
        )
        seg_d2 = Dot(
            np.array([3.5, 2.5, 0.0]), color=COLOR_ENDPOINT, radius=0.1,
        )
        self.play(
            ReplacementTransform(q1, seg_name),
            Create(seg_demo), FadeIn(seg_d1), FadeIn(seg_d2),
            run_time=0.7,
        )

        # ---- 揭示: 射线 ----
        ray_name = Text("射线", font=FONT, font_size=36, color=COLOR_RAY)
        ray_name.move_to(np.array([-2.5, 0.5, 0.0]))
        ray_demo = Line(
            np.array([-0.5, 0.5, 0.0]),
            np.array([2.8, 0.5, 0.0]),
            color=COLOR_RAY, stroke_width=5,
        )
        ray_dot = Dot(
            np.array([-0.5, 0.5, 0.0]), color=COLOR_ENDPOINT, radius=0.1,
        )
        ray_arr = Arrow(
            np.array([2.8, 0.5, 0.0]),
            np.array([3.8, 0.5, 0.0]),
            color=COLOR_RAY, stroke_width=5,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        self.play(
            ReplacementTransform(q2, ray_name),
            Create(ray_demo), FadeIn(ray_dot), GrowArrow(ray_arr),
            run_time=0.7,
        )

        # ---- 揭示: 直线 ----
        line_name = Text("直线", font=FONT, font_size=36, color=COLOR_LINE)
        line_name.move_to(np.array([-2.5, -1.5, 0.0]))
        line_demo = Line(
            np.array([-0.5, -1.5, 0.0]),
            np.array([2.5, -1.5, 0.0]),
            color=COLOR_LINE, stroke_width=5,
        )
        line_al = Arrow(
            np.array([-0.5, -1.5, 0.0]),
            np.array([-1.5, -1.5, 0.0]),
            color=COLOR_LINE, stroke_width=5,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        line_ar = Arrow(
            np.array([2.5, -1.5, 0.0]),
            np.array([3.5, -1.5, 0.0]),
            color=COLOR_LINE, stroke_width=5,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        self.play(
            ReplacementTransform(q3, line_name),
            Create(line_demo), GrowArrow(line_al), GrowArrow(line_ar),
            run_time=0.7,
        )
        self.wait(1.0)

        # 过渡文字
        transition = Text(
            "让我们逐个认识它们!",
            font=FONT, font_size=28, color=GRAY_A,
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(transition, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(hook_q), FadeOut(transition),
            FadeOut(seg_name), FadeOut(seg_demo),
            FadeOut(seg_d1), FadeOut(seg_d2),
            FadeOut(ray_name), FadeOut(ray_demo),
            FadeOut(ray_dot), FadeOut(ray_arr),
            FadeOut(line_name), FadeOut(line_demo),
            FadeOut(line_al), FadeOut(line_ar),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 线段
    # ------------------------------------------------------------------

    def scene_2_line_segment(self):
        title = self.make_section_title("线段", color=COLOR_SEGMENT)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "有两个端点，长度有限",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ---- 绘制线段 AB ----
        cy = 2.5
        A_pos = np.array([-3.0, cy, 0.0])
        B_pos = np.array([3.0, cy, 0.0])

        seg = Line(A_pos, B_pos, color=COLOR_SEGMENT, stroke_width=6)
        dot_A = self.make_endpoint(A_pos)
        dot_B = self.make_endpoint(B_pos)
        label_A = self.make_label("A", A_pos)
        label_B = self.make_label("B", B_pos)

        self.play(Create(seg), run_time=1.0)
        self.play(
            FadeIn(dot_A, scale=1.5),
            FadeIn(dot_B, scale=1.5),
            run_time=0.5,
        )
        self.play(FadeIn(label_A), FadeIn(label_B), run_time=0.4)

        # ---- 标注两个端点 ----
        ep_arrow_A = Arrow(
            A_pos + UP * 1.0 + LEFT * 0.5,
            A_pos + UP * 0.2,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.2, buff=0.05,
        )
        ep_label_A = Text(
            "端点", font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(A_pos + UP * 1.3 + LEFT * 0.5)

        ep_arrow_B = Arrow(
            B_pos + UP * 1.0 + RIGHT * 0.5,
            B_pos + UP * 0.2,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.2, buff=0.05,
        )
        ep_label_B = Text(
            "端点", font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(B_pos + UP * 1.3 + RIGHT * 0.5)

        self.play(
            Create(ep_arrow_A), FadeIn(ep_label_A),
            Create(ep_arrow_B), FadeIn(ep_label_B),
            run_time=0.7,
        )
        self.wait(0.8)
        self.play(
            FadeOut(ep_arrow_A), FadeOut(ep_label_A),
            FadeOut(ep_arrow_B), FadeOut(ep_label_B),
            run_time=0.3,
        )

        # ---- 尺子度量动画 ----
        ruler_y = cy - 0.6
        ruler_body = Rectangle(
            width=6.0, height=0.35,
            color=COLOR_RULER,
            fill_color=COLOR_RULER, fill_opacity=0.15,
            stroke_width=2,
        ).move_to(np.array([0.0, ruler_y, 0.0]))

        # 尺子刻度
        tick_marks = VGroup()
        tick_labels = VGroup()
        for i in range(7):
            x = -3.0 + i
            tick = Line(
                np.array([x, ruler_y - 0.175, 0.0]),
                np.array([x, ruler_y - 0.175 + 0.18, 0.0]),
                color=COLOR_RULER, stroke_width=2,
            )
            tick_marks.add(tick)
            num = Text(
                str(i), font=FONT, font_size=14, color=COLOR_RULER,
            ).move_to(np.array([x, ruler_y + 0.3, 0.0]))
            tick_labels.add(num)

        ruler_group = VGroup(ruler_body, tick_marks, tick_labels)

        # 尺子从左侧滑入
        ruler_group.shift(LEFT * 8)
        self.play(ruler_group.animate.shift(RIGHT * 8), run_time=1.0)
        self.wait(0.3)

        # 度量结果
        brace = Brace(seg, direction=DOWN, color=COLOR_HL)
        brace.shift(DOWN * 0.6)
        measure_text = VGroup(
            Text("长度 = ", font=FONT, font_size=22, color=COLOR_HL),
            MathTex(r"6", font_size=28, color=COLOR_HL),
            Text(" 厘米", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1)
        measure_text.next_to(brace, DOWN, buff=0.15)

        self.play(FadeIn(brace), run_time=0.4)
        self.play(FadeIn(measure_text), run_time=0.5)

        can_measure = Text(
            "线段可以度量长度!",
            font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(np.array([0.0, cy - 2.5, 0.0]))
        self.play(FadeIn(can_measure, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 尺子滑出
        self.play(ruler_group.animate.shift(RIGHT * 8), run_time=0.6)

        # ---- 记法说明 ----
        self.play(
            FadeOut(brace), FadeOut(measure_text), FadeOut(can_measure),
            run_time=0.3,
        )

        notation = VGroup(
            Text("记作: 线段", font=FONT, font_size=24, color=WHITE),
            MathTex(r"AB", font_size=32, color=COLOR_SEGMENT),
            Text("或线段", font=FONT, font_size=24, color=WHITE),
            MathTex(r"BA", font_size=32, color=COLOR_SEGMENT),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 0.5)
        self.play(FadeIn(notation, shift=UP * 0.2), run_time=0.5)

        # ---- 关键特征卡 ----
        key_card = self._make_key_card(
            items=[
                ("端点数:", "2 个", COLOR_ENDPOINT),
                ("长度:", "有限，可以度量", COLOR_SEGMENT),
                ("延伸:", "不延伸", GRAY_B),
            ],
            y=-2.5,
        )
        self.play(FadeIn(key_card, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清场
        self.clean_scene(
            title, subtitle, seg, dot_A, dot_B,
            label_A, label_B, notation, key_card,
        )

    # ------------------------------------------------------------------
    # Scene 3: 射线
    # ------------------------------------------------------------------

    def scene_3_ray(self):
        title = self.make_section_title("射线", color=COLOR_RAY)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "只有一个端点，向一端无限延伸",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ---- 绘制射线 ----
        cy = 2.5
        O_pos = np.array([-3.0, cy, 0.0])
        body_end = np.array([2.5, cy, 0.0])
        arrow_end = np.array([3.8, cy, 0.0])

        dot_O = self.make_endpoint(O_pos)
        label_O = self.make_label("O", O_pos)

        # 从端点"射出"
        self.play(FadeIn(dot_O, scale=2.0), run_time=0.4)
        self.play(FadeIn(label_O), run_time=0.3)

        ray_body = Line(O_pos, body_end, color=COLOR_RAY, stroke_width=6)
        ray_arrow = Arrow(
            body_end, arrow_end,
            color=COLOR_RAY, stroke_width=6,
            max_tip_length_to_length_ratio=0.2, buff=0,
        )
        self.play(Create(ray_body), run_time=0.8)
        self.play(GrowArrow(ray_arrow), run_time=0.6)

        # 虚线延伸暗示无限
        dashes = VGroup()
        dash_x = arrow_end[0] + 0.15
        for i in range(3):
            d = DashedLine(
                np.array([dash_x + i * 0.3, cy, 0.0]),
                np.array([dash_x + i * 0.3 + 0.15, cy, 0.0]),
                color=COLOR_RAY, stroke_width=4, dash_length=0.1,
            )
            dashes.add(d)
        # 限制在安全区域
        if dashes.get_right()[0] > 4.3:
            dashes.shift(LEFT * (dashes.get_right()[0] - 4.3))
        self.play(FadeIn(dashes, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 标注端点和无限 ----
        ep_label = Text(
            "端点 (起点)", font=FONT, font_size=22, color=COLOR_HL,
        ).next_to(dot_O, UP, buff=0.4)

        inf_label = Text(
            "无限延伸...", font=FONT, font_size=22, color=COLOR_ARROW,
        ).move_to(np.array([3.0, cy + 0.6, 0.0]))

        self.play(FadeIn(ep_label), FadeIn(inf_label), run_time=0.5)
        self.play(
            Indicate(ray_arrow, color=COLOR_ARROW, scale_factor=1.2),
            run_time=0.6,
        )
        self.wait(0.6)

        # ---- 不可度量说明 ----
        self.play(FadeOut(ep_label), FadeOut(inf_label), run_time=0.3)

        no_measure = Text(
            "射线无限长，不可度量",
            font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(UP * 0.5)

        # 尺子图标 + 叉号
        ruler_icon = Rectangle(
            width=2.0, height=0.3,
            color=COLOR_RULER, stroke_width=2,
            fill_color=COLOR_RULER, fill_opacity=0.15,
        ).move_to(DOWN * 0.3)
        cross1 = Line(
            ruler_icon.get_corner(UL), ruler_icon.get_corner(DR),
            color=COLOR_ENDPOINT, stroke_width=4,
        )
        cross2 = Line(
            ruler_icon.get_corner(UR), ruler_icon.get_corner(DL),
            color=COLOR_ENDPOINT, stroke_width=4,
        )

        self.play(FadeIn(no_measure), run_time=0.5)
        self.play(FadeIn(ruler_icon), run_time=0.3)
        self.play(Create(cross1), Create(cross2), run_time=0.5)
        self.wait(0.5)
        self.play(
            FadeOut(ruler_icon), FadeOut(cross1), FadeOut(cross2),
            run_time=0.3,
        )

        # ---- 记法 ----
        self.play(FadeOut(no_measure), run_time=0.2)

        # 在射线上标经过点 A
        A_pos = np.array([1.0, cy, 0.0])
        dot_A = Dot(A_pos, color=WHITE, radius=0.08)
        label_A_ray = self.make_label("A", A_pos, font_size=26)
        self.play(FadeIn(dot_A), FadeIn(label_A_ray), run_time=0.4)

        notation = VGroup(
            Text("记作: 射线", font=FONT, font_size=24, color=WHITE),
            MathTex(r"OA", font_size=32, color=COLOR_RAY),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 0.3)

        note = Text(
            "(端点写在前面!)",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(notation), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)

        # 生活例子
        life_eg = Text(
            "例: 手电筒射出的光线",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(life_eg, shift=UP * 0.2), run_time=0.5)

        # ---- 关键特征卡 ----
        key_card = self._make_key_card(
            items=[
                ("端点数:", "1 个 (起点)", COLOR_ENDPOINT),
                ("长度:", "无限，不可度量", COLOR_RAY),
                ("延伸:", "向一端无限延伸", COLOR_ARROW),
            ],
            y=-4.5,
        )
        self.play(FadeIn(key_card, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清场
        self.clean_scene(
            title, subtitle,
            ray_body, ray_arrow, dashes,
            dot_O, label_O, dot_A, label_A_ray,
            notation, note, life_eg, key_card,
        )

    # ------------------------------------------------------------------
    # Scene 4: 直线
    # ------------------------------------------------------------------

    def scene_4_line(self):
        title = self.make_section_title("直线", color=COLOR_LINE)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "没有端点，向两端无限延伸",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ---- 绘制直线 ----
        cy = 2.5
        body_left = np.array([-2.5, cy, 0.0])
        body_right = np.array([2.5, cy, 0.0])
        arr_left_end = np.array([-3.8, cy, 0.0])
        arr_right_end = np.array([3.8, cy, 0.0])

        line_body = Line(
            body_left, body_right, color=COLOR_LINE, stroke_width=6,
        )
        arr_left = Arrow(
            body_left, arr_left_end,
            color=COLOR_LINE, stroke_width=6,
            max_tip_length_to_length_ratio=0.2, buff=0,
        )
        arr_right = Arrow(
            body_right, arr_right_end,
            color=COLOR_LINE, stroke_width=6,
            max_tip_length_to_length_ratio=0.2, buff=0,
        )

        self.play(Create(line_body), run_time=0.8)
        self.play(GrowArrow(arr_left), GrowArrow(arr_right), run_time=0.7)

        # 两侧虚线暗示无限
        dash_l = DashedLine(
            arr_left_end + LEFT * 0.1,
            np.array([-4.3, cy, 0.0]),
            color=COLOR_LINE, stroke_width=3, dash_length=0.1,
        )
        dash_r = DashedLine(
            arr_right_end + RIGHT * 0.1,
            np.array([4.3, cy, 0.0]),
            color=COLOR_LINE, stroke_width=3, dash_length=0.1,
        )
        self.play(FadeIn(dash_l), FadeIn(dash_r), run_time=0.4)

        # 标注"无限延伸"
        left_inf = Text(
            "...无限", font=FONT, font_size=18, color=COLOR_ARROW,
        ).move_to(np.array([-3.5, cy + 0.6, 0.0]))
        right_inf = Text(
            "无限...", font=FONT, font_size=18, color=COLOR_ARROW,
        ).move_to(np.array([3.5, cy + 0.6, 0.0]))
        self.play(FadeIn(left_inf), FadeIn(right_inf), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(left_inf), FadeOut(right_inf), run_time=0.3)

        # ---- 强调: 没有端点 ----
        no_ep = Text(
            "没有端点!", font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(UP * 0.8)
        self.play(FadeIn(no_ep), run_time=0.5)

        # 虚线圈标出"无端点"
        ghost_l = DashedVMobject(
            Circle(radius=0.2, color=GRAY_B).move_to(arr_left_end),
            num_dashes=8,
        )
        ghost_r = DashedVMobject(
            Circle(radius=0.2, color=GRAY_B).move_to(arr_right_end),
            num_dashes=8,
        )
        self.play(FadeIn(ghost_l), FadeIn(ghost_r), run_time=0.5)
        self.wait(0.5)
        self.play(
            FadeOut(ghost_l), FadeOut(ghost_r), FadeOut(no_ep),
            run_time=0.3,
        )

        # ---- 直线上标两个点 ----
        A_pos = np.array([-1.0, cy, 0.0])
        B_pos = np.array([1.5, cy, 0.0])
        dot_A = Dot(A_pos, color=WHITE, radius=0.08)
        dot_B = Dot(B_pos, color=WHITE, radius=0.08)
        label_A = self.make_label("A", A_pos, font_size=26)
        label_B = self.make_label("B", B_pos, font_size=26)
        self.play(
            FadeIn(dot_A), FadeIn(dot_B),
            FadeIn(label_A), FadeIn(label_B),
            run_time=0.5,
        )

        # 记法
        notation = VGroup(
            Text("记作: 直线", font=FONT, font_size=24, color=WHITE),
            MathTex(r"AB", font_size=32, color=COLOR_LINE),
            Text("或直线", font=FONT, font_size=24, color=WHITE),
            MathTex(r"BA", font_size=32, color=COLOR_LINE),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 0.2)

        note2 = Text(
            "(也可用小写字母 l 表示)",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 0.9)

        self.play(FadeIn(notation), run_time=0.5)
        self.play(FadeIn(note2), run_time=0.4)

        # ---- 关键特征卡 ----
        key_card = self._make_key_card(
            items=[
                ("端点数:", "0 个", GRAY_B),
                ("长度:", "无限，不可度量", COLOR_LINE),
                ("延伸:", "向两端无限延伸", COLOR_ARROW),
            ],
            y=-3.0,
        )
        self.play(FadeIn(key_card, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清场
        self.clean_scene(
            title, subtitle,
            line_body, arr_left, arr_right, dash_l, dash_r,
            dot_A, dot_B, label_A, label_B,
            notation, note2, key_card,
        )

    # ------------------------------------------------------------------
    # Scene 5: 对比表格
    # ------------------------------------------------------------------

    def scene_5_comparison_table(self):
        title = Text(
            "三者对比", font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 表格参数
        col_x = [-2.8, -0.8, 1.0, 3.0]
        row_y = [4.8, 3.5, 2.0, 0.5]

        # ---- 表头 ----
        headers = ["", "端点", "长度", "延伸"]
        header_texts = VGroup()
        for i, h in enumerate(headers):
            if h:
                t = Text(h, font=FONT, font_size=22, color=COLOR_HL)
                t.move_to(np.array([col_x[i], row_y[0], 0.0]))
                header_texts.add(t)
        self.play(FadeIn(header_texts), run_time=0.5)

        # 表头下分隔线
        header_line = Line(
            np.array([-3.8, row_y[0] - 0.5, 0.0]),
            np.array([4.0, row_y[0] - 0.5, 0.0]),
            color=GRAY_D, stroke_width=2,
        )
        self.play(Create(header_line), run_time=0.3)

        # ---- 行 1: 线段 ----
        row1 = self._make_table_row(
            name="线段", name_color=COLOR_SEGMENT,
            values=["2 个", "有限", "不延伸"],
            val_colors=[COLOR_ENDPOINT, COLOR_SEGMENT, GRAY_B],
            col_x=col_x, y=row_y[1], icon_type="segment",
        )
        self.play(FadeIn(row1, shift=RIGHT * 0.3), run_time=0.6)

        div1 = Line(
            np.array([-3.8, row_y[1] - 0.6, 0.0]),
            np.array([4.0, row_y[1] - 0.6, 0.0]),
            color=GRAY_D, stroke_width=1,
        )
        self.play(Create(div1), run_time=0.2)

        # ---- 行 2: 射线 ----
        row2 = self._make_table_row(
            name="射线", name_color=COLOR_RAY,
            values=["1 个", "无限", "一端"],
            val_colors=[COLOR_ENDPOINT, COLOR_RAY, COLOR_ARROW],
            col_x=col_x, y=row_y[2], icon_type="ray",
        )
        self.play(FadeIn(row2, shift=RIGHT * 0.3), run_time=0.6)

        div2 = Line(
            np.array([-3.8, row_y[2] - 0.6, 0.0]),
            np.array([4.0, row_y[2] - 0.6, 0.0]),
            color=GRAY_D, stroke_width=1,
        )
        self.play(Create(div2), run_time=0.2)

        # ---- 行 3: 直线 ----
        row3 = self._make_table_row(
            name="直线", name_color=COLOR_LINE,
            values=["0 个", "无限", "两端"],
            val_colors=[GRAY_B, COLOR_LINE, COLOR_ARROW],
            col_x=col_x, y=row_y[3], icon_type="line",
        )
        self.play(FadeIn(row3, shift=RIGHT * 0.3), run_time=0.6)

        self.wait(1.5)

        # ---- 关键结论 ----
        conclusion = VGroup(
            Text(
                "射线和直线都是无限延伸的",
                font=FONT, font_size=24, color=COLOR_HL,
            ),
            Text(
                "只有线段可以度量长度",
                font=FONT, font_size=24, color=COLOR_HL,
            ),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)

        box = SurroundingRectangle(
            conclusion, color=COLOR_HL,
            buff=0.3, corner_radius=0.15, stroke_width=2,
        )
        self.play(FadeIn(conclusion), Create(box), run_time=0.7)
        self.wait(2.5)

        # 清场
        all_table = VGroup(
            header_texts, header_line,
            row1, div1, row2, div2, row3,
            conclusion, box,
        )
        self.clean_scene(title, all_table)

    # ------------------------------------------------------------------
    # Scene 6: 关系演示 (线段 -> 射线 -> 直线)
    # ------------------------------------------------------------------

    def scene_6_relationship(self):
        title = Text(
            "三者的关系", font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        hint = Text(
            "线段延伸可以变成射线和直线",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 5.5)
        self.play(FadeIn(hint), run_time=0.4)

        # ---- 第一步: 线段 ----
        cy = 3.0
        A_pos = np.array([-2.0, cy, 0.0])
        B_pos = np.array([2.0, cy, 0.0])

        seg = Line(A_pos, B_pos, color=COLOR_SEGMENT, stroke_width=6)
        dot_A = self.make_endpoint(A_pos)
        dot_B = self.make_endpoint(B_pos)
        label_seg = Text(
            "线段", font=FONT, font_size=28, color=COLOR_SEGMENT,
        ).move_to(np.array([0.0, cy + 0.6, 0.0]))

        self.play(
            Create(seg), FadeIn(dot_A), FadeIn(dot_B),
            run_time=0.8,
        )
        self.play(FadeIn(label_seg), run_time=0.4)
        self.wait(0.8)

        # ---- 第二步: 线段 -> 射线 ----
        step2_text = Text(
            "向右延伸一端...",
            font=FONT, font_size=22, color=COLOR_RAY,
        ).move_to(np.array([0.0, cy - 0.8, 0.0]))
        self.play(FadeIn(step2_text), run_time=0.4)

        # B 端点消失, 向右延伸成射线
        arrow_end_r = np.array([3.8, cy, 0.0])
        extension_r = Line(
            B_pos, arrow_end_r, color=COLOR_RAY, stroke_width=6,
        )
        ray_tip_r = Arrow(
            np.array([3.2, cy, 0.0]), arrow_end_r,
            color=COLOR_RAY, stroke_width=6,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )

        self.play(
            FadeOut(dot_B),
            seg.animate.set_color(COLOR_RAY),
            run_time=0.5,
        )
        self.play(Create(extension_r), run_time=0.6)
        self.play(GrowArrow(ray_tip_r), run_time=0.4)

        label_ray = Text(
            "射线", font=FONT, font_size=28, color=COLOR_RAY,
        ).move_to(np.array([0.0, cy + 0.6, 0.0]))
        self.play(
            ReplacementTransform(label_seg, label_ray),
            FadeOut(step2_text),
            run_time=0.5,
        )
        self.wait(0.8)

        # ---- 第三步: 射线 -> 直线 ----
        step3_text = Text(
            "再向左也延伸...",
            font=FONT, font_size=22, color=COLOR_LINE,
        ).move_to(np.array([0.0, cy - 0.8, 0.0]))
        self.play(FadeIn(step3_text), run_time=0.4)

        # A 端点也消失, 向左延伸
        arrow_end_l = np.array([-3.8, cy, 0.0])
        extension_l = Line(
            A_pos, arrow_end_l, color=COLOR_LINE, stroke_width=6,
        )
        left_tip = Arrow(
            np.array([-3.2, cy, 0.0]), arrow_end_l,
            color=COLOR_LINE, stroke_width=6,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )

        self.play(
            FadeOut(dot_A),
            seg.animate.set_color(COLOR_LINE),
            extension_r.animate.set_color(COLOR_LINE),
            ray_tip_r.animate.set_color(COLOR_LINE),
            run_time=0.5,
        )
        self.play(Create(extension_l), run_time=0.6)
        self.play(GrowArrow(left_tip), run_time=0.4)

        label_line = Text(
            "直线", font=FONT, font_size=28, color=COLOR_LINE,
        ).move_to(np.array([0.0, cy + 0.6, 0.0]))
        self.play(
            ReplacementTransform(label_ray, label_line),
            FadeOut(step3_text),
            run_time=0.5,
        )
        self.wait(1.0)

        # ---- 总结图解: 三行对照 ----
        summary_data = [
            (0.5,  "线段", COLOR_SEGMENT, "有两个端点"),
            (-1.5, "射线", COLOR_RAY,     "去掉一个端点, 向一端延伸"),
            (-3.5, "直线", COLOR_LINE,    "去掉两个端点, 向两端延伸"),
        ]
        summary_groups = VGroup()
        for sy, name, col, desc in summary_data:
            n = Text(name, font=FONT, font_size=24, color=col)
            n.move_to(np.array([-3.0, sy, 0.0]))
            d = Text(desc, font=FONT, font_size=20, color=GRAY_A)
            d.move_to(np.array([1.0, sy, 0.0]))
            summary_groups.add(VGroup(n, d))

        # 箭头连接
        arrow_1_2 = Arrow(
            np.array([-3.0, 0.5 - 0.5, 0.0]),
            np.array([-3.0, -1.5 + 0.5, 0.0]),
            color=GRAY_B, stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        )
        arrow_2_3 = Arrow(
            np.array([-3.0, -1.5 - 0.5, 0.0]),
            np.array([-3.0, -3.5 + 0.5, 0.0]),
            color=GRAY_B, stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(
            FadeIn(summary_groups[0], shift=RIGHT * 0.3),
            run_time=0.5,
        )
        self.play(GrowArrow(arrow_1_2), run_time=0.3)
        self.play(
            FadeIn(summary_groups[1], shift=RIGHT * 0.3),
            run_time=0.5,
        )
        self.play(GrowArrow(arrow_2_3), run_time=0.3)
        self.play(
            FadeIn(summary_groups[2], shift=RIGHT * 0.3),
            run_time=0.5,
        )
        self.wait(2.0)

        # 清场
        self.clean_scene(
            title, hint,
            seg, extension_r, ray_tip_r, extension_l, left_tip,
            label_line, summary_groups, arrow_1_2, arrow_2_3,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        # 作者信息
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我，学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 三种线的装饰
        deco_seg = VGroup(
            Line(LEFT * 1.5, RIGHT * 1.5,
                 color=COLOR_SEGMENT, stroke_width=4),
            Dot(LEFT * 1.5, color=COLOR_ENDPOINT, radius=0.08),
            Dot(RIGHT * 1.5, color=COLOR_ENDPOINT, radius=0.08),
        ).move_to(DOWN * 2.8)

        deco_ray = VGroup(
            Line(LEFT * 1.5, RIGHT * 1.0,
                 color=COLOR_RAY, stroke_width=4),
            Arrow(
                RIGHT * 1.0, RIGHT * 1.8,
                color=COLOR_RAY, stroke_width=4,
                max_tip_length_to_length_ratio=0.3, buff=0,
            ),
            Dot(LEFT * 1.5, color=COLOR_ENDPOINT, radius=0.08),
        ).move_to(DOWN * 3.8)

        deco_lin = VGroup(
            Line(LEFT * 1.0, RIGHT * 1.0,
                 color=COLOR_LINE, stroke_width=4),
            Arrow(
                LEFT * 1.0, LEFT * 1.8,
                color=COLOR_LINE, stroke_width=4,
                max_tip_length_to_length_ratio=0.3, buff=0,
            ),
            Arrow(
                RIGHT * 1.0, RIGHT * 1.8,
                color=COLOR_LINE, stroke_width=4,
                max_tip_length_to_length_ratio=0.3, buff=0,
            ),
        ).move_to(DOWN * 4.8)

        self.play(
            FadeIn(deco_seg, scale=0.8),
            FadeIn(deco_ray, scale=0.8),
            FadeIn(deco_lin, scale=0.8),
            run_time=0.7,
        )
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco_seg), FadeOut(deco_ray), FadeOut(deco_lin),
            run_time=1.0,
        )

    # ------------------------------------------------------------------
    # 辅助: 特征卡
    # ------------------------------------------------------------------

    def _make_key_card(self, items, y=-2.5):
        """
        创建关键特征卡片.
        items: list of (label_str, value_str, value_color)
        """
        rows = VGroup()
        for label_str, val_str, val_color in items:
            row = VGroup(
                Text(label_str, font=FONT, font_size=22, color=GRAY_A),
                Text(val_str, font=FONT, font_size=22, color=val_color),
            ).arrange(RIGHT, buff=0.2)
            rows.add(row)
        rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        rows.move_to(np.array([-0.5, y, 0.0]))
        return rows

    # ------------------------------------------------------------------
    # 辅助: 表格行
    # ------------------------------------------------------------------

    def _make_table_row(self, name, name_color, values, val_colors,
                        col_x, y, icon_type="segment"):
        """创建表格的一行 (名称 + 小图标 + 三列数值)"""
        group = VGroup()

        # 名称
        name_text = Text(
            name, font=FONT, font_size=24, color=name_color,
        ).move_to(np.array([col_x[0] - 0.6, y, 0.0]))
        group.add(name_text)

        # 小图标
        icon = self._make_mini_icon(icon_type, name_color)
        icon.move_to(np.array([col_x[0] + 0.5, y, 0.0]))
        group.add(icon)

        # 数值列
        for i, (val, vc) in enumerate(zip(values, val_colors)):
            t = Text(val, font=FONT, font_size=22, color=vc)
            t.move_to(np.array([col_x[i + 1], y, 0.0]))
            group.add(t)

        return group

    def _make_mini_icon(self, icon_type, color):
        """创建小型线段/射线/直线图标"""
        sw = 3
        if icon_type == "segment":
            line = Line(
                LEFT * 0.5, RIGHT * 0.5,
                color=color, stroke_width=sw,
            )
            d1 = Dot(LEFT * 0.5, color=COLOR_ENDPOINT, radius=0.05)
            d2 = Dot(RIGHT * 0.5, color=COLOR_ENDPOINT, radius=0.05)
            return VGroup(line, d1, d2)
        elif icon_type == "ray":
            line = Line(
                LEFT * 0.5, RIGHT * 0.3,
                color=color, stroke_width=sw,
            )
            arr = Arrow(
                RIGHT * 0.3, RIGHT * 0.6,
                color=color, stroke_width=sw,
                max_tip_length_to_length_ratio=0.4, buff=0,
            )
            d = Dot(LEFT * 0.5, color=COLOR_ENDPOINT, radius=0.05)
            return VGroup(line, arr, d)
        else:  # "line"
            line = Line(
                LEFT * 0.3, RIGHT * 0.3,
                color=color, stroke_width=sw,
            )
            al = Arrow(
                LEFT * 0.3, LEFT * 0.6,
                color=color, stroke_width=sw,
                max_tip_length_to_length_ratio=0.4, buff=0,
            )
            ar = Arrow(
                RIGHT * 0.3, RIGHT * 0.6,
                color=color, stroke_width=sw,
                max_tip_length_to_length_ratio=0.4, buff=0,
            )
            return VGroup(line, al, ar)


# 运行命令:
# manim -pql 001_线段射线直线.py LineSegmentRayLesson   # 快速预览
# manim -qm 001_线段射线直线.py LineSegmentRayLesson    # 中等质量
# manim -qh 001_线段射线直线.py LineSegmentRayLesson    # 高质量

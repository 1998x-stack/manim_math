"""
002_认识直角.py — 认识直角 教学动画

知识点: 直角的定义、判断方法、生活中的直角
  - 定义: 三角尺上最大的那个角就是直角
  - 判断: 用三角尺上的直角去比一比（顶点重合, 一条边重合, 看另一条边是否重合）
  - 生活中的直角: 书本的角、黑板的角、门框的角
  - 直角 = 90度, 直角符号: 小方块标记
年级: 二年级上册
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
BG_COLOR = "#1a1a2e"
COLOR_ANGLE = "#3b82f6"         # 蓝色 角
COLOR_RIGHT_ANGLE = "#22c55e"   # 绿色 直角
COLOR_RULER = "#f59e0b"         # 橙色 三角尺
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_CHECK = "#ef4444"         # 红色 对比/检验
COLOR_LIFE = "#a78bfa"          # 紫色 生活实例
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class RightAngleLesson(Scene):
    """
    认识直角教学动画
    场景顺序:
      1. 开场钩子 - 什么是直角?
      2. 认识角 - 角的基本结构
      3. 认识直角 - 三角尺上的直角
      4. 直角 = 90度
      5. 直角的判断方法 - 用三角尺去比
      6. 生活中的直角
      7. 公式总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_what_is_angle()
        self.scene_3_right_angle_on_ruler()
        self.scene_4_right_angle_90()
        self.scene_5_check_method()
        self.scene_6_life_examples()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""

        # ===== 基本角的顶点和射线 =====
        self.angle_vertex = np.array([0.0, 1.5, 0.0])
        self.angle_ray_len = 3.0

        # 直角两条射线方向: 水平向右, 垂直向上
        self.ray_right_dir = np.array([1.0, 0.0, 0.0])
        self.ray_up_dir = np.array([0.0, 1.0, 0.0])

        # 射线端点
        self.ray_right_end = self.angle_vertex + self.angle_ray_len * self.ray_right_dir
        self.ray_up_end = self.angle_vertex + self.angle_ray_len * self.ray_up_dir

        # ===== 三角尺 (直角三角形) =====
        # 直角在左下角, 短边向右, 长边向上
        self.ruler_scale = 1.8
        self.ruler_vertex = np.array([-0.5, 0.5, 0.0])   # 直角顶点
        self.ruler_right = self.ruler_vertex + np.array([2.5, 0.0, 0.0]) * self.ruler_scale
        self.ruler_top = self.ruler_vertex + np.array([0.0, 1.5, 0.0]) * self.ruler_scale

        # ===== 直角标记尺寸 =====
        self.right_angle_size = 0.35

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何关系"""
        # 验证射线方向垂直
        dot_product = np.dot(self.ray_right_dir, self.ray_up_dir)
        assert abs(dot_product) < 1e-10, f"射线方向不垂直: dot={dot_product}"

        # 验证三角尺直角 (两边垂直)
        v1 = self.ruler_right - self.ruler_vertex
        v2 = self.ruler_top - self.ruler_vertex
        dot_ruler = np.dot(v1[:2], v2[:2])
        assert abs(dot_ruler) < 1e-10, f"三角尺直角不正确: dot={dot_ruler}"

        print("Geometry verification passed")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def create_right_angle_mark(self, corner, p1, p2, size=0.35, color=WHITE, stroke_width=2.5):
        """
        创建直角小方块标记
        corner: 直角顶点
        p1, p2: 两条边上的点(决定方向)
        """
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size

        mark = Polygon(
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=stroke_width,
            fill_opacity=0,
        )
        return mark

    def make_author(self):
        """创建作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者标识
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "什么是直角?",
            font=FONT,
            font_size=42,
            color=COLOR_HL,
        ).move_to(UP * 5.0)

        sub_hook = Text(
            "它藏在你身边的每一个角落!",
            font=FONT,
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 4.2)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub_hook, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 快速闪现几个直角物品轮廓
        book = Rectangle(width=2.0, height=2.8, color=COLOR_LIFE, stroke_width=3)
        book.move_to(LEFT * 2.5 + UP * 1.0)

        board = Rectangle(width=3.2, height=2.0, color=COLOR_LIFE, stroke_width=3)
        board.move_to(RIGHT * 2.0 + UP * 1.0)

        door = VGroup(
            Rectangle(width=1.4, height=3.0, color=COLOR_LIFE, stroke_width=3),
        ).move_to(DOWN * 1.5)

        self.play(
            FadeIn(book, scale=0.8),
            FadeIn(board, scale=0.8),
            FadeIn(door, scale=0.8),
            run_time=0.8,
        )
        self.wait(0.6)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(sub_hook),
            FadeOut(book),
            FadeOut(board),
            FadeOut(door),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 认识角
    # ------------------------------------------------------------------

    def scene_2_what_is_angle(self):
        title = Text("先来认识角", font=FONT, font_size=36, color=WHITE).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画角: 顶点 + 两条射线
        vertex = np.array([0.0, 2.0, 0.0])
        ray_a_end = vertex + 3.0 * np.array([np.cos(np.radians(15)), np.sin(np.radians(15)), 0.0])
        ray_b_end = vertex + 3.0 * np.array([np.cos(np.radians(75)), np.sin(np.radians(75)), 0.0])

        ray_a = Line(vertex, ray_a_end, color=COLOR_ANGLE, stroke_width=4)
        ray_b = Line(vertex, ray_b_end, color=COLOR_ANGLE, stroke_width=4)
        dot_v = Dot(vertex, color=WHITE, radius=0.08)

        self.play(Create(ray_a), Create(ray_b), FadeIn(dot_v), run_time=1.0)

        # 标注结构
        label_vertex = Text("顶点", font=FONT, font_size=22, color=COLOR_HL)
        label_vertex.next_to(dot_v, DOWN, buff=0.25)

        label_side_a = Text("边", font=FONT, font_size=22, color=COLOR_HL)
        label_side_a.move_to(ray_a.get_center() + DOWN * 0.4 + RIGHT * 0.2)

        label_side_b = Text("边", font=FONT, font_size=22, color=COLOR_HL)
        label_side_b.move_to(ray_b.get_center() + LEFT * 0.5 + UP * 0.2)

        self.play(FadeIn(label_vertex), FadeIn(label_side_a), FadeIn(label_side_b), run_time=0.6)

        # 角弧
        angle_arc = Angle.from_three_points(
            ray_a_end, vertex, ray_b_end,
            radius=0.6, color=COLOR_HL,
        )
        self.play(Create(angle_arc), run_time=0.5)

        explain = Text(
            "一个顶点引出两条边, 就组成了角",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(ray_a), FadeOut(ray_b),
            FadeOut(dot_v), FadeOut(label_vertex),
            FadeOut(label_side_a), FadeOut(label_side_b),
            FadeOut(angle_arc), FadeOut(explain),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 三角尺上的直角
    # ------------------------------------------------------------------

    def scene_3_right_angle_on_ruler(self):
        title = Text("三角尺上的直角", font=FONT, font_size=36, color=COLOR_RIGHT_ANGLE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画三角尺
        rv = np.array([-1.0, 0.5, 0.0])        # 直角顶点
        rr = rv + np.array([4.0, 0.0, 0.0])    # 右端
        rt = rv + np.array([0.0, 3.0, 0.0])    # 上端

        ruler = Polygon(
            rv, rr, rt,
            color=COLOR_RULER,
            stroke_width=4,
            fill_color=COLOR_RULER,
            fill_opacity=0.15,
        )

        self.play(Create(ruler), run_time=1.0)

        # 标注三个角
        # 直角 (最大角)
        right_mark = self.create_right_angle_mark(
            rv, rr, rt, size=0.35, color=COLOR_RIGHT_ANGLE, stroke_width=3,
        )

        label_right = Text("直角", font=FONT, font_size=24, color=COLOR_RIGHT_ANGLE)
        label_right.next_to(rv, DOWN + LEFT, buff=0.3)

        arrow_to_right = Arrow(
            label_right.get_right() + RIGHT * 0.1,
            rv + DOWN * 0.1 + LEFT * 0.1,
            color=COLOR_RIGHT_ANGLE,
            stroke_width=2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15,
        )

        self.play(Create(right_mark), run_time=0.6)
        self.play(FadeIn(label_right), Create(arrow_to_right), run_time=0.5)

        explain_1 = Text(
            "三角尺上最大的那个角",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 3.0)

        explain_2 = Text(
            "就是直角!",
            font=FONT, font_size=28, color=COLOR_RIGHT_ANGLE,
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(explain_1), run_time=0.5)
        self.play(FadeIn(explain_2), run_time=0.5)

        # 高亮闪烁直角标记
        self.play(
            Indicate(right_mark, color=COLOR_HL, scale_factor=1.3),
            run_time=0.8,
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(ruler), FadeOut(right_mark),
            FadeOut(label_right), FadeOut(arrow_to_right),
            FadeOut(explain_1), FadeOut(explain_2),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 直角 = 90度
    # ------------------------------------------------------------------

    def scene_4_right_angle_90(self):
        title = Text("直角有多大?", font=FONT, font_size=36, color=WHITE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画一个直角
        vertex = np.array([0.0, 2.0, 0.0])
        ray_h_end = vertex + 3.5 * RIGHT
        ray_v_end = vertex + 3.5 * UP

        ray_h = Line(vertex, ray_h_end, color=COLOR_RIGHT_ANGLE, stroke_width=4)
        ray_v = Line(vertex, ray_v_end, color=COLOR_RIGHT_ANGLE, stroke_width=4)
        dot_v = Dot(vertex, color=WHITE, radius=0.08)

        self.play(Create(ray_h), Create(ray_v), FadeIn(dot_v), run_time=0.8)

        # 直角标记
        right_mark = self.create_right_angle_mark(
            vertex, ray_h_end, ray_v_end,
            size=0.4, color=COLOR_RIGHT_ANGLE, stroke_width=3,
        )
        self.play(Create(right_mark), run_time=0.5)

        # 角弧和 90 度标注
        angle_arc = Angle.from_three_points(
            ray_h_end, vertex, ray_v_end,
            radius=0.8, color=COLOR_HL,
        )
        self.play(Create(angle_arc), run_time=0.5)

        degree_label = MathTex(r"90^\circ", font_size=36, color=COLOR_HL)
        degree_label.move_to(vertex + np.array([0.7, 0.7, 0.0]))

        self.play(Write(degree_label), run_time=0.6)

        # 公式
        formula_group = VGroup(
            Text("直角", font=FONT, font_size=30, color=WHITE),
            MathTex(r"= 90^\circ", font_size=36, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        self.play(FadeIn(formula_group, shift=UP * 0.3), run_time=0.6)

        # 直角符号说明
        symbol_explain = VGroup(
            Text("直角用小方块", font=FONT, font_size=22, color=GRAY_A),
            Text("来标记", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.2)

        symbol_demo = self.create_right_angle_mark(
            np.array([0.0, -5.3, 0.0]),
            np.array([0.5, -5.3, 0.0]),
            np.array([0.0, -4.8, 0.0]),
            size=0.25, color=COLOR_RIGHT_ANGLE, stroke_width=3,
        )

        self.play(FadeIn(symbol_explain), Create(symbol_demo), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(ray_h), FadeOut(ray_v),
            FadeOut(dot_v), FadeOut(right_mark), FadeOut(angle_arc),
            FadeOut(degree_label), FadeOut(formula_group),
            FadeOut(symbol_explain), FadeOut(symbol_demo),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 判断直角的方法
    # ------------------------------------------------------------------

    def scene_5_check_method(self):
        title = Text("怎么判断直角?", font=FONT, font_size=36, color=WHITE)
        title.move_to(UP * 5.5)

        subtitle = Text(
            "用三角尺的直角去比一比",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.8)

        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 被测量的角 (一个直角)
        test_vertex = np.array([-1.5, 1.5, 0.0])
        test_ray_h = test_vertex + 3.0 * RIGHT
        test_ray_v = test_vertex + 3.0 * UP

        test_line_h = Line(test_vertex, test_ray_h, color=WHITE, stroke_width=4)
        test_line_v = Line(test_vertex, test_ray_v, color=WHITE, stroke_width=4)
        test_dot = Dot(test_vertex, color=WHITE, radius=0.08)

        question_mark = MathTex(r"?", font_size=48, color=COLOR_HL)
        question_mark.move_to(test_vertex + np.array([0.6, 0.6, 0.0]))

        self.play(
            Create(test_line_h), Create(test_line_v),
            FadeIn(test_dot), Write(question_mark),
            run_time=0.8,
        )

        step1_text = Text(
            "第一步: 顶点重合",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(step1_text), run_time=0.4)

        # 三角尺出现在右侧
        ruler_v = np.array([3.0, -1.0, 0.0])
        ruler_r = ruler_v + np.array([2.0, 0.0, 0.0])
        ruler_t = ruler_v + np.array([0.0, 1.5, 0.0])

        ruler = Polygon(
            ruler_v, ruler_r, ruler_t,
            color=COLOR_RULER,
            stroke_width=3,
            fill_color=COLOR_RULER,
            fill_opacity=0.2,
        )

        ruler_mark = self.create_right_angle_mark(
            ruler_v, ruler_r, ruler_t,
            size=0.25, color=COLOR_RULER, stroke_width=2,
        )
        ruler_group = VGroup(ruler, ruler_mark)

        self.play(FadeIn(ruler_group, shift=LEFT * 0.5), run_time=0.6)
        self.wait(0.5)

        # 移动三角尺, 使直角顶点与被测角顶点重合
        shift_to_test = test_vertex - ruler_v
        self.play(
            ruler_group.animate.shift(shift_to_test),
            run_time=1.2,
            rate_func=smooth,
        )

        # 更新步骤文字
        step2_text = Text(
            "第二步: 一条边重合",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 3.0)
        self.play(
            ReplacementTransform(step1_text, step2_text),
            run_time=0.4,
        )

        # 旋转三角尺使底边与水平射线重合
        # 当前三角尺底边方向 = ruler_r - ruler_v = (2, 0, 0) 已经水平
        # 无需旋转, 但添加一条高亮线表示对齐
        align_line = Line(
            test_vertex, test_vertex + 2.0 * RIGHT,
            color=COLOR_HL, stroke_width=6, stroke_opacity=0.5,
        )
        self.play(Create(align_line), run_time=0.4)
        self.wait(0.5)

        # 第三步
        step3_text = Text(
            "第三步: 看另一条边是否重合",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 3.0)
        self.play(
            ReplacementTransform(step2_text, step3_text),
            run_time=0.4,
        )

        # 高亮竖直边对齐
        align_line_v = Line(
            test_vertex, test_vertex + 1.5 * UP,
            color=COLOR_HL, stroke_width=6, stroke_opacity=0.5,
        )
        self.play(Create(align_line_v), run_time=0.4)
        self.wait(0.5)

        # 结论: 重合! 是直角!
        self.play(FadeOut(question_mark), run_time=0.3)

        check_mark = MathTex(r"\checkmark", font_size=56, color=COLOR_RIGHT_ANGLE)
        check_mark.move_to(test_vertex + np.array([0.6, 0.6, 0.0]))

        result_text = Text(
            "完全重合, 是直角!",
            font=FONT, font_size=28, color=COLOR_RIGHT_ANGLE,
        ).move_to(DOWN * 4.5)

        right_mark = self.create_right_angle_mark(
            test_vertex, test_ray_h, test_ray_v,
            size=0.35, color=COLOR_RIGHT_ANGLE, stroke_width=3,
        )

        self.play(
            Write(check_mark),
            FadeIn(result_text, shift=UP * 0.2),
            Create(right_mark),
            run_time=0.8,
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(test_line_h), FadeOut(test_line_v),
            FadeOut(test_dot), FadeOut(ruler_group),
            FadeOut(align_line), FadeOut(align_line_v),
            FadeOut(check_mark), FadeOut(step3_text),
            FadeOut(result_text), FadeOut(right_mark),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 生活中的直角
    # ------------------------------------------------------------------

    def scene_6_life_examples(self):
        title = Text("生活中的直角", font=FONT, font_size=36, color=COLOR_LIFE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        examples = []

        # --- 例1: 书本 ---
        book_center = np.array([-2.5, 3.0, 0.0])
        book = Rectangle(
            width=2.0, height=2.8,
            color=COLOR_LIFE, stroke_width=3,
            fill_color=COLOR_LIFE, fill_opacity=0.1,
        ).move_to(book_center)

        book_corner = book.get_corner(UL)
        book_mark = self.create_right_angle_mark(
            book_corner,
            book_corner + RIGHT * 0.5,
            book_corner + DOWN * 0.5,
            size=0.2, color=COLOR_RIGHT_ANGLE, stroke_width=2.5,
        )
        book_label = Text("书本", font=FONT, font_size=22, color=WHITE)
        book_label.next_to(book, DOWN, buff=0.3)

        self.play(FadeIn(book, scale=0.8), run_time=0.5)
        self.play(Create(book_mark), FadeIn(book_label), run_time=0.5)
        examples.extend([book, book_mark, book_label])

        # --- 例2: 黑板 ---
        board_center = np.array([2.0, 3.0, 0.0])
        board = Rectangle(
            width=2.8, height=1.8,
            color=COLOR_LIFE, stroke_width=3,
            fill_color=COLOR_LIFE, fill_opacity=0.1,
        ).move_to(board_center)

        board_corner = board.get_corner(UR)
        board_mark = self.create_right_angle_mark(
            board_corner,
            board_corner + LEFT * 0.5,
            board_corner + DOWN * 0.5,
            size=0.2, color=COLOR_RIGHT_ANGLE, stroke_width=2.5,
        )
        board_label = Text("黑板", font=FONT, font_size=22, color=WHITE)
        board_label.next_to(board, DOWN, buff=0.3)

        self.play(FadeIn(board, scale=0.8), run_time=0.5)
        self.play(Create(board_mark), FadeIn(board_label), run_time=0.5)
        examples.extend([board, board_mark, board_label])

        # --- 例3: 门框 ---
        door_bl = np.array([-1.0, -1.5, 0.0])
        door_br = door_bl + np.array([2.0, 0.0, 0.0])
        door_tl = door_bl + np.array([0.0, 3.5, 0.0])
        door_tr = door_bl + np.array([2.0, 3.5, 0.0])

        door_frame = VGroup(
            Line(door_bl, door_tl, color=COLOR_LIFE, stroke_width=3),
            Line(door_tl, door_tr, color=COLOR_LIFE, stroke_width=3),
            Line(door_tr, door_br, color=COLOR_LIFE, stroke_width=3),
        ).shift(DOWN * 1.0)

        # 重算因为shift
        door_tl_shifted = door_tl + DOWN * 1.0
        door_tr_shifted = door_tr + DOWN * 1.0
        door_bl_shifted = door_bl + DOWN * 1.0
        door_br_shifted = door_br + DOWN * 1.0

        door_mark_tl = self.create_right_angle_mark(
            door_tl_shifted,
            door_tl_shifted + DOWN * 0.5,
            door_tl_shifted + RIGHT * 0.5,
            size=0.2, color=COLOR_RIGHT_ANGLE, stroke_width=2.5,
        )
        door_mark_tr = self.create_right_angle_mark(
            door_tr_shifted,
            door_tr_shifted + LEFT * 0.5,
            door_tr_shifted + DOWN * 0.5,
            size=0.2, color=COLOR_RIGHT_ANGLE, stroke_width=2.5,
        )

        door_label = Text("门框", font=FONT, font_size=22, color=WHITE)
        door_label.next_to(door_frame, DOWN, buff=0.3)

        self.play(Create(door_frame), run_time=0.8)
        self.play(
            Create(door_mark_tl), Create(door_mark_tr),
            FadeIn(door_label),
            run_time=0.5,
        )
        examples.extend([door_frame, door_mark_tl, door_mark_tr, door_label])

        # 总结文字
        life_summary = Text(
            "直角无处不在!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(life_summary, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            *[FadeOut(e) for e in examples],
            FadeOut(life_summary),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = Text("知识总结", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 总结卡片
        card_bg = RoundedRectangle(
            width=7.5, height=9.0,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.05,
        ).move_to(UP * 0.3)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 条目1
        item1_title = Text("1. 什么是直角", font=FONT, font_size=26, color=COLOR_RIGHT_ANGLE)
        item1_body = Text(
            "三角尺上最大的角就是直角",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item1 = VGroup(item1_title, item1_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item1.move_to(UP * 3.2 + LEFT * 0.3)

        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # 条目2
        item2_title = Text("2. 直角的大小", font=FONT, font_size=26, color=COLOR_RIGHT_ANGLE)
        item2_body = VGroup(
            Text("直角", font=FONT, font_size=22, color=WHITE),
            MathTex(r"= 90^\circ", font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.15)
        item2 = VGroup(item2_title, item2_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item2.move_to(UP * 1.5 + LEFT * 0.3)

        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # 条目3
        item3_title = Text("3. 直角的标记", font=FONT, font_size=26, color=COLOR_RIGHT_ANGLE)

        # 小方块演示
        demo_vertex = np.array([-1.5, -0.2, 0.0])
        demo_h = Line(demo_vertex, demo_vertex + 1.5 * RIGHT, color=WHITE, stroke_width=3)
        demo_v = Line(demo_vertex, demo_vertex + 1.5 * UP, color=WHITE, stroke_width=3)
        demo_mark = self.create_right_angle_mark(
            demo_vertex,
            demo_vertex + RIGHT,
            demo_vertex + UP,
            size=0.25, color=COLOR_RIGHT_ANGLE, stroke_width=3,
        )
        demo_group = VGroup(demo_h, demo_v, demo_mark)

        item3 = VGroup(item3_title, demo_group).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        item3.move_to(DOWN * 0.3 + LEFT * 0.3)

        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        # 条目4
        item4_title = Text("4. 判断方法", font=FONT, font_size=26, color=COLOR_RIGHT_ANGLE)
        item4_body = VGroup(
            Text("用三角尺的直角去比一比", font=FONT, font_size=20, color=GRAY_A),
            Text("顶点重合 -> 边重合 -> 判断", font=FONT, font_size=18, color=GRAY_B),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        item4 = VGroup(item4_title, item4_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item4.move_to(DOWN * 2.2 + LEFT * 0.3)

        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(item2),
            FadeOut(item3), FadeOut(item4),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        # 放大作者信息
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.0)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 直角装饰
        decorations = VGroup()
        for i in range(4):
            angle_val = i * PI / 2
            pos = DOWN * 3.5 + 2.0 * np.array([np.cos(angle_val), np.sin(angle_val), 0.0])
            corner_v = pos
            corner_h = pos + 0.4 * RIGHT
            corner_u = pos + 0.4 * UP
            dec_mark = self.create_right_angle_mark(
                corner_v, corner_h, corner_u,
                size=0.2, color=COLOR_RIGHT_ANGLE, stroke_width=2,
            )
            decorations.add(dec_mark)

        self.play(*[FadeIn(d, scale=0.5) for d in decorations], run_time=0.6)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(decorations),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_认识直角.py RightAngleLesson   # 快速预览
# manim -qm 002_认识直角.py RightAngleLesson    # 中等质量
# manim -qh 002_认识直角.py RightAngleLesson    # 高质量

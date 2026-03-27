"""
001_线段射线直线.py — 线段、射线、直线 教学动画

知识点:
  - 线段: 有两个端点，可以度量长度
  - 射线: 只有一个端点，向一端无限延伸，不可度量
  - 直线: 没有端点，向两端无限延伸，不可度量
  - 三者的区别和联系

年级: 四年级第一学期
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
COLOR_SEGMENT = "#3b82f6"      # 蓝色 - 线段
COLOR_RAY = "#22c55e"          # 绿色 - 射线
COLOR_LINE = "#f59e0b"         # 橙色 - 直线
COLOR_ENDPOINT = "#ef4444"     # 红色 - 端点
COLOR_HL = "#fbbf24"           # 黄色高亮
COLOR_AUTHOR = "#6b7280"       # 灰色作者信息
COLOR_ARROW = "#a78bfa"        # 紫色 - 箭头/无限延伸
FONT = "Hiragino Sans GB"


class LineSegmentRayLesson(Scene):
    """
    线段、射线、直线教学动画

    场景顺序:
      1. 开场钩子
      2. 点的概念 (基础)
      3. 线段 - 有两个端点
      4. 射线 - 只有一个端点
      5. 直线 - 没有端点
      6. 三者对比
      7. 知识总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_line_segment()
        self.scene_3_ray()
        self.scene_4_line()
        self.scene_5_comparison()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""

        # ===== 线段的两个端点 =====
        self.seg_A = np.array([-3.0, 0.0, 0.0])
        self.seg_B = np.array([3.0, 0.0, 0.0])

        # ===== 射线的端点和方向 =====
        self.ray_start = np.array([-2.5, 0.0, 0.0])
        self.ray_dir = np.array([1.0, 0.0, 0.0])   # 向右
        self.ray_end_visible = np.array([4.0, 0.0, 0.0])  # 可见范围内的终点

        # ===== 直线两端延伸 =====
        self.line_left = np.array([-4.0, 0.0, 0.0])
        self.line_right = np.array([4.0, 0.0, 0.0])

        # ===== 对比区域 (三排) =====
        self.row_y = [2.5, 0.0, -2.5]   # 三行的 y 坐标 (线段, 射线, 直线)
        self.compare_x_left = -3.5
        self.compare_x_right = 3.5

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何关系"""
        # 验证线段端点在同一水平线
        assert abs(self.seg_A[1] - self.seg_B[1]) < 1e-10, "线段端点不在同一水平线"

        # 验证射线方向是单位向量
        dir_norm = np.linalg.norm(self.ray_dir)
        assert abs(dir_norm - 1.0) < 1e-10, f"射线方向不是单位向量: {dir_norm}"

        # 验证对比区域 y 坐标数量
        assert len(self.row_y) == 3, "对比行坐标数量应为3"

        print("Geometry verification passed")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_endpoint_dot(self, pos, color=COLOR_ENDPOINT, radius=0.1):
        """创建端点圆点"""
        return Dot(pos, color=color, radius=radius)

    def make_infinite_arrow(self, start, direction, length=1.2, color=COLOR_ARROW):
        """
        创建无限延伸箭头 (用于射线/直线的无限方向指示)
        start: 箭头起始点
        direction: 方向单位向量
        """
        end = start + direction * length
        return Arrow(
            start, end,
            color=color,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )

    def make_dashed_extension(self, start, end, color=GRAY_B):
        """创建虚线延伸段 (表示无限)"""
        return DashedLine(
            start, end,
            color=color,
            dash_length=0.15,
            stroke_width=3,
        )

    def make_section_title(self, text_str, color=WHITE, y=5.5):
        """创建场景标题"""
        return Text(text_str, font=FONT, font_size=36, color=color).move_to(UP * y)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者标识
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "线段、射线、直线",
            font=FONT,
            font_size=42,
            color=COLOR_HL,
        ).move_to(UP * 5.2)

        sub_hook = Text(
            "它们有什么不同?",
            font=FONT,
            font_size=28,
            color=GRAY_A,
        ).move_to(UP * 4.3)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub_hook, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 快速展示三种线
        # 线段 (蓝色, 有两个端点)
        seg_demo = Line(
            np.array([-3.0, 2.0, 0.0]),
            np.array([3.0, 2.0, 0.0]),
            color=COLOR_SEGMENT, stroke_width=5,
        )
        dot_l = Dot(np.array([-3.0, 2.0, 0.0]), color=COLOR_ENDPOINT, radius=0.1)
        dot_r = Dot(np.array([3.0, 2.0, 0.0]), color=COLOR_ENDPOINT, radius=0.1)

        # 射线 (绿色, 一端箭头)
        ray_demo = Line(
            np.array([-3.0, 0.2, 0.0]),
            np.array([2.5, 0.2, 0.0]),
            color=COLOR_RAY, stroke_width=5,
        )
        ray_dot = Dot(np.array([-3.0, 0.2, 0.0]), color=COLOR_ENDPOINT, radius=0.1)
        ray_arrow = Arrow(
            np.array([2.5, 0.2, 0.0]),
            np.array([3.5, 0.2, 0.0]),
            color=COLOR_RAY,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )

        # 直线 (橙色, 两端箭头)
        line_demo = Line(
            np.array([-2.5, -1.6, 0.0]),
            np.array([2.5, -1.6, 0.0]),
            color=COLOR_LINE, stroke_width=5,
        )
        line_arr_l = Arrow(
            np.array([-2.5, -1.6, 0.0]),
            np.array([-3.5, -1.6, 0.0]),
            color=COLOR_LINE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )
        line_arr_r = Arrow(
            np.array([2.5, -1.6, 0.0]),
            np.array([3.5, -1.6, 0.0]),
            color=COLOR_LINE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )

        self.play(
            Create(seg_demo), FadeIn(dot_l), FadeIn(dot_r),
            run_time=0.6,
        )
        self.play(
            Create(ray_demo), FadeIn(ray_dot), GrowArrow(ray_arrow),
            run_time=0.6,
        )
        self.play(
            Create(line_demo), GrowArrow(line_arr_l), GrowArrow(line_arr_r),
            run_time=0.6,
        )
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(sub_hook),
            FadeOut(seg_demo), FadeOut(dot_l), FadeOut(dot_r),
            FadeOut(ray_demo), FadeOut(ray_dot), FadeOut(ray_arrow),
            FadeOut(line_demo), FadeOut(line_arr_l), FadeOut(line_arr_r),
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

        # 绘制线段 AB
        center_y = 2.2
        A_pos = np.array([-3.0, center_y, 0.0])
        B_pos = np.array([3.0, center_y, 0.0])

        seg = Line(A_pos, B_pos, color=COLOR_SEGMENT, stroke_width=6)

        dot_A = self.make_endpoint_dot(A_pos)
        dot_B = self.make_endpoint_dot(B_pos)

        label_A = Text("A", font=FONT, font_size=28, color=WHITE)
        label_A.next_to(dot_A, DOWN, buff=0.2)
        label_B = Text("B", font=FONT, font_size=28, color=WHITE)
        label_B.next_to(dot_B, DOWN, buff=0.2)

        # 先画线
        self.play(Create(seg), run_time=1.0)
        # 再加端点
        self.play(FadeIn(dot_A, scale=1.5), FadeIn(dot_B, scale=1.5), run_time=0.5)
        self.play(FadeIn(label_A), FadeIn(label_B), run_time=0.4)

        # 标注"端点"
        arrow_to_A = Arrow(
            A_pos + UP * 0.8 + LEFT * 0.5,
            A_pos + UP * 0.15,
            color=COLOR_HL,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
            buff=0.05,
        )
        endpoint_label_A = Text("端点", font=FONT, font_size=22, color=COLOR_HL)
        endpoint_label_A.move_to(A_pos + UP * 1.1 + LEFT * 0.5)

        arrow_to_B = Arrow(
            B_pos + UP * 0.8 + RIGHT * 0.5,
            B_pos + UP * 0.15,
            color=COLOR_HL,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
            buff=0.05,
        )
        endpoint_label_B = Text("端点", font=FONT, font_size=22, color=COLOR_HL)
        endpoint_label_B.move_to(B_pos + UP * 1.1 + RIGHT * 0.5)

        self.play(
            Create(arrow_to_A), FadeIn(endpoint_label_A),
            Create(arrow_to_B), FadeIn(endpoint_label_B),
            run_time=0.7,
        )
        self.wait(0.8)

        # 强调: 可以度量长度
        # 用大括号标注长度
        brace = Brace(seg, direction=UP, color=COLOR_HL)
        brace_text = Text("可以度量长度", font=FONT, font_size=22, color=COLOR_HL)
        brace_text.next_to(brace, UP, buff=0.15)

        self.play(
            FadeOut(arrow_to_A), FadeOut(endpoint_label_A),
            FadeOut(arrow_to_B), FadeOut(endpoint_label_B),
            run_time=0.3,
        )
        self.play(FadeIn(brace), FadeIn(brace_text), run_time=0.6)

        # 线段的写法说明
        write_explain = VGroup(
            Text("记作: 线段", font=FONT, font_size=24, color=WHITE),
            MathTex(r"AB", font_size=32, color=COLOR_SEGMENT),
            Text("或线段", font=FONT, font_size=24, color=WHITE),
            MathTex(r"BA", font_size=32, color=COLOR_SEGMENT),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.0)

        self.play(FadeIn(write_explain, shift=UP * 0.2), run_time=0.6)

        # 关键特征
        key_points = VGroup(
            VGroup(
                Text("端点数:", font=FONT, font_size=22, color=GRAY_A),
                Text("2 个", font=FONT, font_size=22, color=COLOR_ENDPOINT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("长度:", font=FONT, font_size=22, color=GRAY_A),
                Text("有限，可度量", font=FONT, font_size=22, color=COLOR_SEGMENT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("延伸:", font=FONT, font_size=22, color=GRAY_A),
                Text("不延伸", font=FONT, font_size=22, color=GRAY_B),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 2.0 + LEFT * 0.5)

        self.play(FadeIn(key_points, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(seg), FadeOut(dot_A), FadeOut(dot_B),
            FadeOut(label_A), FadeOut(label_B),
            FadeOut(brace), FadeOut(brace_text),
            FadeOut(write_explain), FadeOut(key_points),
            run_time=0.5,
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

        # 画射线: 从 O 出发, 向右延伸
        center_y = 2.2
        O_pos = np.array([-3.0, center_y, 0.0])
        ray_body_end = np.array([2.5, center_y, 0.0])
        ray_arrow_end = np.array([3.5, center_y, 0.0])

        ray_body = Line(O_pos, ray_body_end, color=COLOR_RAY, stroke_width=6)
        ray_arrow = Arrow(
            ray_body_end, ray_arrow_end,
            color=COLOR_RAY,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )

        dot_O = self.make_endpoint_dot(O_pos)
        label_O = Text("O", font=FONT, font_size=28, color=WHITE)
        label_O.next_to(dot_O, DOWN, buff=0.2)

        # 射线从端点"射出"
        self.play(FadeIn(dot_O, scale=2.0), run_time=0.4)
        self.play(FadeIn(label_O), run_time=0.3)
        self.play(Create(ray_body), run_time=0.8)
        self.play(GrowArrow(ray_arrow), run_time=0.6)

        # 标注端点
        endpoint_label = Text("端点 (起点)", font=FONT, font_size=22, color=COLOR_HL)
        endpoint_label.next_to(dot_O, UP, buff=0.3)

        self.play(FadeIn(endpoint_label), run_time=0.4)
        self.wait(0.5)

        # 标注"无限延伸"
        infinite_text = Text("无限延伸...", font=FONT, font_size=22, color=COLOR_ARROW)
        infinite_text.next_to(ray_arrow, RIGHT, buff=0.1)
        # 如果超界则向下移
        infinite_text.move_to(np.array([3.8, center_y + 0.5, 0.0]))

        self.play(FadeIn(infinite_text), run_time=0.4)
        # 闪烁动画强调
        self.play(Indicate(ray_arrow, color=COLOR_ARROW, scale_factor=1.3), run_time=0.6)
        self.wait(0.5)

        # 说明: 射线不可以度量
        self.play(FadeOut(endpoint_label), FadeOut(infinite_text), run_time=0.3)

        # 写法说明
        write_explain = VGroup(
            Text("记作: 射线", font=FONT, font_size=24, color=WHITE),
            MathTex(r"OA", font_size=32, color=COLOR_RAY),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.3)

        note = Text(
            "(从 O 出发，经过 A 点，无限延伸)",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 0.4)

        self.play(FadeIn(write_explain), run_time=0.5)
        self.play(FadeIn(note), run_time=0.4)

        # 关键特征
        key_points = VGroup(
            VGroup(
                Text("端点数:", font=FONT, font_size=22, color=GRAY_A),
                Text("1 个 (起点)", font=FONT, font_size=22, color=COLOR_ENDPOINT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("长度:", font=FONT, font_size=22, color=GRAY_A),
                Text("无限，不可度量", font=FONT, font_size=22, color=COLOR_RAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("延伸:", font=FONT, font_size=22, color=GRAY_A),
                Text("向一端无限延伸", font=FONT, font_size=22, color=COLOR_ARROW),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 2.5 + LEFT * 0.5)

        self.play(FadeIn(key_points, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # 生活例子: 手电筒的光
        life_example = Text(
            "例: 手电筒射出的光线",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(life_example, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(ray_body), FadeOut(ray_arrow),
            FadeOut(dot_O), FadeOut(label_O),
            FadeOut(write_explain), FadeOut(note),
            FadeOut(key_points), FadeOut(life_example),
            run_time=0.5,
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

        # 直线主体
        center_y = 2.2
        line_left_body = np.array([-2.5, center_y, 0.0])
        line_right_body = np.array([2.5, center_y, 0.0])
        arr_left_end = np.array([-3.5, center_y, 0.0])
        arr_right_end = np.array([3.5, center_y, 0.0])

        line_body = Line(line_left_body, line_right_body, color=COLOR_LINE, stroke_width=6)
        arr_left = Arrow(
            line_left_body, arr_left_end,
            color=COLOR_LINE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )
        arr_right = Arrow(
            line_right_body, arr_right_end,
            color=COLOR_LINE,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )

        # 直线上的两个点
        A_pos = np.array([-1.2, center_y, 0.0])
        B_pos = np.array([1.2, center_y, 0.0])

        dot_A = Dot(A_pos, color=WHITE, radius=0.08)
        dot_B = Dot(B_pos, color=WHITE, radius=0.08)
        label_A = Text("A", font=FONT, font_size=26, color=WHITE).next_to(dot_A, DOWN, buff=0.2)
        label_B = Text("B", font=FONT, font_size=26, color=WHITE).next_to(dot_B, DOWN, buff=0.2)

        # 先画直线
        self.play(Create(line_body), run_time=0.8)
        # 再添加两端箭头 (表示无限延伸)
        self.play(GrowArrow(arr_left), GrowArrow(arr_right), run_time=0.7)

        # 标注"无限延伸"
        left_inf = Text("无限...", font=FONT, font_size=20, color=COLOR_ARROW)
        left_inf.move_to(arr_left_end + LEFT * 0.5 + UP * 0.5)
        right_inf = Text("...无限", font=FONT, font_size=20, color=COLOR_ARROW)
        right_inf.move_to(arr_right_end + RIGHT * 0.5 + UP * 0.5)

        self.play(FadeIn(left_inf), FadeIn(right_inf), run_time=0.5)
        self.wait(0.5)

        # 在直线上标出两点
        self.play(FadeIn(dot_A), FadeIn(dot_B), run_time=0.4)
        self.play(FadeIn(label_A), FadeIn(label_B), run_time=0.4)
        self.play(FadeOut(left_inf), FadeOut(right_inf), run_time=0.3)

        # 注意: 没有端点
        no_endpoint = Text(
            "没有端点，无法确定起止",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(UP * 0.8)
        self.play(FadeIn(no_endpoint), run_time=0.5)

        # 写法说明
        write_explain = VGroup(
            Text("记作: 直线", font=FONT, font_size=24, color=WHITE),
            MathTex(r"AB", font_size=32, color=COLOR_LINE),
            Text("或直线", font=FONT, font_size=24, color=WHITE),
            MathTex(r"BA", font_size=32, color=COLOR_LINE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.2)

        self.play(FadeOut(no_endpoint), run_time=0.3)
        self.play(FadeIn(write_explain), run_time=0.5)

        # 关键特征
        key_points = VGroup(
            VGroup(
                Text("端点数:", font=FONT, font_size=22, color=GRAY_A),
                Text("0 个", font=FONT, font_size=22, color=GRAY_B),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("长度:", font=FONT, font_size=22, color=GRAY_A),
                Text("无限，不可度量", font=FONT, font_size=22, color=COLOR_LINE),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("延伸:", font=FONT, font_size=22, color=GRAY_A),
                Text("向两端无限延伸", font=FONT, font_size=22, color=COLOR_ARROW),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 2.5 + LEFT * 0.5)

        self.play(FadeIn(key_points, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(line_body), FadeOut(arr_left), FadeOut(arr_right),
            FadeOut(dot_A), FadeOut(dot_B),
            FadeOut(label_A), FadeOut(label_B),
            FadeOut(write_explain), FadeOut(key_points),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 三者对比
    # ------------------------------------------------------------------

    def scene_5_comparison(self):
        title = Text("三者对比", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 三行的 y 坐标
        y_seg = 3.2    # 线段
        y_ray = 1.2    # 射线
        y_lin = -0.8   # 直线

        x_left = -4.0
        x_right = 4.0
        line_x_left = -2.2
        line_x_right = 2.2

        # ------- 行1: 线段 -------
        seg_label = Text("线段", font=FONT, font_size=24, color=COLOR_SEGMENT)
        seg_label.move_to(np.array([-3.2, y_seg, 0.0]))

        seg_line = Line(
            np.array([-1.5, y_seg, 0.0]),
            np.array([2.5, y_seg, 0.0]),
            color=COLOR_SEGMENT, stroke_width=5,
        )
        seg_dot_l = Dot(np.array([-1.5, y_seg, 0.0]), color=COLOR_ENDPOINT, radius=0.1)
        seg_dot_r = Dot(np.array([2.5, y_seg, 0.0]), color=COLOR_ENDPOINT, radius=0.1)
        seg_info = Text("2端点 有限长", font=FONT, font_size=18, color=GRAY_A)
        seg_info.move_to(np.array([0.5, y_seg - 0.5, 0.0]))

        self.play(
            FadeIn(seg_label),
            Create(seg_line), FadeIn(seg_dot_l), FadeIn(seg_dot_r),
            run_time=0.6,
        )
        self.play(FadeIn(seg_info), run_time=0.3)

        # ------- 行2: 射线 -------
        ray_label = Text("射线", font=FONT, font_size=24, color=COLOR_RAY)
        ray_label.move_to(np.array([-3.2, y_ray, 0.0]))

        ray_body = Line(
            np.array([-1.5, y_ray, 0.0]),
            np.array([2.2, y_ray, 0.0]),
            color=COLOR_RAY, stroke_width=5,
        )
        ray_dot = Dot(np.array([-1.5, y_ray, 0.0]), color=COLOR_ENDPOINT, radius=0.1)
        ray_arr = Arrow(
            np.array([2.2, y_ray, 0.0]),
            np.array([3.2, y_ray, 0.0]),
            color=COLOR_RAY,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )
        ray_info = Text("1端点 无限长", font=FONT, font_size=18, color=GRAY_A)
        ray_info.move_to(np.array([0.5, y_ray - 0.5, 0.0]))

        self.play(
            FadeIn(ray_label),
            Create(ray_body), FadeIn(ray_dot), GrowArrow(ray_arr),
            run_time=0.6,
        )
        self.play(FadeIn(ray_info), run_time=0.3)

        # ------- 行3: 直线 -------
        lin_label = Text("直线", font=FONT, font_size=24, color=COLOR_LINE)
        lin_label.move_to(np.array([-3.2, y_lin, 0.0]))

        lin_body = Line(
            np.array([-1.2, y_lin, 0.0]),
            np.array([1.2, y_lin, 0.0]),
            color=COLOR_LINE, stroke_width=5,
        )
        lin_arr_l = Arrow(
            np.array([-1.2, y_lin, 0.0]),
            np.array([-2.2, y_lin, 0.0]),
            color=COLOR_LINE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )
        lin_arr_r = Arrow(
            np.array([1.2, y_lin, 0.0]),
            np.array([2.2, y_lin, 0.0]),
            color=COLOR_LINE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
            buff=0,
        )
        lin_info = Text("0端点 无限长", font=FONT, font_size=18, color=GRAY_A)
        lin_info.move_to(np.array([0.5, y_lin - 0.5, 0.0]))

        self.play(
            FadeIn(lin_label),
            Create(lin_body), GrowArrow(lin_arr_l), GrowArrow(lin_arr_r),
            run_time=0.6,
        )
        self.play(FadeIn(lin_info), run_time=0.3)

        self.wait(1.0)

        # 用分隔线区分行
        div1 = Line(
            np.array([-4.0, y_seg - 0.8, 0.0]),
            np.array([4.0, y_seg - 0.8, 0.0]),
            color=GRAY_D, stroke_width=1.5,
        )
        div2 = Line(
            np.array([-4.0, y_ray - 0.8, 0.0]),
            np.array([4.0, y_ray - 0.8, 0.0]),
            color=GRAY_D, stroke_width=1.5,
        )
        self.play(Create(div1), Create(div2), run_time=0.4)

        # 关系说明
        relation = VGroup(
            Text("关系:", font=FONT, font_size=22, color=COLOR_HL),
            Text("线段 < 射线 < 直线", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.5)

        extend_note = Text(
            "射线和直线都无限延伸，不可度量",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 4.3)

        self.play(FadeIn(relation), FadeIn(extend_note), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(seg_label), FadeOut(seg_line),
            FadeOut(seg_dot_l), FadeOut(seg_dot_r), FadeOut(seg_info),
            FadeOut(ray_label), FadeOut(ray_body),
            FadeOut(ray_dot), FadeOut(ray_arr), FadeOut(ray_info),
            FadeOut(lin_label), FadeOut(lin_body),
            FadeOut(lin_arr_l), FadeOut(lin_arr_r), FadeOut(lin_info),
            FadeOut(div1), FadeOut(div2),
            FadeOut(relation), FadeOut(extend_note),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 知识总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text("知识总结", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 卡片背景
        card_bg = RoundedRectangle(
            width=7.5, height=10.0,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.05,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # ------- 条目 1: 线段 -------
        item1_title = Text("线段", font=FONT, font_size=28, color=COLOR_SEGMENT)
        item1_body = VGroup(
            Text("有 2 个端点", font=FONT, font_size=20, color=GRAY_A),
            Text("长度有限，可以度量", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        # 小图示
        item1_demo = VGroup(
            Line(ORIGIN, RIGHT * 1.5, color=COLOR_SEGMENT, stroke_width=4),
            Dot(ORIGIN, color=COLOR_ENDPOINT, radius=0.07),
            Dot(RIGHT * 1.5, color=COLOR_ENDPOINT, radius=0.07),
        )
        item1_demo.move_to(np.array([2.5, 0.0, 0.0]))

        item1 = VGroup(item1_title, item1_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item1_group = VGroup(item1, item1_demo).arrange(RIGHT, buff=0.4)
        item1_group.move_to(UP * 3.5)

        self.play(FadeIn(item1_group, shift=RIGHT * 0.3), run_time=0.6)

        # ------- 条目 2: 射线 -------
        item2_title = Text("射线", font=FONT, font_size=28, color=COLOR_RAY)
        item2_body = VGroup(
            Text("只有 1 个端点 (起点)", font=FONT, font_size=20, color=GRAY_A),
            Text("向一端无限延伸，不可度量", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        # 小图示
        ray_demo_line = Line(ORIGIN, RIGHT * 1.2, color=COLOR_RAY, stroke_width=4)
        ray_demo_arr = Arrow(
            RIGHT * 1.2, RIGHT * 1.8,
            color=COLOR_RAY, stroke_width=4,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        ray_demo_dot = Dot(ORIGIN, color=COLOR_ENDPOINT, radius=0.07)
        item2_demo = VGroup(ray_demo_line, ray_demo_arr, ray_demo_dot)
        item2_demo.move_to(np.array([2.5, 0.0, 0.0]))

        item2 = VGroup(item2_title, item2_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item2_group = VGroup(item2, item2_demo).arrange(RIGHT, buff=0.4)
        item2_group.move_to(UP * 1.2)

        self.play(FadeIn(item2_group, shift=RIGHT * 0.3), run_time=0.6)

        # ------- 条目 3: 直线 -------
        item3_title = Text("直线", font=FONT, font_size=28, color=COLOR_LINE)
        item3_body = VGroup(
            Text("没有端点", font=FONT, font_size=20, color=GRAY_A),
            Text("向两端无限延伸，不可度量", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        # 小图示
        line_demo_body = Line(LEFT * 0.3, RIGHT * 1.3, color=COLOR_LINE, stroke_width=4)
        line_demo_arr_l = Arrow(
            LEFT * 0.3, LEFT * 0.9,
            color=COLOR_LINE, stroke_width=4,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        line_demo_arr_r = Arrow(
            RIGHT * 1.3, RIGHT * 1.9,
            color=COLOR_LINE, stroke_width=4,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        item3_demo = VGroup(line_demo_body, line_demo_arr_l, line_demo_arr_r)
        item3_demo.move_to(np.array([2.5, 0.0, 0.0]))

        item3 = VGroup(item3_title, item3_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item3_group = VGroup(item3, item3_demo).arrange(RIGHT, buff=0.4)
        item3_group.move_to(DOWN * 1.1)

        self.play(FadeIn(item3_group, shift=RIGHT * 0.3), run_time=0.6)

        # 底部要点
        bottom_note = VGroup(
            Text("射线和直线: 无限长，不可度量", font=FONT, font_size=20, color=GRAY_B),
            Text("线段: 有限长，可以度量", font=FONT, font_size=20, color=GRAY_B),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to(DOWN * 3.3)

        self.play(FadeIn(bottom_note), run_time=0.5)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1_group),
            FadeOut(item2_group),
            FadeOut(item3_group),
            FadeOut(bottom_note),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        # 作者信息放大
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
            "关注我，学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 三种线的装饰
        deco_seg = VGroup(
            Line(LEFT * 1.5, RIGHT * 1.5, color=COLOR_SEGMENT, stroke_width=4),
            Dot(LEFT * 1.5, color=COLOR_ENDPOINT, radius=0.08),
            Dot(RIGHT * 1.5, color=COLOR_ENDPOINT, radius=0.08),
        ).move_to(DOWN * 3.0)

        deco_ray_body = Line(LEFT * 1.5, RIGHT * 1.0, color=COLOR_RAY, stroke_width=4)
        deco_ray_arr = Arrow(
            RIGHT * 1.0, RIGHT * 1.8,
            color=COLOR_RAY, stroke_width=4,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        deco_ray_dot = Dot(LEFT * 1.5, color=COLOR_ENDPOINT, radius=0.08)
        deco_ray = VGroup(deco_ray_body, deco_ray_arr, deco_ray_dot).move_to(DOWN * 4.0)

        deco_lin_body = Line(LEFT * 1.0, RIGHT * 1.0, color=COLOR_LINE, stroke_width=4)
        deco_lin_l = Arrow(
            LEFT * 1.0, LEFT * 1.8,
            color=COLOR_LINE, stroke_width=4,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        deco_lin_r = Arrow(
            RIGHT * 1.0, RIGHT * 1.8,
            color=COLOR_LINE, stroke_width=4,
            max_tip_length_to_length_ratio=0.3, buff=0,
        )
        deco_lin = VGroup(deco_lin_body, deco_lin_l, deco_lin_r).move_to(DOWN * 5.0)

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


# 运行命令:
# manim -pql 001_线段射线直线.py LineSegmentRayLesson   # 快速预览
# manim -qm 001_线段射线直线.py LineSegmentRayLesson    # 中等质量
# manim -qh 001_线段射线直线.py LineSegmentRayLesson    # 高质量

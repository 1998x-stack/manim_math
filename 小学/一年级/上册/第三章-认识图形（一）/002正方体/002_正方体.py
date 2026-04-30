"""
正方体 - Cube Recognition Animation
一年级上册 第三章：认识图形（一）
目标受众: 一年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

NOTE: 2D Scene only. Cube drawn using 2D isometric/perspective polygons.
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CubeRecognitionLesson(Scene):
    """
    正方体认识 教学动画场景

    场景顺序:
    1. 开场钩子 - 引入正方体
    2. 认识正方体 - 展示正方体形状
    3. 6个面 - 展示6个面
    4. 每个面都是正方形 - 验证各面
    5. 所有面大小相同 - 对比展示
    6. 片尾总结 + 关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_CUBE_FRONT = "#4a90d9"
        self.COLOR_CUBE_TOP = "#7bc8f6"
        self.COLOR_CUBE_RIGHT = "#2d6a9f"
        self.COLOR_CUBE_STROKE = "#ffffff"
        self.COLOR_HIGHLIGHT = "#f1c40f"
        self.COLOR_FACE = "#e74c3c"
        self.COLOR_TITLE = "#ffffff"
        self.COLOR_TEXT = "#e0e0e0"
        self.COLOR_AUTHOR = "#6b7280"

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduce_cube()
        self.scene_3_six_faces()
        self.scene_4_square_faces()
        self.scene_5_same_size()
        self.scene_6_outro()

    def setup_geometry(self):
        """初始化正方体的等轴测投影坐标（基准，中心在原点）"""
        s = 2.0    # 正方体边长
        ix = 0.9   # 等轴测水平偏移
        iy = 0.52  # 等轴测垂直偏移

        # 正面4顶点（左下、右下、右上、左上）
        self.pA = np.array([-s / 2, -s / 2, 0])
        self.pB = np.array([ s / 2, -s / 2, 0])
        self.pC = np.array([ s / 2,  s / 2, 0])
        self.pD = np.array([-s / 2,  s / 2, 0])

        # 背面4顶点（通过等轴测偏移）
        self.pE = self.pA + np.array([ix, iy, 0])
        self.pF = self.pB + np.array([ix, iy, 0])
        self.pG = self.pC + np.array([ix, iy, 0])
        self.pH = self.pD + np.array([ix, iy, 0])

    def make_cube_vgroup(self, center=ORIGIN, scale=1.0,
                         front_color="#4a90d9", top_color="#7bc8f6",
                         right_color="#2d6a9f", stroke_color=WHITE,
                         stroke_width=2.5,
                         front_opacity=0.88, top_opacity=0.88,
                         right_opacity=0.88):
        """
        构建一个等轴测正方体 VGroup。
        包括正面、顶面、右侧面、隐藏边（虚线）。
        """
        c = np.array(center) if not isinstance(center, np.ndarray) else center

        def pt(p):
            return p * scale + c

        A = pt(self.pA)
        B = pt(self.pB)
        C = pt(self.pC)
        D = pt(self.pD)
        E = pt(self.pE)
        F = pt(self.pF)
        G = pt(self.pG)
        H = pt(self.pH)

        # 正面 ABCD
        front = Polygon(A, B, C, D,
                        fill_color=front_color,
                        fill_opacity=front_opacity,
                        stroke_color=stroke_color,
                        stroke_width=stroke_width)

        # 顶面 DCGH
        top = Polygon(D, C, G, H,
                      fill_color=top_color,
                      fill_opacity=top_opacity,
                      stroke_color=stroke_color,
                      stroke_width=stroke_width)

        # 右面 BCGF
        right = Polygon(B, C, G, F,
                        fill_color=right_color,
                        fill_opacity=right_opacity,
                        stroke_color=stroke_color,
                        stroke_width=stroke_width)

        # 隐藏边（虚线）
        hidden = VGroup(
            DashedLine(A, E, color=stroke_color, stroke_width=1.2,
                       dash_length=0.07, dashed_ratio=0.5),
            DashedLine(E, H, color=stroke_color, stroke_width=1.2,
                       dash_length=0.07, dashed_ratio=0.5),
            DashedLine(E, F, color=stroke_color, stroke_width=1.2,
                       dash_length=0.07, dashed_ratio=0.5),
        )

        return VGroup(front, top, right, hidden)

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        """开场：钩子 + 作者信息"""
        # 作者信息（顶部常驻）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_label, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "你认识正方体吗？",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.2)

        self.play(Write(hook), run_time=0.9)

        # 简单的正方体出现（居中）
        hook_cube = self.make_cube_vgroup(center=np.array([0.0, 0.5, 0.0]),
                                          scale=0.85)
        self.play(FadeIn(hook_cube, scale=0.6), run_time=0.9)
        self.wait(0.6)

        # 问号装饰
        q_marks = VGroup(
            Text("?", font="PingFang SC", font_size=60,
                 color=self.COLOR_HIGHLIGHT).move_to(LEFT * 3.2 + DOWN * 0.3),
            Text("?", font="PingFang SC", font_size=48,
                 color=self.COLOR_HIGHLIGHT).move_to(RIGHT * 3.3 + UP * 1.0),
        )
        self.play(
            *[FadeIn(q, scale=0.5) for q in q_marks],
            run_time=0.5
        )
        self.wait(0.6)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(q_marks),
            FadeOut(hook_cube),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 2: 认识正方体
    # ─────────────────────────────────────────────
    def scene_2_introduce_cube(self):
        """展示正方体，给出名称"""
        # 大标题
        title = Text(
            "正方体",
            font="PingFang SC",
            font_size=64,
            color=self.COLOR_TITLE,
            weight=BOLD
        ).move_to(UP * 5.8)

        subtitle = Text(
            "立体图形的一种",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_TEXT
        ).move_to(UP * 4.9)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 主正方体（居中稍上）
        self.main_cube = self.make_cube_vgroup(
            center=np.array([0.0, 0.8, 0.0]),
            scale=1.0,
            front_color=self.COLOR_CUBE_FRONT,
            top_color=self.COLOR_CUBE_TOP,
            right_color=self.COLOR_CUBE_RIGHT,
        )
        self.play(Create(self.main_cube), run_time=1.2)
        self.wait(0.5)

        # 标注：生活中的例子
        rubik_label = Text(
            "生活中的正方体：魔方、骰子",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TEXT
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(rubik_label, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)

        # 清理副标题和标注
        self.play(
            FadeOut(subtitle),
            FadeOut(rubik_label),
            run_time=0.4
        )

        # 保留 title（缩小上移）和 main_cube
        self.play(
            title.animate.move_to(UP * 6.5).set_font_size(36),
            run_time=0.5
        )
        self.title_label = title

    # ─────────────────────────────────────────────
    # Scene 3: 6个面
    # ─────────────────────────────────────────────
    def scene_3_six_faces(self):
        """展示正方体有6个面"""
        # 场景标题
        face_title = Text(
            "正方体有 6 个面",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.6)

        self.play(Write(face_title), run_time=0.7)

        # 面名称列表
        face_names = [
            "① 正面",
            "② 背面",
            "③ 顶面",
            "④ 底面",
            "⑤ 左面",
            "⑥ 右面",
        ]
        face_colors_list = [
            "#e74c3c", "#e67e22", "#2ecc71",
            "#3498db", "#9b59b6", "#f39c12",
        ]

        # 左侧面名列表
        name_items = VGroup()
        for name, col in zip(face_names, face_colors_list):
            t = Text(name, font="PingFang SC", font_size=28, color=col)
            name_items.add(t)
        name_items.arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        name_items.move_to(LEFT * 2.5 + DOWN * 2.2)

        # 逐条滑入
        for item in name_items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.22)

        self.wait(0.5)

        # 计数器
        count_text = Text(
            "共 6 个面",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(RIGHT * 2.0 + DOWN * 4.6)

        self.play(FadeIn(count_text, scale=0.8), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(face_title),
            FadeOut(name_items),
            FadeOut(count_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 4: 每个面都是正方形
    # ─────────────────────────────────────────────
    def scene_4_square_faces(self):
        """展示每个面都是正方形"""
        # 场景标题
        sq_title = Text(
            "每个面都是正方形",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.6)

        self.play(Write(sq_title), run_time=0.7)

        # 将主正方体缩小上移
        self.play(
            self.main_cube.animate.scale(0.70).move_to(UP * 3.0),
            run_time=0.6
        )

        # 展示3个独立正方形代表面
        face_colors_3 = ["#e74c3c", "#2ecc71", "#3498db"]
        positions_3 = [
            np.array([-2.8, -1.5, 0]),
            np.array([0.0,  -1.5, 0]),
            np.array([2.8,  -1.5, 0]),
        ]
        labels_3 = ["正面", "顶面", "右面"]

        squares_group = VGroup()
        label_group = VGroup()

        for col, pos, lbl in zip(face_colors_3, positions_3, labels_3):
            sq = Square(side_length=1.5,
                        fill_color=col,
                        fill_opacity=0.88,
                        stroke_color=WHITE,
                        stroke_width=2.5)
            sq.move_to(pos)
            squares_group.add(sq)

            lbl_text = Text(lbl, font="PingFang SC",
                            font_size=24, color=col)
            lbl_text.next_to(sq, DOWN, buff=0.18)
            label_group.add(lbl_text)

        self.play(
            *[FadeIn(sq, scale=0.5) for sq in squares_group],
            run_time=0.9
        )
        self.play(
            *[FadeIn(lbl) for lbl in label_group],
            run_time=0.5
        )

        # 标注"每个面 = 正方形"
        sq_annot = Text(
            "每个面 = 正方形",
            font="PingFang SC",
            font_size=34,
            color=WHITE
        ).move_to(DOWN * 3.5)

        # 勾选标记
        checks = VGroup()
        for sq in squares_group:
            ck = Text("✓", font="PingFang SC",
                      font_size=40, color=self.COLOR_HIGHLIGHT)
            ck.move_to(sq.get_center())
            checks.add(ck)

        self.play(FadeIn(sq_annot, shift=UP * 0.2), run_time=0.5)
        self.play(
            *[FadeIn(ck, scale=0.5) for ck in checks],
            run_time=0.6
        )
        self.wait(1.3)

        # 清理
        self.play(
            FadeOut(sq_title),
            FadeOut(squares_group),
            FadeOut(label_group),
            FadeOut(sq_annot),
            FadeOut(checks),
            run_time=0.5
        )

        # 还原主正方体
        self.play(
            self.main_cube.animate.scale(1.0 / 0.70).move_to(UP * 0.8),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 5: 所有面大小相同
    # ─────────────────────────────────────────────
    def scene_5_same_size(self):
        """展示所有6个面大小完全相同"""
        # 场景标题
        same_title = Text(
            "6个面，大小完全相同！",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.6)

        self.play(Write(same_title), run_time=0.7)

        # 将主正方体缩小上移
        self.play(
            self.main_cube.animate.scale(0.62).move_to(UP * 3.0),
            run_time=0.5
        )

        # 展示6个相同大小的正方形（3列×2行网格）
        side_len = 1.15
        face_color = "#4a90d9"
        face_names_all = ["正面", "背面", "顶面", "底面", "左面", "右面"]

        rows, cols_n = 2, 3
        grid_squares = VGroup()
        grid_labels = VGroup()

        for r in range(rows):
            for c in range(cols_n):
                idx = r * cols_n + c
                x = (c - 1) * (side_len + 0.32)
                y = -r * (side_len + 0.52) - 1.5

                sq = Square(side_length=side_len,
                            fill_color=face_color,
                            fill_opacity=0.85,
                            stroke_color=WHITE,
                            stroke_width=2.2)
                sq.move_to(np.array([x, y, 0]))
                grid_squares.add(sq)

                num_t = Text(str(idx + 1), font="PingFang SC",
                             font_size=26, color=WHITE, weight=BOLD)
                num_t.move_to(sq.get_center() + UP * 0.18)

                name_t = Text(face_names_all[idx], font="PingFang SC",
                              font_size=18, color="#a0c4ff")
                name_t.move_to(sq.get_center() + DOWN * 0.22)

                grid_labels.add(VGroup(num_t, name_t))

        for sq, lbl in zip(grid_squares, grid_labels):
            self.play(
                FadeIn(sq, scale=0.6),
                FadeIn(lbl, scale=0.6),
                run_time=0.17
            )

        self.wait(0.5)

        # 强调"一样大"
        same_annot = Text(
            "一样大！",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(same_annot, scale=0.8), run_time=0.5)

        # 闪烁高亮
        self.play(
            *[sq.animate.set_fill(color=self.COLOR_HIGHLIGHT, opacity=0.95)
              for sq in grid_squares],
            run_time=0.45
        )
        self.play(
            *[sq.animate.set_fill(color=face_color, opacity=0.85)
              for sq in grid_squares],
            run_time=0.45
        )
        self.wait(0.8)

        # 总结公式框
        summary_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.8,
            height=1.55,
            fill_color="#1e3a5f",
            fill_opacity=0.95,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2.5
        ).move_to(DOWN * 6.2)

        summary_text = Text(
            "正方体 = 6个面  每面正方形  大小相同",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(summary_box.get_center())

        self.play(
            FadeIn(summary_box),
            Write(summary_text),
            run_time=0.8
        )
        self.wait(1.6)

        # 清理
        self.play(
            FadeOut(same_title),
            FadeOut(grid_squares),
            FadeOut(grid_labels),
            FadeOut(same_annot),
            FadeOut(summary_box),
            FadeOut(summary_text),
            run_time=0.6
        )

        # 还原主正方体
        self.play(
            self.main_cube.animate.scale(1.0 / 0.62).move_to(UP * 0.8),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 6: 片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        """总结 + 关注提示"""
        self.play(FadeOut(self.main_cube), run_time=0.5)
        self.play(FadeOut(self.title_label), run_time=0.3)

        # 总结卡片
        recap_title = Text(
            "今天学了什么？",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)

        self.play(Write(recap_title), run_time=0.7)

        # 三条总结
        points = [
            "① 正方体有 6 个面",
            "② 每个面都是正方形",
            "③ 6个面大小完全相同",
        ]
        point_colors = ["#e74c3c", "#2ecc71", "#3498db"]

        point_group = VGroup()
        for pt, col in zip(points, point_colors):
            t = Text(pt, font="PingFang SC", font_size=34, color=col)
            point_group.add(t)
        point_group.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        point_group.move_to(UP * 2.8)

        for pt in point_group:
            self.play(FadeIn(pt, shift=RIGHT * 0.4), run_time=0.4)
            self.wait(0.28)

        self.wait(0.9)

        # 小正方体装饰（排成一行）
        mini_cubes = VGroup()
        for i in range(3):
            mc = self.make_cube_vgroup(
                center=np.array([(i - 1) * 2.3, -3.2, 0]),
                scale=0.36,
                front_color=self.COLOR_CUBE_FRONT,
                top_color=self.COLOR_CUBE_TOP,
                right_color=self.COLOR_CUBE_RIGHT,
            )
            mini_cubes.add(mc)

        self.play(
            *[FadeIn(mc, scale=0.5) for mc in mini_cubes],
            run_time=0.8
        )
        self.wait(0.5)

        # 作者信息（放大版）
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4.6)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_AUTHOR
        ).next_to(author_big, DOWN, buff=0.25)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.3)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(recap_title),
            FadeOut(point_group),
            FadeOut(mini_cubes),
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(self.author_label),
            run_time=1.0
        )

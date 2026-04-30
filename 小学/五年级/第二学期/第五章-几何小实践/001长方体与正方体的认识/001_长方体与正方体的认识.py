"""
001_长方体与正方体的认识.py — 长方体与正方体的认识 教学动画

知识点: 长方体和正方体的面、棱、顶点特征
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 长方体: 6面(相对面相等), 12棱(相对棱相等), 8顶点
  2. 长、宽、高的概念
  3. 正方体: 特殊长方体, 6个相同正方形面, 12条等棱
  4. 正方体是长方体的特殊情况
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
COLOR_RECT = "#3b82f6"
COLOR_CUBE = "#22c55e"
COLOR_FACE = "#f59e0b"
COLOR_EDGE = "#a78bfa"
COLOR_VERTEX = "#ef4444"
COLOR_HL = "#fbbf24"
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


class PrismIntroLesson(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_rect_features()
        self.scene_3_cube_features()
        self.scene_4_comparison()
        self.scene_5_summary()
        self.scene_6_outro()

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text("长方体与正方体", font=FONT, font_size=44, color=WHITE, weight=BOLD).move_to(UP * 5.5)
        hook2 = Text("有什么特征？", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    def scene_2_rect_features(self):
        title = Text("长方体的特征", font=FONT, font_size=38, color=COLOR_RECT, weight=BOLD).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 面
        f1 = VGroup(
            Text("面：", font=FONT, font_size=26, color=COLOR_FACE, weight=BOLD),
            Text("6个面，相对的面完全相同", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)
        self.play(FadeIn(f1, shift=RIGHT * 0.3), run_time=0.5)

        # 棱
        f2 = VGroup(
            Text("棱：", font=FONT, font_size=26, color=COLOR_EDGE, weight=BOLD),
            Text("12条棱，相对的棱长度相等", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 2.3)
        self.play(FadeIn(f2, shift=RIGHT * 0.3), run_time=0.5)

        # 顶点
        f3 = VGroup(
            Text("顶点：", font=FONT, font_size=26, color=COLOR_VERTEX, weight=BOLD),
            Text("8个顶点", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.1)
        self.play(FadeIn(f3, shift=RIGHT * 0.3), run_time=0.5)

        # 长宽高
        lwh = Text(
            "三组不同的棱：长、宽、高",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 0.3)
        self.play(Write(lwh), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, f1, f2, f3, lwh)), run_time=0.4)

    def scene_3_cube_features(self):
        title = Text("正方体的特征", font=FONT, font_size=38, color=COLOR_CUBE, weight=BOLD).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        f1 = VGroup(
            Text("面：", font=FONT, font_size=26, color=COLOR_FACE, weight=BOLD),
            Text("6个完全相同的正方形", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)
        self.play(FadeIn(f1, shift=RIGHT * 0.3), run_time=0.5)

        f2 = VGroup(
            Text("棱：", font=FONT, font_size=26, color=COLOR_EDGE, weight=BOLD),
            Text("12条棱，长度全部相等", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 2.3)
        self.play(FadeIn(f2, shift=RIGHT * 0.3), run_time=0.5)

        f3 = VGroup(
            Text("顶点：", font=FONT, font_size=26, color=COLOR_VERTEX, weight=BOLD),
            Text("8个顶点", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 1.1)
        self.play(FadeIn(f3, shift=RIGHT * 0.3), run_time=0.5)

        special = Text(
            "正方体 = 长、宽、高都相等的长方体",
            font=FONT, font_size=22, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.3)
        self.play(Write(special), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, f1, f2, f3, special)), run_time=0.4)

    def scene_4_comparison(self):
        title = Text("对比", font=FONT, font_size=36, color=COLOR_HL, weight=BOLD).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 表头
        h_name = Text("特征", font=FONT, font_size=22, color=COLOR_HL)
        h_rect = Text("长方体", font=FONT, font_size=22, color=COLOR_RECT)
        h_cube = Text("正方体", font=FONT, font_size=22, color=COLOR_CUBE)
        header = VGroup(h_name, h_rect, h_cube).arrange(RIGHT, buff=1.5).move_to(UP * 3.5)
        self.play(FadeIn(header), run_time=0.4)

        sep = Line(LEFT * 4, RIGHT * 4, color=GRAY, stroke_width=1).move_to(UP * 3.0)
        self.play(Create(sep), run_time=0.2)

        rows = []
        data = [
            ("面", "6面,相对面相同", "6个相同正方形"),
            ("棱", "12条,4组×3", "12条,全相等"),
            ("顶点", "8个", "8个"),
            ("关系", "", "特殊的长方体"),
        ]
        for i, (feat, rect_val, cube_val) in enumerate(data):
            r = VGroup(
                Text(feat, font=FONT, font_size=20, color=COLOR_HL),
                Text(rect_val, font=FONT, font_size=18, color=WHITE),
                Text(cube_val, font=FONT, font_size=18, color=WHITE),
            ).arrange(RIGHT, buff=1.2).move_to(UP * (2.0 - i * 1.0))
            rows.append(r)
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.4)

        key = Text(
            "正方体是特殊的长方体！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, header, sep, *rows, key)), run_time=0.4)

    def scene_5_summary(self):
        box = RoundedRectangle(
            width=8.0, height=5.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text("长方体与正方体", font=FONT, font_size=30, color=COLOR_HL, weight=BOLD).move_to(UP * 2.8)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 都有6个面、12条棱、8个顶点", font=FONT, font_size=22, color=WHITE),
            Text("2. 长方体：相对的面和棱相等", font=FONT, font_size=22, color=COLOR_RECT),
            Text("3. 正方体：所有面和棱都相等", font=FONT, font_size=22, color=COLOR_CUBE),
            Text("4. 正方体是特殊的长方体", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)
        self.wait(2.0)
        self.play(FadeOut(VGroup(box, sum_title, items)), run_time=0.5)

    def scene_6_outro(self):
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=42, color=WHITE).move_to(UP * 2.0)
        author_id = Text("@emptyandcalm", font=FONT, font_size=30, color=GRAY_A).move_to(UP * 1.0)
        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=COLOR_HL).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(self.author_mob, author_id, follow)), run_time=0.8)


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 001_长方体与正方体的认识.py PrismIntroLesson
#   高质量:    manim -qh  001_长方体与正方体的认识.py PrismIntroLesson
#   4K:        manim -qk  001_长方体与正方体的认识.py PrismIntroLesson
# ======================================================================

"""一年级：从物体表面描出四种常见平面图形。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
FONT = "PingFang SC"


def plane_shape_traits():
    """本课四个示例形状的直边和角的数量，圆使用弯曲边界。"""
    return {
        "长方形": (4, 4),
        "正方形": (4, 4),
        "三角形": (3, 3),
        "圆形": (0, 0),
    }


class Topic001认识平面图形Animation(Scene):
    """描边、命名、比较直线边和弯曲边界。"""

    def construct(self):
        assert plane_shape_traits()["三角形"] == (3, 3)
        assert plane_shape_traits()["圆形"] == (0, 0)
        self.camera.background_color = BG
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7)
        title = Text("认识平面图形", font=FONT, font_size=45,
                     color=YELLOW).move_to(UP * 5.55)
        self.add(author)
        self.play(Write(title))

        intro = Text(
            "沿着物体的表面描一描，会得到什么？",
            font=FONT, font_size=26
        ).move_to(UP * 4.3)
        self.play(Write(intro))

        examples = [
            (Rectangle(width=1.6, height=1.0, color=BLUE,
                       fill_opacity=0.6), "长方形", "书本的封面"),
            (Square(side_length=1.35, color=GREEN,
                    fill_opacity=0.6), "正方形", "方形棋盘"),
            (Triangle(color=ORANGE, fill_opacity=0.6).scale(0.85),
             "三角形", "三角形小旗"),
            (Circle(radius=0.7, color=PURPLE, fill_opacity=0.6),
             "圆形", "钟表的表面")
        ]
        tiles = VGroup()
        for shape, name, real_life in examples:
            label = Text(name, font=FONT, font_size=28, color=WHITE)
            example = Text(real_life, font=FONT, font_size=21, color=GRAY_A)
            tile = VGroup(
                shape,
                label,
                example
            ).arrange(DOWN, buff=0.18)
            tiles.add(tile)
        tiles.arrange_in_grid(rows=2, cols=2, buff=(1.05, 0.7))
        tiles.move_to(UP * 0.7)

        for tile in tiles:
            self.play(Create(tile[0]), FadeIn(tile[1]), FadeIn(tile[2]),
                      run_time=0.85)
        self.wait(0.8)

        traits = plane_shape_traits()
        # 展示有直边的形状与圆形的弯曲边界，避免混淆立体和平面。
        self.play(Indicate(tiles[2][0], color=YELLOW))
        triangle_note = Text(
            f"三角形：{traits['三角形'][0]}条直边",
            font=FONT, font_size=25, color=YELLOW
        ).move_to(DOWN * 3.45)
        self.play(FadeIn(triangle_note))
        self.wait(0.5)
        circle_note = Text(
            "圆形的边界是弯曲的，没有直角顶点",
            font=FONT, font_size=24, color=YELLOW
        ).move_to(DOWN * 3.45)
        self.play(Indicate(tiles[3][0], color=YELLOW),
                  ReplacementTransform(triangle_note, circle_note))
        self.wait(0.6)
        self.play(FadeOut(tiles), FadeOut(circle_note), FadeOut(intro))

        summary = VGroup(
            Text("长方形、正方形、三角形、圆形", font=FONT,
                 font_size=28, color=YELLOW),
            Text("它们都是常见的平面图形", font=FONT, font_size=28),
            Text("还可以在生活中找到更多例子", font=FONT, font_size=26),
        ).arrange(DOWN, buff=0.65).move_to(UP * 0.5)
        self.play(LaggedStart(*(Write(row) for row in summary),
                              lag_ratio=0.35))
        self.wait(1.3)

"""条形统计图（二）：一格表示 2 个单位。

注意 Python 标识符不能包含中文全角括号；CLI 场景名为 统计条形统计图二Animation。
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 统计条形统计图二Animation(Scene):
    """横向对应同一刻度，柱高严格等于“数量 ÷ 每格单位”。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("认识条形统计图", font_size=44, color=GOLD).move_to(UP * 6.2)
        key = Text("每一格代表2个", font_size=31, color=YELLOW).move_to(UP * 4.7)
        self.play(Write(title), FadeIn(key))

        # 0、2、4、6、8、10 六个刻度，对应 5 个等高网格。
        base_y, step = -3.0, 0.65
        grid = VGroup()
        for grid_index in range(6):
            y = base_y + grid_index * step
            line = Line([-3.2, y, 0], [3.75, y, 0], color=GRAY_B, stroke_width=1)
            tick = Text(str(grid_index * 2), font_size=23)
            tick.move_to([-3.6, y, 0])
            grid.add(line, tick)
        self.play(FadeIn(grid))

        counts = (4, 6, 8, 10)
        names = ("一组", "二组", "三组", "四组")
        centers = (-2.35, -0.75, 0.85, 2.45)
        for count, name, x in zip(counts, names, centers):
            assert count % 2 == 0
            squares = count // 2
            height = squares * step
            bar = Rectangle(
                width=0.9, height=height, color=BLUE_B,
                fill_color=BLUE_B, fill_opacity=0.8
            ).move_to([x, base_y + height / 2, 0])
            group_name = Text(name, font_size=22).move_to([x, base_y - 0.55, 0])
            label = Text(f"{count}个", font_size=24, color=YELLOW)
            label.move_to([x, base_y + height + 0.4, 0])
            self.play(GrowFromEdge(bar, DOWN), FadeIn(group_name), FadeIn(label), run_time=0.7)

        summary = Text("一组：4个，占2格；四组：10个，占5格", font_size=26)
        summary.move_to(DOWN * 5.3)
        self.play(Write(summary))
        self.wait(2)

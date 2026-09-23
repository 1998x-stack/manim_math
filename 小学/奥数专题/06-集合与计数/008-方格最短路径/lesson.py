"""方格最短路径：每个交点的路径数等于左侧和下方的路径数之和。"""
from math import comb
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def path_table(right: int, up: int) -> list[list[int]]:
    if any(type(v) is not int or v < 0 for v in (right, up)):
        raise ValueError("nonnegative integer steps required")
    table = [[0] * (right + 1) for _ in range(up + 1)]
    for y in range(up + 1):
        for x in range(right + 1):
            table[y][x] = 1 if (x, y) == (0, 0) else (table[y-1][x] if y else 0) + (table[y][x-1] if x else 0)
            assert table[y][x] == comb(x + y, x)
    return table


class GridPathScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        table = path_table(3, 2)
        title = Text("最短路径：走方格", font=FONT, font_size=36).move_to(UP * 6.2)
        subtitle = Text("向右 3 步、向上 2 步，共有几种走法？", font=FONT, font_size=27).move_to(UP * 4.95)
        self.play(Write(title), FadeIn(subtitle))
        def point(x, y):
            return np.array([-2.8 + 1.8*x, -1.5 + 1.8*y, 0])
        edges = VGroup()
        for y in range(3):
            for x in range(4):
                if x < 3:
                    edges.add(Line(point(x, y), point(x+1, y), color=GREY_B))
                if y < 2:
                    edges.add(Line(point(x, y), point(x, y+1), color=GREY_B))
        self.play(Create(edges))
        # 按 x+y 的顺序填写，各点只依赖已出现的左侧或下方数字。
        for diagonal in range(6):
            numbers = []
            for y in range(3):
                x = diagonal-y
                if 0 <= x <= 3:
                    disk = Circle(radius=.32, color=BLUE_B, fill_color=BG, fill_opacity=1).move_to(point(x, y))
                    number = MathTex(str(table[y][x]), font_size=29, color=YELLOW if (x, y) == (3, 2) else WHITE).move_to(point(x, y))
                    numbers.append(VGroup(disk, number))
            if numbers:
                self.play(*(FadeIn(m) for m in numbers), run_time=.55)
        example = [(0,0),(1,0),(2,0),(2,1),(3,1),(3,2)]
        route = VGroup()
        for (x1,y1),(x2,y2) in zip(example,example[1:]):
            p,q = point(x1,y1), point(x2,y2)
            direction = (q-p)/np.linalg.norm(q-p)
            route.add(Line(p+direction*.35, q-direction*.35, color=YELLOW, stroke_width=6))
        self.play(Create(route), run_time=2)
        clue = Text("每个交点：左边走法 + 下边走法", font=FONT, font_size=26).move_to(DOWN * 4.15)
        answer = MathTex(r"\binom{5}{2}=10", font_size=44, color=YELLOW).move_to(DOWN * 5.15)
        self.play(FadeIn(clue), Write(answer))
        self.wait(2)

"""方格最短路径：主图演示递推，十个微型网格逐一展示十条不同的最短路线。"""
from itertools import combinations
from math import comb
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def path_table(right: int, up: int) -> list[list[int]]:
    if any(type(v) is not int or v < 0 for v in (right, up)):
        raise ValueError("nonnegative integer steps required")
    table = [[0] * (right + 1) for _ in range(up + 1)]
    for y in range(up + 1):
        for x in range(right + 1):
            table[y][x] = 1 if (x, y) == (0, 0) else (table[y-1][x] if y else 0) + (table[y][x-1] if x else 0)
            assert table[y][x] == comb(x + y, x)
    return table


def shortest_routes(right: int, up: int):
    """枚举所有长 right+up 且恰好包含 up 个向上步的最短路线。"""
    if any(type(v) is not int or v < 0 for v in (right, up)):
        raise ValueError("nonnegative integer steps required")
    routes = []
    for ups in combinations(range(right + up), up):
        x = y = 0
        points = [(x, y)]
        for k in range(right + up):
            if k in ups:
                y += 1
            else:
                x += 1
            points.append((x, y))
        assert points[-1] == (right, up)
        routes.append(points)
    return routes


class GridPathScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        table, routes = path_table(3, 2), shortest_routes(3, 2)
        assert len(routes) == table[2][3] == 10
        title = Text("最短路径：十条路看得见", font=FONT, font_size=35).move_to(UP * 6.22)
        question = Text("从左下到右上：只向右 3 步、向上 2 步", font=FONT, font_size=26).move_to(UP * 5.10)
        self.play(Write(title), FadeIn(question))

        def point(x, y):
            return np.array([-2.7 + 1.8*x, -.15 + 1.60*y, 0])

        edges = VGroup()
        for y in range(3):
            for x in range(4):
                if x < 3:
                    edges.add(Line(point(x, y), point(x+1, y), color=GREY_B))
                if y < 2:
                    edges.add(Line(point(x, y), point(x, y+1), color=GREY_B))
        self.play(Create(edges))
        disk_numbers = {}
        for diagonal in range(6):
            group = VGroup()
            for y in range(3):
                x = diagonal-y
                if 0 <= x <= 3:
                    disk = Circle(radius=.30, color=BLUE_B, fill_color=BG, fill_opacity=1).move_to(point(x, y))
                    number = MathTex(str(table[y][x]), font_size=28,
                                     color=YELLOW if (x, y) == (3, 2) else WHITE).move_to(point(x, y))
                    mob = VGroup(disk, number)
                    disk_numbers[x, y] = mob
                    group.add(mob)
            if len(group):
                self.play(FadeIn(group), run_time=.37)
        rule = Text("交点走法 = 左边走法 + 下边走法", font=FONT, font_size=26).move_to(UP * 4.0)
        self.play(FadeIn(rule))
        self.play(Indicate(disk_numbers[3, 2], color=YELLOW))

        def highlighted_route(coords, projector, width=5):
            segs = VGroup()
            for (x0, y0), (x1, y1) in zip(coords, coords[1:]):
                p, q = projector(x0, y0), projector(x1, y1)
                unit = (q-p) / np.linalg.norm(q-p)
                pad = .31 if width >= 5 else .025
                segs.add(Line(p + unit*pad, q-unit*pad, color=YELLOW, stroke_width=width))
            return segs

        # 主图逐条演示三个不同的方向次序。
        for route in routes[:3]:
            lines = highlighted_route(route, point)
            self.play(Create(lines), run_time=.6)
            self.play(FadeOut(lines), run_time=.22)
        thumbnails = VGroup()
        for index, route in enumerate(routes):
            col, row = index % 5, index // 5
            origin = np.array([-3.10 + 1.55*col, -2.02 - 1.68*row, 0])
            tiny = lambda x, y, o=origin: o + np.array([.39*x, .39*y, 0])
            outline = VGroup()
            for yy in range(3):
                for xx in range(4):
                    if xx < 3:
                        outline.add(Line(tiny(xx, yy), tiny(xx+1, yy), color=GREY_D, stroke_width=1.5))
                    if yy < 2:
                        outline.add(Line(tiny(xx, yy), tiny(xx, yy+1), color=GREY_D, stroke_width=1.5))
            path = highlighted_route(route, tiny, width=3)
            index_label = MathTex(str(index+1), font_size=23).move_to(origin + [.59, -.35, 0])
            thumbnails.add(VGroup(outline, path, index_label))
        self.play(LaggedStart(*(FadeIn(m) for m in thumbnails), lag_ratio=.14), run_time=3)
        explain = Text("每一幅小图都是 5 步；向上位置的选择各不相同", font=FONT, font_size=24).move_to(DOWN * 5.06)
        answer = MathTex(r"\binom52=10", font_size=42, color=YELLOW).move_to(DOWN * 6.12)
        self.play(FadeIn(explain), Write(answer))
        self.wait(2)

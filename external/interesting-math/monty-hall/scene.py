"""固定初选的三门实例 + 完整奖品位置概率树（标准主持人规则）。

Render: manim external/interesting-math/monty-hall/scene.py MontyHallScene
"""
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def host_opens(prize, chosen=0):
    if prize not in range(3) or chosen not in range(3):
        raise ValueError("door numbers must be 0, 1 or 2")
    # Any permissible tie-break rule yields the same unconditional switch-win rate.
    return min(set(range(3)) - {prize, chosen})


def switched_door(prize, chosen=0):
    return (set(range(3)) - {chosen, host_opens(prize, chosen)}).pop()


def switch_wins(prize, chosen=0):
    return switched_door(prize, chosen) == prize


class MontyHallScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=17, color=GREY_B).move_to(UP * 7))
        title = Text("三扇门，换不换？", font=FONT,
                     font_size=37).move_to(UP * 6.35)
        rule = Text("奖品等可能；主持人知情且必开另一扇空门", font=FONT,
                    font_size=23).move_to(UP * 5.25)
        self.play(Write(title), FadeIn(rule))

        # Each horizontal picture is an independent, equally likely prize placement.
        grid = VGroup()
        switches = VGroup()
        for prize, y in enumerate((2.9, 0.1, -2.7)):
            header = Text(f"情况 {prize+1}：奖品在 {prize+1} 号门",
                          font=FONT, font_size=23).move_to([0, y + 1.10, 0])
            doors = VGroup()
            for index, x in enumerate((-2.35, 0, 2.35)):
                panel = RoundedRectangle(width=1.38, height=1.40,
                                         corner_radius=0.10,
                                         stroke_color=BLUE_B,
                                         fill_color="#203C60",
                                         fill_opacity=0.9).move_to([x, y, 0])
                number = Text(str(index+1), font_size=29).move_to(panel)
                doors.add(VGroup(panel, number))
            selection = SurroundingRectangle(doors[0], buff=0.08,
                                             color=YELLOW, stroke_width=3)
            opened = host_opens(prize)
            remaining = switched_door(prize)
            # Cover the door number with a genuine opaque plate, not a fake reveal.
            plate = Rectangle(width=1.23, height=1.16,
                              stroke_width=0, fill_color=GREY_E,
                              fill_opacity=1).move_to(doors[opened])
            empty = Text("空门", font=FONT, font_size=26,
                         color=WHITE).move_to(doors[opened])
            reveal = VGroup(plate, empty)
            target = SurroundingRectangle(doors[remaining], buff=0.12,
                                           color=GREEN_C, stroke_width=3)
            shift_arrow = CurvedArrow(
                doors[0].get_bottom()+DOWN*0.13,
                doors[remaining].get_bottom()+DOWN*0.13,
                angle=-0.35, color=GREEN_C, stroke_width=3,
                tip_length=0.16)
            case = VGroup(header, doors, selection, reveal, target, shift_arrow)
            grid.add(case)
            self.play(FadeIn(header), FadeIn(doors), Create(selection),
                      run_time=0.75)
            self.play(FadeIn(reveal), Create(target), Create(shift_arrow),
                      run_time=0.7)
            result = Text("换门赢" if switch_wins(prize) else "换门输",
                          font=FONT, font_size=21,
                          color=GREEN_C if switch_wins(prize) else GREY_B)
            result.next_to(doors, DOWN, buff=0.39)
            self.play(FadeIn(result), run_time=0.3)
            switches.add(result)
        self.wait(0.7)
        self.play(FadeOut(grid), FadeOut(switches), run_time=0.8)

        # Probability tree is a different representation of those SAME three cases.
        root = Text("首次固定选 1 号门", font=FONT,
                    font_size=27).move_to(UP * 3.25)
        self.play(FadeIn(root))
        branches = VGroup()
        for prize, x in enumerate((-2.65, 0, 2.65)):
            top = Text(f"奖品 {prize+1} 号", font=FONT,
                       font_size=25).move_to([x, 1.1, 0])
            branch = Arrow(root.get_bottom()+DOWN*0.14,
                           top.get_top()+UP*0.13, buff=0.08,
                           color=BLUE_B, stroke_width=3, tip_length=0.13)
            weight = MathTex(r"\frac13", font_size=30).move_to(
                branch.point_from_proportion(0.59)+RIGHT*(0.23 if x <= 0 else -0.23))
            leaf = Text("换门赢" if switch_wins(prize) else "换门输",
                        font=FONT, font_size=28,
                        color=GREEN_C if switch_wins(prize) else GREY_B)
            leaf.move_to([x, -1.0, 0])
            connection = Arrow(top.get_bottom()+DOWN*0.09,
                               leaf.get_top()+UP*0.09, buff=0.08,
                               color=GREEN_C if switch_wins(prize) else GREY_B,
                               tip_length=0.13)
            branches.add(VGroup(branch, weight, top, connection, leaf))
        self.play(LaggedStart(*[FadeIn(group) for group in branches],
                              lag_ratio=0.22), run_time=2.5)
        # The lower bar counts initial prize positions, NOT conditional door odds.
        units = VGroup(*[
            Rectangle(width=2.0, height=0.55, stroke_width=2,
                      stroke_color=BACKGROUND,
                      fill_color=GREEN_C if switch_wins(prize) else GREY_D,
                      fill_opacity=0.95).move_to([x, -3.0, 0])
            for prize, x in enumerate((-2, 0, 2))
        ])
        fraction = MathTex(r"P(\mathrm{switch\ wins})=\frac{2}{3}",
                           font_size=41, color=GREEN_C).move_to(DOWN*4.55)
        note = Text("两格获胜，一格失败；前提是主持人总提供换门",
                    font=FONT, font_size=23).move_to(DOWN*5.6)
        self.play(FadeIn(units), Write(fraction), FadeIn(note))
        self.wait(2)

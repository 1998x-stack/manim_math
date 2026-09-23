"""三门实物状态、换门路径与奖品位置的三分支概率树。

标准规则：奖品初始等可能；主持人知道奖品，必开未选空门并提供换门机会。
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
    return min(set(range(3)) - {prize, chosen})


def switched_door(prize, chosen=0):
    return (set(range(3)) - {chosen, host_opens(prize, chosen)}).pop()


def switch_wins(prize, chosen=0):
    return switched_door(prize, chosen) == prize


class MontyHallScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=17, color=GREY_B).move_to(UP*7))
        title = Text("三扇门，换不换？", font=FONT,
                     font_size=37).move_to(UP*6.35)
        rule = Text("奖品等可能；主持人知情且必开另一扇空门",
                    font=FONT, font_size=23).move_to(UP*5.25)
        self.play(Write(title), FadeIn(rule))
        cases = VGroup()
        for prize, y in enumerate((2.9, 0.1, -2.7)):
            header = Text(f"情况 {prize+1}：奖品在 {prize+1} 号门",
                          font=FONT, font_size=22).move_to([-0.45, y+1.06, 0])
            result = Text("换门赢" if switch_wins(prize) else "换门输",
                          font=FONT, font_size=21,
                          color=GREEN_C if switch_wins(prize) else GREY_B
                          ).move_to([3.25, y+1.06, 0])
            doors = VGroup()
            for index, x in enumerate((-2.35, 0, 2.35)):
                shape = RoundedRectangle(width=1.38, height=1.35,
                                         corner_radius=0.1, stroke_color=BLUE_B,
                                         fill_color="#203C60", fill_opacity=0.9
                                         ).move_to([x, y, 0])
                digit = Text(str(index+1), font_size=29).move_to(shape)
                doors.add(VGroup(shape, digit))
            choice = SurroundingRectangle(doors[0], buff=0.07,
                                          color=YELLOW, stroke_width=3)
            opened = host_opens(prize)
            target_door = switched_door(prize)
            cover = Rectangle(width=1.23, height=1.15, stroke_width=0,
                              fill_color=GREY_E, fill_opacity=1).move_to(doors[opened])
            empty = Text("空门", font=FONT, font_size=26).move_to(doors[opened])
            revealed = VGroup(cover, empty)
            target = SurroundingRectangle(doors[target_door], buff=0.10,
                                           color=GREEN_C, stroke_width=3)
            arrow = CurvedArrow(doors[0].get_bottom()+DOWN*0.1,
                                doors[target_door].get_bottom()+DOWN*0.1,
                                angle=-0.28, color=GREEN_C,
                                stroke_width=3, tip_length=0.14)
            self.play(FadeIn(header), FadeIn(doors), Create(choice),
                      run_time=0.7)
            self.play(FadeIn(revealed), Create(target), Create(arrow),
                      FadeIn(result), run_time=0.8)
            cases.add(VGroup(header, doors, choice, revealed, target,
                             arrow, result))
        self.wait(0.6)
        self.play(FadeOut(cases), run_time=0.8)

        root = Text("固定初选 1 号门", font=FONT,
                    font_size=27).move_to(UP*3.25)
        self.play(FadeIn(root))
        branches = VGroup()
        for prize, x in enumerate((-2.65, 0, 2.65)):
            node = Text(f"奖品 {prize+1} 号", font=FONT,
                        font_size=25).move_to([x, 1.10, 0])
            link = Arrow(root.get_bottom()+DOWN*0.14,
                         node.get_top()+UP*0.13, buff=0.08,
                         color=BLUE_B, stroke_width=3, tip_length=0.13)
            probability = MathTex(r"\frac13", font_size=30).move_to(
                link.point_from_proportion(0.59)+RIGHT*(0.23 if x <= 0 else -0.23))
            leaf = Text("换门赢" if switch_wins(prize) else "换门输",
                        font=FONT, font_size=27,
                        color=GREEN_C if switch_wins(prize) else GREY_B
                        ).move_to([x, -1.0, 0])
            down = Arrow(node.get_bottom()+DOWN*0.09,
                         leaf.get_top()+UP*0.09, buff=0.08,
                         color=leaf.get_color(), tip_length=0.13)
            branches.add(VGroup(link, probability, node, down, leaf))
        self.play(LaggedStart(*[FadeIn(group) for group in branches],
                              lag_ratio=0.22), run_time=2.5)
        blocks = VGroup(*[
            Rectangle(width=2.0, height=0.55, stroke_width=2,
                      stroke_color=BACKGROUND,
                      fill_color=GREEN_C if switch_wins(prize) else GREY_D,
                      fill_opacity=0.95).move_to([x, -3.05, 0])
            for prize, x in enumerate((-2, 0, 2))])
        equation = MathTex(r"P(\mathrm{switch\ wins})=\frac{2}{3}",
                           font_size=40, color=GREEN_C).move_to(DOWN*4.55)
        note = Text("两种奖品位置换门赢，一种换门输",
                    font=FONT, font_size=23).move_to(DOWN*5.6)
        self.play(FadeIn(blocks), Write(equation), FadeIn(note))
        self.wait(2)

"""蒙提霍尔：固定初选 1 号门，逐一枚举等可能的奖品位置。

前提：主持人知道奖品位置，必开一扇未选中的空门，且总会提供换门机会。
Render: manim -pql external/interesting-math/monty-hall/scene.py MontyHallScene
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
    # 当有两扇可开的空门时，选编号较小者；不影响最终换门胜率。
    return min(set(range(3)) - {prize, chosen})


def switched_door(prize, chosen=0):
    return (set(range(3)) - {chosen, host_opens(prize, chosen)}).pop()


def switch_wins(prize, chosen=0):
    return switched_door(prize, chosen) == prize


class MontyHallScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        title = Text("三扇门，换不换？", font=FONT, font_size=37).move_to(UP * 6.4)
        rule = Text("先选 1 号门；主持人必开另一扇空门", font=FONT, font_size=24).move_to(UP * 5.35)
        self.play(Write(title), FadeIn(rule))
        rows = []
        for prize, y in enumerate((3.0, 0.0, -3.0)):
            name = Text(f"情况 {prize + 1}：奖品在 {prize + 1} 号门", font=FONT,
                        font_size=24).move_to([0, y + 1.2, 0])
            doors = VGroup()
            for index, x in enumerate((-2.35, 0.0, 2.35)):
                door = RoundedRectangle(width=1.45, height=1.5, corner_radius=0.12,
                                        stroke_color=BLUE_B, fill_color="#1E3A5F",
                                        fill_opacity=0.8).move_to([x, y, 0])
                number = Text(str(index + 1), font_size=30).move_to(door.get_center())
                doors.add(VGroup(door, number))
            initial_choice = SurroundingRectangle(doors[0], color=YELLOW, buff=0.08)
            rows.append((name, doors, initial_choice, prize, y))
        self.play(*[FadeIn(name) for name, _, _, _, _ in rows],
                  *[FadeIn(doors) for _, doors, _, _, _ in rows], run_time=1.5)
        self.play(*[Create(choice) for _, _, choice, _, _ in rows])
        self.wait(0.7)
        opened_labels = []
        switched_labels = []
        for _, doors, _, prize, _ in rows:
            opened = host_opens(prize)
            remaining = switched_door(prize)
            empty_label = Text("空", font=FONT, font_size=34, color=GREY_B).move_to(doors[opened])
            empty_label.add_background_rectangle(color=BACKGROUND, opacity=0.95, buff=0.16)
            new_choice = SurroundingRectangle(doors[remaining], color=GREEN_C, buff=0.11)
            opened_labels.append(empty_label)
            switched_labels.append(new_choice)
        self.play(*[FadeIn(label) for label in opened_labels], run_time=1)
        self.play(*[Create(label) for label in switched_labels], run_time=1)
        outcomes = Text("换门：输 / 赢 / 赢", font=FONT, font_size=32,
                        color=GREEN_C).move_to(DOWN * 5.35)
        note = MathTex(r"P(\mathrm{switch\ wins})=\frac{2}{3}",
                       font_size=39).move_to(DOWN * 6.35)
        self.play(Write(outcomes), Write(note))
        self.wait(2)

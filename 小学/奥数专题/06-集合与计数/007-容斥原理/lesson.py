"""容斥原理：韦恩图内真正画出 8+4+6 个独立成员，交集的四点只数一次。"""
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def union_count(a: int, b: int, both: int) -> int:
    if any(type(v) is not int for v in (a, b, both)):
        raise ValueError("integer counts required")
    if a < 0 or b < 0 or both < 0 or both > min(a, b):
        raise ValueError("invalid intersection count")
    return a + b - both


class InclusionExclusionScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        both, a_only, b_only = 4, 8, 6
        assert union_count(12, 10, both) == a_only + both + b_only == 18
        title = Text("容斥：交叉的成员只算一次", font=FONT, font_size=34).move_to(UP * 6.22)
        question = Text("数学 12 人、科学 10 人；其中两者都喜欢 4 人", font=FONT, font_size=25).move_to(UP * 5.05)
        self.play(Write(title), FadeIn(question))
        cy, r, dx = .67, 2., 1.25
        left_center, right_center = np.array([-dx, cy, 0]), np.array([dx, cy, 0])
        left = Circle(radius=r, color=BLUE_B, fill_color=BLUE_D, fill_opacity=.18).move_to(left_center)
        right = Circle(radius=r, color=GREEN_B, fill_color=GREEN_D, fill_opacity=.18).move_to(right_center)
        self.play(Create(left), Create(right))
        left_points = [(-2.48, y) for y in (-.49, .19, .87, 1.55)] + [(-1.81, y) for y in (-.49, .19, .87, 1.55)]
        center_points = [(-.34, .25), (.34, .25), (-.34, .98), (.34, .98)]
        right_points = [(x, y) for x in (1.78, 2.44) for y in (-.36, .40, 1.16)]
        for points, should_left, should_right in ((left_points, True, False),
                                                  (center_points, True, True),
                                                  (right_points, False, True)):
            for x, y in points:
                p = np.array([x, y, 0])
                assert (np.linalg.norm(p-left_center) < r) == should_left
                assert (np.linalg.norm(p-right_center) < r) == should_right
        l_dots = VGroup(*(Dot((x, y, 0), radius=.105, color=BLUE_B) for x, y in left_points))
        common = VGroup(*(Dot((x, y, 0), radius=.12, color=YELLOW) for x, y in center_points))
        r_dots = VGroup(*(Dot((x, y, 0), radius=.105, color=GREEN_B) for x, y in right_points))
        self.play(LaggedStart(*(FadeIn(d) for d in l_dots), lag_ratio=.07), run_time=1.1)
        self.play(LaggedStart(*(FadeIn(d) for d in common), lag_ratio=.2))
        self.play(LaggedStart(*(FadeIn(d) for d in r_dots), lag_ratio=.12))
        numbers = VGroup(MathTex("8", font_size=34, color=BLUE_B).move_to([-2.16, -1.72, 0]),
                         MathTex("4", font_size=34, color=YELLOW).move_to([0, -1.72, 0]),
                         MathTex("6", font_size=34, color=GREEN_B).move_to([2.16, -1.72, 0]))
        self.play(FadeIn(numbers))
        add_all = MathTex(r"12+10=22", font_size=36, color=RED_B).move_to(DOWN * 2.87)
        duplicate = Text("黄色的 4 人，在两门课人数中各出现一次", font=FONT, font_size=25).move_to(DOWN * 3.85)
        self.play(Write(add_all), Indicate(common, color=YELLOW), FadeIn(duplicate))
        # 从黄色 4 点的实际一一对应，得到 8+4+6 而不是把 4 个人当成 8 人。
        corrected = MathTex(r"8+4+6=18", font_size=39, color=YELLOW).move_to(DOWN * 4.78)
        formula = MathTex(r"12+10-4=18", font_size=39, color=YELLOW).move_to(DOWN * 5.81)
        self.play(Write(corrected), add_all.animate.set_opacity(.35))
        self.play(Write(formula))
        self.wait(2)

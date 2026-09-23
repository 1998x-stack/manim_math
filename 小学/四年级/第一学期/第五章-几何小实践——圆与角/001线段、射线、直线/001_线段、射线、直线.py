"""线段、射线、直线：从端点数和延伸方向区分三种图形。"""
from manim import *

# Configure the portrait frame before Scene constructs its camera.
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SegmentRayLineLesson(Scene):
    """展示线段、射线、直线的实际图形和端点数量。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("线段、射线、直线", font_size=38).to_edge(UP, buff=0.65)
        self.play(Write(title))

        segment = Line(LEFT * 2, RIGHT * 2, color=BLUE)
        segment_ends = VGroup(Dot(segment.get_start()), Dot(segment.get_end()))
        segment_label = Text("线段：两个端点，长度有限", font_size=26)
        segment_group = VGroup(segment, segment_ends, segment_label)
        segment.shift(UP * 2.6)
        segment_ends.move_to(segment)
        segment_label.next_to(segment, DOWN, buff=0.35)
        self.play(Create(segment), FadeIn(segment_ends), Write(segment_label))

        # Arrow shows the ray's one-way extension; the origin is a single dot.
        ray = Arrow(LEFT * 2, RIGHT * 2, buff=0, color=GREEN)
        origin = Dot(ray.get_start(), color=GREEN)
        ray_label = Text("射线：一个端点，向一个方向无限延伸", font_size=22)
        ray_label.next_to(ray, DOWN, buff=0.35)
        self.play(Create(ray), FadeIn(origin), Write(ray_label))

        line = DoubleArrow(LEFT * 2, RIGHT * 2, buff=0, color=YELLOW)
        line.shift(DOWN * 2.5)
        line_label = Text("直线：没有端点，向两个方向无限延伸", font_size=22)
        line_label.next_to(line, DOWN, buff=0.35)
        self.play(Create(line), Write(line_label))
        self.wait(2)


if __name__ == "__main__":
    # manim -ql 001_线段、射线、直线.py SegmentRayLineLesson
    pass

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class MultiplyTableAnimation(Scene):
    """7、8、9的乘法口诀的Manim动画演示"""

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)

        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)

        # 主标题
        title = Text(
            "7、8、9的乘法口诀",
            font="PingFang SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "让我们一起学习吧！",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.wait(1)

        # 隐藏 titles for next section
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.5
        )

        # Section 1: 7的乘法口诀
        self.show_seven_table()

        # Section 2: 8的乘法口诀
        self.show_eight_table()

        # Section 3: 9的乘法口诀
        self.show_nine_table()

        # Section 4: 总结
        self.show_summary()

        # Outro
        self.show_outro()

    def show_seven_table(self):
        """展示7的乘法口诀"""
        header = Text(
            "7的乘法口诀",
            font="PingFang SC",
            font_size=36,
            color=BLUE
        ).move_to(UP * 5.5)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 7的乘法口诀列表
        seven_equations = [
            "1×7=7    一七得七",
            "2×7=14   二七十四",
            "3×7=21   三七二十一",
            "4×7=28   四七二十八",
            "5×7=35   五七三十五",
            "6×7=42   六七四十二",
            "7×7=49   七七四十九"
        ]

        # 创建动画效果展示7的乘法口诀
        for i, eq in enumerate(seven_equations):
            equation = Text(
                eq,
                font="PingFang SC",
                font_size=24,
                color=WHITE
            ).move_to(UP * (3 - i * 0.6))

            # 添加视觉辅助：7个小圆点代表数字7
            dots_group = VGroup()
            for j in range(min(i + 1, 7)):  # 行号表示乘数
                dot_row = VGroup()
                for k in range(7):  # 7列
                    dot = Dot(color=YELLOW).scale(0.8).shift(RIGHT * k * 0.3 + DOWN * j * 0.3)
                    dot_row.add(dot)
                dots_group.add(dot_row)

            # 根据当前公式调整dots的位置
            dots_group.scale(0.4).move_to(LEFT * 2.5 + UP * (3 - i * 0.6))

            self.play(
                Write(equation),
                Create(dots_group),
                run_time=0.8
            )
            self.wait(0.5)

        self.wait(1.5)

        # 清理7的乘法部分
        all_mobjects = [header]
        all_mobjects.extend([obj for obj in self.mobjects if isinstance(obj, Text) and '七' in str(obj) or '×' in str(obj) or '=' in str(obj)])
        self.play(
            *[FadeOut(mob) for mob in all_mobjects if mob in self.mobjects],
            run_time=0.8
        )

    def show_eight_table(self):
        """展示8的乘法口诀"""
        header = Text(
            "8的乘法口诀",
            font="PingFang SC",
            font_size=36,
            color=GREEN
        ).move_to(UP * 5.5)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 8的乘法口诀列表
        eight_equations = [
            "1×8=8    一八得八",
            "2×8=16   二八十六",
            "3×8=24   三八二十四",
            "4×8=32   四八三十二",
            "5×8=40   五八四十",
            "6×8=48   六八四十八",
            "7×8=56   七八五十六",
            "8×8=64   八八六十四"
        ]

        # 创建动画效果展示8的乘法口诀
        for i, eq in enumerate(eight_equations):
            equation = Text(
                eq,
                font="PingFang SC",
                font_size=24,
                color=WHITE
            ).move_to(UP * (2.5 - i * 0.55))

            # 添加视觉辅助：8个小方块代表数字8
            squares_group = VGroup()
            for j in range(min(i + 1, 8)):  # 行号表示乘数
                square_row = VGroup()
                for k in range(8):  # 8列
                    square = Square(side_length=0.25, color=PURPLE, fill_opacity=0.7).shift(RIGHT * k * 0.3 + DOWN * j * 0.3)
                    square_row.add(square)
                squares_group.add(square_row)

            # 根据当前公式调整squares的位置
            squares_group.scale(0.5).move_to(LEFT * 2.5 + UP * (2.5 - i * 0.55))

            self.play(
                Write(equation),
                Create(squares_group),
                run_time=0.8
            )
            self.wait(0.5)

        self.wait(1.5)

        # 清理8的乘法部分
        all_mobjects = [header]
        self.play(
            *[FadeOut(mob) for mob in all_mobjects if mob in self.mobjects],
            run_time=0.8
        )

    def show_nine_table(self):
        """展示9的乘法口诀"""
        header = Text(
            "9的乘法口诀",
            font="PingFang SC",
            font_size=36,
            color=RED
        ).move_to(UP * 5.5)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 9的乘法口诀列表
        nine_equations = [
            "1×9=9     一九得九",
            "2×9=18    二九十八",
            "3×9=27    三九二十七",
            "4×9=36    四九三十六",
            "5×9=45    五九四十五",
            "6×9=54    六九五十四",
            "7×9=63    七九六十三",
            "8×9=72    八九七十二",
            "9×9=81    九九八十一"
        ]

        # 创建动画效果展示9的乘法口诀
        for i, eq in enumerate(nine_equations):
            equation = Text(
                eq,
                font="PingFang SC",
                font_size=22,
                color=WHITE
            ).move_to(UP * (2 - i * 0.45))

            # 添加视觉辅助：9个小星星代表数字9
            stars_group = VGroup()
            for j in range(min(i + 1, 9)):  # 行号表示乘数
                star_row = VGroup()
                for k in range(9):  # 9列
                    star = Star(color=ORANGE, fill_opacity=0.8).scale(0.2).shift(RIGHT * k * 0.25 + DOWN * j * 0.25)
                    star_row.add(star)
                stars_group.add(star_row)

            # 根据当前公式调整stars的位置
            stars_group.scale(0.4).move_to(LEFT * 2.5 + UP * (2 - i * 0.45))

            self.play(
                Write(equation),
                Create(stars_group),
                run_time=0.8
            )
            self.wait(0.5)

        self.wait(1.5)

        # 清理9的乘法部分
        all_mobjects = [header]
        self.play(
            *[FadeOut(mob) for mob in all_mobjects if mob in self.mobjects],
            run_time=0.8
        )

    def show_summary(self):
        """总结7、8、9的乘法口诀"""
        title = Text(
            "7、8、9的乘法口诀总结",
            font="PingFang SC",
            font_size=36,
            color=YELLOW
        ).move_to(UP * 6)

        self.play(Write(title), run_time=0.8)

        # 显示关键口诀
        key_formulas = [
            Text("七七四十九", font="PingFang SC", font_size=28, color=BLUE).move_to(UP * 4),
            Text("八八六十四", font="PingFang SC", font_size=28, color=GREEN).move_to(UP * 3),
            Text("九九八十一", font="PingFang SC", font_size=28, color=RED).move_to(UP * 2),
            Text("七八五十六", font="PingFang SC", font_size=28, color=PURPLE).move_to(UP * 1),
            Text("八九七十二", font="PingFang SC", font_size=28, color=ORANGE).move_to(ORIGIN)
        ]

        for formula in key_formulas:
            self.play(Write(formula), run_time=0.6)
            self.wait(0.4)

        # 有趣的规律
        pattern_text = Text(
            "有趣的规律：\n\n9的口诀中，十位数字递增，个位数字递减",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2.5)

        self.play(Write(pattern_text), run_time=1.0)
        self.wait(2)

        # 清理总结部分
        all_mobjects = [title] + key_formulas + [pattern_text]
        self.play(
            *[FadeOut(mob) for mob in all_mobjects if mob in self.mobjects],
            run_time=0.8
        )

    def show_outro(self):
        """片尾"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(Write(author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 小星星装饰
        stars = VGroup(*[
            Star(color=GOLD, fill_opacity=0.8).scale(0.3)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]))
            for i in range(8)
        ])

        self.play(
            *[GrowFromCenter(star) for star in stars],
            run_time=0.6
        )
        self.play(Rotate(stars, angle=PI, run_time=1.5))

        self.wait(2)


class Star(Polygon):
    """自定义星形类"""
    def __init__(self, color=YELLOW, fill_opacity=1, **kwargs):
        outer_points = []
        inner_points = []

        for i in range(5):
            angle = PI/2 + i * 2*PI/5
            outer_points.append([np.cos(angle), np.sin(angle), 0])

        for i in range(5):
            angle = PI/2 + (i + 0.5) * 2*PI/5
            inner_points.append([0.4*np.cos(angle), 0.4*np.sin(angle), 0])

        points = []
        for i in range(5):
            points.append(outer_points[i])
            points.append(inner_points[(i + 1) % 5])

        super().__init__(*points, color=color, fill_opacity=fill_opacity, **kwargs)


if __name__ == "__main__":
    # 运行命令: manim -pql "001_7、8、9的乘法口诀.py" MultiplyTableAnimation
    scene = MultiplyTableAnimation()
    scene.render()

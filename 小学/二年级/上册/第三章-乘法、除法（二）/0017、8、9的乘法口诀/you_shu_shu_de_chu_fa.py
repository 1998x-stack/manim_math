from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class MultiplicationTableAnimation(Scene):
    """7、8、9的乘法口诀动画 - 改进版"""

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 作者信息 (顶部) - keep this as an instance variable to manage its lifecycle
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 主标题
        title = Text(
            "7、8、9的乘法口诀",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "乘法口诀要熟记哦！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.wait(1)

        # 清理 titles for next section but keep author info
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.5
        )
        # Actually remove these from the scene
        self.remove(title)
        self.remove(subtitle)

        # Section 1: 7的乘法口诀
        self.show_seven_table()

        # Section 2: 8的乘法口诀
        self.show_eight_table()

        # Section 3: 9的乘法口诀
        self.show_nine_table()

        # Section 4: 有趣的规律
        self.show_interesting_patterns()

        # Section 5: 记忆技巧
        self.show_memory_techniques()

        # Section 6: 总结
        self.show_summary()

        # Section 7: Outro
        self.show_outro()

    def show_seven_table(self):
        """展示7的乘法口诀"""
        header = Text(
            "7的乘法口诀",
            font="Noto Sans CJK SC",
            font_size=36,
            color=BLUE
        ).move_to(UP * 5.5)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 7的乘法口诀列表
        seven_equations = [
            ("1×7=7", "一七得七"),
            ("2×7=14", "二七十四"),
            ("3×7=21", "三七二十一"),
            ("4×7=28", "四七二十八"),
            ("5×7=35", "五七三十五"),
            ("6×7=42", "六七四十二"),
            ("7×7=49", "七七四十九")
        ]

        # 存储动态创建的对象用于清理
        all_dynamic_objects = [header]

        # 创建动画效果展示7的乘法口诀
        for i, (num_eq, chi_eq) in enumerate(seven_equations):
            # 创建两个文本对象
            num_text = Text(num_eq, font="Noto Sans CJK SC", font_size=24, color=WHITE)
            chi_text = Text(chi_eq, font="Noto Sans CJK SC", font_size=22, color=GRAY_A)

            # 组合成一行
            equation = VGroup(num_text, chi_text).arrange(RIGHT, buff=1)
            # Improved vertical spacing to prevent overlapping
            equation.move_to(UP * (2.5 - i * 1.0))

            # 添加视觉辅助：7个小圆点代表数字7
            dots_group = VGroup()
            for j in range(i + 1):  # 行号表示乘数
                dot_row = VGroup()
                for k in range(7):  # 7列代表7
                    dot = Dot(color=YELLOW).scale(0.6).shift(RIGHT * k * 0.25 + DOWN * j * 0.25)
                    dot_row.add(dot)
                dots_group.add(dot_row)

            # 根据当前公式调整dots的位置 - further to the left to avoid overlapping
            dots_group.scale(0.3).move_to(LEFT * 3.5 + UP * (2.5 - i * 1.0))

            self.play(
                Write(equation),
                Create(dots_group),
                run_time=0.8
            )

            # 将创建的对象添加到清理列表中
            all_dynamic_objects.append(equation)
            all_dynamic_objects.append(dots_group)

            self.wait(0.5)

        self.wait(1.5)

        # 清理7的乘法部分 - 使用FadeOut动画然后remove
        self.play(
            *[FadeOut(mob) for mob in all_dynamic_objects if mob in self.mobjects],
            run_time=0.8
        )
        # 确保所有对象都被从场景中移除
        for mob in all_dynamic_objects:
            if mob in self.mobjects:
                self.remove(mob)

    def show_eight_table(self):
        """展示8的乘法口诀"""
        header = Text(
            "8的乘法口诀",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GREEN
        ).move_to(UP * 5.5)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 8的乘法口诀列表
        eight_equations = [
            ("1×8=8", "一八得八"),
            ("2×8=16", "二八十六"),
            ("3×8=24", "三八二十四"),
            ("4×8=32", "四八三十二"),
            ("5×8=40", "五八四十"),
            ("6×8=48", "六八四十八"),
            ("7×8=56", "七八五十六"),
            ("8×8=64", "八八六十四")
        ]

        # 存储动态创建的对象用于清理
        all_dynamic_objects = [header]

        # 创建动画效果展示8的乘法口诀
        for i, (num_eq, chi_eq) in enumerate(eight_equations):
            # 创建两个文本对象
            num_text = Text(num_eq, font="Noto Sans CJK SC", font_size=24, color=WHITE)
            chi_text = Text(chi_eq, font="Noto Sans CJK SC", font_size=22, color=GRAY_A)

            # 组合成一行
            equation = VGroup(num_text, chi_text).arrange(RIGHT, buff=1)
            # Improved vertical spacing to prevent overlapping
            equation.move_to(UP * (2.0 - i * 0.9))

            # 添加视觉辅助：8个小方块代表数字8
            squares_group = VGroup()
            for j in range(i + 1):  # 行号表示乘数
                square_row = VGroup()
                for k in range(8):  # 8列代表8
                    square = Square(side_length=0.2, color=PURPLE, fill_opacity=0.7).shift(RIGHT * k * 0.25 + DOWN * j * 0.25)
                    square_row.add(square)
                squares_group.add(square_row)

            # 根据当前公式调整squares的位置 - further to the left to avoid overlapping
            squares_group.scale(0.3).move_to(LEFT * 3.5 + UP * (2.0 - i * 0.9))

            self.play(
                Write(equation),
                Create(squares_group),
                run_time=0.8
            )

            # 将创建的对象添加到清理列表中
            all_dynamic_objects.append(equation)
            all_dynamic_objects.append(squares_group)

            self.wait(0.5)

        self.wait(1.5)

        # 清理8的乘法部分 - 使用FadeOut动画然后remove
        self.play(
            *[FadeOut(mob) for mob in all_dynamic_objects if mob in self.mobjects],
            run_time=0.8
        )
        # 确保所有对象都被从场景中移除
        for mob in all_dynamic_objects:
            if mob in self.mobjects:
                self.remove(mob)

    def show_nine_table(self):
        """展示9的乘法口诀"""
        header = Text(
            "9的乘法口诀",
            font="Noto Sans CJK SC",
            font_size=36,
            color=RED
        ).move_to(UP * 5.5)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 9的乘法口诀列表
        nine_equations = [
            ("1×9=9", "一九得九"),
            ("2×9=18", "二九十八"),
            ("3×9=27", "三九二十七"),
            ("4×9=36", "四九三十六"),
            ("5×9=45", "五九四十五"),
            ("6×9=54", "六九五十四"),
            ("7×9=63", "七九六十三"),
            ("8×9=72", "八九七十二"),
            ("9×9=81", "九九八十一")
        ]

        # 存储动态创建的对象用于清理
        all_dynamic_objects = [header]

        # 创建动画效果展示9的乘法口诀
        for i, (num_eq, chi_eq) in enumerate(nine_equations):
            # 创建两个文本对象
            num_text = Text(num_eq, font="Noto Sans CJK SC", font_size=22, color=WHITE)
            chi_text = Text(chi_eq, font="Noto Sans CJK SC", font_size=20, color=GRAY_A)

            # 组合成一行
            equation = VGroup(num_text, chi_text).arrange(RIGHT, buff=1)
            # Improved vertical spacing to prevent overlapping
            equation.move_to(UP * (1.5 - i * 0.8))

            # 添加视觉辅助：9个小星星代表数字9
            stars_group = VGroup()
            for j in range(i + 1):  # 行号表示乘数
                star_row = VGroup()
                for k in range(9):  # 9列代表9
                    star = Star(color=ORANGE, fill_opacity=0.8).scale(0.1).shift(RIGHT * k * 0.2 + DOWN * j * 0.2)
                    star_row.add(star)
                stars_group.add(star_row)

            # 根据当前公式调整stars的位置 - further to the left to avoid overlapping
            stars_group.scale(0.25).move_to(LEFT * 3.5 + UP * (1.5 - i * 0.8))

            self.play(
                Write(equation),
                Create(stars_group),
                run_time=0.8
            )

            # 将创建的对象添加到清理列表中
            all_dynamic_objects.append(equation)
            all_dynamic_objects.append(stars_group)

            self.wait(0.5)

        self.wait(1.5)

        # 清理9的乘法部分 - 使用FadeOut动画然后remove
        self.play(
            *[FadeOut(mob) for mob in all_dynamic_objects if mob in self.mobjects],
            run_time=0.8
        )
        # 确保所有对象都被从场景中移除
        for mob in all_dynamic_objects:
            if mob in self.mobjects:
                self.remove(mob)

    def show_interesting_patterns(self):
        """展示有趣的规律"""
        header = Text(
            "有趣的规律",
            font="Noto Sans CJK SC",
            font_size=36,
            color=YELLOW
        ).move_to(UP * 6)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        # 9的规律：9的倍数，十位数递增，个位数递减
        nine_pattern = Text(
            "9的乘法规律：\n\n1×9=09 (0+9=9)\n2×9=18 (1+8=9)\n3×9=27 (2+7=9)\n...\n9×9=81 (8+1=9)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=WHITE,
            line_spacing=1.5
        ).move_to(UP * 2)

        self.play(Write(nine_pattern), run_time=1.5)
        self.wait(1)

        # 用动画展示手指数数9的倍数方法
        finger_text = Text(
            "手指记忆法：弯曲第n根手指，\n左边手指数是十位，右边是各位",
            font="Noto Sans CJK SC",
            font_size=18,
            color=WHITE
        ).move_to(DOWN * 1)

        self.play(Write(finger_text), run_time=1.0)
        self.wait(2)

        # 清理规律部分 - 所有创建的对象
        all_dynamic_objects = [header, nine_pattern, finger_text]
        self.play(
            *[FadeOut(mob) for mob in all_dynamic_objects if mob in self.mobjects],
            run_time=0.8
        )
        # 确保所有对象都被从场景中移除
        for mob in all_dynamic_objects:
            if mob in self.mobjects:
                self.remove(mob)

    def show_memory_techniques(self):
        """展示记忆技巧"""
        header = Text(
            "记忆技巧",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GREEN
        ).move_to(UP * 6)

        self.play(Write(header), run_time=0.8)
        self.wait(0.5)

        techniques = [
            "1. 逐句背诵：每天背几句话",
            "2. 与实物联系：用小物品计数",
            "3. 找规律：如9的乘法口诀规律",
            "4. 反复练习：多做乘法题"
        ]

        tech_group = VGroup()
        for i, tech in enumerate(techniques):
            tech_text = Text(tech, font="Noto Sans CJK SC", font_size=20, color=WHITE).move_to(UP * (1.5 - i * 0.8))
            tech_group.add(tech_text)

        for tech_text in tech_group:
            self.play(Write(tech_text), run_time=0.6)
            self.wait(0.4)

        self.wait(2)

        # 清理技巧部分 - 包括头和所有技术点
        all_dynamic_objects = [header]
        all_dynamic_objects.extend([obj for obj in tech_group])
        self.play(
            *[FadeOut(mob) for mob in all_dynamic_objects if mob in self.mobjects],
            run_time=0.8
        )
        # 确保所有对象都被从场景中移除
        for mob in all_dynamic_objects:
            if mob in self.mobjects:
                self.remove(mob)

    def show_summary(self):
        """总结7、8、9的乘法口诀"""
        title = Text(
            "复习时间！",
            font="Noto Sans CJK SC",
            font_size=40,
            color=YELLOW
        ).move_to(UP * 6)

        self.play(Write(title), run_time=0.8)

        # 快速回顾关键口诀
        key_formulas = [
            Text("七七四十九", font="Noto Sans CJK SC", font_size=28, color=BLUE).move_to(UP * 3.5),
            Text("八八六十四", font="Noto Sans CJK SC", font_size=28, color=GREEN).move_to(UP * 2.5),
            Text("九九八十一", font="Noto Sans CJK SC", font_size=28, color=RED).move_to(UP * 1.5),
            Text("七八五十六", font="Noto Sans CJK SC", font_size=28, color=PURPLE).move_to(UP * 0.5),
            Text("八九七十二", font="Noto Sans CJK SC", font_size=28, color=ORANGE).move_to(DOWN * 0.5)
        ]

        for i, formula in enumerate(key_formulas):
            if i == 0:
                self.play(Write(formula), run_time=0.6)
            else:
                self.play(Write(formula), run_time=0.4)
            self.wait(0.4)

        # 鼓励语
        encourage = Text(
            "加油！熟记乘法口诀，\n数学学习更轻松！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN,
            line_spacing=1.5
        ).move_to(DOWN * 2.5)

        self.play(Write(encourage), run_time=1.0)
        self.wait(2)

        # 清理总结部分 - 包括标题、公式和鼓励语
        all_dynamic_objects = [title]
        all_dynamic_objects.extend(key_formulas)
        all_dynamic_objects.append(encourage)
        self.play(
            *[FadeOut(mob) for mob in all_dynamic_objects if mob in self.mobjects],
            run_time=0.8
        )
        # 确保所有对象都被从场景中移除
        for mob in all_dynamic_objects:
            if mob in self.mobjects:
                self.remove(mob)

    def show_outro(self):
        """片尾"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.2)

        self.play(Write(author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 小星星装饰
        stars = VGroup(*[
            Star(color=GOLD, fill_opacity=0.8).scale(0.3)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]))
            for i in range(8)
        ])

        self.play(
            *[GrowFromCenter(star) for star in stars],
            run_time=0.6
        )
        self.play(Rotate(stars, angle=PI, run_time=1.5))

        # 最后清理所有对象 before ending
        all_final_objects = [author_name, author_id, follow_text, stars]

        self.wait(3)

        # 清理最后的所有对象
        for mob in all_final_objects:
            if mob in self.mobjects:
                self.remove(mob)


class Star(Polygon):
    """自定义星形类"""
    def __init__(self, color=YELLOW, fill_opacity=1, **kwargs):
        outer_points = []
        inner_points = []

        for i in range(5):
            angle = PI/2 + i * 2*PI/5
            outer_points.append([0.8*np.cos(angle), 0.8*np.sin(angle), 0])

        for i in range(5):
            angle = PI/2 + (i + 0.5) * 2*PI/5
            inner_points.append([0.3*np.cos(angle), 0.3*np.sin(angle), 0])

        points = []
        for i in range(5):
            points.append(outer_points[i])
            points.append(inner_points[(i + 1) % 5])

        super().__init__(*points, color=color, fill_opacity=fill_opacity, **kwargs)


if __name__ == "__main__":
    # 运行命令: manim -pql "you_shu_shu_de_chu_fa.py" MultiplicationTableAnimation
    scene = MultiplicationTableAnimation()
    scene.render()